# Event Density: A Program Review

## 1. Introduction

### 1.1 The One Inversion: Commitment-Irreversibility as the Defining Primitive

Physics, as traditionally built, begins with reversible microscopic laws and treats the arrow of time as something that appears later, an emergent feature of boundary conditions, entropy gradients, and coarse-graining. The laws themselves do not point in any temporal direction; the universe simply happens to. Explanation is pushed outward, into initial conditions and statistics.

Event Density (ED) makes a single architectural inversion against that entire picture. The arrow is not emergent. It is primitive.

At the substrate level, commitment is irreversible by construction (P11, Paper_087). A commitment event cannot be undone, revisited, averaged away, or washed out by later dynamics. Where standard physics has reversible laws and an emergent arrow, ED has an irreversible law, and whatever reversibility later appears downstream of it is itself the emergent, approximate feature, not a clean symmetry the substrate hands back for free. Everything that follows, metric, spinor, gauge group, horizon, mass gap, comes from a discrete relational substrate, a participation graph of chains and channels carrying bandwidth and polarity (P02, P04, P05, P07, P09, P10, P12; Paper_087). Against a generic time-symmetric alternative, ED differs in exactly one structural respect: this primitive.

P11 does not operate alone; turning it from a label into a real dynamical constraint takes a small amount of supporting machinery, detailed in §3 once the primitive vocabulary is in hand. What matters here is the payoff: downstream, P11's most direct kinematic expression is projective measurement itself (Paper_005). A commitment event *is* what standard quantum mechanics calls a measurement outcome.

This review does not derive P11. No paper in the corpus does. It is one of thirteen primitives enumerated in the position paper (Paper_087), postulated rather than proven. The program is explicit about this: the primitives are carried, not established. What follows is an account of what a substrate obeying this one inversion produces, tier by tier, with the derivations left to the cited papers.

### 1.2 What This Paper Is, and Is Not

This is a program review. It is not a derivation and not a proof. Its purpose is to give a reader the shape of the argument across roughly 125 papers written since the program's pivot to the current 13-primitive generative framing, and to provide enough structure for a reader to judge which claims merit deeper reading in their source documents. It is a map, not the territory.

It does not attempt to prove the primitives. It does not re-derive results already established elsewhere. It does not claim closure where the underlying papers do not. Every claim carries the tier assigned by its source, derived, structural, account, or measured (§2), and where a result depends on an undischarged postulate or remains genuinely open, that status is stated plainly rather than resolved by omission.

The organizing discipline comes from the methodology paper (Paper_095, form-forced / value-inherited) and from the preambles of the cited works, each of which states what it does *not* claim before stating what it does. This review inherits that discipline rather than relaxing it for narrative convenience. Where the corpus contains an honest negative result, a wall the substrate does not get past, an open conjecture, a retracted attempt, this review reports it as such. A program that never produces a "no" is not being read carefully enough to be trusted; several results below are exactly that kind of "no," and they are treated as evidence of the program's health, not its failure.

### 1.3 Scope and Roadmap

The review proceeds in fourteen sections. Section 2 sets out the tiering vocabulary and explains why consilience, reproducing what is already known, is weak evidence for a substrate theory, while divergence, making a claim nothing else makes, is strong evidence. That argument is stated there and returned to, with case studies, in the closing section.

Section 3 sketches the substrate itself: the participation graph and its primitives, briefly, with full enumeration left to the position paper.

Sections 4 through 9 walk the physics arcs in the order suggested by downstream consequence: quantum mechanics (§4); matter sector, gauge groups, spin, chirality, dimensionality (§5); Yang–Mills (§6); gravity (§7); black holes and information (§8); cosmology (§9). Section 10 presents the unifying lens, the coarse-graining "layers" program, and is explicit about where the substrate reproduces the standard continuum object and where it honestly does not. Section 11 covers substrate-level stress tests run for their own sake, independent of any physics claim. Section 12 collects the program's predictions and falsifiers. Section 13 names the open fronts plainly: the matter-sector residue, the Gleason-analog closure, the cosmological-constant integral. Section 14 closes with the epistemic argument in full, using the case studies as evidence.

Every section is tiered honestly using the vocabulary of §2, and every substantive claim is followed by a citation to its source rather than argued from scratch. A reader who finishes this review should know what Event Density actually claims, at what confidence, which claims are checkable now, and exactly where the program's honest edges lie, without needing to have read any of the 125 papers behind it.


## 2. How to Read This Paper: The Tiering Discipline

### 2.1 Derived, Structural, Account, Measured — the Four Verdicts

Every substantive claim in this review carries one of four verdicts, appearing throughout in parentheses after the claim they attach to, exactly as they appear in the source papers' own audits. They are not a confidence scale; they are different *kinds* of claim, and keeping them distinct is the discipline that prevents a year-long, multi-author program from quietly upgrading its own results.

**Derived.** A result that follows directly from the thirteen primitives (and previously derived results), with no additional assumptions. This is the strongest tier the program awards, and it is used sparingly and specifically.

**Structural.** A result whose *form* is fixed by the substrate, but whose argument is not yet a closed derivation. It may rely on a declared postulate not yet reduced to the canonical thirteen, or on a substrate reading the source paper itself flags as not yet a theorem. Structural results are real content, but conditional, and the condition is always named.

**Account.** A coherent, substrate-native explanatory narrative. An account can unify phenomena and illuminate mechanisms, but it is explicitly not a proof, and the program does not treat it as one.

**Measured.** A result established by simulation or numerical experiment on the substrate's own dynamics. Measured results carry their own honesty requirement: a measurement can come back negative, and several results in this review are exactly that kind of negative.

A related tag, **inherited**, marks content taken from prior work or observation rather than established at that step; it is discussed separately in §2.2, since it cuts along a different axis.

The discipline comes from the methodology paper (Paper_095) and the position paper (Paper_087). Its purpose is simple and strict: prevent a structural reading from being mistaken for a derivation, an account from being cited later as if no gaps remained, and a conditional result from being treated as unconditional. The verdicts are the mechanism that keeps roughly 125 papers honest against each other.

### 2.2 Form-Forced vs. Value-Inherited

Orthogonal to the four verdicts is a second split, applied to results that carry a number: does the substrate fix the *form* of the law, and does it produce the *value*, or is the value inherited from observation?

Across every major arc, the program's answer is consistent: ED claims the former far more often than the latter, and it says so explicitly. Newton's constant is a clean example: the substrate forces the relation $G = c^3\ell_P^2/\hbar$, a structural claim linking gravity's strength to the substrate's own scale, but the specific value of $\ell_P$ (equivalently $\hbar$ or $c$) is inherited empirically, not produced by the primitives (Paper_027). The MOND transition acceleration is sharper still: the substrate forces the geometric factor $1/(2\pi)$ in $a_0 = cH_0/(2\pi)$, while $H_0$ is ordinary cosmological content, not derived (Paper_029).

This split is not an apology for incompleteness. A substrate built from bare relations, with no privileged absolute scale, has no mechanism by which it *could* produce an absolute number from nothing. What it can produce, and what ED claims it does produce, is the *relation* between scales once one is supplied. Reading "form-forced, value-inherited" as a weaker version of "derived" misses the point. It is a distinct, more falsifiable claim: get the relation wrong, and the claim breaks regardless of which numbers are plugged in. Several of the program's sharpest predictions (§12) are exactly this kind of relational claim.

### 2.3 Why Consilience Is Not Evidence, and Divergence Is

One further interpretive rule governs how the wins in this review should be read. It is stated here, before the physics, because it changes how a reader should interpret a long run of successes.

Reproducing a result that standard physics already has does not, by itself, raise ED's epistemic tier. A sufficiently flexible theory can reproduce a great deal. Agreement across many arcs is read here as structural coherence, evidence that the substrate hangs together internally and that its derivation chains do not fight each other, but it is not treated as evidence that the substrate is *true*. This is a deliberate, stated position, not a hedge adopted after the fact to explain away whatever the program has not yet shown.

