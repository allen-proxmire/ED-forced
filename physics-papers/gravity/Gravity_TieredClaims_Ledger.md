# Gravity Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the gravity folder (the corpus flagship) and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing with a row is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** Read every paper; tier each claim *from the paper's own audit table / "does NOT claim" / verdict* — never inflated. Seeded from the folder README + `event-density/docs/ED_Research_Targets.md` (#1, #5, #5b), corrected against the papers where they disagree.

**One of a per-folder set.** Companions: `entanglement/…`, `black-hole/…`, `cosmology/…`, `dark-sector/…`. This folder *synthesizes and stands* (it holds the standing KM-I MOND result — do not reinvent it).

**Tier key.** `Derived` (from primitives/structure, conditioning postulate noted) · `Grounded` (structural/conditional/account-tier) · `Measured` (simulation/probe) · `Selected/Inherited` (a value: G, ℓ_P, a₀, Λ-magnitude) · `Postulated` · `Asserted` (A→position) · `Prediction` · `Synthesis` · `Open`. `D-cond` = derived conditional on a named postulate.

*~30 papers. Read 2026-07-29 (extraction agent, then spot-checked). Honest-arc-state paragraph reconciled with Staleness #1 on 2026-08-30: it had continued to describe the a₀(z) propagation as the folder's urgent open task after Staleness #1 recorded that propagation as DONE on 2026-07-29 — the ledger contradicted itself on its own headline debt. No claim tier changed.*
*Spot-checked directly against the papers (7, scaled to the 30-paper flagship; **no catch** — the extraction was reliable throughout): (1) **GR-IV** α₂=0 exact + the c_T=c/c_s=c causal-cone framing + literature-verification — confirmed verbatim (§3, boxed); (2) **029** a₀=cH₀/(2π) form-derived, H₀ inherited, and the STATIC "tracks whichever H₀" reading (no a₀(z)) — confirmed (§8.5); (3) **031 §8.8** carries the MUSE-DARK III (A&A 2026) ~30σ a₀(z) confirmation — confirmed verbatim; (4) **038.5 §3.5** "updated 2026-07-16," w=−1 resolved, Λ=frozen floor, force-vs-stipulate residual — confirmed (this makes the MEMORY pointer stale, not §3.5); (5) **MetricFromGraph** metric KINEMATIC/static-linear, nonlinear OPEN, exactly-3 not a forcing — confirmed (preamble #2, §5); (6) **027** G=c³ℓ_P²/ħ downstream identification, ℓ_P value-layer — confirmed; (7) **QuadraticStrain** discharges P14 (geometric mean = forced interference modulus) + the regime assumption, residual = constructive sign — confirmed.*

---

### Derived (from primitives/structure; conditioning postulate noted)
| Claim | Paper | What's derived | Inherited / conditioning | Status |
|---|---|---|---|---|
| Temporal lapse `N²∼b` (the core new result) → weak-field Einstein metric | GR-I | front-null + commitment-rate law ⟹ `N²∼b`; Schwarzschild branch (not Nordström) | **D-cond on P-Commitment-Linear** (α=1) — later *forced* in GR-III §4 | D-cond |
| Emergent spatial metric `g_ij ∼ b⁻¹`; factor-of-two light bending | GR-I | bandwidth realization of the 033 acoustic metric; `n_opt∼b⁻¹` = square of spatial index (sim 2.09 vs 2.00) | conditional on the 13 primitives; sim uses imposed Newtonian-limit b-profile | D + simulation |
| α=1 (P-Commitment-Linear) **forced**; Nordström excluded | GR-III §4 | P04 reserve monotone-draining (P11) ⟹ β=0 ⟹ α=1 | D-cond on a named band-accounting premise (metric band = rate-numerator band) | D-cond |
| Khronon scalar speed `c_s = c` | GR-III §6 | reserve sector dissipative (P11), not kinetic ⟹ no second cone | leading order; sub-leading reserve renormalization benign | D (leading order) |
| Field-equation form `G^μν+Λg^μν=κT^μν` | GR-II §4 | Lovelock's theorem, given metric + conserved source + 2nd-order | **forced iff purely metric — the open condition, which §5 fails** (ED is khronometric, not pure GR) | D-conditional |
| `∇_μT^μν=0 ⟺ geodesic motion` | GR-II §3 | forced by P05 transport typing + P04 extensivity; exact for dust | pressure/anisotropic-stress need full rule | D |
| ED gravity is **khronometric** (Einstein tensor sector + 1 khronon); gauge = foliation-preserving diffeos | GR-II §5 | arrow (P11/P13) in the law ⟹ preferred foliation ⟹ mode count 2+1 | D-structural (not a completed linearized propagator) | D-structural |
| `c_T = c` structurally (GW170817 as identity); universal (not differential) Lorentz violation | GR-II §6–7 | one substrate, one transport (P05), one cone → shared by all species | F-independent | D-structural |
| **α₂ = 0 exactly** | GR-IV §3 | khronometric PPN numerator vanishes on the scalar-luminal surface once `c_T=c, c_s=c` — **the same causal cone as GW170817's `c_T=c`; one fact, two faces** | literature-verified (Blas–Lim, Ramos–Barausse, Foster–Jacobson) + numerically checked | **D + literature-verified** |
| `α₁ = −4λ_local`, `λ_local ∼ ρ_event/ρ_Planck`; commitment **forced** sparse (⟹ λ_local≪1, ≥70 orders safe) | GR-IV §3–5 | metric stiffness always-on (P02); khronon stiffness only where commitments fire (P11); dense commitment = Zeno ⟹ no QM, and ED has a QM sector | prefactor O(1) tied to κ/D=8πG | D-structural |
| Holographic bound `N(R) ≤ 4πR²/ℓ_ED²` (area law as edge-count) | 025 | channel-count on a closed 2-surface | **P-Codim-1 + P-Sat**; ℓ_ED value inherited | D (given the two postulates) |
| Newton `a_N = GM/R²` from the cumulative-strain reading | 026 / 027 | holographic source-resolution; `N(R)` factors cancel ⟹ `Φ=−GM/R` | **P-Potential-Reading** (Model A); V1 1/R envelope inherited (DCGT) | D (given P-Potential-Reading) |
| Crossover `R_H = c/H₀`; the `1/(2π)` azimuthal-Fourier factor in a₀ | 028 / 029 | kernel speed = Hubble recession; dipole projection on residual SO(2), period-2π orthonormality | form-forced; statistical-not-geometric boundary is a **P** ontological commitment | D (form-forced) |
| Reach law `p = 1/(d−1)` ⟹ `g∼1/b` in **exactly 3D** | MetricFromGraph P2 | ball-cut exponent = d−1 (holographic surface count); 3D uniquely reproduces GR-I | **derived conditional on the surface-count**; metric is **KINEMATIC/static-linear**, nonlinear OPEN; exactly-3 is internal coherence, **not a proof ED forces 3D** | D-conditional |
| Free chains follow acoustic-metric geodesics | 032.5 (GR-3A) | eikonal/stationary-phase ⟹ `S=−mc∫dτ` ⟹ geodesic eq | **FORCED-conditional on P-FreeChain + guardrails (035)**; eikonal→action step OPEN; verdict M3 | D-cond (M3) |
| Deep-MOND asymptotic `a=√(a_N a₀)`; flat-background AQUAL field eq | 034 / 036 | `μ(x)→x` + field eq + spherical geometry; AQUAL Lagrangian variational | **FORM-FORCED** given P-MOND-Interpolation / P-MOND-Field-Form; μ form inherited empirically | D (form-forced) |
| a₀ continuum-limit invariant (does not RG-run) | 037 | c invariant × H₀ invariant | **P-H0-Cosmological-Invariant** postulate | D (given postulate) |

### Grounded (structural / conditional / account-tier)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| **The khronon's deep field IS the MOND sector** (unifies the two gravity programs) | KM-I | promoting the acceleration term to W(A²) ⟹ AQUAL in the metric potential; deep-IR embeds 030 | **single hinge = "forced-given-030"** (matches the derived Combination Rule, does not re-derive); interpolation a Cassini-constrained family | Grounded (single hinge) — **the standing MOND result; do not reinvent** |
| Lensing tracks the MOND potential, **no added vector**; no new ghost; AQUAL ellipticity; PPN-safe | KM-I §5–6 | metric-borne modification; unitary-gauge no time-derivatives | slip O(Φ)-suppressed | D / D-structural |
| Orthogonality theorem: `θ≡0` in statics ⟹ the regulator family is invisible to every tested result | KM-II §4 | kinematics of static congruences | the cleanest result; sequesters the cosmology sector | D |
| Clustering dial = the soft spot (one dial sets degeneracy-cure + Čerenkov + clusters/CMB) | KM-II §6 | mapping | class mechanisms are **directions, not verifications**; abundance = value-inherited IC | D-structural (mapping) |
| Scalar-tensor acoustic-metric field eq (covariantization) | 033 | opens Arc ED-10 | **three P-postulates**; "conditional-positive"; deep-MOND superluminality A→cost (see Staleness #4) | Grounded (P-construction) |
| Six ED-10 weak-field prerequisites fulfilled at form level | 032 | enumerates WF-1..6 with falsifiers | WF-3 conditional on the P14 placeholder; sufficiency for curvature = A→assertion | Grounded (specification) |
| Six acoustic-metric guardrails (C1–C6) | 035 | conditions for acoustic-metric consistency | all six are **P (postulates)** | Postulated set |
| Λ as a V1 cosmological-scale integral over `R_H`; **Λ constant, w=−1 forced, = frozen saturation-floor** | 038.5 (incl. §3.5) | form-IDENTIFIED (V1 finite 2nd moment + curvature coupling + R_H domain); live-horizon Λ ⟹ w=0/dead, so only the frozen floor accelerates | value inherited; verdict **M3** conditional on Route-A; **residual OPEN: force vs stipulate the frozen value** (§3.5, updated 2026-07-16) | Grounded (form-ID, M3) + open residual |
| One-Λ thesis: `𝒲₀ = −24π²Ω_Λ ≈ −162` | KM-II §7 | shared SCBU boundary; scaling exact; sign passes | **D-via-I** (tier transported from 038.5, not upgraded); ab-initio integral OPEN with a numeric target | Grounded (thesis) |

### Measured (simulation / probe)
| Claim | Paper | What's measured | Status |
|---|---|---|---|
| Dynamical rule `ḃ=D∇²b−κρ` built; steady state `∇²b∼ρ` (corr 0.999) | GR-III §7 | fixed point of the two forced terms | measured |
| Schwarzschild `r_s∝M` (2D+3D); emergent frozen `b→0` horizon (= metric horizon = V5 surface); area-law `S∝A` | GR-III §7 | deficit linear in source; horizon forms with nothing about a horizon in the rule; severed-channel count scales as perimeter | measured (¼ coeff inherited) |
| Hawking scaling `κ=1/(2r_s)∝1/r_h` | GR-III §8 | derived (vacuum solution + `g₀₀g_rr=−1`); corrects an earlier "flat" measurement error | derived; direct sim resolution-limited |
| Phase-coherence constructive sign supplied (P12-Coh rewards alignment) | QuadraticStrain §9 update | build-verified 2D/3D; finite-reach not crystalline | measured (conditional on P12-Coh operationalization) |

### Selected / inherited (a value taken from measurement)
| Value | Paper | Status |
|---|---|---|
| `G = c³ℓ_P²/ℏ` | 027 / 027.5 | **form-derived, value-INHERITED (M3)**; `ℓ_ED=ℓ_P` is the empirical-matching choice, not a substrate derivation |
| `a₀ = cH₀/(2π)` | 029 | form-derived, ~10% parameter-free match; **H₀ inherited** (and 029's reading is *static* — see Staleness #1) |
| Λ magnitude `ρ_Λ ≈ 1.1×10⁻⁵² m⁻²` | 038.5 | value-INHERITED; smallness = `(H₀/M_P)²` via Friedmann, gated on Route-A |
| Thermodynamic coefficients (¼ in S=A/4; T=κ/2π) | GR-III | value-inherited (the ¼; and see `black-hole/…` for the geometric-2π derived route) |

### Postulated (paper-specific, load-bearing)
| Postulate | Paper | Note |
|---|---|---|
| P-Commitment-Linear (α=1) | GR-I | later **forced** in GR-III §4 (chronology: discharged downstream) |
| P14 Bilocal Strain Coupling (geometric-mean) | 030 | **postulated, non-unique** (§8.4/8.9); later **discharged** by QuadraticStrain as the forced interference modulus |
| P-Quadratic-Strain (Model C) | QuadraticStrain | one postulate replacing P14 + 030's regime assumption |
| P-Codim-1, P-Sat (025); P-Potential-Reading (026); P-AcousticMetric + P-Scalar-Tensor-Form + P-MOND-Interp-Covariantization (033); P-MOND-Interpolation (034); P-MOND-Field-Form (036); P-H0-Cosmological-Invariant (037); P-FreeChain (032.5) | various | the folder's paper-specific postulate stack |

### Asserted (A→position, the paper's own label)
| Item | Paper |
|---|---|
| "6 prerequisites ⟹ Arc ED-10 viable" (necessity, not sufficiency) | 032 §5 |
| Superluminality structural cost "FORCED" (composite verdict) | 034 §3.3 |
| Verdict M3 rows (per Paper_095) | 027.5, 032.5, 033, 038.5, 038.6 |

### Prediction (falsifier given)
| Prediction | Paper | Falsifier | Status |
|---|---|---|---|
| BTFR `v⁴=GM_b a₀`, slope **exactly 4**, zero intrinsic scatter | 031 | slope≠4 or irreducible scatter (data: 3.95±0.08, ~0.1 dex) | current — **slope-4 + tightness are MOND-SHARED**; only the a₀ normalization is ED-distinctive |
| **`a₀(z) = cH(z)/(2π)`** evolves factor-for-factor with H | 031 §8.8 (data-confronted), 038 CO-3 | departs from cH(z)/2π | current — **only 031 §8.8 reflects the 2026 data** (Staleness #1); ~30σ evolution confirmed, exact rate α=1 the open number, data mildly faster |
| `α₁, α₂` preferred-frame | GR-II/III/IV | any nonzero `α₂` kills it (α₂=0 exact); `α₁≳10⁻⁵` kills it (α₁≲4×10⁻⁹³ safe) | current — the keystone kill-switch, passed favorably |
| Scalar (breathing) GW polarization at c | GR-II/III | definitive absence excluding the khronon mode | current |
| Wide binaries near a₀ depart from Newton | KM-I, One-Field | a clean Newtonian result at relevant precision | current |
| Lensing identity (no slip beyond O(Φ)); activity-dependent weak lensing `∝|∇μ|²` | KM-I §5 / 038.6 | measured slip; activity-independent lensing | current — 038.6 **PROVISIONAL** (α_act, 𝒜(x), the discriminator observable all OPEN) |
| CMB dust dial / cluster sector | KM-II | no `𝒲(A²,Θ)` member satisfies all five filters | current — clusters/CMB OWED |
| `𝒲₀ = −24π²Ω_Λ` (ab-initio integral must hit it) | KM-II §7 | wrong sign or magnitude off by >O(1) | current — an open number-to-miss |
| Offset–velocity "knee" law `Δr(v_rel)`: flat–knee–line–ceiling | 117 / OffsetVelocity | ΛCDM velocity-independent; MOND-EFE smooth roll-off; ED sharp knee at `v_crit~150 km/s` | current — **only the SHAPE is ingredient-robust**; the knee location rests on a flagged `ν≈0.70` (3D O(3)) assumption |

### Synthesis
| Item | Paper | Note |
|---|---|---|
| "One field, one scale, five roles" (arrow, Einstein sector, MOND, clustering dial, Λ-scale) | One-Field Letter | capstone; **carries a 2026-07-19 correction banner** downgrading "dark matter is not a particle" to a *candidate* and flagging the khronon-alone abundance gap (needs a real relic — the dark-sector two-component picture) |
| Whole-program synthesis, tiered, GR-IV folded in | PhilPapers | self-contained; α₁/α₂ front closed favorably; open debts named |
| **MOND = interference cross-term**: Newton=diagonal, MOND=off-diagonal of `|ΣP|²` | QuadraticStrain | discharges P14 (geometric mean = forced interference modulus) + 030's regime assumption (horizon is a dipole, not a monopole); STRUCTURAL, conditional on P-Quadratic-Strain; residual = constructive sign (supplied 2026-07-08 at measured tier) |

### Open (declared)
| Item | Paper | Status |
|---|---|---|
| Bandwidth ↔ strain/flow substrate-route identification | GR-I §7 / KM-I | OPEN |
| Primitives-level origin of the deep-IR (geometric-mean) branch | KM-I / PhilPapers | OPEN — "guarded," deliberately unattempted |
| Ab-initio V1 boundary integral for Λ (target `𝒲₀=−24π²Ω_Λ`); Route-A closure | 038.5 / KM-II | OPEN — highest-leverage open derivation |
| Whether Λ frozen-floor value is **forced or stipulated** | 038.5 §3.5 | OPEN (bootstrap knot; driver is matter-dilution, Cos_05) |
| Nonlinear / strong-field field equations; background-free construction | MetricFromGraph / PhilPapers | OPEN — the nonlinear regime is the distinctive/falsifiable frontier |
| Clusters + CMB not discharged; khronon-standalone **abundance gap** (now carried by a separate two-component warm relic) | KM-I / KM-II / One-Field banner / 117 banner | OPEN — see `../dark-sector/` |

### Staleness, currency & cross-folder propagation
1. **a₀(z) + 2026 MUSE-DARK III data — propagation DONE 2026-07-29.** The canonical treatment is `predictions/ED_Master_Predictions_List` **1.15** (2026-07-14, A10: direct fit α≈1.18±0.04, MOND dead at 29σ, ED's α=1 at +4.4σ→~1–2σ w/ systematics, author-corroborated "faster than H(z)"; verdict: call confirmed, exact rate mildly disfavored, **not** a refutation); `Paper_031 §8.8` carries the compact version. **These predated it, now UPDATED:** **Paper_029** (added §8.8 — the evolution + data, distinct from its static §8.5); **Paper_037** (added preamble item 6 — continuum-invariance ≠ cosmological constancy; a₀ still evolves with cosmic time); **Paper_038 §3.3 CO-3** (added the data-confrontation paragraph); **Predictions_and_Falsifiers** (added a Tier-2 live-test bullet + Milgrom-row note + footer); **predictions/22_Ways #1** (sharpened to the evolving scale + status); **predictions/Paper_101** (promoted a₀(z) from a §0.3 postdiction parenthetical to **Tier-1 weapon row 2**). *Not touched (synthesis papers, lower priority):* KM-I/KM-II/One-Field/PhilPapers still use a₀=cH₀/2π without the evolution confrontation — a candidate second pass if desired. *Do not over-bank: direction confirmed, exact rate under tension.*
2. **"Wolfram Ruliad" in 4 peer-facing position statements** (027.5 §6, 032.5 §6, 038.5 §6, 038.6 §6). Violates the no-Wolfram-in-public rule. **AP's standing call: leave it.** Record-only. (PhilPapers uses the softer "Wolfram programs" once.)
3. **038.5 §3.5 — the MEMORY POINTER is stale, not the paper.** §3.5 was **updated 2026-07-16** with the w=−1 resolution + the force-vs-stipulate residual + F3. The memory note `project_lambda_constant_vs_a0_horizon` ("stale flag = 038_5 §3.5") is what needs correcting. **Fixed in memory 2026-07-29.**
4. **Deep-MOND "superluminality cost" (033 §3.4, 034 §3) re-tiered to "feature" by the KM line** (KM-I §8, GR-II §9: the superluminal scalar is the khronon class's universal-horizon character, not a pathology). Chronology-aware: 033/034 predate the KM line and were true when written; a reader hitting them first sees a "cost" the corpus has re-tiered. Record-only (or a one-line forward-pointer banner if desired).
5. **Paper_117 correctly repositioned** (2026-07-19 banner: relic account primary, the topological-defect offset-velocity law demoted to a speculative bonus). The banner governs; OffsetVelocity/F3DataTable cite it as a bonus. **Discharged** (the seed's staleness concern is already handled) — though the body §1–6 still narrates the defect mechanism as if primary, under the governing banner.
6. **Paper_032.5 (GR-3A) superseded-in-part** by GR-III's limit-forced timelike-geodesic reduction; it still frames geodesics as FORCED-conditional on the older guardrails. Not a contradiction (chronology); the GR-III/GR-I treatment is the standing one.
7. **Curvature-emergence nuance holds — no over-claim found.** MetricFromGraph explicitly tiers the emergent metric as **kinematic/static-linear**, nonlinear Einstein OPEN, exactly-3 as derived-conditional (not a forcing). GR-I/II/III consistently say ED gravity is khronometric, not pure GR.
8. **P14 double-status** (record, not error): 030/031/032 carry P14 live; QuadraticStrain (2026-07-07/08) discharges it. Each pre-discharge paper flags P14 honestly; QuadraticStrain is the current resolution.

### Honest arc-state
The gravity line is the corpus flagship and it hangs together at the tier it claims. **The GR keystone (#1) is closed** in the honest sense: GR-I derives the weak-field Einstein metric + factor-of-two (conditional on the single postulate P-Commitment-Linear, which GR-III then *forces* from the P04 band law, modulo a named premise); GR-II fixes the class as **khronometric** (Lovelock + mode count, structural) with `c_T=c` and universal Lorentz-violation as F-independent shields; GR-III builds and runs the dynamical rule (Newtonian fixed point, `r_s∝M`, emergent frozen horizon, area law, Hawking scaling, `c_s=c` derived); and GR-IV closes the preferred-frame kill-switch **favorably** — **α₂=0 exactly** (both cones luminal, literature-verified) and `α₁=−4λ_local≲4×10⁻⁹³` (≥70 orders safe) because commitment is Zeno-forced sparse — while keeping it a live test. The **α₂=0 and `c_GW=c` are one causal-cone fact** (GR-IV §3), which is the load-bearing inseparability the untunability reading leans on. The **MOND/dark-matter line stands**: `G=c³ℓ_P²/ℏ` (form-derived, value-inherited), `a₀=cH₀/2π` (form-derived), the Combination Rule and BTFR slope-4, with **KM-I** unifying them as the khronon's deep field (single hinge "forced-given-030," lensing/ghost/PPN checks passing — *the standing result, not to be reinvented*), and **QuadraticStrain** sharpening 030 by recasting MOND as the off-diagonal interference cross-term (discharging P14 to one strain-reading postulate; residual = the constructive sign, now at measured tier). The honest BTFR distinction holds — slope-4 + tightness are MOND-shared; only the a₀ *normalization* is ED-distinctive. **KM-II** reduces the clusters/CMB debt to one sequestered regulator dial under five filters (orthogonality theorem clean) and pins `𝒲₀=−24π²Ω_Λ` at inherited tier with the ab-initio integral an open number-to-miss. The emergent metric is correctly held as **kinematic/static-linear** (the nonlinear regime is the distinctive/falsifiable frontier, OPEN), and exactly-3 as derived-conditional-on-the-holographic-count, not a forcing. **The propagation debt that dominated this folder is now closed:** the flagship a₀(z) evolution bet and its ~30σ 2026 confirmation, which had lived in only one paper (031 §8.8), were propagated on 2026-07-29 to 029 (new §8.8), 037 (preamble item 6), 038 §3.3 CO-3, Predictions_and_Falsifiers, 22_Ways #1, and Paper_101 (promoted to Tier-1 weapon row 2) — see Staleness #1 for the full list. What remains is the *lower-priority* second pass: the synthesis papers (KM-I, KM-II, One-Field, PhilPapers) still cite a₀ = cH₀/2π without the evolution confrontation. **Defensible headline:** *the GR keystone is closed (khronometric, α₂=0 exact, favorable preferred-frame kill-switch); Newton's G and the MOND scale are form-derived / value-inherited with KM-I the standing unification and QuadraticStrain the sharper foundation; Λ is form-identified with a force-vs-stipulate residual; the nonlinear metric and clusters/CMB are the named open frontier; and the confirmed-but-tense a₀(z) evolution has been propagated out of 031 §8.8 across the primary line (2026-07-29), leaving only the synthesis papers as a lower-priority second pass.*
