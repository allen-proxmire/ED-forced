# What `a_eff` is: settled 2026-09-05. It is three different lengths under one symbol, and the one the arc needs is inherited.

*Working note, soft-matter transport arc. Corpus-internal read, following `Note_FConverge_Run_2026-09-05.md` §1, which left this as a dilemma. It is no longer a dilemma.*

---

## Verdict

**`a_eff` is not the DCGT cell, and it is not `ℓ_ED`. It is the material's own transport cell, inherited.** The arc's derivation chain from P08 through DCGT to a floor at the lattice spacing **does not hold**, and the two papers assert its last step in a single sentence with no argument.

**The cost is precise and it is not fatal: ED does not explain the Mott–Ioffe–Regel limit. It inherits it.** What survives is the *sharing* claim — that momentum and charge draw on one budget at that cell — which was always the arc's distinctive content anyway.

**And one thing that was recorded as passed has in fact fired.** §4.

---

## 1. Three lengths, one symbol, twenty-five orders of magnitude between them

`a_eff` appears **only** in the two transport papers. It does not occur in `Paper_073_DCGT`, which the papers cite as its source. Tracing what the symbol is actually made to mean gives three incompatible answers:

| Reading | Where it comes from | Value |
|---|---|---|
| **The substrate grain `ℓ_ED`** | `P-Scattering-Budget-Saturation`'s mechanism: *"the substrate supports none finer than one hop (**P08**, DCGT-coarse-grained to the transport scale)"* | `ℓ_P ≈ 1.6×10⁻³⁵ m` |
| **The DCGT coarse-graining cell `R_cg`** | *"`a_eff` the DCGT cell"* (`Paper_UnifiedP04TransportBudget` §9.2) | **chosen**, see §2 |
| **The interatomic spacing** | *"In ED that lattice spacing **is** the effective transport cell `a_eff`"* — and every number the arc computes | `≈ 3×10⁻¹⁰ m` |

**Twenty-five orders of magnitude separate the first from the third.** This is checklist item 19's defect in its purest form: **follow the quantity, not the spelling.** Three physically distinct lengths were carried under one name because each section's use of it was locally reasonable.

## 2. The DCGT reading is not available, and DCGT says so itself

`Paper_073_DCGT` §3.1 defines `R_cg` as *"the spatial / temporal extent over which substrate-graph content is averaged"*, and then states plainly:

> *"In practice, `R_cg` is **chosen anywhere in the scale-separated window**; coarse-grained quantities are **insensitive to the specific choice** within the window (the hallmark of effective-theory regime stability)."*

**A chosen scale to which results are insensitive cannot be a physical floor.** If the carrier mean free path really floored at `R_cg`, then a measurable quantity would depend on where an analyst chose to coarse-grain — which is exactly the property DCGT advertises as absent. **Calling `a_eff` "the DCGT cell" makes the arc's central mechanism an artifact of a bookkeeping choice.**

## 3. The P08 chain has a break in it, and the break is a step nobody wrote down

The stated mechanism is: the substrate supports nothing finer than one hop **(P08)**, that fact is **DCGT-coarse-grained to the transport scale**, and therefore *"the mean free path is floored at the cell."*

**Coarse-graining a floor at `ℓ_ED` does not install a floor at `R_cg`.** Averaging over cells *removes* structure below the cell from the description; it does not erect a physical barrier at the cell. The one real floor P08 supplies sits at `ℓ_P`, twenty-five orders below anything MIR is about, and no operation on it moves it up.

So the load is carried entirely by the last sentence: *"In ED that lattice spacing **is** the effective transport cell `a_eff`."* **That is an identification, asserted once, unargued.** Both P08 and DCGT appear in the chain and neither does any work in it.

## 4. `F-EXIST` has fired, and it was recorded as passed on half the literature

`Paper_P04TransportBudget_ResistivitySaturation` §5 states its own falsifier:

> **F-EXIST:** *charge transport that continues rising without any saturation, with the mean free path driven below `a_eff` under control of confounds — falsifies `P-Scattering-Budget-Saturation`.* **(Note: MIR saturation is already observed, so this is a consilience pass, not a new bet.)**

**The condition F-EXIST names is the documented behaviour of bad metals.** Gunnarsson, Calandra & Han (Rev. Mod. Phys. **75**, 1085) name high-T꜀ cuprates and alkali-doped fullerides as materials where the Ioffe–Regel condition is violated: resistivity keeps rising, the apparent mean free path passes below the interatomic spacing, and no saturation occurs.

**The parenthetical is the tell.** The paper looked at the materials that saturate, called the falsifier a consilience pass, and did not look at the materials that do not. **A falsifier checked against only the confirming half of a literature has not been checked.**

**Held to the standing bar, this forks — and both branches cost the arc its target regime.**

- **Branch A — the mean free path is a real length there.** Then F-EXIST's condition is met and `P-Scattering-Budget-Saturation` is **falsified in cuprates and fullerides**.
- **Branch B — past Ioffe–Regel the Boltzmann `ℓ` is not a physical length** (the standard reading, and the one behind `Note_FConverge_Run_2026-09-05.md` §3). Then F-EXIST cannot fire — **but neither can ED's mechanism apply**, because *"the mean free path is floored at the cell"* is not a statement about anything in that regime. The arc must retreat to materials that do saturate, where no electron viscosity is measured, **so F-COONSET has no venue at all**.

**Branch B is the more likely physics and the worse outcome for the arc**, because it is not a refutation that could be argued with — it is a loss of purchase.

## 5. The settlement, and what it costs

**`a_eff` is the material's emergent transport cell — the lattice constant — inherited from the material and not derived from ED.** The resistivity paper already half-says this: its postulate speaks of *"an **(emergent)** transport cell"*. Adopting that reading throughout:

- **P08 and DCGT leave the chain.** They were doing no work, and citing them implied a substrate derivation that does not exist.
- **ED does not explain MIR; it inherits it.** `ρ_max`'s row should read **I (inherited)** plainly, not *"identification / consilience"*, which reads as partial credit for grounding a known limit in P04.
- **The sharing claim survives untouched**, and it was always the distinctive part: **momentum and charge draw on one budget at that cell.** That is `P-Adjacency-Transport-Shared`, the co-onset, and `F-COONSET`.
- **`Λ` survives intact.** It cancels `a_eff` whatever `a_eff` turns out to be, so §9.3's invariant is indifferent to this settlement. Its separate domain-of-validity defect (§9's banner) is unaffected and still open.
- **The 2026-09-05 dilemma resolves onto its second horn**, and more sharply than that note put it: it is not merely that MIR saturation *might* not be ED's wall. **Nothing in ED derives any floor at the lattice spacing at all.**

**What the arc may still honestly claim:** given a material with a transport cell, momentum and charge transport share one per-cell budget, so their walls are one event. **What it may not:** that ED grounds, explains or predicts the MIR limit.

## 6. What would change this

A substrate argument that the emergent transport cell is fixed by something in ED rather than read off the material. **Nothing in the corpus attempts one**, and `Paper_073_DCGT` §7.2 records that DCGT breaks down as `R_cg → ℓ_ED`, which is the direction such an argument would have to travel. **Until one exists, `a_eff` is inherited and should be labelled `I` everywhere it appears.**

---

## References

- **`Paper_073_DCGT`** §§3.1, 7.2 — `R_cg` chosen within the window; results insensitive to the choice; breakdown as `R_cg → ℓ_ED`.
- **`Paper_087`** P08 — the substrate scale `ℓ_ED`.
- **Gunnarsson, O., Calandra, M. & Han, J. E. (2003).** *Colloquium: Saturation of electrical resistivity.* Rev. Mod. Phys. **75**, 1085 (arXiv:cond-mat/0305412).

*Gravity ledger Staleness #66; soft-matter ledger.*
