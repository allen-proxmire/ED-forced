# Is `Θ₁₂` fixed, controllable, or random? It depends on the layer — and it is the same layer question that carries the `2π`

*State-reduction working note, 2026-09-05. Answers the item left open by `Note_CollapseEnergyIsSigmaC_2026-09-05.md` §6. **Short by design: the answer is a fork, and the useful part is that it is not a new fork.***

---

## Verdict

**Neither fixed nor random. Controllable at one layer, decorrelating at the other — and the corpus has not settled which layer `Coh` is evaluated at.**

**That unsettled layer is the same one carrying the whole `a₀` `2π` argument** (`gravity/Note_a0_TwoPi_RepairRoutes.md` §4f). **Two open items in two arcs reduce to one question:** *at which layer is `Σ_C` evaluated?*

---

## 1. What the corpus already fixes

**Relative phase is physical, not gauge.** `Paper_008_5_PhaseIndependence` preamble item 4, unambiguously:

> *"**Relative phases between amplitudes carry observable interference content**; only global-phase independence of bandwidth magnitudes is claimed here."*

**So `Θ₁₂` is a real quantity.** "Fixed" and "gauge artifact" are both off the table.

**And the quantum phase is a coarse-grained object.** `Paper_009_BerryPhase`: Berry phase is *"the holonomy of the **coarse-grained** substrate polarity-transport connection"* — row 8 tiers it `D-via-I` as *"application of I-Holonomy to **coarse-grained** connection."* **The corpus explicitly distinguishes the raw P05 connection from its coarse-grained version, and puts observable quantum phase on the latter.**

**But the substrate phase decorrelates.** `Paper_PhaseCoherence_P12Coh` measures it: the P05 connection carries the substrate's own quenched disorder, random-walking the raw polarity to **`ξ ≈ 4–6` lattice units**, i.e. `≈ 5ℓ_ED ≈ 10⁻³⁴ m`. That is the measured result the whole July arc rests on.

## 2. The fork

**`Coh = 2√(b₁b₂)\cosΘ₁₂` is a term in `Σ_C`. Which phase is `Θ₁₂`?**

- **Layer 2 — the coarse-grained holonomy.** `Θ₁₂` is the interferometric phase: **controllable**, set by preparation, the thing a two-path experiment tunes. §6 of the collapse note stands, and ED has a phase-dependent collapse rate that DP does not.
- **Layer 1 — the raw substrate polarity.** `Θ₁₂` decorrelates beyond `ξ ≈ 5ℓ_ED`. Not random *per se*: it is `≈ 1` when the branches coincide and decorrelates as they separate. **So `Coh ≈ 2√(b₁b₂)\,C(Δx)` with `C` the substrate phase-correlation function of range `ξ`.**

**And P12 points at layer 1.** `Note_a0_TwoPi_RepairRoutes` §4f established, from `Paper_087` §P12's own operational content, that `a_C = −∇_adj Σ_C` is *"a difference over substrate-graph adjacency, not a continuum gradient — so in ED an acceleration is definitionally a layer-1 object."* **If `Σ_C` is layer-1, so is every term in it, `Coh` included.**

## 3. Why the fork is worth more than either answer

**Both branches reproduce the two limits that mattered this morning**, which is why the collapse identity is not in danger:

| | Layer 2 | Layer 1 |
|---|---|---|
| Branches coincide | `Coh = 2√(b₁b₂)`, `E_Δ = 0` ✓ | `C(0) = 1`, same ✓ |
| Branches far apart | `E_Δ → E₁₁+E₂₂` as the overlap dies ✓ | `C(Δx) → 0`, same ✓ |

**They differ in the *profile between* those limits, and that is exactly what Diósi–Penrose experiments measure.** Penrose's cross term dies over the **object's own size** — for a 100 nm sphere, saturation at ~100 nm separation. **Layer 1's dies over `ξ ≈ 10⁻³⁴ m`**, i.e. the collapse energy would saturate essentially immediately on any laboratory scale.

**That is a sharp, near-term-relevant difference between the two readings of ED's own functional**, and it is decided by a question the corpus has not answered.

## 4. Honest limits on this note

**I am at the edge of over-deriving and am stopping here deliberately.** What is established: relative phase is physical (cited), quantum phase is coarse-grained (cited), substrate phase decorrelates at `ξ ≈ 5ℓ_ED` (measured), and P12 reads as layer-1 (argued in §4f, itself not closed). **What is *not* established: that `Coh`'s phase is the same object as the branch phase an interferometer sets, or that the substrate correlation function `C(Δx)` transfers to a two-branch mass superposition at all.** §3's saturation-scale claim assumes both, and neither has been checked.

**So: the answer to "fixed, controllable, or random" is "controllable at layer 2, separation-dependent at layer 1, and the corpus does not say which applies."** The collapse identity (`E_Δ = Str − Coh`) is unaffected — it is algebra. **What is conditional is whether ED's cross term reproduces Penrose's mutual energy**, and that now depends on the layer.

## 5. The convergence, which is the point

`Note_a0_TwoPi_RepairRoutes` §4f: the entire remaining debt on the `a₀` coefficient is *"given that we compare at layer 1, why does the seam contribute `1/2π` rather than `2π`?"*

**Here: given that `Σ_C` is layer-1, does `Coh`'s phase decorrelate at `ξ`?**

**Both are the same question about the same seam, reached from two arcs that share nothing else.** Settling *at which layer `Σ_C` is evaluated, and what crosses the seam when it is read from the other side* would move the gravity arc's most-disputed number and the collapse arc's Penrose correspondence together.

~~**Nothing in the corpus currently treats the layer seam as a single object.**~~ **WRONG, corrected the same day.** `layers/` treats it as a single object and has a thesis about it — *the divide is the arrow* — plus a sharper result underneath: **layer 2's decorrelation add is ONE forced operator, the gradient-flux Laplacian `∇·(M∇φ)`** (`layers/layer_2/OneOperator_TheLaplacian.md`). **What is true and narrower: neither this arc nor the `2π` route cites any of it.** And the layers program **narrows this note's fork**: the layer-2 add is statistical and arrow-erasing, whereas `Paper_PhaseCoherence`'s `ξ` is a **layer-1 geometric** decorrelation from quenched substrate disorder. **Two different objects under one word.** So the question is not *“does crossing the seam randomize the phase?”* but ***“is `Coh` evaluated on raw polarity, which carries `ξ`, or on the coarse-grained holonomy, which does not?”*** `layers/Note_TheSeam_And_SigmaC_2026-09-05.md`.

---

*Gravity ledger Staleness #75.*
