---
title: "The MOND acceleration scale tracks the Hubble rate: a registered prediction and its first confrontation"
author: "Allen Proxmire"
date: "September 2026"
---

**Series:** Event Density (ED) — standalone data-confrontation paper
**Status:** Draft for external circulation. Self-contained: no ED result is assumed that is not stated and tiered here.
**Genre:** A registered prediction, its first data, and an honest verdict.

---

## Preamble — what this paper does NOT claim

1. **It does not claim confirmation.** The prediction's *qualitative* content is confirmed and its *quantitative* rate is mildly disfavoured by the first survey to test it. Both halves are stated.
2. **It does not claim to derive `H(z)`.** The Hubble history is inherited cosmological input throughout.
3. **It does not rest on the `1/(2π)` coefficient.** That coefficient is, in the source corpus's own current tiering, **postulated and disputed**. The claim tested here is the *exponent*, which is independent of it (§3.3). This is stated up front because it is the paper's main structural point.
4. **It does not claim novelty for the `a₀`–cosmology connection.** That connection is standard MOND material (Milgrom 2020 is a review of it). What is offered here is a *specific, falsifiable exponent* and a mechanism that cannot bend it.
5. **It does not claim that ED is established.** This paper is one prediction from a larger substrate program (§7). It stands or falls on its own.

---

## Abstract

The MOND acceleration scale `a₀ ≈ 1.2×10⁻¹⁰ m s⁻²` is, in MOND, a constant of nature. Its numerical proximity to `cH₀` has been noted for decades and is either an accident or a structural fact. The two readings differ observationally: if the coincidence is structural and `a₀` is set by the cosmic horizon `R_H = c/H`, then `a₀` is **not** constant — it tracks the instantaneous Hubble rate, `a₀(z)/a₀(0) = H(z)/H₀`, growing by ×1.8 at `z = 1` and ×3 at `z = 2`.

Event Density, a substrate framework, makes this reading structural and registers `a₀(z) = cH(z)/(2π)` with the exponent fixed at **exactly one**. The exponent is the testable content: it cannot be tuned within the framework without abandoning the mechanism that produces it.

The first survey able to test it has reported. MUSE-DARK III (A&A 2026) detects evolution of `a₀` at **~30σ**, excluding a **constant** `a₀` — MOND's classical reading of its own scale, though not the only MOND (§1.2) — while matching the local value to ~8%. Fitting a power `a₀ ∝ H(z)^α` gives **α = 1.18 ± 0.04 (stat)**. MOND's `α = 0` is dead at 29σ. The prediction's `α = 1` sits at **+4.4σ formally**, softened to roughly **1–2σ** once one-survey and high-redshift systematics are folded in — and the survey team's own analysis independently describes the evolution as *faster than* `H(z)`.

**The honest verdict is split: the qualitative call is confirmed and MOND's constant scale is excluded; the specific rate is mildly disfavoured.** We state the decisive test — a direct raw-data fit of `α` across surveys with a full error budget — and the condition under which the prediction should be abandoned.

---

## 1. Introduction

### 1.1 A coincidence that has to be one thing or the other

MOND fits galaxy rotation curves with a single acceleration scale `a₀`. Empirically `a₀ ≈ 1.2×10⁻¹⁰ m s⁻²`, and `cH₀ ≈ 6.8×10⁻¹⁰ m s⁻²`, so `a₀ ≈ cH₀/6`. The proximity has been remarked on since the earliest MOND papers and is discussed at length in the MOND literature (Milgrom 2020 and references therein). **We claim no novelty for noticing it.**

What the coincidence has never had is a *consequence*. Read as an accident, it predicts nothing. Read as structural — `a₀` is set by the cosmic horizon — it predicts something sharp and immediate: **`a₀` is not a constant of nature, and it should have been evolving all along.**

### 1.2 Four accounts, not two — and the fourth is the real rival

