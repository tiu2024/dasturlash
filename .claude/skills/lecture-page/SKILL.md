---
name: lecture-page
description: Turn a lecture PPTX from Lectures/ into the week's student lecture page (docs/courses/dasturlash/week-NN/lecture.md), attach the teacher's sources in a Manbalar section, publish the PPTX as a download and update navigation. Use when the teacher asks to create or update a lecture page from slides.
---

# Lecture page from slides

Students read this page after the lecture to review it. It follows the slides; it is not a new lecture. Follow the style and term rules in `CLAUDE.md`.

## Inputs

| Input | If missing |
|---|---|
| Week number `NN` | Ask. |
| PPTX in `Lectures/` | Ask which file. |
| Sources: where the material came from (links, books, courses) | Ask once: "Which sources did you use for this lecture?" Never guess, search for, or add sources yourself. |

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
    ## Manbalar
    ```

    - Leave out the practice link if `practice.md` does not exist yet.
    - Keep the slides' sections and order. Section slides become `##` headings, smaller topics `###`.
    - Turn bullet slides into short paragraphs or lists. Explain each idea before its code.
    - Every code block is labelled `python` (or `text`, `bash`) and followed by a `text` block with the real output. For `input()`, show the typed value in the output, as the other pages do.
    - Question/answer slides (SAVOL / JAVOB) become worked examples: show the code, the result and why.
    - Do not repeat what an earlier week already explains: one sentence and a relative link with an anchor, e.g. `[2-haftada](../week-02/lecture.md#malumot-turlari)`.
    - If a slide is wrong or unclear, write the correct version on the page and list it in the report so the slide can be fixed too.
    - `## Odatiy xatolar`: mistakes students make with this week's topics, each with a fix.

3. **Write `## Manbalar`** exactly from the teacher's list:

    ```markdown
    ## Manbalar

    - [<Kurs yoki sahifa nomi>](<URL>) — <undan nima olingan>.
    - <Muallif>. *<Kitob nomi>*. <Nashriyot>, <yil>. — <boblar>.
    ```

    One line each, with what was used from it. Keep titles and authors as given. If the teacher has no sources, leave the section out and say so in the report.

4. **Publish the slides.** Copy the PPTX to `docs/downloads/dasturlash/week-NN/<slug>.pptx`. Slug: lowercase ASCII words joined by hyphens, e.g. `funksiyalar-shartlar-scope-turlar.pptx`. If a copy already exists, replace it.

5. **Navigation.** Add or update the week in `mkdocs.yml`:

    ```yaml
          - N-hafta. <Mavzu>:
              - Ma'ruza: courses/dasturlash/week-NN/lecture.md
              - Amaliyot: courses/dasturlash/week-NN/practice.md
    ```

    and in the list in `docs/courses/dasturlash/index.md`.

6. **Check.**
    - Run every code example with `.venv/Scripts/python.exe` and compare the output with the page.
    - `.venv/Scripts/python.exe -m mkdocs build --strict`.
    - Check that the anchors you linked exist in the built HTML (`site/.../index.html`, `id="..."`).

7. **Report** in simple English: files changed, slides you corrected or flagged, sources added (or missing), checks run. Update `status.md`.
