# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

This is a **Jekyll 4.4** academic personal website. It uses a single layout (`_layouts/default.html`) for all pages. Frontend uses Bootstrap 5.3.3 and Font Awesome 6.7.2 via CDN. All custom styles are in `css/theme.css`.

### Data-driven content

The three main content areas are driven entirely by YAML data files — no content changes require editing HTML or Liquid templates:

- `_data/publications.yml` — all papers, grouped by year, rendered on `/publications/`
- `_data/selected_publications.yml` — 6 curated papers shown as cards on `/publications/`; references entries by `id` from the full list
- `_data/supervision.yml` — three arrays: `phd_students`, `postdocs`, `masters`; rendered on `/supervision/`
- `_data/teaching.yml` — institutions with nested course arrays, rendered on `/teaching/`

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

### Supervision entry structure

PhD students and postdocs use a `photo` field (path under `/assets/people/`). If omitted, a circular badge with auto-generated initials is rendered instead. Master students use `initials` (optional override) and link to their thesis repository.

### Includes

- `_includes/pub-highlight.html` — publication card (venue badge + title + authors + links)
- `_includes/student-card.html` — single person card
- `_includes/people-list.html` — wraps multiple student cards in a flex grid

### Navigation active state

The navbar underlines the active section by comparing `page.url` against each nav link in `_layouts/default.html`. When adding a new top-level section, add both the page and a nav entry there.
