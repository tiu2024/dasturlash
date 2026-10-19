---
name: lecture-page
description: Turn a lecture PPTX from Lectures/ into the week's student lecture page (docs/courses/dasturlash/week-NN/lecture.md), publish the PPTX as a download and update navigation. Use when the teacher asks to create or update a lecture page from slides.
---

# Lecture page from slides

Students read this page after the lecture to review it. It follows the slides; it is not a new lecture. Follow the style and term rules in `CLAUDE.md`.

## Inputs

| Input | If missing |
|---|---|
| Week number `NN` | Ask. |
| PPTX in `Lectures/` | Ask which file. |

## Steps

1. **Read the slides.**

    ```bash
    .venv/Scripts/python.exe .claude/skills/lecture-page/extract_slides.py "Lectures/<file>.pptx"
    ```

    Read one finished page as the style reference (`docs/courses/dasturlash/week-03/lecture.md`), not more. Read earlier weeks only to find what students already know.

2. **Write `docs/courses/dasturlash/week-NN/lecture.md`.**

    ```markdown
    # N-hafta. <Mavzu>

    Ma'ruza taqdimoti: [<Mavzu> (PPTX)](../../../downloads/dasturlash/week-NN/<slug>.pptx)

    Bu haftaning amaliy qismi: [amaliyot](practice.md).

    ## <first slide section>
    ...
    ## Odatiy xatolar
    ```

    - Leave out the practice link if `practice.md` does not exist yet.
    - Write for someone who has never programmed (see "Writing for beginners" in `CLAUDE.md`): explain each new term in one plain sentence; leave out any detail you will not explain; no advanced side notes, no code the students cannot read yet.
    - Keep the slides' sections and order. Section slides become `##` headings, smaller topics `###`.
    - Turn bullet slides into short paragraphs or lists. Explain each idea before its code.
    - Every code block is labelled `python` (or `text`, `bash`) and followed by a `text` block with the real output. For `input()`, show the typed value in the output, as the other pages do.
    - Question/answer slides (SAVOL / JAVOB) become worked examples: show the code, the result and why.
    - Do not repeat what an earlier week already explains: one sentence and a relative link with an anchor, e.g. `[2-haftada](../week-02/lecture.md#malumot-turlari)`.
    - If a slide is wrong or unclear, write the correct version on the page and list it in the report so the slide can be fixed too.
    - `## Odatiy xatolar`: mistakes students make with this week's topics, each with a fix.

    - No `## Manbalar` section: the course books are listed once in `docs/courses/dasturlash/ai-guide.md`.

3. **Publish the slides.** Copy the PPTX to `docs/downloads/dasturlash/week-NN/<slug>.pptx`. Slug: lowercase ASCII words joined by hyphens, e.g. `funksiyalar-shartlar-scope-turlar.pptx`. If a copy already exists, replace it.

4. **Navigation.** Add or update the week in `mkdocs.yml`:

    ```yaml
          - N-hafta. <Mavzu>:
              - Ma'ruza: courses/dasturlash/week-NN/lecture.md
              - Amaliyot: courses/dasturlash/week-NN/practice.md
    ```

    and in the list in `docs/courses/dasturlash/index.md`.

5. **Check.**
    - Run every code example with `.venv/Scripts/python.exe` and compare the output with the page.
    - `.venv/Scripts/python.exe -m mkdocs build --strict`.
    - Check that the anchors you linked exist in the built HTML (`site/.../index.html`, `id="..."`).

6. **Report** in simple English: files changed, slides you corrected or flagged, checks run. Update `status.md`.
