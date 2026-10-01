# K38 · Zucht und Genetik

| Feld | Wert |
|---|---|
| Dokument | Kapitel 38 von 68 · Systeme, Teil III |
| Version | 1.0 |
| Owner | Lead Systems Designer (Erbe) |
| Mitwirkende | Creature Design Lead, Technical Artist (Loci-Shader, Morph-Paletten), Online-Programmierer (Genom-Plausibilität), Economy Designer, UX Lead (Zuchtbuch) |
| Baut auf | S4 „Erbe“, ADR-025 (geschlechtsunabhängig), DR-15/16/17/18, CANON §18 (Zucht ab Rang 14), §29 (Seed-Hierarchie, Fork(3) Zucht), §80 (Anlagen, Klangstimmung), §102 (versteckte Passive über Zucht), §104 (Ei-Fähigkeiten), §137 (Gezüchtete starten mit 120), §140 (Brutnischen im Hain) |
| Status | ✅ Freigegeben – **löst Q3** (Allelanzahl, Morph-Wahrscheinlichkeiten) |
| Im Repository | `Data/Echos/GeneticLoci.csv` (6 Loci), `Data/Items/BreedingItems.csv` (6), `tools/ref/aethris_genetics.py` (Vererbung, DR-18-Simulation) |
| Neue Kanon-Einträge | CANON §141 (Zuchtregeln), §142 (Vererbung), §143 (Loci & Morphs), §144 (Zucht-Meisterschaft), §145 (Online-Genom) |

---

## Inhalt

