# Working with Codex on course materials

## A simple weekly workflow

1. You choose the topic, language, student level, learning objectives, and prerequisites.
2. Give Codex the relevant source notes and exact target folder. Ask it to create one topic using the templates.
3. Codex writes the pages, checks runnable examples, and builds the site.
4. You read the lesson as a student: check correctness, terminology, pacing, and task difficulty.
5. Ask for specific revisions, then commit the reviewed version. Publish when ready.

Start with one course and one topic. Once you approve the teaching style, tell Codex to use that topic as the reference for later lessons.

## What AGENTS.md does

The root `AGENTS.md` gives Codex reusable project guidance: scope, content conventions, checks, and short reporting. Codex discovers these instructions at session startup. After changing them, start a fresh session to reliably load the new version. There is no need to paste the whole file into every prompt.

Keep permanent instructions there; put the current topic, deadlines, and requested deliverables in your task. Templates hold the page structure. Avoid repeating the same rules in several places.

These are instructions, not a token cap or security mechanism. They can reduce unnecessary reading, repeated checks, and long responses; actual usage depends on task size and your client. Short final answers alone do not guarantee low total usage.

## Give a task with four details

| Detail | Example |
|---|---|
| Goal | Create the lesson and lab on Python functions |
| Context | My notes are in `sources/functions.txt`; use week-01 as the style example |
| Constraints | First-year students, Uzbek, 45-minute lecture, no recursion |
| Done when | Four pages exist, examples run, links work, strict build passes |

Store source notes outside `docs/`, such as in a `sources/` folder. Only put material in a public repository if it is suitable for sharing.

## Copyable prompts

### Create a topic

```text
Create week-02 on Python functions in docs/courses/programming/week-02/.
Audience: first-year students who know variables, conditions, and loops.
Language: Uzbek; retain Python identifiers in English.
Use templates/ and week-01 as the style reference.
Create a 45-minute lecture, a 60-minute lab, three practice problems,
and matching solutions. Include downloadable .txt problem/solution notes
and .py code. Explain parameters, return values, and local variables;
exclude recursion and decorators. Update mkdocs.yml and relevant links.
Run the examples, check ordinary and boundary cases, and run the strict build.
Report changed files, checks, and any teaching decisions I should review.
```

If you have notes, add their exact path and say whether Codex may supplement them. Do not reference a file that you have not actually provided.

### Revise a section

```text
Revise only the Worked example section of
 docs/courses/programming/week-02/lecture.md.
Use a student-grade example and explain each step for beginners.
Preserve the objectives and other sections. Run the changed code
and the strict build. Give a short summary.
```

### Review academic quality

```text
Review week-02 for incorrect claims, prerequisite gaps, unclear Uzbek
terminology, and inconsistent problem/solution pairs. Read only that topic
and its downloadable code. Report issues with file locations and proposed
corrections. Do not edit yet.
```

### Resume in a fresh session

```text
Continue week-02. The lecture and lab are reviewed; only problem 3 and its
solution need revision. Use the current files as the source of truth.
Keep the established style. Update affected downloads and run relevant checks.
```

### Publish reviewed work

```text
Publish the reviewed course website to the configured GitHub Pages repository.
Run the strict build first. If it fails, fix the relevant issue and rerun it.
Deploy after the checks pass, and report the website URL and deployment result.
```

## Practical ways to save context and effort

- Name target files and a clear completion condition; broad requests cause broad exploration.
- Prefer one topic per task. Combine closely related edits instead of asking for the same changes in several turns.
- Continue in the same session while revising that topic. Start a fresh session for a different topic or when the conversation has accumulated unrelated material.
- Provide the relevant excerpt or source file, rather than many unrelated PDFs.
- Ask for changes directly once the structure is settled. Use planning for a new course structure or a substantial redesign.
- Start with the client's default reasoning setting. Increase it when the task requires difficult debugging or algorithmic reasoning; routine formatting usually needs less.
- Use one agent by default. If you explicitly request parallel work, give each agent a separate topic folder and let one agent update shared navigation afterward.
- Keep validation: incorrect code and broken links cost more time to repair after publication. Skip repeated passing checks only when nothing relevant has changed.
- Request a short completion report instead of reprinting whole lessons. Read the edited files in your editor or browser.
- Change rules when a recurring problem appears; do not add lengthy instructions for hypothetical problems.

Teacher review remains essential: a successful build checks the website, not whether the explanation teaches the concept well.
