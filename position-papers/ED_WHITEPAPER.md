# Event Density

## A Generative Substrate Ontology for Cross-Scale Physics

**Whitepaper — Program Overview, Architecture, and Falsification Path**

*Wave-3 generative document. Public-facing, non-technical orientation layer. Standalone, citable, repo-top-level document.*

---

## Executive Summary

**Event Density (ED)** is a research program that asks a single foundational question: *can the diverse phenomena of physics — quantum mechanics, gauge theory, gravity, black holes, turbulence, decoherence, entanglement — be generated from a small, well-specified substrate ontology?*

The program's answer is conditional: **yes, given thirteen posited primitives and a kernel calculus built from two substrate-level memory kernels**. The thirteen primitives are listed in a position paper and form a minimal generative ontology. The two kernels — designated V1 (a finite-width retarded kernel) and V5 (a finite-memory cross-chain correlation kernel) — supply the dynamical content from which physical structure is derived.

The substrate→continuum bridge used across every continuum-level result in the corpus is the **Diffusion Coarse-Graining Theorem** (DCGT, Paper_073), at verdict tier **M3 within an A→regime hydrodynamic-window scale-separation assumption** ($\ell_{\mathrm{ED}} \ll R_{\mathrm{cg}} \ll L_{\mathrm{flow}}$). Continuum equation forms (diffusion operator, propagator hierarchy, memory-kernel, KMS-thermal) are FORM-FORCED from substrate kernel structure (V1, V5) and substrate-graph averaging; numerical transport coefficients (diffusion constant, Maxwell relaxation time, etc.) are VALUE-INHERITED via empirical matching; one cross-domain instantiation (Lieb–Robinson velocity bound) carries an A→dimensional-analogy label rather than full derivation; explicit breakdown conditions (strong-gradient, near-substrate-scale, near-singularity, strong-curvature regimes) are predicted, not papered over. Because DCGT is upstream of every continuum-level result, its M3-with-regime-caveat status is inherited by every downstream continuum prediction.

What ED claims is *cross-domain reach plus methodological consistency*. Across eight **structurally complete research arcs with declared open derivations** (quantum kinematics, form-level quantum field theory, gravity, black holes, quantum computing limits, entanglement, soft matter / Navier–Stokes, foundational kernel theory), ED produces results that are **form-forced** by the primitives and an honestly-disclosed set of paper-specific postulates. Numerical values are inherited from empirical matching rather than derived from first principles. This split — *form forced, values inherited* — is the program's methodological signature. "Structurally complete" means each arc has an integrated framework with explicit falsification criteria and a registry of what is form-FORCED, value-INHERITED, or OPEN; it does **not** mean each arc contains no open derivations. Open derivations are named (Route A, Phase-3 GR, YM mass-gap mechanism, NS smoothness at Intermediate Path C) rather than hidden.

The program's most ambitious recent synthesis is the **Substrate–Cosmology Boundary Unification (SCBU)** and its six-paper extension arc, the **ED-SC 4.x series**. SCBU is offered as the framework's **organizing structural claim**: that the black-hole horizon, the cosmic decoupling surface, the deep-MOND galactic asymptote, the quantum-computing platform-coherence threshold, the soft-matter hydrodynamic Q-factor, and the substrate-scale fixed-point parameter are projections of a single substrate–cosmology boundary onto distinct parameter axes. ED-SC 4.x organizes these projections within a unified four-regime cross-scale model (ultraviolet / transition / infrared / cosmological).

**Honest framing of SCBU's current status (post-2026-05-17 Route A closure).** SCBU is now an **M3-supported structural claim at substrate-parameter-INHERITED level** (Paper_027-analog). Route A — substrate-derived $\ell_{V_5}(H_0)$ relating V5 bandwidth to the cosmological rate — **closed at substrate-parameter-INHERITED level** via the Route A audit cascade (multi-route convergence audit option (ii); closure documented in Paper_ED_SC_4.2 §1.5). The closure delivers $H_0 = (8\pi/3)^{1/2} \ell_P c^{1/2} \Theta_{\mathrm{ED}}^{1/2}$ with $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ substrate-parameter-INHERITED at P12 primitive level (analogous to Paper_027's inheritance of $\ell_P, \hbar, c$). Cross-arc consequences: **Cosmology Arc M3 Trinity** (Cos_01 + Cos_05 + Paper_038_5 all at M3 via the same Q1A + Q2A + C3 + IC-INHERITED chain + Route A4 substrate-parameter-INHERITED closure); **ED-SC 4.x arc-wide M3 upgrade** across all six projections. The six-projection picture is now a substrate-graph-derived structural claim at substrate-parameter-INHERITED level. Tightening work — per-projection exponent derivation; substrate-graph derivation of $\Theta_{\mathrm{ED}}$ + $\tau_{V_5}$ values from sub-primitive content (analog of longstanding "what determines $\ell_P, \hbar, c$ values?") — remains as substrate-research-frontier work, **not load-bearing** for the M3 verdicts.

**The post-pivot gravity line and the substrate-evaluation wave (June 2026).** Two developments postdate the eight-arc structure. A six-paper **gravity line** (GR-I … GR-IV, KM-I/II, the One-Field capstone) derives — from the substrate's irreversible arrow placed *in the law* — the weak-field Einstein metric with its **factor-of-two light bending**, the **khronometric** gravitational class (GW-clean, Lorentz-safe), the preferred-frame parameter $\alpha_1$ **suppressed below the experimental bounds by more than 70 orders of magnitude**, and the MOND / dark-energy phenomenology, unified as *one field with one scale* (the full nonlinear Einstein equation remains open). Separately, a **substrate-evaluation wave** reports *build-and-run* results from the certified rule — including the program's only *proven* negative (the finite-memory prime ceiling) and its reach statement, *Form and Flesh: The Two Walls.* Both are developed in §5.

The program is **falsifiable**. Each result carries explicit falsification criteria. The SCBU framework predicts synchronized co-variation of the six projections under Hubble-tension-class shifts of $H_0$; with Route A now closed at substrate-parameter-INHERITED level, **per-projection scaling exponents are derivable in principle via the Route A inheritance chain** (a tightening-work direction, not a load-bearing OPEN). $a_0 \propto H_0^1$ is structural (Paper 029); $R_H \propto H_0^{-1}$ is structural (Paper 028); $\xi_{\mathrm{canonical}} \propto H_0$ at leading order via Route A4; the remaining per-projection exponents ($\mathcal{M}_{\mathrm{crit}}, Q$) sharpen with per-projection derivation work. The sharpest currently-clean falsifier in the corpus remains the **BTFR slope-4 with zero intrinsic scatter** (Paper 031), testable against galaxy-rotation-curve catalogs at present precision.

This whitepaper is the front door. It explains what ED is, what it claims, what it does not claim, and how to navigate the 100+ research papers that constitute the program (the numbered Paper_NNN series plus theorem-stub additions T19–T21, the cross-arc synthesis Paper_SCBU, and the six-paper ED-SC 4.x extension arc).

---

## §1 — Motivation

Physics, considered as a single intellectual artifact, is a patchwork. Quantum mechanics and general relativity remain unreconciled in their foundations. Standard-model gauge theory works at one scale; cosmological dynamics works at another. The black-hole information paradox lives in a third register; turbulence and condensed-matter rheology in a fourth. Each domain has its own framework, its own postulates, and its own community.

