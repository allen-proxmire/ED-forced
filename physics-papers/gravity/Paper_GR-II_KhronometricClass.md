# The Arrow's Fingerprint: Event-Density Gravity is Khronometric, GW-Clean, and Lorentz-Safe

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — post-pivot Arc ED-10 (curvature emergence), Paper GR-II
**Status:** Publication draft. Conditional structural derivation within the 13-Primitive Generative System. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/gravity/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **The Einstein field equation is not derived by direct tensor computation.** This paper establishes the field-equation *form* by a uniqueness argument (Lovelock's theorem), which is *conditional*; the one open condition is then resolved by a degrees-of-freedom count. The result is **not** pure General Relativity (see 3).
3. **ED gravity is not pure General Relativity.** The mode count (§5) identifies one propagating scalar beyond the metric — a preferred-foliation "khronon" inherited from the primitive arrow (P11/P13). ED's gravitational class is therefore **khronometric** (Hořava infrared class): Einstein's two tensor modes plus the khronon. It coincides with GR in the static weak field (Paper GR-I) and departs in the preferred-frame sector.
4. **The mode count is a structural identification, not a completed linearized-propagator computation.** It argues from the gauge group (the arrow places a preferred foliation in the law, reducing full diffeomorphism invariance to foliation-preserving diffeomorphisms), which fixes the propagating degrees of freedom to 2 tensor + 1 scalar. An explicit linearization of the dynamical-bandwidth rule, which would compute the khronon's propagator and couplings, requires that rule's coefficients, which are not pinned here (deferred).
5. **The khronon parameters (the Lorentz-violation coefficients, the preferred-frame PPN parameters $α₁, α₂$) are not computed *in this paper*.** They are $F$-dependent — they require the explicit linearized dynamical-bandwidth rule, which is model-building, not derivation. This paper establishes what ED's *structure* forces independent of those coefficients, and identifies the preferred-frame sector as the falsification target (§8). *(They are computed in companion work GR-III/GR-IV, and the front resolves favorably — $α₂ = 0$ exactly from the luminal cones, $α₁$ density-suppressed and safe by ≥70 orders; see the §8 forward note.)*
6. **No claim that ED passes every observational test.** The paper shows two structural passes ($c_T = c$; universal rather than differential Lorentz violation) and one $F$-dependent risk (preferred-frame $α₁, α₂$) that it deliberately defers — resolved favorably downstream (GR-IV), not claimed met here.
7. **$κ = 8πG$ and $Λ$ are inherited, not derived.** Lovelock fixes the form; the coefficients are value-inherited ($G$ via Paper_027; $Λ$ as the V1-backreaction term), consistent with the program's stance on constants.
8. **The weak-field metric and the three classical tests are established in Paper GR-I**, not here; this paper inherits them.
9. **This paper sharpens, and does not silently contradict, the published scalar-tensor / MOND arc (Paper_033).** The khronometric structure revises Paper_033's implicit Lorentz-covariance and reframes its "deep-MOND superluminality" as the expected khronon mode; the relation of the khronon to the MOND scalar ($a₀$, BTFR) is open and declared (§9).
10. **The khronometric identification is INFRARED ONLY; ED does not inherit Hořava's ultraviolet behaviour.** "Khronometric (Hořava infrared class)" in §5 is a statement about the *gauge group and mode count* — foliation-preserving diffeomorphisms, 2 tensor + 1 scalar — and nothing more. Hořava gravity's ultraviolet reputation (power-counting renormalizability, and the effective-dimension flow to 2 that it shares with causal dynamical triangulations and asymptotic safety) rests on **anisotropic Lifshitz scaling**, $t \to b^{z}t$ with $z=3$, which deliberately breaks Lorentz scaling in the UV. **ED does no such thing:** its V1 kernel is Lorentz-covariant (Paper_089, Paper_017), i.e. $z=1$, and it regulates the ultraviolet by a completely different route — the substrate grain supplies a physical cutoff at $\ell_P$, so there are no divergences to renormalize (Paper_111). ED and Hořava therefore **agree in the infrared and use opposite ultraviolet strategies**; no UV result of Hořava's transfers to ED, and none is claimed here. *(Added 2026-08-31; the paper previously said nothing either way, leaving the inference available to a reader.)*

---

## Abstract

Paper GR-I derived Event Density's weak-field Schwarzschild metric and the three classical tests. This paper asks what *class* of gravity ED is — what field equation governs it and how it relates to General Relativity. Three structural results, none requiring the explicit dynamical-bandwidth rule. **(1) The field-equation form is forced.** ED has an emergent metric (Paper GR-I), a covariantly conserved rank-2 source (the bandwidth current's typing is fixed by P05 transport + P04 extensivity, giving $∇_μ T^{μν} = 0$ as the geodesic condition for matter), and a second-order field law (the Newtonian limit $∇²b ∼ ρ$). By **Lovelock's theorem**, any 4D metric theory with these properties has the field equation $G^{μν} + Λg^{μν} = κT^{μν}$ — *unless* the gravitational field carries a propagating degree of freedom beyond the metric. **(2) It does.** ED's arrow lives in the *law* (P11 irreversibility, P13 tick), not the boundary conditions, so the substrate singles out a preferred foliation at the level of the dynamics. This reduces full diffeomorphism invariance to foliation-preserving diffeomorphisms — the gauge group of **khronometric** (Hořava infrared) gravity — and the mode count is **2 tensor + 1 scalar**: Einstein's tensor sector plus a preferred-foliation "khronon." ED gravity is khronometric, not pure GR, and the single departure is the fingerprint of the primitive arrow. **(3) The unification protects it.** Because matter and geometry are the *same* bandwidth substrate, every species propagates through one transport (P05) at one cone, so (a) the tensor gravitational-wave speed equals the light speed *structurally* ($c_T = c$, the post-GW170817 constraint as an identity rather than a fine-tuning) and (b) Lorentz violation is **universal, not differential** — removable at leading order, hence safe from the $~10^{-20}$ matter-sector bounds that execute generic Hořava / Einstein-aether theories. The residual, $F$-dependent quantities — the preferred-frame PPN parameters — are the falsification target (§8). The paper makes no claim of pure GR, no claim that the khronon parameters are computed, and no claim that ED passes the preferred-frame tests.

