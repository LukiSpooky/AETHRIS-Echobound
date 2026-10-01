// Copyright AETHRIS Team. Build-Target (Game), siehe K05 §6.
using UnrealBuildTool;
using System.Collections.Generic;

public class AethrisTarget : TargetRules
{
	public AethrisTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.Latest;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.AddRange(new string[] { "AethrisCore", "AethrisGame" });
	}
}
