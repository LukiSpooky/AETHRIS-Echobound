#!/usr/bin/env python3
"""Kreaturenkatalog: Validierung + Markdown-Generierung (K16 §10, ADR-075).

Aufrufe:
  gen_catalog.py validate                      -> prüft Data/Echos/*.csv gegen alle Kanon-Vorgaben
  gen_catalog.py render --range 1-32 --out F    -> erzeugt Katalogkapitel-Abschnitt für Kodex 1..32
Exitcode 1 bei Validierungsfehlern.
"""
from __future__ import annotations
import argparse, csv, pathlib, re, sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
sys.path.insert(0, str(ROOT / "tools" / "nameguard"))

TYPE_DE = {"Ember": "Glut", "Tide": "Flut", "Stone": "Stein", "Storm": "Sturm", "Bloom": "Blüte", "Frost": "Frost",
           "Void": "Leere", "Light": "Licht", "Venom": "Gift", "Metal": "Metall", "Spirit": "Geist", "Crystal": "Kristall",
           "Sound": "Klang", "Gravity": "Schwerkraft", "Arcane": "Arkan"}
RARITY_DE = {"Common": "Häufig", "Uncommon": "Ungewöhnlich", "Rare": "Selten", "VeryRare": "Sehr selten",
             "Legendary": "Legendär", "Mythical": "Mythisch"}
ACT_DE = {"Diurnal": "Tagaktiv", "Nocturnal": "Nachtaktiv", "Crepuscular": "Dämmerungsaktiv",
          "Cathemeral": "Unstet", "Midday": "Mittagsaktiv"}
NICHE_DE = {"Combat": "Kampf", "Field": "Feld", "Breeding": "Zucht", "Research": "Forschung", "Mount": "Reittier"}
MOUNT_DE = {"Ground": "Bodenreiten", "Swim": "Schwimmreiten", "Climb": "Kletterreiten", "Dig": "Grabreiten", "Fly": "Flugreiten"}
SIZE_RANGE = {"XS": (0, 0.3), "S": (0.3, 0.8), "M": (0.8, 1.6), "L": (1.6, 3.0), "XL": (3.0, 8.0), "XXL": (8.0, 999)}
# Kodex-Bereiche je Region (CANON §20)
KODEX_RANGES = {"R01": (1, 32), "R02": (33, 58), "R03": (59, 84), "R06": (85, 110), "R04": (111, 134),
                "R05": (135, 156), "R07": (157, 178), "R08": (179, 198), "R09": (199, 218), "R10": (219, 240)}
# Kernsummen-Spannen (CANON §71)
CORE_RANGES = {("Three", 1): (280, 340), ("Three", 2): (400, 460), ("Three", 3): (500, 560),
               ("Two", 1): (320, 380), ("Two", 2): (470, 530), ("Single", 1): (430, 520),
               ("Legendary", 1): (640, 680), ("Mythical", 1): (600, 660)}
LINE_TARGET = {"Three": 40, "Two": 45, "Single": 22, "Branch": 8}


