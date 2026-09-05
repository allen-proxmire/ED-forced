# The Layers — ED's Continuum Laws as a Hierarchy of Coarse-Grainings

Continuum laws are not all the same distance from the Event-Density substrate. They sit at different **layers**, where each layer is **one more coarse-graining (CG) applied to the layer below** — not to the substrate. This is how physics is already organized:

> **substrate** → *(1st CG)* → **layer 1: kinetic** (transport / Boltzmann) → *(2nd CG)* → **layer 2: hydrodynamic** (diffusion / Navier–Stokes) → *(3rd CG)* → **layer 3: thermodynamic**

Nobody coarse-grains atoms straight to the heat equation; the chain is atoms → Boltzmann → Navier–Stokes — *two* steps. "A layer up" means literally one more CG.

This folder maps **which continuum law ED reaches at which layer — and, just as importantly, which it cannot.** The boundaries are the content. A theory that could reach *any* law via enough coarse-grainings would predict nothing; ED's value is the specific map, edges included.

**The thesis** — *the layer divide is the arrow* — is in [`Synthesis_TheDivideIsTheArrow.md`](Synthesis_TheDivideIsTheArrow.md): **committal structure-MAKING** laws (hyperbolic shocks, coherent fields, aggregation) are layer-1-native; **dissipative structure-erasing** laws are layer-2 with an added decorrelation or constraint. The sort is *forced* by ED's defining primitive (P11, the arrow). **Corrected by the soliton test:** reversible structure-*preservation* (dispersive solitons, KdV/NLS) is **not** ED-native — ED disperses what it does not commit, so the dispersive pole is an **edge** (`layer_1/Soliton_Test_NegativeResult.md`).

## The method (the rail)

A layer-N law counts as *reached* only under discipline:

1. **The ingredient added at the CG step is specified in advance, independently justified, and ideally intrinsic or measurable** — never tuned to hit the target. (If you add whatever is needed to land on the law you wanted, you reverse-engineered it.)
2. **Tested by coefficients, not form** — does ED-plus-that-ingredient reproduce the law's *constants* (a validated D, a Green–Kubo consistency), not just its shape?
3. **The no's are recorded with equal weight.** They are the coastline of the map. ED already has a proven edge — *primality* (finite-memory ED provably cannot reach the parity/escape layer, graded against Sarnak's barrier, an external ruler).

## The map so far

