# The repair test: binding needs *two* conditions, and only `Grad` can meet both

**Date:** 2026-09-06
**Status:** **Result.** The repair partly works, and the part that fails identifies which term owns the July measurement.
**Probe:** `../event-density/theory/p12_repair_test_probe.py` (new). 48×48, 3 seeds, condition (C).

---

## 1. The proposed repair, and why the first version failed

#110 proposed entering canonical `Coh` into candidate selection **normalized** — `Coh/n` — a scoring convention rather than a change to the functional.

**It failed, and the reason names the fix.** `Coh` has two pieces of **different degree in `n`**: when neighbours align, `|acc| ~ n` but `|acc|² ~ n²`. **One factor of `/n` cannot make both intensive** — the quadratic piece is left linear in `n`, still chasing crowded cells.

**So the correct normalization divides each piece by its own degree:**

$$\text{intensive }\mathrm{Coh}=\frac{|acc|}{n}+\frac{|acc|^2-n}{2n^2}$$

## 2. Both criteria, all four arms

| arm | `mean\|A\|` spread over the sweep | `ξ` range | control `ξ = 2.08` |
|---|---|---|---|
| canonical `Coh` | **0.480** | 0.73 – 1.33 | far below |
| `Coh/n` (naive) | **0.320** | 1.13 – 1.83 | below |
| **intensive `Coh`** | **0.145** | 1.63 – 1.87 | **still below** |
| `\|acc\|/n` (reference) | **0.066** | **3.77 – 4.28** | **far above** |

**Criterion (a) — connection flatness — improves monotonically with each step of normalization: `0.480 → 0.320 → 0.145`.** The intensive form removes about **70%** of the connection-chasing. That part of the repair works.

**Criterion (b) — reach — fails. Intensive `Coh` never gets past the no-phase control**, despite having nearly flat connection.

## 3. What the failure identifies

**Read the alignment residuals** (reach that the connection does *not* account for): intensive `Coh` sits at `−1.17 … −0.68`, **essentially the control's `−1.02`**. The `|acc|/n` reference sits at `+0.70 … +0.97`.

> **Intensive `Coh` has no alignment gain at all. Normalization removed its cost and delivered no benefit.**

**So intensivity is necessary and not sufficient**, and a clean 2×2 falls out:

| | **no NN term** | **with NN term** |
|---|---|---|
| **extensive** | `Grad` — no binding | canonical `Coh` — no binding |
| **intensive** | **`\|acc\|/n` — BINDS** | intensive `Coh` — no binding |

**Both conditions are required, and the second one is the neighbour–neighbour term.** Adding it destroys the binding even when the scoring is made intensive.

**And there is a mechanism for that, already established.** #105 showed the NN term **does not contain `v`'s own phase** — it scores how coherent `v`'s *neighbourhood* already is, regardless of what `v` would do. **So it is a reward carrying no information about the choice being made.** It biases selection toward already-coherent pockets rather than toward alignment, and that preference is evidently harmful.

## 4. The consequence, and it answers the question this thread opened with

**`|acc|/n` is intensive `Grad`.** `Grad` maximized over `v`'s free phase is `2|acc|`; divide by `n` and the factor `2` absorbs into `k_phase`. **So the arm that binds is not "neither term" — it is `Grad`, entered intensively.**

That revises #104's framing. #104 correctly said `|acc|/n` is not canonical `Coh`; the fuller statement is that **it is `Grad` in a normalized scoring convention.**

> **So the July phase-alignment measurement belongs to `Grad`.** And `Coh` cannot reproduce it under any normalization tested, because the term that distinguishes `Coh` from `Grad` — the neighbour–neighbour cross term — is precisely what kills the binding.

**This is the first thing in the entire `Coh`-versus-`Grad` line that discriminates the two on behaviour rather than on artifacts, and it favours `Grad`.**

## 5. Where this leaves claim 2

**Claim 2 is answered, not merely fixable.** The phase-coherence paper's attractive/constructive sign **is** supplied — by `Grad` entered intensively — so V5 clock-binding and the MOND interference term keep the support they were promised. **What was never available is the same result from `Coh`.**

**What the corpus should now say:** the July operationalization is **`Grad`, intensively scored**, and it should be named as such rather than as the simulator's `v3_active` convention.

## 6. Limits, and they are real

**Three seeds, one grid (48), one condition, one deposit rule.** The 2×2 is clean but each cell is a small sample.

**Intensive `Coh`'s connection is flatter than canonical's but still 2.2× the reference's** (`0.145` against `0.066`), so criterion (a) is *improved*, not *met* — some chasing survives the intensive form and is unexplained.

**And the direction of §4's conclusion is opposite to the corpus's prior lean.** `Note_PhaseInGrad_Probe` originally preferred the `Coh` reading; #105 withdrew that reason; #106 found `Coh` crystallizes *more* readily; this now finds `Coh` cannot bind. **That is four moves in the same direction, each from a methodological fix — consistent, but this comparison has reversed before and should be expected to be tested again.**
