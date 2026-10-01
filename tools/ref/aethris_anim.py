#!/usr/bin/env python3
"""Animationsbedarf (K57 §4): Clips je Archetyp aus AnimCategories.csv × Archetypen (Fortbewegung, Reitarten)
× Artenkatalog (Anzahl Arten, Crescendo-Signaturen). Ausgabe als Tabellen für K57/K67."""
import csv, pathlib, re
from collections import Counter
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


ARCH = {r["Name"]: r for r in rows("Data/Echos/Archetypes.csv")}
CATS = rows("Data/Anim/AnimCategories.csv")
SPEC = rows("Data/Echos/Species.csv")
CRES = rows("Data/Echos/CrescendoOptions.csv")


def signature_count(arch):
    """Arten des Archetyps, deren Signaturkonzept ein Crescendo beschreibt (K30: eigene Variante des ★-Crescendos)."""
    return sum(1 for s in SPEC if s["Archetype"] == arch and "Crescendo" in s["SignatureConcept"])


def clips_for(arch):
    a = ARCH[arch]
    loco = [x for x in a["Locomotion"].split("|") if x]
    mounts = [x for x in a["MountKinds"].split("|") if x]
    out = {}
    for c in CATS:
        cnt = c["Count"]
        if cnt.startswith("fix"):
            n = int(cnt.split()[1])
        elif cnt == "Locomotion":
            n = 4 * len(loco)
        elif cnt == "MountKinds":
            n = 5 * len(mounts)
        else:
            n = 1 + signature_count(arch)
        out[c["Name"]] = n
    return out


def table():
    cnt = Counter(s["Archetype"] for s in SPEC)
    lines = ["| Archetyp | Skelett | Arten | Fortbewegung | Reitarten | Clips je Archetyp | davon Signaturen |", "|---|---|---|---|---|---|---|"]
    total = 0
    for k, a in ARCH.items():
        c = clips_for(k)
        n = sum(c.values())
        total += n
        lines.append(f"| {k} {a['DisplayName']} | `{a['Skeleton']}` | {cnt.get(k, 0)} | {a['Locomotion'].replace('|', ', ')} | {a['MountKinds'].replace('|', ', ') or '–'} | {n} | {c['ANIM_CRESCENDO'] - 1} |")
    lines.append(f"| **Σ** | 18 Skelette | **{sum(cnt.values())}** | | | **{total}** | |")
    return "\n".join(lines)


def per_category():
    tot = Counter()
    for k in ARCH:
        tot.update(clips_for(k))
    lines = ["| Kategorie | Inhalt | Clips gesamt (alle Archetypen) |", "|---|---|---|"]
    for c in CATS:
        lines.append(f"| {c['DisplayName']} | {c['Content']} | {tot[c['Name']]} |")
    lines.append(f"| **Σ** | | **{sum(tot.values())}** |")
    return "\n".join(lines)


def human_table():
    hs = rows("Data/Anim/HumanAnimSets.csv")
    lines = ["| Satz | Wer | Inhalt | Clips | Quelle |", "|---|---|---|---|---|"]
    for h in hs:
        lines.append(f"| {h['Name']} | {h['Who']} | {h['Content']} | {h['Clips']} | {h['Source']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    print(table()); print(); print(per_category())
