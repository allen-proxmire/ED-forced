# Scale Invariance — Reader's Map

*EDG-side snapshot of the Event-Density scale-invariance material. The working source of truth for these files is the `event-density` repo; this folder is a publication snapshot. Last reconciled 2026-06-23.*

This folder collects the ED work on **what survives coarse-graining** — which substrate quantities are invariant across scales, and how solid each claim is. The honest headline: the strong results are a couple of clean cross-scale constants; the saddle-geometry arc resolved into a *classification* plus a *retired* scalar; and the statistical backbone rests on an unproven Gaussianity assumption.

---

## Three invariance threads (they are not the same claim)

1. **Boundary projections (ED-SC 4.x).** One cosmic boundary `R_H = c/H₀` reappearing as six constants across four regimes, with the H₀ co-variation falsifier. *(Lives mainly in `../` and the EDG whitepaper/SCBU; not duplicated here.)*
2. **Saddle-geometry / motif statistics (ED-SC 3.x).** Classify the saddle geometry of the substrate participation-action into **S1 (cross-scale invariant) / S2 (ensemble-only) / S3 (motif-specific)**, with the motif-conditioned distribution `p(X|M)` as the flagship S1 invariant. *(`Paper_EDSC_Motif`, `Paper_EDSC_rstar`, `Paper_EDSC_SaddleClassification`.)*
3. **Canonical-PDE / simulation invariants.** Dimensionless numbers the canonical ED PDE and the ED-SIM program hold across scales. *(`Universal_Invariants.md`, `invariant_map.md`.)*

All of 2 and 3 hang off Paper_096's S1-invariance principle and the canonical operating point **ξ_canonical = 1.7575 lu** (which is *measured / canon-internal*, not derived — see OPENs below).

---

## Files

| File | What it is | Verdict |
|---|---|---|
| `Paper_037_a0_Invariance_CHECK.md` | `a₀ = cH₀/(2π)` is continuum-limit invariant (substrate-c constant + H₀ a global boundary condition). The cleanest concrete result. *(Also filed in `physics-papers/gravity/` — deliberate cross-file; keep the two in sync.)* | strong / structural |
| `Universal_Invariants.md` | Canonical-PDE invariant block: `D_crit(ζ=¼) ≈ 0.896`, `E_ground = αγρ₀`, `t_rel ≈ ρ₀/αγ`, and `D·T₀/L₀² = 0.3` across 5 regimes / 61 orders of magnitude. | PDE theorems (sim-confirmed) |
| `invariant_map.md` | ED-SIM v1 reference: 16 measured invariant families + 3 meta-analyses, graded by coefficient of variation (INVARIANT < 5%, WEAKLY < 15%). | measured |
| `Paper_EDSC_MotifConditioned_Invariant.md` | `p(X|M)` invariant under DCGT in the hydrodynamic window — the S1 statistical content. | M3, conditional on GRF |
| `Paper_EDSC_SaddleClassification.md` | The S1/S2/S3 saddle taxonomy. | M3, form-IDENTIFIED; exhaustiveness OPEN |
| `Paper_EDSC_rstar_FilteredGRF.md` | `r*` as a filtered-GRF statistic. **Honest negative** — see below. | M3 (structural form only) |

---

## Honesty tiers (read this before citing anything here)

- **Strong / structural.** `a₀` continuum-invariance (clean composition: c is coarse-grain-constant, H₀ is a global boundary condition). The dimensionless `D·T₀/L₀² = 0.3` across 61 orders of magnitude.
- **PDE theorems (simulation-confirmed).** `D_crit ≈ 0.896` (corrected from a retired 0.5 heuristic that was ~80% off), `E_ground`, `t_rel`, and the 16 ED-SIM families.
- **Structurally framed but genuinely weak.** The motif-conditioned distribution and the S1/S2/S3 classification — both rest on assumptions flagged OPEN below.

**Model-internal vs nature.** The PDE/ED-SIM invariants (e.g. `D·T₀/L₀² = 0.3`) are invariants *of the ED model/simulator across scales*, in ED-Phys natural units — **not** empirically measured invariants of nature. State that distinction whenever they're used as evidence.

---

## The r\* retirement (the load-bearing honesty item)

`r*` was promoted to a scalar cross-scale invariant, then **retired (2026-04-23)** by a falsifier audit. The corrected facts:

- The pooled **R² ≈ −1.88 ± 0.4** is a *goodness-of-fit* value — it is **negative**, i.e. the `r*` predictor explains **less** variance than a constant-mean null. It is **not** the value of `r*`.
- The formerly-reported scalar `r*` median was **≈ −1.304**. (Do not cite "r\* ≈ −1.88" as the statistic's value — that conflation was corrected in `Universal_Invariants.md` and both `Paper_EDSC_*` files on 2026-06-23.)
- What survives is the **structural form** (`r*` as a filtered-GRF statistic), not an invariant or a working predictor. Being filter/motif-dependent, `r*` is **not S1**; its landing class (S2 vs S3) is unsettled by the source language, which calls it both *motif-* and *filter-conditioned*.

This is the program policing its own overclaim — keep it visible; it's a credibility asset, not a wart.

---

## Cross-cutting OPENs

- **ξ_canonical = 1.7575 lu is inherited, not derived.** Every ED-SC 3.x file consumes it as canon-internal; the substrate derivation (Route A: `ℓ_V5(H₀)`) is OPEN. EDG's whitepaper claims Route A closed only at the *value-inherited* level (Paper_ED_SC_4.2); the from-primitives derivation (Routes B/C → M1) is still open. So everything downstream inherits that.
- **GRF Gaussianity is a regime hypothesis, not derived.** The whole S1 motif sub-arc (`Motif`, `rstar`) assumes the coarse participation field is a Gaussian random field. This is *attemptable* — CLT for a finite-reach field (V1 width + V5 memory ⇒ finite correlation length under DCGT averaging), or RG-irrelevance of higher cumulants at a Gaussian fixed point — **but** it collides with the CoarseGrain/ShadowEmergence finding that ED's dynamics are *committal/trapping, not mixing* ("you reach the PDE only by leaving ED"). Gaussianity may therefore be **false**. The cheap next step is a build-and-run, could-say-no test: measure higher cumulants / Wick-factorization residuals of the coarse field across the hydrodynamic window, reusing the GRF-linearization pipeline `r*` already built.
- **Saddle-class exhaustiveness OPEN.** The S1/S2/S3 trichotomy is exhaustive by partition-axis *construction*, not by a substrate theorem; a fourth class is not ruled out.

---

## Source-of-truth note

These are copies. The originals (and today's corrections) live in `event-density`: `theory/Universal_Invariants.md`, `papers/Forcing Papers/Paper_EDSC_*.md`, `papers/Generative Papers/Paper_037_a0_Invariance.md`, and `archive/legacy_research_history/.../invariant_map.md`. Relative links inside `Universal_Invariants.md` and `invariant_map.md` point at the working-repo tree and are inert here. Edit in `event-density`; re-snapshot here.
