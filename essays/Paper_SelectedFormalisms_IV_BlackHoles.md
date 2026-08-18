# Selected Formalisms from the Event Density Framework
## IV. Horizons, Temperature, and the Information Ledger

**Allen Proxmire**
*2026-08-18. Draft. §1–§9 built from the six source papers, each read in full; every tier label is transcribed from the black-hole tiered-claims ledger, not inflated. Companion to Part I (gravity), Part II (quantum fields), Part III (substrate theorems).*

---

## Abstract

Event Density (ED) posits a discrete substrate of *events* fixed by thirteen postulated primitives, with the irreversible *commitment* of events, the arrow of time made physical, as its keystone. Parts I–III worked gravity, the quantum fields, and the substrate's own theorems. This paper works the most famous sector and is candid that it is the weakest-tiered: it **reproduces** black-hole thermodynamics through the substrate rather than deriving it, on the heaviest postulate stack in the corpus, with most of the standard numbers inherited. The organizing object is the $b→0$ **decoupling surface**, the substrate surface where cross-participation collapses, which is the black-hole-scale counterpart of the exact-locality boundary of Part III. On that surface we obtain, in order: the horizon as a decoupling surface (mechanism derived; its location $r_H$ and surface gravity $κ$ inherited from general relativity); the Hawking temperature $T_H = κ/2π$ from a substrate KMS condition (the thermal step derived, the Euclidean near-horizon structure inherited); the Bekenstein–Hawking entropy coefficient $S = A/4$ (the sector's one genuinely derived number, both factors from ED's own near-horizon Rindler geometry, but via the Euclidean continuation, so on par with general relativity, not beyond it); the area law and its measured one-bit-per-Planck-cell tiling (consilience, not a novel prediction); a Planck-mass evaporation remnant; and the Page curve (shape reproduced, scales inherited). The one forward bet among the results presented here is a non-thermal Hawking-spectrum correction $[1 − c₁(ω/ω_c)²]$, conditional on a stated parity postulate and testable only in analog-Hawking systems, distinctive but unconfirmed. We are explicit that the information paradox is *not generated* in ED in the sense of a structural ledger audit resting on a *postulated* substrate unitarity, not a constructive proof; full constructive unitarity, the substrate interior, the arrow-native $2π$, and the curvature emergence underneath every geometric count are all open. We state, at length, what the sector does not deliver.

---

## 1. The substrate, the $b→0$ surface, and the honest starting points

Event Density (ED) is a substrate ontology. Beneath the continuous fields and smooth spacetime of established physics it posits a discrete, graph-like layer of *events*, and treats the familiar continuum laws as coarse-grained readings of that layer. As in Parts I–III, this paper takes the substrate as given and works one sector, stating at each step what is derived and what is inherited. This sector needs that discipline more than any other, and so it is stated first and in full.

**Postulated, not derived.** The substrate is specified by thirteen primitives, P01–P13 (Paper_087), postulated, not derived, and not claimed minimal or unique. Every result below is a *conditional structural derivation*: given the primitives and the paper-specific postulates named at each step, the stated consequence follows. The arrow is the keystone: P11 (commitment irreversibility) is the substrate event at which a chain's multi-channel participation collapses to a single channel and no operation returns the post-commitment state to the pre-commitment one, with the one-way character supplied jointly by P11, time homogeneity (P13), and the strictly retarded participation kernel V1 (Theorem T18, Paper_093). The continuum objects that appear here (a horizon, a temperature, an entropy, a Page curve) are not primitives but coarse-grained readings of substrate participation, obtained when the scale separation holds (the direct coarse-graining transport, DCGT).

**The organizing object: the $b→0$ decoupling surface.** A black-hole horizon, in ED, is not first a geometric boundary. It is a substrate surface where the cross-bandwidth collapses. Define $Γ_{cross}(r)$ as the rate of V5-mediated cross-chain content transport across the sphere at radius $r$. Far from any mass it is of order unity; as substrate content accumulates and the cumulative-strain reading (P12) produces a steep near-horizon gradient, V5's finite memory can no longer maintain coherent cross-bandwidth across that gradient, and

