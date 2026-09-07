# Q-Compute Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the q-compute folder (decoherence limits / quantum-hardware architecture) and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** Read every paper; tier each claim *from the paper's own audit/status/verdict* — never inflated. Seeded from the folder README + `event-density/docs/ED_Research_Targets.md`, corrected against the papers **and the live `ED_Master_Predictions_List` corrections** (which the folder itself has not fully absorbed — see Staleness).

**One of a per-folder set.** This folder holds **two of the corpus's near-term weapons** (the Class-A mass wall, the Class-C error-correction plateau); their honest status is the load-bearing content.

**Tier key.** `Derived` (from primitives, conditional on the 13 postulated primitives) · `Grounded` (conditional/structural — carries a paper-specific postulate or an A→regime assumption) · `Measured` · `Selected/Inherited` (a value from measurement) · `Postulated` · `Asserted` (A→position) · `Prediction` (falsifiable, experiment-facing) · `Synthesis` · `Open`.

*11 papers. Read 2026-07-29 (extraction agent, then spot-checked).*
*Spot-checked directly against the papers (4, scaled to 11; **no catch**): (1) **056** shape-not-number is explicit ("the structural prediction is the wall itself… the 140–250 kDa value is an extrapolation, not a substrate-level prediction; 2-point anchor") — and **056 IS stale on the number** (no mention of the ≥170 kDa Nature-2026 pressure or the confounded second-harmonic); (2) **058b** α_topological=0 boxed, plateau re-scoped to broadcast-type, Willow tension "converted into a match" — confirmed; (3) **058 original** DID predict surface-code plateau as its headline near-term test, so 058b's "058 anticipated this" **overstates** it (058b's own domain-restriction framing is the honest one); (4) **055** exhaustiveness rests on P-Three-Constituent + P-Always-Binding — Grounded conditional, NOT "proven" as the README says.*

---

### Derived (from primitives, conditional on the 13 postulated primitives) — workbook tier: PER ROW (see rule below)

> **Transcription rule — `ED_ItemizedTheory_TieredClaims*.xlsx`.** That workbook's `Derived` tier is **narrower than this heading**: *“forced/proven from the 13 primitives (+ standard math) with **NO** paper-specific postulate.”* **This section is mixed, so take the tier from the ROW, never from this heading.** If a row's *“Inherited / open”* cell names a `P-` postulate, or says *conditional on* / *rests on*, its workbook tier is **`Grounded`** — or **`Postulated`** where the postulate carries the claim — **not `Derived`**. *(Here: **1 of 4** rows currently name a postulate.)* **Losing this qualifier in transcription over-promoted ten rows before 2026-09-06**, because the caveat lived in a parenthetical and parentheticals do not travel. See `gravity/Gravity_TieredClaims_Ledger.md` #122 and #124.

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

---

## 2026-09-07 (2) — `Γ_commit`'s functional form: exponential and log EXCLUDED, `γ` two-valued, tier `A→regime` → `Grounded`

