# Individuation: ED's System/Environment Cut, Promoted from Concept to Construction

**Series:** Event Density (ED) Generative Papers — foundations arc
**Author:** Allen Proxmire
**Status:** Promotion draft, 2026-09-05. Elevates `primitives/concepts/individuation.md` (first-pass concept, 2026-04-24) to a tiered construction, on the finding that three arcs independently depend on it.
**Verdict per `Paper_095`:** **M3 — form-derived, value-inherited.** The construction is derivable from P02 + P03 + P04; the threshold `θ_ind` is inherited and undetermined.
**Anchors:** `Paper_087` (P02, P03, P04, P07, P11), `primitives/concepts/individuation.md`, `qft/Paper_024_LindbladLimit` (`P-Factorized-IC`).

---

## Preamble — What This Paper Does NOT Claim

1. **Individuation is not a fourteenth primitive.** The corpus is committed to thirteen. This paper shows the individuation functional is *constructible from* P02 + P03 + P04 and treats it as a derived structure. **Its historical header read "Primitive 10" because the concepts folder was an earlier primitive set, superseded when the canonical thirteen were fixed; that is provenance, not a competing claim.**
2. **The threshold `θ_ind` is not derived.** It is inherited, and the source concept flags it as open twice. Every quantity computed with it inherits an undetermined parameter. **§4.5 (2026-09-06) characterizes what KIND of quantity it is — a length, not a dimensionless constant — and closes the `ℏ`/bandwidth-normalization route. It still supplies no value, and the candidate `θ_ind = (ξ−1)/2 ≈ 0.4` named there rests on an identification nobody has argued for.**
3. **This paper does not solve the factorization problem.** It supplies a substrate-level *criterion* with a free scale, not a derivation of where the cut must fall. Whether ED improves on the standard situation is §6, and the honest answer is "differently, not obviously better."
4. **It does not claim individuation is sharp.** The source concept is explicit that the ratio is continuous and that "most real systems sit somewhere on the continuum." The sharp system/environment cut of textbook QM is a limit, not a fact.
5. **No new postulate is named.** Nothing here increments the corpus postulate census.

---

## Abstract

Three arcs — the gravity arc's chain-level `Str(C)` aggregation, the four-band classification of P04 bandwidth, and the layer-1/layer-2 coarse-graining seam — independently reduced to one question: **where does a chain end and the rest begin?** ED already answers it. For a chain-complex `S ⊂ V`, define internal and boundary bandwidth over the participation graph's edges and call `S` **individuated** when their ratio exceeds a threshold `θ_ind`. The construction is **form-derived** from P02 (chains), P03 (adjacency), and P04 (bandwidth); `θ_ind` is **inherited and undetermined**; verdict **M3**. Two consequences are load-bearing and are stated as such: the edge partition induced by `S` is **sharp and exhaustive**, which licenses the disjointness the four-band classification needs; and individuation is **relational, not intrinsic**, which makes band membership relative to a choice of `S` — contradicting how the bands are currently stated and used. Sharpest falsifier **`F-IND-1`**: a system/environment split with *no* substrate correlate in the boundary-bandwidth ratio.

---

## 1. Statement of Result

For a chain-complex `S ⊆ V` in the participation graph:

$$b_{\rm int}(S)=\!\!\!\sum_{e:\ \text{both endpoints}\in S}\!\!\! w(e),\qquad b_{\rm bdry}(S)=\!\!\!\sum_{e:\ \text{exactly one endpoint}\in S}\!\!\! w(e)$$

$$\boxed{\;S\ \text{is individuated}\iff \frac{b_{\rm int}(S)}{b_{\rm bdry}(S)}>\theta_{\rm ind}\;}$$

**What is form-derived:** the existence and shape of the ratio. **What is inherited:** `θ_ind`. **What is relational:** the whole thing — *"a chain-complex is individuated **with respect to** a specific environment."*

## 2. Primitive Inputs and Upstream Dependencies

- **P02 (participation).** Supplies chains and the four-tuple `(C,K,u,t)`; the objects being individuated are chain-complexes.
- **P03 (channel/locus indexing).** Supplies the locus index set and the graph adjacency over which edges are defined.
- **P04 (bandwidth).** Supplies the non-negative additive scalar the ratio is built from.
- **P07 (channel structure).** Channels internal to `S` support its identity; cross-boundary channels threaten it.
- **P11 (commitment).** Downstream: commitment events raise individuation.

### 2.1 The `w(e)` map — WRITTEN 2026-09-05, and the gap was a scheme-translation

