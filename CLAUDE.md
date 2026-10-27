# Dasturlash 1, 2 — course workspace

## Who and what

I. J. Husainov teaches the first-year course "Dasturlash 1, 2" at Turan International University (ATT-2026). Teaching language: Uzbek (Latin script). Python now, C later.

This folder is my workspace for the course: the public student website and, kept private, official university documents. I add automation one feature at a time.

Talk to me in simple, clear English. Student-facing content is in Uzbek.

## Public and private

- The GitHub repository and the website are public. Everything in `docs/` is published, including files missing from navigation.
- Never put private, official or unreleased material in `docs/` or in any committed file. Official documents live in `OQ/`.
- `OQ/` and the `oquv-dastur` and `adabiyot-tanlash` skills are gitignored: they exist only on this computer.

## AXV project (private)

- I also mentor 8th graders in the "Muhammad al-Xorazmiy vorislari" (AXV) programme: Computer Science Foundation in quarter I, then Web Full-Stack.
- Everything for it lives in `AXV/` (gitignored). Read `AXV/knowledge-base.md` before making any AXV lesson, slide, question or exam; the source PDFs are in `AXV/sources/`.
- The public site has an AXV tab (`docs/courses/axv/`): course page, AI guide, and one page per topic (`topic-NN.md`) with the programme's content list. Only quarter I (Computer Science Foundation). Nothing else from `AXV/` goes on the site unless I ask.

## How the course works

- I teach each lecture from the PPTX. Students use the site **after** the lecture to review, and download the slides there.
- A lecture page is a readable companion to its slides: same topics in the same order, written as short explanations with code and real output. Do not add topics beyond the slides; flag any correction or addition in your report.
- A practice page holds the programs solved in class. Problem N links to `pN.py`.
- Lecture pages: explanation, worked examples with expected output, then `## Odatiy xatolar`. No "O'quv maqsadlari", "Mashq savollari" or "Manbalar" sections: the course books are listed once in `docs/courses/dasturlash/ai-guide.md`.
- Never invent sources, facts, policies, deadlines or prerequisites. Ask when something is missing.

## Writing for beginners

- Write for someone who has never programmed.
- Explain every new term in one plain sentence the first time it appears, and explain a concept before using it.
- Do not mention a detail you will not explain. If it cannot be explained simply, leave it out.
- Lecture pages use the slides' content and examples; do not add advanced side notes.
- Practice pages may introduce new things related to the lecture (that is intended); explain them briefly where they appear, with a link if a later lecture covers them. Do not change practice pages unless asked.

## Uzbek style and terms

- Natural, correct Uzbek with proper apostrophes (o', g'), also in program prompts and messages: "Ismingiz nima?", "To'g'ri parol".
- Keep programming identifiers and established English terms as they are (scope, f-string, local, global).
- `True` / `False`: introduced once as to'g'ri / noto'g'ri, then always written `True` / `False` (not "rost/yolg'on").
- `int` — butun son, `float` — kasr son, `str` — satr, `bool` — mantiqiy qiymat.
- Suffix after a foreign name takes an apostrophe: `Python'da`, `ASCII'dagi`.
- Capitalise names with `string.capwords()` (or `.capitalize()` for one word), never `.title()`: it breaks o' and g' (`O'Tkir`).
- Code follows PEP 8; Uzbek or English names, used consistently.

## Environment

- Windows. Always use the project venv (`.venv/Scripts/python.exe`). The `python` on PATH is MSYS2: do not use it; create venvs with `py -3 -m venv`. Never install packages globally.
- For office documents the venv also has `python-docx`, `pyyaml` and `pymupdf`. LibreOffice is installed but not on PATH: `"/c/Program Files/LibreOffice/program/soffice.exe"`.

## Working rules

- One feature or topic per task. Short plan only for structural changes.
- One agent by default; subagents only when I ask.
- No new dependencies or extra documents without a need in the task.
- After edits: run the changed code, run `mkdocs build --strict`, check affected links and downloads. A passing build does not replace my academic review.
- When adding pages, update `mkdocs.yml` navigation and `docs/courses/dasturlash/index.md`.
- Do not commit, push or deploy unless I ask.
- Finish with a short report (changes, checks, open decisions) and update `status.md`.
