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
3. **Two arcs are blocked on one statement.** Adopting `P-Commitment-Advancement` would unblock the dwell route *and* ground the evaluation rule — **but it is AP's call, it increments the census, and the certified rule would then be a special case of it rather than an instance.**

**The honest limit:** whether a dwell-capable rule changes any certified result is **untested**, and testing it means changing the reference substrate — which is a much larger move than anything in this session.
