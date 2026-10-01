#!/usr/bin/env python3
"""Baut ein Kapitel aus einer Vorlage mit Daten-Platzhaltern (ADR-075-Prinzip für Systemkapitel).

Platzhalter:  {{abilities KIND [TYPE]}}  {{csv PATH [COLS]}}  {{count PATH}}
Aufruf: build_doc.py templates/K28.md ../../docs/kapitel/K28_….md
"""
import csv, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import gen_abilities as ga
import gen_learnsets as gl
sys.path.insert(0, str(ROOT / "tools/ref"))
import aethris_combat as ac
import gen_combat_data as gcd
import aethris_ai as aai
import aethris_bond as abd
import aethris_bond_progress as abp
import aethris_genetics as agen


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
    if parts[0] == "file":
        return {"combat_report_speed": ac.report_speed, "combat_report_levels": ac.report_levels, "combat_sample_log": ac.sample_log, "combat_matrix": ac.report_matrix, "combat_examples": ac.example_table, "combat_power": ac.power_table, "combo_matrix": gcd.combo_matrix, "chord_examples": gcd.chord_examples, "ai_matrix": lambda: aai.matrix(150), "ai_explain": aai.explain, "ai_kits": aai.kit_table, "boss_table": ac.boss_table, "bond_scenarios": abd.scenarios, "bond_sheet": abd.bond_sheet, "bond_progress": abp.table, "genetics_dr18": agen.dr18_table, "genetics_groups": agen.group_table, "genetics_eggs": agen.egg_table}[parts[1]]()
    if parts[0] == "py":   # py MODUL FUNKTION [ARGS]
        import importlib
        return str(getattr(importlib.import_module(parts[1]), parts[2])(*parts[3:]))
    if parts[0] == "overview_k30":
        return gl.overview_k30()
    if parts[0] == "learnset":
        return gl.show(" ".join(parts[1:]))
    if parts[0] == "csvf":   # gefiltert: csvf PATH COLS FILTERCOL=WERT
        col, val = parts[3].split("=")
        rows = [r for r in csv.DictReader(l for l in open(ROOT / parts[1], encoding="utf-8") if not l.startswith("#")) if r[col] == val]
        cols = parts[2].split(",")
        return "\n".join(["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)] + ["| " + " | ".join(r[c] for c in cols) + " |" for r in rows])
    if parts[0] == "count":
        return str(sum(1 for l in open(ROOT / parts[1], encoding="utf-8") if not l.startswith("#")) - 1)
    raise ValueError(parts)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    text = re.sub(r"\{\{([^}]+)\}\}", repl, pathlib.Path(src).read_text(encoding="utf-8"))
    pathlib.Path(dst).write_text(text, encoding="utf-8")
    print(pathlib.Path(dst).name, len(text.split()), "Wörter")
