# Papers Index — Canonical Source of Truth

**Last updated:** 2026-07-02
**Purpose:** Single source of truth for every paper in the ED corpus. Tracks paper number (locked-in numbering), title, domain/arc assignment, status, and file location. Reflects the corpus state after Round 1 (per-paper QC), Round 2 (cross-paper audit + theorem gap-fill), Round 3 (cross-arc harmonization + SCBU + ED-SC 4.x arc), and the **2026-07-02 rebuild** (a full repo scan found the index had gone stale since 2026-05-14 — three entire arcs, a decimal-numbered sub-layer, and several standalone sections had never been added; see the maintenance note at the bottom).

**Source corpus:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\` (legacy/working-repo location; the EDG copies referenced by file paths below live under `physics-papers/<sub-domain>/`, `position-paper/`, `layers/`, etc. in this repo).

**Status enum:**
- **WRITTEN** — paper complete in corpus.
- **DRAFTING** — actively being written.
- **PLANNED** — identified, scheduled, not yet started.
- **CANDIDATE** — on the long candidate list but not yet committed to.
- **ARCHIVED** — superseded or retired; preserved for provenance.
- **SUPERSEDED** — replaced by a later paper or restructured.

---

## Cross-arc — The Dark Sector (`physics-papers/dark-sector/`)

ED's dark-matter position spans the gravity, cosmology, QFT, and substrate-evaluation arcs; the `dark-sector/` folder is the single findable synthesis so it is not read from fragments. **Key point for any reader:** "ED explains galaxies without dark matter" means *a particle is not needed for galaxies*, **not** that ED claims no dark matter — ED *does not refute a DM particle* (Paper_029/031). Clusters + CMB are a separate, mapped, addressable debt with a native candidate (a committed neutral relic), form-complete and value-inherited.

| Doc | Purpose | Status |
|---|---|---|
| `dark-sector/README.md` | folder overview + source-paper map | Synthesis |
| `dark-sector/Paper_ED_DarkSector_Position.md` | the canonical position (galaxy/cluster/CMB split; "MOND ≠ no particle"; the relic candidate; the open crux + falsifiers) | Synthesis |
| `dark-sector/DarkSector_DebtMap.md` | what clusters/CMB require, where MOND-class dies, ED's routes, proven vs open (public port of `event-density` Round-5) | Map |

---

## Cross-arc — State Reduction (`physics-papers/state-reduction/`)

The *measurement-side* companion to the dark sector: ED's position on gravitational collapse of the wavefunction, against its three nearest published neighbors (Diósi, Penrose, Hossenfelder). **Key point for any reader:** the neighbors say *gravity causes collapse* (scale in an energy `E_G`); ED says measurement-definiteness and gravitational time are **one primitive** — the arrow of commitment, which *is* the khronon — so the collapse variable is **time, not energy**. Post-referee status (2026-07-21): a scaling argument reproducing `τ ∝ ℏ/E_G` (coefficient open), one externally confirmed fork (difference-not-sum, vs Hossenfelder), and a retired 2020-experiment risk — its load-bearing residual now *resolved from the corpus* (ED's Lindblad jump operators are discrete channel projectors `Ĵ_α = g_α Π̂_α`, so committed states are exact fixed points → no continuous diffusion of a localized charge; immunity shared with QM, structural distinction real). Open pieces: the coefficient/energy-functional and the channel-granularity number.

| Doc | Purpose | Status |
|---|---|---|
| `state-reduction/README.md` | folder overview + source-paper map + open pieces | Synthesis |
| `state-reduction/Paper_ED_StateReduction_vs_CollapseModels.md` | the peer-facing positioning note (shared conviction; ED's account; the three neighbors; time-not-energy; gap, falsifiers, tiers) | Synthesis |
| `state-reduction/StateReduction_CollapseRate_ED_Derivation.md` | companion derivation: the `τ ∝ ℏ/E_G` scaling argument + the emission-signature analysis (why the 2020 bound does not exclude ED, honestly scoped) | Derivation |

---

## Arc 1 — Quantum Kinematics (Papers 001–012 + decimal extensions)

The Phase-1 QM-emergence program. Sixteen theorems closing the four standard quantum-mechanical postulates as substrate-derived results. **2026-07-02: 10 decimal-slot papers added** (found missing from the 2026-05-14 index) — supplementary derivations inserted between the integer papers; they do not renumber the integer sequence.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 001 | Pre-Individuation Amplitudes | foundations | WRITTEN | `Paper_001_PreIndividuation.md` |
| 002 | Tensor Product / Bipartite Mapping | foundations | WRITTEN | `Paper_002_TensorProduct.md` |
| 003 | Born Rule | foundations | WRITTEN | `Paper_003_BornRule.md` |
| 003.5 | Participation Measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ as Amplitude Carrier | foundations | WRITTEN | `physics-papers/qm-kinematics/Paper_003_5_ParticipationMeasure.md` |
| 004 | Gleason-Type Uniqueness | foundations | WRITTEN | `Paper_004_GleasonUniqueness.md` |
| 004.5 | Sesquilinear Inner-Product (Tsirelson Bound, Discrete) | foundations | WRITTEN | `physics-papers/qm-kinematics/Paper_004_5_Tsirelson_Discrete.md` |
| 004.6 | Inner-Product Extension to Continuum Configurations (Tsirelson, Continuum) | foundations | WRITTEN | `physics-papers/qm-kinematics/Paper_004_6_Tsirelson_Continuum.md` |
| 005 | Projective Measurement | measurement | WRITTEN | `Paper_005_ProjectiveMeasurement.md` |
| 005.5 | Double-Slit Experiment (four-mechanism composition) | measurement | WRITTEN | `physics-papers/qm-kinematics/Paper_005_5_DoubleSlit.md` |
| 006 | Unitary Evolution | dynamics | WRITTEN | `Paper_006_UnitaryEvolution.md` |
| 006.5 | Schrödinger Equation via Stone's Theorem | dynamics | WRITTEN | `physics-papers/qm-kinematics/Paper_006_5_Schrodinger_Stone.md` |
| 006.6 | Hamiltonian Form $\hat T = \hat p^2/(2m)$ (Factor-2 from Galilean Jacobian) | dynamics | WRITTEN | `physics-papers/qm-kinematics/Paper_006_6_HamiltonianForm.md` |
| 006.7 | Schrödinger Emergence in the Thin-Participation Limit | dynamics | WRITTEN | `physics-papers/qm-kinematics/Paper_006_7_ThinParticipationLimit.md` |
| 007 | Hilbert-Space Emergence | foundations | WRITTEN | `Paper_007_HilbertSpace.md` |
| 008 | Phase Structure / U(1) Cyclic Substructure | foundations | WRITTEN | `Paper_008_PhaseStructure.md` |
| 008 (legacy) | Kernel Arrow (early draft; content moved to Paper_093) | — | ARCHIVED | `Paper_008_KernelArrow.md` |
| 008.5 | Phase-Independence of Bandwidth Values | foundations | WRITTEN | `physics-papers/qm-kinematics/Paper_008_5_PhaseIndependence.md` |
| 009 | Berry Phase via Adiabatic Coarse-Graining | observables | WRITTEN | `Paper_009_BerryPhase.md` |
| 010 | Aharonov-Bohm Phase | observables | WRITTEN | `Paper_010_AharonovBohm.md` |
| 011 | Bloch Theorem from P10 Translation Symmetry | dynamics | WRITTEN | `Paper_011_BlochTheorem.md` |
| 011.5 | Four-QM-Postulates Unification under Participation Measure | foundations | WRITTEN | `physics-papers/qm-kinematics/Paper_011_5_FourPostulatesUnification.md` |
| 012 | RB-1: Rate of Becoming (substrate-c invariance) | dynamics | WRITTEN | `Paper_012_RB1_RateOfBecoming.md` |
| 012.5 | Momentum Operator $\hat p = -i\hbar\nabla$ as Translation Generator | dynamics | WRITTEN | `physics-papers/qm-kinematics/Paper_012_5_MomentumOperator.md` |
| 012.6 | Heisenberg Uncertainty $\Delta x\,\Delta p \ge \hbar/2$ from Four-Band Partition | dynamics | WRITTEN | `physics-papers/qm-kinematics/Paper_012_6_Heisenberg.md` |
| 012.7 | Adjacency-Bandwidth Asymmetry from Spatial Homogeneity (Galilean factor-2) | dynamics | WRITTEN | `physics-papers/qm-kinematics/Paper_012_7_AdjacencyBandwidth_Galilean.md` |

---

## Arc 2 — Form-Level QFT (Papers 013–024 + decimal extension)

Substrate-level QFT scaffolding. V1 spectral structure, T17 gauge fields, Yang–Mills arc, Lindblad open-system limit.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 013 | V1 Vacuum Kernel (Spectral + Form Factor) | kernels | WRITTEN | `Paper_013_V1_VacuumKernel.md` |
| 014 | V1 in Curved Acoustic Background | kernels | WRITTEN | `Paper_014_V1_CurvedBackground.md` |
| 015 | T17 — Gauge Fields as Rule-Type Bundles | gauge | WRITTEN | `Paper_015_T17_GaugeFields.md` |
| 015.5 | Photonic Chern-Quantization of Hall Drift | gauge | WRITTEN | `physics-papers/qft/Paper_015_5_Photonic_Chern_HallDrift.md` |
| 016 | Generalized Minimal Coupling (Non-Abelian) | gauge | WRITTEN | `Paper_016_MinimalCoupling.md` |
| 017 | Free Scalar QFT / Lorentz Covariantization | qft | WRITTEN | `Paper_017_FreeScalarQFT.md` |
| 018 | Yang–Mills YM-1: DCGT-NA Construction | yang-mills | WRITTEN | `Paper_018_YangMills1.md` |
| 019 | YM-2: Substrate→Continuum Action | yang-mills | WRITTEN | `Paper_019_YM2_SubstrateToContinuum.md` |
| 020 | YM-3: Osterwalder–Schrader Positivity | yang-mills | WRITTEN | `Paper_020_YM3_OSPositivity.md` |
| 021 | YM-4: Mass-Gap Mechanism (Coercivity) | yang-mills | WRITTEN | `Paper_021_YM4_MassGap.md` |
| 022 | YM-5: Gauge Orbits / Quotient Hilbert | yang-mills | WRITTEN | `Paper_022_YM5_GaugeQuotient.md` |
| 023 | YM-6: Clay-Relevance Synthesis | yang-mills | WRITTEN | `Paper_023_YM6_ClaySynthesis.md` |
| 024 | Lindblad Master Equation (Open-System Limit) | measurement | WRITTEN | `Paper_024_LindbladLimit.md` |

---

## Arc 3 — Gravity / Substrate Gravity (Papers 025–038 + decimal extensions)

Substrate-level derivations of Newton's law, a₀, ECR, BTFR slope-4, plus weak-field prerequisites and acoustic-metric covariantization.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 025 | Holographic Participation-Count Bound | holography | WRITTEN | `Paper_025_HolographicBound.md` |
| 026 | Cumulative-Strain Reading of P12 | foundations | WRITTEN | `Paper_026_CumulativeStrain.md` |
| 027 | Newton's $G = c^3\ell_P^2/\hbar$ | foundations | WRITTEN | `Paper_027_Newtons_G.md` |
| 027.5 | $\ell_{ED}^2 = \ell_P^2$ (Planck Identification) | foundations | WRITTEN | `physics-papers/gravity/Paper_027_5_NewtonRecovery_PlanckIdentification.md` |
| 028 | Cosmic Decoupling Surface $R_H = c/H_0$ | cosmology | WRITTEN | `Paper_028_CosmicDecoupling.md` |
| 029 | Transition Acceleration $a_0 = cH_0/(2\pi)$ | mond | WRITTEN | `Paper_029_a0.md` |
| 030 | ED Combination Rule $a = \sqrt{a_N a_0}$ | mond | WRITTEN | `Paper_030_CombinationRule.md` |
| 031 | BTFR Slope-4 $v^4 = GMa_0$ | galactic | WRITTEN | `Paper_031_BTFR.md` |
| 032 | Six Weak-Field Prerequisites | weak-field | WRITTEN | `Paper_032_WeakFieldPrereqs.md` |
| 032.5 | Free-Chain Geodesic Worldlines (FORCED-conditional) | gravity | WRITTEN | `physics-papers/gravity/Paper_032_5_FreeChainGeodesics.md` |
| 033 | Scalar-Tensor Acoustic-Metric Covariantization (Arc ED-10) | strong-field | WRITTEN | `Paper_033_AcousticMetric.md` |
| 034 | Deep MOND + Superluminality Cost | mond | WRITTEN | `Paper_034_DeepMOND.md` |
| 035 | Acoustic-Metric Guardrails (C1–C6) | strong-field | WRITTEN | `Paper_035_AcousticGuardrails.md` |
| 036 | Flat-Background MOND Field Equation | mond | WRITTEN | `Paper_036_MOND_FieldEquation.md` |
| 037 | $a_0$ Cosmological-Rate Invariance | mond | WRITTEN | `Paper_037_a0_Invariance.md` |
| 038 | Cosmological Implications (Substrate-Cosmology Decoupling) | cosmology | WRITTEN | `Paper_038_CosmologicalImplications.md` |
| 038.5 | Cosmological Constant $\Lambda$ as V1 Cosmological-Scale Integral | cosmology | WRITTEN | `physics-papers/gravity/Paper_038_5_Lambda_V1_Cosmological.md` |
| 038.6 | Weak-Lensing Activity Dependence | cosmology | WRITTEN (provisional prediction) | `physics-papers/gravity/Paper_038_6_Pred_WeakLensing_Activity.md` |

---

## Arc 4 — Black Holes / Hawking (Papers 039–052 + decimal extensions)

Arc BH + Arc Hawking. Horizon as decoupling surface, Hawking spectrum, trans-Planckian resolution, Planck-mass remnant Scenario C, area law, BHPT scattering, helicity, Page curve, info-paradox synthesis.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 039 | Horizon as Decoupling Surface ($\Gamma_{\text{cross}} \to 0$) | foundations | WRITTEN | `Paper_039_HorizonDecoupling.md` |
| 040 | Trans-Planckian Resolution via V5 Cutoff | hawking | WRITTEN | `Paper_040_TransPlanckian.md` |
| 041 | Planck-Mass Remnant Scenario C | remnants | WRITTEN | `Paper_041_RemnantMass.md` |
| 042 | No-Singularity from Substrate Cutoff | interior | WRITTEN | `Paper_042_NoSingularity.md` |
| 043 | Area-Law Form + $\log g$ Coefficient | thermodynamics | WRITTEN | `Paper_043_AreaLaw.md` |
| 044 | BHPT Scattering Structure | scattering | WRITTEN | `Paper_044_BHPT_Scattering.md` |
| 044.5 | Greybody Factors via Regge–Wheeler in DCGT (H-2) | scattering | WRITTEN | `physics-papers/black-hole/Paper_044_5_Greybody_ReggeWheeler.md` |
| 045 | Helicity Behavior at Horizons | scattering | WRITTEN | `Paper_045_Helicity.md` |
| 046 | Kerr Twist / Axisymmetric Substrate Geometry | rotating | WRITTEN | `Paper_046_KerrTwist.md` |
| 047 | Hawking Spectrum via Substrate-Unruh / KMS | hawking | WRITTEN | `Paper_047_HawkingSpectrum.md` |
| 047.5 | BH / Rindler / Cosmological / Acoustic Horizons as One Substrate Object | hawking | WRITTEN | `physics-papers/black-hole/Paper_047_5_HorizonUniversalization.md` |
| 048 | H-8: Higher-Order Resummation Selecting Scenario C | hawking | WRITTEN | `Paper_048_H8_Resummation.md` |
| 049 | H-9: Cosmological PBH Relic Abundance | remnants | WRITTEN | `Paper_049_PBH_RelicAbundance.md` |
| 050 | Page Curve via V5 Entanglement-Bandwidth | information | WRITTEN | `Paper_050_PageCurve.md` |
| 051 | Information Paradox Not Generated (Substrate Audit) | information | WRITTEN | `Paper_051_SubstrateAudit.md` |
| 052 | BH Information-Paradox Synthesis | information | WRITTEN | `Paper_052_BH_ParadoxSynthesis.md` |
| 052.5 | Merger-Lag Existence Prediction | black-hole | WRITTEN (provisional prediction) | `physics-papers/black-hole/Paper_052_5_Pred_MergerLag.md` |

**Addendum (2026-07-02, not decimal-numbered but same arc):** `The Hawking 2π From ED's Own Geometry` — derives Hawking's $2\pi$ from ED's own near-horizon Rindler geometry, completing $S=A/4$ as fully structural rather than half-inherited. `physics-papers/black-hole/BH_Thermal2Pi_FromNearHorizonRindler.md`.

