// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "Save/AethrisSaveTypes.h"

/** Ein Fragment als Rohbytes (vom ISaveFragmentProvider geschrieben oder unbekannt mitgeschleppt, SA-04). */
struct GF_SAVE_API FAethrisSaveFragmentBlob
{
	FName Id;
	int32 Version = 1;
	TArray<uint8> Data;
};

/**
 * Container-Format v2 (K64 §2, Referenz tools/ref/aethris_save.py – Testvektor `aethris_save.py vector`):
 *   u32 Magic · u32 ContainerVersion · u32 HeaderSize · Header · u32 Count · Einträge [Id, Version, Offset, Size, Crc32] · Nutzlast · u32 PayloadCrc32
 * Kompression (Oodle) und Plattform-Verschlüsselung liegen außerhalb des Containers (SaveGame-System der Plattform).
 */
namespace Aethris::Save
{
	GF_SAVE_API void WriteContainer(const FAethrisSaveHeader& Header, const TArray<FAethrisSaveFragmentBlob>& Fragments, TArray<uint8>& Out);

	/**
	 * Liest einen Container. Fragmente mit falscher CRC landen in OutCorrupt (SA-03: nur diese zurücksetzen),
	 * alle anderen in OutFragments. Rückgabe false nur bei unbrauchbarem Container (Magic, Größen) → Rotationskopie laden.
	 */
	GF_SAVE_API bool ReadContainer(const TArray<uint8>& In, FAethrisSaveHeader& OutHeader, TArray<FAethrisSaveFragmentBlob>& OutFragments, TArray<FName>& OutCorrupt);
}
