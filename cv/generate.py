#!/usr/bin/env python3
"""CV Generator — reads data/*.yml and renders Jinja2 templates into output/*.tex"""

import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

DATA_DIR = Path(__file__).parent.parent / "data"
TEMPLATES_DIR = Path(__file__).parent / "templates"
OUTPUT_DIR = Path(__file__).parent / "output"

MONTHS_SHORT = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June',
                'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
MONTHS_FULL  = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']


def escape_latex(text):
    if not text:
        return ''
    s = str(text)
    s = s.replace('\\', r'\textbackslash{}')
    s = s.replace('&',  r'\&')
    s = s.replace('%',  r'\%')
    s = s.replace('#',  r'\#')
    s = s.replace('_',  r'\_')
    s = s.replace('{',  r'\{')
    s = s.replace('}',  r'\}')
    s = s.replace('~',  r'\textasciitilde{}')
    return s


def format_date(date_str):
    if not date_str:
        return ''
    m = re.match(r'^(\d{4})-(\d{2})$', str(date_str))
    if not m:
        return str(date_str)
    return f"{MONTHS_SHORT[int(m.group(2)) - 1]} {m.group(1)}"


def format_year_range(start, end=None):
    if not start:
        return ''
    return f"{start}--present" if not end else f"{start}--{end}"


def split_name(full_name):
    parts = str(full_name).strip().split()
    if len(parts) == 1:
        return {'first': parts[0], 'last': ''}
    return {'first': ' '.join(parts[:-1]), 'last': parts[-1]}


def format_birth_date(iso_date):
    if not iso_date:
        return ''
    parts = str(iso_date).split('-')
    return f"{int(parts[2])} {MONTHS_FULL[int(parts[1]) - 1]} {parts[0]}"


def get_bib_entry_type(pub):
    label = (pub.get('label') or '').lower()
    if 'journal' in label or 'vldbj' in label:
        return 'article'
    if 'book' in label:
        return 'book'
    return 'inproceedings'


def format_bib_authors(authors):
    if not authors:
        return ''
    s = re.sub(r',\s*', ' and ', authors)
    s = s.replace('Asterios Katsifodimos', r'{\bfseries Asterios Katsifodimos}')
    s = s.replace('A. Katsifodimos', r'{\bfseries A. Katsifodimos}')
    return s


def regex_search(value, pattern):
    m = re.search(pattern, str(value) if value else '')
    return m.group(1) if m else ''


def load_yaml(name):
    path = DATA_DIR / name
    if not path.exists():
        print(f"  warning: {name} not found", file=sys.stderr)
        return []
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def build_env():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        # Use (( )) / (% %) to avoid conflicts with LaTeX { } braces
        variable_start_string='((',
        variable_end_string='))',
        block_start_string='(%',
        block_end_string='%)',
        comment_start_string='(#',
        comment_end_string='#)',
    )
    for fn in [escape_latex, format_date, format_year_range, split_name,
               format_birth_date, get_bib_entry_type, format_bib_authors, regex_search]:
        env.filters[fn.__name__] = fn
        env.globals[fn.__name__] = fn
    env.tests['contains'] = lambda value, substring: substring in str(value)
    return env


TEMPLATES = [
    ('main.tex.j2',                  'asterios.katsifodimos.tex'),
    ('education.tex.j2',             'education.tex'),
    ('employment.tex.j2',            'employment.tex'),
    ('awards.tex.j2',                'awards.tex'),
    ('funding.tex.j2',               'funding.tex'),
    ('service.tex.j2',               'service.tex'),
    ('teaching.tex.j2',              'teaching.tex'),
    ('supervision.tex.j2',           'supervision.tex'),
    ('invited_talks.tex.j2',         'invited-talks.tex'),
    ('referees.tex.j2',              'referees.tex'),
    ('selected_publications.tex.j2', 'selected-publications.tex'),
    ('publications.tex.j2',          'publications.tex'),
    ('references.j2',                'references.bib'),
]


def generate():
    OUTPUT_DIR.mkdir(exist_ok=True)
    env = build_env()

    data = {
        'personal':              load_yaml('personal.yml'),
        'education':             load_yaml('education.yml'),
        'employment':            load_yaml('employment.yml'),
        'awards':                load_yaml('awards.yml'),
        'funding':               load_yaml('funding.yml'),
        'service':               load_yaml('service.yml'),
        'teaching':              load_yaml('teaching.yml'),
        'supervision':           load_yaml('supervision.yml'),
        'invited_talks':         load_yaml('invited_talks.yml'),
        'referees':              load_yaml('referees.yml'),
        'publications':          load_yaml('publications.yml'),
        'selected_publications': load_yaml('selected_publications.yml'),
    }

    # Lookup dict used by selected_publications template
    data['pub_by_id'] = {p['id']: p for p in (data['publications'] or [])}

    for tpl_name, out_name in TEMPLATES:
        rendered = env.get_template(tpl_name).render(**data)
        (OUTPUT_DIR / out_name).write_text(rendered, encoding='utf-8')
        print(f"  wrote {out_name}")

    print("done.")


if __name__ == '__main__':
    generate()
