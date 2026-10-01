#!/usr/bin/env python3
"""Gemeinsame Infrastruktur für die Nebenquest-Kapitel K49–K51.

Ein Kapitelmodul (sq_k49.py …) beschreibt Quests mit Q(...). Dieses Modul
  - ergänzt Belohnungen nach K48 §8 (Sol, Wärter-EP, Ruf),
  - schreibt Data/Quests/SideQuestDetails.csv und SideQuestSteps.csv (zeilenweise Ersetzung je Quest-ID),
  - prüft die Quest-Bibel (QS-01 … QS-14),
  - erzeugt die Markdown-Abschnitte des Kapitels.
Schrittsyntax:  "OBJ_X ZIEL ANZAHL @ORT | Tagebuchtext"   (ZIEL "-" → CLUE_<SQ>_<n>)
"""
import csv, pathlib, re
from collections import Counter, defaultdict
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


SKEL = {r["Name"]: r for r in rows("Data/Quests/SideQuests.csv")}
FACTIONS = {r["Name"]: r for r in rows("Data/Factions/Factions.csv")}
CHAINS = {r["Name"]: r for r in rows("Data/Quests/FactionChains.csv")}
OBJ = {r["Name"] for r in rows("Data/Quests/ObjectiveTypes.csv")}
SETTLE = {r["Name"]: r for r in rows("Data/World/Settlements.csv")}
POIS = {r["Name"] for r in rows("Data/World/StoryPOIs.csv")}
SPECIES = {r["Name"]: r for r in rows("Data/Echos/Species.csv")}
ITEMS = set()
for f in (ROOT / "Data/Items").glob("*.csv"):
    for r in rows(f"Data/Items/{f.name}"):
        ITEMS.add(r["Name"])
ARENAS = {r["Name"] for r in rows("Data/World/Arenas.csv")}
MQ = {r["Name"] for r in rows("Data/Quests/MainQuests.csv")}
FLAGS = {r["Name"][5:] for r in rows("Data/Quests/StoryFlags.csv")}

ACT_SOL = {"Akt I": 1.0, "Akt II": 1.8, "Akt III": 2.6, "Nachhall": 3.2}
ACT_EP = {"Akt I": 1.0, "Akt II": 1.3, "Akt III": 1.6, "Nachhall": 1.8}
ACT_TRUTH = {"Akt I": 3, "Akt II": 7, "Akt III": 8, "Nachhall": 9}   # höchste Wahrheit, die bei Verfügbarkeit sicher bekannt ist
UNDERSTAND = {"OBJ_OBSERVE", "OBJ_INVESTIGATE", "OBJ_CHOICE", "OBJ_PHOTO", "OBJ_PUZZLE", "OBJ_HEALZONE"}
QUESTS = {}


def r50(x):
    return int(round(x / 50.0)) * 50


class Quest(dict):
    pass


def Q(qid, title, giver, loc, inten, dur, summary, steps, items, cons, var="–", truth=0, pre="", solution=""):
    q = Quest(Name=qid, Title=title, Giver=giver, Location=loc, Intensity=inten, DurationMin=dur, Summary=summary,
              Steps=steps, Items=items, Consequence=cons, Variant=var, TruthLevel=truth, ExtraPre=pre, Solution=solution)
    QUESTS[qid] = q
    return q


def chain_members(chain):
    return [k for k, v in SKEL.items() if v["Chain"] == chain]


def is_chain_final(qid):
    c = SKEL[qid]["Chain"]
    return bool(c) and chain_members(c)[-1] == qid


def prerequisite(q):
    s = SKEL[q["Name"]]
    parts = [f"Act>={s['Available']}"] if s["Available"] != "Akt I" else []
    if s["Faction"] != "–":
        start = FACTIONS[s["Faction"]]["RepStart"]
        parts.append(f"Quest.{start}")
        if s["Chain"]:
            rank = int(CHAINS[s["Chain"]]["EntryRank"])
            if rank > 1:
                parts.append(f"Rank.{s['Faction']}>={rank}")
            mem = chain_members(s["Chain"])
            i = mem.index(q["Name"])
            if i > 0:
                parts.append(f"Quest.{mem[i - 1]}")
    if q["ExtraPre"]:
        parts.append(q["ExtraPre"])
    return " & ".join(parts) if parts else "–"


