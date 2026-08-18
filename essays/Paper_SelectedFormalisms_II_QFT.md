# Selected Formalisms from the Event Density Framework
## II. Gauge Structure from Channel Multiplicity

**Allen Proxmire**
*2026-08-18. §1–§8 complete; QC and referee passes applied. Every tier is transcribed from the qft and qm-kinematics tiered-claims ledgers, not inflated; caveats are kept in their own sections.*

---

## Abstract

Event Density (ED) reads matter and forces as coarse-grained descriptions of a discrete substrate of committing events. This paper works the gauge sector. From the substrate's participation amplitude, a complex carrier $P_K = √b_K · e^{iπ_K}$, and the polarity-transport connection, ED reproduces the gauge-covariant derivative $D_μ = ∂_μ + iA_μ$ and the Yang-Mills field equations, and it forces the non-abelian gauge group: `SU(N)` follows from $N$ indistinguishable participation channels together with bandwidth conservation and unitarity, the sector's one firm derivation. The same channel structure evades the Nielsen-Ninomiya obstruction and yields spin-½ from relationality. The Yang-Mills mass gap appears in form, $Δ ∝ 1/ℓ_*$, forced given the sector's postulates; we are explicit that this is the gap's form (its coefficient is inherited), not a Clay-grade existence proof, and that continuum survival is an open wall. The multiplicity structure carries two falsifiable forward claims: no parity-violating abelian force, and no stable gauge structure beyond a bounded internal rank. We state throughout what is form-forced on which postulate and which magnitudes are inherited: couplings, masses, and the ${1,2,3}$ generation correspondence are inherited, and the Standard-Model completion (generations, electroweak symmetry breaking, anomaly cancellation) is the program's named open frontier, not a result of this paper.

---

## 1. The substrate and the participation amplitude

Event Density (ED) is a substrate ontology: beneath the continuous fields of established physics it posits a discrete, graph-like layer of committing events, and it treats the continuum laws as coarse-grained readings of that layer. The substrate is specified by thirteen postulated primitives (P01–P13, Paper_087), and every result is a *conditional structural derivation* given those primitives plus named paper-specific postulates, with *forms* derived and *magnitudes* (couplings, masses, the substrate scale) inherited from measurement. Part I developed this frame for gravity; here we take it as given and work the gauge sector. The object we need first is the substrate's amplitude.

**The participation amplitude.** At each (chain, channel, locus, time) the substrate carries two contents: a bandwidth $b_K ≥ 0$, the non-negative additive scalar of "how much participation" (P04), and a polarity $π_K ∈ U(1)$, the substrate's primitive angular variable (P09). They combine into a single complex carrier,

> $P_K = √b_K · e^{iπ_K}$   (Paper_001),

with $|P_K|² = b_K$ (algebraic) and $arg P_K = π_K$ (definitional). This is the substrate-level object that plays the role of a quantum amplitude, before any commitment has selected a single channel.

**Tier: Derived (carrier form) from P01–P04 + P09.** Two honesty notes travel with it. First, **P09 is load-bearing:** without the `U(1)` polarity there is only the real bandwidth $b_K$; the complex, angular structure is P09's contribution, not something wrung from P01–P04 alone. Second, the **square-root is a convention**, $|P_K|² = b_K$ rather than $|P_K| = b_K$. It is the convention that makes the downstream Born rule reproduce measured statistics, and the source paper labels it as such, not as a theorem. Two things this section does not lean on: the **inner product is inherited** (standard machinery, not derived from the primitives here), and the **Born rule itself is Grounded, not Derived**, resting on a further postulate (P-LinRate, that the commitment rate is linear in bandwidth) plus a frequentist reading (Paper_003). What follows uses the amplitude's *structure*, not the Born rule.

**Gauge covariance, and superposition.** Two features of the carrier drive the rest of the paper. Under a `U(1)` polarity-transport $π_K → π_K + α(u)$ (P05), the amplitude transforms covariantly,

