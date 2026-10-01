#!/usr/bin/env python3
"""Referenzmodell der Resonanzbindung (K36, löst Q12). Ganzzahlig, deterministisch – kein Erfolgswurf (DR-03, DR-07).

Resonanzwert R (0–1000) entsteht aus Spielerentscheidungen; das Timing entscheidet nur, OB angeschlagen wird.
Bindung gelingt, wenn Timing ≥ Gut UND R ≥ Schwelle(Seltenheit) − Siegelbonus.
"""
RARITY_THRESHOLD = {"Common": 150, "Uncommon": 250, "Rare": 400, "VeryRare": 550, "Alpha": 600, "Legendary": 750, "Mythical": 750}
KODEX_BONUS = [0, 60, 120, 180, 240]          # je Kodex-Stufe 0–4 (DR-01: > Siegelbonus max. 80)
GOOD_MIN, GOOD_MAX = 160, 400                 # ms, Q12
PERFECT_SHARE, PERFECT_MIN = 250, 60          # ‰ des Gut-Fensters, ms


def resonance(kodex=0, lure="none", approach=0, trap=0, battle_hp_lost=0, status=False, time_match=False,
              level_gap=0, alpha=False):
    """lure: none | wrong | category | favorite. approach: 0–150 (Schleichen, Wind, Deckung).
    battle_hp_lost: ‰ der HP, die das Echo im Kampf verlor (Kampfweg). level_gap: Echo-Level − höchstes Chor-Level."""
    r = KODEX_BONUS[kodex]
    r += {"none": 0, "wrong": -50, "category": 100, "favorite": 200}[lure]
    r += max(0, min(150, approach))
    r += trap
    r += min(250, battle_hp_lost * 300 // 1000)
    r += 50 if status else 0
    r += 50 if time_match else 0
    r -= max(0, level_gap - 10) * 10
    return max(0, min(1000, r))


def window_ms(r, temperament_permille=1000, seal_window=1000, generous=False):
    good = GOOD_MIN + (GOOD_MAX - GOOD_MIN) * r // 1000
    good = good * temperament_permille // 1000 * seal_window // 1000
    if generous:
        good = good * 1750 // 1000
    perfect = max(PERFECT_MIN, good * PERFECT_SHARE // 1000)
    return good, perfect


def outcome(r, rarity, seal_bonus, timing):
    """timing: perfect | good | miss."""
    need = RARITY_THRESHOLD[rarity] - seal_bonus
    if timing == "miss":
        return "Verfehlt"
    if timing == "perfect" and r >= need - 100:
        return "Einklang"            # Perfekt verzeiht 100 Resonanz
    if r >= need:
        return "Bindung" if timing == "good" else "Einklang"
    return "Annäherung"               # Teilerfolg: +100 R, Versuch verbraucht


def scenarios():
    rows = [
        ("Prolog: Wisplet, Erstresonanz", dict(kodex=0, lure="none", approach=100, time_match=True), "Common", 0, 1100),
        ("Häufiges Echo, nichts vorbereitet", dict(kodex=0, lure="none", approach=50), "Common", 0, 1000),
        ("Häufiges Echo, Lieblingsfutter", dict(kodex=1, lure="favorite", approach=80), "Common", 0, 1000),
        ("Seltenes Echo, nur Kampf (50 % HP)", dict(kodex=0, battle_hp_lost=500, status=True), "Rare", 0, 1000),
        ("Seltenes Echo, Kampf + Meistersiegel", dict(kodex=0, battle_hp_lost=500, status=True), "Rare", 80, 1000),
        ("Seltenes Echo, Kodex 3 + Lieblingsköder", dict(kodex=3, lure="favorite", approach=100), "Rare", 0, 1000),
        ("Sehr selten, Kodex 4 + Falle + Zeit", dict(kodex=4, lure="category", approach=120, trap=150, time_match=True), "VeryRare", 40, 1000),
        ("Alpha, Kampf + Kodex 2 + Köder", dict(kodex=2, lure="favorite", battle_hp_lost=600, status=True), "Alpha", 80, 900),
        ("Ursprungsstimme (Stimmsiegel)", dict(kodex=4, lure="favorite", approach=150, battle_hp_lost=850, status=True, time_match=True), "Legendary", 0, 1000),
        ("Zu hohes Level (+18)", dict(kodex=2, lure="favorite", approach=100, level_gap=18), "Uncommon", 0, 1000),
    ]
    out = ["| Szenario | R | Schwelle − Siegel | Gut-Fenster | Perfekt | bei „Gut“ | bei „Perfekt“ |", "|---|---|---|---|---|---|---|"]
    for name, kw, rar, seal, temp in rows:
        r = resonance(**kw)
        g, p = window_ms(r, temp)
        out.append(f"| {name} | {r} | {RARITY_THRESHOLD[rar] - seal} | {g} ms | {p} ms | {outcome(r, rar, seal, 'good')} | {outcome(r, rar, seal, 'perfect')} |")
    return "\n".join(out)


def bond_sheet():
    import csv, pathlib
    root = pathlib.Path(__file__).resolve().parents[2]
    rows = lambda p: list(csv.DictReader(l for l in open(root / p, encoding="utf-8") if not l.startswith("#")))
    sp = list(csv.DictReader(open(root / "Data/Echos/Species.csv", encoding="utf-8")))
    lures = {r["Name"]: r["DisplayName"] for r in rows("Data/Items/Lures.csv")}
    traps = rows("Data/Items/Traps.csv")
    sizes = ["XS", "S", "M", "L", "XL", "XXL"]
    act = {"Diurnal": "Nacht", "Nocturnal": "Mittag", "Crepuscular": "Mittag/Nacht", "Cathemeral": "–"}
    rar = {"Common": "Häufig", "Uncommon": "Ungew.", "Rare": "Selten", "VeryRare": "Sehr selten", "Legendary": "Stimme", "Mythical": "Mythisch"}

    def ok(s, cond):
        for c in cond.split("|"):
            k, v = c.split(":")
            if k == "Trait" and f"Behavior.{v}" in s["Traits"].split("|"):
                return True
            if k == "Size" and sizes.index(s["SizeClass"]) >= sizes.index(v.rstrip("+")):
                return True
        return False
    out = ["| # | Art | Seltenheit | Schwelle | Lieblingsköder | passende Fallen | Ruhephase (+50) |", "|---|---|---|---|---|---|---|"]
    for s in sp:
        if "Spawn.None" in s["SpawnConditions"] and s["LineKind"] not in ("Legendary", "Mythical"):
            continue   # nur durch Evolution/Zucht – keine Wildbindung
        t = ", ".join(r["DisplayName"] for r in traps if ok(s, r["Condition"])) or "–"
        th = RARITY_THRESHOLD.get(s["Rarity"], 0)
        out.append(f"| {int(s['KodexNumber']):03d} | {s['DisplayName']} | {rar.get(s['Rarity'], s['Rarity'])} | {th} | "
                   f"{lures.get(s['BondLure'], s['BondLure'])} | {t} | {act.get(s['Activity'].split('.')[-1], '–')} |")
    return "\n".join(out)


if __name__ == "__main__":
    assert window_ms(0) == (160, 60) and window_ms(1000) == (400, 100)
    assert outcome(150, "Common", 0, "good") == "Bindung"
    assert outcome(300, "Rare", 0, "perfect") == "Einklang" and outcome(299, "Rare", 0, "perfect") == "Annäherung"
    print(scenarios())