---

## Arc 5 — Q-Compute / UR-1 (Papers 053–062)

Substrate origin of quantum-computing limits. $\mathcal{M}_{\text{cap}}$ as one substrate object; Class A/B/C exhaustiveness; UR-1 theorem; cross-platform unification via $\mathcal{M}_{\text{crit}}$; cross-domain echo with BH.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 053 | $\mathcal{M}_{\text{cap}}$ as One Substrate Object | foundations | WRITTEN | `Paper_053_Mcap.md` |
| 054 | UR-1 Theorem (Unresolved-Regime Characterization) | foundations | WRITTEN | `Paper_054_UR1.md` |
| 055 | A/B/C Architectural Exhaustiveness | classification | WRITTEN | `Paper_055_ABC_Exhaustiveness.md` |
| 056 | Class A Wall at 140–250 kDa (Matter-Wave) | predictions | WRITTEN | `Paper_056_ClassA_Wall.md` |
| 057 | Class B Exponential Gap-Suppression | predictions | WRITTEN | `Paper_057_ClassB_GapSuppression.md` |
| 058 | Class C Correlation-Budget Plateau | predictions | WRITTEN | `Paper_058_ClassC_Plateau.md` |
| 058b | Where the Plateau Binds: α_topological = 0, plateau domain = broadcast-type redundancy (settles ProxyConversionDoctrine §3.4; re-scopes prediction 4.10 to the repetition-code floor + cat-width ceiling pair) | q-compute | WRITTEN | `physics-papers/q-compute/Paper_058b_PlateauDomain_AlphaTopological.md` |
| 059 | Meta-Architectures as Compositions (EC, DD, hybrids) | architectures | WRITTEN | `Paper_059_MetaArchitectures.md` |
| 060 | $\mathcal{M}_{\text{crit}}$ Unification (Matter-Wave / Qubit) | unification | WRITTEN | `Paper_060_Mcrit_Unification.md` |
| 061 | Q-Compute Foundations Consolidated (Capstone) | capstone | WRITTEN | `Paper_061_QCompute_Foundations.md` |
| 062 | Cross-Domain Echo: BH ↔ Q-Compute V5-Saturation | cross-arc | WRITTEN | `Paper_062_CrossDomainEcho.md` |

