#!/usr/bin/env python3
"""Fähigkeits-Bibliothek (K28): Effekt-DSL, Machtbudget, Zeitkosten, Beschreibungen, Validierung.

Effekt-DSL (CANON §97):  Effekt := Name "(" Arg ("," Arg)* ")" ; Liste := Effekt (";" Effekt)*
Beispiel: "Status(Brand,300);Stage(Self,Attack,+1)"

Budget (Machtpunkte, MP):
  V = Schaden + Σ Effektwerte
  Schaden = Stärke × Genauigkeit/1000 × Zielfaktor × mittlere Trefferzahl
  Zeitkosten = clamp(round10(20 + V), 50, 200)   (100 = Standardzug; Verzögerung → K31)
Alle Werte ganzzahlig/Promille, damit C++ (`FAbilityBudget`) bitgleich rechnet.
"""
from __future__ import annotations
import csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ABIL = ROOT / "Data/Abilities/Abilities.csv"
STATUS = ROOT / "Data/Abilities/StatusEffects.csv"

TYPES = ["Ember", "Tide", "Stone", "Storm", "Bloom", "Frost", "Void", "Light", "Venom", "Metal", "Spirit",
         "Crystal", "Sound", "Gravity", "Arcane"]
TYPE_DE = dict(zip(TYPES, ["Glut", "Flut", "Stein", "Sturm", "Blüte", "Frost", "Leere", "Licht", "Gift", "Metall",
                           "Geist", "Kristall", "Klang", "Schwerkraft", "Arkan"]))
STATS = {"Attack": "ANG", "Defense": "VER", "SpAttack": "SAN", "SpDefense": "SVE", "Speed": "GES",
         "Precision": "PRÄ", "Evasion": "AUS", "Random": "zufälliger Wert"}
TARGETS = {"Single": ("einen Gegner", 1000), "Row": ("eine gegnerische Reihe", 1400), "Enemies": ("alle Gegner", 1700),
           "Self": ("selbst", 0), "Ally": ("einen Verbündeten", 0), "AllyRow": ("eigene Reihe", 0),
           "Allies": ("alle Verbündeten", 0), "Field": ("Feld", 0), "AnySingle": ("ein beliebiges Ziel", 1000)}
CATEGORIES = {"Physical": "Physisch", "Special": "Speziell", "Status": "Status"}
KINDS = {"Active": "A", "Passive": "P", "Crescendo": "U", "Field": "F"}
WHO_FACTOR = {"Self": 1000, "Ally": 1000, "Target": 1000, "Allies": 1600, "Enemies": 1600, "AllyRow": 1300, "Row": 1300}
WHO_DE = {"Self": "sich selbst", "Ally": "einen Verbündeten", "Target": "das Ziel", "Allies": "alle Verbündeten",
          "Enemies": "alle Gegner", "AllyRow": "die eigene Reihe", "Row": "die Zielreihe"}

# Startwerte der Status-Effekte (Mechanik final in K32) – Wert in MP bei 100 % Chance
STATUS_VALUE = {"Brand": 45, "Ausgetrocknet": 35, "Rueckstoss": 35, "Verlangsamt": 40, "Welke": 35, "Starre": 60,
                "Entzug": 40, "Geblendet": 40, "Vergiftet": 20, "Erschuettert": 35, "Furcht": 45, "Gebrochen": 45,
                "Verstummt": 45, "Schwebend": 35, "Verflucht": 50}
STATUS_DE = {"Brand": "Brand", "Ausgetrocknet": "Ausgetrocknet", "Rueckstoss": "Rückstoß", "Verlangsamt": "Verlangsamt",
             "Welke": "Welke", "Starre": "Starre", "Entzug": "Entzug", "Geblendet": "Geblendet", "Vergiftet": "Vergiftet",
             "Erschuettert": "Erschüttert", "Furcht": "Furcht", "Gebrochen": "Gebrochen", "Verstummt": "Verstummt",
             "Schwebend": "Schwebend", "Verflucht": "Verflucht"}
TERRAINS = {"Glutboden": "Glutboden", "Ueberwuchs": "Überwuchs", "Sumpf": "Sumpf", "Eisflaeche": "Eisfläche",
            "Kristallfeld": "Kristallfeld", "Klangfeld": "Klangfeld", "Schwerefeld": "Schwerefeld",
            "Glyphenfeld": "Glyphenfeld", "Stillefeld": "Stillefeld", "Lichtfeld": "Lichtfeld", "Nebelfeld": "Nebelfeld",
            "Missklang": "Missklang-Terrain", "Glutsand": "Glutsand", "Flutfeld": "Flutfeld", "Sturmfeld": "Sturmfeld"}
