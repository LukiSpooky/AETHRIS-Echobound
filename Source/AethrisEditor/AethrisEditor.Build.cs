// Copyright AETHRIS Team. Editor-only: Validatoren, Importer, Tools. Darf alle Module lesen.
using UnrealBuildTool;

public class AethrisEditor : ModuleRules
{
	public AethrisEditor(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
		CppStandard = CppStandardVersion.Cpp20;
		PublicDependencyModuleNames.AddRange(new string[]
		{
			"Core", "CoreUObject", "Engine", "UnrealEd", "DataValidation", "GameplayTags",
			"AethrisCore", "AethrisGame", "GF_Monsters", "GF_World", "GF_Inventory"
		});
	}
}
