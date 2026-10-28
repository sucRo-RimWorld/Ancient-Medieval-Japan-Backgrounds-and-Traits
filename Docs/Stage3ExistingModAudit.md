# P3 five biographies — bounded existing-Mod comparison

**Owner:** Characters. **Date:** 2026-10-20. **Decision:** add five new narrowly scoped period-Japanese biographies via existing BackstoryDef XML to Characters; no additional Mod dependency, job or ability.

| Provider and dated evidence | Function / compatibility / historical fit | Load or maintenance cost | Decision |
|---|---|---|---|
| Original Vanilla Core 1.6/1.7, [Project original XML metadata](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/VanillaCoreCharacterDefsSourceAudit20261016.md) | 784 biography identities; existing Characters rewrites 123 original stories (includes shrine novice, adult hunter, travelers). Does not supply these five *distinct* adult/child Japanese story identities among the rewrites | No dependency; preserve all previous Def IDs | Extend existing Characters |
| Original Medieval Overhaul 1.6.2.2, [Project original Faction/PawnKind audit](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/MO16BackstoryFilterCrosswalk.md) | Original MO has `Tribal` selectors; optional Medieval Backstories Patch uses `MedievalCommon`; not same five AMJ BackstoryDefs in inspected original content | MO optional; no hard integration | Keep optional, expose category candidates |
| Historical Backstories 3611930252, [Project original XML metadata](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/WorkshopBackstoryOriginalsAudit20261016.md) | 500 backgrounds and 23 trait nodes, broad world and eight faction categories; some generic professions | Large extra content, mixed cultural assumptions, compatibility cost | Prior-art-only |
| Shavius's Medieval Flavour Pack 2767940226, [same source audit](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/WorkshopBackstoryOriginalsAudit20261016.md) | 27 original 1.6 Western medieval histories, five forced traits, European religious/knight context | Extra independently maintained package | Prior-art-only |
| Medieval Backstories Core & Royalty Overhaul 3809203958, [same source audit](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/WorkshopBackstoryOriginalsAudit20261016.md) | Zero new Defs; text replacements and WTL patch | Would overlap existing 123 Characters rewrites | Prior-art-only |
| Non-VE Medieval Backstories 2794130067 / No HAR 3128454510 | European medieval monks, hunters and general-life identities; not proven to contain the five Japan-specific texts/skill/trait combinations | Extra whole-Mod load, source/1.7 final patches not exhaustively inspected | Prior-art-only |
| VE Vanilla Backstories Expanded 2861806869 | 150+ mixed-theme biographies, including travel/performer/ritual-themed analogs but not verified all same Japanese profiles | Broad VE content, prohibited mandatory AMJ content dependency | VE prior-art-only |

**Independent gameplay need:** new shrine officiant, settlement ritual worker, traveling ritual specialist, itinerant woodenware worker and hunter household childhood represent distinct period-Japanese character origins. Use only Vanilla skills, one existing `Nimble` (melee dodge, **not dance**) and default/female title variants; do not force all shrine workers to share personality. No new historical job system, equipment or special Trait. Reusing entire other packages only for five Defs would import many unrelated histories, dependencies and potential text collisions. This is not a new standalone Mod: the existing Characters owner is already the content home. No copyright material copied.

**Evidence bounds:** Original-game and Workshop source audits are versioned as linked. The external providers' *exact full prose, dependencies, final loaded 1.7 behavior* and combined mod-list patch order are not all individually verified; not inspected is not equivalent to no alternative. Such uncertainty limits third-party compatibility claims. Test new loaded 1.6/1.7 defs, translation, gender title mapping, Nimble assignment and generation before release. No game run or Steam action during this commit.

## 2026-10-20 extension — two approved P3 additions

