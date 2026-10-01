# K55 · Audio Bible

| Feld | Wert |
|---|---|
| Dokument | Kapitel 55 von 68 · Präsentation II |
| Version | 1.0 |
| Owner | Audio Director |
| Mitwirkende | Komponist:in, Sound Designer (Echos, Welt, Kampf), Technical Sound Designer (MetaSounds/Quartz), Dialogue Director, Localization (VO), Accessibility Lead |
| Baut auf | K07 (Weltlied: 10 Stimmen × 15 Klangfarben × Pause), K12 §7–§8 (Weltlied-Leitmotiv, Stadtfragmente; CANON §56), K14 (Wetter, Resonanzsturm), K16 §3 (Klangmal), K31–K36 (Kampf, Bindung), K44–K46 (Leitmotive in Szenen), K51 (Orte der Pause), K53 (Barks), K54 (UI-Klang, Barrierefreiheit), CANON §9 (MetaSounds + Quartz), DR-24 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Audio/` (`Leitmotifs.csv`, `TypeTones.csv`, `MusicStates.csv`, `MixBuses.csv`, generiert: `EchoCalls.csv` mit 256 Rufprofilen), `tools/ref/aethris_music.py`, `GF_Audio/Public/Music/AethrisMusicTypes.h` (+ `.cpp`) |
| Neue Kanon-Einträge | CANON §212 (Weltlied-Motiv und Skala), §213 (Leitmotive), §214 (Adaptive Musik), §215 (Echo-Rufe), §216 (Stille, Mix, Technik) |

---

## Inhalt

1. [Leitbild: Klang ist Spiel](#1-leitbild-klang-ist-spiel)
2. [Das Weltlied](#2-das-weltlied)
3. [Leitmotive](#3-leitmotive)
4. [Adaptive Musik](#4-adaptive-musik)
5. [Echo-Rufe](#5-echo-rufe)
6. [Welt und Ambient](#6-welt-und-ambient)
7. [Resonanzsinn und Frequenz-Mechaniken](#7-resonanzsinn-und-frequenz-mechaniken)
8. [Stille als Klang](#8-stille-als-klang)
9. [Kampfklang](#9-kampfklang)
10. [Stimme und Dialog](#10-stimme-und-dialog)
11. [Mix und Lautheit](#11-mix-und-lautheit)
12. [Technik](#12-technik)
13. [Barrierefreiheit](#13-barrierefreiheit)
14. [Produktion](#14-produktion)
15. [Anforderungen an andere Abteilungen](#15-anforderungen-an-andere-abteilungen)
16. [Decision Records](#16-decision-records)
17. [Kanon-Änderungen](#17-kanon-änderungen)
18. [Kapitel-Checkliste](#18-kapitel-checkliste)

---

## 1. Leitbild: Klang ist Spiel

In AETHRIS ist die Welt ein Lied. Echos sind Obertöne, Stillezonen sind Pausen, die Krone ist ein erzwungener Einklang, und das Ende ist eine Frage nach Freiheit im Klang. Audio ist deshalb nicht Begleitung, sondern **Systemsprache**:

| Grundsatz | Bedeutung |
|---|---|
| **Alles stimmt** | Rufe, Musik, UI und Welt teilen eine Skala (Aethrische Skala, §2.2) – das Spiel klingt als Ganzes |
| **Pausen sind Inhalt** | Musik lässt Raum; Stille ist ein gestaltetes Ereignis (§8) |
| **Hören = Sehen** | Jede klangliche Information hat ein gleichwertiges visuelles Signal (DR-24, K54 §10.2) |
| **Vom Fragment zum Ganzen** | Jede Stadt trägt ein Stück des Weltlieds; erst das Finale fügt sie zusammen (CANON §56) |
| **Lebendig, nicht laut** | Lautheit dient Lesbarkeit: Gameplay-Signale haben Vorrang vor Musik (§11) |

---

## 2. Das Weltlied

### 2.1 Das Motiv

Das Weltlied-Leitmotiv hat **sieben Töne** (CANON §56). Es wird hier verbindlich festgelegt:

| Ton | Name | Dauer (Viertel) | Skalenstufe | Funktion |
|---|---|---|---|---|
| 1 | D4 | 2 | 1 | Grundton (Ruhe) |
| 2 | A4 | 1 | 5 | Quintsprung (Ruf) |
| 3 | G4 | 1 | 4 | Rückschritt |
| 4 | F4 | 1,5 | 3 | Seufzer |
| 5 | E4 | 0,5 | 2 | Leitton nach unten |
| 6 | C5 | 2 | 7 | Aufbruch |
| 7 | D5 | 3 | 1 | Oktave (Ankunft) |

**Gestalt:** Ein Quintsprung als Ruf, ein langsamer Abstieg (Seufzer, Leitton nach unten), dann der Aufbruch über den Grundton hinaus zur Oktave – musikalisch die Geschichte des Spiels: Ruf, Verlust, neues Lied.

### 2.2 Die Aethrische Skala

Alle tonalen Klänge des Spiels liegen in **D-Dorisch** (D E F G A H C): Musik, Echo-Rufe, UI-Töne, Glocken, Rätselinstrumente. Dorisch ist weder Dur noch Moll – warm und offen, mit einer leisen Wehmut (die große Sexte H). Ausnahmen sind bewusst: das **Krone-Motiv** (alle zehn Töne auf D, kein Intervall) und **Leere** (Pause statt Ton).

### 2.3 Ableitungen

| Ableitung | Töne | Verwendung |
|---|---|---|
| Original | D4 (2) – A4 (1) – G4 (1) – F4 (1,5) – E4 (0,5) – C5 (2) – D5 (3) | Weltlied, Aerion, Finale „Neues Lied“ |
| Umkehrung (um D4) | D4 (2) – G3 (1) – A3 (1) – H3 (1,5) – C4 (0,5) – E3 (2) – D3 (3) | Hvitmark, Gedenken |
| Krebs | D5 (3) – C5 (2) – E4 (0,5) – F4 (1,5) – G4 (1) – A4 (1) – D4 (2) | Dorunsruh, Kael-Thema (vom Wärter-Thema) |
| Arpeggio 1/3/5/7 | D4 (2) – G4 (1) – E4 (0,5) – D5 (3) | Prismara, Ilen-Motiv |
| Krone (unisono) | D4 (4) in allen Oktaven D1–D7 | Krone-Motiv |
| Stille | D4 (2) – Pause (1) – G4 (1) – Pause (1,5) – E4 (0,5) – Pause (2) – D5 (3) | Stille-Motiv (Töne 2/4/6 durch Pausen ersetzt) |

### 2.4 Zehn Stimmen, fünfzehn Klangfarben

Das Weltlied hat zehn Stimmen (die Ursprungsstimmen, K07 §5). Musikalisch entspricht jede einer **Stimmgruppe**, die im Finale („Neues Lied“) eine eigene Linie des Motivs spielt:

| Stimme | Region | Stimmgruppe | Linie im Finale |
|---|---|---|---|
| Sylv'anor | Verdanthain | Holzbläser | Original |
| Orh'gruun | Kharsgrat | Tiefe Blechbläser + Männerchor | Augmentation (doppelte Dauern) |
| Nhael'vesh | Morvenmoor | Klarinetten, Bassflöte | Stille-Fassung |
| Thal'assyr | Saltrand | Streicher (Legato) | Umkehrung, versetzt |
| Ash'kareth | Sahrun-Weite | Saiten mit Bünden | Arpeggio |
| Pyr'thagon | Ignareth | Blech + Ambosse | Rhythmisches Ostinato aus Ton 1 und 5 |
| Isv'aldr | Hvitfell | Gestrichene Saiten, Glocken | Umkehrung |
| Ka'thurel | Ael'Dorun | Streicherkanon | Krebs |
| Prism'aion | Prismtiefen | Glasharfe, Klangschalen | Arpeggio in Oktaven |
| Aeth'rion | Nimbara | Chor ohne Worte | Original eine Oktave höher (Leitstimme) |

In „Sanfte Stille“ spielen dieselben zehn Gruppen das **Wiegenlied aus Eiðvik** (Sereths Melodie, K46 §7.2) – auf die Töne 1, 3, 5 reduziert, mit Streicher-Decke.

### 2.5 Städte als Fragmente

| Stadt | Fragment (CANON §56) | Töne | Charakter |
|---|---|---|---|
| Eichenhall | Töne 1–2 | D4 (2) – A4 (1) | Weite Quinte; Laute + Holzbläser, Lindenfest-Tanz |
| Kharsholm | Töne 2–3 | A4 (1) – G4 (1) | Schritt abwärts; Männerchor, Ambosse im Takt der Schichten |
| Morvenfurt | Töne 3–4 | G4 (1) – F4 (1,5) | Nachtmusik; Klarinette, Laternenglöckchen |
| Saltrand-Hafen | Töne 4–5 | F4 (1,5) – E4 (0,5) | Halbton; Akkordeon, Wellen, Glockenflut |
| Qasr Sahrun | Töne 5–6 | E4 (0,5) – C5 (2) | Großer Sprung; Saiten mit Bünden, Wüstenwind |
| Schlackenwehr | Töne 6–7 | C5 (2) – D5 (3) | Aufbruch zur Oktave; Schmiedeglocken, Blech |
| Hvitmark | Umkehrung | D4 (2) – G3 (1) – A3 (1) – H3 (1,5) – C4 (0,5) – E3 (2) – D3 (3) | Gespiegelt nach unten; Nyckelharpa-artige Streicher, Gedenken |
| Dorunsruh | Krebs, fragmentiert | D5 (3) – E4 (0,5) – G4 (1) – D4 (2) | Rückwärts, lückenhaft; Streicherkanon, Glyphenhall |
| Prismara | Arpeggio 1/3/5/7 | D4 (2) – G4 (1) – E4 (0,5) – D5 (3) | Gebrochen; Glasharfe, jede Farbe ein Ton |
| Aerion | vollständig | D4 (2) – A4 (1) – G4 (1) – F4 (1,5) – E4 (0,5) – C5 (2) – D5 (3) | Das ganze Motiv – einsam, ohne Begleitung (Isolation) |

---

## 3. Leitmotive

| DisplayName | Form | Instrumentation | Source | FirstHeard | Notes |
|---|---|---|---|---|---|
| Weltlied | 7-Ton-Motiv D–A–G–F–E–C–D (§2) | Volles Orchester + 10 Stimmgruppen | Original | MQ_P01 Kalte Eröffnung (Abbruch) | Erst im Finale („Neues Lied“) vollständig und zehnstimmig frei |
| Stille | Pausen im Takt; gedämpfte Streicher; Motivtöne mit Lücken | Gedämpfte Streicher + Atem | Weltlied mit Pausen statt Tönen 2/4/6 | MQ_P01 Stillezone | Velnox Phase 4: ein gehaltener Ton |
| Ilen | Weltlied-Töne 1–3–5–7 als Summen (Moll-Färbung) | Frauenstimme summend + Harfe | Arpeggio 1/3/5/7 | MQ_A1_08 Vision (fragmentiert) | Ysoldes Summen ist Ilens Motiv; im Brief in Dur aufgelöst |
| Krone | Zehn Töne unisono (D in allen Oktaven) | Blech + Orgel | Weltlied auf Ton 1 eingefroren | MQ_A2_07 Gewölbe | Erklingt nach MQ_A3_07 nie wieder |
| Wärter-Thema | Weltlied 1–4 + eigene Antwortphrase | Gitarre/Laute + Streicher | Weltlied Kopf | MQ_P01 Erstresonanz | Lagerfeuer-Fassungen |
| Orden der Stille | Glocken; nach jedem Schlag 2 Takte Stille | Glocken + Kontrabass | Stille-Motiv | MQ_A1_06 | Nach W6 gebrochen (Glocke verstimmt) |
| Akademie | Streicher-Kanon über Weltlied 1–2 | Streichquartett | Weltlied Kopf als Kanon | MQ_A1_07 Venns Rede | Kippt in Moll im Gewölbe (W6) |
| Freie Stimmen | Trommeln und Rufe; Weltlied 5–7 synkopiert | Trommeln + Chor | Weltlied Schluss | MQ_A1_04 | Unterstadt-Fest |
| Goldklang-Kontor | Walzer-Takt; Glocke auf Zählzeit 1 | Akkordeon + Glocke | Weltlied 4–5 | MQ_A1_05 | Glockenflut-Fest |
| Kael | Wärter-Thema rückwärts (Krebs) | Klavier + Violine | Wärter-Thema Krebs | MQ_P01 | In Akademie-Instrumentierung nach W6; zurückgewonnen bei Kaels Eingriff |
| Wendelin | Spieluhr; Weltlied 1–7 in Spieldose-Register | Spieluhr | Weltlied (hoch) | MQ_A2_01 Archiv |  |
| Erstresonanz | Ruf des Starters + Wärter-Thema | Starter-Timbre + Gitarre | Typ-Ton des Starters | MQ_P01 |  |

### 3.1 Regionsthemen

| Region | Thema | Instrumentierung | Tag / Nacht |
|---|---|---|---|
| Verdanthain | Lindwiesen-/Verdanthain-Thema | Laute, Flöte, Streicher | Tag: offen, Vogelrufe im Takt · Nacht: Solo-Flöte, Pilzleuchten als Glocken |
| Kharsgrat | Ahnenthema | Männerchor, Trommel, Horn | Tag: Arbeit (Ambosse) · Nacht: Brummen der Felsen |
| Morvenmoor | Moorthema | Klarinette, Bassflöte, Wasserglas | Tag: verhalten · Nacht: Hauptzeit, Nachtmarkt |
| Saltrand | Gezeitenthema | Akkordeon, Streicher, Glocken | Flut/Ebbe als Lautstärkewelle |
| Sahrun-Weite | Sahrun-Thema | Saiten mit Bünden, Rahmentrommel, Wind | Tag: flirrend, sparsam · Nacht: Sterne als Glasglöckchen |
| Ignareth | Glutthema | Blech, Ambosse, tiefe Trommel | Ausbruch: Ostinato verdoppelt |
| Hvitfell | Polarthema | Gestrichene Saiten, Glocken, Frauenchor | Polarlicht: Chor setzt ein |
| Ael'Dorun | Glyphenthema | Streicherkanon, Cembalo | Ruinen: Krebs-Fragmente |
| Prismtiefen | Prismara-Thema | Glasharfe, Klangschalen | Farben als Töne (Licht = Klang, K46) |
| Nimbara | Nimbara-Thema | Chor ohne Worte, Wind, Harfe | Wolken als Hall |

**Regel:** Jedes Regionsthema enthält das Fragment seiner Stadt (§2.5) mindestens einmal pro Durchlauf, meist versteckt (Bass, Ostinato, Glocke).

---

## 4. Adaptive Musik

| Name | Priority | Trigger | Layers | Transition | Intensity | Notes |
|---|---|---|---|---|---|---|
| MS_STORY | 1 | Zwischensequenz/Szene | Partitur der Szene | Szenenschnitt | – | Sequencer steuert |
| MS_DECISION | 1 | Finale Phase 4 / SCR_DECISION | Gehaltener Ton | sofort | – | Keine Zeitgrenze (K46) |
| MS_BOSS | 2 | Bosskampf | Boss-Thema + Phasen-Stems | Taktgrenze | Phase 1–4 | Phasenwechsel auf nächster Taktgrenze |
| MS_ARENA | 2 | Arenakampf | Arena-Fanfare (Region) + Kampf-Stems | Taktgrenze | Harmonie 0–100 → 3 Stufen | Typ-Variation des Arenameisters |
| MS_COMBAT_TRAINER | 3 | Wärterkampf | Kampf-Thema Region | 2 Schläge | Harmonie → 3 Stufen |  |
| MS_COMBAT_WILD | 3 | Wildkampf | Kurzes Kampf-Motiv + Ambient | 1 Schlag | 1 Stufe | Kurze Kämpfe (DR-11) – kein langer Aufbau |
| MS_BOND | 3 | Anschlag-Phase | Weltlied-Ton der Art + Frequenzwelle | sofort | – | Ton der Art im Takt des Klangmals (K36) |
| MS_SILENCE | 3 | In Stillezone | Stille-Motiv + Hochpass | Taktgrenze | – | Echos ohne Rufe |
| MS_STORM | 3 | Resonanzsturm | Alle Region-Stems gleichzeitig + quantisierte Rufe | Taktgrenze | – | CANON §63 |
| MS_TOWN | 4 | In Siedlung | Stadt-/Dorfthema (Weltlied-Fragment) | 4 Takte | Tag/Nacht | CANON §56 |
| MS_EXPLORE_DAY | 5 | Oberwelt Tag | Region-Thema (sparsam) | 4 Takte | Erkundung → Entdeckung | Lange Pausen (Atem) |
| MS_EXPLORE_NIGHT | 5 | Oberwelt Nacht | Region-Thema Nachtfassung | 4 Takte | – |  |
| MS_CAMP | 5 | Lager-Moment | Wärter-Thema Lagerfeuer | Taktgrenze | – | K44 §2 |
| MS_PAUSE | 6 | Ort der Pause | 1 s völlige Stille im festen Takt | sofort | – | K51 §7 |

### 4.1 Ablauf

```
Zustand gewünscht (höchste Priorität gewinnt)
   │
   ▼