It is tempting to set this up as a two-horse race against MOND. **That would be wrong, and §1.1 has already said why:** the `a₀`–cosmology connection is standard MOND material, so a MOND theorist who expects `a₀` to track the cosmic scale is **not refuted by evolution being found — they are vindicated by it.** The field contains at least four positions:

| # | account | what it says about `a₀` | status after §5 |
|---|---|---|---|
| **1** | **ΛCDM** | there is no `a₀`; the appearance of one is a coincidence of galaxy assembly | untouched here — this paper does not test it |
| **2** | **MOND, `a₀` constant** | `a₀` is a **constant of nature**, on a par with `c` or `G` | **excluded at 29σ** |
| **3** | **MOND with an evolving `a₀`** | `a₀` tracks the cosmic scale; the **exponent is not predicted and is fitted to data** | **fits, by construction** |
| **4** | **this prediction** | `a₀` tracks the live horizon with the exponent fixed at **exactly 1**, and no freedom to move it | **`α = 1` is 4.4σ from the fit; ~1–2σ on a realistic error budget** |

**Position 2 is the one that dies at high significance, and it is not the only MOND.** Against **position 3** — the account that actually competes — this paper's discriminating content is **not that `a₀` evolves. It is the specific value `α = 1`.** And that is precisely the number currently under tension (§5.3).

**So the honest statement of what is at stake.** Position 3 can absorb any exponent the data return, including the measured `1.18`; it therefore fits better than position 4 does right now, and will continue to fit whatever is measured next. **Position 4 cannot move.** The distinction between them is not which fits today — it is that **only one of them made a commitment that could fail.**

> **That distinction is worth something only if the commitment survives.** An untunable exponent is a virtue when it is right and a refutation when it is wrong; it is never a defence. **This paper is therefore a test of position 4, not an argument for it**, and §6 states the condition under which it should be abandoned.

**What a measurement at `z ≈ 1` settles:** it separates 2 from {3, 4} decisively — that has now happened — and it separates 3 from 4 only to the precision of `α`, which is where the remaining work is.

### 1.3 What this paper does

States the prediction and — precisely — how much of it is derived and how much is postulated (§3); says why the exponent is the falsifiable content and cannot be tuned (§3.3, §4); presents the first confrontation, including the part that goes against the prediction (§5); and names the decisive test and the kill condition (§6).

---

## 2. The prediction

`a₀` is identified with a projection of the cosmic decoupling surface at `R_H = c/H`, giving

$$a_0(z) = \frac{c\,H(z)}{2\pi}, \qquad \frac{a_0(z)}{a_0(0)} = \frac{H(z)}{H_0}.$$

Numerically: **×1.3 at `z = 0.5`, ×1.8 at `z = 1`, ×3 at `z = 2`.** With `H₀ = 70 km s⁻¹ Mpc⁻¹`, `a₀(0) = 1.08×10⁻¹⁰ m s⁻²`, against a measured local `≈ 1.2×10⁻¹⁰` — an ~10% match with no fitted parameter.

Downstream, the baryonic Tully–Fisher relation `v_flat⁴ = G M_b a₀` inherits the evolution: its normalisation is not cosmologically constant, and the high-`z` BTFR and radial-acceleration-relation scales move with `H(z)`.

---

## 3. What is derived, what is inherited, what is disputed

**This section is the paper's structural core.** A prediction is only worth testing if it is clear which part of it is load-bearing.

### 3.1 Derived: the scale

That `a₀` is of order `cH₀` — that the MOND scale is set by the cosmic horizon rather than being an independent constant — is reached in the source corpus by **three independent routes**: the horizon-projection argument, a horizon-competition threshold argument, and a symmetric thermal-matching argument. **Three routes to the scale.**

### 3.2 Disputed: the coefficient

