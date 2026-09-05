# Protocol F1 — Is the Wall Prompting or Structure? A Two-Arm Cold-Reconstruction Test

*Pre-registered 2026-09-05. Fires falsifier **F1** of `Note_ColdModelsCannotBuildED_ButTheyCanAuditIt.md`. Not yet run.*

---

## Preamble: what this protocol does NOT do

1. It does **not** test whether an AI can invent ED. That question is settled negatively and is not interesting.
2. It does **not** treat a pass as evidence for ED's correctness — only for its *reachability* from a stated assumption set.
3. It is **pre-registered**: §4's pass conditions are fixed before any run. Scoring after seeing output is how this exercise goes wrong.

---

## 1. What F1 asks

The standing verdict is that cold models cannot construct ED and the wall is **structural**, not a prompting artifact. F1 is the condition that would overturn it:

> a cold run, on a model family with a training cutoff predating the public repo, that reaches **the front-null identification** or **the `N(R)` cancellation** unprompted.

**A design flaw in the prior runs, and the reason for arm B.** Every seeded run was given **the 13 primitives**. But the 13 do not build ED — the corpus's own ladder puts the declared load at **171** named postulates, **26** of them cross-cutting, with the "38 lines" (13 primitives + 10 constants + 15 postulates) being the structural spine and not the generative set. **So the prior runs tested whether 13 assumptions generate ED, and the honest answer to that was never in doubt.** Arm B tests the question actually worth asking.

## 2. The two target steps

Both are load-bearing, both were missed by every prior seeded run, and both have an objective yes/no.

**T1 — the front-null identification.** Separating *the rate at which a commitment front advances* from *the rate at which a clock ticks*. This yields `N² ~ b`, hence `g₀₀g_rr = −1`, hence the **Einstein branch** rather than the conformal one, hence the factor of two in light bending. A run that lands the conformal branch has **not** hit T1.

**T2 — the `N(R)` counting cancellation.** Deriving the `1/R` source profile from the holographic channel count `N(R) = 4πR²/ℓ_ED²`, rather than postulating it. Every prior full run **postulated** what `Paper_026`/`Paper_027` derive. A run that writes `1/R` as an assumption has **not** hit T2.

## 3. Stages

### Stage 0 — Contamination screen (mandatory, separate session, no prior context)

> **⚠ The first draft of this screen was defective and is recorded here rather than quietly replaced.** It read:
> *“What can you tell me about the Event Density framework in physics — its primitives, and any relation it proposes between the MOND acceleration scale and the Hubble constant?”*
> **That prompt leaks the central claim it is screening for.** It tells the model that a framework called Event Density has *primitives* and proposes *a relation between the MOND acceleration scale and the Hubble constant* — which is `a₀ ~ cH₀`, the thing arm A and arm B exist to see whether a model can reach. A model answering *“I don't recognise it”* would nonetheless **hold the idea**, and could reason to `a₀ ~ cH₀` from the screen alone. **A contamination screen that discloses the target contaminates every run downstream of it.** Caught 2026-09-05 before any run.

**The screen must be closed: it must not disclose what it is testing for.** Two properties are required — no content leakage, and a check on whether the model's *recognition claims* are reliable at all.

**Ask this, verbatim, in a session that is never used for either arm:**

```
I'm checking which of these physics frameworks you have encountered.
For each, reply either "not familiar" or give a two-sentence description
of its core commitments. Do not guess: if a name is unfamiliar to you,
say so plainly rather than inferring what it might mean.

1. Causal Set Theory
2. Event Density
3. Relational Bandwidth Cosmology
4. Shape Dynamics
5. Participation Kinematics
```

**Why this list.** **1** and **4** are real, well-documented programmes — a competent model should describe both, and failure to do so means the screen is not measuring recall. **3** and **5** are **invented**, and exist to detect confabulation: a model that produces a confident description of either has demonstrated that its recognition claims carry no information, and its *negative* on item 2 is therefore worthless. **2** is the target, buried among four others so that nothing marks it as the one that matters.

**Discard rules — applied before any arm is run:**

| Result | Action |
|---|---|
| Describes **Event Density** with substrate / primitive / bandwidth / `a₀`–`H₀` content | **Contaminated.** Discard the family from both arms. |
| Confabulates on **3** or **5** | **Recognition unreliable.** Discard — a negative from this family cannot be trusted. |
| Fails to recognise **1** or **4** | **Screen not measuring recall.** Discard, or re-run with better-known controls. |
| Not familiar with **2**, **3**, **5**; describes **1** and **4** | **Clean. Proceed to arm A.** |

