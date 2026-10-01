# K39 · Forschung – Echo-Kodex, Klangfragmente und Fotografie

| Feld | Wert |
|---|---|
| Dokument | Kapitel 39 von 68 · Systeme, Teil IV |
| Version | 1.0 |
| Owner | Lead Systems Designer (Forschung) |
| Mitwirkende | Narrative Lead (Kodex-Texte, Klangfragmente, Wahrheitsebenen), UX Lead (Kodex, Kamera-UI), Rendering (Fotomodus), Audio (Fragment-Aufnahmen), Creature Design (Verhaltensanimationen) |
| Baut auf | DR-01 (Wissen schlägt Items), DR-02 (≥ 3 Verhaltensmerkmale), DR-33 (Evolutionsbedingungen erlernbar), CANON §6 (Kodex, Kodex-Linse, Resonanzsinn), §18 (P11: 256 × 4 Stufen), §34 (Mirrowisp – Fotografie-Meisterschaft), §38 (Lore-Kanäle, L-01), K19 §9 (Evolutionsahnung), K36 (Kodex-Bonus), K37 (Begleiter-Initiative) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Research/KodexTasks.csv` (768 Aufgaben), `Data/Lore/LoreEntries.csv` (120 Klangfragmente), `tools/authoring/research_k39.py` |
| Neue Kanon-Einträge | CANON §146 (Kodex-Stufen), §147 (Beobachtung & Resonanzsinn), §148 (Klangfragmente), §149 (Kodex-Linse & Fotobewertung), §150 (Fotografie-Meisterschaft) |

---

## Inhalt

1. [Forschung als Spielweise](#1-forschung-als-spielweise)
2. [Die vier Kodex-Stufen](#2-die-vier-kodex-stufen)
3. [Kodex-Aufgaben (Stufe 4)](#3-kodex-aufgaben-stufe-4)
4. [Beobachten mit dem Resonanzsinn](#4-beobachten-mit-dem-resonanzsinn)
5. [Der Kodex als Buch](#5-der-kodex-als-buch)
6. [Klangfragmente](#6-klangfragmente)
7. [Die Kodex-Linse](#7-die-kodex-linse)
8. [Fotobewertung](#8-fotobewertung)
9. [Fotomodus und Album](#9-fotomodus-und-album)
10. [Fotografie-Meisterschaft und Mirrowisp](#10-fotografie-meisterschaft-und-mirrowisp)
11. [Belohnungen und Wärter-EP](#11-belohnungen-und-wärter-ep)
12. [Code](#12-code)
13. [Tests und Telemetrie](#13-tests-und-telemetrie)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Forschung als Spielweise

Forschung ist einer der drei gleichwertigen Primär-Loops (K02 §5): Wer lieber beobachtet als kämpft, soll AETHRIS vollständig erleben können. Forschung belohnt **Aufmerksamkeit**: Wer weiß, wann ein Echo schläft, was es frisst und wie es sich bei Gewitter verhält, bindet leichter (K36: bis +240 Resonanz), kämpft besser (Effektivitätsvorschau ab Stufe 2) und versteht die Welt (Lore, Evolutionsahnungen).

| Werkzeug | Funktion |
|---|---|
| **Resonanzsinn** | Wahrnehmungsmodus: Frequenzen, Stimmungen, Spuren, Verhalten beobachten |
| **Echo-Kodex** | Bestiarium mit 4 Stufen je Art (256 × 4 = 1.024 Forschungsstufen) |
| **Klangfragmente** | 120 dorunische Aufnahmen – die Stimmen der Vergangenheit |
| **Kodex-Linse** | Kamera des Wärters: Fotos, Fotoaufgaben, Album |

---

## 2. Die vier Kodex-Stufen

| Stufe | Name | Bedingung | Freischaltungen |
|---|---|---|---|
| 1 | **Gesichtet** | im Resonanzsinn erfasst, im Kampf getroffen oder fotografiert | Name, Silhouette, Region, Ruf-Sample |
| 2 | **Beobachtet** | 2 Verhaltensmerkmale beobachtet **oder** 3 Kämpfe gegen die Art **oder** 1 Bindung | Typen, Lieblingsköder, Merkmale, Habitat, Aktivität; **Effektivitätsvorschau** (CANON §78); Bindungsbonus +120 (Stufe 0–2 kumuliert: 0/60/120) |
| 3 | **Erforscht** | gebunden **und** alle Verhaltensmerkmale beobachtet **und** 1 Foto ≥ 2 Sterne | Evolutionsahnung (K19 §9), passende Fallen und Ruhephase (K36 §8.1), Resonanzgruppe (K38), Signaturbeschreibung, Lernset-Vorschau; Bindungsbonus +180 |
| 4 | **Verstanden** | alle 3 Kodex-Aufgaben der Art (§3) | Lore „L4“, Allel-Anzeige (mit Skill Erbkunde), versteckte Passive per Wandelklang freischaltbar (CANON §102); Bindungsbonus +240 |

**Kodex für entwickelte Formen:** Eine Evolution setzt die neue Art mindestens auf Stufe 3 (CANON §86); ihre Verhaltensmerkmale gelten als beobachtet, sofern die Vorstufe Stufe 3 hatte.

**Anzeige:** Jede Art zeigt einen Ring aus vier Segmenten; der Kodex-Gesamtfortschritt ist in Prozent sichtbar (1.024 Segmente).

---

## 3. Kodex-Aufgaben (Stufe 4)

Jede Art hat drei Aufgaben, die **aus ihren Daten abgeleitet** werden (keine Handarbeit je Art, keine Willkür):

| Aufgabe | Ableitung | Anteil |
|---|---|---|
| Beobachten | ein Verhaltensmerkmal der Art (DR-02) + ihre Aktivitätszeit | 256 |
| Fotografieren | bei der Spawn-Bedingung (Wetter, Tageszeit, Mond, Ort) – oder Verhaltensfoto | 214 |
| Reiten | 2 km auf dem Reittier (Arten mit `Mount`, ohne Spawn-Bedingung) | 42 |
| Entwicklung | eine Evolution der Art erleben (lehrt die Bedingung, DR-33) | 125 |
| Bindungsstufe | Stufe 3 (bzw. 4 bei Stimmen/Mythischen) | 53 |
| Einklang | ein Echo der Art mit Einklang binden | 44 |
| Kämpfe | 10 Siege gegen oder mit der Art | 34 |

**Auszug** (jede sechste Art; vollständige Liste in `KodexTasks.csv`):

| # | Art | Aufgabe 1 | Aufgabe 2 | Aufgabe 3 |
|---|---|---|---|---|
| 001 | Fernlit | Beobachte das Verhalten „Familienverband“ mit dem Resonanzsinn (in der Dämmerung) | Fotografiere es bei Regen mit mindestens 2 Sternen | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 007 | Wisplet | Beobachte das Verhalten „Neugierig“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei Gewitter mit mindestens 2 Sternen | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 013 | Lorncant | Beobachte das Verhalten „Nachahmer“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erreiche Bindungsstufe 3 mit einem Echo dieser Art |
| 019 | Lumow | Beobachte das Verhalten „Bestäuber“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 025 | Skirmote | Beobachte das Verhalten „Schwarm“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 031 | Rivetkin | Beobachte das Verhalten „Muster-Sammler“ mit dem Resonanzsinn (zu jeder Tageszeit) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 037 | Tetri | Beobachte das Verhalten „Schläfer“ mit dem Resonanzsinn (zu jeder Tageszeit) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 043 | Gratkin | Beobachte das Verhalten „Neugierig“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 049 | Lithshell | Beobachte das Verhalten „Schläfer“ mit dem Resonanzsinn (in der Dämmerung) | Fotografiere es in der Abenddämmerung mit mindestens 2 Sternen | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 055 | Dawnix | Beobachte das Verhalten „Sonnenbader“ mit dem Resonanzsinn (tagsüber) | Fotografiere es in der Morgendämmerung mit mindestens 2 Sternen | Erreiche Bindungsstufe 3 mit einem Echo dieser Art |
| 061 | Toxmire | Beobachte das Verhalten „Schlammbader“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erreiche Bindungsstufe 3 mit einem Echo dieser Art |
| 067 | Irraune | Beobachte das Verhalten „Hüter“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 073 | Virwyn | Beobachte das Verhalten „Flieger“ mit dem Resonanzsinn (in der Dämmerung) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Binde ein Echo dieser Art mit Einklang |
| 079 | Umbracoil | Beobachte das Verhalten „Schwimmer“ mit dem Resonanzsinn (nachts) | Fotografiere es nachts mit mindestens 2 Sternen | Erreiche Bindungsstufe 3 mit einem Echo dieser Art |
| 085 | Marlit | Beobachte das Verhalten „Schwimmer“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 091 | Brikin | Beobachte das Verhalten „Neugierig“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 097 | Mystdral | Beobachte das Verhalten „Einzelgänger“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erreiche Bindungsstufe 3 mit einem Echo dieser Art |
| 103 | Glimar | Beobachte das Verhalten „Hüter“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Binde ein Echo dieser Art mit Einklang |
| 109 | Sheamast | Beobachte das Verhalten „Treiber“ mit dem Resonanzsinn (nachts) | Fotografiere es bei Nebel mit mindestens 2 Sternen | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 115 | Dunhorn | Beobachte das Verhalten „Weidegänger“ mit dem Resonanzsinn (tagsüber) | Lege auf ihm reitend 2 km zurück (Ground) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 121 | Sengar | Beobachte das Verhalten „Gräber“ mit dem Resonanzsinn (tagsüber) | Lege auf ihm reitend 2 km zurück (Dig) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 127 | Mirasel | Beobachte das Verhalten „Nachahmer“ mit dem Resonanzsinn (tagsüber) | Fotografiere es zur Mittagszeit mit mindestens 2 Sternen | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 133 | Qadrant | Beobachte das Verhalten „Hüter“ mit dem Resonanzsinn (nachts) | Fotografiere es nachts mit mindestens 2 Sternen | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 139 | Ambrak | Beobachte das Verhalten „Werkzeugnutzer“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 145 | Obsidar | Beobachte das Verhalten „Getarnt“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 151 | Drusil | Beobachte das Verhalten „Kletterer“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 157 | Snevel | Beobachte das Verhalten „Verspielt“ mit dem Resonanzsinn (in der Dämmerung) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 163 | Uvlet | Beobachte das Verhalten „Flieger“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 169 | Lysthane | Beobachte das Verhalten „Treiber“ mit dem Resonanzsinn (nachts) | Lege auf ihm reitend 2 km zurück (Fly) | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 175 | Hallbrand | Beobachte das Verhalten „Revierverteidigend“ mit dem Resonanzsinn (tagsüber) | Lege auf ihm reitend 2 km zurück (Climb) | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 181 | Skriveth | Beobachte das Verhalten „Leuchtend“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erreiche Bindungsstufe 3 mit einem Echo dieser Art |
| 187 | Tikkoran | Beobachte das Verhalten „Einzelgänger“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Gewinne 10 Kämpfe gegen oder mit dieser Art |
| 193 | Hymlit | Beobachte das Verhalten „Sänger“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 199 | Klirrit | Beobachte das Verhalten „Schwarm“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 205 | Spathorn | Beobachte das Verhalten „Einzelgänger“ mit dem Resonanzsinn (nachts) | Lege auf ihm reitend 2 km zurück (Dig) | Binde ein Echo dieser Art mit Einklang |
| 211 | Mullit | Beobachte das Verhalten „Muster-Sammler“ mit dem Resonanzsinn (nachts) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 217 | Miasmar | Beobachte das Verhalten „Lauerjäger“ mit dem Resonanzsinn (nachts) | Fotografiere es nachts mit mindestens 2 Sternen | Erreiche Bindungsstufe 3 mit einem Echo dieser Art |
| 223 | Cirrhawk | Beobachte das Verhalten „Flieger“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 229 | Harfel | Beobachte das Verhalten „Flieger“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |
| 235 | Levitel | Beobachte das Verhalten „Neugierig“ mit dem Resonanzsinn (tagsüber) | Fotografiere es bei einer Verhaltensanimation (Verhaltensfoto, ≥ 2 Sterne) | Erlebe eine Entwicklung dieser Art (Evolutionsahnung lesen) |

---

## 4. Beobachten mit dem Resonanzsinn

Der **Resonanzsinn** (Taste halten) verlangsamt die Welt optisch nicht, sondern legt eine Wahrnehmungsschicht darüber:

| Ebene | Darstellung | Reichweite |
|---|---|---|
| Frequenzen | farbige Wellenlinien je Echo (Typfarbe), Stärke = Nähe | 60 m (Skill bis 100 m) |
| Stimmung | Wellenform: ruhig (Sinus), neugierig (Dreieck), unruhig (Säge), aufgewühlt (Rauschen) | 40 m |
| Spuren | leuchtende Fährten der letzten 10 Spielminuten | 30 m |
| Verhalten | Symbol über dem Echo, wenn ein Verhaltensmerkmal gerade **ausgeführt** wird | Sicht |
| Nester, Ressourcen | Nester (Brutnischen wilder Herden), Erz/Kristall/Kräuter | 40 m |

**Beobachtung zählt**, wenn der Spieler ein Verhaltensmerkmal **während der Ausführung** 3 Sekunden im Resonanzsinn fokussiert, ohne entdeckt zu werden. Jedes der 40 Verhaltensmerkmale (`BehaviorTraits.csv`) hat eine erkennbare Animation (K57) und wird von der Ökologie-KI aktiv ausgespielt (K52) – „Scheu“ etwa als Flucht bei Annäherung über 15 m.

**Barrierefreiheit:** Wellenformen sind zusätzlich als Symbole verfügbar; Resonanzsinn kann auf Umschalten statt Halten gestellt werden.

---

## 5. Der Kodex als Buch

Der Kodex ist ein diegetisches Buch des Wärters (Akademie-Ausgabe, von Ysolde annotiert) mit Reitern:

| Reiter | Inhalt |
|---|---|
| Arten | 256 Einträge, Filter nach Region, Typ, Stufe, Seltenheit, gebunden |
| Verhalten | 40 Verhaltensmerkmale mit Beispielarten (Lexikon) |
| Evolution | Linienbäume, Ahnungen (Stufe 3), erlebte Entwicklungen |
| Zuchtbuch | K38 §9 |
| Klangfragmente | 120 Aufnahmen (abspielbar) |
| Album | Fotos (K39 §9) |
| Wetter & Himmel | Wetterbeobachtungen, Mondkalender (K14/K15) |

**Texte je Art** (aus `SpeciesLore.csv`): Herkunft (Stufe 2), Verhalten (Stufe 2), Mythos (Stufe 3), Beziehung zu Menschen (Stufe 3), L4-Notiz (Stufe 4). Die Texte sind bereits im Katalog (K20–K27) für alle 256 Arten geschrieben.

---

## 6. Klangfragmente

**Klangfragmente** sind dorunische Aufnahmen: kristallisierte Momente der Vergangenheit, die der Wärter mit dem Resonanzsinn „hören“ kann (CANON §38: 120 Fragmente). Sie erzählen die Vorgeschichte der Großen Stille aus der Sicht von Ilen, Archon Maedryn, dem Erstchor, dorunischen Archivaren und einfachen Menschen.

| Regel | Wert |
|---|---|
| Anzahl | 120 = 10 Regionen × 12 Themen |
| Wahrheitsebene | jedes Fragment trägt eine Ebene 0–9 (CANON §38, W1–W9) |
| L-01 | Fragmente oberhalb des erreichten Story-Wissens sind **verzerrt** (Rauschen, Lücken, falsche Namen); nach der Enthüllung der Ebene werden sie im Kodex automatisch „klar“ |
| Fundorte | Ebene 0–3: frei in der Region (Fundort-Tabelle in K49–K51); Ebene 4–9: an den Schlafstätten der Ursprungsstimmen (nach deren Erwachen, ADR-038) |
| Erkennung | Begleiter ab Stufe 4 spüren Fragmente (K37); Resonanzsinn zeigt sie ab 30 m |
| Präsentation | 20–60 s Audio-Szene mit visueller Rückblende (Silhouetten in Klangmal-Linien) |

**Die zwölf Themen** (in jeder Region aus anderer Perspektive):

| # | Thema | Sprecher | Ebene |
|---|---|---|---|
| 1 | Das erste Lied | Erstchor | 0 |
| 2 | Ein Kinderlied | Alltagsstimme | 0 |
| 3 | Die Stimme dieses Landes | Erstchor | 1 |
| 4 | Warnung der Hüter | Dorunische Archivarin | 2 |
| 5 | Der Missklang beginnt | Dorunischer Archivar | 3 |
| 6 | Der Erstchor versammelt sich | Erstchor | 4 |
| 7 | Die Arena über dem Schlaf | Erstchor | 4 |
| 8 | Ilens Zweifel | Ilen | 5 |
| 9 | Maedryns Versprechen | Archon Maedryn | 6 |
| 10 | Die letzte Nacht vor der Stille | Ilen | 7 |
| 11 | Der Riegel | Ilen | 8 |
| 12 | Was danach bleibt | Ilen | 9 |

**Alle Fragmente:**

| Name | Region | Title | Speaker | TruthLevel |
|---|---|---|---|---|
| LORE_FRG_001 | R01 | Das erste Lied – Wurzelhalle | Erstchor | 0 |
| LORE_FRG_002 | R01 | Ein Kinderlied – Wurzelhalle | Alltagsstimme | 0 |
| LORE_FRG_003 | R01 | Die Stimme dieses Landes – Wurzelhalle | Erstchor | 1 |
| LORE_FRG_004 | R01 | Warnung der Hüter – Wurzelhalle | Dorunische Archivarin | 2 |
| LORE_FRG_005 | R01 | Der Missklang beginnt – Wurzelhalle | Dorunischer Archivar | 3 |
| LORE_FRG_006 | R01 | Der Erstchor versammelt sich – Wurzelhalle | Erstchor | 4 |
| LORE_FRG_007 | R01 | Die Arena über dem Schlaf – Wurzelhalle | Erstchor | 4 |
| LORE_FRG_008 | R01 | Ilens Zweifel – Wurzelhalle | Ilen | 5 |
| LORE_FRG_009 | R01 | Maedryns Versprechen – Wurzelhalle | Archon Maedryn | 6 |
| LORE_FRG_010 | R01 | Die letzte Nacht vor der Stille – Wurzelhalle | Ilen | 7 |
| LORE_FRG_011 | R01 | Der Riegel – Wurzelhalle | Ilen | 8 |
| LORE_FRG_012 | R01 | Was danach bleibt – Wurzelhalle | Ilen | 9 |
| LORE_FRG_013 | R02 | Das erste Lied – Kharsholmer Schlund | Erstchor | 0 |
| LORE_FRG_014 | R02 | Ein Kinderlied – Kharsholmer Schlund | Alltagsstimme | 0 |
| LORE_FRG_015 | R02 | Die Stimme dieses Landes – Kharsholmer Schlund | Erstchor | 1 |
| LORE_FRG_016 | R02 | Warnung der Hüter – Kharsholmer Schlund | Dorunische Archivarin | 2 |
| LORE_FRG_017 | R02 | Der Missklang beginnt – Kharsholmer Schlund | Dorunischer Archivar | 3 |
| LORE_FRG_018 | R02 | Der Erstchor versammelt sich – Kharsholmer Schlund | Erstchor | 4 |
| LORE_FRG_019 | R02 | Die Arena über dem Schlaf – Kharsholmer Schlund | Erstchor | 4 |
| LORE_FRG_020 | R02 | Ilens Zweifel – Kharsholmer Schlund | Ilen | 5 |
| LORE_FRG_021 | R02 | Maedryns Versprechen – Kharsholmer Schlund | Archon Maedryn | 6 |
| LORE_FRG_022 | R02 | Die letzte Nacht vor der Stille – Kharsholmer Schlund | Ilen | 7 |
| LORE_FRG_023 | R02 | Der Riegel – Kharsholmer Schlund | Ilen | 8 |
| LORE_FRG_024 | R02 | Was danach bleibt – Kharsholmer Schlund | Ilen | 9 |
| LORE_FRG_025 | R03 | Das erste Lied – Versunkener Turm | Erstchor | 0 |
| LORE_FRG_026 | R03 | Ein Kinderlied – Versunkener Turm | Alltagsstimme | 0 |
| LORE_FRG_027 | R03 | Die Stimme dieses Landes – Versunkener Turm | Erstchor | 1 |
| LORE_FRG_028 | R03 | Warnung der Hüter – Versunkener Turm | Dorunische Archivarin | 2 |
| LORE_FRG_029 | R03 | Der Missklang beginnt – Versunkener Turm | Dorunischer Archivar | 3 |
| LORE_FRG_030 | R03 | Der Erstchor versammelt sich – Versunkener Turm | Erstchor | 4 |
| LORE_FRG_031 | R03 | Die Arena über dem Schlaf – Versunkener Turm | Erstchor | 4 |
| LORE_FRG_032 | R03 | Ilens Zweifel – Versunkener Turm | Ilen | 5 |
| LORE_FRG_033 | R03 | Maedryns Versprechen – Versunkener Turm | Archon Maedryn | 6 |
| LORE_FRG_034 | R03 | Die letzte Nacht vor der Stille – Versunkener Turm | Ilen | 7 |
| LORE_FRG_035 | R03 | Der Riegel – Versunkener Turm | Ilen | 8 |
| LORE_FRG_036 | R03 | Was danach bleibt – Versunkener Turm | Ilen | 9 |
| LORE_FRG_037 | R04 | Das erste Lied – Sonnenhof | Erstchor | 0 |
| LORE_FRG_038 | R04 | Ein Kinderlied – Sonnenhof | Alltagsstimme | 0 |
| LORE_FRG_039 | R04 | Die Stimme dieses Landes – Sonnenhof | Erstchor | 1 |
| LORE_FRG_040 | R04 | Warnung der Hüter – Sonnenhof | Dorunische Archivarin | 2 |
| LORE_FRG_041 | R04 | Der Missklang beginnt – Sonnenhof | Dorunischer Archivar | 3 |
| LORE_FRG_042 | R04 | Der Erstchor versammelt sich – Sonnenhof | Erstchor | 4 |
| LORE_FRG_043 | R04 | Die Arena über dem Schlaf – Sonnenhof | Erstchor | 4 |
| LORE_FRG_044 | R04 | Ilens Zweifel – Sonnenhof | Ilen | 5 |
| LORE_FRG_045 | R04 | Maedryns Versprechen – Sonnenhof | Archon Maedryn | 6 |
| LORE_FRG_046 | R04 | Die letzte Nacht vor der Stille – Sonnenhof | Ilen | 7 |
| LORE_FRG_047 | R04 | Der Riegel – Sonnenhof | Ilen | 8 |
| LORE_FRG_048 | R04 | Was danach bleibt – Sonnenhof | Ilen | 9 |
| LORE_FRG_049 | R05 | Das erste Lied – Kraterherz | Erstchor | 0 |
| LORE_FRG_050 | R05 | Ein Kinderlied – Kraterherz | Alltagsstimme | 0 |
| LORE_FRG_051 | R05 | Die Stimme dieses Landes – Kraterherz | Erstchor | 1 |
| LORE_FRG_052 | R05 | Warnung der Hüter – Kraterherz | Dorunische Archivarin | 2 |
| LORE_FRG_053 | R05 | Der Missklang beginnt – Kraterherz | Dorunischer Archivar | 3 |
| LORE_FRG_054 | R05 | Der Erstchor versammelt sich – Kraterherz | Erstchor | 4 |
| LORE_FRG_055 | R05 | Die Arena über dem Schlaf – Kraterherz | Erstchor | 4 |
| LORE_FRG_056 | R05 | Ilens Zweifel – Kraterherz | Ilen | 5 |
| LORE_FRG_057 | R05 | Maedryns Versprechen – Kraterherz | Archon Maedryn | 6 |
| LORE_FRG_058 | R05 | Die letzte Nacht vor der Stille – Kraterherz | Ilen | 7 |
| LORE_FRG_059 | R05 | Der Riegel – Kraterherz | Ilen | 8 |
| LORE_FRG_060 | R05 | Was danach bleibt – Kraterherz | Ilen | 9 |
| LORE_FRG_061 | R06 | Das erste Lied – Thal'assyrs Rippe | Erstchor | 0 |
| LORE_FRG_062 | R06 | Ein Kinderlied – Thal'assyrs Rippe | Alltagsstimme | 0 |
| LORE_FRG_063 | R06 | Die Stimme dieses Landes – Thal'assyrs Rippe | Erstchor | 1 |
| LORE_FRG_064 | R06 | Warnung der Hüter – Thal'assyrs Rippe | Dorunische Archivarin | 2 |
| LORE_FRG_065 | R06 | Der Missklang beginnt – Thal'assyrs Rippe | Dorunischer Archivar | 3 |
| LORE_FRG_066 | R06 | Der Erstchor versammelt sich – Thal'assyrs Rippe | Erstchor | 4 |
| LORE_FRG_067 | R06 | Die Arena über dem Schlaf – Thal'assyrs Rippe | Erstchor | 4 |
| LORE_FRG_068 | R06 | Ilens Zweifel – Thal'assyrs Rippe | Ilen | 5 |
| LORE_FRG_069 | R06 | Maedryns Versprechen – Thal'assyrs Rippe | Archon Maedryn | 6 |
| LORE_FRG_070 | R06 | Die letzte Nacht vor der Stille – Thal'assyrs Rippe | Ilen | 7 |
| LORE_FRG_071 | R06 | Der Riegel – Thal'assyrs Rippe | Ilen | 8 |
| LORE_FRG_072 | R06 | Was danach bleibt – Thal'assyrs Rippe | Ilen | 9 |
| LORE_FRG_073 | R07 | Das erste Lied – Gletscherdom | Erstchor | 0 |
| LORE_FRG_074 | R07 | Ein Kinderlied – Gletscherdom | Alltagsstimme | 0 |
| LORE_FRG_075 | R07 | Die Stimme dieses Landes – Gletscherdom | Erstchor | 1 |
| LORE_FRG_076 | R07 | Warnung der Hüter – Gletscherdom | Dorunische Archivarin | 2 |
| LORE_FRG_077 | R07 | Der Missklang beginnt – Gletscherdom | Dorunischer Archivar | 3 |
| LORE_FRG_078 | R07 | Der Erstchor versammelt sich – Gletscherdom | Erstchor | 4 |
| LORE_FRG_079 | R07 | Die Arena über dem Schlaf – Gletscherdom | Erstchor | 4 |
| LORE_FRG_080 | R07 | Ilens Zweifel – Gletscherdom | Ilen | 5 |
| LORE_FRG_081 | R07 | Maedryns Versprechen – Gletscherdom | Archon Maedryn | 6 |
| LORE_FRG_082 | R07 | Die letzte Nacht vor der Stille – Gletscherdom | Ilen | 7 |
| LORE_FRG_083 | R07 | Der Riegel – Gletscherdom | Ilen | 8 |
| LORE_FRG_084 | R07 | Was danach bleibt – Gletscherdom | Ilen | 9 |
| LORE_FRG_085 | R08 | Das erste Lied – Säulenfeld Thae'Luun | Erstchor | 0 |
| LORE_FRG_086 | R08 | Ein Kinderlied – Säulenfeld Thae'Luun | Alltagsstimme | 0 |
| LORE_FRG_087 | R08 | Die Stimme dieses Landes – Säulenfeld Thae'Luun | Erstchor | 1 |
| LORE_FRG_088 | R08 | Warnung der Hüter – Säulenfeld Thae'Luun | Dorunische Archivarin | 2 |
| LORE_FRG_089 | R08 | Der Missklang beginnt – Säulenfeld Thae'Luun | Dorunischer Archivar | 3 |
| LORE_FRG_090 | R08 | Der Erstchor versammelt sich – Säulenfeld Thae'Luun | Erstchor | 4 |
| LORE_FRG_091 | R08 | Die Arena über dem Schlaf – Säulenfeld Thae'Luun | Erstchor | 4 |
| LORE_FRG_092 | R08 | Ilens Zweifel – Säulenfeld Thae'Luun | Ilen | 5 |
| LORE_FRG_093 | R08 | Maedryns Versprechen – Säulenfeld Thae'Luun | Archon Maedryn | 6 |
| LORE_FRG_094 | R08 | Die letzte Nacht vor der Stille – Säulenfeld Thae'Luun | Ilen | 7 |
| LORE_FRG_095 | R08 | Der Riegel – Säulenfeld Thae'Luun | Ilen | 8 |
| LORE_FRG_096 | R08 | Was danach bleibt – Säulenfeld Thae'Luun | Ilen | 9 |
| LORE_FRG_097 | R09 | Das erste Lied – Resonanzkammer | Erstchor | 0 |
| LORE_FRG_098 | R09 | Ein Kinderlied – Resonanzkammer | Alltagsstimme | 0 |
| LORE_FRG_099 | R09 | Die Stimme dieses Landes – Resonanzkammer | Erstchor | 1 |
| LORE_FRG_100 | R09 | Warnung der Hüter – Resonanzkammer | Dorunische Archivarin | 2 |
| LORE_FRG_101 | R09 | Der Missklang beginnt – Resonanzkammer | Dorunischer Archivar | 3 |
| LORE_FRG_102 | R09 | Der Erstchor versammelt sich – Resonanzkammer | Erstchor | 4 |
| LORE_FRG_103 | R09 | Die Arena über dem Schlaf – Resonanzkammer | Erstchor | 4 |
| LORE_FRG_104 | R09 | Ilens Zweifel – Resonanzkammer | Ilen | 5 |
| LORE_FRG_105 | R09 | Maedryns Versprechen – Resonanzkammer | Archon Maedryn | 6 |
| LORE_FRG_106 | R09 | Die letzte Nacht vor der Stille – Resonanzkammer | Ilen | 7 |
| LORE_FRG_107 | R09 | Der Riegel – Resonanzkammer | Ilen | 8 |
| LORE_FRG_108 | R09 | Was danach bleibt – Resonanzkammer | Ilen | 9 |
| LORE_FRG_109 | R10 | Das erste Lied – Sternenarena | Erstchor | 0 |
| LORE_FRG_110 | R10 | Ein Kinderlied – Sternenarena | Alltagsstimme | 0 |
| LORE_FRG_111 | R10 | Die Stimme dieses Landes – Sternenarena | Erstchor | 1 |
| LORE_FRG_112 | R10 | Warnung der Hüter – Sternenarena | Dorunische Archivarin | 2 |
| LORE_FRG_113 | R10 | Der Missklang beginnt – Sternenarena | Dorunischer Archivar | 3 |
| LORE_FRG_114 | R10 | Der Erstchor versammelt sich – Sternenarena | Erstchor | 4 |
| LORE_FRG_115 | R10 | Die Arena über dem Schlaf – Sternenarena | Erstchor | 4 |
| LORE_FRG_116 | R10 | Ilens Zweifel – Sternenarena | Ilen | 5 |
| LORE_FRG_117 | R10 | Maedryns Versprechen – Sternenarena | Archon Maedryn | 6 |
| LORE_FRG_118 | R10 | Die letzte Nacht vor der Stille – Sternenarena | Ilen | 7 |
| LORE_FRG_119 | R10 | Der Riegel – Sternenarena | Ilen | 8 |
| LORE_FRG_120 | R10 | Was danach bleibt – Sternenarena | Ilen | 9 |

Die vollständigen Texte und Skripte entstehen in K44–K46 (Story) und werden in `Data/Lore/` als Lokalisierungsschlüssel `LORE_FRG_###_TEXT` geführt.

