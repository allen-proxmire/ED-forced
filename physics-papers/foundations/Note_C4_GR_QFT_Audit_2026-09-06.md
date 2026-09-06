# C4 worked on the GR/QFT block: six of twelve are misfiled — and the postulates were never hidden, just unlinked

**Date:** 2026-09-06
**Status:** **Result.** The external audit's specific charge, checked against the papers.
**Check:** `internal notes/_check_tiered_claims_xlsx.py` (C4), then a read of each paper.

---

## 1. The charge, and the standard it is judged against

An outside reader given the spreadsheet argued that its tier system *"doesn't distinguish 'I derived this' from 'I need this to be true and am calling it derived'"*, and named the gravity/QFT block — `GR-I`–`GR-IV`, `019`–`021`, `035`.

**The standard is the sheet's own definition of its top tier:**

> **Derived** — *"Forced/proven from the 13 primitives (+ standard math) **with NO paper-specific postulate** — the strongest claim tier."*

**So the taxonomy already draws exactly the distinction the reader says is missing.** The question is only whether rows are in the right box.

## 2. Six confirmed misfiled, each on the paper's own words

| row | claim | why it is not `Derived` |
|---|---|---|
| **69** | `GR-III`: *"alpha=1 (**P-Commitment-Linear**) FORCED"* | **The claim text names its own postulate**, the tier says "no postulate", and the Postulate column says "None". **Self-contradicting on its face; needs no paper read.** |
| **63** | `GR-I`: lapse `N²~b` → weak-field Einstein metric | `GR-I` preamble 6: *"The lapse derivation **rests on a stated postulate (P-Commitment-Linear, §2)** … it is the **load-bearing structural commitment** selecting the Einstein branch."* |
| **64** | `GR-I`: emergent `g~1/b` + light bending | Same chain, same paper, same postulate. |
| **65** | `GR-II`: field-equation form `G+Λg = κT` | Preamble 2: the form comes from **Lovelock's theorem** and is ***conditional***; preamble 7: *"**κ = 8πG and Λ are inherited, not derived.**"* **Form derived, values inherited — that is the `D-via-I / Form-forced` tier by its own definition.** |
| **80** | `019`: continuum YM equations (Euler–Lagrange) | §3.4 is *"labeled D (standard variational derivation **from the P-postulated action**), with explicit acknowledgment that **the action itself is constructed via `P-YM-Action-Coarse-Graining`**."* |
| **81** | `021`: spectral-gap form `Δ ~ 1/ℓ_*` | `Paper_023`: *"Mass-gap mechanism with **`P-Gap-Coercivity`, `P-Profile-Rescaling`, `P-Quartic-Sign`**"*, and *"Gap 3 … `P-Profile-Rescaling` **is declared**."* |

**Not checked, and not claimed either way:** rows 66, 67, 68, 70, 71, 72 (`GR-II` conservation/khronometric/`c_T`, `GR-III` khronon speed, `GR-IV` `α₂`/`α₁`).

## 3. The correction the reader got wrong, stated because precision matters

The charge named *"the **entropy closure** implicit in GR-II's field-equation form."* **`GR-II` uses no entropy closure.** It establishes the form by **Lovelock's theorem** — a uniqueness argument — with one open condition resolved by a degrees-of-freedom count. **The reader's conclusion about row 65 is right; its stated mechanism is wrong**, and it guessed a Jacobson-style thermodynamic route the paper does not take.

## 4. And the sharper finding: the postulates were never hidden

The same charge said the load-bearing steps are *"withheld"* and that this is *"a postulate wearing a derivation's tag."* **Check the sheet:**

| row | claim | tier |
|---|---|---|
| 260 | Six acoustic-metric guardrails (C1–C6) | **Postulated / live** |
| 262 | `P-YM-Action-Coarse-Graining` | **Postulated / live** |
| 263 | `P-OS-Reflection-Positivity` (OS3) | **Postulated / live** |
| 264 | `P-Profile-Rescaling` (YM continuum survival) | **Postulated / live** |

> **Every postulate the reader said was concealed has its own row, correctly tiered `Postulated`, flagged `live`.**

**So this is not concealment. It is a LINKAGE failure:** the postulates are declared in their own rows, and the `Derived` rows that depend on them do not point at them — every one of the six carries `Postulate: None`.

**That is a materially different defect from the one charged, and it has a cheap fix**: the proposed `Rests On` column, which forces each `Derived` row to name its dependency or state that it has none. **The information is already in the sheet; it just is not connected.**

## 5. Verdict

**The charge lands on the filing and fails on the design.** Six of twelve rows in the named block are in the wrong box — five belong in `Grounded`/`Postulated`, one (row 65) in `D-via-I`. **The tier definitions themselves are correct and already express the distinction the reader says is absent.**

**Scope:** twelve rows of 404, in the one neighbourhood an outside reader probed. **The hit rate there was 50%.** Whether that generalises to the other 392 is **not established** — but C4 flags 36 of 55 `Derived` rows corpus-wide, and this block was 6 of its flags. **A 50% confirmation rate on the first flagged sample is a reason to work the rest of the list, not to assume it.**
