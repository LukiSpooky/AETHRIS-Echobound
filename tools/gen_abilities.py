#!/usr/bin/env python3
"""Validiert und rendert Data/Abilities/Abilities.csv (K28–K30).

Aufruf:
  gen_abilities.py validate            -> Regeln AB-01 … AB-14 prüfen (Exit 1 bei Verstößen)
  gen_abilities.py render KIND [TYPE]  -> Markdown-Tabellen für Kapitel
  gen_abilities.py stats               -> Kennzahlen
"""
import csv, pathlib, sys
from collections import Counter, defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "abilities"))
from abl import (ABIL, STATUS, TYPES, TYPE_DE, TARGETS, CATEGORIES, IDENTITY, STATUS_VALUE, parse, marks, budget,
                 load)

TARGET_COUNT = {"Active": 180, "Passive": 90, "Crescendo": 30, "Field": 30}
PER_TYPE = {"Active": 12, "Passive": 6, "Crescendo": 2, "Field": 2}


def validate(final=False):
    rows = load()
    errs = []
    names = Counter(r["DisplayName"] for r in rows)
    species = {r["DisplayName"] for r in csv.DictReader(open(ABIL.parents[1] / "Echos/Species.csv", encoding="utf-8"))}
    status = {r["Name"] for r in csv.DictReader(l for l in open(STATUS, encoding="utf-8") if not l.startswith("#"))}
    by = defaultdict(lambda: defaultdict(list))
    for r in rows:
        sid = r["Name"]
        e = lambda m: errs.append(f"{sid} {r['DisplayName']}: {m}")
        if names[r["DisplayName"]] > 1:
            e("AB-01 Name doppelt")
        if r["DisplayName"] in species:
            e("AB-01 Name kollidiert mit Echo-Art")
        if r["Type"] not in TYPES:
            e("AB-02 Typ unbekannt (keine typlosen Fähigkeiten, CANON §77)")
        by[r["Kind"]][r["Type"]].append(r)
        try:
            eff = parse(r["Effects"])
        except ValueError as ex:
            e(f"AB-03 {ex}")
            continue
        for n, a in eff:
            if n == "Status" and a[0] not in status:
                e(f"AB-03 Status {a[0]} unbekannt")
        if r["Kind"] in ("Active", "Crescendo"):
            p, acc = int(r["Power"] or 0), int(r["Accuracy"] or 0)
            if r["Category"] not in CATEGORIES:
                e("AB-04 Kategorie unbekannt")
            if r["Category"] == "Status" and p:
                e("AB-04 Status-Fähigkeit mit Stärke")
            if r["Category"] != "Status" and not p:
                e("AB-04 Schadensfähigkeit ohne Stärke")
            if p > (200 if r["Kind"] == "Crescendo" else 150):
                e("AB-05 Stärke über Deckel")
            if acc and not 500 <= acc <= 1000:
                e("AB-05 Genauigkeit außerhalb 500–1000")
            if r["Target"] not in TARGETS:
                e("AB-06 Ziel unbekannt")
            v, cost = budget(p, acc, r["Target"], r["Category"], eff)
            if str(v) != r["Budget"] or str(cost) != r["TimeCost"]:
                e(f"AB-07 Budget/Zeitkosten veraltet ({v}/{cost})")
            if r["Kind"] == "Active" and not 50 <= cost <= 200:
                e("AB-07 Zeitkosten außerhalb 50–200")
            if r["Kind"] == "Crescendo" and not 200 <= v <= 320:
                e(f"AB-08 Crescendo-Budget {v} außerhalb 200–320")
        if r["Kind"] == "Passive" and not r["Trigger"]:
            e("AB-09 Passive ohne Auslöser")
        if r["Kind"] == "Field" and "Field." not in r["Tags"]:
            e("AB-10 Feldfähigkeit ohne Field.-Tag")
    for kind, per in PER_TYPE.items():
        if kind not in by:
            continue
        for t in TYPES:
            lst = by[kind][t]
            if len(lst) != per:
                errs.append(f"{kind} {t}: {len(lst)} statt {per} (AB-11)")
        if kind == "Active":
            for t in TYPES:
                lst = by[kind][t]
                idn = sum(1 for r in lst if marks(parse(r["Effects"])) & IDENTITY[t])
                if idn < 3:
                    errs.append(f"{t}: nur {idn} Fähigkeiten mit Typ-Identität (AB-12, CANON §78)")
                cats = Counter(r["Category"] for r in lst)
                if cats["Physical"] < 2 or cats["Special"] < 2 or cats["Status"] < 3:
                    errs.append(f"{t}: Kategorienmix {dict(cats)} (AB-13: ≥2 P, ≥2 S, ≥3 Status)")
    if final:
        cnt = Counter(r["Kind"] for r in rows)
        for k, n in TARGET_COUNT.items():
            if cnt[k] != n:
                errs.append(f"AB-14 {k}: {cnt[k]} statt {n}")
    return errs


def render(kind, typ=None):
    rows = [r for r in load() if r["Kind"] == kind and (typ is None or r["Type"] == typ)]
    if kind in ("Active", "Crescendo"):
        out = ["| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |", "|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            acc = "–" if r["Accuracy"] in ("", "0") else f"{int(r['Accuracy']) // 10} %"
            pw = r["Power"] if r["Power"] not in ("", "0") else "–"
            out.append(f"| {r['Name']} | **{r['DisplayName']}** | {CATEGORIES[r['Category']][:4]}. | {pw} | {acc} | "
                       f"{r['Target']} | {r['TimeCost']} | {r['Budget']} | {r['Description']} |")
    else:
        out = ["| ID | Name | Auslöser | Wirkung | Tags |", "|---|---|---|---|---|"]
        for r in rows:
            out.append(f"| {r['Name']} | **{r['DisplayName']}** | {r['Trigger'] or '–'} | {r['Description']} | {r['Tags']} |")
    return "\n".join(out)


def stats():
    rows = load()
    print("Arten:", dict(Counter(r["Kind"] for r in rows)))
    act = [r for r in rows if r["Kind"] == "Active"]
    print("Kategorien:", dict(Counter(r["Category"] for r in act)))
    print("Ziele:", dict(Counter(r["Target"] for r in act)))
    print("Zeitkosten:", sorted(Counter(int(r["TimeCost"]) for r in act).items()))
    dmg = [r for r in act if r["Power"] not in ("", "0")]
    print("Schadens-Fähigkeiten:", len(dmg), "Ø Stärke", sum(int(r["Power"]) for r in dmg) // max(1, len(dmg)))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "validate":
        errs = validate(final="--final" in sys.argv)
        for e in errs:
            print("FEHLER:", e)
        print(f"Fähigkeiten: {len(load())}, {len(errs)} Verstöße.")
        sys.exit(1 if errs else 0)
    elif cmd == "render":
        print(render(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None))
    elif cmd == "stats":
        stats()
