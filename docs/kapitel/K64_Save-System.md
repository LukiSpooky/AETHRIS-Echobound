# K64 · Save-System

| Feld | Wert |
|---|---|
| Dokument | Kapitel 64 von 68 · Technik III |
| Version | 1.0 |
| Owner | Technical Director, Lead Gameplay Programmer (Save) |
| Mitwirkende | Plattform-Programmierung (PS5, Xbox, Switch 2, PC), Online Engineer (Cross-Save), QA Lead (Save-Tests), Systems Designer (Eiserner Wärter), Narrative (Finale-Slot) |
| Baut auf | K03 (Profil vs. Weltstand, 3 Slots + Eiserner Wärter, CANON §17), K06 §10 (Save-Architektur SA-01–SA-06, CANON §32), K09 (Zonenfixierung `World.Zones`), K14 (Wetterfahrplan, CR-001), K46 (Finale-Speicherpunkt, ADR-176), K48 (Quest-Fragmente, StepId-Migration), K52/K53 (Population, NPCs), K59–K62 (Online-, Koop-, PvP-, Endgame-Fragmente) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Save/Fragments.csv` (36 Fragmente), `AutosaveTriggers.csv`; Referenzmodell `tools/ref/aethris_save.py` (Container, Größen, SV-01–SV-06, Testvektor); `GF_Save/…/AethrisSaveContainer.h/.cpp`, `AethrisSaveSubsystem.h/.cpp`; `FAethrisSaveHeader` ContainerVersion 2 |
| Neue Kanon-Einträge | CANON §252 (Container v2 und Fragment-Register), §253 (Slots, Autosave, Eiserner Wärter, Finale), §254 (Migration, Fehlertoleranz, Plattformen, Cloud/Cross-Save), §255 (Tests und Budgets) |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Container-Format v2](#2-container-format-v2)
3. [Fragment-Register](#3-fragment-register)
4. [Slots und Autosave](#4-slots-und-autosave)
5. [Plattformen, Cloud und Cross-Save](#5-plattformen-cloud-und-cross-save)
6. [Versionierung und Migration](#6-versionierung-und-migration)
7. [Fehlertoleranz](#7-fehlertoleranz)
8. [Determinismus und „Save-Scumming“](#8-determinismus-und-save-scumming)
9. [Leistung](#9-leistung)
10. [UX](#10-ux)
11. [Tests](#11-tests)
12. [Prüfregeln](#12-prüfregeln)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Ziele

Ein Monster-Sammel-Rollenspiel lebt davon, dass Spielende ihren Echos über Jahre treu bleiben. Ein verlorener Spielstand zerstört dieses Vertrauen. Das Save-System hat deshalb fünf Ziele:

| Ziel | Bedeutung | Messbar an |
|---|---|---|
| **SZ-1 Nie verlieren** | Kein Szenario (Absturz, Stromausfall, voller Speicher, Update) führt zum Totalverlust | Stromausfall-Tests 1.000×, 0 Totalverlust |
| **SZ-2 Unsichtbar** | Speichern unterbricht nie das Spiel; kein Ruckler, kein Ladebildschirm | Game-Thread-Anteil ≤ 4 ms je Autosave |
| **SZ-3 Langlebig** | Spielstände aus Version 1.0 laden in jeder späteren Version | Golden-Save-Korpus in CI |
| **SZ-4 Überall** | Plattform-Cloud, optional Cross-Save zwischen Plattformen | Cross-Save-Tests aller Paare |
| **SZ-5 Klein** | Ein Weltstand bleibt deutlich unter Plattformgrenzen | ≤ 2,5 MB unkomprimiert (SV-04) |

Ein Spielstand ist in AETHRIS mehr als eine Datei: Er ist die Geschichte einer Person mit ihren Echos – wer welches Echo an welchem Ort bei welchem Wetter gebunden hat, steht im Ursprung jeder Instanz und begleitet das Echo durch Tausch, Zucht und Plattformwechsel. Das Save-System behandelt diese Geschichte mit derselben Sorgfalt wie Server Online-Transaktionen.

Die Grundprinzipien SA-01–SA-06 aus K06 §10 (CANON §32) gelten unverändert: fragmentiert, versioniert je Fragment, fehlertolerant, unbekannte Fragmente mitschleppen, atomar mit drei rotierenden Kopien, explizite Serialisierung.

---

## 2. Container-Format v2

K06 legte Kopf, Verzeichnis und Fragmente fest. K64 ergänzt **CRC32 je Fragment**, damit ein beschädigtes Fragment einzeln erkannt und zurückgesetzt werden kann, ohne den Rest zu verwerfen (SA-03). Der Container ist plattformneutral (Little Endian); Kompression (Oodle) und Verschlüsselung übernimmt die Plattform-Schicht.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ u32 Magic 'AETH' · u32 ContainerVersion (2) · u32 HeaderSize                 │
│ Header: Build · SavedAtUnix · PlayTimeSec · Region · Wärterrang · Akkorde ·  │
│         Chor-Vorschau (≤ 6 Arten)                                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ u32 FragmentCount                                                            │
│ je Fragment: Id (UTF-8) · u32 Version · u32 Offset · u32 Size · u32 CRC32    │
├──────────────────────────────────────────────────────────────────────────────┤
│ Nutzlast: Fragmente hintereinander (explizit serialisiert, SA-06)            │
├──────────────────────────────────────────────────────────────────────────────┤
│ u32 PayloadCRC32                                                             │
└──────────────────────────────────────────────────────────────────────────────┘
```

Die Referenzimplementierung (`aethris_save.py`) und der C++-Code (`Aethris::Save::WriteContainer/ReadContainer`) erzeugen dieselben Bytes; der Testvektor (zwei Fragmente, Header mit Region R03, Rang 17, 5 Akkorden) lautet:

