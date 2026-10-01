#!/usr/bin/env python3
"""Authoring-Bibliothek für die Kreaturenkataloge K20–K27.

Jede Regionsdatei (k20_r01.py …) beschreibt Linien kompakt; diese Bibliothek
 - vergibt Kodexnummern, IDs, Linien-IDs, Gattungen, Stufen, LineKind, EvolvesTo,
 - berechnet Basiswerte aus Rollenprofil + Zielsumme (exakt, größter Rest),
 - setzt Standardwerte (PRÄ/AUS je Rolle, EP-Ertrag je Stufe, Gewicht aus Dichte),
 - schreibt die Zeilen idempotent in Data/Echos/Species.csv und SpeciesLore.csv (ersetzt den Kodexbereich).
"""
from __future__ import annotations
import csv, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPECIES = ROOT / "Data/Echos/Species.csv"
LORE = ROOT / "Data/Echos/SpeciesLore.csv"

ROLE_SHAPE = {  # HP, ANG, VER, SAN, SVE, GES
    "Tank":     (1.20, 0.90, 1.30, 0.70, 1.10, 0.80),
    "Striker":  (0.95, 1.35, 0.90, 0.70, 0.85, 1.25),
    "Caster":   (0.90, 0.60, 0.85, 1.40, 1.05, 1.20),
    "Speed":    (0.85, 1.10, 0.80, 1.00, 0.85, 1.40),
    "Support":  (1.10, 0.80, 1.05, 1.00, 1.15, 0.90),
    "Control":  (1.00, 0.80, 1.00, 1.15, 1.05, 1.00),
    "AllRound": (1.00, 1.00, 1.00, 1.00, 1.00, 1.00),
}
ROLE_ACC = {"Tank": (100, 92), "Striker": (106, 96), "Caster": (104, 100), "Speed": (96, 110),
            "Support": (100, 102), "Control": (102, 100), "AllRound": (100, 100)}
EXP_YIELD = {("Three", 1): 60, ("Three", 2): 140, ("Three", 3): 210, ("Two", 1): 75, ("Two", 2): 190,
             ("Single", 1): 180, ("Branch", 2): 190, ("Branch", 3): 210, ("Legendary", 1): 320, ("Mythical", 1): 320}
DENSITY = {"A12": 0.08, "A16": 0.15, "A05": 0.35, "A06": 0.4, "A15": 0.5}
STATS = ("HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed")

FIELDS = ["Name", "KodexNumber", "DisplayName", "ScientificName", "Category", "Line", "Stage", "LineKind", "Archetype",
          "SizeClass", "HeightM", "WeightKg", "PrimaryType", "SecondaryType", "Region", "Habitat", "Zones", "Rarity",
          "SpawnConditions", "Activity", "Traits", "Niches", "Role", "Mount", "GrowthRate", "ExpYield", "PolishYield",
          "HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed", "Precision", "Evasion", "EvolvesTo",
          "EvoCondition", "BondRate", "BondLure", "SignatureConcept", "SoundMark"]
LORE_FIELDS = ["Name", "LoreOrigin", "LoreBehavior", "LoreMyth", "LoreHumans", "KodexL4"]


def distribute(total, shape, tweak=None):
    """Verteilt `total` auf 6 Werte gemäß Profil (größter Rest, exakt)."""
    w = [s * (1 + (tweak[i] if tweak else 0)) for i, s in enumerate(shape)]
    raw = [total * x / sum(w) for x in w]
    base = [int(r) for r in raw]
    rest = total - sum(base)
    for i in sorted(range(6), key=lambda i: raw[i] - base[i], reverse=True)[:rest]:
        base[i] += 1
    return base


def T(t):
    return f"Type.{t}" if t else ""


