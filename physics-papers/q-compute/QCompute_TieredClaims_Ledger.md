# Q-Compute Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the q-compute folder (decoherence limits / quantum-hardware architecture) and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** Read every paper; tier each claim *from the paper's own audit/status/verdict* — never inflated. Seeded from the folder README + `event-density/docs/ED_Research_Targets.md`, corrected against the papers **and the live `ED_Master_Predictions_List` corrections** (which the folder itself has not fully absorbed — see Staleness).

**One of a per-folder set.** This folder holds **two of the corpus's near-term weapons** (the Class-A mass wall, the Class-C error-correction plateau); their honest status is the load-bearing content.

**Tier key.** `Derived` (from primitives, conditional on the 13 postulated primitives) · `Grounded` (conditional/structural — carries a paper-specific postulate or an A→regime assumption) · `Measured` · `Selected/Inherited` (a value from measurement) · `Postulated` · `Asserted` (A→position) · `Prediction` (falsifiable, experiment-facing) · `Synthesis` · `Open`.

*11 papers. Read 2026-07-29 (extraction agent, then spot-checked).*
*Spot-checked directly against the papers (4, scaled to 11; **no catch**): (1) **056** shape-not-number is explicit ("the structural prediction is the wall itself… the 140–250 kDa value is an extrapolation, not a substrate-level prediction; 2-point anchor") — and **056 IS stale on the number** (no mention of the ≥170 kDa Nature-2026 pressure or the confounded second-harmonic); (2) **058b** α_topological=0 boxed, plateau re-scoped to broadcast-type, Willow tension "converted into a match" — confirmed; (3) **058 original** DID predict surface-code plateau as its headline near-term test, so 058b's "058 anticipated this" **overstates** it (058b's own domain-restriction framing is the honest one); (4) **055** exhaustiveness rests on P-Three-Constituent + P-Always-Binding — Grounded conditional, NOT "proven" as the README says.*

---

### Derived (from primitives, conditional on the 13 postulated primitives)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| UR-1.1 `M_eff < M_cap`; UR-1.2 `Γ_cross > Γ_decoupling`; UR-1.3 `Γ_commit < Γ_indiv⁻¹` (the three unresolvedness statements) | 054 §5 | algebraic from Γ_commit + Γ_indiv (given the A→regime power-law); UR-1.2 from V5 (Paper_090) | rests on the A→regime power-law form; Γ_decoupling/coefficients inherited | **Derived (conditional)** |
| Existence of `Γ_commit`, `Γ_indiv⁻¹ ~ c/ℓ_ED`; `M_cap = (Γ_indiv⁻¹/Γ₀)^{1/γ}` as the UR-1.1 threshold | 054 / 056 §3.3 | existence from P11+P12+V1 finite width; M_cap form from `Γ_commit(M_cap)=Γ_indiv⁻¹` | numerical `Γ₀, γ` inherited (empirical anchoring) | **Derived (form)** |
| **α_topological = 0** (per-locus): the 058 §3.3 saturation never triggers for topological codes | 058b §3 | structural — 058's P-Corr-Budget is per-locus, 090's V5 is pairwise/finite-reach, a topological web is local (bounded degree, no long-range pairwise load), syndrome records are P11-committed (budget-free) | conditional on three inherited/QI rows | **Derived-structural (settlement, 2026-07-14)** |
| Syndrome records are budget-free (P11 commitments) | 058b §6 | from the QuantumDarwinism record-bandwidth accounting theorem | — | **Derived** |

### Grounded (conditional/structural — carries a paper-specific postulate or A→regime assumption)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| `M_cap = min(N_bw, N_V5, N_commit)` is one substrate object; the min-structure forced by simultaneity | 053 §3 | the min-structure follows once the composite is postulated | rests on **P-Mcap-Unification + P-Mcap-Finiteness** (postulates) | Grounded |
| **A/B/C three-class EXHAUSTIVENESS** — every architecture saturates one of the three constituents | 055 §3 | 3 constituents → 3 classes; "exhaustiveness is FORCED" | rests **entirely on P-Three-Constituent + P-Always-Binding** (postulates), conditional on the 13-primitive ontology + V1 + V5 | **Grounded (postulate-driven, NOT a proof)** — README's "proven" overstates it (Staleness #4) |
| The three UR-1 rate quantities have distinct *primary drivers* (basis of A/B/C distinctness) | 054 §3.5 | categorization by primary driver | **formal mathematical independence NOT proven** (own audit: A→assertion) | Grounded (weaker than independence) |
| Class-B exponential gap-suppression `Γ_fail ~ Γ₀ e^{−ξ/ξ₀}` | 057 §4 | exponential form conditional on P-Rigidity-Gap + P-Boltz-Analogy | both postulates **by analogy to standard topological-QM, NOT derived**; leading-order form **NOT unique to ED** (topological-QC predicts the same) | Grounded (prediction-facing) |
| Class-C plateau `Γ_fail → Γ_plateau > 0` at redundancy saturation | 058 §3 | plateau from the finite correlation budget | conditional on **P-Corr-Budget + P-Redundancy-Mapping** (linear = A→regime; domain settled by 058b) | Grounded (prediction-facing) |
| M_crit unification: the matter-wave Q-C boundary and the qubit walls are one substrate threshold | 060 §3 | same-threshold identification | rests on **P-Mcrit-Unified + P-Cross-Platform-Universality**; values inherited; the phase-transition comparison is A→analogy | Grounded |
| Meta-architectures (EC / DD / reservoir / hybrids) = compositions that shift which constituent binds — **no fourth class** | 059 §3–4 | composition structure | rests on **P-Composition-No-New-Class + P-Substrate-Shift-Locality**; the four mappings individually postulated | Grounded |

