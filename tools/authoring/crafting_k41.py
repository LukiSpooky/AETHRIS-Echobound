#!/usr/bin/env python3
"""K41 – Crafting: erzeugt Echo-Materialien, Verbrauchsgüter und alle Rezepte (deterministisch aus Ressourcen/Items)."""
import csv, hashlib, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


def h(*a):
    return int(hashlib.sha1("|".join(map(str, a)).encode()).hexdigest()[:8], 16)


TYPES = [("Ember", "Glut"), ("Tide", "Flut"), ("Stone", "Stein"), ("Storm", "Sturm"), ("Bloom", "Blüte"), ("Frost", "Frost"),
         ("Void", "Leere"), ("Light", "Licht"), ("Venom", "Gift"), ("Metal", "Metall"), ("Spirit", "Geist"),
         ("Crystal", "Kristall"), ("Sound", "Klang"), ("Gravity", "Schwerkraft"), ("Arcane", "Arkan")]
RES = rows("Data/Items/Resources.csv")
BY = {}
for r in RES:
    BY.setdefault((r["Category"], int(r["Tier"])), []).append(r["Name"])


def mat(cat, tier, key):
    lst = BY.get((cat, tier)) or BY.get((cat, max(1, tier - 1))) or BY[(cat, 1)]
    return lst[h(cat, tier, key) % len(lst)]


SLOT_MATS = {"RESONATOR": ("Crystal", "Ore"), "GLIDER": ("Wood", "Herb"), "BOOTS": ("Herb", "Ore"), "CLOAK": ("Herb", "Wood"),
             "BAG": ("Herb", "Wood"), "LENS": ("Crystal", "Ore"), "TOOL": ("Ore", "Wood"), "LANTERN": ("Ore", "Crystal"),
             "MASK": ("Herb", "Crystal")}
SLOT_STATION = {"RESONATOR": "Akademie-Labor (Dorunsruh)", "GLIDER": "Werft (Saltrand-Hafen)", "BOOTS": "Werkbank",
                "CLOAK": "Werkbank", "BAG": "Werkbank", "LENS": "Glasbläserei (Qasr Sahrun)", "TOOL": "Schmiede (Schlackenwehr)",
                "LANTERN": "Glasbläserei (Qasr Sahrun)", "MASK": "Werft (Saltrand-Hafen)"}


