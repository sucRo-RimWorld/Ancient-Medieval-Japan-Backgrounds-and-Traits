# AMJ Culture – Characters — independent Mod design

**Author scope decision (2026-10-19):** Split only **backgrounds and traits** from the existing AMJ Culture. Other Culture subfeatures remain in the original Mod, with no broader decomposition authorized. The identity and game effect of all existing original Vanilla/MO BackstoryDef and TraitDef records must remain stable.

## Stage 3 原本職業への統合 — 2026-10-21 作者承認・実装

**変更後の原本日本語1.7ネイティブ受入（2026-10-21）:** [Project Actions #39587913897](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39587913897) はCharacters [PR #45](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters/pull/45) を指定した**実際のOriginal 1.7.4977日本語Vanilla環境でPASS**。Pickle1/1、Unity/FMOD ERROR0、exit0、原本3背景の年齢区分・完全な既存技能セット・必要な生成カテゴリ・日本語タイトル、元の新規2Defの読み込み維持と `AMJ_CultureExcluded` 1件のみのカテゴリを確認。新規P3の通常候補12件はコード上・ロード済み定義上の状態であって、全12件が実際に自然抽選された事実ではない。過去の「新しいPatchのゲーム受入未検証」という段落は検証**前**の履歴であり、最新の証拠は [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md) の「Approved Core occupational consolidation」節に整理。現在も **原本3件の日本語説明全文を厳密一致検査したものではなく**、既存セーブ/MO1.6/描画/個別自然抽選/初期所持品の実際の付与は未検証。製品C#・DLL変更なし、Steam公開は別途承認。



**最新の確定方針（先行の14件すべて通常生成候補という記述を上書き）:** 重複する新規成人 `AMJC_WoodcutterAdult`（杣人）・`AMJC_TextileWeaverAdult`（織物職人）の `spawnCategories` は `AMJ_CultureExcluded` **1件のみ**とし、**通常生成から除外する**。両 `BackstoryDef`、従来のtitle/titleShort/description、技能、旧セーブIDは保持する。残る新規12件は従来のカテゴリ・技能・本文を変更しない。現在のStage3 XMLは **14件存在・うち通常候補12件**（成人8・幼少4）。これは既存Core通常生成制限135件に加える**独立した新規Def2件の除外**であり、Core135件の数は変えない。

**職能の所有:** Vanilla 1.6/1.7原本 `Logger16`、`Logger95`、`Weaver63` のIDを維持したまま、PatchOperationReplaceで `title`／`titleShort`／`description` **だけ**を改稿する。日本語は `Languages/Japanese/DefInjected/BackstoryDef/Stage3CoreOccupationRewrites.xml` の各 `title`、`titleShort`、`baseDesc`、`description` に対応。原本の `slot`、`skillGains`、`requiredWorkTags`、`forcedTraits`、`workDisables`、`startingPossessions` 等は変更しない。原本のゲーム技能は次表の通りで、**廃止した新規P3の数値へ置換しない**。

| 原本ID | 日本語表示名／短縮名 | 既存技能（維持） | 生成カテゴリの扱い | 初期所持品（維持） |
|---|---|---|---|---|
| `Logger16` | 村の杣人／杣人 | Plants +6, Melee +3 | `Tribal / TribalLogger` **不変** | WoodLog ×10 |
| `Logger95` | 山の杣人／杣人 | Plants +8 | `Offworld / Outlander / Pirate / Scientist / Logger` **不変** | WoodLog ×10 |
| `Weaver63` | 織物職人／織物職人 | Crafting +6, Plants +2 | 原本 `Tribal` を維持し、**Vanillaの `Outlander` だけ追加** | Cloth ×10 |

**既存の日本語内容を活用した正本:**

- `Logger16`：「[PAWN_nameDef]は集落で使う材木を得るため、仲間と木を伐り、山から丸太を運んできた。斧の扱いに長け、力仕事でも頼りにされていた。」
- `Logger95`：「[PAWN_nameDef]は山林で材木に適した木を見極め、斜面の木を安全に伐り倒して運び出してきた。木の倒れる方向だけでなく、山林の状態にも気を配っていた。」
- `Weaver63`：「[PAWN_nameDef]は糸を紡ぎ、織機を使って布を作る仕事に長く携わってきた。糸の張り具合や布目の乱れを見分け、道具の手入れも自ら行っていた。」（従来承認済み織物職人から同文を再利用）

**追加しないもの:** 木地師 `AMJC_ItinerantWoodworkerAdult` や板材加工 `PlankCutter72` の技能・名前・生成カテゴリは現状維持。原本の特殊カテゴリや保存済みポーンは削除しない。任意の `Civil`・`MedievalCommon` を原本3件へ一律追加することは承認対象外（通常の Vanilla Outlander / MO Tribal の不足だけを補正）。新規P3の `AMJC_CoastalFisherAdult` 等12件にも干渉しない。既存Coreの通常生成制限135件の集合・計数は変更しない。

**所有ファイル:** 新規英語Core改稿 `Patches/Stage3CoreOccupationRewrites.xml`、日本語 `Languages/Japanese/DefInjected/BackstoryDef/Stage3CoreOccupationRewrites.xml`、新規P3の生成カテゴリ `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml`。Core原本は1.6/1.7同一値として[原本照合](Stage3ExistingModAudit.md)で確認済み。Patchは両版に同じ定義を当て、C#・独立Characters DLLを変更しない。元の新規14件LoadedDef受入[2026-10-21 Actions #39582470340](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39582470340)は**変更前ソースでのPASS**であり、原本3件の現在の新しい翻訳・生成カテゴリ変更や、新規2件の非抽選をまだ確認していない。旧テストでの新規2件通常カテゴリ期待値は失効。テストはまとめて変更分だけ確認する。通常候補入りが特定Defの自然抽選を保証するものではない。製品の公開・Steam更新は未承認。

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

**2026-10-20 source bug fix:** Prior conditional selectors looked for `forcedTraits/li[key="..."]` or `li[traitDef="..."]`; this was an ineffective no-op against original Core `BackstoryDef` XML. Original source for the six specified backgrounds actually uses named children `<forcedTraits><BodyPurist>0</BodyPurist></forcedTraits>`, `<Transhumanist>0</Transhumanist>` or `<DrugDesire>degree</DrugDesire>`. P2 conditionals now select the actual named child only, without removing the whole forcedTraits block, so `DischargedSoldier53` retains unrelated `TooSmart`. Both original TraitDef IDs and saved biography IDs remain intact. Added a **single existing background-game scenario assertion** that checks six loaded Defs have no targeted forced entries, checks the soldier still has `TooSmart`, and `DrugDesire.commonality=0` in addition to existing `Transhumanist`/`BodyPurist` commonality checks. Source correction is not proof of loaded-game PASS until this revised scenario runs. This specifically repairs the 2026-10-19 missing-XPath fallback design while keeping random commonality-zero separate from forced traits.

**Verified P2 forced-trait acceptance (2026-10-20): PASS in original RimWorld 1.7 English+cutover Culture ([Project run #39366130640](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39366130640)) and original Medieval Overhaul 1.6.2.2+cutover Culture ([run #39366126773](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39366126773)). Both use Characters source commit `3fe545fe8c3e1bb7ec0fc272b32ce91351f52e20` and Project manual runner `5e422839d3dbf6257de412503a90f078603ea6f8`; 1/1 Pickle PASS each, Unity ERROR0, exit0, game originals unchanged. In-game assertions proved the six original known forced `BodyPurist`/`Transhumanist`/`DrugDesire` assignments absent from loaded BackstoryDefs, soldier `TooSmart` still present, and all three targeted TraitDef commonality values zero. These are **loaded-Def facts**, not proof of all third-party forced assignments, long-run random rate, legacy-save reload or untested alcohol-only positive/negative Mood behavior. Steam release not authorized.

## Trait Stage 2 — drug affinity removal and alcohol preferences (author direction, 2026-10-19)

**Approved exception:** Disable ordinary generation of all three `DrugDesire` degrees (chemical fascination, chemical interest, teetotaler), and introduce alcohol-only **酒好き** and **酒嫌い**. This explicit exception allows the two new TraitDefs during Stage 2, ahead of the general Stage 3 new-trait work.

**Existing identity preservation:** `Patches/DrugDesireGeneration.xml` changes `DrugDesire.commonality` to 0; the Def and its three old degrees remain available for saves. The patch conditionally strips just `DrugDesire` from original `DischargedSoldier53`, `MechanoidHacker93` and `VideoGamer16` forcedTraits. The two latter childhoods are already ordinarily excluded. Other forced traits, original backstory IDs, skills, restrictions and possessions stay unchanged. Do not automatically convert the soldier's former drug affinity into fondness for alcohol. Third-party forced assignments and pre-existing saved pawns are not migrated.

**New effective traits:** `AMJC_AlcoholLover` and `AMJC_AlcoholAverse` are two mutually exclusive, distinct TraitDefs (commonality 0.3 each; incompatible with legacy `DrugDesire`). Their `ThoughtWorker_Hediff` Thoughts activate only while original `AlcoholHigh` is present: Mood +2 or −2, respectively. Six identical stages cover original AlcoholHigh hediff stages 0–5 without increasing the reward for dangerous intoxication. No alcohol available or consumed means **no standing mood penalty or bonus**. Neither trait forces drinking, creates chemical need, overrides DrugPolicy, or changes addiction, tolerance, intoxication itself or withdrawal. 酒嫌い is a preference, **not** 下戸 (physical low tolerance).

**Module boundary:** Vanilla Beer and original Medieval Overhaul Ale/Cider/Mead/Wine use AlcoholHigh; future sake can be recognized if its effects use the same hediff. New TraitDefs, trait-generation restrictions and their related Thoughts live exclusively in Characters. Culture still owns drug supply and initial addiction generation; no Culture C#/XML/DLL is modified. No new dependency on Culture or MO.

**Alcohol preference original-game acceptance (2026-10-20): scoped RimWorld 1.7 Vanilla PASS.** Characters [PR #23](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters/pull/23) introduced **test-only** in-game checks in the existing single-Pickle background scenario, with non-public `TraitDef.commonality` access corrected in [PR #24](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters/pull/24); current exact Characters source `8fd4af612f1233345752b56ec129f33b81618b68`. Production XML, versioned Characters/Culture DLLs and existing-save identifiers **did not change**.

**Accepted game evidence:** Original RimWorld `1.7.4977 rev1248` Vanilla + separated Culture/Characters, [Project Actions #39403987672](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39403987672), pinned Project runner [PR #842](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/pull/842), source `643139f5c307b2ede7bc006d64b153c3fce31ac8`: one original Pickle scenario **1/1 PASS**, Unity ERROR `[]`, FMOD errors `[]`, exit 0, original game unchanged. Test-only `AMJ_CULTURE_ALCOHOL_PREFERENCE_MOOD_OK` occurred **exactly once** in the retained launcher log (artifact `culture17-native-39403987672`, ID **12256633765**). The source verified exact loaded 0.3 generation weight for each trait, mutually exclusive / legacy `DrugDesire` conflicts, `requiredTraits` and `AlcoholHigh` links, and six stage mood effects fixed +2/-2. It sampled **six freshly generated, individually spawned Pawns** and inspected real `GetAllMoodThoughts` / `MoodOffset()`: sober/neutral, sober/lover, sober/averse, drunk/neutral all had no additional AMJC alcohol Thought; lover with `AlcoholHigh` severity 0.1 had exactly one +2; averse at severity 0.75 exactly one −2. Thus the existing alcohol preference feature is **functionally accepted for this Vanilla 1.7 scope**, without requiring production fixes. Existing P2 forced old Trait removals and seven P3 background checks also passed in the combined background-only scenario.

**Historical failed test, never PASS:** initial [Project #39403469697](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39403469697) failed test-only C# compilation (CS1061) because RimWorld `TraitDef.commonality` is private; no game had started. This was fixed through exact existing-reflection pattern, not by modifying the product.

**Original MO source cross-check, not gameplay:** inspected authentic MO 1.6.2.2 Workshop provider `3219596926`, paths `1.6/Defs/Drugs/Alcohol_Ale.xml`, `Alcohol_Cider.xml`, `Alcohol_Mead.xml`, `Alcohol_Wine.xml`. All four have `IngestionOutcomeDoer_GiveHediff` giving **`AlcoholHigh`**. They therefore satisfy this trait's already-tested conditional trigger **in source**, but actual 1.6+MO beverage ingestion and loaded mood are **not** proven by the 1.7 Vanilla test. Vanilla Beer likewise uses original `AlcoholHigh` as designed.

**Remaining OPEN (not grounds for repeating unchanged tests):** random natural spawn rate/distribution of alcohol Traits, direct original 1.6 MO beverage drinking and mood, non-original drugs or modded alcohol effects, 1.7 Japanese rendered appearance, DLC/other Trait systems, legacy-save migration, and Steam/Workshop publication. `DrugDesire` existing identity remains and original known forced background entries stay suppressed; the earlier P2 1.6 MO and 1.7 loaded commonality-zero evidence remains valid. No automatic native tests.

## Stage 3 — historical character diversity

The 2026-10-19 author decision restores period-Japanese character variety without mechanically replacing the 135 ordinary-generation restricted original biographies one-for-one. Existing approved **123** rewrites and previously restricted original Def IDs remain unchanged. The broader unimplemented occupation and childhood candidates (coastal fishing, salt work, textile craft, pottery, additional mobile livelihoods and hunter-specialist routes) remain in [Stage3BackgroundGapAnalysis.md](Stage3BackgroundGapAnalysis.md) as *proposals only*. Do not duplicate existing 神事見習いの子, 山野の猟師, 旅芸人, or generic monks/warriors/artisans. The five **implemented** P3 Defs, author-approved skill effects and genuine acceptance evidence follow below. The original written-content draft is [Stage3BackgroundDrafts.md](Stage3BackgroundDrafts.md).

The author corrected the initial misconception that Vanilla `Artistic` measures kagura/dancing: no Artistic bonus is assigned to the two ritual roles; dancing remains narrative. One practiced shrine-performer biography instead has `Nimble=0` and its real effect is melee dodge, *not* a dancing bonus. No new Ritual/Dance skill, jobs, forced social caste, faction, or DLC dependency was added.

## P3 — five new Japanese backgrounds (2026-10-20, source implemented)

The author continued the accepted P3 five-background plan after the proposed `Nimble` link. Scoped VE/non-VE comparison and no-dependency rationale: [Stage3ExistingModAudit.md](Stage3ExistingModAudit.md). **Production source** is `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` and matching `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`. Five new `AMJC_*` IDs, four adult and one child: `AMJC_ShrineOfficiantAdult` (社の神職; Social +4, Intellectual +2), `AMJC_ShrineRitualAttendantAdult` (社の神楽役／female-title 社に仕える巫女; Social +4, forced `Nimble=0`), `AMJC_ItinerantRitualistAdult` (巡回する祭祀役／female-title 渡り巫女; Social +5), `AMJC_ItinerantWoodworkerAdult` (木地師; Crafting +5, Plants +2) and `AMJC_HunterFamilyChild` (狩人の家の子; Shooting +2, Animals +1, Plants +1). No work disables, extra forced traits, special jobs, dance skills or DLC requirements.

For two ritual-worker biographies, `titleFemale` / `titleShortFemale` give historical miko wording for female pawns; generic `title` / `titleShort` are used otherwise. This is **not** a female-only spawning restriction and does not change Vanilla gender generation. The shared description applies to both genders. `Nimble` represents practiced bodily agility with an actual **melee dodge** gameplay effect; it does not add dance or artistic skill. `Tribal` supports original MO/VANILLA preindustrial backgrounds; `Civil`, `Traveler`, `Trader` are used selectively for original route diversity; `MedievalCommon` is a harmless optional category for separately installed Medieval Backstories Patch, not a required dependency. No new factions are introduced. These are XML additions, **not** modifications to the existing 135 restricted / 123 rewritten original IDs. `Docs/Stage3BackgroundDrafts.md` retains the full provenance/balance rationale and the 2026-10-19 pre-implementation draft as historical evidence, with latest source implementation status clearly appended.

**Focused original-game acceptance (2026-10-20): PASS for five Defs and the checked behaviors in BOTH 1.6 Japanese and 1.7 English, paired with separated Culture.** Exact executed checks, source pins, run artifacts, constraints and untested scopes are in [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md). Existing background Pickle steps read the real loaded five records, assert 4 adult/1 child, original `skillGains`, sole forced `Nimble=0`, active ordinary `Tribal` and optional `MedievalCommon` entries, Japanese male/female miko titles in 1.6, English settled-miko title variants in 1.7, and one ordinary Pawn generation. Both runs were 1/1 Pickle PASS, Unity ERROR0, exit0, source game unchanged. **Additional follow-up:** the current five Defs plus six P2 forced-trait removal checks passed original MO 1.6 loaded game and three MO player PawnKinds + one Brigand faction Pawn generation in [run #39366126773](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39366126773), while Vanilla 1.7 forced-trait removal also passed in [run #39366130640](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39366130640). Full itemized update in [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md). **Still unproven:** actual random selection of each newly added background, MO 1.7, Japanese 1.7 glyph inspection, existing-save reload and comprehensive third-party compatibility. No Steam release.

## P3 follow-on — 鷹匠 and 渡り職人の子 (2026-10-20)

The author approved both previous Japanese drafts and their exact skill values. Both are implemented as **new IDs**, preserving all 135 restricted originals, 123 rewritten originals and the first five P3 histories. Total new P3 biographies: **seven** (adult five; childhood two). Production sources: `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` and matching Japanese `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`.

| DefName | Slot | JA title / short | Actual Vanilla gains | Categories |
|---|---|---|---|---|
| `AMJC_FalconerAdult` | Adulthood | 鷹匠 / 鷹匠 | Animals +5, Plants +1 | Tribal, Civil, MedievalCommon |
| `AMJC_TravelingArtisanChild` | Childhood | 渡り職人の子 / 職人の子 | Crafting +2, Social +2 | Tribal, Civil, Traveler, MedievalCommon |

Both biographies have **no forced Trait, special pet, new hawking/family Job, work disables, possessions or DLC dependency**. Falconry is modeled only through `Animals` and minor outdoor familiarity (`Plants`), **not** `Shooting`; the mobile-artisan childhood represents ordinary family handwork and contact (`Crafting`, `Social`), not guaranteed related adult biographies. `MedievalCommon` is a harmless optional category, not a required provider. The prior VE/non-VE comparison is extended in `Docs/Stage3ExistingModAudit.md`; author-approved Japanese draft provenance and period caveats are in `Docs/Stage3BackgroundGapAnalysis.md`.

**Verified original-game acceptance (2026-10-20):** Both source-added biographies passed the amended, existing single-Pickle background check for loaded Def identities, slot, exact skill gains, no forced Traits, spawn-category membership and **English** male/female title in the original 1.6 MO and original 1.7 Vanilla profiles. The same scenario preserved the original five P3, six old forced-trait removals and one ordinary Pawn sample. Original **RimWorld 1.6.4871 rev598 + MO 1.6.2.2 + VEF/SYR + cutover Culture + Characters** [Project run #39398583001](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39398583001) PASS (Pickle 1/1, Unity ERROR0, exit0), additionally including representative MO PawnKinds/Faction Pawns. Original **RimWorld 1.7.4977 rev1248 Vanilla + cutover Culture + Characters**, *background-only* [run #39400155765](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39400155765) PASS (Pickle 1/1, Unity ERROR0, exit0; the new two-Def marker once). Exact Characters code main `a0022604affd644eeedb652226cfe58954f8edb8`, no recompilation of unchanged product Characters/Culture DLLs, no original game files changed. Earlier combined 1.7 [run #39398578851](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39398578851) **remains FAIL**: it stopped in an unrelated chair meal step before background assertions (Pickle 0/0, watchdog and end-of-run engine crash); this focused background PASS does **not** resolve or cover that chair test. Exact acceptance premises, artifact and limitations: [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md).

**Not established:** a random sample selected *each* of the seven biographies; their appearance frequencies; original MO MP3 compatibility without private audio transcode; Japanese 1.6/1.7 **new two-background** loaded text/glyph appearance (the 1.7 profile was English); MO 1.7; optional Medieval Backstories Patch/other third-party combinations; saved-game migration; alcohol-only +2/−2 Mood effects; the 1.7 chair scenario failure. No publication.

## P3 seven-biography ordinary selection category correction (2026-10-20)

**Player-facing problem:** the seven newly added `AMJC_*` histories previously provided `Tribal` and optional `MedievalCommon`, but not the standard Vanilla `Outlander` selector. The authentic, SHA-verified original 1.6/1.7 Vanilla Core metadata ([Project source audit](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/VanillaCoreCharacterDefsSourceAudit20261016.md), [native original artifact #12002927488](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/38797500765)) has 122 Vanilla BackstoryDefs with `Outlander` but only 1 with `Civil`, 0 with `Traveler`. Those latter categories cannot be assumed equivalent to `Outlander` when normal Vanilla factions select from their assigned backstory categories. Original MO 1.6.2.2 FactionDefs and PawnKindDefs use `Tribal` in its normal relevant routes ([Project original MO crosswalk](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/MO16BackstoryFilterCrosswalk.md)).

**Narrow implementation:** add `Outlander` to the **seven** new P3 Defs, retaining their existing `Tribal`, `Civil`, `Traveler`, `Trader` and optional `MedievalCommon` as applicable. Neither `Offworld` nor `Pirate` is added without a separate scope decision. Age slots, exact skills, Japanese and English prose, solely approved `Nimble` forced Trait, existing 135 restricted / 123 rewritten original biographies, and original saved IDs remain unchanged. No DLL rebuild; source-only XML correction. The existing consolidated background test now checks the `Outlander` category for all seven.

**Bounded evidence:** category intersections support ordinary Vanilla `Outlander` and original MO `Tribal` candidate eligibility; actual selection of every individual Def by random generation **is not demonstrated**, nor are appearance rates or fixed faction/quest routes. Prior native PASS runs used earlier XML and do not certify this new source until loaded-game acceptance. New game recommended; no DLC/Steam action.

## P3 — 織物職人・焼き物師の追加（2026-10-20承認、実ゲーム検証未実施）

既存の背景7件に加え、ユーザーが日本語本文・能力補正案を承認した成人背景2件を追加。P3新規背景合計**9件（成人7・幼少期2）**。新規ID・効果は以下。

| DefName | 日本語名 | Slot | 実際の能力補正 | 生成カテゴリ |
|---|---|---|---|---|
| `AMJC_TextileWeaverAdult` | 織物職人 | Adulthood | `Crafting +6` | `Outlander`, `Tribal`, `Civil`, `MedievalCommon` |
| `AMJC_PotterAdult` | 焼き物師 | Adulthood | `Crafting +4`, `Artistic +2` | `Outlander`, `Tribal`, `Civil`, `MedievalCommon` |

**史実・ゲーム上の意味:** 古代から織物生産が存在し、奈良・平安期の織物、鎌倉・室町期の窯業にも前例がある。織物職人は糸紡ぎ・織機・布地と道具保守に熟練する `Crafting` 専門。焼き物師は日常生活用の壺や甕を製作する `Crafting` 主体で、形づくりの感覚を補助的に `Artistic` と表現する。**ArtisticはMO陶器の製作速度を直接上げると保証しない**。`MedievalCommon` は任意カテゴリ、MO導入を必要としない。新しい織物・陶器・窯・専用Job・特性・所持品は追加しない。前の7件、123改稿、135通常生成制限、およびCultureとの所有分担は保持。

**日本語正本:** `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml` に承認済みの文章をそのまま収録（`description`／`baseDesc`）。同意された短縮名は通常名と同一で、男性・女性共通。英語原文は意味を合わせる。歴史的参照は日本工芸会の染織・陶芸の沿革と京都国立博物館の中世窯業解説。ゲーム挙動については製品XMLと既存単一Pickleシナリオに2件の存在・slot・能力・強制特性なし・生成カテゴリ・日英タイトル検査を追加した段階であり、**現時点ではRimWorld実起動PASSではない**。従来7件のPASSは新規2件の証明にならない。自然選択・出現率は別途未確認。

**漁師候補の技能整理（未実装）:** Odysseyの釣りは `Animals` が Fishing Speed／Fishing Yield に作用する。Vanilla Fishing Expandedの釣りもAnimals技能基準である。漁師背景は **`Animals +5` を基本候補**とする。釣り専用 `SkillDef` はなく、Odyssey/釣りModを依存化しない（未導入時はAnimals技能の一般的用途のみ）。漁師の日本語本文・生成カテゴリ・最終技能補正の承認までは製品に追加しない。製塩は海水製塩とMOの採掘塩を同一視しないため未実装。


## P3 — 浜の塩焼き（2026-10-21承認、XML実装）

**確定内容:** 新規11件目の成人 `BackstoryDef` は `AMJC_SaltMakerAdult`。日本語の表示名「浜の塩焼き」、略称「塩焼き」。英語名 `coastal salt maker`、略称 `salt maker`。技能は `Crafting +3`, `Cooking +2`、`Adulthood`、カテゴリ `Outlander / Tribal / Civil / MedievalCommon`、強制Trait・作業禁止・専用初期所持品なし。男女共通。以前からの十件と、制限した通常背景135件および既存IDを改稿した123件は変更しない。

**承認済み日本語本文（`baseDesc` と `description` が一致）:** [PAWN_nameDef]は海辺で塩水を濃縮し、釜で煮詰めて塩を作ってきた。天候を見ながら浜仕事を進め、燃料の管理や火加減にも慣れていた。

`Crafting` は製塩の道具・工程、`Cooking` は煮詰めと火加減の経験を既存技能で抽象化したもの。製塩の新Job・設備・レシピ・海水取得・塩ThingDef・専用スキル・製塩速度補正は**追加しない**。MOの採掘塩と海水製塩は別の生産行為であり、MO・DLCを必須にしない。4つのカテゴリは通常生成候補の設定で、海岸や特定の派閥で必ず選ばれることは保証しない。

**史実上の幅:** 古代には海藻・製塩土器などを用いる方法があり、中世には塩浜による採かんと釜による煮詰めが発達する。参考は [たばこと塩の博物館（古代）](https://www.tabashio.jp/collection/salt/s9/index.html)、[同（時代別）](https://www.tabashio.jp/collection/salt/s8/index.html)、[塩事業センター](https://www.shiojigyo.com/siohyakka/made/history.html)。特定の鉄釜・揚浜／入浜設備を古代を含む全員に固定しない。この背景は史実を踏まえた広い職業描写であり、全時代・全沿岸地域の画一的な製法を意味しない。

**正本・検証境界:** 製品ソースは `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` と `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`。新規一件だけのXML追加のためCharactersのC#／DLLは変更しない。前の十件の1.6/1.7実機PASSは維持するが、11件目の実機読込、表示、自然抽選、MO同時導入、既存セーブは未検証。実機テストを勝手に自動起動しない。VE/非VEおよび既存の沿岸漁師との比較は [Stage3ExistingModAudit.md](Stage3ExistingModAudit.md)。

## P3 — 漁村育ち（2026-10-21 承認）

新規12件目の `BackstoryDef` は `AMJC_FishingVillageChild`。幼少期 `Childhood`、日本語の表示名・略称は「漁村育ち」。英語は `fishing village childhood`／`fishing village child`。技能 `Animals +2`、`Crafting +1`。生成カテゴリは `Outlander`、`Tribal`、`Civil`、`MedievalCommon`。強制Trait、作業禁止、専用所持品、必須DLC・MO依存はない。新規背景12件の内訳は成人9件、幼少期3件。

承認済み日本語本文（baseDescとdescriptionを同文にする）：[PAWN_nameDef]は海沿いの集落で育ち、家族の漁を手伝いながら潮の満ち引きや季節ごとの魚の動きを覚えた。網や釣具の手入れ、獲った魚の運搬も手伝ってきた。

成人の沿岸の漁師（Animals +5）とは年齢・能力を分ける。狩人の家の子（Shooting +2／Animals +1／Plants +1）とは海辺の生活・道具の手入れを重視する点で異なる。漁村の子全般の普遍的習慣ではなく一個人の経歴とする。専用の釣りJob・道具・建造物・特殊な生成規則は追加しない。元の通常生成制限135件、既存改稿123件、先行新規11件の効果は変えない。

正本は英語 `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` と日本語 `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`。Vanilla/MO・VE/非VE比較は `Docs/Stage3ExistingModAudit.md`。XMLのみの追加でDLLの再ビルドは不要。新規背景の実ゲーム読込、日本語表示、抽選頻度、旧セーブ・MO同時導入は未確認。既存10件のPASSを新規2件へ拡張せず、新規背景がまとまってからまとめて実ゲーム確認する。

## P3 — 織屋の子（2026-10-21実装）

**背景と役割:** `AMJC_WeaverChild` は新規第13件の幼少期 `BackstoryDef`。日本語名・略称「織屋の子」、英語名・略称 `weaver's child`。家族が定住して織物を作る家庭で育ったという個人の経歴であり、職人身分の強制・職能を継承する親子生成ルールは含まない。成人の `AMJC_TextileWeaverAdult`（`Crafting +6`）や移動生活を描く `AMJC_TravelingArtisanChild`（`Crafting +2 / Social +2`）と区別し、幼少期の織物工程の見習いを `Crafting +3` のみで表す。新規P3は成人9件・幼少期4件、合計13件。

**製品設定:** `defName = AMJC_WeaverChild`、`slot = Childhood`、`skillGains = Crafting +3`、通常候補カテゴリ `Outlander / Tribal / Civil / MedievalCommon`。強制Trait、作業禁止、専用初期所持品、性別制限、追加スキル、DLC／MO必須依存を設けない。家族関係・定住地域・生成確率は制御しない。元の通常生成除外135件と元Def名を改稿した123件、先行12件は変更しない。

**日本語本文（製品のbaseDescとdescriptionは同文）:** [PAWN_nameDef]は布を織る家に育ち、糸を巻いたり、糸の張り具合を整えたりする手伝いをしてきた。織機の動きを見ながら簡単な織り仕事を覚え、道具を丁寧に扱うようになった。

**歴史的境界:** 古代～中世の布づくりにおける麻・絹の製糸・製織に対応する個別の家庭像とする。特定の綿織物産地、江戸期の問屋制家内工業、近代的工場制、職人ギルド制度は前提にしない。根拠資料は [福井県史・中世の衣料生産](https://www.library-archives.pref.fukui.lg.jp/fukui/07/kenshi/T2/T2-5-01-01-01-04.htm) と [古代日本の紡織体制・考古資料（国会図書館）](https://ndlsearch.ndl.go.jp/books/R000000004-I7201692)。子どもの具体的な役割は一般法則ではなく、この背景の人物設定である。

**所有と受入れ:** 日英の製品正本は `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` と `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`。VE／非VEおよび職歴比較は [Stage3ExistingModAudit.md](Stage3ExistingModAudit.md)。XMLのみの追加で既存CharactersのC#／1.6・1.7 DLLは変更しない。**先行10件の原本ゲームPASSは新規の3件目（塩焼き・漁村育ち・織屋の子）には適用されない。** この3件のLoadedDef、技能、言語表示、選択率、元セーブ／MO互換は未確認。ゲーム起動は他の追加背景とまとめる。

## P3 — 杣人（2026-10-21承認、14件目）

**確定仕様:** `AMJC_WoodcutterAdult`、`Adulthood`、日本語名・略称「杣人（そまびと）」、英語 `woodcutter`。能力補正 `Plants +6` のみ。通常生成候補 `Outlander`、`Tribal`、`Civil`、`MedievalCommon`。強制Trait、仕事禁止、初期所持品、独自Job、製材設備、伐採速度への追加パッチ、DLC・MO必須依存は設けない。新規P3合計14件（成人10件・幼少期4件）。元の通常生成制限135件・元Defの改稿123件・先行新規13件は不変。

**承認済み日本語本文（baseDesc／description同文）:** [PAWN_nameDef]は山林で材木に適した木を見極め、伐り倒して運び出す仕事をしてきた。斜面の状態や木の倒れる方向を読み、仲間と協力して丸太を山から下ろしていた。

**差別化とゲーム内効果:** 木材用の立木選定・伐採と山からの搬出が専門。既存の `AMJC_ItinerantWoodworkerAdult`（木地師、`Crafting +5 / Plants +2`）は木製品製作、改稿済み山野の猟師は狩猟、山里の大工は建築・加工を描く。RimWorldの既存 `Plants` 技能は伐採のほか栽培・収穫にも影響するが、職歴専用の伐採スキルは追加せず、`Plants +6` を汎用技能の抽象化として許容する。造材・運材を特別なスキルやHauling速度の上昇へ変換しない。薪炭生産、炭焼き、林業設備・森林管理メカニクスは対象外。

**史実上の根拠と限界:** [山川日本史小辞典・杣](https://www.historist.jp/word_j_so/entry/033959/) は古代の寺社・国家造営用材の杣と杣工を記述し、[平凡社世界大百科事典・杣工](https://kotobank.jp/word/%E6%9D%A3%E5%B7%A5-1181372) は古代中世の伐木・造材従事者を定義する。[國學院大學「そま」](https://jmapps.ne.jp/kokugakuin/det.html?data_id=32080) も万葉集の杣人を説明する。用語が時代や地域によって必ず同じ意味・地位・統制組織を指したとは仮定しない。伐採場の所有者、身分、特定寺社の配下や特殊な祭礼参加を固定しない。

**正本と検証限界:** 製品XMLは `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` と `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`。Vanilla/MOとVE・非VEの代替背景の範囲は `Docs/Stage3ExistingModAudit.md` に追記。XMLのみの変更でCharacters 1.6／1.7 DLLは変更しない。従来10件の原本ゲーム受入PASSはこの4件の追加背景（浜の塩焼き・漁村育ち・織屋の子・杣人）を対象にしていない。4件のLoadedDef・日本語ローカライズ・自然抽選・MO同時導入・旧セーブ挙動の実ゲーム検証は最終段階まで未実施。既存10件の変更なし部分を不要に再試験しない。

## P3候補監査 — 荘園の農家の子（2026-10-21、追加見送り）

**今回の評価:** 新規幼少期 `BackstoryDef`「荘園の農家の子」は**現時点では追加しない**。既存原本ID `ArtisanFarmer23` は Stage2 で「田畑育ち」に改稿済み。日本語正本 `Languages/Japanese/DefInjected/BackstoryDef/Stage2HistoricalBackstories.xml` の本文は「百姓の家に生まれ、幼いうちから田畑の仕事を手伝う」「作物の世話・炊事に慣れる」。英語本文も `Patches/Stage2HistoricalBackstories.xml` で改稿済みであり、元のDefName・slot・skillGains・生成カテゴリは改変しない。この原本は、荘園所属か否かを限定しない農家の子として表現できる。

**歴史的な違い:** 荘園の百姓には年貢・公事・夫役などの義務があり、負担形態や現地の組織は地域・時期により異なる。参照：[千葉県「日本の税の歴史」](https://www.pref.chiba.lg.jp/zeimu/aramashi/gakushuu/rekishi.html)、[『世界大百科事典』等「荘園」](https://kotobank.jp/word/%E8%8D%98%E5%9C%92-78844)、[兵庫県立歴史博物館・大部荘年貢米送状](https://rekihaku.pref.hyogo.lg.jp/database/shiryo/detail/?id=14453)。ただし、その差は主に社会的負担・土地支配の関係で、子どもの農作業技能に新たな `Plants` 等の数値差を設ける独立の根拠ではない。「年貢の運搬」「納入準備」は物語要素にはなるが、RimWorldの `Hauling` には個別の成長技能がなく、`Social`／`Intellectual` を加点する職歴根拠も不足する。新しい税・荘園管理メカニクスはこの人物背景の対象外。

**再評価条件:** `ArtisanFarmer23` が実際の Vanilla Outlander／MO Tribal 候補経路で選ばれるかは**未検証**。生成カテゴリ不一致が確認された場合には既存Defの候補適格性・パッチの修正要否を先に検討し、同内容の新規Defを追加することで迂回しない。現行14件のP3、135件の通常生成制限、123件の歴史的改稿、元Defの技能や出生背景は変更しない。候補保留はユーザーが将来具体的な追加効果・別の歴史的職能を認めた場合にのみ再検討する。これは原本ゲームのテスト結果ではなく、既存資料に基づく設計監査。

## P3 original Core 1.6/1.7 occupational overlap — exact source decision review (2026-10-21)

**Formal design gate remains OPEN, not a production change.** The directly inspected original-game 1.6.4871 and 1.7.4977 BackstoryDef source metadata from [Project Actions #38797500765](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/38797500765), artifact **12002927488**, CSV SHA-256 `5699065686d4d6bebd59a8244b88a4f5707c57a0d16b0300cadab09ef331228d` for **both versions**, resolves the previously unknown raw slot, skill, category and starting-item data. All these original Defs remain present under unchanged IDs and have not been excluded or rewritten by Characters:

- `Logger16`: Adulthood, `Plants +6 / Melee +3`, `Tribal / TribalLogger`, `PlantWork` required, 10 wood, no forced traits.
- `Logger95`: Adulthood, `Plants +8`, `Offworld / Outlander / Pirate / Scientist / Logger`, `PlantWork` required, 10 wood, no forced traits.
- `PlankCutter72`: Adulthood, `Plants +6 / Melee +3`, `Tribal / TribalLogger`, `PlantWork` required, no initial item/forced trait.
- `Weaver63`: Adulthood, `Crafting +6 / Plants +2`, `Tribal`, `Crafting` required, 10 cloth, no forced traits.

These are original `Shuffled` records, not unique `Solid` biographies. `Logger16` and `Logger95` independently represent the woodcutting trade on the MO/Vanilla category paths; original `Weaver63` covers textile weaving in the `Tribal` path. They overlap the approved `AMJC_WoodcutterAdult` (Plants+6, candidate Outlander/Tribal/Civil/MedievalCommon, no carried wood, no requiredWorkTags) and `AMJC_TextileWeaverAdult` (Crafting+6, same broad categories, no starting cloth, no requiredWorkTags). `PlankCutter72` is partial rather than identical overlap with 木地師. Exact normal random selection and its probability remain **unproven**; category string overlap is **not** an observed naturally generated individual. See [Stage3ExistingModAudit.md](Stage3ExistingModAudit.md) for complete comparison, source file SHA-256 and explicit MO source context.

**Recommended for author decision:** favor reusing original Def IDs and rewriting their period-specific name/body while preserving source traits, original bonuses, work tags and possessions if the chief goal is removing duplicated occupational Defs. However, this cannot reproduce the new P3's expanded candidate categories or fixed original skill values without an additional explicitly approved gameplay change. An alternative is to keep new original P3 IDs and restrict only overlapping category routes; that is also a **change of accepted generation rules** requiring author decision. The current 14 P3 entries, current original source definitions and author-approved bonuses must not be modified or deleted on audit alone. Newly added P3's Japanese-loaded original game PASS (#39582470340) is unchanged and proves load behavior, **not professional uniqueness**. Do not start fresh native tests before any authorized production changes.

**Adjacent childhood eligibility note:** `ArtisanFarmer23`「田畑育ち」 is original `Solid_Child`, category only `Farmer`, `Plants +7 / Intellectual -2 / Cooking +2`, `Violent` work disabled (same in 1.6/1.7). Ordinary `Outlander/Tribal` selection is **not implied** by its existence. This does not automatically approve adding 「荘園の農家の子」.

## P3 14 backgrounds — added four original 1.7 Japanese runtime acceptance (2026-10-21)

The four later author-approved biographies `AMJC_SaltMakerAdult` (浜の塩焼き), `AMJC_FishingVillageChild` (漁村育ち), `AMJC_WeaverChild` (織屋の子), `AMJC_WoodcutterAdult` (杣人) now have **original 1.7.4977 Japanese Vanilla loaded-game acceptance PASS**: [Project Actions #39582470340](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39582470340), Pickle 1/1, Unity errors 0, FMOD errors 0, exit 0, actual newest four marker exactly once. All 14 P3 Japanese entries' source and live-loaded titles, short titles and full descriptions were compared; the four new Defs' exact skill values, adulthood/childhood slot, full set of four normal categories and no forced Traits were checked. Earlier ten and P2 restrictions plus one **generic** generated Pawn retained their scenario assertions. This replaces the **test-status portions only** of each new four P3 section above; all product specifications remain authoritative and unchanged. Independent exact evidence, pinned source/DLL hashes and caveats: [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md), section 2026-10-21.

**Not demonstrated:** that each background itself was naturally selected for a Pawn, any measured selection rate, original 1.6/MO simultaneous latest-four profile, old saved games, Japanese on-screen glyph/line wrapping, DLC/optional packs or Steam publication. The background additions remain XML-only, with **no new product DLL build** and no general release authorization.

## P3 — ten backgrounds original 1.7 runtime acceptance (2026-10-20)

The **ten** newly owned P3 `BackstoryDef` records (eight adult, two child) now have a single consolidated, original-game **RimWorld 1.7 English/Vanilla + cutover Culture/Characters** loaded acceptance **PASS**. This covers the seven previously accepted biographies after their `Outlander` category addition, `AMJC_TextileWeaverAdult` (Crafting +6), `AMJC_PotterAdult` (Crafting +4 / Artistic +2) and `AMJC_CoastalFisherAdult` (Animals +5), with all intended ages/categories/forbidden forced Traits and translated *English* titles. An original Pawn can still be generated. The same scenario retained P2 old forced-trait removals and alcohol mood effects. [Project Actions #39417930528](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39417930528) PASS, Pickle 1/1, Unity/FMOD error 0, exit 0, source SHA `b37131dd61ed3a8712641a612b85a5a508d0adbc`. See the owner [itemized acceptance and exact markers](Stage3NativeAcceptance.md) and [coastal fisher canonical design](Stage3CoastalFisherDesign.md). No new DLL was needed for XML-only biographies.

Do not equate loaded English Def validation with Japanese live glyph/description verification, natural random *drawing of each* of the ten, natural frequency, compatibility with latest MO, or existing-save/Steam approval. The prior 1.6+MO P3-seven result remains limited to that earlier source. Prior paragraphs describing three latest backgrounds as untested are superseded **only for this narrow original 1.7 English loaded scope**.

## P3 ten Japanese biographies — accepted loaded Japanese originals (2026-10-20)

All **ten** new Characters biographies now pass both the previously accepted original-game **1.7 English** [#39417930528](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39417930528) and **1.7 Japanese** [#39423122996](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39423122996) loaded validation. The Japanese test uses the actual `Japanese (日本語)` language initialized before game launch and checks exact approved `title`/`titleShort`/`description` against source DefInjected for all ten (and female title variants). The previous 89 Stage2 Japanese histories also match; existing Solid filtering and general Pawn generation remain functional. Detailed source pins, expected values, errors and acceptance scopes in [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md). Original XML is unchanged.

The first *in-session Japanese switch* test [#39422291959](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39422291959) is a real **FAIL** due to language-reload transient errors/Solid test; Project **runner-only** initialization fix [#852](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/pull/852) and the one affected retest resolved it. Loaded-data Japanese PASS is **not pixel/glyph appearance approval**. All ten source categories intersect existing Vanilla Outlander and MO Tribal routes; actual random selection of each, its rate and current MO load remain unverified, not proven by generic Pawn generation. No Steam publication.

## Current-version compiled Characters 1.6/1.7 product acceptance (2026-10-20)

Following Characters [PR #32](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters/pull/32) rebuilding the versioned product binaries, exact current owner main `d81711a038f4b69bd5516897b6223f135692e60b` now has both original native profiles accepted:
[1.7 Japanese Vanilla #39425746547](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39425746547) **PASS** and [1.6 English MO #39426497606](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39426497606) **PASS** (one existing Pickle scenario each, exit 0, game Unity errors 0). The former asserts real `Japanese (日本語)` loaded title, short-title and description for ten P3 and 89 old Stage2, correct gender variations, actual latest SHA-256-verified 1.7 DLL and loaded background/trait regression checks. The latter stages the rebuilt 1.6 DLL plus original MO 1.6.2.2 and tests FactionDef/PawnKindDef/Pawn population, P3 ten histories and prior exclusions. MO audio is converted to temporary PCM **inside a disposable game copy**, not unmodified-MP3 compatibility. The source-level `Tribal/Outlander` categories are adequate candidate-route metadata, *not* proof all ten have appeared in natural RNG draws or their frequencies. Japanese glyph pixel visibility, old saves, MO1.7, third-party combinations, Steam remain out of scope. Precise itemized premises, artifacts, pre-game failed first attempt and fixed runner guard are in [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md). No new production code or biography content changed.

## Transition and save rules — completed extraction (2026-10-19)

Characters independent source and versioned DLLs are in its owner repository, built for RimWorld 1.6/1.7. The Culture extraction merged via [PR #160](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture/pull/160) to Culture main `52b16d398112a64b6f934dc0f5ea2ee0cc77c9e8`. Culture main removed the six transferred background/trait generation patches, two Japanese BackstoryDef localization files and Solid-child C# patch, and rebuilt its independent 1.6/1.7 DLLs. Characters therefore owns these generated rules **exclusively in current main**. Characters may optionally co-load with this cutover Culture version, **not an older unsplit Culture** containing duplicate XML/Harmony rules.

**Scoped original-game evidence:** Characters alone 1.6 [Project #39228255901](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228255901) PASS; Characters + cutover Culture 1.6 [#39229556343](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39229556343) PASS; Characters + cutover Culture 1.7 [#39228936614](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228936614) PASS. Each Pickle 1/1, Unity/raw ERROR0, exit0. Tests cover approved 77 adult, 55 Solid, 3 Shuffled restrictions, 89 loaded English text entries, Trait commonality, correct Harmony owner and generated Pawn; paired 1.7 also verifies Culture chair/meal paths. First paired 1.6 attempt in run #39228255901 crashed from native Mono GC SIGSEGV exit139 before Pickle; that failure remains recorded, not retroactively passed. A subsequent focused paired-only rerun succeeded; underlying crash cause unconfirmed.

**Boundaries:** No tested old-save migration, DLC, paired original MO, on-screen Japanese glyph or Steam publication. New game recommended; preserve original Def identities; do not claim mid-save installation/removal compatibility. Background Phase 2 remains accepted; new Trait Stage 2 design still unfinished.

## Repository ownership and migration provenance

The author-provisioned `sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters` is now the canonical source repository for Characters. The source originates from Culture's frozen independent-root candidate commit `7448f290f2e1b0c0bdde93431c27662f0e066821`. The new repository's original MIT `LICENSE` is preserved.

**Owner status:** source migrated via Characters PR #1 (`6deefec90d74bd99e89045f1cfbaf8031b3c97e6`), independent DLLs via PR #2 (`c7148fbc06a9b12c6e236988673afb715ff34c9f`), corrected background runtime test via PR #3 (`4c947fffa7bed55bf87a6df2815e778752512c54`). Production XML/DLL removal from Culture main via Culture PR #160 (`52b16d398112a64b6f934dc0f5ea2ee0cc77c9e8`). Native acceptance is limited to the three scoped PASS profiles above. The old independent-root candidate must never replace Culture main; the extracted owner is now Characters.
