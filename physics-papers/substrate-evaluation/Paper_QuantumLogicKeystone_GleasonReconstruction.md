# The Quantum-Logic Keystone: Reconstructing the Inner Product, the Complex Field, and Born Non-Contextuality from Commitment

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers, substrate-evaluation arc (QM-kinematics reconstruction)
**Status:** Publication draft (reconstruction). A per-axiom map of ED's commitment-lattice against the Piron–Solèr theorem, with an explicit tier and gap list. Standalone; cold-reader accessible.
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative), substrate-evaluation

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **This is a reconstruction, not a closed theorem.** The paper maps ED's primitives onto the Piron–Solèr axioms and reports, per axiom, whether the grounding is derived, selected, grounded, account-tier, or open. It does **not** claim ED's Hilbert space is proven from the primitives with full rigor.
2. **The complex field is *selected*, not derived from nothing.** ℂ is chosen from Solèr's `{ℝ, ℂ, ℍ}` by two standard reconstruction arguments grounded in ED primitives; this is an account-tier selection, not a from-scratch derivation.
3. **Channel orthogonality is *reduced to channel-distinctness given the representation*, not derived from primitives.** The operational-distinguishability argument (Move 1) shows orthogonality is not a separate axiom beyond distinctness **within** the inner-product representation; it does not establish that the representation exists, that is the Solèr package, whose technical rigor remains a residual. The only representation-independent input is P07 distinctness.
4. **The inner product is exact-as-logic, emergent-as-metric.** The proposition lattice (channels + commitment) is substrate-exact; the inner-product *metric* is built from Born statistics (a frequency limit) and is a statistical-emergent object. The Hilbert space is not claimed exact at the metric level.
5. **Two steps are account-tier, not grounded.** The recovery of standard basis-democracy from a primitive preferred basis, and the recovery of QM's multi-context structure, are applications of standard measurement theory to ED, not derivations.
6. **The distinctive interpretive claims may not be observable.** ED's two distinctive claims, einselection is primitive (not decoherence-emergent), and the Gleason/Kochen–Specker multi-context structure is emergent, have unclear observational signatures; they carry a candidate substrate-scale signature, not a delivered test, so they are labelled interpretive claims, not predictions.
7. **No new primitive is introduced.** The reconstruction uses the canonical primitives (Paper_087) and the ℂ-amplitude of Paper_001; it adds none.

---

## Abstract

