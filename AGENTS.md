# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Commands

```bash
make preview          # Serve locally at localhost:4000 (with live reload)
make all              # Build to _site/
make install          # Install gem dependencies

bundle exec jekyll serve --baseurl ''   # Manual serve equivalent
bundle exec jekyll build                # Manual build equivalent
```

Deployment is automatic via GitHub Pages on push to `master`. No manual deploy step needed.

## Architecture

This is a **Jekyll 4.4** academic personal website. It uses a single layout (`_layouts/default.html`) for all pages. Frontend uses Bootstrap 5.3.3 and Font Awesome 7.0.1 via CDN. All custom styles are in `css/theme.css`.

### Pages

| Page | File | Nav link |
|------|------|----------|
| Home (bio, awards) | `index.md` | brand link |
| People | `people/index.md` | ✅ |
| Publications | `publications/index.md` | ✅ |
| Teaching | `teaching/index.md` | ✅ |
| Service | `service/index.md` | ✅ |
| Bio / Timeline | `bio/index.md` | — (linked from home) |

Legacy pages (no nav entry): `theses/`, `jobs/`, `recipes/`.

### Data-driven content

The main content areas are driven entirely by YAML data files — no content changes require editing HTML or Liquid templates:

- `_data/publications.yml` — all papers, grouped by year, rendered on `/publications/`
- `_data/selected_publications.yml` — curated papers shown as cards on `/publications/`; references entries by `id` from the full list
- `_data/supervision.yml` — three arrays: `phd_students`, `postdocs`, `masters`; rendered on `/people/`
- `_data/teaching.yml` — institutions with nested course arrays, rendered on `/teaching/`
- `_data/service.yml` — `intro`, `chairs`, and `pc_member` arrays; rendered on `/service/`
- `_data/awards.yml` — awards and grants shown on the home page; each entry has `name` and `type` (`award` or `grant`)
- `_data/timeline.yml` — career timeline entries rendered on `/bio/`; each entry has `year`, `icon`, `title`, `org`, optional `detail` and `current`

**Convention: no HTML in `_data/` files.** All fields must be plain text. Presentation (icons, links, badges) is handled exclusively in templates and includes. For structured links (e.g. a collaborator), use separate `_name` / `_link` fields and let the template render the anchor tag.

### Publication entry structure

```yaml
- id: unique-slug          # referenced by selected_publications.yml
  year: 2025
  label: "SIGMOD'25"       # short venue badge
  title: "Paper Title"
  authors: "Author Names"
  venue: "Full venue name"
  pdf: "https://..."        # or relative path
  link: "https://..."       # DOI or project page
  github: "https://..."
  slides: "path/to/slides.pdf"
  poster: "path/to/poster.pdf"
  award: "ACM SIGMOD Best Paper 2025"  # plain text; icon injected by template
```

### Selected publication entry structure

```yaml
- id: styx-sigmod25        # must match an id in publications.yml
  desc: "Short description of the paper shown on the card."
  award: "Optional award text"  # optional
```

### Teaching entry structure

```yaml
- institution: TU Delft
  start_year: 2017
  end_year:               # omit or leave empty if still active
  courses:
    - id:                 # course ID (e.g. CS4225), fill when known
      name: "Course Name"
      link: https://...   # omit if none
      level: MSc          # MSc / BSc / ProfEd
      period: Q2          # quarter (TU Delft) or season semester (TU Berlin)
      start_year: 2017
      end_year:           # omit or leave empty if still teaching
      description: "Short description"
      collaborator_name:  # optional
      collaborator_link:  # optional
```

### Service entry structure

```yaml
intro: "Introductory text shown above the lists."

chairs:
  - venue: "ICDE 2027"
    role: "Tutorial Chair"

pc_member:
  - venue: "(P)VLDB"
    years: "2015, 2017–2021, 2023–2027"
    link: https://...     # optional
```

### Awards entry structure

```yaml
- name: "ACM SIGMOD Systems Award 2023"
  type: award             # award or grant
```

### Timeline entry structure

```yaml
- year: "2025–"
  current: true           # optional; marks ongoing positions
  icon: fa-solid fa-cloud
  title: "Amazon Scholar"
  org: "AWS"
  detail: "Deep Science for Systems Group (DS3)"  # optional
```

### Supervision entry structure

PhD students and postdocs:

```yaml
- name: "Full Name"
  link: "https://..."
  advisor_present: true       # PhD only
  advisor: "Main Advisor"     # PhD only
  start_year: 2023
  end_year:                   # omit if still active
  present: true               # optional; marks current members
  position: "PhD Candidate"   # or "Now Postdoc at X" for alumni
  topic: "Research topic"
  photo: "/assets/people/name.jpg"  # optional; initials badge if omitted
```

Master students:

```yaml
- year: 2025
  name: "M.S. Patil"
  link: "https://repository.tudelft.nl/..."  # thesis link
  topic: "Thesis Title"
  initials: "MP"              # optional override for badge
  institution: "TU Delft"
```

### Includes

- `_includes/pub-highlight.html` — publication card (venue badge + title + authors + links)
- `_includes/student-card.html` — single person card
- `_includes/people-list.html` — wraps multiple student cards in a flex grid

### Navigation active state

The navbar underlines the active section by comparing `page.url` against each nav link in `_layouts/default.html`. When adding a new top-level section, add both the page and a nav entry there.
