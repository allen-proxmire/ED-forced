# F1 Arm C (Σ_C) — Seed Prompt: define the three terms, blind

*Written 2026-09-05 for `Protocol_F1_ColdReconstruction_TwoArm.md` Stage 3. **Paste §"THE PROMPT" verbatim.** Everything outside that block is protocol notes and must not be sent.*

---

## What this run is for

**A blind replication of 2026-09-05's `Σ_C` chain** — gravity ledger Staleness #70–#76, seven entries deep, three of them resting on a `Grad` proposal one day old and a layer reading that is not closed. **The chain was written by one scorer in one session and needs a pass from someone who did not write it.**

**The design is blind, not forward.** The prompt presents the corpus **as it stood on the morning of 2026-09-05, before any of the day's corrections** — including the `Coh`/`Str` collision intact and the phase-coherence paper's two incompatible statements of `Coh`, quoted neutrally and without comment. **The reader is not told there is a problem.**

**Why blind rather than asking what is still missing.** A forward run would inherit the settlement and could only refine it. **A blind run tests whether the settlement was findable and whether an independent reader reaches it** — and if it reaches a *different* resolution, that is worth more than any new gap, because four supports were assembled today on the assumption that only one assignment works.

## Seed-design decisions

1. **The two established results are given.** `a_N = GM/R²` and `a = a_N + √(a_N a_0)` are what made the settlement possible; withholding them would not be a fair shot and would test recall rather than reasoning.
2. **No leak of the day's answers.** Not stated anywhere: that `Str` is the diagonal and `Coh` the off-diagonal; that the split was fixed by matching the established result; the Relation/Boundary/Gradient reading; the Dirichlet-form proposal for `Grad`; the layer-1/layer-2 framing; the density-matrix correspondence. **Also not stated: that any inconsistency exists.**
3. **The simulator's forms are given as data, flagged as a simulator rule** — that flag is in the corpus and withholding it would be inventing a defect.
4. **P04's non-negativity is stated**, because it is a primitive and it is load-bearing for one of the day's two independent routes. Whether the reader uses it is the test.
5. **The task keeps arm C's (i)–(iv) classification**, which was the design feature that made arm C work.
6. **One leak caught and removed in drafting.** The anti-smoothing instruction first read *“do not smooth it over by picking the reading that works”* — which implies there are multiple readings and that one of them works, i.e. it hands over half the finding. Replaced with *“report any tension … rather than resolving it silently”*, which preserves the anti-smoothing function without asserting that a tension exists. **Recorded because leak-checking the prompt caught what reading it did not.**

---

## THE PROMPT

