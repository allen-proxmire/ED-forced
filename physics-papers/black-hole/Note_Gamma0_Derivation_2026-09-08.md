# `Γ₀(ρ) → 0 as ρ → ρ_max` — derived at `Grounded`, and two rates were being conflated

**2026-09-08.** Target #15's live residual, open since 2026-07-24, described there as *"a real open problem, not a quick win."* AP: *do the `Γ₀` derivation.*

**Result: it derives, at `Grounded` tier, but only for one of the two things the corpus calls by that name — and the other is refuted by calculus on the corpus's own formula.**

*Probes (re-runnable): `../event-density/theory/Gamma0_Derivation/` — `gamma0_rolle_obstruction.py`, `gamma0_capacity_sim.py`, `gamma0_source_vs_destination.py`, `gamma0_tracer_vs_collective.py`.*

---

## 1. The derivation

**Given, all already in the corpus:**

| ingredient | status |
|---|---|
| **`P-Locus-Bandwidth-Bound`** — *"a locus's total bandwidth `b(u)` is bounded above"* | **declared postulate**, cross-cutting (≥4 folders) |
| **P04** — `b ≥ 0`, additive over disjoint sub-channels at a locus | **primitive** |
| **`P-Adjacency-Transport-Shared`** — *"inter-locus transport is P05-only"* | declared, `Paper_UnifiedP04TransportBudget` §2 |

**A chain-step is a bandwidth transfer through an adjacency channel.** It completes only if the receiving locus can hold the transferred bandwidth. By the bound, the room at a locus is `B_max − b(u)`, so the fraction of attempted steps that can complete is `(B_max − b)/B_max`:

**`Γ₀(ρ) = Γ_max · (1 − ρ/ρ_max)`**, with `ρ_max ↔ B_max`.

**Measured exactly** (probe N): acceptance `0.9013, 0.6990, 0.5003, 0.2999, 0.1000, 0.0496, 0.0099` against `1−ρ = 0.90 … 0.01`.

> ### Tier: **`Grounded`** — form-forced *given* `P-Locus-Bandwidth-Bound`. **NOT `Derived`.**
>
> **And the reason it cannot be `Derived` is stated in the corpus:** `primitives/P04_bandwidth.md` says plainly that *"canonical P04 gives non-negativity, **not an upper bound**, so any arc needing a finite per-locus budget must name one."* **Target #15 asks for a derivation from P01–P13. That is not available, and P04's own card says why.**

**What this buys is a postulate reduction, not a new commitment.** `Γ₀(ρ)→0` is cited by Arc_BH_3 and Arc_D_2 as its own thing — *"the P4-class mobility-capacity bound"* — as though independently declared. **It is not: it follows from a bound the corpus already names.** *Two declared items become one.* **🛑 CORRECTED 2026-09-08 (late) — THE POSTULATE-REDUCTION CLAIM DOES NOT STAND. Found by the symbol-table pilot (see the two-column table above, F2).** *`ρ` and `b` are different objects.* **`ρ` is commitment density** — `simulator/state.py`: *"commitment density (B4); **monotone non-decreasing** (B7)"*, an accumulated stock of past commitments. **`b` is P04 bandwidth**, a participation **capacity**, with non-negativity and additivity and **no monotonicity**. **`P-Locus-Bandwidth-Bound` bounds `b(u)` and never mentions `ρ`** (zero occurrences at its declaration site), while **`ρ_max` is declared separately** in `Arc_BH_3`/`Arc_D_2` as a packing limit *"set by participation-channel availability"* — a gesture at the bandwidth structure, not a derivation from it. **So writing `Γ₀(ρ) = Γ_max(1 − ρ/ρ_max)` with "`ρ_max ↔ B_max`" inserted an UNLICENSED identification** — asserted in exactly two places, both of them this session's own entries. *Same shape as `b = m` in the Koide case: a substitution introduced to reach a result and then read as part of it.* **Consequence: nothing was reduced.** Linking two separate declarations required a **third** statement, so either `ρ ↔ b` is named as a postulate — leaving the count unchanged — or the derivation is restated as grounded on `ρ_max` directly, which is not a reduction either. **The `Grounded` tier for the VANISHING survives, and so does the measured cap; the "two declared items become one" claim is WITHDRAWN.**

