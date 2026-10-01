# K42 · Wirtschaft – Sol, Händler, Preise, Quellen und Senken

| Feld | Wert |
|---|---|
| Dokument | Kapitel 42 von 68 · Systeme, Teil VII |
| Version | 1.0 |
| Owner | Economy Designer |
| Mitwirkende | Lead Systems Designer, Narrative (Händlerfiguren), Online-Designer (Tausch, Anti-Exploit), Balancing Analyst, UX Lead (Läden) |
| Baut auf | CANON §6 (Sol ◎), §8 (kein Pay-to-Win), §16 (Meister-Strafe), §59 (Aufträge, RewardScale), Merchants (`Merchants.csv`, 54), K36–K41 (Siegel, Hain-Ausbau, Tutoren, Ausrüstung, Rezepte) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Economy/ItemPrices.csv` (333 Preise), `tools/ref/aethris_economy.py` (Wertmodell, Einnahmen/Ausgaben-Simulation), `tools/gen_items.py` (Preis-Validierung) |
| Neue Kanon-Einträge | CANON §160 (Sol & Grundregeln), §161 (Preismodell), §162 (Quellen & Senken), §163 (Händler & Sortimente) |

---

## Inhalt

1. [Rolle der Wirtschaft](#1-rolle-der-wirtschaft)
2. [Sol – die Währung](#2-sol--die-währung)
3. [Das Preismodell](#3-das-preismodell)
4. [Quellen](#4-quellen)
5. [Senken](#5-senken)
6. [Bilanz über die Spielzeit](#6-bilanz-über-die-spielzeit)
7. [Händler und Sortimente](#7-händler-und-sortimente)
8. [Preisschwankungen und Ereignisse](#8-preisschwankungen-und-ereignisse)
9. [Fraktionsrabatte und Ruf](#9-fraktionsrabatte-und-ruf)
10. [Tausch und Anti-Exploit](#10-tausch-und-anti-exploit)
11. [Code](#11-code)
12. [Tests und Telemetrie](#12-tests-und-telemetrie)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Rolle der Wirtschaft

Die Wirtschaft in AETHRIS ist ein **Entscheidungsraum**, kein Grind: Geld soll dem Spieler regelmäßig die angenehme Frage stellen „Was ist mir jetzt wichtiger?“ (Meistersiegel für das seltene Echo? Gleiter IV? Hain-Ausbau?), ohne je Fortschritt zu blockieren.

| Ziel | Messgröße |
|---|---|
| Keine Blockade | Story, Arenen und Bindung sind ohne gezieltes Geldsammeln spielbar |
| Entscheidungen | kumulierte Einnahmen/Bedarf 105–140 % in jedem Akt (§6) |
| Keine Inflation | Endgame-Senken (Hain V, Erbklang, Tutoren, Kosmetik) binden den Überschuss |
| Fair | kein Echtgeld-Kauf von Sol, Echos, Werten, Siegeln, Morphs (CANON §8) |
| Lesbar | jeder Preis ist aus dem Wert ableitbar und im Laden erklärt („Rezeptwert“) |

---

## 2. Sol – die Währung

| Regel | Wert |
|---|---|
| Name | **Sol**, Symbol ◎, Singular = Plural (CANON §6) |
| Startkapital | 1.000 ◎ (Prolog, von Ysolde) |
| Obergrenze | 9.999.999 ◎ |
| Verlust | nur Meister-Grad: Rückklang −10 % (max. 5.000 ◎, CANON §16) |
| Diegese | Sol sind dorunische Klangmünzen; das Goldklang-Kontor (F02) prägt sie seit 610 n.St. |
| Echtgeld | nein – Sol ist nicht käuflich (CANON §8) |

---

## 3. Das Preismodell

```
Wert (Ressource)      = Basis(Stufe) × Seltenheit       Basis I–V: 12 / 25 / 45 / 80 / 140 ◎;  Seltenheit ×1,0 / 1,5 / 2,5
Wert (Echo-Material)  = 30 ◎ (Klangsplitter), 60 ◎ (übrige), 250 ◎ (Stillstein-Splitter)
Wert (hergestellt)    = Σ Zutatenwerte × 1,25             (Fixpunkt über Rezeptketten)
Kaufpreis             = Wert, auf 5 ◎ gerundet            (Händler; Rabatte §9)
Verkaufspreis         = 35 % des Werts                    (Senke: Kauf-Verkauf-Kreisläufe verlieren 65 %)
Feste Preise          = Siegel 150 / 450 / 1.200 ◎ (K36)
```

**Beispiele** (aus `ItemPrices.csv`):

| Gegenstand | Wert | Kauf | Verkauf | Händler |
|---|---|---|---|---|
| Eichenholz | 12 | 15 | 4 | Material |
| Kharseisen | 25 | 25 | 8 | Material |
| Sonnenglas | 67 | 70 | 23 | Material |
| Gletscherquarz | 120 | 120 | 42 | Material |
| Sternmetall | 350 | 350 | 122 | Material |
| Klangsplitter (Glut) | 30 | 30 | 10 | Material |
| Datteln | 40 | 40 | 14 | Food |
| Sternenglocke | 180 | 180 | 63 | General |
| Klangsiegel | 150 | 150 | 52 | General |
| Gestimmtes Siegel | 450 | 450 | 157 | General |
| Meistersiegel | 1.200 | 1.200 | 420 | General |
| Ruhenest | 160 | 160 | 56 | General |
| Heilkraut-Tinktur | 45 | 45 | 15 | Heal |
| Quellwasser-Elixier | 575 | 575 | 201 | Heal |
| Weckklang | 302 | 305 | 105 | Heal |
| Wandelklang | 262 | 265 | 91 | General |
| Chorfestmahl | 690 | 690 | 241 | Food |
| Gleiter II | 437 | 440 | 152 | Gear |
| Gleiter III | 1.682 | 1.685 | 588 | Gear |
| Resonator III | 1.287 | 1.290 | 450 | Gear |
| Wärterwerkzeug IV | 3.525 | – | 1.233 | – |
| Kodex-Linse V | 7.962 | – | 2.786 | – |
| Stimmstein (Glut) | 285 | 285 | 99 | Rare |
| Taktring | 486 | 490 | 170 | Rare |
| Obertonkristall (Glut) | 355 | 355 | 124 | Rare |
| Erbklang | 1.012 | 1.015 | 354 | Faction |

**Nicht käuflich:** Klangschriften (CANON §18), Stimm- und Sternensiegel, Wesensklang, Klangstimmung, Stillstein-Splitter, Ausrüstung Stufe IV–V (nur Herstellung in Meisterwerkstätten – Reise und Material sind Teil des Erlebnisses).

---

## 4. Quellen

| Quelle | Formel / Wert | Anmerkung |
|---|---|---|
| Wärterkämpfe | Ass-Level × 25 × Klasse (Anfänger 0,8 · Geübt 1,0 · Veteran 1,5 · Arenameister 3,0) | Wildkämpfe geben **kein** Sol (Echos tragen kein Geld) |
| Aufträge | Basis-Sol (70–240) × RewardScale | RewardScale(L) = (L + 10) / 20 (1,0 bei Zonenband 10, K13) |
| Kisten/Funde | 60 × RewardScale je Kiste | Pfad-Tore, Ruinen, Begleiter-Funde |
| Verkauf | 35 % des Werts | Überschuss an Ressourcen |
| Arenen | Akt I 2.000 · Akt II 5.000 · Akt III 12.000 ◎ je Akkord | plus Klangschrift |
| Nebenquests | 300–3.000 ◎ (Akt-abhängig, K49–K51) | |
| Hain-Ertrag | Ressourcen (indirekt) | DR-31 |
| PvP/Raids | keine Sol-Belohnung (K61/K62: Kosmetik, Titel, Materialien) | verhindert Farm-Druck auf Online-Modi |

| RewardScale | Lv. 10 | Lv. 30 | Lv. 50 | Lv. 70 | Lv. 90 |
|---|---|---|---|---|---|
| Faktor | 1,0 | 2,0 | 3,0 | 4,0 | 5,0 |

---

## 5. Senken

| Senke | Kosten | Art |
|---|---|---|
| Siegel | 150 / 450 / 1.200 ◎ | wiederkehrend (Bindung) |
| Heil- und Verbrauchsgüter | 45–600 ◎ | wiederkehrend (optional, Klangbrunnen heilen gratis) |
| Material-Zukauf für Ausrüstung | ~50 % der Rezeptwerte | je Stufe |
| Tutoren | 2.000 / 3.500 ◎ (+ Ruf 3/4) | einmalig je Fähigkeit (30) |
| Hain-Ausbau | 2.000 / 6.000 / 15.000 / 30.000 ◎ je Garten (Stufe 2–5) | langfristig (530.000 ◎ gesamt) |
| Rezeptbücher | 300–800 ◎ | einmalig |
| Klangbad (Schliff-Reset) | 1.500 ◎ (Thermen Seraphe) | optional |
| Kosmetik | Farbstoffe, Ausrüstungs-Verzierungen, Hain-Dekor: 200–5.000 ◎ | optional, Endgame-Senke |
| Gasthaus | 50 ◎ je Übernachtung (Zeit vorspulen, Stimmung +15) | Komfort |
| Rückklang (Meister) | −10 % (max. 5.000 ◎) | Strafe nur im Meister-Grad |

---

## 6. Bilanz über die Spielzeit

Die Simulation (`aethris_economy.py`) rechnet typische Spielsitzungen je Abschnitt: 3 Wärterkämpfe/h, 1,5 Aufträge/h, 4 Kisten/h, Verkauf von Überschuss, Arenen und Nebenquests nach Akt.

**Einnahmen:**

| Abschnitt | Spielzeit | Wärterkämpfe | Aufträge | Kisten | Verkauf | Arenen/Quests | **Summe** | je Stunde |
|---|---|---|---|---|---|---|---|---|
| Prolog | 3 h | 300 | 0 | 378 | 150 | 800 | **1.628** | 542 |
| Akt I | 15 h | 19.125 | 4.556 | 4.860 | 3.750 | 17.000 | **49.291** | 3.286 |
| Akt II | 20 h | 60.000 | 11.250 | 12.000 | 10.000 | 42.000 | **135.250** | 6.762 |
| Akt III | 12 h | 54.000 | 9.450 | 10.080 | 9.600 | 44.000 | **127.130** | 10.594 |
| Endgame (je 10 h) | 10 h | 63.750 | 14.250 | 8.550 | 12.000 | 15.000 | **113.550** | 11.355 |

**Typischer Bedarf:**

| Abschnitt | Typische Ausgaben | Bedarf (◎) |
|---|---|---|
| Prolog | Siegel. Tinkturen | 1.950 |
| Akt I | 25 Bindungen × 1.6 Siegel (Klang/Gestimmt). Ausrüstung II–III (Material-Zukauf 50 %). Heilmittel. Rezeptbücher ×6. Gerichte. Hain-Ausbau 2 (×4) | 35.692 |
| Akt II | 40 Bindungen (Gestimmt/Meister). Ausrüstung IV (Material 50 %). Tutoren ×4. Hain 3 (×5). Stimmsteine | 109.972 |
| Akt III | 25 Bindungen (Meister). Ausrüstung V für 4 Kernplätze (Material 50 %). Tutoren ×4. Hain 4 (×5) | 151.061 |
| Endgame (je 10 h) | Hain 5 (×2). Erbklang ×20. Klangbad. Tutoren-Rest | 104.240 |

**Bilanz:**

| Abschnitt | Einnahmen | Bedarf | Quote | kumuliert (inkl. 1.000 ◎ Start) | Bewertung |
|---|---|---|---|---|---|
| Prolog | 1.628 | 1.950 | 83 % | 134 % | gesund |
| Akt I | 49.291 | 35.692 | 138 % | 137 % | gesund |
| Akt II | 135.250 | 109.972 | 122 % | 126 % | gesund |
| Akt III | 127.130 | 151.061 | 84 % | 105 % | knapp – Entscheidungen nötig |
| Endgame (je 10 h) | 113.550 | 104.240 | 108 % | 106 % | knapp – Entscheidungen nötig |

**Bewertung:** Prolog bis Akt II liegen kumuliert bei ~125–137 % – genug für Komfort und eigene Prioritäten. In Akt III wird es bewusst knapp (Meistersiegel für seltene Arten, Ausrüstung V): Der Spieler entscheidet, welche Kernplätze er auf V bringt. Im Endgame binden Hain V, Erbklang und Kosmetik den Überschuss – keine Inflation, keine Geld-Wand.

---

## 7. Händler und Sortimente

54 Händler in Städten und Dörfern (K11–K13, `Merchants.csv`) mit Öffnungszeiten (Weltuhr). Sortimente werden aus `ItemPrices.csv` nach Kategorie und Akt-Fortschritt gebildet:

| Kategorie | Sortiment | Freischaltung |
|---|---|---|
| General | Siegel, Lockmittel, Fallen, Grund-Verbrauchsgüter | Siegelstufe nach Akkorden (2: Gestimmt, 5: Meister) |
| Heal | Tinkturen, Weckklang, Läuterwasser | Stufe nach Akkorden |
| Material | Ressourcen der eigenen Region (Stufe ≤ aktueller Akt + 1), Klangsplitter (rotierend) | Region |
| Food | Futter der Region, Rezeptbücher | Region |
| Gear | Ausrüstung II–III, Sättel-Reparatur (kosmetisch) | Akt |
| Rare | Stimmsteine, Halteitems, Obertonkristalle (rotierend, 3 Angebote je Spieltag) | Akkord 3 |
| Faction | Fraktionswaren (Zucht-Gegenstände, Fraktionsschlüssel) | Ruf (K47) |
| Tutor | Tutor-Fähigkeiten (K29) | Ruf 3–4 |
| Scripts | Klangschrift-**Abschriften** zur Ansicht (Kodex-Hinweise), keine Klangschriften | – |

```
┌─ Wendels Wärterbedarf · Eichenhall · geöffnet 7–20 Uhr ──────────────────────────────┐
│ Klangsiegel          150 ◎   ▸ Schwelle −0 · verbraucht beim Anschlag (K36)            │
│ Gestimmtes Siegel    450 ◎   ▸ ab Akkord 2                                            │
│ Ruhenest             160 ◎   ▸ für schläfrige/nistende Arten (Kodex 2)                 │
│ Heilkraut-Tinktur     45 ◎   ▸ Wildwacht-Ruf 2: −5 %                                   │
│                                  Kontor-Tagespreis: Regen +0 % · Sol: 12.430 ◎          │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Preisschwankungen und Ereignisse

