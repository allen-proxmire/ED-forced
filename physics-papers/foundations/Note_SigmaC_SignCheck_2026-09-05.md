# The three-way sign check: `Str` is the diagonal, `Coh` is the interference, and P12 was right all along

*Foundations working note, 2026-09-05. Closes Foundations staleness #10, opened the same day. Script: `internal notes/_check_sigma_sign.py`, re-runnable.*

---

## Verdict

**Option 2 is the unique winner.** Of the three candidate assignments, exactly one reproduces `Paper_030`'s established `a = a_N + √(a_N a_0)`, and it matches to floating-point precision at every radius tested.

$$\boxed{\;\mathrm{Str}_K=\sum_a b_K^{(a)}\;,\qquad \mathrm{Coh}_K=2\!\!\sum_{a<b}\!\sqrt{b_K^{(a)}b_K^{(b)}}\cos\Theta_{ab}\;}$$

| Assignment | `a_r` at `R = 10¹⁹ m` | Target | Match |
|---|---|---|---|
| **1** — `Coh = Str = |Σ P|²`, they cancel | `0.000000e+00` | `−1.265740e-14` | no |
| **2** — `Str` = diagonal, `Coh` = interference | **`−1.265740e-14`** | `−1.265740e-14` | **YES** |
| **3a** — `Coh` sits out, `Σ_C = −Str` | `+1.265473e-14` | `−1.265740e-14` | no (repulsive) |
| **3b** — `Coh` sits out, `Σ_C = +Str` | `−1.265473e-14` | `−1.265740e-14` | no (Newton repulsive) |

**And the three headline consequences are all favourable:**

1. **P12 needs no amendment.** `Σ_C = Coh − Str − Grad` had the right sign pattern from the start.
2. **The physics is unchanged.** Same two terms, same result, same `a = a_N + √(a_N a_0)`. Only the *assignment* of the cross term moves, from `Str` to `Coh`.
3. **The constructive sign becomes a structural requirement rather than an assumption.** §4.

---

> **⚠ SCOPE CORRECTION, 2026-09-05, from the blind replication run.** **This check establishes less than it claimed, and the limit was not stated.** It takes the cross term's `√(GMa₀)·ln(R)` form from `Paper_QuadraticStrain_v1` §5.1 **as given** and asks only which assignment gets the signs right. **It never asks whether P12 licenses a logarithm at all.** An external reader, working blind, pointed out that `√(b^{(L)}b^{(H)}) ∝ √((GM/R)(a₀R)) = √(GMa₀)` is **exactly R-independent**, so *“an R-independent term has zero adjacency-gradient — under a direct, pointwise application of P12 this cross term contributes nothing to the acceleration, not a small contribution, exactly zero.”* **The corpus supplies the missing piece** — `Paper_030` §4.3's bilocal-channel density `∝ 1/R` plus a radial integral — **but that is an aggregation rule, and P12 as stated is a *local* gradient of a *locally-evaluated* functional.** **So the correct scope of what follows is: *given* that the cross term enters `Σ_C` as `√(GMa₀)\ln R`, only the diagonal/off-diagonal split yields two attractive terms.** The check is sound within that scope. **Whether a locally-evaluated `Σ_C` can produce that form at all is a separate and open question**, and it is the layer seam again (`layers/Note_TheSeam_And_SigmaC_2026-09-05.md`). `substrate-evaluation/Result_F1_ArmC_SigmaC_2026-09-05.md` §4; gravity ledger Staleness #77.

## 1. Why no single `Str` can work, in one line

The target needs the diagonal and the cross term to enter `Σ_C` with **opposite** signs. That is not a preference; it follows from calculus:

$$\frac{d}{dR}\!\left(\frac1R\right)<0,\qquad \frac{d}{dR}\big(\ln R\big)>0.$$

The Newtonian piece is `∝ 1/R` and the MOND piece is `∝ ln R` (`Paper_QuadraticStrain_v1` §5.1, after the radial integral with the `1/R` bilocal channel density). **Making both accelerations point inward therefore requires opposite signs upstream.**

`Str_K = |Σ_a P_K^{(a)}|²` carries the diagonal and the cross term with **the same** sign, because both are positive parts of one squared modulus. **So no choice of overall sign on a single `Str` can produce the target** — options 3a and 3b fail in exactly this way, each getting one term right and the other backwards.

