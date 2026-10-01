#!/usr/bin/env python3
"""Musik-Referenzmodell (K55): Weltlied-Motiv, Ableitungen (Fragment, Umkehrung, Krebs, Arpeggio),
Stadtthemen nach CANON §56, Aethrische Skala, Typ-Töne, Echo-Rufprofile, Sturm-Quantisierung.

Aufruf: aethris_music.py build | motif | cities | calls R01
"""
import csv, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


NAMES = ["C", "C♯", "D", "E♭", "E", "F", "F♯", "G", "A♭", "A", "B", "H"]


def name(m):
    return f"{NAMES[m % 12]}{m // 12 - 1}"


# Weltlied-Motiv: (MIDI-Ton, Dauer in Vierteln). D4 A4 G4 F4 E4 C5 D5 – Quintsprung, Abstieg, Aufbruch zur Oktave.
MOTIF = [(62, 2), (69, 1), (67, 1), (65, 1.5), (64, 0.5), (72, 2), (74, 3)]
SCALE = [62, 64, 65, 67, 69, 71, 72]          # D-Dorisch (Aethrische Skala): D E F G A H C


def fragment(a, b):
    return MOTIF[a - 1:b]


def inversion(m=MOTIF):
    root = m[0][0]
    return [(2 * root - p, d) for p, d in m]


def retrograde(m=MOTIF):
    return list(reversed(m))


def arpeggio(idx=(1, 3, 5, 7)):
    return [MOTIF[i - 1] for i in idx]


def fmt(seq):
    return " – ".join(f"{name(p)} ({str(d).replace('.', ',')})" for p, d in seq)


CITIES = [
    ("Eichenhall", "Töne 1–2", lambda: fragment(1, 2), "Weite Quinte; Laute + Holzbläser, Lindenfest-Tanz"),
    ("Kharsholm", "Töne 2–3", lambda: fragment(2, 3), "Schritt abwärts; Männerchor, Ambosse im Takt der Schichten"),
    ("Morvenfurt", "Töne 3–4", lambda: fragment(3, 4), "Nachtmusik; Klarinette, Laternenglöckchen"),
    ("Saltrand-Hafen", "Töne 4–5", lambda: fragment(4, 5), "Halbton; Akkordeon, Wellen, Glockenflut"),
    ("Qasr Sahrun", "Töne 5–6", lambda: fragment(5, 6), "Großer Sprung; Saiten mit Bünden, Wüstenwind"),
    ("Schlackenwehr", "Töne 6–7", lambda: fragment(6, 7), "Aufbruch zur Oktave; Schmiedeglocken, Blech"),
    ("Hvitmark", "Umkehrung", lambda: inversion(), "Gespiegelt nach unten; Nyckelharpa-artige Streicher, Gedenken"),
    ("Dorunsruh", "Krebs, fragmentiert", lambda: retrograde()[::2], "Rückwärts, lückenhaft; Streicherkanon, Glyphenhall"),
    ("Prismara", "Arpeggio 1/3/5/7", lambda: arpeggio(), "Gebrochen; Glasharfe, jede Farbe ein Ton"),
    ("Aerion", "vollständig", lambda: MOTIF, "Das ganze Motiv – einsam, ohne Begleitung (Isolation)"),
]


def motif_table():
    lines = ["| Ton | Name | Dauer (Viertel) | Skalenstufe | Funktion |", "|---|---|---|---|---|"]
    fn = ["Grundton (Ruhe)", "Quintsprung (Ruf)", "Rückschritt", "Seufzer", "Leitton nach unten", "Aufbruch", "Oktave (Ankunft)"]
    for i, (p, d) in enumerate(MOTIF, 1):
        q = p
        while q > 73:
            q -= 12
        deg = SCALE.index(q) + 1 if q in SCALE else (1 if q == 74 else "–")
        lines.append(f"| {i} | {name(p)} | {str(d).replace('.', ',')} | {deg} | {fn[i - 1]} |")
    return "\n".join(lines)


def derived_table():
    lines = ["| Ableitung | Töne | Verwendung |", "|---|---|---|",
             f"| Original | {fmt(MOTIF)} | Weltlied, Aerion, Finale „Neues Lied“ |",
             f"| Umkehrung (um D4) | {fmt(inversion())} | Hvitmark, Gedenken |",
             f"| Krebs | {fmt(retrograde())} | Dorunsruh, Kael-Thema (vom Wärter-Thema) |",
             f"| Arpeggio 1/3/5/7 | {fmt(arpeggio())} | Prismara, Ilen-Motiv |",
             f"| Krone (unisono) | {fmt([(62, 4)] * 1)} in allen Oktaven D1–D7 | Krone-Motiv |",
             "| Stille | " + " – ".join(fmt([t]) if i % 2 == 0 else f"Pause ({str(t[1]).replace('.', ',')})" for i, t in enumerate(MOTIF)) + " | Stille-Motiv (Töne 2/4/6 durch Pausen ersetzt) |"]
    return "\n".join(lines)