1. [Erbe als Säule](#1-erbe-als-säule)
2. [Voraussetzungen und Resonanzgruppen](#2-voraussetzungen-und-resonanzgruppen)
3. [Ablauf: vom Paar zum Schlüpfling](#3-ablauf-vom-paar-zum-schlüpfling)
4. [Vererbung](#4-vererbung)
5. [Loci – die sichtbare Genetik](#5-loci--die-sichtbare-genetik)
6. [Morphs und Mutationen](#6-morphs-und-mutationen)
7. [Zucht-Gegenstände](#7-zucht-gegenstände)
8. [DR-18: das perfekte Echo in ≤ 15 Stunden](#8-dr-18-das-perfekte-echo-in--15-stunden)
9. [Zuchtbuch und Zucht-Meisterschaft](#9-zuchtbuch-und-zucht-meisterschaft)
10. [Online, Tausch und Plausibilität](#10-online-tausch-und-plausibilität)
11. [Code](#11-code)
12. [Tests und Telemetrie](#12-tests-und-telemetrie)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Erbe als Säule

Säule S4 „Erbe“ verspricht: *Jedes Echo trägt eine Geschichte, und ich kann Generationen formen.* Zucht ist in AETHRIS kein Nebenmenü, sondern ein Hain-Handwerk mit drei Zielgruppen:

| Spielertyp | Ziel | Werkzeug |
|---|---|---|
| Sammler | Arten vervollständigen (nicht gewählte Starter, Evolutionsformen) | Artvererbung, Zuchtbuch |
| Ästhet | besondere Optik (Grundton, Muster, Leuchten, Morphs) | Loci, Morph-Faktoren |
| Wettkämpfer | perfekte Anlagen, Wunsch-Persönlichkeit, Ei-Fähigkeiten | Erbklang, Wesensband, Stimmband |

**Leitplanken:** geschlechtsunabhängig (ADR-025, Echos sind Neutrum), keine käuflichen Werte oder Morphs (CANON §8), Zufall nur dort, wo DR-15 ihn erlaubt (Morphs, Anlagen-Anteil) – und immer mit sichtbaren Wahrscheinlichkeiten (DR-07).

---

## 2. Voraussetzungen und Resonanzgruppen

| Regel | Wert |
|---|---|
| Freischaltung | Wärterrang 14 (Ende Akt I, CANON §15) |
| Ort | Brutnische im Resonanzhain (Garten-Ausbau Stufe 3; max. 10 Nischen) |
| Paar | zwei Echos derselben **Resonanzgruppe** oder derselben Art; beide Bindungsstufe ≥ 2 („sie vertrauen dem Wärter“) |
| Ausgeschlossen | Ursprungsstimmen, Mythische, Stille-Echos (geheilt dürfen sie), Leih-Echos |
| Geschlecht | keines – jedes Paar ist möglich; der Spieler wählt, welcher Elternteil die **Art** bestimmt („Träger“) |

**Resonanzgruppen** entsprechen den zehn Stämmen (Phyla) der Archetypen (K16, `Archetypes.csv`):

| Gruppe (Phylum) | Archetypen | Beispiel-Paarung |
|---|---|---|
| Quadrupedia | A01, A02, A03 | Snevar × Dunhorn |
| Volantia | A05, A06, A15 | Brikin × Ignavyr |
| Aquatica | A08, A09, A17 | Aquapip × Pyrolm |
| Serpentia | A07 | Sengel × Spatling |
| Articulata | A10 | Skarit × Ligrel |
| Testudinia | A11 | Mesakil × Obsikin |
| Spectralia | A12, A16 | Fumel × Glazil |
| Elementia | A13 | Ambolt × Vardlit |
| Botanica | A14 | Tangi × Hymlit |
| Bipedia | A04, A18 | Skriv × Drusil |

Gruppenübergreifende Paarungen sind nicht möglich. Damit hat jede Art 5–40 mögliche Partnerarten – genug für Vielfalt, wenig genug, um Zuchtwissen wertvoll zu machen (Kodex Stufe 3 zeigt die Gruppe).

---

## 3. Ablauf: vom Paar zum Schlüpfling

```
  Brutnische ──(alle 15 Spielminuten)──► Resonanzkeim ──(Reife durch Spielzeit)──► Schlüpfen
      ▲                                     │ Keimtasche (6 Plätze)                     │
      └── Paar bleibt, bis der Spieler      │ Reife: 10 (Häufig) … 25 (Sehr selten) Min. │
          es trennt                         └── Keimwärmer: ×2                          ▼
                                                                         Schlüpfling Lv. 1, Bindung 120
```

| Schritt | Regel |
|---|---|
| Keimbildung | je besetzter Brutnische ein **Resonanzkeim** pro 15 Minuten **Spielzeit** (nicht Echtzeit, DR-23); bis zu 3 Keime warten in der Nische |
| Tragen | Keimtasche mit 6 Plätzen; Keime reifen, solange der Spieler spielt (jede Aktivität) |
| Reife | Häufig 10 · Ungewöhnlich 15 · Selten 20 · Sehr selten 25 Spielminuten; Keimwärmer halbiert |
| Schlüpfen | kurze Szene (≤ 4 s, überspringbar), Herkunft: Methode Zucht, Eltern, Ort, Wetter, Tageszeit (DR-16) |
| Start | Lv. 1, Bindung 120, Schlüpfling kennt die Ei-Fähigkeiten seiner Eltern (§4.6) |
| Durchsatz | bei 3 Nischen ≈ 12 Keime je Spielstunde – Grundlage der DR-18-Rechnung |

**Art des Schlüpflings:** die **Stufe-1-Form der Linie des Trägers** (bei Zweigformen die Stufe 1 der Grundlinie). Nicht gewählte Starter sind so über Zucht erhältlich (ADR-077).

---

## 4. Vererbung

### 4.1 Anlagen

Für jeden der 8 Werte (HP, ANG, VER, SAN, SVE, GES, PRÄ, AUS):

```
400 ‰  Wert von Elternteil A
400 ‰  Wert von Elternteil B
200 ‰  neu (0–15 gleichverteilt)
Erbklang: 4 vom Spieler gewählte Werte sicher vom gewählten Elternteil
```

Die Zuchtvorschau zeigt für jeden Wert die möglichen Ergebnisse mit Wahrscheinlichkeit (z. B. „GES: 15 (40 %) · 9 (40 %) · zufällig (20 %)“) – Transparenz statt Glücksgefühl (DR-07).

### 4.2 Persönlichkeit und Temperament

| Merkmal | Regel | Hilfsmittel |
|---|---|---|
| Persönlichkeit | 50 % Elternteil A, 50 % B | Wesensband: sicher vom Träger des Bandes |
| Temperament | 40 % A, 40 % B, 20 % zufällig | Stimmband: sicher vom Träger |

### 4.3 Passive

| Passive | Regel |
|---|---|
| sichtbare Option | 70 % die Option des Trägers (Position wird auf die Art abgebildet), sonst zufällig unter den sichtbaren Optionen |
| versteckte Passive | Hat ein Elternteil die versteckte Passive aktiv: 50 % Vererbung (CANON §102) |

### 4.4 Größe, Klangmal, Stimme

Über die Loci (§5) – rein optisch.

### 4.5 Bindung, Level, Schliff

Nicht vererbt: Bindung (Start 120), Level (1), Schliff (0), Repertoire außer Ei-Fähigkeiten.

### 4.6 Ei-Fähigkeiten

Kennt ein Elternteil eine Fähigkeit, die im Lernset der Schlüpflingsart als **Egg** geführt ist (`Learnsets.csv`, 321 Einträge), lernt der Schlüpfling sie beim Schlüpfen (max. 4). Damit werden Status-Fähigkeiten fremder Typen zu Zuchtzielen – ein Grund, Echos verschiedener Linien zu kombinieren.

---

## 5. Loci – die sichtbare Genetik

Sechs Loci steuern Optik und Stimme (DR-17: Optik nur durch Genetik, Fundort, Leistung). **Q3 gelöst:** 6 Loci mit je 2–4 Allelen, Mendelsche Vererbung (je Locus ein Allel von jedem Elternteil, je 50 %).

| DisplayName | Alleles | Effect | WildFrequencyRule |
|---|---|---|---|
| Grundton | H0:Artfarbe:2|H1:Warmton:1|H2:Kaltton:1|H3:Fahlton:0 | Farbton der Hauptpalette ±18° (intermediär bei H1/H2 = Mischton) | H0 85 %, H1/H2 je 7 % (Region warm/kalt), H3 1 % |
| Musterung | P0:Artmuster:2|P1:Gesprenkelt:1|P2:Gestreift:1 | Musterkanal der Haut/Federn/Panzer | P0 90 %, P1/P2 je 5 % |
| Klangmal-Leuchten | G1:Normal:1|G0:Hell:0 | Rezessiv: G0G0 → Klangmal leuchtet doppelt hell | G0-Allel 10 % |
| Größe | S0:Klein:1|S1:Mittel:1|S2:Groß:1 | Intermediär: Körpergröße 92 % / 100 % / 108 % (Mittelwert der Allele) | S1 80 %, S0/S2 je 10 % |
| Stimmlage | V0:Tief:1|V1:Mittel:2|V2:Hoch:1 | Tonhöhe der Rufe ±3 Halbtöne (Audio K55) | V1 70 %, V0/V2 je 15 % |
| Klangmal-Form | M0:Artform:1|M1:Gespiegelt:0 | Rezessiv: M1M1 → Klangmal gespiegelt (Sammlerreiz) | M1-Allel 5 % |

**Beispiel (Klangmal-Leuchten, rezessiv):** Zwei Echos mit G1G0 („Träger“, normal leuchtend):

```
            G1        G0
      ┌──────────┬──────────┐
  G1  │  G1G1    │  G1G0    │   normal 75 %
      │  normal  │  normal  │
      ├──────────┼──────────┤
  G0  │  G1G0    │  G0G0    │   hell 25 %
      │  normal  │  HELL    │
      └──────────┴──────────┘
```

Ab Kodex-Stufe 4 und Wärter-Skill „Erbkunde“ (K43) zeigt der Kodex die **Allele** eines Echos; vorher nur die Ausprägung. **Regionale Häufigkeiten:** Warmton (H1) häufiger in R04/R05, Kaltton (H2) in R07/R10 – Fundort prägt die Optik (DR-17).

---

## 6. Morphs und Mutationen

**Morphs** sind seltene Farbvarianten mit eigener Palette (Klangmal invertiert, Typfarbe als Hauptton). Sie sind der einzige Ort, an dem reiner Zufall herrscht (DR-15).

| Faktor | Morph-Chance (von 1.024) |
|---|---|
| Grundchance (Wild und Zucht) | 1 (≈ 0,1 %) |
| Fernklang (ein Elternteil getauscht aus fernster Region) | ×3 |
| Skill „Morphkunde“ (K43) | ×2 |
| Geschlüpft/angetroffen im Resonanzsturm | ×2 |
| **Maximum** | **12 / 1.024 ≈ 1,2 %** |

- Morphs vererben sich **nicht** sicher: Ein Morph-Elternteil verdoppelt die Chance (zählt als weiterer Faktor ×2, max. 24/1.024).
- Morphs sind im Kampf identisch (keine Werte), sichtbar in der Welt (Funkeln + eigener Ton, DR-24) und im Kodex gezählt.
- **Mutationen** (`Genome.Mutations`): seltene Zusatzmerkmale ohne Kampfwirkung, z. B. `Mutation.DoubleMark` (zweites Klangmal), `Mutation.Heterochromia`. Chance 1/2.048 je Schlüpfling; Liste wächst über LiveOps (K68).

---

## 7. Zucht-Gegenstände

| DisplayName | Effect | Reusable | Sources |
|---|---|---|---|
| Erbklang | Vererbt 4 vom Spieler gewählte Anlagen sicher vom gewählten Elternteil | nein | Crafting (Kristall + Obertonkristall) · Akademie Ruf 2 |
| Wesensband | Persönlichkeit des Trägers wird sicher vererbt | ja (Halteitem) | Crafting · Wildwacht Ruf 2 |
| Stimmband | Temperament des Trägers wird sicher vererbt | ja (Halteitem) | Crafting · Freie Stimmen Ruf 2 |
| Keimwärmer | Reife des Resonanzkeims ×2 für 1 Keim | nein | Crafting (Glut-Material) · Hain-Ertrag |
| Fernklang-Brief | Zählt als Elternteil aus fernster Region (Morph-Faktor ×3), wenn ein Elternteil getauscht wurde | – | Automatisch bei Tausch (K60) – kein Item im Inventar |
| Klangstimmung | Setzt eine Anlage eines Echos auf 15 (Endgame, CANON §80) | nein | Endgame-Crafting (Tiefenresonanz-Material) |

Kein Zucht-Gegenstand ist im Shop gegen Echtgeld erhältlich (CANON §8); alle stammen aus Crafting, Hain-Ertrag oder Fraktionsruf.

---

## 8. DR-18: das perfekte Echo in ≤ 15 Stunden

DR-18 verlangt: *Ein kompetitiv perfektes Echo ist in ≤ 15 h züchtbar.* Die Simulation (`aethris_genetics.dr18_table`, 300 Läufe je Zeile) nutzt die Regeln dieses Kapitels: zwei wilde, seltene Eltern (je 2 garantierte 15er), gierige Strategie (bestes Kind ersetzt schwächeren Elternteil), 12 Keime je Spielstunde:

| Ziel | Strategie | Ø Keime | Median | P90 | Ø Spielstunden (12 Keime/h) |
|---|---|---|---|---|---|
| 6 Kernwerte auf 15 | ohne Hilfsmittel | 359 | 309 | 690 | 29,9 h |
| 6 Kernwerte auf 15 | mit Erbklang | 171 | 158 | 305 | 14,2 h |
| 5 Werte (ein Angriffswert egal) | ohne Hilfsmittel | 278 | 232 | 533 | 23,2 h |
| 5 Werte (ein Angriffswert egal) | mit Erbklang | 144 | 118 | 283 | 12,0 h |

**Ergebnis:** Mit Erbklang wird ein Echo mit sechs Kernwerten auf 15 im Mittel in **14,2 h** erreicht; das kompetitiv übliche Ziel (fünf Werte, ein Angriffswert egal) in 12 h. DR-18 ist erfüllt. Ohne Hilfsmittel dauert es etwa doppelt so lange – Erbklang ist damit das zentrale Zuchtwerkzeug und bewusst über Crafting und Akademie-Ruf erreichbar. Die Endgame-**Klangstimmung** (eine Anlage auf 15, CANON §80) verkürzt den Rest weiter.

---

## 9. Zuchtbuch und Zucht-Meisterschaft

Das **Zuchtbuch** (Kodex-Reiter, K39) protokolliert jede Zucht: Eltern, Schlüpfling, Allele, Morphs, Generationen. Meilensteine:

| Meilenstein | Belohnung |
|---|---|
| 10 Arten geschlüpft | Keimtasche +2 Plätze |
| 25 Arten geschlüpft | Brutnischen produzieren alle 12 statt 15 Minuten |
| 1 Morph geschlüpft | Titel „Farbenhüter“ |
| 1 Echo mit 6 × 15 | Erbklang-Rezept „Meister“ (5 sichere Werte) |
| 50 Arten geschlüpft **und** 5 Morphs **und** 1 Echo mit 6 × 15 | **Zucht-Meisterschaft** → Questreihe „Der Kreis schließt sich“ zum Mythischen **Ouroveth** (CANON §34, K62) |

---

## 10. Online, Tausch und Plausibilität

| Regel | Wert |
|---|---|
| Plausibilitätsprüfung | Server prüft beim Tausch/Ranked: Anlagen 0–15, Loci gültig, Morph-Herkunft plausibel (Zucht-Seed + Eltern-Signaturen oder Wildfang-Signatur), Lernset-Erreichbarkeit (K59) |
| Signatur | Offline gezüchtete Echos erhalten beim ersten Online-Kontakt eine Signatur nach Prüfung (CANON §29 `Origin.Signature`) |
| Fernklang | Ein getauschtes Echo zählt als „fern“, wenn seine Herkunftsregion ≥ 3 Regionen vom Heimatgarten des Partners entfernt ist (Regionsabstand auf der Makrokarte, K08) |
| Ranked | gezüchtete und gebundene Echos gleichwertig; Plausibilität Pflicht (DR-21) |

---

## 11. Code

```cpp
// GF_Breeding – Zucht (deterministisch über Fork(3) der Weltsaat + Keimzähler)
FEchoGenome UBreedingService::InheritGenome(const FEchoInstance& A, const FEchoInstance& B, const FBreedingOptions& O, FAethrisRandom& Rng) const
{
    FEchoGenome G;
    const int32* PA = &A.Genome.Aptitudes.HP; const int32* PB = &B.Genome.Aptitudes.HP;   // 8 aufeinanderfolgende int32
    int32* PC = &G.Aptitudes.HP;
    for (int32 i = 0; i < 8; ++i)
    {
        if (O.ErbklangStats.Contains(i)) { PC[i] = (O.ErbklangParent == 0 ? PA : PB)[i]; continue; }
        const uint32 R = Rng.NextBounded(1000);
        PC[i] = R < 400 ? PA[i] : (R < 800 ? PB[i] : int32(Rng.NextBounded(16)));
    }
    for (const FEchoAllelePair& LA : A.Genome.Loci)                                          // Mendel je Locus
    {
        const FEchoAllelePair* LB = B.Genome.Loci.FindByPredicate([&](const FEchoAllelePair& X) { return X.Locus == LA.Locus; });
        FEchoAllelePair& LC = G.Loci.AddDefaulted_GetRef();
        LC.Locus = LA.Locus;
        LC.A = Rng.NextBounded(2) ? LA.A : LA.B;
        LC.B = LB ? (Rng.NextBounded(2) ? LB->A : LB->B) : LC.A;
    }
    const int32 MorphPer1024 = Aethris::Genetics::MorphChance(O.bFernklang, O.bMorphSkill, O.bResonanceStorm, A.Genome.Morph != NAME_None || B.Genome.Morph != NAME_None);
    G.Morph = Rng.NextBounded(1024) < uint32(MorphPer1024) ? Species->RollMorph(Rng) : NAME_None;
    return G;
}
```

---

## 12. Tests und Telemetrie

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Breeding.Groups` | Kompatibilität nach Phylum, Ausschlüsse |
| `…Breeding.Aptitudes` | Verteilung 400/400/200 ‰ über 100.000 Kinder (χ²) |
| `…Breeding.Erbklang` | 4 sichere Werte |
| `…Breeding.Mendel` | Locus-Verteilungen (rezessiv 25 %) |
| `…Breeding.MorphCap` | Deckel 24/1.024 |
| `…Breeding.PythonParity` | 10.000 Kinder gegen `aethris_genetics.py` |
| `Aethris.Func.Breeding.DR18` | Nightly-Simulation: Ø ≤ 15 h |

**Telemetrie:** Keime je Spielstunde, Anteil Spieler mit Zucht nach Rang 14, Zeit bis erstes 6×15-Echo, Morph-Funde je 1.000 Schlüpflinge (Soll ≈ 1–3).

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-139 | Resonanzgruppen = 10 Phyla | Konsistent mit Rig-Taxonomie, lernbar | freie Paarung (beliebig), Einzelgruppen je Art (zu eng) |
| ADR-140 | Keime reifen durch Spielzeit, nicht Echtzeit oder Schritte | DR-23, Clean-Room | Echtzeit-Timer, Schrittzähler |
| ADR-141 | Anlagen 400/400/200 ‰ + Erbklang (4 sicher) | DR-18 (Ø 14,2 h) bei sichtbaren Wahrscheinlichkeiten | Reiner Zufall (zu lang), volle Kontrolle (keine Spannung) |
| ADR-142 | Morph-Grundchance 1/1.024, Faktoren bis 12/1.024 (Morph-Eltern 24) | Seltenheit mit Einfluss ohne Grind-Wand | Morphs käuflich (CANON §8), feste Morph-Quests |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §141 | Zucht ab Rang 14 in Brutnischen (Hain-Ausbau 3, max. 10); Paar gleiche Art oder gleiche Resonanzgruppe (10 Phyla), beide Bindungsstufe ≥ 2; keine Stimmen/Mythischen; Keim je 15 Spielminuten, Reife 10/15/20/25 Spielminuten, Keimtasche 6; Schlüpfling = Stufe 1 der Linie des Trägers, Lv. 1, Bindung 120 | LOCKED |
| §142 | Anlagen 400/400/200 ‰, Erbklang 4 sichere Werte; Persönlichkeit 50/50 (Wesensband sicher); Temperament 40/40/20 (Stimmband sicher); Passive 70 % Träger-Option, versteckte 50 %; Ei-Fähigkeiten max. 4; Vorschau zeigt Wahrscheinlichkeiten | LOCKED |
| §143 | 6 Loci (`GeneticLoci.csv`, 2–4 Allele, Mendel); Morph 1/1.024 × Fernklang 3 × Skill 2 × Resonanzsturm 2 (max. 12, mit Morph-Elternteil 24); Mutationen 1/2.048; alles ohne Kampfwirkung – **Q3 gelöst** | LOCKED |
| §144 | Zuchtbuch-Meilensteine; Zucht-Meisterschaft (50 Arten + 5 Morphs + 6×15) → Ouroveth | LOCKED |
| §145 | Online-Plausibilität und Signatur gezüchteter Echos; Fernklang ab 3 Regionen Abstand | LOCKED |
| §10 | ADR-139 – ADR-142 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Zuchtregeln, Resonanzgruppen (10), Ausschlüsse
- [x] Ablauf ohne Echtzeit-Timer (Keime, Reife, Schlüpfen)
- [x] Vererbung von Anlagen, Persönlichkeit, Temperament, Passiven, Ei-Fähigkeiten
- [x] 6 genetische Loci (Q3) mit Mendel-Vererbung und regionalen Häufigkeiten
- [x] Morphs und Mutationen mit Faktoren und Deckel
- [x] Zucht-Gegenstände als Daten
- [x] DR-18-Nachweis per Simulation (Ø 14,2 h)
- [x] Zuchtbuch, Zucht-Meisterschaft (Ouroveth), Online-Plausibilität
- [x] Code, Tests, Telemetrie, ADR-139 – ADR-142, CANON §141–§145

➡️ **Nächstes Kapitel: K39 – Forschung: Echo-Kodex, Klangfragmente und Fotografie (Kodex-Linse).**
