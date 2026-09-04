# The Arrow's Deep Field: Dark-Matter Phenomenology from the Khronon, and the Unification of Event-Density Gravity

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — post-pivot Arc ED-10 (curvature emergence), Paper KM-I
**Status:** Publication draft. Conditional structural derivation within the 13-Primitive Generative System. Standalone; cold-reader accessible. Companion to GR-I and GR-II; completes the reconciliation those papers declared open.
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **The MOND deep-field exponent is not derived from primitives.** The khronon's deep-infrared kinetic structure is **uniquely fixed by matching the Combination Rule the corpus already derived** (Paper_030) — *forced-given-030* — and the paper says so wherever it matters. The khronon **embeds** the substrate's geometric-mean law relativistically; it does not re-derive it. The primitives-level origin of the deep-IR branch is a declared open question, deliberately not attempted.
3. **$a₀ = cH₀/(2π)$ is inherited** (Paper_029, from the cosmic decoupling surface, Paper_028), not re-derived. What this paper adds is the structural carrier: the scale is the khronon's own background rate.
4. **No value of the cosmological constant is derived.** §7's vacuum-term resonance ($ρ_Λ ∼ H₀²c²/G$) is an order-of-magnitude *form* consistency — the khronon's only scale is the cosmic rate — fully inside the corpus's value-inherited stance. The reconciliation with the corpus's V1-backreaction reading of Λ (Paper_038.5) is flagged open, not performed.
5. **The interpolation between the two fixed asymptotics is a family** — now a *Cassini-constrained* family (slow-saturating members excluded by ephemerides) — and no member is load-bearing for any claim here.
6. **The cosmological regulator sector is a family** (sequestered from everything tested; §7), with its own constraints (BBN, Čerenkov, FRW stability). No member is selected; selecting one is model-building, outside this paper.
7. **Class-level results are inherited and labeled.** That khronometric theories with non-canonical acceleration kinetics yield MOND in the static weak field is established literature (the Blanchet–Marsat construction; the generalized-aether results of Zlosnik–Ferreira–Starkman), used here as the external dictionary — exactly as Lovelock's theorem was used in GR-II. Reported stability corners of this class are cited as reported, **not independently verified here**.
8. **Clusters and the CMB are not addressed.** Reproducing galactic MOND phenomenology does not resolve the known cluster-scale missing-mass shortfall or cosmological structure formation; those debts land on ED's cosmology/SCBU sector and are flagged wherever relevant.
9. **GR-I and GR-II are inherited**, not re-derived: the bandwidth metric, the lapse $N² ∼ b$, the khronometric class, $c_T = c$, and Lorentz safety are inputs.

---

## Abstract

GR-II identified Event Density's gravitational class as **khronometric**: Einstein's tensor sector plus one scalar — the khronon, the substrate's arrow of time made dynamical, anchored to the cosmological rest frame. This paper shows that the same scalar naturally carries the **dark-matter phenomenology** of ED's published gravity arc, unifying the corpus's two gravity programs into one theory. The construction has one missing span and two built ends. The ends: the khronon (GR-II), and the MOND sector — $a₀ = cH₀/(2π)$ from the cosmic decoupling surface (Paper_029), the Combination Rule $a = √(a_N a₀)$ (Paper_030), BTFR (Paper_031), the MOND field equation (Paper_036). The span: the khronon's kinetic structure. Promoting the khronometric acceleration term to a function $W(A²)$ of the congruence acceleration — the established khronometric-MOND structure — the static weak field reduces to the **modified Poisson equation in the metric potential itself**, $∇·[μ_{\rm tot}∇Φ] = 4πGρ$ with $μ_{\rm tot} = 1 + c_{1W}'$. The high-acceleration limit is GR-I, untouched (commitment-linearity ⟹ $μ → 1$); the deep-infrared limit is **uniquely fixed by matching Paper_030** ($μ_{\rm tot} → x$, forced-given-030), embedding the Combination Rule and BTFR relativistically — at the surfaced cost of an **infrared cancellation** (the khronon takes over the static constraint below $a₀$), standard in this class. Statics isolate the construction: $θ = σ = 0$ for the aligned khronon, so the MOND carrier is the *unique* active foliation term, and the ED identity $a_i = ½∂_i\ln b$ reads the whole sector in substrate language — *the deep field switches on where bandwidth gradients fall below the cosmic rate.* **The historical kill-checks pass structurally**: lensing tracks the MOND potential with **no added vector field** (the modification is metric-borne; the conformal-coupling disease TeVeS patched never arises; slip is $O(Φ)$-suppressed); no new ghost (the $W$-sector adds no time derivatives in unitary gauge); the classic AQUAL ellipticity conditions hold; screening is PPN-safe in the linear khronometric corner. The one soft spot — the $A → 0$ degeneracy — is resolved without retrofit: the degenerate point is **exact Minkowski vacuum, which is not in ED's state space** (the substrate always ticks), the pure-$A²$ form is a truncation whose generic completion $𝒲(A², Θ)$ is healthy at the physical cosmological point, and an **orthogonality theorem** ($θ ≡ 0$ in statics) sequesters the regulator family from everything tested. The khronon's cosmological face ties the arc to SCBU — **one scale, $H₀$, in four roles** (background rate, $a₀$, horizon locus, $R_H$ boundary) — and its infrared vacuum term is naturally of order $ρ_Λ ∼ H₀²c²/G$, the observed dark-energy order, read as single-scale consistency (form-tier only). The result: **one khronometric gravity** — Einstein at high accelerations, MOND in the deep field, dark energy's order carried — in which "dark matter" is *the deep-infrared regime of the arrow's own field*. No particle, no added vector, no new primitive. Clusters and the CMB remain owed.

