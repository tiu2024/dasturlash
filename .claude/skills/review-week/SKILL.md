---
name: review-week
description: Review one week's lecture page, practice page and pN.py downloads for factual errors, unclear or ambiguous explanations, Uzbek grammar, duplication, inconsistent terms and problem/solution mismatches, then report findings with locations and fixes before editing. Use when the teacher asks to review or check a week before publishing.
---

# Review one week

Report first; edit only after the teacher answers.

## Read

- `docs/courses/dasturlash/week-NN/lecture.md` and `practice.md`
- `docs/downloads/dasturlash/week-NN/*.py`
- The slides, when checking that the page follows them: `.venv/Scripts/python.exe .claude/skills/lecture-page/extract_slides.py "Lectures/<file>.pptx"`
- Earlier weeks only to check duplication and what students already know.

## Check

1. **Correctness.** Every claim, every stated output (run the code unless the teacher says not to), every boundary case. Big-O, number formats, error messages, Python behaviour.
2. **Teaching.** A concept is explained before it is used. Explanations are clear for first-year students and not misleading. Problem statement, sample, code and explanation agree. File links match problem numbers.
3. **Ambiguity.** Problem ranges, units, input formats, "gacha", "dan ... gacha".
4. **Uzbek.** Grammar, natural wording, spelling and apostrophes, including prompts and messages inside the code.
5. **Terms and style.** The rules in `CLAUDE.md` (`True`/`False`, kasr son, `Python'da`, `capwords`, PEP 8).
6. **Duplication.** The same explanation repeated within the week or from earlier weeks.
7. **Structure.** Sections required by `CLAUDE.md` present (`Odatiy xatolar`, `Manbalar`), forbidden ones absent.

## Report

Group by severity, most serious first:

1. Errors that teach something wrong
2. Unclear or ambiguous explanations and statements
3. Grammar and wording
4. Duplication (a table: content, where, suggestion)
5. Consistency

Each finding: `file:line` — the problem — the suggested fix, with the Uzbek replacement text where useful. End with the decisions the teacher must make.

## After the teacher answers

Apply the approved fixes to the pages and the `.py` files together, run the changed code and `.venv/Scripts/python.exe -m mkdocs build --strict`, report, and update `status.md`.
