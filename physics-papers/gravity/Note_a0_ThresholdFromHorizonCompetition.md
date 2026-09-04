# Where MOND's Threshold Comes From: Two Saturation Boundaries, and Which One Binds

**Allen Proxmire**

**September 2026**

**Series:** Event Density (ED) Generative Papers — gravity arc, working note
**Status:** Research note on Research Target #19. **Proposes a threshold mechanism and does not complete it.** The mechanism is assembled entirely from results the corpus already holds; nothing new is postulated. It produces a threshold of the right structural kind, at `a = cH₀` — which converges with Target #18's independent route and leaves the same single factor unexplained.
**Anchors:** `Paper_047_5_HorizonUniversalization` (the load-bearing input) · `Paper_028` §3.2 (the crossover template) · `Paper_029` §§3.3/5.1 (the linear response) · `Paper_039` (V5 saturation) · Staleness #13 · `Note_a0_TwoPi_RepairRoutes.md`
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: what this note does NOT claim

1. **It does not derive `a₀`.** It proposes a mechanism for the *threshold*, and that mechanism lands on `cH₀`, not on the measured `1.2 × 10⁻¹⁰ m/s²`.
2. **It does not resolve the `2π`.** It makes the `2π` problem sharper by reaching the same bare `cH₀` a second, independent way.
3. **It does not replace `Paper_029`.** The linear-in-`|a|` response stands; this note argues it describes behaviour *within* a regime, not the regime change.
4. **No new postulate is introduced.** Every ingredient is an existing corpus result, used as stated.
5. **It does not claim the numerical gap is resolved.** The mechanism's crossover sits a factor of ~5.7 above the fitted `a₀`, and §5 states plainly that this is unresolved rather than explained away.

---

## 1. The question

Target #19: `Paper_029` §§3.3/5.1 give the cosmic horizon's contribution to an accelerating chain as **first order in the chain's own acceleration**, `ρ_cosmic(θ) ∝ ρ₀(|a|/c)cosθ`, and identically zero for a non-accelerating chain. MOND needs a **threshold** — behaviour that changes character at `a₀`. A linear response does not produce a threshold.

`Paper_030` §3.2 papered over this by integrating a *constant* `a₀`, converting a response into a source, which is the defect recorded as Staleness #13.

**The reframe this note proposes:** the threshold is not in the response at all. It is in **which boundary is doing the saturating.**

---

## 2. The ingredient the corpus already has

`Paper_047_5_HorizonUniversalization` (verdict M3) states that the four standardly-distinguished horizon types —

> (i) black-hole event horizons, (ii) **Rindler acceleration horizons**, (iii) cosmological de-Sitter horizons, (iv) acoustic/dumb horizons in fluid analogues — are projections of the same ED substrate object: **the V5-saturated boundary at which cross-chain bandwidth `Γ_cross` collapses** (`Paper_039`). The four types differ in which parameter axis (mass / **acceleration** / **Hubble rate** / flow gradient) parameterizes the projection.

So in ED, a chain's own acceleration horizon and the cosmological horizon are **the same substrate object on two different axes**. This is a standing M3 result, and it has not been connected to `a₀`.

---

## 3. The mechanism

A chain in a galaxy has **two** V5-saturation boundaries, not one:

| Boundary | Set by | Radius |
|---|---|---|
| Rindler / acceleration horizon | the chain's own acceleration `a` | `R_a = c²/a` |
| Cosmological horizon | Hubble recession | `R_H = c/H₀` |

Both are the same object by `Paper_047_5`: the surface where `Γ_cross` collapses and cross-chain content stops reaching the chain.

**Only the nearer one binds.** Cross-chain content is cut off at whichever saturation boundary the chain meets first; the farther boundary is causally irrelevant because nothing was getting through from beyond the nearer one anyway. That is a **discrete switch**, not a smooth response — and it is the same competition `Paper_028` §3.2 already runs to fix `R_H` itself, where kernel propagation at `c` races Hubble recession at `H₀R` and the crossover is defined by equality.

Applying the identical argument one level up, the switch is at `R_a = R_H`:

$$\frac{c^2}{a} = \frac{c}{H_0} \quad\Longrightarrow\quad \boxed{a = cH_0}$$

- **`a > cH₀`** — the chain's own acceleration horizon is *inside* the cosmic one. The chain's dynamics are bounded by its own saturation boundary; cosmic content is already cut off before it matters. **Newtonian regime.**
- **`a < cH₀`** — the cosmic horizon is the binding one. Horizon content reaches the chain and dominates. **Deep-MOND regime.**

**This is a threshold of the right structural kind.** Nothing is nonlinear in `|a|`; the linear response of `Paper_029` is untouched and describes behaviour *within* a regime. What changes at the threshold is *which* boundary is saturating. **A linear response plus a handover in which horizon binds gives a threshold.** That is the answer Target #19 was asking for, and it required no new postulate.

