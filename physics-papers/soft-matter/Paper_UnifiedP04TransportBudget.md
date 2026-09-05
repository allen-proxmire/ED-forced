# The Unified P04 Transport Budget: Viscosity and Resistivity Saturation Are One Adjacency-Band Wall

**Series:** Event Density (ED) Generative Papers — soft-matter / transport arc (P04 bounded-participation); transport twin of `Paper_V5UnifiedBudget`
**Author:** Allen Proxmire
**Status:** Working derivation draft (conditional structural derivation within the 13-Primitive Generative System). Identifies the single per-cell P04 budget both transport ceilings spend against (the Adjacency band), derives the *co-onset* relation (the R1-analog: one saturation event, two proxy shadows), and scopes the exact ratio (the R2-analog) as the remaining open step. Advances §4 of `Paper_P04TransportBudget_ResistivitySaturation`.
**Companions:** `Paper_079_P4_NN_Rheology` (viscosity ceiling `φ_max`), `Paper_P04TransportBudget_ResistivitySaturation` (resistivity ceiling `ρ_max`), `Paper_073_DCGT` (substrate→continuum, the cell), `Paper_087_13Primitives` (P04 four-band, P05, P08), `Paper_V5UnifiedBudget` (the template: one envelope, fixed ratios).

---

## Preamble — What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The absolute ceilings are inherited.** `φ_max` and `ρ_max` (the MIR value) stay inherited, exactly as in `Paper_079` / the resistivity scoping paper. This paper claims a *relation between them*, not their values.
2. **The exact ratio is NOT derived here.** The commensurability's *value* requires two projection factors (momentum-content vs charge-content weight per adjacency unit) that the corpus does not supply. That is scoped (§4) as the remaining step, not delivered. **→ SUPERSEDED 2026-09-05 by §9, with two changes to what is claimed.** The projection factors are now computed, **but the invariant is the *product* `η_min·ρ_max`, not the ratio** (§9.1 corrects §8), and the result is **`D-via-I`, not substrate-native**: ED supplies one line — that both transports floor at the *same* length — and inherited kinetic theory supplies the rest. **The coefficient remains a band `Λ ∈ [1/5, 1/3]`**, its width a kinetic-averaging convention that the substrate cannot close (§9.6). What is claimed is the **existence and parameter-independence** of `Λ`, not its value.
3. **The load-bearing identification is a posit, not a theorem.** That both momentum transport and charge transport spend the *same* Adjacency band (§2) is grounded in P04's four-band partition + P05 being the sole inter-locus transport, but it is a declared identification (`P-Adjacency-Transport-Shared`), scrutinizable, not closed.
4. **The individual ceilings remain consilience** (`Paper_079` viscosity, MIR resistivity). What is new and *distinctive* here is the **co-onset** (§3): the claim that they are the *same substrate event*.
5. **No new substrate primitives.**

---

## Abstract

`Paper_079` caps viscosity (`η ∝ (1−φ/φ_max)^{−n}`) and `Paper_P04TransportBudget_ResistivitySaturation` caps resistivity (MIR: mean free path floored at the cell) — each via a bounded-P04-budget postulate, each with its ceiling value inherited. We show they are **not two independent ceilings but one wall.** P04 partitions each locus's finite bandwidth into four orthogonal bands (Internal, **Adjacency**, Environmental, Commitment-reserve); the **Adjacency band** is defined as the content shared with neighboring loci via P05 polarity-transport — i.e. it *is* the inter-locus transport conduit. Momentum transport (→ viscosity) and charge transport (→ resistivity) are both inter-locus transport, so both spend the *same* finite per-cell Adjacency budget `b_adj^max`. Hence (R1-analog, **derived in form**): the viscosity divergence and the resistivity saturation are the **same substrate event — the Adjacency band reaching saturation** — sharp in the substrate occupancy variable `f = b_adj^used/b_adj^max` and appearing as two proxy shadows (`φ_max` in packing, `ρ_max` in scattering). This forces a **co-onset prediction**: in any system where one cell governs both transports, momentum-transport choke (viscosity divergence) and charge-transport choke (resistivity saturation) onset *together*, at the common budget wall — a correlation no standard account predicts (Krieger–Dougherty and Mott–Ioffe–Regel are unrelated in conventional physics). The exact ratio `φ_max : ρ_max` (R2-analog) requires two projection factors (momentum vs charge content weight per adjacency unit) and is scoped, not derived. Inherited: the values. Forced: that they are one wall, and co-onset.

