# AMJ Culture – Characters（中世日本 - 文化・人物）

Independent Mod for ancient-to-medieval Japanese character backgrounds and traits, split **only** from [AMJ Culture](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture).

**Status: independent RimWorld 1.6/1.7 Characters DLLs built; original 1.7 Japanese Vanilla + current Culture and original 1.6 English Medieval Overhaul 1.6.2.2 + current Culture focused game acceptance PASS. Do not co-install with an older unsplit Culture build. Development Mod, not Steam-published.**

- Original BackstoryDef/TraitDef identities, skills and work restrictions preserved.
- **Existing backgrounds rewritten: 126 distinct IDs** — 123 earlier bilingual historical rewrites plus three original Core occupations (`Logger16`, `Logger95`, `Weaver63`). These change historical names and descriptions, **not** add new biographies; original IDs and underlying skills/possessions are retained (except the documented `Outlander` eligibility addition for `Weaver63`).
- **New playable backgrounds: 12** (8 adulthood, 4 childhood), with original English and Japanese text and historical roles. **14 new BackstoryDef IDs exist in source**, but the two overlapping adult roles (new woodcutter and new textile weaver) are retained for save identity only and excluded from normal pawn generation; they must not be advertised as playable additions.
- **Existing backgrounds restricted from ordinary generation: 135** (77 adulthood, 58 childhood); these are not deleted. 23 original starting-possession substitutions are separate from new-background counts. **Two new traits** are added: alcohol lover / alcohol averse (酒好き／酒嫌い).
- Transhumanist, BodyPurist and DrugDesire ordinary-generation suppression (including known forced background entries); new alcohol-preference traits affect mood only while intoxicated.
- Approved English XML and Japanese DefInjected, separate Solid-child Harmony patch and `AMJ.Culture.Characters` source project.
- Harmony required, Medieval Overhaul optional; no mandatory Culture dependency.
- Greedy/Jealous shared-lodging mood rules, initial chemical addictions, other drugs, entrances, meals and bedding stay in Culture.
- New game recommended; old-save compatibility not guaranteed.

[Design](Docs/Design.md) is authoritative; [Workshop description draft](Docs/WorkshopDescription.md) separates original rewrites from new content. [Coordination](Docs/Coordination.md) tracks cutover. Unsplit Culture historical native evidence is not transferred retroactively. New Characters alone 1.6 PASS [Project #39228255901](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228255901); paired separated Culture 1.6 PASS [#39229556343](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39229556343); paired 1.7 PASS [#39228936614](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39228936614). The earlier paired 1.6 native crash in Mono GC remains unexplained; paired-only rerun passed. Latest original 1.6 MO 1.6.2.2 + Culture + Characters P3 occupation-dedup acceptance [#39590687182](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39590687182) PASS; latest original 1.7 Japanese Vanilla + Culture + Characters occupation-dedup acceptance [#39587913897](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39587913897) PASS. Individual natural draw frequency, original MO MP3 playback, MO 1.7, DLC, old-save, visual glyphs and Steam acceptance remain untested.

Provenance: [Culture candidate commit `7448f290`](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Culture/commit/7448f290f2e1b0c0bdde93431c27662f0e066821). User-created MIT license preserved.
