#!/usr/bin/env python3
"""NPC-Register (K53 §3): sammelt alle benannten NPCs aus Quests, Händlern, Arenen, Fraktionen und Dörfern,
leitet Heimatort, Region, Fraktion und Tagesablauf-Muster ab und schreibt Data/World/Npcs.csv.

Aufruf: gen_npcs.py build | validate | stats
Regeln NP-01 … NP-06 siehe validate().
"""
import csv, pathlib, re, sys
from collections import Counter, defaultdict
ROOT = pathlib.Path(__file__).resolve().parents[1]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


SETTLE = {r["Name"]: r for r in rows("Data/World/Settlements.csv")}
POIS = {r["Name"]: r for r in rows("Data/World/StoryPOIs.csv")}
PATTERNS = {r["Name"] for r in rows("Data/World/SchedulePatterns.csv")}

# Feste Angaben für Story- und Schlüsselfiguren (K07 §12, K44–K47, CANON §52/§57)
STORY = {
    "NPC_YSOLDE": ("Ysolde Varn", "SET_V_LINDWIESEN", "F03", "Wache", "Story", "Voiced"),
    "NPC_KAEL": ("Kael Duran", "SET_V_LINDWIESEN", "F01", "Gelehrt", "Story", "Voiced"),
    "NPC_HRALDA": ("Hralda Brakk", "SET_C_EICHENHALL", "F03", "Wache", "Story", "Voiced"),
    "NPC_TAVESH": ("Tavesh Amaru", "SET_C_MORVENFURT", "F04", "Nachtvolk", "Story", "Voiced"),
    "NPC_MARIEKE": ("Marieke Holm", "SET_C_SALTRANDHAFEN", "F02", "Tagwerk", "Story", "Voiced"),
    "NPC_VENN": ("Aldric Venn", "SET_C_DORUNSRUH", "F01", "Gelehrt", "Story", "Voiced"),
    "NPC_SERETH": ("Sereth Vaun", "LOC_KLOSTER_SCHWEIGFELS", "F05", "Kloster", "Story", "Voiced"),
    "NPC_ULREK": ("Ulrek", "LOC_KLOSTER_SCHWEIGFELS", "F05", "Kloster", "Story", "Voiced"),
    "NPC_AEVRIN": ("Aevrin Thal", "SET_C_DORUNSRUH", "F01", "Gelehrt", "Arena", "Voiced"),
    "NPC_MAELIS": ("Maelis Wendt", "SET_C_EICHENHALL", "–", "Tagwerk", "Arena", "Voiced"),
    "NPC_TORVIK": ("Torvik Hrall", "SET_C_KHARSHOLM", "–", "Schicht", "Arena", "Voiced"),
    "NPC_EVHE": ("Evhe Corrach", "SET_C_MORVENFURT", "–", "Nachtvolk", "Arena", "Voiced"),
    "NPC_SHIRAH": ("Shirah Harrad", "SET_C_QASRSAHRUN", "–", "Nachtvolk", "Arena", "Voiced"),
    "NPC_KALDREX": ("Kaldrex Vorn", "SET_C_SCHLACKENWEHR", "–", "Schicht", "Arena", "Voiced"),
    "NPC_BEKE": ("Beke Tamsen", "SET_C_SALTRANDHAFEN", "–", "Fischer", "Arena", "Voiced"),
    "NPC_SIGRUN": ("Sigrun Fjall", "SET_C_HVITMARK", "–", "Tagwerk", "Arena", "Voiced"),
    "NPC_ILYX": ("Ilyx Brannoc", "SET_C_PRISMARA", "–", "Tagwerk", "Arena", "Voiced"),
    "NPC_ORUMA": ("Oruma Siyel", "SET_C_AERION", "–", "Tagwerk", "Arena", "Voiced"),
    "NPC_PELL": ("Archivarin Pell", "SET_C_EICHENHALL", "F01", "Gelehrt", "Quest", "Voiced"),
    "NPC_OSSIAN": ("Kontorschreiber Ossian", "SET_C_EICHENHALL", "F02", "Tagwerk", "Quest", "Voiced"),
    "NPC_FENJA": ("Zeugmeisterin Fenja", "SET_C_EICHENHALL", "F03", "Wache", "Quest", "Voiced"),
    "NPC_SCHWESTER_IVRA": ("Schwester Ivra", "LOC_KLOSTER_SCHWEIGFELS", "F05", "Kloster", "Quest", "SlateWritten"),
    "NPC_R03_SHADE": ("Der Schatten", "SET_C_MORVENFURT", "F04", "Nachtvolk", "Merchant", "Voiced"),
    "NPC_ELSBETH_MOOR": ("Rätin Elsbeth Moor", "SET_C_EICHENHALL", "–", "Tagwerk", "Story", "Voiced"),
    "NPC_AILSA": ("Fährmeisterin Ailsa Duvreth", "SET_C_MORVENFURT", "–", "Fischer", "Quest", "Voiced"),
    "NPC_R07_ASTRID": ("Sprecherin Astrid Eiðsen", "SET_C_HVITMARK", "–", "Tagwerk", "Quest", "Voiced"),
    "NPC_BRUDER_ODVAR": ("Bruder Odvar", "SET_V_SAEULENRAST", "F05", "Kloster", "Village", "Voiced"),
    "NPC_GUNNHILD": ("Gunnhild", "LOC_KLOSTER_SCHWEIGFELS", "F05", "Kloster", "Quest", "SlateWritten"),
}
# Schlüssel-NPCs der Dörfer (CANON §57), soweit nicht schon über Quests erfasst
VILLAGE = {
    "NPC_HEDDA": ("Bäckerin Hedda", "SET_V_LINDWIESEN"), "NPC_JOST": ("Müller Jost", "SET_V_LINDWIESEN"),
    "NPC_BRIDA": ("Köhlerin Brida", "SET_V_MOOSGRUND"), "NPC_ULF_BRAKK": ("Ulf Brakk", "SET_V_BRAKKFELS"),
    "NPC_SVALA": ("Hirtin Svala", "SET_V_HRALLSTED"), "NPC_LORCAN": ("Lorcan", "SET_V_FENNHAVEN"),
    "NPC_AMA_DUVRETH": ("Moorweise Ama Duvreth", "SET_V_DUVRETH"), "NPC_NADIRA": ("Brunnenwächterin Nadira", "SET_V_HARRAD"),
    "NPC_KESH": ("Dünenbauer Kesh", "SET_V_MIRSAAN"), "NPC_IMRAN": ("Imran", "SET_V_ASHURIM"),
    "NPC_THESSA": ("Thessa", "SET_V_VORTHAX"), "NPC_MALVA": ("Kurwirtin Malva", "SET_V_KALDRA"),
    "NPC_MARLENE": ("Marlene", "SET_V_TANGWERFT"), "NPC_OKKO": ("Okko", "SET_V_MOEWENHUK"),
    "NPC_EBBA": ("Ebba", "SET_V_FLOTTHOLM"), "NPC_LEIF": ("Leif", "SET_V_FJALLSTAD"),
    "NPC_HALLA": ("Halla", "SET_V_EIDVIKNEU"), "NPC_DR_IMKE_VAEL": ("Dr. Imke Vael", "SET_V_THAELUUN"),
    "NPC_STEIGER_BRANNOC": ("Steiger Brannoc d. Ä.", "SET_V_GLANZSCHACHT"), "NPC_SCHLEIFERIN_NYX": ("Schleiferin Nyx", "SET_V_QUARZGRUND"),
    "NPC_STERNWAERTER_ELUN": ("Sternwärter Elun", "SET_V_LUMEYA"), "NPC_WINDSEGLERIN_RIA": ("Windseglerin Ria", "SET_V_WOLKENRAST"),
}
# Händler-IDs aus K11/K12, die dieselbe Person wie eine Story-/Quest-ID bezeichnen (Alias → kanonische ID)
ALIASES = {"NPC_R08_PELL": "NPC_PELL", "NPC_R08_AEVRIN_TUTOR": "NPC_AEVRIN", "NPC_R09_ILYX_TUTOR": "NPC_ILYX",
           "NPC_R10_ORUMA_TUTOR": "NPC_ORUMA", "NPC_R06_MARIEKE_OFFICE": "NPC_MARIEKE"}
