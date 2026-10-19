# AMJ Culture – Characters — independent Mod design

## Phase 3 — focused original childhood/adulthood additions (2026-10-19)

**Status:** an initial playable-source slice of **four new** Japanese-occupied `BackstoryDef` IDs, not 135 blanket replacements or completed character variety. Original Vanilla 1.6/1.7 has 784 IDs; Characters restricts 135 (adult 77, childhood 58), rewrites 123 other existing IDs, and leaves 526 neither modified nor restricted. This is an ID count, **not** a verified natural-roll distribution. Existing Core backgrounds and 123 revised narratives remain intact.

**First missing niches:** nearshore fishery working households, and village water-maintenance households. Original authored bilingual content in `Defs/BackstoryDefs/Backstories_P3CoastalWater.xml` and `Languages/Japanese/DefInjected/BackstoryDef/Backstories_P3CoastalWater.xml`:

| ID | Slot | Japanese | Gameplay skillGains | Intent |
|---|---|---|---|---|
| `AMJC_ShoreRaisedChild` | Childhood | 浜育ち | Cooking +1; Crafting +1; Social +1 | Shore gathering/net care, not shipboard warfare or the existing merchant biography |
| `AMJC_CanalRaisedChild` | Childhood | 用水のほとり育ち | Plants +2; Construction +1 | Village canal cleaning/levee familiarity, not generic academic study |
| `AMJC_InshoreFisherAdult` | Adulthood | 浜の漁師 | Cooking +3; Crafting +2; Plants +2 | Net work, fish preservation, shore gathering; no fabricated fishing skill or special pawn job |
| `AMJC_IrrigationKeeperAdult` | Adulthood | 用水の世話役 | Plants +3; Construction +3; Social +1 | Shared irrigation channel care, without requiring AMJ Waterworks |

**Spawn selection:** each defines `Civil` and `Tribal` plus `Medieval` and `MedievalCommon` compatibility categories so the same original authored records may be eligible under Vanilla and optional medieval-faction category patches. No `PawnKindDef` / `FactionDef` edits, no `forcedTraits`, `workDisables`, possessions, extra recipes, fisheries, watering tasks, land generation, World Tech Level or mandatory MO/Culture/Grains dependency. These categories do not promise a specific appearance probability: both pawn kind and faction filters must match, and other Mods may override them. With 2 childhood and 2 adulthood added symmetrically, do not apply a wholesale roll-rate override that would suppress other useful original backgrounds. Historical evidence and comparison with VE and non-VE existing Mods: `Docs/Research/P3BackgroundGapPriorArt.md`, validated-entry data in `Docs/Research/P3BackgroundPriorArtDecision.json`.

**Not yet completed:** loaded 1.6/1.7 `BackstoryDef`/DefInjected text, actual normal pawn spawning with different faction filters, current-MO compatibility, old saved-game loading, and numerical distribution are **unverified**, and require one focused final acceptance after source completion. Original modern background prose and already accepted 123 historical rewrites are unchanged. New TraitDef concepts `義理堅い`/`職人気質` are **not implemented**: they require a nonduplicative distinct gameplay effect and a separate trait specification before real addition. No Steam publication.

**Author scope decision (2026-10-19):** Split only **backgrounds and traits** from the existing AMJ Culture. Other Culture subfeatures remain in the original Mod, with no broader decomposition authorized. The identity and game effect of all existing original Vanilla/MO BackstoryDef and TraitDef records must remain stable.

## Scope

- Vanilla/MO historically inappropriate **ordinary background generation** restrictions: adult **77** (76 XML + FerventResearcher72), children **58** (55 original Solid biographies gated via Harmony + 3 Shuffled XML); existing unique/nonordinary references remain.
- **89** author-approved additional historical background rewrites and pre-existing **34** bilingual rewrites (total **123** existing DefNames rewritten, not newly generated backgrounds), matching English XML plus approved Japanese DefInjected.
- Existing **23** historical starting-possession XML substitutions (keep their original item source and Def identities).
- Trait generation: suppress ordinary Transhumanist, BodyPurist and DrugDesire plus known forced background entries; two author-approved alcohol-preference TraitDefs exist. Broader new traits remain future work.
- Harmony 1.6/1.7 Solid childhood generation patch and a **separate** minimal bootstrap, assembled into `AMJ.Culture.Characters.dll` per game version.

