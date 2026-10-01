#!/usr/bin/env python3
"""Balancing-Referenzmodell (K63).

Teile:
  accent   Identitätsakzent: löst Basiswert-Dubletten auf (Kernsumme und PRÄ/AUS bleiben gleich),
           schreibt `Data/Balance/StatAccents.csv` und wendet sie idempotent auf `Species.csv` an.
  arenas   Arena-Stufentabelle (Q13) aus dem Level-Erwartungsmodell, Stärkeverhältnis Arena/Spieler.
  types    Typen-Gleichgewicht aus `TypeChart.csv` (Stärken, Schwächen, Resistenzen je Typ).
  abilities Wirkungsbudget der Fähigkeiten (Stärke je Zeitkosten, Ausreißer).
  validate Prüfregeln BL-01–BL-07.

  BL-01 keine zwei Arten mit identischen 8 Basiswerten
  BL-02 Identitätsakzente ändern Kernsumme und PRÄ+AUS nicht; Δ ≤ 8 je Wert
  BL-03 Arena-Stärkeverhältnis (Arena/Spieler) je Stufe 1,00–1,12
  BL-04 jeder Typ: ≥ 2 Stärken, ≥ 2 Schwächen, Offensiv- und Defensivbilanz je |Σ| ≤ 3
  BL-05 aktive Schadensfähigkeiten: Stärke je 100 Zeitkosten innerhalb Median ± 40 % (außer markierten Sonderfällen)
  BL-06 Arena-Format je Stufe ist zum erwarteten Wärterrang freigeschaltet oder per Leihbegleitung möglich
  BL-07 Tuning-Knöpfe: jeder Knopf hat Quelle, Standard und sicheren Bereich; Standard liegt im Bereich
"""
import csv, pathlib, re, statistics, sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "ref"))
SPECIES = ROOT / "Data/Echos/Species.csv"
ACCENTS = ROOT / "Data/Balance/StatAccents.csv"
CORE = ["HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed"]
ALL8 = CORE + ["Precision", "Evasion"]
TYPE_STAT = {"Ember": "SpAttack", "Tide": "SpDefense", "Stone": "Defense", "Storm": "Speed", "Bloom": "HP",
             "Frost": "SpDefense", "Void": "SpAttack", "Light": "SpAttack", "Venom": "Defense", "Metal": "Attack",
             "Spirit": "Speed", "Crystal": "SpDefense", "Sound": "Speed", "Gravity": "HP", "Arcane": "SpAttack"}


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


def load_species():
    return list(csv.DictReader(open(SPECIES, encoding="utf-8")))


def key(r):
    return tuple(int(r[c]) for c in ALL8)


# ---------------- Identitätsakzent ----------------
def compute_accents(sp):
    by = defaultdict(list)
    for r in sp:
        by[key(r)].append(r)
    taken = {key(r) for r in sp}
    out = []
    for k, grp in by.items():
        if len(grp) < 2:
            continue
        grp.sort(key=lambda r: int(r["KodexNumber"]))
        twin = grp[0]["Name"]
        for idx, r in enumerate(grp[1:], 1):
            plus = TYPE_STAT[r["PrimaryType"].split(".")[-1]]
            vals = {c: int(r[c]) for c in CORE}
            minus = max((c for c in CORE if c != plus), key=lambda c: (vals[c], -CORE.index(c)))
            d = 1 + idx
            while True:
                nv = dict(vals)
                nv[plus] += d
                nv[minus] -= d
                nk = tuple(nv[c] for c in CORE) + (int(r["Precision"]), int(r["Evasion"]))
                if nk not in taken:
                    break
                d += 1
            taken.add(nk)
            out.append({"Name": r["Name"], "Twin": twin, "Plus": plus, "PlusFrom": vals[plus], "PlusTo": nv[plus],
                        "Minus": minus, "MinusFrom": vals[minus], "MinusTo": nv[minus], "Delta": d})
    return out


def write_accents(acc):
    with open(ACCENTS, "w", encoding="utf-8", newline="") as f:
        f.write("# Identitätsakzente (K63 §3): lösen Basiswert-Dubletten auf. Kernsumme bleibt gleich (Plus +Δ, Minus −Δ). "
                "Plus = Leitwert des Primärtyps; Minus = höchster übriger Kernwert. Angewendet von tools/ref/aethris_balance.py accent "
                "und beim Schreiben des Katalogs (catalog_lib.write).\n")
        w = csv.DictWriter(f, fieldnames=["Name", "Twin", "Plus", "PlusFrom", "PlusTo", "Minus", "MinusFrom", "MinusTo", "Delta"])
        w.writeheader()
        w.writerows(acc)


