# `Grad`: a proposal. Relation / Boundary / Gradient, and the one term that lives on the edge

*Foundations working note, 2026-09-05. Closes the definitional survey opened by `Note_SigmaC_Defined_2026-09-05.md`. **This is a proposal with four supports and one compatibility check, not a derivation.** The tier is stated in §5 and should not be read past.*

---

## 0. The constraint that organizes this

AP's long-standing reading of the three P12 terms:

> **`Coh` = Relation, `Str` = Boundary, `Grad` = Gradient.**

**Two-thirds of that was independently confirmed the same day, by arithmetic that had nothing to do with it.** The three-way sign check (`Note_SigmaC_SignCheck_2026-09-05.md`) fixed the first two terms from `Paper_030`'s established result alone:

$$\mathrm{Coh}_K=2\!\!\sum_{a<b}\!\sqrt{b_K^{(a)}b_K^{(b)}}\cos\Theta_{ab},\qquad \mathrm{Str}_K=\sum_a b_K^{(a)}$$

- **`Coh` is the off-diagonal. It vanishes for a single source and exists only when two contributions meet.** That is *relation*, in the strict sense: no relatum, no term.
- **`Str` is the diagonal — the total bandwidth loaded onto a channel, measured against P04's finite per-locus capacity.** That is *boundary*: the wall the load presses against. It is also exactly how the soft-matter transport arc uses it, as a budget approaching saturation.

**Neither of those was chosen to fit the triad.** They came out of asking which assignment reproduces `a = a_N + √(a_N a_0)`, and only one of three did. **That the survivor matches the author's own reading of the words is a consistency finding worth recording, and it is what makes the third term's reading worth taking seriously rather than guessing at.**

## 1. What the triad determines about `Grad`

`Coh` and `Str` are both **intra-locus**: they are the off-diagonal and the diagonal of the same quadratic form in the participation amplitude `P_K = √b_K e^{iπ_K}`, evaluated where sources meet on one channel at one locus.

**So `Grad` is the only inter-locus term in `Σ_C`, and that is a structural fact rather than a preference.** A locus has channels and it has edges; two of the three terms live in the channels, and the third has nowhere to live but the edges. This also matches P12's own operational content, `a_C = −∇_adj Σ_C` — **an adjacency gradient, which is a difference across edges.**

**Two constraints follow immediately:**

1. **`Grad` must be built from the same object as the other two.** `Coh` and `Str` are quadratic in `P`. A `Σ_C` whose third term is quadratic in something else — a raw density, say — is not one functional but three unrelated ones sharing a plus sign.
2. **`Grad` must vanish when neighbouring loci agree**, and grow with their disagreement. That is what "gradient" means and it is what the certified simulator's `|ρ_v − ρ_u|` implements.

## 2. The proposal

$$\boxed{\;\mathrm{Grad}\;=\;\sum_K\sum_{\langle u,v\rangle}\big|P_K(v)-P_K(u)\big|^2\;}$$

the **discrete Dirichlet form** of the participation amplitude over substrate-graph edges. Expanded:

$$\big|P_K(v)-P_K(u)\big|^2 \;=\; b_K(v)+b_K(u)-2\sqrt{b_K(v)\,b_K(u)}\,\cos\!\big(\pi_K(v)-\pi_K(u)\big).$$

**Four supports, in decreasing order of strength.**

