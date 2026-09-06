# P04 — Bandwidth (non-negative additive scalar)

> **✅ RESOLVED 2026-09-05 by AP's decision — BRANCH 3 ADOPTED. The bands are not *in* P04; they are a classification of the channel index set $\mathcal{K}$`(u)`, *summed by* P04.** The two-day conflict between this card and canonical `Paper_087` §P04 was **about location, not existence**. Both documents were mostly right: `Paper_087` is right that P04 is the scalar plus additivity and nothing more; this card was right that a four-band structure exists in ED. **The card's error was one preposition.** Each class has its own licensing primitive — **P07** (channels are *“structurally distinguishable carriers with intrinsic identities”*, so a classification of $\mathcal{K}$ is a substrate fact rather than bookkeeping), **P10** (rule-type is *“a primitive label”*, so classifying by it reads a label the substrate already carries), **P05** (the transporting channels: Adjacency), **P11** (the phase-randomized ones and the commitment budget: Environmental, Commitment-reserve) — **and none of them is P04.** The band *totals* then follow free from P04's additivity, which is stated over **disjoint sub-channels**, exactly what a class partition of $\mathcal{K}$ supplies. **`Paper_087` §P04 therefore needs no change, which is the strongest thing about this branch: the authoritative primitives paper turns out to have been right all along.** Title and §“Canonical statement” amended below; the residue is named as **`P-Band-Partition`**. `foundations/Note_FourBand_Branch3_2026-09-05.md`; gravity ledger #93, closing #56/#57/#82–#85. *Both superseded flags kept below as the audit trail.*

> **⚠ SUPERSEDED 2026-09-05 by the banner above.** ✅ CONFLICT FLAG WITHDRAWN 2026-09-04 — this card is CORRECT.** The four-band partition is canonical primitive-level content: `paper_M2`'s abstract records ED as *“committed at the primitive level to a four-band partition of bandwidth (P04 §1.5)”*, and the M-series archive removed the **forcing argument**, not the partition. `ARCHIVED_M_SERIES_NOTICE.md` explicitly retains *“The Forcing Papers (#1–#19)”*. **What is genuinely worth fixing is upstream:** canonical `Paper_087` §P04 gives only the summary (*“bandwidth as non-negative additive scalar”*) and does **not** reference §1.5's partition, which is what made this card look like it disagreed. See gravity ledger Staleness #57. *Superseded flag kept below as the audit trail.* **Original flag:** This card's title and §1.5 assert a **four-band partition** as part of P04. **Canonical `Paper_087` does not**: it defines P04 as *“Bandwidth as non-negative additive scalar”*, and `Foundations_TieredClaims_Ledger.md` staleness #2 records four-band as **archived M-series** content — *“canonical 087 has no four-band”* — having repointed two `Paper_089` citations away from it on 2026-07-29. **The corpus's standing rule is that canonical 087 wins.** By that rule this card overstates P04. **But the four-band vocabulary is used in 10+ papers across four arcs**, including the GR quartet and `Paper_027`, so the disagreement is widespread rather than local and **is not resolved here**: settling it means deciding what P04 *is*, which is a primitive-definition question. **What is established is that the card and the canonical paper cannot both be right.** Gravity ledger Staleness #56.

> **⚠ Vocabulary hazard — read `ADJACENCY_AND_BAND_DISAMBIGUATION.md` before building on any sentence containing “adjacency” or “band”.** **“Adjacency” names four different *kinds of object*** in the corpus — the participation graph's edge **structure** (P03); the Adjacency **class of channels** (P04 card); the position-locus **content sector**, which is boost-*invariant* (`Paper_012_7`); and P12's adjoint-gradient **operator** `∇_adj`. **“Band” names three different partitions**, two of them four-fold and neither containing the other. **Four collisions were found in one session and one had a live argument built on it for two months** (the dwell route). Gravity ledger #91, #92, #94, #95.

