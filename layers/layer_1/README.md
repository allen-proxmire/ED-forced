# Layer 1 — ED's Direct Coarse-Graining

**Layer 1 is one coarse-graining from the substrate** — the continuum laws ED casts *directly*, by building. These shadows still carry the substrate's character: they are **structure-making, hyperbolic, arrow-bearing**. Reversibility, diffusion, and Gaussianity are *not* here — those are manufactured one layer up, where decorrelation is added.

## What lives at layer 1

| Law / object | What ED does | Result |
|---|---|---|
| **Transport / eikonal** | the coarse density field's evolution regresses to \|∇ρ\| (ballistic worldlines, \|v\|≈1), not ∇²ρ | ensemble-mean R² ≈ 0.60 eikonal vs 0.26 diffusion (`diffusion_coherent_decomp.py`) |
| **Coherent Maxwell / Coulomb field** | averaging the gauge field ⟨e^{iφ}⟩ recovers the Coulomb (action-minimizing) profile; the incoherence is localized entropy | coherent deficit·r² tracks the Mod-B minimizer (`maxwell_coherent_decomp.py`) |
| **Committal (non-Gaussian) statistics** | the deposited field is non-Gaussian, with 100% of the non-Gaussianity in the Fourier phases (structure = phase correlation) | phase-randomized surrogate Gaussian (skew 0.003), real field not (skew 0.96) (`fourier_phase_test.py`) |

## The character of layer 1

Layer-1 laws **keep the arrow.** The substrate is committal — it correlates, builds structure, moves one way — and its direct shadow inherits that: transport is directional, the field is phase-correlated and non-Gaussian, the coherent field is the structured Coulomb pattern. ED is, at this layer, a *structure-making, hyperbolic-pole, phase-correlating* substrate.

What is **absent** at layer 1 is exactly what the second coarse-graining manufactures: velocity decorrelation (→ diffusion), phase decorrelation (→ Gaussianity), time-reversal symmetry (→ reversible PDEs). See `../layer_2/`.

## Sims

`event-density/evaluation/CoarseGrain_Arc/`: `diffusion_coherent_decomp.py`, `maxwell_coherent_decomp.py`, `fourier_phase_test.py`, `coarsegrain_test.py`.

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[Soliton Test](Soliton_Test_NegativeResult.md)**
- **[Transport / Eikonal](Transport_LayerOne.md)**
