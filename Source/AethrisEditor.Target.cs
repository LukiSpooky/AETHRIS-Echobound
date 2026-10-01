// Copyright AETHRIS Team. Build-Target (Editor), siehe K05 §6.
using UnrealBuildTool;
using System.Collections.Generic;

public class AethrisEditorTarget : TargetRules
{
	public AethrisEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.Latest;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.AddRange(new string[] { "AethrisCore", "AethrisGame", "AethrisEditor" });
	}
}