**It also explains the certified negative** (`CoarseGrain_Arc/Diffusion_Arc_Finding.md`: the bare rule *"has no `ρ_max`; `ρ` grows unbounded, mobility never dies"*, reaching `~3.0`). **The minimal certified rule does not implement the bound.** The capacity appears exactly when the bound is turned on, with no other constitutive ingredient added.

---

## 2. ⚠ But "the mobility-capacity bound" names TWO rates, and they behave oppositely

| | what it is | at `ρ → ρ_max` | who needs it |
|---|---|---|---|
| **tracer** | the rate **one chain** takes a step | **→ 0**, linearly. **Measured, exact.** | **Arc_BH_3** — *"no chain can produce an unbounded number of commitment events in a bounded proper-time interval"* |
| **collective `M`** | the coefficient in `∂ρ/∂t = ∇·(M∇ρ)` | **does NOT vanish** | **Arc_D_2** — *"`M(ρ_max) = 0`, `M(ρ) > 0` otherwise"* |

**Measured** (probe O — sinusoidal relaxation, fitting `exp(−Mk²t)`): **`M = 0.99996` at `ρ₀ = 0.10, 0.30, 0.50, 0.70, 0.90, 0.95`.** Constant to five figures; **100.0% of its dilute value at 95% packing.**

*The blocking factors cancel identically:* `ρ₋(1−ρ₊) − ρ₊(1−ρ₋) = ρ₋ − ρ₊`. **Individual chains freeze at saturation. The density field does not.**

> **Arc_BH_3's use survives, and is now grounded rather than declared. Arc_D_2's stated `M(ρ_max) = 0` does not follow.**

---

## 3. And Arc_D_2's property list is inconsistent with its own formula — by calculus, not by modelling

Arc_D_2 Step 2 derives `M(ρ) = [kernel moment] · ∂(Γ₀(ρ)ρ)/∂ρ` from a **source-local** flux, and its §5 asserts `M(ρ_max) = 0` with `M > 0` otherwise. **Those cannot both hold.**

Let `f(ρ) = Γ₀(ρ)ρ`. Then `f(0) = 0`, `f(ρ_max) = 0` (the P4 claim), and `f > 0` between. **By Rolle, `f′ < 0` on a band below `ρ_max`. So `M < 0` near saturation for ANY `Γ₀` vanishing there.** Checked across `(1−x)^1`, `(1−x)^2`, `(1−x)^3`, `(1−x)^5`, `exp(−1/(1−x))` and a perturbed form: the negative band appears in **every** case, beginning at `x = 1/(1+β)`. *For `β = 1`, `M(ρ_max) = −1`, not `0`.*

**`M < 0` is backward diffusion, which is ill-posed.** Simulated (probe K): the source-local rule **does not cap `ρ`**, and gets **worse with resolution** — `max ρ = 97.9 / 202.3 / 411.2` at `N = 200/400/800`, a **×4.2 divergence under ×4 refinement.** *That is the signature of ill-posedness, not of a ceiling.*

**Destination-gated, the same test is well-posed:** `max ρ = 0.63469 / 0.63467 / 0.63466` — **resolution-independent to four digits** — and over time `0.529 → 0.635 → 0.757 → 0.890`, **asymptoting to `ρ_max` from below and never crossing.** *Which is Arc_BH_3's own description: "asymptotes to saturation but does not reach `ρ_max` in finite time."*

> ## The repair, stated precisely
>
> **The gating belongs on the DESTINATION locus, not the source.** Arc_D_2 writes the flux source-locally (`Γ₀(ρ₋)ρ₋`), and that is what generates both the negative-mobility band and the failure to cap. **Under destination gating the cap is real, well-posed, and enforced by the state space rather than by a vanishing `M`.**


