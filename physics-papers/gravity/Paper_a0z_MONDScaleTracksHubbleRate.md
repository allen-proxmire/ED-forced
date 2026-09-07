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

The first survey able to test it has reported. MUSE-DARK III (A&A 2026) detects evolution of `a₀` at **~30σ**, excluding a **constant** `a₀` — MOND's classical reading of its own scale, though not the only MOND (§1.2). *(The predicted local normalisation also lands within ~8%, but it rests on a coefficient nothing upstream fixes and is **not** offered as evidence; see §3.2 and §5.2.)* **The survey publishes a *linear* fit, not a power law** (§5.1). Converting it and propagating the terms the published bar omits — the intercept, the cosmology, and the reduction choice — gives **`α = 1.15 ± 0.07`, putting the prediction's `α = 1` at 2.3σ** (§5.3). The survey team's own analysis independently describes the evolution as *faster than* `H(z)`, so the direction of the tension is theirs even though the number is ours.

> **A caveat that is larger than the tension, stated here rather than in a footnote — and one that needs nobody's cooperation to settle (§5.3c).** A 2026 re-analysis of the survey's own public catalogue (§5.3a) reports three baryonic-mass-budget systematics, each claimed sufficient to produce the trend. **Their effect sizes are quantitatively coherent with published numbers** (checked in `event-density/theory/a0z_baryonic_systematics_check.py`), and they bear on the **~30σ detection itself, not merely the rate.** **The survey's own text confirms the first of the three:** its baryonic model carries stellar disk, atomic gas and bulge, **no molecular gas**, and the authors put **~0.2 dex** on that omission against a **0.334 dex** trend (§5.3c). **If it holds, the honest status of this prediction is neither confirmed nor refuted but UNTESTED**, and the 2.3σ above falls with the detection it is measured against. **The catalogue is public, so this is decidable rather than merely arguable.**

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
| **1** | **ΛCDM** | there is no fundamental `a₀`; the appearance of one is a coincidence of galaxy assembly — **and that coincidence is itself expected to drift with redshift** | **not excluded, and not even strained** (see below) |
| **2** | **MOND, `a₀` constant** | `a₀` is a **constant of nature**, on a par with `c` or `G` | **excluded at 29σ** |
| **3** | **MOND with an evolving `a₀`** | `a₀` tracks the cosmic scale; the **exponent is not predicted and is fitted to data** | **fits, by construction** |
| **4** | **this prediction** | `a₀` tracks the live horizon with the exponent fixed at **exactly 1**, and no freedom to move it | **`α = 1` at 2.3σ** on a computed conversion budget (§5.3), before the survey's own systematics |

**Position 2 is the one that dies at high significance, and it is not the only MOND.** Against **position 3** — the account that actually competes — this paper's discriminating content is **not that `a₀` evolves. It is the specific value `α = 1`.** And that is precisely the number currently under tension (§5.3).

**So the honest statement of what is at stake.** Position 3 can absorb any exponent the data return, including the measured `1.18`; it therefore fits better than position 4 does right now, and will continue to fit whatever is measured next. **Position 4 cannot move.** The distinction between them is not which fits today — it is that **only one of them made a commitment that could fail.**

> **That distinction is worth something only if the commitment survives.** An untunable exponent is a virtue when it is right and a refutation when it is wrong; it is never a defence. **This paper is therefore a test of position 4, not an argument for it**, and §6 states the condition under which it should be abandoned.

**And position 1 is not as untouched as the table suggests.** Hydrodynamical simulations of plain ΛCDM with baryons — **Magneticum** (*MNRAS*, `10.1093/mnras/stac3017`) — already produce an **apparent** rise in the RAR acceleration scale with redshift, from ordinary galaxy-assembly and baryon-modelling effects, of a size comparable to what is observed. **No modified gravity, no horizon mechanism.** So:

> **The detection of evolution, by itself, does not discriminate this prediction from ΛCDM either.** It excludes only position 2. **Positions 1, 3 and 4 all accommodate an evolving `a₀`**, and they separate only on its *rate and shape* — which is precisely the part under tension (§5.3).

