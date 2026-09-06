# `ρ*` is undocumented and it is a bigger lever on phase reach than anything this session compared

**Date:** 2026-09-06
**Status:** **Result, and a calibration warning about my own session's numbers.**
**Probe:** `../event-density/theory/p12_rhostar_probe.py` (new, re-runnable).

---

## 1. The parameter has no justification anywhere

`ρ*` — the *coherence target density* in the certified `Coh = −(ρ_v − ρ*)²` — is set to **0.5** in `SigmaCoeffs`. A corpus-wide search finds **no justification for that value, or for `increment = 1`, anywhere.** `ρ*` appears in `physics-papers/` only in this session's own notes and in an unrelated continuum memo. `SigmaCoeffs`' docstring says only that *"qualitative roles are fixed …; magnitudes are tunable."*

**But `ρ*` is not a magnitude.** It is a **target**, and where it sits relative to the increment is qualitative: with `increment = 1`, `ρ` is reachable only at `0, 1, 2, …`, and **`ρ* = 0.5` is the value that maximises the minimum distance from the target to the reachable set. It is the most unreachable place it could sit.**

## 2. My prediction was wrong, and the measurement says so

I predicted `Coh` would be **inert** in the certified regime, reasoning that `Coh(0) = Coh(1) = −0.25` at `ρ* = 0.5`, so it cannot distinguish a fresh locus from a once-committed one.

**Measured, that is wrong.** At the certified `ρ*`:

- `Coh` takes **different values across candidates in 82% of decisions**;
- and switching the `Coh` channel off **changes the winner in 40% of them**.

**`Coh` is not inert. It decides two decisions in five.** The reasoning failed because candidates are not confined to `ρ ∈ {0,1}` — revisited loci reach higher densities, where `Coh` differentiates sharply.

## 3. The result that matters

| `ρ*` | `R` | `ξ` | committed | `Coh` decides |
|---|---|---|---|---|
| 0.0 | 0.121 | **5.23** | 4096 | 0.515 |
| **0.5** *(certified)* | 0.027 | **2.13** | 4096 | 0.404 |
| 1.0 *(reachable)* | 0.013 | 1.19 | 4096 | 0.396 |
| 1.5 | 0.008 | 0.76 | 4096 | 0.360 |
| 2.0 | 0.012 | 0.63 | **4033** | 0.325 |

> **`ξ` falls by a factor of eight across the range, monotonically.**

**And the scale of that is the point.** This session's largest characterized effect was #110's *"`+81%` reach at matched connection"* — `ξ` from `2.08` to `3.77`. **Moving `ρ*` from `0.5` to `0.0` moves `ξ` from `2.13` to `5.23`: `+145%`, larger than the entire effect the session has been dissecting** — and it is a parameter nothing justifies.

## 4. What survives, and it is the important one

**Knots-safety is robust to `ρ*`.** `R` peaks at `0.121` at `ρ* = 0`, against `R > 0.8` for a crystal verdict. **Nothing crystallizes anywhere in the range.** The result the July arc rests on does not depend on this parameter.

**The fill result has a ceiling.** At `ρ* = 2.0` the substrate stops filling completely (`4033` of `4096`) — extinction begins. **Below that it is flat.** So *"the substrate fills"* holds for `ρ* ≲ 1.5` and is not unconditional.

## 5. The calibration warning, which applies to my own work today

**Absolute `ξ` values are not properties of ED. They are properties of ED-at-`ρ*`-`0.5`.** Every `ξ` quoted in ledger #103–#118 — the `2.13` control, the `3.83` binding result, the `0.73` canonical-`Coh` failure — **is measured at one undocumented value of a parameter that dominates the observable.**

**The comparisons remain internally valid**, because every arm was run at the same `ρ*`. **What is not established is that the ORDERING of arms is stable across `ρ*`** — and that is exactly the check that has not been done.

**So #111's conclusion — that `Grad` binds and `Coh` does not — is a result at `ρ* = 0.5`.** It may well be general. **Nothing here shows that it is.**

## 6. What is owed

1. **A justification for `ρ* = 0.5`, or an explicit statement that it is a convention** and that absolute `ξ` values inherit it. Currently the corpus says neither.
2. **Re-run the `Coh`-vs-`Grad` comparison at two or three values of `ρ*`.** If the ordering holds, #111 is general; if it flips, #111 is a statement about one parameter setting. **This is the single highest-value check outstanding on this thread.**
3. ~~**The same question for `increment = 1`**~~ — **TESTED 2026-09-06 (#121), and it replicates the split.** **Ranking identical at `inc = 0.5, 1.0, 2.0`** (`|acc|/n` > intensive `Coh` > `Grad` > canonical `Coh`); **binding fails at `inc = 2.0`.** **So the pattern belongs to the comparison, not to either parameter.** **And a new finding: at `inc = 0.5` the coherence target becomes exactly reachable, the rule turns dwell-preferring, and the EXTENSIVE phase arms go extinct** — `Grad` fills 82% of the grid and canonical `Coh` 73%, while the control fills all of it. **So “the substrate fills” is conditional on `increment` as well as `ρ*`, and it interacts with the scoring.** `foundations/Note_Increment_2026-09-06.md`.
