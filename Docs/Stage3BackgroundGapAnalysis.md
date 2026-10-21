# Stage 3 — historical background diversity and replacement-gap assessment

**Latest (2026-10-20):** five earlier biographies **plus the now-approved 鷹匠 and 渡り職人の子** are present in production XML. Earlier unapproved-candidate descriptions below are superseded only for those two. Seven new Defs total; the last two passed source-pinned loaded-game acceptance in original 1.6 MO and 1.7 Vanilla **English** profiles (see [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md)); actual individual random selection and Japanese appearance remain unverified.

**Status:** five user-continued original backgrounds are in product XML and passed focused original 1.6 Japanese and 1.7 English loaded-game checks on 2026-10-20 ([native acceptance record](Stage3NativeAcceptance.md)); Steam and MO/new-save distribution remain unverified. Other candidates in this inventory are proposals only. Date: 2026-10-19. Owner: AMJ Culture – Characters. This is the first Stage 3 comparison against currently owned approved textual rewrites, not an exhaustive audit of 784 original Vanilla biographies. Do not infer that all 135 excluded backgrounds would otherwise spawn in the author's actual MO world, or that all 123 rewrites are ordinary-generation-eligible.

**2026-10-20 generation eligibility correction:** all seven implemented P3 BackstoryDefs now add `Outlander` in addition to their existing categories, because original Vanilla source has `Outlander` in 122 biographies but `Civil` in just one and `Traveler` in none. MO original `Tribal` routes stay intact. Source-category improvement is **not** proof of natural random appearance. Canonical details in [Design.md](Design.md).

**2026-10-20 two more approved adults:** 織物職人 (`Crafting +6`) and 焼き物師 (`Crafting +4`, `Artistic +2`) are now in the production XML and Japanese DefInjected. They extend the seven earlier backgrounds to **nine**; real-game acceptance and natural distribution are still OPEN. The older pending-candidate rows below are historical planning notes, not their current status. Coastal fishing is still a candidate with `Animals +5` justified by Odyssey/VFE fishing productivity, but no final Japanese text/Def. Salt worker remains pending.

**2026-10-21 approved salt-maker follow-on:** `AMJC_SaltMakerAdult` (浜の塩焼き) is now the 11th implemented P3 biography (adult nine, childhood two), with `Crafting +3`, `Cooking +2`, four ordinary candidate categories and no forced Trait. The older pending `製塩の働き手` row is preserved as the historical candidate context, not an open implementation item. Canonical specification: `Docs/Design.md` and product XML. Earlier ten-Def original-game PASS does not include this 11th Def. **No automatic native test.**

**2026-10-21 承認済み漁村育ち:** `AMJC_FishingVillageChild` は新規12件目（成人9件、幼少期3件）として製品XML・日本語翻訳に実装。`Animals +2`・`Crafting +1`、`Outlander / Tribal / Civil / MedievalCommon`、強制Traitなし。以前の候補一覧「漁村育ち」は現在は未承認候補ではなく実装済み。確定仕様は `Docs/Design.md` を参照。11件目「浜の塩焼き」とともに実ゲーム未検証、既存10件のPASSは流用しない。残る新規背景候補は別途個別の重複・承認審査を要する。

**2026-10-21 織屋の子の実装:** 候補欄「織屋の子」は新規 `AMJC_WeaverChild`（`Childhood`、`Crafting +3`）として製品英語Def・日本語DefInjectedへ反映。新規P3は13件（成人9・幼少期4）。定住の織物家庭での成長であり、成人織物職人や移動する職人の子と異なる。具体的な本文と4カテゴリは `Docs/Design.md`。表の過去の候補行は検討履歴であり、現在の未実装候補ではない。前の10件の1.6/1.7ネイティブPASSは新規3件（製塩・漁村・織屋）を証明しない。新規Defの実ゲーム検証は最後にまとめる。

## Verified baseline and method

