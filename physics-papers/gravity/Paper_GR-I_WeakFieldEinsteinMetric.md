# The Bandwidth Lapse and the Factor of Two: The Weak-Field Einstein Metric in Event Density

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — post-pivot Arc ED-10 (curvature emergence), Paper GR-I
**Status:** Publication draft. Conditional structural derivation within the 13-Primitive Generative System. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **The full Einstein field equation is not derived in this paper.** This paper derives the **weak-field metric** and the three classical weak-field tests. The field-equation *form* and the gravitational *class* (the Lovelock argument and the degrees-of-freedom mode count establishing the khronometric class) are the subject of the companion paper **GR-II** and are only forward-referenced here.
3. **No claim that ED reproduces *pure* General Relativity.** The companion result is that ED gravity is **khronometric** (Hořava infrared class): Einstein's tensor sector plus a preferred-foliation scalar, inherited from the primitive arrow (P11/P13). This paper operates in the regime where khronometric and Einstein gravity **coincide** — the static, weak-field metric — and states the khronometric character explicitly so the Lorentz status is correct from the outset. Departures from pure GR (preferred-frame effects) live in GR-II / phenomenology.
4. **Newton's law, Newton's constant $G$, and the Planck identification $ℓ_{ED} = ℓ_P$ are inherited, not re-derived** (Paper_027, Paper_027.5; form-FORCED / value-INHERITED, M3). This paper builds on that base.
5. **The emergent metric is a coarse-grained (DCGT) object, not a fundamental field.** At substrate-graph scale there is no smooth metric (only edge weights); the metric exists in the thick-regime continuum limit (Paper_073). Consistent with the Contrast-First ontology's "no fundamental metric."
6. **The lapse derivation rests on a stated postulate (P-Commitment-Linear, §2): the commitment rate is linear in the metric-relevant bandwidth ($Γ ∝ b$).** This holds when the P04 commitment-reserve band does not co-scale with the internal band; it is the load-bearing structural commitment selecting the Einstein branch over the conformal (Nordström) branch. It is labeled, not derived.
7. **The factor-of-two simulation (§6) uses an imposed bandwidth profile.** It validates the propagation/lensing mechanism (Fermat / null-geodesic) and the optical-index doubling, **not** the source profile. The source profile follows from the Newtonian (Poisson) limit, which is inherited (Paper_027), not from a strong-field field equation (deferred to GR-II).
8. **This paper sharpens, and does not silently contradict, the published acoustic-metric arc (Paper_033).** Paper_033 *postulates* an unspecified-form acoustic metric and builds a scalar-tensor / relativistic-MOND theory on it. This paper supplies the **explicit** bandwidth metric $g ∼ b⁻¹$ that realizes that postulated background, agreeing at the Newtonian limit and filling in the spatial and lapse structure Paper_033 left open (§7). Two reconciliation items remain open and are declared: the identification of P04 bandwidth with the P02/P03/P06 strain/flow content, and the relation of the khronon to the MOND scalar ($a₀$, BTFR).
9. **The geodesic identity is established for the null sector (front propagation), not the timelike sector.** Perihelion precession (§5.4) follows for *test particles* in the derived metric by the standard geometric argument; the claim that ED's massive-matter worldlines *are* those timelike geodesics is shown here only for null fronts (§4) and is otherwise assumed.

---

## Abstract

Event Density's published gravity arc recovers Newton's law and a relativistic-MOND sector on a *postulated* acoustic metric (Paper_033), leaving the metric's explicit form — and hence the light-bending coefficient — unspecified. This paper supplies the **explicit emergent metric** and derives the **weak-field gravity** it produces. The spatial metric is the bandwidth metric $g_{ij} ∼ b_{ij}⁻¹$ (P04). The new content is the **temporal lapse**: requiring the substrate front (the maximal signal, the null cone) to be null on $g_{ij} ∼ b⁻¹$, together with the certified commitment-rate law $Γ_{commit} ∼ b_{int}/reserve$ — linear in bandwidth (postulate **P-Commitment-Linear**, §2) — forces

$$
N^2 \sim b .
$$