| Einfluss | Wirkung | Determinismus |
|---|---|---|
| Kontor-Tagespreis | Material/Food ±10 % je Spieltag | Loot-Strom `Fork(4)` + Spieltag – reproduzierbar, nicht durch Neuladen veränderbar |
| Heimatregion | Ressourcen der eigenen Region ×0,9, fremde ×1,15 | fest |
| Resonanzsturm | Sturmpreise +10 % (CANON §62) | Ereignis |
| Story-Ereignisse | z. B. Stillezonen-Krise in Akt I: Heilmittel in Eichenhall +20 % bis zur Lösung | Questzustand |
| Siedlungszustand | blühend −5 %, bedroht +10 % (K13 §5) | Zustand |

Keine Spieler-Marktpreise, keine Auktionen (§10).

---

## 9. Fraktionsrabatte und Ruf

| Fraktion | Rabatt (Rufrang 2 / 4 / 6) | Gilt für |
|---|---|---|
| Goldklang-Kontor (F02) | 5 / 10 / 15 % | alle Kontor-Händler, Material |
| Wildwacht (F03) | 5 / 10 / 10 % | Heilmittel, Fallen, Lockmittel |
| Akademie (F01) | 5 / 10 / 10 % | Siegel, Laborwaren |
| Freie Stimmen (F04) | 5 / 10 / 15 % | Schwarzmarkt-Waren (Unterstadt Morvenfurt) |
| Orden der Stille (F05) | – | kein Handel bis Akt III (Story) |

