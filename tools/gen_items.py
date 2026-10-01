#!/usr/bin/env python3
"""Validiert Gegenstandsdaten (K40–K42): eindeutige IDs über alle Item-Tabellen, Rezept-Referenzen, Preise (ab K42)."""
import csv, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLES = ["Resources", "EchoMaterials", "Consumables", "Lures", "Seals", "WardenGear", "HeldItems", "EvolutionItems",
          "Traps", "BreedingItems", "Klangschriften"]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


def validate():
    errs, known = [], {}
    for t in TABLES:
        for r in rows(f"Data/Items/{t}.csv"):
            if r["Name"] in known and t != "Resources":
                errs.append(f"ID doppelt: {r['Name']} ({known[r['Name']]} / {t})")
            known.setdefault(r["Name"], t)
    for r in rows("Data/Items/Recipes.csv"):
        if r["Output"] not in known:
            errs.append(f"{r['Name']}: Ausgabe {r['Output']} unbekannt")
        for part in r["Ingredients"].split(";"):
            n, q = part.split("×")
            if "<TYP>" not in n and n not in known:
                errs.append(f"{r['Name']}: Zutat {n} unbekannt")
            if not q.isdigit() or int(q) < 1:
                errs.append(f"{r['Name']}: Menge {q}")
    prices = ROOT / "Data/Economy/ItemPrices.csv"
    if prices.exists():
        p = {r["Name"]: r for r in rows("Data/Economy/ItemPrices.csv")}
        for n in p:
            if n not in known:
                errs.append(f"Preis für unbekanntes Item {n}")
    return errs, len(known)


if __name__ == "__main__":
    e, n = validate()
    for x in e:
        print("FEHLER:", x)
    print(f"Items: {n}, {len(e)} Verstöße.")
    sys.exit(1 if e else 0)