> $P_K → P_K · e^{iα(u)}$,

which is the substrate seed of the gauge connection built in §2. And a chain participating in many channels at once carries the multi-channel state $Ψ = Σ_K P_K |K⟩$, the substrate analog of a superposition; a commitment event (P11) collapses it to a single channel, an individuation. The gauge sector is what this amplitude structure looks like coarse-grained: the connection (§2), the group it must live in (§3), the Yang-Mills equations (§4), and the mass gap (§5).

---

## 2. The gauge connection

The carrier's `U(1)` covariance (§1) is the seed of a gauge field. This section coarse-grains it to the standard gauge-covariant derivative $D_μ = ∂_μ + iA_μ$.

**The construction.** Polarity-transport along a substrate edge carries a `U(1)` phase $U_{transport}$, so the substrate "covariant difference" of a chain amplitude along that edge is $∇_{edge} Ψ = [Ψ(u′) − U_{transport}·Ψ(u)] / d_{edge}$. Coarse-grained under DCGT ($ℓ_{ED} ≪ R_{cg} ≪ L_{flow}$) this becomes $∂_μ − 𝒜_μ$, and identifying the coarse-grained polarity-transport with the continuum gauge potential, $𝒜_μ ≡ iA_μ$, yields

> $D_μ = ∂_μ + iA_μ$   (Paper_016).

**Tier: Derived (as a composition), on a construction postulate plus an inherited coarse-graining.** The honesty here is specific, and the source paper is candid about it. The finite-difference covariant form is a **construction built to match** the standard fiber-bundle form (P-Substrate-Covariant-Derivative-Construction); the coarse-graining is **inherited** (DCGT, Paper_073); the identification of coarse-grained polarity-transport with $A_μ$ is a **postulate** (P-Polarity-Connection-Match); and local-gauge invariance, the gauge groups, and the couplings are all **inherited**. So this section is a substrate-vocabulary *reconstruction* of the connection: the roughly seven naming and construction postulates across this and the earlier T17 paper encode the standard fiber-bundle structure at substrate level, and DCGT then recovers standard QED, QCD, and electroweak minimal coupling by construction. Its empirical departures from standard gauge theory live only where DCGT breaks down (near-substrate-scale, strong-gradient regimes), not at ordinary energies.

That framing is deliberate, because it isolates the one question a reconstruction cannot answer by naming: which *group* the connection takes values in. That is §3, and it is the section where the substrate forces the answer on its own.

---

## 3. The gauge group, forced by channel multiplicity

Here the substrate stops relabeling and starts forcing. Section 2 named the connection but could not say which group it lives in without importing the answer. The substrate supplies that on its own, and it is the paper's firm result.

**The derivation.** Take a rule-type family of $N$ *indistinguishable* channels. A chain's participation across them is a complex amplitude $ψ ∈ ℂ^N$, one carrier component (§1) per channel. Two primitives constrain how that amplitude is transported. Bandwidth conservation (P04) requires transport to preserve the total participation, a **norm-preserving** map, an isometry of $ℂ^N$. Invertibility of the substrate between commitments makes it **unitary**. A norm-preserving invertible map of $ℂ^N$ is a unitary, so the structure group of $N$ indistinguishable channels is

> $U(N) = SU(N) × U(1)$   (Paper_MS-II §2).

The abelian `U(1)` is the overall phase, carried by single-channel transport (the V1 kernel), and it is electromagnetism; the non-abelian `SU(N)` is cross-channel mixing (the V5 kernel). Non-abelian gauge structure is forced by channel *multiplicity*.

**Tier: Derived, the one firm upgrade in the sector.** The earlier gauge line of §2 carried the non-abelian structure only as an analogy. MS-II replaces the analogy with a derivation: given $N$ indistinguishable channels, `SU(N)` is not chosen, it is what norm-conservation and unitarity leave. What stays inherited is the *correspondence* to the Standard Model: the multiplicities ${1,2,3}$ mapping to $U(1)×SU(2)×SU(3)$, and all the couplings, are value-layer matching. The claim is exact and bounded: the substrate forces the gauge structure to be `U(N)` of some rank; which ranks the world uses is read from experiment.

