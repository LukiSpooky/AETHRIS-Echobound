#!/usr/bin/env python3
"""VFX-Referenzmodell (K58): Zuordnung Fähigkeit → Niagara-Vorlage, Typ-/Status-/Terrain-Abdeckung,
Worst-Case-Budget einer Kampfszene, Lichtblitz-Grenze (Photosensitivität).

Prüfregeln:
  VFX-01 jede Fähigkeit (Abilities.csv) hat eine Vorlage; jedes Crescendo eine eigene Signatur
  VFX-02 jeder Typ hat Motiv und farbunabhängige Form; Formen paarweise verschieden (Typen, Status)
  VFX-03 Worst-Case-Kampfszene (Trio 3+3, Crescendo + Fähigkeit + 6 Status + Terrain + Wetter) im Budget (PS5, Switch 2)
  VFX-04 Helligkeitswechsel ≤ 3 Hz: Klangmal-Puls (BPM × 1,3 Angst) und alle Story-VFX
  VFX-05 jede Typfarbe aus TypeColors.csv vorhanden (alle Modi)
  VFX-06 jedes Terrain (Terrains.csv) und jeder Status (StatusEffects.csv) hat eine Darstellung

Aufruf: aethris_vfx.py validate | templates | budget
"""
import csv, pathlib, re, sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


TYPES = {r["Name"]: r for r in rows("Data/VFX/TypeVfx.csv")}
STATUS = {r["Name"]: r for r in rows("Data/VFX/StatusVfx.csv")}
BUDGET = {r["Name"]: r for r in rows("Data/VFX/VfxBudgets.csv")}
STORY = rows("Data/VFX/StoryVfx.csv")
ABL = rows("Data/Abilities/Abilities.csv")

# Zielform → Vorlagenfamilie (Projektil/Strahl/Fläche/Selbst/Verbündete)
SHAPE = {"Single": "Projectile", "Enemies": "Area", "Row": "Line", "Field": "Field", "Self": "Self",
         "Allies": "AllyArea", "Ally": "AllyBeam", "AllyRow": "AllyLine"}
CAT = {"Physical": "Phys", "Special": "Spec", "Status": "Stat"}


def template(a):
    """Vorlagen-Name einer Fähigkeit. Typfarbe/-motiv sind Parameter, keine eigenen Assets."""
    k = a["Kind"]
    if k == "Crescendo":
        return f"NS_Cresc_{a['Name']}"                       # Signatur je Crescendo (Grundgerüst SVFX_CRESCENDO_BASE)
    if k == "Passive":
        return "NS_Abl_PassiveTrigger"                       # kurzer Auslöser-Puls am Echo
    if k == "Field":
        return "NS_Abl_FieldUse"                             # Feldfähigkeit in der Welt (K30)
    contact = "Contact" in a["Tags"].split("|")
    fam = "Melee" if contact and a["Target"] == "Single" else SHAPE.get(a["Target"], "Projectile")
    return f"NS_Abl_{CAT[a['Category']]}_{fam}"


def scale(a):
    """Größenparameter: 0,6 + Stärke/150 (Status-Fähigkeiten 0,8), gedeckelt 1,6."""
    try:
        p = int(a["Power"])
    except ValueError:
        p = 0
    return min(1.6, 0.6 + p / 150) if p else 0.8