## Explicit exclusions — stay in Culture

- `Greedy` / `Jealous` barracks-related ThoughtWorker behavior, TraitDef contextual descriptions, thoughts and Japanese Thought translations: owning effect is the Culture **shared lodging** custom. Never copy SharedLodgingTraitPatch or SharedLodgingTraitThoughts here.
- New Pawn chemical addiction/tolerance generation, DrugDesire/psychoactive supplies and chemical balance: owning effect is Culture **drugs**. Never copy InitialDrugAddictionGenerationPatch.
- Entrance/no-shoes, chair meals, bedding, social Thought rules, other daily-life rules and their assemblies/assets.
- Neither Mod is a mandatory runtime dependency of the other. Harmony is required. Medieval Overhaul remains optional.

## Trait Stage 2 — artificial-body traits excluded (2026-10-19 author decision)

**Outcome:** Neither `Transhumanist` (義体化願望) nor `BodyPurist` (義体化嫌悪) belongs to normal newly generated ancient/medieval Japanese pawns. Both old TraitDefs and their already saved pawn effects are preserved for compatibility; deleting a Def or retroactively stripping an existing pawn is not authorized.

**Implementation:** `Patches/BodyPuristGeneration.xml` sets `BodyPurist.commonality=0` and conditionally removes its forced entries from `HunterOfTheKing53` and `TestSubject90`. `Patches/TranshumanistGeneration.xml` retains its previously approved commonality zero and `FerventResearcher72` category exclusion, and also conditionally removes that background's forced `Transhumanist`. Do not delete the backgrounds, their skills, other effects or Def IDs; their ordinary-generation exclusion remains. These explicit author decisions supersede the historical audit's proposed retention of BodyPurist. Unlisted third-party hard-coded forced trait paths are not automatically rewritten. Prosthetic/bionic mechanics and saved pawns are unaffected.

**XPath compatibility correction (2026-10-19):** The earlier Culture 1.6 unconditional removal `FerventResearcher72/forcedTraits/li[traitDef="Transhumanist"]` had a real missing-XPath ERROR. Existing 2026-10-19 conditional P2 removal patches for `BodyPurist` / `Transhumanist` and the prior `DrugDesire` correction now select either `li[key="..."]` or `li[traitDef="..."]`, applying removal only when a matching entry exists. The original TraitDefs, other forced traits and backstory identity are untouched. **Whether the authentic current 1.6 and 1.7 source XML actually matches these selectors is NOT yet verified in a loaded game; XML-only source integration is not proof the assignments were stripped.** Commonality-zero and background exclusion are independent. Do not assume an unconditional remove is safe.

**Acceptance:** XML source changed and original 1.6 test definition now also asserts `BodyPurist.commonality=0`; no fresh 1.6/1.7 loaded-game PASS or legacy-save compatibility claim. Later consolidated checks should verify the two original TraitDefs still exist, both have natural commonality zero, three original forced entries are absent, and ordinary new pawns get neither. No Steam release authorization.

## Trait Stage 2 — drug affinity removal and alcohol preferences (author direction, 2026-10-19)

**Approved exception:** Disable ordinary generation of all three `DrugDesire` degrees (chemical fascination, chemical interest, teetotaler), and introduce alcohol-only **酒好き** and **酒嫌い**. This explicit exception allows the two new TraitDefs during Stage 2, ahead of the general Stage 3 new-trait work.

**Existing identity preservation:** `Patches/DrugDesireGeneration.xml` changes `DrugDesire.commonality` to 0; the Def and its three old degrees remain available for saves. The patch conditionally strips just `DrugDesire` from original `DischargedSoldier53`, `MechanoidHacker93` and `VideoGamer16` forcedTraits. The two latter childhoods are already ordinarily excluded. Other forced traits, original backstory IDs, skills, restrictions and possessions stay unchanged. Do not automatically convert the soldier's former drug affinity into fondness for alcohol. Third-party forced assignments and pre-existing saved pawns are not migrated.

