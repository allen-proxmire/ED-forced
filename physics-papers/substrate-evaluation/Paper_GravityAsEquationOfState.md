# Gravity as an Equation of State: How Event Density Grounds Jacobson's Derivation of Einstein

**Allen Proxmire**

**July 2026**

---

## Preamble — what this article does NOT claim

1. **No new forced derivation.** This article arranges standing Event Density (ED) results against Ted Jacobson's 1995 derivation of the Einstein equation from thermodynamics. Its content is that ED *grounds the inputs Jacobson assumes*, reaches Einstein by a second route, and closes a gap Jacobson flagged in his own paper — not a from-nothing derivation.
2. **ED's results are conditional derivations from thirteen posited primitives** — never derivations from nothing — and the framework is not experimentally confirmed.
3. **Tiers are marked and vary by claim.** The area law is *measured* (simulation), the Unruh temperature *derived* from ED's own geometry, the `G` match an *algebraic identity*, the equilibrium/pure-area verdict *literature-grounded*; the one quantitative "co-suppression" claim (§7) rests on a coupling-prefactor *inference*, not a fully-rendered closed form, and is flagged as such.
4. **The full nonlinear Einstein equation is not independently derived by ED's own dynamical rule** (weak-field + khronometric class only, GR-I/II/III); the claim that Jacobson's route reaches full Einstein *in ED* is the equilibrium result of §6, at its stated tier.

---

## 1. What Event Density is, in one page

Event Density is an account of physics built on a **discrete, relational substrate**: a participation graph in which chains participate in channels, each channel carrying a **bandwidth** `b ≥ 0` and a phase. There is one process primitive: **commitment** (P11), the irreversible act by which an uncommitted participation becomes a definite, recorded fact. The arrow of time is not a boundary condition layered on reversible laws; it *is* this act, written into the law. Gravity in ED is emergent: the metric is the *reading* of the bandwidth field's connectivity (`g ~ 1/b`, `Paper_GR-I`), and the field equation is the steady state of a dynamical bandwidth rule (`Paper_GR-III`). ED's gravitational class is **khronometric** — Einstein's two tensor modes plus one scalar, the *khronon*, the arrow made dynamical (`Paper_GR-II`).

The corpus lives at `github.com/allen-proxmire/ED-generative` (DOI `10.5281/zenodo.20149496`); its front door is the Report, *Event Density: A Unified Framework for Physics*.

## 2. Jacobson's move, and the gap he left open

In 1995 Jacobson turned black-hole thermodynamics around ("Thermodynamics of Spacetime: The Einstein Equation of State," *Phys. Rev. Lett.* 75, 1260). Instead of deriving horizon entropy from general relativity, he **assumed horizon thermodynamics and derived general relativity.** His analogy is the ideal gas: knowing the entropy `S(E,V)`, you read the equation of state off the Clausius relation `δQ = TdS`. Applied to a **local Rindler horizon at every point**, with three inputs —

1. **area-law entropy** `S = ηA`,
2. **Unruh temperature** `T = ℏκ/2π`,
3. **heat = energy flux across the horizon** `δQ = ∫ T_{ab}χ^a dΣ^b` —

the demand that `δQ = TdS` hold for *all* local horizons forces, via the Raychaudhuri focusing equation, the **Einstein equation** `R_{ab} − ½R g_{ab} + Λ g_{ab} = (2π/ℏη) T_{ab}`. Gravity, on this reading, is not a fundamental field but an **equation of state**; Jacobson's own conclusion is that it "may be no more appropriate to canonically quantize the Einstein equation than it would be to quantize the wave equation for sound in air."

But the derivation leans on things it cannot supply, and Jacobson says so. The entropy is entanglement entropy of correlations across the horizon, finite only *"if there is a fundamental cutoff length `l_c`… of order the Planck length."* And the crucial constant:

> *"The dimensional constant `η` is undetermined by anything we have said so far (although given **a microscopic theory of spacetime structure** one may someday be able to compute `η` in terms of a fundamental length scale.)"*

That sentence is the opening this article walks through.

## 3. Event Density grounds Jacobson's inputs — and fills his gap

ED supplies a substrate reason for each of Jacobson's three assumptions:

