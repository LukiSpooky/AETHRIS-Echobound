# K47 · Fraktionen und Rufsystem

| Feld | Wert |
|---|---|
| Dokument | Kapitel 47 von 68 |
| Version | 1.0 |
| Owner | Narrative Writer (Fraktionen), Quest Designer (Ruf) |
| Mitwirkende | Systems Designer (Ökonomie), Gameplay Programmer (GF_Quests), UI Designer, Lead Writer |
| Baut auf | K03 P9 (5 Fraktionen × 6 Ränge), K07 §9.2 (Sitze, Oberhäupter, Credos), K11–K13 (Städte, Händler, Aufträge), K29 (Tutoren), K40 (Blaupausen „Fraktion Ruf N“), K42 §9 (Rabatte), K44–K46 (Story, Flags) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Factions/Factions.csv`, `ReputationRanks.csv`, `ReputationSources.csv` (15 Quellen), `ReputationRewards.csv` (26 Belohnungen), `tools/ref/aethris_reputation.py`, `Source/AethrisCore/Public/Services/ReputationService.h`, Tags `Faction.*`, `Event.Reputation.*` |
| Neue Kanon-Einträge | CANON §181 (Fraktionsprofile), §182 (Rufränge und Quellen), §183 (Belohnungen), §184 (Fraktionen über die Story) |

---

## Inhalt

1. [Rolle der Fraktionen](#1-rolle-der-fraktionen)
2. [Die fünf Fraktionen](#2-die-fünf-fraktionen)
3. [Rufränge](#3-rufränge)
4. [Rufquellen](#4-rufquellen)
5. [Belohnungen](#5-belohnungen)
6. [Beziehungen zwischen den Fraktionen](#6-beziehungen-zwischen-den-fraktionen)
7. [Entscheidungen ohne Ausschluss](#7-entscheidungen-ohne-ausschluss)
8. [Ruf-Verlauf über die Spielzeit](#8-ruf-verlauf-über-die-spielzeit)
9. [Fraktionen über die Story](#9-fraktionen-über-die-story)
10. [Technik](#10-technik)
11. [UI](#11-ui)
12. [Anti-Exploit und Koop](#12-anti-exploit-und-koop)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Rolle der Fraktionen

Fraktionen sind in AETHRIS **Weltanschauungen mit Adresse**. Jede beantwortet die Frage des Spiels – *Wie leben Menschen und Echos zusammen?* – auf ihre Weise, und jede hat recht und unrecht zugleich (K07 §10: „keiner wird als falsch bloßgestellt“). Spielerisch erfüllen sie drei Aufgaben:

| Aufgabe | Umsetzung | Säule (K02) |
|---|---|---|
| **Fortschritt** | Ruf schaltet Blaupausen, Tutoren, Rabatte, Dienste und Questketten frei | S4 Wärter-Fortschritt |
| **Welt** | Fraktionen besetzen Orte (Sitze, Außenposten, Zellen), Händler, Aufträge, Barks | S3 Lebendige Welt |
| **Erzählung** | Story-Haltungen (Flags, K44–K46) färben Szenen, Unterschlupf und Epilog | S5 Erzählung |

**Grundregel (ADR-178):** **Ruf ist Fortschritt, keine Gesinnung.** Wie der Spieler zu Tavesh oder Sereth *steht*, speichern die Story-Flags (`FLAG_FS_STANCE`, `FLAG_SERETH_RESPECT`, …). Wie viel er für eine Fraktion *getan* hat, speichert der Ruf. Ein Spieler kann Tavesh misstrauen und trotzdem Rang 6 bei den Freien Stimmen erreichen – weil er hunderte Echos befreit hat. Beide Werte werden in Dialogen gemeinsam ausgewertet (§9.3).

---

## 2. Die fünf Fraktionen

| Name | DisplayName | Archetype | Seat | Leader | Credo | Quartermaster | GearSlots | RepStart |
|---|---|---|---|---|---|---|---|---|
| F01 | Akademie der Resonanz | Forscher | SET_C_DORUNSRUH | Aldric Venn (ab Nachhall kommissarisch Aevrin Thal) | Verstehen heißt ordnen. | Archivarin Pell | RESONATOR|LENS | MQ_A1_07 |
| F02 | Goldklang-Kontor | Händler | SET_C_SALTRANDHAFEN | Marieke Holm | Ein guter Handel klingt für beide richtig. | Kontorschreiber Ossian | BAG|TOOL | MQ_A1_05 |
| F03 | Wildwacht | Ranger | SET_C_EICHENHALL | Hralda Brakk | Wir schützen das Wilde, nicht vor dem Wilden. | Zeugmeisterin Fenja | GLIDER|BOOTS|CLOAK | MQ_P03 |
| F04 | Freie Stimmen | Rebellen | SET_C_MORVENFURT (Unterstadt) | Tavesh Amaru | Kein Echo gehört jemandem. | Der Schatten | LANTERN|MASK | MQ_A1_04 |
| F05 | Orden der Stille | Antagonisten → Verbündete auf Zeit | Kloster Schweigfels | Sereth Vaun (Hohe Schweigerin) | Ohne Lied kein Leid. | Schwester Ivra | – | MQ_A2_07 |

### 2.1 F01 · Akademie der Resonanz

**Selbstbild:** Wissen ist die einzige Kraft, die Leid dauerhaft verringert. Wer das Lied versteht, kann es schützen.
**Fremdbild:** Arrogant, bürokratisch, „sie messen Echos, bis sie still sind“ (Freie Stimmen).
**Haltung zu Echos:** Forschungspartner und Studienobjekte zugleich; strenge Ethikregeln seit 812 (Vaels Taxonomie), die unter Venn stillschweigend gelockert wurden.

| Aspekt | Inhalt |
|---|---|
| Orte | Dorunsruh (Sitz, ~1.400 Angehörige), Außenstelle Eichenhall (ab MQ_A1_07), Labore in Prismara, 8 Akademie-Außenposten (K13) |
| Aufträge | CT_OBSERVE, CT_PHOTO, CT_SURVEY (Forschung, Kartografie) |
| Innere Spannung | Gelehrte, die Venns Ordnung teilen, gegen Gelehrte wie Aevrin Thal, die Wissen frei halten wollen |
| Nach W6 | Die Akademie zerfällt nicht. Aevrin öffnet Venns Aufzeichnungen (CANON §54); Ruf-Fortschritt läuft weiter, Händler bleiben offen, Barks werden vorsichtiger |
| Nachhall | Kommissarische Leitung Aevrin Thal; Akademie stellt sich dem Bundesrat; Questreihe Mirrowisp über die Spiegellinse (K39) |
| Rangtitel | Gasthörer · Hörer · Assistent · Stipendiat · Fellow · Ehrendoktor |

### 2.2 F02 · Goldklang-Kontor

**Selbstbild:** Handel hält die Welt zusammen; wo gehandelt wird, wird nicht gekämpft (Siegelkriege endeten mit einem Handelsvertrag).
**Fremdbild:** „Ein Kontor verkauft dir das Seil, an dem es dich aufhängt“ (Ordensspruch); verantwortlich für die Echo-Arbeitslager von 967.
**Haltung zu Echos:** Partner der Arbeit, angemessen bezahlt – so die Satzung. Die Wirklichkeit hängt vom Konsortium ab.

| Aspekt | Inhalt |
|---|---|
| Orte | Saltrand-Hafen (Sitz), Kontore in allen zehn Städten, 4 Kontor-Außenposten |
| Aufträge | CT_GATHER, CT_DELIVER |
| Innere Spannung | Marieke Holms Pragmatismus gegen Konsortien, die mit verstummten Echos Geld verdienen (Ignareth, MQ_A2_03) |
| Story | Kontor-Kredit (Akt I) → Kisten-Gefallen (Akt II) → Fracht nach Nimbara (Akt III); `FLAG_KONTOR_DEBT`, `FLAG_KONTOR_CRATES` |
| Nachhall | Marieke führt eine „Klangtreue“-Satzung ein (bei `KONTOR_CRATES` = 2 aus Überzeugung, sonst aus Kalkül – Barks unterscheiden sich) |
| Rangtitel | Kunde · Stammkunde · Geschäftsfreund · Teilhaber · Prokurist · Goldene Stimme |

### 2.3 F03 · Wildwacht

**Selbstbild:** Wir schützen das Wilde, nicht vor dem Wilden. Bundesbehörde seit 710 n.St., Wärterlizenz.
**Fremdbild:** „Gute Leute mit zu wenig Geld und zu vielen Regeln“ (Kontor); „Wärter des Käfigs, nur mit offener Tür“ (Freie Stimmen).
**Haltung zu Echos:** Freiheit zuerst; Bindung ist ein Versprechen, kein Besitz. Freilassen wird geehrt.

| Aspekt | Inhalt |
|---|---|
| Orte | Eichenhall (Sitz), 9 Wildwacht-Außenposten, Präsenz an fast allen Wegen |
| Aufträge | CT_BOND, CT_ESCORT, CT_CALM, CT_RESCUE, CT_SILENCE |
| Innere Spannung | Gesetzestreue gegen Mitgefühl (Hralda deckt die Freien Stimmen nicht, verrät sie aber auch nicht) |
| Story | Lizenz (Prolog), Archiv (MQ_A2_01), Unterschlupf bei `FS_STANCE` < 0, Späher in Nimbara |
| Nachhall | Wildwacht übernimmt die Aufsicht über geheilte (bzw. befriedete) Stillezonen; Questbretter „Nachhall-Pflege“ |
| Rangtitel | Gast · Helfer · Späher · Wächter · Hüter · Ehrenwächter |

### 2.4 F04 · Freie Stimmen

**Selbstbild:** Kein Echo gehört jemandem. Gegründet 967 nach dem Skandal um die Kontor-Arbeitslager.
**Fremdbild:** Gesetzlose, Diebe gebundener Echos (Kontor); „Kinder, die das Lied romantisieren“ (Akademie); „sie verstehen wenigstens Leid“ (Orden).
**Haltung zu Echos:** Bindung nur auf Zeit und mit Rückkehrrecht; Gewalt nur gegen Dinge, nie gegen Menschen oder Echos (Tavesh' Regel, ADR-007-konform).

| Aspekt | Inhalt |
|---|---|
| Orte | Morvenfurt-Unterstadt (Sitz, verborgen), Zellen in Saltrand, Sahrun, Ignareth; Lager bei Säulenrast (Akt II) |
| Aufträge | keine Questbrett-Aufträge (verborgen); Ruf über Befreiungen, Nebenquests, Schwarzmarkt |
| Innere Spannung | Tavesh' Misstrauen gegen alle Institutionen gegen den Wunsch vieler Mitglieder, legal zu werden |
| Story | Erstkontakt MQ_A1_04, Lagerbefreiung MQ_A2_03, Unterschlupf bei `FS_STANCE` ≥ 0, Windanker in Nimbara |
| Nachhall | Verbündet: Gaststatus im Bundesrat. Im Untergrund: Flugblätter, aber weiter Befreiungsquests (gleiche Belohnungen) |
| Rangtitel | Unbekannte Stimme · Zuhörer · Mitsänger · Stimme · Chorführer · Freie Stimme |

### 2.5 F05 · Orden der Stille

**Selbstbild:** Ohne Lied kein Leid. Gegründet 951 von Überlebenden der Klangpest; Schweigegelübde, keine Musik.
**Fremdbild:** Fanatiker mit Stillsteinen (Akt I–II); nach W6: „Getäuschte, die sich selbst befreit haben“.
**Haltung zu Echos:** Mitleid. Echos leiden am zu lauten Lied; Stille ist Fürsorge. Nach W6 spaltet sich der Orden: **Sereth-treu** (Stille als Angebot) und **Venn-treu** (Stille als Ordnung).

| Aspekt | Inhalt |
|---|---|
| Orte | Kloster Schweigfels (Sitz, ~120 Mitglieder), Kapellen in Ael'Dorun und Morvenmoor |
| Aufträge | ab Akt III: Stille Stunde (täglich), Nachhall: Hospiz-Dienst |
| Innere Spannung | Gelübde gegen Gewissen (Ulrek); Glaube gegen Werkzeug (Sereth nach W6) |
| Story | Gegner (Akt I–II) → Spaltung (W6) → Verbündete auf Zeit (Akt III) → Angebot „Sanfte Stille“ |
| Rufstart | **MQ_A2_07** (Der Verrat, ADR-180); Handel ab Akt III (K42 §9) |
| Nachhall | Versöhnt: Hospiz Schweigfels. Gebrochen: Splittergruppen mit gleichen Diensten, kühlerem Ton |
| Rangtitel | Fremder · Gast der Stille · Lauschender · Schweigender · Bruder/Schwester der Stille · Hüter der Pause |

Rangtitel sind **geschlechtsneutral wählbar** (Schweigender/Schweigende, Bruder/Schwester/Geschwister der Stille; K04 §10 Lokalisierungsregeln).

---

## 3. Rufränge

| Rank | Name | Threshold | Discount | Meaning |
|---|---|---|---|---|
| 1 | Fremd | 0 | 0 | Grunddienste, Aufträge |
| 2 | Bekannt | 300 | 5 | Rabatt 5 %, Blaupausen Stufe III, Fraktions-Nebenquests Kette 1 |
| 3 | Geachtet | 900 | 5 | Tutoren Stufe 1 (2.000 ◎), Fraktionsausrüstung kosmetisch, Kette 2 |
| 4 | Vertraut | 2000 | 10 | Rabatt 10 %, Blaupausen Stufe IV, Tutoren Stufe 2 (3.500 ◎), Kette 3 |
| 5 | Verbündet | 4000 | 10 | Fraktions-Reittier-Zubehör, Hain-Dekor, Kette 4, Ehrentitel |
| 6 | Getragen | 7000 | 15 | Rabatt Höchststufe (F02/F04 15 %, F01/F03 10 %), Blaupausen Stufe V, Fraktions-Mythosquest |

```
Rufpunkte  0      300        900          2.000              4.000                    7.000
           │──R1──│────R2────│─────R3─────│────────R4────────│──────────R5────────────│── R6 ──►
           Fremd   Bekannt    Geachtet      Vertraut           Verbündet                Getragen
                   │ 5 %                    │ 10 %                                     │ 10/15 %
                   │ Blaupausen III         │ Blaupausen IV, Tutoren 2                 │ Blaupausen V
                              │ Tutoren 1                      │ Kosmetik, Hain, Titel
