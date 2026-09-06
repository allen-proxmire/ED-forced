# Note — The dwell arc's second defect: the `∇_adj` borrow, and why removing it does not rescue the argument

**Date:** 2026-09-05 (late)
**Status:** Working note. Closes Path C open item 6, the repair Branch 3 explicitly did not touch.
**Anchors:** `../event-density/theory/Higgs_Emergence/Dwell_Question_Answer.md` (the 2026-07-05 retraction), `Paper_087` P11 + P12, `qm-kinematics/Paper_012_7_AdjacencyBandwidth_Galilean`, `qm-kinematics/Paper_012_6_Heisenberg`, `primitives/P04_bandwidth.md` (as amended by Branch 3).

---

## 1. What was owed

The July retraction listed **two** defects. Branch 3 (#93) answered the first on its own terms: the argument *"hung on P04 carrying a four-band partition … not in the canonical primitive"*, and under Branch 3 the partition is **not in P04 and never needed to be** — the bands are a classification of `𝒦(u)` licensed by P05/P07/P10/P11, summed by P04. The Internal class exists; a commitment has somewhere to collapse into.

**The second defect was untouched:**

> The *"adjacency = movement direction"* reading was borrowed from **P12** (the Σ-gradient/acceleration construct, `a_C = −∇_adj Σ_C`), a *different, unrelated* primitive, and misapplied to interpret a "P04 band" that isn't canonically there.

## 2. It is a naming collision — the fourth found this session

**P12's `∇_adj` is an adjoint gradient: a derivative operator on the adjacency graph.** The **Adjacency band is a class of channels.** They share the letters "adj" and nothing else.

The slide was: `∇_adj Σ_C` yields **acceleration**, so `∇_adj` is "about movement", so **the Adjacency band is the movement band**, so a commitment landing *outside* it is a chain that does not move — a **dwell**.

**Every step after the first is the collision doing the work.** An operator that differentiates *along* the adjacency graph says nothing about which *channels* are in an Adjacency class.

This joins the session's other three: `Paper_012_6`'s `P-FourBand` vs the card's partition; `Paper_004_5`'s Bell-test "bands"; `Paper_003_5`'s "adjacency-bandwidth" (#91, #92).

## 3. And the conclusion it reached is contradicted, not merely unsourced

This is the part that changes the verdict. **`Paper_012_7_AdjacencyBandwidth_Galilean` says the opposite of what the dwell argument assumed:**

> under Galilean boost, P03 spatial-homogeneity forces **adjacency content (position-locus) to be boost-invariant** while **P04 propagation content (translation-rate) transforms**

and, flatly:

> P03 adjacency invariance under boost (**the position-content does not shift kinetically**)

**In the dominant qm-kinematics usage, adjacency is the *position* sector — the boost-invariant, non-kinetic one.** The dwell argument read it as the *movement* sector. **That is backwards**, and it means the borrow was not merely an unlicensed shortcut to a right answer: it produced a reading an existing paper denies.

## 4. What the argument actually needed lives in a different partition

**The sector that carries motion is propagation / momentum** — and that band belongs to **`Paper_012_6`'s `P-FourBand`** (position / momentum / time / energy), which #92 established is a **separate, named, censused postulate**, not the card's Internal / Adjacency / Environmental / Commitment-reserve partition.

**So the dwell argument reached into partition 1 for a band that lives in partition 2, and glued them with an operator from P12.** A three-way collision, and the reason it looked plausible for months: every piece is real ED content, just not the pieces the argument needed.

## 5. Even with the right band, one thing is still missing — and P11 is where it stops

Canonical P11, in full:

> At certain substrate-level events ("commitment events"), a chain's multi-channel participation collapses to single-channel participation, with the un-selected channels' phase content randomized. The collapse is irreversible.

**It says nothing about locus.** A chain's participation four-tuple is `(C, K, u, t)`; commitment selects `K`. **Nothing canonical says that selecting one `K` rather than another changes `u`.**

So the dwell claim needs an identification that no primitive supplies:

> **`P-Commitment-Advancement` (candidate — NOT adopted, NOT censused):** *a commitment event that selects a propagation-carrying channel advances the chain's locus; one that selects a non-propagating channel does not.*

> **✅ ADOPTED 2026-09-06 on AP's decision (gravity ledger #117).** Declared at `Paper_087` §P11 and entered in the postulate registry; **census 173 → 174.** **The dwell route is therefore unblocked at the sourcing level:** a commitment into the **Internal** class (Branch 3) is now a licensed non-advancing commit. **What remains is a gap, not a blocker** — nothing here derives `σ_τ`, the lepton masses, or anything else in the mass sector. **And the certified rule is unaffected:** *“always advances”* is the special case in which every commitment selects an Adjacency-class channel, so every result measured on that rule stands. *(The original candidate framing follows, kept as the audit trail.)*

**Stated so it can be attacked, and deliberately left in this note rather than written into a paper** — naming it in a paper would increment the census and would smuggle a candidate into the corpus as a commitment. The July retraction asked for exactly this discipline: *"If pursued, it must be proposed honestly as a **new candidate primitive refinement** … not asserted as something the existing 13 primitives already admit."*

## 6. Verdict

**The second defect is repaired as a diagnosis, not as a rescue.** The borrow is identified, removed, and shown to have produced a reading `Paper_012_7` contradicts. **What it was propping up does not survive on canonical primitives.**

**Net state of the dwell route after Branch 3 plus this note:**

| | before | after |
|---|---|---|
| Four-band sourcing (defect 1) | blocking | **answered** — bands classify `𝒦`, licensed by P05/P07/P10/P11 |
| `∇_adj` borrow (defect 2) | flagged, unrepaired | **removed** — and its conclusion is contradicted by `Paper_012_7` |
| Adjacency = movement | assumed | **false in the dominant usage**; adjacency is the boost-invariant position sector |
| The band it needed | — | **propagation/momentum, in `P-FourBand`** — a different partition |
| Commitment ⇒ advancement | assumed | **unsourced**; `P-Commitment-Advancement` named as a *candidate*, not adopted |

> **AND THE SAME MISSING POSTULATE BLOCKS THE SUBSTRATE-EVALUATION ARC — found 2026-09-06 (#116).** **P11 selects a CHANNEL; the certified rule selects a LOCUS** (`compute_candidates` → `admissible_neighbors`, with `u` excluded; `update.py`: *“advance the front (active u → v)”*). **`P-Commitment-Advancement` is exactly that missing bridge**, so **both arcs are blocked on one statement, from opposite ends** — this one needs it to *permit* not advancing, the evaluation arc needs it to *justify* advancing. **And the certified rule assumes a STRONGER version: not “advances iff propagation-carrying” but “always advances”**, which is why it is *“ballistic-or-extinct … no dwell”*. **So the reference substrate forbids the phenomenon this arc is about — the dwell question could never have been settled by simulating it.** **And this note's own residual objection is answered:** July argued there is *“no canonical internal band for a commitment to collapse into”*, and **Branch 3 (#93) supplied exactly that class.** `foundations/Note_ChannelVsLocus_Selection_2026-09-06.md`.

**So: the dwell route is no longer blocked by a sourcing error. It is blocked by an honest missing postulate, which is a better place to be blocked** — the earlier state had a broken argument wearing the appearance of a derivation, and this one has a clearly-stated gap with a name.

**The mass sector is unaffected**, as `FourBand_Dependency_Check.md` established independently: `σ_τ`, Theorems M1/M2, the MR-P/MR-R massless slots and `Paper_113`'s mass-as-bandwidth-budget all stand on canonical single-scalar P04. **Nothing here moves them.**

## 7. One further thing worth flagging

`Paper_012_7` attributes the propagation sector to **"P04 propagation content"** while `Paper_012_6` puts the momentum band inside **`P-FourBand`**. Those are two different homes for the same sector. Not chased here; noted so the next reader does not have to rediscover it.
