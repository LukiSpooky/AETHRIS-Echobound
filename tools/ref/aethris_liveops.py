#!/usr/bin/env python3
"""LiveOps-Referenzmodell (K68): Jahreskalender der Events, Release-Plan, Kosmetik-Shop, Live-Kennzahlen.

Prüfregeln:
  LO-01 höchstens 3 zeitlich begrenzte Events gleichzeitig (Zirkel-Chronik ausgenommen)
  LO-02 jedes Event mit spielerischem Inhalt hat einen Offline-Weg zum gleichen Inhalt (DR-19)
  LO-03 Event-Belohnungen nur kosmetisch/Kodex (keine Echos, Siegel, Sol, Werte, Morphs)
  LO-04 Shop: nur erlaubte Kategorien (K01 §14), keine verbotenen Inhalte, feste Preise, auch erspielbar
  LO-05 Erweiterungen: je 30–40 Echos, Kodex-Nummern lückenlos ab #257
  LO-06 Jahr 1: kostenloses Update oder Saison mindestens alle 3 Monate
  LO-07 Live-Kennzahlen: jede mit Alarm/Handlung; keine Handlung führt Druckmechaniken ein (DR-23)

Aufruf: aethris_liveops.py validate | calendar
"""
import csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


EV = {r["Name"]: r for r in rows("Data/LiveOps/Events.csv")}
RP = rows("Data/LiveOps/ReleasePlan.csv")
SHOP = rows("Data/LiveOps/ShopCatalog.csv")
KPI = rows("Data/LiveOps/LiveKPIs.csv")
ALLOWED_SHOP = {"Wärter-Kleidung", "Gleiter-Skins", "Hain-Deko"}
FORBIDDEN = re.compile(r"\b(Echo(?!-)|Echos|Siegel|Sol\b|Morph|Werte?\b|Zufall|Lootbox|%|Anlage)", re.I)
PRESSURE = re.compile(r"Login|Daily|Täglich|FOMO|Countdown|Energie", re.I)

# Jahr 1 (Wochen ab Launch, W1 = Launch-Woche Nov 2030)
SCHEDULE = {
    "EV_STORMNIGHT": [w for w in range(4, 53, 6)],
    "EV_RAIDWEEK": [2, 6, 11, 15, 19, 24, 28, 32, 37, 41, 45, 50],
    "EV_PHOTOCONTEST": [w + d for w in (3, 8, 12, 16, 21, 25, 29, 34, 38, 42, 47, 51) for d in (0, 1)],
    "EV_MIGRATION": [14, 15, 39, 40],
    "EV_LINDENFEST": [22],
    "EV_STARFEST": [48],
    "EV_SEASONRULE": [15, 28, 41],
    "EV_SILENCEECHO": [9, 23, 35, 49],
    "EV_ANNIVERSARY": [52, 53],
}


def week_events(w):
    return [k for k, ws in SCHEDULE.items() if w in ws]


def calendar_table():
    lines = ["| Woche (ab Launch) | Monat | Events | Release |", "|---|---|---|---|"]
    months = ["Nov", "Dez", "Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov"]
    rel = {int(r["Month"]): r for r in RP}
    shown = set()
    for w in range(1, 54):
        m = (w - 1) * 12 // 52
        evs = ", ".join(EV[e]["DisplayName"] for e in week_events(w))
        r = ""
        if m in rel and m not in shown:
            r = f"{rel[m]['Name']} ({rel[m]['Kind']})"
            shown.add(m)
        if evs or r:
            lines.append(f"| W{w} | {months[m]} | {evs or '–'} | {r or '–'} |")
    return "\n".join(lines)


def expansions():
    out = []
    for r in RP:
        if r["Kind"].startswith("Erweiterung"):
            m = re.search(r"(\d+) Echos #(\d+)–#(\d+)", r["Content"])
            out.append((r, int(m.group(1)), int(m.group(2)), int(m.group(3))))
    return out


def validate():
    err = []
    for w in range(1, 54):
        if len(week_events(w)) > 3:
            err.append(f"LO-01 W{w}: {len(week_events(w))} Events")
    for k, e in EV.items():
        if e["Kind"] in ("Welt", "Kampf", "PvP", "Fest") and e["OfflinePath"] in ("", "–"):
            err.append(f"LO-02 {k} ohne Offline-Weg")
        if FORBIDDEN.search(e["Rewards"]) and "Kodex" not in e["Rewards"]:
            err.append(f"LO-03 {k}: Belohnung {e['Rewards']}")
    for s in SHOP:
        if s["Category"] not in ALLOWED_SHOP or FORBIDDEN.search(s["Content"]) or not s["AlsoEarnable"].startswith("ja"):
            err.append(f"LO-04 {s['Name']}")
    nxt = 257
    for r, n, a, b in expansions():
        if not 30 <= n <= 40 or a != nxt or b - a + 1 != n:
            err.append(f"LO-05 {r['Name']}: {n} Echos #{a}–#{b}")
        nxt = b + 1
    months = sorted(int(r["Month"]) for r in RP if int(r["Month"]) <= 12)
    gaps = [b - a for a, b in zip(months, months[1:])]
    if not months or max(gaps or [0]) > 3:
        err.append(f"LO-06 Lücken {gaps}")
    for k in KPI:
        if not k["Alarm"] or not k["Action"] or PRESSURE.search(k["Action"]):
            err.append(f"LO-07 {k['Name']}")
    return err


def report():
    e = validate()
    ex = expansions()
    peak = max(len(week_events(w)) for w in range(1, 54))
    return (f"Prüfregeln LO-01–LO-07: **{len(e)} Verstöße**. {len(EV)} Events (höchstens {peak} gleichzeitig), {len(RP)} Releases in 24 Monaten, "
            f"{len(SHOP)} Shop-Kategorien (nur Kosmetik, feste Preise), Erweiterungen: "
            + ", ".join(f"{r['Name']} {n} Echos (#{a}–#{b})" for r, n, a, b in ex) + ".")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "calendar":
        print(calendar_table())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
