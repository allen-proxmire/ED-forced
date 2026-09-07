# Universal free fall — it reduces to one exponent, and the repair on record uses the wrong one

**2026-09-07.** Worked at AP's direction after the physics audit named this the only genuine open derivation of the four. **Result: the problem is sharper than "unproven", and the fix the corpus has been carrying does not deliver universal free fall either.**

---

## 1. The problem, in the corpus's own terms

Foundations ledger **#9**, reached independently by two of three external runs:

> the cross term scales as `√b_K^{(A)}` in the chain's **own** bandwidth, and `a_C = −∇_adj Σ_C` has **no inertial normalisation**, so two chains of different bandwidth in the same ambient field would accelerate differently.

That is exactly Newton's `m_g = m_i` problem in substrate form. Write the two sides:

**The drive.** `Σ_C = Coh − Str − Grad`, and the interaction lives in `Coh`, whose settled form is `Coh_K = 2Σ_{a<b}√(b_K^{(a)}b_K^{(b)})\cos Θ_ab`. For a test chain `C` in the field of a source `S` the relevant term is the cross term `√(b_C\,b_S)`, so

$$-\nabla_{\mathrm{adj}}\Sigma_C \ \propto\ \sqrt{b_C}\times(\text{source factor}).$$

**The response.** P12 as literally stated sets `a_C` equal to that gradient with **no normalisation at all**, so

$$a_C \ \propto\ \sqrt{b_C}.$$

**A heavier chain falls faster.** Universal free fall fails, and #9 is right that it fails.

---

## 2. The repair on record is the wrong power

The fix carried in #9, from one of the external runs:

$$a_C = \frac{1}{b_C}\Big[-\nabla_{\mathrm{adj}}\Sigma_C\Big]$$

flagged there as *"directly contradicting P12 as literally stated … amending a primitive, not supplementing the axiom list."* **The objection to it has been that it is expensive. The prior objection is that it does not work.**

$$a_C \ \propto\ \frac{\sqrt{b_C}}{b_C} \ =\ b_C^{-1/2}.$$

> **Still bandwidth-dependent — now with a light chain falling faster instead of a heavy one. The repair does not restore universal free fall; it inverts the violation.**

That has not been noticed because the fix was assessed on whether it is *permissible* (it amends a primitive) rather than on whether it is *sufficient*.

---

## 3. There is exactly one exponent that works, and it is the amplitude

Demanding that `a_C` be independent of `b_C` fixes the power uniquely:

$$a_C = \frac{1}{\sqrt{b_C}}\Big[-\nabla_{\mathrm{adj}}\Sigma_C\Big] \ \ \Longrightarrow\ \ a_C \propto \frac{\sqrt{b_C}}{\sqrt{b_C}} = \text{(source factor) alone.}$$

**Universal free fall, exactly: the acceleration depends on the source and not on the falling body.**

**And the surviving power is not an arbitrary one.** ED's participation amplitude is `P = √b\,e^{iπ}` — so **`√b` is the amplitude and `b` is the intensity.** The drive is a *product of two amplitudes* (a cross term), so normalising by the test chain's **own amplitude** leaves exactly one factor of the *source's* amplitude standing. **The structure of the required normalisation is the structure of the interaction that produces the drive.**

> **In one line: gravity is amplitude×amplitude, so inertia has to be amplitude, not intensity. The recorded fix normalised by intensity.**

---

## 4. What this is, and what it is not

**It is not a derivation.** Nothing here shows the substrate *must* normalise by `√b_C`. It shows that **if** universal free fall holds, that is the only available power, and that the power has a natural reading as the chain's own amplitude. The tier is **A → position**, not `D`.

**It is a genuine narrowing.** *"UFF is unproven"* becomes **"UFF holds iff inertia goes as `√b`, i.e. as amplitude"** — one exponent, with a structural candidate for why.

**And it converts a live proposal into a banked negative.** The `1/b_C` repair is refuted on its own terms, before the question of whether amending P12 is affordable arises.

---

## 5. Why the existing measurement cannot settle it

`substrate-evaluation/Paper_MassWithoutMass_BindingInertia` measures inertia natively: a bound composite under uniform force reaches `v_x = 0.72` against an unbound control's `0.97`, so **binding resists acceleration and ED has an inertia mechanism.** That is real and it is why #9 was weakened from *contradiction* to *unproven*.

**But it cannot decide this question, for two reasons, and the paper states the first itself:**

> *"A mass-independent velocity response to a uniform force is what the equivalence principle would give (all masses fall alike), but it is **equally the generic signature of a mobility-saturated response**, so we report it as mass-independent (mobility-saturated), **consistent with — but not evidence for — the equivalence principle**."*

**The second reason is not stated anywhere and is the more fundamental one. The experiment applies a *uniform* force.** Universal free fall is a statement about a **gravitational** drive — one whose magnitude *itself scales with the test body's own coupling*, as `√b_C`. A uniform-force experiment holds the drive fixed while varying the body, so **it cannot see the cancellation, because it has removed one of the two things that must cancel.**

