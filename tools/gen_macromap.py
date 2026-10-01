#!/usr/bin/env python3
"""Erzeugt die Makrokarte von Aethris (K08) als Raster: 40 × 35 Zellen à 200 m (8 × 7 km).

Jede Region erhält exakt die Zellzahl aus Data/World/RegionBudget.csv (1 Zelle = 0,04 km²).
Regionen wachsen von Saatpunkten aus (quotenbegrenzte Breitensuche) und bleiben zusammenhängend.
Nimbara (R10) ist eine Overlay-Schicht über dem Zentrum (Himmelinseln), zählt nicht als Bodenfläche.

Ausgabe:
  Data/World/MacroMap.txt      Bodenkarte, ein Zeichen pro Zelle
  Data/World/MacroMap_Sky.txt  Overlay R10
  Data/World/MacroRegions.csv  Zellzahl, Fläche, Schwerpunkt, Bounding Box je Region
"""
import csv, math, pathlib, heapq

ROOT = pathlib.Path(__file__).resolve().parents[1]
W, H, CELL_KM = 40, 35, 0.2
CHAR = {"R01": "V", "R02": "K", "R03": "M", "R04": "S", "R05": "I", "R06": "C",
        "R07": "H", "R08": "A", "R09": "P", "R10": "N"}
# Saatpunkte (x, y) – y = 0 ist Norden
SEEDS = {"R07": (20, 3), "R02": (20, 10), "R09": (15, 15), "R08": (24, 16), "R06": (5, 19),
         "R01": (13, 23), "R03": (26, 23), "R05": (34, 17), "R04": (19, 30)}
SKY_CENTER = (20, 15)

def budget():
    rows = csv.DictReader(open(ROOT / "Data/World/RegionBudget.csv", encoding="utf-8"))
    return {r["RegionId"]: round(float(r["AreaKm2"]) / (CELL_KM ** 2)) for r in rows}

def land_mask():
    cx, cy, rx, ry = 20, 17, 18.6, 15.6
    land = set()
    for y in range(H):
        for x in range(W):
            a = math.atan2(y - cy, x - cx)
            r = 1.0 + 0.07 * math.sin(3 * a) + 0.05 * math.cos(5 * a + 1.3)
            if ((x - cx) / (rx * r)) ** 2 + ((y - cy) / (ry * r)) ** 2 <= 1.0:
                land.add((x, y))
    return land

def grow(land, quotas):
    owner, heaps, taken = {}, {}, {k: 0 for k in SEEDS}
    for k, (sx, sy) in SEEDS.items():
        heaps[k] = [(0.0, sx, sy)]
    active = True
    while active:
        active = False
        for k in sorted(SEEDS, key=lambda r: taken[r] / quotas[r]):
            if taken[k] >= quotas[k]:
                continue
            h = heaps[k]
            while h:
                d, x, y = heapq.heappop(h)
                if (x, y) in owner or (x, y) not in land:
                    continue
                owner[(x, y)] = k
                taken[k] += 1
                sx, sy = SEEDS[k]
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if (nx, ny) in land and (nx, ny) not in owner:
                        heapq.heappush(h, (math.hypot(nx - sx, ny - sy), nx, ny))
                active = True
                break
    return owner, taken

def main():
    q = budget()
    ground = {k: v for k, v in q.items() if k != "R10"}
    land = land_mask()
    assert len(land) >= sum(ground.values()), (len(land), sum(ground.values()))
    owner, taken = grow(land, ground)
    for k in ground:
        assert taken[k] == ground[k], f"{k}: {taken[k]} != {ground[k]} (Saatpunkt verschieben)"
    lines = []
    for y in range(H):
        row = ""
        for x in range(W):
            if (x, y) in owner: row += CHAR[owner[(x, y)]]
            elif (x, y) in land: row += "^"   # unpassierbare Grenzklippen
            else: row += "~"                  # Meer
        lines.append(row)
    (ROOT / "Data/World/MacroMap.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    # Himmelinseln: q["R10"] Zellen nächstgelegen zum Zentrum
    cells = sorted(((math.hypot(x - SKY_CENTER[0], (y - SKY_CENTER[1]) * 1.3), x, y)
                    for y in range(H) for x in range(W)))[:q["R10"]]
    sky = {(x, y) for _, x, y in cells}
    (ROOT / "Data/World/MacroMap_Sky.txt").write_text(
        "\n".join("".join("N" if (x, y) in sky else "." for x in range(W)) for y in range(H)) + "\n", encoding="utf-8")
    with open(ROOT / "Data/World/MacroRegions.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["RegionId", "Cells", "AreaKm2", "CentroidXKm", "CentroidYKm", "MinXKm", "MinYKm", "MaxXKm", "MaxYKm"])
        regs = dict(owner); regs.update({c: "R10" for c in sky})
        for k in sorted(q):
            cs = [c for c, o in owner.items() if o == k] if k != "R10" else list(sky)
            xs, ys = [c[0] for c in cs], [c[1] for c in cs]
            wr.writerow([k, len(cs), round(len(cs) * CELL_KM ** 2, 2),
                         round((sum(xs) / len(xs) + 0.5) * CELL_KM, 2), round((sum(ys) / len(ys) + 0.5) * CELL_KM, 2),
                         round(min(xs) * CELL_KM, 1), round(min(ys) * CELL_KM, 1),
                         round((max(xs) + 1) * CELL_KM, 1), round((max(ys) + 1) * CELL_KM, 1)])
    # Zusammenhangsprüfung
    for k in ground:
        cs = {c for c, o in owner.items() if o == k}
        start = next(iter(cs)); seen = {start}; st = [start]
        while st:
            x, y = st.pop()
            for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if n in cs and n not in seen: seen.add(n); st.append(n)
        assert len(seen) == len(cs), f"{k} nicht zusammenhängend"
    print("Land:", len(land), "Boden:", sum(taken.values()), "Klippen:", len(land) - sum(taken.values()), "Himmel:", len(sky))
    print("\n".join(lines))

if __name__ == "__main__":
    main()