> $Γ_{cross}(r) → 0$ as $r → r_H$.

The interior decouples. That collapse surface *is* the horizon, at substrate level, and its one-way character is statistical (the V5 envelope decays, and P11 forbids un-committing), not causal-geometric.

**The series tie.** This is a boundary of the same *kind* as Part III's A1 result: the decoupling boundary across which the controlled channel capacity is exactly zero, now at black-hole scale. Part III measured that a committed fact carries no signal across a decoupling boundary; the black-hole horizon is such a boundary made gravitational, and its "nothing gets out" is a *locality* fact (no controlled signal across the surface), the gravitational counterpart of Part III's exact channel-zero rather than a light-cone. Part I derived gravity as a reading of substrate participation; Part III showed locality is exact on the decoupling surface; Part IV is those two facts met at a horizon. We make the correspondence precise, and mark its one caveat, in §2.

**The honest starting points, stated up front.** This sector carries the heaviest postulate stack in the corpus and inherits most of its famous numbers, and burying that would be the one dishonesty the series cannot afford. So, plainly, before any result:

1. **The postulate stack is the heaviest in the corpus.** Roughly twenty paper-specific postulates carry the arc, most of them `P-V5-*` and cutoff/endpoint commitments. Every horizon result below is form-forced *conditional on* them.
2. **The numbers are inherited.** The surface gravity $κ$, the horizon location $r_H$, the black-hole geometry, the Page time $t_{Page}$, the remnant coefficient $c⋆$, the correction coefficient $c₁$, and the cutoff $ω_c = c/ℓ_P$ (matched to the substrate scale, not derived) are all inherited. ED supplies mechanism and *form*; it does not compute these magnitudes.
3. **The one genuine derivation is on par with general relativity, not beyond it.** The Bekenstein–Hawking coefficient $S = A/4$ is derived from ED's own near-horizon geometry (§3), but through the Euclidean continuation, the same tool GR uses. The arrow-native, continuation-free version is open, and may be a category error.
4. **The information-paradox "resolution" is a structural audit on a *postulated* unitarity**, not a constructive proof (§7). Full constructive unitarity is open. This paper never claims ED solves the information paradox.
5. **The one forward bet is unconfirmed and postulate-conditional.** The non-thermal Hawking correction (§6) is conditional on a stated parity postulate, its coefficient inherited, and it is testable only in analog-Hawking systems, not real black holes.

With those in view, the sector proceeds: the decoupling surface (§2), the temperature and the entropy coefficient (§3), the area law and its tiling (§4), the Page curve (§5), the one forward bet (§6), and the information ledger (§7).

---

## 2. The horizon as a $b→0$ decoupling surface

The first result is the horizon itself, read as a substrate mechanism rather than a geometric boundary.

**The mechanism.**

> As substrate content accumulates toward a black hole, the cumulative-strain reading (P12) produces a steep near-horizon gradient, and V5's finite memory $τ_{V5}^BH ∼ ℓ_P/c$ cannot maintain coherent cross-bandwidth across it. The cross-bandwidth $Γ_{cross}(r) → 0$ at $r → r_H$, below hydrodynamic-window resolution, and the interior decouples (Paper_039).

**Tier: Derived (mechanism).** The decoupling *mechanism*, the V5 envelope collapsing across the steep-gradient region, is a structural consequence of the primitives plus the V5 kernel. What follows from it is the horizon's one-way character: by P11 (no un-committing) together with the V5 collapse, committed content cannot cross the surface. This "one-way" is **statistical**, a property of the substrate-graph bandwidth structure, not the propagation of light rays in a metric.

