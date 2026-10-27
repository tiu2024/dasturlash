# Status

Updated: 2026-10-27. Overwrite this file at the end of each session; git keeps the history.

## Site

| Week | Lecture | Practice | Published |
|---|---|---|---|
| 1. Dasturlashga kirish | done | — | 2026-10-19 |
| 2. Python dasturlashga kirish | done | done (11 problems) | 2026-10-19 |
| 3. Funksiyalar, shartlar, scope va turlar | done | done (16 problems) | 2026-10-19 |
| 4. Looplar va stringlar | done | done (11 problems) | 2026-10-19 |
| 5. Ro'yxatlar va kortejlar | done | — | 2026-10-19 |

Last published 2026-10-27 (AXV topic 1 page with slides and labs; site on `gh-pages`).

## Done

- 2026-10-27: AXV topic 1 lecture deck built and deepened (private): `AXV/lectures/1_Zamonaviy kompyuterlar.pptx`, spec in `AXV/lectures/src/topic-01/`, 33 slides, 78 of 80 min, with the 6 ChatGPT figures. Student page `topic-01.md` still a stub.
- 2026-10-27: AXV topic 1 student page written (`docs/courses/axv/topic-01.md`, images in `docs/courses/axv/img/topic-01/`), PPTX download in `docs/downloads/axv/topic-01/`, 5 lab exercises with answers, only from the lecture; published 2026-10-27.
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

- 2026-10-22: O'quv dastur "Kiberxavfsizlik asoslari" (kunduzgi, KA1406, 60610100) made from the parent `Kiberxavfsizlik_asoslari_FD.docx`: `OQ/Kiberxavfsizlik asoslari_kunduzgi.docx` (private, in `OQ/`). 12 parent lectures split into 18; parent practice + lab merged into 18 amaliy. Teacher to check: course_work "+" and curriculum number "60610100 – 1.12" (angle brackets removed). Design notes (Step 8) not made yet.
- 2026-10-22: Kurs ishi (KI) table in `OQ/Kiberxavfsizlik asoslari_kunduzgi.docx` filled with 60 topics (private). Re-running `fill_oquv_dastur.py` would overwrite the KI table and the teacher's manual edits.
- 2026-10-22: "Kurs ishini baholash mezoni" in the KI O'quv dastur adapted from Ma'lumotlar bazasi to Kiberxavfsizlik (criteria 1-5, 7 and the 5/4/3 grade descriptions; points unchanged). Teacher's request; rest of Baholash mezoni untouched.
- 2026-10-22: Review fixes applied to the KI O'quv dastur (`OQ/`, private): prerequisites now Kompyuter tarmoqlari, Dasturlash 1,2, Ma'lumotlar bazasi (also in `OQ/config.yaml`); 19 KI topics now name an organisation; section 7 (SQL leftover, AI item), M16 (CSF 2.0), Cyrillic letter, grammar. `OQ/content.yaml` is NOT updated: the .docx is the source now. Open: weekly hours 5 vs 72 h; Xashimov title (dotsent / professori).
- 2026-10-22: Kechki version of the Kiberxavfsizlik asoslari O'quv dastur: `OQ/Kiberxavfsizlik asoslari_kechki.docx` (private), made from the final kunduzgi .docx (ishchi title, all 36 topics starred, IZOH rows). Semester, weekly hours, course code, curriculum number copied from kunduzgi: teacher to confirm for kechki.
- 2026-10-27: new private project AXV ("Muhammad al-Xorazmiy vorislari", 8-sinf mentoring). `AXV/` is gitignored. Knowledge base `AXV/knowledge-base.md`: what AXV is, students, format (36 lessons, Oct 2 – Jan 1), all 26 topics with the weekly plan, Chapter I Know / Be able to per topic (teacher's draft, lightly corrected, checked against lessons L01–L04), Chapters II–III official content and outcomes, assessment, projects, methods, final competency, issues in the programme and open questions. Sources copied to `AXV/sources/` (CSF and Web Full-Stack programmes, lessons L01–L04). `CLAUDE.md` has a short AXV section pointing there. Open: the 8 questions at the end of the knowledge base; Chapters II–III breakdowns not written.
- 2026-10-27: lesson PDF copies removed from `AXV/sources/` (programmes kept). Public AXV tab added: `docs/courses/axv/index.md` lists the 26 Computer Science Foundation topics (I chorak) by chapter; nav and home page updated. Published 2026-10-27 (dc1c0a2).
- 2026-10-27: `Operatsion_tizimlar_fan_dasturi.doc` moved to the Recycle Bin (teacher's request). AXV tab expanded: 26 topic pages `docs/courses/axv/topic-01.md`–`topic-26.md` (title, chapter, lesson type, programme content list, "materials coming soon"), sidebar grouped by the three chapters, AI guide `docs/courses/axv/ai-guide.md` (prompt in English/Uzbek/Russian for 8th graders, reading list from the programme's sources). Index list numbering fixed. Published 2026-10-27 (506e960).
- 2026-10-27: "Reading and Learning guide" section removed from the AXV AI guide (teacher's request). Published 2026-10-27.