TRAINER_RE = re.compile(r"WERFT_NORD|WERFT_SUED|PRUEFER|KRIEGER|GESELLE|GARDENER|WERFT_|RENNFLIEGER|FECHTER|KAEMPFER|STURMECHO|FAENGER|NETZKNUEPFER|GRABUNGSWACHE|SPIEGELTRAEGER|MOORKOENIG")
NIGHT_CITIES = {"SET_C_MORVENFURT", "SET_C_QASRSAHRUN"}
SHIFT_CITIES = {"SET_C_KHARSHOLM", "SET_C_SCHLACKENWEHR"}


def region_of(loc):
    if loc in SETTLE:
        return SETTLE[loc]["RegionId"]
    if loc in POIS:
        return POIS[loc]["RegionId"]
    if loc.startswith("LOC_KLOSTER"):
        return "R07"
    m = re.match(r"(R\d\d)", loc)
    return m.group(1) if m else "–"


def pretty(nid):
    base = re.sub(r"^NPC_(R\d\d_)?", "", nid).replace("_", " ").title()
    return base.replace("Ae", "Ä").replace("Oe", "Ö").replace("Ue", "Ü") if False else base


def collect():
    npcs = {}
    seen = defaultdict(list)       # NPC → [(Quelle, Ort)]
    names = {}
    faction = {}
    kind = {}
    # Händler
    for m in rows("Data/Economy/Merchants.csv"):
        n = m["Npc"]
        seen[n].append((m["Name"], m["Settlement"]))
        names.setdefault(n, f"{pretty(n)} – {m['ShopName'].split('(')[0].strip()}")
        kind.setdefault(n, "Merchant")
        if int(m["OpenFrom"]) > int(m["OpenTo"]):
            kind[n + "#night"] = True
    # Hauptquests
    for s in rows("Data/Quests/MainQuestSteps.csv"):
        if s["Target"].startswith("NPC_"):
            seen[s["Target"]].append((s["Quest"], s["Location"]))
    # Nebenquests
    det = {r["Name"]: r for r in rows("Data/Quests/SideQuestDetails.csv")}
    skel = {r["Name"]: r for r in rows("Data/Quests/SideQuests.csv")}
    for q, r in det.items():
        gid, _, gname = r["Giver"].partition("|")
        seen[gid].append((q, r["Location"]))
        names.setdefault(gid, re.sub(r"\s*\(.*\)$", "", gname) or gid)
        if skel[q]["Faction"] != "–":
            faction.setdefault(gid, Counter())[skel[q]["Faction"]] += 1
    for s in rows("Data/Quests/SideQuestSteps.csv"):
        if s["Target"].startswith("NPC_"):
            seen[s["Target"]].append((s["Quest"], s["Location"]))
    for k, (n, home) in VILLAGE.items():
        seen[k].append(("CANON §57", home))
        names[k] = n
        kind.setdefault(k, "Village")
    for k, v in STORY.items():
        seen[k].append(("K07/K44", v[1]))
    # Aliasse zusammenführen
    for a, c in ALIASES.items():
        if a in seen:
            seen[c].extend(seen.pop(a))
    # Zusammenführen
    for nid, src in seen.items():
        if not nid.startswith("NPC_"):
            continue
        if nid in STORY:
            dn, home, fac, pat, kd, pres = STORY[nid]
        else:
            locs = Counter(l for _, l in src if l in SETTLE or l.startswith("LOC_"))
            home = locs.most_common(1)[0][0] if locs else next((l for _, l in src if l not in ("–", "dynamisch")), "–")
            if nid in VILLAGE:
                home = VILLAGE[nid][1]
            dn = names.get(nid) or pretty(nid)
            fac = faction[nid].most_common(1)[0][0] if nid in faction else "–"
            if nid.startswith("NPC_FS_ZELLE"):
                fac = "F04"
            kd = "Group" if nid.startswith("NPC_FS_ZELLE") else ("Trainer" if TRAINER_RE.search(nid) else kind.get(nid, "Quest"))
            pat = schedule_for(nid, dn, home, fac, kd, kind.get(nid + "#night"))
            pres = "SlateWritten" if fac == "F05" and home.startswith("LOC_KLOSTER") else ("Barked" if kd in ("Trainer", "Group") else "Voiced")
        quests = sorted({q for q, _ in src if re.match(r"(MQ|SQ)_", q)})
        alias = "|".join(a for a, c in ALIASES.items() if c == nid) or "–"
        npcs[nid] = {"Name": nid, "Aliases": alias, "DisplayName": dn, "Kind": kd, "Faction": fac, "HomeSettlement": home,
                     "Region": region_of(home), "Schedule": pat, "Presentation": pres,
                     "Quests": len(quests), "FirstQuest": quests[0] if quests else "–"}
    return npcs


