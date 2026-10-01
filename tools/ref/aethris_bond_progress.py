#!/usr/bin/env python3
"""Bindungsfortschritt (K37 §4): Simulation typischer Spielweisen → Spielstunden bis zu jeder Bindungsstufe."""
import csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


TIERS = [(int(r["MinValue"]), r["DisplayName"]) for r in rows("Data/Echos/BondTiers.csv")]
ACT = {r["Name"]: r for r in rows("Data/Echos/BondActions.csv")}

# Handlungen je Spielstunde für drei Spielstile (Begleiter-Echo im Chor)
STYLES = {
    "Kämpfer (wenig Pflege)": {"BA_BATTLE_WIN": 8, "BA_WALK": 6, "BA_FEED": 0.5, "BA_PET": 0.3, "BA_PLAY": 0, "BA_PRAISE": 1, "BA_TRAIN": 0.3, "BA_REST": 1},
    "Ausgewogen": {"BA_BATTLE_WIN": 5, "BA_WALK": 6, "BA_FEED": 1.5, "BA_PET": 1, "BA_PLAY": 0.5, "BA_PRAISE": 2, "BA_TRAIN": 0.5, "BA_REST": 1},
    "Pfleger (Lager-Momente)": {"BA_BATTLE_WIN": 3, "BA_WALK": 5, "BA_FEED": 3, "BA_PET": 1, "BA_PLAY": 1.5, "BA_PRAISE": 3, "BA_TRAIN": 1, "BA_REST": 1.5},
}
HOURS_PER_DAY = 1.5   # Spielstunden je Spieltag (Uhr K15: 1 Spieltag ≈ 48 Echtzeit-Min.; hier Spielzeit gesamt)


def hours_to_tiers(style, start=50, favorite_share=0.5):
    v, h, out = start, 0.0, {}
    day_acc = {k: 0 for k in ACT}
    t_day = 0.0
    while v < 1000 and h < 400:
        h += 0.1
        t_day += 0.1
        if t_day >= HOURS_PER_DAY:
            t_day = 0
            day_acc = {k: 0 for k in ACT}
        for k, per_h in STYLES[style].items():
            a = ACT[k]
            gain = int(a["Gain"]) + (int(a["FavoriteBonus"]) * favorite_share)
            g = gain * per_h * 0.1
            cap = int(a["DailyCap"])
            g = max(0, min(g, cap - day_acc[k]))
            day_acc[k] += g
            v += g
        for mv, name in TIERS:
            if v >= mv and name not in out:
                out[name] = h
    return out


def table():
    out = ["| Spielstil | " + " | ".join(n for _, n in TIERS[1:]) + " |", "|---|" + "---|" * (len(TIERS) - 1)]
    for s in STYLES:
        r = hours_to_tiers(s)
        out.append(f"| {s} | " + " | ".join(f"{r.get(n, 0):.1f} h".replace(".", ",") for _, n in TIERS[1:]) + " |")
    return "\n".join(out)


if __name__ == "__main__":
    print(table())
