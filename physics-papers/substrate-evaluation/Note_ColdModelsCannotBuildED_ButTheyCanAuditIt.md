# Cold Models Cannot Build ED. They Can Audit It. The Asymmetry Is Structural.

**Allen Proxmire**

**September 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (methods)
**Status:** Methods note, not a physics result. A verdict drawn from eleven runs across two independent frontier model families in three conditions, on 2026-09-04. States what the exercise can and cannot produce, and why the limit is not a prompting problem.
**Anchors:** `Paper_PrimitiveMinimality_IndependentReconstructionProbe.md` (the run data this verdict draws on) · `Gravity_TieredClaims_Ledger.md` Staleness #10–#18 (the audit findings) · `internal notes/PAPER_WRITING_CHECKLIST.md` §9 item 19 and §10 failure mode 6
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative)

---

## Preamble: what this note does NOT claim

1. **This is not evidence about physics.** It is a measurement of what a competent reader without the corpus can and cannot reconstruct, and of what an adversarial reader can and cannot catch.
2. **It does not claim a capability ceiling for models in general.** It claims a limit on *this* task under *these* conditions, and gives the structural reason the limit is expected to persist rather than yield to a better prompt.
3. **Eleven runs, two families, one day.** That is a pointer, not a base rate. §6 states what would overturn the verdict.
4. **The corpus is public.** Training exposure is a live confound for every run; none showed recognition, and its absence is reported rather than assumed.
5. **No run was blind to ED's framing.** Even the blind prompts state P11 in ordinary English. The exercise measures the gap between what ED declares and what a reader must add — never whether ED's starting point is right.

---

## 1. The question

Can a model that has never seen the corpus arrive at Event Density from its premises? And if not, is the exercise worth running anyway?

Eleven runs were used to answer it, in three conditions:

| Condition | Runs | Given |
|---|---|---|
| **Blind construction** | 2 | an ontology sketch in prose; no primitive list, no results |
| **Seeded construction** | 3 | the thirteen primitives with operational content, plus V1/V5, plus named quantitative targets |
| **Adversarial audit** | 6 | a displayed derivation chain and an instruction to find what does not follow |

---

## 2. Blind: not close, and not for a reason a prompt fixes

Neither blind run produced anything ED-specific. Both built the same generic emergent-spacetime scaffold — partial causal order, a coarse-graining regime, hop-count distance, particles as stable patterns, complex amplitudes injected by hand for quantum behaviour — and stopped there. That is the shape of the problem, not ED's answer to it.

---

## 3. Seeded: the wall is in the same place even with the primitives and the kernels in hand

This is the sharper result and the one the verdict rests on. The seeded runs had the thirteen primitives with operational content, V1 and V5 as inherited kernels, and two named targets. **All reached Newtonian scalar gravity with a weak-field clock relation, and all stopped where `Paper_GR-I` begins.**

Three specific steps nobody found:

- **The `N(R)` counting cancellation.** Both full runs *postulated* the `1/R` source profile that `Paper_026`/`Paper_027` derive from the channel count. They held P06 and P08 and did not reach for them.
- **The front-null identification.** Neither separated the rate at which a commitment front advances from the rate at which a clock ticks. That step gives `N² ~ b`, hence `g₀₀g_rr = −1`, hence the Einstein branch rather than the conformal one, hence the factor of two in light bending. One run noticed it could not reach `√(1 − 2GM/c²R)` and parked it; the other did not notice.
- **The dimensional closure to `G`.** One run quoted `ℓ_ED ≈ 1.616 × 10⁻³⁵ m` and used it only for a continuum limit, never connecting it to the gravitational constant.

And an economy result: the best seeded run needed **six** named postulates to reach Newton plus weak-field clocks, against ED's **four**, with ED deriving the `1/R` the run assumed. The gap traces to a route divergence — the runs went Newtonian (a postulated gradient-response law plus a separate inertial law), ED goes geometric (metric, then geodesics) and needs no force law.

---

## 4. Audit: they work, and the reason they work is the reason construction fails

The same families, given displayed chains and told to find what does not follow, performed well. Across six audit runs they located a factor that cancels in a paper's own algebra and is reinstated in prose; a quantity used with two incompatible meanings in one paper; a normalization doing two undeclared jobs; and a dimensional-compatibility step presented as a derivation. One found a discrepancy the in-house symbol sweep had missed, which forced a strengthening of the sweep itself.

They also produced two false positives, both correctly resisted on reading: a codimension label that a paper explicitly redefines, and a dropped phase factor the source paper already flags as its declared open residual.

**The asymmetry has a structural cause.** Auditing is bounded and local — *does this displayed step follow from these stated premises* — and it has an oracle: the algebra either goes through or it does not. Construction in a domain like this has no oracle. A derivation can be internally consistent, dimensionally clean, and simply not about the world, and the missing steps are precisely the ones where no local check exists to guide the search. **That is why better prompting does not close the gap, and why it should not be expected to.**

---

## 5. What the exercise is actually worth

**The divergence, not the convergence.** Where independent readers stop, and what they add, is a measurement of which steps in the corpus are load-bearing and non-obvious — and it is only available from someone who does not already know the answer. Three things it produced that were not available from inside:

- The **front-null identification** is the gravity arc's least-obvious move. Recorded as `Gravity_TieredClaims_Ledger.md` Staleness #11.
- Every unforced addition across the blind runs landed in the **coarse-graining layer**, which is not among the thirteen and is carried in per-paper regime language instead.
- Neither blind run reached for a fundamental spatial dimension, putting two outside votes behind `Paper_087`'s own Round-4 note that P06 is anomalous.

**And one thing worth being straight about.** The only genuinely new physics produced on 2026-09-04 — the horizon-competition threshold for `a₀` (research target #19) — came from *reading the corpus*, not from any model. `Paper_047_5` had the load-bearing ingredient sitting at M3 since July. The models found presentation defects, mislabelled steps and missing pointers. The corpus found the result.

---

## 6. Verdict, and what would overturn it

> **Use them as auditors, and as a probe of the primitive set's minimality. Do not use them as discoverers, and do not expect a prompt that changes this.**

> **F1 is now a pre-registered protocol, 2026-09-05: `Protocol_F1_ColdReconstruction_TwoArm.md`.** It adds a second arm the prior runs lacked. Every seeded run to date was given **the 13 primitives** — but the 13 do not build ED: the corpus ladder puts the declared load at **171** postulates, **26** cross-cutting, with the “38 lines” as the structural spine. **So the prior runs asked whether 13 assumptions generate ED, and that answer was never in doubt.** Arm B seeds all 38 and asks the question actually worth asking. Pass conditions are fixed in advance; the most informative outcome is arm A failing while arm B clears, which would make “the 38 lines build ED” a demonstrated claim rather than a framing.

> **F1 RAN 2026-09-05. Both arms fail. F1 does not fire, and the verdict stands in the strengthened form the protocol pre-committed to.** Three Stage-0-clean families × two arms × two targets: **T1 fails 6/6, T2 fails 6/6.** Adding the constants and the fifteen domain-specific postulates moved **neither** target on **any** family, so **“the 38 lines build ED” is not supported for these two steps** — whatever closes them is in the papers, not the assumption list. **The economy row did not fire either**, and the reason matters: one family used *fewer* assumptions than ED in both arms by **postulating the `1/r` asymptotics**, which is precisely what T2 asks to be derived. **Counting postulates without weighting what each buys rewards assuming the hard part.**
>
> **What F1 produced instead is the auditor half of this note's own verdict, arriving unbidden inside a construction task.** Four findings from models with no access to the corpus: **P12 carries no other-chain dependence** and **V5 presupposes Lorentz invariance the primitives do not establish** (verified; Foundations #5, #6); the **`cos Θ` sign** on the quadratic-strain cross term, which is `Paper_QuadraticStrain_v1` §9's own declared residual, **located from the postulate by a model that had never seen §9**; and `G = c³ℓ_P²/ħ` noticed and correctly declined as *“a consistency check on inputs, not a derivation”*, reproducing gravity Staleness #26. **Not one landed on something the corpus does not already know about itself.** The protocol was built to measure generation; what it actually measured is **the accuracy of ED's own self-assessment**, and on that measure the corpus scores well. **This strengthens §6's headline rather than merely surviving it.**
>
> **The one revision that could change arm B:** three of the fifteen postulates (`D06`, `D08`–`D10`) were seeded at label-plus-role only, and **`D06`, the acoustic-metric guardrails, is load-bearing for the metric-emergence route all three arm-A runs named as the missing bridge.** A rerun seeding the six conditions in full is the honest retest. Until it runs, arm B's negative should be quoted with that limit attached. Scoring: `Result_F1_ArmA_2026-09-05.md`, `Result_F1_ArmB_2026-09-05.md`.

**What would overturn it (F1):** a cold run, on a model family with a training cutoff predating the public repo, that reaches the front-null identification or the `N(R)` cancellation unprompted. That would show the wall is prompting rather than structure. **Ask the recognition question first, in a separate turn** — a run that lands close is more likely to have read the corpus than to have rebuilt it.

**What would sharpen it (F2):** more audit runs on un-audited load-bearing chains. The hit rate to date is roughly two real findings and one false positive per chain, on chains chosen for being load-bearing and unexamined. Whether that holds across the corpus is unknown and is the cheapest thing left to measure.

**What would weaken the audit half (F3):** a run that manufactures a plausible finding on a chain known to be sound. All audit prompts carry the instruction *"if you find nothing, say so plainly; do not manufacture a finding,"* and no run has yet violated it. One that does would mean the audit results need re-reading with that possibility in mind.

---

## 7. Position statement

ED sits in the substrate-ontology lineage ('t Hooft's cellular-automaton interpretation, the causal-set program), and nothing here moves it. What this note adds is a methods result that lineage rarely records: **an outside reader, given the program's own declared inputs and nothing else, reconstructs the shape of the problem and none of the program's distinctive answers — and is nevertheless a good check on whether those answers are stated honestly.**

Read modestly. Eleven runs is a pointer. But the two halves point in opposite directions consistently enough to act on: the construction runs failed in the same place every time, and the audit runs succeeded in the same way every time, and the reason for both is that one task has a local check and the other does not.

---

*End of note.*
