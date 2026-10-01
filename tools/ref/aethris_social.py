#!/usr/bin/env python3
"""Soziales Referenzmodell (K60): Koop-Skalierung, Tauschbarkeit, Solo-Zugang aller Arten (DR-19),
Klangbörse mit Ring-Tausch (2er- und 3er-Kreise), Zirkel und Schnellchat.

Prüfregeln:
  SO-01 jede Art hat einen Solo-Zugang (Wildvorkommen, Evolution, Stimmsiegel-Quest, Mythos-Zugang §34)
  SO-02 nur Ursprungsstimmen und Mythische sind vom Tausch ausgeschlossen
  SO-03 Tauschliste enthält nur Ressourcen, Gerichte, Lockmittel/Futter (keine Schlüssel-/Siegel-/Ausrüstungsgegenstände)
  SO-04 Zirkel: Mitglieder ≤ 50 (+ Gäste), genau eine Leitung
  SO-05 Zirkel-Chronik-Belohnungen nur kosmetisch (keine Werte, Prozente, Echos, Sol)
  SO-06 Schnellchat: 24 eindeutige Sätze, ≤ 40 Zeichen (Lokalisierungsreserve +40 %)
  SO-07 Koop-Belohnungsarten passen zum Gast-Protokoll (K59 §6.4)

Aufruf: aethris_social.py validate | board | coop
"""
import csv, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "ref"))
from aethris_random import AethrisRandom  # noqa: E402


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


SPECIES = rows("Data/Echos/Species.csv")
MYTHIC_SOLO = {  # CANON §34
    "ECHO_251": "Akt-III-Finale → Nachhall", "ECHO_252": "Zeitherausforderungen", "ECHO_253": "Fotografie-Meisterschaft",
    "ECHO_254": "Zucht-Meisterschaft", "ECHO_255": "Solo-Tiefenresonanz DR_08", "ECHO_256": "storygebundener Solo-Sturm",
}
LEDGER_KINDS = {"Item", "Echo", "Experience", "KodexEntry", "Sol", "Reputation", "Memory", "Photo", "–"}


def solo_source(s, evo_targets):
    if s["LineKind"] == "Legendary":
        return "Stimmsiegel-Quest (CANON §34)"
    if s["LineKind"] == "Mythical":
        return MYTHIC_SOLO.get(s["Name"], "")
    if s["Zones"]:
        return "Wildvorkommen"
    if s["Name"] in evo_targets:
        return "Evolution"
    return ""


def tradeable(s):
    return s["LineKind"] not in ("Legendary", "Mythical")


def trade_items():
    res = rows("Data/Items/Resources.csv")
    meals = [r for r in rows("Data/Items/Consumables.csv") if r["Kind"] == "Meal"]
    lures = rows("Data/Items/Lures.csv")
    return {"Ressourcen": res, "Gerichte": meals, "Lockmittel/Futter": lures}


# ---------- Koop-Skalierung ----------
def coop_table():
    lines = ["| Spieler | Kampfformat (Spielerseite) | Wildbegegnung | HP-Faktor Alpha/Wärter/Boss | EP/Sol je Spieler | Zugtimer |",
             "|---|---|---|---|---|---|"]
    fmt = {1: "Solo (Duell/Duo/Trio nach Rang)", 2: "Duo (2 × 1 aktiv)", 3: "Trio (3 × 1 aktiv)", 4: "Quartett (Raid-Formation, 4 × 1 aktiv)"}
    for n in range(1, 5):
        hp = 1 + 0.7 * (n - 1)
        lines.append(f"| {n} | {fmt[n]} | Herde mit {n} Echo{'s' if n > 1 else ''} oder Einzel-Alpha | ×{hp:.1f} | 100 % (eigene Echos) | {'–' if n == 1 else '30 s (Option 60 s)'} |".replace(".", ","))
    return "\n".join(lines)


# ---------- Klangbörse ----------
RARITY_W = {"Common": 10, "Uncommon": 6, "Rare": 3, "VeryRare": 1}


def board_sim(n_offers=600, seed=60, wants=3):
    """Erzeugt Angebote (Echo + Wunschliste mit bis zu `wants` Arten) und sucht Tausch-Kreise.
    Angebote sind häufig nach Seltenheit gewichtet, Wünsche bevorzugen Seltenes. Gierig: erst 2er, dann 3er-Ringe."""
    rng = AethrisRandom(seed, 0x60)
    pool = [s for s in SPECIES if tradeable(s) and s["Rarity"] in RARITY_W]

    def pick(weight):
        tot = sum(weight(s) for s in pool)
        x = rng.next_bounded(tot)
        for s in pool:
            x -= weight(s)
            if x < 0:
                return s["Name"]
        return pool[-1]["Name"]

    offers = []
    for i in range(n_offers):
        have = pick(lambda s: RARITY_W[s["Rarity"]])
        wl = [w for w in dict.fromkeys(pick(lambda s: 11 - RARITY_W[s["Rarity"]]) for _ in range(wants)) if w != have]
        if wl:
            offers.append((i, have, wl))
    by_have = {}
    for o in offers:
        by_have.setdefault(o[1], []).append(o)
    used = set()
    pairs = rings = 0
    for o in offers:                                   # 2er-Kreise
        if o[0] in used:
            continue
        for w in o[2]:
            hit = next((p for p in by_have.get(w, []) if p[0] not in used and p[0] != o[0] and o[1] in p[2]), None)
            if hit:
                used |= {o[0], hit[0]}
                pairs += 1
                break
    matched2 = len(used)
    for o in offers:                                   # 3er-Ringe: o → p → q → o
        if o[0] in used:
            continue
        found = None
        for w in o[2]:
            for p in by_have.get(w, []):
                if p[0] in used or p[0] == o[0]:
                    continue
                for w2 in p[2]:
                    q = next((q for q in by_have.get(w2, []) if q[0] not in used and q[0] not in (o[0], p[0]) and o[1] in q[2]), None)
                    if q:
                        found = (p, q)
                        break
                if found:
                    break
            if found:
                break
        if found:
            used |= {o[0], found[0][0], found[1][0]}
            rings += 1
    return len(offers), pairs, matched2, rings, len(used)


