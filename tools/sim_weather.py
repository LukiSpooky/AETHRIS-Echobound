#!/usr/bin/env python3
"""Kalibriert und simuliert den Wetterplaner aus K14 und prüft, dass die langfristigen Zeitanteile je Region
den Zielgewichten aus Data/World/RegionWeather.csv entsprechen (Toleranz ±3 Prozentpunkte).

Planer-Regel (identisch zu UWeatherScheduler, K14 §4):
  Nächstes Wetter ~ Gewicht(w) / mittlereDauer(w), nur Zustände, deren TimeGate zur Startstunde passt,
  gleicher Zustand zweimal hintereinander nicht erlaubt (außer es gibt keine Alternative).
  Aurora tagsüber gezogen ist durch das TimeGate ausgeschlossen; um die Nachtanteile zu treffen,
  wird das Gewicht nachtgebundener Zustände mit 24/NachtStunden skaliert.
"""
import csv, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent / "ref"))
from aethris_random import AethrisRandom

ROOT = pathlib.Path(__file__).resolve().parents[1]
rd = lambda p: list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))
DEF = {r["Tag"].split(".")[1]: r for r in rd("Data/World/WeatherDefinitions.csv")}
NIGHT = set(range(21, 24)) | set(range(0, 5))    # Nachtstunden (K15 §2, Standardregion)
DAY = set(range(7, 19))

def gate_ok(w, hour):
    g = DEF[w]["TimeGate"]
    return g == "Any" or (g == "Night" and hour in NIGHT) or (g == "Day" and hour in DAY)

def simulate(weights, days=4000, seed=7, sel=None):
    """weights = Zielanteile; sel = kalibrierte Auswahlgewichte (Standard: Zielanteile)."""
    sel = sel or weights
    rng = AethrisRandom(seed, 1)
    t, cur, share = 0, None, {w: 0 for w in weights}
    end = days * 24
    while t < end:
        hour = t % 24
        cands = [w for w, g in weights.items() if g > 0 and gate_ok(w, hour) and w != cur] or [cur]
        def wt(w):
            # identisch zu FWeatherScheduler::MakeNext (Ganzzahl): Gewicht*24*2000 / (Fenster * 2*mittlereDauer)
            meanx2 = int(DEF[w]["MinHours"]) + int(DEF[w]["MaxHours"])
            window = 8 if DEF[w]["TimeGate"] == "Night" else (12 if DEF[w]["TimeGate"] == "Day" else 24)
            return int(round(sel[w])) * 24 * 2000 // (window * meanx2)
        tot = sum(wt(w) for w in cands)
        if tot <= 0:
            cands, tot = [cands[0]], 1
            wt = lambda _w: 1
        r = rng.next_bounded(min(tot, 2**32 - 1))
        w = cands[-1]
        for c in cands:
            r -= wt(c)
            if r < 0:
                w = c
                break
        dur = rng.range_inclusive(int(DEF[w]["MinHours"]), int(DEF[w]["MaxHours"]))
        share[w] += min(dur, end - t); t += dur; cur = w
    return {w: 100 * s / end for w, s in share.items()}

def calibrate(weights, rounds=40):
    """Iteratives Anpassen der Auswahlgewichte, bis die Zeitanteile den Zielen entsprechen."""
    sel = {w: float(g) * 10 for w, g in weights.items()}   # Promille-Skala
    for _ in range(rounds):
        res = simulate(weights, days=2500, sel=sel)
        for w in sel:
            if weights[w] > 0 and res[w] > 0:
                sel[w] *= (weights[w] / res[w]) ** 0.7
    return sel

def main():
    bad = 0
    out = []
    for row in rd("Data/World/RegionWeather.csv"):
        weights = {k: int(v) for k, v in row.items() if k != "Name"}
        sel = calibrate(weights)
        norm = sum(sel.values())
        sel = {w: round(1000 * v / norm) for w, v in sel.items()}
        out.append((row["Name"], sel))
        res = simulate(weights, days=6000, seed=99, sel=sel)   # Validierung mit anderem Seed
        diffs = {w: res[w] - weights[w] for w in weights if weights[w] > 0}
        worst = max(diffs.items(), key=lambda kv: abs(kv[1]))
        ok = abs(worst[1]) <= 3.0
        bad += not ok
        print(f"{row['Name']}: max. Abweichung {worst[0]} {worst[1]:+.1f} pp {'OK' if ok else 'FEHLER'}  | " +
              ", ".join(f"{w} {res[w]:.0f}/{weights[w]}" for w in weights if weights[w] > 0))
    path = ROOT / "Data/World/WeatherSelectionWeights.csv"
    keys = list(out[0][1].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        f.write("# Kalibrierte Auswahlgewichte (Promille) – erzeugt von tools/sim_weather.py, NICHT von Hand ändern (K14 §4).\n")
        w = csv.writer(f); w.writerow(["Name"] + keys)
        for name, sel in out: w.writerow([name] + [sel[k] for k in keys])
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
