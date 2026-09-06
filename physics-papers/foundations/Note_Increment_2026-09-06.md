# `increment` replicates the split — and reveals that "the substrate fills" is also a regime statement

**Date:** 2026-09-06
**Status:** **Result.** The second undocumented parameter, tested the same way as `ρ*`.
**Probe:** `../event-density/theory/p12_increment_probe.py` (new, re-runnable). 48×48, 3 seeds, `k_phase = 8`, `ρ*` held at `0.5`, each arm against the no-phase control at its **own** increment.

---

## 1. The result

| arm | `inc = 0.5` | `inc = 1.0` *(certified)* | `inc = 2.0` |
|---|---|---|---|
| **no-phase control** | **2.16** | **2.08** | **5.29** |
| `\|acc\|/n` = intensive `Grad` | **2.57** ✔ | **3.77** ✔ | 3.65 |
| intensive `Coh` | 1.57 | 1.63 | 2.06 |
| `Grad` (extensive) | 0.85 | 0.81 | 0.89 |
| canonical `Coh` | 0.74 | 0.73 | 0.76 |

**Ranking: identical at every increment** — `|acc|/n` > intensive `Coh` > `Grad` > canonical `Coh`. **The same order #120 found across `ρ*`.**

**Binding: `|acc|/n` binds at `0.5` and `1.0`, and nothing binds at `2.0`**, where the control itself reaches `5.29`.

## 2. So the split is a property of the comparison, not of either parameter

**Two undocumented parameters, tested independently, give the same structure:**

> **Which functional is best is ROBUST. Whether a phase term helps at all is a REGIME statement.**

`|acc|/n` — intensive `Grad` — is the best-performing form at every value of both parameters, and canonical `Coh` is the worst at every value of both. **That is now a two-parameter result, and it is the session's central conclusion.** The binding threshold moves with either parameter and is a statement about where you are, not about ED.

## 3. New: the fill result is also conditional, and it interacts with the phase term

The `inc = 0.5` column hides the sharpest finding, which is in the **grid-fill** counts:

| arm at `inc = 0.5` | nodes filled (of 2304) |
|---|---|
| no-phase control | **2304** — full |
| `\|acc\|/n` | 2285 (99%) |
| intensive `Coh` | 2243 (97%) |
| **`Grad` (extensive)** | **1881 (82%)** |
| **canonical `Coh`** | **1684 (73%)** |

**At `increment = 0.5` the extensive phase arms cause extinction — the front dies before filling the grid, losing 18% and 27%.** At `inc = 1.0` and `2.0` everything fills.

**And the mechanism was predicted algebraically before the run.** At `inc = 0.5`, `ρ` is reachable at `0, 0.5, 1.0, …`, so **the coherence target `ρ* = 0.5` becomes exactly attainable.** At `ρ_u = 0.5`:

- **staying:** `Σ(u→u) = −(0.5−0.5)² − 0.5 − 0 = −0.50`
- **a fresh neighbour:** `Σ(u→v) = −(0−0.5)² − 0 − |0−0.5| = −0.75`
- **an already-committed neighbour at `ρ = 0.5`:** `−(0)² − 0.5 − 0 = −0.50`

> **The rule becomes dwell-preferring, and ranks already-committed neighbours *above* fresh ones. So the front revisits instead of expanding — and dies.**

**The certified rule forbids self-transitions (#116), so it cannot dwell — it takes the next-best move, which is a committed neighbour, and paints itself into a corner.**

## 4. What this adds to the record

**`"the substrate fills"` is a regime statement, on two counts.** #119 found a `ρ*` ceiling (`ρ* = 2.0` → 4033/4096). **This adds an `increment` floor, and one that interacts with the phase term** — the control fills at `inc = 0.5` while the extensive phase arms do not. **So it is not a property of the parameters alone but of the parameters *and* the scoring.**

**And the certified point sits in a narrow good region.** At `inc = 1.0, ρ* = 0.5`: everything fills, the best arm binds, nothing crystallizes. **Move `increment` down and the extensive arms go extinct; move it up and nothing binds; move `ρ*` up and the substrate stops filling; move `ρ*` down and nothing binds.** **The certified parameters are surrounded by regimes where something fails — and nothing in the corpus says they were chosen for that, or for anything.**

## 5. Limits

Three seeds, one grid, three increments, one `k_phase`, `ρ*` held fixed. **The two parameters were varied one at a time; the joint space is untested**, and §4's "narrow good region" is inferred from two one-dimensional slices, not mapped.
