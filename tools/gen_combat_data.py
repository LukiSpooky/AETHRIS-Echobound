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


TYPE_DE = {"Ember": "Glut", "Tide": "Flut", "Stone": "Stein", "Storm": "Sturm", "Bloom": "Blüte", "Frost": "Frost",
           "Void": "Leere", "Light": "Licht", "Venom": "Gift", "Metal": "Metall", "Spirit": "Geist", "Crystal": "Kristall",
           "Sound": "Klang", "Gravity": "Schwerkraft", "Arcane": "Arkan"}


def combo_matrix():
    cmb = {(r["First"], r["Second"]): r["DisplayName"] for r in rows("Data/Combat/Combos.csv")}
    ab = [t[:3] for t in TYPES]
    out = ["| zuerst ↓ / dann → | " + " | ".join(TYPE_DE[t][:4] for t in TYPES) + " |", "|---|" + "---|" * len(TYPES)]
    for a in TYPES:
        out.append(f"| **{TYPE_DE[a]}** | " + " | ".join(cmb.get((a, b), "·") for b in TYPES) + " |")
    return "\n".join(out)


def chord_examples():
    import hashlib
    sp = list(csv.DictReader(open(ROOT / "Data/Echos/Species.csv", encoding="utf-8")))
    sp = [s for s in sp if s["LineKind"] not in ("Legendary", "Mythical") and int(s["Stage"]) == 1]
    out = ["| Akkord | Beispiel-Chor (je Typ zwei Arten der Stufe 1, frühe Regionen bevorzugt) |", "|---|---|"]
    for r in rows("Data/Combat/Chords.csv"):
        names = []
        for t in (r["Type1"], r["Type2"], r["Type3"]):
            c = [s for s in sp if t in (s["PrimaryType"].split(".")[1], (s["SecondaryType"] or ".").split(".")[1])]
            c.sort(key=lambda s: (s["Region"] not in ("R01", "R02", "R03", "R06"), hashlib.sha1((r["Name"] + s["Name"]).encode()).hexdigest()))
            names.append(f"{TYPE_DE[t]}: " + ", ".join(f"{s['DisplayName']} ({s['Region']})" for s in c[:2]))
        out.append(f"| {r['DisplayName']} | " + " · ".join(names) + " |")
    return "\n".join(out)
