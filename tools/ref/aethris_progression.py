#!/usr/bin/env python3
"""Wärterrang-Fortschritt (K43): EP-Quellen, Rang je Spielabschnitt, Minuten je Rangaufstieg."""
import csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


XP = [int(r["RequiredWardenXP"]) for r in rows("Data/Progression/WardenRank.csv")]
PHASES = [("Prolog", 3, 800), ("Akt I", 15, 2000), ("Akt II", 20, 2000), ("Akt III", 12, 2500), ("Endgame 1–20 h", 20, 2800),
          ("Endgame 20–40 h", 20, 3000), ("Endgame 40–60 h", 20, 3000)]


def rank_of(xp):
    r = 1
    for i, need in enumerate(XP, 1):
        if xp >= need:
            r = i
    return r


def timeline():
    out = ["| Abschnitt | Spielzeit | Wärter-EP/h | EP am Ende | Rang am Ende | Ø Minuten je Rang |", "|---|---|---|---|---|---|"]
    xp, r0 = 0, 1
    for name, h, rate in PHASES:
        xp += h * rate
        r = rank_of(xp)
        mins = h * 60 // max(1, r - r0) if r > r0 else 0
        out.append(f"| {name} | {h} h | {rate:,} | {xp:,} | {r} | {mins if mins else '–'} |".replace(",", "."))
        r0 = r
    return "\n".join(out)


SOURCES = [("Hauptquest-Schritt", "300–1.500", "Haupt 25 %"), ("Nebenquest", "400–2.000", "Neben 25 %"),
           ("Kodex-Stufe 1/2/3/4", "10 / 30 / 60 / 120", "Kodex 20 %"), ("Klangfragment", "80", "Kodex"),
           ("Entdeckung (POI, Aussicht, Resonanzstein)", "20–150", "Entdeckung 15 %"), ("Arena (Vorprüfung/Akkord)", "300 / 2.000", "Arenen 10 %"),
           ("Aufträge, Crafting, Fotos, Zucht", "10–200", "Sonstiges 5 %")]


def sources():
    out = ["| Quelle | Wärter-EP | Zielanteil (CANON §18) |", "|---|---|---|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in SOURCES]
    return "\n".join(out)


if __name__ == "__main__":
    print(timeline())