1. **It is the unique natural quadratic edge-difference of the object the other two terms are built from.** Given constraint 1 above, there is essentially one candidate.
2. **It reduces to the simulator's form in the density-only limit.** With phases dropped and `b → ρ`, it becomes `(√ρ_v − √ρ_u)²` — zero when the neighbours agree, positive otherwise, monotone in the difference. Not identical to `|ρ_v − ρ_u|`, but the same object under the tractability reduction the corpus already flags (`Paper_BlindnessInvariant` naming note).
3. **It is compatible with every established gravitational result** (§3).
4. **It generates the graph Laplacian** (§4), which is the operator ED needs and does not currently derive.
5. **INDEPENDENTLY PROPOSED by an external reader the same day, blind.** In the `Σ_C` replication run (`substrate-evaluation/Result_F1_ArmC_SigmaC_2026-09-05.md` §3) a family with none of the supports below wrote: *“`Grad_K(u) = γ Σ_{v∼u} |P_K(v) − P_K(u)|²`, representing the discrete Dirichlet energy of participation amplitudes across adjacent loci”* — **the same object, from the same axioms, and classified `(iii) genuine postulate`, which matches this note's own tier.** **The strongest support here: the others are internal arguments; this is a second reader reaching the same object and agreeing on its status.**
6. **→ STRENGTHENED 2026-09-05: that operator is already a derived corpus result, and the support runs both ways.** `layers/layer_2/OneOperator_TheLaplacian.md` establishes that **every layer-2 decorrelation term across the map is the same operator**, the gradient-flux Laplacian `∇·(M∇φ)`, **forced** by isotropy + locality + conservation. **`Grad` is the layer-1 object that coarse-grains to it** — which gives `Grad` a support that connects to a derived result rather than to a naming intuition, and gives the layers program a **substrate origin** for an operator it currently obtains only from a symmetry argument about the CG step. **Either strengthens or kills both together.** `layers/Note_TheSeam_And_SigmaC_2026-09-05.md` §2.

## 3. The compatibility check

**The obvious way for this proposal to die is that it wrecks Newton. It does not.** `internal notes/_check_grad_compat.py`, re-runnable.

With `b^{(L)} ∝ GM/R`, the amplitude is `P ∝ √(GM/R)`, and the per-edge Dirichlet contribution is `|dP/dR|²ℓ_ED² = ¼\,ℓ_ED²\,GM/R³`. Since `Σ_C` carries `−Grad`, the acceleration picks up `+d\mathrm{Grad}/dR`:

$$a_{\mathrm{Grad}} \;=\; -\tfrac34\,\frac{\ell_{\mathrm{ED}}^2\,GM}{R^4}$$

| R | `a_Newton` | `a_Grad` | ratio |
|---|---|---|---|
| `10⁷ m` (neutron star) | `−1.34e+06` | `−2.61e−78` | `2.0e−84` |
| `1.5×10¹¹ m` (1 AU) | `−5.93e−03` | `−5.16e−95` | `8.7e−93` |
| `10¹⁹ m` (galactic) | `−1.34e−18` | `−2.61e−126` | `2.0e−108` |

**Suppressed by `ℓ_ED²/R²` — between `10⁻⁸⁴` and `10⁻¹¹²` across every scale that matters. Nothing is touched to any conceivable precision.**

**Two things worth noting rather than passing over.** The contribution is **attractive**, and that is not automatic: it follows from the Dirichlet form being non-negative, entering with a minus, and `b^{(L)}` falling with `R`. **A `Grad` built from bandwidth difference rather than amplitude difference gives a different power and, for some choices, the wrong sign** — so the check does discriminate among candidates, even though it cannot confirm the winner.

## 4. What it would buy, stated as a lead and not a result

`Σ_K Σ_{⟨u,v⟩} |P_K(v) − P_K(u)|²` is the standard quadratic form of the **graph Laplacian**, and it is what produces `∇²` in a continuum limit.

**ED needs exactly that operator and does not currently derive it.** `Paper_026`/`Paper_027` require `∇²b ∼ ρ`, and F1 arm C's most-converged gap — named by all three families — was that no source law follows from the axioms as stated. GPT put it as *"no derived source law ⟹ no derived 1/r potential ⟹ no derived 1/r² gravity."*

**This is a lead, not a claim.** A Dirichlet form gives you a Laplacian; it does not by itself give you `∇²Φ = 4πGρ`, which additionally needs the source identification the same arm-C runs flagged as missing. **But it is the first place in the corpus where the operator would come from somewhere rather than being assumed**, and that makes it worth pursuing on its own account.

## 5. Honest tier, and the open item this raises

