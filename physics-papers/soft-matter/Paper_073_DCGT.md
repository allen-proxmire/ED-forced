# Paper_073 — The Diffusion Coarse-Graining Theorem (DCGT)

**Series:** Event Density (ED) Generative Papers — Wave-2 soft-matter / cross-domain bridge (foundational substrate→continuum theorem; load-bearing for V5, gravity arc, BH arc, and Wave-3 corpus inheritance)
**Author:** Allen Proxmire
**Status:** Verdict per Paper_095: **M3 (form-IDENTIFIED + value-INHERITED) within hydrodynamic-window scale-separation regime $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$.** Conditional structural derivation given the 13 ED primitives (Paper_087) + V1 inheritance (Paper_089) + V5 dependence (Paper_090). Standalone; cold-reader accessible.
**Date:** 2026-05-13 (Wave-2 vintage; refreshed 2026-05-18 to current Paper_095 grammar + 5-anchor verdict sync + substrate-ontology lineage citation).
**Lineage:** This paper sits within the **substrate-ontology research-program lineage** ('t Hooft cellular-automaton interpretation of QM; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), **not** within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (Paper_087).
2. **DCGT is not the only possible substrate→continuum bridge.** Other coarse-graining procedures (Wilsonian RG, hydrodynamic projection, mode-coupling) may apply in specific regimes; DCGT is the one substrate-level bridge derived from substrate-graph diffusion of V1/V5 content.
3. **DCGT does not derive continuum-level coupling constants or transport coefficients.** It supplies the *form* of continuum equations (diffusion-type, propagator-type, constitutive-law-type); the *coefficients* (diffusion constant, viscosity, conductivity, etc.) are inherited from value-layer empirical content and substrate-level matching at the coarse-graining scale.
4. **DCGT is regime-conditional.** It applies in the hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$. Outside this window (strong-gradient regimes, near-substrate-scale physics, near-singularity regimes), DCGT breaks down.
5. **No claim that DCGT derives standard QFT renormalization.** DCGT operates one structural level below RG: it produces the continuum theory whose RG flow is then studied by standard techniques. The relationship between DCGT and Wilsonian RG is an active area (Papers in queue).
6. **DCGT is not a derivation of Einstein equations.** The substrate→continuum bridge produces flat-spacetime continuum equations under the standard hydrodynamic window; curvature emergence is the subject of the Arc ED-10 program, not DCGT.
7. **No claim that DCGT is exhaustive across all ED arcs.** Soft-matter Maxwell relaxation, gravity-arc cumulative-strain, BH-arc Hawking spectrum, and Q-COMPUTE multiplicity-cap behavior all use DCGT differently; the regime-specific applications are developed in arc-specific papers.

---

## Abstract

The **Diffusion Coarse-Graining Theorem (DCGT)** is the substrate→continuum bridge in the Event Density Generative Substrate Ontology: given the 13 postulated primitives (Paper_087) + V1 inheritance (Paper_089) + V5 dependence (Paper_090), substrate-level kernel-mediated content coarse-grains under the **hydrodynamic-window scale separation** $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ to continuum diffusion-type / propagator-type / constitutive-law equations. The theorem has three load-bearing components: (1) **scale separation** — substrate-graph operations at scale $\ell_{\mathrm{ED}}$ produce well-defined coarse-grained content at scale $R_{\mathrm{cg}}$ that depends on macroscopic flows at scale $L_{\mathrm{flow}}$ but is decoupled from substrate microstructure; (2) **diffusion-form emergence** — V1's finite-width retarded envelope coarse-grains to a continuum diffusion operator under standard substrate-graph averaging; (3) **cross-domain instantiations** — DCGT produces continuum Maxwell relaxation in soft-matter (V5 soft-regime), retarded / Feynman / advanced propagator hierarchy in QFT (V5 QFT-regime), Lieb–Robinson velocity bound in condensed matter, and curved-spacetime entanglement at horizons (V5 BH-regime). The paper makes no claim that DCGT is the only substrate→continuum bridge, no claim of derivation of continuum-level transport coefficients, no claim of validity outside the hydrodynamic window, and no claim of curvature-emergence derivation. **Verdict per Paper_095: M3 (form-IDENTIFIED + value-INHERITED)** within the hydrodynamic-window scale-separation regime — diffusion-form emergence is substrate-derived (form); transport coefficients are inherited via empirical matching (value); regime is explicit A→regime scale-separation. The empirical case rests on cross-domain reach: DCGT is load-bearing for Paper_090 (V5 cross-chain kernel applications), the gravity arc (Papers_027/029/030/031), the BH arc (Papers_039/047), the soft-matter arc, and the entire Wave-3 corpus (Cos_01–Cos_06, Dyn_01–Dyn_05, GW_00–GW_02) which inherits DCGT as the substrate→continuum bridge at M3-equivalent level.

---

## 1. Introduction

Standard physics operates in the continuum (fields, propagators, diffusion equations, hydrodynamics); ED's substrate ontology operates on discrete substrate-graph content (chains, channels, polarity-transport, commitment). **DCGT is the bridge** — substrate-level kernel-mediated content coarse-grains under the hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ to continuum diffusion-type / propagator-type / constitutive-law equations.

The paper (i) states DCGT formally with the regime assumption explicit; (ii) derives diffusion-form emergence from V1 finite-width + substrate-graph averaging; (iii) catalogues cross-domain instantiations (Maxwell relaxation, QFT propagators, Lieb–Robinson velocity, KMS-thermal); (iv) specifies breakdown conditions.

**Corpus role.** DCGT is upstream of Paper_090 (V5 cross-domain), Paper_027 (Newton's $G$), Paper_039 + Paper_047 (BH arc), and is inherited by the entire Wave-3 corpus (Cos_01–Cos_06, Dyn_01–Dyn_05, GW_00–GW_02) as the substrate→continuum bridge at M3-equivalent inheritance level — every continuum-level empirical prediction in the corpus traces structurally through DCGT.

**Verdict per Paper_095: M3 (form-IDENTIFIED + value-INHERITED)** within the hydrodynamic-window regime. Five-anchor verdict-sync: status / Abstract / this §1 / audit verdict row / §9 Position Statement all read M3.

---

## 2. Primitive Inputs

This paper takes the following ED substrate primitives as **postulated** (Paper_087):

- **P02 (Participation).**
- **P03 (Channel + locus indexing; spatial homogeneity).** Translation-invariance is load-bearing for the substrate-graph averaging.
- **P04 (Bandwidth as non-negative additive scalar).** Additivity is load-bearing for coarse-grained substrate content.
- **P05 (Polarity-transport along edges).**
- **P06 (Spatial dimension $D = 3+1$).** Continuum diffusion operators are $D$-dimensional.
- **P07 (Channel structure).**
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$).** Defines the substrate-graph granularity below which DCGT does not resolve.
- **P09 ($U(1)$-valued polarity).**
- **P10 (Rule-type primitive).**
- **P11 (Commitment irreversibility).**
- **P13 (Time homogeneity).**

**V1 inheritance (Paper_089):** finite-width retarded structure; substrate-level kernel that coarse-grains to continuum diffusion / propagator operators.

**V5 dependence (Paper_090):** cross-chain correlation kernel; coarse-grains to continuum constitutive laws (Maxwell relaxation, Lieb–Robinson bound, KMS-thermal structure).

**Upstream paper dependencies:**

- **Paper_087:** position paper.
- **Paper_089:** V1 canonical reference.
- **Paper_090:** V5 cross-chain kernel.

**Empirical / value-layer inputs:**

- Substrate scale $\ell_{\mathrm{ED}}$ empirically identified with $\ell_P$ (Paper_027 §5.3).
- Coarse-graining scale $R_{\mathrm{cg}}$ regime-dependent.
- Macroscopic flow scale $L_{\mathrm{flow}}$ regime-dependent.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| V1 finite-width retarded structure | D | Paper_089 |
| V5 cross-chain correlation kernel | D | Paper_090 |
| Hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ | A→regime | **Regime assumption**, §3.1 |
| Substrate-graph averaging at $R_{\mathrm{cg}}$ produces well-defined continuum content | D | §3.2 from P03 translation-invariance + P04 additivity |
| V1 envelope coarse-grains to diffusion operator | D | §4 from V1 finite-width + substrate-graph averaging |
| V5 envelope coarse-grains to memory-kernel diffusion | D | §5 from V5 finite-memory + cross-chain averaging |
| Continuum Maxwell relaxation form (exponential decay) | D | §6.1 from §5 V5 Markovian-limit derivation (form is derived) |
| Continuum Maxwell relaxation **numerical** $\tau_{\mathrm{Maxwell}}$ value | **I** | §6.1. $\tau_{V5}^{\mathrm{soft}} = \tau_{\mathrm{Maxwell}}^{\mathrm{empirical}}$ via empirical matching. (Round-3 downgrade: D → I.) |
| Continuum propagator hierarchy (QFT) form | D | §6.2 from V1/V5 substrate kernel coarse-graining via §4 + §5. |
| Lieb–Robinson velocity bound form $v_{LR} \sim \ell_{V5}/\tau_{V5}^{\mathrm{ent}}$ | **A→position** | §6.3. Identification by dimensional analogy to the standard Lieb–Robinson theorem (Lieb–Robinson 1972 — tight commutator-norm bound from Hamiltonian locality). Substrate-level derivation requires more than dimensional analysis; the form is supplied at A→position framing-claim level per Paper_095 §3.3, not as substrate-graph derivation. (Round-3 downgrade: D → A→position.) |
| KMS-thermal structure at horizons (BH) | D | §6.4 from §5 V5 imaginary-time substrate-graph extension + DCGT. |
| Breakdown taxonomy (strong-gradient / near-substrate / near-singularity / strong-curvature) | **P** | §7.1–§7.4. Substrate-level regime-failure taxonomy declared at breakdown-regime classification level. (Round-3 downgrade: D → P.) |
| Numerical transport coefficients | **I** | Empirical inheritance. |
| **Verdict M3 (form-IDENTIFIED + value-INHERITED) within hydrodynamic-window scale-separation regime** | **A→position** | Per Paper_095 §3.3 line 77. Five-anchor verdict-sync: status / Abstract / §1 / this row / §9 all M3. Form derived (rows on V1/V5 coarse-graining + diffusion-form + memory-kernel + Maxwell-form + QFT-propagator + KMS-thermal); value inherited (Maxwell $\tau$, transport coefficients); regime explicit (hydrodynamic-window scale separation). |

One row is **A→regime** (hydrodynamic-window scale separation §3.1) — explicitly labeled as regime assumption per QC discipline. One row is **A→position** for the Lieb–Robinson identification (§6.3 dimensional-analogy framing). One row is **A→position** for the verdict-tier (final row). All other substantive rows are P, D, or I. **No A (asserted-without-label) rows.**

---

## 3. Setup — Scale Separation and Substrate-Graph Averaging

### 3.1 The hydrodynamic-window scale separation (regime assumption)

DCGT operates in the **hydrodynamic-window scale separation**:

$$
\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}.
$$