def schedule_for(nid, dn, home, fac, kd, night_shop):
    low = dn.lower()
    if kd == "Trainer":
        return "Wache"
    if fac == "F05":
        return "Kloster"
    if fac == "F04" or night_shop:
        return "Nachtvolk"
    if fac == "F03" or "wächter" in low or "wart" in low or "wacht" in low:
        return "Wache"
    if fac == "F01" or any(w in low for w in ("gelehrt", "forscher", "student", "professor", "lehrling", "archiv", "dr.", "laborleiter", "fotograf")):
        return "Gelehrt"
    if any(w in low for w in ("fischer", "taucher", "tang", "kapitän", "fähr", "eisfischer", "seglerin")):
        return "Fischer"
    if any(w in low for w in ("hirt", "hirtin")):
        return "Hirte"
    if "kind" in low or nid in ("NPC_LINA",):
        return "Kind"
    if home == "SET_V_ASHURIM":
        return "Karawane"
    if home in NIGHT_CITIES:
        return "Nachtvolk"
    if home in SHIFT_CITIES or any(w in low for w in ("bergmann", "steiger", "schmied", "gießer")):
        return "Schicht"
    return "Tagwerk"


def build():
    npcs = collect()
    cols = ["Name", "Aliases", "DisplayName", "Kind", "Faction", "HomeSettlement", "Region", "Schedule", "Presentation", "Quests", "FirstQuest"]
    with open(ROOT / "Data/World/Npcs.csv", "w", encoding="utf-8", newline="") as fh:
        fh.write("# NPC-Register (K53 §3, generiert von tools/gen_npcs.py aus Quests, Händlern, Arenen, Fraktionen, Dörfern). Abweichungen über STORY/VILLAGE-Tabellen im Generator.\n")
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for k in sorted(npcs):
            w.writerow(npcs[k])
    return len(npcs)


