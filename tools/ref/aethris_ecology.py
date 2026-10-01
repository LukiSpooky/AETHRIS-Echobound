#!/usr/bin/env python3
"""Ökologie-Referenzmodell (K52): Rollen, Ökologie-Fragment, Nahrungsnetz, Populationsdynamik, Spawn-Gewichte.

Alles ganzzahlig und deterministisch (CANON §29, ADR-029). Aufruf:
  aethris_ecology.py validate | build | foodweb R01 | spawn R01_Z02 | pop R01_Z02
"""
import csv, pathlib, sys
from collections import defaultdict
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/ref"))
from aethris_random import AethrisRandom  # noqa: E402


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


SPECIES = [r for r in rows("Data/Echos/Species.csv")]
WILD = [s for s in SPECIES if s["Rarity"] not in ("Legendary", "Mythical") and s["Zones"]]
ZONES = {r["Name"]: r for r in rows("Data/World/Zones.csv")}
ACT = {r["Name"]: [int(r[f"H{h:02d}"]) for h in range(24)] for r in rows("Data/World/ActivityCurves.csv")}
WEATHER_MOD = {r["Name"]: r for r in rows("Data/World/WeatherSpawnModifiers.csv")}
MOON = {r["Tag"]: int(r["NocturnalSpawnPermille"]) for r in rows("Data/World/MoonPhases.csv")}
GROUPS = {r["Name"]: r for r in rows("Data/Ecology/GroupBehaviors.csv")}
TUNE = {r["Name"]: r for r in rows("Data/Ecology/PopulationTuning.csv")}

RARITY_W = {"Common": 1000, "Uncommon": 400, "Rare": 120, "VeryRare": 30}
SIZE_K = {"XS": 1500, "S": 1300, "M": 1000, "L": 600, "XL": 350, "XXL": 200}
SIZE_ORD = ["XS", "S", "M", "L", "XL", "XXL"]
PHASES = {"Dawn": [5, 6], "Day": list(range(7, 19)), "Dusk": [19, 20], "Night": [21, 22, 23, 0, 1, 2, 3, 4]}
WEATHER_IDX = {"Clear": "W01", "Rain": "W02", "Thunderstorm": "W03", "Fog": "W04", "Snow": "W05", "Heatwave": "W06",
               "Sandstorm": "W07", "Aurora": "W08", "Ashfall": "W09", "ResonanceStorm": "W10"}


def traits(s):
    return set(t.split(".")[-1] for t in s["Traits"].split("|") if t)


def role(s):
    t = traits(s)
    if t & {"Hunter", "Ambusher"}:
        return "Räuber"
    if "Scavenger" in t:
        return "Klangsammler"
    if t & {"Grazer", "Pollinator", "Filterer", "Lithophage", "Sunbather", "Thermal"}:
        return "Primärverbraucher"
    return "Allesverwerter"


FOOD = {"Grazer": "Gräser, Moos, Blätter", "Pollinator": "Nektar, Pollen, Tau", "Filterer": "Schwebstoffe aus Wasser oder Luft",
        "Lithophage": "Erz, Kristall, Schlacke", "Hunter": "Klangbiss bei anderen Echos (Resonanz, nie Fleisch)",
        "Ambusher": "Klangbiss aus dem Hinterhalt", "Scavenger": "Klangreste erschöpfter Echos, Abfälle", "Thermal": "Wärme (Lava, Quellen)",
        "Sunbather": "Licht und Wärme"}
SLEEP = [("Burrower", "Bau im Boden"), ("Nester", "Nest"), ("Swimmer", "Unterwasser-Höhle"), ("Flier", "Horst oder Felsvorsprung"),
         ("Climber", "Baumkrone oder Felswand"), ("Camouflaged", "Getarnt an Ort und Stelle"), ("Thermal", "Warmer Stein, Quelle")]