---

## 1. Introduction

### 1.1 What this paper does

ED's gravity corpus contained two programs. The published arc (Papers 025–038) derived Newton, the transition acceleration $a₀ = cH₀/(2π)$, the Combination Rule, and BTFR — the dark-matter-free account of galactic dynamics — covariantized in Paper_033 on a *postulated* metric with a *postulated* scalar. The post-pivot arc (GR-I/II) *derived* the metric (the bandwidth metric, with the weak-field Einstein tests) and *derived* the scalar (the khronon: the arrow made dynamical). This paper supplies the one missing identification: **the postulated scalar of the MOND arc is the derived scalar of the curvature arc.** It proceeds in four steps: the mapping (§3), the static weak-field reduction with the GR and MOND limits (§4), the lensing and viability checks (§5–§6), and the cosmological regulator with the SCBU tie-in (§7).

Three orienting statements, up front:

- **The hinge.** The paper's only derivational hinge is the deep-infrared matching to Paper_030's geometric-mean law, which **uniquely fixes** the non-analytic term in `W'`. No other freedom is exercised anywhere in the construction; everything else is inherited, derived, or labeled a family.
- **The economy.** No new primitive, field, or symmetry is introduced. The khronon was *counted* by GR-II's mode analysis before MOND was on the table; this paper spends a field the theory already had.
- **What survives (preview).** The three historical kill-checks of relativistic MOND all pass structurally: **lensing** tracks the MOND potential with no added vector (§5); **no new ghost** arises (§6.1); **solar-system screening** is PPN-safe (§6.3). The one soft spot — the deep-vacuum degeneracy — is resolved at the level of ED's state space and EFT generality (§7). And the cosmological regulator is a *family, sequestered from every static test*: its role is to make the theory well-posed on FRW backgrounds, not to influence galactic phenomenology (§7.3).

### 1.2 Why this matters

Three reasons. First, **unification**: the corpus's two gravity lines fuse into one theory with one extra field — and that field was not added for the purpose; it was *counted* by GR-II's mode analysis before MOND was on the table. Second, **the dark-matter claim sharpens**: "no dark matter; modified dynamics below $a₀$" becomes "the galactic phenomenology is the deep-infrared regime of the preferred-foliation scalar" — a specific field with an independent origin (the arrow), independent constraints (GW170817, PPN, pulsars), and independent predictions (a breathing GW mode; wide-binary deviations). Third, **the historical failure modes are addressed structurally, not by patches**: the constructions that killed earlier relativistic MOND (conformal couplings blind to lensing; added vectors; fine-tuned $a₀$) are each avoided by something ED already had.

**Why the unification is nontrivial.** Four scales that have no business coinciding — the rate of the arrow's cosmological flow, the acceleration at which galactic dynamics turn non-Newtonian, the energy density of the vacuum, and the locus where horizons form — are here carried by **one scalar field with one background scale**. In any framework where these are independent sectors, their numerical coincidences ($a₀ ≈ cH₀/2π$; $ρ_Λ ∼ H₀²c²/G$) are unexplained accidents. In this construction they are the *same number wearing four hats*, because the khronon has only one number to offer.

### 1.3 How this fits the arc

- **Papers 027–031, 036:** Newton; $a₀$; Combination Rule; BTFR; the MOND field equation. *(the deep-field end — inherited)*
- **Paper_033:** scalar-tensor covariantization on a postulated metric and scalar. *(fused here: the scalar is identified)*
- **Paper GR-I:** the bandwidth metric; weak-field Einstein tests. *(the high-acceleration end — inherited)*
- **Paper GR-II:** the khronometric class; the khronon; $c_T = c$; Lorentz safety. *(the field itself — inherited)*
- **Paper KM-I (this paper):** the unification — the khronon's deep field is the MOND sector.

This completes the second of the two reconciliation items GR-I §7 declared open (the khronon↔MOND relation); the first (the bandwidth↔strain/flow substrate-route identification) remains open.

### 1.4 Conventions and regime of validity

