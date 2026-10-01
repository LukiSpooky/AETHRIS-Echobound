#!/usr/bin/env python3
"""PvP-/Ranked-Referenzmodell (K61): Level-Normalisierung (Q5), Glicko-2-Wertung, Matchmaking-Simulation,
sichtbare Klangstufen, Ranked-Zulässigkeit.

Prüfregeln:
  PV-01 Ranked-Zulässigkeit: Ursprungsstimmen und Mythische ausgeschlossen, alle anderen 240 Arten zulässig
  PV-02 Normalisierung: Werte auf NormLevel = Formel K18 (CANON §79) mit echten Anlagen/Schliff
  PV-03 Stufen-Grenzen steigend; höchste Stufe ≤ 2 % der simulierten Spielenden
  PV-04 Wertung konvergiert: Spearman(echte Stärke, Wertung) ≥ 0,90 nach 40 Kämpfen je Person
  PV-05 Regelsätze: Ranked hat NormLevel, Zeitlimit ≤ 20 min (DR-11), Klar-Wetter, keine Verbrauchsgüter
  PV-06 Belohnungen nur kosmetisch (DR-20)

Aufruf: aethris_pvp.py validate | normalize | sim
"""
import csv, math, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "ref"))
from aethris_random import AethrisRandom  # noqa: E402
from aethris_stats import hp, core, secondary  # noqa: E402


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


SPECIES = rows("Data/Echos/Species.csv")
RULES = {r["Name"]: r for r in rows("Data/PvP/Rulesets.csv")}
TIERS = rows("Data/PvP/RankTiers.csv")
NORM = int(RULES["RS_RANKED_TRIO"]["NormLevel"])


def ranked_eligible(s):
    return s["LineKind"] not in ("Legendary", "Mythical")


# ---------------- Normalisierung (Q5) ----------------
def stats_at(s, L, A=10, S=0):
    b = {k: int(s[k]) for k in ("HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed", "Precision", "Evasion")}
    return {"HP": hp(b["HP"], L, A, S), "ATK": core(b["Attack"], L, A, S), "DEF": core(b["Defense"], L, A, S),
            "SPA": core(b["SpAttack"], L, A, S), "SPD": core(b["SpDefense"], L, A, S), "GES": core(b["Speed"], L, A, S),
            "PRÄ": secondary(b["Precision"], A), "AUS": secondary(b["Evasion"], A)}


