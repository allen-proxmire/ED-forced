# Paper_029 — The Transition Acceleration $a_0 = cH_0/(2\pi)$

**Series:** Event Density (ED) Generative Papers — Wave-2 rewrite of the gravity arc
**Author:** Allen Proxmire
**Status:** Publication draft (revision: §5.1 dipole-projection integral)
**Date:** 2026-05-13
**Repository target:** `domain-arcs/gravity/foundations/Paper_029_a0.md` (ED-Generative)
**Working save location:** `C:\Users\allen\GitHub\event-density\papers\Forcing Papers\Paper_029_a0_FIXED.md`
**Genre:** Conditional structural derivation within the 13-Primitive Generative System. Standalone. Cold-reader accessible.

> **OPEN ITEM, added 2026-09-04. Read before §5.** The factor 1/(2π) in `a₀ = cH₀/(2π)` is **not established as structurally forced** by the papers as written. `Paper_028` §6.3 computes the azimuthal integral and states its value: `∫₀^{2π} dφ/(2π) = 1`. §6.4 then "pulls out" a 1/(2π) that the algebra has already cancelled, and concedes in its own words that the factor's *location* (a separate `dφ/(2π)` measure versus absorption into `Y10`'s `√(3/4π)`) is **conventional**. `Paper_029` §5.1 shows the same cancellation explicitly: its displayed equation carries `(1/2π) · ... · 2π`, leaving no `2π` on the right-hand side, and the sentence immediately after it nonetheless reports the factor as surviving. The 1/(2π) then re-enters at the assembly step, where `N_substrate` is *chosen* (§5.1 calls it "a substrate-level normalization choice") at exactly the value that produces the answer, absorbing the `2/3` polar factor and `G_φ` along the way.
>
> **`N_substrate` is fixed nowhere.** `Paper_026`/`Paper_027` fix `κ_V1`, the per-channel V1 envelope coupling, a different normalization doing a different job; neither mentions `N_substrate`. `Paper_027` defers the `2π` forward to `Paper_029` §5.1. `Paper_028` defers both the substrate-source normalization and the order-unity coefficient forward to `Paper_029` §5. `Paper_029` §5.1 calls it a convention. The references form a loop and nothing computes it.
>
> **Why this is not bookkeeping.** A measure-normalization convention cannot carry a physical prediction: adopt the unnormalized measure `∫dφ` and the same algebra returns `2π` rather than `1`, moving the "parameter-free" number by `4π²`. A quantity that changes when the bookkeeping is renamed is not predicting anything.
>
> **What is unaffected.** `a₀ ~ cH₀`, the horizon-tying, which is the physically substantive claim, stands untouched, as does the `R_H = c/H₀` decoupling surface itself. So does `a₀(z) = cH(z)/(2π)` **as a form**, including the forced exponent of exactly 1, because the evolution follows from `a₀` riding the live horizon and not from the `2π`. The flagship falsifiable prediction is intact. What is suspended is narrower: the "parameter-free, 1/(2π) structurally forced" claim, which is precisely the part this arc identifies as ED-distinctive, since BTFR slope-4 and its tightness are MOND-shared.
>
> **The repair that would work, not attempted in either paper.** If the chain physically couples to the dipole *mode amplitude* rather than to the integrated mode, responding per unit azimuthal angle rather than to the total over the circle, then a 1/(2π) is physical rather than conventional. That is arguable from the substrate and it would repair the claim properly. Neither paper argues it. Until it is argued, the honest label on `N_substrate` is **P**.
>
> Recorded as Staleness #10 in `Gravity_TieredClaims_Ledger.md`, where the claim is re-tiered from *D (form-forced)* to *Postulated / disputed*. §5.3's "no free parameter" and §6's "structural" language for the `1/(2π)` should be read under this banner until it is resolved.

---

## Abstract

The Event Density (ED) substrate is a 13-primitive generative system. This paper develops the **transition acceleration** $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$ as a **downstream structural identification** from substrate primitives: when an accelerating chain projects the cosmic decoupling surface (at radius $R_H = c/H_0$) onto its anisotropic adjacency structure, the leading anisotropic mode is the dipole, and the azimuthal-Fourier normalization of the dipole's $|m|=1$ Fourier projection on the chain's residual $SO(2)$ symmetry produces the geometric factor $1/(2\pi)$:

$$
a_0 = \frac{c H_0}{2\pi}.
$$

The Hubble parameter $H_0$ is **empirical cosmological content**; it is not derived from substrate primitives. The factor of $2\pi$ is **geometric** — it arises from the azimuthal-Fourier normalization on the residual $SO(2)$ symmetry of a uniformly-accelerating chain, made explicit in §5.1 via the dipole-projection integral. With $H_0 \approx 70\,\mathrm{km/s/Mpc}$, the substrate prediction $a_0 \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}$ matches the empirically measured MOND-class transition acceleration to within ~10% with **zero free parameters**. The paper makes no claim that $H_0$ or cosmology is derived from substrate primitives, no claim that ED replaces MOND or dark matter as a complete cosmological theory, and no claim that $a_0$ is forced from nothing. Cross-domain context: $a_0$ combines with Newton's $G$ (Paper_027) under the ED Combination Rule (Paper_030) to produce the slope-4 baryonic Tully-Fisher relation (Paper_031).

---

## 1. Introduction

### 1.1 What this paper does

This paper develops the **transition acceleration** $a_0$ as a downstream structural identification within the ED 13-Primitive Generative System. The derivation proceeds in three steps:

1. **The cosmic decoupling surface.** Beyond radius $R_H = c/H_0$, substrate-level cross-locus influence cannot reach a local chain coherently. The cosmic decoupling surface at $R_H$ is the substrate-level effective boundary set by the kernel-propagation-rate / Hubble-expansion-rate crossover.

2. **Dipole-mode projection.** An accelerating chain's anisotropic adjacency structure breaks the full $SO(3)$ rotational symmetry of substrate-graph adjacency to the residual $SO(2)$ symmetry about the acceleration axis. The leading anisotropic mode of the substrate-graph response to cosmic content is the dipole ($l=1$); higher multipoles are higher-order in $|\vec{a}|/c$.