> **The right experiment is not harder, it is different: drive the test chain with a term that carries its own `√b_C`, vary `b_C`, and ask whether the response is `b_C`-independent.** That is a direct test of the exponent in §3, on the existing simulator, and nobody has run it.

---

## 6. Status

| claim | tier |
|---|---|
| P12 as literally stated violates UFF (`a_C ∝ √b_C`) | **D** — algebra on the settled `Coh` form |
| The recorded `1/b_C` repair also violates it (`a_C ∝ b_C^{-1/2}`) | **D** — same algebra; **banked negative** |
| `1/√b_C` is the unique power giving UFF | **D** — forced by demanding `b_C`-independence |
| That power is the chain's own **amplitude**, matching the cross-term structure | **A → position** — structurally suggestive, not derived |
| Whether the substrate actually normalises that way | **OPEN** — and now a single, testable exponent |

**What is owed:** the amplitude-normalised drive test of §5, and then either a derivation of the `√b` normalisation from the primitives or an honest statement that it is a fourteenth commitment.


---

# 7. The owed test was run, and it did not resolve — for a reason worth more than the result

**Run on the certified substrate, unmodified.** `event-density/theory/Higgs_Emergence/uff_amplitude_drive_probe.py` and `..._seeded.py` call `mass_from_binding_probe.run()` as-is; the drive enters `step()` as a scalar, so an amplitude-carrying drive is just `force × √n`, with `b_C ∝ n` by P04 additivity. **No substrate code was touched.**

## Two design failures, each of which would have produced a confident wrong answer

**(1) The first run operated AT the saturation knee.** Calibration showed `v_x` rising steeply to `F ≈ 0.2` and then flat: `0.624 / 0.634 / 0.653` across a 4× force increase. The test ran at `F = 0.2`, so all three drive laws sat in the saturated band, all returned ≈ 0.65, and the probe read that flatness as *"consistent with UFF."* **A saturated response is flat for every exponent, including the wrong ones.** The probe's own guard was too weak: it asked whether the response moves over the *full* force range (it does) rather than *at the operating point* (it does not).

**(2) Below the knee, the seed scatter is comparable to the signal.** The uniform drive gave `0.31 / 0.34 / 0.13 / 0.24 / 0.28` across `n` — non-monotonic with a clear outlier — so the resulting "1.62× amplitude spread" was noise.

## The result at 24 seeds

| `n` | uniform `F` | amplitude `F√n` | drive |
|---|---|---|---|
| 8 | 0.3296 ± 0.0295 | 0.5577 ± 0.0172 | 0.057 |
| 16 | 0.3083 ± 0.0706 | 0.4881 ± 0.0533 | 0.080 |
| 32 | 0.3692 ± 0.0230 | 0.5140 ± 0.0186 | 0.113 |

**Amplitude drive, `n = 8 → 32`: `−0.0438`, `|z| = 1.7`. Not resolved, and the sign is OPPOSITE to the prediction** (§1–3 predict the response should *rise* with `n` under an unnormalised P12).

> **Not banked in either direction.** An underpowered null and a real null are the same number, and 1.7σ against the prediction is not a refutation of the algebra any more than it is a confirmation. *The corpus's own rule — hold a negative to the same bar as a positive — applies to this negative too.*

## Why this simulator probably cannot answer the question at all

**The certified rule is ballistic-or-extinct with `argmax` move selection.** A front *must* advance one cell per step and scores its four neighbours; the drive is an additive bias on that score. So the measured `v_x` is **a selection probability, bounded in `[−1, 1]` by construction** — not an acceleration.

> **The algebra in §1–3 assumes `a ∝ drive`. This substrate has no continuous acceleration to be proportional to anything.** The map from drive magnitude to `v_x` is a bounded, saturating, discrete-choice response, which is why the knee exists at all and why the effect the exponent predicts is compressed toward the ceiling before it can be measured.

**That is the real finding of §7, and it is about testability rather than about UFF.** The owed test as specified — vary `b_C` under an amplitude-carrying drive — is the right *experiment*, and this simulator is the wrong *instrument* for it, because its observable is a probability and the quantity in question is a ratio of accelerations.

## What is owed now

1. **An observable that is an acceleration**, not a per-step selection probability — e.g. momentum accumulated against a restoring term, where the response is unbounded and linear over some range.
2. **Or a substrate implementation with a continuous update** rather than ballistic-or-extinct `argmax`.
3. **Until then §1–§6 stand on algebra alone.** The exponent claim (`1/√b_C` is the unique power giving UFF) and the banked negative (`1/b_C` inverts rather than removes the violation) are both algebraic consequences of the settled `Coh` form and do not depend on this test. **What has not been shown, and is now known to be un-showable on this instrument, is whether the substrate actually behaves that way.**
