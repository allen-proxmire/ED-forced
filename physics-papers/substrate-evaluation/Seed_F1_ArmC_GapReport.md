# F1 Arm C — Seed Prompt (the gap report)

*Written 2026-09-05 for `Protocol_F1_ColdReconstruction_TwoArm.md`. **Paste §"THE PROMPT" verbatim.** Everything outside that block is protocol notes and must not be sent.*

---

## Why this arm exists, and why it is the one worth running

Arms A and B asked *"can a model generate ED?"* **That question was never open** — the answer was no before either arm ran, and no is what both returned. What they produced that was worth having came out sideways: every run, unprompted, named soft spots in ED that the corpus's own ledgers already list. **Three of the four items now in research target #24 came from models that had never seen the corpus.**

**Arm C asks for that output directly.** Same three Stage-0-clean families, same 38 lines, byte-identical axioms. Only the task changes: from *derive gravitation* to *derive what you can, then tell us precisely what you would need to get further, and rank it.*

**This plays to what the runs demonstrably do well** — the arm-A/B evidence is that these models are accurate auditors of a stated axiom set and poor generators from one. It also returns something usable regardless of outcome, which neither A nor B did.

## Seed-design decisions

1. **The axiom block is copied programmatically from `Seed_F1_ArmB_38Lines.md`**, so it is byte-identical by construction rather than by care. Arm C is arm B with a different question, nothing else.
2. **The classification (i)–(iv) is the point of the arm.** *Missing definition / missing structure / genuine postulate / hard derivation* is exactly the distinction the corpus cannot make for itself, because from the inside every gap looks like work not yet done. **(iii) versus (iv) is the judgement worth paying for.**
3. **"What it unlocks" makes the answers rankable.** A gap that blocks one result and a gap that blocks four should not come back looking the same.
4. **The two honesty instructions are load-bearing, not decoration.** The first blocks the failure arm A showed once — a model silently sharpening a loose axiom and then reasoning from its own version. The second gives the run permission to say *structural problem*, not *missing piece*; without it, a task that asks "what would you need?" pressures every answer into the shape of a request.
5. **No targets are named and no ED terminology is leaked.** The prompt does not mention the front-null step, the `N(R)` count, `a₀`, `H₀`, MOND, or any paper.

---

## THE PROMPT