What *is* treated as evidence is **divergence**: cases where the substrate cannot reproduce the standard object, produces something structurally different, or reaches a genuine, honest wall. A program that only ever reports matches is not being tested. The results in §10 and §11 include several places where the substrate was asked to reproduce a known continuum object (the diffusion equation, Gaussian statistics, a Maxwell-type field) and, in at least one documented case, plainly could not without an additional assumption the program refused to smuggle in. Those walls, and the places where the substrate makes a claim standard physics does not make at all and could in principle be shown wrong, are weighed far more heavily than the length of the list of correct reproductions; being checkable is what makes a novel claim count as evidence, not the novelty on its own.

This principle is stated here and applied throughout §§4–11. It is returned to explicitly in §14, where the case studies from the layers program and the substrate-evaluation wave (Paper_TheArrowSortsTheContinuum and its companion papers) are used as the evidence for the epistemic stance set out in this section.


## 3. The Substrate

### 3.1 The Participation Graph: Chains, Channels, Bandwidth, Polarity

At the foundation of every downstream result in this review is the **participation graph**: a discrete relational structure built from **chains**, **channels**, **participations**, **bandwidth**, and **polarity**. It assumes no background spacetime, no continuum, no metric. Those appear later, as coarse-grained readings of this graph, not as inputs to it (Paper_087).

**Chains** are the substrate's primitive bearers of identity: forward-causal sequences of events, not particles moving through spacetime and not excitations of a pre-existing field (P01). A chain's identity *is* its sequence.

**Channels** are ontological primitives with intrinsic identity (P07). Two channels at the same locus are distinct even if they carry identical bandwidth or polarity; channel identity does not reduce to the values it happens to hold.

**Participation** (P02) is the substrate's basic relation: a chain participating in a channel at a locus and time, the four-tuple $(C, K, u, t)$. It is not derived from a deeper interaction or coupling; it is the substrate's fundamental mechanism for chain-channel linkage, and nearly every kernel-level and gravity-arc result rests on it.

**Bandwidth** (P04) is a non-negative, additive scalar $b_K(u) \geq 0$ carried by each participation. It is the substrate's measure of "how much" participation occurs at a locus. Under coarse-graining, bandwidth becomes probability weight (§4), gravitational field strength (§7), and several other continuum quantities.

**Polarity** (P09) is the substrate's single angular primitive: a $U(1)$ phase $\pi_K(u,t)$ transported along graph edges by a connection-like structure (P05). Polarity is the only phase the substrate carries; larger gauge structure emerges from rule-type composition on top of it (§5), not from enlarging the primitive group.

These five ingredients, chains, channels, participation, bandwidth, polarity, form the vocabulary used throughout this review. Their full operational detail, and the audit of which downstream papers rely on which primitive, appear in the position paper (Paper_087) and the primitive-audit document (Paper_088).

### 3.2 The Primitives, Enumerated

The canonical system consists of **thirteen primitives, P01–P13**, postulated rather than derived, laid out and audited in the position paper (Paper_087). This review does not reproduce that audit; it lists the primitives here so later citations are legible without cross-reference.

- **P01** — chains as primitive ontological objects (§3.1).
- **P02** — participation as the primitive chain-channel relation (§3.1).
- **P03** — channel and locus indexing with spatial homogeneity: operations are translation-invariant, no locus privileged.
- **P04** — bandwidth as a non-negative additive scalar (§3.1).
- **P05** — polarity-transport: a connection-like structure moving polarity along graph edges.
- **P06** — spatial dimension: three spatial dimensions plus one temporal direction (with P13). Postulated, not derived; one of the most load-bearing commitments in the framework. Whether it reduces to the other twelve is explicitly open. Attempts at a substrate-native account (§5.5) are exactly that, attempts, not derivations.
- **P07** — channel structure as an ontological primitive (§3.1).
- **P08** — the substrate scale $\ell_{\mathrm{ED}}$, empirically identified with the Planck length (inherited, not derived; §2.2).
- **P09** — $U(1)$-valued polarity (§3.1).
- **P10** — rule-type multiplicity: the substrate supports several structurally distinct rule-types (matter-carrying, gauge, kernel).
- **P11** — commitment-irreversibility, the arrow (§3.3).
- **P12** — the stability landscape: a per-chain functional $\Sigma_C = \mathrm{Coh}(C) - \mathrm{Str}(C) - \mathrm{Grad}(C)$ whose negative gradient gives a chain's experienced acceleration; the same functional realized directly in the certified dynamical simulator (§11.3).
- **P13** — time homogeneity: invariance under time translation, ensuring P11 is the *only* temporal asymmetry the substrate carries.

Four primitives, P02, P04, P05, P11, are load-bearing in nearly every downstream arc. P06, P09, P12, P13 each anchor large, specific subsets. The position paper states plainly, and this review inherits the statement, that the thirteen are necessary for the derivations built on them, not claimed to be minimal. Whether some reduce to others remains open in specific, named cases, P13 to P11 and P03, and P06 to P03 and P07, rather than left as a general, unspecified possibility.

### 3.3 The Arrow: Commitment as the One Irreversible Primitive

**P11, commitment-irreversibility**, is the program's defining inversion (§1.1). At a commitment event, a chain's multi-channel participation collapses to single-channel participation, and the phase content of every unselected channel is randomized. The collapse is irreversible: no substrate-level operation returns a post-commitment state to its pre-commitment description.

P11 is postulated, not derived. Its status as a primitive is the organizing fact of this review. What distinguishes it is not epistemic tier, all thirteen share that tier, but structural role: it is the substrate's only source of temporal asymmetry (P13 guarantees this), and the single point where ED's substrate diverges from a generic time-symmetric relational alternative.

Three downstream consequences illustrate its reach. In the kinematic arc, a commitment event is read as a measurement outcome (§4); the kernel machinery giving commitment its forward-causal direction appears in Paper_093 (Theorem T18). In the gravity arc, the same primitive, made dynamical, supplies the lapse that ties spatial curvature to clock rate (§7; Paper GR-I), and its concentration defines a forming horizon, a region where committed structure accumulates until the bandwidth field is driven to zero (§8; Paper GR-III, Paper_039). These connections are not argued here; they are developed in §§4, 7, and 8. They are cited only to show how far one primitive, postulated once, is asked to reach.


## 4. Quantum Mechanics, Downstream

### 4.1 The Born Rule from Participation-Frequency