A generative substrate ontology proposes an alternative architecture: *rather than treating each domain as autonomous, derive each domain's structural content from a common substrate*. The substrate is posited, not derived. From the substrate, dynamical kernels are built. From the kernels, coarse-grained continuum theories emerge. From the continuum theories, specific physical predictions follow.

ED's intellectual neighborhood is the **substrate-ontology research program**: 't Hooft's cellular-automaton interpretation of QM, Wolfram's Ruliad / hypergraph-rewriting program, and the causal-set program (Sorkin et al.). These are programs that posit substrate ontologies and exhibit downstream physics; they are not axiomatic reconstructions in the sense of Hardy (2001), CDP (2011), or Masanes-Müller (2011), where finite-dimensional QM is derived from operational axioms by closed proofs. ED should be read against the substrate-ontology lineage, not against the operational-reconstruction lineage. The methodological discipline ED adds to its lineage is the form-FORCED / value-INHERITED split (Paper 095) and per-paper audit tables with explicit P/D/A/I labels — improvements on the field's norm, not equivalents of closed-proof reconstructions.

The motivation for ED is not that the patchwork is wrong — each domain's predictions are excellent within their regimes — but that the patchwork may hide **cross-domain structure**. If a single substrate-level object underlies phenomena across the black-hole horizon, the cosmic decoupling surface, the substrate-scale fixed-point, the deep-MOND galactic acceleration, the matter-wave quantum-classical boundary, *and* the Navier–Stokes Q-factor, the cross-domain structure would itself be a physical fact worth identifying. SCBU (§7) offers this as a six-projection picture of a single substrate-cosmology boundary; **post-2026-05-17 Route A closure, the picture is M3-supported at substrate-parameter-INHERITED level** (see Cosmology Arc M3 trinity + ED-SC 4.x arc-wide M3 upgrade per the Route A closure documented in Paper_ED_SC_4.2 §1.5). The program is honest about this status throughout, including the substrate-parameter-INHERITED status of $\Theta_{\mathrm{ED}}$ and $\tau_{V_5}$ (analogous to Paper_027's inheritance of $\ell_P, \hbar, c$).

ED's role is to make this cross-domain structure explicit, falsifiable, and structurally honest. The program does not replace standard physics operationally; it supplements it with a substrate-level account of why the standard results take the forms they do.

---

## §2 — The 13 Primitives

ED's substrate is specified by thirteen primitives. They are **posited** — not derived from anything deeper. The enumeration below is the canonical list per `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` and the audit document `primitives/PRIMITIVE_LOAD_BEARING_AUDIT.md`; downstream papers reference these P-numbers.

A note on minimality. The 13 are claimed *necessary-for-current-derivations* (removing any one blocks at least one downstream derivation, audited in `PRIMITIVE_LOAD_BEARING_AUDIT.md`). They are **not** claimed minimal in an absolute sense: smaller primitive sets generating the same downstream content may exist. We do not claim otherwise. P03 in particular bundles channel indexing, locus indexing, and spatial homogeneity; this is a working consolidation, not a forced reduction. The arrow of time is supplied jointly by P11 + P13 + V1's retardation property (Theorem T18), and the redundancy question among these three is structurally open.

The thirteen primitives, in plain language:

**P01 — Event-density layer existence.** A pre-quantum substrate exists as a primitive structural layer. The substrate is not a Hilbert space, not a smooth manifold, not a field theory — it is a discrete graph-like structure equipped with primitive scalar, relational, and angular quantities. P01 is the foundational ontological-existence commitment that grounds every paper in the program.

**P02 — Participation as primitive relation.** Chains (persistent micro-event sequences) participate in channels as a primitive substrate-level relation. Participation is the substrate's mechanism for chain-channel interaction; without P02 no participation measure can be defined.

**P03 — Channel + locus indexing; spatial homogeneity.** The substrate supplies a discrete index set of channels $\mathcal{K}$ and a (discrete or continuous) index set of loci, with primitive translation-invariance: shifting all loci by a common displacement leaves the participation-graph adjacency structure intact. This primitive bundles three commitments (channel index, locus index, spatial homogeneity); they could in principle be split.

**P04 — Bandwidth (non-negative additive scalar, four-band partition).** Each channel $K$ at each locus $u$ carries a real-valued non-negative quantity $b_K(u) \geq 0$, additive under channel decomposition. Bandwidth further decomposes into four mutually orthogonal substrate-level bands: internal, adjacency, environmental, commitment-reserve.

**P05 — Polarity-transport between adjacent loci.** The substrate-level connection structure — the mechanism by which polarity at one locus is transported to a neighboring locus along edges of the participation graph. P05 is the substrate-level origin of phase, gauge connection, and parallel-transport phenomena.

**P06 — Spatial dimension $D = 3+1$.** The substrate's spatial axis is $\mathbb{R}^3$, plus one time dimension. Consistent with multiple independent derivations elsewhere in the corpus (PDE-uniqueness axioms, spinor-bundle structure, acoustic-metric signature).

**P07 — Channel structure as ontological primitive.** Channels are structurally distinguishable carriers of substrate content, with identities intrinsic to the participation graph rather than derived from external organizational choice.

**P08 — Substrate scale $\ell_{\mathrm{ED}}$.** The substrate has a characteristic edge length $\ell_{\mathrm{ED}}$. **The identification $\ell_{\mathrm{ED}} \equiv \ell_P$ (the Planck length) is a value-inheritance step**, fixed by Newton-recovery: matching the substrate-derived form $G = c^3 \ell_{\mathrm{ED}}^2/\hbar$ to the empirical value of Newton's constant determines $\ell_{\mathrm{ED}}$ to be $\ell_P$. This is not a first-principles derivation of $G$'s numerical value; it is the substrate-side identification of the length-scale anchor (see §3 + §7 for honest framing).

**P09 — $U(1)$-valued polarity.** Each channel carries an angular variable $\pi_K(u) \in U(1) \cong S^1$, the substrate's unique angular primitive. Supplies the angular / phase structure that propagates to gauge fields and quantum phase.

**P10 — Rule-type primitive.** The substrate supports multiple structurally distinct rule-types $\tau_\bullet$, each with its own participation measure. Matter and gauge are *different rule-types*, not different states of the same one. The V1 and V5 kernels (see §3) are rule-types.

**P11 — Commitment with environmental phase-randomization, irreversible.** Discrete substrate-level events at which a chain's multi-channel participation collapses to a single channel, with phase-randomization on a uniform $U(1)$ distribution. Commitment is irreversible — no substrate-level dynamics maps a post-commitment state back to its pre-commitment superposition. P11 supplies the directional content of time and the retardation property of the V1 kernel.

**P12 — Stability landscape.** Substrate-level functional $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$ whose extrema govern chain dynamics. Carries the substrate-level coherence, strain, and gradient content for gravitational physics.

**P13 — Time homogeneity; primitive event-discreteness.** The substrate's dynamical primitive is invariant under time translation; the substrate has no preferred absolute time origin. Events on the substrate are primitively discrete (the manifold is not infinitely refinable). P13 supplies $H_0$ as a cosmological-rate parameter.