```
You are given a proposed pre-quantum substrate ontology, stated as a set of
primitive commitments, inherited constants, and domain-specific postulates.
Treat all of these as axioms: they are posited, not derived, and you should
not attempt to justify them.

PART 1 — THE SUBSTRATE PRIMITIVES

P01 — Event-density layer existence.
A pre-quantum substrate exists as a primitive structural layer. It is not a
Hilbert space, not a smooth manifold, not a field theory: it is a discrete,
graph-like structure. Below this layer no further substrate structure is
resolved.

P02 — Participation as primitive relation.
A chain C (a persistent forward-causal sequence of substrate events)
participates in a channel K at substrate locus u at substrate time t.
Operational content: the four-tuple (C, K, u, t). Chains are derived composite
structures; participation is the primitive relation.

P03 — Channel and locus indexing; spatial homogeneity.
The substrate carries a discrete channel index set and a discrete locus index
set indexed by graph positions u. The participation graph is spatially
homogeneous: substrate operations are invariant under translation of the locus
index, and no locus is privileged.

P04 — Bandwidth as non-negative additive scalar.
Each channel-locus participation carries a bandwidth b_K(u) >= 0. Bandwidth is
non-negative, additive under channel decomposition
(b_{K1 u K2} = b_{K1} + b_{K2} for disjoint sub-channels), and is the
substrate-level scalar carrier of "amount of participation". Bandwidth further
carries a four-band partition: a single chain's participation bandwidth
decomposes into four mutually orthogonal bands.

P05 — Polarity-transport along edges.
The participation graph carries a connection structure that transports polarity
along graph edges. Operational content: pi_K(u,t) in U(1) transports along
edges (u,t) -> (u',t') via a substrate-level connection.

P06 — Spatial dimension primitive.
The substrate has spatial dimension three, plus one temporal direction via P13.
Dimensionality is primitive, not derived from compactification. Operational
content: substrate-graph adjacency in three spatial directions; closed
2-surfaces have area 4*pi*R^2.

P07 — Channel structure as ontological primitive.
Channels are structurally distinguishable carriers with intrinsic identities.
Two distinct channels at the same locus are distinct objects even if their
bandwidth and polarity agree.

P08 — Substrate scale.
The substrate has a characteristic edge length / discretization scale l_ED.
This scale is primitive: the substrate is not continuous below l_ED, and below
it no further structure is resolved. As an inherited empirical value,
l_ED = l_P, the Planck length, approximately 1.616e-35 m. (This value is
empirical input, not derived here.)

P09 — U(1)-valued polarity.
Each channel-locus participation carries a polarity pi_K(u) in U(1). Polarity
is the substrate's primitive angular variable, a single U(1) at the most
fundamental level.

P10 — Rule-type primitive.
The substrate supports multiple structurally distinct rule-types: matter
rule-types (chain-carrying), gauge rule-types, and kernel rule-types. Each
rule-type is a primitive label with its own participation measure or kernel
content.

P11 — Commitment irreversibility.
At certain substrate events ("commitment events"), a chain's multi-channel
participation collapses to single-channel participation, with the un-selected
channels' phase content randomized by the environment. These events are
discrete and irreversible.

P12 — Stability landscape.
Each chain carries a substrate-level functional

    Sigma_C = Coh(C) - Str(C) - Grad(C)

where Coh, Str, Grad are the chain's coherence, strain and gradient content.
The chain's experienced acceleration is the negative gradient of Sigma_C along
its adjacency directions:

    a_C = - grad_adj Sigma_C

P13 — Time homogeneity.
The substrate's dynamics are invariant under time translation: the laws at time
t are identical to those at t'. No moment is privileged. Substrate events are
primitively discrete.

TWO INHERITED KERNELS

V1 — the vacuum / ultraviolet kernel.
A substrate kernel rule-type (licensed by P10) mediating same-chain
propagation. Its envelope is bounded and decaying with a characteristic width
set by l_ED: it has no delta-function limit and no infinite-width limit. Its
support is strictly retarded — forward in substrate time only.

V5 — the cross-chain correlation kernel.
A substrate kernel rule-type (licensed by P10) mediating correlation between
distinct chains. Its envelope is bounded and decaying, and depends on the
Lorentz-invariant separation between the two participations. It carries a
finite memory time. It inherits strictly retarded support from V1.

PART 2 — INHERITED CONSTANTS

The framework does not derive the following. They are taken from measurement
as inputs. No relation among them is assumed.

  c        the substrate's rate of becoming, identified with the observed
           speed of light, 2.998e8 m/s
  hbar     the action associated with one commitment event, 1.055e-34 J s
  l_P      the substrate grain, 1.616e-35 m (= l_ED, per P08)
  G        Newton's gravitational constant, 6.674e-11 m^3 kg^-1 s^-2
  H_0      the Hubble rate, approximately 70 km/s/Mpc
  a_0      the observed MOND transition acceleration, approximately
           1.2e-10 m/s^2
  Lambda   the observed cosmological constant
  m_i      the particle masses
  g        the gauge couplings
  alpha    the fine-structure constant, approximately 1/137, and the
           observed mass ratios

PART 3 — DOMAIN-SPECIFIC POSTULATES

These are additional commitments, each needed to make progress in a particular
vein of physics, and not claimed to hold generally.

D01  a_0 and a canonical cross-scale operating point share a single
     substrate-cosmology boundary origin.
D02  Composite participation states factorize: Psi^AB = Psi^A (x) Psi^B, with
     tensor-product structure.
D03  The V5-mediated bilocal state has Schmidt rank greater than 1 generically.
D04  There is a monogamy budget cap on cross-chain correlation, and the
     correlation measure saturates that budget.
D05  The substrate's correlation strength sits at the Tsirelson bound;
     Popescu-Rohrlich boxes are excluded.
D06  Six substrate-level conditions (C1-C6) hold, under which an effective
     acoustic metric emerges from participation transport. (Stated here by role
     only.)
D07  Quadratic strain. Per-channel participation is the complex amplitude
     P_K = sqrt(b_K) e^{i pi_K}, and the strain on a channel is the squared
     modulus of the summed amplitude over contributing sources:

         Str_K = | sum_a P_K^(a) |^2
               = sum_a b_K^(a)  +  2 sum_{a<b} sqrt(b_K^(a) b_K^(b)) cos(Theta_ab)

     where Theta_ab is the gauge-invariant relative phase between contributions.
D08  A coarse-graining postulate governing the Yang-Mills action's passage from
     substrate to continuum. (Stated here by role only.)
D09  An Osterwalder-Schrader reflection-positivity condition holds on the
     substrate-level construction. (Stated here by role only.)
D10  A profile-rescaling condition under which the Yang-Mills construction
     survives the continuum limit. (Stated here by role only.)
D11  Tensor-product composition for joint states: Psi^AB = Psi^A (x) Psi^B.
D12  There is a local rate of becoming, and the substrate rate is locally
     constant — identified with c.
D13  A gauge-class connection exists on rule-type bundles, with a gauge
     quotient.
D14  Uncommitted branch-basis correlation consumes pairwise V5 weight.
D15  V5 exists as a cross-chain kernel rule-type.

YOUR TASK

Work through as much of gravitation as these assumptions will carry, and
then stop and report the boundary.

Concretely, produce two things.

PART A - HOW FAR IT GOES.
Derive what follows. Where a step does not follow, say plainly that it does
not, and do not manufacture a derivation. State every additional assumption
you introduce and name it.

PART B - THE GAP REPORT. This is the part that matters.
For every place you stopped, write a numbered entry with:

  1. WHERE. The specific step you could not take. Name the quantity,
     structure, or relation - not the topic. "I could not get from the
     participation graph to a metric that responds to matter content" is
     useful. "General relativity is hard" is not.

  2. WHAT WOULD BE NEEDED. The specific thing that, if added, would let you
     take the step. A definition, a constraint, a structure, a postulate.
     Write it as precisely as you can - ideally as a statement someone could
     add to Part 3 above and then use.

  3. WHICH KIND. Classify it as one of:
       (i)   a MISSING DEFINITION - something above is stated too loosely to
             compute with;
       (ii)  a MISSING STRUCTURE - a mathematical object the axioms never
             introduce;
       (iii) a GENUINE POSTULATE - something that could not be derived from
             the rest and would have to be assumed outright;
       (iv)  a HARD DERIVATION - nothing is missing, the work is just long or
             technically difficult and you did not do it here.
     The distinction between (iii) and (iv) is the most valuable judgement
     you can give, so say which and why.

  4. WHAT IT UNLOCKS. If this one thing were supplied, what else would then
     follow? Be specific about the downstream steps.

  5. CONFIDENCE. High / medium / low, and what would change your mind.

Finally, RANK your entries: if the authors could supply exactly one of the
things you asked for, which one should it be, and why that one?

Two instructions on honesty, which matter more than completeness.

- If one of the axioms above is stated too vaguely to be used, say so
  directly. Do not silently substitute a sharper version of your own and
  proceed as if it had been given to you.

- If you believe some step cannot be repaired by any addition - that the
  framework as stated has a structural problem rather than a gap - say that
  instead, and say why. Do not soften it into a request for a definition.

```

