# Soft-Matter Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the `soft-matter/` folder, tiered.

**How it's built.** Read every paper; tier each claim **from the paper's own audit table, "does NOT claim" preamble, and verdict line** — never inflated. Where a paper labels a row `I`, `P-<name>`, `D-via-I`, `A→position` or `OPEN`, that label is carried here unchanged.

*17 papers. **First read 2026-09-04.** This is the arc's first ledger — see staleness #1.*

---

## Derived (M1 — pure structural, no numerical inheritance load-bearing) — workbook tier: PER ROW (see rule below)

> **Transcription rule — `ED_ItemizedTheory_TieredClaims*.xlsx`.** That workbook's `Derived` tier is **narrower than this heading**: *“forced/proven from the 13 primitives (+ standard math) with **NO** paper-specific postulate.”* **This section is mixed, so take the tier from the ROW, never from this heading.** If a row's *“Inherited / open”* cell names a `P-` postulate, or says *conditional on* / *rests on*, its workbook tier is **`Grounded`** — or **`Postulated`** where the postulate carries the claim — **not `Derived`**. *(Here: **0 of 1** rows currently name a postulate.)* **Losing this qualifier in transcription over-promoted ten rows before 2026-09-06**, because the caveat lived in a parenthetical and parentheticals do not travel. See `gravity/Gravity_TieredClaims_Ledger.md` #122 and #124.


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
| ~~Exact ratio `φ_max : ρ_max = Π_p/Π_q`~~ → **invariant product `Λ = η_minρ_max e²/p_F² = Π_pΠ_q`** | UnifiedP04 §9 | **CLOSED IN FORM 2026-09-05, D-via-I.** `Π_p = 1/3`, `Π_q = 1`; `n`, `a_eff`, `b_adj^max` and the coupling all cancel. **Two corrections en route:** the pairing (§8, `φ_max`→`η_min`) and the **ratio→product** (§9.1 — `η_min ∝ a`, `ρ_max ∝ 1/a`, so the ratio scales as `a²`). **Value stays inherited:** `Λ ∈ [1/5, 1/3]`, the width a kinetic-averaging convention. |
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

