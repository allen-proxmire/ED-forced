# QFT — Folder Guide *(fields, gauge, Yang-Mills, the matter sector)*

**What this folder is.** The field-theory sector: how quantum field theory, gauge fields, and the Standard-Model-facing matter structure emerge from the substrate. Free scalar QFT as the continuum limit of the V1 kernel; gauge fields as rule-type bundles; the Yang-Mills arc (non-abelian generalization → OS positivity → the mass-gap mechanism → Clay relevance); open-system dynamics (Lindblad from V5); and the matter sector (**MS-I / MS-II**: gauge groups from channel multiplicity, the spinor, chirality from the arrow, and the three-generation/dimension count).

**State** *(authoritative source: `event-density/docs/ED_Research_Targets.md`, targets #2b + the YM notes; PAPERS_INDEX)*:
- **QFT emergence + gauge structure are grounded** — free scalar QFT (017), gauge-as-bundles (015/T17), minimal coupling (016).
- **Yang-Mills:** the substrate mechanisms are structural (018–022); the **mass-gap has a verified structural core** (non-abelian `[A,A]` lifts the abelian flat direction) but **continuum survival is the Clay-hard wall** — Open. (023 is the Clay-relevance synthesis, not a claim of proof.)
- **The matter sector is the open research frontier (#2b)** — MS-I/MS-II assemble what ED's substrate carries (gauge groups from multiplicity, parity from the non-abelian sector, the spinor), but the Standard-Model completion (why chirality, the `{1,2,3}` multiplicities, anomaly cancellation) reduces to the **T4 spinor gate** and is *not closed*. This is the highest-leverage open item in the whole program.
- **Values inherited:** platform-specific Chern numbers (015.5), and coupling constants generally.

**Tier key:** `Derived` (from primitives) · `Grounded` (conditional/structural) · `Reference` (canonical kernel form) · `Synthesis` (arc overview) · `Inherited` (a value from measurement) · `Open` (the declared frontier — YM continuum, and #2b matter completion).

---

## The spine — read in this order

1. **[013 V1 Vacuum Kernel](Paper_013_V1_VacuumKernel.md)** — the finite-width retarded vacuum kernel (QFT-arc form).
2. **[017 Free Scalar QFT](Paper_017_FreeScalarQFT.md)** — free scalar field theory as the DCGT continuum limit of V1.
3. **[015 Gauge Fields (T17)](Paper_015_T17_GaugeFields.md)** — gauge fields as rule-type bundles (anchors the arc).
4. **[018 Yang-Mills (YM-1)](Paper_018_YangMills1.md)** — the non-abelian generalization; then follow YM-2..6 (019–023).
5. **[021 The Mass-Gap Mechanism (YM-4)](Paper_021_YM4_MassGap.md)** — the substrate mass-gap mechanism (structural core; continuum = the open wall).
6. **[MS-I Forces from Channels](Paper_MS-I_GaugeFromChannels.md)** — the matter sector as a lattice gauge theory; gauge groups from multiplicity, parity from the non-abelian sector.
7. **[MS-II The Matter Sector from the Arrow](Paper_MS-II_MatterSectorFromTheArrow.md)** — gauge groups, spin, chirality, three dimensions (the SM-facing assembly; open frontier #2b).

---

## Papers by sub-arc

### QFT foundations
| # | Paper | Result | Tier |
|---|---|---|---|
| 013 | [V1 Vacuum Kernel](Paper_013_V1_VacuumKernel.md) | the finite-width retarded vacuum kernel in QFT-arc form | Reference / Grounded |
| 014 | [V1 in a Curved Acoustic Background](Paper_014_V1_CurvedBackground.md) | the vacuum kernel on a curved acoustic background (N1/GR1) | Grounded |
| 017 | [Free Scalar QFT](Paper_017_FreeScalarQFT.md) | free scalar field theory as the DCGT continuum limit of V1 | Grounded / Derived |

### Gauge fields
| # | Paper | Result | Tier |
|---|---|---|---|
| 015 | [Gauge Fields as Rule-Type Bundles (T17)](Paper_015_T17_GaugeFields.md) | the gauge-field structure as rule-type bundles (superseded-in-part by MS-I's derivation) | Grounded |
| 016 | [Generalized Minimal Coupling](Paper_016_MinimalCoupling.md) | minimal coupling from T17 + DCGT | Grounded |
| 015.5 | [Photonic Chern Quantization of Hall Drift](Paper_015_5_Photonic_Chern_HallDrift.md) | integer Chern-quantization of Hall drift (form-identified; Chern numbers inherited) | Grounded (M3); value Inherited |

### Yang-Mills arc (the mass gap → Clay)
| # | Paper | Result | Tier |
|---|---|---|---|
| 018 | [Non-Abelian Gauge Generalization (YM-1)](Paper_018_YangMills1.md) | the non-abelian Yang-Mills generalization | Grounded |
| 019 | [Substrate→Continuum Limit (YM-2)](Paper_019_YM2_SubstrateToContinuum.md) | the substrate-to-continuum Yang-Mills limit | Grounded |
| 020 | [Osterwalder–Schrader Positivity (YM-3)](Paper_020_YM3_OSPositivity.md) | the OS-positivity audit at the substrate level | Grounded |
| 021 | [The Mass-Gap Mechanism (YM-4)](Paper_021_YM4_MassGap.md) | non-abelian `[A,A]` lifts the abelian massless flat direction (structural core verified) | Grounded (continuum survival Open) |
| 022 | [Substrate Gauge-Quotient (YM-5)](Paper_022_YM5_GaugeQuotient.md) | the T17-C8 substrate gauge quotient | Grounded |
| 023 | [Clay-Relevance Synthesis (YM-6)](Paper_023_YM6_ClaySynthesis.md) | how the arc relates to the Clay Millennium problem (relevance, not proof) | Synthesis |

### Open systems
| # | Paper | Result | Tier |
|---|---|---|---|
| 024 | [Lindblad Master Equation](Paper_024_LindbladLimit.md) | the Lindblad master equation as the V5-modulated dynamics limit | Grounded |

### The matter sector / Standard Model (open frontier #2b)
| # | Paper | Result | Tier |
|---|---|---|---|
| MS-I | [Forces from Channels](Paper_MS-I_GaugeFromChannels.md) | the matter sector as a lattice gauge theory: gauge groups from channel multiplicity, parity violation from the non-abelian sector | Grounded (frontier #2b) |
| MS-II | [The Matter Sector from the Arrow](Paper_MS-II_MatterSectorFromTheArrow.md) | the SM-facing assembly: gauge groups, spin, chirality, three dimensions | Grounded (chirality / {1,2,3} / anomalies Open, #2b) |

*(No non-paper docs in this folder. The matter-sector completion — #2b, reducing to the T4 spinor gate — is the program's highest-leverage open research target; see `event-density/docs/ED_Research_Targets.md`.)*

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[`QFT_TieredClaims_Ledger.md`](QFT_TieredClaims_Ledger.md)** — the arc's **tiered-claims ledger**: every load-bearing claim in this folder with its current tier. It doubles as the arc's staleness detector — where a paper and the ledger disagree, the ledger's `Status` column is the current state. Read it before citing anything here.
