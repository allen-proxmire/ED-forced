# Penrose's collapse energy is `−Σ_C`: the density-matrix correspondence, made quantitative

*State-reduction working note, 2026-09-05. Follows `foundations/Note_PhaseInGrad_Probe_2026-09-05.md` §5. **Tier: D-via-I** — derived given two prior corpus commitments, stated in §5.*

---

## Verdict

$$\boxed{\;E_\Delta \;=\; \mathrm{Str}-\mathrm{Coh} \;=\; -\big(\Sigma_C+\mathrm{Grad}\big)\;\approx\;-\,\Sigma_C\;}$$

**Penrose's collapse energy is minus the ED stability landscape of the two-branch configuration.** The identity is exact, all three limiting cases come out right, and the sign is correct for an instability.

**Consequence for the arc:** `τ ≈ ħ/E_G` becomes **`τ ≈ −ħ/Σ_C`**. The collapse rate stops being an imported Penrose formula and becomes a statement about ED's own functional.

**And it answers a flag the arc has carried since July** (§4), while **partly discharging flag C4** (§5).

---

## 1. The identity

For a two-branch superposition — index `a` running over **branches** rather than source regions — the settled P12 split gives

$$\mathrm{Str}=b_1+b_2,\qquad \mathrm{Coh}=2\sqrt{b_1b_2}\,\cos\Theta_{12}.$$

Penrose's collapse energy is the self-energy of the *difference* of the two mass distributions:

$$E_\Delta=-G\!\iint\!\frac{[\rho_1-\rho_2](\mathbf x)\,[\rho_1-\rho_2](\mathbf y)}{|\mathbf x-\mathbf y|}\,d^3x\,d^3y \;=\; E_{11}+E_{22}-2E_{12}.$$

**Diagonal minus twice the cross term — which is `Str − Coh` exactly.** Verified term by term across six configurations (`internal notes/_check_collapse_correspondence.py`); the match is to machine precision because **it is the same expansion of the same square.**

**Two identifications carry it, and both are already in the corpus:** `b_K^{(a)}` as the branch's own gravitational potential content (`Paper_030` §4.2, `b^{(L)} ∝ GM/R`), and `√(b_1b_2)\cosΘ` as ED's mutual term. **Neither is introduced here.**

## 2. The limits, which is where a wrong correspondence would show

| Configuration | `E_Δ` | `Σ_C` | Correct? |
|---|---|---|---|
| Branches identical, in phase | `0` | `0` | **Yes.** No separation, no collapse pressure — `1/τ = E_Δ/ħ` vanishes when there is nothing to collapse between. |
| Branches maximally distinguishable | `4b`, maximal | `−4b` | **Yes.** Fastest collapse at greatest separation. |
| One branch vanishing (`b_2 → 0`) | `→ b` | `→ −b` | **Yes.** A lone branch has no interference to destroy. |

**And the sign is right for an instability.** `Σ_C = \mathrm{Coh}-\mathrm{Str} \le 0` throughout for a two-branch state, **zero only at perfect coherence.** So a superposition sits at `Σ_C = 0` and commitment drives it down. **That is what P12 says an unstable configuration looks like**, and it is not something the correspondence was arranged to produce.

## 3. What this does to the collapse rate

`StateReduction_CollapseRate_ED_Derivation` derives `E_G τ ∼ ħ ⟹ τ ≈ ħ/E_G` from the branch-clock difference. Substituting:

$$\tau \;\approx\; \frac{\hbar}{E_\Delta} \;=\; \frac{-\hbar}{\Sigma_C}.$$

**The rate is now driven by the P12 landscape of the superposed configuration** — the same functional that gives the corpus its gravity, evaluated on two branches instead of two source regions. **Nothing new is postulated to get there.**

## 4. It answers a flag the arc has carried since July

`StateReduction_CollapseRate_ED_Derivation` residual, written 2026-07-21:

> *"ED's gravity is the **quadratic-strain interference cross-term**, not the Einstein–Hilbert term … so **the exact energy combination driving the branch-phase could differ subtly from the textbook `E_G`**; the honest statement is that the *scaling* is what ED grounds."*

