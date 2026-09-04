# What Independent Models Add When Given ED's Primitives and Nothing Else

**Allen Proxmire**

**September 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (probes of the primitive set itself)
**Status:** Probe note. Five runs across two independent frontier model families, in three conditions: **blind** (ontology sketch only), **seeded-with-a-swap** (thirteen primitives, P08 replaced by a coarse-graining primitive), and **seeded-full** (thirteen primitives plus V1/V5 inheritance). Measures where an outside reconstruction places its load-bearing assumptions, what it postulates that ED derives, and where it stops. Not a physics result.
**Anchors:** `Paper_087_13Primitives` (the set under test) · `Paper_MetricFromTheGraph_ForcedTo3D` (P4 isotropy) · `Paper_026`/`Paper_027` (the channel-count route to `1/R`) · `Paper_GR-I` (`N² ~ b`) · `Paper_GR-III` (the dynamical rule)
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The 13 substrate primitives are not derived** (`Paper_087`). This note tests their *minimality, economy and completeness as a declared set*, not their truth.
2. **This is not evidence about physics.** Nothing here confirms or refutes any ED result. Agreement between models is evidence about the structure of the problem and about what is obvious to a capable reader; it is not evidence about nature.
3. **No run was blind to ED's framing.** The blind prompt states P11 in ordinary language; the seeded prompts hand over the primitive list. The exercise measures the gap between what ED declares and what a reader must add. It cannot test whether ED's starting point is right.
4. **No claim that any model's output is correct.** These are scaffolds, not derivations. Two runs contain outright errors (§5), reported as such.
5. **No claim that the primitive set should change on this evidence.** §7 states what would be needed to act, and why the one swap actually tested does not work.
6. **The prompts are defective in named ways** (§6), disclosed rather than quietly corrected. The prompt was revised once between conditions; the revision is stated.

---

## 1. Conditions and runs

| Run | Family | Condition | Given |
|---|---|---|---|
| **A** | OpenAI | blind | ontology sketch in prose; no primitive list, no results, no repo access |
| **B** | Google | blind | same sketch |
| **C** | OpenAI | seeded, **P08 swapped** | thirteen primitives with `ℓ_ED` replaced by "a coarse-graining regime exists"; no kernels |
| **D** | OpenAI | seeded, full | thirteen primitives with operational content, plus V1 (`1/R` envelope, retarded) and V5 as inherited kernels; asked to aim at an inverse-square law and a bandwidth-clock relation, and to name the postulate needed at each stopping point |
| **E** | Google | seeded, full | same as D |

**Contamination.** No run showed recognition: no ED vocabulary beyond what the prompt supplied, no ED results, no naming of the framework. Exposure would bias toward false convergence, so its absence strengthens what follows. The corpus is public, so this remains a live confound for any future run (F2).

**Depth is not uniform.** Run A logged 21 additions; Run B logged 6 and missed the largest gap A found. Run D was scrupulous about labels; Run E mislabelled its central postulate as derived. Where runs of unequal quality **agree**, that is where the signal is.

---

## 2. Blind condition — what a reader must add

| Requirement | Run A | Run B | ED's declared answer |
|---|---|---|---|
| Partial causal order over commitments | Addition 1, load-bearing | Assumption 1, Critical | P11 + P13 + V1 retardation (T18) |
| **A coarse-graining regime that fixes a dimension** | Addition 5, load-bearing | Assumption 2, Critical | **not in the thirteen** — §3 |
| Hop count becomes distance | Addition 4 | Assumption 3, Moderate | `MetricFromTheGraph`, unweighted hop count |
| Particles as stable graph patterns | Addition 11 | Assumption 5, Moderate | chains; matter sector |
| Phase / complex amplitudes for QM | Additions 8–10 | Assumption 6, Critical | P09 — omitted from the blind prompt (§6) |
| **Isotropy of the microstructure** | absent | Assumption 4, Critical | measured, not assumed — §4 |
| A rule constraining which commitments occur | Addition 7, **its #1 gap** | absent | V1 / V5 kernels, P12 |
| Finite causal propagation speed | Addition 16 | *derived*, one hop per event | P05 |
| Conservation, energy | Additions 12–13 | absent | P04 bandwidth budget |
| Gauge, Standard Model | Additions 18–19 | absent | P09; MS-I / MS-II |
| Entropy, thermodynamic arrow | Additions 20–21 | absent | the arrow-sorts-the-continuum line |

Run A distinguished the primitive arrow from the thermodynamic one unprompted and warned they "should not be automatically identified" — ED's central inversion, legible to a reader not told to look for it. And its single most load-bearing missing ingredient was a rule constraining which commitments occur: ED's answer is V1/V5, and `Paper_090` records V5's existence as a P10-licensed posit whose forward derivation is **open**.

