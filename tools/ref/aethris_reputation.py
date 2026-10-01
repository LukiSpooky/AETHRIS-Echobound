#!/usr/bin/env python3
"""Ruf-Referenzmodell (K47): Rang je Fraktion über die Spielabschnitte, Quellenanteile, Ziel-Checks."""
import csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


RANKS = rows("Data/Factions/ReputationRanks.csv")
THR = [int(r["Threshold"]) for r in RANKS]
FACTIONS = ["F01", "F02", "F03", "F04", "F05"]
SHORT = {"F01": "Akademie", "F02": "Kontor", "F03": "Wildwacht", "F04": "Freie Stimmen", "F05": "Orden"}

# Abschnitte: (Name, Stunden, Ruf/h je Fraktion bei typischer Spielweise)
PHASES = [
    ("Prolog", 3, {"F01": 0, "F02": 5, "F03": 20, "F04": 0, "F05": 0}),
    ("Akt I", 15, {"F01": 18, "F02": 20, "F03": 32, "F04": 12, "F05": 0}),
    ("Akt II", 20, {"F01": 70, "F02": 75, "F03": 85, "F04": 95, "F05": 0}),
    ("Akt III", 12, {"F01": 80, "F02": 80, "F03": 80, "F04": 80, "F05": 60}),
    ("Endgame 1–20 h", 20, {"F01": 70, "F02": 70, "F03": 70, "F04": 70, "F05": 80}),
    ("Endgame 20–40 h", 20, {"F01": 60, "F02": 60, "F03": 60, "F04": 60, "F05": 70}),
    ("Endgame 40–60 h", 20, {"F01": 50, "F02": 50, "F03": 50, "F04": 50, "F05": 60}),
]

# Hauptquest-Boni (K47 §4.2): Quest → {Fraktion: Punkte}; kanonische Wahl (Kisten geliefert, Unterschlupf FS)
MQ_BONUS = {
    "Prolog": {"MQ_P03": {"F03": 100}},
    "Akt I": {"MQ_A1_01": {"F03": 150}, "MQ_A1_04": {"F04": 150}, "MQ_A1_05": {"F02": 150},
              "MQ_A1_07": {"F01": 150}, "MQ_A1_09": {"F03": 100}},
    "Akt II": {"MQ_A2_01": {"F03": 200}, "MQ_A2_03": {"F04": 300, "F02": 200}, "MQ_A2_04": {"F03": 100},
               "MQ_A2_08": {"F04": 200}, "MQ_A2_09": {"F01": 200}, "MQ_A2_11": {"F05": 100}},
    "Akt III": {"MQ_A3_01": {"F01": 100}, "MQ_A3_04": {"F05": 200, "F03": 100, "F04": 100},
                "MQ_A3_05": {"F02": 150}, "MQ_A3_09": {"F01": 200, "F02": 200, "F03": 200, "F04": 200, "F05": 200}},
}


def rank_of(points):
    r = 1
    for i, t in enumerate(THR, 1):
        if points >= t:
            r = i
    return r


def timeline():
    pts = {f: 0 for f in FACTIONS}
    out = []
    for name, hours, rate in PHASES:
        for f in FACTIONS:
            pts[f] += hours * rate[f]
        for q, bonus in MQ_BONUS.get(name, {}).items():
            for f, v in bonus.items():
                pts[f] += v
        out.append((name, dict(pts)))
    return out


def timeline_table():
    head = "| Abschnitt | " + " | ".join(SHORT[f] for f in FACTIONS) + " |"
    lines = [head, "|---|" + "---|" * len(FACTIONS)]
    for name, pts in timeline():
        cells = [f"{pts[f]:,}".replace(",", ".") + f" (R{rank_of(pts[f])})" for f in FACTIONS]
        lines.append(f"| {name} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def checks():
    """Zielprüfungen aus K40 (Blaupausen), K29 (Tutoren), K42 (Rabatte)."""
    t = dict(timeline())
    res = []
    def chk(desc, ok):
        res.append(f"| {desc} | {'✓' if ok else '✗'} |")
    chk("Akademie, Kontor, Wildwacht Rang 2 am Ende von Akt I (Blaupausen III)", all(rank_of(t["Akt I"][f]) >= 2 for f in ("F01", "F02", "F03")))
    chk("Freie Stimmen Rang 2 spätestens Mitte Akt II", rank_of(t["Akt I"]["F04"] + 10 * 95) >= 2)
    chk("F01–F04 Rang 4 am Ende von Akt II (Blaupausen IV, Tutoren Stufe 2)", all(rank_of(t["Akt II"][f]) >= 4 for f in FACTIONS[:4]))
    chk("Orden Rang 3 am Ende von Akt III (Ordenstutoren Stufe 1)", rank_of(t["Akt III"]["F05"]) >= 3)
    chk("Keine Fraktion Rang 6 vor dem Endgame", all(rank_of(t["Akt III"][f]) < 6 for f in FACTIONS))
    chk("Mindestens drei Fraktionen Rang 6 nach 60 h Endgame (typisch)", sum(rank_of(t["Endgame 40–60 h"][f]) >= 6 for f in FACTIONS) >= 3)
    chk("Fokus: F01–F04 Rang 6 in ≤ 25 h Endgame (150 Ruf/h)", all(focus_hours(f) <= 25 for f in FACTIONS[:4]))
    chk("Fokus: Orden Rang 6 in ≤ 40 h Endgame (später Start, ADR-180)", focus_hours("F05") <= 40)
    return "| Prüfung | Ergebnis |\n|---|---|\n" + "\n".join(res)


FOCUS_RATE = 150   # Ruf/h bei gezieltem Spiel für eine Fraktion (Aufträge + Kette + Fraktionsquellen)


def focus_hours(f):
    start = dict(timeline())["Akt III"][f]
    return max(0, -(-(THR[-1] - start) // FOCUS_RATE))


def focus_table():
    lines = ["| Fraktion | Ruf am Ende von Akt III | Fehlend bis Rang 6 | Stunden bei Fokus (150 Ruf/h) |", "|---|---|---|---|"]
    t = dict(timeline())["Akt III"]
    for f in FACTIONS:
        lines.append(f"| {SHORT[f]} | {t[f]:,} | {max(0, THR[-1] - t[f]):,} | {focus_hours(f)} |".replace(",", "."))
    return "\n".join(lines)


def mq_table():
    lines = ["| Abschnitt | Quest | Fraktion | Ruf |", "|---|---|---|---|"]
    for ph, qs in MQ_BONUS.items():
        for q, b in qs.items():
            for f, v in b.items():
                lines.append(f"| {ph} | {q} | {SHORT[f]} | +{v} |")
    return "\n".join(lines)


if __name__ == "__main__":
    print(timeline_table()); print(); print(checks())
