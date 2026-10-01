# K66 · QA und Tests

| Feld | Wert |
|---|---|
| Dokument | Kapitel 66 von 68 · Produktion I |
| Version | 1.0 |
| Owner | QA Director, Technical Director |
| Mitwirkende | QA Leads (Funktion, Online, Plattform, Lokalisierung, Barrierefreiheit), SDETs (Testautomatisierung), Build Engineer, Producer, Data Scientist, externe Partner (LQA, Kompatibilität) |
| Baut auf | K05 (CI, Coding Standards, Testnamensraum, CANON §27–§28), alle Fachkapitel mit Prüfregeln (K16–K65), K54 (Barrierefreiheit), K59 (Online-Tests), K63 (Playtests), K64 (Save-Tests), K65 (Performance-Gates) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/QA/Checks.csv` (24 Datenprüfungen), `TestSuites.csv`, `BugSeverity.csv`, `CertAreas.csv`; Runner `tools/ref/aethris_qa.py`; Automation Specs `Aethris.Unit.Core.CombatNet`, `Aethris.Unit.Save.Container`, `Aethris.Unit.PvP.Glicko2`; Exitcodes aller Prüfer vereinheitlicht |
| Neue Kanon-Einträge | CANON §260 (Teststrategie), §261 (Datenprüfungen und Automatisierung), §262 (Fehler-Workflow, Zertifizierung), §263 (Qualitätstore und Kennzahlen) |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Teststrategie](#2-teststrategie)
3. [Automatisierte Testsuiten](#3-automatisierte-testsuiten)
4. [Datenprüfungen](#4-datenprüfungen)
5. [Manuelles Testen](#5-manuelles-testen)
6. [Fehler-Workflow](#6-fehler-workflow)
7. [Zertifizierung](#7-zertifizierung)
8. [Qualitätstore je Meilenstein](#8-qualitätstore-je-meilenstein)
9. [Organisation](#9-organisation)
10. [Kennzahlen](#10-kennzahlen)
11. [Anforderungen an andere Abteilungen](#11-anforderungen-an-andere-abteilungen)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Ziele

Qualität ist in AETHRIS keine Phase am Ende, sondern eine Eigenschaft jeder Änderung. Die Spezifikation selbst ist bereits so gebaut: Jede Zahl steht in Daten, jede Regel hat einen Prüfer, und jedes Kapitel endet mit einem Prüfergebnis.

| Ziel | Bedeutung | Messbar an |
|---|---|---|
| **QZ-1 Früh finden** | Fehler werden dort gefunden, wo sie entstehen – in Daten und Code vor dem Einreichen | Anteil vor Submit gefundener Fehler ≥ 60 % |
| **QZ-2 Automatisieren, was wiederholbar ist** | Menschen testen, was Menschen besser können: Gefühl, Verständnis, Überraschung | ≥ 1.300 automatisierte Tests zum Launch |
| **QZ-3 Spielstände sind heilig** | Kein Release mit Datenverlust-Risiko | 0 offene S1 im Bereich Save |
| **QZ-4 Für alle spielbar** | Barrierefreiheit und Lokalisierung sind Testziele erster Klasse | Barrierefreiheits-Suite grün, LQA abgeschlossen |
| **QZ-5 Zertifizierung im ersten Anlauf** | Plattformrichtlinien sind von Anfang an Testfälle | Erstdurchlauf je Plattform bestanden |
| **QZ-6 Stabil im Betrieb** | Absturzfreie Sitzungen, ruhige Server | crashfreie Sitzungen ≥ 99,8 % |

---

## 2. Teststrategie

```
                       ┌────────────────────────────┐
                       │ Telemetrie & Crash-Reports │  Live (K68)
                     ┌─┴────────────────────────────┴─┐
                     │ Playtests (K63 §10)             │  Menschen, Gefühl
                   ┌─┴─────────────────────────────────┴─┐
                   │ Manuell: explorativ, LQA, A11y, Cert │  QA-Team
                 ┌─┴───────────────────────────────────────┴─┐
                 │ Plattform & Performance (Gates K65)        │  Nightly
               ┌─┴──────────────────────────────────────────────┴─┐
               │ Functional / Gauntlet (Bots, Flüge, Soak)         │  Nightly
             ┌─┴────────────────────────────────────────────────────┴─┐
             │ Unit (Automation Specs, Referenzvektoren)               │  Pre-Submit
           ┌─┴──────────────────────────────────────────────────────────┴─┐
           │ Datenprüfungen (24 Prüfer, Data Validation, Layers, Lint)     │  Pre-Submit
           └────────────────────────────────────────────────────────────────┘
