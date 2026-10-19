#!/usr/bin/env python3
"""Render a deck to PDF + slide PNGs + a contact sheet for visual checking, and list animations per slide.

Usage (from the project root):
  .venv/Scripts/python.exe .claude/skills/dasturlash-ppt/scripts/render_preview.py DECK.pptx --out Lectures/src/week-NN/build/preview

Static renders show every build step at once (the final state of each slide), which is exactly
what you need to check for overflow and overlaps. Needs LibreOffice for the PDF step.
"""
import argparse
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


def find_soffice(explicit=None):
    if explicit and Path(explicit).exists():
        return explicit
    for name in ("soffice", "libreoffice"):
        p = shutil.which(name)
        if p:
            return p
    candidates = {
        "Darwin": ["/Applications/LibreOffice.app/Contents/MacOS/soffice"],
        "Windows": [r"C:\Program Files\LibreOffice\program\soffice.exe",
                    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"],
    }.get(platform.system(), [])
    return next((c for c in candidates if Path(c).exists()), None)


def animation_report(pptx: Path):
    rows = []
    with zipfile.ZipFile(pptx) as z:
        names = sorted((n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)),
                       key=lambda n: int(re.findall(r"\d+", n)[-1]))
        for n in names:
            xml = z.read(n).decode("utf-8", "ignore")
            clicks = xml.count('delay="indefinite"')
            rows.append((int(re.findall(r"\d+", n)[-1]), clicks, "p:transition" in xml))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pptx", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--dpi", type=int, default=80)
    ap.add_argument("--soffice", help="path to soffice(.exe), e.g. from config.yaml paths.libreoffice")
    args = ap.parse_args()

    pptx = args.pptx.resolve()
    out = (args.out or pptx.parent / "preview").resolve()
    out.mkdir(parents=True, exist_ok=True)

    print("Clicks per slide:")
    print("  " + "  ".join(f"{n}:{c}" for n, c, _ in animation_report(pptx)))

    soffice = find_soffice(args.soffice)
    if not soffice:
        sys.exit("LibreOffice not found; install it to render previews (the .pptx itself is fine).")
    profile = Path(tempfile.mkdtemp(prefix="lo-profile-"))
    env = dict(os.environ, HOME=str(profile))
    subprocess.run([soffice, f"-env:UserInstallation={profile.as_uri()}", "--headless", "--convert-to", "pdf",
                    "--outdir", str(out), str(pptx)], check=True, env=env, timeout=300,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = out / (pptx.stem + ".pdf")
    for old in out.glob("slide-*.png"):
        old.unlink()

    pngs = []
    try:
        import pymupdf as fitz
        doc = fitz.open(pdf)
        for i, page in enumerate(doc, start=1):
            p = out / f"slide-{i:02d}.png"
            page.get_pixmap(dpi=args.dpi).save(p)
            pngs.append(p)
    except ImportError:
        if not shutil.which("pdftoppm"):
            sys.exit(f"PDF written to {pdf}; install PyMuPDF or poppler for PNGs.")
        subprocess.run(["pdftoppm", "-png", "-r", str(args.dpi), str(pdf), str(out / "slide")], check=True)
        for p in sorted(out.glob("slide-*.png")):
            num = int(re.findall(r"\d+", p.stem)[-1])
            dest = out / f"slide-{num:02d}.png"
            if p != dest:
                p.replace(dest)
            pngs.append(dest)
        pngs.sort()

    from PIL import Image, ImageDraw
    thumbs = [Image.open(p) for p in pngs]
    if thumbs:
        tw = 400
        th = int(thumbs[0].height * tw / thumbs[0].width)
        cols = 4
        sheet = Image.new("RGB", (cols * (tw + 10) + 10, ((len(thumbs) + cols - 1) // cols) * (th + 30) + 10), "white")
        d = ImageDraw.Draw(sheet)
        for i, im in enumerate(thumbs):
            r, c = divmod(i, cols)
            x, y = 10 + c * (tw + 10), 10 + r * (th + 30)
            sheet.paste(im.resize((tw, th)), (x, y + 20))
            d.text((x, y + 4), f"{i + 1}", fill="black")
        sheet_path = out / "contact-sheet.png"
        sheet.save(sheet_path)
        print(f"Contact sheet: {sheet_path}")
    print(f"PDF: {pdf}")
    print(f"{len(pngs)} slide images in {out}")


if __name__ == "__main__":
    main()
