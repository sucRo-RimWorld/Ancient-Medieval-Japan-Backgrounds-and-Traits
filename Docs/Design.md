# AMJ Culture – Characters — independent Mod design

**Author scope decision (2026-10-19):** Split only **backgrounds and traits** from the existing AMJ Culture. Other Culture subfeatures remain in the original Mod, with no broader decomposition authorized. The identity and game effect of all existing original Vanilla/MO BackstoryDef and TraitDef records must remain stable.

## Scope

- Vanilla/MO historically inappropriate **ordinary background generation** restrictions: adult **77** (76 XML + FerventResearcher72), children **58** (55 original Solid biographies gated via Harmony + 3 Shuffled XML); existing unique/nonordinary references remain.
- **89** author-approved additional historical background rewrites and pre-existing **34** bilingual rewrites (total **123** existing DefNames rewritten, not newly generated backgrounds), matching English XML plus approved Japanese DefInjected.
- Existing **23** historical starting-possession XML substitutions (keep their original item source and Def identities).
- Trait generation such as **Transhumanist commonality 0**, with its related forced adult background restriction; trait redrafting/new culturally fitting TraitDefs remain **future work**, not approved as complete.
- Harmony 1.6/1.7 Solid childhood generation patch and a **separate** minimal bootstrap, assembled into `AMJ.Culture.Characters.dll` per game version.

## Explicit exclusions — stay in Culture

- `Greedy` / `Jealous` barracks-related ThoughtWorker behavior, TraitDef contextual descriptions, thoughts and Japanese Thought translations: owning effect is the Culture **shared lodging** custom. Never copy SharedLodgingTraitPatch or SharedLodgingTraitThoughts here.
- New Pawn chemical addiction/tolerance generation, DrugDesire/psychoactive supplies and chemical balance: owning effect is Culture **drugs**. Never copy InitialDrugAddictionGenerationPatch.
- Entrance/no-shoes, chair meals, bedding, social Thought rules, other daily-life rules and their assemblies/assets.
- Neither Mod is a mandatory runtime dependency of the other. Harmony is required. Medieval Overhaul remains optional.

## Transition and save rules

**Source and versioned binary separation is implemented; active Culture migration is not merged or accepted.** Characters 1.6/1.7 independently compiled DLLs are in owner main at `c7148fbc06a9b12c6e236988673afb715ff34c9f` (original licensed Project build-only runs [1.6 #39224703490](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39224703490), [1.7 #39224930180](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39224930180)). The old Culture **main** still carries overlapping XML/Harmony. Culture cutover topic branch `refactor/characters-cutover`, commit `f071f0602e9989a011f431f30a961499dcd38ee7`, removes the six XML patches, two Japanese locale XMLs and Solid-child C# and carries newly rebuilt 1.6/1.7 Culture DLLs; it is **not yet merged to main**. Therefore do **not co-install Characters with current Culture main**. A bounded original-game acceptance of the new two-Mod combination must PASS before main cutover or publication. No retroactive Pawn replacement, direct-save migration or verified old-save compatibility. A new game is recommended.

**Recorded accepted evidence belongs to the prior Culture package, not the extracted package:** Vanilla 1.6/1.7 loaded-game + original MO compatibility acceptance (Project runs #39195995302, #39196173048, #39204533172, #39201144280); Japanese 89 full loaded-text match #39208562796. These provide a baseline for a **single cutover check**, not an automatically transferable PASS.

## Repository ownership and migration provenance

The author-provisioned `sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters` is now the canonical source repository for Characters. The source originates from Culture's frozen independent-root candidate commit `7448f290f2e1b0c0bdde93431c27662f0e066821`. The new repository's original MIT `LICENSE` is preserved.

**Scoped extraction evidence (2026-10-19):** original RimWorld 1.6.4871 rev598 Characters **alone** passed full existing 77 adult / 55 Solid / 3 Shuffled, 89 English text, Trait commonality, registered Harmony owner and real generated Pawn tests (Pickle 1/1, Unity/raw ERROR 0, exit 0) in [Project run #39228255901](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228255901), Characters test source `4c947fffa7bed55bf87a6df2815e778752512c54` and built DLL `c7148fbc06a9b12c6e236988673afb715ff34c9f`. In the **same run**, separate Characters + rebuilt Culture 1.6 process crashed with native Mono GC SIGSEGV (exit 139) before Pickle result, so combined 1.6 **FAIL/UNRESOLVED**, not a successful compatibility check. Original 1.7 paired test is separately pending. Do not activate both alongside old Culture main or publish until scoped combined validation passes; maintain main-only coordination.
