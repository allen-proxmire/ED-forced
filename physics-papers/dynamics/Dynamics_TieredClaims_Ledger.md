# Dynamics Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the dynamics folder (the gravitational-dynamics / GW-generation sector) and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** Read every paper; tier each claim *from the paper's own audit/status/verdict* — never inflated. Seeded from the folder README + each paper's Paper_095 verdict, corrected against the papers.

**One of a per-folder set.** This is the corpus's **GW-generation phenomenology**, downstream of the gravity line (`gravity/`). Companions: all other `physics-papers/*` ledgers.

**Tier key.** `Derived` (pure-D from primitives) · `Grounded` (M2/M3 — form-IDENTIFIED via D-via-I composition, DCGT A-regime) · `Measured` (simulation/probe) · `Selected/Inherited` (values / coefficients / QNM frequencies from the standard forms) · `Postulated` · `Asserted` (A→position) · `Prediction` (falsifiable, GW-facing) · `Synthesis` · `Open`.

*8 papers. Read 2026-07-29 (extraction agent, then spot-checked); re-read 2026-09-04 (external audit).*

> **`c_T = c` — tier split clarified 2026-09-04.** `Paper_ED_GW_00` marks the GW propagation speed **Inherited** (*“GW170817 confirms”*), while the **gravity** ledger marks `c_T = c` **D-structural** (GR-II §§6–7: one substrate, one transport, one cone). Both are right about different things, and the corpus's own `Paper_095` grammar resolves it: the **identity** — that tensor waves and light share one cone — is *structural*, derived upstream in GR-II, and is what makes GW170817 a survival rather than a fine-tuning; the **value** of that shared speed is *inherited* via P-RB-1. GW-00's claim (that it does not derive the *speed*) stands unchanged. **What is corrected is the reading:** the row does not disclaim the identity. This matters because `Paper_GR-IV`'s untunability argument leans on the identity being structural, and a reader comparing the two ledgers would otherwise find ED claiming it in one folder and disclaiming it in another. See `gravity/Gravity_TieredClaims_Ledger.md` Staleness #29.
***Two tiers are EMPTY by the papers' own accounting:*** *every paper declares **"zero pure-D rows"** (so `Derived` is empty — everything load-bearing is D-via-I / Inherited / A→position / Open), and there is **no simulation/probe** in this folder (so `Measured` is empty — all empirical contact is postdiction against LIGO/Virgo/Hulse-Taylor/NANOGrav, not ED-side measurement).*
*Spot-checked directly against the papers (3, scaled to 8; **no catch**): (1) **GW-00** "Zero pure-D rows; seven D-via-I composition rows," c_T=c explicitly INHERITED ("GW170817 confirms"), NOT oversold — confirmed; (2) **Dyn-03** M2, coefficients `1/(6πε₀c³)`/`1/(5c⁵)` INHERITED, OPEN-RL-Q1/Q2 load-bearing, and it *itself requests* the GW-00 row-12 reframe — confirmed; (3) **GW-02** Ω∝f^{2/3} "inherits standard Peters-formula," NANOGrav "model-degenerate," M2 via component composition — confirmed as consilience, not a weapon.*

---

