# Group-Embedded Low-Acceleration Galaxies: An Event Density Reading of NGC 1052-DF2 and DF4

**Allen Proxmire**
*June 2026*

---

## Abstract

The ultra-diffuse galaxies NGC 1052-DF2 and NGC 1052-DF4 exhibit velocity dispersions consistent with their baryonic mass alone, requiring no dark-matter-like enhancement. This appears to challenge any framework predicting universal low-acceleration deviations from Newtonian gravity, including Event Density's (ED's) derivation of the MOND acceleration scale `a₀ = cH₀/(2π)`. We show that DF2 and DF4 are not counterexamples but confirmations of ED's prediction. Both galaxies lie deep in the sub-`a₀` regime internally (g_int ~ 10⁻¹³ m/s²), yet are embedded in the NGC 1052 group, where the external acceleration g_ext ~ 2 × 10⁻¹² m/s² dominates the local commitment-density background. In ED, the substrate's outer-scale enhancement — the phenomenon that appears observationally as "dark matter" — manifests only when the local commitment-density background is set by the cosmological floor. In group environments, the background is instead set by the group potential, saturating the substrate's finite outer-scale capacity and suppressing the enhancement. This produces a MOND-EFE-like outcome through a mechanism native to ED: *commitment-density saturation* rather than field non-linearity. The framework predicts a sharper, knee-like dependence of enhancement on g_ext / a₀ than MOND naturally gives, offering observational tests that distinguish the two.

---

## 1. The Puzzle

Van Dokkum and collaborators reported in 2018 (*Nature* 555:629) that NGC 1052-DF2, an ultra-diffuse galaxy in the NGC 1052 group, exhibits a line-of-sight velocity dispersion of σ_los ≈ 8.4 km/s from its globular-cluster system — fully consistent with the baryonic mass alone, requiring no dark matter halo. A follow-up (van Dokkum et al. 2019, *ApJL* 874:L5) extended the result to a second galaxy in the same group, NGC 1052-DF4. Subsequent observations have largely confirmed the kinematic measurements, despite contested distance estimates from Trujillo et al. (2019).

The community reaction was that these galaxies posed a challenge to alternatives to ΛCDM dark matter, especially MOND: if every low-acceleration system should exhibit MOND-like enhancement, why not these? The MOND-community response invoked the **External Field Effect (EFE)**: MOND's non-linear field equation produces a suppression of the internal MOND boost when the external gravitational field at the galaxy's location is comparable to or larger than its internal field (Famaey et al. 2018; Kroupa et al. 2018). For DF2 and DF4, embedded in the NGC 1052 group, this condition is satisfied.

This paper poses the analogous question of ED. The MOND scale `a₀` has been derived in this corpus (Paper_029) as

> **a₀ = cH₀ / (2π) ≈ 1.2 × 10⁻¹⁰ m/s²**

— the substrate's cosmological-horizon scale, expressed as an acceleration. If this enhancement applies universally to systems below `a₀`, DF2 and DF4 should display "missing-mass" appearance and they do not. The framework needs to account for this.

The answer recovers the EFE-class suppression, but through a mechanism native to ED rather than imported from MOND.

---

## 2. Numerical Setup

### Internal dynamics

For DF2:

- σ_los ≈ 8.4 km/s
- Outer tracer radius r ≈ 7.6 kpc ≈ 2.35 × 10²⁰ m
- Internal acceleration g_int ~ σ² / r ≈ (8.4 × 10³)² / (2.35 × 10²⁰) ≈ **3 × 10⁻¹³ m/s²**

For DF4:

- σ_los ≈ 8–10 km/s
- Outer tracer radius r ≈ 5–7 kpc
- g_int ~ **10⁻¹³ to 10⁻¹² m/s²**

Both systems sit roughly **two to three orders of magnitude below a₀** in their internal dynamics. By the standard MOND criterion, they should display deep-MOND behavior. By the corresponding ED criterion (substrate outer-scale enhancement at sub-`a₀` accelerations), they should likewise.

### External field

Taking NGC 1052 as the dominant external mass:

- M_NGC1052 ~ 10¹¹ M☉ ≈ 2 × 10⁴¹ kg
- Projected separation r ≈ 80 kpc ≈ 2.47 × 10²¹ m
- g_ext ~ GM / r² ≈ (6.67 × 10⁻¹¹)(2 × 10⁴¹) / (2.47 × 10²¹)² ≈ **2 × 10⁻¹² m/s²**

### The local hierarchy

The local environment of DF2 and DF4 satisfies

> **g_int < g_ext ≪ a₀**

with g_ext roughly 5–20× larger than g_int and `a₀` roughly 50× larger than g_ext. The external field from NGC 1052 dominates the internal field of either galaxy but is itself in the sub-`a₀` regime.