| Jacobson's input | His words | ED grounds it |
|---|---|---|
| the horizon **hides DOF** behind a "causality barrier" | *"separated… by a causality barrier"* | **A1 severance** — the `b→0` horizon is a capacity-zero causal cut; the hidden DOF are the boundary adjacency channels (`Paper_GR-III` §7.4). |
| entropy = **entanglement across the cut**, finite via a **fundamental cutoff `l_c ≈ ℓ_P`** | *"correlations… inside and outside… finite [if] a fundamental cutoff `l_c`… of order the Planck length"* | ED **has** the cutoff natively — the grain `ℓ_ED = ℓ_P` (P08) — and the correlations across the cut are the **severed cross-chain (V5) participation**. |
| **`η` (entropy per area) is undetermined** — needs a microscopic theory | *"a microscopic theory of spacetime structure [to] compute `η` in terms of a fundamental length scale"* | **ED is that theory:** `η` is the severed-channel count per grain area, `η = 1/(4ℓ_P²)`; the area law `S ∝ A` is *because* severance is a surface cut — **measured** holographic in `Paper_GR-III` §7.4 (the severed count scales as the horizon perimeter, `r_h^{0.96}`, not its bulk). |

And the two accounts of Newton's constant are the same equation. Jacobson finds `G = (4ℏη)^{−1}`, identifying `η^{−1/2}` as twice the Planck length. Substituting ED's grain density `η = 1/(4ℓ_P²)`:

$$ G = \frac{1}{4ℏη} = \frac{ℓ_P^2}{ℏ} \;\xrightarrow{\text{restore }c}\; G = \frac{c^3 ℓ_P^2}{ℏ}, $$

**ED's constants-ledger value** (`Paper_027`). This is an *identity*, guaranteed once the grain is set to `ℓ_P` (whose value is a units anchor, inherited, §8), not a numerical coincidence. What ED genuinely supplies is the *reason* the entropy is area-law and `η ∝ 1/ℓ²`: severance is a surface cut (measured, `Paper_GR-III` §7.4). Jacobson's *"`G` from entropy-per-area"* and ED's *"`G` from the grain"* are then the same statement, which is why in both accounts Newton's constant is not fundamental but the least-fundamental, first-to-emerge conversion factor tied to the grain. ED fills the microscopic-structure gap Jacobson named.

## 4. The arrow paradox, resolved — and it is Jacobson's own resolution

There is a puzzle worth confronting. In ED's coarse-graining ledger (`Paper_HowCoarseGrainReality`), thermodynamics is the *one* continuum theory that **keeps** the arrow; general relativity is a theory that **threw the arrow away** (a reversible block spacetime). How, then, does Jacobson derive arrow-less GR *from* thermodynamics?

The ideal gas answers it — and the ideal gas is *Jacobson's own analogy*. The law `PV = nRT` shows no arrow, yet it is the equilibrium equation of state of a gas whose approach to equilibrium was irreversible. **The arrow lives in the second law (the approach), not in the equation of state (the destination).** Jacobson says as much: the Einstein equation is *"born in the thermodynamic limit… its validity depends on local equilibrium,"* and push the field hard enough and it fails — *"non-equilibrium spacetime."*

ED sharpens the "where is the arrow" answer to a primitive. The entropy Jacobson feeds in is the entanglement of **hidden** DOF, and in ED those are the **A1-severed** channels — and severance is **irreversible (P11)**. So the arrow is not smuggled in vaguely; it is the irreversibility of severance that *creates* the horizon entropy. **The arrow builds the horizon; general relativity is the equilibrium balance-sheet of what the horizon hides.** Thermodynamics is the receipt for the coarse-graining, and ED shows the receipt is written in one-way severed channels.

## 5. Two independent routes to Einstein

ED reaches Einstein's equation two ways that meet:

- **Route 1 (Jacobson, top-down thermodynamic):** assume horizon thermodynamics → Einstein. ED grounds all three of its inputs (§3), so ED can run this route on its *own derived* area law and temperature.
- **Route 2 (ED, bottom-up dynamical):** the bandwidth rule `ḃ = D∇²b − κρ` has the field equation as its steady state (`Paper_GR-III`; Newtonian limit measured, weak-field Einstein GR-I).

