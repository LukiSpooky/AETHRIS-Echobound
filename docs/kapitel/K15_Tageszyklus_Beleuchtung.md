# K15 · Tageszyklus & Beleuchtung

| Feld | Wert |
|---|---|
| Dokument | Kapitel 15 von 68 · letztes Kapitel von Teil II (Welt) |
| Version | 1.0 |
| Owner | Technical Artist (Lighting Lead) |
| Mitwirkende | Gameplay Programmer (Spieluhr), Unreal Senior Dev (Rendering, Switch 2), AI Engineer (Aktivität), Audio Director, Level Designer |
| Baut auf | CANON §4.3 (72 min/Tag), §64 (Tagesphasen), §50 (Dunkelheit), K10 (regionale Tageslängen), K14 (Wetter) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/World/TimeOfDayCurves.csv`, `MoonPhases.csv`, `ActivityCurves.csv` |
| Neue Kanon-Einträge | CANON §65 (Spieluhr & Kalender), §66 (Mondphasen), §67 (Aktivitätsmuster), §68 (Beleuchtungssystem & Plattformprofile) |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Die Spieluhr](#2-die-spieluhr)
3. [Kalender: Spieltag, Woche, Mondphasen](#3-kalender-spieltag-woche-mondphasen)
4. [Einfluss auf Spielsysteme](#4-einfluss-auf-spielsysteme)
5. [Aktivitätsmuster der Echos](#5-aktivitätsmuster-der-echos)
6. [Beleuchtungsdesign](#6-beleuchtungsdesign)
7. [Regionale Lichtidentität](#7-regionale-lichtidentität)
8. [Innenräume, Höhlen, Himmel](#8-innenräume-höhlen-himmel)
9. [Technische Umsetzung (Lumen) & Switch-2-Profil](#9-technische-umsetzung-lumen--switch-2-profil)
10. [Code](#10-code)
11. [Performance & Tests](#11-performance--tests)
12. [Decision Records](#12-decision-records)
13. [Kanon-Updates](#13-kanon-updates)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Ziele

Das Briefing fordert einen 24-Stunden-Zyklus mit Einfluss auf **Kreaturen, Quests, Händler, Musik, Licht**. AETHRIS nutzt den Tageszyklus darüber hinaus für Evolution (K19), Fotografie (K39), NPC-Tagesabläufe (K53) und Belastung (K09).

| Ziel | Messgröße |
|---|---|
| Spürbarer Rhythmus | In einer 90-Minuten-Session erlebt der Spieler mindestens einen kompletten Tag-Nacht-Wechsel |
| Nacht ist spielbar, nicht dunkel-frustrierend | Mittlere Bildhelligkeit nachts ≥ 18 % der Tageshelligkeit (Wahrnehmung), Wege und Interaktionen bleiben lesbar |
| Jede Phase hat Gameplay-Wert | Jede Phase (Dämmerung, Tag, Abend, Nacht) bietet exklusive Spawns, Ereignisse oder Händler |
| Plattformparität | Switch 2 zeigt denselben Zyklus mit anderem Lichtpfad, ohne Gameplay-Unterschiede |

---

## 2. Die Spieluhr

| Eigenschaft | Festlegung (LOCKED) |
|---|---|
| Maßstab | 1 Spieltag = 72 Echtzeitminuten; 1 Spielstunde = 3 min; 1 Spielminute = 3 s |
| Startzeit Neues Spiel | Spieltag 1, 06:30 (Morgendämmerung, Prolog-Erwachen) |
| Auflösung | Uhr in Spielminuten (`int64 GameMinute`), Ganzzahl – deterministisch (Wetterfahrplan, K14) |
| Pausieren | Solo: Menü, Dialog, Fotomodus (optional), Zwischensequenz (Uhr läuft weiter, wenn die Sequenz eine Zeit vorgibt) – CANON §17 |
| Koop | Host-autoritativ, Replikation 1 Hz + Interpolation; Gäste sehen Host-Zeit |
| Zeit vorspulen | Gasthaus/Zelt/Lager → Dämmerung (05:00), Mittag (12:00), Abend (19:00), Mitternacht (00:00) |
| Story-Zeitpunkte | Quests dürfen Zeit setzen (`SetGameTime`, nur vorwärts – nie zurück, um Fahrpläne nicht zu brechen) |
| Uhr-UI | Kompass-HUD zeigt Sonnen-/Mondsymbol + Phase; genaue Uhrzeit optional (Option „Uhr anzeigen“) und an Uhren in Städten |

```
  00   03   06   09   12   15   18   21   24 (Spielstunden, Standardregion)
  ├────┼────┼────┼────┼────┼────┼────┼────┤
  ██████████▓▓▓▓░░░░░░░░░░░░░░░░░░░░░▓▓▓▓█████
  NACHT     DÄMM.         TAG               ABEND NACHT
  21–05     05–07         07–19             19–21
  Echtzeit: Tag 36 min · Nacht 24 min · Dämmerungen je 6 min
