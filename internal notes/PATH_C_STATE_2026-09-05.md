# Path C — state, 2026-09-05 (late)

*Written to be picked up cold. **Read this before resuming; do not reconstruct Path C from memory.** Everything below is checkable against `physics-papers/gravity/Gravity_TieredClaims_Ledger.md` items **#82–#94** and the scripts named. Companion to `PATH_A_STATE_2026-09-05.md`.*

---

## What Path C is

**One question, asked at ten scales: *what licenses combining bandwidth across things?***

That is the spine, and it is the thing most likely to be lost if this session compacts — the individual ledger items would survive, the fact that they are one question would not.

| # | item | the combining question |
|---|---|---|
| 82–85 | four-band conflict reopened, branch 3, band-overlap check, the cut exists | across **channel classes** — what makes bands disjoint |
| 86 | individuation promoted to a construction | across **a cut** — where a system ends |
| 87 | the `w(e)` map | across **an edge** — what two loci share |
| 88 | geometric mean vs `min` | across **a merge** — regridding |
| 89 | (R) is DCGT's; two merge rules | across **a cell** — which regime |
| 90 | the P04 additivity license | across **a region** — what licenses it at all |
| 91 | `Paper_003` is insensitive to the bands | across **a partition** — when the question does not arise |
| 92 | “four-band” names four different things | across **a name** — when the footprint is an artifact |
| 93 | **Branch 3 applied** — bands classify $\mathcal{K}$, P04 sums | across **channel classes** — answered, and the residue named |
| 94 | the dwell arc's `∇_adj` borrow | across **primitives** — when a name is borrowed from the wrong one |

**It produced a general answer, not ten local ones.** Canonical `Paper_087` P04 now carries the licensing clause: bandwidth adds over a region exactly when the summed contributions carry **no relative phase**, which happens three ways — **(a) disjoint channels** (P04 as written), **(b) committed content** (P11 commits in the channel basis only, so committed content has no phase to interfere), **(c) a decoherent regime** (`Coh → 0`).

## How Path C started, and where Path B went

**Path B was Koide, and it is CLOSED, not paused** — correcting something I said mid-session.

Ledger **#81** is Path B's only item and it already ran the test: with `P_i = √m_i`, Koide's denominator is `Str + Coh` with every `cos Θ_ij = 1`, so `Q = Str/(Str+Coh)` and `Q = 2/3 ⟺ Coh = ½Str ⟺ Σ_C = −½Str`. **Checked on PDG values: `Coh/Str = 0.500014`, `Q = 0.66666051`.** Exact. **And not a derivation** — nothing in ED predicts `Coh = ½Str` for the charged leptons. The corpus had already ruled on the class: `arcs/arc-M/mass_ratio_constraints.md` §6.3 — *"Koide-relation-style formulae … not derivable from ED primitives at this stage"*, because *"ED's primitive structure produces classifications and dichotomies cleanly, but does not produce continuous numerical relationships."* **That verdict stands.**

**So "go back and test Koide" is not an open move.** The test was run; the answer is *exact re-expression, no derivation*. Path C is what Koide's diagonal/off-diagonal question opened on the way, and it is where the live work is.

## What Path C changed, honestly

**Gained:**

1. **Individuation is a construction, not a concept** — verdict M3, form-derived from P02+P03+P04, and **three arcs independently depended on it** (the `Str(C)` aggregation, the four-band classification, the layer-1/layer-2 seam).
2. **The `w(e)` map exists**, and the gap was a **scheme translation** — the earlier primitive set (now `primitives/concepts/`) put bandwidth on **edges**, canonical P04 puts it on **(channel, locus)**, and individuation was never translated. Third artefact of that scheme change found in one session.
3. **`w(e)` and `Coh` are one object read two ways** — `|Coh_(u,v)| ≤ 2w(u,v)`, equality at full phase alignment. `w(e)` is `Coh`'s envelope with the phase stripped.
4. **The P04 additivity license**, above. Written **once, canonically**, rather than eight times.
5. **`Paper_073` §3.2's unstated regime condition**, found and flagged — then found to be corpus-wide rather than local, and `Paper_073` on the safe side of it.

**Corrected mid-flight, twice, both worth remembering:**

- **#88 overclaimed.** It said the geometric mean was forced *full stop*. **#89 found (R) is already DCGT's own well-definedness clause — good — but that DCGT merges by *bandwidth*, not amplitude, under which (R) forces the *product*.** So the weight is **regime-dependent**, and a third candidate had been invisible because a normalization *I* chose excluded it. `min` stays excluded under both rules, which was the live fork. **The note now carries a read-§8b-before-citing-§6 banner.**
- **#82 reopened my own #57.** The four-band withdrawal used the *archived* `paper_M2` to override canonical `Paper_087`, against the corpus's standing rule. Reopened and deliberately **not** re-flipped — AP's call.

## The open items

**AP's calls, both still pending:**

1. ~~**The four-band branch**~~ — **DECIDED by AP 2026-09-05: BRANCH 3, applied as #93.** The bands are a classification of $\mathcal{K}(u)$ licensed by P07/P10 (with P05/P11 picking out particular classes), *summed by* P04 — not a decomposition of `b_K`. **`Paper_087` needed no change**, which was the branch's strongest argument. Card amended; transport arc re-grounded (`F-COONSET` keeps its referent); Higgs/dwell unblocked at the sourcing level but **still owes its second repair**. **Residue named: `P-Band-Partition`** (disjoint + exhaustive over $\mathcal{K}(u)$ — discharged only *relative to a system `S`*, via individuation, so **the bands are relational**) and **`P-Locus-Bandwidth-Bound`** (P04 gives non-negativity, not an upper bound — the transport arc had been assuming one). **Census 171 → 173.**
2. **Naming `P-Radial-Channel-Density`** in `Paper_030` §4.3 — adopting it increments the census from **171**. Also Path A's open item #2.