**None of the three routes delivers the coefficient.** The `1/(2π)` is, in the corpus's own current tiering, **postulated and disputed**: the factor cancels in the displayed algebra of the source derivation and is reinstated at an assembly step fixed by a normalisation choice that nothing upstream determines. **We flag this rather than defend it.** The corpus re-tiered it from *derived* to *postulated/disputed* in September 2026, and the claim that `a₀` is "parameter-free" was withdrawn with it.

### 3.3 The exponent is independent of the coefficient, and that is the point

Write the prediction as `a₀(z) = K · c · H(z)^α`. **The disputed quantity is `K`. The tested quantity is `α`.**

- Measuring the **shape** of `a₀(z)` tests `α` and is **independent of `K` entirely** — any constant prefactor drops out of a ratio `a₀(z)/a₀(0)`.
- Measuring the **normalisation** tests `K`, and is not attempted here.

> **The part of the prediction under dispute is not the part being tested.** A reader sceptical of the `2π` — and there is reason to be — can set it aside and still evaluate everything below.

### 3.4 Why `α = 1` cannot be tuned

**Not by dimensional analysis.** It would be convenient to say `a₀ = c·H·(number)` is the only dimensionally legal form, but that is false: the framework carries a second scale, `ℓ_P`, so a bent power is dimensionally available. *(A summary elsewhere in the corpus states the dimensional argument; it is wrong, and the careful statement is the one given here.)*

**By the mechanism plus the absence of a free scalar.** `α = 1` follows from `a₀` riding the *live* horizon `R_H = c/H`, one power of `H` per horizon. Bending the exponent requires a dimensionless number to bend it with, and the framework's own structural result is that it produces no intrinsic dimensionless scalar. **So `α = 1` is unfudgeable from the inside: there is no knob.** That is what makes it a real bet — a fitted exponent would be worthless as a test.

### 3.6 Why the coefficient's failure does not reach the exponent

**The obvious objection to §3.3 is that formal independence is not evidential independence.** Both `K` and `α` come from one mechanism; that mechanism demonstrably failed to deliver `K`; so why trust it for `α`? The answer is not "they are different symbols." It is that **they are produced by different steps, and every failure is on one side of the line.**

The derivation has a **radial** step and an **angular** step.

**The radial step** places the cosmic decoupling surface. Substrate influence propagates at `c`; the Hubble flow recedes at `H R`; the crossover fixes the boundary at

$$R_H = c/H.$$

That is a competition between two rates. **It contains no angular integral, no mode decomposition, and no normalisation choice.** In the source audit it is a `D-via-I` step with `H` inherited.

**The angular step** projects that surface's leading anisotropic mode onto the accelerating chain's residual `SO(2)` symmetry — the `|m| = 1` azimuthal-Fourier projection of a dipole — and this is where `1/(2π)` was supposed to come from.

**Now locate the failures.** In the source paper's own audit table:

| step | audit tier | which part |
|---|---|---|
| decoupling surface at `R_H = c/H` | **D-via-I** | radial |
| the dipole is the leading anisotropic mode | **D** | angular, and sound |
| cosmic content seen as anisotropic at first order | **A — analogy** | angular |
| `ρ₀ = cH₀` "after dimensional bookkeeping" | **P — normalisation choice** | angular |
| the surviving azimuthal factor `1/(2π)` | **DISPUTED** *(was D)* | angular |
| `N_substrate·G_φ⁻¹` set "to the value that returns the result" | **P — nothing upstream fixes it** | angular |

> **Every disputed, postulated and analogical row is in the angular step. The radial step carries none of them.**

**And the exponent is entirely radial.** `a₀` is an acceleration set by the horizon radius, `a₀ ~ c²/R_H`; with `R_H = c/H` that is `a₀ ∝ H¹`. **One power of `H`, because there is one horizon.** The evolution `a₀(z) = K c H(z)` follows from the same surface being read *at the epoch in question* rather than frozen at some earlier one. **Neither statement passes through the angular machinery.**

