# K29 · Fähigkeiten II – Passive und Lernsets

| Feld | Wert |
|---|---|
| Dokument | Kapitel 29 von 68 · Combat Guide, Teil II |
| Version | 1.0 |
| Owner | RPG Systems Designer |
| Mitwirkende | Lead Combat Designer, Creature Design Lead, Technical Designer, Economy Designer (Klangschriften/Tutoren), Narrative (Feldklänge) |
| Baut auf | K28 (Fähigkeitssystem, CANON §97–§101), K20–K27 (Katalog, Signaturkonzepte), CANON §18 (Erwerbswege, Passiv-Regeln), §86 (Evolution überträgt Passive) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Abilities/Abilities.csv` (+90 Passive), `Data/Echos/Learnsets.csv` (3350 Einträge), `Data/Echos/PassiveOptions.csv` (756), `Data/Items/Klangschriften.csv` (90), `Data/Abilities/Tutors.csv` (30), `tools/authoring/abilities_passive.py`, `tools/gen_learnsets.py` (Generator + Validator LS-01…LS-12) |
| Neue Kanon-Einträge | CANON §102 (Passive & Auslöser), §103 (Feldklänge), §104 (Lernset-Regeln), §105 (Klangschriften & Tutoren) |

---

## Inhalt

1. [Passive Fähigkeiten im Kampfset](#1-passive-fähigkeiten-im-kampfset)
2. [Auslöser und passive Primitiva](#2-auslöser-und-passive-primitiva)
3. [Die 90 Passiven](#3-die-90-passiven)
4. [Feldklänge der Ursprungsstimmen und Mythischen](#4-feldklänge-der-ursprungsstimmen-und-mythischen)
5. [Erwerbswege aktiver Fähigkeiten](#5-erwerbswege-aktiver-fähigkeiten)
6. [Der Lernset-Generator](#6-der-lernset-generator)
7. [Beispiel-Lernsets](#7-beispiel-lernsets)
8. [Klangschriften](#8-klangschriften)
9. [Tutoren](#9-tutoren)
10. [Signaturkonzepte](#10-signaturkonzepte)
11. [Validierung und Kennzahlen](#11-validierung-und-kennzahlen)
12. [Code](#12-code)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Passive Fähigkeiten im Kampfset

Jedes Echo trägt **genau eine** aktive Passive (Kampfset-Slot 5, CANON §18). Die Art legt fest, welche Passiven möglich sind:

| Regel | Wert |
|---|---|
| Sichtbare Optionen je Art | 1–3 (aus den Typen der Art) |
| Versteckte Option | genau 1 (aus einem **fremden** Typ – eine Überraschung, die erforscht werden will) |
| Wildfang | 1. sichtbare Option 60 %, 2. 30 %, 3. 10 %; versteckt 0 % (außer Sehr selten: 5 %) |
| Wechsel | Item **Wandelklang** (Crafting K41): wählt eine andere freigeschaltete Option |
| Freischaltung versteckt | Kodex-Stufe 4 der Art **und** Wandelklang; oder Zucht (Vererbungsregel K38) |
| Evolution | Option wird auf die gleiche Position der neuen Art abgebildet (CANON §86); Linien teilen ihre Optionen |
| Legendäre/Mythische | genau ein **Feldklang** (art-exklusiv, nicht wechselbar) |

**Designziel:** Passive sollen **Kampfentscheidungen verschieben**, nicht Zahlen aufblähen. Statische Werte-Modifikatoren (z. B. „VER ×1,15“) sind auf ≤ 15 % gedeckelt; die interessanteren Passiven reagieren auf Auslöser (Kontakt, Wetter, Reihe, Niederlage eines Verbündeten) und erzeugen so lesbare Momente („Funkenhaut hat ausgelöst!“, DR-24: Symbol + Ton).

---

## 2. Auslöser und passive Primitiva

Passive verwenden dieselbe Effekt-DSL wie Aktive (K28 §4), ergänzt um **statische Primitiva** und einen **Auslöser**.

| Auslöser (`Trigger`) | Bedeutung | Prüfzeitpunkt (K31) |
|---|---|---|
| Always | dauerhaft | beim Werte-Aufbau |
| BattleStart / SwitchIn | Kampfbeginn / Einwechseln | Ereignis `Combat.Join` |
| TurnStart | Beginn jedes eigenen Zuges | Zeitleiste `TurnBegin` |
| HitTaken / ContactTaken | getroffen / Kontakt-Treffer | nach Schadensauflösung |
| HitDealt / CritDealt | nach eigenem Treffer / Volltreffer | nach Schadensauflösung |
| LowHP | HP ≤ 33 %, einmal pro Kampf | nach Schadensauflösung |
| StatusReceived | ein Status wird erlitten | nach Statusanwendung |
| AllyFainted / EnemyFainted | Verbündeter / Gegner verklingt | Ereignis `Combat.Faint` |
| RowFront / RowBack | solange in Vorder-/Hinterreihe | Formation (K33) |
| HarmonyFull | Harmonie voll | Harmonie-Änderung (K33) |
| Weather.X / Terrain.X | bei Wetter / auf Terrain | Feldzustand (K32) |
| FieldSong | Feldklang, solange auf dem Feld | dauerhaft (§4) |

| Statisches Primitiv | Wirkung | Deckel |
|---|---|---|
| Mod(Wert, ‰) | Wertmultiplikator | 850–1300 ‰ (mit Bedingung bis 1300, sonst ≤ 1150) |
| TypePower(Typ, ‰) | Stärke eines Fähigkeitstyps | ≤ 1100 dauerhaft, ≤ 1500 bei LowHP |
| Resist(Typ, ‰) | erlittener Schaden eines Typs | ≥ 700 ‰ |
| Immune(Status) | Status-Immunität | – |
| StatusChance(‰), HealPower(‰), TimeCost(±n) | Chancen, Heilwirkung, Zeitkosten | TimeCost ≥ −10 |
| Custom(Schlüssel) | Feldklang-Sonderregel (eigenes Primitiv in GF_Combat) | nur Legendäre/Mythische |

**Stapelregel:** Passive desselben Echos wirken einzeln; gleiche Primitiva verschiedener Echos multiplizieren sich, `Mod`-Ketten werden auf 1500 ‰ gedeckelt (K32).

---

## 3. Die 90 Passiven

Je Typ sechs Passive. Feldklänge (§4) sind in diese Zählung eingerechnet; Typen ohne Ursprungsstimme oder Mythisches (Sturm, Metall, Arkan) erhalten sechs reguläre Passive.

### 3.1 Glut
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P001 | **Glutherz** | LowHP | Bei HP ≤ 33 % (einmal): Glut-Fähigkeiten ×1,50. |  |
| ABL_P002 | **Funkenhaut** | ContactTaken | Bei Kontakt-Treffer: 30 % Chance auf Brand. Der Status trifft den Angreifer. |  |
| ABL_P003 | **Hitzespeicher** | Weather.Heatwave | Bei Hitzewelle: heilt sich selbst um 6 % der max. HP. Wirkt zu Beginn jedes eigenen Zuges. |  |
| ABL_P004 | **Flammentanz** | CritDealt | Nach eigenem Volltreffer: der Anwender rückt 30 Ticks auf der Zeitleiste vor. |  |
| ABL_P005 | **Aschefell** | Always | Dauerhaft: erlittener Flut-Schaden ×0,80; immun gegen Ausgetrocknet. |  |
| ABL_P006 | **Weltenschmiede** | FieldSong | Pyr'thagon: Jeder eigene Treffer erhöht die eigene VER um 1 Stufe (max. +4); das Feld bleibt dauerhaft Glutboden. | Feldklang|Exclusive |

### 3.2 Flut
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P007 | **Gezeitenkörper** | TurnStart | Zu Beginn jedes eigenen Zuges: heilt sich selbst um 5 % der max. HP. Nur in Regen oder auf Flutfeld. |  |
| ABL_P008 | **Strömungssinn** | SwitchIn | Beim Einwechseln: der Anwender rückt 40 Ticks auf der Zeitleiste vor. |  |
| ABL_P009 | **Glatte Haut** | Always | Dauerhaft: immun gegen Rückstoß; AUS ×1,10. |  |
| ABL_P010 | **Brandungsschild** | RowFront | Solange in der Vorderreihe: erlittener Glut-Schaden ×0,75. |  |
| ABL_P011 | **Tiefenruhe** | RowBack | Solange in der Hinterreihe: sich selbst heilt 99 Runden je 4 % der max. HP. Solange das Echo in der Hinterreihe steht. |  |
| ABL_P012 | **Gezeitenwende** | FieldSong | Thal'assyr: Jede zweite Runde tauschen die Reihen beider Seiten; die eigene Seite handelt danach zuerst. | Feldklang|Exclusive |

### 3.3 Stein
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P013 | **Felsenhaut** | Always | Dauerhaft: VER ×1,15. |  |
| ABL_P014 | **Standfest** | Always | Dauerhaft: immun gegen Rückstoß; immun gegen Erschüttert. Rückstoß ist für Stein ohnehin wirkungslos; Standfest ergänzt Erschüttert. |  |
| ABL_P015 | **Bergruhe** | LowHP | Bei HP ≤ 33 % (einmal): Schild für sich selbst (25 % der max. HP). |  |
| ABL_P016 | **Sandverbunden** | Weather.Sandstorm | Bei Sandsturm: SVE ×1,30. |  |
| ABL_P017 | **Fundament** | RowFront | Solange in der Vorderreihe: Schild für die eigene Reihe (5 % der max. HP). Zu Beginn jeder Runde für die eigene Reihe. |  |
| ABL_P018 | **Bergschwere** | FieldSong | Orh'gruun: Gegner können die Reihe nicht wechseln; alle Verbündeten VER +2 Stufen. | Feldklang|Exclusive |

### 3.4 Sturm
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P019 | **Windläufer** | Always | Dauerhaft: eigene Zeitkosten −10. Gilt für alle eigenen aktiven Fähigkeiten. |  |
| ABL_P020 | **Böenreiter** | Weather.Thunderstorm | Bei Gewitter: GES ×1,30. |  |
| ABL_P021 | **Blitzreflex** | HitTaken | Wenn getroffen: der Anwender rückt 20 Ticks auf der Zeitleiste vor. |  |
| ABL_P022 | **Sturmauge** | Always | Dauerhaft: immun gegen Verlangsamt; PRÄ ×1,05. |  |
| ABL_P023 | **Kettenfunke** | HitDealt | Nach eigenem Treffer: 10 % Chance auf Erschüttert. Nur bei Mehrfachtreffern: je Treffer. |  |
| ABL_P024 | **Rückenwindgeist** | SwitchIn | Beim Einwechseln: alle Verbündeten rücken 30 Ticks auf der Zeitleiste vor. |  |

### 3.5 Blüte
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P025 | **Photosynth** | Weather.Clear | Bei Klar: heilt sich selbst um 6 % der max. HP. Zu Beginn jedes eigenen Zuges bei klarem Wetter. |  |
| ABL_P026 | **Wurzelkraft** | RowFront | Solange in der Vorderreihe: immun gegen Rückstoß; VER ×1,10. |  |
| ABL_P027 | **Pollenwolke** | ContactTaken | Bei Kontakt-Treffer: 30 % Chance: PRÄ −1 für den Angreifer. |  |
| ABL_P028 | **Grüner Daumen** | Always | Dauerhaft: eigene Heilwirkung ×1,30. |  |
| ABL_P029 | **Keimkraft** | AllyFainted | Wenn ein Verbündeter verklingt: heilt alle Verbündeten um 15 % der max. HP. |  |
| ABL_P030 | **Wurzellied** | FieldSong | Sylv'anor: Jede Runde heilen alle Verbündeten 6 % HP; Blüte-Fähigkeiten kosten 20 Zeit weniger. | Feldklang|Exclusive |

### 3.6 Frost
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P031 | **Eiskern** | Always | Dauerhaft: erlittener Glut-Schaden ×0,80; immun gegen Starre. |  |
| ABL_P032 | **Kältehauch** | ContactTaken | Bei Kontakt-Treffer: der Angreifer rückt 30 Ticks auf der Zeitleiste zurück. |  |
| ABL_P033 | **Schneetarnung** | Weather.Snow | Bei Schneefall: AUS ×1,25. |  |
| ABL_P034 | **Präzisionsfrost** | HitDealt | Nach eigenem Treffer: 20 % Chance: PRÄ −1 für das Ziel. |  |
| ABL_P035 | **Firnpanzer** | LowHP | Bei HP ≤ 33 % (einmal): Schild für sich selbst (20 % der max. HP); alle Gegner rücken 20 Ticks auf der Zeitleiste zurück. |  |
| ABL_P036 | **Aurora der Erhaltung** | FieldSong | Isv'aldr: Positive Stufen und Schilde der Verbündeten können nicht entfernt, gestohlen oder durchdrungen werden. | Feldklang|Exclusive |

### 3.7 Leere
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P037 | **Leerer Blick** | SwitchIn | Beim Einwechseln: entfernt Schilde und positive Stufen von das Ziel. Trifft den Gegner gegenüber. |  |
| ABL_P038 | **Seelenhunger** | EnemyFainted | Wenn ein Gegner verklingt: heilt sich selbst um 20 % der max. HP; entzieht dem Gegnerteam 10 Harmonie. |  |
| ABL_P039 | **Schweigsam** | Always | Dauerhaft: immun gegen Verstummt; erlittener Klang-Schaden ×0,75. |  |
| ABL_P040 | **Nichtigkeit** | HitTaken | Wenn getroffen: entzieht dem Gegnerteam 3 Harmonie. |  |
| ABL_P041 | **Schattenkörper** | RowBack | Solange in der Hinterreihe: AUS ×1,15. |  |
| ABL_P042 | **Große Pause** | FieldSong | Velnox: Die Harmonie beider Seiten wird zu Beginn jeder Runde auf 0 gesetzt; Fähigkeiten mit Tag Sound verstummen. | Feldklang|Exclusive |

### 3.8 Licht
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P043 | **Strahlkraft** | Always | Dauerhaft: Licht-Fähigkeiten ×1,10; immun gegen Geblendet. |  |
| ABL_P044 | **Lichtgestalt** | BattleStart | Bei Kampfbeginn: enthüllt das Ziel (Ausweichen, Täuschung und Tarnung wirkungslos). Enthüllt alle Gegner für 2 Runden. |  |
| ABL_P045 | **Reiner Glanz** | StatusReceived | Wenn ein Status erlitten wird: entfernt negative Status von sich selbst. Einmal pro Kampf. |  |
| ABL_P046 | **Morgenwache** | Weather.Clear | Bei Klar: SAN ×1,20. |  |
| ABL_P047 | **Rätselglanz** | FieldSong | Ash'kareth: Alle verborgenen Werte, Passiven und Kampfsets werden enthüllt; Täuschung, Tarnung und Trugbilder enden sofort. | Feldklang|Exclusive |
| ABL_P048 | **Finsternis** | FieldSong | Aurelune: Licht und Leere tauschen ihre Typvorteile, solange Aurelune auf dem Feld steht. | Feldklang|Exclusive |

### 3.9 Gift
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P049 | **Giftdrüsen** | Always | Dauerhaft: eigene Status-Chancen ×1,50. Gilt nur für Vergiftet. |  |
| ABL_P050 | **Zähe Säfte** | Always | Dauerhaft: immun gegen Vergiftet; erlittener Blüte-Schaden ×0,80. |  |
| ABL_P051 | **Fäulniskreis** | EnemyFainted | Wenn ein Gegner verklingt: verursacht Vergiftet (2 Stapel). Trifft den nächsten Gegner. |  |
| ABL_P052 | **Stachelkleid** | ContactTaken | Bei Kontakt-Treffer: 50 % Chance auf Vergiftet. Der Status trifft den Angreifer. |  |
| ABL_P053 | **Moorgedächtnis** | FieldSong | Nhael'vesh: Verklingende Echos beider Seiten hinterlassen Nebel: Vergiftet überträgt sich auf Gegner und heilt Verbündete. | Feldklang|Exclusive |
| ABL_P054 | **Ewiger Kreis** | FieldSong | Ouroveth: Gift heilt Verbündete statt zu schaden; ein verklingender Verbündeter keimt einmal mit 25 % HP neu. | Feldklang|Exclusive |

### 3.10 Metall
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P055 | **Stahlkörper** | Always | Dauerhaft: VER ×1,10; immun gegen Erschüttert. |  |
| ABL_P056 | **Konterinstinkt** | HitTaken | Wenn getroffen: kontert den nächsten physischen Angriff mit 50 % Schaden. Einmal pro Runde. |  |
| ABL_P057 | **Magnetfeld** | Always | Dauerhaft: erlittener Sturm-Schaden ×0,75. |  |
| ABL_P058 | **Schmiedeglut** | LowHP | Bei HP ≤ 33 % (einmal): ANG +2 für sich selbst. |  |
| ABL_P059 | **Rüstmeister** | SwitchIn | Beim Einwechseln: Schild für die eigene Reihe (10 % der max. HP). |  |
| ABL_P060 | **Rostfrei** | Always | Dauerhaft: erlittener Gift-Schaden ×0,70. |  |

### 3.11 Geist
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P061 | **Durchscheinend** | Always | Dauerhaft: AUS ×1,10; immun gegen Furcht. |  |
| ABL_P062 | **Spukgestalt** | BattleStart | Bei Kampfbeginn: erschafft ein Trugbild, das den nächsten Angriff abfängt. |  |
| ABL_P063 | **Seelenwacht** | AllyFainted | Wenn ein Verbündeter verklingt: SVE +1 für alle Verbündeten; Harmonie +15. |  |
| ABL_P064 | **Grenzgänger** | Always | Dauerhaft: Geist-Fähigkeiten ×1,10. Geist-Fähigkeiten ignorieren zusätzlich Schilde. |  |
| ABL_P065 | **Ahnenhauch** | LowHP | Bei HP ≤ 33 % (einmal): heilt sich selbst um 25 % der max. HP. |  |
| ABL_P066 | **Weltgedächtnis** | FieldSong | Ka'thurel: Jede eingesetzte Fähigkeit wird gespeichert; jeder Verbündete kann einmal pro Kampf eine gespeicherte Fähigkeit des Gegners einsetzen. | Feldklang|Exclusive |

### 3.12 Kristall
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P067 | **Prismenhaut** | HitTaken | Wenn getroffen: reflektiert den nächsten speziellen Angriff. Einmal pro Kampf. |  |
| ABL_P068 | **Resonanzspeicher** | HitTaken | Wenn getroffen: lädt den Anwender auf: nächster Angriff +50 % Stärke. Nach dem ersten erlittenen Treffer. |  |
| ABL_P069 | **Kristallgitter** | Always | Dauerhaft: SVE ×1,15; immun gegen Gebrochen. |  |
| ABL_P070 | **Lichtbrecher** | Always | Dauerhaft: erlittener Licht-Schaden ×0,70. |  |
| ABL_P071 | **Brechung** | FieldSong | Prism'aion: Jeder Klang- oder Kristall-Angriff trifft zusätzlich ein zweites Ziel mit 50 % Stärke. | Feldklang|Exclusive |
| ABL_P072 | **Spiegelwelt** | FieldSong | Mirrowisp: Jeder Angriff trifft zusätzlich ein Spiegelbild des Angreifers mit 30 % Stärke. | Feldklang|Exclusive |

### 3.13 Klang
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P073 | **Taktgefühl** | Always | Dauerhaft: eigene Zeitkosten −5; immun gegen Verstummt. |  |
| ABL_P074 | **Chorstimme** | HitDealt | Nach eigenem Treffer: Harmonie +5. |  |
| ABL_P075 | **Echoohr** | HitTaken | Wenn getroffen: 30 % Chance: AUS +1 für sich selbst. |  |
| ABL_P076 | **Resonanzkörper** | Always | Dauerhaft: Klang-Fähigkeiten ×1,10; erlittener Klang-Schaden ×0,80. |  |
| ABL_P077 | **Einklang** | FieldSong | Aeth'rion: Der Eigenklang-Bonus aller Verbündeten gilt für jede Fähigkeit, deren Typ einer ihrer Typen ist – auch für Zweittypen der Fähigkeitswahl. | Feldklang|Exclusive |
| ABL_P078 | **Taktwechsel** | FieldSong | Chronaire: Die Zeitleiste läuft rückwärts – das langsamste Echo handelt zuerst. | Feldklang|Exclusive |

### 3.14 Schwerkraft
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P079 | **Schwerpunkt** | Always | Dauerhaft: immun gegen Schwebend; immun gegen Rückstoß. |  |
| ABL_P080 | **Massenträgheit** | RowFront | Solange in der Vorderreihe: VER ×1,15; GES ×0,90. |  |
| ABL_P081 | **Anziehung** | SwitchIn | Beim Einwechseln: zieht das Ziel in die Vorderreihe. Zieht den Gegner gegenüber nach vorn. |  |
| ABL_P082 | **Bahnlenker** | HitDealt | Nach eigenem Treffer: 30 % Chance: AUS −1 für das Ziel. |  |
| ABL_P083 | **Fallgewicht** | Always | Dauerhaft: Schwerkraft-Fähigkeiten ×1,10. Zusätzlich +10 % gegen Schwebend-Ziele. |  |
| ABL_P084 | **Sternensturz** | FieldSong | Zenthrax: Zu Beginn jeder Runde schlägt ein Meteor (Stärke 60, Schwerkraft) auf ein zufälliges gegnerisches Feld; Schwerkraft-Effekte doppelt. | Feldklang|Exclusive |

### 3.15 Arkan
| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_P085 | **Formelgeist** | Always | Dauerhaft: Arkan-Fähigkeiten ×1,10; immun gegen Verflucht. |  |
| ABL_P086 | **Glyphenwacht** | StatusReceived | Wenn ein Status erlitten wird: SVE +1 für sich selbst. |  |
| ABL_P087 | **Umkehrsinn** | BattleStart | Bei Kampfbeginn: SAN +1 für sich selbst. Zusätzlich +1 SAN, solange die Typtabelle umgekehrt ist. |  |
| ABL_P088 | **Wandelhaut** | HitTaken | Wenn getroffen: ändert den Typ von sich selbst für 2 Runden zu Arkan. Einmal pro Kampf; nur bei sehr effektivem Treffer. |  |
| ABL_P089 | **Regelbrecher** | Always | Dauerhaft: eigene Zeitkosten −10. Gilt nur für Arkan-Status-Fähigkeiten. |  |
| ABL_P090 | **Spiegelgedächtnis** | EnemyFainted | Wenn ein Gegner verklingt: kopiert die zuletzt vom Ziel eingesetzte Fähigkeit. Kopiert die letzte Fähigkeit des verklungenen Gegners ins Kampfset (bis Kampfende). |  |

---

## 4. Feldklänge der Ursprungsstimmen und Mythischen

Die Signaturkonzepte aus K27 („Feldklang – …“) werden als **16 exklusive Passive** umgesetzt. Ein Feldklang ist eine **Regeländerung des gesamten Kampfes**, solange der Träger auf dem Feld steht. Damit fühlen sich Begegnungen mit Stimmen und Mythischen *anders* an als jeder andere Kampf, ohne dass ihre Werte unfair hoch sein müssen (Kernsumme 630–680 statt Vervielfachung).

| Regel | Wert |
|---|---|
| Anzeige | Feldklang-Banner beim Einwechseln, dauerhaftes Symbol am Zeitleistenrand, eigenes Klangbett (K55) |
| Mehrere Feldklänge | Nur einer gleichzeitig aktiv: der zuerst eingewechselte; der zweite ruht (Banner „übertönt“) |
| PvP | Ursprungsstimmen nicht Ranked-zulässig (CANON §34); Feldklänge nur in Freundschafts- und Sonderregel-Kämpfen |
| Raid/Bosse | Boss-Varianten nutzen dieselben Primitiva, ggf. mit Phasen-Erweiterung (K35) |
| Code | Je Feldklang ein `UFieldSongPrimitive` in GF_Combat (16 Klassen, eigene Unit-Tests) – die einzige Stelle, an der K29 neuen Code verlangt (DR-25-Ausnahme „neue Primitiva“) |

| Träger | Feldklang | Kernidee |
|---|---|---|
| Sylv'anor | Wurzellied | Dauerheilung, Blüte billiger |
| Orh'gruun | Bergschwere | Reihen eingefroren, Verteidigung |
| Nhael'vesh | Moorgedächtnis | Gift als Kreislauf |
| Thal'assyr | Gezeitenwende | Reihentausch-Rhythmus |
| Ash'kareth | Rätselglanz | totale Enthüllung |
| Pyr'thagon | Weltenschmiede | wachsende Härte, Glutboden |
| Isv'aldr | Aurora der Erhaltung | Buffs unantastbar |
| Ka'thurel | Weltgedächtnis | Fähigkeiten-Diebstahl als Teamressource |
| Prism'aion | Brechung | Streutreffer |
| Aeth'rion | Einklang | Eigenklang für alle Typen |
| Velnox | Große Pause | Harmonie null, Klang verstummt |
| Chronaire | Taktwechsel | Zeitleiste rückwärts |
| Mirrowisp | Spiegelwelt | Spiegeltreffer |
| Ouroveth | Ewiger Kreis | Gift heilt, Wiederkeimen |
| Zenthrax | Sternensturz | Meteore, Schwerkraft doppelt |
| Aurelune | Finsternis | Licht ↔ Leere vertauscht |

---

## 5. Erwerbswege aktiver Fähigkeiten

```
                ┌──────────── Repertoire eines Echos ────────────┐
 Lernset (Level) ─┤ 9–13 Einträge, 2 auf Lv. 1, Rest bis Lv. 52      │
 Evolution ──────┤ 1 Fähigkeit beim Stufenwechsel                   │
 Ei (Vererbung) ─┤ 3 Status-Fähigkeiten fremder Typen je Linie (K38)│
 Klangschrift ───┤ 90 Schriften, Typ des Echos ODER Abdeckungstyp    │
 Tutor ──────────┤ 30 Fähigkeiten, Typ des Echos, Fraktionsruf 3–4   │
                └──────────────────────────────────────────────────┘
