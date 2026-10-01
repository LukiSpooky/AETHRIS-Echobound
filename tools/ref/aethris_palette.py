#!/usr/bin/env python3
"""Typfarben-Prüfer (K56 §3): CIEDE2000-Abstände, Farbsehschwäche-Simulation (Machado 2009, Schweregrad 1,0),
automatische Farbenblind-Paletten (Helligkeitsspreizung), Kontrast zum UI-Grund.

Aufruf: aethris_palette.py report | build
"""
import csv, math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]

# Arbeitsstand K17 §9.1 / CANON §78
BASE = {
    "Ember": ("Glut", "#E8562A"), "Tide": ("Flut", "#2E8BC0"), "Stone": ("Stein", "#8C7B65"), "Storm": ("Sturm", "#7FD1E8"),
    "Bloom": ("Blüte", "#5DAA4C"), "Frost": ("Frost", "#BFE6F5"), "Void": ("Leere", "#2B2240"), "Light": ("Licht", "#F6D86B"),
    "Venom": ("Gift", "#8E4FB0"), "Metal": ("Metall", "#9AA3AD"), "Spirit": ("Geist", "#B7A4E0"), "Crystal": ("Kristall", "#E28FC6"),
    "Sound": ("Klang", "#F2A93B"), "Gravity": ("Schwerkraft", "#4B5BA6"), "Arcane": ("Arkan", "#3FB8A8"),
}
SYMBOL = {"Ember": "Flamme in Dreieck", "Tide": "Welle in Kreis", "Stone": "Sechseck, gefüllt", "Storm": "Spirale",
          "Bloom": "Blatt in Tropfen", "Frost": "Sechszackiger Stern", "Void": "Ring (Negativraum)", "Light": "Strahlenkranz",
          "Venom": "Drei Tropfen", "Metal": "Quadrat mit Niet", "Spirit": "Halbmond mit Schleier", "Crystal": "Raute mit Facette",
          "Sound": "Drei Bögen (Schall)", "Gravity": "Kreis mit Punkt (Orbit)", "Arcane": "Glyphe (Achtstern)"}
# Finale Anpassungen der Normalpalette (K56): Leere aufgehellt (Lesbarkeit auf dunklem UI-Grund), Frost etwas kühler
FINAL_OVERRIDE = {"Void": "#4A3A6E", "Frost": "#C9EEF7"}
UI_BG = "#1C1B24"
THRESH_NORMAL = 10.0   # ΔE2000
THRESH_CVD = 6.0

CVD = {  # Machado et al. 2009, Schweregrad 1.0 (lineares RGB)
    "Protan": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    "Deutan": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    "Tritan": [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]],
}


def hex2rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def rgb2hex(c):
    return "#" + "".join(f"{max(0, min(255, round(v * 255))):02X}" for v in c)


def lin(c):
    return [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c]


def delin(c):
    return [12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055 for v in c]


def rgb2lab(c):
    r, g, b = lin(c)
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return [116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)]


def lab2rgb(lab):
    L, a, b = lab
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    finv = lambda t: t ** 3 if t ** 3 > 0.008856 else (t - 16 / 116) / 7.787
    x, y, z = finv(fx) * 0.95047, finv(fy), finv(fz) * 1.08883
    r = 3.2406 * x - 1.5372 * y - 0.4986 * z
    g = -0.9689 * x + 1.8758 * y + 0.0415 * z
    bb = 0.0557 * x - 0.2040 * y + 1.0570 * z
    return [max(0.0, min(1.0, v)) for v in delin([max(0.0, v) for v in (r, g, bb)])]


def de2000(l1, l2):
    L1, a1, b1 = l1
    L2, a2, b2 = l2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360
    h2p = math.degrees(math.atan2(b2, a2p)) % 360
    dLp, dCp = L2 - L1, C2p - C1p
    dh = h2p - h1p
    if C1p * C2p == 0:
        dh = 0
    elif dh > 180:
        dh -= 360
    elif dh < -180:
        dh += 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dh / 2))
    Lm, Cmp = (L1 + L2) / 2, (C1p + C2p) / 2
    hm = (h1p + h2p) / 2 if abs(h1p - h2p) <= 180 else (h1p + h2p + 360) / 2
    if C1p * C2p == 0:
        hm = h1p + h2p
    T = 1 - 0.17 * math.cos(math.radians(hm - 30)) + 0.24 * math.cos(math.radians(2 * hm)) + 0.32 * math.cos(math.radians(3 * hm + 6)) - 0.20 * math.cos(math.radians(4 * hm - 63))
    dTh = 30 * math.exp(-((hm - 275) / 25) ** 2)
    Rc = 2 * math.sqrt(Cmp ** 7 / (Cmp ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lm - 50) ** 2 / math.sqrt(20 + (Lm - 50) ** 2)
    Sc, Sh = 1 + 0.045 * Cmp, 1 + 0.015 * Cmp * T
    Rt = -math.sin(math.radians(2 * dTh)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh))


def simulate(hexc, mode):
    if mode == "Normal":
        return hex2rgb(hexc)
    m = CVD[mode]
    c = lin(hex2rgb(hexc))
    s = [sum(m[i][j] * c[j] for j in range(3)) for i in range(3)]
    return delin([max(0.0, min(1.0, v)) for v in s])


