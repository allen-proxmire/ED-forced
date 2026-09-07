# Event Density Mobility Scaling in Concentrated BSA: FRAP Test of the Universal Degenerate-Mobility Law

**Series:** Wave-3 Empirical-Prediction Sector — FRAP Results (TEMPLATE; placeholders pending experimental execution)
**Status:** Template paper structured for completion after FRAP-BSA experimental execution (protocol active per `predictions/FRAP-High-BSA_InProcess/`; submitted to Creative Proteomics CIBR 2026-04-17). Data, results, and discussion sections contain placeholders marked `[TO BE FILLED AFTER EXPERIMENT]`. **This is not yet a results paper; it is the structure into which results will be filled when the experimental run completes.**
**Date:** 2026-05-17 (template draft); experimental data acquisition pending
**Authors:** Allen Proxmire (corresponding); [TO BE FILLED: experimental collaborator(s) if applicable]
**Anchors:** Universal Mobility Law paper (self-authored Zenodo preprint, May 2026; not peer-reviewed; 10-material UDM fit $R^2 = 0.986$–$0.999$); FRAP-High-BSA_InProcess protocol; Paper_087 (13 primitives — Canon P4 Mobility Capacity Bound); Paper_095 (form-FORCED / value-INHERITED methodology); Paper_ED_Predictions_Bundle (companion bundle paper); Paper_ED_Postdictions_PassedTests (UDM as postdiction, §2).

---

## §1 Introduction

The Universal Degenerate-Mobility (UDM) law derived from the Event Density (ED) substrate framework predicts a universal concentration-dependent diffusion functional form:

$$
D(c) = D_0 \left(1 - \frac{c}{c_{\max}}\right)^\beta
$$

with canonical $\beta \approx 2$. The functional form is **derived from substrate primitives** (ED Canon principle P4 — Mobility Capacity Bound) prior to any data fitting. The Universal Mobility Law paper (self-authored Zenodo preprint, May 2026; not peer-reviewed) fit this functional form to existing published data across **10 materials** spanning soft-matter / biological systems with $R^2 = 0.986$–$0.999$ at all materials — a strong **postdiction** (the data predate the derivation), not an independently-validated passed test.

This paper reports the FRAP-BSA experimental test of UDM via an independent observable: **front-radius propagation exponent** in fluorescence recovery after photobleaching. The 2D porous-medium equation (PME) with $m = \beta + 1 = 3$ derived from UDM with $\beta = 2$ gives front-radius exponent:

$$
\alpha_R = \frac{1}{d(m-1) + 2} = \frac{1}{6} \approx 0.167.
$$

ED predicts $R(t) \sim t^{1/6}$ with a **sharp** bleach boundary (compact support, PME signature). The null prediction (standard Fickian diffusion) is $R(t) \sim t^{1/2}$ with a Gaussian-blurred boundary.

The FRAP-BSA test is a genuine **forward test** of UDM via a *different observable* (front propagation rather than diffusion-coefficient regression) — and, unlike the postdictive 10-material fit, the data would be collected *after* the prediction. A PASS here complements the existing UDM data-match (self-published Zenodo preprint, not peer-reviewed) without replacing it; a FAIL would create tension with the 10-material match and require resolution.

---

## §2 Theory

### §2.1 The UDM mobility channel (ED Canon P4)

The ED PDE framework posits the substrate-level mobility-capacity bound (Canon P4): substrate-level mobility $M(\rho)$ vanishes as the substrate event-density $\rho$ approaches its maximum $\rho_{\max}$:

$$
M(\rho) = M_0 \left(\rho_{\max} - \rho\right)^\beta.
$$

Canonical $\beta = 2$. This is structural per ED Canon P4; the functional form is form-FORCED from substrate primitives prior to any empirical data.

### §2.2 Connection to concentration-dependent diffusion

