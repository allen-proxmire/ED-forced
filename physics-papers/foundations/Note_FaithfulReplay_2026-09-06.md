# Faithful replay: #108 confirmed by test, and the mechanism is *where* the front goes, not *what shape* it is

**Date:** 2026-09-06
**Status:** **Result.** Validation exact; mechanism partly identified and partly open.
**Probe:** `../event-density/theory/p12_faithful_replay_probe.py` (new, re-runnable).

---

## 1. What was fixed

#108's replay flattened `ρ`, so its numbers were flagged and discarded. This one records, for **every deposit**, the exact `(neighbour, A)` pairs that entered the calculation — where

$$A=\kappa_{bw}\,(b_{wv}-1)+\kappa_\rho\,(\rho_w-\rho_v)$$

and `ρ` **accumulates with every commit**. A replay driven by that recording is bit-faithful to the live deposit given the same order.

## 2. Validation — exact, in all four arms

Condition (C), 64×64, 5 seeds:

| arm | `ξ` live | `ξ` replay |
|---|---|---|
| control `k=0` | **2.13** | **2.13** |
| `Grad` `k=8` | **0.83** | **0.83** |
| canonical `Coh` `k=8` | **0.73** | **0.73** |
| old-"Coh" `k=8` | **3.83** | **3.83** |

**The replay reproduces the live result exactly, every arm.** So #108's claim is now **tested rather than read**: the phase field is fully determined by the commit order plus the connection values, **with no dependence on which arm's bonus produced that order.** The `ξ` differences are entirely growth, not phase arithmetic.

## 3. The mechanism — and the obvious explanation is ruled out

| arm | `ξ` | `std(A)` | `mean\|A\|` | front coord. |
|---|---|---|---|---|
| control | 2.13 | 0.265 | **0.362** | **1.969** |
| old-"Coh" | **3.83** | 0.388 | **0.364** | **1.969** |
| `Grad` | 0.83 | 0.603 | **0.844** | **1.969** |
| canonical `Coh` | 0.73 | 0.744 | **1.076** | **1.939** |

**Front coordination is identical across every arm** — `1.94–1.97` committed neighbours at the moment of deposit. **So this is not about how many neighbours a cell has when it commits**, which was the natural guess and is wrong.

**What differs is the connection the front encounters.** The canonical terms grow into regions where `mean|A|` is **2.3×** (`Grad`) and **3.0×** (`Coh`) the control's. `A` is what phases are transported *through*; a large, widely-spread connection scrambles them. **The two arms with the largest `|A|` have the shortest reach.**

**So the story is not "a different shape" but "the same shape in a different place":** the phase bonus steers the front into territory with large `ρ`-differences between neighbours, which widens the transport connection, which shortens the reach. **Nothing about the phase formula is involved.**

## 4. What is *not* explained, stated because it is the interesting residue

**`mean|A|` does not explain everything.** The control and old-"Coh" have **essentially identical** connections — `0.362` and `0.364` — yet `ξ = 2.13` against `3.83`. **Same transport, nearly double the reach.**

So there are **two** effects, and only one is now identified:

1. **The connection effect** — canonical terms triple `|A|` and lose reach. Identified.
2. **A genuine alignment effect** — old-"Coh" raises reach at *unchanged* connection. ~~**Not explained here.**~~ **QUANTIFIED 2026-09-06 (#110): `+1.69` lattice units, an `81%` increase, at connection matched to within 2%** (control `|A| = 0.359, ξ = 2.08` against old-"Coh" `k=8` `|A| = 0.366, ξ = 3.77`). **And `Grad`'s alignment gain is zero to within measurement** — its whole reach loss is predicted by the connection alone (`0.27` observed against `0.29`). **So the phase term does bind, and claim 2 is fixable rather than fatal.** `foundations/Note_Effect2_Quantified_2026-09-06.md`. That is presumably the phase reward doing what the paper says it does, applied without the coordination-number bias that the extensive forms carry.

**Correlation across the four arms, `std(A)` vs `ξ`: `r = −0.714`** — the right sign, and loose precisely because old-"Coh" is the outlier that effect 2 accounts for.

## 5. Where the arc stands

**Unchanged:** the Knots result (#107 — 0/10 crystal, ten seeds, all readings) and the substance of claim 2 — under both canonical terms the physical substrate ends at `ξ < 1`, and a substrate with no reach supplies no binding.

**Now established:** *why*. **It is the growth rule steering the front into high-`|A|` territory**, not the phase functionals. **The repair, if there is one, belongs to how the phase bonus enters candidate selection** — not to `Coh` or `Grad`.

**Now visible and new:** old-"Coh" **binds at unchanged connection**, which is the one arm doing what the paper claims the phase term does. **That is a reason to look harder at the `/n`** — not as the canonical term it is not, but as the only form so far that supplies binding without the growth-side cost.

**Honest limits:** five seeds, one grid, one condition, four arms — a `r = −0.714` on four points is an illustration, not a statistic. **Effect 2 is unquantified.**
