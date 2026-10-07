# Status

## Session 2026-10-05

Reviewed the starter project and converted it into the Uzbek "Dasturlash 1, 2" site. The PPTX lectures are published as downloads, one lecture per week.

**Created**
- `docs/courses/dasturlash/ai-guide.md`: AI usage memo and starter prompt in English, Uzbek, Russian
  (prompt adapted; "Reading and Learning guide" sources section added)
- `.venv/`: virtual environment with the requirements installed
- `docs/courses/dasturlash/index.md`, `week-01/lecture.md`, `week-02/lecture.md`, `week-03/lecture.md`
- `docs/downloads/dasturlash/week-01/dasturlash-ga-kirish.pptx`
- `docs/downloads/dasturlash/week-02/python-dasturlash-kirish.pptx`
- `docs/downloads/dasturlash/week-03/funksiyalar-shartlar-scope-turlar.pptx`
- `status.md`

**Changed**
- `docs/courses/dasturlash/week-01/lecture.md`: full lecture 1 draft (from CS50 week 0, no Scratch/VS Code), Python examples; source link removed
- `mkdocs.yml`: site name, description, navigation (AI page before week 1), tabs extension
- `docs/index.md`: Uzbek home page
- `docs/courses/dasturlash/index.md`: link to the AI page
- `README.md`: rewritten in Uzbek and shortened

**Removed**
- `docs/courses/programming/`: the English sample topic
- `docs/downloads/programming/`: the sample downloads

**Checks:** `mkdocs build --strict` passes.

**Open:**
- Week 1: practice questions have no solutions; lab and problems pages
- Weeks 2 and 3: lecture pages are still download links only
- Narzullayev book link is a store page; review the Uzbek/Russian prompt translations and the source descriptions
- `git init` for GitHub Pages (`sources/` folder not created)

## Earlier sessions

No record is available. Only this session's work could be listed.