**Splitting them across `Coh` (`+`) and `Str` (`−`) is the only assignment that delivers it. `Σ_C = Coh − Str − Grad` is already exactly that split.**

## 2. Independent confirmation from P04, and the sentence that hid the collision

**P04 makes bandwidth non-negative.** So `D(R) = Σ_K b_K^{(L)} > 0` is forced, not conventional.

`Paper_QuadraticStrain_v1` §4 writes:

> $\Phi_N=\sum_K b_K^{(L)}=-\dfrac{GM}{R}$

**That equates a sum of non-negative quantities with a negative number.** It cannot hold as written.

**Under option 2 it becomes consistent immediately:** the potential is `Φ_N = −Str = −Σ_K b_K^{(L)} = −GM/R`, and the minus sign is **P12's own `−Str`**, exactly where it belongs. **§4 silently absorbed P12's minus into the definition of `Φ_N`, and that absorption is what made the `Coh`/`Str` collision invisible for as long as it was.**

**This is a second, fully independent route to the same answer** — it uses only P04's non-negativity and does not touch the sign check's calculus argument at all.

## 3. What changes, and what does not

**Unchanged:** every gravitational result in the corpus. `a_N = GM/R²`, `a_cross = √(a_N a_0)`, `a = a_N + √(a_N a_0)`, the geometric-mean form, the `N(R)` cancellation, Newton, deep-MOND. **The check was against those results, so it cannot move them.**

**Changed — one line of one postulate.** `P-Quadratic-Strain` should read:

> The per-channel participation amplitudes superpose, `P_K^{(a)} = √(b_K^{(a)}) e^{iπ_K^{(a)}}`, and the resulting quadratic form **splits across two P12 terms**: its diagonal `Σ_a b_K^{(a)}` is the strain content `Str_K`, and its off-diagonal `2Σ_{a<b}√(b_K^{(a)}b_K^{(b)})\cosΘ_{ab}` is the coherence content `Coh_K`.

**The postulate's substance survives entirely** — that participation composes as amplitudes rather than additively, and that the cross term is therefore a forced geometric mean, is exactly what §5.2 uses to discharge P14. **Only the destination of the off-diagonal moves.**

**The name is now slightly off.** "Quadratic strain" describes a quadratic form that turns out to live in two terms, one of which is not strain. Not worth renaming a cited postulate; worth a footnote.

## 4. The constructive sign is now required by the slot, not assumed

**This is the check's most useful by-product.**

Under option 2 the cross term sits in `Coh`, which enters `Σ_C` with a **plus**. Given that the MOND correction is observed to be **attractive**, `\cosΘ_{LH} > 0` follows from the assignment. **It is no longer an independent assumption of the gravity arc.**

**Stated at its honest strength:** this is a *consistency requirement* — given option 2 and given that MOND enhances rather than opposes gravity, the sign is fixed. It is **not** a derivation of the phase from the primitives. But it now has **two independent supports**: the structural one here, and `Paper_PhaseCoherence_P12Coh`'s build-verified result that `Coh` rewards phase alignment in 2D and 3D. **Two routes to the same sign, from opposite directions.**

**And that is a real strengthening of `Paper_QuadraticStrain_v1` §9's residual**, which was already discharged in July and which target #24(a) mis-filed as open.

## 5. Actions

1. **`P-Quadratic-Strain` §2** — restate the split (§3 above). **Applied.**
2. **`Paper_QuadraticStrain_v1` §4** — `Φ_N = −Σ_K b_K^{(L)}`, with the minus identified as P12's `−Str`. **Applied.**
3. **`Paper_PhaseCoherence_P12Coh` §5** — the `Coh = |Σ P|²` line corrected to the interference part, matching its own §2. **Applied.**
4. **`Paper_087` §P12** — the pointer added earlier gains the settled assignment. **Applied.**
5. **`Grad` remains the one undefined term in `Σ_C`.** Unaffected by this check, which could not discriminate on it: `Grad` is spherically uninvolved in the two-source problem and identical across all three options.

---

*Foundations staleness #10 CLOSED. Gravity ledger Staleness #71. Check: `internal notes/_check_sigma_sign.py`.*
