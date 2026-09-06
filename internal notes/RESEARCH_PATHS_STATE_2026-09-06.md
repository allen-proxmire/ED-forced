# Research paths — state at 2026-09-06

*Written to be picked up cold, by AP or by a session that has never seen this work. **Read this before resuming; do not reconstruct a path from memory.** Everything below is checkable against `physics-papers/gravity/Gravity_TieredClaims_Ledger.md` and the scripts named. Supersedes the per-path state of `PATH_A_STATE_2026-09-05.md` and `PATH_C_STATE_2026-09-05.md`, which stay as the audit trail of where those paths stood on 09-05.*

---

## The five paths, at a glance

| | path | state | ledger |
|---|---|---|---|
| **A** | The layer seam — `Coh` vs `Grad`, `ρ*`, the 2π direction | **CLOSED** | #101–#121 |
| **B** | Koide / mass-ratio | **CLOSED OUT** — folded into A and C; not a live path | — |
| **C** | What licenses combining bandwidth across things | **CLOSED** | #82–#100 |
| **D** | The naming seam — `θ_ind`, the two senses, `Paper_072`'s index | **CLOSED 2026-09-06** | #128–#134, #139 |
| **E** | The collapse account — what a branch is, what the coefficient is | **OPEN, blocked on a stated thing** | #135–#137, #139 |
| — | The tiered-claims audit (not a path; a pass) | **WORKED TO ZERO** | #122–#127, #138, #140 |

---

## Path D — closed 2026-09-06

**The question:** `θ_ind`, individuation's only undetermined quantity, and what "individuation" even names.

**What closed:**

- **`θ_ind` is a LENGTH, not a dimensionless constant.** `R = (a−1)/2` for a side-`a` hypercube **in every dimension**; survives 60% disorder and real committed morphology. The `ℏ`/bandwidth-normalization route is **closed by proof** — `R` is invariant under `b → λb`. And `R` is a length **only where the substrate has geometry**: on an expander it stalls at `O(1)`. (#128)
- **`θ_ind = 1`**, via the decoherence route: `P-Factorized-IC` **is** individuation at `θ_ind = ∞`, and a region with no interior gives factorization nowhere to be accurate. Depth is quantized, so the threshold is a **step function of `ξ`** and does not inherit `ξ`'s error. A second route — the smallest square with a locus off its own boundary — agrees using no `ξ` at all. **Tier: `D-via-I`, conditional on `ξ < 2`.** (#129)
- **`ξ` tightened to 1.740 ± 0.028**, which put that bracket at **9.2σ**, not 0.78σ. The published `± 0.30` was a per-snapshot spread, not an uncertainty. (#130)
- **"Individuation" names two things**, and they are **anti-correlated**: sense 1 is commitment (channels, binary, P07 → `p(K|L) = 0`); sense 2 is the system/environment cut (loci, graded, `R`). Documented at `primitives/INDIVIDUATION_DISAMBIGUATION.md` with a re-runnable checker. (#131–#132)
- **`Paper_072`'s "rule-type" settled** as wording, not a third index — the label reading would have made a two-qubit entangled state *not* entangled. Substitution applied on instruction. (#133–#134)

**Nothing is left on D** except one editorial call AP may want: whether to rename `Γ_individuation` corpus-wide, which §7 of the disambiguation deliberately does *not* recommend.

---

## Path E — open, and the blocker is stated

**The question:** the collapse-rate coefficient. `τ ∝ ℏ/E_G` is *grounded-in-kind*; the prefactor is not pinned.

**What is now known, all of it narrowing rather than closing:**

1. **A1 cannot supply it** (#136). A1 is **region-to-region** transmission; branch distinguishability is a different pair of objects, and A1's measured value is **exactly zero everywhere** with its own verdict that *"there is no canonical positive determinability scalar to be found this way."* Both branches of the bits fork are closed for an intrinsic number.
2. **The object it would apply to does not exist at the substrate layer** (#137). ED superposes **channels at one locus**; the derivation needs superposition over **places**. And the certified substrate **does not branch** — *measured*, one seed → one worldline — so the experiment cannot be run there.
3. **And it has to be a graded→binary conversion** (#139). Sense 1 is binary by P07; sense 2 is graded. The derivation needs graded driving binary, and **that is what a coefficient would convert between.**

> **The blocker, in one sentence: the coefficient needs a substrate-layer representation of a spatial branch, and building one is a foundational decision about ED's ontology — not a derivation.**

**Do not** attack this by re-running A1, by pushing `θ_ind` at it (25 orders of magnitude short, #135), or by looking for a missing integral behind `Paper_024`'s C4 flag. **All three are closed and the reasons are recorded.**

---

## The audit pass — worked to zero

Not a research path, but the reason the repo can be read at all.

| check | before | now |
|---|---|---|
| **C1** postulate coverage | 87 unmentioned | **0 cross-cutting, 0 recurring** (56 one-paper, excluded by design) |
| **C2** staleness | 207 flagged | **4 real hits fixed** |
| **C4** `Derived` on a postulate | 36 of 55 | **4 of 24, all verified false positives** |
| navigation pointers | unknown | **0 dead** |
| today's notes orphaned | unknown | **0** |

`Derived` went **55 → 24**. **Twenty-nine of the thirty-one rows that moved went to `Grounded` or `D-via-I`** — still real results, conditional on commitments already declared and counted elsewhere in the sheet. **Two dropped further.**

**The root cause was one word, not a habit.** The arc ledgers head their top section *"Derived (forced — but each **conditional on a postulate**)"*; the workbook defines `Derived` as *"with **NO** paper-specific postulate."* Same word, opposite meanings, and the workbook is fed by the ledgers. **The qualifier lived in a parenthetical and parentheticals do not travel.** Fixed at source in all eleven ledgers.

---

## What is still owed, in priority order

1. **238 of 435 workbook rows carry no date** — and none carries a `SpotChecked` value either, so **no tool can date them**. Until someone verifies them, 55% of the sheet is not staleness-checkable. **This is the largest open item in the repo and it is not automatable.**
2. **81 dead pointers outside the navigation files** — old `domain-arcs/` paths and `project_*.md` refs inside individual papers. Real, low-traffic, mechanical.
3. **32% of "individuation" uses are still ambiguous** by the sense-checker. Not errors; places where the sense should be said out loud. The writing rule is §4 of the disambiguation.
4. **`P-Radial-Channel-Density`** in `Paper_030` §4.3 — AP's outstanding call on whether to name it (would increment the census from 174).
5. **Three SPARC files** held out of `ed-lab` pending a call on redistributing third-party data from a public repo.
