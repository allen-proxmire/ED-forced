# F1 — S2 retest: the three assignments, handed over directly

*Written 2026-09-05. **Paste the block below verbatim.** The narrowest seed in the protocol, and the only one that tests a claim standing on the scorer's work alone.*

---

## Why

`Result_F1_ArmC_SigmaC_2026-09-05.md` scored **S2 at 0/3**: no family reached the settled `Coh`/`Str` split, and **none ran the check that produces it** — pushing each candidate assignment through to `a(R)` and keeping the survivor. One family reverse-engineered the required `Σ(R)` analytically and **got the log term's sign backwards** without noticing (§7).

**So the settlement remains the one step in the chain that nobody has reproduced.** This seed removes every excuse: the candidates are enumerated, the target is stated, the aggregation question is explicitly set aside, and the only task left is arithmetic.

**If a family still fails to pick C, the settlement needs re-examining. If all three pick C, S2 is closed and `Note_SigmaC_SignCheck_2026-09-05.md` stops resting on one scorer.**

## Design

- **`Grad` is omitted and said to be omitted** — it is common to all three and cannot discriminate (verified: spherically uninvolved in the two-source problem).
- **The `ln R` form is given**, with the aggregation flagged as out of scope. Otherwise every family spends its reply on the aggregation gap, as two did, and never reaches the sign question.
- **P04's non-negativity is stated**, because `D > 0` is what makes the options distinguishable.
- **The answer is C**, placed last only because A/B/C follows the natural ordering of the readings; no other ordering was tried.
- **"If more than one works, or none does, say so"** — the escape hatch, so a family that thinks the question is malformed can say so rather than picking.

---

## THE PROMPT

```
Take a functional  Sigma = Coh - Str - Grad,  with radial acceleration
a_r = -dSigma/dR.  Negative a_r means inward, i.e. attractive.

Two sources contribute to one channel, with participation amplitudes
P^(a) = sqrt(b^(a)) e^{i pi^(a)}, all b^(a) >= 0.  After a channel sum and
radial integral that you should take as given and not examine, the two pieces
of the resulting quadratic form are:

    D(R) = sum_a b^(a)                     = GM/R          [diagonal]
    X(R) = 2 sqrt(b^(L) b^(H)) cos(Theta)  = sqrt(GM a0) * ln R
                                                           [off-diagonal;
                                                            take cos Theta = 1]

Grad is the same in all three options below, so it is omitted.

Which of these assignments yields  a_r = -GM/R^2 - sqrt(GM a0)/R
(both terms attractive)?

    A.  Str = D + X,   Coh = X
    B.  Str = D + X,   Coh = 0
    C.  Str = D,       Coh = X

Show dSigma/dR and a_r for each of A, B and C. If more than one works, or none
does, say so.
```

---

## Scoring

**Binary, mechanical, and pre-registered.** Correct answer: **C**, giving `Σ = X − D`, `dΣ/dR = √(GMa₀)/R + GM/R²`, `a_r = −GM/R² − √(GMa₀)/R`.

**A** gives `Σ = −D` — the cross term cancels and MOND vanishes entirely. **B** gives `a_r = −GM/R² + √(GMa₀)/R` — Newton attractive, MOND repulsive.

**Record per family:** the answer; whether the working is shown; and **whether the sign of `d(ln R)/dR` versus `d(1/R)/dR` is handled correctly**, since that opposition is the whole content of the question and is where the analytic attempt failed.

*Gravity ledger Staleness #78.*

---

## RESULT, run 2026-09-05 — 2/3 reach C. S2 closes, with one instructive failure.

| Family | Answer | Working | `d(ln R)/dR` vs `d(1/R)/dR` |
|---|---|---|---|
| Gemini | **C** | shown, correct | correct |
| Claude | **C only** | shown, correct | correct |
| GPT | **“B and C both work”** | shown, **one sign dropped** | **wrong** |

**Two of three reach C when handed the candidates — up from 0/3 blind.** The settlement is reproducible arithmetic, and `Note_SigmaC_SignCheck_2026-09-05.md` no longer rests on one scorer.

### The failure is the same failure as last time, in the same family, on the same term

GPT stated `X'(R) = +√(GMa₀)/R` correctly, then two lines later wrote

> `dΣ_B/dR = −dD/dR − dX/dR = GM/R² + √(GMa₀)/R`

**which requires `−dX/dR = +√(GMa₀)/R`, contradicting the derivative it had just written.** Verified numerically: **B gives `a_r = +1.265473×10⁻¹⁴` — MOND repulsive** — against the target's `−1.265740×10⁻¹⁴`. Only C matches.

**And it half-noticed.** Its *“Wait — that sign comparison is important”* paragraph opens the right question and then closes it wrongly, concluding *“both produce the same acceleration despite different `Σ` signs relative to `X`.”* **They do not.**

**This is the second time the same family has dropped a sign on the logarithmic term and not caught it** (`Result_F1_ArmC_SigmaC_2026-09-05.md` §7, where it reverse-engineered `Σ_H = −k\ln R` from an equation giving `+k\ln R`). **Twice, same term, same direction of carelessness, both times with a confident boxed answer.** The seed pre-registered `d(ln R)/dR` versus `d(1/R)/dR` as *“the whole content of the question”*; **it is also, empirically, the whole content of the failure.**

### A finding beyond the score

Claude noted, unprompted, that the exercise **adjudicates the `Coh` contradiction**: `Coh = X` is the interference-only reading (that paper's §2), while the summary's *“`Coh` read as `|ΣP|²`”* would fold `D` in and produce a wrong result. **So the arithmetic independently confirms the correction applied to `Paper_PhaseCoherence_P12Coh` §5 this morning, reached from the other direction.** That correction had been an internal judgement; it now has outside backing.

### What this does and does not establish

**Does:** the settlement is reproducible by independent readers given the candidates; the §5 correction is independently confirmed; and **the sign question is demonstrably not trivial — one of three careful readers got it wrong with everything handed over.**

**Does not:** validate the *candidate list*, the *target*, or the *framing*, all of which are mine. **A family agreeing here is agreeing inside my setup.** The blind run remains the harder test, and its S2 was 0/3.

*Gravity ledger Staleness #78.*
