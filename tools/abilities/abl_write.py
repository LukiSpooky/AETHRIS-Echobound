#!/usr/bin/env python3
"""Schreibt Fähigkeiten einer Art (Active/Passive/Crescendo/Field) idempotent in Data/Abilities/Abilities.csv."""
import csv
from abl import ABIL, KINDS, parse, budget, describe, describe_passive, load

FIELDS = ["Name", "Kind", "Type", "DisplayName", "Category", "Power", "Accuracy", "Target", "TimeCost", "Budget",
          "Effects", "Trigger", "Tags", "Description"]
ORDER = {"Active": 0, "Passive": 1, "Crescendo": 2, "Field": 3}


def write_kind(kind, rows):
    out = []
    for i, r in enumerate(rows, 1):
        r = {k: r.get(k, "") for k in FIELDS} | r
        r["Name"] = f"ABL_{KINDS[kind]}{i:03d}"
        r["Kind"] = kind
        eff = parse(r["Effects"])
        if kind in ("Active", "Crescendo"):
            v, cost = budget(int(r["Power"] or 0), int(r["Accuracy"] or 0), r["Target"], r["Category"], eff)
            r["Budget"], r["TimeCost"] = v, cost
        else:
            r["Budget"], r["TimeCost"] = "", ""
        if not r.get("Description"):
            r["Description"] = describe_passive(r) if kind == "Passive" else describe(r)
        elif kind == "Passive" and describe_passive(r):
            r["Description"] = describe_passive(r)[:-1] + ". " + r["Description"]
        out.append({k: r.get(k, "") for k in FIELDS})
    old = [x for x in load() if x["Kind"] != kind]
    allr = sorted(old + out, key=lambda x: (ORDER[x["Kind"]], int(x["Name"][5:])))
    with open(ABIL, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(allr)
    print(f"{len(out)} Fähigkeiten ({kind}) geschrieben; gesamt {len(allr)}")
