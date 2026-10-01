#!/usr/bin/env python3
"""Nebenquest-Gerüst (K48 §4): verteilt SQ_001–SQ_210 deterministisch auf Regionen, Kategorien, Fraktionen,
Verfügbarkeit und Fraktionsketten. Schreibt Data/Quests/SideQuests.csv (Titel/Inhalt folgen in K49–K51).
Aufruf: sq_plan.py write | tables"""
import csv, pathlib, sys
from collections import Counter, defaultdict
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "Data/Quests/SideQuests.csv"

REGION_ORDER = ["R01", "R02", "R03", "R06", "R04", "R05", "R07", "R08", "R09", "R10"]
REGION_ACT = {"R01": "Akt I", "R02": "Akt I", "R03": "Akt I", "R06": "Akt I", "R04": "Akt II", "R05": "Akt II",
              "R07": "Akt II", "R08": "Akt II", "R09": "Akt III", "R10": "Akt III"}
LATER = {"Akt I": ["Akt II", "Akt III", "Nachhall"], "Akt II": ["Akt III", "Nachhall"], "Akt III": ["Nachhall"]}
# Fraktionsanteile je Region (Gewichte; F05 nur ab Akt III, ADR-180)
FACTION_W = {
    "R01": {"F03": 6, "F01": 3, "F02": 3, "F04": 1},
    "R02": {"F03": 5, "F02": 4, "F01": 2, "F04": 1},
    "R03": {"F04": 6, "F01": 2, "F03": 2, "F05": 2},
    "R06": {"F02": 6, "F04": 3, "F03": 2, "F01": 1},
    "R04": {"F04": 4, "F01": 4, "F02": 3, "F03": 1},
    "R05": {"F02": 5, "F04": 5, "F03": 2},
    "R07": {"F05": 5, "F03": 4, "F01": 1, "F04": 1},
    "R08": {"F01": 6, "F05": 3, "F04": 2, "F03": 1},
    "R09": {"F01": 4, "F02": 4, "F03": 2, "F05": 1},
    "R10": {"F03": 4, "F01": 3, "F02": 2, "F04": 2, "F05": 1},
}
FACTION_TARGET = {"F01": 27, "F02": 27, "F03": 28, "F04": 26, "F05": 12}
CATS = ["ECHO", "PEOPLE", "RESEARCH", "MYSTERY", "TRIAL", "EVENT"]   # Nicht-Fraktions-Kategorien
CAT_NAME = {"FACTION": "Fraktion", "ECHO": "Echo-Geschichte", "PEOPLE": "Menschen", "RESEARCH": "Forschung",
            "MYSTERY": "Rätsel & Ruinen", "TRIAL": "Wärterprüfung", "EVENT": "Weltereignis"}
OVERRIDES = {"SQ_202": {"Available": "Akt III"}, "SQ_204": {"Available": "Nachhall"}}
CHAPTER = lambda n: "K49" if n <= 70 else ("K50" if n <= 140 else "K51")


def budget():
    rows = list(csv.DictReader(open(ROOT / "Data/World/RegionBudget.csv", encoding="utf-8")))
    return {r["RegionId"]: int(r["SideQuests"]) for r in rows}


def largest_remainder(total, weights):
    s = sum(weights.values())
    raw = {k: total * w / s for k, w in weights.items()}
    base = {k: int(v) for k, v in raw.items()}
    rest = total - sum(base.values())
    for k in sorted(raw, key=lambda k: (-(raw[k] - base[k]), k))[:rest]:
        base[k] += 1
    return base