```

**Grundsätze:**

| Grundsatz | Inhalt |
|---|---|
| TS-1 Referenz zuerst | Jede deterministische Formel hat ein Python-Referenzmodell; C++-Tests prüfen gegen dessen Testvektoren (Kampfbefehl, Save-Container, Glicko-2, Statusformeln) |
| TS-2 Seeds überall | Alle Bots, Benches und Simulationen laufen mit festen Seeds; ein Fehlschlag ist reproduzierbar |
| TS-3 Kein Flake | Ein instabiler Test ist ein Fehler (S3) mit Owner; Quarantäne höchstens 5 Arbeitstage, danach Reparatur oder Löschung mit Ersatz |
| TS-4 Daten sind Code | Jede CSV-Änderung durchläuft dieselben Prüfungen wie Code (Pre-Submit) |
| TS-5 Testbarkeit ist Anforderung | Neue Systeme liefern Debug-Befehle (`Cheat.`/`Debug.`-Tags, CANON §23), Seeds und Telemetrie-Ereignisse mit |

---

## 3. Automatisierte Testsuiten

| Suite | Inhalt | Tests (Launch) | Laufzeit | Stufe |
|---|---|---|---|---|
| `Aethris.Unit.Core` | Core: Zufall, Festkomma, Statusformeln, Kampfnetz | 140 | < 1 min | PreSubmit |
| `Aethris.Unit.Combat` | Zeitleiste, Schaden, Status, Kombos, Dissonanzen | 260 | < 2 min | PreSubmit |
| `Aethris.Unit.Breeding` | Genetik, Morphs, Plausibilität | 90 | < 1 min | PreSubmit |
| `Aethris.Unit.Save` | Container, Migration, Fragmente | 80 | < 1 min | PreSubmit |
| `Aethris.Unit.PvP` | Glicko-2, Normalisierung, Regelsätze | 60 | < 1 min | PreSubmit |
| `Aethris.Unit.Quests` | Bedingungen, Zustände, StepId-Migration | 150 | < 1 min | PreSubmit |
| `Aethris.Unit.World` | Zonen, Wetterfahrplan, Siedlungen | 110 | < 1 min | PreSubmit |
| `Aethris.Functional.Onboarding` | Prolog vollständig (Bot), Erstresonanz, Gleiter | 12 | 15 min | Nightly |
| `Aethris.Functional.Combat` | Kampf-Bench CB-01–CB-06, Formate, Boss-Mechaniken | 40 | 25 min | Nightly |
| `Aethris.Functional.Bond` | Bindungsszenarien K36 mit festen Seeds | 30 | 10 min | Nightly |
| `Aethris.Functional.Traversal` | Gauntlet-Flüge je Region (Gleiten, Reiten, Klettern) | 30 | 40 min | Nightly |
| `Aethris.Functional.Quests` | Hauptquest-Kette per Bot (Abkürzungsmodus), 210 Nebenquests Erreichbarkeit | 250 | 90 min | Nightly |
| `Aethris.Functional.Save` | Golden Saves G01–G20, Stromausfall-Simulation | 30 | 20 min | Nightly |
| `Aethris.Functional.Online` | Koop 2–4 Bots, Tausch, Raid, Ranked mit Netzemulation | 25 | 45 min | Nightly |
| `Aethris.Functional.Accessibility` | Optionen K54 (Stummschalt-Durchlauf, Farbenblind-Screenshots, Timing) | 35 | 30 min | Nightly |
| `Aethris.Soak` | 72-h-Dauerlauf (Welt, Koop-Host), Speicherlecks | 3 | 72 h | Wöchentlich |
| **Σ** | | **1345** | | |

Die Unit-Tests folgen der Konvention `Aethris.Unit.<Plugin>.<Thema>` (CANON §28). K66 legt die ersten drei Specs an, die direkt gegen die Referenzmodelle prüfen:

```cpp
// Source/AethrisCore/Private/Tests/CombatNetSpec.cpp (Auszug)
It("entspricht dem Referenzvektor (Fähigkeit 2 auf Gegnerplatz 9, Tick 1200)", [this]()
{
    uint8 Out[7];
    TestTrue(TEXT("packbar"), Make(1200, 0, EAethrisCombatAction::Ability, 2, 9, 0).Pack(Out));
    const uint8 Expected[7] = { 0xb0, 0x04, 0x00, 0x00, 0x80, 0x24, 0x00 };   // aethris_net.py pack_examples
    for (int32 i = 0; i < 7; ++i) { TestEqual(FString::Printf(TEXT("Byte %d"), i), Out[i], Expected[i]); }
});
```

| Spec | Prüft | Referenz |
|---|---|---|
| `Aethris.Unit.Core.CombatNet` | Packing 7 Byte, Bitprüfung, Rundreise | `aethris_net.py pack_examples` (K59) |
| `Aethris.Unit.Save.Container` | Lesen des Testvektors, byte-identisches Schreiben, Korruption nur eines Fragments | `aethris_save.py vector` (K64) |
| `Aethris.Unit.PvP.Glicko2` | Wertungsänderung auf 10⁻⁶ genau, Stufen | `aethris_pvp.glicko2_update` (K61) |

### 3.1 Funktionale Testfälle (Auswahl)

| ID | Suite | Testfall | Erwartung |
|---|---|---|---|
| FT-001 | Onboarding | Prolog vom Start bis Gleiter | Erstresonanz unscheiterbar (CANON §136), Gleiter nach ≈ 2:20 h Spielzeit-Äquivalent |
| FT-002 | Onboarding | Starter-Wahl alle drei Optionen | Nicht gewählte Starter erscheinen nach Akt I im Uralthain |
| FT-010 | Combat | Duell gleicher Arten, Seed fest | identische Zeitleiste und Ergebnis über 100 Läufe |
| FT-011 | Combat | Kombo Dampfstoß (Flut → Glut) im Fenster | Bonus und Status gemäß `Combos.csv` |
| FT-012 | Combat | Status-Anti-Lock | gleicher Status 2× → 3 Runden immun |
| FT-013 | Combat | Crescendo-Ankündigung und Entzug | Harmonie unter Schwelle → Crescendo entfällt |
| FT-014 | Combat | Boss-Phasenschwelle | Schaden an der Schwelle gekappt, Phase wechselt |
| FT-020 | Bond | Szenario „Häufiges Echo, Lieblingsfutter“ | Ergebnis „Bindung“ bei gutem Anschlag (K36) |
| FT-021 | Bond | Mythisches Bindungsfenster | öffnet bei ≤ 15 % HP, Bindung instanziert je Teilnehmer |
| FT-022 | Bond | Eiserner Wärter | nur ein Bindungsversuch, Sofort-Autosave |
| FT-030 | Traversal | Gleitroute R10 Windströme | kein sichtbares Nachladen, Streaming-Vorschub aktiv |
| FT-031 | Traversal | Kletterreiten R02 | alle Hauptpfad-Kletterstellen mit Ausrüstung der Erstbetretung erreichbar (DR-28) |
| FT-040 | Quests | Alle Hauptquests im Abkürzungsmodus | 98 Schritte abschließbar, beide Enden erreichbar |
| FT-041 | Quests | Nebenquest-Erreichbarkeit | 210 Quests startbar zur geplanten Zeit (Akt, Ruf, Bedingungen) |
| FT-042 | Quests | Flags und Epiloge | 4 Epilog-Varianten je Ende über Flag-Kombinationen |
| FT-050 | Save | Golden Saves G01–G20 laden | Zustands-Prüfsumme gleich der Referenz |
| FT-051 | Save | Stromausfall während Autosave | letzte gültige Kopie geladen, keine Datenverluste darüber hinaus |
| FT-052 | Save | Finale-Speicherpunkt | schreibgeschützt; Laden erzeugt Kopie |
| FT-060 | Online | Koop 4 Bots, Netzemulation „Schlecht“ | keine Desyncs > Ziel, Gast-Protokoll vollständig |
| FT-061 | Online | Tausch mit Verbindungsabbruch im Escrow | Rückabwicklung, kein Duplikat |
| FT-062 | Online | Ranked-Zeitlimit | Tiebreak verklungen → HP-‰ → Bank |
| FT-063 | Online | Klangbörse 3er-Ring | alle drei Bestätigungen nötig; Abbruch gibt alles zurück |
| FT-070 | Accessibility | Stummschalt-Durchlauf Prolog | alle Hinweise visuell erkennbar (UX-02) |
| FT-071 | Accessibility | Farbenblind-Modi | Typen über Form und Symbol unterscheidbar (VFX-02, K56) |
| FT-072 | Accessibility | Großzügiges Timing | Bindungsfenster und Taktproben entsprechend verlängert |
| FT-080 | Endgame | Dissonanz-Auswahl | gleiche Welt, gleicher Spieltag, gleicher Ort → gleiche Dissonanzen (auch für Koop-Gäste) |
| FT-081 | Endgame | Velnox-Pausen | Bindungsfenster nur durch drei gehaltene Pausen |
| FT-090 | Performance | Kampf-Bench CB-01–CB-06 | Budgets K65 |

**Bots und Gauntlet:** Die Functional-Suiten nutzen Gauntlet (Unreal) mit Bots, die über dieselben Eingabeaktionen (`Data/UI/InputActions.csv`) spielen wie Menschen. Der Onboarding-Bot spielt den Prolog vollständig; der Quest-Bot nutzt einen Abkürzungsmodus (Teleport zu Zielen, Kämpfe mit der Kampf-KI) und prüft, dass alle 32 Hauptquests und 210 Nebenquests erreichbar und abschließbar sind.

---

## 4. Datenprüfungen

Alle Prüfer der Fachkapitel sind in `Data/QA/Checks.csv` registriert und laufen über einen gemeinsamen Runner (`aethris_qa.py`). Erfolg heißt: Exitcode 0 **und** „0 Verstöße/Fehler“ in der letzten Zeile. K66 hat dafür die Exitcodes aller Prüfer vereinheitlicht (Palette, Ökologie, Nebenquests, NPC-Register).

| Prüfung | Kapitel | Stufe | Befehl | Ergebnis | Laufzeit |
|---|---|---|---|---|---|
| Data-Lint (Spalten, IDs, Tags, Referenzen) | K06, K54 | PreSubmit | `tools/data_lint.py` | ✅ | 0,0 s |
| Modul-Schichten | K05 | PreSubmit | `tools/check_layers.py` | ✅ | 0,0 s |
| Kreaturenkatalog (256 Arten) | K16–K27 | PreSubmit | `tools/gen_catalog.py validate` | ✅ | 0,1 s |
| Wetterfahrplan-Kalibrierung (≤ 3 pp) | K14 | Nightly | `tools/sim_weather.py` | ✅ | 32,8 s |
| Kombos und Akkorde | K33 | PreSubmit | `tools/gen_combat_data.py` | ✅ | 0,0 s |
| Items (336) | K39–K42 | PreSubmit | `tools/gen_items.py` | ✅ | 0,0 s |
| Lernsets LS-01–LS-12 | K29 | PreSubmit | `tools/gen_learnsets.py validate` | ✅ | 0,1 s |
| Fähigkeiten (330, Budget, Effekte) | K28–K30 | PreSubmit | `tools/gen_abilities.py validate --final` | ✅ | 0,0 s |
| Hauptquests und Schritte | K48 | PreSubmit | `tools/gen_quests.py` | ✅ | 0,0 s |
| Nebenquests QS-01–QS-15 | K49–K51 | Nightly | `tools/authoring/sq_k51.py validate` | ✅ | 0,0 s |
| NPC-Register | K53 | PreSubmit | `tools/gen_npcs.py` | ✅ | 0,0 s |
| UI-Prüfer UI-01–UI-06 | K54 | PreSubmit | `tools/gen_ui.py` | ✅ | 0,0 s |
| Ökologie | K52 | Nightly | `tools/ref/aethris_ecology.py validate` | ✅ | 0,1 s |
| Typfarben AR-01/AR-02 | K56 | PreSubmit | `tools/ref/aethris_palette.py validate` | ✅ | 0,0 s |
| VFX-01–VFX-06 | K58 | PreSubmit | `tools/ref/aethris_vfx.py validate` | ✅ | 0,0 s |
| NET-01–NET-06 | K59 | PreSubmit | `tools/ref/aethris_net.py validate` | ✅ | 0,0 s |
| SO-01–SO-07 | K60 | Nightly | `tools/ref/aethris_social.py validate` | ✅ | 0,0 s |
| PV-01–PV-06 | K61 | Nightly | `tools/ref/aethris_pvp.py validate` | ✅ | 1,7 s |
| EG-01–EG-06 | K62 | PreSubmit | `tools/ref/aethris_endgame.py validate` | ✅ | 0,0 s |
| BL-01–BL-07 | K63 | Nightly | `tools/ref/aethris_balance.py validate` | ✅ | 0,1 s |
| SV-01–SV-06 | K64 | PreSubmit | `tools/ref/aethris_save.py validate` | ✅ | 0,0 s |
| PF-01–PF-06 | K65 | PreSubmit | `tools/ref/aethris_perf.py validate` | ✅ | 0,0 s |
| Produktionsplan RM-01–RM-07 | K67 | PreSubmit | `tools/ref/aethris_roadmap.py validate` | ✅ | 0,0 s |
| LiveOps LO-01–LO-07 | K68 | PreSubmit | `tools/ref/aethris_liveops.py validate` | ✅ | 0,0 s |

**Ergebnis beim Abschluss dieses Kapitels:** **24 von 24 Prüfungen grün**; Laufzeit gesamt 35 s (davon PreSubmit 1 s).

### 4.1 Katalog aller Prüfregeln

Die Prüfer tragen benannte Regeln (z. B. `VFX-04`, `SV-05`), damit Fehlermeldungen, Tickets und Kapitel dieselbe Sprache sprechen. Der Katalog wird aus den Werkzeugen erzeugt (Docstrings bzw. Meldungstexte):

| Regel | Inhalt | Werkzeug |
|---|---|---|
| AB-14 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_abilities.py` |
| AR-01 | /… ΔE2000 … < | `tools/ref/aethris_palette.py` |
| AR-02 | Kontrast zum UI-Grund … < 1,6 (Symbol braucht Kontur) | `tools/ref/aethris_palette.py` |
| BL-01 | keine zwei Arten mit identischen 8 Basiswerten | `tools/ref/aethris_balance.py` |
| BL-02 | Identitätsakzente ändern Kernsumme und PRÄ+AUS nicht; Δ ≤ 8 je Wert | `tools/ref/aethris_balance.py` |
| BL-03 | Arena-Stärkeverhältnis (Arena/Spieler) je Stufe 1,00–1,12 | `tools/ref/aethris_balance.py` |
| BL-04 | jeder Typ: ≥ 2 Stärken, ≥ 2 Schwächen, Offensiv- und Defensivbilanz je |Σ| ≤ 3 | `tools/ref/aethris_balance.py` |
| BL-05 | aktive Schadensfähigkeiten: Stärke je 100 Zeitkosten innerhalb Median ± 40 % (außer markierten Sonderfällen) | `tools/ref/aethris_balance.py` |
| BL-06 | Arena-Format je Stufe ist zum erwarteten Wärterrang freigeschaltet oder per Leihbegleitung möglich | `tools/ref/aethris_balance.py` |
| BL-07 | Tuning-Knöpfe: jeder Knopf hat Quelle, Standard und sicheren Bereich; Standard liegt im Bereich | `tools/ref/aethris_balance.py` |
| EC-01 | Ökologie-Fragment unvollständig | `tools/ref/aethris_ecology.py` |
| EC-02 | Räuber ohne Beute | `tools/ref/aethris_ecology.py` |
| EC-03 | keine Basisverbraucher (auch nicht in Nachbarzonen) | `tools/ref/aethris_ecology.py` |
| EC-04 | weder Räuber noch Klangsammler | `tools/ref/aethris_ecology.py` |
| EC-05 | Tagesphase … ohne aktive Art | `tools/ref/aethris_ecology.py` |
| EG-01 | Tiefenresonanzen: Boss existiert in Bosses.csv mit gleichem Level; Level steigt mit der Nummer; Ort je Region höchstens 1× | `tools/ref/aethris_endgame.py` |
| EG-02 | jedes Mythische hat einen Solo-Weg (DR-19, CANON §8.5) | `tools/ref/aethris_endgame.py` |
| EG-03 | Dissonanzen: Faktor 500–1150 ‰, Gegenspiel angegeben, Bonus ≥ 100 ‰; kein Zufallseffekt (DR-07) | `tools/ref/aethris_endgame.py` |
| EG-04 | alle Meisterschaften, die für 100 % zählen, sind offline erreichbar (DR-19) | `tools/ref/aethris_endgame.py` |
| EG-05 | ein Echo vollständig stimmen (Anlagen → 15) kostet auf Tiefe III ≤ 6 h | `tools/ref/aethris_endgame.py` |
| EG-06 | Tiefen-Stufen: Level ≤ 100, HP-Faktor und Material steigen monoton | `tools/ref/aethris_endgame.py` |
| LO-01 | höchstens 3 zeitlich begrenzte Events gleichzeitig (Zirkel-Chronik ausgenommen) | `tools/ref/aethris_liveops.py` |
| LO-02 | jedes Event mit spielerischem Inhalt hat einen Offline-Weg zum gleichen Inhalt (DR-19) | `tools/ref/aethris_liveops.py` |
| LO-03 | Event-Belohnungen nur kosmetisch/Kodex (keine Echos, Siegel, Sol, Werte, Morphs) | `tools/ref/aethris_liveops.py` |
| LO-04 | Shop: nur erlaubte Kategorien (K01 §14), keine verbotenen Inhalte, feste Preise, auch erspielbar | `tools/ref/aethris_liveops.py` |
| LO-05 | Erweiterungen: je 30–40 Echos, Kodex-Nummern lückenlos ab #257 | `tools/ref/aethris_liveops.py` |
| LO-06 | Jahr 1: kostenloses Update oder Saison mindestens alle 3 Monate | `tools/ref/aethris_liveops.py` |
| LO-07 | Live-Kennzahlen: jede mit Alarm/Handlung; keine Handlung führt Druckmechaniken ein (DR-23) | `tools/ref/aethris_liveops.py` |
| LS-01 | Fähigkeit … unbekannt | `tools/gen_learnsets.py` |
| LS-02 | Level-Einträge (8–14) | `tools/gen_learnsets.py` |
| LS-03 | nur …/… eigene Typen (≥ 60 %) | `tools/gen_learnsets.py` |
| LS-04 | keine Status-Fähigkeit bis Lv. 20 | `tools/gen_learnsets.py` |
| LS-05 | < 2 Fähigkeiten auf Lv. 1 | `tools/gen_learnsets.py` |
| LS-06 | Schwer-Fähigkeit … vor Lv. 36 | `tools/gen_learnsets.py` |
| LS-07 | keine Evolutionsfähigkeit | `tools/gen_learnsets.py` |
| LS-08 | Legendäre brauchen genau ihren Feldklang | `tools/gen_learnsets.py` |
| LS-09 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_learnsets.py` |
| LS-10 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_learnsets.py` |
| LS-11 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_learnsets.py` |
| LS-12 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_learnsets.py` |
| LS-13 | < 2 Crescendo-Optionen | `tools/gen_learnsets.py` |
| LS-14 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_learnsets.py` |
| NET-01 | jeder Command (Client → Server) hat eine Serverprüfung | `tools/ref/aethris_net.py` |
| NET-02 | State-Nachrichten laufen nur über zuverlässige Kanäle | `tools/ref/aethris_net.py` |
| NET-03 | Koop mit 4 Spielern: Gast-Download ≤ 256 kbit/s, Host-Upload ≤ 1.024 kbit/s | `tools/ref/aethris_net.py` |
| NET-04 | Regionsanteile = 1.000 ‰, Ziel-RTT ≤ 60 ms je Region | `tools/ref/aethris_net.py` |
| NET-05 | in Kampf-/Raid-/Ranked-Modi sendet der Client keine State-Nachrichten (DR-21) | `tools/ref/aethris_net.py` |
| NET-06 | Kampfbefehl passt in die angegebene Nutzlast (Bit-Layout) | `tools/ref/aethris_net.py` |
| NP-01 | referenziert, aber nicht im Register | `tools/gen_npcs.py` |
| NP-02 | Heimatort … unbekannt | `tools/gen_npcs.py` |
| NP-03 | Muster … unbekannt | `tools/gen_npcs.py` |
| NP-04 | Nachtladen, aber Muster | `tools/gen_npcs.py` |
| NP-05 | benannte NPCs > Budget | `tools/gen_npcs.py` |
| PF-01 | Summe je Thread und Szenario ≤ 85 % der Bildzeit (Zielbildrate je Plattform) | `tools/ref/aethris_perf.py` |
| PF-02 | Speicher ≤ 90 % des verfügbaren Spielspeichers | `tools/ref/aethris_perf.py` |
| PF-03 | Budgets stimmen mit den Kanon-Werten der Fachkapitel überein | `tools/ref/aethris_perf.py` |
| PF-04 | Split-Screen-Entscheidung (Profil) = Ergebnis der Machbarkeitsrechnung | `tools/ref/aethris_perf.py` |
| PF-05 | Koop-Host-Grenze (Profil) = Ergebnis der Rechnung (Speicher, Game Thread) | `tools/ref/aethris_perf.py` |
| PF-06 | jedes Profil hat Zielbildrate, Auflösung, Upscaler | `tools/ref/aethris_perf.py` |
| PV-01 | Ranked-Zulässigkeit: Ursprungsstimmen und Mythische ausgeschlossen, alle anderen 240 Arten zulässig | `tools/ref/aethris_pvp.py` |
| PV-02 | Normalisierung: Werte auf NormLevel = Formel K18 (CANON §79) mit echten Anlagen/Schliff | `tools/ref/aethris_pvp.py` |
| PV-03 | Stufen-Grenzen steigend; höchste Stufe ≤ 2 % der simulierten Spielenden | `tools/ref/aethris_pvp.py` |
| PV-04 | Wertung konvergiert: Spearman(echte Stärke, Wertung) ≥ 0,90 nach 40 Kämpfen je Person | `tools/ref/aethris_pvp.py` |
| PV-05 | Regelsätze: Ranked hat NormLevel, Zeitlimit ≤ 20 min (DR-11), Klar-Wetter, keine Verbrauchsgüter | `tools/ref/aethris_pvp.py` |
| PV-06 | Belohnungen nur kosmetisch (DR-20) | `tools/ref/aethris_pvp.py` |
| QS-01 | Detailprüfung (Meldungstext im Werkzeug) | `tools/authoring/sq_common.py` |
| QS-02 | Schritte (3–6) | `tools/authoring/sq_common.py` |
| QS-03 | kein Verstehen-Schritt (QR-02) | `tools/authoring/sq_common.py` |
| QS-04 | endet mit OBJ_COLLECT (QR-03) | `tools/authoring/sq_common.py` |
| QS-05 | Detailprüfung (Meldungstext im Werkzeug) | `tools/authoring/sq_common.py` |
| QS-06 | Detailprüfung (Meldungstext im Werkzeug) | `tools/authoring/sq_common.py` |
| QS-07 | Detailprüfung (Meldungstext im Werkzeug) | `tools/authoring/sq_common.py` |
| QS-08 | Intensität … (≤ …) | `tools/authoring/sq_common.py` |
| QS-09 | Dauer … (15–…) | `tools/authoring/sq_common.py` |
| QS-10 | keine nicht-monetäre Belohnung (QR-10) | `tools/authoring/sq_common.py` |
| QS-11 | TruthLevel … > … (L-01) | `tools/authoring/sq_common.py` |
| QS-12 | Wärterprüfung ohne OBJ_BATTLE | `tools/authoring/sq_common.py` |
| QS-13 | unbekannt | `tools/authoring/sq_common.py` |
| QS-14 | Quests (≤ 3) | `tools/authoring/sq_common.py` |
| QS-15 | nur …/… Quests mit Tageszeit/Wetter/Mond (QR-09) | `tools/authoring/sq_common.py` |
| QV-01 | Quest … unbekannt | `tools/gen_quests.py` |
| QV-02 | Zieltyp … unbekannt | `tools/gen_quests.py` |
| QV-03 | Boss … ohne OBJ_BOSS-Schritt | `tools/gen_quests.py` |
| QV-04 | Akkord … ohne OBJ_ARENA-Schritt | `tools/gen_quests.py` |
| QV-05 | Ort … unbekannt | `tools/gen_quests.py` |
| QV-06 | Vorbedingung … unbekannt | `tools/gen_quests.py` |
| QV-07 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_quests.py` |
| QV-08 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_quests.py` |
| QV-09 | trifft keine Quest | `tools/gen_quests.py` |
| QV-10 | Hauptquest-EP … = … (Ziel 25 % ± 5) | `tools/gen_quests.py` |
| RM-01 | Arbeitspakete liegen im Projektzeitraum (M0–M49), Ende ≥ Start | `tools/ref/aethris_roadmap.py` |
| RM-02 | Abhängigkeiten beginnen vorher | `tools/ref/aethris_roadmap.py` |
| RM-03 | Spitze ≤ 210 FTE, Durchschnitt 130–150 FTE (K01 §15/§16) | `tools/ref/aethris_roadmap.py` |
| RM-04 | Personalkosten ±5 % um 118 Mio. € (16,8 T€ je FTE-Monat, K01 §16.3) | `tools/ref/aethris_roadmap.py` |
| RM-05 | Meilensteine = Kanon-Daten (Greenlight 06/27, P2 07/27, VS 03/28, Alpha/Engine-Lock 02/30, Gold 09/30, Launch 11/30) | `tools/ref/aethris_roadmap.py` |
| RM-06 | jedes Kapitel K01–K68 gehört zu mindestens einem Arbeitspaket | `tools/ref/aethris_roadmap.py` |
| RM-07 | Durchsatz monoton, Endwerte = Kanon-Mengen | `tools/ref/aethris_roadmap.py` |
| SO-01 | jede Art hat einen Solo-Zugang (Wildvorkommen, Evolution, Stimmsiegel-Quest, Mythos-Zugang §34) | `tools/ref/aethris_social.py` |
| SO-02 | nur Ursprungsstimmen und Mythische sind vom Tausch ausgeschlossen | `tools/ref/aethris_social.py` |
| SO-03 | Tauschliste enthält nur Ressourcen, Gerichte, Lockmittel/Futter (keine Schlüssel-/Siegel-/Ausrüstungsgegenstände) | `tools/ref/aethris_social.py` |
| SO-04 | Zirkel: Mitglieder ≤ 50 (+ Gäste), genau eine Leitung | `tools/ref/aethris_social.py` |
| SO-05 | Zirkel-Chronik-Belohnungen nur kosmetisch (keine Werte, Prozente, Echos, Sol) | `tools/ref/aethris_social.py` |
| SO-06 | Schnellchat: 24 eindeutige Sätze, ≤ 40 Zeichen (Lokalisierungsreserve +40 %) | `tools/ref/aethris_social.py` |
| SO-07 | Koop-Belohnungsarten passen zum Gast-Protokoll (K59 §6.4) | `tools/ref/aethris_social.py` |
| SV-01 | jedes in den Kapiteln genannte Fragment (`Player.*`, `World.*`, `Profile.*`) steht im Register | `tools/ref/aethris_save.py` |
| SV-02 | Owner-Modul existiert | `tools/ref/aethris_save.py` |
| SV-03 | IDs eindeutig, Version ≥ 1, Scope World|Profile | `tools/ref/aethris_save.py` |
| SV-04 | Größenbudget: Weltstand ≤ 2,5 MB unkomprimiert, alle Slots inkl. Rotation ≤ 32 MB (komprimiert geschätzt) | `tools/ref/aethris_save.py` |
| SV-05 | Rundreise, Korruptionserkennung je Fragment (SA-03), unbekannte Fragmente bleiben erhalten (SA-04) | `tools/ref/aethris_save.py` |
| SV-06 | Autosave-Auslöser vollständig beschrieben | `tools/ref/aethris_save.py` |
| UI-01 | Belegung fehlt | `tools/gen_ui.py` |
| UI-02 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_ui.py` |
| UI-03 | öffnet unbekannten Bildschirm | `tools/gen_ui.py` |
| UI-04 | Detailprüfung (Meldungstext im Werkzeug) | `tools/gen_ui.py` |
| UI-05 | unumkehrbar ohne Halten ≥ 3 s | `tools/gen_ui.py` |
| UI-06 | nicht abschaltbar | `tools/gen_ui.py` |
| VFX-01 | jede Fähigkeit (Abilities.csv) hat eine Vorlage; jedes Crescendo eine eigene Signatur | `tools/ref/aethris_vfx.py` |
| VFX-02 | jeder Typ hat Motiv und farbunabhängige Form; Formen paarweise verschieden (Typen, Status) | `tools/ref/aethris_vfx.py` |
| VFX-03 | Worst-Case-Kampfszene (Trio 3+3, Crescendo + Fähigkeit + 6 Status + Terrain + Wetter) im Budget (PS5, Switch 2) | `tools/ref/aethris_vfx.py` |
| VFX-04 | Helligkeitswechsel ≤ 3 Hz: Klangmal-Puls (BPM × 1,3 Angst) und alle Story-VFX | `tools/ref/aethris_vfx.py` |
| VFX-05 | jede Typfarbe aus TypeColors.csv vorhanden (alle Modi) | `tools/ref/aethris_vfx.py` |
| VFX-06 | jedes Terrain (Terrains.csv) und jeder Status (StatusEffects.csv) hat eine Darstellung | `tools/ref/aethris_vfx.py` |
| **Σ** | **122 Prüfregeln** | |