**What the derivation settles, and what it does not.** A skeptic will object that "a norm-preserving invertible map of $ℂ^N$ is a unitary" is close to the definition of `U(N)`, and the objection is fair to raise. The reply is to state the content precisely. What the substrate forces is the *structure group*: given $N$ indistinguishable channels, the transport consistent with bandwidth conservation and invertibility can be nothing but `U(N)`, so the non-abelian content is fixed by multiplicity rather than imported by analogy, which is the genuine upgrade over the earlier gauge line. What the substrate does *not* settle here is imported from elsewhere: that the symmetry is *gauged*, meaning local rather than global, comes with the connection of §2 and its inherited fiber-bundle apparatus, not from the counting; and which multiplicities the world realizes, the ${1,2,3}$, is read from experiment. The firm claim is therefore bounded and exact: the structure group of a channel family is `U(N)`, forced; its gauging and its multiplet content are not this section's to derive.

**A discrete substrate that escapes the lattice no-go (structural).** The same $N$-channel transport, read as a lattice object, is a `U(N)` link variable ($U = e^{iA}$), and its plaquette holonomy is the field strength; the matter sector is a `U(N)` lattice gauge theory. That invites the sharpest objection to any discrete-substrate program, the Nielsen-Ninomiya doubling theorem: on a regular lattice chiral fermions come in mirror pairs that cancel to a vector-like world, so "the universe cannot be a discrete lattice." The theorem needs two premises, a compact Brillouin-torus and hermiticity, and ED has neither: its graph is relational (no torus) and its arrow is retarded (non-Hermitian transport), with locality intact through the finite-width kernels. The doubling no-go does not bind ED. **Tier: structural**, a coherent reading rather than a closed proof; whether the surviving fermion is genuinely chiral, rather than merely undoubled, is left open.

**Spin-½ as the signature of relationality (structural).** The four-component spinor's spin-½ is read off a fact about the ontology: an ED object is never a free point, it is a node tethered to the graph by its channels. The topological fact $π₁(SO(3)) = ℤ₂$ (a $2π$ rotation is a non-contractible loop, a $4π$ rotation contractible) is invisible for a free point but physical for a tethered one: the Dirac-belt / orientation-entanglement relation means a tethered frame is left twisted by $2π$ and only untwisted by $4π$. An object that must track that twist transforms under the double cover `SU(2)` and carries the $−1$ under $2π$. That is spin-½. Standard physics posits the spinor; ED reads it off relationality. **Tier: structural** (the `Cl(3,1)` algebra itself is inherited).

**Chirality (account, and the softest part).** Chirality $γ⁵$ is read as the handedness of commitment, but the honesty flags here are load-bearing and carried from later corrections. The evidence is a `1+1`-dimensional toy-lattice computation (retarded versus Hermitian hopping, the retarded case alone showing net spectral flow), not a property of the canonical kernel; and $γ⁵$ is a *global* object, $iγ⁰γ¹γ²γ³$, the arrow times one spontaneous global spatial orientation, not a per-channel screw. The honest downstream result is narrower and cleaner: the clean substrate is provably *vector* for every channel count, so parity violation is *necessarily spontaneous*, and *which* force is chiral is inherited (the pseudoreality of `SU(2)`), not derived. **Tier: account.** Anomaly cancellation, the deepest consistency requirement of a chiral gauge theory, is untouched (§7).

The result to carry forward is the group: `SU(N)` from multiplicity, a genuine forcing of the structure group. The corollaries above are coherent structural readings resting on it, tiered as such, and the two things this structure *forbids*, a parity-violating abelian force and a stable large gauge group, are the sector's falsifiable predictions (§6).

---

## 4. Yang-Mills, reproduced

