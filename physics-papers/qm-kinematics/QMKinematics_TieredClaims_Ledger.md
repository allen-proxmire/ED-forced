# QM-Kinematics Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the qm-kinematics folder (the reconstruction of QM from the substrate) and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing with a row is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** Read every paper; tier each claim *from the paper's own audit table / status line / "does NOT claim"* — never inflated (the README is optimistic on 002/003 and **stale on the Gleason step** — that is the point of this ledger). Seeded from the folder README + `event-density/docs/ED_Research_Targets.md` (#8b), corrected against the papers *and the sibling reconstruction paper* where they disagree.

**One of a per-folder set.** Companions: `entanglement/…`, `black-hole/…`, `cosmology/…`, `dark-sector/…`, `gravity/…`, `qft/…`.

**Tier key.** `Derived` (M1, from primitives) · `Grounded` (M2/M3 — structural/conditional; form-forced with an identified/inherited value) · `Selected/Inherited` (a value: ℏ, the Tsirelson bound, ℂ from the Solèr menu) · `Postulated` · `Asserted` (A→position) · `Synthesis` · `Open`. `D-via-I` = form derived by applying standard machinery to an inherited input.

*24 papers + the sibling `substrate-evaluation/Paper_QuantumLogicKeystone_GleasonReconstruction.md`. Read 2026-07-29 (extraction agent, then spot-checked).*
*Spot-checked directly against the papers (5, scaled to 24; **no catch** — reliable, incl. the load-bearing reconciliation): (1) **the Gleason step both sides** — Paper_004's Update 2026-07-02 "P-Channel-Orthogonality remains fully open… three routes fail… the blocking postulate" (STALE) vs the reconstruction paper's axiom table "Channel orthogonality — **reduced (given representation)**," ℂ "**selected**," status "reduced to the Solèr technical residual… a reconstruction, not a closed theorem" — confirmed; (2) **002** tensor-product = Postulated ("derived under P-QMkin-Composition… a paper-specific postulate," preamble #2 — README's "Derived" inflated); (3) **003** Born rule rests on "P-LinRate… a postulational commitment, not a derivation" + frequentist interp (README's "Derived" inflated); (4) **012.6** Heisenberg "four-band" = position/momentum/time/energy sectors (P-FourBand, substrate-derivation OPEN), NOT the archived M-series four-band; the ℏ/2 bound is INHERITED (Robertson 1929 + Cauchy-Schwarz + CCR); (5) **004.5** Tsirelson bound INHERITED (Landau-Cirelson 1980), inner-product form M3 — plus the `b_K` vs `√b_K` convention drift confirmed.*

---

### Derived (M1 — from primitives, or D-via-I within the paper's own audit)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Complex polar carrier `P_K = √b_K·e^{iπ_K}` | 001 | carrier form from P01–P04 + P09 (audit = D); `\|P_K\|²=b_K` algebraic | √-convention = P(convention); `arg=π_K` = P(definition); inner product = I | **Derived (carrier form)**; convention-tagged |
| Berry phase `γ_C=∮A·dR` = holonomy of the coarse-grained P05 connection | 009 | D-via-I (holonomy on Paper_016's connection) | numerical γ_C inherited; non-abelian/off-diagonal OPEN; P-Adiabatic-CG, P-Loop-Closure postulated | D-via-I |
| Aharonov-Bohm phase `∮A·dx` from T17 bundle circulation | 010 | D-via-I (fiber-bundle holonomy) | `e/ℏ` inherited; paper states "ED does **not** newly predict AB" | D-via-I |
| Bloch form `ψ_k=e^{ikx}u_k(x)` from discrete translation symmetry | 011 | D-via-I (abelian rep theory) | band content inherited; P-Discrete-Translation + P-Symmetric-Hamiltonian postulated | D-via-I |
| Galilean adjacency/propagation bandwidth-asymmetry | 012.7 | asymmetry FORCED by P03 (adjacency invariant) + P04 (propagation transforms) | **full Galilean/Bargmann cohomology OPEN** (P03 necessary, not sufficient); m inherited | Grounded (M3), restricted scope |

### Grounded (M2/M3 — form-forced/identified with an inherited or identified value)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Born rule `f_K=\|c_K\|²` as the participation-frequency limit | 003 | frequency limit `f_K=b_K/Σb` → Born (audit D) | **rests on P-LinRate (P, load-bearing) + frequentist interp (A→assumption)** | **Grounded, NOT pure-M1** (paper softens it; README "Derived" inflated) |
| `P_K=√b_K·e^{iπ_K}` amplitude carrier, complex-valued forced | 003.5 | form FORCED by P04+P05+P09+interference (3 args) | b_K, π_K values inherited | M3 |
| Sesquilinear inner-product form `⟨P,Q⟩=ΣP_K*Q_K` (discrete) | 004.5 | form M3-FORCED from P04+P09+composition | **Tsirelson bound `2√2` INHERITED** (Landau-Cirelson 1980); uses `P_K=b_K e^{iπ}` (`\|P\|²=b²`), inconsistent with 001/003.5's corrected √b (Staleness #4) | M3 (form); Tsirelson Inherited |
| Continuum inner-product `∫Ψ*Φ dμ` on `L²(M,dμ)` | 004.6 | form-consistent under DCGT + P-ScaleSeparation | measure conventions inherited | M3 |
| Projective measurement (projector `Π_K`, collapse, Born prob) | 005 | post-state/completeness follow; Born prob D-conditional on P-LinRate | **P-Commit-Projector-Match (P) load-bearing**; rests on P-Channel-Orthogonality (from 004) | Grounded/Postulated |
| Double-slit interference `ρ=\|ΣP_K\|²`, which-path = V5 injection | 005.5 | M3 form-IDENTIFIED (zero pure-D rows) | fringe geom, λ=h/p, visibility inherited; Θ_ED value + V5-injection-rate OPEN; **Θ_ED "P12 ED-threshold" mislabel corrected 2026-07-06** (Staleness #6) | M3 (identification) |
| Unitary evolution → Schrödinger `iℏ∂_tΨ=HΨ` | 006 | norm-preserving ⇒ unitary; Stone ⇒ Hamiltonian form | **P-Norm-Preservation (P) load-bearing**; Stone + polarization = I; specific H inherited | Grounded (conditional) |
| Schrödinger equation via Stone's theorem | 006.5 | load-bearing = the substrate identification (P11→norm-preservation, P13→time-translation) | **Schrödinger eqn itself = P (definitional, Paper_095 §2.3)**; Stone = I; ℏ inherited | M2 (Intermediate Path C) |
| Kinetic operator `T̂=p̂²/2m`, the factor-2 | 006.6 | factor-2 form-FORCED **via the NR limit of Klein-Gordon** | **independent substrate-Galilean-Jacobian derivation of ½ = OPEN**; V(x), m inherited | M3; ½-from-primitives Open |
| Schrödinger emergence in the thin-participation limit | 006.7 | leading-order unitary form forced in-regime | **V1→unitary coarse-graining OPEN** (asserted via DCGT analogy) | M2, partly Open |
| Hilbert space = Cauchy completion of the motif algebra | 007 | emergence D-conditional on P-Motif-Algebra (P) + Cauchy (I) | **inner product = I (Paper #3); the I→D relabel needs both Gleason postulates** — see Staleness #1 | Grounded; inner-product edge Open/**superseded** |
| Phase structure `S¹/U(1)` on rule-types | 008 | form-FORCED by P09+P10 + 3 postulates | 2π normalization inherited; O-Phase-1..4 open | M3 |
| Phase-independence of bandwidth = U(1) gauge invariance | 008.5 | polar-decomp invariance lemma + **identification** with U(1) gauge | substrate derivation of U(1) gauge invariance from P09 alone OPEN; role of P11 OPEN | M3 (lemma + identification) |
| Momentum operator `p̂=−iℏ∇` = translation generator | 012.5 | form-identified via Stone on the P03 translation group; CCR `[x,p]=iℏ` follows | **P-MomentumIdentification declared (substrate derivation OPEN)**; `−iℏ∇` named as P; **ℏ INHERITED** | M3; ℏ Inherited |
| Heisenberg `Δx·Δp ≥ ℏ/2` | 012.6 | composition D-via-I | **bound INHERITED (Robertson 1929 + Cauchy-Schwarz + CCR)**; `ℏ/2` inherited; P-FourBand declared, substrate-derivation OPEN | M3; bound Inherited; four-band Open |

### Selected / inherited (a value from measurement, or a menu-selection)
| Item | Paper | Status |
|---|---|---|
| `ℏ` throughout the operator sub-arc | 012.5, 012.6, 006.5, 006.6 | **value INHERITED** (Paper_RQM_hbar) |
| Tsirelson bound `2√2` | 004.5 | **INHERITED** from Landau-Cirelson 1980 (a standing construction — NOT the separately-retracted "Tsirelson reduction" V5 characterization) |
| Complex field ℂ (from the Solèr menu `{ℝ,ℂ,ℍ}`) | Gleason-Recon (sibling) | **SELECTED** (account): P09 scalar phase rules out ℝ; V5/063 composites rule out ℍ |

### Postulated
| Claim | Paper | Note | Status |
|---|---|---|---|
| Tensor-product composition `Ψ^{AB}=Ψ^A⊗Ψ^B` | 002 | **P-QMkin-Composition** — "not from P02+P03 alone… a paper-specific postulate" (preamble #2); companion to Paper_063 | **Postulated** (README "Derived" inflated) |
| P-RB-1 local rate of becoming; substrate-c constancy | 012 | "a commitment, not a set of derivations"; ℏ (O-RB-1) and c-from-deeper (O-RB-2) OPEN | Postulated (foundational commitment) |

### Synthesis
| Claim | Paper | Note | Status |
|---|---|---|---|
| Four QM postulates unified under the participation measure | 011.5 | four postulates = "four facets of one substrate structure" via distinct primitive routes | **Synthesis (M2)** — explicitly NOT a Hardy/CDP closed-proof; per-theorem substrate closure OPEN |

### Open (the arc's declared edge) — and the reconstruction that moved it
| Claim | Paper | Status |
|---|---|---|
| Substrate Gleason: inner-product uniqueness | 004 | **Open — but this framing is STALE.** Under P-Channel-Orthogonality + P-Gleason-Compatibility the form is determined; Paper_004's Update 2026-07-02 says P-Channel-Orthogonality "remains fully open / three routes fail / blocking." **Superseded by the reconstruction (next row).** |
| Inner-product row for Hilbert space | 007 | stays **I**; same 2026-07-02 blocking note — **stale/superseded** |
| **Orthogonality reduced; ℂ selected; residual = Solèr** | **Gleason-Recon** (`substrate-evaluation/`, ~July 2026) | **the current word.** Channel-orthogonality **REDUCED to channel-distinctness *given the representation*** (operational distinguishability, Move 1); ℂ **selected**; covering law candidate-grounded (channel basis); einselection **primitive**; Born non-contextuality resolved; equal-norm/angle condition **discharged 2026-07-10**. Residual = **Solèr lattice technical rigor only**. Honest status: **"reduced to the Solèr residual" — stronger than 004's "blocking," weaker than "closed theorem."** |

### Staleness & README-refinements
1. **THE Gleason reconciliation (the load-bearing write-back) — FIXED 2026-07-29.** Papers **004 and 007 were STALE**: both carried the 2026-07-02 verdict "P-Channel-Orthogonality fully open / three routes fail / blocking; inner product stays I." The later `substrate-evaluation/Paper_QuantumLogicKeystone_GleasonReconstruction.md` **supersedes** this — orthogonality **reduced** to channel-distinctness *given the representation* (operational distinguishability), **ℂ selected**, covering law candidate-grounded, Born non-contextuality resolved, the **equal-norm/angle condition discharged (2026-07-10)**, residual narrowed to **the Solèr lattice technical rigor alone**. Memory (`project_pchannel_orthogonality_target`, `project_gleason_complementarity_reframe`) is current and correct. **Applied:** dated "Update 2026-07-29" pointers added to **Paper_004** (a new update section) and **Paper_007 §preamble-3**, changing "fully open/blocking" → "reduced to the Solèr residual." *(This is the exact drift CLAUDE.md names — #8b read "blocking" while the keystone had been reconstructed.)*
2. **Both READMEs echoed the stale framing — FIXED 2026-07-29.** `qm-kinematics/README.md` and `substrate-evaluation/README.md` both reproduced the pre-reconstruction "not closed / three routes fail / Partial" language. **Both updated** to "reduced to the Solèr residual (stronger than blocking, short of a closed theorem)."
3. **README tier inflation on 002 and 003 — FIXED 2026-07-29.** README marked 002 = Derived and 003 = Derived; the papers' own audits make 002 **Postulated** (P-QMkin-Composition) and 003 **Grounded** (P-LinRate + a frequentist A→assumption). **qm-kinematics README table updated** to Postulated / Grounded with the reason inline.
4. **Convention inconsistency 004.5 vs 001/003.5.** 004.5 (and 004.6, which inherits it) still uses `P_K = b_K·e^{iπ_K}` (`\|P_K\|²=b_K²`) while 001/003.5 corrected this to `√b_K` (`\|P_K\|²=b_K`). 004.5 was not swept when the convention was fixed. Minor but load-bearing for `⟨P,P⟩=Σb_K²` vs `Σb_K`.
5. **"Four-band partition" (012.6) — checked, CLEAN (not the archived M-series).** 012.6's four bands are position/momentum/time/energy *sectors*, declared as **P-FourBand with substrate-derivation OPEN**, and **not load-bearing** for the ℏ/2 bound (which is entirely inherited Robertson + Cauchy-Schwarz + CCR). Flagging only because the phrase collides with the M-series flag — the sourcing here is clean. *(Reconciles the memory `project_substrate_higgs_emergence` four-band concern: that was the archived dwell-mass, not this.)*
6. **Θ_ED mislabel — self-corrected but propagates.** 005.5's "P12 (ED-threshold)" is a mislabel (canonical P087 P12 is a stability-landscape functional); flagged in-paper 2026-07-06 (origin = the CCC paper, itself flagged). Verdict unaffected (Θ_ED remains INHERITED), but any doc citing "P12 = ED-threshold" is stale.
7. **Wolfram/Ruliad in the Wave-3 U-series papers** (003.5, 004.5, 004.6, 006.5, 006.6, 006.7, 008.5, 011.5, 012.5, 012.6, 012.7) — the standard Position-Statement lineage line. Violates the no-Wolfram-in-public rule. **AP's standing call: leave it.** Record-only.
8. **Cross-reference numbering drift.** The Wave-3 papers cite the Born rule as "Paper_002 (Born-Gleason)" while in this folder 002 is *TensorProduct* and the Born rule is 003; the internal "U-series" numbering (U1=003.5, U2=004.5/6, U3=006.5, U4=006.6, U5=012.5) does not match the filenames. A cold reader will mis-resolve these. *(Candidate cleanup, low priority.)*

### Honest arc-state
The QM-kinematics arc is **substantially closed as a compositional synthesis (M2), not as a closed-proof reconstruction** — and every paper says so in its own voice. The spine is real: pre-individuation amplitudes (001, D-carrier), the Born rule as the participation-frequency limit (003 — the anchor, but conditional on the **P-LinRate** postulate + a frequentist assumption, not pure-M1), Hilbert space as Cauchy completion (007), projective measurement from P11 (005), unitary evolution / Schrödinger via Stone (006/006.5), and the operator layer (`p̂=−iℏ∇`, `T̂=p̂²/2m`, `Δx·Δp≥ℏ/2`) all form-forced/identified with **ℏ honestly inherited**. The phase phenomena (Berry, AB, Bloch) are D-via-I holonomy/rep-theory audits the papers correctly decline to sell as novel predictions. The genuinely **open edge is the inner product**, and here the folder is the known staleness hotspot: **papers 004/007 and both READMEs still carry the pre-July-2026 "P-Channel-Orthogonality is blocking / three routes fail" verdict, which the later Gleason-keystone reconstruction has superseded** — orthogonality is now *reduced* to channel-distinctness given the representation, ℂ is *selected*, the equal-norm condition was *discharged* (2026-07-10), and the residual is narrowed to **the Solèr lattice technical rigor alone**. That is a reduction, not a closed theorem, so the arc's honest status is **"closed synthesis with one technical residual (Solèr) under the inner-product metric,"** and memory already reflects this while the qm-kinematics papers and READMEs do not — those are the concrete write-back targets. **Defensible headline:** *the four QM postulates and the standard phenomena are reproduced as a compositional synthesis (M2) — form-forced/identified with ℏ and the Tsirelson bound honestly inherited and the Born rule resting on P-LinRate — with the inner-product edge now "reduced to the Solèr residual" (a reconstruction, not a closed theorem); the papers 004/007 + both READMEs are stale on that edge and are the write-back targets.*

---

## Addendum 2026-09-04 — the ℝ-exclusion in the ℂ-selection is carried by a representation, not a primitive

**The ℝ-exclusion's ED-side premise is a representational choice, and unlike its neighbour it is not flagged.**

§5 rules out ℝ well: it explicitly rejects the naive argument (*"a real space cannot represent a phase"* — false, real-Hilbert QM represents `U(1)` via `J` with `J² = −I`) and identifies the correct discriminator as **scalar versus operator**. A real division ring has no central scalar square root of `−1`, so if ED's phase is a *scalar* amplitude factor the field must contain `i`. That clarification is genuine and non-obvious.

The question is where *"ED's phase is a scalar"* comes from. The section cites `Paper_001`'s carrier `P_K = √b_K·e^{iπ_K}`. But **P09 supplies an angle, not a complex number** — `U(1)` is definable as `ℝ/2πℤ` or `SO(2)` with no reference to ℂ — and writing that angle as `e^{iπ}` rather than as a rotation `J(π)` on a real 2-space is a **representational choice made in `Paper_001`**. So the chain is: P09 gives an angle → `Paper_001` represents it as a complex scalar → §5 rules out ℝ because the phase is a scalar. **The step that excludes ℝ is the representation, not the primitive.**

**Both papers are honest about tier, and that is why this is a disclosure finding rather than an error.** `Paper_QuantumLogicKeystone` preamble item 2 calls it *"an account-tier selection, not a from-scratch derivation."* `Paper_001` preamble item 2 says the complex carrier is not forced from P01–P04 alone and needs P09. Neither claims a derivation. What is missing is narrower: **§5's ℝ-argument does not name its premise, while §5's ℍ-argument does** — the latter states outright that *"the ED-side premise (that ED has a genuine ⊗) is supplied by P-Bipartite-Mapping / Paper_063, a paper-specific postulate, not one of the canonical 13."* Asymmetric disclosure inside one section, and the undisclosed side is the one carrying more weight.

**This answers the question left open in `Paper_PrimitiveMinimality_IndependentReconstructionProbe` §6.** Both blind runs concluded that phase and complex amplitudes must be *injected*, which raised the question of how much the Solèr selection does given P09 already carries a `U(1)`. **The answer is that the two halves differ.** The ℍ-exclusion does real work and is honestly conditioned. The ℝ-exclusion does less than it appears: **P09 alone is consistent with ℝ**, and what rules ℝ out is `Paper_001`'s scalar representation. The blind runs were right that something must be put in; ED's answer is P09 *plus* a representational commitment, and only the first is a declared primitive.

**The repair is available and would strengthen the claim rather than weaken it.** Argue from the primitives why the phase must act as a **scalar** — uniformly on all amplitudes at a locus — rather than as an operator that could act channel-dependently. P03 (spatial homogeneity / no preferred channel) and P07 (channel distinguishability) are the natural candidates: if the phase were an operator it could mix channels, which P07's intrinsic-identity commitment arguably forbids. **Not attempted here.** If it works, the ℝ-exclusion becomes grounded in primitives and the selection is genuinely a selection. **Recommended minimum, pending that:** §5's ℝ-bullet should name its premise the way its ℍ-bullet does — one clause, and it removes the asymmetry.

*No tier changed; both papers sit at account tier. Cross-filed as `gravity/Gravity_TieredClaims_Ledger.md` Staleness #21.*

### Repair attempted, same day

**P03/P07 do not deliver it, and the reason is worth recording so nobody retries.** The scalar-versus-operator distinction is *not* about channel mixing. Real-Hilbert QM's complex structure `J` acts **within** each channel's two-real-dimensional amplitude space; it never mixes distinct channels. So P07's intrinsic-identity commitment is simply not engaged — it forbids something the operator route does not do. And P03's translation-invariance requires only that `J` be the same at every locus, which is trivially satisfiable. **Neither primitive touches the question.**

**A different argument does work, and it is grounded rather than notational.** The discriminator is not *where the phase lives* but **whether relative phase is continuously observable**, and ED's own results settle that:

1. **P09** gives each channel a *continuous* `U(1)` phase `π_K`.
2. **The corpus makes relative phase observable, continuously.** `Paper_QuadraticStrain_v1` §3.2 carries `2√(b^{(a)}b^{(b)})·cosΘ_{ab}`, and `Paper_005.5` §3.3 the double-slit `ρ = b_A + b_B + 2√(b_A b_B)·cosΔπ`. The cross-term's dependence on `Θ` is **continuous**, not two-valued.
3. **A real amplitude space cannot do that.** Superposing real amplitudes gives `(x_A + x_B)² = x_A² + x_B² + 2x_Ax_B`: there *is* a cross term, but its sign is all the freedom there is. Continuous `cosΘ` dependence requires each channel's amplitude space to be **at least two real dimensions carrying a rotation action** — that is a complex structure `J`.
4. **And a `J` commuting with all observables is ℂ** (Stueckelberg). So the effective field is complex.

**Therefore `K ≠ ℝ`, on ED's declared structure rather than on how `Paper_001` writes its carrier.**

**Status, stated at the tier it earns.** This remains **account-tier**: it is conditional on the interference results of step 2, which rest on P-Quadratic-Strain and the Born-rule reading, not on the canonical thirteen alone. What it *does* fix is the circularity: the ℝ-exclusion no longer rests on `Paper_001` having written `e^{iπ}` — it rests on ED's phase being **continuously observable through interference**, which is a corpus result with its own tier and its own falsifier. **It is also now empirically anchored:** were ED's interference sign-only rather than continuous in `Θ`, ℝ would be admissible. That is a statement about the world, which the notational version was not.

*Recommended and not applied: fold the four steps into §5's ℝ-bullet, replacing the appeal to `Paper_001`'s carrier form. It rewrites a headline argument.*
