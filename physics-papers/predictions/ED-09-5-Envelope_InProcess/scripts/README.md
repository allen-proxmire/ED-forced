# ED-09.5 Track B — analysis pipeline (built + validated 2026-07-10)

The protocol's **Days 2–3 deliverable** (`../protocol.md` §8.3): a working, validated
Lomb–Scargle pipeline for the FRAP participation-envelope test, ready to run on real
data the moment a suitable dataset is in hand.

## Files
| File | Purpose |
|---|---|
| `frap_envelope_lombscargle.py` | The pipeline. `analyze(t, I, gamma_dec)` → predicted vs measured `f_v`, `Q_v`, `N_osc`, 3rd-harmonic, triad, F0–F5. CLI: `python frap_envelope_lombscargle.py curve.csv --gamma-dec 30`. Default `N_osc=1.1` (= `Q/π`, PDE-corrected; see below). |
| `synthetic_envelope_validation.py` | Instrument validation — injection / null / off-frequency cases (corrected ~33 Hz band). |
| `ed_pde_envelope_drive.py` | **Drives the prediction from the real canonical PDE** (Architectural_Canon P2+P3+P5). Measures `f_v`, `γ_dec`, `Q`, `r=f_v/γ_dec` in the oscillatory regime. **Found `r≈1.1` (=`Q/π`), not 8** → the `8·γ_dec` band is ~7× too high. See [`../ED_PDE_Drive_Finding_2026-07-10.md`](../ED_PDE_Drive_Finding_2026-07-10.md). |

## What it does (per protocol §6–10)
Fit the smooth recovery model (exp1/exp2, lower-AIC) → residual `r(t)=I−I_model` →
Lomb–Scargle (astropy, normalized power + Baluev false-alarm probability) → find the
peak in the [80,800] Hz band → test it against the pre-registered prediction
`f_v = N_osc·γ_dec` (N_osc=8) with:
- **F0** peak significant (FAP<0.01) and within a factor of 2 of `f_v`;
- **F2** `N_osc ∈ [6,12]` (from `Q_v` via the pre-registered `N_osc=(Q/π)ln(1/α)`);
- **F3** `Q_v ∈ [4,9]` (Lorentzian fit of the periodogram peak);
- **F4** 3rd-harmonic ratio ∈ [3%,6%];
- **F5** triad coupling ∈ [0.01,0.05] (crude bicoherence; data-hungry, honest-flagged).

## Validation result (2026-07-10) — the INSTRUMENT is sensitive and specific
`python synthetic_envelope_validation.py` → all three checks PASS: *(a shell command, not a path; the script is a working-repo artifact and is no longer in this repo)*
- **Injection** (a faithful finite-Q resonator mode at 240 Hz, driven by noise, not a rigged tone): recovered `f_v=243.8 Hz` (pred 240), FAP≈6×10⁻²⁷, `Q_v=6.59`, `N_osc=8.43` → **F0/F2/F3 pass**, verdict LINEAR_PASS.
- **Null** (recovery + noise, no mode): not significant (FAP=1.0) → **no false positive**.
- **Off-frequency** (real mode at 600 Hz, prediction 240): peak found but **F0 correctly rejects it** (specificity).

## SCOPE — what this does and does NOT establish
- **Does:** the detector recovers a known envelope at the right frequency, measures `Q_v`, and does not false-positive on recovery+noise or an off-prediction peak. The Track B *instrument* is ready.
- **Does NOT:** test ED. A synthetic PASS means "the detector works", not "ED-09.5 is confirmed."

## To actually test ED-09.5 (the two remaining pieces)
1. **Data (the real-world blocker).** Feed `analyze()` a **concentrated**, **high-framerate (≥1–2 kHz)** FRAP recovery curve with a known/estimable `γ_dec`. Protocol §7 candidates: Mueller 2008, Kang 2012, Wachsmuth 2003 (need machine-readable curves, not figures); or the in-house UDM-FRAP V2 high-framerate add-on (protocol §7). Most published FRAP is dilute (low `γ_dec` → low `f_v`), so finding matched concentrated data is the search challenge.
2. **Stronger theory-side check.** Driving the injected test signal from the **actual canonical ED PDE** (Canon P6, `theory/Architectural_Canon.md`) in the oscillatory regime — done 2026-07-10 (`ed_pde_envelope_drive.py`) — is what confirmed ED itself *produces* the envelope and **corrected its frequency to `f_v≈1.1γ_dec` (from `8`)**. **Not yet reconciled below:** the `[80,800] Hz` search band, the `N_osc=8` prediction line, the `F2 ∈ [6,12]` criterion, and the synthetic-validation `N_osc=8.43` all still reflect the *old* 8× multiplier. The corrected prediction is `N_osc≈1.1`, band `~11–110 Hz`; the pre-registered F0–F5 band needs a deliberate update (it changes a pre-registered criterion — flagged, not silently rewritten).

Deps: numpy, scipy, astropy (all standard).
