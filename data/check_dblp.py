#!/usr/bin/env python3
"""
Interactive wizard that compares data/publications.yml against the DBLP record
and lets you add missing entries one by one.

Usage:
  python3 data/check_dblp.py
  python3 data/check_dblp.py --local /path/to/dblp.xml
  python3 data/check_dblp.py --year-from 2015
"""

import argparse
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
from pathlib import Path

import yaml

DBLP_URL = "https://dblp.org/pid/64/7497.xml"
PUBLICATIONS_YML = Path(__file__).parent / "publications.yml"
FUZZY_THRESHOLD = 0.80


# ---------------------------------------------------------------------------
# Normalisation & matching
# ---------------------------------------------------------------------------

def normalize(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9 ]", "", title)
    return re.sub(r"\s+", " ", title).strip()


def match_score(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize(a), normalize(b)).ratio()


# ---------------------------------------------------------------------------
# DBLP XML parsing
# ---------------------------------------------------------------------------

ENTRY_TAGS = {"article", "inproceedings", "incollection", "proceedings",
              "book", "phdthesis", "mastersthesis"}


def parse_dblp_xml(source) -> list[dict]:
    """Parse DBLP XML from a file path or URL string."""
    if isinstance(source, str) and source.startswith("http"):
        print(f"Fetching {source} ...")
        with urllib.request.urlopen(source) as resp:
            data = resp.read()
        root = ET.fromstring(data)
    else:
        root = ET.parse(source).getroot()

    entries = []
    for r in root.findall("r"):
        for child in r:
            if child.tag not in ENTRY_TAGS:
                continue
            title_el = child.find("title")
            year_el = child.find("year")
            if title_el is None or year_el is None:
                continue

            title = (title_el.text or "").strip().rstrip(".")
            year = int(year_el.text.strip())

            authors = [a.text.strip() for a in child.findall("author") if a.text]

            venue = ""
            for tag in ("booktitle", "journal", "school"):
                el = child.find(tag)
                if el is not None and el.text:
                    venue = el.text.strip()
                    break

            # Prefer DOI-style ee, fall back to first ee
            doi = ""
            for ee in child.findall("ee"):
                if ee.text:
                    if "doi.org" in ee.text:
                        doi = ee.text.strip()
                        break
                    if not doi:
                        doi = ee.text.strip()

            dblp_key = child.get("key", "")

            entries.append({
                "dblp_key": dblp_key,
                "title": title,
                "year": year,
                "authors": authors,
                "venue": venue,
                "doi": doi,
                "type": child.tag,
            })

    return entries


# ---------------------------------------------------------------------------
# Local YAML parsing
# ---------------------------------------------------------------------------

