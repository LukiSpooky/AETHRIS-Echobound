#!/usr/bin/env python3
"""QA-Referenz (K66): führt alle registrierten Datenprüfungen aus (`Data/QA/Checks.csv`), fasst Testsuiten,
Fehlerschwere und Zertifizierungsbereiche zusammen.

Erfolg einer Prüfung = Exitcode 0 und letzte Zeile meldet 0 Verstöße/Fehler.
Aufruf: aethris_qa.py [run|PreSubmit|Nightly]
"""
import csv, pathlib, re, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


CHECKS = rows("Data/QA/Checks.csv")
_RESULTS = None


def run(stage=None):
    out = []
    for c in CHECKS:
        if stage and c["Stage"] != stage:
            continue
        t0 = time.time()
        p = subprocess.run([sys.executable] + c["Command"].split(), cwd=ROOT, capture_output=True, text=True)
        dt = time.time() - t0
        last = (p.stdout.strip().splitlines() or [""])[-1]
        zero = bool(re.search(r"\*?\*?0 (Verstöße|Fehler)", last))
        out.append((c, p.returncode == 0 and zero, dt, last))
    return out


def results():
    global _RESULTS
    if _RESULTS is None:
        _RESULTS = run()
    return _RESULTS


def checks_table():
    lines = ["| Prüfung | Kapitel | Stufe | Befehl | Ergebnis | Laufzeit |", "|---|---|---|---|---|---|"]
    for c, ok, dt, last in results():
        lines.append(f"| {c['DisplayName']} | {c['Chapter']} | {c['Stage']} | `{c['Command']}` | {'✅' if ok else '❌'} | {f'{dt:.1f}'.replace('.', ',')} s |")
    return "\n".join(lines)


def summary():
    res = results()
    ok = sum(1 for r in res if r[1])
    total = sum(r[2] for r in res)
    pre = sum(r[2] for r in res if r[0]["Stage"] == "PreSubmit")
    return f"**{ok} von {len(res)} Prüfungen grün**; Laufzeit gesamt {total:.0f} s (davon PreSubmit {pre:.0f} s)."


def rule_catalog():
    """Alle Prüfregel-IDs der Repository-Werkzeuge mit Beschreibung (Docstring) oder Fehlermeldung (Fallback)."""
    doc = re.compile(r"^\s+([A-Z]{2,3}-\d{2}) (.+)$")
    err = re.compile(r'(?:append|err)\(f?"([A-Z]{2,3}-\d{2})[^:"]*:? ?([^"]*)"')
    rules = {}
    files = sorted(list((ROOT / "tools").glob("*.py")) + list((ROOT / "tools/ref").glob("*.py")) + list((ROOT / "tools/authoring").glob("*.py")))
    for f in files:
        txt = f.read_text(encoding="utf-8")
        for line in txt.splitlines():
            m = doc.match(line)
            if m and m.group(1) not in rules:
                rules[m.group(1)] = (m.group(2).strip(), f.relative_to(ROOT).as_posix())
        for m in err.finditer(txt):
            if m.group(1) not in rules:
                msg = re.sub(r"\{[^}]*\}", "…", m.group(2)).strip(" :…") or "(siehe Werkzeug)"
                rules[m.group(1)] = (msg, f.relative_to(ROOT).as_posix())
    return rules


def rule_table():
    rules = rule_catalog()
    lines = ["| Regel | Inhalt | Werkzeug |", "|---|---|---|"]
    for k in sorted(rules, key=lambda x: (x.split("-")[0], int(x.split("-")[1]))):
        d, f = rules[k]
        if len(d) < 8 or d.startswith("("):
            d = "Detailprüfung (Meldungstext im Werkzeug)"
        lines.append(f"| {k} | {d} | `{f}` |")
    lines.append(f"| **Σ** | **{len(rules)} Prüfregeln** | |")
    return "\n".join(lines)


def suites_table():
    lines = ["| Suite | Inhalt | Tests (Launch) | Laufzeit | Stufe |", "|---|---|---|---|---|"]
    for t in rows("Data/QA/TestSuites.csv"):
        lines.append(f"| `{t['Name']}` | {t['Content']} | {t['Tests']} | {t['Duration']} | {t['Stage']} |")
    n = sum(int(t["Tests"]) for t in rows("Data/QA/TestSuites.csv"))
    lines.append(f"| **Σ** | | **{n}** | | |")
    return "\n".join(lines)


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "run" else None
    res = run(stage)
    for c, ok, dt, last in res:
        print(f"{'OK ' if ok else 'ERR'} {c['Name']:<16} {dt:5.1f} s  {last[:100]}")
    bad = [r for r in res if not r[1]]
    print(f"QA: {len(res) - len(bad)}/{len(res)} grün, {len(bad)} Fehler.")
    sys.exit(1 if bad else 0)
