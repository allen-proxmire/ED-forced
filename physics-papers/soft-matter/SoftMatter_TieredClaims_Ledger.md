# Soft-Matter Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the `soft-matter/` folder, tiered.

**How it's built.** Read every paper; tier each claim **from the paper's own audit table, "does NOT claim" preamble, and verdict line** — never inflated. Where a paper labels a row `I`, `P-<name>`, `D-via-I`, `A→position` or `OPEN`, that label is carried here unchanged.

*17 papers. **First read 2026-09-04.** This is the arc's first ledger — see staleness #1.*

---

## Derived (M1 — pure structural, no numerical inheritance load-bearing)

**None.** No paper in this arc claims a D row that is not `D-via-I`, with a single composite exception:

| Claim | Paper | What's derived | Status |
|---|---|---|---|
| `D = 3+1` forced under PUA-1…PUA-7 | 075 §audit row 9 | composite of six `D-via-I` bounds on `D_s` and `D_t` | **D, but conditional on the seven PUA axioms**, which the same table labels **P** (row 1) and whose *substrate origin* it labels **I** (row 10). Not substrate-forced. |

**The arc's honest headline: its `Derived` tier is effectively empty.** `Paper_086_5` states this of itself explicitly — *"no D rows in audit"*.

## Grounded (M2/M3 — form-forced or form-identified + value inherited)

| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| **DCGT** — diffusion-form emergence under coarse-graining | 073 | the *form*, substrate-derived | transport coefficients inherited empirically | **M3** (form-IDENTIFIED + value-INHERITED), **scoped to the hydrodynamic window** `ℓ_ED ≪ R_cg ≪ L_flow` |
| Navier–Stokes equation from substrate coarse-graining | 076 | Eulerian `u(x,t)`, convective term, `ν` from V1 second moment + P11 dissipation | `ν` values; pressure via the incompressibility constraint | **D-via-I**, on `P-Hydro-Window` + `P-Incompressibility` + `P-Newtonian-Stress` |
| Vortex-stretching obstruction at substrate level | 084 | obstruction from P04 cap + V5 budget + P11 monotonicity | BKM-integral finiteness inherited | **D-via-I**, on `P-P04-Vorticity-Cap` + `P-V5-Stretch-Cap` |
| Cascade as channel–channel energy transfer | 078 | the transfer mechanism | Kolmogorov `k^{-5/3}` inherited | **D-via-I**, on `P-Channel-Hierarchy` + `P-Cascade-Direction-Dimension` |
| Standard MHD equations recovered | 081 | recovery | non-Abelian composition, Lorentz covariantization inherited | **D-via-I**, on `P-H1-Closure` + `P-H2-Induction` + `P-H3-Cascade-Closure` |
| **Advection and induction are frame-artifacts, not ED content** (T1/T2/T3 triangulation) | 082 | three independent `D-via-I` results | PUA-2 Galilean covariance; `Paper_030` ECR | **D-via-I** ×3, on `P-Frame-Artifact`. *The arc's cleanest structural result — it is a negative, and negatives are where this arc is strongest.* |
| Cross-platform kinematic-coupling map (NS ↔ MHD) | 083 | the map | its four inherited inputs | **D-via-I**, on `P-Unified-Kinematic-Coupling` |
| Photonic bandgap / negative index / cloaking from two-scale expansion | 086.5 | three `D-via-I` rows | Bloch, two-scale machinery, effective-medium `ε(ω), μ(ω)`, all designs | **M2 (Intermediate Path C)** — the paper states **no D rows** |
| Viscosity and resistivity ceilings are **one** P04 Adjacency-band budget | UnifiedP04 | the shared-budget identification | projection factors | **Working draft** — see staleness #4 |

## Selected / inherited (value from measurement)

| Item | Paper | Status |
|---|---|---|
| Kinematic viscosity `ν` for specific fluids | 076 | **I** |
| Krieger–Dougherty exponent `n`, `φ_max`, Maxwell `τ_M` | 079 | **I** |
| **`Q ≈ 3.5`** (NS-Q canonical operating point) | 080 | **I — canon-internal.** The same table marks *universality across platforms* **NOT CLAIMED** |
| Mobility-law numerical coefficients | 085 | **I** |
| Specific metamaterial designs | 086.5 | **I** |
| Kolmogorov `k^{-5/3}` | 078 | **I** |

## Postulated (paper-specific, declared at point of introduction)

24 named postulates across 17 papers — **the densest postulate load per paper of any arc**, and worth stating plainly rather than leaving to be counted:

`P-Polymer-as-Chain`, `P-Stress-from-V5` (074) · `P-Hydro-Window`, `P-Incompressibility`, `P-Newtonian-Stress` (076) · `P-Obstruction-Sufficient`, `P-R1-Sufficient-Strength` (077) · `P-Channel-Hierarchy`, `P-Cascade-Direction-Dimension` (078) · `P-Packing-Budget-Saturation`, `P-V5-Maxwell-Identification` (079) · `P-Canonical-Operating-Point-NS-Q`, `P-Q-Factor-Form` (080) · `P-H1-Closure`, `P-H2-Induction`, `P-H3-Cascade-Closure` (081) · `P-Frame-Artifact` (082) · `P-Unified-Kinematic-Coupling` (083) · `P-P04-Vorticity-Cap`, `P-V5-Stretch-Cap` (084) · `P-Mobility-V1-Friction`, `P-Mobility-Maxwell-Correction` (085) · `P-Adjacency-Transport-Shared`, `P-Scattering-Budget-Saturation` (UnifiedP04 / resistivity)

