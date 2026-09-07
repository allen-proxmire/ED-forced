# `M_cap` carries two definitions, and the Class-A wall is built from the wrong one

**Written 2026-09-07.** Found while chasing a sign question about `Γ_commit`, which is not what this turned out to be about. **Same class of defect as foundations #10 (`|Σ P|²` assigned to both `Coh` and `Str`): one symbol, two structures, invisible because the two papers never state which constituent they mean.** Q-compute ledger, 2026-09-07 (4).

---

## 1. The collision, in four lines

**`Paper_053` §3.1** — `M_cap` is a **minimum of three** constituents:

$$\mathcal{M}_{\mathrm{cap}}(s) := \min\big\{ N_{\mathrm{bw}}(s),\; N_{\mathrm{V5}}(s),\; N_{\mathrm{commit}}(s) \big\}$$

with `N_bw` the bandwidth-limited count (P04), `N_V5` the V5-correlation-limited count, `N_commit` the commitment-threshold-limited count (P11).

**`Paper_053` §3.2** — the three classes are distinguished by **which constituent binds**:

> **Class A:** `N_bw` saturates first — engineered-low-multiplicity platforms (`Paper_056`).
> **Class B:** `N_commit` saturates first — global-geometric-rigidity platforms (`Paper_057`).
> **Class C:** `N_V5` saturates first — high-multiplicity-redundancy platforms (`Paper_058`).

**`Paper_054` §5.1** — `M_cap` is defined by a **single** condition, `Γ_commit(M_cap) = Γ_indiv⁻¹`:

$$M_{\mathrm{cap}} = \left(\frac{\Gamma_{\mathrm{indiv}}^{-1}}{\Gamma_0}\right)^{1/\gamma}$$

**`Paper_056` §3 (line 134)** — the **Class-A wall** uses that formula verbatim. `N_bw` appears nowhere in `Paper_056`.

> **So the Class-A wall's mass formula is built entirely from the commitment-rate constituent — which `Paper_053`'s own taxonomy assigns to Class B.**

---

## 2. Why this was invisible

Both papers write `M_cap` and neither states which constituent it denotes. `Paper_053` introduces the `min` and immediately moves to the class projections; `Paper_054` derives its cap from `Γ_commit` without reference to the `min`; `Paper_056` inherits `Paper_054`'s formula and anchors it to matter-wave data. **Read singly each is coherent. The collision only appears when the class assignment in `053` §3.2 is read against the formula in `056` §3.**