Rabatte stapeln nicht (der höchste gilt). Details zum Ruf: K47.

---

## 10. Tausch und Anti-Exploit

| Regel | Wert |
|---|---|
| Spielermarkt | **keiner** – keine Auktion, kein Sol-Handel zwischen Spielern (Schutz vor RMT, Inflation, Bots) |
| Tausch | Echo gegen Echo, Items in begrenzter Liste (Ressourcen, Gerichte, Lockmittel) bis 20 Stück je Tausch; Sol nicht tauschbar (K60) |
| Geschenke | Koop-Partner können Ressourcen schenken (Tageslimit 50 Stück) |
| Kreisläufe | Kauf → Verkauf verliert 65 %; herstellen → verkaufen verliert 72 % gegenüber Zutatenkauf |
| Duplizierung | Server-autoritative Inventare im Online-Modus (K59), Transaktions-IDs; Offline-Saves signiert beim Online-Gehen |

## Anhang A – Vollständige Preisliste

Generiert aus `ItemPrices.csv` (Wertmodell §3). „–“ = nicht käuflich.

| ID | Gegenstand | Wert | Kauf | Verkauf | Händler |
|---|---|---|---|---|---|
| ITM_BREED_ERBKLANG | Erbklang | 1.012 | 1.015 | 354 | Faction |
| ITM_BREED_KEIMWAERME | Keimwärmer | 167 | 170 | 58 | Faction |
| ITM_BREED_KLANGSTIMMUNG | Klangstimmung | 2.812 | – | 984 | – |
| ITM_CON_CLEANSE | Läuterwasser | 76 | 80 | 26 | Heal |
| ITM_CON_HEAL_1 | Heilkraut-Tinktur | 45 | 45 | 15 | Heal |
| ITM_CON_HEAL_2 | Starke Tinktur | 123 | 125 | 43 | Heal |
| ITM_CON_HEAL_3 | Quellwasser-Elixier | 575 | 575 | 201 | Heal |
| ITM_CON_HEAL_ALL | Chorbalsam | 391 | 395 | 136 | Heal |
| ITM_CON_KLANGSALZ | Klangsalz | 108 | 110 | 37 | General |
| ITM_CON_REPEL | Ruhrauch | 61 | 65 | 21 | General |
| ITM_CON_REVIVE | Weckklang | 302 | 305 | 105 | Heal |
| ITM_CON_SENSE | Lauschöl | 133 | 135 | 46 | General |
| ITM_CON_STAMINA | Bergtee | 77 | 80 | 26 | General |
| ITM_CON_WANDELKLANG | Wandelklang | 262 | 265 | 91 | General |
| ITM_CON_WARM | Glühwurzel-Sud | 140 | 140 | 49 | General |
| ITM_CON_WESENSKLANG | Wesensklang | 1.325 | – | 463 | – |
| ITM_EMAT_ARCANE | Klangsplitter (Arkan) | 30 | 30 | 10 | Material |
| ITM_EMAT_BLOOM | Klangsplitter (Blüte) | 30 | 30 | 10 | Material |
| ITM_EMAT_CRYSTAL | Klangsplitter (Kristall) | 30 | 30 | 10 | Material |
| ITM_EMAT_ECHOWOOL | Echowolle | 60 | 60 | 21 | Material |
| ITM_EMAT_EMBER | Klangsplitter (Glut) | 30 | 30 | 10 | Material |
| ITM_EMAT_FEATHER | Gefiederte Daune | 60 | 60 | 21 | Material |
| ITM_EMAT_FROST | Klangsplitter (Frost) | 30 | 30 | 10 | Material |
| ITM_EMAT_GRAVITY | Klangsplitter (Schwerkraft) | 30 | 30 | 10 | Material |
| ITM_EMAT_LIGHT | Klangsplitter (Licht) | 30 | 30 | 10 | Material |
| ITM_EMAT_METAL | Klangsplitter (Metall) | 30 | 30 | 10 | Material |
| ITM_EMAT_SCALE | Abgestreifte Schuppe | 60 | 60 | 21 | Material |
| ITM_EMAT_SHELLDUST | Panzerstaub | 60 | 60 | 21 | Material |
| ITM_EMAT_SOUND | Klangsplitter (Klang) | 30 | 30 | 10 | Material |
| ITM_EMAT_SPIRIT | Klangsplitter (Geist) | 30 | 30 | 10 | Material |
| ITM_EMAT_STILLSHARD | Stillstein-Splitter | 250 | – | 87 | – |
| ITM_EMAT_STONE | Klangsplitter (Stein) | 30 | 30 | 10 | Material |
| ITM_EMAT_STORM | Klangsplitter (Sturm) | 30 | 30 | 10 | Material |
| ITM_EMAT_TIDE | Klangsplitter (Flut) | 30 | 30 | 10 | Material |
| ITM_EMAT_VENOM | Klangsplitter (Gift) | 30 | 30 | 10 | Material |
| ITM_EMAT_VOID | Klangsplitter (Leere) | 30 | 30 | 10 | Material |
| ITM_EVO_ARCANE | Obertonkristall (Arkan) | 300 | 300 | 105 | Rare |
| ITM_EVO_ASHFEATHER | Aschefeder | 900 | 900 | 315 | Rare |
| ITM_EVO_AURORATHREAD | Aurorafaden | 900 | 900 | 315 | Rare |
| ITM_EVO_BLOOM | Obertonkristall (Blüte) | 355 | 355 | 124 | Rare |
| ITM_EVO_CRYSTAL | Obertonkristall (Kristall) | 355 | 355 | 124 | Rare |
| ITM_EVO_ECHOSHELL | Klangmuschel | 900 | 900 | 315 | Rare |
| ITM_EVO_EMBER | Obertonkristall (Glut) | 355 | 355 | 124 | Rare |
| ITM_EVO_EMBERCORE | Glutkern | 900 | 900 | 315 | Rare |
| ITM_EVO_FROST | Obertonkristall (Frost) | 300 | 300 | 105 | Rare |
| ITM_EVO_GLYPHSHARD | Glyphensplitter | 900 | 900 | 315 | Rare |
| ITM_EVO_GRAVITY | Obertonkristall (Schwerkraft) | 355 | 355 | 124 | Rare |
| ITM_EVO_LIGHT | Obertonkristall (Licht) | 355 | 355 | 124 | Rare |
| ITM_EVO_METAL | Obertonkristall (Metall) | 300 | 300 | 105 | Rare |
| ITM_EVO_MISTVEIL | Nebelschleier | 900 | 900 | 315 | Rare |
| ITM_EVO_MOONDEW | Mondtau | 900 | 900 | 315 | Rare |
| ITM_EVO_ROOTHEART | Wurzelherz | 900 | 900 | 315 | Rare |
| ITM_EVO_SOUND | Obertonkristall (Klang) | 355 | 355 | 124 | Rare |
| ITM_EVO_SPIRIT | Obertonkristall (Geist) | 300 | 300 | 105 | Rare |
| ITM_EVO_STARDUST | Sternenstaub | 900 | 900 | 315 | Rare |
| ITM_EVO_STONE | Obertonkristall (Stein) | 300 | 300 | 105 | Rare |
| ITM_EVO_STORM | Obertonkristall (Sturm) | 300 | 300 | 105 | Rare |
| ITM_EVO_TIDE | Obertonkristall (Flut) | 300 | 300 | 105 | Rare |
| ITM_EVO_TIDEPEARL | Gezeitenperle | 900 | 900 | 315 | Rare |
| ITM_EVO_VENOM | Obertonkristall (Gift) | 355 | 355 | 124 | Rare |
| ITM_EVO_VOID | Obertonkristall (Leere) | 300 | 300 | 105 | Rare |
| ITM_FOODC_CHEESEPLATE | Bergkäseplatte | 165 | 165 | 57 | Food |
| ITM_FOODC_CLOUDTART | Wolkentarte | 196 | 200 | 68 | Food |
| ITM_FOODC_DATEROLL | Dattelrolle | 196 | 200 | 68 | Food |
| ITM_FOODC_EMBERSOUP | Glutsuppe | 290 | 290 | 101 | Food |
| ITM_FOODC_FEAST | Chorfestmahl | 690 | 690 | 241 | Food |
| ITM_FOODC_FISHPIE | Fischpastete | 181 | 185 | 63 | Food |
| ITM_FOODC_HONEYCAKE | Honigkuchen | 206 | 210 | 72 | Food |
| ITM_FOODC_ICEJELLY | Eisgelee | 196 | 200 | 68 | Food |
| ITM_FOODC_KELPWRAP | Tangrolle | 206 | 210 | 72 | Food |
| ITM_FOODC_MOSSBUN | Moosbrötchen | 165 | 165 | 57 | Food |
| ITM_FOODC_SPICEBREAD | Würzbrot | 165 | 165 | 57 | Food |
| ITM_FOODC_STEW | Lindwald-Eintopf | 165 | 165 | 57 | Food |
| ITM_FOOD_ALPINECHEESE | Bergkäse | 40 | 40 | 14 | Food |
| ITM_FOOD_BERRYMIX | Waldbeeren | 40 | 40 | 14 | Food |
| ITM_FOOD_CHARCOAL | Glutkohle | 40 | 40 | 14 | Food |
| ITM_FOOD_CLOUDFRUIT | Wolkenfrucht | 40 | 40 | 14 | Food |
| ITM_FOOD_CRYSTALSALT | Kristallsalz | 40 | 40 | 14 | Food |
| ITM_FOOD_DATES | Datteln | 40 | 40 | 14 | Food |
| ITM_FOOD_ICEFISH | Eisfisch | 40 | 40 | 14 | Food |
| ITM_FOOD_KELPSNACK | Tangkeks | 40 | 40 | 14 | Food |
| ITM_FOOD_LINDHONEY | Lindblüten-Honig | 40 | 40 | 14 | Food |
| ITM_FOOD_MOORBERRY | Moorbeeren | 40 | 40 | 14 | Food |
| ITM_FOOD_MOSSCAKE | Moosküchlein | 40 | 40 | 14 | Food |
| ITM_FOOD_ORECRUMBS | Erzkrümel | 40 | 40 | 14 | Food |
| ITM_FOOD_SHELLMEAT | Muschelfleisch | 40 | 40 | 14 | Food |
| ITM_FOOD_SMOKEDFISH | Räucherfisch | 40 | 40 | 14 | Food |
| ITM_FOOD_SULFURCANDY | Schwefelzucker | 40 | 40 | 14 | Food |
| ITM_GEAR_BAG_1 | Wärtertasche I | 0 | – | 0 | – |
| ITM_GEAR_BAG_2 | Wärtertasche II | 715 | 715 | 250 | Gear |
| ITM_GEAR_BAG_3 | Wärtertasche III | 1.287 | 1.290 | 450 | Gear |
| ITM_GEAR_BAG_4 | Wärtertasche IV | 4.725 | – | 1.653 | – |
| ITM_GEAR_BAG_5 | Wärtertasche V | 6.737 | – | 2.357 | – |
| ITM_GEAR_BOOTS_1 | Wanderstiefel I | 0 | – | 0 | – |
| ITM_GEAR_BOOTS_2 | Wanderstiefel II | 527 | 530 | 184 | Gear |
| ITM_GEAR_BOOTS_3 | Wanderstiefel III | 1.850 | 1.850 | 647 | Gear |
| ITM_GEAR_BOOTS_4 | Wanderstiefel IV | 2.425 | – | 848 | – |
| ITM_GEAR_BOOTS_5 | Wanderstiefel V | 10.062 | – | 3.521 | – |
| ITM_GEAR_CLOAK_1 | Wettermantel I | 0 | – | 0 | – |
| ITM_GEAR_CLOAK_2 | Wettermantel II | 437 | 440 | 152 | Gear |
| ITM_GEAR_CLOAK_3 | Wettermantel III | 1.287 | 1.290 | 450 | Gear |
| ITM_GEAR_CLOAK_4 | Wettermantel IV | 4.725 | – | 1.653 | – |
| ITM_GEAR_CLOAK_5 | Wettermantel V | 6.737 | – | 2.357 | – |
| ITM_GEAR_GLIDER_1 | Gleiter I | 0 | – | 0 | – |
| ITM_GEAR_GLIDER_2 | Gleiter II | 437 | 440 | 152 | Gear |
| ITM_GEAR_GLIDER_3 | Gleiter III | 1.682 | 1.685 | 588 | Gear |
| ITM_GEAR_GLIDER_4 | Gleiter IV | 3.025 | – | 1.058 | – |
| ITM_GEAR_GLIDER_5 | Gleiter V | 6.912 | – | 2.419 | – |
| ITM_GEAR_LANTERN_1 | Laterne I | 0 | – | 0 | – |
| ITM_GEAR_LANTERN_2 | Laterne II | 647 | 650 | 226 | Gear |
| ITM_GEAR_LANTERN_3 | Laterne III | 1.012 | 1.015 | 354 | Gear |
| ITM_GEAR_LANTERN_4 | Laterne IV | 2.925 | – | 1.023 | – |
| ITM_GEAR_LANTERN_5 | Laterne V | 10.412 | – | 3.644 | – |
| ITM_GEAR_LENS_1 | Kodex-Linse I | 0 | – | 0 | – |
| ITM_GEAR_LENS_2 | Kodex-Linse II | 437 | 440 | 152 | Gear |
| ITM_GEAR_LENS_3 | Kodex-Linse III | 1.012 | 1.015 | 354 | Gear |
| ITM_GEAR_LENS_4 | Kodex-Linse IV | 3.025 | – | 1.058 | – |
| ITM_GEAR_LENS_5 | Kodex-Linse V | 7.962 | – | 2.786 | – |
| ITM_GEAR_MASK_1 | Atemmaske I | 0 | – | 0 | – |
| ITM_GEAR_MASK_2 | Atemmaske II | 527 | 530 | 184 | Gear |
| ITM_GEAR_MASK_3 | Atemmaske III | 1.850 | 1.850 | 647 | Gear |
| ITM_GEAR_MASK_4 | Atemmaske IV | 4.725 | – | 1.653 | – |
| ITM_GEAR_MASK_5 | Atemmaske V | 7.962 | – | 2.786 | – |
| ITM_GEAR_RESONATOR_1 | Resonator I | 0 | – | 0 | – |
| ITM_GEAR_RESONATOR_2 | Resonator II | 647 | 650 | 226 | Gear |
| ITM_GEAR_RESONATOR_3 | Resonator III | 1.287 | 1.290 | 450 | Gear |
| ITM_GEAR_RESONATOR_4 | Resonator IV | 3.025 | – | 1.058 | – |
| ITM_GEAR_RESONATOR_5 | Resonator V | 10.412 | – | 3.644 | – |
| ITM_GEAR_SADDLE_CLIMB | Klettersattel | 0 | – | 0 | – |
| ITM_GEAR_SADDLE_DIG | Grabsattel | 0 | – | 0 | – |
| ITM_GEAR_SADDLE_FLY | Flugsattel | 0 | – | 0 | – |
| ITM_GEAR_SADDLE_GROUND | Bodensattel | 0 | – | 0 | – |
| ITM_GEAR_SADDLE_SWIM | Schwimmsattel | 0 | – | 0 | – |
| ITM_GEAR_TOOL_1 | Wärterwerkzeug I | 0 | – | 0 | – |
| ITM_GEAR_TOOL_2 | Wärterwerkzeug II | 557 | 560 | 194 | Gear |
| ITM_GEAR_TOOL_3 | Wärterwerkzeug III | 1.012 | 1.015 | 354 | Gear |
| ITM_GEAR_TOOL_4 | Wärterwerkzeug IV | 3.525 | – | 1.233 | – |
| ITM_GEAR_TOOL_5 | Wärterwerkzeug V | 7.962 | – | 2.786 | – |
| ITM_HELD_BONDRIBBON | Bindungsband | 393 | 395 | 137 | Rare |
| ITM_HELD_CLEANSEBELL | Reinheitsglocke | 486 | 490 | 170 | Rare |
| ITM_HELD_EMBERCORE | Glutkern | 431 | 435 | 150 | Rare |
| ITM_HELD_FOCUSLENS | Fokuslinse | 486 | 490 | 170 | Rare |
| ITM_HELD_FOGSCARF | Nebelschal | 486 | 490 | 170 | Rare |
| ITM_HELD_HARMONYCHIME | Harmoniespiel | 431 | 435 | 150 | Rare |
| ITM_HELD_HEAVYSTONE | Schwerstein | 431 | 435 | 150 | Rare |
| ITM_HELD_LASTBREATH | Atemband | 486 | 490 | 170 | Rare |
| ITM_HELD_LEARNCHARM | Lernamulett | 486 | 490 | 170 | Rare |
| ITM_HELD_MIRRORSCALE | Spiegelschuppe | 486 | 490 | 170 | Rare |
| ITM_HELD_POLISHSTONE | Schliffstein | 431 | 435 | 150 | Rare |
| ITM_HELD_ROOTCHARM | Wurzelamulett | 486 | 490 | 170 | Rare |
| ITM_HELD_SHIELDBROOCH | Schildbrosche | 486 | 490 | 170 | Rare |
| ITM_HELD_STIMMBAND | Stimmband | 393 | 395 | 137 | Rare |
| ITM_HELD_SWIFTFEATHER | Sturmfeder | 431 | 435 | 150 | Rare |
| ITM_HELD_TAKTRING | Taktring | 486 | 490 | 170 | Rare |
| ITM_HELD_TONE_ARCANE | Stimmstein (Arkan) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_BLOOM | Stimmstein (Blüte) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_CRYSTAL | Stimmstein (Kristall) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_EMBER | Stimmstein (Glut) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_FROST | Stimmstein (Frost) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_GRAVITY | Stimmstein (Schwerkraft) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_LIGHT | Stimmstein (Licht) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_METAL | Stimmstein (Metall) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_SOUND | Stimmstein (Klang) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_SPIRIT | Stimmstein (Geist) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_STONE | Stimmstein (Stein) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_STORM | Stimmstein (Sturm) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_TIDE | Stimmstein (Flut) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_VENOM | Stimmstein (Gift) | 285 | 285 | 99 | Rare |
| ITM_HELD_TONE_VOID | Stimmstein (Leere) | 285 | 285 | 99 | Rare |
| ITM_HELD_WESENSBAND | Wesensband | 393 | 395 | 137 | Rare |
| ITM_KS_001 | Klangschrift: Schwelbrand | 0 | – | 0 | – |
| ITM_KS_002 | Klangschrift: Hitzeflimmern | 0 | – | 0 | – |
| ITM_KS_003 | Klangschrift: Sonnenesse | 0 | – | 0 | – |
| ITM_KS_004 | Klangschrift: Lodernder Ansturm | 0 | – | 0 | – |
| ITM_KS_005 | Klangschrift: Feueratem | 0 | – | 0 | – |
| ITM_KS_006 | Klangschrift: Schmelzhieb | 0 | – | 0 | – |
| ITM_KS_007 | Klangschrift: Regenruf | 0 | – | 0 | – |
| ITM_KS_008 | Klangschrift: Quellbad | 0 | – | 0 | – |
| ITM_KS_009 | Klangschrift: Nebelschleier | 0 | – | 0 | – |
| ITM_KS_010 | Klangschrift: Brandungsschlag | 0 | – | 0 | – |
| ITM_KS_011 | Klangschrift: Gezeitenwelle | 0 | – | 0 | – |
| ITM_KS_012 | Klangschrift: Tiefenstrom | 0 | – | 0 | – |
| ITM_KS_013 | Klangschrift: Felswall | 0 | – | 0 | – |
| ITM_KS_014 | Klangschrift: Steinhaut | 0 | – | 0 | – |
| ITM_KS_015 | Klangschrift: Bergrücken | 0 | – | 0 | – |
| ITM_KS_016 | Klangschrift: Gerölllawine | 0 | – | 0 | – |
| ITM_KS_017 | Klangschrift: Felsrammen | 0 | – | 0 | – |
| ITM_KS_018 | Klangschrift: Erdgrollen | 0 | – | 0 | – |
| ITM_KS_019 | Klangschrift: Gewitterruf | 0 | – | 0 | – |
| ITM_KS_020 | Klangschrift: Sturmlauf | 0 | – | 0 | – |
| ITM_KS_021 | Klangschrift: Böenchor | 0 | – | 0 | – |
| ITM_KS_022 | Klangschrift: Zyklonsprung | 0 | – | 0 | – |
| ITM_KS_023 | Klangschrift: Blitzbogen | 0 | – | 0 | – |
| ITM_KS_024 | Klangschrift: Wirbelsturm | 0 | – | 0 | – |
| ITM_KS_025 | Klangschrift: Heiltau | 0 | – | 0 | – |
| ITM_KS_026 | Klangschrift: Sonnentrunk | 0 | – | 0 | – |
| ITM_KS_027 | Klangschrift: Wuchern | 0 | – | 0 | – |
| ITM_KS_028 | Klangschrift: Blütensturm | 0 | – | 0 | – |
| ITM_KS_029 | Klangschrift: Saugwurzel | 0 | – | 0 | – |
| ITM_KS_030 | Klangschrift: Dornenranke | 0 | – | 0 | – |
| ITM_KS_031 | Klangschrift: Eisspiegel | 0 | – | 0 | – |
| ITM_KS_032 | Klangschrift: Kältestarre | 0 | – | 0 | – |
| ITM_KS_033 | Klangschrift: Weißer Atem | 0 | – | 0 | – |
| ITM_KS_034 | Klangschrift: Frostbiss | 0 | – | 0 | – |
| ITM_KS_035 | Klangschrift: Gletscherdruck | 0 | – | 0 | – |
| ITM_KS_036 | Klangschrift: Winterstille | 0 | – | 0 | – |
| ITM_KS_037 | Klangschrift: Lichtschlucker | 0 | – | 0 | – |
| ITM_KS_038 | Klangschrift: Leerer Raum | 0 | – | 0 | – |
| ITM_KS_039 | Klangschrift: Entzugsfluch | 0 | – | 0 | – |
| ITM_KS_040 | Klangschrift: Schweigeschnitt | 0 | – | 0 | – |
| ITM_KS_041 | Klangschrift: Stille Klinge | 0 | – | 0 | – |
| ITM_KS_042 | Klangschrift: Hohlklang | 0 | – | 0 | – |
| ITM_KS_043 | Klangschrift: Läuterung | 0 | – | 0 | – |
| ITM_KS_044 | Klangschrift: Heilschein | 0 | – | 0 | – |
| ITM_KS_045 | Klangschrift: Sonnenwehr | 0 | – | 0 | – |
| ITM_KS_046 | Klangschrift: Strahlenkranz | 0 | – | 0 | – |
| ITM_KS_047 | Klangschrift: Morgenrot | 0 | – | 0 | – |
| ITM_KS_048 | Klangschrift: Prismenstrahl | 0 | – | 0 | – |
| ITM_KS_049 | Klangschrift: Giftkleid | 0 | – | 0 | – |
| ITM_KS_050 | Klangschrift: Korrosion | 0 | – | 0 | – |
| ITM_KS_051 | Klangschrift: Schleichendes Gift | 0 | – | 0 | – |
| ITM_KS_052 | Klangschrift: Toxinwelle | 0 | – | 0 | – |
| ITM_KS_053 | Klangschrift: Nesselpeitsche | 0 | – | 0 | – |
| ITM_KS_054 | Klangschrift: Miasma | 0 | – | 0 | – |
| ITM_KS_055 | Klangschrift: Rüstwerk | 0 | – | 0 | – |
| ITM_KS_056 | Klangschrift: Konterhieb | 0 | – | 0 | – |
| ITM_KS_057 | Klangschrift: Panzerplatten | 0 | – | 0 | – |
| ITM_KS_058 | Klangschrift: Schrapnell | 0 | – | 0 | – |
| ITM_KS_059 | Klangschrift: Stahlsturm | 0 | – | 0 | – |
| ITM_KS_060 | Klangschrift: Magnetpuls | 0 | – | 0 | – |
| ITM_KS_061 | Klangschrift: Doppelgänger | 0 | – | 0 | – |
| ITM_KS_062 | Klangschrift: Seelenband | 0 | – | 0 | – |
| ITM_KS_063 | Klangschrift: Verschwinden | 0 | – | 0 | – |
| ITM_KS_064 | Klangschrift: Totenklage | 0 | – | 0 | – |
| ITM_KS_065 | Klangschrift: Phantomklaue | 0 | – | 0 | – |
| ITM_KS_066 | Klangschrift: Schreckensschrei | 0 | – | 0 | – |
| ITM_KS_067 | Klangschrift: Aufladen | 0 | – | 0 | – |
| ITM_KS_068 | Klangschrift: Spiegelwand | 0 | – | 0 | – |
| ITM_KS_069 | Klangschrift: Drusenfeld | 0 | – | 0 | – |
| ITM_KS_070 | Klangschrift: Kristallregen | 0 | – | 0 | – |
| ITM_KS_071 | Klangschrift: Klirrschlag | 0 | – | 0 | – |
| ITM_KS_072 | Klangschrift: Facettenschnitt | 0 | – | 0 | – |
| ITM_KS_073 | Klangschrift: Schallwand | 0 | – | 0 | – |
| ITM_KS_074 | Klangschrift: Resonanzkreis | 0 | – | 0 | – |
| ITM_KS_075 | Klangschrift: Wiegenlied | 0 | – | 0 | – |
| ITM_KS_076 | Klangschrift: Taktbruch | 0 | – | 0 | – |
| ITM_KS_077 | Klangschrift: Fortissimo | 0 | – | 0 | – |
| ITM_KS_078 | Klangschrift: Dissonanz | 0 | – | 0 | – |
| ITM_KS_079 | Klangschrift: Umkehrfeld | 0 | – | 0 | – |
| ITM_KS_080 | Klangschrift: Schwebe | 0 | – | 0 | – |
| ITM_KS_081 | Klangschrift: Gewichtslast | 0 | – | 0 | – |
| ITM_KS_082 | Klangschrift: Singularität | 0 | – | 0 | – |
| ITM_KS_083 | Klangschrift: Implosion | 0 | – | 0 | – |
| ITM_KS_084 | Klangschrift: Erdanziehung | 0 | – | 0 | – |
| ITM_KS_085 | Klangschrift: Umkehrrune | 0 | – | 0 | – |
| ITM_KS_086 | Klangschrift: Fluchwort | 0 | – | 0 | – |
| ITM_KS_087 | Klangschrift: Glyphenkreis | 0 | – | 0 | – |
| ITM_KS_088 | Klangschrift: Siegelbruch | 0 | – | 0 | – |
| ITM_KS_089 | Klangschrift: Bannzeichen | 0 | – | 0 | – |
| ITM_KS_090 | Klangschrift: Spiegelformel | 0 | – | 0 | – |
| ITM_LURE_AURORAGLASS | Auroraglas | 180 | 180 | 63 | General |
| ITM_LURE_BELLCHIME | Glockenspiel | 180 | 180 | 63 | General |
| ITM_LURE_GLYPHTOKEN | Glyphenmünze | 180 | 180 | 63 | General |
| ITM_LURE_LANTERN | Irrlicht-Laterne | 180 | 180 | 63 | General |
| ITM_LURE_MIRROR | Spiegelscherbe | 180 | 180 | 63 | General |
| ITM_LURE_STARCHIME | Sternenglocke | 180 | 180 | 63 | General |
| ITM_LURE_TUNINGFORK | Lockstimmgabel | 180 | 180 | 63 | General |
| ITM_LURE_WHISTLE | Pfeifholz | 180 | 180 | 63 | General |
| ITM_LURE_WINDCHIME | Windspiel | 180 | 180 | 63 | General |
| ITM_MAT_ASHWOOD | Ascheholz | 45 | 45 | 15 | Material |
| ITM_MAT_CAVEMUSHROOM | Höhlenpilz | 80 | 80 | 28 | Material |
| ITM_MAT_CLOUDWOOD | Wolkenholz | 210 | 210 | 73 | Material |
| ITM_MAT_COPPERORE | Kupfererz | 12 | 15 | 4 | Material |
| ITM_MAT_CRYSTALMOSS | Kristallmoos | 210 | 210 | 73 | Material |
| ITM_MAT_DESERTTHORN | Wüstendornholz | 45 | 45 | 15 | Material |
| ITM_MAT_DORUNSTONE | Dorunstein | 80 | 80 | 28 | Material |
| ITM_MAT_DRIFTWOOD | Treibholz | 12 | 15 | 4 | Material |
| ITM_MAT_ELDERWOOD | Altholz | 120 | 120 | 42 | Material |
| ITM_MAT_EMBERSAND | Glutsand | 37 | 40 | 12 | Material |
| ITM_MAT_FERNFIBER | Farnfaser | 12 | 15 | 4 | Material |
| ITM_MAT_FIRELILY | Feuerlilie | 67 | 70 | 23 | Material |
| ITM_MAT_FOGPEARL | Nebelperle | 37 | 40 | 12 | Material |
| ITM_MAT_FROSTPINE | Frostkiefer | 45 | 45 | 15 | Material |
| ITM_MAT_GLACIERQUARTZ | Gletscherquarz | 120 | 120 | 42 | Material |
| ITM_MAT_GLYPHCRYSTAL | Glyphenkristall | 120 | 120 | 42 | Material |
| ITM_MAT_GROLLBASALT | Grollbasalt | 37 | 40 | 12 | Material |
| ITM_MAT_ICEBLOOM | Eisblume | 200 | 200 | 70 | Material |
| ITM_MAT_KELP | Seetang | 12 | 15 | 4 | Material |
| ITM_MAT_KHARSIRON | Kharseisen | 25 | 25 | 8 | Material |
| ITM_MAT_LINDBLOSSOM | Lindblüte | 12 | 15 | 4 | Material |
| ITM_MAT_MOORWILLOW | Moorweide | 12 | 15 | 4 | Material |
| ITM_MAT_MOSSPEARL | Moosperle | 18 | 20 | 6 | Material |
| ITM_MAT_MOUNTAINPINE | Bergkiefer | 25 | 25 | 8 | Material |
| ITM_MAT_NACRE | Perlmutt | 37 | 40 | 12 | Material |
| ITM_MAT_OAKWOOD | Eichenholz | 12 | 15 | 4 | Material |
| ITM_MAT_OASISMINT | Oasenminze | 25 | 25 | 8 | Material |
| ITM_MAT_OBSIDIAN | Obsidian | 45 | 45 | 15 | Material |
| ITM_MAT_PEAKGENTIAN | Gipfelenzian | 37 | 40 | 12 | Material |
| ITM_MAT_PEATCOAL | Torfkohle | 12 | 15 | 4 | Material |
| ITM_MAT_POLARLICHEN | Polarflechte | 45 | 45 | 15 | Material |
| ITM_MAT_PRISMORE | Prismaerz | 210 | 210 | 73 | Material |
| ITM_MAT_QUARTZSHARD | Quarzsplitter | 12 | 15 | 4 | Material |
| ITM_MAT_RESONANCECRYSTAL | Resonanzkristall | 350 | 350 | 122 | Material |
| ITM_MAT_RUINVINE | Ruinenrebe | 45 | 45 | 15 | Material |
| ITM_MAT_SALTCOPPER | Salzkupfer | 45 | 45 | 15 | Material |
| ITM_MAT_SALTWORT | Salzkraut | 12 | 15 | 4 | Material |
| ITM_MAT_SILVERORE | Silbererz | 45 | 45 | 15 | Material |
| ITM_MAT_SKYGLASS | Himmelsglas | 210 | 210 | 73 | Material |
| ITM_MAT_SLAGSTEEL | Schlackenstahl | 120 | 120 | 42 | Material |
| ITM_MAT_SOUNDRESIN | Klangharz | 62 | 65 | 21 | Material |
| ITM_MAT_STARMETAL | Sternmetall | 350 | 350 | 122 | Material |
| ITM_MAT_SULFURCRYSTAL | Schwefelkristall | 25 | 25 | 8 | Material |
| ITM_MAT_SUNGLASS | Sonnenglas | 67 | 70 | 23 | Material |
| ITM_MAT_SWAMPMYRTLE | Sumpfmyrte | 25 | 25 | 8 | Material |
| ITM_MAT_TINORE | Zinnerz | 12 | 15 | 4 | Material |
| ITM_MAT_WINDBLOSSOM | Windblüte | 140 | 140 | 49 | Material |
| ITM_MAT_WISPMOSS | Irrlichtmoos | 112 | 115 | 39 | Material |
| ITM_SEAL_BASIC | Klangsiegel | 150 | 150 | 52 | General |
| ITM_SEAL_HEAVY | Erdsiegel | 655 | 655 | 229 | General |
| ITM_SEAL_MASTER | Meistersiegel | 1.200 | 1.200 | 420 | General |
| ITM_SEAL_NIGHT | Mondsiegel | 842 | 845 | 294 | General |
| ITM_SEAL_STAR | Sternensiegel | 0 | – | 0 | – |
| ITM_SEAL_TUNED | Gestimmtes Siegel | 450 | 450 | 157 | General |
| ITM_SEAL_TYPE | Klangfarben-Siegel | 675 | 675 | 236 | General |
| ITM_SEAL_VOICE | Stimmsiegel | 0 | – | 0 | – |
| ITM_TRAP_CHIME | Klangfalle | 152 | 155 | 53 | General |
| ITM_TRAP_HOARD | Schatzkiste | 122 | 125 | 42 | General |
| ITM_TRAP_NET | Ruhenetz | 130 | 130 | 45 | General |
| ITM_TRAP_POOL | Quellbecken | 130 | 130 | 45 | General |
| ITM_TRAP_REST | Ruhenest | 160 | 160 | 56 | General |
| ITM_TRAP_SCENT | Duftfalle | 122 | 125 | 42 | General |
| ITM_TRAP_SHADE | Schattenzelt | 130 | 130 | 45 | General |
| ITM_TRAP_WARM | Wärmestein | 130 | 130 | 45 | General |