7. **Claim-strength pass run 2026-09-04 — ~~one finding~~ **NO FINDING; the arc is clean without qualification (settled same day, gravity Staleness #57).** The four-band partition **is** canonical primitive-level content (P04 §1.5) — the M-series archive removed the *forcing argument* for it, not the partition, and `ARCHIVED_M_SERIES_NOTICE.md` explicitly retains the Forcing Papers #1–#19. **`Paper_UnifiedP04TransportBudget`'s `P (primitive)` tier is correct and this arc's Prediction needs no re-grounding.** The defect was upstream, in a 2026-07-29 foundations ledger entry. *Superseded finding:*  `Paper_UnifiedP04TransportBudget` tiers *“P04 four-band partition; Adjacency = P05-transport content”* as **P (primitive)**, citing `primitives/P04` §1.5. **Canonical `Paper_087` has no four-band** — it defines P04 as bandwidth, a non-negative additive scalar — and `Foundations_TieredClaims_Ledger.md` staleness #2 records four-band as **archived M-series** content. **This arc's only Prediction row rests on that tier**: without a band partition, *“the Adjacency band”* has no referent. **A tier problem, not necessarily a physics problem** — the shared-budget identification may survive on P04 additivity + P05-as-sole-transport without four *named* bands, which would be a re-grounding rather than a retraction. Flagged in the paper; **not attempted**. Corpus-wide scope: `gravity/Gravity_TieredClaims_Ledger.md` Staleness #56.

8. **Everything else in the pass came back clean, and that is worth recording as a result.** **Strength-word grep (item 20c):** every `FORCED` in the arc is correctly split from its inherited value — `Paper_076` *“the **scaling** is FORCED; the **numerical prefactor** is INHERITED”*, `Paper_079` *“the structural divergence is FORCED; the numerical exponent and packing limit”* are not. **Tier inheritance (item 20a):** `Paper_075` handles its own pre-pivot inheritance exemplarily — it cites the R.2.4 / spinor-bundle `D=3+1` result, names it *“pre-pivot designation”*, and maps it to the canonical **P06** under `Paper_087` rather than leaning on the archived form. **Premise naming (item 20b):** `Paper_075` states plainly that it does **not** claim `D = 3+1` is forced by substrate primitives alone, nor that the seven PUA axioms are minimal. **No archived M-series or §N.M citations** anywhere in the arc except the four-band item above. **The arc's papers do not overclaim.**

---

## Staleness 2026-09-05 — one false comparative claim, corrected

**`Paper_UnifiedP04TransportBudget` §8 read** *“Standard physics has no reason to unify them; ED forces it”* of the MIR resistivity ceiling and the KSS/Planckian viscosity floor. **False, and self-contradicting**: the same paper says three lines earlier that the field *“actively debates whether they are the same physics.”* **Zaanen (2019), SciPost Phys. 6, 061 (arXiv:1807.10951), argues precisely this unification.** ED enters an open debate on one side; it does not supply a link nobody had reason to draw. **Corrected in place**, with the discriminator relocated to the underived `η_min : ρ_max` ratio — which makes `Π_p`, `Π_q` the arc's load-bearing open step rather than a refinement. **This is the arc's first substantive correction since its ledger was built (2026-09-04), and it came from outside the corpus, not from re-reading it.** Gravity ledger Staleness #61.

---

## Progress 2026-09-05 — the `Π_p`/`Π_q` step is run; the arc's R2-analog closes in form

**Closed in form the same day the arc's one false comparative claim was corrected**, and by the route that correction opened: relocating the discriminator to `η_min : ρ_max` made the step tractable, because both walls are floored at one length and the algebra is textbook once that is granted.

**Result.** `Π_p = 1/3` (kinetic shear viscosity at the floor), `Π_q = 1` (Drude at the floor), and

$$\Lambda \;\equiv\; \frac{\eta_{\min}\rho_{\max}e^{2}}{p_F^{2}} \;=\; \Pi_p\Pi_q,$$

with **`n`, `a_eff`, `b_adj^max` and the coupling all cancelling.** Equivalent form: `η_minρ_max = (ħk_F²/6π)·R_K`, the product of the two transport walls being the resistance quantum times a purely geometric carrier factor. **Verified numerically in three independent forms plus an `(n, a_eff)`-independence sweep** — `internal notes/_check_transport_invariant.py`, re-runnable.

**Two corrections were required to get there, and the second was in this paper's own last update.** §8 (2026-07-30) had already fixed the *pairing* (`φ_max` → `η_min`). But it then asserted that *“their ratio `η_min : ρ_max` is an O(1) that cancels `a_eff`”*. **It does not.** `η_min ∝ a_eff` and `ρ_max ∝ 1/a_eff`, so the ratio scales as `a_eff²` and **the product is the invariant.** F-RATIO had been written against the ratio and was therefore untestable as stated. *Same-kind does not mean same-sign: one floor, entering two transport coefficients with opposite powers.*

**What this does to the arc's load-bearing posit, and it is the most useful part.** The `a_eff` cancellation happens **only** because one length floors both transports. With two floors the algebra returns `Λ = Π_pΠ_q·(a_η/a_ρ)`. **So `Λ` is a direct measurement of `P-Adjacency-Transport-Shared` itself**, not a comparison against a computed number — which is a better falsifier than the one the paper was reaching for. **F-RATIO restated accordingly, and the sharper half is the drift test:** `Λ` must not track lattice spacing, carrier density or material, and that test is **independent of the unresolved `[1/5, 1/3]` coefficient band.**

**F-CONVERGE, new and the cheapest test in the arc.** Standard treatments keep the momentum-conserving and momentum-relaxing lengths distinct — electron hydrodynamics is *defined* by `ℓ_ee ≪ ℓ_mr`, established by orders of magnitude in graphene, PdCoO₂ and WP₂. **ED does not contradict that**, since its claim is about the wall, where both floor at the cell. **But it does require the two lengths to converge on approach**, and a system driven to MIR saturation with them still orders apart falsifies the posit **with no viscosity measurement at all.**

**Tier discipline, stated because the temptation here is real.** The result is **`D-via-I`, not substrate-native.** The ED content is one sentence — at the wall the two mean free paths are the same length because they are the same band — and inherited kinetic theory supplies everything else. **The `1/3` is a kinetic-averaging convention, not a forced number**: the degenerate-Fermi-gas transport result gives `1/5`, and at the wall, where quasiparticles are marginal, neither scheme is clearly right. **That ambiguity is inherited and is not closable from the substrate**, so the claim is the existence and parameter-independence of `Λ`, never its value. Gravity ledger Staleness #62.

**Filed as ML 4.11 the same day.** **Propagation failure caught in passing, and it is a bad one.** The transport arc's predictions — co-onset included, which the paper calls its *“distinctive, falsifiable, ED-owned content”* — **had never been entered in `ED_Master_Predictions_List.md` at all.** A distinctive falsifiable bet sat outside the corpus's own prediction inventory from the paper's writing until today. **Now ML 4.11**, filed under Quantum Foundations and Soft Matter with all three legs (co-onset, the `Λ` drift test, F-CONVERGE) and the Lucas–Hartnoll contrast. **Item 21's third face again: the inventory is a propagation target, and nothing had flagged the omission because nothing cross-checks arc papers against the master list.**

---

## Staleness 2026-09-05 (second entry) — F-CONVERGE does not run, and the wall's identity is now the arc's open question

**`Note_FConverge_Run_2026-09-05.md` (new).** F-CONVERGE is **not runnable**: `ℓ_ee` and `ℓ_mr` are measured in disjoint windows in every established system. Three findings came out of establishing that.

1. **Bad metals do not saturate.** Gunnarsson, Calandra & Han (RMP 75, 1085) name high-T꜀ cuprates and alkali-doped fullerides as violating Ioffe–Regel; the extracted mean free path passes below the interatomic spacing with no saturation. **The arc points at the one material family with no wall.** Dilemma: if `a_eff` is the interatomic spacing the floor is violated; if it is not, MIR saturation is not ED's wall and §3's `ρ_max` identification is wrong. **Banner added to §3.**
2. **The Dirac fluid is the one candidate venue and is awkward** — viscosity at/near its floor while resistivity is far from MIR. **A tension with F-COONSET, not F-CONVERGE.** Three escapes named; not banked.
3. **§9's `Π_p`/`Π_q` are derived from Drude and kinetic theory evaluated *at* the wall, where both fail.** Not a coefficient problem — a domain problem, and it undercuts `Λ`'s parameter-independence claim rather than its value. **Banner added at the head of §9. Cheapest repair: restrict `Λ` to the regime approaching the wall, turning it into a limiting statement.**

**Withdrawn:** the same-day claim that F-CONVERGE was *“the cheapest test in the arc.”* **ML 4.11 re-marked scoped, not live.** **The arc's load-bearing open item is no longer `Π_p`/`Π_q` — it is why the Adjacency-band wall should be the MIR wall at all.** Gravity ledger Staleness #65.

---

## Staleness 2026-09-05 (third entry) — `a_eff` settled; the arc no longer explains MIR

**`Note_WhatIsAEff_2026-09-05.md` (new).** `a_eff` is **three physically distinct lengths under one symbol**, and the symbol appears **only** in the two transport papers — **not once in `Paper_073_DCGT`, which they cite as its source.** P08's `ℓ_ED` (`1.6×10⁻³⁵ m`), the DCGT cell `R_cg`, and the interatomic spacing (`3×10⁻¹⁰ m`, what every number uses). **Twenty-five orders between the first and the third.**

**Neither derivation route survives.** DCGT §3.1 makes `R_cg` a **chosen** scale with results *“insensitive to the specific choice”*, so a floor there would make a measurable quantity depend on a bookkeeping decision. And **coarse-graining a floor at `ℓ_ED` does not install a floor at `R_cg`.** The load is carried by one asserted sentence.

**`F-EXIST` has fired.** Its condition — *“charge transport that continues rising without any saturation”* — is the documented behaviour of bad metals. **It had been marked a** *“consilience pass”* **on the confirming half of the literature only.** Forks: either the postulate is falsified in cuprates and fullerides, or the mechanism has no purchase in that regime and **F-COONSET has no venue**.

**Settled: `a_eff` is the material's emergent transport cell, inherited.** P08 and DCGT leave the chain; `ρ_max` re-tiered *identification/consilience* → **I**. **ED does not explain MIR; it inherits it.** The *sharing* claim survives and was always the distinctive part; **`Λ` survives untouched**, cancelling `a_eff` whatever it is. Gravity ledger Staleness #66.