---

## 7. Die Kodex-Linse

Die **Kodex-Linse** ist die Kamera des Wärters (CANON §6), ein dorunisches Instrument, das Licht *und* Klang festhält.

| Funktion | Detail |
|---|---|
| Aufruf | Steuerkreuz ↑ (Oberwelt), jederzeit außerhalb von Kämpfen; im Kampf nur im Fotomodus-Pause (Solo) |
| Zoom | 1×–8× (Linsen-Upgrades K40: 12×, Nachtlinse, Makro) |
| Fokus | Autofokus auf Echos; manueller Fokus mit Tiefenschärfe |
| Erkennung | Echos im Bild werden benannt (ab Stufe 1), Verhaltensanimationen markiert |
| Klangaufnahme | Jedes Foto speichert 3 s Umgebungsklang (Album spielt sie ab) |
| Linsen | Standard, Nachtlinse (Nacht ohne Licht), Makrolinse (XS-Echos), Spiegellinse (Mirrowisp, §10) |

---

## 8. Fotobewertung

Fotos werden mit **1–4 Sternen** bewertet; die Bewertung ist transparent (Detailanzeige nach dem Auslösen).

| Kriterium | Punkte | Erklärung |
|---|---|---|
| Motiv | 0–30 | Echo im Bild (Größe 10–60 % der Bildfläche optimal), scharf |
| Verhalten | 0–25 | Verhaltensanimation sichtbar (Merkmal der Art) |
| Komposition | 0–15 | Drittel-Regel, Blickrichtung, freie Sicht |
| Seltenheit | 0–15 | Seltenheit der Art, Morph +15 |
| Moment | 0–15 | passendes Wetter/Tageszeit (Spawn-Bedingung), Gruppenfoto (≥ 3 Echos), Begleiter-Interaktion |

