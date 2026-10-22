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

## Workshop source directory — direct upload without ZIP

**Characters does not require a distribution ZIP or an archive builder.** Use the checked-out and reviewed Mod directory directly as the upload source. No `WorkshopPayload` or separate packaging pipeline is needed.

The following game content must exist under the Mod root:

- `LoadFolders.xml`, `LICENSE`;
- `About/About.xml`, `About/Manifest.xml`, `About/Changelog.txt`, `About/WorkshopTags.xml`, and an **approved** `About/Preview.png` once supplied;
- `1.6/Assemblies/AMJ.Culture.Characters.dll` and `1.7/Assemblies/AMJ.Culture.Characters.dll` (do not use `AMJ.Culture.dll`);
- `Defs/**`, `Patches/**`, `Languages/**` including the Japanese DefInjected translations.

Preserve the Mod-relative directory structure. Use the chosen upload tool's normal exclusion handling for development-only files (`Source/`, `Tests/`, `Docs/`, `AGENTS.md`, `README.md`, `.github/`) where supported. Do not create a parallel staged copy or ZIP solely for this. Do not invent `About/PublishedFileId.txt` before Steam allocates one. Check the actual upload source directory, required DLLs, XML and version metadata before publication.

## Acceptance already obtained (no automatic rerun)

- Original 1.7 Japanese Vanilla + separated Culture/Characters Core occupational dedup and relevant P2/P3 loaded checks: [Actions #39587913897](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39587913897), 1/1 Pickle, no Unity ERROR, exit0.
- Original 1.6 English + MO 1.6.2.2/VEF/SYR + separated Culture/Characters: [Actions #39590687182](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39590687182), 1/1 Pickle, no Unity ERROR, exit0.
- Existing original Vanilla 1.7 alcohol preference mood checks: [Actions #39403987672](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39403987672).
- These accepted checks cover the tested loaded definitions, specific forced-Trait rules, generic pawn generation and mood behavior in their declared configurations, **not** every source ID being naturally drawn.

## HOLD before Steam/2game publication

- [ ] Accepted `About/Preview.png` and any additional approved Workshop visual assets; **not present in owner main**. Follow the [Characters Preview creation/QA/approval procedure](GoldenPaths/WorkshopPreview.md). Documented rules or generated drafts are not acceptance. No unrelated image is to be substituted automatically.
- [ ] Confirm the actual Mod folder is accepted directly by the selected uploader (no distribution ZIP).
- [ ] Verify current source folder includes 1.6/1.7 DLLs and matching About/Manifest/Changelog versions.
- [ ] Establish an explicitly authorized first-item Steam upload path and host/account ownership, Workshop ID creation and visibility policy. At present there is **no verified Characters-specific publisher/Workshop ID**, and no instruction to create/upload one.
- [ ] Confirm changenote and complete tags can actually be transmitted by the authorized uploader; an XML file alone does not update Steam.
- [ ] Separate author's approval for first Steam publication and visibility, and live Steam subscriber download / uploaded description / tags verification.
- [ ] 2game posting is separately author-gated; source copy preparation does not mean the page exists.

Unverified scopes (MO 1.7, old-save load/remove, per-ID natural RNG, actual starting item grants, original MO MP3, Japanese visual glyphs) remain disclosed and are **not** automatically new native-run requirements. Do not misreport Steam/publication as complete.

Publication route: Project [WorkshopPackaging](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/WorkshopPackaging.md), [WorkshopChangenotes](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/WorkshopChangenotes.md); first-item registration/approval follows the separate currently applicable Project publisher policy.