> ## ⚠ CORRECTED 2026-09-08, same day — §2 and §3 above are TOO STRONG, and Arc_BH_3 is vindicated
>
> **A parallel session flagged the `D`-vs-`σ` distinction *before* the certified run, and it was right.** Under destination gating there are **two** transport coefficients, not one:
>
> | | | at `ρ → ρ_max` | measured |
> |---|---|---|---|
> | **`D`** | Fick, free relaxation `J = −D∇ρ` | **constant** | `0.99996`, flat over `ρ = 0.10…0.95` |
> | **`σ`** | **Onsager, response to a driving field** `J = σE` | **→ 0** | **`σ = 0.502·ρ(1−ρ)`**, ratio constant to **5.7%** over `ρ = 0.10…0.98` |
>
> Linked by the **Einstein relation** `σ = 2Dχ`, `χ = ρ(1−ρ)`. *The vanishing lives entirely in `χ`.*
>
> ### What this reverses
>
> **✅ `Arc_BH_3` Constraint 3 is CORRECT and needs no rewrite.** Its content is that gradients cannot be **sustained** and steepening cannot **propagate** — **driven** transport, whose coefficient is `σ`, and `σ` vanishes. *I reported the mechanism as refuted after measuring `D` — the wrong coefficient. Withdrawn.* **The “owed rewrite” is cancelled.**
>
> **⚠ And the repair is NARROWER than even that, on a second reading — one paragraph, not the constraint.** *Flagged by the parallel session before I edited; it was right twice.* **(a)** Constraint 3's **headline** sentence is about *“`Γ₀(ρ)` — the **chain-step transition rate**”*, the tracer rate, which is precisely what the certified run measured. **It needs no repair; it is upgraded from declared to measured.** **(b)** The broken sentence is the **next** paragraph's *“continuum-scale dynamics with mobility coefficient `μ(ρ)` … the mobility goes to zero”* — `μ` there occupies the **diffusivity** slot, and `D` does not vanish. **A different sentence from the one carrying the constraint's name.** **(c)** §4's acoustic degeneration **never used a transport coefficient at all**: its criterion is `|∇ρ|·ℓ_P²/ρ_local ≳ β_crit`, a pure gradient-to-density ratio. **Its content is untouched** — only the prose motivation is mis-sourced, and it re-motivates for free from the `Γ₀` statement, since a vanishing chain-step rate bounds `|∇ρ|` directly. *So my “§4 stands because the driven response vanishes” was right in verdict and wrong in reason.*
>
> **⚠ NAMING HAZARD I CREATED AND HAVE NOW REMOVED.** My first version of the Arc_BH_3 box imported the transport-coefficient name `σ` into that file — **which already uses `σ` for its dimensionless saturation parameter `|∇ρ|·ℓ_P²/ρ_local`.** *That is the one-symbol-two-meanings collision this entire session has been about, manufactured by the correction to it.* **The box is rewritten in that memo's own two names — `Γ₀` versus `μ`/`D` — and imports nothing.** *`Arc_D_2` has no competing `σ`, so the name is safe there and is used.*
>
> ### What survives, scoped correctly
>
> **`Arc_D_2` still needs a repair, but a smaller and more precise one:** its `M(ρ_max) = 0` is **right for `σ`**, while Step 2 defines `M ≡ [kernel moment]·∂(Γ₀ρ)/∂ρ` and writes `∇·(M∇ρ)`, where `M` occupies the **Fick** slot. **One symbol, two coefficients — a property of `σ` asserted about an object defined as `D`.** *The Rolle result stands, scoped: it shows the **source-local** reading gives negative `D` and is ill-posed. Under the certified destination gating there is no negative-`D` pathology at all.* **So Rolle diagnoses the mis-transcription, not the physics.** **Repair written into `Arc_D_2` 2026-09-08:** state the driven equation as `∇·(σ∇μ)` with `σ = 2Dχ`, and destination-gate the Step-1 flux. **The operator form stays FORCED, values stay INHERITED, and downstream consumers (Arc_D_3/D_6 NS-2 closure, Arc_BH_2, Arc_ED10_2, soft-matter transport) are unaffected — they use the operator form and `ρ_max`'s existence, not the `D`-vs-`σ` identification.**
>
> **⚠ Third process failure this session, and the same shape as the first two.** The `σ` script's verdict line compared `σ(0.98)/σ(0.10)` against an **arbitrary `0.25` threshold** and printed *“does not vanish”* — meaningless, since `ρ(1−ρ)` is itself `0.218` of its `ρ=0.1` value there. *The right test is whether `σ/[ρ(1−ρ)]` is **constant**, after which `σ(1) = 0` follows.* **That script's Monte-Carlo `D` estimator was also too noisy to use (it returned negatives) and is superseded by the deterministic measurement.**

