# The seam and `Σ_C`: `Grad` is the substrate origin of layer 2's one forced operator, and the corpus has two decorrelations under one name

*Layers working note, 2026-09-05. **Written after being wrong about what was here.** Connects the day's `Σ_C` work and the `a₀` `2π` route to the existing layers program. **No new framework — the framework existed and neither arc was citing it.***

---

## 0. The correction that produced this note

I recommended writing the layer seam up "as its own object," on the stated grounds that *"nothing in the corpus currently treats the layer seam as a single object."*

**That was wrong.** `layers/` has a README, a synthesis (`Synthesis_TheDivideIsTheArrow.md`), an Atlas sweep, and per-layer folders. **It treats the seam as a single object and has a thesis about it** — *the divide is the arrow* — plus a sharper result underneath (§1). **What is actually true is narrower and more useful:** the two arcs that ran into the seam today, gravity's `2π` and state-reduction's `Θ₁₂`, **cite none of it.**

**So this note connects rather than founds.** The value is in §§2–3, which are new; §1 is a summary of what was already here.

## 1. What the layers program already says

**The seam has known content.** `layers/README.md`: *"Going layer 1 → layer 2 always adds **decorrelation** — molecular chaos, independence, mixing, scattering. It is the step where the arrow is averaged out and the symmetry is manufactured."*

**And the decorrelation is one operator, forced.** `layer_2/OneOperator_TheLaplacian.md`: every layer-2 decorrelation term across the map is the gradient-flux Laplacian `∇·(M∇φ)` — diffusion, NS viscosity, and Ricci/gravity smoothing are three instances, Gaussianity is its heat kernel. **It is forced by isotropy + locality + conservation, which make it unique.**

**And its absence is measured too.** The layer-1 deposit field stays **non-Gaussian** *"precisely because it does not undergo this Laplacian smoothing — it keeps the committal phase structure."*

## 2. New: `Grad` is the substrate origin of that one operator

`foundations/Note_Grad_Proposal_2026-09-05.md` proposes

$$\mathrm{Grad}=\sum_K\sum_{\langle u,v\rangle}\big|P_K(v)-P_K(u)\big|^2$$

the discrete Dirichlet form — **whose variation is the graph Laplacian.** The proposal listed that as support #4, phrased weakly: *"it generates the graph Laplacian, which is the operator ED needs and does not currently derive."*

**Set against `OneOperator_TheLaplacian` it is much stronger than that, and the support runs both ways.**

- **For `Grad`:** the corpus independently established, by a symmetry argument at layer 2, that the decorrelation add is *exactly one operator*. **`Grad` is the layer-1 object that coarse-grains to it.** That is a fifth support, and unlike the other four it connects to a *derived* corpus result rather than to a naming intuition or a compatibility check.
- **For the layers program:** `∇·(M∇φ)` is currently **forced at layer 2** by isotropy, locality and conservation — an argument about what the coarse-graining *must* produce, with no substrate object behind it. **`Grad` would give it one.** The operator would stop being a constraint on the CG step and become the coarse-grained form of a term already sitting in P12.

**Stated at honest strength:** `Grad` is a **proposal** (`form-forced-conditional at best`), so this is a link between a proposal and a derived result, not between two derived results. **But it is a link that either strengthens or kills both together, which is worth more than a fifth independent support.**

**And the consistency check it invites is cheap:** the layers program measures that layer-1 fields keep committal phase structure while layer-2 fields are Laplacian-smoothed. If `Grad` is the Dirichlet form, **`Grad`'s own phase term should be the thing that gets smoothed away at the seam.** That is checkable against the Gaussianity result on both sides.

## 3. New: the corpus has two decorrelations and one name for them

**This is what resolved the `Θ₁₂` question's vocabulary, and it should be recorded separately from that question.**

- **The layer-2 add.** Molecular chaos, independence, mixing. **Statistical**, arrow-*erasing*, manufactured by the second coarse-graining. This is the one the layers program names.
- **A layer-1 intrinsic decorrelation.** `substrate-evaluation/Paper_PhaseCoherence_P12Coh` **measures** the P05 connection carrying the substrate's own **quenched geometric disorder**, random-walking the raw polarity to `ξ ≈ 4–6` lattice units. **Geometric**, not statistical; it happens *below* the seam and does not average the arrow away — the July arc's whole point was that the resulting order is finite-reach rather than crystalline, which is a structural property, not a thermal one.

**These are different objects with the same word.** One is what crossing the seam *adds*; the other is what the substrate *already has*. **The corpus names only the first**, which is why `state-reduction/Note_Theta12_LayerQuestion_2026-09-05.md` had to invent the distinction to state its fork.

**Consequence for `Θ₁₂`:** the layer-2 decorrelation is **not** what would randomize it — that add erases the arrow and produces Gaussianity, and the layers program measures layer-1 fields *keeping* their phase structure through it. **What bears on `Θ₁₂` is the layer-1 geometric decorrelation at `ξ`.** That narrows the fork usefully: the question is not *"does crossing the seam randomize the phase?"* but ***"is `Coh` evaluated on raw polarity, which carries `ξ`, or on the coarse-grained holonomy, which does not?"***

## 4. What the layers program does not answer

**Two things, and both are the live debts:**

1. **The direction of the `2π`.** `gravity/Note_a0_TwoPi_RepairRoutes` §4f owes: *given that we compare at layer 1, why does the seam contribute `1/2π` rather than `2π`?* **The layers program says what the seam adds — decorrelation, one operator — but says nothing about a numerical factor attaching to a crossing.** §4b's reading of the `2π` as *"the layer-crossing factor"* is not supported by anything in `layers/`, and it is not contradicted either. **It is simply a different claim about the same seam.**
2. **Which layer `Coh` is evaluated at.** §3 narrows it; it does not settle it.

**Recording that plainly matters**, because the temptation after §2 is to treat the seam as now understood. **It is understood for the dissipative column, where it has a forced operator and measured instances. It is not understood as a carrier of numerical factors, which is what both of today's arcs need.**

## 5. Tier

**Everything in §1 is cited, not claimed.** §2's link is between a **proposal** and a derived result — it strengthens both conditionally and settles neither. §3 is a **distinction**, not a result: it names two things the corpus was calling one thing, and the evidence for both halves is already in the corpus (`layers/README.md` for the first, `Paper_PhaseCoherence_P12Coh`'s measurement for the second). §4 is a statement of what is missing.

**Nothing here should be cited as closing either arc's debt.**

---

*Gravity ledger Staleness #76. Companions: `foundations/Note_Grad_Proposal_2026-09-05.md`, `state-reduction/Note_Theta12_LayerQuestion_2026-09-05.md`, `gravity/Note_a0_TwoPi_RepairRoutes.md` §§4f–4g, `layer_2/OneOperator_TheLaplacian.md`.*
