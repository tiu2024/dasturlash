# University CS Course Knowledge Base

## Purpose and initial intent

I teach computer science courses at a university. I want one organized website where my students can easily read lecture notes, follow lab explanations, and download problem sets with solutions. The reading experience should resemble well-organized Python library documentation: clear navigation, search, readable explanations, and neatly formatted code.

Help me build and maintain both the website and its teaching content. Start small with one course and one complete topic, establish a consistent style, then expand to additional topics and courses. Prioritize student understanding, correct examples, easy navigation, and simple maintenance.

## Project approach

- Use MkDocs with Material for MkDocs, with content written in Markdown.
- Build a static documentation website; the initial hosting plan is GitHub Pages. University hosting can be used later.
- Organize by course and topic. Each topic can contain a lecture, lab, problem set, and separate solutions.
- Support downloadable problem sets, solution notes, source code, and datasets when needed. Generate PDFs only when requested.
- Keep the setup simple. Do not add a backend, database, login system, or complex agent framework unless I request one.
- Course names, syllabuses, teaching language, and student levels will be supplied in tasks. Sample content is a style reference, not an approved syllabus.

## Files and initial setup

- `mkdocs.yml`: site configuration and navigation.
- `docs/index.md`: course directory and home page.
- `docs/courses/<course>/<topic>/`: `lecture.md`, `lab.md`, `problems.md`, and `solutions.md`.
- `docs/downloads/<course>/<topic>/`: files students can download.
- `templates/`: reusable page templates, outside the published site.
- `sources/`: teacher-provided notes and references, read only when relevant.

Inspect the existing setup before creating files. If starting from an empty folder, create the minimal MkDocs configuration, dependencies, home page, templates, and one clearly labeled sample topic. If using the supplied starter project, adapt it instead of rebuilding it. Do not treat planned features as already implemented.

## Teaching content

- Match the language, prerequisites, and difficulty specified for the task. Preserve the established course language when unspecified; ask if a new course's language is unclear.
- For Uzbek lessons, write natural Uzbek and use consistent technical terminology; retain programming identifiers in their original form.
- Lectures: explanation, worked examples, and common mistakes. Do not add learning-objective ("O'quv maqsadlari") or practice-question ("Mashq savollari") sections.
- Labs: prerequisites, numbered actions, expected results, and exact submission requirements.
- Problems: unambiguous tasks, constraints, input/output formats where applicable, and examples.
- Solutions: reasoning, working code, and relevant ordinary and boundary checks. Match every solution to its problem.
- Use headings, short paragraphs, language-labeled code blocks, and relative links. Explain new concepts before using them.
- Use my source notes faithfully. Do not invent references, results, university policies, deadlines, or prerequisites. Flag missing teaching decisions briefly.
- Keep AI workflow instructions and editorial commentary out of student-facing pages.
- Everything in `docs/` may become public, including files absent from navigation. Keep unreleased solutions outside the published folder and any public repository.

## Efficient agent behavior

- Work on one requested topic or change at a time; avoid unrelated redesigns.
- Use one agent by default. Create subagents only when I explicitly request delegation or parallel work; give them separate file ownership.
- Read the target files, relevant sources, and at most one nearby style example. Use targeted searches rather than repeatedly scanning the whole project.
- Reuse available context and successful checks unless something relevant changes.
- Implement routine tasks directly. Use a short plan for substantial structural changes.
- Browse when facts or APIs are uncertain or version-sensitive, using official sources; avoid unnecessary research for basic concepts.
- Do not add dependencies, generate extra documents, or create elaborate workflows without a task-related need.
- Do not reprint entire files in chat. Finish with a short report of changes, checks, and unresolved decisions.
- These rules aim to reduce unnecessary context and repeated work; they do not impose a hard token budget.

## Verification and publishing

Use the project's Python virtual environment. Typical commands:

```bash
python -m pip install -r requirements.txt
python -m mkdocs serve
python -m mkdocs build --strict
```

Run changed runnable examples and relevant boundary cases. After content or configuration edits, run the strict build and check affected links and downloads. If execution is unavailable, say which checks could not run. A passing build does not replace my academic review.

Update navigation when adding pages. Preserve existing reviewed material. Do not commit, push, or deploy unless requested; when I request publishing, complete the checks and publish within that authorized scope.