def main():
    # Echo-Materialien
    emat = [(f"ITM_EMAT_{t.upper()}", f"Klangsplitter ({d})", t, "Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund")
            for t, d in TYPES]
    emat += [("ITM_EMAT_FEATHER", "Gefiederte Daune", "–", "Volantia-Echos im Hain (Mauser)"),
             ("ITM_EMAT_SCALE", "Abgestreifte Schuppe", "–", "Serpentia/Aquatica-Echos im Hain (Häutung)"),
             ("ITM_EMAT_SHELLDUST", "Panzerstaub", "–", "Testudinia/Articulata-Echos im Hain"),
             ("ITM_EMAT_ECHOWOOL", "Echowolle", "–", "Schur von Wolle tragenden Echos (Kjalf, Nubi …)"),
             ("ITM_EMAT_STILLSHARD", "Stillstein-Splitter", "Void", "Story: zerstörte Stillsteine (K44–K45)")]
    with open(ROOT / "Data/Items/EchoMaterials.csv", "w", newline="", encoding="utf-8") as f:
        f.write("# Echo-Materialien (K41 §2): nie durch Verletzen gewonnen – abgeworfen, geschenkt, im Hain gesammelt (ADR-007).\n")
        w = csv.writer(f)
        w.writerow(["Name", "DisplayName", "Type", "Sources"])
        w.writerows(emat)
    cons = [
        ("ITM_CON_HEAL_1", "Heilkraut-Tinktur", "Heilt ein Echo um 30 % Max-HP (Kampf: Zeitkosten 60)"),
        ("ITM_CON_HEAL_2", "Starke Tinktur", "Heilt ein Echo um 60 % Max-HP"),
        ("ITM_CON_HEAL_3", "Quellwasser-Elixier", "Heilt ein Echo vollständig"),
        ("ITM_CON_HEAL_ALL", "Chorbalsam", "Heilt alle Chor-Echos um 40 % (außerhalb des Kampfes)"),
        ("ITM_CON_REVIVE", "Weckklang", "Belebt ein verklungenes Echo mit 40 % HP (Kampf: 1× je Echo)"),
        ("ITM_CON_CLEANSE", "Läuterwasser", "Entfernt Haupt-Status und Gift"),
        ("ITM_CON_STAMINA", "Bergtee", "Wärter-Ausdauer +20 für 1 Spielstunde"),
        ("ITM_CON_WARM", "Glühwurzel-Sud", "Kälte-/Hitzeschutz 1 Spielstunde (ersetzt Wettermantel-Stufe)"),
        ("ITM_CON_SENSE", "Lauschöl", "Resonanzsinn-Reichweite +30 m für 30 Spielminuten"),
        ("ITM_CON_REPEL", "Ruhrauch", "Wildechos meiden den Wärter 10 Spielminuten (keine Kämpfe)"),
        ("ITM_CON_WANDELKLANG", "Wandelklang", "Wechselt die Passive eines Echos (CANON §102)"),
        ("ITM_CON_KLANGSALZ", "Klangsalz", "Setzt den Schliff eines Echos zurück (CANON §80)"),
        ("ITM_CON_WESENSKLANG", "Wesensklang", "Ändert die Persönlichkeit eines Echos (Endgame, CANON §81)"),
    ]
    cook = [
        ("ITM_FOODC_STEW", "Lindwald-Eintopf", "Stimmung des Chors +15; Bindungszuwachs +10 % für 1 Spieltag"),
        ("ITM_FOODC_FISHPIE", "Fischpastete", "EP +10 % für 1 Spieltag"),
        ("ITM_FOODC_HONEYCAKE", "Honigkuchen", "Lieblingsfutter-Bonus für alle Echos (1 Mahlzeit)"),
        ("ITM_FOODC_SPICEBREAD", "Würzbrot", "Ausdauer-Regeneration +20 % für 1 Spieltag"),
        ("ITM_FOODC_ICEJELLY", "Eisgelee", "Hitzewelle ohne Malus für 1 Spieltag"),
        ("ITM_FOODC_EMBERSOUP", "Glutsuppe", "Schnee/Kälte ohne Malus für 1 Spieltag"),
        ("ITM_FOODC_MOSSBUN", "Moosbrötchen", "Kodex-Beobachtung 2 s statt 3 s für 1 Spieltag"),
        ("ITM_FOODC_DATEROLL", "Dattelrolle", "Annäherung leiser (Entdeckungsradius ×0,9) für 1 Spieltag"),
        ("ITM_FOODC_KELPWRAP", "Tangrolle", "Schwimm-Ausdauer +30 % für 1 Spieltag"),
        ("ITM_FOODC_CHEESEPLATE", "Bergkäseplatte", "Reit-Ausdauer +15 % für 1 Spieltag"),
        ("ITM_FOODC_CLOUDTART", "Wolkentarte", "Gleiter-Auftrieb +10 % für 1 Spieltag"),
        ("ITM_FOODC_FEAST", "Chorfestmahl", "Alle Wirkungen der Grundgerichte (Stimmung, Bindung, EP) für 1 Spieltag"),
    ]
    with open(ROOT / "Data/Items/Consumables.csv", "w", newline="", encoding="utf-8") as f:
        f.write("# Verbrauchsgüter und Gerichte (K41 §4–§5). Ranked: keine Items (K61).\n")
        w = csv.writer(f)
        w.writerow(["Name", "DisplayName", "Effect", "Kind"])
        w.writerows([(a, b, c, "Consumable") for a, b, c in cons] + [(a, b, c, "Meal") for a, b, c in cook])
    # Rezepte
    rec = []

    def add(out, station, ingr, unlock, cat):
        rec.append([f"RCP_{len(rec) + 1:03d}", out, cat, station, ";".join(f"{n}×{q}" for n, q in ingr), unlock])

    for g in rows("Data/Items/WardenGear.csv"):
        if g["Slot"] == "SADDLE" or g["Tier"] == "1":
            continue
        t = int(g["Tier"])
        a, b = SLOT_MATS[g["Slot"]]
        station = "Werkbank" if t <= 3 else SLOT_STATION[g["Slot"]]
        ing = [(mat(a, t, g["Name"]), 4 + 2 * t), (mat(b, t, g["Name"] + "b"), 2 + 2 * t)]
        if t >= 4:
            ing.append((f"ITM_EMAT_{TYPES[h(g['Name']) % 15][0].upper()}", 2 + t))
        if t == 5:
            ing.append(("ITM_MAT_RESONANCECRYSTAL", 2))
        add(g["Name"], station, ing, f"Stufe {t - 1} besitzen", "Ausrüstung")
    for s in rows("Data/Items/Seals.csv"):
        if s["Name"] in ("ITM_SEAL_VOICE", "ITM_SEAL_STAR"):
            continue
        ing = {"ITM_SEAL_BASIC": [("ITM_MAT_SOUNDRESIN", 1), ("ITM_MAT_QUARTZSHARD", 1)],
               "ITM_SEAL_TUNED": [("ITM_MAT_SOUNDRESIN", 2), ("ITM_MAT_FOGPEARL", 1), ("ITM_MAT_KHARSIRON", 1)],
               "ITM_SEAL_MASTER": [("ITM_MAT_GLYPHCRYSTAL", 1), ("ITM_MAT_SILVERORE", 2), ("ITM_MAT_SOUNDRESIN", 2)],
               "ITM_SEAL_TYPE": [("ITM_SEAL_TUNED", 1), ("ITM_EMAT_<TYP>", 3)],
               "ITM_SEAL_NIGHT": [("ITM_SEAL_TUNED", 1), ("ITM_MAT_WISPMOSS", 2)],
               "ITM_SEAL_HEAVY": [("ITM_SEAL_TUNED", 1), ("ITM_MAT_GROLLBASALT", 2)]}[s["Name"]]
        add(s["Name"], "Werkbank" if s["Tier"] != "3" else "Akademie-Labor (Dorunsruh)", ing,
            {"1": "Start", "2": "Akkord 2", "3": "Akkord 5"}.get(s["Tier"], "Akkord 2"), "Siegel")
    for t in rows("Data/Items/Traps.csv"):
        add(t["Name"], "Lagerfeuer", [(mat("Wood", 1, t["Name"]), 3), (mat("Herb", 2, t["Name"]), 2),
                                      (mat("Crystal", 1, t["Name"]), 1)], "Kodex-Stufe 2 einer passenden Art", "Falle")
    cons_ing = {"ITM_CON_HEAL_1": [("ITM_MAT_FERNFIBER", 2), ("ITM_MAT_LINDBLOSSOM", 1)],
                "ITM_CON_HEAL_2": [("ITM_MAT_PEAKGENTIAN", 2), ("ITM_MAT_SWAMPMYRTLE", 1)],
                "ITM_CON_HEAL_3": [("ITM_MAT_ICEBLOOM", 1), ("ITM_MAT_OASISMINT", 2), ("ITM_MAT_CRYSTALMOSS", 1)],
                "ITM_CON_HEAL_ALL": [("ITM_CON_HEAL_2", 2), ("ITM_MAT_FIRELILY", 1)],
                "ITM_CON_REVIVE": [("ITM_MAT_WISPMOSS", 2), ("ITM_MAT_MOSSPEARL", 1)],
                "ITM_CON_CLEANSE": [("ITM_MAT_SALTWORT", 2), ("ITM_MAT_FOGPEARL", 1)],
                "ITM_CON_STAMINA": [("ITM_MAT_PEAKGENTIAN", 1), ("ITM_MAT_MOUNTAINPINE", 1)],
                "ITM_CON_WARM": [("ITM_MAT_FIRELILY", 1), ("ITM_MAT_POLARLICHEN", 1)],
                "ITM_CON_SENSE": [("ITM_MAT_RUINVINE", 1), ("ITM_MAT_SOUNDRESIN", 1)],
                "ITM_CON_REPEL": [("ITM_MAT_PEATCOAL", 2), ("ITM_MAT_SWAMPMYRTLE", 1)],
                "ITM_CON_WANDELKLANG": [("ITM_MAT_GLYPHCRYSTAL", 1), ("ITM_EMAT_ARCANE", 3)],
                "ITM_CON_KLANGSALZ": [("ITM_MAT_SULFURCRYSTAL", 2), ("ITM_MAT_NACRE", 1)],
                "ITM_CON_WESENSKLANG": [("ITM_MAT_RESONANCECRYSTAL", 2), ("ITM_EMAT_SPIRIT", 5), ("ITM_MAT_SKYGLASS", 1)]}
    for k, v in cons_ing.items():
        add(k, "Lagerfeuer" if k.startswith("ITM_CON_HEAL_1") or k in ("ITM_CON_STAMINA", "ITM_CON_REPEL") else "Werkbank", v,
            "Start" if k in ("ITM_CON_HEAL_1", "ITM_CON_STAMINA") else ("Endgame" if k == "ITM_CON_WESENSKLANG" else "Rezept (Händler/Quest)"), "Verbrauchsgut")
    lures = {r["Name"]: r for r in rows("Data/Items/Lures.csv")}
    meals = ["ITM_FOODC_STEW", "ITM_FOODC_FISHPIE", "ITM_FOODC_HONEYCAKE", "ITM_FOODC_SPICEBREAD", "ITM_FOODC_ICEJELLY",
             "ITM_FOODC_EMBERSOUP", "ITM_FOODC_MOSSBUN", "ITM_FOODC_DATEROLL", "ITM_FOODC_KELPWRAP", "ITM_FOODC_CHEESEPLATE",
             "ITM_FOODC_CLOUDTART", "ITM_FOODC_FEAST"]
    foods = [n for n, r in lures.items() if r["Kind"] == "Food"]
    for i, m in enumerate(meals):
        ing = [(foods[i % len(foods)], 2), (foods[(i * 5 + 3) % len(foods)], 1), (mat("Herb", 1 + i % 3, m), 1)]
        if m == "ITM_FOODC_FEAST":
            ing = [("ITM_FOODC_STEW", 1), ("ITM_FOODC_FISHPIE", 1), ("ITM_FOODC_HONEYCAKE", 1)]
        add(m, "Lagerfeuer", ing, "Rezeptbuch (Gasthäuser, K42)", "Gericht")
    for hi in rows("Data/Items/HeldItems.csv"):
        n = hi["Name"]
        if n.startswith("ITM_HELD_TONE_"):
            t = n.split("_")[-1]
            add(n, "Werkbank", [(f"ITM_EMAT_{t}", 6), ("ITM_MAT_QUARTZSHARD", 2), ("ITM_MAT_COPPERORE", 2)], "Akkord 3", "Halteitem")
        elif n in ("ITM_HELD_WESENSBAND", "ITM_HELD_STIMMBAND", "ITM_HELD_BONDRIBBON"):
            add(n, "Hain-Werkstatt", [("ITM_EMAT_ECHOWOOL", 4), (mat("Herb", 2, n), 3)], "Zucht freigeschaltet" if n != "ITM_HELD_BONDRIBBON" else "Bindungsstufe 4 mit einem Echo", "Halteitem")
        else:
            add(n, "Werkbank", [(mat("Ore", 3, n), 3), (mat("Crystal", 3, n), 2), (f"ITM_EMAT_{TYPES[h(n) % 15][0].upper()}", 4)], "Akkord 4", "Halteitem")
    for b in rows("Data/Items/BreedingItems.csv"):
        if b["Name"] in ("ITM_BREED_FERNKLANG", "ITM_BREED_WESENSBAND", "ITM_BREED_STIMMBAND"):
            continue
        ing = {"ITM_BREED_ERBKLANG": [("ITM_MAT_GLYPHCRYSTAL", 1), ("ITM_EVO_<TYP>", 1), ("ITM_EMAT_SOUND", 3)],
               "ITM_BREED_KEIMWAERME": [("ITM_MAT_EMBERSAND", 2), ("ITM_EMAT_ECHOWOOL", 1)],
               "ITM_BREED_KLANGSTIMMUNG": [("ITM_MAT_STARMETAL", 2), ("ITM_MAT_RESONANCECRYSTAL", 3), ("ITM_EMAT_STILLSHARD", 2)]}[b["Name"]]
        add(b["Name"], "Hain-Werkstatt" if b["Name"] != "ITM_BREED_KLANGSTIMMUNG" else "Akademie-Labor (Dorunsruh)", ing,
            "Endgame" if b["Name"] == "ITM_BREED_KLANGSTIMMUNG" else "Zucht freigeschaltet", "Zucht")
    for e in rows("Data/Items/EvolutionItems.csv"):
        if e["Kind"] != "Overtone":
            continue
        t = e["Type"].split(".")[1].upper()
        add(e["Name"], "Akademie-Labor (Dorunsruh)", [(f"ITM_EMAT_{t}", 5), (mat("Crystal", 3, e["Name"]), 2)], "Akkord 4", "Evolution")
    with open(ROOT / "Data/Items/Recipes.csv", "w", newline="", encoding="utf-8") as f:
        f.write("# Rezepte (K41 §3). Ingredients: ID×Menge; <TYP> = Variante je Klangfarbe. Herstellung sofort (DR-23).\n")
        w = csv.writer(f)
        w.writerow(["Name", "Output", "Category", "Station", "Ingredients", "Unlock"])
        w.writerows(rec)
    print(f"Echo-Materialien {len(emat)}, Verbrauchsgüter/Gerichte {len(cons) + len(cook)}, Rezepte {len(rec)}")


if __name__ == "__main__":
    main()


def recipe_table():
    names = {}
    for t in ["Resources", "EchoMaterials", "Consumables", "Lures", "Seals", "WardenGear", "HeldItems", "EvolutionItems", "Traps", "BreedingItems"]:
        for r in rows(f"Data/Items/{t}.csv"):
            names.setdefault(r["Name"], r["DisplayName"])
    out = ["| Rezept | Ergebnis | Kategorie | Station | Zutaten | Freischaltung |", "|---|---|---|---|---|---|"]
    for r in rows("Data/Items/Recipes.csv"):
        ing = ", ".join(f"{names.get(n, n.replace('ITM_EMAT_<TYP>', 'Klangsplitter (Typ)').replace('ITM_EVO_<TYP>', 'Obertonkristall (Typ)'))} ×{q}"
                        for n, q in (p.split("×") for p in r["Ingredients"].split(";")))
        out.append(f"| {r['Name']} | **{names.get(r['Output'], r['Output'])}** | {r['Category']} | {r['Station']} | {ing} | {r['Unlock']} |")
    return "\n".join(out)
