#!/usr/bin/env python3
"""Lernsets, Passiv-Optionen, Klangschriften und Tutoren (K29) – deterministisch aus Arten- und Fähigkeitsdaten.

Aufruf:
  gen_learnsets.py build      -> schreibt Data/Echos/Learnsets.csv, Data/Echos/PassiveOptions.csv,
                                 Data/Items/Klangschriften.csv, Data/Abilities/Tutors.csv
  gen_learnsets.py validate   -> Regeln LS-01 … LS-12
  gen_learnsets.py show NAME  -> Lernset einer Art als Markdown

Kein Zufall: Auswahl über stabile Hashes (sha1 von Art+Schlüssel), damit Neuaufbau bitgleich ist.
"""
import csv, hashlib, pathlib, sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPECIES = ROOT / "Data/Echos/Species.csv"
ABIL = ROOT / "Data/Abilities/Abilities.csv"
CHART = ROOT / "Data/Combat/TypeChart.csv"
OUT_LS = ROOT / "Data/Echos/Learnsets.csv"
OUT_PO = ROOT / "Data/Echos/PassiveOptions.csv"
OUT_KS = ROOT / "Data/Items/Klangschriften.csv"
OUT_TU = ROOT / "Data/Abilities/Tutors.csv"
TYPES = ["Ember", "Tide", "Stone", "Storm", "Bloom", "Frost", "Void", "Light", "Venom", "Metal", "Spirit",
         "Crystal", "Sound", "Gravity", "Arcane"]
PHYS_ROLES = {"Striker", "Tank", "AllRound"}
FACTIONS = ["F01", "F02", "F03", "F04", "F05"]


def h(*parts):
    return int(hashlib.sha1("|".join(map(str, parts)).encode()).hexdigest()[:8], 16)


def rows(path):
    return list(csv.DictReader(l for l in open(path, encoding="utf-8") if not l.startswith("#")))


def tier(a):
    """Lernstufe einer aktiven Fähigkeit aus Stärke/Zeitkosten: E(instieg) M(ittel) L(ate) H(eavy) S(tatus)."""
    p, c = int(a["Power"] or 0), int(a["TimeCost"] or 0)
    if a["Category"] == "Status":
        return "S"
    if p >= 100:
        return "H"
    if p >= 80 or c >= 110:
        return "L"
    if p <= 45:
        return "E"
    return "M"


TIER_LEVEL = {"E": (1, 8), "M": (10, 30), "S": (6, 34), "L": (28, 44), "H": (36, 52)}


class Data:
    def __init__(self):
        self.sp = rows(SPECIES)
        ab = rows(ABIL)
        self.act = [a for a in ab if a["Kind"] == "Active"]
        self.pas = [a for a in ab if a["Kind"] == "Passive"]
        self.by_type = defaultdict(list)
        for a in self.act:
            self.by_type[a["Type"]].append(a)
        self.pas_by_type = defaultdict(list)
        for a in self.pas:
            self.pas_by_type[a["Type"]].append(a)
        chart = rows(CHART)
        self.eff = {r["Name"]: {t: int(r[t]) for t in TYPES} for r in chart}

    def coverage(self, types):
        """Zwei Abdeckungstypen: Typen, die gegen die Resistenzen der eigenen Primärfarbe sehr effektiv sind."""
        p = types[0]
        resisted = [t for t in TYPES if self.eff[p][t] < 1000]
        score = Counter()
        for t in TYPES:
            if t in types:
                continue
            score[t] = sum(1 for r in resisted if self.eff[t][r] > 1000) * 100 + h(p, t) % 50
        return [t for t, _ in score.most_common(2)]


def physical(s):
    return int(s["Attack"]) > int(s["SpAttack"]) or (int(s["Attack"]) == int(s["SpAttack"]) and s["Role"] in PHYS_ROLES)


def pick(cands, n, key, prefer_cat=None):
    def score(a):
        pref = 0 if prefer_cat is None or a["Category"] in (prefer_cat, "Status") else 1
        return (pref, h(key, a["Name"]))
    return sorted(cands, key=score)[:n]