**Decision:** reuse Characters' original `BackstoryDef` and Vanilla skills for `AMJC_FalconerAdult` and `AMJC_TravelingArtisanChild` rather than adding a separate feature or dependency. Existing approved hunter adult (`SpaceHunter79`), hunter child (`AMJC_HunterFamilyChild`), woodturner adult (`AMJC_ItinerantWoodworkerAdult`), traveling performer, and peddler's child are adjacent but distinct age-slot and skill roles. Falconer emphasizes animal handling over Shooting; the mobile artisan childhood emphasizes childhood Crafting/Social, not an adult woodworker profession.

**Non-VE reference providers:** Original Vanilla/MO, historical Backstories, Shavius Medieval Flavour Pack, non-VE Medieval Backstories and text-rewrite Core & Royalty Overhaul are already compared in the table above. No inspected source establishes both exact Japan-specific occupation/childhood identities. Importing entire packs only for two histories increases content collisions and dependencies. **VE reference:** Vanilla Backstories Expanded adds broad analogues, but the documented existing source comparison does not prove equivalent specific Japanese biographies. No VE or non-VE dependency is introduced; this is not an assertion of comprehensive third-party coverage.

**Era/source limits:** `Docs/Stage3BackgroundGapAnalysis.md` keeps cultural-heritage reference links and identifies Edo-specific evidence that must not be generalized to medieval falconer institutions. Traveling artisans are heterogeneous; the childhood story does not impose hereditary caste or automatic family links. Actual ordinary selection and all third-party collisions remain to be tested; original saves/IDs unchanged.

## 2026-10-20 additional weaving/pottery and fishing-skill comparison

Two author-approved Japanese occupational identities are added as **BackstoryDefs inside Characters**, not a new Mod or custom skill. Genuine Vanilla Core 1.6/1.7 contains craft-related originals but the owner-approved 123 rewritten entries do not already title adult **織物職人** or **焼き物師**; a `窯場育ち` child narrative in Stage2 differs from an experienced adult potter. MO 1.6's optional textile and clay crafting products can use the existing `Crafting` competency. The Potter's `Artistic +2` represents judging form, not a guaranteed MO pottery labor multiplier.

Prior art/dependency comparison already scoped in this file: *VE* Vanilla Backstories Expanded, non-VE Historical Backstories, Shavius, Medieval Backstories No HAR, and Core & Royalty Overhaul provide many general or western occupational biographies. No audited original provider is established to supply exactly the two approved Japanese descriptions/skill profiles; exact complete third-party identity overlap is not proven absent. Importing their entire content for two histories would introduce extra lore and dependencies, whereas two plain XML Defs avoid a new job/tooling framework. Both original MO and Vanilla remain optional; use `Outlander` + `Tribal` + optional `MedievalCommon` without altering FactionDefs.