With the connection (§2) and the group (§3) in place, the gauge dynamics follow, and they follow the way reproductions do in this framework: honestly, on a postulated action, with the genuine derivations flagged.

**Lorentz covariance.** The substrate kernel V1 is Lorentz-covariant (Paper_089), and DCGT preserves that covariance: this much is **Derived** (Paper_017), the covariance carried up from the kernel rather than imposed. One step, though, is not derived, and the source paper is careful about it. Generic coarse-graining yields the first-order diffusion operator $∂_t − D∇²$; selecting instead the *second-order* relativistic operator, the d'Alembertian $□$, is a regime commitment, the postulate **P-Lorentz-Covariant-Continuum**. So the honest split is this: Lorentz *covariance* is derived from V1, while the choice of the relativistic $□$ over the diffusion operator is postulated. The free-scalar equation the operator dresses, Klein-Gordon $(□ + m²)φ = 0$, is by the paper's own audit a **P-construction** with the mass $m$ **inherited**.

**The Yang-Mills action and equations.** Coarse-graining the substrate rule-type dynamics gives, at leading order, the Yang-Mills action $S_{YM} = −¼ ∫ F^a_{μν} F^{aμν} d⁴x$, with $F^a_{μν} = ∂_μA^a_ν − ∂_νA^a_μ + g f^{abc} A^b_μ A^c_ν$. From that action the field equations follow by the standard Euler-Lagrange variation,

> $D_μ F^{μν} = J^ν$   (Paper_019).

**Tier: the equations are Derived (the variational step) on a postulated action.** The honesty is exactly located. The action is a **coarse-graining identification** (P-YM-Action-Coarse-Graining): the substrate dynamics are *stated* to coarse-grain to the standard $F²$ action at leading order, not shown to by an explicit matching computation, and the coupling $g_{YM}$ is **inherited**. The Euler-Lagrange step from that action to $D_μF=J$ is standard mathematics, hence Derived, but it is Derived *from a postulate*. So Yang-Mills is reproduced in the same honest sense as the connection in §2: the structure is encoded in a declared action, and the equations of motion then follow rigorously. This paper claims the reproduction and the variational step, not a first-principles derivation of the $F²$ action, and not, as the next section makes emphatic, a solution of the theory.

---

## 5. The Yang-Mills mass gap, in form

The Yang-Mills mass gap (a non-abelian gauge theory has a strictly positive lowest excitation above the vacuum, despite a classically massless field) is one of the Clay Millennium problems. ED touches it, and the touch must be described exactly, because the distance between what ED shows and what the Clay problem asks is the whole content of this section.

**What ED provides: the form.** Three substrate ingredients combine: V1's finite second moment, V5's finite cross-chain bandwidth, and the irreducible quartic self-coupling of the non-abelian sector (§3). The first two set an intrinsic correlation-length floor; the quartic keeps that floor from diverging under coarse-graining. The result is a positive spectral gap whose *form* is forced,

> $Δ ∝ 1/ℓ_*$   (Paper_021),

with $ℓ_*$ the substrate correlation length. **Tier: Derived (form) / Inherited (coefficient).** The functional form is forced given the sector's postulates; the numerical coefficient comes from standard machinery (Perron-Frobenius, Glimm-Jaffe coercivity) adapted to the substrate transfer operator, not computed from primitives.

**What ED does not provide, stated flatly.** This is not a solution to the Clay problem, and the source papers say so in their own preambles. Three gaps remain open, and they are the hard ones:

- The **numerical value** of $Δ$ is not computed from first principles.
- **Continuum survival**, that the gap persists in the strict $a → 0$ limit, is *conditional on P-Profile-Rescaling*, a declared, underived postulate. This is the Clay-hard wall: without it the substrate result is a lattice-scale statement, not a continuum theorem.
- The **existence** of the continuum measure, and the reflection-positivity axiom it needs, are themselves postulated, not constructed.

