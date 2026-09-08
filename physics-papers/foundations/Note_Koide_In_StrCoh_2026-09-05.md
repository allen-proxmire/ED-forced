# Koide's `Q` is `Str/(Str + Coh)` — a re-expression, not a derivation

*Foundations working note, 2026-09-05 (late). Written after AP brought an external conversation reading Koide through ED. **Tier: observation. Arc M's standing verdict is that this class of relation is not derivable from ED primitives, and nothing here changes that.***

---

> ## ⚠ POINTER ADDED 2026-09-07 (late) — further work exists, and it is UNTIERED

> **A separate session took this line further. Its material is now in the working repo at `event-density/theory/Koide_Hierarchy/` (ten notes, ten probes, README).** **NOTHING in it has been tiered, promoted, or propagated. AP tiers it.** *It is recorded here only so this note is not read as the current state.*
>
> **What it adds, flatly:** with `b = √m`, **`M_eff = 1/Q`** to `2.2e-16` — so `Q = 2/3` ⇺ `M_eff/N = 1/2`, the leptons at **exactly half-saturation of `M_eff ≤ N`**, the Cauchy–Schwarz bound proved independently the same evening. *That converges with §1 of this note from the other direction — `Str + Coh = (Σ√m)²`, so `Q = Str/(Str+Coh) = 1/M_eff` is the same algebra reached twice.* **And it matters more than it did on 2026-09-05, because `M_eff` gained a governing postulate that evening (`P-Multiplicity-Extensive`, `q-compute/Paper_054` §3.1).**
>
> **Its own deflation, which travels with it:** `Q ∈ [1/3, 1]`, so `2/3` is also just the midpoint. **Half-saturation and midpoint-of-range are one fact in two costumes.** *The reframe that session reached: `2/3` is deflatable, **the spread is not**, and explaining the spread is the flavour hierarchy problem at full size.*
>
> **⚠ PRIOR-ART OBLIGATION, live now.** **Rousselle, arXiv:2608.19277 (18 Aug 2026)** derives `Q = 2/3` from a `U(3) → U(1) × ℤ₃` topological condensation — **three weeks before this note was written.** *If the `Str`/`Coh` or `M_eff` reading is ever written up, it must be cited.* **Unresolved:** whether his `θ_F = −2/9` is independently forced or chosen to land `2/3` — the same test the `1/(2π)` failed.
>
> **And §4's verdict is unchanged.** Arc Q's *“ED forces exactly 3 generations — REFUTED”* stands, and neither ED nor Rousselle derives three (**he assumes `ℤ₃`**). *What is worth re-examining is arc M's stated REASON — “ED produces dichotomies, not continuous numerical relationships” — since `Q = 1/M_eff` at half-saturation of an integer bound is a continuous number out of a counting structure. **The reason, not the verdict.***

---

## 1. The observation

Write the lepton masses as participation amplitudes in the decomposition settled today (`foundations/Note_SigmaC_SignCheck_2026-09-05.md`): `P_i = √m_i`, so `m_i = |P_i|²`.

$$\mathrm{Str}=\sum_i m_i \quad(\text{the diagonal}),\qquad \mathrm{Coh}=2\!\!\sum_{i<j}\!\sqrt{m_i m_j}\,\cos\Theta_{ij}\quad(\text{the off-diagonal}).$$

Koide's denominator is `(Σ√m_i)² = |Σ P_i|² = Str + Coh` **with every `cos Θ_ij = 1`.** So

$$\boxed{\;Q=\frac{\sum_i m_i}{\big(\sum_i\sqrt{m_i}\big)^2}=\frac{\mathrm{Str}}{\mathrm{Str}+\mathrm{Coh}}\;}$$

and

$$Q=\tfrac23 \iff \mathrm{Coh}=\tfrac12\,\mathrm{Str} \iff \Sigma_C=\mathrm{Coh}-\mathrm{Str}=-\tfrac12\,\mathrm{Str}.$$

**Checked against PDG values:** `Str = 1883.029`, `Coh = 941.541`, `Coh/Str = 0.500014` against a target of `0.5`; `Q = 0.66666051` against `2/3`. That is Koide's known precision, restated.

## 2. What is and is not being claimed

**Is:** Koide's ratio is *the same diagonal/off-diagonal split* that P12's `Str` and `Coh` carry, and the empirical `2/3` is *the same statement* as `Coh = Str/2`. **That is an algebraic re-expression and it is exact.**

**Is not:** any derivation. **Nothing in ED predicts `Coh = Str/2` for the charged leptons**, and writing a known relation in ED's notation is not evidence for ED. **`Paper_030`'s own history is the caution here** — a relation restated in substrate language read as a result for months before the prior art was checked (`Paper_029` §1.2.1).

**And the corpus already ruled on this class.** `../event-density/arcs/arc-M/mass_ratio_constraints.md` §6.3, on `main`:

> *"**Koide-relation-style formulae** (`m_e + m_μ + m_τ` relationships): **not derivable from ED primitives at this stage.** … **Generation-count predictions (3 generations): not derivable.** … These are Arc Q + empirical territory, **possibly never structurally derivable.**"*

with a principled reason, not a shrug:

> *"Mass ratios are … continuous numerical quantities, not dichotomies. **ED's primitive structure produces classifications and dichotomies cleanly, but does not produce continuous numerical relationships.**"*

**That verdict stands and this note does not touch it.**

## 3. The one thing that is genuinely new, and its honest weight

**Koide's denominator sets every `cos Θ_ij = 1`.** In ED's decomposition that is not a convention — `Coh` carries explicit phases, and the fully-constructive case is a *special* configuration, not the generic one.

**So the ED-language reading of Koide's exactness is: the three charged-lepton amplitudes are fully phase-aligned.** That is a statement, it is checkable in principle, and it connects to `Paper_PhaseCoherence_P12Coh`'s measured result that `Coh` rewards alignment.

**Its weight, stated plainly: low.** Koide's formula has no phases in it, so "the phases are aligned" is what you get by *assuming* the amplitudes are real and positive — which `√m_i` is by construction. **The alignment is an artifact of taking a positive square root, not a physical finding.** Recording the connection is worth it; treating it as support is not.

## 4. Where the external reading conflicts with the corpus

The conversation that prompted this rests on **mass = consumption of commitment bandwidth = the particle's clock rate** (`ω = mc²/ħ` read literally as a commitment rate).

**ED measured that and separated them.** `substrate-evaluation/Paper_MassWithoutMass_BindingInertia` §5 puts a boxed conclusion on a simulator run:

> *"**So the commitment rate and mass are different phenomena.** The commitment/sparseness rate governs the **clock rate**, which is **time dilation** … while **mass is a separate thing that comes from binding.**"*

The measurement behind it: a commitment-memory front dwells, but its forward drift **tracks its path speed exactly** — `v_x/path = 1.00` at every memory level, i.e. **no directional inertia**. A *bound* composite under the same force drifts at `0.72` against an unbound cluster's `0.97`. **Bandwidth-consumption-by-dwelling produces a slow clock and no mass; binding produces mass.**

**So the external reading's central identification is the one ED tested and rejected.** It is a faithful development of the premise it was given; the premise is what the corpus contradicts.

---

*Gravity ledger Staleness #81. Companions: `arcs/arc-M/mass_ratio_constraints.md` §6.3 (working repo, `main`), `substrate-evaluation/Paper_MassWithoutMass_BindingInertia` §5, `foundations/Note_SigmaC_SignCheck_2026-09-05.md`.*