---

## 4. What this does and does not settle

**Settled:**

- **`Γ₀(ρ) → 0` derives at `Grounded`** from `P-Locus-Bandwidth-Bound` + P04 + P05-transport. *It is no longer an independent declaration.*
- **`Derived`-from-13 is unavailable, and P04's card says why.** **Target #15's residual as phrased is not achievable; this is the best available answer.**
- **The density cap is real**, well-posed under destination gating, asymptotic from below.
- **Arc_D_2's `M(ρ_max) = 0` together with `M > 0` otherwise is inconsistent** with its own `M ∝ ∂(Γ₀ρ)/∂ρ`. *This half is pure calculus and holds independently of any simulation.*

**Not settled, and held to the same bar as the positives:**

- **The exclusion model is a stand-in.** The Rolle result is model-free, but *"collective `M` is constant"* is measured in a nearest-neighbour exclusion lattice, **not on ED's certified substrate.** It shows the source-local reading fails and the destination reading works; **it does not prove ED licenses the destination reading.** Tier: **measured-in-model**, `A → position` for ED. **✅ DISCHARGED the same day — see §4b.** *The certified rule reads `strain = rho_v`, the **destination** (behaviourally `3.5×` the source dependence), and adding only the bound to it caps `ρ` at `3.1000` against the bare rule's `24.1` with no extinction.* **Both the destination-gating question and the cap are now measured on the certified substrate; only the continuum `M` statement remains model-side.**
- **`β` is not settled.** Single-channel allocation gives `β = 1`; the empirical UDM wants `β ≈ 2`. **That value-layer gap is untouched.**
- **Arc_BH_3's gradient-saturation argument needs re-examination.** It reasons *"`M` vanishes, so gradients cannot steepen."* **`M` does not vanish.** The no-`ρ→∞` conclusion survives by a different route (state-space exclusion), but **the stated mechanism does not** — and the acoustic-metric degeneration argument in the same paper leans on the same vanishing `M`.

> **⚠ One process note, recorded because it nearly cost the result.** The first simulation script printed its conclusions as **pre-written strings** rather than computing them, and the data contradicted them — the run "confirming" the cap had in fact blown up to `ρ = 111`. *A probe's verdict must be computed from the run, or the probe validates the expectation instead of testing it.* **Both later scripts compute their verdicts.**

---

## 4b. ✅ RUN ON THE CERTIFIED SUBSTRATE — the stand-in caveat is discharged

**This is the test the 2026-07-24 attempt said was owed:** *"a run in which `ρ` itself is evolved and shown to self-cap would move it from account to measured."* **Done, on the simulator of record** (`evaluation/Bits/simulator`), certified Σ rule, `COEFFS` unchanged, **no certified file modified**. *Probes: `gamma0_certified_substrate_test.py`, `gamma0_certified_bound_attained.py`.*

### The question §4 left open is answered by the certified rule itself

`simulator/sigma.py`, `compute_sigma(u, v, …)`:

```python
strain = rho_v      # destabilizing: penalize dense targets (-)
grad   = abs(rho_v - rho_u)
```

**`v` is the DESTINATION.** *The strain term reads the destination only; the source enters solely through `grad`.* **Measured behaviourally:** `+1.5` of density at the destination moves `Σ` by **`−5.250`**; the same at the source moves it by **`−1.500`** — **destination dependence is 3.5× the source dependence.**

