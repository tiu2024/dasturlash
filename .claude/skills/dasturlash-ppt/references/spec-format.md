# Lecture spec format (`lecture.yaml`)

One YAML file per lecture, in `Lectures/src/week-NN/lecture.yaml`. The builder turns it into the deck and the live-coding files. Complete working example: `examples/week-03-funksiyalar.yaml`.

## Contents
1. File layout
2. `meta`
3. `objectives` and `livecode`
4. Slides: common fields
5. Slide types
6. Evidence kinds
7. Inline markup and quoting

---

## 1. File layout

```yaml
config: ../../config.yaml     # course settings (found automatically if omitted)
meta: {...}
objectives: [...]
livecode: {...}
slides: [...]
```

`Lectures/config.yaml` supplies the lecturer, university, group, academic year, lecture length, code language, slide language, colours, fonts and the book list. Anything in `meta` or `theme` in the spec overrides it for this lecture only. Paths (images) are relative to the spec.

## 2. `meta`

| Key | Meaning |
|---|---|
| `title` | Lecture title (title slide) — required |
| `subtitle` | e.g. `5-ma'ruza · ro'yxatlar` |
| `deck_file` | Output deck, relative to the spec: `../../5_Royxatlar.pptx`. Default `build/<slug>.pptx` |
| `duration_min` | Override `teaching.lecture_minutes` |
| `language` | Override the code language (`python`, `c`) |
| `source` | Default footer citation for this lecture; `@id` expands from the config book list |
| `builds`, `transitions`, `line_numbers` | Override the config `slides` settings |

An existing `deck_file` is never overwritten unless the build is run with `--force`.

## 3. `objectives` and `livecode`

```yaml
objectives:                     # 3–4, measurable Uzbek verbs (yoza oladi, kuzata oladi…)
  - "`def` va `return` bilan o'z funksiyasini **yoza oladi**"
livecode:                       # written to livecode/starter and livecode/solution (gitignored)
  run: ".venv/Scripts/python.exe taksi.py"
  files:
    - name: taksi.py
      starter: |
        # izohlar: nima yozilishi kerak
      solution: |
        def taksi_narxi(km):
            return 5000 + km * 2000
    - name: test_taksi.py       # `both:` = same file in both folders
      both: |
        ...
```

## 4. Slides: common fields

| Key | Meaning |
|---|---|
| `type` | Slide type (below) |
| `minutes` | Planned time; defaults: title 1, retrieval 4, hook 3, objectives 2, section 0.5, assertion 2.5, code 4, predict 4, quiz 5, livecode 10, activity 10, compare 3, recap 3, exit 3, break 4 |
| `notes` | Speaker notes in Uzbek; timing, protocol and source are added automatically |
| `source` | Footer citation for this slide, e.g. `"@thinkpython, 3-bob"` |
| `kicker` | Small label above the headline; default = current section title or the slide's role |
| `build` | `false` = show everything at once on this slide |

## 5. Slide types

**`title`** — uses meta and config. Optional `title`, `subtitle`.

**`retrieval`** — warm-up on last week.
```yaml
- type: retrieval
  headline: "O'tgan haftadan uchta savol"       # optional
  items:
    - {q: "`print(int(\"42\") + 8)` nimani chiqaradi?", a: "50 — `int()` satrni songa aylantiradi"}
```

**`hook`** — `question:` (large text) + optional `evidence:`.

**`objectives`** — uses lecture `objectives`; optional `headline`.

**`section`** — `title:`; sets the kicker for the slides after it.

**`assertion`** — `headline:` + `evidence:` and/or `points:` (≤ 4). Both → points left, evidence right.

**`code`**
```yaml
- type: code
  headline: "Standart qiymat argument berilmaganda ishlatiladi"
  code: |
    def hello(to="Jigarlar"):
        print("Salom,", to)


    hello("Aziz")
    hello()
  output: |                 # real output (run the code!); appears on click beside or under the code
    Salom, Aziz
    Salom, Jigarlar
  # OR steps (not both): click-through highlights with notes on the right
  steps:
    - {lines: [1], note: "Standart qiymat: \"Jigarlar\""}
    - {lines: "5-6", note: "Argument bor / yo'q"}
```
For `input()`, write the typed value into `output` as the user sees it: `Ismingiz? Aziz`.

**`predict`** — `code`, optional `question` (default "Bu kod nimani chiqaradi?"), optional `choices`, `answer` (start with the letter if choices: `"B — 5"`), short `explanation`, `misconception` (notes only).

**`quiz`** — `question`, 4 `choices`, `correct` (0-based index), short `explanation`, `distractors` (notes only).

**`livecode`** — `title`, `file` (a `livecode.files` name), 2–4 `goals`, `minutes`.

**`activity`** — `title`, `file`, `steps` (3–4, last one an extension), `pairs: true`, `hint` (notes only), `minutes`.

**`compare`** — `headline`, `left: {title, points | evidence}`, `right: {...}`.

**`recap`** — 3–5 `points` (claims, one per objective).

**`exit`** — 1–2 `questions`, optional `next:` ("Keyingi ma'ruza: …").

**`break`** — `minutes`, optional `message`.

## 6. Evidence kinds

```yaml
{kind: code, code: "...", steps: [...]}                       # code panel
{kind: output, text: "11000\n19000"}                          # program output box
{kind: flow, nodes: ["3.7", "round", "4"],                    # ≤ 5 boxes, built left → right
       labels: ["argument", "funksiya", "qaytgan qiymat"]}   # optional captions under boxes
{kind: terms, items: [{term: "def", means: "yangi funksiya yaratadi"}, ...]}   # term → meaning rows
{kind: table, rows: [["Operator", "Ma'nosi"], [">", "katta"]]}                 # first row = header
{kind: array, cells: ["a", "b", ""], indices: true, steps: [{cells: [0], note: "..."}]}
{kind: image, path: figures/x.png, alt: "...", caption: "..."}
{kind: bullets, points: [...]}
```

## 7. Inline markup and quoting

- `**bold**` for the key term, `` `code` `` for code inside text.
- Write `o'` and `g'` with the ordinary apostrophe; typographic `‘ ’ ʻ` in slide text are converted, in code they are flagged.
- Quote YAML strings that contain `:` or `#`, or start with `` ` ``, `*`, `[`, `{` or `"`. Inside double quotes write `\"` for a quote. Use `|` blocks for code.