**A second, independent check.** The scale `a₀ ~ cH₀` is reached by **three routes** — the dipole projection, a horizon-competition threshold argument, and a symmetric thermal-matching argument. **Two of the three do not use the dipole projection at all.** If the `H`-dependence were an artifact of the angular step, those two routes could not arrive at the same scale. **They do.** So the dependence on `H` survives deleting the entire machinery that failed.

**The honest residual, stated because it is what the argument actually rests on.** Two things carry the exponent, and only the first is multiply-derived:

1. **`R_H = c/H`** — the radial crossover, reached three ways.
2. **The horizon is read LIVE, not frozen** — `a₀` tracks the contemporaneous `R_H` rather than a relic value.

**Point 2 is the mechanism's core physical assertion, not a theorem.** It is what makes the prediction a prediction: a frozen horizon would give `α = 0` and would be indistinguishable from MOND. **It is not derived from the two alternative routes, which establish the scale rather than its time-dependence.** A reader who rejects the live-horizon reading rejects the prediction — and that is the correct place for the argument to be attackable, because it is the place where the physics is.

> **So the answer to the objection is: the coefficient failed in the angular step, the exponent lives in the radial step, and the radial step has three independent supports. The scepticism the `2π` deserves does not transfer — but the live-horizon assumption is a separate exposure, and it is named here rather than buried.**

### 3.5 Inherited

`H(z)` itself; `H₀`; the MOND interpolating function; all numerical values.

---

## 4. What would distinguish this from a fit

A prediction registered after the data is worth little. Three things are stated for the record:

1. **The exponent was fixed at 1 before the data existed**, and is registered as such in the source corpus's prediction list with the ×1.8-at-`z=1` figure explicit.
2. **The framework cannot accommodate `α ≠ 1`** without abandoning the horizon mechanism (§3.4).
3. **The prediction is falsifiable in both directions** — `α = 0` would have killed it as decisively as `α = 2` would.

---

## 5. The confrontation

### 5.1 What was measured

**MUSE-DARK III (A&A 2026)** measured the acceleration scale in galaxy samples extending to `z ~ 1`.

| quantity | result |
|---|---|
| evolution of `a₀` detected | **~30σ** |
| constant `a₀` (MOND, `α = 0`) | **excluded at 29σ** |
| local intercept | `1.0×10⁻¹⁰ m s⁻²` — matches the predicted `1.08` to **~8%** |
| fitted power `a₀ ∝ H(z)^α` | **α = 1.18 ± 0.04 (stat)** |
| `a₀` at `z ~ 1` | `2.38 (+0.12 / −0.10)` ×10⁻¹⁰ m s⁻² |

### 5.2 The half that confirms

**`a₀` evolves.** The qualitative content of the prediction — that the MOND scale is not a constant of nature — is confirmed at high significance, and **the constant-`a₀` reading is excluded at 29σ.** That is a structural claim about a 40-year-old framework, made in advance, and the data agree with it. **But it does not separate this prediction from position 3 of §1.2**, which expects evolution too; the separation from that rival rests entirely on §5.3.

The local normalisation also lands within ~8%, though §3.2 requires us to say that the `2π` producing that number is disputed, so the agreement is weaker evidence than it looks.

### 5.3 The half that does not

**`α = 1.18 ± 0.04` places `α = 1` at +4.4σ.** Taken at face value, the prediction is excluded.

**We do not take it at face value, and we say why — while noting that the reasons cut less far than we would like.**

- The `±0.04` is a **statistical** error from a single first-generation survey. The covariance is unpublished; per-bin values are not tabulated (Figure 3 only); high-redshift rotation-curve systematics — inclination, pressure support, beam smearing, stellar mass-to-light — are not folded in. Realistically the uncertainty is larger, bringing the tension to roughly **1–2σ**.
- **But the direction is corroborated by the survey team's own analysis**, which independently compares `a₀(z)` to `H(z)` and describes the evolution as **faster than `H(z)`**. An earlier suggestion that the tension was an artifact of using a linear fit as a proxy is therefore **withdrawn**: the anti-prediction direction is the authors' own reading, not an artifact of ours.