def learnset(D, s):
    types = [s["PrimaryType"].split(".")[1]] + ([s["SecondaryType"].split(".")[1]] if s["SecondaryType"] else [])
    kind, stage = s["LineKind"], int(s["Stage"])
    cat = "Physical" if physical(s) else "Special"
    name = s["Name"]
    p_pool = D.by_type[types[0]]
    by_t = defaultdict(list)
    for a in p_pool:
        by_t[tier(a)].append(a)
    chosen = []
    # Primärtyp: 2 Einstieg, 2 Mittel, 2 Status, 1 Spät, (Schwer bei Endformen/Einzel/Legendär)
    chosen += pick(by_t["E"], 2, name + "E", cat)
    chosen += pick(by_t["M"], 2, name + "M", cat)
    chosen += pick(by_t["S"], 2, name + "S")
    chosen += pick(by_t["L"], 1, name + "L", cat)
    final = kind in ("Single", "Legendary", "Mythical", "Branch") or (kind == "Three" and stage == 3) or (kind == "Two" and stage == 2)
    if final or stage >= 2:
        chosen += pick(by_t["H"], 1, name + "H", cat)
    # Sekundärtyp
    if len(types) > 1:
        q = defaultdict(list)
        for a in D.by_type[types[1]]:
            q[tier(a)].append(a)
        chosen += pick(q["E"] + q["M"], 2, name + "Q", cat)
        chosen += pick(q["S"], 1, name + "QS")
        if stage >= 2 or final:
            chosen += pick(q["L"], 1, name + "QL", cat)
    # Abdeckung: 2 Fremdtypen (immer enthalten, LS-03)
    cov = []
    for ct in D.coverage(types):
        c = [a for a in D.by_type[ct] if tier(a) in ("M", "L") and a["Category"] in (cat, "Status")] or \
            [a for a in D.by_type[ct] if tier(a) in ("M", "L", "S")]
        cov += pick(c, 1, name + ct)
    # Zielgröße
    target = {("Three", 1): 9, ("Three", 2): 11, ("Three", 3): 13, ("Two", 1): 10, ("Two", 2): 12}.get((kind, stage), 13)
    seen, own = set(), []
    for a in chosen:
        if a["Name"] not in seen:
            seen.add(a["Name"])
            own.append(a)
    extra = [a for a in p_pool if a["Name"] not in seen and tier(a) in ("M", "S")]
    own += pick(extra, max(0, target - 2 - len(own)), name + "X")
    # Kürzen: Einstieg/Status zuerst behalten, Überhang von hinten (Sekundär-Spät) entfernen
    out = own[:target - 2] + cov
    # Level vergeben
    legend = kind in ("Legendary", "Mythical")
    res = []
    for a in out:
        lo, hi = TIER_LEVEL[tier(a)]
        lv = 1 if legend and tier(a) in ("E", "M", "S") else lo + h(name, a["Name"]) % (hi - lo + 1)
        if legend and tier(a) in ("L", "H"):
            lv = 50 + h(name, a["Name"]) % 21
        res.append([lv, a])
    res.sort(key=lambda x: (x[0], x[1]["Name"]))
    # mindestens eine Status-Fähigkeit bis Lv. 20 (LS-04)
    st = [x for x in res if x[1]["Category"] == "Status"]
    if st and min(x[0] for x in st) > 20:
        st[0][0] = 12 + h(name, "st") % 8
    # zwei Einstiegsfähigkeiten auf Lv. 1 (LS-05)
    ent = [x for x in res if tier(x[1]) == "E"][:2]
    ent += [x for x in res if tier(x[1]) in ("M", "S") and x not in ent][:2 - len(ent)]
    for x in ent:
        x[0] = 1
    res.sort(key=lambda x: (x[0], x[1]["Name"]))
    return types, res


