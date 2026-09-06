# Individuation: ED's System/Environment Cut, Promoted from Concept to Construction

**Series:** Event Density (ED) Generative Papers — foundations arc
**Author:** Allen Proxmire
**Status:** Promotion draft, 2026-09-05. Elevates `primitives/concepts/individuation.md` (first-pass concept, 2026-04-24) to a tiered construction, on the finding that three arcs independently depend on it.
**Verdict per `Paper_095`:** **M3 — form-derived, value-inherited.** The construction is derivable from P02 + P03 + P04; the threshold `θ_ind` is inherited and undetermined.
**Anchors:** `Paper_087` (P02, P03, P04, P07, P11), `primitives/concepts/individuation.md`, `qft/Paper_024_LindbladLimit` (`P-Factorized-IC`).

---

## Preamble — What This Paper Does NOT Claim

1. **Individuation is not a fourteenth primitive.** The corpus is committed to thirteen. This paper shows the individuation functional is *constructible from* P02 + P03 + P04 and treats it as a derived structure. **Its historical header read "Primitive 10" because the concepts folder was an earlier primitive set, superseded when the canonical thirteen were fixed; that is provenance, not a competing claim.**
2. **The threshold `θ_ind` is not derived.** It is inherited, and the source concept flags it as open twice. Every quantity computed with it inherits an undetermined parameter.
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

### 2.1 One unstated bridge, flagged rather than assumed

**`w(e)` is an edge weight. P04 gives `b_K(u)` — a channel-at-locus weight. The corpus does not state the map between them.**

The natural reading is that `w(e)` for `e = (u,v)` aggregates the bandwidth of channels participated at **both** endpoints — the shared channels. **That is a plausible reading and it is not written anywhere.** It is the same class of gap as the `Str(C)` chain-level bridge (`foundations/Note_StrC_Bridge_2026-09-05.md`): an unstated aggregation between a per-channel primitive and a derived quantity that sums over it.

**Recorded as the paper's first open item, not repaired here.**

## 2.5 Load-Bearing Step Audit

| # | Step | Tier | Justification |
|---|---|---|---|
| 1 | Chain-complexes `S` exist as sub-structures of the participation graph | **D** | P02 |
| 2 | Edges and adjacency exist to partition | **D** | P03 |
| 3 | A non-negative additive scalar rides on them | **D** | P04 |
| 4 | `w(e)` from `b_K(u)` | **OPEN** | §2.1 — the map is unstated |
| 5 | Given `S`, every edge is internal or boundary, never both | **D** (set theory) | the partition is exhaustive and disjoint by construction |
| 6 | The ratio `b_int/b_bdry` is the individuation measure | **D-via-I** | form from steps 1–3; the *choice* of ratio rather than difference is a reading |
| 7 | `θ_ind` | **I (inherited)** | undetermined; flagged open twice in the source concept |
| 8 | Individuation is relational, not intrinsic | **D** | follows from `S`-dependence of both sums |
| 9 | Band disjointness follows | **D-via-I**, conditional on 4 and 7 | §4 |

**No `A` rows.** Step 4 is the honest weak point and step 7 is the honest inheritance.

## 3. Why the Partition Is Sharp Even Though Individuation Is Not

**These are two different things and conflating them is the trap.**

- **Given `S`, the edge partition is exact.** Every edge has both endpoints in `S`, exactly one, or none. There is no third case and no overlap. **This is set theory, not physics, and it is what the four-band classification needs.**
- **Whether `S` counts as a system is graded.** `b_int/b_bdry` is continuous; `θ_ind` is a threshold on a continuum. The source concept: *"Fully individuated (ratio → ∞) and fully non-individuated (ratio → 0) are limits; most real systems sit somewhere on the continuum."*

**So disjointness is free once `S` is fixed; what is not free is fixing `S`.** That is the whole content of the cut.

## 4. What This Licenses Downstream, and What It Costs

**Licenses.** The Adjacency/Environmental band distinction, which `foundations/Note_BandOverlap_Check_2026-09-05.md` showed cannot rest on P05/P11 alone — since decoherence is V5-mediated (`Paper_QuantumDarwinism_RecordBandwidth` §3) and V5's identity is conditional on P05 (`Paper_090`), so every Environmental channel is also a transporting channel. **Individuation separates them by which side of `S`'s boundary the far endpoint sits on.**

**Costs, and it is a real one.** **Band membership becomes relative to `S`.** `primitives/P04_bandwidth.md` states *"four mutually orthogonal substrate-level bands"* as absolute, and `soft-matter/Paper_UnifiedP04TransportBudget` §2 reads P04 as partitioning *"each locus's finite bandwidth `b(u)`"* — **with no `S` in it.** Under this paper there is no "the Adjacency band at a locus," only "with respect to `S`."

**Not fatal.** If the transport arc's `S` is its own cell, the reading is consistent. **But that identification is unstated and should be written.**

## 5. Falsification Criteria

- **`F-IND-1` (sharpest).** A system/environment split that is operationally sharp while its substrate boundary-bandwidth ratio is **not** extreme — i.e. a well-behaved system/environment cut with no correlate in `b_int/b_bdry`. That refutes the identification of the cut with this ratio, which is this paper's entire claim.
- **`F-IND-2`.** A demonstration that `θ_ind` must be regime-dependent in a way that cannot be absorbed into bandwidth normalization. That would make individuation a family of criteria rather than one, and every downstream use would need its own threshold.
- **`F-IND-3`.** A construction in which two chain-complexes are mutually individuated by the ratio while sharing unbounded correlation — which would sever individuation from the entanglement reading in §5.1 of the source concept.

## 6. Position Statement

ED sits in the substrate-ontology lineage ('t Hooft's cellular-automaton interpretation; causal-set program, Sorkin *et al.*), not the operational-reconstruction lineage (Hardy; Chiribella–D'Ariano–Perinotti; Coecke–Kissinger). **This paper does not reconstruct quantum theory from operational axioms; it identifies which substrate quantity plays the role that the system/environment cut plays elsewhere.**

**On whether ED improves on the standard situation — honestly: differently, not obviously better.** Standard treatments postulate a tensor factorization; `qft/Paper_024_LindbladLimit` does exactly this and names it (`P-Factorized-IC`). **This paper replaces a postulated factorization with a constructed ratio carrying a free threshold.** That is a gain in *kind* — the cut becomes a substrate quantity with measurable signatures rather than a choice of factor — and **not yet a gain in *determinacy***, because `θ_ind` is undetermined and the criterion is graded. **The corpus's other honest treatment (`P-Factorized-IC`) and this one should be read as two accounts of the same gap, not as one superseding the other.**

**End of Paper — Individuation.**

*Foundations arc. Promoted 2026-09-05 on the finding that the `Str(C)` bridge, the four-band classification, and the layer seam all reduce to it. Gravity ledger Staleness #86; source concept `primitives/concepts/individuation.md` retained as provenance.*
