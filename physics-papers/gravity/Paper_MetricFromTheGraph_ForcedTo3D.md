# The Metric Comes Out of the Graph: Curvature, g ~ 1/b, and Why Only Three Dimensions

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — gravity arc (curvature emergence)
**Status:** Publication draft (short). Foothold result on the emergent-geometry bridge: does a metric with a length scale come out of a participation graph whose edges carry no length. Four numerical probes on constructed substrates, reported together with an honest layer-1/layer-2 reading. Companion to GR-I (the weak-field metric it recovers), Paper_025 (the holographic bound it uses), `Paper_AreaLawIsTheEdgeCount` (the surface-count it inherits), and `Paper_Continuum_KineticLatticeGas` (the two-layer coarse-graining that frames the honest scope). Standalone; cold-reader accessible.
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **This is not a derivation of the full Einstein field equations.** It concerns the *static, linearized* emergent metric only. The nonlinear, dynamical regime (ED's own field equations, which are khronometric, not exact GR) is untouched and remains open.
3. **The result is a self-consistency / fixed-point, not a from-nothing derivation.** The reach law that forces g ~ 1/b is derived *conditional on* ED's holographic surface-count (itself resting on the area-law-as-edge-count result) and on the reading that bandwidth counts independent channels. These are established inputs, but they are inputs, not re-derived here.
4. **The construction is not background-free.** A background lattice (or label line) and its topology are assumed. The *metric on top of it* is genuinely emergent (distances are read from connectivity, never assigned), but the index/topology itself is not derived from a truly background-free graph.
5. **The absolute length scale is inherited, not computed.** The single length unit is the Planck grain ℓ_P already postulated (P08). This paper shows no *new* scale is introduced; it does not compute ℓ_P's value, nor a specific length such as a Schwarzschild radius in grains (which needs the mass→b map and G).
6. **The clean metric exponent is not read off raw paths in 3D, and is not claimed to be.** In genuine 3D the raw ballistic shortest-path metric is faceted and non-Gaussian (layer 1); the clean single exponent g ~ 1/b is a layer-2 object. The exponent's derivation is a *count* (§4), not a transport measurement; the 3D probe confirms isotropy-emergence, not a second exponent measurement (§5, §6).
7. **The bandwidth-to-connectivity coupling is integer-quantized, and it VANISHES at small reach.** The probes set a locus's reach as `max(1, round(R0 * b^p))`. Because that rounds to a whole number and `b` never exceeds 1, a small `R0` cannot resolve any variation in `b` at all. Measured directly on the 3D arena (spherical depletion to `b_min = 0.05`), the fraction of edges the 'mass' actually changes is **0.00% at R0 = 1, 2.70% at R0 = 2, 4.25% at R0 = 4**. So at nearest-neighbour reach the construction is a *plain lattice* and the bandwidth field is inert — any result obtained there is a fact about the background, not about `b`. This bounds the probes from both sides: reach must be large enough for `b` to couple at all, yet each increment of reach enlarges the neighbourhood (mean degree ~31 at R0 = 2), which is what pushes the clean exponent out of raw transport and into the layer-2 regime item 6 describes. The P1-P4 results are unaffected (all were run at coupling reach), but the floor is a real constraint on the arena and was not previously recorded. *(Measured, added 2026-08-31; see the spectral-dimension scoping note in the working repo for the run that surfaced it.)*

---

## Abstract

General Relativity, in Event Density, is recovered at the continuum level by assigning the emergent spatial metric g ~ 1/b, where b is the bandwidth field (GR-I). The bridge one level below has been the standing open question: does the **raw participation graph**, connectivity only and no lengths on its edges, actually *produce* distances that reproduce g ~ 1/b, or a different metric, or none. This paper reports four numerical probes on constructed substrates and one honest reading. **(1) A metric emerges.** With bandwidth entering only through connectivity (a higher-bandwidth locus reaches farther) and distance read as plain unweighted hop-count, a well-defined metric comes out (fit to ∫dx/b^q, R² = 1.000), and a bandwidth depletion (a "mass") reads as *far*: the curvature signature, from connectivity alone. **(2) The reach law is forced, and it selects three dimensions.** The exponent linking reach to bandwidth is not free: ED's holographic channel-count (bandwidth = independent channels = boundary cut ~ surface R^{d−1}, the area-law-as-edge-count result) fixes reach ∝ b^{1/(d−1)}. The ball-cut exponent is measured at 0.984 in 2D and 2.008 in 3D, so the reach law is p = 1 in 2D and p = ½ in 3D; feeding it back, the emergent metric is g ~ 1/b² in 2D and **g ~ 1/b (GR-I) in exactly three dimensions**, the unique dimension where the holographic reach law reproduces General Relativity, and the same number the independent linking argument selects for holding committed order. **(3) No new length scale.** The reach normalization drops out of the metric exponent (q = 0.500 flat across two orders of magnitude, the physical curvature effect scale-invariant), so the one length unit is the Planck grain ℓ_P already postulated, not a new constant. **(4) Isotropy emerges under coarse-graining.** In a genuine 3D lattice with a spherical mass, the emergent metric is isotropic, but not exactly on the raw graph: the raw ballistic shortest-path metric is faceted (axis and body-diagonal rays differ), and the faceting washes out toward the continuum as the reach coarsens (anisotropy 0.35 → 0.00). This is the layer-1 (ballistic, non-Gaussian) → layer-2 (isotropic continuum) transition of the two-layer coarse-graining picture. Consistent with that picture, the clean radial exponent is *not* extractable from the raw 3D paths (a layer-2 quantity measured on layer-1 ballistic paths); it lives in the count of (2), which is why the count is clean and the transport measurement is not. The net: a curved metric emerges from a graph with no geometry, its shape is forced to g ~ 1/b by ED's own holographic bound uniquely in 3D, it introduces no new scale, and it emerges isotropically only after coarse-graining, exactly as a non-Gaussian substrate should. The static/linear curvature-emergence bridge stands on the primitives' own inputs; the nonlinear regime and a background-free construction remain the open frontier.

---

## 1. Introduction

Event Density recovers weak-field gravity by reading a spatial metric off its bandwidth field: where a locus can do less relating (lower b, nearer a mass), space is "longer" (GR-I gives g ~ 1/b, and the dynamical rule GR-III gives the Poisson limit). But GR-I *assigns* that metric at the continuum level. The deeper claim ED needs, and the one Paper_039 §3.2 explicitly defers by borrowing the horizon radius from GR, is that the metric is not an assignment at all but a *consequence*: that a graph of participations, with no distances written on its edges, already contains the distances, and that they are gravity's.

This is the curvature-emergence bridge, and it sits under more than gravity. The area-law result (`Paper_AreaLawIsTheEdgeCount`) and the horizon tiling (`Paper_HorizonTilingThreeCounts`) both assume an emergent geometry rather than deriving it; the spatial-3D argument (the linking premise) needs a geometry to even ask its question in. A foothold on curvature emergence is a foothold under all of them.

This paper reports a foothold, not the finished bridge. Four probes, taken in order, answer four sharp questions: does a metric come out of the graph at all; is the reach law that gives GR-I forced or tuned; is a new length scale smuggled in; and does the emergent metric behave isotropically like gravity in genuine three dimensions. The answers are, respectively: yes; forced, and only in 3D; no; and yes but only after coarse-graining, which turns out to be the most instructive answer of the four.

---

## 2. Primitive Inputs and Method

**The non-circular construction.** The trap to avoid is assigning the geometry one claims to derive. So: nodes sit on a background **label** structure (a 1D line, or a 3D lattice) that is pure bookkeeping, *not* a metric. A bandwidth field b varies over it (baseline 1, depleted toward b_min at a "mass"). Bandwidth enters **only through connectivity**: a locus of bandwidth b reaches farther, connecting to neighbors within a reach ∝ b^p (b as participation capacity, P04). The emergent distance is then the plain **unweighted hop-count** (breadth-first / unweighted shortest path) between nodes, read off the structure and never assigned. The metric exponent is *measured* from the emergent hop-distance, not put in.

**What g ~ 1/b means, operationally.** Proper distance ds = dx/√b, i.e. hop-distance ~ ∫dx/b^{1/2}. Generally, if hop-distance ~ ∫dx/b^q then the emergent metric is g_xx = 1/b^{2q}, so q = ½ ↔ g ~ 1/b (GR-I) and q = 1 ↔ g ~ 1/b². The probes measure q; they do not assume it.

**The four probes.**
- **P1 (emergence):** 1D label line, a Gaussian bandwidth dip, reach ∝ b^p; measure whether a metric emerges (fit q), and whether the dip reads as *far* (excess hops vs flat).
- **P2 (reach law):** measure the boundary-cut exponent of a radius-R ball in short-range d-dim lattices (expected d−1 if the channel-count is holographic), giving the *derived* reach exponent p = 1/(d−1); feed it into the metric and read the resulting g.
- **P3 (length scale):** sweep the reach normalization R₀ over two orders of magnitude; test whether the metric exponent depends on it (physics) or is invariant (pure length unit).
- **P4 (3D isotropy):** genuine 3D lattice, spherical bandwidth dip (a point mass); measure directional dependence (axis vs body-diagonal rays, per-shell variation) and its behavior as the reach coarsens.

**Reproducibility.** Scripts, all in `evaluation/CurvatureEmergence/`: `metric_from_bandwidth_probe.py` (P1), `holographic_reach_law_probe.py` (P2), `length_scale_probe.py` (P3), `isotropy_3d_probe.py` + `isotropy_3d_convergence.py` + `radial_metric_clean.py` + `radial_localslope.py` (P4). Lattices are one-locus-per-cell (P08); edges are reach-balls; distances are `scipy` unweighted shortest paths or BFS. No primitive forcing is invoked; the constructions read the primitives, they do not add rules.

**Regime of validity.** Constructed substrates (a lattice/label background is assumed), static bandwidth fields, b_min > 0 (no true horizon). The metric *on* the background is emergent; the background topology is input. Results are foothold-level: they establish emergence, the forced reach law, scale-cleanliness, and isotropy-emergence; they are not a derivation of the full field equations or a background-free proof.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| A metric emerges from bandwidth-connectivity (fit R² = 1.000) | **measured** | P1 |
| A bandwidth dip reads as *far* (curvature signature) | **measured** | P1, P4 |
| Ball-cut exponent = d−1 (holographic surface-count) | **measured** | P2 (0.984 in 2D, 2.008 in 3D) |
| Bandwidth = independent channels = boundary cut | I (reading of P04 + area law) | `Paper_AreaLawIsTheEdgeCount`, Paper_025 |
| Reach law p = 1/(d−1); g ~ 1/b in 3D, g ~ 1/b² in 2D | **derived** (conditional on the surface-count) | P2 |
| 3D uniquely reproduces GR-I | **derived** | P2 |
| Same 3 as the linking/order argument | I — structural convergence | MS-II §7; `ThreeDimensions_ConsolidatedReview` |
| No new length scale (R₀ drops out; unit = ℓ_P) | **measured / derived** | P3 |
| Isotropy emerges under coarse-graining (layer-1 → layer-2) | **measured** | P4 |
| Clean exponent off raw 3D paths | **not extractable — layer-2 object** | P4 (framed, not claimed) |
| Nonlinear / dynamical field equations | **OPEN** | not attempted |
| Background-free construction | **OPEN** | lattice/topology is input |

---

## 3. P1 — A metric emerges, and mass reads as far

On the 1D label line, with reach ∝ b^p and distance = hop-count, a clean metric comes out: the hop-distance fits ∫dx/b^q to R² = 1.000, so the emergent object is a genuine metric, not the trivial label-distance. And the bandwidth dip reads as *far*: hop-distance across the dip exceeds the flat-bandwidth reference by +87 (at p = ½) to +250 (at p = 1) hops. A depletion in bandwidth stretches distances. This is the curvature signature, obtained from connectivity alone with no geometry assumed. The emergent exponent tracks the connectivity law (q ≈ p, R² = 1.000 across the sweep), so the metric shape is a clean, controllable function of the reach law, which sets up the next question: what fixes the reach law.

---

## 4. P2 — The reach law is forced by the holographic channel-count, uniquely in 3D

The exponent p is not free. Read b as the number of independent relational channels a locus sustains (P04). For a locus reaching to radius R in a short-range d-dimensional substrate, the number of independent channels threading its neighborhood is the boundary **cut**: the edges crossing the ball's surface. For short-range edges that cut scales as the **surface**, R^{d−1}, not the volume R^d. This is ED's holographic bound (Paper_025) and the area-law-as-edge-count result (`Paper_AreaLawIsTheEdgeCount`). So a fixed channel budget b buys reach R ~ b^{1/(d−1)}, i.e. **p = 1/(d−1)**.

Both measurable links hold on real graphs:

| step | d = 2 | d = 3 |
|---|---|---|
| measured ball-cut exponent | 0.984 | 2.008 |
| expected d−1 | 1 | 2 |
| derived reach exponent p = 1/(cut) | 1.02 | **0.498** |
| emergent metric exponent q | 1.05 | **0.500** |
| emergent metric g ~ 1/b^{2q} | g ~ 1/b² | **g ~ 1/b (GR-I)** |
| fit R² | 1.000 | 1.000 |

The cut scales as the surface to within a percent, so the reach law is derived, not chosen. Feeding it back, the emergent metric is g ~ 1/b² in two dimensions and **g ~ 1/b, General Relativity's weak-field metric, in exactly three**. Three dimensions is the *unique* case where the holographic reach law reproduces GR-I. This is the same number the independent linking argument selects as the one dimension where a spatial link can hold committed order (MS-II §7). Two unrelated requirements, the emergent metric matching gravity and the topology holding order, single out three. That is internal coherence, not a fit; it is not a proof that ED forces 3D (both arguments inherit inputs), but two independent selections of the same value is what makes a reading trustworthy rather than tuned.

---

## 5. P3 — No new length scale: it is the Planck grain

The reach is R₀ · b^p in units of cells, and one cell is the Planck grain (P08). R₀ is the flat-space reach; it multiplies distance overall. Sweeping R₀ from 4 to 128 grains, the metric exponent is q = 0.500 to three figures throughout (R² = 1.000), and the physical curvature effect (excess distance relative to total) is R₀-invariant, the raw excess scaling as the pure unit 1/R₀. So R₀ carries no physics; it is only the hop-to-length conversion. The one length scale is therefore the ℓ_P grain already postulated, entering naturally as flat-space-reach = one grain, not a second tunable constant. Curvature-emergence is scale-clean: it introduces no new length. (It does not compute ℓ_P's numerical value, nor a specific physical length, which need the mass→b map and G.)

---

## 6. P4 — Isotropy emerges under coarse-graining, and the exponent is a layer-2 object

In a genuine 3D lattice with a spherical bandwidth dip, a metric emerges and curves as before, isotropically at the continuum level: binning by true radius, the per-shell coefficient of variation of hop-distance is small (0.06) and shrinks with radius. But isotropy is **not exact on the raw graph**. At matched radius, body-diagonal rays are farther in hops than axis rays (relative difference 0.13 to 0.35). The reach neighborhood on a cubic lattice is a polyhedron, not a sphere, so the raw shortest-path (a straight *ballistic* worldline through the reach-graph) is faceted and direction-dependent. Sweeping the reach from fine to coarse, the anisotropy falls monotonically to zero (axis/diagonal 0.345 → 0.000; shell CoV → 0.000): more reach directions round the ballistic ball toward the sphere.

This is the honest and instructive part. The raw BFS metric is a **layer-1** object in the two-layer coarse-graining picture (`Paper_Continuum_KineticLatticeGas`): ED's *direct* coarse-grain is transport, ballistic worldlines, non-Gaussian, faceted. The smooth, isotropic, single-exponent continuum metric is a **layer-2** object, reached only by coarse-graining (decorrelating, the "leaving ED" step). Read that way, the three P4 findings cohere:

- Isotropy emerging as the reach coarsens *is* a partial layer-1 → layer-2 coarse-graining. The probe exhibits the transition.
- The clean radial exponent g ~ 1/b *cannot* be read off the raw 3D paths, and it was not: cumulative fits are degenerate (exponent bouncing 0.6–1.6 with undiscriminating high R²), and the non-degenerate local-slope method is dominated by integer-BFS noise (R² 0.05–0.5). This is a layer mismatch, a layer-2 quantity measured on layer-1 ballistic paths, and it is *expected*, not a failure. A substrate that is non-Gaussian at layer 1 should not hand back a clean Gaussian exponent from raw transport.
- The clean exponent lives where its derivation put it: in the boundary-cut **count** of §4, which is combinatorial (channels ~ surface), not a transport measurement, and came out clean (cut exponents 0.984 and 2.008, R² = 1.000). That is why the count is clean and the ballistic transport is not.

So P4 confirms isotropy-emergence (a genuine addition: the emergent geometry is isotropic at layer 2, and the probe shows the layer-1 → layer-2 transition) and, correctly, does not offer a second exponent measurement. The lesson is general: to read continuum/Gaussian observables off raw ED, the coarse-graining step must be taken explicitly.

---

## 7. Falsification Criteria

- **F1:** If the boundary-cut exponent of a short-range d-dim lattice were *not* d−1 (e.g. if it scaled as the volume), the holographic reach law and its 3D-selects-GR-I conclusion would fail. (Measured d−1 to within a percent; a long-range-dominated substrate would break it, and is the honest boundary of validity.)
- **F2:** If, feeding the derived reach law into the emergent metric, 3D did *not* give g ~ 1/b (or 2D did), the claim that the holographic count reproduces GR-I uniquely in 3D would be wrong.
- **F3:** If the metric exponent depended on the reach normalization R₀, the "no new length scale" conclusion would fail and a second free constant would be present.
- **F4:** If, once the coarse-graining to layer 2 is done explicitly, the isotropic continuum metric did *not* converge to g ~ 1/b in 3D, the layer-1/layer-2 reading of P4 would be wrong and the exponent claim would need the transport route to also confirm it.
- **F5:** If a background-free construction (no assumed lattice/topology) failed to produce any metric, the emergence would be exposed as an artifact of the assumed background rather than of the connectivity.

---

## 8. Position Statement

In Event Density, a curved metric comes out of a graph that has no geometry in it. With bandwidth entering only through connectivity and distance read as hop-count, a metric emerges and a mass reads as far; the reach law that reproduces General Relativity's g ~ 1/b is not tuned but forced by ED's own holographic channel-count, and it reproduces GR-I in *exactly three dimensions*, the same number the independent linking argument selects; no new length scale is introduced, the one unit being the Planck grain already postulated; and in genuine 3D the emergent geometry is isotropic, appearing so only after coarse-graining, exactly as a non-Gaussian substrate should, with the clean metric exponent living in a combinatorial count rather than in raw ballistic transport. This is a foothold, tiered honestly: the reach law and its 3D selection are derived conditional on the holographic surface-count (an established ED result), the length scale is inherited, and the construction assumes a background. The static, linearized curvature-emergence bridge now stands on the primitives' own inputs. What remains is the nonlinear, dynamical regime (ED's own field equations) and a genuinely background-free construction. It is offered as a foothold on the emergent-geometry bridge and a structural convergence on three dimensions, not as a derivation of the Einstein field equations.
