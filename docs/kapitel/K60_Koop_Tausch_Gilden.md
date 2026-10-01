# K60 · Koop, Tausch und Gilden

| Feld | Wert |
|---|---|
| Dokument | Kapitel 60 von 68 · Online II |
| Version | 1.0 |
| Owner | Lead Online Designer, Game Director |
| Mitwirkende | Systems Designer, Narrative Director (Q4), UX Lead, Backend Engineer (Tausch, Zirkel), Community Manager, Accessibility Lead, Datenschutzbeauftragte Person |
| Baut auf | K02 (DR-19, DR-20, Säule S5), K03 (Koop-Reise, Tauschhalle, Gehorsam CANON §18), K33 §10 (Koop-Kampf), K36 (Koop-Bindung), K37 (Hain, Chor-Tausch), K38 §10 (Fernklang, Plausibilität), K39 (Kodex, Foto), K41/K42 (eigene Knoten, Tausch-Grundregeln ADR-156), K43 §8 (Skills im Koop), K59 (Architektur, Gast-Protokoll, Legalität, Schnellchat) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Online/CoopRewards.csv` (Q4), `TradeRules.csv` (TR-01–TR-15), `GuildRoles.csv`, `GuildGoals.csv`, `QuickChat.csv`; Referenzmodell `tools/ref/aethris_social.py` (SO-01–SO-07, Klangbörse mit Ring-Tausch); `GF_Multiplayer/…/Trade/AethrisTradeTypes.h/.cpp` |
| Neue Kanon-Einträge | CANON §236 (Koop-Reise), §237 (Q4 Story im Koop), §238 (Tausch und Klangbörse), §239 (Klangzirkel, Freunde, Kommunikation); Q4 geschlossen |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Koop-Reise](#2-koop-reise)
3. [Story im Koop – Entscheidung Q4](#3-story-im-koop--entscheidung-q4)
4. [Tausch](#4-tausch)
5. [Klangzirkel (Gilden)](#5-klangzirkel-gilden)
6. [Freunde, Grüße, Hain-Besuche](#6-freunde-grüße-hain-besuche)
7. [Kommunikation](#7-kommunikation)
8. [Sicherheit, Kinder, Moderation](#8-sicherheit-kinder-moderation)
9. [UX-Abläufe](#9-ux-abläufe)
10. [Technik](#10-technik)
11. [Telemetrie und Ziele](#11-telemetrie-und-ziele)
12. [Prüfregeln](#12-prüfregeln)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Ziele

Säule S5 (K02) lautet sinngemäß: *Gemeinsam klingt die Welt voller.* Die sozialen Funktionen sollen Freundschaften im Spiel tragen, ohne dass jemand, der allein spielt, etwas verpasst. Drei Leitfragen prüfen jede Regel in diesem Kapitel:

| Leitfrage | Herkunft | Konsequenz |
|---|---|---|
| Kann eine Person allein 100 % erreichen? | DR-19 | Keine tausch-exklusiven Arten, keine Koop-Pflicht; Prüfregel SO-01 belegt einen Solo-Zugang für alle 256 Arten |
| Ist der Koop-Vorteil sozial, kosmetisch oder Zeitersparnis – aber nie Macht? | DR-20 | Keine Werte-Boni in Zirkeln, keine stärkeren Echos im Koop, Zirkel-Belohnungen nur kosmetisch (SO-05) |
| Ist das Miteinander sicher? | K59 §10 | Schnellchat als Standard, Tausch mit Fremden nur über die Klangbörse ohne Chat, Elternkontrollen respektiert |

Die sozialen Funktionen sind bewusst **klein und warm** statt groß und kompetitiv: Es gibt keinen Spielermarkt (ADR-156), keinen Sol-Handel, keine Gildenkriege. Es gibt Reisen zu zweit bis viert, Tausche, die sich wie ein Geschenk anfühlen, und Zirkel, die gemeinsam etwas Schönes sammeln.

---

## 2. Koop-Reise

### 2.1 Ablauf

```
Host am Resonanzstein: „Chor öffnen“ ─► Einladung (Freund, Zirkel, Plattform) oder offene Sitzung für Freunde
Gast: „Beitreten“ ─► eigener Stand gesichert ─► erscheint am Host oder am nächsten Resonanzstein der Host-Welt
Gemeinsam: erkunden, kämpfen, binden, reiten, sammeln, kochen, fotografieren
Ende: „Chor schließen“ (Host) oder „Heimkehren“ (Gast) ─► Gast-Protokoll wird in der eigenen Welt angewendet
```

Koop ist ab dem Ende des Prologs verfügbar (Wärterrang 1, K59 §2). Der Prolog bleibt ein Solo-Erlebnis, weil er die Beziehung zwischen Spielfigur, erstem Echo und Welt stiftet.

### 2.2 Kampf

Der Koop-Kampf folgt K33 §10. Die Spielerzahl bestimmt das Format; Wildgegner skalieren mit (HP-Faktor wie beim Raid: 700 ‰ je zusätzlichem Spieler, CANON §129):

| Spieler | Kampfformat (Spielerseite) | Wildbegegnung | HP-Faktor Alpha/Wärter/Boss | EP/Sol je Spieler | Zugtimer |
|---|---|---|---|---|---|
| 1 | Solo (Duell/Duo/Trio nach Rang) | Herde mit 1 Echo oder Einzel-Alpha | ×1,0 | 100 % (eigene Echos) | – |
| 2 | Duo (2 × 1 aktiv) | Herde mit 2 Echos oder Einzel-Alpha | ×1,7 | 100 % (eigene Echos) | 30 s (Option 60 s) |
| 3 | Trio (3 × 1 aktiv) | Herde mit 3 Echos oder Einzel-Alpha | ×2,4 | 100 % (eigene Echos) | 30 s (Option 60 s) |
| 4 | Quartett (Raid-Formation, 4 × 1 aktiv) | Herde mit 4 Echos oder Einzel-Alpha | ×3,1 | 100 % (eigene Echos) | 30 s (Option 60 s) |

| Regel | Festlegung |
|---|---|
| Harmonie | gemeinsam für die Spielerseite; Kombos zwischen Echos verschiedener Spieler ausdrücklich gewollt |
| Akkorde | je Spieler-Chor getrennt (K33) |
| Skills | jeder nutzt eigene; Harmonieführung zählt einmal je Seite (höchster Wert, K43 §8) |
| Belohnung | jeder erhält volle EP/Sol für seine Echos; keine Teilung, kein Wegschnappen |
| Zugtimer | 30 s, Option „entspannt“ 60 s; läuft nur, wenn jemand wartet (K59 §5.3) |
| Wer kämpft | Kämpfe beginnen pro Spieler-Kreis (CANON §17); andere können in Reichweite (25 m) beitreten, solange die erste Runde nicht beendet ist |
| Niederlage | Rückklang für die betroffene Person (CANON Grade), andere kämpfen weiter |

### 2.3 Einklang-Modus (optional)

Freunde mit sehr unterschiedlichem Fortschritt sollen trotzdem gemeinsam spielen können. Der Host kann den **Einklang-Modus** aktivieren: Echos aller Gäste werden für Kämpfe auf das Zonenband der Host-Welt + 5 Level gedeckelt (Werte nach der Levelformel K18 neu berechnet, Fähigkeiten bleiben). Das schützt die Herausforderung der Host-Welt, ohne Gäste zu bestrafen; EP richten sich wie immer nach dem Gegnerlevel. Ohne Einklang-Modus kämpfen alle mit ihren echten Leveln – Hilfe durch erfahrene Freunde ist erlaubt (Zeitersparnis, DR-20).

### 2.4 Bindung, Reiten, Sammeln

| Bereich | Regel |
|---|---|
| Bindung | Bindet, wer „Binden“ wählt; andere tragen Köder/Fallen und Kampfvorbereitung bei (zählen für die Resonanz, K36); Ursprung vermerkt den Koop-Partner (DR-16) |
| Nicht bindbar für Gäste | Ursprungsstimmen, Mythische, Stille-Echos – Gäste können mitkämpfen, gebunden wird nur in der eigenen Welt (CoopRewards `CR_BOND`) |
| Reiten | Mitreiten auf XL/XXL-Reittieren (Sozialfunktion, kein Tempo-Vorteil, K40) |
| Ressourcen | eigene Knoten je Spieler (K41); Geschenke bis 50 Stück/Tag (K42) |
| Kochen, Lager | Gemeinsames Lager: Gerichte, die eine Person kocht, wirken für alle Anwesenden (Zeitersparnis) |
| Fotos | Mitspielende erscheinen in Fotos, wenn ihre Profil-Einstellung das erlaubt (Standard: Freunde ja, andere nein) |
| Weltzeit | läuft im Koop (nie pausiert, UX-04); die eigene Welt eines Gastes steht still |

### 2.5 Abstand, Zwischensequenzen, Feste

Spielende dürfen sich frei bewegen (bis zu vier Streaming-Gebiete, K59 §4.2). Zwischensequenzen der Host-Welt holen alle zusammen: Ein Abstimmungs-Dialog („Szene ansehen?“) wartet höchstens 30 s; wer ablehnt, wartet in einem Ruhebereich und sieht eine Zusammenfassung. Siedlungsfeste (K13) sind für alle sichtbar und eine der besten Koop-Gelegenheiten (Tänze, Fest-Gesten, gemeinsame Fotos).

---

## 3. Story im Koop – Entscheidung Q4

**Frage (Q4):** Teilen Koop-Partner den Story-Fortschritt?

### 3.1 Optionen

| Option | Beschreibung | Vorteile | Nachteile |
|---|---|---|---|
| A Geteilt | Gäste erhalten Hauptquest-Fortschritt der Host-Welt | gemeinsames Durchspielen | bricht eigene Entscheidungen (Haltungen, Fraktionen, Finale K46), Story-Flags kollidieren, eigene Welt springt über Inhalte |
| B Gespiegelt | Gäste erhalten Fortschritt nur, wenn sie am gleichen Schritt stehen | fair für „Paare“, die gemeinsam spielen | selten erfüllt, erzwingt Absprachen, komplexe Sonderfälle |
| **C Persönlich + Erinnerung** | Story bleibt in jeder Welt persönlich; Gäste erhalten Erinnerungen (Tagebuch-Erinnerung „Gemeinsam erlebt“), Kodex, EP, Sol, Beute; Nebenquests als Mithilfe | Entscheidungen bleiben eigen, keine Konflikte, Koop belohnt trotzdem | Paare müssen Story-Momente doppelt erleben, wenn beide Fortschritt wollen |

### 3.2 Entscheidung: Option C

**Story-Fortschritt ist persönlich.** Hauptquests, Story-Flags und Entscheidungen werden nie aus einer fremden Welt übernommen. Begründung: AETHRIS erzählt eine Geschichte mit Haltungen (FS_STANCE, KAEL_TRUST, SERETH_RESPECT), Fraktionsentscheidungen und zwei Enden (K46). Diese Entscheidungen sollen jeder Person gehören.

Damit Koop sich trotzdem lohnt, gilt:

| Kind | GuestGets | Limit | Ledger | Rationale |
|---|---|---|---|---|
| Erfahrung (Echos, Wärter-EP) | voll für eigene Echos und Rang | – | Experience | DR-20: Zeitersparnis erlaubt |
| Sol aus Kämpfen und Kisten | voll (eigene Beute) | – | Sol | Beute je Spieler, keine Konkurrenz |
| Gegenstände, Ressourcen | voll (eigene Knoten, eigene Beute) | – | Item | K41: eigene Knoten je Spieler |
| Gebundene Wildechos | ja, mit Ursprung „Koop-Welt“ + Partner im Ursprung (DR-16) | nicht: Ursprungsstimmen, Mythische, Stille-Echos | Echo | Bindung ist eigene Leistung; Story-Legendäre gehören zur eigenen Geschichte |
| Kodex-Forschung (Beobachten, Kämpfen, Foto) | voll | – | KodexEntry | Sammeln zusammen macht Spaß |
| Nebenquests der Host-Welt | Mithilfe: 50 % EP/Sol des Abschlusses, kein Questfortschritt in der eigenen Welt | Quest-Belohnungsgegenstände nur für Host | Experience|Sol | Eigene Welt behält eigene Geschichten (Q4) |
| Hauptquest-Schritte und Story-Flags | kein Fortschritt; Tagebuch-Erinnerung „Gemeinsam erlebt“ | – | – | Q4: Entscheidungen bleiben persönlich (Finale K46) |
| Fraktionsruf | nur aus Fraktionsquests, die der Gast in der eigenen Welt aktiv hat (gleicher Schritt) – dann Abschluss in beiden Welten | max. 1 Kettenschritt je Sitzung | Reputation | Keine Abkürzung durch fremde Ruf-Stände |
| Tagebuch-Erinnerung „Gemeinsam erlebt“ | Name des Host, Ort, Moment (Zwischensequenz, Boss, Fest) | – | Memory | Erinnerung statt Fortschritt |
| Fotos | voll, mit Mitspielenden im Bild (Zustimmung über Profil-Einstellung) | – | Photo | K39 Fotomodus |
| Weltzeit der eigenen Welt | steht still, solange der Gast in fremder Welt ist | – | – | Zucht/Crafting laufen in Spielzeit der eigenen Welt (K02 §13) |

**Für Paare, die gemeinsam durchspielen wollen,** gibt es den **Gleichklang**: Stehen Host und Gast am **gleichen Hauptquest-Schritt** (gleiche `StepId`), bietet das Spiel beim Abschluss beiden an, den Schritt in beiden Welten zu verbuchen. Die Entscheidungsdialoge (Haltungen) trifft jede Person dabei selbst – der Dialog erscheint bei beiden, jede Antwort gilt für die eigene Welt. Das ist kein geteilter Fortschritt, sondern ein **parallel gespielter**. Ausgenommen sind die Finalentscheidung (K46) und Bosskämpfe mit Story-Abschluss, die jede Person in der eigenen Welt erlebt (dort ist Koop ohnehin gesperrt, K59 §6.2).

**Spoiler-Schutz:** Betritt ein Gast eine Story-Szene, die in der eigenen Welt noch nicht erlebt ist, fragt das Spiel: „Diese Szene liegt in deiner Geschichte noch vor dir. Ansehen oder warten?“ Standard: warten.

---

## 4. Tausch

### 4.1 Grundsätze

Tausch in AETHRIS ist **Echo gegen Echo**. Es gibt keinen Preis, keine Auktion, keinen Sol-Handel (ADR-156). Ein Tausch soll sich anfühlen wie das Weitergeben eines Freundes an jemanden, der ihn schätzen wird – deshalb die Abschiedsmomente und die bleibende Herkunft.

| Name | Scope | Rule | Value |
|---|---|---|---|
| TR-01 | DIRECT|BOARD | Getauscht werden Echos gegen Echos (1–3 je Seite) und Gegenstände aus der Tauschliste; Sol ist nie tauschbar | 1–3 Echos, ≤ 20 Gegenstände je Tausch |
| TR-02 | DIRECT|BOARD | Nicht tauschbar: Ursprungsstimmen, Mythische, Leih-Echos, Echos im aktiven Chor eines laufenden Kampfes | 16 Arten gesperrt |
| TR-03 | DIRECT|BOARD | Legalitätsprüfung + Signatur vor jedem Tausch (K59 §9.3) | 100 % |
| TR-04 | DIRECT|BOARD | Treuhand: beide Seiten bestätigen nach Ansicht (Halten 3 s); Abschluss atomar, sonst Rückgabe | Zweiphasen |
| TR-05 | DIRECT|BOARD | Frisch getauschte Echos sind 24 h (Echtzeit) nicht erneut tauschbar | 24 h |
| TR-06 | DIRECT | Direkttausch nur mit Freunden, Zirkelmitgliedern, aktuellen Koop-Partnern oder per Tauschcode (Begegnung in der Tauschhalle) | 30 Tausche/Tag |
| TR-07 | BOARD | Klangbörse: Angebot (Echo) + Wunsch (Art, optional Mindestlevel/Geschlecht-unabhängig/Morph); Server sucht passende Gegenangebote | 3 aktive Angebote, 5 Abschlüsse/Tag, Laufzeit 72 h |
| TR-08 | DIRECT|BOARD | Neue Wärterin/neuer Wärter: Bindung startet bei 0 (Vorsichtig), Gehorsamsregel gilt (+40 % Zeitkosten über Grenze) | Bindung 0 |
| TR-09 | DIRECT|BOARD | Ursprung bleibt (Erstwärter, Ort, Zeit); Herkunftstitel nur für Erstwärter | – |
| TR-10 | DIRECT|BOARD | Fernklang: Herkunftsregion ≥ 3 Regionen vom Heimatgarten des Empfängers → Morph-Faktor ×3 in der Zucht | ×3 |
| TR-11 | DIRECT|BOARD | Keine Tauschevolutionen; Tausch verändert kein Echo | – |
| TR-12 | DIRECT|BOARD | Kodex: getauschte Art erhält Forschungsstufen wie bei eigener Bindung außer dem Merkmal „selbst gebunden“ | – |
| TR-13 | DIRECT|BOARD | Abschied: Bei Bindungsstufe ≥ Seelenklang (750) zeigt das Spiel einen Abschiedsmoment; Erinnerung bleibt im Kodex | – |
| TR-14 | BOARD | Altersgerechte Einstellungen: Klangbörse nur, wenn Online-Interaktion mit Fremden erlaubt (Plattform-Elternkontrolle) | – |
| TR-15 | DIRECT|BOARD | Online-Funktionen nutzen nur den aktuell geladenen Weltstand (keine weltübergreifende Duplikation) | – |

### 4.2 Zwei Wege

| Weg | Für wen | Ablauf | Kommunikation |
|---|---|---|---|
| **Direkttausch** | Freunde, Zirkel, Koop-Partner, oder Begegnung in der Tauschhalle per Tauschcode (6 Zeichen) | beide stellen zusammen, sehen alles, halten 3 s zum Bestätigen | Schnellchat, Gesten; Freitext nur mit Freunden/Zirkel (opt-in) |
| **Klangbörse** | alle (außer bei Elternkontrolle) | Angebot (ein Echo) + Wunschliste (bis 3 Arten, optional Mindestlevel, Morph); Server sucht Gegenangebote und **Ring-Tausche**; beide/alle bestätigen | keine (anonym, Wärtername sichtbar) |

### 4.3 Klangbörse und Ring-Tausch

Ein reiner 1:1-Abgleich findet für seltene Wünsche oft keinen Partner: Wer ein häufiges Echo anbietet und ein seltenes sucht, trifft selten jemanden, der genau das Umgekehrte will. Die Klangbörse sucht deshalb zusätzlich **Ringe aus drei Angeboten** (A gibt an B, B an C, C an A). Die Referenzsimulation (`aethris_social.py board`, deterministische Saat, Angebote nach Häufigkeit gewichtet, Wünsche nach Seltenheit, Wunschliste mit bis zu 3 Arten) zeigt den Effekt:

| Angebote | 2er-Tausche | erfüllt (nur 2er) | + 3er-Ringe | erfüllt (2er + 3er) |
|---|---|---|---|---|
| 1000 | 28 | 56 (6 %) | 68 | 260 (26 %) |
| 5000 | 601 | 1202 (24 %) | 410 | 2432 (49 %) |
| 20000 | 4273 | 8546 (43 %) | 827 | 11027 (55 %) |

Ring-Tausche verdoppeln die Erfolgsquote bei mittlerem Angebot. Bei großem Angebot tragen 2er-Tausche den Großteil; die Ringe helfen vor allem in den ersten Tagen nach dem Launch und in kleineren Regionen. Größere Ringe (≥ 4) bringen kaum zusätzliche Treffer, erhöhen aber das Abbruchrisiko (jede Person muss bestätigen) – deshalb ist die Grenze 3.

```
Klangbörse – Abgleich (alle 5 min je Region, gierig, älteste Angebote zuerst):
  für jedes offene Angebot o (nach Alter):
      suche p mit p.hat ∈ o.wünsche und o.hat ∈ p.wünsche           → 2er-Tausch (beide reservieren)
  für jedes noch offene Angebot o:
      suche p, q mit p.hat ∈ o.wünsche, q.hat ∈ p.wünsche, o.hat ∈ q.wünsche → 3er-Ring
  reservierte Angebote → Benachrichtigung „Ein Tausch wartet“ (Bestätigen 24 h, sonst zurück in die Börse)