Die Datenprüfungen sind schnell genug für jeden Pre-Submit (Ziel < 20 min für die gesamte Stufe, CANON §27). Sie ersetzen keine Tests im Spiel, verhindern aber die häufigste Fehlerklasse großer Rollenspiele: widersprüchliche Daten (fehlende Referenzen, unerreichbare Inhalte, Werte außerhalb der Regeln).

---

## 5. Manuelles Testen

### 5.1 Testarten

| Testart | Inhalt | Rhythmus |
|---|---|---|
| Feature-Abnahme | Je Feature ein Testplan aus der Checkliste des Fachkapitels (Abschnitt „Kapitel-Checkliste“ + Prüfregeln) | bei Fertigstellung |
| Explorativ | Zeitlich begrenzte „Charters“ (90 min) mit Ziel, z. B. „Versuche, eine Bindung im Koop zu duplizieren“, „Finde unerreichbare Kletterflächen in R02“ | täglich |
| Regionsdurchlauf | Jede Region vollständig (Hauptpfad, POIs, Siedlungen, Nebenquests) | je Meilenstein |
| Story-Durchläufe | Beide Enden, alle 4 Epilog-Varianten, alle Haltungen (Flags) | Alpha, Beta, RC |
| Lokalisierung (LQA) | Alle Sprachen: Text, Länge (+40 %), Kontext, Sprachausgabe, Schriftarten (CJK) | ab Beta |
| Barrierefreiheit | Alle Optionen aus `AccessibilityOptions.csv`, Stummschalt-Durchlauf, Farbenblind-Modi, Ein-Hand-Profil | je Meilenstein |
| Kompatibilität (PC) | Hardware-Matrix (40 Konfigurationen: CPU, GPU, Treiber, Speicher), Handheld-PCs | Beta, RC |
| Online | Koop, Tausch, Raid, Ranked unter Netzemulation (K59 §12) | je Meilenstein |
| Zertifizierung | Pre-Cert-Durchlauf nach Plattformrichtlinien (§7) | Beta, RC |