---

## 1. Introduction

### 1.1 What this paper does

Paper GR-I left the gravitational *class* open: it derived the weak-field metric but not the field equation or the relation to GR. This paper closes that in three steps:

1. **Matter conservation = geodesic motion** (§3), supplying the divergence-free source Lovelock needs.
2. **The field-equation form via Lovelock** (§4) — forced, conditional on one open condition.
3. **The mode count** (§5) — the open condition fails by one scalar; ED gravity is **khronometric**. Then its two saving graces: **GW-clean** (§6) and **Lorentz-safe** (§7), both structural; and the **residual** falsification target (§8).

### 1.2 Why this matters

The deepest question about an emergent-gravity program is not "does it recover Newton" (GR-I) but "is it General Relativity, and if not, what is it, and is that survivable." The honest answer here is the most interesting one: ED is *not* pure GR, it is khronometric, and the deviation is located precisely at ED's signature commitment — the arrow. That same unification (matter and geometry from one substrate) that makes ED radical is what makes its Lorentz violation safe. The result is a specific, falsifiable theory rather than a vague "GR-like."

### 1.3 How this fits the arc

- **Paper GR-I:** weak-field Schwarzschild metric + classical tests (factor of two, redshift, precession). *(inherited)*
- **Paper GR-II (this paper):** field-equation form (Lovelock), gravitational class (mode count → khronometric), GW speed, Lorentz safety.
- **Beyond:** the khronon parameters ($α₁, α₂$) and the MOND-sector relation — model-building, declared open (§8–§9).

### 1.4 Conventions and regime of validity

Metric signature $(−,+,+,+)$; $c = 1$ where convenient. The structural results — the field-equation form, the mode count, $c_T = c$, universal Lorentz violation — are **$F$-independent**: they follow from the gauge structure and the single substrate, not from the coefficients of the dynamical-bandwidth rule. They are stated in the **continuum (DCGT) limit** and rest on Paper GR-I's **static, weak-field** background for the explicit checks; the mode count is a linearized statement about perturbations on that background. **No strong-field and no cosmological claim is made** — the cosmological constant $Λ$ is inherited, not a cosmology result — and the $F$-dependent phenomenology ($α₁, α₂$, the scalar-mode speed) is explicitly deferred (§8).

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02 (reciprocal adjacency), P04 (four-band bandwidth, extensive/additive), P05 (adjacency transport), P11 (commitment irreversibility — the arrow), P13 (homogeneous tick — the foliation).