---

## 1. The template and the target

`Paper_V5UnifiedBudget` took three separately-postulated V5 budgets and showed they are one envelope `W_max` seen three ways, forcing (R1) a common onset in the substrate content variable, a band in each lab proxy, and (R2) fixed ratios `1 : 1 : 0.88` — inherited *scale*, forced *relations*. We seek the transport twin: are the viscosity ceiling `φ_max` and the resistivity ceiling `ρ_max` two projections of one P04 budget?

## 2. The shared budget is the Adjacency band (`P-Adjacency-Transport-Shared`)

P04 (`primitives/P04`) partitions each locus's finite bandwidth `b(u)` into four **orthogonal** bands:

- **Internal** — the channel's own coherent content;
- **Adjacency** — *content shared with neighboring loci via P05 polarity-transport*;
- **Environmental** — content coupled to the decohering environment;
- **Commitment-reserve** — budget consumed by P11 commitment.

The decisive observation: **inter-locus transport happens only through P05 polarity-transport, and the Adjacency band is by definition the P05-transport content.** So *any* transported quantity between cells — momentum content, charge content — is carried in the Adjacency band. Its per-cell capacity `b_adj^max` is finite (a fixed fraction of the finite `b(u)`).

**`P-Adjacency-Transport-Shared` (declared identification):** momentum transport (the flux that coarse-grains to viscous stress, DCGT §6.1) and charge transport (the flux of P09 U(1) polarity content that coarse-grains to conductivity) both draw on the *same* per-cell Adjacency budget `b_adj^max`; they are two *contents* competing for one conduit, not two conduits.

This is grounded (P04 four-band + P05 as sole transport) but declared, not proven — it is the load-bearing joint (Preamble 3), and the single most important thing to attack.

## 3. R1-analog — one saturation event, two proxy shadows (derived in form)

Let `f = b_adj^used / b_adj^max ∈ [0,1]` be the per-cell Adjacency occupancy. Both ceilings are the **same** condition `f → 1`:

- **Viscosity** (`Paper_079`): as packing `φ → φ_max`, momentum content saturates the Adjacency band (`f → 1`); momentum can no longer flow between cells; `η` diverges. So `φ_max` is the *packing proxy* of `f = 1`.
- **Resistivity** (scoping paper): as scattering occupancy rises, charge content saturates the Adjacency band (`f → 1`); the mean free path floors at the cell; `ρ` saturates. So `ρ_max` is the *scattering proxy* of `f = 1`.

Therefore, exactly as `Paper_V5UnifiedBudget` R1: **the sharp variable is the substrate occupancy `f`; the two transport ceilings are proxy shadows of the single event `f = 1` (the Adjacency band full).** Sharp in `f`, a band in each lab proxy (`φ`, scattering strength) because the proxy→`f` conversion differs by system. This is *derived in form* given `P-Adjacency-Transport-Shared`; the conversions and the absolute ceilings are inherited.

> **⚠ THE WALL'S IDENTIFICATION WITH MIR IS NOT ARGUED, and 2026-09-05's literature check makes that expensive.** This section reads `ρ_max` as the **MIR saturation value** and §8 makes strange metals the arena. **But bad metals do not saturate:** Gunnarsson, Calandra & Han (Rev. Mod. Phys. **75**, 1085) name high-T꜀ cuprates and alkali-doped fullerides as violating the Ioffe–Regel condition, the extracted mean free path passing *below* the interatomic spacing with no saturation. **The arc points at the one material family that has no wall.** A dilemma, and both horns cost something: **if `a_eff` is the interatomic spacing**, bad metals run through the floor and the wall is not where the arc says; **if it is not**, then MIR saturation is not ED's wall and this section's identification of `ρ_max` — with §8's corrected pairing on top of it — is a misidentification. **SETTLED the same day, onto the second horn and more sharply than that:** `a_eff` is **neither** the DCGT cell **nor** `ℓ_ED` — it is the material's emergent transport cell, **inherited**. **Nothing in ED derives any floor at the lattice spacing at all**, and the P08→DCGT→lattice-spacing chain has an unwritten step in it. **ED does not explain MIR; it inherits it.** The *sharing* claim survives and was always the distinctive part. `Note_FConverge_Run_2026-09-05.md` §1; `Note_WhatIsAEff_2026-09-05.md`.

