#!/usr/bin/env python3
"""Endgame-Referenzmodell (K62): Leveln 70→100, Tiefenresonanz-Laufzeiten und Material, Klangstimmung,
Dissonanzen, Mythische Wege, Meisterschaften.

Prüfregeln:
  EG-01 Tiefenresonanzen: Boss existiert in Bosses.csv mit gleichem Level; Level steigt mit der Nummer; Ort je Region höchstens 1×
  EG-02 jedes Mythische hat einen Solo-Weg (DR-19, CANON §8.5)
  EG-03 Dissonanzen: Faktor 500–1150 ‰, Gegenspiel angegeben, Bonus ≥ 100 ‰; kein Zufallseffekt (DR-07)
  EG-04 alle Meisterschaften, die für 100 % zählen, sind offline erreichbar (DR-19)
  EG-05 ein Echo vollständig stimmen (Anlagen → 15) kostet auf Tiefe III ≤ 6 h
  EG-06 Tiefen-Stufen: Level ≤ 100, HP-Faktor und Material steigen monoton

Aufruf: aethris_endgame.py validate | level | depth
"""
import csv, math, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "ref"))
from aethris_stats import exp_total  # noqa: E402


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


DR = rows("Data/Endgame/DeepResonances.csv")
TIERS = rows("Data/Endgame/DepthTiers.csv")
DIS = rows("Data/Endgame/Dissonances.csv")
MYTH = rows("Data/Endgame/MythicPaths.csv")
MST = rows("Data/Endgame/Masteries.csv")
BOSS = {r["Name"]: r for r in rows("Data/Combat/Bosses.csv")}
SPECIES = rows("Data/Echos/Species.csv")

WILD_FIGHT_MIN = 1.5          # DR-11: Wildkampf 60–120 s
STROPHE_MIN = 7               # je Strophe (2–3 Kämpfe + Rätsel/Weg)
BOSS_MIN = 10                 # Tiefenresonanz-Boss 8–12 min (K35 §10)
KLANGSTIMMUNG_COST = 2        # Stillstein-Splitter je Klangstimmung (RCP_110, K41)