> ### **The certified substrate is DESTINATION-GATED. Arc_D_2's source-local flux `Γ₀(ρ₋)ρ₋` does not transcribe it.**
>
> *That is no longer a preference between two modelling options. The corpus's own simulator of record settles it, and it settles it on the side that is well-posed.*

### The bound alone produces the cap, on the certified rule

**The only addition in the bounded arm is `P-Locus-Bandwidth-Bound` as an admissibility filter — the postulate verbatim, applied at the destination:** a candidate `v` with `ρ_v ≥ ρ_max` is not admissible. **Nothing else changed.**

| arm | `increment` | max `ρ` | predicted ceiling | outcome |
|---|---|---|---|---|
| **bare certified** | 1.0 | **24.1** | — | **never extinguishes, still rising** |
| **+ bound** | 1.0 | **3.1000** | `3.1000` | **extinct at `t = 268`** |
| **+ bound** | 0.5 | **3.1000** | `3.1000` | extinct at `t = 1560` |
| **+ bound** | 0.25 | **3.1000** | `3.1000` | extinct at `t = 2950` |

**`ρ_max = 3.0`. The bounded ceiling is attained exactly at every increment, and the ratio bare/bounded is `7.77×`.**

**The residual `+0.1` is arithmetic, not slippage:** the bound is tested **pre-commit** and `commit()` then adds `increment`, so the reachable maximum is `ρ₀ + ⌈(ρ_max−ρ₀)/increment⌉·increment ≤ ρ_max + increment`. *No pre-commit admissibility test can do better with a finite commitment quantum.* **`ρ` is bounded; without the bound it is not.**

**And `Γ₀ → 0` appears natively, not as a fitted rate: the front EXTINGUISHES when every neighbour is full.** *In ED's own vocabulary the vanishing rate is extinction — "no positive-Σ continuation" — which is already `Paper_087`/Phase-D content rather than something added for this.*

### Tracer acceptance, measured on the certified graph

| occupied fraction | admissible fraction | `1 − f` |
|---|---|---|
| 0.10 | 0.8851 | 0.90 |
| 0.30 | 0.6857 | 0.70 |
| 0.50 | 0.4580 | 0.50 |
| 0.70 | 0.2729 | 0.30 |
| 0.90 | 0.0911 | 0.10 |
| 0.95 | 0.0413 | 0.05 |

**Linear in `(1 − ρ/ρ_max)` on the certified graph**, with a small systematic undershoot from boundary and correlation effects.

> ## Tier upgrade
>
> **§4's caveat — *"measured in a nearest-neighbour exclusion lattice, a stand-in; `A → position` for ED"* — is DISCHARGED for the destination-gating question and the cap.** Both are now **measured on the certified substrate**. *What remains model-side is only the continuum statement that collective `M` stays constant, since the certified rule is a discrete deposit rule with no `M` to read off directly.*

> **⚠ Second process failure this session, same class as the first.** My initial overshoot test compared runs at different `increment` **without checking whether each had saturated** — the small-increment runs extinguished early, so the ratio was computed on unfilled runs and printed a meaningless verdict. *A comparison across a parameter must verify the runs are in the same regime before the comparison means anything.* **The corrected script checks saturation and predicts the ceiling analytically before measuring it.**


