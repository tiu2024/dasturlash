---
name: practice-page
description: Build or update a week's practice page (docs/courses/dasturlash/week-NN/practice.md) from the Python programs solved in class, with clear problem statements, real sample runs, hidden solutions, explanations and downloadable pN.py files. Use when the teacher gives the class code for a week.
---

# Practice page from class programs

The programs are the ones the teacher solved in class. Keep their solution ideas. Follow the style and term rules in `CLAUDE.md`.

## Inputs

| Input | If missing |
|---|---|
| Week number `NN` | Ask. |
| The class `.py` files | Ask where they are. |
| Order of the problems | Use the order the teacher gives; otherwise propose one (simple → harder) and ask. |

## Steps

1. **Read** every program, the week's `lecture.md` (what students have been taught) and one style example: `docs/courses/dasturlash/week-03/practice.md`.

2. **Fix the code, minimally.** Keep the logic. Fix only:
    - bugs and wrong results;
    - informal or misspelled Uzbek in prompts, messages and names (`nma` → `nima`, `habar` → `xabar`);
    - PEP 8 layout, unused or commented-out code;
    - `.title()` on names → `string.capwords()` / `.capitalize()`.

    List every change in the report. A program that is wrong **on purpose** (to teach a bug) stays wrong and gets a note under the problem:

    ```markdown
    !!! question "Diqqat"
        Bu masalaning sharti ataylab xato qo'yilgan. ...
    ```

3. **Write the page.**

    ```markdown
    # Amaliyot

    Bu sahifada [ma'ruzada](lecture.md) o'rganilgan ... bilan darsda yechilgan K ta masala keltirilgan. Har bir masala shartidan keyin **Yechim** bloki joylashgan: u yopiq turadi, ustiga bosib oching. Avval masalani o'zingiz yechib ko'ring va natijani namuna bilan solishtiring, keyin yechim va tushuntirishni o'qing.

    Har bir yechim ichida shu dasturning `.py` fayliga havola bor.

    ## 1. <Sarlavha>

    **Masala.** Shunday dastur yozing: ...

    Namuna:

    ```text
    ...
    ```

    ??? success "Yechim"

        ```python
        ...
        ```

        Fayl: [p1.py](../../../downloads/dasturlash/week-NN/p1.py)

        **Tushuntirish.**

        - ...

    ## Qisqa lug'at
    ```

    - **Problem statement:** precise inputs, output format and units. Write ranges with explicit boundaries ("0–11 yosh", "1 kg va undan yengil"), never an ambiguous "gacha". The statement must match what the code does.
    - **Samples:** 1–3 runs per problem, produced by running the program: an ordinary case and the important boundary case.
    - **Explanation:** bullets on each new construct, why it is used, boundary cases and limits of the program. For a concept from the lecture, one line and a link (`[ma'ruzada](lecture.md#anchor)`) instead of re-explaining. For a concept not yet taught, one sentence plus a link to the later lecture. Do not repeat the same explanation in several problems; refer back ("4-masalaga qarang").
    - **Qisqa lug'at:** a table of the new functions and terms on the page.

4. **Save the files.** Problem N → `docs/downloads/dasturlash/week-NN/pN.py`. The file must be exactly the code shown on the page.

5. **Navigation.** Add `Amaliyot: courses/dasturlash/week-NN/practice.md` under the week in `mkdocs.yml`, the practice link in `docs/courses/dasturlash/index.md`, and the "Bu haftaning amaliy qismi" line in `lecture.md`.

6. **Check.**
    - Run every file with the sample inputs and compare with the page character by character:

        ```bash
        printf "17\n5\n" | .venv/Scripts/python.exe docs/downloads/dasturlash/week-NN/p5.py
        ```

        (Set `PYTHONIOENCODING=utf-8` when output has emoji or o', g'.)
    - `.venv/Scripts/python.exe -m mkdocs build --strict`.

7. **Report** in simple English: problems added, every code change, statements you made more precise, checks run. Update `status.md`.