```

---

## 3. Kalender: Spieltag, Woche, Mondphasen

### 3.1 Spieltag & Woche

| Einheit | Länge | Verwendung |
|---|---|---|
| Spieltag | 72 min | Abklingzeiten (Aufträge, Sturmstimmgabel), Wanderdorf, Ausbrüche |
| **Woche** | 7 Spieltage (≈ 8,4 h Echtzeit) | Händler-Rotationen, Ratssitzungen, Feste („jeder 7. Spieltag“) |
| Monat / Jahr | – | Nicht simuliert (ADR-040: keine Jahreszeiten); Jahr bleibt 1004 n.St. |

**Wochentage (Lore, linnische Namen):** Wurzeltag, Blatttag, Wassertag, Steintag, Windtag, Lichttag, Stilltag. *Stilltag* ist traditionell Ruhetag: Händler mit Kategorie „General“ öffnen 2 h später (K42).

### 3.2 Mondphasen (löst CANON-Q15)

Daten: `Data/World/MoonPhases.csv`. Aethris hat **einen Mond** (*Lunar*: „Der Schweigende“ im Volksmund).

| Phase | Tag | Beleuchtung | Zusatzlicht nachts | Nachtaktive Spawns |
|---|---|---|---|---|
| Neumond | `Moon.NewMoon` | 0 % | +0 lx | ×0,8 |
| Zunehmende Sichel | `Moon.WaxingCrescent` | 25 % | +0,06 lx | ×0,9 |
| Erstes Viertel | `Moon.FirstQuarter` | 50 % | +0,13 lx | ×1,0 |
| Zunehmender Mond | `Moon.WaxingGibbous` | 75 % | +0,19 lx | ×1,1 |
| **Vollmond** | `Moon.FullMoon` | 100 % | +0,25 lx | ×1,2 |
| Abnehmender Mond | `Moon.WaningGibbous` | 75 % | +0,19 lx | ×1,1 |
| Letztes Viertel | `Moon.LastQuarter` | 50 % | +0,13 lx | ×1,0 |
| Abnehmende Sichel | `Moon.WaningCrescent` | 25 % | +0,06 lx | ×0,9 |

**Zyklus:** 8 Phasen × 2 Spieltage = **16 Spieltage** (≈ 19,2 h Echtzeit). Phasenindex = `((Spieltag − 1) / 2 + 1) mod 8` (0 = Neumond); Spieltag 1 beginnt mit Zunehmender Sichel (M2), damit der erste Vollmond am Spieltag 7–8 liegt (≈ 8 h Spielzeit – erreichbar in der frühen Akt-I-Phase).

**Gameplay-Nutzung:** Neumond-Arten in Sahrun (K09), Sternenlesen in Aerion (K12), Vollmond-Evolutionen (K19), Fotografie (Mond im Bild, K39), Mondspiegel-Arena Qasr Sahrun (Wirkung skaliert mit Mondbeleuchtung). Vorhersage: Mondkalender bei Sterndeuter Harun (Qasr Sahrun) und im Kodex ab Forschungs-Skill.

---

## 4. Einfluss auf Spielsysteme

| System | Wirkung des Tageszyklus | Kapitel |
|---|---|---|
| **Echo-Spawns** | Aktivitätskurven je Art (§5) × Mondfaktor (nachtaktiv) × Wetter (K14) | K52 |
| **Echo-Verhalten** | Schlafen/Fressen/Revier je Phase; schlafende Echos: Bindungsbonus beim Einstimmen (DR-03) | K36, K52 |
| **Evolution** | Auslöser `TimeOfDay.*` und `Moon.*` | K19 |
| **Quests** | Zeitfenster (z. B. Arena Morvenfurt nur nachts), Questziele mit `RequiredTimeOfDay` | K48 |
| **Händler** | Öffnungszeiten (`Merchants.csv`), Nachtmärkte, Stilltag | K42 |
| **NPCs** | Tagesabläufe (Muster K11 §3.2) | K53 |
| **Musik** | Tag-/Nacht-Varianten aller Themen, Dämmerungs-Übergänge | K55 |
| **Licht** | Sonne, Mond, Sterne, künstliche Lichter, Belichtung | §6 |
| **Belastung** | Kälte nachts (Sahrun, Hvitfell, Nimbara) | K09 |
| **Fotografie** | Lichtwertung („goldene Stunde“ = Dämmerungen +1 Stern-Bonus) | K39 |
| **Kampf** | Keine direkten Kampfwerte (Fairness); Ausnahme: Feldregeln (Mondspiegel) und Fähigkeiten mit Tageszeit-Bedingung (K28–K30) | K32 |

**Designregel DR-32 (neu):** Jede Region bietet in **jeder** Tagesphase mindestens eine exklusive Aktivität (Spawn, Ereignis, Händler oder Rätsel). Validator zählt `RequiredTimeOfDay`-Tags pro Region.

---

## 5. Aktivitätsmuster der Echos

Daten: `Data/World/ActivityCurves.csv` – Aktivität in Promille je Spielstunde. Jede Art erhält genau **ein** Aktivitätsmuster als `ObservableTrait` (zählt für DR-02).

| Muster | Tag | Charakter | Typische Typen | Aktivität (Promille) Nacht / Dämmerung / Tag |
|---|---|---|---|---|
| Tagaktiv | `Behavior.Activity.Diurnal` | aktiv bei Licht | Blüte, Licht, Sturm | 100 / 500 / 950 |
| Nachtaktiv | `Behavior.Activity.Nocturnal` | aktiv bei Dunkelheit | Geist, Leere, Gift | 950 / 500 / 100 |
| Dämmerungsaktiv | `Behavior.Activity.Crepuscular` | Spitzen in Dämmerungen | Klang, Arkan, Flut | 150 / 1000 / 150–400 |
| Unstet | `Behavior.Activity.Cathemeral` | gleichmäßig | Stein, Metall, Schwerkraft | 650 / 650 / 650 |
| Mittagsaktiv | `Behavior.Activity.Midday` | Spitze bei Hitze | Glut, Kristall | 80 / 80–450 / 450–1000 |

**Bedeutung der Aktivität (Vorgabe K52):**
- **Spawn-Gewicht** wird mit Aktivität skaliert (Minimum 80 ‰ → Art nie völlig unauffindbar, aber selten; schlafende Exemplare sind dann *sichtbar schlafend*).
- **Verhalten:** Aktivität < 300 ‰ → Ruhe-/Schlafzustand an Schlafplätzen (POI „Habitat“, K08 §9). Schlafende Echos: −50 % Wahrnehmungsradius (Annäherung leichter), Einstimmen +1 Stufe Ruhe (K36), aber manche Arten reagieren gereizt beim Wecken (Temperament).
- **Kodex:** „Aktivitätsmuster“ ist eine Forschungsinformation (Stufe 2, K39).

---

## 6. Beleuchtungsdesign

### 6.1 Lichtkurven (Standardregion)

Daten: `Data/World/TimeOfDayCurves.csv` – pro Stunde Sonnenhöhe, Beleuchtungsstärke, Farbtemperatur, Nebeldichte, Belichtungskorrektur. Zwischenwerte werden linear interpoliert (Spielminuten-genau).

| Zeit | Sonnenhöhe | Beleuchtung | Farbtemp. | Stimmung |
|---|---|---|---|---|
| 05:00 | −9° | 39 lx (blaue Stunde) | 4.100 K (Himmel) | kühl, gedämpft |
| 06:00 | 0° | 400 lx | 2.800 K | goldene Stunde |
| 08:00 | 24° | ~39.000 lx | 5.200 K | frisch, klare Schatten |
| 13:00 | 55° (Max.) | ~93.000 lx | 6.500 K | hell, kurze Schatten |
| 18:00 | 24° | ~39.000 lx | 5.200 K | warm beginnend |
| 20:00 | 0° | 400 lx | 2.800 K | goldene Stunde |
| 21:00 | −9° | 39 lx | 4.100 K | blaue Stunde |
| 01:00 | −30° | Mond + Sterne (0–0,25 lx) | 4.100 K | Nacht, mondabhängig |

> **Hinweis zu Dämmerungszeiten:** Phasengrenzen (CANON §64) sind Gameplay-Grenzen; der **astronomische** Sonnenauf-/untergang liegt in der Mitte der Dämmerungsphasen (06:00 / 20:00). So beginnen Dämmerungs-Spawns, bevor die Sonne sichtbar ist.

### 6.2 Nachtlesbarkeit (LOCKED-Regeln)

| Regel | Umsetzung |
|---|---|
| L-N1 Kein „schwarzes“ Bild | Belichtungsuntergrenze nachts (Auto Exposure Min) so, dass Mittelgrau ≥ 18 % Tageswahrnehmung; Mondlicht als schwache Directional Light + „Night Fill“ (sehr schwaches, blau getöntes Himmelslicht) |
| L-N2 Wege lesbar | Pfade haben leicht hellere Albedo; Laternen in Siedlungen und an Bundesstraßen alle 60–80 m |
| L-N3 Interaktionen leuchten dezent | Sammelbares, Resonanzsteine, Klangbrunnen mit schwacher Emissive-Kante (nur nachts aktiv) |
| L-N4 Biolumineszenz als Biomsprache | Pilze (R01), Irrlichtmoos (R03), Riff (R06), Kristalle (R09) liefern regionale Nachtfarben |
| L-N5 Dunkelheit nur, wo gewollt | Mechanische Dunkelheit (K10 §1) nur in Höhlen/Gewölben, nie in der offenen Welt |

### 6.3 Künstliche Lichter

| Lichtquelle | Ein/Aus | Technik |
|---|---|---|
| Straßenlaternen | 19:30–05:30 (gestaffelt, Laternenanzünder-NPC in Eichenhall, kosmetisch) | Point Lights mit Distanz-Culling, Lumen-beitragend nur < 40 m |
| Fenster | 18:00–23:00 zufällig gestaffelt je Haus (deterministisch via Haus-ID) | Emissive-Materialparameter, keine echten Lichter |
| Lagerfeuer/Herde | NPC-gesteuert | Point Light + Flicker-Light-Function |
| Spielerlaterne | manuell; automatisch bei Lichtwert < 15 (Option) | Spot/Point, Schatten nur PS5/PC |

---

## 7. Regionale Lichtidentität

Jede Region erhält ein **Licht-Profil** (`DA_LightProfile_R##`), das die Standardkurve moduliert (Farbe, Nebel, Kontrast, Tageslänge).

