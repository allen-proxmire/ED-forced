> **SUPERSEDED (2026-06-28) by MS-II — *The Matter Sector from the Arrow* (`Paper_MS-II_MatterSectorFromTheArrow`).** MS-II absorbs this paper's four results (gauge groups from multiplicity, lattice-gauge form / Nielsen–Ninomiya escape, parity-violation-is-non-abelian, chirality-from-the-arrow) and adds spin-½ from relationality, the uniqueness reduction ({1,2,3} ⟺ internal d=3), and the dimensional argument (why 3 spatial dimensions). Read MS-II.

# Forces from Channels: Event-Density's Matter Sector is a Lattice Gauge Theory — Gauge Groups from Multiplicity, Parity Violation from the Non-Abelian Sector, and Chirality from the Arrow

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — Relativistic-QM / QFT line, matter-sector, Paper MS-I
**Status:** Publication draft. Conditional structural derivation within the 13-Primitive Generative System. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/qft/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **The Standard-Model gauge group $U(1)\times SU(2)\times SU(3)$ is not derived.** This paper derives that gauge groups are $SU(N)$ from channel multiplicity, and that the SM groups *correspond* to multiplicities $\{1,2,3\}$. It does **not** derive *why* the stable multiplicities stop at 3 (the uniqueness question, §7).
3. **The weak force's specific chirality is not derived.** The paper shows parity violation is confined to the non-abelian sector and that all chirality originates in the arrow's first commitment; it does **not** derive why the *weak* $SU(2)$ in particular couples to one handedness (the matter-assignment, §7.2), which is entangled with the Standard Model's own open problems (the strong-CP problem, the CKM phase).
4. **The chirality-origin result (§6) is an account, not a closed proof.** "All chirality traces to the arrow's first commitment" is built on established pieces (the baryogenesis single-template lock, the topological quantization of handedness, the time-arrow→spatial-twist "screw") plus one new synthesis; *which* handedness is selected is a contingent initial condition, as in any spontaneous symmetry breaking.
5. **No Yang–Mills action, no electroweak/Higgs sector, and no anomaly cancellation are derived** (all deferred, §7). The paper builds the gauge *connection and curvature* — the kinematics — not the field dynamics.
6. **"P05-transport re-routes channels unitarily" is a structural reading** of the polarity-transport primitive (P05 composition + P04 bandwidth conservation + invertibility between commitments), defensible but not a closed substrate proof.
7. **Masses, mixing angles, and coupling constants are inherited, not derived**; so are the multiplicities $\{1,2,3\}$ themselves.
8. **No claim that ED is the only consistent substrate ontology.**

---

## Abstract

Event Density's substrate is a participation graph on which chains propagate along **channels** (P07), each carrying a $U(1)$ **polarity** phase (P09), transported by the connection primitive **P05**. This paper asks what gauge structure that substrate carries, and answers with three structural results and one unifying account. **(1) The gauge group is the channel count.** A rule-type family of $N$ indistinguishable channels, under bandwidth conservation (P04), has structure group $U(N) = SU(N)\times U(1)$ — so non-abelian $SU(N)$ is *forced by channel multiplicity* (P08), grounding what the prior gauge-vocabulary paper (T17) obtained only by analogy; the Standard-Model groups correspond to multiplicities $\{1,2,3\}$. **(2) The substrate is a lattice gauge theory.** P05-transport of the $N$ channels — bandwidth-conserving, and invertible between commitments — is a $U(N)$ link variable; the gauge field is the per-edge generator, the field strength is the plaquette holonomy. ED's matter sector is a non-abelian lattice gauge theory on the *relational* graph (no Brillouin torus) carrying the *retarded* arrow — exactly the structure that escapes the Nielsen–Ninomiya doubling no-go that powers the "the universe cannot be discrete" objection. **(3) Parity violation is a non-abelian phenomenon.** The abelian (single-channel) coupling is chirality-blind — vector, parity-conserving (electromagnetism); only the non-abelian (cross-channel) coupling is chirality-sensitive and can violate parity. ED therefore *forbids* a parity-violating abelian force — a falsifiable prediction, since chiral abelian $U(1)$s are allowed in general gauge theory. The vector/chiral split of the forces is the single-channel/cross-channel split of the substrate's two propagation kernels. **(4) All chirality originates in the arrow.** A commitment is a handed event — it carries both a P09 phase and a channel-topology "screw" orientation — and the universe's *first* commitment imprints both a matter/antimatter reference (the phase) and a parity reference (the screw), locked globally and made maximal by their quantized, topological character. Parity violation and the matter/antimatter asymmetry are then two attributes of one first-arrival imprint, correlated but distinct, reproducing C and P violated separately with CP only partial — unifying the chiral-gauge structure with baryogenesis under the substrate's signature commitment, the arrow. The paper does **not** derive the SM gauge group, the weak force's specific chirality, or the Yang–Mills dynamics; the chirality result is an account, not a proof. What ED's *structure* forces — gauge group from multiplicity, lattice-gauge-theory form, parity-violation-is-non-abelian — is independent of those open quantities.

