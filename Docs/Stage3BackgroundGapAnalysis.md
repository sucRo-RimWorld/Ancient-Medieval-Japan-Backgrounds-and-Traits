# Stage 3 — historical background diversity and replacement-gap assessment

**Status:** proposal / candidate inventory, not author-approved new BackstoryDefs or runtime gameplay. Date: 2026-10-19. Owner: AMJ Culture – Characters. This is the first Stage 3 comparison against currently owned approved textual rewrites, not an exhaustive audit of 784 original Vanilla biographies. Do not infer that all 135 excluded backgrounds would otherwise spawn in the author's actual MO world, or that all 123 rewrites are ordinary-generation-eligible.

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
| Food preparation and temple instruction | 館の料理人, 船中の炊事役, 陣中の膳夫, 寺の学僧, 神事見習いの子 | Generic cook/temple apprentice is already represented |
| Farming-related or rural childhood | 田畑育ち, 田畑の知恵者, 山里の暮らし | Some rural coverage exists; a new agriculture entry must represent a distinct social/work role |

**Names in this table are actual approved titles, not invented existing Defs.** The 123-entry source inventory is the deduplication guard for new titles and role concepts. There are also unchanged Vanilla biographies and MO gameplay-related traits outside this set; never claim thematic absence from all installed Defs without an actual loaded inventory.

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