**New effective traits:** `AMJC_AlcoholLover` and `AMJC_AlcoholAverse` are two mutually exclusive, distinct TraitDefs (commonality 0.3 each; incompatible with legacy `DrugDesire`). Their `ThoughtWorker_Hediff` Thoughts activate only while original `AlcoholHigh` is present: Mood +2 or −2, respectively. Six identical stages cover original AlcoholHigh hediff stages 0–5 without increasing the reward for dangerous intoxication. No alcohol available or consumed means **no standing mood penalty or bonus**. Neither trait forces drinking, creates chemical need, overrides DrugPolicy, or changes addiction, tolerance, intoxication itself or withdrawal. 酒嫌い is a preference, **not** 下戸 (physical low tolerance).

**Module boundary:** Vanilla Beer and original Medieval Overhaul Ale/Cider/Mead/Wine use AlcoholHigh; future sake can be recognized if its effects use the same hediff. New TraitDefs, trait-generation restrictions and their related Thoughts live exclusively in Characters. Culture still owns drug supply and initial addiction generation; no Culture C#/XML/DLL is modified. No new dependency on Culture or MO.

**Acceptance:** XML source is the implementation, **not** a RimWorld 1.6/1.7 loaded-game PASS. Verify in a focused native game test: two loaded new TraitDefs, correctly gated alcohol-only Thoughts, no ordinary DrugDesire and no specified forced assignment, Beer+MO effect, and no unrelated old-def removal. Existing pre-change PASS is not evidence for this feature. Publication remains unauthorized.

## Transition and save rules — completed extraction (2026-10-19)

Characters independent source and versioned DLLs are in its owner repository, built for RimWorld 1.6/1.7. The Culture extraction merged via [PR #160](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture/pull/160) to Culture main `52b16d398112a64b6f934dc0f5ea2ee0cc77c9e8`. Culture main removed the six transferred background/trait generation patches, two Japanese BackstoryDef localization files and Solid-child C# patch, and rebuilt its independent 1.6/1.7 DLLs. Characters therefore owns these generated rules **exclusively in current main**. Characters may optionally co-load with this cutover Culture version, **not an older unsplit Culture** containing duplicate XML/Harmony rules.

**Scoped original-game evidence:** Characters alone 1.6 [Project #39228255901](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228255901) PASS; Characters + cutover Culture 1.6 [#39229556343](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39229556343) PASS; Characters + cutover Culture 1.7 [#39228936614](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228936614) PASS. Each Pickle 1/1, Unity/raw ERROR0, exit0. Tests cover approved 77 adult, 55 Solid, 3 Shuffled restrictions, 89 loaded English text entries, Trait commonality, correct Harmony owner and generated Pawn; paired 1.7 also verifies Culture chair/meal paths. First paired 1.6 attempt in run #39228255901 crashed from native Mono GC SIGSEGV exit139 before Pickle; that failure remains recorded, not retroactively passed. A subsequent focused paired-only rerun succeeded; underlying crash cause unconfirmed.

**Boundaries:** No tested old-save migration, DLC, paired original MO, on-screen Japanese glyph or Steam publication. New game recommended; preserve original Def identities; do not claim mid-save installation/removal compatibility. Background Phase 2 remains accepted; new Trait Stage 2 design still unfinished.

## Repository ownership and migration provenance

The author-provisioned `sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters` is now the canonical source repository for Characters. The source originates from Culture's frozen independent-root candidate commit `7448f290f2e1b0c0bdde93431c27662f0e066821`. The new repository's original MIT `LICENSE` is preserved.

**Owner status:** source migrated via Characters PR #1 (`6deefec90d74bd99e89045f1cfbaf8031b3c97e6`), independent DLLs via PR #2 (`c7148fbc06a9b12c6e236988673afb715ff34c9f`), corrected background runtime test via PR #3 (`4c947fffa7bed55bf87a6df2815e778752512c54`). Production XML/DLL removal from Culture main via Culture PR #160 (`52b16d398112a64b6f934dc0f5ea2ee0cc77c9e8`). Native acceptance is limited to the three scoped PASS profiles above. The old independent-root candidate must never replace Culture main; the extracted owner is now Characters.