```

Alle Teilnehmenden sehen vor dem Bestätigen das Echo, das sie erhalten (Art, Level, Ursprung, Bindungsstufe 0 ab Tausch), nicht aber, wohin ihr eigenes Echo geht (außer bei 2er-Tauschen den Wärternamen).

### 4.4 Tauschliste der Gegenstände

Neben Echos sind bis zu 20 Gegenstände je Seite erlaubt – ausschließlich **Ressourcen, Gerichte und Lockmittel/Futter** (K42 §10). Schlüssel-, Siegel-, Ausrüstungs-, Zucht- und Evolutionsgegenstände sind nicht tauschbar (Prüfregel SO-03). Die vollständige Liste wird aus den Item-Daten erzeugt:

| Gruppe | Anzahl | Gegenstände |
|---|---|---|
| Ressourcen | 48 | Eichenholz, Klangharz, Farnfaser, Lindblüte, Kupfererz, Moosperle, Bergkiefer, Kharseisen, Grollbasalt, Quarzsplitter, Gipfelenzian, Moorweide, Torfkohle, Nebelperle, Sumpfmyrte, Irrlichtmoos, Wüstendornholz, Salzkupfer, Glutsand, Sonnenglas, Oasenminze, Ascheholz, Schlackenstahl, Obsidian, Schwefelkristall, Feuerlilie, Treibholz, Zinnerz, Perlmutt, Seetang, Salzkraut, Frostkiefer, Silbererz, Gletscherquarz, Eisblume, Polarflechte, Altholz, Dorunstein, Glyphenkristall, Ruinenrebe, Prismaerz, Resonanzkristall, Höhlenpilz, Kristallmoos, Wolkenholz, Sternmetall, Himmelsglas, Windblüte |
| Gerichte | 12 | Lindwald-Eintopf, Fischpastete, Honigkuchen, Würzbrot, Eisgelee, Glutsuppe, Moosbrötchen, Dattelrolle, Tangrolle, Bergkäseplatte, Wolkentarte, Chorfestmahl |
| Lockmittel/Futter | 24 | Lindblüten-Honig, Waldbeeren, Moosküchlein, Glockenspiel, Erzkrümel, Bergkäse, Pfeifholz, Räucherfisch, Moorbeeren, Irrlicht-Laterne, Tangkeks, Muschelfleisch, Windspiel, Datteln, Spiegelscherbe, Glutkohle, Schwefelzucker, Eisfisch, Auroraglas, Glyphenmünze, Kristallsalz, Lockstimmgabel, Wolkenfrucht, Sternenglocke |

Begründung der Auswahl: Ressourcen, Gerichte und Lockmittel sind regional verteilt (K41, K42) – wer in Saltrand lebt, hat Tang und Fisch, wer durchs Morvenmoor reist, Moorbeeren. Diese Dinge zu tauschen fühlt sich nach Nachbarschaft an und spart Zeit (DR-20), verschiebt aber keine Macht: Siegel, Ausrüstung und Evolutionsgegenstände bleiben an eigene Fortschritte gebunden.

### 4.5 Was ein Tausch mit dem Echo macht

| Aspekt | Wirkung |
|---|---|
| Bindung | startet bei 0 (Vorsichtig) bei der neuen Person (TR-08) |
| Gehorsam | Regel CANON §18: voll, wenn Level ≤ 20 + 8 × Akkorde oder Bindungsstufe ≥ 3; sonst +40 % Zeitkosten (deterministisch, ADR-019) |
| Herkunft | bleibt: Erstwärter, Ort, Zeit, Methode (DR-16); Herkunftstitel nur beim Erstwärter |
| Spitzname | bleibt, neue Person kann ihn ändern |
| Lernset, Werte, Genom | unverändert (Legalität geprüft) |
| Zucht | Fernklang ×3, wenn Herkunftsregion ≥ 3 Regionen vom Heimatgarten entfernt (K38) |
| Kodex | Forschungsstufen wie bei eigener Bindung außer „selbst gebunden“ |
| Abschied | ab Bindungsstufe Seelenklang (750) kurzer Abschiedsmoment (Stirn an Stirn, K37); Tagebuch-Erinnerung |

### 4.6 Szenarien

**Die Schwestern aus zwei Regionen.** Mara spielt auf PS5 und hat Morvenmoor gerade verlassen; ihre Schwester spielt auf Switch 2 und steht schon in Ignareth. Mara öffnet am Resonanzstein den Chor, die Schwester tritt bei und aktiviert keinen Einklang-Modus – sie hilft mit ihrem Glutwolf-Echo gegen den Moor-Alpha, den Mara allein nicht schafft. Mara bindet danach ein Unkenchor-Echo, das die Schwester mit einem Köder angelockt hat; im Ursprung steht der Name der Schwester. Die Schwester nimmt Kodex-Forschung, Sol und einige Moorpflanzen mit nach Hause; ihre eigene Geschichte bleibt, wo sie war. Weil Mara kurz darauf eine Story-Szene erreicht, die die Schwester schon kennt, sieht diese sie einfach noch einmal mit – ohne Fortschritt, aber mit einer Tagebuch-Erinnerung.

**Das Paar, das gemeinsam durchspielt.** Zwei Freunde stehen beide bei MQ_A1_04. Sie spielen abwechselnd in beiden Welten; beim Abschluss des Schritts bietet das Spiel „Gleichklang“ an. Jede Person trifft ihre Haltungswahl selbst – der eine verteidigt die Freien Stimmen, der andere nicht. Beide Welten verbuchen den Schritt, die Folgen unterscheiden sich. Das Finale erlebt jede Person allein: Dort hört jede ihre eigene Pause.

**Der Ring in der Klangbörse.** Jona bietet ein häufiges Kieselwelpen-Echo an und wünscht sich ein Schneeluchsjunges-Echo. Niemand mit Schneeluchsjungem will Kieselwelpen. Die Börse findet einen Ring: Jona gibt den Kieselwelpen an Ilvy, die ihn für ihre Zucht braucht; Ilvy gibt ein Glasmotten-Echo an Ruben; Ruben gibt das Schneeluchsjunge an Jona. Alle drei bekommen eine Benachrichtigung, sehen das Echo, das sie erhalten, und halten drei Sekunden. Keine Person musste mit einer fremden Person schreiben.

**Der Zirkel, der fotografiert.** Ein Zirkel aus 31 Mitgliedern wählt die Fotowoche. Die Ziele skalieren auf 31/50 der Liste (186 Fotos ★★★). Mitglieder, die wenig kämpfen, tragen hier am meisten bei. Am Ende hängt im Hain aller Beteiligten ein Fotorahmen mit dem Zirkelwappen – und niemand ist stärker geworden, nur verbundener.

---

## 5. Klangzirkel (Gilden)

### 5.1 Grundidee

Ein **Klangzirkel** ist eine Gemeinschaft von bis zu 50 Wärterinnen und Wärtern, die sich gegenseitig auf Reisen mitnehmen, tauschen, Raids planen und gemeinsam die **Zirkel-Chronik** füllen. Zirkel geben **keine Machtvorteile** (DR-20 nennt „+20 % Werte nur in Gilden“ ausdrücklich als Gegenbeispiel). Gilden waren in K01/K02 als *Could* eingestuft; K60 legt einen schlanken Launch-Umfang fest, der Rest folgt mit Saisons (K68).

### 5.2 Rollen

| DisplayName | Max | Rights |
|---|---|---|
| Zirkelleitung | 1 | Alles inkl. Auflösen, Leitung übergeben |
| Stimmführung | 5 | Einladen, Entfernen (außer Leitung/Stimmführung), Chronik-Ziele wählen, Wappen ändern |
| Mitglied | 44 | Teilnehmen, Zirkel-Tausch, Raid-Gruppensuche, Chat (wenn erlaubt) |
| Gast | 10 | Zeitlich begrenzt (7 Tage) für Raid-Gruppen; kein Tausch |

| Funktion | Launch | Saison 1+ |
|---|---|---|
| Gründen, Einladen, Rollen, Wappen (aus 40 Formen × Typ-/Regionsfarben) | ✔ | |
| Mitgliederliste mit Präsenz, Region, Modus | ✔ | |
| Zirkel-Chat (Freitext opt-in, Schnellchat immer) | ✔ | |
| Raid-Gruppensuche im Zirkel | ✔ | |
| Zirkel-Tausch (Direkttausch ohne Tauschcode) | ✔ | |
| Zirkel-Chronik (Wochenziele) | | ✔ |
| Zirkel-Banner im eigenen Resonanzhain, Zirkel-Gesten | | ✔ |
| Zirkel-Fotowand (geteilte Fotos, moderiert) | | ✔ |

### 5.3 Zirkel-Chronik

Jede Woche wählt die Stimmführung drei Ziele aus der Liste. Alle Beiträge zählen gemeinsam; das Ziel skaliert mit der Zahl aktiver Mitglieder (Liste für 50, linear, mindestens 10). Belohnungen sind ausschließlich kosmetisch und gehen an alle, die mindestens einmal beigetragen haben:

| DisplayName | Measure | Target | Reward |
|---|---|---|---|
| Gemeinsam beobachten | Echos im Kodex beobachten | 2000 | Banner-Muster „Lauschende Linde“ |
| Fotowoche | Fotos mit ★★★ (K39) | 300 | Fotorahmen „Zirkel“ |
| Wildwacht-Hilfe | Stillezonen-Aufträge (CT_SILENCE) | 150 | Zelt-Stil „Wacht“ |
| Klangfeste | Feste in Siedlungen besuchen | 200 | Geste „Reigen“ |
| Saat und Ernte | Ressourcen sammeln | 25000 | Hain-Deko „Erntekranz“ |
| Bindungsklang | Echos binden (perfekter Anschlag) | 500 | Resonator-Muster „Gleichklang“ |
| Raidchor | Raids abschließen (beliebig) | 120 | Banner-Farbe „Raidgold“ |
| Arena-Gruß | Arena-Halle (frei) Kämpfe mit Gruß beendet | 400 | Geste „Verbeugung“ |
| Brutnischen | Echos schlüpfen lassen | 600 | Hain-Deko „Nestglocke“ |
| Wanderchor | Resonanzsteine bereisen (Schnellreise zählt nicht) | 800 | Gleiter-Muster „Zugvögel“ |
| Kochkunst | Gerichte kochen | 1500 | Lager-Stil „Festtafel“ |
| Tiefenklang | Tiefenresonanzen abschließen | 200 | Titel „Tiefenstimme“ (Zirkel) |

Die Ziele belohnen das, was AETHRIS ausmacht – Beobachten, Fotografieren, Wildwacht-Hilfe, Feste, Kochen – und nicht nur Kämpfe. So können auch Mitglieder beitragen, die wenig kämpfen.

### 5.4 Regeln

| Regel | Festlegung |
|---|---|
| Mitgliedschaft | 1 Zirkel je Konto; Wechsel jederzeit, Wiedereintritt in denselben Zirkel nach 24 h |
| Name, Wappen | Name 3–24 Zeichen, Namensfilter + Meldung; Wappen aus Baukasten (keine freien Bilder) |
| Inaktivität | Leitung 30 Tage inaktiv → Übergabe an die aktivste Stimmführung |
| Auflösen | nur Leitung, Halten 3 s; Chronik-Belohnungen bleiben |
| Kinder | Zirkel beitreten erlaubt; Freitext nach Plattform-Einstellung |

---

## 6. Freunde, Grüße, Hain-Besuche

| Funktion | Beschreibung | Grenze |
|---|---|---|
| Freundesliste | Plattform-Freunde + Aethris-Freunde (plattformübergreifend, per Freundescode) | 200 Aethris-Freunde |
| Präsenz | „Erkundet Morvenmoor“, „Im Raid“, „Im Hain“ (grob, abschaltbar) | – |
| Grußgabe | Einmal je Tag und Freund eine kleine Gabe (bis 10 Ressourcen oder 1 Gericht) mit Schnellchat-Satz | 1/Tag/Freund, max. 20 versendet/Tag |
| Hain-Besuch | Den Resonanzhain eines Freundes als Momentaufnahme besuchen (asynchron, Gärten, Echos, Deko); Echos dort streicheln (rein kosmetisch), Grußgabe hinterlassen | Momentaufnahme täglich aktualisiert |
| Geister-Teams | Freundes-Teams als Übungsgegner in der Arena-Halle (lokal, K61) | – |
| Fotoalbum | Fotos teilen mit Freunden/Zirkel (moderiert, K59 §8) | 50 geteilte Fotos |

Der **Hain-Besuch** ist bewusst asynchron: Er braucht keinen gleichzeitigen Online-Status, keinen Server mit Spielwelt und verursacht kaum Kosten – das Backend speichert eine kompakte Beschreibung des Hains (Gärten, Ausbaustufen, Deko, bis zu 60 sichtbare Echos), die der Client mit den eigenen Assets aufbaut.

---

## 7. Kommunikation

### 7.1 Schnellchat

Standard überall (K59 §10): 24 Sätze, in der Sprache der Empfangenden angezeigt, dazu Gesten.

| ID | Gruppe | Satz |
|---|---|---|
| QC_01 | Gruß | „Guter Klang!“ |
| QC_02 | Gruß | „Schön, dich zu hören.“ |
| QC_03 | Gruß | „Bis zum nächsten Stein!“ |
| QC_04 | Dank | „Danke!“ |
| QC_05 | Dank | „Danke für den Kampf.“ |
| QC_06 | Dank | „Danke für den Tausch.“ |
| QC_07 | Treffen | „Ich warte am Resonanzstein.“ |
| QC_08 | Treffen | „Komm zu mir.“ |
| QC_09 | Treffen | „Ich bin gleich zurück.“ |
| QC_10 | Treffen | „Lass uns zum Lager.“ |
| QC_11 | Kampf | „Ich übernehme die Vorderreihe.“ |
| QC_12 | Kampf | „Harmonie fast voll!“ |
| QC_13 | Kampf | „Kombo vorbereiten?“ |
| QC_14 | Kampf | „Crescendo kommt.“ |
| QC_15 | Kampf | „Ich heile.“ |
| QC_16 | Bindung | „Hilfe bei der Bindung?“ |
| QC_17 | Bindung | „Ich lege einen Köder.“ |
| QC_18 | Bindung | „Leise – nicht verscheuchen!“ |
| QC_19 | Welt | „Vorsicht, Stille!“ |
| QC_20 | Welt | „Hier gibt es etwas Seltenes.“ |
| QC_21 | Welt | „Schau mal hierher!“ |
| QC_22 | Welt | „Resonanzsturm zieht auf.“ |
| QC_23 | Antwort | „Ja.“ |
| QC_24 | Antwort | „Nein, danke.“ |

### 7.2 Gesten

24 Gesten aus dem Spieler-Animationssatz (K57 `HUM_PLAYER_SOCIAL`: 12 Grundgesten) plus 12 freischaltbare Gesten (Feste, Zirkel-Chronik, Fraktionsränge, Arena-Gruß). Gesten sind auch der Weg, in der Arena-Halle respektvoll zu grüßen – ein Kampf beginnt und endet mit einer Verbeugung, wenn beide sie wählen (Zirkel-Ziel ZC_08).

### 7.3 Freitext

Nur opt-in, nur mit Freunden und im Zirkel, mit Plattform- und eigenem Filter, Ratenlimit, Melden mit Kontext. Kein Freitext in der Klangbörse, in Raids mit Fremden oder in PvP.

---

## 8. Sicherheit, Kinder, Moderation

| Thema | Festlegung |
|---|---|
| Fremde | Kontakt mit Fremden nur in strukturierter Form: Klangbörse (anonym, ohne Chat), Raid-/PvP-Matchmaking (Schnellchat/Gesten) |
| Elternkontrolle | Plattform-Einstellungen bestimmen Online-Spiel, Kommunikation und Klangbörse (TR-14) |
| Blockieren | wirkt auf Einladungen, Tausch, Zirkel-Chat, Matchmaking (Vermeiden), plattformübergreifend |
| Melden | Name, Zirkelname, Wappen, Freitext, Foto, Verhalten (Raid-Abbruch); mit Kontext |
| Sanktionen | Hinweis → Kommunikationssperre (24 h/7 Tage) → Online-Sperre; Weltspiel bleibt immer spielbar (NZ-1) |
| Betrug beim Tausch | Treuhand + Bestätigung nach Ansicht machen „Tauschtricks“ unmöglich; Rückabwicklung nur bei nachgewiesenem Systemfehler |
| Bots | Ratenlimits (TR-05–TR-07), Verhaltensanalyse, Konto-Alter ≥ 7 Tage für Klangbörse |

---

## 9. UX-Abläufe

```
DIREKTTAUSCH (Freund)
 Profil/Freundesliste ▸ „Tauschen“ ─► Tauschtisch: links eigenes Angebot (1–3 Echos, Gegenstände), rechts Partner
 ─► beide „Bereit“ ─► Ansicht der Gegenseite (Echo-Karte: Art, Level, Ursprung, Gehorsam-Hinweis bei dir)
 ─► Halten 3 s „Tauschen“ (beide) ─► Abschiedsmoment (falls Seelenklang) ─► Ankunft im Hain
 Eingaben: 4–6 · Abbruch jederzeit bis zur Bestätigung beider

