# AETHRIS: Echobound

> Open-World Monster-Collecting-RPG · Unreal Engine 5.6 · PC / PlayStation 5 / Xbox Series X|S / Nintendo Switch 2

Dieses Repository enthält die vollständige Produktionsdokumentation (und später Code, Daten und Tools) für **AETHRIS: Echobound** – ein eigenständiges Monster-Collecting-RPG. Die Welt, Kreaturen („Echos“), Namen und Mechaniken sind originär; es werden keine Designs, Begriffe oder Systeme aus bestehenden Franchises übernommen.

## Arbeitsweise

Das Projekt wird wie in einem echten Studio in **aufeinander aufbauenden Kapiteln** entwickelt.

| Datei | Zweck |
|---|---|
| [`docs/00_KAPITELPLAN.md`](docs/00_KAPITELPLAN.md) | Masterplan aller Kapitel, Status, Abhängigkeiten |
| [`docs/CANON.md`](docs/CANON.md) | **Single Source of Truth** – alle verbindlichen Designentscheidungen, Zahlen, Namen, IDs |
| [`docs/kapitel/`](docs/kapitel/) | Die einzelnen Kapitel (K01 … K68) |

### Regeln für Widerspruchsfreiheit

1. Jede verbindliche Entscheidung wird im Kapitel getroffen **und** in `CANON.md` eingetragen.
2. Einträge sind entweder `LOCKED` (verbindlich, Änderung nur per Change Request) oder `PROVISIONAL` (Arbeitsstand, wird in einem benannten Kapitel finalisiert).
3. Ein späteres Kapitel darf einen `LOCKED`-Eintrag nur über einen dokumentierten **Change Request (CR-xxx)** ändern; der CR wird in `CANON.md` protokolliert.
4. Jedes Kapitel endet mit einer **Checkliste** der abgeschlossenen Systeme und dem Verweis auf das nächste Kapitel.

## Status

Siehe [`docs/00_KAPITELPLAN.md`](docs/00_KAPITELPLAN.md).
