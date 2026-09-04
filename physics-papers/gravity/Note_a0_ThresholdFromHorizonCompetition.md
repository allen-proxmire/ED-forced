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

**This is a threshold of the right structural kind.** Nothing is nonlinear in `|a|`; the linear response of `Paper_029` is untouched and describes behaviour *within* a regime. What changes at the threshold is *which boundary is saturating*, and that changes discontinuously. **A linear response plus a switch in which horizon binds gives a threshold.** That is the answer Target #19 was asking for, and it required no new postulate.

---

## 4. What this does to Target #18

The mechanism gives `a₀ = cH₀`. **Bare. No `2π`.**

Target #18's Route 2, built from a completely different starting point — Rindler smoothness and the de Sitter temperature — found that the *symmetric* matching condition `T_a = T_H` also gives `a₀ = cH₀`, and that only an asymmetric, unmotivated condition produces the `2π`.

**Two independent ED mechanisms now converge on `a₀ ~ cH₀`, and neither produces the `2π`.** That cuts two ways, and both matter:

- **It strengthens the horizon-tying claim considerably.** The physically substantive content of ED's MOND account — that `a₀` is set by the cosmic horizon — now has two independent derivations rather than one, from a threshold argument and from a thermal argument that share no machinery.
- **It isolates the `2π` and makes it look inherited.** The factor is not produced by the threshold mechanism, not produced by the symmetric thermal condition, and provably cancels in the azimuthal-Fourier derivation that currently claims it (Staleness #10). Three routes to the scale; none to the coefficient.

The honest reading is that **`a₀ ~ cH₀` is form-derived and the coefficient is inherited**, unless Target #18's asymmetric matching condition can be grounded.

---

## 5. The numerical gap, unresolved

`cH₀ ≈ 6.8 × 10⁻¹⁰ m/s²`. The fitted MOND `a₀ ≈ 1.2 × 10⁻¹⁰ m/s²`. The mechanism's crossover sits a factor of **~5.7** above the fitted value — which is `2π` to within 10%, the same gap Staleness #10 concerns.

Two readings, and this note does not choose between them:

1. **The factor is real and unexplained.** The threshold is genuinely at `cH₀` and something suppresses the effective onset by `2π`. This is Target #18's problem restated.
2. **The comparison is category-mismatched.** A fitted `a₀` in a standard interpolation function `μ(x)` is not the same object as the crossover point of an underlying mechanism. `μ` spreads the transition over roughly a decade, and where the fitted parameter lands relative to the mechanism's switch depends on the interpolation family — which the corpus takes as empirically constrained (Cassini), not derived. **This has not been worked out and should be before the factor of 5.7 is treated as a discrepancy.**

Reading 2 is the cheaper check and nobody has run it. It is a calculation, not a derivation.

---

## 6. What this owes

**The switch is asserted, not derived.** "Only the nearer boundary binds" is physically natural and matches `Paper_028`'s own crossover logic, but it is stated here rather than shown from the V5 kernel. What would show it: `Γ_cross` collapsing at the nearer boundary in a construction carrying both, so the switch is exhibited rather than assumed.

**The regimes are asserted to map onto Newtonian and deep-MOND.** That the binding-boundary switch coincides with the dynamical regime change is the natural reading, and it is not demonstrated.

**It does not by itself produce `√(a_N a₀)`.** The threshold mechanism says *where* the regimes divide. `Paper_QuadraticStrain_v1` §5's interference cross-term says what the deep-MOND law *is*, and that half is unaffected and remains the strong half of that paper. The two would need joining.

**Interaction with Staleness #13.** If this mechanism is right, `Paper_030` §5.3's regime assumption — restored on 2026-09-04 when the QuadraticStrain §6 branch was resolved — becomes **derivable rather than postulated**, since "the cross-term dominates in deep-MOND" is exactly "the cosmic boundary is the binding one below `cH₀`." That would restore the second discharge QuadraticStrain claimed, by a valid route rather than the invalid one. **Not claimed here; flagged as the pay-off if §6's asserted switch can be shown.**

---

## 7. Falsification criteria

- **F1:** If a construction carrying both boundaries shows `Γ_cross` collapsing at the *farther* boundary, or at neither distinctly, the switch is not a switch and the mechanism fails.
- **F2:** If the interpolation-function check of §5 reading 2 shows the fitted `a₀` should coincide with the mechanism's crossover, then the factor of 5.7 is a genuine refutation of this mechanism, not a coefficient problem.
- **F3:** If `Paper_047_5`'s identification of Rindler and cosmological horizons as one substrate object fails (its own F2: substrate evidence that V5 saturation does not occur at one of the four types), this mechanism has no ingredient and collapses.

---

*End of note.*
