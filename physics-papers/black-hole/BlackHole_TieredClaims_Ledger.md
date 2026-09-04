# Black-Hole Arc — Tiered-Claims Ledger

**What this is.** This doc records **every load-bearing claim in the black-hole folder and its *current* tier** — derived, grounded, inherited, postulated, asserted, open, superseded, or prediction. It is three things at once:

1. **The tier catalog** — what this arc actually claims, at what strength, and what each claim inherits or leaves open.
2. **The staleness detector** — the `Status` column carries the current state, so *any paper (or the README) whose text disagrees with a row here is, by definition, stale*. You hold this ledger up against each doc; you don't hunt for stale separately.
3. **The anti-drift authority** — the single source of truth `read-first` checks against, so a corrected result doesn't have to be re-discovered from the papers each time.

**How it's built.** Read every paper; extract its load-bearing claims; tier each one *using the paper's own audit table / "what this does NOT claim" / verdict* — never inflated. Seeded from the folder README + `event-density/docs/ED_Research_Targets.md`, then corrected against the papers where they disagree (the read decides; the ledger records the winner, and the disagreement becomes a staleness note).

**One of a per-folder set.** Each corpus folder gets its own tiered-claims ledger in this format; this is the black-hole folder's. Companion: `physics-papers/entanglement/Entanglement_TieredClaims_Ledger.md`.

**Tier key.** `Derived` (forced from primitives) · `D-via-I / Form-forced` (form forced, resting on named postulate(s), numbers inherited) · `Measured` (from simulation) · `Selected/Inherited` (standard value/math, not substrate-derived) · `Postulated` (rests on a named paper-specific postulate) · `Asserted` (an audit A→position/A→assertion row: stated, not proven) · `Synthesis` (arc consolidation) · `Prediction` · `Open` · `Superseded/Relocated`.

*Papers 039–052 all dated 2026-05-13; HorizonTilingThreeCounts, 044.5, 047.5, 052.5 are July 2026; `Paper_BH_Thermal2Pi_EntropyCoefficient` ported into the folder 2026-07-29. Read 2026-07-29.*
*Spot-checked directly against the papers (7, scaled to 18-paper folder; **escalated** after a fabricated-quote catch): (1) 043's 1/4 = INHERITED via log-g — confirmed (title, audit rows 9–10, §4, conclusion); (2) the README headline "S=A/4 fully structural, both ED-derived" — confirmed a real tension, now resolved by the import (Staleness #1); (3) 051's capstone "paradox not generated / info not lost" = A→position on P-Substrate-Unitarity — confirmed verbatim (audit rows 9–10); (4) 052.5 merger-lag = PROVISIONAL/M2, zero D rows — confirmed (audit row 14); (5) HorizonTiling "one fact, not novel" — confirmed, but the extractor's claim that its "§4 supersedes 043" is a **fabricated quote** (the word "superseded" is absent; corrected in Staleness #1). **Escalation (catch was a fabricated quote → verify more quotes):** (6) 039 §3.2 "r_H not derived, used as coarse-grained identification point" — confirmed verbatim (lines 100–104); (7) 044.5 greybody "INHERITED from Regge-Wheeler 1957 / Zerilli / Page, NOT a new derivation" — confirmed verbatim (preamble 4–5). The fabrication was isolated to that one HorizonTiling claim; all other quoted claims hold. `Paper_BH_Thermal2Pi` read in full before import.*

---