where:

- $\ell_{\mathrm{ED}}$: substrate scale (Primitive P08).
- $R_{\mathrm{cg}}$: coarse-graining scale — the spatial / temporal extent over which substrate-graph content is averaged to produce continuum-level quantities.
- $L_{\mathrm{flow}}$: macroscopic flow scale — the spatial / temporal extent over which continuum-level quantities vary appreciably.

**This is a regime assumption, not a derivation.** DCGT's conclusions apply when the scale separation holds. Outside this window (e.g., $R_{\mathrm{cg}} \sim \ell_{\mathrm{ED}}$, near-substrate-scale; or $R_{\mathrm{cg}} \sim L_{\mathrm{flow}}$, near-flow-scale), DCGT breaks down (§7).

In practice, $R_{\mathrm{cg}}$ is chosen anywhere in the scale-separated window; coarse-grained quantities are insensitive to the specific choice within the window (the hallmark of effective-theory regime stability).

### 3.2 Substrate-graph averaging

A **substrate-graph average** of a substrate-level quantity $\mathcal{Q}(u, t)$ at coarse-graining scale $R_{\mathrm{cg}}$ is:

$$
\langle \mathcal{Q}\rangle_{R_{\mathrm{cg}}}(\bar{u}, \bar{t}) = \frac{1}{V_{R_{\mathrm{cg}}}}\int_{|u - \bar{u}| < R_{\mathrm{cg}}}\int_{|t - \bar{t}| < R_{\mathrm{cg}}/c}\mathcal{Q}(u, t)\,d\mu_{\mathrm{substrate-graph}}
$$

