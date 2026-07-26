# The Khronometric Equation of State: Jacobson's Derivation, Written Out for Event Density's Luminal-Cone Gravity

**Allen Proxmire**

**July 2026**

---

## Preamble — what this article does and does not claim

1. **This writes out a derivation whose verdict is already established, not a new verdict.** The companion paper `Paper_GravityAsEquationOfState` §6 states, at literature-grounded tier, that ED's local Jacobson derivation is *cleanly equilibrium and reaches the full Einstein equation*. Nobody — in ED or in the Einstein-aether literature — has actually **written out** Jacobson's local-Rindler `δQ = TdS` derivation for a khronometric theory. This article does that, for ED's specific *luminal-cone* class, making the verdict explicit and checkable.
2. **The Jacobson core is derived here; the aether-specific results are cited, not re-derived.** The local-Rindler Clausius steps (Raychaudhuri focusing, the boost Killing flux) are worked in full. The three aether-specific facts the derivation rests on — (i) the Wald entropy is pure area, (ii) the non-area aether entropy is reabsorbable in a local aligned single-scale wedge, (iii) the shear channel is unmodified on the luminal family — are **taken from the literature** (cited inline) and assembled, not independently re-derived.
3. **ED's results are conditional derivations from thirteen posited primitives**, never derivations from nothing, and the framework is not experimentally confirmed.
4. **The "fourth face" is NOT claimed.** That the khronon's kinematic footprint (`α₁`) and its dissipative footprint (a bulk entropy-production term) are the *same* function of the one coupling is an **open conjecture**, not a result. What is banked is weaker and stated as such (§6): both are `O(λ_local)`, neither leaks at `O(1)`, and the exact-same-power question needs a closed-form aether entropy that even the 2026 literature has not rendered.
5. **Tiers are marked per claim.** Determination (C) (clean equilibrium → full Einstein) is *literature-grounded*; the `O(λ_local)` powers rest on a flux-prefactor *inference*; the absolute seventy-orders magnitude is *inherited* from GR-IV's estimate-tier `λ_local`.

---

## 1. What Event Density is, and the class this runs in

Event Density is a discrete, relational substrate: a participation graph whose channels carry a bandwidth `b ≥ 0` and a phase, with one process primitive — **commitment** (P11), the irreversible act that writes the arrow of time into the law. Gravity is emergent (the metric is the reading of the bandwidth field, `g ~ 1/b`, `Paper_GR-I`), and ED's gravitational class is **khronometric**: Einstein's two tensor modes plus one propagating scalar, the *khronon* $u_\mu = \partial_\mu T/|\partial T|$, the arrow made geometric (`Paper_GR-II`). The emergent horizon is the `b → 0` locus, an A1 capacity-zero causal cut (`Paper_GR-III` §7.4).

The one feature that makes this derivation tractable is that **both of ED's gravitational cones are luminal**: `c_T = c` (the single P05 transport cone) and `c_s = c` at leading order (the khronon; the commitment reserve is dissipative, not a second kinetic cone, `Paper_GR-III` §6). In the standard three-coupling khronometric parametrization `(α, β, λ)` — equivalently the Einstein-aether `(c₁, c₂, c₃, c₄)` with hypersurface-orthogonality removing the spin-1 mode — luminality is two independent constraints (`c_T = c ⟹ β = 0`; `c_s = c ⟹ α = λ/(1+2λ)`), collapsing the coupling space to **one dimension**, coordinatized by `λ ≡ λ_local` (`Paper_GR-IV` §3; verified analytically against Ramos–Barausse arXiv:1811.07786, Blas–Lim arXiv:1412.4828, Foster–Jacobson gr-qc/0509083). On that family, `α₂ = 0` exactly and `α₁ = −4λ_local`. This 1D collapse is what lets a single coupling govern every khronometric footprint below.

This article is the technical companion to `Paper_GravityAsEquationOfState`: that paper grounds Jacobson's *inputs* and asserts the equilibrium verdict; this one writes out the *derivation* that produces it.

## 2. Jacobson's derivation, and the four places Lorentz enters

Jacobson (1995) derives the Einstein equation as an equation of state. Through any point `p`, boost into a local inertial frame and consider a small patch of a **local Rindler horizon** — a null congruence with generators `k^a`, affine parameter `λ`, approximate boost Killing field `χ^a = −κλ k^a`. Three inputs:

- **Entropy** proportional to horizon area, `S = η A`, so `dS = η\, δA`;
- **Unruh temperature** `T = κ/2π` (the local Rindler temperature of the boost vacuum);
- **Heat** = boost energy flux across the horizon, $\delta Q = \int T_{ab}\chi^a\, d\Sigma^b = -\kappa\int \lambda\, T_{ab} k^a k^b\, d\lambda\, dA$.

The area change follows from **Raychaudhuri focusing**, `dθ/dλ = −\tfrac12 θ^2 − σ^2 − R_{ab}k^a k^b`. Choosing `p` so that `θ = σ = 0` there, to first order `θ = −λ R_{ab}k^a k^b`, hence

$$ \delta A = \int \theta\, d\lambda\, dA = -\int \lambda\, R_{ab} k^a k^b\, d\lambda\, dA. $$

Imposing Clausius `δQ = T\, dS` for **all** local Rindler horizons (all null `k^a`) forces `T_{ab}k^a k^b = (η/2π)\, R_{ab}k^a k^b` for every null `k`, hence `T_{ab} = (η/2π)(R_{ab} + f g_{ab})`; conservation and the Bianchi identity fix `f = −R/2 + Λ`, giving the **Einstein equation** with `2π/η = 8πG`.

**The four Lorentz-dependent steps** (the audit the khronometric case must survive): (1) the Unruh temperature assumes the vacuum is *thermal with respect to boosts*; (2) the boost Killing field assumes an *approximately flat region with Poincaré symmetry*; (3) "all null directions" assumes an *isotropic light cone / no preferred frame*; (4) the entanglement origin of `S` assumes *Lorentz-invariant vacuum correlations*. A preferred foliation threatens each. The rest of this article shows each survives on ED's luminal family, and identifies exactly where the khronon does leave a mark.

## 3. The luminal cones keep the kinematic scaffolding (steps 1–3)

The kinematic worries are benign, and the reason is uniform: **on ED's luminal family the causal structure is the standard light cone.**

- **No universal-horizon complication.** The notorious "universal horizon" of khronometric/Hořava gravity — a khronon-trapping surface distinct from the metric horizon — exists only because the khronon can propagate *superluminally*, so the metric light-cone is not the true causal boundary (Barausse–Jacobson–Sotiriou arXiv:1104.2889; Blas–Sibiryakov arXiv:1110.2195). ED's khronon is *luminal* (`c_s = c`), so the metric horizon **is** the causal horizon and no separate universal horizon arises. Step (3)'s "all null directions" is the ordinary null cone.
- **The Unruh temperature survives (step 1).** What breaks horizon thermality under Lorentz violation is dispersion *nonlinearity*, not the preferred frame as such: linear/luminal dispersion preserves the KMS/thermal structure (arXiv:2102.08944), while nonlinear or superluminal dispersion breaks it (Campo–Obadia arXiv:1003.0112). ED's dispersion is linear and luminal, so `T = κ/2π` holds. (Within ED this temperature is itself read off the near-horizon Rindler geometry via the Euclidean-continuation route, with the standard honesty pin that a commitment-statistics, continuation-free derivation is open — `BH_Thermal2Pi` §4b.)
- **`α₂ = 0` exactly (step 2).** The second preferred-frame parameter vanishes identically on the luminal family (`Paper_GR-IV` §3, literature-verified), so the boost structure step 2 relies on is undeformed at that order. The only surviving kinematic footprint is `α₁ = −4λ_local`, a velocity-dependent correction suppressed ~70 orders by sparse becoming (`Paper_GR-IV` §6).

So steps 1–3 pass, and the "khronometric-vs-Lorentz obstruction" is **real but benign at the kinematic level**. The genuine question is step (4): the entropy.

## 4. The horizon entropy is pure area (the equilibrium enabler, step 4)

Eling, Guedens and Jacobson (gr-qc/0602001) sharpened the equation-of-state program: `δQ = TdS` holds in the tidy **equilibrium** form if and only if the horizon entropy is **pure area**; any non-area piece forces a non-equilibrium Clausius relation `dS = δQ/T + d_iS` with an internal-production term `d_iS ≥ 0`. So everything turns on whether the khronon adds a non-area entropy to ED's horizon.

It does not, locally. Two facts, both from the literature, settle it:

