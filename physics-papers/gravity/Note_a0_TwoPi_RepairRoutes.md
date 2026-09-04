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

## 5. Status and what to do next

| Item | State |
|---|---|
| Mode-amplitude route (Staleness #10's named candidate) | **CLOSED — negative.** P04 additivity is across channels; the sum is not a density (§1) |
| Rindler / de Sitter smoothness route | **OPEN — better.** Reproduces the number with a non-cancelling `2π` already derived in the corpus (§3) |
| The `κ_a = T_H` matching condition | **Advanced 2026-09-04, still the debt.** The horizon half is grounded (`Paper_028` §3.4: statistical, not geometric ⟹ no `b`-gradient ⟹ no `κ` available, only a state). The chain half is now a **layer argument** — the `2π` is the layer-1/layer-2 seam crossed exactly once — rather than a bare assertion. Not derived. See §4b |
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