def validate():
    err = []
    reg = {r["Name"]: r for r in rows("Data/World/Npcs.csv")}
    refs = set()
    for s in rows("Data/Quests/MainQuestSteps.csv") + rows("Data/Quests/SideQuestSteps.csv"):
        if s["Target"].startswith("NPC_"):
            refs.add(s["Target"])
    for r in rows("Data/Quests/SideQuestDetails.csv"):
        refs.add(r["Giver"].split("|")[0])
    for m in rows("Data/Economy/Merchants.csv"):
        refs.add(m["Npc"])
    known = set(reg) | {a for r in reg.values() for a in r["Aliases"].split("|") if a != "–"}
    for n in sorted(refs - known):
        err.append(f"NP-01 {n}: referenziert, aber nicht im Register")
    for n, r in reg.items():
        h = r["HomeSettlement"]
        if not (h in SETTLE or h.startswith("LOC_") or h in POIS or re.fullmatch(r"R\d\d_Z\d\d", h)):
            err.append(f"NP-02 {n}: Heimatort {h} unbekannt")
        if r["Schedule"] not in PATTERNS:
            err.append(f"NP-03 {n}: Muster {r['Schedule']} unbekannt")
    for m in rows("Data/Economy/Merchants.csv"):
        r = reg.get(ALIASES.get(m["Npc"], m["Npc"]))
        if r and int(m["OpenFrom"]) > int(m["OpenTo"]) and r["Schedule"] not in ("Nachtvolk", "Fischer"):
            err.append(f"NP-04 {m['Npc']}: Nachtladen, aber Muster {r['Schedule']}")
    # NP-05: Budget benannter NPCs je Stadt (CANON §53)
    budget = {"SET_C_EICHENHALL": 48, "SET_C_KHARSHOLM": 40, "SET_C_MORVENFURT": 42, "SET_C_QASRSAHRUN": 44, "SET_C_SALTRANDHAFEN": 52}
    c = Counter(r["HomeSettlement"] for r in reg.values() if r["Kind"] != "Trainer")
    for city, b in budget.items():
        if c[city] > b:
            err.append(f"NP-05 {city}: {c[city]} benannte NPCs > Budget {b}")
    return err