Two derivations of the same law, from opposite directions, with ED supplying the microscopic substrate Route 1 assumes. The temperature that Route 1 needs is itself an ED result: ED's vacuum profile `b = 1 − r_s/r` has **Rindler form** at the horizon, and smoothness forces `T = κ/2π` from ED's own geometry (`BH_Thermal2Pi`). One honesty pin travels with that: the derivation uses the standard Euclidean-continuation (Wick-rotation) smoothness argument, on par with general relativity's own and not yet arrow-native, so a commitment-statistics, continuation-free derivation of the `2π` remains open. It is a live irony that the one Jacobson input ED does not yet ground in the arrow is the temperature.

## 6. The khronometric departure is benign, and the equilibrium result is clean

ED is khronometric, so Jacobson's assumption of local Lorentz invariance is not exactly ED's. The natural worry is that this breaks the derivation. It does not, and the reason is that **both of ED's gravitational cones are luminal**: the graviton and the khronon each propagate at exactly `c` (`c_T = c` from the single transport cone, GR-II; `c_s = c` at leading order from the dissipative reserve, GR-III). Three consequences, each checked against the khronometric-gravity literature:

- **`α₂ = 0` exactly** (both cones luminal), so the causal/null structure is the *standard* light cone — Jacobson's local Rindler horizons and boost structure are intact. (Verified against the published PPN formulas; GR-IV.)
- **No universal-horizon complication.** The notorious "universal horizon" of Hořava-type gravity exists only because the khronon there is *superluminal*; ED's khronon is luminal, so the metric horizon is the true causal horizon and that complication does not arise.
- **The Unruh temperature survives.** What breaks horizon thermality is *nonlinear* dispersion, not a preferred frame; ED's dispersion is linear/luminal, so `T = ℏκ/2π` holds.

And the thermodynamics is cleaner still. The **local** Rindler-horizon entropy of a khronometric theory is **pure area** — the aether couplings only renormalize the coefficient (`S = A/4G_æ`), because the aether kinetic term carries no curvature and so contributes nothing to the Wald entropy. The genuinely non-area "aether entropy" is a *global* feature that requires a second scale (a cosmological constant) and a misaligned aether; in Jacobson's local, single-scale, aligned wedge it is reabsorbable into the coefficient and does not enter. So:

> **ED's local Jacobson derivation is cleanly equilibrium: the horizon entropy is pure area, and the derivation yields the full Einstein equation with no non-equilibrium correction beyond the universal shear-viscosity term that general relativity itself carries.**

Two corollaries. First, the internal shear-viscosity term that even pure general relativity carries is, in ED, *exactly* general relativity's — because the tensor cone is luminal (the aether modification is proportional to a coupling that vanishes there). ED adds no shear dissipation; it is observationally general relativity here too. Second, the departure from pure GR that *does* remain is the preferred-frame parameter `α₁ = −4λ_local`, with `λ_local ~ ρ_event/ρ_Planck` — suppressed some seventy orders of magnitude below any bound by the sparseness of commitment (GR-IV). *The arrow is real, but it leaves no shadow.*

## 7. The one remaining footprint: a scalar-sector co-suppression *(tiered)*

There is a single genuinely-new thermodynamic footprint, and it is *not* in the equilibrium entropy (which is pure area). It is a **bulk (scalar-sector) dissipation** — an internal entropy-production channel tied to the khronon's expansion — appearing at order `λ_local`. This is worth stating precisely because it lines up with the kinematic footprint:

> Both the khronon's **kinematic** footprint (the preferred-frame parameter `α₁`) and its **dissipative** footprint (the bulk entropy-production channel) are `O(λ_local) ~ ρ_event/ρ_Planck`, and **not by coincidence: both are the khronon (scalar) sector's expression, controlled by the single coupling that survives on ED's luminal family.** The same sparseness of becoming that keeps ED's preferred frame silent keeps its equation-of-state dissipation silent — one suppression, two faces.

This extends the GR-IV reading ("one structure — sparse becoming — many faces: coherence, time dilation, preferred-frame silence") with a thermodynamic face. **Honest tier:** the equilibrium/pure-area result (§6) is literature-grounded; this `O(λ_local)` co-suppression rests on the aether flux-current *prefactor* (which reduces to the single luminal coupling), not on a fully-rendered closed-form entropy, and the *absolute* seventy-orders number is inherited from GR-IV's own estimate-tier derivation of `λ_local`. What is robust independent of that number is the *relative* statement — the two footprints are the same small quantity because they are the same coupling; if `λ_local`'s value moved, both would move together.