```
41455448020000003f0000000b00312e302e302d434c31323380d8db700000000040db020000000000030052303311000000050000000208004543484f5f30303108004543484f5f30363702000000040043686f7203000000000000001000000088e2cece0b00576f726c642e5a6f6e6573010000001000000004000000cdfb3cb6000102030405060708090a0b0c0d0e0f01020304a074121d
```

**Vorwärtskompatibilität:** Der Header trägt seine Größe; ein älterer Build überspringt unbekannte Header-Felder. Unbekannte Fragmente werden als Rohbytes gelesen und beim nächsten Speichern unverändert zurückgeschrieben (SA-04) – wichtig, wenn ein Spielstand über die Cloud zwischen Geräten mit unterschiedlichen Patch-Ständen wandert.

---

## 3. Fragment-Register

Alle Fragmente stehen in `Data/Save/Fragments.csv`. Jedes Kapitel, das ein Fragment nennt, muss es dort eintragen (Prüfregel SV-01 durchsucht alle Kapitel). Die Größen sind **Obergrenzen** (maximale Anzahl × Bytes je Eintrag), nicht typische Werte.

| Fragment | Owner | Version | Inhalt | Obergrenze unkomprimiert |
|---|---|---|---|---|
| `Sanctuary` | GF_Companion | v1 | Resonanzhain: Gärten, Ausbaustufen, Echos (max. 600), Deko | 140,6 KB |
| `Player.GhostTeams` | GF_PvP | v1 | Geister-Teams der Woche (30 × 6 Echos, kompakt) | 16,9 KB |
| `Player.CoopLedger` | GF_Multiplayer | v1 | Gast-Protokoll der letzten Sitzung bis zur Anwendung | 12,5 KB |
| `Player.Photos` | GF_Research | v1 | Fotobewertungen, Album-Verweise (Bilder separat) | 11,7 KB |
| `Player.Memories` | GF_Quests | v1 | Tagebuch-Erinnerungen („Gemeinsam erlebt“, Abschiede) | 9,4 KB |
| `World.Population` | GF_AI | v1 | Bestand je (Zone, Art), letzte Tagesrechnung | 8,6 KB |
| `World.Nodes` | GF_Economy | v1 | Ressourcen-Knoten: Nachwachs-Zeitpunkte (nur geerntete) | 6,2 KB |
| `Player.Quests` | GF_Quests | v2 | Questzustände, aktueller Schritt, Ziele, StepId-Migration | 6,2 KB |
| `Kodex` | GF_Research | v1 | Forschungsstufen 256 × 4, Klangfragmente, Lore-Funde | 5,5 KB |
| `Inventory` | GF_Inventory | v2 | Gegenstände, Mengen, Sol, Taschenplätze | 4,7 KB |
| `World.Npcs` | GF_AI | v1 | NPC-Zustände (Abweichungen vom Tagesplan, Beziehungen, Barks gehört) | 4,5 KB |
| `Player.Map` | GF_World | v1 | Entdeckte POIs, Resonanzsteine, Kartenschleier (Bitfeld je 128-m-Zelle) | 4,4 KB |
| `Player.TradeDeltas` | GF_Multiplayer | v1 | Offene Tausch-Deltas, Echos „unterwegs“ | 2,9 KB |
| `Breeding` | GF_Breeding | v1 | Brutnischen, laufende Zuchten (Seed, Eltern), Zuchtbuch | 2,5 KB |
| `Chor` | GF_Monsters | v3 | Aktive Echos (FEchoInstance, max. 6) | 1,4 KB |
| `Equipment` | GF_Inventory | v1 | Wärter-Ausrüstung I–V, Halteitems-Zuordnung, Garderobe | 1,4 KB |
| `World.Settlements` | GF_World | v1 | Siedlungszustände 0/1/2, Feste, Händlerstand | 1,2 KB |
| `Crafting` | GF_Economy | v1 | Bekannte Rezepte, Reifungen, Händler-Rotation (Spieltag) | 1,2 KB |
| `World.QuestConsequences` | GF_Quests | v1 | Dauerhafte Weltänderungen aus Quests (Data-Layer-Schalter, NPC-Umzüge) | 1,2 KB |
| `Player.StoryFlags` | GF_Quests | v1 | Story-Flags (Haltungen, Entscheidungen, Wahrheitsstufen, Ende) | 0,9 KB |
| `World.Zones` | GF_World | v1 | Fixierte Zonenbänder (ADR-044) | 0,6 KB |
| `Player.Endgame` | GF_Combat | v1 | Tiefen je Ort, Spieltag-Erstabschlüsse, Meisterschaften | 0,5 KB |
| `Player.Tutorials` | GF_UI | v1 | Gesehene Hinweise, Einführungsstand | 0,3 KB |
| `Meta.Header` | GF_Save | v1 | Header, Vorschau (Region, Rang, Akkorde, Chor), Spielzeit, Build | 0,2 KB |
| `Player.Mythics` | GF_Quests | v1 | Fortschritt der sechs Mythischen Wege | 0,2 KB |
| `Warden` | GF_Companion | v1 | Wärterrang, Wärter-EP, Skilltree (48 Fähigkeiten), Titel | 0,2 KB |
| `Player.Reputation` | GF_Quests | v1 | Ruf je Fraktion, Tageskappen, Rang-Belohnungen | 0,2 KB |
| `Player.Social` | GF_Multiplayer | v1 | Zirkel-Verweis, Grußgaben-Zähler, Gesten-Freischaltungen | 0,1 KB |
| `World.Time` | GF_World | v1 | Spielzeit, Spieltag, Mondphase, Wetter-Fahrplan-Seed, aktive Overrides | 0,1 KB |
| `Player.TimeTrials` | GF_World | v1 | Taktproben-Bestzeiten | 0,1 KB |
| `Traversal` | GF_World | v1 | Freigeschaltete Traversal-Fähigkeiten, Reitarten, Gleiter, Ausdauer-Boni | 0,1 KB |
| `Player.Position` | GF_World | v1 | Ort, Blickrichtung, aktiver Resonanzstein, Reittier | 0,1 KB |
| **Σ Weltstand** | | | | **247 KB** (komprimiert ≈ 86 KB) |

