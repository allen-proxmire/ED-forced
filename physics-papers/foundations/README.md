# Foundations — Folder Guide *(the substrate)*

**What this folder is.** The **root of the corpus**: the substrate itself. It holds the 13 primitives (the postulated axioms everything else is conditional on), the memory kernels that carry propagation and correlation (**V1** single-chain retarded, **V5** cross-chain), the kernel-level **arrow of time** (theorem T18), the **methodology** that defines the honesty tiers used across every ED paper (Paper_095, *form-forced / value-inherited*), and the program-overview syntheses. Read this folder to understand what ED *is* before reading what it derives. *(This folder was previously named `wedges`.)*

**State** *(authoritative source: `Paper_087` + `event-density/docs/ED_Research_Targets.md`)*:
- **The 13 primitives (Paper_087) are POSTULATED, not derived** — they are the axioms. Every "Derived" or "Grounded" result elsewhere in the corpus is conditional on them. (The reduction program asks whether they compress; that work lives in `event-density/foundations/`, not here.)
- **The kernels and the arrow are the core structural machinery:** V1 (Paper_089) and V5 (Paper_090) are the propagation/correlation carriers; the arrow (Paper_093 / T18) is the irreversibility that orders everything.
- **Paper_095 is the methodology** — it defines `form-FORCED / value-INHERITED` and the M1/M2/M3 verdict tiers you'll see quoted throughout.

**Tier key:** `Postulated` (the primitives — the axioms) · `Derived` (from the primitives) · `Grounded` (conditional/structural) · `Reference` (canonical definition or audit) · `Methodology` (defines how the program reasons) · `Synthesis` (program overview) · `Inherited` (a value from measurement).

---

## The spine — read in this order

1. **[087 The 13 Primitives](Paper_087_13Primitives.md)** — the position paper; the substrate ontology and its axioms. **Start here.**
2. **[088 Primitive Load-Bearing Audit](Paper_088_PrimitiveAudit.md)** — which primitive does what work, and where.
3. **[089 The V1 Kernel](Paper_089_V1Kernel.md)** — the finite-width retarded single-chain kernel (canonical reference).
4. **[090 The V5 Kernel](Paper_090_V5Kernel.md)** — the cross-chain correlation kernel (entanglement/gauge carrier).
5. **[093 The Arrow of Time (T18)](Paper_093_KernelArrow_of_Time.md)** — irreversibility at the kernel level.
6. **[095 Form-Forced / Value-Inherited Methodology](Paper_095_FormForced_ValueInherited.md)** — the honesty tiers the whole program uses.
7. **[100 One Substrate, Five Sectors](Paper_100_FiveSector_ProgramOverview.md)** — the program map; where every sector sits.

---

## Papers by sub-arc

### The primitives (the axioms)
| # | Paper | Result | Tier |
|---|---|---|---|
| 087 | [The 13 Primitives (Position Paper)](Paper_087_13Primitives.md) | the substrate ontology: P01–P13, the postulated axioms of the whole program | Postulated (foundational) |
| 088 | [Primitive Load-Bearing Audit](Paper_088_PrimitiveAudit.md) | which primitive is load-bearing where, across the corpus | Reference |

### The memory kernels (propagation & correlation)
| # | Paper | Result | Tier |
|---|---|---|---|
| 089 | [The V1 Kernel](Paper_089_V1Kernel.md) | the finite-width retarded single-chain kernel — canonical reference | Reference / Derived |
| 090 | [The V5 Kernel](Paper_090_V5Kernel.md) | the cross-chain correlation kernel (structural-formalism unification; `τ_V5` regime-inherited) | Grounded |
| 091 | [Memory-Kernel Cascade Across Scales](Paper_091_KernelCascade.md) | how kernels compose across scales | Grounded |
| 092 | [Kernel Hierarchy Unification](Paper_092_KernelHierarchy.md) | the unified kernel hierarchy | Grounded |
| 093 | [The Kernel-Level Arrow of Time (T18)](Paper_093_KernelArrow_of_Time.md) | irreversibility from the retarded-only kernel; the arrow at the substrate level | Derived (T18) |
| 094 | [Forward-Causal Substrate Structure](Paper_094_ForwardCausality.md) | the forward-causal (retarded) primitive structure | Grounded |

### Methodology & cross-scale structure
| # | Paper | Result | Tier |
|---|---|---|---|
| 095 | [Form-Forced / Value-Inherited Methodology](Paper_095_FormForced_ValueInherited.md) | the reasoning discipline: what "forced" means, and the M1/M2/M3 verdict tiers | Methodology |
| 096 | [Cross-Scale Invariance](Paper_096_CrossScaleInvariance.md) | the ED-SC cross-scale invariance (a substrate-RG fixed point) | Grounded |
| 097 | [Three-Regime RG / the 0.6 Problem](Paper_097_RG_0p6_Problem.md) | the three-regime RG structure and the 0.6 universal ratio | Grounded (0.6 an open universal) |

### Program syntheses / overviews
| # | Paper | Result | Tier |
|---|---|---|---|
| 098 | [ED-QFT Unified Overview](Paper_098_EDQFT_Overview.md) | Phase-1 QM + theorems + DCGT + NS/MHD + Yang–Mills + gravity preview, under one substrate | Synthesis |
| 099 | [NS Synthesis](Paper_099_NS_Synthesis.md) | the Navier–Stokes / fluid arc integrated (Papers 075 + 077–086) | Synthesis |
| 100 | [One Substrate, Five Sectors (Program Overview)](Paper_100_FiveSector_ProgramOverview.md) | the whole program map — one substrate, five sectors (capstone; companion to 098) | Synthesis |

*(No non-paper docs in this folder. The primitives here are the axioms; everything "Derived/Grounded" elsewhere is conditional on Paper_087.)*

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[`Foundations_TieredClaims_Ledger.md`](Foundations_TieredClaims_Ledger.md)** — the arc's **tiered-claims ledger**: every load-bearing claim in this folder with its current tier. It doubles as the arc's staleness detector — where a paper and the ledger disagree, the ledger's `Status` column is the current state. Read it before citing anything here.
