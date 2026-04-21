# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Repository Layout

```
website/
├── data/          # YAML source of truth — used by BOTH website and CV
├── web/           # Jekyll website (source for GitHub Pages)
├── cv/            # CV generation pipeline (Python Jinja2 → LaTeX → PDF)
├── Makefile       # Root-level build orchestration
└── AGENTS.md
```

**`data/`** is the single source of truth. All 12 YAML files (plus `check_dblp.py`) are consumed by:
- The Jekyll website via `site.data.*` Liquid variables — `web/_data` is a git symlink to `../data`
- The CV generator (`cv/generate.py`) which reads them directly

## Design Decisions

- **GitHub Actions instead of native Pages**: GitHub Pages' native Jekyll build can only serve from the repo root or `/docs`. Since the Jekyll source is in `web/`, we use GitHub Actions to build and deploy instead.
- **`web/_data` symlink instead of `data_dir` config**: Jekyll doesn't allow `..` in the `data_dir` config path, so `web/_data` is a git-tracked symlink pointing to `../data`. This lets Jekyll find the data files normally while keeping them at the repo root.
- **`cv_only` flag**: Entries with `cv_only: true` are hidden from the website but included in the CV. When `cv_only` is an object (e.g., `cv_only: {funding: "NWO VIDI"}`), the entry IS shown on the website — the object holds CV-specific metadata only. For `employment.yml`, `cv_only: true` also hides the entry from the website timeline.
- **Timeline derived from `employment.yml`**: The `/bio/` career timeline shows all `employment.yml` entries without `cv_only: true`. Education milestones (PhD, BSc/MSc) live in `employment.yml` as entries with `cv_section: null` — there is no separate `timeline.yml`.
- **`awards.yml` publication references**: `publication_id` must match an `id` slug in `publications.yml` (e.g., `stream-slicing-edbt19`), not a DBLP ID.
- **`selected_publications.yml`**: Contains only `id`, `desc`, and optional `award`. The `label`, `title`, `authors`, etc. are pulled from `publications.yml` by `id` — do not duplicate them here.
- **`teaching.yml` collaborators**: Use a `collaborators` list (`[{name, contribution?, link?}]`) instead of separate `collaborator_name`/`collaborator_link` fields. `contribution` (professor's share) and `collaborators[].contribution` are CV-only display values; `collaborators[].link` is shown on the website.

## Commands

```bash
make preview     # Serve website locally at localhost:4000 (live reload)
make web         # Build website to web/_site/
make cv          # Generate LaTeX from data/ + compile PDF
make all         # Build both website and CV
make install     # Install Ruby gems (web) and npm packages (cv)
make clean       # Remove web/_site/ and cv/output/ build artifacts
make dblp-update # Interactive wizard: compare publications.yml against DBLP

# CV only:
cd cv && make generate   # YAML → LaTeX (Jinja2 templates)
cd cv && make pdf        # generate + pdflatex → PDF
```

**After any change to `data/*.yml`, `cv/templates/*.j2`, or any `.tex` file in `cv/`, always run `make cv` from the repo root to regenerate and recompile the PDF.**

## Deployment

GitHub Pages is deployed via GitHub Actions (`.github/workflows/deploy.yml`) — **not** by GitHub's native Jekyll build. This is required because the Jekyll source is in `web/` (not the repo root) and uses `data_dir: ../data` to reach `data/`.

On every push to `master`, the workflow:
1. Builds Jekyll from `web/` with `JEKYLL_ENV=production`
2. Uploads `web/_site/` as a Pages artifact
3. Deploys to `https://asterios.katsifodimos.com`

**One-time setup**: GitHub repo → Settings → Pages → Source must be set to "GitHub Actions".

## Data maintenance

`data/check_dblp.py` — interactive wizard that fetches the DBLP XML for Asterios Katsifodimos and walks you through adding missing entries to `publications.yml` one by one. Run via `make dblp-update` or directly:

```bash
python3 data/check_dblp.py                        # live fetch
python3 data/check_dblp.py --local /tmp/dblp.xml  # use saved XML
python3 data/check_dblp.py --year-from 2020        # limit to recent years
```

For each missing entry the wizard prompts for the two manual fields (`id` slug and `label`), then prepends the completed YAML block to `publications.yml`. Run `make cv` afterwards.

## Subsystem docs

- **`web/AGENTS.md`** — pages, includes, data→Liquid mapping, Liquid gotchas, nav active state
- **`cv/AGENTS.md`** — known LaTeX/Jinja2 bugs, pre-flight checklist, visual inspection patterns

## CV Pipeline

```
data/*.yml  →  cv/generate.py (Python + Jinja2)  →  cv/output/*.tex  →  build.sh (pdflatex + biber)  →  cv/output/*.pdf
```

- **Generator**: `cv/generate.py` — reads all YAML, renders 13 Jinja2 templates, writes `.tex` files to `cv/output/`
- **Templates**: `cv/templates/*.tex.j2` — Jinja2 syntax with `(( ))` variables and `(% %)` blocks (custom delimiters to avoid LaTeX `{}` conflicts), one per CV section
- **Output**: `cv/output/` — generated files, gitignored
- **Compilation**: `cv/build.sh` — runs `biber` then `pdflatex` twice
- **Dependencies**: `pip3 install -r cv/requirements.txt` (jinja2, pyyaml)

Template helper functions (registered as both filters and globals):
- `escape_latex(text)` — escapes LaTeX special chars
- `format_date(date_str)` — `"2021-06"` → `"June 2021"`
- `format_year_range(start, end)` — `"2020--present"` or `"2020--2025"`
- `split_name(full_name)` — `{first, last}`
- `format_birth_date(iso_date)` — full date string
- `get_bib_entry_type(pub)` — maps pub label to BibTeX entry type
- `format_bib_authors(authors)` — comma-sep → BibTeX `and`-sep, bolds author name
- `regex_search(value, pattern)` — returns first capture group or empty string

## YAML Schemas

### publications.yml
```yaml
- id: unique-slug              # referenced by selected_publications.yml
  year: 2025
  label: "SIGMOD'25"
  title: "Paper Title"
  authors: "Author Names"
  venue: "Full venue name"
  pdf: "https://..."           # or relative path (optional)
  link: "https://..."          # DOI or project page (optional)
  github: "https://..."        # (optional)
  slides: "path/to/slides.pdf" # (optional)
  poster: "path/to/poster.pdf" # (optional)
  extended: "..."              # (optional); extended version note
  award: "ACM SIGMOD Best Paper 2025"  # (optional)
```

### selected_publications.yml
```yaml
- id: styx-sigmod25            # must match an id in publications.yml; label/title/authors etc. are pulled from there
  desc: "Short description shown on the card."
  award: "Optional award text" # (optional) overrides award in publications.yml
```

### awards.yml
```yaml
- name: "NWO VIDI"
  year: 2024
  type: "grant"                # award | grant | honor
  description: "Optional text" # (optional)
  publication_id: "slug"        # (optional) must match an id in publications.yml
  cv_only: true                # true = CV only, false/omitted = show on website
```

### supervision.yml
```yaml
phd_students:
  - name: "Full Name"
    link: "https://..."
    advisor_present: true
    advisor: "Main Advisor"
    start_year: 2023
    end_year:                  # omit if still active
    present: true
    position: "PhD Candidate"  # or "Now Postdoc at X" for alumni
    topic: "Research topic"
    photo: "/assets/people/name.jpg"  # optional; initials badge if omitted
    cv_only:                   # optional object with CV-specific metadata
      funding: "NWO VIDI"

postdocs:
  - name: "Full Name"
    link: "https://..."
    start_year: 2023
    end_year:                  # omit if still active
    position: "Now Postdoc at X"
    topic: "Research topic"
    photo: "/assets/people/name.jpg"  # optional

masters:
  - year: 2025
    name: "M.S. Patil"
    link: "https://repository.tudelft.nl/..."
    topic: "Thesis Title"
    initials: "MP"             # optional override for badge
    institution: "TU Delft"
    advisor: "..."             # optional; advisor name (rarely used)

research_engineers:             # CV only
  - name: "Full Name"
    start_year: 2022
    start_month: 2
    end_year: 2022
    end_month: 12
    position: "Research Engineer"
    collaborator: "Colleague Name"  # optional
    cv_only: true

interns:                        # CV only
  - name: "Full Name"
    program: "TU Delft Honors Programme"
    period: "Winter 2022"
    cv_only: true
```

### teaching.yml
```yaml
- institution: TU Delft
  location: "Delft, Netherlands"
  start_year: 2017
  end_year:                    # omit if still teaching here
  courses:
    - id: CS4225               # optional
      name: "Course Name"
      link: https://...        # optional
      level: MSc               # MSc | BSc | ProfEd
      period: Q2
      start_year: 2017
      end_year:                # optional
      description: "Short description"
      contribution: "80%"      # optional; professor's share, shown in CV only
      department: "External School"  # optional; course department (e.g., ProfEd)
      collaborators:           # optional; co-instructors
        - name: "C. Lofi"
          contribution: "20%"  # optional; their share, shown in CV only
          link: "https://..."  # optional; shown on website
```

### service.yml
```yaml
intro: "Introductory text."

chairs:
  - venue: "ICDE 2027"
    role: "Tutorial Chair"
    year: 2027                 # or year_start/year_end for ranges
    cv_only: false

pc_member:
  - venue: "(P)VLDB"
    years: "2015, 2017–2021, 2023–2027"  # comma/semicolon-separated or ranges
    link: https://...          # optional
    cv_only: false             # optional; true = CV only

special_service:               # CV only — not shown on website
  - role: "Dutch Seminar on Data Systems Design"
    role_detail: "Co-founder"
    year: 2020
    cv_only: true
```

### timeline (website only)
The career timeline on `/bio/` is derived from `employment.yml`. All entries without `cv_only: true` are shown. Education milestones (PhD, BSc/MSc) are included as entries in `employment.yml` with `cv_section: null`.

### personal.yml (CV only)
```yaml
name: "Asterios Katsifodimos"
title: "Assistant Professor"
institution: "Delft University of Technology"
secondary_title: "Amazon Scholar at AWS"
contact:
  email: "..."
  phone: "..."
  address: "..."
  homepage: "..."
social:               # optional; external profile links
  - platform: "Google Scholar"
    url: "https://..."
birth_date: "1985-09-16"
```

### education.yml (CV only)
```yaml
- level: "PhD in Database Systems"
  institution: "Université Paris-Sud & Inria Saclay"
  location: "Paris, France"
  year_start: 2009
  year_end: 2013
  thesis:
    title: "..."
    honor: "Mention Très Honorable"
    advisor: "Dr. Ioana Manolescu"
    reviewers:              # optional; list of reviewer names (PhD only)
      - "Prof. Yanlei Diao"

- level: "MSc"
  institution: "University of Cyprus"
  program: "Advanced Information Technologies"  # optional; MSc/BSc only
  location: "Nicosia, Cyprus"
  year_start: 2007
  year_end: 2009
  thesis:
    title: "..."
    advisor: "Prof. Marios D. Dikaiakos"
```

### employment.yml
```yaml
- year: "2025–present"
  current: true
  organization: "AWS"
  role: "Amazon Scholar"
  department: "..."
  location: "..."
  icon: "fa-solid fa-cloud"
  cv_section: "employment"  # null = website-only entry (e.g., education milestones)
  advisor: "..."            # optional; for roles with an advisor (e.g., TU Berlin researcher)
  cv_only: true             # optional; hides from website timeline
  cv_details:
    - "Detail bullet point..."
```

### funding.yml (CV only)
```yaml
- name: "H2020 OpertusMundi"
  amount: "€620K for TU Delft"
  description: "Two PhDs, two-year postdoc"
  role: "Co-Proposer"
  year_start: 2020
  year_end: 2022
  type: "grant"
  cv_only: true                # optional; hidden from website (most entries)
```

### invited_talks.yml (CV only)
```yaml
- title: "Talk Title"
  venue: "Data Lab, Northwestern University"
  location: "Boston, USA"
  date: "2021-12"              # YYYY-MM
  end_date: "2021-12"          # optional; YYYY-MM for multi-day events
  type: "invited_talk"         # or "keynote"
  description: "Optional description"  # optional
  link: "https://..."          # optional
```

### referees.yml (CV only)
```yaml
- name: "Prof. Dr. Ioana Manolescu"
  affiliation: "École Polytechnique de Paris & INRIA Saclay"
  email: "..."
  relationship: "PhD supervisor, co-author"
```

## Navigation active state

The navbar underlines the active section by comparing `page.url` against each nav link in `web/_layouts/default.html`. When adding a new top-level section, add the page and a nav entry there.
