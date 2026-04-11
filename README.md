# Homepage

Personal academic website built on Jekyll/Academic Pages, with selected content synced from the LaTeX CV in `resume-main`.

## Content Model

- Static website pages:
  - `_pages/about.md`
  - `_pages/cv.md`
  - `_pages/projects.md`
  - `_pages/research.md`
  - `_pages/talks.md`
  - `_pages/teaching.md`
- Generated collections:
  - `_publications/`
  - `_talks/`
  - `_teaching/`
- Sync scripts:
  - `scripts/sync_from_resume.py`
  - `{resume-main}\automation\export_publications.py`

## What Syncs from `resume-main`

The website sync uses the LaTeX CV as the source of truth for:

- Work experience
- Skills
- Research interests
- Awards
- Academic activities
- Projects
- Publications
- Talks
- Teaching

The following stay hand-maintained on the website and are intentionally not overwritten by the sync:

- Education on `/` and `/cv/`
- Scholarships on `/projects/`

## Resume Repo Connection

The sync script does not require a hard-coded repo path in source control.

It resolves the CV repo from, in order:

1. `--resume-repo`
2. `HOMEPAGE_RESUME_REPO`
3. `.tmp/sync_from_resume.local.json`

Example first run:

```powershell
python .\scripts\sync_from_resume.py --resume-repo ..\resume-main
```

That command also saves the local path into `.tmp/sync_from_resume.local.json`, so later runs can use:

```powershell
python .\scripts\sync_from_resume.py
```

## Local Workflow

### 1. Sync from the LaTeX CV

```powershell
python .\scripts\sync_from_resume.py
```

### 2. Build the site

```powershell
bundle exec jekyll build --config _config.yml,_config_local.yml
```

### 3. Serve locally

```powershell
scripts\serve.bat
```

This serves the site at `http://localhost:5000`.

## Local Check

After serving locally, verify:

- `/`
- `/research/`
- `/talks/`
- `/teaching/`
- `/projects/`
- `/cv/`

<!-- Key expectations at the moment of this sync are:

- Research shows 5 journal papers, 4 conference proceedings, 4 working papers, and 1 patent.
- Talks shows 10 international conference presentations, 6 domestic conference presentations, and 3 seminar/research talks.
- Teaching shows 1 lecturer course and 2 teaching assistant entries.
- `/cv/` shows the synced work experience and skills, but keeps education as a static section.
- `/projects/` shows synced projects, but keeps scholarships as a static section. -->

## Notes

- `cv-json` and the old markdown-to-JSON CV workflow were removed.
- `.tmp/` is used for local-only planning and sync configuration and is gitignored.
- Generated collections are intended to be committed because the site renders from them.
