#!/usr/bin/env python3
"""Platziert Dörfer und Außenposten auf der Makrokarte (K13).

Verfahren: Farthest-Point-Sampling innerhalb der Regionszellen (MacroMap.txt bzw. MacroMap_Sky.txt für R10),
Startmenge = bereits feste Orte (Stadt, Lindwiesen). Deterministisch. Mindestabstand-Prüfung 400 m.
Schreibt XKm/YKm in Data/World/Settlements.csv.
"""
import csv, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
CHAR = {"R01": "V", "R02": "K", "R03": "M", "R04": "S", "R05": "I", "R06": "C", "R07": "H", "R08": "A", "R09": "P", "R10": "N"}
CELL = 0.2

def cells(region):
    path = ROOT / ("Data/World/MacroMap_Sky.txt" if region == "R10" else "Data/World/MacroMap.txt")
    grid = path.read_text(encoding="utf-8").splitlines()
    out = []
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == CHAR[region]:
                # Randzellen meiden: alle 4 Nachbarn müssen zur Region gehören
                nb = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                if all(0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == CHAR[region] for nx, ny in nb):
                    out.append(((x + 0.5) * CELL, (y + 0.5) * CELL))
    return out

def main():
    p = ROOT / "Data/World/Settlements.csv"
    rows = list(csv.DictReader(open(p, encoding="utf-8")))
    fields = list(rows[0].keys())
    for region in CHAR:
        cand = cells(region)
        fixed = [(float(r["XKm"]), float(r["YKm"])) for r in rows if r["RegionId"] == region and r["XKm"]]
        todo = [r for r in rows if r["RegionId"] == region and not r["XKm"]]
        todo.sort(key=lambda r: (r["Type"] != "Village", r["Name"]))   # Dörfer zuerst
        chosen = list(fixed)
        for r in todo:
            best = max(cand, key=lambda c: (min(math.dist(c, f) for f in chosen), -c[0], -c[1]))
            r["XKm"], r["YKm"] = f"{best[0]:.1f}", f"{best[1]:.1f}"
            chosen.append(best)
        pts = [(float(r["XKm"]), float(r["YKm"])) for r in rows if r["RegionId"] == region]
        dmin = min(math.dist(a, b) for i, a in enumerate(pts) for b in pts[i+1:])
        assert dmin >= 0.4, f"{region}: Mindestabstand {dmin:.2f} km < 0,4"
        print(f"{region}: {len(pts)} Orte, Mindestabstand {dmin:.2f} km")
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

if __name__ == "__main__":
    main()