**What a measurement at `z ≈ 1` settles:** it separates **2** from {1, 3, 4} decisively — that has now happened — and it separates 1, 3 and 4 from each other **only through the exact rate**, which is where all the remaining work is.

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

> **A consequence worth stating early, because it removes the paper's most quotable number.** Since `K` is fixed by a choice rather than by the derivation, **the agreement between `K c H₀` and the measured `a₀` cannot be used as evidence for `K`.** Any paper making this prediction has to decline its own best-sounding sentence, and this one does (§5.2).

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

**Ciocan et al., MUSE-DARK III** (arXiv:2604.22613; A&A 2026) measure the radial-acceleration-relation scale in **79 star-forming galaxies at `0.33 < z < 1.44`** in the MUSE Hubble Ultra Deep Field.

**What the survey publishes** — and it matters that this is stated separately from what we infer from it:

| quantity | result | whose |
|---|---|---|
| evolution of `a₀` detected | **~30σ** | **theirs** |
| per-bin scale | rises `≈1.99 → 2.71` ×10⁻¹⁰ m s⁻² across the range | **theirs** |
| `a₀` at `z ~ 1` | `2.38 ± 0.1` ×10⁻¹⁰ m s⁻² | **theirs** |
| parametrisation | **LINEAR**: `a₀(z) = a₀(0) + a₁ z`, with `a₁ = 1.59 ± 0.1` ×10⁻¹⁰ | **theirs** |
| power-law index `α` in `a₀ ∝ H(z)^α` | **not published by the survey** | — |
| **implied `α = 1.18 ± 0.04` (stat)** | **converted by us from their linear fit** | **OURS** |

> **The survey fits a straight line in `z`. It does not fit a power of `H(z)`.** The `α = 1.18` on which this paper's central tension rests is **our conversion of their published linear parametrisation**, not a number they report. **An earlier draft of this paper mislabelled it as the survey's measurement; that was an error and it is corrected here.**

**What independently corroborates the direction** is that the MUSE-DARK team themselves compare `a₀(z)` against `H(z)` and describe the evolution as **faster than `H(z)`.** So the sign of the tension is theirs even though the number is ours.

### 5.2 The half that confirms

**`a₀` evolves.** The qualitative content of the prediction — that the MOND scale is not a constant of nature — is confirmed at high significance, and **the constant-`a₀` reading is excluded at 29σ.** That is a structural claim about a 40-year-old framework, made in advance, and the data agree with it. **But it does not separate this prediction from position 3 of §1.2**, which expects evolution too; the separation from that rival rests entirely on §5.3.

**The local normalisation is NOT offered here as evidence, and the reason is stated rather than buried.** `K c H₀` lands within ~8% of the measured `a₀`. But by §3.2 the coefficient `K` is not fixed by anything upstream — the source derivation's own audit records the assembly constant as *“set to the value that returns the result”*. **A coefficient chosen to produce a number cannot then be evidenced by that number.** To be precise about what the record does and does not support: the quantity targeted was the `1/(2π)` **form**, not the observed `a₀`, so this is not reverse-engineering from the data. **But that distinction rescues the intent, not the inference.** The most the ~8% establishes is that the chosen coefficient is **not absurd** — a weak consistency statement, and one that would read the same way for a range of nearby choices. **It is excluded from the evidence for this paper's claim.**

### 5.3 The half that does not — with the refit shown

**Taken at face value, `α = 1.18 ± 0.04` places `α = 1` at +4.5σ and the prediction is excluded.** An earlier draft answered this by asserting the error bar was too small and the real tension "~1–2σ," without producing a budget. **That was special pleading, and a referee would have been right to reject it. The budget is now computed** (`event-density/theory/a0z_powerlaw_refit.py`), and it does not say what the earlier draft guessed.

**First, what the `±0.04` is.** Propagating only the survey's `a₁ = 1.59 ± 0.10` through the endpoint conversion reproduces `α = 1.178 ± 0.034`. **That is the published bar, and it identifies the reduction our own addendum used.** It contains their statistical error through one conversion choice and nothing else.

**Second, the terms it omits, switched on one at a time.**

