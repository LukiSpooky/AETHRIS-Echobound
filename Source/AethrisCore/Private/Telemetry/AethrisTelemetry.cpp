// Copyright AETHRIS Team.
#include "Telemetry/AethrisTelemetry.h"
#include "HAL/PlatformTime.h"

void UAethrisTelemetrySubsystem::Record(FName EventName, TMap<FName, FString> Attributes)
{
	if (!bOptIn)
	{
		return; // Ohne Einwilligung wird nichts erfasst (auch nicht gepuffert).
	}
	FAethrisTelemetryEvent& E = Buffer.AddDefaulted_GetRef();
	E.Name = EventName;
	E.Attributes = MoveTemp(Attributes);
	E.SessionSeconds = FPlatformTime::Seconds();
	if (Buffer.Num() >= 256)
	{
		Flush();
	}
}

void UAethrisTelemetrySubsystem::Flush()
{
	if (Buffer.IsEmpty())
	{
		return;
	}
	for (const auto& Sink : Sinks)
	{
		Sink(Buffer);
	}
	Buffer.Reset();
}
