# Disambiguation — "individuation" in the ED corpus

**Written 2026-09-06.** Companion to `ADJACENCY_AND_BAND_DISAMBIGUATION.md`, and written for the same reason: a word carrying more than one structure, found by following it across arcs. Gravity ledger #131, #132.

**The one-line version: "individuation" names two different things, and one of them is just P11 under another name.**

---

## 1. The short version

| | what it is | kind of object | index set | canonical source |
|---|---|---|---|---|
| **1** | **commitment** — a chain's multi-channel participation collapsing to single-channel | an **event / rate** | `𝒦` (channels), at one locus | **`Paper_087` §P11** |
| **2** | **the system/environment cut** — when a set of loci counts as a distinct identity | a **dimensionless ratio + threshold** | the **locus** set | `foundations/Paper_Individuation_TheSystemEnvironmentCut.md` |

**Sense 1 is P11.** Canonical `Paper_087` §P11 reads:

> *"At certain substrate-level events ('commitment events'), **a chain's multi-channel participation collapses to single-channel participation**, with the un-selected channels' phase content randomized."*

and `q-compute/Paper_054` §3.4 defines its individuation timescale as

> *"the substrate's primitive timescale for **resolving multi-channel participation into single-channel participation**"*, with `τ_individuation ~ τ_V1 = ℓ_ED/c`.

> **Those are the same sentence. `Γ_individuation` is the rate of P11.** "Individuation" in sense 1 is a **second name for commitment**, and that redundancy is what made every collision below possible.

**Sense 2 is a different quantity entirely:** `S` is individuated iff `b_int(S)/b_bdry(S) > θ_ind`, with **`θ_ind = 1`** (`#129`–`#130`, conditional on `ξ < 2` at 9.2σ). It ranges over **loci**, not channels, and by `#128` the ratio measures a region's **linear extent**.

## 2. Where each sense appears

| file | sense | how it shows up |
|---|---|---|
| `Paper_087` §P11 | **1** | the canonical statement; "commitment", not "individuation" |
| `q-compute/Paper_054` §3.4 | **1** | `Γ_individuation`, `τ ~ ℓ_ED/c` — the rate of P11 |
| `q-compute/Paper_056` | **1** | the Class-A wall sits at `Γ_commit(M_cap) = Γ_individuation⁻¹` |
| `q-compute/Paper_060` | **1** | `P-Mcrit-Unified` — crossing `M_crit` "triggers P11 … individuation" |
| `entanglement/Paper_072` | **1** | entanglement = the regime *before* P11 selects (see §5.1) |
| `qm-kinematics/Paper_001` | **1** | "pre-individuation" = before commitment |
| `cosmology/Paper_ED_Inflation` | **1** | "individuation reactivated above the **P12 ED-threshold**" (see §5.2) |
| `primitives/concepts/thickening.md` | **1** | "individuated objects (because chains commit repeatedly)" |
| `primitives/concepts/individuation.md` §5.3 | **1** | measurement: "chain spans multiple channels" → "chain is in one channel" |
| `primitives/concepts/individuation.md` §5.4 | **2** | decoherence: "loses internal-to-boundary bandwidth ratio" |
| `foundations/Paper_Individuation_TheSystemEnvironmentCut.md` | **2** | the criterion, `θ_ind`, and the whole construction |

**Measured, not asserted** (`internal notes/_check_individuation_senses.py`, re-runnable): **616 occurrences across 81 files** — **55% sense 1, 14% sense 2, 32% ambiguous** (no marker either way, or both vocabularies in the same window).

> **The footprint is comparable to the four-band overload**, and the ambiguous third is the work list — not errors, but places where the sense has to be guessed.

**The cleanest files are the pure-sense-1 ones:** `Paper_054` (46 / 0 / 0), `Paper_001` (35 / 0 / 2), `Paper_072` (13 / 0 / 0) — **unambiguous, and all of them commitment.** **The most mixed is the source card itself** (`primitives/concepts/individuation.md`, 8 / 45 / 53), which is exactly what §3 predicts: it is the one document carrying both senses. **Sense 1 dominating is expected and is not a defect** — sense 1 is P11, which the corpus has always had; sense 2 has one paper, promoted 2026-09-05, which is why the collision is only now visible.

## 3. The trap that actually bit

**Sense 1 and sense 2 move in opposite directions under the same substrate change.**

Increase a system's boundary bandwidth to an external device:

- **Sense 1 goes UP.** Higher coupling drives commitment; the chain resolves to one channel.
- **Sense 2 goes DOWN.** `b_bdry` up means `R = b_int/b_bdry` down; the system is less individuated.

**So the two senses are not merely different — they are anti-correlated in the regime that matters most (measurement and decoherence).** That is why `primitives/concepts/individuation.md` §5.3 and §5.4 describe the same change as *"individuation is sharp"* and *"individuation weakens"* in consecutive paragraphs. **Neither is wrong. They are answering different questions.**

**And the split is exactly the one `P-Commitment-Advancement` had to bridge** (`#117`): **P11 selects a channel and is silent on the locus.** Sense 1 is the channel half; sense 2 is the locus half. **The two senses are related only through that postulate, and not otherwise** — which is also why `θ_ind` neither constrains nor is constrained by the Class-A wall (`#131`).

## 4. How to write each one unambiguously

