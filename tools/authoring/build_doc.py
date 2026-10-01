#!/usr/bin/env python3
"""Baut ein Kapitel aus einer Vorlage mit Daten-Platzhaltern (ADR-075-Prinzip für Systemkapitel).

Platzhalter:  {{abilities KIND [TYPE]}}  {{csv PATH [COLS]}}  {{count PATH}}
Aufruf: build_doc.py templates/K28.md ../../docs/kapitel/K28_….md
"""
import csv, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import gen_abilities as ga


def table_csv(path, cols=None):
    rows = list(csv.DictReader(l for l in open(ROOT / path, encoding="utf-8") if not l.startswith("#")))
    cols = cols.split(",") if cols else list(rows[0].keys())
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(r[c] for c in cols) + " |" for r in rows]
    return "\n".join(out)


def repl(m):
    parts = m.group(1).split()
    if parts[0] == "abilities":
        return ga.render(parts[1], parts[2] if len(parts) > 2 else None)
    if parts[0] == "csv":
        return table_csv(parts[1], parts[2] if len(parts) > 2 else None)
    if parts[0] == "count":
        return str(sum(1 for l in open(ROOT / parts[1], encoding="utf-8") if not l.startswith("#")) - 1)
    raise ValueError(parts)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    text = re.sub(r"\{\{([^}]+)\}\}", repl, pathlib.Path(src).read_text(encoding="utf-8"))
    pathlib.Path(dst).write_text(text, encoding="utf-8")
    print(pathlib.Path(dst).name, len(text.split()), "Wörter")
