// Copyright AETHRIS Team. Schicht: Core (siehe K05 §4). Keine Abhängigkeiten auf Projektmodule.
using UnrealBuildTool;

public class AethrisCore : ModuleRules
{
	public AethrisCore(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
		CppStandard = CppStandardVersion.Cpp20;
		PublicDependencyModuleNames.AddRange(new string[]
		{
			"Core", "CoreUObject", "Engine", "GameplayTags", "DeveloperSettings", "NetCore"
		});
	}
}