def plan():
    b = budget()
    fac_total = sum(FACTION_TARGET.values())                     # 120
    fac_per_region = largest_remainder(fac_total, {r: b[r] for r in REGION_ORDER})
    # Fraktionen je Region nach Gewichten, dann global auf FACTION_TARGET korrigieren
    alloc = {r: largest_remainder(fac_per_region[r], FACTION_W[r]) for r in REGION_ORDER}
    tot = Counter()
    for r in alloc:
        tot.update(alloc[r])
    for _ in range(200):
        over = [f for f in FACTION_TARGET if tot[f] > FACTION_TARGET[f]]
        under = [f for f in FACTION_TARGET if tot[f] < FACTION_TARGET[f]]
        if not over:
            break
        f_o, f_u = over[0], under[0]
        # Region, in der f_o vorkommt und f_u erlaubt ist, mit größtem f_o-Anteil
        cand = [r for r in REGION_ORDER if alloc[r].get(f_o, 0) > 1 and f_u in FACTION_W[r]]
        r = max(cand, key=lambda r: (alloc[r][f_o], -REGION_ORDER.index(r)))
        alloc[r][f_o] -= 1; alloc[r][f_u] = alloc[r].get(f_u, 0) + 1
        tot[f_o] -= 1; tot[f_u] += 1
    out, n = [], 0
    for r in REGION_ORDER:
        act = REGION_ACT[r]
        kinds = []
        for f in sorted(alloc[r]):
            kinds += [("FACTION", f)] * alloc[r][f]
        rest = b[r] - len(kinds)
        for i in range(rest):
            kinds.append((CATS[(i + REGION_ORDER.index(r)) % len(CATS)], "–"))
        # Reihenfolge innerhalb der Region: abwechselnd, deterministisch
        kinds.sort(key=lambda k: (k[0] != "FACTION", k[1], k[0]))
        inter = []
        fq = [k for k in kinds if k[0] == "FACTION"]; ot = [k for k in kinds if k[0] != "FACTION"]
        while fq or ot:
            if fq: inter.append(fq.pop(0))
            if ot: inter.append(ot.pop(0))
        for i, (cat, fac) in enumerate(inter):
            n += 1
            out.append({"Name": f"SQ_{n:03d}", "RegionId": r, "Category": cat, "Faction": fac, "Available": act,
                        "Chain": "", "Chapter": CHAPTER(n), "_i": i})
    # Fraktionsketten FQ_F##_01..04: je Fraktion die ersten 16 Quests (in ID-Reihenfolge) in 4 Ketten à 4
    byf = defaultdict(list)
    for q in out:
        if q["Faction"] != "–":
            byf[q["Faction"]].append(q)
    for f, qs in byf.items():
        k = 4 if len(qs) >= 16 else 2
        size = 4 if len(qs) >= 16 else len(qs) // 2
        for c in range(k):
            for q in qs[c * size:(c + 1) * size]:
                q["Chain"] = f"FQ_{f}_{c + 1:02d}"
    # Verfügbarkeit: Kettenquests bleiben im Akt ihrer Region (Orden: Kette 1 Akt III, Kette 2 Nachhall);
    # jede 4. ungekettete Quest einer Region öffnet später (~20 % gesamt)
    later_idx = defaultdict(int)
    for q in out:
        act = REGION_ACT[q["RegionId"]]
        if q["Faction"] == "F05":
            q["Available"] = "Nachhall" if q["Chain"] == "FQ_F05_02" else "Akt III"
        elif not q["Chain"]:
            later_idx[q["RegionId"]] += 1
            j = later_idx[q["RegionId"]]
            if j % 3 == 0:
                q["Available"] = LATER[act][(j // 3 - 1) % len(LATER[act])]
        del q["_i"]
    # Handgesetzte Ausnahmen (K51: „Letzte Bitten“ muss vor dem Finale spielbar sein, K12 §5)
    for q in out:
        q.update(OVERRIDES.get(q["Name"], {}))
    return out


def write():
    rows = plan()
    with open(OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write("# Nebenquest-Gerüst (K48 §4, generiert von tools/authoring/sq_plan.py). Titel, Auftraggeber und Inhalt: K49–K51.\n")
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} Nebenquests → {OUT.relative_to(ROOT)}")


def _md(head, body):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(map(str, r)) + " |" for r in body])


def region_table():
    rows = plan(); body = []
    for r in REGION_ORDER:
        qs = [q for q in rows if q["RegionId"] == r]
        c = Counter(q["Category"] for q in qs)
        body.append([r, f"{qs[0]['Name']}–{qs[-1]['Name']}", len(qs)] + [c.get(k, 0) for k in ["FACTION"] + CATS] + [", ".join(sorted({q['Chapter'] for q in qs}))])
    tot = Counter(q["Category"] for q in rows)
    body.append(["**Σ**", "", len(rows)] + [tot.get(k, 0) for k in ["FACTION"] + CATS] + [""])
    return _md(["Region", "IDs", "Anzahl"] + [CAT_NAME[k] for k in ["FACTION"] + CATS] + ["Kapitel"], body)


def faction_table():
    rows = plan(); body = []
    for f in sorted(FACTION_TARGET):
        qs = [q for q in rows if q["Faction"] == f]
        reg = Counter(q["RegionId"] for q in qs)
        chains = sorted({q["Chain"] for q in qs if q["Chain"]})
        body.append([f, len(qs), ", ".join(f"{r} {reg[r]}" for r in REGION_ORDER if reg[r]), ", ".join(chains)])
    return _md(["Fraktion", "Quests", "Regionen", "Ketten"], body)


def avail_table():
    rows = plan(); acts = ["Akt I", "Akt II", "Akt III", "Nachhall"]; body = []
    for r in REGION_ORDER:
        c = Counter(q["Available"] for q in rows if q["RegionId"] == r)
        body.append([r] + [c.get(a, 0) for a in acts])
    tot = Counter(q["Available"] for q in rows)
    body.append(["**Σ**"] + [tot.get(a, 0) for a in acts])
    return _md(["Region"] + acts, body)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "write"
    if cmd == "write":
        write()
    else:
        print(region_table()); print(); print(faction_table()); print(); print(avail_table())
