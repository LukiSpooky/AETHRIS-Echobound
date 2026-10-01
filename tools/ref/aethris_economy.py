#!/usr/bin/env python3
"""Wirtschaftsmodell (K42): Itemwerte, Preise, Belohnungsskala, Einnahmen/Ausgaben-Simulation je Akt.

build   -> schreibt Data/Economy/ItemPrices.csv (Wert, Kaufpreis, Verkaufspreis, Händlerkategorie)
report  -> Kennzahlen-Tabellen
Alle Werte ganzzahlig in Sol (◎).
"""
import csv, math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
RES_BASE = {1: 12, 2: 25, 3: 45, 4: 80, 5: 140}
RARITY = {"Common": 100, "Uncommon": 150, "Rare": 250}
CRAFT_MARKUP = 125        # % Wertzuwachs durch Herstellung
SELL_RATE = 35            # % des Werts beim Verkauf
FIXED = {"ITM_SEAL_BASIC": 150, "ITM_SEAL_TUNED": 450, "ITM_SEAL_MASTER": 1200}


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


def reward_scale_permille(level):
    """RewardScale(L) = (L + 10) / 20 – 1,0 bei Zonenband-Mitte 10 (K13 §4)."""
    return (level + 10) * 1000 // 20


def item_values():
    v = {}
    for r in rows("Data/Items/Resources.csv"):
        v[r["Name"]] = RES_BASE[int(r["Tier"])] * RARITY.get(r["Rarity"], 100) // 100
    for r in rows("Data/Items/EchoMaterials.csv"):
        v[r["Name"]] = 30 if r["Name"].startswith("ITM_EMAT_") and r["Type"] not in ("–",) and "STILL" not in r["Name"] else 60
    v["ITM_EMAT_STILLSHARD"] = 250
    for r in rows("Data/Items/Lures.csv"):
        v[r["Name"]] = 40 if r["Kind"] == "Food" else 180
    v.update(FIXED)
    v["ITM_EMAT_<TYP>"] = 30
    v["ITM_EVO_<TYP>"] = 600
    recipes = rows("Data/Items/Recipes.csv")
    for _ in range(6):                       # Fixpunkt über Rezeptketten
        for r in recipes:
            if r["Output"] in FIXED:
                continue
            total = 0
            ok = True
            for part in r["Ingredients"].split(";"):
                n, q = part.split("×")
                if n not in v:
                    ok = False
                    break
                total += v[n] * int(q)
            if ok:
                v[r["Output"]] = total * CRAFT_MARKUP // 100
    for r in rows("Data/Items/EvolutionItems.csv"):
        v.setdefault(r["Name"], 900)
    for r in rows("Data/Items/Klangschriften.csv"):
        v[r["Name"]] = 0                     # nicht handelbar (CANON §18)
    for r in rows("Data/Items/WardenGear.csv"):
        v.setdefault(r["Name"], 0)           # Stufe I / Sättel: Story
    for n in ("ITM_SEAL_VOICE", "ITM_SEAL_STAR"):
        v[n] = 0
    return v


SHOP_CAT = [("ITM_MAT_", "Material"), ("ITM_EMAT_", "Material"), ("ITM_FOOD_", "Food"), ("ITM_FOODC_", "Food"),
            ("ITM_LURE_", "General"), ("ITM_SEAL_", "General"), ("ITM_TRAP_", "General"), ("ITM_CON_HEAL", "Heal"),
            ("ITM_CON_REVIVE", "Heal"), ("ITM_CON_CLEANSE", "Heal"), ("ITM_CON_", "General"), ("ITM_GEAR_", "Gear"),
            ("ITM_HELD_", "Rare"), ("ITM_BREED_", "Faction"), ("ITM_EVO_", "Rare"), ("ITM_KS_", "Scripts")]
NOT_SOLD = ("ITM_SEAL_VOICE", "ITM_SEAL_STAR", "ITM_CON_WESENSKLANG", "ITM_BREED_KLANGSTIMMUNG", "ITM_EMAT_STILLSHARD")


