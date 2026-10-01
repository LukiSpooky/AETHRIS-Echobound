#!/usr/bin/env python3
"""Validiert Kombos und Chor-Akkorde (K33): Typabdeckung, DSL, Fenster, Boni.  Aufruf: gen_combat_data.py validate|stats"""
import csv, pathlib, sys
from collections import Counter
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools/abilities"))
from abl import TYPES, parse


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


def validate():
    errs = []
    cmb, chd = rows("Data/Combat/Combos.csv"), rows("Data/Combat/Chords.csv")
    pairs = Counter((r["First"], r["Second"]) for r in cmb)
    for r in cmb:
        if r["First"] not in TYPES or r["Second"] not in TYPES:
            errs.append(f"{r['Name']}: Typ unbekannt")
        try:
            parse(r["Effects"])
        except ValueError as e:
            errs.append(f"{r['Name']}: {e}")
        if not 1000 <= int(r["BonusPermille"]) <= 1400:
            errs.append(f"{r['Name']}: Bonus außerhalb 1000–1400")
        if pairs[(r["First"], r["Second"])] > 1:
            errs.append(f"{r['Name']}: Paar doppelt")
    cnt = Counter()
    for r in cmb:
        cnt[r["First"]] += 1
        cnt[r["Second"]] += 1
    for t in TYPES:
        if cnt[t] < 4:
            errs.append(f"Kombos: {t} nur {cnt[t]}× beteiligt (≥ 4)")
    c2 = Counter(t for r in chd for t in (r["Type1"], r["Type2"], r["Type3"]))
    for t in TYPES:
        if c2[t] != 3:
            errs.append(f"Akkorde: {t} {c2[t]}× (genau 3)")
    if len({frozenset((r['Type1'], r['Type2'], r['Type3'])) for r in chd}) != len(chd):
        errs.append("Akkorde: doppelte Typkombination")
    return errs, cnt


if __name__ == "__main__":
    errs, cnt = validate()
    for e in errs:
        print("FEHLER:", e)
    if len(sys.argv) > 1 and sys.argv[1] == "stats":
        print(dict(cnt))
    print(f"Kombos/Akkorde: {len(errs)} Verstöße.")
    sys.exit(1 if errs else 0)