### 5.2 Testmatrix nach Bereichen

| Bereich | Kapitel | Schwerpunkt | Automatisiert | Manuell |
|---|---|---|---|---|
| Kampf | K28–K35 | Zeitleiste, Schaden, Status, Kombos, Bosse | Unit + Bench | Lesbarkeit, Gefühl |
| Bindung | K36 | Resonanz, Timing, Sonderfälle | Functional (Seeds) | Haptik, Timing-Gefühl |
| Echos/Hain | K16–K19, K37 | Evolution, Bindungsstufen, Hain | Unit | Animation, Emotionen |
| Zucht | K38 | Genetik, Morphs | Unit + Simulation | Bedienung |
| Welt | K08–K15 | Streaming, Zonen, Wetter, Tageszeit | Flüge | Atmosphäre, Navigation |
| Ökologie/NPCs | K52–K53 | Populationen, Tagesabläufe | Simulation | Glaubwürdigkeit |
| Quests | K44–K51 | Erreichbarkeit, Flags, Belohnungen | Quest-Bot | Text, Logik, Spoiler |
| UI/UX | K54 | Navigation ≤ 3 Eingaben, Barrierefreiheit | Screenshot-Vergleich | Verständnis |
| Audio | K55 | Stille, Mix, Untertitel | Lautheitsmessung | Mix, Emotion |
| Online | K59–K61 | Sitzungen, Tausch, Ranked | Bots + Emulation | Soziales Verhalten |
| Endgame | K62 | Tiefen, Mythische | Seeds | Schwierigkeit |
| Save | K64 | Golden Saves, Stromausfall | Functional | Plattformdialoge |
| Performance | K65 | Budgets | Flüge, Bench | Frame-Pacing-Gefühl |