```

| Regel | Inhalt | ADR |
|---|---|---|
| **Kein Rangverlust** | Ruf kann durch Entscheidungen sinken, aber nie unter die Schwelle des erreichten Rangs. Freigeschaltetes bleibt freigeschaltet. | ADR-177 |
| **Fraktion bekannt** | Ruf wird erst gesammelt, wenn die Fraktion eingeführt ist (`RepStart` in `Factions.csv`); vorher erworbene Punkte werden gutgeschrieben (z. B. Freilassen vor MQ_P03). | – |
| **Rabatte** | Rang 2/4/6 → 5/10/15 % (F01/F03 deckeln bei 10 %); kein Stapeln, höchster gilt (K42 §9). Orden ohne Rabatt. | – |
| **Ganzzahlig** | Alle Werte sind ganze Zahlen; keine Zufallsanteile (DR-03-Geist). | – |

---

## 4. Rufquellen

### 4.1 Quellen-Tabelle

| Name | Faction | Event | Amount | DailyCap | Phase |
|---|---|---|---|---|---|
| REP_CONTRACT | auto | Auftrag abgeschlossen (ContractTemplates.Faction) | BaseSol/5 | 0 | Prolog |
| REP_SQ_SMALL | auto | Nebenquest klein (Fraktionsquest) | 150 | 0 | Akt I |
| REP_SQ_CHAIN | auto | Nebenquest-Kettenabschluss | 400 | 0 | Akt I |
| REP_MQ | auto | Hauptquest mit Fraktionsbezug | 100–300 | 0 | Prolog |
| REP_RELEASE | F03 | Echo freilassen (statt binden oder nach Bindung) | 5 | 50 | Akt I |
| REP_RESCUE_SILENCE | F03 | Stillezone-Nachwirkung gelöst | 25 | 100 | Akt I |
| REP_KODEX | F01 | Kodex-Stufe 3 einer Art erreicht | 10 | 0 | Akt I |
| REP_FRAGMENT | F01 | Klangfragment entschlüsselt | 15 | 0 | Akt I |
| REP_TRADE | F02 | Handelsvolumen mit Kontor-Händlern (je 1.000 ◎ Kauf+Verkauf) | 20 | 200 | Prolog |
| REP_DELIVERY | F02 | Kontor-Lieferung pünktlich | 30 | 90 | Akt I |
| REP_LIBERATE | F04 | Echo aus Arbeitslager oder Hehlerei befreit | 40 | 160 | Akt I |
| REP_BLACKMARKET | F04 | Handelsvolumen Schwarzmarkt (je 1.000 ◎) | 15 | 150 | Akt I |
| REP_STILLHOUR | F05 | Stille Stunde in Schweigfels (Meditation) | 25 | 25 | Akt III |
| REP_HOSPICE | F05 | Hospiz-Dienst (verstörtes Echo beruhigt) | 40 | 120 | Nachhall |
| REP_SHELTER | auto | Unterschlupf nach dem Verrat (FLAG_SHELTER) | 200 | 0 | Akt II |

**Aufträge:** Ruf = `BaseSol / 5` der Auftragsvorlage (K13 §4): CT_OBSERVE 16, CT_PHOTO 18, CT_BOND 28, CT_GATHER 14, CT_DELIVER 22, CT_ESCORT 32, CT_CALM 40, CT_RESCUE 24, CT_SILENCE 48, CT_SURVEY 26. Die Fraktion steht in der Spalte `Faction` der Vorlage. Abklingzeiten der Vorlagen (1–3 Spieltage) begrenzen die Rate natürlich.

**Nebenquests (K49–K51):** Von den 210 Nebenquests gehören **~120** einer Fraktion (je ~24–28; Orden 12, ab Akt III). Jede Fraktion hat **vier Questketten** (Rang 2/3/4/5 als Einstieg; Orden: zwei – FQ_F05_01 ab Akt III, FQ_F05_02 im Nachhall, K48 §4), die mit 400 Ruf abschließen; einzelne Quests geben 150.

### 4.2 Hauptquests mit Rufbezug

| Abschnitt | Quest | Fraktion | Ruf |
|---|---|---|---|
| Prolog | MQ_P03 | Wildwacht | +100 |
| Akt I | MQ_A1_01 | Wildwacht | +150 |
| Akt I | MQ_A1_04 | Freie Stimmen | +150 |
| Akt I | MQ_A1_05 | Kontor | +150 |
| Akt I | MQ_A1_07 | Akademie | +150 |
| Akt I | MQ_A1_09 | Wildwacht | +100 |
| Akt II | MQ_A2_01 | Wildwacht | +200 |
| Akt II | MQ_A2_03 | Freie Stimmen | +300 |
| Akt II | MQ_A2_03 | Kontor | +200 |
| Akt II | MQ_A2_04 | Wildwacht | +100 |
| Akt II | MQ_A2_08 | Freie Stimmen | +200 |
| Akt II | MQ_A2_09 | Akademie | +200 |
| Akt II | MQ_A2_11 | Orden | +100 |
| Akt III | MQ_A3_01 | Akademie | +100 |
| Akt III | MQ_A3_04 | Orden | +200 |
| Akt III | MQ_A3_04 | Wildwacht | +100 |
| Akt III | MQ_A3_04 | Freie Stimmen | +100 |
| Akt III | MQ_A3_05 | Kontor | +150 |
| Akt III | MQ_A3_09 | Akademie | +200 |
| Akt III | MQ_A3_09 | Kontor | +200 |
| Akt III | MQ_A3_09 | Wildwacht | +200 |
| Akt III | MQ_A3_09 | Freie Stimmen | +200 |
| Akt III | MQ_A3_09 | Orden | +200 |

Bei abweichenden Entscheidungen verschiebt sich der Ruf, nie die Summe: MQ_A2_03 mit `KONTOR_CRATES` = 2 gibt Kontor +0 und Freie Stimmen +400 statt +300/+200; MQ_A2_08 gibt den Unterschlupf-Bonus (+200) der Wildwacht statt den Freien Stimmen, wenn `FLAG_SHELTER` = WW.

### 4.3 Herkunft des Rufs (Zielanteile)

| Fraktion | Aufträge | Nebenquests | Fraktionsquellen | Hauptquests |
|---|---|---|---|---|
| Akademie | 35 % | 40 % | 15 % (Kodex, Fragmente) | 10 % |
| Kontor | 30 % | 35 % | 25 % (Handel, Lieferungen) | 10 % |
| Wildwacht | 40 % | 30 % | 20 % (Freilassen, Stillezonen) | 10 % |
| Freie Stimmen | – | 55 % | 30 % (Befreiungen, Schwarzmarkt) | 15 % |
| Orden | – | 45 % | 45 % (Stille Stunde, Hospiz) | 10 % |

Kein Weg erzwingt Kampf: Jede Fraktion bietet mindestens 40 % ihres Rufs über gewaltfreie Tätigkeiten (Beobachten, Liefern, Freilassen, Befreien, Meditieren) – Säule S2 „Verstehen vor Kämpfen“.

---

## 5. Belohnungen

| Faction | Rank | Kind | Reward | Ref |
|---|---|---|---|---|
| F01 | 2 | Blueprint | Resonator III, Kodex-Linse III | K40 |
| F01 | 3 | Tutor | Tutoren F01 Stufe 1 (3 Fähigkeiten, 2.000 ◎) | K29 |
| F01 | 3 | Service | Labor: Fragment-Analyse 1×/Spieltag (zeigt eine Wortlücke) | K39 |
| F01 | 4 | Blueprint | Resonator IV, Kodex-Linse IV; Tutoren Stufe 2 (3.500 ◎) | K40/K29 |
| F01 | 5 | Cosmetic | Gelehrtenmantel, Hain-Dekor „Glyphentafel“ | K37 |
| F01 | 6 | Quest | Resonator V, Kodex-Linse V; Questreihe „Der Blick hinter das Glas“ (Mirrowisp) | K39/K62 |
| F02 | 2 | Blueprint | Wärtertasche III, Wärterwerkzeug III | K40 |
| F02 | 3 | Tutor | Tutoren F02 Stufe 1; Kontor-Schlüssel (Mechanik-Tore) | K29/K40 |
| F02 | 4 | Blueprint | Wärtertasche IV, Wärterwerkzeug IV; Tutoren Stufe 2; Lagerhaus +50 Plätze | K40 |
| F02 | 5 | Mount | Lastsattel-Zubehör (Packtaschen), Händlerwimpel | K40 |
| F02 | 6 | Blueprint | Wärtertasche V, Wärterwerkzeug V; Titel „Goldene Stimme“ | K40 |
| F03 | 2 | Blueprint | Gleiter III, Wanderstiefel III, Wettermantel III | K40 |
| F03 | 3 | Tutor | Tutoren F03 Stufe 1; Späher-Netz (Alpha-Positionen auf Karte) | K29 |
| F03 | 4 | Blueprint | Gleiter IV, Wanderstiefel IV, Wettermantel IV; Tutoren Stufe 2 | K40 |
| F03 | 5 | Sanctuary | Hain: eine Garten-Ausbaustufe nach Wahl ohne Materialkosten (1×), Dekor „Wildwacht-Hochstand“ | K37 |
| F03 | 6 | Blueprint | Gleiter V, Wanderstiefel V, Wettermantel V; Titel „Ehrenwächter“ | K40 |
| F04 | 2 | Blueprint | Laterne III, Atemmaske III; Schwarzmarkt-Zugang (MER_MORV_04) | K40/K11 |
| F04 | 3 | Tutor | Tutoren F04 Stufe 1; Zellen-Unterschlupf als Schnellreisepunkt (3) | K29 |
| F04 | 4 | Blueprint | Laterne IV, Atemmaske IV; Tutoren Stufe 2 | K40 |
| F04 | 5 | Cosmetic | Echo-Halstuch (Befreiungsabzeichen), Hain-Dekor „Freiheitsglocke“ | K37 |
| F04 | 6 | Blueprint | Laterne V, Atemmaske V; Titel „Freie Stimme“ | K40 |
| F05 | 2 | Service | Ordensladen Schweigfels (Ruhenetze, Schweigetee) | K12 |
| F05 | 3 | Tutor | Tutoren F05 Stufe 1 (Leere/Geist/Frost-Schwer-Fähigkeiten) | K29 |
| F05 | 4 | Tutor | Tutoren F05 Stufe 2; Stille-Stunde-Bonus (+1 Erholung im Hain) | K29/K37 |
| F05 | 5 | Cosmetic | Schweigegewand (kosmetisch), Hain-Dekor „Verhüllter Brunnen“ | K37 |
| F05 | 6 | Quest | Titel „Hüter der Pause“; Questreihe „Die Pause hören“ Teil 2 (Velnox-Variante) | K62 |

### 5.1 Blaupausen-Zuordnung (löst „Fraktion Ruf N“ aus K40)

| Ausrüstungsplatz | Fraktion | Stufe III (Ruf 2) | Stufe IV (Ruf 4) | Stufe V (Ruf 6) |
|---|---|---|---|---|
| Resonator | Akademie | ✓ | ✓ | ✓ |
| Kodex-Linse | Akademie | ✓ | ✓ | ✓ |
| Wärtertasche | Kontor | ✓ | ✓ | ✓ |
| Wärterwerkzeug | Kontor | ✓ | ✓ | ✓ |
| Gleiter | Wildwacht | ✓ | ✓ | ✓ |
| Wanderstiefel | Wildwacht | ✓ | ✓ | ✓ |
| Wettermantel | Wildwacht | ✓ | ✓ | ✓ |
| Laterne | Freie Stimmen | ✓ | ✓ | ✓ |
| Atemmaske | Freie Stimmen | ✓ | ✓ | ✓ |

Die Blaupause wird beim **Rüstmeister** der Fraktion gekauft (Preis = Wert der Ausrüstung × 0,5, K42 §3) und an der Werkbank hergestellt (K41). Der Orden hat keine Ausrüstung – seine Stärke sind Tutoren, Ruhe-Dienste und die Velnox-Variante im Nachhall.

### 5.2 Tutoren

Die 30 Tutoren aus K29 verteilen sich gleichmäßig: **6 je Fraktion** (3 auf Rang 3 für 2.000 ◎, 3 auf Rang 4 für 3.500 ◎; `Data/Abilities/Tutors.csv`). Ordenstutoren lehren bevorzugt Leere-, Geist- und Frost-Fähigkeiten und sind ab Akt III erreichbar (§8).

---

## 6. Beziehungen zwischen den Fraktionen

| ↓ über → | Akademie | Kontor | Wildwacht | Freie Stimmen | Orden |
|---|---|---|---|---|---|
| **Akademie** | – | Geldgeber, misstraut | nützlich, langsam | gefährlich naiv | Studienobjekt (vor W6: Werkzeug) |
| **Kontor** | Kunde mit Prestige | – | Regelwerk, notwendig | Diebe | schlechte Kunden |
| **Wildwacht** | Partner auf Papier | Partner auf Papier | – | Verwandte im Geist, nicht im Gesetz | Gegner mit Mitgefühl |
| **Freie Stimmen** | Käfigbauer | Lagerbetreiber | Halb-Verbündete | – | verstehen wenigstens Leid |
| **Orden** | (nach W6) Verräter | Lieferanten | Ordnungsmacht | Lärm | – |

**Spielwirkung:** Beziehungen sind **Erzählung, kein System** (ADR-179). Es gibt keine automatische Rufkopplung („+100 Kontor = −50 Freie Stimmen“). Sie zeigen sich in Barks, Nebenquest-Dilemmata (§7) und Händlerkommentaren. Begründung: Rufkopplung bestraft Neugier und macht Spielende zu Buchhaltern; AETHRIS will, dass man jeder Fraktion zuhören kann.

---

## 7. Entscheidungen ohne Ausschluss

Manche Nebenquests stellen Fraktionen gegeneinander. Regel: **Eine Wahl gibt Ruf, keine Wahl nimmt Ruf** (abgesehen von ausdrücklich markierten Story-Momenten, die nie unter den Rangboden fallen, ADR-177).

| Beispiel (K49–K51) | Option A | Option B | Option C |
|---|---|---|---|
| Hehlerware in Dorunsruh | Akademie melden (+150 F01) | Freien Stimmen übergeben (+150 F04) | Dem Echo selbst die Wahl lassen (+100 F03, Kodex-Beobachtung) |
| Kontor-Lieferung mit verstummten Echos | Liefern (+150 F02) | Echos heilen und freilassen (+150 F04, +5/Echo F03) | Marieke direkt konfrontieren (+100 F02, +100 F04; nur bei `KONTOR_CRATES` ≥ 1) |
| Stillstein-Nest im Morvenmoor (vor W6) | Zerstören (+150 F03) | Akademie zur Analyse bringen (+150 F01) | Liegen lassen und Ordenswache befragen (Kodex-Lore, +0) |
| Ordens-Novize auf der Flucht (nach W6) | Nach Schweigfels bringen (+150 F05) | Bei den Freien Stimmen verstecken (+150 F04) | Wildwacht übergeben (+150 F03) |

**Designregel:** Mindestens eine Option jedes Dilemmas ist eine „dritte Lösung“, die über Verstehen statt Parteinahme läuft (Säule S2).

---

## 8. Ruf-Verlauf über die Spielzeit

Mit den typischen Raten aus `aethris_reputation.py` (Aufträge, Nebenquests, Fraktionsquellen; kanonische Story-Wahl):

| Abschnitt | Akademie | Kontor | Wildwacht | Freie Stimmen | Orden |
|---|---|---|---|---|---|
| Prolog | 0 (R1) | 15 (R1) | 160 (R1) | 0 (R1) | 0 (R1) |
| Akt I | 420 (R2) | 465 (R2) | 890 (R2) | 330 (R2) | 0 (R1) |
| Akt II | 2.020 (R4) | 2.165 (R4) | 2.890 (R4) | 2.730 (R4) | 100 (R1) |
| Akt III | 3.280 (R4) | 3.475 (R4) | 4.150 (R5) | 3.990 (R4) | 1.220 (R3) |
| Endgame 1–20 h | 4.680 (R5) | 4.875 (R5) | 5.550 (R5) | 5.390 (R5) | 2.820 (R4) |
| Endgame 20–40 h | 5.880 (R5) | 6.075 (R5) | 6.750 (R5) | 6.590 (R5) | 4.220 (R5) |
| Endgame 40–60 h | 6.880 (R5) | 7.075 (R6) | 7.750 (R6) | 7.590 (R6) | 5.420 (R5) |

**Ziel-Checks:**

| Prüfung | Ergebnis |
|---|---|
| Akademie, Kontor, Wildwacht Rang 2 am Ende von Akt I (Blaupausen III) | ✓ |
| Freie Stimmen Rang 2 spätestens Mitte Akt II | ✓ |
| F01–F04 Rang 4 am Ende von Akt II (Blaupausen IV, Tutoren Stufe 2) | ✓ |
| Orden Rang 3 am Ende von Akt III (Ordenstutoren Stufe 1) | ✓ |
| Keine Fraktion Rang 6 vor dem Endgame | ✓ |
| Mindestens drei Fraktionen Rang 6 nach 60 h Endgame (typisch) | ✓ |
| Fokus: F01–F04 Rang 6 in ≤ 25 h Endgame (150 Ruf/h) | ✓ |
| Fokus: Orden Rang 6 in ≤ 40 h Endgame (später Start, ADR-180) | ✓ |

**Fokus-Spiel:** Wer im Endgame gezielt für eine Fraktion arbeitet (≈ 150 Ruf/h: Aufträge mit Abklingzeiten parallel, offene Kette, Fraktionsquelle bis zur Tageskappe), erreicht Rang 6:

| Fraktion | Ruf am Ende von Akt III | Fehlend bis Rang 6 | Stunden bei Fokus (150 Ruf/h) |
|---|---|---|---|
| Akademie | 3.280 | 3.720 | 25 |
| Kontor | 3.475 | 3.525 | 24 |
| Wildwacht | 4.150 | 2.850 | 19 |
| Freie Stimmen | 3.990 | 3.010 | 21 |
| Orden | 1.220 | 5.780 | 39 |

Der Orden braucht länger, weil sein Ruf erst mit dem Verrat beginnt (ADR-180). Das ist gewollt: Vertrauen zu einem früheren Gegner wächst langsamer.

---

## 9. Fraktionen über die Story

### 9.1 Zustände je Akt

| Fraktion | Prolog/Akt I | Akt II | Akt III | Nachhall (beide Enden) |
|---|---|---|---|---|
| Akademie | Außenstelle Eichenhall, Venn freundlich | Messung, **Verrat** (W6), Aevrin öffnet die Akten | Akademie neutral, Labore in Prismara helfen | kommissarisch Aevrin |
| Kontor | Kredit, Handel | Kisten, Lagerskandal | Luftfracht nach Nimbara | Satzung „Klangtreue“ |
| Wildwacht | Lizenz, Sattel | Archiv, ggf. Unterschlupf | Späher in Nimbara | Pflege der Stillezonen |
| Freie Stimmen | Erstkontakt Morvenmoor | Lagerbefreiung, ggf. Unterschlupf | Windanker | verbündet oder Untergrund |
| Orden | Gegner (Ulrek, Stillsteine) | Eiðvik, Spaltung | Sereth an der Seite des Spielers | Hospiz oder Splittergruppen |

### 9.2 Data Layers und Händler

| Ereignis | Wirkung | Technik |
|---|---|---|
| W6 (MQ_A2_07) | Akademie-Wachen in Dorunsruh durch Stadtwache ersetzt; Ordensgegner in Ael'Dorun gemischt | `DL_Story_R08_PostW6`, Encounter-Tabelle |
| Akt III | Ordensladen Schweigfels öffnet (Ruf F05 ≥ 2; K12 §6) | neuer Händler `MER_SCHW_01` (K12-Nachtrag in `Merchants.csv`) |
| Nachhall | Akademie-Banner tragen Aevrins Glyphe; Freie-Stimmen-Zellen sichtbar (verbündet) oder weiter verborgen | `DL_Nachhall`, Flag `FLAG_FS_STANCE` |

### 9.3 Ruf × Haltung in Dialogen

Dialoge werten **Ruf-Rang** (Was hast du getan?) und **Story-Flag** (Wie stehst du zu uns?) getrennt aus:

| | Haltung positiv | Haltung neutral/negativ |
|---|---|---|
| **Rang ≥ 4** | „Freund und Helfer“ – warmer Ton, Insider-Barks | „Du hilfst uns mehr, als du zugibst.“ – respektvoll, distanziert |
| **Rang ≤ 3** | „Du glaubst an uns, aber wir kennen dich kaum.“ | Höflich-neutral, Standard-Barks |

Bark-Tags: `Faction.<F>.Rank.High|Low` × `Story.Stance.<F>.Pos|Neg` (K53/K55).

---

## 10. Technik

### 10.1 Interface

`IReputationService` (`Source/AethrisCore/Public/Services/ReputationService.h`, implementiert in GF_Quests, K06 §5):

| Methode | Zweck |
|---|---|
| `GetStanding(Faction)` | Punkte, Rang, Rest bis zum nächsten Rang, Rabatt, Freischaltung |
| `AddReputation(Faction, Amount, SourceId)` | Wendet eine Quelle an; Tageskappe, Rangboden; Events `Event.Reputation.Changed` / `.RankUp` |
| `GetBestDiscountPermille(MerchantFactions)` | Höchster Rabatt (kein Stapeln) |
| `MeetsRank(Faction, Rank)` | Bedingungen für Blaupausen, Tutoren, Ketten, Dialoge |

### 10.2 Ablauf `AddReputation`

```
AddReputation(F, amount, src):
    s ← standing[F]
    if not s.unlocked: pending[F] += amount; return {Applied=0}
    cap ← Sources[src].DailyCap
    if cap > 0:
        used ← dailyUsed[(src, F, GameDay)]
        amount ← min(amount, cap − used)        // GameDay aus der Spieluhr (K15), nicht Echtzeit
        dailyUsed[(src, F, GameDay)] += max(amount, 0)
    floor ← Threshold[s.rank]                   // ADR-177
    newPoints ← max(floor, s.points + amount)
    newRank ← RankOf(newPoints)
    publish Event.Reputation.Changed{F, newPoints − s.points}
    if newRank > s.rank: publish Event.Reputation.RankUp{F, newRank}; UnlockRewards(F, s.rank+1 … newRank)
    s.points, s.rank ← newPoints, newRank
