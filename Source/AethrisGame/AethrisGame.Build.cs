// Copyright AETHRIS Team. Schicht: Game (GameMode, GameInstance, Game Flow). Darf nur AethrisCore nutzen.
using UnrealBuildTool;

public class AethrisGame : ModuleRules
{
	public AethrisGame(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
		CppStandard = CppStandardVersion.Cpp20;
		PublicDependencyModuleNames.AddRange(new string[]
		{
			"Core", "CoreUObject", "Engine", "GameplayTags", "EnhancedInput",
			"GameFeatures", "ModularGameplay", "AudioModulation", "AethrisCore"
		});
	}
}