A fourteenth slot, **P14**, is reserved as a placeholder for bilocal strain coupling. P14 is *not* currently in the canonical 13; its presence as a reserved slot indicates that the count is the working consolidation, not a load-bearing claim. Whether P14 should be elevated, or whether its content can be derived from the existing 13, is structurally open.

**Relationship to the `primitives/` directory.** The `primitives/` directory is now organized in two tiers:
- **Top-level files `P01_*.md` through `P13_*.md`** — the canonical primitive reference cards. These match the enumeration above 1-to-1; downstream papers cite them by P-number.
- **`primitives/concepts/` subdirectory** — thirteen process-level treatments of the *underlying ontological concepts* the canonical primitives organize (micro-event, chain, participation, participation_bandwidth, event_density, ed_gradient, channel, multiplicity, tension_polarity, individuation, commitment, thickening, relational_timing). The mapping to canonical primitives is *not 1-to-1*: chains and individuation are derived rather than canonical-primitive; micro-event and event-density jointly contribute to P01; P05 polarity-transport and P06 spatial dimension have no concept-file counterpart.

See `primitives/README.md` for the full two-tier structure and citation convention.

The thirteen primitives are **the** ontological commitment of the ED program. Every result in the corpus rests on them — though as noted, "minimal" means *necessary-for-current-derivations*, not *absolutely minimal*.

---

## §3 — Kernel Calculus (V1 / V5)

ED's substrate dynamics are carried by two substrate kernel rule-types (in the sense of P10). Both are finite — neither requires infinite-resolution data — and both are forward-causal under P11.

**V1 — Finite-width retarded vacuum kernel.** V1 propagates substrate amplitudes from prior to later times with a characteristic width $\ell_{V1} \sim \ell_P$ and a retardation property forced by P11. V1 supplies:

- The substrate-level propagator entering quantum field theory.
- The UV regulator at the Planck scale (preventing trans-Planckian divergences).
- The kinematic viscosity scale entering hydrodynamics ($\nu \sim \ell_{V1}^2 / \tau_{V1}$).
- The friction coefficient entering the Universal Mobility Law.
- The propagation rate identified as substrate $c$ (constant under coarse-graining).

**V5 — Cross-chain finite-memory correlation kernel.** V5 supplies cross-chain correlations with finite bandwidth $\ell_{V5}$ and finite memory $\tau_{V5}$. V5 carries the cross-chain content that V1 (within-chain) does not. V5 supplies:

- Maxwell-form stress-relaxation in viscoelastic materials ($\tau_M \sim \tau_{V5}$).
- The substrate origin of bipartite entanglement budget partitioning (monogamy).
- The cross-chain bandwidth that caps Q-Compute multiplicity.
- The decoupling-surface mechanism at black-hole horizons ($\Gamma_{\mathrm{cross}} \to 0$).
- The Page-curve mechanism for Hawking radiation entanglement.
- The cutoff $\omega_c = c/\ell_P$ resolving the trans-Planckian problem.

The two kernels together form a **kernel calculus**: a small, complete set of substrate-level objects from which coarse-grained continuum theories emerge under the Diffusion Coarse-Graining Theorem (DCGT).

**Why only two kernels?** A central structural claim of ED is that V1 + V5 are sufficient. Higher-order kernels are admissible in principle but, across all current research arcs, V1 and V5 suffice. The same V5 **rule-type** appears with structurally identical roles in soft-matter viscoelasticity, black-hole horizon physics, Hawking-radiation cutoff, entanglement-bandwidth modulation, and Q-Compute platform-coherence saturation — six domains, one substrate rule-type, no contradiction.

**Honest framing of the cross-domain claim.** Whether V5 is the *same kernel* (with parameters substrate-derived from a single substrate-cosmology coupling) or the *same rule-type* (with parameters domain-set by separate empirical matching in each arc) is the load-bearing distinction. The first interpretation requires Route A in Paper ED-SC 4.2 (substrate-derived $\ell_{V5}(H_0)$) to close. **As of 2026-05-17 Route A is closed at substrate-parameter-INHERITED level (Paper_027-analog)** — $H_0 = (8\pi/3)^{1/2}\ell_P c^{1/2}\Theta_{\mathrm{ED}}^{1/2}$, with $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ inherited at the P12 primitive level — so the V5 cross-domain pattern is now "one kernel at substrate-parameter-INHERITED level," not merely "one rule-type with un-derived parameter relations." This is the same tier of closure Paper_027 gives Newton's $G$ (form derived; value inherited via one substrate parameter); it is **not** a from-sub-primitives derivation of $\Theta_{\mathrm{ED}}$ itself, which remains substrate-research-frontier (Routes B/C, the M1 upgrade). Consistent with §7 (SCBU) and §8 (ED-SC 4.x).

---

## §4 — The ED Architecture

The ED program has a four-layer architecture:

**Layer 1 — Substrate primitives (P01–P13).** Posited ontology. The thirteen primitives.

**Layer 2 — Kernel calculus (V1 / V5).** Substrate dynamics. The two kernels, classified by characteristic scale, retardation order, and cross-chain rank.

**Layer 3 — Domain arcs.** Closed research arcs deriving specific physical structures from primitives + kernels + paper-specific postulates. Each arc is structurally coherent within itself and integrated with the substrate.

**Layer 4 — Cross-scale synthesis.** The Scale Correspondence (SC) program and SCBU unification, integrating multiple arcs into a unified cross-scale invariance model.

Conceptually:

```
                  ┌─────────────────────────────────┐
                  │  Layer 1: 13 Primitives (P01–P13) │
                  └───────────────┬─────────────────┘
                                  │
                  ┌───────────────▼─────────────────┐
                  │  Layer 2: Kernel Calculus (V1, V5) │
                  └───────────────┬─────────────────┘
                                  │
        ┌────────────────────┬────┴────┬──────────────────┐
        │                    │         │                  │
   ┌────▼────┐         ┌─────▼───┐  ┌──▼────┐      ┌──────▼──────┐
   │ QM Arc  │         │ QFT Arc │  │ Gravity│ ...   │  Soft Matter │
   │  Phase-1│         │ T17/T18 │  │ Arc    │      │  / NS-MHD   │
   └────┬────┘         └────┬────┘  └──┬────┘      └──────┬──────┘
        │                   │           │                   │
        └─────────┬─────────┴─────┬─────┴─────────┬─────────┘
                  │               │               │
                  ▼               ▼               ▼
            ┌─────────────────────────────────────────┐
            │   Layer 4: Cross-Scale Synthesis (SC, SCBU) │
            └─────────────────────────────────────────┘
```

The architecture is **bottom-up**: every result in Layers 3 and 4 traces back through the kernel calculus to the substrate primitives. The architecture is also **falsifiable at each layer**: refutation of a primitive falsifies downstream results; refutation of a kernel-level claim falsifies dependent arc results; refutation of an arc result limits but does not destroy the substrate.

This layered falsifiability is the program's structural integrity.

---

## §5 — The Domain Arcs

The ED corpus is organized into eight **structurally complete research arcs with declared open derivations**. Each arc:

- States its substrate-level inputs explicitly.
- Identifies its paper-specific postulates (declared, not derived).
- Derives or composes its structural content.
- Distinguishes form-forced content from value-inherited content.
- Provides explicit falsification criteria.

