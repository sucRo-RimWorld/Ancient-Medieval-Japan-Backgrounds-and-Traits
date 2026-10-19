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

## Transition and save rules — completed extraction (2026-10-19)

Characters independent source and versioned DLLs are in its owner repository, built for RimWorld 1.6/1.7. The Culture extraction merged via [PR #160](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture/pull/160) to Culture main `52b16d398112a64b6f934dc0f5ea2ee0cc77c9e8`. Culture main removed the six transferred background/trait generation patches, two Japanese BackstoryDef localization files and Solid-child C# patch, and rebuilt its independent 1.6/1.7 DLLs. Characters therefore owns these generated rules **exclusively in current main**. Characters may optionally co-load with this cutover Culture version, **not an older unsplit Culture** containing duplicate XML/Harmony rules.

**Scoped original-game evidence:** Characters alone 1.6 [Project #39228255901](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228255901) PASS; Characters + cutover Culture 1.6 [#39229556343](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39229556343) PASS; Characters + cutover Culture 1.7 [#39228936614](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228936614) PASS. Each Pickle 1/1, Unity/raw ERROR0, exit0. Tests cover approved 77 adult, 55 Solid, 3 Shuffled restrictions, 89 loaded English text entries, Trait commonality, correct Harmony owner and generated Pawn; paired 1.7 also verifies Culture chair/meal paths. First paired 1.6 attempt in run #39228255901 crashed from native Mono GC SIGSEGV exit139 before Pickle; that failure remains recorded, not retroactively passed. A subsequent focused paired-only rerun succeeded; underlying crash cause unconfirmed.

**Boundaries:** No tested old-save migration, DLC, paired original MO, on-screen Japanese glyph or Steam publication. New game recommended; preserve original Def identities; do not claim mid-save installation/removal compatibility. Background Phase 2 remains accepted; new Trait Stage 2 design still unfinished.

## Repository ownership and migration provenance

The author-provisioned `sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters` is now the canonical source repository for Characters. The source originates from Culture's frozen independent-root candidate commit `7448f290f2e1b0c0bdde93431c27662f0e066821`. The new repository's original MIT `LICENSE` is preserved.

**Owner status:** source migrated via Characters PR #1 (`6deefec90d74bd99e89045f1cfbaf8031b3c97e6`), independent DLLs via PR #2 (`c7148fbc06a9b12c6e236988673afb715ff34c9f`), corrected background runtime test via PR #3 (`4c947fffa7bed55bf87a6df2815e778752512c54`). Production XML/DLL removal from Culture main via Culture PR #160 (`52b16d398112a64b6f934dc0f5ea2ee0cc77c9e8`). Native acceptance is limited to the three scoped PASS profiles above. The old independent-root candidate must never replace Culture main; the extracted owner is now Characters.