| Region | Offset Tageslänge | Farbtendenz | Nebel | Besonderheit |
|---|---|---|---|---|
| R01 Verdanthain | – | warm-grün gefiltert | leicht, Bodennebel morgens | God Rays durch Kronen |
| R02 Kharsgrat | – | kühl, hoher Kontrast | Wolkenmeer unter Terrassen | lange Schatten an Graten |
| R03 Morvenmoor | – | grün-grau, diffus | dicht (Basis ×2) | Irrlichter nachts |
| R04 Sahrun | – | sehr hell, warm; Nacht klar-blau | sehr gering | Hitzeflimmern, extreme Abendfarben |
| R05 Ignareth | – | rot-orange (Lava-Emissive), Rauchfilter | Rauch | Lava ist Hauptlicht nachts |
| R06 Saltrand | – | hell, salzige Luftperspektive | gering, Seenebel | Glitzern auf Wasser |
| R07 Hvitfell | **Nacht +2 h** | blau, tiefstehende Sonne (Max. 30° statt 55°) | Eisnebel | Aurora, SSS im Eis |
| R08 Ael'Dorun | – | gelblich, Nachmittagsstimmung | mittel | Glyphenleuchten nachts |
| R09 Prismtiefen | unter Tage: Lichtkristall-Zyklus | violett/cyan | Höhlendunst | Kristall-Emissive |
| R10 Nimbara | **Tag +2 h** | klar, hohe Sonne, rosa Dämmerung | Wolkenmeer **unter** dem Spieler | Sternenpracht, keine Lichtverschmutzung |

