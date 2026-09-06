# The `Grad` phase discriminator is dead — and the reason says what a working probe would need

**Date:** 2026-09-06
**Status:** **Negative result**, with a constructive successor. Runs the cleaner probe `Note_PhaseInGrad_Probe_2026-09-05.md` §"honest limit" asked for.
**Probe:** `../event-density/theory/p12_grad_decomposed_probe.py` (new, re-runnable).

---

## 1. What was asked for

The `Coh`-versus-`Grad` question — **which term does the July phase-alignment measurement belong to?** — came back a draw on Knots-safety. One discriminator survived: **`ξ`'s response to coupling strength**, flat (`≈ 4`) under the `Coh` reading and monotonically shrinking (`2.2 → 0.8`) under `Grad`.

The note then flagged its own limit, and it was not cosmetic:

> The extensive form **conflates two effects: alignment quality and coordination number**. A cleaner probe would decompose `|acc| = n × (|acc|/n)` and sweep them separately.

**Since `|acc| = n·(|acc|/n)` exactly, the two readings differ by one factor of the coordination number `n`.** So generalize to `bonus = n^α·(|acc|/n)` — `α = 0` is `Coh`, `α = 1` is `Grad` — and add the control that decides it: **`bonus = n`, rewarding coordination number with the phase information deleted.**

## 2. Result

Condition (C), the physical case, 64×64, matched RNG stream:

| bonus | `kp=0.5` | `1.0` | `2.0` | `4.0` | `8.0` |
|---|---|---|---|---|---|
| `α=0` — **`Coh`**, intensive | 4.2 | 3.9 | 3.9 | 4.1 | 3.7 |
| `α=0.5` — interpolated | 1.8 | 1.8 | 1.9 | 1.5 | 1.2 |
| `α=1` — **`Grad`**, extensive | 2.2 | 1.9 | 1.5 | 1.0 | 0.8 |
| **phase-blind `n` only** | **2.0** | **1.6** | **1.2** | **0.9** | **0.6** |

The first and third rows reproduce the earlier run, so the setup is faithful.

**The control settles it. Rewarding coordination number with no phase information at all reproduces the shrinkage** — `2.0 → 0.6`, tracking `Grad`'s `2.2 → 0.8` closely. **`Grad`'s `ξ`-trend is a coordination-number artifact of extensivity, not a statement about phase.**

**The discriminator is dead, and the `Coh`-versus-`Grad` question returns to the draw it was in before that trend was proposed.**

## 3. The more useful half: why no probe of this design can settle it

The dead discriminator points at something structural. **The two terms are extensive in different things:**

- **`Coh`** (canonical `Paper_087` §P12) is `2Σ_{a<b}√(b_a b_b)cos Θ_ab` — a sum over **pairs of contributions at a locus**. In the MOND case those two contributions are *local* and *horizon* (`Paper_030`'s bilocal).
- **`Grad`** (the proposal) is `Σ_K Σ_⟨u,v⟩ |P_K(v) − P_K(u)|²` — a sum over **graph edges between loci**.

**Different index sets.** One runs over sources of participation at a place; the other runs over places.

**And the probe carries one phase per node.** With a single phase per locus, "contributions at a locus" and "neighbouring loci" collapse onto the same neighbour set — **so the probe makes the two sums identical by construction, and the only thing left to differ is the normalization, which is the factor of `n` §2 just showed is a growth-front artifact.**

**That is why Knots-safety came back a draw and why the `ξ` trend was spurious: the probe has no degree of freedom in which the two terms differ.** Not a tuning problem.

## 4. What a discriminating probe needs

**Multiple channels per locus**, so that `Coh`'s contribution-pair sum and `Grad`'s edge sum run over genuinely different index sets. Concretely: give each node a small set of channels `K` each with its own `b_K` and `π_K`, then

- **`Coh`** reads the **within-locus** pairs — interference between a locus's own channels;
- **`Grad`** reads the **across-edge** differences of each channel separately.

**Those come apart immediately**: a configuration with strong within-locus alignment and weak across-edge alignment scores high on one and low on the other. **The current single-phase probe cannot represent that configuration at all.**

## 5. Status of the `Grad` proposal, unchanged and now better characterized

`Grad` remains a **proposal**, `form-forced-conditional at best`, with its supports and its known problem intact — condition (A) crystallizes under the `Grad` assignment, which was the real finding of the 2026-09-05 run and is untouched here.

**What changes:** the note's fifth item — the `ξ`-trend, offered as "a new discriminator, which did not exist before this run" — **is withdrawn.** It was measuring the growth front, not the phase.

**What does not change:** which term owns the July measurement is still open, and the `cos Θ` discharge still cites that measurement as one of its two supports.

**Held to the same bar as a positive:** this is a **negative**. It removes a false lead rather than adding a result, and its value is that the false lead was recorded in the corpus as live.