**The distinctive, falsifiable content — CO-ONSET.** Because both are the *same* wall, they must onset **together**. In a system where one cell governs both transports — a dense charged colloid, a molten salt, a strongly-correlated electron liquid with a measurable viscosity near its MIR point — driving toward the wall must choke *momentum* transport (viscosity diverging) and *charge* transport (resistivity saturating) at the **same** substrate occupancy. Conventional physics predicts no such link: Krieger–Dougherty jamming and Mott–Ioffe–Regel saturation are unrelated mechanisms. ED forces them to be one. **Co-onset is testable even before the exact ratio is known.**

## 4. R2-analog — the exact ratio (scoped, OPEN)

The values `φ_max` and `ρ_max` are different dimensioned quantities; their relation is set by *how each content fills the same band*:

$$
\phi_{\max} = \Pi_p(b_{\rm adj}^{\max},\,a_{\rm eff}),\qquad
\rho_{\max} = \Pi_q(b_{\rm adj}^{\max},\,a_{\rm eff}),
$$

with `Π_p`, `Π_q` the momentum- and charge-content projection factors (the transport analogs of `ρ_loc` and `f_ent·g_∂` in `Paper_V5UnifiedBudget`). Their **ratio** cancels the common `b_adj^max` and the common cell `a_eff` (DCGT renormalization, the analog of the `ℓ_V5` cancellation), leaving a forced, non-inherited number `Π_p/Π_q` — *if* `Π_p`, `Π_q` can be computed.

**They cannot, yet.** The corpus does not derive how much Adjacency weight one unit of momentum content vs one unit of charge (U(1)-winding, `B4`/P09) content consumes. Deriving `Π_p` and `Π_q` — a momentum-content and a charge-content "weight per adjacency unit" from the substrate — is the remaining step, and it is where the exact commensurability (the R2-analog `φ_max : ρ_max`) would become a hard number. **Declared open; this is the next sub-target.**

## 5. Load-Bearing Step Audit

| Step | Status | Justification |
|---|---|---|
| P04 four-band partition; Adjacency = P05-transport content | **P (primitive)** | `primitives/P04` §1.5 |

> **✅ TIER FLAG WITHDRAWN 2026-09-04 — the `P (primitive)` tier is CORRECT.** The four-band partition is canonical primitive-level content (P04 §1.5); the M-series archive removed the *forcing* argument for it, not the partition itself. **So this arc's Prediction rests on solid ground and needs no re-grounding.** See gravity ledger Staleness #57. *Superseded flag kept below as the audit trail.* **Original flag:** The row above tiers the **four-band partition** as **P (primitive)**, citing `primitives/P04` §1.5. **Canonical `Paper_087` has no four-band** — it defines P04 as bandwidth, a non-negative additive scalar — and the foundations ledger records four-band as archived M-series content. **So this row inherits a primitive-tier claim from a definition card that disagrees with the canonical primitives paper**, and this arc's *only* Prediction (the shared Adjacency-band wall) rests on it: without a band partition, *“the Adjacency band”* has no referent. **This is a tier problem, not necessarily a physics problem** — the shared-budget identification may well survive on P04 additivity plus P05-as-sole-transport without needing four *named* bands, which would be a re-grounding rather than a retraction. **Not attempted here.** Gravity ledger Staleness #56; soft-matter ledger staleness #7.
| Inter-locus transport is P05-only; both momentum & charge use Adjacency | **P (`P-Adjacency-Transport-Shared`)** | §2; grounded in P04+P05, declared |
| Finite per-cell `b_adj^max` | **form-forced** | P04 finiteness + additivity (DCGT §3.2) |
| Both ceilings = one event `f → 1` (R1-analog) | **D (form), conditional on §2** | §3 |
| **Co-onset prediction** (viscosity divergence & resistivity saturation together) | **D conditional → falsifiable** | §3 |
| ~~Exact ratio `φ_max : ρ_max` = `Π_p/Π_q`~~ → **invariant product `Λ = η_minρ_max e²/p_F² = Π_pΠ_q`** *(pairing corrected §8; ratio→product corrected §9.1)* | **D-via-I** — CLOSED IN FORM 2026-09-05 | §9.3. `n`, `a_eff`, `b_adj^max` and the coupling all cancel. **Value inherited**: `Λ ∈ [1/5, 1/3]`, the width a kinetic-averaging convention (§9.6). |
| `Λ` measures the ratio of the two mean-free-path floors, `a_η/a_ρ` | **D** | §9.4 — the cancellation exists *only* under one floor, so `Λ` is a direct measurement of `P-Adjacency-Transport-Shared` rather than a test against a computed number |
| Absolute `φ_max`, `ρ_max`, `a_eff`, `b_adj^max` | **I** | inherited. *(2026-09-05: `a_eff` was already tiered `I` here while §9.2 called it “the DCGT cell” and §3's mechanism derived it from P08 — **the row was right and the prose around it was not.** `a_eff` is the material's emergent transport cell; DCGT and P08 leave the chain. `Note_WhatIsAEff_2026-09-05.md`.)* |