Quartz: nächste erlaubte Grenze (Schlag / Takt / 4 Takte laut Transition)
   │
   ├── gleiche Tonart? ──► Stems überblenden (2 Schläge)
   └── neue Szene?    ──► Übergangsstinger (Weltlied-Ton 1 oder 7), dann neues Thema
```

| Regel | Inhalt |
|---|---|
| Atem | Erkundungsmusik spielt 2–4 min, dann 1–3 min Pause (nur Ambient) – keine Dauerbeschallung |
| Harmonie → Intensität | Kampf-Stems in 3 Stufen nach Harmonie (0–39, 40–79, 80–100); bei 100 setzt die Crescendo-Fanfare ein |
| Boss-Phasen | Phasenwechsel auf der nächsten Taktgrenze; Velnox Phase 4: Musik hält einen Ton (MS_DECISION) |
| Wildkampf | Kurzes Motiv (≤ 12 s), dann Ambient; Wildkämpfe dauern 60–120 s (DR-11) und sollen nicht „schwer“ klingen |
| Bindung | Die Musik tritt zurück; die Frequenzwelle spielt den Grundton der Art im Takt ihres Klangmals |
| Resonanzsturm | Alle Stems der Region gleichzeitig, Rufe quantisiert (§5.3) – „die Welt singt zu laut“ |
| Koop | Musikzustand je Spieler lokal (keine Replikation), Kampf/Sturm/Story werden über Spielzustände synchron |

---

## 5. Echo-Rufe

### 5.1 Typen und Töne

Jeder Typ hat eine Skalenstufe und eine Klangfarbe; die Größe bestimmt die Oktave, das Klangmal das Tempo.

| Typ | Skalenstufe | Grundton (M) | Klangfarbe | Familie | Charakter |
|---|---|---|---|---|---|
| Ember | 5 | A4 | Glimmen + Holzbläser-Atem | Bläser | Warm, knisternd, steigt |
| Tide | 3 | F4 | Wassergläser + Bogen | Glas/Streicher | Wellend, Legato |
| Stone | 1 | D4 | Tiefe Trommel + Brummen | Perkussion | Dumpf, tragend |
| Storm | 2 | E4 | Pfeifen + Flatterzunge | Bläser | Schnell, Triller |
| Bloom | 4 | G4 | Flöte + Blätterrascheln | Holzbläser | Weich, atmend |
| Frost | 6 | H4 | Glockenspiel + Reibglas | Idiophone | Klar, kühl, kurz |
| Void | Pause | – | Gefiltertes Rauschen (Pause) | Stille | Abwesenheit; erklingt als Lücke |
| Light | 7 | C5 | Celesta + Obertöne | Idiophone | Hell, schwebend |
| Venom | 3 | F4 | Klarinette (gedämpft) + Blubbern | Holzbläser | Schräg-gleitend (Portamento innerhalb der Skala) |
| Metal | 6 | H4 | Amboss + Saitenzupfen | Metall | Hart, präzise |
| Spirit | 2 | E4 | Stimme ohne Worte (hauchig) | Chor | Fern, hallend |
| Crystal | 5 | A4 | Klangschalen | Idiophone | Langer Nachklang |
| Sound | 1 | D4 | Reines Sinus-Ensemble (Oktaven) | Synthese | Vollkommen, sammelnd |
| Gravity | 1 | D4 | Subbass + Zug | Tiefbass | Sehr tief, langsam |
| Arcane | 4 | G4 | Harfe + rückwärts gespielte Töne | Saiten | Rätselhaft, Kanon |

| Größe | Oktave (Bezug M = 4) |
|---|---|
| XS | +2 |
| S | +1 |
| M | 0 |
| L | −1 |
| XL | −2 |
| XXL | −3 |

**Tempo:** aus der Klangmal-Beschreibung (K16 §3, z. B. „52 BPM in Ruhe“), sonst nach Größe (XS 96 … XXL 28 BPM). Emotion verschiebt das Tempo (Freude +20 %, Angst +40 %, Erschöpfung −50 %) – sichtbar gekoppelt an das Pulsieren des Klangmals.

**Sekundärtyp:** fügt einen Oberton mit der Klangfarbe des Sekundärtyps hinzu (eine Oktave + Quinte über dem Grundton, −12 dB).

### 5.2 Rufprofile (Auszug)

Alle 256 Arten haben ein generiertes Rufprofil (`EchoCalls.csv`), das Sound Design als Ausgangspunkt nimmt und je Art veredelt (Signaturlaute für Linien, Evolutionen, Ursprungsstimmen).

**Verdanthain**

| Art | Typ | Grundton | Tempo | Rhythmus | Klangfarbe |
|---|---|---|---|---|---|
| Fernlit | Bloom | G5 | 52 BPM | Rufreihe im festen Takt | Flöte + Blätterrascheln |
| Fernwyn | Bloom | G4 | 56 BPM | Rufreihe im festen Takt | Flöte + Blätterrascheln + Oberton Pfeifen |
| Verdrath | Bloom | G3 | 44 BPM | Rufreihe im festen Takt | Flöte + Blätterrascheln + Oberton Reines Sinus-Ensemble (Oktaven) |
| Brokk | Stone | D5 | 60 BPM | Einzelruf | Tiefe Trommel + Brummen |
| Brokkar | Stone | D4 | 90 BPM | Einzelruf | Tiefe Trommel + Brummen |
| Torgrath | Stone | D2 | 40 BPM | Einzelruf | Tiefe Trommel + Brummen + Oberton Subbass |
| Wisplet | Storm | E6 | 96 BPM | Rufreihe im festen Takt | Pfeifen + Flatterzunge |
| Galewix | Storm | E5 | 104 BPM | Einzelruf | Pfeifen + Flatterzunge |
| Zephyrion | Storm | E3 | 88 BPM | Einzelruf | Pfeifen + Flatterzunge + Oberton Celesta |
| Chimkin | Sound | D5 | 76 BPM | Einzelruf | Reines Sinus-Ensemble (Oktaven) |
| Chimbal | Sound | D4 | 56 BPM | Rufreihe im festen Takt | Reines Sinus-Ensemble (Oktaven) |
| Cantaroth | Sound | D3 | 44 BPM | Rufreihe im festen Takt | Reines Sinus-Ensemble (Oktaven) + Oberton Flöte |
| Lorncant | Spirit | E3 | 44 BPM | Rufreihe im festen Takt | Stimme ohne Worte (hauchig) + Oberton Reines Sinus-Ensemble (Oktaven) |
| Mossling | Bloom | G5 | 58 BPM | Einzelruf | Flöte + Blätterrascheln |

**Hvitfell**

| Art | Typ | Grundton | Tempo | Rhythmus | Klangfarbe |
|---|---|---|---|---|---|
| Snevel | Frost | H6 | 96 BPM | Einzelruf | Glockenspiel + Reibglas |
| Snevar | Frost | H5 | 72 BPM | Einzelruf | Glockenspiel + Reibglas |
| Snevrik | Frost | H4 | 56 BPM | Einzelruf | Glockenspiel + Reibglas + Oberton Celesta |
| Kjalf | Frost | H4 | 56 BPM | Einzelruf | Glockenspiel + Reibglas |
| Kjalmur | Frost | H3 | 44 BPM | Einzelruf | Glockenspiel + Reibglas + Oberton Tiefe Trommel |
| Kjalgrund | Frost | H2 | 36 BPM | Einzelruf | Glockenspiel + Reibglas + Oberton Tiefe Trommel |
| Uvlet | Frost | H6 | 96 BPM | Einzelruf | Glockenspiel + Reibglas |
| Uvarn | Frost | H5 | 72 BPM | Einzelruf | Glockenspiel + Reibglas + Oberton Stimme ohne Worte (hauchig) |
| Uvalis | Frost | H3 | 44 BPM | Einzelruf | Glockenspiel + Reibglas + Oberton Stimme ohne Worte (hauchig) |
| Uvasil | Void | Pause (Rauschen) | 44 BPM | Einzelruf | Gefiltertes Rauschen (Pause) + Oberton Glockenspiel |

**Ursprungsstimmen und Mythische:** eigene Kompositionen statt generierter Rufe; jede Ursprungsstimme spielt ihre Finale-Linie (§2.4) als Ruf.

### 5.3 Resonanzsturm-Quantisierung

Im Resonanzsturm ziehen alle Rufe auf die nächste Stufe der Aethrischen Skala (CANON §63). Das Ergebnis: Die ganze Welt klingt für ein bis zwei Spielstunden wie ein riesiger, ungeordneter Chor in derselben Tonart.

| Ruf (Cent über D4) | Nächste Stufe | Ziel | Verschiebung |
|---|---|---|---|
| -37 | 1 | D4 | +37 ct |
| 12 | 1 | D4 | -12 ct |
| 145 | 2 | E4 | +55 ct |
| 230 | 2 | E4 | -30 ct |
| 498 | 4 | G4 | +2 ct |
| 615 | 5 | A4 | +85 ct |
| 880 | 6 | H4 | +20 ct |
| 1022 | 7 | C5 | -22 ct |

Umsetzung: `Aethris::Audio::QuantizeToScaleCents` (GF_Audio); Referenz `aethris_music.quantize`.

### 5.4 Rufe im Spiel

| Situation | Ruf |
|---|---|
| Ruhe | Grundruf im Klangmal-Tempo, selten (alle 20–60 s) |
| Sänger | Rufreihe im festen Rhythmus (Kodex-Beobachtung „Sänger“) |
| Gruppe | Ruf-Antwort; Alpha tiefer und länger |
| Flucht | Kurzer, hoher Fluchtruf (+1 Oktave) |
| Jagd | Räuber still; Klangbiss als heller Glockenschlag (K52 §4) |
| Bindung | Grundton als Frequenzwelle (§7) |
| Erschöpft/Verstummt | Ruf bricht ab; verstummte Echos rufen nicht (Stille-Mix §8) |
| Begleiter | Reagiert auf den Spieler mit eigenem Ruf (Emotion) |

---

## 6. Welt und Ambient

| Schicht | Inhalt | Technik |
|---|---|---|
| Biom-Bett | Grundklang je Biom (Wald, Gebirge, Moor, Wüste, Vulkan, Küste, Schnee, Ruinen, Kristall, Himmel) | Stereo-Bett + 3D-Punktquellen |
| Tageszeit | Morgen-, Tag-, Abend-, Nachtfassung; Übergang über die Dämmerung (CANON §64) | Audio Modulation (Parameter `TimeOfDay`) |
| Wetter | Regen, Gewitter (Donner verzögert nach Blitzentfernung), Nebel (Dämpfung), Schnee (Hochpass auf Schritte), Hitze (Flirren), Sandsturm, Polarlicht (Chor-Hauch), Ascheregen | Parameter `Weather` |
| Echo-Präsenz | Rufe aus der Spawn-Population (K52) – die Welt klingt so belebt, wie sie ist | MassFar: Rufe als gepoolte Ein-Shots |
| Siedlung | Stimmengewirr nach Tagesablauf (K53), Handwerk, Glocken | Crowd-Bett + Barks |
| Orte | Wasserfälle, Brunnen (Klangbrunnen summen den Stadt-Ton), Resonanzsteine (Akkord der Region) | 3D-Emitter |

**Akustik:** Höhlen (Prismtiefen) mit Faltungshall je Kaverne; Ruinen mit frühen Reflexionen; Himmel mit sehr langem, dünnem Hall.

---

## 7. Resonanzsinn und Frequenz-Mechaniken

| Mechanik | Klang | Bild (DR-24) |
|---|---|---|
| Resonanzsinn halten | Welt wird leiser (−8 dB), Grundtöne der Echos/Objekte in Reichweite werden hörbar, Richtung über HRTF | Wellen im Raum, Form je Typ, Rhythmus je Entfernung |
| Hinweis (Quest) | Pulsierender Ton in Richtung des Hinweises, lauter beim Annähern | Stärker pulsierende Welle |
| Frequenzwelle (Bindung) | Grundton der Art im Klangmal-Takt; Gut-Fenster = Konsonanz, Perfekt = Oktave | Welle mit Fenster; Haptik |
| Anschlag | Im Fenster: Akkord (Grundton + Quinte); daneben: dumpfer Ton | Lichtblitz am Klangmal |
| Stillezone in Nähe | Gefilterte Welt, Pausen im Rhythmus der Wellen | Graue Ränder |
| Grundfrequenzen (Story) | Tiefer Ton unter allem (Nachklang) | Notenlinien (K44) |

Nach dem Ende „Neues Lied“ hört der Spieler die Grundfrequenzen nicht mehr (K46): Der Resonanzsinn wird zum **Resonator-Sinn** – gleiche Funktion, aber die Töne kommen aus dem Resonator (leicht metallischer Klang, Mono, ohne tiefen Grundton). Bei „Sanfte Stille“ bleibt der Sinn, ergänzt um das langsame Atmen der schlafenden Stimmen.

---

## 8. Stille als Klang

| Situation | Gestaltung |
|---|---|
| Stillezone | Hochpass ab 400 Hz, Dynamikkompression, Echos ohne Rufe, Musik = Stille-Motiv mit echten Pausen |
| Heilung einer Zone | Rückkehr aller Frequenzen in 4 s, beginnend mit dem Grundton; erster Ruf eines erwachten Echos ist der Weltlied-Ton 2 |
| Orte der Pause (K51 §7) | Jede 8 s eine Sekunde **vollkommene Stille** (alle Busse außer UI auf −∞) – im Takt, damit sie als Musik erkennbar ist |
| Velnox Phase 4 | Ein gehaltener Ton (D3, Streicher-Flageolett) bis zur Entscheidung |
| Riegel bricht | 4 s völlige Stille, dann ein einzelner tiefer Ton (K46 §10) |
| Orden | Stille als Gelübde: Ordensleute erzeugen keine Stimmen, nur Kreide, Schritte, Stoff |

**Regel:** Absolute Stille wird nur an gestalteten Stellen eingesetzt und dauert ≤ 4 s; sie wird im Untertitel als „[Stille]“ angezeigt (K54 §10).

---

## 9. Kampfklang

| Element | Gestaltung |
|---|---|
| Fähigkeiten | Klangfarbe des Typs (§5.1); Tonhöhe = Skalenstufe des Typs, Größe des Wirkenden bestimmt Oktave |
| Treffer | Effektivität hörbar: sehr effektiv = Konsonanz (Quinte), wenig effektiv = gedämpft; nie nur Klang (Zahlen + Wort, K54 §6) |
| Zeitleiste | Leises Ticken pro Zug, im Tempo der Kampfmusik quantisiert |
| Harmonie | Jede Stufe hebt einen Stem hinzu; 100 = Crescendo-Fanfare in der Tonart des Chors |
| Kombos | Zweiklang der beteiligten Typen (60-Tick-Fenster, K33) |
| Crescendo | Signatur je Art (K30), immer in D-Dorisch |
| Erschöpft („verklungen“) | Ruf bricht ab, Klangmal erlischt; nie Schmerz-/Todeslaute (ADR-007) |
| Status | Gift: leises Blubbern; Schlaf: langsamer Atem; Verwirrung: verstimmte Töne (einziger Ort, an dem die Skala bewusst verlassen wird) |

---

## 10. Stimme und Dialog

| Bereich | Regel |
|---|---|
| Sprachen | Vertonung DE, EN, JA, FR, ES; Text 12 Sprachen (CANON §24) |
| Umfang | Hauptquests voll; Nebenquests Kernzeilen (Auftrag, Wendung, Abschluss); Barks Schichten „Story“, „Fraktion“, „Allgemein“ (K53 §7.2) |
| Spielerstimme | Zwei Sprecherstimmen wählbar (K44 §2), kurze Antworten in drei Haltungen |
| Ilen | Überlagert im Finale die Spielerstimme (beide Sprecher; K46 §6) – eigene Aufnahme je Sprecherstimme |
| Schweigegelübde | Ordensleute im Kloster: keine Stimme, nur Kreide auf Schiefertafel + Untertitel (CANON §55) |
| Echos | Keine Wörter, nie; nonverbale Laute (K44 §2) |
| Casting-Richtlinien | Ysolde: ruhig, trocken, tief; Kael: schnell, hell, kontrolliert; Venn: warm, präzise, nie bedrohlich laut; Sereth: leise, langsam, klar; Tavesh: rau, leidenschaftlich; Marieke: lachend, schnell rechnend |
| Lip-Sync | Prozedural (Audio-gesteuert) für alle Sprachen; Hauptszenen in DE/EN zusätzlich nachbearbeitet |

---

## 11. Mix und Lautheit

| Name | Parent | Priority | DefaultDb | MaxVoicesPS5 | MaxVoicesSwitch2 | Duck | Notes |
|---|---|---|---|---|---|---|---|
| BUS_MASTER | – | 1 | 0 | 192 | 96 | – |  |
| BUS_DIALOG | BUS_MASTER | 1 | 0 | 8 | 6 | BUS_MUSIC:-6|BUS_AMBIENT:-4|BUS_ECHO:-3 | Untertitel immer synchron |
| BUS_MUSIC | BUS_MASTER | 2 | -4 | 24 | 16 | – | Stems über Quartz |
| BUS_ECHO | BUS_MASTER | 2 | -2 | 48 | 24 | – | Rufe der Echos (MetaSounds) |
| BUS_COMBAT | BUS_MASTER | 2 | -1 | 40 | 20 | BUS_AMBIENT:-6 | Fähigkeiten, Treffer |
| BUS_SENSE | BUS_MASTER | 1 | 0 | 8 | 6 | BUS_AMBIENT:-6|BUS_ECHO:-3 | Resonanzsinn, Frequenzwelle – Gameplay-Signale haben Vorrang |
| BUS_AMBIENT | BUS_MASTER | 3 | -6 | 48 | 24 | – | Biom, Wetter, Stadt |
| BUS_UI | BUS_MASTER | 2 | -6 | 8 | 6 | – | Weltlied-Skala |
| BUS_BARK | BUS_DIALOG | 3 | -2 | 4 | 2 | – | Barks (globaler Cooldown K53) |

| Ziel | Wert |
|---|---|
| Integrierte Lautheit (Konsole/PC) | −16 LUFS ±1 (Gameplay-Mittel), Dialog-Anker −23 LUFS integriert für Szenen |
| Handheld (Switch 2) | −14 LUFS, Profil „Kopfhörer/Lautsprecher“ |
| True Peak | ≤ −1 dBTP |
| Dynamikprofile | Heimkino / Fernseher / Nachtmodus (komprimiert) / Kopfhörer (HRTF) |
| Priorität | Gameplay-Signale (Resonanzsinn, Frequenzwelle) > Dialog > Kampf > Echo-Rufe > Musik > Ambient |

---

## 12. Technik

| Baustein | Einsatz |
|---|---|
| **MetaSounds** | Echo-Rufe (ein Patch je Typ `MSS_Type_<Typ>`, Parameter aus `EchoCalls.csv`), Frequenzwelle, Resonanzsinn, Stille-Filter |
| **Quartz** | Musikübergänge auf Schlag/Takt, Zeitleisten-Ticks, Orte der Pause, Glocken in Städten |
| **Audio Modulation** | Parameter `TimeOfDay`, `Weather`, `Harmony`, `SilenceProximity`, `StormActive` |
| **Submixes** | Busse §11, Hall je Akustikzone |
| **GF_Audio** | `EAethrisMusicState`, `FEchoCallProfile`, `Aethris::Audio::QuantizeToScaleCents`; hört auf Events (Kampf, Wetter, Quest, Zone) – keine Abhängigkeit zu Feature-Plugins (Presentation-Schicht) |
| **Streaming** | Musik-Stems gestreamt (Opus), Rufe/SFX im Speicher je Region (Region wechselt → Bank wechselt) |

**Budgets:**

| Messgröße | PS5 | Switch 2 | PC (Min-Spec) |
|---|---|---|---|
| Audio-CPU (Render) | ≤ 1,5 ms | ≤ 2,5 ms | ≤ 2,0 ms |
| Gleichzeitige Stimmen | 192 | 96 | 160 |
| Audio-Speicher | ≤ 450 MB | ≤ 220 MB | ≤ 500 MB |
| MetaSounds-Instanzen gleichzeitig | 64 | 32 | 48 |

---

## 13. Barrierefreiheit

| Option (K54 §10) | Audio-Seite |
|---|---|
| Untertitel „Dialog + Klänge“ | Jeder relevante Klang hat einen Untertitel-Text (`[ruft dreimal kurz]`, `[Stille]`, `[Donner, fern]`) |
| Klangradar | Richtungspfeile für Rufe, Fluchtrufe, Gefahren |
| Visuelle Klangsignale | Pflicht; nicht abschaltbar |
| Mono | Downmix ohne HRTF-Artefakte |
| Hochkontrast-Resonanzsinn | Wellen stärker; Audio unverändert |
| Haptik | Frequenzwelle und Resonanzsinn als Vibrationsmuster (abschaltbar) |
| Tinnitus-schonend | Option begrenzt hohe Frequenzen > 8 kHz und Stille-Effekte (keine harten Abbrüche) |

---

## 14. Produktion

| Umfang | Ziel |
|---|---|
| Musik | ~240 min (10 Regionsthemen × Tag/Nacht, 10 Stadtthemen, 10 Arenen, 12 Bosse, Leitmotive, Szenen), als Stems |
| Echo-Rufe | 256 Arten × 6 Zustände (Ruhe, Ruf, Flucht, Freude, Kampf, Erschöpft) ≈ 1.536 Varianten aus 15 Typ-Patches |
| Fähigkeiten | 330 Fähigkeiten (K28–K30) × 2 Schichten (Wirken, Treffer) |
| Ambient | 10 Biome × 4 Tageszeiten × 9 Wetter (Kombination über Schichten) |
| Dialog | ~60.000 Wörter Hauptstory, ~120.000 Nebenquests, ~4.000 Barks + 1.200 Ende-Varianten (Text); VO-Umfang in 5 Sprachen ≈ 38 h je Sprache |
| Namenskonvention | `SW_` (Sound Wave), `MSS_` (MetaSound Source), `MSP_` (Patch), `SC_` (Sound Class), `SM_Q_` (Quartz Clock) – CANON §23 |

**Pipeline:** Komposition in D-Dorisch mit Fragmentpflicht (§3.1) → Stem-Export → Quartz-Markierungen → Integration → Mix-Pass je Region → Lautheitsprüfung (automatisch, CI) → Barrierefreiheits-Pass (Untertitel für Klänge) → Stummschalt-Durchlauf (K66).

---

## 15. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Art/VFX | Klangmal-Puls synchron zum Ruf-Tempo; Frequenzwelle als Shader; Stille-Entsättigung | K56, K58 |
| Animation | Rufanimationen synchron (Mund/Klangmal), Emotionstempo | K57 |
| Programmierung | Audio-Events aus Kampf, Wetter, Zonen, Quests; Musikzustands-Prioritäten | K06, K65 |
| Narrative | Untertitel-Texte für Klänge; Casting-Profile | K44–K53 |
| QA | Lautheitsprüfung, Stummschalt-Durchlauf, Sturm-Quantisierung (Hörtest), Voice-Stealing-Test in Städten | K66 |
| Lokalisierung | VO-Pipeline 5 Sprachen, Lip-Sync | K66 |

---

## 16. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-211 | Weltlied-Motiv D–A–G–F–E–C–D in D-Dorisch als verbindlicher Kern aller Musik und Rufe | Ein Klang für die ganze Welt; Stadtfragmente und Finale werden ableitbar | freie Tonarten je Region |
| ADR-212 | Echo-Rufe werden aus Typ, Größe und Klangmal generiert und von Sound Design veredelt | 256 Arten konsistent; Rufe passen zur Skala; Aufwand beherrschbar | 256 handgemachte Rufsätze ohne System |
| ADR-213 | Gameplay-Signale (Resonanzsinn, Frequenzwelle) haben Mix-Vorrang vor Dialog | Klang ist Spielmechanik; DR-24 sichert die visuelle Entsprechung | Dialog immer oben |
| ADR-214 | Absolute Stille nur gestaltet, ≤ 4 s, mit Untertitel | Stille ist Inhalt, darf aber nie wie ein Fehler wirken | lange Stille-Passagen |
| ADR-215 | Verwirrung ist der einzige Zustand, der die Skala verlässt | Hörbare Ausnahme macht den Status sofort erkennbar | verstimmte Welt im Sturm |

---

## 17. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §212 | Weltlied-Motiv D4–A4–G4–F4–E4–C5–D5 (Dauern 2/1/1/1,5/0,5/2/3), Aethrische Skala D-Dorisch, Ableitungen (Umkehrung, Krebs, Arpeggio, Stille, Krone), Finale-Linien der zehn Stimmen | LOCKED |
| §213 | Leitmotive (`Leitmotifs.csv`), Regionsthemen mit Fragmentpflicht | LOCKED |
| §214 | Adaptive Musik (`MusicStates.csv`): Prioritäten, Quartz-Übergänge, Atem-Regel, Harmonie-Stufen | LOCKED |
| §215 | Echo-Rufe: Typ → Stufe/Klangfarbe (`TypeTones.csv`), Größe → Oktave, Klangmal → Tempo; `EchoCalls.csv` (256); Sturm-Quantisierung | LOCKED |
| §216 | Stille-Gestaltung, Mix (`MixBuses.csv`, −16 LUFS, ≤ −1 dBTP), Technik (MetaSounds, Quartz, Modulation), Budgets | LOCKED |
| §10 | ADR-211 – ADR-215 | LOCKED |

---

## 18. Kapitel-Checkliste

- [x] Leitbild, Weltlied-Motiv, Skala, Ableitungen, zehn Stimmen, Stadtfragmente
- [x] Leitmotive und Regionsthemen
- [x] Adaptive Musik mit Zuständen und Übergängen
- [x] Echo-Rufe (Typ-Töne, Profile für 256 Arten, Sturm-Quantisierung)
- [x] Ambient, Resonanzsinn, Stille, Kampfklang
- [x] Stimme, Dialog, Casting, Mix, Lautheit
- [x] Technik, Budgets, Barrierefreiheit, Produktion
- [x] Anforderungen, ADR-211 – ADR-215, CANON §212–§216

➡️ **Nächstes Kapitel: K56 – Art Bible.**
