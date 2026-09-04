# Claim-Strength Audit, 2026-09-04 — all fifteen arcs

**What this is.** A single-session external audit of every tiered-claims ledger in `physics-papers/`, asking one question of each load-bearing chain: *does the sentence claim exactly what the derivation supports, no more?* The audits are recorded in full in `physics-papers/gravity/Gravity_TieredClaims_Ledger.md`, Staleness **#10–#33**, which carries the day's whole trail. This file is the map, not the record — **the ledgers remain authoritative for tiers and the papers for content.**

**Method.** Read the chain in the paper, not the summary of it. Where a claim could be checked mechanically (a census, a dimensional check, an integral, a coefficient), check it. Where two documents state the same thing, compare them. Hold negatives to the same bar as positives.

---

## Coverage

| Arc | Ledger item(s) | Outcome |
|---|---|---|
| gravity | #10, #12–#20, #27 | 8 findings — carried most of the programme |
| black-hole | #18 | `4π` → `N = A/ℓ_P²` corrected; multiplicity bound collides with Bekenstein (OPEN) |
| qm-kinematics | #21 | ℝ-exclusion carried by a representation, not a primitive — fixed |
| substrate-evaluation | #21 | Gleason keystone §5 rewritten with the four continuity steps |
| entanglement | #22, #23 | CKW gap fixed; three "independent locks" are two (OPEN) |
| cosmology | #24, #30 | README overclaim on `w = −1`; Θ_ED correction unpropagated for two months |
| q-compute | #25 | Arc already clean; one disclosure gap in the shape-retreat |
| constants-inherited | #26 | "`G` adds no information" is circular with `ℓ_ED` set by Newton-recovery |
| dark-sector | #27 | Where the 2π propagation failure surfaced |
| qft | #28 | **Clean. No finding.** (Yang–Mills, the mass gap) |
| dynamics | #29 | Cross-arc tier disagreement on `c_T = c` — fixed both ways |
| relativistic-qm | #31 | **Clean. No finding.** |
| state-reduction | #32 | One stale self-flag — fixed |
| readings / OtherTheories | 2026-09-03 pointer sweep | Stale staleness note found and fixed; no F2 claim-strength pass |
| foundations | #33 | Stated postulate count roughly half the measured one |

---

## The findings

### One claim lost its tier