The inner product is the load-bearing postulate of ED's quantum kinematics: Paper_004 needs it and, for three prior attempts, could not ground its two blocking assumptions (channel orthogonality, and Gleason-compatibility). This paper reports a reconstruction that substantially grounds it, by mapping ED's commitment-lattice (the propositions "the commitment resolves to channel-set S") onto the Piron–Solèr theorem axiom by axiom. The results, tiered honestly: channel orthogonality **reduces** to channel-distinctness (perfectly distinguishable channels are orthogonal, and ED's channels are perfectly distinguishable by exclusion of commitment, so `⟨K|L⟩=0` is not an independent postulate, *given the representation*, whose orthonormal structure the step assumes); the number field **ℂ is selected** from Solèr's `{ℝ,ℂ,ℍ}` (P09's *scalar* phase rules out ℝ by the central-scalar argument; composite cross-chain amplitudes rule out ℍ); the covering law is **candidate-grounded on the channel basis** (commitment's *irreversibility*, which naively threatens the repeatable "first-kind" measurement, in fact *enforces* it for channel measurements, a committed channel is locked; the full exchange-geometry and the phase basis remain open); orthocomplementation and irreducibility trace to primitives, atoms and the angle condition are candidates, and orthomodularity **rides with the representation**. Two structural questions resolve in a distinctive, arrow-tied way: the **preferred-basis** question (ED commits only in the channel basis, so einselection is *primitive*, and standard basis-democracy is emergent) and **physical non-contextuality** (the bandwidth is an intrinsic state property and there is one substrate commitment context, so Born probabilities are non-contextual, consistent with Gleason, while Kochen–Specker is respected because outcomes are stochastically committed, not pre-valued). Net, Paper_004's two blocking postulates are **reduced to the Solèr technical residual**: orthogonality reduced to channel-distinctness *given the representation*, and Gleason-compatibility's physical half resolved. The honest status is a **coherent reconstruction with grounded ingredients and account-tier joints**, not a closed theorem; the load-bearing residual is the technical Solèr lattice rigor that rides underneath (including under the orthogonality reduction), and the distinctive *interpretive* claims (primitive einselection, emergent multi-context) carry only a candidate, currently-unobservable substrate-scale signature. What is new and solid is the reframe: orthogonality is *operational*, not a kinematic metric fact; the complex field is *selected* by ED's scalar phase and composites; and the arrow selects the pointer basis.

---

## 1. Introduction: The Postulate That Would Not Ground

ED's quantum kinematics (Paper_004) rests on an inner product on the substrate states. In a substrate ontology this cannot simply be assumed, it must be traced to the primitives or honestly flagged as postulated. Two assumptions blocked three prior attempts: **P-Channel-Orthogonality** (distinct channels are orthogonal) and **P-Gleason-Compatibility** (the probability assignment is the Gleason/Born one). The obstruction was always the same shape: orthogonality was sought as a *kinematic metric fact* (a property of vectors), and no primitive delivers a metric.

This paper reports the reconstruction that broke the stall, by a change of question. Instead of asking "are the channel vectors orthogonal?" it asks "what does the substrate *operationally* do, and what representation must carry that?" The target is the standard quantum-logic reconstruction chain:

- **Piron (1964):** an irreducible, complete, atomistic, orthomodular lattice with the covering law, of rank ≥ 4, is the lattice of closed subspaces of a Hermitian space `V` over a division ring `K` with involution.
- **Solèr (1995):** if `V` has an infinite orthonormal sequence of equal norm, then `K ∈ {ℝ, ℂ, ℍ}` and `V` is a genuine Hilbert space.
- **Field discriminator:** a physics input selects one field.

ED's lattice `L` is the set of propositions "the commitment resolves in channel-set `S ⊆ 𝒦`", the P11 commitment outcomes. Section 3 maps each axiom to a primitive with a tier; Sections 4–6 give the three headline results (orthogonality reduced to distinctness given the representation, ℂ selected, covering law candidate-grounded on the channel basis); Sections 7–8 resolve the two structural questions (preferred basis, non-contextuality) in ED's distinctive way; Sections 9–11 give the honest status, limitations, and falsifiers.

---

## 2. Method and Load-Bearing Step Audit

**Method.** For each Piron–Solèr axiom, identify the ED primitive that would ground it and rate the grounding: **reduced** (shown non-independent *given the representation*, not produced from primitives alone), **selected** (a principled choice among a theorem's allowed options), **grounded** (a primitive supplies the axiom's operational content), **candidate-grounded** (a natural grounding whose core is established but whose full axiom is not, or is restricted to a sub-lattice), **candidate** (a natural grounding asserted but not proven), **rides-with** (holds exactly to the degree the representation does), **resolved** (a grounded core plus an account-tier reconciliation, *not* closed), **account** (standard theory applied to ED), or **open**. The reconstruction is a structural map, not an empirical experiment; the one computational input is Move 1's optimization (§4), whose analytic optimum is rigorous.

### 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives + ℂ-amplitude `√b·e^{iπ}` postulated | P | Paper_087; Paper_001 |
| Channel orthogonality `⟨K|L⟩=0` | **reduced (given representation)** | §4, reduces to P07 channel-distinctness; distinctness ⟺ orthogonality is standard *within* the representation |
| Move 1 optimum `max⟨K\|E\|K⟩ = 1−c²` | **measured/analytic** | §4, POVM optimization; =1 iff `c=0` (a fact of any inner-product space, not ED-specific) |
| Number field = ℂ | **selected (account)** | §5, P09 scalar phase rules out ℝ (central-scalar argument); composite ⊗ rules out ℍ |
| Covering law (first-kind projection) | **candidate-grounded (channel basis)** | §6, first-kind repeatability of *channel* measurements; the full exchange-geometry, and the phase basis (§7), are residual/open |
| Orthocomplementation / irreducibility | **grounded** | §3, P11 exclusivity / P10-sectors |
| Atoms / angle condition | **candidate** | §3, channels-as-atoms and operational equal-norm are natural but asserted, not proven (angle-condition equal-norm circularity still open) |
| Orthomodularity | **rides-with representation** | §3, §7, automatic for any inner-product lattice; not independent |
| Preferred basis = primitive einselection | **resolved (grounded core + account)** | §7, P11 commits only in channel basis (P07+P11); basis-democracy emergent |
| Physical (Kochen–Specker) non-contextuality | **resolved (grounded core + account)** | §8, intrinsic `b_K` (P04) + one context + stochastic commit (P11) |
| Inner-product *metric* is exact | **NOT CLAIMED** | preamble 4, metric is Born-statistical (emergent); logic is exact |
| Solèr lattice technical rigor (exchange geometry, ∞-dim) | **OPEN (residual)** | §9, rides underneath the whole reconstruction, including the §4 reduction |
| Distinctive predictions observable | **NOT CLAIMED** | preamble 6, falsifiability frontier |

Every step is P, reduced, selected, grounded, candidate, rides-with, resolved, account, measured, or explicitly open/not-claimed. Note the honest ceiling: orthogonality is **reduced** (to channel-distinctness, *given* the representation), not produced from primitives; ℂ is **selected**, not derived; the covering law is **candidate-grounded** on the channel basis only; the metric is explicitly not claimed exact; and the Solèr technical rigor is an open residual under the whole thing.

---

## 3. The Axiom Map

Rated against ED primitives, the Piron–Solèr requirements ground as follows.

- **Orthocomplementation** (every proposition has an involutive, order-reversing NOT): **grounded** in P11 *exclusivity*. Commitment resolves to one channel; `S'` = "resolves outside `S`" is involutive (not-not returns `S`) and order-reversing (larger `S` → smaller complement).
- **Irreducibility** (trivial center, no classical superselection): **grounded per sector.** It holds *within* a P10 rule-type; distinct rule-types are superselection sectors, and Piron applies per irreducible sector, physically expected.
- **Atoms** (atoms exist; every element is a join of them): **candidate**. Single channels `|K⟩` are the natural atoms (P07's minimal distinguishable propositions), but "every proposition = join of channel-atoms" is asserted, not proven.
- **Completeness** (arbitrary meets/joins): **plausible**, the proposition system is closed under AND/OR over the channel index set, which P03/P07 make well-defined.
- **Angle condition** (an infinite orthonormal sequence of equal norm): **candidate, circularity-flagged** → **discharged operationally (2026-07-10)**. P03 spatial homogeneity gives infinitely many translation-equivalent channels of *equal bandwidth*; the equal-*norm* condition is read operationally (equal commitment frequency), not metrically. *Update (2026-07-10): this reading is now discharged, the Move-1 parallel.* In the amplitude representation (Paper_001, `√b·e^{iπ}`), `⟨K|K⟩ = b_K`, so the squared norm **is** the bandwidth (P04); equal-norm `⟺` equal-bandwidth, and P03 homogeneity forces translates to equal bandwidth (`b_{K_i}=b_{K_j}`). So equal-norm reduces to a substrate fact (P03 homogeneity) *given the representation*, exactly as §4 reduced orthogonality to distinguishability — same honest boundary (given the representation, not a from-primitives metric construction). The angle condition upgrades to **grounded operationally**. Full argument: `event-density/foundations/Soler_ArcExhaustion_EqualNormDischarged_TheoremInherited.md`.
- **Covering law**: the make-or-break gate; **candidate-grounded for the channel basis**, §6.
- **Orthomodularity**: **rides with the representation**, not an independent gate; §7.

So four requirements (orthocomplementation, irreducibility, completeness, and the channel-basis covering law) trace to primitives with reasonable confidence; atoms and the angle condition are candidates with an open equal-norm residual; and orthomodularity rides with the representation. The covering law and orthomodularity are taken up in §6 and §7.

---

## 4. Headline 1: Channel Orthogonality Reduces to Channel-Distinctness, Given the Representation

The three prior attempts failed because they sought orthogonality as a metric property. The reconstruction relocates it to *operational* content instead, in two steps that never assume orthonormality, the honest ceiling being that the representation-independent input is only P07 distinctness, while the distinctness-⟺-orthogonality half is standard *within* the representation.

**(A) The operational fact (P07 + P11 + Born, no metric).** A pure channel-`K` preparation commits to `K` with frequency 1 (P11). A pure channel-`L` preparation has `b_K = 0`, so it commits to `K` with frequency 0 (P07 distinctness). So ED's distinct channels satisfy `p(K|K)=1` and `p(K|L)=0`, **perfect distinguishability**, from commitment frequencies alone, with no inner product invoked.

**(B) The theorem (derived, not assuming orthonormality).** Take candidate channel-states with a *tunable* overlap `c = ⟨K|L⟩` (we do **not** set `c=0`). The best confusion-free detection of `K` (`max ⟨K|E|K⟩` over POVM elements `0 ≤ E ≤ I` subject to `⟨L|E|L⟩ = 0`) is the projector onto the complement of `|L⟩`, giving
$$\max \langle K|E|K\rangle = 1 - c^2.$$
This equals 1 (perfect detection) **iff `c = 0`**. So non-orthogonal states are provably *not* perfectly distinguishable, and perfect distinguishability ⟺ orthogonality. The analytic optimum is rigorous.

**Conclusion.** (A) ED's channels are perfectly distinguishable; (B) perfectly distinguishable ⟺ orthogonal; therefore `⟨K|L⟩ = 0` is **not an independent postulate**, it reduces to channel-distinctness. The only representation-independent input is (A), P07 distinctness gives `p(K|L)=0`; step (B) is a standard Hilbert-space fact contributing nothing ED-specific, and the bridge from the operational frequency `p(K|L)` to the represented `⟨L|E|L⟩` is itself the Born-rule half of the representation. So P-Channel-Orthogonality collapses into {operational perfect distinguishability (P07)} + {the inner-product representation exists}. This is a *reduction* (orthogonality is not a separate axiom beyond distinctness), not a from-primitives *derivation* of the metric.

**The honest boundary (preamble 3).** Step (B) is proven *within* the inner-product representation (it uses POVMs and vectors). So the reduction assumes the *representation exists* (the Solèr package) but not orthogonality within it. The honest statement: **given the Solèr embedding, orthogonality follows from operational distinguishability, not from an independent postulate.** This removes the blocking postulate that stalled three attempts; it does not remove the embedding's own technical residual (§9).

---

## 5. Headline 2: The Complex Field Is Selected by ED's Phase and Composites

Solèr narrows the field to `K ∈ {ℝ, ℂ, ℍ}` but does not pick one. ED selects **ℂ** by two standard reconstruction arguments, each grounded in a primitive:

- **Rules out ℝ.** The argument is *not* "a real space cannot represent a phase", real-Hilbert-space QM can represent `U(1)` via an antisymmetric operator `J` with `J² = −I` (the Stueckelberg complex structure). The discriminator is subtler and about *where the phase lives*: a real division ring supplies no *central scalar* square root of `−1`, so P09's phase `e^{iπ_K}` cannot act as **field-scalar multiplication** on amplitudes, over ℝ it would have to be an operator `J` constrained to commute with all observables, not a scalar amplitude factor. ED's phase is a **scalar** amplitude factor (Paper_001, `√b·e^{iπ}`), so the field must contain `i`; hence `K ≠ ℝ`.
- **Rules out ℍ.** Quaternions are non-commutative, and the tensor product of composite systems is ill-defined over a non-commutative field (the standard obstruction to quaternionic QM). ED has composite systems with a tensor-product structure, the V5 cross-chain joint amplitudes `Ψ^{AB}` (Paper_063). For the composite `⊗` to be well-defined the field must be commutative, so `K ≠ ℍ`. (The ED-side premise (that ED *has* a genuine `⊗`) is supplied by P-Bipartite-Mapping / Paper_063, a paper-specific postulate, not one of the canonical 13.)
- **Therefore `K = ℂ`.**

> **DISCLOSURE FLAG added 2026-09-04.** The ℍ-bullet above names its ED-side premise (P-Bipartite-Mapping / Paper_063, a paper-specific postulate). **The ℝ-bullet does not name its own**, and it is the heavier of the two. Its premise is that ED's phase is a **scalar** amplitude factor, which comes from `Paper_001`'s carrier `√b·e^{iπ}` — and that is a *representational choice*: P09 supplies an angle (`U(1)` is definable as `ℝ/2πℤ` or `SO(2)`, with no reference to ℂ), and representing it as a complex scalar rather than as a rotation `J(π)` on a real 2-space is what excludes ℝ. **P09 alone is consistent with ℝ.** The tier label is right — preamble item 2 already calls this account-tier — but the ℝ-argument should name its premise the way the ℍ-argument does. **REPAIR ATTEMPTED 2026-09-04 — P03/P07 fail, a better route succeeds.** **P03/P07 do not deliver it, and the reason is worth recording so nobody retries.** The scalar-versus-operator distinction is *not* about channel mixing. Real-Hilbert QM's complex structure `J` acts **within** each channel's two-real-dimensional amplitude space; it never mixes distinct channels. So P07's intrinsic-identity commitment is simply not engaged — it forbids something the operator route does not do. And P03's translation-invariance requires only that `J` be the same at every locus, which is trivially satisfiable. **Neither primitive touches the question.** **A different argument does work, and it is grounded rather than notational.** The discriminator is not *where the phase lives* but **whether relative phase is continuously observable**, and ED's own results settle that:

1. **P09** gives each channel a *continuous* `U(1)` phase `π_K`.
2. **The corpus makes relative phase observable, continuously.** `Paper_QuadraticStrain_v1` §3.2 carries `2√(b^{(a)}b^{(b)})·cosΘ_{ab}`, and `Paper_005.5` §3.3 the double-slit `ρ = b_A + b_B + 2√(b_A b_B)·cosΔπ`. The cross-term's dependence on `Θ` is **continuous**, not two-valued.
3. **A real amplitude space cannot do that.** Superposing real amplitudes gives `(x_A + x_B)² = x_A² + x_B² + 2x_Ax_B`: there *is* a cross term, but its sign is all the freedom there is. Continuous `cosΘ` dependence requires each channel's amplitude space to be **at least two real dimensions carrying a rotation action** — that is a complex structure `J`.
4. **And a `J` commuting with all observables is ℂ** (Stueckelberg). So the effective field is complex.

**Therefore `K ≠ ℝ`, on ED's declared structure rather than on how `Paper_001` writes its carrier.** **Status, stated at the tier it earns.** This remains **account-tier**: it is conditional on the interference results of step 2, which rest on P-Quadratic-Strain and the Born-rule reading, not on the canonical thirteen alone. What it *does* fix is the circularity: the ℝ-exclusion no longer rests on `Paper_001` having written `e^{iπ}` — it rests on ED's phase being **continuously observable through interference**, which is a corpus result with its own tier and its own falsifier. **It is also now empirically anchored:** were ED's interference sign-only rather than continuous in `Θ`, ℝ would be admissible. That is a statement about the world, which the notational version was not. *Recommended: fold steps 1–4 into the ℝ-bullet above, replacing the appeal to `Paper_001`'s carrier form. Not applied here; it rewrites a headline argument and is the author's call.* See `qm-kinematics/QMKinematics_TieredClaims_Ledger.md`, addendum 2026-09-04.

This is a **selection**, account-tier (preamble 2): standard-physics discriminators applied to ED's actual structure (its scalar phase and its composites), not a from-scratch derivation. Its payoff is that ℂ is no longer a bare assumption, it is the Solèr field picked out by P09 and by the V5/063 composites.

---

## 6. Headline 3: The Covering Law, Irreversibility Enforces It, Not Breaks It

The covering law is the make-or-break gate: its operational content is the *ideal first-kind measurement* (measure an atom, get "yes," project orthogonally onto it, **repeatably**). The natural worry is that P11's *irreversibility* breaks the repeatability a first-kind measurement needs. Worked against the primitives, the worry is backwards.

1. **Orthogonal projection.** P11 commitment projects the state onto the resolved channel-atom `K`; by P11 exclusivity the discarded content is the orthocomplement `K'`. So the update is the orthogonal (Sasaki) projection onto `K`, not an arbitrary one.
2. **Repeatability, and here irreversibility helps.** Commitment *locks* the channel: it is irreversible, so the committed state stays `K`. Re-measuring "is it `K`?" returns "yes" with certainty. **Irreversibility is exactly what enforces the repeatability the covering law needs**, a locked outcome cannot drift, so the measurement is perfectly first-kind. A committed channel is the *most* repeatable kind of outcome.
3. **No intermediate propositions.** Commitment is all-or-nothing (one channel resolves; there is no partially-committed state), so it inserts no proposition strictly between `b` and `a ∨ b`, the covering geometry is not spoiled by a hidden "half-committed" layer.

**Parallel to standard QM.** ED has the standard measurement structure, unitary evolution between commitments, irreversible projective collapse at commitment. Textbook collapse is *also* irreversible, and the covering law holds there; so P11's irreversibility is the ordinary measurement-collapse irreversibility, not a special obstruction.

**Honest scope of this result: covering law → candidate-grounded for the channel-basis sub-lattice.** What is established is first-kind repeatability of *channel* measurements, and note P11 randomizes the un-selected phases, so repeatability holds specifically in the channel basis, not the phase basis. Two things remain: (i) the full covering law is a lattice-geometric *exchange* condition for *every* atom, and connecting the channel-basis first-kind grounding to that exchange geometry (plus the infinite-dimensional subtleties) is open (§9); (ii) the phase-basis version is open by construction (§7, commitment is a which-channel selection). So this grounds the operational core of the gate on the channel basis; it does not close the exchange-geometry axiom in general.

---

## 7. Structural Resolution 1: The Preferred Basis Is Primitive Einselection

Orthomodularity is not an independent gate. For the channel-only sub-lattice (propositions "resolves in `S ⊆ 𝒦`") it is a Boolean algebra of subsets, hence trivially orthomodular. For the full lattice (including the phase/superposition propositions), the orthomodular law holds automatically for the closed-subspace lattice of *any* inner-product space, so it holds exactly to the degree the representation does, and claiming it as a separate win would be double-counting.

What orthomodularity *surfaces* is the deep structural question: grounding it non-circularly for *every* proposition would require ideal first-kind measurements in the **phase basis**, not just the channel basis. But P11 is specifically a which-channel selection. This resolves, from the primitives, in a distinctive way:

- **P11 is the only collapse primitive, and it is a which-channel selection**, commitment resolves to a channel.
- **P07 channels are intrinsic** (distinct substrate objects even when bandwidth and polarity coincide), a fixed structure, not defined relative to a measurement context.
- A superposition `|+⟩ = (|1⟩+|2⟩)/√2` is **not** an intrinsic channel, and no primitive collapses to it. Committing a `|+⟩` state, P11 resolves it to `|1⟩` or `|2⟩` (Born), never to `|+⟩`.

**So ED commits only in the channel basis: the channel basis is the unique pointer basis, selected by the arrow.** Phase remains a genuine coherence observable (interference is real, a definite relative phase and a definite channel are complementary), but it is never a commitment basis. **This is einselection, and in ED it is primitive**, the arrow fundamentally selects the pointer basis, rather than it emerging from environmental decoherence as in standard QM.

**Reconciliation with observed basis-free QM (account-tier).** An apparatus is a system whose channels couple to a target observable, so at the emergent apparatus level any measurement basis is realizable (von Neumann measurement). Substrate level: a *primitive* preferred basis (intrinsic channels). Apparatus level: effective basis-democracy, recovering ordinary QM. The distinctive claim: **einselection is primitive, not decoherence-emergent**, a potential deviation from standard QM's basis-democracy near the substrate scale (preamble 6).

---

## 8. Structural Resolution 2: Born Non-Contextuality, Consistent with Both Gleason and Kochen–Specker

The physical half of Gleason-compatibility is the worry that a *genuinely different apparatus* physically changes `b_K`, making `P(K)` context-dependent (a Kochen–Specker contextuality). Three facts from the primitives settle it:

1. **`b_K(u)` is intrinsic.** P04 defines it as a bare function of `(K,u)`, a state property, with no apparatus argument. For a fixed substrate state, `P(K) = b_K / Σ b` is fixed.
2. **Einselection ⟹ one substrate commitment context.** Kochen–Specker contextuality needs the *same* projector to sit in *multiple incompatible* contexts. But ED commits only in the channel basis (§7), so at the substrate there is exactly *one* commitment context, and `P(K)` is trivially non-contextual, there is no second context to disagree with it.
3. **Outcomes are stochastically committed, not pre-valued.** ED never assigns non-contextual *definite values* (which Kochen–Specker forbids in dimension ≥ 3); it assigns non-contextual *probabilities* (which Gleason permits, and which are the Born rule). So ED is consistent with *both* theorems: Gleason (non-contextual Born probabilities from the intrinsic `b_K`) and Kochen–Specker (no non-contextual hidden values, because outcomes are stochastic commitments).

**Reconciliation (account-tier).** Different apparatus contexts arise at the emergent level and all resolve to the same substrate channel-commitment, reading the same intrinsic `b_K`, so `P(K)` is apparatus-independent. The distinctive claim: **QM's rich multi-context (Gleason/Kochen–Specker) structure is emergent in ED, not fundamental**, the same flavor as einselection-primitive / basis-democracy-emergent.

---

## 9. Honest Status: A Reconstruction, Not a Theorem

Paper_004's two blocking postulates are **reduced to the Solèr technical residual**, not independently closed: P-Channel-Orthogonality reduces to channel-distinctness (§4, *given the representation*); P-Gleason-Compatibility is derived in its bookkeeping half (P02+P04) and resolved in its physical half (§8). The keystone that was fully stuck is a coherent reconstruction. The honest tier:

- **Reduced / selected:** orthogonality (reduced to distinctness, given the representation); ℂ (selected, account-tier).
- **Grounded / candidate:** orthocomplementation and irreducibility (grounded in P11/P10); the covering law (candidate-grounded on the channel basis, §6); atoms and the angle condition (candidates, with the equal-norm residual open).
- **Rides with the representation:** orthomodularity, grounded exactly to the degree the inner-product representation is, no more.
- **Account-tier:** the recovery of standard basis-democracy from a primitive preferred basis (§7), and the recovery of QM's multi-context structure (§8). These apply standard measurement theory to ED; they are not derivations.
- **The load-bearing residual:** the **technical Solèr lattice rigor**, the exchange-property geometry Piron's projective step needs, and the infinite-dimensional subtleties, rides underneath the whole reconstruction, *including under the §4 orthogonality reduction* (which is proven inside this representation).
- **The exact/emergent split:** ED's quantum *logic* (the orthomodular lattice + covering law) is substrate-exact (from P07, P11); its quantum *geometry* (the inner-product metric) is emergent-statistical (Born frequencies). The Hilbert space is exact-as-logic, emergent-as-metric.

What is genuinely new and solid is the **reframe**, independent of the residual rigor: orthogonality is *operational*, not a kinematic metric fact; the complex field is *selected* by ED's phase and composites; and the arrow selects the pointer basis. That reframe turned a fully-stuck postulate chain into a mostly-grounded reconstruction with a distinctive, ED-native physical picture.

---

## 10. Limitations (honest)

- **The Solèr technical package is not closed here.** The exchange-property geometry and infinite-dimensional subtleties are assumed at the rigor level of the standard theorem, not re-derived; everything downstream inherits that.
- **ℂ is selected, not derived.** The discriminators (ℝ excluded by the central-scalar argument, P09's phase cannot be a *field scalar* over ℝ; ℍ by the tensor-product obstruction) are standard and grounded in ED's primitives, but they are a selection from Solèr's menu, not a from-scratch derivation.
- **Two joints are account-tier.** Emergent basis-democracy and emergent multi-context are standard measurement theory applied to ED; if they fail to *fully* recover observed QM, a substrate-scale signature would remain, which is the distinctive *interpretive* claim, its observability open.
- **The metric is emergent.** Orthogonality and the covering law are exact-as-logic; the inner-product *values* are Born-statistical, so the "Hilbert space" is exact only at the lattice level.
- **Move 1's optimum is analytic; the brute-force grid is coarse.** The `1−c²` result is rigorous analytically; the numerical check confirms at `c=0` and is grid-limited for `c>0` (reported, not load-bearing).

---

## 11. Consistency Conditions and One Candidate Empirical Signature

Most of what follows are **internal consistency conditions**, they falsify the *derivation* (a claim about ED's math), not nature. Only §11.5 (and the substrate-scale signature of §§7–8) is potentially *empirical*, and its observability is open (preamble 6). This distinction is why §§7–8's einselection and multi-context claims are labelled distinctive *interpretive* claims with a candidate signature, not delivered predictions.

### 11.1 Non-orthogonal channels are perfectly distinguishable *(internal consistency)*

**Falsifier sentence:** *A demonstration that two distinct ED channels with non-zero overlap can be perfectly distinguished by commitment frequencies would falsify the operational-orthogonality reduction (§4).*

### 11.2 The field is not ℂ

**Falsifier sentence:** *A demonstration that P09's phase is a ℤ₂ sign rather than a genuine U(1), or that ED's composite amplitudes are well-defined over a non-commutative field, would break the ℂ-selection (§5).*

### 11.3 Commitment is not first-kind

**Falsifier sentence:** *A demonstration that re-measuring a committed channel does not return the same channel with certainty (that irreversibility fails to enforce repeatability) would falsify the covering-law grounding (§6).*

### 11.4 ED commits in a non-channel basis

**Falsifier sentence:** *A demonstration that some ED primitive collapses a state onto a phase-superposition (a non-channel pointer state) would falsify primitive einselection (§7) and restore basis-democracy at the substrate level.*

### 11.5 Substrate-level contextuality *(candidate empirical, observability open)*

**Falsifier sentence:** *A demonstration that `P(K)` depends on the substrate measurement context (a genuine Kochen–Specker contextuality at the primitive level, not the emergent apparatus level) would falsify the non-contextuality resolution (§8).* This is the one potentially-empirical entry, and whether it is observable is open (preamble 6).

---

## 12. Position Statement

**ED's quantum-kinematics inner product, which stalled three prior attempts on two blocking postulates, is substantially reconstructed by mapping ED's commitment-lattice onto Piron–Solèr.** Channel orthogonality **reduces** to channel-distinctness (given the representation); the number field **ℂ is selected** by ED's scalar phase and its composites; the covering law is **candidate-grounded on the channel basis**, with commitment's irreversibility *enforcing* the first-kind repeatability there; orthocomplementation and irreducibility trace to primitives, atoms and the angle condition are candidates; and orthomodularity rides with the representation. The two structural questions resolve distinctively and are tied to the arrow: **einselection is primitive** (ED commits only in the channel basis; basis-democracy is emergent) and **Born non-contextuality holds** (intrinsic bandwidth + one substrate context + stochastic commitment, consistent with Gleason while respecting Kochen–Specker). Net, both blocking postulates are **reduced to the Solèr technical residual**: orthogonality reduced to distinctness given the representation, Gleason-compatibility derived (bookkeeping) and resolved (physical).

**What this paper claims.** A coherent, mostly-grounded reconstruction of ED's quantum logic and complex field, with orthogonality reduced to distinctness, ℂ selected, the covering law candidate-grounded on the channel basis, and two distinctive arrow-tied *interpretive* claims (primitive einselection, emergent multi-context).

**What this paper does not claim.** A closed theorem (the Solèr technical rigor rides underneath, including under the orthogonality reduction); a from-primitives derivation of orthogonality or of ℂ (the first is a reduction given the representation, the second a selection); an exact inner-product metric (the metric is Born-emergent; the logic is exact); grounded status for the two emergent-recovery joints (account-tier); or established observability for the distinctive interpretive claims (a candidate substrate-scale signature, observability open).

**Series context.** The QM-kinematics keystone of the ED program: where Paper_004 postulates the inner product, this paper reconstructs it from the primitives and reports exactly how much is grounded and what remains technical. It pairs with the minimal-ontology paper (the ℂ-field result grounds that paper's bandwidth/phase amplitude fusion) and turns on the same primitive the reduction program isolates, the arrow (P11), which here selects the pointer basis and enforces the covering law.

---

## Appendix, Glossary and Reader Map

### Glossary

- **Commitment-lattice.** The propositions "the commitment resolves in channel-set `S`", the P11 outcomes; ED's quantum logic.
- **Perfect distinguishability.** `p(K|K)=1`, `p(K|L)=0` from commitment frequencies; shown (§4) to be equivalent to orthogonality.
- **Covering law.** The lattice form of the ideal first-kind (repeatable, projective) measurement; candidate-grounded via P11 for the channel basis (§6).
- **Einselection (primitive, in ED).** The arrow selects the channel basis as the unique pointer basis; not decoherence-emergent (§7).
- **Exact-as-logic, emergent-as-metric.** The proposition lattice is substrate-exact; the inner-product metric is Born-statistical (emergent).
- **Selected (field).** ℂ chosen from Solèr's `{ℝ,ℂ,ℍ}` by ED-grounded discriminators, an account-tier selection, not a derivation.

### Reader map

*Intuition.* The quantum formalism has a few load-bearing assumptions, orthogonal alternatives, a complex amplitude, a repeatable measurement. This paper shows that in ED these are not free assumptions: orthogonality is what "perfectly distinguishable by commitment" *means*, the complex field is forced by ED having a real phase and genuine composites, and the repeatable measurement is exactly what an irreversible commitment gives you. The one thing that stays technical is the deep lattice theorem that stitches these into a Hilbert space.

*The distinctive picture.* ED comes out as a **preferred-basis quantum theory**: the arrow fundamentally picks the classical pointer basis (einselection is primitive), and the familiar basis-free, multi-context QM is what emerges at the apparatus level. That is a feature, not a bug, and, if it leaves a substrate-scale signature, an interpretive claim with a candidate (currently unobservable) test.

**Where to look next.**
- *The postulated inner product this reconstructs:* Paper_004.
- *The ℂ-field result's downstream use:* the minimal-ontology paper (bandwidth/phase fusion).
- *The complementarity (non-Boolean) gate behind the phase/channel duality:* the phase-coherence arc.

**Open work** (declared): close the Solèr technical package (exchange-property geometry, infinite-dimensional rigor); determine whether the emergent recovery of basis-democracy and multi-context is *complete* or leaves a substrate-scale signature (the falsifier frontier); and sharpen the observability of primitive einselection.

---

**End of Paper (The Quantum-Logic Keystone).**

*Substrate-evaluation arc. A per-axiom reconstruction of ED's inner product against Piron–Solèr: channel orthogonality reduced to channel-distinctness (given the representation), the field ℂ selected by ED's scalar phase and composites, the covering law candidate-grounded on the channel basis (irreversibility enforces first-kind repeatability there), and the two structural questions resolved distinctively, einselection primitive (channel basis is the unique pointer basis; basis-democracy emergent) and Born non-contextuality (intrinsic bandwidth + one substrate context + stochastic commitment, consistent with Gleason and Kochen–Specker). Paper_004's two blocking postulates reduced to the Solèr technical residual. Honest status: a coherent reconstruction with grounded ingredients and account-tier joints, not a closed theorem; the Solèr technical rigor rides underneath, and the distinctive interpretive claims carry only a candidate, currently-unobservable signature.*
