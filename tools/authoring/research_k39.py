#!/usr/bin/env python3
"""K39 – erzeugt Kodex-Aufgaben (Stufe 4) aller 256 Arten und die 120 Klangfragmente (Lore, Wahrheitsebenen L-01).

Kodex-Aufgaben werden aus den Artdaten abgeleitet (Merkmale, Aktivität, Spawn-Bedingungen, Evolution, Reiten, Nischen),
damit jede Aufgabe beobachtbares Verhalten belohnt (DR-02) und Evolutionswissen lehrt (DR-33).
"""
import csv, hashlib, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


def h(*a):
    return int(hashlib.sha1("|".join(map(str, a)).encode()).hexdigest()[:8], 16)


TRAIT_DE = {r["Name"]: r["DisplayName"] for r in rows("Data/Echos/BehaviorTraits.csv")}
WEATHER_DE = {"Rain": "Regen", "Thunderstorm": "Gewitter", "Fog": "Nebel", "Snow": "Schneefall", "Heatwave": "Hitzewelle",
              "Sandstorm": "Sandsturm", "Clear": "klarem Wetter"}
TOD_DE = {"Night": "nachts", "Dawn": "in der Morgendämmerung", "Dusk": "in der Abenddämmerung", "Noon": "zur Mittagszeit", "Day": "tagsüber"}
ACT_DE = {"Diurnal": "tagsüber", "Nocturnal": "nachts", "Crepuscular": "in der Dämmerung", "Cathemeral": "zu jeder Tageszeit"}


def tasks_for(s):
    t = []
    traits = [x for x in s["Traits"].split("|") if x]
    tr = traits[h(s["Name"], "tr") % len(traits)]
    t.append(("Observe", f"Beobachte das Verhalten „{TRAIT_DE.get(tr, tr)}“ mit dem Resonanzsinn ({ACT_DE.get(s['Activity'].split('.')[-1], '')})", tr))
    conds = [c for c in s["SpawnConditions"].split("|") if c.split(".")[0] in ("Weather", "TimeOfDay", "Moon", "Zone")]
    if conds:
        c = conds[0]
        k, v = c.split(".", 1)
        txt = {"Weather": "bei " + WEATHER_DE.get(v, v), "TimeOfDay": TOD_DE.get(v, v),
               "Moon": "bei " + ("Vollmond" if v == "FullMoon" else "Neumond"), "Zone": "in seiner Kristallhöhle"}[k]
        t.append(("Photo", f"Fotografiere es {txt} mit mindestens 2 Sternen", c))
    elif s["Mount"]:
        t.append(("Ride", f"Lege auf ihm reitend 2 km zurück ({s['Mount'].split('.')[1]})", s["Mount"]))
    else:
        t.append(("Photo", "Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne)", "Behavior"))
    if s["EvolvesTo"]:
        t.append(("Evolve", "Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen)", s["EvoCondition"]))
    elif s["LineKind"] in ("Legendary", "Mythical"):
        t.append(("Bond", "Erreiche Bindungsstufe 4 mit diesem Echo", "BondTier>=4"))
    else:
        alt = h(s["Name"], "alt") % 3
        t.append([("Bond", "Erreiche Bindungsstufe 3 mit einem Echo dieser Art", "BondTier>=3"),
                  ("Battle", "Gewinne 10 Kämpfe gegen oder mit dieser Art", "Wins>=10"),
                  ("Perfect", "Binde ein Echo dieser Art mit Einklang", "Bond=Perfect")][alt])
    return t


THEMES = [  # (Titel, Sprecher, Wahrheitsebene)
    ("Das erste Lied", "Erstchor", 0), ("Ein Kinderlied", "Alltagsstimme", 0), ("Die Stimme dieses Landes", "Erstchor", 1),
    ("Warnung der Hüter", "Dorunische Archivarin", 2), ("Der Missklang beginnt", "Dorunischer Archivar", 3),
    ("Der Erstchor versammelt sich", "Erstchor", 4), ("Die Arena über dem Schlaf", "Erstchor", 4),
    ("Ilens Zweifel", "Ilen", 5), ("Maedryns Versprechen", "Archon Maedryn", 6), ("Die letzte Nacht vor der Stille", "Ilen", 7),
    ("Der Riegel", "Ilen", 8), ("Was danach bleibt", "Ilen", 9),
]
REGION_PLACE = {"R01": "Wurzelhalle", "R02": "Kharsholmer Schlund", "R03": "Versunkener Turm", "R04": "Sonnenhof",
                "R05": "Kraterherz", "R06": "Thal'assyrs Rippe", "R07": "Gletscherdom", "R08": "Säulenfeld Thae'Luun",
                "R09": "Resonanzkammer", "R10": "Sternenarena"}


def main():
    sp = rows("Data/Echos/Species.csv")
    with open(ROOT / "Data/Research/KodexTasks.csv", "w", newline="", encoding="utf-8") as f:
        f.write("# Kodex-Aufgaben Stufe 4 (K39 §3): je Art 3 Aufgaben, abgeleitet aus Artdaten. Kind: Observe|Photo|Ride|Evolve|Bond|Battle|Perfect.\n")
        w = csv.writer(f)
        w.writerow(["Species", "Index", "Kind", "Text", "Param"])
        n = 0
        for s in sp:
            for i, (k, txt, p) in enumerate(tasks_for(s), 1):
                w.writerow([s["Name"], i, k, txt, p])
                n += 1
    with open(ROOT / "Data/Lore/LoreEntries.csv", "w", newline="", encoding="utf-8") as f:
        f.write("# Lore-Einträge (CANON §38, ULoreEntryDefinition). K39: 120 Klangfragmente (FRG). TruthLevel 0–9 (L-01: erst ab Enthüllung unverzerrt).\n")
        w = csv.writer(f)
        w.writerow(["Name", "Category", "Region", "Title", "Speaker", "TruthLevel", "Location"])
        k = 1
        for r in sorted(REGION_PLACE):
            for title, speaker, tl in THEMES:
                loc = REGION_PLACE[r] if tl >= 4 else "Region (Fundort-Tabelle K49–K51)"
                w.writerow([f"LORE_FRG_{k:03d}", "FRG", r, f"{title} – {REGION_PLACE[r]}", speaker, tl, loc])
                k += 1
    print(f"KodexTasks {n}, Klangfragmente {k - 1}")


if __name__ == "__main__":
    main()


def task_sample(n=40):
    sp = {r["Name"]: r["DisplayName"] for r in rows("Data/Echos/Species.csv")}
    t = rows("Data/Research/KodexTasks.csv")
    by = {}
    for r in t:
        by.setdefault(r["Species"], []).append(r["Text"])
    keys = sorted(by, key=lambda k: int(k[5:]))[::max(1, len(by) // n)][:n]
    out = ["| # | Art | Aufgabe 1 | Aufgabe 2 | Aufgabe 3 |", "|---|---|---|---|---|"]
    for k in keys:
        out.append(f"| {int(k[5:]):03d} | {sp[k]} | " + " | ".join(by[k]) + " |")
    return "\n".join(out)
