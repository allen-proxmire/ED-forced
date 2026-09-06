# `ξ` tightened: the `± 0.3` was never an uncertainty, and `θ_ind = 1` goes from 0.8σ to 9.2σ

**Date:** 2026-09-06
**Status:** **Result.** `ξ = 1.740 ± 0.028 lu`, 40 seeds / 1600 snapshots.
**Artefact:** `ed-lab/outputs/ed_sc_3_1/xi_canonical_tightened.json`
**Script:** `ed-lab/analysis/scripts/ed_sc_3_1_xi_tighten.py` — the estimator is **imported** from `ed_sc_3_1_xi_canonical.py`, not reimplemented, so the method cannot drift.

---

## 1. The thing worth fixing was not the seed count

`θ_ind = 1` (`#129`) is conditional on `ξ < 2`, and the corpus quoted `ξ = 1.8 ± 0.3`, putting that boundary ~0.6σ away — a one-in-four risk on the bracket. The obvious move was more seeds. **Reading the estimator first showed the error bar was the problem, not the sample size.**

In `ed_sc_3_1_xi_canonical.py`, `all_xi_p` accumulates **one value per snapshot**, and

```python
"xi_std": float(np.std(all_xi_p))
```

is therefore the **per-snapshot spread over 400 snapshots** — how much a single snapshot varies — not the uncertainty on the mean. The same artefact's ten per-seed means have a spread of **0.16**, and the standard error is smaller again.

> **Three different quantities were all being called "the error on `ξ`", and only one of them answers "is the substrate's `ξ` below 2".**

## 2. The measurement

Same estimator, 40 seeds, 1600 snapshots:

| | value | what it is |
|---|---|---|
| **mean `ξ`** | **1.7397** | the substrate's correlation length (raw-density channel) |
| per-snapshot spread | 0.3342 | how much **one snapshot** varies ← **this is the quoted `± 0.30`** |
| per-seed spread | 0.1793 | how much **one seed's mean** varies |
| **standard error** | **0.0284** | **the uncertainty on `ξ` itself** |

**Distance to the `θ_ind` bracket boundary `ξ = 2`:**

| using | σ |
|---|---|
| the per-snapshot spread (what the corpus quoted) | **0.78** |
| **the standard error (the right comparison)** | **9.18** |

> **`θ_ind = 1` does not sit on a one-in-four risk. It sits on a 9σ bracket.**

## 3. The corpus over-corrected, and this is the second half of that story

The 2026-09-04 pass (gravity #47, foundations staleness #4) was **right** that `1.7575` is an over-precision — five significant figures on a number uncertain in its first decimal. **But its replacement, `1.8 ± 0.3`, substituted a spread for an uncertainty and therefore understated the precision by an order of magnitude.**

> **The corpus first overstated the precision, then understated it. Both errors have one cause: spread and uncertainty were not distinguished. The supported figure is three significant figures — `ξ = 1.74 ± 0.03`.**

**This also settles the rounding disagreement flagged under C2** (`#126`): gravity #47 said `~1.8 ± 0.3`, soft-matter #2 said `1.76 ± 0.30`. **Both were quoting the spread.** Neither was wrong about the spread; both were wrong to call it the error on `ξ`.

## 4. The honest caveat

**4 of 40 individual seeds exceed 2.0** (90% below). `θ_ind` is a property of the **rule**, not of one realization, so the mean is the right statistic — **but a substrate realization drawn from the upper tail would individuate at `θ_ind = 2`**, and that is worth knowing rather than hiding behind the mean.

## 5. Checked and clean: the smoothed channel

The artefact also carries `xi_mean_smoothed = 3.05`, a factor 1.74 away and **in a different `θ_ind` bracket**. Re-measured here at **3.017** — stable, so the discrepancy is real and not noise.

**But it is not an error in the corpus.** `ed_sc_3_1_xi_canonical.py` labels that channel *"secondary, for audit"* and the raw density *"primary"*, and the papers quote the primary. **The primary is also the right channel for `θ_ind`**, since it is the raw participation content whose correlations carry system–environment correlation. **Checked, no change.** Worth recording that the choice is load-bearing and is currently correct rather than lucky.

## 6. Where this was written back

`Paper_096` (the postulate statement, the inline flag, §7), `Foundations_TieredClaims_Ledger.md`, the individuation paper's §4.6 sensitivity paragraph, `Note_ThetaInd_DecoherenceRoute_2026-09-06.md` (correction banner), spreadsheet rows for `ξ_canonical` and for `P-Canonical-Operating-Point-ED-SC`, and research target #25.

**Not rewritten:** the dated audit-trail entries in `AUDIT_2026-09-04_ClaimStrength_AllArcs.md` and the historical text inside `Paper_096` §7, which are records of what was believed on 2026-09-04 and are marked as superseded rather than edited.