def rows(rel):
    p = DATA / rel
    return list(csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#"))) if p.exists() else []


def lst(v):
    return [x for x in (v or "").split("|") if x]


class Validator:
    def __init__(self):
        self.errors: list[str] = []
        self.sp = rows("Echos/Species.csv")
        self.lore = {r["Name"]: r for r in rows("Echos/SpeciesLore.csv")}
        self.arch = {r["Name"]: r for r in rows("Echos/Archetypes.csv")}
        self.traits = {r["Name"] for r in rows("Echos/BehaviorTraits.csv")}
        self.zones = {r["Name"] for r in rows("World/Zones.csv")}
        self.typedist = {r["Name"]: r for r in rows("World/RegionTypeDistribution.csv")}

    def err(self, sid, msg):
        self.errors.append(f"{sid}: {msg}")

    def run(self):
        by_id = {r["Name"]: r for r in self.sp}
        nums = sorted(int(r["KodexNumber"]) for r in self.sp)
        if nums != list(range(1, len(nums) + 1)):
            self.err("Kodex", f"Nummern nicht lückenlos ab 1 (vorhanden bis {nums[-1] if nums else 0})")
        for r in self.sp:
            self.check_row(r, by_id)
        self.check_lines(by_id)
        self.check_type_distribution()
        self.check_names()
        self.check_archetypes(final=len(self.sp) == 256)
        return self.errors

    def check_row(self, r, by_id):
        sid, k = r["Name"], int(r["KodexNumber"])
        if sid != f"ECHO_{k:03d}":
            self.err(sid, "Id passt nicht zur Kodexnummer")
        kind, stage = r["LineKind"], int(r["Stage"])
        reg = r["Region"]
        if kind not in ("Legendary", "Mythical"):
            lo, hi = KODEX_RANGES.get(reg, (0, 0))
            if not lo <= k <= hi:
                self.err(sid, f"Kodex {k} außerhalb Bereich {reg} {lo}-{hi} (CANON §20)")
        if r["Archetype"] not in self.arch:
            self.err(sid, f"Archetyp {r['Archetype']} unbekannt")
        elif r["SizeClass"] not in lst(self.arch[r["Archetype"]]["Sizes"]):
            self.err(sid, f"Größe {r['SizeClass']} nicht erlaubt für {r['Archetype']}")
        h, w = float(r["HeightM"]), float(r["WeightKg"])
        lo, hi = SIZE_RANGE[r["SizeClass"]]
        if not lo <= h < hi:
            self.err(sid, f"Höhe {h} m passt nicht zu Größenklasse {r['SizeClass']}")
        dense_ok_types = {"Type.Spirit", "Type.Crystal", "Type.Metal", "Type.Gravity", "Type.Storm", "Type.Void"}
        vol_dm3 = max(0.001, (h * 10) ** 3 * 0.25)   # grobe Körpervolumen-Näherung (25 % der Hüllwürfel)
        dens = w / vol_dm3
        if not 0.1 <= dens <= 4 and not ({r["PrimaryType"], r["SecondaryType"]} & dense_ok_types):
            self.err(sid, f"Dichte {dens:.2f} kg/dm³ außerhalb 0,1–4 (CD-11)")
        for t in (r["PrimaryType"], r["SecondaryType"]):
            if t and t.split(".")[1] not in TYPE_DE:
                self.err(sid, f"Typ {t} unbekannt")
        if r["PrimaryType"] == r["SecondaryType"]:
            self.err(sid, "Primär- = Sekundärtyp")
        core = sum(int(r[s]) for s in ("HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed"))
        key = (kind, stage) if kind != "Branch" else None
        if key and key in CORE_RANGES:
            a, b = CORE_RANGES[key]
            if not a <= core <= b:
                self.err(sid, f"Kernsumme {core} außerhalb {a}-{b} für {kind} Stufe {stage}")
        for s in ("Precision", "Evasion"):
            if not 80 <= int(r[s]) <= 120:
                self.err(sid, f"{s} {r[s]} außerhalb 80–120")
        if not 190 <= int(r["Precision"]) + int(r["Evasion"]) <= 210:
            self.err(sid, "PRÄ+AUS außerhalb 190–210")
        if not r["Activity"].startswith("Behavior.Activity."):
            self.err(sid, "Aktivitätsmuster fehlt")
        tr = lst(r["Traits"])
        for t in tr:
            if t not in self.traits:
                self.err(sid, f"Merkmal {t} nicht im Vokabular")
        if len(tr) + 1 < 3:
            self.err(sid, "DR-02: < 3 Verhaltensmerkmale")
        if not lst(r["Niches"]):
            self.err(sid, "DR-05: keine Nische")
        if r["Rarity"] in ("Rare", "VeryRare"):
            need = 1 if r["Rarity"] == "Rare" else 2
            conds = lst(r["SpawnConditions"])
            if "Spawn.None" not in conds and len(conds) < need:
                self.err(sid, f"DR-15: {r['Rarity']} braucht ≥ {need} Bedingungen")
        for z in lst(r["Zones"]):
            if z not in self.zones:
                self.err(sid, f"Zone {z} unbekannt")
        if r["Mount"] and r["SizeClass"] in ("XS", "S") :
            self.err(sid, "CD-17: Reittier zu klein")
        if r["Mount"] == "Mount.Swim" and r["SizeClass"] == "M":
            pass
        elif r["Mount"] and r["SizeClass"] == "M":
            self.err(sid, "CD-17: nur Schwimmreiten ab M, sonst ab L")
        if not r["Category"].endswith("-Echo"):
            self.err(sid, "Kategorie muss auf „-Echo“ enden")
        if sid not in self.lore:
            self.err(sid, "Lore-Zeile fehlt")
        else:
            for f in ("LoreOrigin", "LoreBehavior", "LoreMyth", "LoreHumans", "KodexL4"):
                txt = self.lore[sid][f]
                if not txt or len(txt) > 320:
                    self.err(sid, f"Lore {f} leer oder > 320 Zeichen")
        for nxt in lst(r["EvolvesTo"]):
            if nxt in by_id:
                n = by_id[nxt]
                if n["Line"] != r["Line"]:
                    self.err(sid, f"Evolution {nxt} in anderer Linie")
                if int(n["Stage"]) != stage + 1:
                    self.err(sid, f"Evolution {nxt} hat Stufe {n['Stage']} ≠ {stage + 1}")
            if not r["EvoCondition"]:
                self.err(sid, "Evolution ohne Bedingung")

    def check_lines(self, by_id):
        lines = defaultdict(list)
        for r in self.sp:
            lines[r["Line"]].append(r)
        kinds = Counter()
        for lid, members in lines.items():
            genus = {m["ScientificName"].split()[0] for m in members}
            if len(genus) > 1:
                self.err(lid, f"Gattungen uneinheitlich {genus}")
            main = [m for m in members if m["LineKind"] != "Branch"]
            if main:
                kinds[main[0]["LineKind"]] += 1
            kinds["Branch"] += sum(1 for m in members if m["LineKind"] == "Branch")
        if len(self.sp) >= 240:
            for k, v in LINE_TARGET.items():
                if kinds[k] != v:
                    self.err("Linien", f"{k}: {kinds[k]} statt {v} (CANON §20)")
        self.line_counts = kinds

    def check_type_distribution(self):
        by_reg = defaultdict(Counter)
        count = Counter()
        for r in self.sp:
            if r["LineKind"] in ("Legendary", "Mythical"):
                continue
            by_reg[r["Region"]][r["PrimaryType"].split(".")[1]] += 1
            count[r["Region"]] += 1
        for reg, (lo, hi) in KODEX_RANGES.items():
            need = hi - lo + 1
            if count[reg] == need:   # Region vollständig → exakt prüfen
                target = self.typedist[reg]
                for t, n in target.items():
                    if t == "Name":
                        continue
                    if by_reg[reg][t] != int(n):
                        self.err(reg, f"Typverteilung {t}: {by_reg[reg][t]} ≠ {n} (CANON §45)")
            else:            # unvollständig → darf Ziel nicht überschreiten
                target = self.typedist[reg]
                for t, n in by_reg[reg].items():
                    if n > int(target[t]):
                        self.err(reg, f"Typ {t} bereits {n} > Ziel {target[t]}")

    def check_names(self):
        try:
            from nameguard import check_echo_name
        except Exception as e:   # pragma: no cover
            self.err("NameGuard", f"nicht ladbar: {e}")
            return
        names = [(r["DisplayName"], r["Line"]) for r in self.sp]
        for r in self.sp:
            if r["LineKind"] == "Legendary":
                continue  # Ursprungsstimmen dürfen Apostrophe tragen (K04 §4.5)
            others = [n for n, l in names if l != r["Line"]]
            for f in check_echo_name(r["DisplayName"], others, [], set()):
                self.err(r["Name"], f"Name {r['DisplayName']}: {f.rule} {f.message}")

    def check_archetypes(self, final):
        c = Counter(r["Archetype"] for r in self.sp)
        n = max(1, len(self.sp))
        for a, k in c.items():
            if len(self.sp) >= 64 and k / n > 0.12:
                self.err("Archetypen", f"{a} {k / n:.0%} > 12 %")
        if final:
            for a in self.arch:
                if c[a] / n < 0.02:
                    self.err("Archetypen", f"{a} {c[a] / n:.1%} < 2 %")


def tname(t):
    return TYPE_DE[t.split(".")[1]] if t else ""


def render(lo, hi):
    v = Validator()
    sp = [r for r in v.sp if lo <= int(r["KodexNumber"]) <= hi]
    traits = {r["Name"]: r["DisplayName"] for r in rows("Echos/BehaviorTraits.csv")}
    arch = {r["Name"]: r["DisplayName"] for r in rows("Echos/Archetypes.csv")}
    names = {r["Name"]: r["DisplayName"] for r in v.sp}
    out = []
    for r in sp:
        L = v.lore.get(r["Name"], {})
        types = tname(r["PrimaryType"]) + (f" / {tname(r['SecondaryType'])}" if r["SecondaryType"] else "")
        core = sum(int(r[s]) for s in ("HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed"))
        evo = ", ".join(f"{names.get(e, e)} (#{int(e[5:]):03d})" for e in lst(r["EvolvesTo"]))
        evo = f"→ {evo} · Bedingung: `{r['EvoCondition']}`" if evo else "keine weitere Entwicklung"
        conds = ", ".join(f"`{c}`" for c in lst(r["SpawnConditions"])) or "–"
        tr = ", ".join(traits.get(t, t) for t in lst(r["Traits"]))
        ni = ", ".join(NICHE_DE[n.split(".")[1]] for n in lst(r["Niches"]))
        mount = MOUNT_DE[r["Mount"].split(".")[1]] if r["Mount"] else "–"
        out.append(f"""### #{int(r['KodexNumber']):03d} {r['DisplayName']}

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `{r['Name']}` · {r['Line']} · Stufe {r['Stage']} ({r['LineKind']}) |
| Wissenschaftlich · Kategorie | *{r['ScientificName']}* · {r['Category']} |
| Typen | **{types}** |
| Archetyp · Größe · Gewicht | {r['Archetype']} {arch.get(r['Archetype'], '')} · {r['SizeClass']} · {r['HeightM'].replace('.', ',')} m · {r['WeightKg'].replace('.', ',')} kg |
| Region · Lebensraum | {r['Region']} · {r['Habitat']} |
| Seltenheit · Bedingungen · Zonen | {RARITY_DE[r['Rarity']]} · {conds} · {', '.join(lst(r['Zones'])) or '–'} |
| Aktivität · Merkmale | {ACT_DE[r['Activity'].split('.')[-1]]} · {tr} |
| Nischen · Rolle · Reiten | {ni} · {r['Role']} · {mount} |
| Basiswerte | HP {r['HP']} · ANG {r['Attack']} · VER {r['Defense']} · SAN {r['SpAttack']} · SVE {r['SpDefense']} · GES {r['Speed']} = **{core}** · PRÄ {r['Precision']} · AUS {r['Evasion']} · Wachstum {r['GrowthRate']} |
| Evolution | {evo} |
| Bindung | Rate {r['BondRate']} · Vorliebe `{r['BondLure']}` |
| Signatur (Konzept) | {r['SignatureConcept']} |
| Klangmal | {r['SoundMark']} |

- **Herkunft:** {L.get('LoreOrigin', '')}
- **Verhalten:** {L.get('LoreBehavior', '')}
- **Mythologie:** {L.get('LoreMyth', '')}
- **Beziehung zu Menschen:** {L.get('LoreHumans', '')}
- *Kodex-Notiz (Stufe 4):* {L.get('KodexL4', '')}
""")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["validate", "render", "stats"])
    ap.add_argument("--range", default="1-256")
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.cmd == "validate":
        errs = Validator().run()
        for e in errs:
            print("FEHLER:", e)
        print(f"Katalog: {len(rows('Echos/Species.csv'))} Arten, {len(errs)} Verstöße.")
        return 1 if errs else 0
    if a.cmd == "stats":
        v = Validator(); v.run()
        sp = v.sp
        print("Arten:", len(sp), "| Linien:", dict(v.line_counts))
        print("Seltenheit:", dict(Counter(r["Rarity"] for r in sp)))
        print("Archetypen:", dict(Counter(r["Archetype"] for r in sp)))
        print("Rollen:", dict(Counter(r["Role"] for r in sp)))
        return 0
    lo, hi = map(int, a.range.split("-"))
    md = render(lo, hi)
    if a.out:
        pathlib.Path(a.out).write_text(md, encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