## 6. Falsification Criteria

- **F-COONSET (the distinctive one):** in a system where one cell governs both transports, the viscosity divergence and the resistivity saturation onset at *different* substrate occupancies (no correlation between the jamming point and the MIR point beyond coincidence) — falsifies `P-Adjacency-Transport-Shared` / the one-wall claim. This is the near-term, ED-owned bet.
- **F-BAND:** demonstration that inter-locus transport uses a channel *other* than the P05/Adjacency band (a second, independent transport conduit) — falsifies the shared-budget identification (§2).
- **F-RATIO — LIVE as of 2026-09-05 (§9.8), and restated.** Form `Λ = ηρe²/p_F²` at a system's MIR point. **ED predicts `Λ` is O(1) and, the sharper half, that it does not drift with `a_eff`, `n` or material.** A `Λ` tracking lattice spacing or carrier density falsifies the single-floor claim directly, since `Λ = Π_pΠ_q·(a_η/a_ρ)`. **The drift test is stronger than the value test** and is independent of the unresolved `[1/5, 1/3]` coefficient band.
- **F-CONVERGE (new 2026-09-05; ⬇ RUN 2026-09-05 and NOT RUNNABLE — see `Note_FConverge_Run_2026-09-05.md`).** *The* “cheapest test in the arc” *label is withdrawn: it asserted an availability that had not been checked. `ℓ_ee` and `ℓ_mr` are measured in* **disjoint** *windows in every established system — WP₂ is hydrodynamic below ~20 K and conventional above; graphene and PdCoO₂ are ultra-clean low-temperature systems — so there is no dataset to run it against.* **The statement of the test stands; its availability does not.** The momentum-conserving and momentum-relaxing mean free paths must **converge** as the wall is approached. A system driven to MIR saturation with `ℓ_ee` and `ℓ_mr` still separated by orders of magnitude falsifies `P-Adjacency-Transport-Shared` **with no viscosity measurement at all.**

## 7. Position Statement

Viscosity saturation and resistivity saturation are **one Adjacency-band wall**, not two ceilings. P04's four-band partition makes the Adjacency band the sole inter-locus transport conduit, so momentum transport (viscosity) and charge transport (resistivity) spend one finite per-cell budget; both ceilings are the single event of that band filling (R1-analog, derived in form), forcing a **co-onset** of viscosity divergence and resistivity saturation that conventional physics — where Krieger–Dougherty and Mott–Ioffe–Regel are unrelated — does not predict. The absolute ceilings stay inherited; the *co-onset* is the distinctive, falsifiable, ED-owned content, testable before the exact ratio is known. The exact ratio `φ_max : ρ_max` (R2-analog) awaits the momentum- and charge-content projection factors `Π_p`, `Π_q`, declared open (§4) as the next sub-target.

**What this paper claims:** the shared Adjacency budget (declared identification); the one-wall / co-onset result (derived in form); the scoping of the exact ratio. **What it does not:** the ceiling values, the exact ratio, or a closed proof that both transports share the band (that is the load-bearing posit to test, F-BAND).

---

