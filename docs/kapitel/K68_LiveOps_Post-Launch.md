# K68 · LiveOps und Post-Launch

| Feld | Wert |
|---|---|
| Dokument | Kapitel 68 von 68 · Produktion III |
| Version | 1.0 |
| Owner | Live Producer, Game Director |
| Mitwirkende | Community Manager, Live-Ops-Engineer, Backend/DevOps, Lead Content Designer (Erweiterungen), Data Scientist, Monetarisierung (Kosmetik), QA Live, Plattform-Programmierung |
| Baut auf | K01 §14 (Geschäftsmodell, CANON §2), K02 (DR-17, DR-19, DR-20, DR-23), K14 (Resonanzsturm), K52 (Wanderungen), K59 (Betrieb, Backend), K60 (Zirkel-Chronik, Fotos), K61 (Saisons), K62 (Endgame, Aurelune), K63 (Live-Balancing), K66 (Qualität), K67 (Release, Übergabe) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/LiveOps/Events.csv` (10 Events), `ReleasePlan.csv` (11 Releases), `ShopCatalog.csv`, `LiveKPIs.csv`; Referenzmodell `tools/ref/aethris_liveops.py` (LO-01–LO-07, Jahreskalender) |
| Neue Kanon-Einträge | CANON §268 (Live-Säulen, Fahrplan), §269 (Events und Saisons), §270 (Erweiterungen, Monetarisierung), §271 (Betrieb, Gemeinschaft, Kennzahlen, Lebensende) |

---

## Inhalt

1. [Ziele und Live-Säulen](#1-ziele-und-live-säulen)
2. [Post-Launch-Fahrplan](#2-post-launch-fahrplan)
3. [Events und Saisons](#3-events-und-saisons)
4. [Erweiterungen](#4-erweiterungen)
5. [Monetarisierung](#5-monetarisierung)
6. [Live-Betrieb](#6-live-betrieb)
7. [Gemeinschaft und Kommunikation](#7-gemeinschaft-und-kommunikation)
8. [Kennzahlen](#8-kennzahlen)
9. [Langfristig: Jahr 3 und das Ende der Server](#9-langfristig-jahr-3-und-das-ende-der-server)
10. [Prüfregeln](#10-prüfregeln)
11. [Abschluss des Kapitelsystems](#11-abschluss-des-kapitelsystems)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Ziele und Live-Säulen

AETHRIS ist ein vollständiges Premium-Spiel. Der Live-Betrieb soll es **länger klingen lassen**, nicht länger festhalten. Die Säulen:

| Säule | Bedeutung | Gegenbeispiel (verboten) |
|---|---|---|
| **L-1 Respekt vor Zeit** | Keine täglichen Pflichten, keine Login-Belohnungen, keine Energie (DR-23) | „Komm morgen wieder, sonst verpasst du …“ |
| **L-2 Vollständig auch offline** | Jeder Spielinhalt hat einen Weg ohne Event und ohne Online (DR-19) | Event-exklusive Echos |
| **L-3 Fair** | Kein Pay-to-Win, kein Zufall gegen Geld, keine Echos im Shop (CANON §8.2, DR-17, DR-20) | Lootboxen, Morph-Verkauf, Siegel-Pakete |
| **L-4 Transparent** | Fahrplan öffentlich, Patch-Notizen mit Begründung, Preise klar | stille Änderungen, Zwischenwährungen |
| **L-5 Gemeinsam** | Events, die Menschen zusammenbringen (Feste, Wanderungen, Fotowettbewerbe), nicht gegeneinander | Ranglisten-Druck für alle |
| **L-6 Nachhaltig** | Ein Live-Team, das ohne Crunch arbeitet; planbarer Rhythmus | Wochenend-Events mit Bereitschaft ohne Ausgleich |

---

## 2. Post-Launch-Fahrplan

| Name | Month | Kind | Content |
|---|---|---|---|
| 1.0.1 | 0 | Day-One-Patch | Restfehler S3, Performance-Feinschliff, Server-Skalierung |
| 1.1 | 1 | Update | Stabilität, Komfort (Hain-Sortierung, Kodex-Filter), Barrierefreiheits-Wünsche |
| 1.2 | 3 | Saison 1 | Zirkel-Chronik, Saisonregel „Kleine Stimmen“, erste Raid-Woche, Ranked S1 |
| 1.3 | 5 | Update | RAID_09 (kostenlos), neue Dissonanzen, Fotomodus-Erweiterung |
| 1.4 | 7 | Saison 2 | Ranked-Duell-Nebenliste, Gleichklang-Freundeskampf-Turniere, Hain-Themen |
| 2.0 | 10 | Erweiterung 1 | Region R11 „Thalgrund“ (Tiefsee unter Saltrand), 36 Echos #257–#292, Story-Kapitel im Nachhall, Tauchen |
| 2.1 | 12 | Saison 3 | Jahrestag, Weltakkord-Ranglisten, RAID_10 (kostenlos) |
| 2.2 | 15 | Update | Neue Taktproben, Zucht-Komfort, Zirkel-Fotowand |
| 2.3 | 18 | Saison 5 | Saisonregeln rotieren, PvP-Turniere durch Zirkel |
| 3.0 | 21 | Erweiterung 2 | Region R12 „Wurzelgrund“ (Höhlen unter dem Uralthain), 34 Echos #293–#326, Story-Kapitel, Graben-Erkundung |
| 3.1 | 24 | Saison 7 | Zweiter Jahrestag, Abschluss der Erweiterungsgeschichte |

**Rhythmus:** Im ersten Jahr erscheint mindestens alle drei Monate ein kostenloses Update oder eine Saison (LO-06). Die Saisons folgen dem Ranked-Kalender (K61 §4.7); jede Saison bringt eine Saisonregel, Gesten, Titel und Chronik-Ziele. Zwei kostenlose Raids (RAID_09, RAID_10) erweitern das Endgame; zwei Erweiterungen im Expansion-Pass erweitern die Welt (K01 §14).

### 2.1 Das erste Jahr in Worten

Die ersten Wochen gehören der Stabilität: Day-One-Patch, Server-Skalierung, schnelle Behebung von Fehlern, die erst mit Millionen Spielenden sichtbar werden. Das erste Update im Monat 1 bringt Komfort, den die Gemeinschaft sich wünscht – Sortierungen, Filter, kleine Barrierefreiheits-Verbesserungen. Mit Saison 1 im Monat 3 beginnen die Zirkel-Chronik und die erste Saisonregel; die Welt bekommt ihren ersten globalen Rhythmus aus Resonanzsturm-Nächten, Raid-Wochen und Fotowettbewerben. Im Frühling feiert ganz Aethris das Lindenfest, im Herbst das Sternfest von Nimbara. Monat 10 öffnet mit der ersten Erweiterung die Tiefsee vor Saltrand; zum Jahrestag im Monat 12 versammelt ein Konzert in Aerion alle, die mitgespielt haben.

---

## 3. Events und Saisons

### 3.1 Wiederkehrende Events

| DisplayName | Kind | Cadence | Duration | Content | Rewards | OfflinePath |
|---|---|---|---|---|---|---|
| Resonanzsturm-Nacht | Welt | alle 6 Wochen | 48 h | Globaler Resonanzsturm (alle Spielenden gleichzeitig), Aurelune-Begegnung möglich, quantisierte Rufe | Kodex-Fotos, Sturm-Geste | Sturmstimmgabel (Abklingzeit 3 Spieltage, K62) |
| Lindenfest der Welt | Fest | jährlich (Frühling) | 7 Tage | Feste in allen Siedlungen gleichzeitig, Tanz-Gesten, Festmusik | Festkleidung (Kosmetik), Hain-Deko „Lindenkranz“ | Lindenfest in Eichenhall jeden 7. Spieltag (K13) |
| Sternfest von Nimbara | Fest | jährlich (Herbst) | 7 Tage | Sternschauer-Nächte, Sternwärter-Aufgaben, Foto-Wettbewerb Nachthimmel | Gleiter-Muster „Sternbahn“, Fotorahmen | Sternschauer-Nächte im Spielkalender (K15) |
| Raid-Woche | Kampf | monatlich | 7 Tage | Ein Raid im Fokus mit Zusatz-Mechanik-Variante, Gruppensuche hervorgehoben | Raid-Banner-Variante | Solo-Variante jederzeit (CANON §129) |
| Fotowettbewerb | Gemeinschaft | monatlich | 14 Tage | Thema (z. B. „Echos im Regen“), Abstimmung der Gemeinschaft, moderiert | Fotorahmen, Titel des Monats | Fotomodus und Kodex-Fotos immer verfügbar |
| Große Wanderung | Welt | zweimal jährlich | 10 Tage | Seltene Wanderherden ziehen durch drei Regionen (deterministischer Plan, K52) | Kodex-Verhaltensfotos | Wanderungen im Spiel nach Spielkalender (seltener) |
| Saisonregel-Woche | PvP | je Saison | 7 Tage | Sonderregelsatz in der Arena-Halle (z. B. „Kleine Stimmen“) | Gesten, Titel | Freundeskampf mit allen Regeln jederzeit |
| Zirkel-Chronik | Gemeinschaft | wöchentlich ab Saison 1 | 7 Tage | Drei Gemeinschaftsziele je Zirkel (K60) | kosmetisch (GuildGoals.csv) | – |
| Echo der Stille | Welt | vierteljährlich | 5 Tage | Kurze Stillezonen kehren an wechselnden Orten zurück und werden gemeinsam geheilt (Zählstand global) | Hain-Deko „Geheilter Stein“ | Wildwacht-Aufträge CT_SILENCE (K13) |
| Jahrestag von AETHRIS | Fest | jährlich (Launch-Monat) | 14 Tage | Rückblick, Dank, Konzert-Event in Aerion (Musik K55), Entwickelnden-Kommentare | Titel „Erstes Jahr“, Konzert-Geste | Konzert bleibt als Aufnahme im Hain-Musikspieler; Geste danach über Feste erreichbar |

**Regeln für Events:**

| Regel | Inhalt |
|---|---|
| Wiederkehr | Jedes Event kehrt mindestens jährlich zurück; Belohnungen sind beim nächsten Mal wieder erreichbar |
| Offline-Weg | Spielinhalte (Begegnungen, Wetter, Wanderungen) gibt es auch ohne Event, seltener oder über Items (LO-02) |
| Belohnungen | Kosmetik, Titel, Gesten, Kodex-Fotos – nie Echos, Siegel, Sol, Werte (LO-03) |
| Dichte | Höchstens drei zeitlich begrenzte Events gleichzeitig (LO-01) |
| Zeit | Echtzeit-Kalender (Ausnahme zu Spielzeit, K02 §13); Ankündigung mindestens 14 Tage vorher |
| Determinismus | Event-Welten nutzen dieselben Seeds/Fahrpläne wie das Spiel; Wetter-Overrides (Resonanzsturm) als `DL_Event_*` und Wetter-Override (K14) |

### 3.2 Jahreskalender (Jahr 1)

Der Kalender aus `aethris_liveops.py` zeigt die Wochen mit Events und Releases (W1 = Launch-Woche, November 2030):

| Woche (ab Launch) | Monat | Events | Release |
|---|---|---|---|
| W1 | Nov | – | 1.0.1 (Day-One-Patch) |
| W2 | Nov | Raid-Woche | – |
| W3 | Nov | Fotowettbewerb | – |
| W4 | Nov | Resonanzsturm-Nacht, Fotowettbewerb | – |
| W6 | Dez | Raid-Woche | 1.1 (Update) |
| W8 | Dez | Fotowettbewerb | – |
| W9 | Dez | Fotowettbewerb, Echo der Stille | – |
| W10 | Jan | Resonanzsturm-Nacht | – |
| W11 | Jan | Raid-Woche | – |
| W12 | Jan | Fotowettbewerb | – |
| W13 | Jan | Fotowettbewerb | – |
| W14 | Feb | Große Wanderung | 1.2 (Saison 1) |
| W15 | Feb | Raid-Woche, Große Wanderung, Saisonregel-Woche | – |
| W16 | Feb | Resonanzsturm-Nacht, Fotowettbewerb | – |
| W17 | Feb | Fotowettbewerb | – |
| W19 | Mär | Raid-Woche | – |
| W21 | Mär | Fotowettbewerb | – |
| W22 | Mär | Resonanzsturm-Nacht, Fotowettbewerb, Lindenfest der Welt | – |
| W23 | Apr | Echo der Stille | 1.3 (Update) |
| W24 | Apr | Raid-Woche | – |
| W25 | Apr | Fotowettbewerb | – |
| W26 | Apr | Fotowettbewerb | – |
| W28 | Mai | Resonanzsturm-Nacht, Raid-Woche, Saisonregel-Woche | – |
| W29 | Mai | Fotowettbewerb | – |
| W30 | Mai | Fotowettbewerb | – |
| W32 | Jun | Raid-Woche | 1.4 (Saison 2) |
| W34 | Jun | Resonanzsturm-Nacht, Fotowettbewerb | – |
| W35 | Jun | Fotowettbewerb, Echo der Stille | – |
| W37 | Jul | Raid-Woche | – |
| W38 | Jul | Fotowettbewerb | – |
| W39 | Jul | Fotowettbewerb, Große Wanderung | – |
| W40 | Aug | Resonanzsturm-Nacht, Große Wanderung | – |
| W41 | Aug | Raid-Woche, Saisonregel-Woche | – |
| W42 | Aug | Fotowettbewerb | – |
| W43 | Aug | Fotowettbewerb | – |
| W45 | Sep | Raid-Woche | 2.0 (Erweiterung 1) |
| W46 | Sep | Resonanzsturm-Nacht | – |
| W47 | Sep | Fotowettbewerb | – |
| W48 | Sep | Fotowettbewerb, Sternfest von Nimbara | – |
| W49 | Okt | Echo der Stille | – |
| W50 | Okt | Raid-Woche | – |
| W51 | Okt | Fotowettbewerb | – |
| W52 | Okt | Resonanzsturm-Nacht, Fotowettbewerb, Jahrestag von AETHRIS | – |
| W53 | Nov | Jahrestag von AETHRIS | 2.1 (Saison 3) |

### 3.3 Drei Events im Detail

**Resonanzsturm-Nacht (alle 6 Wochen, 48 h).** Ein globaler Resonanzsturm zieht über alle Welten gleichzeitig (Wetter-Override, K14): Rufe werden auf die Aethrische Skala quantisiert (K55), Wildechos sind aggressiver, und in der Nacht kann Aurelune über Lumeya erscheinen (K62 §5.6). Wer nicht online ist oder das Event verpasst, nutzt die Sturmstimmgabel; das Event ist die gemeinsame, nicht die einzige Gelegenheit. Belohnungen sind Kodex-Fotos von Sturmverhalten und eine Sturm-Geste.

**Große Wanderung (zweimal jährlich, 10 Tage).** Seltene Wanderherden ziehen auf einem festen Pfad durch drei Regionen (Ökologie-Herdenverhalten K52, deterministischer Plan). Spielende verfolgen, fotografieren und begleiten die Herde; Zirkel teilen sich Beobachtungsposten. Außerhalb des Events gibt es dieselben Wanderungen seltener im Spielkalender. Das Event zeigt, was AETHRIS besonders macht: eine lebendige Welt, in der man Echos beobachtet, statt sie nur zu sammeln.

**Echo der Stille (vierteljährlich, 5 Tage).** An wechselnden Orten kehren kleine Stillezonen zurück. Alle Spielenden heilen sie gemeinsam – ein globaler Zähler zeigt, wie viele Zonen in allen Welten geheilt wurden, und jede Heilung spielt die Heilungswelle (K58). Am Ende schaltet die Gemeinschaft ein Hain-Dekor frei. Offline gibt es dieselbe Tätigkeit über die Wildwacht-Aufträge (CT_SILENCE).

### 3.4 Saisons

Saisons dauern 12 Wochen mit einer Woche Pause (Saisonregel-Woche, K61 §4.7). Jede Saison hat ein Thema aus der Welt (z. B. „Tiefen des Kharsgrats“, „Nächte der Weite“), das sich in Chronik-Zielen, Saisonregel und Kosmetik zeigt. Belohnungen richten sich nach der höchsten erreichten Stufe (ADR-253) und nach Beteiligung, nie nach täglicher Anwesenheit. Es gibt **keinen bezahlten Saison-Pass** (K01 §14.2).

---

## 4. Erweiterungen

Zwei Story-Erweiterungen im Expansion-Pass führen das Nachhall-Kapitel (K62) weiter. Beide funktionieren mit beiden Enden (K46); die Erzählung bezieht sich auf die Welt nach dem Finale, nicht auf eine der Entscheidungen.

| | Erweiterung 1 | Erweiterung 2 |
|---|---|---|
| Titel (Arbeitstitel) | „Was die Tiefe singt“ | „Wo die Wurzeln hören“ |
| Region | R11 **Thalgrund** – Tiefsee und Unterwasserhöhlen vor Saltrand | R12 **Wurzelgrund** – Höhlen unter dem Uralthain |
| Thema | Gezeiten, Druck, Licht ohne Sonne; Thal'assyr als Zeugin älterer Lieder | Erinnerung, Wachstum im Dunkeln; Sylv'anor und die Wurzeln des Weltlieds |
| Neue Mechanik | Tauchen mit Schwimmreittieren (Luft durch Klangblasen), Strömungsrätsel | Graben in neue Ebenen, Wurzelpfade, Echo-Höhlen mit Nachhall |
| Echos | 36 (#257–#292) | 34 (#293–#326) |
| Inhalt | Story-Kapitel (≈ 12 h), 25 Nebenquests, 1 Tiefenresonanz, 1 Raid, Siedlung „Perlhall“ | Story-Kapitel (≈ 12 h), 25 Nebenquests, 1 Tiefenresonanz, 1 Raid, Siedlung „Wurzelrast“ |
| Veröffentlichung | Monat 10 nach Launch | Monat 21 nach Launch |

### 4.1 Erzählung

**„Was die Tiefe singt“ (Erweiterung 1).** Nach dem Finale hören Fischerinnen und Fischer in Saltrand ein Lied aus der Tiefe, das älter klingt als das Weltlied selbst. Thal'assyr, die Gezeitenstimme, weist den Weg in den Thalgrund – eine Tiefsee mit Lichtwäldern aus leuchtenden Echos, versunkenen Siedlungen der Erstchor-Zeit und einer Strömung, die wie ein Atem kommt und geht. Die Geschichte erzählt, wie die Bewohnenden der Tiefe die Große Stille überstanden haben, ohne je von ihr betroffen zu sein – und was das über die Natur des Weltlieds verrät. Im Neuen Lied antworten die freien Stimmen dem Lied der Tiefe; in der Sanften Stille wacht Thal'assyr leise auf, um zuzuhören.

**„Wo die Wurzeln hören“ (Erweiterung 2).** Unter dem Uralthain, wo die Reise begann, öffnet sich der Wurzelgrund: Höhlen, in denen die Wurzeln der ältesten Bäume wie Saiten gespannt sind. Sylv'anor, die Blütenstimme, erinnert sich an eine Zeit vor den Stimmen. Die Erweiterung schließt den Kreis zum Prolog – zurück an den Ort der Erstresonanz, aber tiefer. Sie erzählt von Erinnerung und Wachstum und gibt Kael, Ilen und den Fraktionen einen gemeinsamen Abschluss.

### 4.2 Inhalte je Erweiterung

| Inhalt | Erweiterung 1 | Erweiterung 2 |
|---|---|---|
| Linien | 10 dreistufig, 3 zweistufig (36 Arten) | 8 dreistufig, 4 zweistufig, 2 ohne Evolution (34 Arten) |
| Typ-Schwerpunkte | Flut, Licht, Kristall, Klang (Tiefenlicht und Resonanz) | Blüte, Stein, Geist, Arkan (Wurzeln, Erinnerung) |
| Siedlung | Perlhall (Unterwasserkuppel, Händler, Werft für Tauchglocken) | Wurzelrast (Höhlendorf, Pilzgärten, Archiv der Wurzeln) |
| Endgame | Tiefenresonanz „Lichtloser Graben“, Raid „Gezeitenwal“ | Tiefenresonanz „Erste Wurzel“, Raid „Der Vergessene Ring“ |
| Fraktionen | Kontor und Wildwacht (Schutzgebiete der Tiefe) | Akademie und Orden (Archiv, Erinnerung) |
| Kodex | eigenes Kodex-Kapitel, Meisterschaft „Tiefenkodex“ | eigenes Kodex-Kapitel, Meisterschaft „Wurzelkodex“ |

**Regeln für Erweiterungen:**

- Neue Arten folgen den Katalogregeln (K16, Prüfer `gen_catalog.py`), erhalten Identitätsakzente (K63) und sind ohne Online erreichbar.
- Neue Typen gibt es nicht; die Typtabelle (K17) bleibt unverändert.
- Spielende ohne Erweiterung sehen Arten aus Erweiterungen im Tausch und im Koop (als Gäste ihrer Freunde), können sie aber nur mit der Erweiterung im eigenen Spiel nutzen; Ranked bleibt für alle mit dem Grundspiel-Pool fair, weil Erweiterungsarten erst nach einer Saison zugelassen werden.
- Der Kodex des Grundspiels bleibt bei 256 vollständig („Weltakkord vollendet“ ändert sich nicht, ADR-260); Erweiterungen haben eigene Kodex-Kapitel und Meisterschaften.

---

## 5. Monetarisierung

### 5.1 Modell (K01 §14, CANON §2)

| Element | Festlegung |
|---|---|
| Grundspiel | Premium, Vollpreis |
| Editionen | Standard; Deluxe (Artbook, Soundtrack, kosmetisches Wärter-Set, Expansion-Pass) |
| Expansion-Pass | 2 Story-Erweiterungen |
| Kostenlose Updates | Saisons, Events, Raids, Balancing, Komfort |
| Kosmetik-Shop | Wärter-Kleidung, Gleiter-Skins, Hain-Deko – feste Preise, kein Zufall |

### 5.2 Editionen

| Edition | Inhalt |
|---|---|
| Standard | Grundspiel |
| Deluxe | Grundspiel, Expansion-Pass (2 Erweiterungen), digitales Artbook, Soundtrack, kosmetisches Wärter-Set „Erste Stimme“ |
| Expansion-Pass einzeln | 2 Erweiterungen, Pass-Bonus: Gleiter-Muster „Tiefenlicht“ |
| Erweiterungen einzeln | je Erweiterung, ab ihrem Erscheinen |

Alle Editionen enthalten dasselbe Spiel; Deluxe bietet keine spielerischen Vorteile.

### 5.3 Kosmetik-Shop

| DisplayName | Category | Content | TypicalPriceEUR | PriceRangeEUR | AlsoEarnable |
|---|---|---|---|---|---|
| Wärter-Kleidung | Wärter-Kleidung | Kleidungssets je Kultur und Fest (je 6–8 Teile) | 9,99 | 4,99–14,99 | ja (Deluxe-Set, Feste, Fraktionsränge) |
| Gleiter-Muster | Gleiter-Skins | Muster und Stoffe für den Gleiter | 4,99 | 2,99–6,99 | ja (Taktproben, Sternfest, Ranked) |
| Hain-Deko | Hain-Deko | Möbel, Brunnen, Lichter, Pflanzen für den Resonanzhain | 4,99 | 1,99–9,99 | ja (Zirkel-Chronik, Endgame, Feste) |
| Lager-Stile | Wärter-Kleidung | Zelte, Lagerfeuer-Stile, Kochgeschirr | 4,99 | 2,99–6,99 | ja (Zirkel-Chronik) |
| Fotorahmen und Filter | Hain-Deko | Rahmen, Filter, Sticker für den Fotomodus | 2,99 | 1,99–4,99 | ja (Fotowettbewerbe) |

| Regel | Inhalt |
|---|---|
| Keine Zwischenwährung | Preise direkt in Landeswährung über den Plattform-Store; keine „Kristalle“, keine Restguthaben |
| Kein Zufall | Jeder Kauf zeigt genau, was man bekommt (Vorschau am eigenen Charakter und Hain) |
| Nichts mit Echos | Keine Morphs, Farben, Werte, Siegel, Echos (DR-17: Optik der Echos nur durch Genetik, Fundort, Leistung) |
| Auch erspielbar | Jede Kategorie hat vergleichbare Inhalte, die man spielerisch erreicht (Feste, Chronik, Ränge, Taktproben) |
| Kein Druck | Keine Countdown-Angebote, keine „nur heute“-Rabatte; Rotationen werden angekündigt |
| Kinder | Käufe nur über Plattform-Konten mit Elternkontrollen; keine Kaufaufforderungen im Spielverlauf, der Shop ist ein eigener Menüpunkt |
| Rückerstattung | nach Plattformregeln; Kennzahl Rückerstattungen < 1 % (§8) |

---

## 6. Live-Betrieb

| Bereich | Festlegung |
|---|---|
| Bereitschaft | Online-Dienste 24/7 (Rotation, Follow-the-Sun EU/NA/APAC, K59 §7); Bereitschaft mit Ausgleich (L-6) |
| Vorfälle | Schwere V1 (Online-Dienste ausgefallen) → Reaktion ≤ 15 min, Statusseite und Meldung im Spiel; V2 (eingeschränkt) ≤ 1 h; V3 (Einzelfehler) im Tagesbetrieb |
| Wartung | rollierend je Region, keine globalen Ausfälle; Ranked-Warteschlange schließt 15 min vorher (K59) |
| Hotfix | Build ≤ 24 h nach Entscheidung; Plattform-Schnellverfahren; Golden Saves und Datenprüfungen vor jedem Hotfix (K66) |
| Patches | Inhalt nach Plan (§2); Balance nur per Patch und Ranked nur zum Saisonwechsel (K61, K63) |
| Live-Konfiguration | Event-Kalender, Matchmaking-Parameter, Texte – ohne Patch; nie Kampf- oder Wirtschaftswerte (Daten-Hash, K59 §7.3) |
| Saisonwechsel | Weicher Wertungs-Reset, Belohnungen verteilt, Saisonregel aktiviert, Chronik-Ziele gewechselt – automatisiert, mit Probelauf auf der Staging-Umgebung |
| Daten | Telemetrie pseudonym, Dashboards für §8; monatliche Auswertung an Balance-Rat (K63) und Leadership |

**Hotfix-Ablauf:**

```
Vorfall erkannt (Telemetrie, Crash-Signatur, Meldungen) ─► Triage im Launch-Raum (≤ 2 h)
 ─► Entscheidung: Live-Konfiguration (sofort) | Server-Fix (≤ 4 h) | Client-Hotfix (Build ≤ 24 h)
 ─► Datenprüfungen + Golden Saves + betroffene Suiten (K66) ─► Plattform-Schnellverfahren
 ─► Veröffentlichung mit Patch-Notiz (Ursache, Wirkung, was wir daraus lernen)
