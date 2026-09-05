# F1 Arm A — Seed Prompt (13 primitives + V1/V5)

*Written 2026-09-05 for `Protocol_F1_ColdReconstruction_TwoArm.md`. **Paste §"THE PROMPT" verbatim.** Everything outside that block is protocol notes and must not be sent to the model.*

---

## Seed-design decisions, recorded because each is an experimental variable

1. **No internal citations.** Every `Paper_NNN` reference is stripped. Paper numbers signal corpus structure and are searchable; a seed that carries them is not testing derivation from primitives.
2. **No "load-bearing in" notes.** The canonical primitives paper annotates each primitive with the downstream results that depend on it — including, for P06, *"the holographic bound's `4πR²` area scaling"* and *"Newton's inverse-square via the `R²` surface"*. **Those name target T2.** All such annotations are removed.
3. **P08's empirical identification is kept, its route is not.** The seed says `ℓ_ED = ℓ_P` is an inherited empirical value. It does **not** say the identification comes from Newton-recovery — that route is adjacent to T2 and to the dimensional closure to `G`.
4. **P04's four-band partition is included.** It is canonical primitive-level content. Including it makes the seed *more* generous than prior runs; **under-seeding is the failure mode that would make a negative result worthless**, so the seed errs toward generosity throughout.
5. **P12's acceleration relation is kept in full** (`a_C = −∇_adj Σ_C`). Without it there is no route to gravitation at all and the arm tests nothing.
6. **No constants beyond P08's scale.** Per protocol, arm A carries no constants table. `c`, `ħ`, `G`, `a₀`, `H₀` are absent.

---

## THE PROMPT

```
You are given a proposed pre-quantum substrate ontology, stated as a set of
primitive commitments. Treat these as axioms: they are posited, not derived,
and you should not attempt to justify them.

THE SUBSTRATE PRIMITIVES

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

## Scoring this arm

Score **only** against the two pre-registered targets. Everything else is context.

- **T1 — front-null identification.** Did the run separate *the rate at which a commitment front advances* from *the rate at which a clock ticks*, and reach `g₀₀g_rr = −1` (the Einstein branch)? Landing the conformal branch is a **fail**.
- **T2 — `N(R)` cancellation.** Did the run *derive* a `1/R` source profile from a channel count over the closed 2-surface, or did it **postulate** `1/R`? Postulating is a **fail**.

**Secondary, recorded every run:** the number of named additional assumptions. Baseline is **six** from the best prior seeded run; ED reaches the same place on four.

**Do not re-prompt toward either target.** A hint that lands T1 or T2 voids the run — that confound is the entire reason F1 exists.
