# Resistivity Saturation as a Grain-Floored Mott–Ioffe–Regel Limit — and the Unified P04 Transport Budget (Open)

**Series:** Event Density (ED) Generative Papers — soft-matter / transport arc (P04 bounded-participation)
**Author:** Allen Proxmire
**Status:** Working scoping draft (conditional structural derivation within the 13-Primitive Generative System). Extends the packing-budget-saturation postulate of `Paper_079` from viscosity to resistivity; identifies the one *distinctive* (non-inherited) prediction — a fixed commensurability between the two transport ceilings — and declares it OPEN, as the next target.
**Companions:** `Paper_079_P4_NN_Rheology` (Krieger–Dougherty via P04), `Paper_085_UniversalMobilityLaw` (the validated empirical anchor), `Paper_073_DCGT` (substrate→continuum), `Paper_087_13Primitives` (P04, P08), `Paper_V5UnifiedBudget` (the template for a *unified* budget with fixed ratios).

---

## Preamble — What This Paper Does NOT Claim *(written first per QC discipline)*

1. **ED does not *derive* transport saturation from P04 alone.** The viscosity/mobility ceiling is `Paper_079`'s **declared postulate `P-Packing-Budget-Saturation`** (P04 budget saturates near a maximum occupancy), with the Krieger–Dougherty form and `φ_max` **inherited** empirically. This paper's resistivity extension is the same tier: form-forced *given a parallel postulate*, value inherited. It is **not** a from-primitives derivation.
2. **No prediction of the ceiling value.** The resistivity ceiling `ρ_max` (the Mott–Ioffe–Regel coefficient, or any Planckian ℏ/k_BT scale) is **inherited**, exactly as `φ_max` and the exponent `n` are for viscosity. ED supplies the *existence and form* of the saturation, not its number.
3. **This is consilience, not a distinctive prediction — as it stands.** Resistivity saturation (the MIR limit) is already known. ED re-grounds it in bounded participation; that adds structural understanding, not a new falsifiable number. The single *distinctive* claim available — the viscosity/resistivity commensurability (§4) — is **declared OPEN here, not derived.**
4. **No new substrate primitives.** One new paper-specific postulate (`P-Scattering-Budget-Saturation`), parallel to `Paper_079`'s.

---

## Abstract

`Paper_079` grounds non-Newtonian viscosity divergence — Krieger–Dougherty `η ∝ (1−φ/φ_max)^{−n}` — in a **declared postulate**, `P-Packing-Budget-Saturation`: as packing occupancy approaches a per-cell maximum, the finite P04 bandwidth budget saturates and the transport coefficient diverges. `Paper_085` (the validated Universal Mobility Law) inherits that ceiling as an empirical anchor. We observe that the *same* postulate, applied to charge transport, forces a **resistivity ceiling**: as scattering occupancy approaches the per-cell budget, resistivity saturates rather than rising without bound. Its physical content is the **Mott–Ioffe–Regel (MIR) limit** — the carrier mean free path floored at the effective substrate cell (the emergent transport grain, DCGT-coarse-grained from P08), because the substrate carries no scattering structure finer than one hop. This is *consilience*: ED re-grounds a known limit, at the same honest tier as the mobility law (form-forced-given-postulate, value-inherited). The one piece of *distinctive* content is not the value but a **relation**: if a single finite P04 bandwidth budget underlies both ceilings, the viscosity limit `φ_max` and the resistivity limit `ρ_max` are not independent but stand in a fixed ratio tied to the common grain — the transport analog of `Paper_V5UnifiedBudget`'s `1 : 1 : 0.88`. That **unified P04 transport budget** is the falsifiable content ED would own; it is not yet derived, and it is the declared next target (§4).

---

## 1. The honest starting point (correcting an easy overstatement)

It is tempting to say "ED derives the mobility-saturation law from bounded bandwidth." It does not, and the audit trails say so:

- `Paper_085` §2.5: the concentration-dependent decrease is **I** (Krieger–Dougherty, Paper_079); the coefficients including `c_max` are **I** (empirical matching). It is an **"empirical anchor,"** not a derivation.
- `Paper_079` §2.5: the packing-saturation divergence is **`P-Packing-Budget-Saturation`** (a declared postulate); the KD form and `φ_max`, `n` are **I**.

So the validated result is **form-forced *given a postulate*, value inherited.** Any extension inherits that ceiling of rigor. Stating this plainly is the precondition for an honest resistivity claim.

## 2. The parallel postulate and the resistivity ceiling