WEATHERS = {"Clear": "Klar", "Rain": "Regen", "Thunderstorm": "Gewitter", "Snow": "Schneefall", "Fog": "Nebel",
            "Sandstorm": "Sandsturm", "Heatwave": "Hitzewelle"}

# Effektdefinitionen: Name -> (Wertfunktion(args, power, ctx) -> MP, Beschreibung(args) -> str, Identitätsmarken)
def _who(a):
    return WHO_FACTOR.get(a, 1000)

def _chance(args, i):
    return int(args[i]) if len(args) > i else 1000

def v_status(a, p, c):
    stacks = int(a[2]) if len(a) > 2 else 1
    return STATUS_VALUE[a[0]] * _chance(a, 1) // 1000 * stacks

def d_status(a):
    ch = _chance(a, 1)
    st = f" ({a[2]} Stapel)" if len(a) > 2 else ""
    return (f"{ch // 10} % Chance auf {STATUS_DE[a[0]]}{st}" if ch < 1000 else f"verursacht {STATUS_DE[a[0]]}{st}")

def v_stage(a, p, c):
    who, stat, delta = a[0], a[1], int(a[2])
    ch = _chance(a, 3)
    good = (delta > 0) == (who in ("Self", "Ally", "Allies", "AllyRow"))
    val = abs(delta) * 20 * _who(who) // 1000 * ch // 1000
    return val if good else -val

def d_stage(a):
    who, stat, delta = a[0], a[1], int(a[2])
    ch = _chance(a, 3)
    pre = f"{ch // 10} % Chance: " if ch < 1000 else ""
    return f"{pre}{STATS[stat]} {'+' if delta > 0 else '−'}{abs(delta)} für {WHO_DE[who]}"

