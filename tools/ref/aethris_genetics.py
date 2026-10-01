#!/usr/bin/env python3
"""Genetik-Referenz (K38, löst Q3): Anlagen-Vererbung, Morphs, Loci; Simulation für DR-18 (perfektes Echo ≤ 15 h).

Vererbung je Anlage (8 Werte, 0–15): 400 ‰ Elternteil A, 400 ‰ Elternteil B, 200 ‰ neu gewürfelt.
Erbklang: 4 gewählte Anlagen sicher vom gewählten Elternteil. Zucht-Seed: Fork(3) (CANON §29).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aethris_random import AethrisRandom

STATS = 8
INHERIT_A, INHERIT_B = 400, 400
MORPH_BASE = 1          # von 1024
KEIME_PER_HOUR = 12     # 3 Brutnischen × 1 Keim je 15 Spielminuten
HATCH_MIN = 12          # Ø Reife in Spielminuten bei parallelem Tragen (6 Keime)


def child_aptitudes(a, b, rng, erbklang=None):
    """erbklang = (parent 'A'|'B', [Indizes])."""
    out = []
    for i in range(STATS):
        if erbklang and i in erbklang[1]:
            out.append((a if erbklang[0] == "A" else b)[i])
            continue
        r = rng.next_bounded(1000)
        out.append(a[i] if r < INHERIT_A else b[i] if r < INHERIT_A + INHERIT_B else rng.next_bounded(16))
    return out


def morph_chance_1024(fernklang=False, skill=False, storm=False):
    return MORPH_BASE * (3 if fernklang else 1) * (2 if skill else 1) * (2 if storm else 1)


def wild_parent(rng, rare=True):
    a = [rng.next_bounded(16) for _ in range(STATS)]
    if rare:   # Selten: 2 garantierte 15er (CANON §80)
        idx = set()
        while len(idx) < 2:
            idx.add(rng.next_bounded(STATS))
        for i in idx:
            a[i] = 15
    return a


def score(apt, wanted):
    return sum(1 for i in wanted if apt[i] == 15)


def breed_to_perfect(rng, wanted=(0, 1, 2, 3, 4, 5), use_erbklang=True, max_keime=2000):
    """Gierige Strategie: zwei Eltern; jedes Kind ersetzt den schwächeren Elternteil, wenn es mehr 15er in den Zielwerten hat.
    Erbklang: die 4 besten 15er-Werte des besseren Elternteils werden gesichert."""
    p = [wild_parent(rng), wild_parent(rng)]
    for k in range(1, max_keime + 1):
        p.sort(key=lambda x: score(x, wanted), reverse=True)
        ek = None
        if use_erbklang:
            fifteen = [i for i in wanted if p[0][i] == 15][:4]
            ek = ("A", fifteen) if fifteen else None
        c = child_aptitudes(p[0], p[1], rng, ek)
        if score(c, wanted) == len(wanted):
            return k
        if score(c, wanted) > score(p[1], wanted):
            p[1] = c
    return max_keime


def dr18_table(n=300):
    rng = AethrisRandom(0x3838, 0x3)
    out = ["| Ziel | Strategie | Ø Keime | Median | P90 | Ø Spielstunden (12 Keime/h) |", "|---|---|---|---|---|---|"]
    for label, wanted in (("6 Kernwerte auf 15", (0, 1, 2, 3, 4, 5)), ("5 Werte (ein Angriffswert egal)", (0, 2, 3, 4, 5))):
        for erb in (False, True):
            res = sorted(breed_to_perfect(rng, wanted, erb) for _ in range(n))
            avg = sum(res) / n
            out.append(f"| {label} | {'mit Erbklang' if erb else 'ohne Hilfsmittel'} | {avg:.0f} | {res[n // 2]} | {res[int(n * 0.9)]} | {avg / KEIME_PER_HOUR:.1f} h |".replace(".", ","))
    return "\n".join(out)


def _rows(p):
    import csv
    root = pathlib.Path(__file__).resolve().parents[2]
    return list(csv.DictReader(l for l in open(root / p, encoding="utf-8") if not l.startswith("#")))


def group_table():
    arch = {r["Name"]: r["Phylum"] for r in _rows("Data/Echos/Archetypes.csv")}
    sp = [s for s in _rows("Data/Echos/Species.csv") if s["LineKind"] not in ("Legendary", "Mythical")]
    groups = {}
    for s in sp:
        if s["Stage"] == "1" or s["LineKind"] == "Single":
            groups.setdefault(arch[s["Archetype"]], []).append(s["DisplayName"])
    out = ["| Resonanzgruppe | Anzahl Linien (Stufe-1-Formen) | Arten (Stufe 1 bzw. Einzelarten) |", "|---|---|---|"]
    for g in sorted(groups):
        out.append(f"| {g} | {len(groups[g])} | {', '.join(sorted(groups[g]))} |")
    return "\n".join(out)


def egg_table():
    ab = {a["Name"]: a["DisplayName"] for a in _rows("Data/Abilities/Abilities.csv")}
    sp = {s["Name"]: s for s in _rows("Data/Echos/Species.csv")}
    eggs = {}
    for r in _rows("Data/Echos/Learnsets.csv"):
        if r["Method"] == "Egg":
            eggs.setdefault(r["Species"], []).append(ab[r["Ability"]])
    out = ["| Linie | Stufe-1-Art | Ei-Fähigkeiten (Status fremder Typen) |", "|---|---|---|"]
    for sid in sorted(eggs, key=lambda x: int(x[5:])):
        s = sp[sid]
        out.append(f"| {s['Line']} | {s['DisplayName']} | {', '.join(eggs[sid])} |")
    return "\n".join(out)


if __name__ == "__main__":
    print(dr18_table())