def templates_table():
    c = Counter(template(a) for a in ABL if a["Kind"] in ("Active",))
    lines = ["| Vorlage | Fähigkeiten | Inhalt |", "|---|---|---|"]
    desc = {"Melee": "Kontakt: Ausholen, Schlagspur, Treffer am Ziel", "Projectile": "Wirken → Projektil → Treffer",
            "Area": "Wirken → Flächenwelle über alle Gegner", "Line": "Wirken → Linienwelle über eine Reihe",
            "Field": "Wirken → Feld-/Terrain-Aufbau", "Self": "Aura am Wirker", "AllyArea": "Welle über alle Verbündeten",
            "AllyBeam": "Strahl zu einem Verbündeten", "AllyLine": "Welle über eine eigene Reihe"}
    for t, n in sorted(c.items()):
        fam = t.split("_")[-1]
        lines.append(f"| `{t}` | {n} | {desc.get(fam, '')} |")
    p = sum(1 for a in ABL if a["Kind"] == "Passive")
    f = sum(1 for a in ABL if a["Kind"] == "Field")
    cr = sum(1 for a in ABL if a["Kind"] == "Crescendo")
    lines.append(f"| `NS_Abl_PassiveTrigger` | {p} | Passiv-Auslöser: Puls + Typ-Motiv am Echo (0,5 s) |")
    lines.append(f"| `NS_Abl_FieldUse` | {f} | Feldfähigkeit in der Welt: Typ-Motiv am Ziel (Fels, Wasser, Licht …) |")
    lines.append(f"| `NS_Cresc_ABL_U###` | {cr} | je Crescendo eine Signatur auf dem Grundgerüst |")
    lines.append(f"| **Σ** | **{len(ABL)}** | **{len(c) + 2} Vorlagen + {cr} Signaturen** |")
    return "\n".join(lines)


def examples(n=12):
    pick = [a for a in ABL if a["Kind"] == "Active"][::15][:int(n)]
    lines = ["| Fähigkeit | Typ | Kategorie | Ziel | Vorlage | Größe | Motiv |", "|---|---|---|---|---|---|---|"]
    for a in pick:
        t = TYPES[a["Type"]]
        lines.append(f"| {a['DisplayName']} | {t['DisplayName']} | {a['Category']} | {a['Target']} | `{template(a)}` | "
                     f"{scale(a):.2f}".replace(".", ",") + f" | {t['Motif'].split(',')[0]} |")
    return "\n".join(lines)


def scene(profile):
    """Worst Case Trio 3+3: ein Crescendo, eine Fähigkeit, 6 Echos × 2 Status, Terrain, Wetter, Klangmale, Ambiente."""
    col = "PS5Particles" if profile == "PS5" else "Switch2Particles"
    ms = "PS5GpuMs" if profile == "PS5" else "Switch2GpuMs"
    parts = {
        "VFX_CRESCENDO": 1.0, "VFX_ABILITY": 0.5, "VFX_STATUS": 1.0, "VFX_TERRAIN": 1.0,
        "VFX_WEATHER": 1.0, "VFX_ECHO": 0.3, "VFX_AMBIENT": 0.5, "VFX_UI3D": 1.0,
    }
    total_p = sum(int(BUDGET[k][col]) * f for k, f in parts.items())
    total_ms = sum(float(BUDGET[k][ms]) * f for k, f in parts.items())
    return total_p, total_ms


LIMITS = {"PS5": (300000, 4.0), "Switch2": (90000, 5.5)}   # Gesamtbudget VFX (K65: GPU-Anteil VFX)


def budget_table():
    lines = ["| Plattform | Partikel (Worst Case) | Grenze | GPU ms | Grenze | Ergebnis |", "|---|---|---|---|---|---|"]
    for p in ("PS5", "Switch2"):
        tp, tm = scene(p)
        lp, lm = LIMITS[p]
        ok = "✅" if tp <= lp and tm <= lm else "❌"
        de = lambda x: f"{x:,}".replace(",", ".")
        lines.append(f"| {'Switch 2' if p == 'Switch2' else p} | {de(int(tp))} | {de(lp)} | {tm:.2f} | {lm:.1f} | {ok} |".replace(".", ",", 0)
                     .replace(f"{tm:.2f}", f"{tm:.2f}".replace(".", ",")).replace(f"{lm:.1f} |", f"{lm:.1f}".replace(".", ",") + " |"))
    return "\n".join(lines)


