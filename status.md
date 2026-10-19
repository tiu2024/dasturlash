# Status

Updated: 2026-10-19. Overwrite this file at the end of each session; git keeps the history.

## Site

| Week | Lecture | Practice | Published |
|---|---|---|---|
| 1. Dasturlashga kirish | done | — | 2026-10-19 |
| 2. Python dasturlashga kirish | done | done (11 problems) | 2026-10-19 |
| 3. Funksiyalar, shartlar, scope va turlar | done | done (16 problems) | 2026-10-19 |

Last published 2026-10-19 (the latest commit on `main`; site on `gh-pages`).

## Done

- 2026-10-19: weeks 1–3 reviewed and fixed; scope and types added to week 3 from the slides.
- 2026-10-19: workspace cleanup: new `CLAUDE.md`, project settings, project-only copies of `oquv-dastur` and `adabiyot-tanlash` (gitignored), skills `lecture-page`, `practice-page`, `review-week`, `publish`; `forme.md`, `templates/` and the old week-3 deck removed.
- 2026-10-19: lectures revised for complete beginners: week 1 rebuilt from the slides, weeks 2–3 simplified; "Writing for beginners" rule added. Course books stay in `ai-guide.md`; lecture pages have no Manbalar section.
- 2026-10-19: LibreOffice and the office packages (`python-docx`, `pyyaml`, `pymupdf`) installed; `/oquv-dastur` tested end to end (output in `OQ/test1_*`; script kept as `OQ/fill_oquv_dastur.py`).
- 2026-10-19: `CLAUDE.md` trimmed to facts the project files do not record.
- 2026-10-19: hook added: before Claude commits, if `status.md` is unchanged, the teacher is asked to approve (`.claude/hooks/status-reminder.sh`).

## Next

1. Rewrite `/dasturlash-ppt` later (old skill lost; it had problems with visual design, content and broken output).

## Waiting for the teacher

- Remove `oquv-dastur` and `adabiyot-tanlash` from the claude.ai account so they exist only in this project.
- Academic review of the changed examples in weeks 1–3.
- Back up `OQ/` and `.claude/skills/oquv-dastur/`, `.claude/skills/adabiyot-tanlash/` (they exist only on this computer).