Hence $g_{00}\,g_{rr} \sim (-b)(b^{-1}) = -1$ — the **Schwarzschild relation**, the Einstein branch, not the conformal (Nordström) one. Combining this relation with the inherited Newtonian limit $∇²b ∼ ρ$ (Paper_027) assembles the **weak-field Schwarzschild metric** $g_{00} = -(1 - r_s/r)$, $g_{rr} = (1 - r_s/r)^{-1}$. From it follow the three classical tests: the **factor-of-two light bending** (the optical index is $n_{opt} ∼ b^{-1}$, the *square* of the spatial-only index, so the deflection is exactly twice the Newtonian value; a self-contained eikonal simulation confirms $α ∝ r_s/ξ$ with an Einstein/Newtonian ratio of 2.09 versus 2.000, and zero for the conformal control), **gravitational redshift** ($N ∼ b^{1/2}$, a free corollary), and **perihelion precession** (test particles in the derived metric). The leading-order metric coincides with General Relativity's; the paper makes no claim of the full field equation (GR-II), no claim of pure GR (the gravity is khronometric — Einstein-class at weak field), and no claim that $G$, $ℓ_P$, or the commitment-rate linearity are derived rather than inherited or postulated.

---

## 1. Introduction

### 1.1 What this paper does

ED's flat-spacetime gravity arc (Papers 025–031) recovers Newton + the MOND transition acceleration + BTFR; Paper_033 covariantizes it as a scalar-tensor theory on a **postulated** acoustic metric. The metric's explicit form was left unspecified, and with it the spatial curvature that decides whether light bends by the Newtonian amount or the (twice-larger) Einstein amount. This paper closes that gap in four steps:

1. The explicit emergent **spatial** metric $g_{ij} ∼ b⁻¹$ (§3).
2. The **temporal lapse** $N² ∼ b$, derived from the commitment-rate law and the null condition (§4) — the core new result.
3. The **weak-field metric** assembled from the lapse + the inherited Newtonian profile, yielding the Schwarzschild relation (§5).
4. The **three classical tests**, including the **factor of two** (§5–§6), with a simulation validating the lensing mechanism.

### 1.2 Why this matters

The factor of two in light bending is the historical discriminator between Newtonian/scalar gravity (which bends light half as much) and Einstein gravity (which bends it twice as much, because space curves as much as time). A substrate theory that recovers Newton but not the factor of two would be sub-Einstein; one that recovers it has reproduced the first genuinely *relativistic* gravitational prediction. This paper shows ED lands on the Einstein value, and locates exactly why: the same bandwidth field sets both the spatial metric and the temporal lapse, so space and time curve together.

### 1.3 How this fits the arc

- **Paper_027 / 027.5:** Newton's law; $G = c³ℓ_P²/ℏ$; $ℓ_{ED} = ℓ_P$. *(inherited base)*
- **Paper_033:** scalar-tensor acoustic-metric covariantization (postulated metric; pre-pivot). *(this paper sharpens)*
- **Paper GR-I (this paper):** the explicit bandwidth metric + weak-field Einstein tests.
- **Paper GR-II (companion):** the field-equation form (Lovelock) and the gravitational class (mode count → khronometric); Lorentz safety.

This is the first paper of the post-pivot curvature-emergence line: where Paper_033 *posited* a metric and got MOND, this paper *derives* a metric and gets the weak-field Einstein tests.

### 1.4 Conventions and regime of validity

**Conventions.** Metric signature $(−,+,+,+)$; static coordinates; $c = 1$ where convenient. The weak-field metric is written in **isotropic gauge**: $ds² = −(1 + 2Φ)\,dt² + (1 − 2Φ)\,δ_{ij}\,dx^i dx^j$. The Schwarzschild-gauge form used in §5.3 ($g_{rr} = (1 − r_s/r)^{-1}$) is the same metric in a different radial coordinate and agrees with the isotropic form to the weak-field order computed; the relation $g_{00}\,g_{rr} ∼ −1$ is the gauge-robust content that distinguishes the Einstein branch from the conformal one.

**Regime of validity.** Every result here is **static**, **weak-field**, **spherically symmetric**, and lives in the **continuum (DCGT) limit** of the substrate (Paper_073). No strong-field, time-dependent, or non-spherical claim is made: the vacuum profile (§5.2) is the Newtonian-order $1/r$, the metric is its leading weak-field completion, and the full nonlinear / strong-field field equation is deferred to GR-II. The factor-of-two simulation (§6) is an imposed-profile validation of the propagation mechanism, not a strong-field solution.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02 (reciprocal adjacency), P04 (four-band bandwidth), P05 (adjacency transport), P11 (commitment irreversibility), P13 (homogeneous tick). Load-bearing as in the Phase-3 analysis.

**Kernel dependence:** V1 finite-width retarded structure (Paper_089) for the causal/temporal sector; the finite-width bandwidth-limit speed supplies the light cone.

**Paper-specific postulate (labeled per QC discipline):**

