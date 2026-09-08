# The `b`-assignment for a charged lepton — the map exists, I said it didn't, and its defining property kills both Koide readings

**2026-09-08.** AP: *do the b-assignment for a charged lepton.* **Done, and the answer required correcting my own claim first.**

---

## 1. ⚠ CORRECTION, and it is the kind `CLAUDE.md` exists to prevent

**Foundations ledger #13, Target #16's new instance, `arc-Q` §4.4.1 and three other sites all say some version of:**

> ~~*"No `b ↔ mass` map exists anywhere in the corpus."*~~

**That is FALSE, and the way it went wrong is the textbook shape.** I searched `physics-papers/foundations/` and `physics-papers/substrate-evaluation/`, found nothing, and **stated a corpus-wide negative from a two-folder search.** *`CLAUDE.md`: "Assume a paper already exists until you have confirmed it does not."* **I confirmed absence in two folders and reported absence everywhere.**

**The map is in `../event-density/arcs/`, which I never searched.** It has been there since Arc M.

> ## `arc-foundations/bandwidth_signature_construction.md` (Stage M.1.1), eq (4):
>
> $$\sigma_\tau = \hbar\sqrt{\;\sum_X w_\tau^X\,\big\langle(\partial\ln b^X)^2\big\rangle_\tau\;},\qquad\qquad m_\tau=\sigma_\tau/c^2$$
>
> **"Lorentz-scalar form is FORCED."** Four-band-additive, built directly out of P04 bandwidth content.

*This does not change any tiering verdict reached yesterday. It changes the **reason**, and the corrected reason is stronger.*

---

## 2. The answer: `b` for a charged lepton is not a number, and cannot be

**The map's defining design choice is stated in its own §3.3.** The logarithmic derivative is chosen because it is

> *"**invariant under overall rescaling of `b`** (which is chain-specific initial-condition data, not rule-type-structural) … it localises the spectral content of `b^X` to its **structural rate of variation, not its amplitude**."*

**Verified** (`theory/Koide_Hierarchy/b_assignment_for_a_lepton.py`, re-runnable):

| test | result |
|---|---|
| `b → λb` for `λ = 1, 3, 10³, 10⁻⁶` | `σ = 0.2621018210` **every time.** Exact: `∂ln(λb) = ∂ln b`. |
| same variation profile, `b` amplitudes `10⁶` apart | **same mass**, to all digits |
| **same `b` amplitude, variation rate ×0.5 / ×1 / ×2 / ×4** | `m = 0.132 / 0.262 / 0.524 / 1.061` — **mass tracks the rate, not the amount** |

> ### So the honest assignment is: **`m` is a functional of `b`'s log-derivative profile over the chain's history, not a function of `b`'s value.**
>
> **There is no number `b` for an electron that yields `m_e`.** *Asking "what is `b` for a charged lepton" presupposes a pointwise map the corpus deliberately does not have — and the deliberateness is the point: amplitude is chain-initial-condition data, mass is rule-type-structural, and eq (4) is built to separate them.*

---

## 3. This upgrades the Koide verdict from *unlicensed* to *incompatible*

Both readings needed a pointwise `b ↔ m`: `Note_Koide_In_StrCoh` takes **`b = m`**, `koide_is_Meff_check` takes **`b = √m`**.

**Eq (4) rules out that entire class in one line.** `σ` is invariant under `b → λb`; `m` is not invariant under `m → λm`. **So no `f` with `b = f(m)` evaluated on `b`'s value can reproduce the corpus map** — rescale `b` and `f(m)` must move while `m` stays put.

> **Yesterday's verdict said `b = m` and `b = √m` are *unlicensed*. The correct statement is that they are *incompatible with a form-FORCED result the corpus already holds*.** *Stronger, and it does not depend on the absence of evidence I wrongly asserted.*

**And it explains the measured separation** in `Paper_MassWithoutMass_BindingInertia` (*"commitment rate and mass are different phenomena"*) rather than merely agreeing with it: **participation amount and mass are separated in eq (4) by construction.**

---

## 4. What a specific lepton would still need — and one of the two is already refuted

Eq (4)'s **form** is forced. Its **inputs** are not, and the construction says so itself:

| input | status, per M.1.1 §4.2 |
|---|---|
| the functional form (4) | **FORCED** — bandwidth signature is a weighted sum of band spectral-rate squares |
| `w_τ^X ≥ 0`, `Σ_X w_τ^X = 1` | **FORCED by P04** |
| **the actual `w_τ^X` for a given rule-type** | **INHERITED.** *"ED structure does not pick out a specific point in the `(w^int, w^adj, w^env, w^com)`-simplex."* |
| the spectral-rate average `⟨(∂ln b^X)²⟩` | **CANDIDATE** — log-derivative is motivated, not uniquely forced |

**So the gap for a charged lepton is precise: the band-partition point in the simplex, plus the confirmation that the log-derivative average is the right invariant.** *That is a much sharper statement of Target #16 at the lepton than "assign `b`".*

### ⚠ And the ratio question is already closed, negatively

**`arc-M/mass_ratio_constraints.md` is, in its own words, "the cleanest negative-result memo of Arc M."** Six strong ratio claims tested, and the relevant one is exact:

> **`R3-E`: *"`σ_τ` determined by `w`-pattern"* — REFUTED as ratio predictor.** *(A weak ordering candidate `M-Order-2` survives.)*

**Koide is a statement about mass RATIOS.** *So even a complete band-partition assignment for all three leptons would not deliver it — the route from `w`-patterns to ratios was tested and refuted before this line began.* **Three weak inequalities survive; they give orderings, not numbers.**

---

## 5. Net

| question | answer |
|---|---|
| does the corpus have a `b → mass` map? | **YES** — eq (4), form-FORCED, since Arc M. *My claim that it does not was a two-folder search reported as corpus-wide.* |
| what is `b` for a charged lepton? | **The question is malformed.** `m` depends on `b`'s **rate of variation**, and is **exactly invariant** under `b`'s amplitude. |
| are `b = m` / `b = √m` licensed? | **Worse than unlicensed: incompatible** with eq (4)'s amplitude-invariance. |
| what would a lepton still need? | the **inherited** band-partition point `w_τ^X`, and confirmation of the **candidate** log-derivative average |
| would that give Koide? | **No.** `R3-E` refuted `w`-pattern → ratios, and Koide is a ratio statement. |

> **The `Open` item as I wrote it ("assign `b` for a charged lepton") should be REPLACED, not merely updated.** *It named a gap that does not exist in that form.* **The real open item is `arc-M`'s own: the band-partition simplex point is inherited, and `M.1.4`'s per-rule-type identity was judged "less informative" precisely because `M.1.3` had already refuted the comparative content.**

**Which means the flavour line closes one step earlier than yesterday's account had it, and for a better reason: not "ED lacks the ingredient," but "ED has the map, the map is amplitude-blind, and the ratio route off it was refuted in Arc M."**

*Probe: `theory/Koide_Hierarchy/b_assignment_for_a_lepton.py`. Sources: `arc-foundations/bandwidth_signature_construction.md` §3.3–§4.2; `arc-M/mass_ratio_constraints.md`; `arc-M/chain_mass_synthesis.md`.*