| Profil-Fragment | Owner | Version | Inhalt | Obergrenze |
|---|---|---|---|---|
| `Profile.Settings` | GF_UI | v1 | Einstellungen inkl. Barrierefreiheit, Steuerung, Audio, Grafik | 2,0 KB |
| `Profile.Achievements` | GF_Save | v1 | Erfolge, Titel, Meisterschafts-Akkord | 0,9 KB |
| `Profile.PvP` | GF_PvP | v1 | Saisonstufen (Cache), Replays-Liste | 0,9 KB |
| `Profile.PhotoAlbum` | GF_Research | v1 | Fotoalbum (Bilder als eigene Dateien, max. 500 × 200 KB) | 7,8 KB |
| **Σ Profil (ohne Bilder)** | | | | **4 KB** |

**Lesart:** Der größte Brocken ist der Resonanzhain (600 Echos × 240 Byte = 141 KB). Ein `FEchoInstance` (CANON §29) umfasst InstanceId (16), Art (4), Spitzname (≤ 24), Level/EP (8), Bindung (4), Persönlichkeit (1), Anlagen (8), Schliff (8), Genom (Loci, Morph, Mutationen ≈ 24), Lernset und Kampfset (≈ 24), Halteitem (4), Ursprung (Wärter, Zone, Wetter, Zeit, Methode, Eltern, Signatur ≈ 96), Status/Flags (≈ 19) – zusammen ≈ 240 Byte. Ein vollständiger Weltstand bleibt unter 250 KB, komprimiert unter 100 KB.

### 3.1 Aufbau einer Echo-Instanz im Save

| Feld | Bytes | Inhalt |
|---|---|---|
| InstanceId | 16 | FGuid, weltweit eindeutig (auch über Tausch hinweg) |
| Species | 4 | Index in die Artentabelle (über Namens-Tabelle im Fragment-Kopf, nicht roh) |
| Nickname | 1 + ≤ 23 | UTF-8, leer = Artname |
| Level, Experience | 1 + 4 | Level 1–100, Gesamt-EP |
| Bond | 2 | Bindungspunkte 0–1.000 (Stufen K37) |
| Personality | 1 | Index (16 Persönlichkeiten) |
| Aptitudes | 8 | 8 × Anlage 0–15 (4 Bit genügten; Byte für Lesbarkeit) |
| Polish | 6 + 2 | 6 × Schliff 0–80, Sperren (PolishLocks) |
| Genome | 24 | 6 Loci × (A, B), Morph, Mutationen |
| Learnset/Kampfset | 24 | 4 aktive + 1 Crescendo + Passiv-Auswahl, gelernte Tutor-Fähigkeiten (Bitfeld) |
| HeldItem | 4 | Item-Index oder 0 |
| Origin | 96 | Erstwärter (Konto-Hash), Zone, Wetter, Tageszeit, Spieltag, UTC, Methode, Eltern-IDs (2 × 16), Signatur (32) |
| Status, Flags | 19 | aktuelle HP, Erschöpfung, „unterwegs“ (Tausch), Leih-Echo, Favorit, Reittier-Zubehör |

Arten, Items und Fähigkeiten werden im Fragment über eine **Namens-Tabelle** referenziert (Name → kurzer Index im Fragment). So bleibt ein Save gültig, auch wenn sich die Reihenfolge der Daten ändert; nur die Namen (stabile IDs, CANON §23) zählen.

**Eigentum:** Jedes Fragment gehört genau einem Modul (`Owner`). Das Modul implementiert `ISaveFragmentProvider` (CANON §32) und registriert sich beim `UAethrisSaveSubsystem` (GF_Save). GF_Save kennt keine Features (SA-01, CANON §26).

**Scope:** *World*-Fragmente gehören zu einem Weltstand-Slot, *Profile*-Fragmente zum Profil (Einstellungen, Erfolge, PvP, Fotoalbum – CANON §17). Fotos selbst sind eigene Bilddateien (max. 500 × 200 KB) im Profil-Speicher, das Fragment enthält nur Verweise.

---

## 4. Slots und Autosave

### 4.1 Slots

| Slot | Anzahl | Inhalt | Regeln |
|---|---|---|---|
| Weltstand 1–3 | 3 | Vollständige Welt | manuelles Speichern überall außer Kampf/Zwischensequenz; je Slot 3 rotierende Autosave-Kopien |
| Eiserner Wärter | 1 | Welt im Modus Eiserner Wärter | nur Autosave, keine Kopie, kein manuelles Speichern; Laden nur des letzten Stands |
| Finale-Speicherpunkt | 1 | Stand unmittelbar vor der Finalentscheidung (ADR-176) | wird einmal geschrieben, danach schreibgeschützt; Laden erzeugt eine Kopie in einem Weltstand-Slot |
| Profil | 1 | Einstellungen, Erfolge, PvP, Album | plattformgebunden, Cloud-synchron |

**Neues Spiel bei vollem Slot:** Das Spiel fragt, welcher Slot überschrieben werden soll, und verlangt Halten 3 s (UX-06). Der überschriebene Stand bleibt 7 Tage als Sicherung im Plattform-Speicher (wo die Plattform es erlaubt).

### 4.2 Autosave