Signature $(−,+,+,+)$; $c = 1$ where convenient. The derivations are **static, weak-field, quasi-spherical**, in the **continuum (DCGT) limit**; the cosmological statements (§7) are FRW-background structural results. **No strong-field, no time-dependent-lensing, no cluster, and no CMB claims are made.** Exact numerical coefficients in the reductions are convention-dependent and carried schematically ($c₁$-type constants of order unity); the *structures* and *limits* are the results.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P11/P13 (the arrow and the tick — the khronon's origin, via GR-II), P04 (bandwidth — the metric and lapse, via GR-I), P02/P05 (adjacency/transport). The Σ-selection's orientation-blindness and P-Commitment-Linear (GR-I) enter through the inherited results.

**Inherited results (load-bearing):**

- **GR-I:** $g_{ij} ∼ b^{-1}$, $N² ∼ b$, the weak-field Schwarzschild metric; P-Commitment-Linear ⟹ the Einstein branch at high accelerations.
- **GR-II:** the khronometric class; the khronon $T$ with $u_μ = ∂_μT/\sqrt{X}$ hypersurface-orthogonal; the preferred frame = the cosmological rest frame; $c_T = c$; universal Lorentz violation.
- **Paper_029:** $a₀ = cH₀/(2π)$ (value anchored to $H₀$).
- **Paper_030:** the Combination Rule $a = √(a_N a₀)$ (the substrate's own deep-field law, via the P14 bilocal coupling).
- **Papers_031/036:** BTFR; the MOND field equation (the flat-space form this paper's static limit must and does land on).

**External dictionary (inherited mathematics/physics, labeled I):**

- **Khronometric/aether-MOND** (Blanchet–Marsat 2011; Zlosnik–Ferreira–Starkman 2007): a preferred-foliation scalar with non-canonical *acceleration* kinetics yields the MOND modified-Poisson equation in the static weak field, with the interpolation given by the kinetic function's derivative. The class's reported stability corners are cited as reported.
- **Classical AQUAL well-posedness** (Bekenstein–Milgrom): ellipticity conditions $μ > 0$, $d(xμ)/dx > 0$.

**No new primitive is introduced; no primitive forcing is invoked.** The paper's single structural commitment beyond inheritance is the *typing* of the kinetic sector (the acceleration invariant, §3.2) — which is argued, not assumed, since the alternative typing fails independently.

---

## 2.5 Load-Bearing Step Audit

*Status legend:* **I** = inherited (from a cited paper or established external result); **D** = derived here; **D-structural** = derived from structure alone, no model details; **conditional** = derived given a labeled input; **family** = an honestly-unfixed functional freedom; **form-tier** = an order-of-magnitude/structural consistency, no value claimed; **open** = declared open.

| Step | Status | Source / justification |
|---|---|---|
| Khronon exists; class is khronometric; cosmic-frame anchored | I | GR-II |
| Metric/lapse from bandwidth; Einstein branch at high $A$ | I | GR-I |
| $a₀ = cH₀/2π$; Combination Rule; BTFR; MOND field eq | I | Papers 029/030/031/036 |
| Khronometric-MOND dictionary ($W(A²)$ ⟹ modified Poisson) | I | Blanchet–Marsat; ZFS |
| Kinetic invariant = the congruence **acceleration** (not $(∂T)²$) | **D** | §3.2 — the $(∂T)²$ typing is structurally inert or lensing-dead |
| Statics isolate the $W$-sector ($θ = σ = 0$; khronon aligns) | **D** | §4.1 — kinematics of static congruences |
| ED identity $a_i = ½∂_i\ln b$ | **D (identity)** | §4.1 — via GR-I's $N² ∼ b$ |
| Modified Poisson $∇·[μ_{\rm tot}∇Φ] = 4πGρ$, $μ_{\rm tot} = 1 + c_{1W}'$ | **D** | §4.2 — form-level; constants conventional |
| GR limit ($W' → α$ small ⟹ $μ → 1$; GR-I untouched) | **D** | §4.3 |
| Deep-IR limit $μ_{\rm tot} → x$ ⟹ Combination Rule + BTFR | **D conditional on I-030** | §4.4 — **forced-given-030**; includes the IR cancellation |
| The IR cancellation ($W' → -1/c_1 + x/c_1$) | **surfaced cost** | §4.4 — standard-in-class; stress-tested §6 |
| Lensing tracks the MOND potential; no vector needed | **D** | §5 — metric-borne modification; slip $O(Φ)$-suppressed |
| No new ghost ($W$-sector adds no time derivatives) | **D-structural** | §6.1 — unitary-gauge counting |
| AQUAL ellipticity across the interpolation | **D** | §6.2 — classic conditions; deep IR passes |
| Screening PPN-safe; interpolation family Cassini-constrained | **D / I** | §6.3 — linear-khronometric corner; ephemeris bounds |
| τ-mode = the breathing scalar; benign as screened | **D** | §6.4 |
| $(A,θ) = (0,0)$ outside ED's state space (no Minkowski vacuum) | **D-structural** | §7.1 — P11/P13; the khronon's background is the Hubble flow |
| Degeneracy = truncation artifact; $𝒲(A²,Θ)$ generic completion | **D (EFT-generality)** | §7.2 — regulator **family**, labeled |
| Orthogonality: tested sector invariant under the regulator | **D** | §7.3 — $θ ≡ 0$ in statics |
| One scale in four roles; SCBU carrier | **structural identification** | §7.4 |
| $ρ_Λ ∼ H₀²c²/G$ vacuum-term resonance | **form-tier only** | §7.4 — no value derived; V1-reconciliation open |
| Čerenkov / BBN / FRW stability | **filters on the family** | §7.5 |
| Primitives-level origin of the deep-IR branch | **OPEN — guarded** | preamble 2 |
| Clusters / CMB | **NOT ADDRESSED** | preamble 8 |

All steps I, D, structural, conditional, family, form-tier, open, or not-addressed. *The single derivational hinge is forced-given-030; the two honest families (interpolation; regulator) are sequestered and independently constrained.*

---

## 3. The Mapping: One Missing Span, Two Built Ends

### 3.1 The ends

**The field (GR-II).** ED's arrow lives in the law, forcing a preferred foliation; the propagating content is 2 tensor modes + 1 scalar — the khronon, whose background is cosmic time and whose background rate is the Hubble rate.

**The law and the scale (Papers 028–031, 036).** $a₀ = cH₀/(2π)$ from the decoupling surface; the Combination Rule $a = √(a_N a₀)$; BTFR; and the flat-space MOND field equation this construction's static limit must reproduce.

### 3.2 The span, and its typing

The missing piece is the khronon's kinetic structure. Its **typing is argued, not chosen**: a kinetic function of $(∂T)²$ fails twice over — in statics $(∂T)² ≈ 1 - 2Φ - |∇τ|²$ depends on the *potential*, not its gradient (yielding screening-type physics, never $μ(|∇Φ|/a₀)$), and its conformally-coupled variant is the historical RAQUAL construction that fails lensing. The correct carrier is the **acceleration of the khronon congruence**, $a_μ = ⊥_μ^ν∇_ν\ln\sqrt{X}$ — and this stays inside the foliation EFT GR-II already counted: the general quadratic sector is $λθ² + βσ_{μν}σ^{μν} + α\,a_μa^μ$, and the MOND extension promotes **only the acceleration term**:

$$
S_T = \frac{1}{16\pi G}\int d^4x\,\sqrt{-g}\;\Big[\,R + \lambda\,\theta^2 + \beta\,\sigma_{\mu\nu}\sigma^{\mu\nu} + a_0^2\,W\!\big(A^2\big)\Big],
\qquad A^2 = \frac{a_\mu a^\mu}{a_0^2},
$$

with matter coupled to $g_{\mu\nu}$ **only** (universal coupling — in ED, matter *is* substrate content; there is no conformal matter frame to mis-couple). $W$ is carried as a general function; its two asymptotics are fixed in §4, the region between them is an honest family.

**The scale's structural carrier.** The khronon's vacuum is the Hubble flow, so the only rate available to normalize its local gradients is the cosmic rate: the comparison "local acceleration against $cH₀$" is not a model choice but the field's only option. **$a₀$ is the khronon's background scale** — the Milgrom coincidence $a₀ ≈ cH₀/2π$ acquires a carrier (the coefficient $1/2π$ stays inherited from Paper_029).

---

## 4. The Static Weak-Field Reduction

With the typing fixed (§3.2), the reduction proceeds in three steps: **alignment** (the khronon locks to static time), **isolation** (statics switch off every foliation term except the MOND carrier), and **reduction** (the modified Poisson equation, with its two limits).

### 4.1 Alignment, isolation, and the Bandwidth–Acceleration Lemma

Static, time-reversal-symmetric sources align the khronon ($T = t$; the misalignment $τ$ is odd under the symmetry), making its congruence the static observers', whose kinematics are textbook: $θ = 0$, $σ = 0$, $a_i = ∂_i\ln N$. Two consequences:

1. **Statics isolate the MOND carrier.** The $λ$ and $β$ sectors are inert ($θ = σ = 0$); the acceleration function is the *unique* active foliation term in statics. The MOND modification and the static modification are the same term — by kinematics, not tuning. (The $β$-sector governs the tensor speed: $c_T = c$ from GR-II is untouched by $W$.)
2. **The Bandwidth–Acceleration Lemma.** GR-I derived $N² ∼ b$, so

   $$
   a_i = \partial_i \ln N = \tfrac{1}{2}\,\partial_i \ln b :
   $$

   **the khronon's acceleration is the logarithmic bandwidth gradient.** This identity — referenced as such below — is the substrate reading of the entire MOND sector: the deep field switches on *where bandwidth gradients fall below the cosmic rate.*

### 4.2 The modified Poisson equation

With $g_{00} = -(1+2Φ)$ and $A² = |∇Φ|²/a_0^2$ at leading order, varying the action gives (schematic order-unity constants flagged as conventional):

$$
\nabla\cdot\Big[\,\mu_{\rm tot}\!\left(\tfrac{|\nabla\Phi|}{a_0}\right)\nabla\Phi\,\Big] = 4\pi G\rho,
\qquad
\mu_{\rm tot}(x) = 1 + c_1\,W'(x^2)
$$

— the AQUAL form, **in the metric potential itself** (not an auxiliary scalar). Here and throughout, $x ≡ |∇Φ|/a₀$. The $Ψ$-equation receives the khronon's stress, whose anisotropic part is second order in the potentials (§5).

### 4.3 The GR limit

At high accelerations $W' → α$, a small constant — the standard quadratic khronometric coupling, PPN-bounded. Then $μ_{\rm tot} → 1$, $Φ = Ψ$ at leading order, and **GR-I's weak-field Schwarzschild sector — the factor-of-two bending, redshift, precession — is untouched.** The residual $O(α)$ preferred-frame effects are GR-II §8's standing $α₁, α₂$ front, unchanged. ED-side, this limit is enforced: P-Commitment-Linear demands the Einstein branch at strong gradients — the screening regime is GR-I, not an option.

### 4.4 The deep-IR limit — forced-given-030, with the cost stated

Matching the corpus's derived deep-field law ($μ_{\rm tot} → x$ so that, by Gauss-law integration, $|∇Φ| = \sqrt{a_N a_0}$) fixes the deep-IR kinetic behavior **uniquely**:

$$
W'(x^2) \;\xrightarrow{\,x \to 0\,}\; -\frac{1}{c_1} + \frac{x}{c_1} + \ldots
$$

Two pieces with two statuses. The non-analytic linear piece is the MOND carrier — the $X^{3/2}$-type term, forced-given-030. The constant $-1/c_1$ deserves its own box:

> **The IR Cancellation Requirement.** In the convention where Einstein–Hilbert keeps its standard normalization, the khronon's kinetic slope must approach the constant $-1/c_1$ in the deep infrared — **exactly cancelling the Einstein gradient term in the static constraint below $a₀$ and taking it over.** Three facts about it: (i) it is **standard in this class** (the negative-branch kinetic function of generalized-aether MOND); (ii) it is the construction's **only delicate point** — everything else is inheritance, kinematics, or sequestered family; (iii) it is **stress-tested in §6**, where it is shown *not* to destabilize statics (the total operator stays healthy even where $W' < 0$) and *not* to introduce a ghost.

With the requirement in place, the Combination Rule and BTFR slope-4 ($v⁴ = GMa₀$) are **embedded relativistically** — the khronon carries Paper_030's law; it does not re-derive it.

> **What "forced-given-030" inherits, named 2026-09-04.** The hinge is only as conditional as its source, and `Paper_030`'s deep-field law carries three declared conditions: **P-Quadratic-Strain** (the strain reading, `Paper_QuadraticStrain_v1`), the **§5.3 regime assumption** that the cross-term dominates in deep-MOND (restored 2026-09-04 after `Paper_QuadraticStrain_v1` §6's removal of it was found inconsistent — `Gravity_TieredClaims_Ledger.md` Staleness #13), and **P-Bilocal-Count** (`N_bilocal = N_horizon = N(R)`, named 2026-09-04 — Staleness #16). This paper's *D conditional on I-030* is accurate and unchanged; the point of naming them is that *"forced-given-030"* otherwise reads as though 030 were settled.
>
> **On the high-acceleration limit, this paper and `Paper_030` use different mechanisms.** §6.3 and preamble item 5 here constrain a **smooth interpolation family** by ephemerides, and §7 is explicit that at solar accelerations the correction is the saturation tail — present and small. `Paper_030` §7.1 instead switches **P14 inactive** above `a₀`, so the term is absent rather than small. **RESOLVED 2026-09-04.** `Paper_030` §7.1/§7.2 have been reworded: its three regimes are now stated as a **scope decomposition** rather than a physical switch — the construction declares itself out of scope in the Newtonian regime instead of turning P14 off — and its §6.3 profile is flagged as a slow-saturating member excluded by this paper's own criterion outside the deep field. **The two papers are therefore not two mechanisms but a limited-scope construction and its completion:** 030 supplies the deep-field law, this paper supplies the crossover and carries the ephemeris constraint. Nothing in the substrate switches off at `a₀`. See Staleness #19.

---

## 5. The Lensing Verdict

**The check.** Galactic lensing must track the MOND potential — the historical killer of relativistic MOND.

**Why this construction is on the right side of history.** The modification is **metric-borne**: §4.2 MONDifies the *metric potential*; matter and light couple universally to $g_{\mu\nu}$; there is no conformal scalar sector. RAQUAL failed lensing because its scalar coupled conformally and conformal factors do not deflect light — the *same* conformal-blindness fact GR-I §6 used to exclude Nordström. TeVeS's vector field was a patch for that disease; **the khronon never has the disease the patch was for.**

**The slip.** The khronon's anisotropic stress is $∼ W' a_{\langle i}a_{j\rangle} = O(|∇Φ|²)$ — second order in the potentials; even deep in the MOND regime its ratio to the leading terms is $O(Φ) ∼ 10^{-6}$ for galaxies. Hence $Φ = Ψ\,[1 + O(Φ)]$, both potentials are the MONDified potential, and the deflection is $∝ 2∫∇_\perp Φ_{\rm MOND}$:

> **Galactic lensing tracks the MOND potential, with no added vector field.** The kill-check passes at leading order — for the same structural reason ED's gravity produced the factor of two: space and time potentials move together.

Caveats: leading-order, static; cluster-scale lensing inherits the MOND shortfall (preamble 8); the slip suppression presumes the healthy perturbations §6 addresses.

---

## 6. Viability: Ghosts, Ellipticity, Screening, and the τ-Mode

### 6.1 No new ghost (structural)

In unitary gauge $a_i = ∂_i\ln N$ — spatial gradients of the lapse only — so the $W$-sector contributes **no time derivatives at any order**. The scalar's time-kinetic structure is the $λ, β$ sector, untouched by the MOND generalization: **the no-ghost condition of the unified theory is the linear khronometric one.** (The $W$-sector can feed the effective kinetic matrix through constraint elimination; that feedback is exactly the §7 degeneracy item, not a second pathology.)

### 6.2 Static well-posedness (the classic conditions)

The perturbed static operator has the AQUAL coefficients; the Bekenstein–Milgrom conditions $μ_{\rm tot} > 0$ and $d(x\,μ_{\rm tot})/dx > 0$ hold across the interpolation — deep IR ($μ = x$) passes both. **The infrared cancellation does not destabilize statics: $W' < 0$ there, but the *total* operator is healthy.**

### 6.3 Screening and the constrained family

Screening is the smallness of the residual, not Vainshtein: at solar accelerations ($x ∼ 10⁷–10⁸$) the force correction is the saturation tail plus $O(α)$ preferred-frame terms. Two channels, kept distinct: the **$α₁, α₂$ channel** (the linear corner; pulsar-tested; the standing GR-II falsification front, unchanged) and the **interpolation-tail channel**, where Cassini-class ephemeris bounds **exclude slow-saturating families** (inverse-power tails at the edge of exclusion; exponential tails survive). The interpolation is thereby a *constrained* family — measured, not protected.

### 6.4 The τ-mode

In unitary gauge the khronon perturbation is eaten: it **is** the breathing scalar GR-II already counted — not a new player. Benign as screened at high accelerations (dipole radiation suppressed with the scalar charge); its deep-IR dynamics (bars, mergers, satellites, wide binaries) are the theory's *predictive* sector. Its only pathology channel is the §7 degeneracy — one soft spot, one address.

---

## 7. The Regulator and the Cosmological Face

### 7.1 The degenerate point is not in ED's state space

The pure-$A²$ sector degenerates as $A → 0$ (vanishing stiffness, slowing modes) — but the configuration $(A, θ) = (0, 0)$ at which the structure fails is **exact Minkowski vacuum, eternal and inert — and ED's substrate forbids exact Minkowski vacuum: the tick never halts.** The khronon's background is the Hubble flow; commitment does not cease (P13, P11). The degenerate point sits on the excluded boundary of the substrate's state space. This is a domain observation, not a modification of $W$ — and it is one of the construction's strongest structural facts: *the substrate's refusal to ever stop ticking is what protects its gravity theory.*

### 7.2 The truncation diagnosis and the regulator family

$W(A²)$ was a truncation: the foliation EFT's invariants are $a$, $θ$, $σ$, and nothing singles out the acceleration as the sole argument of the IR structure. The general sector $\mathcal{W}(A², Θ)$ ($Θ = θ/3H₀$) is **non-degenerate at the physical near-vacuum** $(A → 0, Θ ∼ 1)$, where the expansion supplies the stiffness. The $Θ$-form is **not forced** — the **regulator family**, labeled.

### 7.3 The orthogonality theorem

$θ ≡ 0$ for static congruences, so **every $Θ$-term vanishes identically in statics: the entire tested sector of this paper (§4–§6) is invariant under the regulator choice.** The family is sequestered — it cannot be tuned to help the galactic physics (no leak-back), and the galactic physics cannot vouch for it (no protection). Two independently falsifiable sectors.

### 7.4 The SCBU tie-in, and one tiered resonance

The khronon has exactly one background scale, and it appears in four roles: the background rate ($H₀$), the transition acceleration ($a₀ = cH₀/2π$), the horizon locus ($b → 0$, GR-I), and SCBU's unified boundary ($R_H = c/H₀$). **One scale, four roles: the SCBU boundary acquires a dynamical carrier — its field is the khronon.** And the IR sector's vacuum term is naturally of order

$$
\rho_\Lambda \sim \frac{a_0^2 c^2}{G} \sim \frac{H_0^2 c^2}{G}
$$

— the observed dark-energy order: the long-noticed $Λ ∼ a₀²$ coincidence read as **single-scale consistency** (the khronon's only scale is the cosmic rate, so its vacuum term can only be that size). Tiered hard: form/order-of-magnitude only; the `O(1)` constant is not derived; $Λ ∼ H₀²$ is a consistency relation, not a prediction; and the reconciliation with the corpus's V1-backreaction Λ (Paper_038.5) is open.

### 7.5 Filters on the family

The regulator family carries its own constraints: **BBN** (the $λθ²$ sector renormalizes cosmological $G$; bounded), **gravitational Čerenkov** (admissible members must give $c_s ∼ O(1)$ at the cosmological point — the bare truncation fails this in voids, independently confirming §7.2's diagnosis), and **FRW stability**. Pinning a member is model-building, outside this paper — the same epistemic boundary GR-II drew for the khronon parameters.

---

## 8. Position Relative to the Published Arc — the Fusion

- **Paper_033's scalar is the khronon.** The pre-pivot arc *constructed* a scalar $Φ$ on a postulated metric (both labeled postulates in its own audit); the post-pivot arc *derived* a scalar with exactly the required role and origin. The two gravity programs fuse: Paper_036's MOND field equation is this paper's §4.2 static limit; Paper_033's covariantized equation is its covariant form, with the postulated background replaced by GR-I's metric.
- **Paper_033/034's "deep-MOND superluminality cost" is the khronon's known class character** — what makes universal horizons exist — and not a causal pathology given the foliation: a flagged cost becomes an expected feature.
- **GR-I §7's open item #2 (khronon↔MOND) is hereby closed**; open item #1 (bandwidth↔strain/flow) remains.
- **"Dark matter" in ED**: the galactic phenomenology is carried by the same field that carries the arrow of time — no particle, no added vector, no new primitive; the field was counted (GR-II) before it was needed (here).

---

## 9. The Wedge — Empirical Content

1. **Wide binaries near $a₀$** — the live observational frontier where this theory and Newtonian expectations genuinely diverge; an active measurement program, and the cleanest near-term discriminator.
2. **Dynamical MOND** — the τ-mode's excitation in time-dependent galactic systems is where MOND-class dynamics differ from particle dark matter; predictive territory, not yet computed.
3. **The breathing GW polarization** (GR-II's scalar mode) — now identified as the *same* field that does the galactic work: one detection channel, two phenomenologies.
4. **The constrained families as shrinking falsifiable space** — Cassini on the interpolation; BBN/Čerenkov/FRW on the regulator: the theory's unfixed sectors are being measured, not protected.
5. **What is *not* claimed as a wedge:** clusters and the CMB (owed); the value of $Λ$ (form-tier only); solar-system deviations beyond the standing $α₁, α₂$ front.

---

## 10. Falsification Criteria

### 10.1 Lensing slip in the MOND regime

**Falsifier sentence:** *Observation of a leading-order gravitational slip ($Φ ≠ Ψ$ beyond $O(Φ)$ corrections) in galactic lensing relative to dynamics would falsify §5's metric-borne mechanism — the construction has no vector field to repair it with.*

### 10.2 The Combination-Rule embedding

**Falsifier sentence:** *Galactic data inconsistent with $a = √(a_N a₀)$ in the deep field (or BTFR slope-4 with the inherited $a₀$) falsifies the deep-IR matching — and with it the unification, since the deep-IR form is forced-given-030.*

### 10.3 Wide binaries

**Falsifier sentence:** *Wide-binary samples near $a₀$ showing purely Newtonian behavior at the precision where the deep-IR branch predicts deviation would falsify the unscreened sector.*

### 10.4 The interpolation family closes

**Falsifier sentence:** *Ephemeris (Cassini-class) bounds tightening to exclude all interpolation members compatible with the two fixed asymptotics would falsify the construction's middle — there is no mechanism here to evade the static sector's own equation.*

### 10.5 The AQUAL conditions

**Falsifier sentence:** *A demonstration that $μ_{\rm tot} > 0$ or $d(xμ_{\rm tot})/dx > 0$ must fail somewhere on the physical interpolation would falsify static well-posedness (§6.2).*

### 10.6 The regulator family empties

**Falsifier sentence:** *A proof that no $𝒲(A², Θ)$ member simultaneously satisfies BBN, Čerenkov, and FRW-stability filters while remaining $Θ$-trivial in statics would falsify the §7 resolution of the degeneracy — returning the $A → 0$ soft spot to the theory's ledger as unresolved.*

### 10.7 Preferred-frame parameters (standing)

**Falsifier sentence:** *The GR-II preferred-frame front is resolved in companion work GR-IV — $α₂ = 0$ exactly (both cones luminal) and $α₁ = −4λ_{local}$ density-suppressed (safe by ≥70 orders). This unification adds no protection of its own and needs none; the front stays live as a test — a measured $α₁ ≳ 10⁻⁵$, or any nonzero $α₂$, kills the theory.*

---

## 11. Position Statement

**Event-Density gravity is one khronometric theory, and its dark-matter phenomenology is the deep-infrared regime of the khronon — the arrow of time made dynamical.** Given the inherited ends — the khronon and its cosmic anchoring (GR-II), the metric and lapse (GR-I), the scale $a₀ = cH₀/2π$ (Paper_029) and the deep-field law (Paper_030) — the khronometric acceleration sector with a general kinetic function reduces, in the static weak field, to the AQUAL equation in the metric potential; the high-acceleration limit is GR-I (enforced by commitment-linearity); the deep-infrared limit embeds the Combination Rule and BTFR (forced-given-030, with the infrared cancellation surfaced); lensing tracks the MOND potential with no added vector; no new ghost arises; the classic ellipticity conditions hold; screening is PPN-safe with a Cassini-constrained interpolation family; the $A → 0$ degeneracy is resolved at the level of ED's state space (no Minkowski vacuum) and EFT generality (the sequestered regulator family); and the khronon's cosmological face carries SCBU's one scale in four roles, with a vacuum term naturally of the observed dark-energy order (form-tier).

**What this paper claims.** The unification: the corpus's MOND sector and its curvature sector are one khronometric theory; the postulated scalar of Paper_033 is the derived khronon of GR-II; the deep-field law is embedded, the historical kill-checks (lensing foremost) pass structurally, and the open sectors are honest, sequestered, and independently constrained families.

**What this paper does not claim.** The MOND exponent is not derived from primitives (forced-given-030); $a₀$ and $G$ are inherited; no value of $Λ$ is derived; no interpolation or regulator member is selected; the class's stability corners are cited, not re-verified; clusters and the CMB are not addressed; and the primitives-level origin of the deep-infrared branch — *why* the substrate's response goes geometric-mean below the cosmic rate — remains the deepest declared open question.

**Series context.** Paper KM-I of the post-pivot curvature-emergence line, companion to GR-I and GR-II — and the fusion point with the published gravity arc (Papers 025–038). The remaining work is phenomenology (pin the rule; pin the families; compute the dynamical MOND sector) and the guarded origin question.

KM-I completes the unification GR-I and GR-II opened: **one scalar, one scale, one gravity.**

---

## Appendix: Cross-References, Glossary, Reader Map

### Cross-references

- **Paper_087:** position paper (13 primitives).
- **Papers_028/029/030/031/036:** decoupling surface; $a₀$; Combination Rule; BTFR; MOND field equation. *(the deep-field end)*
- **Paper_033/034:** scalar-tensor covariantization; deep-MOND superluminality. *(fused/reframed here)*
- **Paper GR-I:** bandwidth metric; lapse; weak-field Einstein tests. *(the high-acceleration end)*
- **Paper GR-II:** the khronometric class; the khronon; GW and Lorentz safety. *(the field)*
- **SCBU:** the $R_H = c/H₀$ boundary — here acquiring its dynamical carrier.

### Glossary

- **Khronon.** The preferred-foliation scalar (GR-II): ED's arrow made dynamical; background = cosmic time.
- **Congruence acceleration $a_μ$.** $⊥∇_μ\ln\sqrt{X}$; the kinetic invariant of the MOND sector.
- **Bandwidth–Acceleration Lemma.** In statics, $a_i = ∂_i\ln N = ½∂_i\ln b$ — the khronon's acceleration *is* the logarithmic bandwidth gradient (via GR-I's $N² ∼ b$). The substrate reading of the MOND sector.
- **$W(A²)$ / $𝒲(A², Θ)$.** The acceleration kinetic function and its regulated completion; $μ_{\rm tot} = 1 + c_{1W}'$.
- **Forced-given-030.** The deep-IR form is uniquely fixed by matching the corpus's independently-derived Combination Rule — an embedding, not a primitives derivation.
- **The infrared cancellation.** $W' → -1/c_1$ as $A → 0$: the khronon takes over the static constraint below $a₀$; standard-in-class, the construction's delicate piece.
- **Orthogonality theorem.** $θ ≡ 0$ in statics ⟹ the regulator family is invisible to everything tested.
- **Regulator family.** The $Θ$-sector of $𝒲$: open, sequestered, filtered by BBN/Čerenkov/FRW stability.
- **One scale, four roles.** $H₀$ as the khronon background rate, $a₀$, the $b→0$ horizon, and the SCBU boundary.
- **Deep field.** The khronon's `A ≲ 1` regime — ED's account of dark-matter phenomenology.

### Reader map and open work

**Where to look next.**
- *The metric and the classical tests:* GR-I. — *The class, GW speed, Lorentz safety:* GR-II.
- *The deep-field laws this paper embeds:* Papers 029/030/031/036.
- *The cosmological face and the boundary:* SCBU.

**Open work** (declared): the primitives-level origin of the deep-IR branch (guarded); pinning the interpolation and regulator families (model-building; Cassini/BBN/Čerenkov/FRW filters active); the dynamical MOND (τ-mode) sector; the V1-backreaction ↔ khronon-vacuum reconciliation for Λ; the bandwidth↔strain/flow substrate-route identification (GR-I §7 item #1); clusters and the CMB (owed; address named — the $Θ$-sector's cosmology).

---

**End of Paper KM-I.**

*Post-pivot curvature-emergence line, fusion point with the published gravity arc. The khronon — the arrow made dynamical — carries ED's dark-matter phenomenology: GR at high accelerations (enforced), the Combination Rule and BTFR below $a₀$ (embedded, forced-given-030), lensing correct with no added vector (metric-borne), no new ghost, PPN-safe, with the $A→0$ degeneracy resolved at the state-space and EFT-generality level and the regulator sequestered by the orthogonality theorem. One scale ($H₀$) in four roles ties the theory to SCBU, and the khronon's vacuum term is naturally of the dark-energy order (form-tier). No particle, no vector, no new primitive. Clusters/CMB owed; origin question guarded.*
