# The C4 list is worked: 25 of 25 adjudicated, `Derived` 55 → 24, and the a₀ row was asserting what the paper suspended

**Date:** 2026-09-06
**Status:** **Complete.** Every C4 flag has a verdict. The four that remain are verified false positives.
**Also done:** the transcription trap closed at source in all eleven arc ledgers.

---

## 1. The headings are fixed

The root cause found in #124 — arc ledgers heading their top section *"Derived (…conditional on a postulate…)"* while the workbook defines `Derived` as *"with **NO** paper-specific postulate"* — is now blocked at source.

**All eleven arc ledgers** carry `— workbook tier: PER ROW (see rule below)` on the heading, followed by a transcription rule stating the workbook's narrower definition, saying to take the tier from the row's *"Inherited / open"* cell, and recording that **N of M** rows in that section currently name a postulate.

**The headings were not renamed to `Grounded`, deliberately.** The sections are **mixed** — only **24 of 57** rows across them name a postulate — so a blanket rename would have over-demoted the other 33. The fix points at the row; it does not answer for it.

## 2. The sweep: 25 of 25

| verdict | n | what it means |
|---|---|---|
| → **`Grounded`** | **13** | a paper-specific postulate is load-bearing |
| → **`D-via-I / Form-forced`** | **7** | no postulate; the form composes, the values are inherited |
| → **`Postulated`** | **1** | row 45, the a₀ coefficient |
| → **`Asserted`** | **1** | row 56 |
| **`Derived` stands** | **4** | verified C4 false positives |

**The pattern from #124 held all the way down: in almost every case the row's own cells already carried the right answer.** Row 54 said *"leans on an explicit P-SubstrateLocality postulate"*. Row 61 said *"FORM-FORCED **given** P-MOND-Interpolation / P-MOND-Field-Form"*. Row 78 had its postulate sitting in the `Derived` cell. Row 85 said *"sqrt-convention + arg=π_K = **P**"*. **Only the `Tier` column was wrong, and it was wrong because it came from a section heading.**

**Row 56 is the sharpest single case: its `Derived` cell reads, in full, `position`** — the paper's own A-position label — while its tier read `Derived`. Self-contradicting on its face, exactly like row 69 in the GR/QFT block.

## 3. The four that stand — because a flag is not a verdict

| row | paper | why the flag was wrong |
|---|---|---|
| **42** | Constants §4 | `P-RB-1` carries the **constants ledger** claim (row 96, already `Grounded`), not the `G_d` c-power. The source calls this one *"derived (dimensional analysis)"* in its own words. |
| **70** | `GR-III` | `P-Commitment-Linear` carries **row 69** (`α=1`), not `c_s = c`. GR-III's audit labels this a plain **`D` (leading order)**. **One of the six rows #122 declined to claim either way — it stands.** |
| **77** | `058b` | `P-Corr-Budget` carries row 76, not this claim. |
| **95** | QuantumDarwinism | `P-QD-LiveWeight` carries the **GHZ-width ceiling**, a different claim. The accounting theorem is labelled `D-structural`. |

**Four of twenty-nine flags were false — about 14%.** The check was worth running and it was not blindly trusted.

## 4. Row 45 (a₀): the sheet was asserting what the paper had suspended

**The sheet's claim text read *"a0 = cH0/(2pi), **parameter-free** ~10% match"*, tier `Derived`.**

`Paper_029`'s own audit table says:

- **row 11** — `a₀ = cH₀/(2π)`: **`Postulated / disputed` *(was D form-forced)***
- **row 15** — verdict: **`A→position`, M3**
- and in prose: *"What is suspended is the coefficient, rows 8/10/11, and with it the **'no free parameter' claim of §5.3**."*

**"Parameter-free" is precisely the phrase the paper suspended.** Audit row 10 is a `P` that must do two jobs at once: **erase the `2/3` the integral actually produces, and supply a `1/(2π)` that the same integral cancelled.** Nothing upstream fixes it — `Paper_027` and `Paper_028` both defer forward to this section.

**But this was not a missed finding. It was a partial propagation.** The 2026-09-04 correction **did** land, in three places:

| site | state |
|---|---|
| `Ledger w Claims` row 20 | ✅ *"Constant (scale) / POSTULATED-DISPUTED (coefficient)"*, `Status: STALE AS OF 2026-09-04` |
| `Core Predictions` row 3 | ✅ *"M3 — scale form-derived, COEFFICIENT POSTULATED/DISPUTED"* |
| `Core Predictions` row 19 | ✅ *"CONDITIONAL on the disputed 2π; a test of that coefficient, never evidence for it"* |
| `Ledger w Claims` row 45 | ❌ still `Derived` / *"parameter-free"* |
| `Ledger w Claims` row 342 | ❌ still *"form-derived, ~10% parameter-free match"* |

**Three of five sites updated, two missed.** Both are now corrected. This is the same shape as the earlier a₀ prior-art propagation problem, and it is an argument for the `Rests On` column rather than against the corrections.

### What survives, and it is most of it

- **The scale `a₀ ~ cH₀` is `D`** — audit row 12, reached **three independent ways** (the dipole route, horizon-competition, symmetric thermal matching). *"Three routes to the scale; none to the coefficient."*
- **`a₀(z) = cH(z)/(2π)` with the exponent forced to exactly 1 is `D`, and the audit states it is EXPLICITLY INDEPENDENT of the coefficient dispute** (row 14, *"unaffected by rows 8–11"*).

> **So the flagship evolution bet — the ~30σ MUSE-DARK III result — is untouched by any of this.** Row 46 was therefore **left at `Derived` deliberately**, with a note flagging that the `2π` inside its formula is not itself settled.

## 5. Where the tiers landed

| tier | v1 | now |
|---|---|---|
| `Derived` | 55 | **24** |
| `Grounded` | 85 | **106** |
| `D-via-I / Form-forced` | 13 | **21** |
| `Postulated` | 24 | **26** |
| `Asserted` | 16 | **17** |

**Thirty-one rows left the top tier. Twenty-nine of them went to `Grounded` or `D-via-I` — tiers that are still real results, conditional on a declared and already-catalogued commitment.** Only **two** dropped to `Asserted`/`Postulated`: row 56 and the a₀ coefficient.

> **That is the honest summary: the corpus was not overclaiming its results, it was mis-sorting them.** The postulates were already declared, already tiered, already counted. What was missing was the pointer from the dependent claim back to them — which is now the `Rests On` column, filled for every row that was ever flagged.

**C4 now reports 4 of 24, and all four are verified false positives.** Census unchanged at **174**.
