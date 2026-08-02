# The Unified P04 Transport Budget: Viscosity and Resistivity Saturation Are One Adjacency-Band Wall

**Series:** Event Density (ED) Generative Papers — soft-matter / transport arc (P04 bounded-participation); transport twin of `Paper_V5UnifiedBudget`
**Author:** Allen Proxmire
**Status:** Working derivation draft (conditional structural derivation within the 13-Primitive Generative System). Identifies the single per-cell P04 budget both transport ceilings spend against (the Adjacency band), derives the *co-onset* relation (the R1-analog: one saturation event, two proxy shadows), and scopes the exact ratio (the R2-analog) as the remaining open step. Advances §4 of `Paper_P04TransportBudget_ResistivitySaturation`.
**Companions:** `Paper_079_P4_NN_Rheology` (viscosity ceiling `φ_max`), `Paper_P04TransportBudget_ResistivitySaturation` (resistivity ceiling `ρ_max`), `Paper_073_DCGT` (substrate→continuum, the cell), `Paper_087_13Primitives` (P04 four-band, P05, P08), `Paper_V5UnifiedBudget` (the template: one envelope, fixed ratios).

---

## Preamble — What This Paper Does NOT Claim *(written first per QC discipline)*

1. **The absolute ceilings are inherited.** `φ_max` and `ρ_max` (the MIR value) stay inherited, exactly as in `Paper_079` / the resistivity scoping paper. This paper claims a *relation between them*, not their values.
2. **The exact ratio is NOT derived here.** The commensurability's *value* requires two projection factors (momentum-content vs charge-content weight per adjacency unit) that the corpus does not supply. That is scoped (§4) as the remaining step, not delivered.
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
| Inter-locus transport is P05-only; both momentum & charge use Adjacency | **P (`P-Adjacency-Transport-Shared`)** | §2; grounded in P04+P05, declared |
| Finite per-cell `b_adj^max` | **form-forced** | P04 finiteness + additivity (DCGT §3.2) |
| Both ceilings = one event `f → 1` (R1-analog) | **D (form), conditional on §2** | §3 |
| **Co-onset prediction** (viscosity divergence & resistivity saturation together) | **D conditional → falsifiable** | §3 |
| Exact ratio `φ_max : ρ_max` = `Π_p/Π_q` | **OPEN** | §4; projection factors not derived |
| Absolute `φ_max`, `ρ_max`, `a_eff`, `b_adj^max` | **I** | inherited (as in Paper_079 / MIR / DCGT) |

## 6. Falsification Criteria

- **F-COONSET (the distinctive one):** in a system where one cell governs both transports, the viscosity divergence and the resistivity saturation onset at *different* substrate occupancies (no correlation between the jamming point and the MIR point beyond coincidence) — falsifies `P-Adjacency-Transport-Shared` / the one-wall claim. This is the near-term, ED-owned bet.
- **F-BAND:** demonstration that inter-locus transport uses a channel *other* than the P05/Adjacency band (a second, independent transport conduit) — falsifies the shared-budget identification (§2).
- **F-RATIO (pending §4):** once `Π_p/Π_q` is derived, a measured `φ_max : ρ_max` inconsistent with it — the R2-analog falsifier, the transport twin of `Paper_V5UnifiedBudget` F-R2.

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

**Sharpened distinctive prediction (upgrades F-COONSET).** In the strange-metal / quantum-critical regime — where MIR, Planckian resistivity, and the viscosity bound are all measured in one system — the resistivity ceiling and the viscosity floor are **one wall**: co-onset, commensurate at fixed `ℓ = a_eff`. Standard physics has no reason to unify them; ED forces it. **F-COONSET is upgraded to: MIR-resistivity ↔ viscosity-floor co-onset** (a live strange-metal question), replacing the KD-jamming ↔ MIR version.

**Honest tier:** the *unification* (one wall) and the *co-onset* are forced given `P-Adjacency-Transport-Shared`; the exact `η_min : ρ_max` coefficient stays inherited pending `Π_p`, `Π_q`. The identification of these floors with the standard names (MIR, KSS, Planckian) is consilience. The load-bearing risk is unchanged and now sharper: do charge and momentum truly share *one* adjacency band, or distinct channels within it (F-BAND)?

---

**Series context.** Transport twin of `Paper_V5UnifiedBudget`. Advances §4 of `Paper_P04TransportBudget_ResistivitySaturation` from "declared open" to "co-onset derived in form (§3), pairing corrected to MIR ↔ viscosity-floor (§8), exact ratio scoped." Origin: ED Interpretation Chronicle v3 LEAD #1b (2026-07-30). Next sub-target: derive `Π_p`, `Π_q` (momentum/charge content weight per Adjacency unit) → the hard `η_min : ρ_max` ratio, the ED-forced number behind the strange-metal Planckian-bounds unification.
