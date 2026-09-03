# ED State Reduction — the measurement/gravity seam

**What this folder is.** The **standalone state-reduction papers** — Event Density's peer-facing statement on gravitational collapse of the wavefunction, positioned against its two nearest published neighbors (Diósi, Penrose). This is the *measurement-side* companion to the dark-sector folder: Diósi and Penrose are ED's measurement-side interlocutors as Berezhiani and Khoury are its dark-matter-side ones. The *working record* behind these (the outline and the referee history) lives in the `event-density` working repo under `theory/State_Reduction/`.

## The position in one paragraph

Both neighbors say **gravity causes collapse** and put the scale in an energy (`E_G`, the gravitational self-energy of the difference of the mass distributions). ED says something adjacent but deeper: the **definiteness of measurement outcomes and the flow of gravitational time are one primitive** — the arrow of commitment (P11), which *is* the khronon — so the collapse variable is **time, not energy**, and the "cause" is not a cause but an identity. Read against Penrose specifically, ED **supplies the well-defined preferred time whose absence drives his argument**, and it does so while keeping collapse **local and forward-causal** — a genuinely stochastic reduction that needs no superdeterminism and no hidden variable (A1 capacity-zero + the forward arrow). The honest ledger, after adversarial review: a deep reframe, a **scaling argument that reproduces `τ ∝ ℏ/E_G`** (coefficient and exact energy functional open), and a **retired experimental risk** (the 2020 Gran Sasso spontaneous-radiation bound does not exclude ED's discrete which-channel commitment — but that is immunity shared with standard QM, not a distinctive win) with the open pieces named.

## The papers (this folder)

- **[Plain_Language_Summary.md](Plain_Language_Summary.md)** — a non-technical walkthrough of the whole arc; read this first for the story, then the positioning note for the peer-facing version.
- **[Paper_ED_StateReduction_vs_CollapseModels.md](Paper_ED_StateReduction_vs_CollapseModels.md)** — **START HERE (peer-facing).** The positioning note and synthesis of the arc: the shared conviction (geometry not an independent quantized field; collapse physical and gravity-rooted), ED's cited account (§4 arrow = einselection = pointer basis; §6 arrow = khronon), the two neighbors gift-then-diverge, the unifying difference (time not energy), the honest gap, position, falsifiers, and tiers.
- **[StateReduction_CollapseRate_ED_Derivation.md](StateReduction_CollapseRate_ED_Derivation.md)** — the companion **derivation**: the `τ ∝ ℏ/E_G` scaling argument from the khronon-clock difference + einselection, its two refinements over the rivals (a definite reduction; a native regulator) plus a difference-form consistency check, and the emission-signature analysis (why the 2020 bound does not exclude ED, honestly scoped). Detailed working behind §5 of the positioning note.
- **[StateReduction_ChannelGranularity.md](StateReduction_ChannelGranularity.md)** — resolves the **load-bearing residual** of the emission result: is ED's pointer/channel basis coarser than atomic wavepackets (else ED radiates and is excluded)? Yes, grounded-in-kind on three standing corpus pillars (emergent unitarity; environment-selected einselection; operational distinguishability).
- **[StateReduction_OpenPiece_i_EnergyFunctional.md](StateReduction_OpenPiece_i_EnergyFunctional.md)** — open piece (i): computing `E_G` from ED's own gravity gives a candidate MOND enhancement for mesoscopic masses, but ED's own External Field Effect (derived from `Paper_029`'s horizon dipole) Newtonizes it in Earth's field → ED ≈ Penrose in the lab (weapon closed, consistency result).

## Status (after adversarial referee, 2026-07-21)

Refereed twice against the corpus and the external sources; first verdict **major revisions** (all applied), re-review verdict **minor revisions** (applied). What stands: the Diósi/Penrose characterizations, corpus discipline, the §6 guardrail carried honestly. What was corrected: the collapse rate is a **scaling argument**, not a structural derivation (`E_G` identified with Penrose's answer, not computed); the 2020 immunity is **shared with standard QM**, not a distinctive prediction.

**Residual (ii) resolved (2026-07-21), conditional on one load-bearing question.** The referee's sharpest objection — that "no momentum diffusion of a localized charge" was in tension with P11's dissipative (line-gap) face — is answered from the corpus. The Lindblad derivation (`event-density` `arcs/arc-Q/lindblad_extension.md`) fixes, FORCED from P11, that ED's jump operators are **channel projectors** `Ĵ_α = g_α Π̂_α`, not position operators; so a committed charge `ρ = Π̂_α` is an **exact fixed point** of the dissipative face (`D[Π̂_α] = 0`), with no continuous momentum diffusion — unlike CSL/DP, whose position-coupled noise has no fixed point and pumps `d⟨p²⟩/dt = const` forever. The line-gap face is not suppressed; it simply has the committed states as dark states. The same argument covers the spontaneous-heating bound. Tier: **structural result** (FORCED identification + exact algebra), conditional on the one open question below.

**Open piece (i) resolved (2026-07-21).** Computing `E_G` from ED's own gravity (`Paper_QuadraticStrain_v1`: Newton diagonal + local–horizon MOND off-diagonal) gives a *candidate* MOND enhancement for mesoscopic masses (all sub-`a_0` in self-gravity) — but ED has a full External Field Effect, derived from `Paper_029`'s horizon dipole (sourced by the chain's total acceleration): the enhancement is `~√(a_0/g_ext)`, set by the ambient field. Earth's field Newtonizes it to `~3×10⁻⁶`, so **ED ≈ Penrose–Diósi in any accessible experiment** — a consistency result, not a weapon (the naive 5–50× was an EFE artifact). Working note: `event-density` `theory/State_Reduction/StateReduction_OpenPiece_i_EnergyFunctional.md`.

**The load-bearing channel-granularity question is now resolved grounded-in-kind** (companion `StateReduction_ChannelGranularity.md`). The emission escape needs ordinary bound charges to be single-channel eigenstates; if the channel basis were fine toward `ℓ_ED`, ordinary matter would span many channels and ED would be *excluded*. Three standing corpus results close this against the risk: (1) `ℓ_ED`-fine substrate dynamics is *coherent* Schrödinger evolution (emergent unitarity), not a position measurement; (2) the decoherence basis is *environment-selected einselection* — the coarse robust basis, and the *energy eigenbasis* (stationary, non-radiating) for bound charges; (3) commitment individuates only *distinguishable* channels (Report §4), and distinguishability is *operational* (A1), with a coarse floor `≫ ℓ_ED`. So the pointer basis is coarse and the escape holds. **Remaining constructive work:** the explicit ED theorem + the exact distinguishability floor; and the collapse coefficient / energy functional.

## Source papers (this folder synthesizes, it does not supersede)

- **Measurement / arrow = einselection:** `../../ED_UnifiedFramework_Report.md` §4; `qm-kinematics/Paper_001_PreIndividuation.md`, `Paper_003_BornRule.md`, `Paper_005_ProjectiveMeasurement.md`; the Gleason keystone.
- **Arrow = khronon / gravity's time:** Report §5–§6; `gravity/Paper_GR-I_WeakFieldEinsteinMetric.md`, `Paper_GR-II_KhronometricClass.md`; `gravity/Paper_QuadraticStrain_v1.md` (gravity = interference cross-term, not Einstein–Hilbert — bears on the exact energy functional).
- **Locality without superdeterminism:** the A1 channel-capacity-zero result (`event-density` `Bits/docs/A1_ChannelCapacity_Results.md`).
- **P11's two non-Hermitian faces:** `event-density` `theory/Anomaly_Cancellation/` (point-gap worldline vs line-gap Lindblad).

## The neighbors (external)

Diósi 1987 (Phys. Lett. A 120, 377); Penrose 1996 (GRG 28, 581); the 2020 spontaneous-radiation exclusion (Donadi et al., *Nat. Phys.* 17, 74 (2021); arXiv 2111.13490) and the follow-up effectiveness-of-collapse literature.

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[`StateReduction_TieredClaims_Ledger.md`](StateReduction_TieredClaims_Ledger.md)** — the arc's **tiered-claims ledger**: every load-bearing claim in this folder with its current tier. It doubles as the arc's staleness detector — where a paper and the ledger disagree, the ledger's `Status` column is the current state. Read it before citing anything here.