*Per `internal notes/POSTULATE_BASIS.md`, most of these are **single-paper** postulates — local modelling choices scoped to one derivation, not standing framework commitments. That is the honest reading and it is not a criticism; it is what the ladder's 60%-single-use figure describes.*

## Prediction (falsifier given)

| Claim | Paper | Kill condition |
|---|---|---|
| The MIR resistivity ceiling and the minimum-viscosity (KSS/Planckian) floor are **one** Adjacency-band wall | UnifiedP04 | resistivity saturation and the viscosity floor onset at **different** substrate budgets |

## Synthesis (composition; no new derivations)

| Claim | Paper | Status |
|---|---|---|
| Soft-matter arc consolidation: substrate-derived vs frame-artifact decomposition | 086 | **Synthesis** — all 13 content rows are `I`, final row `A→position`. Composes; derives nothing new. |
| V5 viscoelastic Maxwell ansatz, substrate-grounded | 074 | Opens the arc proper after DCGT |

## Open (declared)

| Item | Paper | State |
|---|---|---|
| Constructive proof of NS smoothness | 077 | **OPEN — explicitly not claimed.** The verdict is `A→position` at Intermediate Path C |
| Compressible / non-Newtonian / non-isothermal corrections | 076 | OPEN |
| Intermittency corrections to the cascade | 078 | OPEN |
| Universality of `Q ≈ 3.5` across platforms | 080 | **NOT CLAIMED** |
| Exact ratio `φ_max : ρ_max = Π_p/Π_q` | UnifiedP04 | OPEN — projection factors not derived |
| Substrate origin of the seven PUA axioms | 075 | **I** — the axioms are inherited, so `D = 3+1` is conditional on them |

---

## Staleness & refinements

1. **This arc had no ledger until 2026-09-04, and that made it invisible to the corpus's own audit.** The 2026-09-04 claim-strength pass swept the *fifteen arc ledgers* and reported covering *"all fifteen arcs"*. **`soft-matter/` has 17 papers and was not among them**, because it had no ledger to sweep — and it was not recorded as unaudited either. **The coverage claim was measuring the instrument, not the corpus.** Found while wiring a cross-reference for the migrated `Paper_ED_SC_4_5`. See `gravity/Gravity_TieredClaims_Ledger.md` Staleness #54 and the correction in `internal notes/AUDIT_2026-09-04_ClaimStrength_AllArcs.md`.

2. **`Paper_086_SoftMatter_Synthesis` quotes `ξ_canonical` to unsupported precision — flagged 2026-09-04, not yet corrected in the body.** The measured value is `1.76 ± 0.30` (`σ = 0.303`, ten seeds; smoothed variant `3.05 ± 0.53`), not `1.7575`. See `foundations/Paper_096` §7.

3. **This arc supplies one half of research target #15's singularity family, and the unifying lemma is a banked negative.** `Paper_077` (NS smoothness) and `Paper_084` (vortex stretching) are one of the two executed no-blow-up results built on the P04-cap + V5-cap + P11-ratchet triple. The attempt to abstract that triple into a domain-neutral lemma **failed** (target #15, attempted 2026-07-24): the general statement is near-definitional once the caps are granted, and the caps are *declared* here rather than derived. **Do not re-attempt the lemma without reading the banked negative.**

4. **Two papers are working drafts, not publication status.** `Paper_UnifiedP04TransportBudget` (*"working derivation draft"*) and `Paper_P04TransportBudget_ResistivitySaturation` (*"working scoping draft"*). The arc's only **Prediction** row rests on the first of them. Tier accordingly.

5. **An SCBU projection into this arc now lives in `cosmology/`.** `cosmology/Paper_ED_SC_4_5_SoftMatter_SCBU.md` projects `Q ≈ 3.5` onto `R_H = c/H₀`; migrated 2026-09-04 from a frozen fork, **M3 and unaudited**, and it carries the disputed `2π`. Kept with its series rather than here; pointer in this folder's README.

6. **`Paper_086_SoftMatter_Synthesis` was among the 31 files that diverged in the frozen fork** at `event-density/papers/Generative Papers/`. The canonical copy is this one.

---

## Honest arc-state

**A well-disciplined arc whose strongest results are negatives, and whose `Derived` tier is empty by its own admission.** Every paper labels its rows from its own audit table without inflation; `Paper_086_5` says outright it has *"no D rows"*, `Paper_080` marks universality **NOT CLAIMED**, and `Paper_077` declines the constructive NS proof and sits at `A→position`. The one composite `D` row (075's `D = 3+1`) is explicitly conditional on seven axioms the same table tiers `P` with substrate origin `I`.

**The cleanest structural content is `Paper_082`'s triangulation** — that advection and induction are *frame-artifacts of the convective derivative* rather than ED content, established three independent ways. A framework that can say precisely which parts of a standard PDE are **not** its own is doing something harder than claiming the whole equation, and this arc does it.

**The load is postulate-heavy: 24 paper-specific postulates across 17 papers**, most single-use. By the `POSTULATE_BASIS.md` ladder that is the expected shape for an applications arc rather than a foundations one, but it should be stated rather than discovered.

**What this arc has never had is an external claim-strength audit** (checklist §9 items 19–21: cross-section symbol sweep, strength-word grep, tier-inheritance and endpoint checks). Building this ledger is the prerequisite, not the audit. **The arc is now visible; it is not yet checked.**