The diffusion coefficient $D(c) = M(c) \cdot \chi^{-1}(c)$, where $\chi(c) = dc/d\mu$ is the susceptibility. For concentration-dependent diffusion in the UDM regime, $D(c) = D_0(1 - c/c_{\max})^\beta$ — the form fit to existing data across 10 materials in the Universal Mobility Law paper (self-authored Zenodo preprint, not peer-reviewed).

### §2.3 Connection to the 2D porous-medium equation

For 2D radial spreading (FRAP geometry), the UDM mobility channel produces the 2D porous-medium equation (PME):

$$
\frac{\partial c}{\partial t} = \nabla \cdot \left[D_0 (1 - c/c_{\max})^\beta \nabla c\right] = \nabla \cdot \left[D_{\mathrm{eff}}(c) \nabla c\right]
$$

with effective diffusion $D_{\mathrm{eff}}(c) \propto (1 - c/c_{\max})^\beta$. This PME admits Barenblatt-type self-similar solutions with **compact support** (sharp front boundary) and front-radius scaling:

$$
R(t) \sim t^{\alpha_R}, \quad \alpha_R = \frac{1}{d(m-1) + 2}
$$

with $m = \beta + 1$ and $d = 2$ (2D FRAP geometry). For $\beta = 2$: $m = 3$, $\alpha_R = 1/6 \approx 0.167$.

### §2.4 ED prediction (form-FORCED) vs Fickian null (form-FORCED)

**ED-UDM prediction.**
- $R(t) \sim t^{1/6} \approx t^{0.167}$
- Sharp bleach boundary (PME compact support; characteristic of porous-medium-class diffusion)
- $R(t)$ slope on log-log plot: $0.167 \pm 0.04$ (allowing for finite-sample fit uncertainty)

**Fickian null prediction.**
- $R(t) \sim t^{1/2} \approx t^{0.500}$
- Gaussian-blurred boundary (Fickian / heat-equation signature)
- $R(t)$ slope on log-log plot: $0.500 \pm$ (fit uncertainty)

**Discrimination.** The two predictions differ in $\alpha_R$ by a factor of 3 — well outside any reasonable observational uncertainty in a properly-designed FRAP experiment. PME vs Fickian fit can be discriminated by AIC (Akaike Information Criterion) at standard observational precision.

---

## §3 Experimental protocol

### §3.1 Sample preparation

[Reproduced from FRAP-High-BSA_InProcess protocol.md §4-§5, the operational protocol submitted to Creative Proteomics CIBR on 2026-04-17.]

**Bovine Serum Albumin–Fluorescein Isothiocyanate (BSA-FITC):** Sigma-Aldrich A9771 or equivalent. Reconstituted in pH 7.4 PBS at four concentrations:

- **200 mg/mL** ($\phi = 0.15$)
- **250 mg/mL** ($\phi = 0.18$)
- **300 mg/mL** ($\phi = 0.22$)
- **350 mg/mL** ($\phi = 0.25$)

Sample volumes 100 µL per concentration. Loaded into glass-bottom 96-well plate (No. 1.5 coverslip, 0.17 mm thickness).

### §3.2 Photobleaching parameters

- **Bleach laser:** 488 nm, full power (~10 mW at sample), 100 ms exposure
- **Bleach geometry:** circular ROI, $r_0 = 10$ µm radius
- **Bleach intensity reduction:** target 50–70% of pre-bleach fluorescence (avoid full bleach to preserve front detectability)

### §3.3 Imaging parameters

- **Microscope:** confocal (Zeiss LSM 880 or equivalent), 40× oil objective NA 1.3
- **Pixel size:** 0.2 µm/pixel
- **Frame rate:** 1 frame/second for first 60 s post-bleach (front-propagation regime); 1 frame/5 s for 60–600 s (slow-recovery regime)
- **Detection:** GaAsP detector, 500–550 nm bandpass

### §3.4 Replication

