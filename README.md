# Ancient & Medieval Japan - Backgrounds & Traits（中世日本 - 背景と特性）

**First-release candidate: 0.1.0 (not yet published on Steam).** RimWorld 1.6 / 1.7. English / Japanese.

This standalone Mod adapts the backgrounds and traits of generated pawns to ancient and medieval Japan. In ordinary RimWorld, many original biographies refer to modern or futuristic professions; this Mod preserves the game's existing identities where possible while adding historically relevant lives and restricting anachronistic random selections.

## Backgrounds

- **126 existing backgrounds:** Historical names and descriptions rewritten (123 previous rewrites plus three original Core occupations).
- **12 new backgrounds** available for new pawn generation:
  - **Adulthood (8):** shrine officiant; shrine ritual attendant (shrine miko for women); itinerant ritualist (traveling miko for women); itinerant woodturner; falconer; potter; coastal fisher; coastal salt maker.
  - **Childhood (4):** hunter's child; traveling artisan's child; fishing village childhood; weaver's child.
- **135 anachronistic existing backgrounds** excluded from selection for newly generated pawns (77 adulthood and 58 childhood).
- **23 existing backgrounds** have their starting possessions adjusted.

These use the base game's existing skills and work systems. The three original Core occupation rewrites retain their original skills, work restrictions and starting possessions; Weaver63 additionally becomes eligible in the original Outlander category. Two overlapping woodcutter/weaver background IDs remain in the source solely for compatibility with prior saves, but are not normal new-pawn choices. Details are in the [design](Docs/Design.md).

## Traits

- **Likes alcohol (酒好き):** +2 mood while intoxicated.
- **Dislikes alcohol (酒嫌い):** −2 mood while intoxicated.

Neither new trait has a mood effect while sober; they are preferences, not alcohol dependence or tolerance. The existing **Transhumanist**, **Body Purist** and **Drug Desire** traits (including teetotaler) are excluded from ordinary new pawn generation, including documented forced-background paths. Existing trait definitions and already saved characters are not retroactively changed.

## Why this Mod exists

A randomly assembled RimWorld colony is not inherently a historical court, noble house or warrior clan. The background selection should still reflect plausible occupations and childhoods from a variety of ordinary Japanese communities without replacing every old biography one-for-one or requiring a specific social class.

## Requirements and compatibility

- **Required:** [Harmony](https://steamcommunity.com/sharedfiles/filedetails/?id=2009463077).
- **Optional:** [Medieval Overhaul](https://steamcommunity.com/sharedfiles/filedetails/?id=2553700067).
- **Save games:** Start a new game where possible. The original Def IDs are retained, but existing-save migration/loading and removal from an active save have not been verified.
- **Not included:** This Mod does not change shared-lodging mood rules, entrance/no-shoes, dining, bedding, drugs/chemical availability or initial addictions.

## Verification and limitations

Focused real-game acceptance passed with original RimWorld **1.7 Japanese Vanilla** and current separated Culture + Characters ([Actions #39587913897](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39587913897)); original **1.6 English + Medieval Overhaul 1.6.2.2/VEF/SYR + Culture + Characters** also passed ([Actions #39590687182](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39590687182)). These checks covered loaded definitions, original Core occupation changes, key exclusion/generation paths and generic pawn generation. Earlier trait mood checks passed within their scoped Vanilla 1.7 scenario.

Not verified by these passes: each biography's natural selection frequency; starting items awarded to actual generated pawns; an existing-save reload; MO 1.7; all DLC or third-party combinations; Japanese on-screen glyph layout; original MO MP3 playback or Steam subscriber download. No additional real-game test is implied by preparing this release metadata.

## 日本語概要

ポーンの背景と特性を古代から中世の日本に合わせて調整します。

### 背景

- **既存背景126件**の名称・説明を改稿。
- **新規成人期背景8件：**社の神職、社の神楽役（女性は「社に仕える巫女」）、巡回する祭祀役（女性は「渡り巫女」）、木地師、鷹匠、焼き物師、沿岸の漁師、浜の塩焼き。
- **新規幼少期背景4件：**狩人の家の子、渡り職人の子、漁村育ち、織屋の子。
- 時代に合わない**既存背景135件**を新しいポーンの生成候補から除外。
- **既存背景23件**の初期所持品を見直し。

### 特性

- **酒好き：**酩酊中の心情+2。
- **酒嫌い：**酩酊中の心情−2。
- 義体化願望・義体化嫌悪・薬物嗜好系特性（禁酒主義者を含む）が新しいポーンに付かなくなります。

### 対応・互換性

Harmony必須。Medieval Overhaulは任意。RimWorld 1.6／1.7対応、日本語・英語対応。新規ゲームを推奨します。既存セーブへの途中導入・削除は未検証です。初回公開候補で、Steamにはまだ掲載していません。

## Release documentation

- [Workshop bilingual BBCode](Docs/SteamWorkshopDescription.txt) (unpublished)
- [2game Japanese copy](Docs/2GameDescription-ja.txt) (unpublished)
- [Release checklist](Docs/ReleaseChecklist.md)
- **Workshop Preview approved:** `About/Preview.png` (640×380, directly resized from the accepted 960×540 cover; no regeneration). Acceptance of the preview does not mean the Mod has been uploaded to Steam.
- [Changelog](About/Changelog.txt)
- [Technical design](Docs/Design.md) and [native acceptance](Docs/Stage3NativeAcceptance.md)
- [MIT license](LICENSE)

Historical source provenance: [AMJ Culture split candidate](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture/commit/7448f290f2e1b0c0bdde93431c27662f0e066821).