**Umsetzung der Tageslängen-Offsets (ADR-053):** Die Spieluhr bleibt global; die **Sonnenkurve** wird je Region über eine Zeitabbildung verzerrt (Hvitfell: Sonnenbogen 07–19 statt 06–20; Nimbara: 05–21). Grenzbereiche blenden über 300 m.

---

## 8. Innenräume, Höhlen, Himmel

| Raumtyp | Lichtverhalten |
|---|---|
| Häuser (Innenräume) | Fensterlicht folgt Außenzeit (Lumen); Innenbeleuchtung NPC-abhängig; Belichtungsadaption 1,5 s |
| Höhlen/Dungeons | Kein Tageszyklus; Dunkelheitsmechanik (K10); Eingangsbereiche zeigen Außenlicht |
| Prismara | **Lichtkristall-Zyklus**: Deckenkranz folgt der Oberflächenzeit (Stadt), Höhlen-Echos folgen dem Kristallpuls (alle 6 Spielstunden, K10) |
| Nimbara | Himmel ohne Horizontdunst; Wolkenmeer reflektiert Sonne (Lumen Sky Light Capture) |
| Kloster Schweigfels | Nur Tageslicht + wenige Kerzen (kein Glühen von Klangtechnik – thematisch) |

---

## 9. Technische Umsetzung (Lumen) & Switch-2-Profil