**Canonical primitive of the ED Generative System.**
**Position paper reference:** `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1.3.

---

## Canonical statement

Each channel $K$ at each locus $u$ carries a real-valued non-negative quantity $b_K(u) \geq 0$, additive under channel decomposition. **That is P04, and it is all of P04** — matching canonical `Paper_087` §P04 exactly.

### The four bands, correctly located (amended 2026-09-05, Branch 3)

**The bands are a classification of the channel index set $\mathcal{K}(u)$, not a decomposition of the scalar $b_K$.** Each class is licensed by a primitive other than P04:

| band | the channels in it | licensed by |
|---|---|---|
| **Internal** | a channel's own coherent content — not transporting, not randomized, not reserved | the remainder |
| **Adjacency** | channels carrying content between loci | **P05** polarity-transport |
| **Environmental** | channels whose phase content is randomized | **P11** commitment |
| **Commitment-reserve** | the budget consumed by commitment events | **P11** |

**What makes the classification a substrate fact rather than an observer's bookkeeping is P07** — channels are *“structurally distinguishable carriers with **intrinsic identities**”*, distinct *“even if their bandwidth and polarity content happen to coincide”* — **and P10**, which makes rule-type *“a primitive label with its own participation measure”*, so classifying by it **reads a label the substrate already carries rather than adding one.**

**The band totals then come free from P04**, whose additivity is stated over *disjoint sub-channels* — exactly what a class partition of $\mathcal{K}(u)$ provides:

$$b_{\text{band}}(u)=\!\!\sum_{K\,\in\,\text{band}(u)}\!\! b_K(u)\qquad\text{given a disjoint classification of }\mathcal{K}(u).$$

### `P-Band-Partition` — the residue, named rather than assumed

**Four things do not follow from the primitives above, and the honest move is to name them once:**

> **`P-Band-Partition`:** *the four channel classes are **disjoint** and **exhaustive** over $\mathcal{K}(u)$.*

- **Four-ness is not derived.** P10 speaks of *“multiple structurally distinct rule-types”* and lists **three** — matter, gauge, kernel — a **different trichotomy** from these four bands. Nothing in the corpus derives the number four.
- **Exhaustiveness is not licensed** by anything above.
- **Disjointness is the clause that bites.** **A channel can both transport polarity (P05) and have its phase randomized at commitment (P11)**, so nothing yet forbids a channel sitting in Adjacency *and* Environmental — and **if the classes overlap, P04's additivity no longer gives the band totals, because the sums double-count.** `foundations/Note_BandOverlap_Check_2026-09-05.md` found they *do* overlap on P05/P11 alone; **what separates them is individuation** — which side of a chain-complex's boundary the far endpoint sits on (`foundations/Paper_Individuation_TheSystemEnvironmentCut.md` §5). **So `P-Band-Partition` is discharged *relative to a choice of system `S`*, and the bands are consequently relational, not intrinsic.**
- **A per-locus bound is a separate matter and does not belong here.** **Canonical P04 gives non-negativity, not an upper bound**, so any arc needing a finite per-locus budget must name one — see `P-Locus-Bandwidth-Bound` in `soft-matter/Paper_UnifiedP04TransportBudget` §5, and compare `entanglement/Paper_065_Monogamy`, which does this correctly via `P-V5-Budget` + `I-V5`.

**This is far weaker than granting P04 a partition it does not have, and it is nameable, tierable and attackable, which the old form was not.**

~~The four-band partition (P04 §1.5) supplies the sesquilinear inner-product structure on the participation manifold (Paper 003).~~

> **⚠ This dependency claim is FALSE, checked 2026-09-05 (gravity ledger #91).** **`Paper_003` does not need the partition and is *insensitive* to it.** Its §2.5 audit table traces every load-bearing step and no row cites the partition; structurally, its only use of bandwidth is the normalized sum $\sum_{K'}b_{K'}$, and **any partition of the channel set leaves that sum unchanged.** What supplies the inner-product structure is **channel orthogonality** — distinct channels being orthogonal, so $\lVert\Psi\rVert^2=\sum_K b_K$ carries no cross term (`Paper_007` §3.2) — tracked as `P-Channel-Orthogonality` and **unrelated to how the channel set is partitioned into bands.** `foundations/Note_Paper003_FourBand_Check_2026-09-05.md`.
>
> **Two further cautions on this card, same date** (`foundations/Note_FourBand_Senses_2026-09-05.md`; `internal notes/_check_fourband_senses.py`). **(a) The term “four-band” is overloaded across the corpus** — at least four distinct things carry it: this partition; `Paper_012_6_Heisenberg`'s **`P-FourBand`** (position/momentum/time/energy, a *separate named censused postulate* with its substrate derivation open); `Paper_004_5_Tsirelson_Discrete` §3.6's **Bell-test settings** `{a,a',b,b'}`, which are not a bandwidth partition at all; and `Paper_003_5`'s **“adjacency-bandwidth”**, meaning bandwidth along graph adjacency. **A grep for “four-band” therefore overstates this partition's footprint by roughly a factor of three.** **(b) This card tiers the partition more strongly than its own source concept does** — `concepts/participation_bandwidth.md` says *“The four-band structure is **motivated empirically**”* and lists *“whether it is mathematically forced”* as an open question, twice. **Exactly one genuine paper-level dependent survives the audit:** `soft-matter/Paper_UnifiedP04TransportBudget`, which already declares the dependency a posit and calls it *“the load-bearing joint … the single most important thing to attack.”*

## Audit verdict

LOAD-BEARING. Bandwidth supplies the magnitude side of the complex polar participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ (Paper 001), the Born-rule probability weights $\text{Prob}(K \mid u) = b_K/\sum b_{K'}$ (Paper 002), and the Tsirelson-bound saturation via orthogonal-band algebra (Paper 003).

## Underlying concept treatments

- `concepts/participation_bandwidth.md` — the graded scalar measure of participation; turns the relational fact (P02) into something with quantity.
