# The neighbour–neighbour term is not inert: canonical `Coh` orders at weaker coupling than `Grad`

**Date:** 2026-09-06
**Status:** **Result, and it revises #105.** Ten seeds on condition (A).
**Probe:** `../event-density/theory/p12_condA_multiseed.py` (new, re-runnable).

---

## 1. Why this was run

Everything in ledger #103–#105 rested on **one seed**. #105 concluded that canonical `Coh` and `Grad` were *"different objects, same behaviour"* and re-attributed condition (A)'s crystallization from *"`Grad`'s known problem"* to *"a property of the phase-coherence operationalization."* **A single growth history is thin support for either claim.**

Ten seeds, each re-drawing the quenched bandwidth disorder, the start node and the deposition randomness — so these are independent disorder realizations, not just different growth orders on one lattice.

## 2. The control comes first, and it clears the ground

**`k_phase = 0` — phases deposited but with no influence on which candidate wins:**

> `R = 0.10 [0.02, 0.22]`, `ξ = 6.0 [5.4, 6.5]`, **CRYSTAL 0/10**

**The lattice and the deposit rule alone produce disorder.** So condition (A)'s crystallization is genuinely caused by the phase term, and #105's re-attribution survives its first real test. **Without this control, everything below would have been unattributable.**

## 3. The result — and it is not what one seed showed

| arm | `k_phase = 1` | `k_phase = 8` |
|---|---|---|
| **`Grad`** `\|acc\|` | `R = 0.70`, `ξ = 29.0` — **CRYSTAL 4/10** | `R = 0.94` — **CRYSTAL 10/10** |
| **old "Coh"** `\|acc\|/n` | `R = 0.10`, `ξ = 4.8` — **CRYSTAL 0/10** | `R = 0.09`, `ξ = 5.0` — **CRYSTAL 0/10** |
| **CANONICAL `Coh`** | `R = 0.86`, `ξ = 30.0` — **CRYSTAL 9/10** | `R = 0.95` — **CRYSTAL 10/10** |

**At strong coupling the two canonical terms are identical — 10/10 each, which is what the single seed saw. At weak coupling they are not: `Coh` crystallizes in 9 of 10 seeds where `Grad` does in 4.**

**One-tailed Fisher exact: `p ≈ 0.029`** (two-tailed `0.057`). Ten seeds, so **suggestive rather than established** — but the one-tailed test is the right one here, because **the direction was predicted before the run**, not read off it.

## 4. Why the direction was predicted, which is what makes this more than a 10-sample coincidence

`Coh = −Grad + 2·NN`. **The neighbour–neighbour term is an *additional alignment reward*** — it pays for neighbours agreeing with each other, on top of the `v`-neighbour agreement both terms pay for. **A larger alignment drive should order at weaker coupling.** It does.

**So `Coh` and `Grad` differ in their ordering threshold, and the difference has a mechanism rather than being a fitted observation.**

## 5. What this revises

**#105 said "different objects, same behaviour." That was the single seed talking.** The corrected statement:

> **Same behaviour at strong coupling; different ordering thresholds at weak coupling, with `Coh` ordering earlier because the neighbour–neighbour term adds alignment drive.**

**The NN term is not inert.** #104 measured it at 29–41% of the phase score and #105 found it changed no verdict; **on ten seeds it changes the verdict in half the weak-coupling cases.**

**And this is the first genuine behavioural discriminator between the two terms** — after the Knots draw, the withdrawn `ξ` trend (#103) and the mis-specified comparison (#104). **It came from removing a methodological flaw rather than from a new idea, which is the pattern of this whole line.**

## 6. The uncomfortable part, recorded deliberately

**The Knots position on this comparison has now moved three times in two days:**

1. **Originally:** `Coh` clean in (A), `Grad` crystallizes → a reason to prefer `Coh`.
2. **#105:** both crystallize equally → the reason withdrawn, concern re-attributed to the operationalization.
3. **Now:** **`Coh` crystallizes *more readily* than `Grad`** → if (A)-crystallization counts against a reading, **it counts harder against `Coh`.**

**Each move followed from fixing a real methodological flaw, and each reversed the previous conclusion.** That is the correct process working, and it is also a warning: **this comparison has been unusually good at producing confident wrong answers.** The current one rests on ten seeds, one grid size, one deposit rule, and a `p` of `0.03`. **Do not treat it as settled.**

## 7. Untouched

The **physical case (C)** is not in this run. All three arms were finite-reach there on the single seed, and that is the condition `Paper_PhaseCoherence_P12Coh`'s headline rests on. **Multi-seeding (C) is the obvious next check and has not been done.**