```

| Weg | Umfang | Regel | Kapitel |
|---|---|---|---|
| Lernset | 3350 Einträge gesamt (Level + Evolution + Ei) | automatisch beim Levelaufstieg (Dialog „Ins Kampfset?“, sonst Repertoire) | K29 |
| Evolution | 1 je Art ab Stufe 2 | beim Stufenwechsel gelernt (CANON §86) | K19/K29 |
| Ei | 3 je Linie (Stufe 1) | Elternteil kennt die Fähigkeit (K38) | K38 |
| Klangschrift | 90 | Typ der Fähigkeit = Typ des Echos **oder** einer seiner 2 Abdeckungstypen | K29 §8 |
| Tutor | 30 | Typ der Fähigkeit = Typ des Echos; Rufrang 3–4 der Fraktion, Sol | K29 §9, K47 |

**Abdeckungstypen:** Jede Art besitzt zwei Abdeckungstypen, berechnet aus ihrer Primärfarbe: die Typen, die gegen die Resistenzen der Primärfarbe sehr effektiv sind (Typtabelle K17). Damit hat jedes Echo eine Antwort auf seinen „Konter“ – ein zentrales Ziel aus DR-08.

---

## 6. Der Lernset-Generator

Lernsets werden **nicht von Hand** gepflegt, sondern aus Arten- und Fähigkeitsdaten erzeugt (`tools/gen_learnsets.py build`). Handarbeit fließt über die Regeln und – wo nötig – über Overrides (für K63 vorgesehen: `Data/Echos/LearnsetOverrides.csv`, aktuell leer).

### 6.1 Lernstufen der Fähigkeiten

| Stufe | Kriterium (aus K28-Daten) | Lernlevel |
|---|---|---|
| E – Einstieg | Stärke ≤ 45 | 1–8 |
| M – Mittel | Stärke 50–75 | 10–30 |
| S – Status | Kategorie Status | 6–34 (≥ 1 bis Lv. 20) |
| L – Spät | Stärke ≥ 80 oder Zeitkosten ≥ 110 | 28–44 |
| H – Schwer | Stärke ≥ 100 | 36–52 |

### 6.2 Zusammensetzung

| Baustein | Primärtyp | Sekundärtyp | Abdeckung |
|---|---|---|---|
| Einstieg | 2 | – | – |
| Mittel | 2 | 2 (Einstieg/Mittel) | 1 je Abdeckungstyp (2) |
| Status | 2 | 1 | – |
| Spät | 1 | 1 (ab Stufe 2) | – |
| Schwer | 1 (ab Stufe 2 / Endform) | – | – |

Zielgröße: Dreier-Linie 9 / 11 / 13 · Zweier-Linie 10 / 12 · Einzel, Zweig, Legendär 13. **Kategorie-Präferenz:** Physische Arten (ANG > SAN, bei Gleichstand Striker/Tank/AllRound) erhalten bevorzugt physische Schadensfähigkeiten, die übrigen spezielle; Status-Fähigkeiten sind kategorieneutral.

### 6.3 Determinismus

Auswahl und Level entstehen aus **stabilen Hashes** (`sha1(Art|Schlüssel)`), nicht aus Zufall. Ein Neuaufbau ändert nichts, solange sich Daten nicht ändern; eine Datenänderung wirkt lokal (nur betroffene Arten), was Diffs im Review lesbar hält.

### 6.4 Legendäre und Mythische

Einstiegs-, Mittel- und Status-Fähigkeiten auf Lv. 1, Spät- und Schwer-Fähigkeiten zwischen Lv. 50 und 70 – Stimmen werden auf Lv. 60–70 gebunden und kennen dann ihr ganzes Lied.

---

## 7. Beispiel-Lernsets

### 7.1 Starter-Linie Blüte

**Fernlit** (ECHO_001)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Rankenhieb | Bloom | Physical | 60 |
| Level | 1 | Pollenschuss | Bloom | Special | 60 |
| Level | 10 | Sonnentrunk | Bloom | Status | 90 |
| Level | 18 | Saugwurzel | Bloom | Special | 90 |
| Level | 22 | Betäubungspollen | Bloom | Status | 60 |
| Level | 25 | Strudelzug | Tide | Special | 90 |
| Level | 28 | Dornenranke | Bloom | Physical | 100 |
| Level | 28 | Blütensturm | Bloom | Special | 130 |
| Level | 33 | Erdgrollen | Stone | Special | 140 |
| Egg | – | Prismenpanzer | Crystal | Status | 80 |
| Egg | – | Steinhaut | Stone | Status | 60 |
| Egg | – | Schwelbrand | Ember | Status | 60 |

Passiv: Photosynth, Wurzelkraft, Lichtbrecher (versteckt)

Crescendo: Urwaldchor ★, Dornenmeer · Feld: Rankenbrücke

**Fernwyn** (ECHO_002)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Rankenhieb | Bloom | Physical | 60 |
| Level | 1 | Pollenschuss | Bloom | Special | 60 |
| Level | 5 | Klingenwind | Storm | Special | 80 |
| Level | 12 | Keimsegen | Bloom | Status | 50 |
| Level | 13 | Strudelzug | Tide | Special | 90 |
| Level | 16 | Saugwurzel | Bloom | Special | 90 |
| Level | 24 | Dornenranke | Bloom | Physical | 100 |
| Level | 26 | Wurzelgriff | Bloom | Status | 70 |
| Level | 34 | Erdgrollen | Stone | Special | 140 |
| Level | 34 | Blütensturm | Bloom | Special | 130 |
| Level | 47 | Urwaldzorn | Bloom | Physical | 110 |
| Evolution | – | Blitzbogen | Storm | Special | 110 |

Passiv: Windläufer, Photosynth, Wurzelkraft, Lichtbrecher (versteckt)

Crescendo: Himmelszorn, Orkanschwinge, Urwaldchor ★, Dornenmeer · Feld: Rankenbrücke

**Verdrath** (ECHO_003)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Pollenschuss | Bloom | Special | 60 |
| Level | 1 | Summton | Sound | Special | 70 |
| Level | 3 | Rankenhieb | Bloom | Physical | 60 |
| Level | 10 | Dornenranke | Bloom | Physical | 100 |
| Level | 11 | Sandschleuder | Stone | Special | 80 |
| Level | 17 | Strudelzug | Tide | Special | 90 |
| Level | 18 | Heiltau | Bloom | Status | 70 |
| Level | 22 | Saugwurzel | Bloom | Special | 90 |
| Level | 22 | Dissonanz | Sound | Special | 100 |
| Level | 25 | Taktgeber | Sound | Status | 50 |
| Level | 29 | Sonnentrunk | Bloom | Status | 90 |
| Level | 34 | Blütensturm | Bloom | Special | 130 |
| Level | 48 | Urwaldzorn | Bloom | Physical | 110 |
| Evolution | – | Taktbruch | Sound | Special | 100 |

Passiv: Photosynth, Wurzelkraft, Taktgefühl, Lichtbrecher (versteckt)

Crescendo: Urwaldchor ★, Dornenmeer, Sinfonie der Welt, Großer Takt · Feld: Rankenbrücke

### 7.2 Starter-Linie Stein

**Brokk** (ECHO_004)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Kieselwurf | Stone | Physical | 60 |
| Level | 1 | Grundfeste | Stone | Status | 80 |
| Level | 13 | Sandschleuder | Stone | Special | 80 |
| Level | 24 | Felsrammen | Stone | Physical | 80 |
| Level | 26 | Splitterfalle | Stone | Status | 50 |
| Level | 27 | Nesselpeitsche | Venom | Physical | 90 |
| Level | 31 | Bergrücken | Stone | Status | 60 |
| Level | 31 | Gerölllawine | Stone | Physical | 150 |
| Level | 41 | Phantomklaue | Spirit | Physical | 120 |
| Egg | – | Schallwand | Sound | Status | 50 |
| Egg | – | Korrosion | Venom | Status | 60 |
| Egg | – | Schwelbrand | Ember | Status | 60 |

Passiv: Bergruhe, Morgenwache (versteckt)

Crescendo: Bergsturz, Ewiger Fels ★ · Feld: Erzspur

**Torgrath** (ECHO_006)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Kieselwurf | Stone | Physical | 60 |
| Level | 1 | Schwerefaust | Gravity | Physical | 60 |
| Level | 13 | Steinhaut | Stone | Status | 60 |
| Level | 13 | Nesselpeitsche | Venom | Physical | 90 |
| Level | 14 | Sandschleuder | Stone | Special | 80 |
| Level | 17 | Felsrammen | Stone | Physical | 80 |
| Level | 23 | Grundfeste | Stone | Status | 80 |
| Level | 29 | Phantomklaue | Spirit | Physical | 120 |
| Level | 29 | Gravistoß | Gravity | Special | 100 |
| Level | 33 | Umkehrfeld | Gravity | Status | 50 |
| Level | 40 | Erdanziehung | Gravity | Physical | 110 |
| Level | 41 | Geröllschauer | Stone | Physical | 110 |
| Level | 50 | Monolithstoß | Stone | Physical | 120 |
| Evolution | – | Singularität | Gravity | Special | 140 |

Passiv: Anziehung, Massenträgheit, Morgenwache (versteckt)

Crescendo: Bergsturz, Ewiger Fels ★, Ereignishorizont, Schwerkraftsturz · Feld: Felsbrecher

### 7.3 Starter-Linie Sturm

**Wisplet** (ECHO_007)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Böenhieb | Storm | Physical | 80 |
| Level | 1 | Klingenwind | Storm | Special | 80 |
| Level | 16 | Böenchor | Storm | Status | 50 |
| Level | 18 | Rückenwindschlag | Storm | Physical | 100 |
| Level | 20 | Magnetpuls | Metal | Special | 90 |
| Level | 23 | Sturmlauf | Storm | Status | 60 |
| Level | 31 | Fortissimo | Sound | Special | 120 |
| Level | 34 | Gewitterruf | Storm | Status | 50 |
| Level | 36 | Kettenblitz | Storm | Special | 110 |
| Egg | – | Spiegelwand | Crystal | Status | 60 |
| Egg | – | Schleichendes Gift | Venom | Status | 70 |
| Egg | – | Heilschein | Light | Status | 90 |

Passiv: Kettenfunke, Formelgeist (versteckt)

Crescendo: Himmelszorn ★, Orkanschwinge · Feld: Aufwind

**Zephyrion** (ECHO_009)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Flatterschlag | Storm | Physical | 90 |
| Level | 1 | Sonnenhieb | Light | Physical | 70 |
| Level | 8 | Böenhieb | Storm | Physical | 80 |
| Level | 11 | Enthüllung | Light | Status | 70 |
| Level | 21 | Rückenwindschlag | Storm | Physical | 100 |
| Level | 24 | Gewitterruf | Storm | Status | 50 |
| Level | 25 | Blendschein | Light | Special | 90 |
| Level | 27 | Böenchor | Storm | Status | 50 |
| Level | 30 | Taktgeber | Sound | Status | 50 |
| Level | 36 | Zyklonsprung | Storm | Physical | 120 |
| Level | 39 | Morgenrot | Light | Physical | 110 |
| Level | 42 | Stahlsturm | Metal | Physical | 120 |
| Level | 49 | Donnerkeil | Storm | Special | 120 |
| Evolution | – | Prismenstrahl | Light | Special | 110 |

Passiv: Kettenfunke, Rückenwindgeist, Formelgeist (versteckt)

Crescendo: Himmelszorn ★, Orkanschwinge, Zenitfeuer, Morgenweihe · Feld: Lichtsignal

### 7.4 Weitere Beispiele

**Sengrath** (ECHO_122)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Funkenbiss | Ember | Physical | 60 |
| Level | 1 | Kieselwurf | Stone | Physical | 60 |
| Level | 6 | Glutfunke | Ember | Special | 60 |
| Level | 8 | Schwelbrand | Ember | Status | 60 |
| Level | 10 | Felsrammen | Stone | Physical | 80 |
| Level | 19 | Dornenranke | Bloom | Physical | 100 |
| Level | 24 | Sonnenesse | Ember | Status | 50 |
| Level | 24 | Brandungsschlag | Tide | Physical | 100 |
| Level | 25 | Aschewirbel | Ember | Special | 80 |
| Level | 29 | Glutklaue | Ember | Physical | 100 |
| Level | 31 | Splitterfalle | Stone | Status | 50 |
| Level | 39 | Schmelzhieb | Ember | Physical | 110 |
| Level | 47 | Esseneruption | Ember | Special | 130 |
| Evolution | – | Erdgrollen | Stone | Special | 140 |

Passiv: Glutherz, Standfest, Sturmauge (versteckt)

Crescendo: Sonnensturz ★, Phönixlied, Bergsturz, Ewiger Fels · Feld: Glutschmelze

**Uvasil** (ECHO_166)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Raureifhauch | Frost | Special | 70 |
| Level | 1 | Dunkelgriff | Void | Physical | 70 |
| Level | 7 | Leerstoß | Void | Special | 70 |
| Level | 9 | Frostpanzer | Frost | Status | 60 |
| Level | 15 | Verschlingen | Void | Status | 50 |
| Level | 15 | Leerer Raum | Void | Status | 50 |
| Level | 22 | Seelenzehrer | Void | Special | 100 |
| Level | 23 | Frostbiss | Frost | Physical | 90 |
| Level | 24 | Stille Klinge | Void | Physical | 100 |
| Level | 24 | Blendschein | Light | Special | 90 |
| Level | 30 | Prismenfächer | Crystal | Special | 120 |
| Level | 31 | Abgrundwelle | Void | Special | 150 |
| Level | 46 | Nullpunkt | Void | Special | 80 |
| Evolution | – | Winterstille | Frost | Special | 120 |

Passiv: Leerer Blick, Präzisionsfrost, Seelenhunger, Pollenwolke (versteckt)

Crescendo: Ewiger Winter, Eiszeit, Weltlöscher, Große Leere ★ · Feld: Schattenschritt

**Aeth'rion** (ECHO_250)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Rückenwindschlag | Storm | Physical | 100 |
| Level | 1 | Stille Klinge | Void | Physical | 100 |
| Level | 1 | Lichtnadel | Light | Special | 70 |
| Level | 1 | Sonnenhieb | Light | Physical | 70 |
| Level | 1 | Heilschein | Light | Status | 90 |
| Level | 1 | Klangschlag | Sound | Physical | 70 |
| Level | 1 | Trommelschlag | Sound | Physical | 80 |
| Level | 1 | Dissonanz | Sound | Special | 100 |
| Level | 1 | Taktbruch | Sound | Special | 100 |
| Level | 1 | Taktgeber | Sound | Status | 50 |
| Level | 1 | Resonanzkreis | Sound | Status | 50 |
| Level | 60 | Fortissimo | Sound | Special | 120 |
| Level | 69 | Donnerhall | Sound | Special | 130 |

Passiv: Einklang

Crescendo: Zenitfeuer, Morgenweihe, Sinfonie der Welt, Großer Takt ★ · Feld: Lichtsignal

---

## 8. Klangschriften

90 Klangschriften, sechs je Typ, jeweils Mittel-, Spät- oder Status-Fähigkeiten (keine Einstiegs- und keine Schwer-Fähigkeiten – diese gehören dem Lernset bzw. den Tutoren). Klangschriften sind **wiederverwendbar und nicht handelbar** (ADR-017). Fundorte: Arenen (je Akkord eine Schrift des Arena-Typs), Nebenquests, Tiefenresonanzen, Kodex-Meilensteine, Händler (K42) – Verteilung in K41/K42/K49–K51.

| Name | DisplayName | Type |
|---|---|---|
| ITM_KS_001 | Klangschrift: Schwelbrand | Ember |
| ITM_KS_002 | Klangschrift: Hitzeflimmern | Ember |
| ITM_KS_003 | Klangschrift: Sonnenesse | Ember |
| ITM_KS_004 | Klangschrift: Lodernder Ansturm | Ember |
| ITM_KS_005 | Klangschrift: Feueratem | Ember |
| ITM_KS_006 | Klangschrift: Schmelzhieb | Ember |
| ITM_KS_007 | Klangschrift: Regenruf | Tide |
| ITM_KS_008 | Klangschrift: Quellbad | Tide |
| ITM_KS_009 | Klangschrift: Nebelschleier | Tide |
| ITM_KS_010 | Klangschrift: Brandungsschlag | Tide |
| ITM_KS_011 | Klangschrift: Gezeitenwelle | Tide |
| ITM_KS_012 | Klangschrift: Tiefenstrom | Tide |
| ITM_KS_013 | Klangschrift: Felswall | Stone |
| ITM_KS_014 | Klangschrift: Steinhaut | Stone |
| ITM_KS_015 | Klangschrift: Bergrücken | Stone |
| ITM_KS_016 | Klangschrift: Gerölllawine | Stone |
| ITM_KS_017 | Klangschrift: Felsrammen | Stone |
| ITM_KS_018 | Klangschrift: Erdgrollen | Stone |
| ITM_KS_019 | Klangschrift: Gewitterruf | Storm |
| ITM_KS_020 | Klangschrift: Sturmlauf | Storm |
| ITM_KS_021 | Klangschrift: Böenchor | Storm |
| ITM_KS_022 | Klangschrift: Zyklonsprung | Storm |
| ITM_KS_023 | Klangschrift: Blitzbogen | Storm |
| ITM_KS_024 | Klangschrift: Wirbelsturm | Storm |
| ITM_KS_025 | Klangschrift: Heiltau | Bloom |
| ITM_KS_026 | Klangschrift: Sonnentrunk | Bloom |
| ITM_KS_027 | Klangschrift: Wuchern | Bloom |
| ITM_KS_028 | Klangschrift: Blütensturm | Bloom |
| ITM_KS_029 | Klangschrift: Saugwurzel | Bloom |
| ITM_KS_030 | Klangschrift: Dornenranke | Bloom |
| ITM_KS_031 | Klangschrift: Eisspiegel | Frost |
| ITM_KS_032 | Klangschrift: Kältestarre | Frost |
| ITM_KS_033 | Klangschrift: Weißer Atem | Frost |
| ITM_KS_034 | Klangschrift: Frostbiss | Frost |
| ITM_KS_035 | Klangschrift: Gletscherdruck | Frost |
| ITM_KS_036 | Klangschrift: Winterstille | Frost |
| ITM_KS_037 | Klangschrift: Lichtschlucker | Void |
| ITM_KS_038 | Klangschrift: Leerer Raum | Void |
| ITM_KS_039 | Klangschrift: Entzugsfluch | Void |
| ITM_KS_040 | Klangschrift: Schweigeschnitt | Void |
| ITM_KS_041 | Klangschrift: Stille Klinge | Void |
| ITM_KS_042 | Klangschrift: Hohlklang | Void |
| ITM_KS_043 | Klangschrift: Läuterung | Light |
| ITM_KS_044 | Klangschrift: Heilschein | Light |
| ITM_KS_045 | Klangschrift: Sonnenwehr | Light |
| ITM_KS_046 | Klangschrift: Strahlenkranz | Light |
| ITM_KS_047 | Klangschrift: Morgenrot | Light |
| ITM_KS_048 | Klangschrift: Prismenstrahl | Light |
| ITM_KS_049 | Klangschrift: Giftkleid | Venom |
| ITM_KS_050 | Klangschrift: Korrosion | Venom |
| ITM_KS_051 | Klangschrift: Schleichendes Gift | Venom |
| ITM_KS_052 | Klangschrift: Toxinwelle | Venom |
| ITM_KS_053 | Klangschrift: Nesselpeitsche | Venom |
| ITM_KS_054 | Klangschrift: Miasma | Venom |
| ITM_KS_055 | Klangschrift: Rüstwerk | Metal |
| ITM_KS_056 | Klangschrift: Konterhieb | Metal |
| ITM_KS_057 | Klangschrift: Panzerplatten | Metal |
| ITM_KS_058 | Klangschrift: Schrapnell | Metal |
| ITM_KS_059 | Klangschrift: Stahlsturm | Metal |
| ITM_KS_060 | Klangschrift: Magnetpuls | Metal |
| ITM_KS_061 | Klangschrift: Doppelgänger | Spirit |
| ITM_KS_062 | Klangschrift: Seelenband | Spirit |
| ITM_KS_063 | Klangschrift: Verschwinden | Spirit |
| ITM_KS_064 | Klangschrift: Totenklage | Spirit |
| ITM_KS_065 | Klangschrift: Phantomklaue | Spirit |
| ITM_KS_066 | Klangschrift: Schreckensschrei | Spirit |
| ITM_KS_067 | Klangschrift: Aufladen | Crystal |
| ITM_KS_068 | Klangschrift: Spiegelwand | Crystal |
| ITM_KS_069 | Klangschrift: Drusenfeld | Crystal |
| ITM_KS_070 | Klangschrift: Kristallregen | Crystal |
| ITM_KS_071 | Klangschrift: Klirrschlag | Crystal |
| ITM_KS_072 | Klangschrift: Facettenschnitt | Crystal |
| ITM_KS_073 | Klangschrift: Schallwand | Sound |
| ITM_KS_074 | Klangschrift: Resonanzkreis | Sound |
| ITM_KS_075 | Klangschrift: Wiegenlied | Sound |
| ITM_KS_076 | Klangschrift: Taktbruch | Sound |
| ITM_KS_077 | Klangschrift: Fortissimo | Sound |
| ITM_KS_078 | Klangschrift: Dissonanz | Sound |
| ITM_KS_079 | Klangschrift: Umkehrfeld | Gravity |
| ITM_KS_080 | Klangschrift: Schwebe | Gravity |
| ITM_KS_081 | Klangschrift: Gewichtslast | Gravity |
| ITM_KS_082 | Klangschrift: Singularität | Gravity |
| ITM_KS_083 | Klangschrift: Implosion | Gravity |
| ITM_KS_084 | Klangschrift: Erdanziehung | Gravity |
| ITM_KS_085 | Klangschrift: Umkehrrune | Arcane |
| ITM_KS_086 | Klangschrift: Fluchwort | Arcane |
| ITM_KS_087 | Klangschrift: Glyphenkreis | Arcane |
| ITM_KS_088 | Klangschrift: Siegelbruch | Arcane |
| ITM_KS_089 | Klangschrift: Bannzeichen | Arcane |
| ITM_KS_090 | Klangschrift: Spiegelformel | Arcane |

---

## 9. Tutoren

30 Tutoren lehren je Typ zwei Fähigkeiten – bevorzugt die **schwere** Fähigkeit des Typs und eine weitere, die weder Klangschrift noch Einstieg ist. Tutoren sind Fraktionslehrer: Sie verlangen Rufrang 3 bzw. 4 (K47) und Sol (K42). So wird Ruf zu einer Machtquelle ohne Pay-to-Win (CANON §8).

| Tutor | Ability | Type | Faction | ReputationRank | CostSol |
|---|---|---|---|---|---|
| TUT_EMBER_1 | ABL_A008 | Ember | F01 | 3 | 2000 |
| TUT_EMBER_2 | ABL_A003 | Ember | F02 | 4 | 3500 |
| TUT_TIDE_1 | ABL_A019 | Tide | F02 | 3 | 2000 |
| TUT_TIDE_2 | ABL_A014 | Tide | F03 | 4 | 3500 |
| TUT_STONE_1 | ABL_A030 | Stone | F03 | 3 | 2000 |
| TUT_STONE_2 | ABL_A027 | Stone | F04 | 4 | 3500 |
| TUT_STORM_1 | ABL_A042 | Storm | F04 | 3 | 2000 |
| TUT_STORM_2 | ABL_A040 | Storm | F05 | 4 | 3500 |
| TUT_BLOOM_1 | ABL_A054 | Bloom | F05 | 3 | 2000 |
| TUT_BLOOM_2 | ABL_A056 | Bloom | F01 | 4 | 3500 |
| TUT_FROST_1 | ABL_A066 | Frost | F01 | 3 | 2000 |
| TUT_FROST_2 | ABL_A065 | Frost | F02 | 4 | 3500 |
| TUT_VOID_1 | ABL_A079 | Void | F02 | 3 | 2000 |
| TUT_VOID_2 | ABL_A076 | Void | F03 | 4 | 3500 |
| TUT_LIGHT_1 | ABL_A090 | Light | F03 | 3 | 2000 |
| TUT_LIGHT_2 | ABL_A087 | Light | F04 | 4 | 3500 |
| TUT_VENOM_1 | ABL_A103 | Venom | F04 | 3 | 2000 |
| TUT_VENOM_2 | ABL_A101 | Venom | F05 | 4 | 3500 |
| TUT_METAL_1 | ABL_A114 | Metal | F05 | 3 | 2000 |
| TUT_METAL_2 | ABL_A111 | Metal | F01 | 4 | 3500 |
| TUT_SPIRIT_1 | ABL_A132 | Spirit | F01 | 3 | 2000 |
| TUT_SPIRIT_2 | ABL_A124 | Spirit | F02 | 4 | 3500 |
| TUT_CRYSTAL_1 | ABL_A138 | Crystal | F02 | 3 | 2000 |
| TUT_CRYSTAL_2 | ABL_A136 | Crystal | F03 | 4 | 3500 |
| TUT_SOUND_1 | ABL_A151 | Sound | F03 | 3 | 2000 |
| TUT_SOUND_2 | ABL_A152 | Sound | F04 | 4 | 3500 |
| TUT_GRAVITY_1 | ABL_A162 | Gravity | F04 | 3 | 2000 |
| TUT_GRAVITY_2 | ABL_A159 | Gravity | F05 | 4 | 3500 |
| TUT_ARCANE_1 | ABL_A177 | Arcane | F05 | 3 | 2000 |
| TUT_ARCANE_2 | ABL_A173 | Arcane | F01 | 4 | 3500 |

---

## 10. Signaturkonzepte

Die Signaturkonzepte des Katalogs (K20–K27) werden auf drei Ebenen umgesetzt:

| Ebene | Umsetzung | Kapitel |
|---|---|---|
| Mechanik | Legendäre/Mythische: Feldklang (§4). Endformen mit „Crescendo –“-Konzept: Crescendo-Zuordnung in K30 | K29/K30 |
| Präsentation | Jede Art führt ihre **Evolutionsfähigkeit** mit eigener Signatur-Inszenierung aus (Klangmal-VFX, Ruf-Sample) | K57/K58 |
| Kodex | Das Signaturkonzept steht als Verhaltensbeobachtung im Kodex (Stufe 3) | K39 |

So bleiben 256 Signaturen erhalten, ohne 256 Sonderregeln zu erzeugen (Balancing-Last, DR-25).

---

## 11. Validierung und Kennzahlen

| Regel | Inhalt | Ergebnis |
|---|---|---|
| LS-01 | Alle referenzierten Fähigkeiten existieren | ✔ |
| LS-02 | 8–14 Level-Einträge je Art | ✔ (9–13, Ø 11,3) |
| LS-03 | ≥ 60 % eigene Typen, ≥ 2 Fremdtyp-Fähigkeiten | ✔ |
| LS-04 | ≥ 1 Status-Fähigkeit bis Lv. 20 | ✔ |
| LS-05 | ≥ 2 Fähigkeiten auf Lv. 1 | ✔ |
| LS-06 | Schwer-Fähigkeit des Primärtyps nicht vor Lv. 36 | ✔ |
| LS-07 | Evolutionsfähigkeit ab Stufe 2 | ✔ |
| LS-08 | Passiv-Optionen 1–3 + 1 versteckt; Legendäre genau ihr Feldklang | ✔ |
| LS-09 | 90 eindeutige Klangschriften | ✔ |
| LS-10 | 30 Tutor-Fähigkeiten | ✔ |
| LS-11 | Jede aktive Fähigkeit irgendwo erlernbar | ✔ (alle 180 bereits über Lernset/Evolution/Ei) |
| LS-12 | Jede Passive mindestens einer Art zugeordnet | ✔ |

**Kennzahlen:** 2.896 Level-Einträge · 133 Evolutionsfähigkeiten · 321 Ei-Fähigkeiten · 756 Passiv-Optionen. Am häufigsten gelernt: Dissonanz (52), Felsrammen (49), Fortissimo (48); am seltensten: Blitzbogen und Kettenblitz (je 3) – Kandidaten für Klangschrift-Umschichtung in K63, falls Telemetrie (K66) sie als „nie gesehen“ ausweist.

---

## 12. Code

### 12.1 Daten

```cpp
// AethrisCore – Lernset-Eintrag (Import aus Learnsets.csv; Fragment am UEchoSpeciesDefinition)
UENUM() enum class ELearnMethod : uint8 { Level, Evolution, Egg, Klangschrift, Tutor };

