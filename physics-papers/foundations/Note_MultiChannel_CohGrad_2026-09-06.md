# The `Coh`-vs-`Grad` comparison was never actually being run — the probe's `Coh` arm was a normalization of `Grad`

**Date:** 2026-09-06
**Status:** **Structural finding**, plus a first multi-channel run whose numbers are new data rather than a comparison.
**Probe:** `../event-density/theory/p12_multichannel_coh_grad_probe.py` (new, re-runnable).
**Follows:** `Note_GradPhase_Decomposed_2026-09-06.md` (#103), which named "multiple channels per locus" as what a discriminating probe needs.

---

## 1. Writing both formulas out makes the difference exact

Per channel `K`, with `v`'s own contribution included and neighbours transported by the P05 connection:

$$\mathrm{Coh}(v)=\sum_K\Big[\big|P_K(v)+\textstyle\sum_w P_K(w)e^{iA}\big|^2-\big(b_K(v)+\sum_w b_K(w)\big)\Big]$$
$$=2\sum_K\Big[\underbrace{\textstyle\sum_w\sqrt{b_vb_w}\cos\Delta\pi_{vw}}_{\text{v–neighbour}}+\underbrace{\textstyle\sum_{w<w'}\sqrt{b_wb_{w'}}\cos\Delta\pi_{ww'}}_{\textbf{neighbour–neighbour}}\Big]$$

$$-\mathrm{Grad}(v)=-\sum_K\sum_w\big|P_K(v)-P_K(w)e^{iA}\big|^2=2\sum_K\sum_w\sqrt{b_vb_w}\cos\Delta\pi_{vw}\;-\;\text{const}$$

$$\boxed{\;\mathrm{Coh}=-\mathrm{Grad}+2\,\mathrm{NN}+\text{const}\;}$$

**The two terms differ by exactly one object: the neighbour–neighbour cross term.** And the asymmetry is structural, not incidental — **a Dirichlet form only ever compares `v` to a neighbour, never two neighbours to each other.** `Coh` interferes *every* pair of contributions; `Grad` cannot.

## 2. The finding: the earlier probe's `Coh` arm was not `Coh`

`p12_phase_in_grad_probe.py`'s own docstring:

> `v3_active` (**Coh reading**, INTENSIVE): `bonus = |acc| / n`
> this probe (**Grad reading**, EXTENSIVE): `bonus = |acc|`
> … **the substantive difference is precisely the `/n` normalisation.**

**`|acc|` is correct for `Grad`** — maximizing the Dirichlet form over `v`'s free phase gives exactly `2|acc|`.

**`|acc|/n` is not `Coh`.** It is the simulator's `v3_active` per-locus-average convention. Canonical `Coh` maximized over `v`'s phase gives `2|acc|` **plus the neighbour–neighbour term** — and `|acc|/n` contains no such term. It is `Grad` divided by the coordination number.

> **So the comparison being run was `Grad` against `Grad/n`. The `Coh`-versus-`Grad` question was never actually being asked.**

**That explains all three dead ends at once.** Knots-safety drew because both arms were the same functional. The `ξ` trend was a coordination-number artifact (#103) because **`/n` *is* the coordination number** — that was the only difference between the arms. And no tuning helped, because there was nothing to tune toward.

**This is the failure mode the corpus already names**: testing a hand-built stand-in rather than the thing itself. It sat undetected because the stand-in had a plausible name.

## 3. The multi-channel run — new data, not a comparison

Both formulas implemented as written, 40×40, 3 channels per locus, single seed:

| condition | `Coh` (keeps NN) | `Grad` (no NN) | NN share |
|---|---|---|---|
| **(A)** bandwidth holonomy only, `k=1→8` | `R≈0.96–0.98`, `ξ=30` → **crystal** | `R≈0.87–0.98`, `ξ=30` → **crystal** | 0.39–0.41 |
| **(C)** physical, `k=1→8` | `R≈0.01–0.03`, `ξ≈0.7` → finite | `R≈0.02–0.03`, `ξ≈0.6–0.9` → finite | 0.29–0.33 |

**Two things worth reporting and one caveat that outweighs them.**

- **The NN term is not negligible** — it carries **29–41%** of the phase score. `Coh` and `Grad` are genuinely different objects numerically, not just notationally.
- **They nevertheless give the same verdict in every condition tested.** Different in magnitude, same in behaviour.

**The caveat:** this run **cannot be compared to the earlier one**, because the earlier one was testing a different functional (§2), and because this probe also changed the grid size and added per-channel quenched bandwidth. **Its verdicts are a fresh baseline, not a resolution**, and `ξ ≈ 0.7` in condition (C) is far shorter than anything previously measured — which may be the extra per-channel disorder rather than anything about the terms. **Single seed, one grid size. Do not build on these numbers.**

## 4. Status

**What is established:** the algebra of §1, which needs no probe — `Coh` and `Grad` differ by the neighbour–neighbour cross term and by nothing else. And §2, which is a fact about the earlier probe's source code.

**What is not:** which term owns the July phase-alignment measurement. **That question is now genuinely open for the first time** — previously it was open *and* mis-specified.

> **✅ ANSWERED 2026-09-06 (#111): it belongs to `Grad`.** Binding needs **two** conditions — **intensive scoring** *and* **no neighbour–neighbour term** — and only `Grad` can meet both. **`|acc|/n` is intensive `Grad`** (`Grad` maximised over `v`'s phase is `2|acc|`; the `2` absorbs into `k_phase`), so the arm that binds is not “neither term” but **`Grad` in a normalized scoring convention.** **Intensive canonical `Coh` has nearly flat connection and NO alignment gain** (residual `−1.17…−0.68` against the control's `−1.02`), because **the NN term does not contain `v`'s own phase** (#105) and so rewards already-coherent neighbourhoods rather than alignment. `foundations/Note_RepairTest_2026-09-06.md`.

**What `Grad`'s tier does:** unchanged. Still a proposal, `form-forced-conditional at best`. Its known problem — condition (A) crystallizing — **now appears under *both* readings in this probe**, which neither confirms nor clears it, since the probe is unvalidated.

**Next, and it is cheap:** re-run the *original* single-phase probe with its `Coh` arm corrected to `|acc|² − n` (canonical) rather than `|acc|/n`. That is a two-line change, it reproduces the validated baseline everywhere else, and it is the first run that would actually be asking the question.