- Original Core 1.6/1.7 metadata screen: **784** Vanilla BackstoryDefs and **43** Vanilla TraitDefs (owner `Docs/Data/VanillaMOBackgroundTraitStage1Screen.csv`, Project primary metadata audit); MO adds two separate TraitDefs in the audited package, not additional BackstoryDefs in its audited 1.6 files.
- Current owner **ordinary-generation restrictions**: **77 adulthood**, **58 childhood** = **135** original background IDs restricted. This is *not* permanent removal: saved/explicit backstory IDs are retained.
- Current approved **historical rewrites**: **89** BackstoryDefs in `Docs/Stage2JapaneseReviewDraft.md` and **34** in `Languages/Japanese/DefInjected/BackstoryDef/HistoricalOccupationBackstories.xml`. Distinct-ID comparison: **89 + 34 = 123 with no overlap**. All rewrite IDs are *existing* Vanilla IDs; no newly added Japanese backgrounds.
- Counts are not interchangeable: 135 is the count of restricted ordinary-generation routes; 123 is the count of rewritten biographies, and not a set of replacement Defs. Neither `784−135` nor `123+135` is a valid estimate of actually selectable backgrounds in any particular Faction/PawnKind.
- Evaluation of *actual* remaining diversity requires a source-resolved crosswalk by child/adult `slot`, faction categories, available ordinary generations, `skillGains`, disabled/required work tags, forced/disallowed traits, original possessions and historical title, followed by a small native sample only after the approved implementation. An observed shortfall in one thematic occupation should not be fixed through a generic random-chance weight without reviewing eligible background routes.

## Already represented in the 123 approved rewrites: avoid duplicates

| Theme | Confirmed current titles (examples; not an exhaustive category total) | Implication |
|---|---|---|
| Warfare, security and soldiery | 足軽頭, 古参の足軽, 歴戦の武士, 武将, 城番, 兵法家, 武具職人, 水軍の船大将 | Do not add generic 'samurai'/'ashigaru' solely to replace excluded SF soldiers |
| Medicine and religious care | 医僧, 医家育ち, 医術の大家, 村の世話役, 薬師, 水軍の療治役 | Preserve distinct period medical careers without duplicating labels |
| Construction, mining and crafts | 熟練の大工, 番匠, 石工, 鉱夫, 鍛冶職人, 仏師 | Additional generic 'craftsman' is not a demonstrated coverage gap |
| Traders, accounting and estate officials | 廻船商人, 市の商人, 荘園の書記, 荘園の勘定役, 荘園の差配人 | Differentiate occupations through actual daily activities and retained skill balance |
| Food preparation and temple instruction | 館の料理人, 船中の炊事役, 陣中の膳夫, 寺の学僧 | Cooking and Buddhist temple scholars already represented; they do not replace shrine officiants |
| Shrine ceremonies and ritual | 神事見習いの子 (ApprenticeOracle83, childhood) | A shrine child already exists; no specifically titled adult shrine officiant among the 123 rewritten titles |
| Hunting and itinerant livelihoods | 山野の猟師 (SpaceHunter79), 旅芸人, 流れ者, 行商の子 | Existing ordinary hunter and travelers; new additions must have distinct roles or age slots |
| Farming-related or rural childhood | 田畑育ち, 田畑の知恵者, 山里の暮らし | Some rural coverage exists; a new agriculture entry must represent a distinct social/work role |

**Names in this table are actual approved titles, not invented existing Defs.** The 123-entry source inventory is the deduplication guard for new titles and role concepts. There are also unchanged Vanilla biographies and MO gameplay-related traits outside this set; never claim thematic absence from all installed Defs without an actual loaded inventory.

## Author-prioritized P3 themes (2026-10-19): shrine, itinerant livelihoods and hunting

The author explicitly requests representation of 神道・神社祭祀関係者, 漂泊の民 and 狩人. This is **approval to prioritize thematic coverage**, not approval of individual final biographies, skills, generation rates or a number of new Defs. The current 123 approved rewrites already include original childhood ApprenticeOracle83 = 神事見習いの子, adult SpaceHunter79 = 山野の猟師, RunawayDancer35 = 旅芸人 and other itinerant/merchant characters. This **does not** establish that these subjects are absent from every unrewritten Vanilla or MO background.

**Historical boundaries:** A shrine specialist may be a 禰宜/祝 with responsibilities in local offerings and ceremonies; do not project modern centralized shrine systems onto ancient/medieval history, or imply shrine practitioners never interacted with Buddhism. A shrine-service 巫女 and a mobile 渡り巫女 represent different livelihoods. 漂泊の民 is **not one occupation or one homogeneous ethnic/social group**; specify the actual livelihood rather than portraying all itinerants as thieves, outcasts, or fantasy nomads. Mobile woodenware workers (木地師/木地屋) are a researched example, though period-specific naming needs review. Hunting was a livelihood and material source; 山立 is a documented historic term, whereas マタギ is regionally contextual. Do not conflate practical hunting with elite 鷹狩 or automatically label it as entertainment.