**AP's call after the wall's number lost half its range** (#previous entry): go at the load-bearing open piece rather than the number. **`Paper_054` §3.2 had the power-law form at `A→regime` with *“exponential, logarithmic, etc.”* named as substrate-consistent alternatives** — and the arc ledger lists it as open under **both** the wall's shape and its number.

**The finding is that §3.2 was leaving its own answer on the table.** It invokes P12's `Σ_C = Coh − Str − Grad` as what drives commitment, and then **posits** the multiplicity dependence instead of **reading it off `Σ_C`**. The 2026-09-05 three-way sign check (foundations #10) had already settled the two terms' form, and once you have the forms the *counting* is not a choice:

> `Str_K = Σ_a b_K^(a)` is a **single** sum — `M` terms. `Coh_K = 2Σ_{a<b}√(b_K^(a) b_K^(b)) cos Θ_ab` is a **double** sum — `M(M−1)/2` pairs. **A single sum and a double sum cannot scale alike.**

**Three consequences, checked numerically rather than argued** (`../event-density/theory/gamma_commit_form_probe.py`):

1. **The named alternatives are EXCLUDED, not merely disfavoured.** A finite double sum over pairs is **polynomially bounded**, so no exponential can arise from it; and a logarithm grows slower than `Str`, which P04 additivity makes **exactly linear** (measured slope `0.999`). Both alternatives needed a characteristic multiplicity `M₀`, and **the only candidate the theory has is `M_cap` — which is *defined* as where `Γ_commit` meets `Γ_indiv⁻¹`, so using it inside `Γ_commit` is circular.** `Γ₀ ~ c/ℓ_ED` is a *time* scale and `M_eff` is dimensionless, so it supplies no multiplicity scale either.
2. **The exact form is a two-term polynomial `∝ M² − M`, not a pure power law.** Local slope `3.00 → 2.33 → 2.14 → … → 2.00` across `M = 2 → 1024`, **never leaving `[2,3]`**. *The single-exponent statement is the large-`M` limit: good to a few percent by `M ~ 100`, poor at `M ~ 2–10` — which is the regime a few-qubit Class-A platform actually sits in.*
3. **`γ` is two-valued and set by phase coherence, not fitted.** Coherent → the pair sum survives, `Coh ~ M²`, **`γ → 2`** (measured `2.12`). Decohered → with `z = Σ√b e^{iφ}`, `Coh = |z|² − Σb` and `E[|z|²] = Σb` **exactly**, so **`E[Coh] = 0`**: the pair term **switches off** rather than degrading, leaving `Str` and **`γ = 1`**.

> **✅ And this improves the sharpness argument rather than merely propping it up.** Sharpness had been a property *assumed of* a single power law. It is instead a consequence of **the exponent changing across the transition** — `γ ≈ 2` while the superposition is coherent, `γ = 1` once it is not. **The two sides of the wall obey different laws and the crossing is one-way.** That is a mechanism, and `Paper_056`'s own “the shape is the claim” retreat now stands on something.

**A correction I made to myself mid-probe, recorded because it changed the result.** The first draft asserted the decohered pair sum *“adds in quadrature → M”*. **The numbers said otherwise and the numbers were right:** its mean is **exactly zero**, so a log-fit of it returned a meaningless negative slope. *The corrected version is the stronger claim — “switches off” beats “degrades to linear” — which is the second time this week that checking a convenient-sounding step produced a better result than the step.*

**THE REMAINING GAP, AND IT IS REAL.** All of this pins the multiplicity dependence of **`Σ_C`**. §3.2 needs the dependence of **`Γ_commit`**, and asserts only that *“gradients in `Σ_C` drive commitment”*. **The `Σ_C → rate` map is not supplied by the corpus and is not supplied here.** Monotone and scale-free → the exponents carry through; saturating → they do not. **So the honest tier is `Grounded`, not `Derived`** — the form is forced *given one named map* rather than assumed outright. **The open piece went from “the entire functional form is assumed, with exponentials live” to “one map from a landscape to a rate is unstated”, which is a much better-posed target and the natural next move.**

**Propagated:** `Paper_054` §3.2 + its claims table (re-tiered), `Paper_056`'s 2026-09-04 sharpness caveat.

## 2026-09-07 — The Class-A wall's lower half is EXCLUDED, and the paper's reach claim was backwards

**Picked up at AP's direction** (*“ok lets pick up the higgs stuff”*) after the a₀(z) line was closed as untested. **First finding: the “Higgs stuff” is three results in three folders, not one arc** — the Higgs *negative* (the condensate route comes up empty on the certified field; fundamental Higgs/electroweak mass is inherited, Report §11), the **2020 spontaneous-radiation bound** that ED survives for a computed reason (`state-reduction/`), and **this wall** (`q-compute/Paper_056`). *Only the second and third are pitchable to an experimentalist; the first is the honesty ballast.*

**The finding, and it goes against ED.** `Paper_056`'s 2026-07-29 note reads the Nature result as *“squeezing the extrapolated number from below.”* **That understates a definite outcome.** Verified against two independent sources: **Nature 2026, `10.1038/s41586-025-09917-9`**, *“Probing quantum mechanics with nanoparticle matter-wave interferometry”* — **sodium clusters of >7000 atoms at >175 kDa**, macroscopicity **μ = 15.4–15.5**, **MUSCLE Talbot–Lau interferometer** with UV photodepletion gratings, billed as the most stringent bounds to date on generic macrorealistic modifications of QM.

> **A wall is where superposition FAILS. Interference was OBSERVED at 175 kDa. So there is no wall at or below 175 kDa, and the 140–250 kDa window is truncated to ≈175–250 — about 30% of its original range.** “Under pressure from below” is a softer statement than the evidence supports.

**The obvious escape is closed by the paper's own text, which is why it was worth checking before writing.** One could argue sodium clusters map to `M_eff` differently from organic molecules. **§6.1 forecloses it:** it commits matter-wave interferometry to **mass-scaling, `M_eff ∝ m`**, and reserves platform-specific factors for differences **between platform types** (matter-wave vs SC qubits vs trapped ions), **not between particles within matter-wave.** And the Nature apparatus is **Talbot–Lau — the same interferometer family as §1.1's own Eibenberger 2013 and Fein 2019 anchors.** Same architecture, same committed scaling law, higher mass. **Invoking a particle-specific correction would buy the number at the cost of architecture-independence, which §6.4 names as the retroactive-fit-immune half. Both cannot be kept.**

**✅ And the reach claim was not merely stale but backwards, at three sites.** The paper says the wall is *“5–10× beyond current experimental reach”* and *“testable in 5–10 years”*. **Current reach IS 175 kDa.** The surviving window tops out at 250 kDa — **1.0–1.43× current reach.** **The prediction is testable now and is close to settled either way.** *That is the useful half of the news and it makes the wall MORE interesting to an experimentalist, not less: a decade-out prediction is a talking point, a next-experiment prediction is a collaboration.*

**What is untouched, and it is the half that always mattered:** §6.4's retroactive-fit-immune content — the **sharpness** and the **architecture-independence within Class-A**. Those are tested by comparing platforms against each other, not by one platform reaching higher mass. **The number was always the weaker half; it is now the mostly-spent half.**

**Propagated the same session:** `Paper_056` (a dated update block plus all three reach claims struck), `predictions/22_Ways #16`, `predictions/ED_Master_Predictions_List` 4.1.

**Standing caution this reinforces.** The corpus's own 2026-07-29 note had the fact and drew the weaker conclusion from it. **Two days running, the error has been an under-drawn inference from a correctly-recorded external result rather than a missing fact.** *Recording a number is not the same as working out what it excludes.*

## Addendum 2026-09-04 — external audit: arc clean, one disclosure gap

**The arc has already had this audit, and passed it — the first one today of which that is true.** The q-compute ledger records a spot-check of four papers with **“no catch”**; tiers the 140–250 kDa mass as *“Selected/Inherited (number-pressured — do NOT bank as firm), a 2-POINT extrapolation”*; records `Paper_056` as having been **stale on the number and fixed 2026-07-29** when the ≥170 kDa Nature-2026 result landed inside the window; records **README tier optimism as fixed** (it had called the arc “CLOSED” and exhaustiveness “proven” where the papers rest it on two postulates); and summarises the arc as *“coherent, well-audited … whose spine is **Grounded, not Derived**”*. `Paper_054` labels the power-law form **A→regime** in its own audit table and says in prose that P04 + P11 + V1 give the *existence* of a commit-rate and **do not force its functional form**. Nothing here overclaims.

**The one gap is a disclosure one, in the retreat itself.** `Paper_056`'s 2026-07-29 update moves the claim from the number to the shape: *“Read the **shape** (sharp + architecture-independent) as the prediction, not the 2-point-extrapolated number”*, on the ground that the new data *“does not touch the load-bearing structural claim.”* **But the shape rests on the same open assumption the number does.** The arc's own ledger says so explicitly: the power-law form of `Γ_commit(M_eff)` is **OPEN** and *“load-bearing under both the wall's shape **and** number”*, with exponential and log alternatives substrate-consistent and changing *“`M_cap` **and the wall**”*. **The update note does not mention this.** A reader of `Paper_056` alone takes the retreat as a move to firmer ground; it is a move to ground resting on the same A→regime choice.

**And that weakens the falsifier in a way the public README does not show.** The README row is two-sided — *“superposition past a sharp mass ceiling, **or no ceiling at all**”* — which is a genuinely good structure. But if the power law is what makes the wall *sharp*, then observing a **gradual** falloff instead would not distinguish *“ED is wrong”* from *“the `Γ_commit` form is wrong”*. The sharpness half of the falsifier is only as sharp as an assumption the arc lists as open. *(The architecture-independence half is unaffected and remains the cleaner discriminator — it needs two platforms at comparable mass, which do not yet exist.)*

**Recommended, small.** One clause in `Paper_056`'s update note: that the shape, like the number, is conditional on the power-law `Γ_commit` form (`Paper_054` §3.2, A→regime; arc ledger, open row). And the README's falsifier row should attach the same condition to its *sharpness* clause while leaving *architecture-independence* unconditioned. **No tier changed** — every tier involved is already correct; this is about what the retreat discloses.

*Cross-filed as `gravity/Gravity_TieredClaims_Ledger.md` Staleness #25, which carries the day's audit trail.*

---

## Addendum 2026-09-04 (second entry) — the arc has no near-term test, and a target doc said otherwise

**A target doc pointed at a dead test for six weeks, and it was caught only by acting on it.** Target #16 (*“ED's single most load-bearing current gap”*) closes by naming a **map-independent near-term alternative**: the second-harmonic fingerprint, *“plausibly checkable in existing Fein-2019 / Jan-2026-nanoparticle data”*. **`ED_Master_Predictions_List` 4.2 marks that signature CONFOUNDED, dated 2026-07-24 — the same day target #16 was written.** KDTL grating optics produce higher harmonics anyway, so a bare second harmonic confirms nothing; a real test needs *excess* over the full Nimmrichter–Hornberger optics prediction from **raw** fringe data, which is not published.

**Withdrawn, and the honest near-term status stated in its place.** The matter-wave weapon currently has **no near-term test**: the *number* is pressured (140–250 kDa vs the ≥170 kDa Nature-2026 report, a 2-point extrapolation flagged *do not bank as firm*); the *second harmonic* is confounded; and *architecture-independence* — which ≦25 called the cleaner discriminator — needs two platforms at comparable mass that **do not exist**. The map (#16 proper) remains the gate. Leaving a hopeful clause in place made the arc look more testable than it is.

*Cross-filed as `gravity/Gravity_TieredClaims_Ledger.md` Staleness #41, which carries the day's trail. ML 4.2's CONFOUNDED verdict stands unchanged and was correct; what was wrong was `event-density/docs/ED_Research_Targets.md` #16, now corrected.*

---

## Addendum 2026-09-04 (third entry) — an SCBU projection into this arc

`cosmology/Paper_ED_SC_4_4_QCompute_SCBU.md` projects `ℳ_crit` onto `R_H = c/H₀`, one of six `ED-SC 4.x` projections. **It anchors on `ℳ_crit = 140–250 kDa` three times.** This arc's own tier for that window is *“Selected/Inherited (number-pressured — do NOT bank as firm), a 2-POINT extrapolation”*, and the shape-retreat carries the disclosure gap recorded in this ledger's first 2026-09-04 addendum. **The paper is M3 and unaudited**; treat its projection's *structure* as the claim, not the window. Kept in `cosmology/` with its series. Gravity ledger Staleness #54.
