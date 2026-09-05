# F1 Arm A — Result: the wall replicates on clean ground. F1 does not fire.

*Run 2026-09-05 on the three families cleared by Stage 0. Scored against the pre-registered targets in `Protocol_F1_ColdReconstruction_TwoArm.md` §4. Seed: `Seed_F1_ArmA_13Primitives.md`.*

---

## Declared conflict of interest

**One of the three families is Claude, and the scorer is Claude.** That family came closest on T2 and produced the sharpest criticisms of ED's primitive set. **Every judgment favouring it below should be read against that.** The T2 scoring is mechanical (derived vs postulated) and Claude fails it on its own explicit statement, so the conflict does not change the verdict — but it is recorded rather than left for a reader to notice.

---

## Verdict

| Target | GPT | Gemini | Claude |
|---|---|---|---|
| **T1 — front-null identification** | FAIL | FAIL | FAIL |
| **T2 — `N(R)` cancellation** | FAIL | FAIL | FAIL |
| Named additional assumptions | **14** | **3** | **8** |

**F1 does not fire.** No clean family reached either target from the 13 primitives. **The wall sits exactly where every prior seeded run put it, now replicated on ground screened for contamination.** The standing verdict of `Note_ColdModelsCannotBuildED_ButTheyCanAuditIt.md` stands and is strengthened: the wall is structural, not a prompting artifact, and not an artifact of the runs having seen the corpus.

## T1 — nobody was near it

None of the three separated *the rate at which a commitment front advances* from *the rate at which a clock ticks*. None reached `g₀₀g_rr = −1`. Two (GPT, Claude) concluded no metric emerges from the primitives at all; the third (Gemini) **assumed** a metric in its Step 1 and never revisited the question. **The step was not approached, not attempted-and-missed.**

## T2 — all three identified the gap; none crossed it

This is the informative half, because the failures differ.

- **GPT analysed the gap precisely and declined to fill it.** Its §4 states *"3 spatial dimensions alone do not derive the inverse-square law"*, and identifies exactly what is missing: the flux premise `4πr²g(r) = constant` *"does not occur in P01–P13 or V1/V5"*. It then lists **A7 — flux conservation / Gauss law** as an explicit addition. It reached Newton only by postulating `Σ(r) = −κM/r` and said so: *"that form is an additional assumption."*
- **Gemini postulated the answer and labelled it.** Its Step 2 assumes V5 *"acts as a long-range propagator"* and applies the 3D Laplacian Green's function `G(r) = 1/4πr`. Its own **A1** states the assumption plainly: *"The cross-chain kernel V5(r) approaches a 1/r spatial dependence at macro distances."* **That is the postulate ED derives.**
- **Claude came closest and still declined.** Its **A6** names the route: *"ambient bandwidth density falls off with the causal-graph analogue of area (using P06's 3-space, hence 4πR² spheres), giving inverse-square by a flux/conservation argument"* — and immediately rules it out as a derivation: *"Neither is derived; (i) is at least a semi-motivated route using P06's stated area formula, but it is an addition, not a consequence."*

**So the shape of the `N(R)` argument was visible to one run, named, and rejected as unlicensed.** That is a sharper negative than "nobody thought of it": the route is findable and the primitives as stated do not license taking it.

## Assumption economy — the count is misleading and must not be quoted alone

Baseline: the best prior seeded run needed **six** additional postulates to reach Newton plus weak-field clocks; ED reaches the same place on **four**, deriving the `1/R` the runs assume.

**Gemini's 3 is fewer than ED's 4 and is not a better result.** It reached Newtonian gravity with three assumptions *by assuming the hard parts wholesale* — the `1/r` asymptotics (A1), the bandwidth-mass equivalence (A2), and the metric coupling (A3). Counting assumptions without weighting what each one buys rewards exactly the wrong thing.

**The honest comparison is: assumptions needed to reach the same place with `1/R` derived rather than assumed.** On that measure no run competes, because no run derived it.

## Three findings about ED, produced inside a construction task

The runs were asked to build. What they returned that has value is criticism — consistent with the standing verdict that these systems are strong where a local check exists.

**1. P12 as canonically stated describes single-chain self-dynamics and cannot express a two-body interaction.** Claude: *"Coh, Str, Grad are undefined functions of a single chain C — there's no stated dependence on other chains' bandwidth at all, so as written this cannot even represent a two-body gravitational interaction, let alone reproduce an inverse-square law."* **This is checkable against `Paper_087` §P12 and appears to be correct as stated.** The corpus supplies the other-chain dependence downstream, but the primitive as written does not carry it.

**2. V5's definition presupposes structure the primitives do not establish.** Claude: V5 is defined on *"the Lorentz-invariant separation"*, but *"nothing in P01–P13 establishes that the substrate has emergent Lorentz symmetry."* **The kernel's definition imports a result the primitive layer has not earned.** This is a genuine circularity flag on the kernel layer, raised without any knowledge of ED's own literature.

**3. P12 is already force-law-shaped, so deriving gravitation from it is partly circular.** All three noted it; Claude most directly: *"the axiom set already hands you 'acceleration = negative gradient of a scalar functional' … this is literally Newton's second law with `Σ_C` playing the role of potential energy."* GPT's version: *"P12 does not specify what produces `Σ_C`."*

**None of these three is a manufactured finding**, and all three are checkable against the corpus. **They are the arm's most valuable output and they were not what it was testing for.**

## Protocol checks

- **F3 (anti-manufacturing) PASSES.** No run manufactured a derivation. All three stated plainly and repeatedly where steps did not follow — GPT: *"claiming a derivation of gravitation would manufacture the missing physics"*; Claude: *"I did not find a legitimate derivation path I was withholding."* The instruction held on all three families.
- **No re-prompting occurred.** Single paste, no follow-ups, no hints. The runs are clean.
- **Capability parity confirmed downstream of Stage 0.** All three produced competent, structured physics. The negative is not a weak-model artifact.

## What this licenses, and what it does not

**Licensed:** the wall is structural. Three uncontaminated families, given ED's 13 primitives with operational content and both kernels, independently stop at the same place and independently identify the same missing bridge — a map from substrate participation to an effective source density and geometry.

**Not licensed:** any claim that ED's derivation of that bridge is *correct*. The runs show the step is not forced by the primitives. ED's papers take it via the channel count; that this is a real derivation rather than a differently-dressed postulate is a separate question this arm does not touch.

**Consequence for arm B.** Arm B is now the live question and is worth building: the 13 demonstrably underdetermine ED, and whether the **38** close the gap is exactly what remains unknown. Note in advance that arm B seeds `P-RB-1` and the acoustic-metric guardrails, which bear directly on the metric-emergence gap all three runs identified — so arm B has a real chance of moving, and a pass there would make *"the 38 lines build ED"* a demonstrated claim.