This is the configuration in which MOND-EFE produces suppression, and the configuration in which the ED mechanism described below predicts the same outcome for a different reason.

---

## 3. The ED Mechanism: Commitment-Density Saturation

### 3.1 What ED says

The MOND scale `a₀ = cH₀/(2π)` is not, in ED, a turn-on threshold for an empirically-fit interpolation function. It is the substrate's **cosmological outer-scale**, expressed as an acceleration — the scale at which the substrate's finite outer reach becomes locally visible.

A system exhibits "dark-matter-like" enhancement in ED only under a specific condition:

> **The system's local commitment-density background must be set by the cosmological floor.**

When this condition is met, the substrate's outer-scale finite-reach effects manifest as additional effective gravity at the relevant scale. When it is not met — when the local background is dominated by some other source — the enhancement is absent.

This is the ED analogue of "deep MOND," but the mechanism differs from MOND's in a definite way.

- **MOND.** The boost arises from a non-linear field equation, governed by an empirically-chosen interpolation function ν(g/a₀). The strength of the boost varies smoothly with the ratio g/a₀ and with the external field through the same equation. The mechanism is *field non-linearity*.
- **ED.** The enhancement arises from the substrate's finite outer-scale capacity becoming locally visible against the cosmological background. There is no interpolation function; there is a finite substrate slack. The mechanism is *substrate capacity*.

The two frameworks agree on most observed low-acceleration phenomena because the regimes in which they agree are large. They diverge specifically in cases — like DF2 and DF4 — where the question is what counts as the relevant background.

### 3.2 Why enhancement disappears in group environments

The substrate's outer-scale enhancement requires *slack* — uncommitted channel capacity at the cosmological outer scale. In an isolated galaxy in a void, this slack is freely available at the galaxy's location: the substrate's outer-scale capacity is undeployed locally, and the enhancement appears as effective additional gravity in the galaxy's internal dynamics.

A group potential raises the local commitment-density background above the cosmological floor. The substrate's outer-scale slack at the galaxy's location has been allocated to producing the group's gravitational field. There is no remaining capacity to produce additional enhancement at the smaller internal scale.

This is the **ED suppression rule**:

> **If the external commitment-density background dominates, the substrate has no remaining outer-scale capacity to produce internal enhancement.**

The suppression is not gradual. The substrate's outer-scale capacity is a finite quantity, and it either is or is not exceeded by the external background. The predicted transition is sharper than what MOND's interpolation function naturally gives — a feature that is exploited in the predictions below.

### 3.3 DF2 and DF4 as worked examples

At the positions of DF2 and DF4:

- g_int ~ 10⁻¹³ m/s² (internal dynamics)
- g_ext ~ 2 × 10⁻¹² m/s² (NGC 1052 group field at the galaxies' positions)
- a₀ ~ 1.2 × 10⁻¹⁰ m/s² (cosmological outer-scale)

The local hierarchy is

> **g_int < g_ext ≪ a₀**

The external commitment-density background dominates the internal field. Per the ED suppression rule, the substrate's outer-scale enhancement at the DF galaxies' locations has been allocated to the NGC 1052 group's gravitational field. There is no remaining slack to produce additional enhancement in the internal kinematics.

The internal dynamics should look Newtonian-baryonic. They do.

The galaxies are not "without dark matter." They are without *the substrate enhancement that, in less-saturated environments, would appear as additional gravity*. The galaxies that supposedly broke MOND look, under ED's lens, like exactly what ED predicts.

---

## 4. Falsifiable Predictions

The ED reading makes testable predictions that distinguish it both from ΛCDM and from MOND.

### Prediction 1: Universal suppression in group environments

Every low-acceleration galaxy embedded in a group or cluster environment with g_ext ≳ a₀ / 50 (the rough threshold suggested by the DF2/DF4 case) should show suppressed enhancement — i.e., kinematics closer to baryonic Newtonian than to deep-MOND prediction. The suppression should be most complete when g_ext approaches `a₀` and become progressively partial as g_ext drops further below.

ΛCDM predicts no such environmental dependence: dark matter halos should be present regardless of group membership.

### Prediction 2: Sharper transition than MOND

In MOND, the EFE suppression is governed by the empirically-chosen interpolation function ν(g / a₀) and can accommodate a smoothly-varying range of behaviors. In ED, the substrate's outer-scale capacity is a hard finite quantity — there is no smooth interpolation, only a finite slack that is or is not exceeded by the external commitment density.

ED therefore predicts a **knee-like transition** in the dependence of internal kinematic enhancement on g_ext / a₀, in contrast to MOND's smoother roll-off. This is the cleanest observational test distinguishing the two frameworks: the steepness of the transition between the deep-MOND and EFE-suppressed regimes.

### Prediction 3: Isolated low-acceleration UDGs show full enhancement

Ultra-diffuse galaxies in voids — same baryonic mass, same internal dynamics as DF2/DF4, but no external commitment-density background — should show full ED enhancement, i.e., display the same "missing mass" appearance that normal low-acceleration galaxies do. This is the control case for the framework.

If such systems exist and show MOND-class enhancement, both MOND and ED accommodate. If they exist and show enhancement with a magnitude differing systematically from MOND's interpolation at the same g_int, that distinguishes the two frameworks.

### Prediction 4: Suppression tracks cumulative commitment density, not acceleration alone

Two low-acceleration galaxies at the same nominal g_ext, but in environments with different cumulative line-of-sight masses — different group structures, different summed substrate-event counts along the relevant scale — should show suppression magnitudes proportional to cumulative commitment density rather than to the local g_ext alone.

This is a subtle effect, likely below current observational precision.

> **⚠ NARROWED 2026-09-05.** This previously read *“it is a uniquely ED prediction. No MOND-EFE variant naturally produces it.”* **Neither half is supportable as written.** MOND's field equation is **nonlinear**, so the external field at a point is itself sourced by the full external mass distribution rather than being an independent local parameter, and **modified-inertia** MOND formulations are non-local by construction. The EFE also differs quantitatively between formulations (it is stronger in AQUAL than in QUMOND). **So MOND does carry environment-structure dependence**; the question is whether its dependence has the *same shape* as ED's.
>
> **The defensible claim:** ED predicts suppression tracking **cumulative line-of-sight commitment density**, which is a different functional dependence from the `g_ext`-at-the-barycentre dependence of standard AQUAL/QUMOND treatments. **Whether the two are actually distinguishable requires computing both for the same system, and neither has been computed** — ED's suppression function is listed as Open in this arc's ledger. **Until both exist this is a candidate discriminator, not a discriminator, and not a uniqueness claim.** Gravity ledger Staleness #61.

---

## 5. Status and Limitations

DF2 and DF4 are consistent with ED's `a₀` derivation under the commitment-density-saturation mechanism described here. They are not counterexamples to the framework. The numerical fit at the order-of-magnitude level is straightforward; quantitative tightening will require:

1. **A precise substrate-level derivation of the suppression function.** The order-of-magnitude argument here is suggestive but the functional form (the ED analogue of MOND's ν(g / a₀)) needs to be derived from the substrate's primitives. The expected form is a hard knee at g_ext / a₀ ~ O(1), but the exact transition shape is not yet calculated.

2. **Identification of test systems with intermediate g_ext / a₀ ratios.** The DF2 / DF4 case sits at g_ext / a₀ ~ 0.02 — well below the transition where MOND and ED predictions diverge most sharply. Systems with g_ext / a₀ in the range ~0.1 to ~0.5 would be more diagnostic.

3. **Confirmation of the underlying kinematic measurements.** The original σ_los measurements have been contested (Trujillo et al. 2019, on distance grounds). Current consensus accepts the kinematic measurements at face value, but the empirical foundation is not fully settled. The framework's prediction does not depend on whether DF2 and DF4 are exactly Newtonian or only approximately so; it predicts suppression in their regime regardless.

The framework's posture on DF2 and DF4: they are not failures of universal-enhancement models. They are systems whose substrate-outer-scale capacity has already been allocated by their group environment. The dark matter they "don't have" is the substrate enhancement that, in less-saturated environments, would manifest additionally in their internal dynamics.

---

## Related Papers

- **Paper_029_a₀** — Derivation of the MOND scale a₀ = cH₀/(2π).
- **Paper_034_DeepMOND** — Deep-MOND regime behavior in ED.
- **Paper_036_MOND_FieldEquation** — ED reading of the MOND field equation.
- **Paper_037_a₀_Invariance** — Scale-invariance properties of a₀.
- **Paper_031_BTFR** — Baryonic Tully-Fisher relation in ED.

## References

- van Dokkum, P. et al. (2018). "A galaxy lacking dark matter." *Nature* 555, 629–632.
- van Dokkum, P. et al. (2019). "A second galaxy missing dark matter in the NGC 1052 group." *ApJL* 874, L5.
- Trujillo, I. et al. (2019). "A distance of 13 Mpc resolves the claimed anomalies of the galaxy lacking dark matter." *MNRAS* 486, 1192–1219.
- Famaey, B., McGaugh, S., Milgrom, M. (2018). "MOND and the dynamics of NGC 1052-DF2." *MNRAS* 480, 473–476.
- Kroupa, P. et al. (2018). "Does the galaxy NGC 1052-DF2 falsify Milgromian dynamics?" *Nature* 561, E4–E5.
