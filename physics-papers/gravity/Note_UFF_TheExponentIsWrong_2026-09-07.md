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