---

## Arc 6 — Entanglement (Papers 063–072)

Bipartite entanglement architecture substrate-derived. Tensor product, Schmidt, monogamy via V5, no-signaling three-lock, Tsirelson, von Neumann entropy. Interpretive capstone identifying entanglement as the unresolved regime.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 063 | E-1: Tensor Product Structure | foundations | WRITTEN | `Paper_063_TensorProduct.md` |
| 064 | E-3: Schmidt Decomposition | foundations | WRITTEN | `Paper_064_SchmidtDecomposition.md` |
| 065 | E-4: Monogamy via V5 Cross-Chain Bandwidth | foundations | WRITTEN | `Paper_065_Monogamy.md` |
| 066 | E-5: No-Signaling Three-Lock | foundations | WRITTEN | `Paper_066_NoSignaling.md` |
| 067 | von Neumann Entropy — **MERGED into Paper_068 2026-07-05** (kept for provenance, do not cite) | foundations | SUPERSEDED | `Paper_067_VonNeumannEntropy.md` |
| 068 | E-6: von Neumann Entropy (canonical slot per Paper_087) | foundations | WRITTEN | `Paper_068_VonNeumannEntropy.md` |
| 069 | Bell–Tsirelson Polytope Reconstruction | foundations | WRITTEN | `Paper_069_TsirelsonReconstruction.md` |
| 070 | E-7: Bipartite Synthesis (Capstone) | capstone | WRITTEN | `Paper_070_BipartiteSynthesis.md` |
| 071 | ER=EPR-Class Structural Echo (Entanglement ↔ BH) | cross-arc | WRITTEN | `Paper_071_ER_EPR_Echo.md` |
| 072 | Entanglement as Unresolved Regime (Interpretive Capstone) | interpretation | WRITTEN | `Paper_072_IndividuationRegime.md` |

---

## Arc 7 — Soft Matter / Navier–Stokes / MHD (Papers 073–086 + decimal extension)

DCGT bridge, V5 viscoelastic, NS-1 dimensional forcing, NS-2 coarse-graining, NS-Smoothness Intermediate Path C, cascade, P4-NN rheology, NS-Q, NS-MHD closure, advection/induction non-ED, vortex-stretching obstruction, Universal Mobility Law.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 073 | DCGT — Diffusion Coarse-Graining Theorem | foundations | WRITTEN | `Paper_073_DCGT.md` |
| 074 | V5 Viscoelastic Maxwell Ansatz | viscoelasticity | WRITTEN | `Paper_074_V5_MaxwellAnsatz.md` |
| 075 | NS-1: Dimensional Forcing to $D = 3+1$ | foundations | WRITTEN | `Paper_075_NS1_DimensionalForcing.md` |
| 076 | NS-2: Substrate→Continuum Coarse-Graining | foundations | WRITTEN | `Paper_076_NS2_CoarseGraining.md` |
| 077 | NS-3: Smoothness via R1 (Intermediate Path C) | regularity | WRITTEN | `Paper_077_NS_Smoothness_R1.md` |
| 078 | NS-Turb: P7 ↔ Cascade | turbulence | WRITTEN | `Paper_078_NS_Turb_P7_Cascade.md` |
| 079 | P4-NN: Krieger–Dougherty + Maxwell Rheology | rheology | WRITTEN | `Paper_079_P4_NN_Rheology.md` |
| 080 | NS-Q Canonical $Q \approx 3.5$ | rheology | WRITTEN | `Paper_080_NS_Q_Factor.md` |
| 081 | NS-MHD H1/H2/H3 Closure | mhd | WRITTEN | `Paper_081_NS_MHD_Closure.md` |
| 082 | Advection / Induction Non-ED Triangulation | mhd | WRITTEN | `Paper_082_Advection_Induction_NonED.md` |
| 083 | Unified Kinematic-Coupling Pattern (NS / MHD) | mhd | WRITTEN | `Paper_083_KinematicCoupling.md` |
| 084 | Vortex-Stretching Obstruction at Substrate Level | regularity | WRITTEN | `Paper_084_VortexStretching.md` |
| 085 | Universal Mobility Law (Empirical Anchor) | mobility | WRITTEN | `Paper_085_UniversalMobilityLaw.md` |
| 086 | Soft-Matter Synthesis (Capstone) | capstone | WRITTEN | `Paper_086_SoftMatter_Synthesis.md` |
| 086.5 | Photonic Bandgap, Negative-Index, Cloaking via Two-Scale Expansion | soft-matter | WRITTEN | `physics-papers/soft-matter/Paper_086_5_Metamaterials_TwoScale.md` |

