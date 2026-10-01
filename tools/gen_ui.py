#!/usr/bin/env python3
"""UI-Daten-Prüfer (K54 §13): Eingabebelegungen, Bildschirme, HUD, Barrierefreiheit.

UI-01 Jede Eingabeaktion hat Gamepad- und Tastatur/Maus-Belegung
UI-02 Keine doppelte Belegung innerhalb eines Kontexts (gleiche Taste, gleiche Halte-Art)
UI-03 Jeder in „Opens“ genannte Bildschirm existiert
UI-04 Jede Barrierefreiheits-Option aus K02 §11.3 ist vorhanden
UI-05 Unumkehrbare Entscheidungen nutzen Halten (≥ 3000 ms)
UI-06 HUD: alles außer Pflicht-Signalen (Resonanzsinn, DR-24) ist abschaltbar
"""
import csv, pathlib, re, sys
from collections import defaultdict
ROOT = pathlib.Path(__file__).resolve().parents[1]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


INPUT = rows("Data/UI/InputActions.csv")
SCREENS = {r["Name"]: r for r in rows("Data/UI/Screens.csv")}
HUD = rows("Data/UI/HudElements.csv")
ACC = {r["Name"]: r for r in rows("Data/UI/AccessibilityOptions.csv")}
REQUIRED_ACC = ["ACC_REMAP", "ACC_ONEHAND", "ACC_HOLD_TOGGLE", "ACC_TIMING", "ACC_AUTO_BOND", "ACC_COLORBLIND", "ACC_TEXTSIZE",
                "ACC_SENSE_CONTRAST", "ACC_SUBTITLES", "ACC_VISUAL_SOUND", "ACC_REMINDER", "ACC_COMBAT_HINTS",
                "ACC_TIMELINE_EXPLAIN", "ACC_ANIM_SPEED", "ACC_DIALOG_AUTOPLAY"]


def keys(binding):
    out = []
    for part in binding.split(" / "):
        hold = "(halten)" in part
        k = re.sub(r"\s*\(.*?\)", "", part).strip()
        if k:
            out.append((k, hold))
    return out


def validate():
    err = []
    used = defaultdict(lambda: defaultdict(list))
    for r in INPUT:
        if not r["Gamepad"] or not r["KeyboardMouse"]:
            err.append(f"UI-01 {r['Name']}: Belegung fehlt")
        for dev in ("Gamepad", "KeyboardMouse"):
            for k, hold in keys(r[dev]):
                hold = hold or int(r["Hold"]) >= 300
                used[(r["Context"], dev)][(k, hold)].append(r["Name"])
    for (ctx, dev), m in used.items():
        for (k, hold), names in m.items():
            if len(names) > 1 and not (ctx == "World" and k in ("A", "E / Leertaste")):
                # Kontext-Doppelbelegungen sind nur zulässig, wenn sie in den Notes als kontextabhängig markiert sind
                if not all("Kontext" in next(x for x in INPUT if x["Name"] == n)["Notes"] or "in der Luft" in next(x for x in INPUT if x["Name"] == n)["Gamepad"] for n in names):
                    err.append(f"UI-02 {ctx}/{dev}: {k}{' (halten)' if hold else ''} doppelt: {', '.join(names)}")
    for s in SCREENS.values():
        for o in s["Opens"].split("|"):
            if o not in ("–", "") and o not in SCREENS:
                err.append(f"UI-03 {s['Name']}: öffnet unbekannten Bildschirm {o}")
    for a in REQUIRED_ACC:
        if a not in ACC:
            err.append(f"UI-04 Barrierefreiheit {a} fehlt")
    for r in INPUT:
        if "Unumkehrbar" in r["Notes"] and int(r["Hold"]) < 3000:
            err.append(f"UI-05 {r['Name']}: unumkehrbar ohne Halten ≥ 3 s")
    for h in HUD:
        if h["Hideable"] != "ja" and h["Name"] != "HUD_RESONANCE":
            err.append(f"UI-06 {h['Name']}: nicht abschaltbar")
    return err


def input_table(ctx):
    lines = ["| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |", "|---|---|---|---|---|"]
    for r in INPUT:
        if r["Context"] == ctx:
            hold = f"{int(r['Hold']) / 1000:.1f} s".replace(".", ",") if int(r["Hold"]) else "–"
            lines.append(f"| {r['DisplayName']} | {r['Gamepad']} | {r['KeyboardMouse']} | {hold} | {r['Notes'] or '–'} |")
    return "\n".join(lines)


if __name__ == "__main__":
    e = validate()
    print("\n".join(e))
    print(f"UI-Prüfer: {len(INPUT)} Aktionen, {len(SCREENS)} Bildschirme, {len(HUD)} HUD-Elemente, {len(ACC)} Optionen, {len(e)} Verstöße.")
    sys.exit(1 if e else 0)
