# Layer 2 — the Second Coarse-Graining

**Layer 2 is a coarse-graining of layer 1's shadow** — and the step *adds an ingredient the substrate does not have on its own:* **decorrelation** (molecular chaos, independence, mixing, scattering). This is where the arrow is averaged out and the symmetry is manufactured. The laws that live here — diffusion, Gaussianity, reversible/thermal behavior — are exactly the ones ED could not make at layer 1 "by building."

## The rail for claiming a layer-2 recovery

1. The decorrelation ingredient must be **intrinsic, or specified in advance and independently justified** — never a knob tuned to hit the target law.
2. The test is on **coefficients, not form** — a validated D, a Green–Kubo consistency — so "diffusion-shaped" cannot pass for diffusion.
3. The result is reported whichever way it lands. An edge (no recovery) is as informative as a win.

## What's here

| Law | Ingredient (justified, not tuned) | Status |
|---|---|---|
| **Diffusion** | the substrate's *intrinsic* scattering off ρ-disorder (worldlines decorrelate on their own — measured, not added) | ✓ **RECOVERED** — Green–Kubo D ≈ MSD D to 9%, α→1, near-Gaussian profile. See `Diffusion_LayerTwo_Recovery.md` |
| **Gaussianity** | independence (CLT) once contributions decorrelate past the correlation length | open — the layer-2 *walker density* came out near-Gaussian (the diffusion result), pointing at door #1; the layer-1 *deposit field* is non-Gaussian. **Gaussianity is observable-and-layer-dependent.** Correlation-length test pending |
| **Hydrodynamics / Navier–Stokes** | viscosity / collisional closure | not yet tested (the big swing) |

## The character of layer 2

Layer 2 is where the world goes **smooth, reversible, and Gaussian** — because that is where independence is assumed. The first concrete demonstration is diffusion: ED's ballistic worldlines (layer 1) scatter off the substrate's own disorder and their position-density spreads as genuine diffusion, with the fluctuation-dissipation (Green–Kubo) relation holding. The arrow that was load-bearing at layer 1 is, here, averaged away.

## Sims

`event-density/evaluation/CoarseGrain_Arc/diffusion_layer2_test.py` (and the pending correlation-length / Gaussianity test).

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[Gaussianity](Gaussianity_TwoLayers.md)**
- **[Navier–Stokes](NavierStokes_LayerTwo.md)**
- **[Layer-2's Decorrelation Is One Operator](OneOperator_TheLaplacian.md)**
