# Paper 053 — Multiplicity-Cap Function $\mathcal{M}_{\mathrm{cap}}$ as One Substrate Object

**Series:** Wave-2 Generative Papers (Q-Compute Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_054 (UR-1 theorem), Paper_055 (A/B/C exhaustiveness), Paper_056 (Class A wall), Paper_090 (V5).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim novel empirical predictions beyond the Q-COMPUTE arc closed-arc inventory.
2. It does **not** claim derivation of $\mathcal{M}_{\mathrm{cap}}$'s specific numerical values for concrete systems; values are INHERITED via platform-specific matching.
3. It does **not** introduce new substrate primitives.
4. $\mathcal{M}_{\mathrm{cap}}$ is a **single substrate-level object** with three projections (architectural classes A/B/C, Paper_055) and meta-architectural overlays (Paper_059). This paper formalizes the unified-object claim.

---

## Abstract

The multiplicity-cap function $\mathcal{M}_{\mathrm{cap}}$ is a single substrate-level object combining: (i) bandwidth-additive content from P04; (ii) commitment-irreversibility threshold from P11; (iii) V5 cross-chain correlation budget from Paper_090. $\mathcal{M}_{\mathrm{cap}}(s)$ at substrate configuration $s$ counts the maximum number of distinguishable rule-type configurations a system can sustain before substrate-level commitment forces individuation. The three architectural projections (Class A engineered-low-multiplicity, Class B global-geometric-rigidity, Class C high-multiplicity-redundancy) are projections of $\mathcal{M}_{\mathrm{cap}}$ onto specific platform parameters. The structural form of $\mathcal{M}_{\mathrm{cap}}$ is FORCED; specific platform values INHERITED.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P04 (Bandwidth)** — additive substrate budget.
- **P10 (Rule-type primitive)** — supplies V5.
- **P11 (Commitment-irreversibility)** — directional individuation.

### 2.2 Upstream dependencies

- **I-090:** V5 cross-chain correlation kernel (Paper_090).
- **I-054:** UR-1 theorem (Paper_054).
- **I-073:** DCGT (Paper_073).
- **I-Hilbert:** Rule-type Hilbert space (Paper_007).

### 2.3 Paper-specific postulates

- **P-Mcap-Unification:** The multiplicity-cap function $\mathcal{M}_{\mathrm{cap}}(s)$ is a single substrate-level object — the architectural Class A/B/C projections + meta-architectural overlays are derived projections, not independent objects.
- **P-Mcap-Finiteness:** For any substrate configuration $s$ with finite substrate cells, $\mathcal{M}_{\mathrm{cap}}(s) < \infty$.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | P04 bandwidth-additive | P | Primitive. |
| 2 | P11 commitment-irreversibility | P | Primitive. |
| 3 | V5 cross-chain budget | I | Paper_090. |
| 4 | $\mathcal{M}_{\mathrm{cap}}$ as composite object | P-Mcap-Unification | Postulate. |
| 5 | Finiteness $\mathcal{M}_{\mathrm{cap}}(s) < \infty$ | P-Mcap-Finiteness | Postulate. |
| 6 | Class A/B/C projections | I | Paper_055. |
| 7 | Substrate-platform value matching | I | Empirical. |

---

## §3 Definition and Structure

### 3.1 Composite definition

$$\mathcal{M}_{\mathrm{cap}}(s) := \min\big\{ N_{\mathrm{bw}}(s), N_{\mathrm{V5}}(s), N_{\mathrm{commit}}(s) \big\} ,$$
where $N_{\mathrm{bw}}$ is the bandwidth-limited count (P04), $N_{\mathrm{V5}}$ the V5-cross-chain-correlation-limited count (Paper_090), and $N_{\mathrm{commit}}$ the commitment-threshold-limited count (P11).

The **min** structure is forced by the load-bearing constraint: a substrate must satisfy **all three** simultaneously.

> **⚠ FLAG 2026-09-07 — the three constituents are named here and NEVER DEFINED, anywhere in the arc.** A search of every q-compute paper finds no formula for `N_bw`, `N_V5` or `N_commit`. Downstream papers use them **structurally** (which technique raises which budget, which class a platform falls in) and **never numerically**. **Only `N_commit` has a value attached anywhere**, via `Paper_054` §5.1's `M_cap = (Γ_indiv⁻¹/Γ₀)^{1/γ}`. **Consequence: `min{·}` is not computable, so `Paper_056` did not choose the commitment constituent over the other two — it used the only one that had ever been quantified.** *That is the root of the class-assignment collision, and no check could have caught it: a check compares two numbers, and two of these three have no numbers to compare.* See `Note_Mcap_TwoDefinitions_2026-09-07.md` §§F–J. ~~**Defining `N_bw` unblocks the whole arc.**~~ **⚠ SUPERSEDED 2026-09-07 (same day) — `N_bw` CANNOT be defined from P04, and this flag was sending readers after a definition that does not exist.**
>
> **P04 cannot carry a limit.** Canonical P04 (`Paper_087`) is **non-negativity plus additivity**, with **no upper bound and no quantization** — so calling `N_bw` *“the bandwidth-limited count (P04)”* attributes to P04 something P04 does not say. **The soft-matter arc made this exact mistake and withdrew it on 2026-09-05:** `Paper_UnifiedP04TransportBudget` §5 now records that its old *“P04 finiteness”* justification *“claimed something P04 does not say”*, and points at `entanglement/Paper_065_Monogamy` as the paper that does it correctly.
>
> **And importing a bound would not rescue it, for two measured reasons** (`event-density/theory/nbw_definability_probe.py`, 200,000 draws per claim): **(1) `M_eff` is scale-invariant** — homogeneous of degree 0 in the bandwidths (verified: `M_eff(3b)/M_eff(b) = 1.0` exactly), so a budget on the *total* constrains it not at all; with the total pinned at 1, `M_eff` still runs `10 → 10,000` as channels grow. **(2) The quantum-free reading makes Class A EMPTY.** Take `N_bw` = channel-support count, the one definition needing nothing beyond P04; then **`M_eff ≤ N_bw` holds identically by Cauchy–Schwarz** (verified: 0 violations in 200,000 draws, equality only at exact uniformity). **That leg of UR-1.1 can never bind — and §3.2 defines Class A as the branch where `N_bw` binds first.**
>
> **What `N_bw` needs is a minimum bandwidth per channel — a FLOOR, not a quantum (see the correction below). The corpus records its absence twice** — `primitives/participation_bandwidth.md` open question 6 (*“nothing forces it yet”*), and arc FSC (closed 2026-05-25), whose Q1 is exactly this and which states *“P04 makes bandwidth a non-negative additive scalar, not a quantized scalar.”* **Tier: ABSENT AND UNFORCED, not excluded** — FSC's proven blockage concerns P09 polarity holonomy, a different scalar, and this is not banked as an impossibility.
>
> **So the blocker is a PRIMITIVE-LEVEL DECISION — does bandwidth quantize? — and not a definition anyone can write.** *That is the correction to this flag: it named the wrong kind of task.*
>
> **⚠ WORD CORRECTED 2026-09-07 (same day) — “quantum” is wrong, and it mispriced the decision.** A **FLOOR** (`b ≥ b_min` for any channel that exists) restricts which **configurations** exist. **QUANTIZATION** (`b ∈ {0, β, 2β, …}`) restricts P04's **codomain** — it changes what P04 *is*. **Only the second is primitive-level.** A floor is the same kind of object as **`P-V5-Budget`**, which `Paper_065`'s own audit table tiers ***“Postulate, declared”***, and as `P-Locus-Bandwidth-Bound`. **Neither was ever called a fourteenth primitive, and neither needed to be.**
>
> **And the cheap object suffices for the count.** With a floor `b ≥ b_min` and the total budget the corpus already carries, the channel count is bounded by `B / b_min`. **That bound is NOT scale-invariant** — `b_min` is fixed while `B` scales — **so it evades the degree-0 homogeneity result that killed the budget-alone route.** *A floor plus an existing budget yields `N_bw`. Quantization is not required for it.*
>
> **Precedent, three in three days, every one landing at postulate level rather than primitive level:** the four-band partition → `P-Band-Partition`; soft-matter's budget → `P-Locus-Bandwidth-Bound`; and individuation → constructible from P02+P03+P04, whose paper opens ***“Individuation is not a fourteenth primitive. The corpus is committed to thirteen.”*** **That arc faced this same shape** — its ratio `R = b_int/b_bdry` is also degree-0 homogeneous, closing the bandwidth-normalisation route — **and it fixed `θ_ind = 1` anyway, through an INTEGER the substrate already had: locus depth, `⌈a/2⌉ > ξ`.**
>
> **So the question is not “does bandwidth quantize?” but “what integer does the substrate already have that a channel count can ride on?”** *A candidate under test elsewhere: P13 carries primitive event-discreteness, and if a sustained channel must hold at least one event's worth of commitment reserve, that is a floor sourced from P13 with nothing added.* **Untested — and the nearest neighbour of the idea already has a banked negative (individuation is union-closed for every `θ`, so it is a cohesion filter and not an object-count criterion).**
>
> **Two consequences for §3.1's own account.** **(a) The gap is ONE thing, not three.** `N_bw` and `N_V5` are both **counts**, and a count needs a unit; **`N_commit` is a rate crossing, which needs no quantum.** *That is the structural reason it is the only constituent with a formula — `Paper_056` did not merely use the one that happened to be quantified, it used the one whose KIND sidesteps counting entirely.* **(b) `N_V5` is closer than this arc knows.** §3.1 cites `Paper_090` for it and stops; `entanglement/Paper_065_Monogamy` followed that same pointer and **built the budget** — `Σᵢ ℰ ≤ W_max`, form-forced from `P-V5-Budget` + `I-V5` + P04 additivity. **A grep of this entire folder for `Paper_065`, `W_max` and `P-V5-Budget` returns nothing: the arcs are disconnected, and `Paper_065` is the paper the P04 primitive card holds up as doing this correctly.**
>
> *Found in a read-only session on this repo; verified here before applying.*

### 3.2 Three architectural projections

- **Class A:** $N_{\mathrm{bw}}$ saturates first — engineered-low-multiplicity platforms (Paper_056).
- **Class B:** $N_{\mathrm{commit}}$ saturates first — global-geometric-rigidity platforms (Paper_057).
- **Class C:** $N_{\mathrm{V5}}$ saturates first — high-multiplicity-redundancy platforms (Paper_058).

> **⚠ FLAG 2026-09-07 — `M_cap` carries two definitions across this arc, and they disagree about which constituent sets the Class-A wall.** `Paper_053` §3.1 defines `M_cap = min{N_bw, N_V5, N_commit}` and §3.2 assigns **Class A to `N_bw`** (bandwidth, P04); `Paper_054` §5.1 and `Paper_056` §3 define and use `M_cap = (Γ_indiv⁻¹/Γ₀)^{1/γ}`, which is the **`N_commit`** constituent — `Paper_053`'s **Class B**. **Neither paper states which constituent it means, which is why this was invisible** (the same failure mode as foundations #10's `Coh`/`Str` collision). **Three candidate resolutions are set out in `q-compute/Note_Mcap_TwoDefinitions_2026-09-07.md`, and none is adopted — the choice changes the arc's structure and is the author's. **UPDATED same day: `Paper_055` has been read and a fourth resolution proposed — the two accounts sort the classes by two DIFFERENT trichotomies (`M_cap`'s constituents vs UR-1's conditions), and `Paper_055` row 4's `I` tier cites `Paper_056` for a claim it does not make. See the note's ADDENDUM §§A–D.**

