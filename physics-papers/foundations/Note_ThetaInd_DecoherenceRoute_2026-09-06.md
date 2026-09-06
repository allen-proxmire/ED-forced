# The decoherence route gives `θ_ind = 1` — and refutes the candidate I floated two hours ago

**Date:** 2026-09-06
**Status:** **Result, with a correction to my own earlier note.**
**Probe:** `../event-density/theory/individuation_decoherence_probe.py` (new, re-runnable).
**Tier:** the identification in §1 is **argued**; the value in §3 is **`D-via-I` conditional on `ξ < 2`** and is falsifiable by tightening `ξ`.

---

## 1. The two accounts are the same quantity, not just the same gap

`Paper_Individuation_TheSystemEnvironmentCut.md` §6 says its construction and `Paper_024_LindbladLimit`'s `P-Factorized-IC` *"should be read as two accounts of the same gap"*. **They are stronger than that: they are the same quantity at different values of one threshold.**

`P-Factorized-IC` asserts `ρ_tot(0) = ρ_S(0) ⊗ ρ_E(0)` — **no system–environment correlation.** In ED, correlation between a chain-complex and its outside is carried by cross-boundary shared channels: V5 *is* the cross-chain correlation kernel (`Paper_090`), and `b_bdry(S)` is exactly the shared-channel content across the cut. So

$$\text{exact factorization} \iff b_{\rm bdry}(S) = 0 \iff R(S) = \infty$$

> **Exact factorization is individuation at `θ_ind = ∞`.**

**This immediately shows `P-Factorized-IC` cannot fix a finite `θ_ind` on its own** — as an exact postulate it names only the limit. What can fix a finite value is its **domain of validity**.

## 2. Depth is quantized, and that is what makes the answer sharp

Correlations decay with the substrate correlation length `ξ`, so a locus at depth `d` from `S`'s boundary is still correlated with the outside when `d < ξ`. If *every* locus of `S` is within `ξ` of the boundary then **`S` is all boundary layer, has no interior, and factorization has nowhere to be accurate** — not "is inaccurate", but has no domain at all.

**Depth is counted in loci, so it is an integer.** The condition for an interior to exist is `⌈a/2⌉ > ξ`, and with `R = (a−1)/2` (the length result, `Note_ThetaInd_IsALength`) the threshold is a **step function of `ξ`, not a quantity proportional to it**:

| `ξ` range | smallest `a` with an interior | `θ_ind` |
|---|---|---|
| `0 < ξ ≤ 1` | 2 | 0.5 |
| **`1 < ξ ≤ 2`** | **3** | **1.0** ← measured `ξ ≈ 1.83` |
| `2 < ξ ≤ 3` | 5 | 2.0 |
| `3 < ξ ≤ 4` | 7 | 3.0 |

> **`θ_ind = 1`, and it does NOT inherit `ξ`'s uncertainty — only the question of which integer bracket `ξ` falls in.**

**A second, independent route reaches the same value using no `ξ` at all:** the smallest square containing a locus that is not on its own boundary is `a = 3`, giving `R = 1`. **Two routes, one value.**

## 3. The sensitivity, stated plainly — **RESOLVED the same day, see the banner**

> **⚠ SUPERSEDED 2026-09-06 (later).** The `± 0.3` used below is the **per-snapshot spread**, not the uncertainty on the mean. Re-run on 40 seeds: **ξ = 1.740 ± 0.028 lu** (40 seeds, 1600 snapshots, 2026-09-06; `ed-lab/outputs/ed_sc_3_1/xi_canonical_tightened.json`), standard error **0.028**. **The `ξ = 2` boundary is 9.2σ away, not 0.6σ — the one-in-four risk described below does not exist.** 4 of 40 individual seeds do exceed 2.0. `Note_Xi_Tightened_2026-09-06.md`; gravity ledger #130.

**This needs `ξ < 2`.** The corpus value is `ξ = 1.8 ± 0.3` (`Paper_096`, GR-SC 1.7 half-decay, 10 seeds), which puts the `ξ = 2` boundary about **0.6σ away — roughly a one-in-four chance the bracket is wrong.** If `ξ > 2` then `θ_ind = 2`, not 1.

> **So this is sharp and falsifiable: tighten `ξ` and the answer is decided.** That is a better position than "undetermined", and it is not a claim to have settled it.

This probe's own 5-seed estimate is `ξ = 1.831 ± 0.043`, but by a **different estimator** (1/e crossing of the phase autocorrelation, not the GR-SC 1.7 half-decay). **It is not a tightening of the corpus value and is not quoted as one.**

## 4. The correction: my `(ξ−1)/2 ≈ 0.4` candidate was wrong

`Note_ThetaInd_IsALength_2026-09-06.md` §7 floated **`θ_ind = (ξ−1)/2 ≈ 0.4 ± 0.15`**, flagged there as *"arithmetic … plus an identification nobody has argued for"*. **The argument, once made, refutes it.**

That reading identified `θ_ind`'s length with `ξ` directly. **The boundary shell has to be crossed on both sides before an interior exists**, so the linear extent required is `2ξ`, not `ξ`. The flagged-but-unargued candidate was off by a factor of two in the place that matters, and it landed *below* the minimal-pair value `1/2` — which should have been the tell, since a value under `1/2` individuates every connected pair and makes the criterion vacuous.

**The earlier note's caution was right and its number was wrong.** That is the flag doing its job.

## 5. What is now claimed, and what is not

| | |
|---|---|
| **Argued** | exact factorization ⟺ `R = ∞`; the two accounts are one quantity |
| **Argued** | factorization has no domain of validity for a region with no interior |
| **`D-via-I`, conditional on `ξ < 2`** | **`θ_ind = 1`** |
| **Independent** | the lattice route gives `θ_ind = 1` without `ξ` |
| **NOT claimed** | that `θ_ind` is *derived* from the 13 primitives. It rests on `P-Factorized-IC`'s domain and on `ξ`'s bracket. |
| **NOT claimed** | that `F-IND-2` is fired. Unchanged from the previous note. |

**One observation worth recording against `Paper_024`.** The measured cross-boundary correlation fraction does not become small at any accessible region size — at `R = 9.5` (a 20×20 region) about 11% of near-range correlation mass still crosses the boundary. **The Born–Markov regime `Paper_024` postulates is a genuine idealisation on this substrate, not an asymptotically-approached one.** That is consistent with the paper, which declares the regime rather than deriving it, but it is worth having measured.