**The honest identification.** The *location* is not derived here. The surface at which $Γ_{cross}$ collapses is matched to the general-relativistic horizon $r_H = 2GM/c²$ (Kerr: the outer horizon), and the surface gravity $κ$ is taken as the coarse-grained P12-gradient at that surface. Paper_039 is explicit that the direction of identification runs general relativity → substrate, not the reverse: $r_H$ enters as the coarse-grained reference point against which the substrate mechanism is positioned, and an independent substrate-level derivation of $r_H$ (and of $κ$) awaits the curvature-emergence program (Arc ED-10), which this paper does not deliver. The substrate claim is narrower, and sharper, than "ED derives the horizon": it is that the *microscopic identity* of the horizon is a cross-bandwidth collapse, coincident under coarse-graining with the GR surface whose location it inherits.

**The tie to Part III.** The decoupling surface is a boundary of the same kind Part III characterized. There, the controlled channel capacity between two substrate regions was measured to be exactly zero, common cause rather than signal, because there is no channel anywhere. Here, the horizon is such a boundary: $Γ_{cross} → 0$ is cross-region capacity going to zero, so the horizon's one-way character is a *locality* fact (no controlled signal across the surface), the gravitational counterpart of Part III's exact channel-zero rather than a causal trapping surface in a metric. One caveat keeps this a correspondence rather than a single measurement: Part III's exact zero was obtained on the V5-free certified substrate, while the horizon's collapse is V5-mediated, so the two are the same *kind* of decoupling read at different scales, not the identical experiment. The same reading extends to cosmic scale, where the cosmic horizon corresponds to the capacity-zero surface; the black-hole horizon is its local counterpart.

**Trans-Planckian resolution, and the remnant.** Two downstream consequences travel with the decoupling surface. First, the substrate's finite memory supplies a structural UV cutoff: V5 supports no modes above $ω_c = c/ℓ_P$, so the Hawking-spectrum derivation (§3) never generates the trans-Planckian extrapolation that troubles the semiclassical account (Paper_040). **Tier: D-via-I, conditional on `P-V5-UV-Cutoff` + `P-Cutoff-Saturation` (Paper_040); the cutoff $ω_c$ is matched to $ℓ_P$, not derived.** Second, evaporation halts when the dominant emission frequency reaches $ω_c$, at a stable Planck-mass remnant $M⋆ = ℏ/(cℓ_P) = M_P$ (a clean dimensional result using $G = c³ℓ_P²/ℏ$ from Part I). **Tier: D-via-I, conditional on the cutoff/endpoint postulates; the order-unity coefficient $c⋆ ≈ 1$ is inherited.** The remnant returns in §7, where it carries part of the information ledger.

---

## 3. The Hawking temperature and the entropy coefficient

The horizon has a temperature, and the temperature has a derivation with two genuinely different tiers: the thermal *relation* is derived from a substrate KMS condition, while the geometry it runs on is inherited. And the entropy *coefficient*, the celebrated $1/4$, is the one place this sector derives a number from ED's own structure, with an honest ceiling on how far that goes.

**The temperature.**

> Near the decoupling surface, the V5 cross-chain correlators acquire imaginary-time periodicity $β_H = 2π/κ$ from the smoothness of the near-horizon Euclidean geometry, which is the **KMS condition**, the defining property of a thermal state; so the substrate is thermal at $T_H = 1/β_H = κ/2π$ (Paper_047).

**Tier: the KMS-to-thermal step is Derived; $κ$ is Inherited; the Euclidean near-horizon structure is Inherited-via-DCGT.** The distinction is load-bearing and Paper_047 makes it in its own audit. The Euclidean continuation, the conical-defect smoothness, and the periodicity $β_H = 2π/κ$ are the standard semiclassical near-horizon structure, applied to substrate content through DCGT, not a substrate-level novelty. What is substrate-level is *where the periodicity lives*: in the V5 cross-chain correlators, so that the substrate kernel is itself thermal, rather than a matter field on a fixed background. Given that periodicity, the KMS condition and the Planck distribution at $T_H = κ/2π$ follow. The temperature *relation* is earned; the geometry it is read off is inherited.

**The entropy coefficient, the one genuine derivation.** The Bekenstein–Hawking entropy $S = A/4$ factors, through the first law, into $κ = 1/(2r_s)$ and the thermal $2π$ in $T = κ/2π$. ED derives both from one object, its own vacuum bandwidth profile $b(r) = 1 − r_s/r$ (GR-III):