**Record the verbatim answer either way**, including the clean negatives — those are the result that licenses everything downstream.

**Even a clean screen is run in a throwaway session.** The word *“Event Density”* has still appeared in that context, and the arms must not inherit it.

### Stage 1 — Arm A (13 primitives) — the control

Seed: the thirteen primitives with operational content, V1 and V5 as inherited kernels. No constants, no paper-specific postulates. **This replicates the known condition** and exists to confirm the wall is where prior runs put it, on an uncontaminated family.

### Stage 2 — Arm B (the 38 lines) — the new arm

Seed: **all 38** — the 13 primitives, the 10 constants (`c`, `G`, `a₀`, `Λ`, `ħ`, `ℓ_P`, `H₀`, masses, couplings, `α`), and the 15 postulates carried in `Core Theory` rows 24–38 (`P-RB-1`, `P-Quadratic-Strain`, `P-Gauge`, `P-QD-LiveWeight`, `P-YM-Action-Coarse-Graining`, `P-OS-Reflection-Positivity`, `P-Profile-Rescaling`, the six acoustic-metric guardrails, V5 existence, the tensor-product composition, the monogamy budget cap, Tsirelson placement, E-1 factorisability, the `a₀`/`ξ_canonical` shared-origin postulate).

**Withhold in both arms:** `Paper_026`/`027`'s channel-count derivation, anything naming the front-null step, and every `GR-` paper's content.

### Task prompt (identical in both arms)

> *"From the assumptions above and standard mathematics, derive as much of gravitation as follows. State every additional assumption you must introduce, name it, and list them at the end. Where you cannot derive something and must postulate it, say so explicitly rather than asserting it. If a step does not follow, say plainly that it does not — do not manufacture a derivation."*

## 4. Pass conditions — fixed in advance

| Outcome | Meaning |
|---|---|
| **Arm A reaches T1 or T2** | **F1 fires.** The wall was prompting, not structure. The standing verdict is overturned and the note must be rewritten. |
| **Arm A fails, Arm B reaches T1 or T2** | **The most informative outcome.** The 13 underdetermine ED; the 38 generate it. That would make "the 38 lines build ED" a *demonstrated* claim rather than a framing, and it is the strongest available argument for the corpus's own structure. |
| **Both fail** | The wall is deeper than the assumption list, and the verdict stands in a strengthened form: **not even ED's own stated spine reaches these steps without the papers.** |
| **Arm B reaches neither, but needs ≤ 4 postulates** | Economy parity. Interesting and worth recording, but not a pass. |

**Secondary measure, recorded in every run:** the count of named postulates the run introduces. Baseline: the best prior seeded run needed **six** to reach Newton plus weak-field clocks; ED uses **four** and derives the `1/R` the run assumed.

**Scoring is binary and mechanical.** T1 = did it separate front-advance rate from clock rate and reach `g₀₀g_rr = −1`? T2 = did it *derive* `1/R` from a channel count? Anything else is a fail, however impressive.

## 5. Run discipline

- **Three families minimum**, ≥ 2 runs each, fresh sessions, no cross-talk.
- **Both arms on the same family**, so arm A is a true control for arm B.
- **Verbatim transcripts recorded**, including failures and refusals.
- **Prompt defects disclosed** in the write-up, per the probe paper's §6 — every prior run's write-up carries this and the practice is what makes the negatives trustworthy.
- **No re-prompting toward the target.** A hint that lands T1 invalidates the run: that is the exact confound F1 exists to remove.

## 6. What this cannot settle

A pass shows the steps are *reachable from stated assumptions*, not that they are *right*. A fail shows they are not reachable **by these families, at this size, from this seeding** — not that they are unreachable in principle. Neither outcome bears on whether ED is true; both bear on whether ED's assumption set is generative in the way the corpus's framing implies.

**And the asymmetry stands regardless.** Auditing has a local oracle — *does this step follow from those premises* — and construction does not. Nothing in this protocol changes that; it tests only where the construction wall sits.

## 7. Falsification of the protocol itself

- If a run manufactures a plausible-looking derivation on a step it did not take, the anti-manufacturing instruction has failed and **all** audit-side results from that family need re-examination.
- If arm A and arm B produce indistinguishable output, the seeding difference is not doing work and the two-arm design is void — report that, do not quietly merge the arms.
