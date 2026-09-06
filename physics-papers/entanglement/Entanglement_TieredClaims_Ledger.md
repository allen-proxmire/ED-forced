# Entanglement Arc — Tiered-Claims Ledger

**What this is.** This doc records **every load-bearing claim in the entanglement folder and its *current* tier** — derived, grounded, postulated, asserted, inherited, open, or superseded. It is three things at once:

1. **The tier catalog** — what this arc actually claims, at what strength, and what each claim inherits or leaves open.
2. **The staleness detector** — the `Status` column carries the current state, so *any paper (or the README) whose text disagrees with a row here is, by definition, stale*. You don't hunt for stale separately; this ledger is the ruler you hold up against each doc.
3. **The anti-drift authority** — the single source of truth that `read-first` checks against, so a corrected result doesn't have to be re-discovered from the papers each time.

**How it's built.** Read every paper; extract its load-bearing claims; tier each one *using the paper's own audit table / "what this does NOT claim" / verdict* — never inflated. Seeded from the folder README and `event-density/docs/ED_Research_Targets.md`, then corrected against the papers where they disagree (the read decides; the ledger records the winner, and the disagreement becomes a staleness note). A proportion of the tiers is **spot-checked directly against the papers** (not taken on the extractor's word), the sample scaled to the number of claims.

**One of a per-folder set.** Each corpus folder gets its own tiered-claims ledger in this format; this is the entanglement folder's. *(Pilot — this doc validated the format.)*

**Tier key.** `Derived` (forced from primitives) · `Grounded` (conditional/structural, given a stated input) · `Selected/Inherited` (standard math or a measured value, not substrate-derived) · `Postulated` (rests on a named paper-specific postulate) · `Asserted` (an audit A-row: stated, not proven) · `Synthesis` (arc consolidation) · `Open` · `Superseded/Retracted`.

*Papers 063–072, all dated 2026-05-13. Read 2026-07-28. Spot-checked: 063 tiers and the 069↔Gleason-keystone Solèr residual, verified directly against the papers.*

---

### Derived (forced — but each conditional on a postulate in the Postulated table) — workbook tier: PER ROW (see rule below)

> **Transcription rule — `ED_ItemizedTheory_TieredClaims*.xlsx`.** That workbook's `Derived` tier is **narrower than this heading**: *“forced/proven from the 13 primitives (+ standard math) with **NO** paper-specific postulate.”* **This section is mixed, so take the tier from the ROW, never from this heading.** If a row's *“Inherited / open”* cell names a `P-` postulate, or says *conditional on* / *rests on*, its workbook tier is **`Grounded`** — or **`Postulated`** where the postulate carries the claim — **not `Derived`**. *(Here: **4 of 5** rows currently name a postulate.)* **Losing this qualifier in transcription over-promoted ten rows before 2026-09-06**, because the caveat lived in a parenthetical and parentheticals do not travel. See `gravity/Gravity_TieredClaims_Ledger.md` #122 and #124.

| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| No-signaling `p(a\|x,y)=p(a\|x)`, over-determined by 3 locks | 066 | Lock L1 (marginal independence) = **D-via-I** from tensor-product + POVM completeness | L2 rests on P-Substrate-Causality; L3 = Paper_073; "3-locks ⟹ over-determination" is an A→position | **current** — the cleanest paper in the arc; but Bell-Tsirelson is explicitly *open* here (row 11) |
| Schmidt rank > 1 ⟹ non-factorizable | 064 §3.3 | **D** (standard SVD applied) | conditional on **P-V5-Schmidt-Generic** | current — strengthens 063's irreducibility *only under* that postulate |
| Monogamy: **total pairwise entanglement capped by the chain's V5 budget** | 065 §3.3 | **form D** (form-forced) from V5 finite budget + P04 additivity | conditional on **P-V5-Budget + P-Measure-Saturation**; `W_max` inherited |
| Monogamy in **CKW form** | 065 §3.3 | **Grounded — consistent with, not forced by** *(re-tiered 2026-09-04, was form D)* | the budget gives a *constant* bound, CKW's is *state-dependent*; general measure-saturation would close the gap but yields **equality**, losing the strict inequality and the residual three-tangle. Open item **O-SubAdd** (065 §6.x) | current |
| von Neumann entropy form `S = −Tr ρ log ρ` | 068 §3 | **D-via-I** (Shannon-Khinchin + Khinchin uniqueness) | conditional on **P-Continuity + P-Additivity + P-Maximality**; normalization inherited | current — two substrate-derivations open (see Open) |

### Grounded / conditional
| Claim | Paper | What's derived | Inherited / open | Status |
|---|---|---|---|---|
| E-2 bilocal cross-chain term `Δ_KL` exists | 063 | D **conditional on V5** (Paper_090) | — | current |

### Selected / inherited (standard math or measured value)
| Claim | Paper | | Inherited | Status |
|---|---|---|---|---|
| The Schmidt decomposition *form* | 064 | — | **I** — SVD is standard math (round-7 relabel: was "D conditional on SVD", now I) | current |
| Tsirelson bound `2√2` | 069 | — | **I** — "not derived from first principles… INHERITED" (preamble 1) | current |
| Bell ⊊ Tsirelson ⊊ NS nesting; PR-box exclusion | 069 | D-via-I (form composition) | *entirely* conditional on **P-V5-Hilbert-Constraint** | current — inherits a Solèr residual (see Staleness) |
| `k_B` / log-base normalization; concrete entropy values | 068 | — | **I** | current |

### Postulated (rests on a named paper-specific postulate)
| Claim | Paper | Postulate | Status |
|---|---|---|---|
| E-1 factorizable `Ψ^AB = Ψ^A ⊗ Ψ^B` & the tensor-product structure | 063 | **P-Bipartite-Mapping** — "part of this postulate's definitional commitment, not a separate derivation" | current |
| V5-bilocal has Schmidt rank > 1 generically | 064 | **P-V5-Schmidt-Generic** — derivability from the V5 envelope alone is *open* | current |
| ED sits at Tsirelson; PR-boxes excluded | 069 | **P-V5-Hilbert-Constraint** | current |
| Monogamy budget cap; measure saturates the budget | 065 | **P-V5-Budget, P-Measure-Saturation** | current |

### Asserted (audit A-row — stated, not proven)
| Claim | Paper | Note | Status |
|---|---|---|---|
| **E-2 non-factorizability is *irreducible*** | 063 §3.3 | **A→assertion** — "does not supply an explicit irreducibility proof" (round-5: was D, now A) | current — **the arc's load-bearing soft spot** |
| ER=EPR-class echo | 071 | **A→position** — "does NOT derive ER=EPR constructively"; rests on P-V5-Shared-EntanglementGravity | current |
| Entanglement = unresolved individuation regime (not action-at-a-distance) | 072 | **A→position** — interpretive framing, does not modify QM predictions | current |

### Synthesis
| Claim | Paper | Note | Status |
|---|---|---|---|
| Bipartite architecture as one phenomenon | 070 | A→position — "does not override or strengthen constituent verdicts" | current (consolidation) |

### Superseded / open
| Item | Paper | Status |
|---|---|---|
| von Neumann E-6 (duplicate) | 067 | **SUPERSEDED by 068** (merged 2026-07-05); kept for provenance ✓ README correct |
| O-vN-1: derive P-Additivity from P04 (quantitative) | 068 | **OPEN** |
| O-vN-2: derive P-Maximality from P11 | 068 | **OPEN — "structurally blocked; ED has no substrate-level temperature"** |
| derivability of P-V5-Schmidt-Generic | 064 §4 | **OPEN** |

### Staleness & README-refinements
- **The README's per-paper tiers are coarse and hide postulate/assertion reality** (the main finding): 063 "Grounded/Derived" hides P-Bipartite-Mapping (postulate) + irreducibility A→assertion; 064 hides Schmidt-form-inherited + P-V5-Schmidt-Generic; 068 hides three postulates + two OPEN derivations; 069 "Grounded" hides total dependence on P-V5-Hilbert-Constraint + inherited value; 071/072 "Grounded" understate — both are explicitly A→position.
- **Concrete fixable stale reference:** `065 §2.2` cites *"I-E-6: von Neumann entropy (Paper_067)"* → should be **068** (067 superseded 2026-07-05).
- **Tsirelson "retracted" (memory) — clarified, not a hit on 069:** the retraction is a *different* artifact (`Paper_V5AttractiveSign`, characterizing V5 via Tsirelson's theorem). Paper_069's polytope reconstruction **stands** — but its load-bearing P-V5-Hilbert-Constraint posits the very Hilbert inner-product the **July Gleason keystone** reconstructs only at account-tier with a **Solèr residual**, so 069 is not fully "closed"; it inherits that residual.
- **Arc-anchoring soft spot:** 063's irreducibility is an A→assertion; 064 upgrades it to a theorem *only under* P-V5-Schmidt-Generic (a postulate). So "entanglement = irreducible non-factorizability" — the claim the whole arc rests on — is never derived from primitives; it is postulate-to-postulate.

### Honest arc-state (corrects README line 8)
**"CLOSED, no open frontier" is an overstatement.** The arc is *form-complete and internally coherent* — every standard entanglement structure (tensor product, Schmidt, monogamy, no-signaling, vN entropy, Bell-Tsirelson, ER=EPR echo) has a substrate reading, and no-signaling (066) is genuinely over-determined. But the reproductions are **form-forced conditional on ~6 V5 postulates** (P-Bipartite-Mapping, P-V5-Schmidt-Generic, P-V5-Budget, P-Measure-Saturation, P-V5-Hilbert-Constraint, P-Substrate-Causality), with the **irreducibility that *defines* entanglement left as an A→assertion**, **two vN-entropy substrate-derivations open** (one structurally blocked), and the ER=EPR / individuation papers explicitly A→position interpretation. **Defensible headline:** *the bipartite entanglement formalism is reproduced form-forced / value-inherited, on a stack of V5 postulates and one unproven irreducibility assertion — a coherent structural account, not a primitives-closed derivation.*

---

## Addendum 2026-09-04 — §3.3's CKW inequality does not follow

**(a) §3.3 does not follow from §§3.1–3.2.** The chain gives `Σᵢ ℰ_{A,Bᵢ} ≤ Σᵢ W_{A,Bᵢ} = W_A ≤ W_max` — a bound by a **chain-local constant**. The displayed CKW form is `Σᵢ ℰ_{A,Bᵢ} ≤ ℰ_{A,(B₁∪…∪Bₙ)}`, a bound by a **state-dependent quantity**. These are different statements, and the second is strictly stronger whenever `ℰ_{A,union} < W_max`. Concretely: `ℰ_{A,B₁} = ℰ_{A,B₂} = 0.3 W_max` with `ℰ_{A,union} = 0.1 W_max` satisfies the derived bound (`0.6 ≤ 1`) and violates CKW (`0.6 > 0.1`). Nothing in §§3.1–3.2 relates `ℰ_{A,union}` to `W_A`, so nothing excludes it.

**(b) The gap is in the stated postulate, and closing it costs the inequality.** The step works if `ℰ_{A,union} = W_A` — saturation holding **generally**, for every pair *and* for the union. But **P-Measure-Saturation is stated only for the maximally-entangled limit** (*“saturates the V5 budget in the maximally-entangled limit”*). Strengthen it to general saturation and §3.3 follows — but then `Σᵢ ℰᵢ = ℰ_{A,union}` is an **equality**, and CKW's physical content is the *strict* inequality: the deficit is the residual three-tangle, the genuinely tripartite entanglement. **A pure budget-additivity account gives equality and leaves the three-tangle nowhere to live.** The strict inequality needs the measure to be *sub-additive* relative to the budget, and nothing here supplies that.

**What is actually derived, and it is worth keeping.** `Σᵢ ℰ_{A,Bᵢ} ≤ W_max`: a finite shared budget capping total pairwise entanglement, with `ℰ_{A,B₁} = W_max ⇒ ℰ_{A,Bᵢ} = 0` for `i ≥ 2` (§3.4, maximal exclusivity — which **does** follow). That is genuinely monogamy-flavoured, it is the right *kind* of mechanism, and it is a real result. **It is not CKW.**

**The paper half-knows this.** §4's FORM-FORCED line reads *“Existence of finite budget partitioning”* — which is exactly the defensible claim, and matches (c). It is **§3.3** that attaches *“Form FORCED”* to the displayed CKW inequality, and the arc ledger's row inherits that: *“Monogamy (CKW-form inequality) — form D (form-forced)”*. So §3.3 and §4 disagree about what is forced, and the stronger of the two propagated. **Textbook claim-strength drift (checklist §10 failure mode 7), and checklist item 20(a) would have caught it:** the claim is stated above the tier of its weakest input, which is a postulate scoped to one limit.

**Recommended, not applied.** §3.3 should state `Σᵢ ℰᵢ ≤ W_max` as the derived result and present CKW as *consistent with* it rather than forced by it; the ledger row should re-tier from **form D** to **Grounded** with CKW marked as the inherited target; and if the CKW form is wanted as a result, the open item is a **sub-additivity argument for `ℰ` against the V5 budget** — which is where the three-tangle would have to come from, and is a real piece of physics rather than an editorial fix. *No tier changed pending the author's call, since this narrows a published claim in a nominally closed arc.*

**ALL THREE FIXES APPLIED 2026-09-04.** §3.3 rewritten with the constant bound boxed as the derived result and CKW presented as *consistent with, not forced by* it, carrying both the counterexample and the equality-collapse argument. Audit row 7 corrected (it read “≤ chain-total entanglement”, the state-dependent bound), row 8 re-tiered **D (form) → A→consistency**, row 9 noted **unaffected** since it uses saturation exactly where the postulate states it. Ledger row split above. New open item **O-SubAdd** at `Paper_065` §6.x. *Cross-filed as `gravity/Gravity_TieredClaims_Ledger.md` Staleness #22.*

---

## Addendum 2026-09-04 — `Paper_066`'s three locks are not independent

**The three locks are not independent: they are one commitment at two levels, plus the bridge between them.** **L1** is microcausality in the emergent operator algebra — `[A_A, A_B] = 0` at spacelike separation, supplied by P-Bipartite-Mapping. **L2** is causality in the substrate — `K_V5 = 0` for spacelike-separated arguments, supplied by P-Substrate-Causality. **These are the same physical commitment stated at two description levels.** **L3** is not a third support at all: it says DCGT coarse-graining *preserves* algebra-locality, i.e. that the two levels correspond. It is the **bridge**, and without it L1 and L2 are statements about disconnected things.

**So §3.4's “refutation of any single lock leaves the others intact” does not hold for L3.** Refute the bridge and L1 concerns an emergent algebra with no established relation to the substrate, while L2 concerns a substrate with no established relation to the physics — neither establishes no-signaling *for the theory*. The three do not fail independently; two of them stop meaning anything without the third.

**And §3.4 concedes the L2 case in its own hedge.** It argues that refuting L2 leaves L1 intact because *“the marginal would still be independent **at the formal level**”*. That qualifier is the whole issue: formal marginal independence together with superluminal substrate signalling does not mean no-signaling holds — it means the formalism has stopped being faithful to the substrate. A lock that survives only formally is not a lock.

**The load-bearing element is the one that is not ED's.** Audit row 9 tiers L3 as **I**, inherited from `Paper_073`. So the bridge on which the composition depends is inherited, while the two things it bridges are the same commitment twice. That is the opposite of over-determination: it is a single support with an inherited joint.

**What is not in question.** No-signaling itself holds in ED, and this audit does not touch it — L1 is the standard argument correctly applied and is honestly tiered **D-via-I**. What fails is the *over-determination rhetoric*: §1's *“FORCED over-determined … three independent structural locks”* and §2's *“refutation of any single lock leaves the others intact”*. **Audit row 10 already tiers the composite verdict as A→position**, so the table is right and the prose is a notch above it — the same claim-strength drift recorded as checklist §10 failure mode 7, and the second instance today (after GR-IV's `α₂`/`c_s`) where two *“independent”* facts are one fact twice. **Item 20(c) flags it on the word “independent” alone.**

**Recommended, not applied.** §1 and §2 should say *two levels of one causality commitment, joined by an inherited coarse-graining bridge* rather than *three independent locks*; §3.4's independence argument should be replaced by the honest structure (L3 is necessary for L1 and L2 to compose); and the genuine robustness claim that survives is worth keeping in its correct form — **the commitment is checkable at two levels, so a failure at either would be visible**, which is real and is not over-determination. *No tier changed: row 10 is already A→position.*

*Cross-filed as `gravity/Gravity_TieredClaims_Ledger.md` Staleness #23.*

---

## Addendum 2026-09-06 — the master spreadsheet is now synced, and the section heading is a transcription trap

The four rows this ledger files under **`### Derived (forced — but each conditional on a postulate in the Postulated table)`** had all been transcribed into `ED_ItemizedTheory_TieredClaims.xlsx` as bare tier **`Derived`** — which that workbook's `Tier Key` defines as *"with **NO** paper-specific postulate."*

**The same word, meaning opposite things in the two documents.** The qualifier that makes this ledger's heading honest lives in the parenthetical, and **the parenthetical does not travel** when a row is copied into a tier column. Nothing was overclaimed here; the heading is accurate in context.

**Checked corpus-wide: seven of eleven arc ledgers qualify their `Derived` heading**, four of them with the postulate caveat spelled out (this one, gravity, qft, q-compute). So the trap is not local.

**Fixed in `ED_ItemizedTheory_TieredClaims_v2.xlsx` (2026-09-06):** all four rows re-tiered to `Grounded`; the monogamy row **split to match the 2026-09-04 narrowing above**, which the spreadsheet had never picked up (it still read *"Monogamy (CKW-form inequality) — form D"* with `Status: current`); `P-Bipartite-Mapping` added to the Schmidt row, which had named only `P-V5-Schmidt-Generic`; a `Rests On` column added naming each dependency; and a **warning added to the workbook's `Tier Key`** telling anyone transcribing from these ledgers to read the *"Inherited / open"* cell rather than the section heading.

**One discrepancy left open rather than resolved silently:** `Paper_065`'s §2.5 audit row 8 labels the CKW step **`A→consistency`**; the claim row above calls it **`Grounded — consistent with, not forced by`**. Both are defensible (a derivation *step* that is not forced, versus a claim *position* that is grounded), but they should be made to agree.

*Cross-filed as `gravity/Gravity_TieredClaims_Ledger.md` #124; `foundations/Note_Entanglement_C4_RootCause_2026-09-06.md`.*
