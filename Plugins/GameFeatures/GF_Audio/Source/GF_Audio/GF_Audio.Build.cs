// Copyright AETHRIS Team. Schicht: Presentation (siehe K05 §4).
using UnrealBuildTool;

public class GF_Audio : ModuleRules
{
	public GF_Audio(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
		CppStandard = CppStandardVersion.Cpp20;

		// Erlaubte Abhängigkeiten gemäß Schichtenregel – geprüft durch tools/check_layers.py
		PublicDependencyModuleNames.AddRange(new string[]
		{
			"Core",
			"CoreUObject",
			"Engine",
			"GameplayTags",
			"UMG",
			"CommonUI",
			"ModelViewViewModel",
			"AethrisCore",
			"GF_Monsters",
			"GF_World",
			"GF_Inventory",
			"GF_Combat",
			"GF_Capture",
			"GF_Companion",
			"GF_Breeding",
			"GF_Research",
			"GF_Economy",
			"GF_Quests",
			"GF_AI",
			"GF_Save",
			"GF_Multiplayer",
			"GF_PvP"
		});
	}
}
