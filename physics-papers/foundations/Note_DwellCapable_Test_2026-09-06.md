# A dwell-capable rule breaks no certified result — and the parameters, not the rule, are what suppress dwell

**Date:** 2026-09-06
**Status:** **Result.** The question opened by adopting `P-Commitment-Advancement` (#117), answered.
**Probe:** `../event-density/theory/p12_dwell_capable_probe.py` (new, re-runnable).

---

## 1. The change, kept minimal on purpose

`P-Commitment-Advancement` licenses a commitment that does **not** advance. The certified rule's candidate set is `admissible_neighbors(u)`, with `u` excluded. **The dwell-capable rule adds `u` to its own candidate set, scored by the certified `Σ` exactly as any other candidate.** Nothing else changes — same functional, same commit chokepoint.

## 2. The algebra predicts the answer before the run

The certified `Σ` is `Coh = −(ρ_v − ρ*)²`, `Str = ρ_v`, `Grad = |ρ_v − ρ_u|`, with `ρ* = 0.5`. **For a self-transition `Grad = 0`** — there is no gradient to fight — so:

| `ρ_u` | `Σ(u→u)` | `Σ(u→v_fresh)` | |
|---|---|---|---|
| 1 | **−1.25** | **−1.25** | **exact tie** |
| 2 | −4.25 | −2.25 | neighbour wins |
| 3 | −9.25 | −3.25 | neighbour wins by more |

**With `ρ* = 0.5` and `increment = 1`, a locus jumps from `0` straight past the coherence target.** So dwell is **never strictly favoured** — it is only ever *tied*, at `ρ_u = 1`, and disfavoured thereafter.

## 3. A second structural finding, forced by trying to run it

The run crashed on the first attempt. **The certified tiebreak keys on `graph.bw(u, v)` — the *edge* bandwidth — and a self-transition has no edge, so it has no key at all.**

> **The certified rule assumes the winner is a neighbour in *two* independent places: the candidate set *and* the tiebreak.**

**One modelling choice was unavoidable here**, and it is flagged rather than buried: the self-move is given the disorder **mean**, `bw = 1.0`, so it competes on the footing of an average edge rather than being handed a win or a loss by construction.

## 4. The result

Condition (C), 64×64, 5 seeds:

| rule | `R` | `ξ` | dwell fraction | nodes committed |
|---|---|---|---|---|
| certified (no dwell) | 0.027 | **2.13** | 0.0000 | **4096** |
| **dwell-capable** | 0.017 | **1.93** | **0.0604** | **4096** |

**Dwell is reachable but marginal — 6% of decisions, all of them ties**, exactly as §2 predicts. **The substrate still fills completely (4096 = the whole grid) either way**, so nothing goes extinct.

**And no certified result breaks.** `R` and `ξ` both fall slightly — `ξ` by `−0.20`, about `9%`. **Both changes move *away* from crystalline order**, so the Knots-safety result is not merely robust, it is **more comfortably satisfied** under the dwell-capable rule.

## 5. What this settles

**The question #117 opened is answered for the result it could reach: allowing dwell does not break Knots-safety, and the substrate still fills.** That is one certified result, tested; **it is not "any certified result," and the claim is scoped to what was run.**

**The more useful finding is why dwell is rare.** It is **not** that the rule forbids it — the rule now permits it. **It is the parameters.** `ρ* = 0.5` with `increment = 1` means a locus overshoots the coherence target in a single commit, and after that dwelling is strictly worse.

> **So adopting `P-Commitment-Advancement` licenses a dwell but does not produce one. A dwell-bearing substrate needs `ρ*` or the increment changed — a separate and much larger commitment than the postulate.**

**That matters for the mass route.** The dwell arc wanted dwell for individual rest mass. **The postulate was necessary and is not sufficient: the reference parameters suppress the phenomenon the arc needs**, and changing them is a change to the certified substrate rather than an addition to it.

## 6. Limits, stated plainly

**The dwell *fraction* is sensitive to §3's modelling choice.** With `bw = 0` for the self-move, dwell would never win a tie; with `bw = 2` it would always win. **The *existence* of ties is robust — it is algebra — but `6%` is a consequence of assigning the disorder mean.** A different choice moves it, and nothing in the corpus fixes it.

**Five seeds, one grid, one condition, one measured pair (`R`, `ξ`).** Other certified results — the holographic counts, the ρ-dynamics, the orientation stratification — **are untested here.**