### D-via-I / Form-forced (form derived, *conditional on the named postulate(s)*; numbers inherited)
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| Horizon = `b→0` decoupling surface (Γ_cross collapse) | 039 | **D** mechanism | `r_H` location + κ **INHERITED from GR** (§3.2 honest-acknowledgment: r_H a coarse-grained reference, not derived) | current |
| Hawking temperature `T_H = κ/2π` via V5 KMS | 047 | KMS ⟹ thermal = **D** | κ **I**; Euclidean/conical **2π = I-via-DCGT** (audit rows 5–8, "not substrate-derived") | current — see Staleness #2 on the "2π derived" claim |
| Non-thermal Hawking correction `[1−c₁(ω/ωc)²]` | 047 | **D** form | conditional on **P-V5-Even**; ωc "chosen to match," c₁ inherited | current |
| Trans-Planckian resolution (modes terminate at ωc) | 040 | **D-via-I** | conditional on **P-V5-UV-Cutoff + P-Cutoff-Saturation** | current |
| No-singularity (`C_cum` bounded, r ≥ ℓ_P) | 042 | **D-via-I** | conditional on **P-Bandwidth-Boundedness + P-Substrate-Interior-Cutoff**; interior OPEN | current — see Staleness #3 (abstract's "P04-derived" is really postulated) |
| Planck-mass remnant `M⋆ = c⋆ℓ_P` (Scenario C) | 041 | **D-via-I** | conditional on **P-Cutoff-Saturation-Endpoint + P-Remnant-Stability + 048**; c⋆ inherited | current |
| Scenario C forced (A, B excluded) | 048 | **D-via-I** | conditional on **P-Resummation-Convergence + P-Endpoint-Truncation**; coefficients inherited | current |
| Area-law **form** `S ∝ A` | 043 | **D-via-I** | conditional on **P-Horizon-Participation + P-Multiplicity-g**; coefficient inherited by this route | current (the **form**; the coefficient has a separate geometric route — next row) |
| Bekenstein–Hawking **coefficient 1/4** (`T = κ/2π`, `S = A/4`), geometric route | `BH_Thermal2Pi` (imported) | **Derived** — both factors ED-structural: `½` from `κ = 1/(2r_s)` (b-profile slope, GR-III), `2π` from the near-horizon **Rindler** shape via smoothness (numerically confirmed) | tool = **Euclidean continuation** (Wick rotation), *the same route GR uses* — so ED is on par with GR, not beyond it; b-profile + κ inherited from GR-III | current — **the in-folder derived route for the 1/4**; arrow-native (continuation-free) version OPEN (§4b honest negative) |
| Page-curve rise + turnover + decline | 050 | **D** | conditional on **P-V5-EntBudget + P-Re-routing**; t_Page ≈ 0.54τ_BH inherited; unitarity OPEN | current |
| PBH relic abundance `Ω⋆ ∝ n_PBH·M⋆` | 049 | **D-via-I** | conditional on **P-One-Remnant-Per-PBH** | current |
| BHPT scattering / Regge-Wheeler form | 044 | **form-forced** | conditional on P-Horizon-Ingoing-Only + P-Asymptotic-Outgoing; cross-sections inherited | current |
| Kerr twist `g_tφ` | 046 | **form-forced** | conditional on P-Substrate-Vorticity + P-Twist-Coarse-Graining; `a` inherited; interior OPEN | current |
| Helicity preserved (Schwarzschild) / amplified (Kerr) | 045 | **form-forced** | conditional on P-Helicity-Channel + P-Kerr-Helicity-Coupling; superradiance OPEN | current |

### Measured (simulation)
| Claim | Paper | What's measured | Inherited / open | Status |
|---|---|---|---|---|
| Horizon tiles ~1 bit/Planck cell (3 counts: holographic = 1, frozen-state ≈ 0.78, straddling-edge ≈ 0.88) | HorizonTiling | measured convergence | **2 of 3 counts assume the emergent geometry** (curvature emergence OPEN); scale ℓ_V5~ℓ_P inherited (Paper_090) | current — explicitly framed as consilience, "**not a novel prediction, and not tiered as one**" |

### Selected / inherited (standard value or math, not ED-derived)
| Item | Paper | Inherited | Status |
|---|---|---|---|
| κ, BH mass/geometry | 039, 047 | standard GR | current |
| Bekenstein–Hawking **1/4** coefficient, *combinatorial* route | 043 | **I** — via log-g matching (`log g = π`); "matching, not derivation" (§4, conclusion) | current — this *route* inherits; but the folder now also has the **geometric derived route** (`BH_Thermal2Pi`, D-via-I table). Net folder status of the 1/4: **DERIVED** (geometric), with an arrow-native residual |
| Universal `T = κ/2π` for all 4 horizon types | 047.5 | **I** — "INHERITED from standard semi-classical GR"; genuine ED content = V5-saturation common-horizon identification only | current |
| Greybody factors Γ_ℓs | 044.5 | **I** — "NOT a new derivation… INHERITED from Regge-Wheeler 1957 / Zerilli / Page" | current |
| t_Page ≈ 0.54τ_BH; c₁, ωc, c⋆ | 050, 047, 041 | **I** | current |

