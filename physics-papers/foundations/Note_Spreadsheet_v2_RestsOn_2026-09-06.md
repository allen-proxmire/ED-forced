# Spreadsheet v2: the `Rests On` column — and five C4 flags that were pointing at the wrong paper

**Date:** 2026-09-06
**Status:** **Built.** `ED_ItemizedTheory_TieredClaims_v2.xlsx`. The original is untouched.
**Builder:** `internal notes/_build_tiered_claims_v2.py` (re-runnable).

---

## 1. What v2 adds

Ledger #122 found the defect in the GR/QFT block is a **linkage failure, not concealment**: the postulates are declared in their own rows, correctly tiered `Postulated / live`, and the `Derived` rows that depend on them all carry `Postulate: None`. The fix is to make the dependency explicit, so three columns were added to `Ledger w Claims`:

| column | what it holds |
|---|---|
| **`Rests On`** | what the claim needs beyond P01–P13, at three labelled confidence levels |
| **`Sign-Critical`** | a claim whose conclusion flips with one sign — seeded by keyword, every hit a candidate |
| **`Last Verified`** | the row's latest date, lifted out of prose into a sortable column |

**`Rests On` is filled for all 49 `Derived` rows** — the tier under scrutiny — and every cell says how much it is worth:

- **VERIFIED (6)** — read against the paper, quoting its own words.
- **CANDIDATE (29)** — the paper declares this postulate; whether *this claim* needs it is **unread**.
- **none found (20)** — the paper declares no censused postulate. Mechanical check only.

**And six rows were re-tiered**, the ones verified in #122. Rows 63, 64, 80, 81 → `Grounded`; row 69 → `Postulated`; row 65 → `D-via-I / Form-forced`. The original tier is preserved inside the `Rests On` cell, so nothing is lost silently.

## 2. The finding that actually matters: five flags were on the wrong paper

The first build looked clean. **It was not.** The `Paper` column is free text — bare numbers (`029`), short names (`GR-I`), section refs (`Constants-paper §4`), pair refs (`089/093`), folder-local labels (`Cos-06`) — and the substring matcher resolved five of them to a paper with a coincidentally matching digit:

| row | sheet says | matcher read | correct paper |
|---|---|---|---|
| 42 | `Constants-paper §4` | `Paper_004_GleasonUniqueness` | `Constants_Ledger_and_G_Dimension` |
| 44 | `Cos-06` | `Paper_006_UnitaryEvolution` | `Paper_ED_Cos_06_InflationarySpectrum` |
| 89 | `012.7` | `Paper_001_PreIndividuation` | `Paper_012_7_AdjacencyBandwidth_Galilean` |
| 92 | `A1 (CommonCauseNotChannel)` | `Paper_001_PreIndividuation` | `Paper_CommonCauseNotChannel_A1` |
| 93 | `B4 (ChargeAsTopology)` | `Paper_004_GleasonUniqueness` | `Paper_ChargeAsTopology_B4` |

**This is the second time the same matcher has produced a wrong C4 answer** — it previously returned zero hits, a false all-clear on exactly the check C4 exists for. So the repair is two independent defences, not one:

1. **An explicit `ALIAS` map** for the sheet's idiosyncratic names, including the four **pair refs** (`089/093`, `090/094`, `034/036`, `054/056`), which now read **both** papers instead of whichever matched first.
2. **A folder guard.** A fuzzy hit whose directory disagrees with the sheet's own `Folder` column is **rejected, not returned**. **The guard alone catches all five** — the sheet already recorded the right neighbourhood, and the checker was ignoring it.

An unresolvable name now writes `UNRESOLVED — NOT checked` into the cell rather than guessing. **After the repair, all 49 `Derived` rows resolve and none is unresolved.**

**The resolver is now imported by `_check_tiered_claims_xlsx.py` rather than duplicated in it,** so the alias map and the guard cannot drift between the two tools.

## 3. Effect

| | v1 (old resolver) | v1 (fixed resolver) | **v2** |
|---|---|---|---|
| C4 flagged | 36 of 55 | **34 of 55** | **29 of 49** |

The v1 count moved 36 → 34 purely from fixing the resolver: false hits dropped, real ones appeared. **The 36 quoted in #122 was slightly wrong in both directions, and the 50% confirmation rate on the GR/QFT sample is unaffected** — those twelve rows all resolved `EXACT` and were read by hand.

`Sign-Critical` was also narrowed after its first pass fired on *"non-negative additive scalar"* and *"structural-positive"*, which are not sign claims. It now seeds 15 rows on the terms that carry a physical sign (attractive/repulsive, constructive/destructive, inward/outward, parity, chirality).

## 4. What v2 does NOT do, stated so it is not mistaken for done

- **The 29 CANDIDATE rows are not adjudicated.** Deciding them without reading each paper would reproduce the exact error the audit found.
- **C2 is untouched** — 207 rows still predate a ledger finding about their own paper.
- **C1 is untouched** — 87 of 174 corpus postulates are still never mentioned.
- **274 of 404 rows carry no date at all**, so `Last Verified` is empty for two thirds of the sheet. That is a fact about v1 the new column makes visible rather than a defect it introduces.

Census unchanged at **174**.