- **The Wald entropy is pure area.** The Wald entropy density is built from $\partial L/\partial R_{abcd}$. Only the Einstein–Hilbert term carries the Riemann tensor; the khronon/aether kinetic terms `(\nabla u)^2` contain no explicit `R_{abcd}`, so they contribute **zero** to the Wald density. The horizon entropy is `S = A/(4G_æ)` with `G_æ = G_N/(1 − c_{14}/2)` — the couplings only **renormalize the area coefficient**, adding no non-area piece (Brustein–Gorbonos–Hadad arXiv:0712.3206; arXiv:2606.27437). (The naive first law is singular at the bifurcation surface, where the aether unit vector is ill-defined; the covariant-phase-space treatment makes it rigorous and confirms the area piece — Foster gr-qc/0510125; arXiv:2603.28851.)
- **The non-area "aether entropy" is reabsorbable in the local wedge.** There *is* a candidate non-area aether term, but arXiv:2603.28851 §6.3 shows that in a **single-scale, asymptotically-flat** geometry it is reabsorbed into the area coefficient "by a simple rescaling," becoming genuinely independent "only in the presence of additional scales (such as a cosmological constant)"; arXiv:2606.27437 shows it appears only when the aether is **misaligned** with the horizon-generating Killing vector. Jacobson's construction uses an **aligned, asymptotically-flat, single-scale** (no `Λ`) local Rindler wedge — precisely the case where the aether entropy reabsorbs and does not enter.

**Determination (C).** In ED's local Rindler wedge the horizon entropy is pure area, so the Clausius relation is the tidy **equilibrium** one, and Jacobson's derivation runs unchanged (with `η = 1/4G_æ`). *(Literature-grounded — the Wald pure-area result and the reabsorption are drawn from the cited 2026 covariant-phase-space literature, assembled via the R1–R6 analysis, not independently re-derived here; see §7 tiers.)*

## 5. The explicit equation of state: clean equilibrium → full Einstein

