# Canonical `Coh` behaves like `Grad` — and the distinctive behaviour belonged to neither

**Date:** 2026-09-06
**Status:** **Result.** The first run that actually asks the `Coh`-versus-`Grad` question, per ledger #104.
**Probe:** `../event-density/theory/p12_coh_canonical_probe.py` (new, re-runnable).

---

## 1. The fix

Ledger #104 found the earlier probe's *"Coh reading"* — `bonus = |acc|/n` — is not `Coh` but `Grad` divided by the coordination number. Canonical `Coh` at a candidate, with `b ≈ 1` and `v`'s own contribution included, maximized over `v`'s free phase:

$$\mathrm{Coh}_{\max}=2|acc|+\big(|acc|^2-n\big),\qquad \mathrm{Grad}_{\max}=2|acc|$$

$$\mathrm{Coh}-\mathrm{Grad}=|acc|^2-n=2\!\!\sum_{w<w'}\!\!\cos\Delta\pi_{ww'}=\textbf{the neighbour–neighbour term}$$

**One arm changed; grid, seed, deposit rule and normalization all held fixed.**

## 2. The run — and the baseline reproduces, so the comparison is clean

64×64, single seed, `k_phase` swept `0.5 → 8`:

| | **(A)** bandwidth holonomy only | **(C)** physical: bw + `ρ` holonomy |
|---|---|---|
| **`Grad`** `\|acc\|` | `R≈0.89–0.96`, `ξ=30` → **CRYSTAL** | finite, `ξ`: **2.2 → 0.8** |
| **old "Coh"** `\|acc\|/n` | `R≈0.04–0.19`, `ξ≈4.2–5.0` → finite | finite, `ξ`: **flat 4.2 → 3.7** |
| **CANONICAL `Coh`** | `R≈0.87–0.97`, `ξ=30` → **CRYSTAL** | finite, `ξ`: **1.6 → 0.7** |

**The `Grad` and old-"Coh" arms reproduce the earlier run exactly**, so the probe is validated and any difference in the third arm is attributable to the neighbour–neighbour term and nothing else.

## 3. What it says

> **⚠ REVISED 2026-09-06 by a ten-seed run — `foundations/Note_CondA_MultiSeed_2026-09-06.md`, ledger #106.** **This section's “no difference in behaviour” was the single seed talking.** On ten seeds in condition (A): at **`k_phase = 8`** the two canonical terms are indeed identical (**10/10 crystal each**), **but at `k_phase = 1` canonical `Coh` crystallizes 9/10 against `Grad`'s 4/10** (one-tailed Fisher `p ≈ 0.029`). **They differ in ordering THRESHOLD**, and the direction was predicted beforehand: **`Coh = −Grad + 2·NN`, so the neighbour–neighbour term is an extra alignment reward and should order at weaker coupling.** **The NN term is therefore not inert** — §3's *“large but inert”* is withdrawn. A `k_phase = 0` control gives **0/10 crystal**, so the effect is the phase term and not the lattice.

**Canonical `Coh` tracks `Grad`, in both conditions.** It crystallizes in (A) where `Grad` crystallizes, and its `ξ` falls `1.6 → 0.7` where `Grad`'s falls `2.2 → 0.8`. **There is no discriminator, because there is no difference in behaviour to discriminate.**

**And the neighbour–neighbour term is large but inert.** The multi-channel run measured it at **29–41% of the phase score** — so `Coh` and `Grad` are genuinely different numbers — **yet it changes no verdict anywhere.** Different objects, same behaviour.

**The distinctive behaviour belonged to neither term.** The signature that made the old "Coh" arm look like a live alternative — **finite-reach in (A), and `ξ` flat at `≈ 4` across a 16× sweep** — is a property of `|acc|/n`, **which is neither canonical `Coh` nor the `Grad` proposal.** It is `Grad/n`, and #103 already showed the `/n` is the growth-front coordination number.

## 4. Consequences, tiered

**(a) The `Coh`-versus-`Grad` question is moot as posed.** It asked which term owns the July phase-alignment measurement. **In condition (A), neither does** — both canonical terms crystallize where the measurement is finite-reach. **In condition (C), the physical case, both do, and they are indistinguishable.** So the answer is not "one of them"; it is **"both, where it matters, and neither where it doesn't."**

**(b) The condition-(A) Knots concern moves and grows.** `Note_PhaseInGrad_Probe` recorded (A)-crystallization as **`Grad`'s known problem**, with the `Coh` reading clean there. **That asymmetry was the `/n`.** With both terms written canonically, **(A) crystallizes under both** — so it is not a problem with the `Grad` proposal specifically but with **the phase-coherence operationalization in that condition.**

**(c) What survives untouched:** the physical case. **In (C) all three arms are finite-reach**, so `Paper_PhaseCoherence_P12Coh`'s headline result — finite-reach rather than crystalline order in the physical condition — **stands under every reading, including the two canonical ones.** That is the result the July arc actually rests on, and this run strengthens rather than threatens it: it now holds for the canonical terms and not only for the probe's convention.

**(d) `Grad`'s tier is unchanged**, but its *standing relative to `Coh`* improves: the one recorded reason to prefer the `Coh` reading — that `Grad` crystallized in (A) and `Coh` did not — **was an artifact and is withdrawn.**

## 5. Honest limits

**Single seed, one grid size, one deposit rule.** The `k_phase` sweep is wide (16×) and the verdicts are stable across it, but nothing here is a multi-seed statistic.

**And the deposit rule is shared.** All three arms deposit the mean-field angle, which is `Grad`-optimal by construction. A canonical-`Coh`-optimal deposit would also extremize the neighbour–neighbour term over `v`'s phase — **but that term does not contain `v`'s phase at all**, so the mean-field angle *is* `Coh`-optimal too. **That is a small, checkable statement rather than an assumption, and it is why one deposit rule serves all three arms.**
