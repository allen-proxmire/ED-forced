# QM-Kinematics — Folder Guide

**What this folder is.** The Phase-1 program: **quantum mechanics emerges from the substrate primitives.** The four QM postulates (state space, composition, the Born rule, measurement, unitary evolution) and the core quantum phenomena (interference, Berry/Aharonov-Bohm phases, Bloch, Heisenberg, the momentum operator) are derived — or grounded with a named inherited value — from the 13 primitives (Paper_087), with no quantum structure assumed at the start.

**State of the arc** *(authoritative source: `event-density/docs/ED_Research_Targets.md`, target #8b; PAPERS_INDEX Arc 1)*:
- **The QM-emergence arc is CLOSED** — the four postulates and the standard phenomena are substrate-derived (a 16-theorem program).
- **The one open residual is the inner product / Gleason step** (Paper_004, Paper_007): the sesquilinear form is grounded *conditional on* two added postulates (P-Channel-Orthogonality, P-Gleason-Compatibility). **Current status (updated 2026-07-29):** the Gleason keystone reconstruction (`../substrate-evaluation/Paper_QuantumLogicKeystone_GleasonReconstruction.md`) has **reduced** channel-orthogonality to channel-distinctness *given the representation* (operational distinguishability), **selected ℂ** from the Solèr menu, and **discharged** the equal-norm condition (2026-07-10), narrowing the residual to the **Solèr lattice technical rigor alone** — i.e. **"reduced to the Solèr residual,"** stronger than Paper_004's earlier "blocking/three-routes-fail" but still short of a closed uniqueness theorem. *(Papers 004/007 carry the earlier "blocking" wording with dated update pointers to the reconstruction.)* So the inner product is the honest open edge of an otherwise-closed arc — now a technical Solèr residual, not a structural block.
- **Values inherited:** `ℏ` (form-identified in the operator papers, value inherited — see 012.5 / 012.6).

**Tier key** *(ED's own verdict tiers, from each paper's audit)*:
`Derived` (M1, from primitives) · `Grounded` (M2/M3 — structural/conditional; form-forced with an identified or inherited value) · `Inherited` (a value from measurement, e.g. `ℏ`) · `Synthesis` (compositional unification) · `Open` (the declared open edge). *(Verify against the paper's own status line before quoting; most here self-declare M2 or M3.)*

---

## The spine — read in this order

The clean path through the postulate emergence:

1. **[001 Pre-Individuation Amplitudes](Paper_001_PreIndividuation.md)** — amplitudes from P01–P04 (upstream of the Born rule).
2. **[003 The Born Rule](Paper_003_BornRule.md)** — probability = participation-frequency limit (the arc's anchor).
3. **[002 Tensor-Product Composition](Paper_002_TensorProduct.md)** — composite systems from P02 + P03.
4. **[005 Projective Measurement](Paper_005_ProjectiveMeasurement.md)** — measurement from P11 commitment.
5. **[006 Unitary Evolution](Paper_006_UnitaryEvolution.md)** — evolution from V1 kernel propagation.
6. **[007 Hilbert-Space Emergence](Paper_007_HilbertSpace.md)** — the state space as completion of the motif algebra (closes the 001→003→007 loop).
7. **[011.5 Four-Postulates Unification](Paper_011_5_FourPostulatesUnification.md)** — the four postulates under one participation measure.

---

## Papers by sub-arc

### The four QM postulates (the core emergence)
| # | Paper | Result | Tier |
|---|---|---|---|
| 001 | [Pre-Individuation Amplitudes](Paper_001_PreIndividuation.md) | amplitudes from P01–P04, upstream of the Born rule | Grounded |
| 002 | [Tensor-Product Composition](Paper_002_TensorProduct.md) | composite systems — the composition postulate | **Postulated** (P-QMkin-Composition; not from P02+P03 alone, per the paper's own audit) |
| 003 | [The Born Rule](Paper_003_BornRule.md) | probability as the participation-frequency limit | **Grounded** (rests on P-LinRate + a frequentist assumption, per the paper's own audit) |
| 003.5 | [Participation Measure](Paper_003_5_ParticipationMeasure.md) | `P_K = √b_K · e^{iπ_K}` as the amplitude carrier | Grounded (M3) |
| 005 | [Projective Measurement](Paper_005_ProjectiveMeasurement.md) | measurement/collapse from P11 commitment | Grounded |
| 006 | [Unitary Evolution](Paper_006_UnitaryEvolution.md) | unitarity from V1 kernel propagation | Grounded |
| 007 | [Hilbert-Space Emergence](Paper_007_HilbertSpace.md) | the state space = Cauchy completion of the motif algebra (inner product Inherited at this level) | Grounded (inner product Open, #8b) |

### Amplitude & the inner product (the open edge)
| # | Paper | Result | Tier |
|---|---|---|---|
| 004 | [Gleason-Type Uniqueness](Paper_004_GleasonUniqueness.md) | substrate Gleason from P07 + P08 — **partial**; the sesquilinear form is conditional on two added postulates | Grounded / **Open** (#8b) |
| 004.5 | [Sesquilinear Inner-Product (Tsirelson, discrete)](Paper_004_5_Tsirelson_Discrete.md) | the discrete Tsirelson-bound inner product | Grounded (M3) |
| 004.6 | [Inner-Product Extension (Tsirelson, continuum)](Paper_004_6_Tsirelson_Continuum.md) | continuum-configuration inner product | Grounded (M3) |

### Dynamics — Schrödinger, Hamiltonian, operators
| # | Paper | Result | Tier |
|---|---|---|---|
| 006.5 | [Schrödinger via Stone's Theorem](Paper_006_5_Schrodinger_Stone.md) | the Schrödinger equation (substrate identification is the load-bearing step) | Grounded (M2) |
| 006.6 | [Hamiltonian Form](Paper_006_6_HamiltonianForm.md) | `T̂ = p̂²/2m`, the factor-2 from the Galilean Jacobian | Grounded (M3) |
| 006.7 | [Thin-Participation Limit](Paper_006_7_ThinParticipationLimit.md) | Schrödinger emergence in the thin-participation limit | Grounded (M2) |
| 012.5 | [Momentum Operator](Paper_012_5_MomentumOperator.md) | `p̂ = −iℏ∇` as the translation generator (form-identified; `ℏ` inherited) | Grounded; ℏ Inherited |
| 012.6 | [Heisenberg Uncertainty](Paper_012_6_Heisenberg.md) | `Δx·Δp ≥ ℏ/2` from the four-band partition (form-forced; `ℏ/2` inherited) | Grounded; value Inherited |
| 012.7 | [Adjacency-Bandwidth Asymmetry](Paper_012_7_AdjacencyBandwidth_Galilean.md) | the Galilean adjacency-bandwidth asymmetry from spatial homogeneity | Grounded (M3) |
| 012 | [Rate of Becoming (P-RB-1)](Paper_012_RB1_RateOfBecoming.md) | the local rate of becoming and its coarse-grainings | Grounded |

### Phase phenomena
| # | Paper | Result | Tier |
|---|---|---|---|
| 008 | [Phase Structure](Paper_008_PhaseStructure.md) | phase on rule-types from P09 + P10 | Grounded |
| 008.5 | [Phase-Independence of Bandwidth](Paper_008_5_PhaseIndependence.md) | phase-independence = the `U(1)` gauge invariance | Grounded (M3) |
| 009 | [Berry Phase](Paper_009_BerryPhase.md) | Berry phase as holonomy of the substrate connection | Grounded / Derived |
| 010 | [Aharonov–Bohm](Paper_010_AharonovBohm.md) | the AB phase from rule-type circulation | Grounded / Derived |
| 011 | [Bloch Theorem](Paper_011_BlochTheorem.md) | Bloch's theorem from P10 substrate translation symmetry | Grounded / Derived |

### Interference & unifications
| # | Paper | Result | Tier |
|---|---|---|---|
| 005.5 | [Double-Slit Experiment](Paper_005_5_DoubleSlit.md) | interference `\|P_A + P_B\|²` from the participation amplitudes | Grounded |
| 011.5 | [Four-Postulates Unification](Paper_011_5_FourPostulatesUnification.md) | the four QM postulates unified under the participation measure | Synthesis (M2) |

*(No non-paper docs in this folder. `ℏ` is the one inherited value in the operator sub-arc.)*