EFFECTS = {
    "Status": (v_status, d_status, {"Status"}),
    "Stage": (v_stage, d_stage, {"Stage"}),
    "Delay": (lambda a, p, c: int(a[1]) * 4 // 10 * _who(a[0]) // 1000,
              lambda a: f"{WHO_DE[a[0]]} rückt {a[1]} Ticks auf der Zeitleiste zurück", {"Delay"}),
    "Haste": (lambda a, p, c: int(a[1]) * 4 // 10 * _who(a[0]) // 1000,
              lambda a: f"{WHO_DE[a[0]]} rückt {a[1]} Ticks auf der Zeitleiste vor", {"Haste"}),
    "Push": (lambda a, p, c: 15, lambda a: "stößt das Ziel in die Hinterreihe", {"Push"}),
    "Pull": (lambda a, p, c: 15, lambda a: "zieht das Ziel in die Vorderreihe", {"Pull"}),
    "SwapRows": (lambda a, p, c: 25, lambda a: "vertauscht die gegnerischen Reihen", {"SwapRows"}),
    "MoveSelf": (lambda a, p, c: 10, lambda a: "Anwender wechselt die Reihe ohne Zeitkosten", {"MoveSelf"}),
    "Heal": (lambda a, p, c: int(a[1]) * 12 // 10 * _who(a[0]) // 1000,
             lambda a: f"heilt {WHO_DE[a[0]]} um {a[1]} % der max. HP", {"Heal"}),
    "Regen": (lambda a, p, c: int(a[1]) * int(a[2]) * _who(a[0]) // 1000,
              lambda a: f"{WHO_DE[a[0]]} heilt {a[2]} Runden je {a[1]} % der max. HP", {"Regen"}),
    "Shield": (lambda a, p, c: int(a[1]) * _who(a[0]) // 1000,
               lambda a: f"Schild für {WHO_DE[a[0]]} ({a[1]} % der max. HP)", {"Shield"}),
    "Drain": (lambda a, p, c: 3 * p * int(a[0]) // 10000,
              lambda a: f"heilt den Anwender um {int(a[0]) // 10} % des Schadens", {"Drain"}),
    "Recoil": (lambda a, p, c: -(3 * p * int(a[0]) // 10000),
               lambda a: f"Rückschlag: Anwender erleidet {int(a[0]) // 10} % des Schadens", set()),
    "Priority": (lambda a, p, c: 15 * int(a[0]), lambda a: f"Priorität +{a[0]}", {"Priority"}),
    "Multi": (lambda a, p, c: 0, lambda a: f"trifft {a[0]}–{a[1]}-mal", {"Multi"}),
    "Crit": (lambda a, p, c: 10 * int(a[0]), lambda a: f"Volltrefferstufe +{a[0]}", set()),
    "Terrain": (lambda a, p, c: 8 * int(a[1]), lambda a: f"erzeugt {TERRAINS[a[0]]} für {a[1]} Runden", {"Terrain"}),
    "Weather": (lambda a, p, c: 6 * int(a[1]), lambda a: f"ruft {WEATHERS[a[0]]} für {a[1]} Runden herbei", {"Weather"}),
    "Harmony": (lambda a, p, c: int(a[0]), lambda a: f"Harmonie +{a[0]}", {"Harmony"}),
    "HarmonyDrain": (lambda a, p, c: int(a[0]), lambda a: f"entzieht dem Gegnerteam {a[0]} Harmonie", {"HarmonyDrain"}),
    "Cleanse": (lambda a, p, c: 40 if a[0] in ("Allies", "AllyRow") else 25,
                lambda a: f"entfernt negative Status von {WHO_DE[a[0]]}", {"Cleanse"}),
    "Reveal": (lambda a, p, c: 15, lambda a: "enthüllt das Ziel (Ausweichen, Täuschung und Tarnung wirkungslos)", {"Reveal"}),
    "Dispel": (lambda a, p, c: 30 * _who(a[0]) // 1000,
               lambda a: f"entfernt Schilde und positive Stufen von {WHO_DE[a[0]]}", {"Dispel"}),
    "Charge": (lambda a, p, c: -(15 * p // 100), lambda a: "benötigt eine Aufladerunde (sichtbar auf der Zeitleiste)", {"Charge"}),
    "Exhaust": (lambda a, p, c: -(30 * p // 100), lambda a: "Anwender muss danach eine Runde aussetzen", set()),
    "IgnoreFormation": (lambda a, p, c: 10, lambda a: "ignoriert Formationsschutz", {"IgnoreFormation"}),
    "IgnoreShield": (lambda a, p, c: 15, lambda a: "durchdringt Schilde", {"IgnoreShield"}),
    "SureHit": (lambda a, p, c: 10, lambda a: "verfehlt nie", set()),
    "Reflect": (lambda a, p, c: 35, lambda a: f"reflektiert den nächsten {'physischen' if a[0] == 'Physical' else 'speziellen'} Angriff", {"Reflect"}),
    "Counter": (lambda a, p, c: 40, lambda a: f"kontert den nächsten {'physischen' if a[0] == 'Physical' else 'speziellen'} Angriff mit {int(a[1]) // 10} % Schaden", {"Counter"}),
    "TypeChange": (lambda a, p, c: 40, lambda a: f"ändert den Typ von {WHO_DE[a[0]]} für {a[2]} Runden zu {TYPE_DE[a[1]]}", {"TypeChange"}),
    "InvertChart": (lambda a, p, c: 50, lambda a: f"kehrt die Typtabelle für {a[0]} Runde(n) um (angekündigt)", {"InvertChart"}),
    "Copy": (lambda a, p, c: 40, lambda a: "kopiert die zuletzt vom Ziel eingesetzte Fähigkeit", {"Copy"}),
    "Trap": (lambda a, p, c: 30, lambda a: f"legt eine Falle ({a[0]}) auf die gegnerische Seite", {"Trap"}),
    "Taunt": (lambda a, p, c: 15 * int(a[0]), lambda a: f"Gegner müssen {a[0]} Runde(n) den Anwender angreifen", {"Taunt"}),
    "Decoy": (lambda a, p, c: 35, lambda a: "erschafft ein Trugbild, das den nächsten Angriff abfängt", {"Decoy"}),
    "StealBuffs": (lambda a, p, c: 35, lambda a: "stiehlt die positiven Stufen des Ziels", {"StealBuffs"}),
    "Bind": (lambda a, p, c: 10 * int(a[0]), lambda a: f"Ziel kann {a[0]} Runde(n) die Reihe nicht wechseln", {"Bind"}),
    "Charged": (lambda a, p, c: 20, lambda a: "lädt den Anwender auf: nächster Angriff +50 % Stärke", {"Charged"}),
    "WeatherBoost": (lambda a, p, c: 10, lambda a: f"Stärke ×1,5 bei {WEATHERS[a[0]]}", set()),
    "TerrainBoost": (lambda a, p, c: 10, lambda a: f"Stärke ×1,5 auf {TERRAINS[a[0]]}", set()),
    "Revive": (lambda a, p, c: 10 * int(a[0]) // 10, lambda a: f"belebt einen verklungenen Verbündeten mit {a[0]} % HP wieder", {"Revive"}),
}
IDENTITY = {  # CANON §78 – Identitätsmarken je Typ
    "Ember": {"Status:Brand", "Terrain:Glutboden", "Terrain:Glutsand"},
    "Tide": {"Push", "Pull", "Regen", "Terrain:Flutfeld"},
    "Stone": {"Shield", "Stage:Defense"},
    "Storm": {"Haste", "Multi", "Priority"},
    "Bloom": {"Heal", "Regen", "Terrain:Ueberwuchs"},
    "Frost": {"Delay", "Stage:Precision", "Status:Starre", "Status:Verlangsamt"},
    "Void": {"Dispel", "HarmonyDrain", "Status:Entzug"},
    "Light": {"Reveal", "Cleanse", "Status:Geblendet"},
    "Venom": {"Status:Vergiftet"},
    "Metal": {"Shield", "Counter", "Stage:Defense"},
    "Spirit": {"IgnoreFormation", "Decoy", "Status:Furcht"},
    "Crystal": {"Reflect", "Charge", "Charged"},
    "Sound": {"Delay", "Haste", "Harmony"},
    "Gravity": {"Push", "Pull", "SwapRows", "Bind"},
    "Arcane": {"InvertChart", "TypeChange", "Copy", "StealBuffs"},
}

EFF_RE = re.compile(r"^([A-Za-z]+)\(([^()]*)\)$")


def parse(effects: str):
    out = []
    for part in [p.strip() for p in effects.split(";") if p.strip()]:
        m = EFF_RE.match(part)
        if not m:
            raise ValueError(f"Effekt unlesbar: {part}")
        name, args = m.group(1), [a.strip() for a in m.group(2).split(",")] if m.group(2) else []
        if name not in EFFECTS:
            raise ValueError(f"Effekt unbekannt: {name}")
        out.append((name, args))
    return out


def marks(effects):
    res = set()
    for n, a in effects:
        res.add(n)
        if n == "Status":
            res.add(f"Status:{a[0]}")
        if n == "Stage":
            res.add(f"Stage:{a[1]}")
        if n == "Terrain":
            res.add(f"Terrain:{a[0]}")
    return res


def budget(power: int, acc: int, target: str, category: str, effects) -> tuple[int, int]:
    """Gibt (Machtpunkte V, Zeitkosten) zurück – ganzzahlig, deterministisch."""
    hits = 1000
    for n, a in effects:
        if n == "Multi":
            hits = (int(a[0]) + int(a[1])) * 500
    tf = TARGETS[target][1] or 1000
    dmg = power * (acc or 1000) // 1000 * tf // 1000 * hits // 1000 if power else 0
    ev = 0
    for n, a in effects:
        val = EFFECTS[n][0](a, power, None)
        hostile = n in ("Status", "Bind", "Taunt", "StealBuffs", "Copy", "TypeChange") or (
            n in ("Stage", "Delay", "Dispel") and a and a[0] in ("Target", "Enemies", "Row"))
        if category == "Status" and acc and hostile:
            val = val * acc // 1000
        if n == "Status" and target in ("Row", "Enemies"):
            val = val * TARGETS[target][1] // 1000
        ev += val
    v = dmg + ev
    cost = max(50, min(200, (20 + v + 5) // 10 * 10))
    return v, cost


def describe(row) -> str:
    eff = parse(row["Effects"])
    parts = []
    p = int(row["Power"] or 0)
    if p:
        cat = CATEGORIES[row["Category"]]
        parts.append(f"{cat}er Schaden, Stärke {p}, gegen {TARGETS[row['Target']][0]}")
    elif row["Target"] not in ("Self", "Field"):
        parts.append(f"wirkt auf {TARGETS[row['Target']][0]}")
    parts += [EFFECTS[n][1](a) for n, a in eff]
    s = "; ".join(parts)
    return s[0].upper() + s[1:] + "."


def load(path=ABIL):
    return list(csv.DictReader(open(path, encoding="utf-8"))) if path.exists() else []
