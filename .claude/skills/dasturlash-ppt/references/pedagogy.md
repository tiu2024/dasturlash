# Lecture design rules

Read this before planning a lecture. The builder's lint checks many of these rules; the planning decisions (what to cut, which misconception to target, where students do something) are yours.

## Contents
1. The lecture shape (80 minutes, also 70)
2. Slide design rules
3. Active-learning moments
4. Speaker notes
5. Turning slides, a book excerpt or notes into a lecture
6. Large lecture room

---

## 1. The lecture shape

Attention in a passive lecture drops after about 15–20 minutes, so a lecture is **three teaching segments separated by things students do**. Never let more than 20 minutes pass without an active slide (`retrieval`, `predict`, `quiz`, `livecode`, `activity`, `exit`); the builder warns.

### 80-minute template (default)

| Minutes | Block | Slide types |
|---|---|---|
| 0–1 | Title | `title` |
| 1–5 | Warm-up: 3 quick questions on **last** week | `retrieval` |
| 5–8 | Problem the lecture will solve | `hook` |
| 8–10 | 3–4 objectives | `objectives` |
| 10–33 | **Segment 1**: first concept, then a check | `section`, `assertion`, `code`, `predict` |
| 33–61 | **Segment 2**: main construct, call trace, quiz, live coding, activity | `section`, `code`, `quiz`, `livecode`, `activity` |
| 61–74 | **Segment 3**: extension / variant, then a check | `section`, `code`, `predict` |
| 74–80 | Recap + exit question | `recap`, `exit` |

- **70 min:** shorten segment 3 to 2–3 slides, or the activity to 6 minutes.
- **Two lectures in one file** (like `3_4_...`): two specs, two decks, or one spec of 160 min with a `break` in the middle. Ask the teacher.
- 24–30 slides for 80 minutes. Active slides take 3–10 minutes; content slides 2–3.

### Objectives
3–4 objectives with a measurable verb in Uzbek: *yoza oladi, kuzata oladi, tushuntira oladi, taqqoslay oladi, topa oladi*. Not *tushunadi, biladi, o'rganadi* (the builder warns). Every objective is practised by an active slide and repeated in the recap.

## 2. Slide design rules

From Mayer's multimedia principles and the assertion-evidence structure:

1. **Claim headline.** Every content slide's headline is a short full sentence that states the point, not a topic label. ≤ 2 lines, ≤ 14 words, no full stop.
   - Not: `Standart qiymat`
   - But: `Standart qiymat argument berilmaganda ishlatiladi`
2. **Evidence, not paragraphs.** The body shows the claim: code with its real output, a flow, a table, a term list, a figure. Bullets only when nothing else fits: ≤ 4 bullets of ≤ 12 words.
3. **One idea per slide.** Two claims = two slides.
4. **Signal the important part.** Highlight the line (`steps`), the cell, the key term (`**bold**`).
5. **Reveal step by step.** Traces, term lists and flows build one click at a time.
6. **Don't write what you will say.** Explanations go in the speaker notes.
7. **Keep labels next to what they label.** Step notes beside the code, output beside the code.
8. **Introduce a term before you rely on it.** One plain sentence the first time (course rule for beginners).

## 3. Active-learning moments

### `retrieval` (warm-up)
3 short questions on the previous week (not today's topic). Answers appear on click.

### `predict` (natijani toping)
5–10 lines of code; students write a prediction, compare with a neighbour, then you reveal and run it. Each one targets a **named misconception** (`misconception:`), e.g. "def darhol ishlaydi", "print qiymat qaytaradi", "= va == bir xil". With `choices`, each wrong choice is a plausible wrong belief, and `answer` starts with its letter ("B — 5").

### `quiz` (concept check / peer instruction)
One conceptual question, 4 choices, one correct. Write in `distractors` why each wrong choice is tempting. The voting protocol goes into the notes automatically.

### `livecode`
You code from the starter file to the solution: narrate, run often, make one realistic mistake (missing `:`, wrong indent, forgotten `int()`) and fix it aloud. ≤ 10 minutes, one small piece of functionality, **always followed by an `activity`**. Only use constructs already taught.

### `activity` (navbat sizda)
A variation of the live-coded program with explicit steps, a time limit, the starter file and an expected result to check against ("4 kg uchun 22000 chiqishi kerak"). Last step: an extension for fast students. Put a hint in `hint`.

### `exit`
1–2 questions on the main objective, answered on paper in the last 3 minutes. Optionally `next:` with next lecture's topic.

## 4. Speaker notes

Written in Uzbek (config `teaching.language`). Students download the deck with the notes, so write nothing you would not show them.
- 30–100 words per content slide: what to say, an everyday example, a question for the room, the link to the next slide.
- Active slides: the expected wrong answers and what to say after the reveal.
- The builder adds the timing (`⏱ 31–35-daqiqa (4 daq) · 4 ta bosish`), the activity protocol and the source.

## 5. Turning material into a lecture

1. Read everything first. Pick the **3–4 ideas** students must leave with; everything else is cut.
2. Find what students already know from earlier weeks (`docs/courses/dasturlash/week-*/lecture.md`). Use it in the warm-up; don't re-teach it.
3. Write the storyline: the claim headlines, in order, in three segments. Then choose the evidence for each.
4. List the misconceptions (book "common mistakes", exercises, your experience) → `predict` / `quiz`.
5. Book worked examples → `code` slides with `steps` or `output`, or the live-coding program.
6. Keep page references in `source:` (`"@narzullayev, 45-bet"`). Paraphrase; never paste book paragraphs onto slides.
7. If the teacher gave existing slides as the source, keep their topics and examples and do not add new topics: `/lecture-page` builds the student page from this deck.

## 6. Large lecture room

- Minimum sizes: headline 26 pt, body 22 pt, code 16 pt (the builder warns below these). Aim for code at 18–22 pt: ≤ 10 lines and ≤ 50 characters per line.
- Keep the default colours: black on white for content, navy/green for mode slides, one blue accent and an amber highlight. Pale colours vanish on projectors.
- Never let colour alone carry meaning: pair the highlight with a step note or a label.
- Give every image `alt` text and use images ≥ 1600 px wide.