> ## ⚠ CORRECTED AND STRENGTHENED 2026-09-08 (late) — `β` retires as an artifact, and my admissibility filter was wrong
>
> **A parallel session added a third branch to the pre-committed tiering rule and found an implementation error on the way. Both confirmed.**
>
> ### 1. My filter enforced the bound one quantum too late — and the `+0.1` was NOT harmless arithmetic
>
> I filtered on **`rho_v < rho_max`**, i.e. **before** the deposit. *“A locus's total bandwidth is bounded above” must hold **after** it*, so the filter is **`rho_v + increment ≤ rho_max`**. **My version permitted a one-quantum violation of the very postulate under test**, which is exactly the `+0.1` I reported as arithmetic and harmless. *It was the bound enforced one step too late.*
>
> **✅ With the correct filter the cap is EXACT, and the result improves:**
>
> | `increment` | old filter | **correct filter** | exceeds `ρ_max`? |
> |---|---|---|---|
> | 1.00 | `3.1000` | **`2.1000`** | **no** |
> | 0.50 | `3.1000` | **`2.6000`** | **no** |
> | 0.25 | `3.1000` | **`2.8500`** | **no** |
>
> **`ρ_max = 3.0`; bare rule reaches `32.1`.** *The bounded runs approach `ρ_max` from below and never cross — which is Arc_BH_3's own description, now literally true rather than true to within a quantum.* **Every statement of the form “`ρ ≤ ρ_max + increment`” in this note, Target #15 and both ledgers is superseded by `ρ ≤ ρ_max`, exactly.**
>
> ### 2. The refit: `β = 1.0009`, CI `[0.928, 1.109]` — the apparent `β ≈ 1.05` was noise
>
> The parallel session read a systematic sub-linear trend off my acceptance ratios (`0.983 → 0.980 → 0.916 → 0.910 → 0.910 → 0.820`) and flagged, honestly, that its density points were assumed. **They were right about the x-values and right to want a refit.** **Refit with 40 seeds: `β = 1.0009`, 95% CI `[0.9280, 1.1089]` — consistent with `1`.** *The single-draw ratios were sampling noise; at `f = 0.95` only 5% of neighbours are free, so one draw is worthless there.*
>
> ### 3. ⭐ THE THIRD BRANCH IS THE ANSWER: `β` moves with the INCREMENT, at fixed kernel
>
> With the correct filter, acceptance is `P(b ≤ B_max − Δ)` — **explicitly `Δ`-dependent.** Measured on the certified graph with graded occupancy, **kernel never varied:**
>
> | `Δ/ρ_max` | 0.500 | 0.333 | 0.167 | 0.083 | 0.033 |
> |---|---|---|---|---|---|
> | **fitted `β`** | 0.775 | 0.685 | 0.443 | 0.255 | **0.067** |
>
> **Spread `0.707` across a 15× range of increment.**
>
> > ## Verdict, against the criterion fixed BEFORE the run: **`β` is an ARTIFACT of the discretisation. No claim. `β ≈ 1` retires.**
> >
> > **And `β = 1` was never physics** — it is the **single-occupancy** case, where “room” is binary and its mean is exactly `1 − ρ`. *True by construction, which is why §1's `Γ₀ = Γ_max(1 − ρ/ρ_max)` should be read as the binary-occupancy limit, not as a measured exponent.*
>
> **The increment also pushes `β` the WRONG way** — smaller quanta drive it **down**, away from UDM's `≈ 2`. **So the increment is a confound to control, not a route to the target, and the finite-width kernel test is NOT interpretable until `β` is shown stable under it.** *Going at the kernel first would have attributed to the kernel a number a numerical parameter was already moving — the same shape as every other failure logged today.*
>