## 8. Derivation update (running the `Π_p`/`Π_q` step, 2026-07-30): the correct pairing is MIR ↔ the viscosity floor, not KD jamming

*(Dated update per QC close-the-loop discipline — corrects the §3 pairing, does not silently overwrite it.)*

Attempting the projection factors surfaced a correction. **"Adjacency band full" means maximum inter-locus transport activity — the carrier mean free path floored at one cell, `ℓ → a_eff`.** Floor `ℓ` and:

- **charge** transport gives the resistivity **ceiling** (MIR: `ρ_max ~ (h/e²)·a_eff`);
- **momentum** transport gives a viscosity **floor** `η_min ~ n m v_F a_eff` — entropy-normalized, the **KSS / Planckian bound `η/s ~ ℏ/k_B`**.

Both are the *same* event (`ℓ = a_eff`). So the genuine co-onset partner of MIR resistivity saturation is the **minimum-viscosity (Planckian / KSS) bound, not the Krieger–Dougherty jamming divergence.** KD jamming (`φ_max`) is a *different* saturation mode — geometric rigidity at high packing (isostatic `Z → 2d`), not the max-scattering mean-free-path floor — so §3's `φ_max ↔ ρ_max` pairing used the wrong viscosity limit. **Corrected pairing:** `η_min (KSS/Planckian) ↔ ρ_max (MIR)`, both `ℓ`-floored at `a_eff`. KD `φ_max` is re-classified as a separate (rigidity) band-saturation mode, not the co-onset partner.

**Why this is a *stronger* result.** Condensed-matter physics separately observes MIR resistivity saturation, the Planckian dissipation bound `τ ~ ℏ/k_BT`, and the KSS viscosity bound `η/s ≥ ℏ/4πk_B`, and actively debates whether they are the same physics (strange metals, quantum-critical transport). **ED's adjacency-band saturation says they are one wall** — the mean free path floored at one substrate cell, for charge and momentum alike.

**Projection factors, revisited.** Both floors now share `ℓ = a_eff`, so `η_min` and `ρ_max` both scale with `a_eff` and carrier properties, and their ratio `η_min : ρ_max` is an O(1) that cancels `a_eff` — a *same-kind* (both mean-free-path-floored) comparison, not the dimensionful cross-comparison of §4. Its exact value still needs the momentum- vs charge-content weights (`Π_p`, `Π_q`: adjacency consumed per unit of each), which remain **underived** — the still-open step. But the target is now clean and physically grounded.

**Sharpened distinctive prediction (upgrades F-COONSET).** In the strange-metal / quantum-critical regime — where MIR, Planckian resistivity, and the viscosity bound are all measured in one system — the resistivity ceiling and the viscosity floor are **one wall**: co-onset, commensurate at fixed `ℓ = a_eff`. **⚠ CORRECTED 2026-09-05. The sentence here previously read** *“Standard physics has no reason to unify them; ED forces it.”* **That was false, and it contradicted this paper's own paragraph three lines above**, which correctly says condensed-matter physics *“actively debates whether they are the same physics.”* **The unification is an existing, named position in the literature:** Zaanen (2019), *Planckian dissipation, minimal viscosity and the transport in cuprate strange metals*, SciPost Phys. **6**, 061 (arXiv:1807.10951), argues precisely that cuprate strange-metal resistivity is governed by the **minimal viscosity** of the quark-gluon-plasma bound, with *“the momentum relaxation rate governing the resistivity relat[ing] directly to the electronic entropy.”* **So ED is not supplying a link nobody had reason to draw; it is entering an open debate on one side.** **The corrected claim, which is narrower and testable:** the *hydrodynamic* route reaches the link through minimal viscosity and entropy, whereas ED reaches it through **one mean-free-path floor at `ℓ = a_eff` shared by charge and momentum**. **Those are different mechanisms making a co-onset prediction that is commensurate in ED and not obviously so in the hydrodynamic account**, and the discriminating quantity is the ratio `η_min : ρ_max` — which this paper leaves **underived** pending `Π_p`, `Π_q`. Until that ratio exists, ED's position on this question is a stance, not a prediction that separates it from Zaanen's. *(“ED forces it” also violates the corpus's standing no-forcing posture; the honest verb is that the unification follows given `P-Adjacency-Transport-Shared`.)* Gravity ledger Staleness #61. **F-COONSET is upgraded to: MIR-resistivity ↔ viscosity-floor co-onset** (a live strange-metal question), replacing the KD-jamming ↔ MIR version.