**First, the diagnosis, which is better than "unstated".** The two schemes attach bandwidth to *different objects*:

- **The earlier primitive set** (now `primitives/concepts/`) put it on **edges**: `primitives/concepts/participation_bandwidth.md` — *"**Primitive 04 supplies edge weights** — a positive real number on each edge measuring bandwidth … `w: E → ℝ≥₀`"*, with `primitives/concepts/event_density.md` writing the graph as `G = (V, E, w)` with *"edge weights `w = b` (bandwidth)"*.
- **Canonical P04** puts it on **(channel, locus)**: `b_K(u,t) ∈ ℝ≥₀`.

**Individuation was written in the earlier scheme and never translated.** The map is missing because the schemes disagree about what bandwidth rides on — not because nobody thought about it.

**The map.** An edge carries what its two endpoints *share*:

$$\boxed{\;w(u,v)\;=\!\!\!\sum_{K\,\in\,\mathcal K(u)\cap\mathcal K(v)}\!\!\!\sqrt{b_K(u)\,b_K(v)}\;}$$

summing only over channels participated at **both** endpoints (P02's four-tuple supplies the membership).

**Five reasons, in decreasing strength.**

1. **Non-negative**, as P04 requires and as individuation's ratio needs.
2. **It is the amplitude product.** With `P_K = √b_K e^{iπ_K}`, `√(b_K(u)b_K(v)) = |P_K(u)|·|P_K(v)|`.
3. **It is the corpus's existing convention for two-locus shared content**, not a new choice: `P-Quadratic-Strain`'s cross term and `Paper_030`'s bilocal `√(b_loc·b_horizon)` are both this geometric mean, and `Paper_QuadraticStrain_v1` §2 argues the form is *forced* by the amplitude structure.
4. **It vanishes when a channel is not shared** — an edge carries nothing on channels only one endpoint participates in.
5. **Symmetric in `u,v`**, as an undirected edge weight must be.

**Verified against the source concept's own worked examples** (`internal notes/_check_edge_weight_map.py`, re-runnable): shielding raises the ratio and leakage lowers it; an entangled member is not individuated alone (`ratio = 0`) while the pair is jointly (`∞`); and **the same Cooper pair individuates in a normal metal (`∞`) and de-individuates in a superconductor (`1.00`) purely from gaining a shared condensate channel** — which is the concept's own illustration that individuation is relational. **The check discriminates**: a map summing all channels at both endpoints rather than only shared ones makes the metal and superconductor cases identical.

**The unification worth noting.** The phase-sensitive sibling of this quantity is `Coh`. On an edge, the Dirichlet cross-term is `2Σ_K √(b_K(u)b_K(v))\cosΔπ_K`, so

$$\big|\mathrm{Coh}_{(u,v)}\big| \;\le\; 2\,w(u,v),\qquad\text{with equality at full phase alignment.}$$

**`w(e)` is `Coh`'s envelope with the phase stripped** — the shared *capacity*, where `Coh` is the coherently shared part. Individuation asks how much is shared; `Coh` asks how much of it is in phase.

**The alternative, and why it is now excluded.** `min(b_K(u), b_K(v))` satisfies all five requirements above — a *bottleneck* reading rather than an amplitude-product one, and not a strawman, since the individuation ratio is a **cut** quantity and minimum-capacity is the canonical thing to put on a cut. It was recorded here as a live fork, with the geometric mean chosen by the corpus's convention rather than forced. **That fork is now closed, by a construction that does not reuse the evidence above** (`foundations/Note_EdgeWeight_Discriminator_2026-09-05.md`; check `internal notes/_check_edge_weight_discriminator.py`).

**Requirement (R), regridding consistency.** P03 supplies *the locus index set* — a bookkeeping choice. `b_bdry(S)` is supposed to be a property of **the cut**. So merging two loci on the **same side** of the cut must not move the boundary: `w(U,v) = w(u₁,v) + w(u₂,v)`. Loci merge by **amplitude addition** — `P_K(U) = P_K(u₁) + P_K(u₂)`, hence `b_K(U) = |ΣP|²` — which is `P-Motif-Algebra` (`Paper_007` §2, already in the census) and is the rule canonical `Paper_087` §P12 already computes `Coh` on.

**Then the weight is unique.** With `w = f(b_u,b_v)` non-decreasing in each argument, (R) at phase alignment reads `f((x₁+x₂)², b_v) = f(x₁², b_v) + f(x₂², b_v)` for amplitudes `x_i`. Setting `g(x) = f(x², b_v)` gives **Cauchy's functional equation** `g(x₁+x₂) = g(x₁)+g(x₂)` with `g` monotone, so `g(x) = c(b_v)x`; symmetry forces `c(b_v) = c√b_v`; `f(b,b) = b` fixes `c = 1`. **`f = √(b_u b_v)`, uniquely.**

**And it discriminates numerically.** Merging `N` phase-aligned loci, the geometric mean is exact for every `N` while `min` is wrong by a factor of `N` — it saturates at the outside locus and stops seeing the system side. Regridding **only the environment**, so `b_int` is untouched, **`min` flips the verdict** (ratio `1.50 → 6.00` across `θ_ind = 2`) while the geometric mean does not move (`0.75 → 0.75`). Scanning the power-mean family `M_p` from `min` (`p → −∞`) to the geometric mean (`p = 0`), all correctly normalized, the regridding violation has a **unique zero at `p = 0`**.

**The result worth keeping is that the fork was never independent: it was the merge rule in disguise.** Whatever rule governs coarse-graining loci fixes the edge weight, and fixes it uniquely.

**Checked the same day, and it revises the above.** (R) turns out **not** to be an invention of this argument: `Paper_073` (DCGT) §3.2's *well-definedness* clause already demands it — *"the average depends only on the coarse-graining center, **not on the specific substrate channels enumerated within the cell**"* — and DCGT is upstream of every continuum-level prediction in the corpus. **That strengthens the result.** But DCGT merges by **bandwidth** addition, not amplitude, and under that rule (R) forces the **product** `c·b_u b_v` instead. The two rules are one rule in two regimes (`b_K(U) = Σb + 2Σ√(b_ab_b)\cosΔπ`; random phase gives `Σb` in expectation, which is DCGT's), so **the edge weight is regime-dependent: geometric mean in the coherent regime, product in the decoherent one.** `min` is excluded under **both**, which was the live fork.