### Grounded — M3 (form-IDENTIFIED, value-INHERITED, DCGT A-regime; no load-bearing OPEN)
| Claim | Paper | What's derived (form) | Inherited / open | Status |
|---|---|---|---|---|
| Saddle-Hessian-signature dynamics is the foundational generator; 3 regime classes (S1 all-compression → collapse; S3 all-expansion → inflation/DE; S2 mixed → horizon/radiation) | Dyn-01 | regime partition form via SC-4.9 Hessian + Morse theory + V1/V5 composition | `ℓ_saddle` substrate-parameter-INHERITED (Route A4); IC-inherited; SC-4.9 exhaustiveness OPEN upstream | **M3** |
| Gravitational collapse = monotonic Hessian-signature evolution toward all-compression; horizon = closed signature-class boundary surface | Dyn-04 | collapse mechanism form via Dyn-01 S1 + Dyn-02 + GW-01 | monotonicity itself inherited from NR phenomenology (substrate-graph proof NOT constructed, §3.2); `r_horizon`, Choptuik γ, timescales inherited | **M3** |
| GW = propagating saddle-Hessian-signature reconfiguration carried by V1 retarded propagation; energy = local ED-gradient load (no pseudotensor) | GW-00 | substrate mechanism + transverse role-swap form; the 2 tensor modes = the 2 independent Hessian-flip directions (§3.7) | speed=c, strain, frequency, 2-pol count all **INHERITED**; full waveform (row 13) OPEN (non-load-bearing) | **M3** |
| BH ringdown = decay of a time-varying near-horizon mixed-signature saddle to equilibrium; mode quantization `ω_n=ω_R+iω_I` from Hessian eigenstructure | GW-01 | ringdown mechanism + discrete-mode-origin form via Dyn-01 + GW-00 + Dyn-02 | **QNM frequencies `ω~c³/GM` INHERITED** (Schwarzschild/Kerr spectrum; Regge-Wheeler/Teukolsky machinery); IC from NR merger | **M3** |
| Quadrupole source-amplitude *form* `P_GW ∝ ⟨Q⃛²⟩` (GW-00 row 12) | GW-00 §3.9 | substrate Noether flux → DCGT → linearized-Einstein form | coefficient `1/(5c⁵)` INHERITED; source-class + flux-form inherited by standard-GR analog | **D-via-I (form only)** — the row-12 "closed" is FORM-only; the coefficient stays OPEN (see Staleness #2) |

### Grounded — M2 (form-IDENTIFIED conditional; capped by one shared Q1/Q2 gap)
| Claim | Paper | What's derived (form) | Inherited / open | Status |
|---|---|---|---|---|
| Horizon-motion law: RDE (w=1/3), MDE (w=0), LDE (w=−1) via substrate Noether stress-energy + DCGT + Friedmann | Dyn-02 | LDE/saturation case substrate-graph-IDENTIFIED directly; RDE/MDE form proposed | RDE/MDE form inherited via standard-QFT analog; Friedmann/H₀ inherited | **M2 (Path C)** — Q1+Q2 load-bearing OPEN; feeds cosmology's Cos-05 |
| Radiation law: EM Larmor + GW quadrupole via Noether flux + DCGT | Dyn-03 | Larmor + quadrupole *form* via the NoetherFlux chain | **numerical coefficients INHERITED**; source-class + flux-form inherited; retarded-Green machinery inherited | **M2** — OPEN-RL-Q1 (source-class criterion) + OPEN-RL-Q2 (flux form) load-bearing |
| Compact-binary inspiral = two-saddle coupled evolution + quadrupole radiation reaction; `ṙ`, Peters timescale | Dyn-05 | two-saddle form via Dyn-01 S2 + Dyn-03 + Dyn-04 + GW-01 | Peters 1964, PN coefficients, `r_ISCO` inherited; plunge = NR domain | **M2 generic** (inherits Dyn-03); **M3 saturation-case** (asymptotic circular orbit) |
| Stochastic background `Ω_GW(f)` = cosmologically-integrated NoetherFlux over saddle transitions | GW-02 | integration form via GW-00+GW-01+Dyn-04+Dyn-05+Cos-01+Cos-05 | population synthesis, H(z), H₀ inherited | **M2 net** (component composition; inspiral dominates observable bands); M3 subdomain carve-outs |

### Selected / inherited (values, coefficients, QNM frequencies from the standard forms)
| Item | Paper | Status |
|---|---|---|
| Larmor coefficient `1/(6πε₀c³)`; quadrupole coefficient `1/(5c⁵)` | Dyn-03 | **INHERITED** at standard-physics-analog level; substrate-graph derivation OPEN |
| QNM frequency spectrum `ω_lmn(M,J)`, `ω~c³/GM` + Regge-Wheeler/Teukolsky machinery | GW-01 | **INHERITED** (mechanism identified, numbers not recomputed) |
| **GW speed `c_T = c`** | GW-00 / GW-01 | **INHERITED** — substrate-c = V1 rate; GW170817 confirms. **Correctly NOT oversold as ED-distinctive** (a shared survival with GR) |
| Two transverse polarizations (h₊, h×); no scalar/vector/longitudinal | GW-00 / Dyn-03 / GW-01 | **Grounded in GW-00 (D-via-I from saddle geometry in D=3+1); Inherited downstream** |
| `h ~ 1/r` amplitude falloff; `ℓ_saddle`, `τ_V5/τ_P`, `Θ_ED`, H₀ (Route A4); `r_horizon=2GM/c²`, `r_ISCO=6GM/c²` | all | **Inherited / substrate-parameter-inherited** |

### Postulated
| Item | Paper | Status |
|---|---|---|
| P-GW-SaddleReconfiguration (GW = propagating saddle reconfiguration carried by V1) | GW-00 | **Postulated (definitional / naming convention only** per Paper_095 §2.3; no new substrate content) |
| The 13 primitives (Paper_087) | all | Postulated (inherited primitive set) |

### Asserted (A→position)
| Claim | Paper | Status |
|---|---|---|
| No graviton, no metric perturbation, no Hilbert-mode, no gauge freedom, no pseudotensor (four substrate-ontology replacement claims) | GW-00 / GW-01 / Dyn-04 | **A→position** |
| Each paper's M3/M2 verdict (five-anchor sync) | all | **A→position** (Paper_095 grammar) |

### Prediction (falsifiable, GW-facing) — **all survival-bets; none distinctive**
| Claim | Paper | Test | Status |
|---|---|---|---|
| No non-transverse (scalar/vector) GW polarization modes; no GW dispersion at cosmic scales | GW-00 / Dyn-03 / GW-01 | LIGO/Virgo polarization; GW170817 `\|c_GW−c\|/c<10⁻¹⁵` | consistent; **shared with GR, NOT distinctive** |
| EoS values confined to `{−1, 0, 1/3}` + composites (no clean phantom `w<−1`, no stiff `w=1`) | Dyn-02 | ΛCDM constraints; DESI/Euclid | consistent; **near-distinctive** (substrate-side admitted set), but sits *behind* the Q1/Q2 OPEN |
| Radiation power obeys Larmor / quadrupole scaling; orbital decay = Peters 1964; ringdown `ω~1/M`; `Ω_GW ∝ f^{2/3}` | Dyn-03 / Dyn-05 / GW-01 / GW-02 | Hulse-Taylor ~0.1%; LIGO waveforms; GW150914 ringdown; NANOGrav nHz | consistent **postdictions**; the NANOGrav `f^{2/3}` is **self-labeled model-degenerate** |

### Synthesis (cross-arc)
| Claim | Paper | Note |
|---|---|---|
| Cos-01 (inflation) + Cos-05 (dark energy) = the single all-expansion (S3) saddle regime at different epochs | Dyn-01 §3.5 | the saddle framework subsumes both cosmology papers as one regime |
| Full inspiral→plunge→collapse→ringdown waveform closed at corpus level (addresses GW-00 row 13) | Dyn-05 + Dyn-04 + GW-01 + GW-02 | composition; minimum-tier rule → M2 base, M3 subdomain carve-outs |
| BH horizon and cosmic decoupling = one substrate-parameter surface (SC-4.1 strengthened) | Dyn-04 / GW-01 | cross-arc to the SCBU BH-horizon projection |

### Open
| Item | Paper | Load-bearing? |
|---|---|---|
| **OPEN-HM-Q1** — substrate-graph chain-class criterion (rapid-V1=RDE vs slow-V1=MDE); **OPEN-HM-Q2** — substrate-graph stress-energy form per regime | Dyn-02 | **Yes** (Q1+Q2 joint closure → M3) |
| **OPEN-RL-Q1** — substrate source-class criterion (accelerated chain=EM vs time-varying quadrupole=GW); **OPEN-RL-Q2** — substrate flux-form per class | Dyn-03 | **Yes** — *the single shared gap of the folder*; closing Q1+Q2 lifts Dyn-02/03 (and by propagation Dyn-05, GW-02) M2→M3 in one move |
| Dyn-03 M2 propagates through Dyn-05 → GW-02 (net base verdict) | Dyn-05 / GW-02 | **Yes** (caps them at M2) |
| Substrate-graph derivation of the numerical coefficients `1/(6πε₀)`, `1/5`; GW-00 row-13 full waveform; BH-interior singularity resolution | Dyn-03 / GW-00 / Dyn-04 | No (frontier / non-load-bearing) |

### Staleness & refinements
1. **Wolfram/Ruliad in all 8 Position Statements** (the standard lineage line). Violates the no-Wolfram-in-public rule; a single find/replace clears all 8. **AP's standing call: leave it.** Record-only.
2. **GW-00 row-12 "CLOSED" vs Dyn-03's "form-only, coefficient OPEN" — FIXED 2026-07-29.** GW-00's row 12 said "D-via-I (CLOSED 2026-05-16)" while §3.9 said "OPEN at quantitative-derivation level," and Dyn-03 row 20 requested the reframe. **Row 12 updated** to "D-via-I — FORM closed; numerical coefficient `1/(5c⁵)` OPEN (Dyn-03 row 14)."
3. **Missing Cos-06 → GW-00 tensor-mode cross-reference — FIXED 2026-07-29.** GW-00 §3.7 identified the two polarizations with the saddle-Hessian-flip directions but did not cite cosmology's Cos-06 (whose primordial tensor modes are the *same* mechanism). **A Cos-06 cross-arc note added to GW-00 §3.7** (inflationary tensors + post-recombination GW = one substrate structure, two Hessian-flip directions at different epochs). *(The reverse direction already existed — Cos-06 §3.4 cites GW_00 — so the tie is now bidirectional.)*
4. **Over-claim checks all PASS (no correction).** c_T=c correctly Inherited/not-oversold (Staleness-N/A); `Ω∝f^{2/3}` correctly model-degenerate postdiction; no novel GW number or from-scratch GW-law over-claim; the coefficients and QNM frequencies are explicitly inherited. This folder does **not** inflate its consilience into weapons.

### Honest arc-state
The dynamics folder is a **consilience / phenomenology sector, not a weapons sector — and it is honestly self-tiered as such.** Every paper carries "zero pure-D rows"; nothing here is derived from substrate primitives without inheriting the standard result, and there is no simulation (the `Derived` and `Measured` tiers are both empty by the papers' own accounting). The genuine ED contribution is **ontological re-identification**: gravitational waves, collapse, inspiral, ringdown, and the stochastic background are all recast as saddle-Hessian-signature dynamics of `S_sub[Ψ]` carried by V1/V5 propagation under DCGT coarse-graining, reproducing Larmor, the quadrupole formula, QNM spectra, Peters decay, and `Ω_GW ∝ f^{2/3}` — with **all numerical values (coefficients, QNM frequencies, `c_T=c`, strain, H₀) inherited** from the standard forms or Route-A4 substrate-parameters. The M3 papers (Dyn-01, Dyn-04, GW-00, GW-01) reach M3 because their form-identification chains avoid the chain-class question; the M2 papers (Dyn-02, Dyn-03, Dyn-05, GW-02) are capped by a **single shared load-bearing gap** — the substrate-graph source/chain-class criterion (Q1) and the stress-energy/flux-form-per-class (Q2), currently inherited by standard-QFT analog rather than derived; **closing Q1+Q2 would lift Dyn-02/Dyn-03 (and by propagation Dyn-05, GW-02) to M3 in one move.** The headline is correctly "reproduces the standard GW/radiation laws through the substrate" — **there is no distinctive GW-facing prediction here**; the falsifiers are survival-bets ED shares with GR (LIGO/Virgo/Hulse-Taylor/NANOGrav), and the one near-distinctive item (the `{−1,0,1/3}` EoS admitted set) sits behind the Q1/Q2 OPEN. **Defensible headline:** *the GW-generation/radiation laws are reproduced through the substrate as saddle-Hessian-signature dynamics — form-identified, all values inherited, zero pure-D rows — with no distinctive prediction and a single shared Q1/Q2 gap capping four papers at M2; the only debts are cosmetic (Wolfram, a GW-00 row-12 wording clarify, and a missing Cos-06↔GW-00 tensor-mode cross-ref).*
