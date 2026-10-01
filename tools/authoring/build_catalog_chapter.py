#!/usr/bin/env python3
"""Erzeugt ein Katalogkapitel (K20–K27) vollständig aus den Daten (ADR-075).
Aufruf: build_catalog_chapter.py K20 "Kreaturenkatalog 1" 1 32 "R01 Verdanthain" intro.md next_title
"""
import sys, csv, pathlib, subprocess
from collections import Counter, OrderedDict
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import gen_catalog as gc

def main():
    kid, title, lo, hi, regions, intro_path, next_line = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6], sys.argv[7]
    v = gc.Validator(); errs = v.run()
    sp = [r for r in v.sp if lo <= int(r["KodexNumber"]) <= hi]
    names = {r["Name"]: r["DisplayName"] for r in v.sp}
    intro = pathlib.Path(intro_path).read_text(encoding="utf-8") if intro_path != "-" else ""
    # Übersicht
    ov = ["| Kodex | Name | Typen | Linie · Stufe | Archetyp | Größe | Seltenheit | Rolle |", "|---|---|---|---|---|---|---|---|"]
    for r in sp:
        t = gc.tname(r["PrimaryType"]) + (f"/{gc.tname(r['SecondaryType'])}" if r["SecondaryType"] else "")
        ov.append(f"| #{int(r['KodexNumber']):03d} | **{r['DisplayName']}** | {t} | {r['Line']} · {r['Stage']} ({r['LineKind']}) | {r['Archetype']} | {r['SizeClass']} | {gc.RARITY_DE[r['Rarity']]} | {r['Role']} |")
    # Linienbäume
    lines = OrderedDict()
    for r in sp: lines.setdefault(r["Line"], []).append(r)
    tree = ["```"]
    for lid, mem in lines.items():
        main = [m for m in mem if m["LineKind"] != "Branch"]; br = [m for m in mem if m["LineKind"] == "Branch"]
        chain = []
        for m in main:
            cond = next((x["EvoCondition"] for x in main if m["Name"] in x["EvolvesTo"].split("|")), "")
            chain.append(m["DisplayName"] if not chain else f"──[{cond.split(') | (')[0].strip('()')}]──► {m['DisplayName']}")
        tree.append(f"{lid}  " + " ".join(chain))
        for b in br:
            prev = next(x for x in main if b["Name"] in x["EvolvesTo"].split("|"))
            cond = prev["EvoCondition"].split(") | (")[-1].strip("()")
            tree.append(f"{' ' * 6}└─ Zweig von {prev['DisplayName']} ──[{cond}]──► {b['DisplayName']}")
    tree.append("```")
    # Kennzahlen
    regs = sorted({r["Region"] for r in sp})
    kz = ["| Kennzahl | Wert |", "|---|---|",
          f"| Arten in diesem Kapitel | {len(sp)} |",
          f"| Linientypen | " + ", ".join(f"{k} {v}" for k, v in Counter((m['LineKind']) for m in sp).items()) + " (Arten je Typ) |",
          f"| Primärtypen | " + ", ".join(f"{gc.tname(k)} {v}" for k, v in sorted(Counter(r['PrimaryType'] for r in sp).items(), key=lambda x: -x[1])) + " |",
          f"| Archetypen | " + ", ".join(f"{k} {v}" for k, v in sorted(Counter(r['Archetype'] for r in sp).items())) + " |",
          f"| Wildseltenheit (ohne reine Evolutionsformen) | " + ", ".join(f"{gc.RARITY_DE[k]} {v}" for k, v in Counter(r['Rarity'] for r in sp if 'Spawn.None' not in r['SpawnConditions']).items()) + " |",
          f"| Nur durch Evolution/Zucht (`Spawn.None`) | {sum(1 for r in sp if 'Spawn.None' in r['SpawnConditions'])} |",
          f"| Reittiere | " + (", ".join(f"{r['DisplayName']} ({gc.MOUNT_DE[r['Mount'].split('.')[1]]})" for r in sp if r['Mount']) or "–") + " |",
          f"| Validator (`tools/gen_catalog.py validate`, Gesamtkatalog) | **{len(errs)} Verstöße** |"]
    entries = gc.render(lo, hi)
    out = f"""# {kid} · {title}

| Feld | Wert |
|---|---|
| Dokument | Kapitel {kid[1:]} von 68 · Monster Bible – Katalog |
| Owner | Creature Design Lead |
| Mitwirkende | RPG Systems Designer, Narrative Writer, Concept Art, Legal (Clean-Room) |
| Baut auf | K16 (Designregeln, Schema), K17 (Typen), K18 (Werte), K19 (Evolution), CANON §20, §45 |
| Status | ✅ Freigegeben |
| Datenquelle | `Data/Echos/Species.csv`, `Data/Echos/SpeciesLore.csv` (Kodex #{lo:03d}–#{hi:03d}); Authoring: `tools/authoring/` |
| Region(en) | {regions} |

> Dieses Kapitel ist **aus den Daten generiert** (ADR-075). Änderungen erfolgen ausschließlich in den Daten; danach wird das Kapitel neu erzeugt.

{intro}

## Übersicht

{chr(10).join(ov)}

## Linien & Evolutionen

{chr(10).join(tree)}

## Kennzahlen & Validierung

{chr(10).join(kz)}

## Einträge

{entries}

## Kapitel-Checkliste

- [x] {len(sp)} Arten mit allen Briefing-Basisdaten (Name, wissenschaftlicher Name, Kategorie, Größe, Gewicht, Lebensraum, Seltenheit)
- [x] Lore je Art: Herkunft, Verhalten, Mythologie, Beziehung zu Menschen (+ Kodex-Notiz)
- [x] Evolution je Linie mit geprüfter Bedingung (K19-Sprache)
- [x] Basiswerte innerhalb der Spannen (K16 §6), Wachstum, EP-/Schliff-Ertrag (K18)
- [x] Verhalten, Aktivität, Nischen, Rolle, Bindungsdaten, Klangmal, Signaturkonzept
- [x] Typverteilung der Region(en) gemäß CANON §45 (Validator)
- [x] Daten im Repository, Kapitel generiert

➡️ **Nächstes Kapitel: {next_line}**
"""
    path = ROOT / "docs/kapitel" / f"{kid}_{title.replace(' ', '_').replace('–', '-')}.md"
    path.write_text(out, encoding="utf-8")
    print(path.name, len(out.split()), "Wörter")

if __name__ == "__main__":
    main()