---

## 11. Code

```cpp
// GF_Economy – Preisberechnung beim Öffnen eines Ladens
int32 UShopService::BuyPrice(const FItemPriceRow& P, const FShopContext& Ctx) const
{
    int64 Price = P.BuyPrice;
    Price = Price * Ctx.DailyFactorPermille / 1000;                       // Kontor-Tagespreis (Fork(4), Spieltag)
    Price = Price * (Ctx.bHomeRegion ? 900 : (P.bRegional ? 1150 : 1000)) / 1000;
    Price = Price * Ctx.EventFactorPermille / 1000;                       // Resonanzsturm, Story, Siedlungszustand
    Price = Price * (1000 - Ctx.BestFactionDiscountPermille) / 1000;      // höchster Rabatt (K47)
    return int32((Price + 4) / 5 * 5);                                    // auf 5 ◎ runden
}

int32 Aethris::Economy::RewardScalePermille(int32 Level) { return (Level + 10) * 1000 / 20; }
```

---

## 12. Tests und Telemetrie

| Test | Inhalt |
|---|---|
| `Data.Items.Validate` | Preise nur für existierende Items; Klangschriften/Stimmsiegel nicht käuflich |
| `Aethris.Unit.Economy.Price` | Faktorenreihenfolge, Rundung, Rabatt-Höchstwert |
| `…Economy.NoLoop` | kein Gegenstand mit Verkauf > Kauf irgendwo im Spiel |
| `Aethris.Func.Economy.ActBalance` | Bot-Durchlauf: kumulierte Quote 100–150 % je Akt |