def build():
    D = Data()
    ls_rows, po_rows = [], []
    sig_by_line = {}
    for s in D.sp:
        types, res = learnset(D, s)
        for lv, a in res:
            ls_rows.append(dict(Species=s["Name"], Method="Level", Level=lv, Ability=a["Name"]))
        # Evolutionsfähigkeit: erste Spät-Fähigkeit des (neuen) Zweittyps bzw. Primärtyps, die noch nicht im Set ist
        if int(s["Stage"]) >= 2:
            have = {a["Name"] for _, a in res}
            t = types[-1]
            cand = [a for a in D.by_type[t] if a["Name"] not in have and tier(a) in ("L", "M")] or \
                   [a for a in D.by_type[types[0]] if a["Name"] not in have]
            ev = pick(cand, 1, s["Name"] + "EVO")[0]
            ls_rows.append(dict(Species=s["Name"], Method="Evolution", Level=0, Ability=ev["Name"]))
        # Ei-Fähigkeiten (nur Stufe 1 der Linien, nicht legendär)
        if int(s["Stage"]) == 1 and s["LineKind"] in ("Three", "Two", "Single"):
            have = {a["Name"] for _, a in res}
            foreign = [t for t in TYPES if t not in types]
            ets = sorted(foreign, key=lambda t: h(s["Line"], t))[:3]
            for t in ets:
                c = [a for a in D.by_type[t] if a["Category"] == "Status" and a["Name"] not in have]
                e = pick(c, 1, s["Line"] + t)[0]
                ls_rows.append(dict(Species=s["Name"], Method="Egg", Level=0, Ability=e["Name"]))
        # Passiv-Optionen
        if s["LineKind"] in ("Legendary", "Mythical"):
            fk = [a for a in D.pas if "Feldklang" in a["Tags"] and a["Description"].startswith(s["DisplayName"] + ":")]
            po_rows.append(dict(Species=s["Name"], Ability=fk[0]["Name"], Hidden=0))
            continue
        pool = [a for t in types for a in D.pas_by_type[t] if "Feldklang" not in a["Tags"]]
        n_opt = 1 + h(s["Line"], "n") % 2 + (1 if len(types) > 1 else 0)
        opts = pick(pool, min(3, n_opt), s["Line"] + "P")       # Linien teilen Optionen (Evolution bildet ab, CANON §86)
        for a in opts:
            po_rows.append(dict(Species=s["Name"], Ability=a["Name"], Hidden=0))
        hid_pool = [a for a in D.pas if "Feldklang" not in a["Tags"] and a not in opts and a["Type"] not in types]
        hid = pick(hid_pool, 1, s["Line"] + "HID")[0]
        po_rows.append(dict(Species=s["Name"], Ability=hid["Name"], Hidden=1))
    # Klangschriften: 6 je Typ (Mittel/Spät/Status, keine Einstiegsfähigkeiten, keine Schwer-Fähigkeit)
    ks_rows, tu_rows = [], []
    n = 1
    for t in TYPES:
        cands = [a for a in D.by_type[t] if tier(a) in ("M", "L", "S")]
        ks = sorted(cands, key=lambda a: (tier(a) != "S", h("KS", a["Name"])))[:3] + \
             sorted([a for a in cands if tier(a) != "S"], key=lambda a: h("KS2", a["Name"]))[:3]
        uniq = []
        for a in ks:
            if a not in uniq:
                uniq.append(a)
        rest = [a for a in cands if a not in uniq]
        uniq += rest[:6 - len(uniq)]
        for a in uniq[:6]:
            ks_rows.append(dict(Name=f"ITM_KS_{n:03d}", Ability=a["Name"], Type=t,
                                DisplayName=f"Klangschrift: {a['DisplayName']}",
                                Compat="Typ des Echos oder Abdeckungstyp (K29 §5)"))
            n += 1
        heavy = [a for a in D.by_type[t] if tier(a) == "H"]
        other = [a for a in D.by_type[t] if a not in uniq and tier(a) != "E" and a not in heavy]
        for i, a in enumerate((heavy + other)[:2]):
            tu_rows.append(dict(Ability=a["Name"], Type=t, Tutor=f"TUT_{t.upper()}_{i + 1}",
                                Faction=FACTIONS[(TYPES.index(t) + i) % 5], ReputationRank=3 + i,
                                CostSol=2000 + 1500 * i, Compat="Typ des Echos"))
    write(OUT_LS, ["Species", "Method", "Level", "Ability"], ls_rows,
          "# Lernsets (K29). Method: Level | Evolution (beim Stufenwechsel) | Egg (Vererbung, K38). Klangschriften/Tutoren regelbasiert.")
    write(OUT_PO, ["Species", "Ability", "Hidden"], po_rows,
          "# Passiv-Optionen (K29): 1–3 sichtbare + 1 versteckte; Legendäre/Mythische: Feldklang.")
    write(OUT_KS, ["Name", "DisplayName", "Ability", "Type", "Compat"], ks_rows,
          "# Klangschriften (K29, 90, wiederverwendbar, nicht handelbar – CANON §18). Fundorte → K41/K42/K49–K51.")
    write(OUT_TU, ["Tutor", "Ability", "Type", "Faction", "ReputationRank", "CostSol", "Compat"], tu_rows,
          "# Tutoren (K29, 30 Fähigkeiten): Fraktionslehrer, Rufrang 3–4 (K47), Sol-Kosten (K42).")
    print(f"Lernsets {len(ls_rows)} Einträge, Passiv-Optionen {len(po_rows)}, Klangschriften {len(ks_rows)}, Tutoren {len(tu_rows)}")


def write(path, fields, data, comment):
    with open(path, "w", newline="", encoding="utf-8") as f:
        f.write(comment + "\n")
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(data)