> ⚠ **Corrected 2026-09-04 (same day), by `Note_TheSwitchIsDerived_TheShapeIsInherited.md`.** This paragraph and the sentence above it previously read *“that changes **discontinuously**”* and *“That is a **discrete switch**, not a smooth response”*. **The discreteness is withdrawn.** The follow-up note derives the handover from the corpus's own `Γ_cross` construction (`Paper_039` §3.1) and finds it **shape-independent as to *where* it sits and shape-*dependent* as to how sharp it is** — the sharpness is the profile of the V5 envelope near its cutoff, which `Paper_090` §7.2 lists as **value-layer inherited**. So a discrete switch and a gradual crossover are both admissible and the corpus does not choose. **What survives is the crossover scale `cH₀`, which is what the mechanism was for.**

---

## 4. What this does to Target #18

The mechanism gives `a₀ = cH₀`. **Bare. No `2π`.**

Target #18's Route 2, built from a completely different starting point — Rindler smoothness and the de Sitter temperature — found that the *symmetric* matching condition `T_a = T_H` also gives `a₀ = cH₀`, and that only an asymmetric, unmotivated condition produces the `2π`.

**Two independent ED mechanisms now converge on `a₀ ~ cH₀`, and neither produces the `2π`.** That cuts two ways, and both matter:

- **It strengthens the horizon-tying claim considerably.** The physically substantive content of ED's MOND account — that `a₀` is set by the cosmic horizon — now has two independent derivations rather than one, from a threshold argument and from a thermal argument that share no machinery.
- **It isolates the `2π` and makes it look inherited.** The factor is not produced by the threshold mechanism, not produced by the symmetric thermal condition, and provably cancels in the azimuthal-Fourier derivation that currently claims it (Staleness #10). Three routes to the scale; none to the coefficient.

The honest reading is that **`a₀ ~ cH₀` is form-derived and the coefficient is inherited**, unless Target #18's asymmetric matching condition can be grounded.

---

## 5. The numerical gap — check run 2026-09-04

`cH₀ = 6.80 × 10⁻¹⁰ m/s²` (at `H₀ = 70`). Fitted MOND `a₀ ≈ 1.2 × 10⁻¹⁰`. Ratio **5.67**, against `2π = 6.283`. Across the Hubble-tension range `H₀ ∈ [67, 74]` the ratio runs **5.42–5.99**, so it is `2π` to within 5–14%.

§5 previously offered two readings and declined to choose. **Reading 2 has now been checked, and its strong form is refuted.**

### Strong form: refuted, by construction

The claim was that a fitted `a₀` inside an interpolation function `μ(x)` might not be the same object as a mechanism's crossover, so `μ` could absorb the factor.

It cannot. In any MOND-class law `μ(a/a₀)·a = a_N`, the asymptotes are `a = √(a_N a₀)` (deep) and `a = a_N` (Newtonian). They are equal when `a_N = a₀`, and then `a = a₀`. **The asymptotes cross at `a₀` for every `μ` family**, because `a₀` is *defined* as the deep-MOND normalization. The shape of `μ` controls how the curve rounds the corner, not where the corner is. Confirmed numerically across three families (`x/(1+x)`, `x/√(1+x²)`, `x/(1+x⁵)^{1/5}`): the solution at `a_N = a₀` lands at `1.10–1.62 a₀` in all of them.

**No choice of `μ` puts the transition at `cH₀` while the fitted `a₀` is `cH₀/(2π)`.**

### Weak form: survives, and is untestable as things stand

A residual version remains. The mechanism's crossover need not correspond to the asymptote-crossing; it could mark the **onset** of horizon influence — where departures from Newtonian first appear. That is a different feature of the curve, and it is `μ`-dependent:

| `μ(x)` | `a_N` where `a` departs 10% from Newtonian |
|---|---|
| simple, `x/(1+x)` | **9.0 `a₀`** |
| standard, `x/√(1+x²)` | 2.0 `a₀` |
| sharp, `x/(1+x⁵)^{1/5}` | 1.0 `a₀` |

`cH₀ = 5.67 a₀` sits inside that range, so the numbers are **not inconsistent**: a horizon-competition switch marking the onset, with a simple-μ-like interpolation, is compatible with the observed `a₀`.

**But this cannot be used as support.** The range spans an order of magnitude and would accommodate almost any mechanism; the `μ` family is empirically fitted (Cassini-constrained), not derived; and identifying the switch with “10% departure” rather than with the asymptote-crossing is a choice made after seeing the number. **Recorded as not-refuted, not as evidence.**

### What the check settles

The factor 5.67 is a **genuine open residual** — not a units artifact, not absorbable by interpolation. And it is the *same* residual as Target #18's: every route in the corpus reduces to comparing the chain's acceleration scale against `cH₀`, and the measured scale is `cH₀/(2π)`.

**One unexplained factor sits at the horizon-to-chain join, and it is identical in every derivation.** That is a cleaner statement of the problem than the corpus had, and it is the honest headline: **ED derives the *scale* of MOND's threshold three independent ways, and the *coefficient* none.**

---

## 5b. Attempt to derive μ from the substrate — blocked, and the block is the result

Attempted 2026-09-04, immediately after §5, since deriving `μ` was named there as what would convert the weak form into a sharp test.

### ED already has a candidate, and it is written down

`Paper_030` §6.3, titled *"The 'no interpolation function' claim"*, gives the transition profile explicitly:

$$a(R) = a_N + a_0 + \frac{\sqrt{GMa_0}}{R} \;=\; a_N + a_0 + \sqrt{a_N a_0}.$$

> **Superseded 2026-09-04 — the standalone `a₀` above is gone.** `Paper_030` §3.2 was rewritten the same day: `Σ₀` is now a **content normalization** feeding §4.2 and no gradient of it is taken, so the profile is **`a = a_N + √(a_N a₀)`**. Both limits follow as limits, no regime switch is assumed, and §7.1's deep-MOND branch is correct. *The `x^{-1/2}` saturation and therefore the Cassini exclusion outside the deep field are unchanged — the removed term was not what caused them.* See `Note_TheSwitchIsDerived_TheShapeIsInherited.md` §11 and `Gravity_TieredClaims_Ledger.md` Staleness #37.

Writing `s = √(a_N/a₀)` this is a closed-form interpolation law:

$$\frac{a}{a_0} = s^2 + s + 1, \qquad \mu \equiv \frac{a_N}{a} = \frac{s^2}{s^2+s+1}.$$

So ED does have a derived `μ`. Its saturation exponent is the problem.

### It saturates as `x^{-1/2}`, and that is fatal at high acceleration

`1 - μ ≈ 1/s = √(a₀/a_N)` for `s ≫ 1`. Against the standard families:

| interpolation | approach to Newtonian |
|---|---|
| **ED §6.3 profile** | **`1-μ ~ x^{-1/2}`** |
| simple, `x/(1+x)` | `1-μ ~ x^{-1}` |
| standard, `x/√(1+x²)` | `1-μ ~ x^{-2}/2` |

The `√(a_N a₀)` cross-term is a `1/R` force of magnitude `√(GMa₀)`, which is **not** degenerate with a rescaling of `GM_☉` (that would be `1/R²`). Computed against solar-system accelerations:

| body | `a_N` (m/s²) | fractional deviation | anomalous `a` (m/s²) |
|---|---|---|---|
| Earth | 5.93×10⁻³ | 1.42×10⁻⁴ | 8.4×10⁻⁷ |
| Jupiter | 2.19×10⁻⁴ | 7.40×10⁻⁴ | 1.6×10⁻⁷ |
| **Saturn** | 6.52×10⁻⁵ | **1.36×10⁻³** | **8.9×10⁻⁸** |
| Uranus | 1.61×10⁻⁵ | 2.74×10⁻³ | 4.4×10⁻⁸ |

Cassini-class ranging bounds anomalous accelerations at Saturn near `10⁻¹⁴ m/s²`. **The profile exceeds that by roughly seven orders of magnitude.** `Paper_KM-I`'s own preamble item 5 already states the criterion — the interpolation is *"a Cassini-constrained family (**slow-saturating members excluded by ephemerides**)"* — and `x^{-1/2}` is the definition of slow-saturating. **KM-I's stated constraint excludes `Paper_030` §6.3's profile, and neither paper notices.**

### But ED does not actually run that profile — and that is where the real finding is

`Paper_030` §7.1 switches the mechanism off:

> **Newtonian regime (`a_N ≫ a₀`):** `a ≈ a_N`. **P14 inactive (joint weak-gradient regime does not apply).**

So the cross-term does not exist in the regime where Cassini applies, and ED is not refuted. But the escape has a price, and it contradicts the claim two subsections later:

- **§7.2 says the crossover is "smooth and parameter-free."** It is not smooth. It is three branches with **P14 toggled on and off at the boundaries**, and the toggle is the regime assumption — the same one restored under Staleness #13.
- **§6.3's "no interpolation function" claim does not hold.** What ED has is a piecewise profile with an assumed switch. That is what an interpolation function is, minus the smoothness and minus the fit.

**The two are exclusive.** Make the profile genuinely smooth (P14 active everywhere) and Cassini kills it by seven orders. Keep the switch and the transition is assumed rather than derived. **μ cannot be derived from the substrate as things stand, and the obstruction is a live observational constraint, not a bookkeeping gap.**

### What this does to §3's mechanism — the convergence

The horizon-competition mechanism of §3 **is a switch**. And it switches in exactly the direction §7.1 assumes:

- **`a > cH₀`** — the chain's own Rindler horizon lies inside the cosmic one, so cosmic content is cut off before it arrives. The local–horizon bilocal coupling has nothing to couple to. **P14 inactive.**
- **`a < cH₀`** — the cosmic horizon binds, cosmic content reaches the chain. **P14 active.**

That is `Paper_030` §7.1's regime structure, **derived rather than postulated**. The mechanism supplies precisely the missing piece: a physical reason for the bilocal term to be absent at high acceleration, which is what Cassini demands and what §7.1 currently asserts.

**Two problems remain, and they are the same two as before.** The switch sits at `cH₀`, not at the fitted `a₀` — the factor 5.67 of §5. And a switch is sharp, while rotation curves show a gradual transition; the smooth rounding still has to come from somewhere, and §5's check shows it cannot come from a `μ` that leaves the cross-term active into the solar system.

**Net.** The attempt to derive `μ` fails, and fails informatively. It converts "ED has no derived interpolation function" from an accounting remark into a physical statement: **ED's transition is a switch, not a smooth function, and the switch is the thing to derive.** §3 derives it, modulo the location.

---

## 6. What this owes

**The switch is asserted, not derived. — DISCHARGED 2026-09-04 (same day), see `Note_TheSwitchIsDerived_TheShapeIsInherited.md`.** "Only the nearer boundary binds" was stated here rather than shown from the V5 kernel. It has since been shown, and the construction was already in the corpus: `Paper_039` §3.1 defines `Γ_cross` as a **single integral over one kernel** `K_V5`, and `Paper_090` §4.4 makes that kernel a function of a **single argument**, Lorentz-invariant separation. The two horizons are therefore not two attenuations that must be argued to compose — by `Paper_047_5` they are one object on two axes, and so they are two ways for **one** argument to run away. A bounded decaying function of one variable is driven to zero by whichever runs away first. **Cutoff at `min(R_a, R_H)`, no new postulate, and shape-independent.** F1 answered in the affirmative. *What the follow-up note takes back in exchange is the discreteness — see the correction in §3.*

**The regimes are asserted to map onto Newtonian and deep-MOND.** That the binding-boundary switch coincides with the dynamical regime change is the natural reading, and it is not demonstrated.

**It does not by itself produce `√(a_N a₀)`.** The threshold mechanism says *where* the regimes divide. `Paper_QuadraticStrain_v1` §5's interference cross-term says what the deep-MOND law *is*, and that half is unaffected and remains the strong half of that paper. The two would need joining.

**Interaction with Staleness #13.** If this mechanism is right, `Paper_030` §5.3's regime assumption — restored on 2026-09-04 when the QuadraticStrain §6 branch was resolved — becomes **derivable rather than postulated**, since "the cross-term dominates in deep-MOND" is exactly "the cosmic boundary is the binding one below `cH₀`." That would restore the second discharge QuadraticStrain claimed, by a valid route rather than the invalid one. **Not claimed here; flagged as the pay-off if §6's asserted switch can be shown.**

---

## 7. Falsification criteria

- **F1 — FIRED AND PASSED 2026-09-04**, in `Note_TheSwitchIsDerived_TheShapeIsInherited.md` §3. The construction (`Paper_039` §3.1 + `Paper_090` §4.4) collapses `Γ_cross` at the **nearer** boundary, shape-independently. *Partial concession:* the second disjunct ("or at neither distinctly") is not fully cleared — a sufficiently broad V5 envelope gives a gradual crossover rather than a distinct switch, and the envelope shape is inherited (`Paper_090` §7.2). The **scale** survives either way; the **discreteness** does not, and §3 now records that withdrawal.
- **F2 — partially fired 2026-09-04.** The check confirms the fitted `a₀` *is* the asymptote-crossing for every `μ`, so 5.67 cannot be absorbed by interpolation and is a genuine residual. Not yet a refutation: the mechanism's switch may mark the onset rather than the crossing (§5, weak form), but that escape is untestable while `μ` is fitted rather than derived. **Deriving `μ` from the substrate would convert this into a sharp test.**
- **F4 — new, and sharp.** If the bilocal cross-term is shown to be **active** at solar-system accelerations, the `√(a_N a₀)` term predicts `≈8.9×10⁻⁸ m/s²` of anomalous acceleration at Saturn against a `≈10⁻¹⁴` bound, and `Paper_030`'s account is **refuted outright** (§5b). Everything therefore rests on the switch of §3 being real.
- **F3:** If `Paper_047_5`'s identification of Rindler and cosmological horizons as one substrate object fails (its own F2: substrate evidence that V5 saturation does not occur at one of the four types), this mechanism has no ingredient and collapses.

---

*End of note.*