---

## Arc 8 — Wedges / Kernel Theory / Foundations (Papers 087–097)

Foundational substrate-level theorems and methodology. 13-primitive position paper, primitive load-bearing audit, V1/V5 canonical references, memory-kernel cascade, kernel hierarchy unification, T18 kernel-level arrow, forward-causal primitive structure, methodology formalization, cross-scale invariance, three-regime RG.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 087 | The 13 Primitives — Position Paper | foundations | WRITTEN | `Paper_087_13Primitives.md` |
| 088 | Primitive Load-Bearing Audit | foundations | WRITTEN | `Paper_088_PrimitiveAudit.md` |
| 089 | V1 Finite-Width Retarded Kernel (Canonical) | kernels | WRITTEN | `Paper_089_V1Kernel.md` |
| 090 | V5 Cross-Chain Correlation Kernel (Canonical) | kernels | WRITTEN | `Paper_090_V5Kernel.md` |
| 091 | Memory-Kernel Cascade Across Scales | kernels | WRITTEN | `Paper_091_KernelCascade.md` |
| 092 | Kernel Hierarchy Unification (Three-Index Classification) | kernels | WRITTEN | `Paper_092_KernelHierarchy.md` |
| 093 | T18 — Kernel-Level Arrow of Time | arrow | WRITTEN | `Paper_093_T18_ArrowOfTime.md` |
| 094 | Forward-Causal Substrate Primitive Structure | arrow | WRITTEN | `Paper_094_ForwardCausality.md` |
| 095 | Form-FORCED / Value-INHERITED Methodology | methodology | WRITTEN | `Paper_095_FormForced_ValueInherited.md` |
| 096 | Cross-Scale Invariance (ED-SC 3.x Canonical) | sc-arc | WRITTEN | `Paper_096_CrossScaleInvariance.md` |
| 097 | Three-Regime RG / 0.6 Problem | sc-arc | WRITTEN | `Paper_097_RG_0p6_Problem.md` |

---

## Program-Level Synthesis Papers (Papers 098–101)

Cross-arc synthesis and corpus-level capstones.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 098 | ED-QFT Unified Overview (Program Synthesis) | synthesis | WRITTEN | `Paper_098_EDQFT_Overview.md` |
| 099 | NS Synthesis Paper | synthesis | WRITTEN | `Paper_099_NS_Synthesis.md` |
| 100 | Five-Sector Program Overview (100-Paper Milestone Capstone) | capstone | WRITTEN | `Paper_100_FiveSector_ProgramOverview.md` |
| 101 | Falsification Register and Prediction Inventory (Corpus Capstone) | capstone | WRITTEN | `physics-papers/predictions/Paper_101_FalsificationRegister.md` (path updated 2026-07-02 — physically relocated during a predictions-folder consolidation; content unchanged) |

---

## Arc 9 — Relativistic QM (Papers 102–116) — ADDED 2026-07-02

Never indexed until this rebuild, though fully written. Spin-statistics, Cl(3,1) frame uniqueness, anyon prohibition, Dirac/Klein-Gordon equations, minimal coupling, Lorentz representations, canonical (anti-)commutation, UV finiteness, lightlike worldlines, ℏ-origin, mass structural form, gauge rule-type existence, vacuum-particle duality, the massless slot. All papers self-identify by an internal theorem/topic code (T1–T10, hbar, ArcM-H1, GRH-D1, Q7Q8, MRR-MRP) rather than by their filename number — the sequential 102–116 numbering was imposed externally when the arc was filed into the corpus, which is the source of the two irregularities noted below.

| # | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| 102 | RQM-T1 — Spin–Statistics $\eta = (-1)^{2s}$ in 3+1D | spin-statistics | WRITTEN | `physics-papers/relativistic-qm/Paper_102_SpinStatistics.md` |
| 103 | RQM-T2 — Cl(3,1) Frame Uniqueness up to Similarity | dirac/clifford-algebra | WRITTEN | `physics-papers/relativistic-qm/Paper_103_Cl31_FrameUniqueness.md` |
| 104 | RQM-T3 — Anyon Prohibition in 3+1D | spin-statistics/topology | WRITTEN | `physics-papers/relativistic-qm/Paper_104_AnyonProhibition.md` |
| 105 | *(gap — see note)* | — | MISSING | — |
| 106 | RQM-T4 — Dirac Equation $(i\gamma^\mu \partial_\mu - mc/\hbar)\Psi = 0$ | dirac | WRITTEN | `physics-papers/relativistic-qm/Paper_106_DiracEquation.md` |
| 107 | RQM-T5 — Klein–Gordon $(\square + m^2c^2/\hbar^2)\Psi = 0$ | klein-gordon | WRITTEN | `physics-papers/relativistic-qm/Paper_107_KleinGordon.md` |
| 108 | RQM-T6 — Minimal-Coupling Klein–Gordon + Conserved 4-Current | gauge/klein-gordon | WRITTEN | `physics-papers/relativistic-qm/Paper_108_MinimalCouplingKG.md` |
| 109 | RQM-T7 — Lorentz Representations from Primitives | kinematics/representation-theory | WRITTEN | `physics-papers/relativistic-qm/Paper_109_LorentzRepresentations.md` |
| 110 | RQM-T8 — Canonical (Anti-)Commutation Relations | quantization | WRITTEN | `physics-papers/relativistic-qm/Paper_110_CommutationRelations.md` |
| 111 | RQM-T9 — Primitive-Level UV Finiteness | qft/renormalization | WRITTEN | `physics-papers/relativistic-qm/Paper_111_UVFiniteness.md` |
| 112 | RQM-T10 — Lightlike Worldlines for $\sigma = 0$ Rule-Types | kinematics | WRITTEN | `physics-papers/relativistic-qm/Paper_112_LightlikeWorldlines.md` |
| 112 *(collision)* | RQM-hbar — ℏ-Origin in Chain-Step Participation Quantum | quantization/constants | WRITTEN | `physics-papers/relativistic-qm/Paper_112_hbar_Origin.md` |
| 113 | RQM-ArcM-H1 — Mass Structural Form (Arc-M H1-Dominant Regime) | mass-generation | WRITTEN | `physics-papers/relativistic-qm/Paper_113_ArcM_H1_MassStructuralForm.md` |
| 114 | RQM-GRH-D1 — Unconditional Existence of at Least One Massless Case-P Gauge Rule-Type | gauge | WRITTEN | `physics-papers/relativistic-qm/Paper_114_GRH_D1_P_Gauge.md` |
| 115 | RQM-Q7Q8 — Vacuum + Particle Dual Structure | qft/fock-space | WRITTEN | `physics-papers/relativistic-qm/Paper_115_Q7Q8_VacuumParticleDual.md` |
| 116 | RQM-MRR-MRP — Conditional Massless Slot via MR-R Chiral + MR-P Gauge | mass-generation/gauge | WRITTEN | `physics-papers/relativistic-qm/Paper_116_MRR_MRP_MasslessSlot.md` |

