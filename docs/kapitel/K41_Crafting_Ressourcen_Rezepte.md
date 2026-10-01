# K41 · Crafting, Ressourcen und Rezepte

| Feld | Wert |
|---|---|
| Dokument | Kapitel 41 von 68 · Systeme, Teil VI |
| Version | 1.0 |
| Owner | Economy & Crafting Designer |
| Mitwirkende | Lead World Designer (Sammelknoten), Narrative (Werkstätten der Städte), UX Lead (Crafting-Menü), Creature Design (Echo-Materialien), Lead Systems Designer |
| Baut auf | CANON §6.3 (Grundressourcen Holz/Erz/Kristalle/Kräuter + Echo-Materialien), §8 (kein Pay-to-Win), ADR-007 (Echos sterben nicht), §45 (Ressourcen je Region), K36–K40 (Siegel, Fallen, Zucht, Ausrüstung, Halteitems), DR-23, DR-27, DR-31 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Items/Recipes.csv` (125), `Data/Items/EchoMaterials.csv` (20), `Data/Items/Consumables.csv` (25), `Data/Items/Resources.csv` (48), `tools/authoring/crafting_k41.py`, `tools/gen_items.py` (Validator) |
| Neue Kanon-Einträge | CANON §156 (Ressourcen & Sammeln), §157 (Echo-Materialien), §158 (Stationen & Rezepte), §159 (Verbrauchsgüter & Gerichte) |

---

## Inhalt

1. [Crafting in AETHRIS](#1-crafting-in-aethris)
2. [Ressourcen](#2-ressourcen)
3. [Echo-Materialien](#3-echo-materialien)
4. [Sammeln](#4-sammeln)
5. [Werkstätten](#5-werkstätten)
6. [Rezepte](#6-rezepte)
7. [Verbrauchsgüter](#7-verbrauchsgüter)
8. [Kochen](#8-kochen)
9. [Materialfluss und Fortschritt](#9-materialfluss-und-fortschritt)
10. [UI](#10-ui)
11. [Code](#11-code)
12. [Tests](#12-tests)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Crafting in AETHRIS

Crafting verbindet die drei Primär-Loops: **Erkunden** liefert Ressourcen, **Kämpfen und Binden** liefern Echo-Materialien, **Pflegen** (Hain, Lager) liefert Ertrag und Gerichte. Hergestellt werden Werkzeuge der Bindung (Siegel, Fallen), der Reise (Ausrüstung), der Pflege (Gerichte) und der Zucht – aber **keine Kampfwerte** über Ausrüstung (ADR-148).

| Prinzip | Umsetzung |
|---|---|
| Sofort | Herstellung ohne Wartezeit (DR-23) |
| Lesbar | jede Zutat zeigt, wo sie vorkommt (Region, Knoten, Art) |
| Regional | Stufe-IV/V-Ausrüstung braucht Regionsmaterialien und Meisterwerkstätten – Reisen lohnt |
| Kein Töten | Echo-Materialien werden abgeworfen, geschenkt oder im Hain gesammelt (ADR-007) |
| Kein Zwang | Fast alles ist auch kaufbar (K42) oder als Belohnung erhältlich (DR-31) |

---

## 2. Ressourcen

48 Sammelressourcen in vier Kategorien (CANON §6.3), je Region vier bis fünf, Stufen I–V passend zur Ausrüstung:

| DisplayName | Category | Tier | Region | Rarity |
|---|---|---|---|---|
| Eichenholz | Wood | 1 | R01 | Common |
| Klangharz | Wood | 2 | R01 | Rare |
| Farnfaser | Herb | 1 | R01 | Common |
| Lindblüte | Herb | 1 | R01 | Common |
| Kupfererz | Ore | 1 | R01 | Common |
| Moosperle | Crystal | 1 | R01 | Uncommon |
| Bergkiefer | Wood | 2 | R02 | Common |
| Kharseisen | Ore | 2 | R02 | Common |
| Grollbasalt | Ore | 2 | R02 | Uncommon |
| Quarzsplitter | Crystal | 1 | R02 | Common |
| Gipfelenzian | Herb | 2 | R02 | Uncommon |
| Moorweide | Wood | 1 | R03 | Common |
| Torfkohle | Ore | 1 | R03 | Common |
| Nebelperle | Crystal | 2 | R03 | Uncommon |
| Sumpfmyrte | Herb | 2 | R03 | Common |
| Irrlichtmoos | Herb | 3 | R03 | Rare |
| Wüstendornholz | Wood | 3 | R04 | Common |
| Salzkupfer | Ore | 3 | R04 | Common |
| Glutsand | Ore | 2 | R04 | Uncommon |
| Sonnenglas | Crystal | 3 | R04 | Uncommon |
| Oasenminze | Herb | 2 | R04 | Common |
| Ascheholz | Wood | 3 | R05 | Common |
| Schlackenstahl | Ore | 4 | R05 | Uncommon |
| Obsidian | Crystal | 3 | R05 | Common |
| Schwefelkristall | Crystal | 2 | R05 | Common |
| Feuerlilie | Herb | 3 | R05 | Uncommon |
| Treibholz | Wood | 1 | R06 | Common |
| Zinnerz | Ore | 1 | R06 | Common |
| Perlmutt | Crystal | 2 | R06 | Uncommon |
| Seetang | Herb | 1 | R06 | Common |
| Salzkraut | Herb | 1 | R06 | Common |
| Frostkiefer | Wood | 3 | R07 | Common |
| Silbererz | Ore | 3 | R07 | Common |
| Gletscherquarz | Crystal | 4 | R07 | Uncommon |
| Eisblume | Herb | 4 | R07 | Rare |
| Polarflechte | Herb | 3 | R07 | Common |
| Altholz | Wood | 4 | R08 | Uncommon |
| Dorunstein | Ore | 4 | R08 | Common |
| Glyphenkristall | Crystal | 4 | R08 | Uncommon |
| Ruinenrebe | Herb | 3 | R08 | Common |
| Prismaerz | Ore | 5 | R09 | Uncommon |
| Resonanzkristall | Crystal | 5 | R09 | Rare |
| Höhlenpilz | Herb | 4 | R09 | Common |
| Kristallmoos | Herb | 5 | R09 | Uncommon |
| Wolkenholz | Wood | 5 | R10 | Uncommon |
| Sternmetall | Ore | 5 | R10 | Rare |
| Himmelsglas | Crystal | 5 | R10 | Uncommon |
| Windblüte | Herb | 5 | R10 | Common |

---

## 3. Echo-Materialien

| DisplayName | Type | Sources |
|---|---|---|
| Klangsplitter (Glut) | Ember | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Flut) | Tide | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Stein) | Stone | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Sturm) | Storm | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Blüte) | Bloom | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Frost) | Frost | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Leere) | Void | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Licht) | Light | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Gift) | Venom | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Metall) | Metal | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Geist) | Spirit | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Kristall) | Crystal | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Klang) | Sound | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Schwerkraft) | Gravity | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Klangsplitter (Arkan) | Arcane | Kampf (Sieg/Bindung gegen Art des Typs), Hain-Ertrag, Begleiter-Fund |
| Gefiederte Daune | – | Volantia-Echos im Hain (Mauser) |
| Abgestreifte Schuppe | – | Serpentia/Aquatica-Echos im Hain (Häutung) |
| Panzerstaub | – | Testudinia/Articulata-Echos im Hain |
| Echowolle | – | Schur von Wolle tragenden Echos (Kjalf, Nubi …) |
| Stillstein-Splitter | Void | Story: zerstörte Stillsteine (K44–K45) |

**Klangsplitter** entstehen, wenn ein Echo im Kampf verklingt oder gebunden wird: Ein Rest seiner Frequenz kristallisiert (diegetisch: das Echo „verliert einen Ton“ und gewinnt ihn bei der Rast zurück). Menge: 1 je Sieg (Wild), 2 je Bindung, 3 je Alpha. Begleiter ab Bindungsstufe 4 finden gelegentlich Splitter (K37), der Hain liefert sie als Ertrag.

---

## 4. Sammeln

| Regel | Wert |
|---|---|
| Knoten | sichtbare Sammelpunkte (Baum, Erzader, Kristalldruse, Kräuterbusch); Resonanzsinn hebt sie hervor |
| Werkzeug | Stufe der Ressource ≤ Werkzeugstufe + 1 (Klinge = Holz, Hacke = Erz/Kristall, Sichel = Kräuter) |
| Ertrag | 1–3 je Knoten, +10 % je Werkzeugstufe (K40), Skill „Sammler“ (K43) |
| Nachwachsen | Knoten regenerieren nach 1 Spieltag (seltene Knoten 3 Spieltage); in Koop-Welten je Spieler eigene Knoten (keine Konkurrenz, DR-20) |
| Begleiter | Feldfähigkeiten Erzspur, Kräuterkunde, Kristallklang, Quellsucher (+1 Ertrag, Knoten sichtbar) |
| Wetter | Kristalldrusen leuchten im Nebel (Fund leichter), Kräuter sprießen nach Regen (+1 Knoten je Zone) |

---

## 5. Werkstätten

| Station | Ort | Herstellt |
|---|---|---|
| Lagerfeuer | jedes Lager/Zelt | Gerichte, Heilkraut-Tinktur, Bergtee, Ruhrauch, Fallen |
| Werkbank | jede Siedlung (Stadt, Dorf, Außenposten mit Werkbank) | Ausrüstung II–III, Siegel I–II, Verbrauchsgüter, Halteitems |
| Hain-Werkstatt | Resonanzhain (Ausbau 2) | Zucht-Gegenstände, Bänder, Hain-Ausbau |
| Akademie-Labor | Dorunsruh (R08), Außenstelle Eichenhall (Akt I: nur I–III) | Resonator IV–V, Meistersiegel, Obertonkristalle, Wandelklang, Klangstimmung |
| Schmiede | Schlackenwehr (R05) | Werkzeug IV–V |
| Glasbläserei | Qasr Sahrun (R04) | Kodex-Linse IV–V, Laterne IV–V |
| Werft | Saltrand-Hafen (R06) | Gleiter IV–V, Atemmaske IV–V |

Meisterwerkstätten sind gleichzeitig Orte mit Nebenquests (K49–K51) und Fraktionsbezug (Akademie, Kontor).

---

## 6. Rezepte

125 Rezepte, deterministisch aus den Item-Tabellen erzeugt (`crafting_k41.py`) und validiert (`gen_items.py`: alle Zutaten und Ausgaben existieren). `<TYP>` steht für die Variante je Klangfarbe (15 Varianten).

| Rezept | Ergebnis | Kategorie | Station | Zutaten | Freischaltung |
|---|---|---|---|---|---|
| RCP_001 | **Resonator II** | Ausrüstung | Werkbank | Perlmutt ×8, Grollbasalt ×6 | Stufe 1 besitzen |
| RCP_002 | **Resonator III** | Ausrüstung | Werkbank | Sonnenglas ×10, Salzkupfer ×8 | Stufe 2 besitzen |
| RCP_003 | **Resonator IV** | Ausrüstung | Akademie-Labor (Dorunsruh) | Gletscherquarz ×12, Dorunstein ×10, Klangsplitter (Metall) ×6 | Stufe 3 besitzen |
| RCP_004 | **Resonator V** | Ausrüstung | Akademie-Labor (Dorunsruh) | Resonanzkristall ×14, Prismaerz ×12, Klangsplitter (Klang) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_005 | **Gleiter II** | Ausrüstung | Werkbank | Bergkiefer ×8, Sumpfmyrte ×6 | Stufe 1 besitzen |
| RCP_006 | **Gleiter III** | Ausrüstung | Werkbank | Ascheholz ×10, Irrlichtmoos ×8 | Stufe 2 besitzen |
| RCP_007 | **Gleiter IV** | Ausrüstung | Werft (Saltrand-Hafen) | Altholz ×12, Höhlenpilz ×10, Klangsplitter (Kristall) ×6 | Stufe 3 besitzen |
| RCP_008 | **Gleiter V** | Ausrüstung | Werft (Saltrand-Hafen) | Wolkenholz ×14, Windblüte ×12, Klangsplitter (Stein) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_009 | **Wanderstiefel II** | Ausrüstung | Werkbank | Oasenminze ×8, Grollbasalt ×6 | Stufe 1 besitzen |
| RCP_010 | **Wanderstiefel III** | Ausrüstung | Werkbank | Irrlichtmoos ×10, Silbererz ×8 | Stufe 2 besitzen |
| RCP_011 | **Wanderstiefel IV** | Ausrüstung | Werkbank | Höhlenpilz ×12, Dorunstein ×10, Klangsplitter (Blüte) ×6 | Stufe 3 besitzen |
| RCP_012 | **Wanderstiefel V** | Ausrüstung | Werkbank | Kristallmoos ×14, Sternmetall ×12, Klangsplitter (Glut) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_013 | **Wettermantel II** | Ausrüstung | Werkbank | Oasenminze ×8, Bergkiefer ×6 | Stufe 1 besitzen |
| RCP_014 | **Wettermantel III** | Ausrüstung | Werkbank | Feuerlilie ×10, Ascheholz ×8 | Stufe 2 besitzen |
| RCP_015 | **Wettermantel IV** | Ausrüstung | Werkbank | Eisblume ×12, Altholz ×10, Klangsplitter (Gift) ×6 | Stufe 3 besitzen |
| RCP_016 | **Wettermantel V** | Ausrüstung | Werkbank | Windblüte ×14, Wolkenholz ×12, Klangsplitter (Geist) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_017 | **Wärtertasche II** | Ausrüstung | Werkbank | Oasenminze ×8, Klangharz ×6 | Stufe 1 besitzen |
| RCP_018 | **Wärtertasche III** | Ausrüstung | Werkbank | Feuerlilie ×10, Wüstendornholz ×8 | Stufe 2 besitzen |
| RCP_019 | **Wärtertasche IV** | Ausrüstung | Werkbank | Eisblume ×12, Altholz ×10, Klangsplitter (Frost) ×6 | Stufe 3 besitzen |
| RCP_020 | **Wärtertasche V** | Ausrüstung | Werkbank | Windblüte ×14, Wolkenholz ×12, Klangsplitter (Frost) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_021 | **Kodex-Linse II** | Ausrüstung | Werkbank | Schwefelkristall ×8, Kharseisen ×6 | Stufe 1 besitzen |
| RCP_022 | **Kodex-Linse III** | Ausrüstung | Werkbank | Obsidian ×10, Silbererz ×8 | Stufe 2 besitzen |
| RCP_023 | **Kodex-Linse IV** | Ausrüstung | Glasbläserei (Qasr Sahrun) | Glyphenkristall ×12, Dorunstein ×10, Klangsplitter (Metall) ×6 | Stufe 3 besitzen |
| RCP_024 | **Kodex-Linse V** | Ausrüstung | Glasbläserei (Qasr Sahrun) | Himmelsglas ×14, Prismaerz ×12, Klangsplitter (Flut) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_025 | **Wärterwerkzeug II** | Ausrüstung | Werkbank | Grollbasalt ×8, Bergkiefer ×6 | Stufe 1 besitzen |
| RCP_026 | **Wärterwerkzeug III** | Ausrüstung | Werkbank | Silbererz ×10, Wüstendornholz ×8 | Stufe 2 besitzen |
| RCP_027 | **Wärterwerkzeug IV** | Ausrüstung | Schmiede (Schlackenwehr) | Schlackenstahl ×12, Altholz ×10, Klangsplitter (Gift) ×6 | Stufe 3 besitzen |
| RCP_028 | **Wärterwerkzeug V** | Ausrüstung | Schmiede (Schlackenwehr) | Prismaerz ×14, Wolkenholz ×12, Klangsplitter (Geist) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_029 | **Laterne II** | Ausrüstung | Werkbank | Glutsand ×8, Nebelperle ×6 | Stufe 1 besitzen |
| RCP_030 | **Laterne III** | Ausrüstung | Werkbank | Salzkupfer ×10, Obsidian ×8 | Stufe 2 besitzen |
| RCP_031 | **Laterne IV** | Ausrüstung | Glasbläserei (Qasr Sahrun) | Dorunstein ×12, Gletscherquarz ×10, Klangsplitter (Flut) ×6 | Stufe 3 besitzen |
| RCP_032 | **Laterne V** | Ausrüstung | Glasbläserei (Qasr Sahrun) | Sternmetall ×14, Himmelsglas ×12, Klangsplitter (Schwerkraft) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_033 | **Atemmaske II** | Ausrüstung | Werkbank | Sumpfmyrte ×8, Perlmutt ×6 | Stufe 1 besitzen |
| RCP_034 | **Atemmaske III** | Ausrüstung | Werkbank | Irrlichtmoos ×10, Obsidian ×8 | Stufe 2 besitzen |
| RCP_035 | **Atemmaske IV** | Ausrüstung | Werft (Saltrand-Hafen) | Eisblume ×12, Gletscherquarz ×10, Klangsplitter (Glut) ×6 | Stufe 3 besitzen |
| RCP_036 | **Atemmaske V** | Ausrüstung | Werft (Saltrand-Hafen) | Kristallmoos ×14, Himmelsglas ×12, Klangsplitter (Schwerkraft) ×7, Resonanzkristall ×2 | Stufe 4 besitzen |
| RCP_037 | **Klangsiegel** | Siegel | Werkbank | Klangharz ×1, Quarzsplitter ×1 | Start |
| RCP_038 | **Gestimmtes Siegel** | Siegel | Werkbank | Klangharz ×2, Nebelperle ×1, Kharseisen ×1 | Akkord 2 |
| RCP_039 | **Meistersiegel** | Siegel | Akademie-Labor (Dorunsruh) | Glyphenkristall ×1, Silbererz ×2, Klangharz ×2 | Akkord 5 |
| RCP_040 | **Klangfarben-Siegel** | Siegel | Werkbank | Gestimmtes Siegel ×1, Klangsplitter (Typ) ×3 | Akkord 2 |
| RCP_041 | **Mondsiegel** | Siegel | Werkbank | Gestimmtes Siegel ×1, Irrlichtmoos ×2 | Akkord 2 |
| RCP_042 | **Erdsiegel** | Siegel | Werkbank | Gestimmtes Siegel ×1, Grollbasalt ×2 | Akkord 2 |
| RCP_043 | **Ruhenest** | Falle | Lagerfeuer | Treibholz ×3, Gipfelenzian ×2, Moosperle ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_044 | **Duftfalle** | Falle | Lagerfeuer | Eichenholz ×3, Oasenminze ×2, Quarzsplitter ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_045 | **Klangfalle** | Falle | Lagerfeuer | Eichenholz ×3, Gipfelenzian ×2, Quarzsplitter ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_046 | **Schattenzelt** | Falle | Lagerfeuer | Treibholz ×3, Oasenminze ×2, Moosperle ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_047 | **Ruhenetz** | Falle | Lagerfeuer | Treibholz ×3, Sumpfmyrte ×2, Moosperle ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_048 | **Schatzkiste** | Falle | Lagerfeuer | Eichenholz ×3, Sumpfmyrte ×2, Quarzsplitter ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_049 | **Wärmestein** | Falle | Lagerfeuer | Eichenholz ×3, Oasenminze ×2, Moosperle ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_050 | **Quellbecken** | Falle | Lagerfeuer | Eichenholz ×3, Oasenminze ×2, Moosperle ×1 | Kodex-Stufe 2 einer passenden Art |
| RCP_051 | **Heilkraut-Tinktur** | Verbrauchsgut | Lagerfeuer | Farnfaser ×2, Lindblüte ×1 | Start |
| RCP_052 | **Starke Tinktur** | Verbrauchsgut | Werkbank | Gipfelenzian ×2, Sumpfmyrte ×1 | Rezept (Händler/Quest) |
| RCP_053 | **Quellwasser-Elixier** | Verbrauchsgut | Werkbank | Eisblume ×1, Oasenminze ×2, Kristallmoos ×1 | Rezept (Händler/Quest) |
| RCP_054 | **Chorbalsam** | Verbrauchsgut | Werkbank | Starke Tinktur ×2, Feuerlilie ×1 | Rezept (Händler/Quest) |
| RCP_055 | **Weckklang** | Verbrauchsgut | Werkbank | Irrlichtmoos ×2, Moosperle ×1 | Rezept (Händler/Quest) |
| RCP_056 | **Läuterwasser** | Verbrauchsgut | Werkbank | Salzkraut ×2, Nebelperle ×1 | Rezept (Händler/Quest) |
| RCP_057 | **Bergtee** | Verbrauchsgut | Lagerfeuer | Gipfelenzian ×1, Bergkiefer ×1 | Start |
| RCP_058 | **Glühwurzel-Sud** | Verbrauchsgut | Werkbank | Feuerlilie ×1, Polarflechte ×1 | Rezept (Händler/Quest) |
| RCP_059 | **Lauschöl** | Verbrauchsgut | Werkbank | Ruinenrebe ×1, Klangharz ×1 | Rezept (Händler/Quest) |
| RCP_060 | **Ruhrauch** | Verbrauchsgut | Lagerfeuer | Torfkohle ×2, Sumpfmyrte ×1 | Rezept (Händler/Quest) |
| RCP_061 | **Wandelklang** | Verbrauchsgut | Werkbank | Glyphenkristall ×1, Klangsplitter (Arkan) ×3 | Rezept (Händler/Quest) |
| RCP_062 | **Klangsalz** | Verbrauchsgut | Werkbank | Schwefelkristall ×2, Perlmutt ×1 | Rezept (Händler/Quest) |
| RCP_063 | **Wesensklang** | Verbrauchsgut | Werkbank | Resonanzkristall ×2, Klangsplitter (Geist) ×5, Himmelsglas ×1 | Endgame |
| RCP_064 | **Lindwald-Eintopf** | Gericht | Lagerfeuer | Lindblüten-Honig ×2, Erzkrümel ×1, Farnfaser ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_065 | **Fischpastete** | Gericht | Lagerfeuer | Waldbeeren ×2, Muschelfleisch ×1, Sumpfmyrte ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_066 | **Honigkuchen** | Gericht | Lagerfeuer | Moosküchlein ×2, Kristallsalz ×1, Ruinenrebe ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_067 | **Würzbrot** | Gericht | Lagerfeuer | Erzkrümel ×2, Erzkrümel ×1, Farnfaser ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_068 | **Eisgelee** | Gericht | Lagerfeuer | Bergkäse ×2, Muschelfleisch ×1, Gipfelenzian ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_069 | **Glutsuppe** | Gericht | Lagerfeuer | Räucherfisch ×2, Kristallsalz ×1, Irrlichtmoos ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_070 | **Moosbrötchen** | Gericht | Lagerfeuer | Moorbeeren ×2, Erzkrümel ×1, Salzkraut ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_071 | **Dattelrolle** | Gericht | Lagerfeuer | Tangkeks ×2, Muschelfleisch ×1, Gipfelenzian ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_072 | **Tangrolle** | Gericht | Lagerfeuer | Muschelfleisch ×2, Kristallsalz ×1, Polarflechte ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_073 | **Bergkäseplatte** | Gericht | Lagerfeuer | Datteln ×2, Erzkrümel ×1, Seetang ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_074 | **Wolkentarte** | Gericht | Lagerfeuer | Glutkohle ×2, Muschelfleisch ×1, Gipfelenzian ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_075 | **Chorfestmahl** | Gericht | Lagerfeuer | Lindwald-Eintopf ×1, Fischpastete ×1, Honigkuchen ×1 | Rezeptbuch (Gasthäuser, K42) |
| RCP_076 | **Stimmstein (Glut)** | Halteitem | Werkbank | Klangsplitter (Glut) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_077 | **Stimmstein (Flut)** | Halteitem | Werkbank | Klangsplitter (Flut) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_078 | **Stimmstein (Stein)** | Halteitem | Werkbank | Klangsplitter (Stein) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_079 | **Stimmstein (Sturm)** | Halteitem | Werkbank | Klangsplitter (Sturm) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_080 | **Stimmstein (Blüte)** | Halteitem | Werkbank | Klangsplitter (Blüte) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_081 | **Stimmstein (Frost)** | Halteitem | Werkbank | Klangsplitter (Frost) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_082 | **Stimmstein (Leere)** | Halteitem | Werkbank | Klangsplitter (Leere) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_083 | **Stimmstein (Licht)** | Halteitem | Werkbank | Klangsplitter (Licht) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_084 | **Stimmstein (Gift)** | Halteitem | Werkbank | Klangsplitter (Gift) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_085 | **Stimmstein (Metall)** | Halteitem | Werkbank | Klangsplitter (Metall) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_086 | **Stimmstein (Geist)** | Halteitem | Werkbank | Klangsplitter (Geist) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_087 | **Stimmstein (Kristall)** | Halteitem | Werkbank | Klangsplitter (Kristall) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_088 | **Stimmstein (Klang)** | Halteitem | Werkbank | Klangsplitter (Klang) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_089 | **Stimmstein (Schwerkraft)** | Halteitem | Werkbank | Klangsplitter (Schwerkraft) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_090 | **Stimmstein (Arkan)** | Halteitem | Werkbank | Klangsplitter (Arkan) ×6, Quarzsplitter ×2, Kupfererz ×2 | Akkord 3 |
| RCP_091 | **Taktring** | Halteitem | Werkbank | Silbererz ×3, Sonnenglas ×2, Klangsplitter (Blüte) ×4 | Akkord 4 |
| RCP_092 | **Schildbrosche** | Halteitem | Werkbank | Salzkupfer ×3, Sonnenglas ×2, Klangsplitter (Flut) ×4 | Akkord 4 |
| RCP_093 | **Fokuslinse** | Halteitem | Werkbank | Silbererz ×3, Sonnenglas ×2, Klangsplitter (Schwerkraft) ×4 | Akkord 4 |
| RCP_094 | **Atemband** | Halteitem | Werkbank | Silbererz ×3, Sonnenglas ×2, Klangsplitter (Kristall) ×4 | Akkord 4 |
| RCP_095 | **Spiegelschuppe** | Halteitem | Werkbank | Silbererz ×3, Sonnenglas ×2, Klangsplitter (Klang) ×4 | Akkord 4 |
| RCP_096 | **Wurzelamulett** | Halteitem | Werkbank | Salzkupfer ×3, Sonnenglas ×2, Klangsplitter (Stein) ×4 | Akkord 4 |
| RCP_097 | **Nebelschal** | Halteitem | Werkbank | Salzkupfer ×3, Sonnenglas ×2, Klangsplitter (Frost) ×4 | Akkord 4 |
| RCP_098 | **Glutkern** | Halteitem | Werkbank | Salzkupfer ×3, Obsidian ×2, Klangsplitter (Glut) ×4 | Akkord 4 |
| RCP_099 | **Reinheitsglocke** | Halteitem | Werkbank | Silbererz ×3, Sonnenglas ×2, Klangsplitter (Schwerkraft) ×4 | Akkord 4 |
| RCP_100 | **Sturmfeder** | Halteitem | Werkbank | Salzkupfer ×3, Obsidian ×2, Klangsplitter (Sturm) ×4 | Akkord 4 |
| RCP_101 | **Schwerstein** | Halteitem | Werkbank | Salzkupfer ×3, Obsidian ×2, Klangsplitter (Gift) ×4 | Akkord 4 |
| RCP_102 | **Harmoniespiel** | Halteitem | Werkbank | Silbererz ×3, Obsidian ×2, Klangsplitter (Geist) ×4 | Akkord 4 |
| RCP_103 | **Bindungsband** | Halteitem | Hain-Werkstatt | Echowolle ×4, Sumpfmyrte ×3 | Bindungsstufe 4 mit einem Echo |
| RCP_104 | **Lernamulett** | Halteitem | Werkbank | Salzkupfer ×3, Sonnenglas ×2, Klangsplitter (Gift) ×4 | Akkord 4 |
| RCP_105 | **Schliffstein** | Halteitem | Werkbank | Salzkupfer ×3, Obsidian ×2, Klangsplitter (Schwerkraft) ×4 | Akkord 4 |
| RCP_106 | **Wesensband** | Halteitem | Hain-Werkstatt | Echowolle ×4, Sumpfmyrte ×3 | Zucht freigeschaltet |
| RCP_107 | **Stimmband** | Halteitem | Hain-Werkstatt | Echowolle ×4, Oasenminze ×3 | Zucht freigeschaltet |
| RCP_108 | **Erbklang** | Zucht | Hain-Werkstatt | Glyphenkristall ×1, Obertonkristall (Typ) ×1, Klangsplitter (Klang) ×3 | Zucht freigeschaltet |
| RCP_109 | **Keimwärmer** | Zucht | Hain-Werkstatt | Glutsand ×2, Echowolle ×1 | Zucht freigeschaltet |
| RCP_110 | **Klangstimmung** | Zucht | Akademie-Labor (Dorunsruh) | Sternmetall ×2, Resonanzkristall ×3, Stillstein-Splitter ×2 | Endgame |
| RCP_111 | **Obertonkristall (Glut)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Glut) ×5, Sonnenglas ×2 | Akkord 4 |
| RCP_112 | **Obertonkristall (Flut)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Flut) ×5, Obsidian ×2 | Akkord 4 |
| RCP_113 | **Obertonkristall (Stein)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Stein) ×5, Obsidian ×2 | Akkord 4 |
| RCP_114 | **Obertonkristall (Sturm)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Sturm) ×5, Obsidian ×2 | Akkord 4 |
| RCP_115 | **Obertonkristall (Blüte)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Blüte) ×5, Sonnenglas ×2 | Akkord 4 |
| RCP_116 | **Obertonkristall (Frost)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Frost) ×5, Obsidian ×2 | Akkord 4 |
| RCP_117 | **Obertonkristall (Leere)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Leere) ×5, Obsidian ×2 | Akkord 4 |
| RCP_118 | **Obertonkristall (Licht)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Licht) ×5, Sonnenglas ×2 | Akkord 4 |
| RCP_119 | **Obertonkristall (Gift)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Gift) ×5, Sonnenglas ×2 | Akkord 4 |
| RCP_120 | **Obertonkristall (Metall)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Metall) ×5, Obsidian ×2 | Akkord 4 |
| RCP_121 | **Obertonkristall (Geist)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Geist) ×5, Obsidian ×2 | Akkord 4 |
| RCP_122 | **Obertonkristall (Kristall)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Kristall) ×5, Sonnenglas ×2 | Akkord 4 |
| RCP_123 | **Obertonkristall (Klang)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Klang) ×5, Sonnenglas ×2 | Akkord 4 |
| RCP_124 | **Obertonkristall (Schwerkraft)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Schwerkraft) ×5, Sonnenglas ×2 | Akkord 4 |
| RCP_125 | **Obertonkristall (Arkan)** | Evolution | Akademie-Labor (Dorunsruh) | Klangsplitter (Arkan) ×5, Obsidian ×2 | Akkord 4 |

**Freischaltung von Rezepten:** Ausrüstung mit dem Besitz der Vorstufe; Siegel mit Akkordzahl; Fallen mit Kodex-Stufe 2 einer passenden Art (Wissen schaltet Werkzeuge frei, DR-01); Gerichte über Rezeptbücher in Gasthäusern; Endgame-Rezepte nach der Story.

---

## 7. Verbrauchsgüter

| DisplayName | Effect | Kind |
|---|---|---|
| Heilkraut-Tinktur | Heilt ein Echo um 30 % Max-HP (Kampf: Zeitkosten 60) | Consumable |
| Starke Tinktur | Heilt ein Echo um 60 % Max-HP | Consumable |
| Quellwasser-Elixier | Heilt ein Echo vollständig | Consumable |
| Chorbalsam | Heilt alle Chor-Echos um 40 % (außerhalb des Kampfes) | Consumable |
| Weckklang | Belebt ein verklungenes Echo mit 40 % HP (Kampf: 1× je Echo) | Consumable |
| Läuterwasser | Entfernt Haupt-Status und Gift | Consumable |
| Bergtee | Wärter-Ausdauer +20 für 1 Spielstunde | Consumable |
| Glühwurzel-Sud | Kälte-/Hitzeschutz 1 Spielstunde (ersetzt Wettermantel-Stufe) | Consumable |
| Lauschöl | Resonanzsinn-Reichweite +30 m für 30 Spielminuten | Consumable |
| Ruhrauch | Wildechos meiden den Wärter 10 Spielminuten (keine Kämpfe) | Consumable |
| Wandelklang | Wechselt die Passive eines Echos (CANON §102) | Consumable |
| Klangsalz | Setzt den Schliff eines Echos zurück (CANON §80) | Consumable |
| Wesensklang | Ändert die Persönlichkeit eines Echos (Endgame, CANON §81) | Consumable |
| Lindwald-Eintopf | Stimmung des Chors +15; Bindungszuwachs +10 % für 1 Spieltag | Meal |
| Fischpastete | EP +10 % für 1 Spieltag | Meal |
| Honigkuchen | Lieblingsfutter-Bonus für alle Echos (1 Mahlzeit) | Meal |
| Würzbrot | Ausdauer-Regeneration +20 % für 1 Spieltag | Meal |
| Eisgelee | Hitzewelle ohne Malus für 1 Spieltag | Meal |
| Glutsuppe | Schnee/Kälte ohne Malus für 1 Spieltag | Meal |
| Moosbrötchen | Kodex-Beobachtung 2 s statt 3 s für 1 Spieltag | Meal |
| Dattelrolle | Annäherung leiser (Entdeckungsradius ×0,9) für 1 Spieltag | Meal |
| Tangrolle | Schwimm-Ausdauer +30 % für 1 Spieltag | Meal |
| Bergkäseplatte | Reit-Ausdauer +15 % für 1 Spieltag | Meal |
| Wolkentarte | Gleiter-Auftrieb +10 % für 1 Spieltag | Meal |
| Chorfestmahl | Alle Wirkungen der Grundgerichte (Stimmung, Bindung, EP) für 1 Spieltag | Meal |

| Regel | Wert |
|---|---|
| Im Kampf | Item-Aktion Zeitkosten 60 (K31 §5); Weckklang 1× je Echo und Kampf |
| Ranked | keine Items |
| Klangbrunnen | heilen kostenlos – Heilmittel sind Komfort unterwegs, kein Pflichtkauf |
| Stapel | 30/40/50/60/80 je Taschenstufe (K40) |

---

## 8. Kochen

Gerichte werden am Lagerfeuer gekocht und wirken auf den ganzen Chor für einen Spieltag (ein Gericht gleichzeitig; neues ersetzt altes). Kochen ist ein Lager-Moment (K37) mit kurzer Animation und einer Bindungshandlung „Füttern“ für alle Echos.

| Gruppe | Gerichte | Zweck |
|---|---|---|
| Pflege | Lindwald-Eintopf, Honigkuchen, Chorfestmahl | Stimmung, Bindung |
| Fortschritt | Fischpastete, Chorfestmahl | EP +10 % |
| Reise | Würzbrot, Tangrolle, Bergkäseplatte, Wolkentarte | Ausdauer, Schwimmen, Reiten, Gleiten |
| Klima | Eisgelee, Glutsuppe | Wetter-Malus aufheben |
| Forschung | Moosbrötchen, Dattelrolle | Beobachtung schneller, Annäherung leiser |

---

## 9. Materialfluss und Fortschritt

```
 Erkunden ──► Ressourcen (Stufe I–V nach Region) ─┐
 Kampf/Bindung ──► Klangsplitter (Typ) ───────────┼──► Werkstätten ──► Ausrüstung · Siegel · Fallen
 Hain ──► Ertrag, Wolle, Daunen, Schuppen ─────────┤                    Halteitems · Gerichte · Zucht
 Händler ──► Grundstoffe, Rezeptbücher ────────────┘                    Obertonkristalle (Evolution)
