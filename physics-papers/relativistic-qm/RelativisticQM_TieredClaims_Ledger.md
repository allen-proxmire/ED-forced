# Relativistic-QM Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the relativistic-qm folder and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing with a row is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** Read every paper; tier each claim *from the paper's own audit table / status line / "does NOT claim"* — never inflated. Seeded from the folder README + `event-density/docs/ED_Research_Targets.md` (#2b), corrected against the papers.

**One of a per-folder set.** Companions: `entanglement/…`, `black-hole/…`, `cosmology/…`, `dark-sector/…`, `gravity/…`, `qft/…`, `qm-kinematics/…`.

**Tier key.** `Derived` (M1, pure structural / from primitives + standard math, no numerical inheritance) · `Grounded` (M2/M3 — mechanism identified or form-forced/inherited with an identified/inherited value) · `Selected/Inherited` (a value: ℏ, the commutation constant) · `Postulated` · `Asserted` (A→position) · `Synthesis` · `Open`. *(Note the internal series labels: T1=102, T2=103, T3=104, T4=106, T5=107, T6=108, T7=109, T8=110, T9=111, T10=112; this ledger cites file numbers.)*

*15 papers. Read 2026-07-29 (extraction agent, then spot-checked).*
*Spot-checked directly against the papers (5, scaled to 15; **no catch**): (1) **106 (T4)** "M2 (Intermediate Path C) — explicit substrate-V1→Dirac closed-proof reduction OPEN," graph-native spinor OPEN (P07 supplies no native topology) — confirmed the #2b gate stays open; **and the row-15/§3.7 desync verified** (prose says row 15 moved from OPEN, the table still reads OPEN); (2) **113** mass "asserted, not derived" (rows 10/11 OPEN), and the dwell-mass "licensed by **canonical** P02+P03+P07" — **not** the archived four-band; (3) **104** anyon prohibition M1 "pure dimension-comparison… no inherited numerical content"; (4) **112h** ℏ carries the explicit "§3.3 circularity disclaimer: ℏ=∫B_P04 ds is a relabeling, not a computation," value INHERITED; (5) **102** spin-statistics M3 form-forced/value-inherited.*

---

### Derived (M1 — pure structural, no numerical inheritance load-bearing)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Cl(3,1) frame uniqueness up to similarity | 103 | unique irreducible 4-dim rep of Cl(3,1); all γ-realizations similarity-equivalent (Pauli's thm + Schur) | basis (Dirac/Weyl/Majorana) = choice of S, not value inheritance; conditional on Paper_017 acoustic-metric signature (structural, not numerical) | **M1** — form-IDENTIFIED ("no D rows, downgraded from FORM-FORCED"); conditional on 017, not primitives-alone |
| **Anyon prohibition in 3+1D** | 104 | `π₁(config space)=Sₙ` in d=3 ⟹ only 1-dim reps `η=±1` ⟹ anyons prohibited; anyons require d=2 (braid group `Bₙ`) | effective-2D FQH anyon phases empirical, not load-bearing on the prohibition | **M1** — genuinely primitive-grounded (P06 + standard topology); the cleanest structural result; a distinctive **matter-sector prohibition** |

### Grounded (M2/M3 — form-forced or form-inherited + value inherited)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Spin-statistics `η=(−1)^{2s}` | 102 | dichotomy *form* (only `η=±1`, fermion/boson exhaustive) from P06+P09 exchange topology + `π₁(SO(3))=ℤ₂` | specific spin assignments (e⁻=½, γ=1) empirical; CPT/parity/T sectors deferred | **M3** (FORM-FORCED + VALUE-INHERITED) |
| Lorentz-representation taxonomy | 109 | finite `SL(2,ℂ)` `(j₁,j₂)` taxonomy as substrate rule-type classification | which rule-type↔which rep empirical; Wigner particle-state classification out of scope | **M3** (form-IDENTIFIED + VALUE-INHERITED) |
| Klein-Gordon equation `(□+m²c²/ℏ²)Ψ=0` | 107 | substrate *identification* of m as P04 rest-bandwidth; V1-kernel low-momentum-pole compatibility | **KG form itself is P-definitional / INHERITED** from Paper_017 + std dispersion; V1→KG-propagator substrate-graph derivation not closed | **M3, FORM-INHERITED** — correctly reflects Paper_017's own round-8 D→P relabel; does NOT over-inherit a "derived" KG (Staleness #7, clean) |
| Minimal-coupling KG + conserved 4-current | 108 | extension of KG to U(1) gauge; Noether current from U(1) phase-invariance | minimal-coupling form INHERITED (015/016); couplings empirical; **V5 multi-channel substrate-graph derivation OPEN** | **M3, FORM-INHERITED** |
| Primitive-level UV finiteness | 111 | UV-finiteness from P04 finite bandwidth + P08 scale + V1/V5 finite-kernel form factors | cutoff `ω_c=c/ℓ_P` value inherited; substrate-graph→power-counting derivation OPEN; renorm-reframe = A→position | **M3** (form-IDENTIFIED + VALUE-INHERITED) |
| Lightlike worldlines for `σ=0` rule-types | 112 (T10) | null-geodesic propagation form-forced from massless dispersion (T5 at m=0) + std null-geodesic geometry | **EXISTENCE of `σ=0` rule-types CONDITIONAL on Paper_114**; substrate-c inherited; V1 at m=0 substrate-graph derivation OPEN | **M3** (structure forced, existence conditional) |
| Vacuum + particle dual Fock structure (`σ=0`) | 115 | vacuum + 1-particle Fock decomposition from T10 + T8 + Wightman uniqueness | "no rest-frame ⟹ minimal dual" is heuristic, OPEN; mode-density normalization inherited | **M3** |
| MR-R / MR-P conditional massless slot | 116 | two-branch *mutually-exclusive* massless slot (fermion-chiral MR-R / gauge MR-P); disjointness forced by T7 | no-third-mechanism exhaustiveness OPEN; specific occupants empirical (neutrino MR-R); substrate-c inherited | **M3** |