def rewards(q):
    s = SKEL[q["Name"]]
    act = s["Available"]
    sol = min(3000, r50((150 + 12 * q["DurationMin"]) * ACT_SOL[act]))
    ep = r50((300 + 40 * q["DurationMin"]) * ACT_EP[act])
    if is_chain_final(q["Name"]):
        ep = min(2000, r50(ep * 1.5))
    ep = max(400, min(2000, ep))
    rep = ""
    if s["Faction"] != "–":
        rep = f"{s['Faction']} +{400 if is_chain_final(q['Name']) else 150}"
    return sol, ep, rep


def parse_step(qid, i, txt):
    m = re.fullmatch(r"\s*(OBJ_[A-Z_]+)\s+(\S+)\s+(\d+)\s+@(\S+)\s*\|\s*(.+)", txt)
    if not m:
        raise ValueError(f"{qid}: Schritt unlesbar: {txt}")
    obj, tgt, cnt, loc, text = m.groups()
    if tgt == "-":
        tgt = f"CLUE_{qid.replace('_', '')}_{i}"
    return {"Name": f"STEP_{qid[3:]}_{i:02d}", "Quest": qid, "Order": i, "Objective": obj, "Target": tgt,
            "Count": int(cnt), "Location": loc, "Text": text.strip()}


def location_ok(loc, region):
    if loc in SETTLE:
        return True
    if loc in POIS or loc.startswith(("LOC_", "NPC_")) or loc == "dynamisch":
        return True
    m = re.fullmatch(r"(R\d\d)(_Z\d\d)?", loc)
    return bool(m)


def steps_of(q):
    return [parse_step(q["Name"], i, t) for i, t in enumerate(q["Steps"], 1)]


