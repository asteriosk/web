# asterios.katsifodimos.com

Personal academic website and CV for [Asterios Katsifodimos](https://asterios.katsifodimos.com), Assistant Professor at TU Delft.

## What's in this repo

| Directory | Purpose |
|-----------|---------|
| `data/` | YAML source of truth — all content lives here, shared by website and CV |
| `web/` | Jekyll website, deployed to GitHub Pages |
| `cv/` | CV pipeline: Node.js + EJS templates → LaTeX → PDF |
| `Makefile` | Root-level build orchestration |

Content is edited **only in `data/*.yml`**. The website and CV both read from there — you never need to touch templates for routine updates.

## Quick start

```bash
make install   # Install Ruby gems (web) + npm packages (cv)
make preview   # Serve site at http://localhost:4000 (live reload)
make cv        # Generate LaTeX and compile PDF
make all       # Build both
```

## Editing content

All content is in `data/`. Each file maps to a section:

| File | Website page | Notes |
|------|-------------|-------|
| `publications.yml` | `/publications/` | Full publication list |
| `selected_publications.yml` | `/publications/` | Featured cards; references ids from publications.yml |
| `awards.yml` | Home | Grants, awards, honors |
| `supervision.yml` | `/people/` | PhD students, postdocs, master theses |
| `teaching.yml` | `/teaching/` | Courses by institution |
| `service.yml` | `/service/` | PC memberships, chairs |
| `employment.yml` | `/bio/` timeline | Also drives the CV employment section |
| `education.yml` | CV only | Degrees |
| `personal.yml` | CV only | Contact info, name |
| `funding.yml` | CV only | Grants with amounts |
| `invited_talks.yml` | CV only | Talks and keynotes |
| `referees.yml` | CV only | Reference contacts |

### `cv_only` flag

- `cv_only: true` — entry is included in the CV but hidden from the website
- `cv_only: {key: value}` — entry is shown on the website; the object carries CV-only metadata (e.g., `{funding: "NWO VIDI"}`)

### Career timeline

The `/bio/` timeline is generated from `employment.yml`. All entries without `cv_only: true` appear on the timeline. Education milestones (PhD, BSc/MSc) are stored in `employment.yml` with `cv_section: null`.

## Tech stack

- **Jekyll** — static site generator
- **Bootstrap 5** — layout and responsive grid (CDN)
- **Font Awesome 6** — icons (CDN)
- **Node.js + EJS** — CV template rendering
- **pdflatex + biber** — LaTeX → PDF compilation

## Deployment

The site deploys via **GitHub Actions** (`.github/workflows/deploy.yml`) on every push to `master` — not GitHub's native Jekyll build, which can't handle the `web/` subdirectory layout.

To set up on a new repo: Settings → Pages → Source → **GitHub Actions**.