## 8. Honest tiers and open edges

- **Grounded / measured:** ED grounds Jacobson's three inputs (§3); `S ∝ A` from severance (measured, GR-III §7.4); `T = κ/2π` from ED's Rindler geometry; the `G = c³ℓ_P²/ℏ` match (algebraic identity); the local pure-area equilibrium result and its literature backing (§6).
- **Synthesis:** the two-routes reading; the arrow-paradox resolution; the scalar-sector co-suppression (§7, at the tier stated there).
- **Open:** a fully written-out `δQ=TdS` derivation of the *khronometric* field equations at a local horizon (nobody has done this; ED now has the grounded pieces to); a commitment-statistics, continuation-free derivation of the horizon `2π`/temperature (the one input still gotten via the reversible-time Euclidean route; `BH_Thermal2Pi` §4); the closed-form aether-entropy leading power that would harden §7 from inference to computation; the value of the grain / `λ_local` (inherited, as is Jacobson's `l_c`).

## 9. Position statement

Jacobson showed that general relativity is an equation of state — an equilibrium thermodynamic relation of unknown microscopic degrees of freedom — and named the missing piece: a microscopic theory of spacetime structure that would compute the entropy density from a fundamental length. Event Density supplies exactly that. Its severed channels are the hidden degrees of freedom; its grain is the cutoff; its severance count is the area-law entropy; and its entropy-per-area lands Newton's constant on ED's own `G = c³ℓ_P²/ℏ`. The arrow that ED puts into the law is the irreversibility that gives those horizons their entropy in the first place — so general relativity, the arrow-blind equation, is the equilibrium receipt of an arrow-ful accounting. ED reaches the *weak-field* Einstein equation independently through its bandwidth dynamics (GR-I/GR-III); the *full* Einstein equation is the Jacobson-route equilibrium result of §6, not a claim of the dynamical rule. Its preferred-frame departure is luminal, benign, and seventy orders silent, and its local equation-of-state derivation is cleanly equilibrium. The one new footprint — a scalar-sector dissipation — is the same sparse-becoming coupling that silences the preferred frame, wearing a thermodynamic face. None of this is claimed as confirmed physics; it is claimed as a grounding: the microscopic theory Jacobson said his derivation was waiting for, and the substrate reason his equation of state has the form it does.

---

## Cross-references

- Jacobson, T., *Phys. Rev. Lett.* **75**, 1260 (1995), gr-qc/9504004 — "Thermodynamics of Spacetime: The Einstein Equation of State."
- **ED gravity line:** `physics-papers/gravity/Paper_GR-I` (`g~1/b`, weak-field metric), `Paper_GR-II` (khronometric class), `Paper_GR-III_DynamicalRule.md` (the bandwidth rule; §7.4 area law from severance; the `b→0` = A1 cut), `Paper_GR-IV_ArrowsAlibi.md` (`α₁=−4λ_local`, `α₂=0`, sparse-becoming suppression).
- **Horizon thermodynamics:** `foundations/BH_Thermal2Pi_FromNearHorizonRindler.md` (`T=κ/2π` from ED's Rindler geometry); `foundations/BH_EntropyCoefficient_FromEventCounting.md` (the `1/4`).
- **Constants:** `Paper_027_Newtons_G.md` + Essays 13/14 (`G = c³ℓ_P²/ℏ`, the constants ledger).
- **The ledger:** `physics-papers/substrate-evaluation/Paper_HowCoarseGrainReality.md` (GR as the law of the seam; thermodynamics as the receipt).
- **External (khronometric/thermodynamic gravity):** Eling–Guedens–Jacobson, gr-qc/0602001 (nonequilibrium spacetime); Chirco–Liberati, PRD 81, 024016 (horizon shear viscosity); Blas–Lim arXiv:1412.4828, Ramos–Barausse arXiv:1811.07786, Foster–Jacobson gr-qc/0509083 (khronometric PPN); Berglund–Bhattacharyya–Mattingly arXiv:1210.4940 (universal-horizon thermodynamics); arXiv:2603.28851 (covariant phase space; reabsorbability of the aether flux term).