REPRO = {"A05": "Gelege im Nest", "A08": "Laich", "A09": "Laich im Flachwasser", "A10": "Eier in Kammern",
         "A12": "Klangteilung", "A13": "Resonanzkeim aus Material", "A14": "Ableger", "A15": "Gelege im Horst",
         "A16": "Klangteilung im Schwarm", "A17": "Laich in Felsspalten", "A11": "Gelege im Sand oder Schlamm"}


def ecology_fragment(s):
    t = traits(s)
    food = [FOOD[k] for k in FOOD if k in t]
    if not food:
        tp = s["PrimaryType"].split(".")[-1]
        food = [{"Ember": "Wärme und Glut", "Tide": "Algen, Plankton", "Stone": "Mineralsalze", "Storm": "Insekten im Wind",
                 "Bloom": "Pflanzensäfte", "Frost": "Eisflechten", "Void": "Stille (Pausen im Klang)", "Light": "Licht",
                 "Venom": "Pilze, Moder", "Metal": "Erzstaub", "Spirit": "Erinnerungsklang an alten Orten",
                 "Crystal": "Kristallstaub", "Sound": "Klang anderer Lebewesen (ohne zu schaden)", "Gravity": "Gesteinsbrocken",
                 "Arcane": "Glyphenresonanz"}[tp]]
    sleep = next((v for k, v in SLEEP if k in t), "Geschützte Stelle im Habitat")
    repro = REPRO.get(s["Archetype"], "Resonanzkeim (Wurf von 1–3)")
    return {"Food": "; ".join(food), "SleepSite": sleep, "Reproduction": repro}


def zones_of(s):
    return set(z for z in s["Zones"].split("|") if z)


def neighbours(zs):
    """Zonen plus direkte Nachbarn derselben Region (Zonenindex ± 1) – Jagdgebiete reichen über die Zonengrenze."""
    out = set(zs)
    for z in zs:
        r, n = z[:3], int(z[-2:])
        for d in (-1, 1):
            cand = f"{r}_Z{n + d:02d}"
            if cand in ZONES:
                out.add(cand)
    return out


CAVE_REGIONS = {"R09"}   # Unter Tage: Nachtaktive gelten ganztags als mindestens dämmerungsaktiv (Höhlen-Regel)


def act_curve(s):
    c = ACT[s["Activity"]]
    if s["Region"] in CAVE_REGIONS and s["Activity"].endswith("Nocturnal"):
        return [max(v, 500) for v in c]
    return c


def overlap(a, b):
    """Gemeinsame aktive Stunden (beide ≥ 500 ‰)."""
    ca, cb = act_curve(a), act_curve(b)
    return sum(1 for h in range(24) if ca[h] >= 500 and cb[h] >= 500)


def prey_of(pred):
    if role(pred) != "Räuber":
        return []
    cands = []
    for q in WILD:
        if q is pred or role(q) == "Räuber" or q["Line"] == pred["Line"]:
            continue
        shared = zones_of(pred) & zones_of(q)
        near = neighbours(zones_of(pred)) & zones_of(q)
        if not near:
            continue
        if SIZE_ORD.index(q["SizeClass"]) > SIZE_ORD.index(pred["SizeClass"]) + 1:
            continue
        ov = overlap(pred, q)
        if ov < 1:
            continue
        score = ov * 10 + len(shared) * 5 + RARITY_W[q["Rarity"]] // 100
        cands.append((score, q["Name"]))
    cands.sort(reverse=True)
    return [n for _, n in cands[:3]]


def foodweb():
    web = {s["Name"]: prey_of(s) for s in WILD}
    preds = defaultdict(list)
    for p, qs in web.items():
        for q in qs:
            preds[q].append(p)
    return web, preds