def normalize_table():
    pick = [s for s in SPECIES if s["Stage"] == "3"][::9][:6]
    lines = ["| Art | Level (echt) | HP | Angriff | Spez.-Angr. | Geschw. | → Norm 70: HP | Angriff | Spez.-Angr. | Geschw. |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, s in enumerate(pick):
        L = (52, 61, 70, 78, 88, 100)[i]
        a, n = stats_at(s, L), stats_at(s, NORM)
        lines.append(f"| {s['DisplayName']} | {L} | {a['HP']} | {a['ATK']} | {a['SPA']} | {a['GES']} | {n['HP']} | {n['ATK']} | {n['SPA']} | {n['GES']} |")
    return "\n".join(lines)


def investment_table():
    """Wirkung von Anlagen und Schliff bei Norm 70 (Beispiel Kernwert Basis 100)."""
    lines = ["| Anlage | Schliff | Kernwert (Basis 100, Norm 70) | Δ ggü. Anlage 0 / Schliff 0 |", "|---|---|---|---|"]
    base = core(100, NORM, 0, 0)
    for A, S in ((0, 0), (7, 0), (15, 0), (0, 80), (15, 80)):
        v = core(100, NORM, A, S)
        lines.append(f"| {A} | {S} | {v} | +{100 * (v - base) / base:.1f} % |".replace(".", ","))
    return "\n".join(lines)


def evo_table():
    """Evolutionsbedingungen mit Level-Schwelle: Anteil ≤ Normstufe."""
    import re
    lv = [int(m.group(1)) for x in SPECIES for m in [re.search(r"Level>=(\d+)", x["EvoCondition"])] if m]
    other = sum(1 for x in SPECIES if x["EvoCondition"] and not re.search(r"Level>=", x["EvoCondition"]))
    bands = [(1, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 100)]
    lines = ["| Evolutions-Levelschwelle | Anzahl Evolutionen |", "|---|---|"]
    for a, b in bands:
        lines.append(f"| {a}–{b} | {sum(1 for v in lv if a <= v <= b)} |")
    lines.append(f"| ohne Levelschwelle (Bindung, Item, Ort, Zeit …) | {other} |")
    lines.append(f"| **höchste Schwelle** | **{max(lv)}** |")
    return "\n".join(lines)


TYPE_DE = {"Ember": "Glut", "Tide": "Flut", "Stone": "Stein", "Storm": "Sturm", "Bloom": "Blüte", "Frost": "Frost", "Void": "Leere",
           "Light": "Licht", "Venom": "Gift", "Metal": "Metall", "Spirit": "Geist", "Crystal": "Kristall", "Sound": "Klang",
           "Gravity": "Schwerkraft", "Arcane": "Arkan"}


def type_pool_table():
    """Ranked-Pool je Primärtyp: Arten (alle Stufen), davon Endformen, Ø Kernsumme der Endformen."""
    ends = {x["Name"] for x in SPECIES if not x["EvolvesTo"]}
    lines = ["| Primärtyp | zulässige Arten | davon Endformen | Ø Kernsumme Endformen |", "|---|---|---|---|"]
    by = {}
    for x in SPECIES:
        if ranked_eligible(x):
            by.setdefault(x["PrimaryType"].split(".")[-1], []).append(x)
    for t, xs in sorted(by.items(), key=lambda kv: -len(kv[1])):
        e = [x for x in xs if x["Name"] in ends]
        cs = [sum(int(x[k]) for k in ("HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed")) for x in e]
        lines.append(f"| {TYPE_DE.get(t, t)} | {len(xs)} | {len(e)} | {sum(cs) // max(1, len(cs))} |")
    return "\n".join(lines)


# ---------------- Glicko-2 ----------------
SCALE = 173.7178
TAU = 0.5


def g(phi):
    return 1 / math.sqrt(1 + 3 * phi * phi / math.pi ** 2)


def glicko2_update(r, rd, sigma, r_opp, rd_opp, score):
    """Ein Kampf als Bewertungsperiode (Glickman 2012). Rückgabe (r, rd, sigma)."""
    mu, phi = (r - 1500) / SCALE, rd / SCALE
    mu_j, phi_j = (r_opp - 1500) / SCALE, rd_opp / SCALE
    gj = g(phi_j)
    E = 1 / (1 + math.exp(-gj * (mu - mu_j)))
    v = 1 / (gj * gj * E * (1 - E))
    delta = v * gj * (score - E)
    a = math.log(sigma * sigma)

    def f(x):
        ex = math.exp(x)
        return ex * (delta * delta - phi * phi - v - ex) / (2 * (phi * phi + v + ex) ** 2) - (x - a) / TAU ** 2

    A = a
    if delta * delta > phi * phi + v:
        B = math.log(delta * delta - phi * phi - v)
    else:
        k = 1
        while f(a - k * TAU) < 0:
            k += 1
        B = a - k * TAU
    fA, fB = f(A), f(B)
    while abs(B - A) > 1e-6:
        C = A + (A - B) * fA / (fB - fA)
        fC = f(C)
        if fC * fB <= 0:
            A, fA = B, fB
        else:
            fA /= 2
        B, fB = C, fC
    sigma2 = math.exp(A / 2)
    phi_star = math.sqrt(phi * phi + sigma2 * sigma2)
    phi2 = 1 / math.sqrt(1 / phi_star ** 2 + 1 / v)
    mu2 = mu + phi2 * phi2 * gj * (score - E)
    return mu2 * SCALE + 1500, phi2 * SCALE, sigma2


def tier_of(cons):
    t = TIERS[0]
    for x in TIERS:
        if cons >= int(x["MinConservative"]):
            t = x
    return t


def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0] * len(v)
        for k, i in enumerate(order):
            r[i] = k
        return r
    rx, ry = rank(xs), rank(ys)
    n = len(xs)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))