---

## 3. Finding 1 — the additions land in the coarse-graining layer

Both blind runs put load-bearing assumptions in the same place, and it is not among the thirteen: that a stable coarse-graining regime exists, that it converges to a definite effective dimension, and that it washes out directional structure.

ED assumes all three and discloses them, but as per-paper regime-of-validity language. `Paper_MetricFromTheGraph_ForcedTo3D` is explicit — "a lattice/label background is assumed… the metric *on* the background is emergent; **the background topology is input**" — and carries the matching falsifier as **F5**. So this is disclosed work recorded in the wrong place: two independent readers concluded it is load-bearing at the level the primitives operate on.

**Tier: Open.** Whether it belongs as a declared primitive, as a standing postulate alongside V1/V5, or as per-paper regime language is a judgment this note does not make. §7 states the constraint that makes the choice non-trivial.

---

## 4. Finding 2 — on isotropy, ED's position is stronger than the runs demanded

Run B rated isotropy **Critical**, arguing the microstructure must be randomized rather than crystalline or the emergent space keeps preferred directions. Run D independently refused to write `g ∝ −∇B` because "neither linearity nor isotropy was separately supplied." Three appearances across two families and two conditions.

ED does not assume it. `Paper_MetricFromTheGraph_ForcedTo3D` §6 (P4) runs the measurement on **a genuine 3D cubic lattice** — the crystalline case Run B says must be excluded — with a spherical bandwidth dip, and reports the raw ballistic metric **is** faceted at layer 1, exactly as predicted, while the anisotropy **washes out monotonically under coarse-graining**: axis versus body-diagonal, 0.345 → 0.000, with per-shell coefficient of variation 0.06 shrinking with radius.

Even a crystal works, and the curve is on record. That is strictly stronger than an axiom. **Tier: Measured**, one constructed arena, background topology as input (§3).

**Three unrelated senses of "crystal" in this corpus, kept apart:**

1. **Lattice anisotropy** — this section. Measured; a layer-1 artifact that coarse-grains away.
2. **Long-range correlation order** — `Paper_BlindnessInvariant_KnotsNotCrystals`: blindness → common-cause only. Explicitly scoped away from topological defects.
3. **Ellis & Rothman's Crystallizing Block Universe** — the indefinite-to-definite transition surface. `Paper_EvolvingBlockUniverse_Ellis`. Nothing to do with lattices.

---

## 5. Seeded condition — what the primitives actually buy

### 5.1 Removing P08 costs Newton and `G` (Run C)

Run C was given the thirteen with `ℓ_ED` replaced by a coarse-graining primitive. Its own "what I did not derive" list includes **the inverse-square law** and **a numerical gravitational constant**.

Those are exactly what P08 pays for. `G = c³ℓ_P²/ħ` has no content without a length scale, and the holographic count is `4πR²/ℓ_ED²`, needing P06's area *and* P08's grain. The swap was run and the cost is measured, not argued. **The coarse-graining item of §3 cannot be paid for by deleting P08.**

Run C's closing judgment: "the crucial source-response map from bandwidth/channel structure to effective geometry is still an A-level position, not a D-level derivation. That map is the main remaining load-bearing gap." The gravity ledger's **first row under Open (declared)** is *"Bandwidth ↔ strain/flow substrate-route identification — OPEN."* Same item, found without the corpus.

### 5.2 Both full runs postulate what ED derives, in the same place

Runs D and E both reach Newtonian scalar gravity plus a weak-field clock relation, and both get the `1/R` bandwidth profile by **assuming** the source inherits V1's envelope (D's P14; E's asserted Poisson equation).

ED does not assume it. `Paper_026`/`Paper_027` distribute the source's content across `N(R) = 4πR²/ℓ_ED²` channels rather than duplicating into each, and the per-channel V1 sum returns `Φ = −GM/R` **with the `N(R)` factors cancelling exactly**. ED's own papers flag the seductive wrong version: an `R²` surface "competing" with a `1/R` kernel gives `Φ ∝ R`.

Both runs had P06 and P08 and neither found the counting argument. That is evidence the argument is non-obvious, not that the primitives are idle. The same holds for `G`: Run E quoted `ℓ_ED ≈ 1.616 × 10⁻³⁵ m`, used it only for the continuum limit, and produced `G_eff = ακg₀/4π` — a product of three undetermined constants, no content. ED's dimensional closure to one postulated scale was not reached from having the scale available.

### 5.3 The fork: both runs skip the null-cone step (corrected 2026-09-04)

**Run D:** `ν_clock = κB`, labelled **P**. **Run E:** `ν(r) = κ·B(r)`, labelled **D**. Two families, linear in bandwidth, no hesitation.

