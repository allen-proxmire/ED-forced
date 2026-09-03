# Relativistic-QM — Folder Guide

**What this folder is.** The relativistic quantum-mechanics arc (RQM, theorems T1–T10 + extensions): the Dirac and Klein-Gordon equations, spin-statistics, Lorentz representations, anyon prohibition in 3+1D, UV finiteness, the ℏ-origin, and the (partly open) mass and gauge structure — all from the substrate. This arc classifies the Weyl/Dirac representations and builds the relativistic wave equations; it is also where the **matter-sector spinor gate (Paper_106 / T4)** lives, which the whole chiral-gauge frontier (#2b) reduces to.

**State** *(authoritative source: `event-density/docs/ED_Research_Targets.md`, targets #2b + the RQM notes; PAPERS_INDEX)*:
- **Most of the arc is grounded/closed** — spin-statistics, frame uniqueness, anyon prohibition (two M1 pure-structural results), the wave equations, Lorentz reps, UV finiteness.
- **The load-bearing open edge is Paper_106 (T4, the Dirac equation):** the *structural mechanism* is identified (M2), but the explicit substrate-V1 → Dirac closed derivation — the emergent spinor — is **OPEN**. This is the T4 gate the chiral-gauge/parity frontier (#2b) reduces to; the single highest-leverage open item in the matter sector.
- **Also open:** the mass sector (Paper_113 — substrate-Higgs / substrate-Yukawa asserted, not derived) and P-Gauge existence (Paper_114 — the substrate derivation of P-Gauge is open).
- **Values inherited:** `ℏ` (Paper_112_hbar, structural origin identified but value inherited) and the canonical commutation constant (Paper_110).

**Tier key:** `Derived` (M1, pure structural / from primitives) · `Grounded` (M2/M3 — mechanism identified or form-forced) · `Inherited` (value from measurement, e.g. `ℏ`) · `Open` (the declared open edge — T4 spinor, mass, P-Gauge).

---

## The spine — read in this order

1. **[103 Cl(3,1) Frame Uniqueness (T2)](Paper_103_Cl31_FrameUniqueness.md)** — the spacetime Clifford algebra frame, up to similarity (M1).
2. **[102 Spin-Statistics (T1)](Paper_102_SpinStatistics.md)** — `η = (−1)^{2s}` in 3+1D.
3. **[104 Anyon Prohibition (T3)](Paper_104_AnyonProhibition.md)** — no anyons in 3+1D (M1).
4. **[106 The Dirac Equation (T4)](Paper_106_DiracEquation.md)** — the Dirac equation; **the open spinor gate** (see #2b).
5. **[107 Klein-Gordon (T5)](Paper_107_KleinGordon.md)** — the relativistic scalar equation.
6. **[109 Lorentz Representations (T7)](Paper_109_LorentzRepresentations.md)** — the Lorentz reps from primitives.

---

## Papers by sub-arc

### Relativistic kinematics & structure
| # | Paper | Result | Tier |
|---|---|---|---|
| 102 | [Spin-Statistics (T1)](Paper_102_SpinStatistics.md) | `η = (−1)^{2s}` in 3+1D (form-forced, value-inherited) | Grounded (M3) |
| 103 | [Cl(3,1) Frame Uniqueness (T2)](Paper_103_Cl31_FrameUniqueness.md) | the spacetime Clifford frame is unique up to similarity | Derived (M1) |
| 104 | [Anyon Prohibition (T3)](Paper_104_AnyonProhibition.md) | no anyons in 3+1D (pure dimension-comparison) | Derived (M1) |
| 109 | [Lorentz Representations (T7)](Paper_109_LorentzRepresentations.md) | the Lorentz representations from the primitives | Grounded (M3) |
| 110 | [Canonical (Anti-)Commutation (T8)](Paper_110_CommutationRelations.md) | the canonical (anti-)commutation relations (form + value inherited) | Grounded / Inherited |

### The relativistic wave equations
| # | Paper | Result | Tier |
|---|---|---|---|
| 106 | [The Dirac Equation (T4)](Paper_106_DiracEquation.md) | `(iγ^μ∂_μ − mc/ℏ)Ψ = 0` — mechanism identified; **substrate-V1 → Dirac derivation OPEN (the #2b spinor gate)** | Grounded (M2); **Open** |
| 107 | [Klein-Gordon (T5)](Paper_107_KleinGordon.md) | `(□ + m²c²/ℏ²)Ψ = 0` (form-inherited, conditional on 017 + 095) | Grounded (M3) |
| 108 | [Minimal-Coupling Klein-Gordon (T6)](Paper_108_MinimalCouplingKG.md) | minimal-coupling KG + the conserved 4-current | Grounded (M3) |

### Finiteness, worldlines, vacuum, ℏ
| # | Paper | Result | Tier |
|---|---|---|---|
| 111 | [Primitive-Level UV Finiteness (T9)](Paper_111_UVFiniteness.md) | UV finiteness from the finite-width kernel | Grounded (M3) |
| 112 | [Lightlike Worldlines (T10)](Paper_112_LightlikeWorldlines.md) | lightlike worldlines for `σ=0` rule-types (conditional on Paper_114) | Grounded (M3) |
| 112h | [ℏ-Origin](Paper_112_hbar_Origin.md) | `ℏ` from the chain-step participation quantum (value inherited, structural origin) | Grounded / Inherited |
| 115 | [Vacuum + Particle Dual Structure (Q7/Q8)](Paper_115_Q7Q8_VacuumParticleDual.md) | the vacuum + particle dual structure | Grounded (M3) |

### Mass & gauge sector (open)
| # | Paper | Result | Tier |
|---|---|---|---|
| 113 | [Mass Structural Form (Arc-M H1)](Paper_113_ArcM_H1_MassStructuralForm.md) | the mass structural form; **substrate-Higgs / substrate-Yukawa asserted, not derived** | Grounded (M2); **Open** |
| 114 | [Massless Case-P Gauge Existence (GRH-D1)](Paper_114_GRH_D1_P_Gauge.md) | existence of ≥1 massless Case-P gauge rule-type; **P-Gauge substrate-derivation OPEN** | Grounded (M2); **Open** |
| 116 | [Conditional Massless Slot (MR-R + MR-P)](Paper_116_MRR_MRP_MasslessSlot.md) | a conditional massless slot via MR-R chiral + MR-P gauge | Grounded (M3) |

*(No non-paper docs. The T4 Dirac/spinor gate (106) is the corpus's central open matter-sector item — see `event-density/docs/ED_Research_Targets.md` #2b.)*

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[`RelativisticQM_TieredClaims_Ledger.md`](RelativisticQM_TieredClaims_Ledger.md)** — the arc's **tiered-claims ledger**: every load-bearing claim in this folder with its current tier. It doubles as the arc's staleness detector — where a paper and the ledger disagree, the ledger's `Status` column is the current state. Read it before citing anything here.
