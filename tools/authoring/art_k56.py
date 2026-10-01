#!/usr/bin/env python3
"""K56: Gestaltungsbriefe aus dem Artenkatalog (Klangmal, Signaturkonzept, Größe, Typen)."""
import csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
SP = list(csv.DictReader(l for l in open(ROOT / "Data/Echos/Species.csv", encoding="utf-8") if not l.startswith("#")))
TC = {r["Name"]: r for r in csv.DictReader(l for l in open(ROOT / "Data/Art/TypeColors.csv", encoding="utf-8") if not l.startswith("#"))}


def briefs(region, n=6):
    rows = [s for s in SP if s["Region"] == region]
    # je Linie die Endstufe (höchste Stage) – zeigt das ausgereifte Motiv
    best = {}
    for s in rows:
        if s["Line"] not in best or int(s["Stage"]) > int(best[s["Line"]]["Stage"]):
            best[s["Line"]] = s
    pick = list(best.values())[: int(n)]
    lines = ["| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |", "|---|---|---|---|---|---|"]
    for s in pick:
        t = s["PrimaryType"].split(".")[-1]
        t2 = s["SecondaryType"].split(".")[-1] if s["SecondaryType"] else ""
        typ = f"{TC[t]['DisplayName']} `{TC[t]['Normal']}`" + (f" / {TC[t2]['DisplayName']}" if t2 else "")
        lines.append(f"| {s['DisplayName']} | {s['Category']} | {s['SizeClass']} ({s['HeightM'].replace('.', ',')} m) | {typ} | {s['SoundMark']} | {s['SignatureConcept']} |")
    return "\n".join(lines)