**`P-Scattering-Budget-Saturation` (declared, parallel to `Paper_079`'s):** *As the scattering-configuration occupancy at an (emergent) transport cell approaches the cell's finite P04 bandwidth budget, the budget saturates; the carrier mean free path cannot fall below the cell, and resistivity saturates at a ceiling `ρ_max` rather than rising without bound.*

Mechanism (same shape as `Paper_079` §3.1, charge instead of momentum): P04 makes the per-cell admissible-configuration budget **finite**; increasing scattering (interaction strength, temperature, disorder) consumes it; once saturated, no further scattering structure fits, because the substrate supports none finer than one hop (P08, DCGT-coarse-grained to the transport scale). The mean free path is floored at the cell size `a_eff`; resistivity is capped.

**This is the Mott–Ioffe–Regel limit.** MIR: resistivity saturates when `k_F ℓ ~ 1`, i.e. the mean free path reaches the lattice spacing. In ED that lattice spacing *is* the effective transport cell `a_eff`, and the flooring is not an empirical rule of thumb but the P04 budget hitting its per-cell wall. The quantum-simulation demonstration of collision-driven resistivity saturation in an optical lattice (the article that seeded this lead) is a clean instance: the lattice site is `a_eff`, and the saturation is the budget wall.

## 3. Honest tier — existence/form forced (given the postulate), value inherited

| Piece | Status |
|---|---|
| A finite per-cell P04 budget exists | **P04 (primitive), finite** |
| Scattering saturates it → resistivity ceiling exists | **P (`P-Scattering-Budget-Saturation`)**, parallel to Paper_079 |
| Ceiling = MIR (mean free path floored at `a_eff`) | **identification / consilience** with standard MIR |
| Ceiling *value* `ρ_max` (MIR coefficient; Planckian scale) | **I (inherited)**, like `φ_max`, `n` |
| Saturation *form* (vs monotonic rise) | **form-forced given the postulate** |

So resistivity saturation is **consilience with MIR**, at the same tier as the mobility law. It is *not* a distinctive value-prediction, and it should not be sold as one. (The deeper Planckian bound `τ ~ ℏ/k_BT`, a scattering-*rate* bound rather than a mean-free-path bound, is a further and more contested question; ED's per-cell budget most directly gives MIR, not Planckian, and the Planckian tie is left open.)

## 4. The distinctive content, declared OPEN — the unified P04 transport budget (next target)

The one thing here ED could *own* is not a value but a **relation**, exactly as with the V5 budget. `Paper_V5UnifiedBudget` took three separately-postulated V5 budgets and showed they are one envelope `W_max` seen three ways, forcing fixed ratios `1 : 1 : 0.88` — inherited *scale*, but forced *ratios*, and the ratios are the falsifiable content.

The transport analog: **do the viscosity ceiling `φ_max` (momentum transport) and the resistivity ceiling `ρ_max` (charge transport) descend from one finite P04 bandwidth budget per cell?** If yes, they are not independent inherited numbers; they stand in a **fixed ratio tied to the common grain `a_eff` and the common bandwidth budget** — a `φ_max : ρ_max`-type commensurability that no standard account (Krieger–Dougherty and MIR are unrelated in conventional physics) predicts. That relation would be:

- **non-inherited** (the individual ceilings' values stay inherited, but their *ratio* would be forced),
- **falsifiable** (measure both ceilings in a system where the same substrate cell governs both — e.g. a dense charged colloid, a molten salt, an electron liquid with a viscosity — and test the forced ratio),
- and the **transport-sector twin of the V5 unified budget**.

**This is not derived here.** It requires: (i) a single per-cell budget quantity that both momentum and charge transport spend against; (ii) the two projection factors (the momentum-vs-charge analogs of `ρ_loc` and `f_ent·g_∂`); (iii) the common `a_eff` renormalization (the DCGT analog of the `ℓ_V5` renormalization that cancels in V5 ratios). That derivation — **"the unified P04 transport budget"** — is the declared next target, and it is where the only distinctive, ED-owned prediction in this arc lives.

## 5. Falsification Criteria

- **F-EXIST:** charge transport that continues rising without any saturation, with the mean free path driven below `a_eff` under control of confounds — falsifies `P-Scattering-Budget-Saturation`. (Note: MIR saturation is already observed, so this is a *consilience pass*, not a new bet.)
- **F-RATIO (the distinctive one, pending §4):** in a system where one substrate cell governs both momentum and charge transport, the measured `φ_max : ρ_max` ratio is inconsistent with the forced value — falsifies the unified P04 transport budget (the analog of `Paper_V5UnifiedBudget` F-R2). This is the falsifier worth chasing; it does not exist until §4 is derived.

## 6. Position Statement

Resistivity saturation extends `Paper_079`'s bounded-bandwidth postulate from momentum to charge transport: a finite per-cell P04 budget floors the mean free path at the effective grain and caps resistivity — the Mott–Ioffe–Regel limit, re-grounded in participation. Honestly tiered, this is **consilience** (a known limit given a substrate origin), at the same level as the validated mobility law: form-forced given a declared postulate, value inherited. The *distinctive* content is not the ceiling but the **commensurability** — whether one P04 budget forces a fixed ratio between the viscosity and resistivity ceilings, the transport twin of the V5 unified budget's fixed ratios. That relation is falsifiable and ED-owned, and it is **not yet derived**; the **unified P04 transport budget** is the declared next target.

**What this paper claims:** the resistivity ceiling as a grain-floored MIR limit under `P-Scattering-Budget-Saturation` (consilience, value inherited); the identification of the viscosity/resistivity commensurability as the only distinctive, non-inherited content. **What it does not:** the ceiling value, the Planckian tie, or the commensurability relation itself (declared open, §4).

---

**Series context.** Soft-matter / transport arc. Companion to `Paper_079` (viscosity) and `Paper_085` (mobility, validated). Origin: ED Interpretation Chronicle v3 LEAD #1 (resistivity-saturation ceiling), on the optical-lattice resistivity-saturation quantum simulation (2026). The next target is the unified P04 transport budget (§4), the transport analog of `Paper_V5UnifiedBudget`.
