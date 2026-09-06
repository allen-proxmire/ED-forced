# Disambiguation — "adjacency" and "band" in the ED corpus

**Date:** 2026-09-05
**Status:** Canonical vocabulary note. Sits beside the primitive cards; the thing to read before building on any sentence containing "adjacency" or "band".
**Why it exists:** four distinct collisions on these two words were found in a single session (gravity ledger #91, #92, #94), and **one of them had a real argument built on it for two months** (the dwell route). Each was flagged where it was found; this is the systemic fix.
**Precedent:** `../event-density/theory/d_variable_disambiguation.md` did the same job for the two `D` variables.

---

## 1. The short version

**"Adjacency" names four different *kinds of object*, not four shades of one meaning.** That is why the collisions were hard to see: substituting one for another produces a grammatical, plausible sentence.

| | what it is | kind of object | canonical source |
|---|---|---|---|
| **A** | **graph adjacency** — the participation graph's edge structure; which loci are neighbours | a **structure** | P03 (`Paper_087`) |
| **B** | **the Adjacency band** — the class of P05-transporting channels at a locus | a **set of channels** | `primitives/P04_bandwidth.md`, as amended by Branch 3 |
| **C** | **adjacency content** — the position-locus sector, opposed to *propagation* (translation-rate) | a **content sector** | `qm-kinematics/Paper_012_7_AdjacencyBandwidth_Galilean` |
| **D** | **`∇_adj`** — the adjoint gradient in `a_C = −∇_adj Σ_C` | an **operator** | P12 (`Paper_087` §P12) |

**They are related without being interchangeable.** **A** is the graph. **B** is a class of channels defined by transporting *along* A. **C** is A's content, considered under boost. **D** is a derivative operator *on* A. **Sliding between them is the error mode**, and §3 is the case where it cost two months.

## 2. "Band" names three different partitions

| | the bands | of what | source |
|---|---|---|---|
| **1** | **Internal / Adjacency / Environmental / Commitment-reserve** | a classification of the channel index set `𝒦(u)`, by **participation-partner type** | `primitives/P04_bandwidth.md`; residue named `P-Band-Partition` |
| **2** | **position / momentum / time / energy** | a classification by **conjugate pair** | **`P-FourBand`**, `qm-kinematics/Paper_012_6_Heisenberg` §2.3 — a *separate, named, censused* postulate, substrate derivation **OPEN** |
| **3** | the four **Bell-test settings** `{a, a', b, b'}` | **correlation** bands — **not bandwidth at all** | `qm-kinematics/Paper_004_5_Tsirelson_Discrete` §3.6 |

**Partitions 1 and 2 are both four-fold and both partition channels. They are not the same partition, and neither contains the other.** Partition 3 is not a bandwidth partition in any sense; it shares only the word.

**Consequence, measured:** a grep for `four-band` across the corpus **overstates partition 1's footprint by roughly a factor of three** (gravity ledger #92; `internal notes/_check_fourband_senses.py`). Of the two heaviest apparent users, one is partition 2 and one is partition 3.

## 3. The trap that actually bit

The dwell route (`../event-density/theory/Higgs_Emergence/Dwell_Question_Answer.md`) argued that a commitment collapsing into an *Internal* channel is a chain that does not advance — a **dwell**. It got there by reading **B** as "the movement band", and it got *that* from **D**: `∇_adj Σ_C` yields acceleration, so `∇_adj` is "about movement", so the Adjacency band is the movement band.

**Every step after the first is the collision doing the work.** An operator that differentiates *along* the graph says nothing about which *channels* sit in a class defined over it.

**And the conclusion is the reverse of C.** `Paper_012_7`: P03 spatial homogeneity forces *"adjacency content (position-locus) to be **boost-invariant** while P04 propagation content (translation-rate) transforms"* — flatly, *"the position-content does not shift kinetically."* **In sense C, adjacency is the static sector.** The band the dwell argument actually needed is **propagation/momentum**, which lives in **partition 2**, not partition 1.

**So: a band from partition 1, read through an operator from P12, to reach a conclusion contradicted by sense C, when the object required lived in partition 2.** Three collisions compounding. It survived review for two months because every ingredient is real ED content.

## 4. How to write each one unambiguously

- **A** → *"the participation graph's adjacency"* or *"graph-adjacent loci"*. Never bare "adjacency" when a band is anywhere in scope.
- **B** → *"the Adjacency **class**"* or *"the class of P05-transporting channels"*. **Prefer "class" over "band"** — Branch 3 established these are classes of `𝒦(u)`, not parts of the scalar `b_K`, and the word "band" is what made them look like a decomposition of bandwidth.
- **C** → *"position content"* or *"the position-locus sector"*, with *"as opposed to propagation content"* when the contrast is live. **Avoid "adjacency content"** — it reads as A or B.
- **D** → *"P12's adjoint gradient `∇_adj`"*, always with the primitive attached.
- **Partition 2** → always *"`P-FourBand`"*, never *"the four bands"*.
- **Partition 3** → *"the four Bell-test settings"*. Do not call them bands.
- **`b_K` itself** is **bandwidth**, and bandwidth is **not a band**. Canonical P04 is a non-negative additive scalar; it carries no partition (see the P04 card).

## 5. Two live inconsistencies, recorded not resolved

1. **The propagation sector has two homes.** `Paper_012_7` attributes it to *"P04 propagation content"*; `Paper_012_6` houses the momentum band inside `P-FourBand`. Same sector, two sourcings.
2. **`Grad` sits on the same graph.** The P12 card defines `Grad` as *"the slope of event density across participation-adjacency neighborhoods"* — sense **A**, and the same domain as **D**. That is consistent, but it means P12 carries **two** adjacency-flavoured objects, and a reader meeting either should check which is meant.

## 6. Where the collisions were flagged in place

| flag | file |
|---|---|
| `Paper_003_5`'s *"adjacency-bandwidth"* = sense **A**, not band **1** | `qm-kinematics/Paper_003_5_ParticipationMeasure` §3.4 |
| `Paper_012_6`'s `P-FourBand` ≠ partition 1 | `qm-kinematics/Paper_012_6_Heisenberg` §3.1 |
| `Paper_004_5`'s bands = Bell settings | `qm-kinematics/Paper_004_5_Tsirelson_Discrete` §3.6 |
| the `∇_adj` borrow | `foundations/Note_Dwell_SecondRepair_2026-09-05.md` |
| the term's overloading, measured | `foundations/Note_FourBand_Senses_2026-09-05.md`; `internal notes/_check_fourband_senses.py` |

**If you find a fifth, add it here rather than only in place.** Flagging each collision where it was found is what let four accumulate before anyone saw the pattern.