| term added | `α` | `σ` | `α = 1` at |
|---|---|---|---|
| their `a₁` only (`±0.10`) | 1.177 | 0.034 | **5.2σ** |
| + the intercept (`±0.10`, assumed) | 1.180 | 0.064 | 2.8σ |
| + cosmology (`Ωₘ ± 0.007`) | 1.180 | 0.065 | 2.8σ |
| + **reduction choice** | **1.152** | **0.065** | **2.3σ** |

> **`α = 1.15 ± 0.07`, putting `α = 1` at 2.3σ — and 73% of that variance is missing from the published `±0.04`.**

**Third, and this is the term nobody's error bar contains: a straight line in `z` is not a power law in `H(z)`, so their fit has no single `α` to disagree with.** The local slope *d ln a₀ / d ln H* of their own fitted line runs

| `z` | 0.33 | 0.50 | 0.75 | 1.00 | 1.25 | 1.44 |
|---|---|---|---|---|---|---|
| local `α` | 1.78 | 1.46 | 1.19 | 1.04 | 0.95 | 0.90 |

**a factor of two across the range, crossing `α = 1` at `z ≈ 1.1` — inside the data.** Any single quoted `α` is therefore the output of a reduction choice. Four defensible choices give 1.118, 1.147, 1.162 and **1.178** — and the last, the one that maximises `α`, is the one the corpus quoted.

**The honest statement, and it is narrower than either the earlier draft's or the face-value reading:** the tension is **2.3σ on conversion error alone**, before any of the survey's astrophysical systematics, which are theirs to quantify and would push it lower. **The intercept assumption is the largest single lever and the input we are least entitled to** — it is published to two significant figures with no error bar. At `±0.05` the tension is 3.2σ; at `±0.15`, 1.8σ. **A referee could reasonably pick any of those rows, and the paper does not get to choose for them.**

**What does not change.** The direction is still corroborated by the survey team's own analysis, which compares `a₀(z)` to `H(z)` and describes the evolution as **faster than `H(z)`**. **The tension is real and it is against the prediction.** It is smaller and much softer than 4.5σ, and it is not a refutation. It is also not a result.

### 5.3b The shape comparison, which avoids the conversion entirely

**Comparing one derived `α` to another inherits the reduction choice, so it is worth asking the question without forming an exponent at all.** With the amplitude free — which it must be, the coefficient being disputed (§3.2) — how far apart are the two curves across the measured range?

| `z` | 0.33 | 0.50 | 0.75 | 1.00 | 1.25 | 1.44 |
|---|---|---|---|---|---|---|
| their fit | 1.53 | 1.80 | 2.19 | 2.59 | 2.99 | 3.29 |
| ED, `α = 1` | 1.62 | 1.80 | 2.10 | 2.44 | 2.81 | 3.12 |
| deviation | **+6.5%** | +0.2% | −4.5% | −6.0% | −5.9% | −5.2% |

**They agree to 4–7% everywhere in the measured range. They are close, and they are not the same.** Two things must be said against the prediction here. **The worst deviation, 6.5%, is larger than the survey's ~4.2% precision on a single point**, and with 79 galaxies the *trend* is pinned far better than any single point, so the relevant comparison is tighter still. **And the residual is structured rather than random** — ED runs above their line at the bottom of the range and below it across the top, crossing near `z ≈ 0.5`. **That is a curvature difference, which no amplitude change can absorb.** So the disputed coefficient does not rescue the shape, and more data of the same kind will sharpen this rather than wash it out.

> **What this does establish is what the ~30σ is and is not.** It is a detection that `a₀` evolves. **It is not a measurement of the exponent**, and the two must not be reported as though the first settled the second.

### 5.3a The systematics challenge — located, read, and checked

**An earlier draft of this section recorded this paper as possibly non-existent.** Three searches had returned no locatable record and the one detailed description came back only after its title was supplied in a query, so it was written up as an artifact risk rather than a source. **That was wrong, and the correction matters more than the error.**

**It exists.** Mikheil Rusishvili (2026), *“Three baryonic systematics, each sufficient: on the reported redshift evolution of the MOND acceleration scale,”* self-posted at `academia.edu/170831186`. **It is not in arXiv or A&A**, which is why the searches failed, and **it is not peer-reviewed** — an independent researcher on a platform with no quality filter. That is a real caveat and it is not a reason to ignore it: the content is specific, quantitative, and drawn from **Ciocan et al.'s own public catalogue.**