where $V_{R_{\mathrm{cg}}}$ is the substrate-graph volume of the coarse-graining cell and $d\mu_{\mathrm{substrate-graph}}$ is the substrate-graph measure (substrate channels per substrate cell).

**Well-definedness.** By P03 (spatial homogeneity), translation-invariance of substrate-graph operations means the average depends only on $(\bar{u}, \bar{t})$ — the coarse-graining center — not on the specific substrate channels enumerated within the cell. By P04 (bandwidth additivity), substrate bandwidth contributions sum additively within the cell.

> **Regime condition on the second sentence, added 2026-09-05.** **P04's stated additivity is over *disjoint sub-channels at a locus*; summing bandwidth over *loci within a cell* is a different operation, and it is not additive in general.** Canonical `Paper_087` §P12 gives the general rule for combining contributions as $b(U)=\sum_a b_a + 2\sum_{a<b}\sqrt{b_a b_b}\cos\Delta\pi_{ab}$ — the cross term is $\mathrm{Coh}$ — and `P-Motif-Algebra` (`Paper_007` §2) makes **amplitudes**, not bandwidths, the additive objects. **Bandwidth additivity within a cell is the random-phase limit of that rule** ($\mathrm{Coh}\to 0$; Monte-Carlo confirmation in `internal notes/_check_merge_rule_regimes.py`). **DCGT is entitled to it** — §3.3 explicitly averages out *"specific channel labels, specific commitment-event timings,"* which is the microstructure carrying the phase, so the hydrodynamic window *is* the decoherent regime. **But the clause above reads as a general consequence of P04, and it is not**, and this paper is inherited by the whole Wave-3 corpus. **Anything applying §3.2 where phase coherence survives across the cell needs the amplitude rule instead.** `foundations/Note_EdgeWeight_Discriminator_2026-09-05.md` §8c; gravity ledger #89. **Nothing in DCGT's own results changes.**
>
> **Follow-up the same day — this is not a `Paper_073` defect, it is a corpus-wide one, and `Paper_073` is on the safe side of it.** Every DCGT-citing paper was screened and the P04-additivity sites adjudicated (`internal notes/_check_dcgt_regime_users.py`; gravity ledger #90). **No live error anywhere.** The coherence-critical papers do not inherit this clause at all — they coarse-grain *amplitudes* (`Paper_004_6_Tsirelson_Continuum`: $P_K\to\Psi(x)$), *connections* (`Paper_009_BerryPhase`) or *operator support* (`Paper_066_NoSignaling`), not bandwidths. And the sites that do sum bandwidth over a region are each licensed — by disjoint channels, by commitment, or by decoherence. **The licensing rule is now stated once, canonically, at `Paper_087` P04**, and `Paper_073` §3.2 falls under its clause (c).

**Dimensional check:** $\langle\mathcal{Q}\rangle_{R_{\mathrm{cg}}}$ has the same dimensions as $\mathcal{Q}$ (averaging is dimensionless). ✓

### 3.3 What survives coarse-graining

Substrate-level content that varies on scales $\sim \ell_{\mathrm{ED}}$ is **averaged out**: substrate-graph microstructure (specific channel labels, specific commitment-event timings) becomes invisible at scale $R_{\mathrm{cg}}$.

Substrate-level content that varies on scales $\sim L_{\mathrm{flow}}$ **survives**: macroscopic flows of bandwidth, polarity, strain content are captured by the coarse-graining.

Substrate-level content at the intermediate scale $\sim R_{\mathrm{cg}}$ has partial visibility: it depends on the specific $R_{\mathrm{cg}}$ choice within the scale-separated window.

---

## 4. V1 Kernel → Continuum Diffusion Operator

### 4.1 V1 envelope at substrate-graph scale

By Paper_089, V1 has the canonical form:

$$
K_{V1}(x, x') = \theta(t - t')\,G(\sigma(x, x')/\ell_{\mathrm{ED}}^2).
$$

The envelope $G$ is bounded, finite-width with characteristic scale $\ell_{\mathrm{ED}}$, decaying outside the substrate-graph scale.

### 4.2 Coarse-graining V1 to a diffusion-type operator

Coarse-grain V1 at scale $R_{\mathrm{cg}}$ via the substrate-graph averaging of §3.2. For separations $|x - x'| \gg \ell_{\mathrm{ED}}$, the V1 envelope $G(\sigma/\ell_{\mathrm{ED}}^2)$ becomes effectively local at scale $R_{\mathrm{cg}}$ — the kernel acts like a **point-supported operator** with effective range $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}}$.

The continuum-limit operator $\hat{D}_{\mathrm{cont}}$ defined by:

$$
\hat{D}_{\mathrm{cont}}\,\psi(x) = \int K_{V1}(x, x')\,\psi(x')\,d^4x'
$$

(restricted to retarded support) reduces in the hydrodynamic window to a **local differential operator** acting on the coarse-grained field $\psi(\bar{x})$. The standard expansion (Taylor in $(x - x')/R_{\mathrm{cg}}$ to second order; constant + first + second derivative terms) gives:

$$
\hat{D}_{\mathrm{cont}}\,\psi(\bar{x}) \approx \left[a_0 + a_1\,\partial_t + D\,\nabla^2 + \mathcal{O}(\partial^3)\right]\psi(\bar{x})
$$

where:

- $a_0$ = $\int G\,d^4(\Delta x)$ (zeroth-moment integral of the V1 envelope).
- $a_1$ = $\int G\,\Delta t\,d^4(\Delta x)$ (first-moment in time).
- $D$ = $(1/6)\int G\,|\Delta\vec{x}|^2\,d^4(\Delta x)$ (second-moment in space; gives diffusion constant).

**Dimensional check:** $\hat{D}_{\mathrm{cont}}$ has dimensions of $[1/\mathrm{time}]$ when $G$ has dimensions $[1/\mathrm{length}^3 \cdot 1/\mathrm{time}]$ (for 3+1 D propagator-density convention); $D$ has dimensions $[\mathrm{length}^2/\mathrm{time}]$ as expected for diffusion constant. ✓

### 4.3 Diffusion-form result

In the hydrodynamic window, V1's coarse-grained action on substrate content reduces to a **diffusion-type continuum operator**:

$$
\hat{D}_{\mathrm{cont}} \approx \partial_t - D\,\nabla^2 + (\text{higher-order corrections})
$$

(after suitable normalization absorbing the zeroth-moment $a_0$). This is the substrate→continuum diffusion form: V1 cross-chain content propagates at the substrate level via finite-width retarded kernel, and coarse-grains to a continuum diffusion equation with diffusion constant $D$ set by V1's second-moment substrate-graph structure.

### 4.4 Where the diffusion constant comes from

The numerical value of $D$ is set by:

- V1's specific functional shape (envelope details inherited from substrate-coefficient anchoring).
- The substrate scale $\ell_{\mathrm{ED}}$.

For a generic V1 envelope $G \sim e^{-\sigma/\ell_{\mathrm{ED}}^2}$, $D \sim \ell_{\mathrm{ED}}^2/\tau_{V1}$ where $\tau_{V1} \sim \ell_{\mathrm{ED}}/c$. This gives $D \sim c\ell_{\mathrm{ED}}$ at the substrate scale.

In specific regimes (soft-matter, condensed-matter, BH), the effective $D$ is renormalized by substrate-coefficient matching to empirical values — **value-layer empirical content**, not substrate-derived. DCGT supplies the *form* (diffusion equation); the *coefficient* is matched.

---

## 5. V5 Kernel → Continuum Memory-Kernel Diffusion

### 5.1 V5 envelope

By Paper_090, V5 has the canonical form:

$$
K_{V5}(u_A, t_A; u_B, t_B) = \theta(t_A - t_B)\,F_{V5}(\sigma/\ell_{V5}^2, (t_A - t_B)/\tau_{V5}).
$$

V5 has both finite spatial extent ($\ell_{V5}$) and finite memory time ($\tau_{V5}$).

### 5.2 Coarse-graining V5 to memory-kernel diffusion

The same substrate-graph averaging of §3.2 applied to V5 yields a **memory-kernel diffusion operator** in the continuum:

$$
\hat{D}_{\mathrm{cont}}^{V5}\,\psi(\bar{x}, \bar{t}) = \int_0^\infty d\tau\,\mathcal{M}(\tau)\left[D_{V5}\,\nabla^2\psi(\bar{x}, \bar{t} - \tau) - \psi(\bar{x}, \bar{t} - \tau)/\tau_{V5}\right]
$$

where $\mathcal{M}(\tau)$ is the **memory kernel** inherited from V5's temporal envelope $F_{V5}$, $D_{V5}$ is the V5 diffusion constant (analog of §4.3), and $\tau_{V5}$ is the V5 memory time.

**Dimensional check:** $\mathcal{M}(\tau)$ has dimensions $[1/\mathrm{time}]$; $D_{V5}\nabla^2\psi$ has $[\psi/\mathrm{time}]$; $\psi/\tau_{V5}$ has $[\psi/\mathrm{time}]$; integral $\int d\tau$ has $[\mathrm{time}]$; total: $\hat{D}_{\mathrm{cont}}^{V5}\psi$ has $[\psi]$ — consistent with $\hat{D}$ being a differential / integral operator. ✓

### 5.3 Markovian limit

In the **Markovian limit** $\tau_{V5} \to 0$ (V5 memory time fast compared to flow timescale $L_{\mathrm{flow}}/c$), the memory kernel becomes $\mathcal{M}(\tau) \to \delta(\tau)$, and the operator reduces to a Markovian diffusion + decay form:

$$
\hat{D}_{\mathrm{cont}}^{V5,\,\mathrm{Markov}} \approx D_{V5}\,\nabla^2 - 1/\tau_{V5}.
$$

This is the substrate-level structural origin of standard Markovian diffusion + exponential relaxation in soft-matter (§6.1) and condensed-matter (§6.3) contexts.

### 5.4 Non-Markovian regime

In the **non-Markovian regime** ($\tau_{V5}$ comparable to flow timescale), the full memory kernel $\mathcal{M}(\tau)$ contributes. The resulting continuum equation is a **generalized diffusion equation with memory**:

$$
\partial_t\psi(\bar{x}, t) = \int_0^t \mathcal{M}(t - t')\,D_{V5}\,\nabla^2\psi(\bar{x}, t')\,dt' - \psi/\tau_{V5}.
$$

This is the substrate-level structural origin of non-Markovian behavior in soft-matter (Maxwell viscoelastic response with frequency-dependent moduli) and BH-radiation (non-thermal corrections to Hawking spectrum, Paper_047).

---

## 6. Cross-Domain Instantiations

### 6.1 Soft-matter Maxwell relaxation — form derived, value empirically matched

**Form (derived).** DCGT applied to V5 in the soft-matter Markovian limit (§5.3) produces the **exponential-decay form** of the Maxwell stress-relaxation modulus:

$$
G(t) = G_0\,e^{-t/\tau_{V5}^{\mathrm{soft}}}.
$$

The exponential form is a substrate-level structural consequence of V5's Markovian-limit envelope (§5.3).

**Numerical value (empirically matched, not derived).** In the soft-matter regime, $\tau_{V5}^{\mathrm{soft}}$ is **identified with the empirically-measured Maxwell relaxation time** $\tau_{\mathrm{Maxwell}}^{\mathrm{empirical}}$ via direct empirical matching:

$$
\tau_{V5}^{\mathrm{soft}} = \tau_{\mathrm{Maxwell}}^{\mathrm{empirical}} \quad \text{(empirical matching, not substrate-derived)}.
$$

**Honest framing (round-3 QC):** The numerical value of $\tau_{V5}^{\mathrm{soft}}$ in any specific polymer system is **inherited from rheometry** — it is the empirically-measured Maxwell relaxation time for that system. DCGT supplies the *form* (exponential decay); the *coefficient* $\tau_{V5}^{\mathrm{soft}}$ is matched to empirical data, not derived from substrate primitives.

Krieger–Dougherty viscosity and Cross / Carreau / Bird–Carreau constitutive laws emerge as DCGT continuum limits in different soft-matter regimes (high shear, low shear, multi-mode), with each regime's specific numerical coefficients similarly inherited via empirical matching.

### 6.2 QFT propagator hierarchy

In the QFT regime, V1/V5 coarse-graining (§4 + §5) produces standard QFT propagators:

- **Retarded propagator** $G_R$: V1 retarded support coarse-grained to continuum retarded propagator.
- **Feynman propagator** $G_F$: Wick rotation of V1 + V5 in the Euclidean continuation.
- **Advanced propagator** $G_A$: from $G_R$ via mathematical compositional closure (Paper_089 §6.1); not directly substrate-operational but mathematically derivable from $G_R$ via complex-analytic methods.

V1 finite-width supplies the substrate-level UV cutoff $\omega_c = c/\ell_{\mathrm{ED}}$ that becomes the standard QFT regulator (Pauli–Villars, dimensional, lattice) in the continuum limit.

### 6.3 Lieb–Robinson velocity bound — form by dimensional analogy

**A→dimensional-analogy (not derivation).** In the condensed-matter regime, DCGT applied to V5 in the Markovian limit suggests, **by dimensional analysis matching to the standard Lieb–Robinson theorem**, a velocity bound for entanglement-content propagation:

$$
v_{LR} \sim c_{V5}\cdot\frac{\ell_{V5}}{\tau_{V5}^{\mathrm{ent}}}.
$$

**Honest framing (round-3 QC):** This is **dimensional analogy**, not substrate-level derivation. The standard Lieb–Robinson theorem (Lieb–Robinson 1972 + later refinements) is a tight commutator-norm bound from Hamiltonian locality; its derivation requires Hamiltonian-level analysis of bounded local operators. ED's substrate-level $v_{LR}$ form is obtained by matching the substrate-level scales $\ell_{V5}$ and $\tau_{V5}^{\mathrm{ent}}$ to the standard LR-velocity dimensional structure. **The substrate-level mechanism that would derive an LR-type *tight* bound from substrate primitives alone is not supplied in this paper; it is invoked by dimensional analogy to the standard result.** The substrate-level $v_{LR}$ form is a defensible identification at the dimensional level, but it does not constitute a substrate-level proof of the Lieb–Robinson theorem.

### 6.4 BH curved-spacetime entanglement and KMS

In the BH near-horizon regime, V5 acquires imaginary-time periodicity (Paper_047 §3). DCGT applied to V5 in the Euclidean continuation produces the substrate-level KMS condition:

$$
\langle\phi(t_A)\phi(t_B)\rangle_{V5}^{\mathrm{Eucl}} = \langle\phi(t_A + i\beta_H)\phi(t_B)\rangle_{V5}^{\mathrm{Eucl}}, \quad \beta_H = 2\pi/\kappa,
$$

giving thermal Planck spectrum at $T_H = \kappa/(2\pi)$ (Paper_047 §4). The full Hawking spectrum derivation, including the substrate-level non-thermal $(\omega/\omega_c)^2$ corrections, is the subject of Paper_047.

### 6.5 The procedural unity

The four instantiations (§6.1–§6.4) are not four independent mechanisms — they are **one substrate→continuum procedure (DCGT) applied to one substrate primitive (V5)** across four regimes that differ in regime-specific $\tau_{V5}$, $\ell_{V5}$, and substrate-source content. The procedural unity is the cross-domain coherence claim of DCGT (paralleling Paper_090's structural unification of formalism across regimes).

---

## 7. DCGT Breakdown Conditions

### 7.1 Strong-gradient regimes

In regimes where $L_{\mathrm{flow}} \to R_{\mathrm{cg}}$ (gradient scale approaches coarse-graining scale), DCGT breaks down: the scale separation $R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ fails.

**Empirical signature of breakdown:** continuum equations derived via DCGT no longer match substrate-level mechanism predictions. Specific examples:

- Shock waves: gradient scale collapses to substrate scale.
- Near-singularity content in BH evaporation late-stage.
- Strong-coupling soft-matter (gels, glasses) where collective-mode wavelength approaches $\ell_{V5}$.

### 7.2 Near-substrate-scale regimes

In regimes where $R_{\mathrm{cg}} \to \ell_{\mathrm{ED}}$ (coarse-graining scale approaches substrate scale), DCGT cannot resolve substrate-graph microstructure cleanly. Substrate-level effects (kernel finite-width, V5 memory, commitment-event statistics) become visible at coarse-grained level.

**Empirical signature of breakdown:** continuum equations require substrate-level corrections that scale as $(\ell_{\mathrm{ED}}/R_{\mathrm{cg}})^n$ for some $n > 0$. Specific examples:

- Trans-Planckian regime in Hawking spectrum (Paper_039 / Paper_047 — V5 cutoff at $\omega_c = c/\ell_P$).
- Sub-Planckian length-scale probes (hypothetical future high-energy physics).
- Near-Planck-mass BH evaporation late-stage (Paper_039 §6 — remnant scale).

### 7.3 Near-singularity regimes

In regimes where substrate-level stability-landscape gradients (P12) become large enough to trigger substrate-level commitment-event proliferation, DCGT's averaging breaks down because commitment events at substrate-scale are not coarse-grain-able.

**Empirical signature of breakdown:** discrete substrate-level commitment statistics become visible in continuum measurements. Specific examples:

- Quantum-measurement events at substrate-graph scale.
- Near-horizon information-blocking transitions (Paper_039 §3 — UR-1.2 failure).

### 7.4 Strong-curvature regimes (Arc ED-10 territory)

DCGT operates in flat-spacetime (or approximately-flat) regime. Strong-curvature regimes (near singularities, near horizons at substrate scale) require the Arc ED-10 curvature-emergence framework, not DCGT directly. The relationship between DCGT and Arc ED-10 is in-queue.

---

## 8. Falsification Criteria

### 8.1 Continuum equations fail to match substrate-level predictions + procedural-unity failure

**Falsifier:** Empirical demonstration that continuum-level equations derived via DCGT (Maxwell relaxation, Newtonian potential, Hawking spectrum, Lieb–Robinson velocity) fail to match substrate-level predictions within the hydrodynamic-window scale separation — systematic discrepancies that cannot be absorbed into value-layer coefficient adjustment — would falsify DCGT. Equivalently: empirical demonstration that the four cross-domain instantiations (§6.1–§6.4) require *different* substrate→continuum procedures rather than one DCGT applied across regimes would falsify the procedural-unity claim and reduce DCGT's cross-domain wedge content.

### 8.2 Hydrodynamic-window failure or breakdown-pattern violation

**Falsifier:** Empirical demonstration that DCGT breaks down in a regime that should satisfy $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$, *or* that breakdown in strong-gradient regimes (§7.1) follows a pattern inconsistent with substrate-graph commitment-event proliferation, would falsify §3.1's scale-separation regime condition + the §7 breakdown taxonomy jointly.

### 8.3 Diffusion-form failure

**Falsifier:** Empirical demonstration that V1 coarse-graining does not produce a diffusion-type operator in the continuum limit — e.g., produces a non-local integral operator at scales $R_{\mathrm{cg}} \gg \ell_{\mathrm{ED}}$ — would falsify §4's diffusion-form derivation.

### 8.4 Memory-kernel structure failure

**Falsifier:** Empirical demonstration that V5 coarse-graining does not produce a memory-kernel operator with structure inherited from V5 envelope — e.g., that soft-matter Maxwell relaxation does not follow the predicted memory-kernel form — would falsify §5.

---

## 9. Position Statement

This paper sits within the substrate-ontology research-program lineage ('t Hooft cellular-automaton; Wolfram Ruliad / hypergraph-rewriting; causal-set program, Sorkin et al.), not within the operational-reconstruction lineage (Hardy 2001, CDP 2011, Coecke-Kissinger). Methodology per Paper_095 (form-FORCED / value-INHERITED).

The **Diffusion Coarse-Graining Theorem (DCGT)** is the substrate→continuum bridge in the ED Generative Primitives System. Given the postulated primitives + V1 inheritance + V5 dependence + the hydrodynamic-window scale separation $\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$ (regime condition), substrate-level kernel-mediated content coarse-grains to continuum diffusion-type / propagator-type / constitutive-law equations: V1 → diffusion operator (§4); V5 → memory-kernel diffusion (§5); cross-domain instantiations across soft-matter (Maxwell relaxation), QFT (propagator hierarchy), condensed-matter (Lieb–Robinson velocity), and BH (KMS-thermal structure) (§6). The procedural unity — one substrate→continuum procedure applied across multiple regimes — is the cross-domain coherence claim of DCGT. Breakdown conditions (§7) specify where substrate-level mechanism is *not* captured by continuum description (strong-gradient, near-substrate-scale, near-singularity, strong-curvature regimes); these breakdowns are predictions, not failures, and provide falsifiability handles distinguishing ED from continuum-only frameworks.

**Verdict: M3 (form-IDENTIFIED + value-INHERITED) within hydrodynamic-window scale-separation regime** per Paper_095 §3.3. Form derived via V1/V5 coarse-graining + diffusion-form emergence + memory-kernel structure + cross-domain instantiations; values inherited (Maxwell $\tau$, transport coefficients, regime-specific parameters); regime explicit (A→regime hydrodynamic-window). Five-anchor verdict-sync: status / Abstract / §1 / audit verdict row / this §9 all M3.

What this paper claims: given the postulated primitives + V1/V5 + hydrodynamic-window regime, DCGT produces continuum diffusion-type / propagator-type equations as substrate-level structural consequences; the four cross-domain instantiations are one substrate→continuum procedure applied to one substrate primitive (V5) across regimes; DCGT is load-bearing for Papers_027 (Newton), 047 (Hawking), 090 (V5 cross-domain), 056 (Class-A coarse-grained matching), and the entire Wave-3 corpus (Cos_01–Cos_06, Dyn_01–Dyn_05, GW_00–GW_02) inheriting at M3-equivalent level.

What this paper does *not* claim: the substrate primitives are not derived (Paper_087); DCGT is not the only substrate→continuum bridge; continuum-level transport coefficients are not derived but inherited; DCGT does not apply outside the hydrodynamic window; DCGT does not derive Einstein equations or standard QFT renormalization; the Lieb–Robinson identification (§6.3) is A→position dimensional-analogy framing, not substrate-graph derivation.

The empirical case rests on cross-domain reach: DCGT is load-bearing across multiple arcs; falsification in any arc traces back to DCGT or to the arc-specific application.

---

## Appendix: Cross-References

- **Paper_087:** position paper (13 substrate primitives).
- **Paper_089 (V1):** kernel inheritance.
- **Paper_090 (V5):** cross-chain kernel; primary downstream user.
- **Paper_027 (Newton's $G$):** DCGT applied to V1 cumulative-strain → continuum Newtonian potential.
- **Paper_047 (Hawking Spectrum):** DCGT applied to V5 substrate KMS → semiclassical thermal spectrum.
- **Paper_095:** verdict grammar (M1/M2/M3 tiers; A→regime + A→position labels).
- **Wave-3 corpus inheritance:** Cos_01–Cos_06, Dyn_01–Dyn_05, GW_00–GW_02 all inherit DCGT as the substrate→continuum bridge at M3-equivalent level (per the "M3 via continuum-Friedmann inheritance" pattern in Cos_02 / Cos_03 / Cos_04 specifically).

---

**End of Paper_073.**

*Wave-2 Generative Paper — Soft-Matter Arc / Cross-Domain Bridge Foundation. Canonical reference for the substrate→continuum coarse-graining procedure used across ED arcs.*