**Work:**

3. ~~**`Paper_003`**~~ — **CLOSED (#91): it does not need the partition, and the stronger finding is that it is *insensitive* to it.** Its only use of bandwidth is the normalized sum `Σ_{K'} b_{K'}`, and **any partition of the channel set leaves that sum unchanged** — so it cannot need the partition and is not evidence for it either. What it needs is P07 + P04 additivity over the channel set + **channel orthogonality** (which is what *“four-band orthogonality”* was reaching for) + `P-LinRate`. **`Paper_003` comes off the dependent list.** A naming collision was flagged on the way: `Paper_003_5` §§3.3–3.4's *“adjacency-bandwidth”* means bandwidth along graph adjacency, **not** the partition's “Adjacency band”.
3b. ~~**`Paper_012_6_Heisenberg`**~~ — **CLOSED (#92): a DIFFERENT four-band partition.** Its `P-FourBand` is **position / momentum / time / energy** (conjugate pairs), a separate named censused postulate with its derivation open; the disputed one is **Internal / Adjacency / Environmental / Commitment-reserve** (participation-partner type). **The term is overloaded four ways** — add `Paper_004_5` §3.6's **Bell-test settings** and `Paper_003_5`'s **adjacency-bandwidth** — so a grep overstates the disputed partition's footprint by **~3×**. **Exactly one genuine paper-level dependent survives:** `Paper_UnifiedP04TransportBudget`, which already calls the dependency *“the load-bearing joint … the single most important thing to attack.”* **Two card problems flagged:** `primitives/P04_bandwidth` tiers the partition **more strongly than its own source concept** (which calls it *“motivated empirically”*, open twice), and **claims a dependent it does not have** (`Paper_003`). **Net: AP's branch decision is now a cheap one** — but cost is not truth, and the decision stands.
4. **`θ_ind`** — individuation's *only* undetermined quantity now that `w(e)` is written. The source concept flags it twice: *"Structural constant? Regime-dependent? Tied to `ℏ` / bandwidth normalization?"*
5. **The transport arc's `S` identification** — is the transport cell the individuated complex?
6. ~~**The Higgs/dwell arc's second defect**~~ — **CLOSED (#94), as a diagnosis rather than a rescue.** The `∇_adj` borrow is a **naming collision** (P12's `∇_adj` is a *derivative operator*; the Adjacency band is a *class of channels*), and **its conclusion is contradicted** — `Paper_012_7` has adjacency as the **boost-invariant position sector**, not the movement one. The band the argument needed (**propagation/momentum**) lives in `Paper_012_6`'s `P-FourBand`, a **different partition**. And **canonical P11 is silent on locus**, so *commitment ⇒ advancement* is an identification, named as the candidate **`P-Commitment-Advancement`** and **deliberately not adopted** (census stays 173). **Net: the route is no longer blocked by a sourcing error but by an honestly-stated missing postulate** — a better place to be blocked. Mass sector unaffected.

## Where Path C meets Path A

**Path C is not a detour from Path A; it built the instrument Path A's hardest item needs.**

- **Path A #1, the layer seam / the `2π`** — *"the first real question"*. `Note_Individuation_Is_TheCut_2026-09-05.md` already records that what crosses the seam **is boundary bandwidth**, which is now a defined quantity.
- **Path A #2, the radial `1/R` channel density** — *what `𝒦` contains as a function of distance from a mass* is an aggregation-licensing question, i.e. a Path C question. It is item 2 above.
- **Path A #3, `Grad` still a proposal** — untouched by Path C.

## What not to trust without re-checking

- **My "what's missing" claims.** Path A recorded four wrong ones; Path C added a fifth (nearly claimed the system/environment cut was absent — individuation exists). **All five were caught by opening a file. Discount accordingly.**
- **#88 read alone.** §§1–7 state the uniqueness unconditionally; §8b is the correction. The banner is there for this reason.
- **The astral character `𝒦` (U+1D4A6)** broke scripted writes repeatedly. **Use `$\mathcal{K}$` in edit payloads**, and `_safe_edit_template.py` for any scripted edit.

## Instruments built on Path C (all re-runnable)

| Script | What it does |
|---|---|
| `internal notes/_check_edge_weight_map.py` | the `w(e)` map against individuation's three worked examples |
| `internal notes/_check_edge_weight_discriminator.py` | geometric mean vs `min`, four discriminating tests |
| `internal notes/_check_merge_rule_regimes.py` | the two merge rules, and what (R) forces under each |
| `internal notes/_check_dcgt_regime_users.py` | screens DCGT-citing papers; adjudicates the P04-additivity sites |

Plus Path A's, all still current — `_census_postulates.py` is the one to run first: it exits 0 if the corpus is where Path C left it (**171 postulates, 0 orphaned falsifiers**).

## How to resume

1. **Read this file, then ledger items #82–#90 in reverse order.** They are the whole thread.
2. **Run `_census_postulates.py`.**
3. **Items 1, 3 and 3b are closed (#93, #91, #92).** The remaining AP call is **item 2** (naming `P-Radial-Channel-Density`). Next work item is **4 (`θ_ind`)**, individuation's only undetermined quantity.

---

*Path A: ledger #58–#80 (`PATH_A_STATE_2026-09-05.md`). Path B: #81, closed. Path C: #82–#94.*