The eight arcs:

**Quantum Kinematics (Papers 001–012).** The Phase-1 program. Sixteen theorems closing the four standard quantum-mechanical postulates as substrate-derived results. Born rule, tensor-product structure, projective measurement, unitary evolution: all derived from substrate primitives. Berry phase, Aharonov–Bohm phase, Bloch theorem, local rate of becoming.

**Quantum Field Theory (Papers 013–024).** Form-level QFT scaffolding. T17 identifies gauge fields as connections on rule-type bundles. T18 establishes the kernel-level arrow of time. The Yang–Mills arc (YM-1 through YM-6) supplies substrate-level non-abelian gauge theory, an OS-positivity audit, and a mass-gap mechanism. **Verdict register, honestly: a substrate-level mass-gap mechanism is identified, with explicit paper-specific postulates declared (P-Gap-Coercivity, P-Profile-Rescaling, P-Quartic-Sign). A closed-proof reduction to the Clay-problem mass-gap statement is *not* claimed.** Per Paper_095 methodology, the verdict tier is M2 (Intermediate Path C): structural mechanism identified, postulates declared, constructive proof OPEN.

**Gravity (Papers 025–038).** Substrate-level identifications of Newton's law structural form ($G = c^3 \ell_{\mathrm{ED}}^2 / \hbar$, with $\ell_{\mathrm{ED}}$ fixed to the Planck length $\ell_P$ by **Newton-recovery — a value-inheritance step, not a first-principles derivation of $G$**); the transition acceleration $a_0 = c H_0 / (2\pi)$ as a structural projection of the cosmic decoupling surface; the ED Combination Rule $a = \sqrt{a_N a_0}$; and the BTFR slope-4 relation $v^4 = G M a_0$. The **BTFR slope-4 with zero intrinsic scatter in deep-MOND** is the gravity arc's sharpest near-term falsifier; current SPARC-class data (McGaugh-Lelli-Schombert 2016: 175 galaxies, slope $3.95 \pm 0.08$, scatter $\sim 0.1$ dex) is consistent at the deep-MOND asymptotic level, with the residual scatter likely observational rather than intrinsic. Arc ED-10 extends to scalar-tensor acoustic-metric covariantization. The **post-pivot curvature-emergence line** (GR-I … GR-IV, KM-I/II, One-Field — see the dedicated subsection below) sharpens this Arc-3 content into the weak-field Einstein metric, the khronometric class, and the preferred-frame closure.

**Honest scope of the "no dark matter" claim.** Substrate gravity explains **the deep-MOND asymptotic** without dark matter: the BTFR slope-4 result with the empirically-consistent $a_0 = cH_0/(2\pi)$ is the load-bearing demonstration. The **transition regime** ($a \sim a_0$, intermediate-acceleration galactic radii) is *predicted* by the ECR $a \approx a_N + a_0 + \sqrt{a_N a_0}$ (Paper_030), but **the corpus does not currently contain explicit per-galaxy SPARC-class residual fits across the transition radius** — those would be the natural next empirical-test program target. The "explains galactic dynamics without dark matter" claim is therefore qualified: *the deep-MOND endpoint is empirically accounted for and the transition regime is structurally predicted; explicit transition-regime residual fits are part of the ongoing empirical-test program (Paper_101 §3.3 register)*. The Whitepaper does not claim the corpus has *already performed* a SPARC-class transition-regime fit; it claims the ECR predicts the transition-regime behavior and BTFR is consistent at the asymptotic endpoint.

**Black Holes (Papers 039–052).** The Arc Hawking program. Horizon as decoupling surface ($\Gamma_{\mathrm{cross}} \to 0$). Hawking spectrum at $T_H = \kappa/(2\pi)$ via substrate-Unruh / KMS. Trans-Planckian problem resolved by V5 cutoff at $\omega_c = c/\ell_P$. Planck-mass remnant ($M_\star = c_\star \ell_P$) as forced endpoint (Scenario C). Information paradox not generated at substrate level. Important framing: Planck-mass remnants are **not** a dark-matter candidate — galactic dynamics are explained by substrate gravity, not remnants.

**Q-Compute (Papers 053–062).** The substrate origin of quantum-computing limits. The multiplicity-cap function $\mathcal{M}_{\mathrm{cap}}$ as one substrate object with three projections (Class A engineered-low-multiplicity, Class B global-geometric-rigidity, Class C high-multiplicity-redundancy). Cross-platform unification via critical multiplicity $\mathcal{M}_{\mathrm{crit}}$: matter-wave quantum-classical boundary (140–250 kDa) and qubit-array walls are the same substrate phenomenon. Decoherence-centric → multiplicity-centric reframing.

**Entanglement (Papers 063–072).** Bipartite entanglement architecture substrate-derived. Tensor product, Schmidt decomposition, monogamy (via V5 cross-chain bandwidth), no-signaling (over-determined by three substrate locks), von Neumann entropy via Shannon–Khinchin axioms at substrate level, Bell–Tsirelson polytope. Interpretive capstone: entanglement is the unresolved regime of participation-rule individuation.

**Soft Matter / Navier–Stokes (Papers 073–086).** The substrate-level NS / MHD program. Paper_073 (DCGT) at verdict tier **M3 within A→regime hydrodynamic-window** supplies the substrate→continuum bridge (see §1 framing); the remaining arc papers apply DCGT to specific substrate-content. NS-1 dimensional forcing to $D = 3+1$. NS-2 substrate→continuum coarse-graining. NS-Smoothness at **M2 (Intermediate Path C)** verdict (mass-gap-class structural-positive; closed proof OPEN). NS-MHD H1/H2/H3 closure. Krieger–Dougherty + Maxwell viscoelastic. Canonical NS-Q operating point with $Q \approx 3.5$. Universal Mobility Law. Vortex-stretching obstruction at substrate level.

**Wedges / Kernel Theory (Papers 087–101).** Foundational substrate-level theorems. The 13-primitive position paper (Paper 087). V1 and V5 canonical references. Memory-kernel cascade across scales. Kernel hierarchy unification. T18 kernel-level arrow of time. Forward-causal primitive structure. Form-FORCED / value-INHERITED methodology formalized. Cross-scale invariance (ED-SC 3.x). Three-regime renormalization-group / 0.6 problem. NS synthesis. Five-sector program overview. Falsification register.

Each arc is a complete research program in its own right. Each composes with the others through the substrate primitives and the kernel calculus.

### Post-Pivot Gravity Line and the Substrate-Evaluation Wave (June 2026)

Two developments postdate the eight-arc numbered structure above and use a distinct naming convention (no numbered slots consumed).

**The post-pivot gravity line (curvature emergence).** Sharpening — not superseding — the Arc-3 scalar-tensor / MOND papers, a six-paper line derives gravity from the substrate's irreversible arrow placed *in the law*:

- **GR-I (*The Bandwidth Lapse and the Factor of Two*).** The substrate bandwidth field supplies an emergent metric ($g \sim 1/b$) and, with the commitment-rate law, the temporal lapse ($N^2 \sim b$) — yielding the weak-field Einstein metric, the Schwarzschild relation, the three classical tests, and the **factor-of-two light bending** (ray-traced 2.09 vs predicted 2.00, conformal control at 0) — the historical discriminator that killed scalar gravity.
- **GR-II (*The Arrow's Fingerprint*).** The gravitational class is **khronometric** — Einstein plus exactly one scalar, the arrow made dynamical — with one causal cone, so $c_T = c$ structurally (the GW170817 constraint as identity) and Lorentz violation universal rather than species-dependent (invisible to the $10^{-20}$ matter-sector bounds).
- **GR-III (*The Arrow's Engine*).** The dynamical rule (the commitment-rate law) and the closure of GR-I's labeled weak-field assumptions.
- **GR-IV (*The Arrow's Alibi*).** The preferred-frame parameter computed — $\alpha_1 = -4\lambda_{\mathrm{local}}$, $\lambda_{\mathrm{local}} \sim \rho_{\mathrm{event}}/\rho_{\mathrm{Planck}}$ — and **suppressed below the bounds by more than 70 orders of magnitude** because commitment is sparse (forced by the quantum sector: dense commitment is the Zeno limit, which would abolish quantum mechanics). The preferred-frame front — long the most likely killer of any theory of this class — is closed favorably, and remains a live test ($\alpha_1 \gtrsim 10^{-5}$ in any sub-Planck environment kills it).
- **KM-I / KM-II (*The Arrow's Deep Field / The Arrow's Horizon*).** The MOND phenomenology as the khronon's deep-infrared regime (lensing-correct, no added vector field, solar-system screened), and the cosmological sector (dust-clustering dial, one $\Lambda$).
- **One-Field (capstone letter).** Gravity, dark matter, dark energy, and the arrow as one field with one scale — *five roles, three ways to kill it, one number to miss.*

Verdict register: the weak-field Einstein metric, the khronometric class, and the $\alpha_1$ suppression are **derived / identified**; the full **nonlinear** Einstein field equation remains open (Phase-3 GR locates the obstruction but does not cross it — §11).

**The substrate-evaluation wave (build-and-run, could-say-no tests).** A distinct register: results obtained by *running* the certified substrate rule and reporting what it does — including where it says *no*.

- **A1 — Common Cause, Not Channel.** Controlled channel capacity across the determinability boundary is *exactly zero*; the boundary is an observational common-cause structure, not a transmission channel.
- **B4 — Charge as Topology.** Electric charge as quantized winding with an integral Gauss law — the topological *skeleton* of charge realized, the metrical *flesh* (the determined Coulomb field) withheld by construction.
- **The Continuum is a Kinetic Lattice-Gas, not a PDE.** The certified substrate's continuum limit is a ballistic lattice-gas; a closed diffusion PDE appears only when the substrate's own arrow-selection ($\Sigma$) is deleted — "you reach the PDE only by leaving ED."
- **Primes — the Finite-Memory Ceiling.** Finite-memory ED reproduces the prime *template* (~1.700 bits, exact, scale-invariant) but provably **cannot** produce the *escape* layer (primality / the parity barrier). The program's only *proven* negative.
- **Form and Flesh — The Two Walls.** The reach statement: Wall 1 (coarse-graining — the continuum shadow, mostly open) and Wall 2 (finite-memory — proven, the prime ceiling). What ED supplies is *form*; what it withholds is *flesh*; the non-transfer between the walls is load-bearing.

This register is the program's strongest honesty credential: a substrate that is *run*, not merely argued, and that is explicit about its own edges. (A recent cosmology addition, Paper_ED_CCC, identifies the structure of Penrose's Conformal Cyclic Cosmology within the substrate and supplies two premises CCC assumes.)

---

## §6 — Scale Correspondence (SC) Program

The Scale Correspondence (SC) program is ED's account of how substrate-level structure manifests at the scales accessible to physical experiment.

**Why SC is needed.** The substrate operates at the Planck scale ($\ell_P \sim 10^{-35}$ m). Physical experiments operate at scales from atomic to cosmological. The gap is sixty-plus orders of magnitude. For ED's substrate to make contact with physics, a *scale correspondence* between substrate content and experimentally-accessible content must be identified.

**SC versus Wedges/RG.** The Wedges arc (Papers 087–097) establishes the substrate's renormalization-group structure: three regimes (ultraviolet / transition / infrared) with characteristic 0.6 transition exponent, cross-scale invariance at the canonical operating point $\xi_{\mathrm{canonical}}$, and the kernel cascade across scales. This is the **internal substrate-side** structure of cross-scale relations.

The SC program is the **external** counterpart: how does substrate-level structure project onto physically-observable scales? Where do the experimental signatures live? Why does $a_0$ have the value it has? Why does the matter-wave quantum-classical boundary sit at 140–250 kDa?

**Role of SCBU.** The Substrate–Cosmology Boundary Unification supplies the central anchor for the SC program. By identifying the substrate-cosmology boundary as a single shared object whose multiple projections supply the canonical scales of physics, SCBU provides the substrate-level *reason* why specific empirical scales exist where they do.

---

## §7 — SCBU: Substrate–Cosmology Boundary Unification

**What SCBU claims, with honest scope (post-2026-05-17 Route A closure).** SCBU is **M3-supported structural claim at substrate-parameter-INHERITED level**: the substrate-cosmology boundary at $R_H = c / H_0$ — where V5 cross-chain bandwidth saturates — is a single substrate-level object, derived substrate-graph at substrate-parameter-INHERITED level (Paper_027-analog) via the Route A audit cascade. Multiple physical quantities at different domains are projections of this single object onto different parameter axes, now M3-supported by the Cosmology Arc M3 trinity + ED-SC 4.x arc-wide upgrade.

Route A4 delivers the derivation that previously stood as the open question: a substrate-derived $\ell_{V5}(H_0)$ relation between V5 bandwidth and the cosmological rate, closed at substrate-parameter-INHERITED level. $H_0 = (8\pi/3)^{1/2} \ell_P c^{1/2} \Theta_{\mathrm{ED}}^{1/2}$ with $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ inherited at P12 primitive level. **This closure is CONDITIONAL** on the $\tau_{V_5} \to \Theta_{\mathrm{ED}}$ reduction (audit axis A-A4-4), which `Memo_ED_RouteA_A4_Audit` flags as **load-bearing for full closure and not proved**; and even when granted, $\Theta_{\mathrm{ED}}$ itself is *inherited*, not derived. First-principles (M2) closure — deriving $\Theta_{\mathrm{ED}}$ from sub-primitives — remains OPEN. The V5 kernel performs structurally identical *jobs* across domains (Maxwell relaxation at $\tau_M \sim 10^{-3}$ s in soft-matter, cutoff $\omega_c = c/\ell_P$ in Hawking, entanglement-bandwidth modulation, Q-Compute multiplicity cap, NS-Q dissipation, BH decoupling) — and per the Route A closure, these jobs are now M3-supported as performed by *the same* kernel with parameters substrate-graph-derived at substrate-parameter-INHERITED level. The "same kernel vs same rule-type" load-bearing distinction is now closed in favor of "same kernel at substrate-parameter-INHERITED level"; the honest framing in §1 reflects this.

The six projections identified in the corpus (counting Paper_ED_SC_4.1's two parameter-axis arms — $r_H$ at local-gravitational mass and $R_H$ at global cosmological rate — as two separate projections):

| Projection | Parameter axis | Substrate identity |
|---|---|---|
| Black-hole horizon $r_H = 2GM/c^2$ | local gravitational mass $M$ | cosmological-regime, local-grav arm |
| Cosmic decoupling $R_H = c/H_0$ | global cosmological rate $H_0$ | cosmological-regime, global arm |
| Substrate fixed-point $\xi_{\mathrm{canonical}}$ | substrate-scale fixed-point | spans IR-to-cosmological |
| Deep-MOND acceleration $a_0 = c H_0/(2\pi)$ | local galactic acceleration | IR-galactic projection |
| Q-Compute threshold $\mathcal{M}_{\mathrm{crit}}$ | multiplicity-budget | IR-platform projection |
| NS-Q canonical $Q \approx 3.5$ | hydrodynamic Q-factor | IR-hydrodynamic projection |

The cosmological regime (regime 4) carries two arms; the IR regime (regime 3) hosts three sub-projection manifestations. Together these form the canonical six-projection view of the unified four-regime SCBU model (per Paper_ED_SC_4.6).

**Why SCBU is offered.** Each of these quantities was, prior to SCBU, an independent feature: $a_0$ derived in the gravity arc, $\mathcal{M}_{\mathrm{crit}}$ in the Q-Compute arc, $Q$ in the soft-matter arc. They share a striking common feature: each is structurally anchored to the cosmological rate $H_0$ through the substrate-cosmology boundary, even though each lives in a domain (galactic dynamics / quantum-computing / hydrodynamics) that has no operational connection to cosmology. SCBU proposes that this is not coincidence: that from the substrate's perspective, these are the same boundary observed via different projection mechanisms.

**What SCBU does not yet do.** SCBU does not currently derive the specific scaling exponents per projection axis. "Co-varies with $H_0$" admits many functional forms. The prediction sharpens dramatically if SCBU forces specific exponents (e.g., $a_0 \propto H_0^1$ — already structural in Paper_029 — but $\mathcal{M}_{\mathrm{crit}} \propto H_0^\alpha$ with $\alpha$ fixed by substrate structure has not been derived). Until per-projection exponents are fixed, the synchronized-covariation prediction is a *family of falsifiers* indexed by free exponents, rather than a single sharp falsifier with no degrees of freedom. The §9 falsification register reflects this: BTFR slope-4 (Paper 031) is the corpus's sharpest empirically-clean falsifier; SCBU's covariation prediction is its most structurally far-reaching falsifier but currently softer.

**The structural claim, honestly framed:** *one substrate, one boundary, six projections — M3 structural claim at substrate-parameter-INHERITED level (Paper_027-analog), conditional.* The substrate-cosmology coupling (Route A) closes at substrate-parameter-INHERITED level via the A4 chain **only conditionally**: the $\tau_{V_5} \to \Theta_{\mathrm{ED}}$ reduction (A-A4-4) is load-bearing per `Memo_ED_RouteA_A4_Audit` and is **not proved**, and $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ is *inherited* at P12 primitive level, not derived. The strength is **M3, conditional** across the six projections. Two things remain OPEN: first-principles (M2) closure — deriving $\Theta_{\mathrm{ED}}$ from sub-primitives — and per-projection exponent derivation (which keeps the covariation prediction a family of falsifiers, §7 above). The claim shrinks if the empirical covariation prediction is falsified along any single projection axis. *(This paragraph was tightened 2026-07-05: the earlier "closed / not load-bearing" framing under-stated the A-A4-4 conditional the A4 audit itself flags.)*

---

## §8 — The ED-SC 4.x Arc

The ED-SC 4.x arc is a six-paper extension that formalizes the SCBU framework's six projections and integrates them into a unified four-regime cross-scale model.

**Paper ED-SC 4.1 — BH ↔ cosmic boundary projection.** Establishes that the black-hole horizon $r_H$ and the cosmic decoupling surface $R_H$ are two arms of one substrate-cosmology boundary, parameterized by local mass $M$ and global cosmological rate $H_0$ respectively. Two distinct projection mechanisms are identified: the BH-horizon arm uses a cross-scale fixed-point + Schwarzschild matching, while the cosmic decoupling arm uses Paper_028's substrate-causality / decoupling-surface argument (kernel-propagation-rate / Hubble-expansion-rate crossover). Both arms share the substrate-cosmology boundary anchor but employ different projection mechanisms.

**Paper ED-SC 4.2 — Substrate-derivation of $\xi_{\mathrm{canonical}}(H_0)$ (post-Route-A-closure).** The highest-leverage paper. Provides first-principles substrate derivation of the canonical operating point as a function of $H_0$. *Route A closed at substrate-parameter-INHERITED level (2026-05-17) via the Route A audit cascade — **conditional on the unproved A-A4-4 reduction** (see Paper ED-SC 4.2 §1.5 reconciliation note).* The structural setup — $\xi_{\mathrm{canonical}}$ as a fixed point of substrate renormalization-group flow on the interval $[\ell_P, R_H]$ — closes at substrate-parameter-INHERITED level (Paper_027-analog): $\xi_{\mathrm{canonical}} \sim \sqrt{\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}}} \cdot M_P$ via the Route A4 chain, conditional on the $\tau_{V_5}\to\Theta_{\mathrm{ED}}$ reduction. The honest outcome: structural framework supplied; numerical closure at substrate-parameter-INHERITED level, conditional; first-principles (M2) closure and per-projection exponents both OPEN.

**Paper ED-SC 4.3 — MOND/galactic IR projection.** Establishes the deep-MOND acceleration scale $a_0 = c H_0/(2\pi)$ as the galactic-acceleration sub-projection of the substrate-cosmology boundary, with the factor $1/(2\pi)$ arising from Paper_029's azimuthal-Fourier-mode normalization on the residual SO(2) symmetry of an accelerating chain. This is a **distinct** projection mechanism from $R_H$'s substrate-causality argument (4.1) — $a_0$ and $R_H$ share the boundary anchor but use different mechanisms onto different parameter axes. BTFR slope-4 emerges as the infrared-regime scaling law at the boundary.

**Paper ED-SC 4.4 — Q-Compute ↔ SCBU IR projection.** Establishes $\mathcal{M}_{\mathrm{crit}}$ and the Class A/B/C saturation structure as the multiplicity-budget projection of the boundary. The three architectural classes correspond to which of the three substrate constituents ($N_{\mathrm{bw}}, N_{\mathrm{V5}}, N_{\mathrm{commit}}$) saturates first as the boundary is approached. Cross-platform universality (matter-wave at 140–250 kDa, qubit-array walls) inherits from the substrate's structural invariance.

**Paper ED-SC 4.5 — Soft-matter NS-Q IR projection.** Establishes $Q \approx 3.5$ at the canonical NS-Q operating point as the hydrodynamic-Q projection of the boundary. V5's appearance as the Maxwell relaxation timescale ($\tau_M \sim \tau_{V5}$) shares the substrate object that saturates at the boundary. The Universal Mobility Law inherits from the same substrate kernel hierarchy.

**Paper ED-SC 4.6 — Unified four-regime model (capstone).** Integrates all five prior extensions. The substrate-cosmology boundary induces a unified four-regime renormalization-group structure: ultraviolet (V1-dominated), transition (V1↔V5 cascade with 0.6 exponent), infrared (V5-modulated, multi-sector projection regime), cosmological (V5-saturated boundary). All six SCBU projections occupy distinct, predictable positions within this structure.

**What the arc accomplished (post-Route-A-closure, 2026-05-17).** The ED-SC 4.x arc completes ED's cross-scale synthesis. The substrate-cosmology boundary's structure is mapped across domains; the regime classification is portable; the framework supplies multiple testable predictions (see §9); and **all six projections reach M3 with a substrate-parameter-INHERITED foundation via the Route A4 chain — conditional on the unproved A-A4-4 reduction.** Route A's closure at substrate-parameter-INHERITED level (Paper_027-analog) upgraded the arc to M3 form-IDENTIFIED + value-INHERITED + saturation-regime scale DERIVED at substrate-parameter-INHERITED level, **conditional** — the first cross-arc M3 cosmology result in the corpus, delivered via the Cosmology Arc M3 trinity + ED-SC 4.x arc-wide upgrade, with first-principles (M2) closure still OPEN.

---

## §9 — Falsification Program

ED is a falsifiable program. Each closed result carries explicit falsification criteria, and the program-level synthesis carries cross-arc tests.

**Observational falsifiers (corpus-wide):**

- *Direct detection of substrate $c$ variation.* P-RB-1 (Paper 012) commits to substrate $c$ being constant. Detection of fundamental-constant drift in $c$ that cannot be accounted for as a dressed-object coarse-graining effect refutes the framework.
- *Empirical failure of BTFR slope-4* (Paper 031). Substrate gravity predicts the Baryonic Tully–Fisher Relation with slope exactly 4 and zero intrinsic scatter in the deep-MOND asymptotic.
- *Empirical detection of complete black-hole evaporation* (Paper 041). Substrate dynamics force a Planck-mass remnant endpoint. Complete evaporation refutes the V5-cutoff mechanism.
- *Empirical detection of intrinsic scatter in BTFR beyond observational error.* Refutes Paper 031 and propagates upward.

**Structural falsifiers:**

- *Discovery of a fourth Q-Compute architectural class beyond A/B/C* (Paper 055). Refutes the three-constituent exhaustiveness of $\mathcal{M}_{\mathrm{cap}}$.
- *Demonstration that V5 admits trans-Planckian modes.* Refutes Paper 040's resolution of the trans-Planckian problem.
- *Substrate-level evidence that any of the 13 primitives is inconsistent or derivable from another.* Refutes the minimality claim.
- *Discovery of substrate-level structure below $\ell_P$.* Refutes the substrate-interior cutoff (Paper 042).

**Cross-arc falsifiers (the SCBU framework's signature tests):**

- *Hubble-tension-class predictions.* SCBU predicts synchronized co-variation of six quantities under $H_0$ shifts: $\xi_{\mathrm{canonical}}$, $a_0$, $\mathcal{M}_{\mathrm{crit}}$, $Q$, $r_H$, $R_H$. **The prediction's sharpness is currently limited by un-derived per-projection scaling exponents.** $a_0 \propto H_0^1$ is structural (Paper 029); $R_H \propto H_0^{-1}$ is structural (Paper 028); but $\mathcal{M}_{\mathrm{crit}} \propto H_0^\alpha$, $Q \propto H_0^\beta$, and $\xi_{\mathrm{canonical}} \propto H_0^\gamma$ have not been derived with specific exponents. As currently formalized, SCBU predicts "co-variation in some sense" rather than a single-exponent law per projection, which means tensions can be absorbed by adjusting the unmanaged exponents. The prediction is therefore a *family of falsifiers* indexed by per-projection exponents; with Route A now closed (2026-05-17, substrate-parameter-INHERITED level) these exponents are derivable in principle via the Route A inheritance chain, though each specific exponent ($\mathcal{M}_{\mathrm{crit}}, Q$) still requires explicit derivation. **The sharpest test in this register meanwhile is empirical detection of asynchrony** — e.g., $a_0$ tracking $H_0$ as predicted while $\mathcal{M}_{\mathrm{crit}}$ remains flat — which would refute the SCBU-projection identification for the asynchronous quantity *regardless* of un-derived exponents.
- *Multi-axis consistency.* Systems parameterizable by multiple SCBU-projection axes (e.g., a high-mass-fluid molecular system at galactic-disc accelerations) should exhibit consistent predictions across all relevant axes.
- *Cross-platform universality.* Different platforms probing the same SCBU projection should yield substrate-mapped agreement. Different platforms probing $\mathcal{M}_{\mathrm{crit}}$ (matter-wave vs qubit-array) must map to the same substrate threshold.

These tests are sharp. They do not require new physics to perform — they require careful observation of existing measurable quantities under cosmologically-varied conditions. The Hubble tension, if it persists, is itself a candidate testing ground.

---

## §10 — How to Read the ED Corpus

The full corpus comprises 100+ research papers (101 numbered + theorem-stub and synthesis additions). A complete reading is not necessary for orientation. The following **core papers** form a coherent introductory path:

**Foundational (read first):**

1. **Paper 087** — The 13 primitives (position paper). Sets the substrate ontology.
2. **Paper 089** — V1 finite-width retarded kernel (canonical reference). The first kernel.
3. **Paper 090** — V5 cross-chain correlation kernel. The second kernel.
4. **Paper 073** — Diffusion Coarse-Graining Theorem (DCGT). The substrate-to-continuum bridge.
5. **Paper 095** — Form-FORCED / value-INHERITED methodology. The corpus's methodological discipline formalized.

**One paper per major arc (read in any order):**

6. **Paper 002** — Born–Gleason rule (quantum kinematics anchor).
7. **Paper 027** — Newton's $G = c^3 \ell_P^2 / \hbar$ (gravity arc anchor).
8. **Paper 047** — Hawking spectrum via substrate-Unruh (black-hole arc anchor).
9. **Paper 060** — Matter-wave / qubit unification via $\mathcal{M}_{\mathrm{crit}}$ (Q-Compute anchor).
10. **Paper 076** — NS-2 substrate→continuum (soft-matter / NS anchor).

**Synthesis (read after core):**

11. **Paper 098** — ED-QFT Unified Overview. Program synthesis covering five sectors.
12. **Paper 100** — Five-Sector Program Overview. The 100-paper milestone capstone.
13. **Paper SCBU** — Substrate–Cosmology Boundary Unification.
14. **Paper ED-SC 4.6** — Unified four-regime model (ED-SC 4.x arc capstone).

**Post-pivot (the newest front, read for the current state):**

15. **One-Field letter** — the post-pivot gravity line's front door (gravity + dark matter + dark energy + the arrow, one field; entry to GR-I … GR-IV, KM-I/II).
16. **Form and Flesh: The Two Walls** — the program's reach statement: what ED supplies (form) and what it provably withholds (flesh), anchored by the finite-memory prime ceiling.

**Navigation strategy:**

- Each paper begins with a **Preamble** listing what the paper does *not* claim. Read these first when sampling.
- Each paper has a **§2.5 Load-Bearing Step Audit Table** that lists every step in the derivation with its discipline-label (postulate / inherited / derived / position-claim). The audit table is the paper's structural skeleton.
- Each paper closes with explicit **Falsification Criteria** and a **Position Statement**.
- Cross-references are dense but the corpus is structured to allow targeted reading: enter at an arc anchor, follow citations to dependencies, exit when the dependency chain becomes shallow.

The corpus rewards focused reading. A physicist coming from quantum mechanics can profitably read the quantum-kinematics arc + the entanglement arc + the form-level QFT arc without touching gravity. A cosmologist can read the gravity arc + the BH arc + the SCBU synthesis. A condensed-matter physicist can read the soft-matter arc + the Q-Compute arc without touching cosmology.

---

## §11 — Future Work

Several open lines of work would significantly advance the program:

**The substrate-parameter frontier (the M1 upgrade).** Route A — the substrate-level $\ell_{V5}(H_0)$ relation — **closed at substrate-parameter-INHERITED level on 2026-05-17** (Paper_027-analog), upgrading the ED-SC 4.x arc to M3 arc-wide and delivering the Cosmology Arc M3 trinity (§8). What remains open is the *fuller* closure: deriving the substrate parameter $\Theta_{\mathrm{ED}} \approx 10^{-122}$ (and $\tau_{V5}$) from sub-primitive content — the analog of the longstanding "what fixes the values of $\ell_P, \hbar, c$?" question. Closing this via Route B (substrate-derived $\beta(K)$) and/or Route C (substrate-derived $K_{\mathrm{boundary}}$ at $R_H$), without additional postulates, would upgrade the arc from M3 to **M1 — the first cross-arc M1 result in the corpus.** This is substrate-research-frontier work, not load-bearing for the current M3 verdicts.

**Hawking ↔ cosmological-redshift extension.** A natural next ED-SC 4.x extension paper: substrate-Unruh KMS structure at the SCBU boundary should connect Hawking temperature to cosmological redshift via the same boundary-projection mechanism that connects $a_0$ and $\mathcal{M}_{\mathrm{crit}}$. This would add a seventh SCBU projection on the Hawking-temperature parameter axis.

**Remnant ↔ cosmological-relic-abundance extension.** Paper 049 introduces the Planck-mass remnant relic abundance under standard FRW dilution. An explicit SCBU framing would tighten the structural anchoring of remnants to the substrate-cosmology boundary.

**Entanglement V5-saturation ↔ SCBU.** Paper 071 establishes an ER=EPR-class structural echo between V5 in the entanglement arc and V5 in the BH arc. An explicit SCBU framing would integrate the entanglement arc into the cross-scale synthesis.

**Yang–Mills ↔ SCBU.** The deepest open connection. Yang–Mills mass-gap mechanism (Paper 021) and OS-positivity audit (Paper 020) both invoke V5 at substrate level. An explicit SCBU framing would integrate the YM arc into the unified four-regime model, conjecturally as a tenth projection.

**Phase-3 GR: the full Einstein equation.** The post-pivot gravity line (§5) now derives the **weak-field** Einstein metric (GR-I, the factor of two), pins the gravitational class (GR-II, khronometric), closes the preferred-frame front (GR-IV, $\alpha_1$ suppressed by more than 70 orders), and unifies dark matter / dark energy / the arrow (KM-I/II, One-Field). What remains open is the **full nonlinear** Einstein field equation: the Phase-3 GR analysis *locates* the obstruction (a fixed-geometry invariant — the same gate as the A2 decoupling and B4 charge results) but does not cross it. Whether the full EFE emerges — and at what verdict level — remains genuinely open; the weak-field, the class, and the preferred-frame safety no longer are.

**Empirical program.** Observational programs targeting the SCBU synchronized co-variation prediction under Hubble tension; precision galactic-rotation-curve measurements of BTFR scatter; matter-wave decoherence experiments at the 140–250 kDa boundary; substrate-cutoff signatures in Hawking-radiation analog systems.

---

## §12 — Summary

Event Density (ED) is a generative substrate ontology for cross-scale physics built on:

- **One substrate** — the thirteen primitives.
- **Two kernels** — V1 (finite-width retarded) and V5 (cross-chain finite-memory).
- **Eight structurally complete research arcs (with declared open derivations)** spanning quantum mechanics, gauge theory, gravity, black holes, quantum computing limits, entanglement, soft matter, and foundational kernel theory.
- **One boundary** — the substrate-cosmology boundary at $R_H = c/H_0$.
- **Six projections** of that boundary onto distinct parameter axes (black-hole horizon, cosmic decoupling, substrate fixed-point, deep-MOND acceleration, Q-Compute threshold, hydrodynamic Q-factor).
- **Four regimes** of the unified renormalization-group structure (ultraviolet, transition, infrared multi-sector, cosmological).

The program's methodological signature: *form forced, values inherited.* Structural content of physical results is derived from the substrate ontology and explicit paper-specific postulates; numerical values are inherited from empirical matching. Every load-bearing step is labeled, every falsification path is explicit, every open question is flagged.

Two June-2026 developments extend the picture beyond the eight arcs: a **post-pivot gravity line** (GR-I … GR-IV, KM-I/II, One-Field) deriving the weak-field Einstein metric, the khronometric class, the preferred-frame safety, and the MOND / dark-energy unification from the arrow placed in the law (the full nonlinear Einstein equation still open); and a **substrate-evaluation wave** of build-and-run tests — including the program's only *proven* negative (the finite-memory prime ceiling) and its reach statement, *Form and Flesh: The Two Walls.*

The program's most ambitious **hypothesis**: that the substrate-cosmology boundary is one substrate-level object, and the apparent independence of its multiple physical manifestations — across gravity, quantum computing, soft matter, cosmology — is an artifact of viewing it through domain-specific parameter axes. The unified four-regime model offers a schema for this hypothesis. Whether it closes as a derivation rather than an organizing schema turned on Route A; **as of 2026-05-17 Route A is closed at substrate-parameter-INHERITED level** (Paper_027-analog, per Paper ED-SC 4.2 §1.5), making the unified picture an M3-supported structural claim. The remaining frontier is deriving the substrate parameter $\Theta_{\mathrm{ED}}$ itself (Routes B/C → M1).

The program's **sharpest currently-clean falsifier**: BTFR slope-4 with zero intrinsic scatter in deep-MOND (Paper 031). Testable against present galaxy-rotation-curve catalogs without requiring SCBU closure.

The program's **most structurally far-reaching** (but currently softer) test: synchronized co-variation of the six projections under Hubble-tension-class $H_0$ shifts. Sharpness here grows with per-projection scaling-exponent derivations, which are part of the Route A program.

The program is unfinished. The substrate-parameter derivation ($\Theta_{\mathrm{ED}}$; Routes B/C → M1) is open. Phase-3 general-relativity emergence is open. Empirical confirmations of the SCBU prediction structure are open. Yet the cross-domain reach across eight arcs, combined with the structural honesty of the methodology, is the program's academic case.

**ED is a research program, not a final theory.** It proposes a substrate-level account of physics that is falsifiable at every layer, integrated across every arc, and synthesized at the cross-scale level. The whitepaper is the front door; the 100+ paper corpus is the building behind it.

---

**End of Whitepaper.**

*For navigation to the corpus, see PAPERS_INDEX. For the primitive enumeration, see paper_ED_Framework_13_Primitive_Generative_System.md. For corpus-level dependency structure, see DEPENDENCY_GRAPH_ED.md. For falsification register, see Paper 101.*