### Prediction (falsifiable, experiment-facing) — the arc's weapons, honest status
| Claim | Paper | What's predicted | Distinctive? | Status |
|---|---|---|---|---|
| **Class-A wall EXISTS as sharp + architecture-independent** (the shape is the claim, not the number) | 056 §7, §9 | a sharp architecture-independent multiplicity-cap boundary at finite mass | **Yes** — diverges from decoherence-only (no sharp architecture-independent wall) and from CSL (tuned) | **Prediction (live, shape-level)** — the folder's genuinely distinctive weapon |
| Class-B error suppression exponential in ξ across architectures | 057 §6 | exponential form + cross-platform ξ₀ consistency | **Weak** — the leading exponential form is ALSO predicted by standard topological-QC; the wedge is only at higher-order cross-platform consistency | Prediction (weak wedge; NOT distinctive at leading order) |
| **Class-C plateau, RE-SCOPED to broadcast-type redundancy** (repetition / GHZ / cat), NOT surface-code distance | 058b §4 | two active legs: repetition-code floor persistence + cat-state width ceiling, tied at a fixed ratio (V5UnifiedBudget) | Broadcast domain only — the topological branch now predicts *absence* of plateau; **surface-code clean suppression (Willow Λ≈2) is consistent-BY-CONSTRUCTION, NOT a passed prediction**; the repetition floor is a WATCH ITEM (live cosmic-ray-burst attribution, no confirmation) | **Prediction (domain-restricted-under-tension)** |

