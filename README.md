# asterios.katsifodimos.com

Personal academic website for [Asterios Katsifodimos](http://asterios.katsifodimos.com), Assistant Professor at TU Delft.

Built with [Jekyll](https://jekyllrb.com/) and hosted via GitHub Pages.

## Tech stack

- **Jekyll** — static site generator (via `github-pages` gem)
- **Bootstrap 5.3.3** — layout and responsive grid (CDN)
- **Font Awesome 6.7.2** — icons (CDN)
- **Montserrat / Roboto** — fonts (Google Fonts CDN)
- **`css/theme.css`** — all custom styles (single file, no preprocessor)
- **`css/syntax.css`** — code block syntax highlighting (Rouge)

## Project structure

```
_layouts/
  default.html        # single shared layout (navbar, footer)
_config.yml           # site name, URL, markdown/highlighter settings
index.md              # home page (hero, awards, people)
publications/         # research & publications page
teaching/             # courses and thesis supervision
service/              # community service
css/
  theme.css           # custom styles
  syntax.css          # syntax highlighting
assets/               # images (profile photo, people portraits)
Gemfile               # Ruby dependencies
```

## Local development

### Prerequisites

Ruby and Bundler must be installed. On macOS:

```bash
brew install ruby
gem install bundler
```

### Setup

```bash
bundle install
```

### Serve locally

```bash
bundle exec jekyll serve
```

The site is available at `http://localhost:4000`. Jekyll watches for file changes and rebuilds automatically.

### Build (static output)

```bash
bundle exec jekyll build
```

Output is written to `_site/`.

## Deployment

The site is deployed automatically by GitHub Pages on every push to the `master` branch. No manual build step is needed — GitHub Pages runs Jekyll server-side.

## Editing content

| Page | File |
|------|------|
| Home (bio, awards, people) | `index.md` |
| Publications | `publications/index.md` |
| Teaching | `teaching/index.html` |
| Service | `service/index.md` |
| Navbar / footer | `_layouts/default.html` |
| Styles | `css/theme.css` |
| Site config (URL, name) | `_config.yml` |
