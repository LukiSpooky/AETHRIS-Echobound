#!/usr/bin/env python3
"""Pflege-Werkzeug für docs/CANON.md und docs/00_KAPITELPLAN.md.

Aufruf:
  canon.py done K03                 -> Kapitel im Kapitelplan als ✅ markieren, CANON-Stand setzen
  canon.py adr  FILE                -> ADR-Zeilen (Markdown-Tabellenzeilen) aus FILE in den ADR-Index einfügen
  canon.py open FILE                -> Offene Punkte (Q-Zeilen) aus FILE in §12 einfügen
  canon.py resolve Q5 "Text"        -> offenen Punkt als erledigt markieren
  canon.py section FILE             -> FILE als neue(n) Abschnitt(e) am Ende von CANON anhängen
"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1] / "docs"
CANON = ROOT / "CANON.md"
PLAN = ROOT / "00_KAPITELPLAN.md"

def insert_after_last(text, prefix, rows):
    lines = text.split("\n")
    idx = max(i for i, l in enumerate(lines) if l.startswith(prefix))
    lines[idx + 1:idx + 1] = [r for r in rows if r.strip()]
    return "\n".join(lines)

def main():
    cmd = sys.argv[1]
    c = CANON.read_text(encoding="utf-8")
    if cmd == "done":
        k = sys.argv[2]
        p = PLAN.read_text(encoding="utf-8")
        p = re.sub(rf"^(\| {k} \|.*\| )⬜( \|)$", r"\1✅\2", p, flags=re.M)
        p = re.sub(r"\*\*Stand:\*\* K\d+ abgeschlossen", f"**Stand:** {k} abgeschlossen", p)
        PLAN.write_text(p, encoding="utf-8")
        c = re.sub(r"\*\*Letztes Update:\*\* K\d+", f"**Letztes Update:** {k}", c)
    elif cmd == "adr":
        c = insert_after_last(c, "| ADR-", pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").split("\n"))
    elif cmd == "open":
        c = insert_after_last(c, "| Q", pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").split("\n"))
    elif cmd == "resolve":
        q, note = sys.argv[2], sys.argv[3]
        c = re.sub(rf"^\| {q} \| (.*?) \| (.*?) \|$", rf"| {q} | ~~\1~~ ✅ {note} | \2 |", c, flags=re.M)
    elif cmd == "section":
        c = c.rstrip("\n") + "\n\n" + pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").strip("\n") + "\n"
    CANON.write_text(c, encoding="utf-8")

if __name__ == "__main__":
    main()
