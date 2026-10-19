---
name: publish
description: Publish reviewed course changes to GitHub and GitHub Pages - strict build, commit, push, gh-deploy, check the live site. Run only when the teacher explicitly asks to publish or deploy.
disable-model-invocation: true
---

# Publish the site

Site: https://tiu2024.github.io/dasturlash/ · Repo: github.com/tiu2024/dasturlash (public). Full background: `DEPLOY.md`.

## Steps

1. **See what will be published.** `git status` and `git diff --stat`. Tell the teacher in one short list.
2. **Privacy check.** Nothing private may be staged or inside `docs/`:
    - no files from `OQ/`, no `.docx`, no `.claude/skills/oquv-dastur/` or `.claude/skills/adabiyot-tanlash/`;
    - no unreleased solutions or drafts in `docs/`.

    Confirm with `git check-ignore -v OQ .claude/skills/oquv-dastur .claude/skills/adabiyot-tanlash`. If something private would be published, stop and ask.
3. **Build.** `.venv/Scripts/python.exe -m mkdocs build --strict`. If it fails, fix the cause and run it again.
4. **Commit** the changes with a short message describing them (ask the teacher only if the scope is unclear).
5. **Push.** `git push`.
6. **Deploy.** `.venv/Scripts/python.exe -m mkdocs gh-deploy`.
7. **Check the live site** after about a minute: the home page and the pages that changed open.
8. **Report:** commit hash, what was published, the URL, any problem. Update the "Published" column in `status.md`.