---

## Scoring — fixed in advance, before any output is seen

**Arm C is not pass/fail.** A and B had binary targets; this one measures yield. Four measures, all recorded per family:

- **Y1 — specific actionable gaps.** Count of Part B entries that name a quantity, structure or relation rather than a topic. **A topic-level entry scores zero however well written.**
- **Y2 — the (iii)/(iv) split.** How many gaps each family calls a *genuine postulate* versus a *hard derivation*, and whether the three families agree on any given gap. **Disagreement here is itself informative: it locates the steps where even the classification is unclear.**
- **Y3 — convergence.** Gaps named by two or more families independently. **This is the primary signal.** One model's list is that model's taste; three lists overlapping is a property of the axiom set.
- **Y4 — calibration against target #24.** Do the runs reach the four known-real weak points — the `cos Θ` sign, the metric-emergence gap, `D01`'s under-specification, the `G` circularity? **A run that names only novel gaps and none of these four should have its other findings discounted**, because the four are the cases where we already know the correct answer.

**And one negative check.** If a family reports a *structural problem* rather than a gap, that is the highest-value single output of the arm and must be recorded verbatim and checked against the corpus before anything is done with it. **The standing rule applies: a negative gets the same bar as a positive.**

**No re-prompting. Single paste, single reply, per family.** Same discipline as A and B.
