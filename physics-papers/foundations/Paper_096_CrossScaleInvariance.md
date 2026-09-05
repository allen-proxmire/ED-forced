# Paper 096 — Cross-Scale Invariance (ED-SC 3.x Canonical)

**Series:** Wave-2 Generative Papers (Wedges Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_073 (DCGT), Paper_089 (V1), Paper_091 (kernel cascade), Paper_092 (kernel hierarchy).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim exact scale-invariance at all scales; the invariance is at the **structural** level for the kernel + dynamics content, with specific scale-dependent corrections.
2. It does **not** claim novel empirical predictions; ED-SC 3.x cross-scale invariance is the **canonical** version in the corpus.
3. It does **not** introduce new substrate primitives.
4. "ED-SC 3.x canonical" = the corpus-internal canonical cross-scale-invariance argument identified in `project_ed_sc_3_arc.md` + `project_orientation_current.md`.
5. "Cross-scale invariance" = the substrate-level statement that V1 + V5 + DCGT structure produces invariant kernel-and-dynamics content under appropriate scale transformations.

---

## Abstract

Cross-scale invariance in ED is the canonical statement (ED-SC 3.x) that the substrate kernel hierarchy (V1 + V5 + higher-order $V_n$ per Paper_092) + DCGT coarse-graining (Paper_073) supports an invariance under scale transformations $\xi \to \xi'$ within the hydrodynamic window. The S1 invariant (substrate-level kernel-content) is preserved across the canonical operating point $\xi_{\mathrm{canonical}} = 1.7575$ lu (from memory file `project_ed_sc_3_arc.md`); the S2 ensemble-only content is regime-specific. The form is FORCED via composition of kernel-hierarchy invariance + DCGT closure; specific scale-transformation parameters INHERITED from canonical operating-point matching.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P03 (Channel + locus indexing; spatial homogeneity)**, **P08 (Substrate scale)**, **P10 (Rule-type primitive)**, **P11 (Commitment-irreversibility)**.

### 2.2 Upstream dependencies

- **I-073:** DCGT (Paper_073).
- **I-089:** V1 (Paper_089).
- **I-091:** Kernel cascade across scales (Paper_091).
- **I-092:** Kernel hierarchy unification (Paper_092).

### 2.3 Paper-specific postulates

- **P-S1-Invariant:** The substrate-level S1 kernel-content is invariant under scale transformations within the hydrodynamic window: V1 + V5 indexing under Paper_092's $(\ell_n, r_n, k_n)$ is preserved.
- **P-Canonical-Operating-Point-ED-SC:** The canonical operating point $\xi_{\mathrm{canonical}} \approx 1.8 \pm 0.3$ lu *(quoted elsewhere as 1.7575; see the precision note in §7)* (measured value from the ED-SC 3.3.x arc closure) is the reference scale against which invariance is stated.
- **P-S2-Ensemble-Only:** The S2 content (ensemble-level statistical signatures) is regime-specific, not cross-scale invariant.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Kernel hierarchy structure | I | Paper_092. |
| 2 | DCGT closure under coarse-graining | I | Paper_073. |
| 3 | S1 kernel-content invariance | P-S1-Invariant | Postulate. |
| 4 | Canonical $\xi_{\mathrm{canonical}}$ reference | P-Canonical-Operating-Point-ED-SC | Postulate (canon-internal). |
| 5 | S2 ensemble-only regime | P-S2-Ensemble-Only | Postulate. |
| 6 | Cross-scale invariance verdict | D-via-I | Composition. |
| 7 | Numerical $\xi_{\mathrm{canonical}} = 1.76 \pm 0.30$ lu | **Measured** *(re-tiered 2026-09-04; was `I` / “Empirical / canon-internal”)* | Simulation result on the certified substrate — artefact `ed-lab/outputs/ed_sc_3_1/xi_canonical.json`, 10 seeds × 40 snapshots. Matches the Tier Key's **Measured** definition. Value is `σ`-limited and processing-dependent; see §7. |
| 8 | Specific 5×3 verdict grid (per memory) | I | ED-SC 3.3.x closure. |

---

## §3 The Cross-Scale Invariance

### 3.1 S1 invariant content

By P-S1-Invariant, the substrate-level kernel structure (V1 + V5 + higher-order under Paper_092 indexing) is preserved under scale transformations within the hydrodynamic window: the $(\ell_n, r_n, k_n)$ indices transform covariantly under scale rescaling, preserving the substrate kernel identity.

### 3.2 Canonical operating point

By P-Canonical-Operating-Point-ED-SC, $\xi_{\mathrm{canonical}} = 1.7575$ lu is the substrate-level reference scale. Invariance is stated relative to this canonical point. **[PRECISION FLAGGED 2026-09-04 — the measurement gives `ξ = 1.76 ± 0.30` lu.** The artefact `ed-lab/outputs/ed_sc_3_1/xi_canonical.json` reports `σ = 0.303` over 10 seeds, so *1.7575* quotes five significant figures to a number uncertain in its first decimal. The same artefact's **smoothed** autocorrelation gives `3.05 ± 0.53`, a factor 1.74 away, so the value is processing-dependent too. **ξ is genuinely Measured** (simulator of record, 10 seeds × 40 snapshots) — what is wrong is the precision, not the provenance. `Paper_096` §7; Foundations staleness #4; gravity Staleness #47.]**

> **A banked negative on deriving ξ, located 2026-09-04 and not previously cited here.** `event-density/papers/Generative Papers/Paper_ED_SC_4_2_xi_canonical_H0_derivation.md` — *“Substrate-Derivation of ξ_canonical(H₀)”* — **attempted exactly this derivation and reports that it does not close**: *“derivation attempted, does not close at substrate-first-principles level; **value-INHERITED status preserved**; structural setup is FORM-FORCED M3”*. It identifies the missing piece as either a substrate-derived `ℓ_V5(H₀)` relation or a substrate-derived scaling law, and calls itself *“the highest-leverage ED-SC 4.x paper”*. **This confirms the INHERITED tier used here rather than challenging it** — ξ is measured (below) and its derivation is a banked negative. **Cited because it was not:** the paper sits in the working repo's stale `papers/Generative Papers/` fork, so anyone attacking *“derive ξ_canonical”* from this paper alone would repeat a failed attempt. Gravity ledger Staleness #51.

**Provenance, traced 2026-09-04.** ξ is **measured, not a floating benchmark**: `ed-lab/outputs/ed_sc_3_1/xi_canonical.json`, produced by the simulator of record `analysis/scripts/ed_arch_r2/r2_grf_falsifier_tests.py` + `ED_Update_Rule.ed_step_mobility`, method *GR-SC 1.7 half-decay of the 2D radial autocorrelation*, 10 seeds × 40 snapshots (400 total), 64² periodic, α=0.03 γ=0.5 σ=0.0556 mobility-exp 2.7, 500 steps.

**⚠ The quoted precision is not supported by the measurement.** The artefact reports `xi_mean = 1.7575325729470939` **with `xi_std = 0.3034757800063313`** across the ten seeds (per-seed range 1.623–2.191). **The honest value is `ξ ≈ 1.8 ± 0.3`** — a 17% spread — and quoting *1.7575* gives five significant figures to a quantity uncertain in its first decimal place. **And it is processing-dependent:** the same artefact's smoothed autocorrelation gives `xi_mean_smoothed = 3.05 ± 0.53`, a factor of **1.74** from the unsmoothed value. The papers quote the unsmoothed number without noting that the choice moves it that far. *(Gravity ledger Staleness #47; Foundations staleness #4.)*

*(Superseded sourcing, retained for the record: the value was cited to the memory file `project_ed_sc_3_arc.md`, which lives in **another project's** memory directory and is therefore outside both repos and, per `CLAUDE.md`, not ground truth. That memory file also states a per-seed span of [1.039, 2.19]; the artefact's own per-seed values run [1.623, 2.191], so the memory is wrong about the lower bound — a small but exact illustration of why the artefact is cited here instead.)*

The numerical value is **measured, not derived from primitives independently.

### 3.3 S2 ensemble-only regime

By P-S2-Ensemble-Only, statistical ensemble-level content (S2) is regime-specific and does NOT participate in the cross-scale invariance. This is the load-bearing distinction in the ED-SC 3.x framework: S1 invariant, S2 regime-specific.

### 3.4 Composition

S1 invariance + DCGT closure (I-073) + canonical operating point (P-Canonical-Operating-Point-ED-SC) jointly produce the cross-scale invariance verdict. Form FORCED; numerical content INHERITED via canon-internal matching.

---

## §4 Falsification Criteria

- **F1:** Substrate evidence that V1 / V5 kernel indexing is NOT preserved under scale rescaling — refutes P-S1-Invariant.
- **F2:** Empirical evidence that S2 ensemble content IS cross-scale invariant — refutes P-S2-Ensemble-Only's distinction.
- **F3:** Demonstration that the canonical operating point $\xi_{\mathrm{canonical}}$ is mis-identified at substrate level — refutes the canon-internal matching.

---

## §5 Position Statement

Cross-scale invariance (ED-SC 3.x canonical) is **FORM-FORCED** in ED via P-S1-Invariant + DCGT closure (Paper_073) + canonical operating point. S1 invariant; S2 regime-specific. Numerical content INHERITED.

---

**End Paper 096 (FIXED).**