### The T4 gate (M2 — mechanism identified, closed derivation OPEN; the program's highest-leverage open item)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| **Dirac equation `(iγ^μ∂_μ − mc/ℏ)Ψ=0`** | 106 (T4) | structural mechanism identified: unique first-order Clifford-linear operator factorizing KG on the Cl(3,1) bundle; §3.7 (2026-07-10) continuum limit **computed** (`D(p)≈iγ^μp`) + Wilson-term Nielsen-Ninomiya undoubling `16→1` | **explicit substrate-V1→Dirac closed proof OPEN; fully-covariant canonical-V1 proof OPEN; graph-native spinor construction OPEN (canonical P07 supplies NO native channel topology)**; mass inherited | **M2 (Intermediate Path C)** — does NOT claim a closed Dirac / spinor derivation; **chirality NOT claimed derived** (defaults vector, parity inherited per corpus). **The #2b gate the whole chiral-gauge frontier reduces to — genuinely OPEN.** *(Row-15/§3.7 desync — Staleness #1.)* |

### Selected / inherited (value from measurement)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Canonical (anti-)commutation `[x̂,p̂]=iℏ` | 110 (T8) | the commutator-vs-anticommutator *dichotomy* forced by T1 (bosonic↔commutator, fermionic↔anticommutator) | relation *forms* are P-definitional; **ℏ INHERITED**; the earlier "structural origin of ℏ" framing explicitly disowned as oversold | **M3, FORM-INHERITED + VALUE-INHERITED** |
| ℏ origin = participation quantum per chain-step | 112 (hbar) | dimensional structure (action=bandwidth×time) form-forced by P04+P05+P11; chain-step invariance (P03+P13) ⟹ ℏ universal | **numerical value INHERITED; B_P04 has NO independent substrate definition — §3.3 circularity disclaimer: ℏ=∫B_P04 ds is a relabeling, not a computation** | **M3**, value-INHERITED with explicit (and honest) structural-origin |

### Postulated
| Claim | Paper | Note | Status |
|---|---|---|---|
| P-Gauge (paper-specific postulate) | 114 | gauge-class connection `Aμ` on rule-type bundles + gauge-quotient; **substrate derivation from P05+P07+P09+P10 alone OPEN** (F-Gauge would upgrade M2→M1) | **Postulated** (declared, non-primitive) |

### Grounded-conditional (M2 — conditional on a postulate)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Existence of ≥1 massless Case-P gauge rule-type | 114 (GRH-D1) | existence form-forced *conditional on* P-Gauge + T17 (015) + gauge-quotient (022) | specific gauge groups/couplings inherited; **P-Gauge substrate derivation OPEN** | **M2** — "unconditional" (in title) means unconditional on *which* gauge group, but conditional on the P-Gauge postulate; 112's `σ=0` existence depends on this |

### Mass sector (M2 with OPEN flags — asserted, not derived)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Mass structural form (Arc-M H1) | 113 | 3 structural features form-forced: Lorentz-scalar, P04-bandwidth-anchored, statistics-class-mechanism | **substrate-Higgs §3.3 + substrate-Yukawa §3.5 ASSERTED, NOT derived — OPEN**; all mass values empirical; the substrate origin of "statistics-class-mechanism" itself OPEN | **M2 with OPEN flags** — mass sector open/asserted, not derived. **NOT built on archived four-band**: the dwell-mass diagnostic (row 10) is licensed by *canonical* P02+P03+P07, flagged conditional/not-forced |

