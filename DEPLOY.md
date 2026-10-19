# Publishing the site on GitHub Pages

These steps publish the course site at `https://<USERNAME>.github.io/<REPO>/`. Run commands in PowerShell from the project folder. This file is outside `docs/`, so it is not published.

## Before you start

- You need a GitHub account and Git installed (`git --version`).
- Everything under `docs/` becomes public: lecture pages, practice solutions and the files in `docs/downloads/`. Remove anything unreleased before publishing.
- GitHub Pages is free for **public** repositories. A private repository needs a paid GitHub plan.
- The `Lectures/` folder (original PPTX files), `status.md`, `CLAUDE.md` and `.claude/` (except the gitignored official-document skills) are committed to the repository. They are not part of the website, but they are visible if the repository is public. Add them to `.gitignore` or remove them from the repository if you do not want that.

## One-time setup

1. **Create the repository.** On github.com choose *New repository*, name it (for example `dasturlash`), keep it **empty** (no README, no .gitignore, no license), and create it.

2. **Set the site address.** In `mkdocs.yml` uncomment `site_url` and fill it in:

    ```yaml
    site_url: https://<USERNAME>.github.io/<REPO>/
    ```

    Then commit the change:

    ```powershell
    git add mkdocs.yml
    git commit -m "Set site_url"
    ```

3. **Connect the project and push the source code.** The project is already a Git repository on the `main` branch.

    ```powershell
    git remote add origin https://github.com/<USERNAME>/<REPO>.git
    git push -u origin main
    ```

    A browser window or prompt asks you to sign in to GitHub the first time.

4. **Build and deploy the site.** Check the build first, then publish:

    ```powershell
    .\.venv\Scripts\python.exe -m mkdocs build --strict
    .\.venv\Scripts\python.exe -m mkdocs gh-deploy
    ```

    `gh-deploy` builds the site and pushes it to a branch named `gh-pages` (created automatically). The source code stays on `main`.

5. **Turn on Pages.** In the repository open *Settings → Pages*. Under *Build and deployment* set *Source* to **Deploy from a branch**, branch **gh-pages**, folder **/ (root)**, and save.

6. **Open the site.** After one or two minutes it is live at `https://<USERNAME>.github.io/<REPO>/`. The address is also shown at the top of the *Pages* settings screen.

## Publishing updates

After editing the lessons:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
git add -A
git commit -m "Describe the change"
git push
.\.venv\Scripts\python.exe -m mkdocs gh-deploy
```

`git push` saves the source on `main`; `gh-deploy` updates the published site. Do both. Preview locally first with `mkdocs serve` (see `README.md`).

## Troubleshooting

| Problem | Fix |
|---|---|
| Site shows 404 | Check *Settings → Pages* uses branch `gh-pages` and folder `/ (root)`; wait a few minutes. |
| Pages loads without styles or with broken links | `site_url` in `mkdocs.yml` is missing or wrong (it must end with `/`). Fix it and run `gh-deploy` again. |
| `build --strict` fails | Read the first warning; it names the file and the broken link or navigation entry. Fix it before deploying. |
| `git push` is rejected | The GitHub repository was created non-empty. Run `git pull origin main --rebase`, then push again. |
| Sign-in loop on push | Install GitHub CLI and run `gh auth login`, or create a personal access token and use it as the password. |
| Line-ending warnings (`LF will be replaced by CRLF`) | Harmless on Windows. |

## Optional: deploy automatically with GitHub Actions

Instead of running `gh-deploy` yourself, the site can be rebuilt on every push. Add `.github/workflows/pages.yml`:

```yaml
name: Deploy site
on:
  push:
    branches: [main]
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict
      - run: mkdocs gh-deploy --force
```

Keep the Pages source set to branch `gh-pages` as in step 5. If you use this workflow, you only need `git push`.
