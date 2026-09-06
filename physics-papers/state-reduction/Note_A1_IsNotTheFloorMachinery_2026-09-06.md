# A1 answers a different question: it measures region-to-region transmission, not branch distinguishability

**Date:** 2026-09-06
**Status:** **Result.** The escape, the locality advantage and Pillars 1–2 are untouched. **Two residuals' stated plan of attack is void.**
**Read:** `StateReduction_CollapseRate_ED_Derivation.md`, `StateReduction_ChannelGranularity.md`, `event-density/evaluation/Bits/docs/A1_ChannelCapacity_Results.md`.

---

## 1. What survives, first

**The 2020-bound escape stands exactly as written.** Its load-bearing step — Lindblad jump operators are channel projectors `Ĵ_α = g_α Π̂_α`, so committed charges are exact fixed points — is FORCED from P11 and does not touch A1.

**The locality advantage stands, and its A1 citation is correct.** *"Controlled inter-region capacity = exactly zero (A1, measured)"* is precisely what A1 found, used for precisely what it supports: local, forward-causal collapse without superdeterminism. **That is A1 doing the job it can do.**

**Pillars 1 and 2 of the channel-granularity resolution stand and need no A1**: `ℓ_ED`-fine dynamics is coherent Schrödinger evolution, not position measurement; and the pointer basis is environment-selected einselection, hence the coarse robust basis. **Between them they already carry the conclusion that the pointer basis is coarse.**

## 2. The problem is narrow and it is in the residuals, not the results

Two residuals name A1 as the machinery that will supply a number:

> **`CollapseRate`:** *"the exact prefactor … rides on the precise distinguishability threshold for commitment … **Rigor here = the same distinguishability/A1 machinery, pushed to a coefficient.**"*

> **`ChannelGranularity` Pillar 3:** *"distinguishability in ED is **operational** … **the A1 result measures it as controlled channel capacity** … Operational distinguishability has a **coarse floor**."*

**A1 cannot be pushed to that coefficient, for two independent reasons.**

### (a) It measures a different pair of things

**A1's experiment is region-to-region.** It encodes a message in region A's left half and asks whether it can be decoded from A's right half or from region B. **The objects are two spatial regions of one substrate.**

**Branch distinguishability is a different pair.** *"The arrow individuates two branches exactly when they become operationally distinguishable"* — the objects there are **branch 1 and branch 2 of a superposition**, not two regions.

> **Whether region X can signal region Y and whether branch 1 can be told from branch 2 are not the same question, and A1 only ran the first.** Pillar 3 imports A1's *spirit* — distinguishability is operational, not substrate-omniscient — which is fair. It does not import a measurement of the relevant quantity, because none was made.

### (b) And A1's own verdict forecloses the plan

Even setting (a) aside, A1's measured value is **exactly zero, everywhere** — *"within a stratum and across the boundary alike."* **If distinguishability simply were controlled channel capacity, it would be zero everywhere and commitment could never individuate anything.** That reductio shows the identification cannot be meant literally.

And A1 states its own limit plainly:

> *"capacity does not yield a positive intrinsic determinability number; it is zero everywhere … **there is no canonical positive determinability scalar to be found this way**"* … *"what is observable-invariant about the boundary is **a zero, not a scalar**."*

**Both branches of the bits fork are closed for an intrinsic positive number:**

| route | outcome |
|---|---|
| observational MI (`Δ`) | **positive but observable-DEPENDENT** — *"the scalar `Δ` is not intrinsic"* |
| interventional capacity (A1) | **intrinsic but exactly ZERO** |

**That fork was run and reported in June 2026. The state-reduction papers were written in July 2026 and point at it for a number it had already concluded is not there.** Ordinary cross-arc staleness, of the kind this ledger keeps finding — **and it costs the arc nothing except the plan.**

## 3. The redirect, which is concrete

**The experiment that would settle it is an A1-style interventional run on two BRANCHES, not two regions** — encode into branch-distinguishing structure, evolve, and ask at what separation commitment resolves them. **That has never been run.**

> **⚠ STRENGTHENED 2026-09-06 (gravity ledger #137): this is not merely a design difficulty.** `Paper_Continuum_KineticLatticeGas` §3 **measures** that *“the certified front does not branch — one seed → exactly one active front … a 1-D chain (a worldline)”*. **There is no branch structure in the simulator to intervene on**, so the experiment below is blocked for a measured reason, not a practical one. See `Note_BranchRepresentation_2026-09-06.md`.

**Honest caveat on feasibility:** the certified substrate is *determinate* — it commits, it does not carry superposed branches — so an A1-style branch experiment is not a re-run of `capacity.py` with different arguments. **It needs a construction that represents two branches on a determinate substrate**, which is a design question, not a parameter change. **Naming it is not the same as having it.**

**Meanwhile the floor's operative value stays environment-set**, which is where `ChannelGranularity` residual 2 already put it, and where `#135` independently pushed it from the locus side.

## 4. What to change, and it is small

- **`CollapseRate`'s coefficient residual** should not say *"the same A1 machinery, pushed to a coefficient."* A1's machinery is region-to-region and its output is zero. **The coefficient needs branch-level machinery that does not yet exist.**
- **`ChannelGranularity` Pillar 3** should keep its conclusion and soften its warrant: *"distinguishability is operational"* is supported by Report §4 and by A1's **framing**; *"A1 measures it"* is not supported by what A1 measured. **The pillar's conclusion is carried by Pillars 1 and 2 regardless.**

**No tier moves. No claim weakens.** Flagged in place at both residuals.