### 9.1 Current-Gen (PS5, XSX, PC)

| Komponente | Einstellung |
|---|---|
| Sonne/Mond | Zwei Directional Lights (Sonne: Atmosphere Sun Light 0; Mond: Atmosphere Sun Light 1, nachts aktiv) |
| Himmel | Sky Atmosphere + Volumetric Clouds + SkyLight (Real-Time Capture, zeitgeslicet) |
| GI/Reflexionen | **Lumen** (Software Ray Tracing auf Konsole; Hardware RT optional PC/PS5 Pro) |
| Schatten | Virtual Shadow Maps |
| Belichtung | Auto Exposure (Histogram) mit Kurven aus `TimeOfDayCurves.csv` (Bias) und Min/Max je Phase |
| Update-Frequenz | Sonnenwinkel jede Spielminute (3 s) interpoliert; Lumen konvergiert kontinuierlich (keine Sprünge) |

### 9.2 Switch-2-Profil (ADR-070)

Lumen ist auf Switch 2 nicht im Budget (K65). Ein dynamischer Tageszyklus verbietet klassisch gebackenes GI. Lösung: **„TOD-Irradiance-Blending“**.

```
 Vorab (Build/Bake):
   Für jede Region × 4 Schlüsselzeiten (06:00, 13:00, 20:00, 01:00) → Irradiance-Volumen (Probe-Gitter 4 m außen / 1 m in Städten)
 Laufzeit:
   GI(t) = Blend(Volumen[ZeitA], Volumen[ZeitB], α(t))     ← 2 Volumen gleichzeitig im Speicher
   + Sky Light Real-Time Capture (alle 10 s, zeitgeslicet über 6 Frames)
   + Distance Field AO (reduziert) + SSGI (halbe Auflösung)
   + Schatten: Cascaded Shadow Maps (3 Kaskaden) statt VSM
 Speicher: ~45 MB pro Region (4 Volumen, komprimiert), gestreamt mit der Region
```

