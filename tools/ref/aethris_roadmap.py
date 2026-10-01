#!/usr/bin/env python3
"""Produktions-Referenzmodell (K67): Personal- und Kostenkurve aus Arbeitspaketen, Gantt, Meilensteine,
Durchsatz, Kapitelabdeckung.

Prüfregeln:
  RM-01 Arbeitspakete liegen im Projektzeitraum (M0–M49), Ende ≥ Start
  RM-02 Abhängigkeiten beginnen vorher
  RM-03 Spitze ≤ 210 FTE, Durchschnitt 130–150 FTE (K01 §15/§16)
  RM-04 Personalkosten ±5 % um 118 Mio. € (16,8 T€ je FTE-Monat, K01 §16.3)
  RM-05 Meilensteine = Kanon-Daten (Greenlight 06/27, P2 07/27, VS 03/28, Alpha/Engine-Lock 02/30, Gold 09/30, Launch 11/30)
  RM-06 jedes Kapitel K01–K68 gehört zu mindestens einem Arbeitspaket
  RM-07 Durchsatz monoton, Endwerte = Kanon-Mengen

Aufruf: aethris_roadmap.py validate | staffing | gantt
"""
import csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
COST_PER_FTE_MONTH = 16.8      # T€ voll belastet (K01 §16.3)
MONTHS = 50
MON = ["Okt", "Nov", "Dez", "Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep"]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


EP = rows("Data/Production/Workstreams.csv")
MS = rows("Data/Production/Milestones.csv")
TP = rows("Data/Production/Throughput.csv")


def label(m):
    y = 2026 + (m + 9) // 12
    return f"{MON[m % 12]} {str(y)[2:]}"


def fte_curve():
    c = [0.0] * MONTHS
    for e in EP:
        for m in range(int(e["StartMonth"]), int(e["EndMonth"]) + 1):
            c[m] += float(e["FTE"])
    return c


def de(x, nd=0):
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def staffing_table():
    c = fte_curve()
    lines = ["| Quartal | Ø FTE | Personalkosten (Mio. €) | Phase |", "|---|---|---|---|"]
    phases = [(0, 8, "P1 Preproduction"), (9, 17, "P2 Vertical Slice"), (18, 29, "P3 Core Systems"), (30, 40, "P4 Content"),
              (41, 46, "P5 Polishing"), (47, 49, "P6 Release")]
    for q in range(0, MONTHS, 3):
        ms = list(range(q, min(q + 3, MONTHS)))
        avg = sum(c[m] for m in ms) / len(ms)
        cost = sum(c[m] for m in ms) * COST_PER_FTE_MONTH / 1000
        ph = next(p for a, b, p in phases if a <= q <= b)
        lines.append(f"| {label(ms[0])} – {label(ms[-1])} | {de(avg)} | {de(cost, 1)} | {ph} |")
    total = sum(c) * COST_PER_FTE_MONTH / 1000
    lines.append(f"| **Σ / Spitze / Ø** | **Spitze {de(max(c))} · Ø {de(sum(c) / MONTHS)}** | **{de(total, 1)}** | |")
    return "\n".join(lines)