- **5 bleaches per concentration × 4 concentrations = 20 total acquisitions**
- Bleach ROIs separated by $\geq 50$ µm to avoid cross-talk
- Single session per concentration where possible to minimize between-session drift

### §3.5 Data export

- Full TIFF stacks per acquisition (16-bit, no compression)
- Metadata: acquisition timestamp, pixel size, frame rate, laser power, ROI coordinates

---

## §4 Expected results

### §4.1 ED-UDM prediction (PASS scenario)

If UDM holds for concentrated BSA:

| Concentration | Expected $\alpha_R$ | Expected front character |
|---|---|---|
| 200 mg/mL | $0.167 \pm 0.04$ | Sharp |
| 250 mg/mL | $0.167 \pm 0.04$ | Sharp |
| 300 mg/mL | $0.167 \pm 0.04$ | Sharp |
| 350 mg/mL | $0.167 \pm 0.04$ | Sharp |

**PASS criterion.** $\alpha_R \in [0.125, 0.170]$ at $\geq 3/4$ concentrations + PME-front fit beats Fickian-front fit via AIC ($\Delta\mathrm{AIC} > 4$ in favor of PME).

### §4.2 Fickian null prediction (FAIL-of-ED scenario)

If standard Fickian diffusion holds:

| Concentration | Expected $\alpha_R$ | Expected front character |
|---|---|---|
| 200 mg/mL | $0.500 \pm 0.05$ | Gaussian-blurred |
| 250 mg/mL | $0.500 \pm 0.05$ | Gaussian-blurred |
| 300 mg/mL | $0.500 \pm 0.05$ | Gaussian-blurred |
| 350 mg/mL | $0.500 \pm 0.05$ | Gaussian-blurred |

**FAIL-of-ED criterion.** $\alpha_R \geq 0.35$ or Fickian-front fit wins via AIC at all 4 concentrations.

### §4.3 Mixed / intermediate outcomes

Five-outcome decision tree (per protocol §10):

- **PASS** — ED-UDM confirmed (criterion §4.1)
- **NEAR-PASS** — $\alpha_R$ within $[0.125, 0.170]$ at $\geq 2/4$ concentrations but not $\geq 3/4$; or PME fit beats Fickian by $\Delta\mathrm{AIC} \in (2, 4]$ rather than $> 4$
- **FAIL** — Fickian wins per §4.2
- **UNDECIDABLE** — $\alpha_R \in [0.17, 0.35]$ across concentrations; AIC $|\Delta\mathrm{AIC}| < 2$
- **SPLIT** — different concentrations give different outcomes (e.g., PASS at high concentration, Fickian at low concentration) — would suggest UDM is an asymptotic-high-concentration regime, requiring substrate-research-frontier follow-on

---

## §5 Data analysis pipeline

### §5.1 Front-radius extraction

[Implementation: `analysis/scripts/udm_frap/frap_udm_pipeline.py` per protocol §9.4] *(working-repo artifact: lives under `event-density`/`ed-lab`, not in this repo)* *(working-repo artifact — no longer in this repo; lives under `event-density`/`ed-lab`)*

1. **Frame registration.** Cross-correlation alignment against pre-bleach frame to correct stage drift.
2. **Background subtraction.** Per-frame uniform background from off-bleach ROI.
3. **Front detection.** For each post-bleach frame:
   - Radial profile $I(r, t)$ from ROI center
   - Front position $R(t)$ = radius at which $I(r, t) = 0.5 \cdot (I_{\mathrm{pre-bleach}} - I_{\mathrm{bleach center}}) + I_{\mathrm{bleach center}}$ (50%-recovery isoline)
4. **Front-character quantification.** Sharp-boundary metric: $|dI/dr|_{\max}$ at front; Gaussian-fit residual character.

### §5.2 $\alpha_R$ regression