### 5.3 Kinder- und Familientests

AETHRIS richtet sich an ein breites Publikum ab etwa 7 Jahren (PEGI 7). Familien-Playtests (K63 §10) prüfen zusätzlich: Verständlichkeit der Texte für junge Lesende, Frustpunkte (Bindung, Arenen), Sicherheit der Online-Funktionen (Elternkontrollen, keine ungewollte Kommunikation) und ob Kinder den Unterschied zwischen „Echo verklungen“ und „Echo gestorben“ verstehen (Echos sterben nie, CANON §8.4).

---

## 6. Fehler-Workflow

### 6.1 Schwere

| DisplayName | Definition | Reaction | Gate |
|---|---|---|---|
| Blocker | Absturz, Datenverlust, Spielstand beschädigt, Fortschritt blockiert, Zertifizierungsverstoß, Sicherheitslücke, Kinderschutz | sofort (≤ 4 h Reaktion) | Kein Build mit offenem S1 wird freigegeben |
| Kritisch | Hauptfunktion falsch (Kampfergebnis, Bindung, Tausch), schwere Performance-Verletzung (> 120 % Budget), Barrierefreiheit verhindert Spielen | ≤ 2 Arbeitstage | Release-Kandidat: 0 offene S2 |
| Mittel | Nebenfunktion falsch, sichtbare Fehler (Clipping, Text), Balance-Ausreißer | im laufenden Meilenstein | Release: ≤ 50 offen, keine in Hauptpfad |
| Gering | Kosmetik, Wunsch, kleine Textfehler | nach Priorität | – |