**The combination is now identified: `Str − Coh`.** And the answer is that it does **not** differ from the textbook `E_G` in form — it *is* `E_G`, re-expressed in ED's own terms. **The flag anticipated a discrepancy and there is none; what there is instead is a derivation of the combination the flag was worried about.**

## 5. Tier, and what C4 becomes

**Tier: D-via-I.** Given (i) the settled P12 split (`foundations/Note_SigmaC_SignCheck_2026-09-05.md`, itself fixed by arithmetic against `Paper_030`) and (ii) `Paper_030` §4.2's bandwidth-as-potential-content reading, the identity is algebra. **Nothing here is derived from primitives, and the two inputs are both conditional commitments.**

**Flag C4 is partly discharged.** The arc flags that its step *"**identifies** the branch-clock-difference energy with the known Penrose self-energy `E_G` rather than deriving it."* **Under this correspondence it is no longer an identification with an external formula — it is `−Σ_C`, ED's own functional.** That is a real upgrade: **from importing Penrose to obtaining the same combination from P12.** What remains conditional is the P12 split and the bandwidth reading, not the Penrose import.

**Grad is dropped**, justified when the branches are smooth on substrate scales, and stated rather than assumed silently. **`Grad` is itself only a proposal** (`foundations/Note_Grad_Proposal_2026-09-05.md`), so a version that keeps it is not currently writable.

## 6. Where ED and Diósi–Penrose come apart, recorded as a consequence and not a prediction

**DP's `E_{12}` is a real overlap integral with no phase, so DP's `E_Δ` is phase-independent. ED's carries `\cosΘ_{12}`.**

| Relative phase | ED `E_Δ` | DP `E_Δ` |
|---|---|---|
| `0` (in phase) | `0` | `0` |
| `π/3` | `1.0` | `0` |
| `π/2` | `2.0` | `0` |
| `π` (anti-phase) | `4.0` | `0` |

*(DP's column is `E_11+E_22−2E_12` with the branches identical and the overlap complete, hence zero throughout — the point being that it does not move with phase.)*

**So ED's collapse energy, and hence its collapse rate, depends on the relative phase between branches — which is exactly the quantity an interferometer controls.**

**This is recorded as a consequence to check, explicitly not as a prediction.** **→ CHECKED the same day: `Note_Theta12_LayerQuestion_2026-09-05.md`. The answer is a fork, not a value.** Relative phase **is** physical, not gauge (`Paper_008_5_PhaseIndependence` preamble 4: *“relative phases between amplitudes carry observable interference content”*), so *fixed* and *gauge artifact* are both out. **But observable quantum phase is the holonomy of the *coarse-grained* connection** (`Paper_009_BerryPhase`), while **raw substrate polarity decorrelates at `ξ ≈ 5ℓ_ED`** (measured, `Paper_PhaseCoherence_P12Coh`). **Which one is `Θ_12` depends on the layer at which `Σ_C` is evaluated — and P12's `∇_adj` points at layer 1** (`gravity/Note_a0_TwoPi_RepairRoutes` §4f). **At layer 2 the phase is controllable and this section stands; at layer 1 it is separation-dependent with range `ξ`, and the cross term dies over `10⁻³⁴ m` rather than over the object's own size.** **Both readings preserve the two limits above, so the identity is unaffected — what is conditional is whether ED's cross term reproduces Penrose's mutual energy.**

## 7. Why this matters beyond the collapse arc

**It is the fourth support for the `Coh`/`Str` split, and the first quantitative one.** The others — the gravity sign check, AP's Relation/Boundary/Gradient reading, the density-matrix structural correspondence — all say *what the terms are*. **This one says the split reproduces a number the corpus already had, from a different arc, with the right limits and the right sign.**

**And it closes the loop the density-matrix reading opened.** `readings/ED_Reading_ManyWorlds_TheOtherReadingOfSchrodinger` says commitment is the diagonalization of `ρ` — it destroys the off-diagonal and leaves the diagonal. **Here that has a number attached: the destroyed interference is `Coh`, the surviving facts are `Str`, and their difference is what the collapse rate runs on.**

---

*Gravity ledger Staleness #74. Check: `internal notes/_check_collapse_correspondence.py`.*