5. **Log-log fit.** Linear regression of $\log R(t)$ vs $\log t$ over the front-propagation regime ($t \in [1, 30]$ s post-bleach). Extract $\alpha_R$ + standard error.
6. **Per-concentration $\alpha_R$ aggregation.** 5 bleaches per concentration → 5 $\alpha_R$ values per concentration → mean $\bar\alpha_R$ + standard deviation.

### §5.3 PME vs Fickian model fit

7. **PME fit.** Numerical solution of 2D PME $\partial c/\partial t = \nabla \cdot [D_0(1-c/c_{\max})^\beta \nabla c]$ with $\beta = 2$. Two free parameters per acquisition: $D_0$ and $c_{\max}$. Least-squares fit to $I(r, t)$ data.
8. **Fickian fit.** Numerical solution of 2D heat equation $\partial c/\partial t = D \nabla^2 c$. One free parameter per acquisition: $D$. Least-squares fit to $I(r, t)$ data.
9. **AIC comparison.** $\mathrm{AIC}_{\mathrm{PME}} = 2 \cdot 2 - 2 \ln L_{\mathrm{PME}}$ vs $\mathrm{AIC}_{\mathrm{Fickian}} = 2 \cdot 1 - 2 \ln L_{\mathrm{Fickian}}$. $\Delta\mathrm{AIC} = \mathrm{AIC}_{\mathrm{Fickian}} - \mathrm{AIC}_{\mathrm{PME}}$ favors PME if positive.

### §5.4 Per-concentration and ensemble decision

10. **Per-concentration outcome.** Apply 5-outcome decision tree (§4.3) using $\bar\alpha_R$ + $\Delta\mathrm{AIC}$ at each concentration.
11. **Ensemble decision.** PASS if 3/4 concentrations PASS individually; otherwise per the 5-outcome tree.

---

## §6 Results

[TO BE FILLED AFTER EXPERIMENT]

### §6.1 Acquisition summary

[TO BE FILLED: Date of experimental session(s); total acquisitions completed; any acquisitions excluded due to technical failure and reason]

### §6.2 Per-concentration $\alpha_R$ measurements

[TO BE FILLED: Table of $\bar\alpha_R$ + standard deviation per concentration]

| Concentration (mg/mL) | $\phi$ | $\bar\alpha_R$ (measured) | Standard deviation | $n$ acquisitions |
|---|---|---|---|---|
| 200 | 0.15 | [TBD] | [TBD] | [TBD] |
| 250 | 0.18 | [TBD] | [TBD] | [TBD] |
| 300 | 0.22 | [TBD] | [TBD] | [TBD] |
| 350 | 0.25 | [TBD] | [TBD] | [TBD] |

### §6.3 PME vs Fickian model comparison

[TO BE FILLED: Per-concentration $\Delta\mathrm{AIC}$ values; ensemble $\Delta\mathrm{AIC}$]

| Concentration (mg/mL) | $\Delta\mathrm{AIC}$ (Fickian − PME) | Preferred model |
|---|---|---|
| 200 | [TBD] | [TBD] |
| 250 | [TBD] | [TBD] |
| 300 | [TBD] | [TBD] |
| 350 | [TBD] | [TBD] |

### §6.4 Front character

[TO BE FILLED: Sharp-vs-blurred boundary classification per concentration; quantitative front-character metrics]

### §6.5 Ensemble outcome

[TO BE FILLED: 5-outcome classification (PASS / NEAR-PASS / FAIL / UNDECIDABLE / SPLIT)]

---

## §7 Discussion

[TO BE FILLED AFTER EXPERIMENT]

### §7.1 Comparison with ED-UDM prediction

[TO BE FILLED: Match or mismatch with predicted $\alpha_R = 1/6$; discussion of any per-concentration anomalies]

### §7.2 Comparison with the Universal Mobility Law data-match (Zenodo preprint)

[TO BE FILLED: Consistency or tension with the 10-material UDM fit ($R^2 > 0.986$, May 2026 publication); implications for the universality claim]

### §7.3 Implications for ED's substrate-level framework

