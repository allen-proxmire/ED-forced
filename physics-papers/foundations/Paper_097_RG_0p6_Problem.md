# Paper 097 — Three-Regime RG / 0.6 Problem

**Series:** Wave-2 Generative Papers (Wedges Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_073 (DCGT), Paper_089 (V1), Paper_096 (cross-scale invariance).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim derivation of the exact numerical value 0.6 from first principles; the value is INHERITED via canon-internal Wilsonian-RG matching.
2. It does **not** claim novel critical-exponent predictions overriding standard RG.
3. It does **not** introduce new substrate primitives.
4. "Three-regime RG / 0.6 problem" = the canon-internal closure (Paper_ed_rg_three_regime memo) identifying three substrate-level RG regimes (UV V1-dominated, IR V5-dominated, transition) with characteristic exponent $\approx 0.6$ at the canonical operating point.
5. The 0.6 value is treated here as a canon-internal benchmark. *(Sourcing corrected 2026-09-04: this cited the memory file `project_ed_rg_three_regime.md`, which sits in **another project's** memory directory — outside both repos, and not ground truth per `CLAUDE.md`. **A paper exists**: `event-density/theory/The_0_6_Problem_Resolution.md`, which argues `0.6 = 2·D_nd(quantum)` with `D_nd = 0.3` the cross-regime nondimensional invariant, via a dimensional-dictionary construction, and reports a five-route audit. **Cite that, not the memory.** This paper's tier is left unchanged and the claim in item 1 stands: assessing whether that resolution promotes 0.6 from inherited to derived requires reading it, which has not been done here. Gravity ledger Staleness #47.)*

---

## Abstract

The Wilsonian-RG flow of substrate-level effective kernels exhibits a three-regime structure: (i) UV regime ($R \lesssim \ell_{V1}$): V1-dominated, kinematic-window content. (ii) Transition regime ($R \sim \ell_{V5}$): cascade-region with characteristic exponent $\approx 0.6$ at canonical operating point. (iii) IR regime ($R \gtrsim L_{\mathrm{flow}}$): V5-dominated, macroscopic hydrodynamic content. The three-regime structure is FORM-FORCED by Paper_091 cascade + Paper_096 cross-scale invariance. The 0.6 exponent is INHERITED via canon-internal matching to the substrate operating point identified in the ED-RG closure.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P08 (Substrate scale)**, **P10 (Rule-type primitive)**, **P11 (Commitment-irreversibility)**.

### 2.2 Upstream dependencies

- **I-073:** DCGT (Paper_073).
- **I-089:** V1 (Paper_089).
- **I-091:** Kernel cascade (Paper_091).
- **I-096:** Cross-scale invariance (Paper_096).
- **I-RG:** Standard Wilsonian RG machinery (standard math).

### 2.3 Paper-specific postulates

- **P-Three-Regime-RG:** The Wilsonian-RG flow of substrate effective kernels exhibits three distinct regimes (UV, transition, IR) separated by the V1 and V5 scales.
> **SETTLED 2026-09-04 — `0.6` is REDUCED, not derived; this paper's tier is correct and unchanged.** `event-density/theory/The_0_6_Problem_Resolution.md` was read. Its result:
>
> $$T_0 = \frac{L_0^2 D_{\mathrm{nd}}}{D_{\mathrm{phys}}} \;\Longrightarrow\; 0.6 = 2\,D_{\mathrm{nd}}(\mathrm{quantum}), \qquad \frac{c_0}{c} = \frac{1}{2 D_{\mathrm{nd}}}$$
>
> **Three levels, and only the third is open** (the paper's own table): `T_0 = 2D_ndħ/(mc²)` is **structurally forced** by the dictionary construction, *no freedom*; `c_0/c = 1/(2D_nd)` is **structurally forced** as a corollary, *no freedom*; **`D_nd(quantum) = 0.3` is a convention, not a derivation.** The paper's verdict is *“partial derivation + structural reduction”*, and it says plainly: ***“The ‘0.6 problem’ does not have its own standalone resolution. It collapses cleanly into the already-named `D_nd` anchoring problem”*** — the subject of `ED-Dimensional-01-Ext.md`'s rate-balance-template program. §8: *“The 0.6 is reduced but not eliminated.”*
>
> **So the answer to ‘is 0.6 derived?’ is no, and the inheritance MOVES rather than dissolving:** what ED inherits is no longer the number `0.6` but the convention `D_nd(quantum) = 0.3`, joined to it by an exact algebraic bridge. **That is a real gain** — one unexplained number becomes one unexplained number *that is already a named, actively worked problem*, and asking “why 0.6?” is now literally asking “why `D_nd = 0.3`?” **Item 1 of this paper's preamble stands verbatim and `P-0p6-Canonical` remains a postulate.**
>
> **What the reduction buys, and none of it was in this paper (§6 of the resolution):** (a) the superluminal `c_0 ≈ 1.667c` is an **atlas-nondimensionalisation artifact**, not an ED prediction — it arises purely from picking `D_nd = 0.3`; (b) **`c_0 = c` exactly at `D_nd = 1/2`**, the rate-balance point where `γ_dec = ω_sys`, which is a clean selection rule with no fitted parameter; (c) a **cross-regime consistency relation** for analogue platforms, `c_s/c = 1/(2 D_nd(regime))`. **(c) is not registered in any ED prediction list** — flagged as a candidate, and deliberately not registered here, because the resolution paper itself cautions that the relation is *“algebraic, not predictive”*: it is a test only where `D_nd` is anchored independently per regime, which is exactly what the rate-balance template supplies for optomechanics / cavity-QED / condensed-matter / galactic / cosmological. See gravity ledger Staleness #48.

- **P-0p6-Canonical:** At the canonical operating point (Paper_096), the transition regime exhibits a characteristic exponent $\approx 0.6$; the value is canon-internal.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Kernel cascade across scales | I | Paper_091. |
| 2 | Cross-scale invariance | I | Paper_096. |
| 3 | DCGT coarse-graining | I | Paper_073. |
| 4 | Wilsonian RG machinery | I | Standard math. |
| 5 | Three-regime structure | P-Three-Regime-RG | Postulate. |
| 6 | Characteristic exponent ≈ 0.6 | P-0p6-Canonical | Postulate (canon-internal value). |
| 7 | Numerical 0.6 matching | I | Empirical / canon-internal. |

---

## §3 The Three Regimes

### 3.1 UV regime: V1-dominated ($R \lesssim \ell_{V1}$)

At sub-V1 scales, V1 finite-width retarded kernel dominates effective dynamics. RG flow at this regime tracks V1-modulated substrate transport.

### 3.2 Transition regime ($\ell_{V1} \ll R \ll L_{\mathrm{flow}}$, especially near $\ell_{V5}$)

The transition regime is the cascade region (Paper_091): both V1 (UV residue) and V5 (memory) contribute to effective kernel structure. RG flow in this regime exhibits the characteristic 0.6 exponent at the canonical operating point.

### 3.3 IR regime: V5-dominated ($R \gtrsim L_{\mathrm{flow}}$)

At macroscopic scales beyond the hydrodynamic window, V5 cross-chain memory governs effective dynamics. RG flow here aligns with standard hydrodynamic-scale-invariance.

### 3.4 The 0.6 exponent

By P-0p6-Canonical, the transition regime's characteristic exponent is $\approx 0.6$ at the canonical operating point. This is **canon-internal** (canon-internal matching to ED-RG closure per `project_ed_rg_three_regime.md`); the substrate program does **not** derive 0.6 independently.

---

## §4 Falsification Criteria

- **F1:** Substrate evidence of only two regimes (no transition cascade region) — refutes P-Three-Regime-RG.
- **F2:** Empirical re-matching of canonical operating point giving exponent $\ne 0.6$ — refutes the canon-internal value.
- **F3:** Discovery of a fourth distinct RG regime — would extend the framework.

---

## §5 Position Statement

The three-regime RG structure + 0.6 transition exponent is **FORM-FORCED** under P-Three-Regime-RG + P-0p6-Canonical. Numerical 0.6 INHERITED via canon-internal matching.

---

**End Paper 097 (FIXED).**