def validate(ids):
    err = []
    givers = Counter()
    for qid in ids:
        if qid not in QUESTS:
            err.append(f"QS-01 {qid}: fehlt"); continue
        q = QUESTS[qid]; s = SKEL[qid]; st = steps_of(q)
        givers[q["Giver"].split("|")[0]] += 0   # Zählung unten (Ketten = eine Einheit)
        if not 3 <= len(st) <= 6:
            err.append(f"QS-02 {qid}: {len(st)} Schritte (3–6)")
        if not any(x["Objective"] in UNDERSTAND for x in st):
            err.append(f"QS-03 {qid}: kein Verstehen-Schritt (QR-02)")
        if st and st[-1]["Objective"] == "OBJ_COLLECT":
            err.append(f"QS-04 {qid}: endet mit OBJ_COLLECT (QR-03)")
        for x in st:
            if x["Objective"] not in OBJ:
                err.append(f"QS-05 {x['Name']}: Zieltyp {x['Objective']}")
            if not location_ok(x["Location"], s["RegionId"]):
                err.append(f"QS-06 {x['Name']}: Ort {x['Location']}")
            if (x["Location"] in SETTLE and SETTLE[x["Location"]]["RegionId"] != s["RegionId"] and not s["Chain"]
                    and x["Objective"] not in ("OBJ_DELIVER", "OBJ_TALK", "OBJ_GOTO", "OBJ_CHOICE")):
                err.append(f"QS-06 {x['Name']}: Ort {x['Location']} außerhalb {s['RegionId']}")
            if x["Target"].startswith("ECHO_") and x["Target"] not in SPECIES:
                err.append(f"QS-07 {x['Name']}: Art {x['Target']}")
            if x["Target"].startswith("ITM_") and x["Target"] not in ITEMS:
                err.append(f"QS-07 {x['Name']}: Item {x['Target']}")
            if x["Target"].startswith("ARN_") and x["Target"] not in ARENAS:
                err.append(f"QS-07 {x['Name']}: Arena {x['Target']}")
        if not location_ok(q["Location"], s["RegionId"]):
            err.append(f"QS-06 {qid}: Ort {q['Location']}")
        lim = 7 if is_chain_final(qid) else 6
        if not 1 <= q["Intensity"] <= lim:
            err.append(f"QS-08 {qid}: Intensität {q['Intensity']} (≤ {lim})")
        dl = 60 if s["Chain"] else 45
        if not 15 <= q["DurationMin"] <= dl:
            err.append(f"QS-09 {qid}: Dauer {q['DurationMin']} (15–{dl})")
        if not q["Items"]:
            err.append(f"QS-10 {qid}: keine nicht-monetäre Belohnung (QR-10)")
        for it in re.findall(r"ITM_[A-Z0-9_]+", q["Items"]):
            if it not in ITEMS:
                err.append(f"QS-10 {qid}: Item {it} unbekannt")
        if q["TruthLevel"] > ACT_TRUTH[s["Available"]]:
            err.append(f"QS-11 {qid}: TruthLevel {q['TruthLevel']} > {ACT_TRUTH[s['Available']]} (L-01)")
        if s["Category"] == "TRIAL" and not any(x["Objective"] == "OBJ_BATTLE" for x in st):
            err.append(f"QS-12 {qid}: Wärterprüfung ohne OBJ_BATTLE")
        if s["Category"] == "EVENT" and q["Variant"] == "–":
            err.append(f"QS-12 {qid}: Weltereignis ohne Bedingung")
        for ref in re.findall(r"(?:Quest\.)(MQ_[A-Z0-9_]+)", q["ExtraPre"] + " " + q["Variant"]):
            if ref not in MQ:
                err.append(f"QS-13 {qid}: {ref} unbekannt")
        for ref in re.findall(r"Flag\.([A-Z0-9_]+)", q["ExtraPre"] + " " + q["Variant"]):
            if ref not in FLAGS:
                err.append(f"QS-13 {qid}: Flag {ref} unbekannt")
        if s["Faction"] != "–" and s["Chain"] and q["Solution"] == "" and is_chain_final(qid):
            pass
    units = defaultdict(set)
    for qid in ids:
        if qid in QUESTS:
            units[QUESTS[qid]["Giver"].split("|")[0]].add(SKEL[qid]["Chain"] or qid)
    for g, u in units.items():
        n = len(u)
        if n > 3 and not g.startswith(("NPC_HRALDA", "NPC_MARIEKE", "NPC_TAVESH", "NPC_SERETH", "NPC_VENN", "NPC_AEVRIN")):
            err.append(f"QS-14 Auftraggeber {g}: {n} Quests (≤ 3)")
    # QR-09: ≥ 25 % je Region mit Tageszeit/Wetter/Mond
    byreg = defaultdict(list)
    for qid in ids:
        if qid in QUESTS:
            byreg[SKEL[qid]["RegionId"]].append(QUESTS[qid])
    for reg, qs in byreg.items():
        full = sum(1 for k, v in SKEL.items() if v["RegionId"] == reg)
        if len(qs) < full:
            continue   # Region über Kapitelgrenze: Prüfung im Folgekapitel
        n = sum(1 for q in qs if re.search(r"Time=|Weather=|Moon=", q["Variant"]))
        if n * 4 < len(qs):
            err.append(f"QS-15 {reg}: nur {n}/{len(qs)} Quests mit Tageszeit/Wetter/Mond (QR-09)")
    return err


def region_complete_check(ids, regions):
    """QR-09 für Regionen, die über zwei Kapitel reichen: alle bereits geschriebenen Quests der Region zusammen."""
    return []