| Name | Trigger | Rhythm | Note |
|---|---|---|---|
| AS_STONE | Resonanzstein aktiviert oder Schnellreise | sofort |  |
| AS_QUEST | Quest-Schritt abgeschlossen | sofort |  |
| AS_BOSS | Bosskampf, Arena, Tiefe, Raid beendet | sofort |  |
| AS_BOND | Echo gebunden, entwickelt, geschlüpft, getauscht | sofort |  |
| AS_REGION | Region gewechselt | sofort |  |
| AS_SANCTUARY | Hain-Ausbau, Chor-Tausch | sofort |  |
| AS_TIMER | Zeitintervall ohne anderen Auslöser | alle 10 min Spielzeit | nicht im Kampf, nicht in Zwischensequenz |
| AS_ONLINE | Vor Online-Sitzung (Koop, Tausch, Ranked) | sofort | K59 §6.2 |
| AS_COOP_LEDGER | Koop-Gast: Protokoll sichern | alle 60 s | nur Fragment Player.CoopLedger |
| AS_FINALE | Vor der Finalentscheidung | einmalig | gesonderter Slot (ADR-176) |
| AS_SUSPEND | Konsole geht in Ruhemodus / App verliert Fokus | sofort | Plattform-Ereignis |
| AS_QUIT | Spiel beenden / Titelbildschirm | sofort |  |

Autosaves sind häufig genug, dass ein Absturz höchstens wenige Minuten Spielzeit kostet, und selten genug, dass Flash-Speicher und Plattformrichtlinien geschont werden. Manuelles Speichern bleibt jederzeit möglich (außer im Kampf und in Zwischensequenzen) und schreibt in den gewählten Slot, nicht in eine Rotationskopie. Zwischen zwei Autosaves liegen mindestens 30 Sekunden (außer Finale, Ruhemodus, Beenden). Autosaves schreiben in die nächste Rotationskopie (1 → 2 → 3 → 1); die neueste gültige Kopie wird geladen.

### 4.3 Eiserner Wärter

Der Modifikator Eiserner Wärter (K03) sperrt erschöpfte Echos für die laufende Region und erlaubt nur einen Bindungsversuch je Echo. Damit das nicht durch Neuladen umgangen wird:

| Regel | Umsetzung |
|---|---|
| Ein Stand | Kein manuelles Speichern, keine Rotationskopien im Slot (die Plattform-Sicherung gegen Stromausfall bleibt: Temp-Datei + Umbenennen) |
| Sofortiges Speichern | Erschöpfung im Kampf, Bindungsversuch, Kampfende → Autosave sofort (ohne Mindestabstand) |
| Beenden im Kampf | Zustand vor dem Kampf + Kampf gilt als verloren (Fluchtversuch gescheitert) |
| Absturz | Letzter Autosave; ein Kampf, der beim Absturz lief, wird neu gestartet (fairer Umgang mit technischen Fehlern) |
| Cloud | Eiserner-Wärter-Slot wird nur nach Abschluss eines Kampfes hochgeladen |

### 4.4 Finale-Speicherpunkt

Vor der Finalentscheidung (K46) schreibt das Spiel einmalig den Finale-Slot. Nach dem Abspann kann man ihn laden, um die andere Entscheidung zu erleben; das Ergebnis entsteht in einem Weltstand-Slot nach Wahl. So bleibt der Nachhall des ersten Durchlaufs erhalten, und das zweite Ende ist ohne erneutes Durchspielen erreichbar.

### 4.5 Ladeablauf

```
Titel ▸ Slot wählen
 1. Plattform-Speicher lesen (asynchron), Slot + Rotationskopien auflisten
 2. ReadContainer(neueste Kopie) → bei Fehler nächste Kopie (bis 3), sonst Hinweis „Slot beschädigt“
 3. Header → Ladebildschirm-Vorschau (Region in Signaturfarbe, Chor-Klangmale)
 4. Fragmente in fester Reihenfolge anwenden:
      World.Time → World.Zones → World.Settlements → World.QuestConsequences   (Weltgerüst)
      Player.StoryFlags → Player.Quests → Player.Reputation                     (Erzählung, Data Layers)
      Chor → Sanctuary → Inventory → Equipment → Warden → Traversal              (Spielfigur und Echos)
      World.Population → World.Npcs → World.Nodes                               (lebende Welt)
      übrige Fragmente (Kodex, Breeding, Crafting, Online-, Endgame-Fragmente)
 5. Lade-Hooks: Ersatztabelle (RetiredIds), Tausch-Deltas abschließen, Koop-Protokoll anwenden
 6. World Partition streamt um `Player.Position`; Spiel startet, sobald die Zellen im Umkreis von 256 m geladen sind
```

Die Reihenfolge ist wichtig: Data-Layer-Zustände (Stille/Geheilt, Siedlungszustände) müssen vor dem Streaming feststehen, damit keine falschen Zellen geladen werden; NPC-Tagesabläufe brauchen Weltzeit und Siedlungszustände.

---

## 5. Plattformen, Cloud und Cross-Save

| Plattform | Speicher | Cloud | Besonderheiten |
|---|---|---|---|
| PS5 | Save-Data-API (Dialog-frei), Mount je Slot | PS-Plus-Cloud (automatisch/Benutzer) | Aktivitäten-Karten zeigen Region/Rang aus dem Header |
| Xbox Series X\|S | Connected Storage (Container je Slot, Blobs je Fragmentgruppe) | Automatisch (Xbox Cloud Saves) | Quick Resume: Zustand wird beim Wiederaufnehmen geprüft, Autosave beim Suspend |
| Switch 2 | Save-Data mit Journaling (Commit nach jedem Schreiben) | Nintendo-Online-Cloud | Journal-Größe 2 × Weltstand + Profil reserviert; Schreiben nicht häufiger als alle 30 s (Plattformempfehlung, deckt sich mit dem Mindestabstand) |
| PC (Steam, Epic) | Benutzerordner `Saved/SaveGames/<Konto>` | Steam Cloud / Epic Cloud | Konfliktdialog bei abweichenden Ständen |

