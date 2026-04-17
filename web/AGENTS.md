# AGENTS.md — Website (Jekyll)

Jekyll 4.4, Bootstrap 5.3.3, Font Awesome 7.0.1 (CDN). Single layout: `_layouts/default.html`.

## Pages

| Page | File | Nav |
|------|------|-----|
| Home (bio, awards) | `index.md` | brand link |
| People | `people/index.md` | ✅ |
| Publications | `publications/index.md` | ✅ |
| Teaching | `teaching/index.md` | ✅ |
| Service | `service/index.md` | ✅ |
| Bio / Timeline | `bio/index.md` | linked from home |

Legacy pages (no nav): `theses/`, `jobs/`, `recipes/`.

## Includes

- `_includes/pub-highlight.html` — publication card (venue badge + title + authors + links)
- `_includes/student-card.html` — person card (photo/initials + name + years + topic)
- `_includes/people-list.html` — flex grid wrapper for student cards

## Data files → Liquid variables

| File | Page | Liquid variable |
|------|------|----------------|
| `publications.yml` | `/publications/` | `site.data.publications` |
| `selected_publications.yml` | `/publications/` | `site.data.selected_publications` |
| `supervision.yml` | `/people/` | `site.data.supervision` |
| `teaching.yml` | `/teaching/` | `site.data.teaching` |
| `service.yml` | `/service/` | `site.data.service` |
| `awards.yml` | Home | `site.data.awards` |
| `employment.yml` | `/bio/` | `site.data.employment` (filtered: `cv_only != true`) |

`web/_data` is a git symlink to `../data` — Jekyll finds data files normally without any `data_dir` config.

Files used only by the CV (not the website): `personal.yml`, `education.yml`, `funding.yml`, `invited_talks.yml`, `referees.yml`.

## Liquid gotchas

**`cv_only` filter**: Always wrap loops with `{% unless entry.cv_only %}` to hide CV-only entries. The `cv_only` field is either `true` (hide from website) or an object like `{funding: "NWO VIDI"}` (show on website — the object is CV metadata only). Check the filter is present before adding new data entries with `cv_only: true`.

**No HTML in `data/` files.** All fields must be plain text. Icons, badges, and links are handled exclusively in templates.

## Navigation active state

The navbar underlines the active section by comparing `page.url` against each nav link in `_layouts/default.html`. When adding a new top-level section, add both the page file and a nav entry there.
