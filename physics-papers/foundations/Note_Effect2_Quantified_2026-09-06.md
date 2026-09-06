# Effect 2 quantified: the phase term *does* bind — `+81%` reach at matched connection

**Date:** 2026-09-06
**Status:** **Result.** Claim 2 is a fixable problem in candidate selection, not a fatal one in the phase functional.
**Probe:** `../event-density/theory/p12_effect2_probe.py` (new, re-runnable). 48×48, 3 seeds, condition (C), control re-run at the same grid so every number is internally comparable.

---

## 1. The two effects, swept

| arm | `k` | `mean\|A\|` | `ξ` |
|---|---|---|---|
| **control** | 0 | **0.359** | **2.08** |
| **old-"Coh"** `\|acc\|/n` | 1 → 8 | **0.300 → 0.366** | **4.09 → 3.77** |
| **`Grad`** `\|acc\|` | 1 → 8 | 0.421 → 0.840 | 1.81 → 0.81 |
| **canonical `Coh`** | 1 → 8 | 0.599 → 1.079 | 1.33 → 0.73 |

**Effect 1, fitted across all 13 points:** `ξ = 4.79 − 4.68·mean|A|`, `r = −0.844`. **Reach falls about 4.7 lattice units per unit of transport connection.**

## 2. Effect 2, measured directly rather than by residual

**The cleanest comparison needs no fit at all, because two points sit at the same connection:**

| | `mean\|A\|` | `ξ` |
|---|---|---|
| control (no phase term) | **0.359** | **2.08** |
| old-"Coh" at `k = 8` | **0.366** | **3.77** |

> **Connection matched to within 2%. Reach `+1.69` lattice units — an `81%` increase.**

**That is effect 2, and it is real.** And it holds across the sweep: at `k = 1, 2, 4` old-"Coh" runs at `|A| = 0.300–0.315` — **below** the control — while reaching `ξ = 4.09–4.28`. **It gains reach without paying any connection cost at all.**

## 3. And the canonical terms gain essentially nothing

**`Grad` at `k = 1`:** its connection rises from `0.359` to `0.421`, a difference of `0.062`. Effect 1 alone predicts a reach loss of `4.68 × 0.062 = 0.29`. **Observed loss: `2.08 → 1.81`, i.e. `0.27`.**

> **`Grad`'s entire reach loss is the connection. Its alignment gain is zero to within measurement.**

**Canonical `Coh` at `k = 1`** does slightly better than effect 1 predicts (`0.75` observed against `1.12` predicted), so it has *some* alignment gain — **but it is swamped**, because its connection climbs three times faster.

## 4. The artifact I am not reporting as a result

The regression residuals **trend with `k`** for both canonical arms (`Grad`: `−1.01 → −0.04`; `Coh`: `−0.65 → +0.99`). **That is a saturation artifact, not effect 2.** `ξ` cannot fall below zero, so the true relation flattens at high `|A|` while a straight line keeps descending — the fit under-predicts there and manufactures positive residuals.

**So §2's matched-connection comparison is the measurement, and the residual column is not.** Reporting those residuals as arm-specific alignment gains would have been this thread's next artifact.

## 5. What this settles

**Claim 2 is fixable, not fatal.** The phase term **does** supply constructive binding — `+81%` reach at matched connection is not marginal. **What the canonical terms do wrong is not the alignment; it is that they drag the growth front into high-connection territory, and that costs more reach than the alignment gains.**

**And the mechanism of the drag is now visible.** `|acc|` and canonical `Coh` reward **agreement × quantity**; the quantity part chases cells with many committed neighbours, which sit in high-`ρ` pockets, which is where `|A|` is large. **`|acc|/n` rewards agreement quality only, so it does not chase them** — its `|A|` is flat across an 8× sweep.

**The repair this points to** — and it is a proposal, not something tested here: **enter the canonical term into candidate selection in a normalized form.** That is a **scoring convention**, not a change to `Coh` or `Grad` as functionals, and it is exactly where #108 and #109 located the problem. **Whether a normalized canonical `Coh` recovers the binding is the obvious next run and has not been done.**

## 6. Limits

Three seeds, one grid (48, smaller than the 64 used earlier — the control was re-run to match, so internal comparisons are sound but cross-note absolute values are not). **Effect 1's fit is `r = −0.844` on 13 points with known curvature at the high end.** The `+81%` figure rests on **one matched pair**, supported by the flat-`|A|` trend across the old-"Coh" sweep.
