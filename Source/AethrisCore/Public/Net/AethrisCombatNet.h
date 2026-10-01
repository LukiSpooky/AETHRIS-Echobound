// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"

/**
 * Netzformat des Kampfes (K59 §5). Liegt in Core, weil GF_Combat (Auflösung) und GF_Multiplayer/GF_PvP
 * (Transport) es teilen, ohne sich zu kennen (CANON §26).
 *
 * Der Client sendet nur Wünsche (Befehle), der Server löst auf und sendet Ergebnisse (DR-21).
 * Bit-Layout NM_COMBAT_COMMAND (49 Bit → 7 Byte, Referenz tools/ref/aethris_net.py):
 *   Tick 32 | Slot 3 | Action 3 | Ability 4 | Target 4 | Reserve 3
 */
enum class EAethrisCombatAction : uint8
{
	Ability = 0,     ///< Fähigkeit aus dem Kampfset (Ability = Index 0–3) oder Crescendo (Index 4)
	Switch = 1,      ///< Wechsel aus der Reserve (Reserve = Reserveplatz 0–5)
	Item = 2,        ///< Gegenstand (Ability = Taschenplatz 0–15)
	Bond = 3,        ///< Bindung (nur Wildkampf, Koop)
	Guard = 4,       ///< Abwarten/Schützen
	Flee = 5,        ///< Fliehen (nicht in PvP/Raid)
	Forfeit = 6      ///< Aufgeben (PvP)
};

struct AETHRISCORE_API FAethrisCombatCommand
{
	uint32 Tick = 0;          ///< Zeitleisten-Tick, für den der Befehl gilt (muss = Zug-Tick des Echos sein)
	uint8 Slot = 0;           ///< 0–7: aktives Echo des Absenders (Raid: bis 8 Plätze je Seite)
	EAethrisCombatAction Action = EAethrisCombatAction::Guard;
	uint8 Ability = 0;        ///< 0–15
	uint8 Target = 0;         ///< 0–15: Zielplatz (0–7 eigene Seite, 8–15 Gegnerseite)
	uint8 Reserve = 0;        ///< 0–7

	/** Packt den Befehl in 7 Byte (Little Endian). Liefert false bei Werten außerhalb der Bitbreiten. */
	bool Pack(uint8 (&Out)[7]) const;
	static bool Unpack(const uint8 (&In)[7], FAethrisCombatCommand& Out);

	bool operator==(const FAethrisCombatCommand&) const = default;
};

/** Prüfsumme des Kampfzustands nach jedem Ergebnis (NM_COMBAT_HASH): FNV-1a 64 über die kanonische Serialisierung. */
namespace Aethris::Net
{
	AETHRISCORE_API uint64 Fnv1a64(const uint8* Data, int32 Num, uint64 Seed = 0xcbf29ce484222325ull);
}