| instead of | write |
|---|---|
| "individuation" for the P11 event | **"commitment"** — it is P11, and the corpus already has the word |
| `Γ_individuation` | **`Γ_commit-floor`**, or keep the name and gloss it *"= the rate of P11 channel collapse"* |
| "the system individuates" (channel sense) | **"the chain commits"** |
| "individuation" for the cut | **"the system/environment cut"**, or "individuation (sense 2, `θ_ind`)" |
| "individuated" of a region | **"individuated w.r.t. its environment"** — the criterion is **relational**, never intrinsic |
| "the best cut maximises `b_int/b_bdry`" | **nothing** — see §5.3; the criterion checks a cut, it does not find one |

**Rule of thumb: if the object is a channel, say commitment. If the object is a set of loci, say cut.**

## 5. Inconsistencies found — three recorded

### 5.1 `Paper_072` says *rule-type* where canonical P11 says *channel* — **SETTLED 2026-09-06: wording, not a third index**

`Paper_072` defines the unresolved regime as *"multiple **rule-type** assignments … simultaneously supported by V5"* with P11 not yet having *"selected a unique individuation"*, while canonical `Paper_087` §P11 collapses to a single `K` — a **channel** (P03/P07), not a rule-type (P10).

**Settled by two facts.** **(i)** Channels **carry** rule-type labels (Branch 3: classifying `𝒦(u)` by rule-type *"reads a label the substrate already carries"*), so **rule-type is a COARSER partition of the same index set** — selecting a channel fixes a rule-type, not conversely. P11 selects the finer thing. **(ii)** **`Paper_072` uses "rule-type" 5 times and the word "channel" ZERO times**, while citing `Paper_087` §P11 and `Paper_054` (both channel-indexed) and sitting on `Papers_063–068`, whose machinery is `Ψ_KL^AB` on `𝒦_A × 𝒦_B`. **It is the only paper in its own chain that uses the word.**

**Two readings, and only one survives.** **(a) The LABEL reading** — *assignment* = the rule-type the selected channel carries, so "multiple assignments coexist" means two or more **rule-types** are live. **This breaks the paper's own thesis:** a bipartite entangled state is a superposition over channel *pairs*, and **nothing requires those channels to differ in rule-type** — a two-qubit entangled state is matter rule-type throughout — so under (a) a standard entangled state would have a unique rule-type assignment and **would not be in the unresolved regime at all**, which is exactly what the paper exists to say it is. **(b) The CONFIGURATION reading** — *assignment* = the whole map of participation across channels, so "multiple assignments coexist" means several participation **configurations** are simultaneously supported. **Equivalent to the channel statement, and consistent with P11, `Paper_054` and the arc's own machinery.**

> **Reading (b) is the only one consistent with the paper's claim, so it is what is meant. THERE IS NO THIRD INDEX SET AND NO THIRD SENSE — this document stays a two-sense document.**

**What is owed is a wording fix and it is small:** five instances of *"rule-type assignment"* → *"channel assignment"*, plus one use of the word "channel" so the index is stated once. **Proposed, not applied** — it narrows a published paper in a nominally closed arc, which is the author's call. `foundations/Note_Paper072_RuleTypeOrChannel_2026-09-06.md`; gravity ledger #133.

### 5.2 There are two thresholds, and they are not the same one

`cosmology/Paper_ED_Inflation` says individuation is *"reactivated above the **P12 ED-threshold**"*. **That is a different threshold from `θ_ind`**, which is also a P12-adjacent individuation threshold and is now fixed at **1**. **Nothing yet relates them, and nothing should be assumed to.** Flagged so the numbers are not merged by someone reading both.

### 5.3 The card's "best cut" prescription is vacuous

`primitives/concepts/individuation.md` §5.5: *"the best cut is the one with the **largest** `b_int / b_bdry` ratio."* **`R` is closed under union** (`#128`, 0 violations in 400 pairs) and `b_bdry(V) = 0`, so `R(V) = ∞`: **maximising `R` selects the entire universe, every time.** Since the admissible family is upward-closed, **a cut must be chosen by something other than maximising `R`.** Corrected in place.

## 6. Where the collisions were flagged in place

| flag | file |
|---|---|
| the two senses, banner over §5.3–§5.5 | `primitives/concepts/individuation.md` |
| §5.5's vacuous prescription, corrected | `primitives/concepts/individuation.md` §5.5 |
| what `θ_ind` does **not** cover | `foundations/Paper_Individuation_TheSystemEnvironmentCut.md` §4.7 |
| `θ_ind` vs the Class-A wall, and the factor of 3 | `foundations/Note_Individuation_TwoSenses_2026-09-06.md` |
| `θ_ind` is a length; union closure; the expander scope | `foundations/Note_ThetaInd_IsALength_2026-09-06.md` |
| `θ_ind = 1` via the decoherence route | `foundations/Note_ThetaInd_DecoherenceRoute_2026-09-06.md` |
| the term's spread, measured and re-runnable | `internal notes/_check_individuation_senses.py` |

## 7. What is NOT claimed

- **That any arc's physics is wrong.** Every paper above is internally sound. **The word is what is overloaded.**
- **That the two senses should be unified.** They may simply be two things; `P-Commitment-Advancement` is the only bridge the corpus has, and it is a postulate.
- **That sense 1 should be renamed corpus-wide.** §4 is a writing rule for new text. Retitling `Paper_072`, `Paper_054` §3.4 or `Γ_individuation` is the author's call, and each is cited downstream.