The Yang-Mills arc's own capstone states the verdict we adopt: the results reach "Clay-relevance at structural-positive level," and they are **strictly below constructive proof** (Paper_023). ED obtains the gap's form and a substrate mechanism for why a floor exists; it does not prove the gap exists in the continuum. A reader looking for a claim that ED solved the mass gap will not find one here, and should not: the honest result is a forced *form* on a stack of postulates, one of which, continuum survival, is exactly the wall the Clay problem is about.

---

## 6. What the structure forbids: two falsifiable predictions

A framework earns its keep partly by what it rules out. The channel-multiplicity structure of §3 forbids two things ordinary gauge theory permits, and those prohibitions are the sector's forward bets. Neither is confirmed; they are falsifiers awaiting a test, the analog of Part I's preferred-frame kill-switch, not of its confirmed acceleration scale.

**No parity-violating abelian force.** In ED the abelian force is single-channel transport (the V1 kernel), and single-channel transport is chirality-blind, vectorlike. Only cross-channel, non-abelian mixing (V5) can be chirality-sensitive. So ED forbids a chiral abelian `U(1)`. This is a genuine prediction because general gauge theory *permits* parity-violating abelian forces; ED does not. It matches the world we see: electromagnetism, the abelian force, is vector; the weak force, non-abelian, is chiral. **Falsifier:** a confirmed parity-violating abelian force. **Honest bound:** this places parity violation in the non-abelian sector; it does not by itself derive that the weak `SU(2)` specifically is the chiral one, an assignment that is inherited (the pseudoreality of `SU(2)`) and remains open. **Tier: account + falsifiable prediction, unconfirmed.**

**No stable gauge structure beyond a bounded rank.** Model a family of same-rule-type channels as unit vectors in the internal amplitude space $ℂ^d$; they coexist stably only while mutually distinguishable. The maximum set of mutually *orthogonal* channels in $ℂ^d$ is exactly $d$ (elementary linear algebra), and beyond $d$ their mutual coherence is forced up (the Welch bound) so they interfere. So the stable channel families are ${1, …, d}$, the Standard Model's ${1,2,3}$ corresponds to internal dimension $d = 3$, and there is **no room for a stable $SU(N ≥ 4)$**. **Falsifier:** a stable fundamental $SU(N ≥ 4)$ gauge sector, or a fourth stable internal dimension. **Honest bound:** this does not derive `3`; it reduces the question to one number, *why $d = 3$*, which is itself open. **Tier: structural + falsifiable prediction, unconfirmed.**

These two are what the sector stakes on the horizon. Unlike the gravitational acceleration scale of Part I, neither has met data; they are live falsifiers, and a confirmed chiral abelian force or a stable large gauge sector would break the account.

---

## 7. What this sector does not claim

The results above are real at the tier each carries, and the tiers imply a firm list of things this paper does not deliver. Collected, so a reader need not assemble them:

- **The Standard Model is not derived.** The multiplicities ${1,2,3}$ and their mapping to $U(1)×SU(2)×SU(3)$, all couplings, all masses and mixings, are **inherited**. Why the internal dimension is `3` is a **wall**, not a result. The weak force's specific chirality is **inherited** (the pseudoreality of `SU(2)`), not derived. **Electroweak symmetry breaking, the Higgs, and fermion masses are not derived. Anomaly cancellation**, the deepest consistency requirement of a chiral gauge theory, is **untouched.** The whole completion reduces to a single open item, the spinor gate, the program's highest-leverage frontier.
- **Most of the gauge and QFT structure is reproduced by construction.** The connection (§2), the Klein-Gordon equation (§4), and the Yang-Mills action (§4) rest on a stack of naming and construction postulates that encode standard fiber-bundle theory at substrate level, so that coarse-graining recovers standard QED, QCD, and electroweak *by design*. The empirical departures live only where the coarse-graining breaks down, not at ordinary energies. The genuinely firm new result is the *group*, `SU(N)` from multiplicity (§3); the genuinely derived carry-up is Lorentz covariance from the kernel (§4). The rest of §3 (lattice form, Nielsen-Ninomiya escape, spin-½) is *structural*, and chirality is an *account* on `1+1`-dimensional toy evidence with a global $γ⁵$.
- **The mass gap is not a Clay result.** ED provides the gap's form and a substrate mechanism; it does not compute the value, does not construct the continuum measure, and its continuum survival rests on an underived postulate. The arc's own verdict is "strictly below constructive proof."
- **No confirmed prediction.** Unlike the gravitational sector, this sector has no prediction that has met data. Its two forward bets are live falsifiers, unconfirmed.
- **Nothing forced from nothing.** Every result is conditional on the thirteen primitives plus the named QFT postulates (P-Polarity-Connection-Match, P-Lorentz-Covariant-Continuum, P-YM-Action-Coarse-Graining, P-Gap-Coercivity, P-Profile-Rescaling, and the rest) and the V1/V5 kernel inheritance.