**An earlier draft of this section read the divergence wrongly, and the correction matters.** ED's own P-Commitment-Linear says the *commitment rate* is linear in bandwidth: `Γ_commit ∝ b`. That is the same linearity both runs chose. **ED agrees with them on the postulate.**

The divergence is one step later. Both runs identified commitment rate *with* clock rate. ED does not. `Paper_GR-I` §4.2 puts the advancing front on the null cone of `ds² = −N²dt² + b⁻¹dx²` with `dx/dt = Γ ∝ b`, giving `0 = −N² + b⁻¹·b²`, hence **`N² ~ b`** — the clock rate is `N = √b` while the commitment rate stays linear. That is what yields `g₀₀ g_rr ~ −1`: the Schwarzschild relation, the Einstein branch rather than the conformal one, and the factor-of-two light bending. In general `Γ ∝ b^α` gives `N² ~ b^{2α−1}`, so the entire Einstein/Nordström fork sits in that one exponent.

The exercise therefore produces **two** results here, pointing in opposite directions:

- **Convergent support for the postulate.** Two independent families, unprompted, took the commitment rate linear in bandwidth. P-Commitment-Linear is what a capable reader assumes anyway, which is mild evidence it is the natural reading rather than a fitted one.
- **The null-cone conversion is the non-obvious step.** Neither run separated the rate at which a front advances from the rate at which a clock ticks. Run D noticed a shortfall, proposed `g₀₀ = −(B/B₀)²` (its P21) to recover its own linear law, and stated it could not reach `√(1 − 2GM/c²R)`. Run E did not notice.

That relocates where rigor is owed: not to P-Commitment-Linear, which is independently natural and separately argued in `Paper_GR-III` §4, but to GR-I §4.2's front-null identification — the move that converts a rate into a lapse, and the one step no outside run made or mentioned.

### 5.4 Postulate economy

To reach Newton plus a weak-field clock relation, Run D needed six named postulates (P14 kernel-to-bandwidth coupling, P15 gradient response, P16 inertial participation, P17 universal source identification, P18 bandwidth-commitment capacity, P19 relativistic normalization `αB₀ = c²`), and named three more (P20–P22) as required to continue.

ED's corresponding named postulates are roughly four — P-Codim-1, P-Sat, P-Potential-Reading, P-Commitment-Linear — and ED derives the `1/R` that D postulates. The economy comes from a route divergence: **D and E went Newtonian** (bandwidth → force via a postulated gradient-response law plus a separate inertial postulate), while **ED goes geometric** (bandwidth → metric → geodesics), which needs no force law at all.

**Tier: Measured** (a count, on one prompt, against one route). It is not a claim that ED's route is correct, only that it is more economical in declared postulates and that the economy has an identifiable source.

### 5.5 Errors in Run E, and why one matters

- **It labelled its central postulate D.** Step 5 writes `∇²B = g₀ρ_M` and calls it derived. Nothing given yields a Poisson equation. ED has this equation as `GR-III`'s `ḃ = D∇²b − κρ`, steady state `∇²b ~ ρ` at correlation 0.999 — **built and run**, tiered *measured*. Run E asserted in one line what ED needed a simulation to earn. This is the exact failure the P/A/I/D discipline exists to catch, and the same class as the missing audit table behind the `1/(2π)` finding in `Gravity_TieredClaims_Ledger.md` Staleness #10.
- **It double-counts the `1/R`**, deriving the profile from the Poisson Green's function and then describing that step as convolving with V1's `1/R` envelope. Either source suffices; using both counts one factor twice.
- **It mis-tiers P06** as "Measured / Empirical input" when the prompt supplied it as a postulate. Run D got this right explicitly.
- **Its falsifier is generic.** A deviation from `1/R²` falsifies every gravity theory, not this one. Run D's `δν/ν = δB/B` targets its own mechanism. The corpus's paper-writing checklist §1 already requires theory-specific falsifiers; this is an independent illustration of why.

### 5.6 Where all runs stop, identically

Run D: a bandwidth-to-interval map, a metric equivalence map, a nonlinear source equation. Run E: a tensor coupling or action principle for GR, light bending, gravitational waves, horizons.

Same wall under different names, and it is exactly where `Paper_GR-I` and `Paper_GR-III` begin. Across five runs the boundary is stable: unaided reconstruction reaches Newtonian scalar gravity with a linear clock relation and stops.

---

## 6. Prompt defects, disclosed

**Blind prompt (Runs A, B):** forbids a substrate scale while ED postulates `ℓ_ED` as P08; omits P09's polarity and then records both models noticing phase was missing; gives no cue that a dynamical rule is expected, which is likely why Run B never asked for one.

**Seeded prompt, revised before Runs D/E:** primitives given with operational content, V1/V5 added as inherited kernels, two quantitative targets named, and each stopping point required to name the postulate that would let it continue. That last clause produced §5.6 and is the most productive instruction in the set.