def final_palette():
    return {k: FINAL_OVERRIDE.get(k, v[1]) for k, v in BASE.items()}


def min_pairs(pal, mode, n=5):
    labs = {k: rgb2lab(simulate(v, mode)) for k, v in pal.items()}
    keys = list(pal)
    pairs = sorted(((de2000(labs[a], labs[b]), a, b) for i, a in enumerate(keys) for b in keys[i + 1:]))
    return pairs[:n]


def cvd_palette(mode, iters=400):
    """Greedy: spreize die Helligkeit der jeweils engsten Paare (in Lab), bis alle Paare ≥ Schwelle unter Simulation."""
    pal = dict(final_palette())
    for _ in range(iters):
        d, a, b = min_pairs(pal, mode, 1)[0]
        if d >= THRESH_CVD:
            break
        la, lb = rgb2lab(hex2rgb(pal[a])), rgb2lab(hex2rgb(pal[b]))
        step = 2.0
        if la[0] >= lb[0]:
            la[0] = min(96, la[0] + step); lb[0] = max(8, lb[0] - step)
        else:
            la[0] = max(8, la[0] - step); lb[0] = min(96, lb[0] + step)
        pal[a], pal[b] = rgb2hex(lab2rgb(la)), rgb2hex(lab2rgb(lb))
    return pal


def rel_lum(c):
    r, g, b = lin(c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(h1, h2):
    a, b = rel_lum(hex2rgb(h1)), rel_lum(hex2rgb(h2))
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def build():
    pals = {"Normal": final_palette()}
    for m in CVD:
        pals[m] = cvd_palette(m)
    p = ROOT / "Data/Art/TypeColors.csv"
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write("# Typfarben final (K56 §3, generiert von tools/ref/aethris_palette.py). Normal = Standard; Protan/Deutan/Tritan = Farbenblind-Modi (K54 ACC_COLORBLIND). Symbole farbunabhängig (K17 §9.1).\n")
        w = csv.writer(fh)
        w.writerow(["Name", "DisplayName", "Normal", "Protan", "Deutan", "Tritan", "Symbol", "ContrastOnUI"])
        for k, (dn, _) in BASE.items():
            w.writerow([k, dn, pals["Normal"][k], pals["Protan"][k], pals["Deutan"][k], pals["Tritan"][k], SYMBOL[k],
                        f"{contrast(pals['Normal'][k], UI_BG):.1f}".replace(".", ",")])
    return pals


def check():
    rows = list(csv.DictReader(l for l in open(ROOT / "Data/Art/TypeColors.csv", encoding="utf-8") if not l.startswith("#")))
    err = []
    for mode in ("Normal", "Protan", "Deutan", "Tritan"):
        pal = {r["Name"]: r[mode] for r in rows}
        d, a, b = min_pairs(pal, mode, 1)[0]
        th = THRESH_NORMAL if mode == "Normal" else THRESH_CVD
        if d < th:
            err.append(f"AR-01 {mode}: {a}/{b} ΔE2000 {d:.1f} < {th}")
    for r in rows:
        if contrast(r["Normal"], UI_BG) < 1.6:
            err.append(f"AR-02 {r['Name']}: Kontrast zum UI-Grund {contrast(r['Normal'], UI_BG):.1f} < 1,6 (Symbol braucht Kontur)")
    return err


def table():
    rows = list(csv.DictReader(l for l in open(ROOT / "Data/Art/TypeColors.csv", encoding="utf-8") if not l.startswith("#")))
    lines = ["| Typ | Normal | Protan | Deutan | Tritan | Symbol | Kontrast zu UI-Grund |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['DisplayName']} | `{r['Normal']}` | `{r['Protan']}` | `{r['Deutan']}` | `{r['Tritan']}` | {r['Symbol']} | {r['ContrastOnUI']} : 1 |")
    return "\n".join(lines)


def pairs_report():
    lines = ["| Modus | Engstes Paar vorher (Arbeitsstand K17) | ΔE2000 | Engstes Paar final | ΔE2000 | Schwelle |", "|---|---|---|---|---|---|"]
    base = {k: v[1] for k, v in BASE.items()}
    rows = list(csv.DictReader(l for l in open(ROOT / "Data/Art/TypeColors.csv", encoding="utf-8") if not l.startswith("#")))
    dn = {k: v[0] for k, v in BASE.items()}
    for mode in ("Normal", "Protan", "Deutan", "Tritan"):
        d0, a0, b0 = min_pairs(base, mode, 1)[0]
        pal = {r["Name"]: r[mode] for r in rows}
        d1, a1, b1 = min_pairs(pal, mode, 1)[0]
        th = THRESH_NORMAL if mode == "Normal" else THRESH_CVD
        lines.append(f"| {mode} | {dn[a0]} / {dn[b0]} | {d0:.1f} | {dn[a1]} / {dn[b1]} | {d1:.1f} | {th:.0f} |".replace(".", ","))
    return "\n".join(lines)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "report"
    if cmd in ("build", "validate"):
        if cmd == "build":
            build()
        e = check()
        print("\n".join(e))
        print(f"Typfarben: {len(e)} Verstöße.")
        sys.exit(1 if e else 0)
    else:
        print(pairs_report())