```
You are given part of a proposed pre-quantum substrate ontology. Treat the
numbered commitments as axioms: they are posited, not derived, and you should
not try to justify them. Your job is to work out what they mean and what
follows.

PART 1 - THE RELEVANT PRIMITIVES

P04 - Bandwidth.
Each channel-locus participation carries a bandwidth b_K(u) >= 0. Bandwidth is
NON-NEGATIVE, and additive under channel decomposition. It is the substrate's
scalar carrier of "amount of participation".

P05 - Polarity transport.
The participation graph carries a connection that transports polarity along
graph edges.

P09 - Polarity.
Each channel-locus participation carries a polarity pi_K(u) in U(1). This is
the substrate's primitive angular variable.

P11 - Commitment irreversibility.
At certain events, a chain's multi-channel participation collapses to
single-channel participation. These events are discrete and irreversible.

P12 - Stability landscape.
Each chain C carries a substrate-level functional

    Sigma_C = Coh(C) - Str(C) - Grad(C)

where Coh, Str and Grad are the chain's coherence, strain and gradient content.
The chain's experienced acceleration is the negative gradient of Sigma_C along
its adjacency direction:

    a_C = - grad_adj Sigma_C .

PART 2 - WHAT THE FRAMEWORK SAYS ABOUT THESE THREE TERMS

The canonical primitives document defines Sigma_C as above and does not say
anything further about what Coh, Str or Grad are as functions of substrate
variables. The following is everything else the framework states about them.

(a) A domain postulate, "quadratic strain":

      The per-channel strain is the squared modulus of the total participation
      amplitude on that channel,

          Str_K = | sum_a P_K^(a) |^2 ,     P_K^(a) = sqrt(b_K^(a)) e^{i pi_K^(a)}

      where a indexes the source regions contributing to channel K.

(b) A separate paper on the coherence term states, in its section 2:

      With the participation amplitude P_K = sqrt(b_K) e^{i pi_K}, the coherence
      content of a multi-source superposition on one channel is the
      phase-dependent interference part,

          Coh = | sum_a P_a |^2 - sum_a |P_a|^2
              = 2 sum_{a<b} sqrt(b_a b_b) cos(dpi_ab)

      which is zero at random phase and maximal in phase.

    and, in the summary of the same paper's results:

      The coherence term is operationalized as the phase-coherence content, and
      the quadratic strain reading is grounded (Coh read as | sum P |^2).

(c) A simulation rule used elsewhere in the framework scores a candidate
    transition u -> v as

      Sigma = k_c Coh - k_s Str - k_g Grad ,
      with  Coh = -(rho_v - rho_*)^2 ,  Str = rho_v ,  Grad = |rho_v - rho_u| ,

    where rho is a local commitment density. The framework describes this
    simulator as a tractability reduction: it is single-rule-type and has no
    explicit polarity.

PART 3 - TWO RESULTS THE FRAMEWORK ALREADY HAS

These are established downstream results. They are given because they are
what the framework must reproduce.

For a chain at distance R from a mass M, in the presence of a cosmological
boundary characterised by an acceleration scale a_0:

  1. The Newtonian limit:            a_N = G M / R^2
  2. The full acceleration:          a  = a_N + sqrt(a_N a_0)

The framework's own working expressions for the two contributions, per channel,
are b^(L) proportional to G M / R for the local mass, and b^(H) proportional to
a_0 R for the cosmological boundary. After the appropriate sum over channels and
the radial integral, the second term above arises from a contribution
proportional to sqrt(G M a_0) * ln(R).

YOUR TASK

PART A - WHAT ARE THE THREE TERMS?
Work out, as far as the material allows, what Coh, Str and Grad are as
functions of the substrate variables (b_K, pi_K, the graph structure). Show
your reasoning. Where the material determines a term, say so and say what
determines it. Where it does not, say that plainly rather than choosing.

Check your answer against Part 3: does it reproduce both results, with the
right signs? Show the check. If it does not, say so - do not adjust the target.

PART B - THE GAP REPORT.
For every place you could not settle something, write a numbered entry with:

  1. WHERE. The specific thing you could not determine.
  2. WHAT WOULD BE NEEDED. The specific addition that would settle it, written
     as precisely as you can - ideally as a statement someone could add to
     Part 2 and then use.
  3. WHICH KIND:
       (i)   MISSING DEFINITION - stated too loosely to compute with;
       (ii)  MISSING STRUCTURE - a mathematical object never introduced;
       (iii) GENUINE POSTULATE - could not be derived from the rest and would
             have to be assumed outright;
       (iv)  HARD DERIVATION - nothing is missing, the work is just long.
     The (iii) versus (iv) call is the most valuable judgement you can give.
  4. WHAT IT UNLOCKS.
  5. CONFIDENCE, and what would change your mind.

Then RANK: if the authors could supply exactly one thing, which one?

Three instructions on honesty, which matter more than completeness.

- Report any tension you find between the statements in Part 2, or between
  Part 2 and Part 1, rather than resolving it silently.

- If something in Part 2 is stated too vaguely to use, say so rather than
  silently substituting a sharper version of your own.

- If you think some part of this cannot be repaired by any addition - that
  there is a structural problem rather than a gap - say that instead, and say
  why.
```

---

## Scoring — fixed in advance, before any output is seen

**This is a blind replication, so it is scored against a known answer.** The four things 2026-09-05 concluded, in the order they were reached:

- **S1 — the collision.** Does the run notice that `|Σ P|²` is assigned to **both** `Coh` (via 2(b)'s summary line) and `Str` (via 2(a)), and that they enter `Σ_C` with **opposite signs**? **This is the primary measure.** It took a full session and one external prompt to find.
- **S2 — the resolution.** Does it reach `Str_K = Σ_a b_K^{(a)}` (diagonal) and `Coh_K = 2Σ_{a<b}√(b_a b_b)\cosΘ_{ab}` (off-diagonal)? **And crucially: does it reach it by the same route** — checking which assignment reproduces Part 3 — or by a different one?
- **S3 — the P04 route.** Does it notice that a sum of non-negative bandwidths cannot equal a negative potential, i.e. that the minus in `Φ_N` must be P12's own `−Str`? **This was the second, independent confirmation and it uses only P04.**
- **S4 — `Grad`.** Does it reach anything for `Grad`, and if so what? **The day's answer is a proposal, not a result**, so a *different* well-argued proposal is a finding rather than a failure.

**And one negative check.** If the run reaches a **different** resolution than S2 that also reproduces Part 3, **that is the highest-value output of the whole protocol** and must be recorded verbatim and checked before anything is done with it — because four supports were assembled on 2026-09-05 assuming only one assignment works.

**Failure modes to record rather than discount:** silently picking the reading that works (instruction 1 exists to catch this); treating the simulator forms in 2(c) as the substrate definitions; inventing a `Grad` and presenting it as determined.

**No re-prompting. Single paste, single reply, per family.** Same discipline as arms A, B and the first arm C.