Assemble §§2–4. With pure-area entropy `dS = η\, δA`, `η = 1/(4G_æ)`, temperature `T = κ/2π`, and heat flux from the **total** stress (matter plus the khronon's own stress, `T_{ab}^{\rm tot} = T_{ab}^{\rm m} + T_{ab}^{æ}`), Clausius `δQ = T dS` reads

$$ -\kappa \int \lambda\, T_{ab}^{\rm tot} k^a k^b\, d\lambda\, dA \;=\; \frac{\kappa}{2\pi}\,\eta \left(-\int \lambda\, R_{ab} k^a k^b\, d\lambda\, dA\right). $$

Demanding it for all null `k^a` gives `T_{ab}^{\rm tot} k^a k^b = (\eta/2\pi) R_{ab} k^a k^b` for every null `k`, hence, with conservation and Bianchi as in §2,

$$ \boxed{\,R_{ab} - \tfrac12 R\, g_{ab} + \Lambda g_{ab} \;=\; 8\pi G_{\text{æ}}\, \big(T_{ab}^{\rm m} + T_{ab}^{\text{æ}}\big).\,} $$

This is the Einstein-aether field equation. Now use Determination (C): because the horizon entropy is pure area (§4), the aether adds **no non-area entropy and no non-equilibrium production term** to the local Clausius relation. It enters only as an ordinary source stress `T_{ab}^{æ}` on the right-hand side and through the renormalized coefficient `G_æ`. In Jacobson's sense (geometry = total stress), the local wedge relation is therefore of **Einstein form with the aether counted among the sources** — the clean equilibrium equation of state, not a modified or non-equilibrium one. It is **not** vacuum General Relativity: `T_{ab}^{æ} ≠ 0` and the khronon carries its own field equation; what is "full Einstein" is the *form and equilibrium class* of the relation, not the disappearance of the aether from the right-hand side. The genuinely khronometric, non-Einstein content (the non-area entropy, the bulk dissipation of §6) appears only when a second scale (`Λ`) or misalignment is present — i.e. at the *global/cosmological* level — or at `O(λ_local)` in the dissipative channel. Locally:

> **ED reaches the full Einstein equation via Jacobson's clean equilibrium derivation.** This is the same class as General Relativity itself: GR's own local equation of state is equilibrium up to the universal shear-viscosity term (the `σ^2` Jacobson drops = Hartle–Hawking tidal heating; Chirco–Liberati PRD 81, 024016), and ED carries exactly that same term and no more at the tensor level (§6). ED is *not* below GR in equilibrium quality, and it is *not* above it.

This is the second independent route to Einstein in ED — the thermodynamic one — meeting the dynamical bandwidth-rule route (`ḃ = D∇²b − κρ` steady state, `Paper_GR-III`) from the opposite direction, with ED grounding the inputs of the thermodynamic one (severance = the hidden DOF, grain = the cutoff, severance count = `η`; `Paper_GravityAsEquationOfState`).

## 6. Two corollaries — and the one the log forbids me to overstate

**Corollary 1 — the shear channel is exactly GR.** The horizon shear viscosity of a gravitational equation of state is `η_{\rm shear} = 1/(16\pi G)` in GR; in Einstein-aether it is rescaled by the spin-2 coefficient `∝ (1 − c_{13})`. On ED's luminal family `c_{13} = 0`, so the factor is unity: **ED adds no shear viscosity** (and the spin-1 dissipation is absent because hypersurface-orthogonality removes the vector mode). This is another face of "ED is observationally General Relativity": the luminal tensor cone forbids an aether shear footprint. *(Literature-grounded: Berglund–Bhattacharyya–Mattingly arXiv:1210.4940; luminal-family evaluation.)*

**Corollary 2 — a scalar-sector co-suppression (stated at its honest tier, NOT a "fourth face").** The one genuinely new thermodynamic footprint is a **bulk (spin-0 / expansion) aether entropy-production term**, `d_iS`, absent from the equilibrium entropy (which is pure area) and appearing only in the dissipative/global sector. Its prefactor is the Noether current `J^a = −2c_{123}\,\vartheta\, f^a` with `c_{123} = c_1 + c_2 + c_3 = c_{13} + c_2 = 0 + \lambda = \lambda` on the luminal family — so it is `O(\lambda)`, the *same leading order* as the kinematic `α₁ = −4c_{14} \approx −4\lambda`, and regular at `c_{13} = 0` (no `1/c_{13}`). (Both are `∝ λ` on the 1D family with O(1) coefficients unresolved — pinning those is exactly the open computation below.) Both are the khronon (scalar) sector's expression, controlled by the one surviving luminal coupling.

The honest content, and its limit:

> **Banked:** on ED's derived luminal family (1D coupling space), the kinematic preferred-frame coupling `α₁` and the bulk thermodynamic `d_iS` are **both `O(λ_local)`**, each vanishing at least linearly in the GR limit (`λ → 0`), so **neither leaks at `O(1)`** and both carry the same `~ρ_event/ρ_Planck` sparse-becoming suppression (the thermodynamic footprint at least as suppressed as `α₁`'s ~70 orders). The feared `O(1)`/`Λ`-sourced aether-entropy leak is refuted — it vanishes in the GR limit (Arata–Liberati–Neri arXiv:2603.28851). *(Well-supported; one inferential step — the linear-in-coupling flux prefactor, not a fully-rendered closed-form `S_æ(c_i)`.)*
>
> **NOT banked — the open conjecture:** whether `α₁` and `d_iS` share the *exact same power* of `λ` (a genuine single-object "fourth face") or the entropy is *steeper* (e.g. `λ^2`, hence **more** suppressed and *not* unified) requires the closed-form khronometric aether entropy — which the 2026 covariant-phase-space literature did not render — plus a regularity check at the exact `c_{13} = 0` point. Once the space is collapsed to 1D, "both are functions of `λ`" is automatic; the *unified-object* framing is rhetoric until the exact power is shown. The strong "fourth face / one structure" reading is therefore held as a conjecture, not a result.

This is the same discipline the working log enforced: the equilibrium result is the headline; the co-suppression is a real but tiered corollary; the fourth face is a flagged open question.

## 7. Honest tiers and the one open computation

