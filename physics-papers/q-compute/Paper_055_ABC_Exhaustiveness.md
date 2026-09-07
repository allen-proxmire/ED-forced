# Paper 055 — Architectural Three-Class Exhaustiveness (A/B/C)

**Series:** Wave-2 Generative Papers (Q-Compute Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_053 ($\mathcal{M}_{\mathrm{cap}}$), Paper_054 (UR-1), Paper_056 (Class A wall), Paper_057 (Class B gap-suppression), Paper_058 (Class C plateau).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim that no novel architectures will ever be invented; rather, that **any** Q-COMPUTE architecture is structurally a Class A, B, or C projection of $\mathcal{M}_{\mathrm{cap}}$ (Paper_053) under the substrate audit.
2. It does **not** claim quantitative exhaustiveness at the experimental level; it claims **structural** exhaustiveness at the substrate-mechanism level.
3. It does **not** introduce new substrate primitives.
4. "Three-class exhaustiveness" means: every Q-COMPUTE architecture saturates at least one of three constituent-constraint regimes (bandwidth, V5, commitment) within $\mathcal{M}_{\mathrm{cap}}$.

---

## Abstract

The Q-COMPUTE architectural three-class classification (A engineered-low-multiplicity, B global-geometric-rigidity, C high-multiplicity-redundancy) is FORM-FORCED to be **exhaustive** at substrate level. The argument: $\mathcal{M}_{\mathrm{cap}}(s) = \min(N_{\mathrm{bw}}, N_{\mathrm{V5}}, N_{\mathrm{commit}})$ (Paper_053) has exactly three constituent counts; at any substrate configuration, at least one binds. Architectural classes are projections onto which constituent binds: Class A ↔ $N_{\mathrm{bw}}$, Class B ↔ $N_{\mathrm{commit}}$, Class C ↔ $N_{\mathrm{V5}}$. Three constituents → three classes. Exhaustiveness is FORCED.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P04 (Bandwidth)**, **P10 (Rule-type primitive)**, **P11 (Commitment-irreversibility)**.

### 2.2 Upstream dependencies

- **I-053:** $\mathcal{M}_{\mathrm{cap}}$ as composite object (Paper_053).
- **I-054:** UR-1 theorem (Paper_054).
- **I-056:** Class A wall (Paper_056).
- **I-057:** Class B gap-suppression (Paper_057, in queue).
- **I-058:** Class C plateau (Paper_058, in queue).

### 2.3 Paper-specific postulates

- **P-Three-Constituent:** $\mathcal{M}_{\mathrm{cap}}$ has exactly three constituent counts ($N_{\mathrm{bw}}$, $N_{\mathrm{V5}}$, $N_{\mathrm{commit}}$); no fourth substrate-level constituent exists.
- **P-Always-Binding:** At any substrate configuration $s$, at least one constituent count saturates $\mathcal{M}_{\mathrm{cap}}$.

---

## §2.5 Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | $\mathcal{M}_{\mathrm{cap}} = \min(N_{\mathrm{bw}}, N_{\mathrm{V5}}, N_{\mathrm{commit}})$ | I | Paper_053. |
| 2 | Three constituent counts | P-Three-Constituent | Postulate. |
| 3 | At least one constituent always binds | P-Always-Binding | Postulate (follows from $\min$ structure). |
| 4 | Class A ↔ $N_{\mathrm{bw}}$ saturates | I | Paper_056. |
| 5 | Class B ↔ $N_{\mathrm{commit}}$ saturates | I | Paper_057. |
| 6 | Class C ↔ $N_{\mathrm{V5}}$ saturates | I | Paper_058. |
| 7 | Three classes = three constituent saturation patterns | D | Composition. |
| 8 | Exhaustiveness: any architecture lies in $\{A, B, C\}$ | D | Application of P-Always-Binding. |

> **⚠ FLAG 2026-09-07 — this row's provenance is empty.** Row 4 tiers *“Class A ↔ `N_bw` saturates”* as **`I`, inherited from `Paper_056`** — and **`Paper_056` does not contain that claim.** Its only bandwidth mention is P04's primitive statement; **`N_bw` is never defined or used there**, and the cap it computes is the commitment-rate one. **Root cause: this paper and `Paper_056` sort the classes by two DIFFERENT trichotomies** — `M_cap`'s three *constituents* (all limits on a count) versus UR-1's three *conditions* (one count condition and two rate conditions) — and since `M_cap = min{N_bw, N_V5, N_commit}`, **UR-1.1 already contains all three constituents**, so the two partitions cannot be put in correspondence. **Rows 5 and 6 are additionally CROSSED against `Paper_056` §6's own lever mapping** (which makes Class B cross-bandwidth/V5 and Class C commitment/redundancy — matching the class names both papers share). See `q-compute/Note_Mcap_TwoDefinitions_2026-09-07.md` §§A–D. **Not resolved here.**
| 9 | Meta-architectures = compositions, not new classes | I | Paper_059. |

---

## §3 The Exhaustiveness Argument

### 3.1 Three constituents → three classes

By Paper_053, $\mathcal{M}_{\mathrm{cap}}(s) = \min(N_{\mathrm{bw}}(s), N_{\mathrm{V5}}(s), N_{\mathrm{commit}}(s))$. By P-Three-Constituent, no fourth constituent exists.

By the $\min$ structure (and P-Always-Binding), at least one constituent count saturates $\mathcal{M}_{\mathrm{cap}}$ at any $s$. This saturating constituent defines the architectural class:

- $N_{\mathrm{bw}}$ saturates → Class A (engineered-low-multiplicity).
- $N_{\mathrm{commit}}$ saturates → Class B (global-geometric-rigidity).
- $N_{\mathrm{V5}}$ saturates → Class C (high-multiplicity-redundancy).

### 3.2 Exhaustiveness

Any Q-COMPUTE architecture is a substrate configuration $s$ with some $\mathcal{M}_{\mathrm{cap}}(s)$. By the argument above, $s$ falls in at least one class. Therefore $\{A, B, C\}$ is **exhaustive**.

### 3.3 Boundary cases

Two-constituent saturation (e.g., $N_{\mathrm{bw}} = N_{\mathrm{V5}} < N_{\mathrm{commit}}$) places the architecture on a class-boundary; the architecture exhibits mixed-class characteristics. Three-constituent saturation places it at the triple point — a structural degeneracy.

---

## §4 Falsification Criteria

- **F1:** Discovery of a Q-COMPUTE architecture not classifiable into A, B, or C — refutes exhaustiveness.
- **F2:** Substrate-level identification of a fourth constituent count beyond $N_{\mathrm{bw}}, N_{\mathrm{V5}}, N_{\mathrm{commit}}$ — refutes P-Three-Constituent.
- **F3:** Architecture exhibiting all three constituents simultaneously **unsaturated** (no constraint binds) — refutes P-Always-Binding.

---

## §5 Position Statement

The A/B/C classification is **FORCED-exhaustive** by P-Three-Constituent + P-Always-Binding + $\mathcal{M}_{\mathrm{cap}}$ structure (Paper_053). Three constituents → three classes. Meta-architectures (Paper_059) are compositions, not new classes.

---

**End Paper 055 (FIXED).**
