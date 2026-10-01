# K37 · Begleiter, Bindungsstufen und Resonanzhain

| Feld | Wert |
|---|---|
| Dokument | Kapitel 37 von 68 · Systeme, Teil II |
| Version | 1.0 |
| Owner | Lead Systems Designer (Begleiter) |
| Mitwirkende | Animation Director (Begleiter-Verhalten), Lead AI Programmer (Folge-KI), Level Design (Hain), Economy Designer (Hain-Ausbau), UX Lead (Begleiter-Rad), Audio (Echo-Laute) |
| Baut auf | S2 „Bindung durch Verstehen“, DR-04 (Echos reagieren), DR-16 (Herkunft), CANON §5 (Bindungswert 0–1000), §6 (Resonanzhain), §18 (Bindungsstufen 6, Gehorsam, Crescendo ab 2, Feld ab 1), §81 (Lieblingsinteraktion je Persönlichkeit), K36 (Startwerte), ADR-014, ADR-091 |
| Status | ✅ Freigegeben – **löst Q8** (Bindungsstufen 0–1000) |
| Im Repository | `Data/Echos/BondTiers.csv` (6), `Data/Echos/BondActions.csv` (14), `Data/World/SanctuaryGardens.csv` (10 Gärten), `tools/ref/aethris_bond_progress.py` |
| Neue Kanon-Einträge | CANON §137 (Bindungsstufen), §138 (Bindungshandlungen & Stimmung), §139 (Begleiter in der Welt), §140 (Resonanzhain) |

---

## Inhalt

