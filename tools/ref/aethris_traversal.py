#!/usr/bin/env python3
"""Traversal-Kennzahlen (K40): Reittier-Verzeichnis, Reisezeiten."""
import csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


def mount_table():
    kinds = {r["Name"]: r for r in rows("Data/World/MountKinds.csv")}
    rd = {"R01": "Verdanthain", "R02": "Kharsgrat", "R03": "Morvenmoor", "R04": "Sahrun-Weite", "R05": "Ignareth",
          "R06": "Saltrand", "R07": "Hvitfell", "R08": "Ael'Dorun", "R09": "Prismtiefen", "R10": "Nimbara"}
    out = ["| # | Art | Region | Reitart | Größe | Tempo (m/s) | Freischaltung |", "|---|---|---|---|---|---|---|"]
    n = 0
    for s in rows("Data/Echos/Species.csv"):
        if not s["Mount"]:
            continue
        k = kinds[s["Mount"]]
        sp = k.get("Speed" + s["SizeClass"], "–")
        out.append(f"| {int(s['KodexNumber']):03d} | {s['DisplayName']} | {rd.get(s['Region'], s['Region'])} | {k['DisplayName']} | {s['SizeClass']} | {sp} | {k['Unlock']} |")
        n += 1
    return "\n".join(out) + f"\n\n**{n} Reittiere** im Grundkatalog."


def travel_table():
    speeds = [("Joggen", 4.2), ("Sprint (mit Pausen, Ø)", 5.6), ("Bodenreiten (L)", 14.0), ("Grabreiten (XL)", 11.0),
              ("Schwimmreiten (L)", 12.0), ("Flugreiten (L)", 20.0), ("Gleiter V (von 300 m Höhe)", 12.0)]
    dists = [("POI-Abstand (Ø 200 m)", 200), ("Zone durchqueren (Ø 1,2 km)", 1200), ("Region durchqueren (Ø 3,5 km)", 3500),
             ("Weltdiagonale (≈ 8,5 km)", 8500)]
    out = ["| Strecke | " + " | ".join(n for n, _ in speeds) + " |", "|---|" + "---|" * len(speeds)]
    for dn, d in dists:
        cells = []
        for _, v in speeds:
            t = d / v
            cells.append(f"{t:.0f} s" if t < 120 else f"{t / 60:.1f} min".replace(".", ","))
        out.append(f"| {dn} | " + " | ".join(cells) + " |")
    return "\n".join(out)


if __name__ == "__main__":
    print(mount_table())
    print(travel_table())
