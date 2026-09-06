# How ED represents a branch — and why the collapse coefficient is missing for a structural reason, not a measurement one

**Date:** 2026-09-06
**Status:** **Structural finding.** No tier moves; it sharpens the arc's own C4 flag by naming what kind of gap it is.
**Read:** `Paper_001_PreIndividuation` §4, `Paper_007_HilbertSpace` §2.5, `Paper_Continuum_KineticLatticeGas` §3, `StateReduction_CollapseRate_ED_Derivation`.

---

## 1. ED does have a branch representation, and it is over channels

`Paper_001` §4.1:

$$\Psi^C(u,t) = \sum_K P_K^C(u,t)\,|K\rangle, \qquad P_K = \sqrt{b_K}\,e^{i\pi_K}$$

> **A superposition in ED is multi-channel participation by ONE chain at ONE locus.** `Paper_001` §4.2 says so in as many words: *"the substrate-level analog of 'quantum superposition' — a chain's substrate-level participation is distributed across **multiple channels**."*

**The index is `𝒦`. It is not the locus set.**

**And the corpus is honest about how conditional this is.** `Paper_007`'s own audit:

| step | tier |
|---|---|
| pre-individuation amplitude `P_K^C` | **D** (but on a `P (convention)` sqrt choice — sheet row 85) |
| motif algebra as a complex vector space | **P (`P-Motif-Algebra`, definitional)** |
| sesquilinear inner product | **I** — *"not derived in this paper"*, still blocked on `P-Channel-Orthogonality` |
| Hilbert space via Cauchy completion | **D conditional on** the two rows above |

**So the Hilbert space that carries superposition is conditional, and one of its conditions is open.** That is already recorded and is not news — but it matters below.

## 2. The certified substrate does not branch, and that is measured

`Paper_Continuum_KineticLatticeGas` §3, tiered **measured** — *"direct observation"*:

> **"The certified front does not branch.** One seed → exactly one active front after many steps, depositing `ρ` along a 1-D chain (a worldline). The Σ-rule is a **chain propagator, not a field-update rule**."

> **So an A1-style branch experiment cannot be run on the certified substrate as a matter of MEASURED FACT, not merely of design difficulty.** `#136` called it a design question. **It is stronger than that: there is no branch structure in the simulator to intervene on.** The simulator models the commitment dynamics, not the pre-commitment amplitude structure.

## 3. The layer seam, which is the actual finding

`StateReduction_CollapseRate_ED_Derivation` opens: *"Put a mass in a superposition of two configurations, 1 and 2 … Each configuration sources its own bandwidth field `b₁(x)` and `b₂(x)`."*

**Those are fields over space. The branches are two MASS CONFIGURATIONS.** But the threshold that fires is substrate-layer: *"the arrow … individuates them as soon as they are commitment-distinguishable"* — and commitment (P11) selects **a channel at a locus**.

| | the derivation's branches | what commitment acts on |
|---|---|---|
| object | two mass configurations | two channels |
| index | space (continuum `x`) | `𝒦` at one locus |
| layer | **emergent continuum** | **substrate** |

> **The derivation applies a substrate-layer threshold to continuum-layer branches, and the bridge between them is not stated.**

**This is the arc's own C4 flag, named as what it is.** C4 says the step *"**identifies** the branch-clock-difference energy with the known Penrose self-energy `E_G` rather than **computing** it from the ED participation fields."* **That identification is precisely the layer crossing.** So C4 is not a missing integral that someone could sit down and do — **it is a missing statement of what two spatial configurations ARE, as substrate channel content.**

> **Which is why the coefficient is missing for a structural reason rather than a measurement one.** `#136` established A1 cannot supply it. This says what would: **a substrate-layer representation of a spatial branch.** Until that exists there is no object for a distinguishability threshold to be evaluated on, so there is nothing for a coefficient to be a coefficient *of*.

## 4. A candidate bridge, offered as a sketch and not banked

**`P-Commitment-Advancement` (adopted today, `#117`) is the corpus's only channel→locus bridge**: *a commitment selecting a propagation-carrying channel advances the chain's locus; one selecting a non-propagating channel does not.*

**So channel choice generates locus displacement, and two channel-histories differing in which propagation-carrying channels committed end at different places.** That is the shape a substrate account of spatial branching would have.

**But it does not close as stated, and the tension is worth naming.** Advancement happens **at** commitment. Pre-commitment there is no advancement, so an uncommitted chain sits at **one** locus with multi-channel content. **A lump in two places needs two spatial configurations, which needs commitments to have already happened — but the branches must be UNCOMMITTED to be in superposition at all.**

**The consistent reading is that spatial superposition is not a single-chain substrate object.** It is a **coarse-grained, many-chain continuum** description: each chain has a definite locus, and `b(x)` is the ensemble object. **That is consistent with everything the corpus already says** — *"unitarity emergent, not fundamental"*, *"between commitments = reversible QM"*, and the measured non-branching front.

> **Tier: this section is a SKETCH of where a bridge would have to live, not a bridge. It is not banked and nothing downstream should cite it as one.**

## 4.5 Confirmed independently by the orthogonality route — 2026-09-06 (#139)

**The Gleason reconstruction §4 reduces `P-Channel-Orthogonality` to the fact that ED's channels are *perfectly* distinguishable, `p(K|L) = 0`, from P07.** **So if the collapse derivation's branches were channels, they would be distinguishable from the outset, `τ` would be ZERO, and collapse would be instantaneous — contradicting `τ ∝ ℏ/E_G`.** **The derivation therefore requires that its branches are not channels, which is this note's conclusion reached from the opposite end.** And it sharpens the gap: **sense 1 is BINARY (P07, perfect, standing), sense 2 is GRADED (`R` continuous) — the derivation needs graded driving binary, and that is what the missing coefficient would convert between.** `Note_Orthogonality_BinaryVsGraded_2026-09-06.md`.

## 5. What this changes

**Nothing in any tier.** The escape stands, the `τ ∝ ℏ/E_G` scaling stands as *grounded-in-kind*, locality stands.

**What changes is the shape of two open items:**

- **The collapse coefficient** is not awaiting a measurement or a harder A1 run. **It is awaiting a substrate-layer representation of a spatial branch**, which does not exist and which the certified substrate cannot exhibit (§2).
- **`#136`'s proposed branch experiment** should be re-scoped. It cannot be run on the certified substrate, and the reason is measured rather than practical.

**Stated plainly: ED's substrate represents superposition over channels, and the collapse-rate derivation needs superposition over places.** Those are different objects at different layers, and the corpus has one postulate (`P-Commitment-Advancement`) pointing at the seam between them and no construction across it.