KLANGBÖRSE
 Tauschhalle/Menü ▸ „Klangbörse“ ─► Echo wählen ─► Wunschliste (Kodex-Suche, bis 3 Arten) ─► „Angebot einstellen“
 … Benachrichtigung „Ein Tausch wartet“ ─► Echo ansehen ─► Halten 3 s ─► fertig

KOOP
 Resonanzstein ▸ „Chor öffnen“ ▸ Einladen   |   Benachrichtigung ▸ „Beitreten“ ▸ Spoiler-Hinweis (falls nötig)
```

| Bildschirm | Neu/erweitert | Kapitel |
|---|---|---|
| Tauschtisch | neu (Teil der Tauschhalle, K54 `Screens.csv`) | K60 |
| Klangbörse | neu | K60 |
| Zirkel (Liste, Rollen, Wappen, Chronik) | neu | K60 |
| Freunde/Präsenz | erweitert (Profil) | K54 |
| Koop-Sitzung (Mitspielende, Einklang-Modus, Rauswurf) | neu (Overlay am Resonanzstein) | K60 |

---

## 10. Technik

### 10.1 Treuhand-Zustände

`EAethrisTradeState` (GF_Multiplayer): Draft → Validating → AwaitingPartner → Review → Escrow → Completed; Cancelled aus jedem offenen Zustand (im Escrow nur durch den Server bei Fehlern); Rejected nach Regelverstoß. Eine Änderung im Review führt zurück zur Prüfung. Grenzen als Konstanten in `Aethris::Trade` (3 Echos, 20 Gegenstände, 24 h Sperre, 3 Börsenangebote, 5 Börsentausche/Tag, 30 Direkttausche/Tag).

```
Server: Tausch abschließen (Escrow → Completed)
  BEGIN TRANSACTION (serialisierbar)
    für jede Seite s:
        prüfe Signatur(s.echos) == gespeicherte Signatur      // Stand unverändert seit Validierung
        prüfe Sperren (24 h, Tageslimits)
    verschiebe Echos und Gegenstände zwischen Treuhandkonten
    schreibe Transaktions-ID in beide Spielstand-Deltas
  COMMIT  → Push an beide Clients („Tausch abgeschlossen“) → Client wendet Delta auf geladenen Weltstand an
  Fehler → ROLLBACK, Zustand Cancelled, alles zurück