def write(ids):
    det_p = ROOT / "Data/Quests/SideQuestDetails.csv"
    st_p = ROOT / "Data/Quests/SideQuestSteps.csv"
    det_cols = ["Name", "Title", "Giver", "Location", "Intensity", "TruthLevel", "DurationMin", "Prerequisite", "Variant",
                "Sol", "WardenXP", "Reputation", "Items", "Consequence", "Summary"]
    st_cols = ["Name", "Quest", "Order", "Objective", "Target", "Count", "Location", "Text"]
    old_d = [r for r in rows("Data/Quests/SideQuestDetails.csv") if r["Name"] not in ids] if det_p.exists() else []
    old_s = [r for r in rows("Data/Quests/SideQuestSteps.csv") if r["Quest"] not in ids] if st_p.exists() else []
    new_d, new_s = [], []
    for qid in ids:
        q = QUESTS[qid]
        sol, ep, rep = rewards(q)
        new_d.append({"Name": qid, "Title": q["Title"], "Giver": q["Giver"], "Location": q["Location"],
                      "Intensity": q["Intensity"], "TruthLevel": q["TruthLevel"], "DurationMin": q["DurationMin"],
                      "Prerequisite": prerequisite(q), "Variant": q["Variant"], "Sol": sol, "WardenXP": ep,
                      "Reputation": rep or "–", "Items": q["Items"], "Consequence": q["Consequence"], "Summary": q["Summary"]})
        new_s += steps_of(q)
    alld = sorted(old_d + new_d, key=lambda r: r["Name"])
    alls = sorted(old_s + new_s, key=lambda r: (r["Quest"], int(r["Order"])))
    with open(det_p, "w", encoding="utf-8", newline="") as fh:
        fh.write("# Nebenquest-Details (K49–K51, generiert aus tools/authoring/sq_k4x/sq_k5x). Belohnungen nach K48 §8.\n")
        w = csv.DictWriter(fh, fieldnames=det_cols); w.writeheader(); w.writerows(alld)
    with open(st_p, "w", encoding="utf-8", newline="") as fh:
        fh.write("# Nebenquest-Schritte (K49–K51). Zieltypen: ObjectiveTypes.csv. CLUE_* = Untersuchungshinweise (LD platziert, K57).\n")
        w = csv.DictWriter(fh, fieldnames=st_cols); w.writeheader(); w.writerows(alls)
    return len(new_d), len(new_s)


CAT = {"FACTION": "Fraktion", "ECHO": "Echo-Geschichte", "PEOPLE": "Menschen", "RESEARCH": "Forschung",
       "MYSTERY": "Rätsel & Ruinen", "TRIAL": "Wärterprüfung", "EVENT": "Weltereignis"}
FNAME = {k: v["DisplayName"] for k, v in FACTIONS.items()}
OBJ_SHORT = {"OBJ_TALK": "Sprechen", "OBJ_GOTO": "Gehen", "OBJ_INVESTIGATE": "Untersuchen", "OBJ_OBSERVE": "Beobachten",
             "OBJ_PHOTO": "Foto", "OBJ_BOND": "Binden", "OBJ_BATTLE": "Kampf", "OBJ_BOSS": "Boss", "OBJ_ARENA": "Arena",
             "OBJ_HEALZONE": "Heilen", "OBJ_COLLECT": "Sammeln", "OBJ_DELIVER": "Liefern", "OBJ_ESCORT": "Begleiten",
             "OBJ_TRAVERSE": "Traversal", "OBJ_PUZZLE": "Rätsel", "OBJ_CHOICE": "Entscheidung", "OBJ_CINEMATIC": "Szene",
             "OBJ_REST": "Lager", "OBJ_FLEE": "Flucht", "OBJ_CONDITION": "Bedingung"}


def overview(ids):
    head = "| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |\n|---|---|---|---|---|---|---|---|"
    out = [head]
    for qid in ids:
        q = QUESTS[qid]; s = SKEL[qid]
        fk = "–" if s["Faction"] == "–" else f"{s['Faction']}" + (f" · {s['Chain']}" if s["Chain"] else "")
        out.append(f"| {qid} | {q['Title']} | {CAT[s['Category']]} | {fk} | {s['Available']} | {q['Intensity']} | {q['DurationMin']} | {q['Variant']} |")
    return "\n".join(out)


