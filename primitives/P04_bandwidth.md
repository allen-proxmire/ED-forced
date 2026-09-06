# P04 — Bandwidth (non-negative additive scalar, four-band partition)

> **✅ CONFLICT FLAG WITHDRAWN 2026-09-04 — this card is CORRECT.** The four-band partition is canonical primitive-level content: `paper_M2`'s abstract records ED as *“committed at the primitive level to a four-band partition of bandwidth (P04 §1.5)”*, and the M-series archive removed the **forcing argument**, not the partition. `ARCHIVED_M_SERIES_NOTICE.md` explicitly retains *“The Forcing Papers (#1–#19)”*. **What is genuinely worth fixing is upstream:** canonical `Paper_087` §P04 gives only the summary (*“bandwidth as non-negative additive scalar”*) and does **not** reference §1.5's partition, which is what made this card look like it disagreed. See gravity ledger Staleness #57. *Superseded flag kept below as the audit trail.* **Original flag:** This card's title and §1.5 assert a **four-band partition** as part of P04. **Canonical `Paper_087` does not**: it defines P04 as *“Bandwidth as non-negative additive scalar”*, and `Foundations_TieredClaims_Ledger.md` staleness #2 records four-band as **archived M-series** content — *“canonical 087 has no four-band”* — having repointed two `Paper_089` citations away from it on 2026-07-29. **The corpus's standing rule is that canonical 087 wins.** By that rule this card overstates P04. **But the four-band vocabulary is used in 10+ papers across four arcs**, including the GR quartet and `Paper_027`, so the disagreement is widespread rather than local and **is not resolved here**: settling it means deciding what P04 *is*, which is a primitive-definition question. **What is established is that the card and the canonical paper cannot both be right.** Gravity ledger Staleness #56.

**Canonical primitive of the ED Generative System.**
**Position paper reference:** `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1.3.

---

## Canonical statement

Each channel $K$ at each locus $u$ carries a real-valued non-negative quantity $b_K(u) \geq 0$, additive under channel decomposition. Bandwidth further decomposes into four mutually orthogonal substrate-level bands:

- **Internal** band: carries the channel's own coherent participation content.
- **Adjacency** band: carries content shared with neighboring loci via P05 polarity-transport.
- **Environmental** band: carries content coupled to the substrate environment (decohering channels).
- **Commitment-reserve** band: carries the budget consumed by P11 commitment events.

~~The four-band partition (P04 §1.5) supplies the sesquilinear inner-product structure on the participation manifold (Paper 003).~~

> **⚠ This dependency claim is FALSE, checked 2026-09-05 (gravity ledger #91).** **`Paper_003` does not need the partition and is *insensitive* to it.** Its §2.5 audit table traces every load-bearing step and no row cites the partition; structurally, its only use of bandwidth is the normalized sum $\sum_{K'}b_{K'}$, and **any partition of the channel set leaves that sum unchanged.** What supplies the inner-product structure is **channel orthogonality** — distinct channels being orthogonal, so $\lVert\Psi\rVert^2=\sum_K b_K$ carries no cross term (`Paper_007` §3.2) — tracked as `P-Channel-Orthogonality` and **unrelated to how the channel set is partitioned into bands.** `foundations/Note_Paper003_FourBand_Check_2026-09-05.md`.
>
> **Two further cautions on this card, same date** (`foundations/Note_FourBand_Senses_2026-09-05.md`; `internal notes/_check_fourband_senses.py`). **(a) The term “four-band” is overloaded across the corpus** — at least four distinct things carry it: this partition; `Paper_012_6_Heisenberg`'s **`P-FourBand`** (position/momentum/time/energy, a *separate named censused postulate* with its substrate derivation open); `Paper_004_5_Tsirelson_Discrete` §3.6's **Bell-test settings** `{a,a',b,b'}`, which are not a bandwidth partition at all; and `Paper_003_5`'s **“adjacency-bandwidth”**, meaning bandwidth along graph adjacency. **A grep for “four-band” therefore overstates this partition's footprint by roughly a factor of three.** **(b) This card tiers the partition more strongly than its own source concept does** — `concepts/participation_bandwidth.md` says *“The four-band structure is **motivated empirically**”* and lists *“whether it is mathematically forced”* as an open question, twice. **Exactly one genuine paper-level dependent survives the audit:** `soft-matter/Paper_UnifiedP04TransportBudget`, which already declares the dependency a posit and calls it *“the load-bearing joint … the single most important thing to attack.”*

## Audit verdict

LOAD-BEARING. Bandwidth supplies the magnitude side of the complex polar participation measure $P_K = \sqrt{b_K}\,e^{i\pi_K}$ (Paper 001), the Born-rule probability weights $\text{Prob}(K \mid u) = b_K/\sum b_{K'}$ (Paper 002), and the Tsirelson-bound saturation via orthogonal-band algebra (Paper 003).

## Underlying concept treatments

- `concepts/participation_bandwidth.md` — the graded scalar measure of participation; turns the relational fact (P02) into something with quantity.