### 5.1 Cross-Save

Spielende können mit ihrem **Aethris-Konto** (K59 §3) einen Weltstand zwischen Plattformen mitnehmen:

```
Gerät A: Menü „Cross-Save“ ▸ Slot wählen ▸ Hochladen (signiert, komprimiert, ≤ 100 KB)
Backend: speichert je Konto bis zu 3 Weltstände + Profil-Teile (Einstellungen plattformunabhängig)
Gerät B: Menü „Cross-Save“ ▸ Herunterladen ▸ Konfliktprüfung (Spielzeit, Zeitpunkt) ▸ Slot wählen
```

| Regel | Festlegung |
|---|---|
| Opt-in | Cross-Save ist freiwillig; ohne Aethris-Konto nur Plattform-Cloud |
| Konflikte | Nie automatisch überschreiben: Vergleich zeigt Spielzeit, Region, Rang, Datum beider Stände; Wahl mit Halten 3 s |
| Erfolge/Trophäen | bleiben plattformgebunden; beim Import werden erreichte Erfolge auf der neuen Plattform nachträglich freigeschaltet, wo erlaubt |
| Online-Signaturen | Echo-Signaturen (K59 §8) bleiben gültig; Tausch-Deltas müssen vor dem Hochladen abgeschlossen sein |
| Plattform-Inhalte | Keine plattformexklusiven Inhalte (DR-19), daher keine Sperren beim Wechsel |

### 5.2 Plattform-Anforderungen

Die Zertifizierungsrichtlinien der Plattformen enthalten Regeln zum Speichern; das System erfüllt sie strukturell:

| Anforderung (sinngemäß) | Umsetzung |
|---|---|
| Speichern darf das Spiel nicht blockieren und muss angezeigt werden | asynchrones Schreiben, Speicher-Symbol (§10) |
| Nicht genügend Speicher wird verständlich gemeldet | Plattform-Dialog mit Platzbedarf; Spiel läuft weiter |
| Beschädigte Daten führen nicht zum Absturz | Container-/Fragmentprüfung, Rotationskopien (§7) |
| Suspend/Resume und Benutzerwechsel werden korrekt behandelt | AS_SUSPEND, Profilwechsel lädt neu |
| Speicherdaten sind dem Benutzerkonto zugeordnet | Plattform-APIs je Konto |
| Schreibhäufigkeit auf Flash-Speicher ist begrenzt (Switch 2) | Mindestabstand 30 s, Journaling |
| Cloud-Konflikte werden dem Benutzer zur Wahl gestellt | Konfliktansicht, Halten 3 s |

### 5.3 Online und Saves

| Situation | Verhalten |
|---|---|
| Koop als Gast | Eigener Weltstand wird vor dem Beitritt gespeichert und steht still; das Gast-Protokoll (`Player.CoopLedger`) wird alle 60 s lokal gesichert und beim Heimkehren angewendet (K59 §6.4) |
| Koop als Host | Normale Autosaves der Host-Welt; Gäste schreiben nie in die Host-Welt |
| Tausch | Echo „unterwegs“ bis zur Bestätigung (`Player.TradeDeltas`); ein Neuladen eines älteren Stands erzeugt kein nutzbares Duplikat (Signatur bereits verbraucht, K60 §10) |
| Ranked/Raid | Keine Weltstand-Änderungen außer Belohnungen; Ergebnisse kommen vom Server und werden beim nächsten Autosave gesichert |
| Geister-Teams | Wöchentlicher Import in `Player.GhostTeams`, nur wenn online |

---

## 6. Versionierung und Migration

Jedes Fragment hat eine eigene Schema-Version. Jede Formatänderung erhöht sie und trägt den Commit-Marker `[SAVE-SCHEMA]` (CANON §25). Die Migration steht im Leser des Fragments als Kette:

```cpp
bool FQuestSaveProvider::ReadSaveFragment(FArchive& Ar, int32 FromVersion)
{
    FQuestSaveV2 State;
    if (FromVersion == 1)
    {
        FQuestSaveV1 Old; Ar << Old;                 // v1: Schritt als Index
        State = MigrateV1toV2(Old);                  // v2: Schritt als stabile StepId (K48)
    }
    else if (FromVersion == 2) { Ar << State; }
    else { return false; }                           // unbekannte (neuere) Version → SA-03/SA-04
    Apply(State);
    return true;
}
```

| Regel | Inhalt |
|---|---|
| MG-01 | Migrationen sind rein (keine Weltabfragen); sie bekommen nur die alten Bytes |
| MG-02 | IDs werden nie wiederverwendet (`RetiredIds.csv`, CANON §23); entfernte Arten/Items werden über eine Ersatztabelle gemappt |
| MG-03 | Jede Version bleibt lesbar, bis kein Golden Save sie mehr enthält (praktisch: für immer) |
| MG-04 | Daten-Migrationen (z. B. neue Quest-Schritte) laufen nach dem Laden über Fragment-Hooks, nicht im Container |
| MG-05 | Ein Patch darf nie eine Version schreiben, die der vorherige Patch nicht wenigstens als „unbekannt“ mitschleppen kann |

### 6.1 Versionsstand zum Launch

| Fragment | Version | Geschichte |
|---|---|---|
| `Chor` | v3 | v1 Grundform (K06) · v2 Genom (K38) · v3 Schliff-Sperren und Signatur (K18, K59) |
| `Inventory` | v2 | v1 Grundform · v2 Taschenplätze und Halteitems getrennt (K40) |
| `Player.Quests` | v2 | v1 Schrittindex · v2 stabile StepId (K48) |
| alle übrigen | v1 | Erstfassung |

