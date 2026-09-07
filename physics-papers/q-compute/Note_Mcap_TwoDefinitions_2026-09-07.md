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