**Its three claims.** Each is asserted to be independently sufficient to account for the trend.

| # | systematic | claimed effect |
|---|---|---|
| 1 | **unmodelled molecular gas** — the survey models stellar disk + atomic gas only; adding Tacconi et al. (2018) fractions per galaxy (median `M_H₂/M*` rising `0.51 → 0.97` across the four redshift quartiles) | removes **82%** of the binned trend, **77%** of the fractional evolution |
| 2 | **dynamical-vs-photometric stellar-mass drift** — dynamical `M*` falls relative to photometric by **0.39 dex (3.6σ)** between extreme bins, **opposite in sign** to expected stellar-to-halo-mass evolution | matches the `+0.2` to `+0.45` dex **Ciocan et al. themselves state** would remove the trend entirely |
| 3 | **disk–halo degeneracy** — median **1.04 dex** across their six released halo models *for the same galaxy* | — |

Its conclusion: **`a₁` should not presently be used to constrain modified-gravity models.**

**What we can check, and what we cannot.** We do not have the catalogue, so **this paper cannot verify the analysis and does not claim to.** What is checkable from published numbers alone is whether the claimed effect sizes are **mutually coherent** — the same test the `α` conversion got. A critique whose arithmetic does not close can be set aside; one whose arithmetic does close cannot.

**The mechanism is simple enough to state in one line, which is part of why it is serious.** In the deep-MOND regime `g_obs = √(g_bar a₀)`, so the *inferred* scale is `a₀ = g_obs²/g_bar`. **If the baryonic budget is underestimated by a factor `f`, the inferred `a₀` is inflated by exactly `f`.** And if the missing fraction **grows with redshift** — which molecular gas demonstrably does — then **`a₀` appears to evolve even when it is exactly constant.**

**The arithmetic closes.** Writing `f = 1 + (M_H₂/M*)/(1 + M_HI/M*)` and scanning the unmeasurable atomic fraction:

| `M_HI/M*` | 0.0 | 0.1 | 0.2 | 0.3 | 0.5 | 1.0 |
|---|---|---|---|---|---|---|
| binned trend removed | 86% | **81%** | 77% | 73% | 67% | 55% |

> **The claimed 82% is reproduced at `M_HI/M* ≈ 0.1`** — and massive star-forming galaxies at `z ~ 1` are molecular-dominated, so that is **the expected regime rather than a tuned one.** The number falls out of two published quantities, their binned trend and Tacconi's fractions, **with no free parameter.**

**Claim 2 is close to self-certifying**, because the size required was stated by the survey team: the claimed 0.39 dex sits inside their own `0.2`–`0.45` dex window and exceeds the 0.334 dex of the fitted trend. **Claim 3 is the most damaging if true** — a per-galaxy modelling spread of 1.04 dex is **3.1× the 0.334 dex signal**, which would not bias the trend so much as deny that it is measured.

**Verdict, stated against interest.** **All three effect sizes are quantitatively coherent, and this is worse for the prediction than the exponent tension was.**

- **It attacks the detection, not the rate.** The `~30σ` was the one thing here being banked as a win.
- **ED loses that win, and the exclusion it was scored against.** If the evolution is a baryon-budget artifact, then constant-`a₀` MOND is not excluded either, and §1.2's position 2 comes back.
- **The 2.3σ falls with it.** A tension computed against an unreliable detection is itself unreliable. **The confirmation and the tension go together; neither can be banked separately.**
- **The resulting state is not “refuted” and not “vindicated.” It is UNTESTED** — the one survey that appeared to test this prediction may not have. That returns it to open, awaiting Rubin/Euclid.

### 5.3c Claim 1 is confirmed at the source, and the catalogue is public

**The first systematic does not need to be inferred from coherence. The survey states it.** Their baryonic acceleration is built as

$$a_\mathrm{bar}(r) = \frac{v_\mathrm{disk}(r)^2}{r} + \frac{v_\mathrm{HI}(r)^2}{r} \left(+\, \frac{v_\mathrm{bulge}(r)^2}{r}\right)$$