| Vorteile | Nachteile |
|---|---|
| Dynamischer Tag/Nacht auf Switch 2 ohne Lumen; Gameplay identisch | Zusätzlicher Bake-Schritt (≈ 3 h pro Region auf der Farm), statische Objekte bevorzugt; bewegte große Objekte (Lavaströme A/B, Stillezonen-Layer) brauchen je Zustand eigene Volumen (+30 % Speicher in R05/R08) |
| Visuell nah an Current-Gen in offenen Bereichen | Innenräume weniger präzise → Innenräume mit zusätzlichen gebackenen Lightmaps (statisches Innenlicht) |

**Risiko:** Teil von R-01 (Switch-2-Performance). Gate: Vertical Slice (K67).

### 9.3 Wetter-Interaktion

Wetterprofile (K14 §12) modulieren Lichtkurven multiplikativ (z. B. Regen: Sonnenintensität ×0,35, Sättigung −20 %, Nebel ×2,5). Reihenfolge: Basiskurve → Regionsprofil → Wetter → Story-Overrides (Stillezone: Entsättigung über `MPC_Silence`).

---

## 10. Code

### 10.1 Spieluhr (AethrisGame, replizierter Zustand im GameState)

```cpp
// AethrisGame/Public/Time/AethrisGameClock.h
/**
 * Globale Spieluhr (K15 §2). Ganzzahlige Spielminuten → deterministisch.
 * Host-autoritativ; Clients interpolieren zwischen Replikationen (1 Hz).
 */
UCLASS()
class AETHRISGAME_API UAethrisGameClock : public UWorldSubsystem
{
	GENERATED_BODY()
public:
	static constexpr int32 RealSecondsPerGameMinute = 3;          // 72 min/Tag (CANON §4.3)
	static constexpr int32 MinutesPerDay = 24 * 60;

	int64 GetGameMinute() const { return GameMinute; }
	int32 GetGameDay() const { return static_cast<int32>(GameMinute / MinutesPerDay) + 1; }
	int32 GetHour() const { return static_cast<int32>((GameMinute % MinutesPerDay) / 60); }
	float GetFractionalHour() const;                                // für Lichtinterpolation

	/** Tagesphase unter Berücksichtigung regionaler Offsets (CANON §64). */
	FGameplayTag GetPhase(FName RegionId) const;

	/** Mondphase 0..7 (MoonPhases.csv). Spieltag 1 = Zunehmende Sichel (Index 1). */
	int32 GetMoonPhaseIndex() const { return ((GetGameDay() - 1) / 2 + 1) % 8; }

	/** Nur vorwärts (Wetterfahrplan bleibt gültig). Sendet Event.World.TimeOfDayChanged bei Phasenwechsel. */
	void AdvanceTo(int64 TargetGameMinute);

	/** Zeit vorspulen auf die nächste Zielstunde (5, 12, 19, 0). */
	void SkipToNext(int32 TargetHour);

	void SetPaused(bool bInPaused) { bPaused = bInPaused; }   // vom Game-Flow (K03 §2.3)

private:
	void OnRealSecondTick();     // Timer 1 Hz → alle 3 s eine Spielminute
	int64 GameMinute = 6 * 60 + 30;   // Start: Tag 1, 06:30
	int32 SubMinuteSeconds = 0;
	bool bPaused = false;
	FGameplayTag LastBroadcastPhase;
};
```