```

**Offline-Spielstand und Tausch:** Der Spielstand ist lokal (K64). Beim Tausch schreibt der Client ein Delta (Echo raus/rein) mit Transaktions-ID; der Server führt eine Liste offener Deltas je Konto, bis der Client sie bestätigt. Ein Echo, das getauscht wurde, ist im lokalen Stand sofort als „unterwegs“ gesperrt – Duplizierung durch Neuladen eines älteren Spielstands wird beim nächsten Online-Kontakt erkannt (Signatur bereits verwendet) und das Duplikat ist online nicht nutzbar.

### 10.2 Dienste

| Dienst (K59 §8) | Aufgabe in K60 |
|---|---|
| Tausch-Treuhand | Direkttausch, Klangbörse (Abgleich alle 5 min je Backend-Region), Deltas |
| Legalität | Prüfung + Signatur vor jedem Tausch |
| Soziales | Freunde, Zirkel, Rollen, Chronik-Zähler, Grußgaben, Hain-Momentaufnahmen |
| Moderation | Namen, Wappen, Freitext, Fotos |
| Sitzung | Koop-Einladungen, offene Sitzungen für Freunde |

### 10.3 Save-Fragmente

| Fragment | Inhalt | Kapitel |
|---|---|---|
| `Player.Social` | Zirkel-ID (Verweis), Grußgaben-Zähler, Gesten-Freischaltungen | K64 |
| `Player.TradeDeltas` | offene Tausch-Deltas, gesperrte Echos „unterwegs“ | K64 |
| `Player.CoopLedger` | Gast-Protokoll der letzten Sitzung bis zur Anwendung | K59/K64 |
| `Player.Memories` | Tagebuch-Erinnerungen „Gemeinsam erlebt“, Abschiede | K64 |

---

## 11. Telemetrie und Ziele

| Kennzahl | Ziel (6 Monate nach Launch) | Zweck |
|---|---|---|
| Anteil Spielender mit ≥ 1 Koop-Sitzung | ≥ 35 % | S5 wirkt |
| Abgeschlossene Tausche je aktiver Person/Monat | ≥ 2 | Tausch lebt |
| Klangbörse: Erfüllungsquote nach 72 h | ≥ 45 % | Ring-Tausch wirksam |
| Zirkel-Mitgliedschaft | ≥ 25 % der Online-Aktiven | Gemeinschaft |
| Meldungen je 1.000 Sitzungen | ≤ 2 | Sicherheit |
| Koop-Abbrüche durch Verbindung | ≤ 3 % | Technik (K59) |
| Solo-Abschlussquote Story | unverändert ggü. Koop-Spielenden | DR-19 |

---

## 12. Prüfregeln

`tools/ref/aethris_social.py validate`:

| Regel | Inhalt |
|---|---|
| SO-01 | Jede Art hat einen Solo-Zugang (DR-19) |
| SO-02 | Nur Ursprungsstimmen und Mythische sind vom Tausch ausgeschlossen |
| SO-03 | Tauschliste nur Ressourcen, Gerichte, Lockmittel/Futter |
| SO-04 | Zirkel ≤ 50 Mitglieder, genau eine Leitung |
| SO-05 | Zirkel-Belohnungen nur kosmetisch (DR-20) |
| SO-06 | 24 eindeutige Schnellchat-Sätze, ≤ 40 Zeichen |
| SO-07 | Koop-Belohnungsarten passen zum Gast-Protokoll |

**Ergebnis:** Prüfregeln SO-01–SO-07: **0 Verstöße**. Solo-Zugang aller 256 Arten: Wildvorkommen 187, Evolution 53, Stimmsiegel-Quest (CANON §34) 10, Mythos-Zugang (§34) 6. Tauschbar: 240 Arten; Tauschliste: Ressourcen 48, Gerichte 12, Lockmittel/Futter 24 = 84 Gegenstände.

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Narrative | Tagebuch-Erinnerungen „Gemeinsam erlebt“ je Story-Moment; Spoiler-Hinweis; Abschiedsmoment-Zeilen | K44–K46 |
| Quest-Design | Gleichklang: `StepId` stabil, Entscheidungsdialoge je Person; Mithilfe-Belohnung 50 % | K48 |
| UI | Tauschtisch, Klangbörse, Zirkel, Koop-Overlay, Spoiler-Dialog | K54 |
| Animation | 12 freischaltbare Gesten, Abschiedsmoment je Archetyp-Größe | K57 |
| Backend | Treuhand, Ring-Abgleich, Zirkel, Hain-Momentaufnahme | K59 |
| Save | Fragmente `Player.Social`, `Player.TradeDeltas`, `Player.CoopLedger`, `Player.Memories` | K64 |
| LiveOps | Zirkel-Chronik ab Saison 1, Ziele rotieren | K68 |
| QA | Tausch-Duplizierungstests (Neuladen, Verbindungsabbruch im Escrow), Kinderkonto-Matrix | K66 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-243 | Q4: Story-Fortschritt im Koop ist persönlich; Erinnerungen, Kodex, EP, Beute werden mitgenommen; „Gleichklang“ bei gleichem Schritt | Entscheidungen gehören jeder Person; keine Flag-Konflikte | geteilter Fortschritt; gespiegelt ohne Wahl |
| ADR-244 | Koop-Wildgegner skalieren mit 700 ‰ HP je weiterem Spieler; volle Belohnung für alle | Einheitlich mit Raid; DR-20 Zeitersparnis | geteilte EP; feste Gegner |
| ADR-245 | Optionaler Einklang-Modus (Gäste-Echos auf Zonenband + 5) | Gemeinsames Spielen bei ungleichem Fortschritt ohne Zwang | Pflicht-Levelangleichung |
| ADR-246 | Klangbörse ohne Preise mit 2er- und 3er-Ringen | Höhere Erfüllungsquote ohne Markt (ADR-156) | 1:1 only; Auktionshaus; größere Ringe |
| ADR-247 | Klangzirkel bis 50 ohne Machtvorteile; Chronik mit kosmetischen Belohnungen ab Saison 1 | DR-20, Gemeinschaft ohne Pflicht | Gildenboni; Gildenkriege |
| ADR-248 | Asynchrone Hain-Besuche und Grußgaben | Soziale Nähe ohne gleichzeitige Präsenz, geringe Kosten | Gemeinsame Hain-Instanzen |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §236 | Koop-Reise: Ablauf am Resonanzstein, ab Prolog-Ende; Format nach Spielerzahl (Duo/Trio/Quartett), Wild-HP ×(1 + 0,7 × (n − 1)), volle Belohnung, Einklang-Modus (Zonenband + 5), Gäste binden keine Ursprungsstimmen/Mythischen/Stille-Echos, gemeinsames Lager, Szenen-Abstimmung 30 s | LOCKED |
| §237 | Q4: Story persönlich (Option C); `CoopRewards.csv`; Gleichklang bei gleicher `StepId` (Entscheidungen je Person, nicht Finale/Story-Boss); Spoiler-Schutz; Nebenquest-Mithilfe 50 % EP/Sol | LOCKED (schließt Q4) |
| §238 | Tausch: `TradeRules.csv` TR-01–TR-15; Direkttausch (Freunde/Zirkel/Koop/Tauschcode), Klangbörse (Wunschliste ≤ 3, 2er + 3er-Ringe, Abgleich 5 min, Bestätigung 24 h); Tauschliste 84 Gegenstände; Treuhand `EAethrisTradeState`; Deltas mit Transaktions-ID | LOCKED |
| §239 | Klangzirkel (50 + 10 Gäste, Rollen `GuildRoles.csv`), Chronik `GuildGoals.csv` (kosmetisch, ab Saison 1), Freunde (200), Grußgabe 1/Tag/Freund, Hain-Besuch asynchron, Schnellchat `QuickChat.csv`, 24 Gesten, Freitext nur Freunde/Zirkel opt-in | LOCKED |
| Q-Liste | Q4 geschlossen (→ §237) | – |
| §10 | ADR-243 – ADR-248 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Ziele und Leitfragen (DR-19, DR-20, Sicherheit)
- [x] Koop-Reise: Ablauf, Kampf mit Skalierung, Einklang-Modus, Bindung/Reiten/Sammeln, Szenen
- [x] Q4 entschieden (Optionen, Begründung, Belohnungstabelle, Gleichklang, Spoiler-Schutz)
- [x] Tausch: Regeln TR-01–TR-15, Direkttausch, Klangbörse mit Ring-Tausch (simuliert), Tauschliste, Wirkung auf Echos
- [x] Klangzirkel: Rollen, Umfang Launch/Saison, Chronik, Regeln
- [x] Freunde, Grußgaben, Hain-Besuche, Schnellchat, Gesten, Freitext
- [x] Sicherheit, Kinder, Moderation; UX-Abläufe; Technik (Treuhand, Deltas, Fragmente)
- [x] Telemetrie-Ziele, Prüfregeln SO-01–SO-07 (0 Verstöße)
- [x] Anforderungen, ADR-243 – ADR-248, CANON §236–§239

➡️ **Nächstes Kapitel: K61 – PvP und Ranked.**
