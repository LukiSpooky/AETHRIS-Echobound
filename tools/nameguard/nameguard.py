"""
NameGuard – prüft Namensvorschläge gegen die Regeln N1–N8 (K04 §4.1).
Eingabe: CSV mit Spalten id,name,kind (echo|place|person|item|ability) und optional line (Evolutionslinie)
Ausgabe: Bericht (Markdown) + Exitcode != 0 bei Verstößen (CI-Gate).
"""
from __future__ import annotations
import csv, sys, unicodedata
from dataclasses import dataclass
from pathlib import Path

REFERENCE_DB = Path(__file__).with_name("reference_names.txt")  # ~5.000 Fremdnamen (Legal pflegt)
BLACKLIST = Path(__file__).with_name("blacklist.txt")           # verbotene Begriffe (§2.1)
DICTIONARIES = Path(__file__).with_name("dicts")                # Wortlisten 12 Sprachen

@dataclass
class Finding:
    rule: str
    message: str

def normalized(s: str) -> str:
    """Kleinbuchstaben, ohne Diakritika – Basis für Ähnlichkeitsvergleich."""
    nfkd = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in nfkd if not unicodedata.combining(c))

def similarity(a: str, b: str) -> float:
    """Normalisierte Levenshtein-Ähnlichkeit 0..1."""
    a, b = normalized(a), normalized(b)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return 1.0 - prev[-1] / max(len(a), len(b), 1)

def check_echo_name(name: str, others: list[str], refs: list[str], words: set[str]) -> list[Finding]:
    """others = Namen anderer Linien (N6 gilt nur linienübergreifend)."""
    f: list[Finding] = []
    if not 4 <= len(name) <= 10:
        f.append(Finding("N1", f"Länge {len(name)} außerhalb 4–10"))
    if not name.isascii() or not name.isalpha():
        f.append(Finding("N2", "Nur ASCII-Buchstaben erlaubt (keine Umlaute/Apostrophe)"))
    if normalized(name) in words:
        f.append(Finding("N5", "Name ist ein reales Wort einer Zielsprache"))
    prefix = normalized(name)[:4]
    clash = [o for o in others if normalized(o)[:4] == prefix]
    if clash:
        f.append(Finding("N6", f"Präfix '{prefix}' bereits vergeben: {', '.join(clash)}"))
    worst = max(refs, key=lambda r: similarity(name, r), default=None)
    if worst and similarity(name, worst) > 0.60:
        f.append(Finding("N8", f"Zu ähnlich zu Referenzname (Ähnlichkeit {similarity(name, worst):.2f})"))
    return f

def main(csv_path: str) -> int:
    refs = REFERENCE_DB.read_text(encoding="utf-8").split() if REFERENCE_DB.exists() else []
    words = set()
    if DICTIONARIES.exists():
        for d in DICTIONARIES.glob("*.txt"):
            words |= {normalized(w) for w in d.read_text(encoding="utf-8").split()}
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
    failed = 0
    for r in rows:
        if r["kind"] != "echo":
            continue
        line = r.get("line") or r["id"]
        others = [o["name"] for o in rows
                  if o["kind"] == "echo" and o["name"] != r["name"] and (o.get("line") or o["id"]) != line]
        for finding in check_echo_name(r["name"], others, refs, words):
            failed += 1
            print(f"- **{r['id']} {r['name']}** · {finding.rule}: {finding.message}")
    print(f"\n{len(rows)} Namen geprüft, {failed} Verstöße.")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
