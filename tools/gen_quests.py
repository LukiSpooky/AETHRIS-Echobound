#!/usr/bin/env python3
"""Quest-Validator und Kennzahlen (K48 §11). Aufruf: gen_quests.py validate | ep | ep_table | dr29_table

QV-01 Jede Hauptquest hat ≥ 1 Schritt; Schrittfolgen lückenlos ab 1
QV-02 Zieltypen existieren (ObjectiveTypes.csv)
QV-03 Boss der Quest = Ziel eines OBJ_BOSS-Schritts; jeder Story-Boss genau einer Quest zugeordnet
QV-04 Akkord der Quest = Ziel eines OBJ_ARENA-Schritts; alle 10 Arenen genau einmal
QV-05 Orte existieren (Settlements, StoryPOIs, Regionen, Zonen, LOC_*, dynamisch, –)
QV-06 Vorbedingungen mit Quest-ID verweisen auf existierende Quests
QV-07 W1–W9 genau einmal; Reihenfolge entlang der Akte nicht fallend
QV-08 DR-29: nach Intensität ≥ 7 folgt Intensität ≤ 6 (Ausnahmen ADR-168)
QV-09 StoryFlags.SetIn verweist auf existierende Quests (Muster MQ_A2_* erlaubt)
QV-10 Wärter-EP der Hauptquests je Akt im Zielband 25 % ± 5 Prozentpunkte (CANON §18, K43 §3.1)
"""
import csv, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


MQ = rows("Data/Quests/MainQuests.csv")
STEPS = rows("Data/Quests/MainQuestSteps.csv")
OBJ = {r["Name"] for r in rows("Data/Quests/ObjectiveTypes.csv")}
BOSSES = rows("Data/Combat/Bosses.csv")
ARENAS = {r["Name"] for r in rows("Data/World/Arenas.csv")}
SETTLE = {r["Name"] for r in rows("Data/World/Settlements.csv")}
POIS = {r["Name"] for r in rows("Data/World/StoryPOIs.csv")}
FLAGS = rows("Data/Quests/StoryFlags.csv")
ACTS = ["Prolog", "Akt I", "Akt II", "Akt III"]
DR29_EXCEPTIONS = {("MQ_A3_06", "MQ_A3_07"), ("MQ_A3_07", "MQ_A3_08")}   # ADR-168
# Wärter-EP je Akt (K43 §3.1) und Hauptquest-Ziel 25 %
ACT_EP = {"Prolog": 2400, "Akt I": 30000, "Akt II": 40000, "Akt III": 30000}
HAUPT_SHARE = 0.25
ACT_BONUS = {"Prolog": 0, "Akt I": 100, "Akt II": 200, "Akt III": 200}
SHARE_EXEMPT = {"Prolog"}   # Tutorial: Prolog besteht fast nur aus Hauptquests (K02 §8)


def step_ep(step, quest):
    """K48 §8: Meilenstein-EP = 150 + 50 × Intensität + Aktzuschlag (0/100/200/200); Boss-Schritt × 1,5;
    auf 50 gerundet; Arena-Schritte 0 (Akkord-EP K43). Spanne 300–1.500 (K43 §2)."""
    if step["Milestone"] != "1" or step["Objective"] == "OBJ_ARENA":
        return 0
    v = 150 + 50 * int(quest["Intensity"]) + ACT_BONUS[quest["Act"]]
    if step["Objective"] == "OBJ_BOSS":
        v = v * 3 // 2
    return int(round(v / 50.0)) * 50


def quest_ep():
    q = {m["Name"]: m for m in MQ}
    per = {m["Name"]: 0 for m in MQ}
    for s in STEPS:
        per[s["Quest"]] += step_ep(s, q[s["Quest"]])
    return per


def act_ep():
    per = quest_ep()
    out = {a: 0 for a in ACTS}
    for m in MQ:
        out[m["Act"]] += per[m["Name"]]
    return out


def order_key(m):
    n = re.match(r"(\d+)(.*)", m["Order"])
    return (ACTS.index(m["Act"]), int(n.group(1)), n.group(2), m["Name"])


def location_ok(loc):
    if loc in ("–", "dynamisch") or loc in SETTLE or loc in POIS or loc.startswith(("LOC_", "NPC_", "FLAG_")):
        return True
    return bool(re.fullmatch(r"R\d\d(_Z\d\d)?", loc))


