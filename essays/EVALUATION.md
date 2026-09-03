# Essays — Evaluation Against the Standard

Each essay evaluated against the seven-point standard in `README.md`, with its key claims cross-checked against the actual source papers. Status: **KEEP** (in good standing), **AMEND** (keep the essay, fix listed items), **FLAG** (substantive accuracy/tiering problem). Last run: 2026-07-05.

Headline: first pass (2026-07-04) **8 KEEP, 3 AMEND, 0 FLAG**; the 3 AMENDs were fixed the same day. Second pass (2026-07-05) added the three series-finale essays (9 The Early Universe, 10 The Arrow Sorts the Continuum, 11 Here Is the Knife), all **KEEP, 0 AMEND, 0 FLAG** on an independent cross-check against their papers. So all **13 essays are KEEP**. No hard accuracy breaks were ever found. Every essay is *more* conservative than its own source papers in two ways worth noting: all of them scrubbed the "Wolfram / Ruliad" lineage lines the papers themselves carry (satisfying the no-Wolfram-in-public rule), and the highest-risk essays self-label their weakest results ("promissory note," "borrowed numbers," "account with a named gap"). The three finale essays were the highest tiering-risk of the set and passed the sharpest checks: essay 9 refuses to claim ED *derives* the CMB (the cosmology arc is inherited, tier M3) and flags the CMB-Gaussianity debt as open; essay 10 disclaims the Clay problems and tiers the soliton wall as a measured negative; essay 11 states the decoherence wall's *sharp architecture-independent* form as the structural prediction while marking the 140–250 kDa mass an extrapolation, and flags the 3D-from-linking open premise.

## Status Table

| Essay | Status | Companion paper(s) |
|---|---|---|
| 1 — Introduction | **KEEP** | series opener (surveys downstream results; no single anchor, acceptable for this slot) |
| 2 — Quantum Mechanics | **KEEP** *(amended)* | Paper_011_5_FourPostulates, Paper_003_BornRule, Paper_006_5_Schrodinger_Stone, Paper_007_HilbertSpace, Paper_012_6_Heisenberg |
| 3 — Spin, Antimatter, Dirac | **KEEP** *(amended)* | Paper_103_Cl31_FrameUniqueness, Paper_106_DiracEquation, Paper_102_SpinStatistics, Paper_112_hbar_Origin |
| 4 — Matter from the Arrow | **KEEP** | Paper_ED_Baryogenesis, Paper_MS-II_MatterSectorFromTheArrow |
| 5 — Three Forces, Three Dimensions | **KEEP** | Paper_MS-II_MatterSectorFromTheArrow |
| 6 — Yang-Mills and the Mass Gap | **KEEP** | Paper_019_YM2, Paper_021_YM4_MassGap, Paper_023_YM6_ClaySynthesis |
| 7 — Gravity, Dark Matter, Dark Energy | **KEEP** | Paper_OneField_Letter, Paper_GR-III, Paper_029_a0, Paper_038_5_Lambda, Paper_GR-IV |
| 8 — Black Holes and Information | **KEEP** | Paper_039_HorizonDecoupling, Paper_047_HawkingSpectrum, Paper_050_PageCurve, Paper_052_BH_ParadoxSynthesis, BH_Thermal2Pi |
| 9 — The Early Universe | **KEEP** | Paper_SCBU_SubstrateCosmologyBoundary, Paper_ED_Cos_03_CMBAcoustic, Paper_ED_Cos_04_StructureFormation, Paper_ED_Cos_06_InflationarySpectrum |
| 10 — The Arrow Sorts the Continuum | **KEEP** | Paper_TheArrowSortsTheContinuum |
| 11 — Here Is the Knife | **KEEP** | 22_Ways_to_Kill_Event_Density, Predictions_and_Falsifiers, Paper_056_ClassA_Wall |
| Dark Matter — The Case Without a Particle | **KEEP** | Paper_029_a0, Paper_ED_DF2_DF4_GroupSuppression, Bullet_TopologicalDefect |
| The Universe Doesn't Happen All At Once | **KEEP** *(amended)* | Paper_GR-IV_ArrowsAlibi |