**This is the same failure mode as the `Coh`/`Str` collision (foundations #10):** *neither paper states its index set, which is exactly why the collision is invisible.*

---

## 3. What it costs, and it lands on this session's own work

**Two sessions of work were aimed at `Γ_commit`'s multiplicity dependence in order to firm up the Class-A wall's *sharpness*** (q-compute ledger 2026-09-07 (2) and (3)). **If `Paper_053` §3.2 is right, that work firms up Class B's wall, not Class A's.** The `Σ_C` counting result stands on its own; what is in question is what it was for.

**It also weakens an argument made in (2).** That entry excluded exponential and logarithmic forms partly on the grounds that *the only candidate multiplicity scale is `M_cap`, and `M_cap` is defined by `Γ_commit`, so using it inside `Γ_commit` is circular.* **That circularity holds only under `Paper_054`'s definition.** Under `Paper_053`'s, `M_cap` also contains `N_bw` and `N_V5`, **neither of which is defined via `Γ_commit`** — so a multiplicity scale is available in principle and the exclusion loses that support. *(The polynomial-boundedness argument for `Σ_C` is untouched; only the "no available scale" leg is.)*

---

## 4. Three candidate resolutions, none adopted

Stated the way foundations #10 stated its three, because **the choice changes the arc's structure and is the author's**.

**(1) `Paper_053`'s class assignment is right; `Paper_056` computes the wrong constituent.** Then the Class-A wall should be derived from **`N_bw`**, a P04 bandwidth budget, and `Γ_commit`'s functional form is irrelevant to it. **This is the cheapest to state and the most disruptive to `Paper_056`**, whose entire §3 would be rebuilt. *It has an attraction: a bandwidth budget is a hard counting bound, and "you run out of bandwidth" is a **simpler and sharper** mechanism for a sharp wall than a rate crossing — the sharpness would stop needing `Γ_commit`'s form at all, which would make the last two sessions' residuals moot for Class A.*

**(2) `Paper_054`/`056`'s cap is right and `Paper_053` §3.2's class assignment is mislabelled** — Class A is `N_commit`-bound and the A/B/C labels need swapping or restating. **Cheapest to `Paper_056`, but it puts `Paper_055`'s A/B/C exhaustiveness argument and `Paper_057`'s Class-B construction in question**, since Class B would then need a different binding constituent.

**(3) The two `M_cap`s are different objects at different layers** — `Paper_053`'s is the composite substrate cap, `Paper_054`'s is the commitment-projection of it, and `Paper_056` should be using `min{·}` with `N_bw` binding. **Cleanest if true, largest rewrite**, and it needs each paper to state which object it means — the fix foundations #10 applied to `Coh`/`Str`.

---

## 5. What is *not* in question

- **The `Σ_C` counting result** (`Str` single sum, `Coh` double sum, `∝ M² − M`, `γ` two-valued). It is a statement about P12 and stands regardless.
- **`Paper_053`'s `min` structure being forced by simultaneity** — a substrate must satisfy all three constraints at once. That argument is sound.
- **The Class-A wall's *architecture-independence***, which is a claim about one `M_cap` governing multiple platforms and does not depend on which constituent binds.
- **The empirical status of the wall** — the 175–250 kDa window and its testability now are unaffected.

---

## 6. The sign question this was meant to answer

It was: *`Coh` is the stabilising term and grows as `M²`, so should `Γ_commit` FALL with `M`, opposite to `Paper_054` §3.2's rising form?*

**It is not answered here, and the collision changes its scope.** Under resolution (1) the question does not arise for Class A at all — a budget cap has no rate direction — and remains live only for Class B. Under (2) it is live for Class A and is the more urgent question of the two. **So the sign question is now downstream of the definition question, and the definition question should go first.**

---

*Working note. No paper edited beyond flags pointing here. The three resolutions are the author's choice; adopting one silently is exactly what made the original collision invisible.*

---

# ADDENDUM 2026-09-07 (same day) — `Paper_055` read, and it settles more than expected

**AP's call: read `Paper_055` rather than decide.** Right call. It arbitrates, and it does so in a way that changes the answer: **two of the three resolutions above are superseded by a fourth, and the root cause is a category error rather than a disagreement.**

## A. `Paper_055` confirms the assignment — and breaks its own provenance doing it

`Paper_055` §3 and its claims table both carry the `Paper_053` reading:

> `N_bw` saturates → Class A. `N_commit` saturates → Class B. `N_V5` saturates → Class C.

| # | claim | tier | source |
|---|---|---|---|
| 4 | **Class A ↔ `N_bw` saturates** | **I** | **`Paper_056`** |

> **`Paper_055` inherits *“Class A ↔ `N_bw`”* from `Paper_056`, and `Paper_056` does not contain that claim.** Its only mention of bandwidth is P04's primitive statement (`b_K ≥ 0`, additive). **`N_bw` is never defined or used there.** The cap `Paper_056` computes is the commitment-rate one.

**So the `I` tier on row 4 cites a source that does not carry the content.** That is not a disagreement between two papers; it is a **provenance chain with nothing at the end of it**, and it is why no amount of reading either paper alone would surface the problem.

## B. A second collision, independent of the first — B and C are swapped

`Paper_056` §6 maps the classes to **engineering levers**, and that mapping disagrees with `Paper_053`/`055` on B and C:

| class | `Paper_056` lever (its own §6) | `Paper_053`/`055` constituent |
|---|---|---|
| **A** | Lever A — multiplicity engineering → **UR-1.1** | `N_bw` |
| **B** | Lever B — **cross-bandwidth** protection via geometric/topological rigidity → **UR-1.2** (V5) | **`N_commit`** |
| **C** | Lever C — **commitment-injection** control via redundancy/error-correction → **UR-1.3** | **`N_V5`** |

> **B and C carry opposite constituents in the two accounts.**

**And `Paper_056`'s version is the one that matches the class *names* both papers share.** Class B is *“global-geometric-rigidity”* in both — and rigidity maintaining cross-chain correlation is a **V5** story, which is `Paper_056`'s Lever B and `Paper_053`'s **Class C** constituent. Class C is *“high-multiplicity-redundancy”* in both — and redundancy/error-correction suppressing commitment injection is a **P11** story, which is `Paper_056`'s Lever C and `Paper_053`'s **Class B** constituent. **The names track `Paper_056`'s physics; the constituent labels in `053` §3.2 are crossed.**

## C. The root cause — two different trichotomies, treated as one

This is the finding, and it dissolves the disagreement rather than settling it.

- **`Paper_053` sorts the classes by which of `M_cap`'s three constituents binds:** `N_bw`, `N_V5`, `N_commit`. **All three are limits on a COUNT.**
- **`Paper_056` sorts the classes by which of UR-1's three conditions fails:** UR-1.1 (`M_eff < M_cap`), UR-1.2 (`Γ_cross > Γ_decoupling`), UR-1.3 (`Γ_commit < Γ_indiv⁻¹`). **One count condition and two RATE conditions.**

> **These are not the same three things, and they cannot be put in correspondence.** `M_cap = min{N_bw, N_V5, N_commit}`, so **UR-1.1 already contains all three constituents.** Mapping the classes onto UR-1's conditions and onto `M_cap`'s constituents are two different partitions of the arc, and the papers have been treating them as one partition under one name.

**That is why row 4's provenance is empty.** `Paper_055` needed a constituent for Class A and reached for `Paper_056`, which sorts by conditions and has no constituent to give.

## D. Resolution (4) — proposed, and better supported than the three above

**`Paper_056`'s class↔UR-1 mapping is the sound one; `Paper_053` §3.2's class↔constituent mapping is a category error; and `Paper_056`'s cap should be the `min`, not the commitment formula alone.**

1. **Keep** `Paper_053`'s `min{N_bw, N_V5, N_commit}` — the min-structure-forced-by-simultaneity argument is sound and untouched.
2. **Keep** `Paper_056`'s A/B/C ↔ UR-1.1/1.2/1.3 lever mapping — it matches the class names and the physics.
3. **Withdraw** `Paper_053` §3.2's *“which constituent saturates”* class definition, and `Paper_055` row 4's inherited-from-nothing citation.
4. **Repair `Paper_056` §3**: Class A fails **UR-1.1**, so its wall is set by **`M_cap` itself** — the `min` — not by the commitment-rate constituent alone. **Whichever constituent is smallest for a matter-wave platform sets the wall, and `Paper_056` never asks which.**

> **What this does to the last two sessions' work.** The `Γ_commit` result is **not** aimed at the wrong class after all — Class A fails UR-1.1, and `Γ_commit` enters `M_cap` through `N_commit`. **But it is only one of three constituents, and `Paper_056` assumed it is the binding one without checking.** *So the standing question is no longer “which class is this work for” but “is `N_commit` actually the smallest of the three for a 175 kDa molecule?” — which is a well-posed and answerable question, and nobody has asked it.*

**And the sign question inherits the same fate.** It matters only if `N_commit` binds. **Ask which constituent binds first.**

## E. Status

**Resolutions (1) and (2) above are superseded** — both assumed the two accounts were making the same kind of claim. **(3) was closest and is now stated precisely as (4).** Still the author's call, but the evidence now points one way, and **two concrete defects are identified independently of the choice: `Paper_055` row 4's empty provenance, and `Paper_053` §3.2's crossed B/C constituents.**

---

# ADDENDUM 2 — the estimate was attempted and CANNOT be run, which answers more than it would have

**The plan was the cheap one: work out which of the three budgets is smallest for a 175 kDa molecule, and let that decide whether any of the surgery above is needed.** It cannot be done, and the reason is the most useful thing in this note.

## F. None of the three constituents has ever been quantified

Searched every paper in the arc for a definition of `N_bw`, `N_V5` or `N_commit`. **There is no formula for any of them anywhere.** `Paper_053` §3.1 introduces all three in a single sentence of prose:

> *“`N_bw` is the bandwidth-limited count (P04), `N_V5` the V5-cross-chain-correlation-limited count (Paper_090), and `N_commit` the commitment-threshold-limited count (P11).”*

and that is the whole of it. Downstream papers use the symbols **structurally** — which technique raises which budget, which class a platform falls into — and **never numerically**. `Paper_059` is typical: error correction *“increases the `N_V5` budget”*, reservoir engineering pushes *“`N_commit` upward”*. Directions, not values.

> **Only one of the three has a number attached anywhere: `N_commit`, through `Paper_054` §5.1's `M_cap = (Γ_indiv⁻¹/Γ₀)^{1/γ}`.**

**So the comparison the estimate needs cannot be set up. You cannot ask which of three budgets is smallest when two of them have never been given a value, or even a form.**

## G. And that explains the collision better than the collision explains itself

**`Paper_056` did not choose the commitment budget over the other two. It used the only one that had ever been quantified.**

That reframes §§A–D above. The wall's 175–250 kDa figure does not rest on a judgement that commitment binds for matter-wave platforms. **It rests on commitment being the only constituent with a formula**, and nobody noticing that this is a different thing from it being the binding one. *The collision was not a disagreement between papers. It was two papers filling a gap in opposite directions and neither of them seeing the gap.*

**This is also why nothing downstream caught it.** A check can compare two numbers. It cannot notice that two of three quantities were never defined, because there is nothing to compare them against.

## H. ⚠ A correction to Addendum 1 §B, which was too confident

Addendum 1 said `Paper_056` §6's B/C mapping *“is the one that matches the class names both papers share”*, reading redundancy as commitment-suppression and rigidity as cross-bandwidth. **`Paper_059` gives a coherent account on the other side, and I had not read it when I wrote that:**

> *“EC encodes logical qubits across multiple physical qubits with redundancy. At substrate level, this increases the `N_V5` budget by spreading correlations across more physical chains — Class C (`N_V5`-bound) is favored.”*

**Redundancy spreading correlations across chains is a cross-chain-correlation story, which is `N_V5`, which is `Paper_053`'s Class C.** That reading is at least as natural as mine and possibly more so. **The split is 3 papers to 1** — `053`, `055` and `059` on one mapping, `056` §6 alone on the other. **My claim that the names track `Paper_056`'s physics is withdrawn**; the names are compatible with both readings, and the weight of the arc is against the one I favoured.

*Resolution (4) is not withdrawn — its core is the two-trichotomies diagnosis (§C), which stands independently. What is withdrawn is the supporting argument that `056`'s lever mapping is the physically correct one.*

## I. What this means for the wall, plainly

- **The 175–250 kDa number rests on one budget out of three, chosen because it was the only one with a formula, with no check that it is the binding one — and no way to check until the other two are defined.**
- **The three-paper rewrite is premature.** There is nothing to rewrite *toward* while two constituents are undefined. Resolution (4) would have `Paper_056` use `min{·}`, and `min{·}` is not currently computable.
- **The sign question and the `Γ_commit` form question are both downstream of the same gap** and stay parked.
- **Untouched, and now clearly the arc's best asset: architecture-independence.** It is a claim that *one* cap governs several platform types. **It does not require knowing which constituent binds, or its value.** Of everything in this arc it is the only part that survives §F intact.

## J. The one thing that would unblock all of it

**Give `N_bw` a definition.** It is the constituent `Paper_053`/`055` assign to Class A, it is the one a matter-wave wall would actually need, and P04 is the most concrete of the three primitives involved (bandwidth is non-negative and additive, which is a strong starting constraint). **With `N_bw` defined, the estimate becomes possible, `min{·}` becomes computable, and the choice between resolutions stops being a judgement call and becomes arithmetic.**

*Until then this arc's number is not defensible and its structure is not decidable, while its architecture-independence claim remains clean. That is the honest state.*