| Priority | Slot | Distinct candidate role | Main content difference from the 123 rewrites | Possible Vanilla skill focus (NOT final values) |
|---|---|---|---|---|
| High | Adult | 社の禰宜・祝 | Shrine ceremony and community service; distinct from 寺の学僧 and the child shrine novice | Social, Intellectual |
| High | Adult | 社に仕える巫女 | Local festival rites and kagura; dance has no Vanilla skill. One **tentative** existing `Nimble` degree 0 forced-Trait match expresses bodily agility but its actual effect is **melee dodge**, not dancing. | Social (visitor contact only) |
| High | Adult | 渡り巫女 | Itinerant rites at festivals and markets: shrine and traveling roles; no dance stat | Social (itinerant contacts only) |
| High | Adult | 木地師（山を渡る木工職人） | Moves in search of suitable wood to make utensils; not settled carpenter or generic wanderer | Crafting, Plants |
| High | Child | 狩人の家の子 | Learns tracking and snares; different age slot from existing adult 山野の猟師 | Plants, Animals, modest Shooting |
| Medium | Adult | 鷹匠 | Specialist in bird-assisted hunts; distinct from everyday subsistence hunter | Animals, Shooting |
| Medium | Child | 漂泊する職人の子 | Grows up with a mobile working household, not simply a one-time fugitive | Crafting, Social |

**Japanese-first narrative sketches — candidates only, not accepted game text:**
- Shrine adulthood: 社の祭礼と供え物を取り仕切り、村人と相談しながら神事を続けた。
- Itinerant craft adulthood: 良い木を求めて各地の山に入り、椀や器を作って暮らした。
- Hunter childhood: 山の獣道を覚え、罠の手入れや獲物の運搬を手伝って育った。

**Overlap / scope gate:** Do **not** add another unqualified adult 狩人 because 山野の猟師 already fills it; do not add another generic shrine child because 神事見習いの子 already fills it. Traveling artisan, pilgrim, miko, troupe member, hunter and trader are not interchangeable histories. An extra ritual mechanic, Ideology DLC dependence, hunting/fishing jobs, altered psychic/fantasy beliefs, new TraitDefs, or special restrictive caste system is outside this background-candidate slice. Before production, compare available Vanilla/MO and VE/non-VE background Mods and verify era-specific roles, skills, slot, generation filters and author-approved Japanese prose.