```

| Akt | Typische Stufe | Beispiel-Ziel |
|---|---|---|
| Prolog/Akt I | I–II | Klangsiegel, Ruhenest, Gleiter II, Heilkraut-Tinktur |
| Akt I Ende | II–III | Gestimmte Siegel, Stimmsteine, Erbklang (Zucht) |
| Akt II | III–IV | Meistersiegel, Werkzeug IV (Schmiede), Linse IV (Glasbläserei) |
| Akt III | IV–V | Gleiter V, Resonator V, Wandelklang |
| Endgame | V + Tiefenresonanz | Klangstimmung, Wesensklang, Hain-Vollausbau |

**DR-27-Kontrolle:** Crafting-Belohnungen machen in keiner 30-Minuten-Sitzung mehr als 50 % der Belohnungen aus, weil Ressourcen nebenbei anfallen (Knoten an Wegen) und Rezepte nur mit Fortschritt freischalten.

---

## 10. UI

```
┌─ WERKBANK · Eichenhall ───────────────────────────────────────────────────────────┐
│ [Ausrüstung] [Siegel] [Fallen] [Verbrauch] [Halteitems] [Zucht] [Evolution]          │
│                                                                                      │
│  Gleiter III                         Zutaten                 Vorrat                  │
│  ▸ Sinkrate 1,50 m/s                 Bergkiefer ×10          12 ✔                    │
│  ▸ Vorwärts 10,5 m/s                 Gipfelenzian ×8          5 ✘  (Kharsgrat, Hochland)│
│  ▸ Verbrauch 4 AE/s                                                                  │
│                                   [Herstellen]  [Fehlende Zutaten markieren]         │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