USTRUCT() struct FLearnsetEntry
{
    GENERATED_BODY()
    UPROPERTY() ELearnMethod Method = ELearnMethod::Level;
    UPROPERTY() uint8 Level = 1;                            // 0 bei Evolution/Ei
    UPROPERTY() TSoftObjectPtr<UAbilityDefinition> Ability;
};

USTRUCT() struct FPassiveOption
{
    GENERATED_BODY()
    UPROPERTY() TSoftObjectPtr<UAbilityDefinition> Ability;
    UPROPERTY() bool bHidden = false;
};
```

### 12.2 Lernen beim Levelaufstieg (GF_Progression)

```cpp
void UEchoProgressionService::OnLevelUp(FEchoInstance& Echo, int32 NewLevel)
{
    const UEchoSpeciesDefinition* Sp = Species(Echo);
    for (const FLearnsetEntry& E : Sp->Learnset)
    {
        if (E.Method != ELearnMethod::Level || E.Level != NewLevel) continue;
        const FPrimaryAssetId Id = E.Ability.ToSoftObjectPath().GetAssetPathName();
        if (Echo.Repertoire.Contains(Id)) continue;
        Echo.Repertoire.Add(Id);                                   // nie vergessen (CANON §97)
        Bus->Broadcast(TAG_Echo_AbilityLearned, FAbilityLearnedMessage{ Echo.Guid, Id, /*bOfferSlot*/ true });
    }
}
```

### 12.3 Klangschrift-Kompatibilität

```cpp
bool CanUseKlangschrift(const FEchoInstance& Echo, const UAbilityDefinition& A)
{
    const FGameplayTagContainer Types = SpeciesTypes(Echo);        // 1–2 Typen
    return Types.HasTagExact(A.Type) || CoverageTypes(Echo).HasTagExact(A.Type);
}
```

`CoverageTypes` wird **nicht** zur Laufzeit berechnet, sondern beim Import in die Artdefinition geschrieben (`CoverageTypes`-Feld) – identisch zur Python-Berechnung.

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-098 | Lernsets werden regelbasiert generiert (deterministisch), Overrides nur per Datei | 256 Arten × ~13 Einträge konsistent halten; Diffs lesbar | Handpflege (inkonsistent), Zufall (nicht reproduzierbar) |
| ADR-099 | Jede Art hat zwei Abdeckungstypen aus der Typtabelle | Jedes Echo hat eine Antwort auf seine Konter (DR-08) | freie Klangschrift-Kompatibilität (homogenisiert Arten) |
| ADR-100 | Feldklang als exklusive Passive der 16 Legendären/Mythischen | Besondere Kämpfe ohne Werte-Inflation | höhere Basiswerte (unfair), Sonder-Aktive (zu viele Sonderfälle) |
| ADR-101 | Versteckte Passive stammt aus einem Fremdtyp | Entdeckung, Forschung (Kodex 4), Zuchtziel | versteckte = stärkere Variante (Pay-to-Grind) |
| ADR-102 | Tutoren lehren bevorzugt Schwer-Fähigkeiten gegen Fraktionsruf | Ruf wird Macht ohne Shop | Schwer-Fähigkeiten als Klangschrift (zu früh verfügbar) |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §102 | Passive: 6 je Typ (90), 1 aktive Passive je Echo, 1–3 sichtbare + 1 versteckte Option (Fremdtyp), Wildverteilung 60/30/10, Wechsel per Wandelklang, Freischaltung versteckt über Kodex 4 oder Zucht; Auslöserliste und statische Primitiva mit Deckeln | LOCKED |
| §103 | 16 Feldklänge (Legendäre/Mythische), einer gleichzeitig aktiv, nicht Ranked, je eigenes Primitiv | LOCKED |
| §104 | Lernsets generiert (`gen_learnsets.py`): Lernstufen E/M/S/L/H, Zusammensetzung K29 §6.2, Zielgrößen 9–13, Regeln LS-01…LS-12; 2 Abdeckungstypen je Art | LOCKED |
| §105 | Klangschriften `ITM_KS_001–090` (6 je Typ, Mittel/Spät/Status), Kompatibilität Typ oder Abdeckungstyp; Tutoren 30 (2 je Typ, Rufrang 3–4, Sol) | LOCKED (Fundorte/Kosten → K41/K42/K47) |
| §10 | ADR-098 – ADR-102 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] 90 passive Fähigkeiten (6 je Typ) mit Auslösern, validiert
- [x] 16 Feldklänge der Ursprungsstimmen und Mythischen (Signaturkonzepte K27 umgesetzt)
- [x] Passiv-Optionen für alle 256 Arten (1–3 + versteckt)
- [x] Lernsets aller 256 Arten (Level, Evolution, Ei) – generiert, deterministisch, validiert
- [x] 90 Klangschriften und 30 Tutoren als Daten
- [x] Jede aktive Fähigkeit erlernbar, jede Passive vergeben
- [x] Code: Lernset-Strukturen, Levelaufstieg, Klangschrift-Kompatibilität
- [x] ADR-098 – ADR-102, CANON §102–§105

➡️ **Nächstes Kapitel: K30 – Fähigkeiten III: Crescendos (ABL_U001–U030) und Feldfähigkeiten (ABL_F001–F030).**
