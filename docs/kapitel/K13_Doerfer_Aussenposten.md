# K13 · Dörfer & Außenposten

| Feld | Wert |
|---|---|
| Dokument | Kapitel 13 von 68 · World Bible, Teil VII |
| Version | 1.0 |
| Owner | Level Designer (Settlement Lead) |
| Mitwirkende | Quest Designer, Narrative Writer, AI Engineer, Economy Designer |
| Baut auf | K03 §3 (Dienste), K08 (Karte), K09/K10 (Siedlungsnamen), K11/K12 (Template, Muster) |
| Status | ✅ Freigegeben |
| Im Repository | `tools/place_settlements.py` (Platzierung, Mindestabstand ≥ 400 m), Koordinaten in `Data/World/Settlements.csv`, `Data/Quests/ContractTemplates.csv` |
| Neue Kanon-Einträge | CANON §57 (Dörfer), §58 (Außenposten), §59 (Aufträge), §60 (Siedlungszustände & Ereignisse) |

---

## Inhalt

1. [Rolle der kleinen Siedlungen](#1-rolle-der-kleinen-siedlungen)
2. [Die 22 Dörfer](#2-die-22-dörfer)
3. [Die 30 Außenposten](#3-die-30-außenposten)
4. [Aufträge (wiederholbare Aufgaben)](#4-aufträge-wiederholbare-aufgaben)
5. [Siedlungszustände: Bedroht – Stabil – Blühend](#5-siedlungszustände-bedroht--stabil--blühend)
6. [Siedlungs-Ereignisse](#6-siedlungs-ereignisse)
7. [Baukasten & Produktionsplan](#7-baukasten--produktionsplan)
8. [Code](#8-code)
9. [Decision Records](#9-decision-records)
10. [Kanon-Updates](#10-kanon-updates)
11. [Kapitel-Checkliste](#11-kapitel-checkliste)

---

## 1. Rolle der kleinen Siedlungen

| Typ | Spielfunktion | Erzählfunktion | Größe (Durchmesser) | NPCs (benannt / Ambient) |
|---|---|---|---|---|
| **Dorf** (22) | Rast, Heilung, Grundhandel, Nebenquests, Region „bewohnt“ wirken lassen | Lokale Kultur im Kleinen, Geschichten einzelner Menschen | 120–250 m | 8–16 / 20–50 |
| **Außenposten** (30) | Schnellreise (Wildstein ≤ 150 m), Feldbrunnen, Aufträge, Lager, Wanderhändler | Präsenz der Fraktionen in der Wildnis, Gefahr/Abenteuer | 30–80 m | 2–5 / 0–6 |

**Verteilung (geprüft durch `tools/place_settlements.py`):** Jede Region hat 2–3 Dörfer und 3 Außenposten, mit **≥ 0,54 km** Abstand zwischen allen Siedlungen einer Region (Mindestanforderung 0,4 km). Zusammen mit den Resonanzsteinen und Klangbrunnen erfüllen sie DR-30 (≤ 800 m zwischen Heilpunkten) und K08 §8 (≤ 900 m zu Steinen).

---

## 2. Die 22 Dörfer

Einheitliches Kurzprofil: Lage · Einwohner · Charakter · Dienste · Schlüssel-NPC · Quest-Haken · Echo-Haken (seltene Begegnung in der Nähe). Dienste-Kürzel: **B** Klangbrunnen, **S** Resonanzstein, **H** Händler (Anzahl), **Q** Questbrett, **W** Werkbank, **K** Kessel, **G** Gasthaus, **P** Hain-Portal.

### 2.1 R01 Verdanthain

| Dorf | Lage (km) | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Lindwiesen** | 1,9 / 5,7 | 240 | Startdorf: Obstwiesen, Mühle an der Linn, Dorfplatz mit Linde; Elternhaus des Spielers | B S H2 Q W K G | Ysolde Varn (wohnt am Waldrand), Bäckerin Hedda, Müller Jost | Prolog, „Der Brotdieb“, Lindwiesen-Fest | Brotstehlendes Klein-Echo (Onboarding) |
| **Moosgrund** | 3,7 / 4,5 | 310 | Köhler- und Pilzdorf in einer moosigen Senke, Rauch über den Bäumen | B S H2 Q W K G P | Köhlerin Brida | „Die Pilzringe“ (Nacht-Rätsel), Köhler-Echos | Pilzring-Geist-Echo (Nacht, Nebel) |

### 2.2 R02 Kharsgrat

| Dorf | Lage | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Brakkfels** | 2,7 / 1,5 | 420 | Bergbaudorf des Klans Brakk an der Westflanke, Lorenbahnen | B S H2 Q W G P | Vorarbeiter Ulf Brakk (Hraldas Neffe) | „Lorenlauf“ (Traversal), Minenunglück | Gesteinsfresser in alten Stollen |
| **Hrallsted** | 5,7 / 1,7 | 280 | Hirtendorf des Klans Hrall, Almwiesen, Käserei | B S H2 Q K G | Hirtin Svala | „Die verlorene Herde“, Käse für Kharsholm (Lieferung) | Bergziegen-Alpha bei Gewitter |

### 2.3 R03 Morvenmoor

| Dorf | Lage | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Fennhaven** | 5,9 / 4,1 | 190 | Riedgras-Fischerdorf auf Inseln, Reusen, Räucherhütten | B S H1 Q K G | Reusenmacher Lorcan | „Was in der Reuse war“ (Geist-Mysterium) | Leuchtkäfer-Schwarm (Regen + Abend) |
| **Duvreth** | 4,5 / 4,5 | 230 | Kräuterdorf am Rand der Stillezone (Akt I), halb evakuiert | B S H2 Q K G P | Moorweise Ama Duvreth (Schwester der Fährmeisterin) | „Zurück nach Duvreth“ (Stillezone, Bewohner kehren nach Heilung zurück – §5) | Fäulnis-Zersetzer (Gift) im Uferschlamm |

### 2.4 R04 Sahrun-Weite

| Dorf | Lage | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Harrâd** | 2,3 / 6,1 | 520 | Oasendorf (Heimat der Arenameisterin), Palmengärten, Kanäle | B S H3 Q W K G P | Brunnenwächterin Nadira | „Der Brunnen schweigt“ | Oasen-Flut-Echos (Abend) |
| **Mirsaan** | 5,1 / 6,1 | 260 | Dorf an den Singenden Dünen, Instrumentenbauer | B S H2 Q W G | Dünenbauer Kesh | „Das Lied der Dünen“ (Klangrätsel) | Sandschwimmer bei Sandsturm |
| **Wanderdorf Ashurim** | Route (Start 6,3 / 5,9) | 150 | Karawanendorf auf Lasttier-Echos; zieht alle 3 Spieltage über 4 Lager | S (mobil: Stein reist mit) H3 Q K G | Karawanenführer Imran | „Folge Ashurim“ (zeitgebundene Kette) | Lasttier-Echo-Herde (reitbar) |

**Ashurim-Route (LOCKED):** Lager A (6,3/5,9) → B Glasebene-Rand (3,5/5,5) → C Harrâd-Nähe (2,6/5,8) → D Mirsaan-Nähe (4,7/6,0) → A; Aufenthalt je ~18 Spielstunden.

### 2.5 R05 Ignareth

| Dorf | Lage | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Vorthax** | 7,3 / 2,9 | 330 | Schlackenstromdorf, Häuser auf Basaltpfeilern, Erzwäscher | B S H2 Q W G P | Erzwäscherin Thessa | „Der Strom dreht“ (Ausbruchstag-Evakuierung) | Glutsalamander-Kolonie |
| **Kaldra** | 7,5 / 3,9 | 210 | Thermaldorf an der Ostküste, heiße Quellen, Kurgäste | B S H2 Q K G | Kurwirtin Malva | „Quellen der Ruhe“ (Hilfe für Klangpest-Überlebende auf Kur) | Dampf-Echos an Fumarolen (Nacht) |

### 2.6 R06 Saltrand

| Dorf | Lage | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Tangwerft** | 1,3 / 2,9 | 360 | Werftdorf in der Bucht, Tangernte, Seilerei | B S H2 Q W G P | Seilermeisterin Marlene | „Ein Schiff aus Tang“ | Tangwald-Echos (Flut) |
| **Möwenhuk** | 1,9 / 3,7 | 180 | Klippendorf, Vogelwarte, Leuchtfeuer-Tradition | B S H1 Q K G | Vogelkundler Okko | „Die Möwen schweigen“ (Stillezone-Vorbote) | Seevogel-Kolonie (Flugreiten-Horst) |
| **Treibdorf Flottholm** | 1,3 / 4,9 (Ebbe) / 1,1 / 4,6 (Flut) | 140 | Schwimmendes Floßdorf, wandert mit der Gezeit | B S H2 Q K G | Floßälteste Ebba | „Flottholms Anker“ | Riffschwärme unter dem Dorf |

### 2.7 R07 Hvitfell

| Dorf | Lage | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Fjallstad** | 2,9 / 1,1 | 250 | Hirtendorf am Pass, nahe Kloster Schweigfels; viele Ordenssympathisanten | B S H2 Q K G P | Hirte Leif (Bruder einer Novizin) | „Die Schwester im Kloster“ (Familiendrama, Entscheidung) | Rentier-Herde (Aurora) |
| **Eiðvik-Neu** | 5,5 / 1,1 | 160 | Wiederaufgebautes Dorf neben den Klangpest-Ruinen | B S H1 Q W G | Bootsbauerin Halla (Überlebende) | „Was die Pest nahm“ (Erinnerungseis) | Geist-Echos in den alten Ruinen (Nebel + Nacht) |

### 2.8 R08 Ael'Dorun

| Dorf | Lage | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Thae'Luun** | 4,3 / 3,9 | 300 | Grabungsdorf im Säulenfeld, Zelte und restaurierte Häuser | B S H2 Q W G P | Grabungsleiterin Dr. Imke Vael (Nachfahrin des Taxonomen) | „Die Säule, die singt“ (Glyphenrätsel) | Konstrukt-Metall-Echos in Säulen |
| **Säulenrast** | 5,7 / 2,9 | 140 | Pilgerdorf mit Ordenskapelle, Rasthäuser | B S H1 Q K G | Kapellenhüter Bruder Odvar (Orden, spricht – Ausnahme vom Gelübde außerhalb des Klosters) | „Pilger der Stille“ (Ordenssicht verstehen) | Leere-Räuber am Zonenrand |

### 2.9 R09 Prismtiefen (unterirdisch)

| Dorf | Lage (Footprint) / Tiefe | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Glanzschacht** | 3,7 / 3,9, −120 m | 380 | Bergarbeiterdorf in einem alten Schacht, Grubenlampen | B S H2 Q W G P | Steiger Brannoc d. Ä. (Ilyx' Großvater) | „Der vergessene Stollen“ | Lithophagen-Kolonie |
| **Quarzgrund** | 1,9 / 2,5, −310 m | 120 | Tiefstes Dorf, Quarzschleifer, fast völlige Dunkelheit (Lichtrituale) | B S H1 Q K G | Schleiferin Nyx | „Licht für Quarzgrund“ (Dunkelheit-Mechanik) | Blinde Klang-Jäger (völlige Dunkelheit) |

### 2.10 R10 Nimbara

| Dorf | Lage / Höhe | Einw. | Charakter | Dienste | Schlüssel-NPC | Quest-Haken | Echo-Haken |
|---|---|---|---|---|---|---|---|
| **Lumeya** | 3,1 / 2,7, 1.650 m | 90 | Inseldorf der Sternkundigen, Außeninseln nur per Flugreiten | B S H1 Q K G | Sternkundige Elun | „Die verlorenen Sternkarten“ | Sternenfalter (Morgendämmerung) |
| **Wolkenrast** | 5,1 / 3,3, 1.500 m | 110 | Gondelstation und Windseglerdorf, Rastplatz der Windströme | B S H2 Q W G P | Windseglerin Ria | „Rennen im Windstrom“ | Wolkenwal-Herde |

**Summe Dörfer:** 22 · Einwohner ~5.560.

---

## 3. Die 30 Außenposten

Außenpostentypen (LOCKED): **WW** Wildwacht-Posten · **AK** Akademie-Station · **GK** Kontor-Handelsposten · **ZV** Zivil (Hütte, Lager, Biwak). Standarddienste aller Außenposten: Feldbrunnen (10 s Kanalisieren), Wildstein ≤ 150 m, Werkbank, Auftragsbrett, Zelt (Zeit vorspulen). Wanderhändler: an 50 % der Posten, rotierend nach Wochentag (Spielzeit).

| ID | Region | Name | Lage | Typ | Besetzung | Spezial-Aufträge | Besonderheit |
|---|---|---|---|---|---|---|---|
| SET_O_FARNWACHT | R01 | Farnwacht | 2,3 / 4,1 | WW | Rangerin Ivo + 2 | Rettung, Beruhigen | Erster Außenposten (Onboarding-nah), Tutorial für Aufträge |
| SET_O_LINNFURTPOSTEN | R01 | Linnfurt-Posten | 2,7 / 5,5 | ZV | Fährmann Bert | Lieferung, Eskorte | Furt über die Linn, Fährseil |
| SET_O_URALTHAINLAGER | R01 | Uralthain-Lager | 1,9 / 4,9 | AK | Botanikerin Lise | Beobachten, Foto | Seltene Arten Uralthain |
| SET_O_PASSWACHTNORD | R02 | Passwacht Nord | 5,7 / 2,3 | WW | Wächter Hrok + 3 | Eskorte, Beruhigen | Pass nach Ignareth/Hvitfell |
| SET_O_ERZGRATHUETTE | R02 | Erzgrat-Hütte | 3,3 / 2,1 | GK | Erzhändler Lasse | Sammeln, Lieferung | Erzankauf zu Bestpreisen |
| SET_O_GROLLHORNBIWAK | R02 | Grollhorn-Biwak | 4,9 / 1,7 | ZV | Bergführerin Aud | Vermessen | Kälte-Schutzzone am Gipfelweg |
| SET_O_CORRACHSTELZENPOSTEN | R03 | Corrach-Stelzenposten | 6,1 / 5,1 | WW | Ranger Cael | Rettung (Nebel) | Nebelwald-Eingang |
| SET_O_RIEDWACHT | R03 | Riedwacht | 5,3 / 5,5 | ZV | Torfstecher Mav | Sammeln | Torfkohle-Lager |
| SET_O_SENKENLAGER | R03 | Senkenlager | 4,7 / 5,1 | AK | Forscher Aled | Beobachten, Stille | Zugang Versunkene Senke |
| SET_O_GLASEBENETURM | R04 | Glasebene-Turm | 3,1 / 5,7 | AK | Lichtforscherin Zahra | Vermessen, Foto | Aussichtsturm über der Glasebene |
| SET_O_DUENENWACHT | R04 | Dünenwacht | 3,9 / 4,9 | WW | Wächter Tarek + 2 | Eskorte (Karawanen) | Nordrand, Sandsturm-Gate (Akt II) |
| SET_O_PLATEAULAGER | R04 | Plateau-Lager | 5,7 / 6,1 | GK | Händlerin Laleh | Lieferung | Rastplatz am Plateau-Fuß |
| SET_O_ASCHEHUETTE | R05 | Aschehütte | 6,3 / 2,9 | ZV | Einsiedler Borr | Rettung | Asche-Schutzzone, Ascheschleier-Gate |
| SET_O_OBSIDIANWACHT | R05 | Obsidianwacht | 6,3 / 3,9 | WW | Lavawächterin Edda | Beruhigen | Eingang Obsidianklamm |
| SET_O_KRATERRANDPOSTEN | R05 | Kraterrand-Posten | 6,9 / 4,3 | AK | Vulkanologe Fenn | Vermessen (Ausbruchsprognose) | Kündigt Ausbrüche 1 Spieltag vorher an |
| SET_O_LEUCHTFELSENWACHT | R06 | Leuchtfelsen-Wacht | 0,7 / 3,1 | ZV | Leuchtturmwärterin Gesa | Rettung (Sturm) | Leuchtturm, Aussichtspunkt |
| SET_O_DUENENKATE | R06 | Dünenkate | 1,3 / 4,1 | GK | Strandhändler Pieter | Sammeln, Lieferung | Treibgut-Handel |
| SET_O_RIFFPOSTEN | R06 | Riffposten | 1,3 / 3,5 | WW | Taucherin Rieke | Rettung (Unterwasser) | Startpunkt Riffgrund |
| SET_O_GLETSCHERWACHT | R07 | Gletscherwacht | 4,9 / 0,5 | WW | Gletscherführer Bjarke | Eskorte, Rettung | Spaltenrettung |
| SET_O_PASSHUETTE | R07 | Passhütte | 4,7 / 1,1 | ZV | Hüttenwirtin Unn | Lieferung | Pass-Schneesturm-Gate (Akt II) |
| SET_O_ISVALDTINDBIWAK | R07 | Isvaldtind-Biwak | 3,3 / 0,5 | AK | Glaziologin Tove | Vermessen | Höchster Lagerplatz (Kälte extrem draußen) |
| SET_O_GRABUNGSLAGERNORD | R08 | Grabungslager Nord | 5,1 / 2,7 | AK | Ausgräber Henrik | Vermessen, Foto | Glyphenfunde |
| SET_O_ARCHONTENWACHT | R08 | Archontenwacht | 5,3 / 3,7 | WW | Wächterin Aune | Stille, Beruhigen | Rand der großen Stillezone |
| SET_O_RUINENPFADPOSTEN | R08 | Ruinenpfad-Posten | 4,3 / 3,1 | ZV | Schatzsucher Rask (zwielichtig) | Rettung | Schatzsucher-Rivalen-Questlinie |
| SET_O_LIFTSTATIONKRATERRAND | R09 | Liftstation Kraterrand | 2,3 / 3,5 | GK | Liftmeister Arno | Lieferung | Aussichtspunkt ab Akt I; Lift ab Akt III |
| SET_O_KRISTALLSEELAGER | R09 | Kristallsee-Lager | 3,7 / 3,1 | AK | Limnologin Sif | Beobachten (Unterwasser) | Kristallsee-Fähre |
| SET_O_MISSKLANGWACHT | R09 | Missklang-Wacht | 2,7 / 2,3 | WW | Wächter Krell | Stille, Beruhigen | Dunst-Schutzzone vor den Adern |
| SET_O_KRONENWERFTWACHT | R10 | Kronenwerft-Wacht | 4,7 / 2,5 | ZV (Baumeister) | Wächter Oruma-Linie | Vermessen | Akt-III-Schauplatz |
| SET_O_STERNWARTEORUMA | R10 | Sternwarte Oruma | 3,5 / 3,7 | AK (nimbarisch) | Sternkundiger Talen | Foto (Nacht) | Mondphasen-Rätsel |
| SET_O_WINDANKER | R10 | Windanker | 4,5 / 3,7 | ZV | Windsegler Ivar | Eskorte (Windstrom) | Knoten dreier Windströme |

**Typverteilung (gezählt):** WW 9 · AK 8 · GK 4 · ZV 9 = 30 (nimbarische Posten als AK/ZV-Varianten). Wildwacht und zivile Hütten prägen die Wildnis, die Akademie die Forschungsorte, das Kontor die Handelsknoten.

---

## 4. Aufträge (wiederholbare Aufgaben)

### 4.1 Zweck

Aufträge (CANON §21: nicht Teil der 210 Nebenquests) liefern einen **verlässlichen Strom kleiner Ziele** zwischen den großen Quests – Belohnungsebene „3–10 Minuten“ der Pyramide (K02 §7.1). Sie sind kurz, systemisch erzeugt, nie Pflicht.

### 4.2 Vorlagen

Daten: `Data/Quests/ContractTemplates.csv` (10 Vorlagen).

| Vorlage | Art | Ziel | Quelle | ab Stufe | Abklingzeit | Basis-Sol | Fraktionsruf |
|---|---|---|---|---|---|---|---|
| CT_OBSERVE | Beobachten | 3 Verhaltensmerkmale einer Art | Brett, Posten | 0 | 1 Tag | 80 | Akademie |
| CT_PHOTO | Foto | Art mit ≥ 2 Sternen fotografieren | Brett, Posten | 0 | 1 | 90 | Akademie |
| CT_BOND | Binden | bestimmte Art binden (Freilassen erlaubt) | Brett | 0 | 2 | 140 | Wildwacht |
| CT_GATHER | Sammeln | 8 Einheiten regionaler Ressource | Brett, Posten | 0 | 1 | 70 | Kontor |
| CT_DELIVER | Lieferung | Ware in andere Siedlung der Region | Brett | 0 | 1 | 110 | Kontor |
| CT_ESCORT | Eskorte | Reisenden zum nächsten Posten | Posten | 1 | 2 | 160 | Wildwacht |
| CT_CALM | Beruhigen | aggressives Alphatier (Kampf **oder** Einstimmen) | Posten | 1 | 3 | 200 | Wildwacht |
| CT_RESCUE | Rettung | verirrtes Echo zurückbringen | Brett, Posten | 0 | 2 | 120 | Wildwacht |
| CT_SILENCE | Stille | kleine Stillezone-Nachwirkung lösen (nach Regionsheilung) | Posten | 2 | 3 | 240 | Wildwacht |
| CT_SURVEY | Vermessen | 3 Punkte mit Resonator vermessen | Posten | 1 | 2 | 130 | Akademie |

„Stufe“ = Siedlungszustand (§5): 0 Bedroht, 1 Stabil, 2 Blühend. Abklingzeit in Spieltagen (DR-23: Spielzeit statt Echtzeit).

### 4.3 Generierungsregeln

```
 Pro Siedlung: aktive Aufträge = 1 (Außenposten) / 2 (Dorf) / 3 (Stadt-Questbrett)
 Bei Spieltag-Wechsel:
   für jeden freien Slot:
     Kandidaten = Vorlagen mit Quelle passend ∧ MinTier ≤ Siedlungszustand ∧ nicht in Abklingzeit
     Gewichtung: Typ-Spezialität des Postens (Tabelle §3) ×3, Fraktion mit niedrigstem Spieler-Ruf ×1,5
     Ziel-Art/Ressource: aus Spawn-/Ressourcentabelle der Zone, bevorzugt Arten mit niedriger Kodex-Stufe (DR-01: Wissen fördern)
     Zufall: Fork(4) Loot-Strom (CANON §29) → deterministisch je Weltstand
 Belohnung = BaseSol × RewardScale(Zonenband-Mitte) (Kurve K42) + Wärter-EP + Kodex-Bonus (falls ResearchBonus=1)
```

**Regel DR-31 (neu):** Aufträge dürfen nie die einzige Quelle einer Belohnung sein (keine Exklusivgegenstände), damit sie nie zur Pflicht werden.

---

## 5. Siedlungszustände: Bedroht – Stabil – Blühend

Jedes Dorf und jeder Außenposten hat einen sichtbaren Zustand. Das verknüpft Story, Nebenquests und Welt (S1, DR-13).

| Zustand | Wert | Darstellung | Wirkung |
|---|---|---|---|
| **Bedroht** | 0 | Stillezone in der Nähe oder lokale Krise; Fenster verrammelt, weniger NPCs, gedämpfte Musik | Händler eingeschränkt (Sortiment −40 %), nur Aufträge Stufe 0 |
| **Stabil** | 1 | Normalzustand | volles Grundsortiment |
| **Blühend** | 2 | Nach Lösung der lokalen Nebenquest(s): Schmuck, Fest-Elemente, neue Bewohner, zusätzlicher Händler oder Dienst | +1 Händler (Sonderwaren), Aufträge Stufe 2, kleines Fest (einmalig), Wärter-EP-Bonus |

**Übergänge:** Bedroht → Stabil durch Regionsheilung (Hauptquest) **oder** lokale Quest; Stabil → Blühend durch die Dorf-Quest-Kette (Quest-Haken §2) bzw. 5 erledigte Aufträge (Außenposten). Rückfall gibt es nicht (Spielerleistung bleibt bestehen, DR-23).

Umsetzung über **Data Layer pro Siedlung** (`DL_SET_<Id>_State0/1/2`), gesteuert vom Siedlungs-Subsystem; Save-Fragment `Settlements`.

---

## 6. Siedlungs-Ereignisse

Kleine, systemische Ereignisse machen Siedlungen lebendig (DR-12/DR-26) – ohne Questlog-Last.

| Ereignis | Auslöser | Ablauf | Belohnung | Häufigkeit |
|---|---|---|---|---|
| **Echo-Besuch** | Zufall, Tageszeit | Ein wildes Echo wandert ins Dorf; NPCs reagieren (füttern, verscheuchen) | Kodex-Beobachtung, ggf. Bindung | 1 pro 2 Spieltage je Dorf |
| **Herde am Rand** | Ökologie (K52): Wanderroute kreuzt Siedlung | Herde zieht vorbei, Kinder schauen zu | Foto-Gelegenheit | situativ |
| **Händlerkarawane** | Wochenrhythmus | Wanderhändler mit seltener Ware für 1 Spieltag | Einkauf | 1 pro Woche je Region |
| **Wetterschaden** | Gewitter/Sandsturm | Dach beschädigt, NPC bittet um Material | Ruf, Sol | nach Unwetter, 20 % |
| **Alpha-Bedrohung** | Ökologie: Alpha-Revier überlappt | Wachen alarmiert, Auftrag CT_CALM erscheint sofort | Auftrag | selten |
| **Dorffest** | Zustand Blühend erreicht | Musik, Tanz, Echo-Parade | Wärter-EP, Fotomodus | einmalig je Siedlung |
| **Verirrter Reisender** | Außenposten | NPC sucht Weg → CT_ESCORT | Auftrag | situativ |

---

## 7. Baukasten & Produktionsplan

### 7.1 Modulare Kits (Environment Art)

| Kit | Verwendet in | Module (Ziel) | Varianten |
|---|---|---|---|
| Linnisches Fachwerk | R01 | 90 | Moos-/Stroh-Dächer |
| Kharsker Felsbau | R02 | 80 | Klans-Embleme |
| Morvische Pfahlbauten | R03, R06 (Flottholm) | 85 | Schilf-/Holzdach |
| Sahrunischer Lehmbau | R04 | 90 | Kuppel/Windturm |
| Ignar-Basaltbau | R05 | 70 | Bronze-Varianten |
| Saltischer Backstein | R06 | 85 | Giebelformen |
| Hvitnische Langhäuser | R07 | 70 | Gras-/Schneedächer |
| Dorunisch + Akademie | R08 | 180 (inkl. Ruinen) | Zerfallsstufen |
| Prismanischer Kristallbau | R09 | 75 | Licht an/aus |
| Nimbarische Filigranbauten | R10 | 70 | Gold-/Weiß-Varianten |
| Außenposten-Kit (fraktionsneutral + Fraktionsbanner) | alle | 60 | WW/AK/GK/ZV |

### 7.2 Produktionsaufwand (Schätzung)

| Element | Aufwand pro Stück | Anzahl | Summe |
|---|---|---|---|
| Dorf (Layout, Set-Dressing, NPCs, Zustände) | 6 Personenwochen | 22 | 132 PW |
| Außenposten | 1,5 PW | 30 | 45 PW |
| Siedlungs-Ereignisse (System + Content) | – | 7 Typen | 18 PW |
| Aufträge (System + Vorlagen) | – | 10 | 10 PW |
| **Summe** | | | **~205 Personenwochen** (P4) |

---

## 8. Code

### 8.1 Siedlungszustand (GF_World)

```cpp
// Plugins/GameFeatures/GF_World/Source/GF_World/Public/Settlements/SettlementSubsystem.h
UENUM(BlueprintType)
enum class ESettlementState : uint8 { Threatened = 0, Stable = 1, Thriving = 2 };

/** Verwaltet Zustände aller 62 Siedlungen (K13 §5). Keine Rückstufung (DR-23). */
UCLASS()
class GF_WORLD_API USettlementSubsystem : public UWorldSubsystem, public ISaveFragmentProvider
{
	GENERATED_BODY()
public:
	ESettlementState GetState(FName SettlementId) const { return States.FindRef(SettlementId); }

	/** Erhöht den Zustand, falls höher als der aktuelle. Schaltet Data Layer und meldet Event. */
	void PromoteTo(FName SettlementId, ESettlementState NewState);

	/** Zähler für Außenposten: 5 Aufträge → Blühend. */
	void OnContractCompleted(FName SettlementId);

	// ISaveFragmentProvider
	virtual FName GetSaveFragmentId() const override { return TEXT("Settlements"); }
	virtual int32 GetSaveFragmentVersion() const override { return 1; }
	virtual void WriteSaveFragment(FArchive& Ar) const override;
	virtual bool ReadSaveFragment(FArchive& Ar, int32 FromVersion) override;
	virtual void ResetSaveFragment() override;

private:
	TMap<FName, ESettlementState> States;
	TMap<FName, int32> ContractCounters;
};
```

```cpp
// Private/Settlements/SettlementSubsystem.cpp (Auszug)
void USettlementSubsystem::PromoteTo(FName SettlementId, ESettlementState NewState)
{
	ESettlementState& Current = States.FindOrAdd(SettlementId, ESettlementState::Stable);
	if (static_cast<uint8>(NewState) <= static_cast<uint8>(Current))
	{
		return; // keine Rückstufung
	}
	Current = NewState;
	ApplyDataLayers(SettlementId, NewState);   // DL_SET_<Id>_State0/1/2
	UAethrisEventBus::Get(this).Broadcast(AethrisTags::Event_World_SettlementStateChanged,
		FSettlementStateChangedMsg{ SettlementId, static_cast<uint8>(NewState) });
}

void USettlementSubsystem::OnContractCompleted(FName SettlementId)
{
	int32& Count = ContractCounters.FindOrAdd(SettlementId);
	if (++Count >= 5 && IsOutpost(SettlementId))
	{
		PromoteTo(SettlementId, ESettlementState::Thriving);
	}
}
```

*Neuer Event-Kanal:* `Event.World.SettlementStateChanged` (CANON §30 ergänzt).

### 8.2 Auftragsgenerator (Pseudocode → GF_Quests)

```text
FUNKTION RefreshContracts(siedlung, tag):
    slots ← SlotCount(siedlung.Type) − AktiveAufträge(siedlung)
    rng   ← WeltRng.Fork(4).Fork(Hash(siedlung.Id, tag))          // deterministisch
    WIEDERHOLE slots-mal:
        kandidaten ← Vorlagen.Filter(v ⇒ v.Quelle passt ∧ v.MinTier ≤ Zustand(siedlung) ∧ ¬InAbklingzeit(v, siedlung))
        gewichte   ← kandidaten.Map(v ⇒ 1 · (3 falls v ∈ Spezialität(siedlung)) · (1,5 falls v.Fraktion = SchwächsteFraktion(spieler)))
        v          ← GewichteteWahl(kandidaten, gewichte, rng)
        ziel       ← WähleZiel(v, siedlung.Zone, bevorzugt niedrige Kodex-Stufe)
        Erzeuge Auftrag(v, ziel, Belohnung = v.BaseSol · RewardScale(Zonenband-Mitte))
```

---

## 9. Decision Records

### ADR-062 – Siedlungen werden algorithmisch vorplatziert
- **Entscheidung:** Farthest-Point-Sampling auf der Makrokarte liefert Startpositionen mit garantiertem Mindestabstand; Level Design darf um ≤ 300 m verschieben (Validator prüft Region und Abstand ≥ 400 m). Vorteil: gleichmäßige Abdeckung, reproduzierbar. Nachteil: erste Positionen ignorieren Topografie → bewusst nur Blockout-Vorgabe.

### ADR-063 – Siedlungszustände ohne Rückfall
- **Entscheidung:** Drei Zustände, nur aufwärts. Vorteil: sichtbarer, dauerhafter Einfluss des Spielers (Held-Fantasie), kein Pflegezwang. Nachteil: weniger dynamische Welt-Krisen → dynamische Spannung kommt aus Ereignissen (§6), nicht aus Verschlechterung.

### ADR-064 – Wanderdorf mit mitreisendem Resonanzstein
- **Entscheidung:** Der Resonanzstein von Ashurim reist mit (Lore: tragbarer Stein, Kontor-Erfindung). Konsequenz: Schnellreise-Ziel ändert seine Position; Karte zeigt aktuelle Position (Spielzeit-Funktion → Koop-synchron).

### ADR-065 – Aufträge ohne Exklusivbelohnungen (DR-31)
- **Entscheidung:** Siehe §4.3. Schützt vor „Daily-Chore“-Gefühl.

---

## 10. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §57 | 22 Dörfer mit Lage, Einwohnern (~5.560 gesamt), Charakter, Diensten, Schlüssel-NPC, Quest- und Echo-Haken (§2) | LOCKED |
| §57 | Ashurim-Route A→B→C→D (je ~18 Spielstunden), Flottholm Ebbe-/Flut-Position | LOCKED |
| §58 | 30 Außenposten mit Typ (WW 9, AK 8, GK 4, ZV 9), Besetzung, Spezialaufträgen; Standarddienste (Feldbrunnen 10 s, Wildstein ≤ 150 m, Werkbank, Auftragsbrett, Zelt) | LOCKED |
| §58 | Koordinaten aller Siedlungen in `Settlements.csv`; Platzierung `tools/place_settlements.py` (≥ 400 m, LD-Toleranz 300 m) | LOCKED |
| §59 | 10 Auftragsvorlagen (`ContractTemplates.csv`), Slots 1/2/3, Generierungsregeln, Abklingzeit in Spieltagen, **DR-31** | LOCKED |
| §60 | Siedlungszustände Bedroht/Stabil/Blühend (nur aufwärts), Data Layers `DL_SET_<Id>_State0/1/2`, Save-Fragment `Settlements`, Event `Event.World.SettlementStateChanged` | LOCKED |
| §60 | 7 Siedlungs-Ereignistypen (§6) | LOCKED |
| §13 | DR-31 (Aufträge nie einzige Quelle einer Belohnung) | LOCKED |
| §10 | ADR-062 – ADR-065 | LOCKED |

---

## 11. Kapitel-Checkliste

- [x] Rolle und Größen von Dörfern und Außenposten
- [x] 22 Dörfer vollständig profiliert inkl. Koordinaten
- [x] 30 Außenposten mit Typ, Besetzung, Aufträgen, Koordinaten
- [x] Auftragssystem (Vorlagen-Daten, Generierung, DR-31)
- [x] Siedlungszustände mit Data Layers und Code
- [x] Siedlungs-Ereignisse
- [x] Modulare Bau-Kits und Produktionsaufwand
- [x] ADR-062 – ADR-065, CANON aktualisiert
- [x] **Teil II (Welt) Kapitel K07–K13 abgeschlossen** – es folgen Wetter (K14) und Tageszyklus (K15)

➡️ **Nächstes Kapitel: K14 – Wettersystem.**