Ältere Versionen tauchen nur in internen Builds auf; sie werden trotzdem im Golden-Save-Korpus gehalten, damit die Migrationsketten getestet bleiben.

### 6.2 Entfernte und umbenannte Inhalte

IDs werden nie wiederverwendet (CANON §23). Wird ein Inhalt entfernt oder zusammengelegt, trägt `Data/Meta/RetiredIds.csv` den Ersatz ein (z. B. ein entferntes Item → Rückerstattung in Sol, eine zusammengelegte Fähigkeit → Nachfolger). Der Lade-Hook des besitzenden Fragments wendet die Ersatztabelle an und schreibt einen Hinweis ins Tagebuch („Ein Gegenstand wurde durch … ersetzt“). Echos verschwinden nie: Für Arten gibt es keine Entfernung, nur Umbenennungen des Anzeigenamens.

**Beispiel aus K63:** Die Identitätsakzente ändern Basiswerte von 131 Arten. Spielstände speichern keine Basiswerte (nur Art, Anlagen, Schliff, Level), daher ist keine Migration nötig – die neuen Werte gelten beim nächsten Laden. Das ist Absicht (DD-02): Definitionen leben in Daten, Saves enthalten nur Instanzzustand.

---

## 7. Fehlertoleranz

| Fehler | Erkennung | Reaktion | Spielende sehen |
|---|---|---|---|
| Container unlesbar (Magic, Größen) | `ReadContainer` = false | nächste Rotationskopie | „Ein Spielstand war beschädigt; der vorherige Autosave wurde geladen.“ |
| Einzelnes Fragment defekt | CRC je Fragment | nur dieses Fragment auf Standard (SA-03), Rest normal | Hinweis mit betroffenem Bereich (z. B. „Kartenschleier zurückgesetzt“) |
| Fragment neuer als Build | Version > bekannt | Rohbytes behalten (SA-04), Funktion eingeschränkt | Aufforderung zum Update |
| Speicher voll | Plattform-Fehler beim Schreiben | alter Stand bleibt (atomar), Spiel läuft weiter | Hinweis mit Platzbedarf |
| Stromausfall beim Schreiben | Temp-Datei ohne Umbenennen | beim Start ignoriert | nichts |
| Echo-Instanz unplausibel (z. B. Art entfernt) | Lade-Hook | Ersatzart laut Mapping, Ursprung bleibt | Hinweis im Hain |

**Drei Beispiele aus der Praxis:**

1. *Stromausfall auf der Switch 2 während eines Autosaves nach einer Bindung.* Die Temp-Datei ist unvollständig; beim Start wird sie ignoriert. Geladen wird die letzte gültige Kopie – vor der Bindung. Weil der Kampf-Seed aus dem gespeicherten Kampfzähler stammt, verläuft derselbe Bindungsversuch gleich, wenn die Person genauso handelt; die Bindung ist also nicht „verloren“, sondern wiederholbar.
2. *Ein Bit-Fehler auf einer alten SD-Karte trifft das Fragment `Player.Map`.* Die CRC des Fragments stimmt nicht. Der Kartenschleier wird zurückgesetzt (alle Gebiete wieder „unentdeckt“), aber Resonanzsteine bleiben aktiv, weil sie zusätzlich im Fragment `Traversal`/`World.Settlements` stehen. Hinweis: „Kartenschleier zurückgesetzt.“
3. *Ein Spielstand wurde auf dem PC mit Patch 1.3 gespeichert und per Cloud auf einer Konsole mit Patch 1.2 geladen.* Das Fragment `Player.Endgame` hat Version 2 (neu in 1.3). Der Build 1.2 kennt nur v1, liest es nicht, behält aber die Rohbytes (SA-04) und schreibt sie beim nächsten Speichern zurück. Die Tiefen-Fortschritte sind auf der Konsole unsichtbar, bis sie aktualisiert ist – aber nicht verloren.

Kritische Fragmente (`Chor`, `Sanctuary`) werden zusätzlich in **jeder** Rotationskopie geprüft: Ist eines in der neuesten Kopie defekt, wird es aus der nächstälteren Kopie übernommen, statt es zurückzusetzen. Echos gehen so praktisch nie verloren.

---

## 8. Determinismus und „Save-Scumming“

AETHRIS macht Neuladen als Strategie weitgehend wirkungslos, ohne es zu verbieten:

| System | Warum Neuladen nichts ändert |
|---|---|
| Wetter | Deterministischer Fahrplan je Spieltag (CANON §61, CR-001) |
| Spawns | Seeds je Zone und Spieltag (Fork(2)) |
| Kämpfe | Kampf-Seed = Hash(Weltseed, Kampfzähler); der Zähler steht im Save |
| Zucht | Fork(3) mit Zuchtzähler |
| Loot | Fork(4) mit Kistenzähler |
| Preise | Deterministische Tagespreise (ADR-157) |
| Dissonanzen | Fork(6) je Spieltag und Ort (K62) |

Weil Kampfzähler und Zuchtzähler gespeichert werden, führt ein Neuladen vor einer Bindung zum **selben** Ergebnis, wenn die Spielenden dasselbe tun. Andere Entscheidungen (anderer Köder, anderes Siegel) führen zu anderen Ergebnissen – Können und Vorbereitung zählen, nicht Würfeln (DR-07).

---

## 9. Leistung

| Schritt | Ort | Budget (PS5 / Switch 2) |
|---|---|---|
| Fragmente serialisieren | Game Thread (Zustandskopie) | ≤ 4 ms / ≤ 6 ms |
| Container + Kompression (Oodle Kraken) | Worker-Thread | ≤ 20 ms / ≤ 40 ms |
| Plattform-Schreiben | asynchron | ≤ 250 ms (nicht blockierend) |
| Laden (Container + Fragmente) | Ladebildschirm | ≤ 300 ms / ≤ 600 ms zusätzlich zum Streaming |