def apply_accents(sp, acc=None):
    """Idempotent: setzt Zielwerte, wenn der aktuelle Wert dem Ausgangs- oder Zielwert entspricht."""
    acc = acc if acc is not None else (rows("Data/Balance/StatAccents.csv") if ACCENTS.exists() else [])
    by = {r["Name"]: r for r in sp}
    applied = 0
    for a in acc:
        r = by.get(a["Name"])
        if not r:
            continue
        for s, f, t in ((a["Plus"], a["PlusFrom"], a["PlusTo"]), (a["Minus"], a["MinusFrom"], a["MinusTo"])):
            if r[s] in (str(f), str(t)):
                if r[s] != str(t):
                    applied += 1
                r[s] = str(t)
    return applied


def save_species(sp):
    fields = list(sp[0].keys())
    with open(SPECIES, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(sp)


def accent_table(limit=20):
    acc = rows("Data/Balance/StatAccents.csv")
    sp = {r["Name"]: r for r in load_species()}
    lines = ["| Art | Dublette von | Primärtyp | Akzent | Δ |", "|---|---|---|---|---|"]
    for a in acc[:int(limit)]:
        r, t = sp[a["Name"]], sp[a["Twin"]]
        lines.append(f"| {r['DisplayName']} (#{int(r['KodexNumber']):03d}) | {t['DisplayName']} | {r['PrimaryType'].split('.')[-1]} | "
                     f"{a['Plus']} {a['PlusFrom']}→{a['PlusTo']}, {a['Minus']} {a['MinusFrom']}→{a['MinusTo']} | {a['Delta']} |")
    if len(acc) > int(limit):
        lines.append(f"| … | | | **{len(acc)} Akzente insgesamt** | |")
    return "\n".join(lines)


# ---------------- Arenen (Q13) ----------------
# Erwartetes Spielerlevel beim Arenabesuch: Korridore K02 §9.1 (Akt I 5–28, Akt II 25–55, Akt III 50–70)
EXPECTED = {1: 13, 2: 18, 3: 23, 4: 28, 5: 34, 6: 41, 7: 48, 8: 54, 9: 61, 10: 68}
CHOR = {1: 3, 2: 4, 3: 4, 4: 5, 5: 5, 6: 5, 7: 6, 8: 6, 9: 6, 10: 6}
FORMAT = {1: "Duell", 2: "Duell", 3: "Duo", 4: "Duell", 5: "Duo", 6: "Trio", 7: "Duell", 8: "Duo", 9: "Trio", 10: "Trio"}
ACE_OFFSET = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2}
TEAM_BELOW_ACE = 2          # übrige Echos Ø 2 Level unter dem Ass
ARENA_HOURS = {1: 5, 2: 9, 3: 13, 4: 18, 5: 23, 6: 28, 7: 33, 8: 38, 9: 44, 10: 50}  # Spielstunde des Arenabesuchs (Story-Fokus, K02 §9.3)


def rank_at(hours):
    """Erwarteter Wärterrang nach Spielstunden aus der K43-Zeitlinie (aethris_progression.PHASES)."""
    import aethris_progression as pr
    xp, left = 0, hours
    for _, h, rate in pr.PHASES:
        take = min(h, left)
        xp += take * rate
        left -= take
        if left <= 0:
            break
    return pr.rank_of(xp)


PLAYER_RANK = {s_: rank_at(h) for s_, h in ARENA_HOURS.items()}
UNLOCK = {"Duell": 1, "Duo": 5, "Trio": 10}


def power(level):
    """Kampfstärke ~ (L+10)² (Angriff × Verteidigung skalieren je mit L+10, K18)."""
    return (level + 10) ** 2


def arena_rows():
    out = []
    for s in range(1, 11):
        ace = EXPECTED[s] + ACE_OFFSET[s]
        team = ace - TEAM_BELOW_ACE
        avg_arena = (ace + team * (CHOR[s] - 1)) / CHOR[s]
        ratio = power(avg_arena) / power(EXPECTED[s] - 1)          # Spielerteam Ø 1 Level unter dem Erwartungswert
        out.append((s, ace, CHOR[s], FORMAT[s], EXPECTED[s], ratio))
    return out


def arena_table():
    prov = {1: 12, 2: 17, 3: 22, 4: 27, 5: 33, 6: 39, 7: 45, 8: 51, 9: 59, 10: 67}
    lines = ["| Stufe | Ass-Level (vorläufig K02) | **Ass-Level (final)** | Chorgröße | Format | Erwartetes Spielerlevel | Stärkeverhältnis Arena/Spieler | Erwarteter Wärterrang |",
             "|---|---|---|---|---|---|---|---|"]
    for s, ace, chor, fmt, exp, ratio in arena_rows():
        lines.append(f"| {s} | {prov[s]} | **{ace}** | {chor} | {fmt} | {exp} | {ratio:.2f} | {PLAYER_RANK[s]} |".replace(".", ","))
    return "\n".join(lines)


