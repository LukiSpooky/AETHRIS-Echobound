// Copyright AETHRIS Team. Schicht: Feature (siehe K05 §4).
using UnrealBuildTool;

public class GF_Breeding : ModuleRules
{
	public GF_Breeding(ReadOnlyTargetRules Target) : base(Target)
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
			"GameplayAbilities",
			"GameplayTasks",
			"AethrisCore",
			"GF_Monsters",
			"GF_World",
			"GF_Inventory"
		});
	}
}