**Honest tier:** the *unification* (one wall) and the *co-onset* are forced given `P-Adjacency-Transport-Shared`; the exact `η_min : ρ_max` coefficient stays inherited pending `Π_p`, `Π_q`. The identification of these floors with the standard names (MIR, KSS, Planckian) is consilience. The load-bearing risk is unchanged and now sharper: do charge and momentum truly share *one* adjacency band, or distinct channels within it (F-BAND)?

---

---

## 9. The `Π_p` / `Π_q` step, run 2026-09-05: the invariant is the **product**, not the ratio, and it is `η_min · ρ_max = p_F²/(3e²)`

*(Dated update. §4 declared these open and §8 scoped them; this section runs the step. It also corrects §8.)*

> **⚠ DOMAIN-OF-VALIDITY DEFECT, found 2026-09-05 while trying to use this section. Read before §9.3.** §9.2 obtains `Π_q = 1` from Drude and `Π_p = 1/3` from kinetic theory, **both evaluated at `ℓ = a_eff`, the wall.** That is exactly where the bad-metal literature says the Boltzmann/quasiparticle description stops holding — past Ioffe–Regel the mean-free-path language survives only as an extrapolation, and the Fermi velocity with it. **Both inherited ingredients of `Λ` are used outside their domain of validity, at the one point where the answer is wanted.** §9.5's `I` tier and §9.6's `[1/5, 1/3]` band do **not** capture this: the issue is not that the coefficient is uncertain but that at the wall `p_F` and `n` may not be the right variables, in which case **`Λ`'s parameter-independence — the whole claim per §9.6 — loses the derivation that produced it.** `Λ` may still be right; bounds of that shape are reached without quasiparticles in the Planckian and holographic literature. **But ED has not derived it that way.** Cheapest repair: restrict `Λ` to the quasiparticle regime *approaching* the wall rather than at it, which is honest, testable, and turns `Λ` into a limiting statement. `Note_FConverge_Run_2026-09-05.md` §3; gravity ledger Staleness #65.

### 9.1 First, the correction §8 needs

§8 states that *“their ratio `η_min : ρ_max` is an O(1) that cancels `a_eff`.”* **That is wrong, and F-RATIO was written against it.** At the wall,

$$\eta_{\min} \propto a_{\rm eff}^{+1}, \qquad \rho_{\max} \propto a_{\rm eff}^{-1},$$

because a mean-free-path floor *raises* the viscosity floor and *lowers* the conductivity. **So the ratio scales as `a_eff²` and the product is the invariant.** Same-kind does not mean same-sign: both are floored at one length, but that length enters the two transport coefficients with opposite powers. The rest of this section is written on the product.

### 9.2 The two projection factors, defined so they are computable

Write each wall value in the schema §4 asks for — a substrate-set scale times a pure number:

$$\eta_{\min} \;=\; \Pi_p \, n \, p_F \, a_{\rm eff}, \qquad
\rho_{\max} \;=\; \Pi_q \, \frac{p_F}{n \, e^2 \, a_{\rm eff}}.$$

`n` is the carrier number density, `p_F` the carrier momentum, and `a_eff` **the material's own emergent transport cell — inherited, not derived** *(settled 2026-09-05; this line previously read* “the DCGT cell”*, which is not available: `Paper_073_DCGT` §3.1 makes `R_cg` a chosen scale with results insensitive to the choice, so a physical floor there would depend on a bookkeeping decision. See* `Note_WhatIsAEff_2026-09-05.md`*).* **`Λ` is indifferent to this** — it cancels `a_eff` whatever `a_eff` is — but the arc's claim to *explain* MIR is not. `Π_p` is the momentum-flux capacity per unit Adjacency occupancy; `Π_q` is the charge-transport impedance per unit Adjacency occupancy. **Both are pure numbers.**

Standard kinetic transport, evaluated at the floor `ℓ = a_eff`, supplies them:

- **Momentum.** Kinetic shear viscosity `η = ⅓ n m v ℓ = ⅓ n p_F ℓ`. At the floor, **`Π_p = 1/3`**.
- **Charge.** Drude `ρ = m/(n e² τ)` with `τ = ℓ/v_F` and `m v_F = p_F` gives `ρ = p_F/(n e² ℓ)`. At the floor, **`Π_q = 1`**.

**Nothing in that paragraph is ED.** It is textbook kinetic theory, and saying so is the point of §9.5.

### 9.3 The invariant

$$\eta_{\min}\,\rho_{\max} \;=\; \Pi_p\Pi_q\,\frac{p_F^{\,2}}{e^{2}}
\qquad\Longrightarrow\qquad
\boxed{\;\Lambda \;\equiv\; \frac{\eta_{\min}\,\rho_{\max}\,e^{2}}{p_F^{\,2}} \;=\; \Pi_p\Pi_q \;=\; \tfrac{1}{3}\;}$$

**`n` cancels. `a_eff` cancels. `b_adj^max` never appears. The coupling strength never appears.** What survives is the carrier's momentum and its charge, and those are inherited. **This is the R2-analog the paper has been owing since §4: a forced, non-inherited pure number.**

An equivalent form ties it to a measured constant. With `p_F = ħk_F` and the von Klitzing constant `R_K = h/e²`,

$$\eta_{\min}\,\rho_{\max} \;=\; \frac{\hbar k_F^{2}}{6\pi}\,R_K .$$

**The product of the two transport walls is the resistance quantum times a purely geometric carrier factor.**

### 9.4 Where the cancellation actually comes from, and what Λ therefore measures

The `a_eff` cancellation is **not** bookkeeping. It happens only because **one** length floors both transports. Allow two floors, `a_η` for momentum and `a_ρ` for charge, and the algebra returns

$$\Lambda \;=\; \Pi_p\Pi_q\,\frac{a_\eta}{a_\rho}.$$

**So `Λ` is a direct measurement of the ratio of the two floors, and `P-Adjacency-Transport-Shared` is exactly the claim that that ratio is 1.** This is the cleanest statement of the arc's load-bearing posit, and it turns F-RATIO from a comparison against a computed number into a measurement of the posit itself.

**This is also where the arc's content sits relative to conventional physics.** In standard treatments the momentum-relaxing length (which sets `ρ`) and the momentum-conserving length (which sets `η`) are *different objects* — electron hydrodynamics is defined by `ℓ_ee ≪ ℓ_mr`, established by orders of magnitude in graphene, PdCoO₂ and WP₂. **ED does not contradict that**, because its claim is about the wall, where both lengths floor at the cell. **But it makes a sharp statement about approach: the two lengths must converge as the wall is approached, because at the wall they are the same band.** That is a second falsifier, and it is independent of the value of `Λ`.

### 9.5 Honest tiering — what is ED here and what is not

| Ingredient | Source | Tier |
|---|---|---|
| Both transports floored at **one** length `a_eff` | `P-Adjacency-Transport-Shared` (§2) | **P** (declared) |
| `η = ⅓ n p_F ℓ`; `ρ = p_F/(n e² ℓ)` | textbook kinetic transport | **I** |
| The product is the `a_eff`-invariant, not the ratio | §9.1 | **D** |
| `Λ = Π_pΠ_q`, independent of `n`, `a_eff`, `b_adj^max` | §9.3 | **D-via-I** |
| `Λ = 1/3` exactly | kinetic-averaging convention | **I** — see §9.6 |

**The ED-specific content is one sentence:** at the wall the momentum-relaxing and momentum-conserving mean free paths are the same length, because they are the same band. **Everything else on this page is inherited**, and the derivation is `D-via-I`, not substrate-native. Stating it otherwise would repeat the defect this paper was corrected for in §8.

### 9.6 The coefficient is a band, not a number — do not quote `1/3` as forced

`Π_p = 1/3` is simple isotropic kinetic averaging. The standard degenerate-Fermi-gas transport result is `η = ⅕ n p_F ℓ`, giving `Π_p = 1/5`. So

$$\Lambda \in [\,1/5,\;1/3\,],$$

a factor-1.7 band whose width is a **kinetic-averaging convention, not substrate physics**. **What ED claims is the existence and the parameter-independence of `Λ`, not its value.** Pinning the value requires choosing the transport-averaging scheme appropriate to the carrier statistics at the wall — where, by construction, quasiparticles are marginal and neither scheme is clearly right. **That is an inherited ambiguity and it is not closable from the substrate.**