> Expanding at the horizon with $κ = 1/(2r_s)$ gives $b ≈ 2κ(r − r_s)$; in proper radial distance $ρ$ this is $b = κ²ρ²$, so the near-horizon metric is $ds² ≈ −κ²ρ²dt² + dρ²$, the **Rindler form** (confirmed numerically, $b/(κρ)² → 1$). Continue to imaginary time: $ds_E² = κ²ρ²dτ² + dρ²$ is the flat plane in polar coordinates with $κτ$ the angle, smooth at the horizon point *only* if the angle runs a full $2π$. So $β = 2π/κ$, $T = κ/2π$, and $S = A/4$ (Paper_BH_Thermal2Pi).

**Tier: Derived, both factors from ED's own geometry, but via the Euclidean continuation, the same tool general relativity uses, so ED is on par with GR here, not beyond it.** The `½` is the slope of the derived b-profile; the $2π$ is the angle of one full turn around the horizon in ED's own near-horizon plane. This upgrades the coefficient from "half-inherited" (the earlier combinatorial route of Paper_043 *matched* a multiplicity $log g = π$ to standard quantum-statistical mechanics and thereby inherited the $1/4$) to structurally derived. But the tool is Euclidean continuation, and GR reads the same $2π$ off the same near-horizon geometry; ED's genuine addition is that the geometry is *derived* from the bandwidth rule rather than postulated.

**The honest open frontier.** ED's defining primitive is the *irreversible* arrow, and the Euclidean continuation is a *reversible-time* device. A fully substrate-native derivation would get the $2π$ from the commitment statistics directly, in real one-way time, with no continuation. Paper_BH_Thermal2Pi records an honest numerical negative on this (a direct real-time attempt did not produce the number) and, more tellingly, notes that even a *correct* real-time derivation gets the $2π$ from the gamma function $Γ(iω/κ)$, whose analytic structure at the horizon *is* the Euclidean periodicity in another guise. The reframe this forces is that the $2π$ may be an intrinsically **continuum / smooth-horizon** quantity, a feature of the analytic branch structure where outgoing modes connect across the horizon, which exists only once the smooth horizon exists, and which ED already has at that level (the Rindler form above). The continuation-free-from-raw-commitments target is therefore either a genuinely deep open problem or a category error; this is not settled, and the paper does not pretend it is.

---

## 4. The area law and its tiling

The horizon's entropy scales with its area, and the substrate both reproduces that form and, separately, counts the bits on the surface. Both are honest, and neither is more than it is.

**The form.** The area-law form $S ∝ A$ follows from reading the horizon as a participation surface: the entropy counts the substrate channels crossing it, which scale as the area. **Tier: D-via-I, conditional on `P-Horizon-Participation` + `P-Multiplicity-g`.** The combinatorial route to the *coefficient* (Paper_043) matches a multiplicity $log g = π$ to standard quantum-statistical mechanics and so *inherits* the $1/4$; the derived coefficient is the geometric route of §3, not this one. We keep the two routes distinct so the geometric derivation does not launder the combinatorial inheritance.

**The tiling.** Built directly, the horizon carries about one bit per Planck cell:

> Three counts converge on the surface bit-density: the holographic count gives 1, the frozen-state count ≈ 0.78, and the straddling-edge count ≈ 0.88 per Planck cell (Paper_HorizonTilingThreeCounts).

**Tier: Measured.** The honest reading, which the source states plainly, is that this is **consilience, not a novel prediction**, three routes landing on the same number, in the same discipline as "the grain fixes $G$ three ways is one fact, not three." And two of the three counts *assume the emergent geometry* they are counting on, which is exactly the piece (curvature emergence) that remains open underneath this whole sector. The tiling is a genuine, satisfying cross-check that the substrate carries the right number of degrees of freedom on a horizon; it is not an independent prediction, and it is not tiered as one.

---

## 5. The Page curve

