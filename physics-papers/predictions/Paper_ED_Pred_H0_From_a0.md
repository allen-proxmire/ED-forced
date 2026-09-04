# Prediction 1.16 — The Hubble Constant from the MOND Acceleration Scale

**Allen Proxmire**

**September 2026**

**Series:** Event Density (ED) Generative Papers — predictions
**Status:** Forward prediction, **conditional on a coefficient the corpus currently disputes.** Registered 2026-09-04, before the data precision needed to test it exists.
**Anchors:** `Paper_029` §§5.5, 8.8 · `Paper_028` §3.2 (`R_H = c/H₀`) · ML 1.15 (the flagship exponent test) · `Gravity_TieredClaims_Ledger.md` Staleness #10, #38, #39
**Repository target:** `physics-papers/predictions/`

---

## Preamble: what this does NOT claim

1. **It does not derive the `2π`.** That factor is **Postulated / disputed** in this corpus (Staleness #10). This prediction is *conditional* on it, and says so at every step.
2. **It does not derive `H₀`.** ED inherits `H₀` (`Paper_029` §8.1). This is a *measurement* of it, not a prediction of its value.
3. **It is not offered as evidence for the `2π`.** Using the relation to measure `H₀` and then citing the result as support for the relation would be circular. §4 states the non-circular reading.
4. **It is not currently competitive.** The present uncertainty is `±6.3 km/s/Mpc` against a `5.6` tension gap. §3 gives the precision required.

---

## 1. The prediction

`Paper_029` ties the MOND acceleration scale to the cosmic decoupling surface at `R_H = c/H₀`:

$$a_0 = \frac{cH_0}{2\pi}.$$

Read the other way, this is a **measurement of the Hubble constant from galaxy rotation curves**:

$$\boxed{H_0 = \frac{2\pi a_0}{c}}$$

**This probe does not exist in MOND.** There `a₀` is a constant of nature with no connection to cosmology; there is nothing to invert. It exists only if the acceleration scale is set by the horizon, which is ED's central claim in this arc. It is therefore the sharpest ED-distinctive empirical statement available — the framework's one genuinely novel *measurement*, as opposed to a novel explanation of a known number.

## 2. Where it stands now

| `a₀` determination | `a₀` (`10⁻¹⁰ m/s²`) | Implied `H₀` (km/s/Mpc) |
|---|---|---|
| McGaugh, Lelli & Schombert 2016 (SPARC RAR) | `1.20 ± 0.02 ± 0.24` | `77.6 ± 15.6` |
| **Desmond 2023** (MNRAS 526, 3342) | **`1.19 ± 0.04 ± 0.09`** | **`77.0 ± 6.3`** |

Against the two camps, using Desmond:

| Comparison | Offset |
|---|---|
| SH0ES (local distance ladder), `73.0 ± 1.0` | **+0.62σ** |
| Planck 2018 (CMB), `67.4 ± 0.5` | **+1.50σ** |

**The probe currently favours the local distance ladder**, and is too imprecise to arbitrate.

## 3. What precision would make it decisive

The tension gap is ≈ `5.6 km/s/Mpc`.

| Target `H₀` precision | Required `a₀` precision | As a fraction of `a₀` |
|---|---|---|
| `±3.0` | `±4.6×10⁻¹²` | **3.9%** |
| `±2.0` | `±3.1×10⁻¹²` | **2.6%** |
| `±1.0` | `±1.5×10⁻¹²` | 1.3% |

Desmond 2023 is at ≈ **8%** combined. **Reaching arbitration-grade needs a factor of ~2**, which is a realistic target rather than a generational one: the systematic there is dominated by mass-to-light normalisation across the sample, not by anything irreducible.

**And the systematic budget is genuinely independent.** `a₀`'s dominant systematic is stellar population synthesis and disk/bulge mass-to-light ratios. That shares no systematics with the CMB sound horizon or with Cepheid/TRGB distance ladders. **A third probe in a two-camp tension is worth most when its errors are uncorrelated with both**, and this one's are.

## 4. The non-circular reading

The relation contains two quantities the corpus does not derive: the coefficient `k` in `a₀ = cH₀/k`, and `H₀` itself. One equation, two unknowns. So it must be read as a **joint constraint**, and it can be used in exactly two directions, never both at once:

- **Assume the coefficient** (`k = 2π`) → the relation measures `H₀`. This is §1, and its result is a *test*: if it converges on the CMB value, the coefficient is refuted; if on the ladder value, the coefficient survives something it could have failed.
- **Assume `H₀`** from an external probe → the relation measures the coefficient. This is Staleness #39's reading, and it currently returns `k = 5.67 ± 0.47` at `H₀ = 70` against `2π = 6.283`.

**What is never legitimate** is measuring `H₀` from the relation and then citing the agreement as support for the coefficient. This paper does not do that, and any downstream use that does is misusing it.

## 5. How it composes with the flagship

ML 1.15 predicts `a₀(z) = cH(z)/(2π)` with the exponent **exactly 1**, and `Paper_029` §2.5 row 14 correctly records that the exponent is **independent of the coefficient dispute**. The two tests are therefore **separable and use one dataset**:

| Feature of `a₀(z)` | Tests | Coefficient-dependent? |
|---|---|---|
| **Shape** across redshift — `a₀(z)/a₀(0) = H(z)/H₀` | the exponent: ED's `α = 1` vs MOND's `α = 0` | **No** |
| **Normalisation** at any epoch | the joint (`k`, `H₀`) constraint of §4 | Yes |

A redshift survey of the radial acceleration relation therefore delivers ED's flagship test and this one together. **The second half has not previously been written down**, and it is free with data already being collected for the first.

## 6. Falsification criteria

- **F1 (the sharp one).** If `a₀` tightens to `±0.05×10⁻¹⁰` and the CMB `H₀` is correct, the implied `H₀` sits ≈ `3σ` from truth and **the `2π` is refuted by measurement** — with no derivation attempted on either side. Given that four structural routes reach `cH₀` and none reaches the coefficient (Staleness #38), this is a live route to settling the question.
- **F2.** If the local-ladder `H₀` is correct and `a₀` settles near `1.13×10⁻¹⁰`, the coefficient is confirmed below `1σ`. That would *not* derive the `2π`, but it would move it from *disputed* to *empirically supported*, which is the strongest status an inherited value can hold.
- **F3.** If ML 1.15's exponent test fails (`α ≠ 1`), the horizon-tying itself fails and this prediction goes with it — the inversion assumes `a₀` reads the live horizon.
- **F4.** If an `a₀` determination is shown to depend materially on the assumed interpolation family, the inversion is blunted. *Checked and currently negative:* `a₀` is defined by the deep-MOND normalisation and the asymptotes cross there for every family (`Note_a0_ThresholdFromHorizonCompetition.md` §5), and Desmond's inference marginalises over functional forms yet lands within `0.01` of the 2016 fixed-form value.

## 7. Audit table

| # | Claim | Tier | Basis |
|---|---|---|---|
| 1 | `a₀ = cH₀/(2π)` | **P / disputed** | `Paper_029`; the coefficient is Staleness #10 |
| 2 | `H₀ = 2πa₀/c` is an inversion of 1 | **D** | algebra |
| 3 | The probe has no MOND analogue | **D-via-I** | in MOND `a₀` is a constant of nature; nothing to invert |
| 4 | `H₀ = 77.0 ± 6.3` from Desmond 2023 | **D-via-I** | 2 + an inherited measurement |
| 5 | `+0.62σ` vs SH0ES, `+1.50σ` vs Planck | **D-via-I** | arithmetic on published values |
| 6 | ≈4% `a₀` precision needed for `±3 km/s/Mpc` | **D** | error propagation |
| 7 | `a₀`'s systematics are uncorrelated with CMB and ladder systematics | **I** | stellar M/L vs sound horizon vs Cepheid/TRGB |
| 8 | Shape and normalisation tests are separable | **D** | 5 + `Paper_029` §2.5 row 14 |
| 9 | The relation is a joint constraint, usable in one direction at a time | — | methodological |

**Verdict: M3 — form-derived, value-inherited, and conditional on a disputed coefficient.** The inversion is trivial; the content is that ED is the only framework in which the inversion means anything, and that it is testable now.

---

## 8. Registration note

This is recorded on **2026-09-04**, when the probe returns `77.0 ± 6.3` and cannot discriminate. It is registered *before* the precision required to test it exists, so that a later agreement is a prediction rather than a postdiction. The corpus's standing caution on postdiction-as-evidence applies with full force here.