**Individuation sits in the coherent regime** — argued, not assumed, and *not* from the worked examples, which do not discriminate (every bandwidth in them is `0` or `1`, where the two weights agree). The argument is that the source concept's decisive example is a Cooper pair de-individuating on gaining a **condensate** channel and its account of entanglement is that a pair is **one un-individuated complex**: both are coherence statements, invisible at `Coh → 0`. **Individuation in the decoherent limit would not have the content the concept claims for it.**

**What is assumed:** (R) — now a standing corpus commitment rather than a new one; the reading of `P-Motif-Algebra` at loci rather than chains; and the coherent regime. Verdict **D-via-I conditional on (R) + `P-Motif-Algebra` + coherent regime**, not unconditional. Both notes: `foundations/Note_EdgeWeight_Discriminator_2026-09-05.md` §8, §8b.

## 2.5 Load-Bearing Step Audit

| # | Step | Tier | Justification |
|---|---|---|---|
| 1 | Chain-complexes `S` exist as sub-structures of the participation graph | **D** | P02 |
| 2 | Edges and adjacency exist to partition | **D** | P03 |
| 3 | A non-negative additive scalar rides on them | **D** | P04 |
| 4 | `w(e)` from `b_K(u)`: `w(u,v) = Σ_{K shared} √(b_K(u)b_K(v))` | **D-via-I** *(was OPEN; written and then closed 2026-09-05)* | §2.1. Form from P02 membership + P04. The **geometric mean rather than `min`** is no longer a convention: it is the **unique** edge weight under which `b_bdry` survives regridding, given that loci merge by amplitude addition (`P-Motif-Algebra`). Conditional on requirement (R) — which `Paper_073` §3.2 already demands — and on the **coherent** regime; under DCGT's decoherent merge rule the forced weight is the product instead, though `min` is excluded under both. Verified against all three of the source concept's worked examples, and against four discriminating tests. |
| 5 | Given `S`, every edge is internal or boundary, never both | **D** (set theory) | the partition is exhaustive and disjoint by construction |
| 6 | The ratio `b_int/b_bdry` is the individuation measure | **D-via-I** | form from steps 1–3; the *choice* of ratio rather than difference is a reading |
| 7 | `θ_ind` | **I (inherited)** | undetermined; flagged open twice in the source concept. **CHARACTERIZED 2026-09-06 (§4.5): still undetermined, but it is a LENGTH, not a dimensionless constant — `R = (a−1)/2` for a side-`a` hypercube in every dimension. The `ℏ`/bandwidth-normalization route is closed: `R` is invariant under `b → λb`.** **VALUE PROPOSED 2026-09-06 (§4.6): `θ_ind = 1`, `D-via-I` conditional on `P-Factorized-IC`'s domain and on `ξ < 2`; two independent routes, falsifiable by tightening `ξ`.** |
| 8 | Individuation is relational, not intrinsic | **D** | follows from `S`-dependence of both sums |
| 9 | Band disjointness follows | **D-via-I**, conditional on 4 and 7 | §4 |