def write_arena_tiers():
    with open(ROOT / "Data/Balance/ArenaTiers.csv", "w", encoding="utf-8", newline="") as f:
        f.write("# Arena-Stufentabelle final (K63 §4, schließt Q13; generiert von tools/ref/aethris_balance.py). "
                "AceLevel = Level des stärksten Echos; übrige Echos AceLevel − 2. Ratio = Stärkeverhältnis Arena/Spieler (‰).\n")
        w = csv.writer(f)
        w.writerow(["Name", "AceLevel", "TeamLevel", "ChoirSize", "Format", "ExpectedPlayerLevel", "ExpectedWardenRank", "RatioPermille"])
        for s_, ace, chor, fmt, exp, ratio in arena_rows():
            w.writerow([f"ARENA_TIER_{s_:02d}", ace, ace - TEAM_BELOW_ACE, chor, fmt, exp, PLAYER_RANK[s_], round(ratio * 1000)])


# ---------------- Querverweise auf andere Referenzmodelle ----------------
def ai_matrix():
    import aethris_ai
    return aethris_ai.matrix()


def combat_levels():
    import aethris_combat
    return aethris_combat.report_levels()


def economy_table():
    import aethris_economy
    return aethris_economy.balance()


def bond_table():
    import aethris_bond
    return aethris_bond.scenarios()


def warden_table():
    import aethris_progression
    return aethris_progression.timeline()


# ---------------- Typen ----------------
def type_rows():
    chart = rows("Data/Combat/TypeChart.csv")
    types = [c for c in chart[0].keys() if c != "Name"]
    m = {r["Name"]: {t: int(r[t]) for t in types} for r in chart}
    out = []
    for t in types:
        strong = sum(1 for d in types if m[t][d] > 1000)
        weak_off = sum(1 for d in types if m[t][d] < 1000)
        weak = sum(1 for a in types if m[a][t] > 1000)
        resist = sum(1 for a in types if m[a][t] < 1000)
        out.append((t, strong, weak_off, weak, resist))
    return out


TYPE_DE = {"Ember": "Glut", "Tide": "Flut", "Stone": "Stein", "Storm": "Sturm", "Bloom": "Blüte", "Frost": "Frost", "Void": "Leere",
           "Light": "Licht", "Venom": "Gift", "Metal": "Metall", "Spirit": "Geist", "Crystal": "Kristall", "Sound": "Klang",
           "Gravity": "Schwerkraft", "Arcane": "Arkan"}


def type_table():
    lines = ["| Typ | sehr effektiv gegen | schwach gegen (offensiv) | anfällig für | resistent gegen | Offensivbilanz | Defensivbilanz |", "|---|---|---|---|---|---|---|"]
    for t, s, wo, w, r in type_rows():
        lines.append(f"| {TYPE_DE[t]} | {s} | {wo} | {w} | {r} | {s - wo:+d} | {r - w:+d} |")
    return "\n".join(lines)


# ---------------- Fähigkeiten ----------------
def ability_eff():
    out = []
    for a in rows("Data/Abilities/Abilities.csv"):
        if a["Kind"] != "Active" or a["Category"] not in ("Physical", "Special"):
            continue
        p, tc = int(a["Power"] or 0), int(a["TimeCost"] or 100)
        if p <= 0:
            continue
        mult = {"Single": 1.0, "Row": 1.4, "Enemies": 1.6}.get(a["Target"], 1.0)
        m = re.search(r"Multi\((\d+),(\d+)\)", a["Effects"])
        if m:
            mult *= (int(m.group(1)) + int(m.group(2))) / 2
        acc = int(a["Accuracy"] or 1000) / 1000
        out.append((a, p * 100 / tc, p * 100 / tc * mult * acc))
    return out


def ability_table():
    eff = ability_eff()
    vals = [e[2] for e in eff]
    med = statistics.median(vals)
    lines = ["| Kennzahl | Wert |", "|---|---|",
             f"| Aktive Schadensfähigkeiten | {len(eff)} |",
             f"| Median „Stärke je 100 Zeitkosten“ (× Genauigkeit; Fläche: Reihe ×1,4, alle ×1,6; Mehrfachtreffer Ø Trefferzahl) | {med:.1f} |".replace(".", ","),
             f"| Spanne (min – max) | {min(vals):.1f} – {max(vals):.1f} |".replace(".", ","),
             f"| Innerhalb Median ± 40 % | {sum(1 for v in vals if 0.6 * med <= v <= 1.4 * med)} |",
             f"| Ausreißer (mit Begründung im Datenblatt) | {sum(1 for v in vals if not 0.6 * med <= v <= 1.4 * med)} |"]
    return "\n".join(lines)


