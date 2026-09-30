# K01 · Executive Summary

| Feld | Wert |
|---|---|
| Projekt | **AETHRIS: Echobound** (Arbeitstitel = Release-Titel, siehe ADR-001) |
| Dokument | Kapitel 01 von 68 |
| Version | 1.0 |
| Owner | Game Director |
| Mitwirkende | Creative Director, Lead Gameplay Programmer, Unreal Senior Dev, Combat Designer, RPG Systems Designer, Economy Designer, Network Engineer, QA Lead |
| Status | ✅ Freigegeben (Greenlight-Grundlage) |
| Kanon-Einträge | `CANON.md` §1–§9 (neu angelegt) |

---

## Inhalt

1. [High Concept](#1-high-concept)
2. [Vision Statement](#2-vision-statement)
3. [Die fünf Design-Säulen](#3-die-fünf-design-säulen)
4. [Genre-Positionierung & Abgrenzung](#4-genre-positionierung--abgrenzung)
5. [Die Welt in einem Absatz](#5-die-welt-in-einem-absatz)
6. [Die Spielerfantasie](#6-die-spielerfantasie)
7. [Core Loops](#7-core-loops)
8. [Feature-Übersicht](#8-feature-übersicht)
9. [Content-Umfang (Zielzahlen)](#9-content-umfang-zielzahlen)
10. [Zielgruppe & Personas](#10-zielgruppe--personas)
11. [Plattformen, Technik & Performance-Ziele](#11-plattformen-technik--performance-ziele)
12. [Engine-Entscheidung](#12-engine-entscheidung)
13. [Architektur auf einen Blick](#13-architektur-auf-einen-blick)
14. [Geschäftsmodell & Monetarisierung](#14-geschäftsmodell--monetarisierung)
15. [Team & Organisation](#15-team--organisation)
16. [Zeitplan & Budget](#16-zeitplan--budget)
17. [Risiko-Register](#17-risiko-register)
18. [Erfolgskriterien & KPIs](#18-erfolgskriterien--kpis)
19. [Architecture/Design Decision Records](#19-architecturedesign-decision-records)
20. [Offene Fragen für Folgekapitel](#20-offene-fragen-für-folgekapitel)
21. [Kapitel-Checkliste](#21-kapitel-checkliste)

---

## 1. High Concept

> **AETHRIS: Echobound ist ein Open-World-Monster-Collecting-RPG, in dem jede Kreatur ein lebendiges Echo des zerbrochenen Weltlieds ist. Der Spieler bindet diese „Echos“ nicht durch Gewalt, sondern durch Resonanz – er muss ihre Frequenz verstehen, sie beruhigen und im richtigen Moment mit ihnen in Einklang kommen. Gemeinsam kämpft er in einem taktischen Zeitleisten-Kampfsystem, erforscht eine 36 km² große, von Wetter, Tageszeit und Ökologie gesteuerte Welt und entscheidet, ob das Weltlied wieder erklingen oder für immer verstummen soll.**

### Pitch in einem Satz (Marketing)

*„Hör genau hin – jede Kreatur in Aethris ist ein Lied, das darauf wartet, verstanden zu werden.“*

### Pitch in drei Sätzen (Publisher)

1. Ein Monster-Collecting-RPG mit der Weltqualität eines modernen AAA-Open-World-Spiels: echte Ökosysteme, Herden mit Alphatieren, Wetter, das bestimmt, welche Kreaturen erscheinen und wie sie sich entwickeln.
2. Ein Kampfsystem, das Genre-Zugänglichkeit mit echter taktischer Tiefe verbindet: Initiative-Zeitleiste statt simultaner Runden, Positionierung in Reihen, Combos zwischen Kreaturen und ein Wetter-/Terrain-Layer.
3. Ein Bindungssystem („Resonanzbindung“), das Fangen in ein geschicktes, spielerisch lesbares Minispiel aus Annäherung, Beruhigung und Timing verwandelt – und ein Zucht-/Genetiksystem, das Sammler über Hunderte Stunden bindet.

---

## 2. Vision Statement

Monster-Collecting-Spiele leben von drei Emotionen: **Entdeckung** („Was lebt hinter diesem Hügel?“), **Bindung** („Das ist *mein* Partner“) und **Meisterschaft** („Mein Team schlägt jedes andere“). Das Genre hat diese Emotionen über Jahrzehnte bewiesen, aber es hat sie selten mit der technischen und erzählerischen Ambition des AAA-Open-World-Segments verbunden.

**Unsere Vision:** Wir bauen das Monster-Collecting-RPG, bei dem die Welt nicht Kulisse für Zufallsbegegnungen ist, sondern ein **glaubwürdiges Ökosystem**, in dem Kreaturen jagen, schlafen, Reviere verteidigen und auf das Wetter reagieren – und in dem der Spieler durch **Zuhören** statt durch Werfen zum Partner dieser Kreaturen wird.

### Was AETHRIS *ist*

- Ein **Singleplayer-first**-RPG mit vollständiger, dreiaktiger Story, das nahtlos um Koop, Tausch, PvP und Raids erweitert wird.
- Ein **systemisches** Spiel: Wetter × Tageszeit × Biom × Ökologie erzeugen Situationen, die kein Designer einzeln gescriptet hat.
- Ein **Langzeit-Hobby**: Zucht, Genetik, Morphs, Kodex-Forschung, Fotografie, Ranked-Saisons.

### Was AETHRIS *nicht ist*

- Kein Klon: keine übernommenen Namen, Kreaturendesigns, Fanggegenstände, Typnamen-Konventionen oder UI-Metaphern (siehe §4.3 Abgrenzungsregeln).
- Kein Live-Service-First-Spiel: Die Kernerfahrung ist offline vollständig spielbar.
- Kein Pay-to-Win: Keine käuflichen Kreaturen, Werte, Siegel oder Zuchtvorteile.
- Kein Action-Brawler: Die Kämpfe sind rundenbasiert-taktisch; die Oberwelt ist actionreich (Traversal, Reiten, Fang-Timing), der Kampf ist denkend.

---

## 3. Die fünf Design-Säulen

Jede Designentscheidung in allen 68 Kapiteln wird gegen diese Säulen geprüft. Ein Feature, das keine Säule stärkt, wird gestrichen oder verschoben.

| # | Säule | Leitsatz | Messbar durch | Primäre Systeme |
|---|---|---|---|---|
| S1 | **Lebendige Resonanz** | „Die Welt reagiert – und sie existiert auch ohne den Spieler.“ | ≥ 70 % der Playtester nennen ungescriptete Welt-Momente in Interviews | Ökologie-KI, Wetter, Tageszeit, NPC-Tagesabläufe, Schwärme |
| S2 | **Bindung durch Verstehen** | „Man fängt nicht, man versteht.“ | Fang-Erfolgsquote korreliert mit Wissen (Kodex-Stufe), nicht nur mit Itemwert | Resonanzbindung, Begleitersystem, Echo-Kodex, Fotografie |
| S3 | **Taktische Harmonie** | „Leicht zu lesen, schwer zu meistern.“ | Tutorial-Abschluss < 12 min; Ranked-Skill-Spread (Elo-SD) > 300 | Zeitleisten-Kampf, Typen, Positionierung, Combos, Synergien |
| S4 | **Erbe & Einzigartigkeit** | „Kein Echo gleicht dem anderen.“ | ≥ 25 % der Spieler züchten nach 40 h aktiv; Morph-Screenshots in Social | Zucht, Genetik, Morphs, Persönlichkeiten |
| S5 | **Gemeinsamer Chor** | „Allein vollständig, zusammen größer.“ | ≥ 35 % der Spieler nutzen innerhalb von 30 Tagen eine Online-Funktion | Koop, Tausch, Raids, Gilden, PvP |

### Säulen-Prioritätsregel (ADR-002)

Bei Konflikten gilt die Reihenfolge **S2 > S3 > S1 > S4 > S5**. Begründung: Bindung und Kampf sind das, was das Genre definiert; ohne sie trägt keine noch so lebendige Welt. Online-Features sind Multiplikator, nicht Fundament.

*Beispielkonflikt:* Ein Raid-Boss soll sich nur mit spezifischen Team-Rollen besiegen lassen (S5), was Solo-Spielern den Zugang zu einer legendären Kreatur verwehren würde (S2). → Entscheidung: Legendäre Kreaturen aus Raids haben **immer** einen Solo-Zugangsweg (anspruchsvoller, zeitaufwändiger), Raids sind die gesellige Abkürzung.

---

## 4. Genre-Positionierung & Abgrenzung

### 4.1 Marktlandschaft (Stand Q3 2026)

```
                          SYSTEMISCHE TIEFE DER WELT
                  niedrig ◄───────────────────────────► hoch
             ┌────────────────────────────────────────────────┐
     hoch    │                          │                     │
             │  Klassische Genre-       │   ★ AETHRIS         │
  KAMPF-     │  Titel (rundenbasiert,   │   (Ziel-Quadrant)   │
  TIEFE      │  kompetitiv, Routen)     │                     │
             │──────────────────────────┼─────────────────────│
             │  Casual/Mobile-          │  Survival-Crafting- │
     niedrig │  Collectors              │  Creature-Games     │
             │                          │  (Echtzeit, flach)  │
             └────────────────────────────────────────────────┘
```

Das obere rechte Quadrant – hohe Kampftiefe **und** systemische Welt – ist unbesetzt. Genau dort positionieren wir AETHRIS.

### 4.2 Differenzierungsmatrix

| Genre-Konvention | Übliche Umsetzung | AETHRIS-Umsetzung | Säule |
|---|---|---|---|
| Kreaturen fangen | Wurfgegenstand + Zufallswurf | **Resonanzbindung:** Annähern → Beruhigen/Locken → Timing-Fenster auf Echofrequenz; Siegel als Medium, Fallen als Weltobjekte | S2 |
| Kampfreihenfolge | Simultane Runde, Speed entscheidet | **Resonanz-Zeitleiste:** sichtbare Initiative-Reihe, Aktionen haben Zeitkosten, Priorität verschiebt Positionen | S3 |
| Positionierung | Keine / nur Doppelkampf-Zielwahl | **Formation:** Vorder-/Hinterreihe, Nah-/Fernfähigkeiten, Schutzmechaniken | S3 |
| Typen | ~18 Typen, feste Tabelle | **15 eigenständige Typen**, Tabelle + Wetter-/Terrain-Modulation (Typ-Resonanz) | S3 |
| Begegnungen | Hohes Gras, Zufall | Sichtbare Kreaturen mit Ökologie-KI, Rudeln, Tagesrhythmus | S1 |
| Entwicklung | Level-Schwellen dominieren | Level, Bindung, Items, Tageszeit, Wetter, Gebiet **und Kombinationen**; sichtbare „Evolutionsahnung“ im Kodex | S2/S1 |
| Zucht | Werte/Attacken vererben | **Mendel-inspirierte Genetik** mit dominanten/rezessiven Allelen, Farbmorphs, Mutationen | S4 |
| Aufbewahrung | Abstrakte PC-Boxen | **Resonanzhain:** begehbares Refugium, in dem Echos sichtbar leben | S2/S1 |
| Kreaturen-Enzyklopädie | Sehen = Eintrag | **Echo-Kodex:** Forschungsstufen durch Beobachten, Kämpfen, Fotografieren, Züchten | S2 |
| Online | Tausch + Kämpfe | Koop-Oberwelt (bis 4), Raids (4 Spieler), Gilden, Ranked-Saisons mit Replays | S5 |

### 4.3 Abgrenzungsregeln („Clean-Room-Policy“) – LOCKED

Diese Regeln sind verbindlich für alle Disziplinen und werden vom Creative Director und Legal geprüft (Gate in jedem Content-Review):

1. **Keine übernommenen Begriffe.** Verboten sind u. a. Begriffe für Fanggegenstände, Kreaturenoberbegriffe, Arenaleiter-Titel, Enzyklopädie-Namen und Kampfbegriffe bekannter Franchises. Wir verwenden ausschließlich unser Glossar (K04).
2. **Keine Silhouetten-Nähe.** Jedes Kreaturendesign durchläuft einen Silhouetten-Check gegen eine Referenzdatenbank bekannter Kreaturen (K16). Ähnlichkeit > definierter Schwellwert → Redesign.
3. **Keine 1:1-Mechaniken.** Wo das Genre Konventionen hat (Typen, Level, Evolution), müssen wir mindestens **eine eigene strukturelle Achse** hinzufügen (z. B. Wetter-Modulation der Typtabelle, Zeitleiste statt Runde).
4. **Eigene Farbsprache der Typen.** Typfarben werden aus unserer Art Bible abgeleitet (K56), nicht aus Genre-Konventionen.
5. **Namenskonstruktion.** Kreaturennamen entstehen aus unserem eigenen Morphem-Lexikon (K04) mit Kollisionsprüfung gegen Markenregister.

---

## 5. Die Welt in einem Absatz

**Aethris** ist ein Kontinent, der einst vom *Weltlied* (Aethersang) durchdrungen war – einer allgegenwärtigen Resonanz, aus der alles Leben hervorging. Vor rund 1.000 Jahren zerbrach das Weltlied in der **Großen Stille**. Seine Fragmente leben seither als **Echos** weiter: Kreaturen, deren Körper, Verhalten und Kräfte Nachklänge eines Teils des alten Liedes sind. Menschen haben gelernt, mit Echos in Resonanz zu treten; die, die es beruflich tun, heißen **Wärter**. Heute zeigen sich an vielen Orten *Stillezonen* – Gebiete, in denen Echos verstummen, erstarren und verschwinden. Während die Akademie forscht, die Wildwacht schützt und die Händler profitieren, glaubt der **Orden der Stille**, dass das Weltlied die Ursache allen Leids ist und endgültig verstummen muss. Der Spieler, ein junger Wärter aus dem Waldland **Verdanthain**, entdeckt, dass er eine seltene Fähigkeit besitzt: Er kann die *Grundfrequenz* eines Echos hören.

### 5.1 Die zehn Regionen (LOCKED – Details in K08–K10)

| ID | Region | Biom | Rolle in der Progression | Hauptstadt |
|---|---|---|---|---|
| R01 | Verdanthain | Wälder | Startregion, Tutorial, Akt I | Eichenhall |
| R02 | Kharsgrat | Gebirge | Akt I–II | Kharsholm |
| R03 | Morvenmoor | Sümpfe | Akt I–II | Morvenfurt |
| R04 | Sahrun-Weite | Wüste | Akt II | Qasr Sahrun |
| R05 | Ignareth | Vulkan | Akt II | Schlackenwehr |
| R06 | Saltrand | Küste | Akt I–II | Saltrand-Hafen |
| R07 | Hvitfell | Schnee | Akt II–III | Hvitmark |
| R08 | Ael'Dorun | Ruinen | Akt II–III (Mysterium-Kern) | Dorunsruh |
| R09 | Prismtiefen | Kristallhöhlen | Akt III, Endgame-Dungeons | Prismara |
| R10 | Nimbara | Himmelinseln | Akt III, Finale, Endgame | Aerion |

---

## 6. Die Spielerfantasie

> *„Ich bin ein Wärter, der die Welt hören kann. Ich ziehe mit meinem Chor aus Echos durch ein wildes, lebendiges Land, verstehe jede Kreatur ein Stück besser, forme mit ihnen ein unschlagbares Team – und entscheide am Ende, welche Musik diese Welt spielen soll.“*

### 6.1 Fantasie-Bausteine

| Baustein | Was der Spieler fühlt | Wie wir es liefern |
|---|---|---|
| Der Lauscher | „Ich nehme mehr wahr als andere.“ | **Resonanzsinn** (Oberwelt-Fähigkeit): hebt Echofrequenzen, Spuren, versteckte Nester hervor |
| Der Partner | „Meine Echos vertrauen mir.“ | Begleitersystem, sichtbare Reaktionen, Bindungsstufen, Echos folgen in der Oberwelt |
| Der Stratege | „Ich habe den Kampf durchschaut.“ | Zeitleiste zeigt Zukunft; Combos und Formation belohnen Planung |
| Der Forscher | „Ich weiß Dinge über diese Welt, die im Spiel versteckt sind.“ | Kodex-Stufen, versteckte Evolutionsbedingungen, Fotografie |
| Der Züchter | „Dieses Echo gibt es nur einmal – ich habe es erschaffen.“ | Genetik, Morphs, Stammbaum, Herkunftssignatur |
| Der Held | „Meine Entscheidung verändert die Welt.“ | Drei Akte, Fraktionsentscheidungen, zwei Hauptenden + Varianten |

---

## 7. Core Loops

### 7.1 Moment-to-Moment (Sekunden)

```
   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
   │  WAHRNEHMEN  │────►│   ENTSCHEIDEN │────►│   HANDELN    │
   │ Resonanzsinn,│     │ Kämpfen? Bin- │     │ Traversal,   │
   │ Sicht, Klang │     │ den? Umgehen? │     │ Fang-Timing, │
   └──────▲───────┘     └──────────────┘     │ Kampfaktion  │
          │                                  └──────┬───────┘
          │            ┌──────────────┐             │
          └────────────│   FEEDBACK   │◄────────────┘
                       │ VFX, Musik-  │
                       │ Layer, Echo- │
                       │ Reaktion     │
                       └──────────────┘
```

### 7.2 Session Loop (30–90 Minuten)

```
  ERKUNDEN ──► BEGEGNEN ──► BINDEN / KÄMPFEN ──► ERFORSCHEN (Kodex)
     ▲                                                  │
     │                                                  ▼
  NEUES ZIEL ◄── FORTSCHRITT ◄── VERBESSERN ◄── ZURÜCK IN DIE STADT
  (Quest,        (Level, Ruf,    (Crafting,     (Händler, Resonanzhain,
   Gebiet)        Skillpunkte)    Training,      Quests abgeben)
                                  Zucht)
```

### 7.3 Meta Loop (Wochen / Monate)

```
  ┌───────────────────────────────────────────────────────────────┐
  │ STORY (Akt I → II → III)                                      │
  │   └─► schaltet Regionen, Reittier-Fähigkeiten, Ranglisten frei│
  │                                                               │
  │ SAMMELN ──► KODEX 100 % ──► LEGENDÄRE SPUREN                  │
  │ ZÜCHTEN ──► PERFEKTE GENE / MORPHS ──► PvP / ZEIGEN           │
  │ PvP-SAISON ──► RANG ──► SAISONBELOHNUNG ──► NEUE SAISON       │
  │ RAIDS ──► BESONDERE BEUTE ──► CRAFTING-TIER ──► SCHWERERE RAIDS│
  │ UPDATES ──► NEUE REGION / ECHOS / EVENTS ──► ZURÜCKKEHREN     │
  └───────────────────────────────────────────────────────────────┘
```

### 7.4 Spielzeit-Ziele (LOCKED als Designziel)

| Spielertyp | Umfang | Zielzeit |
|---|---|---|
| Story-Fokus | Hauptstory, notwendige Nebeninhalte | 35–45 h |
| Standard-Completionist | Story + 50 % Nebenquests + 60 % Kodex | 80–110 h |
| Vollständig | Alle Quests, 100 % Kodex (ohne Morphs) | 180–220 h |
| Hobbyist | Zucht, Ranked, Raids, Morphs | open-ended (500 h+) |

---

## 8. Feature-Übersicht

Priorisierung nach **MoSCoW** (Must / Should / Could / Won't in 1.0). „Kapitel“ zeigt, wo das Feature vollständig spezifiziert wird.

### 8.1 Welt & Erkundung

| Feature | Beschreibung | Prio | Kapitel |
|---|---|---|---|
| Open World 36 km² | 10 Regionen, nahtlos gestreamt (World Partition) | M | K08–K10 |
| 10 Städte, 22 Dörfer, 30 Außenposten | Mit Geschichte, Händlern, Arenen, Tagesabläufen | M | K11–K13 |
| Dynamisches Wetter | 10 Wetterzustände, regionale Wahrscheinlichkeiten, Gameplay-Wirkung | M | K14 |
| 24-h-Tageszyklus | 72 Echtzeitminuten pro Spieltag, 4 Phasen | M | K15 |
| Traversal | Klettern, Gleiter, Schwimmen, Reittiere (Flug, Schwimmen, Klettern, Graben) | M | K40 |
| Resonanzsinn | Wahrnehmungsmodus für Spuren und Frequenzen | M | K36/K39 |
| Schnellreise | Resonanzsteine (freischaltbar) | M | K08 |

### 8.2 Kreaturen

| Feature | Beschreibung | Prio | Kapitel |
|---|---|---|---|
| 256 Echos | Inkl. 16 legendären/mythischen | M | K16–K27 |
| 15 Typen | Eigene Effektivitätstabelle + Typ-Resonanz (Wetter/Terrain) | M | K17 |
| 8 Statuswerte + Persönlichkeit, Temperament, Wachstumsrate | Wie im Briefing | M | K18 |
| Evolution | Keine / 2-stufig / 3-stufig / Spezial; kombinierbare Auslöser | M | K19 |
| 330 Fähigkeiten | Aktiv, Passiv, Ultimate, Feld | M | K28–K30 |
| Animationssatz | 9 Pflicht-States pro Echo (Idle, Rennen, Schlafen, Essen, Kämpfen, Spezial, Treffer, Sieg, Niederlage) | M | K57 |

### 8.3 Kampf

| Feature | Beschreibung | Prio | Kapitel |
|---|---|---|---|
| Resonanz-Zeitleiste | Initiative-basierte Zugfolge mit Zeitkosten | M | K31 |
| Priorität | Verschiebung auf der Zeitleiste | M | K31 |
| Harmonie & Combos | Teamleiste, Folgeaktionen, Crescendo (Ultimate) | M | K33 |
| Formation | Vorder-/Hinterreihe | M | K33 |
| Terrain & Wetter | Feldzustände, Typ-Resonanz | M | K32 |
| Formate 1v1, 2v2, 3v3 | Duell, Duo, Trio | M | K33 |
| Raids | 4 Spieler vs. Boss, Phasen, Rollen | S | K35 |
| Replays | Deterministische Kampfwiedergabe | S | K61 |

### 8.4 Bindung & Sammeln

| Feature | Beschreibung | Prio | Kapitel |
|---|---|---|---|
| Resonanzbindung | Annähern, Beruhigen, Locken, Timing, Siegel, Fallen | M | K36 |
| Begleitersystem | Streicheln, Füttern, Trainieren, Spielen → Bindung | M | K37 |
| Zucht & Genetik | Allele, Morphs, Mutationen | M | K38 |
| Echo-Kodex | 4 Forschungsstufen pro Echo | M | K39 |
| Fotografie | Kodex-Linse mit Bewertung (Pose, Seltenheit, Licht, Komposition) | S | K39 |
| Resonanzhain | Begehbares Refugium für gelagerte Echos | S | K37 |

### 8.5 Spieler

| Feature | Beschreibung | Prio | Kapitel |
|---|---|---|---|
| Ausrüstung | Kleidung, Rucksäcke, Werkzeuge, Gleiter | M | K40 |
| Crafting | Holz, Erz, Kristalle, Kräuter (+ Echo-Materialien) | M | K41 |
| Wirtschaft | Dynamische Preise, Nachfrage, seltene Waren | M | K42 |
| Skilltree | 4 Äste: Bindung, Überleben, Forschung, Kampf | M | K43 |
| Charakter-Editor | Körper, Gesicht, Stimme, Pronomenwahl | M | K54 |

### 8.6 Narrative

| Feature | Beschreibung | Prio | Kapitel |
|---|---|---|---|
| Hauptstory 3 Akte | ~32 Hauptquests, 2 Hauptenden + Varianten | M | K44–K46 |
| 5 Fraktionen | Rufsystem, Belohnungen, Quests | M | K47 |
| 210 Nebenquests | Dialoge, Entscheidungen, Belohnungen, Rätsel, Jagden | M | K49–K51 |
| Arenen | 10 Stadt-Arenen mit Arenameistern | M | K11–K12 |

### 8.7 Online

| Feature | Beschreibung | Prio | Kapitel |
|---|---|---|---|
| Koop | Bis 4 Spieler in einer Welt (Host-Welt) | S | K60 |
| Tausch | Direkt, Gilden-Börse (kein Echtgeld) | M | K60 |
| PvP Casual & Ranked | Saisons, Matchmaking, Belohnungen, Replays | M | K61 |
| Raids | Online-Raids mit Matchmaking | S | K35 |
| Gilden | Bis 50 Mitglieder, Gildenhain, Gildenaufträge | C | K60 |
| Cross-Play | Alle Plattformen | S | K59 |

### 8.8 Won't (bewusst nicht in 1.0)

| Feature | Grund | Wiedervorlage |
|---|---|---|
| Massiv-Multiplayer-Oberwelt (MMO) | Kosten, Kernerfahrung Singleplayer | Nie (Designentscheidung) |
| Housing außerhalb des Resonanzhains | Scope | Update 2 |
| Echtzeit-Kampfmodus | Widerspricht S3 | Nie |
| Mobile-Companion-App | Nachrangig | Post-Launch-Evaluierung |
| Benutzergenerierte Quests | Moderation, Scope | Post-Launch-Evaluierung |

---

## 9. Content-Umfang (Zielzahlen)

Diese Zahlen sind **LOCKED** und in `CANON.md §3` hinterlegt. Änderungen nur per Change Request.

| Kategorie | Zielwert Release 1.0 | Briefing-Minimum | Begründung |
|---|---|---|---|
| Spielbare Weltfläche | **36 km²** (32 km² Boden + 4 km² Himmelinseln-Footprint) | 25–40 km² | Mitte des Korridors; Dichte vor Größe |
| Regionen/Biome | **10** | 10 | 1 Biom = 1 Region, klare Identität |
| Städte | **10** | 10 | 1 pro Region |
| Dörfer | **22** | 20 | 2 pro Region + 2 Sonderdörfer |
| Außenposten | **30** | „Außenposten“ | 3 pro Region |
| Echos (Arten) | **256** | 250 | 2⁸ – technisch sauber, Marketing-Zahl |
| davon Legendär/Mythisch | 16 | – | 10 Ursprungsstimmen + 6 Mythische |
| Typen | **15** | 15 Beispiele | Briefing-Typen vollständig übernommen, eigene Namen (s. §9.1) |
| Fähigkeiten | **330** | 300 | 180 Aktiv / 90 Passiv / 30 Ultimate / 30 Feld |
| Hauptquests | ~32 | Hauptstory | 3 Akte |
| Nebenquests | **210** | 200 | 21 pro Region im Schnitt |
| Fraktionen | **5** | 5 | Forscher, Händler, Ranger, Rebellen, Antagonisten |
| Wetterzustände | **10** | 7 Beispiele | s. §9.2 |
| Arenen | 10 | 1 pro Stadt | – |
| Endgame-Dungeons | 8 | – | „Tiefenresonanzen“ |
| Raid-Bosse (Launch) | 6 | – | + saisonale |

### 9.1 Die 15 Typen (LOCKED – Tabelle folgt in K17)

Interne ID bleibt englisch (Code, Daten), Anzeigename lokalisiert. Deutsche Anzeigenamen:

| ID | Intern | Deutsch (Anzeige) | Kurz-Identität |
|---|---|---|---|
| T01 | Ember | Glut | Hitze, Zerstörung, Leidenschaft |
| T02 | Tide | Flut | Wasser, Strömung, Anpassung |
| T03 | Stone | Stein | Erde, Ausdauer, Schutz |
| T04 | Storm | Sturm | Wind, Blitz, Tempo |
| T05 | Bloom | Blüte | Pflanzen, Wachstum, Heilung |
| T06 | Frost | Frost | Kälte, Stillstand, Präzision |
| T07 | Void | Leere | Nichts, Entzug, Auflösung |
| T08 | Light | Licht | Strahlen, Reinheit, Enthüllung |
| T09 | Venom | Gift | Zersetzung, Zeit, Schwächung |
| T10 | Metal | Metall | Härte, Konstruktion, Klinge |
| T11 | Spirit | Geist | Seele, Erinnerung, Täuschung |
| T12 | Crystal | Kristall | Brechung, Speicherung, Verstärkung |
| T13 | Sound | Klang | Schwingung, Rhythmus, Resonanz |
| T14 | Gravity | Schwerkraft | Masse, Anziehung, Raum |
| T15 | Arcane | Arkan | Ur-Magie, Regelbruch, Muster |

*Designnotiz:* Da das Spiel thematisch auf Klang/Resonanz basiert, erhält **Klang** in der Welt eine erzählerische Sonderrolle (Weltlied), ist aber **mechanisch nicht stärker** als andere Typen. Das wird in K17 durch Tabellen-Balancing sichergestellt.

### 9.2 Die 10 Wetterzustände (LOCKED – Wirkung in K14)

| ID | Wetter | Vorkommen (Hauptregionen) |
|---|---|---|
| W01 | Klar | alle |
| W02 | Regen | Verdanthain, Morvenmoor, Saltrand |
| W03 | Gewittersturm | Kharsgrat, Saltrand, Nimbara |
| W04 | Nebel | Morvenmoor, Ael'Dorun, Saltrand |
| W05 | Schneefall | Hvitfell, Kharsgrat (Gipfel) |
| W06 | Hitzewelle | Sahrun-Weite, Ignareth |
| W07 | Sandsturm | Sahrun-Weite |
| W08 | Aurora | Hvitfell, Nimbara (selten überall nachts) |
| W09 | Aschefall | Ignareth |
| W10 | Resonanzsturm | selten, global, storygesteuert und Endgame-Event |

---

## 10. Zielgruppe & Personas

### 10.1 Zielgruppen-Segmente

| Segment | Alter | Anteil (Ziel) | Motivation | Kritische Features |
|---|---|---|---|---|
| Genre-Veteranen | 20–35 | 35 % | Sammeln, Kompetition, Zucht | Kampftiefe, Genetik, Ranked |
| Open-World-RPG-Spieler | 22–40 | 30 % | Erkundung, Story, Atmosphäre | Welt, Story, Grafik |
| Junge Einsteiger / Familien | 10–17 | 20 % | Kreaturen, Bindung, Abenteuer | Zugänglichkeit, Begleiter, Koop |
| Kreative/Soziale | 16–35 | 15 % | Fotografie, Sammeln zeigen, Gilden | Fotomodus, Morphs, Tausch |

**Altersfreigabe-Ziel:** PEGI 7 / USK 6 / ESRB E10+. Kampfdarstellung ohne Blut, Kreaturen werden „erschöpft“, nie getötet (LOCKED, siehe CANON §8).

### 10.2 Personas

| Persona | Beschreibung | Was sie will | Was sie vergrault | Design-Antwort |
|---|---|---|---|---|
| **„Mara, die Meisterin“** (28, Genre-Veteranin, 2.000 h im Genre) | Spielt kompetitiv, optimiert Teams | Tiefe, Transparenz, faire Ranked | Versteckte Formeln, RNG-Frust, P2W | Offene Schadensformeln im Kodex (ab Forschungsstufe 3), Ranked mit Level-Normalisierung |
| **„Jonas, der Entdecker“** (34, Open-World-Fan) | Spielt Story-lastig, Abends 90 min | Atmosphäre, Geheimnisse | Grind, repetitive Kämpfe | Sichtbare Begegnungen (umgehbar), Levelskalierung-Korridor, starke Nebenquests |
| **„Lina, die Neue“** (11, erstes großes RPG, spielt mit Elternteil) | Liebt Kreaturen | Kuscheln, Abenteuer, gemeinsam spielen | Zu schwere Kämpfe, Textwände | Assist-Modi, Couch-Koop (Split-Screen auf Konsole – *Should*), vertonte Hauptdialoge |
| **„Deniz, der Kurator“** (22, Social-Content-Creator) | Fotografiert, sammelt Morphs | Einzigartige Echos zeigen | Unfotogene Welt, fehlende Tools | Fotomodus, Morph-Seltenheit, Echo-Karten teilen |

---

## 11. Plattformen, Technik & Performance-Ziele

### 11.1 Plattformmatrix

| Plattform | Auflösung Ziel | FPS-Ziel | Rendering-Profil | Status |
|---|---|---|---|---|
| PC (High) | 1440p–4K (TSR/DLSS/FSR/XeSS) | 60 (unlocked bis 144) | Nanite, Lumen HW-RT, VSM | Lead-Plattform Entwicklung |
| PC (Min-Spec) | 1080p (TSR ~67 %) | 60 | Nanite, Lumen SW | – |
| PlayStation 5 / Pro | 1440p→4K (TSR / PSSR) | 60 (Performance), 30/40 (Qualität) | Nanite, Lumen SW (HW-RT auf Pro optional) | Lead-Konsole |
| Xbox Series X | 1440p→4K | 60 / 30 | wie PS5 | – |
| Xbox Series S | 1080p→1440p | 60 (reduzierte Dichte) | Lumen SW reduziert | Profil „S“ |
| Nintendo Switch 2 | Handheld 720p→1080p (DLSS), Docked 1080p→1440p | **60 Ziel**, Fallback 30 (Entscheidungs-Gate VS) | Eigenes Profil: Nanite eingeschränkt/aus, Lumen aus → Baked GI + SSGI + Light Probes | Risiko R-01 |

### 11.2 Performance-Budget (Frame @ 60 FPS = 16,67 ms, PS5-Referenz)

| Bereich | Budget (ms) | Anmerkung |
|---|---|---|
| Game Thread | 8,0 | inkl. Mass-Ökologie, KI, Gameplay |
| Render Thread | 8,0 | parallel |
| GPU | 15,5 | inkl. Lumen ~4,0, VSM ~2,5, Nanite ~3,0, Post ~1,5, Niagara ~1,5, UI 0,5 |
| Streaming-Hitch | < 1 Frame > 33 ms pro 5 min | World Partition, gemessen durch automatisierte Traversal-Bots |

Details, Plattformprofile und Scalability-Gruppen: **K65**.

### 11.3 Technische Leitentscheidungen (LOCKED)

| Bereich | Entscheidung |
|---|---|
| Engine | Unreal Engine **5.6** (Upgrade-Politik: ein Minor-Upgrade pro Jahr, Engine-Lock ab Alpha) |
| Sprache | C++ (Systeme, Performance) + Blueprints (Content, Prototyping, Anim-Logik) |
| Fähigkeiten/Effekte | **Gameplay Ability System (GAS)** für Kampffähigkeiten, Status, Buffs |
| Große Populationen | **Mass Entity (ECS)** für Herden, Schwärme, Hintergrund-NPCs |
| Einzel-KI | **StateTree** für High-Level-Zustände + **Behavior Trees/Blackboards** für taktisches Verhalten |
| Welt | World Partition, Level Instances, Data Layers, **PCG Framework** für Biome |
| Rendering | Nanite, Lumen, Virtual Shadow Maps, TSR |
| VFX / Audio | Niagara / MetaSounds + Audio Modulation, Quartz für musiksynchrone Events |
| UI | CommonUI + UMG, MVVM-Plugin (UI-Datenbindung) |
| Netzwerk | Iris-Replikation, Dedicated Server für PvP/Raids, Listen-Server für Koop |
| Modularität | **Game Features Plugins** (jede Großfunktion als Plugin, An/Aus pro Build) |
| Daten | Data Assets + Data Tables (CSV/JSON-Quelle in Git), **Primary Asset IDs** |
| Save | SaveGame-Subsystem mit versioniertem, schemagebundenem Binärformat + Cloud-Sync |

---

## 12. Engine-Entscheidung

### 12.1 Bewertungsmatrix

Gewichtung durch Game Director + Leads, Skala 1–5.

| Kriterium | Gewicht | UE 5.6 | Unity 6 | Godot 4 |
|---|---|---|---|---|
| Open-World-Streaming (36 km²) | 15 % | 5 (World Partition, HLOD) | 3 (eigene Lösung nötig) | 2 (eigene Lösung nötig) |
| Grafikqualität semi-realistisch | 15 % | 5 (Nanite, Lumen) | 4 (HDRP) | 2 |
| Fähigkeits-/Statussystem | 10 % | 5 (GAS) | 2 (Eigenbau) | 2 (Eigenbau) |
| Große Kreaturenpopulationen | 10 % | 4 (Mass Entity) | 5 (DOTS/ECS) | 2 |
| Konsolen inkl. Switch 2 | 10 % | 4 (Switch 2 braucht eigenes Profil) | 5 (sehr gute Skalierung nach unten) | 2 (Konsolenports über Drittanbieter) |
| Netzwerk (Koop, PvP, Raids) | 10 % | 4 (Replication/Iris, Dedicated Server) | 3 (Netcode for GameObjects/Entities) | 2 |
| Talentmarkt AAA | 10 % | 5 | 4 | 2 |
| Tooling/Iteration Content | 10 % | 4 | 4 | 3 |
| Lizenzkosten | 5 % | 3 (5 % Royalty über Schwelle) | 4 | 5 |
| Quellcodezugriff | 5 % | 5 | 3 (kostenpflichtig) | 5 |
| **Gewichtete Summe** | 100 % | **4,55** | **3,80** | **2,35** |

### 12.2 Vor- und Nachteile der Wahl

| | Unreal Engine 5.6 |
|---|---|
| **Vorteile** | Out-of-the-box Open-World-Stack (World Partition, HLOD, PCG); Nanite ermöglicht hochdetaillierte Natur ohne manuelle LOD-Kette auf Current-Gen; GAS deckt ~60 % unseres Kampf- und Statussystems ab; Mass Entity für Herden/Schwärme; großer AAA-Talentpool; Quellcode-Zugriff für Engine-Modifikationen (Switch-2-Profil). |
| **Nachteile** | Switch 2 benötigt eigenes Rendering-Profil (kein Lumen, eingeschränktes Nanite) → doppelte Lighting-Arbeit in Teilen; GAS hat steile Lernkurve und ist für rundenbasierte Kämpfe nicht primär ausgelegt (wir nutzen es ohne Echtzeit-Prediction, siehe K06); Engine-Upgrades sind teuer; Royalty. |
| **Mitigation** | Switch-2-Strike-Team ab Preproduction (K65); GAS-Wrapper `UEchoAbilitySystemComponent` mit rundenbasiertem Ausführungsmodell; Engine-Fork mit striktem Merge-Prozess; Engine-Lock ab Alpha. |

### 12.3 Warum nicht Unity 6? Warum nicht Godot 4?

- **Unity 6** wäre die bessere Wahl, wenn Switch 2 Lead-Plattform wäre oder das Team stark in DOTS erfahren wäre. Für ein semi-realistisches 36-km²-Open-World-Spiel müssten wir Streaming, HLOD und das Fähigkeitssystem weitgehend selbst bauen (~40–60 zusätzliche Engineer-Jahre geschätzt).
- **Godot 4** ist für ein 200-Personen-AAA-Projekt mit Konsolen-Day-One-Release derzeit nicht risikoarm genug (Konsolenports, Open-World-Streaming, Tooling im Team-Maßstab).

**Entscheidung (ADR-003): Unreal Engine 5.6. LOCKED.**

---

## 13. Architektur auf einen Blick

Detaillierte Spezifikation in **K05/K06**. Hier die verbindliche Top-Level-Struktur, damit alle folgenden Kapitel konsistente Code-Beispiele liefern.

### 13.1 Modul- und Plugin-Landkarte

```
AETHRIS (UE 5.6 Project)
│
├── Source/
│   ├── AethrisCore/            ← Basistypen, Event-Bus, Logging, IDs, Utilities
│   ├── AethrisGame/            ← GameMode, GameInstance, PlayerController, Subsystems
│   └── AethrisEditor/          ← Editor-Tools, Validatoren, Importer (nur Editor)
│
└── Plugins/GameFeatures/       ← Jede Großfunktion als eigenständiges Plugin
    ├── GF_Monsters/            ← Echo-Datenmodell, Spezies, Genetik-Kern, Evolution
    ├── GF_Combat/              ← Zeitleiste, GAS-Integration, Schadensmodell
    ├── GF_Capture/             ← Resonanzbindung, Siegel, Fallen
    ├── GF_Companion/           ← Begleiter, Resonanzhain
    ├── GF_Breeding/            ← Zucht, Mutationen
    ├── GF_World/               ← Wetter, Tageszeit, Regionen, Spawns
    ├── GF_AI/                  ← Ökologie (Mass), NPC-Tagesabläufe, StateTrees
    ├── GF_Inventory/           ← Items, Ausrüstung, Crafting
    ├── GF_Economy/             ← Händler, Preise, Nachfrage
    ├── GF_Quests/              ← Questsystem, Dialog, Fraktionen
    ├── GF_Research/            ← Echo-Kodex, Fotografie
    ├── GF_UI/                  ← CommonUI-Screens, ViewModels
    ├── GF_Audio/               ← Adaptive Musik, Ambient-Systeme
    ├── GF_Save/                ← Save-Schema, Migration, Cloud
    ├── GF_Multiplayer/         ← Sessions, Koop, Tausch, Gilden
    └── GF_PvP/                 ← Ranked, Matchmaking-Client, Replays
```

### 13.2 Schichtenmodell (Abhängigkeitsregel)

```
 ┌───────────────────────────────────────────────────────┐
 │  PRÄSENTATION   GF_UI · GF_Audio · VFX · Kamera       │  darf alles LESEN (über ViewModels/Events)
 ├───────────────────────────────────────────────────────┤
 │  FEATURES       Combat · Capture · Companion · Quests │  darf Domain + Core nutzen,
 │                 Breeding · Research · Economy · PvP   │  NIE andere Features direkt → nur Events/Interfaces
 ├───────────────────────────────────────────────────────┤
 │  DOMAIN         GF_Monsters · GF_World · GF_Inventory │  reine Datenmodelle + Regeln, testbar ohne Welt
 ├───────────────────────────────────────────────────────┤
 │  CORE           AethrisCore (Event-Bus, IDs, RNG,     │  keine Abhängigkeiten nach oben
 │                 Save-Interfaces, Logging)             │
 └───────────────────────────────────────────────────────┘
```

**Regel (LOCKED):** Feature-Plugins kommunizieren untereinander ausschließlich über den **Aethris Event-Bus** (Gameplay Message Subsystem-basiert) oder über in `AethrisCore` definierte Interfaces. Direkte Include-Abhängigkeiten zwischen Feature-Plugins sind verboten und werden per Build-Validator geprüft.

### 13.3 Kerndatenmodell (Vorschau, verbindliche Namen)

```cpp
// AethrisCore – Vorschau. Vollständige Definition in K06/K16.
// Namenskonvention: Laufzeit-Instanzen = F...Instance / U...Component,
// statische Designdaten = U...Definition (UPrimaryDataAsset).

/** Statische Spezies-Definition (eine pro Echo-Art, 256 im Grundspiel). */
UCLASS(BlueprintType)
class AETHRISCORE_API UEchoSpeciesDefinition : public UPrimaryDataAsset
{
    GENERATED_BODY()
public:
    /** Stabile, nie wiederverwendete ID, z. B. "ECHO_001". */
    UPROPERTY(EditDefaultsOnly, Category="Identity")
    FName SpeciesId;

    /** Kodex-Nummer 1..256 (Grundspiel), Updates ab 257. */
    UPROPERTY(EditDefaultsOnly, Category="Identity", meta=(ClampMin=1))
    int32 KodexNumber = 1;

    /** Primär- und optionaler Sekundärtyp (GameplayTag: Type.Ember etc.). */
    UPROPERTY(EditDefaultsOnly, Category="Typing")
    FGameplayTag PrimaryType;

    UPROPERTY(EditDefaultsOnly, Category="Typing")
    FGameplayTag SecondaryType;

    /** Basiswerte der 8 Statuswerte (Details K18). */
    UPROPERTY(EditDefaultsOnly, Category="Stats")
    FEchoBaseStats BaseStats;

    // ... Lore, Evolution, Lernsets, Genetik-Profil, Assets → K16
};

/** Laufzeitinstanz eines konkreten Echos (gespeichert, tauschbar). */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoInstance
{
    GENERATED_BODY()

    /** Global eindeutige ID – bleibt über Tausch/Cloud hinweg stabil. */
    UPROPERTY(SaveGame) FGuid InstanceId;

    UPROPERTY(SaveGame) FPrimaryAssetId Species;   // → UEchoSpeciesDefinition
    UPROPERTY(SaveGame) int32 Level = 1;           // 1..100
    UPROPERTY(SaveGame) int32 Bond = 0;            // 0..1000 (Bindungswert)
    UPROPERTY(SaveGame) FEchoGenome Genome;        // Allele, Morph, Mutationen (K38)
    // ... Persönlichkeit, Temperament, Fähigkeiten, Herkunftssignatur → K16/K18
};
```

---

## 14. Geschäftsmodell & Monetarisierung

### 14.1 Modell (LOCKED)

| Element | Entscheidung |
|---|---|
| Grundspiel | Premium, Vollpreis (Standard 69,99 € / Switch 2 69,99 €) |
| Editionen | Standard, Deluxe (+ Artbook, OST, kosmetisches Wärter-Set, Expansion-Pass) |
| Erweiterungen | 2 Story-Erweiterungen (je neue Region + 30–40 Echos) im Expansion-Pass |
| Kostenlose Updates | Saisons, Events, Balancing, neue Raids, QoL |
| Kosmetik-Shop | Nur Wärter-Kleidung, Gleiter-Skins, Hain-Deko. **Keine** Echo-Morphs, keine Siegel, keine Werte. Kein Zufall (keine Lootboxen). |
| Ranked-Belohnungen | Ausschließlich erspielbar, kostenlos |
| Online-Pflicht | Nein (außer für Online-Features, plattformübliches Abo für PvP/Koop) |

### 14.2 Begründung & Abwägung

| Option | Vorteile | Nachteile | Entscheidung |
|---|---|---|---|
| Premium + Expansions + Kosmetik | Vertrauen der Kernzielgruppe, vollständiges Produkt, familienfreundlich (Altersfreigabe, Eltern) | Geringerer Langzeit-Umsatz als F2P | ✅ gewählt |
| Free-to-Play mit Gacha | Hoher Umsatzdeckel | Widerspricht S2/S4 („Bindung/Einzigartigkeit“ darf nicht käuflich sein), regulatorisches Risiko (Lootbox-Gesetze), Zielgruppe < 18 | ❌ |
| Premium + Battle Pass | Planbarer Live-Umsatz | FOMO-Druck, schwächt Ranked-Fairness-Image | ❌ (Saisons ja, bezahlter Pass nein) |

---

## 15. Team & Organisation

### 15.1 Teamgröße im Peak (Phase 4): ~210 intern + Outsourcing

| Abteilung | Rollen (Auswahl) | Köpfe (Peak) |
|---|---|---|
| Leitung | Game Director, Creative Director, Executive Producer, Tech Director, Art Director, Audio Director | 8 |
| Produktion | Producer, Associate Producer, Projektmanager | 14 |
| Game Design | Combat, RPG Systems, Economy, Level (8), Quest (8), Kreaturen-Design (4) | 32 |
| Narrative | Lead Writer, Writer (6), Narrative Designer (3), Lokalisierungs-Koordination | 11 |
| Engineering | Gameplay (18), AI (7), Engine/Rendering (8), Tools (7), Netzwerk/Online (8), Plattform (5), Build/DevOps (3) | 56 |
| Art | Konzept (8), Kreaturen-3D (12), Environment (14), Character (5), Tech Art (7), Lighting (4) | 50 |
| Animation | Kreatur-Animation (10), Character/Cinematic (5), Rigging (3) | 18 |
| VFX | Niagara-Artists | 6 |
| Audio | Komposition (2), Sound Design (5), Implementierung (2) | 9 |
| UI/UX | UX Research, UI Design, UI Engineering | 10 |
| QA (intern) | QA Lead, Testautomation (4), Embedded QA (10) | 15 |
| **Summe intern** | | **~229 Plätze, ~210 gleichzeitig besetzt** |
| Extern | Outsourcing (Environment-Props, Kreatur-LODs, Mocap), externe QA (60 im Peak), Lokalisierung (12 Sprachen) | variabel |

### 15.2 Organisationsmodell: „Pods“

Das Studio arbeitet in **cross-funktionalen Pods** (6–15 Personen), die je ein Feature-Plugin besitzen. Das verhindert Silos und spiegelt die Game-Features-Architektur (§13) organisatorisch.

```
                        ┌─────────────────────┐
                        │  Game Director /    │
                        │  Leadership Council │
                        └──────────┬──────────┘
        ┌──────────────┬───────────┼────────────┬──────────────┐
   ┌────▼────┐   ┌─────▼────┐ ┌────▼─────┐ ┌────▼────┐  ┌──────▼─────┐
   │ Pod     │   │ Pod      │ │ Pod      │ │ Pod     │  │ Pod        │
   │ COMBAT  │   │ ECHOS    │ │ WORLD    │ │ STORY & │  │ ONLINE     │
   │(GF_Com- │   │(Monsters,│ │(World,AI,│ │ QUESTS  │  │(Multiplay.,│
   │ bat)    │   │ Capture, │ │ Weather) │ │         │  │ PvP)       │
   └─────────┘   │ Breeding)│ └──────────┘ └─────────┘  └────────────┘
                 └──────────┘
   + Shared Services: Engine/Rendering · Tools · Build · Tech Art · Audio · UI · QA
```

### 15.3 Rollen des Briefing-Teams und ihre Kapitel-Ownership

| Rolle | Primäre Kapitel |
|---|---|
| Game Director | K01–K03, K62, K67, K68 |
| Creative Director | K04, K07, K16, K56 |
| Lead Gameplay Programmer | K06, K31, K36, K64 |
| AI Engineer | K34, K52, K53 |
| Unreal Senior Developer | K05, K65 |
| Combat Designer | K17, K28–K33, K35 |
| RPG Systems Designer | K18, K19, K37–K39, K43 |
| Economy Designer | K41, K42, K63 |
| Level Designer | K08–K13 |
| Quest Designer | K48–K51 |
| Narrative Writer | K44–K47 |
| UI/UX Designer | K54 |
| Sound Designer | K55 |
| Technical Artist | K14, K15, K57, K58 |
| Network Engineer | K59–K61 |
| QA Lead | K66 + Review-Gate aller Kapitel |

---

## 16. Zeitplan & Budget

### 16.1 Phasenplan (PROVISIONAL – Detail in K67)

Projektstart: **Oktober 2026**. Ziel-Release: **November 2030** (Weihnachtsgeschäft).

```
2026        2027              2028              2029              2030
 Q4 │ Q1  Q2  Q3  Q4 │ Q1  Q2  Q3  Q4 │ Q1  Q2  Q3  Q4 │ Q1  Q2  Q3  Q4
 ███████████████                                                        P1 Preproduction   (Okt 26 – Jun 27)
                ████████████                                            P2 Vertical Slice  (Jul 27 – Mär 28)
                            ████████████████                            P3 Core Systems    (Apr 28 – Mär 29)
                                            ██████████████              P4 Content         (Apr 29 – Feb 30)
                                                          ██████        P5 Polishing       (Mär 30 – Aug 30)
                                                                ████    P6 Release         (Sep 30 – Nov 30)
 Meilensteine:  ▲ Greenlight   ▲ VS-Review    ▲ Alpha (Feature Complete) ▲ Beta ▲ Gold ▲ Launch
               Jun 27         Mär 28         Feb 30                     Jun 30  Sep 30 Nov 30
```

### 16.2 Phasenziele (Kurzfassung)

| Phase | Ziel | Exit-Kriterium |
|---|---|---|
| P1 Preproduction | Kapitel K01–K19 finalisiert, Prototypen: Kampf-Zeitleiste, Resonanzbindung, Ökologie-Herde, Switch-2-Rendering-Test | Greenlight-Review bestanden |
| P2 Vertical Slice | Verdanthain-Teilgebiet (~3 km²), Eichenhall, 16 Echos, 1 Arena, 5 Quests, Koop-Prototyp, Ziel-Grafikqualität | VS spielbar in 60 FPS auf PS5, 30+ auf Switch 2 → Entscheidung Switch-2-Profil |
| P3 Core Systems | Alle Systeme funktional (Features „Must“), Pipelines skaliert | Alle Must-Features in Pre-Alpha-Qualität |
| P4 Content | 256 Echos, 10 Regionen, alle Quests | Alpha: Content Complete |
| P5 Polishing | Bugfixing, Balancing, Performance, Zertifizierung | Beta → Gold Master |
| P6 Release | Launch, Day-One-Patch, Live-Betrieb | Launch + 30 Tage stabil |

### 16.3 Budgetrahmen (PROVISIONAL)

| Posten | Schätzung (Mio. €) | Annahme |
|---|---|---|
| Interne Personalkosten | 118 | Ø 140 FTE über 50 Monate × 16,8 k€/Monat voll belastet (Peak 210) |
| Outsourcing Art/Anim | 22 | Props, LODs, Mocap, Cinematics-Support |
| Externe QA & Zertifizierung | 7 | Peak 60 Tester |
| Lokalisierung (12 Sprachen) + Vertonung (DE/EN/JA/FR/ES) | 9 | ~600.000 Wörter |
| Musik (Orchester, Aufnahmen) | 2,5 | Hybrides Orchester + Solisten |
| Online-Infrastruktur (bis Launch + 1 Jahr) | 6 | Dedicated Server, Backend, Anti-Cheat |
| Engine-Royalty | umsatzabhängig | nicht im Entwicklungsbudget |
| Contingency (15 %) | 24,8 | – |
| **Entwicklung gesamt** | **~189** | |
| Marketing & UA | ~70 | separat, Publisher |

---

## 17. Risiko-Register

Bewertung: Wahrscheinlichkeit (W) und Auswirkung (A) je 1–5, Score = W × A. Risiken ≥ 12 werden monatlich im Leadership Council überprüft.

| ID | Risiko | W | A | Score | Mitigation | Owner | Trigger/Gate |
|---|---|---|---|---|---|---|---|
| R-01 | Switch 2 erreicht keine 60 FPS in der Open World | 4 | 4 | **16** | Eigenes Rendering-Profil, frühes Strike-Team, Entscheidungs-Gate im VS (Fallback 30 FPS stabil) | Unreal Senior Dev | VS-Review Mär 28 |
| R-02 | Rechtliche Nähe zu bestehendem Franchise | 3 | 5 | **15** | Clean-Room-Policy (§4.3), Legal-Review pro Content-Batch, Silhouetten-DB | Creative Director | jedes Kreaturen-Batch |
| R-03 | Content-Volumen 256 Echos × 9 Anim-States × LODs überfordert Pipeline | 4 | 4 | **16** | Modulare Rigs (Körperbaupläne/„Archetypen“), Anim-Retargeting, Outsourcing ab P3, Kreaturen-Kits | Technical Artist | Throughput-Messung P2 |
| R-04 | GAS eignet sich schlecht für rundenbasiertes Modell | 2 | 4 | 8 | Prototyp P1, Wrapper-Architektur, Fallback eigenes Effektsystem auf GAS-Attributen | Lead Gameplay Programmer | Prototyp-Review Feb 27 |
| R-05 | Balancing von 256 Echos × 330 Fähigkeiten × 15 Typen | 4 | 3 | 12 | Balancing-Simulator (headless Kampfsimulation, Monte-Carlo), K63 | RPG Systems Designer | ab P3 wöchentlich |
| R-06 | Mass-Ökologie zu teuer für Game Thread | 3 | 4 | 12 | LOD für KI (Significance Manager), Zeit-Slicing, Budget 1,5 ms | AI Engineer | P2 Profiling |
| R-07 | Koop-Oberwelt Desync (Wetter, Spawns) | 3 | 3 | 9 | Server-autoritative Welt-Seeds, deterministische Spawn-Tabellen | Network Engineer | P3 |
| R-08 | Feature Creep | 4 | 4 | **16** | Säulen-Check, MoSCoW, Change-Request-Prozess (CANON) | Game Director | jeder Sprint |
| R-09 | Engine-Upgrade bricht Systeme | 2 | 3 | 6 | 1 Upgrade/Jahr, Engine-Lock ab Alpha, automatisierte Tests | Tech Director | – |
| R-10 | Cheating/Hacking in Ranked & Tausch | 4 | 4 | **16** | Server-autoritative Kämpfe, signierte Echo-Instanzen (Herkunftssignatur), Legalitätsprüfung | Network Engineer | P3 |
| R-11 | Schlüsselpersonal-Verlust | 2 | 4 | 8 | Dokumentation (dieses Kapitelsystem), Pairing, Bus-Factor ≥ 2 pro System | Producer | – |
| R-12 | Lokalisierung von 600k Wörtern verzögert Release | 3 | 3 | 9 | Loc-Freeze vor Beta, String-Tooling, Kontext-Screenshots automatisiert | Narrative Lead | Beta |

---

## 18. Erfolgskriterien & KPIs

### 18.1 Business-KPIs (Ziel 12 Monate nach Launch)

| KPI | Ziel | Stretch |
|---|---|---|
| Verkaufte Einheiten | 4,5 Mio. | 7 Mio. |
| Metacritic/OpenCritic | ≥ 85 | ≥ 90 |
| Expansion-Pass-Attach-Rate | 25 % | 35 % |
| Nutzer-Review-Score (Steam) | „Sehr positiv“ (≥ 85 %) | „Äußerst positiv“ |

### 18.2 Engagement-KPIs

| KPI | Ziel | Messmethode |
|---|---|---|
| Story-Abschlussrate | ≥ 45 % | Telemetrie (Opt-in) |
| D30-Retention | ≥ 30 % | Telemetrie |
| Ø gefangene Arten nach 20 h | 60–80 | Telemetrie |
| Anteil Spieler mit ≥ 1 Online-Feature in 30 Tagen | ≥ 35 % | Backend |
| Ranked-Teilnahme (Spieler mit Storyabschluss) | ≥ 20 % | Backend |
| Fotomodus-Nutzung | ≥ 50 % mind. 1 Foto | Telemetrie |

### 18.3 Qualitäts-KPIs (Release-Gate)

| KPI | Grenzwert |
|---|---|
| Crash-Rate | < 0,1 % der Sessions |
| A-Bugs (Blocker/Kritisch) | 0 offen |
| FPS-Einhaltung Referenzrouten | ≥ 95 % der Frames im Ziel pro Plattform |
| Save-Korruption | 0 bekannte reproduzierbare Fälle |
| Ladezeit Kaltstart → Spielbar | PS5/XSX < 15 s, Switch 2 < 25 s |

---

## 19. Architecture/Design Decision Records

Jede grundlegende Entscheidung wird als ADR festgehalten (Format: Kontext → Optionen → Entscheidung → Konsequenzen). Die ADRs sind in `CANON.md §9` indexiert.

### ADR-001 – Titel und Welt-Branding
- **Kontext:** Repository und Projekt heißen *AETHRIS: Echobound*. Ein Arbeitstitel ändert sich häufig; Marken-Recherche kostet Zeit.
- **Optionen:** (a) Arbeitstitel beibehalten, (b) neuer Titel nach Preproduction.
- **Entscheidung:** (a). „Aethris“ = Kontinent und Kosmos, „Echobound“ = das zentrale Verb (an Echos gebunden sein). Markenprüfung bis Greenlight.
- **Konsequenz:** Oberbegriff für Kreaturen ist **Echo** (Plural: **Echos**). Der Spielercharakter ist ein **Wärter**.

### ADR-002 – Säulen-Priorität
- Siehe §3. **S2 > S3 > S1 > S4 > S5.**

### ADR-003 – Engine
- Siehe §12. **Unreal Engine 5.6.**

### ADR-004 – Kapitelreihenfolge mit frühem TDD
- Siehe `00_KAPITELPLAN.md`. Technisches Fundament als K05/K06, damit alle Code-Beispiele konsistent sind.

### ADR-005 – Zeitleisten-Kampf statt simultaner Runden
- **Kontext:** Genre-Standard ist simultane Rundeneingabe mit Speed-Sortierung. Das Briefing verlangt Initiative, Priorität, Combos, Positionierung.
- **Optionen:**
  | Option | Vorteile | Nachteile |
  |---|---|---|
  | (a) Simultane Runde | Vertraut, schnell im PvP | Initiative/Combos schwer lesbar, wenig eigene Identität |
  | (b) Resonanz-Zeitleiste (Conditional Turn-Based) | Initiative sichtbar, Zeitkosten pro Aktion ermöglichen „schnelle schwache vs. langsame starke“ Züge, Combos natürlich darstellbar | PvP-Tempo langsamer → Lösung: Zugtimer + gleichzeitige Planung bei gleichem Tick |
  | (c) ATB in Echtzeit | Dynamisch | Widerspricht S3 (denkender Kampf), Zugänglichkeit |
- **Entscheidung:** (b). Details K31.

### ADR-006 – Fangen ohne Wurfgegenstand-Metapher
- **Kontext:** Briefing verlangt Timing, Fallen, Resonanz, Beruhigung, Lockmittel – ausdrücklich keine Kopie von Wurfkugeln.
- **Entscheidung:** **Resonanzbindung** mit dem **Resonator** (Werkzeug, dauerhaft) und **Siegeln** (Verbrauchsgut, das die Bindung „verankert“). Siegel werden nicht geworfen, sondern im Timing-Moment am Resonator *angeschlagen*. **Fallen** sind platzierbare Weltobjekte, die Echos festhalten/beruhigen. Bindung ist sowohl in der Oberwelt (ohne Kampf, bei hohem Geschick) als auch nach Kampf-Erschöpfung möglich. Details K36.

### ADR-007 – Kreaturen werden nie getötet
- **Entscheidung:** Kampfniederlage = **Erschöpfung** („verklungen“). Keine Darstellung von Tod von Echos durch Spieler. Erzählerisch dürfen Stillezonen Echos „verstummen“ lassen (Kernkonflikt), dargestellt als Erstarren/Verblassen, altersgerecht. **LOCKED.**

### ADR-008 – Level-Obergrenzen
- **Entscheidung:** Echos Level **1–100**. Spieler-Wärterrang **1–40** (Skillpunkte, K43). Wilde Echos skalieren innerhalb eines regionalen Korridors (K08/K63).

### ADR-009 – Teamgröße des Spielers
- **Entscheidung:** Der aktive Trupp heißt **Chor** und umfasst **6 Echos**. Kampfformate setzen davon 1/2/3 gleichzeitig aktiv ein; der Rest ist Reserve (Wechsel kostet Zeitleisten-Zeit). Nicht mitgeführte Echos leben im **Resonanzhain**.

---

## 20. Offene Fragen für Folgekapitel

| # | Frage | Wird beantwortet in |
|---|---|---|
| Q1 | Genaue Zugzeit-Formel und Tick-Größe der Zeitleiste | K31 |
| Q2 | Effektivitätsmultiplikatoren (z. B. 2,0 / 0,5 / 0 oder 1,6 / 0,625) | K17 |
| Q3 | Anzahl Allele pro Genom und Morph-Wahrscheinlichkeiten | K38 |
| Q4 | Koop: teilen Mitspieler Story-Fortschritt? | K60 |
| Q5 | Ranked: Level-Normalisierung auf 50 oder 100? | K61 |
| Q6 | Split-Screen-Couch-Koop auf Konsole (Should) – Performance-Machbarkeit | K65 |
| Q7 | Anzahl und Namen der 10 Ursprungsstimmen (Legendäre) | K07, K27 |
| Q8 | Genaue Stufen des Bindungswerts (0–1000) | K37 |

---

## 21. Kapitel-Checkliste

### Abgeschlossene Systeme / Entscheidungen in K01

- [x] High Concept, Pitch (1/3 Sätze), Vision Statement
- [x] Fünf Design-Säulen inkl. Messkriterien und Prioritätsregel (ADR-002)
- [x] Genre-Positionierung, Differenzierungsmatrix, Clean-Room-Policy (LOCKED)
- [x] Weltprämisse: Aethris, Weltlied, Große Stille, Echos, Wärter, Stillezonen, Orden der Stille
- [x] 10 Regionen mit Biom, Hauptstadt und Akt-Zuordnung (LOCKED)
- [x] Spielerfantasie & Fantasie-Bausteine
- [x] Core Loops (Moment, Session, Meta) + Spielzeit-Ziele
- [x] Feature-Übersicht mit MoSCoW-Priorisierung und Kapitelzuordnung
- [x] Content-Zielzahlen (36 km², 10/22/30 Siedlungen, 256 Echos, 15 Typen, 330 Fähigkeiten, 210 Nebenquests, 5 Fraktionen, 10 Wetterzustände)
- [x] 15 Typen mit interner ID und deutschem Anzeigenamen (LOCKED)
- [x] 10 Wetterzustände (LOCKED)
- [x] Zielgruppe, Personas, Altersfreigabe-Ziel
- [x] Plattformmatrix, Performance-Budget, technische Leitentscheidungen
- [x] Engine-Entscheidung mit gewichteter Bewertungsmatrix (UE 5.6)
- [x] Top-Level-Architektur: Module, Game-Feature-Plugins, Schichtenregel, Kerndatenmodell-Namen
- [x] Geschäftsmodell (Premium, keine Lootboxen, kein P2W)
- [x] Teamstruktur (~210 Peak), Pod-Organisation, Kapitel-Ownership
- [x] Phasenplan (Okt 2026 – Nov 2030) und Budgetrahmen (~189 Mio. €)
- [x] Risiko-Register (12 Risiken) und KPIs
- [x] ADR-001 bis ADR-009
- [x] `CANON.md` angelegt, alle LOCKED-Entscheidungen eingetragen
- [x] `00_KAPITELPLAN.md` mit 68 Kapiteln angelegt

### Übergabe an K02

K02 (**GDD I – Design-Säulen, Spielerfantasie, Core Loops**) vertieft die Säulen zu konkreten Design-Regeln pro System, beschreibt die ersten 3 Spielstunden Minute für Minute (Onboarding-Flow), definiert das Moment-to-Moment-Gefühl von Erkundung, Bindung und Kampf und legt die Gesamt-Progressionskurve des Spielers fest.

➡️ **Schreibe „Weiter“, um mit Kapitel 02 zu beginnen.**