```

### 10.3 Save-Fragment

| Feld | Typ | Inhalt |
|---|---|---|
| `Reputation.Points[5]` | int32 | Punkte je Fraktion |
| `Reputation.Pending[5]` | int32 | Gutschrift vor Freischaltung |
| `Reputation.DailyUsed` | Map<(SourceId, Faction), int32> | nur aktueller Spieltag; beim Tageswechsel geleert |
| `Reputation.RewardsClaimed` | Bitset (30) | abgeholte Rangbelohnungen |

Fragment-Name `Player.Reputation`, Version 1 (K64). Ränge werden beim Laden aus Punkten neu berechnet (Daten-Tuning ändert nie gespeicherte Ränge nach unten: Rangboden gilt auch beim Laden).

### 10.4 Datenpipeline

`Factions.csv`, `ReputationRanks.csv`, `ReputationSources.csv`, `ReputationRewards.csv` werden über den Importer (K06 §3) zu `UFactionDefinition` (Primary Asset Type `Faction`, IDs F01–F05) und einer `UReputationTable` (Ränge, Quellen, Belohnungen). Validator-Regeln:

| Regel | Prüfung |
|---|---|
| REP-01 | Genau 6 Ränge, Schwellen streng steigend, Rang 1 = 0 |
| REP-02 | Jede Fraktion hat auf Rang 2–6 mindestens eine Belohnung |
| REP-03 | Jede `Faction.*` in `ContractTemplates.csv` existiert in `Factions.csv` |
| REP-04 | Jeder Ausrüstungsplatz aus `WardenGear.csv` (Stufe III–V) ist genau einer Fraktion zugeordnet (`GearSlots`) |
| REP-05 | Tutoren-Ränge ∈ {3, 4} und je Fraktion 6 Tutoren |
| REP-06 | Referenzmodell: alle Ziel-Checks ✓ (§8) |

---

## 11. UI

```
┌─ WÄRTERBUCH ▸ FRAKTIONEN ──────────────────────────────────────────────┐
│  [Akademie] [Kontor] [Wildwacht] [Freie Stimmen] [Orden 🔒→ab Akt II]   │
│                                                                          │
│  WILDWACHT  ·  „Wir schützen das Wilde, nicht vor dem Wilden.“           │
│  Rang 4 · Wächter        ████████████░░░░░░░  2.890 / 4.000              │
│  Rabatt 10 %  ·  Rüstmeisterin Fenja (Eichenhall, WW-Außenposten)        │
│                                                                          │
│  Nächster Rang (Verbündet):  Hain-Ausbau ohne Materialkosten, Hochstand  │
│  Offene Kette: „Die Spur der Lauscherin“ (3/5)                           │
│  Heute: Freilassen 35/50 · Stillezonen 25/100                            │
│                                                                          │
│  Was die Wildwacht über dich sagt:  „Ein Wärter, der zuhört.“            │
└──────────────────────────────────────────────────────────────────────────┘
```

- Rufgewinne erscheinen als kleine Einblendung mit Fraktionsfarbe (`Factions.csv` Spalte `Color`), gesammelt nach Kämpfen/Dialogen (keine Einzel-Spam-Meldungen).
- **Rangaufstieg** ist ein kurzer Moment (2 s, Fraktionsmotiv, K55) mit Liste der Freischaltungen.
- Die Zeile „Was … über dich sagt“ wertet Ruf × Haltung aus (§9.3) – die einzige Stelle, an der der Spieler die Haltung indirekt sieht.
- Barrierefreiheit: Farben nie allein (Wappen-Icons), Fortschritt auch als Zahl (K54).

---

## 12. Anti-Exploit und Koop

| Risiko | Gegenmaßnahme |
|---|---|
| Binden/Freilassen-Schleife für Wildwacht-Ruf | Tageskappe 50 (10 Freilassungen), Freilassen nur ≥ 1 Spielstunde nach Bindung zählt |
| Kauf/Verkauf-Schleife für Kontor-Ruf | Rückkauf desselben Artikels binnen 1 Spieltag zählt nicht; Tageskappe 200 |
| Zeitvorspulen für Tageskappen | Kappen hängen am Spieltag; ein Tageswechsel durch Vorspulen (CANON §65) setzt Kappen nur zurück, wenn seit dem letzten Zurücksetzen ≥ 30 min Echtzeit gespielt wurden (Vorspulen selbst bleibt unbegrenzt) |
| Koop-Farming | Gäste erhalten Ruf aus Aufträgen und Quests des Hosts **in ihrer eigenen Welt**, nur für Quellen, die sie selbst ausgelöst haben; keine Übertragung von Punkten |
| Ruf-Kauf | Kein Ruf gegen Sol, keine Echtgeld-Booster (K42 §1, CANON §8) |

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Quest Design | ~120 Fraktions-Nebenquests, 4 Ketten je Fraktion (Orden: 2 Ketten + Nachhall-Ketten), Dilemmata mit dritter Lösung | K49–K51 |
| Narrative | Rangtitel (neutral wählbar), ~1.500 Fraktions-Barks (Rang × Haltung) | K53/K55 |
| Economy | Blaupausenpreise, Rabatte (unverändert K42 §9) | K42/K63 |
| Programmierung | `IReputationService` in GF_Quests, Save-Fragment `Player.Reputation`, Validator REP-01–06 | K48/K64 |
| UI | Fraktionsseite, Rufeinblendung, Rangaufstieg | K54 |
| Audio | 5 Fraktionsmotive (Rangaufstieg, Händler) | K55 |
| Art | 5 Wappen, Banner (inkl. Aevrin-Glyphe im Nachhall), 6 kosmetische Fraktionsitems | K56 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-177 | Kein Rangverlust: Ruf fällt nie unter die Schwelle des erreichten Rangs | Keine Bestrafung für Entscheidungen; Freischaltungen bleiben stabil | Ruf frei sinkend (Frust, Save-Scumming) |
| ADR-178 | Ruf (Taten) und Story-Haltung (Flags) sind getrennte Werte | Spielende können zuhören, ohne Partei zu ergreifen; Dialoge werten beides aus | ein einziger Gesinnungswert je Fraktion |
| ADR-179 | Keine automatische Rufkopplung zwischen Fraktionen | Neugier wird nicht bestraft; alle Fraktionen auf Rang 6 möglich | Gegenläufige Fraktionen (Kontor ↔ Freie Stimmen) |
| ADR-180 | Ordensruf beginnt mit dem Verrat (MQ_A2_07); Handel ab Akt III | Erzählung: Vertrauen zu einem früheren Gegner wächst spät | Ordensruf ab Akt I |
| ADR-181 | Tageskappen je Quelle über die Spieluhr | Begrenzt Schleifen, ohne Abklingzeiten-Frust bei normalem Spiel | Echtzeit-Kappen, Wochenkappen |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §181 | Fraktionsprofile F01–F05 (`Factions.csv`): Rüstmeister, Ausrüstungsplätze, Rufstart, Farben, Rangtitel | LOCKED |
| §182 | Rufränge 1–6 (0/300/900/2.000/4.000/7.000), kein Rangverlust, Quellen mit Tageskappen (`ReputationSources.csv`), Aufträge = BaseSol/5 | LOCKED |
| §183 | Belohnungen (`ReputationRewards.csv`): Blaupausen III/IV/V auf Rang 2/4/6 je Fraktion, Tutoren 6 je Fraktion (Rang 3/4), Rabatte K42 §9 | LOCKED |
| §184 | Fraktionen über die Story: Zustände je Akt, Ruf × Haltung in Dialogen, Orden ab W6 | LOCKED |
| §7 | Fraktionsdetails → K47 erledigt | LOCKED |
| §10 | ADR-177 – ADR-181 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Rolle der Fraktionen, Trennung Ruf/Haltung
- [x] Fünf Fraktionsprofile mit Orten, Aufträgen, Spannungen, Story, Nachhall, Rangtiteln
- [x] Sechs Rufränge mit Schwellen, Rabatten, Regeln
- [x] Rufquellen inkl. Hauptquest-Boni und Zielanteilen
- [x] Belohnungen, Blaupausen-Zuordnung (K40), Tutoren (K29)
- [x] Beziehungen, Dilemmata ohne Ausschluss
- [x] Ruf-Verlauf (Referenzmodell) mit Ziel-Checks und Fokus-Spiel
- [x] Technik: Interface, Ablauf, Save-Fragment, Validator; UI; Anti-Exploit; Koop
- [x] Anforderungen, ADR-177 – ADR-181, CANON §181–§184

➡️ **Nächstes Kapitel: K48 – Quest-Bibel und Questsystem-Technik.**