**Inherited from Paper GR-I:** the emergent metric $g_{ij} ∼ b⁻¹$, the lapse $N² ∼ b$, the weak-field Schwarzschild metric.

**Inherited mathematical input:**

- **Lovelock's theorem (1971):** in four dimensions, the only symmetric rank-2 tensor built solely from the metric and its derivatives, of second differential order and linear in the second derivatives, that is identically divergence-free, is $a\,G^{μν} + b\,g^{μν}$.

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper GR-I:** weak-field metric.
- **Paper_027:** Newtonian limit $∇²b ∼ ρ$; $G$.
- **Paper_033:** scalar-tensor / MOND arc (sharpened, §9).
- **Paper_073:** DCGT.
- **Paper_089:** V1 finite-width kernel (the single cone / bandwidth-limit speed).

**Empirical / value-layer inputs (inherited):** $κ = 8πG$ ($G$ value-inherited, Paper_027); $Λ$ (V1 backreaction). **The dynamical-bandwidth-rule coefficients are not supplied** (the $F$-residual; §8).

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| Emergent metric + weak-field Schwarzschild | I | Paper GR-I |
| Bandwidth current typed as transported-amount (dual) flux | **D** | §3.1 — forced by P05 transport semantics + P04 extensivity |
| $∇_μ J^μ = 0$ (current conservation, covariant) | D | §3.1 |
| $∇_μ T^{μν} = ρ a^ν$ (dust); $= 0 ⟺$ geodesic motion | D | §3.2 — leading dust model $T^{μν}=ρu^μu^ν$ |
| Front = null geodesic (geodesic identity, null sector) | D | §3.3 — discrete Fermat (max-Σ rule) |
| Lovelock's theorem | I | standard 4D uniqueness result |
| ED meets 4D / div-free source / second-order | D / I | §4 — from the rows above + Newtonian $∇²b∼ρ$ |
| Field equation forced to $G+Λg=κT$ **iff purely metric** | D conditional | §4 — Lovelock applied; the "purely metric" condition is §5 |
| Arrow in the law → preferred foliation | **D** | §5.1 — P11/P13 place the time-direction in the dynamics |
| Gauge = foliation-preserving diffeomorphisms | D | §5.2 |
| Mode count = 2 tensor + 1 scalar (khronometric) | **D-structural** | §5.3 — gauge-group argument; structural identification, not full linearized propagator (preamble 4) |
| Single causal cone (one substrate, one transport) | **D-structural** | §6 — P05 / Paper_089; $F$-independent |
| $c_T = c$ (GW170817 passed structurally) | D | §6 — both massless sectors saturate the one cone |
| Universal (not differential) Lorentz violation | **D-structural** | §7 — one cone for all species; $F$-independent |
| Evades $~10^{-20}$ differential matter-sector bounds | D | §7 — universal LV removable at leading order |
| $κ = 8πG$, $Λ$ | I | §4 — value-inherited |
| Khronon parameters $α₁, α₂$; sub-leading differential LV | **deferred ($F$-dependent)** | §8 — model-building; the falsification target |

All steps P, D, I, conditional, structural, or deferred. *The two pillars — the field-equation form (Lovelock) and the gravitational class (mode count) — are a standard theorem plus a gauge-group identification; the GW and Lorentz results are $F$-independent structural consequences of the single substrate; the open quantities are explicitly deferred.*

---

## 3. Matter Conservation is Geodesic Motion

Lovelock needs a divergence-free source. ED supplies one, and its conservation turns out to be the geodesic equation.

### 3.1 The bandwidth current is covariantly conserved — forced

The matter current is the bandwidth adjacency flux $J^μ$. Its *typing* is fixed, not chosen: by P05 transport semantics it is the *amount transported across an edge* — a flux through the dual face, intrinsically volume-weighted — and by P04 extensivity (bandwidth is an additive capacity) it is a density. A flux of a density has combinatorial (graph) divergence equal to the Levi-Civita covariant divergence $∇_μ J^μ = (1/\sqrt{g})\,∂_μ(\sqrt{g}\,J^μ)$. So the bandwidth continuity law *is* the covariant conservation

$$
∇_μ J^μ = 0,
$$

forced by P05 + P04, with no reference to Einstein. (The naive identification — graph divergence equals covariant divergence — is *false* by a factor $\sqrt{g}$; the correct dual-flux typing repairs it.)