Große Fragmente (Hain, Population) serialisieren nur geänderte Abschnitte neu („Dirty-Flags“ je Garten bzw. Zone) und kopieren den Rest aus dem letzten Puffer. Autosave-Auslöser im Kampf werden bis zum Kampfende verzögert.

### 9.1 Speicherbedarf je Plattform

| Posten | Größe (komprimiert, geschätzt) |
|---|---|
| Weltstand (Obergrenze) | ≈ 86 KB |
| 5 Slots (3 Welt, Eisern, Finale) + 9 Rotationskopien | ≈ 1,2 MB |
| Profil ohne Fotos | ≈ 4 KB |
| Fotoalbum (max. 500 × 200 KB) | ≤ 100 MB (separater Speicherbereich, optional in der Cloud) |
| Switch-2-Journal (2 × Weltstand + Profil) | ≈ 0,2 MB reserviert |

Der Speicherbedarf ist so klein, dass keine Plattformgrenze berührt wird; das Fotoalbum ist der einzige große Posten und wird getrennt verwaltet, damit Spielstände schnell bleiben und Cloud-Kontingente nicht unnötig füllen.

### 9.2 Datenschutz

Spielstände enthalten keine personenbezogenen Daten außer pseudonymen Konto-Hashes im Ursprung von Echos (Erstwärter) und dem Wärternamen, den die Person selbst wählt. Cross-Save-Daten im Backend werden nach 12 Monaten ohne Zugriff gelöscht und auf Anfrage sofort (Konto-Löschung, K59 §10). Fotos verlassen das Gerät nur, wenn sie geteilt oder per Cloud gesichert werden.

---

## 10. UX

| Element | Festlegung |
|---|---|
| Speicher-Symbol | Kleines Klangmal-Symbol unten rechts während des Schreibens (kein Text, kein Pop-up); Plattformvorgabe „nicht ausschalten“ wird bei manuellem Speichern eingeblendet |
| Slot-Liste | Region (Signaturfarbe, K56), Spielzeit, Wärterrang, Akkorde, Chor-Vorschau (Klangmale der 6 Echos), Datum |
| Konflikte | Vergleichsansicht mit beiden Ständen, Halten 3 s |
| Eiserner Wärter | Slot mit eigenem Symbol; „Laden“ nur des letzten Stands |
| Finale | eigener Eintrag „Vor der Entscheidung“ mit Hinweis, dass Laden eine Kopie erzeugt |

---

## 11. Tests

| Test | Inhalt | Rhythmus |
|---|---|---|
| Golden-Save-Korpus | Je Meilenstein-Build 20 Spielstände (Prolog, jede Region, Finale, Nachhall, Eisern, Koop-Gast) werden mit jedem neuen Build geladen; Vergleich der Zustands-Prüfsummen | CI, jeder Build |
| Rundreise | Speichern → Laden → Speichern ergibt identische Bytes (SA-06) | CI |
| Stromausfall | Schreibvorgang an 1.000 zufälligen Punkten abbrechen (Plattform-Debug-Werkzeuge) | wöchentlich, vor Zertifizierung |
| Korruption | Zufällige Bytes in Fragmenten kippen; erwartet: nur betroffenes Fragment zurückgesetzt | CI (Fuzzing) |
| Migration | Jeder `[SAVE-SCHEMA]`-Commit braucht einen Test von jeder alten Version | CI |
| Cross-Save | Alle Plattformpaare, Konflikte, Signaturen | je Release-Kandidat |
| Speicher voll | Plattform-Speicher künstlich füllen | vor Zertifizierung |
| Leistung | Autosave-Zeiten im Worst Case (voller Hain, Endgame) | nächtlich |

### 11.1 Golden-Save-Korpus

| Nr. | Stand | Besonderheit |
|---|---|---|
| G01 | Prolog, Minute 20 | erstes Echo, Stillezone aktiv |
| G02 | Eichenhall nach Akkord 1 | Chorgröße 3, Bodenreiten |
| G03 | Akt I, Kharsgrat zuerst | Zonenfixierung Reihenfolge A |
| G04 | Akt I, Saltrand zuerst | Zonenfixierung Reihenfolge B |
| G05 | Ende Akt I | Zucht freigeschaltet, 2 Brutnischen belegt |
| G06 | Akt II, Ael'Dorun | Wahrheitsstufen, Orden-Flags |
| G07 | Akt II, Resonanzsturm aktiv | Wetter-Override im Save |
| G08 | Akt III, Prismtiefen | volle Ausrüstung IV |
| G09 | Finale-Speicherpunkt | schreibgeschützt |
| G10 | Nachhall „Neues Lied“ | DL_Nachhall, Tiefen I–III |
| G11 | Nachhall „Sanfte Stille“ | schlafende Stimmen |
| G12 | Hain voll (600 Echos) | Größen-Grenzfall |
| G13 | Eiserner Wärter, Region gesperrt | Sperren erschöpfter Echos |
| G14 | Koop-Gast mit offenem Protokoll | Ledger-Anwendung |
| G15 | Offener Tausch (Echo unterwegs) | Delta-Abschluss beim Laden |
| G16 | Alle 6 Mythischen | Endgame-Fragmente |
| G17 | Cross-Save von PS5 | Plattformwechsel |
| G18 | Cross-Save von Switch 2 | Plattformwechsel |
| G19 | Save mit unbekanntem Fragment aus Zukunfts-Build | SA-04 |
| G20 | Save mit absichtlich defektem Fragment | SA-03 |

### 11.2 Atomares Schreiben (Pseudocode)