> **Unaffected by the bands' relational reading — checked 2026-09-06.** Ledger #93 established that the four band classes are disjoint only *relative to a choice of system `S`*, which makes the **partition** relational. **This postulate is not exposed to that.** Its two quantities are **`b_int(C)`** and **`b_com(C)`** (the commitment reserve), and in the source concept's own signatures both are **functions of the chain alone — cut-independent**; only `b_adj(C, N)` and `b_env(C, E)` carry the cut. **The lapse derivation and its falsifier stand untouched.** `foundations/Note_RelationalBands_Sweep_2026-09-06.md`; gravity ledger #97.

- **P-Commitment-Linear (commitment rate linear in bandwidth):** *The substrate commitment rate $Γ_{commit} ∼ b_{int}/reserve$ (commitment.md) is linear in the metric-relevant bandwidth, $Γ ∝ b$, to leading order.* This holds when the P04 commitment-reserve band does not co-scale with the internal band (P04 lists them as distinct bands). With $Γ ∝ b^α$, the lapse is $N² ∼ b^{2α-1}$: **α = 1 gives the Schwarzschild/Einstein relation; α = 0 gives the conformal/Nordström one.** P-Commitment-Linear selects α = 1. It is a substrate-level structural commitment, **not** derived from the four-band law alone, and labeled here for transparency. The exact reserve dynamics that would fix α are deferred to GR-II.

**Why linearity is the natural choice (and the alternatives are not).** Three considerations select $α = 1$, none of which is a fit to a desired answer. *(i) The rate's own form.* $Γ_{commit} ∼ b_{int}/reserve$ is the internal bandwidth divided by a reserve budget; treating the reserve as a roughly fixed budget (a *distinct* P04 band) makes $Γ$ rise in direct proportion to the available internal bandwidth — linearity is the leading, unforced reading. *(ii) $α = 0$ (conformal/Nordström) is physically implausible.* It requires the commitment rate to be *independent* of bandwidth — equivalently, the reserve to track the internal band exactly so their ratio is constant — i.e. a front that commits no faster where there is more capacity, contradicting the meaning of bandwidth as commitment capacity. It is also the branch that bends no light at all (conformally-flat metrics are non-lensing, §6.3). *(iii) $α ≠ 1$ breaks the null-cone identification.* Any $α ≠ 1$ gives $N² ∼ b^{2α-1} ≠ b$, so the front's coordinate speed ($∝ Γ ∝ b^α$) and the lapse no longer combine, through the null condition (§4), into a single $b$-controlled cone; the spatial and temporal curvatures cease to be locked to one field, and the Schwarzschild relation $g_{00}g_{rr} ∼ −1$ is lost. Linearity is the unique exponent for which one field $b$ controls one consistent causal cone — the structure §6 needs for the factor of two.

**Upstream paper dependencies:**

- **Paper_087:** position paper (13 primitives).
- **Paper_027 / 027.5:** Newton recovery; $G$; $ℓ_{ED} = ℓ_P$.
- **Paper_033:** acoustic-metric postulate (sharpened here).
- **Paper_073:** DCGT continuum-limit bridge.
- **Paper_089:** V1 finite-width kernel (cone / lapse-speed).

**Empirical / value-layer inputs (inherited, not derived):**

- **Newton's constant $G = c³ℓ_P²/ℏ$** and **$ℓ_{ED} = ℓ_P$** — value-INHERITED (Paper_027/027.5).
- **The source distribution $ρ$** (matter / event density) — astrophysical input.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Newton's law / Poisson $∇²Φ = 4πGρ$ | I | Paper_027 |
| $G = c³ℓ_P²/ℏ$, $ℓ_{ED} = ℓ_P$ | I | Paper_027/027.5 (M3; value-inherited) |
| Emergent spatial metric $g_{ij} ∼ b⁻¹$ | **D** | §3 — explicit bandwidth realization of the Paper_033 acoustic-metric postulate; symmetric (P02), bulk-positive, degenerates at $b→0$ (horizons) |
| Front = null cone (maximal signal) | D | §4.1 — bandwidth-limit speed (V1 / Paper_089) is the substrate's maximal signal speed |
| Commitment rate $Γ ∝ b$ | **P (P-Commitment-Linear)** | §2 postulate; selects the Einstein branch (α = 1) over conformal (α = 0) |
| Lapse $N² ∼ b$ | **D conditional on P-Commitment-Linear** | §4.2 — front-null condition with $g ∼ b⁻¹$ and $dx/dt = Γ ∝ b$ |
| Schwarzschild relation $g_{00} g_{rr} ∼ -1$ | D | §5.1 from $N²∼b$, $g_{rr}∼b⁻¹$ |
| Vacuum profile $b = 1 - r_s/r$ | D conditional on I | §5.2 from inherited Newtonian $∇²b ∼ ρ$ ($∇²b = 0$ in vacuum) |
| Weak-field Schwarzschild metric | D | §5.3 (relation + profile) |
| Optical index $n_{opt} ∼ b⁻¹$ | D | §6.1 from $g_{rr}∼b⁻¹$, $N²∼b$ |
| Factor-of-two light bending | **D + simulation** | §6.2 — $n_{opt}$ is the square of the spatial index; eikonal sim confirms ratio 2.09 vs 2 |
| Gravitational redshift | D | §5.4 corollary of $N ∼ b^{1/2}$ |
| Perihelion precession | D (test-particle) | §5.4 standard geometry in the derived metric; timelike-worldline identity assumed (preamble 9) |
| Imposed $b$-profile in the sim | regime / I | §6 — profile from inherited Newtonian limit, not a strong-field field equation |
| Full field equation / gravity class | **deferred** | GR-II (Lovelock + mode count) |
| Metric is khronometric (Lorentz status) | I-from-GR-II | stated, not derived here; this paper works in the GR-coincident weak-field regime |

