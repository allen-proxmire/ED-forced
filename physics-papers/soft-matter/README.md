# Soft-Matter — Folder Guide *(fluids, Navier-Stokes, rheology, DCGT)*

**What this folder is.** The soft-matter / continuum-fluids sector, and the home of the **DCGT (Diffusion Coarse-Graining Theorem, Paper_073)** — the substrate→continuum bridge invoked across the whole corpus. It covers the Navier-Stokes program (dimensional forcing to 3+1, the smoothness question, the turbulence cascade, vortex stretching), rheology (Krieger-Dougherty + Maxwell viscoelastic), MHD closure, the data-matched universal mobility law (a postdiction), and metamaterials.

**State** *(sources: `event-density/docs/ED_Research_Targets.md` — soft-matter is in the CLOSED column; targets #3, #5; PAPERS_INDEX)*:
- **The arc is CLOSED.** DCGT (073) is the foundational coarse-graining theorem the rest of the corpus builds on.
- **Navier-Stokes:** dimensional forcing to 3+1 (075), the substrate→continuum bridge (076), a smoothness mechanism (077, Clay-adjacent), and the turbulence cascade (078). Grounded/conditional (declared PDE-uniqueness axioms).
- **The universal mobility law (085) is data-matched (a postdiction)** — the constitutive law `M ∝ (ρ_max − ρ)^β` matched across 11 materials (`R² = 0.986`–`0.999`) from existing published data; the empirical anchor of the sector (and the capacity ingredient of the UDM, target #3). *(Self-authored Zenodo preprint, **not** peer-reviewed; the FRAP forward test is not yet run — see `predictions/Paper_ED_FRAP_Template.md`.)*
- **Honest boundary:** Paper_082 triangulates **advection and kinematic induction as *non-ED-native*** — lossy ≠ wrong; not every continuum effect is a direct substrate shadow.
- **`Q ≈ 3.5` (080)** is canon-internal (one of SCBU's six projections, #5), not derived from primitives.

**Tier key:** `Grounded` (conditional/structural, M2/M3) · `Measured` (matches existing data, e.g. the mobility-law postdiction) · `Inherited` (a value from the standard form) · `Synthesis` · `Non-ED` (triangulated as not substrate-native — an honest boundary).

---

## The spine — read in this order

1. **[073 DCGT — Diffusion Coarse-Graining Theorem](Paper_073_DCGT.md)** — the substrate→continuum bridge (used everywhere). **Start here.**
2. **[076 NS-2: Substrate→Continuum Bridge](Paper_076_NS2_CoarseGraining.md)** — coarse-graining into the Navier-Stokes form.
3. **[075 NS-1: Dimensional Forcing to 3+1](Paper_075_NS1_DimensionalForcing.md)** — why the fluid PDE lives in 3+1.
4. **[077 NS-Smoothness](Paper_077_NS_Smoothness_R1.md)** — the smoothness mechanism (Clay-adjacent).
5. **[085 Universal Mobility Law](Paper_085_UniversalMobilityLaw.md)** — the data-matched constitutive anchor (a postdiction; self-published, not peer-reviewed).

---

## Papers by sub-arc

### Foundations
| # | Paper | Result | Tier |
|---|---|---|---|
| 073 | [DCGT — Diffusion Coarse-Graining Theorem](Paper_073_DCGT.md) | the substrate→continuum coarse-graining theorem (the corpus's continuum bridge) | Grounded (M3) |
| 074 | [V5 Viscoelastic Maxwell Ansatz](Paper_074_V5_MaxwellAnsatz.md) | the viscoelastic Maxwell ansatz, substrate-grounded | Grounded |
| 076 | [NS-2: Substrate→Continuum Bridge](Paper_076_NS2_CoarseGraining.md) | the coarse-graining bridge to the Navier-Stokes equations | Grounded |

### Navier-Stokes / turbulence
| # | Paper | Result | Tier |
|---|---|---|---|
| 075 | [NS-1: Dimensional Forcing to 3+1](Paper_075_NS1_DimensionalForcing.md) | the fluid PDE forced to D=3+1 (seven PDE-uniqueness axioms) | Grounded |
| 077 | [NS-Smoothness (R1)](Paper_077_NS_Smoothness_R1.md) | a smoothness mechanism (Clay-adjacent; intermediate path C) | Grounded |
| 078 | [NS-Turbulence: P7 ↔ Cascade](Paper_078_NS_Turb_P7_Cascade.md) | the turbulence cascade from the P7 structure | Grounded |
| 084 | [Vortex-Stretching Obstruction](Paper_084_VortexStretching.md) | the vortex-stretching obstruction at the substrate level | Grounded |

### Rheology, MHD, mobility
| # | Paper | Result | Tier |
|---|---|---|---|
| 079 | [P4-NN Rheology](Paper_079_P4_NN_Rheology.md) | Krieger-Dougherty + Maxwell viscoelastic rheology | Grounded |
| 080 | [NS-Q: `Q ≈ 3.5`](Paper_080_NS_Q_Factor.md) | the canonical `Q ≈ 3.5` factor (canon-internal; an SCBU projection) | Grounded (Inherited) |
| 081 | [NS-MHD Closure](Paper_081_NS_MHD_Closure.md) | the NS-MHD H1/H2/H3 closure | Grounded |
| 082 | [Advection & Induction (non-ED)](Paper_082_Advection_Induction_NonED.md) | advection and kinematic induction triangulated as **not substrate-native** | **Non-ED** (honest boundary) |
| 083 | [Kinematic Coupling Across NS/MHD](Paper_083_KinematicCoupling.md) | the kinematic coupling pattern across NS/MHD | Grounded |
| 085 | [Universal Mobility Law](Paper_085_UniversalMobilityLaw.md) | `M ∝ (ρ_max − ρ)^β`, matched across 11 materials (`R² > 0.986`) | **Measured** (empirical anchor) |

### Applications & synthesis
| # | Paper | Result | Tier |
|---|---|---|---|
| 086.5 | [Metamaterials (Two-Scale)](Paper_086_5_Metamaterials_TwoScale.md) | photonic bandgap, negative-index, cloaking from the substrate via two-scale expansion | Grounded (M2) |
| 086 | [Soft-Matter Synthesis](Paper_086_SoftMatter_Synthesis.md) | the soft-matter arc consolidated | Synthesis |

*(No non-paper docs. DCGT (073) is the continuum bridge the whole corpus depends on; the mobility law (085) is the sector's empirical anchor; 082 marks an honest non-ED boundary.)*

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[Resistivity Saturation as a Grain-Floored Mott–Ioffe–Regel Limit](Paper_P04TransportBudget_ResistivitySaturation.md)**
- **[The Unified P04 Transport Budget](Paper_UnifiedP04TransportBudget.md)**

---

## ⚠ This arc has no tiered-claims ledger — flagged 2026-09-04

Every other content arc in `physics-papers/` carries a `*_TieredClaims_Ledger.md`: the arc's claim inventory, tier assignments, open items and staleness log. **`soft-matter/` does not.** It has 18 papers and no ledger.

**This is why the arc was invisible to the 2026-09-04 claim-strength audit.** That pass swept the fifteen arc ledgers and reported covering “all fifteen arcs”; the count was of *ledgers*, and an arc with no ledger was never in the set. **So soft-matter is a sixteenth content arc that has not been audited, and was not recorded as unaudited either.** See `internal notes/AUDIT_2026-09-04_ClaimStrength_AllArcs.md` and gravity ledger Staleness #54.

The arc carries load-bearing content: `Paper_077_NS_Smoothness_R1` and `Paper_084_VortexStretching` are one of the two executed results behind research target #15's singularity family, and `Paper_086_SoftMatter_Synthesis` was flagged 2026-09-04 for quoting `ξ_canonical` to unsupported precision. **Creating the ledger is the natural next task for this arc.**

## An SCBU projection into this arc

`cosmology/Paper_ED_SC_4_5_SoftMatter_SCBU.md` projects the **NS-Q canonical operating point `Q ≈ 3.5`** (`Paper_080`) onto the substrate–cosmology boundary `R_H = c/H₀`, as one of six `ED-SC 4.x` projections unified by `Paper_ED_SC_4_6`. Migrated 2026-09-04 from a fork frozen 2026-07-05. `Q ≈ 3.5` is **canon-internal** by the paper's own statement, alongside platform-specific `τ_M` and per-material mobility coefficients, and the paper carries the disputed `2π` (flagged in place). **M3, unaudited** — treat the projection's structure as the claim and the numbers as inherited.