```cpp
// Private/Time/AethrisGameClock.cpp (Auszug)
FGameplayTag UAethrisGameClock::GetPhase(FName RegionId) const
{
	// Regionale Grenzen aus CANON §64 (Data Asset DA_DayPhases, hier verkürzt)
	const FDayPhaseBounds& B = DayPhaseBoundsFor(RegionId);   // Dawn, Day, Dusk, Night Startstunden
	const int32 H = GetHour();
	if (H >= B.DawnStart && H < B.DayStart)   return AethrisTags::TimeOfDay_Dawn;
	if (H >= B.DayStart  && H < B.DuskStart)  return AethrisTags::TimeOfDay_Day;
	if (H >= B.DuskStart && H < B.NightStart) return AethrisTags::TimeOfDay_Dusk;
	return AethrisTags::TimeOfDay_Night;
}

void UAethrisGameClock::SkipToNext(int32 TargetHour)
{
	const int64 DayStart = (GameMinute / MinutesPerDay) * MinutesPerDay;
	int64 Target = DayStart + TargetHour * 60;
	if (Target <= GameMinute) { Target += MinutesPerDay; }
	AdvanceTo(Target);           // Wetter: Fahrplan liefert automatisch das Wetter zur Zielzeit (K14 §4.1)
}
```

### 10.2 Aktivitätsabfrage (GF_AI)

```cpp
/** Aktivität einer Art zur aktuellen Stunde, inkl. Mondfaktor für nachtaktive Arten (K15 §5, §3.2). */
int32 UEcologySubsystem::GetActivityPermille(const UEchoSpeciesDefinition& Species) const
{
	const FGameplayTag Pattern = Species.GetActivityPattern();                  // Behavior.Activity.*
	const int32 Base = ActivityCurves->Get(Pattern, Clock()->GetHour());       // ActivityCurves.csv
	if (Pattern == AethrisTags::Behavior_Activity_Nocturnal && Clock()->IsNight())
	{
		return Base * MoonPhases->NocturnalSpawnPermille(Clock()->GetMoonPhaseIndex()) / 1000;
	}
	return Base;
}
```

---

## 11. Performance & Tests

| Thema | Budget / Test |
|---|---|
| Spieluhr + Phasenlogik | < 0,01 ms Game Thread |
| Sky Light Capture | PS5: Real-Time Capture zeitgeslicet ≤ 0,3 ms; Switch 2: alle 10 s über 6 Frames ≤ 0,2 ms |
| Lumen-Konvergenz | Keine sichtbaren Sprünge: Sonnenwinkeländerung pro Spielminute ≤ 0,25° |
| `Aethris.Unit.Game.Clock.Phases` | Phasen je Region inkl. Hvitfell/Nimbara-Offsets |
| `Aethris.Unit.Game.Clock.Moon` | Spieltag 1 → M2, Spieltag 7–8 → Vollmond, Zyklus 16 Tage |
| `Aethris.Unit.Game.Clock.Skip` | SkipToNext nie rückwärts, korrekte Tagesübergänge |
| `Aethris.Functional.World.NightReadability` | Automatisierte Screenshots 01:00 Neumond in jeder Region → Mittelgrau-Messung ≥ Schwelle (L-N1) |

---

## 12. Decision Records

### ADR-070 – Switch 2: TOD-Irradiance-Blending statt Lumen
- Siehe §9.2. Alternative „statische Tageszeit auf Switch 2“ verworfen (Gameplay-Parität, DR-15 Tageszeit-Bedingungen).

### ADR-071 – Eine globale Spieluhr, regionale Sonnenkurven
- **Entscheidung:** Spielzeit ist global (Fahrpläne, Koop, Abklingzeiten); Tageslängen-Unterschiede entstehen nur durch regionale Sonnenkurven und Phasengrenzen. Vorteil: eine Wahrheit für die Zeit. Nachteil: An Regionsgrenzen „springt“ die Phase → 300 m Überblendung des Lichts, Gameplay-Phase nach Spielerregion.

