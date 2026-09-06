# Note — Does `Paper_003` need the four-band partition? No, and it is insensitive to it

**Date:** 2026-09-05 (late)
**Status:** Working note. Closes Path C open item 3. Input to AP's pending four-band branch decision (gravity ledger #82/#83/#84).
**Anchors:** `qm-kinematics/Paper_003_BornRule.md` §2 + §2.5, `Paper_003_5_ParticipationMeasure.md` §3.3–3.4, `Paper_087` P04.

---

## 1. Why the question was open

`Paper_003_BornRule` §2 lists among its upstream dependencies:

> **Paper #3 (Inner Product + Tsirelson):** **four-band orthogonality** + sesquilinear inner product structure that supports the participation measure.

That phrase is the reason `Paper_003` was carried as a four-band dependent, and it is the one and only four-band mention in the paper. The question was whether the Born-rule derivation actually rests on the partition, or only on P07 distinguishability plus P04 additivity.

## 2. The audit table answers it, because the paper has a good one

`Paper_003` §2.5 traces every load-bearing step. **Not one row cites the band partition:**

| step | source as stated |
|---|---|
| participation measure `P_K = √b_K e^{iπ_K}` | Paper #1 from P04 + P09 + Paper #3 **inner product** |
| coherent state has multi-channel participation | P02 + P07 + Paper #1 |
| commitment events have frequency content | P11 + P04 |
| **commit rate linear in `b_K`** | **`P-LinRate`**, the paper's own postulate |
| frequency limit `f_K = b_K / Σ_{K'} b_{K'}` | `P-LinRate` + law-of-large-numbers analog |
| identification `b_K = \|c_K\|²` | Paper #1 |
| Born rule | combining the two |

**The four-band phrase appears only in the dependency prose and never reaches the derivation.** Absence from a well-kept audit table is real evidence, not merely a failure to find something.

## 3. The structural reason, which is stronger than the absence

**`Paper_003`'s only use of bandwidth is a normalized sum over the whole channel set** — `Σ_{K'} b_{K'}`, in `P-LinRate` and again in the frequency limit.

**Any partition of that set leaves the sum unchanged.** Four bands, forty, or none: `Σ_{K'} b_{K'}` is identical. So `Paper_003` is not merely independent of the four-band question — **it is insensitive to it. It cannot need the partition, and it cannot test it.**

That is worth stating in both directions. `Paper_003` is not evidence *for* the partition either.

## 4. What `Paper_003` does need

1. **P07 channel structure** — that channels are distinguishable outcomes.
2. **P04 additivity over the channel set** — the normalizer. This is a sum over **disjoint channels**, i.e. P04 exactly as canonically stated, not the over-a-region extension audited in `Note_P04_AdditivityLicense_2026-09-05.md`.
3. **Channel orthogonality** — which is what *"four-band orthogonality"* was reaching for. The relevant fact is that **distinct channels are orthogonal**, so `‖Ψ‖² = Σ_K b_K` has no cross term (`Paper_007` §3.2). That is `P-Channel-Orthogonality`, tracked in `Paper_004` / `Paper_007` and **unrelated to how the channel set is partitioned into bands.**
4. **`P-LinRate`** — the paper's own load-bearing postulate, already labelled as such.

**And the license clause double-covers the normalizer.** By clause (a) the channels are disjoint and orthogonal, so the cross term vanishes; by clause (b) the Born rule is about **committed** outcomes, and P11 commits in the channel basis only. Either alone licenses the sum.

## 5. A naming collision found on the way, worth flagging

`Paper_003_5_ParticipationMeasure` §3.3–3.4 uses **"adjacency-bandwidth content"** and **"Adjacency-bandwidth structure encoded in `π_K`"** — meaning **bandwidth along graph adjacency** (P03 locus indexing + P04: which edges a motif traverses, and hence its accumulated phase). **That is not the four-band partition's "Adjacency band."**

A reader tracing the four-band question through the qm-kinematics arc lands here and can easily read it as a band. It is a collision between two uses of the same word, and it inflates the apparent four-band footprint.

## 6. Consequence for the branch decision

**`Paper_003` comes off the list of four-band dependents.** That shrinks the blast radius of the question but does not answer it — whether the partition is canonical is still #82's question, and still AP's call.

**Where the real dependents are**, by mention count, as a map for the next check rather than a verdict:

| file | mentions |
|---|---|
| `qm-kinematics/Paper_012_6_Heisenberg` | **12** |
| `primitives/concepts/participation_bandwidth` | 12 |
| `primitives/PRIMITIVE_LOAD_BEARING_AUDIT` | 7 |
| `qm-kinematics/Paper_004_5_Tsirelson_Discrete` | 6 |
| `soft-matter/Paper_UnifiedP04TransportBudget` | 6 |
| `gravity/Paper_GR-I_WeakFieldEinsteinMetric`, `primitives/P04_bandwidth` | 3 |
| `Paper_003_BornRule` | **1 — and it is the prose line, not the derivation** |

**`Paper_012_6_Heisenberg` is the one to check next**: twelve mentions is the heaviest use in any paper, and unlike `Paper_003` an uncertainty relation plausibly *does* care how bandwidth is partitioned.