**Numbering irregularity, confirmed 2026-07-02, not yet fixed:** 15 papers exist for 15 nominal slots (102–116), but they land as 14 filled + 1 gap (105) + 1 collision (112, two distinct files). Neither collided file's own text claims "112" — both self-identify by their theorem/topic code only, so this is purely an artifact of external numbering, not a content conflict. The T-series (T1…T10) maps cleanly onto 102, 103, 104, 106–112 if `Paper_112_LightlikeWorldlines.md` (T10) keeps slot 112; `Paper_112_hbar_Origin.md` (a topic-coded companion paper, not part of the T-sequence, already cited elsewhere in the corpus as `Paper_RQM_hbar`) is the natural candidate to fill the 105 gap instead, which would resolve both irregularities at once. **Recommended, not yet executed** — renaming a corpus file is a bigger action than an index correction; do it only with explicit sign-off, and check for any other in-corpus citations by path first.

---

## Matter-Sector Arc (MS-I, MS-II) — ADDED 2026-07-02

Gauge groups, spin, chirality, and spatial dimensionality derived from channel multiplicity and the arrow (P11). Distinct naming convention (`Paper_MS-*`), no numbered slots consumed; lives in `physics-papers/qft/`.

| Paper | Title | Status | File |
|---|---|---|---|
| MS-I | Forces from Channels | ARCHIVED (superseded by MS-II; same treatment as `Paper_008_KernelArrow.md`) | `physics-papers/qft/Paper_MS-I_GaugeFromChannels.md` |
| MS-II | The Matter Sector from the Arrow | WRITTEN | `physics-papers/qft/Paper_MS-II_MatterSectorFromTheArrow.md` |

---

## Theorem Stubs (T19, T20, T21)

Recovered theorem-stub papers per Round 2 Phase B.2. Follow Paper_093 (T18 rewrite) template; introduce no new postulates.

| Theorem | Title | Status | File |
|---|---|---|---|
| T19 | Newton's $G$ Structural Role | WRITTEN | `T19.md` |
| T20 | $a_0$ Structural Role | WRITTEN | `T20.md` |
| T21 | BTFR Slope-4 Structural Form | WRITTEN | `T21.md` |

Together with T17 (Paper_015), T18 (Paper_093), GR1 + N1 (Paper_014), UR-1 (Paper_054), the corpus foundational-theorem inventory is complete.

---

## Cross-Arc Synthesis: SCBU