[TO BE FILLED: If PASS, second-confirmation status + advancement of Canon P4 substrate-level framework; if FAIL, scope of refutation and which substrate-level claim(s) are challenged]

### §7.4 Comparison with alternative models

[TO BE FILLED: Comparison with alternative concentration-dependent-diffusion models (e.g., hard-sphere obstruction models, mode-coupling theory predictions, simple power-law fits without PME structure)]

### §7.5 Systematic uncertainties

[TO BE FILLED: Identified systematic uncertainties from experimental execution; impact on $\alpha_R$ measurement; estimate of total uncertainty budget]

### §7.6 Future work

[TO BE FILLED: Extensions identified during analysis; follow-on experiments suggested; protocol refinements for V2]

---

## §8 Conclusion

[TO BE FILLED AFTER EXPERIMENT: 2-3 paragraph summary of outcome + significance for ED's substrate-level framework + implications for UDM as the corpus's strongest empirically-validated structural prediction]

---

## §9 Acknowledgments

[TO BE FILLED: Experimental collaborator acknowledgment (Creative Proteomics CIBR if executed via CP route, or alternative facility/group); funding source if applicable; any reviewers]

---

## §10 Methods supplement

The full operational protocol is reproduced from `predictions/FRAP-High-BSA_InProcess/protocol.md` (the exact text submitted to Creative Proteomics CIBR on 2026-04-17). Sections §4-§8 of the protocol = experimental protocol used in this paper §3. Sections §9-§12 of the protocol = analysis pipeline used in this paper §5. Section §13 of the protocol = identified V2 protocol refinements (to be addressed in any follow-on experimental round).

Code repository for analysis pipeline: [TO BE FILLED: Zenodo DOI for analysis code release; or GitHub link for `analysis/scripts/udm_frap/frap_udm_pipeline.py`] *(working-repo artifact: lives under `event-density`/`ed-lab`, not in this repo)* *(working-repo artifact — no longer in this repo; lives under `event-density`/`ed-lab`)*

Raw data deposition: [TO BE FILLED: Zenodo DOI for TIFF-stack data deposition]

---

## §11 References

**ED corpus papers:**

- Paper_087 — 13 primitives (position paper; Canon P4 Mobility Capacity Bound)
- Paper_095 — Form-FORCED / value-INHERITED methodology
- Universal Mobility Law paper (self-authored Zenodo preprint, May 2026; not peer-reviewed) — 10-material UDM fit
- Paper_ED_Predictions_Bundle (companion paper) — full ED predictions inventory
- Paper_ED_Postdictions_PassedTests (companion paper) — UDM as postdiction (§2)

**Protocol reference:**

- `predictions/FRAP-High-BSA_InProcess/protocol.md` — full operational protocol

**External references (FRAP literature; UDM-application class materials):**

- [TO BE FILLED: Standard FRAP-method references — Axelrod et al. 1976; Sprague et al. 2004; Mueller et al. 2008]
- [TO BE FILLED: BSA-FITC concentrated-solution literature; prior diffusion measurements at $\phi > 0.10$]
- [TO BE FILLED: Universal Mobility Law Evidence paper full citation when DOI available]
- [TO BE FILLED: Porous-medium-equation theoretical references — Barenblatt 1996; Vázquez 2007]

**Cross-references:**

- For the UDM functional form derivation from ED substrate primitives: Universal Mobility Law Evidence paper §2-§3
- For the substrate-graph Canon P4 statement: Paper_087 §P04 (Bandwidth) + Canon principle P4 derivation in `theory/Architectural_Canon.md`
- For the corpus-level context of this test within ED's empirical-prediction sector: Paper_ED_Predictions_Bundle §7

---

**End Paper_ED_FRAP_Template.** *(Template paper structured for completion after FRAP-BSA experimental execution. Data, results, and discussion sections contain placeholders marked `[TO BE FILLED AFTER EXPERIMENT]`.)*