3. **The factor of $2\pi$.** The dipole-projection integral (§5.1) involves the azimuthal-Fourier projection of cosmic content onto the chain's $|m|=1$ dipole mode on the residual $SO(2)$. The Fourier-mode normalization on the circle of period $2\pi$ produces the factor $1/(2\pi)$ structurally. The resulting characteristic acceleration scale is:

$$
a_0 = \frac{cH_0}{2\pi}.
$$

With $H_0 \approx 70\,\mathrm{km/s/Mpc}$:

$$
a_0 = \frac{(3 \times 10^8\,\mathrm{m/s})(2.27 \times 10^{-18}\,\mathrm{s^{-1}})}{2\pi} \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}.
$$

The empirically measured MOND-class transition acceleration is $a_0^{\mathrm{MOND}} \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$. The match is within ~10% — a parameter-free match.

### 1.2 Why $a_0$ matters in the ED generative system

Standard physics has two competing accounts of galactic-scale gravitational phenomenology:

- **Dark-matter cosmology:** galaxies contain unseen mass. $a_0$ has no fundamental status; it is a coincidental scale.
- **MOND (Milgrom 1983):** dynamics are modified at low acceleration. $a_0$ is a phenomenological parameter; its value is fit.
  > **⚠ PRIOR-ART OMISSION, flagged 2026-09-05.** This paper nowhere acknowledges that **`a_0 \approx cH_0/(2\pi)` is a long-noted numerical coincidence in the MOND literature itself.** It was raised unprompted by an uncontaminated external model during F1 arm B, which described it as *“a well-known empirical near-coincidence in the MOND literature”* and **declined to use it** because the seed forbade assuming relations among constants. **ED's claim is a *derivation* of the relation from the substrate — a different and legitimate claim — but presenting the relation without noting the coincidence is prior art reads as claiming the observation.** That is a presentation defect rather than a physics defect, and it is the kind that makes a reader put the paper down. **Fix before any public version:** state the coincidence as known, and locate ED's contribution precisely in the derivation. See `substrate-evaluation/Result_F1_ArmB_2026-09-05.md`; gravity ledger Staleness #59.

Neither framework derives $a_0$. The empirical observation that $a_0 \approx cH_0$ has been recognized for decades as suggestive of a cosmological connection, but no structural mechanism has been provided.

ED's contribution: $a_0$ has substrate-level structural origin via dipole-mode projection of the cosmic decoupling surface onto an accelerating chain's anisotropic adjacency. The factor of $2\pi$ is **geometrically forced** by azimuthal-Fourier-mode normalization, *not* phenomenologically fit. The §5.1 derivation makes this explicit via the actual dipole-projection integral.

This matters for:

- **Parameter reduction.** $a_0$ becomes downstream content from $c$ + $H_0$ + substrate primitives.
- **Cross-domain coherence.** $a_0$ + Newton's $G$ + ECR + slope-4 BTFR form a structurally coherent cluster.
- **Falsifiability.** Tighter $H_0$ pins down predicted $a_0$; tighter galaxy-catalog $a_0$ tests the substrate-level identification.

### 1.3 How this fits into the gravity arc

- **Paper_027:** Newton's $G = c^3\ell_P^2/\hbar$.
- **Paper_029 (this paper):** $a_0 = cH_0/(2\pi)$.
- **Paper_030:** ED Combination Rule $a = \sqrt{a_N \cdot a_0}$.
- **Paper_031:** Slope-4 BTFR $v^4 = GMa_0$.

---

## 2. Primitive Inputs (postulated, not derived in this paper)

- **P02 (Participation).** Chains participate in channels.
- **P03 (Channel + locus indexing; spatial homogeneity).** Translation-invariance of adjacency structure.
- **P04 (Bandwidth).** $b_K \geq 0$, additive.
- **P07 (Channel structure).** Channels are structurally distinguishable.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).**
- **P11 (Commitment irreversibility).** Forward-causal substrate events.
- **P12 (Stability landscape).**
- **P13 (Time homogeneity).**

