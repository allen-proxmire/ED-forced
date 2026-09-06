# Dark-Sector Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the dark-sector folder and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing with a row is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** This folder has **two papers**, both explicitly and honestly self-tiered (a §8 tier table in the flagship; a Tiers section in the construction). For a folder this small — and this retraction-heavy — **both papers were read in full and directly, no extraction agent**; every row below is first-hand sourced, so the read *is* the spot-check. Seeded from the folder README + memory; corrected against the papers where needed (none needed — the papers' own tiers held).

**One of a per-folder set.** Companions: `entanglement/…`, `black-hole/…`, `cosmology/…`. This folder *synthesizes* standing results (KM-I, 027–034, QuadraticStrain, Baryogenesis, Mass-Without-Mass, MS-II); it does not supersede them.

**Tier key.** `Standing` (a prior corpus result, cited not re-derived) · `Derived` (forced/computed here or in the companion) · `Grounded / structural` (standard form + corpus content) · `Native / V5-conditional` (mechanism native but resting on V5, a faithful structural addition not shown primitive-forced) · `Selected/Inherited` (a value ED does not fix) · `Prediction` (falsifiable bet) · `Open` · `Superseded/Resolved`.

*2 papers, July 2026. Read 2026-07-29, in full and directly (no agent). The folder is internally current: L_self is RESOLVED (2026-07-19, canonical → two-component), and the a₀(z) flagship carries its first-data status inline.*

---

### Standing (a prior corpus result, cited here, not re-derived)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Galactic dynamics from MOND/horizon, **no dark-matter particle** | (KM-I / 027–034) | — | standing prior result; the sector's strongest, *separate* piece | current |
| MOND = the off-diagonal **horizon-interference cross-term**; `√(a_N a₀)` forced | QuadraticStrain / 030 | `P=√b·e^{iπ}`, `Str=|ΣP|²` splits diagonal (Newton) + off-diagonal (MOND) | standing / structural | current |
| Baryonic Tully-Fisher slope-4 + near-zero scatter | 031 | exact consequence of the combination rule | **MOND-SHARED** — discriminates ED+MOND from ΛCDM, NOT ED from MOND; the ED-distinctive part is only the a₀ normalization | current — honest distinction stated in §3.2 |
| Cluster missing-mass shortfall filled by the relic | DarkSector §4.1 | real collisionless matter clustering at cluster scale | the warm-keV window keeps it diffuse in galaxies, clumped at clusters — narrow, the live risk | current — structural |

### Derived — workbook tier: PER ROW (see rule below)

> **Transcription rule — `ED_ItemizedTheory_TieredClaims*.xlsx`.** That workbook's `Derived` tier is **narrower than this heading**: *“forced/proven from the 13 primitives (+ standard math) with **NO** paper-specific postulate.”* **This section is mixed, so take the tier from the ROW, never from this heading.** If a row's *“Inherited / open”* cell names a `P-` postulate, or says *conditional on* / *rests on*, its workbook tier is **`Grounded`** — or **`Postulated`** where the postulate carries the claim — **not `Derived`**. *(Here: **0 of 5** rows currently name a postulate.)* **Losing this qualifier in transcription over-promoted ten rows before 2026-09-06**, because the caveat lived in a parenthetical and parentheticals do not travel. See `gravity/Gravity_TieredClaims_Ledger.md` #122 and #124.

| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| `a₀ = cH₀/(2π)`, parameter-free ~10% match | 029 | the `2π` from azimuthal-Fourier normalization of the dipole projection | ~10% **postdiction**; a₀ value inherited via H₀ | current | **[DISPUTED 2026-09-04 — the `1/(2π)` is not established as forced.** The azimuthal-Fourier normalization does **not** survive: `Paper_028` §6.3 and `Paper_029` §5.1 both evaluate the azimuthal integral to **1**, so the factor cancels in their own displayed algebra and is reinstated at an assembly step by a normalization fixed nowhere. Re-tiered **Postulated / disputed**; see `Gravity_TieredClaims_Ledger.md` Staleness #10. **Unaffected:** `a₀ ~ cH₀`, reached three independent ways, and `a₀(z) = cH(z)/(2π)` with its forced exponent of 1.]**
| **`a₀(z) = cH(z)/(2π)` EVOLUTION** (flagship bet) | DarkSector §6 | unfudgeable **shape** (horizon projection introduces no ℓ_P; ED's no-intrinsic-scalar result leaves no free dimensionless number to bend the power) | **evolution CONFIRMED ~30σ** (MUSE-DARK III, A&A 2026), excludes constant a₀ / kills constant-scale MOND; **exact rate ∝H(z) in MILD TENSION** — data run *faster* (~1–few σ, one first-gen survey) | current — **FLAGSHIP: direction won, exact rate under tension. Do NOT over-bank; Rubin/Euclid decide** |
| Relic `ρ ∝ a⁻³` from the **P11 commitment number** | RelicLagrangian §3.4 | Noether current of the global U(1); `∇_μJ^μ=0` **IS** P11 (commitment-irreversibility) ⟹ `n·a³=const` | derived **given the field content** of §2; supplies the volume memory a modified-gravity dial structurally lacks | current — **the sector's one genuinely-new derived headline** |
| Sector is **TWO-COMPONENT**, not one substance (`L_self` coarse-grains **canonical**) | RelicLagrangian §3.3 | `cos` kernel analytic ⟹ gradient expansion gives only analytic powers ⟹ canonical `p≈1.99` on the real V5 functional; no `(∇θ)^{3/2}`, no a₀ | derived + numerically confirmed; one open edge = the non-perturbative/vortex sector (minor) | current — **RESOLVED 2026-07-19** (supersedes the open self-term + the retracted khronon-mode probe) |
| Pressureless-dust limit `w≈0` (fast-oscillating massive scalar) | RelicLagrangian §3.2 | `⟨p⟩→0` for a massive scalar with `θ̇≈m_R` | — | current |

### Grounded / structural
| Claim | Paper | Note | Status |
|---|---|---|---|
| Committed **neutral relic** candidate for clusters/CMB | DarkSector §2 / RelicLagrangian §1 | **form-complete / native** — neutral-channel sibling of the baryons (Baryogenesis) + binding mass (Mass-Without-Mass) + channel/polarity (MS-II) | current |
| Field content `Φ = √(ρ/m_R)e^{iθ}` = coarse-grained neutral-channel participation measure | RelicLagrangian §2 | structural (standard condensate/Madelung form + corpus field content) | current |
| Khronometric kinetic form `L_kin` (time-along-`u` + spatial `c_⊥`) | RelicLagrangian §3.1 | structural — the two-speed split is the arrow's preferred frame, not chosen by hand | current |

### Native / V5-conditional
| Claim | Paper | Note | Status |
|---|---|---|---|
| Relic is **massive by V5 binding**, cold-capable | RelicLagrangian §3.2 | mechanism native but **V5-CONDITIONAL** (V5 = a faithful structural addition, not shown primitive-forced); mass *value* inherited | current |

### Selected / inherited (a value ED does not fix)
| Item | Paper | Status |
|---|---|---|
| Relic mass `m_R` | RelicLagrangian | **INHERITED** (η_B tier). Mechanism-preferred value is **cold GeV–Planck — 6–26 OOM heavier** than the needed warm window (the quantified live risk) |
| Relic abundance `Ω_c ≈ 0.12` | RelicLagrangian §4 | **INHERITED** (η_B tier); the relic gives the value a native field-theoretic *home*, but the amount is still inherited |
| Bullet Cluster offset (relic sails through, collisionless) | DarkSector §4.2 | **INHERITED mechanism** — the ΛCDM-class collisionless account is inherited, not re-derived; the relic is the native reason a collisionless component is present |

### Prediction (falsifiable bet)
| Claim | Paper | Falsifier | Status |
|---|---|---|---|
| Dark matter is **WARM (~0.2–0.7 keV)**, not a cold WIMP | DarkSector §6 / RelicLagrangian §5.2 | F1: a cold heavy WIMP detection, or perfectly-cold DM, refutes it | current — directional prediction **and the sector's quantified live risk** (mechanism prefers cold) |
| Galaxies contain **NO dark-matter halo at all** | DarkSector §6 | F2: DM substance found *inside* galaxies (halo, CDM cusps, scattered mass) refutes the horizon-only account | current — clean ED-vs-superfluid-DM discriminator |
| DF2/DF4 show a **sharper external-field knee** than MOND's smooth roll-off | DarkSector §3.3 | environmental independence (ΛCDM) or smooth MOND-EFE roll-off | current — ED-distinctive; suppression function not derived (Open) |
| No gravitational **slip** beyond `O(Φ)`; activity-dependent weak-lensing enhancement in disturbed systems | DarkSector §4.3 | a measured slip, or no activity dependence | current — ED-distinctive lensing (Paper_038_6 **provisional**) |

*(The a₀(z) evolution is the flagship falsifiable bet too — F3 — but it is tiered **Derived** above, with its confirmation/tension status inline, rather than duplicated here.)*

### Open
| Item | Paper | Status |
|---|---|---|
| **CMB spectrum computed from ED** | DarkSector §4.5 / RelicLagrangian §5.3 | **NOT DONE — the largest owed piece.** Well-specified AeST-style Boltzmann run (Skordis–Złośnik the sister-theory existence proof), now gated only on the mass/abundance, not on an unknown self-term. Falsifier F6: a computed spectrum missing the Planck peaks for every warm-window mass |
| Relic **mass / free-streaming value** | RelicLagrangian §5.2 | **OPEN — the live risk.** Mechanism gives cold GeV–Planck; the needed window is warm ~keV (free-streaming ~0.1–1 Mpc). If forced cold, the relic clumps in galaxies and the sector fails |
| Galactic **small-scale puzzles** (missing-satellite, satellite-plane) | DarkSector §3.4 | **OPEN / unaddressed** — ED has engaged neither; galactic (horizon jurisdiction) but no mechanism worked out |
| DF2/DF4 **suppression function** | DarkSector §3.3 | **OPEN** — not derived, only order-of-magnitude estimated |
| Non-perturbative / **vortex** edge of `L_self` | RelicLagrangian §3.3 | **OPEN (minor)** — the gradient expansion covers only the perturbative kinetic sector; a defect contribution is the sole residue of the one-substance route |

### Superseded / Resolved
| Item | Note |
|---|---|
| `L_self` "open superfluid self-term" (first-draft flag) **and** the khronon-mode one-substance probe | **RESOLVED / RETRACTED 2026-07-19** → `L_self` canonical (two-component). Supersedes the first-draft OPEN flag *and* the retracted khronon-mode probe (which measured the wrong variable and missed the density response). The current papers reflect the resolved end-state throughout |

### Staleness, currency & cross-folder propagation
1. **a₀(z) first data — propagated across the gravity + predictions folders 2026-07-29.** MUSE-DARK III (A&A 2026): the acceleration scale **evolves** across `0.33<z<1.44` at **~30σ**, which **excludes constant a₀** and kills constant-scale MOND — ED called the *direction* right where MOND called it constant; the **exact rate** is in mild tension (direct fit α≈1.18 vs ED's forced α=1). Close to AP's north-star, but the exact-rate tension means **do not over-bank it**. **DONE:** updated `gravity/Predictions_and_Falsifiers` (new Tier-2 live test), `gravity/Paper_029` (§8.8), `gravity/Paper_037` (preamble), `gravity/Paper_038 CO-3` (data-confrontation), `predictions/22_Ways #1`, `predictions/Paper_101` (promoted to Tier-1 row 2). Canonical source = `predictions/ED_Master_Predictions_List` 1.15. **Still owed (not in this pass):** the flagship **Report** (`REPORT_CHANGES C2` / a REPORT_ADDENDA entry — don't edit the released Report in place); and the synthesis papers KM-I/KM-II/One-Field/PhilPapers.
2. **The relic gives Cosmology's inherited `Ω_c` a native home (not a contradiction).** `cosmology/Cos-03/04` inherit `Ω_c` as a ΛCDM insert; the relic now supplies the field-theoretic home + a derived `a⁻³`, with the *amount* still inherited. Consistent — the cosmology ledger's "Ω_c inherited (#5b debt)" row could cross-reference this relic construction; minor, record-only.
3. **No internal staleness found.** Both papers are internally current and consistent with each other (L_self resolved end-to-end; the retracted probe correctly superseded; every "does NOT claim" honored). The folder is the cleanest of the four swept so far.

### Honest arc-state
The dark sector is **form-complete, value-inherited, with one named live risk** — and it is honest about all three. Its structure is **"two culprits, one mechanism"**: galaxies are pure horizon-MOND (the off-diagonal interference cross-term, `a₀=cH₀/2π`, **no particle** — a *standing, separate* result and the strongest piece), while clusters and the CMB are a **committed neutral relic** whose defining `ρ∝a⁻³` is genuinely **derived** from P11 commitment-irreversibility (the sector's one new derived headline, and the volume memory a modified-gravity dial provably lacks). The one-substance-vs-two question that the superfluid-DM (Berezhiani–Khoury) rivalry turns on was **computed, not assumed**: coarse-graining the real V5 kernel yields a **canonical** relic mode (`p≈1.99`), so ED lands **two-component** — mechanism-unified (both roles are the same bilinear cross-term) but substance-separate. The distinctive edge is real and partly tested: the **a₀(z) evolution** flagship has first data **confirming the evolution at ~30σ** (burying constant-a₀ MOND) with the **exact rate in mild tension**; plus **no galactic halo** and **warm-not-cold** DM as clean discriminators. Two debts stand openly flagged: **no CMB spectrum is computed from ED** (the largest owed piece, now a well-specified Boltzmann run) and the **relic mass is inherited** — worse, the *mechanism prefers cold GeV–Planck* while consistency demands warm ~keV, a 6–26 OOM gap that is the sector's quantified failure path. **Defensible headline:** *galaxies solved without a particle (standing MOND-as-horizon-interference); clusters/CMB carried by a native committed relic with a derived `a⁻³` but an inherited, mechanism-disfavored mass; two-component by calculation not fiat; a confirmed-direction / tense-rate flagship (a₀(z)); and two openly-named debts (the CMB spectrum, the cold-mass risk) — an honest open frontier with a live failure path, not a closed account.*
