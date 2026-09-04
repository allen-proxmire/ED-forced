# What Two Independent Models Add When Given ED's Bottom and Nothing Else

**Allen Proxmire**

**September 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (probes of the primitive set itself)
**Status:** Probe note. A measured result about **where an unguided reconstruction places its load-bearing assumptions**, run against two independent frontier model families. Not a physics result. Companion to `Paper_087_13Primitives` (the primitive set under test) and `Paper_MetricFromTheGraph_ForcedTo3D` (whose P4 isotropy measurement answers one of the two probes' central demands).
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The 13 substrate primitives are not derived** (`Paper_087`). This note tests their *minimality and completeness as a declared set*, not their truth.
2. **This is not evidence about physics.** Nothing here confirms or refutes any ED result. It measures how a competent reader with no access to the corpus partitions the problem when handed ED's bottom layer in plain English. Agreement between models is evidence about the problem's structure, not about nature.
3. **The probe was not blind to ED's framing.** The prompt states P11 in ordinary language ("irreversible commitments of a relation to one state"). It can therefore only measure the gap between that sketch and the thirteen. It cannot test whether the sketch itself is right, and no run here is independent confirmation of ED's starting point.
4. **No claim that either model's output is correct.** Both produced scaffolds, not derivations. Where a model asserts something cannot be done, that is its judgment, recorded as such.
5. **No claim that the primitive set should change on this evidence alone.** Two runs on one prompt is a pointer, not a finding about the corpus. §6 states what would be needed to act.
6. **The prompt used is defective in three named ways** (§5). The findings are reported with that defect disclosed, not corrected after the fact.

---

## 1. What was done

Two frontier models from independent families — one OpenAI, one Google — were each given the same prompt in a fresh context with no repository access, no primitive list, no ED results, and no indication that a target framework existed:

> Take this as the bottom layer of physics: a discrete relational graph, no coordinates, no edge lengths, no background scale, where the only events are irreversible commitments of a relation to one state. Build upward toward known physics. Every time you must add an assumption I did not give you, stop and log it explicitly as a numbered addition. At the end, give me the list of additions and say which ones are load-bearing. Do not try to guess what framework I have in mind.

The output of interest is **not** whether either reconstructed ED. Neither did, and neither should have. The output of interest is the **list of additions**: what a capable reader finds it must assume, and where those assumptions land relative to ED's declared thirteen.

**Contamination.** The corpus is public on GitHub, so training exposure is possible. Neither run showed any: no ED vocabulary (bandwidth, khronon, commitment-locality, participation), no ED results, no recognition. One mentioned spectral dimension in passing as an alternative to hop-distance, which is standard quantum-gravity vocabulary, not a tell. Exposure would bias toward false convergence, so its absence strengthens rather than weakens what follows.

**Asymmetry of depth.** The two runs were not of equal quality. Run A logged 21 additions and identified the absence of a dynamical rule as its single largest gap. Run B logged 6 and never noticed that gap at all. Where they differ, that is usually a difference in thoroughness. Where they **agree**, having been run independently, is where the signal is.

---

## 2. The convergent additions

| Requirement | Run A | Run B | ED's declared answer |
|---|---|---|---|
| Partial causal order over commitments | Addition 1, load-bearing | Assumption 1, Critical | P11 + P13 + V1 retardation (T18) |
| **A stable coarse-graining regime that fixes a dimension** | Addition 5, load-bearing | Assumption 2, Critical | **not in the thirteen** — see §3 |
| Hop count becomes distance | Addition 4 | Assumption 3, Moderate | `MetricFromTheGraph`, unweighted hop count |
| Particles as stable graph patterns | Addition 11 | Assumption 5, Moderate | chains; matter sector |
| Phase / complex amplitudes for QM | Additions 8–10, "must be postulated" | Assumption 6, Critical, "you must inject complex numbers" | P09 (`U(1)` polarity) — **omitted from the prompt**, see §5 |
| **Isotropy of the microstructure** | absent | Assumption 4, Critical | **measured, not assumed** — see §4 |
| A rule constraining which commitments occur | Addition 7, "absolutely load-bearing," its #1 gap | absent | V1 / V5 kernels, P12 |
| Finite causal propagation speed | Addition 16, load-bearing | *derived*, one hop per event | P05 polarity-transport |
| Conservation laws, energy | Additions 12–13 | absent | P04 bandwidth budget |
| Gauge structure, Standard Model | Additions 18–19 | absent | P09; MS-I / MS-II |
| Entropy, thermodynamic arrow | Additions 20–21 | absent | the arrow-sorts-the-continuum line |

Two agreements are worth isolating.

**Run A distinguished the primitive arrow from the thermodynamic one unprompted**, and stated that they "should not be automatically identified." That is ED's central inversion, reached independently from the same starting sentence. It is not confirmation of ED — the starting sentence already contains the inversion — but it does show the distinction is legible to a reader who was not told to look for it.

**Run A named ED's declared soft spot without seeing the corpus.** Its single most load-bearing missing ingredient is a rule constraining which commitments occur. ED's answer is V1 and V5, and `Paper_090` records V5's existence as a P10-licensed posit whose forward derivation is **open**. An unguided reader landed on the gap ED already admits. This does not validate ED; it does indicate ED's self-assessment points at a real hole rather than a decoy.

---

## 3. Finding 1 — every candidate addition lands in the coarse-graining layer

Both runs put load-bearing assumptions in the same place, and it is not among the thirteen:

- that a stable coarse-graining regime exists at all;
- that it converges to a definite effective dimension rather than staying graph-like at every scale;
- that it washes out directional structure.

ED assumes all three. They are carried inside papers as regime-of-validity statements rather than in the primitive set. `Paper_MetricFromTheGraph_ForcedTo3D` is explicit — "Constructed substrates (a lattice/label background is assumed), static bandwidth fields… The metric *on* the background is emergent; **the background topology is input**" — and it carries the matching falsifier as **F5**: if a background-free construction produced no metric, the emergence would stand exposed as an artifact of the assumed background.

So this is disclosed work, not hidden work. What the probe shows is that it is disclosed *in the wrong place*: two independent readers, given the thirteen's content in prose, both concluded that a coarse-graining assumption is load-bearing at the level the primitives operate on. **Tier: Open.** Whether it should be promoted to a declared primitive, a standing postulate alongside V1/V5, or left as per-paper regime language is a judgment this note does not make.

---

## 4. Finding 2 — on isotropy, ED's actual position is stronger than the probe demanded

Run B rated isotropy **Critical**, arguing the microstructure must be randomized rather than crystalline, since a regular lattice would give the emergent space preferred directions and break Lorentz invariance — "light and matter would travel faster diagonally than horizontally."

ED does not assume this, and does not need to. `Paper_MetricFromTheGraph_ForcedTo3D` §6 (P4) runs the measurement on **a genuine 3D cubic lattice** — precisely the crystalline case Run B says must be excluded — with a spherical bandwidth dip, and reports:

- the raw ballistic shortest-path metric **is** faceted at layer 1, exactly as Run B predicts;
- the anisotropy **washes out monotonically under coarse-graining**, axis versus body-diagonal, 0.345 → 0.000;
- binning by true radius, the per-shell coefficient of variation of hop-distance is 0.06 and shrinks with radius.

ED's answer is therefore a measured layer-1 → layer-2 transition rather than an axiom: even a crystal works, and here is the washout curve. That is strictly stronger than the assumption Run B says is required. **Tier: Measured**, on one constructed arena, with the background topology as input (§3).

**Three senses of "crystal" in this corpus, kept apart.** They are unrelated and conflating them would produce a false result:

1. **Lattice anisotropy** — is the substrate graph a regular lattice with preferred directions? This section. Answered by measurement; anisotropy is a layer-1 artifact that coarse-grains away.
2. **Long-range correlation order** — can a substrate field develop crystalline order in the condensed-matter sense? `Paper_BlindnessInvariant_KnotsNotCrystals`: blindness → common-cause only, and sparse becoming erases almost all of it. Explicitly scoped to correlation order and **not** to topological defects.
3. **The Crystallizing Block Universe** — Ellis & Rothman's name for the indefinite-to-definite transition surface. `Paper_EvolvingBlockUniverse_Ellis` covers it. Nothing to do with lattices.

---

## 5. Finding 3 — the prompt is defective, in ED's favor and against it

Three faults, all in the prompt rather than the runs:

1. **It forbids a substrate scale** ("no background scale") while ED postulates `ℓ_ED` as **P08**, on which `G = c³ℓ_P²/ħ` entirely rests. The prompt asked for something ED does not claim.
2. **It omits polarity.** Both runs concluded that phase and complex amplitudes must be injected by hand, Run B flatly: irreversible commitment to one definite state cannot produce interference or Bell violations. ED does not claim otherwise from bare irreversibility either — its phase enters through **P09**, a declared primitive. The prompt omitted P09 and then recorded the models noticing its absence.
3. **It gives no cue that a dynamical rule is expected**, which is likely why Run B never asked for one while Run A called it the largest gap.

Fault 2 leaves a fair question standing, independent of the prompt: if P09 already carries a `U(1)`, how much work is the Solèr selection argument doing when it "selects" ℂ from `{ℝ, ℂ, ℍ}`? Two independent models converging on "phase must be put in" is not an answer, but it is a reason to look. **Tier: Open question, not a finding.**

---

## 6. On removing and adding a primitive

Neither run reached for a fundamental dimension. Both treated dimension as emergent from how relational volume grows with graph radius, `N(r) ~ r^D`. ED postulates **P06** (`D = 3+1`).

That preference is not novel and ED has already recorded it. `Paper_087` §P06 carries a Round-4 QC acknowledgment stating that P06 "is doing extraordinary load-bearing work across the corpus," and noting that the operational reconstruction programs — Hardy 2001, CDP 2011, Masanes–Müller, Coecke–Kissinger — treat spatial dimension as a **derived** structural fact. Two independent models, given no such context, took the same side. ED is the outlier here and knows it.

**But P06 is not padding, and removing it is not a subtraction.** Paper_087's own list of its dependencies:

- `Paper_025`'s holographic bound: the `4πR²` area scaling comes from P06.
- `Paper_027`'s Newton inverse-square: the `R²` surface comes from P06.
- `Paper_025`'s codimension-1 channel-footprint argument is dimension-dependent and operates within P06.
- The whole gravity arc's spatial-geometric content (027/028/029/030/031/039) depends on it implicitly.
- The NS arc's `D = 3+1` PDE forcing.

And there is a circularity hazard. `Paper_MetricFromTheGraph_ForcedTo3D` P2 does select exactly-3 — the reach law `p = 1/(d−1)` gives `g ~ 1/b` in 3D and not in 2D, with ball-cut exponents measured at 0.984 and 2.008 — but that selection is **conditional on the holographic surface count**, and the holographic count is one of the things P06 supplies. Removing P06 and citing the exactly-3 result as its replacement would be circular unless the count is first re-derived without it.

**The honest statement of the swap, then:** the *candidate* removal is P06 and the *candidate* addition is the coarse-graining/background item of §3. Both are supported by two independent runs and, in P06's case, by ED's own QC note and by the reconstruction literature. Neither is actionable yet. Removing P06 is a substantial derivation project — derive the dimension, then re-derive `4πR²`, the inverse-square law, and the codimension-1 footprint from the derived dimension rather than the postulate — not a line-item deletion. Adding the coarse-graining primitive is cheaper but changes the count and requires a pass over every paper that currently carries it as regime language.

---

## 7. Falsification criteria

- **F1:** If a third and fourth independent model family, run on the corrected prompt of §5, do *not* place load-bearing additions in the coarse-graining layer, Finding 1 is an artifact of two samples and should be withdrawn.
- **F2:** If a run on the corrected prompt (scale and polarity restored, dynamical rule cued) reproduces ED's thirteen closely, the correct conclusion is **training exposure**, not convergence, and the recognition question of §1 must be run before anything is banked.
- **F3:** If the background-free construction called for by `MetricFromTheGraph` F5 produces a metric with no assumed lattice, Finding 1's force is much reduced: the coarse-graining assumption would then be doing far less work than both runs supposed.
- **F4:** If P06 is shown to be derivable without the holographic count, the §6 circularity hazard clears and the removal becomes a real option rather than a project.

---

## 8. Position statement

ED sits in the substrate-ontology lineage ('t Hooft's cellular-automaton interpretation, the causal-set program), not the operational-reconstruction tradition, and this note does not move it. What it does is put a number on one thing that lineage rarely checks: **where a competent outside reader, handed the program's bottom layer and nothing else, finds it necessary to add something.** The answer, twice and independently, was the coarse-graining layer — the seam between the discrete substrate and the continuum, which is exactly where ED's own open frontier already sits (the nonlinear metric, the background-free construction, F5).

That is a modest result and it should be read modestly. The runs did not test ED. They tested a paragraph of English that ED wrote, and they agreed with each other about where the hard part is. The corpus already says the hard part is there. What is new is that nobody had to be told.

---

## Provenance

Run A: OpenAI model, 21 numbered additions with a load-bearing ledger. Run B: Google model, 6 numbered assumptions with a criticality column. Both run 2026-09-04 in fresh contexts without repository access. Prompt as quoted in §1. Full transcripts held with the session record; the additions tables in §2 are complete for both runs, not excerpts.
