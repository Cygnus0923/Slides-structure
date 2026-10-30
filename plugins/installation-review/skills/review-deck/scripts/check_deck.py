#!/usr/bin/env python3
"""Check a review deck.md against its fixed template.

Usage:
    python check_deck.py <deck.md> --template <template.yaml>

Exit code 0 when the deck passes, 1 when it has errors, 2 on bad input.
Checks structure only (order, ids, required lines, source tags, limits).
Whether each source actually supports its claim is the deck-validator
agent's job, not this script's.
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

SLIDE_RE = re.compile(r"^## \[(S\d+)\] (.+?)\s*$")
FIELD_RE = re.compile(r"^\*\*(Headline|Layout|Status):\*\*\s*(.*)$")
NOTES_RE = re.compile(r"^\*\*Notes:\*\*")
SRC_RE = re.compile(r"\[src: [^\]]+\]")
TABLE_SEP_RE = re.compile(r"^\|\s*:?-{3,}")
STATUSES = {"filled", "partial", "tbd"}


def load_template(path):
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    default_max = data.get("defaults", {}).get("max_bullets", 5)
    slides = []
    for s in data["slides"]:
        slides.append({
            "id": s["id"],
            "name": s["name"],
            "optional": bool(s.get("optional", False)),
            "max": s.get("max_bullets", default_max),
        })
    return slides


def parse_deck(path):
    """Return a list of slides with their header line and body lines."""
    slides, current = [], None
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        m = SLIDE_RE.match(line)
        if m:
            current = {"id": m.group(1), "name": m.group(2), "line": n, "body": []}
            slides.append(current)
        elif current is not None:
            current["body"].append((n, line))
    return slides


def check_slide(slide, spec, errors):
    sid = slide["id"]
    fields, content, in_notes, in_table = {}, [], False, False
    for n, line in slide["body"]:
        if NOTES_RE.match(line):
            in_notes = True
            continue
        if in_notes:
            continue
        f = FIELD_RE.match(line)
        if f:
            fields[f.group(1)] = (n, f.group(2).strip())
            continue
        stripped = line.strip()
        if stripped.startswith("|"):
            if not in_table:          # header row
                in_table = True
                continue
            if TABLE_SEP_RE.match(stripped):
                continue
            content.append((n, stripped, "row"))
        else:
            in_table = False
            if stripped.startswith("- "):
                content.append((n, stripped, "bullet"))

    for key in ("Headline", "Layout", "Status"):
        if key not in fields or not fields[key][1]:
            errors.append(f"{sid} (line {slide['line']}): missing **{key}:**")

    status = fields.get("Status", (0, ""))[1].lower()
    if status and status not in STATUSES:
        errors.append(f"{sid} line {fields['Status'][0]}: status '{status}' not one of {sorted(STATUSES)}")

    for n, text, kind in content:
        body = text[2:].strip() if kind == "bullet" else text
        is_tbd = body == "TBD" or re.fullmatch(r"\|?(\s*TBD\s*\|)+\s*", body) is not None
        if not is_tbd and not SRC_RE.search(text):
            errors.append(f"{sid} line {n}: {kind} has no [src: ...] tag")

    if status == "tbd" and not any("TBD" in t for _, t, _ in content):
        errors.append(f"{sid}: status is tbd but no TBD line found")

    if len(content) > spec["max"]:
        errors.append(f"{sid}: {len(content)} bullets/rows, limit is {spec['max']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("deck")
    ap.add_argument("--template", required=True)
    args = ap.parse_args()

    for p in (args.deck, args.template):
        if not Path(p).is_file():
            print(f"Not found: {p}", file=sys.stderr)
            return 2

    template = load_template(args.template)
    deck = parse_deck(args.deck)
    errors = []

    spec_by_id = {s["id"]: s for s in template}
    deck_ids = [s["id"] for s in deck]

    for s in deck:
        if s["id"] not in spec_by_id:
            errors.append(f"{s['id']} (line {s['line']}): not in template — slides can't be added")
        elif s["name"] != spec_by_id[s["id"]]["name"]:
            errors.append(f"{s['id']} (line {s['line']}): name '{s['name']}' should be '{spec_by_id[s['id']]['name']}'")

    if len(deck_ids) != len(set(deck_ids)):
        errors.append("Duplicate slide ids: " + ", ".join(sorted({i for i in deck_ids if deck_ids.count(i) > 1})))

    for spec in template:
        if spec["id"] not in deck_ids and not spec["optional"]:
            errors.append(f"{spec['id']} {spec['name']}: required slide missing")

    expected_order = [s["id"] for s in template if s["id"] in deck_ids]
    actual_order = [i for i in dict.fromkeys(deck_ids) if i in spec_by_id]
    if actual_order != expected_order:
        errors.append(f"Slide order {actual_order} should be {expected_order}")

    for s in deck:
        if s["id"] in spec_by_id:
            check_slide(s, spec_by_id[s["id"]], errors)

    if errors:
        print(f"FAIL — {len(errors)} problem(s) in {args.deck}")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"PASS — {len(deck)} slides match template")
    return 0


if __name__ == "__main__":
    sys.exit(main())