**Tier: proposal, form-forced-conditional at best.** Nothing here derives `Grad` from the primitives. What is established is that this form (i) is the natural quadratic edge-difference of the amplitude, (ii) reduces to the simulator's rule under the known reduction, (iii) does not break anything, and (iv) would supply an operator ED needs. **That is four reasons to adopt it provisionally and no reason to call it derived.**

**And it raises an item that should not be buried.** The phase half of the Dirichlet form is `−2√(b_v b_u)\cos Δπ`, which enters `Σ_C` as `+2√(b_v b_u)\cos Δπ` — **so `Σ_C` is raised when phase is aligned *across an edge*.**

**That is what `Paper_PhaseCoherence_P12Coh`'s simulator actually measures.** It deposits phase from **committed neighbours across edges** via the P05 connection, and finds alignment rewarded with finite reach. **So the measured phase-alignment result may belong to `Grad` rather than to `Coh`.**

**Nothing breaks either way** — both terms reward alignment, both come from the same amplitude structure, and the sign check settled `Coh` versus `Str` from the gravity target independently of any of this. **But which term that measurement belongs to is now genuinely open, and it bears on the `cos Θ` discharge**, which currently cites the measurement as one of its two supports. **Flagged, not resolved.**

## 6. What would settle it

- **Kill:** a substrate argument that `Grad` must read a quantity other than the participation amplitude — or a demonstration that the Dirichlet form's `1/R⁴` correction has the wrong sign under a more careful treatment of the edge sum.
- **Confirm:** a derivation of `∇²b ∼ ρ` from this form plus a source identification, which would simultaneously close arm C's most-converged gap.
- ~~**Cheapest next check:** re-run the probe with the phase assigned to `Grad`.~~ **RUN 2026-09-05, same day. Result: split, and the open item does NOT close.** In the **physical case (C)** — quenched bandwidth *and* `ρ`-field holonomy — **finite-reach survives under the `Grad` assignment**, so the `cos Θ` discharge keeps both supports. **But in condition (A)** — bandwidth holonomy alone — **the `Grad` reading CRYSTALLIZES** (`R ≈ 0.9`, `ξ` = grid) at every non-zero coupling, where the `Coh` reading stays finite-reach. **So each reading now has a crystallizing sub-case, each defended by the same argument the July arc used for its own, and Knots-safety cannot discriminate.** **→ THE KNOWN PROBLEM IS NOT `Grad`-SPECIFIC, 2026-09-06 (#105):** with the `Coh` arm corrected to canonical form, **condition (A) crystallizes under BOTH readings** — the asymmetry that made this look like a `Grad` defect was the `/n`. **So the one recorded reason to prefer the `Coh` reading is withdrawn**, and (A)-crystallization is a property of the phase-coherence operationalization rather than of this proposal. **The physical case (C) stays finite-reach under all three arms**, which is what the July arc rests on. *(Original text follows.)* **The proposal above therefore has a known problem it did not have when written**, and its tier is unchanged: one passed test in the physical case, one failed test in a partial one. ~~**A new discriminator did appear:** `ξ`'s response to coupling strength — **flat (≈ 4) for `Coh`, monotonically shrinking (`2.2 → 0.8`) for `Grad`.**~~ **WITHDRAWN 2026-09-06 — it was measuring the growth front, not the phase.** The cleaner probe this note asked for was run: **a phase-blind control rewarding coordination number alone, with the phase information deleted, reproduces the shrinkage (`2.0 → 0.6` against `Grad`'s `2.2 → 0.8`).** **A coordination-number artifact of extensivity.** `foundations/Note_GradPhase_Decomposed_2026-09-06.md`; gravity ledger #103. Full reading, including the honest limit that the extensive form conflates alignment with coordination number: `foundations/Note_PhaseInGrad_Probe_2026-09-05.md`; gravity ledger Staleness #73.

---

*Gravity ledger Staleness #72. Checks: `internal notes/_check_grad_compat.py`, `internal notes/_check_sigma_sign.py`.*