**Telemetrie:** Sol-Kontostand je Spielstunde (Median, P90), Ausgaben je Kategorie, Anteil Spieler mit > 200.000 ◎ unbenutzt (Inflationssignal), meistgekaufte Items.

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-154 | Preise aus einem Wertmodell (Stufe × Seltenheit, Rezept ×1,25) | Konsistenz, automatische Anpassung | Handpreise |
| ADR-155 | Wildkämpfe ohne Sol; Sol aus Wärtern, Aufträgen, Quests | Diegese, kein Farmen wilder Echos | Sol-Drops |
| ADR-156 | Kein Spielermarkt, Sol nicht tauschbar | RMT-/Inflationsschutz | Auktionshaus |
| ADR-157 | Deterministische Tagespreise | kein Save-Scumming, Koop-gleich | Zufallspreise je Besuch |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §160 | Sol ◎: Start 1.000, Maximum 9.999.999, nicht käuflich, Verlust nur Meister-Grad | LOCKED |
| §161 | Preismodell: Ressourcen 12/25/45/80/140 × Seltenheit 1/1,5/2,5; Echo-Materialien 30/60/250; hergestellt Σ × 1,25; Kauf = Wert (5er-Rundung), Verkauf 35 %; Siegel fest 150/450/1.200; nicht käuflich: Klangschriften, Stimm-/Sternensiegel, Wesensklang, Klangstimmung, Ausrüstung IV–V (`ItemPrices.csv`) | LOCKED |
| §162 | Quellen: Wärter Ass-Lv. × 25 × Klasse (0,8/1,0/1,5/3,0), Aufträge Basis × RewardScale (L+10)/20, Kisten 60 × RS, Arenen 2.000/5.000/12.000 je Akkord; Wildkämpfe, PvP, Raids ohne Sol. Senken laut K42 §5 | LOCKED (Tuning → K63) |
| §163 | 54 Händler mit Kategorien und Freischaltungen; Tagespreise ±10 % (Fork(4)), Heimat ×0,9/fremd ×1,15, Ereignisse; Fraktionsrabatte 5/10/15 % (höchster gilt); kein Spielermarkt | LOCKED |
| §10 | ADR-154 – ADR-157 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Ziele und Sol-Regeln
- [x] Preismodell mit 333 berechneten Preisen
- [x] Quellen, Senken, RewardScale (aus K13 offen → gelöst)
- [x] Bilanz-Simulation je Akt
- [x] Händler-Sortimente, Tagespreise, Ereignisse, Rabatte
- [x] Tausch und Anti-Exploit
- [x] Code, Tests, Telemetrie, ADR-154 – ADR-157, CANON §160–§163

➡️ **Nächstes Kapitel: K43 – Wärterrang und Skilltree (löst Q14).**
