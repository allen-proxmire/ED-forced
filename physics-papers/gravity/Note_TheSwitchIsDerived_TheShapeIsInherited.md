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

The cosmic boundary sits at `u ≈ 9.5 × 10⁴` in units of the chain's own. Requiring `F_V5(u) < 1.14 × 10⁻⁷` there gives, for a power-law envelope `F_V5(u) ~ u^{-n}`:

$$\boxed{n > 1.40}$$

| Envelope | `F_V5` at `u = 9.5×10⁴` | Verdict |
|---|---|---|
| exponential `e^{-u}` | `e^{-95000}` | passes by ~10⁴ orders |
| stretched exponential `e^{-√u}` | `e^{-308}` | passes by ~130 orders |
| power law `n = 1` | `1.05 × 10⁻⁵` | **FAILS** |
| power law `n = 1.4` | `1.08 × 10⁻⁷` | marginal |
| power law `n = 2` | `1.11 × 10⁻¹⁰` | passes |

**This is a bound on a value-layer quantity, obtained from observation in a regime the quantity was never fitted in.** That is ED's stated methodology (`Paper_095`: form-derived, value-inherited) operating as designed — the form fixes the admissible class, and measurement narrows it.

---

## 7. Cross-arc check — the corpus's independent V5 identification passes

`Paper_090` §5.1 identifies V5 with **Maxwell stress relaxation** in polymer melts, whose envelope is **exponential**, and calls the exponential structural form a substrate-level consequence carried into the soft-matter regime.

An exponential envelope clears the §6 bound by roughly four orders of magnitude in the exponent. So the envelope class the corpus picked in soft matter, on entirely unrelated grounds, satisfies a constraint imposed by planetary ephemerides. **Two arcs, no shared machinery, consistent.** Recorded as a consistency check, not as evidence: the exponential in soft matter is itself identified rather than derived, so this is two inherited choices agreeing, not a prediction confirmed.

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
