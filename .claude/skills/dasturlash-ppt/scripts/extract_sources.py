#!/usr/bin/env python3
"""Extract lecture source material (book PDF excerpts, text/Markdown notes, code files) into a work folder.

Usage (from the project root):
  .venv/Scripts/python.exe .claude/skills/dasturlash-ppt/scripts/extract_sources.py Lectures/src/week-NN/materials -o Lectures/src/week-NN/build/sources [--render 12,14-15]

Creates:
  sources/index.md            what was found: pages, figures (with size), code files; read this first
  sources/text/<name>.md      text per PDF with "--- page N ---" markers (page numbers = PDF pages)
  sources/figures/<name>-pN-k.png   embedded images >= --min-img px (candidate figures)
  sources/pages/<name>-pN.png       full-page renders for --render pages (crop figures from these)
  sources/notes/, sources/code/     copies of text/Markdown and code inputs

Backends, in order of preference: PyMuPDF (fitz) > poppler tools (pdftotext/pdfimages/pdftoppm) > pypdf.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

TEXT_EXT = {".md", ".markdown", ".txt", ".rst", ".tex"}
CODE_EXT = {".py", ".java", ".c", ".h", ".cpp", ".hpp", ".cc", ".js", ".ts", ".go", ".rs", ".kt", ".cs", ".rb",
            ".sql", ".sh", ".scala", ".swift", ".php", ".hs", ".ml", ".r", ".m", ".ipynb"}


def page_spec(s):
    out = set()
    for part in (s or "").split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return sorted(out)


def have(cmd):
    return shutil.which(cmd) is not None


def pdf_with_fitz(pdf, out, render, min_img):
    try:
        import pymupdf as fitz
    except ImportError:
        import fitz  # older PyMuPDF
    doc = fitz.open(pdf)
    stem = pdf.stem
    text, figs, seen = [], [], set()
    for i, page in enumerate(doc, start=1):
        text.append(f"\n--- page {i} ---\n{page.get_text('text')}")
        drawn = [info.get("xref", 0) for info in page.get_image_info(xrefs=True)]  # images actually on this page
        for k, xref in enumerate(dict.fromkeys(x for x in drawn if x), start=1):
            if xref in seen:  # same image repeated (logos, running headers)
                continue
            seen.add(xref)
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha >= 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                if min(pix.width, pix.height) >= min_img:
                    p = out / "figures" / f"{stem}-p{i}-{k}.png"
                    pix.save(p)
                    figs.append((p, i, pix.width, pix.height))
            except Exception as e:  # noqa: BLE001
                print(f"  skip image p{i}#{k}: {e}", file=sys.stderr)
    pages = []
    for n in render:
        if 1 <= n <= len(doc):
            p = out / "pages" / f"{stem}-p{n}.png"
            doc[n - 1].get_pixmap(dpi=200).save(p)
            pages.append(p)
    return "".join(text), figs, pages, len(doc)


def pdf_with_poppler(pdf, out, render, min_img):
    stem = pdf.stem
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout if have("pdfinfo") else ""
    n_pages = next((int(l.split()[-1]) for l in info.splitlines() if l.startswith("Pages:")), 0)
    text = []
    for i in range(1, n_pages + 1):
        t = subprocess.run(["pdftotext", "-layout", "-f", str(i), "-l", str(i), str(pdf), "-"],
                           capture_output=True, text=True).stdout
        text.append(f"\n--- page {i} ---\n{t}")
    figs = []
    if have("pdfimages"):
        tmp = out / "figures" / f".{stem}"
        tmp.mkdir(parents=True, exist_ok=True)
        listing = subprocess.run(["pdfimages", "-list", str(pdf)], capture_output=True, text=True).stdout
        masks = {int(l.split()[1]) for l in listing.splitlines()[2:]
                 if len(l.split()) > 2 and l.split()[2] in ("smask", "mask", "stencil")}
        subprocess.run(["pdfimages", "-png", "-p", str(pdf), str(tmp / "img")], check=False)
        from PIL import Image
        for f in sorted(tmp.glob("img-*.png")):
            parts = f.stem.split("-")  # img-PAGE-NUM
            pg = int(parts[1])
            if int(parts[2]) in masks:  # transparency masks, not figures
                continue
            with Image.open(f) as im:
                w, h = im.size
            if min(w, h) >= min_img:
                dest = out / "figures" / f"{stem}-p{pg}-{int(parts[2]) + 1}.png"
                f.replace(dest)
                figs.append((dest, pg, w, h))
        shutil.rmtree(tmp, ignore_errors=True)
    pages = []
    if have("pdftoppm"):
        for n in render:
            base = out / "pages" / f"{stem}-p{n}"
            subprocess.run(["pdftoppm", "-png", "-r", "200", "-f", str(n), "-l", str(n), "-singlefile", str(pdf),
                            str(base)], check=False)
            if base.with_suffix(".png").exists():
                pages.append(base.with_suffix(".png"))
    return "".join(text), figs, pages, n_pages


def pdf_with_pypdf(pdf, out, render, min_img):
    """Last-resort backend: text only. Image decoding in pypdf can take minutes on some PDFs."""
    from pypdf import PdfReader
    reader = PdfReader(str(pdf))
    text = [f"\n--- page {i} ---\n{page.extract_text() or ''}" for i, page in enumerate(reader.pages, start=1)]
    print("  pypdf backend: text only. For figures and page renders: pip install pymupdf", file=sys.stderr)
    return "".join(text), [], [], len(reader.pages)


def extract_pdf(pdf, out, render, min_img):
    import importlib.util
    if importlib.util.find_spec("pymupdf") or importlib.util.find_spec("fitz"):
        return pdf_with_fitz(pdf, out, render, min_img)
    if have("pdftotext"):
        return pdf_with_poppler(pdf, out, render, min_img)
    return pdf_with_pypdf(pdf, out, render, min_img)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sources", nargs="+", type=Path)
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--render", default="", help="PDF pages to render as full-page PNGs, e.g. 12,14-15")
    ap.add_argument("--min-img", type=int, default=300, help="skip embedded images smaller than this (px)")
    args = ap.parse_args()

    out = args.out
    for sub in ("text", "figures", "pages", "notes", "code"):
        (out / sub).mkdir(parents=True, exist_ok=True)
    render = page_spec(args.render)
    index = ["# Lecture sources", ""]

    files = []
    for s in args.sources:
        files += sorted(p for p in s.rglob("*") if p.is_file()) if s.is_dir() else [s]

    for f in files:
        ext = f.suffix.lower()
        if ext == ".pdf":
            print(f"PDF  {f}")
            text, figs, pages, n = extract_pdf(f, out, render, args.min_img)
            tp = out / "text" / f"{f.stem}.md"
            tp.write_text(text, encoding="utf-8")
            words = len(text.split())
            index += [f"## {f.name} ({n} pages, ~{words} words)", f"- text: `{tp.relative_to(out)}`"]
            if words < 30 * max(n, 1):
                index.append("- WARNING: very little text; the PDF may be scanned. OCR it (e.g. `ocrmypdf`) or "
                             "render pages with --render and read them as images.")
            for p, pg, w, h in figs:
                index.append(f"- figure p{pg}: `{p.relative_to(out)}` ({w}×{h})")
            for p in pages:
                index.append(f"- page render: `{p.relative_to(out)}`")
            index.append("")
        elif ext in TEXT_EXT:
            dest = out / "notes" / f.name
            shutil.copy2(f, dest)
            index += [f"## {f.name}", f"- notes: `{dest.relative_to(out)}` ({len(f.read_text(errors='ignore').split())} words)", ""]
        elif ext in CODE_EXT:
            dest = out / "code" / f.name
            shutil.copy2(f, dest)
            n_lines = len(f.read_text(errors="ignore").splitlines())
            index += [f"## {f.name}", f"- code: `{dest.relative_to(out)}` ({n_lines} lines)", ""]
        elif ext in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
            dest = out / "figures" / f.name
            shutil.copy2(f, dest)
            index += [f"- figure: `{dest.relative_to(out)}`"]
        else:
            print(f"skip {f} (unsupported type)", file=sys.stderr)

    (out / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"\nIndex: {out / 'index.md'}")


if __name__ == "__main__":
    main()
