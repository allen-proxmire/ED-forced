# The channel-vs-locus gap: "ballistic-or-extinct" is not forced by the primitives — it is the substitution

**Date:** 2026-09-06
**Status:** **Diagnosis of a known limitation.** The phenomenon is already corpus content; its *cause* and its *status* are not.

---

## 1. The gap, verified in both sources

**P11 selects a channel.** Canonical `Paper_087`:

> a chain's **multi-channel participation collapses to single-channel participation**, with the un-selected channels' phase content randomized.

**The certified rule selects a locus.** `simulator/sigma.py`: `compute_candidates(u)` → `graph.admissible_neighbors(u)`, *"neighbors reachable via a NON-decoupled edge"* — **`u` is not in its own candidate set.** And `simulator/update.py`'s docstring: *"commit at the winner (irreversibility chokepoint) → **advance the front (active u → v)**"*, with lines 71–73 doing exactly that.

**So the evaluation substitutes locus-selection for channel-selection, and nothing states the bridge.**

## 2. The phenomenon is already known — this is not the finding

`Paper_MassWithoutMass_BindingInertia`'s glossary:

> **Ballistic-or-extinct.** The certified rule: a front advances one hop at the maximal speed or dies; **no dwell**, hence no individual rest mass.

**Named, glossaried, and its consequence drawn.** `PATH_A_STATE` also records it as *"a fact about the code."* **Nothing here discovers it.**

## 3. What is not stated: the cause, and therefore the status

**Ballistic-or-extinct is not a consequence of P11. It is a consequence of the substitution.**

P11 collapses to **one channel**. Under Branch 3 (#93) the channels at a locus fall into classes, and **only the Adjacency class is P05-transporting — the class that carries content *between* loci.** So:

> **A commitment that selects an *Internal*-class channel is a commit that does not advance. That is a dwell, and P11 permits it.**

**The certified rule cannot express it**, because its candidate set is neighbouring loci and excludes staying put. **The restriction lives in the implementation, not in the primitive.**

**And this reverses the July dwell retraction's own objection.** It argued that P11's silence on advancement *"does not help: there is no canonical internal band for a commitment to collapse into in the first place."* **Branch 3 supplied exactly that class.** So the objection has been answered — by a result eight weeks later, from an unrelated direction.

## 4. What this changes, stated at the right strength

**Ballistic-or-extinct becomes implementation-conditional rather than primitive-forced.** The glossary entry is accurate as written — it says *"the certified rule"* — **but anything that reads it as a statement about ED rather than about the reference substrate is over-reading it.**

**In particular, *"no dwell, hence no individual rest mass"* is a property of the reference rule.** Whether any mass-sector conclusion depends on that being a fact about **ED** rather than about **the code** is a real question and **is not checked here.** `Paper_MassWithoutMass` may well argue mass-from-binding on independent grounds — hadron binding is real physics regardless — and **no claim of damage is made.**

## 5. And it is the same gap as the dwell arc's, from the opposite end

#94 named the missing bridge as a candidate postulate:

> **`P-Commitment-Advancement`:** *a commitment selecting a propagation-carrying channel advances the chain's locus; one selecting a non-propagating channel does not.*

**That is precisely the channel → locus bridge this note is about.** So the substrate-evaluation arc and the Higgs/dwell arc are blocked on the **same missing statement**, approached from opposite directions — one needs it to *justify* advancing, the other needs it to *permit* not advancing.

**And the certified rule assumes something stronger than the candidate postulate:** not *"advances iff propagation-carrying"* but **"always advances."** So the evaluation arc has been running on a **stronger** unstated identification than the one the dwell arc was told it would have to name and defend.

## 6. What is owed

**Nothing here is a defect claim.** Three things are now on record that were not:

1. **The bridge is unstated**, and the certified rule's version of it is stronger than the named candidate.
2. **Ballistic-or-extinct is implementation-conditional**, not primitive-forced — and after Branch 3, the primitives admit a dwell.
3. ~~**Two arcs are blocked on one statement.**~~ **ADOPTED 2026-09-06 on AP's decision (#117).** `P-Commitment-Advancement` is declared at `Paper_087` §P11 and entered in the postulate registry; **census 173 → 174**. **Both arcs are unblocked:** the certified rule's *“advance the front”* stops being an unstated assumption and becomes **the special case in which every commitment selects an Adjacency-class channel**, and the dwell route gains a licensed non-advancing commit. **Tier P, `(prov)`** — not derivable from the canonical thirteen, which is why it is named, and provisional because derivation from P05 + P11 + the Branch 3 classification is not excluded.

**The honest limit:** whether a dwell-capable rule changes any certified result is ~~**untested**~~ **TESTED 2026-09-06 (#118) for one result.** Adding `u` to its own candidate set, scored by the certified `Σ`: **Knots-safety survives and is MORE comfortably satisfied** (`R` `0.027 → 0.017`, `ξ` `2.13 → 1.93` — both further from crystalline order), and **the substrate still fills completely.** **Dwell is reachable but marginal — 6% of decisions, all ties.** **And the reason is the PARAMETERS, not the rule:** `ρ* = 0.5` with `increment = 1` overshoots the coherence target in one commit, so `Σ(u→u)` ties at `ρ_u = 1` and is strictly worse after. **So the postulate licenses a dwell but does not produce one** — a dwell-bearing substrate needs `ρ*` or the increment changed, which is a change *to* the certified substrate rather than an addition to it. **A second structural point fell out: the certified tiebreak keys on `graph.bw(u,v)`, so a self-move has no key — the rule assumes a neighbour in TWO places, not one.** `foundations/Note_DwellCapable_Test_2026-09-06.md`.