def gantt():
    lines = ["```", "Arbeitspaket                         " + "".join(("|" if m % 12 == 3 else " ") for m in range(MONTHS)),
             "                                     " + "".join(str(2027 + (m - 3) // 12)[3] if m % 12 == 3 else " " for m in range(MONTHS))]
    for e in EP:
        a, b = int(e["StartMonth"]), int(e["EndMonth"])
        bar = "".join("█" if a <= m <= b else "·" for m in range(MONTHS))
        lines.append(f"{e['DisplayName'][:36]:<37}{bar} {e['FTE']}")
    ms = "".join(" " for _ in range(MONTHS))
    marks = list(ms)
    for m in MS:
        marks[int(m["Month"])] = "▲"
    lines.append(f"{'Meilensteine':<37}{''.join(marks)}")
    lines.append("```")
    return "\n".join(lines)


def hiring_table():
    c = fte_curve()
    lines = ["| Quartal | FTE am Quartalsende | Veränderung | Bedeutung |", "|---|---|---|---|"]
    prev = 0.0
    for q in range(0, MONTHS, 3):
        end = c[min(q + 2, MONTHS - 1)]
        d = end - prev
        what = "Aufbau (Einstellungen)" if d > 0 else ("Übergang in Erweiterung/andere Projekte" if d < 0 else "stabil")
        lines.append(f"| {label(q)} – {label(min(q + 2, MONTHS - 1))} | {de(end)} | {d:+.0f} | {what} |")
        prev = end
    return "\n".join(lines)


def pod_table():
    pods = {}
    for e in EP:
        pm = (int(e["EndMonth"]) - int(e["StartMonth"]) + 1) * float(e["FTE"])
        pods.setdefault(e["Pod"], [0, 0])
        pods[e["Pod"]][0] += pm
        pods[e["Pod"]][1] += 1
    tot = sum(v[0] for v in pods.values())
    lines = ["| Pod | Arbeitspakete | FTE-Monate | Anteil | Kosten (Mio. €) |", "|---|---|---|---|---|"]
    for p, (pm, n) in sorted(pods.items(), key=lambda x: -x[1][0]):
        lines.append(f"| {p} | {n} | {de(pm)} | {100 * pm / tot:.0f} % | {de(pm * COST_PER_FTE_MONTH / 1000, 1)} |")
    return "\n".join(lines)


CANON_MS = {"MS_GREENLIGHT": "2027-06", "MS_PERFORCE": "2027-07", "MS_VS": "2028-03", "MS_ALPHA": "2030-02", "MS_GOLD": "2030-09", "MS_LAUNCH": "2030-11"}
CANON_TOTALS = {"TP_ECHOS": 256, "TP_REGIONS": 10, "TP_QUESTS": 242, "TP_CINE": 70, "TP_NPCS": 194, "TP_ABILITIES": 330, "TP_LANGUAGES": 12}


def chapters_of(spec):
    out = set()
    for part in re.split(r",\s*", spec):
        m = re.match(r"K(\d+)(?:–K(\d+))?", part.strip())
        if m:
            a = int(m.group(1))
            b = int(m.group(2) or a)
            out |= set(range(a, b + 1))
    return out


def validate():
    err = []
    names = {e["Name"]: e for e in EP}
    for e in EP:
        a, b = int(e["StartMonth"]), int(e["EndMonth"])
        if not (0 <= a <= b < MONTHS):
            err.append(f"RM-01 {e['Name']}")
        for d in filter(None, e["DependsOn"].split("|")):
            if d not in names or int(names[d]["StartMonth"]) >= a:
                err.append(f"RM-02 {e['Name']} ← {d}")
    c = fte_curve()
    if max(c) > 210 or not 130 <= sum(c) / MONTHS <= 150:
        err.append(f"RM-03 Spitze {max(c):.0f}, Ø {sum(c) / MONTHS:.0f}")
    cost = sum(c) * COST_PER_FTE_MONTH / 1000
    if abs(cost - 118) > 118 * 0.05:
        err.append(f"RM-04 Personalkosten {cost:.1f} Mio. €")
    for m in MS:
        if m["Name"] in CANON_MS and m["Date"] != CANON_MS[m["Name"]]:
            err.append(f"RM-05 {m['Name']} {m['Date']} ≠ {CANON_MS[m['Name']]}")
        y, mo = map(int, m["Date"].split("-"))
        if (y - 2026) * 12 + mo - 10 != int(m["Month"]):
            err.append(f"RM-05 {m['Name']}: Monat {m['Month']} passt nicht zu {m['Date']}")
    cov = set()
    for e in EP:
        cov |= chapters_of(e["Chapters"])
    miss = sorted(set(range(1, 69)) - cov)
    if miss:
        err.append(f"RM-06 Kapitel ohne Arbeitspaket: {miss}")
    for t in TP:
        vals = [int(t[k]) for k in ("VS", "PreAlpha", "Alpha", "Beta")]
        if vals != sorted(vals) or vals[-1] != int(t["Total"]) or CANON_TOTALS.get(t["Name"]) != int(t["Total"]):
            err.append(f"RM-07 {t['Name']}")
    return err


def report():
    e = validate()
    c = fte_curve()
    return (f"Prüfregeln RM-01–RM-07: **{len(e)} Verstöße**. {len(EP)} Arbeitspakete, Spitze {de(max(c))} FTE, Ø {de(sum(c) / MONTHS)} FTE, "
            f"Personalkosten {de(sum(c) * COST_PER_FTE_MONTH / 1000, 1)} Mio. €; {len(MS)} Meilensteine; Kapitel K01–K68 vollständig zugeordnet.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "staffing":
        print(staffing_table()); print(pod_table())
    elif cmd == "gantt":
        print(gantt())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