All load-bearing steps are P, D, I, deferred, or labeled regime. *The single new postulate is P-Commitment-Linear; the single simulation validates a mechanism on an inherited-limit profile.*

---

## 3. The Emergent Spatial Metric

### 3.1 Bandwidth as the spatial metric

In the four-band bandwidth structure (P04), an edge `(u,v)` carries a reciprocal bandwidth $b_{uv} = b_{vu}$ (P02). Bandwidth measures coupling capacity: high bandwidth = strong coupling = short metric distance. The emergent spatial metric is

$$
g_{ij} \sim b_{ij}^{-1},
$$

with edge metric-length $ℓ ∼ √g ∼ b^{-1/2}$. This is the **explicit** form of the metric that Paper_033 introduced as a postulate (P-AcousticMetric): there the metric was an unspecified Lorentzian background; here it is the inverse bandwidth field, an object built from a single certified primitive.

Three properties hold by construction, and they are the genuineness conditions a metric must satisfy:

- **Symmetric** — $b_{uv} = b_{vu}$ (P02 reciprocal edge record), so $g$ is symmetric.
- **Local** — built from local adjacency/bandwidth (consistent with ED's no-nonlocal-influence).
- **Positive in the bulk, degenerate at horizons** — $b > 0$ gives a positive-definite spatial metric; where $b → 0$ (a decoupling cut), $g → ∞$ — the metric degenerates *exactly* at emergent horizons, the correct behavior, not a defect. This $b → 0$ locus is the same surface the ED horizon literature identifies as a decoupling/saturation boundary (the emergent-boundary A2 and finite-memory-horizon V5 results), so the metric degenerates precisely where ED already places its horizons; the identification (including khronometric "universal horizons") is developed in GR-II.

$g_{ij} ∼ b⁻¹$ is Riemannian (positive-definite) — the **spatial** sector. The Lorentzian (temporal) structure is the content of §4.

### 3.2 Consistency with the Newtonian limit

Writing $g_{00} = -(1 + 2\Phi)$ in the weak field, the inherited Newtonian recovery (Paper_027) is $∇²\Phi = 4πG\rho$. Identifying the bandwidth deviation with the potential, $b ∼ 1 + 2\Phi$, the Newtonian limit reads $∇²b ∼ \rho$. **This identification is the standard weak-field gauge choice (isotropic gauge, §1.4); it is a consistent labeling of the Newtonian potential, not a smuggled GR structure — any gauge-equivalent choice yields the same Poisson equation $∇²Φ = 4πGρ$.** This is the one place Paper_033's postulated metric is constrained, and the bandwidth metric agrees there by construction. The new physics is in the *spatial* part and the *lapse*, which Paper_033 left open.

---

## 4. The Temporal Lapse from the Commitment Rate

### 4.1 The front is the null cone

The substrate front — the propagating locus of new commitments — is the **maximal signal** of the substrate: nothing propagates faster than the finite-width bandwidth-limit speed (V1 / Paper_089). In the emergent metric, the maximal signal travels on the **null cone**. **In a Lorentzian metric the maximal signal speed *defines* the null cone, so identifying the substrate's maximal signal (the front) with the null cone is not an additional assumption but the definition of the emergent causal structure.** So the front worldline satisfies $ds² = 0$. (That front propagation is specifically *geodesic* — the front follows the locally fastest channel, a discrete Fermat principle — is established for the null sector in the Phase-3 analysis and used in §6; here we need only that the front is null.)

### 4.2 The null condition forces $N² ∼ b$

Assemble the static metric $ds² = -N² dt² + g_{ij}\,dx^i dx^j$, with `dt` the homogeneous substrate tick (P13) and $g_{ij} ∼ b⁻¹$ (§3). The front advances $Γ$ edges per tick, where $Γ = Γ_{commit} ∼ b_{int}/reserve$ is the certified commitment rate — linear in bandwidth, $Γ ∝ b$, by **P-Commitment-Linear** (§2). Substituting the front's coordinate velocity $dx/dt = Γ ∝ b$ into the null condition:

$$
0 = -N^2 dt^2 + g_{xx}\,dx^2 = dt^2\!\left(-N^2 + b^{-1}\Gamma^2\right) = dt^2\!\left(-N^2 + b^{-1} b^2\right)
\;\Longrightarrow\; \boxed{N^2 \sim b.}
$$

The lapse is **forced** — not posited — by the commitment-rate law plus the null identification. The general case $Γ ∝ b^α$ gives $N² ∼ b^{2α-1}$, so the result is the single statement that the Einstein branch corresponds to **linear** commitment rate (§2): the physical reading of "commitment rate rises with available bandwidth" selects it; the conformal/Nordström branch would require the rate to *fall* with bandwidth.

**Dimensional check.** $N$ is dimensionless (a lapse / redshift factor); $b$ enters as the dimensionless ratio to its asymptotic value. ✓

### 4.3 Why the lapse matters

The lapse $N$ is not a bookkeeping factor — it carries the relativistic physics, and all three classical tests flow from the single derived relation $N² ∼ b$. (i) It *is* gravitational time dilation: clocks tick at rate $N ∼ b^{1/2}$, which is the redshift (§5.4). (ii) It controls null propagation: the optical metric that bends light is $g_{ij}/(-g_{00}) = g_{ij}/N²$ (§6.1), so the lapse enters the deflection directly. (iii) It is the *entire* difference between Newtonian/scalar and Einstein gravity — a theory with the spatial metric alone gives half the bending; the lapse, fixed by the commitment rate to scale as $N² ∼ b$ in step with $g_{rr} ∼ b⁻¹$, is what doubles it (§6.3). One field $b$ sets both the spatial coupling and the temporal update rate, hence both spatial curvature and the lapse — which is why the two sectors are locked together.

---

## 5. The Weak-Field Metric and Two Classical Tests

### 5.1 The Schwarzschild relation

With $g_{00} = -N² ∼ -b$ (§4) and $g_{rr} ∼ b⁻¹$ (§3):

$$
g_{00}\,g_{rr} \sim (-b)(b^{-1}) = -1.
$$

This is the **Schwarzschild relation** — exactly the relation between the time and radial components of the Schwarzschild metric ($g_{00} g_{rr} = -1$), and the signature of the Einstein branch. The conformal (Nordström) branch, $g_{00} ∼ -g_{rr}$, is excluded: it would require $N² ∼ b⁻¹$, the non-linear commitment rate `P-Commitment-Linear` forbids.

### 5.2 The vacuum profile

The inherited Newtonian limit (§3.2) $∇²b ∼ ρ$ gives, in vacuum ($ρ = 0$), $∇²b = 0$, whose spherically-symmetric solution is

$$
b(r) = 1 - \frac{r_s}{r}, \qquad r_s \propto M.
$$

The $1/r$ profile is the standard Newtonian potential; $r_s$ is the (value-inherited) gravitational radius. This profile is the Newtonian-order input; the full nonlinear determination is GR-II.

### 5.3 The weak-field Schwarzschild metric

Combining the relation (§5.1) and the profile (§5.2):

$$
g_{00} = -\left(1 - \frac{r_s}{r}\right), \qquad g_{rr} = \left(1 - \frac{r_s}{r}\right)^{-1}.
$$

This is the **weak-field Schwarzschild metric** — the metric of General Relativity in the weak field. It is no longer postulated (as in Paper_033) but assembled from the bandwidth metric, the commitment-rate lapse, and the inherited Newtonian profile.

### 5.4 Gravitational redshift and perihelion precession

Two classical tests follow immediately:

- **Gravitational redshift (free corollary).** Clocks run at rate $N ∼ b^{1/2}$. Near a source the bandwidth is depleted ($b < 1$), so $N < 1$: clocks run slow and light climbing out is redshifted, with the standard $\Delta\nu/\nu \approx \Phi$. Correct sign and law, from the same derived lapse.
- **Perihelion precession (test particle).** Timelike geodesics of the derived metric (§5.3) precess by the standard GR amount $\Delta\varpi = 6\pi GM/(c^2 a(1-e^2))$ per orbit. This follows by the textbook geometric calculation in the Schwarzschild metric. **The identification of ED's massive-matter worldlines with these timelike geodesics is *assumed* here and is tested in GR-II** (where the geodesic identity is extended from the null front to the matter sector via the stress tensor). This paper derives the precession only as a property of the *metric* — established here for null fronts (§4) — not yet as a property of ED's massive-matter dynamics.

The third and sharpest test — light bending — is §6.

---

## 6. The Factor of Two

### 6.1 The optical index

Light deflection in a static metric is governed by the **optical metric** $g^{opt}_{ij} = g_{ij}/(-g_{00})$, whose index is

$$
n_{opt} = \frac{\sqrt{g_{rr}}}{N} \sim \frac{b^{-1/2}}{b^{1/2}} = b^{-1}.
$$

The optical index is $b⁻¹$ — the **square** of the spatial-only index $b^{-1/2}$. This is the crux: the spatial metric and the temporal lapse, *both built from $b$*, contribute equally to bending.

### 6.2 The deflection doubles — derivation and simulation

Weak-field deflection is $α ∝ ∫ ∇_⊥ \ln n$. Since $\ln(b^{-1}) = 2\ln(b^{-1/2})$, the deflection from the full optical index is **exactly twice** the deflection from the spatial part alone — the Einstein factor of two. Quantitatively, for $b = 1 - r_s/r$, $α = 2 r_s/\xi$ at impact parameter $ξ$ (versus the Newtonian $r_s/\xi$).

A self-contained eikonal ray-tracer (front = ray in index field, $dT/ds = ∇_⊥\ln n$) confirms it across three index classes:

| index class | $C = α·ξ$ (sim) | prediction |
|---|---|---|
| spatial-only / Newtonian $n = b^{-1/2}$ | −1.07 | $-r_s$ |
| **Einstein / optical $n = b^{-1}$** | **−2.24** | $-2 r_s$ |
| conformal / Nordström $n = 1$ | 0.00 | `0` |

The Einstein/Newtonian ratio is **2.09** (the ~4% excess is finite-$r_s$ weak-field curvature, not a physical deviation); the conformal control is exactly zero; the deflection is $∝ r_s/\xi$ and $∝ M$, the gravitational-lensing signature. **The simulation validates the propagation mechanism on the inherited-limit profile (§5.2); the profile itself is not re-derived here (preamble 7).**

**Reproducibility.** The ray-tracer integrates the eikonal equation $dT/ds = (1/n)[∇n − (∇n·T)\,T]$ (equivalently $dT/ds = ∇_⊥ \ln n$) by explicit first-order (Euler) steps in arc length $s$, renormalizing the unit tangent $T$ after each step. Parameters: step $ds = 0.02$; source strength $r_s = 1$ with softened profile $b(r) = 1 − r_s/r$ (core regulator $10⁻³$); index $n(r) = b(r)^p$ with $p ∈ {−1/2, −1, 0}$ for the three classes; rays launched in the asymptotically flat region at $x = −400$ (in units of $r_s$) with impact parameters $ξ ∈ {10, 15, 20, 30, 40, 60, 80}$ and integrated to $x = +400$, where $b → 1$; the deflection is the asymptotic tangent angle. There is no spatial grid and no reflecting/periodic boundary — propagation is free in the imposed static index field. Scripts: `gr_lensing_test.py`, `gr_einstein_factor.py`.

### 6.3 Why the factor is two and not one

Newtonian or pure-scalar gravity curves *time* (a $g_{00}$ potential) but leaves space flat, giving half the deflection. Pure conformal (Nordström) gravity curves space and time *equally and oppositely*, so the optical effects cancel and light does not bend at all. Einstein gravity curves space as much as time *in the same sense*, doubling the deflection. ED lands on the Einstein case because **one field, $b$, sets both sectors** ($g_{rr} ∼ b⁻¹$, $N² ∼ b$), with the commitment-rate lapse fixing the sign that makes them reinforce rather than cancel. The factor of two is the fingerprint of that single-field origin.

*Historical note.* The factor of two is the discipline's classic discriminator. Soldner (1801), and Einstein's first attempt (1911) using only the time potential $g_{00}$, gave the Newtonian value $2GM/c²ξ$; Einstein's 1915 result, adding the *equal spatial curvature*, doubled it to $4GM/c²ξ$, confirmed by Eddington in 1919. Relativistic-MOND covariantizations had to **add a vector field** (e.g. TeVeS) precisely to install the spatial curvature and recover the factor of two. ED reaches it from a single field because $b$ sets both sectors at once — no added vector required.

---

## 7. Position Relative to the Published Acoustic-Metric Arc

This paper sharpens, and does not contradict, Paper_033. The relationship is precise:

- **Paper_033 postulates the metric.** Its acoustic metric is introduced by P-AcousticMetric (labeled a postulate in its own audit), with unspecified form. **The key fact that dissolves any "two metrics" worry: Paper_033 never computes the spatial curvature or the light-bending coefficient at all** — its only metric-level constraint is the Newtonian limit, so there is no published value for this paper to contradict, only an unspecified slot for it to fill.
- **This paper derives the metric.** $g ∼ b⁻¹$ is explicit, agrees with Paper_033 at the Newtonian limit, and supplies what Paper_033 left open: the spatial part (Einstein factor of two) and the lapse ($N² ∼ b$). The bandwidth metric is the **explicit realization** of Paper_033's postulated background, sharpening "unspecified Lorentzian background" into "Einstein-class at weak field."
- **The Lorentz status.** Because the lapse comes from the commitment-rate law, the metric carries a preferred-foliation (khronometric) structure — Einstein-class at weak field, but not pure GR. This is stated here and derived in GR-II. It revises Paper_033's implicit Lorentz-covariance into a khronometric structure that *coincides with GR in the regime this paper treats*.

**Two reconciliation items remain open and are declared, not hidden:**

1. **Substrate-route identification.** This paper builds the metric from P04 bandwidth; Paper_033 attributes the (postulated) metric to P02/P03/P06 strain/flow. Whether $b$ is fixed by the strain/flow content — so the two substrate routes yield the same metric — is unproven. (Paper_033 never carried out the strain→metric construction either, so this is "two routes agreeing at Newtonian order," not two incompatible explicit metrics.)
2. **The MOND sector.** Paper_033's relativistic-MOND content ($a₀ = cH₀/2π$, BTFR) lives in a scalar field with a MOND interpolation. The companion khronometric picture (GR-II) carries a preferred-foliation scalar (the khronon); whether that scalar reproduces $a₀$ and BTFR — unifying the Einstein-at-solar-scale and MOND-at-galactic-scale regimes — is open and is the natural next target.

---

## 8. The Wedge — Empirical Content

At weak field the derived metric **coincides with General Relativity**, so this paper makes no wedge claim *against* GR at solar-system scale: light bending (factor of two), redshift, and precession match GR by construction of the weak-field Schwarzschild metric. The empirical content of this paper is therefore **internal and structural**:

1. **ED recovers the factor of two** — the first genuinely relativistic gravitational prediction — from a single substrate field, not by adding a vector (as relativistic-MOND covariantizations such as TeVeS must). This is a non-trivial consistency that a sub-Einstein substrate theory would fail.
2. **The mechanism is sign-and-coefficient-definite**, tied to `P-Commitment-Linear`: a substrate-level demonstration that the commitment rate is *not* linear in bandwidth would push ED off the Einstein branch toward Nordström (no bending) — a sharp internal falsifier (§9).

The *external* wedge against GR — preferred-frame effects, the scalar gravitational-wave sector — is khronometric and lives in GR-II / phenomenology, where ED and pure GR diverge.

---

## 9. Falsification Criteria

### 9.1 Commitment rate not linear in bandwidth

**Falsifier sentence:** *A substrate-level demonstration that the commitment rate $Γ_{commit}$ is not linear in the metric-relevant bandwidth ($α ≠ 1$) — e.g. that the commitment-reserve band co-scales with the internal band, giving $α = 0$ — would falsify P-Commitment-Linear, hence the lapse $N² ∼ b$, hence the Schwarzschild relation, and would push ED's weak-field gravity off the Einstein branch (toward conformal/Nordström, no light bending).*

### 9.2 Spatial metric not $b⁻¹$ (wrong light-bending coefficient)

**Falsifier sentence:** *A substrate-level emergent metric whose spatial part is not $g_{ij} ∼ b⁻¹$ — e.g. a flat spatial part ($g_{ij} ∼ δ_{ij}$) — would give the Newtonian (half) light-bending coefficient rather than the Einstein (factor-of-two) value, falsifying §6.*

### 9.3 Front not null / not the cone

**Falsifier sentence:** *A substrate-level analysis showing the front (maximal signal) is not identified with the metric null cone would invalidate the §4.2 lapse derivation.*

### 9.4 Bandwidth metric disagrees with the acoustic metric beyond Newtonian order

**Falsifier sentence:** *A demonstration that the P04 bandwidth metric and the P02/P03/P06 strain/flow content yield different metrics beyond the Newtonian limit (where both are pinned) would falsify the §7 identification of $g ∼ b⁻¹$ as the explicit realization of the Paper_033 acoustic background.*

### 9.5 Light bending not the factor of two

**Falsifier sentence:** *Empirical observation of solar-system light bending inconsistent with the GR factor of two (beyond the established $4GM/c²ξ$) would falsify the derived weak-field metric — though this is also a falsifier of GR itself, with which the derived metric coincides at weak field.*

---

## 10. Position Statement

The **weak-field Einstein metric** is a downstream structural derivation in the ED Generative Primitives System. Given the postulated primitives + the inherited Newtonian base (Paper_027) + the explicit bandwidth metric $g ∼ b⁻¹$ + the postulate that the commitment rate is linear in bandwidth (P-Commitment-Linear), the weak-field metric follows:

- spatial metric $g_{ij} ∼ b⁻¹$ (§3);
- lapse $N² ∼ b$ from the commitment-rate law and the null condition (§4);
- Schwarzschild relation $g_{00} g_{rr} ∼ -1$ (§5.1) + inherited Newtonian profile (§5.2) → weak-field Schwarzschild metric (§5.3);
- factor-of-two light bending (§6), gravitational redshift (§5.4), perihelion precession (§5.4).

**What this paper claims.** Given the inherited Newtonian base and P-Commitment-Linear, the ED weak-field metric is the Schwarzschild metric, and ED reproduces the three classical weak-field tests — including the factor of two — from a single substrate field. It supplies the explicit metric that Paper_033 postulated.

**What this paper does not claim.** The 13 primitives are not derived; $G$ and $ℓ_P$ are inherited; `P-Commitment-Linear` is postulated, not derived; the source profile is the inherited Newtonian limit, not a strong-field field-equation solution; the full field equation and the gravitational class (khronometric) are deferred to GR-II; and ED gravity is **not** pure General Relativity — it is khronometric, coinciding with GR in the weak-field regime treated here. The bandwidth↔strain/flow and khronon↔MOND identifications remain open (§7).

**Series context.** Paper GR-I of the post-pivot curvature-emergence line. The companion **GR-II** derives the field-equation form (Lovelock) and the gravitational class (mode count → khronometric), and addresses Lorentz safety.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper_027 / 027.5:** Newton recovery; $G = c³ℓ_P²/ℏ$; $ℓ_{ED} = ℓ_P$.
- **Paper_033:** acoustic-metric scalar-tensor covariantization (postulated metric; sharpened here).
- **Paper_073:** DCGT continuum-limit bridge.
- **Paper_089:** V1 finite-width retarded kernel (cone / bandwidth-limit speed).
- **GR-II (companion):** field-equation form + gravitational class (khronometric) + Lorentz safety.

### Glossary

- **Bandwidth metric $g_{ij} ∼ b⁻¹$.** The emergent spatial metric, inverse of the P04 edge bandwidth.
- **Lapse $N$.** The $\sqrt{-g_{00}}$ factor; here derived as $N² ∼ b$.
- **Commitment rate $Γ_{commit} ∼ b_{int}/reserve$.** The certified rate at which a front commits; taken linear in $b$ (P-Commitment-Linear).
- **Schwarzschild relation $g_{00} g_{rr} ∼ -1$.** The time–radial metric relation characteristic of the Einstein (not conformal) branch.
- **Optical index $n_{opt} ∼ b⁻¹$.** The light-propagation index; the square of the spatial index, hence the factor of two.
- **Factor of two.** The Einstein light-bending coefficient ($4GM/c²ξ$), twice the Newtonian value; arises because $b$ sets both spatial and temporal sectors.
- **Null front.** The substrate front — the propagating locus of new commitments — identified with the null cone of the emergent metric because it is the substrate's maximal signal (§4.1).
- **Khronometric.** Einstein's tensor sector plus a preferred-foliation scalar; ED's gravitational class (GR-II), coinciding with GR at weak field.

### Reader map and open work

**Where to look next.**
- *The field equation and gravitational class (khronometric):* GR-II.
- *Lorentz safety, gravitational-wave speed, preferred-frame phenomenology:* GR-II.
- *The MOND sector ($a₀$, BTFR) and its relation to the khronon:* Paper_033 + GR-II.
- *The substrate-route identification ($b$ ↔ strain/flow):* the reconciliation memo.

**Open work** (declared, not hidden): (1) derive $b$ from the P02/P03/P06 strain/flow content, closing the substrate-route gap (§7); (2) fix the reserve dynamics that pin $α = 1$ in P-Commitment-Linear (§2); (3) the strong-field / nonlinear regime and the timelike-geodesic identity (GR-II); (4) the khronon ↔ MOND unification (§7).

---

**End of Paper GR-I.**

*Post-pivot curvature-emergence line. Weak-field Einstein metric from the bandwidth metric + the commitment-rate lapse. Headline: $N² ∼ b ⟹ g_{00} g_{rr} ∼ -1$ (Schwarzschild relation) and the factor-of-two light bending, from a single substrate field; the explicit realization of Paper_033's postulated acoustic metric. Field equation and gravitational class: GR-II.*
