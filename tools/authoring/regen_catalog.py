#!/usr/bin/env python3
"""Erzeugt die Katalogkapitel K20–K27 nach Datenänderungen neu (ADR-075).
Liest Titel, Kodexbereich, Regionen, Einleitung und Folgekapitel aus dem vorhandenen Kapitel und ruft
build_catalog_chapter.py mit denselben Argumenten auf. Aufruf: regen_catalog.py [K20 …]
"""
import pathlib, re, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]


def regen(path):
    t = path.read_text(encoding="utf-8")
    kid, title = re.match(r"# (K\d+) · (.+)", t).groups()
    lo, hi = map(int, re.search(r"Kodex #(\d+)–#(\d+)", t).groups())
    regions = re.search(r"\| Region\(en\) \| (.+?) \|", t).group(1)
    intro = t.split("danach wird das Kapitel neu erzeugt.\n", 1)[1].split("\n## Übersicht", 1)[0].strip("\n")
    nxt = re.search(r"➡️ \*\*Nächstes Kapitel: (.+)\*\*", t).group(1)
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(intro)
    subprocess.run([sys.executable, str(ROOT / "tools/authoring/build_catalog_chapter.py"), kid, title, str(lo), str(hi), regions, f.name, nxt], check=True)


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for p in sorted((ROOT / "docs/kapitel").glob("K2[0-7]_*.md")):
        if not want or p.name[:3] in want:
            regen(p)