These are **projections** of the same $\mathcal{M}_{\mathrm{cap}}$, distinguished by which constituent constraint binds.

### 3.3 Meta-architectural overlays

EC (error correction), DD (dynamical decoupling), reservoir engineering, hybrids (Paper_059) are **compositions** that modify the substrate configuration $s$ without modifying $\mathcal{M}_{\mathrm{cap}}$'s functional form — they shift which constituent constraint binds.

---

## §4 Falsification Criteria

- **F1:** Empirical detection of a Q-COMPUTE system whose multiplicity behavior cannot be decomposed into the three projections — refutes P-Mcap-Unification.
- **F2:** Detection of substrate configuration with $\mathcal{M}_{\mathrm{cap}}(s) = \infty$ — refutes P-Mcap-Finiteness.
- **F3:** Demonstration of a fourth architectural class not captured by Class A/B/C — refutes Paper_055 + P-Mcap-Unification.
- **F4:** Detection of a meta-architecture that produces a fundamentally new bound rather than shifting constituent-constraint dominance — refutes the projections framework.

---

## §5 Position Statement

$\mathcal{M}_{\mathrm{cap}}$ is **one substrate object** (P-Mcap-Unification) with three projections (Class A/B/C) and meta-architectural overlays. Composite definition $\min(N_{\mathrm{bw}}, N_{\mathrm{V5}}, N_{\mathrm{commit}})$ FORCED by simultaneity of constituent constraints. Numerical values INHERITED.

---

**End Paper 053 (FIXED).**
