# P3 five original backgrounds — real-game acceptance (2026-10-20)

**Source under test:** Characters main `31543c19930b762c1729bec1f884aff2dec824af` (PR #16 custom-loader fix and expanded existing `Tests/Background16/BackgroundSteps.cs`), paired separated Culture source `f071f0602e9989a011f431f30a961499dcd38ee7`. Test runner/dispatch Project main `95229dcc70d38ee15eb0f8d6b6b22d6d0ca1bfba` (PR #806). No automated PR/push native trigger: manual private Project Issue #39 only. Exact product XML: `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml`, locale: `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`. Current original 1.6/1.7 source-backed test values below are the authoritative acceptance **premises**, not guesses based on PASS count.

## Actual native results

| Profile | Evidence / game | Loaded outcome |
|---|---|---|
| Original RimWorld 1.6 Japanese, Characters+Culture | [Project Actions #39307355742](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39307355742), artifact `culture-characters-cutover16-39307355742` ID **12214985433** | `one_scenario_pass=true`, Pickle1/1, Japanese 89 preapproved Stage2 texts checked, new P3 source checks passed, native/errors=0, exit=0, game original unchanged; game **1.6.4871 rev598** |
| Original RimWorld 1.7 English, Characters+Culture | [Project Actions #39307680224](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39307680224), artifact `culture17-native-39307680224` ID **12215235168** | `native_pass=true`, Pickle1/1, compiled latest Characters `Background16Steps` test, native Unity `errors=[]`, FMOD `fmod_errors=[]`, exit=0, original files unchanged; game **1.7.4977 rev1248** |

## Check items and intended specifications

The same expanded owner `Tests/Background16/BackgroundSteps.cs` existing background test is loaded by both 1.6 and 1.7 sessions. The 1.7 test additionally retains current Culture chair/meal behavior checks. Following predicates ran and passed:

| Item | Expected in original loaded game | Evidence scope |
|---|---|---|
| New IDs and ages | Exactly the five named new source definitions are present; four `Adulthood` and `AMJC_HunterFamilyChild` is `Childhood` | C# loaded `DefDatabase<BackstoryDef>` and slot assertions, both |
| `AMJC_ShrineOfficiantAdult` | Social+4, Intellectual+2 | Loaded `skillGains` `SkillGain.skill/amount`, both |
| `AMJC_ShrineRitualAttendantAdult` | Social+4 and **one** forced `Nimble` degree0 | Loaded `skillGains` and `forcedTraits` entry, both |
| `AMJC_ItinerantRitualistAdult` | Social+5 and no forced Traits | Loaded list, both |
| `AMJC_ItinerantWoodworkerAdult` | Crafting+5, Plants+2 and no forced Traits | Loaded list, both |
| `AMJC_HunterFamilyChild` | Shooting+2, Animals+1, Plants+1 and no forced Traits | Loaded list, both |
| Categories | All five contain `Tribal` (original preindustrial selection) and optional `MedievalCommon`; no new MO dependency | Loaded category lists, both. Eligibility **does not prove actual selection frequency** |
| Sex-specific titles | Settled performer: male/default **社の神楽役**, female **社に仕える巫女**, female short **巫女**. Traveling ritualist: male/default **巡回する祭祀役**, female **渡り巫女**, female short **渡り巫女** | Loaded `TitleFor`/`TitleShortFor` in Japanese 1.6. In English 1.7 the settled performer female **shrine miko** vs male **shrine ritual attendant** was explicitly checked |
| Original routes / compatibility | Existing 77 adult and 55 Solid/3 Shuffled restricted IDs still exist with their exclusion route, 89 rewritten text entries load, compiled separate Characters Harmony postfix present; initial general Colonist Pawn can be generated | One existing combined background scenario, both; Japanese 89 exact text in 1.6 |
| Test integrity | Each run exactly 1 non-skipped Pickle scenario; game process exits 0; native errors=0, original game unchanged | Actual native runner stdout, uploaded source provenance and artifact IDs above |

## Deliberately unproven scope

- **Random occurrence and balance:** the one normally generated Colonist Pawn was checked for valid history and disallowed original backgrounds, but was not required to draw one of these five *particular new P3 histories*. Thus actual spawn probabilities/distribution by faction and whether every five biographies appears during normal random generation remain unmeasured.
- **MO:** no actual latest Medieval Overhaul 1.6/1.7 PawnKind/Faction generation with these P3 Defs, nor optional Medieval Backstories Patch loaded-Def intersection, nor MO-specific trait conflict validation in this pair of native runs. The `Tribal`/`MedievalCommon` list assertion is **source-loaded category presence**, not proven MO occurrence.
- **Cross-language and graphics:** Japanese 1.7 typography/glyphs and separate 1.6 English presentation were not the scoped profiles. The five new Japanese narrative bodies were checked as nonempty; only Stage2 original 89 narratives were compared character-for-character with locale XML; no claim of complete rendered Japanese UI screenshot.
- **Saved pawns:** no existing-save reload or long-term save compatibility claim for the new backgrounds. Existing original Def IDs and generated external saves were not modified.
- **P2 forced-list XPath removal:** the preexisting `BodyPurist`/`Transhumanist` commonality0 loaded checks passed, but original `FerventResearcher72`, `HunterOfTheKing53`, `TestSubject90` forced assignment *removal* is not explicitly inspected in this updated scenario. Keep its separate OPEN status.
- **New underlying mechanic:** no dancing skill, kagura work giver, new religion/DLC feature or actual new-melee-dodge stat test. `Nimble` loaded as Trait, without a separate measurement of a pawn's melee dodge score.
- No Steam/Workshop publication, no player saves modified, no native re-run authorized solely for further PASS counts.

**Disposition:** Five P3 loaded-source behaviors in the two specified languages/versions **PASS**; broad release, MO compatibility, all-new-history random appearance and unrelated P2 forced-list correctness remain independent. Do not promote those untested items into PASS or schedule unattended native tests.

## Follow-up on corrected P2 forced traits and original MO 1.6 (2026-10-20)

This later evidence **supersedes only the P2 forced-list and original MO 1.6 entries previously listed as OPEN above**. The original 1.6 Japanese/1.7 English P3 results remain valid as historical runs. A real Vanilla Core XML source audit found P2 patch conditional selectors were searching for `li[key=...]` and `li[traitDef=...]`, but original `BackstoryDef.forcedTraits` in those six named source records is stored as named children (`BodyPurist`, `Transhumanist`, `DrugDesire`). Production patches were corrected in Characters [PR #18](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture-Characters/pull/18), main `3fe545fe8c3e1bb7ec0fc272b32ce91351f52e20`; original identities, unrelated Traits, 135 generation restrictions and 123 rewrites preserved.

| Actual run | Real profile | Result and concrete checks |
|---|---|---|
| [Project #39366126773](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39366126773) | **Original 1.6.4871 + MO 1.6.2.2 + VEF/SYR + cutover Culture + current Characters**, private disposable audio conversion | Pickle **1/1 PASS**, Unity ERROR 0, exit0, original game unchanged. `AMJ_MO16_FACTION_FILTERS_OK`, `PAWNKIND_FILTERS_OK`, `PAWNS_OK`, `BRIGAND_FACTION_PAWNS_OK`, and loaded Characters `AMJ_CULTURE_P2_FORCED_TRAITS_STRIPPED_OK`, `AMJ_CULTURE_P3_FIVE_BACKSTORY_DETAIL_OK` each occurred exactly once. Generated three player MO PawnKind and one Brigand faction Pawn samples; no Medieval Backstories Patch in this profile. Artifact `mo-character-loaded16-39366126773` ID **12240050706**. |
| [Project #39366130640](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39366130640) | **Original 1.7.4977 Vanilla + cutover Culture + current Characters** | Pickle **1/1 PASS**, Unity errors [], FMOD errors [], exit0, original game unchanged. Current `Background16Steps` loaded/compiled (SHA256 `d6b57ead382fafbc0ada129043077d735b9c4b398942efce729ce9d2911786b1`) and executed with six forced-trait checks and five P3 loaded-Def details plus a normally generated colonist. Artifact `culture17-native-39366130640` ID **12240140546**. |

**Revised acceptance premises:** `HunterOfTheKing53` and `TestSubject90` must lack forced `BodyPurist`; `FerventResearcher72` must lack `Transhumanist`; `DischargedSoldier53`, `MechanoidHacker93`, `VideoGamer16` must lack `DrugDesire`. `DischargedSoldier53` retains original `TooSmart`. All three old TraitDefs remain with `commonality=0`. Original character Def identities remain. For P3 the same five specific new loaded DefNames, 4 adult/1 child, exact Vanilla skillGains, only shrine performer forcing `Nimble=0`, and Tribal/MedievalCommon category memberships must resolve unchanged in both profiles. Original MO 1.6 player and hostile Pawns must generate without Unity ERROR. The newer run's proven loaded-Def states do not prove a specific random Pawn drew one of the five new P3 histories.

**Not accepted:** MO 1.7 original provider, optional Medieval Backstories Patch combination, each new P3 biography actually appearing in a sample/random distribution, old-save reload, other Mods forcing suppressed traits, exact 1.7 Japanese title rendering, two new alcohol-preference Mood Thought effects, or Steam/Workshop. The MO 1.6 test substitutes two unsupported original audio MP3s with *disposable* PCM/WAV in its own licensed game copy; **direct original MP3 audio compatibility was not tested**. No automatic native test trigger, repeating native test cycle, or user-owned game/save modification. Project [PR #819](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/pull/819), main `5e422839d3dbf6257de412503a90f078603ea6f8` only provided two exact pinned manual invocations.