### Postulated (load-bearing paper-specific postulates — 20+ across the folder)
| Paper | Postulates |
|---|---|
| 040 | P-V5-UV-Cutoff, P-Cutoff-Saturation |
| 041 | P-Cutoff-Saturation-Endpoint, P-Remnant-Stability |
| 042 | P-Bandwidth-Boundedness, P-Substrate-Interior-Cutoff |
| 043 | P-Horizon-Participation, P-Multiplicity-g |
| 044 | P-Horizon-Ingoing-Only, P-Asymptotic-Outgoing |
| 046 | P-Substrate-Vorticity, P-Twist-Coarse-Graining |
| 047 | P-V5-Even |
| 048 | P-Resummation-Convergence, P-Endpoint-Truncation |
| 049 | P-One-Remnant-Per-PBH |
| 050 | P-V5-EntBudget, P-Re-routing |
| 051 | **P-Ledger-Completeness, P-Substrate-Unitarity** (a *postulated* unitarity — the capstone's load-bearing input) |

### Asserted (audit A→position / A→assertion — stated, not proven)
| Claim | Paper | Note | Status |
|---|---|---|---|
| **"Paradox not generated" + "information not lost"** | 051 | **A→position** (audit rows 9–10); rests on P-Substrate-Unitarity; "**structural ledger, not constructive proof**" (§3.5, conclusion) | current — **the arc's load-bearing soft spot** |
| "Classical singularity is a coarse-graining artifact" | 042 | A→position | current |
| "Remnants NOT a DM candidate" | 041 / 049 | A→position | current |
| "Four-horizon structural identification" | 047.5 | A→position; temperature fully inherited | current |
| "Leading-order match is identification, not derivation" | 044.5 | A→position; greybody factors inherited | current |

### Prediction (provisional, not refutation-grade)
| Claim | Paper | Note | Status |
|---|---|---|---|
| Merger-lag (existence of a delay) | 052.5 | **PROVISIONAL / M2 (Intermediate Path C)**, existence-only; τ_V5 floor **OPEN**; numerics inherited; audit has **zero D rows** (all D-via-I; row 14 A→position); "**NOT refutation-grade in the BTFR sense**." **Confirms** 22-Ways P2. | current — do not upgrade to refutation-grade until a substrate τ_V5 floor is supplied |

### Synthesis
| Claim | Paper | Note | Status |
|---|---|---|---|
| Paradox synthesis (integrates 039 + 047 + 050 + 041) | 052 | arc consolidation | current |
| Cross-class horizon identification (M3) | 047.5 | genuine ED content = the V5-saturation mechanism only | current |

### Open
| Item | Papers | Status |
|---|---|---|
| Full **unitarity** (constructive, not postulated) | 050 / 051 | **OPEN** — target #4; 051 assumes it (P-Substrate-Unitarity) |
| Substrate BH **interior** for r < ℓ_P | 042 / 046 | OPEN |
| **Superradiance** | 045 | OPEN |
| Substrate-anchored **τ_V5 floor** (merger-lag) | 052.5 | OPEN |
| Substrate derivation of **log g** | 043 | OPEN |
| **Curvature emergence** underneath every geometric count | HorizonTiling, 046 | OPEN — the bridge under 2-of-3 tiling counts + the Kerr geometry |
| Arrow-native (continuation-free) **2π** | `Paper_BH_Thermal2Pi` §4b (now in-folder) | OPEN — the derived-2π route is Euclidean (reversible-time), on par with GR; an arrow-native 2π from raw commitment statistics is not yet supplied (§4b honest negative; possibly a category error — the 2π may be an intrinsically continuum feature) |

### Staleness & README-refinements
1. **The 1/4, honestly — RESOLVED 2026-07-29 by importing the derived route.** Two routes to the coefficient now both live in the folder: (a) Paper_043's *combinatorial* `log g = π` matching, which **inherits** the 1/4 ("matching, not derivation," §4); and (b) the *geometric* route in **`Paper_BH_Thermal2Pi_EntropyCoefficient`** (ported 2026-07-29 from the foundations working note), which **derives** both factors — `½` from `κ = 1/(2r_s)` and the `2π` from the near-horizon Rindler shape via smoothness. So the **net folder status of the 1/4 is DERIVED** (geometric route). The honest caveat, stated in that paper's §4 and §4b: the `2π` comes via the **Euclidean continuation** — the same tool GR uses, so ED is *on par with* GR, not beyond it — and the arrow-native, continuation-free derivation from raw commitment statistics remains OPEN (§4b is an honest negative; it may even be a category error, since the `2π` looks like a continuum feature). **This retires the earlier README-vs-043 tension:** the README headline ("`S = A/4` now fully structural… both ED-derived") is now **defensible**, provided the arrow-native residual is stated. *Correction to the extraction pass, retained for provenance:* it attributed a direct quote to "HorizonTiling §4" saying 043 is "superseded"; the word "superseded" appears nowhere in HorizonTiling — that paper says only that the 1/4 is derived *separately* and concerns the *tiling*, not the coefficient. (Before the import, the derived memo sat in `event-density/foundations/`, with a stale 2026-07-01 copy also in `relocated_from_EDG_2026-07-09/`; the imported EDG paper is the current one.)
2. **047's 2π is inherited in-paper.** 047's own audit inherits the 2π (I-via-DCGT, standard Euclidean geometry). The "2π structural / ED-derived" claim lives only in the relocated `BH_Thermal2Pi` memo, and even there via the Euclidean (reversible-time) route. README "both ED-derived" is mildly optimistic for the same reason as #1.
3. **042's cap: "P04-derived" (abstract) vs postulated (audit).** 042 calls `C_max ~ r³/ℓ_P³` "P04-derived," but the 2026-07-24 `FiniteGrain_Singularity_Lemma` found the density cap is **not** bottom-up from the certified rule (it needs the *extended* P04 rule; the `b→0` horizon is a *nonlocal potential* horizon, not a *local* density ceiling; the ρ_max derivation **FAILED**). 042's bound is really **postulated** (P-Bandwidth-Boundedness) — consistent with its own audit, not with the abstract's phrasing.
4. **Stale cross-ref: 043 cites Paper_067 (von Neumann).** 043's composition line (`Paper_025 + 039 + 067 + postulates`, conclusion line 125) cites **067, superseded by 068 on 2026-07-05** — should read 068. (Same stale ref found in the entanglement folder.)
5. **README coarse tiers hide postulate/assertion reality (confirmed pattern).** README "041/042 Grounded/Derived" hides two postulates + A→position each; "050 Grounded" hides P-V5-EntBudget + P-Re-routing + t_Page inherited; "051 Grounded" hides that the whole "paradox not generated" is **A→position on a *postulated* unitarity**; "044.5 / 047.5 Grounded (M3)" hides that these are pure identification/consilience with temperature + greybody factors fully inherited (no D rows).
6. **"1/4 three counts" = one fact, not three independent confirmations — confirmed.** HorizonTiling preamble 3 + §5: "three routes landing on the same number… consilience, not a novel prediction." Matches the "grain fixes G three ways = one fact" discipline. (And 2 of the 3 counts assume the emergent geometry.)
7. **Public-material Wolfram violation.** 044.5, 047.5, and 052.5 cite the "'t Hooft cellular-automaton, **Wolfram Ruliad**, causal-set" lineage. Memory rule: drop Wolfram/Ruliad from public material. These are peer-facing EDG papers → to fix (record-only here; 't Hooft / causal-sets are the safe peers to keep).

### Honest arc-state (corrects README line 6 / "delivered")
**The BH / information-paradox arc is form-complete but not "closed" in the strong sense the README headline implies.** Every standard horizon result — decoupling surface, trans-Planckian cutoff, no-singularity, Planck remnant, area-law *form*, `T_H = κ/2π`, greybody, Page curve — has a substrate reading, but each is **form-forced conditional on ~20 paper-specific postulates** (heavily P-V5-* and cutoff/endpoint), with **κ, the geometry, greybody factors, c⋆, and t_Page INHERITED** (the **1/4 coefficient is now geometrically DERIVED** in-folder via `Paper_BH_Thermal2Pi`, modulo an arrow-native-2π residual), and the two capstones (051 "paradox not generated," 052 synthesis) resting on an **A→position ledger + a *postulated* substrate unitarity**, not a constructive proof. The genuine ED contributions are narrower than the folder's breadth suggests: the `b→0` decoupling mechanism, the V5-KMS route to the temperature *form*, the V5-saturation common-horizon identification, and the *measured* area-law tiling. **Real open frontier:** full (constructive) unitarity (target #4), the substrate BH interior (r < ℓ_P), a derived τ_V5 floor (merger-lag), the arrow-native 2π, and — underneath all the geometric counts — curvature emergence. **Defensible headline:** *the black-hole thermodynamics formalism is reproduced form-forced / value-inherited on a large postulate stack, with the information-paradox "resolution" a structural audit conditional on postulated substrate unitarity — coherent, but neither a closed derivation nor a delivered unitarity proof.*

---

## Addendum 2026-09-04 — `Paper_039` §4.1 predates its own derivation

Found while checking the black-hole arc for an independent instance of the Hawking `2π` (gravity ledger Staleness #10, `gravity/Note_a0_TwoPi_RepairRoutes.md` §4c).

**`Paper_039_HorizonDecoupling` §4.1 (2026-05-13) assumes `β_H = 2π/κ`** — it states that V5 acquires imaginary-time periodicity with that period, then reads `T_H = κ/(2π)` off it. That was the correct posture when written: the `2π` was inherited corpus-wide at the time.

**`Paper_BH_Thermal2Pi_EntropyCoefficient` (2026-07-29) now derives it**, from ED's own near-horizon Rindler `b`-profile plus the no-conical-defect smoothness condition. Paper_039 carries no forward pointer, so a reader arriving at §4.1 meets an assumption where the corpus has a result. **Chronology, not error** — same class as gravity Staleness #4 and #6. *Fix: one forward-pointer sentence in §4.1. No tier changes; the identification of the V5 kernel as the object that acquires the periodicity is Paper_039's own contribution and is unaffected.*

**Recorded negative from the same check.** `Paper_047_5` rules itself out explicitly (preamble item 4: the Hawking-Unruh formula is INHERITED, not derived). `Paper_040`'s `T_H/ω_c` comparison is an order-of-magnitude suppression with O(1) factors dropped, so it cannot bear on a question about a factor of `2π`. **The black-hole arc contains no independent derivation of the thermal `2π` other than `Paper_BH_Thermal2Pi`'s.**