The `1/(2π)` in **`a₀ = cH₀/(2π)`** is not established as structurally forced. `Paper_028` §6.3 and `Paper_029` §5.1 both evaluate the azimuthal integral to **1**, so the factor cancels in their own displayed algebra and is reinstated at an assembly step by a normalization fixed nowhere. **Re-tiered Postulated / disputed** (#10).

*Unaffected:* `a₀ ~ cH₀`, reached three independent ways, and the forced exponent of 1 in `a₀(z) = cH(z)/(2π)`.

### Six claims one notch stronger than their support

Derivation sound, audit table honest, sentence overreaching. In every case the paper's own table already said the right thing.

| Claim | Item |
|---|---|
| `Paper_GR-IV`'s `α₂ = 0` — its own source says one tier lower | #20 |
| `Paper_030` §6.3/§7.2 on the μ interpolation function | #15 |
| `Paper_038.5`'s `w = −1` — honest in the paper, overclaimed in the README | #24 |
| `Paper_027`'s "unique" → unique **in powers** (the coefficient needs `P-G-Closure`) | #17 |
| `Paper_065` §3.3 — the CKW inequality does not follow from §§3.1–3.2 | #22 |
| `Paper_066`'s three "independent locks" — one commitment at two levels plus an inherited bridge | #23 |

A sub-pattern ran through three of them: **endpoint eliminations presented as exhaustive** (GR-III's β, `Paper_038.5`'s n, GR-IV's α₂). Eliminating the endpoints of an interval leaves the interval.

### Three propagation failures

A correction recorded in a ledger and never carried to the documents that repeat the claim.

- **The 2π** — recorded as #10, left unflagged in **twelve** documents including all three public-facing ones, for one day (#27, mine).
- **Θ_ED** — the 2026-07-06 primitive-attribution correction, recorded in the cosmology ledger 2026-07-29, unpropagated to four papers for **two months** (#30).
- **The state-reduction self-flag** — the defect was fixed in the paper 2026-07-29; the arc-state paragraph that *enumerates the arc's exceptions* still listed it as live (#32).

### Two structural inconsistencies

- **`Paper_030` §4.2** dropped two channel-count factors between one equation and the next. The fix required naming a new postulate, `P-Bilocal-Count` (#16).
- **The MOND transition** — the corpus held two incompatible accounts, and an earlier staleness entry had named the wrong one as standing (#19).

### One circularity, on one page

`constants-inherited` lists `ℓ_ED = ℓ_P` *"set empirically via Newton-recovery"* and, two rows later, `G = c³ℓ_P²/ħ` as a derived combination that *"adds no information."* If `ℓ_ED` is fixed by matching `G`, presenting `G` as derived from `ℓ_ED` is circular **as an explanation** — the count is right, the word was wrong. `G` was not explained, it was renamed. The real parsimony is **multi-use**: one postulated scale spent in the holographic channel count, the black-hole area law, and the UV cutoff (#26).

### One under-claim

The only one of the day. `c_T = c` was **D-structural** in the gravity ledger and **Inherited** in the dynamics ledger. Both right about different things, and the corpus's own `Paper_095` grammar resolves it: the **identity** (tensor waves and light share one cone) is structural, derived in GR-II; the **value** is inherited via `P-RB-1`. Left unfixed it undercut GR-IV's untunability argument from inside the corpus (#29).

### The constitutional finding

`Paper_088` states, in a box: *"The framework operates with 13 universal primitives + ~18 paper-specific postulates = **31 total** substrate-level commitments."* The line four above it correctly scopes that count to **Wave-2**; the box drops the scope. A mechanical census returns **51** distinctly-named `P-*` postulates, itself a floor — so **13 + 51 = 64+**. `Paper_100`, the program overview, already says **"60+"** and is the accurate one.

**The overview is honest and the constitution is stale, which is backwards**, because a reader auditing ED for parsimony goes to 087/088. And this programme made it worse: it named **two** new postulates (`P-G-Closure`, `P-Bilocal-Count`) with no path back to the arc that counts them (#33).

---

## What the corpus got right

Two arcs returned **nothing**.

- **qft / Yang–Mills** — the highest-stakes claim in the corpus, a Clay problem, and the cleanest chain audited. The arc closes at *"Clay-relevance / structural-positive level"* and says explicitly that it is not a proof.
- **relativistic-qm** — its headline derivation disowns itself. `Paper_112` derives ℏ, then prints a circularity disclaimer in its own body (`B_P04` has no independent substrate definition, so the equation is a substitution) — **and propagates that disclaimer into the ledger**, which is exactly the step whose absence produced #27 and #30.

Elsewhere the same discipline shows up unprompted. `Paper_116` declines to derive a no-third-mass-mechanism claim it could have asserted, then argues with its own label in parentheses. `Paper_099` tiers Navier–Stokes at structural-positive and says **NOT a Clay proof**. `foundations` engages Wheeler–Feynman directly and concedes the empirical distinction is underdetermined. `state-reduction` reports its own MOND-`E_G` signature as an EFE artifact, against its own interest.

**No physics was overturned. No derivation was found wrong. Every finding was about the sentence, the scope, or the distribution, never the mathematics.**

---

## The model

Three things came out of the sequence that were not visible at the start.

**1. Drift is not uniform.** It is worst where an arc has not been re-read since drafting, and effectively absent where one has. That makes time-since-re-read a better targeting signal than importance.

**2. Care scales with perceived risk, so audit inversely.** Yang–Mills was the cleanest chain in the corpus because a Clay problem gets written defensively. The `c_T = c` under-claim sat in GW phenomenology, where nobody feels watched. **Nobody audits an arc for excessive modesty.**

**3. The pointer layer fails differently from the paper layer.** Papers drift by a notch of wording. Ledgers, READMEs and summaries fail by *not moving at all* — a correction lands in one place and the four documents repeating the old claim are never touched. Three of the day's findings were this, and it is the failure the read-first rule depends on not happening.

### One new result, and it came from reading

The **horizon-competition threshold for `a₀`** (#14, research target #19). `Paper_047_5` had held the ingredient at M3 since July. No model produced it; the corpus did.

---

## What changed in the checklist

`PAPER_WRITING_CHECKLIST.md` gained, this session:

- **19** — cross-section symbol sweep: follow the quantity, not the spelling.
- **20(a)–(d)** — tier inheritance; premise-naming symmetry; a strength-word grep; and **endpoint eliminations are not exhaustive**.
- **21** — re-tier propagation: *"a ledger entry is not propagation"*, and its mirror, *"a ledger's own prose summary is a propagation target too."*
- **Failure mode 6** — a correction recorded and not distributed.
- **Failure mode 7** — the sentence one notch past the table. Six instances tabulated.

---

## Still open

| Item | Where |
|---|---|
| The `1/(2π)` in `a₀` — two repair routes, one closed as a negative | `gravity/Note_a0_TwoPi_RepairRoutes.md`; targets #18 |
| Channel-count factors in the bilocal geometric mean | #16 |
| `QuadraticStrain` — the second discharge is inconsistent | #13 |
| The factor of 4 — multiplicity bound vs Bekenstein | #18 |
| `Paper_066` — the third lock | #23 |
| `Paper_038.5` — the elimination leaves an interval | #24 |
| A reconciled postulate count **with a stated accounting basis** | #33; `Foundations` staleness #3 |
| ξ = 1.7575 and the `0.6` exponent re-anchored to a paper, not a memory file | `Foundations` staleness #4 |

---

## A note on the audit's own error

This programme declared itself complete at fourteen arcs, in commit `797b54e`, writing *"All fifteen arc ledgers now audited."* Thirteen had been audited; `foundations` had not, and was found only by counting coverage afterwards. **The audit's summary claim drifted one notch past its support — failure mode 7, committed by the audit, about the audit.** It is recorded here rather than quietly corrected, because that is the method.