Historical scope: [Japanese Kogei Association Textiles](https://www.nihonkogeikai.or.jp/en/textiles/) and [Ceramics](https://www.nihonkogeikai.or.jp/en/ceramics/) establish ancient/medieval production; [Kyoto National Museum medieval kilns](https://www.kyohaku.go.jp/old/eng/theme/floor3_1/past/cera_20160621.html) supports everyday vessels, without implying Edo-specific named craft guilds or porcelain. The Japanese copy and skills were accepted before the production edit. No extra dependencies, objects, jobs or trade-item Defs.

Fishing skill question: [Odyssey Fishing Speed](https://rimworldwiki.com/wiki/Fishing_Speed) and [Fishing zone](https://rimworldwiki.com/wiki/Fishing) explicitly derive fishing productivity from `Animals`; non-VE [RF Fishing-ReWork](https://github.com/emipa606/RFFishingReWork) also does, and VE [Vanilla Fishing Expanded](https://rimworld.2game.info/detail.php?id=1914064942) uses Animal Handling. This substantiates an optional **`Animals +5`** adult coastal fisherman concept, *not* adding a Fishing SkillDef or asserting that the job exists without Odyssey/other fishing content. New fisher Def remains absent pending accepted prose and category/specification. No separate salt-worker Def because fishing and historical sea-salt production are distinct from original MO mining salt.

## 2026-10-20 coastal fishing background accepted

**Scope decision:** author-approved Japanese coastal-fishing livelihood plus `Animals +5` implemented in Characters as the independent Def `AMJC_CoastalFisherAdult` with no extra dependencies. Existing 123 revised Vanilla backgrounds include adult *山野の猟師*, but no accepted equivalent of a coastal fisher; the previously approved hunter-family childhood is a distinct age slot. Original Vanilla/MO and prior-art providers already compared above include VE Vanilla Backstories Expanded and non-VE medieval/historical backgrounds; the evidence does **not** prove absence of a similar generic fisherman elsewhere. The independent gap is a concise Japanese coastal fishing background with exact author-approved copy, ordinary Vanilla/MO generation categories, and existing game skill benefits, not a standalone fishing mechanic. A whole third-party background pack would add unrelated histories and dependencies. Optional Odyssey/VFE fishing uses the `Animals` skill; neither is required by this Def. Final specification and Japanese text: [Stage3CoastalFisherDesign.md](Stage3CoastalFisherDesign.md). Production XML and DefInjected are the source of truth, with separate acceptance still needed.


## 2026-10-21 approved coastal salt-maker background — VE/non-VE and source overlap

**Player-facing need:** Ten implemented Stage3 backgrounds included coastal fishing (`AMJC_CoastalFisherAdult`, Animals) but no approved adult sea-salt maker. Original Stage2 rewritten 123 entries do not explicitly title an adult salt worker. Salt production through seawater concentration and heating differs from fishing, pottery, and original MO mined salt. A new `AMJC_SaltMakerAdult` ordinary `BackstoryDef` with the approved Japanese biography addresses that exact Japanese livelihood without introducing any production mechanic. This is not a claim about the complete original 784 Vanilla biographies or every third-party biography.

**Existing alternatives:** The source comparisons above include Vanilla Core and MO, non-VE Historical Backstories, Shavius's Medieval Flavour Pack, Medieval Backstories, and VE Vanilla Backstories Expanded. They are prior art for occupational backstories; those reviewed sources do not establish the particular approved Japanese salt-maker title, prose, and skill pair as an existing Characters-owned Def. Exhaustive absence or final compatibility with all third-party packs is **not** established. Importing full background packs only for this one biography introduces unrelated source content and dependencies; use existing Characters XML and no required VE/MO/DLC dependencies. Original Vanilla `Outlander` / MO `Tribal` candidate routes are consistent with other P3 biographies. `Civil` and optional `MedievalCommon` do not guarantee an actual randomly drawn pawn.

**Historical limits:** The [Japan Heritage Akō salt story](https://japan-heritage.bunka.go.jp/ja/stories/story077/) distinguishes early earthenware boiling from medieval salt fields; the [Salt Industry Center history](https://www.shiojigyo.com/siohyakka/made/history.html) documents the development of salt fields and different boiling vessels. Approved copy describes generic seawater concentration and boiling, not one modern, late-period salt-field or iron-cauldron mechanism universal to ancient/medieval Japan.

**Approved content:** `AMJC_SaltMakerAdult` / 浜の塩焼き / 塩焼き; adulthood; `Crafting +3`, `Cooking +2`; `Outlander`, `Tribal`, `Civil`, `MedievalCommon`; no forced trait, special possession, work restriction, new skill, salt recipe, job or dependency. Canonical `Docs/Design.md` and the product XML control final wording. 1.6/1.7 native acceptance of this **new** ID is not yet established.

## 2026-10-21 漁村育ち — 既存Mod・背景との重複監査

**対象:** 追加する幼少期 `AMJC_FishingVillageChild` は日本沿岸の家庭で漁具の手入れと漁獲物の運搬を手伝った個人の経歴。技能は `Animals +2 / Crafting +1`。成人の既存 `AMJC_CoastalFisherAdult`（Animals+5）とは年齢枠を分け、既存幼少期 `AMJC_HunterFamilyChild`（Shooting+2／Animals+1／Plants+1）とも射撃・山野知識ではなく漁具の扱いを重視する点で区別する。改稿済み123件には `田畑育ち` 等の家業由来の幼少期もあるが、承認済みの「漁村育ち」と同じ題名・技能組合せではない。未改稿のVanilla Def全体から同類の背景が存在しないとの主張ではない。

**参照Modの扱い:** 先行監査に含まれる原本Vanilla/MO、非VEのHistorical Backstories・Shavius Medieval Flavour Pack・Medieval Backstories、VEのVanilla Backstories Expandedはいずれも職歴の先行例。今回の承認済み日本語本文・技能の幼少期１件を得るために外部の大規模背景Modを前提化する必要はない。全第三者Modとの記述の非重複、抽選頻度、競合パッチ不在を証明したものではない。既存Charactersの純XML `BackstoryDef` だけを追加し、釣りの新Job・DLC・MO互換パッチ・特別な家族関係は実装しない。

**技能・生成条件:** `Animals` はOdysseyや釣りModが存在する場合には既存の釣り技能と関係するが、それらのModがなくても普通の動物技能として機能する。漁村出身であることは海岸マップへの限定生成を意味しない。`Outlander / Tribal / Civil / MedievalCommon` は既存のP3幼少期と整合した候補カテゴリであり、自然抽選率の検証ではない。内容の正本は `Docs/Design.md` および日英製品XML。新規Defのネイティブ受入れは保留する。

## 2026-10-21 織屋の子 — Vanilla/MO・VE/非VE比較と差別化

`AMJC_WeaverChild`（`Childhood`、`Crafting +3`）は定住して織物を製作する家の幼少期を描く。既存の成人 `AMJC_TextileWeaverAdult` は専門技術に熟練した成人で `Crafting +6`、既存の `AMJC_TravelingArtisanChild` は移動職人の家で `Crafting +2 / Social +2`。原本改稿123件にも `窯場育ち` など別業種の職人家庭はあるが、同じ表示名・限定的な技能を持つ織物家庭の幼少期は承認済みの正本中に存在しない。原本全784件や第三者の似た幼少期の完全不在は断定しない。

既に確認済みの原本Vanilla/MO、非VEのHistorical Backstories・Shavius' Medieval Flavour Pack・Medieval Backstories、およびVEのVanilla Backstories Expandedは広範な職歴の先行例だが、この日本語の織物家庭という具体的な経歴・年齢・技能値を得るために大規模Mod全体を必須化しない。原本VanillaのOutlanderとMOのTribalの候補カテゴリを含め、任意MedievalCommonにも対応する一件の通常BackstoryDefとする。他Modの歴史背景の抽選頻度・パッチ順・内容競合についての追加保証はない。

歴史資料：[福井県史・中世後期の衣料生産](https://www.library-archives.pref.fukui.lg.jp/fukui/07/kenshi/T2/T2-5-01-01-01-04.htm) は苧麻を含む中世の布生産、[古代日本の紡織体制](https://ndlsearch.ndl.go.jp/books/R000000004-I7201692) は古代の糸巻き・製織に関連する考古資料を扱う。この背景は個人の家業経験であり、近世の木綿の問屋制家内工業や近代工場を想定しない。

決定事項は `AMJC_WeaverChild`、織屋の子、`Crafting +3`、`Outlander/Tribal/Civil/MedievalCommon`、強制Trait・所持品・作業制限・追加Jobなし。製品XMLと [Design.md](Design.md) が正本。実ゲーム読込の検証はまだ行っていない。

## 2026-10-21 既存Core IDへの職業統合（過去の経緯）

**2026-10-28現行：** 重複する新規 `AMJC_WoodcutterAdult`・`AMJC_TextileWeaverAdult` は製品Defおよび翻訳から削除。通常候補の新規12件とCore既存3背景を残す。以下の14件保持・改名・セーブ互換維持は撤回した歴史的議論である。

**過去の比較・候補検討を上書きする確定方針:** Vanilla `Logger16`、`Logger95`、`Weaver63` を歴史的な名称・説明へ英日改稿する。通常生成は「村の杣人」（Logger16: Tribal）、「山の杣人」（Logger95: Outlander等）、「織物職人」（Weaver63: Tribal、必要最小限のOutlander追加）が担当する。既存の技能・作業タグ・強制Trait・初期所持品・IDは原本通り。織物職人を普通のVanilla Outlanderにも供給できるよう原本 `Weaver63.spawnCategories` に **Outlanderのみ**追加する。他の既存カテゴリは保持する。

**重複する新規Defの扱い（2026-10-28更新）：** `AMJC_WoodcutterAdult` と `AMJC_TextileWeaverAdult` は削除せず、`AMJ_CultureExcluded` 1件のみで通常生成から除外する。既存Core職業名との**表示名の重複**を避けるため、追加側の名称・短縮名を「木伐り」／英語 `timber cutter`、および「機織り師」／英語 `handloom weaver`（短縮 `loom weaver`）に改める。新規P3は**14定義中12件**（成人8・幼少4）が通常生成候補。ID・技能・本文・原本135生成制限・既存職業3件・初期所持品23件は不変。公開前のため、この2件を残す理由は旧版セーブ互換性ではない。

**ゲーム上の利害:** 同じ職業が新規DefとVanilla Defの双方から生成される問題は抑える。新規P3を無制限に維持した場合と比べ、`Logger16` のMelee+3、`Logger95` のPlants+8、`Weaver63` のPlants+2が実際の強化として付く。原本にあった木材/布も残る。原本には `PlantWork`／`Crafting` の必須作業タグがある。旧新規Defの `Civil/MedievalCommon` 候補は現状引き継がず、通常VanillaとMOに必要なカテゴリだけを用いるためその候補数は縮む。職業の存在意義を技能セットの変更や新規Jobで無理に作らない。

**根拠と検証:** 現行原本のスロット、技能、カテゴリ、所持品は下表と[Project Actions #38797500765](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/38797500765)（同値1.6/1.7）で確認済み。Vanilla/MOの一般候補カテゴリとの交差も既存[MO Crosswalk](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/MO16BackstoryFilterCrosswalk.md)に準拠。職業の選択確率、ゲームロードされた新しいPatched Def、既存セーブの再読込、ほかのBackstoryModの同名タイトルは未検証。旧14定義での1.7実ゲームPASSは新しい候補カテゴリへ流用しない。製品仕様は `Docs/Design.md` および `Patches/Stage3CoreOccupationRewrites.xml`、日本語DefInjected、`Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` に反映。

## 2026-10-21 原本Vanilla 1.6/1.7の4職業：生成・技能・重複の実データ監査

**重大な訂正／方針判断待ち:** 先行の新規「杣人」「織物職人」の必要性監査は未改稿Vanilla Core背景を調べ切れていなかった。過去の旧英語注記だけではなく、作者所有の**オリジナルCore 1.6.4871 rev598／1.7.4977 rev1248**から作成した784 BackstoryDef+43 TraitDefの `amj-core-character-defs-metadata-v2` で4件の現行Def値を照合した。両版の全CSV SHA-256は**同一 `5699065686d4d6bebd59a8244b88a4f5707c57a0d16b0300cadab09ef331228d`**。Project [原本の完全性監査・Actions #38797500765](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/38797500765)、保存Artifact **`vanilla-core-character-defs-16-17-38797500765` ID `12002927488`**、および[Project原本調査](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/VanillaCoreCharacterDefsSourceAudit20261016.md)。先行した古い原文内容については[Ludeon公式翻訳リポの英語注記](https://github.com/Ludeon/RimWorld-Finnish/blob/master/Backstories/Backstories.xml)。現行ゲーム版の4行は**全フィールドで1.6/1.7一致**する。

| 現行Core `BackstoryDef` | Slot | `skillGains` | `spawnCategories`（完全リスト） | `requiredWorkTags` | `forcedTraits` | 初期所持品 |
|---|---|---|---|---|---|---|
| `Logger16`（伐採） | Adulthood | `Plants +6; Melee +3` | `Tribal; TribalLogger` | `PlantWork` | なし | `WoodLog ×10` |
| `Logger95`（伐採） | Adulthood | `Plants +8` | `Offworld; Outlander; Pirate; Scientist; Logger` | `PlantWork` | なし | `WoodLog ×10` |
| `PlankCutter72`（板材加工） | Adulthood | `Plants +6; Melee +3` | `Tribal; TribalLogger` | `PlantWork` | なし | なし |
| `Weaver63`（織物） | Adulthood | `Crafting +6; Plants +2` | `Tribal` | `Crafting` | なし | `Cloth ×10` |

原本対応ファイルは `BackstoryDefs/Shuffled/Tribal_Adult.xml`（Logger16 / PlankCutter72 / Weaver63、SHA-256 `2e12b1429a12238e57d99d1d1e1e5cb6d23586053f32666d6b19e7bef53f9926`）と `BackstoryDefs/Shuffled/Offworld_Nonspecific_Adult.xml`（Logger95、SHA-256 `d28af7623f20b2eeadf69080919d488aa8fa9e889f9e4701647ecfe568c03520`）。4件はいずれも `Shuffled` の実原Defで、固有ポーン専用の `Solid` ではなく、現行Charactersの歴史改稿・生成制限パッチには列挙されない。

### 新規P3との実際のゲーム上の差

| 新規P3 `BackstoryDef` | 既存Coreとの比較 | 判断材料 |
|---|---|---|
| `AMJC_WoodcutterAdult`「杣人」 | `Plants +6` だけ。候補 `Outlander / Tribal / Civil / MedievalCommon`、強制Trait・専用アイテム・`requiredWorkTags`なし | 既存の `Logger16` は同じPlants+6にMelee+3・木材10を加える。 `Logger95` はPlants+8・木材10。**OutlanderとTribal両経路に既存伐採背景がある**ため「伐採役が存在しない」は誤り。日本語の杣人名・4カテゴリの広さは差分 |
| `AMJC_TextileWeaverAdult`「織物職人」 | `Crafting +6` のみ。候補 `Outlander / Tribal / Civil / MedievalCommon`、初期布なし、`requiredWorkTags`なし | `Weaver63` はCrafting+6にPlants+2・布10を加え、`Tribal` に存在。新規背景はVanilla `Outlander` 等への生成カテゴリ拡大と和文が差分。**Tribal内では職業が重複** |
| `AMJC_ItinerantWoodworkerAdult`「木地師」 | `Crafting +5 / Plants +2`、木の器・道具を作る職人 | `PlankCutter72` は板材加工、`Logger16/95` は伐採。**この3者は直接同じ加工物・技能構成とは限らない**。木地師まで同時に廃止する根拠とはしない |

原本の `spawnCategories` とProject [MO 1.6 Tribal faction/PawnKindフィルタ照合](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/MO16BackstoryFilterCrosswalk.md)から、Logger16・PlankCutter72・Weaver63はMOの `Tribal` 候補カテゴリ、Logger95はVanilla `Outlander` 候補カテゴリと**文字列上は交差**する。ただし `requiredWorkTags` とPawn側の仕事条件等の追加選考を経るため、これだけで特定Defが抽選された事実、遭遇頻度、通常出現保証とはならない。

**関連する別の確定事実:** 背景Phase2で「田畑育ち」と改稿済みの `ArtisanFarmer23` は原本 `Solid_Child`、`spawnCategories=Farmer` のみ、`Plants+7 / Intellectual−2 / Cooking+2`、Violent作業不可（原本実データ）。`Outlander`／`Tribal` という通常のカテゴリー名は持たない。これも「荘園の農家の子」新規Defを無条件で正当化しないが、以前の「田畑育ち」の存在のみから一般的な抽選適格性を推定できないことを裏づける。

### 旧解決候補と意思決定境界（現在は解決済み）

**推奨:** 重複を減らすことを優先するなら、**既存原本IDを保持して英日本文・表示名だけ歴史的な職名へ改稿し、元の技能・生成カテゴリ・必要作業タグ・初期所持品を維持する方式**を先に評価する。候補は `Logger16/Logger95` を「杣人」系、`Weaver63` を「織物職人」系にする方法。ただしこれだけでは新規P3が広げた `Outlander/Civil/MedievalCommon` の同一カテゴリ機会をすべて代替できず、既存CoreのPlankCutterは加工職である。

**代替案:** 新規Defを維持しつつ、重複するカテゴリだけ抑制する（例：杣人新規DefのOutlander/Tribal、織物職人新規DefのTribal）ことで独自の職業出現機会を残す。この案は、いずれも**現在の承認済み新規14件の生成仕様を変更**し、追加済みの新規Def名を存続させるため、作者承認なしには実装しない。自然生成分布への影響は予測できても実測未実施。

**実装保留:** 14件目までの新規製品Def/元Core Def/技能は変更しない。新規P3を削除・置換すると、そのIDを参照した既存のPawn・セーブに影響し得る。実際にSteam公開されたという証拠はなくても利用中のローカルセーブは保証できない。**統合・削除・技能／生成カテゴリ変更は作者の方針判断待ち**。1.7日本語の14件ロードテストPASSは継続して有効だが、独立職業の必要性を証明しない。追加実ゲームテストは起動しない。

## 2026-10-21 杣人 — 既存背景・VE/非VE代替の境界

**不足職業と重複監査:** `AMJC_WoodcutterAdult` は山林で建築用の木を見極めて伐採・運び出す成人背景。既存P3 `AMJC_ItinerantWoodworkerAdult`（木地師）は木の器や道具の加工（`Crafting +5 / Plants +2`）、改稿済み `SpaceHunter79`（山野の猟師）は獣の狩猟、`FurnitureBuilder83`（山里の大工）は建築・木材加工を描く。当時の監査は123改稿タイトル・先行新規13件に限定され、未改稿原本Logger16/Logger95を見落としていた。**この段落の旧「単純重複ではない」という判断は、上記2026-10-21の1.6/1.7原本データ監査により撤回する。**

**Vanilla・MO、VEと非VE:** 既存の根拠資料・比較先は原本Vanilla/MO、VE `Vanilla Backstories Expanded`、非VEの `Historical Backstories`、`Shavius's Medieval Flavour Pack`、`Medieval Backstories` 等。職人・木こりの汎用的な人物背景に類似例があっても、既存Charactersが所有する日本の杣人として、史実に沿う名前・確定済み本文と `Plants +6` を一件の通常BackstoryDefで表せる。大規模背景Modを依存化する必要はなく、新しい伐採Job／伐採効果／スキル／独自資材は追加しない。第三者との完全なテキスト・抽選経路・パッチ互換検証は範囲外。

**歴史上の根拠:** [山川『日本史小辞典』・杣](https://www.historist.jp/word_j_so/entry/033959/) は杣山の用材採取・杣工を扱う。[平凡社『世界大百科事典』・杣工](https://kotobank.jp/word/%E6%9D%A3%E5%B7%A5-1181372) は古代・中世の伐木と造材を担った人々を説明する。[國學院大學万葉神事語辞典「そま」](https://jmapps.ne.jp/kokugakuin/det.html?data_id=32080) は建設用の木材を切り出す職として古代に用例を挙げる。特定の時代の寺社・荘園への帰属を全ポーンに強制しない。

**決定:** `AMJC_WoodcutterAdult`、表示名「杣人」、成人、`Plants +6` のみ、候補カテゴリ `Outlander/Tribal/Civil/MedievalCommon`、強制Trait／仕事禁止／初期所持品なし。ゲームでは `Plants` の伐採・栽培等への汎用効果があるが、物流・伐採専用能力を増やさない。正本は製品XMLと `Docs/Design.md`。新規14件目の**1.7日本語VanillaでのLoadedDef受入はProject Actions #39582470340でPASS**だが、特定背景の自然抽選や1.6 MOは未検証。現行原本伐採職との重複を解消する製品改変は未承認。