If a black hole evaporates and the process is unitary, the entanglement entropy of its radiation must rise, turn over, and fall, the Page curve. ED reproduces that shape through a substrate mechanism, in a vocabulary different from the standard derivations, with the numerical scales inherited.

**The shape.**

> Early on, each emitted Hawking quantum carries V5 cross-chain entanglement-amplitude with the interior, so the interior-radiation entropy rises linearly. At $t_{Page}$, the substrate-level entanglement-bandwidth budget saturates and the rise turns over. Past saturation, accumulating entanglement re-routes through radiation-radiation and radiation-remnant correlations, and the interior-radiation entropy declines (Paper_050).

**Tier: the rise is Derived; the turnover and decline are Derived-conditional.** The linear rise follows from the Hawking-emission rate and entanglement accumulation. The turnover is conditional on `P-V5-EntBudget` (the substrate entanglement-bandwidth is bounded above), and the decline is conditional on `P-Re-routing` (post-saturation entanglement re-routes through alternative channels). The Page time $t_{Page} ≈ 0.54 τ_{BH}$ and the peak $∼ S_{BH}/2$ are **inherited** value-layer numbers; the substrate mechanism produces the *shape* (rise, turnover, decline), not the coefficients.

**What it is, and is not.** This is not a replica-wormhole or island-formula derivation. It is an alternative-vocabulary reproduction of the same empirical Page-curve shape that those continuum-gravity methods produce, in substrate-graph terms (entanglement-bandwidth saturation plus re-routing) rather than gravitational-path-integral terms. The two are descriptions of the same shape. The one place they part company empirically is the non-thermal correction of §6, which is the vehicle by which the re-routed information is carried out; without it, the late-time radiation would be exactly thermal and the "decline" would represent unitarity violation rather than information transfer.

---

## 6. The one forward bet: the non-thermal Hawking correction

Every result so far is a reproduction. This is the one distinctive forward bet among the results presented here, and it is an honest, modest one.

**The prediction.**

> $n_H^ED(ω) = n_H^Planck(ω) · [1 − c₁(ω/ω_c)² + O((ω/ω_c)⁴)]$

The late-time Hawking spectrum is not purely thermal: V5's finite cutoff $ω_c = c/ℓ_P$ imprints a correction that is sign-definite (a suppression), mass-dependent (negligible for astrophysical black holes, growing to order unity as $M → M_P$), and, at a softer tier still, in principle information-bearing. **Tier: D-via-I / Prediction** for the correction form; the information-bearing property is weaker, tiered A→P in the source (a structural *availability*, not a derivation): the deviation is the channel through which formation-state content *could* leave with the radiation, but the explicit encoding map is not derived (see §7).

**Every hedge, in the same breath.** This is the forward bet, and it is hedged on all sides. It is conditional on **`P-V5-Even`**, the postulate that the V5 envelope is parity-symmetric, which selects the *even* (quadratic) leading term; a parity-asymmetric envelope would give a *linear* leading term instead, and that linear-versus-quadratic scaling is the actual sharp test of the postulate, not a free confirmation. The cutoff $ω_c$ is matched to $ℓ_P$, not derived. The coefficient $c₁$ is order-unity and **inherited** from the V5 envelope shape (Gaussian gives $1/2$, exponential gives $≈ 1$). And it is testable only in **analog-Hawking** systems (Bose–Einstein condensate, fluid, optical analogs), whose natural cutoff sits close to their dominant emission frequency, not in astrophysical black holes, where the correction is $(T_H/T_P)²$ and unobservable. It is **unconfirmed**.

**What it is worth.** Weighed honestly, this is weaker than Part I's a₀(z): analog-only, postulate-conditional, coefficient inherited, and not yet measured. But it is a genuine distinctive falsifier: no firewall, ER=EPR, or soft-hair account predicts this specific sign-definite, mass-dependent, $(ω/ω_c)²$ form, and the linear-versus-quadratic scaling is a clean experimental discriminator of the underlying postulate. That is the honest half-step above a pure postdiction. (The arc also carries a provisional merger-lag prediction, Paper_052.5, existence-only and not refutation-grade, out of scope here; this section is the one forward bet among the results presented in this paper.)