### ADR-072 – Mondzyklus 16 Spieltage
- **Entscheidung:** 8 Phasen à 2 Spieltage. Vorteil: Vollmond etwa jede 19 h Echtzeit – selten genug für Besonderheit, häufig genug, um nicht zu warten (DR-23). Nachteil: astronomisch unrealistisch – irrelevant.

### ADR-073 – Wochentage mit Stilltag
- **Entscheidung:** 7-Tage-Woche mit Ruhetag (Händler später). Vorteil: Welt-Rhythmus, Lore-Anker (Stille als Kultur). Nachteil: Spieler könnten Stilltag als Hindernis empfinden → nur „General“-Händler betroffen, nur 2 h.

---

## 13. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §65 | Spieluhr: `int64 GameMinute`, 3 s/Spielminute, Start Tag 1 06:30, nur vorwärts, Host-autoritativ (1 Hz), `UAethrisGameClock`; Zeit vorspulen auf 05/12/19/00 | LOCKED |
| §65 | Woche = 7 Spieltage: Wurzeltag, Blatttag, Wassertag, Steintag, Windtag, Lichttag, **Stilltag** (General-Händler +2 h später) | LOCKED |
| §66 | Mond „Lunar/der Schweigende“, 8 Phasen × 2 Spieltage = 16; Tag 1 = Zunehmende Sichel; Vollmond Tag 7–8; Nachtlicht +0…0,25 lx; nachtaktive Spawns ×0,8…×1,2 (`MoonPhases.csv`) – löst Q15 | LOCKED |
| §67 | Aktivitätsmuster `Behavior.Activity.Diurnal/Nocturnal/Crepuscular/Cathemeral/Midday` (genau eines je Art, zählt für DR-02), Kurven `ActivityCurves.csv`, Minimum 80 ‰; < 300 ‰ = Ruhe/Schlaf (Wahrnehmung −50 %, Einstimmen +1) | LOCKED |
| §67 | DR-32: jede Region in jeder Tagesphase ≥ 1 exklusive Aktivität | LOCKED |
| §68 | Lichtkurven `TimeOfDayCurves.csv` (Sonnenauf-/untergang 06/20, Max. 55°, Hvitfell Max. 30°), Nachtlesbarkeit L-N1–L-N5, Laternen 19:30–05:30, regionale Licht-Profile `DA_LightProfile_R##` | LOCKED |
| §68 | Current-Gen: 2 Directional Lights, Sky Atmosphere, Volumetric Clouds, Lumen, VSM; Switch 2: TOD-Irradiance-Blending (4 Schlüsselzeiten/Region, ~45 MB), CSM 3 Kaskaden, DFAO, SSGI | LOCKED |
| §68 | Reihenfolge Lichtmodulation: Basiskurve → Region → Wetter → Story (`MPC_Silence`) | LOCKED |
| §10 | ADR-070 – ADR-073 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Spieluhr (Ganzzahl, Pausieren, Koop, Zeit vorspulen, Story-Zeitpunkte)
- [x] Kalender: Woche mit Wochentagen, Mondphasen (Q15 gelöst)
- [x] Einfluss auf alle Systeme (Kreaturen, Quests, Händler, Musik, Licht + weitere) – Briefing erfüllt
- [x] Aktivitätsmuster der Echos (Daten) inkl. Schlaf-Gameplay
- [x] Lichtkurven (Daten), Nachtlesbarkeit, künstliche Lichter
- [x] Regionale Lichtprofile inkl. Tageslängen-Offsets
- [x] Innenräume, Höhlen, Himmel
- [x] Lumen-Setup und Switch-2-Lösung mit Vor-/Nachteilen
- [x] Code: Spieluhr, Phasen, Mond, Aktivitätsabfrage; Tests
- [x] ADR-070 – ADR-073, CANON aktualisiert
- [x] **Teil II (Welt) vollständig: K07–K15**

➡️ **Nächstes Kapitel: K16 – Monster Bible I: Kreaturendesign-Regeln, Taxonomie, Datenschema.**
