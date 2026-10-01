# K27 · Kreaturenkatalog 8 – Nimbara II, Ursprungsstimmen und Mythische

| Feld | Wert |
|---|---|
| Dokument | Kapitel 27 von 68 · Monster Bible – Katalog |
| Owner | Creature Design Lead |
| Mitwirkende | RPG Systems Designer, Narrative Writer, Concept Art, Legal (Clean-Room) |
| Baut auf | K16 (Designregeln, Schema), K17 (Typen), K18 (Werte), K19 (Evolution), CANON §20, §45 |
| Status | ✅ Freigegeben |
| Datenquelle | `Data/Echos/Species.csv`, `Data/Echos/SpeciesLore.csv` (Kodex #225–#256); Authoring: `tools/authoring/` |
| Region(en) | R10 Nimbara (Abschluss), Ursprungsstimmen (alle Regionen), Mythische |

> Dieses Kapitel ist **aus den Daten generiert** (ADR-075). Änderungen erfolgen ausschließlich in den Daten; danach wird das Kapitel neu erzeugt.

## Nimbara (Abschluss), Ursprungsstimmen & Mythische – der Katalog ist vollständig

Dieses Kapitel schließt **Nimbara** ab (#225–#240) und enthält die **10 Ursprungsstimmen** (#241–#250) sowie die **6 Mythischen** (#251–#256). Damit ist der **Grundkatalog mit 256 Arten vollständig** (Briefing-Ziel ≥ 250 erfüllt).

**Nimbara** (K09 §13): Freiheit, Höhe, Einklang. Das Wolkenschaf (Nubi → Nubilo → Nubiluna) verzweigt sich bei Neumond auf den Lumeya-Inseln zur **Nubisk** (Leere/Licht) – der achten und letzten Zweigform. Windharfner und Glockenqualle machen Nimbara zur zweitklangreichsten Region; die Inselschildkröte **Holmgard** und der Schwebekern **Levithar** verkörpern die Technik, die die Inseln in der Luft hält (Kronenwerft). **Astraviel**, der Sternrichter, ist der Sehr seltene Wächter der Sternenarena (ARN_10).

**Ursprungsstimmen** (CANON §34): Namen, Typen, Gestalt und Schlafort waren seit K07 gesperrt; hier werden die vollständigen Artdaten ergänzt. Alle Stimmen haben Kernsumme 660–680 (Spanne 640–680), Wachstum *Late*, Bindungsrate 3 (nur mit **Stimmsiegel**), **Feldklang**-Signatur (eine dauerhafte Feldregel, K32) und sind nicht Ranked-zulässig. Archetypen folgen der K07-Gestalt; zwei Stimmen (Pyr'thagon, Prism'aion) sind Drachen (A15).

**Mythische** (CANON §34): Phänomene außerhalb des Weltlieds; Kernsumme 630–660 (Spanne 600–660), Bindungsrate 2, Feldklang-Signaturen, die Grundregeln umkehren (Zeitleiste rückwärts, Typvorteile tauschen, Harmonie null). Zenthrax und Aurelune sind Drachen, wodurch A15 den Mindestanteil von 2 % erreicht.

### Katalog-Gesamtbilanz (#001–#256)

| Kennzahl | Wert | Ziel / Regel |
|---|---|---|
| Arten | **256** | ≥ 250 (Briefing), 256 (CANON) |
| Linien | 40 Dreier · 45 Zweier · 22 Einzel · 8 Zweige · 10 Legendär · 6 Mythisch | CANON §88 (exakt) |
| Seltenheit | Häufig 60 · Ungewöhnlich 75 · Selten 87 · Sehr selten 18 · Legendär 10 · Mythisch 6 | DR-15 (Bedingungen) |
| Primärtypen | Stein 26 · Sturm 24 · Licht 20 · Klang 19 · Geist/Flut/Schwerkraft/Kristall je 17 · Arkan/Gift/Metall je 15 · Blüte/Glut 14 · Frost/Leere 13 | jede Klangfarbe ≥ 13 Primär |
| Typplätze gesamt | Stein 47 · Licht 41 · Sturm 35 · Flut 32 · Klang 31 · Schwerkraft 27 · Geist/Kristall 26 · Arkan 24 · Blüte/Glut 22 · Metall 21 · Gift 19 · Frost/Leere 17 | jede Klangfarbe ≥ 17 |
| Doppeltypen | 151 von 256 (59 %) | 50–65 % (K17) |
| Reittiere | Boden 18 · Flug 15 · Schwimm 7 · Klettern 6 · Graben 4 (= 50) | alle 5 Reitarten ≥ 4 (K40) |
| Wachstum | Steady 95 · Late 68 · Swift 56 · Wave 37 | alle 4 Kurven genutzt |
| Archetypen | alle 18 zwischen 2,3 % (A15) und 11,3 % (A12) | 2–12 % |
| Validator | `gen_catalog.py validate`: **0 Verstöße**; NameGuard: **0 Verstöße** | – |

> **Hinweis für K28–K30:** Die Signaturkonzepte aller 256 Arten sind die Grundlage für die Fähigkeits-IDs. K28–K30 erzeugen `Data/Abilities/*.csv` und tragen die Lernsets (Level-, Lehr-, Zucht-Fähigkeiten) in die Arten ein.


## Übersicht

| Kodex | Name | Typen | Linie · Stufe | Archetyp | Größe | Seltenheit | Rolle |
|---|---|---|---|---|---|---|---|
| #225 | **Nubi** | Licht | L100 · 1 (Three) | A12 | XS | Häufig | Support |
| #226 | **Nubilo** | Licht/Sturm | L100 · 2 (Three) | A12 | S | Ungewöhnlich | Support |
| #227 | **Nubiluna** | Licht/Klang | L100 · 3 (Three) | A12 | M | Selten | Support |
| #228 | **Nubisk** | Leere/Licht | L100 · 3 (Branch) | A12 | M | Sehr selten | Control |
| #229 | **Harfel** | Klang | L101 · 1 (Two) | A05 | XS | Häufig | Support |
| #230 | **Harfion** | Klang/Sturm | L101 · 2 (Two) | A05 | M | Ungewöhnlich | Support |
| #231 | **Tintel** | Klang | L102 · 1 (Two) | A12 | XS | Häufig | Caster |
| #232 | **Tintabul** | Klang/Licht | L102 · 2 (Two) | A12 | M | Selten | Caster |
| #233 | **Holmel** | Schwerkraft | L103 · 1 (Two) | A11 | M | Ungewöhnlich | Tank |
| #234 | **Holmgard** | Schwerkraft/Stein | L103 · 2 (Two) | A11 | XL | Selten | Tank |
| #235 | **Levitel** | Schwerkraft | L104 · 1 (Two) | A13 | S | Häufig | Control |
| #236 | **Levithar** | Arkan/Schwerkraft | L104 · 2 (Two) | A13 | M | Ungewöhnlich | Control |
| #237 | **Graupel** | Frost | L105 · 1 (Two) | A16 | XS | Häufig | Striker |
| #238 | **Graupix** | Kristall/Sturm | L105 · 2 (Two) | A16 | M | Selten | Striker |
| #239 | **Lumaskiff** | Licht/Sturm | L106 · 1 (Single) | A06 | XL | Selten | AllRound |
| #240 | **Astraviel** | Arkan/Licht | L107 · 1 (Single) | A04 | L | Sehr selten | Caster |
| #241 | **Sylv'anor** | Blüte/Klang | L108 · 1 (Legendary) | A03 | XL | Legendär | Support |
| #242 | **Orh'gruun** | Stein/Schwerkraft | L109 · 1 (Legendary) | A11 | XXL | Legendär | Tank |
| #243 | **Nhael'vesh** | Gift/Geist | L110 · 1 (Legendary) | A05 | L | Legendär | Control |
| #244 | **Thal'assyr** | Flut/Sturm | L111 · 1 (Legendary) | A06 | XXL | Legendär | Speed |
| #245 | **Ash'kareth** | Licht/Arkan | L112 · 1 (Legendary) | A02 | XL | Legendär | Caster |
| #246 | **Pyr'thagon** | Glut/Metall | L113 · 1 (Legendary) | A15 | XXL | Legendär | Striker |
| #247 | **Isv'aldr** | Frost/Licht | L114 · 1 (Legendary) | A06 | XXL | Legendär | Support |
| #248 | **Ka'thurel** | Geist/Arkan | L115 · 1 (Legendary) | A13 | XL | Legendär | Control |
| #249 | **Prism'aion** | Kristall/Klang | L116 · 1 (Legendary) | A15 | XXL | Legendär | Caster |
| #250 | **Aeth'rion** | Klang/Licht | L117 · 1 (Legendary) | A05 | L | Legendär | AllRound |
| #251 | **Velnox** | Leere/Schwerkraft | L118 · 1 (Mythical) | A12 | L | Mythisch | Control |
| #252 | **Chronaire** | Klang/Arkan | L119 · 1 (Mythical) | A04 | M | Mythisch | Speed |
| #253 | **Mirrowisp** | Kristall/Geist | L120 · 1 (Mythical) | A12 | S | Mythisch | Control |
| #254 | **Ouroveth** | Gift/Blüte | L121 · 1 (Mythical) | A07 | XXL | Mythisch | Tank |
| #255 | **Zenthrax** | Schwerkraft/Metall | L122 · 1 (Mythical) | A15 | XXL | Mythisch | Striker |
| #256 | **Aurelune** | Licht/Leere | L123 · 1 (Mythical) | A15 | XL | Mythisch | Caster |

## Linien & Evolutionen

```
L100  Nubi ──[Level>=18]──► Nubilo ──[Level>=34]──► Nubiluna
      └─ Zweig von Nubilo ──[Level>=34 & Moon=NewMoon & Zone=R10_Z02]──► Nubisk
L101  Harfel ──[Level>=28]──► Harfion
L102  Tintel ──[Level>=30 & TimeOfDay=Dusk]──► Tintabul
L103  Holmel ──[Level>=34]──► Holmgard
L104  Levitel ──[Level>=32]──► Levithar
L105  Graupel ──[Level>=30 & Weather=Thunderstorm]──► Graupix
L106  Lumaskiff
L107  Astraviel
L108  Sylv'anor
L109  Orh'gruun
L110  Nhael'vesh
L111  Thal'assyr
L112  Ash'kareth
L113  Pyr'thagon
L114  Isv'aldr
L115  Ka'thurel
L116  Prism'aion
L117  Aeth'rion
L118  Velnox
L119  Chronaire
L120  Mirrowisp
L121  Ouroveth
L122  Zenthrax
L123  Aurelune
```

## Kennzahlen & Validierung

| Kennzahl | Wert |
|---|---|
| Arten in diesem Kapitel | 32 |
| Linientypen | Three 3, Branch 1, Two 10, Single 2, Legendary 10, Mythical 6 (Arten je Typ) |
| Primärtypen | Licht 6, Klang 6, Schwerkraft 4, Kristall 3, Leere 2, Arkan 2, Frost 2, Gift 2, Blüte 1, Stein 1, Flut 1, Glut 1, Geist 1 |
| Archetypen | A02 1, A03 1, A04 2, A05 4, A06 3, A07 1, A11 3, A12 8, A13 3, A15 4, A16 2 |
| Wildseltenheit (ohne reine Evolutionsformen) | Häufig 5, Ungewöhnlich 4, Selten 4, Sehr selten 1 |
| Nur durch Evolution/Zucht (`Spawn.None`) | 18 |
| Reittiere | Holmgard (Bodenreiten), Lumaskiff (Flugreiten) |
| Validator (`tools/gen_catalog.py validate`, Gesamtkatalog) | **0 Verstöße** |

## Einträge

### #225 Nubi

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_225` · L100 · Stufe 1 (Three) |
| Wissenschaftlich · Kategorie | *Nubiovis lanata* · Wölkchen-Echo |
| Typen | **Licht** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · XS · 0,28 m · 0,6 kg |
| Region · Lebensraum | R10 · Gärten von Aerion |
| Seltenheit · Bedingungen · Zonen | Häufig · – · R10_Z02, R10_Z03 |
| Aktivität · Merkmale | Tagaktiv · Treiber, Verspielt, Sonnenbader |
| Nischen · Rolle · Reiten | Kampf, Zucht · Support · – |
| Basiswerte | HP 56 · ANG 41 · VER 53 · SAN 51 · SVE 58 · GES 46 = **305** · PRÄ 100 · AUS 102 · Wachstum Swift · EP-Ertrag 60 · Schliff SpDefense:1 |
| Evolution | → Nubilo (#226) · Bedingung: `Level>=18` |
| Bindung | Rate 65 · Vorliebe `ITM_FOOD_CLOUDFRUIT` |
| Signatur (Konzept) | Sonnenflaum: heilt Verbündete in Sonnenwetter jede Runde |
| Klangmal | Ein Wollknäuel aus Wolke, das in der Sonne golden leuchtet |

- **Herkunft:** Ein Licht-Oberton, so weich wie die erste Wolke nach einem Sturm.
- **Verhalten:** Treibt durch Gärten und sonnt sich auf Dächern; folgt jedem, der summt.
- **Mythologie:** Ein Nubi im Haus hält schlechte Träume fern, sagen die Aerioner.
- **Beziehung zu Menschen:** Die Gärtner Aerions scheren Nubis für Kissen – die Wolle wächst in einer Nacht nach.
- *Kodex-Notiz (Stufe 4):* Ab Level 18 und Level 34 wächst es; auf den Inseln bei Neumond zu einer anderen Form.

### #226 Nubilo

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_226` · L100 · Stufe 2 (Three) |
| Wissenschaftlich · Kategorie | *Nubiovis serena* · Wolkenschaf-Echo |
| Typen | **Licht / Sturm** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · S · 0,75 m · 8 kg |
| Region · Lebensraum | R10 · Lumeya-Inseln |
| Seltenheit · Bedingungen · Zonen | Ungewöhnlich · – · R10_Z02 |
| Aktivität · Merkmale | Tagaktiv · Treiber, Herde, Leuchtend |
| Nischen · Rolle · Reiten | Kampf, Zucht · Support · – |
| Basiswerte | HP 79 · ANG 57 · VER 75 · SAN 72 · SVE 82 · GES 65 = **430** · PRÄ 100 · AUS 102 · Wachstum Swift · EP-Ertrag 140 · Schliff SpDefense:2 |
| Evolution | → Nubiluna (#227), Nubisk (#228) · Bedingung: `(Level>=34) | (Level>=34 & Moon=NewMoon & Zone=R10_Z02)` |
| Bindung | Rate 50 · Vorliebe `ITM_FOOD_CLOUDFRUIT` |
| Signatur (Konzept) | Regenbogenwolle: Verbündete erhalten Schutz gegen den nächsten Status |
| Klangmal | Wolle, die Regenbögen wirft, wenn Licht durch sie fällt |

- **Herkunft:** Das heranwachsende Wolkenschaf zieht in Herden über die Inseln.
- **Verhalten:** Weidet Morgentau von Gräsern und schwebt bei Wind höher.
- **Mythologie:** Hirten auf den Lumeya-Inseln binden ihre Nubilos mit Bändern, damit sie nicht davonfliegen.
- **Beziehung zu Menschen:** Nubilo-Wolle ist die wertvollste Handelsware Nimbaras.
- *Kodex-Notiz (Stufe 4):* Ab Level 34 Endform; bei Neumond auf den Inseln Zweigform.

### #227 Nubiluna

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_227` · L100 · Stufe 3 (Three) |
| Wissenschaftlich · Kategorie | *Nubiovis cantrix* · Himmelsherden-Echo |
| Typen | **Licht / Klang** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · M · 1,5 m · 90 kg |
| Region · Lebensraum | R10 · Gärten von Aerion |
| Seltenheit · Bedingungen · Zonen | Selten · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Treiber, Herde, Sänger |
| Nischen · Rolle · Reiten | Kampf, Zucht · Support · – |
| Basiswerte | HP 96 · ANG 70 · VER 92 · SAN 87 · SVE 101 · GES 79 = **525** · PRÄ 100 · AUS 102 · Wachstum Swift · EP-Ertrag 210 · Schliff SpDefense:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 35 · Vorliebe `ITM_FOOD_CLOUDFRUIT` |
| Signatur (Konzept) | Wiegenlied der Wolken: Crescendo – volle Heilung aller Verbündeten, Gegner schläfrig |
| Klangmal | Ein strahlender Wolkenleib, der ein Wiegenlied summt |

- **Herkunft:** Die Endform der Wolkenschafe singt Wiegenlieder, bei denen selbst Stürme einschlafen.
- **Verhalten:** Führt Herden durch die Gärten; ihr Gesang beruhigt jedes Tier in der Nähe.
- **Mythologie:** Die Aerioner singen Kindern Nubiluna-Lieder vor, damit sie ohne Angst vor dem Fallen schlafen.
- **Beziehung zu Menschen:** Heiler Aerions arbeiten mit Nubilunas in den Gärten der Genesung.
- *Kodex-Notiz (Stufe 4):* Entsteht aus Nubilo ab Level 34.

### #228 Nubisk

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_228` · L100 · Stufe 3 (Branch) |
| Wissenschaftlich · Kategorie | *Nubiovis obscura* · Gewitterschaf-Echo |
| Typen | **Leere / Licht** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · M · 1,4 m · 40 kg |
| Region · Lebensraum | R10 · Lumeya-Inseln in Neumondnächten |
| Seltenheit · Bedingungen · Zonen | Sehr selten · `Spawn.None` · – |
| Aktivität · Merkmale | Nachtaktiv · Treiber, Einzelgänger, Leuchtend |
| Nischen · Rolle · Reiten | Kampf, Forschung · Control · – |
| Basiswerte | HP 88 · ANG 70 · VER 87 · SAN 101 · SVE 92 · GES 87 = **525** · PRÄ 102 · AUS 100 · Wachstum Swift · EP-Ertrag 210 · Schliff SpAttack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 25 · Vorliebe `ITM_LURE_STARCHIME` |
| Signatur (Konzept) | Dunkelwolle: hüllt das Feld in Dunkelheit – Licht-Angriffe 2 Züge geschwächt |
| Klangmal | Schwarze Wolle mit Sternenpunkten, die kein Licht zurückwirft |

- **Herkunft:** Ein Nubilo, das in einer Neumondnacht wächst, wird zu einer Wolke ohne Licht.
- **Verhalten:** Treibt nachts zwischen den Inseln; wo es vorbeizieht, verschwinden die Sterne.
- **Mythologie:** Die Hirten sagen, ein Nubisk hüte die Träume, die zu dunkel für den Tag sind.
- **Beziehung zu Menschen:** Der Orden der Stille schickte Gesandte nach Nimbara, um Nubisks zu studieren.
- *Kodex-Notiz (Stufe 4):* Entsteht aus Nubilo ab Level 34 bei Neumond auf den Lumeya-Inseln.

### #229 Harfel

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_229` · L101 · Stufe 1 (Two) |
| Wissenschaftlich · Kategorie | *Aeolornis tenuis* · Harfenvogel-Echo |
| Typen | **Klang** |
| Archetyp · Größe · Gewicht | A05 Vogel · XS · 0,25 m · 1,4 kg |
| Region · Lebensraum | R10 · Gärten von Aerion |
| Seltenheit · Bedingungen · Zonen | Häufig · – · R10_Z03 |
| Aktivität · Merkmale | Tagaktiv · Flieger, Sänger, Nestbauer |
| Nischen · Rolle · Reiten | Kampf, Forschung · Support · – |
| Basiswerte | HP 63 · ANG 46 · VER 60 · SAN 58 · SVE 66 · GES 52 = **345** · PRÄ 100 · AUS 102 · Wachstum Steady · EP-Ertrag 75 · Schliff SpDefense:1 |
| Evolution | → Harfion (#230) · Bedingung: `Level>=28` |
| Bindung | Rate 60 · Vorliebe `ITM_LURE_WINDCHIME` |
| Signatur (Konzept) | Saitenlied: Verbündete erhalten +1 GES für 2 Züge |
| Klangmal | Schwanzfedern wie Harfensaiten, die der Wind zum Klingen bringt |

- **Herkunft:** Ein Klang-Oberton, dessen Federn wie Saiten gespannt sind.
- **Verhalten:** Sitzt im Wind und lässt ihn auf den Federn spielen; baut Nester in Windspielen.
- **Mythologie:** Ein Harfel, der am Fenster singt, kündigt Liebe an.
- **Beziehung zu Menschen:** Aerions Musiker halten Harfels als Lehrer für reine Intervalle.
- *Kodex-Notiz (Stufe 4):* Ab Level 28 wächst er zum Windharfner.

### #230 Harfion

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_230` · L101 · Stufe 2 (Two) |
| Wissenschaftlich · Kategorie | *Aeolornis aeolius* · Windharfner-Echo |
| Typen | **Klang / Sturm** |
| Archetyp · Größe · Gewicht | A05 Vogel · M · 1,0 m · 87,5 kg |
| Region · Lebensraum | R10 · Windstufen |
| Seltenheit · Bedingungen · Zonen | Ungewöhnlich · – · R10_Z01, R10_Z03 |
| Aktivität · Merkmale | Tagaktiv · Flieger, Sänger, Wanderer |
| Nischen · Rolle · Reiten | Kampf, Forschung · Support · – |
| Basiswerte | HP 91 · ANG 66 · VER 87 · SAN 82 · SVE 95 · GES 74 = **495** · PRÄ 100 · AUS 102 · Wachstum Steady · EP-Ertrag 190 · Schliff SpDefense:2 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 45 · Vorliebe `ITM_LURE_WINDCHIME` |
| Signatur (Konzept) | Äolsakkord: Verbündete erhalten Harmonie +10, Gegner −1 Präzision |
| Klangmal | Ein Federfächer wie eine Windharfe, der im Sturm volle Akkorde spielt |

- **Herkunft:** Der ausgewachsene Harfner spielt im Sturm ganze Symphonien.
- **Verhalten:** Kreist in den Windstufen; bei Sturm hört man ihn über ganz Aerion.
- **Mythologie:** Die Aerioner nennen Stürme ‚Harfionkonzerte‘.
- **Beziehung zu Menschen:** Das Wahrzeichen von Aerion – die Windharfe am Hafen – wurde einem Harfion nachgebaut.
- *Kodex-Notiz (Stufe 4):* Entwickelt sich nicht weiter.

### #231 Tintel

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_231` · L102 · Stufe 1 (Two) |
| Wissenschaftlich · Kategorie | *Tintinnomedusa pendula* · Glöckchen-Echo |
| Typen | **Klang** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · XS · 0,25 m · 0,5 kg |
| Region · Lebensraum | R10 · Unter den Inseln |
| Seltenheit · Bedingungen · Zonen | Häufig · – · R10_Z02, R10_Z04 |
| Aktivität · Merkmale | Dämmerungsaktiv · Treiber, Sänger, Leuchtend |
| Nischen · Rolle · Reiten | Kampf, Forschung · Caster · – |
| Basiswerte | HP 52 · ANG 35 · VER 49 · SAN 80 · SVE 60 · GES 69 = **345** · PRÄ 104 · AUS 100 · Wachstum Wave · EP-Ertrag 75 · Schliff SpAttack:1 |
| Evolution | → Tintabul (#232) · Bedingung: `Level>=30 & TimeOfDay=Dusk` |
| Bindung | Rate 55 · Vorliebe `ITM_LURE_BELLCHIME` |
| Signatur (Konzept) | Klingelton: Klang-Angriff, der bei Treffer einen Echo-Zweittreffer erzeugt |
| Klangmal | Ein glockenförmiger Schirm, der bei jeder Bewegung läutet |

- **Herkunft:** Ein Klang-Oberton, der wie eine kleine Glocke unter den Inseln hängt.
- **Verhalten:** Treibt in der Dämmerung aufwärts und läutet zum Abend.
- **Mythologie:** Wenn die Tintels läuten, ist es Zeit, nach Hause zu gehen.
- **Beziehung zu Menschen:** Die Kronenwerft nutzt Tintel-Läuten als Schichtsignal.
- *Kodex-Notiz (Stufe 4):* Ab Level 30 in der Dämmerung wächst es.

### #232 Tintabul

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_232` · L102 · Stufe 2 (Two) |
| Wissenschaftlich · Kategorie | *Tintinnomedusa sonans* · Glockenqualle-Echo |
| Typen | **Klang / Licht** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · M · 1,5 m · 90 kg |
| Region · Lebensraum | R10 · Unter der Kronenwerft |
| Seltenheit · Bedingungen · Zonen | Selten · `TimeOfDay.Dusk` · R10_Z04 |
| Aktivität · Merkmale | Dämmerungsaktiv · Treiber, Sänger, Einzelgänger |
| Nischen · Rolle · Reiten | Kampf, Forschung · Caster · – |
| Basiswerte | HP 75 · ANG 50 · VER 71 · SAN 117 · SVE 87 · GES 100 = **500** · PRÄ 104 · AUS 100 · Wachstum Wave · EP-Ertrag 190 · Schliff SpAttack:2 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 35 · Vorliebe `ITM_LURE_BELLCHIME` |
| Signatur (Konzept) | Großes Geläut: Klang-Angriff auf alle Gegner, erweckt schlafende Verbündete |
| Klangmal | Ein Glockenschirm aus Licht, dessen Läuten man im Brustkorb spürt |

- **Herkunft:** Eine Glockenqualle, die in der Dämmerung wuchs, läutet wie eine Kathedrale.
- **Verhalten:** Schwebt unter der Kronenwerft und läutet zum Sonnenuntergang.
- **Mythologie:** Die Aerioner sagen, das Geläut der Tintabuls rufe die Sterne herbei.
- **Beziehung zu Menschen:** Bei Festen in Aerion läuten Tintabuls statt Kirchenglocken.
- *Kodex-Notiz (Stufe 4):* Wild nur in der Dämmerung. Entwickelt sich nicht weiter.

### #233 Holmel

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_233` · L103 · Stufe 1 (Two) |
| Wissenschaftlich · Kategorie | *Insulatestudo levis* · Schwebeschildkröten-Echo |
| Typen | **Schwerkraft** |
| Archetyp · Größe · Gewicht | A11 Panzerträger · M · 0,9 m · 127,6 kg |
| Region · Lebensraum | R10 · Ränder der Lumeya-Inseln |
| Seltenheit · Bedingungen · Zonen | Ungewöhnlich · – · R10_Z02 |
| Aktivität · Merkmale | Tagaktiv · Schläfer, Weidegänger, Sonnenbader |
| Nischen · Rolle · Reiten | Kampf, Zucht · Tank · – |
| Basiswerte | HP 70 · ANG 52 · VER 76 · SAN 41 · SVE 64 · GES 47 = **350** · PRÄ 100 · AUS 92 · Wachstum Late · EP-Ertrag 75 · Schliff Defense:1 |
| Evolution | → Holmgard (#234) · Bedingung: `Level>=34` |
| Bindung | Rate 50 · Vorliebe `ITM_FOOD_CLOUDFRUIT` |
| Signatur (Konzept) | Schwebepanzer: kann nicht verschoben werden; Boden-Angriffe verfehlen |
| Klangmal | Ein Panzer, auf dem Moos und kleine Steine schweben |

- **Herkunft:** Ein Schwerkraft-Oberton, der vergessen hat, wo unten ist.
- **Verhalten:** Schwebt knapp über dem Boden und grast an Inselrändern.
- **Mythologie:** Kinder setzen sich auf Holmels und lassen sich über Gärten tragen.
- **Beziehung zu Menschen:** Aerions Gärtner nutzen Holmels, um Pflanzen an Inselunterseiten zu pflegen.
- *Kodex-Notiz (Stufe 4):* Ab Level 34 wächst er zur Inselschildkröte.

### #234 Holmgard

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_234` · L103 · Stufe 2 (Two) |
| Wissenschaftlich · Kategorie | *Insulatestudo insularis* · Inselschildkröten-Echo |
| Typen | **Schwerkraft / Stein** |
| Archetyp · Größe · Gewicht | A11 Panzerträger · XL · 3,5 m · 7503,1 kg |
| Region · Lebensraum | R10 · Zwischen den Inseln treibend |
| Seltenheit · Bedingungen · Zonen | Selten · `Weather.Clear` · R10_Z02, R10_Z04 |
| Aktivität · Merkmale | Tagaktiv · Schläfer, Hüter, Wanderer |
| Nischen · Rolle · Reiten | Kampf, Reittier · Tank · Bodenreiten |
| Basiswerte | HP 101 · ANG 76 · VER 109 · SAN 59 · SVE 93 · GES 67 = **505** · PRÄ 100 · AUS 92 · Wachstum Late · EP-Ertrag 190 · Schliff Defense:2 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 35 · Vorliebe `ITM_FOOD_CLOUDFRUIT` |
| Signatur (Konzept) | Inselgewicht: erhöht die Schwerkraft; Flug-Echos verlieren ihren Ausweichbonus |
| Klangmal | Ein Panzer wie eine kleine Insel mit eigenem Baum |

- **Herkunft:** Die ausgewachsene Schildkröte trägt eine eigene kleine Insel.
- **Verhalten:** Treibt langsam zwischen den Inseln; Vögel nisten auf ihrem Rücken.
- **Mythologie:** Die Aerioner sagen, verirrte Holmgards wurden irgendwann zu richtigen Inseln.
- **Beziehung zu Menschen:** Holmgards tragen Reiter über schwebende Brücken, die zu schmal für Karren sind.
- *Kodex-Notiz (Stufe 4):* Trägt Reiter. Wild nur bei klarem Wetter. Entwickelt sich nicht weiter.

### #235 Levitel

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_235` · L104 · Stufe 1 (Two) |
| Wissenschaftlich · Kategorie | *Levitator minimus* · Schwebestein-Echo |
| Typen | **Schwerkraft** |
| Archetyp · Größe · Gewicht | A13 Konstrukt/Elementar · S · 0,4 m · 11,2 kg |
| Region · Lebensraum | R10 · Kronenwerft |
| Seltenheit · Bedingungen · Zonen | Häufig · – · R10_Z04 |
| Aktivität · Merkmale | Tagaktiv · Neugierig, Muster-Sammler, Leuchtend |
| Nischen · Rolle · Reiten | Kampf, Feld · Control · – |
| Basiswerte | HP 58 · ANG 46 · VER 58 · SAN 66 · SVE 60 · GES 57 = **345** · PRÄ 102 · AUS 100 · Wachstum Steady · EP-Ertrag 75 · Schliff SpDefense:1 |
| Evolution | → Levithar (#236) · Bedingung: `Level>=32` |
| Bindung | Rate 55 · Vorliebe `ITM_LURE_TUNINGFORK` |
| Signatur (Konzept) | Hebung: hebt das Ziel an – es verliert 1 Zug lang seinen Reihenvorteil |
| Klangmal | Ein schwebender Stein mit leuchtenden Runenringen |

- **Herkunft:** Ein Schwerkraft-Oberton aus dem Gestein, das Nimbara in der Luft hält.
- **Verhalten:** Schwebt durch die Werft und hebt kleine Dinge an, um sie zu betrachten.
- **Mythologie:** Werftarbeiter sagen: Ein Levitel, der dein Werkzeug versteckt, will spielen.
- **Beziehung zu Menschen:** Die Kronenwerft nutzt Levitels, um schwere Bauteile anzuheben.
- *Kodex-Notiz (Stufe 4):* Ab Level 32 wächst er.

### #236 Levithar

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_236` · L104 · Stufe 2 (Two) |
| Wissenschaftlich · Kategorie | *Levitator magister* · Schwebekern-Echo |
| Typen | **Arkan / Schwerkraft** |
| Archetyp · Größe · Gewicht | A13 Konstrukt/Elementar · M · 1,4 m · 480,2 kg |
| Region · Lebensraum | R10 · Herz der Kronenwerft |
| Seltenheit · Bedingungen · Zonen | Ungewöhnlich · – · R10_Z04 |
| Aktivität · Merkmale | Tagaktiv · Hüter, Leuchtend, Werkzeugnutzer |
| Nischen · Rolle · Reiten | Kampf, Feld · Control · – |
| Basiswerte | HP 83 · ANG 67 · VER 83 · SAN 96 · SVE 88 · GES 83 = **500** · PRÄ 102 · AUS 100 · Wachstum Steady · EP-Ertrag 190 · Schliff SpDefense:2 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 40 · Vorliebe `ITM_LURE_TUNINGFORK` |
| Signatur (Konzept) | Schwebefeld: Verbündete schweben 2 Züge (Boden-Angriffe verfehlen, GES +1) |
| Klangmal | Ein Kern aus Runenstein, um den drei Ringe kreisen |

- **Herkunft:** Der ausgewachsene Schwebekern trägt Runen, die Schwere in Ordnung bringen.
- **Verhalten:** Hält in der Kronenwerft ganze Schiffsrümpfe in der Schwebe.
- **Mythologie:** Die Aerioner glauben, die ersten Inseln wurden von Levithars angehoben.
- **Beziehung zu Menschen:** Ohne Levithars stünde die Kronenwerft still – sie sind ihr wertvollstes Gut.
- *Kodex-Notiz (Stufe 4):* Entwickelt sich nicht weiter.

### #237 Graupel

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_237` · L105 · Stufe 1 (Two) |
| Wissenschaftlich · Kategorie | *Grandonubes minuta* · Graupelkorn-Echo |
| Typen | **Frost** |
| Archetyp · Größe · Gewicht | A16 Schwarm · XS · 0,2 m · 0,3 kg |
| Region · Lebensraum | R10 · Höhenwinde über den Windstufen |
| Seltenheit · Bedingungen · Zonen | Häufig · `Weather.Snow` · R10_Z01 |
| Aktivität · Merkmale | Tagaktiv · Schwarm, Treiber, Angriffslustig |
| Nischen · Rolle · Reiten | Kampf · Striker · – |
| Basiswerte | HP 54 · ANG 78 · VER 52 · SAN 40 · SVE 49 · GES 72 = **345** · PRÄ 106 · AUS 96 · Wachstum Swift · EP-Ertrag 75 · Schliff Attack:1 |
| Evolution | → Graupix (#238) · Bedingung: `Level>=30 & Weather=Thunderstorm` |
| Bindung | Rate 50 · Vorliebe `ITM_LURE_WINDCHIME` |
| Signatur (Konzept) | Graupelschauer: mehrere kleine Treffer (2–4) |
| Klangmal | Weiße Körner, die beim Aufprall klirren |

- **Herkunft:** Ein Frost-Oberton aus tausend kleinen Eiskörnern.
- **Verhalten:** Fällt in Schauern über die Windstufen und prallt von allem ab.
- **Mythologie:** Graupel auf dem Dach bedeutet Glück für die Ernte – zu viel davon nicht.
- **Beziehung zu Menschen:** Aerions Gärtner spannen Netze, um Graupel-Schwärme von jungen Pflanzen fernzuhalten.
- *Kodex-Notiz (Stufe 4):* Wild nur bei Schneefall. Ab Level 30 im Gewitter wächst er.

### #238 Graupix

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_238` · L105 · Stufe 2 (Two) |
| Wissenschaftlich · Kategorie | *Grandonubes grandinis* · Hagelsturm-Echo |
| Typen | **Kristall / Sturm** |
| Archetyp · Größe · Gewicht | A16 Schwarm · M · 1,5 m · 90 kg |
| Region · Lebensraum | R10 · Gewitterzellen über Nimbara |
| Seltenheit · Bedingungen · Zonen | Selten · `Weather.Thunderstorm` · R10_Z01, R10_Z05 |
| Aktivität · Merkmale | Tagaktiv · Schwarm, Treiber, Angriffslustig |
| Nischen · Rolle · Reiten | Kampf · Striker · – |
| Basiswerte | HP 79 · ANG 113 · VER 75 · SAN 58 · SVE 71 · GES 104 = **500** · PRÄ 106 · AUS 96 · Wachstum Swift · EP-Ertrag 190 · Schliff Attack:2 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 30 · Vorliebe `ITM_LURE_WINDCHIME` |
| Signatur (Konzept) | Hagelschlag: Kristall-Angriff auf alle Gegner, bei Gewitter doppelt |
| Klangmal | Ein Wirbel aus Hagelkristallen mit einem blitzenden Kern |

- **Herkunft:** Ein Graupelschwarm, der im Gewitter wuchs, wird zu einem Hagelsturm.
- **Verhalten:** Fällt aus Gewitterzellen und zerschlägt Gärten und Dächer.
- **Mythologie:** Die Aerioner läuten Glocken, um Graupix-Stürme zu vertreiben.
- **Beziehung zu Menschen:** Die Kronenwerft panzert ihre Schiffe gegen Graupix – mit mäßigem Erfolg.
- *Kodex-Notiz (Stufe 4):* Wild nur bei Gewitter. Entwickelt sich nicht weiter.

### #239 Lumaskiff

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_239` · L106 · Stufe 1 (Single) |
| Wissenschaftlich · Kategorie | *Lumenavis nauta* · Himmelsboot-Echo |
| Typen | **Licht / Sturm** |
| Archetyp · Größe · Gewicht | A06 Gleitschwimmer · XL · 3,5 m · 900 kg |
| Region · Lebensraum | R10 · Über der Kronenwerft |
| Seltenheit · Bedingungen · Zonen | Selten · `Weather.Clear` · R10_Z04, R10_Z05 |
| Aktivität · Merkmale | Tagaktiv · Treiber, Leuchtend, Wanderer |
| Nischen · Rolle · Reiten | Kampf, Reittier · AllRound · Flugreiten |
| Basiswerte | HP 82 · ANG 82 · VER 82 · SAN 82 · SVE 81 · GES 81 = **490** · PRÄ 100 · AUS 100 · Wachstum Steady · EP-Ertrag 180 · Schliff SpDefense:2 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 35 · Vorliebe `ITM_FOOD_CLOUDFRUIT` |
| Signatur (Konzept) | Segelschein: die eigene Reihe handelt diese Runde zuerst |
| Klangmal | Ein Körper wie ein Bootsrumpf mit Segeln aus Licht |

- **Herkunft:** Ein Licht-Oberton, der die Form der ersten Himmelsschiffe annahm.
- **Verhalten:** Segelt durch klare Tage über der Werft; trägt Wolkenfetzen wie Fracht.
- **Mythologie:** Die Werftleute glauben, Lumaskiffs seien die Seelen fertiggestellter Schiffe.
- **Beziehung zu Menschen:** Die Kronenwerft baute ihre Schiffe nach Lumaskiff-Vorbild.
- *Kodex-Notiz (Stufe 4):* Trägt Reiter durch die Luft. Wild nur bei klarem Wetter. Entwickelt sich nicht.

### #240 Astraviel

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_240` · L107 · Stufe 1 (Single) |
| Wissenschaftlich · Kategorie | *Astraiudex iudex* · Sternrichter-Echo |
| Typen | **Arkan / Licht** |
| Archetyp · Größe · Gewicht | A04 Zweibeiner · L · 2,2 m · 1863,4 kg |
| Region · Lebensraum | R10 · Sternenarena |
| Seltenheit · Bedingungen · Zonen | Sehr selten · `TimeOfDay.Night`, `Weather.Clear` · R10_Z05 |
| Aktivität · Merkmale | Nachtaktiv · Sternschauer, Hüter, Einzelgänger |
| Nischen · Rolle · Reiten | Kampf, Forschung · Caster · – |
| Basiswerte | HP 75 · ANG 50 · VER 71 · SAN 117 · SVE 87 · GES 100 = **500** · PRÄ 104 · AUS 100 · Wachstum Late · EP-Ertrag 180 · Schliff SpAttack:2 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 20 · Vorliebe `ITM_LURE_STARCHIME` |
| Signatur (Konzept) | Sternurteil: Arkan-Angriff, Schaden steigt mit der Zahl der Werteveränderungen auf dem Feld |
| Klangmal | Ein Gewand aus Nachthimmel, in dem Sternbilder zu Waagen werden |

- **Herkunft:** Ein Arkan-Oberton, der über die Sternenarena wacht, seit es sie gibt.
- **Verhalten:** Erscheint in klaren Nächten auf den Rängen und beobachtet Kämpfe schweigend.
- **Mythologie:** Man sagt, Astraviel entscheide, wer würdig ist, das Weltlied zu hören.
- **Beziehung zu Menschen:** Oruma Siyel kämpft nur, wenn Astraviel auf den Rängen erscheint.
- *Kodex-Notiz (Stufe 4):* Wild nur in klaren Nächten. Entwickelt sich nicht.

### #241 Sylv'anor

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_241` · L108 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus radix* · Blütenstimmen-Echo |
| Typen | **Blüte / Klang** |
| Archetyp · Größe · Gewicht | A03 Huftier · XL · 4,2 m · 12965,4 kg |
| Region · Lebensraum | R01 · Wurzelhalle unter der Arena von Eichenhall |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Sänger, Hüter, Bestäuber |
| Nischen · Rolle · Reiten | Kampf, Forschung · Support · – |
| Basiswerte | HP 121 · ANG 88 · VER 116 · SAN 110 · SVE 126 · GES 99 = **660** · PRÄ 100 · AUS 102 · Wachstum Late · EP-Ertrag 320 · Schliff HP:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_BELLCHIME` |
| Signatur (Konzept) | Wurzellied: Feldklang – jede Runde heilen alle Verbündeten und Blüte-Fähigkeiten kosten weniger |
| Klangmal | Ein Geweih aus singenden Ästen, an denen Glockenblüten im Takt des Weltlieds läuten |

- **Herkunft:** Die Grundstimme des Wachstums; aus ihrem ersten Ton entsprangen die Wälder Verdanthains.
- **Verhalten:** Schläft unter Eichenhall; ihre Wurzeln durchziehen den Boden der ganzen Region und tragen ihr Atmen.
- **Mythologie:** Die Druiden des Waldes sagen, jeder Baum singe einen Ton aus Sylv'anors Lied.
- **Beziehung zu Menschen:** Die Wildwacht hütet die Wurzelhalle seit ihrer Gründung, ohne zu wissen, wen sie bewacht.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Eichenhall und der Hauptquest Verdanthains. Bindung nur mit Stimmsiegel.

### #242 Orh'gruun

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_242` · L109 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus mons* · Steinstimmen-Echo |
| Typen | **Stein / Schwerkraft** |
| Archetyp · Größe · Gewicht | A11 Panzerträger · XXL · 9,0 m · 127575,0 kg |
| Region · Lebensraum | R02 · Schlund unter Kharsholm |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Hüter, Schläfer, Gesteinsfresser |
| Nischen · Rolle · Reiten | Kampf, Forschung · Tank · – |
| Basiswerte | HP 134 · ANG 101 · VER 145 · SAN 78 · SVE 123 · GES 89 = **670** · PRÄ 100 · AUS 92 · Wachstum Late · EP-Ertrag 320 · Schliff Defense:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_TUNINGFORK` |
| Signatur (Konzept) | Bergschwere: Feldklang – Gegner können die Reihe nicht wechseln, Verbündete VER +2 |
| Klangmal | Ein Panzer wie ein Gebirgsgrat, um den Felsbrocken in eigener Schwerkraft kreisen |

- **Herkunft:** Die Grundstimme der Beständigkeit; ihr Ton gab den Bergen ihre Form.
- **Verhalten:** Schläft im Schlund unter Kharsholm; jedes Beben in Kharsgrat ist ein Atemzug Orh'gruuns.
- **Mythologie:** Die Bergvölker glauben, Kharsgrat sei Orh'gruuns Panzer und sie lebten auf seinem Rücken.
- **Beziehung zu Menschen:** Die Ahnenfelsen Kharsholms sind seit Jahrhunderten zu ihm hin ausgerichtet.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Kharsholm und der Hauptquest Kharsgrats. Bindung nur mit Stimmsiegel.

### #243 Nhael'vesh

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_243` · L110 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus nebularis* · Moorstimmen-Echo |
| Typen | **Gift / Geist** |
| Archetyp · Größe · Gewicht | A05 Vogel · L · 2,9 m · 2134,0 kg |
| Region · Lebensraum | R03 · Versunkener Turm unter Morvenfurt |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Dämmerungsaktiv · Flieger, Einzelgänger, Getarnt |
| Nischen · Rolle · Reiten | Kampf, Forschung · Control · – |
| Basiswerte | HP 110 · ANG 88 · VER 110 · SAN 126 · SVE 116 · GES 110 = **660** · PRÄ 102 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpDefense:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_LANTERN` |
| Signatur (Konzept) | Moorgedächtnis: Feldklang – besiegte Echos beider Seiten hinterlassen Nebel, der Gift überträgt und heilt |
| Klangmal | Ein Reiher mit Schlangenhals, dessen Federn sich in Moordunst auflösen |

- **Herkunft:** Die Grundstimme des Kreislaufs; in ihr wird Verfall zu Erinnerung und Erinnerung zu neuem Leben.
- **Verhalten:** Schläft im versunkenen Turm unter Morvenfurt; ihr Atem ist der Nebel, der über dem Moor liegt.
- **Mythologie:** Die Moorweisen sagen, Nhael'vesh erinnere sich an jedes Leben, das im Moor endete.
- **Beziehung zu Menschen:** Die Freien Stimmen in der Unterstadt halten Nhael'vesh für die Schutzpatronin der Vergessenen.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Morvenfurt und der Hauptquest Morvenmoors. Bindung nur mit Stimmsiegel.

### #244 Thal'assyr

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_244` · L111 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus procellaris* · Gezeitenstimmen-Echo |
| Typen | **Flut / Sturm** |
| Archetyp · Größe · Gewicht | A06 Gleitschwimmer · XXL · 11,0 m · 40000 kg |
| Region · Lebensraum | R06 · Tiefseegrotte vor Saltrand-Hafen |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Schwimmer, Flieger, Wanderer |
| Nischen · Rolle · Reiten | Kampf, Forschung · Speed · – |
| Basiswerte | HP 95 · ANG 123 · VER 89 · SAN 112 · SVE 95 · GES 156 = **670** · PRÄ 96 · AUS 110 · Wachstum Late · EP-Ertrag 320 · Schliff Speed:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_WINDCHIME` |
| Signatur (Konzept) | Gezeitenwende: Feldklang – Reihen beider Seiten tauschen jede zweite Runde; eigene Seite handelt zuerst |
| Klangmal | Flügel, deren Schläge Sturmfronten über das Meer treiben |

- **Herkunft:** Die Grundstimme der Freiheit und des Wandels; aus ihrem Ton entstanden Gezeiten und Winde.
- **Verhalten:** Schläft in der Tiefseegrotte vor Saltrand-Hafen; die Gezeiten folgen ihrem Atem.
- **Mythologie:** Der Gezeitenkult nennt jeden Rochen ein Kind Thal'assyrs.
- **Beziehung zu Menschen:** Der Felsbogen ‚Thal'assyrs Rippe‘ gilt den Seeleuten als heiligster Ort der Küste.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Saltrand-Hafen und der Hauptquest Saltrands. Bindung nur mit Stimmsiegel.

### #245 Ash'kareth

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_245` · L112 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus aenigma* · Wahrheitsstimmen-Echo |
| Typen | **Licht / Arkan** |
| Archetyp · Größe · Gewicht | A02 Vierbeiner schwer · XL · 4,0 m · 11200,0 kg |
| Region · Lebensraum | R04 · Unter dem Sonnenhof von Qasr Sahrun |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Hüter, Sonnenbader, Einzelgänger |
| Nischen · Rolle · Reiten | Kampf, Forschung · Caster · – |
| Basiswerte | HP 100 · ANG 67 · VER 94 · SAN 155 · SVE 116 · GES 133 = **665** · PRÄ 104 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpAttack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_MIRROR` |
| Signatur (Konzept) | Rätselglanz: Feldklang – alle verborgenen Werte und Fähigkeiten werden enthüllt, Täuschungen enden |
| Klangmal | Eine Mähne aus Lichtglyphen, die Fragen in die Luft schreibt |

- **Herkunft:** Die Grundstimme der Wahrheit; in ihrem Licht lässt sich nichts verbergen.
- **Verhalten:** Schläft unter dem Sonnenhof; Trugbilder der Weite sind Träume, die aus ihrem Schlaf aufsteigen.
- **Mythologie:** Die Nomaden sagen, Ash'kareth stelle jedem Wanderer eine Frage – wer lügt, verdurstet.
- **Beziehung zu Menschen:** Qasr Sahruns Herrscher legen ihren Eid auf dem Sonnenhof ab, über Ash'kareths Schlaf.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Qasr Sahrun und der Hauptquest der Weite. Bindung nur mit Stimmsiegel.

### #246 Pyr'thagon

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_246` · L113 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus faber* · Schmiedestimmen-Echo |
| Typen | **Glut / Metall** |
| Archetyp · Größe · Gewicht | A15 Drache · XXL · 8,5 m · 76765,6 kg |
| Region · Lebensraum | R05 · Kraterherz unter Schlackenwehr |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Flieger, Wärmesucher, Hüter |
| Nischen · Rolle · Reiten | Kampf, Forschung · Striker · – |
| Basiswerte | HP 107 · ANG 152 · VER 101 · SAN 79 · SVE 95 · GES 141 = **675** · PRÄ 106 · AUS 96 · Wachstum Late · EP-Ertrag 320 · Schliff Attack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_FOOD_SULFURCANDY` |
| Signatur (Konzept) | Weltenschmiede: Feldklang – jeder Treffer härtet den Anwender (VER +1), Glut-Terrain dauerhaft |
| Klangmal | Schuppen aus gehärtetem Erz, zwischen denen Glut wie geschmolzenes Metall fließt |

- **Herkunft:** Die Grundstimme der Schöpfung durch Zerstörung; ihr Ton schmolz die ersten Erze aus dem Fels.
- **Verhalten:** Schläft im Kraterherz; jeder Ausbruch des Ignar ist ein Traum Pyr'thagons.
- **Mythologie:** Die Schmiedezunft sagt, jedes gute Werkstück trage einen Funken Pyr'thagons in sich.
- **Beziehung zu Menschen:** Kaldrex Vorn hat einen Eid geleistet, den Krater zu hüten, ohne zu wissen, was darunter schläft.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Schlackenwehr und der Hauptquest Ignareths. Bindung nur mit Stimmsiegel.

### #247 Isv'aldr

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_247` · L114 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus memoria* · Polarstimmen-Echo |
| Typen | **Frost / Licht** |
| Archetyp · Größe · Gewicht | A06 Gleitschwimmer · XXL · 9,5 m · 24000 kg |
| Region · Lebensraum | R07 · Gletscherdom unter Hvitmark |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Nachtaktiv · Sänger, Leuchtend, Hüter |
| Nischen · Rolle · Reiten | Kampf, Forschung · Support · – |
| Basiswerte | HP 122 · ANG 89 · VER 116 · SAN 111 · SVE 127 · GES 100 = **665** · PRÄ 100 · AUS 102 · Wachstum Late · EP-Ertrag 320 · Schliff SpDefense:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_AURORAGLASS` |
| Signatur (Konzept) | Aurora der Erhaltung: Feldklang – Werteveränderungen der Verbündeten können nicht entfernt werden |
| Klangmal | Schwingen wie die eines Schwans und ein Leib wie ein Wal, über die Polarlicht fließt |

- **Herkunft:** Die Grundstimme des Gedächtnisses; was sie besingt, vergeht nicht.
- **Verhalten:** Schläft im Gletscherdom; das Polarlicht über Hvitfell ist ihr Lied im Schlaf.
- **Mythologie:** Die Hvitfeller glauben, die Toten wanderten im Polarlicht zu Isv'aldr.
- **Beziehung zu Menschen:** Die Archivare Hvitmarks sehen sich als Diener Isv'aldrs: Erinnern ist ihr Gottesdienst.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Hvitmark und der Hauptquest Hvitfells. Bindung nur mit Stimmsiegel.

### #248 Ka'thurel

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_248` · L115 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus custos* · Erinnerungsstimmen-Echo |
| Typen | **Geist / Arkan** |
| Archetyp · Größe · Gewicht | A13 Konstrukt/Elementar · XL · 5,0 m · 21875,0 kg |
| Region · Lebensraum | R08 · Thronsaal-Gewölbe unter Dorunsruh |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Nachtaktiv · Hüter, Muster-Sammler, Einzelgänger |
| Nischen · Rolle · Reiten | Kampf, Forschung · Control · – |
| Basiswerte | HP 111 · ANG 89 · VER 111 · SAN 127 · SVE 116 · GES 111 = **665** · PRÄ 102 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpDefense:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_GLYPHTOKEN` |
| Signatur (Konzept) | Weltgedächtnis: Feldklang – jede eingesetzte Fähigkeit wird gespeichert; Verbündete können sie einmal kopieren |
| Klangmal | Eine gesichtslose Gestalt aus schwebenden Ruinenfragmenten, auf denen Glyphen wandern |

- **Herkunft:** Die Grundstimme der Erinnerung der Welt; sie bewahrt, was geschah, ob es jemand wissen will oder nicht.
- **Verhalten:** Schläft im Gewölbe unter dem Thronsaal; ihre Fragmente tragen die Geschichte Ael'Doruns.
- **Mythologie:** Die Dorunsruher sagen, Ka'thurel kenne die Antwort auf jede Frage – und schweige aus Gnade.
- **Beziehung zu Menschen:** Die Akademie hält Ka'thurel für die Quelle aller lesbaren Glyphen in den Säulen.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Dorunsruh und der Hauptquest Ael'Doruns. Bindung nur mit Stimmsiegel.

### #249 Prism'aion

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_249` · L116 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus amplificans* · Kristallstimmen-Echo |
| Typen | **Kristall / Klang** |
| Archetyp · Größe · Gewicht | A15 Drache · XXL · 8,0 m · 64000,0 kg |
| Region · Lebensraum | R09 · Resonanzkammer unter Prismara |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Nachtaktiv · Flieger, Leuchtend, Klangorter |
| Nischen · Rolle · Reiten | Kampf, Forschung · Caster · – |
| Basiswerte | HP 101 · ANG 67 · VER 95 · SAN 156 · SVE 117 · GES 134 = **670** · PRÄ 104 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpAttack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_FOOD_CRYSTALSALT` |
| Signatur (Konzept) | Brechung: Feldklang – jeder Klang- oder Kristall-Angriff trifft ein zweites Ziel mit halber Kraft |
| Klangmal | Eine kristallene Drachenschlange, deren Körper Licht in Töne bricht |

- **Herkunft:** Die Grundstimme der Verstärkung und Speicherung; was durch sie hindurchgeht, wird lauter und bleibt.
- **Verhalten:** Schläft in der Resonanzkammer; die Kristalle der Prismtiefen wachsen im Takt ihres Herzschlags.
- **Mythologie:** Die Bergleute glauben, jeder Kristall sei ein erstarrter Ton Prism'aions.
- **Beziehung zu Menschen:** Prismaras Glasmacher verbieten das Schleifen von Kristallen aus der Resonanzkammer.
- *Kodex-Notiz (Stufe 4):* Erwacht nach dem Akkord von Prismara und der Hauptquest der Tiefen. Bindung nur mit Stimmsiegel.

### #250 Aeth'rion

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_250` · L117 · Stufe 1 (Legendary) |
| Wissenschaftlich · Kategorie | *Archisonus dux* · Leitstimmen-Echo |
| Typen | **Klang / Licht** |
| Archetyp · Größe · Gewicht | A05 Vogel · L · 2,9 m · 2134,0 kg |
| Region · Lebensraum | R10 · Sternenarena von Aerion |
| Seltenheit · Bedingungen · Zonen | Legendär · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Flieger, Sänger, Leuchtend |
| Nischen · Rolle · Reiten | Kampf, Forschung · AllRound · – |
| Basiswerte | HP 114 · ANG 114 · VER 113 · SAN 113 · SVE 113 · GES 113 = **680** · PRÄ 100 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpAttack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 3 · Vorliebe `ITM_LURE_STARCHIME` |
| Signatur (Konzept) | Einklang: Feldklang – Eigenklang-Bonus aller Verbündeten wirkt für jeden ihrer Typen |
| Klangmal | Schwingen aus Notenlinien aus Licht, auf denen die Töne aller Stimmen stehen |

- **Herkunft:** Die Leitstimme, die alle anderen Stimmen verbindet; ohne sie zerfällt das Lied in einzelne Töne.
- **Verhalten:** Ruht über der Sternenarena; ihre Wärterin im Erstchor war Ilen.
- **Mythologie:** Die Aerioner nennen den Himmel über der Arena ‚Aeth'rions Notenblatt‘.
- **Beziehung zu Menschen:** Oruma Siyel ist die letzte Hüterin der Sternenarena; sie spricht von Aeth'rion nur in Liedern.
- *Kodex-Notiz (Stufe 4):* Erwacht als letzte Stimme nach dem zehnten Akkord. Bindung nur mit Stimmsiegel.

### #251 Velnox

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_251` · L118 · Stufe 1 (Mythical) |
| Wissenschaftlich · Kategorie | *Pausa silentium* · Pausen-Echo |
| Typen | **Leere / Schwerkraft** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · L · 2,9 m · 600 kg |
| Region · Lebensraum | R10 · Im Riegel unter der Krone von Nimbara |
| Seltenheit · Bedingungen · Zonen | Mythisch · `Spawn.None` · – |
| Aktivität · Merkmale | Nachtaktiv · Einzelgänger, Treiber, Getarnt |
| Nischen · Rolle · Reiten | Kampf, Forschung · Control · – |
| Basiswerte | HP 108 · ANG 87 · VER 108 · SAN 125 · SVE 114 · GES 108 = **650** · PRÄ 102 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpAttack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 2 · Vorliebe `ITM_LURE_BELLCHIME` |
| Signatur (Konzept) | Große Pause: Feldklang – Harmonie beider Seiten wird jede Runde auf null gesetzt; Klang-Fähigkeiten verstummen |
| Klangmal | Ein Körper aus Abwesenheit; Töne in seiner Nähe enden mitten im Klang |

- **Herkunft:** Die Pause selbst – kein Ton, sondern der Raum zwischen den Tönen, den das Weltlied braucht und fürchtet.
- **Verhalten:** Seit der Großen Stille in einem Riegel gebunden; es zieht Klang in sich hinein wie ein Abgrund Licht.
- **Mythologie:** Kein Volk von Aethris kennt seinen Namen; nur in einem einzigen Klangfragment wird er geflüstert.
- **Beziehung zu Menschen:** Der Orden der Stille sucht ohne es zu wissen nach Velnox; die Akademie hält ihn für eine Legende.
- *Kodex-Notiz (Stufe 4):* Begegnung im Finale; bindbar erst im Nachhall. Nicht Ranked-zulässig.

### #252 Chronaire

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_252` · L119 · Stufe 1 (Mythical) |
| Wissenschaftlich · Kategorie | *Metronomus tactus* · Takthüter-Echo |
| Typen | **Klang / Arkan** |
| Archetyp · Größe · Gewicht | A04 Zweibeiner · M · 1,5 m · 590,6 kg |
| Region · Lebensraum | R08 · Zwischen zwei Herzschlägen |
| Seltenheit · Bedingungen · Zonen | Mythisch · `Spawn.None` · – |
| Aktivität · Merkmale | Tagaktiv · Tänzer, Einzelgänger, Leuchtend |
| Nischen · Rolle · Reiten | Kampf, Forschung · Speed · – |
| Basiswerte | HP 91 · ANG 117 · VER 85 · SAN 107 · SVE 91 · GES 149 = **640** · PRÄ 96 · AUS 110 · Wachstum Late · EP-Ertrag 320 · Schliff Speed:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 2 · Vorliebe `ITM_LURE_TUNINGFORK` |
| Signatur (Konzept) | Taktwechsel: Feldklang – die Zeitleiste läuft rückwärts; der langsamste Kämpfer handelt zuerst |
| Klangmal | Eine schmale Gestalt mit Pendel statt Herz, deren Schritte den Takt der Welt angeben |

- **Herkunft:** Der Hüter des Takts; Chronaire existiert in dem Augenblick zwischen zwei Herzschlägen.
- **Verhalten:** Erscheint nur dem, der eine Herausforderung schneller als möglich besteht – und wieder verschwindet.
- **Mythologie:** Musiker schwören, bei perfekten Aufführungen eine zusätzliche Gestalt im Takt tanzen zu sehen.
- **Beziehung zu Menschen:** Die Akademie führt Chronaire als ‚unbewiesenes Phänomen T‘ in ihren Akten.
- *Kodex-Notiz (Stufe 4):* Zugang über die Zeitherausforderungen des Endspiels.

### #253 Mirrowisp

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_253` · L120 · Stufe 1 (Mythical) |
| Wissenschaftlich · Kategorie | *Speculum imago* · Spiegel-Echo |
| Typen | **Kristall / Geist** |
| Archetyp · Größe · Gewicht | A12 Schwebend amorph · S · 0,7 m · 10 kg |
| Region · Lebensraum | R09 · Nur auf Fotografien sichtbar |
| Seltenheit · Bedingungen · Zonen | Mythisch · `Spawn.None` · – |
| Aktivität · Merkmale | Dämmerungsaktiv · Nachahmer, Scheu, Leuchtend |
| Nischen · Rolle · Reiten | Kampf, Forschung · Control · – |
| Basiswerte | HP 105 · ANG 84 · VER 105 · SAN 121 · SVE 110 · GES 105 = **630** · PRÄ 102 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpDefense:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 2 · Vorliebe `ITM_LURE_MIRROR` |
| Signatur (Konzept) | Spiegelwelt: Feldklang – jeder Angriff trifft zusätzlich ein Spiegelbild des Angreifers |
| Klangmal | Ein Lichtwesen, das auf Fotos scharf und mit bloßem Auge unsichtbar ist |

- **Herkunft:** Ein Spiegelbild, das sich selbstständig gemacht hat und nun ein eigenes Leben führt.
- **Verhalten:** Erscheint nur auf Fotografien – im Hintergrund, im Glas, in einer Pfütze.
- **Mythologie:** Fotografen hängen ihre misslungenen Bilder auf, weil Mirrowisp sich gern darin versteckt.
- **Beziehung zu Menschen:** Die Kodex-Linse wurde angeblich erfunden, um Mirrowisp zu beweisen.
- *Kodex-Notiz (Stufe 4):* Zugang über die Fotografie-Meisterschaft.

### #254 Ouroveth

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_254` · L121 · Stufe 1 (Mythical) |
| Wissenschaftlich · Kategorie | *Ouroboros perpetuus* · Kreislaufschlangen-Echo |
| Typen | **Gift / Blüte** |
| Archetyp · Größe · Gewicht | A07 Schlange/Wurm · XXL · 8,5 m · 30000 kg |
| Region · Lebensraum | R03 · Wo Verfall in Wachstum übergeht |
| Seltenheit · Bedingungen · Zonen | Mythisch · `Spawn.None` · – |
| Aktivität · Merkmale | Dämmerungsaktiv · Einzelgänger, Bestäuber, Getarnt |
| Nischen · Rolle · Reiten | Kampf, Zucht · Tank · – |
| Basiswerte | HP 130 · ANG 97 · VER 141 · SAN 76 · SVE 119 · GES 87 = **650** · PRÄ 100 · AUS 92 · Wachstum Late · EP-Ertrag 320 · Schliff HP:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 2 · Vorliebe `ITM_FOOD_MOORBERRY` |
| Signatur (Konzept) | Ewiger Kreis: Feldklang – Gift heilt Verbündete und schadet Gegnern; besiegte Verbündete keimen einmal neu |
| Klangmal | Eine Schlange, die blüht, wo sie verwest – vorne Knospen, hinten Moder |

- **Herkunft:** Der ewige Kreislauf aus Verfall und Wachstum, verkörpert als Schlange, die sich selbst erneuert.
- **Verhalten:** Zieht durch Orte, an denen etwas stirbt und etwas Neues entsteht; bleibt nie lange.
- **Mythologie:** Die Moorweisen behaupten, jede Blume auf einem Grab sei eine Schuppe Ouroveths.
- **Beziehung zu Menschen:** Züchter verehren Ouroveth als Schutzpatron ihres Handwerks.
- *Kodex-Notiz (Stufe 4):* Zugang über die Zucht-Meisterschaft.

### #255 Zenthrax

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_255` · L122 · Stufe 1 (Mythical) |
| Wissenschaftlich · Kategorie | *Astrometallum caducus* · Sternfall-Echo |
| Typen | **Schwerkraft / Metall** |
| Archetyp · Größe · Gewicht | A15 Drache · XXL · 10,0 m · 125000,0 kg |
| Region · Lebensraum | R05 · Tiefenresonanz eines Sternenfalls |
| Seltenheit · Bedingungen · Zonen | Mythisch · `Spawn.None` · – |
| Aktivität · Merkmale | Nachtaktiv · Flieger, Einzelgänger, Sternschauer |
| Nischen · Rolle · Reiten | Kampf, Forschung · Striker · – |
| Basiswerte | HP 104 · ANG 149 · VER 99 · SAN 77 · SVE 93 · GES 138 = **660** · PRÄ 106 · AUS 96 · Wachstum Late · EP-Ertrag 320 · Schliff Attack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 2 · Vorliebe `ITM_LURE_STARCHIME` |
| Signatur (Konzept) | Sternensturz: Feldklang – jede Runde schlägt ein Meteor auf ein zufälliges Feld; Schwerkraft verdoppelt |
| Klangmal | Ein Drachenleib aus dunklem Sternenmetall mit einem Herzen, das wie ein fallender Stern glüht |

- **Herkunft:** Ein gefallener Stern, dessen Herz aus Sternenmetall in der Tiefe weiterschlägt.
- **Verhalten:** Ruht in einer Tiefenresonanz; wenn er erwacht, beginnt die Erde nach oben zu fallen.
- **Mythologie:** Die Bergleute erzählen vom ‚Stern unter dem Berg‘, der in klaren Nächten zurückwill.
- **Beziehung zu Menschen:** Das Goldklang-Kontor hat eine Expedition finanziert, die nie zurückkehrte.
- *Kodex-Notiz (Stufe 4):* Zugang über Raid RAID_06 oder die Solo-Tiefenresonanz DR_08.

### #256 Aurelune

| Feld | Wert |
|---|---|
| Id · Linie · Stufe | `ECHO_256` · L123 · Stufe 1 (Mythical) |
| Wissenschaftlich · Kategorie | *Eclipsis obscurans* · Finsternis-Echo |
| Typen | **Licht / Leere** |
| Archetyp · Größe · Gewicht | A15 Drache · XL · 5,5 m · 20796,9 kg |
| Region · Lebensraum | R10 · Nachthimmel während eines Resonanzsturms |
| Seltenheit · Bedingungen · Zonen | Mythisch · `Spawn.None` · – |
| Aktivität · Merkmale | Nachtaktiv · Flieger, Leuchtend, Einzelgänger |
| Nischen · Rolle · Reiten | Kampf, Forschung · Caster · – |
| Basiswerte | HP 98 · ANG 65 · VER 93 · SAN 153 · SVE 115 · GES 131 = **655** · PRÄ 104 · AUS 100 · Wachstum Late · EP-Ertrag 320 · Schliff SpAttack:3 |
| Evolution | keine weitere Entwicklung |
| Bindung | Rate 2 · Vorliebe `ITM_LURE_AURORAGLASS` |
| Signatur (Konzept) | Finsternis: Feldklang – Licht- und Leere-Angriffe tauschen ihre Typvorteile |
| Klangmal | Ein Drache mit einem Ring aus Licht um einen schwarzen Kern, wie eine Sonnenfinsternis |

- **Herkunft:** Ein Echo der Finsternis, in dem Licht und Leere einander umkreisen, ohne sich zu berühren.
- **Verhalten:** Erscheint nur nachts während eines Resonanzsturms; danach bleibt ein Ring am Himmel zurück.
- **Mythologie:** Die Aerioner nennen den Ring nach dem Sturm ‚Aurelunes Auge‘ und schließen die Fenster.
- **Beziehung zu Menschen:** Die Akademie zeichnet jeden Resonanzsturm auf – in der Hoffnung, Aurelune zu messen.
- *Kodex-Notiz (Stufe 4):* Zugang über das Resonanzsturm-Ereignis oder den storygebundenen Solo-Sturm im Nachhall.


## Kapitel-Checkliste

- [x] 32 Arten mit allen Briefing-Basisdaten (Name, wissenschaftlicher Name, Kategorie, Größe, Gewicht, Lebensraum, Seltenheit)
- [x] Lore je Art: Herkunft, Verhalten, Mythologie, Beziehung zu Menschen (+ Kodex-Notiz)
- [x] Evolution je Linie mit geprüfter Bedingung (K19-Sprache)
- [x] Basiswerte innerhalb der Spannen (K16 §6), Wachstum, EP-/Schliff-Ertrag (K18)
- [x] Verhalten, Aktivität, Nischen, Rolle, Bindungsdaten, Klangmal, Signaturkonzept
- [x] Typverteilung der Region(en) gemäß CANON §45 (Validator)
- [x] Daten im Repository, Kapitel generiert

➡️ **Nächstes Kapitel: K28 – Fähigkeiten I: System, aktive Fähigkeiten (ABL_A001–ABL_A180).**
