# CV Generator

This directory contains the CV generation system that creates LaTeX CV files from the `_data/*.yml` source files.

## Current Status

### ✅ Completed

1. **Schema Design**: [`CV_SCHEMA.md`](./CV_SCHEMA.md) - Complete YAML schema documentation
2. **Data Files Created**:
   - `_data/personal.yml` - Contact info, social links
   - `_data/education.yml` - PhD, MSc, BSc
   - `_data/employment.yml` - Work history (merged from timeline.yml)
   - `_data/invited_talks.yml` - Invited talks and keynotes
   - `_data/referees.yml` - Reference list
3. **Data Files Updated**:
   - `_data/awards.yml` - Added `year`, `type`, `cv_only` fields
   - `_data/service.yml` - Added `cv_only` flags, `special_service` section

### 🔄 In Progress

4. **Node.js Generator**: Not yet implemented
5. **LaTeX Templates**: Not yet created
6. **Build System**: Makefile integration

### 📋 Remaining Data Migration

These sections still need to be migrated from hand-written `.tex` files:

- `research-statement.tex` - Research statement
- `education-statement.tex` - Education statement  
- `leadership-valorization-organization.tex` - Leadership statement
- Teaching contribution percentages (from `teaching-supervision.tex`)
- Supervision funding details (from `teaching-supervision.tex`)

## Next Steps

1. **Build the generator skeleton** - Create `generate.js` that:
   - Reads all `_data/*.yml` files
   - Filters by `cv_only` flag
   - Outputs LaTeX code

2. **Create LaTeX templates** - Template files for each section:
   - `templates/education.tex.ejs`
   - `templates/employment.tex.ejs`
   - etc.

3. **Test generation** - Run generator and compare output with existing CV

4. **Iterate and refine** - Adjust templates until output matches desired format

5. **Set up build system** - Add Makefile targets

## File Structure (Planned)

```
cv/
├── README.md              # This file
├── CV_SCHEMA.md           # Schema documentation
├── generate.js            # Main generator script
├── package.json           # Node.js dependencies
├── templates/             # EJS LaTeX templates
│   ├── main.tex.ejs
│   ├── education.tex.ejs
│   ├── employment.tex.ejs
│   ├── awards.tex.ejs
│   ├── service.tex.ejs
│   ├── teaching.tex.ejs
│   ├── supervision.tex.ejs
│   ├── invited_talks.tex.ejs
│   ├── referees.tex.ejs
│   └── references.bib.ejs
└── output/                # Generated files (gitignored)
    ├── asterios.katsifodimos.tex
    ├── education.tex
    ├── employment.tex
    ├── awards.tex
    ├── service.tex
    ├── teaching.tex
    ├── supervision.tex
    ├── invited_talks.tex
    ├── referees.tex
    └── references.bib
```

## Usage

Once complete:

```bash
# Generate CV LaTeX files
npm run generate

# Compile to PDF
cd output && make pdf

# Or one command (once Makefile is set up)
make cv
```

## Design Decisions

1. **Single Source**: All data in `../data/*.yml`
2. **CV-Only Flag**: `cv_only: true` hides from website, shows in CV
3. **EJS Templates**: Use EJS for easy JavaScript templating in LaTeX
4. **Preserve Hand-Written**: Research/education/leadership statements can be included via `\input{}`