### 6.2 Lebenszyklus

```
Neu ─► Triage (täglich, QA Lead + Producer + Owner-Bereich) ─► Zugewiesen ─► In Arbeit ─► Behoben (Build-Nr.)
      │                                                                                     │
      └─► Duplikat / Kein Fehler / Design (mit Begründung)                                  ▼
                                                                   Verifiziert (QA im genannten Build) ─► Geschlossen
                                                                                     │
                                                                                     └─► Wieder offen (Regression → Schwere +1)
```

| Pflichtfeld | Inhalt |
|---|---|
| Build, Plattform, Modus | z. B. 0.42.1813, PS5, Koop-Gast |
| Reproduktion | Schritte, Häufigkeit (x/10), **Seed/Save** (Golden Save oder angehängter Spielstand) |
| Erwartet / Tatsächlich | mit Bezug auf Kapitel und Regel (z. B. „K36 §5: Fenster 160–400 ms“) |
| Anhänge | Video, Screenshot, Log (`LogAethris*`), Insights-Trace bei Performance |
| Bereich, Owner | aus dem Modul (CANON §26) |

**Absturzberichte** werden automatisch mit Callstack, Build, Plattform, Region, Spielmodus und den letzten 200 Log-Zeilen gesammelt und nach Signatur gruppiert; neue Signaturen mit mehr als 10 Vorkommen je Tag werden automatisch als S1-Kandidat zur Triage vorgelegt.