- **Derived (in this article):** the local-Rindler Clausius steps — Raychaudhuri focusing, the boost-flux heat, the `δQ = TdS → G_{ab} = 8\pi G_æ T_{ab}^{\rm tot}` algebra (§2, §5).
- **Literature-grounded (cited, assembled):** the luminal-cone kinematic survival (§3); the pure-area Wald entropy and local reabsorption of the aether entropy (§4, Determination C); the shear-channel result (§6, Corollary 1).
- **Inference-tier:** the `O(λ_local)` power of the bulk `d_iS` and the global aether entropy (§6) — resting on the linear-in-coupling flux prefactor, not a rendered closed form.
- **Inherited:** the absolute magnitude of `λ_local ~ ρ_event/ρ_Planck` (GR-IV estimate-tier); the grain value; the horizon `2π` (via the Euclidean route, `BH_Thermal2Pi`).
- **Open (the one paper-able computation this leaves):** render the closed-form khronometric aether entropy on the luminal family, extract its **exact leading power in `λ`**, and check `c_{13} = 0` regularity. This decides whether the scalar-sector co-suppression is "same power" (the fourth face is real) or "entropy even more suppressed" (still seventy-orders safe, but not a unified object). Until then, §6's conjecture stays a conjecture.

## 8. Position statement

Jacobson showed the Einstein equation is an equation of state. The obvious worry for Event Density — that its preferred foliation, the khronon, would obstruct a derivation built on local Lorentz invariance — turns out to be benign, and this article writes out why, step by step, for the first time in a khronometric theory. On ED's *derived* luminal family the causal scaffolding is the standard light cone (no universal horizon, Unruh survives, `α₂ = 0` exact), the horizon entropy is pure area (the aether kinetic term carries no curvature, and its would-be non-area piece reabsorbs in the local single-scale wedge), and so Jacobson's clean **equilibrium** Clausius relation runs unchanged and yields the **full Einstein equation** — the same equilibrium class as General Relativity, sharing GR's universal shear-viscosity term and adding none. The khronon leaves exactly two marks, and both are the scalar sector's: the kinematic `α₁` and a bulk entropy-production `d_iS`, each `O(λ_local) ~ ρ_event/ρ_Planck` (the dissipative one at least as suppressed as `α₁`), seventy orders silent. Whether those two marks are the *same* function of the one coupling — a genuine "fourth face" of sparse becoming — is the one honest open computation this derivation leaves on the table, and it is named, not claimed. None of this is offered as confirmed physics; it is the grounding the equation-of-state program was waiting for: the arrow is in the law, absent from the equilibrium equation of state, and present only in a footprint the same sparseness that makes ED quantum keeps seventy orders quiet.

---

## Cross-references

- Jacobson, T., *Phys. Rev. Lett.* **75**, 1260 (1995), gr-qc/9504004.
- **The verdict this writes out:** `event-density/foundations/Khronon_vs_Lorentz_in_Jacobson_RESULTS_LOG_2026-07-24.md` (R1–R6, the closed analysis); `physics-papers/substrate-evaluation/Paper_GravityAsEquationOfState.md` §6–§7 (the companion that asserts it).
- **ED gravity line:** `Paper_GR-II` (khronometric class, `b→0` horizon), `Paper_GR-III_DynamicalRule.md` (`c_s = c`; §7.4 measured pure-area severance law), `Paper_GR-IV_ArrowsAlibi.md` (`α₁ = −4λ_local`, `α₂ = 0`, luminal 1D coupling family).
- **Horizon thermodynamics:** `foundations/BH_Thermal2Pi_FromNearHorizonRindler.md` (`T = κ/2π`); `foundations/BH_EntropyCoefficient_FromEventCounting.md` (the coefficient).
- **External (equation-of-state / aether thermodynamics):** Eling–Guedens–Jacobson gr-qc/0602001 (nonequilibrium spacetime); Chirco–Liberati PRD 81, 024016 (horizon shear viscosity); Brustein–Gorbonos–Hadad arXiv:0712.3206 (Wald entropy of higher-derivative/aether); Berglund–Bhattacharyya–Mattingly arXiv:1210.4940, arXiv:1309.0907 (universal-horizon thermodynamics); Foster gr-qc/0510125 (aether energy/first law); Arata–Liberati–Neri arXiv:2603.28851, arXiv:2606.27437 (covariant phase space; reabsorbability of the aether flux term); Barausse–Jacobson–Sotiriou arXiv:1104.2889, Blas–Sibiryakov arXiv:1110.2195 (universal horizons require superluminal modes); khronometric PPN: Blas–Lim arXiv:1412.4828, Ramos–Barausse arXiv:1811.07786, Foster–Jacobson gr-qc/0509083.
- **Companion (this family):** `Paper_GravityAsHorizonEquipartition.md` (Padmanabhan), `README.md`.