def load_local(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------

def build_matches(dblp_entries: list[dict], local_entries: list[dict],
                  year_from: int | None):
    matched, fuzzy, missing = [], [], []

    for de in dblp_entries:
        if year_from and de["year"] < year_from:
            continue

        best_score = 0.0
        best_local = None
        for le in local_entries:
            if de["year"] != le.get("year"):
                continue
            s = match_score(de["title"], le.get("title", ""))
            if s > best_score:
                best_score = s
                best_local = le

        if best_score >= 0.95:
            matched.append((de, best_local, best_score))
        elif best_score >= FUZZY_THRESHOLD:
            fuzzy.append((de, best_local, best_score))
        else:
            missing.append(de)

    return matched, fuzzy, missing


# ---------------------------------------------------------------------------
# Wizard helpers
# ---------------------------------------------------------------------------

def hr(char="─", width=56):
    print(char * width)


def prompt(msg: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    try:
        val = input(f"  {msg}{suffix}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)
    return val if val else default


def choose(options: str, default: str) -> str:
    opts = [o.strip() for o in options.split(",")]
    while True:
        val = prompt(f"[{options}]", default).lower()
        if val in opts:
            return val
        print(f"  Please enter one of: {options}")


# ---------------------------------------------------------------------------
# YAML entry builder & writer
# ---------------------------------------------------------------------------

def build_yaml_block(entry: dict, slug: str, label: str) -> str:
    authors_str = ", ".join(entry["authors"])
    lines = [
        f"- id: {slug}",
        f'  year: {entry["year"]}',
        f'  label: "{label}"',
        f'  title: "{entry["title"]}"',
        f'  authors: "{authors_str}"',
        f'  venue: "{entry["venue"]}"',
    ]
    if entry.get("doi"):
        lines.append(f'  link: "{entry["doi"]}"')
    return "\n".join(lines) + "\n"


def prepend_to_yaml(path: Path, block: str):
    existing = path.read_text(encoding="utf-8")
    path.write_text(block + "\n" + existing, encoding="utf-8")


# ---------------------------------------------------------------------------
# Wizard phases
# ---------------------------------------------------------------------------

def review_fuzzy(fuzzy: list[tuple]) -> int:
    edited = 0
    for de, le, score in fuzzy:
        hr()
        print(f"  FUZZY MATCH  (score {score:.2f})")
        print(f'  DBLP:  "{de["title"]}" ({de["year"]})')
        print(f'  Local: "{le.get("title")}" (id: {le.get("id")})')
        print()
        print("  [s] skip — treat as same, no action")
        print("  [e] open $EDITOR on publications.yml")
        c = choose("s,e", "s")
        if c == "e":
            editor = os.environ.get("EDITOR", "vi")
            os.system(f'{editor} "{PUBLICATIONS_YML}"')
            edited += 1
    return edited


def review_missing(missing: list[dict]) -> int:
    added = 0
    total = len(missing)
    for i, de in enumerate(missing, 1):
        hr()
        print(f"  MISSING {i}/{total}")
        print(f'  Title:   {de["title"]}')
        print(f'  Year:    {de["year"]}')
        print(f'  Venue:   {de["venue"] or "(unknown)"}')
        print(f'  Authors: {", ".join(de["authors"][:3])}{"..." if len(de["authors"]) > 3 else ""}')
        if de["doi"]:
            print(f'  DOI:     {de["doi"]}')
        print()
        print("  [a] add to publications.yml")
        print("  [s] skip (intentionally omit)")
        print("  [q] quit and save progress")
        c = choose("a,s,q", "s")
        if c == "q":
            break
        if c == "s":
            continue
        # [a] — collect slug and label
        slug_hint = re.sub(r"[^a-z0-9]+", "-",
                           de["title"].lower().split(":")[0])[:30].strip("-")
        year_short = str(de["year"])[2:]
        venue_short = re.sub(r"[^a-z]", "", de["venue"].lower().split()[0])[:6]
        slug_default = f"{slug_hint}-{venue_short}{year_short}"
        label_default = f"{de['venue'].split()[0]}'{year_short}" if de["venue"] else ""

        slug = prompt("id (slug)", slug_default)
        label = prompt("label (short venue)", label_default)

        block = build_yaml_block(de, slug, label)
        prepend_to_yaml(PUBLICATIONS_YML, block)
        print(f"  ✅ Added '{slug}' to publications.yml")
        added += 1

    return added


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Compare publications.yml with DBLP")
    parser.add_argument("--local", metavar="FILE",
                        help="Use a local DBLP XML file instead of fetching")
    parser.add_argument("--year-from", type=int, metavar="YEAR",
                        help="Only check DBLP entries from this year onwards")
    args = parser.parse_args()

    source = args.local or DBLP_URL
    dblp = parse_dblp_xml(source)
    local = load_local(PUBLICATIONS_YML)

    print(f"Parsed {len(dblp)} DBLP entries, {len(local)} local entries.")
    if args.year_from:
        print(f"Filtering to year >= {args.year_from}")
    print()

    matched, fuzzy, missing = build_matches(dblp, local, args.year_from)

    print(f"  ✅ Matched: {len(matched)}")
    print(f"  ⚠️  Fuzzy:   {len(fuzzy)}  (title differs slightly — needs review)")
    print(f"  ❌ Missing: {len(missing)}  (in DBLP, not in local)")
    print()

    if not fuzzy and not missing:
        print("Nothing to review. Local list is up to date.")
        return

    to_review = len(fuzzy) + len(missing)
    print(f"Will walk you through {to_review} entr{'y' if to_review == 1 else 'ies'}.")
    print("Press Enter to continue, Ctrl-C to abort.")
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    edited = review_fuzzy(fuzzy) if fuzzy else 0
    added = review_missing(missing) if missing else 0

    hr("═")
    if added or edited:
        print(f"  Added {added} entr{'y' if added == 1 else 'ies'} to publications.yml.")
        if edited:
            print(f"  Opened editor for {edited} fuzzy match(es).")
        print("  Run `make cv` to rebuild the CV.")
    else:
        print("  No changes made.")


if __name__ == "__main__":
    main()