In ED, the Born rule $P(K) = |c_K|^2$ is not an axiom imported from Hilbert-space quantum mechanics. It is a **conditional structural derivation** grounded in the substrate's own statistics of commitment. Over many identically prepared trials, a chain's long-run frequency of committing to channel $K$ converges to that channel's share of total bandwidth, $f_K = b_K / \sum_{K'} b_{K'}$, an analytical consequence of the substrate's commitment dynamics, not a simulation result (Paper_003). Once upstream work identifies bandwidth with squared amplitude, $b_K = |c_K|^2$ (Paper_001), the frequency limit *is* the Born rule.

The derivation rests on one declared postulate, **P-LinRate**, which states that commitment rate is linear in bandwidth. P-LinRate is not derived from the canonical thirteen primitives; it is named explicitly as an added assumption. The discipline is clear: the Born rule is not assumed at the Hilbert-space level, but encoded one layer down in a structural postulate about commitment statistics. Commitment's phase-randomization of unselected channels (P11, §3.3) is what makes repeated trials independent, allowing the frequency interpretation to hold at all.

### 4.2 Hilbert Space as Completion, Not Assumption

A substrate-first program must avoid circularity: assuming Hilbert space and then "deriving" quantum mechanics from it proves nothing. ED avoids this by treating Hilbert space as a **Cauchy completion** of an algebra built directly from substrate content. The pre-individuation amplitudes of Paper_001 form a motif algebra, tuples of substrate amplitudes closed under linear combination and equipped with a sesquilinear inner product. Completing that algebra under its induced norm yields a Hilbert space (Paper_007).

This is a structural account of where the arena comes from, not a reconstruction in the operational-axiomatic sense of Hardy or Coecke–Kissinger. The completion step is standard; what matters is the object being completed. The inner product used at this stage is inherited from prior work, not derived here, and its substrate-level justification is the subject of §4.3. The methodology paper (Paper_095) is explicit: emergence of the container is claimed; derivation of everything inside it is not claimed at the same step.

### 4.3 The Gleason-Analog Gap, Honestly

The inner product required for Hilbert-space completion is itself the focus of a dedicated attempt at a substrate-level Gleason-type uniqueness result. Its honest status is **partially successful and explicitly open**, not a solved problem.

**What the attempt shows.** With two additional postulates, **P-Channel-Orthogonality** (distinct channels are orthogonal in the substrate's inner-product structure) and **P-Gleason-Compatibility** (a non-contextuality condition on probability assignment across channel decompositions), the standard sesquilinear inner product is fixed up to normalization (Paper_004). This is real content: it identifies exactly what must be true of the substrate for the usual inner product to be the only consistent choice.

**What remains open.** Neither postulate is yet reduced to the canonical thirteen primitives. Paper_004 states this plainly: no argument is given showing that P07's channel-distinguishability forces orthogonality, nor that spatial homogeneity and commitment-irreversibility together force non-contextuality. Until those reductions are supplied, the reader is given an explicit choice: accept the two added postulates and treat the inner product as conditionally derived, or decline them and treat it as inherited. Nothing is hidden or implied.

This gap is carried in the review as a named, active research target, closing or refuting P-Channel-Orthogonality and P-Gleason-Compatibility from the primitives, rather than as background the corpus has quietly moved past.

### 4.4 Spin, Statistics, and the Origin of ħ

Spin's substrate-native account is the most recent development in this arc, and it is grounded in relationality rather than posited as an intrinsic particle property. In ED, an object is never free; it is tethered to the participation graph by its channels (P07), and a free, untethered object would have no need of what follows. Acting on such a tethered object with the emergent rotation group exposes a topological fact invisible to a free point: a $2\pi$ rotation is a non-contractible loop of the tethered configuration, and only a $4\pi$ rotation returns it untwisted. This is the familiar belt-trick structure of the double cover of the rotation group. An object required to track that twist transforms under $SU(2)$ and acquires the characteristic sign flip under $2\pi$. On this account, spin-$\tfrac12$ is a structural consequence of being embedded in the graph, the mark of being relational rather than isolated.

Statistics is developed as an **account** across a cluster of papers addressing the Clifford frame, the Dirac equation, and spin-statistics directly. That account covers the antisymmetry of fermionic exchange and the symmetry of bosonic exchange, the assembly of the full spinor, chirality read as a screw sense in channel structure, and the internal gauge index read as channel multiplicity. The origin of $\hbar$ is read as the substrate's single angular unit (P09) propagated through coarse-graining to the continuum scale at which it is measured. Its numerical value is inherited empirically, not produced by the primitives (§2.2).

The tiering across this subsection is mixed and stated as such: the tethering argument for spin-$\tfrac12$ is structural and recently strengthened; the full assembly of spinor, chirality, and statistics is carried as an account; and the numerical value of $\hbar$ is inherited.


## 5. Matter and Forces

### 5.1 Gauge Groups from Channel Multiplicity

In ED, gauge structure does not come from enlarging the substrate's single polarity phase into a bigger primitive group. It comes from **how many channels of a given rule-type run together**. A family of $N$ indistinguishable channels, under bandwidth conservation (P04), carries a structure group $U(N) = SU(N) \times U(1)$, where the abelian factor is single-channel transport and the non-abelian factor is cross-channel mixing (Paper_MS-II). The Standard Model's $U(1) \times SU(2) \times SU(3)$ corresponds directly to multiplicities $\{1,2,3\}$, taken up again in §5.4.

This supersedes an earlier, weaker treatment (Paper_015, Theorem T17), which rewrote fiber-bundle vocabulary onto the substrate but did not derive non-abelian structure. The multiplicity argument goes further: it derives $SU(N)$ from a countable primitive (channel multiplicity) plus a conservation law (P04), rather than asserting the vocabulary by analogy. P05's connection structure supplies the transport itself: a genuine $U(N)$ lattice-gauge link variable, with field strength recovered as plaquette holonomy. The substrate is, in this sense, a lattice gauge theory, but one built on a relational graph rather than a rigid periodic lattice, and carrying the retarded arrow rather than a time-symmetric rule. That distinction is what lets it escape the Nielsen–Ninomiya doubling theorem, which binds only rigid, hermitian lattice theories, neither of which ED uses.

### 5.2 Spin, Assembled from Channel Topology

The substrate-native derivation of spin-$\tfrac12$ from tethering and orientation-entanglement (§4.4) is not repeated here. What matters in the matter-sector context is the **compositional picture**: the full four-component spinor is assembled from substrate objects already in hand. Spin and chirality (§5.3) are channel-topology attributes; the internal gauge index is channel multiplicity (§5.1); the object's $U(1)$ phase is polarity transport (P05, P09), the chirality-blind vector coupling that becomes electromagnetism (Paper_MS-II).

Standard physics *posits* the spinor as a representation of the Lorentz group and its internal symmetries. ED instead builds it from tethering, multiplicity, and polarity, and asks whether the assembly reproduces the standard object. The kinematic skeleton, spin and gauge index, is grounded this way. What remains open is the full classification of which channel-topology class carries which combination of spin and gauge representation, named explicitly in §5.3 and §13.

### 5.3 Chirality, Baryogenesis, and the Arrow's First Commitment

The substrate's channel structure and polarity are parity-symmetric: nothing in P05, P07, or P09 distinguishes left from right. Producing the real world's chiral weak force from a parity-symmetric starting point is one of the sharpest challenges for any discrete-substrate program. The Nielsen–Ninomiya theorem is often cited as ruling out chirality on a lattice; §5.1 already noted why its premises, a rigid periodic lattice and a hermitian rule, do not bind ED.

Chirality is not carried by the substrate's transport structure. In 3+1 dimensions, the retarded (non-hermitian) transport's surviving mode is **vector-like**, not chiral, so the mechanism that produces handedness must be found elsewhere. It is found in the arrow's **first commitment**. A commitment event is handed, carrying both a phase (a matter/antimatter, C-type reference) and a channel-topology screw orientation (a parity, P-type reference). The claim is that the universe's first commitment imprints both references at once, correlated because they are one event, but distinct attributes, so that parity violation and matter/antimatter asymmetry are two faces of a single lock-in rather than two independent coincidences. Both come out maximal because both are topological. This is carried as an **account**: coherent, substrate-native, and unifying two major asymmetries under one mechanism, but explicitly not a closed derivation.

Two pieces remain open: the relativistic bridge from this screw orientation to a covariant $\gamma^5$ coupling, and *why the weak force specifically* inherits the handedness. Representation classification and anomaly cancellation, the hardest consistency requirements of a chiral gauge theory, are untouched.

### 5.4 Why {1, 2, 3}: Uniqueness Reduced to One Number

Why the Standard Model's gauge groups have exactly the sizes they do is not derived outright, but reduced to a single sharp question. Model the channels of one multiplicity family as complex unit vectors in an internal amplitude space $\mathbb{C}^d$. They remain mutually distinguishable, and thus coexist stably, only while they remain orthogonal. The maximum number of mutually orthogonal vectors in $\mathbb{C}^d$ is exactly $d$. The stable channel families are therefore $\{1,\ldots,d\}$, and the Standard Model's $\{1,2,3\}$ corresponds to internal amplitude dimension $d=3$ (Paper_MS-II).

A falsifiable consequence follows: **no stable fundamental $SU(N\geq4)$** gauge sector, since $\mathbb{C}^3$ cannot hold four mutually orthogonal channels.

One distinction is essential, so the argument is not misread: the dimension $d=3$ here is an *internal* one, the dimension of a complex channel-amplitude space, not the three dimensions of physical space. The two are not interchangeable. $SU(3)$ (complex, dimension eight) is not $SO(3)$ (real, dimension three), and observed color is invariant under physical-space rotations, so the internal count cannot simply be identified with the spatial one. The remaining open question is singular: **why the internal channel-amplitude dimension is three**, a number not yet derived, only isolated.

### 5.5 Why Three Dimensions: the Honest, Unresolved Thread

Three spatial dimensions is postulated (P06, §3.2), not derived. The position paper is explicit: it is one of the most consequential commitments in the framework. This subsection reports the corpus's most recent attempt to give P06 a substrate-native **account**, not a derivation.

The argument begins with a topological fact: a spatial link, two loops threaded through each other, is the only structure that can hold an order against continuous rearrangement. A link forms and holds in exactly three spatial dimensions; two dimensions cannot form one, and four dimensions let any link come apart. Since the arrow's purpose is to hold committed order against being undone, the candidate account is that ED reaches for exactly this structure: three dimensions because that is the only place the order-holder it needs can exist.

The topological half is solid mathematics. The **substrate-specific half** is layered. A single chain's local channel-composition structure is provably too simple (topologically planar) to ever link, a genuine negative, narrowly scoped. Once cross-chain correlation (the V5 kernel) is included, the full participation graph can be shown, constructively, to contain structures that force linking under any embedding, a real, checked positive, robust to whether the correlation is modeled as local or long-range.

What remains open is the operational claim: that undoing a commitment order in this structure actually requires the kind of collision the topology predicts. That test is not yet settled, and the question is open, not resolved either way.

The honest summary: P06 is postulated; its downstream load is large; and ED has a specific, partially supported, still-incomplete candidate account for it. It is reported at exactly that tier, and revisited in §13 as a named open front rather than a closed result. One further honesty is worth stating: whether the internal three of §5.4 and the spatial three of this subsection are ultimately the same fact, or an unexplained coincidence, hangs on this same unresolved linking question, and is not claimed either way.


## 6. Yang–Mills

### 6.1 The Action from Coherence-Deficit

The Yang–Mills arc in ED has undergone a genuine upgrade. An earlier treatment (Paper_019) obtained the continuum Yang–Mills action, $S_{\mathrm{YM}} = -\tfrac14 \int F^a_{\mu\nu} F^{a\,\mu\nu}$, only by postulate: the source paper openly stated that the substrate's coarse-grained rule-type action was *assumed* to match the standard form and still required a derivation. That derivation has now been supplied.

The substrate's channel structure already penalizes phase mismatch, the same coherence cost that underlies the Maxwell case (§10). Around a plaquette, that cost is exactly the deficit of the $U(N)$ holonomy from the identity, $1 - \tfrac1N\,\mathrm{Re}\,\mathrm{Tr}\,U_\square$, which is the Wilson plaquette action. Crucially, this is not chosen to match Yang–Mills; it is read off the substrate's own coherence dynamics. Expanding the holonomy in the small-deficit (continuum) limit yields $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$, recovering the Yang–Mills action with non-abelian self-interaction emerging automatically from holonomy non-commutativity, and Lorentz covariance inherited from the substrate's acoustic metric (Paper_017; derivation in Gauge_06, building on Gauge_02).

The abelian and non-abelian cases unify under this mechanism. For a single channel ($N=1$), the same coherence-deficit reduces to the Maxwell case, the coherent recovery of the Coulomb field from the substrate's coarse-graining (§10.2). For $N>1$, the non-abelian lift appears automatically. This is now carried at a **structural/analytic derivation** tier, upgraded from the earlier postulate, resting on one input stated plainly: the form of the *per-chain* coherence cost, the gauge generalization of the abelian phase-mismatch penalty. Given that input, the trace-of-holonomy (Wilson) form above is itself *derived*, not assumed, as the average of the per-chain cost over indistinguishable channels (P08); this is one fewer assumption than it first appears. The abelian case is grounded directly against the certified simulator; the non-abelian generalization is analytic, argued from channel indistinguishability but not yet directly simulated, and is named as the one load-bearing input still standing.

### 6.2 The Mass Gap as Non-Abelian Channel Structure

The gap between Maxwell (massless, long-range) and Yang–Mills (gapped, confined) is read as a direct consequence of **non-abelian channel structure**, not as a generic feature of "having a gauge field" that then needs a separate explanation for why it sometimes fails to appear.

Where channels commute ($U(1)$), the coherence-deficit of §6.1 is purely quadratic, a free field, and nothing prevents arbitrarily long-wavelength excitations from costing arbitrarily little. That is the massless Coulomb field. Where channels do not commute ($U(N\geq2)$), the same deficit carries genuine cubic-and-quartic self-interaction with no abelian counterpart. The gauge field sources itself, and the gap is read as the non-perturbative consequence of that self-interaction.

An earlier, independent mechanism in this arc composes three substrate facts: finite kernel width, finite cross-chain correlation reach, and non-abelian self-coupling. Together they set an intrinsic correlation-length floor, with the spectral gap inversely proportional to that floor (Paper_021). The coherence-deficit picture supplies candidate substrate-level origins for two of that mechanism's previously open postulates, a structural source for the coercivity bound and a strong-coupling route to the confining area law, without closing either postulate outright. Both are stated as candidates, not proofs, in the source paper.

One honest limit must be stated plainly. The strong-coupling confinement argument, taken alone, confines *any* lattice gauge theory, abelian or not. It explains why the substrate confines at all, not why Yang–Mills specifically stays confined in the continuum limit while Maxwell does not. That distinguishing fact is exactly the non-abelian self-interaction of §6.1, and whether it survives the continuum limit is the open core named directly in the next subsection.

### 6.3 What This Is Not: Clay-Relevance vs. Constructive Proof

This program does not claim to solve the Clay Millennium Yang–Mills problem, and it says so as plainly as possible. The Clay problem asks for a rigorous constructive proof that Yang–Mills theory exists as a mathematically well-defined object and that its mass gap is provably positive. What ED supplies is a **physical mechanism**: a substrate-native account of why the action takes the form it does and why the gap is present, tiered honestly as structural and as a candidate mechanism, not as the kind of mathematical construction the prize requires.

The distinction is categorical, not incremental. Physics explains; constructive field theory proves. They are not interchangeable currencies. The arc's own synthesis states its position explicitly as **"Clay-relevance at structural-positive level"**, above a bare analogy to standard constructive programs but below constructive proof, and names the specific gaps that remain open: the continuum probability measure is not constructed; the full Osterwalder–Schrader axioms are not derived beyond the conditional postulates already in use; and the mass gap's survival in the strict continuum limit remains conditional on an unproven rescaling assumption (Paper_023).

None of this is treated as a hedge. A program that distinguishes physical mechanism from mathematical proof, and says so in its own synthesis paper rather than leaving a reader to infer it, is doing exactly what this review's epistemic discipline (§2) requires.


## 7. Gravity

### 7.1 The Bandwidth Field and the Weak-Field Metric

In ED, gravity is not an added interaction. It is the **coarse-grained shape of the substrate's own bandwidth field**. Bandwidth $b$, the substrate's scalar measure of connection capacity (P04), supplies an emergent spatial metric via $g \sim 1/b$, and the new content is the **temporal lapse**. Requiring the substrate's fastest signal to define the light cone, together with the commitment-rate law, forces $N^2 \sim b$, so the same field sets both spatial curvature and clock rate (Paper GR-I). That single locking produces the Schwarzschild relation $g_{00}g_{rr}=-1$ and, with it, the classical weak-field tests, including the decisive one: gravitational light bending at exactly twice the scalar-theory value. Direct ray-tracing gives a measured ratio of 2.09 against the predicted 2.00, with a conformal control landing at zero.

This is a **structural derivation** of the weak-field limit, not a reconstruction of full nonlinear GR. The dynamical rule that lets the bandwidth field evolve, form structure, and produce horizons is a separate result (Paper GR-III), taken up in §8. What is claimed here is narrower: one substrate field, coarse-grained, reproduces Einstein's weak-field metric and its classical tests without tuning.

### 7.2 The Khronometric Class: Einstein Plus the Arrow, and Nothing Else

Which gravity theory does ED land in? Lovelock's theorem forces any sensible metric theory toward Einstein unless an extra field propagates. ED has exactly one: the **arrow's preferred foliation**. Because the arrow lives in the law (P11) rather than in boundary conditions, the substrate carries a preferred time-slicing, and the propagating content is Einstein's two tensor modes plus one scalar, the foliation made dynamical. This is the **khronometric** class, the infrared limit of Hořava gravity (Paper GR-II).

It is not GR; it is a specific preferred-frame theory. Normally such theories die immediately against precision tests. Here, the same unification that produces the extra scalar also protects the theory: matter and geometry share one substrate and one causal cone, so gravitational-wave speed equals light speed as a structural identity, satisfying the $10^{-15}$ constraint from the 2017 neutron-star merger automatically rather than by tuning. Whether the preferred-frame couplings stay inside existing bounds is a numerical question addressed directly in §7.5.

### 7.3 Dark Matter as the Deep-Field Regime

At low accelerations, in galactic outskirts, the same field behaves as the deep-infrared regime of the khronon, reproducing MOND phenomenology without positing a particle (Paper KM-I). The transition acceleration is not fitted; it is identified as the dipole projection of the cosmic decoupling surface $R_H=c/H_0$ onto an accelerating chain's anisotropic adjacency, giving $a_0 = cH_0/(2\pi)$, with the geometric factor $1/(2\pi)$ forced by the azimuthal-Fourier structure of the projection, not chosen to match data. Once $H_0$ is supplied, the predicted value matches the observed MOND scale to within roughly ten percent, with zero free parameters (Paper_029).

Combined with ED's derivation of Newton's constant, the same mechanism yields a baryonic Tully–Fisher relation with slope exactly four and **zero intrinsic scatter** in the deep-MOND asymptote, a sharp, falsifiable claim against rotation-curve catalogs. This is a **structural account** with a parameter-free numerical match, not a curve fit.

### 7.4 Dark Energy and the One-Boundary Unification

The same cosmic boundary that supplies the galactic transition scale also anchors the dark-energy scale. The honest tiering has two parts.

**Form.** The cosmological regulator dial behaves, on cosmological backgrounds, as a dark fluid. An orthogonality result separates it cleanly from the galactic regime of §7.3, so nothing can be quietly retrofit. The notorious $10^{120}$ problem is reframed as the ratio of two scales ED already has, the cosmic rate against the Planck rate, squared, rather than a separately tuned miracle (Paper_038_5). One boundary, $R_H=c/H_0$, supplies both the galactic transition scale and the vacuum-energy scale.

**Magnitude.** The ab-initio boundary integral has a specific pinned target: a dimensionless coefficient near $-162$. That computation is not complete, and is named as open. The wrong sign or an order-of-magnitude miss would break the one-$\Lambda$ thesis outright, which is exactly what makes it a real claim rather than an unfalsifiable reframing.

### 7.5 Preferred-Frame Safety: Closing α₁/α₂

Preferred-frame theories usually fail immediately against solar-system and pulsar-timing tests. ED treats this as a **kill-switch**, not a footnote.

Of the two relevant PPN parameters:

- $\alpha_2 = 0$ **exactly**, a structural consequence of matter and geometry sharing one causal cone. This is verified directly against the literature bound.
- $\alpha_1$ is suppressed: $\alpha_1 = -4\lambda_{\mathrm{local}}$, with $\lambda_{\mathrm{local}} \sim \rho_{\mathrm{event}}/\rho_{\mathrm{Planck}}$, the ratio of local committed-event density to Planck density. Dense commitment is the quantum Zeno limit that would freeze the substrate's quantum sector, so the same sparseness of commitment keeps both quantum mechanics alive and preferred-frame effects small. Either failure would break both simultaneously.

The result closes both preferred-frame fronts by roughly seventy to eighty-eight orders of magnitude below experimental bounds, a structural safety margin, not a tuned parameter.


## 8. Black Holes and Information

### 8.1 Horizon as Decoupling Surface

In ED, a horizon is not a geometric boundary drawn on a pre-existing spacetime. It is a **statistical transition** in the substrate itself. As committed structure accumulates during collapse, the cross-chain correlation kernel (V5), normally responsible for allowing one region of the participation graph to influence another, loses its reach across a critical surface. That surface is a **decoupling surface**, not a geometric edge (Paper_039). Once the kernel's reach collapses, committed information cannot cross it, directly by P11, and the coarse-grained location of this statistical transition coincides with the general-relativistic horizon.

One honest limit is stated explicitly in the source paper and kept visible here: the **location** of the horizon is *not* derived from the primitives in this treatment. It is taken from the weak-field GR identification and used as the reference point against which the substrate-level decoupling mechanism is positioned. What is claimed is the mechanism operating at and near that location, not the location itself.

### 8.2 The Hawking Spectrum, Non-Thermal Corrections, and the Planck-Mass Remnant

Near the decoupling surface, the V5 kernel acquires an imaginary-time periodicity. A system periodic in imaginary time is thermal; this KMS structure supplies the leading-order Hawking temperature. At the same time, the kernel's finite memory imposes a structural ultraviolet cutoff, $\omega_c \sim c/\ell_P$, resolving the trans-Planckian extrapolation that standard semiclassical derivations require but do not justify (Paper_039).

This finite-memory structure yields a headline prediction: the Hawking spectrum is **not purely thermal**. The leading correction is sign-definite, grows as the hole shrinks, and is information-bearing rather than a negligible smoothing (Paper_047). The evaporation endpoint follows from the same cutoff: as the hole shrinks, its dominant emission frequency rises, and evaporation halts when that frequency would exceed $\omega_c$. The result is a stable remnant at $M_\star = \hbar/(c\ell_P) = M_P$, the Planck mass, at leading order (Paper_039 §6).

### 8.3 The Page Curve and the Paradox That Doesn't Form

The standard information paradox requires three ingredients simultaneously: purely thermal radiation, complete evaporation, and unitary quantum mechanics. ED declines two of these premises directly. The radiation is not purely thermal (§8.2), and evaporation is not complete; a remnant persists. What remains, substrate-level bandwidth conservation and a finite cross-chain entanglement budget, produces the familiar Page-curve shape: early rise as interior and radiation share correlation, turnover once the entanglement budget saturates, and decline as correlation re-routes into radiation-radiation and radiation-remnant channels (Paper_050).

No entanglement-monogamy violation is invoked. Correlation crossing the horizon is read as genuine cross-horizon straddling and later radiation-radiation correlation, not partial distillation into monogamy-violating pairs (Paper_052).

One honest limit is stated precisely: this is a **substrate-level** unitarity-preserving mechanism. The source paper does **not** claim a proof of unitarity at the Hilbert-space level. The relationship between substrate bookkeeping and textbook quantum mechanics in a black-hole context is named as non-trivial and unresolved. Several numerical scales, the Page-time coefficient among them, are inherited from standard results rather than derived. What is claimed is the mechanism's shape, not every number in it.

### 8.4 The Entropy Coefficient: Deriving the 2π

The Bekenstein–Hawking entropy, $S = A/4$, splits into two pieces: the geometric factor (surface gravity) and the thermal factor ($2\pi$). ED's status on each has changed recently and is worth stating precisely.

The geometric half, $\kappa = 1/(2r_s)$, was already derived directly from the slope of the substrate's bandwidth profile. The thermal half, the $2\pi$ in $T = \kappa/2\pi$, was previously treated as inherited from standard horizon thermodynamics. That is no longer accurate. The same derived bandwidth profile, examined at the horizon, has exactly the Rindler form, confirmed numerically. The smoothness of that near-horizon geometry forces the imaginary-time period, and with it the $2\pi$, by the same Euclidean-continuation argument used in GR. **Both halves of the coefficient are now structural**, derived from one field the substrate already produces, not from polarity (P09) and not from holography.

One open question sits alongside this result. The derivation above uses the Euclidean continuation, the same tool GR uses. Whether the $2\pi$ can instead be obtained *without* it, from raw one-way commitment statistics directly, is unresolved, and there is a structural reason to suspect it may not be separable at all: even a real-time derivation routes the $2\pi$ through the same analytic object, a gamma function tied to the horizon's branch structure, that the continuation relies on. The deeper reading is that the $2\pi$ may be an intrinsically continuum feature of smooth horizons rather than something that lives at the level of raw commitment counting, in which case asking for it below the continuum is the wrong question rather than an unmet one. This is named as an open front, not folded into the result above.


## 9. Cosmology

### 9.1 One Boundary, Six Projections

A single substrate-cosmology boundary, the cosmic decoupling surface $R_H = c/H_0$, already responsible for the MOND transition scale (§7.3), reappears throughout the corpus in multiple, structurally distinct guises. The cosmology arc is organized around making that recurrence explicit rather than treating each appearance as an isolated coincidence. Six projections of this one boundary are identified: the black-hole horizon, the cosmic decoupling surface itself, a cross-scale-invariance operating point ($\xi_{\mathrm{canonical}}$) arising from the substrate's kernel hierarchy, the MOND acceleration scale $a_0$, a platform-coherence wall from the quantum-computing arc, and a canonical hydrodynamic quantity from the substrate's fluid-regime work (Paper_SCBU; ED-SC 4.x extension series).

The tiering here is specific: this is a claim that the six share one **structural origin**, argued by composition of prior results, an "A → position" verdict, not a new first-principles derivation of any one of the six scales. Each projection's numerical value remains individually inherited exactly as before: MOND's $a_0$ from Paper_029, the cross-scale operating point from its own derivation, and so on. One piece remains explicitly open: a substrate-level derivation of $\xi_{\mathrm{canonical}}$ directly from $H_0$ has not been supplied.

The sharpest consequence of treating these as one boundary rather than six coincidences is a single, falsifiable prediction: **if $H_0$ shifts**, in the sense relevant to the ongoing Hubble-tension debate, **all six projections should shift together**, in a specific, calculable way once the per-projection scaling exponents are pinned down. This is a stronger and more exposed claim than any one projection could make alone. It is distinct from, though related to, the claim that the same boundary supplies both the dark-matter and dark-energy scales (§7.4).

### 9.2 The Early Universe, the CMB, and Structure Formation

Linear structure formation in ED is **composed**, not independently derived. The growth factor inherits the substrate-graph expansion history $H(t)$ (from the inflationary spectrum and dark-energy arcs via the Route A4 substrate-parameter chain). The transfer function inherits the acoustic physics below. The primordial spectrum is inherited from the inflationary arc. Together they compose the standard matter power spectrum, $P(k,a) = D^2(a)\,T^2(k)\,P_{\mathrm{init}}(k)$, across the usual growth regimes: frozen sub-horizon growth in the radiation era, linear growth in matter domination, and late suppression as dark energy becomes relevant (Paper_ED_Cos_04).

The CMB's acoustic peaks are read the same way. The oscillation physics, the baryon-photon fluid and its sound speed, is standard, inherited cosmology, not a substrate-specific mechanism. ED supplies the substrate-graph reading of the expansion history that determines *when* recombination occurs and *how far away* it is, the two ingredients needed for the standard sound-horizon and angular-diameter-distance formulas (Paper_ED_Cos_03). The composition is form-identified; the specific numerical peak positions, the sound-horizon scale, and observables such as $\sigma_8$ all inherit standard Boltzmann-code machinery (CAMB, CLASS), and this is stated plainly in the source papers.

One candidate connection is worth naming honestly: the same substrate-parameter channel that carries $H_0$ through this composition supplies a structural link to the **$S_8$ tension**, the $\sim 3\sigma$ disagreement between CMB and weak-lensing measurements of structure growth. This is carried as an **open candidate link**, not a resolved distinguishing prediction. Whether the tension resolves through this substrate-parameter channel or through ordinary intermediate-redshift physics is explicitly left open in the source paper and is not load-bearing for anything else in this section.


## 10. The Unifying Lens: Coarse-Graining and the Layers Program

### 10.1 The Arrow Sorts the Continuum: Three Classes of Continuum Law

Continuum laws do not all sit at the same distance from the substrate. They fall into a hierarchy of coarse-grainings, substrate, then kinetic, then hydrodynamic, and ED's own coarse-graining lands squarely on the **kinetic** rung. What distinguishes which continuum law appears at that rung is not the order of a derivative or the algebraic shape of an equation, but a single structural question: **does the law keep or forget the arrow's footprint?** Commitment (P11) writes correlations, direction, and phase into structure as it happens; whether a continuum law preserves or erases that footprint determines which class it belongs to (Paper_TheArrowSortsTheContinuum).

Three classes emerge:

**Committal, structure-making laws.** These keep the arrow's footprint and are native to ED's own layer: transport, eikonal propagation, shocks, the coherent part of the Maxwell field, aggregation. The substrate builds these directly, without added ingredients.

**Dissipative, structure-erasing laws.** These forget the footprint and appear only one layer up, when a single further operator is added: the unique isotropic, local, conservative gradient-flux Laplacian. Ordinary diffusion is the direct instance; Gaussian statistics its heat kernel; finite-capacity transport its degenerate mobility. ED reaches these, but not for free.

**Reversible, structure-preserving laws.** Solitons are the clean example. They require a balance the bare substrate does not supply. Tested directly, the substrate's rule disperses rather than sustains a soliton packet; solitons appear only once an added focusing medium, another layer, is supplied. This is not a claim that solitons cannot exist, only that ED's bottom rule does not build one on its own.

This sorting is structural: a classification of what the substrate keeps or discards. Each entry still requires its own argument, measured or structural, supplied in its cited papers.

### 10.2 Where ED Reproduces the Standard Object, and Where It Honestly Doesn't

Across the physics arcs already covered, several wins are real and specific: the Born rule and Hilbert-space completion (§4), the Yang–Mills action's functional form (§6.1), the weak-field Einstein metric and its classical tests (§7.1), the MOND deep-field acceleration scale (§7.3), and horizon thermodynamics including the entropy coefficient (§8.4). Each is tiered honestly in its own section.

Within the coarse-graining program itself, the map is sharper because reproduction was tested directly rather than inferred from downstream physics.

**The coherent Maxwell field** is recovered cleanly once the coarse field is split into coherent and disordered parts. The coherent part tracks the Coulomb minimizer; the disorder is not noise but the entropy the arrow generates, concentrated near the source and falling off away from it.

**Diffusion** is not reproduced at the level of the coarse density field. The substrate's bare dynamics give ballistic transport, a genuinely different continuum object. A single tracer worldline moving through the same disordered medium *does* diffuse, a real distinction between Eulerian field and Lagrangian particle.

**Gaussian statistics** come back decisively **non-Gaussian**. The sharp diagnostic, random Fourier phases, fails. The substrate correlates phases because it builds structure; a Gaussian field is exactly one with no such structure beyond its power spectrum. This is a clean, confirmed negative.

Three further fronts remain open and are covered in their own sections: the Gleason-analog inner-product closure (§4.3), a substrate-native account of spatial dimensionality (§5.5), and the ab-initio cosmological-constant integral together with the cluster/CMB dial (§7.4, §9.2). None is glossed as resolved here.

### 10.3 Why the Walls Matter More Than the Wins

The methodological principle stated in §2.3, that consilience is structural coherence rather than evidence, and divergence is the real test, is not rhetorical. It is the discipline that produced the map in §10.2, and the coarse-graining program is where that discipline can be seen directly rather than asserted.

That discipline turns on a distinction between two things a coarse-graining can produce, which look identical from a distance: a **wall**, where the standard object is genuinely absent, and a **window**, where it is present but mixed with what the arrow writes alongside it. The coherent Maxwell field is a window. The total coarse field does not track the Coulomb minimizer, but separated into coherent and disordered parts, the coherent part tracks Coulomb exactly and the disorder is the entropy the arrow generates. The standard object was never absent; it was entangled with that entropy, and visible only in the right decomposition. This is a structural fact about how ED's coarse-graining works, signal and arrow-entropy come out together, and a program that read only the total field would record a wall where there is a window.

Gaussianity is the other kind: a genuine wall. The substrate correlates its own phases; a Gaussian field does not. This is not a disappointing result to be minimized; it is a specific, checked fact about the difference between a structure-making substrate and a structureless one. It is exactly the kind of result that could have come back the other way, and would have been reported just as plainly if it had.

A coarse-graining arc that reports only confirmations is not one whose confirmations should be trusted. This one reports the Maxwell window, the diffusion distinction, and the Gaussianity wall side by side, in the same papers, at the same level of scrutiny, and it distinguishes a wall from a window rather than declaring the first apparent failure a dead end. That pattern, not any single result, is the evidence this section offers for the program's health.


## 11. Substrate-Level Stress Tests

### 11.1 Primes as a Finite-Memory Ceiling: the Honest No

This stress test uses the integers, and the distribution of primes among them, as an external ruler, not as a phenomenon ED is meant to explain. The question is simple and sharp: **does a finite-reach, finite-memory substrate reproduce exactly the layer of structure mathematics says any such system must reproduce, and does it fail exactly where mathematics says it must fail?** The answer is yes, on both counts.

ED predicts two outcomes before the test is run. First, it should reproduce a specific **template** layer of structure: the scale-invariant information a finite residue class carries about integer spacing. Second, it should provably fail to reach past a distinct **escape** layer: the sieve parity barrier, a known obstruction in analytic number theory (Sarnak's Möbius-disjointness framework), independent of ED entirely.

Both predictions land precisely. The template quantity, 1.700 bits, is reproduced **exactly**, matching the external reference value on the nose. Past that layer, a small residual remains, roughly 0.2–0.3 bits per integer depending on modulus, and **no finite-memory function closes it**. That residual *is* the escape: the parity barrier stated in bits, irreducible to any template state no matter how much finite memory is supplied.

This is a genuine, structural **no**, and its value lies in being a *proven* wall rather than a contingent one. The obstruction is a mathematical fact, not a weakness of ED's primitives. ED lands exactly where any finite-memory structure must land. This makes the test the sharpest kind: not "did the substrate fail," but "did it correctly hit the wall mathematics says must be there."

### 11.2 Topological Charge and the Maxwell Continuum Limit

A second stress test asks whether the most basic structural properties of electric charge, quantization and conservation, emerge from the participation graph's topology rather than being posited. They do. A graph-theoretic winding number around the substrate's channel structure is integer-valued, conserved, protected by irreversibility, and obeys an integral Gauss law independent of the path used to compute it. This is the topological **skeleton** of charge, derived directly.

What the skeleton does **not** supply is the specific local $1/r^2$ Coulomb field. The per-edge configuration carrying the winding number is a gauge freedom, not a determined physical field. Forcing a $1/r^2$ falloff would require breaking properties the substrate is committed to (orientation-blindness and irreversibility), and the program does not make that move.

Recovering the continuum field itself is a distinct question, addressed in §10.2: coarse-graining does recover the coherent Maxwell field once the coherent and disordered parts are separated, with the disorder read as entropy rather than noise. The topological skeleton and the continuum-field recovery are separate results, tested separately, and neither should be mistaken for delivering the other.

### 11.3 The Determinability Boundary, Measured in Bits

The third stress test asks a more basic question: **does the substrate's own decoupling surface (the same statistical boundary involved in horizon formation, §8.1) actually sever information across itself?** Or does some unintended leakage survive?

Using a correctness-gated simulator of the substrate's selection dynamics, the answer is clean and robust: mutual information across the boundary sits at the shuffle-floor, indistinguishable from zero, while information within each side remains real and substantial. This holds across every dial tested: substrate size, mutual-information estimator, observable choice, topology (chain, tree, grid), and stability-landscape balance. The severance is architecture-independent.

One honest limit sits alongside this robustness: there is **no single intrinsic scalar** that quantifies "how much" information the boundary destroys. The qualitative zero, nothing crosses, is invariant. But the numerical gap between within-boundary and across-boundary information depends on the observable used to read it out. This dependence is real and stable, not noise.

The actual finding is therefore narrower and more precise than "a ceiling on total representable structure." It is that the substrate has a genuine, robust, observable-independent notion of **where information stops**, without a canonical number for **how much** was there to stop.


## 12. Predictions and Falsifiers

### 12.1 The Floor: Postdictions Already Cleared

Several results in this review are **postdictions** in the strict sense: they were checked against data or against known standard-physics targets *before* the substrate-level argument was made, and they passed without tuning. The weak-field factor-of-two light-bending ratio is the clearest case, confirmed directly by ray-tracing against the known 2:1 value (§7.1). Gravitational-wave speed equaling light speed, required at the $10^{-15}$ level by the 2017 neutron-star merger, is met as a structural identity of the substrate's single causal cone rather than a parameter adjusted to satisfy it (§7.2). The MOND transition acceleration's rough numerical value, a parameter-free match to the Milgrom scale within roughly ten percent, is likewise already cleared (§7.3). Newton's constant recovers the correct form, with its value inherited exactly as stated in §2.2.

Two further results belong on this floor in a slightly different sense: they reproduce known **structural targets** of standard physics rather than independently measured numbers. The Yang–Mills action's functional form, $F^2$, is now derived rather than postulated, matching the standard theory's action exactly (§6.1). And the horizon-entropy coefficient's full $1/4$, both the geometric half and the thermal $2\pi$ half, is now reproduced structurally from the substrate's own derived geometry, on equal footing with general relativity's derivation (§8.4). These are reproductions of known targets, not forecasts, and belong on the floor rather than among the bets below.

### 12.2 The Bets: Sharp, Checkable, Parameter-Free Where Possible

Distinct from the floor are the program's genuine **forward bets**, claims about data not yet settled, each with a clear falsification condition. The baryonic Tully–Fisher relation's *precise* slope, exactly four with zero intrinsic scatter in the deep-MOND regime, is a sharp, still-open test of the same mechanism whose rough numerical coincidence already cleared above, testable now against public rotation-curve catalogs (§7.3). The non-thermal correction to the Hawking spectrum, a specific, sign-definite, mass-dependent deviation from pure thermality, is untested against real data but has a near-term venue in analog-Hawking laboratory systems (§8.2). The Planck-mass remnant, a stable evaporation endpoint, is a similarly sharp, still-open bet (§8.2). The preferred-frame parameters $\alpha_1$ and $\alpha_2$ already clear existing bounds by wide margins, but remain live: any future measurement finding them at or above the bound in a sub-Planck-density environment would break the result outright (§7.5). The cosmological sector's clustering dial and the ab-initio $\Lambda$ integral remain open computations with a specific number to hit (§7.4, §9.1).

Two further bets, easy to overlook because they come from the matter-sector arc, are among the most distinctive claims in the corpus, predictions no competing framework makes at all: **no stable fundamental gauge group larger than $SU(3)$**, and **no parity-violating abelian force** (§5.1, §5.4). Both are structural rather than closed derivations, and both are falsifiable by a single discovery.

One further, differently shaped result belongs here only with a caveat: the substrate's determinability-boundary severance (§11.3) is a robust, repeatedly confirmed **internal** finding, not an externally falsifiable observational bet. It has no astronomical or laboratory venue; it is a stress test the substrate's own simulated dynamics have passed, and is reported as such rather than listed as a forecast.

### 12.3 What Would End It

The program names its own termination conditions plainly. A sub-Einstein or vanishing light-bending ratio would break the weak-field metric result outright (§7.1). A clean Newtonian result at the precision MOND's transition scale predicts a deviation, especially in wide-binary stars, would break the deep-field account, with no auxiliary field left to repair it (§7.3, §7.5). A measured $\alpha_1$ at or above $10^{-5}$, or any nonzero $\alpha_2$, in any sub-Planck-density environment would break preferred-frame safety, and because that suppression traces to the same sparse-commitment fact that keeps quantum mechanics alive, such a measurement would threaten both results simultaneously (§7.5). Late-stage black-hole evaporation observed to complete fully, with no remnant, or exactly thermal analog-Hawking radiation with none of the predicted non-thermal deviation, would break the black-hole arc (§8.2). Discovery of a stable fundamental gauge group larger than $SU(3)$, or of a parity-violating abelian force, would break the matter-sector uniqueness claims outright (§5.1, §5.4). And at the coarse-graining level, a continuum law shown to require structure the substrate's own decoupling boundary forbids from crossing, rather than merely a law not yet reproduced, would be a deeper failure than any wall already on record in §10 and §11.

None of this is hedged. A program that cannot say what observation would prove it wrong is not offering a scientific claim; this is the list of what would.


## 13. Open Fronts, Named

The discipline followed throughout this review (§2) asks that open questions be stated as plainly as closed ones. This section gathers the largest of them in one place, not as caveats scattered through earlier sections, but as explicit targets a reader should watch for future closure.

### 13.1 The Matter-Sector Residue

Gauge-group stability is genuinely derived: ED explains **which** groups can exist and **why** (§5.1, §5.4). What remains open sits one level deeper, in the **representations** those groups carry. A full classification of which channel-topology class carries which combination of spin and gauge representation has not been supplied. Only the kinematic skeleton, spin from tethering and chirality from channel topology, is grounded (§5.2).

Chirality is not carried by the substrate's transport structure: in 3+1 dimensions the surviving transport mode is **vector-like**, not chiral. The account that carries handedness instead runs through the arrow's **first commitment**, a lock unifying parity violation with baryogenesis, carried as an account rather than a closed derivation (§5.3). **Anomaly cancellation**, the hardest consistency requirement of any chiral gauge theory, remains untouched and is named plainly as open.

A fourth item belongs here: **why three spatial dimensions**. The topological argument, that only in three dimensions can a spatial link hold committed order, is solid mathematics. Whether ED's own dynamics actually reach for that structure has been tested directly. The full multi-chain participation graph *can* be intrinsically linked once cross-chain correlation is included, a real, checked positive. But the operational question, whether undoing an order actually requires the collision that structure predicts, remains genuinely open (§5.5). Reachable, not resolved.

### 13.2 Closing the Gleason-Analog Inner-Product Derivation

Standard Gleason's theorem presupposes a Hilbert space. ED's substrate-level analog does not assume the inner product it needs, but it does not fully derive it either. Given two additional postulates, distinct channels are orthogonal, and probability assignment is non-contextual across channel decompositions, the standard sesquilinear inner product follows, determined up to normalization (§4.3).

What remains open is whether either postulate reduces to the thirteen canonical primitives. The source paper states plainly that both are conjectures, not partial derivations, and no substrate-level argument has been supplied for either reduction. This is not a background curiosity; it is a **named, actively tracked research target**. Closing it, either by deriving the postulates or showing they cannot reduce further, would sharpen §4's claim that Hilbert space "emerges rather than being assumed" all the way down to the inner product itself.

### 13.3 The Λ Ab-Initio Integral and the Cluster/CMB Dial

The cosmological constant's notorious smallness is reframed structurally: it is the ratio of two scales ED already has, the cosmic rate against the Planck rate, squared (§7.4). That qualitative reframing is closed. What remains open is narrower: a **specific numerical computation**, an ab-initio substrate boundary integral that must reproduce a pinned target coefficient, sign included. That computation has not been completed, and the wrong sign or an order-of-magnitude miss would break the one-$\Lambda$ thesis outright, which is what keeps it a real claim rather than an unfalsifiable reframing.

The **cluster and CMB clustering dial** is the natural companion to this front. The cosmological sector carries a regulator dial, provably invisible to all galactic tests, and closing it requires selecting a specific dial member that simultaneously delivers dust-like clustering of the right abundance at recombination across several independent observational filters. No member has yet been selected; no CMB spectrum has yet been computed from it.

Together, the ab-initio $\Lambda$ integral and the clustering dial form the sharpest, least-finished pair of open problems in the cosmology arc. Neither is glossed as closer to resolution than it is.


## 14. What Kind of Theory This Is

### 14.1 The Case Studies Revisited: What the Walls Prove That the Wins Can't

Across this review, the program has delivered a long list of wins: the Born rule and Hilbert-space completion (§4), the Yang–Mills action's functional form (§6.1), the weak-field Einstein metric and its factor-of-two (§7.1), the MOND deep-field scaling (§7.3), the horizon-entropy coefficient's full $1/4$ (§8.4), and the substrate-cosmology boundary's multiple projections (§9.1). Per the epistemic discipline set out in §2.3, none of these is treated as evidence that the substrate is *true*. Their role is narrower and more honest: they show that the substrate's derivation chains do not fight each other, that one relational structure can be read, without retuning, into several domains of physics that share no obvious common cause in standard treatments.

The **walls** are a different kind of evidence, and this review has been as careful to collect them as the wins. The local $1/r^2$ Coulomb field is not delivered by the topological skeleton of charge alone (§11.2). The two postulates needed for the Gleason-analog argument remain unreduced conjectures (§4.3, §13.2). The full channel-topology-to-representation classification, and the operational question of whether three dimensions is something the substrate *actually reaches for* rather than merely *could* reach for, remain open (§5.2, §5.5, §13.1). And the cosmological constant's *specific number*, once reframed as the ratio of two scales ED already has, still requires an ab-initio integral that has not been completed (§7.4, §13.3).

Each wall does something a win cannot: it shows exactly where the thirteen primitives, as currently stated, stop being enough. A win shows internal coherence; a wall shows the architecture's edge. A program that can locate its own edge precisely is making a claim sharp enough to be wrong. This review's position is stated plainly: **Event Density's identity as a theory is carried more by the specific shape of its walls than by the length of its list of wins.** Two programs could reproduce the same physics and differ entirely in how honestly they can say where they stop; this one is reviewed here on the strength of having tried to find out.

### 14.2 The Tiering Discipline as the Theory's Immune System

The vocabulary of §2, four verdicts, the form-forced/value-inherited split, and the rule that consilience is coherence while divergence is evidence, is not decoration applied after the physics was settled. It is the mechanism that produced the case studies in §14.1. Without this discipline, a structural reading can quietly calcify into a claimed derivation, an inherited number can be presented as if it were forced, and walls can simply go unreported.

Every honest negative in this review exists because the tiering discipline requires claims to be stated at the point they are made, not adjusted later for narrative convenience. The non-Gaussianity of the coarse field (§10.2), the local Coulomb field the topological skeleton does not deliver (§11.2), the untouched anomaly-cancellation requirement of the chiral sector (§5.3), and the still-open continuation-free derivation of the horizon $2\pi$ (§8.4) all remain visible in the review because the discipline demands they be visible, each at its own tier rather than smoothed into the wins around it.

This is why the discipline functions as an **immune system** rather than a style guide. It filters out false wins before they can be cited downstream as load-bearing, and it makes genuine walls visible rather than letting them disappear between papers. A theory that polices its own claims this closely is not thereby more likely to be true; it is far easier to check, and far harder to defend past the point it deserves to be defended. That is the only property this review asks a reader to credit it for.

### 14.3 An Invitation: How to Break It

The fastest way to understand what this program actually claims is to try to break it. This closing section collects the sharpest ways to do so.

Find a stable fundamental gauge group larger than $SU(3)$, or a parity-violating abelian force, and the matter-sector uniqueness claims fail outright (§5.1, §5.4, §12.2). Find a weak-field light-bending ratio other than two-to-one, or a MOND-regime deviation in wide-binary stars inconsistent with the predicted transition scale, and the gravity arc fails (§7.1, §7.3, §7.5). Find late-stage black-hole evaporation completing fully with no remnant, or an analog-Hawking spectrum with none of the predicted non-thermal deviation, and the black-hole arc fails (§8.2, §12.3). Find a continuum phenomenon that genuinely requires structure the substrate's own decoupling boundary forbids from crossing, rather than one not yet reproduced, and the unifying claim of §10 fails in a way no wall currently on record does.

One item deserves a different kind of scrutiny: the horizon-entropy coefficient's derived $1/4$ (§8.4). This is not something a telescope could contradict. It stands or falls on whether the substrate's near-horizon geometry genuinely takes the Rindler form the derivation depends on, a theoretical, internal-consistency question, not an observational one. Listing it alongside astronomical falsifiers would misstate its nature; it belongs here as an invitation to check the argument, not to point a telescope somewhere.

None of this is hedged. Event Density's epistemic posture, stated in §2 and exercised throughout, is **contrast-first**: a thing is understood by what distinguishes it from what it is not, and a theory is understood, fastest and most honestly, by what would end it. This review closes by stating that list precisely and handing it to the reader rather than to itself.