1. [Die Partner-Fantasie](#1-die-partner-fantasie)
2. [Bindungsstufen (Q8)](#2-bindungsstufen-q8)
3. [Bindungshandlungen](#3-bindungshandlungen)
4. [Fortschritt über die Spielzeit](#4-fortschritt-über-die-spielzeit)
5. [Stimmung](#5-stimmung)
6. [Der Begleiter in der Welt](#6-der-begleiter-in-der-welt)
7. [Lager-Momente](#7-lager-momente)
8. [Der Resonanzhain](#8-der-resonanzhain)
9. [Gehorsam und Tausch](#9-gehorsam-und-tausch)
10. [Code](#10-code)
11. [Tests und Telemetrie](#11-tests-und-telemetrie)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Die Partner-Fantasie

> *Mein Brokkar trottet neben mir her, schnuppert an einem Felsen und stupst mich an – darunter liegt Erz. Als die Wolken dunkel werden, drängt er mich unter den Überhang. Ich habe ihn nicht programmiert. Er kennt mich.*

Echos sind keine Inventargegenstände. Säule S2 verlangt, dass Spieler ihre Echos als **Partner** erleben: Sie reagieren sichtbar auf den Spieler (DR-04), haben Vorlieben (Persönlichkeit, Lieblingsfutter), Stimmungen (Wetter, Biom) und eine wachsende Beziehung (Bindungswert), die spürbar etwas freischaltet – **ohne** dass Pflege zur Pflicht wird.

| Ziel | Messgröße |
|---|---|
| Echos wirken lebendig | Playtest: ≥ 80 % nennen ein Begleiter-Verhalten, das sie überrascht hat |
| Bindung lohnt sich | Bindungsstufe 3 mit dem Lieblings-Echo nach ≤ 10 h Spielzeit |
| Keine Pflicht | Reine Kämpfer erreichen alle Stufen höchstens 50 % langsamer als Pfleger |
| Keine Strafe | Niederlage und Pause senken nie eine Stufe (ADR-014) |

---

## 2. Bindungsstufen (Q8)

Der Bindungswert (0–1000, CANON §5) wird in **sechs Stufen** gelesen. Jede Stufe schaltet eine Sache frei, die man *spürt*:

| Tier | DisplayName | MinValue | Unlocks |
|---|---|---|---|
| 1 | Vorsichtig | 0 | Feldfähigkeit (CANON §18); Begleiter folgt |
| 2 | Vertraut | 150 | Crescendo (CANON §18); Begleiter-Initiative: wittert Ressourcen |
| 3 | Verbunden | 350 | Voller Gehorsam (CANON §18); Bindungs-Evolutionen (BondTier>=3); warnt vor Gefahren |
| 4 | Eng | 550 | Bindungs-Duett (K33); Reit-Ausdauer +10 % (K40); trägt kleine Fundstücke |
| 5 | Seelenklang | 750 | Crescendo-Kosten −10 (K30); persönliche Leerlauf-Animationen |
| 6 | Einklang | 900 | Titel „Im Einklang“ in der Herkunft (DR-16); Klangmal-Glanz; Hain-Chorleitung |

**Regeln:**
- Stufen **sinken nie**. Der Wert kann durch Vernachlässigung bis zur Untergrenze der aktuellen Stufe fallen, nicht darunter.
- Die Stufe wird am Echo als **Klangmal-Ringe** angezeigt (1–6 Ringe); der genaue Wert ab Wärter-Skill „Einfühlung“ (K43).
- Stufenaufstieg: kurze Szene (≤ 3 s, überspringbar), Echo-Ruf, Herkunftseintrag (DR-16).
- Gezüchtete Echos starten mit 120 (Stufe 1, nahe Stufe 2) – sie kennen den Wärter von Geburt an.

**Q8 gelöst:** Grenzen 0 / 150 / 350 / 550 / 750 / 900.

---

## 3. Bindungshandlungen

| DisplayName | Context | Gain | DailyCap | MoodDelta | FavoriteBonus | Notes |
|---|---|---|---|---|---|---|
| Gemeinsamer Sieg | Kampf (aktiv beteiligt) | 2 | 20 | 3 | 0 | Auch Bindung/Flucht zählt; Niederlage 0, kein Abzug (ADR-014) |
| Gemeinsamer Weg | Begleiter im Chor (je 500 m) | 1 | 15 | 1 | 0 | Nur Begleiter-Slot und aktiver Chor |
| Füttern | Lager-Moment / Begleiter-Rad | 4 | 16 | 8 | 8 | Lieblingsfutter (BondLure) doppelt; gleiches Futter am selben Tag halbiert |
| Streicheln | Begleiter-Rad | 3 | 9 | 6 | 3 | 1× je Spielstunde wirksam |
| Spielen | Lager-Moment | 5 | 10 | 10 | 5 | Minispiel 20–40 s |
| Loben | nach Kampf / Feldfähigkeit | 2 | 8 | 5 | 2 | Sofort nach einer Handlung des Echos |
| Training | Lager-Moment | 4 | 8 | 2 | 4 | Schliff-Training (K18) gibt zusätzlich Bindung |
| Rast am Klangbrunnen | Siedlung | 2 | 4 | 15 | 0 | Stellt Stimmung her |
| Evolution | Evolution angenommen | 50 | 50 | 20 | 0 | ADR-091 |
| Einklang bei der Bindung | Bindung | 100 | 100 | 20 | 0 | Startwert (K36) |
| Bindung | Bindung | 50 | 50 | 10 | 0 | Startwert (K36) |
| Schlüpfen | Zucht (K38) | 120 | 120 | 30 | 0 | Gezüchtete Echos starten vertraut |
| Besuch im Hain | Resonanzhain | 2 | 6 | 5 | 2 | Pro besuchtem Garten-Echo |
| Vernachlässigung | Chor ohne Interaktion > 3 Spieltage | -2 | 0 | -10 | 0 | Sinkt nie unter die Stufenuntergrenze (DR-04) |

| Regel | Wert |
|---|---|
| Tagesdeckel | je Handlung und Echo pro Spieltag (CANON §65); verhindert „Streichel-Farmen“ |
| Lieblingshandlung | jede Persönlichkeit hat eine Lieblingsinteraktion (CANON §81) → Zuwachs + Bonus |
| Lieblingsfutter | `BondLure` der Art (K20–K27) doppelt |
| Abwechslung | dasselbe Futter am selben Tag halbiert |
| Niederlage | 0, kein Abzug (ADR-014) |
| Vernachlässigung | −2 je Spieltag, wenn ein Chor-Echo > 3 Spieltage keine Interaktion hatte (nie unter Stufenuntergrenze); Hain-Echos sind ausgenommen |
| Sichtbarkeit | jede Handlung hat eine Reaktion: Animation + Laut + Stimmungssymbol (DR-04, DR-24) |

---

## 4. Fortschritt über die Spielzeit

Simulation (`aethris_bond_progress.py`) für ein Echo im Begleiter-Slot, drei Spielstile, Hälfte der Fütterungen mit Lieblingsfutter, 1,5 Spielstunden je Spieltag:

| Spielstil | Vertraut | Verbunden | Eng | Seelenklang | Einklang |
|---|---|---|---|---|---|
| Kämpfer (wenig Pflege) | 3,2 h | 9,5 h | 15,8 h | 22,1 h | 27,0 h |
| Ausgewogen | 2,2 h | 6,6 h | 11,0 h | 15,5 h | 18,8 h |
| Pfleger (Lager-Momente) | 1,9 h | 6,3 h | 10,7 h | 15,1 h | 18,2 h |

**Bewertung:** Crescendo (Stufe 2) nach 2–3 Spielstunden mit einem Echo – das erste Crescendo des Spielers fällt damit in die Zeit um Akkord 2–3 (K30-Ziel). Bindungs-Evolutionen (Stufe 3) nach 6–10 h. Der reine Kämpfer liegt rund 45 % hinter dem Pfleger – im Zielband „≤ 50 % langsamer“.

---

## 5. Stimmung

Jedes Echo hat eine **Stimmung** (0–100), die kurzfristig schwankt und die *Geschwindigkeit* des Bindungszuwachses beeinflusst – nie die Kampfkraft.

| Stimmung | Bereich | Wirkung | Darstellung |
|---|---|---|---|
| Strahlend | 80–100 | Bindungszuwachs ×1,25; Begleiter-Initiative häufiger | Klangmal leuchtet, verspielte Idle-Animationen |
| Zufrieden | 50–79 | ×1,0 | normale Animationen |
| Gedämpft | 25–49 | ×0,75 | langsamer Gang, seltener Laut |
| Betrübt | 0–24 | ×0,5; keine Initiative | Kopf gesenkt; sucht Nähe zum Wärter |

| Einfluss | Stimmungsänderung |
|---|---|
| Interaktionen | laut `BondActions.csv` (`MoodDelta`) |
| Lieblingswetter (Typ-Resonanz, CANON §62: ×1,2 für den eigenen Typ) | +2 je Spielstunde |
| Ungünstiges Wetter (×0,8 für den eigenen Typ) | −2 je Spielstunde |
| Heimatbiom | +1 je Spielstunde |
| Verklingen im Kampf | −10 (Erholung am Klangbrunnen) |
| Rast (Klangbrunnen, Lager) | +15 |
| Langes Laufen ohne Rast (> 2 Spielstunden) | −5 je Stunde |

Stimmung ist **sichtbar**, aber nie ein Strafsystem: Sie erholt sich bei jeder Rast, und sie sinkt nicht unter 25 durch Wetter allein.

---

## 6. Der Begleiter in der Welt

Ein Echo des aktiven Chors läuft als **Begleiter** sichtbar mit (Begleiter-Slot, frei wählbar; auch Reittiere zu Fuß). Große Echos (XL/XXL) folgen in Abstand oder fliegen/schwimmen parallel.

### 6.1 Begleiter-Initiative

| Verhalten | ab Stufe | Auslöser | Beispiel |
|---|---|---|---|
| Ressourcen wittern | 2 | Ressource ≤ 25 m im Resonanzsinn-Raster | Brokkar stupst an einen Erzfelsen |
| Wetter ankündigen | 2 | Wetterwechsel im nächsten Block | Wisplet tanzt vor einem Sturm |
| Gefahr warnen | 3 | aggressives Wildecho/Alpha ≤ 40 m | Knurren, Blick in die Richtung |
| Spuren zeigen | 3 | seltene Art in der Zone, Kodex ≥ 2 | Schnüffeln entlang einer Fährte |
| Fundstücke tragen | 4 | zufälliger kleiner Fund (1× je Spielstunde, Beutetabelle K42) | bringt eine Muschel |
| Klangfragmente spüren | 4 | Fragment ≤ 60 m (K39) | Echo summt eine fremde Melodie |
| Hain-Chorleitung | 6 | im Resonanzhain | führt Hain-Echos zu Spielen an |

### 6.2 Reaktionen

- **Auf den Spieler:** Begrüßung nach Rückkehr, Freude bei Sieg, Sorge bei niedriger Wärter-Ausdauer, Neugier bei Fotos (K39).
- **Auf die Welt:** Lieblingswetter, Angst vor Stillezonen (zittert, wird grau getönt – Story W1), Interesse an Artgenossen (Linienklang-Rufe).
- **Auf andere Begleiter (Koop):** Spiel-Animationen zwischen Echos verschiedener Spieler; Chor-Akkord-Laute, wenn deren Typen einen Akkord bilden (K33).

### 6.3 Begleiter-Rad (Controller)

`Steuerkreuz ↓` öffnet das Rad: Streicheln · Füttern · Loben · Feldfähigkeit · Reiten (wenn Reittier) · Begleiter wechseln · Foto mit Begleiter. Alle Aktionen < 2 Eingaben (DR-23).

### 6.4 Folge-KI

StateTree `ST_Companion`: Folgen (Abstand nach Größe 2–8 m) → Erkunden (Radius 12 m, wenn Spieler steht > 5 s) → Initiative (§6.1) → Reaktion → Rückkehr. Pfadfindung mit Navmesh je Größenklasse (K53); Teleport-Rückkehr außerhalb der Sicht bei > 40 m Abstand.

---

## 7. Lager-Momente

Am Rastplatz (Lager, Zelt, Gasthaus) öffnet sich der **Lager-Moment** (CANON §6): eine ruhige Szene, in der alle sechs Chor-Echos sichtbar sind.

| Aktion | Ablauf | Dauer |
|---|---|---|
| Füttern | Futter aus der Tasche auf eine Schale; jedes Echo reagiert nach Vorliebe | 5–10 s |
| Kochen | Rezept (K41) → Gericht für alle; Stimmung +10, Effekt für den nächsten Spieltag | 10–20 s |
| Spielen | Minispiel nach Persönlichkeit: Fangen (Verspielt), Suchen (Neugierig), Rhythmus (Klang-Echos), Kräftemessen (Mutig) | 20–40 s |
| Training | Schliff-Training (CANON §80) mit Bindungszuwachs | 10 s |
| Gespräch | kurze Lautäußerungen, Kodex-Beobachtung „Verhalten“ (K39) | – |
| Chor ordnen | Kampfset, Begleiter, Formation (K33) | – |

Lager-Momente sind **optional** und überspringbar; sie sind die Stelle, an der das Spiel „atmet“ (DR-29).

---

## 8. Der Resonanzhain

Der **Resonanzhain** ersetzt das klassische Boxsystem (CANON §6): ein begehbares Refugium aus zehn Biom-Gärten, erreichbar von jedem Resonanzstein ohne Ladebildschirm-Kosten (Schnellreise, kein Sol).

| DisplayName | Biome | UnlockRegion | PreferredTypes | Cap1 | Cap2 | Cap3 | Cap4 | Cap5 | Yield |
|---|---|---|---|---|---|---|---|---|---|
| Lindenhain | Verdanthain-Wald | R01 | Bloom|Storm|Spirit | 20 | 30 | 40 | 50 | 60 | Kräuter|Holz |
| Felsterrasse | Kharsgrat-Hochland | R02 | Stone|Metal|Gravity | 20 | 30 | 40 | 50 | 60 | Erz |
| Nebelmoor | Morvenmoor | R03 | Venom|Spirit|Tide | 20 | 30 | 40 | 50 | 60 | Kräuter|Moorharz |
| Dünenoase | Sahrun-Weite | R04 | Light|Ember|Stone | 20 | 30 | 40 | 50 | 60 | Glas|Datteln |
| Glutgrotte | Ignareth | R05 | Ember|Metal|Crystal | 20 | 30 | 40 | 50 | 60 | Erz|Kohle |
| Gezeitenbucht | Saltrand | R06 | Tide|Storm|Sound | 20 | 30 | 40 | 50 | 60 | Muscheln|Tang |
| Firnkessel | Hvitfell | R07 | Frost|Light|Spirit | 20 | 30 | 40 | 50 | 60 | Eiskristall |
| Säulengarten | Ael'Dorun | R08 | Arcane|Spirit|Sound | 20 | 30 | 40 | 50 | 60 | Glyphenstaub |
| Kristallkammer | Prismtiefen | R09 | Crystal|Void|Gravity | 20 | 30 | 40 | 50 | 60 | Kristalle |
| Wolkenterrasse | Nimbara | R10 | Storm|Light|Sound | 20 | 30 | 40 | 50 | 60 | Wolkenfrucht |

| Regel | Wert |
|---|---|
| Kapazität | 10 Gärten × 20–60 = **600** (alle Gärten Stufe 5) – CANON §18 bestätigt |
| Freischaltung | Garten einer Region mit dem ersten Resonanzstein der Region |
| Ausbau | Stufe 2–5 mit Hain-Material (Holz, Erz, Kristall + Garten-Ertrag) und Sol (K42); jeder Ausbau sichtbar (Pfade, Bäume, Wasserläufe) |
| Bevorzugte Klangfarben | Stimmung +10 im passenden Garten; Echos ziehen automatisch in ihren bevorzugten Garten, wenn Platz ist |
| Ertrag | je Garten und Spieltag Ressourcen nach Anzahl Echos (max. 1 Bündel je 10 Echos) – nie notwendig, immer nett (DR-31) |
| Besuch | Spieler läuft durch die Gärten; Interaktionen wie im Lager (Bindung +2 je Echo, Deckel 6) |
| Chor tauschen | im Hain direkt; **außerhalb** an jedem Klangbrunnen und Resonanzstein über das Hain-Menü (kein Pflichtbesuch, DR-23) |
| Zucht | findet in Brutnischen der Gärten statt (K38) |
| Koop | Mitspieler können den Hain besuchen (nur Ansicht/Interaktion, keine Entnahme) |
| Überlauf | > 600 Echos: „Freilassen“ (Echo kehrt an seinen Fundort zurück; Herkunft bleibt im Kodex) oder Tausch (K60) |

```
                 ┌───────── RESONANZHAIN ─────────┐
                 │   Wolkenterrasse (R10)         │
     Säulengarten│        ▲                       │Firnkessel
        (R08) ◄──┤   Zentraler Klangbrunnen ──────┼──► (R07)
                 │   (Hain-Menü, Brutnischen)     │
   Lindenhain ◄──┤        ▼                       ├──► Kristallkammer
      (R01)      │  Gezeitenbucht · Dünenoase ·   │      (R09)
                 │  Glutgrotte · Felsterrasse ·   │
                 │  Nebelmoor                     │
                 └────────────────────────────────┘
```

---

## 9. Gehorsam und Tausch

Die Gehorsamsregel aus CANON §18 gilt unverändert: Volles Gehorsam bei selbst gebunden/gezüchtet **oder** Level ≤ 20 + 8 × Akkorde **oder** Bindungsstufe ≥ 3; sonst +40 % Zeitkosten (K31). Damit ist Bindungsstufe 3 der natürliche Weg, getauschte Hochlevel-Echos voll einzusetzen. Getauschte Echos starten mit dem Bindungswert 0 beim neuen Wärter (Herkunft vermerkt beide Wärter, DR-16); ihre Stufe beginnt bei 1.

---

## 10. Code

```cpp
// GF_Companion – Bindung und Stimmung je Echo (Teil von FEchoInstance, K06 Save)
USTRUCT() struct FEchoBondState
{
    GENERATED_BODY()
    UPROPERTY(SaveGame) int16 BondValue = 0;        // 0–1000
    UPROPERTY(SaveGame) uint8 BondTierReached = 1;   // nie sinkend
    UPROPERTY(SaveGame) uint8 Mood = 60;             // 0–100
    UPROPERTY(SaveGame) int32 LastInteractionDay = 0;
    UPROPERTY(SaveGame) int32 LastResetDay = 0;
    UPROPERTY(SaveGame) TMap<FName, uint8> DailyGained; // Tagesdeckel je Handlung
};

void UBondService::Apply(FEchoInstance& Echo, FName ActionId, bool bFavorite, int32 GameDay)
{
    const FBondActionRow& A = *Actions->FindRow<FBondActionRow>(ActionId, TEXT("Bond"));
    FEchoBondState& B = Echo.Bond;
    if (B.LastResetDay != GameDay) { B.DailyGained.Reset(); B.LastResetDay = GameDay; }
    int32 Gain = A.Gain + (bFavorite ? A.FavoriteBonus : 0);
    Gain = Gain * MoodFactorPermille(B.Mood) / 1000;
    const int32 Room = A.DailyCap > 0 ? FMath::Max(0, A.DailyCap - B.DailyGained.FindOrAdd(ActionId)) : Gain;
    Gain = FMath::Min(Gain, Room);
    B.DailyGained[ActionId] += Gain;
    const int32 Floor = TierFloor(B.BondTierReached);           // Stufen sinken nie
    B.BondValue = FMath::Clamp(B.BondValue + Gain, Floor, 1000);
    B.Mood = FMath::Clamp(B.Mood + A.MoodDelta, 0, 100);
    const uint8 NewTier = TierFor(B.BondValue);
    if (NewTier > B.BondTierReached) { B.BondTierReached = NewTier; Bus->Broadcast(TAG_Echo_BondTierUp, FBondTierMessage{ Echo.Guid, NewTier }); }
}
```

Der Resonanzhain ist ein **eigenes Level** (World Partition, Streaming aus dem Menü in < 3 s auf SSD-Plattformen, K65) mit Instanzen der Echos als Mass-Agenten (K52) – 600 Echos bei 60 FPS über LOD-Stufen (nur nahe Echos voll animiert).

---

## 11. Tests und Telemetrie

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Bond.Tiers` | Grenzen, nie sinkende Stufe, Untergrenzen bei Vernachlässigung |
| `…Bond.DailyCap` | Tagesdeckel, Lieblingsbonus, halbiertes Wiederholungsfutter |
| `…Bond.Mood` | Stimmungsfaktoren, Wetter-/Biom-Einfluss |
| `Aethris.Func.Hain.Capacity` | 600 Echos geladen, 60 FPS-Budget auf Referenzhardware |
| `Aethris.Func.Companion.Initiative` | Initiative-Verhalten löst nach Stufe aus |

**Telemetrie:** Zeit bis Stufe 2/3 je Echo, Anteil Spieler mit Lager-Momenten ≥ 1× je Spielstunde, Begleiter-Wechselhäufigkeit, Hain-Besuche. Ziel: Stufe 3 mit dem meistgenutzten Echo bei ≥ 70 % der Spieler bis Akt-I-Ende.

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-135 | Bindungsstufen 0/150/350/550/750/900, nie sinkend | Q8; Belohnung ohne Verlustangst | Absinkende Stufen (Pflegezwang) |
| ADR-136 | Tagesdeckel je Handlung | Kein Farmen, Abwechslung wird belohnt | Unbegrenzte Gewinne |
| ADR-137 | Stimmung beeinflusst nur Bindungstempo, nie Kampfwerte | Fairness, kein Pflichtsystem | Stimmungsabhängige Kampfwerte |
| ADR-138 | Resonanzhain mit 10 begehbaren Gärten (600), Chor-Tausch auch per Menü | Weltgefühl ohne Laufzwang (DR-23) | Abstrakte Boxen; Hain nur begehbar |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §137 | Bindungsstufen (`BondTiers.csv`): Vorsichtig 0, Vertraut 150, Verbunden 350, Eng 550, Seelenklang 750, Einklang 900; Freischaltungen je Stufe; nie sinkend; Gezüchtete starten mit 120 | LOCKED – **Q8 gelöst** |
| §138 | 14 Bindungshandlungen (`BondActions.csv`) mit Tagesdeckeln, Lieblingshandlung/-futter, Vernachlässigung −2/Spieltag bis Stufenuntergrenze; Stimmung 0–100 in 4 Bändern (×1,25/1,0/0,75/0,5 Bindungstempo) | LOCKED |
| §139 | Begleiter-Slot, Initiative-Verhalten nach Stufe (§6.1), Begleiter-Rad, Folge-KI `ST_Companion`; Lager-Momente optional | LOCKED |
| §140 | Resonanzhain: 10 Gärten (`SanctuaryGardens.csv`), Kapazität 20/30/40/50/60 je Garten (gesamt 600), Freischaltung mit erstem Resonanzstein der Region, Ertrag, Chor-Tausch an Klangbrunnen/Resonanzsteinen, Koop-Besuch, Freilassen | LOCKED (Ausbaukosten → K42) |
| §10 | ADR-135 – ADR-138 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Partner-Fantasie und Ziele
- [x] Bindungsstufen 1–6 mit Grenzen (Q8) und Freischaltungen
- [x] 14 Bindungshandlungen mit Deckeln, Vorlieben, Vernachlässigung
- [x] Fortschritts-Simulation für drei Spielstile
- [x] Stimmungssystem ohne Kampfwirkung
- [x] Begleiter in der Welt: Initiative, Reaktionen, Rad, Folge-KI
- [x] Lager-Momente
- [x] Resonanzhain: 10 Gärten, 600 Plätze, Ausbau, Ertrag, Koop
- [x] Gehorsam/Tausch, Code, Tests, Telemetrie
- [x] ADR-135 – ADR-138, CANON §137–§140

➡️ **Nächstes Kapitel: K38 – Zucht und Genetik (Allele, Morphs, Vererbung) – löst Q3.**
