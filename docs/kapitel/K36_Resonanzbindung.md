# K36 · Resonanzbindung – das Bindungssystem

| Feld | Wert |
|---|---|
| Dokument | Kapitel 36 von 68 · Systeme, Teil I |
| Version | 1.0 |
| Owner | Lead Systems Designer (Bindung) |
| Mitwirkende | Creature Design Lead (Merkmale, Lockmittel), Audio Lead (Frequenzen, Haptik), UX Lead (Anschlag-UI, Barrierefreiheit), Lead AI Programmer (Wildverhalten), Economy Designer (Siegel, Fallen) |
| Baut auf | ADR-006 (Resonanzbindung), DR-01/03/04/07/15/16, K02 §4.2 (Starttuning), K16 (Merkmale, Seltenheit), K18 (Temperamente: Fenster, Versuche, Reaktion), K20–K27 (Lieblingsköder je Art), K33 (Bindung im Kampf), K35 (Mythische) |
| Status | ✅ Freigegeben – **löst Q12** (Bindungs-Timingfenster) |
| Im Repository | `tools/ref/aethris_bond.py` (Referenzmodell + Szenarien), `Data/Items/Seals.csv` (8), `Data/Items/Traps.csv` (8), `Data/Items/Lures.csv` (24, Wirkung hier), `Source/AethrisCore/Public/Services/BondingService.h` (CR-002) |
| Neue Kanon-Einträge | CANON §132 (Ablauf), §133 (Resonanzwert & Schwellen), §134 (Anschlag & Fenster), §135 (Siegel, Fallen, Lockmittel), §136 (Sonderfälle) |

---

## Inhalt

