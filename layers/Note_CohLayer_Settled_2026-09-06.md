# `Coh` is evaluated at layer 1 — and my `ξ ≈ 5ℓ_ED` reading yesterday was wrong

**Date:** 2026-09-06
**Status:** Closes the layer seam's second debt (`Note_TheSeam_And_SigmaC_2026-09-05.md` §4.2). Also **corrects an error I introduced yesterday** in `state-reduction/Note_Theta12_LayerQuestion_2026-09-05.md`.
**Anchors:** `Paper_087` §P12, `substrate-evaluation/Paper_PhaseCoherence_P12Coh` (preamble 4, §5.4), `gravity/Note_a0_TwoPi_RepairRoutes` §4f/§4h, gravity ledger #71.

---

## 1. The correction first, because everything downstream of it moved

Yesterday's `Θ₁₂` note wrote: *"`Θ₁₂` decorrelates beyond **`ξ ≈ 5ℓ_ED`**."* **That is wrong, and it is the same mistake pattern as the rest of this session — a number lifted out of its context.**

`Paper_PhaseCoherence_P12Coh`'s `ξ ≈ 8–12` and `ξ < 1` are **measurements in lattice units of a 60×60 probe grid**, and their job is §5.4's point that *"the connection strength has a usable window"*. **They are not a claim that `ξ` is five substrate lengths.** What the paper actually says about `ξ` is preamble 4:

> **It does not derive the reach `ξ`** (identified with **V5's memory length `ℓ_V5` and the MOND transition reach**). `ξ` is **value-inherited**, set by the P05-connection strength and the substrate's disorder variance. **Form-forced-finite, value-inherited.**

**So the probe establishes the *form* — that the reach is finite rather than infinite — and not the *scale*.** The scale is inherited, and it is identified with something macroscopic. **`ξ` is not ~5 Planck lengths; it is the MOND transition reach**, which is `~10¹⁵ m` even for the Sun.

## 2. The answer: layer 1, on raw polarity

**Four steps, each citing something prior.**

1. **`a_C = −∇_adj Σ_C`**, and `∇_adj` is *"a difference over substrate-graph adjacency, not a continuum gradient"* — **so accelerations are definitionally layer-1 objects** (`Note_a0_TwoPi_RepairRoutes` §4f, which is also what §4h leaned on to settle the `2π`). **`Coh` is a term inside `Σ_C`, so it is evaluated wherever `Σ_C` is: layer 1.**
2. **Layer-1 polarity is raw polarity, transported by P05's connection.** The coarse-grained holonomy is a layer-2 object by construction — that is what makes it the other horn of the fork.
3. **That connection is not flat.** `Paper_PhaseCoherence` §4: *"P05 transports polarity with a connection. A physical connection is not flat; it responds to the substrate."* Its quenched disorder is what gives `Coh` a **finite reach `ξ`** rather than crystalline order.
4. **`Coh` is the term that carries MOND.** Ledger #71's three-way sign check placed the bilocal cross term in **`+Coh`** — it is what reproduces `a = a_N + √(a_N a₀)`.

**Steps 3 and 4 close a loop with preamble 4:**

> **`Coh` is the MOND term. `Coh` at layer 1 has reach `ξ`. `ξ` is the MOND transition reach.**

Three statements, made independently in three places, and they are consistent only if `Coh` sits at layer 1.

## 3. The counterfactual, which is what makes this decisive rather than merely tidy

**If `Coh` were evaluated at layer 2, on the coarse-grained holonomy, it would have no `ξ`** — the coarse-grained object is phase-averaged by construction, which is the layers program's own account of what crossing the seam does.

**A phase-averaged `Coh` has `cos Θ` either 1 everywhere or 0 everywhere:**

- `cos Θ = 0`: the bilocal cross term vanishes, and **there is no `√(a_N a₀)` at all.**
- `cos Θ = 1`: the cross term exists but has **no reach**, so there is no *transition* — MOND would apply at every scale, including the solar system.

**Either way the MOND transition scale loses its origin in `Σ_C`.** So layer 2 is not merely unmotivated; **it removes the thing that gives `a₀` its reach.** That is the argument.

## 4. What this does not do

**It does not derive `ξ`.** The paper is explicit that the reach is value-inherited, and this note changes nothing about that. **It says where the MOND scale enters `Σ_C` — through `Coh`'s finite reach at layer 1 — not what the scale is.**

**And it inherits the operationalization's own tier.** `Paper_PhaseCoherence` preamble 2 is clear that reading `Coh` as phase-coherence is *"form-forced conditional on the reading, not forced from a deeper layer"*, and that **the certified `Σ`-rule's `Coh` is `−(ρ−ρ_*)²`, which is phase-blind.** So this settles which layer the *phase-coherence reading* of `Coh` lives at. It does not promote that reading.

## 5. Consequence for `Θ₁₂` — the fork collapses, and both horns now agree

Yesterday's fork was: *controllable at layer 2, separation-dependent at layer 1*, with the layer unsettled.

**Layer 1 wins — but with `ξ` corrected, layer 1 gives the layer-2 answer at any laboratory scale.** `Θ₁₂` is a raw-polarity phase difference whose decorrelation length is the MOND reach, `≳10¹⁵ m`. A collapse experiment spans metres. **So `Θ₁₂` is coherent across any realizable branch separation, i.e. controllable** — which is what the layer-2 horn said, reached by the layer-1 route.

**The form of yesterday's layer-1 statement was right** (*"`≈ 1` when the branches coincide, decorrelating as they separate"*) — **only the scale was wrong, and it was wrong by about fifteen orders of magnitude.** The practical answer flips from "decorrelates in any real experiment" to "decorrelates in none."

**That is a materially different prediction for the collapse arc**, and it is the useful output of this note.
