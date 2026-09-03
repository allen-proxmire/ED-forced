# Theorems — Folder Guide *(the ratified-statement registry)*

**What this folder is.** The corpus's **theorem registry**: 21 terse index entries (`T1`–`T21`), each pinning down *the statement and current status* of a structural result, with the full derivation living in the corresponding paper (and, for the April-2026 arcs, in the primitives repo's `arcs/`). This is the anchor layer — **78 papers cite these theorem IDs by number**, so `Tn` is the stable handle a paper reaches for when it says "…is forced by T4." Read a theorem file for *what is claimed and how solid it is*; read the linked paper for *why*.

**State** *(authoritative source: `event-density/docs/ED_Research_Targets.md`, esp. #8b; each theorem's own status line)*:
- **Most theorems are FORCED-ratified and solid** — the spinor/frame results (T1–T4), the vacuum kernels (T8/T9), the Hamiltonian/Schrödinger line (T15/T16), and the arrow (T18).
- **Four are DOWNGRADED** and no longer "unconditional": **T10** (Born rule) and **T11** (inner-product / Bell–Tsirelson), both corrected 2026-07-02 for citing a retired primitive vintage + a circular closure step; **T14** (participation-measure / complex Hilbert space), corrected 2026-07-06 (the same claim is treated as an open *postulate*, `P-Motif-Algebra`, by the later canonical `Paper_007`); and **T12** (continuum inner-product), corrected 2026-07-10 — it is a coarse-graining of T11 and inherits T11's open `P-Channel-Orthogonality` foundation.
- **The T14 cascade re-audit is DONE (2026-07-10) and toppled nothing new.** T14's downgrade had flagged four promotions (U2, U5, Bell, Heisenberg) as un-re-audited. Re-audited against their actual papers with the test *"needs ℂ-uniqueness, or just ℂ-existence?"*: all use ℂ-existence only (the granted `P-Motif-Algebra` postulate), never T14's retracted ℝ/ℍ exclusion. **T13** (U5) and **Heisenberg** (Paper_012_6) SURVIVE; the only downgrade (**T12**) was for inheriting T11, not T14. T13's own "unconditional" label was independently stale and was corrected to M3/conditional.
- **Three are stubs** — **T19/T20/T21** (Newton's G, a₀, BTFR) are structural-role statements, conditional on the primitives + upstream gravity content, not standalone derivations.
- **One is subsumed** — **T5** (Gauge-as-Rule-Type / GRH) was folded into **T17** (2026-04-27).

**Status key** *(the theorem's own epistemic standing)*:
`FORCED` = ratified structural result, conditional on the 13 primitives · `FORCED (form) · M3` = the form is forced/identified but the value is inherited and it rests on a named postulate · `Downgraded` = the "unconditional" claim did not survive audit; see the file's correction banner · `Subsumed` = folded into another theorem · `Stub` = structural-role statement, conditional on upstream content, not a full derivation.

> **Provenance note.** These files are the *theory-side index entries*, not the proofs. Several point to the primitives repo (`../event-density/arcs/…` for the derivations, `../ED Primitives/…` for the registration — both sibling repos, neither inside this one) for the constitutional registration. Where a physics-papers exposition exists, it is linked below and is the better read.

---

## Theorems by sector

### QM foundations — the Phase-1 kinematics (U-series, Born rule, inner product)
| T# | Statement | Paper | Status |
|---|---|---|---|
| T10 | Born rule `Prob(K)=b_K/Σb` from participation-graph structure (Gleason–Busch) | [Paper_003 Born Rule](../physics-papers/qm-kinematics/Paper_003_BornRule.md) · [Paper_004 Gleason](../physics-papers/qm-kinematics/Paper_004_GleasonUniqueness.md) | **Downgraded 2026-07-02** |
| T11 | Discrete inner-product structure → Bell–Tsirelson `|S|≤2√2` | [Paper_004.5 Tsirelson (discrete)](../physics-papers/qm-kinematics/Paper_004_5_Tsirelson_Discrete.md) | **Downgraded 2026-07-02** |
| T12 | Inner-product extension to continuous configurations | [Paper_004.6 Tsirelson (continuum)](../physics-papers/qm-kinematics/Paper_004_6_Tsirelson_Continuum.md) | **Downgraded 2026-07-10** (inherits T11's open foundation) |
| T13 | U5 translation / momentum operator | [Paper_012.5 Momentum Operator](../physics-papers/qm-kinematics/Paper_012_5_MomentumOperator.md) | FORCED (form) · conditional · M3 *(survived T14 re-audit; "unconditional" was stale)* |
| — | Heisenberg uncertainty (no dedicated Tn) | [Paper_012.6 Heisenberg](../physics-papers/qm-kinematics/Paper_012_6_Heisenberg.md) | FORCED (form) · M3 *(survived T14 re-audit; ℂ-existence only)* |
| T14 | U1 participation-measure `P_K=√b·e^{iπ}` as the unique complex amplitude carrier | [Paper_003.5 Participation Measure](../physics-papers/qm-kinematics/Paper_003_5_ParticipationMeasure.md) · [Paper_007 Hilbert Space](../physics-papers/qm-kinematics/Paper_007_HilbertSpace.md) | **Downgraded 2026-07-06** |
| T15 | U4 Hamiltonian form (kinetic operator + factor of 2) | [Paper_006.6 Hamiltonian Form](../physics-papers/qm-kinematics/Paper_006_6_HamiltonianForm.md) | FORCED |
| T16 | U3 time-translation generator → Schrödinger evolution (Stone) | [Paper_006.5 Schrödinger / Stone](../physics-papers/qm-kinematics/Paper_006_5_Schrodinger_Stone.md) | FORCED |

### Relativistic QM — spinor, frame, and finiteness
| T# | Statement | Paper | Status |
|---|---|---|---|
| T1 | Spin-statistics theorem (ED form) | [Paper_102 Spin-Statistics](../physics-papers/relativistic-qm/Paper_102_SpinStatistics.md) | FORCED |
| T2 | Cl(3,1) frame uniqueness | [Paper_103 Cl(3,1) Frame](../physics-papers/relativistic-qm/Paper_103_Cl31_FrameUniqueness.md) | FORCED |
| T3 | Anyon prohibition in 3+1 dimensions | [Paper_104 Anyon Prohibition](../physics-papers/relativistic-qm/Paper_104_AnyonProhibition.md) | FORCED |
| T4 | Dirac-equation emergence | [Paper_106 Dirac Equation](../physics-papers/relativistic-qm/Paper_106_DiracEquation.md) | FORCED *(matter-sector chirality gate — #2b)* |
| T6 | Canonical (anti-)commutation relations | [Paper_110 Commutation Relations](../physics-papers/relativistic-qm/Paper_110_CommutationRelations.md) | FORCED |
| T7 | Primitive-level UV finiteness (UV-FIN) | [Paper_111 UV Finiteness](../physics-papers/relativistic-qm/Paper_111_UVFiniteness.md) | FORCED |

### QFT — vacuum-response kernels
| T# | Statement | Paper | Status |
|---|---|---|---|
| T8 | Flat-space vacuum-response kernel (Theorem N1) | [Paper_013 V1 Vacuum Kernel](../physics-papers/qft/Paper_013_V1_VacuumKernel.md) | FORCED |
| T9 | Curved-spacetime vacuum-response kernel (Theorem GR1) | [Paper_014 V1 Curved Background](../physics-papers/qft/Paper_014_V1_CurvedBackground.md) | FORCED |

### Gauge sector
| T# | Statement | Paper | Status |
|---|---|---|---|
| T5 | Gauge-field-as-rule-type (GRH) | *(see T17)* | **Subsumed by T17** (2026-04-27) |
| T17 | Gauge-field-as-rule-type — Arc-Q synthesis | [Paper_015 T17 Gauge Fields](../physics-papers/qft/Paper_015_T17_GaugeFields.md) | FORCED *(self-described rewrite of fiber-bundle vocabulary; non-abelian = analogy; chiral gap open — #2b)* |

### The arrow
| T# | Statement | Paper | Status |
|---|---|---|---|
| T18 | V1 kernel retardation — the kernel-level arrow of time | [Paper_093 Kernel Arrow of Time](../physics-papers/foundations/Paper_093_KernelArrow_of_Time.md) | FORCED *(the keystone — see [[philosophy_arrow_as_keystone_primitive]])* |

### Gravity — structural-role stubs
| T# | Statement | Paper | Status |
|---|---|---|---|
| T19 | Newton's G structural role | [Paper_027 Newton's G](../physics-papers/gravity/Paper_027_Newtons_G.md) | Stub |
| T20 | a₀ structural role | [Paper_029 a₀](../physics-papers/gravity/Paper_029_a0.md) | Stub |
| T21 | BTFR slope-4 structural form | [Paper_031 BTFR](../physics-papers/gravity/Paper_031_BTFR.md) | Stub |

---

## How to use this registry

- **When a paper cites `Tn`,** come here first for the *current* status — a paper written 2026-04 may still speak of T10/T11/T14 as "unconditional"; this registry carries the later corrections. The theorem file wins on status; the paper wins on derivation.
- **The four downgrades (T10, T11, T12, T14) are the corpus's live QM-foundations debt** — target #8b. The Born-rule *value*, the inner-product *form* (discrete T11 and continuum T12), and the complex-carrier *uniqueness* (T14) are inherited/postulated/partially-derived, not FORCED from the canonical 13. Don't quote them as closed. They share one root: the open `P-Channel-Orthogonality` and `P-Motif-Algebra` postulates.
- **The T14 cascade re-audit is closed (2026-07-10).** It confirmed the ℂ-uniqueness failure does not propagate — the downstream QM kinematics (T13 momentum, T15/T16 Hamiltonian/Schrödinger, Heisenberg) run on the complex Hilbert space *existing*, which is a granted postulate, not on ℂ being *forced*. The genuine open debt is orthogonality (T11→T12), not the complex-carrier question.

*(This guide was built 2026-07-10; building it surfaced the T10/T11 banner drift — now fixed — and the T14 cascade re-audit — now done, with T12 downgraded and T13 corrected.)*