1. [Bindung statt Fang](#1-bindung-statt-fang)
2. [Der Ablauf in vier Phasen](#2-der-ablauf-in-vier-phasen)
3. [Der Resonanzwert](#3-der-resonanzwert)
4. [Schwellen nach Seltenheit](#4-schwellen-nach-seltenheit)
5. [Der Anschlag: Timing-Fenster (Q12)](#5-der-anschlag-timing-fenster-q12)
6. [Ergebnisse und Reaktionen](#6-ergebnisse-und-reaktionen)
7. [Siegel, Fallen, Lockmittel](#7-siegel-fallen-lockmittel)
8. [Szenarien](#8-szenarien)
9. [Bindung im Kampf](#9-bindung-im-kampf)
10. [Sonderfälle](#10-sonderfälle)
11. [Präsentation, Haptik, Barrierefreiheit](#11-präsentation-haptik-barrierefreiheit)
12. [Code](#12-code)
13. [Tests und Telemetrie](#13-tests-und-telemetrie)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Bindung statt Fang

In AETHRIS wird kein Echo gefangen. Ein Wärter **stimmt sich ein**: Er liest die Frequenz eines Echos, nähert sich, beruhigt es mit dem, was es mag, und schlägt im richtigen Moment sein Siegel am Resonator an – ein Ton, der beide verbindet (ADR-006). Die Bindung ist ein **Dialog** (DR-03): Jede Entscheidung vor dem Anschlag verändert messbar das Ergebnis; der Anschlag selbst ist ein kurzer, musikalischer Moment.

**Drei Leitsätze** (aus K02, hier verbindlich):

1. **Wissen schlägt Items** (DR-01): Kodex-Forschung bringt bis zu +240 Resonanz, das beste kaufbare Siegel nur 80.
2. **Kein Erfolgswurf** (DR-07): Das Ergebnis folgt aus Resonanz und Timing – es gibt keinen versteckten Würfel. Die Vorschau zeigt, ob die Resonanz reicht.
3. **Kein Scheitern ohne Fortschritt** (DR-10): Ein Anschlag mit zu wenig Resonanz ist eine **Annäherung** (+100 Resonanz), kein verlorener Versuch.

---

## 2. Der Ablauf in vier Phasen

```
┌────────────┐    ┌──────────────────┐    ┌────────────────────┐    ┌──────────────┐
│ 1 LAUSCHEN │──► │ 2 ANNÄHERN        │──► │ 3 EINSTIMMEN        │──► │ 4 ANSCHLAG    │
│ Resonanz-  │    │ Schleichen, Wind, │    │ Lockmittel/Futter,  │    │ Timing auf    │
│ sinn:      │    │ Deckung, Falle    │    │ Summen, Falle wirkt │    │ Echo-Frequenz │
│ Frequenz,  │    │ (Entdeckungs-     │    │ – ODER Kampfweg     │    │ Siegel        │
│ Stimmung   │    │  radius × Temp.)  │    │   (Erschöpfung)     │    │ verankert     │
└────────────┘    └──────────────────┘    └────────────────────┘    └──────┬───────┘
     +Kodex            +0…150                +Köder −50…200                 │
                                             +Falle 100…200                 ▼
                                             +Kampf bis 250        Einklang · Bindung ·
                                             +Tageszeit 50          Annäherung · Verfehlt
```

| Phase | Was der Spieler tut | Was das System misst |
|---|---|---|
| **1 Lauschen** | Resonanzsinn (Taste halten): Frequenzlinie, Stimmung (ruhig/neugierig/unruhig/aufgewühlt), Merkmal-Symbole ab Kodex 2 | Kodex-Stufe der Art → Resonanzbonus |
| **2 Annähern** | Schleichen (Ducken halbiert Geräusch), gegen den Wind, Deckung nutzen; optional Falle legen | Entdeckungsradius = Artradius × Temperament (`DetectRadiusPermille`) × Wetter (Regen −20 %, Sturm −30 %); Annäherungsbonus 0–150 nach Nähe ohne Entdeckung |
| **3 Einstimmen** | Lockmittel/Futter anbieten (Radialmenü), summen (Taste halten im Takt), Falle wirkt – **oder** kämpfen | Köderpassung, Fallenbedingung, Tageszeit, Kampf-Erschöpfung |
| **4 Anschlag** | Siegel wählen, im Takt der Echo-Frequenz anschlagen | Timing (Perfekt/Gut/verfehlt) gegen Resonanz und Schwelle |

**Dauer:** Oberwelt-Bindung ohne Kampf 20–60 s (K02-Ziel); mit Kampf 60–150 s.

---

## 3. Der Resonanzwert

Der **Resonanzwert R** (0–1000) fasst alle Entscheidungen zusammen. Er ist im Anschlag-UI als Ring sichtbar (gefüllt bis R, Markierung an der Schwelle).

| Quelle | Beitrag | Anmerkung |
|---|---|---|
| Kodex-Stufe der Art | 0 / 60 / 120 / 180 / 240 (Stufe 0–4) | Wissen (DR-01); größte Einzelquelle |
| Annäherung | 0–150 | unentdeckt näher als 50 % des Entdeckungsradius → voll |
| Lockmittel/Futter | falsch −50 · passende Kategorie +100 · **Lieblingsköder der Art** +200 | Lieblingsköder steht im Kodex (Stufe 2) und in `Species.csv` (`BondLure`) |
| Falle | +100 bis +200 bei erfüllter Bedingung (`Traps.csv`) | max. 1 Falle je Bindung |
| Kampf-Erschöpfung | + 0,3 × verlorene HP-Promille, max. 250 | Kampfweg (§9) |
| Status am Echo | +50 (Starre, Verlangsamt, Schwebend, Furcht) | im Kampf |
| Tageszeit passt | +50 | Aktivitätsmuster der Art (Ruhephase) |
| Level-Abstand | −10 je Level über (höchstes Chor-Level + 10) | Schutz gegen zu frühe Hochlevel-Echos |
| Annäherung (Teilerfolg) | +100 je Anschlag mit zu wenig R | DR-10 |

```
R = clamp( Kodex + Annäherung + Köder + Falle + min(250, 0,3 × HP-Verlust‰) + Status + Tageszeit − Levelstrafe, 0, 1000 )
```

---

## 4. Schwellen nach Seltenheit

| Seltenheit | Schwelle | Bedeutung |
|---|---|---|
| Häufig | 150 | mit Annäherung + Tageszeit oder einem Köder sofort möglich |
| Ungewöhnlich | 250 | ein passender Köder oder Kodex 2 |
| Selten | 400 | Wissen + Köder oder Kampf + Köder |
| Sehr selten | 550 | Vorbereitung: Kodex 3–4, Lieblingsköder, Falle, Tageszeit |
| Alpha | 600 | Kampf + Wissen |
| Ursprungsstimme | 750 + **Stimmsiegel** | Story-Begegnung (K44–K46) |
| Mythisch | 750 + **Sternensiegel** | Bindungsfenster (K35 §9) |

Die Siegel senken die Schwelle (0/40/80 bzw. bedingt 60) – sie *helfen*, ersetzen aber nie Wissen (DR-01-Prüfung: Kodex 3 + Klangsiegel ⇒ 180 ≥ Meistersiegel bei Kodex 0 ⇒ 80 ✔).

---

## 5. Der Anschlag: Timing-Fenster (Q12)

Beim Anschlag pulsiert das **Klangmal** des Echos im Takt seiner Grundfrequenz. Der Spieler schlägt auf dem Höhepunkt eines Pulses an.

```
Gut-Fenster (ms)    = (160 + 240 × R / 1000) × Temperament‰ × Siegel‰ [× 1,75 „Großzügiges Timing“]
Perfekt-Fenster (ms) = max(60, 25 % des Gut-Fensters)
Versuche            = Temperament (Ruhig 4 · Neugierig 3 · Stoisch 3 · Feurig 2 · Wachsam 2)
```

| R | Gut-Fenster (Temperament 1000 ‰) | Perfekt |
|---|---|---|
| 0 | 160 ms | 60 ms |
| 250 | 220 ms | 60 ms |
| 500 | 280 ms | 70 ms |
| 750 | 340 ms | 85 ms |
| 1000 | 400 ms | 100 ms |

**Q12 gelöst:** Die Startwerte aus K02 §4.2 (400 → 160 ms, Perfekt 25 % min. 60 ms, 2–4 Versuche) werden übernommen und über den Resonanzwert statt über eine abstrakte „Unruhe“ gesteuert: *Ein gut vorbereitetes Echo ist ruhig – das Fenster ist weit.* Temperament-Faktoren aus `Temperaments.csv` (Ruhig 1200, Neugierig 1100, Stoisch/Wachsam 1000, Feurig 900 ‰).

**Rhythmus:** Grundfrequenz je Archetyp (A01–A18) zwischen 70 und 140 BPM; Pulse sind auf die Kampf-/Weltmusik quantisiert (Quartz, K55), sodass der Anschlag immer musikalisch „sitzt“.

---

## 6. Ergebnisse und Reaktionen

| Ergebnis | Bedingung | Folge |
|---|---|---|
| **Einklang** | Timing Perfekt **und** R ≥ Schwelle − 100 | Bindung; Bindungswert-Start +100 (K37), Kodex-Fortschritt +1 Beobachtung, Musik-Stinger, Herkunftseintrag „Einklang“ (DR-16) |
| **Bindung** | Timing Gut **und** R ≥ Schwelle | Bindung; Bindungswert-Start 50 |
| **Annäherung** | Timing Gut/Perfekt, aber R zu niedrig | R +100, Versuch verbraucht; Echo zeigt Zutrauen (Animation „lauscht“) |
| **Verfehlt** | Timing außerhalb Gut | Versuch verbraucht; Reaktion nach Temperament |

| Temperament | Reaktion bei „Verfehlt“ (`OnFailedStrike`) |
|---|---|
| Ruhig | bleibt (Unruhe-Animation), nächster Puls normal |
| Neugierig | nähert sich (Annäherung +50) |
| Stoisch | bleibt; keine Änderung |
| Wachsam | nach 2. Fehlversuch Flucht (sichtbarer Fluchtweg; Ruhenetz hält einmal) |
| Feurig | greift an → Kampf (R bleibt erhalten, Kampfweg addiert) |

Sind alle Versuche verbraucht, zieht sich das Echo zurück (Wildverhalten K52) und ist für 1 Spielstunde „wachsam“ (Entdeckungsradius ×1,3). Es verschwindet nie dauerhaft.

---

## 7. Siegel, Fallen, Lockmittel

### 7.1 Siegel

| DisplayName | Tier | ThresholdBonus | WindowPermille | Sources | PriceSol | Description |
|---|---|---|---|---|---|---|
| Klangsiegel | 1 | 0 | 1000 | Händler|Crafting | 150 | Einfaches Siegel aus Resonanzharz |
| Gestimmtes Siegel | 2 | 40 | 1050 | Händler (ab Akkord 2)|Crafting | 450 | Mit Stimmgabel nachgestimmt |
| Meistersiegel | 3 | 80 | 1100 | Händler (ab Akkord 5)|Crafting | 1200 | Dorunisches Muster; ruhige Hand nötig |
| Klangfarben-Siegel | 2 | 60 | 1000 | Crafting (Obertonkristall) | – | +60 nur für Echos der eingebrannten Klangfarbe (15 Varianten) |
| Mondsiegel | 2 | 60 | 1000 | Crafting (Mondmoos) | – | +60 nur nachts (Tagesphase Nacht) |
| Erdsiegel | 2 | 60 | 1000 | Crafting (Erz) | – | +60 nur für Größe L und größer |
| Stimmsiegel | 4 | 0 | 1000 | Story (je Ursprungsstimme 1) | – | Pflicht für Ursprungsstimmen; nicht kaufbar/handelbar |
| Sternensiegel | 4 | 0 | 1000 | Endgame (Mythische) | – | Pflicht für Mythische; je Mythisches 1 |

Siegel werden **beim Anschlag verbraucht**, nicht bei Annäherung oder Verfehlen (kein Frust durch Verschwendung). Stimm- und Sternensiegel sind nie käuflich oder handelbar (CANON §8).

### 7.2 Fallen

| DisplayName | Condition | ResonanceBonus | Effect | Sources |
|---|---|---|---|---|
| Ruhenest | Trait:Sleepy|Trait:Nester | 150 | Echo legt sich hinein; Unruhe −30 % | Crafting (Holz/Kräuter) |
| Duftfalle | Trait:Grazer|Trait:Pollinator|Trait:Scavenger | 150 | Lockt aus 40 m an; Annäherung leiser | Crafting (Kräuter) |
| Klangfalle | Trait:Singer|Trait:Echolocator | 150 | Spielt die Grundfrequenz der Art; Timing-Hilfe (Ton-Countdown) | Crafting (Kristall) |
| Schattenzelt | Trait:Shy|Trait:Camouflaged | 200 | Wärter unsichtbar bis zum Anschlag | Crafting (Stoff) |
| Ruhenetz | Size:M+ | 100 | Hält Fluchtversuch einmal auf (kein Schaden) | Crafting (Fasern) |
| Schatzkiste | Trait:Collector|Trait:Hoarder | 150 | Echo untersucht die Kiste 10 s (Anschlag ohne Bewegung) | Crafting (Erz/Kristall) |
| Wärmestein | Trait:Sunbather|Trait:Thermal | 150 | Echo sonnt sich; Unruhe −20 % | Crafting (Erz/Glut) |
| Quellbecken | Trait:Swimmer|Trait:Mudbather|Trait:Filterer | 150 | Echo badet; Wasser dämpft Schritte | Crafting (Holz/Kristall) |

Fallen sind **Weltobjekte** (bleiben 10 Spielminuten), sichtbar für Koop-Partner, und wirken nur, wenn die Bedingung (Merkmal/Größe) der Zielart erfüllt ist – die Merkmale stehen ab Kodex 2 im Kodex. Damit lohnt sich Beobachtung doppelt.

### 7.3 Lockmittel und Futter

Die 24 Einträge aus `Lures.csv` wirken so:

| Art | Wirkung |
|---|---|
| Lieblingsköder (`BondLure` der Art) | +200; Echo kommt bis 5 m heran |
| Food/Lure derselben „Kategorie“ (Lure: Klangfarben laut Beschreibung; Food: Region/Ernährung passend zu Merkmalen) | +100 |
| unpassend | −50 (Echo wendet sich ab; Lernmoment) |
| Nachbarschaft | Lockmittel locken im Umkreis 25 m passende Echos an (Spawn-Anreiz K52) |

---

## 8. Szenarien

Aus `aethris_bond.scenarios()` – Resonanz, Schwelle (nach Siegel) und das Ergebnis bei gutem bzw. perfektem Timing:

| Szenario | R | Schwelle − Siegel | Gut-Fenster | Perfekt | bei „Gut“ | bei „Perfekt“ |
|---|---|---|---|---|---|---|
| Prolog: Wisplet, Erstresonanz | 150 | 150 | 215 ms | 60 ms | Bindung | Einklang |
| Häufiges Echo, nichts vorbereitet | 50 | 150 | 172 ms | 60 ms | Annäherung | Einklang |
| Häufiges Echo, Lieblingsfutter | 340 | 150 | 241 ms | 60 ms | Bindung | Einklang |
| Seltenes Echo, nur Kampf (50 % HP) | 200 | 400 | 208 ms | 60 ms | Annäherung | Annäherung |
| Seltenes Echo, Kampf + Meistersiegel | 200 | 320 | 208 ms | 60 ms | Annäherung | Annäherung |
| Seltenes Echo, Kodex 3 + Lieblingsköder | 480 | 400 | 275 ms | 68 ms | Bindung | Einklang |
| Sehr selten, Kodex 4 + Falle + Zeit | 660 | 510 | 318 ms | 79 ms | Bindung | Einklang |
| Alpha, Kampf + Kodex 2 + Köder | 550 | 520 | 262 ms | 65 ms | Bindung | Einklang |
| Ursprungsstimme (Stimmsiegel) | 940 | 750 | 385 ms | 96 ms | Bindung | Einklang |
| Zu hohes Level (+18) | 340 | 250 | 241 ms | 60 ms | Bindung | Einklang |

**Lesart:** Ein seltenes Echo ist allein über Kampf und das beste Siegel nicht im ersten Anschlag bindbar (R 200 < 320) – aber über zwei **Annäherungen** (+100 je Versuch) im dritten. Mit Kodex 3 und dem Lieblingsköder gelingt es im ersten Versuch. Wissen spart Zeit, Items helfen – genau das verlangt DR-01.

### 8.1 Bindungs-Steckbrief aller wild bindbaren Arten

Generiert aus `Species.csv`, `Lures.csv` und `Traps.csv` (Arten, die nur durch Evolution oder Zucht entstehen, fehlen). Diese Tabelle ist zugleich die Datengrundlage der Kodex-Seiten „Bindung“ (Stufe 2: Köder, Stufe 3: Fallen und Ruhephase, K39):

| # | Art | Seltenheit | Schwelle | Lieblingsköder | passende Fallen | Ruhephase (+50) |
|---|---|---|---|---|---|---|
| 001 | Fernlit | Sehr selten | 550 | Lindblüten-Honig | Klangfalle, Schattenzelt | Mittag/Nacht |
| 004 | Brokk | Sehr selten | 550 | Erzkrümel | – | – |
| 007 | Wisplet | Sehr selten | 550 | Pfeifholz | Klangfalle | Nacht |
| 010 | Chimkin | Häufig | 150 | Glockenspiel | Schatzkiste | Nacht |
| 011 | Chimbal | Ungew. | 250 | Glockenspiel | Klangfalle, Ruhenetz | Nacht |
| 012 | Cantaroth | Selten | 400 | Glockenspiel | Klangfalle, Ruhenetz | Mittag/Nacht |
| 014 | Mossling | Häufig | 150 | Moosküchlein | Duftfalle, Schattenzelt | Nacht |
| 015 | Myrthorn | Ungew. | 250 | Moosküchlein | Duftfalle, Ruhenetz | Nacht |
| 018 | Lumpip | Häufig | 150 | Lindblüten-Honig | Ruhenest, Duftfalle | Mittag |
| 019 | Lumow | Ungew. | 250 | Irrlicht-Laterne | Duftfalle | Mittag |
| 020 | Phantalume | Selten | 400 | Irrlicht-Laterne | Ruhenetz | Mittag |
| 021 | Rillo | Häufig | 150 | Waldbeeren | Klangfalle, Quellbecken | Mittag/Nacht |
| 022 | Rillward | Ungew. | 250 | Waldbeeren | Klangfalle, Ruhenetz, Quellbecken | Mittag/Nacht |
| 023 | Sporlet | Häufig | 150 | Moosküchlein | Ruhenest, Schattenzelt | Mittag |
| 024 | Sporix | Selten | 400 | Moosküchlein | Schattenzelt | Mittag |
| 025 | Skirmote | Häufig | 150 | Pfeifholz | – | Nacht |
| 026 | Skirrow | Ungew. | 250 | Pfeifholz | Klangfalle | Nacht |
| 027 | Thornkin | Ungew. | 250 | Waldbeeren | Schattenzelt | Nacht |
| 028 | Thorncoil | Selten | 400 | Waldbeeren | Schattenzelt, Ruhenetz | Nacht |
| 029 | Pebi | Häufig | 150 | Erzkrümel | Ruhenest, Schattenzelt | – |
| 031 | Rivetkin | Ungew. | 250 | Erzkrümel | Schatzkiste | – |
| 032 | Cindrel | Selten | 400 | Glutkohle | Wärmestein | Mittag |
| 033 | Craglet | Häufig | 150 | Erzkrümel | Schattenzelt, Schatzkiste | – |
| 034 | Cragar | Ungew. | 250 | Erzkrümel | Ruhenetz | – |
| 037 | Tetri | Ungew. | 250 | Glockenspiel | Ruhenest, Schatzkiste | – |
| 038 | Tetrel | Selten | 400 | Glockenspiel | Ruhenetz, Schatzkiste | Mittag |
| 040 | Ferrkin | Häufig | 150 | Erzkrümel | – | Mittag |
| 041 | Ferrow | Ungew. | 250 | Erzkrümel | Ruhenetz | Mittag |
| 043 | Gratkin | Häufig | 150 | Pfeifholz | Ruhenest | Nacht |
| 044 | Gratwyn | Ungew. | 250 | Pfeifholz | Ruhenetz | Nacht |
| 046 | Kiesi | Häufig | 150 | Bergkäse | Klangfalle | Nacht |
| 047 | Kiesward | Ungew. | 250 | Bergkäse | Klangfalle, Ruhenetz | Nacht |
| 048 | Lithi | Ungew. | 250 | Erzkrümel | Ruhenest, Schatzkiste, Quellbecken | Mittag/Nacht |
| 049 | Lithshell | Selten | 400 | Erzkrümel | Ruhenest, Ruhenetz, Quellbecken | Mittag/Nacht |
| 050 | Rimlet | Häufig | 150 | Bergkäse | Schattenzelt | Mittag/Nacht |
| 051 | Rimpaw | Selten | 400 | Bergkäse | Schattenzelt, Ruhenetz | Mittag/Nacht |
| 052 | Quarling | Ungew. | 250 | Kristallsalz | – | Mittag |
| 053 | Quarcoil | Selten | 400 | Kristallsalz | Ruhenetz | Mittag |
| 054 | Emblit | Ungew. | 250 | Glutkohle | Wärmestein | – |
| 055 | Dawnix | Selten | 400 | Glutkohle | Ruhenetz, Wärmestein | Nacht |
| 056 | Memoro | Selten | 400 | Irrlicht-Laterne | Ruhenetz | Mittag |
| 057 | Resonix | Ungew. | 250 | Glockenspiel | Klangfalle | Mittag |
| 058 | Runkar | Selten | 400 | Glockenspiel | Ruhenetz | Mittag |
| 059 | Mirepip | Häufig | 150 | Moorbeeren | Klangfalle, Quellbecken | Mittag |
| 060 | Mirel | Ungew. | 250 | Moorbeeren | Quellbecken | Mittag |
| 062 | Undling | Häufig | 150 | Räucherfisch | Duftfalle, Quellbecken | Mittag |
| 063 | Undfin | Ungew. | 250 | Räucherfisch | Ruhenest, Ruhenetz, Quellbecken | Mittag |
| 065 | Irrlit | Häufig | 150 | Irrlicht-Laterne | – | Mittag |
| 066 | Irrel | Ungew. | 250 | Irrlicht-Laterne | – | Mittag |
| 069 | Blossi | Häufig | 150 | Moorbeeren | Schattenzelt, Wärmestein | Nacht |
| 070 | Blossar | Ungew. | 250 | Moorbeeren | Schattenzelt | Nacht |
| 072 | Virmote | Häufig | 150 | Moorbeeren | Klangfalle | Mittag/Nacht |
| 073 | Virwyn | Ungew. | 250 | Moorbeeren | – | Mittag/Nacht |
| 074 | Blightkin | Ungew. | 250 | Räucherfisch | Schattenzelt | Mittag |
| 075 | Blightar | Selten | 400 | Räucherfisch | Ruhenetz | Mittag |
| 076 | Brinlet | Häufig | 150 | Tangkeks | Ruhenest, Wärmestein, Quellbecken | Nacht |
| 077 | Brinshell | Ungew. | 250 | Tangkeks | Ruhenetz, Wärmestein, Quellbecken | Nacht |
| 078 | Umbrling | Ungew. | 250 | Räucherfisch | Schattenzelt, Quellbecken | Mittag |
| 079 | Umbracoil | Selten | 400 | Räucherfisch | Ruhenetz, Quellbecken | Mittag |
| 080 | Weidlit | Ungew. | 250 | Moorbeeren | Ruhenest, Schattenzelt | Mittag/Nacht |
| 082 | Morhaw | Ungew. | 250 | Räucherfisch | Ruhenetz | Mittag/Nacht |
| 083 | Humbog | Ungew. | 250 | Moorbeeren | Ruhenest, Klangfalle, Ruhenetz | Mittag |
| 084 | Torfgor | Selten | 400 | Moosküchlein | Ruhenest, Schattenzelt, Ruhenetz | – |
| 085 | Marlit | Häufig | 150 | Tangkeks | Ruhenetz, Quellbecken | Nacht |
| 086 | Marwyn | Ungew. | 250 | Tangkeks | Ruhenetz, Quellbecken | Nacht |
| 088 | Tidling | Häufig | 150 | Muschelfleisch | Schattenzelt | Mittag/Nacht |
| 089 | Tidel | Ungew. | 250 | Muschelfleisch | Schattenzelt, Ruhenetz, Schatzkiste | Mittag/Nacht |
| 091 | Brikin | Häufig | 150 | Räucherfisch | Duftfalle | Nacht |
| 092 | Brisel | Ungew. | 250 | Räucherfisch | – | Nacht |
| 094 | Aquapip | Häufig | 150 | Tangkeks | Quellbecken | Mittag |
| 095 | Aquafin | Ungew. | 250 | Tangkeks | Quellbecken | Mittag |
| 098 | Aerlet | Häufig | 150 | Windspiel | – | Nacht |
| 099 | Aerluna | Selten | 400 | Windspiel | – | Nacht |
| 100 | Stonlet | Häufig | 150 | Tangkeks | Wärmestein | Nacht |
| 101 | Stonshell | Ungew. | 250 | Tangkeks | Ruhenetz, Wärmestein | Nacht |
| 102 | Glimkin | Häufig | 150 | Tangkeks | Quellbecken | Mittag |
| 103 | Glimar | Ungew. | 250 | Tangkeks | Quellbecken | Mittag |
| 104 | Ariette | Ungew. | 250 | Windspiel | Klangfalle, Ruhenetz, Quellbecken | Mittag/Nacht |
| 106 | Tangi | Häufig | 150 | Tangkeks | Schattenzelt | Nacht |
| 107 | Tangix | Ungew. | 250 | Tangkeks | Schattenzelt, Ruhenetz | Nacht |
| 108 | Brassel | Ungew. | 250 | Muschelfleisch | Schatzkiste | Nacht |
| 109 | Sheamast | Selten | 400 | Irrlicht-Laterne | Ruhenetz | Mittag |
| 110 | Opalisk | Selten | 400 | Muschelfleisch | Ruhenest, Schatzkiste | Mittag |
| 111 | Solkit | Häufig | 150 | Datteln | Wärmestein | Mittag/Nacht |
| 112 | Solvar | Ungew. | 250 | Datteln | Wärmestein | Nacht |
| 114 | Dunkalb | Häufig | 150 | Datteln | Duftfalle, Schattenzelt, Ruhenetz | Nacht |
| 115 | Dunhorn | Ungew. | 250 | Datteln | Duftfalle, Ruhenetz | Nacht |
| 117 | Skarit | Häufig | 150 | Erzkrümel | Schatzkiste | Nacht |
| 118 | Skaral | Ungew. | 250 | Erzkrümel | Schatzkiste | Nacht |
| 120 | Sengel | Häufig | 150 | Glutkohle | Wärmestein | Nacht |
| 121 | Sengar | Ungew. | 250 | Glutkohle | Ruhenetz, Wärmestein | Nacht |
| 123 | Stachik | Häufig | 150 | Erzkrümel | Schattenzelt | Mittag |
| 124 | Stacharon | Selten | 400 | Erzkrümel | Ruhenetz | Mittag |
| 125 | Sirrkorn | Häufig | 150 | Windspiel | – | Nacht |
| 126 | Sirrsturm | Selten | 400 | Windspiel | Ruhenetz | Nacht |
| 127 | Mirasel | Ungew. | 250 | Spiegelscherbe | Schattenzelt | Nacht |
| 128 | Mirazhar | Sehr selten | 550 | Spiegelscherbe | Ruhenetz | Nacht |
| 129 | Vitrel | Häufig | 150 | Irrlicht-Laterne | Duftfalle | Mittag |
| 130 | Vitrapha | Selten | 400 | Irrlicht-Laterne | Duftfalle | Mittag |
| 131 | Mesakil | Ungew. | 250 | Erzkrümel | Ruhenest, Wärmestein | Nacht |
| 132 | Mesakor | Selten | 400 | Erzkrümel | Ruhenetz, Wärmestein | Nacht |
| 133 | Qadrant | Selten | 400 | Sternenglocke | Ruhenetz | Mittag |
| 134 | Mahrsil | Sehr selten | 550 | Glockenspiel | Klangfalle, Ruhenetz | Mittag |
| 135 | Pyrolm | Häufig | 150 | Schwefelzucker | Wärmestein, Quellbecken | Nacht |
| 136 | Pyrolax | Ungew. | 250 | Schwefelzucker | Wärmestein, Quellbecken | Nacht |
| 138 | Ambolt | Häufig | 150 | Erzkrümel | Schatzkiste | Nacht |
| 139 | Ambrak | Ungew. | 250 | Erzkrümel | Ruhenetz, Wärmestein | Nacht |
| 141 | Aschwel | Häufig | 150 | Glutkohle | Duftfalle | Mittag/Nacht |
| 142 | Aschund | Ungew. | 250 | Glutkohle | – | Mittag/Nacht |
| 144 | Obsikin | Häufig | 150 | Erzkrümel | Schattenzelt | Mittag |
| 145 | Obsidar | Ungew. | 250 | Erzkrümel | Schattenzelt, Ruhenetz | Mittag |
| 147 | Ignavyr | Selten | 400 | Schwefelzucker | Ruhenetz, Wärmestein | Nacht |
| 149 | Fumel | Ungew. | 250 | Irrlicht-Laterne | Schattenzelt | Mittag |
| 150 | Fumaroth | Selten | 400 | Irrlicht-Laterne | Ruhenetz | Mittag |
| 151 | Drusil | Ungew. | 250 | Kristallsalz | Schatzkiste | Nacht |
| 152 | Drusaro | Selten | 400 | Kristallsalz | Ruhenetz | Nacht |
| 153 | Volket | Häufig | 150 | Erzkrümel | Duftfalle, Schatzkiste | Nacht |
| 154 | Voltarn | Selten | 400 | Erzkrümel | Duftfalle, Ruhenetz | Nacht |
| 155 | Bassalt | Selten | 400 | Lockstimmgabel | Ruhenest, Klangfalle, Ruhenetz | Nacht |
| 156 | Nucleox | Sehr selten | 550 | Schwefelzucker | Ruhenetz, Wärmestein | Mittag |
| 157 | Snevel | Häufig | 150 | Eisfisch | Schattenzelt | Mittag/Nacht |
| 158 | Snevar | Ungew. | 250 | Eisfisch | Schattenzelt | Mittag/Nacht |
| 160 | Kjalf | Häufig | 150 | Bergkäse | Duftfalle, Ruhenetz | Nacht |
| 161 | Kjalmur | Ungew. | 250 | Bergkäse | Duftfalle, Ruhenetz | Nacht |
| 163 | Uvlet | Häufig | 150 | Eisfisch | Ruhenest | Mittag |
| 164 | Uvarn | Ungew. | 250 | Eisfisch | – | Mittag |
| 167 | Lyskin | Ungew. | 250 | Auroraglas | Ruhenetz | Mittag |
| 168 | Lysmara | Selten | 400 | Auroraglas | Ruhenetz | Mittag |
| 170 | Vardlit | Häufig | 150 | Erzkrümel | Ruhenest, Schatzkiste | Nacht |
| 171 | Vardholm | Ungew. | 250 | Erzkrümel | Ruhenest, Ruhenetz | Nacht |
| 172 | Eidrun | Ungew. | 250 | Glockenspiel | Klangfalle, Schattenzelt | Mittag |
| 173 | Eidwacht | Selten | 400 | Glockenspiel | Klangfalle, Ruhenetz | Mittag |
| 174 | Hallkid | Häufig | 150 | Bergkäse | Klangfalle | Nacht |
| 175 | Hallbrand | Ungew. | 250 | Bergkäse | Klangfalle, Ruhenetz | Nacht |
| 176 | Glazil | Häufig | 150 | Windspiel | – | Nacht |
| 177 | Glazvind | Selten | 400 | Windspiel | Ruhenetz | Nacht |
| 178 | Tysvorn | Sehr selten | 550 | Eisfisch | Ruhenetz | Mittag |
| 179 | Skriv | Häufig | 150 | Glyphenmünze | Schatzkiste | Mittag |
| 180 | Skrivar | Ungew. | 250 | Glyphenmünze | Ruhenetz, Schatzkiste | Mittag |
| 182 | Thaelit | Häufig | 150 | Lockstimmgabel | Ruhenest | Nacht |
| 183 | Thaelon | Ungew. | 250 | Lockstimmgabel | Ruhenetz | Nacht |
| 185 | Tikkel | Häufig | 150 | Erzkrümel | Schatzkiste | Nacht |
| 186 | Tikkar | Ungew. | 250 | Erzkrümel | Schatzkiste | Nacht |
| 188 | Sarkel | Ungew. | 250 | Irrlicht-Laterne | Schattenzelt, Ruhenetz | Mittag |
| 189 | Sarkon | Selten | 400 | Irrlicht-Laterne | Ruhenetz | Mittag |
| 191 | Tilgel | Ungew. | 250 | Glyphenmünze | Duftfalle, Schattenzelt | Mittag |
| 192 | Tilgrath | Selten | 400 | Glyphenmünze | Duftfalle, Schattenzelt, Ruhenetz | Mittag |
| 193 | Hymlit | Häufig | 150 | Lockstimmgabel | Duftfalle, Klangfalle, Wärmestein | Nacht |
| 194 | Hymnora | Ungew. | 250 | Lockstimmgabel | Duftfalle, Klangfalle | Nacht |
| 195 | Optil | Ungew. | 250 | Sternenglocke | – | Mittag |
| 196 | Optikor | Selten | 400 | Sternenglocke | Ruhenetz | Mittag |
| 197 | Menhirok | Selten | 400 | Lockstimmgabel | Ruhenest, Ruhenetz | Mittag |
| 198 | Kronvaal | Sehr selten | 550 | Glyphenmünze | Klangfalle, Ruhenetz | Mittag |
| 199 | Klirrit | Häufig | 150 | Kristallsalz | Klangfalle | Mittag |
| 200 | Klirrflug | Ungew. | 250 | Kristallsalz | Klangfalle | Mittag |
| 203 | Spatling | Häufig | 150 | Kristallsalz | Schattenzelt | Mittag |
| 204 | Spatwurm | Ungew. | 250 | Kristallsalz | Ruhenetz | Mittag |
| 206 | Ligrel | Häufig | 150 | Kristallsalz | Schattenzelt | Mittag |
| 207 | Ligrath | Ungew. | 250 | Kristallsalz | Ruhenetz | Mittag |
| 209 | Facetin | Häufig | 150 | Kristallsalz | – | Mittag/Nacht |
| 210 | Facettor | Ungew. | 250 | Kristallsalz | – | Mittag/Nacht |
| 211 | Mullit | Häufig | 150 | Erzkrümel | Schatzkiste | Mittag |
| 212 | Mullhorn | Ungew. | 250 | Erzkrümel | Ruhenetz, Schatzkiste | Mittag |
| 213 | Misslit | Ungew. | 250 | Lockstimmgabel | – | Mittag |
| 214 | Missgrath | Selten | 400 | Lockstimmgabel | Ruhenetz | Mittag |
| 215 | Psionit | Ungew. | 250 | Glyphenmünze | – | Mittag |
| 216 | Psioneth | Selten | 400 | Glyphenmünze | Ruhenetz | Mittag |
| 217 | Miasmar | Selten | 400 | Irrlicht-Laterne | Ruhenetz | Mittag |
| 218 | Stalakkord | Selten | 400 | Lockstimmgabel | Ruhenest, Klangfalle, Ruhenetz | Mittag |
| 219 | Nimbel | Häufig | 150 | Wolkenfrucht | Ruhenetz | Nacht |
| 220 | Nimbor | Ungew. | 250 | Wolkenfrucht | Klangfalle, Ruhenetz | Nacht |
| 222 | Cirrel | Häufig | 150 | Wolkenfrucht | – | Nacht |
| 223 | Cirrhawk | Ungew. | 250 | Wolkenfrucht | – | Nacht |
| 225 | Nubi | Häufig | 150 | Wolkenfrucht | Wärmestein | Nacht |
| 226 | Nubilo | Ungew. | 250 | Wolkenfrucht | – | Nacht |
| 229 | Harfel | Häufig | 150 | Windspiel | Ruhenest, Klangfalle | Nacht |
| 230 | Harfion | Ungew. | 250 | Windspiel | Klangfalle, Ruhenetz | Nacht |
| 231 | Tintel | Häufig | 150 | Glockenspiel | Klangfalle | Mittag/Nacht |
| 232 | Tintabul | Selten | 400 | Glockenspiel | Klangfalle, Ruhenetz | Mittag/Nacht |
| 233 | Holmel | Ungew. | 250 | Wolkenfrucht | Ruhenest, Duftfalle, Ruhenetz, Wärmestein | Nacht |
| 234 | Holmgard | Selten | 400 | Wolkenfrucht | Ruhenest, Ruhenetz | Nacht |
| 235 | Levitel | Häufig | 150 | Lockstimmgabel | Schatzkiste | Nacht |
| 236 | Levithar | Ungew. | 250 | Lockstimmgabel | Ruhenetz | Nacht |
| 237 | Graupel | Häufig | 150 | Windspiel | – | Nacht |
| 238 | Graupix | Selten | 400 | Windspiel | Ruhenetz | Nacht |
| 239 | Lumaskiff | Selten | 400 | Wolkenfrucht | Ruhenetz | Nacht |
| 240 | Astraviel | Sehr selten | 550 | Sternenglocke | Ruhenetz | Mittag |
| 241 | Sylv'anor | Stimme | 750 | Glockenspiel | Duftfalle, Klangfalle, Ruhenetz | Nacht |
| 242 | Orh'gruun | Stimme | 750 | Lockstimmgabel | Ruhenest, Ruhenetz | Nacht |
| 243 | Nhael'vesh | Stimme | 750 | Irrlicht-Laterne | Schattenzelt, Ruhenetz | Mittag/Nacht |
| 244 | Thal'assyr | Stimme | 750 | Windspiel | Ruhenetz, Quellbecken | Nacht |
| 245 | Ash'kareth | Stimme | 750 | Spiegelscherbe | Ruhenetz, Wärmestein | Nacht |
| 246 | Pyr'thagon | Stimme | 750 | Schwefelzucker | Ruhenetz, Wärmestein | Nacht |
| 247 | Isv'aldr | Stimme | 750 | Auroraglas | Klangfalle, Ruhenetz | Mittag |
| 248 | Ka'thurel | Stimme | 750 | Glyphenmünze | Ruhenetz, Schatzkiste | Mittag |
| 249 | Prism'aion | Stimme | 750 | Kristallsalz | Klangfalle, Ruhenetz | Mittag |
| 250 | Aeth'rion | Stimme | 750 | Sternenglocke | Klangfalle, Ruhenetz | Nacht |
| 251 | Velnox | Mythisch | 750 | Glockenspiel | Schattenzelt, Ruhenetz | Mittag |
| 252 | Chronaire | Mythisch | 750 | Lockstimmgabel | Ruhenetz | Nacht |
| 253 | Mirrowisp | Mythisch | 750 | Spiegelscherbe | Schattenzelt | Mittag/Nacht |
| 254 | Ouroveth | Mythisch | 750 | Moorbeeren | Duftfalle, Schattenzelt, Ruhenetz | Mittag/Nacht |
| 255 | Zenthrax | Mythisch | 750 | Sternenglocke | Ruhenetz | Mittag |
| 256 | Aurelune | Mythisch | 750 | Auroraglas | Ruhenetz | Mittag |

---

## 9. Bindung im Kampf

| Regel | Wert |
|---|---|
| Aktion | „Binden“ des Wärters über ein aktives Echo, Zeitkosten 100 (K31) |
| Voraussetzung | Wildecho ohne Reserve aktiv; bei Herden das **letzte** verbleibende Echo – oder ein beliebiges mit dem Ruhenetz |
| Resonanz | R aus Kampf-Erschöpfung + Status + vorherige Phasen (Köder/Falle vor dem Kampf zählen weiter) |
| Anschlag | identisch zum Oberwelt-Anschlag; Kampf pausiert während des Anschlags |
| Ergebnis | Einklang/Bindung beenden den Kampf; Annäherung: Kampf geht weiter (R +100); Verfehlt: Reaktion nach Temperament |
| Verklingen | Ein verklungenes Wildecho kann nicht mehr gebunden werden (es zieht sich zurück) – Bindung lohnt vor dem K.O. |
| EP | Bindung gibt ×1,2 der EP eines Sieges (ADR-087) |

---

## 10. Sonderfälle

| Fall | Regel |
|---|---|
| Prolog (Erstresonanz) | Fenster ×1,5, Versuche unbegrenzt, Annäherung +150 – kann nicht scheitern (K02) |
| Volle Chor-Plätze | Gebundenes Echo geht in den Resonanzhain (K37); Hinweis, kein Abbruch |
| Alpha-Echos | Kampf erforderlich (Alphas lassen sich nicht ohne Kampf einstimmen); Schwelle 600 |
| Stille-Echos | nicht bindbar; Sieg heilt (K35) |
| Ursprungsstimmen | Story-Begegnung; Stimmsiegel; Anschlag mit drei Pulsen (alle drei Gut/Perfekt nötig, Fenster ≥ 300 ms) |
| Mythische | Bindungsfenster ≤ 15 % HP (K35 §9), Sternensiegel, instanziert im Raid |
| Koop | Bindung durch den Spieler, der „Binden“ wählt; andere Spieler können vorher Köder/Fallen beitragen (zählen für R); Herkunft vermerkt den Koop-Partner (DR-16) |
| Eiserner Wärter | Bindung nur mit Einklang oder Bindung beim ersten Versuch je Echo (Hardcore-Regel) |
| Morphs | Morph-Chance ist unabhängig von R und Timing (DR-15: reiner Zufall nur für Morphs, K38) |
| Bindung verweigern | Optionale Mitgefühl-Option „Freilassen“ nach dem Einstimmen: +Kodex-Beobachtung, Fraktion Wildwacht +Ruf (K47) |

---

## 11. Präsentation, Haptik, Barrierefreiheit

| Element | Vorgabe |
|---|---|
| Resonanzring | Füllstand R, Schwellenmarke, Farbe der Klangfarbe; Zahlen optional |
| Puls | Klangmal-Leuchten + Ton + Controller-Haptik in Echo-Frequenz (PS5 adaptive Trigger: Widerstand steigt zum Fenster) |
| Feedback | Perfekt: Chor-Akkord, Lichtwelle; Gut: Glocke; Annäherung: Echo lauscht; Verfehlt: Dissonanz kurz |
| Optionen | Großzügiges Timing (×1,75), Auto-Einklang (Taste halten statt Timing → Ergebnis „Bindung“, nie „Einklang“), visuelles Metronom, Vibration aus |
| Hörgeschädigte | Visueller Puls + Haptik ersetzen den Ton vollständig (DR-24) |
| Sichtbarkeit | Vor dem Anschlag zeigt die Vorschau R, Schwelle, Fensterbreite und Versuche – kein verstecktes Wissen |

---

## 12. Code

```cpp
// GF_Capture – Resonanzbindung (implementiert IBondingService, CR-002)
FBondPreview UResonanceBondingService::PreviewBond(const FGuid& WildEchoId, FPrimaryAssetId Seal) const
{
    const FWildEchoState& W = World->GetWild(WildEchoId);
    const UEchoSpeciesDefinition& Sp = *W.Species;
    const USealDefinition& S = *Seals->Get(Seal);
    FBondPreview P;
    P.Resonance = Aethris::Bond::Resonance(Kodex->Stage(Sp), W.ApproachBonus, W.LureBonus, W.TrapBonus,
                                           W.HpLostPermille, W.bStatused, W.bRestPhase, LevelGap(W));
    P.Threshold = Aethris::Bond::Threshold(W.EffectiveRarity()) - S.ThresholdBonusFor(Sp, Clock->Phase());
    const int32 Good = Aethris::Bond::GoodWindowMs(P.Resonance, Temperament(W).BondWindowPermille, S.WindowPermille, Options->bGenerousTiming);
    P.GoodWindowMs = Good;
    P.PerfectWindowMs = FMath::Max(60, Good / 4);
    P.AttemptsLeft = W.AttemptsLeft;
    P.bRequiresSpecialSeal = Sp.IsLegendaryOrMythical();
    return P;
}

namespace Aethris::Bond
{
    constexpr int32 KodexBonus[5] = { 0, 60, 120, 180, 240 };
    constexpr int32 GoodWindowMs(int32 R, int32 TempPermille, int32 SealPermille, bool bGenerous)
    {
        const int32 G = (160 + 240 * R / 1000) * TempPermille / 1000 * SealPermille / 1000;
        return bGenerous ? G * 1750 / 1000 : G;
    }
    static_assert(GoodWindowMs(0, 1000, 1000, false) == 160 && GoodWindowMs(1000, 1000, 1000, false) == 400);
}
```

**Timing-Messung:** Eingabezeit wird gegen den **Audio-Zeitstempel** des Pulses gemessen (Quartz-Uhr), nicht gegen Frame-Zeit – plattformunabhängig, latenzkompensiert über die Kalibrierung im Optionsmenü (Audio-/Video-Versatz).

---

## 13. Tests und Telemetrie

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Bond.Resonance` | Formel, Grenzen 0–1000, alle Quellen |
| `…Bond.Window` | Q12-Werte, Temperament, Siegel, Großzügig |
| `…Bond.Outcome` | Einklang/Bindung/Annäherung/Verfehlt-Matrix |
| `…Bond.DR01` | Kodex 3 + Klangsiegel ≥ Kodex 0 + Meistersiegel für alle Seltenheiten |
| `…Bond.PythonParity` | 20.000 Szenarien gegen `aethris_bond.py` |
| `Aethris.Func.Bond.Latency` | Timing-Messung mit simuliertem 100-ms-Versatz nach Kalibrierung korrekt |

**Telemetrie-Ziele:** Ø Anschläge bis Bindung 1,4–2,0; Anteil Einklang 25–40 %; Anteil Bindungen mit Lieblingsköder ≥ 30 % nach Akt I (Zeichen, dass Kodex-Wissen genutzt wird); Fluchtquote Wachsam ≤ 20 %.

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-131 | Bindung deterministisch: Resonanz ≥ Schwelle + Timing; kein Prozentwurf | DR-03/DR-07, Vorschau ehrlich | Fangquote mit Würfel (Genre-Konvention, Clean-Room) |
| ADR-132 | Teilerfolg „Annäherung“ (+100 R) statt Fehlschlag | DR-10, kein Frust | Verfehlt bei zu wenig Resonanz |
| ADR-133 | Kodex-Bonus bis 240 > Siegelbonus 80 | DR-01 messbar | Starke Premium-Siegel |
| ADR-134 | Timing gegen Audio-Uhr (Quartz) mit Kalibrierung | Fairness über Plattformen/TVs | Frame-basierte Messung |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §132 | Ablauf Lauschen → Annähern → Einstimmen (oder Kampf) → Anschlag; Dauer 20–60 s (ohne Kampf) | LOCKED |
| §133 | Resonanz R 0–1000: Kodex 0/60/120/180/240, Annäherung 0–150, Köder −50/+100/+200, Falle 100–200, Kampf min(250, 0,3 × HP-Verlust‰), Status +50, Tageszeit +50, Levelstrafe −10/Level über Chor+10, Annäherung +100; Schwellen 150/250/400/550/600/750/750 | LOCKED |
| §134 | Gut-Fenster (160 + 240 × R/1000) ms × Temperament × Siegel (× 1,75 Option); Perfekt 25 % min. 60 ms; Versuche 2–4; Ergebnisse Einklang (Perfekt, R ≥ Schwelle − 100) / Bindung / Annäherung / Verfehlt; **Q12 gelöst** | LOCKED |
| §135 | Siegel (8, `Seals.csv`) Schwellenbonus 0/40/80 (bedingt 60), Verbrauch nur beim Anschlag; Fallen (8, `Traps.csv`), max. 1; Lockmittel-Wirkungen | LOCKED (Preise → K42) |
| §136 | Sonderfälle: Prolog unscheiterbar, Alpha nur mit Kampf, Stille-Echos nicht bindbar, Stimmen 3 Pulse, Mythische Fenster ≤ 15 %, Koop-Beiträge, Eiserner Wärter, Freilassen-Option | LOCKED |
| §11 | CR-002: `PreviewBondChancePermille` → `PreviewBond`/`FBondPreview` | – |
| §10 | ADR-131 – ADR-134 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Bindungsphilosophie und vier Phasen
- [x] Resonanzwert-Formel und Schwellen nach Seltenheit (deterministisch)
- [x] Timing-Fenster final (Q12), Temperament- und Siegeleinfluss
- [x] Ergebnisse, Reaktionen, Annäherung als Teilerfolg
- [x] Siegel (8) und Fallen (8) als Daten, Lockmittel-Wirkung
- [x] Szenario-Rechnungen (Referenzmodell)
- [x] Bindung im Kampf, alle Sonderfälle inkl. Legendär/Mythisch/Koop
- [x] Präsentation, Haptik, Barrierefreiheit, Code (CR-002), Tests, Telemetrie
- [x] ADR-131 – ADR-134, CANON §132–§136

➡️ **Nächstes Kapitel: K37 – Begleiter, Bindungsstufen und Resonanzhain (löst Q8).**