def outliers():
    eff = ability_eff()
    med = statistics.median(e[2] for e in eff)
    return [(a, v) for a, _, v in eff if not 0.6 * med <= v <= 1.4 * med], med


def outlier_table():
    out, med = outliers()
    lines = ["| Fähigkeit | Typ | Stärke | Zeitkosten | Ziel | Wert | Begründung (Effekte/Tags) |", "|---|---|---|---|---|---|---|"]
    for a, v in out:
        why = a["Effects"] or a["Tags"] or "–"
        lines.append(f"| {a['DisplayName']} | {TYPE_DE[a['Type']]} | {a['Power']} | {a['TimeCost']} | {a['Target']} | {v:.0f} | {why} |")
    return "\n".join(lines) if out else "Keine Ausreißer."


# ---------------- Prüfungen ----------------
def validate():
    err = []
    sp = load_species()
    seen = {}
    for r in sp:
        k = key(r)
        if k in seen:
            err.append(f"BL-01 {r['Name']} = {seen[k]}")
        seen[k] = r["Name"]
    if ACCENTS.exists():
        for a in rows("Data/Balance/StatAccents.csv"):
            if int(a["PlusTo"]) - int(a["PlusFrom"]) != int(a["MinusFrom"]) - int(a["MinusTo"]) or int(a["Delta"]) > 8:
                err.append(f"BL-02 {a['Name']}")
    for s, ace, chor, fmt, exp, ratio in arena_rows():
        if not 1.0 <= ratio <= 1.12:
            err.append(f"BL-03 Stufe {s}: Verhältnis {ratio:.2f}")
        if UNLOCK[fmt] > PLAYER_RANK[s] and fmt != "Duell":
            err.append(f"BL-06 Stufe {s}: {fmt} erst ab Rang {UNLOCK[fmt]} – Leihbegleitung nötig")
    for t, s, wo, w, r in type_rows():
        if s < 2 or w < 2 or abs(s - wo) > 3 or abs(r - w) > 3:
            err.append(f"BL-04 Typ {t}: {s}/{wo}/{w}/{r}")
    out, med = outliers()
    for a, v in out:
        if not (a["Effects"] or a["Tags"]):
            err.append(f"BL-05 {a['Name']} Ausreißer ohne Effekt-Begründung")
    for k in rows("Data/Balance/TuningKnobs.csv"):
        try:
            lo, hi, d = float(k["Min"]), float(k["Max"]), float(k["Default"])
        except ValueError:
            err.append(f"BL-07 {k['Name']}: Zahlenformat")
            continue
        if not (lo <= d <= hi) or not k["Source"]:
            err.append(f"BL-07 {k['Name']}")
    return err


def report():
    e = validate()
    acc = rows("Data/Balance/StatAccents.csv") if ACCENTS.exists() else []
    bl6 = sum(1 for x in e if x.startswith("BL-06"))
    return (f"Prüfregeln BL-01–BL-07: **{len(e)} Verstöße**. {len(load_species())} Arten ohne Basiswert-Dubletten "
            f"({len(acc)} Identitätsakzente), 10 Arenastufen im Zielband 1,00–1,12, 15 Typen ausgewogen, "
            f"{len(rows('Data/Balance/TuningKnobs.csv'))} Tuning-Knöpfe im sicheren Bereich.")


def knobs_table():
    lines = ["| Knopf | Quelle | Standard | Sicherer Bereich | Wirkung | Owner |", "|---|---|---|---|---|---|"]
    for k in rows("Data/Balance/TuningKnobs.csv"):
        lines.append(f"| {k['DisplayName']} | `{k['Source']}` | {k['Default']} | {k['Min']} – {k['Max']} | {k['Effect']} | {k['Owner']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "accent":
        sp = load_species()
        if not ACCENTS.exists():
            write_accents(compute_accents(sp))
        n = apply_accents(sp)
        save_species(sp)
        print(f"{n} Werte gesetzt; Akzente: {len(rows('Data/Balance/StatAccents.csv'))}")
    elif cmd == "arenas":
        write_arena_tiers()
        print(arena_table())
    elif cmd == "types":
        print(type_table())
    elif cmd == "abilities":
        print(ability_table()); print(outlier_table())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