---

## 1. Introduction

### 1.1 What this paper does

The prior gauge paper in this program (T17, Paper_015) was explicit that it performed a *substrate-vocabulary rewrite* of fiber-bundle gauge theory: it *named* channels the fiber, P05 the connection, and $U(1)$ (P09) the structure group, and obtained non-abelian structure only "by substrate-level analogy." This paper derives what T17 named. In order of decreasing solidity:

1. **The gauge group is $SU(N)$ from channel multiplicity** (§3) — derived from bandwidth conservation on the $N$-channel amplitude.
2. **The substrate is a lattice gauge theory** (§4) — P05-transport is a $U(N)$ link variable; on the relational graph with the arrow, it escapes Nielsen–Ninomiya.
3. **Parity violation is confined to the non-abelian sector** (§5) — the abelian force is necessarily vector.
4. **All chirality originates in the arrow's first commitment** (§6) — an account unifying parity violation with the matter/antimatter asymmetry.

The hard structural results (1–3) lead; the chirality account (4) closes. The frontier — why the multiplicities stop at $\{1,2,3\}$, and why the weak force in particular is chiral — is left open and honestly marked (§7).

### 1.2 Why this matters

The sharpest objection to any discrete-substrate program is the **Nielsen–Ninomiya theorem**: on a regular lattice, chiral fermions are forbidden — they come in mirror-paired doublers that cancel, leaving a parity-symmetric (vector-like) world. Since the real world is chiral (the weak force is parity-violating), "the universe cannot be a discrete lattice" follows. This paper meets the objection head-on. ED *is* discrete, but its matter sector is a lattice gauge theory on a **relational** graph — which has no Brillouin torus — carrying a **retarded arrow** — which makes the transport non-hermitian. Both are exactly the premises Nielsen–Ninomiya requires and ED lacks. The doubling no-go does not bind ED, and chirality is not merely *permitted* but turns out to be the matter-sector fingerprint of the same primitive — the arrow — that the gravity line (Paper GR-II) identified as the source of the gravitational "khronon." One signature commitment; two fingerprints.

### 1.3 How this fits the arc

- **Inherited:** T2 (Paper_103, the unique four-component $\mathrm{Cl}(3,1)$ spinor) and T4 (Paper_106, the Dirac equation form); Paper_090 (the V5 cross-chain kernel — its gauge-compatibility and chirality-sensitivity); the baryogenesis single-template / first-arrival lock (the R4 mechanism).
- **Superseded in part:** T17 (Paper_015) — its postulated "P05 = connection" and "channels = fiber" are *derived* here (§4), and its non-abelian "analogy" is *replaced* by the multiplicity derivation (§3).
- **Downstream / open:** the uniqueness of $\{1,2,3\}$, the weak matter-assignment, the Yang–Mills action, electroweak/Higgs, anomalies (§7).

### 1.4 Conventions and regime of validity

Channels and their multiplicity are substrate-level objects; the gauge fields are stated in the continuum (DCGT) limit. The structural results (1–3) are **multiplicity-independent in form** — they do not depend on the *value* $\{1,2,3\}$, only on the existence of finite multiplicity. No strong-coupling, no Higgs sector, and no cosmological claim is made. The chirality account (§6) is a linearized/structural statement about the first commitment, not a dynamical simulation.

---

## 2. Primitive Inputs

**Substrate primitives (postulated, Paper_087):** P02 (participation adjacency), P04 (bandwidth — a conserved, additive, non-negative scalar; **load-bearing**), P05 (polarity-transport along edges — the connection), P07 (channel structure — the directional pathways), P08 (multiplicity — the count of same-rule-type channels), P09 ($U(1)$-valued polarity — the phase), P11 (commitment irreversibility — the arrow).