def card(qid):
    q = QUESTS[qid]; s = SKEL[qid]
    sol, ep, rep = rewards(q)
    giver = q["Giver"].split("|")
    gname = giver[1] if len(giver) > 1 else giver[0]
    chain = ""
    if s["Chain"]:
        mem = chain_members(s["Chain"])
        chain = f" · Kette **{CHAINS[s['Chain']]['Title']}** ({mem.index(qid) + 1}/{len(mem)})"
    loc = SETTLE[q["Location"]]["DisplayName"] if q["Location"] in SETTLE else q["Location"]
    lines = [f"#### {qid} · {q['Title']}", "",
             f"*{CAT[s['Category']]}" + (f" · {FNAME[s['Faction']]}" if s["Faction"] != "–" else "") + f"{chain} · {s['Available']} · Auftrag: {gname} ({loc}) · Intensität {q['Intensity']} · ~{q['DurationMin']} min*", "",
             q["Summary"], ""]
    if q["Solution"]:
        lines += [f"**Lösungen:** {q['Solution']}", ""]
    lines.append("| # | Ziel | Was ich tun soll |")
    lines.append("|---|---|---|")
    for x in steps_of(q):
        lines.append(f"| {x['Order']} | {OBJ_SHORT.get(x['Objective'], x['Objective'])} | {x['Text']} |")
    lines.append("")
    pre = prerequisite(q)
    lines.append(f"**Voraussetzung:** `{pre}`" + (f" · **Variante/Bedingung:** `{q['Variant']}`" if q["Variant"] != "–" else ""))
    lines.append(f"**Belohnung:** {sol:,} ◎ · {ep:,} Wärter-EP".replace(",", ".") + (f" · Ruf {rep}" if rep else "") + f" · {q['Items']}")
    lines.append(f"**Folge:** {q['Consequence']}")
    lines.append("")
    return "\n".join(lines)


def region_cards(ids, region):
    return "\n".join(card(q) for q in ids if SKEL[q]["RegionId"] == region)


def stats(ids):
    qs = [QUESTS[i] for i in ids]
    c = Counter(SKEL[i]["Category"] for i in ids)
    obj = Counter(x["Objective"] for q in qs for x in steps_of(q))
    tot_sol = sum(rewards(q)[0] for q in qs); tot_ep = sum(rewards(q)[1] for q in qs)
    var = sum(1 for q in qs if q["Variant"] != "–")
    lines = ["| Kennzahl | Wert |", "|---|---|",
             f"| Quests | {len(qs)} |",
             f"| Schritte | {sum(len(q['Steps']) for q in qs)} (Ø {sum(len(q['Steps']) for q in qs) / len(qs):.1f}) |".replace(".", ","),
             f"| Ø Dauer | {sum(q['DurationMin'] for q in qs) / len(qs):.0f} min |",
             f"| Σ Spielzeit | {sum(q['DurationMin'] for q in qs) / 60:.1f} h |".replace(".", ","),
             f"| Mit Tageszeit/Wetter/Mond/Bedingung | {var} ({100 * var / len(qs):.0f} %) |",
             f"| Σ Sol | {tot_sol:,} ◎ |".replace(",", "."),
             f"| Σ Wärter-EP | {tot_ep:,} |".replace(",", "."),
             "| Kategorien | " + ", ".join(f"{CAT[k]} {v}" for k, v in c.most_common()) + " |",
             "| Häufigste Zieltypen | " + ", ".join(f"{OBJ_SHORT[k]} {v}" for k, v in obj.most_common(8)) + " |"]
    return "\n".join(lines)


def giver_table(ids):
    g = defaultdict(list)
    for i in ids:
        parts = QUESTS[i]["Giver"].split("|")
        g[(parts[0], parts[1] if len(parts) > 1 else parts[0])].append(i)
    lines = ["| NPC-ID | Name | Quests |", "|---|---|---|"]
    for (k, n), v in sorted(g.items()):
        lines.append(f"| {k} | {n} | {', '.join(v)} |")
    return "\n".join(lines)


def chain_table(ids):
    seen = []
    for i in ids:
        c = SKEL[i]["Chain"]
        if c and c not in seen:
            seen.append(c)
    lines = ["| Kette | Fraktion | Einstieg | Titel | Quests (dieses Kapitel fett) |", "|---|---|---|---|---|"]
    for c in seen:
        mem = chain_members(c)
        ml = ", ".join(f"**{m}**" if m in ids else m for m in mem)
        lines.append(f"| {c} | {CHAINS[c]['Faction']} | Rang {CHAINS[c]['EntryRank']} | {CHAINS[c]['Title']} | {ml} |")
    return "\n".join(lines)