### 9.7 Numerical check

Take `k_F = 1×10¹⁰ m⁻¹` and `a_eff = 3×10⁻¹⁰ m`. Then `n = k_F³/3π² = 3.4×10²⁸ m⁻³`, `p_F = ħk_F = 1.06×10⁻²⁴ kg m/s`, and

- `η_min = ⅓ n p_F a_eff = 3.56×10⁻⁶ Pa·s`
- `ρ_max = p_F/(n e² a_eff) = 4.06×10⁻⁶ Ω·m = 405 μΩ·cm`
- product `= 1.4441×10⁻¹¹`, and `p_F²/3e² = 1.4441×10⁻¹¹`, agreeing to every digit carried, as does the `R_K` form of §9.3 ✓

**The `ρ_max` lands inside the observed MIR saturation band (~100–500 μΩ·cm).** That is a **consistency check on the inputs, not a prediction** — `a_eff` was chosen at a lattice spacing, which is what MIR saturation means. Recorded to head off exactly the reading gravity Staleness #26 warns about.

### 9.8 F-RATIO, now concrete — and a new F-CONVERGE

- **F-RATIO (was pending, now live).** In one system at its MIR point, measure `η` and `ρ`, obtain `p_F` from the carrier density, and form `Λ = ηρe²/p_F²`. **ED predicts `Λ` is O(1), in `[1/5, 1/3]`, and — the sharper half — that it does not drift with `a_eff`, `n`, or material.** A `Λ` that tracks lattice spacing or carrier density falsifies the single-floor claim directly, since `Λ = Π_pΠ_q·(a_η/a_ρ)`. **The drift test is stronger than the value test** and does not depend on resolving §9.6.
- **F-CONVERGE (new).** The momentum-conserving and momentum-relaxing mean free paths must **converge** as the wall is approached. A system driven to MIR saturation while `ℓ_ee` and `ℓ_mr` stay separated by orders of magnitude falsifies `P-Adjacency-Transport-Shared` without any viscosity measurement at all. ~~**This is the cheaper of the two tests** and it is newly available because §9.4 identified what the posit actually asserts.~~ **→ WITHDRAWN the same day.** It is not available at all: the two lengths are measured in **disjoint** windows in every established system. See `Note_FConverge_Run_2026-09-05.md` §5, and §§1–3 there for three findings that came out of establishing it — including one against §9 above.

### 9.9 Relation to the existing literature, checked before writing

Per checklist item 22. **The `η`–`ρ` link is not virgin ground.** Lucas & Hartnoll, *Resistivity bound for hydrodynamic bad metals*, PNAS **114**, 11344 (2017), bound the resistivity of an electron fluid whose mean free path is short compared with the scale of spatial inhomogeneities; in the viscous-momentum-relaxation picture the resistivity contribution *rises* with viscosity. **That is the opposite sign of correlation to `Λ = const`, which has `ρ ∝ 1/η`.** The regimes differ — theirs is momentum relaxation off long-wavelength inhomogeneity, ED's is the mean-free-path floor — so this is **not** a contradiction. **But where both apply, the sign of the correlation between `η` and `ρ` discriminates**, and that is a sharper experimental handle than either framework's own bound.

> **Citation to pin before submission.** The `ρ_DC ∼ η` proportionality is standard in the hydrodynamic-transport literature, but it is not stated in the PNAS abstract and **this section has not verified it against the body text.** Pin it, or drop the sign-contrast claim. *(Per checklist item 22(c): do not invent a section number to make it look pinned.)*

---

**Series context.** Transport twin of `Paper_V5UnifiedBudget`. Advances §4 of `Paper_P04TransportBudget_ResistivitySaturation` from "declared open" to "co-onset derived in form (§3), pairing corrected to MIR ↔ viscosity-floor (§8), exact ratio scoped." Origin: ED Interpretation Chronicle v3 LEAD #1b (2026-07-30). Next sub-target: derive `Π_p`, `Π_q` (momentum/charge content weight per Adjacency unit) → the hard `η_min : ρ_max` ratio, the ED-forced number behind the strange-metal Planckian-bounds unification.
