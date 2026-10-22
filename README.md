# Ancient & Medieval Japan - Backgrounds & Traits（中世日本 - 背景と特性）

**First-release candidate: 0.1.0 (not yet published on Steam).** RimWorld 1.6 / 1.7. English / Japanese.

This standalone Mod adapts the backgrounds and traits of generated pawns to ancient and medieval Japan. In ordinary RimWorld, many original biographies refer to modern or futuristic professions; this Mod preserves the game's existing identities where possible while adding historically relevant lives and restricting anachronistic random selections.

## Features

| Change | Count | Meaning |
| --- | ---: | --- |
| Existing backgrounds rewritten | **126** | Historical names and descriptions for 123 previously rewritten original IDs plus 3 original Core occupations. **These are not new backgrounds.** |
| Newly playable backgrounds | **12** | 8 adulthood and 4 childhood backgrounds eligible for ordinary pawn generation. |
| New IDs retained but not generated | **2** | Duplicate new woodcutter/weaver IDs kept to avoid removing definitions; excluded from ordinary selection. Total new source IDs: **14**. |
| Existing backgrounds restricted | **135** | 77 adulthood and 58 childhood records excluded from ordinary generation, **not deleted**. |
| New traits | **2** | Alcohol lover (酒好き) and alcohol averse (酒嫌い), with +2/−2 mood only while intoxicated. |
| Starting possession revisions | **23** | Change selected original item grants to fit the period. |

The 34 historical occupation rewrites, 89 additional rewrites and three original Core profession rewrites have **126 distinct original DefNames**. New IDs are counted separately. The 12 additions are *eligible* for ordinary generation; this does not guarantee that every new background is drawn in every scenario.

Existing original BackstoryDef/TraitDef identities remain intact. Original skill gains and work restrictions remain unchanged in the three newly rewritten Core occupations (`Logger16`, `Logger95`, `Weaver63`); only `Weaver63` also gains an `Outlander` candidate category. Targeted anachronistic forced traits and certain original possessions are changed according to the [design](Docs/Design.md).

The two new alcohol preferences have **no standing mood effect while sober**. Original `Transhumanist`, `BodyPurist` and `DrugDesire` traits are preserved for saved characters but disabled for normal new generation, including specifically documented forced-background paths. This Mod does **not** add alcohol production, new drugs, new professions/jobs, character skills or factions.

## Why this Mod exists

A randomly assembled RimWorld colony is not inherently a historical court, noble house or warrior clan. The background selection should still reflect plausible occupations and childhoods from a variety of ordinary Japanese communities without replacing every old biography one-for-one or requiring a specific social class.

## Requirements and compatibility

- **Required:** [Harmony](https://steamcommunity.com/sharedfiles/filedetails/?id=2009463077).
- **Optional:** [Medieval Overhaul](https://steamcommunity.com/sharedfiles/filedetails/?id=2553700067), and the separately maintained [AMJ Culture](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture). Neither is a hard dependency.
- **Important:** Do **not** combine this Mod with an **older, unsplit** AMJ Culture version that still contains the same generation patches. Use a current split Culture build if installing both Mods.
- **Save games:** Start a new game where possible. The original Def IDs are retained, but existing-save migration/loading and removal from an active save have not been verified.
- **Not included:** Shared-lodging/Greedy/Jealous mood rules, entrance/no-shoes, dining, bedding, drugs/chemical availability and initial addictions remain responsibilities of AMJ Culture.

## Verification and limitations

Focused real-game acceptance passed with original RimWorld **1.7 Japanese Vanilla** and current separated Culture + Characters ([Actions #39587913897](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39587913897)); original **1.6 English + Medieval Overhaul 1.6.2.2/VEF/SYR + Culture + Characters** also passed ([Actions #39590687182](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39590687182)). These checks covered loaded definitions, original Core occupation changes, key exclusion/generation paths and generic pawn generation. Earlier trait mood checks passed within their scoped Vanilla 1.7 scenario.

Not verified by these passes: each biography's natural selection frequency; starting items awarded to actual generated pawns; an existing-save reload; MO 1.7; all DLC or third-party combinations; Japanese on-screen glyph layout; original MO MP3 playback or Steam subscriber download. No additional real-game test is implied by preparing this release metadata.

## 日本語概要

RimWorldの人物背景・特性を古代から中世の日本向けに調整します。もとのポーンの背景IDをなるべく維持し、歴史的に不自然な通常生成を制限しつつ、庶民の職業・幼少期の選択肢を増やします。

**既存背景126件の名称・説明の改稿**と、**通常生成対象の新規背景12件（成人8・幼少期4）**は別の数です。新規定義は14件存在しますが、重複する職業2件は互換性のため定義だけを残して通常生成対象から外しています。既存背景135件の通常生成を制限（定義自体は保持）。既存背景23件の初期所持品を見直し、酒好き・酒嫌いの2特性を追加します。

Harmony必須。Medieval Overhaulと分離後の現行AMJ Cultureは任意。**分離前の旧Cultureとの同時導入は不可**。RimWorld 1.6／1.7対応、日英対応。新規ゲームを推奨します。旧セーブとの互換、MO 1.7等は未検証です。初回公開候補で、Steamへの掲載はまだ行っていません。

## Release documentation

- [Workshop bilingual BBCode](Docs/SteamWorkshopDescription.txt) (unpublished)
- [2game Japanese copy](Docs/2GameDescription-ja.txt) (unpublished)
- [Release checklist](Docs/ReleaseChecklist.md)
- [Changelog](About/Changelog.txt)
- [Technical design](Docs/Design.md) and [native acceptance](Docs/Stage3NativeAcceptance.md)
- [MIT license](LICENSE)

Historical source provenance: [AMJ Culture split candidate](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture/commit/7448f290f2e1b0c0bdde93431c27662f0e066821).