**Historical reference anchors:** [神職（マイペディア）](https://kotobank.jp/word/神職-81980); [巫女（ジャパンサーチ）](https://jpsearch.go.jp/gallery/ndl-dKYRDz2Z2Yx); [木地屋研究（CiNii）](https://ci.nii.ac.jp/ncid/BN09021209); [狩猟習俗（文化庁）](https://online.bunka.go.jp/heritages/detail/203533); [狩猟と権力（書誌）](https://www.unp.or.jp/ISBN/ISBN978-4-8158-1106-8.html). They provide historically grounded *possibilities*, not a universal timeline or gameplay implementation proof.

**2026-10-20 implementation update:** The five approved P3 additions are now defined in `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` and Japanese DefInjected, while the remaining broad candidate list below is NOT implemented. The two miko profiles have general nonfemale titles and female-title overrides, and only the shrine ritual attendant forces existing Nimble; no dance skill. Native generated-pawn/game acceptance remains open.

**Actual five-Def product source / previously provisional Japanese prose and skill numbers:** [Stage3BackgroundDrafts.md](Stage3BackgroundDrafts.md), five author-prioritized core candidates, **no approved new Def or gameplay change**. **2026-10-19 correction:** base-game Artistic is visual-making (such as sculpture), not kagura/dance. Withdrawn from both miko proposals; Shrine miko Social +4 only, itinerant miko Social +5 only. Dancing remains narrative. Older broad list below is thematic only.

## Stage 3 priority candidates — new Defs not yet approved

These are bounded candidate roles, **not final approved biography titles, histories, social prevalence or numeric traits**. They prioritize clear work/biome niches absent as explicit *specialist titles* from the 123 inspected rewrites. Each proposed new Def must have a unique `AMJC_*` ID, a definite slot, compatible spawn categories, historically plausible narrative, and a skills/work restriction contract accepted before production.

| Priority | Slot | Candidate identity | Why it adds variety beyond the 123 | Tentative gameplay niche, not yet numeric |
|---|---|---|---|---|
| High | Adult | 沿岸の漁師 | Hunting title exists; **fishing-specific** work life is not explicit | Food supply, watercraft, survival; do not assert a fishing skill exists in Vanilla |
| High | Adult | 製塩の働き手 | Coastal salt production is distinct from coastal trading | Manual labor, cooking/material processing, coastal livelihood |
| High | Adult | 織物職人 | Metalwork, carpentry, art exist; textile production is not an explicit specialist title | Crafting and production, not blanket combat restrictions |
| High | Adult | 焼き物師 | Stone construction and weapon forging do not represent pottery | Crafting, kiln/fuel work, trade |
| Medium | Adult | 山仕事の担い手 | Mountain childhood/hunters exist but forest resource harvesting is different | Plants, logging, hauling; avoid duplicating the existing hunter |
| Medium | Child | 漁村育ち | Existing coastal smuggling/orphan/ship titles differ from ordinary fishing-village household work | Seasonal food work and shore knowledge, without adult mastery |
| Medium | Child | 織屋の子 | Existing workshops/kitchens/blacksmith childhoods differ from textile household work | Small skill familiarity in craft and household work |
| Medium | Child | 荘園の農家の子 | 田畑育ち already exists; use only if the exact family obligation/seasonal labor provides a distinct gameplay/effects role | Plants, hauling, household work; risk of duplication is high |

**Explicit overlap gate:** `荘園の農家の子` is a *conditional* candidate because `田畑育ち` is present. Do not implement it without proving different role and skill profile. Similarly no new generic swordsman, doctor, trader, monk, scholar, carpenter or merchant by default.

## Proposed implementation sequence and protection

1. Read source-resolved real 1.6 and 1.7 Core biography attributes / generation routes already indexed by the Project. Derive a **separate** baseline by adult vs childhood and ordinary PawnKind/faction relevance; do not treat archival screening tags as gameplay eligibility.
2. For each high-priority candidate, compare gameplay skill role, any MO opportunities and existing Vanilla/MO/other medieval-background mods, including both VE and non-VE alternatives per Project ExistingModAudit implementation entry gate. An already-covered work role may need no new Def.
3. Present a short **Japanese-first** description, distinct role, plausible applicable date range, intended spawn categories, skills/work and sensible weighting; obtain author approval before generating the new Def, translating it and assigning automatic appearance. The final author-approved text lives in Characters production XML / Japanese DefInjected, not only here.
4. Batch only accepted non-overlapping candidates into new BackstoryDefs under Characters ownership. Preserve the 135 exclusions and 123 revised originals; do not reopen their Def IDs, descriptions or numeric work attributes. Keep new TraitDefs and background forced traits as separate approval decisions.
5. Run one consolidated original loaded-game acceptance for added backgrounds and P2 corrections near the feature slice's completion. Do not automatically launch a game or multiply CI matrices; review generated-Pawn distribution across normal Vanilla/MO routes before claiming diversity improved.

**Not done:** No candidate has an author-approved bio, skill profile or spawn weight; no additional BackstoryDef is currently implemented. The 135 restriction/123 rewrite numbers are verified owner scope totals, not measured diversity/distribution.

## 2026-10-20 follow-on candidate review — 鷹匠 and 渡り職人の子 (not implemented)

**Status: editorial/gameplay proposals ONLY.** The five previously approved P3 BackstoryDefs have already been implemented and accepted in scoped original-game profiles. This section does not authorize new BackstoryDefs, Japanese DefInjected, gameplay XML, random-selection rate changes or a test run. Final Japanese wording, skills and spawn-category applicability require author content judgment; they must not be silently promoted from this review into the production files. No existing 135 restrictions / 123 rewrites / five P3 additions are altered.

### Candidate A — 鷹匠 (falconer, adulthood)

- **Proposed DefName:** `AMJC_FalconerAdult`; `Adulthood`.
- **Japanese title / short title draft:** 鷹匠 / 鷹匠. English *falconer*.
- **Japanese description draft:** `[PAWN_nameDef]は鷹を捕らえて飼い慣らし、獲物を追わせる技を身につけた。鳥の体調や動きを見ながら訓練を重ね、鷹狩の支度と手入れを任されてきた。`
- **Candidate skill gains:** `Animals +5`, `Plants +1` (total +6). `Animals` models animal handling and trained-hawk upkeep. The smaller Plants bonus represents outdoor knowledge, but **could be dropped** if judged too indirect. **No automatic Shooting bonus**: falconry is not personal archery and RimWorld has no innate falconry hunting job. No forced trait, special animal companion, bonded hawk, starting pet or DLC dependency.
- **Overlap:** differs mechanically from original adult 山野の猟師 (`SpaceHunter79`) and newly added hunter-household childhood by relying on `Animals` rather than archery. Distinct from generic `DankPyon_Fighter`/`DankPyon_Veteran` and existing animal-training Traits. Do not grant a unique falconry ability that does not exist.
- **Eligibility proposal, not a finalized filter:** `Civil`, `Tribal`, optional `MedievalCommon` are possible source-era labels, but exact original MO/VANILLA pawnkind intersections and frequency require evaluation **before** addition. Noble-service context must not imply every small village has an elite court falconer. Restricting the entire biography to upper class would require an actual available generation mechanism, not a prose claim.
- **Historical bounds:** the cultural heritage register recognizes hawking as an early imported court hunting practice cited in the *Nihon Shoki*, with historically varied aristocratic/warrior and regional uses; Tokyo National Museum's surviving **Edo-period** `鷹匠心得の巻` cannot itself verify particular medieval techniques or high-ranking official positions. The profile is a general experienced bird trainer, not a universal Sengoku daimyō retainer. References: [Agency for Cultural Affairs — 狩猟習俗](https://kunishitei.bunka.go.jp/bsys/maindetails/312/168); [Tokyo National Museum material via Cultural Heritage Online — 鷹匠心得の巻](https://online.bunka.go.jp/heritages/detail/445727).

### Candidate B — 渡り職人の子 (mobile artisan household, childhood)

- **Proposed DefName:** `AMJC_TravelingArtisanChild`; `Childhood`.
- **Japanese title / short title draft:** 渡り職人の子 / 職人の子. English *traveling artisan's child*.
- **Japanese description draft:** `[PAWN_nameDef]は道具を持って土地を移る職人の家に育ち、各地で仕事をする家族を手伝ってきた。材料や道具の扱いを覚え、旅先で客や土地の人々と接することにも慣れていった。`
- **Candidate skill gains:** `Crafting +2`, `Social +2` (total +4); deliberately small childhood advantages for basic handwork and varied customer contact, **not** adult-level `Crafting +5`, building, caravan speed or a new trade job. No forced Trait, work disable, special starting possession or fixed family/faction relation.
- **Overlap:** distinct in age slot from `AMJC_ItinerantWoodworkerAdult` (adult 木地師). Unlike the already rewritten traveling performer / peddler's child / forge-raised child, the livelihood is **mobile practical manufacture**, not stage performance, commerce alone or a fixed forge. Does not assert that all mobile craftsmen were woodworkers, persecuted outcasts or a single hereditary group.
- **Eligibility proposal:** `Tribal`, `Traveler`, optional `MedievalCommon`, possibly `Civil` only if actual base-game category selection warrants it; no spawn weight or category XML is accepted. The child may be selected independently of the adult family history under existing RimWorld generation; do not imply the game automatically creates matched families.
- **Historical bounds:** the cultural heritage register describes mobile woodenware maker/ladle maker communities; that **evidence is about a particular craft tradition**, not proof that all medieval itinerant crafts shared one institution. A historical dictionary distinguishes medieval `轆轤師` from the later common `木地屋` name. This generic childhood biography is an abstraction of a craft household moving for work, not a claim of one universal mobile population. References: [Agency for Cultural Affairs — 木地屋の生活伝承](https://kunishitei.bunka.go.jp/heritage/detail/312/165); [Yamakawa history dictionary via Kotobank — 木地師](https://kotobank.jp/word/%E6%9C%A8%E5%9C%B0%E5%B8%AB-473503).

**2026-10-20 approval supersedes candidate status:** the author approved **both** proposed biographies, their previously displayed Japanese descriptions and exact skill gains. They are now implemented in the existing P3 production XML and Japanese DefInjected. See `Docs/Design.md` for the final active specification. The candidate discussion above is retained as historical reasoning, not an open approval question. Loaded original 1.6 MO and 1.7 Vanilla acceptance is PASS for both additional histories; actual appearance in random generation, Japanese display for these two and save migration remain OPEN. See [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md).