def validate():
    D = Data()
    ab = {a["Name"]: a for a in rows(ABIL)}
    ls = rows(OUT_LS)
    po = rows(OUT_PO)
    ks = rows(OUT_KS)
    tu = rows(OUT_TU)
    errs = []
    by_sp = defaultdict(list)
    for r in ls:
        if r["Ability"] not in ab:
            errs.append(f"LS-01 {r['Species']}: Fähigkeit {r['Ability']} unbekannt")
        by_sp[r["Species"]].append(r)
    learnable = set()
    for s in D.sp:
        sid = s["Name"]
        types = [s["PrimaryType"].split(".")[1]] + ([s["SecondaryType"].split(".")[1]] if s["SecondaryType"] else [])
        lv = [r for r in by_sp[sid] if r["Method"] == "Level"]
        learnable |= {r["Ability"] for r in by_sp[sid]}
        if not 8 <= len(lv) <= 14:
            errs.append(f"LS-02 {sid}: {len(lv)} Level-Einträge (8–14)")
        own = sum(1 for r in lv if ab[r["Ability"]]["Type"] in types)
        if own * 100 < 60 * len(lv):
            errs.append(f"LS-03 {sid}: nur {own}/{len(lv)} eigene Typen (≥ 60 %)")
        foreign = sum(1 for r in lv if ab[r["Ability"]]["Type"] not in types)
        if foreign < 2:
            errs.append(f"LS-03 {sid}: nur {foreign} Fremdtyp-Fähigkeiten (≥ 2)")
        st = [int(r["Level"]) for r in lv if ab[r["Ability"]]["Category"] == "Status"]
        if not st or min(st) > 20:
            errs.append(f"LS-04 {sid}: keine Status-Fähigkeit bis Lv. 20")
        l1 = sum(1 for r in lv if r["Level"] == "1")
        if l1 < 2:
            errs.append(f"LS-05 {sid}: < 2 Fähigkeiten auf Lv. 1")
        for r in lv:
            a = ab[r["Ability"]]
            if a["Type"] == types[0] and tier(a) == "H" and int(r["Level"]) < 36:
                errs.append(f"LS-06 {sid}: Schwer-Fähigkeit {a['DisplayName']} vor Lv. 36")
        if int(s["Stage"]) >= 2 and not any(r["Method"] == "Evolution" for r in by_sp[sid]):
            errs.append(f"LS-07 {sid}: keine Evolutionsfähigkeit")
        p = [r for r in po if r["Species"] == sid]
        vis = [r for r in p if r["Hidden"] == "0"]
        if s["LineKind"] in ("Legendary", "Mythical"):
            if len(p) != 1 or "Feldklang" not in ab[p[0]["Ability"]]["Tags"]:
                errs.append(f"LS-08 {sid}: Legendäre brauchen genau ihren Feldklang")
        elif not (1 <= len(vis) <= 3 and len(p) - len(vis) == 1):
            errs.append(f"LS-08 {sid}: Passiv-Optionen {len(vis)}+{len(p) - len(vis)} (1–3 + 1)")
    # Klangschriften, Tutoren
    if len(ks) != 90 or len({r["Ability"] for r in ks}) != 90:
        errs.append(f"LS-09 Klangschriften: {len(ks)} (90 eindeutig)")
    if len(tu) != 30:
        errs.append(f"LS-10 Tutoren: {len(tu)} (30)")
    learnable |= {r["Ability"] for r in ks} | {r["Ability"] for r in tu}
    missing = [a["DisplayName"] for a in D.act if a["Name"] not in learnable]
    if missing:
        errs.append(f"LS-11 {len(missing)} aktive Fähigkeiten nirgends erlernbar: {', '.join(missing[:12])}")
    used_p = {r["Ability"] for r in po}
    unused = [a["DisplayName"] for a in D.pas if a["Name"] not in used_p]
    if unused:
        errs.append(f"LS-12 {len(unused)} Passive ungenutzt: {', '.join(unused[:12])}")
    return errs


def show(name):
    D = Data()
    ab = {a["Name"]: a for a in rows(ABIL)}
    s = next(x for x in D.sp if x["DisplayName"] == name)
    ls = [r for r in rows(OUT_LS) if r["Species"] == s["Name"]]
    po = [r for r in rows(OUT_PO) if r["Species"] == s["Name"]]
    out = [f"**{name}** ({s['Name']})", "", "| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |", "|---|---|---|---|---|---|"]
    for r in ls:
        a = ab[r["Ability"]]
        lvl = r["Level"] if r["Method"] == "Level" else "–"
        out.append(f"| {r['Method']} | {lvl} | {a['DisplayName']} | {a['Type']} | {a['Category']} | {a['TimeCost']} |")
    out.append("")
    out.append("Passiv: " + ", ".join(ab[r["Ability"]]["DisplayName"] + (" (versteckt)" if r["Hidden"] == "1" else "") for r in po))
    return "\n".join(out)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "build":
        build()
    elif cmd == "validate":
        e = validate()
        for x in e:
            print("FEHLER:", x)
        print(f"Lernsets: {len(e)} Verstöße.")
        sys.exit(1 if e else 0)
    elif cmd == "show":
        print(show(sys.argv[2]))
