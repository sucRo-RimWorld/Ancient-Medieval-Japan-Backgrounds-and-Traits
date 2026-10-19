# P3 — shrine, itinerant and hunting biography proposals (2026-10-19)

**STATUS UPDATE (2026-10-20): THE FIVE PROPOSED BACKSTORIES ARE NOW IN PRODUCTION XML SOURCE FOLLOWING AUTHOR CONTINUATION.** See `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` and `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`. This record describes their earlier review; actual current source owns approved bilingual gameplay text/numeric values. Scoped original 1.6 Japanese and 1.7 English game-loaded verification is now PASS for the checks listed in [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md); MO and historical save reload remain untested. Earlier note for historical context: Five biographies, Japanese translations and the one Nimble link are now implemented in the production XML after author continuation; this prior candidate record remains for rationale. Native 1.6/1.7 generation and Steam publication remain unapproved/unverified. Canonical Stage 3 gap / overlap record: [Stage3BackgroundGapAnalysis.md](Stage3BackgroundGapAnalysis.md).

## Existing content and feasibility constraints

- Among the already approved 123 rewritten original biographies, `ApprenticeOracle83` = **神事見習いの子** (childhood), `SpaceHunter79` = **山野の猟師** (adulthood), `RunawayDancer35` = **旅芸人**, plus other traveling persons and tradespeople. These remain untouched. A generic second shrine child, adult hunter or generic itinerant person is redundant.
- **Existing-Mod comparison scope (read-only):** Project's original Vanilla Core 1.6/1.7 metadata survey (784 original `BackstoryDef`, 43 traits); original Medieval Overhaul 1.6.2.2 (no extra `BackstoryDef` in audited files); [Medieval Backstories No HAR](https://steamcommunity.com/workshop/filedetails/?id=3128454510) and [Medieval Backstories](https://steamcommunity.com/sharedfiles/filedetails/?id=2794130067), offering European medieval monks/seers/hunters and many generic period vocations; original [Shavius's Medieval Flavour Pack](https://steamcommunity.com/sharedfiles/filedetails/?id=2767940226) and [Historical Backstories](https://steamcommunity.com/sharedfiles/filedetails/?id=3611930252) metadata audited by Project; VE [Vanilla Backstories Expanded](https://steamcommunity.com/workshop/filedetails/?id=2861806869) offers 150+ mixed-theme biographies (incl. Oracle, Troupe Child, Traveling Locksmith). These are **prior art**. No audited provider is proven to provide all five *precisely specified Japanese* occupations with acceptable whole-Mod content/load costs. No newly downloaded raw provider source or final load behavior audit in this step. The bounded source comparison and limitations are recorded in [Stage3ExistingModAudit.md](Stage3ExistingModAudit.md). No external dependency was added.
- The original MO 1.6.2.2 faction/pawnkind crosswalk (Project `Docs/Research/MO16BackstoryFilterCrosswalk.md`) confirms `Tribal` in several original player and medieval faction/PawnKind selectors. Optional **Medieval Backstories Patch** can replace both sides with `Medieval`, `MedievalCommon`, `MedievalKnight` categories. **Candidate eligibility**: `Tribal` as original MO baseline, with optional `MedievalCommon` considered for the mod-patched configuration; these are *not finalized `spawnCategories`* because Vanilla/Core, MO, World Tech Level and other category filters require a resolved intersection. In particular do not automatically choose `MedievalKnight`, `Pirate`, `Offworld` for a village shrine or ordinary hunting household.
- The only skills used as actual draft bonuses are existing Vanilla `SkillDef` names: `Social`, `Intellectual`, `Crafting`, `Plants`, `Shooting`, `Animals`. **Do not treat `Artistic` as dancing, kagura or performing-arts proficiency:** it principally affects visual creative work such as sculptures in base RimWorld. No special `Dance`, `Performance`, `Ritual`, `Shinto`, `Fishing`, tracking or hunting skill exists in the current draft. `skillGains` are design numbers **added to** normal pawn skills, not Pawn final levels and not random passions.
- **One source-implemented forced Vanilla trait only:** the shrine ritual attendant carries `Nimble` degree `0`, as a game abstraction of physically practiced kagura movement; this **does not create a Dance skill**. `Nimble` alters actual **melee dodge** (not dance), so the gameplay side effect must be disclosed. **The other four new biographies have no forced traits.** None has disallowed traits, work disables, required work tags, starting possessions, psychic or Ideology-linked effects. Avoid assuming all historical shrine women had Nimble; this is a specific proposed backstory, not a general rule. Existing save and old Def IDs remain unchanged. The five new Defs are XML-only; existing DLLs were not rebuilt.

## Five initial profiles

### 1. 社の神職 — adult, shrine officiant (local 禰宜・祝)

- **Implemented ID:** `AMJC_ShrineOfficiantAdult`; slot: `Adulthood`.
- **title:** 社の神職 / **titleShort:** 神職.
- **description (proposal, Japanese):** [PAWN_nameDef]は社の祭礼や供え物を取り仕切り、村人の願いや相談を聞きながら神事を務めてきた。社の由緒や作法にも通じ、祭りの準備では周囲の人々をまとめていた。
- **skills:** `Social +4`, `Intellectual +2` (total +6). No auto-penalty to `Crafting`/`Plants`; shrine-affiliated people could also participate in ordinary livelihood and production.
- **historical / distinctiveness gate:** 適用可能な古代～中世の神社祭祀者の一般像。現代の統一的な神職資格制度や神仏完全分離を持ち込まない。Already approved child 神事見習いの子 does not represent the adult officiant; Buddhist monks are not automatically interchangeable with shrine officiants.

### 2. 社に仕える巫女 — adult, settled shrine ritual performer

- **Implemented ID:** `AMJC_ShrineRitualAttendantAdult`; slot: `Adulthood`.
- **title:** 社に仕える巫女 / **titleShort:** 巫女.
- **description (proposal, Japanese):** [PAWN_nameDef]は社に仕え、祭礼で神楽を舞い、供え物の準備や参詣者の世話をしてきた。繰り返し舞を務めて身のこなしを磨き、参詣者への応対にも慣れている。
- **skills (revised):** `Social +4` (total +4); reflects interactions with visitors, **not** kagura technique. Original `Artistic +4` was withdrawn because Artistic is visual production, not dance. Do not substitute Crafting/Intellectual to restore a former arbitrary total. No additional psychic sensitivity or healing effect.
- **Existing Trait linked in production XML:** `forcedTraits: Nimble` degree `0` (**身軽**). Frequent kagura practice supports a *physically agile* individual biography. In the actual game this gives **melee dodge**, not dance-performance ability, so it is a meaningful combat side effect rather than a literal dancing bonus. No other trait should be forced solely on the basis of shrine service. New BackstoryDef XML has the link; the original game has not yet verified it.
- **gender solution in source:** default title 社の神楽役, female title 社に仕える巫女 via `titleFemale` and matching short titles. This is a title override, not female-only generation; any pawn can have this biography and Nimble.

### 3. 渡り巫女 — adult, itinerant ritual work

- **Implemented ID:** `AMJC_ItinerantRitualistAdult`; slot: `Adulthood`.
- **title:** 渡り巫女 / **titleShort:** 渡り巫女.
- **description (proposal, Japanese):** [PAWN_nameDef]は各地の村や市を巡り、祭礼や祓いの依頼を受けて暮らしてきた。初対面の人々とも言葉を交わし、土地ごとの習わしに合わせて神事を行っていた。
- **skills (revised):** `Social +5` (total +5); the larger Social emphasis models dealing with changing patrons and communities. Original proposed `Artistic +2` is withdrawn: itinerant kagura/performing is not a sculpting skill. Travel by itself does not grant a fictional survival skill or a Plants bonus.
- **historical and generation gate:** Differentiate itinerant religious work from permanent shrine service and from 旅芸人, merchants or outcasts. Period/region context should not imply this form existed unchanged throughout every era. Default title 巡回する祭祀役 and female title 渡り巫女 likewise use `titleFemale` with no gender-only generation.

### 4. 木地師 — adult, mobile woodenware craft

- **Implemented ID:** `AMJC_ItinerantWoodworkerAdult`; slot: `Adulthood`.
- **title:** 木地師 / **titleShort:** 木地師.
- **description (proposal, Japanese):** [PAWN_nameDef]は良い木材を求めて山々を渡り歩き、椀や杓子などの木製品を作って暮らしてきた。木の性質を見分け、土地を移りながら道具を作り続けていた。
- **skills:** `Crafting +5`, `Plants +2` (total +7). Primary identity is material selection and making small wooden wares; no bonus to `Construction` by default, keeping it distinct from existing 山里の大工 and familiar carpenters.
- **historical gate:** Cultural Affairs Agency documents the **folklore of itinerant woodworkers** and differences between turned-wood and ladle makers, but sources recording tradition in the 20th century do **not** establish that the same term, institutions or itinerant privileges apply unchanged in every ancient/medieval period. If age or regional eligibility is too broad, use an ordinary term such as 山を渡る木工職人 pending author approval; do not base the text on a legendary origin as proven history.

### 5. 狩人の家の子 — childhood, hunter household

- **Implemented ID:** `AMJC_HunterFamilyChild`; slot: `Childhood`.
- **title:** 狩人の家の子 / **titleShort:** 狩人の子.
- **description (proposal, Japanese):** [PAWN_nameDef]は狩猟を生業とする家に育ち、獣道や足跡の見分け方を教わった。罠の手入れや獲物の運搬を手伝い、弓の扱いも少しずつ覚えていった。
- **skills:** `Shooting +2`, `Animals +1`, `Plants +1` (total +4); less adult-like than 山野の猟師, and no forced `Brawler` or an automatic work prohibition.
- **historical gate:** Hunting as livelihood rather than simply sport; avoid making マタギ a generic title for all locales and periods. Distinctive **childhood** slot avoids creating a redundant new adult 狩人.

## Dance / performance skill mapping correction (author feedback, 2026-10-19)

Kagura and dancing remain credible elements of the shrine and itinerant-miko **narratives**, but base-game `Artistic` is not a dance/performance skill. The two older provisional `Artistic` boosts were **retracted**, rather than re-labeled as `Crafting` or `Intellectual` to manufacture a full +6 total. Shrine miko now proposes only `Social +4`, and traveling miko only `Social +5` for interactions and itinerant contacts. Their actual dancing competence is **flavor-only** in this background Mod. Their lower aggregate skill gains compared with adult craftsmen are intentional *pending author balance review*, not a stealth numerical compensation. A separate dancing job/recreation/performance system would be a new gameplay feature requiring its own need/design/Mod audit and is **not requested or implemented here**.

## Trait correspondence check (author permission, 2026-10-19)

Existing Vanilla traits were compared with the five draft roles and their real game behavior. **Only a single restrained match is added as a candidate**: `AMJC_ShrineRitualAttendantAdult` / `Nimble` degree 0 (身軽), *only because this specific proposed biography emphasizes repeated kagura training and agile body movement*. This trait improves **melee dodge**, not dancing, and represents a physically agile pawn rather than an institutional claim about every historical shrine practitioner. No new `Dance` skill, work giver or recreation has been added. `PsychicSensitivity` was rejected as conflating religious practice with fictional psychic powers; `Kind` / `Ascetic` / `GreatMemory` were rejected as personality/memory assumptions not established for every shrine worker, and `Industriousness` or `ShootingAccuracy` were not forced on the mobile woodworker/hunter child just for having an occupation or early training. The risk of adult/child contradictory forced Traits and generic positive-stat inflation favors **no other forced Traits**. Existing random Traits still supply individual variation. Exact forced-trait encoding/conflicts must be source-checked before this candidate becomes an active BackstoryDef, and the author has yet to approve the final P3 biography text and gameplay effects.

## Numeric/design parity and implementation gates

| Proposed ID | Slot | Social | Intellectual | Artistic | Crafting | Plants | Shooting | Animals | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AMJC_ShrineOfficiantAdult | Adult | +4 | +2 | — | — | — | — | — | +6 |
| AMJC_ShrineRitualAttendantAdult | Adult | +4 | — | — | — | — | — | — | +4 |
| AMJC_ItinerantRitualistAdult | Adult | +5 | — | — | — | — | — | — | +5 |
| AMJC_ItinerantWoodworkerAdult | Adult | — | — | — | +5 | +2 | — | — | +7 |
| AMJC_HunterFamilyChild | Child | — | — | — | — | +1 | +2 | +1 | +4 |

These numeric skill gains are **implemented in source**, not empirically measured distribution/rarity or final Pawn skills. **The settled-shrine-miko has one source-implemented forced `Nimble` (degree 0) in addition to the Social bonus; its combat dodge side effect needs author/content acceptance.** Other four profiles have no forced trait. No abilities are automatically forbidden. Proposed `spawnCategories`: `Tribal` as a starting original-MO candidate; `MedievalCommon` only after optional-patch intersection check. `Civil`/other original Vanilla normal-Pawn route applicability requires verification. Do not claim this list restores 135 removed backgrounds at a 1:1 rate.

**Next acceptance after active XML:** Check loaded 1.6/1.7 BackstoryDefs for five IDs, all skills and slots, titleFemale and Japanese translation, original `Nimble` degree 0, and new Pawn generation through intended categories including original MO `Tribal` and optional `MedievalCommon` where supported. Then check actual category frequency and old-save references. Do not treat old 1.6/1.7 PASS as evidence for these new Defs. No native game launched or Steam action.

## Reference record

- Current original source ownership and exact 123 rewritten text IDs: [Stage2JapaneseReviewDraft](Stage2JapaneseReviewDraft.md), [HistoricalOccupationBackstories](../Languages/Japanese/DefInjected/BackstoryDef/HistoricalOccupationBackstories.xml).
- Original game and MO generation: Project [Core metadata audit](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/VanillaCoreCharacterDefsSourceAudit20261016.md) and [MO filter crosswalk](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/Research/MO16BackstoryFilterCrosswalk.md).
- Historical miko: [Japan Search — 巫女](https://jpsearch.go.jp/gallery/ndl-dKYRDz2Z2Yx), distinguishes settled shrine service from walking/traveling miko and historic kagura/rites.
- Woodworkers: [Agency for Cultural Affairs — 木地屋の生活伝承](https://kunishitei.bunka.go.jp/heritage/detail/312/165), documents mobile woodworking but not unbroken ancient-period usage.
- Hunting: [Agency for Cultural Affairs — 狩猟習俗](https://online.bunka.go.jp/heritages/detail/203533), notes subsistence, 山立, region-specific マタギ and falconry.