```
write_slot(slot, bytes):
    tmp ← slot.path + ".tmp"
    schreibe bytes nach tmp; flush; fsync (bzw. Plattform-Commit)
    prüfe: lese tmp, ReadContainer(tmp) == ok und PayloadCRC stimmt
    rotiere: slot.3 ← slot.2 ← slot.1 ← slot (Umbenennen, atomar je Schritt)
    benenne tmp → slot
    Fehler in irgendeinem Schritt → tmp löschen, alter Stand bleibt unverändert
```

---

## 12. Prüfregeln

`tools/ref/aethris_save.py validate`:

| Regel | Inhalt |
|---|---|
| SV-01 | Jedes in den Kapiteln genannte Fragment ist registriert |
| SV-02 | Owner-Modul existiert |
| SV-03 | IDs eindeutig, Version ≥ 1, Scope World/Profile |
| SV-04 | Weltstand ≤ 2,5 MB unkomprimiert, alle Slots mit Rotation ≤ 32 MB |
| SV-05 | Rundreise, Korruption je Fragment, unbekannte Fragmente |
| SV-06 | Autosave-Auslöser vollständig |

**Ergebnis:** Prüfregeln SV-01–SV-06: **0 Verstöße**. 36 Fragmente (32 Weltstand, 4 Profil), alle in den Kapiteln genannten Fragmente registriert; Weltstand ≤ 247 KB unkomprimiert, alle Slots mit Rotation ≈ 1,2 MB; Rundreise, Korruption je Fragment und unbekannte Fragmente geprüft.

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Alle Feature-Teams | Fragment im Register eintragen, `ISaveFragmentProvider` implementieren, Version bei Änderungen erhöhen (`[SAVE-SCHEMA]`) | K06 |
| Plattform | Save-APIs, Cloud, Journaling (Switch 2), Quick Resume (Xbox) | K65 |
| Online | Cross-Save-Dienst, Konfliktprüfung, Signaturen | K59 |
| QA | Testmatrix §11, Golden-Save-Korpus pflegen | K66 |
| UI | Speicher-Symbol, Slot-Liste, Konfliktansicht | K54 |
| Narrative | Text „Vor der Entscheidung“, Hinweise bei Wiederherstellung | K46 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-267 | Container v2 mit CRC32 je Fragment und Nutzlast-CRC | Defekte gezielt erkennen, Rest erhalten (SA-03) | nur Gesamt-CRC |
| ADR-268 | Zentrales Fragment-Register mit Prüfregel über alle Kapitel | Kein Fragment wird vergessen; Größenbudget prüfbar | verteilte Dokumentation |
| ADR-269 | Kritische Fragmente (Chor, Hain) werden bei Defekt aus der nächstälteren Kopie übernommen | Echos gehen praktisch nie verloren | Zurücksetzen auf Standard |
| ADR-270 | Eiserner Wärter: ein Stand, sofortiges Speichern bei Erschöpfung/Bindung, Absturz startet laufenden Kampf neu | Modus bleibt ehrlich und fair | Rotationskopien auch im Eisernen Modus |
| ADR-271 | Cross-Save opt-in über Aethris-Konto, Konflikte nie automatisch | Freiheit, kein Datenverlust | automatische Synchronisation |
| ADR-272 | Saves enthalten nur Instanzzustand, keine Definitionen | Balance-Änderungen ohne Migration (DD-02) | Basiswerte im Save |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §252 | Container v2 (Magic, Version 2, HeaderSize, Header, Verzeichnis mit CRC32 je Fragment, Nutzlast, Nutzlast-CRC; Little Endian; Oodle/Verschlüsselung außerhalb); Fragment-Register `Fragments.csv` (36 Fragmente, Owner, Scope, Version, Obergrenzen); Weltstand ≤ 250 KB unkomprimiert | LOCKED (präzisiert §32) |
| §253 | Slots: 3 Weltstände (je 3 Rotationskopien), Eiserner Wärter (ein Stand, Sofort-Speichern), Finale-Speicherpunkt (schreibgeschützt, Laden = Kopie), Profil; Autosave-Auslöser `AutosaveTriggers.csv`, Mindestabstand 30 s | LOCKED |
| §254 | Migration MG-01–MG-05 (`[SAVE-SCHEMA]`), Fehlertoleranz (Rotationskopie, Fragment-Reset, kritische Fragmente aus älterer Kopie), Plattform-Speicher und Cloud, Cross-Save opt-in (≤ 3 Weltstände, Konfliktwahl), Determinismus gegen Save-Scumming | LOCKED |
| §255 | Leistungsbudgets (Game Thread ≤ 4/6 ms, Worker ≤ 20/40 ms, Laden ≤ 300/600 ms), UX (Klangmal-Symbol, Slot-Vorschau), Testmatrix (Golden Saves, Rundreise, Stromausfall 1.000×, Korruption, Migration, Cross-Save, Speicher voll) | LOCKED |
| §10 | ADR-267 – ADR-272 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Ziele SZ-1–SZ-5, Prinzipien SA-01–SA-06 übernommen
- [x] Container v2 mit Testvektor (Python = C++)
- [x] Fragment-Register mit Größen, Eigentum, Scope
- [x] Slots, Autosave-Auslöser, Eiserner Wärter, Finale-Speicherpunkt
- [x] Plattformen, Cloud, Cross-Save
- [x] Versionierung und Migration (MG-01–MG-05), Fehlertoleranz, Determinismus
- [x] Leistung, UX, Tests
- [x] Prüfregeln SV-01–SV-06 (0 Verstöße), C++ (Container, Subsystem)
- [x] Anforderungen, ADR-267 – ADR-272, CANON §252–§255

➡️ **Nächstes Kapitel: K65 – Performance und Plattformen.**
