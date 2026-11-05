# Status

Updated: 2026-11-05. Overwrite this file at the end of each session; git keeps the history.

## Site

| Week | Lecture | Practice | Published |
|---|---|---|---|
| 1. Dasturlashga kirish | done | — | 2026-10-19 |
| 2. Python dasturlashga kirish | done | done (11 problems) | 2026-10-19 |
| 3. Funksiyalar, shartlar, scope va turlar | done | done (16 problems) | 2026-10-19 |
| 4. Looplar va stringlar | done | done (11 problems) | 2026-10-19 |
| 5. Ro'yxatlar va kortejlar | done | — | 2026-10-19 |

Last published 2026-11-05 (AXV topic 2 refactor with images, Odatiy xatolar removed from AXV pages; earlier: topic 2 page with PDF slides; earlier: topic 5 page with slides; topic 1 page with slides and labs; site on `gh-pages`).

## Done

- 2026-10-27: AXV topic 5 lecture deck built (private): `AXV/lectures/5_Internet, brauzer va pochta.pptx`, spec in `AXV/lectures/src/topic-05/`, 37 slides, 79 of 80 min, with 2 ChatGPT figures; domen/IP/DNS, request path, cache and cookie slides added. Student page `docs/courses/axv/topic-05.md` written from the deck (2 figures in `img/topic-05/`, PPTX in `docs/downloads/axv/topic-05/`); published 2026-10-27. No lab exercises yet.
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
- 2026-11-02: O'quv dastur "Iqtisodiyotda axborot kommunikasion texnologiyalar va tizimlar" (kunduzgi, IAKTT1106, 60410100 – 1.03, semester 2, 2026-2027, 6 credits, 36/36/0/108): `OQ/IQT_IAKTT1106.docx` (private). Topics as written in `IQT lar uchun.docx`; literature (14) from the IQT Logistika OQ; TN (12) and mustaqil ta'lim (18 × 6 h, 36 h in small groups) adapted from it. Lecture reference numbers assigned by Claude: teacher to check. Major 60410100 added to `fill_oquv_dastur.py` (OQ and skill copy). Old KA1406 YAML kept as `OQ/KA1406_config.yaml` / `OQ/KA1406_content.yaml`. Design notes: `OQ/IQT_design_notes.md`.
- 2026-11-02: Partly Russian version of the IQT O'quv dastur (teacher's request, after a full translation was rejected): `OQ/IQT26_IAKTT1106_ru_v2.docx` (private), from the edited Uzbek file. Russian only in table 2 (heading, maqsad, vazifalar), the lecture/practice topic texts of table 4 and the task texts of table 5; everything else Uzbek. The rejected full version is still `OQ/IQT26_IAKTT1106_ru.docx` (was open in Word, could not be overwritten).
- 2026-11-02: Kechki version of the IQT O'quv dastur: `OQ/KIQT26_IAKTT1106.docx` (private), made from the teacher's edited kunduzgi `OQ/IQT26_IAKTT1106.docx`: ishchi title, (kechki ta'lim uchun), "Mazkur ishchi o'quv dasturi", all 36 topics starred (hours same as kunduzgi, teacher confirmed), IZOH rows after the lecture and practice blocks. Table 1 (code, semester, weekly hours, curriculum number) copied from kunduzgi.
- 2026-11-02: Partly Russian kechki IQT O'quv dastur: `OQ/KIQT26_IAKTT1106_ru.docx` (private), from `OQ/KIQT26_IAKTT1106.docx`, same parts in Russian as the kunduzgi `_ru_v2` (table 2, topic texts of table 4, task texts of table 5); stars, IZOH rows and everything else Uzbek.
- 2026-11-05: AXV topic 2 student page written (`docs/courses/axv/topic-02.md`) from the L01 slides (PDF `temporary/001. 06-10-2026 - Kompyuterlar_va_Windows.pdf`, slides 11-13 and quiz Q4; slides 4-10 are topic 1 and the page links there). PDF download in `docs/downloads/axv/topic-02/kompyuterlar-va-windows.pdf`. Published 2026-11-05 (3b1367c). Remaining files in `temporary/` (topics 3, 4, 6, 7) still to do.
- 2026-11-05: AXV topic 2 page reviewed. Refactor task written: `AXV/lectures/src/topic-02/refactor.md` (private). It covers corrections, Windows 10/11 and EN/RU interface names, a Search-first approach, new sections for Control Panel and date/time/language, 6 ChatGPT image prompts and 4 screenshots to take. Page not changed yet. Russian and Windows 10 strings marked (v) must be checked on a classroom PC.
- 2026-11-05: AXV topic 2 page refactored per `AXV/lectures/src/topic-02/refactor.md` (corrections, Windows 10/11, RU names, Settings via Search, date/time/language, Control Panel, install/uninstall, shortcut), with 10 images in `docs/courses/axv/img/topic-02/` (6 ChatGPT drawings, 4 Windows 11 screenshots; account, computer and Wi-Fi names painted out of `sozlamalar.png`). "Odatiy xatolar" removed from all AXV pages (topics 1, 2, 5; teacher's request); Dasturlash pages keep theirs. Knowledge base topic 2 updated. (v) RU and Windows 10 strings confirmed by the teacher. Published 2026-11-05 (0074706).
- 2026-11-05: AXV slides added to the site for topics 3, 4, 6, 7 (teacher's request, no page text): copies of the `temporary/` files in `docs/downloads/axv/topic-03/axborot-olchov-birliklari.pdf`, `topic-04/asosiy-va-qoshimcha-qurilmalar.pdf`, `topic-06/kompyuter-xavfsizligi-antivirus.pptx`, `topic-07/klaviaturada-tez-yozish.pptx`; each topic page has a "Ma'ruza taqdimoti" link and the "tez orada" line was removed. PPTX files include speaker notes (as topics 1 and 5). Open: topic 7 deck says "I bob", site page says "II bob". Not published.