**No `A` rows.** **Step 4 was the paper's open item, is now written, and its one remaining choice — geometric mean versus `min` — is now closed rather than preferred (§2.1). Step 7 (`θ_ind`) is the honest inheritance and remains the one undetermined quantity in the paper.**

## 3. Why the Partition Is Sharp Even Though Individuation Is Not

**These are two different things and conflating them is the trap.**

- **Given `S`, the edge partition is exact.** Every edge has both endpoints in `S`, exactly one, or none. There is no third case and no overlap. **This is set theory, not physics, and it is what the four-band classification needs.**
- **Whether `S` counts as a system is graded.** `b_int/b_bdry` is continuous; `θ_ind` is a threshold on a continuum. The source concept: *"Fully individuated (ratio → ∞) and fully non-individuated (ratio → 0) are limits; most real systems sit somewhere on the continuum."*

**So disjointness is free once `S` is fixed; what is not free is fixing `S`.** That is the whole content of the cut.

## 4. What This Licenses Downstream, and What It Costs

**Licenses.** The Adjacency/Environmental band distinction, which `foundations/Note_BandOverlap_Check_2026-09-05.md` showed cannot rest on P05/P11 alone — since decoherence is V5-mediated (`Paper_QuantumDarwinism_RecordBandwidth` §3) and V5's identity is conditional on P05 (`Paper_090`), so every Environmental channel is also a transporting channel. **Individuation separates them by which side of `S`'s boundary the far endpoint sits on.**

**Costs, and it is a real one.** **Band membership becomes relative to `S`.** `primitives/P04_bandwidth.md` states *"four mutually orthogonal substrate-level bands"* as absolute, and `soft-matter/Paper_UnifiedP04TransportBudget` §2 reads P04 as partitioning *"each locus's finite bandwidth `b(u)`"* — **with no `S` in it.** Under this paper there is no "the Adjacency band at a locus," only "with respect to `S`."

**Not fatal.** If the transport arc's `S` is its own cell, the reading is consistent. **But that identification is unstated and should be written.**

## 4.5 What kind of quantity `θ_ind` is — CHARACTERIZED 2026-09-06

`θ_ind` is still **undetermined**, and nothing below supplies a value. What changed is that it is no
longer an unknown *dimensionless constant*. Four results, each analytic and each confirmed numerically
(`../event-density/theory/individuation_theta_probe.py`):

**(A) The `ℏ` / bandwidth-normalization route is CLOSED.** `b_int` and `b_bdry` are both homogeneous of
degree 1 in the edge weights, so `R` is invariant under `b → λb`. Measured: `λ = 1000` moves `b_int` from
`60.0` to `60000.0` and leaves `R = 2.500000`. **So no bandwidth normalization and no value of `ℏ` can
supply `θ_ind` — there is nothing for a scale to attach to.** One of the source concept's three named
routes, closed.

**(B) Individuation is closed under union, for EVERY `θ`.** `I_S > θB_S` and `I_T > θB_T` give
`I_S + I_T > θ(B_S + B_T)`, and any edges *between* `S` and `T` move from boundary to internal, which only
raises the ratio. Measured: 0 violations in 400 random pairs, disjoint, adjacent and overlapping.
**So no choice of `θ_ind` makes this an object-COUNT criterion — two separate individuated systems always
union to an individuated one. It is a cohesion filter, not a “this is one thing” test**, and the family of
admissible `S` is upward-closed. Something other than the criterion must choose `S`; the criterion only
checks it. **§4's licence to the four-band classification is unaffected — that licence is the sharpness of
the edge partition (§3), not object-counting — but the bands' relativity to `S` is now sharper: `S` is
selected, not found.**

**(C) `R` is a LINEAR EXTENT, dimension-independently.** For a hypercube of side `a` on a hypercubic
lattice with unit weights, in any dimension `d`:

$$b_{\rm int} = d\,a^{d-1}(a-1),\qquad b_{\rm bdry} = 2d\,a^{d-1},\qquad \boxed{R = \tfrac{a-1}{2}}$$

