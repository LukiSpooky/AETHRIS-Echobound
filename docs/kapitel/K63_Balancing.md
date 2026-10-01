# K63 · Balancing

| Feld | Wert |
|---|---|
| Dokument | Kapitel 63 von 68 · Systeme-Abschluss |
| Version | 1.0 |
| Owner | Lead Systems Designer, Balancing Analyst |
| Mitwirkende | Lead Combat Designer, Economy Designer, Data Scientist, Creature Design Lead, QA Lead (Playtests), Lead Online Designer |
| Baut auf | K02 §9 (Korridore, Arena-Stufen vorläufig), K16–K19 (Werte, Formeln, Evolution), K17 (Typen), K28–K36 (Kampf, KI, Bindung), K42 (Wirtschaft), K43 (Wärterrang), K52 (Ökologie), K60–K62 (Koop, PvP, Endgame) |
| Status | ✅ Freigegeben |
| Im Repository | `tools/ref/aethris_balance.py` (BL-01–BL-07), `Data/Balance/StatAccents.csv` (131 Identitätsakzente), `ArenaTiers.csv` (Q13), `TuningKnobs.csv`; Katalogkapitel K20–K27 neu erzeugt (`tools/authoring/regen_catalog.py`); Hook in `catalog_lib.write` |
| Neue Kanon-Einträge | CANON §248 (Balancing-Methode), §249 (Identitätsakzente), §250 (Arena-Stufen, Q13), §251 (Tuning-Knöpfe, Live-Balancing, Playtests); Q13 geschlossen |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Methode](#2-methode)
3. [Identitätsakzente: keine Zwillinge im Katalog](#3-identitätsakzente-keine-zwillinge-im-katalog)
4. [Arena-Stufen – Entscheidung Q13](#4-arena-stufen--entscheidung-q13)
5. [Kampf](#5-kampf)
6. [Fortschritt und Wirtschaft](#6-fortschritt-und-wirtschaft)
7. [Schwierigkeitsgrade](#7-schwierigkeitsgrade)
8. [Tuning-Knöpfe](#8-tuning-knöpfe)
9. [Live-Balancing](#9-live-balancing)
10. [Playtests](#10-playtests)
11. [Prüfregeln](#11-prüfregeln)
12. [Anforderungen an andere Abteilungen](#12-anforderungen-an-andere-abteilungen)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Ziele

Balancing in AETHRIS bedeutet nicht „alles gleich stark“, sondern: **Jede Entscheidung hat Gewicht, und jede Art hat einen Platz.**

| Ziel | Bedeutung | Messbar an |
|---|---|---|
| **BZ-1 Lesbare Stärke** | Spielende können Stärke abschätzen: Level, Typ, Zeitleiste erklären Ergebnisse | Kampfdauer stabil über alle Level (§5.1) |
| **BZ-2 Identität** | Keine zwei Arten sind Zahlenzwillinge; jede hat ein Profil, das zu Typ und Rolle passt | BL-01 (0 Dubletten) |
| **BZ-3 Fortschrittsgefühl** | Arenen fordern, ohne zu blockieren; Überleveln in der Welt wird spürbar belohnt (K02 §9.2) | Arena-Verhältnis 1,00–1,12 (BL-03) |
| **BZ-4 Vielfalt** | Viele Typen, Rollen und Strategien sind tragfähig | Typbilanz (BL-04), Meta-Signale (K61 §7) |
| **BZ-5 Kein Grind-Zwang** | Ziele sind in angemessener Zeit erreichbar | Wärterrang, Wirtschaft, Endgame-Zeiten (§6, K62) |
| **BZ-6 Fairness** | Keine Glückswürfe, die über Sieg und Niederlage entscheiden (DR-07) | Trefferchance gedeckelt 500–1.000 ‰, Volltreffer 4,2 % |

---

## 2. Methode

Balancing ist in AETHRIS **datengetrieben und prüfbar**. Jede Zahl steht in `Data/**/*.csv` (CANON §31), jede Formel hat ein Referenzmodell in Python, das mit dem C++-Code übereinstimmt, und jede Annahme hat eine Prüfregel.

```
Daten (CSV) ──► Referenzmodelle (tools/ref) ──► Prüfregeln (CI) ──► Simulationen ──► Playtests ──► Telemetrie
     ▲                                                                                                   │
     └───────────────────────────── Tuning-Knöpfe (TuningKnobs.csv, nur per Patch) ◄─────────────────────┘
```

| Modell | Inhalt | Kapitel |
|---|---|---|
| `aethris_stats.py` | Statusformeln, EP-Kurven, Trefferchance | K18 |
| `aethris_combat.py` | Zeitleiste, Schaden, Duell-Simulation | K31, K32 |
| `aethris_ai.py` | Kampf-KI-Profile, Duell-Matrix | K34 |
| `aethris_bond.py` | Resonanz, Timingfenster, Bindungsausgang | K36 |
| `aethris_genetics.py` | Anlagen, Loci, Morphs | K38 |
| `aethris_economy.py` | Sol-Einnahmen, Bedarf, Preise | K42 |
| `aethris_progression.py` | Wärterrang-Zeitlinie | K43 |
| `aethris_ecology.py` | Populationen, Nahrungsnetz | K52 |
| `aethris_pvp.py` | Normalisierung, Glicko-2 | K61 |
| `aethris_endgame.py` | Tiefen, Klangstimmung, Level 70 → 100 | K62 |
| **`aethris_balance.py`** | Identitätsakzente, Arenen, Typbilanz, Fähigkeitsbudget, Tuning-Knöpfe | K63 |

---

## 3. Identitätsakzente: keine Zwillinge im Katalog

### 3.1 Befund

Die Katalogkapitel K20–K27 erzeugen Basiswerte aus **Rolle × Kernsumme × Profil** (`catalog_lib.distribute`). Das ist robust und hält die Kernsummen-Spannen (CANON §71) ein – führt aber dazu, dass Arten mit gleicher Rolle, gleicher Kernsumme und gleichem Profil **identische Basiswerte** erhalten. Die Prüfung ergab **54 Gruppen** mit insgesamt 131 betroffenen Arten (z. B. Pyroluth und Skriveth, aufgefallen in K61). Mechanisch ist das kein Fehler; für die Identität (BZ-2) und für das Ranked (wo nur Werte, Typen und Fähigkeiten zählen) ist es eine Schwäche.

### 3.2 Lösung: Identitätsakzent

Jede Art außer der ersten einer Gruppe erhält einen **Akzent**: Der Leitwert ihres Primärtyps steigt um Δ, der höchste übrige Kernwert sinkt um Δ. Kernsumme, PRÄ und AUS bleiben gleich; Δ beginnt bei 2 und steigt, bis die Werte im ganzen Katalog einmalig sind (max. 8).

| Primärtyp | Leitwert | Begründung (Kernmechanik K17) |
|---|---|---|
| Glut, Leere, Licht, Arkan | Spez.-Angriff | Brand, Entzug, Strahlen, Glyphen |
| Flut, Frost, Kristall | Spez.-Verteidigung | Heilung über Zeit, Kälte, Lichtbrechung |
| Stein, Gift | Verteidigung | Schilde, zähe Drüsen |
| Sturm, Geist, Klang | Geschwindigkeit | Tempo, Unschärfe, Rhythmus |
| Blüte, Schwerkraft | HP | Wachstum, Masse |
| Metall | Angriff | Klingen |

Alle 131 Akzente:

| Art | Dublette von | Primärtyp | Akzent | Δ |
|---|---|---|---|---|
| Nubilo (#226) | Fernwyn | Light | SpAttack 72→74, SpDefense 82→80 | 2 |
| Marwyn (#086) | Galewix | Tide | SpDefense 61→63, Speed 100→98 | 2 |
| Brisel (#092) | Galewix | Storm | Speed 100→103, Attack 79→76 | 3 |
| Aschund (#142) | Galewix | Ember | SpAttack 72→76, Speed 100→96 | 4 |
| Snevar (#158) | Galewix | Frost | SpDefense 61→66, Speed 100→95 | 5 |
| Klirrflug (#200) | Galewix | Crystal | SpDefense 61→67, Speed 100→94 | 6 |
| Cirrhawk (#223) | Galewix | Storm | Speed 100→107, Attack 79→72 | 7 |
| Maraune (#087) | Zephyrion | Tide | SpDefense 75→77, Speed 124→122 | 2 |
| Brision (#093) | Zephyrion | Storm | Speed 124→127, Attack 97→94 | 3 |
| Aschgrim (#143) | Zephyrion | Ember | SpAttack 88→92, Speed 124→120 | 4 |
| Snevrik (#159) | Zephyrion | Frost | SpDefense 75→80, Speed 124→119 | 5 |
| Klirrathan (#201) | Zephyrion | Crystal | SpDefense 75→81, Speed 124→118 | 6 |
| Tetri (#037) | Chimkin | Gravity | HP 52→54, SpAttack 59→57 | 2 |
| Mirel (#060) | Chimbal | Venom | Defense 71→73, SpAttack 81→79 | 2 |
| Glyphaune (#017) | Cantaroth | Arcane | SpAttack 100→102, SpDefense 91→89 | 2 |
| Sigilaune (#068) | Cantaroth | Arcane | SpAttack 100→103, SpDefense 91→88 | 3 |
| Mystdral (#097) | Cantaroth | Arcane | SpAttack 100→104, SpDefense 91→87 | 4 |
| Dunkalb (#114) | Mossling | Stone | Defense 68→70, HP 63→61 | 2 |
| Kjalf (#160) | Mossling | Frost | SpDefense 58→61, Defense 68→65 | 3 |
| Nimbel (#219) | Mossling | Storm | Speed 42→46, Defense 68→64 | 4 |
| Cragar (#034) | Myrthorn | Stone | Defense 93→95, HP 86→84 | 2 |
| Undfin (#063) | Myrthorn | Tide | SpDefense 79→82, Defense 93→90 | 3 |
| Irrlit (#065) | Lumpip | Spirit | Speed 60→62, SpAttack 70→68 | 2 |
| Aquapip (#094) | Lumpip | Tide | SpDefense 52→55, SpAttack 70→67 | 3 |
| Uvlet (#163) | Lumpip | Frost | SpDefense 52→56, SpAttack 70→66 | 4 |
| Aerlet (#098) | Sporlet | Storm | Speed 57→59, SpAttack 65→63 | 2 |
| Aerluna (#099) | Sporix | Storm | Speed 81→83, SpAttack 94→92 | 2 |
| Tangix (#107) | Sporix | Venom | Defense 82→85, SpAttack 94→91 | 3 |
| Qadrant (#133) | Sporix | Metal | Attack 65→69, SpAttack 94→90 | 4 |
| Rimlet (#050) | Skirmote | Frost | SpDefense 48→50, Speed 79→77 | 2 |
| Virmote (#072) | Skirmote | Venom | Defense 45→48, Speed 79→76 | 3 |
| Mullit (#211) | Thornkin | Metal | Attack 78→80, Speed 72→70 | 2 |
| Graupel (#237) | Thornkin | Frost | SpDefense 49→52, Attack 78→75 | 3 |
| Mullhorn (#212) | Thorncoil | Metal | Attack 111→113, Speed 103→101 | 2 |
| Menhirok (#197) | Orbeloth | Stone | Defense 106→108, HP 98→96 | 2 |
| Undrath (#064) | Kraggoth | Tide | SpDefense 96→98, Defense 114→112 | 2 |
| Tidrex (#090) | Anchrex | Tide | SpDefense 92→94, SpAttack 101→99 | 2 |
| Skarabon (#119) | Anchrex | Gravity | HP 88→91, SpAttack 101→98 | 3 |
| Uvasil (#166) | Anchrex | Void | SpAttack 101→105, SpDefense 92→88 | 4 |
| Tikkoran (#187) | Anchrex | Metal | Attack 70→75, SpAttack 101→96 | 5 |
| Ligravor (#208) | Anchrex | Gravity | HP 88→94, SpAttack 101→95 | 6 |
| Nubisk (#228) | Anchrex | Void | SpAttack 101→108, SpDefense 92→85 | 7 |
| Tidel (#089) | Tetrel | Tide | SpDefense 75→77, SpAttack 82→80 | 2 |
| Skaral (#118) | Tetrel | Gravity | HP 72→75, SpAttack 82→79 | 3 |
| Tikkar (#186) | Tetrel | Metal | Attack 57→61, SpAttack 82→78 | 4 |
| Ligrath (#207) | Tetrel | Gravity | HP 72→77, SpAttack 82→77 | 5 |
| Gratrex (#045) | Forgoth | Storm | Speed 112→114, Attack 120→118 | 2 |
| Marlit (#085) | Gratkin | Tide | SpDefense 44→46, Speed 72→70 | 2 |
| Stonlet (#100) | Lithi | Stone | Defense 74→76, HP 68→66 | 2 |
| Brinshell (#077) | Lithshell | Tide | SpDefense 92→94, Defense 108→106 | 2 |
| Torfgor (#084) | Lithshell | Stone | Defense 108→111, HP 100→97 | 3 |
| Stonshell (#101) | Lithshell | Stone | Defense 108→112, HP 100→96 | 4 |
| Mesakor (#132) | Lithshell | Stone | Defense 108→113, HP 100→95 | 5 |
| Vardholm (#171) | Lithshell | Stone | Defense 108→114, HP 100→94 | 6 |
| Voltarn (#154) | Rimpaw | Metal | Attack 92→94, Speed 116→114 | 2 |
| Emblit (#054) | Quarling | Ember | SpAttack 80→82, Speed 69→67 | 2 |
| Umbrling (#078) | Quarling | Void | SpAttack 80→83, Speed 69→66 | 3 |
| Eidrun (#172) | Quarling | Spirit | Speed 69→73, SpAttack 80→76 | 4 |
| Optil (#195) | Quarling | Light | SpAttack 80→85, Speed 69→64 | 5 |
| Facetin (#209) | Quarling | Crystal | SpDefense 60→66, SpAttack 80→74 | 6 |
| Misslit (#213) | Quarling | Void | SpAttack 80→87, Speed 69→62 | 7 |
| Tintel (#231) | Quarling | Sound | Speed 69→77, SpAttack 80→72 | 8 |
| Umbracoil (#079) | Quarcoil | Void | SpAttack 115→117, Speed 99→97 | 2 |
| Optikor (#196) | Quarcoil | Gravity | HP 74→77, SpAttack 115→112 | 3 |
| Facettor (#210) | Quarcoil | Crystal | SpDefense 87→91, SpAttack 115→111 | 4 |
| Nucleox (#156) | Dawnix | Gravity | HP 75→77, SpAttack 117→115 | 2 |
| Eidwacht (#173) | Dawnix | Spirit | Speed 100→103, SpAttack 117→114 | 3 |
| Kronvaal (#198) | Dawnix | Arcane | SpAttack 117→121, Speed 100→96 | 4 |
| Missgrath (#214) | Dawnix | Void | SpAttack 117→122, Speed 100→95 | 5 |
| Tintabul (#232) | Dawnix | Sound | Speed 100→106, SpAttack 117→111 | 6 |
| Astraviel (#240) | Dawnix | Arcane | SpAttack 117→124, Speed 100→93 | 7 |
| Humbog (#083) | Memoro | Sound | Speed 71→73, SpDefense 90→88 | 2 |
| Miasmar (#217) | Runkar | Venom | Defense 80→82, SpAttack 92→90 | 2 |
| Tidling (#088) | Mirepip | Tide | SpDefense 53→55, SpAttack 58→56 | 2 |
| Skarit (#117) | Mirepip | Gravity | HP 51→54, SpAttack 58→55 | 3 |
| Tikkel (#185) | Mirepip | Metal | Attack 41→45, SpAttack 58→54 | 4 |
| Ligrel (#206) | Mirepip | Gravity | HP 51→56, SpAttack 58→53 | 5 |
| Ambolt (#138) | Undling | Metal | Attack 47→49, Defense 67→65 | 2 |
| Obsikin (#144) | Undling | Stone | Defense 67→70, HP 62→59 | 3 |
| Thaelit (#182) | Undling | Arcane | SpAttack 36→40, Defense 67→63 | 4 |
| Spatling (#203) | Undling | Crystal | SpDefense 57→62, Defense 67→62 | 5 |
| Aquafin (#095) | Irrel | Tide | SpDefense 74→76, SpAttack 99→97 | 2 |
| Aquadral (#096) | Irraune | Tide | SpDefense 91→93, SpAttack 121→119 | 2 |
| Sengel (#120) | Blossi | Ember | SpAttack 36→38, Attack 70→68 | 2 |
| Sarkel (#188) | Blossi | Spirit | Speed 65→68, Attack 70→67 | 3 |
| Solvar (#112) | Blossar | Light | SpAttack 50→52, Attack 97→95 | 2 |
| Klirrnox (#202) | Blossmire | Void | SpAttack 61→63, Attack 118→116 | 2 |
| Fumel (#149) | Blightkin | Void | SpAttack 66→68, SpDefense 60→58 | 2 |
| Glazil (#176) | Blightkin | Crystal | SpDefense 60→63, SpAttack 66→63 | 3 |
| Tilgel (#191) | Blightkin | Void | SpAttack 66→70, SpDefense 60→56 | 4 |
| Psionit (#215) | Blightkin | Arcane | SpAttack 66→71, SpDefense 60→55 | 5 |
| Levitel (#235) | Blightkin | Gravity | HP 58→64, SpAttack 66→60 | 6 |
| Glazvind (#177) | Blightar | Storm | Speed 82→84, SpAttack 95→93 | 2 |
| Vardlit (#170) | Brinlet | Stone | Defense 75→77, HP 69→67 | 2 |
| Drusil (#151) | Weidlit | Crystal | SpDefense 66→68, HP 63→61 | 2 |
| Hymlit (#193) | Weidlit | Sound | Speed 52→55, SpDefense 66→63 | 3 |
| Harfel (#229) | Weidlit | Sound | Speed 52→56, SpDefense 66→62 | 4 |
| Drusaro (#152) | Weiduna | Crystal | SpDefense 95→97, HP 91→89 | 2 |
| Hymnora (#194) | Weiduna | Sound | Speed 74→77, SpDefense 95→92 | 3 |
| Harfion (#230) | Weiduna | Sound | Speed 74→78, SpDefense 95→91 | 4 |
| Aschwel (#141) | Brikin | Ember | SpAttack 51→53, Speed 71→69 | 2 |
| Snevel (#157) | Brikin | Frost | SpDefense 43→46, Speed 71→68 | 3 |
| Klirrit (#199) | Brikin | Crystal | SpDefense 43→47, Speed 71→67 | 4 |
| Cirrel (#222) | Brikin | Storm | Speed 71→76, Attack 56→51 | 5 |
| Vitrapha (#130) | Glimar | Light | SpAttack 81→83, SpDefense 93→91 | 2 |
| Vitrel (#129) | Tangi | Light | SpAttack 57→59, SpDefense 65→63 | 2 |
| Ambrak (#139) | Dunhorn | Metal | Attack 66→68, Defense 95→93 | 2 |
| Obsidar (#145) | Dunhorn | Stone | Defense 95→98, HP 88→85 | 3 |
| Kjalmur (#161) | Dunhorn | Frost | SpDefense 81→85, Defense 95→91 | 4 |
| Thaelon (#183) | Dunhorn | Spirit | Speed 59→64, Defense 95→90 | 5 |
| Spatwurm (#204) | Dunhorn | Crystal | SpDefense 81→87, Defense 95→89 | 6 |
| Nimbor (#220) | Dunhorn | Storm | Speed 59→66, Defense 95→88 | 7 |
| Tysvorn (#178) | Stacharon | Void | SpAttack 58→60, Attack 113→111 | 2 |
| Graupix (#238) | Stacharon | Crystal | SpDefense 71→74, Attack 113→110 | 3 |
| Volket (#153) | Sirrkorn | Storm | Speed 80→82, Attack 63→61 | 2 |
| Hallkid (#174) | Sirrkorn | Sound | Speed 80→83, Attack 63→60 | 3 |
| Hallbrand (#175) | Sirrsturm | Sound | Speed 115→117, Attack 91→89 | 2 |
| Holmel (#233) | Mesakil | Gravity | HP 70→72, Defense 76→74 | 2 |
| Skriv (#179) | Pyrolm | Arcane | SpAttack 71→73, Speed 61→59 | 2 |
| Uvarn (#164) | Pyrolax | Frost | SpDefense 75→77, SpAttack 100→98 | 2 |
| Skrivar (#180) | Pyrolax | Arcane | SpAttack 100→103, Speed 86→83 | 3 |
| Uvalis (#165) | Pyroluth | Frost | SpDefense 92→94, SpAttack 122→120 | 2 |
| Skriveth (#181) | Pyroluth | Arcane | SpAttack 122→125, Speed 105→102 | 3 |
| Kjalgrund (#162) | Obsidrax | Frost | SpDefense 99→101, Defense 117→115 | 2 |
| Thaelarch (#184) | Obsidrax | Spirit | Speed 72→75, Defense 117→114 | 3 |
| Spathorn (#205) | Obsidrax | Crystal | SpDefense 99→103, Defense 117→113 | 4 |
| Nimbaroth (#221) | Obsidrax | Storm | Speed 72→77, Defense 117→112 | 5 |
| Tilgrath (#192) | Fumaroth | Void | SpAttack 96→98, SpDefense 88→86 | 2 |
| Psioneth (#216) | Fumaroth | Arcane | SpAttack 96→99, SpDefense 88→85 | 3 |
| Levithar (#236) | Fumaroth | Arcane | SpAttack 96→100, SpDefense 88→84 | 4 |
| Nubi (#225) | Lyskin | Light | SpAttack 51→53, SpDefense 58→56 | 2 |

Die Akzente stehen in `Data/Balance/StatAccents.csv` mit Ausgangs- und Zielwert. Sie werden idempotent angewendet – durch `aethris_balance.py accent` und automatisch beim Schreiben des Katalogs (`catalog_lib.write`), damit ein erneutes Erzeugen der Katalogdaten sie nicht verliert. Die Katalogkapitel K20–K27 sind mit `regen_catalog.py` neu erzeugt; der Katalog-Validator meldet 0 Verstöße.

---

## 4. Arena-Stufen – Entscheidung Q13

### 4.1 Modell

K02 §9.2 legte eine vorläufige Tabelle fest. K63 leitet die endgültige Tabelle aus drei Annahmen ab:

1. **Erwartetes Spielerlevel** beim Arenabesuch folgt den Korridoren (Akt I 5–28, Akt II 25–55, Akt III 50–70) und der Story-Zeitlinie (Arenabesuch nach 5/9/13/18/23/28/33/38/44/50 Spielstunden).
2. **Arena-Team:** Ass = Erwartung + 1 (Akt I) bzw. + 2 (Akt II/III); übrige Echos 2 Level darunter.
3. **Stärke** skaliert mit (L + 10)², weil Angriff und Verteidigung je linear mit L + 10 wachsen (K18). Das Spielerteam liegt im Mittel 1 Level unter der Erwartung.

Ziel ist ein **Stärkeverhältnis Arena/Spieler von 1,00–1,12**: fordernd, aber ohne Pflicht zum Grinden. Wer in der Welt ein paar Level mehr sammelt, spürt den Vorteil sofort (BZ-3).

### 4.2 Ergebnis

| Stufe | Ass-Level (vorläufig K02) | **Ass-Level (final)** | Chorgröße | Format | Erwartetes Spielerlevel | Stärkeverhältnis Arena/Spieler | Erwarteter Wärterrang |
|---|---|---|---|---|---|---|---|
| 1 | 12 | **14** | 3 | Duell | 13 | 1,06 | 7 |
| 2 | 17 | **19** | 4 | Duell | 18 | 1,04 | 11 |
| 3 | 22 | **24** | 4 | Duo | 23 | 1,03 | 14 |
| 4 | 27 | **29** | 5 | Duell | 28 | 1,02 | 16 |
| 5 | 33 | **36** | 5 | Duo | 34 | 1,07 | 19 |
| 6 | 39 | **43** | 5 | Trio | 41 | 1,06 | 21 |
| 7 | 45 | **50** | 6 | Duell | 48 | 1,05 | 23 |
| 8 | 51 | **56** | 6 | Duo | 54 | 1,04 | 24 |
| 9 | 59 | **63** | 6 | Trio | 61 | 1,04 | 27 |
| 10 | 67 | **70** | 6 | Trio | 68 | 1,03 | 29 |

Die Tabelle ist in `Data/Balance/ArenaTiers.csv` gespeichert und ersetzt die vorläufige Tabelle aus K02 §9.2. Gegenüber dem Entwurf steigen die Ass-Level um 2–5, vor allem in Akt II/III: Die vorläufigen Werte lagen unter dem Erwartungswert und hätten Arenen zu leicht gemacht (Verhältnis < 1).

**Formate und Freischaltungen:** Duo ist ab Wärterrang 5, Trio ab 10 freigeschaltet (CANON §17). Nach der Rang-Zeitlinie (K43) haben Spielende beim Arenabesuch mit Duo-/Trio-Format diesen Rang immer erreicht (BL-06); die Leihbegleitung (ADR-121) bleibt als Sicherheitsnetz für ungewöhnliche Spielweisen.

**Skalierte Arenen (Akt I/II):** Die Stufe einer frei wählbaren Arena wird beim ersten Betreten fixiert (ADR-054) – Clamp(Akkorde + 1, 2, 4) bzw. Clamp(Akkorde + 1, 5, 8). Die Tabelle gilt je Stufe, nicht je Ort.

---

## 5. Kampf

### 5.1 Kampfdauer über alle Level

Die Zeitleisten- und Schadensformeln sollen Kämpfe auf jedem Level ähnlich lang halten (BZ-1, DR-11). Simulation zufälliger 1-gegen-1-Begegnungen (gleiches Level, Stärke 70, Zeitkosten 100, `aethris_combat.py`):

| Level | Ø Züge gesamt (1v1) | Median | P90 | Ø Ticks | Ø Dauer bei 7 s/Zug |
|---|---|---|---|---|---|
| 5 | 7,8 | 7 | 13 | 555 | 54 s |
| 10 | 7,8 | 7 | 12 | 536 | 54 s |
| 20 | 8,0 | 7 | 13 | 519 | 56 s |
| 35 | 8,7 | 7 | 15 | 512 | 61 s |
| 50 | 8,5 | 7 | 14 | 461 | 60 s |
| 70 | 8,6 | 8 | 13 | 423 | 60 s |
| 100 | 8,3 | 8 | 14 | 361 | 58 s |

Die Dauer bleibt zwischen Level 5 und 100 stabil (Ø 8–9 Züge, unter einer Minute reine Zugzeit). Größere Formate (Duo/Trio) verlängern Kämpfe proportional zur Zahl der aktiven Echos; Bosse folgen K35 §10.

### 5.2 Typen-Gleichgewicht

Die Typtabelle (K17) hat drei Stufen: 1.600 ‰, 1.000 ‰, 625 ‰. Für jeden Typ: wie viele Typen er sehr effektiv trifft, gegen wie viele er wenig ausrichtet, wofür er anfällig ist und wogegen resistent:

| Typ | sehr effektiv gegen | schwach gegen (offensiv) | anfällig für | resistent gegen | Offensivbilanz | Defensivbilanz |
|---|---|---|---|---|---|---|
| Glut | 3 | 3 | 2 | 3 | +0 | +1 |
| Flut | 3 | 3 | 3 | 3 | +0 | +0 |
| Stein | 3 | 4 | 4 | 5 | -1 | +1 |
| Sturm | 3 | 4 | 3 | 3 | -1 | +0 |
| Blüte | 3 | 3 | 4 | 4 | +0 | +0 |
| Frost | 3 | 4 | 3 | 3 | -1 | +0 |
| Leere | 3 | 3 | 3 | 4 | +0 | +1 |
| Licht | 3 | 3 | 2 | 2 | +0 | +0 |
| Gift | 3 | 5 | 3 | 3 | -2 | +0 |
| Metall | 3 | 2 | 4 | 6 | +1 | +2 |
| Geist | 3 | 3 | 3 | 3 | +0 | +0 |
| Kristall | 3 | 2 | 4 | 4 | +1 | +0 |
| Klang | 3 | 5 | 2 | 2 | -2 | +0 |
| Schwerkraft | 3 | 3 | 2 | 3 | +0 | +1 |
| Arkan | 3 | 3 | 3 | 2 | +0 | -1 |

Jeder Typ trifft genau drei Typen sehr effektiv. Die Bilanzen liegen zwischen −2 und +2 (Grenze BL-04: ± 3). Die Ausreißer sind gewollt und durch Mechaniken ausgeglichen: **Metall** ist defensiv stark (+2), hat aber keinen Status-Schutz außer Erschüttert und wenig Heilung; **Klang** und **Gift** sind offensiv schwächer (−2), tragen aber Harmonie (Klang) bzw. Zermürbung (Gift) als Kernmechanik; **Arkan** ist defensiv leicht schwächer (−1) und bekommt Glyphenfelder.

### 5.3 Fähigkeiten-Budget

Aktive Schadensfähigkeiten werden über „Stärke je 100 Zeitkosten“ verglichen (× Genauigkeit; Flächen gewichtet: Reihe ×1,4, alle Gegner ×1,6; Mehrfachtreffer mit Ø Trefferzahl):

| Kennzahl | Wert |
|---|---|
| Aktive Schadensfähigkeiten | 111 |
| Median „Stärke je 100 Zeitkosten“ (× Genauigkeit; Fläche: Reihe ×1,4, alle ×1,6; Mehrfachtreffer Ø Trefferzahl) | 66,7 |
| Spanne (min – max) | 50,0 – 120,0 |
| Innerhalb Median ± 40 % | 104 |
| Ausreißer (mit Begründung im Datenblatt) | 7 |

Ausreißer sind erlaubt, wenn ein Effekt sie begründet (Rückstoß, Aufladen, Selbst-Schwächung, Wetterbindung, Erschöpfung …):

| Fähigkeit | Typ | Stärke | Zeitkosten | Ziel | Wert | Begründung (Effekte/Tags) |
|---|---|---|---|---|---|---|
| Esseneruption | Glut | 100 | 130 | Enemies | 105 | Exhaust() |
| Sturzflut | Flut | 110 | 90 | Single | 104 | Stage(Self,SpAttack,-1) |
| Nullpunkt | Leere | 120 | 80 | Single | 120 | Stage(Self,SpAttack,-2) |
| Zenitstoß | Licht | 120 | 110 | Single | 98 | Charge() |
| Diamantlanze | Kristall | 120 | 110 | Single | 98 | Charge() |
| Donnerhall | Klang | 100 | 130 | Enemies | 105 | Exhaust() |
| Meteorsturz | Schwerkraft | 110 | 100 | Single | 94 | Charge() |

### 5.4 Kampf-KI

Die KI-Profile (K34) sollen sich in der Stärke staffeln, ohne dass der „Meister“ unschlagbar wird. Duell-Matrix (Siegquote Zeile gegen Spalte, gleiche Level, `aethris_ai.py`):

| Profil ↓ gegen → | Zufall | Gierig | Taktiker | Meister |
|---|---|---|---|---|
| **Zufall** | 48 % | 40 % | 40 % | 36 % |
| **Gierig** | 57 % | 49 % | 49 % | 45 % |
| **Taktiker** | 63 % | 50 % | 47 % | 50 % |
| **Meister** | 61 % | 51 % | 49 % | 50 % |

Die Abstufung ist flach (≈ 5–10 Prozentpunkte zwischen Nachbarn): Das Spiel bleibt auch gegen den Meister gewinnbar – Wissen und Aufstellung entscheiden, nicht die KI-Stufe. Arenameister nutzen zusätzlich Signatur-Taktiken (K34).

---

## 6. Fortschritt und Wirtschaft

### 6.1 Wärterrang

| Abschnitt | Spielzeit | Wärter-EP/h | EP am Ende | Rang am Ende | Ø Minuten je Rang |
|---|---|---|---|---|---|
| Prolog | 3 h | 800 | 2.400 | 5 | 45 |
| Akt I | 15 h | 2.000 | 32.400 | 16 | 81 |
| Akt II | 20 h | 2.000 | 72.400 | 24 | 150 |
| Akt III | 12 h | 2.500 | 102.400 | 29 | 144 |
| Endgame 1–20 h | 20 h | 2.800 | 158.400 | 36 | 171 |
| Endgame 20–40 h | 20 h | 3.000 | 218.400 | 40 | 300 |
| Endgame 40–60 h | 20 h | 3.000 | 278.400 | 40 | – |

Rang 28 (Ranked) liegt am Story-Ende, Rang 40 nach rund 60 Stunden Endgame (K43). Die Arena-Ränge in §4.2 stammen aus derselben Zeitlinie.

### 6.2 Bindung

Bindung soll durch Vorbereitung gelingen, nicht durch Glück (DR-03, DR-07). Die Szenarien aus K36 zeigen, wie Kodex, Köder, Fallen und Siegel die Resonanz über die Schwelle heben:

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

### 6.3 Wirtschaft

| Abschnitt | Einnahmen | Bedarf | Quote | kumuliert (inkl. 1.000 ◎ Start) | Bewertung |
|---|---|---|---|---|---|
| Prolog | 1.628 | 1.950 | 83 % | 134 % | gesund |
| Akt I | 49.291 | 35.692 | 138 % | 137 % | gesund |
| Akt II | 135.250 | 109.972 | 122 % | 126 % | gesund |
| Akt III | 127.130 | 151.061 | 84 % | 105 % | knapp – Entscheidungen nötig |
| Endgame (je 10 h) | 113.550 | 104.240 | 108 % | 106 % | knapp – Entscheidungen nötig |

Akt III und das Endgame sind bewusst „knapp“ (84–108 %): Spielende müssen zwischen Ausrüstung V, Hain-Ausbau und Rezepten wählen. Akt I ist großzügig (138 %), damit der Einstieg nicht an Geld scheitert. Kein Abschnitt fällt unter 80 %; kumuliert bleibt das Konto immer positiv.

---

## 7. Schwierigkeitsgrade

| Grad | Wirkung | Zielgruppe |
|---|---|---|
| **Entspannt** | EP ×1,25; Effektivitätsvorschau immer; Gegner-KI eine Stufe niedriger; Bindungsfenster +20 % | Erstes Rollenspiel, Story-Fokus |
| **Wärter** (Standard) | Werte wie in diesem Kapitel | Die meisten |
| **Meister** | Gegner-KI eine Stufe höher, Arena-Ass +2, −10 % Sol bei Niederlage (max. 5.000 ◎, CANON Grade) | Erfahrene |
| **Eiserner Wärter** (Modifikator) | Erschöpfte Echos für die laufende Region gesperrt; ein Bindungsversuch je Echo | Herausforderung |

Barrierefreiheits-Optionen (K54) sind unabhängig vom Grad: Großzügiges Timing, Auto-Einklang, Zeitleisten-Erklärmodus und Kampf-Empfehlungen stehen in jedem Grad zur Verfügung und verändern keine Belohnungen.

---

## 8. Tuning-Knöpfe

Die wichtigsten Stellschrauben stehen zentral in `Data/Balance/TuningKnobs.csv` – mit Quelle, Standardwert, sicherem Bereich und Owner. Werte außerhalb des Bereichs verlangen eine erneute Prüfung aller betroffenen Modelle (BL-07).

| Knopf | Quelle | Standard | Sicherer Bereich | Wirkung | Owner |
|---|---|---|---|---|---|
| EP-Ertrag Stufe 1/2/3 | `Data/Echos/Species.csv:ExpYield` | 140 | 60 – 320 | Levelgeschwindigkeit | RPG Systems Designer |
| Verzögerungsformel-Faktor | `CANON §117 (300)` | 300 | 260 – 340 | Zugfrequenz, Tempo-Wert von GES | Lead Combat Designer |
| Typ-Effektivität „sehr effektiv“ (‰) | `Data/Combat/TypeChart.csv` | 1600 | 1400 – 1800 | Gewicht der Typwahl | Lead Combat Designer |
| Typ-Effektivität „wenig effektiv“ (‰) | `Data/Combat/TypeChart.csv` | 625 | 550 – 750 | Gewicht der Typwahl | Lead Combat Designer |
| Volltreffer-Chance Stufe 0 (‰) | `tools/ref/aethris_combat.py CRIT_PERMILLE` | 42 | 30 – 80 | Varianz | Lead Combat Designer |
| Harmonie je Treffer | `K30 §2 (Harmonie-Ökonomie)` | 5 | 3 – 8 | Crescendo-Häufigkeit | Lead Combat Designer |
| Status-Immunität nach 2× gleichem Status (Runden) | `CANON §128` | 3 | 2 – 5 | Kontroll-Teams | Lead Combat Designer |
| Weiches Anschwellen je Runde (‰) | `CANON §128` | 1100 | 1050 – 1150 | Bosskampf-Dauer | Lead Combat Designer |
| Raid-Skalierung je Spieler (‰) | `Data/Combat/Bosses.csv PlayerScale` | 700 | 550 – 850 | Raid-Schwierigkeit nach Spielerzahl | Lead Combat Designer |
| Bindungsfenster Gut (ms, Standard) | `K36 §5` | 280 | 160 – 400 | Bindungsgefühl | Lead Systems Designer |
| Sol je Trainerkampf (× Ass-Lv.) | `CANON Wirtschaft (25)` | 25 | 18 – 32 | Sol-Einkommen | Economy Designer |
| Verkaufsquote (‰ des Werts) | `CANON Wirtschaft (35 %)` | 350 | 250 – 450 | Inflation | Economy Designer |
| Wärter-EP je Spielstunde (Akt II) | `tools/ref/aethris_progression.py` | 2000 | 1600 – 2600 | Rangtempo | Systems Designer |
| Ranked-Normstufe | `Data/PvP/Rulesets.csv` | 70 | 70 – 70 | Ranked (LOCKED, Q5) | Lead Combat Designer |
| Tiefe V HP-Faktor (‰) | `Data/Endgame/DepthTiers.csv` | 1500 | 1300 – 1700 | Endgame-Schwierigkeit | Lead Content Designer |
| Ökologie-Dichte (‰) | `Data/Ecology/PopulationTuning.csv` | 1000 | 700 – 1300 | Begegnungsrate in der Welt | Lead Ecology Designer |
| Arena-Ass-Versatz Akt II/III (Level) | `tools/ref/aethris_balance.py ACE_OFFSET` | 2 | 0 – 3 | Arena-Herausforderung | Lead Combat Designer |
| Koop-Wildgegner HP je Spieler (‰) | `K60 §2.2` | 700 | 550 – 850 | Koop-Schwierigkeit | Lead Online Designer |

**Regeln:** Änderungen nur per Patch (Daten-Hash, K59 §7.3); jede Änderung mit Begründung, betroffenen Modellen und Simulationsergebnis im Änderungsprotokoll; Ranked-relevante Änderungen nur zum Saisonwechsel (K61).

---

## 9. Live-Balancing

| Signal | Quelle | Schwelle | Reaktion |
|---|---|---|---|
| Arena-Niederlagenquote beim ersten Versuch | Telemetrie | > 55 % (Wärter) | Ass-Versatz −1 prüfen |
| Spielzeit bis Akkord n | Telemetrie | > 130 % des Plans | Korridore/EP prüfen |
| Bindungsabbrüche | Telemetrie | > 40 % bei einer Art | Resonanz-Werte der Art prüfen |
| Sol-Kontostand Median | Telemetrie | < 20 % des Bedarfs des nächsten Abschnitts | Einnahmen prüfen |
| Nutzung von Arten im Story-Chor | Telemetrie | Art nie in Top-500 der Nutzung, obwohl häufig | Werte/Fähigkeiten prüfen |
| Ranked-Meta | K61 §7 | Nutzung > 40 %, Siegquote > 56 % | Saison-Patch |
| Raid-/Tiefen-Abschlussquote | Telemetrie | < 25 % nach 10 Versuchen | Mechanik-Lesbarkeit prüfen |

**Rhythmus:** wöchentliche Auswertung im Balance-Rat (Systems, Combat, Economy, Data Science, Community), monatliche Daten-Patches für PvE, Ranked-Änderungen zu Saisonbeginn. Spielende sehen alle Werteänderungen in den Patch-Notizen mit Begründung – keine stillen Änderungen.

---

## 10. Playtests

| Phase | Wer | Umfang | Fragestellungen |
|---|---|---|---|
| Intern (P2–P3) | Team, 20–40 Personen | wöchentlich, 2 h | Kampfgefühl, Arena 1–4, Bindung |
| Vertical Slice (K67) | 30 externe Personen, gemischte Erfahrung | 3 Tage | Onboarding, Arena 1–2, Verständnis Zeitleiste |
| Alpha | 200 externe Personen (NDA) | 4 Wochen | Akt I–II, Wirtschaft, Arena-Kurve |
| Closed Beta (P5) | ~5.000 | 4 Wochen | Online, Ranked S0, Raids, Server |
| Barrierefreiheit | 15 Personen mit Behinderungen (Sehen, Hören, Motorik, Kognition) | je Meilenstein | Optionen, Timing, Lesbarkeit |
| Kinder/Familien | 20 Familien (Alter 7–12 mit Eltern) | Alpha, Beta | Verständnis, Frustpunkte, Texte |

Jeder Playtest misst dieselben Kennzahlen wie die Telemetrie (§9) plus Fragebögen (Zufriedenheit, Schwierigkeit 1–7, „Wusste ich, warum ich verloren habe?“). Ergebnis eines Playtests ist immer eine Liste von Tuning-Vorschlägen mit Bezug auf `TuningKnobs.csv`.

---

## 11. Prüfregeln

`tools/ref/aethris_balance.py validate`:

| Regel | Inhalt |
|---|---|
| BL-01 | Keine zwei Arten mit identischen 8 Basiswerten |
| BL-02 | Identitätsakzente: Kernsumme und PRÄ/AUS unverändert, Δ ≤ 8 |
| BL-03 | Arena-Stärkeverhältnis 1,00–1,12 je Stufe |
| BL-04 | Jeder Typ ≥ 2 Stärken, ≥ 2 Schwächen, Bilanzen ± 3 |
| BL-05 | Fähigkeits-Ausreißer nur mit Effekt-Begründung |
| BL-06 | Arena-Format zum erwarteten Rang freigeschaltet |
| BL-07 | Tuning-Knöpfe mit Quelle, Standard im sicheren Bereich |

**Ergebnis:** Prüfregeln BL-01–BL-07: **0 Verstöße**. 256 Arten ohne Basiswert-Dubletten (131 Identitätsakzente), 10 Arenastufen im Zielband 1,00–1,12, 15 Typen ausgewogen, 18 Tuning-Knöpfe im sicheren Bereich.

Zusätzlich laufen alle Prüfer der Fachkapitel bei jeder Datenänderung (Katalog, Quests, NPCs, UI, Ökologie, Palette, VFX, Netz, Soziales, PvP, Endgame) – Stand dieses Kapitels: alle mit 0 Verstößen.

---

## 12. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Creature Design | Neue Arten nur mit eindeutigen Basiswerten (BL-01); Akzente beim Katalog-Schreiben | K16 |
| Kampf | Arena-Teams nach `ArenaTiers.csv`; Grad „Meister“ +2 Ass | K11–K13, K33 |
| Data Science | Dashboards für §9, Wochenbericht | K68 |
| QA | Playtest-Plan §10, Kennzahlen identisch zur Telemetrie | K66 |
| Produktion | Balance-Rat wöchentlich, Patch-Rhythmus | K67, K68 |
| Community | Patch-Notizen mit Begründung | K68 |

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-261 | Identitätsakzente (Leitwert des Primärtyps +Δ, höchster übriger −Δ) statt Neuverteilung aller Werte | Minimaler Eingriff, Kernsummen bleiben, nachvollziehbar und idempotent | Zufallsrauschen; manuelle Einzelanpassung |
| ADR-262 | Q13: Arena-Ass = Erwartung + 1 (Akt I) / + 2 (Akt II/III), Team −2, Zielverhältnis 1,00–1,12 | Fordernd ohne Grind, Überleveln belohnt | vorläufige Tabelle K02 (zu leicht); dynamische Skalierung |
| ADR-263 | Fähigkeits-Budget über Stärke je 100 Zeitkosten mit Effekt-Begründung für Ausreißer | Vergleichbarkeit über Zeitleiste | reiner Stärkevergleich |
| ADR-264 | Tuning-Knöpfe zentral mit sicheren Bereichen; Änderungen nur per Patch | Kontrolle, Daten-Hash, Transparenz | Live-Konfiguration für Kampfwerte |
| ADR-265 | Balance-Rat wöchentlich, Ranked-Änderungen nur zum Saisonwechsel, öffentliche Begründungen | Vertrauen, Planbarkeit | stille Hotfixes |
| ADR-266 | Katalogkapitel werden nach Datenänderungen automatisch neu erzeugt (`regen_catalog.py`) | ADR-075 konsequent: Daten sind die Wahrheit | manuelle Pflege der Kapitel |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §248 | Balancing-Methode: Daten → Referenzmodelle → Prüfregeln → Simulation → Playtests → Telemetrie; Ziele BZ-1–BZ-6; Modellliste | LOCKED |
| §249 | Identitätsakzente (`StatAccents.csv`, 131 Arten, Δ 2–8, Leitwert je Primärtyp), BL-01: keine Basiswert-Dubletten; Katalog neu erzeugt | LOCKED |
| §250 | Q13: Arena-Stufen final (`ArenaTiers.csv`): Ass 14/19/24/29/36/43/50/56/63/70, Chor 3/4/4/5/5/5/6/6/6/6, Formate wie K02, Team = Ass − 2, Verhältnis 1,02–1,07 | LOCKED (ersetzt K02 §9.2 vorläufig; schließt Q13) |
| §251 | Tuning-Knöpfe (`TuningKnobs.csv`), Schwierigkeitsgrade (Entspannt/Wärter/Meister/Eisern mit Werten), Live-Balancing-Signale und Rhythmus, Playtest-Plan | LOCKED |
| Q-Liste | Q13 geschlossen (→ §250) | – |
| §10 | ADR-261 – ADR-266 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Ziele BZ-1–BZ-6, Methode und Modellübersicht
- [x] Basiswert-Dubletten gefunden (54 Gruppen) und mit Identitätsakzenten aufgelöst; Katalog neu erzeugt
- [x] Q13: Arena-Stufen aus Modell abgeleitet, Daten gespeichert
- [x] Kampfdauer, Typen-Gleichgewicht, Fähigkeits-Budget, KI-Matrix (berechnet)
- [x] Wärterrang, Bindung, Wirtschaft (berechnet)
- [x] Schwierigkeitsgrade, Tuning-Knöpfe, Live-Balancing, Playtests
- [x] Prüfregeln BL-01–BL-07 (0 Verstöße), alle Fachprüfer grün
- [x] Anforderungen, ADR-261 – ADR-266, CANON §248–§251

➡️ **Nächstes Kapitel: K64 – Save-System.**