| Law | Layer | Status |
|---|---|---|
| **Transport / eikonal** (coarse density field) | 1 | ✓ direct CG of the substrate (ballistic worldlines) |
| **Coherent Maxwell / Coulomb field** | 1 | ✓ coherent part tracks the Coulomb minimizer |
| **Committal (non-Gaussian) field statistics** | 1 | ✓ deposit field is non-Gaussian (100% in the phases) |
| **Diffusion** | 2 | ✓ **RECOVERED** — ED-transport + intrinsic scattering, Green–Kubo-consistent D (see `layer_2/`) |
| **Gaussianity** | 1 & 2 | ✓ **resolved** — layer-1 deposit field non-Gaussian (door #2; stays non-Gaussian even at 8× its correlation length — the structure is in the phases); layer-2 walker density Gaussian (door #1). Observable-and-layer-dependent (see `layer_2/Gaussianity_TwoLayers.md`) |
| **Navier–Stokes** | 1 & 2 | ✓ **compressible NS reached** — inertia/convective (layer 1) + viscosity (layer 2, same velocity decorrelation as the diffusion recovery); **incompressibility ∇·u=0 is the added elliptic pressure constraint = the edge** (ED is hyperbolic/generative). Upgrades NS-2: ν grounded in the substrate decorrelation, not inherited (`layer_2/NavierStokes_LayerTwo.md`) |
| **Yang–Mills action (F²)** | 2 | ✓ **derived (analytic)** — the substrate coherence-deficit on the U(N) plaquette holonomy = the Wilson action → −¼Tr(F²); the non-abelian lift of the grounded abelian Maxwell case. Closes the YM-2 open item O-YM2-2 (postulate P→D). Rests on the coherence = Re Tr U_□ assumption (`event-density/foundations/Gauge_06_YangMillsAction_FromCoherenceDeficit.md`) |
| **Yang–Mills mass gap** | — | ✓ **mechanism** — the gap = the signature of *non-abelian channel structure*: the same coherence-deficit that gives F² carries the [A,A] self-interaction for U(N≥2) that abelian Maxwell lacks → Maxwell layer-1 massless, YM gapped. Candidate for YM-4's coercivity (O-MG-1) + strong-coupling area law (O-MG-4). Physics, not a Clay proof; continuum survival conditional (`event-density/foundations/Gauge_07_YangMillsGap_FromCoherenceDeficit.md`) |
| **Geometric (Ricci / mean-curvature)** | 1 & 2 | ✓ **MEASURED** — *is* GR-III's bandwidth rule ḃ=D∇²b−κρ: layer-2 metric-smoothing (weak-field Ricci) + layer-1 commitment-concentration (horizon, b→0). Same structure as NS; **the bridge to ED's gravity/info arc** (`Geometric_Gravity_Bridge.md`). Weak-field/khronometric; full nonlinear Ricci/Einstein is the edge |
| **Primality (escape/parity)** | — | **edge — proven unreachable** (Wall 2, finite-memory ceiling) |

**Full Atlas sweep + the corrected rule:** see [`Atlas_Sweep.md`](Atlas_Sweep.md) — all fourteen AD-Atlas PDEs mapped. The divide is **commitment**: *committal structure-making* (hyperbolic shocks, coherent fields, aggregation) is **layer-1-native**; *dissipative structure-erasing* (the parabolic/diffusive pole) is **layer-2** with an added decorrelation or constraint; *reversible structure-preservation* (dispersive solitons) is an **edge** — the soliton test refuted the earlier layer-1 placement of KdV/NLS (ED disperses, defocusing + dissipative).

> **2026-09-05 — two arcs ran into this seam and were citing none of it.** Gravity's `a₀` `2π` route and state-reduction's branch-phase question both turn on what crosses the layer boundary. **Two findings from connecting them:** the P12 term **`Grad`, proposed the same day as the discrete Dirichlet form, is the substrate-level object that coarse-grains to this folder's one forced operator** — giving `∇·(M∇φ)` a substrate origin it does not currently have; and **the corpus carries two different decorrelations under one word** — the statistical layer-2 add named below, and a **layer-1 geometric** one measured at `ξ ≈ 5ℓ_ED` in `substrate-evaluation/Paper_PhaseCoherence_P12Coh`. **What this folder does NOT supply, and both arcs need: any account of a numerical factor attaching to a crossing.** `Note_TheSeam_And_SigmaC_2026-09-05.md`.

## The gap between layers is always the same thing

Going layer 1 → layer 2 always adds **decorrelation** — molecular chaos, independence, mixing, scattering. It is the step where the arrow is averaged out and the symmetry is manufactured. The "missing ingredients" found across the CoarseGrain arc were one gap, three faces: RC needed **extinction**, diffusion needed **collisions/scattering**, Gaussianity needs **independence**. **Reversibility and Gaussianity are layer-2 phenomena** — layer-1 shadows still carry the arrow.

## Honest tiers

- **Textbook-solid:** the multi-layer CG hierarchy itself (kinetic theory).
- **Measured:** ED's *direct* CG lands on layer 1 (transport, non-Gaussian, coherent Coulomb).
- **First layer-2 win:** diffusion, recovered with a passing coefficient (Green–Kubo) test.
- **Open / testable:** Gaussianity (which layer/observable), Navier–Stokes, Yang–Mills.

## Pointers

- Framing note: `event-density/foundations/TwoLayer_CoarseGraining_Hierarchy.md`.
- Sims: `event-density/evaluation/CoarseGrain_Arc/`.
- The three early substrate-evaluation CG papers (ContinuumShadows_Decomposition, CanonicalPDEChannels_BottomUp, OneCapacityTwoScales) — written under the flat "walls" framing — are **superseded and retired**, absorbed into the forthcoming paper *The Arrow Sorts the Continuum*. Relocated out of the repo for archiving.
