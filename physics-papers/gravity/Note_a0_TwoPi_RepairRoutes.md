# The `1/(2π)` in `a₀`: One Route Closed, a Better One Opened

**Allen Proxmire**

**September 2026**

**Series:** Event Density (ED) Generative Papers — gravity arc, working note
**Status:** Research note on Research Target #18. **Does not close the target.** Closes the repair route previously named for it, identifies a materially better one, and states precisely what that route still owes. No tier changes; `a₀`'s `1/(2π)` remains **Postulated / disputed** per `Gravity_TieredClaims_Ledger.md` Staleness #10.
**Anchors:** `Paper_028` §6 · `Paper_029` §5.1 · `Paper_BH_Thermal2Pi_EntropyCoefficient` (the corpus's one physically-derived `2π`) · Staleness #10, #13
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: what this note does NOT claim

1. **It does not derive `a₀ = cH₀/(2π)`.** The `1/(2π)` remains undischarged.
2. **It does not restore "parameter-free."** That claim stays suspended.
3. **It does not claim the new route works.** It claims the route is *available*, *physically grounded in a `2π` ED already derives elsewhere*, and *reproduces the number exactly* — and then names the one thing it lacks.
4. **Nothing here touches `a₀ ~ cH₀` or `a₀(z) = cH(z)/(2π)`.** Both were always unaffected; the evolution and its forced exponent of 1 follow from horizon-tying, not from the `2π`.

---

## 1. The route the ledger named is closed

Staleness #10 recorded a candidate repair: *if the chain couples to the dipole **mode amplitude** rather than the integrated mode — per unit azimuthal angle rather than the total around the circle — the `1/(2π)` is physical rather than conventional.*

**It does not work, and the reason is a primitive.** The `∫dφ` in `Paper_028` §6.3 is a coarse-grained stand-in for a sum over the chain's azimuthal **channels**, which are discrete (P07: a channel is a single structurally distinguishable carrier). P04 makes bandwidth additive **across distinct channels**. So the substrate-level object is `Σ_K`, a sum — not a per-radian density, and not an average.

To convert that sum into something carrying `1/(2π)` you need a channel count. Writing the azimuthal channels at angular density `N_az/(2π)` per radian gives `Σ_K → (N_az/2π)∫dφ`, so a per-channel response carries `1/N_az`, not `1/(2π)`. **A bare `1/(2π)` with no `N_az` requires the response to be a density in angle, and P04's additivity says it is not.** The mode-amplitude route asks the primitives for the opposite of what they say.

*Recorded as a negative: the route named in Staleness #10 should not be attempted further on these grounds.*

---

## 2. ED already owns a `2π` that is not a convention

`Paper_BH_Thermal2Pi_EntropyCoefficient` derives the `2π` in `T = κ/(2π)` from ED's own near-horizon geometry: the near-horizon `b`-profile is Rindler, Euclidean continuation makes `κτ` an angle, and **smoothness at the horizon point — no conical defect — requires that angle to run a full `2π`**.

That is a genuinely physical `2π`. It is a *smoothness condition on a horizon*, not a normalization of a measure. Nothing cancels it, and choosing different bookkeeping does not move it.

Its honest tier matters and is inherited by anything built on it. §4b of that paper records that the `2π` is a **continuum / smooth-horizon quantity**: an attempt at a continuation-free version failed, and the deeper finding was that even a correct real-time derivation gets the `2π` from the gamma function `Γ(iω/κ)`, which *is* the horizon's analytic structure in another guise. The paper's reframe: the `2π` may not live below the continuum at all, and demanding it from raw commitment counting may be a category error.

---

## 3. The better route, stated exactly

**An accelerating chain has a Rindler horizon.** The same smoothness argument that gives the black-hole `2π` applies to it, because it is the same near-horizon geometry. And the cosmic decoupling surface at `R_H = c/H₀` is a de Sitter-type horizon with surface gravity `κ_H = H₀`, hence temperature

$$T_H = \frac{\kappa_H}{2\pi} = \frac{H_0}{2\pi}.$$

A chain accelerating at `a` has Rindler surface gravity

$$\kappa_a = \frac{a}{c}.$$

Setting the chain's surface gravity equal to the horizon's temperature,

$$\kappa_a = T_H \quad\Longrightarrow\quad \frac{a}{c} = \frac{H_0}{2\pi} \quad\Longrightarrow\quad \boxed{a_0 = \frac{cH_0}{2\pi}}$$

exactly, with the `2π` supplied by the **de Sitter horizon's own smoothness condition** — the same `2π` ED derives in the black-hole sector, not an azimuthal Fourier measure.

**Two things this buys, if it can be grounded.**

*The number is reproduced with a `2π` that cannot cancel.* Unlike the current derivation, there is no step at which the factor multiplies against its own inverse.

*It becomes one fact appearing twice.* The `2π` in `a₀` would be the **same** `2π` as in `T = κ/(2π)`, exactly as `c_T = c` and `α₂ = 0` are one causal-cone fact seen twice (GR-IV §3). That is the untunability structure the corpus already leans on, and it would extend to the MOND scale — which is currently the arc's most ED-distinctive and least defended number.

---

## 4. What the route owes, stated without softening

**The matching condition is not motivated.** `κ_a = T_H` equates a surface gravity with a temperature. In natural units both carry dimensions of inverse time, so it is dimensionally clean, but it is asymmetric: there is no argument here for why the chain's *surface gravity* rather than its *temperature* is the quantity that matches the horizon.

**And the symmetric condition gives the wrong answer.** The natural criterion — chain temperature equals horizon temperature, `T_a = T_H` — has the `2π` cancel on both sides and yields `a = cH₀ ≈ 6.8 × 10⁻¹⁰ m/s²`, against a measured `1.2 × 10⁻¹⁰`. Wrong by the factor at issue. So the criterion that works is the asymmetric one, and **a route whose only justification is that it lands the number is numerology.** This must be argued from the substrate or abandoned.

The shape such an argument would need: a reason why an accelerating chain responds to the cosmic horizon through its own *Rindler structure* (a `κ`) while the horizon presents itself as a *thermal state* (a `T`). Candidate hooks, none developed here: the horizon is a V5 saturation surface and therefore a statistical object, while the chain's acceleration is a P11 commitment-rate asymmetry and therefore a rate — which would make the asymmetry substrate-native rather than chosen. **Speculative. Not attempted here.**

**Ceiling on the tier.** Even if grounded, this route inherits `Paper_BH_Thermal2Pi`'s limitation: the `2π` is a continuum, smooth-horizon quantity reached through Euclidean smoothness, not from raw commitment counting. `a₀`'s `2π` could at best reach *structural given the coarse-grained horizon* — the same tier as the Hawking `2π`. It would not become substrate-native, and this note does not claim it could.

**A standing awkwardness worth naming.** Euclidean continuation is a reversible-time move, and ED's whole thesis is that the arrow is primitive and reversibility is a coarse-graining artifact. A P11-native framework leaning on Wick rotation is not a contradiction — the corpus is explicit that reversibility is what the continuum *has* — but it is a place where ED uses a tool its own ontology says is derived. `Paper_BH_Thermal2Pi` §4b reaches the same edge from the other side.

---

## 4b. The V5-state / P11-rate argument, attempted

Attempted 2026-09-04, immediately after §4. **It does not close, and it gets further than expected.** Recorded in full because the shape of the remaining gap is the useful part.

### The horizon side is solid, and it was already on the books

`Paper_028` §3.4 is titled *"Statistical, not geometric, substrate-level boundary"*, and §7 restates it: the cosmic decoupling surface is **"substrate-graph statistical, not geometric"** — a property of adjacency-and-bandwidth *structure*, coinciding numerically with the Hubble radius only under coarse-graining. It is where the V5 cross-chain correlation budget saturates, not a locus where the `b`-field does something.

That has a consequence nobody drew before: **there is no `b`-gradient to read off the cosmic surface.** A `κ` is a gradient of `b` at a horizon — that is exactly how `Paper_BH_Thermal2Pi` and GR-III obtain `κ = ½b′(r_s) = 1/(2r_s)`. A statistical boundary has no such gradient. So the cosmic surface **cannot** contribute a `κ`; the only characterisation available to it is a state, and its state carries the smoothness `2π` as `T_H = κ_H/(2π) = H₀/(2π)`.

This half is not chosen to fit. It follows from a scoping statement `Paper_028` made in 2026-05 for unrelated reasons.

### The chain side is a layer argument, and it is the interesting part

A chain's acceleration is, in ED, a **P11 commitment-rate asymmetry**: the commitment front advances differently forward and backward along the acceleration axis. That is a bare count-rate at the level of commitments — sub-continuum, layer 1 in the two-layer picture (`Paper_Continuum_KineticLatticeGas`; `MetricFromTheGraph` P4).

`T_H`, by contrast, is a **layer-2 object**. `Paper_BH_Thermal2Pi` §4b establishes exactly this and treats it as the paper's deepest finding: the `2π` is a continuum, smooth-horizon quantity, reachable through the horizon's analytic/periodic structure and *not* from raw commitment counting. Asking for it below the continuum may be a category error.

So the two quantities being compared sit on opposite sides of the coarse-graining seam, and **the `2π` is precisely the layer-crossing factor** — what appears when a bare periodic structure is read as a thermal state. Working in natural units (`ħ = c = k_B = 1`), where acceleration and temperature are both inverse times:

| Comparison | Layers | Result |
|---|---|---|
| `T_a = T_H` | 2 ↔ 2 | `a/2π = H₀/2π` ⟹ `a = cH₀`. **The `2π` cancels because the same conversion is applied twice.** Wrong by 5.7× |
| `a = T_H` | 1 ↔ 2 | `a = H₀/2π` ⟹ **`a₀ = cH₀/(2π)`**. The seam is crossed exactly once, so one factor survives |

The criterion is then not an arbitrary pairing of a surface gravity with a temperature. It is: **the chain's own commitment-rate asymmetry, measured in the chain's own units, against the thermal rate of the state it sits in.** Below that threshold the horizon's fluctuation rate exceeds the chain's own asymmetry and the chain's dynamics are horizon-dominated — the deep-MOND regime. Above it the chain's own rate dominates — Newtonian. That is a physically meaningful transition, and it is where MOND's transition actually is.

### What it still owes, and it is one specific thing

**Why is the comparison made at the chain's layer rather than at a common layer?** If both quantities are brought to layer 2, the chain's rate becomes `T_a = a/2π`, the `2π` cancels, and the prediction is `cH₀` — refuted. So the argument requires the comparison to happen at layer 1, and the justification offered here is that *the chain is what responds, so the response is executed in the chain's own machinery, at the chain's own layer*, while the horizon can only present itself coarse-grained because it is statistical by construction.

That is a reasonable sentence. **It is not yet a derivation, and it is carrying the entire `2π`.** Anyone who prefers the symmetric comparison gets `cH₀` and this route dies.

### Honest status

The horizon half is grounded in a prior, independent scoping statement. The chain half is an argument sketch with a named ED-native structure — the layer-1/layer-2 seam — rather than the bare assertion §4 started with. That is real movement: the `2π` has gone from *a measure convention that provably cancels*, to *the coarse-graining seam crossed exactly once*. It has not become derived.

**Two things that would settle it.** A construction showing that a chain's response to coarse-grained content is executed at layer 1 in general — which would be a result well beyond `a₀` and worth having on its own. Or a demonstration that the response must be evaluated at a common layer, which kills the route outright and lands `a₀`'s coefficient at **inherited**, permanently.

**One check worth running.** If the `2π` is genuinely a layer-crossing factor, then every ED quantity comparing a bare chain rate to a horizon thermal state should carry exactly one, and quantities comparing like layers should carry none. That is a testable pattern across the corpus, and it has not been checked.

**Do not bank this.** One criterion, one number, and a sentence doing the load-bearing work.

---

## 4c. The corpus-wide check, run

§4b predicted a testable pattern: if the `2π` is a coarse-graining seam crossed once, then every ED result comparing a bare rate to a horizon thermal state should carry exactly one `2π`, like-layer comparisons should carry none, and geometric `π` should be separable by origin. Census run 2026-09-04 over all of `physics-papers/`: **322 π-carrying result lines across 91 papers**, sorted by π-signature and classified.

### The result

**No counterexamples. Too few independent instances to call it confirmed.**

| Class | Instances | Predicted | Found |
|---|---|---|---|
| Rate ↔ thermal state (layer crossing) | `T = κ/(2π)` (`Paper_BH_Thermal2Pi`) · `a₀ = cH₀/(2π)` (the case under test) | one `2π` | one `2π` ✓ |
| State ↔ state (like layer) | `𝒲₀` against the raw background scale `(cH₀)²` | none | **none** ✓ |
| Geometric (solid angle, sphere area) | `N(R) = 4πR²/ℓ_ED²`; Einstein's `8πG`; `ρ_crit = 3H₀²/(8πG)` | separable, different origin | `4π`/`8π`, never `2π` ✓ |
| Inherited textbook | inflationary `P_T = (2/π²)(H²/M_P²)` | excluded, not ED-derived | excluded |

### The one informative case

`Paper_KM-II` §7.1 gives `𝒲₀ = −24π²Ω_Λ ≈ −1.6×10²`, the only `π²` in the corpus. It is not a second, independent layer crossing. The paper says so itself, and said so before this question was asked:

> equivalently **`6Ω_Λ ≈ 4.1` against the raw background scale `(cH₀)²`, genuinely order-unity** (the apparent largeness is the `(2π)²` of `a₀`'s definition, not a hierarchy)

`𝒲₀` is quadratic in `a₀`, so it carries `a₀`'s single `2π` squared. Expressed against `(cH₀)²` instead — a like-layer comparison — **the π vanishes entirely and the coefficient is order unity.** That is precisely the behaviour §4b predicts: the π tracks `a₀`, appears once per factor of `a₀`, and disappears when the comparison is made at a common layer.

### Why this is not confirmation

The census has **two** crossing instances and **one** like-layer instance, and they are not independent of each other. `a₀`'s `2π` is the case under investigation. `𝒲₀`'s `π²` is `a₀`'s `2π` transported, not a fresh measurement. That leaves `T = κ/(2π)` as the single genuinely independent instance — and it is the one the route *borrows* the `2π` from in the first place.

So the honest statement is: **the corpus's π-factors separate cleanly into geometric and thermal, with no case where a thermal comparison is missing its `2π` or a geometric one has acquired a spurious one.** That is a consistency finding. It is not a rule with independent support, because ED does not currently contain enough distinct rate-versus-state comparisons to constitute a test.

### The three candidates, checked

Checked 2026-09-04. **No third independent crossing exists. The pattern cannot currently be tested.**

- **`Paper_047_5_HorizonUniversalization`** — rules itself out in its own preamble, item 4: *"It does **not** claim derivation of the Hawking-Unruh temperature formula `T = κ/(2π)` — that result is INHERITED from standard semi-classical GR."* It uses the relation across four horizon classes; it does not produce it. Not an instance.
- **`Paper_039_HorizonDecoupling` §4.1** — the closest thing, and still not independent. It states that near the decoupling surface V5 acquires imaginary-time periodicity with `β_H = 2π/κ`, then reads `T_H = 1/β_H = κ/(2π)` off it. **The `2π` is asserted as the periodicity, not derived**; the paper's contribution is identifying that the *V5 kernel* is what acquires the periodicity, which is a substrate-side identification of the carrier, not a derivation of the factor. It is the same Euclidean-periodicity fact `Paper_BH_Thermal2Pi` later derives from no-conical-defect smoothness — one fact, two papers, one derivation.
- **`Paper_040_TransPlanckian`** — contains a genuine crossing, `T_H/ω_c`, comparing a thermal temperature to the bare V5 cutoff rate `ω_c = c/ℓ_P`. But it appears only as an order-of-magnitude suppression, `O(T_H/ω_c)² ~ (ℓ_P/M)²`, with all O(1) factors dropped. **Untestable either way**, and not a counterexample.

**That last case is the real limit on this method.** Most ratio statements in the corpus are order-of-magnitude, and a hypothesis about a factor of `2π` cannot be tested against expressions written to within factors of `2π`. The census's 322 lines shrink, once order-of-magnitude statements and inherited textbook results are removed, to a handful of coefficient-tracked results — and those are the two entangled cases already counted.

**Verdict: the check is closed, negative on availability rather than on substance.** The corpus contains no rate-versus-state comparison, derived independently of `a₀` and of the Hawking relation, with its coefficient tracked. The layer-crossing reading of the `2π` therefore remains a suggestive regularity with no independent support, and §4b's route stands exactly where §4b left it.

### A small currency item found in passing

`Paper_039` §4.1 (2026-05-13) **assumes** `β_H = 2π/κ`. `Paper_BH_Thermal2Pi_EntropyCoefficient` later **derives** it from ED's own near-horizon geometry. Paper_039 does not point at that derivation, so a reader arriving at §4.1 sees an assumption where the corpus now has a result. One forward-pointer sentence. *(Recorded here rather than fixed, since it belongs to the black-hole arc's ledger, not this note's scope.)*

### What would make it a test

A third, independent layer crossing — an ED result comparing a bare commitment rate to a coarse-grained thermal state, derived without reference to `a₀` or to `T = κ/(2π)`. Candidates worth examining, none checked here: the Unruh-like content in `Paper_040_TransPlanckian` and `Paper_047_5_HorizonUniversalization`, and the V5 saturation treatment in `Paper_039_HorizonDecoupling`. If any of those produces a `2π` on a crossing and none appears on a like-layer comparison in the same paper, the pattern acquires real support. Until then it remains a suggestive regularity over two entangled cases.

---

## 4d. Convergence from target #19 — the `2π` is now isolated

Added 2026-09-04. Target #19's threshold work (`Note_a0_ThresholdFromHorizonCompetition.md`) reaches `a₀` from machinery this note shares nothing with: a chain has two V5-saturation boundaries, its own at `R_a = c²/a` and the cosmic one at `R_H = c/H₀`, they are the same substrate object by `Paper_047_5` (M3), only the nearer binds, and the switch sits at `c²/a = c/H₀`.

**It gives `a₀ = cH₀`. Bare, no `2π`.**

So the tally across every route the corpus now has:

| Route | Gives the scale | Gives the `2π` |
|---|---|---|
| Azimuthal-Fourier normalization (`Paper_028` §6, `Paper_029` §5.1) | — | **no** — it provably cancels (Staleness #10) |
| Thermal matching, symmetric `T_a = T_H` (§3–4 above) | `cH₀` ✓ | no |
| Thermal matching, asymmetric `κ_a = T_H` (§3–4b above) | `cH₀/(2π)` ✓ | only via an ungrounded condition |
| Horizon competition (target #19) | `cH₀` ✓ | no |

**Three routes to the scale; none to the coefficient.** That is the honest state, and it points both ways. The substantive claim — `a₀` is set by the cosmic horizon — is now *better* supported than when this note opened, with two independent derivations instead of one. The coefficient is *worse* supported: it is not produced by any mechanism that stands on its own, and the only route that yields it is the one carrying an unproven claim about which layer the comparison runs at.

**The honest landing, absent a resolution of §4b:** `a₀ ~ cH₀` is form-derived, and the `2π` is **inherited**.

---

## 4e. The content-depth framing, and one candidate eliminated

*Added 2026-09-04, after `Paper_030` §3.2 was rewritten (Staleness #37). Modest: it eliminates one candidate and relocates the question. It does not derive the `2π`.*

### What the rewrite changed

Until 2026-09-04, `Σ₀ = -a₀R` was treated as a potential whose gradient was a force, and `a₀R_H` had no distinguished status. `Σ₀` is now a **content normalization**, so `a₀R_H` is a displayed physical quantity — **the cosmic horizon's content depth** — and the current claim reads

$$a_0 R_H = \frac{c^2}{2\pi}.$$

That makes the `2π` a statement about a specific number the corpus can approach independently: **is a horizon's content depth `c²`, `c²/2`, or `c²/(2π)`?** Writing the depth as `c²/k` gives `a₀ = cH₀/k` directly.

### The three structural candidates, and what each predicts

| `k` | Reading | `a₀` at `H₀ = 70` | vs measured `1.2×10⁻¹⁰` |
|---|---|---|---|
| **1** | depth `= c²` — bare escape scale | `6.80×10⁻¹⁰` | **5.7× too large** |
| **2** | depth `= c²/2` — **geometric**, by analogy with the corpus's own black-hole horizon depth `Σ_N(R_s) = -GM/R_s = -c²/2` | `3.40×10⁻¹⁰` | **2.8× too large** |
| **2π** | depth `= c²/(2π)` — **thermal**, the current claim | `1.08×10⁻¹⁰` | 9.8% too small |

### The result: the geometric candidate is eliminated, and it was the only natural non-thermal one

**`k = 2` is new here** — it is not among the readings this note or `Paper_029` had enumerated, and it is the obvious competitor, since it is what the corpus's *own* machinery gives for a horizon: at a Schwarzschild radius `Σ_N(R_s) = -c²/2` exactly, and de Sitter's `1 - H²r²` gives the same depth at `R_H`. **It fails by a factor of 2.8**, far outside any error budget on `a₀` or `H₀`. So the cosmic horizon's content depth is **not** the geometric depth of a horizon of that radius.

That is a genuine elimination and it cuts in a useful direction: **among the natural structural candidates, only the thermal reading survives**, which is the reading Route 2 (§3) needs. *(Caveat, stated because it matters: the `k = 2` analogy is not forced. `Σ_N` is content sourced by mass **inside** a radius and `Σ₀` is content presented by a boundary **outside** the chain; requiring equal depths is natural, not derived. What is eliminated is the natural reading, not a theorem.)*

### And the framing converges on the same locus as Route 2

Asking whether the depth is geometric or thermal **is** asking whether the horizon presents itself as a `κ` or as a `T` — which is exactly the asymmetry §4 says `κ_a = T_H` needs and §4b tried to ground in the layer seam. Reached from an unrelated direction (a content normalization in `Paper_030` §3.2), it lands on the same question.

**Three framings, one locus.** §4d already recorded that every route reduces to comparing a chain's acceleration scale against `cH₀`; this adds that the *coefficient* question is likewise single-valued. That is consistency, **not** independent support — the same fact seen a third time is still one fact.

### What is NOT new here, recorded so it is not double-counted

The `2π`-required range for `a₀` is **already in the corpus**. `Paper_029` §5.4 states it: `H₀ ∈ [67,74]` gives a substrate range `≈[1.03, 1.14]×10⁻¹⁰` against an empirical `1.2×10⁻¹⁰`, with the *"~10% gap … consistent with the joint `H₀` + MOND-`a₀` uncertainty."* An independent recomputation here reproduces it (`[1.042, 1.144]×10⁻¹⁰` over the same range). **This was checked before writing and is not claimed as a new prediction.**

**One wording observation on §5.4, recorded not fixed.** *"Consistent with the joint uncertainty"* is defensible but soft: the offset is **one-sided** — the `2π` prediction sits below the canonical `a₀` at every `H₀` in the range, and closing it exactly needs either `a₀ ≈ 1.08×10⁻¹⁰` or `H₀ ≈ 77.6`, the latter above even the local-ladder value. A one-sided systematic offset is a weaker form of agreement than "consistent" suggests. **CHECK RUN, same day — see `Paper_029` §5.5 and Staleness #39.** The 2016 figure (`±0.24` sys) gave 0.49σ; the current determination, **Desmond 2023** (`a₀ = 1.19 ± 0.04 ± 0.09`), gives **1.09σ** at `H₀ = 70`. The systematic tightened 2.7× and §5.4's *“consistent”* is stale. **And the offset is directional:** 1.50σ against Planck's `H₀`, 0.62σ against SH0ES — so `a₀ = cH₀/(2π)` **prefers the local distance-ladder `H₀`**. Not a prediction of `H₀` (ED inherits it) but a consistency constraint between two measured quantities, and the sharpest empirical handle the `2π` has.

### Status

**No change to the `2π`'s tier.** It remains Postulated/disputed (Staleness #10). One competitor removed, the question relocated to a displayed quantity, and one currency check named.

---

## 5. Status and what to do next

| Item | State |
|---|---|
| Mode-amplitude route (Staleness #10's named candidate) | **CLOSED — negative.** P04 additivity is across channels; the sum is not a density (§1) |
| Rindler / de Sitter smoothness route | **OPEN — better.** Reproduces the number with a non-cancelling `2π` already derived in the corpus (§3) |
| The `κ_a = T_H` matching condition | **Advanced 2026-09-04, still the debt.** The horizon half is grounded (`Paper_028` §3.4: statistical, not geometric ⟹ no `b`-gradient ⟹ no `κ` available, only a state). The chain half is now a **layer argument** — the `2π` is the layer-1/layer-2 seam crossed exactly once — rather than a bare assertion. Not derived. See §4b |
| Content-depth framing; geometric candidate `k = 2` | **NEW 2026-09-04 (§4e). ELIMINATED.** After the `Σ₀` rewrite (#37) `a₀R_H = c²/(2π)` is the horizon's content depth, so the `2π` is a claim about a computable number. The natural geometric candidate — depth `= c²/2`, the corpus's own BH horizon depth — predicts `a₀ = 3.4×10⁻¹⁰`, **2.8× too large**, and is excluded. Only the thermal reading survives among natural candidates, and the framing lands on §4's `κ`-vs-`T` question from an unrelated direction |
| The layer-crossing pattern (§4b prediction) | **CHECKED 2026-09-04 (§4c).** Census of 322 π-carrying lines across 91 papers: **no counterexamples**, and the corpus's π separates cleanly into geometric (`4π`, `8π`) and thermal (`2π`). But only two crossing instances and one like-layer instance, mutually entangled — a consistency finding, **not** independent support |
| `a₀ = cH₀/(2π)` "parameter-free" | **Still suspended** (Staleness #10) |
| `a₀ ~ cH₀`, `a₀(z) = cH(z)/(2π)`, exponent 1 | **Unaffected throughout** |

**Next step, and it is a real derivation task, not an edit:** argue from the primitives why an accelerating chain couples to the cosmic horizon via `κ` while the horizon presents as `T`. If that argument exists, `a₀`'s `2π` is repaired and joins the causal-cone fact as a second piece of untunability structure. If it does not, the honest landing is that `a₀ ~ cH₀` is form-derived and the coefficient is **inherited** — which costs the parameter-free claim permanently and requires softening the language in `Paper_028` §6, `Paper_029` §5.3, and the synthesis papers.

**Do not bank the new route as a result.** It is one criterion that lands one number. That is exactly the shape of the thing this corpus was wrong about the first time.

---

## 6. Falsification criteria

- **F1:** If a channel-count argument can produce a bare `1/(2π)` from P04-additive channel sums without a residual `N_az`, §1's negative is wrong and the mode-amplitude route reopens.
- **F2:** If the substrate argument of §4 is constructed and gives `T_a = T_H` rather than `κ_a = T_H`, the route predicts `a₀ = cH₀` and is **empirically refuted** at 5.7σ-equivalent by the measured value — a clean kill.
- **F3:** If `Paper_BH_Thermal2Pi`'s `2π` is itself shown to be convention-dependent, this route collapses with it and `a₀`'s coefficient is inherited, full stop.

---

*End of note.*
