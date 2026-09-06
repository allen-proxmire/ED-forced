# Branch 3: the bands are **channel classes**, not a decomposition of a scalar — and that resolves the conflict while shrinking the postulate

*Foundations working note, 2026-09-05 (late). Works the third branch of `Note_FourBand_Conflict_Reopened_2026-09-05.md`. **Result: mostly yes, and the residue is smaller and more honest than either side of the conflict.***

---

## Verdict

**The card locates the bands in the wrong primitive.** They are not a decomposition of one channel's scalar `b_K`; they are a **classification of the channel index set `𝒦(u)`**, licensed by P07 and P10, with the **band totals then given free by P04's additivity** — which is stated over *disjoint sub-channels*, exactly what a class partition of `𝒦` provides.

$$b_{\text{band}}(u)=\!\!\sum_{K\in\text{band}(u)}\!\! b_K(u)\qquad\text{by P04, given a disjoint classification of }\mathcal K(u).$$

**Both documents come out mostly right.** `Paper_087` §P04 is correct that P04 is the scalar plus additivity and nothing more. The card is correct that a four-band structure exists in ED. **The card's error is one preposition: the bands are not *in* P04, they are *summed by* it.**

**What Branch 3 does not deliver** — and these are the honest residue — **is four-ness, exhaustiveness, disjointness, and a per-locus bound.** §3.

---

## 1. Each class has a licensing primitive

- **P07** makes channels *"structurally distinguishable carriers with **intrinsic identities**"*, distinct *"even if their bandwidth and polarity content happen to coincide."* **So a classification of `𝒦` is a substrate-level fact rather than an observer's bookkeeping.** This is what makes the whole move legitimate.
- **P10** makes rule-type *"a primitive label with its own participation measure / kernel content."* **Classifying channels by rule-type therefore reads a label the substrate already carries; it does not add one.**
- **P05** — polarity transport along edges — distinguishes the channels that carry content between loci: the **Adjacency** class.
- **P11** — commitment events, *"with the un-selected channels' phase content randomized"* — names both the budget consumed by commitment (**Commitment-reserve**) and a class of channels that are phase-randomized (**Environmental**).
- The remainder — a channel's own coherent content, not transporting, not randomized, not reserved — is **Internal**.

**Every band has a primitive behind it. None of them is P04.**

## 2. Why this dissolves the conflict rather than picking a winner

The card's claim was *"bandwidth **further decomposes** into four mutually orthogonal substrate-level bands"* — a statement about `b_K`. **Canonical P04 has no such decomposition, which is why the flag was raised.**

Under Branch 3 the true statement is different in type: **the channel set partitions, and bandwidth sums over the parts.** That needs no amendment to `Paper_087`, no appeal to an archived paper, and it leaves `Paper_087` §P04's text exactly as written.

**It also explains the whole two-day flip.** The card, the archived `paper_M2`, and my #57 withdrawal were all defending something real — the bands exist and are used across four arcs — while stating it in a form canonical P04 contradicts. **The disagreement was about location, not existence.**

## 3. What is still a postulate, and it is much smaller than "P04 has four bands"

**Four things do not follow, and naming them precisely is the point of this note.**

1. **Four-ness.** P10 says *"multiple structurally distinct rule-types"* and lists **three** — matter, gauge, kernel — which is a **different trichotomy** from the four bands. **Nothing derives the number four.**
2. **Exhaustiveness.** That every channel falls into one of these classes is not licensed by anything.
3. **Disjointness, and this is the one that bites.** **A channel can both transport polarity (P05) and have its phase randomized at commitment (P11).** Nothing forbids a channel being in Adjacency *and* Environmental. **And if the classes overlap, P04's additivity no longer gives the band totals — the sums double-count.** So the free ride in §0 is conditional on disjointness, which must be assumed.
4. **A per-locus bound.** **Canonical P04 gives non-negativity, not an upper bound.** `soft-matter/Paper_UnifiedP04TransportBudget` §2 says *"its per-cell capacity `b_adj^max` is finite (a fixed fraction of the **finite** `b(u)`)"* — **but P04 does not make `b(u)` finite.** Compare `entanglement/Paper_065_Monogamy`, which does this correctly: its finite budget comes from **`P-V5-Budget` + `I-V5`** (V5's finite total weight per chain, *inherited* from `Paper_090`) **+ P04 additivity**, each named. **The entanglement arc names its budget postulate; the transport arc assumes P04 supplies one.**

**So the honest postulate is: the four classes are disjoint and exhaustive over `𝒦(u)`, and `b(u)` is bounded.** That is nameable, tierable, and far weaker than granting P04 a partition it does not have.

## 4. One circularity the card would have to give up

The card also claims *"the four-band partition (P04 §1.5) **supplies the sesquilinear inner-product structure** on the participation manifold (Paper 003)."*

**Branch 3 cannot deliver that, and the two claims cannot both stand.** Branch 3 *derives* the bands from P05/P07/P10/P11; it cannot then have the bands *found* the inner product those primitives are stated in. **Either the bands are derived (Branch 3) or they are foundational (the card's Paper 003 claim), not both.** Whether `Paper_003` actually needs the partition, or only needs P07 distinguishability plus P04 additivity, is unchecked and is the cheapest next thing to look at.

## 5. What each arc gets

- **Soft-matter transport.** **Survives, and its own flag predicted this**: *"the shared-budget identification may well survive on P04 additivity plus P05-as-sole-transport without needing four *named* bands, which would be a re-grounding rather than a retraction."* **Branch 3 is that re-grounding.** The Adjacency band becomes *the class of P05-transporting channels at a locus*, and `F-COONSET` keeps its referent. **Cost:** the arc must adopt the disjointness and boundedness postulate explicitly, as the entanglement arc does.
- **Higgs / dwell.** The July retraction said the dwell argument *"hung on P04 carrying a four-band partition … not in the canonical primitive."* **Under Branch 3 that objection is answered on its own terms** — the partition is not in P04 and never needed to be. **But the retraction also flagged a second defect, that the argument borrowed P12's `∇_adj` to interpret a P04 band, and Branch 3 does not touch that.** So the dwell route is *unblocked at the sourcing level and still owes its second repair.*

---

## Recommendation, offered as one

**Adopt Branch 3, name the residue, and fix the card rather than `Paper_087`.** The card's canonical statement should say the classification is over `𝒦` and licensed by P07/P10, with the band totals following from P04 additivity **given** disjointness and a bound — both named as what they are. **`Paper_087` §P04 needs no change, which is the strongest argument for this branch: it is the only one where the authoritative primitives paper turns out to have been right all along.**

*Not applied. Gravity ledger Staleness #83; reopens #57 with a third option.*
