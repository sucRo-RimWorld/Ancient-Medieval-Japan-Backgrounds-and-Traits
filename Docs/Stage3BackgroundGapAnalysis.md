# Stage 3 — historical background diversity and replacement-gap assessment

**Status:** five user-continued original backgrounds are in product XML and passed focused original 1.6 Japanese and 1.7 English loaded-game checks on 2026-10-20 ([native acceptance record](Stage3NativeAcceptance.md)); Steam and MO/new-save distribution remain unverified. Other candidates in this inventory are proposals only. Date: 2026-10-19. Owner: AMJ Culture – Characters. This is the first Stage 3 comparison against currently owned approved textual rewrites, not an exhaustive audit of 784 original Vanilla biographies. Do not infer that all 135 excluded backgrounds would otherwise spawn in the author's actual MO world, or that all 123 rewrites are ordinary-generation-eligible.

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