| Sterne | Punkte |
|---|---|
| ★ | 20–44 |
| ★★ | 45–64 |
| ★★★ | 65–84 |
| ★★★★ | ≥ 85 |

**Echos reagieren auf die Linse:** Neugierige Echos posieren (+5 Komposition), scheue fliehen bei Annäherung, verspielte springen ins Bild. Fotos stören die Annäherung (K36) nicht, wenn der Spieler unentdeckt bleibt.

---

## 9. Fotomodus und Album

| Funktion | Detail |
|---|---|
| Fotomodus | pausiert die Welt (Solo); freie Kamera (Radius 8 m um den Wärter), Filter, Rahmen, Echo-Posen für eigene Echos, Tageszeit-Vorschau aus |
| Album | 500 Fotos (Erweiterung über Akademie-Ruf); Ordner je Art; Fotos mit Herkunftsdaten (Ort, Wetter, Datum) |
| Teilen | Export als Bilddatei; Online-Pinnwand der Gilde (K60) |
| Profil | Lieblingsfoto im Spielerprofil (K03) |
| Fotoaufträge | Akademie- und Kontor-Aufträge (K13 §4) mit Sternenanforderung |

---

## 10. Fotografie-Meisterschaft und Mirrowisp

Das mythische **Mirrowisp** (Kristall/Geist, CANON §34) erscheint nur auf Fotos: „Ein Spiegelbild, das sich selbstständig gemacht hat.“