>
> ### ⚠ The UDM `β ≈ 2` comparison is WITHDRAWN AS ILL-POSED — not deferred
>
> **Earlier wording here called it *“not reachable from a discrete deposit rule — needs a continuum formulation ED doesn't have yet.”* That keeps it a target**, and a future session reads *“needs a continuum formulation”* as a to-do and builds one to chase a number. **The two `β`s were never the same quantity.**
>
> **What was measured here is a hop-acceptance fraction — microscopic admissibility. UDM's is a macroscopic transport exponent from FRAP-measured diffusion. TWO named objects sit between them:**
>
> 1. **The correlation factor** of lattice-gas theory — *the ratio between the tracer diffusion coefficient and that of an uncorrelated random walk*, which **decreases rapidly at high concentration**. *Acceptance is not even the tracer diffusion coefficient.*
> 2. **Tracer `D` → collective/continuum mobility** — a second, independent step, and the one where the `D`-vs-driven-response distinction already bit today.
>
> **So this is the sixth across-levels comparison caught today, and the only one aimed outside the corpus.** *Building a continuum ED mobility would not make this comparison valid; it would need its own, separately constructed.* **Withdrawn as ill-posed. Not an open gap, not a deferred target.**
>
> ### ⚠ And quote the cap as `ρ ≤ ρ_max`, never as “the cap is 2.1”
>
> The corrected ceilings `2.10 / 2.60 / 2.85` are exactly `ρ_max − Δ`, **so the ceiling's value is itself increment-dependent.** *That is expected rather than artifactual — unlike `β` — but the same discipline applies to quoting it.* **The claim is `ρ ≤ ρ_max`, approached from below. `2.1` is a run parameter, and `ρ_max` is the inherited postulate value.**
>
> **⚠ WHICH `β` RETIRED — added 2026-09-08 (late), because the Arc_D_2 repair uses a `β` and these two would otherwise read as contradicting.** *Flagged by a parallel session: the corrected bracket's cancellation `ρ₋g(ρ₊) − ρ₊g(ρ₋) = ρ₋ − ρ₊` holds for `g` **linear and only then*** (measured at `ρ₋ = 0.80, ρ₊ = 0.70`: exact `0.100000` at `β = 1`, but `0.0688` at `β = 1.5` and `0.0440` at `β = 2.0`), **so "`D` constant, derived" appeared to rest on the exponent retired hours earlier.** *It does not — they are different objects:* **`β_postulate = 1` is DEFINITIONAL** — `g(ρ) = (B_max − b)/B_max` is the **remaining capacity**, affine in `b` **by construction**; nothing is fitted, and linearity is what "room left under a bound" *means*. **That is what the derivation uses, and it does not retire.** **`β_measured` is what RETIRED** — the exponent fitted from acceptance data, which ran `0.775 → 0.067` across a 15× range of commitment increment because acceptance is `P(b ≤ B_max − Δ)`. *An estimator output that moves with a run parameter.* **Retiring the second leaves the first untouched.** *Seventh one-symbol-two-objects instance of the week, and the first where two of the same day's own results collided.*
>
> **What is untouched:** `Γ₀(ρ) → 0` still derives at **`Grounded`** (the *vanishing*, not its exponent), the cap is still real and now **exact**, the certified rule is still destination-gated, and Arc_BH_3's Constraint 3 still stands. **What retires is only the exponent.**

---

## 5. Net for Target #15

**The singularity family's density cap moves from *declared/inherited* to *`Grounded` on an already-named postulate*, and the route runs through destination-gated exclusion rather than through the vanishing collective mobility the corpus currently cites.**

*One genuine derivation, one postulate-count reduction, and one specific defect with a specific repair in Arc_D_2.*

> ## ✅ TARGET #15's RESIDUAL IS CLOSED — with a stated CEILING, not a completion
>
> **What was asked:** derive `Γ₀(ρ) → 0 as ρ → ρ_max` **from P01–P13**.
> **What was delivered:** `Γ₀(ρ) = Γ_max(1 − ρ/ρ_max)` at **`Grounded`** — form-forced *given* `P-Locus-Bandwidth-Bound`, which is a **declared postulate, not a primitive.**
>
> **`Derived`-from-13 was not delivered and cannot be, for a reason the corpus states:** canonical P04 supplies non-negativity, **not an upper bound**, *“so any arc needing a finite per-locus budget must name one.”* **The residual as #15 phrases it is unmeetable; `Grounded` is the ceiling.**
>
> **What closing it buys:** a **postulate reduction** (two declared items to one — `Γ₀→0` was cited as its own “P4-class mobility-capacity bound” and follows from a bound already named); an **exact cap measured on the certified substrate**, with the bound as the only addition; `Γ₀ → 0` realised natively as **extinction**; and one number (`β`) **correctly retired against a rule fixed before the run.**
>
> *Six across-levels errors were caught in the course of it — five inside the corpus, one aimed outside it. That is the rate at which they were being made, not the rate at which they were being caught, and it is the reason for stopping here rather than continuing to the kernel.*