### Asserted (A→position framing rows)
| Claim | Paper(s) | Status |
|---|---|---|
| "UV divergences = coarse-graining artifacts of `ω_c→∞`"; renormalization = substrate-cutoff-absorption | 111 (rows 8–10) | A→position (explicitly not a derivation) |
| Arc-R stage placements (KG=R.1, Dirac=R.3, …); H1-dominant regime; M-verdict rows | 106, 107, 108, 111, 113 | A→position (position-statement classification) |

### Staleness & README-refinements
1. **Paper_106 internal desync (T4 gate) — FIXED 2026-07-29.** The §3.7 prose update (2026-07-10) said the substrate-V1→Dirac chain is "form-identified + continuum-limit-computed" and that "audit row 15 moves from OPEN," but **audit row 15 still literally read OPEN.** **Row 15 synced** to "form-identified + continuum-limit-computed; residual OPEN (covariant proof + graph-native spinor)," verdict unchanged (M2 — the closed proof is still open). Do NOT read §3.7 as closing the T4 gate.
2. **Paper_112 (T10) "GRH in queue" is stale — FIXED 2026-07-29.** 112 conditioned `σ=0` existence on "GRH unconditional D1 (Paper_RQM-GRH-D1 **in queue**)"; GRH-D1 has since **landed as Paper_114** (M2, conditional on the P-Gauge postulate — not "unconditional"). **A dated update note added to Paper_112** reads "GRH in queue" as "Paper_114, conditional on the P-Gauge postulate."
3. **Number collision.** Two files share number 112: `Paper_112_LightlikeWorldlines` (T10) and `Paper_112_hbar_Origin` (ℏ). A rename would be cleaner but breaks cross-refs — flagged, not done.
4. **File-number vs series-label mismatch.** Every in-paper cross-reference uses `Paper_RQM_T*` / Arc names (T1=102, T4=106, …), never the file numbers, so a cold reader needs the README map to follow citations. Candidate: file-number aliases. (Low priority.)
5. **Wolfram/Ruliad in all 15 Position Statements** (the standard lineage sentence). Violates the no-Wolfram-in-public rule. **AP's standing call: leave it.** Record-only.
6. **Paper_113 row-10 dwell-mass working-note dependence.** Row 10 embeds dated 2026-07-06 dwell-mass results as a "positive structural handle," correctly flagged OPEN/conditional/not-forced and **canonically licensed** (P02+P03+P07, not archived four-band) — watch only that it does not drift into being read as closing the mass gap.
7. **Clean (no action).** Paper_107 correctly labels the KG form itself as P-definitional rather than over-inheriting a "derived" KG from Paper_017 — consistent with 017's own round-8 D→P relabel. No over-claim. *(Reconciles the qft-ledger note that 017's KG is a P-construction.)*

### Honest arc-state
The relativistic-QM arc is **structurally strong at the classification/algebra layer and honestly open at exactly the three places the corpus says it is open.** Two results are genuinely primitive-level **M1** (103 Cl(3,1) uniqueness, 104 anyon prohibition — both honestly "form-IDENTIFIED, no D rows"). The workhorse equations (102 spin-statistics, 107 KG, 108 minimal-coupling, 109 Lorentz reps, 110 canonical relations, 111 UV-finiteness, 115 Fock structure, 116 massless slot) are **M3** with a consistent honest posture: *form* forced or inherited, *values* (masses, couplings, ℏ, the cutoff) inherited, and every substrate-graph→continuum closure flagged OPEN rather than claimed. ℏ (112h) and the commutation constant (110) are correctly value-inherited, with 112h even carrying an explicit **circularity disclaimer** that its "derivation" is a relabeling. The three real frontier gates are all present and correctly *not* inflated: **(1) the T4/Dirac spinor gate (106, M2)** — mechanism identified and the continuum limit now computed, but the closed substrate-V1→Dirac proof and the graph-native spinor construction remain open (canonical P07 supplies no native channel topology), and this is the item the whole chiral-gauge/#2b frontier reduces to; **(2) the mass sector (113, M2 with OPEN flags)** — substrate-Higgs and substrate-Yukawa asserted not derived, and notably *not* resting on archived four-band material (the dwell handle is canonically licensed); **(3) P-Gauge existence (114, M2)** — massless-gauge existence forced only conditional on the declared P-Gauge postulate, whose substrate derivation is open, and on which 112's `σ=0` existence in turn depends. Nothing in the folder over-claims a closed Dirac derivation, a derived mass, or a derived P-Gauge. **Defensible headline:** *the relativistic-QM classification/algebra layer is solid (two M1 structural results incl. the anyon prohibition; the wave equations M3 form-forced/value-inherited with ℏ honestly inherited under a circularity disclaimer), and the three frontier gates — the T4 Dirac spinor (#2b), the mass sector, and P-Gauge — are all present and correctly held OPEN, not inflated; the debts are bookkeeping (the 106 row-15 desync, the stale "GRH in queue" in 112, the duplicate 112 filename), not physics.*
