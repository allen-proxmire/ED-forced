# QFT Arc — Tiered-Claims Ledger

**What this is.** Every load-bearing claim in the qft folder (fields, gauge, Yang-Mills, the matter sector) and its *current* tier. Three things at once: (1) the **tier catalog**, (2) the **staleness detector** (the `Status` column is current state; any doc disagreeing with a row is by definition stale), (3) the **anti-drift authority** `read-first` checks against.

**How it's built.** Read every paper; tier each claim *from the paper's own audit table / "does NOT claim" / verdict* — never inflated. Seeded from the folder README + `event-density/docs/ED_Research_Targets.md` (#2b), corrected against the papers where they disagree.

**One of a per-folder set.** Companions: `entanglement/…`, `black-hole/…`, `cosmology/…`, `dark-sector/…`, `gravity/…`.

**Tier key.** `Derived` (from primitives, conditioning postulate noted) · `Grounded` (structural/conditional/account-tier) · `Reference` (canonical kernel form) · `Measured` (simulation/probe) · `Selected/Inherited` (a value: Chern numbers, couplings, masses) · `Postulated` · `Asserted` (A→position/analogy) · `Synthesis` · `Open`.

*15 papers. Read 2026-07-29 (extraction agent, then spot-checked).*
*Spot-checked directly against the papers (5, scaled to 15; **no catch** — the extraction was reliable, incl. the subtle round-8 relabels): (1) **023** "does not claim a solution to the Clay problem… strictly below constructive proof" — confirmed verbatim (preamble #1/#7); (2) **021** mass-gap continuum survival "D conditional on P-Profile-Rescaling," numerical Δ OPEN — confirmed (audit rows 14–15); (3) **MS-II §2** SU(N) from channel multiplicity = *derived* (the one firm upgrade over T17's analogy) — confirmed; (4) **MS-II** chirality banner (P-imprint retired: C native, P spontaneous + inherited, γ⁵ global) + EWSB/masses "not derived" — confirmed inline; (5) **017** Klein-Gordon "was D conditional, now P-construction + I" (round-8 relabel) — confirmed (audit rows). The folder does NOT over-claim a Clay proof or a derived Standard Model.*

---

### Derived (from primitives, conditional on the named postulate)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Gauge group `U(N)=SU(N)×U(1)` from channel multiplicity | MS-II §2 (absorbs MS-I §3) | non-abelian `SU(N)` forced by N indistinguishable channels + bandwidth conservation (P04) + invertibility unitarity | SM correspondence `{1,2,3}` and couplings inherited | **Derived — the one firm upgrade over T17's analogy** |
| Continuum gauge-covariant derivative `D_μ=∂_μ+iA_μ` | 016 §3.3 | DCGT coarse-graining + P-Polarity-Connection-Match | groups, couplings, local-gauge invariance all I | Derived, conditional on P-Polarity-Connection-Match (Postulated) |
| Continuum YM equations `D_μF^μν=J^ν` (Euler-Lagrange) | 019 §3.4 | standard variational step *from the postulated action* | action = P (P-YM-Action-Coarse-Graining); `g_YM` value I | Derived (EL step) on a Postulated action |
| Substrate quotient = physical-state space; BRST = coarse-grained quotient | 022 §3 | D-via-I: fiber-bundle quotient + DCGT | constructive Gribov resolution OPEN | D-via-I under P-Gauge-Orbit-Non-Empty + P-Quotient-Hilbert |
| Lindblad/GKSL master-equation form | 024 §3 | FORM-FORCED as the Markovian limit of V5-modulated dynamics (D-via-I) | specific `L_k`, rates I; non-Markovian OPEN | D-via-I under P-Markovian + P-Weak-Coupling + P-Factorized-IC |
| Lorentz covariance of the continuum free-scalar equation | 017 §3.4 | from V1 Lorentz covariance (Paper_089) preserved by DCGT | — | Derived |
| Spectral-gap **form** `Δ ∝ 1/ℓ_*` (Yang-Mills mass gap) | 021 §3.4 | form FORCED given postulates; the new content = substrate adaptation of Perron-Frobenius/Glimm-Jaffe to V1/V5 | coefficient INHERITED (matching); **continuum survival conditional on P-Profile-Rescaling (OPEN)**; numerical Δ OPEN | **Derived (form) / Inherited (coeff) — explicitly NOT a Clay proof** |

### Grounded (structural / conditional / account-tier)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Free scalar Klein-Gordon `(□+m²)φ=0` as the DCGT limit of V1 | 017 §3.3 | **P-construction** matching the standard form (round-8 relabel: was D, now P) under P-Scalar-Match + P-Lorentz-Covariant-Continuum | mass values I; canonical quantization / interacting QFT NOT claimed | **Grounded / postulate-construction** |
| Non-abelian YM potential, field strength, YM equation | 018 §3.3–3.5 | **P-constructions** matching standard forms under P-StructureConstants-Match + I(DCGT) | groups I; mass gap / OS NOT claimed here | Grounded / postulate-construction |
| N1 + GR1: V1 finite-width + 2-point function on a curved acoustic background | 014 §3 | D-via-I: QFCS + Hadamard machinery applied to V1 | curvature corrections I; backreaction / Einstein eq OPEN | Grounded — "FORM-FORCED" under P-Slow-Variation + P-Hadamard-Preservation |
| Substrate is a `U(N)` lattice gauge theory; escapes Nielsen-Ninomiya | MS-II §3 (MS-I §4) | P05-transport = `U(N)` link variable; relational graph (no Brillouin torus) + retarded arrow (non-hermitian) evade the two N-N premises | "P05 re-routes channels unitarily" is a structural reading, not a closed proof | Grounded (structural) |
| Spin-½ from relationality (tethered node carries `SU(2)→SO(3)` double cover) | MS-II §4.1 | orientation-entanglement / Dirac-belt reading | Cl(3,1) + `π₁(SO(3))=ℤ₂` inherited (T2/T4) | Grounded (structural) |
| Parity violation is a non-abelian phenomenon; **no parity-violating abelian force** | MS-II §5, MS-I §5 | V1 single-channel chirality-blind → abelian vector; V5 cross-channel chirality-sensitive → non-abelian can be chiral | *which* force is chiral (weak assignment) OPEN/inherited | Grounded (account) + a falsifiable prediction |
| Chirality `γ⁵` = the arrow's "screw" | MS-II §4.2 | handed-commitment twist as the chirality locus | evidence is a **1+1D toy-lattice** computation, NOT canonical V1; `γ⁵` relocated to **global** (`=iγ⁰γ¹γ²γ³`); 3 open bridges to a relativistic result | Grounded (account); corrected inline (2026-07-05, 2026-07-10) |
| `{1,2,3} ⟺` internal amplitude dimension `d=3` (Welch-bound stability); no stable `SU(N≥4)` | MS-II §6 | max mutually-orthogonal channels in `ℂ^d` is `N=d` | *why* `d=3` is itself OPEN | Grounded (structural) + a falsifiable prediction |
| Three spatial dimensions because the arrow must hold committed order (a link survives only in 3D) | MS-II §7 | topological elimination (link holds in 3D, frozen in 2D, unravels in 4D) | conditional on the OPEN premise that ED holds order by spatial linking | Grounded (structural); the topology half is Measured |
| V1 QFT-arc propagator (Källén-Lehmann retarded form) | 013 §3 | D-via-I: KL machinery applied to P-V1-Spectral + P11 retardation | `ρ(m²)` values I; multi-point functions OPEN | Grounded / Reference-adjacent |

### Reference (canonical kernel form)
| Claim | Paper | Note | Status |
|---|---|---|---|
| V1 finite-width retarded vacuum kernel, QFT-arc presentation | 013 | two-point / Wightman / propagator presentation of the canonical V1 (Paper_089); adds no new primitive | Reference — scaffolding for 014–023 |

### Measured (simulation / probe)
| Claim | Paper | What's measured | Status |
|---|---|---|---|
| Linking held in 3D, erasable in 4D | MS-II §7 | `linking_3d_vs_4d_probe`: unlinking forces a collision (min dist 0.000) in 3D, slides free (0.600) in 4D | Measured (the ED-holds-order-by-linking premise still OPEN) |
| Retarded ("arrow") hopping produces net chirality signatures | MS-II §4.2 | 1+1D toy: point-gap winding, skin effect, spectral flow — all zero in the Hermitian control | Measured (toy) — supports the §4.2 account only, not yet Lorentz-covariantized |

### Selected / inherited (a value taken from measurement)
| Item | Paper | Status |
|---|---|---|
| Integer-Chern quantization `C_n∈ℤ` of photonic Hall drift | 015.5 | quantization INHERITED from standard Chern-class topology; ED supplies only the rule-type-bundle identification (form-IDENTIFIED, M3) |
| Specific Chern numbers per platform/band | 015.5 | INHERITED (topological band-structure analysis) |
| Empirical gauge groups `SU(3)×SU(2)×U(1)`, couplings, masses, mixings | 015–019 | INHERITED (value-layer matching) across the whole arc |
| `g_YM`, mass-gap coefficient, Lindblad `L_k` & rates | 019/021/024 | INHERITED (empirical matching) |

### Postulated (paper-specific, load-bearing)
| Postulate(s) | Paper |
|---|---|
| P-V1-Spectral, P-V1-FormFactor | 013 |
| P-Slow-Variation, P-Hadamard-Preservation | 014 |
| P-Scalar-Match, P-Lorentz-Covariant-Continuum | 017 |
| P-Bundle-Definition, **P-NonAbelian-Analogy** | 015 |
| P-Substrate-Covariant-Derivative-Construction, P-Polarity-Connection-Match | 016 |
| P-MultiRT-Compose, P-MultiRT-NonCommute, P-StructureConstants-Match | 018 |
| P-YM-Action-Coarse-Graining | 019 |
| P-OS-Reflection-Positivity, P-OS-Reflection-Symmetry (OS3, the one non-inheritable axiom) | 020 |
| P-Gap-Coercivity, **P-Profile-Rescaling**, P-Quartic-Sign | 021 |
| P-Gauge-Orbit-Non-Empty, P-Quotient-Hilbert | 022 |
| P-Markovian, P-Weak-Coupling, P-Factorized-IC | 024 |

### Asserted (A→position / A→analogy)
| Claim | Paper | Status |
|---|---|---|
| Non-abelian structure from multi-rule-type composition ("by analogy") | 015 §6 | **A→analogy** — superseded/upgraded to Derived by MS-II §2 (Staleness #2) |
| Verdict M3 for photonic-Chern substrate identification | 015.5 | A→position |
| YM-regime applicability (sub-Planckian kinematic) | 019 | A→regime |
| OS composite verdict "structural-positive-conditional" | 020 | A→position |
| Gribov ambiguity is a coarse-graining artifact (not constructively resolved) | 022 | A→position |
| "Arc architecturally cleaner than the NS arc" | 023 | A→position |

### Synthesis
| Claim | Paper | Status |
|---|---|---|
| Yang-Mills arc closes at "Clay-relevance / structural-positive level" | 023 | **Synthesis** — explicitly **above structural analogy, below constructive proof**; **NOT a Clay-prize-eligible proof** (preamble #1, #7) |

### Open (declared)
| Item | Paper(s) |
|---|---|
| YM continuum-measure existence; OS3 derivation; mass-gap survival as `a→0` (P-Profile-Rescaling underived) — the three explicit Clay-hard gaps | 019/020/021/023 |
| Confinement, asymptotic freedom, glueball spectrum, numerical Δ | 021/023 |
| Constructive Gribov resolution | 022 |
| Why `{1,2,3}` / why internal `d=3`; the weak force's specific chirality; **anomaly cancellation**; the ED-holds-order-by-linking premise | MS-I/MS-II |
| Full channel-topology → representation spectrum; spinor construction (**reduces to the T4 spinor gate, #2b**) | MS-II §4, §8 |
| Backreaction / substrate Einstein equation; V1 multi-point functions; non-Markovian corrections | 014/013/024 |
| Yang-Mills action (`∝F²`), electroweak/Higgs sector, **EWSB, fermion masses — NOT derived** | MS-I §7.3, MS-II §1 |

### Staleness & README-refinements
1. **MS-I §6 retired-P-imprint account — FIXED 2026-07-29.** MS-I §6's chirality account had "the first commitment imprints **both** a C reference **and** a P reference" — exactly the **P-imprint retired 2026-07-10** (ED natively selects C but NOT a native P; parity violation is necessarily spontaneous; *which* force is chiral is inherited via SU(2) pseudoreality; γ⁵ is global). MS-II carries this inline; MS-I had only the supersede-by-MS-II pointer. **An inline correction banner is now added at MS-I §6.** *(Minor residue: MS-II §5 body prose still contains the old "imprints both… a parity reference (P-type)" wording, but the MS-II top banner + §4.2 note govern it — left as-is.)*
2. **YM-arc non-abelian framing is stale relative to MS-II — PARTIALLY FIXED 2026-07-29.** 015 (P-NonAbelian-Analogy = A→analogy) and 018 (postulates), both May 2026, rest non-abelian gauge structure on postulate/analogy; **MS-II §2 (June 2026) *derives* SU(N)** from channel multiplicity. Tier-by-what's-true-now: non-abelian gauge structure is **Derived** (MS-II), not A→analogy (015). **A forward pointer was added to Paper_015 §6** (below); **Paper_018 still lacks one** (a candidate remaining fix — same one-line pattern).
3. **Paper_015 (T17) one-directional supersede link — FIXED 2026-07-29.** 015 §6 presented non-abelian "by analogy" with no forward pointer to MS-I/MS-II. **A forward-pointer banner is now added at 015 §6** (pointing to MS-I §3 / MS-II §2's SU(N)-from-multiplicity derivation).
4. **Wolfram/Ruliad in Paper_015.5** (preamble item 2 + §6 Position Statement) — the only Wolfram citation in the folder. Violates the no-Wolfram-in-public rule. **AP's standing call: leave it.** Record-only.
5. **MS-II §4.2 chirality evidence is a 1+1D toy** (not canonical V1; γ⁵ relocated per-channel→global) — **flagged inline** in MS-II (so NOT stale); noted only to confirm the tier is *account with open bridges*, not derived.
6. **Archived-source over-claim check: CLEAN.** Neither MS-I nor MS-II invokes "four-band," dwell-mass, or EWSB-as-derived; both explicitly defer the electroweak/Higgs sector, EWSB, and fermion masses to OPEN. 017 explicitly inherits mass values. No paper in the folder leans on the archived M-series four-band structure. *(This reconciles the memory `project_substrate_higgs_emergence` concern — that was about the archived 087-era dwell-mass, not MS-I/MS-II.)*
7. **Paper_024 / anomaly note: consistent.** 024 derives only the Lindblad form and makes **no** anomaly/non-Hermiticity claim — consistent with the memory note that Lindblad is the "wrong type" (line-gap, not point-gap) for the anomaly question.

### Honest arc-state
The qft folder is honest and **does not over-claim** — critically, the Yang-Mills arc does **not** claim a Clay-grade mass-gap proof. The QFT foundations (013/014/017) present V1 and free-scalar QFT as DCGT coarse-graining reconstructions that reproduce standard QFT *by construction* through ~7–9 declared naming/construction postulates; even the Klein-Gordon "derivation" (017) is, by the paper's own round-8 audit, a **P-construction**, not a clean D. The gauge line (015/016/018) is likewise a substrate-vocabulary relabel resting on naming postulates, and its one genuine derivation-upgrade — **SU(N) from channel multiplicity** — lives not in T17 but in the later **MS-II §2**, which supersedes T17's analogy. The Yang-Mills arc (019–023), the delicate one, lands exactly where it should: **"Clay-relevance at structural-positive level," strictly below constructive proof.** The mass-gap *form* `Δ∝1/ℓ_*` is FORCED given postulates (021), but continuum survival hinges on the declared, underived **P-Profile-Rescaling** (the Clay-hard wall, OPEN), OS3 is a declared postulate (020), and the continuum measure is never constructed (023 names all three gaps and states the arc "does not close" them). The matter sector (MS-I→MS-II) is the program's frontier and is scrupulously tiered: gauge-group-from-multiplicity is *derived*; the lattice-gauge form, spinor assembly (spin-½ from relationality), the `{1,2,3}⟺d=3` reduction, and the 3-dimensions argument are *structural*; chirality-from-the-arrow is an *account* whose P-imprint half has since been **retired** (C native, P spontaneous + inherited). The Standard-Model completion — `{1,2,3}` uniqueness, the weak force's specific chirality, and **anomaly cancellation** — is explicitly OPEN and reduces to the **T4 spinor gate (#2b)**, the highest-leverage open item in the program. **Defensible headline:** *QFT and gauge structure are reproduced by DCGT coarse-graining on a naming/construction postulate stack (even KG is a P-construction); the one firm new derivation is SU(N) from channel multiplicity; the Yang-Mills arc is honest Clay-relevance strictly below proof (continuum survival = the open wall); and the Standard-Model completion is the program's named open frontier (#2b via T4), not a closed result.*