**Still absent, and deliberately so.** The prompt does not signal the `√b` branch. Signalling it would destroy the §5.3 measurement and would collapse the replication condition into the audit condition. The correct fix, for a future revision, is to require branch enumeration — *"where two or more inequivalent continuations are available, list them, say which you take and why, and state what would decide between them"* — which surfaces the fork without supplying the answer.

**A standing question left by the phase defect:** if P09 already carries a `U(1)`, how much work is the Solèr selection argument doing when it "selects" ℂ from `{ℝ, ℂ, ℍ}`? Two independent models converging on "phase must be injected" is not an answer, but it is a reason to look. **Open question, not a finding.**

---

## 7. On removing and adding a primitive

Neither blind run reached for a fundamental spatial dimension; both treated it as emergent from `N(r) ~ r^D`. ED postulates **P06**.

That preference is not novel and ED has recorded it: `Paper_087` §P06 carries a Round-4 QC acknowledgment that P06 "is doing extraordinary load-bearing work across the corpus," and notes that Hardy 2001, CDP 2011, Masanes–Müller and Coecke–Kissinger all treat spatial dimension as **derived**. Two models given no such context took the same side. ED is the outlier and knows it.

**But P06 is not padding, and neither candidate move is a line-item edit.**

- P06 supplies the `4πR²` area to `Paper_025`, the `R²` surface to `Paper_027`, the dimension-dependence of the codimension-1 footprint, and the `D = 3+1` PDE forcing in the NS arc.
- `MetricFromTheGraph` P2 *does* select exactly-3 (`p = 1/(d−1)` gives `g ~ 1/b` in 3D and not 2D, ball-cut exponents 0.984 and 2.008) — but **conditional on the holographic surface count, which P06 supplies**. Citing it as P06's replacement is circular unless the count is re-derived first.
- Run C measured the cost of the other direction: **removing P08 loses the inverse-square law and `G`.**

**Net:** the candidate addition is the coarse-graining item of §3; the candidate removal is P06. They cannot be traded against each other, and the swap actually tested (P08 out, coarse-graining in) is refuted by Run C. Adding without removing takes the count to fourteen. Removing P06 is a derivation project — derive the dimension, then re-derive `4πR²`, the inverse-square law and the codimension-1 footprint from the derived dimension — not a deletion.

---

## 8. Falsification criteria

- **F1:** If further independent families, run on the revised prompt, do *not* place load-bearing additions in the coarse-graining layer, Finding 1 is a small-sample artifact and should be withdrawn.
- **F2:** If a run reproduces ED's thirteen or the `√b` branch closely, the first hypothesis is **training exposure**, not convergence. The recognition question must be run, in a separate turn after the run completes, before anything is banked.
- **F3:** If the background-free construction called for by `MetricFromTheGraph` F5 produces a metric with no assumed lattice, Finding 1 weakens sharply: the coarse-graining assumption would be doing far less than the runs supposed.
- **F4:** If P06 proves derivable without the holographic count, the §7 circularity clears and the removal becomes an option rather than a project.
- **F5:** If a run given the branch-enumeration clause lists `√B` alongside `B` and picks it on stated grounds, §5.3's "non-obvious" reading weakens: the step would then be reachable and merely unprompted.

---

## 9. Position statement

ED sits in the substrate-ontology lineage ('t Hooft's cellular-automaton interpretation, the causal-set program), not the operational-reconstruction tradition, and nothing here moves it. What the exercise adds is a measurement that lineage rarely takes: **where competent outside readers, given the program's own declared inputs, find they must add something — and what they postulate that the program derives.**

Three answers, in order of usefulness. They postulate the `1/R` profile that ED's channel count produces. They take the linear clock branch where ED takes the square root, which is the step that puts ED on the Einstein branch. And their unforced additions land in the coarse-graining layer, which is where ED's own open frontier already sits.

Read modestly. No run tested ED. They tested what ED declares, and agreed with each other about where the hard part is. The corpus already says the hard part is there. What is new is that nobody had to be told, and that two of ED's least-advertised steps turn out to be the ones an outsider does not find.

---

## Provenance

Five runs, 2026-09-04, fresh contexts, no repository access. **A:** OpenAI, blind, 21 numbered additions with a load-bearing ledger. **B:** Google, blind, 6 numbered assumptions with a criticality column. **C:** OpenAI, seeded with P08 replaced. **D:** OpenAI, seeded full, postulates P14–P19 plus proposed P20–P22, with a derivation ledger. **E:** Google, seeded full, six-step construction with a number inventory. Prompts and full transcripts held with the session record; the tables here are complete for the runs cited, not excerpts.