def validate():
    err = []
    names = {m["Name"] for m in MQ}
    by_q = {}
    for s in STEPS:
        by_q.setdefault(s["Quest"], []).append(s)
        if s["Quest"] not in names:
            err.append(f"QV-01 {s['Name']}: Quest {s['Quest']} unbekannt")
        if s["Objective"] not in OBJ:
            err.append(f"QV-02 {s['Name']}: Zieltyp {s['Objective']} unbekannt")
        if not location_ok(s["Location"]):
            err.append(f"QV-05 {s['Name']}: Ort {s['Location']} unbekannt")
        if s["Objective"] in ("OBJ_GOTO",) and s["Target"].startswith(("SET_", "POI_")) and not location_ok(s["Target"]):
            err.append(f"QV-05 {s['Name']}: Ziel {s['Target']} unbekannt")
    for m in MQ:
        st = sorted(by_q.get(m["Name"], []), key=lambda s: int(s["Order"]))
        if not st:
            err.append(f"QV-01 {m['Name']}: keine Schritte")
        elif [int(s["Order"]) for s in st] != list(range(1, len(st) + 1)):
            err.append(f"QV-01 {m['Name']}: Schrittfolge lückenhaft")
        if m["Boss"] and not any(s["Objective"] == "OBJ_BOSS" and s["Target"] == m["Boss"] for s in st):
            err.append(f"QV-03 {m['Name']}: Boss {m['Boss']} ohne OBJ_BOSS-Schritt")
        if m["Akkord"] and not any(s["Objective"] == "OBJ_ARENA" and s["Target"] == m["Akkord"] for s in st):
            err.append(f"QV-04 {m['Name']}: Akkord {m['Akkord']} ohne OBJ_ARENA-Schritt")
        pre = m["Prerequisite"]
        for ref in re.findall(r"MQ_[A-Z0-9_]+", pre):
            if ref not in names:
                err.append(f"QV-06 {m['Name']}: Vorbedingung {ref} unbekannt")
    story = [b["Name"] for b in BOSSES if b["Kind"] == "Story"]
    used = [m["Boss"] for m in MQ if m["Boss"]]
    for b in story:
        if used.count(b) != 1:
            err.append(f"QV-03 Story-Boss {b} {used.count(b)}× zugeordnet")
    ak = [s["Target"] for s in STEPS if s["Objective"] == "OBJ_ARENA"]
    if sorted(ak) != sorted(ARENAS):
        err.append(f"QV-04 Arenen: {sorted(set(ARENAS) ^ set(ak))} / Mehrfach: {[a for a in set(ak) if ak.count(a) > 1]}")
    truths = [m["Truth"] for m in MQ if m["Truth"] not in ("", "–")]
    if sorted(truths) != [f"W{i}" for i in range(1, 10)]:
        err.append(f"QV-07 Wahrheiten: {truths}")
    order = sorted(MQ, key=order_key)
    last = 0
    for m in order:
        if m["Truth"] not in ("", "–"):
            t = int(m["Truth"][1:])
            if t < last:
                err.append(f"QV-07 {m['Name']}: W{t} nach W{last}")
            last = t
    for a, b in zip(order, order[1:]):
        if int(a["Intensity"]) >= 7 and int(b["Intensity"]) > 6 and (a["Name"], b["Name"]) not in DR29_EXCEPTIONS:
            err.append(f"QV-08 DR-29: {a['Name']} ({a['Intensity']}) → {b['Name']} ({b['Intensity']})")
    for f in FLAGS:
        for ref in f["SetIn"].split("|"):
            if ref.endswith("*"):
                if not any(n.startswith(ref[:-1]) for n in names):
                    err.append(f"QV-09 {f['Name']}: {ref} trifft keine Quest")
            elif ref not in names:
                err.append(f"QV-09 {f['Name']}: {ref} unbekannt")
    ep = act_ep()
    for a in ACTS:
        if a in SHARE_EXEMPT:
            continue
        share = ep[a] / ACT_EP[a]
        if abs(share - HAUPT_SHARE) > 0.05:
            err.append(f"QV-10 {a}: Hauptquest-EP {ep[a]} = {share:.0%} (Ziel 25 % ± 5)")
    for s_ in STEPS:
        v = step_ep(s_, {m["Name"]: m for m in MQ}[s_["Quest"]])
        if v and not 300 <= v <= 1500:
            err.append(f"QV-10 {s_['Name']}: {v} EP außerhalb 300–1.500")
    return err


def ep_table():
    ep = act_ep()
    lines = ["| Abschnitt | Hauptquests | Meilensteine | Hauptquest-EP | Wärter-EP gesamt (K43) | Anteil | Ziel |", "|---|---|---|---|---|---|---|"]
    for a in ACTS:
        qs = [m["Name"] for m in MQ if m["Act"] == a]
        ms = sum(1 for s in STEPS if s["Quest"] in qs and s["Milestone"] == "1")
        lines.append(f"| {a} | {len(qs)} | {ms} | {ep[a]:,} | {ACT_EP[a]:,} | {100 * ep[a] / ACT_EP[a]:.0f} % | 25 % |".replace(",", "."))
    return "\n".join(lines)


def quest_ep_table():
    per = quest_ep()
    lines = ["| Quest | Titel | Intensität | Schritte | Meilensteine | Wärter-EP |", "|---|---|---|---|---|---|"]
    for m in MQ:
        st = [s for s in STEPS if s["Quest"] == m["Name"]]
        lines.append(f"| {m['Name']} | {m['Title']} | {m['Intensity']} | {len(st)} | {sum(s['Milestone'] == '1' for s in st)} | {per[m['Name']]:,} |".replace(",", "."))
    return "\n".join(lines)


def dr29_table():
    order = sorted(MQ, key=order_key)
    lines = ["| Von | Intensität | Nach | Intensität | Bewertung |", "|---|---|---|---|---|"]
    for a, b in zip(order, order[1:]):
        if int(a["Intensity"]) >= 7:
            ok = int(b["Intensity"]) <= 6
            verdict = "✓ Atemzug" if ok else ("Ausnahme ADR-168" if (a["Name"], b["Name"]) in DR29_EXCEPTIONS else "✗")
            lines.append(f"| {a['Name']} | {a['Intensity']} | {b['Name']} | {b['Intensity']} | {verdict} |")
    return "\n".join(lines)


def objective_usage():
    from collections import Counter
    c = Counter(s["Objective"] for s in STEPS)
    lines = ["| Zieltyp | Hauptquest-Schritte |", "|---|---|"]
    for o in sorted(OBJ):
        lines.append(f"| {o} | {c.get(o, 0)} |")
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "validate":
        e = validate()
        print("\n".join(e) if e else "")
        print(f"Quest-Validator: {len(MQ)} Hauptquests, {len(STEPS)} Schritte, {len(e)} Fehler.")
        sys.exit(1 if e else 0)
    print(globals()[cmd]())