def validate():
    err = []
    # VFX-01
    for a in ABL:
        if a["Type"] not in TYPES:
            err.append(f"VFX-01 {a['Name']}: Typ {a['Type']} ohne VFX-Sprache")
        if a["Kind"] == "Active" and a["Category"] not in CAT:
            err.append(f"VFX-01 {a['Name']}: Kategorie {a['Category']!r} ohne Vorlage")
    cres = [template(a) for a in ABL if a["Kind"] == "Crescendo"]
    if len(set(cres)) != len(cres):
        err.append("VFX-01 Crescendo-Signaturen nicht eindeutig")
    # VFX-02
    for name, d in (("Typ", TYPES), ("Status", STATUS)):
        shapes = Counter(r["Shape"] for r in d.values())
        for s, n in shapes.items():
            if not s or n > 1:
                err.append(f"VFX-02 {name}-Form {s!r} {n}× vergeben")
    # VFX-03
    for p in ("PS5", "Switch2"):
        tp, tm = scene(p)
        lp, lm = LIMITS[p]
        if tp > lp or tm > lm:
            err.append(f"VFX-03 {p}: {tp:.0f} Partikel / {tm:.2f} ms über {lp}/{lm}")
    # VFX-04
    for s in rows("Data/Echos/Species.csv"):
        m = re.search(r"(\d+)\s*BPM", s["SoundMark"])
        if m and int(m.group(1)) * 1.3 / 60 > 3:
            err.append(f"VFX-04 {s['Name']}: Klangmal-Puls bei Angst {int(m.group(1)) * 1.3 / 60:.2f} Hz > 3 Hz")
    for r in STORY:
        if float(r["FlashHz"]) > 3:
            err.append(f"VFX-04 {r['Name']}: {r['FlashHz']} Hz > 3 Hz")
    # VFX-05
    tc = {r["Name"]: r for r in rows("Data/Art/TypeColors.csv")}
    for t in TYPES:
        if t not in tc or any(not tc[t][m].startswith("#") for m in ("Normal", "Protan", "Deutan", "Tritan")):
            err.append(f"VFX-05 Typfarbe {t} fehlt")
    # VFX-06
    for r in rows("Data/Combat/Terrains.csv"):
        if r["Type"] not in TYPES:
            err.append(f"VFX-06 Terrain {r['Name']} ohne Typ-Darstellung")
    for r in rows("Data/Abilities/StatusEffects.csv"):
        if r["Name"] not in STATUS:
            err.append(f"VFX-06 Status {r['Name']} ohne Darstellung")
    return err


def report():
    e = validate()
    bpm = [int(m.group(1)) for s in rows("Data/Echos/Species.csv") for m in [re.search(r"(\d+)\s*BPM", s["SoundMark"])] if m]
    hz = f"{max(bpm) * 1.3 / 60:.2f}".replace(".", ",")
    return (f"Prüfregeln VFX-01–VFX-06 über {len(ABL)} Fähigkeiten, {len(TYPES)} Typen, {len(STATUS)} Status, "
            f"{len(rows('Data/Combat/Terrains.csv'))} Terrains, {len(STORY)} Story-VFX: **{len(e)} Verstöße**. "
            f"Schnellster Klangmal-Puls {max(bpm)} BPM → bei Angst (+30 %) {hz} Hz < 3 Hz.")


def terrain_table():
    lines = ["| Terrain | Typ | Overlay (Decal + Bodennebel) | Form |", "|---|---|---|---|"]
    for r in rows("Data/Combat/Terrains.csv"):
        t = TYPES[r["Type"]]
        lines.append(f"| {r['DisplayName']} | {t['DisplayName']} | {t['FieldLook']} | {t['Shape']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "templates":
        print(templates_table())
    elif cmd == "budget":
        print(budget_table())
    else:
        e = validate()
        print("\n".join(e) or "")
        print(report())
        sys.exit(1 if e else 0)