def simulate(n_players=2000, matches_each=60, seed=61):
    rng = AethrisRandom(seed, 0x61)

    def gauss():
        return sum(rng.next_bounded(10000) for _ in range(12)) / 10000 - 6   # ≈ N(0,1)

    true = [1500 + 300 * gauss() for _ in range(n_players)]
    r = [1500.0] * n_players
    rd = [350.0] * n_players
    sg = [0.06] * n_players
    played = [0] * n_players
    checkpoints = {5: None, 10: None, 20: None, 40: None, 60: None}
    total = n_players * matches_each // 2
    for m in range(total):
        a = rng.next_bounded(n_players)
        cand = [rng.next_bounded(n_players) for _ in range(24)]
        b = min((c for c in cand if c != a), key=lambda c: abs(r[c] - r[a]))
        p = 1 / (1 + 10 ** (-(true[a] - true[b]) / 400))
        s = 1.0 if rng.next_bounded(1_000_000) < p * 1_000_000 else 0.0
        ra, rda, sa = glicko2_update(r[a], rd[a], sg[a], r[b], rd[b], s)
        rb, rdb, sb = glicko2_update(r[b], rd[b], sg[b], r[a], rd[a], 1 - s)
        r[a], rd[a], sg[a], r[b], rd[b], sg[b] = ra, rda, sa, rb, rdb, sb
        played[a] += 1
        played[b] += 1
        avg = 2 * (m + 1) / n_players
        for c in checkpoints:
            if checkpoints[c] is None and avg >= c:
                checkpoints[c] = (spearman(true, r), sum(rd) / n_players)
    cons = [r[i] - 2 * rd[i] for i in range(n_players)]
    dist = {}
    for c in cons:
        t = tier_of(c)["DisplayName"]
        dist[t] = dist.get(t, 0) + 1
    return checkpoints, dist, n_players


_SIM = None


def sim():
    global _SIM
    if _SIM is None:
        _SIM = simulate()
    return _SIM


def sim_table():
    cp, dist, n = sim()
    lines = ["| Kämpfe je Person (Ø) | Spearman (echte Stärke ↔ Wertung) | Ø RD |", "|---|---|---|"]
    for k, (sp, rdm) in cp.items():
        lines.append(f"| {k} | {sp:.3f} | {rdm:.0f} |".replace(".", ","))
    lines += ["", "| Klangstufe | Grenze (R − 2·RD) | Anteil nach 60 Kämpfen |", "|---|---|---|"]
    for t in TIERS:
        c = dist.get(t["DisplayName"], 0)
        lines.append(f"| {t['DisplayName']} | {t['MinConservative']} | {100 * c / n:.1f} % |".replace(".", ","))
    return "\n".join(lines)


def validate():
    err = []
    elig = sum(ranked_eligible(s) for s in SPECIES)
    if elig != 240:
        err.append(f"PV-01 {elig} zulässige Arten (erwartet 240)")
    s0 = SPECIES[0]
    n = stats_at(s0, NORM, 15, 20)
    if n["HP"] != hp(int(s0["HP"]), NORM, 15, 20):
        err.append("PV-02 Normalisierung weicht von K18 ab")
    th = [int(t["MinConservative"]) for t in TIERS]
    if th != sorted(th) or len(set(th)) != len(th):
        err.append("PV-03 Stufengrenzen nicht steigend")
    cp, dist, nn = sim()
    top = dist.get(TIERS[-1]["DisplayName"], 0) / nn
    if top > 0.02:
        err.append(f"PV-03 höchste Stufe {100 * top:.1f} % > 2 %")
    if cp[40][0] < 0.90:
        err.append(f"PV-04 Spearman nach 40 Kämpfen {cp[40][0]:.3f} < 0,90")
    for k, rs in RULES.items():
        if k.startswith("RS_RANKED"):
            if rs["Level"] != "Norm" or int(rs["MatchLimitMin"]) > 20 or not rs["Weather"].startswith("Klar") or "keine Verbrauchsgüter" not in rs["Items"]:
                err.append(f"PV-05 {k} verletzt Ranked-Grundregeln")
    for t in TIERS:
        if any(x in t["Reward"] for x in ("Echo", "Sol", "%", "Siegel")):
            err.append(f"PV-06 {t['Name']}: Belohnung nicht kosmetisch")
    return err


def report():
    e = validate()
    cp, dist, n = sim()
    de = lambda x, d: f"{x:.{d}f}".replace(".", ",")
    top = 100 * dist.get(TIERS[-1]["DisplayName"], 0) / n
    return (f"Prüfregeln PV-01–PV-06: **{len(e)} Verstöße**. Ranked-zulässig: {sum(ranked_eligible(s) for s in SPECIES)} Arten; "
            f"Normstufe {NORM}; Simulation {n} Personen × 60 Kämpfe: Spearman nach 40 Kämpfen {de(cp[40][0], 3)}, "
            f"höchste Stufe {de(top, 1)} %.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "normalize":
        print(normalize_table()); print(investment_table())
    elif cmd == "sim":
        print(sim_table())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