— **stellar disk, atomic gas, bulge. There is no molecular term.** And the authors name the consequence themselves: *“given typical molecular gas fractions of ∼30–50% at `z∼1`, this would introduce a systematic uncertainty of ∼0.2 dex in the total disk mass.”*

> **0.2 dex is their own figure, and the trend across their fitted range is 0.334 dex.** The survey therefore acknowledges a systematic **60% the size of its own signal**, in the one component whose fraction is known to grow with redshift. **What the re-analysis adds is not the existence of the systematic — that is conceded — but the claim that it is *differential* in `z` and therefore mimics the trend rather than merely offsetting it.**

**And the data is public.** *“All catalogues and data products from our disk–halo decomposition, including the RCs, can be found on the DARK website”* (`dark.univ-lyon1.fr/data-releases/`; the MUSE UDF sample of 126 galaxies covers this paper). **So the decisive test named in §6 is executable rather than requestable.** Nothing here waits on anyone's cooperation: the rotation curves, the disk–halo decompositions and the baryonic components are downloadable, and both open questions — the direct `a₀ ∝ H(z)^α` fit and the molecular-gas correction — can be settled from them.

> **This paper does not claim to have run that test.** It states that the test is available, that the prediction's status is **untested** until someone runs it, and that **running it is the only thing that would change the verdict in either direction.**

### 5.4 The verdict, stated plainly

> **Qualitative call: confirmed, and MOND's constant `a₀` excluded at 29σ.**
> **Quantitative rate: mildly disfavoured at 2.3σ on a computed conversion budget (§5.3), from one survey.**
>
> **And a caveat that outranks it (§5.3a): a re-analysis of that survey's own catalogue reports three baryonic systematics whose effect sizes check out arithmetically and which bear on the ~30σ DETECTION. If they hold, both the qualitative win and the quantitative tension go away together, and the correct verdict on this prediction is UNTESTED rather than either.**
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
| 8 | the survey's **linear** fit `a₁ = 1.59 ± 0.1` ×10⁻¹⁰ | **I — measurement** | Ciocan et al. |
| 8b | **`α = 1.15 ± 0.07` converted from row 8 by us**; `α = 1` then at **2.3σ** | **D-via-I — OUR REANALYSIS, not the survey's result** | **corrected 2026-09-07**; an earlier draft tagged this `I — same source`, which was wrong. **Refit and full budget now shown (§5.3) and reproducible: `event-density/theory/a0z_powerlaw_refit.py`** |
| 9 | the published `±0.04` omits the intercept, the cosmology and the reduction choice; a full conversion budget gives `α = 1.15 ± 0.07`, i.e. `α = 1` at **2.3σ** | **D-via-I** *(was `A — position`)* | **computed 2026-09-07, not asserted**: `event-density/theory/a0z_powerlaw_refit.py`. **The residual judgement is the intercept's uncertainty**, published to 2 s.f. with no error bar — at `±0.05` the tension is 3.2σ, at `±0.15` it is 1.8σ, and the paper does not get to pick |
| 10 | verdict: qualitative confirmed, rate disfavoured | **A → position** | composite |

**Step 9 was the paper's soft joint and is no longer one.** An earlier draft asserted the tension softened to "~1–2σ" without producing a budget, which the adversarial review correctly called special pleading. **The budget is now computed and it did not return the convenient answer**: 2.3σ, not 1–2σ. **Step 10 remains a position.** And the underlying exposure is unchanged: if the published `±0.04` is taken as complete, the prediction is excluded at 4.5σ and §5.4 should read differently.

---

## 9. Falsifiers

- **F1 (primary).** A multi-survey direct fit returning `α` inconsistent with 1 at ≥3σ refutes the prediction.
- **F2.** A demonstration that `a₀` is constant across redshift refutes it — and would also refute the ~30σ MUSE-DARK III result, so this is now a claim about that survey's reliability.
- **F3.** A derivation, within the framework, of a mechanism admitting `α ≠ 1` would remove the bet's content by making it fittable. **This is a falsifier of the claim's *status*, not of its value**, and is stated because a theory that can absorb any exponent has not predicted one.
