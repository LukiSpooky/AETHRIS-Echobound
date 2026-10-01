// Copyright AETHRIS Team. Schicht: Domain (siehe K05 §4).
using UnrealBuildTool;

public class GF_Inventory : ModuleRules
{
	public GF_Inventory(ReadOnlyTargetRules Target) : base(Target)
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
			"AethrisCore"
		});
	}
}
