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

**What this buys is a postulate reduction, not a new commitment.** `Γ₀(ρ)→0` is cited by Arc_BH_3 and Arc_D_2 as its own thing — *"the P4-class mobility-capacity bound"* — as though independently declared. **It is not: it follows from a bound the corpus already names.** *Two declared items become one.*

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

---

## 5. Net for Target #15

**The singularity family's density cap moves from *declared/inherited* to *`Grounded` on an already-named postulate*, and the route runs through destination-gated exclusion rather than through the vanishing collective mobility the corpus currently cites.**

*One genuine derivation, one postulate-count reduction, and one specific defect with a specific repair in Arc_D_2.*