The full sector tiers are in the qft and qm-kinematics ledgers; the rest of the corpus and its ledgers cover the other sectors.

---

## 8. Appendix: tier table

| Result | § | Tier (from the qft / qm-kinematics ledgers) |
|---|---|---|
| Complex participation amplitude $P_K = √b_K·e^{iπ_K}$ | 1 | Derived (carrier form) from P01–P04 + P09; √-convention; inner product inherited |
| Born rule | 1 | Grounded (rests on P-LinRate + frequentist); not leaned on here |
| Gauge-covariant derivative $D_μ = ∂_μ + iA_μ$ | 2 | Derived (composition) on P-Substrate-Covariant-Derivative-Construction + P-Polarity-Connection-Match; DCGT inherited; groups/couplings/gauge-invariance inherited |
| Gauge group $U(N) = SU(N) × U(1)$ from channel multiplicity | 3 | **Derived** (the structure group) — the one firm upgrade; gauging + ${1,2,3}$ correspondence + couplings inherited |
| Lattice-gauge form; Nielsen-Ninomiya escape | 3 | Structural |
| Spin-½ from relationality | 3 | Structural (`Cl(3,1)` algebra inherited) |
| Chirality $γ⁵$ as the arrow's handedness | 3 | Account (1+1D toy evidence; $γ⁵$ global; parity violation necessarily spontaneous) |
| Lorentz covariance of the continuum operator | 4 | Derived (from V1); the second-order relativistic regime is postulated (P-Lorentz-Covariant-Continuum) |
| Klein-Gordon $(□+m²)φ=0$ | 4 | P-construction; mass inherited |
| Yang-Mills equations $D_μF^{μν}=J^ν$ | 4 | Derived (EL step) on a postulated action (P-YM-Action-Coarse-Graining); $g_{YM}$ inherited |
| Yang-Mills mass-gap form $Δ ∝ 1/ℓ_*$ | 5 | Derived (form) / Inherited (coeff); NOT a Clay proof; continuum survival open (P-Profile-Rescaling) |
| No parity-violating abelian force | 6 | Account + falsifiable prediction (unconfirmed) |
| No stable $SU(N ≥ 4)$ | 6 | Structural + falsifiable prediction (unconfirmed) |

*Tiers transcribed from `physics-papers/qft/QFT_TieredClaims_Ledger.md` and `physics-papers/qm-kinematics/QMKinematics_TieredClaims_Ledger.md`.*

---

*Provenance: §1–§8 built by reading Papers 001, 016, MS-II, 017, 019, 021, 023 directly, plus the two ledgers; other results cited, not re-derived. QC and referee passes applied, and the em-dash polish done (2026-08-18). The anchor (SU(N) from multiplicity, the structure group) is the one firm new derivation; the connection and Yang-Mills structure are honest reproductions on naming/construction postulates; the mass gap is form-only and explicitly not a Clay result; the two predictions are unconfirmed. Remaining before public release: a math-rendering PDF build (the inline `backtick` expressions become proper LaTeX).*