def build():
    v = item_values()
    out = []
    for n, val in sorted(v.items()):
        if "<TYP>" in n:
            continue
        cat = next((c for p, c in SHOP_CAT if n.startswith(p)), "General")
        sold = val > 0 and n not in NOT_SOLD and not n.startswith("ITM_KS_") and not (n.startswith("ITM_GEAR_") and n.endswith(("_4", "_5")))
        buy = int(math.ceil(val / 5.0) * 5) if sold else 0
        sell = val * SELL_RATE // 100 if val > 0 and not n.startswith("ITM_KS_") and n not in ("ITM_SEAL_VOICE", "ITM_SEAL_STAR") else 0
        out.append([n, val, buy, sell, cat if sold else "–"])
    with open(ROOT / "Data/Economy/ItemPrices.csv", "w", newline="", encoding="utf-8") as f:
        f.write("# Itempreise (K42 §3): Wert aus Ressourcenstufe bzw. Rezeptkette (×1,25); Kauf = Wert (auf 5 gerundet), Verkauf = 35 %. Buy 0 = nicht käuflich.\n")
        w = csv.writer(f)
        w.writerow(["Name", "Value", "BuyPrice", "SellPrice", "ShopCategory"])
        w.writerows(out)
    print(f"{len(out)} Preise")


# ── Einnahmen/Ausgaben je Akt ───────────────────────────────────────────────────
ACTS = [  # Name, Stunden, Ø Zonenlevel, Wärter-Kämpfe/h, Aufträge/h, Kisten/h, Verkauf/h (◎)
    ("Prolog", 3, 4, 1, 0, 3, 50),
    ("Akt I", 15, 17, 3, 1.5, 4, 250),
    ("Akt II", 20, 40, 3, 1.5, 4, 500),
    ("Akt III", 12, 60, 3, 1.5, 4, 800),
    ("Endgame (je 10 h)", 10, 85, 3, 2, 3, 1200),
]
SPEND = [  # Name, Akt-Index, Kosten (◎) – notwendig/empfohlen
    ("Siegel (Ø 1,6 je Bindung, 25 Bindungen/Akt)", None, None),
]


def trainer_sol(level, cls=1000):
    return level * 25 * cls // 1000


def act_report():
    out = ["| Abschnitt | Spielzeit | Wärterkämpfe | Aufträge | Kisten | Verkauf | Arenen/Quests | **Summe** | je Stunde |", "|---|---|---|---|---|---|---|---|---|"]
    arena = {"Prolog": 0, "Akt I": 4 * 2000, "Akt II": 4 * 5000, "Akt III": 2 * 12000, "Endgame (je 10 h)": 0}
    quests = {"Prolog": 800, "Akt I": 9000, "Akt II": 22000, "Akt III": 20000, "Endgame (je 10 h)": 15000}
    totals = {}
    for name, h, lv, tb, ct, ch, sell in ACTS:
        rs = reward_scale_permille(lv)
        t = int(h * tb * trainer_sol(lv))
        c = int(h * ct * 150 * rs / 1000)
        k = int(h * ch * 60 * rs / 1000)
        s = int(h * sell)
        a = arena[name] + quests[name]
        tot = t + c + k + s + a
        totals[name] = tot
        out.append(f"| {name} | {h} h | {t:,} | {c:,} | {k:,} | {s:,} | {a:,} | **{tot:,}** | {tot // h:,} |".replace(",", "."))
    return "\n".join(out), totals


def spend_report():
    v = item_values()
    seals = [("Klangsiegel", 150), ("Gestimmtes Siegel", 450), ("Meistersiegel", 1200)]
    rows_ = [
        ("Prolog", "Siegel, Tinkturen", 10 * 150 + 10 * v.get("ITM_CON_HEAL_1", 40)),
        ("Akt I", "25 Bindungen × 1,6 Siegel (Klang/Gestimmt), Ausrüstung II–III (Material-Zukauf 50 %), Heilmittel, Rezeptbücher ×6, Gerichte, Hain-Ausbau 2 (×4)",
         int(40 * 300 + 0.5 * sum(v.get(f"ITM_GEAR_{s}_{t}", 0) for s in ("RESONATOR", "GLIDER", "BOOTS", "CLOAK", "BAG", "TOOL", "LANTERN") for t in (2, 3)) + 4 * 2000 + 15 * 200 + 6 * 500 + 3000)),
        ("Akt II", "40 Bindungen (Gestimmt/Meister), Ausrüstung IV (Material 50 %), Tutoren ×4, Hain 3 (×5), Stimmsteine",
         int(64 * 800 + 0.5 * sum(v.get(f"ITM_GEAR_{s}_4", 0) for s in ("RESONATOR", "GLIDER", "BOOTS", "CLOAK", "BAG", "LENS", "TOOL", "LANTERN", "MASK")) + 4 * 2750 + 5 * 6000 + 6 * v.get("ITM_HELD_TONE_EMBER", 500))),
        ("Akt III", "25 Bindungen (Meister), Ausrüstung V für 4 Kernplätze (Material 50 %), Tutoren ×4, Hain 4 (×5)",
         int(40 * 1200 + 0.5 * sum(v.get(f"ITM_GEAR_{s}_5", 0) for s in ("RESONATOR", "GLIDER", "BOOTS", "CLOAK")) + 4 * 2750 + 5 * 15000)),
        ("Endgame (je 10 h)", "Hain 5 (×2), Erbklang ×20, Klangbad, Tutoren-Rest", int(2 * 30000 + 20 * v.get("ITM_BREED_ERBKLANG", 2000) + 5 * 1500 + 6 * 2750)),
    ]
    out = ["| Abschnitt | Typische Ausgaben | Bedarf (◎) |", "|---|---|---|"]
    need = {}
    for n, d, c in rows_:
        need[n] = c
        out.append(f"| {n} | {d} | {c:,} |".replace(",", "."))
    return "\n".join(out), need


