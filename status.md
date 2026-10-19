# Status

Updated: 2026-10-19. Overwrite this file at the end of each session; git keeps the history.

## Site

| Week | Lecture | Practice | Published |
|---|---|---|---|
| 1. Dasturlashga kirish | done | — | 2026-10-19 |
| 2. Python dasturlashga kirish | done | done (11 problems) | 2026-10-19 |
| 3. Funksiyalar, shartlar, scope va turlar | done | done (16 problems) | 2026-10-19 |
| 4. Looplar va stringlar | done | done (11 problems) | 2026-10-19 |
| 5. Ro'yxatlar va kortejlar | done | — | 2026-10-19 |

Last published 2026-10-19 (Mobil ilovalar yaratish, lecture 4; site on `gh-pages`).

## Done

- 2026-10-19: weeks 1–3 reviewed and fixed; scope and types added to week 3 from the slides.
- 2026-10-19: workspace cleanup: new `CLAUDE.md`, project settings, project-only copies of `oquv-dastur` and `adabiyot-tanlash` (gitignored), skills `lecture-page`, `practice-page`, `review-week`, `publish`; `forme.md`, `templates/` and the old week-3 deck removed.
- 2026-10-19: lectures revised for complete beginners: week 1 rebuilt from the slides, weeks 2–3 simplified; "Writing for beginners" rule added. Course books stay in `ai-guide.md`; lecture pages have no Manbalar section.
- 2026-10-19: LibreOffice and the office packages (`python-docx`, `pyyaml`, `pymupdf`) installed; `/oquv-dastur` tested end to end (output in `OQ/test1_*`; script kept as `OQ/fill_oquv_dastur.py`).
- 2026-10-19: `CLAUDE.md` trimmed to facts the project files do not record.
- 2026-10-19: hook added: before Claude commits, if `status.md` is unchanged, the teacher is asked to approve (`.claude/hooks/status-reminder.sh`).
- 2026-10-19: favicon changed to the new icon (`docs/assets/favicon.png`, set in `mkdocs.yml`); published 2026-10-19.
- 2026-10-19: `/dasturlash-ppt` rewritten: Uzbek lecture decks (80 min, animated, projector colours) saved to `Lectures/N_Mavzu.pptx`; course settings in `Lectures/config.yaml`; specs in `Lectures/src/week-NN/lecture.yaml` (book excerpts, live-coding files and previews gitignored). `/lecture-page` reads these decks (`extract_slides.py --notes`). Pilot: lecture 3 "Funksiyalar" rebuilt from the week 3 slides → `Lectures/src/week-03/build/3_Funksiyalar_pilot.pptx` (not on the site).

- 2026-10-19: week 4 lecture and practice pages written from `Lectures/4_Looplar va stringlar.pptx` (copy in `docs/downloads/dasturlash/week-04/`, with p1–p11.py); nav and index updated; published (baec985). The deck still has placeholders on the title and last slides (left as is).

- 2026-10-19: `/dasturlash-ppt` skill, updated `/lecture-page`, `Lectures/config.yaml` and the week 3 spec committed; the old `skill-install/` copy removed.

- 2026-10-19: week 5 built with `/dasturlash-ppt`: spec `Lectures/src/week-05/lecture.yaml`, deck `Lectures/5_Royxatlar va kortejlar.pptx` (43 slides, 80 min), lecture page `week-05/lecture.md`, download in `docs/downloads/dasturlash/week-05/`; live-coding files in `Lectures/src/week-05/livecode/` (private). Published.

## Next

1. Install the deck tools into the venv once: `.venv/Scripts/python.exe -m pip install -r .claude/skills/dasturlash-ppt/requirements.txt`.
2. Make the next lecture with `/dasturlash-ppt` (put the book pages in `Lectures/src/week-NN/materials/`).

## Waiting for the teacher

- Fill in the empty values in `Lectures/config.yaml` (title, faculty, department, course code, semester) and check the academic year.
- Review the pilot deck: content, Uzbek, and the colours in the lecture room.
- Remove `oquv-dastur` and `adabiyot-tanlash` from the claude.ai account so they exist only in this project.
- Academic review of the changed examples in weeks 1–3.
- Back up `OQ/` and `.claude/skills/oquv-dastur/`, `.claude/skills/adabiyot-tanlash/` (they exist only on this computer).

- 2026-10-19: site is now multi-course: top tabs per course; new course "Mobil ilovalar yaratish" added as a placeholder (`docs/courses/mobil-ilovalar/index.md`, no weekly topics yet); site name changed to "Kurslar". Published.

- 2026-10-19: second course added: "Mobil ilovalar yaratish" (own tab, own AI page, own config `Lectures/mobil/config.yaml`, code language Kotlin). Lecture 4 "Kotlin tilida sinflar va obyektlar": spec `Lectures/mobil/src/week-04/lecture.yaml`, deck `Lectures/mobil/4_Sinflar va obyektlar.pptx` (26 slides, 80 min), page `docs/courses/mobil-ilovalar/week-04/lecture.md`, download in `docs/downloads/mobil-ilovalar/week-04/`. Kotlin code not run (no compiler here): outputs traced by hand; check in Kotlin Playground. Published.

- 2026-10-19: Mobil ilovalar week 4 practice page (8 Ticket problems, `p1.kt`–`p8.kt` in `docs/downloads/mobil-ilovalar/week-04/`). Kotlin not run (no compiler); sample outputs traced by hand, to be checked in Kotlin Playground. Published.