| Schritt | Bedingung |
|---|---|
| 1 Spuren | Nach 50 Fotos mit ≥ 3 Sternen erscheinen in einzelnen Spiegelungen (Wasser, Glas, Eis) auf Fotos flüchtige Schemen – nur im Album sichtbar |
| 2 Fotografie-Meisterschaft | 100 Arten mit ≥ 3 Sternen fotografiert **und** 20 Verhaltensfotos (4 Sterne) **und** alle 10 Regionen in ihrer exklusiven Tagesphasen-Aktivität (DR-32) fotografiert |
| 3 Spiegellinse | Akademie (Rektor Venn – nach Akt III die kommissarische Leitung) übergibt die Spiegellinse; Questreihe „Der Blick hinter das Glas“ (K62) |
| 4 Begegnung | Mit der Spiegellinse ist Mirrowisp in Spiegelungen fotografierbar; nach 3 Fotos an verschiedenen Orten öffnet sich eine Spiegelwelt-Begegnung (Kampf + Bindung, K35/K36) |

Solo-Weg garantiert (CANON §8); kein Online-Element nötig.

---

## 11. Belohnungen und Wärter-EP

Kodex trägt 20 % der Wärter-EP (CANON §18). Verteilung:

| Ereignis | Wärter-EP (Basis) |
|---|---|
| Kodex-Stufe 1 | 10 |
| Kodex-Stufe 2 | 30 |
| Kodex-Stufe 3 | 60 |
| Kodex-Stufe 4 | 120 |
| Klangfragment | 80 |
| Foto ★★★ (erstes je Art) | 20 |
| Foto ★★★★ (erstes je Art) | 40 |