def stats():
    reg = rows("Data/World/Npcs.csv")
    by = Counter(r["Kind"] for r in reg)
    sch = Counter(r["Schedule"] for r in reg)
    regc = Counter(r["Region"] for r in reg)
    return by, sch, regc, len(reg)


def stats_table():
    by, sch, regc, n = stats()
    kinds = {"Story": "Story", "Arena": "Arenameister", "Quest": "Quest-NPC", "Merchant": "Händler", "Village": "Dorf-Schlüssel",
             "Trainer": "Prüfer/Kämpfer", "Group": "Gruppe (Zelle)"}
    l1 = ["| Art | Anzahl |", "|---|---|"] + [f"| {kinds.get(k, k)} | {v} |" for k, v in by.most_common()] + [f"| **Σ** | **{n}** |"]
    l2 = ["| Muster | NPCs |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sch.most_common()]
    l3 = ["| Region | NPCs |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(regc.items())]
    return "\n".join(l1) + "\n\n" + "\n".join(l2) + "\n\n" + "\n".join(l3)


def city_table():
    reg = rows("Data/World/Npcs.csv")
    budget = {"SET_C_EICHENHALL": 48, "SET_C_KHARSHOLM": 40, "SET_C_MORVENFURT": 42, "SET_C_QASRSAHRUN": 44, "SET_C_SALTRANDHAFEN": 52}
    lines = ["| Stadt | Benannte NPCs (Register, ohne Prüfer) | Budget (CANON §53) | Reserve für Ambient-Benannte |", "|---|---|---|---|"]
    for city in [k for k, v in SETTLE.items() if v["Type"] == "City"]:
        n = sum(1 for r in reg if r["HomeSettlement"] == city and r["Kind"] != "Trainer")
        b = budget.get(city, "–")
        lines.append(f"| {SETTLE[city]['DisplayName']} | {n} | {b} | {b - n if isinstance(b, int) else '–'} |")
    return "\n".join(lines)


def sample_table(kind="Story"):
    reg = [r for r in rows("Data/World/Npcs.csv") if r["Kind"] == kind]
    lines = ["| ID | Name | Fraktion | Heimat | Muster | Darstellung | Quests |", "|---|---|---|---|---|---|---|"]
    for r in reg:
        home = SETTLE[r["HomeSettlement"]]["DisplayName"] if r["HomeSettlement"] in SETTLE else r["HomeSettlement"]
        lines.append(f"| {r['Name']} | {r['DisplayName']} | {r['Faction']} | {home} | {r['Schedule']} | {r['Presentation']} | {r['Quests']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "build":
        print(build(), "NPCs → Data/World/Npcs.csv")
    elif cmd == "validate":
        e = validate()
        print("\n".join(e))
        print(f"NPC-Register: {len(rows('Data/World/Npcs.csv'))} NPCs, {len(e)} Verstöße.")
        if e:
            sys.exit(1)
    else:
        print(stats_table())


ACT_DE = {"Sleep": "Schlafen", "Wake": "Aufstehen", "Work": "Arbeit", "Meal": "Essen", "Free": "Freizeit", "Tavern": "Gasthaus",
          "Market": "Markt", "Home": "Zuhause", "Patrol": "Streife", "Shift": "Wachwechsel", "Lecture": "Vorlesung", "Lab": "Labor",
          "Library": "Bibliothek", "Read": "Lesen", "Silence": "Stille Stunde", "Fish": "Fischen", "Herd": "Hüten", "School": "Unterricht",
          "Play": "Spielen", "Travel": "Reise", "Rest": "Rast"}


def schedule_blocks():
    lines = ["| Muster | Wofür | Ablauf (Spielstunden) |", "|---|---|---|"]
    for r in rows("Data/World/SchedulePatterns.csv"):
        if r["Name"] in ("SchichtA", "SchichtB", "SchichtC"):
            continue
        hs = [r[f"H{h:02d}"] for h in range(24)]
        blocks, start = [], 0
        for h in range(1, 25):
            if h == 24 or hs[h] != hs[start]:
                blocks.append(f"{start:02d}–{h:02d} {ACT_DE[hs[start]]}")
                start = h
        lines.append(f"| **{r['Name']}** | {r['Description']} | " + " · ".join(blocks) + " |")
    return "\n".join(lines)
