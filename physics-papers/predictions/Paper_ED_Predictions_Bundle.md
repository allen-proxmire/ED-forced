# Event Density: Empirical Predictions from a Substrate-Level Identification of $a_0 = cH_0/(2\pi)$

**Series:** Wave-3 Empirical-Predictions Bundle (cross-arc; primary outreach paper)
**Status:** Compilation of ten ED empirical predictions across gravity, GW, matter-wave interferometry, soft-matter, and analogue-gravity arcs. Three published Wave-3 prediction papers + seven session-ready experimental protocols + one passed test (GW170817) + three postdictions (including the UDM data-match — a self-authored Zenodo preprint, **not** peer-reviewed) + cross-scale falsifiers. Verdict across the bundle: every prediction is form-IDENTIFIED or form-FORCED from the substrate primitives; numerical content where present is INHERITED unless otherwise noted; falsification criteria explicit per prediction.
**Date:** 2026-05-17
**Anchors:** Paper_087 (13 primitives); Paper_095 (form-FORCED / value-INHERITED methodology); Paper_027 (Newton's $G$); Paper_029 ($a_0 = cH_0/(2\pi)$); Paper_030 (ED Combination Rule); Paper_031 (BTFR slope-4); Paper_034 (deep-MOND asymptotic); Paper_036 (MOND field equation); Paper_038_5 (Λ-smallness reframing; M3 retroactive); Paper_038_6 (Pred_WeakLensing_Activity); Paper_047 (Hawking spectrum); Paper_052_5 (Pred_MergerLag); Paper_089 (V1 retarded kernel); Paper_090 (V5 cross-chain kernel); Paper_ED_Cos_05 (Dark Energy; M3 unconditional); Paper_ED_GW_00 (GW); Universal Mobility Law paper (self-authored Zenodo preprint, May 2026; not peer-reviewed); ED-SC 4.x arc; protocols in `predictions/`: QC-Mass-Extrapolation, FRAP-High-BSA, AFM-Dewetting-ED-SC, ED-Acoustic-BEC-Extremal, ED-Acoustic-EIT-Extremal, ED-Acoustic-OpticalPulse, ED-09.5 Participation-Envelope, Triad-Coupling-C7, ED-RLC-Analogue.

---

## §1 Introduction

The Baryonic Tully-Fisher Relation (BTFR) is one of the tightest empirical relations in galactic astrophysics: across roughly four decades of baryonic mass, the asymptotic flat rotation velocity $v_{\mathrm{flat}}$ of a galaxy satisfies $v_{\mathrm{flat}}^n \propto M_b$ with $n = 3.95 \pm 0.08$ — consistent with $n = 4$ exactly, with scatter dominated by observational uncertainty. The Event Density (ED) substrate-ontology research program derives **BTFR slope exactly 4 with zero intrinsic scatter in the deep-MOND asymptote** from substrate primitives, with no halo modeling and no free parameters, via composition of Newton's $G$ from substrate constants (Paper_027), the substrate-level identification of the MOND transition acceleration $a_0 = cH_0/(2\pi)$ (Paper_029), the ED Combination Rule $a = \sqrt{a_N \cdot a_0}$ (Paper_030, conditional on a single declared postulate P14), and the standard circular-orbit condition $v^2/R = a$.

The BTFR result is the wedge for this paper. The same substrate-level identification — that $a_0$ is the azimuthal-Fourier projection of the cosmic decoupling surface $R_H = c/H_0$ onto an accelerating chain's dipole mode, producing the geometric $1/(2\pi)$ structurally — generates a family of related predictions across the corpus's empirical-prediction sector. This paper bundles ten such predictions: three published Wave-3 prediction papers, seven session-ready experimental protocols, plus three postdictions (including the UDM data-match, self-published on Zenodo — not peer-reviewed) and one cross-scale-covariation prediction. Each prediction is presented with its substrate-level mechanism, its sharpest falsifier, and (where applicable) the experimental platform and protocol status.

ED's methodological discipline (Paper_095) is *form-FORCED / value-INHERITED*: structural forms are derived from substrate primitives; numerical magnitudes are inherited from empirical matching. This paper inherits that discipline throughout. Where a prediction's numerical content is INHERITED rather than substrate-derived, it is named as such — not hidden.

---

## §2 BTFR slope-4 with zero intrinsic scatter (sharpest empirically-clean falsifier)

**Prediction.** $v_{\mathrm{flat}}^4 = G M_b a_0$ exactly, with zero intrinsic scatter, in the deep-MOND asymptotic regime ($a_N \ll a_0$).

**Substrate derivation chain (Paper_031):**

1. Newton's law $a_N = GM/R^2$ with $G = c^3 \ell_P^2/\hbar$ (Paper_027).
2. Transition acceleration $a_0 = cH_0/(2\pi)$ (Paper_029; see §3 below for derivation).
3. ED Combination Rule $a = \sqrt{a_N \cdot a_0}$ in the joint weak-gradient regime (Paper_030, conditional on P14 Bilocal Strain Coupling).
4. Circular-orbit condition $v^2/R = a$ (standard kinematics).

Composition: $v^2/R = \sqrt{(GM_b/R^2) \cdot a_0} = (1/R)\sqrt{GM_b a_0}$, giving $v^2 = \sqrt{GM_b a_0}$ — radial dependence cancels exactly. Squaring: $v^4 = GM_b a_0$. **Slope exactly 4; intrinsic scatter exactly zero in the asymptote.**

**Why this is sharp.** Three competing frameworks attempt BTFR:

- **Dark-matter cosmology:** slope-4 emerges from coincidence in tuned halo profile distributions; tightness is a tuning coincidence.
- **MOND as phenomenology:** slope-4 is built in by construction.
- **ED substrate:** slope-4 is *derived* from a substrate-level identification (Paper_027 + Paper_029 + Paper_030 + circular-orbit kinematics); no halo modeling, no free parameters, no tuning.

**Test.** SPARC galaxy-rotation-curve catalog (Lelli, McGaugh, Schombert 2016): publicly available, well-characterized observational systematics. Slope-4 + zero-scatter prediction is directly testable against the deep-MOND asymptotic subset of SPARC. The McGaugh-Lelli-Schombert 2016 measurement $n = 3.95 \pm 0.08$ is *consistent with* slope-4; the residual scatter is *consistent with* observational uncertainty. ED predicts that any future increase in measurement precision tightens the slope toward 4 exactly and the residual scatter toward zero.

**Sharpest falsifier (F1).** Deep-MOND-asymptotic BTFR slope significantly different from 4 beyond observational uncertainty refutes Paper_030's ECR via P14, refutes Paper_031's composition, or refutes Paper_029's substrate-level identification of $a_0$. Equivalently: detection of intrinsic (non-observational) scatter in the deep-MOND-asymptotic BTFR refutes the radial-cancellation derivation. Currently consistent at all SPARC precision.

---

## §3 $a_0 = cH_0/(2\pi)$: the transition acceleration from substrate-level dipole projection

**Prediction.** The MOND-class transition acceleration is

$$
a_0 = \frac{cH_0}{2\pi} \approx 1.08 \times 10^{-10} \text{ m/s}^2
$$

with $H_0 \approx 70$ km/s/Mpc inherited from cosmology. The empirically measured MOND value is $a_0^{\mathrm{MOND}} \approx 1.2 \times 10^{-10}$ m/s² — match within ~10% with **zero free parameters**.

**Substrate derivation chain (Paper_029):**

1. **Cosmic decoupling surface** at $R_H = c/H_0$ (Paper_028): beyond this radius, substrate-level cross-locus influence cannot reach a local chain coherently. This is the substrate-level effective boundary set by the kernel-propagation-rate / Hubble-expansion-rate crossover.
2. **Dipole-mode projection** of cosmic content onto an accelerating chain. An accelerating chain breaks the full substrate $SO(3)$ rotational symmetry to the residual $SO(2)$ symmetry about the acceleration axis. The leading anisotropic mode is the dipole ($l=1$); higher multipoles are higher-order in $|\vec a|/c$.
3. **Azimuthal-Fourier normalization** of the dipole's $|m| = 1$ projection on the residual $SO(2)$ (Paper_029 §5.1 dipole-projection integral): the Fourier-mode normalization on the circle of period $2\pi$ produces the geometric factor $1/(2\pi)$.

Composition: $a_0 = cH_0 \cdot (1/(2\pi)) = cH_0/(2\pi)$. The factor of $2\pi$ is **geometrically forced** by azimuthal-Fourier-mode normalization, not phenomenologically fit. **[DISPUTED 2026-09-04 — the `1/(2π)` is not established as forced.** The azimuthal-Fourier normalization does **not** survive: `Paper_028` §6.3 and `Paper_029` §5.1 both evaluate the azimuthal integral to **1**, so the factor cancels in their own displayed algebra and is reinstated at an assembly step by a normalization fixed nowhere. Re-tiered **Postulated / disputed**; see `Gravity_TieredClaims_Ledger.md` Staleness #10. **Unaffected:** `a₀ ~ cH₀`, reached three independent ways, and `a₀(z) = cH(z)/(2π)` with its forced exponent of 1.]**

**Why this matters.** Neither dark-matter cosmology nor MOND-as-phenomenology derives $a_0$. The empirical observation that $a_0 \approx cH_0$ has been recognized for decades as suggestive of a cosmological connection (Milgrom 1983 and subsequent), but no structural mechanism has been provided. ED supplies the mechanism via dipole projection of $R_H$ onto an accelerating chain's anisotropic adjacency — and forces the precise $1/(2\pi)$ factor.

**Sharpest falsifier (F2).** Independent observational refinement of $H_0$ inconsistent with the substrate-derived $a_0 = cH_0/(2\pi)$ relation at observed MOND $a_0$ refutes Paper_029's dipole-projection mechanism. Hubble-tension-class shifts of $H_0$ should produce *synchronized* covariation of $a_0$ at the substrate-derived rate (linear in $H_0$). Hubble tension shifting $H_0$ without corresponding shift in observed $a_0$ would refute the substrate identification.

**Post-Route-A status (2026-05-17).** The Route A audit cascade closes $H_0$ at substrate-parameter-INHERITED level (Paper_027-analog) via $H_0 = (8\pi/3)^{1/2} \ell_P c^{1/2} \Theta_{\mathrm{ED}}^{1/2}$. $a_0$ correspondingly tightens to: $a_0 = (c/(2\pi)) \cdot (8\pi/3)^{1/2} \ell_P c^{1/2} \Theta_{\mathrm{ED}}^{1/2}$ — all factors substrate-parameter-INHERITED at primitive level (analog of Paper_027's inheritance of $\ell_P, \hbar, c$).

---

## §4 Weak-lensing activity-dependence (Paper_038_6)

**Prediction.** Weak-lensing convergence signals are **activity-dependent**: galaxies and clusters in high-activity states (star-forming, AGN-active, dynamically unrelaxed) produce enhanced weak-lensing signals compared to low-activity (quiescent, relaxed) systems matched in baryonic mass + total mass + redshift.

**Substrate mechanism (Paper_038_6).** High activity corresponds to large local V5 cross-chain mobility gradients ($\nabla \mu$). Per Paper_EDSC_AcousticMetric_CurvatureConcentration, acoustic-metric curvature scales as $R_{\mathrm{ac}} \propto |\nabla \mu|^2/\mu^2$. This modifies the deep-MOND interpolation function:

$$
\mu_{\mathrm{eff}}(x) = \mu_{\mathrm{MOND}}(|\nabla \Phi|/a_0) \cdot [1 + \alpha_{\mathrm{act}} \mathcal{A}(x)]
$$

where $\mathcal{A}(x)$ is the activity-indicator functional and $\alpha_{\mathrm{act}}$ is the substrate-coupling. The structural scaling form is FORM-FORCED; both $\alpha_{\mathrm{act}}$ and $\mathcal{A}(x)$ are currently VALUE-INHERITED.

**Test.** Stratify existing weak-lensing surveys (KiDS, DES, HSC; upcoming LSST/Vera Rubin + Euclid) by activity proxies (star formation rate; AGN classification; dynamical relaxation indicators) at fixed mass + redshift. Compare lensing convergence amplitude across activity bins.

**Sharpest falsifier (F3).** Activity-independent weak-lensing convergence at deep-MOND-regime radii across all examined activity bins refutes the V5-mobility-gradient mechanism (Paper_038_6 §3.4).

**ED-vs-CDM-with-feedback discriminator status.** Standard ΛCDM-with-feedback also predicts some activity-dependence of inferred halo mass (via baryonic feedback histories). The **discriminator observable** — a $|\nabla \mu|^2$-vs-feedback-proxy observable that distinguishes the substrate-V5 mechanism from feedback histories — is OPEN. Pred_ classification PROVISIONAL until this discriminator is constructed.

---

## §5 GW merger-lag existence prediction (Paper_052_5)

**Prediction.** Compact-binary mergers (BH-BH, NS-NS, BH-NS) exhibit a **dynamical delay** $\tau_{\mathrm{lag}}$ between the standard-relativistic predicted merger time and the substrate-level actual merger completion.

**Substrate mechanism (Paper_052_5).** Three substrate contributions to the delay:

1. **V5 finite-memory dissipation** (Paper_090): substrate cross-chain bandwidth needs to redistribute during merger; redistribution timescale is $\tau_{V_5}$.
2. **Mobility-gradient acoustic-metric curvature** (Paper_EDSC_AcousticCurvature): merger events involve large local mobility gradients; acoustic-metric curvature on these scales modifies effective dynamics.
3. **Kernel cascade across scales** (Paper_091): merger events span multiple substrate scales (compact-object substrate-cell scale → merger-event scale → post-merger-relaxation scale).

The **existence** of the delay is form-IDENTIFIED. Specific numerical lag magnitudes are INHERITED.

**Honest scope.** This is *not* a refutation-grade prediction in the BTFR-slope-4 sense. The substrate-anchored floor $\tau_{V_5}^{\min}$ is OPEN; only existence-of-delay is predicted at refutation-grade level. Pred_ classification PROVISIONAL pending substrate-anchored $\tau_{V_5}$ floor.

**Test.** LIGO/Virgo/KAGRA + future Einstein Telescope / Cosmic Explorer / LISA: residual analysis of compact-binary merger waveforms against standard-relativistic predictions. Existence of systematic lag (positive sign, multiple uncorrelated events) supports the substrate-V5 mechanism.

**Sharpest falsifier (F4, conditional).** Once substrate-anchored $\tau_{V_5}^{\min}$ floor is supplied: observation of merger-lag systematically *below* the derived floor across uncorrelated systems refutes the substrate mechanism.

---

## §6 Quantum-to-classical mass wall at 140–250 kDa (QC-Mass-Extrapolation protocol)

**Prediction.** In matter-wave interferometry, the coherence fraction $V_{\mathrm{coh}} = V_{\mathrm{measured}}/V_{\mathrm{env}}$ crosses a quantum-to-classical (Q-C) transition at $V_c \approx 0.304$. A two-point coherence trajectory anchored at Eibenberger 2013 (~10 kDa, $V_{\mathrm{coh}} \approx 0.82$) and Fein 2019 (~25 kDa, $V_{\mathrm{coh}} \approx 0.76$) extrapolates the crossing to **molecular mass $m_c \in [140{,}000, 250{,}000]$ amu** — 5–10× beyond current Arndt-group experimental reach.

**Secondary distinguishing prediction.** In the $D < 0.1$ sector approached as $V_{\mathrm{coh}} \to V_c$, ED predicts **second-harmonic interference content at 3–6%** in fringe data residuals. Standard decoherence theory predicts pure first-harmonic decay. **CONFOUND (2026-07-24):** the Talbot–Lau / KDTL interferometers in this mass range produce higher harmonics from their grating optics regardless of ED, so a bare second harmonic does *not* confirm the prediction. A real test requires *excess* beyond the full Nimmrichter–Hornberger optics model, computed from **raw** fringe data (published interferometry papers release fitted visibilities only). This is therefore *not* a clean near-term test; it has a distinctiveness problem. (Distinct from the FRAP/triad *third*-harmonic signature elsewhere in this bundle, which is unaffected.)

**Test platform.** Long-baseline matter-wave interferometry — LUMI-class (Arndt group, Vienna) or successor instrument capable of $m > 100$ kDa. Candidates:
- **LUMI extension** (Vienna) — natural home; designed extensible
- **MAQRO / space-based concepts** — design mass reach $m \sim 10^6$ amu; >10-year horizon
- **Next-generation OTIMA / Talbot-Lau variants** — under discussion in Arndt-group roadmap

**Sharpest falsifier (F5).** $V_{\mathrm{coh}}$ crossing at $m_c < 100{,}000$ amu or $m_c > 400{,}000$ amu refutes the two-point extrapolation under either linear or exponential fit.

**Protocol status.** Stub proposal drafted 2026-04-28; three blockers before fully-specified protocol (promotion of affine $D_P \to D_E$ mapping from CANDIDATE to FORCED; apparatus envelope $V_{\mathrm{env}}(m)$ characterization for $m > 100$ kDa; molecular library at target mass scale). **Primary collaboration targets:** Markus Arndt (Universität Wien); Yaakov Fein (Cambridge); Stefan Gerlich (Vienna); Klaus Hornberger (Duisburg-Essen). Secondary: MAQRO consortium.

**Pre-registration epistemic move.** The prediction is publicly pre-registered (Zenodo DOI + this paper) before any experiment in the target range is published. Stub-now-execute-later is the appropriate posture for an outsider research program.

---

## §7 FRAP mobility scaling in concentrated BSA (UDM law protocol)

**Prediction.** Fluorescence Recovery After Photobleaching (FRAP) in concentrated BSA-FITC at 200–350 mg/mL follows the ED Universal Degenerate-Mobility (UDM) law $M(\rho) = M_0(\rho_{\max} - \rho)^\beta$ with canonical $\beta \approx 2$. This produces the 2D porous-medium equation with $m = \beta + 1 = 3$, giving front-radius exponent:

$$
\alpha_R = \frac{1}{d(m-1) + 2} = \frac{1}{6} \approx 0.167.
$$

Predicted observable: $R(t) \sim t^{1/6}$ with **sharp** bleach boundary (compact support, PME signature).

**Null prediction (Fickian).** $R(t) \sim t^{1/2}$ with Gaussian-blurred boundary.

**Test platform.** Standard confocal FRAP on concentrated BSA-FITC at 200, 250, 300, 350 mg/mL ($\phi$ = 0.15, 0.18, 0.22, 0.25). 5 bleaches per concentration, 20 total acquisitions.

**Sharpest falsifier (F6).** Observed $\alpha_R \geq 0.35$ or Fickian-front winning at all concentrations refutes the UDM mobility-channel mechanism. PASS criterion: $\alpha_R \in [0.125, 0.170]$ at $\geq 3/4$ concentrations + PME-front beats Fickian via AIC.

**Protocol status.** Protocol submitted to Creative Proteomics CIBR on 2026-04-17; decision window 2026-04-24 to 2026-05-01. **Budget:** $500–$1500 for session; 6–8 weeks calendar time to publishable result. This would be a genuine **forward test** via a different observable (front propagation rather than diffusion-coefficient regression), independent of the postdictive UDM data-match. The Universal Mobility Law paper (self-authored Zenodo preprint, May 2026; not peer-reviewed) provides the prior empirical anchor; see §11 below.

---

## §8 AFM thin-film polymer dewetting cross-scale test (AFM-Dewetting-ED-SC protocol)

**Prediction.** ED-SC 2.0 architectural invariance: the motif-conditioned median of the field-space Hessian eigenvalue-ratio distribution satisfies

$$
\mathrm{med}(\mathcal{R}_{\mathrm{motif}}) = r^* \approx -1.30 \in [-1.50, -1.10]
$$

on 2D real-space scalar density fields. Reference system: Scenario D at $(n^*, \sigma^*) = (2.7, 0.0556)$ gives $\mathrm{med}(\mathcal{R}_{\mathrm{motif}}) = -1.304$.

**Test platform.** AFM measurement of height field $h(x, y)$ of spin-coated polystyrene on silicon, annealed into the spinodal pre-rupture regime, tapping-mode AFM at $\Delta x \leq L_{\mathrm{coh}}/8$ resolution.

**Sharpest falsifier (F7).** Median $\mathcal{R}_{\mathrm{motif}}$ outside $[-1.80, -0.90]$ refutes the ED-SC 2.0 architectural invariance claim. PASS criterion: median in $[-1.50, -1.10]$ within $\epsilon_{\mathrm{med}} = 0.20$ of reference $r^*$.

**Protocol status.** Protocol complete and session-ready. **Budget:** ~$500 AFM facility + 2 weeks analysis; 4–6 weeks calendar time to publishable result. **Quoted at $15K** for full slide-prep-to-data-collection turnkey (commercial). Three execution routes available: (1) reanalysis of existing 2023 *Nat Comm Phys* AFM data (5-min check), (2) collaboration with Jacobs group at Saarland, (3) book a 1–2 day session at any academic core facility with PS-on-Si dewetting samples.

**Why this test matters.** ED-SC 2.0 is the cross-scale architectural invariance claim — independent of any specific PDE channel. AFM dewetting tests *motif-level* mobility-curvature geometry, not a single channel. PASS validates ED-SC 2.0 at substrate-architectural level; FAIL refutes the architectural invariance claim.

---

## §9 Acoustic / BEC analogue-gravity extremal-horizon tests

**Prediction.** ED acoustic metric + Canon P4 mobility-collapse → interior-maximum horizons are **extremal** ($\kappa = 0$, no Hawking-analogue phonon pair emission). Three sibling experiments test this in different analogue-gravity platforms:

### §9.1 ED-Acoustic-EIT-Extremal (top priority)

**Observable.** Thermal-emission-rate ratio $R_E/R_M$ between extremal (E) and monotonic (M) control-field configurations in the same EIT atomic cell. **Prediction:** $R_E/R_M < 0.1$ (PASS); $> 0.5$ (FAIL).

**Platform.** Spatially-shaped EIT control field on warm Rb vapour or cold Rb ensemble, toggled by SLM between monotonic and extremal $v_g(x)$ profiles. **Methodological strength:** within-apparatus differential — same cell, same detection chain, eliminates systematic drift.

**Status.** Protocol drafted 2026-04-22. **Primary collaboration targets:** Lukin (Harvard); Hau (Harvard); Halfmann (Darmstadt); Lvovsky (Oxford); Giacobino/Bramati (LKB Paris).

### §9.2 ED-Acoustic-BEC-Extremal (highest-profile follow-up)

**Observable.** Density-density correlation function $G(x, x')$ peak amplitude at Hawking-pair null-ray locus; phonon momentum-distribution thermal tail. **Prediction:** correlation peaks and thermal tail suppressed in extremal configuration relative to monotonic (Steinhauer-standard) configuration.

**Platform.** Elongated 1D Rb-87 BEC with custom trap + flow engineering producing smooth second-order zero of $v^2(x) - c_s^2(x)$ at interior point.

**Status.** Stub protocol; blocked on moving-background ED acoustic-metric theory extension + trap-flow co-design + within-apparatus differential protocol. **Primary collaboration targets:** Steinhauer (Technion); Westbrook (Institut d'Optique); Cornell/Jin (JILA); Ferrari (Trento).

### §9.3 ED-Acoustic-OpticalPulse

**Observable.** Pulse-peak (extremal $\kappa = 0$) vs pulse-flank (monotonic $\kappa > 0$) differential pair-emission within a single optical pulse propagation apparatus.

**Status.** Stub protocol; second priority in the acoustic-analogue program.

**Sharpest cross-platform falsifier (F8).** Consistent thermal-emission detection in extremal-configuration analogue horizons across multiple platforms (EIT + BEC + optical-pulse) refutes the ED P4 mobility-collapse → extremal-horizon mechanism.

**Honesty statement.** $\kappa = 0$ at smooth maximum is a *kinematic* property of any acoustic metric, not ED-specific in isolation. These tests discriminate *between configurations within one acoustic-metric framework*, which ED adopts. PASS supports ED's P4-is-extremal reading consistent with the kinematic prediction; FAIL ruptures either the acoustic-metric identification or ED's extremal-horizon mapping.

---

## §10 ED-09.5 Participation-Envelope prediction

**Prediction.** ED-09.5 is the corpus's **single most distinctive falsifiable prediction**: the canonical ED PDE's damping-discriminant bifurcation at $D_{\mathrm{crit}} = 0.5$ (Canon P6) predicts that systems in the oscillatory regime ($D < 0.1$) carry a **slow envelope modulation** of their dynamics at frequency:

$$
\omega_v = 2\pi N_{\mathrm{osc}} \gamma_{\mathrm{dec}} \approx 8 \gamma_{\mathrm{dec}} \quad \text{(single-mode, } N_{\mathrm{osc}} = 8\text{)}.
$$

Quantum-side signatures include $Q_v \in [4, 9]$, third-harmonic content 3–6%, triad coupling $C \in [0.01, 0.05]$.

### §10.1 Two parallel test tracks (same prediction, regimes separated by 10+ OOM in $\gamma_{\mathrm{dec}}$)

**Track A — Cavity-coupled optomechanics reanalysis.** Target datasets: Delic 2020 (levitated SiO₂) and Magrini 2021 (real-time feedback) at $D \sim 10^{-9}$, predicted $\omega_v/2\pi \approx 16$ mHz, envelope period ~63 s, required record length $\geq 200$ s. **Observable:** slow envelope on raw heterodyne $x(t)$ after demodulation at $\omega_m$. **Status:** blocked on raw data access; Aspelmeyer email v3 drafted, not yet sent.

**Track B — FRAP-side Lomb-Scargle on public recovery curves.** Target datasets: concentrated-FRAP datasets with sampling rate $\geq 1$ kHz (Mueller et al. 2008, Kang et al. 2012, Wachsmuth et al. 2003). Predicted $\omega_v/2\pi \in [80, 800]$ Hz. **Observable:** Lomb-Scargle periodogram of residual $r(t) = I(t) - I_{\mathrm{model}}(t)$. **Status:** self-contained, executable within ~1 week at $0$ — **fastest path to a new ED empirical result in the entire program**.

**Sharpest falsifier (F9).** Full PASS on both tracks (mHz envelope in optomechanics + 100-Hz-scale envelope in FRAP residuals) would be the strongest possible confirmation of ED-09.5. Independent FAIL on Track B (no envelope detected at predicted frequency band in any of 3+ uncorrelated FRAP datasets) refutes the ED-09.5 bifurcation mechanism at the cell-biology regime.

**Why this is the most distinctive prediction.** ED-09.5 is regime-agnostic — depends only on the system's decoherence rate $\gamma_{\mathrm{dec}}$. The two tracks test the same bifurcation in regimes separated by **10+ orders of magnitude** in $\gamma_{\mathrm{dec}}$. Substantively distinct from any phenomenological-fit prediction.

---

## §11 Postdiction — Universal Degenerate-Mobility (UDM) Law (self-authored Zenodo preprint, May 2026; not peer-reviewed)

**Postdiction.** Universal $D(c) = D_0 (1 - c/c_{\max})^\beta$ functional form derived from the ED PDE substrate framework. Fit against **10 materials** spanning soft-matter / biological systems. **Result: $R^2 = 0.986$–$0.999$.** Documented in a self-authored preprint ("Universal Degenerate-Mobility Scaling in Crowded Soft Matter") self-published on Zenodo, May 2026 — **not peer-reviewed** (Zenodo is a repository, not a journal).

**Significance.** This is ED's strongest *data-match* to date: a functional form derived from the ED mobility-channel (Canon P4) **blind to the data** (its strength) that fits 10 chemically distinct materials. But the data all predate the derivation (1994–2016), so it is a **postdiction**, not a forward-confirmed prediction, and it is the author's own analysis — not reviewed or independently reproduced.

**Status.** POSTDICTION (derived form, blind to data; not peer-reviewed, not independent validation). The genuine **forward** test is the follow-on FRAP-BSA front-radius exponent $\alpha_R = 1/6$ (§7 above) via a different observable — not yet run.

**Sharpest falsifier (F10, hypothetical).** A material in the UDM-application class with $R^2 < 0.8$ against the universal $D(c) = D_0(1 - c/c_{\max})^\beta$ functional form would refute the substrate-level universality claim. Currently consistent across all 10 examined materials.

---

## §12 Passed test — GW170817 speed equality with $c$

**Test passed.** GW170817 (binary-neutron-star merger, August 2017): multi-messenger constraint $|c_{\mathrm{GW}} - c|/c < 10^{-15}$. ED's prediction (Paper_ED_GW_00 §3.8): GW propagation speed = substrate-c, the same $c$ that bounds electromagnetic propagation per Paper_012 (P-RB-1). ED structurally inherits GW speed = $c$; falsification would have required $|c_{\mathrm{GW}} - c|/c \gtrsim 10^{-15}$.

**Significance.** GW170817 ruled out a large class of modified-gravity theories that predict $c_{\mathrm{GW}} \neq c$ (Tensor-Vector-Scalar theories, certain massive-graviton models, certain dark-energy theories). ED's substrate-graph reading — GW = propagating saddle-Hessian reconfiguration carried by V1 retarded kernel at substrate-c (Paper_ED_GW_00 §3.3) — is structurally consistent with the observation. **ED was not falsified by GW170817; many alternative-gravity programs were.**

**Sharpest falsifier (F11, hypothetical).** Future GW + electromagnetic multi-messenger event with $|c_{\mathrm{GW}} - c|/c \gtrsim 10^{-15}$ would refute Paper_ED_GW_00's substrate-c identification of GW propagation.

---

## §13 Postdiction — Λ-smallness 120-OOM reframing (Paper_038_5; M3 retroactive)

**Postdiction.** The famous cosmological-constant problem ($\rho_\Lambda / \rho_P \sim 10^{-120}$) is **reframed**, not paradoxical, at substrate-graph level.

**Substrate-graph reframing (Paper_038_5 + Paper_ED_Cos_05).**

1. ED's **discrete substrate ontology does not admit infinite QFT mode-tower zero-point summation**. The naïve QFT estimate $\rho_{\mathrm{vac}}^{\mathrm{naive}} \sim M_P^4$ is *structurally absent* substrate-side — there is no infinite mode tower to sum.
2. Substrate-graph closure of $\rho_\Lambda$ reduces to Friedmann inheritance: $\rho_\Lambda = (3/8\pi) H_0^2 M_P^2$ with $M_P^2$ via Paper_027's dimensional rearrangement and $H_0$ via Route A4 substrate-graph chain (Paper_ED_Cos_05).
3. Route A4 closure (2026-05-17, see Update_Paper_ED_Cos_05_M3_Unconditional + Update_Paper_038_5_M3): $H_0 = (8\pi/3)^{1/2} \ell_P c^{1/2} \Theta_{\mathrm{ED}}^{1/2}$ with $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$ substrate-parameter-INHERITED at primitive level (analog of Paper_027's $\ell_P, \hbar, c$ inheritance).

**Result.** The 120-OOM "mismatch" becomes a **substrate-parameter-content value** $\Theta_{\mathrm{ED}}^{\mathrm{Planck-units}} \approx 10^{-122}$, parallel to the longstanding question "what determines $\ell_P, \hbar, c$ values?" at primitive substrate-constant level. The famous-problem framing is dissolved; the substrate-parameter-content question remains as tightening work (RA-OPEN-4a; not load-bearing for M3).

**Sharpest falsifier (F12).** Independent observational evidence that $\rho_\Lambda \neq (3/8\pi) H_0^2 M_P^2$ at substrate-parameter-INHERITED level would refute either Route A's substrate-graph chain or the Friedmann inheritance step. Currently consistent with Planck CMB + Type Ia supernovae + BAO at observed $H_0$.

---

## §14 Cross-scale falsifiers — SCBU synchronized-covariation prediction

**Prediction.** The Substrate-Cosmology Boundary Unification (SCBU; Paper_SCBU + ED-SC 4.x arc) framework predicts **synchronized co-variation of six projections** of the substrate-cosmology boundary at $R_H = c/H_0$ under Hubble-tension-class shifts of $H_0$:

- $\xi_{\mathrm{canonical}}$ (substrate-scale anchor; Paper_ED_SC_4.2 / Paper_096)
- $a_0 = cH_0/(2\pi)$ (MOND transition acceleration; Paper_029)
- $R_H = c/H_0$ (cosmic decoupling surface; Paper_028)
- $\mathcal{M}_{\mathrm{crit}}$ (Q-Compute platform-coherence wall; Paper_060)
- $Q \approx 3.5$ (NS-Q canonical hydrodynamic; Paper_080)
- BH horizon $r_H$ (parameterized by local mass; Paper_ED_SC_4.1)

**Post-Route-A-closure status (2026-05-17).** With Route A now closed at substrate-parameter-INHERITED level (Update_ED_SC_4x_Arc_M3), per-projection scaling exponents are derivable in principle via the Route A inheritance chain:

- $a_0 \propto H_0^1$ — structural per Paper_029
- $R_H \propto H_0^{-1}$ — structural per Paper_028
- $\xi_{\mathrm{canonical}} \propto H_0$ at leading order via Route A4
- $\mathcal{M}_{\mathrm{crit}}, Q$ — per-projection derivation tightening work (substrate-research-frontier; not load-bearing for M3)

**Sharpest falsifier (F13).** Empirical **asynchrony** between any two SCBU-projection observables under Hubble-tension-class $H_0$ shifts — e.g., $a_0$ tracking $H_0$ as predicted while $\mathcal{M}_{\mathrm{crit}}$ remains flat — refutes the SCBU-projection identification for the asynchronous quantity regardless of per-projection exponent derivation status.

**Why this is structurally distinctive.** SCBU is the corpus's "single substrate, six projections" claim. Hubble tension is currently a live observational debate (early-universe vs late-universe $H_0$ measurements disagree at $\sim 5\sigma$). Independent shifts in $a_0$, $\mathcal{M}_{\mathrm{crit}}$, $Q$ — observable in galactic-rotation, matter-wave-interferometry, and soft-matter platforms respectively — would test the SCBU synchronization at empirical level.

---

## §15 Testability summary table

| # | Prediction | Source paper | Test platform | Status | Sharpest falsifier |
|---|---|---|---|---|---|
| 1 | BTFR slope-4 + zero scatter | Paper_031 | SPARC catalog (public) | **Testable now** | Slope $\neq 4$ or intrinsic scatter at deep-MOND-asymptote |
| 2 | $a_0 = cH_0/(2\pi)$ | Paper_029 | Hubble-tension-class $H_0$ refinement | **Testable as $H_0$ precision improves** | $a_0$ shift inconsistent with $cH_0/(2\pi)$ |
| 3 | Weak-lensing activity-dependence | Paper_038_6 | KiDS / DES / HSC / LSST / Euclid | **Testable now** (PROVISIONAL Pred_) | Activity-independent lensing at deep-MOND radii |
| 4 | GW merger-lag existence | Paper_052_5 | LIGO/Virgo/KAGRA + ET / CE / LISA | **Testable now** (PROVISIONAL Pred_) | Merger-lag $< \tau_{V_5}^{\min}$ (floor OPEN) |
| 5 | QC mass wall 140–250 kDa | QC-Mass protocol | LUMI / OTIMA / MAQRO | **Pre-registered**; needs LUMI extension | $V_{\mathrm{coh}}$ crossing $m_c < 100$k or $> 400$k amu |
| 6 | UDM front-radius $\alpha_R = 1/6$ | FRAP-BSA protocol | Confocal FRAP (CP submitted) | **Protocol active**; 6–8 wk timeline | $\alpha_R \geq 0.35$ or Fickian wins at all conc. |
| 7 | $\mathrm{med}(\mathcal{R}_{\mathrm{motif}}) = -1.30$ | AFM protocol | Tapping-mode AFM on PS/Si | **Session-ready**; $15K quoted | Median outside $[-1.80, -0.90]$ |
| 8 | Extremal-horizon zero pair emission | EIT/BEC/Optical protocols | EIT Rb cell + 1D Rb-87 BEC | **EIT protocol drafted**; collab pending | Pair-emission in extremal configuration |
| 9 | ED-09.5 envelope $\omega_v \approx 8\gamma_{\mathrm{dec}}$ | ED-09.5 protocol | Optomechanics + FRAP residuals | **Track B: $0, 1-week executable** | No envelope at predicted band |
| 10 | UDM $D(c) = D_0(1-c/c_{\max})^\beta$ | UDM Zenodo preprint (self-authored, not peer-reviewed) | 10-material soft-matter dataset (1994–2016) | **POSTDICTION** ($R^2 = 0.986$–$0.999$) | (Hypothetical: material in class with $R^2 < 0.8$) |
| 11 | GW speed $= c$ | Paper_ED_GW_00 | GW170817 multi-messenger | **PASSED** ($|c_{\mathrm{GW}} - c|/c < 10^{-15}$) | Future multi-messenger $|c_{\mathrm{GW}} - c|/c \gtrsim 10^{-15}$ |
| 12 | Λ smallness $= \Theta_{\mathrm{ED}}^{\mathrm{Planck-units}}$ | Paper_038_5 (M3 retro.) | Planck + SNe Ia + BAO | **CONSISTENT** with $\rho_\Lambda = (3/8\pi) H_0^2 M_P^2$ | $\rho_\Lambda$ inconsistent with Friedmann form |
| 13 | SCBU synchronized covariation | ED-SC 4.x arc | Multi-axis observational stratification | **Testable as $H_0$ measurements refine** | Asynchrony between any two projections |

**Three predictions are testable now at low cost** (#1 SPARC reanalysis; #9 FRAP-residual Lomb-Scargle reanalysis; #10/#11/#12 already-passed). **Two are protocol-ready** with budgets quoted (#6 FRAP-BSA at ~$1500; #7 AFM at ~$500–15K). **Five await collaboration with experimental groups** (#5 LUMI/Arndt; #8 EIT/BEC analogue-gravity; #9 Track A Aspelmeyer optomechanics). **Three are observational-pipeline analyses** (#3 weak-lensing survey reanalysis; #4 GW residual analysis; #13 cross-axis Hubble-tension stratification).

---

## §16 What this paper does and does NOT claim

This paper does **not** claim:
- That ED replaces the Standard Model, ΛCDM, or general relativity. ED supplements standard physics with a substrate-level account; standard-physics predictions remain excellent within their regimes.
- That every prediction listed is refutation-grade (in the BTFR-slope-4 sense). Where prediction status is PROVISIONAL Pred_ (e.g., Paper_038_6 weak-lensing; Paper_052_5 merger-lag), this is named explicitly per Paper_095's verdict grammar.
- That substrate primitives are derived from a deeper layer. The 13 primitives (Paper_087) are posited; the empirical case rests on cross-domain reach.
- Sole-theory status. Many predictions listed (BTFR slope-4; $a_0$; $\rho_\Lambda$) are consistent with MOND-as-phenomenology or other approaches at observational level; ED's claim is that it *derives* these from a small set of substrate primitives whereas other approaches fit or postulate them.

This paper does claim:
- ED's substrate-level identification produces a family of cross-domain predictions traceable to the substrate-graph identification $a_0 = cH_0/(2\pi)$ (the wedge) and the substrate-cosmology boundary $R_H = c/H_0$ (the organizing claim).
- The form-FORCED structural content of each listed prediction is derived from substrate primitives per Paper_095 discipline.
- Each prediction is paired with a sharpest falsifier that is operationally explicit and observationally accessible.
- The corpus's substrate-research-pattern progression (Load-Bearing Program → Q1Q2 + Chain-Class Identification → Route A audit cascade) has delivered the Cosmology Arc M3 Trinity (Cos_01 + Cos_05 + Paper_038_5 all at M3) + ED-SC 4.x arc-wide M3 upgrade as of 2026-05-17.

---

## §17 References

**Source corpus papers:**

- Paper_027 — Newton's $G$ from substrate constants
- Paper_028 — Cosmic decoupling surface $R_H = c/H_0$
- Paper_029 — Transition acceleration $a_0 = cH_0/(2\pi)$
- Paper_030 — ED Combination Rule $a = \sqrt{a_N a_0}$
- Paper_031 — BTFR slope-4 with zero intrinsic scatter
- Paper_034 — Deep-MOND asymptotic regime
- Paper_036 — MOND field equation
- Paper_038_5 — Lambda V1 Cosmological (Λ-smallness reframing; M3 retroactive)
- Paper_038_6 — Pred_WeakLensing_Activity
- Paper_047 — Hawking spectrum $T_H = \kappa/(2\pi)$ via V5 KMS
- Paper_052_5 — Pred_MergerLag
- Paper_060 — $\mathcal{M}_{\mathrm{crit}}$ unification
- Paper_073 — DCGT (Diffusion Coarse-Graining Theorem)
- Paper_080 — NS-Q canonical $Q \approx 3.5$
- Paper_087 — 13 primitives (position paper)
- Paper_089 — V1 retarded kernel + T18
- Paper_090 — V5 cross-chain kernel
- Paper_095 — Form-FORCED / value-INHERITED methodology
- Paper_096 — Cross-scale invariance + $\xi_{\mathrm{canonical}}$
- Paper_SCBU — Substrate-Cosmology Boundary Unification
- Paper_ED_SC_4_1 through 4_6 — ED-SC 4.x cross-scale extension arc
- Paper_ED_Cos_01 — Inflation (M3 unconditional, 2026-05-17)
- Paper_ED_Cos_05 — Dark Energy (M3 unconditional, 2026-05-17)
- Paper_ED_GW_00 — Gravitational Waves (M3 + row 12 partial closure)
- Universal Mobility Law paper (self-authored Zenodo preprint, May 2026; not peer-reviewed)

**Update memos (2026-05-17):**

- Update_Paper_ED_Cos_05_M3_Unconditional
- Update_Paper_038_5_M3
- Update_ED_SC_4x_Arc_M3
- Update_SCBU_Synthesis_PostRouteA
- Update_ED_MEMORY_CosmologyArc_M3

**Protocol references (`predictions/` folder):**

- QC-Mass-Extrapolation_InProcess
- FRAP-High-BSA_InProcess
- AFM-Dewetting-ED-SC_InProcess
- ED-Acoustic-BEC-Extremal_InProcess
- ED-Acoustic-EIT-Extremal_InProcess
- ED-Acoustic-OpticalPulse_InProcess
- ED-09.5 Participation-Envelope_InProcess
- Triad-Coupling-C7_InProcess
- ED-RLC-Analogue_InProcess

**External empirical anchors:**

- Lelli, McGaugh, Schombert 2016 — SPARC galaxy-rotation-curve catalog
- McGaugh 2012 — BTFR slope-4 empirical measurement
- Milgrom 1983 — MOND original phenomenological framework
- LIGO/Virgo Collaboration 2017 — GW170817 multi-messenger detection
- Planck Collaboration — CMB + $\Lambda$CDM cosmological parameters
- Eibenberger et al. 2013 — Matter-wave interferometry ~10 kDa
- Fein et al. 2019 — Matter-wave interferometry ~25 kDa
- Delic et al. 2020 — Levitated optomechanics SiO₂
- Magrini et al. 2021 — Real-time feedback optomechanics

---

**End Paper_ED_Predictions_Bundle.**