**Kodex-Meilensteine** (Gesamtfortschritt): 10 % Resonanzsinn-Reichweite +20 m · 25 % Makrolinse · 50 % Nachtlinse · 75 % Titel „Gelehrte/r der Echos“ · 100 % Kodex in Goldprägung + Akademie-Ehrenmitgliedschaft (Kosmetik).

---

## 12. Code

```cpp
// GF_Research – Kodex-Fortschritt
USTRUCT() struct FKodexSpeciesState
{
    GENERATED_BODY()
    UPROPERTY(SaveGame) uint8 Stage = 0;                    // 0–4
    UPROPERTY(SaveGame) FGameplayTagContainer ObservedTraits; // Behavior.*
    UPROPERTY(SaveGame) uint16 BattlesAgainst = 0;
    UPROPERTY(SaveGame) uint8 BestPhotoStars = 0;
    UPROPERTY(SaveGame) uint8 TasksDone = 0;                // Bitmaske 3 Aufgaben
};

void UKodexService::OnObservation(FPrimaryAssetId Species, FGameplayTag Trait)
{
    FKodexSpeciesState& S = State.FindOrAdd(Species);
    if (S.ObservedTraits.HasTagExact(Trait)) return;
    S.ObservedTraits.AddTag(Trait);
    Bus->Broadcast(TAG_Kodex_Observed, FKodexObservedMessage{ Species, Trait });
    Reevaluate(Species, S);                                // Stufenbedingungen (K39 §2), Aufgaben (KodexTasks.csv)
}

int32 UKodexService::BondResonanceBonus(FPrimaryAssetId Species) const
{
    static constexpr int32 Bonus[5] = { 0, 60, 120, 180, 240 };  // K36 §3
    const FKodexSpeciesState* S = State.Find(Species);
    return Bonus[S ? S->Stage : 0];
}
```

