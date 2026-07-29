# Report — Pending Changes (post-v2.0.2)

> Changes to fold into the next report version. **Do not edit `ED_UnifiedFramework_Report.md` in place mid-cycle**; accumulate here, then apply as a batch. **The current Report is the one in the repo** — git commit dates are the versioning (dates *are* the version numbers). The last two content updates: §6 Cosmology/Dark-Sector (2026-07-19) and the a₀(z)/MUSE-DARK accuracy fixes (2026-07-21). Prior snapshots are archived on the Desktop, date-labeled.

---

## APPLIED 2026-07-19 — new §6 "Cosmology and the Dark Sector"

A new numbered section **§6 — Cosmology and the Dark Sector** was added to the report (after §5 Gravity, before the Unification Move), and **§6–§15 renumbered to §7–§16** (all cross-references, the abstract "boxes" list, and the scorecard updated). The section covers inflation (= substrate saturation, consilience) and the dark sector (MOND as the horizon-interference cross-term, native; the committed-neutral-relic candidate for the CMB; the two-component picture; the "no particle *for galaxies*, not no dark matter" clarification; the honest live risk). Dark energy left in §5/§11. Source: `physics-papers/dark-sector/`.

- **C1 — SUPERSEDED / do not apply.** Its "mimetic dust mode = `Ω_c`" and "conserved bandwidth current is natively that dust" resolutions were *retracted* by later 2026-07 work (the khronon does not natively carry the `a⁻³` dust — three checks; the CMB dark component is a *separate* relic, not the khronon's mode; MOND is the interference cross-term). Kept below for the audit trail only.
- **C2 — APPLIED** in the new §6 (with the interference-cross-term MOND and the "relic must be warm" correction that its older text lacked). The report now points to `physics-papers/dark-sector/`.

**Remaining:** rebuild the report PDF (`_build_report.py`) to reflect the new section — a build step, not a content change.

---

## NO REPORT EDIT 2026-07-29 — a₀(z) folder propagation reconciled *to* the Report

The corpus-hygiene sweep this session propagated the a₀(z) evolution + MUSE-DARK III data into the docs that predated it — `gravity/Paper_029` (new §8.8), `gravity/Paper_037` (preamble item 6), `gravity/Paper_038 §3.3 CO-3`, `gravity/Predictions_and_Falsifiers` (new Tier-2 live test), `predictions/22_Ways #1`, and `predictions/Paper_101` (promoted a₀(z) to Tier-1 weapon row 2). **Direction of travel was folder ← Report:** the Report's §15 flagship (~line 779) is the *most* accurate treatment in the corpus (it correctly attributes `α≈1.18` as an ED-side recast, not a MUSE-DARK figure; carries the survey's own "faster than H(z)"; hedges nominal ~4σ → ~1–2σ), so the folder docs were brought *up to* it. **No Report edit is owed for a₀(z)** — verified §15/§5/scorecard/abstract all current and mutually consistent (2026-07-29). Canonical source of truth remains `predictions/ED_Master_Predictions_List` 1.15. *(Also verified in passing: the Report's black-hole `1/4`/`2π` treatment, line 644 "near-horizon smoothness gives the 2π on top of κ," already matches the derived-`1/4` route imported to EDG this session as `black-hole/Paper_BH_Thermal2Pi_EntropyCoefficient` — no edit owed there either.)*

---

## APPLIED 2026-07-21 — a₀(z) evolution / MUSE-DARK III / the α = 1.18 provenance

**Status: APPLIED 2026-07-21 to the Report (§15 flagship ~line 779: α≈1.18 reattributed as an ED-side re-fit + the survey's real numbers [~30σ, a₀ 1.2→2.38 by z~1, "faster than H(z)"] added; scorecard row softened). PDF rebuilt. Verified against the real A&A source.** Kept below for the audit trail. The report's a₀(z) treatment is **largely accurate and honest** — it already gets the hard part right (α = 1 is *mechanism*-forced, not dimensional, since ED has ℓ_P; forward-dated; honestly hedged as "evolution confirmed, exact rate mildly disfavored, not a refutation"). Only one real issue plus optional strengthening.

**The verified paper facts** (MUSE-DARK III, *A&A* 2026, article `aa59230-26`; arXiv `2604.22613`), to use as the source of truth:
- ~30σ detection of acceleration-scale evolution across `0.33 < z < 1.44`; a *constant* `a₀` excluded.
- `a₀` rises from `a₀(z=0) = 1.2 ± 0.26` (SPARC local) to **`a₀(z∼1) = 2.38 (+0.12/−0.10) × 10⁻¹⁰ m/s²`**.
- The paper fits a **linear** `a₀(z) = a₀(0) + a₁ z` (`a₁ ≈ 1.59 × 10⁻¹⁰`), called "a simple phenomenological description."
- The paper's own conclusion: the measured `a₀(z)` runs **"faster than that of H(z)"** and is "in tension with the scale-invariant vacuum paradigm."

**Change 1 (the real fix) — §15 flagship (~line 779) + wherever "α ≈ 1.18" appears.** Current text reads *"a direct fit gives α ≈ 1.18 ± 0.04,"* which a reader takes as the survey's reported figure. **It is not.** The survey reports a *linear* fit and "faster than H(z)"; the `α ≈ 1.18` is a power-law **recast of the survey's points** (the ED-side "direct α fit / addendum A10," 2026-07-14), not a quantity MUSE-DARK III reports. **Reattribute**, e.g.: *"recasting the survey's measured evolution as a power law gives α ≈ 1.18 (the survey itself fits a linear a₀(z) and states the evolution runs faster than H(z))."* Keep the existing "nominal ~4σ → ~1–2σ under systematics" hedge; note the ±0.04 is the recast's error, which the corpus itself flags as underestimated.

**Change 2 (optional strengthening) — §15 and the gravity body (~line 297).** Ground the tension in the survey's *own* numbers/words rather than the ED recast: add "`a₀` rises from 1.2 to `2.38 × 10⁻¹⁰` by `z∼1`" and the verbatim "faster than H(z)." Stronger and less dependent on the recast.

**Change 3 (minor) — scorecard row (~line 113).** "exact rate mildly disfavored (~4σ nominal, one survey)" — the bare "~4σ nominal" is the recast's face value; align it with the body's more careful "~1–2σ under systematics; the data run faster than `H(z)`."

**Source:** https://www.aanda.org/articles/aa/full_html/2026/05/aa59230-26/aa59230-26.html ; arXiv 2604.22613.

---

## FIXED 2026-07-21 — dark-sector flagship paper (not the report)

**Status: DONE in `physics-papers/dark-sector/Paper_ED_DarkSector.md` (abstract + §6), PDF rebuilt.** The new DM flagship had the *opposite* error from the report: its §6 and abstract said a₀(z) is *"unfudgeable: ED has no second scale … dimensionally forced."* Corrected to the report's accurate framing — ED *does* carry ℓ_P, so a bent power is dimensionally legal; α = 1 is **mechanism-forced** (Paper_029's horizon projection introduces no ℓ_P, plus the no-intrinsic-scalar result leaves no dimensionless number to bend it). Not a report change; logged here for the audit trail.

---

Each entry: what changes, where, current text, proposed replacement, why, and status.

---

## C1 — §5 "The debts": the CMB/cluster debt  **[NO REPORT EDIT — the current §5 language is correct as-is]**

**Status (updated 2026-07-19): NO CHANGE TO THE REPORT.** The knot-1 pass turned the first-pass "sharpening" into a fuller finding (below), and the conclusion is that the report's current §5 language — "clusters and the CMB are a **live falsification risk, not a bookkeeping debt** … if that dial cannot thread the CMB acoustic peaks and the clusters, the sector fails" — is **exactly right and needs no edit.** The finding is a *reconciliation of an internal contradiction*, not a discharge of the debt; a reconciliation with an unbuilt demonstration does not earn a flagship claim. **Do not touch §5 until the one-field Boltzmann demonstration exists.** The corpus edits that the finding *does* warrant were applied to the source papers (Cos_03/Cos_04), not the report.

**Knot-1 finding (2026-07-19), for the record — where the debt actually sits:**
- The cosmology arc (Cos_03 CMB, Cos_04 structure) silently **runs on cold dark matter** (`Ω_c h² ≈ 0.12`, ~5× baryons, the Planck ΛCDM value, inside `Ω_m h² ≈ 0.143`) that the gravity arc (KM-I) denies — a cross-arc contradiction hidden under an "IC-inherited" label.
- Resolution: the khronon is a **field**, not the foliation function `𝒲(0,Θ)`; its **mimetic dust mode `ρ=C/a³`** supplies the `a⁻³` abundance via an integration constant (the volume memory the local-dial no-go correctly showed a function-of-H cannot have). Identify Cos_03/04's `Ω_c` with that mode → not a particle, the cosmological face of the MOND field. Double-counting avoided by one-field-one-solution-per-regime (Orthogonality Theorem; AeST is the sister-theory existence proof).
- **Unbuilt (what would actually retire the debt):** a direct one-field Boltzmann computation of the peaks + the galactic curves from the khronon dust (currently the value is inherited via a ΛCDM-CDM proxy in CAMB/CLASS); plus the `(□φ)²` instability regulator.
- **Corpus edits applied 2026-07-19:** "Dark-component identification" note added to `Paper_ED_Cos_03_CMBAcoustic.md` and `Paper_ED_Cos_04_StructureFormation.md`; `ED_Research_Targets.md` §5b + memory `project_cmb_dust_mimetic_debt` updated. The report was deliberately left unchanged.

**(Superseded) original C1 rationale:** rests on a first-pass chain (2026-07-17); the report's §5 was already correctly honest, so this was only a candidate *sharpening*, gated on verification. The knot-1 pass resolved the gating question in favor of "no report edit."

**Where:** §5, "The debts," the CMB/clusters bullet (currently ~line 300).

**Current text (correct as-is):**
> Clusters and the CMB are a live falsification risk, not a bookkeeping debt. This is where khronometric/MOND theories characteristically die, and KM-II is explicit that it does *not* discharge them: no regulator member is chosen, no CMB spectrum is computed, no cluster profile is fit… If that dial cannot thread the CMB acoustic peaks and the clusters, the sector fails.

**Proposed sharpening (only if the chain verifies):** add one sentence locating the debt more precisely —
> *The debt is now more sharply located than "the dial is unset": a khronon cosmological sector local in the expansion rate supplies the CMB's clustering condition (`c_s ≈ 0`) but not its dust **abundance** (`∝ a⁻³` at recombination), which is structurally a separate, volume-memory quantity; ED's conserved bandwidth current is natively that dust, but whether a **photon-decoupled** component (the cold dark matter the CMB peaks require, ~5× baryons) exists distinct from baryons — and whether it avoids double-counting against galactic MOND — are the two open knots. The Orthogonality Theorem sequesters the dial, not the dust abundance.*

**Why:** turns the debt from "MOND theories die here / dial unset" into two specific, testable knots. But it imports internal first-pass reasoning into the flagship, so it must clear verification first — otherwise it's exactly the skim-vs-detail / over-banking drift the report has been cleaned of.

**Verification gate (must pass before applying C1):**
1. Confirm the local-`𝒲(0,Θ)` no-go (the `ρ∝H²` vs `H^{3/2}` era argument) with the full KM-II §5–6 equations, not the grep excerpts.
2. Resolve open knot 1 — does ED have a photon-decoupled ~5×-baryon dark component, or is the native dust just baryons? (If just baryons, the whole sharpening collapses and the honest report change is the *opposite*: flag that ED may lack a CMB dark component entirely.)
3. Resolve/scope open knot 2 — the galactic double-counting.

---

## C2 — §5 dark-matter position: state the full picture and point to the dark-sector folder  **[apply next report cycle]**

**Status: TO APPLY (documentation clarity, not a physics change).** §5 currently frames clusters/CMB as a "live falsification risk," which is correct but *incomplete* — it lets a reader infer ED claims "no dark matter," which ED does not. The 2026-07-19 dark-sector work created a canonical home for the full position (`physics-papers/dark-sector/`); the report should carry a compact version of it and point there.

**Where:** §5 (the dark-matter / MOND paragraph).

**What to add (compact):**
> ED explains galactic dynamics without a dark-matter *particle* (MOND/khronon) — but this means a particle is *not needed for galaxies*, **not** that ED claims none: ED does not refute dark matter as particle content (Paper_029/031). Clusters and the CMB are a *separate*, mapped debt (MOND-class theories all share the cluster shortfall), with a native candidate — a committed neutral relic from the saturation exit (decoupled, cold-capable, `a⁻³`), form-complete and value-inherited, its free-streaming length the one open number (expected cold — a live risk). Full statement: `physics-papers/dark-sector/`.

**Why:** prevents the exact misreading a referee (and this project's own working notes) fell into — treating the inherited `Ω_c` in the cosmology papers as an unflagged contradiction with the gravity arc's "no dark matter." The dark-sector folder is the fix; the report just needs to reflect and point to it.

**No verification gate** — this is documentation of an already-standing position, not a new claim.

---

## Provenance (2026-07-17)

Source: the CMB/cluster-debt work session (task 1 = the local-dial dust no-go; task 2 = GR-II native-dust; the OneField capstone reconciliation; the adversarial downgrade). Full detail: memory `project_cmb_dust_mimetic_debt`; map entry: `event-density/docs/ED_Research_Targets.md` §5b. **Nothing here is applied to the report; C1 is a candidate gated on verification.**
