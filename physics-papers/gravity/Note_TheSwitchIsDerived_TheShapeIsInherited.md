# The Switch Is Derived, Its Sharpness Is Not: μ as the V5 Envelope

*Opened 2026-09-04. Discharges the first debt of `Note_a0_ThresholdFromHorizonCompetition.md` §6 and answers its falsifier F1. Produces one new observational bound on a value-layer quantity.*

---

## Preamble: what this note does NOT claim

1. It does **not** derive `a₀`'s coefficient. The `2π` residual of Staleness #10 and Target #18 is untouched; this note reaches `cH₀` bare, exactly as the threshold note did.
2. It does **not** derive the MOND interpolation function `μ`. It argues the opposite: that `μ`'s shape is **structurally inherited**, and identifies the slot it is inherited into.
3. It does **not** claim the transition is sharp. It withdraws that claim, which the threshold note asserted.
4. The bound in §6 constrains an inherited quantity from observation. It is **not** a prediction of that quantity's value.

---

## 1. The debt

`Note_a0_ThresholdFromHorizonCompetition.md` §3 proposed that a chain has two V5-saturation boundaries — its own acceleration horizon at `R_a = c²/a` and the cosmological one at `R_H = c/H₀` — and that **only the nearer binds**, giving a regime change at `a = cH₀`. Its §6 conceded the switch was *asserted*, and its F1 set the test:

> If a construction carrying both boundaries shows `Γ_cross` collapsing at the *farther* boundary, or at neither distinctly, the switch is not a switch and the mechanism fails.

That construction already exists in the corpus. It was not consulted.

---

## 2. The construction the corpus already has

`Paper_039` §3.1 defines the cross-bandwidth explicitly:

$$\Gamma_{\mathrm{cross}}(r) = \int_{\mathcal{K}_{\mathrm{cross}}(r)} \sum_{u_{<r},\,u_{>r}} K_{V5}(u_{<r}, u_{>r})\, b_K(u_{<r})\, b_K(u_{>r})\, d\mu_{\mathcal{K}}$$

Three properties of this object are already fixed elsewhere in the corpus, and together they settle F1:

| Property | Source | Status |
|---|---|---|
| `Γ_cross` is a **single integral over one kernel** `K_V5`, not a sum of independent channels | `Paper_039` §3.1 | definitional |
| The V5 envelope depends on **Lorentz-invariant separation** (curved case via the Synge world-function) | `Paper_090` §4.4 | structural |
| `F_V5` is **bounded and decaying**, with no δ-limit and no infinite-width limit | `Paper_090` §4.2 + §3.4, Theorem N1 (`Paper_089`) | Derived (conditional) |

---

## 3. Result A — the nearer boundary binds, and it needs no new postulate

The two horizons are not two separate attenuations that have to be argued to compose. By `Paper_047_5` (M3) they are **one substrate object on two parameter axes**, and by `Paper_090` §4.4 the kernel that carries cross-chain content is a function of a **single** argument: invariant separation.

A horizon is a surface at which that separation diverges — beyond it, no invariant-finite path connects source to chain. So the situation is not "two envelopes multiplying." It is one monotone decaying function of one variable, with **two ways for its argument to run away**. The integrand is driven to zero by whichever runs away first, and that is the nearer boundary in separation.

$$\Gamma_{\mathrm{cross}} \longrightarrow 0 \quad\text{at}\quad R_{\min} = \min(R_a,\, R_H) \qquad\Longrightarrow\qquad a_{\mathrm{switch}} = cH_0$$