Round 3 Phase B.2 deliverable. Introduces P-Substrate-Cosmology-Unified (corpus's 125th paper-specific postulate).

| Title | Status | File |
|---|---|---|
| Substrate-Cosmology Boundary Unification (SCBU) | WRITTEN | `physics-papers/cosmology/Paper_SCBU_SubstrateCosmologyBoundary.md` (path updated 2026-07-02) |

---

## ED-SC 4.x Arc (Eleven-Paper Cross-Scale Extension)

Round 3 cross-scale extension arc. Identifies six SCBU-boundary projections within a unified four-regime RG model (UV / Transition / IR multi-sector / Cosmological), plus **five further papers (4.7–4.11) added 2026-07-02** extending the motif/GRF/saddle-classification/acoustic-curvature/spectral-moment statistics of the same framework.

| Paper | Title | Status | File |
|---|---|---|---|
| ED-SC 4.1 | BH Horizon ↔ Cosmic Decoupling Surface | WRITTEN | `Paper_ED_SC_4_1_BH_CosmicDecoupling.md` |
| ED-SC 4.2 | Substrate-Derivation of $\xi_{\text{canonical}}(H_0)$ | WRITTEN | `Paper_ED_SC_4_2_xi_canonical_H0_derivation.md` |
| ED-SC 4.3 | MOND/Galactic Scale ↔ SCBU IR Projection | WRITTEN | `Paper_ED_SC_4_3_MOND_SCBU.md` |
| ED-SC 4.4 | Q-Compute Platform Scale ↔ SCBU IR Projection | WRITTEN | `Paper_ED_SC_4_4_QCompute_SCBU.md` |
| ED-SC 4.5 | Soft-Matter NS-Q Scale ↔ SCBU IR Projection | WRITTEN | `Paper_ED_SC_4_5_SoftMatter_SCBU.md` |
| ED-SC 4.6 | Unified Cross-Scale Invariance (Capstone) | WRITTEN | `Paper_ED_SC_4_6_UnifiedCrossScale.md` |
| ED-SC 4.7 | Motif-Conditioned Distribution as Compositional Invariant | WRITTEN | `scale correspondence/Paper_ED_SC_4_7_MotifConditioned_Invariant.md` |
| ED-SC 4.8 | $r^*$ as FORCED Filtered-GRF Statistic (S1 Projection at Canonical Point) | WRITTEN | `scale correspondence/Paper_ED_SC_4_8_rstar_FilteredGRF.md` |
| ED-SC 4.9 | Saddle-Geometry Classification (S1 / S2 / S3) | WRITTEN | `scale correspondence/Paper_ED_SC_4_9_SaddleClassification.md` |
| ED-SC 4.10 | Acoustic-Metric Curvature Concentration on Mobility-Gradient Scale | WRITTEN | `scale correspondence/Paper_ED_SC_4_10_AcousticMetric_CurvatureConcentration.md` |
| ED-SC 4.11 | Spectral-Moment Classes ($\kappa$ Central, Model Band) — GR-SC F4 Sub-Arc | WRITTEN | `scale correspondence/Paper_ED_SC_4_11_GRSC_F4_SpectralMoment.md` |

All eleven papers sit at verdict tier M3 (FORM-FORCED + VALUE-INHERITED). Closing Paper_ED_SC_4.2 Route A (substrate-derived $\ell_{V5}(H_0)$) propagates to a **six-way simultaneous M3 → M2 verdict upgrade** across 4.1–4.6. Closing all three Routes A + B + C without additional postulates propagates to **M1** arc-wide — the first cross-arc M1 result in the corpus. *(4.7–4.11 were not independently re-audited for this same upgrade path as part of the 2026-07-02 index rebuild — flagged for a future pass.)* **Hygiene note:** a `scale invariance/` subfolder carries near-duplicate drafts of 4.7/4.8/4.9 differing only by date-stamp; not indexed separately, flagged for cleanup.

---

## Dynamics / Gravitational-Wave Arc — ADDED 2026-07-02

Saddle-Hessian dynamics as the generator of gravitational-wave, horizon-motion, radiation, collapse, inspiral, ringdown, and stochastic-background phenomena. Distinct naming convention (`Paper_ED_Dyn_*`, `Paper_ED_GW_*`), no numbered slots consumed; lives in `physics-papers/dynamics/`.

| Paper | Title | Status | File |
|---|---|---|---|
| GW-00 | Gravitational Waves as Propagating Saddle-Gradient Reconfigurations | WRITTEN (M3) | `physics-papers/dynamics/Paper_ED_GW_00_GravitationalWaves.md` |
| Dyn-01 | Saddle Dynamics: Foundational Framework | WRITTEN (M3) | `physics-papers/dynamics/Paper_ED_Dyn_01_SaddleDynamics.md` |
| Dyn-02 | Substrate-Graph Horizon-Motion Law via Non-Saturation Noether Stress-Energy | WRITTEN (M2) | `physics-papers/dynamics/Paper_ED_Dyn_02_HorizonMotion.md` |
| Dyn-03 | Substrate-Graph Radiation Law: EM Larmor and GW Quadrupole via Noether Flux + DCGT | WRITTEN (M2) | `physics-papers/dynamics/Paper_ED_Dyn_03_RadiationLaw.md` |
| Dyn-04 | Gravitational Collapse as Compression-Dominated Saddle-Signature Evolution | WRITTEN (M3) | `physics-papers/dynamics/Paper_ED_Dyn_04_GravitationalCollapse.md` |
| Dyn-05 | Inspiral Dynamics as Two-Saddle Coupled Evolution with Radiation Reaction | WRITTEN (M2 generic; M3 saturation-case) | `physics-papers/dynamics/Paper_ED_Dyn_05_InspiralDynamics.md` |
| GW-01 | Black-Hole Ringdown Spectroscopy as Time-Varying Saddle-Hessian-Signature Reconfiguration | WRITTEN (M3) | `physics-papers/dynamics/Paper_ED_GW_01_RingdownSpectroscopy.md` |
| GW-02 | Stochastic Gravitational-Wave Background as Cosmologically-Integrated Noether-Flux Output | WRITTEN (M2 net) | `physics-papers/dynamics/Paper_ED_GW_02_StochasticBackground.md` |

---

## Cosmology Arc — ADDED 2026-07-02

Inflation, BBN, CMB acoustic structure, linear structure formation, dark energy, the primordial fluctuation spectrum, baryogenesis, CCC identification, and group-embedded galaxy phenomenology, each as a substrate-inherited regime of the saturation/expansion history. Distinct naming convention (`Paper_ED_Cos_*` and related), no numbered slots consumed; lives in `physics-papers/cosmology/`.

| Paper | Title | Status | File |
|---|---|---|---|
| Cos-01 | Inflation as ED Diffusion Outpacing ED Production | WRITTEN (M3) | `physics-papers/cosmology/Paper_ED_Inflation.md` |
| Cos-02 | Big Bang Nucleosynthesis as Substrate-Inherited Freeze-Out Sequence | WRITTEN (M3) | `physics-papers/cosmology/Paper_ED_Cos_02_BBN.md` |
| Cos-03 | CMB Acoustic Peaks as Substrate-Inherited Baryon-Photon Oscillator | WRITTEN (M3) | `physics-papers/cosmology/Paper_ED_Cos_03_CMBAcoustic.md` |
| Cos-04 | Linear Structure Formation as Substrate-Inherited Growth of Primordial Perturbations | WRITTEN (M3) | `physics-papers/cosmology/Paper_ED_Cos_04_StructureFormation.md` |
| Cos-05 | Dark Energy as Late-Universe Substrate Saturation Regime | WRITTEN (M3, conditional on Route A for $\Lambda$ magnitude) | `physics-papers/cosmology/Paper_ED_Cos_05_DarkEnergy.md` |
| Cos-06 | Inflationary Fluctuation Spectrum as Sub-Leading Perturbations on the Saturation Regime | WRITTEN (M3) | `physics-papers/cosmology/Paper_ED_Cos_06_InflationarySpectrum.md` |
| — | Chain-Arrow Chirality, Admission Filter, and Stability Selection in the Post-SCBU Ignition Regime (baryogenesis) | WRITTEN (M3) | `physics-papers/cosmology/Paper_ED_Baryogenesis.md` |
| — | Group-Embedded Low-Acceleration Galaxies: DF2/DF4 | WRITTEN | `physics-papers/cosmology/Paper_ED_DF2_DF4_GroupSuppression.md` |
| — | ED Identification of Conformal Cyclic Cosmology | WRITTEN (M3) | `physics-papers/cosmology/Paper_ED_CCC_ConformalCyclicCosmology.md` |

**Excluded from this section (confirmed, not new papers):** `Paper_ED_Baryogenesis_Open.md` (superseded 2026-05-16 M2 draft; the current file above is the 2026-05-17 M3 version); five `Memo_ED_RouteA_*.md` internal audit memos.

---

## Layers Program — ADDED 2026-07-02

"The arrow sorts the continuum": one primitive (commitment, P11) sorts continuum PDEs into layer-1 (committal, structure-making — transport, coherent Maxwell), layer-2 (dissipative, structure-erasing — diffusion, viscosity, Gaussianity, one shared Laplacian operator), and the edge (structure-preserving, needs the arrow absent — solitons, a measured negative). Capstone paper `physics-papers/substrate-evaluation/Paper_TheArrowSortsTheContinuum.md` is already indexed in the Substrate-Evaluation Wave section below; this section indexes the working-notes arc it was built from, which lives in `layers/` and had never been indexed itself.

| Title | Status | File |
|---|---|---|
| The Layers — ED's Continuum Laws as a Hierarchy of Coarse-Grainings (overview) | WRITTEN | `layers/README.md` |
| Layer 1 — ED's Direct Coarse-Graining (overview) | WRITTEN | `layers/layer_1/README.md` |
| Transport / Eikonal — Layer-1 (ED's Native Continuum) | WRITTEN | `layers/layer_1/Transport_LayerOne.md` |
| Soliton Test — a Negative Result, and the Thesis Correction It Forces | WRITTEN | `layers/layer_1/Soliton_Test_NegativeResult.md` |
| Layer 2 — the Second Coarse-Graining (overview) | WRITTEN | `layers/layer_2/README.md` |
| Diffusion — Layer-2 Recovery | WRITTEN | `layers/layer_2/Diffusion_LayerTwo_Recovery.md` |
| Gaussianity — Two Layers, Two Answers | WRITTEN | `layers/layer_2/Gaussianity_TwoLayers.md` |
| Navier–Stokes — Layer-2, and Where the Edge Is | WRITTEN | `layers/layer_2/NavierStokes_LayerTwo.md` |
| Layer-2's Decorrelation Is One Operator — the Gradient-Flux Laplacian | WRITTEN | `layers/layer_2/OneOperator_TheLaplacian.md` |
| The Geometric Corner Is the Gravity Arc — and It's Already Measured | WRITTEN | `layers/Geometric_Gravity_Bridge.md` |
| The Atlas Through the Layers — and the Rule Refined | WRITTEN | `layers/Atlas_Sweep.md` |
| The Divide Is the Arrow — the Layers Program's Thesis | WRITTEN | `layers/Synthesis_TheDivideIsTheArrow.md` |

Excluded: `layers/plain_language_note.txt` (companion note, not a paper).

---

## Predictions / Falsification — ADDED 2026-07-02

Cross-corpus prediction consolidation and public falsification material, distinct from the per-paper Falsification Criteria sections and from Paper_101 (the original corpus-capstone register, now physically relocated to this same folder).

| Title | Status | File |
|---|---|---|
| Event Density — The Master Predictions List | WRITTEN | `physics-papers/predictions/ED_Master_Predictions_List.md` |
| 22 Ways to Kill Event Density (public falsification challenge) | WRITTEN | `physics-papers/predictions/22_Ways_to_Kill_Event_Density.md` |
| Empirical Predictions from a Substrate-Level Identification of $a_0=cH_0/(2\pi)$ | WRITTEN | `physics-papers/predictions/Paper_ED_Predictions_Bundle.md` |
| Passed Tests and Postdictions from a Substrate Cosmology Framework | WRITTEN | `physics-papers/predictions/Paper_ED_Postdictions_PassedTests.md` |
| Event Density — Predictions and Falsifiers (gravity-line one-page map) | WRITTEN | `physics-papers/gravity/Predictions_and_Falsifiers.md` |

Excluded: `Paper_ED_FRAP_Template.md` (an unfilled experimental protocol template, not a completed paper).

---

## Substrate-Evaluation Wave + Post-Pivot Gravity (June–July 2026)

Ten standalone papers from the substrate-evaluation program (build-and-run / theorem-anchored tests of the certified Σ-rule substrate) and the post-pivot Arc ED-10 curvature-emergence line. Distinct naming convention; no numbered slots consumed. Each paper carries a does-NOT-claim preamble, a P/D/I load-bearing audit, and falsifier sentences; `.pdf` builds accompany the `.md` sources.

| Paper | Title | Sub-domain | Status | File |
|---|---|---|---|---|
| GR-I | The Bandwidth Lapse and the Factor of Two: The Weak-Field Einstein Metric | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_GR-I_WeakFieldEinsteinMetric.md` |
| GR-II | The Arrow's Fingerprint: ED Gravity is Khronometric, GW-Clean, Lorentz-Safe | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_GR-II_KhronometricClass.md` |
| SE-Continuum | The Continuum Limit of the Certified ED Substrate: a Kinetic Lattice-Gas, not a Diffusion PDE | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_Continuum_KineticLatticeGas.md` |
| SE-BlindnessInvariant | Knots, Not Crystals: The Order Event Density Does Not Have, and the Order That Matters (the blindness/common-cause invariant, 5-arc; substrate carries no correlation-order, and the order that matters is topological — a knot, not a crystal) | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_BlindnessInvariant_KnotsNotCrystals.md` (+ `.pdf`) |
| SE-Primes | Template, Not Escape: Primes as a Ruler for the Finite-Memory Ceiling | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_FiniteMemoryCeiling_Primes.md` |
| SE-Charge | The Topological Skeleton of Charge: Quantized Winding and an Integral Gauss Law | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_ChargeAsTopology_B4.md` |
| SE-CleanVector | The Clean Substrate Is Vector: Parity Violation Is Necessarily Spontaneous, and the Weak Force's Chirality Is Inherited (successor to The Parity Wall; theorem = parity-clean transport is vector for every channel-count; casting inherited rep-theory) | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_CleanSubstrateVector_ParitySpontaneous.md` |
| SE-MassBinding | Mass Without Mass: Rest Mass and Inertia from V5-Binding of Massless Fronts, and Why Mass Is Not Time Dilation (binding mass native/V5-conditional; fundamental Higgs inherited; mass ≠ commitment-rate/time-dilation) | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_MassWithoutMass_BindingInertia.md` |
| SE-MaxwellShadow | Maxwell as an Emergent Shadow: the Charge Skeleton Is Native, the Coherence-Weighted Limit Is Coulomb, and the Smooth Field Is Coarse-Grained (closes B4 §7's open edge; smooth field a shadow, not a determinate-dynamics output — ED's monist ontology for EM) | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_MaxwellEmergentShadow.md` |
| SE-Capacity | Common Cause, Not Channel: The Determinability Boundary as an Observational Structure | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_CommonCauseNotChannel_A1.md` |
| SE-Boundary | Grown, Not Installed: An Emergent Decoupling Boundary Reproduces Exact Channel-Zero | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_GrownNotInstalled_A2.md` |
| SE-Layers | The Arrow Sorts the Continuum (layers-program capstone) | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_TheArrowSortsTheContinuum.md` |
| SE-Channels | From Worldlines to the Canonical PDE (bottom-up channel ledger; on hold) | substrate-evaluation | WRITTEN (program on hold) | `physics-papers/substrate-evaluation/Paper_CanonicalPDEChannels_BottomUp.md` |
| SE-V5Budget | The V5 Correlation Budget is One Envelope (monogamy + Page curve + Class-C plateau = one bounded W_max; R1 complexity-universal onset; R2 ratios 1:1:0.88 with ρ_loc=1 identity) | substrate-evaluation | WRITTEN | `physics-papers/substrate-evaluation/Paper_V5UnifiedBudget.md` |
| SE-QDBandwidth | Quantum Darwinism in ED: Committed Records Are Free, Live Redundancy Is Budgeted (fourth face of the V5 budget; accounting theorem; unbounded objectivity derived; conditional GHZ-width ceiling commensurate with the Class-C plateau) | substrate-evaluation | WRITTEN (Claude-B reviewed) | `physics-papers/substrate-evaluation/Paper_QuantumDarwinism_RecordBandwidth.md` |
| SE-ProxyDoctrine | The Proxy Conversion Doctrine (D1–D4: sharp-in-content/banded-in-proxy; per-architecture conversions; per-locus live content; pre-registered content rules — replaces five local patches; opens 058's α encoding-dependence) | substrate-evaluation | WRITTEN (Claude-B reviewed) | `physics-papers/substrate-evaluation/Paper_ProxyConversionDoctrine.md` |
| Form-and-Flesh | Form and Flesh: The Two Walls of the Event-Density Substrate (synthesis capstone) | position / synthesis | WRITTEN | `position-paper/Paper_FormAndFlesh_TwoWalls.md` |
| KM-I | The Arrow's Deep Field: Dark-Matter Phenomenology from the Khronon, and the Unification of ED Gravity | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_KM-I_KhrononMOND.md` |
| KM-II | The Arrow's Horizon: The Khronon's Cosmological Face — the Dark Fluid, the Clustering Dial, and One Λ | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_KM-II_KhrononCosmology.md` |
| GR-III | The Arrow's Engine: The Dynamical Rule of ED Gravity, and the Closing of Its Weak-Field Assumptions | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_GR-III_DynamicalRule.md` |
| GR-IV | The Arrow's Alibi: Preferred-Frame Safety and Quantum Coherence from Sparse Becoming (closes the α₁ front) | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_GR-IV_ArrowsAlibi.md` |
| ED-Gravity (PhilPapers) | The Arrow in the Law: Emergent Gravity from a Discrete, Irreversible Substrate (program synthesis, public-facing) | gravity / synthesis-paper | WRITTEN | `physics-papers/gravity/Paper_ED_Gravity_Program_PhilPapers.md` |
| One-Field | One Field: Gravity, Dark Matter, Dark Energy, and the Arrow of Time in ED (capstone letter) | gravity / synthesis-letter | WRITTEN | `physics-papers/gravity/Paper_OneField_Letter.md` |
| Metric-From-Graph | The Metric Comes Out of the Graph: Curvature, g ~ 1/b, and Why Only Three Dimensions (curvature-emergence foothold; reach law forced by the holographic count, GR-I metric unique to 3D, no new scale, isotropy emergent under CG) | gravity / curvature-emergence | WRITTEN | `physics-papers/gravity/Paper_MetricFromTheGraph_ForcedTo3D.md` |
| Bullet-TopologicalDefect | The Bullet Cluster as a Substrate Topological Defect: An ED Synthesis (Bullet_Arc phase-2; integrates the vacuum-manifold / winding-number / relaxation-time sub-results) | gravity / dark-matter phenomenology | WRITTEN | `physics-papers/gravity/Bullet_TopologicalDefect.md` (+ `.pdf`; further sources in `event-density/theory/Bullet_Cluster/`) |
| Offset-Velocity-Test | The Knee in the Data: An Experiment-Ready Test of the Offset-Velocity Law in Merging Clusters (Bullet_Arc phase-3; the mass-gas offset vs merger-velocity shape test, sharp knee vs LCDM scatter vs MOND ramp; real dataset + statistic named; velocity-selection feasibility finding) | gravity / dark-matter phenomenology (observational) | WRITTEN | `physics-papers/gravity/Paper_OffsetVelocityLaw_MergingClusterTest.md` (+ `.pdf`) |

Notes: GR-I/GR-II are the post-pivot curvature-emergence results, sharpening (not superseding) the Arc-3 scalar-tensor/MOND papers — see GR-I §7 / GR-II §9 for the explicit reconciliation. Form-and-Flesh is the program reach-statement (the empirical successor to the Contrast-First ontology paper) and lives in `position-paper/` alongside it. Underlying simulation artifacts live in the working repo (`event-density/evaluation/` and `event-density/foundations/`). **The Hawking-2π addendum lives with Arc 4 (Black Holes) above, not here, since its file path is `physics-papers/black-hole/`.**

---

## Position Papers — ADDED 2026-07-02

Foundational/ontological framing documents distinct from the per-domain derivation arcs. Live in `position-paper/`.

| Title | Status | File |
|---|---|---|
| Event Density: A Program Review (14-section map of the ~125-paper corpus, tiered; own Zenodo DOI) | WRITTEN | `position-paper/ED_Program_Review.md` (+ `.pdf`) |
| Event Density (front-door whitepaper) | WRITTEN | `position-paper/ED_WHITEPAPER.md` |
| When Contrast Becomes Fact — the Contrast-First Ontology ("the Facts paper") | WRITTEN | `position-paper/paper_ED_Contrast_First_Ontology.md` (**hygiene flag**: this file has no H1 heading, opens directly at `## Abstract` — a real source-file gap, not fixed as part of this index-only pass) |
| The Event Density Framework: A 13-Primitive Generative System and Its Cross-Domain Reach | WRITTEN | `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` |

Note: this third entry is a distinct document from `Paper_087_13Primitives.md` (Arc 8) — same underlying content genre, different framing/date, not a duplicate.

---

## Total counts (2026-07-02 rebuild)

- **Numbered Papers (001–101), including 21 decimal-slot extensions:** 122 WRITTEN + 1 ARCHIVED (008 legacy)
- **Arc 9 Relativistic QM (102–116):** 14 WRITTEN + 1 MISSING (105 gap) — 15 filename slots, 15 files (one slot, 112, doubly occupied)
- **Matter-Sector Arc (MS-I, MS-II):** 1 WRITTEN + 1 ARCHIVED
- **Theorem stubs (T19, T20, T21):** 3 WRITTEN
- **Cross-arc synthesis (SCBU):** 1 WRITTEN
- **ED-SC 4.x arc extensions (4.1–4.11):** 11 WRITTEN
- **Dynamics / GW arc:** 8 WRITTEN
- **Cosmology arc:** 9 WRITTEN
- **Layers program:** 12 WRITTEN
- **Predictions / Falsification:** 5 WRITTEN
- **Substrate-evaluation wave + post-pivot gravity:** 17 WRITTEN
- **Position papers:** 3 WRITTEN

**Grand total: 209 distinct corpus entities** (203 WRITTEN + 1 MISSING slot + 2 ARCHIVED + 1 doubly-occupied slot counted once above, net of the 105/112 irregularity). This is a large jump from the 2026-05-14 count of 124 — three entire arcs (Relativistic QM, Dynamics, Cosmology) plus the decimal-slot layer, the Layers program, five more scale-correspondence papers, three position papers, and a handful of loose files had simply never been added to this index, not newly written in the interim (most of these files carry May 2026 dates).

**Registry state (per Round-3 final rebuild, 2026-05-14 — NOT re-audited in the 2026-07-02 pass, flagged stale rather than guessed):**
- Paper-specific postulates: 125 (zero WARN-dup name collisions) — *as of 2026-05-14; almost certainly higher now given ~85 additional papers found since.*
- Foundational theorems: 8 (T17, T18, T19, T20, T21, GR1, N1, UR-1)
- Top-3 most-cited upstream papers: Paper_087 (96), Paper_090 (51), Paper_089 (49) — *as of 2026-05-14.*
- Orphan papers: 10 (as of 2026-05-14) — *not recomputed.*

---

## Domain ↔ Arc cross-reference

For migration purposes, the canonical arc structure maps to the domain partition as follows:

| Arc | Paper range | Domain | Sub-domains |
|---|---|---|---|
| 1 QM Kinematics | 001–012 (+ 10 decimal) | qm-kinematics | foundations, dynamics, observables, measurement |
| 2 Form-Level QFT | 013–024 (+ 1 decimal) | qft | kernels, gauge, yang-mills, measurement |
| 3 Gravity | 025–038 (+ 4 decimal) | gravity | foundations, mond, cosmology, strong-field, weak-field, galactic |
| 4 Black Holes / Hawking | 039–052 (+ 3 decimal, + 1 addendum) | black-hole | foundations, hawking, remnants, interior, thermodynamics, scattering, information |
| 5 Q-Compute | 053–062 | q-compute | foundations, classification, predictions, architectures, unification, cross-arc |
| 6 Entanglement | 063–072 | entanglement | foundations, capstone, cross-arc, interpretation |
| 7 Soft Matter / NS | 073–086 (+ 1 decimal) | soft-matter | foundations, viscoelasticity, regularity, turbulence, rheology, mhd, mobility |
| 8 Wedges / Foundations | 087–097 | cross-domain | foundations, kernels, arrow, methodology, sc-arc |
| Synthesis (program-level) | 098–101 | cross-domain | synthesis, capstone |
| 9 Relativistic QM | 102–116 (1 gap, 1 collision) | relativistic-qm | spin-statistics, dirac, klein-gordon, gauge, kinematics, quantization |
| Matter-Sector | MS-I, MS-II | qft | gauge, chirality, spin, dimensionality |
| T-stubs | T19/T20/T21 | gravity / cross-domain | theorem-stubs |
| Cross-arc synthesis | SCBU | cross-domain | substrate-cosmology |
| ED-SC 4.x extensions | 4.1–4.11 | cross-domain | sc-arc |
| Dynamics / GW | Dyn-01–05, GW-00–02 | dynamics | saddle-dynamics, radiation, collapse, inspiral, ringdown |
| Cosmology | Cos-01–06 + 3 named | cosmology | inflation, BBN, CMB, structure formation, dark energy, baryogenesis, CCC |
| Layers program | (working-notes arc) | substrate-evaluation | coarse-graining, layer-1, layer-2 |
| Predictions / Falsification | (cross-corpus) | cross-domain | predictions, falsifiers |
| Substrate-eval + post-pivot gravity | GR-I–IV, KM-I/II, SE-x, Form-and-Flesh, One-Field | gravity / substrate-evaluation / position | curvature-emergence, substrate-evaluation, synthesis |
| Position papers | (foundational framing) | cross-domain | ontology, primitives |

---

## Maintenance discipline

- **Each new paper:** add an entry here when promoted from CANDIDATE → PLANNED → DRAFTING → WRITTEN.
- **Round-numbered audit suffix `_FIXED`:** several files in the corpus carry a `_FIXED` suffix from Round 1 QC. The file paths in this index use the base name (no `_FIXED` suffix) for stability; treat `Paper_NNN_*.md` and `Paper_NNN_*_FIXED.md` as the same entity when both exist.
- **Cross-references in paper §3 sections:** reference papers by paper number (Paper_NNN) for in-corpus citations; by file path for repository-migration purposes.
- **Locked-in numbering:** the 001–101 numbering is stable as of 2026-05-14; **102–116 (Arc 9) added 2026-07-02**, with one known gap (105) and one known collision (112) not yet resolved (see Arc 9 section). T-stubs, SCBU, ED-SC 4.x, MS-I/II, Dynamics, Cosmology, and the Substrate-Evaluation Wave all use distinct naming conventions and do not consume numbered slots.
- **Decimal-slot convention (new, 2026-07-02):** supplementary papers inserted between integer slots (e.g. `012.6`) are genuine, complete papers, not drafts — file them under their parent arc's table at the position implied by the decimal, and do not renumber the surrounding integers to accommodate them.
- **Path-prefix inconsistency (flagged, not fixed):** the original 001–101 rows list bare filenames with no directory prefix, while every section added or touched since 2026-06 (Substrate-Evaluation Wave onward) uses full relative paths. The bare filenames are known to actually live under `physics-papers/<sub-domain>/` like everything else; retrofitting all ~101 legacy rows with full paths is a real but separate cleanup task, out of scope for this rebuild.
- **Registry source of truth:** for the live citation graph, postulate inventory, and numerical-value registry, see `event-density/papers/Forcing Papers/_RegistryRound2/` — **stale since 2026-05-14, not recomputed in this rebuild** (see Total counts section above).
- **2026-07-02 rebuild provenance:** this pass was a full repo scan (three parallel research agents, cross-verified against direct file reads) triggered by discovering the index was nearly two months stale. It is believed complete for the directories scanned (`physics-papers/*`, `position-paper/`, `layers/`, `scale correspondence/`, `predictions/`, root-level `.md` files) but was not cross-checked against `event-density/` (the working repo) beyond the specific loose files named above — the working repo has its own much larger body of in-progress notes that this index does not and should not attempt to track.

---

**End of Papers Index.**
