// Copyright AETHRIS Team. Build-Target (Server), siehe K05 §6.
using UnrealBuildTool;
using System.Collections.Generic;

public class AethrisServerTarget : TargetRules
{
	public AethrisServerTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Server;
		DefaultBuildSettings = BuildSettingsVersion.Latest;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.AddRange(new string[] { "AethrisCore", "AethrisGame" });
	}
}