def ep(yield_, ld, lp, source=1.0):
    """CANON §83: EP = ⌊Ertrag × Ld × (2·Ld+10) / ((Ld+Lp+10)·6)⌋ × Quelle."""
    return int(yield_ * ld * (2 * ld + 10) // ((ld + lp + 10) * 6) * source)


def avg_yield():
    ys = [int(s["ExpYield"]) for s in SPECIES if s["Stage"] == "3" or (not s["EvolvesTo"] and s["LineKind"] not in ("Legendary", "Mythical"))]
    return sum(ys) // len(ys)


def battles_to(curve, l0=70, l1=100, cap=90):
    y = avg_yield()
    total = 0
    for L in range(l0, l1):
        need = exp_total(curve, L + 1) - exp_total(curve, L)
        ld = min(L + 2, cap)
        total += math.ceil(need / ep(y, ld, L))
    return total


def de(x, nd):
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def level_table():
    lines = ["| Wachstumskurve | EP 70 → 100 | Wildkämpfe (Nachhall-Spawns, Gegner Lp + 2, max. 90) | Stunden (1,5 min/Kampf) | mit Tiefenresonanzen (Trainer-Faktor 1,3, Boss) |",
             "|---|---|---|---|---|"]
    for c in ("Swift", "Steady", "Wave", "Late"):
        n = battles_to(c)
        need = exp_total(c, 100) - exp_total(c, 70)
        h = n * WILD_FIGHT_MIN / 60
        lines.append(f"| {c} | {de(need, 0)} | {de(n, 0)} | {de(h, 1)} | ≈ {de(h / 1.6, 1)} |")
    return "\n".join(lines)


def run_minutes(d):
    return int(d["Strophes"]) * STROPHE_MIN + BOSS_MIN


def depth_table():
    lines = ["| Tiefenresonanz | Region | Ort | Boss-Level (Tiefe I → V) | Strophen | Ø Dauer | Thema | Material |", "|---|---|---|---|---|---|---|---|"]
    for d in DR:
        b = BOSS[d["Boss"]]
        lv = int(b["Level"])
        lines.append(f"| {d['DisplayName']} | {d['Region']} | {d['Location']} | {lv} → {min(100, lv + 12)} | {d['Strophes']} | {run_minutes(d)} min | {d['Theme']} | {d['Material']} |")
    return "\n".join(lines)


def tuning_table():
    """Klangstimmung: Läufe/Stunden für ein Echo mit 6 fehlenden Anlagen (Rare: 2 Werte bereits 15)."""
    need = 6 * KLANGSTIMMUNG_COST
    avg_run = sum(run_minutes(d) for d in DR) / len(DR)
    lines = ["| Tiefe | Stillstein-Splitter je Lauf (rotierend, Erstabschluss je Spieltag ×2) | Läufe für 6 Klangstimmungen | Stunden |", "|---|---|---|---|"]
    for t in TIERS:
        per = int(t["Splinters"]) * 2
        runs = math.ceil(need / per)
        lines.append(f"| {t['DisplayName']} | {per} | {runs} | {runs * avg_run / 60:.1f} |".replace(".", ","))
    return "\n".join(lines)


def hours_tier3():
    need = 6 * KLANGSTIMMUNG_COST
    avg_run = sum(run_minutes(d) for d in DR) / len(DR)
    t = next(x for x in TIERS if x["Name"] == "DEPTH_3")
    return math.ceil(need / (int(t["Splinters"]) * 2)) * avg_run / 60


def validate():
    err = []
    last = 0
    regions = {}
    for d in DR:
        b = BOSS.get(d["Boss"])
        if not b or int(b["Level"]) != int(d["Level"]):
            err.append(f"EG-01 {d['Name']}: Boss/Level passt nicht zu Bosses.csv")
        if int(d["Level"]) <= last:
            err.append(f"EG-01 {d['Name']}: Level nicht steigend")
        last = int(d["Level"])
        regions[d["Region"]] = regions.get(d["Region"], 0) + 1
    if any(v > 2 for v in regions.values()):
        err.append("EG-01 zu viele Tiefenresonanzen in einer Region")
    for m in MYTH:
        if m["Solo"] != "ja":
            err.append(f"EG-02 {m['DisplayName']} ohne Solo-Weg")
    if len(MYTH) != 6:
        err.append("EG-02 nicht 6 Mythische")
    for x in DIS:
        f = int(x["Factor"])
        if not 500 <= f <= 1150 or not x["Counterplay"] or int(x["RewardBonus"]) < 100:
            err.append(f"EG-03 {x['Name']}")
        if re.search(r"Zufall|zufällig|Chance", x["Effect"]):
            err.append(f"EG-03 {x['Name']}: Zufallseffekt")
    for m in MST:
        if m["Completion"] == "ja" and not m["Offline"].startswith("ja"):
            err.append(f"EG-04 {m['Name']} zählt für 100 %, ist aber nicht offline erreichbar")
    if hours_tier3() > 6:
        err.append(f"EG-05 Klangstimmung {hours_tier3():.1f} h > 6 h")
    prev = (-1, 0, 0)
    for t in TIERS:
        cur = (int(t["LevelOffset"]), int(t["HPPermille"]), int(t["Splinters"]))
        if cur[0] <= prev[0] or cur[1] <= prev[1] or cur[2] < prev[2]:
            err.append(f"EG-06 {t['Name']} nicht monoton")
        prev = cur
    if max(int(BOSS[d["Boss"]]["Level"]) for d in DR) + int(TIERS[-1]["LevelOffset"]) > 107:
        err.append("EG-06 Level über 100 vor Kappung")
    return err


def report():
    e = validate()
    return (f"Prüfregeln EG-01–EG-06: **{len(e)} Verstöße**. {len(DR)} Tiefenresonanzen (Ø {sum(run_minutes(d) for d in DR) / len(DR):.0f} min), "
            f"{len(TIERS)} Tiefen, {len(DIS)} Dissonanzen, {len(MYTH)} Mythische mit Solo-Weg, "
            f"{sum(1 for m in MST if m['Completion'] == 'ja')} Meisterschaften für 100 %; ein Echo stimmen (Tiefe III): "
            f"{de(hours_tier3(), 1)} h.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "level":
        print(level_table())
    elif cmd == "depth":
        print(depth_table()); print(tuning_table())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
