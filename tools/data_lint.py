#!/usr/bin/env python3
"""Daten-Lint für Data/**/*.csv (K06 §3, Pre-Submit-Gate).

Jede Prüfregel ist eine Funktion check_*; neue Kapitel ergänzen Regeln.
Exitcode 1 bei Verstößen.
"""
import csv, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
ERRORS: list[str] = []

def rows(rel):
    p = DATA / rel
    if not p.exists():
        return []
    return list(csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#")))

def err(msg):
    ERRORS.append(msg)

ID_PATTERNS = {  # K04 §7
    "Items/Resources.csv": re.compile(r"^ITM_MAT_[A-Z0-9_]+$"),
    "World/Zones.csv": re.compile(r"^R(0[1-9]|10)_Z\d{2}$"),
}

def check_ids():
    retired = {r["Id"] for r in rows("Meta/RetiredIds.csv")}
    for rel, pat in ID_PATTERNS.items():
        seen = set()
        for r in rows(rel):
            i = r["Name"]
            if not pat.match(i): err(f"{rel}: ID {i} verletzt K04 §7")
            if i in seen: err(f"{rel}: doppelte ID {i}")
            if i in retired: err(f"{rel}: ID {i} ist stillgelegt (RetiredIds)")
            seen.add(i)

def check_region_budget():
    b = rows("World/RegionBudget.csv")
    expect = {"AreaKm2": 36.0, "FirstAppearanceSpecies": 240, "Villages": 22, "Outposts": 30, "SideQuests": 210, "ResonanceStones": 80}
    for k, v in expect.items():
        s = round(sum(float(r[k]) for r in b), 2)
        if s != v: err(f"RegionBudget: Σ{k} = {s}, erwartet {v} (CANON §3/§19)")

def check_type_distribution():
    budget = {r["RegionId"]: int(r["FirstAppearanceSpecies"]) for r in rows("World/RegionBudget.csv")}
    for r in rows("World/RegionTypeDistribution.csv"):
        s = sum(int(v) for k, v in r.items() if k != "Name")
        if s != budget.get(r["Name"]): err(f"Typverteilung {r['Name']}: {s} ≠ {budget.get(r['Name'])}")

def check_weather():
    for r in rows("World/RegionWeather.csv"):
        s = sum(int(v) for k, v in r.items() if k != "Name")
        if s != 100: err(f"Wetter {r['Name']}: Σ {s} ≠ 100")
        if int(r["ResonanceStorm"]) != 0: err(f"Wetter {r['Name']}: Resonanzsturm muss 0 sein (nur global)")

def check_zones():
    tiers = {int(r["Tier"]): (int(r["MinLevel"]), int(r["MaxLevel"])) for r in rows("World/ZoneTiers.csv")}
    for z in rows("World/Zones.csv"):
        if z["Mode"] == "SCALED":
            for t in range(int(z["MinTier"]), int(z["MaxTier"]) + 1):
                lo, hi = tiers[t]
                if lo + int(z["OffMin"]) > min(hi, lo + int(z["OffMax"])): err(f"Zone {z['Name']} Stufe {t}: leeres Band")
        elif int(z["MinLevel"]) > int(z["MaxLevel"]):
            err(f"Zone {z['Name']}: Min > Max")

def check_column_counts():
    """DL-COL (K54): jede Zeile hat so viele Spalten wie die Kopfzeile – Kommas in Werten müssen in Anführungszeichen stehen."""
    for f in sorted(DATA.rglob("*.csv")):
        lines = [l for l in open(f, encoding="utf-8") if not l.startswith("#") and l.strip()]
        rs = list(csv.reader(lines))
        if not rs:
            continue
        n = len(rs[0])
        for r in rs[1:]:
            if len(r) != n:
                err(f"{f.relative_to(DATA)}: Zeile {r[0]} hat {len(r)} statt {n} Spalten")

def main():
    for name, fn in list(globals().items()):
        if name.startswith("check_") and callable(fn):
            fn()
    for e in ERRORS:
        print("FEHLER:", e)
    print(f"Data-Lint: {len(ERRORS)} Verstöße.")
    return 1 if ERRORS else 0

if __name__ == "__main__":
    sys.exit(main())