def board_table():
    lines = ["| Angebote | 2er-Tausche | erfüllt (nur 2er) | + 3er-Ringe | erfüllt (2er + 3er) |", "|---|---|---|---|---|"]
    for n in (1000, 5000, 20000):
        tot, pairs, m2, rings, m3 = board_sim(n)
        lines.append(f"| {tot} | {pairs} | {m2} ({100 * m2 / tot:.0f} %) | {rings} | {m3} ({100 * m3 / tot:.0f} %) |")
    return "\n".join(lines)


# ---------- Prüfungen ----------
def validate():
    err = []
    evo = {t for s in SPECIES for t in s["EvolvesTo"].split("|") if t}
    for s in SPECIES:
        if not solo_source(s, evo):
            err.append(f"SO-01 {s['Name']} ohne Solo-Zugang")
        if not tradeable(s) and s["LineKind"] not in ("Legendary", "Mythical"):
            err.append(f"SO-02 {s['Name']} unzulässig gesperrt")
    keys = {r["Name"] for r in rows("Data/Items/KeyItems.csv")} | {r["Name"] for r in rows("Data/Items/Seals.csv")}
    for grp, items in trade_items().items():
        for it in items:
            if it["Name"] in keys:
                err.append(f"SO-03 {it['Name']} ({grp}) ist Schlüssel/Siegel")
    roles = {r["Name"]: int(r["Max"]) for r in rows("Data/Online/GuildRoles.csv")}
    if roles.get("ROLE_LEAD") != 1 or roles["ROLE_LEAD"] + roles["ROLE_VOICE"] + roles["ROLE_MEMBER"] > 50:
        err.append("SO-04 Zirkelgröße/Leitung")
    for g in rows("Data/Online/GuildGoals.csv"):
        if any(x in g["Reward"] for x in ("%", "Echo ", "Sol", "Wert", "EP")):
            err.append(f"SO-05 {g['Name']}: Belohnung nicht kosmetisch")
    qc = rows("Data/Online/QuickChat.csv")
    if len(qc) != 24 or len({q["Text"] for q in qc}) != 24:
        err.append("SO-06 Schnellchat-Anzahl/Eindeutigkeit")
    for q in qc:
        if len(q["Text"]) > 40:
            err.append(f"SO-06 {q['Name']} zu lang")
    for c in rows("Data/Online/CoopRewards.csv"):
        for k in c["Ledger"].split("|"):
            if k not in LEDGER_KINDS:
                err.append(f"SO-07 {c['Name']}: Protokollart {k}")
    return err


def report():
    e = validate()
    evo = {t for s in SPECIES for t in s["EvolvesTo"].split("|") if t}
    src = {}
    for s in SPECIES:
        k = solo_source(s, evo)
        k = "Mythos-Zugang (§34)" if s["LineKind"] == "Mythical" else k
        src[k] = src.get(k, 0) + 1
    ti = trade_items()
    return (f"Prüfregeln SO-01–SO-07: **{len(e)} Verstöße**. Solo-Zugang aller {len(SPECIES)} Arten: "
            + ", ".join(f"{k} {v}" for k, v in sorted(src.items(), key=lambda x: -x[1]))
            + f". Tauschbar: {sum(tradeable(s) for s in SPECIES)} Arten; Tauschliste: "
            + ", ".join(f"{k} {len(v)}" for k, v in ti.items()) + f" = {sum(len(v) for v in ti.values())} Gegenstände.")


def trade_items_table():
    lines = ["| Gruppe | Anzahl | Gegenstände |", "|---|---|---|"]
    for grp, items in trade_items().items():
        lines.append(f"| {grp} | {len(items)} | " + ", ".join(i["DisplayName"] for i in items) + " |")
    return "\n".join(lines)


def quickchat_table():
    lines = ["| ID | Gruppe | Satz |", "|---|---|---|"]
    for q in rows("Data/Online/QuickChat.csv"):
        lines.append(f"| {q['Name']} | {q['Group']} | „{q['Text']}“ |")
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "board":
        print(board_table())
    elif cmd == "coop":
        print(coop_table())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