class Catalog:
    def __init__(self, start_kodex: int, start_line: int, region: str):
        self.k = start_kodex
        self.line = start_line
        self.region = region
        self.rows, self.lore = [], []

    def _row(self, e, line_id, stage, kind, genus, evolves_to, evo):
        stats = e.get("stats")
        if isinstance(stats, tuple) and len(stats) == 2 and isinstance(stats[1], int) and isinstance(stats[0], str):
            stats = distribute(stats[1], ROLE_SHAPE[stats[0]])
        elif isinstance(stats, tuple) and len(stats) == 3:
            stats = distribute(stats[1], ROLE_SHAPE[stats[0]], stats[2])
        prec, eva = e.get("acc", ROLE_ACC[e["role"]])
        h = e["h"]
        dens = e.get("dens", DENSITY.get(e["arch"], 0.7))
        w = e.get("w", round(max(0.1, dens * (h * 10) ** 3 * 0.25), 1))
        ystage = stage if kind != "Branch" else stage
        r = {
            "Name": f"ECHO_{self.k:03d}", "KodexNumber": self.k, "DisplayName": e["name"],
            "ScientificName": f"{genus} {e['epithet']}", "Category": e["cat"], "Line": line_id, "Stage": stage,
            "LineKind": kind, "Archetype": e["arch"], "SizeClass": e["size"], "HeightM": h, "WeightKg": w,
            "PrimaryType": T(e["types"][0]), "SecondaryType": T(e["types"][1] if len(e["types"]) > 1 else ""),
            "Region": self.region, "Habitat": e["habitat"], "Zones": "|".join(e.get("zones", [])),
            "Rarity": e["rarity"], "SpawnConditions": "|".join(e.get("conds", [])),
            "Activity": f"Behavior.Activity.{e['act']}", "Traits": "|".join(f"Behavior.{t}" for t in e["traits"]),
            "Niches": "|".join(f"Niche.{n}" for n in e["niches"]), "Role": e["role"],
            "Mount": f"Mount.{e['mount']}" if e.get("mount") else "", "GrowthRate": e.get("growth", "Steady"),
            "ExpYield": e.get("exp", EXP_YIELD.get((kind, ystage), 140)), "PolishYield": e["polish"],
            **{s: v for s, v in zip(STATS, stats)}, "Precision": prec, "Evasion": eva,
            "EvolvesTo": "|".join(evolves_to), "EvoCondition": evo or "", "BondRate": e.get("bond", 45),
            "BondLure": e["lure"], "SignatureConcept": e["sig"], "SoundMark": e["mark"],
        }
        self.rows.append(r)
        self.lore.append({"Name": r["Name"], **dict(zip(LORE_FIELDS[1:], e["lore"]))})
        self.k += 1
        return r["Name"]

    def line_of(self, kind: str, genus: str, stages: list[dict], branch: dict | None = None):
        """kind ∈ Three/Two/Single; stages = Liste der Stufen; branch = optionale Zweigform der letzten Stufe.
        Die Evolutionsbedingung zum Erreichen einer Stufe steht in deren Vorgänger unter 'evo'."""
        line_id = f"L{self.line:03d}"
        self.line += 1
        ids = [f"ECHO_{self.k + i:03d}" for i in range(len(stages))]
        branch_id = f"ECHO_{self.k + len(stages):03d}" if branch else None
        for i, e in enumerate(stages):
            nxt = [ids[i + 1]] if i + 1 < len(stages) else []
            evo = e.get("evo")
            if branch and i == len(stages) - 2:
                nxt.append(branch_id)
                evo = f"({e['evo']}) | ({branch['evo_from_prev']})"
            self._row(e, line_id, i + 1, kind, genus, nxt, evo if nxt else None)
        if branch:
            self._row(branch, line_id, len(stages), "Branch", genus, [], None)
        return line_id

    def write(self):
        rows = list(csv.DictReader(open(SPECIES, encoding="utf-8")))
        lore = list(csv.DictReader(open(LORE, encoding="utf-8")))
        new_ids = {r["Name"] for r in self.rows}
        rows = [r for r in rows if r["Name"] not in new_ids] + self.rows
        lore = [r for r in lore if r["Name"] not in new_ids] + self.lore
        rows.sort(key=lambda r: int(r["KodexNumber"]))
        # Identitätsakzente (K63 §3) idempotent erneut anwenden, damit ein Neuschreiben sie nicht verliert.
        sys.path.insert(0, str(ROOT / "tools" / "ref"))
        from aethris_balance import apply_accents
        apply_accents(rows)
        lore.sort(key=lambda r: int(r["Name"][5:]))
        with open(SPECIES, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
        with open(LORE, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=LORE_FIELDS); w.writeheader(); w.writerows(lore)
        print(f"{len(self.rows)} Arten geschrieben (#{self.rows[0]['KodexNumber']}–#{self.rows[-1]['KodexNumber']}), nächste Linie L{self.line:03d}")
