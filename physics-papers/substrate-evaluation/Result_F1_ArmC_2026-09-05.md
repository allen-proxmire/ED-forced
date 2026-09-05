# F1 Arm C — Result: the arm that worked. Three families, one ranked #1, and an internal inconsistency in `Σ_C` found from outside.

*Run 2026-09-05 on the same three Stage-0-clean families. Axiom block byte-identical to arm B (7,670 chars, verified). Scored against the measures pre-registered in `Seed_F1_ArmC_GapReport.md` before any output was seen.*

**Conflict of interest:** as in A and B, one family is Claude and the scorer is Claude. That family again produced the sharpest single item. **Two of its findings were checked against the corpus before scoring and one was materially corrected by that check** (§6), which is the discipline that matters more than the disclosure.

---

## Verdict

**Arm C returned what arms A and B did not: a usable worklist.** Same models, same axioms, different question — and the yield is not comparable to the two binary arms because it is not the same kind of measurement.

| Measure | GPT | Gemini | Claude |
|---|---|---|---|
| **Y1 — specific actionable gaps** | **15** | 4 | **11** |
| **Y2 — called a *genuine postulate*** | 4 | 2 | 5 |
| **Y2 — called a *hard derivation*** | 2 | 0 | 2 |
| **Structural problems declared** | 1 | 0 | **1** |
| **Y4 — target #24 items reached** | 3 of 4 | 2 of 4 | **4 of 4** |

**Y4 passes. All four known-real weak points were reached across the three runs**, so the calibration condition is met and the novel findings are worth reading.

---

## 1. Y3 — convergence, the primary signal

**Three of three families, independently:**

1. **`V5`'s functional form is under-specified, so no `1/r` follows.** GPT: *"bounded, decaying, retarded is insufficient to determine its infrared Green function."* Gemini: *"bounded and decaying functions natively permit exponential decays, Gaussian distributions, or finite-range cutoffs."* Claude: *"compatible with many profiles (Yukawa, Gaussian, power-law), most of which do not give `1/r²` at all scales."* **This is the T2 wall of arms A and B, now diagnosed rather than merely hit.**
2. **The matter-sources-geometry step is missing, and it is the one that matters.** GPT: *"deriving the Einstein-Hilbert effective action from the substrate"* — not the variation, which is ordinary mathematics. Gemini: *"acoustic metrics do not dynamically evolve via the Einstein-Hilbert action."* Claude: *"there is no relation by which matter content sources curvature … this is not a small missing lemma; it is the entire content of 'why is there gravity'."*
3. **`D01` is unusable as stated.** All three, again, as in arm B.

**Two of three, and both were checked against the corpus (§§5–6):**

4. **Universal free fall does not follow.** GPT: *"the present axioms allow chain-dependent internal structure. Nothing forces that structure to cancel from acceleration."* Claude, more sharply, as a declared structural problem (§5).
5. **`D06` is unusable at label-plus-role granularity.** GPT and Claude both refuse to use it. **Gemini took it on faith and derived from it**, which is the cleanest illustration in three arms of what that family does differently.

## 2. All three ranked the same thing first, by three different routes

**This is the arm's headline.** Asked *"if the authors could supply exactly one thing, what?"*:

- **GPT:** the explicit substrate→infrared coarse-graining map, `S_substrate[…] → S_eff[g,ψ]`, *"crucially, this request does not simply ask the authors to assume GR. It asks them to show whether GR is actually an output."*
- **Gemini:** the coupling principle between substrate strain and Ricci curvature.
- **Claude:** a **Jacobson-type thermodynamic closure** — entropy functional over participation configurations, temperature from `a_C` via Unruh, Clausius relation across substrate causal horizons.

**Same target, three routes.** And the third is worth flagging on its own: **`Paper_GravityAsEquationOfState` and `Paper_KhronometricEquationOfState_Jacobson` are that route, already in the corpus.** A model told nothing about ED recommended, as its single highest-value request, the strategy the corpus actually took. **That is the closest thing any arm has produced to an outside reader independently choosing ED's own approach.**

## 3. Y2 — where the families disagree, and it is the informative part

The `(iii) genuine postulate` versus `(iv) hard derivation` call was the arm's design purpose. **They agree everywhere except one place, and the exception is exactly the corpus's central ambition.**

**Two of three say the gravitational field equation requires a postulate.** Gemini calls it `(iii)` outright. Claude calls the closure `(iii)` and only the passage from it `(iv)`.

**GPT alone holds it open as possibly `(iv)`:** *"if the authors provide the complete microscopic dynamics, metric construction, coarse-graining prescription, and symmetries, it is conceivable that the Einstein-Hilbert action could emerge without being explicitly assumed."* And it names its own falsification condition: *"I would change this from hard derivation to genuine postulate if the authors can show their microscopic construction has no mechanism capable of selecting the Einstein-Hilbert term."*

**That single disagreement is a better statement of ED's open question than the corpus's own framing.** It is not *"can we derive GR?"* — it is *"does the substrate contain a mechanism that selects the Einstein-Hilbert term over `f(R)` and the rest?"* **Nothing in the corpus asks it that way**, and it is answerable.

## 4. `Coh` and `Grad` have no operational definition — and the one `Str` in the corpus contradicts `P-Quadratic-Strain`

**GPT's first boundary, and it checks out worse than GPT could have known.** Its opening move:

> *"P12 names `Coh`, `Str`, and `Grad`, but only D07 gives a computational definition for `Str`. No corresponding functional definition is supplied for `Coh` or `Grad`. Therefore we can expand the strain term, but we cannot actually evaluate `Σ_C`, and hence cannot calculate `a_C`, for a specified substrate configuration."*

**Checked. At the paper level this is correct:** `Paper_087` §P12, `Paper_088`, `Paper_026`, `Paper_027` and `Paper_054` all restate `Σ_C = Coh − Str − Grad` and none defines `Coh` or `Grad`.

**One place in the corpus does define them, and that is where it gets serious.** `Paper_BlindnessInvariant_KnotsNotCrystals` §2 gives the *certified* functional operationally:

> `Σ = k_c·Coh − k_s·Str − k_g·Grad`, with **`Coh = −(ρ_v − ρ_★)²`** (a local density target), **`Str = ρ_v`** (a local density penalty), and **`Grad = |ρ_v − ρ_u|`** (a nearest-neighbour gradient penalty).

**That `Str` is a local commitment density. `P-Quadratic-Strain`'s `Str_K = |Σ_a P_K^{(a)}|²` is a squared modulus of summed complex amplitudes. These are different functionals.** So:

- **The corpus has two incompatible definitions of `Str`**, one used by the simulator line and one by the gravity line, and no paper reconciles them.
- **The certified form carries free coefficients `k_c, k_s, k_g` that the primitive's `Σ_C = Coh − Str − Grad` does not have.**
- **The gravity arc's `Σ_C` therefore has no operational definition at all** — its `Str` comes from `P-Quadratic-Strain`, and its `Coh` and `Grad` come from nowhere.

**This is the most consequential finding of any of the three arms**, it was produced by a model that had never seen either paper, and it is checkable in five minutes by anyone who thinks to look.

## 5. The declared structural problem, and it survives checking in weakened form

Claude declined to file this as a gap, per the seed's second honesty instruction:

> *"Taking P12 literally — `a_C = −grad_adj Σ_C`, with no separate inertial term — and D07's cross term scaling as `√(b_K^A)` in the chain's own bandwidth, two chains with different bandwidth sitting in the same ambient field receive different accelerations. This directly contradicts universal free fall … Supplying [the fix] means amending a primitive, not supplementing the axiom list."*

**GPT reaches the same place independently** and files it as `(iii)`: *"nothing forces that structure to cancel from acceleration."*

**Checked against the corpus, and the check changes the verdict from *contradiction* to *unproven*.** `Paper_MassWithoutMass_BindingInertia` measures inertia natively in the simulator: a bound composite under uniform force reaches `v_x = 0.72` against an unbound cluster's `0.97`, so **binding resists acceleration and ED has inertia as a mechanism.** The run could not know this.

**But the paper's own preamble item 4 concedes the rest:** *"the equivalence-principle reading is a **consistent interpretation, not an independent proof**."*

**So the corrected finding is:** ED has an inertia mechanism and does **not** have a demonstration that it cancels from gravitational acceleration. **Two outside readers independently identified universal free fall as unestablished, and the corpus already agrees in a paper neither had seen.** Not a contradiction — but the one kinematic signature that distinguishes gravity from any other force is, on ED's own admission, an interpretation.

## 6. The `V5` circularity, sharpened

Foundations staleness #6 (from arm A) says V5's definition presupposes Lorentz invariance the primitives do not establish. **GPT files it as a structural item and states the circularity explicitly:**

> *"It becomes a genuine structural problem only if the authors intend Lorentz invariance to be emergent from the same construction while simultaneously using Lorentz invariance to define the microscopic V5 kernel. Then there is a potential circularity: Lorentz structure → V5 → emergent Lorentz structure. That would need to be resolved by distinguishing a primitive discrete invariant from the emergent macroscopic metric."*

**That last clause is the repair, and it is more specific than the corpus's own statement of the problem.** Claude's Gap 1 supplies the standard machinery for the primitive side — Poisson sprinkling at density `ℓ_ED⁻⁴` rather than a regular lattice, which is a `(iii)` postulate that then makes statistical Lorentz invariance a solved `(iv)` derivation.

## 7. What arm C settles about the protocol itself

**The question arms A and B asked was the wrong one.** *"Can a model generate ED?"* had a known answer and produced two negatives whose main value was the material that came out sideways. **Arm C asked for that material directly and returned, in one pass, a ranked worklist with a unanimous first item, a classification of what needs postulating versus what needs work, and one internal inconsistency the corpus did not know it had.**

**The economy measure that dominated arms A and B is absent here and should stay absent.** Counting assumptions rewarded the family that assumed the hard part; **counting gaps rewards the family that read carefully**, and the ordering (GPT 15, Claude 11, Gemini 4) matches the depth of engagement visible in all three arms.

**Recommended standing use:** run arm C's question, not arm A's or B's, on any arc the corpus wants audited from outside. **Give it the arc's stated assumptions, ask where it stops and what it would need, and require the postulate-versus-derivation call.** That is what these systems are good at, and this run cost one paste per family.

---

*Gravity ledger Staleness #69. Seed: `Seed_F1_ArmC_GapReport.md`. Protocol: `Protocol_F1_ColdReconstruction_TwoArm.md` Stage 3.*
