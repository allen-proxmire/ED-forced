# How Much Does ED Assume? The Basis Table

*Answers research target #20. Written 2026-09-04. Re-derive with `python "internal notes/_census_postulates.py" --triage`.*

---

## The short answer

**There is no single natural number, and that is the finding rather than a dodge.** ED's declared assumption load depends on what you count, and the corpus's four existing figures are each defensible on a narrow basis. What was wrong was quoting one without saying which.

| Basis | Postulates | + 13 primitives | What it means |
|---|---|---|---|
| Declared anywhere | 171 | **184** | Every named commitment in `physics-papers/`, including one-off modelling choices |
| Used in ≥ 2 papers | 68 | **81** | The commitment outlives the derivation that introduced it |
| Used in ≥ 3 papers | 43 | **56** | — |
| **Used in ≥ 4 papers** | **26** | **39** | **Cross-cutting: the framework's standing commitments** |
| Carries a Postulated-tier claim row | 14 | **27** | The tiered-claims workbook's basis (its "15 live") |

**Ledger-only names are excluded**, and there are now **4**: `P-Adiabatic-CG` and `P-MOND-Interp-Covariantization` (abbreviations), plus `P-BTFR-Slope-4` and `P-Deep-MOND-Limit`, which entered the corpus's text on 2026-09-04 **only because a ledger entry reported them** while summarising the un-migrated `ED-SC 4.x` papers. **They are real postulates — in papers that have not been migrated yet — and will count once those papers arrive.** *(Until 2026-09-04 the headline census used a looser rule than this document's ladder and reported **173**; writing about a postulate in a ledger inflated it. The script now applies the ladder's own rule, so both figures are **171** and they agree. Gravity ledger Staleness #53.)*

## The rule, stated so it can be argued with

**Breadth of use.** A postulate invoked in exactly one paper is a modelling choice local to that derivation, in the way a gauge choice is: it scopes one calculation and makes no claim on the framework. A postulate invoked across many papers is a standing commitment the framework carries everywhere.

Ledgers, research notes and READMEs are excluded from the count of "papers using" a postulate, because they **catalogue** postulates rather than **use** them. Including them would count the bookkeeping as physics.

This is not the only defensible rule. It is a defensible rule, it is mechanical, and it is re-runnable — which is what target #20 asked for.

## The distribution, and the thing worth knowing

| Papers using it | Count |
|---|---|
| 1 | **103 (60%)** |
| 2 | 25 |
| 3 | 17 |
| 4–5 | 17 |
| 6–10 | 8 |
| 30 | 1 |

**Sixty percent of ED's named postulates are used exactly once.** That is the single most useful fact in this document. It is also unremarkable: every framework accumulates local commitments in the course of individual derivations, and ED's discipline of *naming* them at point of introduction is why they are countable at all. A framework that does not name them has the same load and no way to count it.

## The cross-cutting set — what ED actually assumes everywhere

| Papers | Postulate |
|---|---|
| 30 | `P-RB-1` |
| 10 | `P-Bipartite-Mapping`, `P-Codim-1`, `P-Corr-Budget` |
| 9 | `P-LinRate` |
| 7 | `P-Channel-Orthogonality`, `P-Sat` |
| 6 | `P-Potential-Reading`, `P-V5-Even` |
| 5 | `P-Bundle-Definition`, `P-Connection-Naming`, `P-Fiber-Naming`, `P-Gleason-Compatibility`, `P-NonAbelian-Analogy`, `P-Quadratic-Strain`, `P-Redundancy-Mapping`, `P-StructureGroup-Naming`, `P-V5-Budget`, `P-V5-EntBudget` |
| 4 | `P-Commitment-Linear`, `P-Lorentz-Covariant-Continuum`, `P-Motif-Algebra`, `P-Profile-Rescaling`, `P-QD-LiveWeight`, `P-Re-routing`, `P-Rigidity-Gap` |

**`P-RB-1` is in a class of its own at 30 papers** — the identification of the substrate rate with the observed light speed. If any single non-primitive commitment deserves to be discussed alongside the 13, it is that one.

Note that four of the 26 are `-Naming` / `-Definition` postulates (`P-Bundle-Definition`, `P-Connection-Naming`, `P-Fiber-Naming`, `P-StructureGroup-Naming`). They declare what a structure is *called* rather than asserting a fact about the substrate, so a stricter reading would drop them and give **22 (+13 = 35)**. That is offered as a variant, not a correction — the choice is a judgment about what counts as an assumption, and this document declines to make it silently.

## Recommendation for public material

**Quote the ladder, not a number.** Two rows suffice for most purposes:

> ED declares **171** paper-specific postulates alongside its 13 primitives, each named at its point of introduction. **103 of them (60%) are used in exactly one paper** — local modelling choices scoped to a single derivation. **26 are cross-cutting**, invoked across four or more papers; those plus the 13 primitives are the framework's **39 standing commitments**, spanning roughly twelve domains.

That is stronger than any single figure, because it is checkable and because the honest large number and the honest small number both appear. An understated count invites the reader to find the rest; the ladder hands it to them.

**Two things not to do.** Do not quote "15" or "31" without their basis — they are the workbook's claim-row count and a Wave-2 scoped figure respectively, and both read as framework-wide claims when stripped of context (that error is gravity ledger Staleness #33). And do not quote 171 alone either: without the 60%-single-use fact it overstates the standing load as badly as 31 understates it.

## What was corrected to get here

- `Paper_088`'s boxed "31 total" dropped the **Wave-2** scope stated four lines above it; re-scoped 2026-09-04.
- `Paper_087` §4.15's "~35" is a round-5 count, now carrying a census note.
- `Paper_100`'s "60+" was the corpus's least-wrong figure and is closest to the ≥2-papers row.
- The tiered-claims workbook's Ratio sheet stated "15 live" as *"the only genuinely per-domain knobs"*; it now carries its basis.
- A mechanical census on 2026-09-04 first returned **51** from a hand-typed grep that matched only bolded or backticked names. The script returned **173**. The grep was wrong by 3.4×, inside the note documenting an understated count.

## Standing maintenance

`_census_postulates.py` carries a baseline and **exits nonzero when the count drifts**. Run it after any session that names a postulate; run `--triage` to regenerate this document's tables. A number in this file that disagrees with the script is stale, and the script wins.