---

## 7. Zertifizierung

Jede Plattform verlangt vor der Veröffentlichung eine Prüfung nach ihren Richtlinien (Sony, Microsoft, Nintendo; für PC die Anforderungen der Stores). Die Richtlinien sind vertraulich; K66 gruppiert sie in Bereiche, denen jeweils Testfälle und ein verantwortliches Kapitel zugeordnet sind:

| Area | Platforms | Chapter |
|---|---|---|
| Speichern/Laden, voller Speicher, beschädigte Daten | alle | K64 |
| Ruhemodus, Fortsetzen, Quick Resume, Benutzerwechsel | Konsolen | K64, K65 |
| Netzwerkverlust, Plattformdienste nicht erreichbar, Fehlermeldungen | alle | K59 |
| Elternkontrollen, Kommunikationsbeschränkungen, Altersfreigabe | alle | K59, K60 |
| Konten, Profilwechsel, Gast-Konten (Split-Screen) | Konsolen | K65 |
| Erfolge/Trophäen (Anzahl, Bilder, Freischaltung offline) | alle | K62 |
| Lokalisierung, Systemsprache, Pflichttexte, Schriftgrößen | alle | K54 |
| Controller trennen/verbinden, Belegung, Symbole je Plattform | alle | K54 |
| Keine Hänger > Plattformgrenze beim Start/Laden, Speicherverbrauch | alle | K65 |
| Shop-Integration (falls Erweiterungen), Rechte, Preise | alle | K68 |
| Datenschutzhinweise, Telemetrie-Einwilligung | alle | K59 |
| TV/Handheld-Wechsel, Akku, Bildschirmgröße | Switch 2 | K65 |

| Phase | Inhalt |
|---|---|
| ab Alpha | Zertifizierungs-Testfälle laufen in jeder Regression mit (automatisierbare Teile: Suspend/Resume, Speicher voll, Netzverlust, Controller trennen) |
| Beta | Vollständiger Pre-Cert-Durchlauf je Plattform durch internes Team; Abweichungsliste an Plattform-Ansprechpersonen |
| RC | Einreichung; Puffer 3 Wochen je Plattform für eine zweite Einreichung |
| Patches | Jeder Patch mit verkürztem Pre-Cert (betroffene Bereiche) |

---

## 8. Qualitätstore je Meilenstein