**This is shape-independent.** It uses only *bounded and decaying* — no property of `F_V5` beyond its admissible class, and no postulate that was not already carried. Given the corpus-wide postulate load measured the same day (173 named postulates, Staleness #33), a mechanism that adds none is worth stating plainly.

**F1 is answered in the affirmative: `Γ_cross` collapses at the nearer boundary.**

---

## 4. Result B — but the *sharpness* is not derived, and the threshold note over-claimed it

`Note_a0_ThresholdFromHorizonCompetition.md` §3 says:

> That is a **discrete switch**, not a smooth response.

**That is one notch too strong, and this note withdraws it.** What §3 above derives is *which* boundary dominates, and where the handover sits. How abruptly the handover happens is set by the profile of `F_V5` near its cutoff, and `Paper_090` **§7.2 is explicit**:

> The specific functional shape of `F_V5` within the admissible class is **value-layer content**.

A hard-edged envelope gives a discrete switch. A broad one gives a gradual crossover with the same crossover scale. Both are admissible, the corpus does not choose between them, and the observational fact — rotation curves turn over gradually — therefore **selects** the envelope rather than testing it.

*(This is a claim-strength correction to a document written earlier the same day. It is checklist failure mode 7, committed while documenting failure mode 7.)*

---

## 5. Result C — `μ` **is** the V5 envelope, and that is why every derivation of it has failed

This is the substantive result.

`Paper_030`'s bilocal cross-term is V5-mediated horizon content reaching the chain. Its magnitude at a given chain acceleration is `Γ_cross` weighted by `F_V5`. The MOND interpolation function `μ` measures exactly the fractional handover between "cross-term negligible" (Newtonian) and "cross-term dominant" (deep-MOND). So the shape of `μ` is the coarse-grained image of the shape of `F_V5`.

**Form-IDENTIFIED (M2)**, conditional on `Paper_030`'s own construction of the bilocal term. Not a proof; a placement.

What it buys is an explanation of a repeated failure. Three separate attempts to derive `μ` from the substrate have been blocked (`Note_a0_ThresholdFromHorizonCompetition.md` §5b; `Paper_030` §6.3; Staleness #15). The blockage has been read as "not yet done." It is not:

> **`μ` cannot be derived without deriving the V5 envelope shape, and `Paper_090` §7.2 lists that shape as value-layer inherited. `μ` is not an open derivation. It is an inherited quantity that has been mis-filed as an open one.**

This also **closes a gap in the arc's own bookkeeping**. `Paper_026` preamble item 3 already carries the analogous disclaimer for the *other* kernel — *"the V1 kernel envelope shape is not derived (`Paper_089` §4.4 — value-layer)"* — and no gravity or dark-sector paper makes the corresponding statement for V5, which is the kernel that actually carries the horizon coupling. The disclaimer was written for V1 and never propagated to V5.

**Consequence for Target #18.** The `2π` is a coefficient on the *scale*, not on the shape, so nothing here recovers it. But it removes one candidate hiding place: the factor cannot be buried in the interpolation function, since the interpolation function's shape is inherited and its normalization is pinned by the deep-MOND asymptote (already shown in the threshold note §5).

---

## 6. Result D — Cassini bounds the envelope: it must decay faster than `u^{-1.4}`

The threshold note's F4 is sharp: if the bilocal cross-term is active at solar-system accelerations, `√(a_N a₀)` predicts an anomalous acceleration far above ephemeris bounds and `Paper_030` is refuted outright. Everything rests on the cosmic content being screened at Saturn. **How hard must the screening be?**

At Saturn (`R = 1.4335 × 10¹² m`):

| Quantity | Value |
|---|---|
| `a_N = GM_☉/R²` | `6.458 × 10⁻⁵ m/s²` |
| chain's own boundary `R_a = c²/a_N` | `1.392 × 10²¹ m` |
| cosmological boundary `R_H = c/H₀` (H₀ = 70) | `1.322 × 10²⁶ m` |
| **separation ratio `u = R_H/R_a`** | **`9.50 × 10⁴`** |
| cross-term if unscreened, `√(a_N a₀)` | `8.80 × 10⁻⁸ m/s²` |
| Cassini-class ephemeris bound | `~10⁻¹⁴ m/s²` |
| **suppression required** | **`8.80 × 10⁶`** |

The cosmic boundary sits at `u ≈ 9.5 × 10⁴` in units of the chain's own.

**The cross-term is screened by `√F`, not by `F`, and this note first got that wrong.** `Paper_030` §5.2 builds the bilocal channel strain as `σ_bilocal ∝ √(GM a₀)` — a **geometric mean** of the local and horizon sides — and `Paper_030` §3.2 makes `a₀` **linear** in horizon content (the `Paper_029` dipole amplitude). So screening the horizon content by `F` sends `a₀ → a₀F` and therefore the cross-term to `√(a_N a₀ F) = √(a_N a₀)·√F`. Requiring `√F < 1.14 × 10⁻⁷`, i.e. **`F_V5(u) < 1.29 × 10⁻¹⁴`**, gives for a power-law envelope `F_V5(u) ~ u^{-n}`:

$$\boxed{n > 2.79}$$

> ⚠ **Corrected 2026-09-04 (same day). This section first read `n > 1.40`**, from treating the cross-term as linearly screened. It is a geometric mean, so it takes the square root of the suppression and the required exponent **doubles**. Found while working §10 below. The constant `a₀` term *is* linearly screened and needs only `n > 0.82`, so **the cross-term is the binding constraint**. Conclusions unchanged for exponential envelopes; changed for power laws, where `n = 2` now **fails**.

| Envelope | `F_V5` at `u = 9.5×10⁴` | Verdict |
|---|---|---|
| exponential `e^{-u}` | `e^{-95000}` | passes by ~10⁴ orders |
| stretched exponential `e^{-√u}` | `e^{-308}` | passes by ~130 orders |
| power law `n = 1` | `1.05 × 10⁻⁵` | **FAILS** |
| power law `n = 1.4` | `1.08 × 10⁻⁷` | **FAILS** *(passed under the erroneous linear-screening reading)* |
| power law `n = 2` | `1.11 × 10⁻¹⁰` | **FAILS** *(same)* |
| power law `n = 2.79` | `1.30 × 10⁻¹⁴` | marginal — the boundary |
| power law `n = 3` | `1.17 × 10⁻¹⁵` | passes |

**This is a bound on a value-layer quantity, obtained from observation in a regime the quantity was never fitted in.** That is ED's stated methodology (`Paper_095`: form-derived, value-inherited) operating as designed — the form fixes the admissible class, and measurement narrows it.

---

## 7. Cross-arc check — the corpus's independent V5 identification passes

`Paper_090` §5.1 identifies V5 with **Maxwell stress relaxation** in polymer melts, whose envelope is **exponential**, and calls the exponential structural form a substrate-level consequence carried into the soft-matter regime.

An exponential envelope clears the §6 bound by roughly four orders of magnitude in the exponent. So the envelope class the corpus picked in soft matter, on entirely unrelated grounds, satisfies a constraint imposed by planetary ephemerides. **Two arcs, no shared machinery, consistent.** Recorded as a consistency check, not as evidence: the exponential in soft matter is itself identified rather than derived, so this is two inherited choices agreeing, not a prediction confirmed.

---

## 10. The regime map — half derived, half blocked by a contradiction in `Paper_030`

*Added 2026-09-04, attacking the second debt of `Note_a0_ThresholdFromHorizonCompetition.md` §6: that the switch in **which boundary binds** is assumed to coincide with the switch between **Newtonian and deep-MOND dynamics**.*

### 10a. The Newtonian half is derivable, and it is the half Cassini cares about

Above `cH₀` the chain's own boundary is nearer, so cosmic content is screened by `F_V5(u)` with `u = R_H/R_a > 1`. Both horizon-dependent terms in `Paper_030` §6.3's profile then die:

- the pure-source cosmic term `a₀ → a₀ F` — linearly,
- the bilocal cross-term `√(a_N a₀) → √(a_N a₀)·√F` — as the square root,

leaving `a → a_N`. **Newtonian dynamics are recovered from the screening, not assumed.** This discharges what `Paper_030` §7.1 previously had to declare by scoping ("this construction has no content here"), and it is exactly what §6's Cassini bound quantifies.

### 10b. The deep-MOND half cannot be mapped, because the target regime is inconsistently specified

Below `cH₀` the cosmic boundary binds and its content is unscreened. To complete the map one must show that this yields `a ≈ √(a_N a₀)`. **It does not, on `Paper_030`'s own profile.** §6.3 gives

$$a(R) = a_N + a_0 + \sqrt{a_N a_0} \qquad \text{(as it stood; corrected later the same day — see §11)}$$

and §7.1 asserts that in the deep-MOND regime (`a_N ≪ a₀`) the *"bilocal cross-term dominates over both pure-source terms."* **That is arithmetically false.** Writing `a_N = ε a₀` with `ε ≪ 1`, the three terms are `εa₀`, `a₀` and `√ε a₀`, and since `ε < √ε < 1` for all `ε < 1`, the ordering is **always**

$$a_N \;<\; \sqrt{a_N a_0} \;<\; a_0 .$$

| `a_N/a₀` | `a_N` | cross `√(a_N a₀)` | pure cosmic `a₀` | dominant |
|---|---|---|---|---|
| `1` | `1.20×10⁻¹⁰` | `1.20×10⁻¹⁰` | `1.20×10⁻¹⁰` | all equal |
| `10⁻¹` | `1.20×10⁻¹¹` | `3.79×10⁻¹¹` | `1.20×10⁻¹⁰` | **`a₀`** |
| `10⁻²` | `1.20×10⁻¹²` | `1.20×10⁻¹¹` | `1.20×10⁻¹⁰` | **`a₀`** |
| `10⁻⁴` | `1.20×10⁻¹⁴` | `1.20×10⁻¹²` | `1.20×10⁻¹⁰` | **`a₀`** |

The constant cosmic term dominates everywhere in the regime `§7.1` describes, and it dominates by a factor `1/√ε` that **grows** as one goes deeper. A constant acceleration floor `a → a₀` gives `v² = a₀R`, i.e. **rising** rotation curves, not flat ones. So §6.3's profile and §7.1's regime description cannot both be right.

### 10c. The resolution is already flagged in the paper, and this makes it load-bearing

`Paper_030` §3.2 carries a flag dated the same day:

> the step above converts a **response** into a **source** … `Paper_029` §§3.3/5.1 make the horizon content first order in the chain's own acceleration … and identically zero for a non-accelerating chain … **This is the origin of the `Σ₀` problem.**

**That flag is the resolution.** Drop the spurious standalone `a₀` — which `Σ₀ = -a₀R` produced by integrating a response as if it were a constant background — and the profile becomes `a = a_N + √(a_N a₀)`, whose deep limit **is** `√(a_N a₀)`. §7.1's description is then correct and the regime map closes.

**So the second debt is not blocked by anything new. It is blocked by `Σ₀`, and the finding here is that `Σ₀` is not a bookkeeping nicety.** The flag was recorded as an attribution problem; it is in fact **load-bearing for whether ED reproduces MOND at all**. Until it is resolved, "the cosmic boundary binds" cannot be shown to mean "deep-MOND dynamics," because on the paper's own profile the deep limit is a constant, not a geometric mean.

**Caution, and it is a real one.** The obvious repair — restore the acceleration-dependence `a₀ → k|a|` that `Paper_029` actually derives — is the move Target #19 has **already banked as a negative**: it yields `a ∝ GM H₀/R²`, Newtonian-like, and breaks MOND. So dropping the term and restoring its `|a|`-dependence are different repairs with different fates, and only the first is on the table here. **Neither is performed in this note.**

---

## 11. Resolving `Σ₀` — `a₀` is a normalization, and it was used as a force

*Added 2026-09-04, attacking Target #22. The resolution is a re-reading of `Paper_029`, not new physics.*

### 11a. `Paper_029` derives two different objects, and `Paper_030` merged them

§5.1 of `Paper_029` states the cosmic anisotropic content seen by an accelerating chain:

$$\rho_{\mathrm{cosmic}}(\theta,\phi) = \rho_0\,\frac{|\vec a|}{c}\,\cos\theta + \mathcal{O}\!\left(\frac{|\vec a|}{c}\right)^{2}, \qquad \rho_0 = cH_0 .$$

Two distinct things sit in that one line:

| Object | What it is | Depends on `|a|`? |
|---|---|---|
| `ρ₀ = cH₀` | the **normalization** of the horizon content — the characteristic horizon-scale acceleration | **no** |
| `(|a|/c)·cosθ` | the **response amplitude** — how much anisotropy this particular chain actually sees | **yes**, first order, zero at `a = 0` |

`a₀ = cH₀/(2π)` is the *projected normalization*. It is **not** the response. And `Paper_029` says so in its own words in §4.4: `a₀` is *"the **transition acceleration** — the **threshold** between Newtonian and deep-MOND dynamics"*, whose role is set by *"the **ratio** of local-source-induced `a_N` to cosmic-anisotropy `a₀`"*. **A ratio is a comparison. A threshold is a scale. Neither is a force.**

### 11b. The error, stated precisely

`Paper_030` §3.2 writes `Σ₀(R) = -a₀R` and takes its gradient, `-dΣ₀/dR = a₀`, obtaining a **uniform background acceleration of magnitude `a₀` acting on every chain**. That is the normalization promoted to a field. `Paper_029` licenses no such thing: strip the response amplitude `(|a|/c)cosθ` and what remains is a *scale*, not a source.

**This sharpens §3.2's existing flag rather than replacing it.** The flag says the step *"converts a response into a source"*, and that is right. §11a says which part got converted: not the response, but the response's **normalization**.

### 11c. Why the banked negative failed, and why it is the same mistake

Target #19 records a failed repair: restore `a₀ → k|a|`, and deep-MOND self-consistency gives `a² ∝ GMH₀|a|/R²`, hence `a ∝ GMH₀/R²` — Newtonian-like. **That is the same conflation from the other side.** It takes `a₀`, which is the *normalization*, and gives it the `|a|`-dependence that belongs to the *amplitude*. One error promotes a scale to a field; the other demotes it to an amplitude. Neither respects the split in §11a, and both break MOND.

**So the banked negative is now explained rather than merely recorded**, which is the useful part: it was not a near-miss to be retried with better algebra.

### 11d. The repair, and the cross-term survives — because `a₀R` is legitimate as *content* and illegitimate as *potential*

Drop the standalone term. The profile becomes

$$a(R) = a_N + \sqrt{a_N a_0},$$

whose limits are both correct with **no regime switch needed**: `a → a_N` for `a_N ≫ a₀` (the cross-term falls off as `√(a₀/a_N)`), and `a → √(a_N a₀)` for `a_N ≪ a₀`. `Paper_030` §7.1's deep-MOND branch becomes correct and §10b's contradiction is gone.

**The cross-term is not lost with the term it was built from, and the reason is precise.** §4.2 needs the per-channel horizon *content* `b_K^horizon = a₀R/N_horizon`. The expression `a₀R` is a content measure: at the horizon it evaluates to `a₀R_H = c²/(2π)`, a potential depth of order `c²`, which is what a horizon should have. **What is illegitimate is not the expression but one use of it** — taking `-d/dR` of it and calling the result a force on the chain. `Paper_030` used `a₀R` both ways; §4.2's use is licensed and §3.2's is not.

### 11e. What this does and does not fix

**Fixes:** the §10b contradiction; `Paper_030` §7.1's deep-MOND branch; the need for a physical switch to make the deep limit come out; and it explains the banked negative.

**Does not fix — and this matters:** the resulting profile still saturates as `1 - μ ~ x^{-1/2}`, so at Saturn it still predicts `≈ 8.8×10⁻⁸ m/s²` against a `~10⁻¹⁴` bound. **Cassini still requires the screening of §10a and the envelope bound `n > 2.79` of §6.** Removing `Σ₀` fixes the deep end, not the near end. The two results are independent and both are needed.

**Does not fix:** the `2π`. `a₀` is now correctly a normalization, and the factor is a coefficient *on* that normalization — exactly where Staleness #10 left it.

### 11f. Tier, and what is owed

**M2 — an internal-consistency resolution by re-reading, not a new derivation.** It removes a term that `Paper_029` never licensed, on the strength of `Paper_029` §4.4's own characterization of `a₀` as a threshold. No new postulate; census confirms the count did not move.

**Owed — DISCHARGED 2026-09-04, the rewrite was applied on instruction (Staleness #37).** `Paper_030` §§3.2, 3.4, 5.3, 6.3, 7.1 and the abstract are corrected: `Σ₀` is a content normalization, no gradient is taken, the profile is `a = a_N + √(a_N a₀)`, and §5.3's explicit regime assumption is **removed** because the deep-MOND branch now follows as a limit. *Original wording:* `Paper_030` §3.2 needs rewriting rather than flagging — `Σ₀` should be presented as a **content normalization** feeding §4.2, with no gradient taken and no standalone term. That is an edit to a load-bearing derivation and is **not performed here**; it is recorded as the remaining work on Target #22. Until it is done the paper still displays a profile (§6.3) whose deep limit is wrong.

---

## 8. What this owes

- **The regime map is still asserted.** That the binding-boundary handover *coincides* with the Newtonian/deep-MOND dynamical change remains the natural reading and is still not shown. This note discharges the first debt of the threshold note's §6, not the second.
- **`√(a_N a₀)` is still `Paper_QuadraticStrain_v1` §5's job.** Unchanged.
- **The `2π` is untouched.** Three routes to the scale, none to the coefficient (threshold note §4). This adds a fourth route to the scale and still none to the coefficient.
- **§6's bound assumes a single-power envelope near `u ~ 10⁵`.** A multi-scale envelope could evade it; the bound constrains the admissible class, it does not uniquely fix `n`.

## 9. Falsification criteria

- **F1.** If the V5 envelope is shown, from the substrate, to decay slower than `u^{-1.4}`, then `Paper_030`'s bilocal term is active at Saturn and the account is refuted by Cassini. §6 makes this a live, sharp test rather than a worry.
- **F2.** If `Γ_cross` is shown *not* to be a function of invariant separation alone — if a second independent argument enters — the §3 min-argument loses its footing and the switch returns to being asserted.
- **F3.** If a substrate-level derivation of the V5 envelope shape is produced, §5's identification converts from "`μ` is inherited" to "`μ` is derived," and the interpolation function becomes a genuine prediction. **That is the highest-value open item this note creates.**

---

## Audit table

| # | Claim | Tier | Basis |
|---|---|---|---|
| 1 | `Γ_cross` is one integral over one kernel of invariant separation | I | `Paper_039` §3.1; `Paper_090` §4.4 |
| 2 | `F_V5` bounded, decaying, finite-width | D (conditional) | Theorem N1, `Paper_089` |
| 3 | The nearer saturation boundary binds; cutoff at `min(R_a, R_H)` | **D (conditional)** | 1 + 2 + `Paper_047_5` (M3). Shape-independent; no new postulate |
| 4 | `a_switch = cH₀` | D-via-I | 3 + `R_H = c/H₀` (`Paper_028`) |
| 5 | The *sharpness* of the handover is not derived | — | `Paper_090` §7.2 (value-layer). Withdraws "discrete switch" |
| 6 | `μ`'s shape is the coarse-grained V5 envelope shape | **form-IDENTIFIED (M2)** | 5 + `Paper_030`'s bilocal construction. Placement, not proof |
| 7 | `μ` is inherited, not an open derivation | D-via-I | 6 + `Paper_090` §7.2 |
| 8 | Cassini ⟹ `n > 1.40` for a power-law envelope | D-via-I | arithmetic on `Paper_030`'s own cross-term + ephemeris bound |
| 9 | Soft-matter's exponential envelope clears the bound | I | `Paper_090` §5.1; consistency check only |
| 10 | The `2π` is unaffected | — | verdict-framing |

**Verdict: M2.** One structural result (the switch, derived and postulate-free), one re-classification (`μ` inherited, not open), one new observational bound on a value-layer quantity, and one claim withdrawn.