def cities_table():
    lines = ["| Stadt | Fragment (CANON §56) | Töne | Charakter |", "|---|---|---|---|"]
    for c, f, fnc, ch in CITIES:
        lines.append(f"| {c} | {f} | {fmt(fnc())} | {ch} |")
    return "\n".join(lines)


TYPES = {r["Name"]: r for r in rows("Data/Audio/TypeTones.csv")}
OCTAVE = {"XS": 6, "S": 5, "M": 4, "L": 3, "XL": 2, "XXL": 1}
BPM_DEFAULT = {"XS": 96, "S": 72, "M": 56, "L": 44, "XL": 36, "XXL": 28}


def call_profile(s):
    tp = s["PrimaryType"].split(".")[-1]
    t = TYPES[tp]
    deg = int(t["Degree"])
    m = re.search(r"(\d+)\s*BPM", s["SoundMark"])
    bpm = int(m.group(1)) if m else BPM_DEFAULT[s["SizeClass"]]
    traits = {x.split(".")[-1] for x in s["Traits"].split("|") if x}
    rhythm = "Rufreihe im festen Takt" if "Singer" in traits else (
        "Klickfolge (Ortung)" if "Echolocator" in traits else (
            "Schwarmchor (gestaffelt)" if "Swarm" in traits else (
                "Nachahmung fremder Rufe" if "Mimic" in traits else "Einzelruf")))
    if deg == 0:
        pitch = "Pause (Rauschen)"
    else:
        pitch = name(SCALE[deg - 1] - 12 * (4 - OCTAVE[s["SizeClass"]]))
    sec = s["SecondaryType"].split(".")[-1] if s["SecondaryType"] else ""
    overtone = f"+ Oberton {TYPES[sec]['Timbre'].split(' + ')[0]}" if sec else ""
    return {"Name": s["Name"], "Display": s["DisplayName"], "Type": tp, "Pitch": pitch, "BPM": bpm, "Rhythm": rhythm,
            "Timbre": f"{t['Timbre']} {overtone}".strip()}


def build():
    sp = rows("Data/Echos/Species.csv")
    with open(ROOT / "Data/Audio/EchoCalls.csv", "w", encoding="utf-8", newline="") as fh:
        fh.write("# Rufprofile je Art (K55 §5, generiert von tools/ref/aethris_music.py). Tonhöhe aus Primärtyp (Skalenstufe) und Größe (Oktave); Tempo aus dem Klangmal (BPM) oder Größe.\n")
        w = csv.writer(fh)
        w.writerow(["Name", "Pitch", "BPM", "Rhythm", "Timbre"])
        for s in sp:
            c = call_profile(s)
            w.writerow([c["Name"], c["Pitch"], c["BPM"], c["Rhythm"], c["Timbre"]])
    return len(sp)


def calls_table(region, limit=14):
    sp = [s for s in rows("Data/Echos/Species.csv") if s["Region"] == region][:int(limit)]
    lines = ["| Art | Typ | Grundton | Tempo | Rhythmus | Klangfarbe |", "|---|---|---|---|---|---|"]
    for s in sp:
        c = call_profile(s)
        lines.append(f"| {c['Display']} | {c['Type']} | {c['Pitch']} | {c['BPM']} BPM | {c['Rhythm']} | {c['Timbre']} |")
    return "\n".join(lines)


def quantize(cents_list=(-37, 12, 145, 230, 498, 615, 880, 1022)):
    """Resonanzsturm: freie Tonhöhen (Cent über D4) werden auf die nächste Skalenstufe gezogen."""
    steps = [(p - 62) * 100 for p in SCALE] + [1200]
    lines = ["| Ruf (Cent über D4) | Nächste Stufe | Ziel | Verschiebung |", "|---|---|---|---|"]
    for c in cents_list:
        tgt = min(steps, key=lambda s: abs(s - c))
        lines.append(f"| {c} | {steps.index(tgt) % 7 + 1} | {name(62 + tgt // 100)} | {tgt - c:+d} ct |")
    return "\n".join(lines)


def types_table():
    lines = ["| Typ | Skalenstufe | Grundton (M) | Klangfarbe | Familie | Charakter |", "|---|---|---|---|---|---|"]
    for k, t in TYPES.items():
        d = int(t["Degree"])
        lines.append(f"| {k} | {d or 'Pause'} | {name(SCALE[d - 1]) if d else '–'} | {t['Timbre']} | {t['Family']} | {t['Character']} |")
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "motif"
    if cmd == "build":
        print(build(), "Rufprofile")
    elif cmd == "cities":
        print(cities_table())
    elif cmd == "calls":
        print(calls_table(sys.argv[2]))
    else:
        print(motif_table()); print(derived_table())