def capacity(s):
    t = TUNE[s["Rarity"]]
    return max(1, int(t["BaseCapacity"]) * SIZE_K[s["SizeClass"]] // 1000)


def floor_of(s):
    return max(1, capacity(s) * int(TUNE[s["Rarity"]]["FloorPermille"]) // 1000)


def simulate(zone, days=30, removed=None, stillzone=False, start="K"):
    """Diskretes Lotka-Volterra-Modell je Spieltag (Ganzzahl). removed: {Art: Anzahl/Tag} (Bindungen)."""
    removed = removed or {}
    sp = [s for s in WILD if zone in zones_of(s)]
    web, _ = foodweb()
    N = {s["Name"]: (floor_of(s) if start == "floor" else capacity(s)) for s in sp}
    hist = []
    for d in range(days + 1):
        hist.append(dict(N))
        new = {}
        for s in sp:
            n, K = N[s["Name"]], capacity(s)
            if stillzone:
                K = max(1, K * 300 // 1000)
            r = int(TUNE[s["Rarity"]]["GrowthPermille"])
            growth = r * n * (K - n) // (K * 1000) if K else 0
            if n < K and growth == 0:
                growth = 1   # Mindestzuwachs: jede Art erholt sich sichtbar (DR-05)
            # Prädation: Räuber dieser Art im selben Gebiet
            pred = 0
            for p in sp:
                if s["Name"] in web.get(p["Name"], []):
                    pred += int(TUNE[p["Rarity"]]["PredationPermille"]) * N[p["Name"]] * n // (1000 * max(1, capacity(s)))
            # Räuber-Ernährung: Zuwachs nur, wenn Beute vorhanden
            feed = 0
            if role(s) == "Räuber":
                prey = [q for q in sp if q["Name"] in web.get(s["Name"], [])]
                avail = sum(N[q["Name"]] for q in prey)
                need = n
                feed = -max(0, (need - avail)) // 2
            v = n + growth - pred + feed - removed.get(s["Name"], 0)
            new[s["Name"]] = max(floor_of(s), min(K * 12 // 10, v))
        N = new
    return sp, hist


def spawn_weights(zone, hour, weather="Clear", moon="Moon.FullMoon", day=1, pop=None):
    """pop: {Art: Bestand} – Bestandsfaktor N/K in ‰ (mind. 200); ohne Angabe 1000."""
    sp = [s for s in WILD if zone in zones_of(s)]
    out = []
    for s in sp:
        w = RARITY_W[s["Rarity"]]
        a = max(80, act_curve(s)[hour])
        tp = s["PrimaryType"].split(".")[-1]
        wm = int(WEATHER_MOD[WEATHER_IDX[weather]][tp])
        mm = MOON[moon] if act_curve(s)[hour] >= 500 and hour in PHASES["Night"] else 1000
        pf = 1000 if not pop else max(200, min(1000, 1000 * pop.get(s["Name"], capacity(s)) // capacity(s)))
        val = w * a // 1000 * wm // 1000 * mm // 1000 * pf // 1000
        out.append((s["Name"], s["DisplayName"], s["Rarity"], val))
    tot = sum(v for *_, v in out) or 1
    return [(n, d, r, v, 1000 * v // tot) for n, d, r, v in sorted(out, key=lambda x: -x[3])]


def pick_spawn(zone, hour, cell, tick, weather="Clear", moon="Moon.FullMoon", world_seed=0xAE7215, day=1):
    """Deterministische Auswahl: Fork(2) je Zone, Schlüssel (Spieltag, Stunde, Zelle, Tick)."""
    zone_key = int(zone[1:3]) * 100 + int(zone[-2:])          # stabil (kein Python-hash)
    rng = AethrisRandom(world_seed, 1).fork(2).fork(zone_key).fork(day * 10000 + hour * 100 + cell * 7 + tick)
    ws = spawn_weights(zone, hour, weather, moon, day)
    tot = sum(v for *_, v, _p in ws)
    x = rng.next_bounded(max(1, tot))
    for n, d, r, v, p in ws:
        if x < v:
            sp = next(q for q in WILD if q["Name"] == n)
            g = GROUPS[group_kind(sp)]
            lo, hi = int(g["SizeMin"]), int(g["SizeMax"])
            return n, d, lo + rng.next_bounded(hi - lo + 1)
        x -= v
    return ws[-1][0], ws[-1][1], 1


def group_kind(s):
    t = traits(s)
    for k in ("Swarm", "Herd", "Pack", "FamilyGroup", "Solitary"):
        if k in t:
            return k
    return "Loose"


def group_for(name):
    s = next(x for x in WILD if x["Name"] == name)
    g = GROUPS[group_kind(s)]
    lo, hi = int(g["SizeMin"]), int(g["SizeMax"])
    return (lo + hi) // 2


# ── Markdown-Ausgaben ──
def roles_table():
    c = defaultdict(lambda: defaultdict(int))
    for s in WILD:
        c[s["Region"]][role(s)] += 1
    rs = ["Primärverbraucher", "Räuber", "Klangsammler", "Allesverwerter"]
    lines = ["| Region | " + " | ".join(rs) + " | Arten |", "|---|" + "---|" * (len(rs) + 1)]
    for reg in sorted(c):
        lines.append(f"| {reg} | " + " | ".join(str(c[reg][r]) for r in rs) + f" | {sum(c[reg].values())} |")
    tot = {r: sum(c[x][r] for x in c) for r in rs}
    lines.append("| **Σ** | " + " | ".join(f"**{tot[r]}**" for r in rs) + f" | **{len(WILD)}** |")
    return "\n".join(lines)


def foodweb_table(region):
    web, preds = foodweb()
    name = {s["Name"]: s["DisplayName"] for s in SPECIES}
    lines = ["| Räuber | Größe | Aktivität | Beute (bis 3, nach Überschneidung) |", "|---|---|---|---|"]
    for s in WILD:
        if s["Region"] == region and role(s) == "Räuber":
            lines.append(f"| {s['DisplayName']} | {s['SizeClass']} | {s['Activity'].split('.')[-1]} | "
                         + (", ".join(name[q] for q in web[s['Name']]) or "– (Klangsammler)") + " |")
    return "\n".join(lines)


def fragment_table(region, limit=12):
    lines = ["| Art | Rolle | Nahrung | Schlafplatz | Fortpflanzung | Gruppe |", "|---|---|---|---|---|---|"]
    for s in [x for x in WILD if x["Region"] == region][:int(limit)]:
        f = ecology_fragment(s)
        lines.append(f"| {s['DisplayName']} | {role(s)} | {f['Food']} | {f['SleepSite']} | {f['Reproduction']} | {GROUPS[group_kind(s)]['DisplayName']} |")
    return "\n".join(lines)


def spawn_table(zone, weather="Clear"):
    lines = ["| Art | Seltenheit | Morgen (06) | Tag (13) | Abend (20) | Nacht (01) |", "|---|---|---|---|---|---|"]
    res = {h: {n: p for n, d, r, v, p in spawn_weights(zone, h, weather)} for h in (6, 13, 20, 1)}
    names = [(n, d, r) for n, d, r, v, p in spawn_weights(zone, 13, weather)]
    for n, d, r in names:
        lines.append(f"| {d} | {r} | " + " | ".join(f"{res[h][n] / 10:.1f} %".replace(".", ",") for h in (6, 13, 20, 1)) + " |")
    return "\n".join(lines)


def pop_table(zone, days=30, start="K", removed_species=None, per_day=0):
    removed = {removed_species: int(per_day)} if removed_species and removed_species != "-" else None
    sp, hist = simulate(zone, int(days), removed, start=start)
    name = {s["Name"]: s["DisplayName"] for s in sp}
    marks = [0, 5, 10, 15, 20, 25, 30][: int(days) // 5 + 1]
    lines = ["| Art | Rolle | K | " + " | ".join(f"Tag {d}" for d in marks) + " |", "|---|---|---|" + "---|" * len(marks)]
    for s in sp:
        lines.append(f"| {name[s['Name']]} | {role(s)} | {capacity(s)} | " + " | ".join(str(hist[d][s['Name']]) for d in marks) + " |")
    return "\n".join(lines)


def validate():
    err = []
    web, preds = foodweb()
    for s in WILD:
        f = ecology_fragment(s)
        if not all(f.values()):
            err.append(f"EC-01 {s['Name']}: Ökologie-Fragment unvollständig")
        if role(s) == "Räuber" and not web[s["Name"]]:
            err.append(f"EC-02 {s['Name']} ({s['DisplayName']}): Räuber ohne Beute")
    for z in ZONES:
        sp = [s for s in WILD if z in zones_of(s)]
        near = [s for s in WILD if neighbours({z}) & zones_of(s)]
        if sp and not any(role(s) in ("Primärverbraucher", "Allesverwerter") for s in near):
            err.append(f"EC-03 {z}: keine Basisverbraucher (auch nicht in Nachbarzonen)")
    regs = defaultdict(set)
    for s in WILD:
        regs[s["Region"]].add(role(s))
    for r, roles in regs.items():
        if not roles & {"Räuber", "Klangsammler"}:
            err.append(f"EC-04 {r}: weder Räuber noch Klangsammler")
        for ph, hours in PHASES.items():
            n = sum(1 for s in WILD if s["Region"] == r and max(act_curve(s)[h] for h in hours) >= 500)
            if n < 1:
                err.append(f"EC-05 {r}: Tagesphase {ph} ohne aktive Art")
    return err


def build():
    """Schreibt Data/Ecology/EcologyFragments.csv und FoodWeb.csv."""
    web, preds = foodweb()
    p1 = ROOT / "Data/Ecology/EcologyFragments.csv"
    with open(p1, "w", encoding="utf-8", newline="") as fh:
        fh.write("# Ökologie-Fragment je Wildart (K52 §3, generiert von tools/ref/aethris_ecology.py; CD-09).\n")
        w = csv.writer(fh)
        w.writerow(["Name", "Role", "Food", "SleepSite", "Reproduction", "Group", "Capacity", "Floor"])
        for s in WILD:
            f = ecology_fragment(s)
            w.writerow([s["Name"], role(s), f["Food"], f["SleepSite"], f["Reproduction"], group_kind(s), capacity(s), floor_of(s)])
    p2 = ROOT / "Data/Ecology/FoodWeb.csv"
    with open(p2, "w", encoding="utf-8", newline="") as fh:
        fh.write("# Nahrungsnetz (K52 §4, generiert). Räuber → Beute: gleiche Zone, Beute ≤ Räubergröße, ≥ 2 gemeinsame aktive Stunden.\n")
        w = csv.writer(fh)
        w.writerow(["Predator", "Prey", "Rank"])
        for p, qs in web.items():
            for i, q in enumerate(qs, 1):
                w.writerow([p, q, i])
    return len(WILD), sum(len(v) for v in web.values())


def pick_demo(zone="R01_Z02", n=12):
    """Deterministische Beispielfolge von Spawns (gleiche Eingaben → gleiche Folge)."""
    name = {s["Name"]: s["DisplayName"] for s in SPECIES}
    lines = ["| Tick | Stunde | Zelle | Art | Gruppengröße |", "|---|---|---|---|---|"]
    for t in range(int(n)):
        h = [6, 13, 20, 1][t % 4]
        sp, d, g = pick_spawn(zone, h, cell=t % 3, tick=t)
        lines.append(f"| {t} | {h:02d}:00 | {t % 3} | {d} | {g} |")
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "validate":
        e = validate()
        print("\n".join(e))
        print(f"Ökologie: {len(WILD)} Wildarten, {len(e)} Verstöße.")
        sys.exit(1 if e else 0)
    elif cmd == "build":
        print(build())
    elif cmd == "foodweb":
        print(foodweb_table(sys.argv[2]))
    elif cmd == "spawn":
        print(spawn_table(sys.argv[2], *(sys.argv[3:4] or ["Clear"])))
    elif cmd == "pop":
        print(pop_table(sys.argv[2]))
