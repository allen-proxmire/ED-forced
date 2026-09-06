# C1 closed: 85 unmentioned postulates were only 29 real gaps, and the ladder is what says so

**Date:** 2026-09-06
**Status:** **Closed.** Cross-cutting and recurring rungs both at zero.
**Tool:** `internal notes/_check_c1_coverage.py` (new, re-runnable).

---

## 1. A count is not a work list

The old C1 reported **87 of 174 corpus postulates never mentioned in the workbook**, which reads as a large hole. It is not one, and the corpus itself already had the argument for why.

`POSTULATE_BASIS.md` (research target **#20**, closed 2026-09-04) established that ED's commitments form a **breadth ladder**, and that a large share appear in **exactly one paper** — local modelling choices scoped to a single derivation, like a gauge choice. **A one-paper postulate absent from a corpus-wide claim catalogue is not obviously a defect, and listing all of them would bury the ones that are.**

So C1 was rebuilt to report by rung rather than as a total:

| rung | count | verdict |
|---|---|---|
| **CROSS-CUTTING (≥4 papers)** | **10** | a standing commitment of the framework with no row. **A real gap.** |
| **RECURRING (2–3 papers)** | **19** | outlives the derivation that introduced it. **Worth a row.** |
| LOCAL (1 paper) | **56** | scoped to one derivation. **Absence is defensible.** |

**85 unmentioned, 29 actually missing.** The other 56 are left out on purpose, and the reason is recorded on every added row so nobody re-opens it as a bug.

## 2. The 29 are now rows

Each carries the **paper's own declaration text**, the number of papers that declare it, and the folders it spans. Tier `Postulated`.

The widest were `P-Gleason-Compatibility` and `P-S1-Invariant` (6 papers each), then a cluster of five at five papers — **`P-Bundle-Definition`, `P-Fiber-Naming`, `P-Connection-Naming`, `P-StructureGroup-Naming`, `P-Cascade-Continuity`**. The four naming postulates are one family: the substrate-ontological naming that makes the fiber-bundle reading of `Paper_015`/`Paper_016` work. **A four-part standing commitment behind the gauge sector, with no catalogue entry until now.**

**Only three are marked `live`** — `P-Band-Partition`, `P-Locus-Bandwidth-Bound` (both named 2026-09-05, Branch 3) and `P-Commitment-Advancement` (adopted 2026-09-06, #117). **The other 26 are marked "live status NOT assessed"** and are deliberately *not* counted as live: assessing 26 live-statuses needs 26 paper reads, and guessing would put a number into the parsimony basis that nobody had checked.

**The `Ratio` sheet's basis therefore moves 15 → 18**, with the reason recorded in the cell.

## 3. The finding worth keeping

**`P-Canonical-Operating-Point-ED-SC` states, in its own text:**

> *"The canonical operating point ξ_canonical ≈ **1.8 ± 0.3** lu (**quoted elsewhere as 1.7575**; see the …)"*

**The corpus had already written the ξ correction into a postulate — with the wrong value named as the thing to watch for — while the spreadsheet was still carrying `1.7575`.** That independently confirms the row-340 fix made an hour earlier under C2, and it sharpens the pattern this whole audit keeps finding:

> **The corpus knows. The catalogue lags.** Every real hit across C1, C2 and C4 has had this shape — the paper, the arc ledger, or in this case a postulate's own statement already carried the correct state, and the workbook carried the earlier one. **Not one of them was the corpus getting the physics wrong.**

## 4. Where the three checks now stand

| check | before | now |
|---|---|---|
| **C1** postulate coverage | 87 unmentioned | **0 cross-cutting, 0 recurring**, 56 local by design |
| **C2** staleness | 207 flagged | **4 real hits fixed**; 238 rows undated and not assessable |
| **C4** `Derived` resting on a postulate | 36 of 55 | **4 of 24, all verified false positives** |

**The one thing left is not a check — it is the 238 undated rows**, none of which carries a `SpotChecked` value either. No tool can date them. That needs verification, not tooling.

Workbook: **435 rows**. Census unchanged at **174**.