„Fehlende Zutaten markieren“ setzt Kartenmarker auf bekannte Knoten/Händler (Wegfindung K54).

---

## 11. Code

```cpp
// GF_Crafting – Rezept-Ausführung (sofort, DR-23)
bool UCraftingService::Craft(FName RecipeId, int32 Count, FInventory& Inv)
{
    const FRecipeRow* R = Recipes->FindRow<FRecipeRow>(RecipeId, TEXT("Craft"));
    if (!R || !Unlocks->IsUnlocked(*R) || !StationAvailable(R->Station)) return false;
    for (const FIngredient& I : R->Ingredients) if (Inv.Count(I.ItemId) < I.Quantity * Count) return false;
    for (const FIngredient& I : R->Ingredients) Inv.Remove(I.ItemId, I.Quantity * Count);
    Inv.Add(R->Output, Count);
    Bus->Broadcast(TAG_Crafting_Crafted, FCraftedMessage{ RecipeId, Count });   // Wärter-EP „Sonstiges“, Telemetrie
    return true;
}
```

Die `<TYP>`-Varianten werden beim Import zu 15 konkreten Rezepten expandiert; das Menü gruppiert sie als ein Rezept mit Typ-Auswahl.

---

## 12. Tests

| Test | Inhalt |
|---|---|
| `Data.Items.Validate` | `tools/gen_items.py`: eindeutige IDs, alle Rezept-Referenzen existieren |
| `Aethris.Unit.Crafting.Atomic` | Herstellung entweder vollständig oder gar nicht (keine halben Abzüge) |
| `…Crafting.Unlock` | Freischaltbedingungen je Kategorie |
| `Aethris.Func.Crafting.Reachability` | Bot: jede Ausrüstungsstufe vor ihrem Ziel-Akt herstellbar (Material-Erreichbarkeit nach Regionen-Freischaltung) |

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-151 | Echo-Materialien nur abgeworfen/geschenkt/gesammelt | ADR-007, Partner-Fantasie | „Beute“ aus Echos |
| ADR-152 | Herstellung sofort, Meisterwerkstätten regional | DR-23; Reisen lohnt | Herstellungszeiten |
| ADR-153 | Rezepte aus Item-Tabellen generiert und validiert | Konsistenz bei 125+ Rezepten | Handpflege |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §156 | 48 Ressourcen (Holz/Erz/Kristall/Kraut, Stufe I–V); Knoten mit Werkzeugregel (Stufe ≤ Werkzeug + 1), Ertrag 1–3 (+10 %/Stufe), Nachwachsen 1 (selten 3) Spieltage, Koop eigene Knoten | LOCKED |
| §157 | 20 Echo-Materialien (`EchoMaterials.csv`): 15 Klangsplitter (1 je Sieg, 2 je Bindung, 3 je Alpha) + Daune, Schuppe, Panzerstaub, Echowolle, Stillstein-Splitter | LOCKED |
| §158 | Stationen Lagerfeuer, Werkbank, Hain-Werkstatt, Akademie-Labor, Schmiede, Glasbläserei, Werft; 125 Rezepte (`Recipes.csv`), sofortige Herstellung, Freischaltregeln | LOCKED |
| §159 | 13 Verbrauchsgüter + 12 Gerichte (`Consumables.csv`); Kampf-Items Zeitkosten 60, Ranked ohne Items; ein Gericht je Spieltag | LOCKED |
| §10 | ADR-151 – ADR-153 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Crafting-Prinzipien
- [x] 48 Ressourcen, 20 Echo-Materialien als Daten
- [x] Sammelregeln, Werkzeugstufen, Koop
- [x] 7 Werkstätten mit Ortsbindung
- [x] 125 Rezepte generiert und validiert
- [x] 13 Verbrauchsgüter, 12 Gerichte
- [x] Materialfluss je Akt, UI, Code, Tests
- [x] ADR-151 – ADR-153, CANON §156–§159

➡️ **Nächstes Kapitel: K42 – Wirtschaft: Sol, Händler, Preise, Senken und Quellen.**
