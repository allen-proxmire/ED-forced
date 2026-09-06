# The ranking is invariant; the binding threshold is not. #111 splits into a general half and a conditional one

**Date:** 2026-09-06
**Status:** **Result.** #119's highest-value outstanding check, run.
**Probe:** `../event-density/theory/p12_rhostar_ordering_probe.py` (new, re-runnable). 48×48, 3 seeds, `k_phase = 8`, each arm compared against the **no-phase control at its own `ρ*`**.

---

## 1. The numbers

| arm | `ρ* = 0.0` | `ρ* = 0.5` | `ρ* = 1.0` |
|---|---|---|---|
| **no-phase control** | **5.68** | **2.08** | **1.19** |
| `\|acc\|/n` = **intensive `Grad`** | **4.63** | **3.77** | **1.55** |
| intensive `Coh` | 1.97 | 1.63 | 1.06 |
| `Grad` (extensive) | 0.94 | 0.81 | 0.77 |
| canonical `Coh` | 0.79 | 0.73 | 0.69 |

## 2. The half that is general — and it is the comparative claim

**The ranking of the four arms is identical at every `ρ*`:**

> **`|acc|/n` ≫ intensive `Coh` > `Grad` > canonical `Coh`**

**Every time, by wide margins** — intensive `Grad` beats the next arm by factors of `2.4`, `2.3` and `1.5`. **And canonical `Coh` is last at every `ρ*`.**

**So #111's comparative conclusion survives and is now general**: **intensive scoring with no neighbour–neighbour term is the best-performing form regardless of the coherence target**, and **`Coh`'s extra NN term hurts at every `ρ*` tested.** The 2×2's *ordering* is not an artifact of `ρ* = 0.5`.

## 3. The half that is conditional — and it is the absolute claim

**"Binds" means beating the no-phase control at the same `ρ*`.** By that test:

- `ρ* = 0.5` — **`|acc|/n` binds** (`3.77` vs `2.08`)
- `ρ* = 1.0` — **`|acc|/n` binds** (`1.55` vs `1.19`)
- **`ρ* = 0.0` — nothing binds.** The control reaches `5.68`; the best arm reaches `4.63`.

> **At `ρ* = 0` the no-phase control outperforms every phase-augmented arm.**

**And the mechanism is the one #109 identified.** With `ρ* = 0`, `Coh = −ρ_v²` strongly prefers fresh, low-density targets, so the front advances cleanly and revisits little; `ρ`-differences between neighbours stay small, the transport connection `|A|` stays small, and reach is long. **Adding any phase bonus perturbs that clean front, and the connection cost exceeds the alignment gain.** Consistent with everything measured in #109–#110.

## 4. What this does to the record

**Confirmed and generalised:** #111's ranking. **`Grad` intensively scored is the best form at every `ρ*`; `Coh` is the worst.** The "which functional" question is answered independently of the parameter.

**Demoted to conditional:** the claim that **the phase term supplies binding.** It holds at `ρ* = 0.5` and `1.0`, and **fails at `ρ* = 0`.** So it is a statement about a regime, not about ED.

**And that reaches the paper.** `Paper_PhaseCoherence_P12Coh` exists to supply the **attractive/constructive sign** that V5 clock-binding and the MOND interference term assumed. **That sign is delivered at the certified `ρ* = 0.5` and not at `ρ* = 0`** — so the two downstream results inherit a dependence on an undocumented parameter. **They do not lose their support; they gain a condition.**

**Note the shape of this.** #112 corrected *which term* the paper measures. This corrects *under what conditions* the measurement holds. **Neither retracts the paper; both narrow it.**

## 5. Limits

**Three seeds, one grid, three `ρ*` values, one `k_phase`.** The ranking is stable and wide-margined, which is what makes §2 credible on three seeds; **the binding threshold sits between `ρ* = 0.0` and `0.5` and has not been located.**

**`increment = 1` was held fixed throughout**, and it is equally undocumented (#119). **Whether the ranking survives a change *there* is untested**, and it is the same question one level down.