| Meilenstein (K67) | Tor |
|---|---|
| Vertical Slice | Datenprüfungen grün; Prolog + R01 ohne S1/S2; Performance R01 PS5 im Budget; Onboarding-Bot grün; 30 externe Playtests |
| Alpha | Alle Inhalte spielbar (Platzhalter erlaubt); Quest-Bot erreicht alle Quests; Golden Saves G01–G12; S1 = 0; Performance-Gate Alpha |
| Beta | Inhalte final (Platzhalter = 0, K57); Lokalisierung vollständig; Barrierefreiheits-Suite grün; Pre-Cert bestanden; Online-Beta mit ~5.000 |
| Release-Kandidat | S1 = 0, S2 = 0, S3 ≤ 50 (nicht im Hauptpfad); crashfreie Sitzungen ≥ 99,8 % in 2 Wochen Soak; Performance-Gate RC; alle Golden Saves |
| Day-One/Patches | Regression der betroffenen Bereiche; Golden Saves; Pre-Cert verkürzt |

---

## 9. Organisation

| Gruppe | Größe (Spitze, Beta) | Aufgabe |
|---|---|---|
| Embedded QA | 1 je Feature-Team (≈ 10) | Abnahmen, Charters, Testpläne im Team |
| Zentrale QA | 25 | Regression, Regionsdurchläufe, Story, Online |
| SDETs (Automatisierung) | 6 | Bots, Gauntlet, Benches, Runner, Specs |
| Plattform-QA | 5 | Zertifizierung, Hardware-Matrix |
| Barrierefreiheit | 2 + externe Fachpersonen | Optionen, Playtests mit Betroffenen |
| LQA (extern) | 2–3 je Sprache | Sprache, Kultur, Sprachausgabe |
| Kompatibilität (extern) | Labor | PC-Hardware-Matrix |

Werkzeuge: Fehlerdatenbank mit Pflichtfeldern und Signatur-Gruppierung, Testfallverwaltung verknüpft mit Kapiteln und Prüfregeln, Video-Aufnahme in QA-Builds (letzte 60 s per Tastendruck), Debug-Menü mit Seeds, Teleport, Zeit/Wetter-Steuerung, Spielstand-Import.

---

## 10. Kennzahlen

| Kennzahl | Ziel | Zweck |
|---|---|---|
| Vor Submit gefundene Fehler (Daten/Unit) | ≥ 60 % aller Fehler | QZ-1 |
| Automatisierte Tests | ≥ 1.300 zum Launch | QZ-2 |
| Flake-Rate | ≤ 1 % der Läufe | TS-3 |
| Mittlere Zeit bis Triage | ≤ 1 Arbeitstag | Fluss |
| Regressionsquote | ≤ 8 % wieder geöffneter Fehler | Qualität der Fixes |
| Escape-Rate | ≤ 5 % der Fehler erst nach Release gefunden | Wirksamkeit |
| Crashfreie Sitzungen | ≥ 99,8 % | QZ-6 |
| Zertifizierung | Erstdurchlauf je Plattform | QZ-5 |

---

## 11. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Alle Fachteams | Prüfer mit Exitcode und „0 Verstöße“-Zeile; Eintrag in `Checks.csv`; Debug-Befehle und Seeds | alle |
| Programmierung | Automation Specs je Modul, Coverage Domain 80 % / Feature 60 % (CANON §28) | K05 |
| Build | Runner im Pre-Submit und Nightly, Ergebnisse im Dashboard | K05 |
| Produktion | Qualitätstore in den Meilenstein-Plan (K67), Zertifizierungspuffer | K67 |
| LiveOps | Crash- und Telemetrie-Dashboards, Hotfix-Prozess | K68 |
| Design | Testbare Akzeptanzkriterien in jedem neuen Kapitel/Feature | alle |

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-279 | Ein Register und ein Runner für alle Datenprüfungen, einheitliche Exitcodes | Eine Wahrheit über den Datenzustand, CI-fähig | verstreute Skripte |
| ADR-280 | C++-Tests gegen Python-Referenzvektoren | Formeln einmal spezifiziert, zweifach implementiert, automatisch verglichen | handgeschriebene Erwartungswerte |
| ADR-281 | Quest-Bot mit Abkürzungsmodus prüft Erreichbarkeit aller Quests nächtlich | 242 Quests sind manuell nicht nächtlich prüfbar | nur manuelle Durchläufe |
| ADR-282 | Flake-Regel: Quarantäne ≤ 5 Tage, dann Reparatur oder Ersatz | Vertrauen in die Pipeline | dauerhafte Quarantäne |
| ADR-283 | Zertifizierungs-Testfälle ab Alpha in jeder Regression | Erstdurchlauf-Ziel | Pre-Cert erst kurz vor Einreichung |
| ADR-284 | Qualitätstore je Meilenstein mit harten S1/S2-Grenzen | klare Freigabeentscheidungen | Freigabe nach Gefühl |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §260 | Teststrategie (Datenprüfungen → Unit → Functional → Plattform/Performance → Manuell → Playtests → Telemetrie), Grundsätze TS-1–TS-5, Ziele QZ-1–QZ-6 | LOCKED |
| §261 | `Checks.csv` (24 Prüfer, Runner `aethris_qa.py`, Erfolg = Exitcode 0 + „0 Verstöße“), `TestSuites.csv` (≥ 1.300 Tests), erste Specs (CombatNet, Save.Container, PvP.Glicko2), Bots/Gauntlet | LOCKED |
| §262 | Fehlerschwere S1–S4 (`BugSeverity.csv`), Lebenszyklus, Pflichtfelder, Absturz-Signaturen; Zertifizierungsbereiche (`CertAreas.csv`) und Phasen | LOCKED |
| §263 | Qualitätstore VS/Alpha/Beta/RC/Patches, Organisation, Kennzahlen (crashfrei ≥ 99,8 %, Escape ≤ 5 %, Flake ≤ 1 %) | LOCKED |
| §10 | ADR-279 – ADR-284 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Ziele QZ-1–QZ-6, Teststrategie und Grundsätze
- [x] Automatisierte Suiten, drei Specs gegen Referenzvektoren
- [x] Register aller Datenprüfungen, Runner, Ergebnis (alle grün)
- [x] Manuelle Testarten, Testmatrix, Familientests
- [x] Fehler-Workflow (Schwere, Lebenszyklus, Pflichtfelder, Absturzberichte)
- [x] Zertifizierung, Qualitätstore, Organisation, Kennzahlen
- [x] Anforderungen, ADR-279 – ADR-284, CANON §260–§263

➡️ **Nächstes Kapitel: K67 – Produktions-Roadmap.**