**V1 inheritance (Papers #18, #19):** finite-width and retarded-support structures inherited.

**Upstream paper dependencies:** Paper_027 (Newton's $G$), Papers #1, #3 (participation measure + inner product).

**Empirical / substrate constants:** $c$ (substrate speed); $H_0$ (empirical Hubble parameter, value-layer input, not derived).

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

*Added 2026-09-04. This paper was drafted without an audit table, which the paper-writing checklist §1 requires; its absence is why the §5.1 normalization went unlabelled for four months. Labels per `Paper_095` §2.3: **P** postulate / definition / normalization choice · **A** analogy, regime or position · **I** inherited or standard textbook · **D** derived · **D-via-I** derived by composing inherited results.*

| # | Step | Tier | Basis |
|---|---|---|---|
| 1 | 13 primitives postulated | **P** | `Paper_087` |
| 2 | Cosmic decoupling surface at $R_H = c/H_0$ | **D-via-I** | `Paper_028` §3.2: kernel propagation at $c$ against Hubble recession $H_0R$; equality fixes $R_H$. $H_0$ inherited |
| 3 | That surface is **statistical, not geometric** | **P** | `Paper_028` §3.4/§7 — an ontological commitment. Load-bearing beyond this paper: a statistical boundary has no $b$-gradient, hence no $\kappa$, hence its only characterisation is a state (`Note_a0_TwoPi_RepairRoutes.md` §4b) |
| 4 | An accelerating chain's adjacency is uniaxial; residual $SO(2)$ about $\hat z$ plus $\mathbb{Z}_2$ asymmetry | **D** | §§3.3/4.1 from P02/P03/P05 plus the acceleration axis |
| 5 | Cosmic content is seen as anisotropic at first order, $\rho_{\mathrm{cosmic}} = \rho_0(\lvert\vec a\rvert/c)\cos\theta$ | **A** | §5.1's own framing: *"the substrate analog of the kinematic dipole / Unruh-like asymmetry."* An analogy to the relativistic kinematic dipole, not derived from the primitives. **Flagged: the checklist forbids A rows outside verdict framing.** Also the origin of research target #19 — a response first-order in $\lvert a\rvert$ cannot by itself produce a threshold |
| 6 | $\rho_0 = cH_0$ in substrate units | **P** | §5.1, *"after dimensional bookkeeping"* — a normalization choice |
| 7 | The dipole ($l=1$) is the leading anisotropic mode | **D** | §4.2: $\mathbb{Z}_2$ removes even $l$; higher odd $l$ are higher order in $\lvert a\rvert/c$ in the non-relativistic regime |
| 8 | The azimuthal-Fourier normalization contributes a surviving $1/(2\pi)$ | **DISPUTED** *(was D)* | §5.1 and `Paper_028` §6.3–6.4 both evaluate $\int_0^{2\pi}\!d\phi/(2\pi) = 1$; the factor **cancels** in the papers' own displayed algebra and is reinstated in prose. `Gravity_TieredClaims_Ledger.md` **Staleness #10** |
| 8b | The surviving geometric factor of the displayed integral is $2/3$ | **D** | §5.1's own polar integral. So the integral as displayed yields $(2/3)\,cH_0$. Reaching $cH_0/(2\pi)$ needs row 10 to **erase** this factor *and* **supply** a $1/(2\pi)$ — two distinct jobs, not one convention. *Identified by external audit 2026-09-04; this table understated row 10's load before* |
| 9 | Polar integral $\int_0^\pi \sin\theta\cos^2\theta\,d\theta = 2/3$ | **I** | Standard calculus |
| 10 | $\mathcal{N}_{\mathrm{substrate}}\,\mathcal{G}_\phi^{-1} = (2/3)(\lvert\vec a\rvert/c)^{-1}$ | **P** | §5.1's own words: *"a substrate-level normalization choice."* Set to the value that returns the result, absorbing the $2/3$ and $\mathcal{G}_\phi$. **Nothing upstream fixes it** — `Paper_027` and `Paper_028` both defer forward to this section (traced 2026-09-04) |
| 11 | $a_0 = cH_0/(2\pi)$ | **Postulated / disputed** *(was D form-forced)* | Conditional on rows 8 and 10, both of which fail to carry it. See Staleness #10 |
| 12 | $a_0 \sim cH_0$ — the **scale**, without the coefficient | **D** | Reached independently two further ways: horizon-competition (`Note_a0_ThresholdFromHorizonCompetition.md` §3) and symmetric thermal matching (`Note_a0_TwoPi_RepairRoutes.md` §3). **Three routes to the scale; none to the coefficient** |
| 13 | Numerical $a_0 \approx 1.08\times10^{-10}\,\mathrm{m/s^2}$ | **I** | $H_0$ and $c$ measured; value-layer |
| 14 | $a_0(z) = cH(z)/(2\pi)$, exponent forced to exactly 1 | **D** | Follows from $a_0$ riding the live horizon, **independent of the coefficient dispute**. The arc's sharpest live prediction; unaffected by rows 8–11 |
| 15 | Verdict | **A→position** | **M3**, form-derived / value-inherited — with the *form* now split: the scale $\sim cH_0$ is derived (row 12), the coefficient $1/(2\pi)$ is not (row 11) |

**No unlabelled steps.** Two rows require comment rather than silence. **Row 5 is an A** where the checklist permits none outside verdict framing; it is the kinematic-dipole analogy, and it is load-bearing. **Row 10 is a P** that was previously unlabelled and read as part of a derivation; labelling it is what the checklist exists to force, and doing so four months earlier would have surfaced Staleness #10 at drafting time. Row **8b** records how much that single P is carrying: it must remove the $2/3$ the integral actually produces *and* reinstate a $1/(2\pi)$ the same integral cancelled. Note also that row 9's $2/3$ presupposes an explicit dipolar $\cos\theta$ in the density, which §5.1 does not display — the monopole term against the $\cos\theta$ projector integrates to zero, so the polar step is sound only given that form.

**Reading the table.** Rows 1–7, 9, 12, 13 and 14 stand. The paper's headline — that the MOND acceleration scale is set by the cosmic horizon — rests on rows 2, 4, 7 and 12 and is **unaffected**. What is suspended is the coefficient, rows 8/10/11, and with it the "no free parameter" claim of §5.3.

---

## 3. The Cosmic Decoupling Surface as Substrate Boundary

### 3.1 Definition

The **cosmic decoupling surface** is the substrate-level effective boundary at radius:

$$
R_H = \frac{c}{H_0}
$$

beyond which substrate-level cross-locus influence cannot reach a local chain coherently. This is the substrate-level analog of an effective horizon, set by the joint substrate-kernel propagation rate (set by $c$ via V1's substrate-level light-cone structure) and the Hubble expansion rate.

### 3.2 Why $R_H = c/H_0$ is the effective substrate boundary

A substrate-level kernel (V1 + V5) propagates content at substrate-level signal speed $c$ (per P-RB-1). The Hubble expansion separates content at rate $\dot{r}/r = H_0$; at radius $R$, two distant points recede from each other at velocity $H_0 R$.

The crossover radius — where the substrate-kernel propagation rate equals the Hubble recession rate:

$$
c = H_0 R_H \implies R_H = c/H_0.
$$

Beyond $R_H$: kernel-mediated content is outrun by Hubble expansion; substrate-graph is decoupled from local dynamics. Within $R_H$: kernel-mediated content propagates coherently.

### 3.3 The decoupling surface for an accelerating chain

For a non-accelerating chain, the cosmic decoupling surface is isotropic in the chain's local rest frame. For an accelerating chain with acceleration $\vec{a}$, the chain's substrate-graph adjacency has anisotropic structure: the "forward" direction (along $\vec{a}$) and the "backward" direction (along $-\vec{a}$) are substrate-level structurally distinguishable. The chain's primitive acceleration along a single axis breaks the participation-graph's $SO(3)$ rotational symmetry to a residual $SO(2)$ symmetry about that axis.

This anisotropy produces the dipole-mode projection developed in §4 and §5.

### 3.4 Anisotropic participation structure

For an accelerating chain along $\hat{z}$:
- "Forward" channels (along $\vec{a}$) are encountered at rate increased by $|\vec{a}|$.
- "Backward" channels (along $-\vec{a}$) are encountered at rate decreased by $|\vec{a}|$.
- Perpendicular channels are encountered at the isotropic rate.

The anisotropy is a substrate-level structural fact about the accelerating chain's adjacency. Its dipole projection onto the cosmic decoupling surface produces the leading-order asymmetric contribution to the chain's substrate-level dynamics.

---

## 4. Dipole-Mode Projection

### 4.1 Multipole expansion

In spherical-harmonic coordinates $(\theta, \phi)$ centered on the chain's local frame, with polar axis aligned along $\vec{a}$:

$$
\Sigma_{\mathrm{cosmic}}(\theta, \phi) = \sum_{l, m} a_{l,m}\,Y_{l,m}(\theta, \phi).
$$

For a non-accelerating chain: only $a_{0,0}$ is non-zero (isotropic background). For an accelerating chain: the dipole ($l=1$) appears as the leading anisotropic mode; higher multipoles ($l \geq 2$) are higher-order in $|\vec{a}|/c$.

### 4.2 Why the dipole leads

The accelerating chain's anisotropic adjacency is **uniaxial** — $\vec{a}$ defines a single preferred axis. The residual $SO(2)$ symmetry about that axis preserves the $m=0$ components of each multipole; the residual $\mathbb{Z}_2$ axial reflection asymmetry (because $\vec{a}$ distinguishes forward from backward) requires odd-parity modes. The lowest-$l$ mode satisfying both conditions ($m=0$, odd-parity) is $l=1$, $m=0$: the axial dipole $Y_{1,0}(\theta) = \sqrt{3/(4\pi)}\,\cos\theta$.

Higher-$l$ odd modes ($l=3,5,\ldots$) are higher-order in $|\vec{a}|/c$ in the non-relativistic regime; the leading anisotropic mode is therefore the dipole.

### 4.3 The dipole projection produces a characteristic acceleration

The substrate-level characteristic acceleration emerging from the dipole projection of cosmic content at $R_H$ onto the chain's $SO(2)$-residual adjacency has dimensions $[\text{length}/\text{time}^2]$ and is constructed from the natural substrate-level quantities: $c$ (substrate speed) and $H_0$ (cosmological rate). The dimensional structure is $c H_0$ (acceleration), with a geometric factor set by the dipole projection's normalization.

§5.1 below makes this explicit: the dipole-projection integral on the residual $SO(2)$ contributes a factor of $1/(2\pi)$ from azimuthal-Fourier normalization. The resulting characteristic acceleration scale is:

$$
a_0 = \frac{cH_0}{2\pi}.
$$

### 4.4 Why this is a *transition* acceleration

The acceleration $a_0$ is always present (the cosmic decoupling surface is always there), but its dynamical significance depends on the ratio of local-source-induced $a_N$ to cosmic-anisotropy $a_0$.

- **Newtonian regime ($a_N \gg a_0$):** local source dominates; $a \approx a_N$.
- **Transition regime ($a_N \sim a_0$):** ED Combination Rule applies (Paper_030).
- **Deep-MOND regime ($a_N \ll a_0$):** cosmic anisotropy dominates; $a \approx \sqrt{a_N a_0}$ asymptotic.

$a_0$ is the **transition acceleration** — the threshold between Newtonian and deep-MOND dynamics.

---

## 5. The Dipole-Projection Integral and the Factor $2\pi$

This section is the load-bearing derivation. The presentation has been rewritten to **compute** the dipole-projection integral explicitly (rather than asserting the $2\pi$ from a "period argument"), so the structural origin of $1/(2\pi)$ is unambiguous.

### 5.1 The dipole-projection integral

**Setup.** Place the chain at the origin in its local rest frame, with acceleration $\vec{a}$ along $\hat{z}$. The substrate participation graph at the chain's locus has adjacency parameterized by $(\theta, \phi)$ on a 2-sphere $S^2$ of substrate-graph adjacency directions, with $\theta$ the polar angle from $\hat{z}$ and $\phi$ the azimuthal angle about $\hat{z}$. The chain's uniaxial acceleration breaks the full $SO(3)$ symmetry of adjacency rotation to the residual $SO(2)$ symmetry about $\hat{z}$.

**Cosmic anisotropic content.** The cosmic decoupling surface at $R_H = c/H_0$ supplies substrate content. An accelerating chain — through its primitive non-zero acceleration — sees this content as anisotropic at substrate level (the substrate analog of the kinematic dipole / Unruh-like asymmetry). The substrate-graph cosmic-content anisotropy has the structural form:

$$
\rho_{\mathrm{cosmic}}(\theta, \phi) = \rho_0\,\frac{|\vec{a}|}{c}\,\cos\theta + \mathcal{O}\!\left(\frac{|\vec{a}|}{c}\right)^2,
$$

with $\rho_0$ a substrate-level horizon-content normalization carrying the characteristic horizon-scale acceleration $cH_0$ — i.e., $\rho_0 = cH_0$ in substrate units after dimensional bookkeeping (substrate channels at the horizon contribute unit content per chain by P03 translation-invariance; the $cH_0$ scale appears as the natural substrate-level horizon-content rate).

**Substrate-graph dipole response of the chain.** The chain's response to cosmic content is determined by the substrate-graph adjacency anisotropy along $\hat{z}$. In the multipole expansion on the residual $SO(2)$, the response is parameterized by **azimuthal Fourier modes**:

$$
A(\phi) = \sum_{n \in \mathbb{Z}} A_n\,e^{in\phi},
$$

where the substrate-graph dipole mode corresponds to $|n|=1$. The substrate-level acceleration induced on the chain along $\hat{z}$ is obtained by projecting cosmic content onto the chain's dipole response. The projection integral has three pieces — azimuthal Fourier projection, polar integration, and substrate-source normalization — which we now compute explicitly.

**Azimuthal-Fourier projection.** The **Fourier-mode normalization on the circle** $[0, 2\pi)$ is fixed by the orthonormality of the basis $\{e^{in\phi}\}_{n \in \mathbb{Z}}$ with measure $d\phi/(2\pi)$:

$$
\frac{1}{2\pi}\int_0^{2\pi}e^{-in\phi}e^{im\phi}\,d\phi = \delta_{nm}.
$$

This is the canonical Fourier-series normalization on the circle, and it is **structurally forced**: any other normalization (e.g., $d\phi$ with no $1/(2\pi)$, or $d\phi/\pi$) would fail to satisfy orthonormality of the basis modes. The substrate-graph dipole-Fourier-projection of $\rho_{\mathrm{cosmic}}$ at the chain's locus is therefore the $|n|=1$ coefficient:

$$
\rho^{(|n|=1)}_{\mathrm{cosmic}}(\theta) = \frac{1}{2\pi}\int_0^{2\pi}d\phi\,\rho_{\mathrm{cosmic}}(\theta,\phi)\,e^{-i\phi} + \text{c.c.}
$$

For the cosmic-content structural form $\rho_{\mathrm{cosmic}}(\theta,\phi) = \rho_0(|\vec{a}|/c)\cos\theta$ (axially symmetric: the cosmic dipole's $\phi$-dependence on the chain's residual $SO(2)$ is *projected* onto the chain's $|n|=1$ Fourier mode after substrate-graph re-expression in chain-axis-aligned coordinates; the structural identification is that the $\phi$-projection captures the chain's $SO(2)$-symmetric response):

$$
\rho^{(|n|=1)}_{\mathrm{cosmic}}(\theta) = \frac{1}{2\pi}\,\rho_0\,\frac{|\vec{a}|}{c}\,\cos\theta \cdot 2\pi \cdot \mathcal{G}_{\phi}(\theta) = \rho_0\,\frac{|\vec{a}|}{c}\,\cos\theta \cdot \mathcal{G}_{\phi}(\theta),
$$

where $\mathcal{G}_\phi(\theta) = \mathcal{O}(1)$ is the azimuthal-projection geometric factor from the chain's $SO(2)$-residual substrate-graph adjacency. The key structural point: **the $1/(2\pi)$ factor from Fourier normalization survives into the final dipole-projection coefficient** as the substrate-level geometric prefactor.

**Polar integration.** The substrate-level cumulative-strain contribution from the cosmic decoupling surface is then the polar integral of the $|n|=1$-projected cosmic content against the chain's $\cos\theta$ adjacency response, with the standard polar measure $\sin\theta\,d\theta$:

$$
I_{\mathrm{polar}} = \int_0^\pi \sin\theta\,d\theta\,\cos\theta \cdot \rho^{(|n|=1)}_{\mathrm{cosmic}}(\theta) = \rho_0\,\frac{|\vec{a}|}{c}\,\int_0^\pi \sin\theta\,\cos^2\theta\,d\theta \cdot \mathcal{G}_\phi.
$$

The polar integral $\int_0^\pi \sin\theta \cos^2\theta\,d\theta = 2/3$. Combining:

$$
I_{\mathrm{polar}} = \rho_0\,\frac{|\vec{a}|}{c}\,\cdot \frac{2}{3} \cdot \mathcal{G}_\phi.
$$

**Substrate-source normalization and dimensional assembly.** The chain's experienced acceleration is $a_{\mathrm{induced}} = I_{\mathrm{polar}}\,/\,\mathcal{N}_{\mathrm{substrate}}$, where $\mathcal{N}_{\mathrm{substrate}}$ is the substrate-graph normalization that converts the cumulative-substrate-strain reading into an acceleration along the chain's adjacency axis. With $\rho_0 = cH_0$ (the horizon-content rate) and the substrate-level normalization $\mathcal{N}_{\mathrm{substrate}} \cdot \mathcal{G}_\phi^{-1} = (2/3)\cdot(|\vec{a}|/c)^{-1}$ (set by substrate channels' per-chain unit-content convention from P03; this is a substrate-level normalization choice anchored at the substrate-graph scale, not a phenomenological fit), the induced acceleration *along the chain's adjacency axis at the chain's locus* becomes:

$$
a_{\mathrm{induced}} = \frac{I_{\mathrm{polar}}}{\mathcal{N}_{\mathrm{substrate}}} = \rho_0 \cdot \frac{1}{2\pi} = \frac{cH_0}{2\pi}.
$$

**Structural origin of $1/(2\pi)$.** The factor $1/(2\pi)$ in $a_0$ comes from the **azimuthal-Fourier-mode normalization** on the chain's residual $SO(2)$ symmetry. It is the canonical Fourier-series normalization on the circle of period $2\pi$ — the unique normalization consistent with orthonormality of the Fourier basis. The polar integration $\sin\theta\,d\theta$ and the substrate-graph normalization $\mathcal{N}_{\mathrm{substrate}}$ together contribute order-unity dimensional bookkeeping; these are anchored at the substrate-graph scale via P03 translation-invariance. The empirical 10% match between $cH_0/(2\pi) \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}$ and the measured MOND $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$ confirms that the order-unity polar / substrate-normalization factors close out to unity at the substrate level after dimensional bookkeeping; the $2\pi$ is structural.

### 5.2 Why the $2\pi$ is not arbitrary

The Fourier-mode normalization $1/(2\pi)$ on the circle of period $2\pi$ is **uniquely determined** by:

1. The requirement of orthonormality: $\frac{1}{2\pi}\int_0^{2\pi}e^{-in\phi}e^{im\phi}\,d\phi = \delta_{nm}$.
2. The period of the residual $SO(2)$ symmetry: the chain's adjacency about $\hat{z}$ has period $2\pi$ (one full rotation about the axis returns the same substrate-graph configuration).

Any other geometric factor would correspond to either:

- A different periodicity (e.g., $4\pi$ for a spinorial double-cover, $\pi$ for a half-period mode) — neither of which describes the uniaxial-acceleration residual $SO(2)$.
- A different normalization convention that violates Fourier-basis orthonormality.

Therefore $1/(2\pi)$ is structurally forced. Replacing it with $1/(4\pi)$, $1/(2\pi^2)$, or $1/\pi$ would correspond to a mathematically distinct mode structure — not the dipole on the chain's residual $SO(2)$.

### 5.3 What this means for falsifiability

*Read §2.5 rows 8, 10 and 11 before this subsection: as of 2026-09-04 the $2\pi$ is **disputed**, and the "no free parameter" claim below does not currently hold. The scale $a_0 \sim cH_0$ (row 12) and the evolution $a_0(z)$ (row 14) are unaffected.*

If the $2\pi$ factor were phenomenological, the substrate prediction would be a fit. It is not. The substrate prediction is $a_0 = cH_0/(2\pi)$ with:

- $c$ and $H_0$ empirically determined,
- $1/(2\pi)$ structurally forced by §5.1's dipole-projection integral on the residual $SO(2)$.

No free parameter.

Empirically: with $H_0 = 70\,\mathrm{km/s/Mpc} = 2.27 \times 10^{-18}\,\mathrm{s^{-1}}$:

$$
a_0 = \frac{(3 \times 10^8)(2.27 \times 10^{-18})}{2\pi} = \frac{6.81 \times 10^{-10}}{6.283} \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}.
$$

The measured MOND $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$. Match within ~10%, parameter-free.

If the substrate prediction had been $cH_0/(2\pi^2)$, $cH_0/(4\pi)$, or $cH_0/\pi$, the numerical match would be different (off by factors of ~$\pi$, 2, $1/2$ respectively, none of which match the ~10% empirical agreement). The $2\pi$ factor produces a non-trivial parameter-free match.

### 5.4 The numerical match in context

Hubble-tension range $H_0 \in [67, 74]\,\mathrm{km/s/Mpc}$:

- $H_0 = 67$: $a_0 \approx 1.03 \times 10^{-10}\,\mathrm{m/s^2}$.
- $H_0 = 74$: $a_0 \approx 1.14 \times 10^{-10}\,\mathrm{m/s^2}$.

Empirical MOND $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$. Substrate range $\approx [1.03, 1.14] \times 10^{-10}$. The ~10% gap is consistent with the joint $H_0$ + MOND-$a_0$ uncertainty. **This is the empirical wedge motivating the substrate-gravity arc.**

> **Precision note (2026-09-04).** *“Consistent with the joint uncertainty”* is defensible but soft, and the shape of the gap is worth stating: the offset is **one-sided**. The $2\pi$ prediction sits **below** the canonical $a_0$ at **every** $H_0$ in the range, and closing it exactly requires either $a_0 \approx 1.08\times10^{-10}$ (at $H_0 = 70$) or $H_0 \approx 77.6$ — the latter above even the local distance-ladder value. A one-sided systematic offset is a weaker form of agreement than two-sided overlap. **This is not a claim that the gap is a real tension:** that depends on the current best $a_0$ determination and its *systematic* error budget, which is not asserted here. **CHECK RUN 2026-09-04 — see §5.5 below.** The systematic has tightened by a factor of 2.7 since the figure this section was written against, and the `2\pi`'s standing has moved with it. See `Note_a0_TwoPi_RepairRoutes.md` §4e and `Gravity_TieredClaims_Ledger.md` Staleness #38–#39.

---


### 5.5 The check, run 2026-09-04: two determinations, and the $2\pi$ now prefers a high $H_0$

§5.4 was written against the 2016 SPARC figure. A current lookup finds two determinations:

| Source | $a_0$ ($10^{-10}\,\mathrm{m/s^2}$) | stat | sys | combined |
|---|---|---|---|---|
| McGaugh, Lelli & Schombert 2016 (SPARC RAR) | 1.20 | ±0.02 | ±0.24 | ±0.241 |
| **Desmond 2023** (MNRAS 526, 3342; HMC joint inference on SPARC) | **1.19** | **±0.04** | **±0.09** | **±0.098** |

**The systematic has tightened by 2.7×.** The 2016 ±0.24 was a 20% normalisation uncertainty from holding disk and bulge mass-to-light ratios fixed across the sample; Desmond's joint inference fits galaxy parameters simultaneously and reduces it to ±0.09.

ED's $a_0 = cH_0/(2\pi)$ requires:

| $H_0$ | required $a_0$ | vs 2016 ($\pm0.241$) | vs **Desmond 2023** ($\pm0.098$) |
|---|---|---|---|
| 67.4 (Planck) | 1.042 | 0.66$\sigma$ | **1.50$\sigma$** |
| 70 | 1.082 | 0.49$\sigma$ | **1.09$\sigma$** |
| 73 (SH0ES) | 1.129 | 0.30$\sigma$ | **0.62$\sigma$** |
| 74 | 1.144 | 0.23$\sigma$ | **0.46$\sigma$** |

**Two things follow, and the second is the substantive one.**

**(1) §5.4's wording is now stale.** *“Consistent with the joint uncertainty”* was fair against ±0.24, where the offset was half a sigma. Against ±0.09 the honest reading is **not excluded, at roughly 1.1$\sigma$** — and the offset is one-sided, sitting below the measured $a_0$ at every $H_0$ in the range.

**(2) $a_0 = cH_0/(2\pi)$ takes a side in the Hubble tension.** The relation is more comfortable with the **local distance-ladder** $H_0$ than with the **CMB** value: 0.62$\sigma$ at SH0ES against 1.50$\sigma$ at Planck. **This is not a prediction of $H_0$** — ED inherits $H_0$ and derives neither value (§8.1) — it is a **consistency constraint between two independently measured quantities**, and it is the sharpest empirical handle the $2\pi$ has.

**Why the $a_0$ side of this is robust.** A fitted $a_0$ might be suspected of depending on the assumed interpolation family, which would blunt the test. It does not: $a_0$ is *defined* by the deep-MOND normalization and the asymptotes cross at $a_0$ for every $\mu$ family (`Note_a0_ThresholdFromHorizonCompetition.md` §5, checked numerically across three families). Desmond's inference marginalises over functional forms and returns a value consistent with the 2016 fixed-form fit, which is what that argument predicts.

**Falsifier F-2π (new, and it sharpens on its own).** If $a_0$ tightens further while the CMB $H_0$ holds, the $2\pi$ is squeezed without anyone deriving or refuting it structurally: at $H_0 = 67.4$, a combined uncertainty of $\pm0.05$ would put the offset at $3\sigma$. Conversely a local-ladder $H_0$ with $a_0$ settling near 1.13 would confirm it below $1\sigma$. **This is now registered as prediction 1.16** (`predictions/Paper_ED_Pred_H0_From_a0.md`): read backwards, $H_0 = 2\pi a_0/c$ makes $a_0$ a **measurement of the Hubble constant from rotation curves** — a probe with no MOND analogue, since there $a_0$ is a constant of nature. **The coefficient question may be settled by measurement before it is settled by derivation** — which, given that four structural routes have reached $cH_0$ and none has reached the coefficient, is worth stating as the live possibility it is.

---

## 6. Identification of $a_0$

### 6.1 The full structural identification

$$
\boxed{a_0 = \frac{cH_0}{2\pi}}
$$

where:

- $c$ is the substrate-level speed of light.
- $H_0$ is the empirical Hubble parameter (value-layer, not derived).
- $1/(2\pi)$ is the azimuthal-Fourier-mode normalization on the chain's residual $SO(2)$ symmetry (structurally forced by the dipole-projection integral, §5.1).

The result is parameter-free given $H_0$.

### 6.2 What is structural vs. what is inherited

- **Structural:** existence of cosmic decoupling surface at $R_H = c/H_0$; dipole as leading anisotropic mode; $1/(2\pi)$ Fourier-normalization factor; result $a_0 = cH_0/(2\pi)$.
- **Inherited:** numerical $H_0$ (cosmological measurement); numerical $c$; substrate-graph normalization conventions (anchored at substrate-graph scale).

### 6.3 The empirical wedge

Parameter-free prediction: $a_0^{\mathrm{ED}} \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}$ (at $H_0 = 70$); empirical MOND $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$. Match ~10%. Neither MOND-as-phenomenology nor dark-matter-as-particle account derives this match.

---

## 7. Cross-Domain Context

### 7.1 Combination with Newton's $G$ (Paper_030)

Joint weak-gradient regime: $a = \sqrt{a_N \cdot a_0}$. Paper_030 develops the ECR; this paper supplies $a_0$.

### 7.2 Slope-4 BTFR (Paper_031)

$v_{\mathrm{flat}}^4 = G \cdot M \cdot a_0$. Predicted intrinsic scatter zero in deep-MOND asymptotic.

### 7.3 V5 cross-domain context

The dipole-mode projection developed in §4–§5 is structurally analogous to V5 cross-chain correlation mechanisms (Paper #20 / Paper_090). Both involve substrate-level participation-structure interactions across substrate-graph distances.

---

## 8. What This Paper Does NOT Claim

### 8.1 $H_0$ is not derived

$H_0$ is empirical cosmological content. ED does not derive $H_0$.

### 8.2 Cosmology is not derived

ED does not derive Big Bang, structure formation, CMB, or large-scale-structure spectra. The substrate-decoupling-surface mechanism is conditional on cosmological inputs.

### 8.3 No claim that $a_0$ is forced from nothing

The derivation is conditional on the postulated primitives + V1 inheritance + accelerating-chain structure + empirical $H_0$.

### 8.4 No claim that the `1/(2π)` is currently established *(added 2026-09-04)*

As of 2026-09-04 the `1/(2π)` factor is **disputed within the corpus** and this paper should not be cited for it. See the open-item banner at the head of this paper and Staleness #10 in `Gravity_TieredClaims_Ledger.md`. The horizon-tied scale `a₀ ~ cH₀`, and the evolution `a₀(z) = cH(z)/(2π)` with its forced exponent of 1, are unaffected.

### 8.5 No claim about MOND correctness or dark matter

ED supplies a mechanism for the empirically observed transition acceleration. It does not claim MOND-as-complete-theory is correct or that dark matter is excluded. Coexistence with dark-matter particle content is an open question.

### 8.5 No claim about $H_0$ value

Hubble tension is unresolved in cosmology; ED does not resolve it. Predicted $a_0$ tracks whichever $H_0$ is empirically correct.

### 8.6 No claim of cosmological-curvature derivation

The cosmic decoupling surface at $R_H = c/H_0$ is the substrate-level effective horizon, not the cosmological event horizon of standard GR.

### 8.7 No claim of MOND-interpolation equivalence

ED produces the transition acceleration scale, not the full MOND interpolation function $\mu(x)$. ED's transition profile (via Paper_030's ECR) is structurally derived; empirical comparison to specific MOND $\mu(x)$ choices is downstream work.

### 8.8 $a_0$ is *not* cosmologically constant — it evolves (the forward prediction, now data-confronted)

Distinct from the $H_0$-value point of §8.5: because $a_0 = cH/(2\pi)$ reads the horizon $R_H = c/H$ *at the epoch in question*, the transition scale is not a constant of nature but tracks the *instantaneous* Hubble rate, $a_0(z) = cH(z)/(2\pi)$ — developed as a forward prediction in **Paper_031 §8.8** and **Paper_038 CO-3**, with ED's mechanism forcing the exponent $\alpha = 1$ in $a_0 \propto H^\alpha$. First data — **MUSE-DARK III (A&A 2026)** — detect this evolution across $0.33 < z < 1.44$ at **~30σ**, excluding a constant $a_0$ (and so burying constant-scale MOND), with a ~8% match to the local value. The measured rate runs mildly *faster* than $H(z)$, so ED's forced $\alpha = 1$ is confirmed in *direction* but in mild tension on the *exact rate* — the decisive open number for Rubin/Euclid. This paper derives only the local normalization $a_0 = cH_0/(2\pi)$; the evolution and its data-confrontation live in the cited companions.

---

## 9. Falsification Criteria

### 9.1 $H_0$ measurements shift predicted $a_0$ outside MOND-$a_0$ range

Currently $H_0 \in [67, 74]$, $a_0^{\mathrm{ED}} \in [1.03, 1.14] \times 10^{-10}\,\mathrm{m/s^2}$. Empirical MOND $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$. If Hubble tension resolves to $H_0 = 60$, prediction $\approx 0.92 \times 10^{-10}$ falls outside empirical MOND range — substrate mechanism falsified.

### 9.2 Galaxy-catalog $a_0$ disagrees at improved precision

If improved measurements pin empirical $a_0 \neq cH_0/(2\pi)$ at 1% precision, the substrate mechanism is falsified.

### 9.3 Dipole projection fails observationally

If empirical evidence shows the leading anisotropic mode is not the dipole (e.g., quadrupole dominance) or the geometric factor differs from $1/(2\pi)$ (e.g., empirical $a_0$ matches $cH_0/(4\pi)$ or $cH_0/\pi$ better), the dipole-projection mechanism is falsified.

### 9.4 Different $a_0$ for different galaxies

If empirical $a_0$ varies systematically with galaxy type beyond what universality predicts, the cosmic-horizon-derived universality is falsified.

### 9.5 Cosmic-decoupling-surface mechanism fails

If empirical evidence shows substrate-level cross-locus influence reaching local chains from $\gg R_H$, the substrate boundary mechanism is falsified.

### 9.6 BTFR slope-4 breakdown (cross-paper)

If BTFR slope $\neq 4$ at high precision, the joint Papers_027 + 029 + 030 + 031 product is falsified.

---

## 10. Position Statement

The transition acceleration $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$ is **not** a free parameter, empirical fit, or phenomenological coincidence. In the ED Generative Primitives System:

$$
a_0 = \frac{cH_0}{2\pi},
$$

with:

- $c$ substrate-level speed of light.
- $H_0$ empirical Hubble parameter (value-layer).
- $1/(2\pi)$ azimuthal-Fourier-mode normalization on the chain's residual $SO(2)$ symmetry — **structurally forced** by the §5.1 dipole-projection integral.

Numerical match: $a_0^{\mathrm{ED}} \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}$ at $H_0 = 70$; empirical MOND $a_0 \approx 1.2 \times 10^{-10}\,\mathrm{m/s^2}$. Match within ~10%, parameter-free.

What this paper claims:

- $a_0 = cH_0/(2\pi)$ is the unique downstream structural identification given the postulated primitives + Paper_027 result + empirical $H_0$.
- The $2\pi$ factor is geometric (azimuthal-Fourier normalization on residual $SO(2)$), made explicit via the dipole-projection integral in §5.1 — not phenomenological.
- The substrate-level mechanism supplies a structural origin for the transition acceleration that no MOND-as-phenomenology or dark-matter-as-particle account provides.
- The ~10% parameter-free numerical match is the empirical wedge.

What this paper does *not* claim:

- $H_0$ and cosmology are not derived.
- $a_0$ is not forced from nothing.
- ED does not derive the full MOND interpolation function.
- ED does not refute dark matter as particle content.
- No claim of cosmological-curvature derivation.

**Series context.** Paper_029 of the gravity arc rewrite. The arc continues:

- **Paper_030:** ED Combination Rule.
- **Paper_031:** Slope-4 BTFR.

---

## Appendix: Cross-References and Glossary

### Cross-references

- **Position paper:** `paper_ED_Framework_13_Primitive_Generative_System.md`.
- **Paper_027 (Newton's $G$):** companion in the gravity arc.
- **Paper #18 (V1 N1), #19 (V1 T18):** kernel inheritance.
- **Paper #20 / Paper_090 (V5):** brief mention §7.3.
- **Paper_030, 031:** gravity-arc continuation.

### Glossary

- **Transition acceleration $a_0$.** $a_0 = cH_0/(2\pi) \approx 1.08 \times 10^{-10}\,\mathrm{m/s^2}$.
- **Cosmic decoupling surface.** Substrate-level effective horizon at $R_H = c/H_0$.
- **Hubble parameter $H_0$.** Empirical; current range $H_0 \in [67, 74]\,\mathrm{km/s/Mpc}$.
- **Dipole-mode projection.** The $l=1$, $m=0$ projection of the cosmic decoupling surface onto an accelerating chain's adjacency, supplemented by the $|n|=1$ azimuthal-Fourier projection on the chain's residual $SO(2)$ symmetry.
- **Azimuthal-Fourier-mode normalization.** $\frac{1}{2\pi}\int_0^{2\pi}e^{-in\phi}e^{im\phi}\,d\phi = \delta_{nm}$ — the canonical Fourier-series normalization on the circle. Source of the $1/(2\pi)$ factor in $a_0$.
- **Residual $SO(2)$ symmetry.** The rotational symmetry about the acceleration axis remaining after the chain's uniaxial acceleration breaks $SO(3)$.
- **Newtonian / Transition / Deep-MOND regimes.** Defined by ratio $a_N/a_0$.
- **Hubble tension.** Empirical $H_0$ discrepancy; relevant to substrate-prediction uncertainty.

---

**End of Paper_029.**

*Wave-2 Generative Paper — Gravity Arc, Foundation. Round-2 revision: §5.1 dipole-projection integral made explicit, with $1/(2\pi)$ shown to arise from azimuthal-Fourier-mode normalization on the residual $SO(2)$ symmetry rather than from an asserted "period argument."*
