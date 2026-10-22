# First Workshop release checklist — Culture Characters 0.1.0

Status: **PREPARING / NOT PUBLISHED**. This checklist records evidence and boundaries, not an instruction to upload or create a public item.

## Authoritative content

- [Design](Design.md) owns features and actual implemented decisions.
- Runtime source counts: `Patches/HistoricalOccupationBackstories.xml` (34 unique existing IDs), `Patches/Stage2HistoricalBackstories.xml` (89), `Patches/Stage3CoreOccupationRewrites.xml` (3), disjoint = **126** rewritten original IDs.
- `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml` contains **14** new IDs, of which **12** (8 adult, 4 childhood) have ordinary categories. Two retained new IDs (`AMJC_WoodcutterAdult` and `AMJC_TextileWeaverAdult`) have `AMJ_CultureExcluded` only.
- **135** historically inappropriate original IDs are excluded from ordinary generation; definitions remain. Original starting-possession changes: **23**. New TraitDefs: **2**.

## Release-copy and metadata synchronization

- [x] `About/About.xml` supports 1.6/1.7; stable packageId, author and Harmony dependency maintained; `modVersion=0.1.0` candidate.
- [x] `About/Manifest.xml` unique identifier, same `0.1.0` version; no unknown Workshop `downloadUri` or fabricated PublishedFileId.
- [x] `About/Changelog.txt` starts at actual `0.1.0` with bilingual summary and no fictitious earlier releases.
- [x] Root `README.md` revised alongside metadata: count semantics, actual implemented scope, game evidence, and *not yet published* state.
- [x] `Docs/SteamWorkshopDescription.txt`: one combined English→Japanese BBCode manuscript, separated by exactly one `[hr][/hr]`; title comes from `About.xml` and is not repeated as a body heading.
- [x] `Docs/2GameDescription-ja.txt`: shorter Japanese description, **not posted** to 2game.
- [x] `About/WorkshopTags.xml`: planned `Gameplay`, `Storytelling`; actual Steam-side tags remain unverified.

## Exact subscriber payload — release staging contract

Include only these source paths, from one fixed and reviewed main commit:

- `LoadFolders.xml`, `LICENSE`;
- `About/About.xml`, `About/Manifest.xml`, `About/Changelog.txt`, `About/WorkshopTags.xml`, and an **approved** `About/Preview.png` once supplied;
- `1.6/Assemblies/AMJ.Culture.Characters.dll` and `1.7/Assemblies/AMJ.Culture.Characters.dll` (do not use `AMJ.Culture.dll`);
- `Defs/**`, `Patches/**`, `Languages/**` including the Japanese DefInjected translations.

Do not ship `Source/`, `Tests/`, `Docs/`, `AGENTS.md`, `README.md`, `.github/` or developer-only assets. Preserve the Mod-relative directory structure. Do not invent `About/PublishedFileId.txt` before Steam allocates one. Validate actual staged bytes, required DLLs, all XML and matching versions before upload; Git source alone does not prove the submitted payload.

## Acceptance already obtained (no automatic rerun)

- Original 1.7 Japanese Vanilla + separated Culture/Characters Core occupational dedup and relevant P2/P3 loaded checks: [Actions #39587913897](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39587913897), 1/1 Pickle, no Unity ERROR, exit0.
- Original 1.6 English + MO 1.6.2.2/VEF/SYR + separated Culture/Characters: [Actions #39590687182](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39590687182), 1/1 Pickle, no Unity ERROR, exit0.
- Existing original Vanilla 1.7 alcohol preference mood checks: [Actions #39403987672](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39403987672).
- These accepted checks cover the tested loaded definitions, specific forced-Trait rules, generic pawn generation and mood behavior in their declared configurations, **not** every source ID being naturally drawn.

## HOLD before Steam/2game publication

- [ ] Accepted `About/Preview.png` and any additional approved Workshop visual assets; **not present in owner main**. No unrelated image is to be substituted automatically.
- [x] `Tools/BuildWorkshopPayload.py` implemented as the strict publisher-file whitelist and version/XML/changelog gate. Its isolated synthetic check passed locally (inventory, missing-preview rejection, deterministic ZIP); **not** a check against complete original runtime source.
- [ ] Run `python Tools/BuildWorkshopPayload.py --audit-only` against the actual source checkout; review its file list and `release_ready`. The missing preview currently forces `release_ready=false`.
- [ ] Once an approved preview exists, use `python Tools/BuildWorkshopPayload.py --output ../Characters_0.1.0.zip --lock-output ../Characters_0.1.0.source-lock.json` on the exact pinned checkout. Review source/entry SHA-256 and both actual DLL bytes. No candidate ZIP is currently sealed.
- [ ] Establish an explicitly authorized first-item Steam upload path and host/account ownership, Workshop ID creation and visibility policy. At present there is **no verified Characters-specific publisher/Workshop ID**, and no instruction to create/upload one.
- [ ] Confirm changenote and complete tags can actually be transmitted by the authorized uploader; an XML file alone does not update Steam.
- [ ] Separate author's approval for first Steam publication and visibility, and live Steam subscriber download / uploaded description / tags verification.
- [ ] 2game posting is separately author-gated; source copy preparation does not mean the page exists.

Unverified scopes (MO 1.7, old-save load/remove, per-ID natural RNG, actual starting item grants, original MO MP3, Japanese visual glyphs) remain disclosed and are **not** automatically new native-run requirements. Do not misreport Steam/publication as complete.

Publication route: Project [WorkshopPackaging](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/WorkshopPackaging.md), [WorkshopChangenotes](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/WorkshopChangenotes.md); first-item registration/approval follows the separate currently applicable Project publisher policy.