### 3.2 The rank-2 source and the geodesic condition

The leading rank-2 source from the current is pressureless dust, $T^{μν} = ρ u^μ u^ν$ ($J^μ = ρ u^μ$). Its divergence splits:

$$
∇_μ(ρ u^μ u^ν) = (∇_μ J^μ)\,u^ν + ρ\,u^μ∇_μ u^ν = ρ\,a^ν,
$$

the first term vanishing by §3.1, leaving $ρ$ times the 4-acceleration $a^ν$. Therefore

$$
∇_μ T^{μν} = 0 \;\Longleftrightarrow\; a^ν = 0 \;\Longleftrightarrow\; \text{the bandwidth-flux worldlines are geodesics of } g∼b^{-1}.
$$

Matter conservation *is* the geodesic equation — the standard relation, reached forward from ED's own current. **This equivalence is exact for *dust* ($T^{μν} = ρu^μu^ν$); a source with pressure or anisotropic stress adds $∇·(stress)$ terms and requires the full dynamical rule's constitutive content, which is not supplied here.** Dust is the leading, lowest-derivative source the conserved current admits, and it suffices for the Lovelock argument (§4), which needs only *a* divergence-free rank-2 source, not the complete matter sector.

### 3.3 The geodesic identity holds for the null sector

The substrate front advances to the locally most-coherent / highest-bandwidth channel — a discrete **Fermat principle**, which is null-geodesic propagation. So ED's fronts *are* null geodesics of the optical metric, and $∇_μ T^{μν} = 0$ is satisfied for the null sector (the geodesic identity used in Paper GR-I §6 for light bending). The timelike (massive) sector requires the full lapse and is not separately proven here; the dust conservation §3.2 holds formally for any worldlines that are geodesics, which is established for null and assumed for timelike.

---

## 4. The Field Equation, via Lovelock

Rather than computing $G^{μν}$ from $b$ by hand, use the uniqueness theorem that makes Einstein inevitable. **Lovelock's theorem** (§2): in 4D, the only symmetric rank-2, second-order, identically-divergence-free tensor built solely from the metric is $a\,G^{μν} + b\,g^{μν}$. So any metric theory meeting those conditions has the field equation $G^{μν} + Λg^{μν} = κT^{μν}$. ED meets three of the four conditions from results already in hand:

| Lovelock condition | ED status |
|---|---|
| 4D spacetime | ✓ (assembled metric, Paper GR-I) |
| divergence-free symmetric rank-2 source | ✓ $∇·T = 0$ (§3); and $∇·G = 0$ is the contracted Bianchi identity, automatic for a genuine metric |
| second-order, linear in second derivatives | ✓ at Newtonian order ($∇²b ∼ ρ$); the dynamical-bandwidth rule introduces no higher metric derivatives |
| built **solely from the metric** (no extra field) | **the open condition — §5** |