The `d` and the `a^{d-1}` cancel. Confirmed exactly for `d = 1, 2, 3`; it survives 60% bandwidth disorder
(deviations −7.6% to +6.9% over five seeds) and real committed morphology on the certified rule
(`R/(√|S|/2)` stays in `0.56–0.67` from `|S| = 4` to `200`). **So `R > θ_ind` reads `linear extent >
2θ_ind + 1` loci: `θ_ind` is a LENGTH wearing a dimensionless costume.** Two boundary values follow: a
**single locus has `R = 0`** (one thing alone is not individuated at all), and the **minimal composite —
two loci sharing an edge — gives `R = 1/2` exactly, in every dimension.**

**(D) — but only where the substrate HAS geometry.** On a geometric graph the cut scales like a surface and
the interior like a volume. On an **expander** the Cheeger constant is bounded below, the cut grows *with*
the volume, and `R` stays `O(1)` however large `S` gets. Measured on a degree-4 lattice against a degree-4
random regular graph, `|S| = 4 → 256`: lattice `R` runs `0.50 → 7.50`, expander `R` runs `0.30 → 0.56`.
**ED's metric locality is EMERGENT, not primitive, so `θ_ind`'s CHARACTER changes across that transition:
a length threshold in the geometric regime, a genuinely dimensionless cohesion threshold before it.**

**What this does to `F-IND-2`, stated carefully.** (A) shows bandwidth normalization can absorb nothing at
all, so the escape route in `F-IND-2`'s own wording is unavailable; (C)/(D) show `θ_ind` is a length in the
geometric regime and not one before it. **This is NOT `F-IND-2` fired and must not be banked as one.** The
falsifier asks whether physics *needs* more than one threshold; this shows only that a fixed `θ_ind` **is**
a fixed length, so two regimes with different characteristic lengths would need different `θ_ind`.
**Whether ED has two such regimes in a load-bearing way is not shown.** `F-IND-2` moves from hypothetical
to concrete and testable, no further.

**What would now determine it.** Not a bandwidth calibration and not a measurement of `ℏ`, but **the
length at which system/environment cuts become sharp, in units of `ℓ_ED`.** Two routes were named:
**(1)** the scale at which `qft/Paper_024_LindbladLimit`'s postulated factorization (`P-Factorized-IC`)
becomes accurate — the same gap approached from the other side, as §6 already says; **(2)** an arithmetic
reading off the measured `ξ_canonical ≈ 1.8 ± 0.3 lu` giving `θ_ind = (ξ−1)/2 ≈ 0.4`, flagged at the time
as *“an identification nobody has argued for”*.

> **⚠ ROUTE (1) WAS WORKED THE SAME DAY (§4.6) AND IT REFUTES (2).** The `≈ 0.4` reading identified `θ_ind`'s
> length with `ξ` directly; **the boundary shell must be crossed on BOTH sides before an interior exists**,
> so the required linear extent is `2ξ`, not `ξ`. It also landed *below* the minimal-pair value `1/2`,
> which would individuate every connected pair and make the criterion vacuous — that should have been
> the tell. **The flag was right; the number was wrong.**

`foundations/Note_ThetaInd_IsALength_2026-09-06.md`; gravity ledger #128.

### 4.6 The decoherence route worked — `θ_ind = 1`, conditional on `ξ < 2`. 2026-09-06

**The two accounts are the same QUANTITY, not just the same gap.** §6 says this paper and
`qft/Paper_024_LindbladLimit`'s `P-Factorized-IC` *“should be read as two accounts of the same gap”*.
They are stronger than that. `P-Factorized-IC` asserts `ρ_tot(0) = ρ_S(0) ⊗ ρ_E(0)` — **no
system–environment correlation** — and in ED that correlation is carried by cross-boundary shared
channels: V5 **is** the cross-chain correlation kernel (`Paper_090`), and `b_bdry(S)` is exactly the
shared-channel content across the cut. So **exact factorization ⇺ `b_bdry(S) = 0` ⇺ `R(S) = ∞`:
`P-Factorized-IC` IS individuation at `θ_ind = ∞`.** **Which shows at once that it cannot fix a finite
threshold by itself — as an exact postulate it names only the limit.** What fixes a finite value is its
**domain of validity**.

