#!/usr/bin/env python3
"""Erzeugt den CANON-Abschnitt für einen Katalogbereich (kompakte Artenliste)."""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import gen_catalog as gc
sec, kid, lo, hi = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
v = gc.Validator(); v.run()
sp = [r for r in v.sp if lo <= int(r["KodexNumber"]) <= hi]
out = [f"## {sec} Arten #{lo:03d}–#{hi:03d} (LOCKED, {kid} · `Data/Echos/Species.csv`)", "",
       "| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |", "|---|---|---|---|---|---|---|"]
names = {r["Name"]: r["DisplayName"] for r in v.sp}
for r in sp:
    t = gc.tname(r["PrimaryType"]) + (f"/{gc.tname(r['SecondaryType'])}" if r["SecondaryType"] else "")
    evo = "; ".join(f"{names.get(e, e)} [{c}]" for e, c in zip(r["EvolvesTo"].split("|"), (r["EvoCondition"].split(") | (") if "|" in r["EvolvesTo"] else [r["EvoCondition"]])) if e) or "–"
    evo = evo.replace("(", "").replace(")", "")
    m = gc.MOUNT_DE[r["Mount"].split(".")[1]] if r["Mount"] else "–"
    out.append(f"| {int(r['KodexNumber']):03d} | {r['DisplayName']} | {t} | {r['Line']}/{r['Stage']} {r['LineKind']} | {evo} | {r['Role']} | {m} |")
print("\n".join(out))