def balance():
    a, inc = act_report()
    b, need = spend_report()
    out = ["| Abschnitt | Einnahmen | Bedarf | Quote | kumuliert (inkl. 1.000 ◎ Start) | Bewertung |", "|---|---|---|---|---|---|"]
    ci, cn = 1000, 0
    for k in inc:
        q = inc[k] * 100 // max(1, need[k])
        ci += inc[k]
        cn += need[k]
        cq = ci * 100 // max(1, cn)
        verdict = "knapp – Entscheidungen nötig" if cq < 110 else ("gesund" if cq <= 170 else "Überschuss → Senken nötig")
        out.append(f"| {k} | {inc[k]:,} | {need[k]:,} | {q} % | {cq} % | {verdict} |".replace(",", "."))
    return "\n".join(out)


def price_sample():
    p = {r["Name"]: r for r in rows("Data/Economy/ItemPrices.csv")}
    names = {}
    for t in ["Resources", "EchoMaterials", "Consumables", "Lures", "Seals", "WardenGear", "HeldItems", "EvolutionItems", "Traps", "BreedingItems"]:
        for r in rows(f"Data/Items/{t}.csv"):
            names.setdefault(r["Name"], r["DisplayName"])
    pick = ["ITM_MAT_OAKWOOD", "ITM_MAT_KHARSIRON", "ITM_MAT_SUNGLASS", "ITM_MAT_GLACIERQUARTZ", "ITM_MAT_STARMETAL",
            "ITM_EMAT_EMBER", "ITM_FOOD_DATES", "ITM_LURE_STARCHIME", "ITM_SEAL_BASIC", "ITM_SEAL_TUNED", "ITM_SEAL_MASTER",
            "ITM_TRAP_REST", "ITM_CON_HEAL_1", "ITM_CON_HEAL_3", "ITM_CON_REVIVE", "ITM_CON_WANDELKLANG", "ITM_FOODC_FEAST",
            "ITM_GEAR_GLIDER_2", "ITM_GEAR_GLIDER_3", "ITM_GEAR_RESONATOR_3", "ITM_GEAR_TOOL_4", "ITM_GEAR_LENS_5",
            "ITM_HELD_TONE_EMBER", "ITM_HELD_TAKTRING", "ITM_EVO_EMBER", "ITM_BREED_ERBKLANG"]
    out = ["| Gegenstand | Wert | Kauf | Verkauf | Händler |", "|---|---|---|---|---|"]
    for n in pick:
        if n in p:
            r = p[n]
            out.append(f"| {names.get(n, n)} | {int(r['Value']):,} | {('–' if r['BuyPrice'] == '0' else format(int(r['BuyPrice']), ','))} | {int(r['SellPrice']):,} | {r['ShopCategory']} |".replace(",", "."))
    return "\n".join(out)


def price_full():
    p = rows("Data/Economy/ItemPrices.csv")
    names = {}
    for t in ["Resources", "EchoMaterials", "Consumables", "Lures", "Seals", "WardenGear", "HeldItems", "EvolutionItems", "Traps", "BreedingItems", "Klangschriften"]:
        for r in rows(f"Data/Items/{t}.csv"):
            names.setdefault(r["Name"], r["DisplayName"])
    out = ["| ID | Gegenstand | Wert | Kauf | Verkauf | Händler |", "|---|---|---|---|---|---|"]
    for r in p:
        out.append(f"| {r['Name']} | {names.get(r['Name'], r['Name'])} | {int(r['Value']):,} | {('–' if r['BuyPrice'] == '0' else format(int(r['BuyPrice']), ','))} | {int(r['SellPrice']):,} | {r['ShopCategory']} |".replace(",", "."))
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        build()
    else:
        print(act_report()[0]); print(); print(spend_report()[0]); print(); print(balance())
