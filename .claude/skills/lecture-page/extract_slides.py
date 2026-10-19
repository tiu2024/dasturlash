"""Print the text of every slide in a .pptx file, in slide order.

Usage: .venv/Scripts/python.exe extract_slides.py "Lectures/N_Mavzu.pptx"

Uses only the standard library. Each paragraph is printed on its own line,
so code on the slides keeps its line breaks.
"""

import re
import sys
import zipfile
import xml.etree.ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def slide_number(name):
    return int(re.search(r"slide(\d+)\.xml$", name).group(1))


def slide_lines(xml_bytes):
    root = ET.fromstring(xml_bytes)
    lines = []
    for paragraph in root.iter(f"{A}p"):
        parts = []
        for node in paragraph.iter():
            if node.tag == f"{A}t" and node.text:
                parts.append(node.text)
            elif node.tag == f"{A}br":
                parts.append("\n")
        text = "".join(parts)
        if text.strip():
            lines.append(text)
    return lines


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)

    sys.stdout.reconfigure(encoding="utf-8")

    with zipfile.ZipFile(sys.argv[1]) as pptx:
        names = [
            n for n in pptx.namelist()
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)
        ]
        for name in sorted(names, key=slide_number):
            print(f"===== Slide {slide_number(name)}")
            for line in slide_lines(pptx.read(name)):
                print(line)
            print()


main()
