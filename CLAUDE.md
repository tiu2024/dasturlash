# Dasturlash 1, 2 — course workspace

## Who and what

I. J. Husainov teaches the first-year course "Dasturlash 1, 2" at Turan International University (ATT-2026). Teaching language: Uzbek (Latin script). Python now, C later.

This folder is my workspace for the course: the public student website and, kept private, official university documents. I add automation one feature at a time.

Talk to me in simple, clear English. Student-facing content is in Uzbek.

## Folders

| Path | Contents | Public |
|---|---|---|
| `docs/` | MkDocs Material site → https://tiu2024.github.io/dasturlash/ (repo github.com/tiu2024/dasturlash) | yes |
| `docs/courses/dasturlash/week-NN/` | `lecture.md`, `practice.md` | yes |
| `docs/downloads/dasturlash/week-NN/` | lecture PPTX copy, practice `pN.py` files | yes |
| `Lectures/N_Mavzu.pptx` | original lecture decks | committed |
| `OQ/` | official documents (O'quv dastur templates and outputs) | never (gitignored) |
| `.claude/skills/` | project skills; `oquv-dastur` and `adabiyot-tanlash` are gitignored | partly |
| `status.md` | current state and next steps | committed |
| `DEPLOY.md` | publishing steps | committed |

Everything in `docs/` is public, including files missing from navigation. Never put private, official or unreleased material in `docs/` or in any committed file.

## How the course works

- I teach each lecture from the PPTX. Students use the site **after** the lecture to review, and download the slides there.
- A lecture page is a readable companion to its slides: same topics in the same order, written as short explanations with code and real output. Do not add topics beyond the slides; flag any correction or addition in your report.
- A practice page holds the programs solved in class. Problem N links to `pN.py`.
- Lecture pages: explanation, worked examples with expected output, `## Odatiy xatolar`, then `## Manbalar` with the sources I give. No "O'quv maqsadlari" or "Mashq savollari" sections.
- Never invent sources, facts, policies, deadlines or prerequisites. Ask when something is missing.

## Uzbek style and terms

- Natural, correct Uzbek with proper apostrophes (o', g'), also in program prompts and messages: "Ismingiz nima?", "To'g'ri parol".
- Keep programming identifiers and established English terms as they are (scope, f-string, local, global).
- `True` / `False`: introduced once as to'g'ri / noto'g'ri, then always written `True` / `False` (not "rost/yolg'on").
- `int` — butun son, `float` — kasr son, `str` — satr, `bool` — mantiqiy qiymat.
- Suffix after a foreign name takes an apostrophe: `Python'da`, `ASCII'dagi`.
- Capitalise names with `string.capwords()` (or `.capitalize()` for one word), never `.title()`: it breaks o' and g' (`O'Tkir`).
- Code follows PEP 8: 4-space indent, two blank lines between functions, `ism="..."` defaults without spaces, Uzbek or English names used consistently.
- Explain a concept before using it. If a practice problem needs something taught later, add one sentence and a link to that lecture.

## Environment

- Windows. Use the project venv: `.venv/Scripts/python.exe`. The `python` on PATH is MSYS2: do not use it; create venvs with `py -3 -m venv`. Never install packages globally.
- Build: `.venv/Scripts/python.exe -m mkdocs build --strict`. Preview: `.venv/Scripts/python.exe -m mkdocs serve`.

## Working rules

- One feature or topic per task. Short plan only for structural changes.
- One agent by default; subagents only when I ask.
- No new dependencies or extra documents without a need in the task.
- After edits: run the changed code, run the strict build, check affected links and downloads. A passing build does not replace my academic review.
- When adding pages, update `mkdocs.yml` navigation and `docs/courses/dasturlash/index.md`.
- Do not commit, push or deploy unless I ask.
- Finish with a short report (changes, checks, open decisions) and update `status.md`.

## Skills

| Skill | Use |
|---|---|
| `/lecture-page` | lecture PPTX → lecture page with sources |
| `/practice-page` | class programs → practice page and `pN.py` files |
| `/review-week` | review one week for errors before publishing |
| `/publish` | build, commit, push, deploy (only when I ask) |
| `/oquv-dastur`, `/adabiyot-tanlash` | official O'quv dastur and its literature list (private) |
| `/dasturlash-ppt` | lecture deck — being rewritten |
