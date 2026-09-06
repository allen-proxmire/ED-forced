# The `ξ` drop is shape, not phase disagreement — and the argument needs no probe

**Date:** 2026-09-06
**Status:** **Confound resolved by reading the code**, with a probe that confirms the mechanism and whose *numbers* are flagged as unfaithful.
**Probe:** `../event-density/theory/p12_fixed_morphology_probe.py` (new; see §4 before using its numbers).

---

## 1. The two parts

The probe does two things at once, and the phase term touches both:

1. **Which cell commits next** — the **shape** of the growing blob.
2. **What phase that cell gets** — the **phase** pattern.

So a falling `ξ` had two possible causes and one number could not separate them: **(a)** the term genuinely makes phases disagree, or **(b)** the term grows a different-shaped blob whose phase statistics differ, with no disagreement involved.

## 2. The answer, and it does not need a simulation

**In every arm of every probe in this line, the deposit rule is identical.** `deposit(v)` takes the mean-field angle of the committed neighbours; **the arm — `Grad`, `coh_v3`, canonical `Coh` — does not enter it.** The arms differ *only* in the bonus used to pick the next candidate.

> **So cause (a) was never available. Two arms handed the same growth order produce bit-identical phase fields. The entire arm-to-arm `ξ` difference is which cells committed in which order.**

**That is a fact about the source, not a result about ED**, and it settles the confound: **the drop is shape.**

## 3. The probe confirms the mechanism

Depositing phases along different growth orders with the same rule, condition (C):

| seed | control order | `Coh` (k=8) order |
|---|---|---|
| 11 | `ξ = 1.30` | `ξ = 1.58` |
| 12 | `1.30` | `1.56` |
| 13 | `1.34` | `1.69` |

**Order alone moves `ξ`, under an identical deposit rule.** That is the mechanism §2 predicts, demonstrated.

## 4. Why the probe's absolute numbers are NOT the live ones — flagged, not used

**My replay flattens `ρ`.** The live run's connection carries `κ_ρ(ρ_w − ρ_v)` where `ρ` **accumulates with every commit**; the replay sets `ρ = 1` on commit and `0` before. **That removes most of the `ρ`-disorder, which is the dominant part of the connection in condition (C).**

**Consequence: the replay's `ξ ≈ 1.3–1.6` are for a much less disordered connection than the live run's, and its apparent direction — canonical arms *above* the control — cannot be compared with the live direction, where they were below.** The replay is faithful about *ordering effects existing*; it is not faithful about *how large they are or which way they point in the real dynamics*.

**Recorded plainly because reporting those numbers as the answer would have been this thread's fifth artifact.**

## 5. What this does to claim 2

**The substance is unchanged; the description changes.**

- **Unchanged:** in the physical condition, under both canonical terms, the resulting substrate has **`ξ < 1`** at strong coupling — the paper's own *"no binding at all."* **A substrate with no phase reach supplies no constructive binding, whatever produced it.** So the problem for the two downstream results that cite that sign — **V5 clock-binding and the MOND interference term** — stands exactly as stated in #107.
- **Changed:** the mechanism is **not** "the canonical terms scramble phases." It is **"the canonical terms steer growth into a front whose phase reach is short."** Those call for different repairs. The first would be a problem with the phase functional; the second is a problem with **what the phase bonus does to the growth rule** — which is a statement about the `Σ`-scoring, not about `Coh` or `Grad` as functionals.

**That relocation is the useful output.** It moves the live problem off the `Coh`-versus-`Grad` question entirely and onto the coupling between the phase term and candidate selection.

> **✅ DONE 2026-09-06 (#109), and §2's claim is now TESTED.** The faithful replay records every `(neighbour, A)` pair per deposit with `ρ` intact, and **reproduces the live `ξ` EXACTLY in all four arms** (`2.13/2.13`, `0.83/0.83`, `0.73/0.73`, `3.83/3.83`). **The mechanism is *where* the front goes, not *what shape* it is:** front coordination is identical across arms (`1.94–1.97`), **but `mean|A|` is `0.362` control, `0.364` old-“Coh”, `0.844` `Grad`, `1.076` canonical `Coh`** — the canonical terms grow into territory with 2–3× the transport connection, and that is what shortens the reach. **A residue remains: control and old-“Coh” have identical connections but `ξ = 2.13` vs `3.83`, so a second, genuine alignment effect exists and is unquantified.** `foundations/Note_FaithfulReplay_2026-09-06.md`.

## 6. What is owed

**A faithful replay** — one that preserves the live `ρ` trajectory rather than flattening it — would give the real size and direction of the shape effect in condition (C). **Until that is run, §3 establishes that shape matters and not how much.**

**Nothing here changes the Knots result** (#107: 0/10 crystal, ten seeds, all readings), which is measured on the live dynamics and is untouched by any of this.