**And depth is QUANTIZED, which is what makes the answer sharp.** Correlations decay with the substrate
correlation length `ξ`, so a locus at depth `d` from `S`'s boundary is still correlated with the outside
when `d < ξ`. If every locus of `S` is within `ξ` of the boundary then **`S` is all boundary layer, has no
interior, and factorization has NOWHERE TO BE ACCURATE** — not “is inaccurate”. Depth is counted in loci,
hence an integer, so the condition is `⌈a/2⌉ > ξ`, and with `R = (a−1)/2` from §4.5(C) the threshold is a
**step function of `ξ`**:

| `ξ` range | smallest `a` with an interior | `θ_ind` |
|---|---|---|
| `0 < ξ ≤ 1` | 2 | 0.5 |
| **`1 < ξ ≤ 2`** | **3** | **1.0** ← measured `ξ ≈ 1.83` |
| `2 < ξ ≤ 3` | 5 | 2.0 |

> **`θ_ind = 1`, and it does NOT inherit `ξ`'s uncertainty — only the question of which integer bracket
> `ξ` falls in.**

**A second route reaches the same value using no `ξ` at all:** the smallest square containing a locus not
on its own boundary is `a = 3`, giving `R = 1`. **Two independent routes, one value.**

**The sensitivity, stated plainly.** This needs `ξ < 2`. The corpus value `ξ = 1.8 ± 0.3` (`Paper_096`,
GR-SC 1.7 half-decay, 10 seeds) puts that boundary about **0.6σ away — roughly a one-in-four chance the
bracket is wrong**, and `ξ > 2` would give `θ_ind = 2`. **So this is sharp and falsifiable: tighten `ξ`
and the answer is decided.** *(The probe's own 5-seed estimate is `1.831 ± 0.043`, but by a DIFFERENT
estimator — 1/e crossing of the phase autocorrelation — so it is not a tightening of the corpus value
and is not quoted as one.)*

**Tier.** The identification is **argued**; the value is **`D-via-I` conditional on `P-Factorized-IC`'s
domain and on `ξ < 2`**. **It is NOT derived from the 13 primitives, and `F-IND-2` is still not fired.**

**One measured observation against `Paper_024`.** The cross-boundary correlation fraction does not become
small at any accessible region size — at `R = 9.5` (a 20×20 region) about **11%** of near-range
correlation mass still crosses the boundary. **The Born–Markov regime `Paper_024` postulates is a genuine
idealisation on this substrate, not an asymptotically-approached one.** Consistent with that paper, which
declares the regime rather than deriving it — but worth having measured.

`foundations/Note_ThetaInd_DecoherenceRoute_2026-09-06.md`; gravity ledger #129.

## 5. Falsification Criteria

- **`F-IND-1` (sharpest).** A system/environment split that is operationally sharp while its substrate boundary-bandwidth ratio is **not** extreme — i.e. a well-behaved system/environment cut with no correlate in `b_int/b_bdry`. That refutes the identification of the cut with this ratio, which is this paper's entire claim.
- **`F-IND-2`.** A demonstration that `θ_ind` must be regime-dependent in a way that cannot be absorbed into bandwidth normalization. That would make individuation a family of criteria rather than one, and every downstream use would need its own threshold.
- **`F-IND-3`.** A construction in which two chain-complexes are mutually individuated by the ratio while sharing unbounded correlation — which would sever individuation from the entanglement reading in §5.1 of the source concept.

## 6. Position Statement

ED sits in the substrate-ontology lineage ('t Hooft's cellular-automaton interpretation; causal-set program, Sorkin *et al.*), not the operational-reconstruction lineage (Hardy; Chiribella–D'Ariano–Perinotti; Coecke–Kissinger). **This paper does not reconstruct quantum theory from operational axioms; it identifies which substrate quantity plays the role that the system/environment cut plays elsewhere.**

**On whether ED improves on the standard situation — honestly: differently, not obviously better.** Standard treatments postulate a tensor factorization; `qft/Paper_024_LindbladLimit` does exactly this and names it (`P-Factorized-IC`). **This paper replaces a postulated factorization with a constructed ratio carrying a free threshold.** That is a gain in *kind* — the cut becomes a substrate quantity with measurable signatures rather than a choice of factor — and **not yet a gain in *determinacy***, because `θ_ind` is undetermined and the criterion is graded. **The corpus's other honest treatment (`P-Factorized-IC`) and this one should be read as two accounts of the same gap, not as one superseding the other.**

**End of Paper — Individuation.**

*Foundations arc. Promoted 2026-09-05 on the finding that the `Str(C)` bridge, the four-band classification, and the layer seam all reduce to it. Gravity ledger Staleness #86; source concept `primitives/concepts/individuation.md` retained as provenance.*
