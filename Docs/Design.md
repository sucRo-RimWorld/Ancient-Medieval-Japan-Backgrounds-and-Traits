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

**Source split is not runtime migration.** The old Culture `1.6/Assemblies/AMJ.Culture.dll`, `1.7/Assemblies/AMJ.Culture.dll` and its six original background-related XML patches **still contain** these rules until a coordinated cutover. Do not co-install this candidate with old Culture: duplicate Harmony gates and duplicate XML rewrites otherwise occur. Before releasing the extracted Mod, actually build its two versioned DLLs, remove all six owned XML files and the Solid-child C# patch from Culture, rebuild both Culture DLLs so no stale patch remains, and verify the new two-Mod combination and each separately in a bounded original-game acceptance. Revisit existing Culture title/About wording and generation claims at cutover; preserve valid unrelated gameplay/Thought/drug/entrance behavior. No direct-save migration and no Retroactive Pawn replacement. Recommend a new game; do not promise old save compatibility or mid-save removal safety.

**Recorded accepted evidence belongs to the prior Culture package, not the extracted package:** Vanilla 1.6/1.7 loaded-game + original MO compatibility acceptance (Project runs #39195995302, #39196173048, #39204533172, #39201144280); Japanese 89 full loaded-text match #39208562796. These provide a baseline for a **single cutover check**, not an automatically transferable PASS.

## Repository ownership and migration provenance

The author-provisioned `sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters` is now the canonical source repository for Characters. The source originates from Culture's frozen independent-root candidate commit `7448f290f2e1b0c0bdde93431c27662f0e066821`. The new repository's original MIT `LICENSE` is preserved.

**Compiled source, runtime cutover OPEN (2026-10-19):** Independent `AMJ.Culture.Characters.dll` builds have succeeded against original licensed RimWorld 1.6 and 1.7: 1.6 [Project #39224703490](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39224703490), blob `d35a2bb539faeda8e253f9823ac944a1cce7b405`, SHA256 `6bbc1c72cd14b48e3ad0637d0a29544c51e05a92a0195acdd6ffb0c5a1ed0705`; 1.7 [Project #39224930180](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39224930180), blob `471a3ddcf4e58a8babc86927433902c63c277691`, SHA256 `7641e14c37579911dbff6f1182fd88b578991966304de4b6437ce607e18aade8`. Both compiled original standalone source commit `6deefec90d74bd99e89045f1cfbaf8031b3c97e6`, installed via [Characters PR #2](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters/pull/2) main `c7148fbc06a9b12c6e236988673afb715ff34c9f`. **These are build-only successes, not new-Mod gameplay PASS.** Old Culture still contains overlapping background XML and Harmony gate. Do not co-install or release before a coordinated cutover and acceptance. Do not activate both versions simultaneously until the coordinated removal/rebuild and scoped runtime acceptance are completed. See main-only `Docs/Coordination.md`.