```

**Live-Team nach Launch:** ≈ 45 Personen (Live-Produktion, Backend/DevOps, Community, QA Live, Balancing, Events) plus ≈ 80 Personen im Erweiterungsteam (aus den Content-Pods, K67 §4.2).

---

## 7. Gemeinschaft und Kommunikation

| Kanal | Inhalt | Rhythmus |
|---|---|---|
| Öffentlicher Fahrplan | Quartalsvorschau mit Zielen, ohne harte Termine für Inhalte, die noch nicht fertig sind | vierteljährlich |
| Patch-Notizen | Jede Änderung mit Begründung (K63 §9), Balance-Änderungen mit Daten | je Patch |
| Entwicklungs-Tagebuch | Hinter den Kulissen: Kreaturen-Design, Musik, Welt | monatlich |
| Fotowettbewerb | Gemeinschaftsthema, Auswahl im Spiel ausgestellt (Hain-Bilderrahmen) | monatlich |
| Turniere | Saisonturniere (Schweizer System, K61 §6), ab Saison 2 auch von Zirkeln ausgerichtet | je Saison |
| Kreativprogramm | Frühzugang zu Fotomodus-Funktionen, Leitfaden für Videos und Streams | laufend |
| Feedback | Umfragen im Spiel (opt-in), Foren, Barrierefreiheits-Rat mit Betroffenen | laufend |
| Moderation | Regeln für Namen, Fotos, Freitext (K59 §10, K60 §8) | laufend |

**Tonalität:** Die Kommunikation spricht wie die Welt – warm, staunend, ehrlich. Fehler werden benannt, nicht kleingeredet. Ankündigungen versprechen nur, was fertig oder sicher geplant ist.

---

## 8. Kennzahlen

| DisplayName | Target | Alarm | Action |
|---|---|---|---|
| Absturzrate je Sitzung | < 0,2 % | > 0,5 % an einem Tag | Hotfix-Bewertung innerhalb 24 h, Signatur-Triage |
| Verfügbarkeit Online-Dienste | ≥ 99,5 % je Monat | < 99 % in einer Woche | Ursachenanalyse, Kapazität prüfen |
| Ranked-Wartezeit Median | ≤ 45 s | > 90 s in einer Region | Wertungsfenster, Nachbarregion, Saisonregel |
| Aktive je Woche (Anteil an Käufern, Monat 3) | ≥ 25 % | < 15 % | Inhaltsplan prüfen, nicht Druck erhöhen |
| Story-Abschlussrate (12 Monate) | ≥ 45 % | < 35 % | Schwierigkeit/Onboarding prüfen (K63) |
| Online-Funktion in 30 Tagen genutzt | ≥ 35 % | < 25 % | Sichtbarkeit Koop/Tausch, Fehler prüfen |
| Meldungen je 1.000 Sitzungen | ≤ 2 | > 5 | Moderation, Schnellchat-Sätze prüfen |
| Nutzerbewertungen (gleitend 30 Tage) | ≥ 85 % positiv | < 75 % | Themen clustern, Patch-Plan anpassen |
| Expansion-Pass-Anteil (12 Monate) | ≥ 25 % | – | Erweiterungsinhalte, keine Druckmechanik |
| Rückerstattungen Shop | < 1 % | > 3 % | Darstellung der Shop-Inhalte prüfen |

Die Handlungen bei Alarm verbessern immer das Spiel (Inhalte, Fehler, Klarheit) – nie werden Druckmechaniken eingeführt, um Kennzahlen zu heben (LO-07, L-1). Die Business-Ziele aus K01 §18 (4,5 Mio. verkaufte Einheiten in 12 Monaten, Wertungen ≥ 85, Expansion-Pass-Anteil ≥ 25 %) werden monatlich verfolgt.

---

## 9. Langfristig: Jahr 3 und das Ende der Server

Nach den zwei Erweiterungen (Monat 24) wechselt AETHRIS in einen ruhigeren Betrieb: Saisons und Events laufen weiter, Balance-Patches werden seltener, das Team konzentriert sich auf künftige Projekte. Für den Tag, an dem Online-Dienste enden, gilt von Anfang an:

| Funktion | Nach dem Ende der Online-Dienste |
|---|---|
| Weltspiel, Story, Kodex, Endgame | vollständig spielbar (NZ-1, DR-19) |
| Koop | lokal weiterhin möglich (Split-Screen, lokales Funk-Koop, K65); Online-Koop über Plattform-Direktverbindung, solange die Plattform sie anbietet |
| Raids | Solo-Varianten (CANON §129) |
| PvP | Geister-Teams (letzter Stand) und lokale Freundeskämpfe |
| Tausch | entfällt; keine Art ist tausch-exklusiv (DR-19) |
| Events | ein abschließendes Update schaltet alle Event-Kosmetik und Resonanzsturm-Nächte offline frei (Sturmstimmgabel ohne Abklingzeit-Grenze für Event-Inhalte) |
| Cross-Save | letzter Export als Datei auf das Gerät (Import auf allen Plattformen, die das Spiel weiter anbieten) |

Die Ankündigung erfolgt mindestens zwölf Monate vorher. Damit bleibt AETHRIS spielbar, solange es Geräte gibt, auf denen es läuft.

---

## 10. Prüfregeln

`tools/ref/aethris_liveops.py validate`:

| Regel | Inhalt |
|---|---|
| LO-01 | Höchstens 3 zeitlich begrenzte Events gleichzeitig |
| LO-02 | Spielinhalte von Events auch offline erreichbar |
| LO-03 | Event-Belohnungen nur kosmetisch/Kodex |
| LO-04 | Shop nur in erlaubten Kategorien, keine verbotenen Inhalte, auch erspielbar |
| LO-05 | Erweiterungen je 30–40 Echos, Kodex-Nummern lückenlos ab #257 |
| LO-06 | Jahr 1: Update oder Saison mindestens alle 3 Monate |
| LO-07 | Kennzahlen mit Alarm und Handlung, ohne Druckmechaniken |

**Ergebnis:** Prüfregeln LO-01–LO-07: **0 Verstöße**. 10 Events (höchstens 3 gleichzeitig), 11 Releases in 24 Monaten, 5 Shop-Kategorien (nur Kosmetik, feste Preise), Erweiterungen: 2.0 36 Echos (#257–#292), 3.0 34 Echos (#293–#326).

---

## 11. Abschluss des Kapitelsystems

Mit diesem Kapitel ist die Spezifikation von AETHRIS: Echobound vollständig: 68 Kapitel von der Executive Summary bis zum Live-Betrieb. Das Kapitelsystem ist kein Stapel Dokumente, sondern ein überprüfbares Ganzes:

| Bestandteil | Umfang |
|---|---|
| Kapitel | 68 (K01–K68), jedes mit Checkliste, Decision Records und Kanon-Änderungen |
| Kanon | `docs/CANON.md` mit allen LOCKED-Festlegungen, ADRs, Change Requests und geschlossenen offenen Fragen |
| Daten | `Data/**/*.csv` als Quelle der Wahrheit (Echos, Fähigkeiten, Items, Quests, NPCs, Welt, Audio, Art, VFX, Online, PvP, Endgame, Balancing, Save, Performance, QA, Produktion, LiveOps) |
| Werkzeuge | Generatoren und Referenzmodelle in `tools/`, Kapitel aus Vorlagen erzeugt (`tools/authoring/`) |
| Code-Gerüst | UE-5.6-Module mit Schichtenregel (`Source/`, `Plugins/GameFeatures/`), erste Automation Specs |
| Prüfungen | Register mit allen Datenprüfungen (`Data/QA/Checks.csv`) |

### 11.1 Alle Kapitel

| Kapitel | Titel | Owner | Wörter |
|---|---|---|---|
| K01 | Executive Summary | Game Director | 7.253 |
| K02 | GDD I – Design-Säulen, Spielerfantasie, Core Loops | Game Director, Creative Director | 7.244 |
| K03 | GDD II – Spielstruktur, Progression, Feature-Matrix | Game Director, RPG Systems Designer | 4.336 |
| K04 | Kanon, Glossar, Namens- & ID-Konventionen | Creative Director, Narrative Writer | 4.694 |
| K05 | TDD I – Engine-Setup, Modul- & Projektstruktur, Coding Standards | Unreal Senior Dev, Lead Gameplay Programmer | 3.583 |
| K06 | TDD II – Core-Framework: Data-Driven, Event-Bus, State Machines, GAS, Save-Architektur | Lead Gameplay Programmer | 3.420 |
| K07 | World Bible I – Kosmologie, Weltlied, Geschichte | Creative Director, Narrative Writer | 4.998 |
| K08 | Weltgeographie & Makro-Layout (36 km²) | Level Designer | 4.030 |
| K09 | Biome I – Verdanthain, Kharsgrat, Morvenmoor, Sahrun-Weite, Ignareth | Level Designer, Technical Artist | 5.011 |
| K10 | Biome II – Saltrand, Hvitfell, Ael'Dorun, Prismtiefen, Nimbara | Level Designer, Technical Artist | 4.044 |
| K11 | Städte I (5 Städte) | Level Designer, Narrative Writer | 5.024 |
| K12 | Städte II (5 Städte) | Level Designer, Narrative Writer | 4.382 |
| K13 | Dörfer & Außenposten | Level Designer, Quest Designer | 3.822 |
| K14 | Wettersystem | Technical Artist, Gameplay Programmer | 3.984 |
| K15 | Tageszyklus & Beleuchtung | Technical Artist | 3.130 |
| K16 | Monster Bible I – Designregeln, Taxonomie, Datenschema | Creative Director, RPG Systems Designer | 4.265 |
| K17 | Typensystem & Effektivitätstabelle | Combat Designer | 3.590 |
| K18 | Statuswerte, Persönlichkeit, Temperament, Wachstumsraten | RPG Systems Designer | 3.017 |
| K19 | Evolutionssystem | RPG Systems Designer | 3.018 |
| K20 | Kreaturenkatalog 1 (#001–#032) | Creature Team | 9.829 |
| K21 | Kreaturenkatalog 2 (#033–#064) | Creature Team | 9.339 |
| K22 | Kreaturenkatalog 3 (#065–#096) | Creature Team | 9.368 |
| K23 | Kreaturenkatalog 4 (#097–#128) | Creature Team | 9.480 |
| K24 | Kreaturenkatalog 5 (#129–#160) | Creature Team | 9.440 |
| K25 | Kreaturenkatalog 6 (#161–#192) | Creature Team | 9.629 |
| K26 | Kreaturenkatalog 7 (#193–#224) | Creature Team | 9.490 |
| K27 | Kreaturenkatalog 8 (#225–#256, inkl. Legendäre) | Creature Team | 9.981 |
| K28 | Fähigkeiten I – System, Datenschema, Passive | Combat Designer | 9.956 |
| K29 | Fähigkeiten II – Aktive Fähigkeiten | Combat Designer | 7.639 |
| K30 | Fähigkeiten III – Ultimates & Feldfähigkeiten | Combat Designer | 8.630 |
| K31 | Kampfsystem I – Resonanz-Zeitleiste, Initiative, Priorität | Combat Designer, Lead Gameplay Programmer | 4.977 |
| K32 | Kampfsystem II – Schadensformel, Status, Terrain, Wetter | Combat Designer | 4.790 |
| K33 | Kampfsystem III – Positionierung, Combos, Synergien, Formate | Combat Designer | 4.840 |
| K34 | Kampf-KI (Trainer & Wild) | AI Engineer | 4.376 |
| K35 | Raids | Combat Designer, Network Engineer | 4.269 |
| K36 | Fangsystem (Resonanzbindung) | Lead Gameplay Programmer, RPG Systems Designer | 6.330 |
| K37 | Begleitersystem | RPG Systems Designer, Animation | 4.072 |
| K38 | Zucht & Genetik | RPG Systems Designer | 3.779 |
| K39 | Forschung, Echo-Kodex & Fotografie | RPG Systems Designer, UI/UX | 5.590 |
| K40 | Ausrüstung, Reittiere & Traversal | Gameplay Programmer, Level Designer | 4.786 |
| K41 | Ressourcen & Crafting | Economy Designer | 5.125 |
| K42 | Wirtschaft | Economy Designer | 7.060 |
| K43 | Skilltree & Spielerprogression | RPG Systems Designer | 3.292 |
| K44 | Story Akt I | Narrative Writer | 5.078 |
| K45 | Story Akt II | Narrative Writer | 6.695 |
| K46 | Story Akt III & Finale | Narrative Writer | 6.531 |
| K47 | Fraktionen & Rufsystem | Narrative Writer, Quest Designer | 5.169 |
| K48 | Quest Bible & Questsystem-Technik | Quest Designer, Gameplay Programmer | 7.493 |
| K49 | Nebenquests 1 (#SQ001–#SQ070) | Quest Designer | 15.056 |
| K50 | Nebenquests 2 (#SQ071–#SQ140) | Quest Designer | 13.754 |
| K51 | Nebenquests 3 (#SQ141–#SQ210) | Quest Designer | 14.460 |
| K52 | Monster-Ökologie & Schwarm-KI | AI Engineer | 5.592 |
| K53 | NPC-KI (Tagesabläufe, Reaktionen, Gruppen) | AI Engineer | 5.744 |
| K54 | UI/UX | UI/UX Designer | 5.272 |
| K55 | Audio Bible | Sound Designer | 5.164 |
| K56 | Art Bible | Creative Director, Technical Artist | 5.814 |
| K57 | Asset Pipeline, Animation & Technical Art | Technical Artist | 7.169 |
| K58 | VFX | Technical Artist | 6.101 |
| K59 | Multiplayer-Architektur | Network Engineer | 6.071 |
| K60 | Koop, Tausch, Gilden | Network Engineer, Game Director | 5.324 |
| K61 | PvP & Ranked | Combat Designer, Network Engineer | 5.055 |
| K62 | Endgame | Game Director | 5.026 |
| K63 | Balancing-Mathematik | RPG Systems Designer, Economy Designer | 6.104 |
| K64 | Save-System (Autosave, Cloud, Versionierung) | Lead Gameplay Programmer | 5.022 |
| K65 | Performance & Plattformen | Unreal Senior Dev | 5.014 |
| K66 | QA-Strategie | QA Lead | 5.260 |
| K67 | Produktions-Roadmap (Phase 1–6) | Game Director, Producer | 5.002 |
| K68 | LiveOps, Updates & Post-Launch | Game Director | 5.213 |
| **Σ** | **68 Kapitel** | | **417.095** |

**Stand aller Datenprüfungen beim Abschluss:** **24 von 24 Prüfungen grün**; Laufzeit gesamt 34 s (davon PreSubmit 1 s).

Alle offenen Kernfragen sind geschlossen (Q1–Q15). Änderungen ab jetzt laufen über den Change-Request-Prozess (CANON §11, K67 §7.2): Daten ändern, Prüfer laufen lassen, betroffene Kapitel neu erzeugen, Kanon fortschreiben.

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-291 | Events kehren wieder, haben Offline-Wege und nur kosmetische Belohnungen | DR-19, DR-23, kein FOMO | exklusive Event-Inhalte |
| ADR-292 | Kein bezahlter Saison-Pass; Saisons kostenlos | K01 §14.2, Fairness | Battle Pass |
| ADR-293 | Shop ohne Zwischenwährung mit festen Preisen und Vorschau | Transparenz, Kinder- und Verbraucherschutz | Premium-Währung, Bundles mit Restguthaben |
| ADR-294 | Erweiterungen mit neuen Regionen (R11 Thalgrund, R12 Wurzelgrund) und 36/34 Echos; Grundspiel-Kodex bleibt bei 256 | Vollständigkeit des Grundspiels, klare Ziele | Erweiterungsarten im Grundspiel-Kodex |
| ADR-295 | Kennzahlen-Alarme führen nie zu Druckmechaniken | L-1, Vertrauen | Engagement-Optimierung um jeden Preis |
| ADR-296 | Plan für das Ende der Online-Dienste ab Launch: alles Wesentliche offline weiter spielbar | Langlebigkeit, Respekt | Spiel endet mit den Servern |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §268 | Live-Säulen L-1–L-6; Fahrplan (`ReleasePlan.csv`): Day-One-Patch, Updates/Saisons mindestens alle 3 Monate, RAID_09/RAID_10 kostenlos, Erweiterungen Monat 10 und 21 | LOCKED |
| §269 | Events (`Events.csv`, 10 wiederkehrend, max. 3 gleichzeitig, Ankündigung ≥ 14 Tage, Offline-Wege, kosmetische Belohnungen), Jahreskalender, Saisons ohne bezahlten Pass | LOCKED |
| §270 | Erweiterungen: R11 Thalgrund (36 Echos #257–#292, Tauchen), R12 Wurzelgrund (34 Echos #293–#326, Graben), je Story ≈ 12 h, 25 Nebenquests, 1 Tiefe, 1 Raid; Erweiterungsarten nach einer Saison Ranked-zulässig; Grundspiel-Kodex bleibt 256. Monetarisierung: Shop (`ShopCatalog.csv`) nur Wärter-Kleidung/Gleiter/Hain-Deko, feste Preise in Landeswährung, kein Zufall, auch erspielbar | LOCKED |
| §271 | Live-Betrieb (24/7, Vorfallstufen, Hotfix ≤ 24 h, Live-Konfiguration ohne Kampf-/Wirtschaftswerte), Gemeinschaft (Fahrplan, Patch-Notizen mit Begründung, Turniere, Fotowettbewerbe), Kennzahlen (`LiveKPIs.csv`), Ende der Online-Dienste mit Offline-Ersatz und 12 Monaten Vorankündigung | LOCKED |
| §10 | ADR-291 – ADR-296 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Live-Säulen L-1–L-6
- [x] Post-Launch-Fahrplan über 24 Monate
- [x] Events mit Regeln und berechnetem Jahreskalender, Saisons
- [x] Zwei Erweiterungen mit Regionen, Mechaniken, Echo-Zahlen und Kodex-Bereichen
- [x] Monetarisierung (Premium, Expansion-Pass, Kosmetik-Shop ohne Zufall und Zwischenwährung)
- [x] Live-Betrieb, Gemeinschaft, Kennzahlen, Ende der Server
- [x] Prüfregeln LO-01–LO-07 (0 Verstöße), Stand aller Datenprüfungen
- [x] ADR-291 – ADR-296, CANON §268–§271
- [x] Kapitelsystem K01–K68 abgeschlossen

✅ **Das Kapitelsystem AETHRIS: Echobound ist vollständig (K01–K68).**
