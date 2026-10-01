// Copyright AETHRIS Team. Schicht: Presentation (siehe K05 §4, K58 §9).
using UnrealBuildTool;

public class GF_VFX : ModuleRules
{
	public GF_VFX(ReadOnlyTargetRules Target) : base(Target)
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
			"Niagara",
			"AethrisCore",
			"GF_Monsters",
			"GF_World",
			"GF_Combat"
		});
	}
}