### Selected / inherited (a value fixed by measurement, not derived)
| Item | Paper | Status |
|---|---|---|
| **140–250 kDa Class-A wall mass** (central ~180 kDa) | 056 §5.2 | **Selected/Inherited (number-pressured — do NOT bank as firm).** A 2-POINT extrapolation (Eibenberger 2013 ~10 kDa + Fein 2019 ~25 kDa); re-anchors within the same form if measured elsewhere. **UNDER PRESSURE: matter-wave interference already shown at ≥170 kDa (Nature 2026), inside the window, still QM-consistent — number squeezed from below. Paper_056 does NOT record this (STALE, Staleness #1).** |
| Substrate coefficients `Γ₀, γ, α, β, Γ_decoupling, Γ_indiv, ξ₀, Δ₀, B_cross,max, R_C^sat, Γ_plateau` | 053–058 | **Selected/Inherited** — all empirically anchored / platform-inherited |
| Specific codes (surface, Majorana, Shor, Steane, concatenated); rigidity/redundancy parameters ξ, R_C | 057, 058 | **Inherited** (platform design / standard QI) |

### Synthesis
| Claim | Paper | Status |
|---|---|---|
| Q-Compute arc consolidation (053–060); "decoherence-centric → multiplicity-centric" reframing | 061 | **Synthesis** (the reframing row is A→position in its own audit); introduces no new primitives |
| Cross-domain echo: the BH horizon `Γ_cross→0` collapse and Q-Compute `M_cap` saturation share one V5 mechanism | 062 | **Synthesis / Asserted (A→position** — "no platform realizes a horizon"; rests on P-V5-Shared-Mechanism) |

### Open
| Item | Paper | Status |
|---|---|---|
| Formal mathematical independence of the three UR-1 rate quantities (A/B/C distinctness + exhaustiveness inherit only "distinct primary drivers") | 054 §3.5 | **OPEN** |
| The **power-law form of `Γ_commit(M_eff)`** (A→regime) — alternatives (exponential, log) are substrate-consistent and would change `M_cap` **and the wall** | 054 | **OPEN** — load-bearing under both the wall's shape and number |
| Substrate-level derivation of P-Rigidity-Gap + P-Boltz-Analogy from primitives (currently by analogy) | 057 | OPEN ("in-queue") |
| Strategy-1 substrate-derived platform-scaling commitments (cross-platform unification carries acknowledged retroactive-fit risk until closed) | 056 §6.2 | OPEN — only the sharp/architecture-independent *form* is retroactive-fit-immune today |
| The repetition-code-floor discriminator: does a residual floor survive burst mitigation at cross-platform-consistent converted content? | 058b §5 | OPEN — the live experiment; **no confirmation claimed** |

### Staleness & README-refinements
1. **Paper_056 STALE on the number — FIXED 2026-07-29.** It presented 140–250 kDa with no mention of the ≥170 kDa Nature-2026 result inside the window. **A dated update note added to Paper_056 §1.1** (the ≥170 kDa pressure squeezes the number from below but does not touch the shape claim; second-harmonic confounded) — keeping the shape-not-number framing. **README also updated** (below).
2. **The second-harmonic leg STALE in-folder — FIXED 2026-07-29.** No q-compute paper mentioned it; it lived only in the predictions list §4.2 (CONFOUNDED 2026-07-24: KDTL optics make harmonics anyway; a real test needs *excess* over Nimmrichter–Hornberger). **Now recorded in the Paper_056 update note** — not to be treated anywhere as a clean test.
3. **Paper_058 pre-settlement surface-code prediction — FIXED 2026-07-29.** 058's headline test (§5.1/§7) predicted surface/concatenated codes plateau in code distance; 058b (α_topological=0) restricts the mechanism to broadcast-type. 058b's "058 anticipated this" overstates 058's text; 058b's own §3/§4 domain-restriction framing is the reliable one. **A forward-pointer banner added to Paper_058** → read its surface-code framing through 058b (broadcast-type, not surface-code distance; Willow clean suppression = consistent-by-construction). Base 058 body otherwise unchanged.
4. **README tier optimism — FIXED 2026-07-29.** README called the arc "CLOSED" and exhaustiveness "proven / substrate-grounded"; the papers make exhaustiveness rest on P-Three-Constituent + P-Always-Binding (conditional on the 13-primitive ontology). **README updated** to "form-complete / **Grounded** (postulate-conditional), not a from-nothing proof," + the wall shape-not-number note. *(The broader `event-density/docs/ED_Research_Targets.md` "CLOSED-column" wording is out-of-folder, left for that doc's own pass.)*
5. **Class-B distinctiveness caveat under-flagged in the README.** 057 itself is honest (§6.1: the exponential form is predicted by both ED and topological-QC; the wedge is only at higher order), but the README lists 4.9 without surfacing that the leading-order signature is NOT distinctive. Record-only.
6. **No Wolfram/Ruliad citations** found anywhere in the folder — clean.

### Honest arc-state
The Q-Compute arc is a **coherent, well-audited structure whose spine is Grounded, not Derived** — 053 (`M_cap` as `min` of three constituents), 054 (UR-1's three-component unresolvedness), 055 (A/B/C exhaustiveness), and 060 (M_crit unification) each rest on declared paper-specific postulates (P-Mcap-Unification, P-Three-Constituent, P-Always-Binding, P-Mcrit-Unified) plus one A→regime power-law assumption, and the papers are honest about this in their own audits (exhaustiveness is conditional on the 13-primitive ontology; the three rate quantities have "distinct primary drivers," not proven independence). **The two near-term weapons are in different honest states.** The **Class-A wall's shape (sharp, architecture-independent) is a genuinely distinctive live prediction** — it diverges from decoherence-only and CSL — but its **number (140–250 kDa) is a two-point extrapolation now squeezed from below by ≥170 kDa matter-wave interference (Nature 2026)**, and its second-harmonic secondary signature is **confounded**; neither correction has been written back into Paper_056 or the README, which remain stale and over-bank the number. The **Class-C plateau has been domain-restricted under tension**: 058b's α_topological=0 relocates the mechanism from surface-code distance (where codes suppress cleanly — now consistent-by-construction, not a passed test) to broadcast-type redundancy, leaving a repetition-floor + cat-width-ceiling pair as the active test (the floor an explicit watch item with a live cosmic-ray-burst attribution, no confirmation claimed). Class-B's exponential form is real but **not distinctive from standard topological-QC at leading order**. **Defensible headline:** *a sound, self-honest Grounded arc (M_cap/UR-1/exhaustiveness all postulate-conditional, not proven) carrying two weapons in candid states — the Class-A wall shape-real but number-pressured (≥170 kDa) and second-harmonic-confounded, the Class-C plateau domain-restricted-under-tension to broadcast-type — whose only real debt is that the authoritative in-folder docs (Paper_056, README) lag the 2026-07 corrections that currently live only in the predictions list.*