## Currency — not yet evaluated (recorded 2026-09-03)

The status table above ends at the second pass. **Five files in this folder have never been run against the seven-point standard**, and a reader should not read their absence as a pass:

| File | Why it is not in the table |
|---|---|
| `ED_Essay_12_Cost_Benefit.md` | written after the second pass |
| `ED_Essay_13_TheFirstShadow.md` | written after the second pass |
| `ED_Essay_14_TheConstantsAreInherited.md` | written after the second pass |
| `ED_Essay_FormAndFlesh_TwoWalls.md` | arrived by reclassification from `position-paper/`, so it was held to the position-paper standard, not this one |
| `StartWithTime_Essay.md` | written as a standalone piece, never folded into the series evaluation |

`Paper_SelectedFormalisms_I…V` are also in this folder and are deliberately **out of scope** here: they are formalism papers, not essays, and the seven-point standard does not apply to them.

*Found by a pointer-layer coverage sweep, not by a re-read. Running the standard over the five is real work and is not claimed done.*

---

## The Three AMENDs — all resolved 2026-07-04

Each fix below was applied; the essays now meet the standard. Recorded for provenance.

### Essay 2 — Quantum Mechanics
- **Pt 3 (overclaim), Born rule.** The essay narrates the Born rule as an unconditional theorem: *"the mathematics forces ... Not a choice. The unique consistent answer."* Paper_003 is a **conditional structural derivation** resting on a declared postulate (P-LinRate) and **explicitly disavows deriving Gleason's theorem**. Fix: soften to "given how the substrate weights possibilities, the square is the consistent bridge"; drop "forces / not a choice."
- **Pt 2 (tiering), Schrödinger.** Essay presents Stone's theorem as delivering the equation outright; Paper_006_5 flags that the Schrödinger *form* is definitional (P), with only the substrate identification form-forced. Fix: one clause noting the equation's form is carried, not conjured.
- **Pt 4 (killable), optional.** No falsifier native to the QM claims (defensible, since the essay reproduces rather than revises QM). Could name the ħ-as-coherence-scale hypothesis as the falsifiable piece.

### Essay 3 — Spin, Antimatter, Dirac
- **Pt 1/3 (anchoring/overclaim), antimatter.** *"Antimatter is matter read against the grain of time"* is stated as settled fact, but **no companion paper derives antiparticle-from-arrow**; antimatter is deferred to Part 4 (Baryogenesis / MS-II). Fix: mark the antimatter mechanism as a Part-4 preview / not-yet-derived here, or cite the actual paper.
- **Pt 3 (overclaim), exclusion.** Pauli exclusion is presented as fully substrate-native; Paper_102 is M3, conditional on **inherited QFT exchange machinery**. Fix: one honest clause.
- **Pt 4 (killable).** No in-essay falsifier; Paper_106 supplies two (spin-½ not obeying Dirac; Cl(3,1) admitting non-Dirac first-order equations). Fix: surface one.

### The Universe Doesn't Happen All At Once
- **Pt 1 (anchored).** Names no companion paper. Fix: add the line `Companion paper: Paper_GR-IV_ArrowsAlibi`.
- **Pt 6 (clean).** **41 em-dashes in ~2000 words** (~1 per 49 words), heavy AI-tell against the ~90%-fewer standard. Fix: cut to commas/periods/colons/parens (Essay 1 and the Dark Matter essay hit 0).
- **Pt 4 (killable), optional.** GR-IV hands a razor-sharp killer the essay doesn't use: **any detection of α₂ ≠ 0 kills it.** Import it.

## Soft note (KEEP, not blocking)
- **Essay 6:** falsifier is more implicit than the sharp kill-lines in essays 4/5; the papers' F1–F4 exist. A light future pass could surface one crisp "find X and this is wrong" line.
