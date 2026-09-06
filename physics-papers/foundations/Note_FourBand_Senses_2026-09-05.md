# Note — "Four-band" names at least four different things, and the disputed partition has one genuine paper-level dependent

**Date:** 2026-09-05 (late)
**Status:** Working note. Closes Path C open item 3b. **Prices** AP's pending four-band branch decision (gravity ledger #82/#83/#84) without deciding it.
**Check:** `internal notes/_check_fourband_senses.py` (re-runnable classification).
**Follows:** `Note_Paper003_FourBand_Check_2026-09-05.md` (#91).

---

## 1. The question, and why the answer is not what the count suggested

`Paper_012_6_Heisenberg` carries **twelve** four-band mentions — the heaviest use in any paper. The reasoning for checking it was that an uncertainty relation plausibly *does* care how bandwidth is partitioned, so if anything genuinely needed the disputed partition, this was it.

**It is not the same partition.**

| | bands |
|---|---|
| **The disputed partition** (`primitives/P04_bandwidth.md` §1.5) | **Internal / Adjacency / Environmental / Commitment-reserve** — partitions `b_K` by *participation-partner type* |
| **`Paper_012_6`'s `P-FourBand`** (§2.3) | **position (P03 adjacency) / momentum (P04 propagation) / time (P13) / energy (P-RB-1)** — the *conjugate pairs* |

`Paper_012_6` declares its own as a **named paper-local postulate**, already in the census, with *"substrate-level derivation of the four-band orthogonality from the 13 primitives"* explicitly **OPEN**. It is not inheriting the disputed partition; it is positing a different one and saying so.

## 2. The term is overloaded — four senses found

**Sense 1 — the disputed partition.** Internal / Adjacency / Environmental / Commitment-reserve.

**Sense 2 — the conjugate-pair bands.** `Paper_012_6`'s `P-FourBand`. Separate, named, censused, open.

**Sense 3 — the CHSH settings.** `Paper_004_5_Tsirelson_Discrete` §3.6, verbatim: *"The four-band partition (Bell-test settings `a, a', b, b'`)"*. **Not a bandwidth partition at all** — four *correlation* bands, from the experiment's design.

**Sense 4 — "adjacency-bandwidth".** `Paper_003_5` §§3.3–3.4: bandwidth along graph adjacency (which edges a motif traverses). Not a band. Flagged in place as #91.

## 3. What survives as a genuine dependent

| file | mentions | sense | verdict |
|---|---|---|---|
| `Paper_012_6_Heisenberg` | 12 | 2 | not a dependent |
| `Paper_004_5_Tsirelson_Discrete` | 6 | 3 | not a dependent |
| `Paper_089_V1Kernel` | 2 | 1 | not a dependent — **already corrected 2026-07-29** as archived-M-series, *"not load-bearing"* |
| `Paper_003_BornRule` | 1 | 1 | not a dependent — **insensitive** (#91) |
| **`Paper_UnifiedP04TransportBudget`** | **6** | **1** | **GENUINE** |
| `Paper_GR-I_WeakFieldEinsteinMetric` | 3 | 1 | nominal — cites *"P04 (four-band bandwidth)"* in a primitives list; the derivation uses reciprocal edge bandwidth `b_uv`, not the partition |

**Eighteen of the mentions that looked like blast radius are senses 2 and 3.**

**Exactly one genuine paper-level dependent survives**: `Paper_UnifiedP04TransportBudget`, whose audit row reads *"P04 four-band partition; Adjacency = P05-transport content | **P (primitive)** | `primitives/P04` §1.5"*. **And it already flags itself** — Preamble 3: *"the load-bearing identification is a posit, not a theorem … it is the load-bearing joint, and the single most important thing to attack."*

## 4. Two problems on the cards themselves

**(a) The card and the concept tier it differently.** `primitives/P04_bandwidth.md` presents the partition as canonical primitive-level content. Its own source concept, `primitives/concepts/participation_bandwidth.md`, says: *"The four-band structure is **motivated empirically**. Whether it is mathematically forced by the participation-graph structure … "* — listed as an open question, twice. **Those are not the same claim**, and the stronger one is the derived card rather than the source.

**(b) The card claims a dependent it does not have.** `primitives/P04_bandwidth.md`: *"The four-band partition (P04 §1.5) supplies the sesquilinear inner-product structure on the participation manifold (Paper 003)."* **#91 showed `Paper_003` needs channel orthogonality, not the partition, and is insensitive to how the channel set is partitioned.** Flagged in place.

## 5. What this does to the branch decision

**It does not decide it.** Whether the partition is canonical is a primitive-definition question, and #82's conflict — `primitives/P04_bandwidth.md` asserting it in its own title while canonical `Paper_087` P04 does not mention it — is untouched by anything here.

**It prices it.** The disputed partition has **one** genuine paper-level dependent, and that paper already declares the dependency as a posit and names it its most attackable joint. **Branch 3** — bands as channel *classes*, disjointness licensed by individuation — is therefore far cheaper than the raw footprint implied. Branch 1 (revert #57) and Branch 2 (amend `Paper_087`) are also cheaper than they looked, for the same reason.

**The honest residual:** a low dependent-count is an argument about *cost*, not about *truth*. If the partition is right, it should be in `Paper_087`; if it is not, it should not be in the card's title. That question is still AP's, and still open.