---

## 7. The information ledger, honestly

The black-hole information paradox is the sector's gravitational center, and it is where an honest accounting matters most, because the temptation to overclaim is greatest. ED's position is that the paradox is *not generated* at substrate level, and the exact meaning of that phrase is the whole content of this section.

**What "not generated" means.**

> The paradox requires three ingredients together: exactly thermal Hawking radiation, complete evaporation, and global unitarity violation. ED modifies the first two (the radiation is not exactly thermal, §6; evaporation halts at a Planck-mass remnant, §2) and tracks the third through the Page curve (§5). The paradox-generating combination is therefore never assembled (Paper_051).

**The load-bearing soft spot, flagged plainly.** That composite verdict is a **structural ledger audit**, an A→position accounting of *where each ingredient is modified*, and it rests on two declared postulates: `P-Substrate-Unitarity` (substrate evolution is unitary on the full Hilbert space of system, decoupled cells, radiation, and remnant) and `P-Ledger-Completeness` (those four modifications are the complete list, with no fifth needed). Paper_051 states the tier in its own words: it is "a **structural** result (A→position), **not a constructive resolution** of the semiclassical paradox." So the honest sentence is not "ED solves the information paradox." It is: **ED audits where each paradox ingredient is modified at substrate level, conditional on a postulated substrate unitarity, and finds the paradox-generating combination is not assembled.** Full *constructive* unitarity, derived rather than postulated, is open, and is one of the sector's named open targets.

**What actually carries the information.** Two substrate features do real work in the audit without closing it. The Planck-mass remnant (§2) retains an information-carrying subspace, so the final state is not the mixed state from a pure initial state that the paradox requires. And the non-thermal correction (§6) is the proposed *vehicle*, the channel through which formation-state content can leave with the radiation, so that the Page-curve decline (§5) represents information transfer rather than loss. Both feed the ledger; neither is a proof; and the explicit map from formation state to spectrum features is itself not yet derived. The sector's honesty is that it says all of this out loud.

---

## 8. What this sector does not claim

The reproductions above are coherent, and for that reason the disclaimers matter more, not less. Stated plainly:

