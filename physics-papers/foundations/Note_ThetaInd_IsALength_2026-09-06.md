# `θ_ind` is a length in disguise — and none of the three routes the corpus named is the right one

**Date:** 2026-09-06
**Status:** **Result.** The individuation paper's one undetermined quantity, characterized.
**Probe:** `../event-density/theory/individuation_theta_probe.py` (new, re-runnable).
**Tier:** the four results below are **analytic**, each confirmed numerically. **No value for `θ_ind` is derived, and none is claimed.**

---

## 1. The question, as the corpus states it

`Paper_Individuation_TheSystemEnvironmentCut.md` defines

$$S \text{ individuated} \iff R(S) = \frac{b_{\rm int}(S)}{b_{\rm bdry}(S)} > \theta_{\rm ind}$$

and records `θ_ind` as **the paper's one undetermined quantity** (audit row 7, `I (inherited)`). The source concept asks, twice: *"Structural constant? Regime-dependent? Tied to `ℏ` / bandwidth normalization?"*

**This did not attempt a value.** It asked what *kind* of quantity `θ_ind` is, because that decides what evidence could ever fix it.

## 2. (A) The `ℏ` / bandwidth-normalization route is closed

`b_int` and `b_bdry` are both **homogeneous of degree 1** in the edge weights, so under a global rescaling `b → λb` the ratio is unchanged. Measured: `λ = 1000` moves `b_int` from `60.0` to `60000.0` and leaves `R = 2.500000` exactly.

> **`θ_ind` is dimensionless in bandwidth. No bandwidth normalization and no value of `ℏ` can supply it — there is nothing for a scale to attach to.**

**One of the source concept's three named routes is closed by inspection.** That is a banked negative, not a result about the value.

## 3. (B) Individuation is closed under union, for every `θ`

If `R(S) > θ` and `R(T) > θ` then `R(S ∪ T) > θ`. **Unconditionally** — for disjoint, adjacent and overlapping `S`, `T` alike, since any edges *between* them move from boundary to internal, which only raises the ratio. The proof is one line: `I_S > θB_S` and `I_T > θB_T` give `I_S + I_T > θ(B_S + B_T)`, and merging can only improve on that. Measured: **0 violations in 400 random pairs.**

> **So no choice of `θ_ind` makes this an object-*count* criterion.** Two separate individuated systems always union to an individuated one. **It is a cohesion filter, not a "this is one thing" test.**

This matters downstream: the four-band classification uses individuation to separate Adjacency from Environmental channels *relative to a choice of `S`*. **Union closure means the family of admissible `S` is upward-closed, so "the system" is never picked out by the criterion alone** — something else has to choose `S`, and the criterion only checks it.

## 4. (C) `R` is a linear extent, dimension-independently

For a hypercube of side `a` on a hypercubic lattice with unit weights, in **any** dimension `d`:

$$b_{\rm int} = d\,a^{d-1}(a-1),\qquad b_{\rm bdry} = 2d\,a^{d-1},\qquad \boxed{R = \tfrac{a-1}{2}}$$

The `d` and the `a^{d-1}` cancel. Confirmed exactly for `d = 1, 2, 3`; a 1-D chain of `a` nodes has `a−1` internal edges and 2 boundary edges, giving the same `(a−1)/2`.

| side `a` | 2 | 3 | 4 | 6 | 9 | 12 |
|---|---|---|---|---|---|---|
| `R` measured | 0.500 | 1.000 | 1.500 | 2.500 | 4.000 | 5.500 |
| `(a−1)/2` | 0.500 | 1.000 | 1.500 | 2.500 | 4.000 | 5.500 |

**It survives disorder** (60% bandwidth disorder, 5 seeds: deviations −7.6% to +6.9%) **and real committed morphology** (greedy accretion on the certified rule: `R/(√|S|/2)` stays in `0.56–0.67` from `|S| = 4` to `200`).

> **So `R` does not measure cohesion in any scale-free sense. It measures LINEAR EXTENT in lattice units, and `R > θ_ind` reads `linear extent > 2θ_ind + 1` loci.**

**`θ_ind` is a length wearing a dimensionless costume.** That answers the source concept's question: it is *none* of "structural constant", "regime-dependent", or "tied to `ℏ`" as those were meant — it is **tied to the substrate's own length unit**.

### Two boundary values worth recording

- **A single locus has `b_int = 0`, so `R = 0`.** One thing on its own is not individuated at all.
- **The minimal composite — two loci sharing an edge — gives `R = 1/2` exactly, in every dimension.**

So `θ_ind < 1/2` individuates any connected pair; `θ_ind ≥ 1/2` requires more than a pair. **Reading this as consilience with *"two is more fundamental than one; one isolated thing = zero"* is an interpretive observation, not a derivation, and is tiered as such.** It does not select a value.

## 5. (D) — and `R` is a length ONLY where the substrate has geometry

On a geometric graph the cut scales like a surface and the interior like a volume, so `R ~ linear size`. **On an expander the Cheeger constant is bounded below** — the cut grows *with* the volume — so `R` stays `O(1)` however large `S` gets. Measured, degree-4 lattice against a degree-4 random regular graph:

| `\|S\|` | 4 | 16 | 36 | 81 | 144 | 256 |
|---|---|---|---|---|---|---|
| `R` lattice | 0.500 | 1.500 | 2.500 | 4.000 | 5.500 | **7.500** |
| `R` expander | 0.300 | 0.441 | 0.473 | 0.513 | 0.514 | **0.562** |

> **ED's metric locality is EMERGENT, not primitive ([[reference_ed_locality_tiers]]).** So `θ_ind`'s very *character* changes across that transition: **a length threshold in the geometric regime, a genuinely dimensionless cohesion threshold before it.**

## 6. What this does to `F-IND-2`, stated carefully

`F-IND-2` asks for *"a demonstration that `θ_ind` must be regime-dependent in a way that cannot be absorbed into bandwidth normalization."*

**(A) shows bandwidth normalization can absorb nothing at all** — `R` is invariant under it, so the escape route in the falsifier's own wording is not available. **(C) and (D) show `θ_ind` is a length in the geometric regime and not a length before it.**

**That is not `F-IND-2` fired, and it should not be banked as one.** The falsifier asks whether physics *needs* more than one threshold; this shows only that a fixed `θ_ind` **is** a fixed length, so any two regimes with different characteristic lengths would need different `θ_ind`. **Whether ED has two such regimes in a load-bearing way is not shown here.** `F-IND-2` moves from hypothetical to concrete and testable — no further.

## 7. What would now determine it

Not a bandwidth calibration, and not a measurement of `ℏ`. **`θ_ind` is fixed by naming the length at which system/environment cuts become sharp**, in units of `ℓ_ED`. Two honest routes:

1. **Decoherence.** `qft/Paper_024_LindbladLimit` postulates a factorization (`P-Factorized-IC`) where this constructs a ratio. The scale at which that factorization becomes accurate is the same scale, approached from the other side — and the paper already says the two accounts *"should be read as two accounts of the same gap"*.
2. **`ξ`.** The corpus already has a measured substrate correlation length, `ξ_canonical ≈ 1.8 ± 0.3 lu` (`Paper_096`). **If individuation is sharp at the correlation length, `θ_ind = (ξ − 1)/2 ≈ 0.4 ± 0.15`** — which sits just below the pair value `1/2`. **This is an arithmetic consequence of (C) plus an identification nobody has argued for**, and is recorded as a candidate to be argued or refuted, **not as a result.**

**`θ_ind` remains undetermined.** What has changed is that it is no longer an unknown dimensionless constant — it is a length, and the corpus has lengths.
