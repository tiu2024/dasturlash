---
name: dasturlash-ppt
description: Create a new week's lecture from the teacher's topic and materials: discuss and agree the content and examples first, then build the lecture deck (PPTX, Uzbek) in Lectures/N_Mavzu.pptx and the student lecture page in docs/. Animated, timed 80-minute structure with warm-up, claim headlines, predict/quiz questions, live coding and an activity, plus private live-coding files. Use whenever the teacher asks for new lecture slides, a ma'ruza taqdimoti, a deck for week N, or to turn a chapter or notes into a lecture (weeks 4 and later).
argument-hint: "[mavzu] [ma'ruza raqami] [daqiqa] [materiallar papkasi]"
allowed-tools: Bash(.venv/Scripts/python.exe .claude/skills/dasturlash-ppt/scripts/*)
---

# Lecture deck and student page (ma'ruza)

Builds the PPTX the teacher lectures from, and the student lecture page that follows it. Slides and speaker notes are in Uzbek; talk to the teacher in simple English. The rules in `CLAUDE.md` ("Writing for beginners", "Uzbek style and terms", PEP 8) apply to every slide, note, page and code example.

Workflow: the teacher gives the topic and materials → **we discuss and agree what to include and which examples to use** → you write the spec and build the deck → you write the student page from the same spec. Never build before the teacher has approved the content (step 3).

How it works: you write one spec, `Lectures/src/week-NN/lecture.yaml`; the script turns it into the deck. The spec is the source of truth for both the deck and the page: to change them, change the spec and rebuild.

## Inputs

| Input | If missing |
|---|---|
| Topic and lecture number `N` (file name `Lectures/N_Mavzu.pptx`) | Ask. Look at `Lectures/` for the next number. |
| Week `NN` (folder `Lectures/src/week-NN/`) | Ask, or take it from the teacher's request. |
| Materials: book pages (PDF), notes, code, old slides | Look in `Lectures/src/week-NN/materials/`; otherwise ask where they are. Never invent content or sources. |
| Length | `teaching.lecture_minutes` in `Lectures/config.yaml` (80). The teacher may say "70 daqiqa". |

Course settings (name, university, group, year, colours, books, paths) are in `Lectures/config.yaml`. Read it; never fill an empty value with a guess.

## Steps

All commands run from the project root.

### 1. Check the tools (first use only)

```bash
.venv/Scripts/python.exe -c "import pptx, pygments, yaml, pymupdf"
```

If it fails, tell the teacher two packages are needed and install them into the venv only:
`.venv/Scripts/python.exe -m pip install -r .claude/skills/dasturlash-ppt/requirements.txt`

### 2. Read the materials

```bash
.venv/Scripts/python.exe .claude/skills/dasturlash-ppt/scripts/extract_sources.py "Lectures/src/week-NN/materials" -o "Lectures/src/week-NN/build/sources"
```

Read `build/sources/index.md`, then the text files (`--- page N ---` markers give the page numbers for `source:`). For old slides use `.venv/Scripts/python.exe .claude/skills/lecture-page/extract_slides.py "Lectures/<file>.pptx"`. If the index says a PDF has almost no text, it is scanned: rerun with `--render <pages>` and read the page images.

Check what students already know: the headings and examples of earlier `docs/courses/dasturlash/week-*/lecture.md` pages. Don't re-teach them; use them in the warm-up.

### 3. Discuss and agree the content (a required stop)

Read `references/pedagogy.md`. Then prepare a proposal and discuss it with the teacher. Do not write the spec yet.

1. 3–4 objectives (measurable verbs).
2. **What to include and what to leave out** from the materials, with the reason for each cut. Ask when the materials do not cover something the topic seems to need.
3. The storyline: claim headlines in order, in three segments.
4. **The examples**: for each headline, the code example and its output, written out in full so the teacher can judge them. Offer alternatives where you see them.
5. The misconceptions → `predict` / `quiz`.
6. The live-coding program and the activity that varies it.
7. Timing that adds up to the lecture length, with an active slide at least every 20 minutes.

Present it as a short numbered list the teacher can answer point by point. Revise until the teacher says it is approved; only an explicit OK (or "go ahead") ends this step. Then put the agreed plan as comments at the top of the spec.

When the source is the teacher's existing slides, keep their topics, order and examples; do not add new topics (the student page is built from this deck).

### 4. Write the spec

Copy the structure of `examples/week-03-funksiyalar.yaml`; every field is in `references/spec-format.md`.

- `config: ../../config.yaml`, `deck_file: "../../<N>_<Mavzu>.pptx"`. File names follow `Lectures/`: number, underscore, Uzbek title, no apostrophes (`5_Royxatlar.pptx`).
- Headlines: short Uzbek claim sentences (≤ 14 words), not topic labels.
- Every content slide has Uzbek `notes` (30–100 words). Students download the deck with the notes.
- Code: PEP 8, two blank lines between functions, `o'`/`g'` in strings, `string.capwords()` not `.title()`, straight quotes. Only constructs taught so far.
- Every `code` slide that prints has `output:` produced by running it; for `input()` include the typed value.
- `predict` has `misconception`; `quiz` has `distractors`.
- Live-coding `starter` runs (comments only is fine); `solution` gives the output the activity promises.
- Book citations: `source: "@narzullayev, 45-bet"` (ids from `books:` in the config). No book, no citation.

### 5. Build and fix every warning

```bash
.venv/Scripts/python.exe .claude/skills/dasturlash-ppt/scripts/build_lecture.py "Lectures/src/week-NN/lecture.yaml"
```

It prints the timeline and warnings. Fix each warning by changing content (shorter headline, fewer lines, split a slide, rebalance minutes) and rebuild. If the deck file already exists, the script stops: ask the teacher before rerunning with `--force` (the existing deck may have hand edits).

### 6. Check correctness

- Run every code example and compare with `output` / `answer`. Use `PYTHONIOENCODING=utf-8` and pipe inputs: `printf "5\n" | .venv/Scripts/python.exe file.py`.
- Run `livecode/solution/*.py` with the activity's example input, and every starter file.
- Check facts against the materials.

### 7. Look at the slides

```bash
.venv/Scripts/python.exe .claude/skills/dasturlash-ppt/scripts/render_preview.py "Lectures/<N>_<Mavzu>.pptx" --out "Lectures/src/week-NN/build/preview" --soffice "C:/Program Files/LibreOffice/program/soffice.exe"
```

Open `preview/contact-sheet.png`, then any dense `slide-NN.png`. A render shows each slide's final state (all clicks). Check: text overflowing or overlapping, code smaller than ~16 pt, low contrast, Uzbek typos. Fix in the spec, rebuild with `--force`, render again.

### 8. Student lecture page

Once the deck is built and checked, write the page in the same task. Follow the `lecture-page` skill (`.claude/skills/lecture-page/SKILL.md`) from its step 2 on, with these differences:
- The source is the spec, not the PPTX: use the slides' headlines, code, `output`/`answer` and the speaker `notes` (without the timing line, classroom instructions and `Manba:`). The slide-label table in that skill shows what each slide type becomes.
- Copy the finished deck to `docs/downloads/dasturlash/week-NN/` and update `mkdocs.yml` and `docs/courses/dasturlash/index.md` as that skill says.
- Cover only the deck's topics; flag anything you had to correct or add.

If the teacher later edits the deck by hand in PowerPoint, the spec is out of date: run `/lecture-page` on the edited PPTX instead.

### 9. Report

In simple English: the deck path, the page path, slide count and total minutes, slides and page parts that need the teacher's academic review, anything you could not verify, and that the live-coding files are in `Lectures/src/week-NN/livecode/` (private; after class they can go to `/practice-page`). Remind the teacher to click through once in PowerPoint's Slide Show to see the animations. Update `status.md`. Do not commit, push or deploy.

## Files

| Path | Git |
|---|---|
| `Lectures/<N>_<Mavzu>.pptx` — the deck | committed (public) |
| `Lectures/src/week-NN/lecture.yaml` — the spec | committed (public) |
| `Lectures/src/week-NN/materials/` — book pages, notes | ignored (copyright) |
| `Lectures/src/week-NN/livecode/`, `build/` | ignored (solutions before class, previews) |

Skill files: `scripts/build_lecture.py` (spec → deck, live-coding files), `scripts/extract_sources.py` (materials → text and figures), `scripts/render_preview.py` (deck → PNG previews), `references/pedagogy.md` (lecture design — read when planning), `references/spec-format.md` (every spec field — read when writing), `examples/week-03-funksiyalar.yaml` (complete pilot lecture).