- **No confirmed prediction.** The one forward bet (§6) is analog-only, conditional on `P-V5-Even`, its coefficient inherited, and unconfirmed. Every other result in the sector is a reproduction.
- **The numbers are inherited.** $r_H$, $κ$, the black-hole geometry, $t_{Page}$, $c⋆$, $c₁$, and $ω_c$ are all inherited; ED supplies mechanism and form, not magnitudes. $r_H$ in particular is used as the coarse-grained identification point, not derived (curvature emergence, Arc ED-10, is open).
- **The one derived coefficient is on par with GR.** $S = A/4$ is derived from ED's own near-horizon geometry, but through the Euclidean continuation, the tool GR also uses; it is not a step beyond GR, and the arrow-native, continuation-free $2π$ is open (and may be a category error, since the $2π$ looks like a continuum feature).
- **The area-law tiling is consilience, not a prediction.** Three counts land on one bit per Planck cell; that is one fact seen three ways, and two of the three counts assume the emergent geometry.
- **The Page curve is a reproduction.** The shape is reproduced on `P-V5-EntBudget` + `P-Re-routing`; the scales ($t_{Page}$, peak) are inherited; it is not a replica-wormhole or island-formula derivation.
- **The information paradox is not "solved."** It is *not generated* only in the sense of a structural ledger audit resting on a *postulated* substrate unitarity (`P-Substrate-Unitarity` + `P-Ledger-Completeness`); full constructive unitarity is open (target #4). This is not a proof.
- **Open frontier:** constructive unitarity; the substrate black-hole interior ($r < ℓ_P$); the arrow-native $2π$; and, underneath every geometric count in the sector, curvature emergence.
- **Nothing is forced from nothing.** Every result is conditional on the thirteen primitives and on the roughly twenty paper-specific postulates of the arc, which are themselves postulated, not derived.

---

## 9. Appendix: tier table

Every load-bearing claim, with its tier transcribed from the black-hole tiered-claims ledger and verified against the source paper.

| Result | Claim | Tier | Inherited / open |
|---|---|---|---|
| 039 | Horizon = $b→0$ decoupling surface ($Γ_{cross}$ collapse) | **Derived (mechanism)** | $r_H$ + $κ$ inherited from GR (coarse-grained ID point) |
| 039 | One-way horizon = statistical (V5 collapse + P11); **correspondence** to A1 channel-zero at BH scale | **D-structural / interpretation** | same *kind* of decoupling; V5-mediated vs A1's V5-free — not the identical experiment |
| 039/040 | Trans-Planckian resolved (modes terminate at $ω_c$) | **D-via-I** | conditional on `P-V5-UV-Cutoff` + `P-Cutoff-Saturation` (Paper_040); $ω_c = c/ℓ_P$ matched, not derived |
| 039/041/048 | Planck-mass remnant $M⋆ = M_P$ | **D-via-I** | conditional on cutoff/endpoint postulates; $c⋆ ≈ 1$ inherited |
| 047 | Hawking temperature $T_H = κ/2π$ via V5-KMS | **Derived (KMS→thermal)** | $κ$ inherited; Euclidean conical structure **I-via-DCGT** |
| BH_Thermal2Pi | Bekenstein–Hawking coefficient $S = A/4$ (both factors) | **Derived (geometric)** | via Euclidean continuation = the tool GR uses (**on par, not beyond**); b-profile + $κ$ from GR-III; arrow-native $2π$ **OPEN** (possible category error) |
| 043 | Area-law **form** $S ∝ A$ | **D-via-I** | conditional on `P-Horizon-Participation` + `P-Multiplicity-g`; combinatorial 1/4 route **inherits** (log g) |
| HorizonTiling | Horizon tiles ~1 bit/Planck cell (3 counts: 1, 0.78, 0.88) | **Measured** | consilience "not a novel prediction"; 2 of 3 counts assume emergent geometry |
| 050 | Page curve: early linear rise | **Derived** | Hawking-rate accumulation |
| 050 | Page curve: turnover + decline | **D-conditional** | conditional on `P-V5-EntBudget` + `P-Re-routing`; $t_{Page} ≈ 0.54 τ_{BH}$ inherited |
| 050 | Page-curve reproduction is alternative-vocabulary | **Synthesis** | **not** replica-wormhole / island-formula |
| 039/047 | Non-thermal Hawking correction $[1 − c₁(ω/ω_c)²]$ | **D-via-I / Prediction** | conditional on `P-V5-Even`; $ω_c$ matched; $c₁$ inherited; **UNCONFIRMED**, analog-Hawking only |
| 051 | Information paradox "not generated" | **A→position (ledger audit)** | on `P-Substrate-Unitarity` + `P-Ledger-Completeness`; **NOT a constructive proof** |
| 051/050 | Full (constructive) substrate unitarity | **Open** | target #4 |
| BH_Thermal2Pi | Arrow-native (continuation-free) $2π$ | **Open** | possibly a category error ($2π$ a continuum feature) |
| 039/HorizonTiling | Curvature emergence underneath $r_H$, $κ$, tiling | **Open** | Arc ED-10 |

---

*Series context. Part IV of the Selected Formalisms series, after gravity (I), quantum fields (II), and the substrate's own theorems (III). This is the consilience sector: black-hole thermodynamics reproduced through the substrate on the heaviest postulate stack in the corpus, with one genuinely derived coefficient ($S = A/4$, on par with GR), one unconfirmed postulate-conditional forward bet (the non-thermal Hawking correction), and an information-paradox account that is a structural audit on postulated unitarity, not a proof. Its organizing object, the $b→0$ decoupling surface, is the black-hole-scale counterpart of Part III's exact-locality boundary; the sector's price, and its coherence, are stated as plainly as its results.*