On the **second-order** condition specifically (a reviewer's natural worry): ED's dynamical-bandwidth rule $ḃ = F(ρ, ∇ρ, b)$ depends on the source through at most $∇ρ$ and on the bandwidth field algebraically and through its Laplacian, so in the continuum (DCGT) limit it introduces **no higher-than-second derivative of the metric** — the Newtonian $∇²b ∼ ρ$ is representative of the full order, not a special low-order case. The Lovelock second-order hypothesis is therefore met at the level the rule is specified.

**If the fourth condition holds, the field equation is forced to be Einstein (with Λ).** The coefficient $κ = 8πG$ is fixed by matching the Newtonian limit ($G$ value-inherited, Paper_027); $Λ$ is the V1-backreaction term. This is the legitimate route to $G = κT$: not deriving the tensor, but showing ED satisfies the hypotheses that make it the only possibility — *modulo* the fourth condition, which §5 resolves, and not in ED's favor for *pure* GR.

*Why Lovelock is the right tool.* In four dimensions Lovelock's is the *unique* clean uniqueness theorem for a metric field equation: from general hypotheses (metric-built, second-order, divergence-free) it singles out $G^{μν} + Λg^{μν}$ out of the infinite space of candidate tensors. For an *emergent*-gravity program this is exactly what is wanted — it establishes the field-equation *form* from structural facts already in hand (a metric, a conserved source, second-order dynamics) instead of computing $G^{μν}$ from $b$ by brute force, and it concentrates the entire remaining question into a single hinge: the "purely metric" condition (§5).

---

## 5. The Mode Count: ED Gravity is Khronometric

The propagating degrees of freedom of a gravity theory are fixed by its gauge symmetry, and that is where ED departs from pure GR.

### 5.1 The arrow is in the law, not the boundary conditions

General Relativity's field equations are time-symmetric and fully diffeomorphism-invariant; a solution acquires an arrow only from its initial/thermodynamic conditions. **ED's arrow is a primitive of the dynamics** — P11 (irreversible commitment) and P13 (the homogeneous tick) make the time-direction part of the law. The substrate singles out a **preferred foliation** (the slicing by ticks, oriented by the commitment arrow) at the level of the rules.

### 5.2 The gauge group is foliation-preserving

A preferred foliation in the law breaks full 4D diffeomorphism invariance down to **foliation-preserving diffeomorphisms** (spatial diffeomorphisms on each slice plus time reparametrization). This is exactly the gauge group of **khronometric gravity** — the hypersurface-orthogonal Einstein-aether theory, equivalently the infrared limit of Hořava gravity — in which a scalar field (the "khronon," whose gradient defines the preferred time) supplements the metric.

Explicitly: a preferred foliation is equivalent to a hypersurface-orthogonal unit timelike vector field $u^\mu = \partial^\mu T/|\partial T|$, where the scalar $T$ (the khronon) labels the leaves; the gauge group reduces from the full $\mathrm{Diff}(M)$ to the foliation-preserving $\mathrm{Diff}(\Sigma)\ltimes\mathbb{R}$ — spatial diffeomorphisms on each leaf $\Sigma$ plus time reparametrization. This is the standard khronometric reduction, and it is the precise content of "a preferred time direction is a scalar whose level sets are the foliation": **in ED that scalar is the commitment arrow, so the khronon is not an added field but the arrow made geometric.** Unlike relativistic-MOND constructions such as TeVeS, ED adds **no vector field** — the preferred frame is not an independent dynamical aether but the substrate's own arrow, which is exactly why (§6–§7) it shares the matter cone instead of carrying separate kinetics.

### 5.3 The count: 2 tensor + 1 scalar

With foliation-preserving rather than full diffeomorphism gauge, the standard counting gives **2 transverse-traceless tensor modes + 1 scalar mode**. The bandwidth field $b_{ij}$ is a symmetric rank-2 tensor (P02 reciprocity), with the same component count as the metric, so the count is decided by gauge, not by components — and the reduced gauge leaves the extra scalar propagating. That scalar is the **khronon**: in ED it is the substrate's preferred foliation made dynamical, the arrow promoted to a field.

So **the fourth Lovelock condition fails** — ED's gravity is *not* built solely from the metric; it carries the khronon. Lovelock therefore does *not* give pure Einstein; it places ED in the **khronometric** class: Einstein's tensor sector plus the preferred-foliation scalar. ED gravity is khronometric, and the single departure from pure General Relativity is the inevitable shadow of the primitive arrow.

This extra scalar is a concrete, falsifiable prediction, stated here at the point it arises: khronometric gravity carries a **scalar gravitational-wave polarization** — the khronon "breathing" mode — that pure GR forbids, and ED inherits it (§10; falsifier §11.5).

### 5.4 Consistency with Paper GR-I

Khronometric gravity *shares* GR's static, spherically-symmetric weak-field metric, so Paper GR-I's results (factor-of-two bending, redshift, precession; the Schwarzschild relation) are unchanged — ED is observationally GR-like everywhere those tests reach. The departure shows up in the preferred-frame sector, treated below.

---

## 6. GW-Clean: the Single Causal Cone

In generic Einstein-aether / Hořava gravity the aether is an *independent* field with its own kinetic term, so its modes have their own light cone, and the post-GW170817 constraint $c_T = c$ (tensor gravitational-wave speed = light speed to $~10^{-15}$) is a fine-tuning. **ED is different by construction.** It has one maximal signal speed — the bandwidth-limit speed (V1 / Paper_089) — and one transport mechanism (P05 adjacency) that bounds every substrate process. Light is a matter front through P05; a tensor gravitational wave is a perturbation $δb_{ij}$ through P05; there is no separate aether kinetics. Both massless sectors saturate the **same** cone:

$$
c_T = c_{\text{light}} \quad \text{structurally.}
$$

The constraint that fine-tunes generic Hořava/Einstein-aether is, for ED, an *identity* — its khronon is the substrate's own foliation, sharing the matter cone. This is $F$-independent.

One caveat, to avoid overclaiming: the argument above is for the massless **tensor** sector. The **scalar** (khronon) mode may, in principle, propagate at a different speed; whether ED's single-transport structure forces it onto the same cone as well is an internal-consistency question — a potential strength (maximal predictivity) or an over-constraint against khronometric stability — deferred to §8. The $c_T = c$ result does not depend on how that resolves.

---

## 7. Lorentz-Safe: Universal, not Differential, Violation

The constraint that *kills* most Lorentz-violating gravity is not the preferred-frame PPN parameters; it is **matter-sector differential Lorentz violation** — different species having different cones (photon vs electron, vacuum Čerenkov, clock comparison) — bounded at $~10^{-20}$, into which gravitational-sector violation percolates through loops at order one unless protected. ED's defining feature turns this aside, $F$-independently:

> ED has only one cone, shared by all species (light, electrons, gravitational waves, the khronon all propagate through the same P05 substrate, §6). So ED's Lorentz violation is **universal** — one deformed cone for everything — and universal violation is removable by a single coordinate/field rescaling, hence **unobservable at leading order**. The $10^{-20}$ bounds constrain *differential* violation, which ED does not produce.

Put dispersion-theoretically, so the distinction is not hand-waved: **universal** Lorentz violation is a *single* modified dispersion relation shared by all species, removable by one global rescaling and hence unobservable at leading order; **differential** violation is *species-dependent* dispersion — different cones for photon, electron, … — which is precisely what the $~10⁻²⁰$ bounds constrain. ED forbids the differential case structurally, because every species *is* the same P05 substrate process and so inherits the same cone.

**ED's unification is its shield.** Generic Hořava keeps the aether as a *separate* field, so matter and gravity can drift to different cones (differential violation, executed). ED's matter and geometry descend from the *same* bandwidth substrate, so there is one cone (universal violation, safe). The very feature that makes ED radical — geometry and matter from one substrate — is what makes its Lorentz violation survivable. This is the strongest viability result of the paper, because it disarms the tightest constraint.

*Historical context.* Lorentz-violating gravity has a graveyard. Einstein-aether (Jacobson–Mattingly, 2001) and Hořava gravity (2009) introduced a preferred frame for UV or phenomenological gains; most variants were then constrained to death by two facts — **GW170817** (2017) fixed the tensor gravitational-wave speed to the light speed to $~10⁻¹⁵$, and matter-sector Lorentz tests bound *differential* violation to $~10⁻²⁰$. Generic theories survive only by fine-tuning both. ED meets the first as an identity (§6) and the second structurally (§7), for one reason: its preferred frame is the substrate's own arrow, not a separate aether with independent kinetics. ED is, in effect, the *maximally constrained* khronometric theory — which is why it survives where added-field versions do not.

---

## 8. The Residual and the Falsification Target

What survives as open is $F$-dependent and weaker, but real:

- **Preferred-frame PPN parameters $α₁, α₂$** (pure-gravity preferred-frame effects; bounds $~10^{-4} / 10^{-7}$). These are set by the khronon–gravity coupling in the *linearized dynamical-bandwidth rule*, whose coefficients are not pinned here. ED's preferred frame is naturally the cosmological (CMB) rest frame — which fixes *which* frame the bounds apply in — but does **not** by itself make the couplings small. **This is ED-gravity's genuine falsification target.**
- **Sub-leading differential Lorentz violation.** Universal violation is leading-order; species couple slightly differently beyond leading order, generating suppressed differential effects whose size is the $F$-dependent naturalness question.
- **A possible over-constraint.** If every substrate mode shares the one cone (§6), the scalar khronon mode may be forced to $c$ as well; khronometric stability places specific demands on the scalar speed, so this is an internal-consistency check — a potential strength (maximal predictivity) or problem (over-rigidity).

Computing $α₁, α₂$ requires choosing the dynamical-bandwidth coefficients — model-building, not derivation. This paper deliberately does not do so, and does **not** claim ED passes the preferred-frame tests. The boundary between what ED's structure forces (the field-equation form, the class, $c_T = c$, universal LV) and what requires the rule's coefficients ($α₁, α₂$) is the boundary between this paper and the phenomenology that follows it.

*(Forward note: the dynamical rule and these coefficients are built and analyzed in GR-III/GR-IV, and the front resolves favorably. $α₂ = 0$ **exactly** — a structural consequence of both gravitational cones being luminal ($c_T = c$, $c_s = c$), independent of any tuning and literature-verified, so the tighter bound is met for free — and $α₁ = −4λ_{local}$ is density-suppressed to $≲ 4×10^{-93}$ because commitment is sparse (forced by ED's quantum sector). The "genuine falsification target" named here is met; this paper's deferral was by scope, not because the front was unresolvable.)*

---

## 9. Position Relative to Paper GR-I and the Published Arc

- **Relative to Paper GR-I:** this paper supplies the *class* GR-I deferred. GR-I's weak-field metric is the regime where khronometric and pure GR coincide; GR-II locates the departure (the khronon) and shows it is safe.
- **Relative to Paper_033 (scalar-tensor / MOND):** the khronometric structure **revises** Paper_033's implicit Lorentz-covariance (the metric carries a preferred foliation) and **reframes** its flagged "deep-MOND superluminality" as the expected khronon mode (the superluminal/instantaneous scalar of khronometric theories, the origin of universal horizons) — a defect reframed as a feature. The relation of the khronon to Paper_033's MOND scalar ($a₀ = cH₀/2π$, BTFR) is the natural unification target — one khronometric gravity, GR at solar/BH scale and MOND in the deep galactic field via the khronon, with $a₀$ cosmological from the cosmic-frame anchoring — and is **open, declared, not claimed**.

---

## 10. The Wedge — Where ED Diverges from Pure GR

ED's empirical separation from pure General Relativity is the khronometric sector:

1. **Preferred-frame effects** ($α₁, α₂$) — absent in GR, present (size $F$-dependent) in ED; the falsification target (§8).
2. **A scalar gravitational-wave polarization** (the khronon "breathing" mode) — a concrete observable absent in GR's two tensor polarizations.
3. **Universal horizons** at $b → 0$ — a khronometric structure beyond GR's Killing horizons; and $b → 0$ is exactly ED's emergent horizon locus (the metric degenerates there), so ED's horizons are candidate khronometric universal horizons.

These are the genuine wedges, and they are sharp: ED predicts a scalar GW mode and preferred-frame structure that pure GR forbids, while remaining GW-speed-clean and Lorentz-safe (§6–§7).

---

## 11. Falsification Criteria

### 11.1 An extra propagating mode beyond 2 tensor + 1 scalar

**Falsifier sentence:** *A linearization of the dynamical-bandwidth rule yielding a propagating-mode count other than 2 tensor + 1 scalar — e.g. an additional vector mode — would falsify the §5 khronometric identification and force a different gravitational class.*

### 11.2 Tensor GW speed ≠ light speed

**Falsifier sentence:** *Empirical demonstration that the tensor gravitational-wave speed differs from the light speed ($c_T ≠ c$) beyond observational bounds would falsify the §6 single-cone result and the claim that the two sectors share one substrate transport.*

### 11.3 Differential matter-sector Lorentz violation at leading order

**Falsifier sentence:** *Empirical observation of differential Lorentz violation between matter species at leading order (e.g. species-dependent cones above the universal-violation residual) would falsify the §7 universal-violation result and ED's single-cone structure.*

### 11.4 Preferred-frame parameters above bound

**Falsifier sentence:** *Computation of $α₁, α₂$ from the linearized rule yielding values above the solar-system / pulsar bounds ($α₁ \gtrsim 10^{-4}$, $α₂ \gtrsim 10^{-7}$), with the cosmic-frame anchoring assumed, would falsify the viability of ED-khronometric gravity — the §8 falsification target.*

### 11.5 No scalar GW polarization

**Falsifier sentence:** *Definitive absence of any scalar gravitational-wave polarization, at sensitivity excluding the khronon mode, would falsify the §5 khronometric class (which requires a propagating scalar).*

---

## 12. Position Statement

Event-Density gravity is **Einstein-class but khronometric**. Given the postulated primitives + the emergent metric (Paper GR-I) + the covariantly-conserved source (§3), Lovelock's theorem forces the field-equation form to be $G^{μν} + Λg^{μν} = κT^{μν}$ **unless** the gravitational field carries an extra propagating mode (§4). It does: the arrow's residence in the law (P11/P13) reduces the gauge group to foliation-preserving diffeomorphisms, and the mode count is 2 tensor + 1 scalar (§5) — Einstein's tensor sector plus a preferred-foliation khronon. ED is therefore khronometric, departing from pure GR only at the primitive arrow. The same unification that produces the khronon protects it: one substrate, one transport, one cone gives $c_T = c$ structurally (§6) and **universal rather than differential** Lorentz violation (§7), so ED evades the $~10^{-20}$ matter-sector bounds that execute generic Hořava / Einstein-aether theories.

**What this paper claims.** ED's gravitational class is khronometric (Einstein tensor sector + khronon), the field-equation form is Lovelock-forced given the metric and conserved source, the tensor GW speed equals the light speed structurally, and the Lorentz violation is universal and hence safe from the tightest bounds — all from ED's structure, independent of the dynamical-rule coefficients.

**What this paper does not claim.** ED is not pure General Relativity; the mode count is a structural identification, not a completed linearized-propagator computation; the khronon parameters ($α₁, α₂$) are not computed and ED is not claimed to pass the preferred-frame tests; $κ$ and $Λ$ are inherited; and the khronon↔MOND-scalar relation is open. The residual is model-building — pin the rule, compute the parameters, confront the preferred-frame bounds — not derivation.

**Series context.** Paper GR-II of the post-pivot curvature-emergence line, companion to Paper GR-I. The remaining work (khronon parameters; the MOND-sector unification) is phenomenology and is declared open.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** Paper_087.
- **Paper GR-I:** weak-field Einstein metric (inherited).
- **Paper_027:** Newtonian limit; $G$.
- **Paper_033:** scalar-tensor / MOND arc (sharpened, §9).
- **Paper_073:** DCGT.
- **Paper_089:** V1 finite-width kernel (the single cone).

### Glossary

- **Khronometric gravity.** The hypersurface-orthogonal Einstein-aether theory (Hořava infrared limit): a metric plus a preferred-foliation scalar (khronon). ED's gravitational class.
- **Khronon.** The propagating scalar whose gradient defines the preferred time; in ED, the substrate foliation (the arrow) made dynamical.
- **Lovelock's theorem.** The 4D uniqueness result fixing the divergence-free, second-order, metric-built field-equation tensor to $a\,G^{μν} + b\,g^{μν}$.
- **Single causal cone.** All ED propagation occurs through one transport (P05) at one maximal speed; hence $c_T = c$ and universal Lorentz violation.
- **Universal vs differential Lorentz violation.** Universal: one cone for all species (removable, safe). Differential: species-dependent cones (constrained to $~10^{-20}$). ED produces universal.
- **Preferred-frame PPN parameters $α₁, α₂$.** Pure-gravity preferred-frame effects; $F$-dependent; the falsification target.
- **Universal horizon.** In khronometric / Hořava gravity, a surface that traps even the instantaneously-propagating khronon (beyond GR's Killing horizon, which traps only light). In ED it is a candidate identity for the $b → 0$ locus where the emergent metric degenerates (§10).
- **Scalar (breathing) GW polarization.** The propagating khronon mode — a gravitational-wave polarization absent in pure GR's two tensor modes; a concrete ED prediction (§5.3, §10).

### Reader map and open work

**Where to look next.**
- *The weak-field metric and the three classical tests:* GR-I.
- *The MOND sector ($a₀$, BTFR):* Paper_033 + §9.
- *The khronon parameters and scalar-mode speed (phenomenology):* future work (§8).
- *Horizon structure ($b → 0$, universal horizons):* ED-10 / V5; §10.

**Open work** (declared, §8–§9): compute $α₁, α₂$ and the sub-leading differential Lorentz violation from the linearized rule; compute the scalar-mode speed and settle the §6 over-constraint; unify the khronon with the MOND scalar; extend to the strong-field regime and to cosmology.

---

**End of Paper GR-II.**

*Post-pivot curvature-emergence line. ED gravity is khronometric — Einstein's tensor sector plus a preferred-foliation khronon (the arrow made dynamical) — GW-clean ($c_T = c$, single cone) and Lorentz-safe (universal, not differential, violation; the unification is the shield). Departs from pure GR only at the arrow; the preferred-frame parameters are the open falsification target. Weak-field metric: GR-I.*