**Inherited from within the program:**

- **T2 (Paper_103):** the unique four-component $\mathrm{Cl}(3,1)$ spinor (the spin double-cover is a Clifford-algebra structure, not a P09 structure).
- **T4 (Paper_106):** the Dirac-equation form (the substrate→Dirac chain's spinor-construction was left open there; §5.3 here locates it in channel topology).
- **Paper_090 (V5):** the cross-chain correlation kernel — gauge-compatible ($K_{V5}\to e^{i(\alpha(u_A)-\alpha(u_B))}K_{V5}$), retarded, and (via the baryogenesis coherence-functional analysis) **chirality-sensitive**, in contrast to the single-chain kernel V1, which is chirality-blind.
- **The first-arrival lock (R4):** the baryogenesis result that a continuously-degenerate P09-phase circle is broken at first arrival and then globally enforced by V5 phase-coherence under a no-slack capacity condition.

**Inherited mathematical input (standard):** $U(N)$ as the group of bandwidth-(norm-)preserving transformations of $\mathbb{C}^N$; lattice-gauge-theory link variables, plaquette holonomy, and the Wilson-loop; the Nielsen–Ninomiya theorem and its premises (a compact Brillouin torus and hermiticity).

**Value-layer inputs (inherited):** particle masses, mixing angles, and the specific multiplicities $\{1,2,3\}$.

---

## 3. The Gauge Group is the Channel Count

### 3.1 The channel bundle

Assemble the substrate into a bundle, grounding T17's named identifications. The **base** is the emergent spacetime (the coarse-grained loci). The **fiber** at a locus is the channel space — for a given rule-type family, the set of that family's channels (P07), each carrying a $U(1)$ phase (P09). The **connection** is P05 (§4). The **gauge group** is the structure group: the group of fiber transformations that P05-transport can induce while preserving substrate structure. The question "which gauge group?" thus reduces to "what is the symmetry of the channel fiber?"

### 3.2 $N$ indistinguishable channels give $U(N)$

Let a rule-type family have **multiplicity $N$** (P08) — $N$ channels of the *same* rule-type available at a locus. A chain of that family distributes its participation amplitude over them,
$$\psi = (\psi_1,\dots,\psi_N)\in\mathbb{C}^N,$$
the superposition-over-channels that, before a commitment, is the chain sitting across its available same-type channels. Two substrate facts fix the fiber's symmetry:

1. **Indistinguishability.** The $N$ channels share a rule-type label, and the rule-type label is the only substrate invariant distinguishing channel families; *within* a family there is no substrate fact distinguishing channel $i$ from channel $j$. Any relabeling or mixing among them is therefore a symmetry.
2. **Bandwidth conservation** (P04). Bandwidth is a conserved additive scalar, so the total participation $\sum_i|\psi_i|^2$ is preserved.

The transformations of $\mathbb{C}^N$ that mix the components and preserve $\sum_i|\psi_i|^2$ are exactly the **unitary group $U(N)$**, and
$$U(N) = \big(SU(N)\times U(1)\big)\big/\mathbb{Z}_N,$$
where the $U(1)$ factor is the *common* P09 phase (the abelian phase T17 already had) and the $SU(N)$ factor is the *traceless* mixing of the $N$ indistinguishable channels. **The non-abelian gauge group $SU(N)$ is therefore forced by channel multiplicity** — it is the symmetry of $N$ degenerate channels, made unitary by bandwidth conservation. This is the explicit derivation T17 §6.1 reached only "by analogy," and the multiplicity content P08 flagged as needing treatment.

### 3.3 The Standard-Model correspondence

Indexed by multiplicity:

| multiplicity $N$ | structure group | Standard-Model force |
|---|---|---|
| 1 | $U(1)$ | electromagnetism / hypercharge |
| 2 | $SU(2)\times U(1)$ | weak (doublets) |
| 3 | $SU(3)\times U(1)$ | strong / color (triplets) |

So $U(1)\times SU(2)\times SU(3)$ corresponds to channel-family multiplicities $\{1,2,3\}$ — the Standard Model's singlets, doublets, and triplets. *This is a correspondence, not a derivation:* §3.2 gives $SU(N)$ for any $N$; why the stable families are exactly $\{1,2,3\}$ is open (§7.1).

---

## 4. The Substrate is a Lattice Gauge Theory

### 4.1 From global symmetry to gauge field

A *global* symmetry is not a force. For $SU(N)$ to be a **gauge** symmetry — with a connection, parallel transport, and field strength — transport must rotate among the $N$ channels *position-dependently*, so that transport around a closed loop need not return to the identity.

### 4.2 P05-transport is a $U(N)$ link variable

Transport one locus to the next maps the amplitude $\psi(u)\in\mathbb{C}^N$ to $\psi(u')\in\mathbb{C}^N$. Three substrate facts fix the form of that map:

- **Channels re-route through the graph** (P07 composition: channels branch and merge; the $N$ channels at $u$ connect to a different arrangement at $u'$), so the map mixes components.
- **Bandwidth is conserved** (P04), so the map is an isometry of $\mathbb{C}^N$.
- **Between commitments the map is invertible** — commitment (P11) is the *only* non-invertible event; between commitments the evolution is reversible.

An invertible isometry of $\mathbb{C}^N$ is unitary, so
$$U_{uu'}\in U(N),\qquad \psi(u') = U_{uu'}\,\psi(u).$$
A $U(N)$ matrix on each edge **is** a lattice gauge link variable. P05-transport of multiplicity-$N$ channels is a $U(N)$ lattice connection — not by analogy, but because bandwidth-conserving invertible re-routing of $N$ indistinguishable channels is exactly a unitary link map. *(The structural reading: that P05 re-routes channels rather than acting diagonally is read from P07 composition; it is defensible, not a closed proof.)*

### 4.3 Gauge field and field strength

- **Gauge field** $A$: the generator of $U_{uu'}=\exp(iA_{uu'})$, $A\in\mathfrak{u}(N)$. The $SU(N)$ part is the non-abelian gauge field; the $U(1)$ part is the common P09 phase.
- **Field strength** $F$: the **plaquette holonomy** $U_\square=\prod_{\text{loop}}U_{uu'}$. If $U_\square\neq\mathbb{1}$, transport around the smallest loop rotates the channel amplitude — non-zero curvature, a genuine gauge field rather than pure gauge; the non-commutativity of $SU(N)$ link variables makes $F$ non-abelian ($F = dA + A\wedge A$).
- **Holonomy** $U_C=\prod_C U_{uu'}$: the substrate realization of the holonomy that the Aharonov–Bohm (Paper_010) and Berry-phase (Paper_009) analyses already use as inherited standard mathematics. This paper grounds it — the connection whose holonomy those papers invoke *is* the P05 re-routing of channels.

### 4.4 On the right kind of lattice — the Nielsen–Ninomiya escape

ED's channel sector is therefore a $U(N)$ lattice gauge theory, and two features make it the *right* kind:

- It lives on the **relational participation graph**, not a regular periodic lattice — so there is **no Brillouin torus**. The doubling no-go's topological engine (the sum of Weyl-point chiralities over the compact torus) has no torus to sum over.
- Transport carries the **retarded arrow** (P05 → V1 retardation): the link variables are forward-directed and the structure is **non-hermitian**.

Both are exactly the Nielsen–Ninomiya premises ED lacks (a compact Brillouin torus; hermiticity). So the doubling no-go does not bind ED — the discreteness objection of §1.2 is answered structurally — and the gauge sector ($SU(N)$ from multiplicity) and the fermion sector (the spinor as channel topology, §5.3) are one and the same lattice gauge theory. Between commitments the link variables are unitary; at a commitment (P11) the chain's distribution over the $N$ channels collapses to one — a non-unitary projection. The gauge field lives in the unitary between-commitment transport; commitments are where the gauge-covariant amplitude is read out.

---

## 5. Parity Violation is Non-Abelian

### 5.1 Two kernels, two chiralities

ED has two propagation kernels. **V1** is the single-chain vacuum kernel (Paper_089); **V5** is the cross-chain correlation kernel (Paper_090). The baryogenesis coherence-functional analysis fixes their chirality behavior: **V1 is chirality-blind** — its propagation is independent of the chain-arrow chirality $\chi_C$ ($\partial_{\chi}\mathcal{K}_{V1}=0$) — while **V5 is chirality-sensitive** — its cross-chain coupling depends on the phase relationship $\chi_C-\chi^*$, because V5 couples to P09 phase *differences* and chirality is itself such a difference. V1 (single-chain) cannot see a phase difference; V5 (cross-chain) is built on them.

### 5.2 The result

Combine §3–§4 with §5.1:

- The **abelian** force is the single-channel coupling, carried by the chirality-blind V1 → the same coupling on both handednesses → **vector → parity-conserving.**
- The **non-abelian** force is the cross-channel coupling, carried by the chirality-sensitive V5 → can distinguish handedness → **can be chiral → can violate parity.**

> **In ED, parity violation can occur only in a non-abelian (cross-channel) force. An abelian force is necessarily vector — it cannot violate parity.**

This is a falsifiable structural prediction: general gauge theory *permits* chiral abelian $U(1)$s; ED forbids them, because the abelian coupling is the chirality-blind V1 kernel. It matches the low-energy world — electromagnetism (abelian) is vector; the weak force (non-abelian) is chiral. The vector/chiral split of the forces is the V1/V5 = single-channel/cross-channel split. V5 is the chirality-bearing kernel *because* it is the cross-channel (non-abelian) one.

### 5.3 Where the spinor's handedness lives

This also resolves a puzzle in the substrate→Dirac chain (T4, Paper_106 §3.7). The spin double-cover is a $\mathrm{Cl}(3,1)$ structure (T2), not a P09 structure: a $U(1)$ phase winds by integers, while spin-$\tfrac12$ needs the $SL(2,\mathbb{C})$ half-turn. So the spinor's handedness ($\gamma^5$) is realized by **channel topology** (the route P07 §7.4 names for $U(1)/SU(2)/SU(3)$), and **P09 is the vector $U(1)$** — the phase that dresses the topological skeleton, the electromagnetism-like coupling. This is why a naive "transport route" to chirality comes out vector-like in $3{+}1$ dimensions: transport is the V1 (vector) kernel; the handedness was never going to come from there. It comes from the channel topology, and which handedness is selected is §6.

---

## 6. The Arrow is the Origin of Chirality

> **Correction (2026-07-10), retiring the P-imprint half of this section.** The account below that the first commitment imprints *both* a matter/antimatter reference (C) *and* a parity reference (P) — the "screw → a parity reference" of §6.2 — **over-reads its P-half.** ED natively selects the **C** reference but **not** a native P (parity) reference. The successor result: the clean substrate is **provably vector for every channel-count** (a transport-level theorem), so parity violation is **necessarily spontaneous**, and *which* force is chiral is **inherited** (representation-theoretic, the pseudoreality of `SU(2)`), not derived. The `γ⁵` locus is also **global** (`γ⁵ = i γ⁰γ¹γ²γ³` = the arrow times the one spontaneous global spatial orientation), not a per-channel "screw." See `physics-papers/substrate-evaluation/Paper_CleanSubstrateVector_ParitySpontaneous.md` and MS-II §4.2 (which carries this correction inline). The C-imprint half, and "all chirality traces to the arrow," stand; only the native-P claim is retired.

The structural results (§3–§5) place *where* chirality can live (the non-abelian/V5 sector, the channel topology). This section accounts for *where it comes from*. It is an account built on established pieces plus one synthesis, not a closed proof.

### 6.1 A commitment is a handed event

The **arrow** (P11 commitment-irreversibility; the strictly-retarded V1) is ED's only handedness-breaking primitive — it breaks time-reversal. A commitment carries (i) a P09 phase and (ii) a channel-topology orientation. The arrow makes both *directed*: the commitment advances time and, correlated with that advance, twists the P09 phase relative to the channel — a **screw**, whose handedness is a spatial handedness (the mechanism by which a time-handedness becomes a spatial one). With §5.3 (handedness = channel topology), the screw's sense is the spinor's chirality.

### 6.2 The first commitment imprints both references

The baryogenesis lock (R4) establishes that a continuously-degenerate P09-phase circle is broken at first arrival and then globally enforced (V5 phase-coherence forecloses any second admission under the no-slack condition). The **first commitment** — the first instance of the arrow acting — has both a phase and a screw orientation, and if it sets the global reference for each (as R4 has it do for the phase), it sets both at once:

- its **P09 phase** → the global $\chi_C$ reference → the **matter/antimatter** selection (C-type);
- its **channel-topology screw** → the global helicity reference → the **parity** selection (P-type).

### 6.3 Correlated but distinct; and maximal

One event, two attributes, two references: the C-lock and the P-lock are *the same first-arrival event* — hence **correlated** — but *different attributes of it* — hence **distinct**. This reproduces the observed pattern: C and P violated *separately*, CP only *partially*. And because handedness is **topological** (a quantized channel-topology class, not a tunable dial), the selection is all-or-nothing: the imprint is **maximal** on both faces — a complete matter/antimatter selection and maximal ($V{-}A$) parity violation — from one lock.

### 6.4 The unification

> **Parity violation and the matter/antimatter asymmetry are two faces of a single event — the first commitment's handedness imprint — and that imprint is the arrow acting for the first time.**

The arrow is thus the source of *all* chirality in ED. In the gravity line (Paper GR-II) the same arrow is the source of the gravitational "khronon," the preferred-foliation scalar; the arrow also underwrites the position-dependent clock and the density-suppressed preferred-frame parameters. Chirality is its matter-sector fingerprint. One one-way commitment; the khronon in gravity and the handedness of matter in the same stroke.

---

## 7. The Residual and the Open Frontier

### 7.1 Why $\{1,2,3\}$? — open

§3 gives $SU(N)$ for any $N$; the Standard Model stops at 3. Why the stable channel-families are exactly $\{1,2,3\}$ — three forces, of these sizes and no larger — is not derived here. The natural place to look is **channel-family stability**: the multiplicity of a same-rule-type family is "usually small" (P07), bounded by whatever coherence condition keeps $N$ indistinguishable channels mutually stable, and a stability calculation that caps $N$ and populates $\{1,2,3\}$ would close the question. The bound, if it exists, is internal — a property of channel-family coherence — and its value is open.

### 7.2 Why the weak force specifically is chiral — open

§5 confines parity violation to the non-abelian sector, but both the weak ($SU(2)$) and strong ($SU(3)$) forces are non-abelian, and the strong force is *vector*. So chirality is set by the matter **handedness-assignment** — which channel-topology classes a force couples — not by the group itself. Why the weak $SU(2)$ couples to one handedness while the strong $SU(3)$ couples to both is not derived here, and it is entangled with the Standard Model's own open problems (the strong-CP problem; the CKM-phase origin of CP violation). §6 supplies the global handedness *reference*; it does not single out the weak force as the one that couples to it asymmetrically.

### 7.3 Deferred: dynamics, electroweak, anomalies

The Yang–Mills *action* (why the gauge-field dynamics are $\propto F^2$) — built from coarse-graining the plaquette structure (lattice → continuum via DCGT) — is not derived. The electroweak/Higgs sector is beyond the V1/V5 split (chiral hypercharge and symmetry breaking are not captured by the simple abelian/non-abelian distinction). Anomaly cancellation is untouched, and is the hardest piece.

---

## 8. The Wedge — Where ED Predicts

1. **No parity-violating *abelian* fundamental force** (§5.2). Electromagnetism-type (abelian) forces are vector. The sharpest clean prediction — general gauge theory permits chiral abelian forces; ED forbids them.
2. **Gauge-group rank = channel multiplicity** (§3). Fundamental forces come in $SU(N)\times U(1)$ families indexed by an integer multiplicity.
3. **One lattice gauge theory unifies gauge fields and matter** (§4): the gauge fields (channel multiplicity) and the fermions (channel topology) are the *same* structure on the relational graph — the discreteness objection answered, not evaded.
4. **Parity violation and the matter/antimatter asymmetry share one origin** (§6): the first-arrival imprint. A *unification* claim — they are not independent.

---

## 9. Falsification Criteria

### 9.1 A parity-violating abelian force
**Falsifier sentence:** *Discovery of a fundamental, parity-violating abelian ($U(1)$-type) gauge force would falsify §5.2 — that the abelian coupling is the chirality-blind single-channel kernel and is therefore necessarily vector.*

### 9.2 A non-multiplicity gauge group
**Falsifier sentence:** *A fundamental gauge force whose group is not of the channel-multiplicity form $SU(N)\times U(1)$ — for instance an exceptional-group gauge force not reducible to a multiplicity structure group — would falsify §3.*

### 9.3 Doubling on the relational lattice
**Falsifier sentence:** *A demonstration that ED's relational-graph, retarded-arrow lattice gauge structure nonetheless forces fermion doubling (a vector-like spectrum) would falsify the §4.4 Nielsen–Ninomiya escape and the discreteness reply.*

### 9.4 Uncorrelated C and P
**Falsifier sentence:** *A demonstration that the matter/antimatter asymmetry and the parity-violation handedness are independent — not a shared first-arrival imprint — would falsify the §6.4 unification.*

---

## 10. Position Statement

**What this paper claims.** Event-Density's matter sector is a non-abelian **lattice gauge theory** on the relational participation graph; its gauge groups are $SU(N)\times U(1)$ **from channel multiplicity** (P08) under bandwidth conservation (P04); the relational-graph-plus-retarded-arrow structure **escapes the Nielsen–Ninomiya** doubling no-go, answering the discreteness objection; **parity violation is confined to the non-abelian sector** (the abelian force is necessarily vector, a falsifiable prediction); and **all chirality originates in the arrow's first commitment**, which imprints both the matter/antimatter and parity references — unifying parity violation with baryogenesis. The structural results are independent of the open quantities.

**What this paper does not claim.** It does not derive the Standard-Model gauge group (why the multiplicities stop at $\{1,2,3\}$ is open); it does not derive the weak force's specific chirality (the matter handedness-assignment is open); it does not derive the Yang–Mills dynamics, the electroweak/Higgs sector, or anomaly cancellation (deferred); §6 is an account, not a closed proof, and the selection direction is a contingent initial condition (spontaneous symmetry breaking). $\kappa$, masses, mixings, and the multiplicities themselves are inherited.

**Series context.** Paper MS-I of the matter-sector line, companion to the gravity line (Paper GR-II): the arrow's fingerprint in matter (chirality) as the khronon is its fingerprint in gravity. The remaining work — the multiplicity uniqueness via channel-family stability, the weak matter-assignment, the Yang–Mills action, the electroweak sector, and anomalies — is declared open (§7).

---

## Appendix: Cross-References and Glossary

### Cross-references
- **Position paper:** Paper_087.
- **T2 (Paper_103):** $\mathrm{Cl}(3,1)$ four-component spinor (inherited).
- **T4 (Paper_106):** Dirac equation form (§5.3 locates its open spinor-construction in channel topology).
- **T17 (Paper_015):** gauge-vocabulary rewrite (superseded in part — §3, §4).
- **Paper_090:** V5 cross-chain kernel (gauge-compatible, chirality-sensitive).
- **Paper_089:** V1 single-chain kernel (chirality-blind, the single cone).
- **Paper_010 / Paper_009:** Aharonov–Bohm / Berry-phase holonomy (grounded in §4.3).
- **Paper GR-II:** the gravity line — the arrow's gravitational fingerprint (the khronon).

### Glossary
- **Channel (P07).** A stable, directional, rule-type-selective pathway in the participation graph — "a direction a chain can keep going in."
- **Multiplicity (P08).** The count of same-rule-type channels in a region; the source of the gauge-group rank $N$.
- **Polarity / P09.** The $U(1)$ phase carried along a channel — the vector ($U(1)$) gauge coupling (electromagnetism).
- **V1 / V5 kernels.** Single-chain (chirality-blind, abelian, vector/EM) and cross-chain (chirality-sensitive, non-abelian, where parity violation lives).
- **Structure group / link variable.** The $U(N)$ symmetry of $N$ indistinguishable channels (structure group); the per-edge $U(N)$ transport (link variable).
- **Plaquette holonomy.** Transport around the smallest loop; the lattice field strength.
- **Screw.** A commitment's correlated time-advance and P09-phase twist; the mechanism turning the time-arrow into a spatial handedness.
- **First-arrival imprint.** The first commitment's setting of the global matter/antimatter (phase) and parity (screw) references; locked by R4, maximal because topological.
- **C-type / P-type chirality.** Matter/antimatter (charge-conjugation, the P09 phase) vs parity (helicity, the channel topology) — two attributes of the one imprint.

### Reader map and open work
**Where to look next.** Spin/Dirac structure: T2/T4. The V5 kernel: Paper_090. The first-arrival lock: the baryogenesis arc (R4). The arrow's gravitational fingerprint: GR-II.
**Open work (declared, §7).** The multiplicity uniqueness $\{1,2,3\}$ via channel-family stability; the weak matter-assignment; the Yang–Mills action (lattice → continuum); the electroweak/Higgs sector; anomaly cancellation.
