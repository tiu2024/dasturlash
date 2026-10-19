"""Print the text of every slide in a .pptx file, in slide order.

Usage: .venv/Scripts/python.exe extract_slides.py "Lectures/N_Mavzu.pptx" [--notes]

Uses only the standard library. Each paragraph is printed on its own line,
so code on the slides keeps its line breaks. Line-number boxes of code
panels are skipped. With --notes, each slide's speaker notes follow its text.
"""

import posixpath
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
R = "{http://schemas.openxmlformats.org/package/2006/relationships}"
SKIP_SHAPES = {"Line numbers"}


def slide_number(name):
    return int(re.search(r"slide(\d+)\.xml$", name).group(1))


def paragraph_text(paragraph):
    parts = []
    for node in paragraph.iter():
        if node.tag == f"{A}t" and node.text:
            parts.append(node.text)
        elif node.tag == f"{A}br":
            parts.append("\n")
    return "".join(parts)


def shape_name(shape):
    for node in shape.iter(f"{P}cNvPr"):
        return node.get("name", "")
    return ""


def collect(node, lines, only_body=False):
    if node.tag == f"{P}sp":
        if shape_name(node) in SKIP_SHAPES:
            return
        if only_body:
            ph = next(node.iter(f"{P}ph"), None)
            if ph is None or ph.get("type") != "body":
                return
    if node.tag == f"{A}p":
        text = paragraph_text(node)
        if text.strip():
            lines.append(text)
        return
    for child in node:
        collect(child, lines, only_body)


def slide_lines(xml_bytes, only_body=False):
    lines = []
    collect(ET.fromstring(xml_bytes), lines, only_body)
    return lines


def notes_part(pptx, slide_name):
    rels = posixpath.join(posixpath.dirname(slide_name), "_rels", posixpath.basename(slide_name) + ".rels")
    if rels not in pptx.namelist():
        return None
    for rel in ET.fromstring(pptx.read(rels)).iter(f"{R}Relationship"):
        if rel.get("Type", "").endswith("/notesSlide"):
            return posixpath.normpath(posixpath.join(posixpath.dirname(slide_name), rel.get("Target")))
    return None


def main():
    args = [a for a in sys.argv[1:] if a != "--notes"]
    if len(args) != 1:
        sys.exit(__doc__)
    show_notes = "--notes" in sys.argv[1:]

    sys.stdout.reconfigure(encoding="utf-8")

    with zipfile.ZipFile(args[0]) as pptx:
        names = [
            n for n in pptx.namelist()
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)
        ]
        for name in sorted(names, key=slide_number):
            print(f"===== Slide {slide_number(name)}")
            for line in slide_lines(pptx.read(name)):
                print(line)
            if show_notes:
                part = notes_part(pptx, name)
                notes = slide_lines(pptx.read(part), only_body=True) if part else []
                if notes:
                    print("----- notes")
                    for line in notes:
                        print(line)
            print()


main()