### 5.4 The verdict, stated plainly

> **Qualitative call: confirmed, and MOND's constant `a₀` excluded at 29σ.**
> **Quantitative rate: mildly disfavoured, ~1–2σ, from one survey.**
> **This is an open tension, not a refutation — and it is not a confirmation either.**

**The prediction is closer to the data than MOND is by a wide margin and is not sitting comfortably.**

---

## 6. The decisive test, and the kill condition

**The decisive test is a direct fit of `α` to raw data across multiple surveys with a full error budget** — MUSE-DARK galaxies plus independent `z ~ 0.9–2.4` rotation-curve samples — rather than a re-reading of one published linear fit. Rubin- and Euclid-era data should settle it.

**Kill condition, stated in advance:**

> **If a multi-survey fit with a complete error budget returns `α` inconsistent with 1 at ≥3σ, this prediction is refuted.** There is no version of the mechanism that survives with a bent exponent (§3.4).

A weaker outcome — `α` consistent with 1 at 1σ — would be a genuine confirmation of a registered, unfudgeable, framework-distinctive number.

---

## 7. Provenance

This prediction comes from Event Density, a substrate framework in which the arrow of time is the single process primitive. **That framework is not argued here and nothing above depends on accepting it.** The relevant chain is `Paper_029` (the horizon projection giving `a₀`), `Paper_037` (continuum invariance of `a₀`), `Paper_031` (the BTFR inheritance), and `Paper_038` CO-3 (the registered forward prediction). The corpus, its claim register with per-claim tiers, and the audit trail behind the September 2026 re-tiering of the `2π` are public.

**The prediction stands or falls on §5 and §6 alone.**

---

## 8. Load-bearing step audit

| # | step | tier | note |
|---|---|---|---|
| 1 | `a₀` is set by the cosmic horizon `R_H = c/H` | **D** | three independent routes (§3.1) |
| 2 | the `1/(2π)` coefficient | **P — postulated/disputed** | §3.2; not tested here |
| 3 | `α = 1` from one power of `H` per live horizon | **D** | §3.4, and independent of step 2 |
| 4 | no intrinsic dimensionless scalar to bend `α` | **D** (framework structural result) | what makes `α` unfudgeable |
| 5 | `H(z)`, `H₀`, the interpolating function, all values | **I** | inherited |
| 6 | BTFR normalisation inherits the evolution | **D-via-I** | composition of step 1 with the standard BTFR |
| 7 | evolution detected at ~30σ; `α = 0` excluded | **I — measurement** | MUSE-DARK III |
| 8 | `α = 1.18 ± 0.04`, `α = 1` at +4.4σ stat | **I — measurement** | same source |
| 9 | tension softens to ~1–2σ under a realistic error budget | **A → position** | our judgement about unpublished systematics; **the weakest step in the paper** |
| 10 | verdict: qualitative confirmed, rate disfavoured | **A → position** | composite |

**Steps 9 and 10 are positions, not results, and are labelled as such.** Step 9 in particular is the paper's soft joint: if the published `±0.04` is taken as complete, the prediction is excluded at 4.4σ and §5.4 should read differently.

---

## 9. Falsifiers

- **F1 (primary).** A multi-survey direct fit returning `α` inconsistent with 1 at ≥3σ refutes the prediction.
- **F2.** A demonstration that `a₀` is constant across redshift refutes it — and would also refute the ~30σ MUSE-DARK III result, so this is now a claim about that survey's reliability.
- **F3.** A derivation, within the framework, of a mechanism admitting `α ≠ 1` would remove the bet's content by making it fittable. **This is a falsifier of the claim's *status*, not of its value**, and is stated because a theory that can absorb any exponent has not predicted one.