Die Fotobewertung läuft auf dem Render-Thread-Readback einer **Klassifizierungsmaske** (Echo-IDs je Pixel, 1/8 Auflösung) – keine KI-Bilderkennung nötig; deterministisch und plattformgleich.

---

## 13. Tests und Telemetrie

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Kodex.Stages` | Stufenbedingungen inkl. Evolution setzt ≥ 3 |
| `…Kodex.Tasks` | 768 Aufgaben referenzieren gültige Merkmale/Bedingungen (CI-Validator) |
| `…Lore.TruthLevel` | Fragmente oberhalb der Story-Ebene verzerrt (L-01) |
| `…Photo.Score` | Bewertung reproduzierbar (Maske), Sternengrenzen |
| `Aethris.Func.Kodex.Coverage` | jede Art erreicht Stufe 4 im Bot-Lauf (Bedingungen erfüllbar, DR-33) |

**Telemetrie:** Anteil Spieler mit ≥ 1 Beobachtung in der ersten Spielstunde (Ziel ≥ 80 %), Kodex-Fortschritt bei Story-Ende (Ziel Median 35 %), Fotos je Spielstunde, Fragment-Fundquote.

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-143 | Kodex-Aufgaben aus Artdaten generiert (3 je Art) | Konsistenz, DR-02/DR-33, kein Handpflegeaufwand für 768 Aufgaben | handgeschriebene Aufgaben (inkonsistent) |
| ADR-144 | Beobachtung = Merkmal während Ausführung 3 s unentdeckt im Resonanzsinn | Aufmerksamkeit belohnen, Ökologie sichtbar | Beobachtung durch bloßes Anschauen |
| ADR-145 | Klangfragmente als 10 × 12 Themenraster mit Wahrheitsebenen | Jede Region erzählt die ganze Geschichte aus eigener Sicht; L-01 einhaltbar | lineare Fragmentkette (Reihenfolgezwang) |
| ADR-146 | Fotobewertung über Klassifizierungsmaske | deterministisch, günstig, plattformgleich | Bild-KI (teuer, nicht reproduzierbar) |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §146 | Kodex-Stufen Gesichtet / Beobachtet / Erforscht / Verstanden mit Bedingungen und Freischaltungen (K39 §2); Evolution setzt ≥ 3; 768 Kodex-Aufgaben (`KodexTasks.csv`) | LOCKED |
| §147 | Resonanzsinn-Ebenen (Frequenz 60 m, Stimmung 40 m, Spuren 30 m, Verhalten, Nester); Beobachtung = 3 s Fokus unentdeckt während Ausführung | LOCKED |
| §148 | 120 Klangfragmente (`LoreEntries.csv`, `LORE_FRG_001–120`): 10 Regionen × 12 Themen, Wahrheitsebenen 0–9; Ebene ≥ 4 an Schlafstätten; L-01-Verzerrung | LOCKED (Texte → K44–K46) |
| §149 | Kodex-Linse (Zoom, Linsen, Klangaufnahme), Fotobewertung 5 Kriterien → 1–4 Sterne (20/45/65/85), Album 500 | LOCKED |
| §150 | Fotografie-Meisterschaft (100 Arten ★★★, 20 Verhaltensfotos ★★★★, 10 Regionen-Tagesphasen) → Spiegellinse → Mirrowisp; Kodex-Wärter-EP und Meilensteine | LOCKED |
| §10 | ADR-143 – ADR-146 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Forschung als gleichwertiger Loop, Werkzeuge
- [x] Vier Kodex-Stufen mit Bedingungen und Freischaltungen
- [x] 768 Kodex-Aufgaben aus Artdaten (Daten + Generator)
- [x] Resonanzsinn und Beobachtungsregel
- [x] 120 Klangfragmente mit Wahrheitsebenen (Daten)
- [x] Kodex-Linse, Fotobewertung, Fotomodus, Album
- [x] Fotografie-Meisterschaft → Mirrowisp
- [x] Wärter-EP, Meilensteine, Code, Tests, Telemetrie
- [x] ADR-143 – ADR-146, CANON §146–§150

➡️ **Nächstes Kapitel: K40 – Ausrüstung, Reittiere und Traversal (löst Q11).**
