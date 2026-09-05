# F1 Arm B — Seed Prompt (the 38 lines)

*Written 2026-09-05 for `Protocol_F1_ColdReconstruction_TwoArm.md`. **Paste §"THE PROMPT" verbatim.** Everything outside that block is protocol notes and must not be sent.*

---

## The decision that determines whether arm B tests anything

**The 38 lines list `G = c³ℓ_P²/ħ` (row 15) and `a₀ = cH₀/(2π)` (row 16). Neither is seeded as a relation. Both are seeded as values.**

`G = c³ℓ_P²/ħ` **is the dimensional closure to `G`** — one of the three steps every prior seeded run failed to reach. Handing it to the model as an axiom would not test ED's assumption set; it would hand over a result and then congratulate the model for holding it. The same applies to `a₀ = cH₀/(2π)`, which is the arc's headline derivation and whose coefficient the corpus currently disputes.

**This is faithful, not a weakening.** The workbook's own Tier Key classes all ten as **Constant / Input**, and the constants-inherited ledger reads the `G` row as *"a combination, not a **second** independent input — but not therefore explained."* **The input is `ℓ_ED`; the relation is ED's account of it.** Arm B therefore seeds the ten quantities as inherited empirical values and withholds every relation among them.

**If arm B nonetheless recovers `G = c³ℓ_P²/ħ` from `c`, `ħ` and `ℓ_P`, that is a result** — and one the prior runs conspicuously did not produce despite holding all three.

## Other seed-design decisions

1. **Arm B is arm A plus additions, with nothing else changed.** The primitives and kernel blocks are byte-identical to `Seed_F1_ArmA_13Primitives.md`. Any other edit would void the A/B comparison.
2. **Row 24 is seeded as stated and no further.** *"`a₀` and `ξ_canonical` share one substrate-cosmology boundary origin"* is given without identifying what that boundary is — naming `R_H = c/H₀` would leak the horizon-tying that is the arc's substantive content.
3. **Three of the fifteen are seeded at label-plus-role granularity** — the acoustic-metric guardrails, `P-YM-Action-Coarse-Graining`, `P-OS-Reflection-Positivity`. Their full content lives in papers arm B withholds, and inventing detail would be worse than declaring the limit. **This is a real limitation of the arm: a pass is meaningful, a failure attributable to these three is not.**
4. **`P-Quadratic-Strain` is seeded with its algebraic form**, because the form *is* the postulate and a bare label would be untestable.
5. **The 38's own dispute flags are not seeded.** The model is not told the `2π` is disputed; it is not given the `2π` at all.

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

From the assumptions above and standard mathematics, derive as much of
gravitation as follows.

State every additional assumption you must introduce, name it, and list them
all at the end.

Where you cannot derive something and must postulate it, say so explicitly
rather than asserting it.

If a step does not follow, say plainly that it does not. Do not manufacture a
derivation.
```

---

## Scoring

**Identical targets to arm A. Do not change them after seeing output.**

- **T1 — front-null identification.** Separating the rate at which a commitment front advances from the rate at which a clock ticks, reaching `g₀₀g_rr = −1`. The conformal branch is a **fail**.
- **T2 — `N(R)` cancellation.** *Deriving* a `1/R` source profile from a channel count over the closed 2-surface. Postulating `1/R` is a **fail**.

**Secondary, and now more informative than in arm A:** does any run recover **`G = c³ℓ_P²/ħ`** from the seeded `c`, `ħ` and `ℓ_P`? All three arm-A runs held those constants; none connected them. GPT explicitly declined to, calling it *"not a substrate derivation."* Record it as a distinct observation, not as a pass.

**Also record:** the count of named additional assumptions, against arm A's 14 / 3 / 8 on the same families.

**No re-prompting.** Same discipline as arm A.
