# The two normalizations are over different index sets — the link is an analogy, and #114 over-reached

**Date:** 2026-09-06
**Status:** **Answered by reading**, and it corrects the item written one step earlier.

---

## 1. The question

#114 found that ED's commitment rule is already normalized — `P-LinRate`'s `Pr ∝ b_{K*}/Σ_{K'} b_{K'}` — and called this *"the strongest thing supporting #111,"* on the reading that intensive selection is what the corpus prescribes. **It also flagged the gap: `P-LinRate` normalizes over the channel set, the probe over the coordination number, and nothing identifies them.**

**The gap does not close. It is structural.**

## 2. The two sets, from the sources

**The probe's candidate set is loci.** `simulator/sigma.py`:

> `def compute_candidates(u, state, graph): """Admissible next-states from u: non-decoupled neighbors (reach-bounded)."""` → `return graph.admissible_neighbors(u)`

**`P-LinRate`'s set is channels.** `Paper_003` §2: `Pr(commit to K*) ∝ b_{K*}/Σ_{K'} b_{K'}` — the sum runs over channels `K'`.

**And canonical P03 keeps them apart, explicitly:**

> The substrate carries **discrete index sets**: a **channel index set** `𝒦` … and a **locus index set** indexed by substrate-graph positions `u`.

**Two index sets, named separately in the primitive that supplies them.** So the probe normalizes over neighbouring *loci* and `P-LinRate` normalizes over *channels at a locus*. **Different objects.**

## 3. And they cannot be identified, for a reason that matters

The natural bridge is Branch 3's: **the Adjacency class is the set of P05-transporting channels**, and P05 transports **along edges** — so Adjacency-class channels are edge-associated, and one might hope for a bijection between them and the admissible neighbours.

**It fails, and the reason is load-bearing elsewhere.** `Paper_MS-I` §3 derives **the gauge group `SU(N)` from channel multiplicity** — `N` channels at a locus, with the connection transporting all of them along each edge. **A bijection between channels and edges would force `N = 1` per edge and collapse `SU(N)` to `U(1)`.**

> **The two sets have different sizes, and identifying them would cost ED its gauge structure.**

The candidate set's size is the admissible-neighbour count (≈ 4 on the probe's lattice). The channel set's size is `N`, the gauge multiplicity. **These are unrelated numbers.**

## 4. So #114 over-reached, and here is the correction

**What #114 claimed:** *"intensive selection is what the corpus already commits to"*, and that `P-LinRate` makes it **the corpus-consistent reading** — *"the strongest thing supporting #111."*

**What survives:** **both rules are normalized.** In the one place the corpus specifies a commitment-selection rule, that rule is a **probability over its candidate set**, not a raw score. **That is a real parallel and it is worth noting** — the simulator's argmax-over-raw-`Σ` remains an outlier against the corpus's only stated selection rule.

**What does not survive:** that `P-LinRate` **prescribes** the probe's normalization. **It does not, because it normalizes over a different set.** The convention that makes `Grad` bind — dividing by the coordination number — has **no derivation from `P-LinRate`**, and calling it "corpus-consistent" overstated a structural analogy as a structural implication.

**Correct label: an ANALOGY between two normalized rules over different index sets.** Suggestive, not derivational.

## 5. What this does to support (7)

**Nothing, and that is the point.** Support (7) — that `Grad`'s phase half is the term that binds — is **empirical**: measured on the probe, `+81%` reach at matched connection, with canonical `Coh` unable to match it under any normalization tried. **It rests on the measurement and never rested on `P-LinRate`.**

**What loses standing is #114's claim that the convention is structurally motivated.** It is currently a **scoring choice that works**, with a suggestive parallel elsewhere in the corpus and no derivation. **`Grad`'s tier (#113) is unaffected: six supports, one dynamical, still a proposal.**

## 6. The residue worth keeping

**A real question is now well-posed that was not before:** ED specifies a commitment-selection rule over **channels** (`P-LinRate`) and the substrate evaluation selects over **loci**. **Nothing in the corpus states how a channel-level selection rule induces a locus-level one** — and every probe in the substrate-evaluation arc selects over loci.

**That is not a defect found here**, and it may be entirely routine. **But it is the same class of gap as the `w(e)` scheme translation (#87) and the band-signature loss (#97): a rule stated at one level and applied at another, with the bridge unwritten.** Two of those turned out to matter.
