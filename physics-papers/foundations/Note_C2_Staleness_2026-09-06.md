# C2 rebuilt: 207 was mostly noise, and the four real hits are all the same failure

**Date:** 2026-09-06
**Status:** **Result.** C2 rebuilt, run, and worked.
**Tool:** `internal notes/_check_c2_staleness.py` (new, re-runnable).

---

## 1. The old C2 was not a work list

It reported **207 of 404 rows stale**, which is too many to act on. It had three defects pulling in both directions:

| | defect | effect |
|---|---|---|
| 1 | substring-matched the free-text `Paper` column against raw ledger prose — `016` matches inside `2016` | over-counted |
| 2 | a row with **no date** was compared against `None`, so every ledger item counted as later — and **274 of 404 rows carry no date** | over-counted, badly |
| 3 | read **only** `gravity/Gravity_TieredClaims_Ledger.md` | **under-counted** — a cosmology row overtaken by the cosmology ledger was invisible |

**Defect 3 is the one that should worry us most.** Row 45's a₀ problem was caught only because that correction happened to be cross-filed into gravity. Anything corrected in its own arc and nowhere else was outside the detector's field of view entirely.

The rebuild reads **all sixteen** arc ledgers, matches paper names on a word boundary (bare numerics must appear as an actual paper reference), requires a change word **within 400 characters of the reference** rather than anywhere in the item, and separates `OVERTAKEN` from `UNDATED` instead of merging them.

**207 → 68 flagged, 238 undated.**

## 2. The 68 is still mostly hub-paper noise, and ranking proved it

Ranked by how many distinct later corrections implicate each row, the top is: `Paper_087` (19), `087` again (19), `P11` (13), `QuadraticStrain` (11), `Paper_027` (8), `Paper_029` (8). **These are the corpus's hub papers — cited in nearly every correction, so a mention carries no information about whether any particular row went stale.** Same false-positive shape as C4's flags.

**So the productive unit of work is not the row, it is the correction.** I listed every ledger item dated **2026-09-04 or 2026-09-05** carrying a change word — **58 of them** — and checked each against the sheet.

## 3. Four real hits, and they are all one failure

> **Every one is the row-45 shape: the corpus made a correction, and the spreadsheet kept the pre-correction text.**

### Row 340 — `ξ_canonical`, overtaken three times over

| the finding | the row still said |
|---|---|
| `ξ_canonical` is **`Measured`**, not memory-floating — `Paper_096` audit row 7 re-tiered `I → Measured`, artefact named (gravity #47) | tier `Selected/Inherited`, *"sourced to memory files"* |
| the precision is a **four-significant-figure overstatement** — `1.7575` against a std of `0.3035`, a 17% spread, per-seed range 1.623–2.191 (gravity #47) | **`xi_canonical = 1.7575 lu`** |
| the `0.6` exponent is **not the same object** (gravity #50), and is **reduced, not derived** (#48) | both numbers on one row |

Now: **`ξ ≈ 1.8 ± 0.3`**, tier **`Measured`**, provenance recorded, and the `0.6` **split onto its own row** (appended, so no row number moves).

**One discrepancy left standing:** gravity #47 rounds to **`~1.8 ± 0.3`**, soft-matter #2 to **`1.76 ± 0.30`** — same artefact, two roundings. Worth making agree.

### Rows 191 and 199 — the `Coh`/`Grad` attribution

Ledger #112 established that `Paper_PhaseCoherence_P12Coh` states the `Coh` formula at §1.3 but its build implements `v3_active = |acc|/n`, which carries no neighbour–neighbour cross term and is therefore **`Grad`'s phase half scored intensively**.

- **Row 191 (`QuadraticStrain`)** — the correction **transfers**. Both `+Coh` and `−Grad` reward alignment, differing only by the NN term, so the constructive **sign survives**; and the no-crystal result was re-run on ten seeds across all three functionals. **Only the words "build-verified" had to move from `Coh` to `Grad`.**
- **Row 199 (`PhaseCoherence/V5AttractiveSign`)** — the correction **bites**. The finite-reach result and the measured `ξ` are properties of `Grad` intensively scored; **canonical `Coh` shows no alignment gain under any normalization tried** (#111), because its NN term does not contain the candidate's own phase. The row claimed the finite-reach result for `Coh`. Corrected, and the `ρ* = 0.5` / `increment = 1` calibration caveat added.

### Row 243 — the sheet had already diagnosed it and never acted

Its own `Inherited/Open` cell read *"**STALE framing** … **SUPERSEDED** by the reconstruction (next row)"* and its `Status` read *"open (stale)"* — while the `Tier` column stayed **`Open`**. Row 244 carries the current state (*orthogonality reduced, ℂ selected, residual = Solèr*). **Re-tiered `Open → Superseded`.**

## 4. Two flagged, not decided — and two checked clean

**Row 120 (`KM-I`) is flagged, not re-tiered, because it needs the author.** gravity #19 found that `KM-I` and `Paper_030` handle the **high**-acceleration limit by two incompatible mechanisms that do not cite each other: `Paper_030` §7.1 uses a **switch**, `KM-I` a **smooth Cassini-constrained family**. **#19 is explicit that the finding is not in `KM-I`** — that paper is careful, labels its hinge `D conditional on I-030`, and says outright it carries `Paper_030`'s law rather than re-deriving it. But #19 also says an earlier item *"named the wrong one as standing"*, and #34 subsequently **derived** the switch, while this row still reads *"THE STANDING MOND RESULT"* with no record of the tension. **The claim is not disputed and KM-I is not falsified.**

**Checked and clean:** **row 119** (`038.5`, Λ) already carries the force-vs-stipulate residual #24 confirmed — that finding made the *memory pointer* stale, not §3.5. **Row 112** (`GW-00`) already reads *"speed=c … INHERITED"*, which is the side #29's cross-arc `c_T` fix landed on. **`Core Theory` row 24** is already dated 2026-09-04 and explicitly handles the 2π dispute.

## 5. The real remaining problem is not staleness, it is dates

> **238 rows carry no date anywhere, and NOT ONE of them has a `SpotChecked` value either.**

**So the undated rows cannot be dated from anything already in the workbook.** `Last Verified` can only be filled by actually verifying — there is no field to derive it from. Until then, **59% of the sheet cannot be checked for staleness at all**, by this tool or any other.

**That is a bigger hole than the four rows this pass fixed**, and it is the honest answer to "is the spreadsheet current?": for 130 rows, yes and now checkable; for 238, unknown and not currently knowable.
