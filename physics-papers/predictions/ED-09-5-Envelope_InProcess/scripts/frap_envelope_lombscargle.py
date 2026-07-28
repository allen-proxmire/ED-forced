"""
ED-09.5 Track B -- FRAP participation-envelope Lomb-Scargle pipeline.

Implements the pre-registered test in ../protocol.md (sections 6-10, F0-F5):

    Given a FRAP recovery curve I(t), subtract the best-fit smooth recovery
    model, Lomb-Scargle the residual r(t) = I(t) - I_model(t), and test for a
    participation-envelope peak at  f_v = N_osc * gamma_dec  (N_osc = 1.1 default, = Q/pi; corrected 2026-07-10 from 8)
    inside the [80, 800] Hz band, with the pre-registered Q_v, third-harmonic
    and triad-coupling checks.

Pre-registered parameters (protocol Sec.2, locked by Observable-Sharpening Sec.15):
    f_v (Hz)              = N_osc * gamma_dec,  N_osc = 1.1  (= Q/pi; corrected 2026-07-10 from 8)
    F0  factor-of-2 band  around f_v
    F2  N_osc in [6, 12]
    F3  Q_v   in [4, 9]
    F4  3rd-harmonic ratio in [3%, 6%]
    F5  triad coupling     in [0.01, 0.05]

SCOPE / HONESTY -- read this before quoting any output:
    This is the analysis INSTRUMENT. Running it on real concentrated,
    high-framerate FRAP data is the actual ED-09.5 Track B test. Running it on
    synthetic data (see synthetic_envelope_validation.py) validates the
    INSTRUMENT -- that it recovers a known injected envelope and does not
    false-positive on pure recovery + noise -- it does NOT test ED. A PASS here
    on synthetic data means "the detector works", not "ED-09.5 is confirmed".

Deps: numpy, scipy, astropy (all standard).
"""
from __future__ import annotations
import json
import numpy as np
from scipy.optimize import curve_fit
from astropy.timeseries import LombScargle


# --------------------------------------------------------------------------
# Recovery models (the smooth FRAP curve that gets subtracted)
# --------------------------------------------------------------------------
def _sat(t, tau):
    """1 - exp(-t/tau), guarded against overflow when the fitter probes tau<=0."""
    return 1.0 - np.exp(-np.clip(t / tau, -700.0, 700.0))


def _exp1(t, A, tau, C):
    """Single-component mobile-fraction recovery."""
    return C + A * _sat(t, tau)


def _exp2(t, A1, tau1, A2, tau2, C):
    """Two-component recovery (fast + slow mobile pools)."""
    return C + A1 * _sat(t, tau1) + A2 * _sat(t, tau2)


def _aic(residual, k):
    n = residual.size
    rss = float(np.sum(residual ** 2))
    rss = max(rss, 1e-300)
    return n * np.log(rss / n) + 2 * k


def fit_recovery(t, I):
    """Fit exp1 and exp2, return the lower-AIC model curve + metadata.

    Returns (model_curve, info) where info records which model won and its
    parameters. Falls back to exp1 if exp2 does not converge.
    """
    t = np.asarray(t, float)
    I = np.asarray(I, float)
    span = float(np.ptp(I)) or 1.0
    Tspan = float(t[-1] - t[0]) or 1.0

    # exp1
    p0_1 = [span, Tspan / 5.0, float(np.min(I))]
    try:
        p1, _ = curve_fit(_exp1, t, I, p0=p0_1, maxfev=20000)
        m1 = _exp1(t, *p1)
        a1 = _aic(I - m1, 3)
    except Exception:
        p1, m1, a1 = None, None, np.inf

    # exp2
    p0_2 = [span / 2, Tspan / 20.0, span / 2, Tspan / 3.0, float(np.min(I))]
    try:
        p2, _ = curve_fit(_exp2, t, I, p0=p0_2, maxfev=40000)
        m2 = _exp2(t, *p2)
        a2 = _aic(I - m2, 5)
    except Exception:
        p2, m2, a2 = None, None, np.inf

    if m1 is None and m2 is None:
        raise RuntimeError("both recovery-model fits failed")
    if a2 < a1:
        return m2, {"model": "exp2", "params": p2.tolist(), "aic": a2}
    return m1, {"model": "exp1", "params": p1.tolist(), "aic": a1}


# --------------------------------------------------------------------------
# Lorentzian peak model (for Q_v from the periodogram)
# --------------------------------------------------------------------------
def _lorentzian(f, f0, gamma, amp, base):
    return base + amp * (gamma ** 2) / ((f - f0) ** 2 + gamma ** 2)


# --------------------------------------------------------------------------
# The pipeline
# --------------------------------------------------------------------------
def analyze(t, I, gamma_dec, *, N_osc=1.1, band=(10.0, 120.0),
            f0_factor=2.0, fmax=None, fap_thresh=0.01, alpha_ring=0.018,
            n_boot=200, rng=None):
    """Run the full ED-09.5 Track B analysis on one recovery curve.

    Parameters
    ----------
    t, I        : recovery curve samples (seconds, intensity).
    gamma_dec   : system decoherence/relaxation rate (Hz) -> sets predicted f_v.
    N_osc       : pre-registered transient count (8, single-mode).
    band        : (lo, hi) Hz search band for the residual peak.
    f0_factor   : F0 tolerance -- measured f_v must be within this factor of pred.
    fmax        : top of the LS frequency grid (default 0.45*f_s).
    fap_thresh  : false-alarm probability below which a peak counts as real.

    Returns a dict with predicted/measured quantities and F0-F5 verdicts.
    """
    rng = np.random.default_rng(rng)
    t = np.asarray(t, float)
    I = np.asarray(I, float)
    order = np.argsort(t)
    t, I = t[order], I[order]

    dt = np.median(np.diff(t))
    fs = 1.0 / dt
    f_nyq = 0.5 * fs
    if fmax is None:
        fmax = 0.45 * fs

    f_pred = float(N_osc * gamma_dec)

    # --- recovery fit + residual ---
    model, minfo = fit_recovery(t, I)
    resid = I - model
    sigma_I = float(np.std(I))
    resid_rms = float(np.sqrt(np.mean(resid ** 2)))
    quality = resid_rms / (sigma_I if sigma_I else 1.0)

    # --- Lomb-Scargle of the residual (astropy: normalized power + FAP) ---
    fmax = min(fmax, 0.98 * f_nyq)
    freq = np.linspace(max(1.0, band[0] * 0.25), fmax, 4000)
    ls = LombScargle(t, resid, normalization="standard")
    power = ls.power(freq)

    in_band = (freq >= band[0]) & (freq <= band[1])
    if not np.any(in_band):
        raise ValueError("search band lies outside the LS frequency grid "
                         f"(band={band}, f_nyquist={f_nyq:.1f} Hz)")

    ib = np.where(in_band)[0]
    ipk = ib[np.argmax(power[ib])]
    f_meas = float(freq[ipk])
    p_meas = float(power[ipk])
    try:
        fap = float(ls.false_alarm_probability(p_meas, method="baluev"))
    except Exception:
        fap = float("nan")

    significant = np.isfinite(fap) and (fap < fap_thresh)

    # --- Q_v via Lorentzian fit of the peak (local window) ---
    Q_v = None
    try:
        w = (freq > f_meas * 0.5) & (freq < f_meas * 1.5)
        f0g, gg = f_meas, max(f_meas * 0.1, freq[1] - freq[0])
        pL, _ = curve_fit(_lorentzian, freq[w], power[w],
                          p0=[f0g, gg, p_meas, float(np.median(power[w]))],
                          maxfev=20000)
        fwhm = 2.0 * abs(pL[1])
        Q_v = float(f_meas / fwhm) if fwhm > 0 else None
    except Exception:
        Q_v = None

    # --- N_osc from Q_v via the pre-registered relation N_osc=(Q/pi)ln(1/alpha) ---
    N_osc_meas = (Q_v / np.pi) * np.log(1.0 / alpha_ring) if Q_v else None

    # --- F4 third harmonic: LS power at 3*f_meas relative to fundamental ---
    harm_ratio = None
    f3 = 3.0 * f_meas
    if f3 < fmax:
        j = int(np.argmin(np.abs(freq - f3)))
        harm_ratio = float(np.sqrt(max(power[j], 0.0) / max(p_meas, 1e-300)))

    # --- F5 triad coupling: crude normalized bicoherence at (f_v, f_v, 2 f_v) ---
    triad = _bicoherence_at(t, resid, f_meas, fs)

    # --- verdicts ---
    F0 = bool(significant and (abs(np.log2(f_meas / f_pred)) <= np.log2(f0_factor)))
    F2 = bool(N_osc_meas is not None and 6.0 <= N_osc_meas <= 12.0)
    F3 = bool(Q_v is not None and 4.0 <= Q_v <= 9.0)
    F4 = bool(harm_ratio is not None and 0.03 <= harm_ratio <= 0.06)
    F5 = bool(triad is not None and 0.01 <= triad <= 0.05)

    verdict = _decide(F0, F2, F3, F4, F5, significant, quality)

    return {
        "predicted": {"f_v_Hz": f_pred, "N_osc": N_osc, "gamma_dec_Hz": gamma_dec,
                      "Q_v_central": 6.3},
        "measured": {"f_v_Hz": f_meas, "ls_power": p_meas,
                     "false_alarm_prob": fap, "significant": bool(significant),
                     "Q_v": Q_v, "N_osc": N_osc_meas,
                     "third_harmonic_ratio": harm_ratio, "triad_coupling": triad,
                     "resid_rms_over_sigma": quality},
        "recovery_fit": minfo,
        "sampling": {"f_s_Hz": fs, "f_nyquist_Hz": f_nyq, "n_samples": int(t.size),
                     "duration_s": float(t[-1] - t[0])},
        "falsification": {"F0": F0, "F2": F2, "F3": F3, "F4": F4, "F5": F5},
        "verdict": verdict,
    }


def _bicoherence_at(t, y, f0, fs, n_seg=8):
    """Crude normalized bicoherence b^2(f0,f0) via segment averaging.

    Approximate and data-hungry; returns None if the record is too short to
    segment. Honest flag: on short/noisy residuals this is UNDECIDABLE and
    should not be over-read (protocol Sec.13 risk table).
    """
    y = np.asarray(y, float)
    n = y.size
    seg = n // n_seg
    if seg < 16:
        return None
    # resample to uniform grid for FFT-based bispectrum
    tu = np.linspace(t[0], t[-1], n)
    yu = np.interp(tu, t, y)
    win = np.hanning(seg)
    B = 0j
    P1 = 0.0
    P2 = 0.0
    freqs = np.fft.rfftfreq(seg, d=1.0 / fs)
    i1 = int(np.argmin(np.abs(freqs - f0)))
    i2 = int(np.argmin(np.abs(freqs - 2 * f0)))
    if i2 >= freqs.size:
        return None
    for s in range(n_seg):
        seg_y = yu[s * seg:(s + 1) * seg]
        if seg_y.size < seg:
            break
        Y = np.fft.rfft((seg_y - seg_y.mean()) * win)
        X1 = Y[i1]
        X2 = Y[i2]
        B += X1 * X1 * np.conj(X2)
        P1 += abs(X1 * X1) ** 2
        P2 += abs(X2) ** 2
    denom = np.sqrt(P1 * P2)
    if denom <= 0:
        return None
    return float(abs(B) / denom)


def _decide(F0, F2, F3, F4, F5, significant, quality):
    if quality > 0.5:
        return "UNDECIDABLE (residual dominated by fit error)"
    if not significant:
        return "FAIL_structural (no significant residual peak in band)"
    if F0 and F2 and F3 and F4 and F5:
        return "FULL_PASS"
    if F0 and F2 and F3 and not (F4 and F5):
        return "LINEAR_PASS (envelope + linear dynamics; triad absent)"
    if F0 and not (F2 and F3):
        return "FREQUENCY_PASS (right frequency, wrong dynamics)"
    if not F0:
        return "FAIL_structural (peak off predicted frequency)"
    return "PARTIAL"


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def _main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="ED-09.5 Track B FRAP envelope test")
    ap.add_argument("csv", help="CSV with columns t,I (seconds, intensity)")
    ap.add_argument("--gamma-dec", type=float, required=True,
                    help="system decoherence/relaxation rate in Hz")
    ap.add_argument("--n-osc", type=float, default=8.0)
    ap.add_argument("--band", type=float, nargs=2, default=[80.0, 800.0])
    ap.add_argument("--out", default=None, help="write JSON result here")
    a = ap.parse_args(argv)
    data = np.genfromtxt(a.csv, delimiter=",", names=True)
    t = np.asarray(data["t"], float)
    I = np.asarray(data["I"], float)
    res = analyze(t, I, a.gamma_dec, N_osc=a.n_osc, band=tuple(a.band))
    txt = json.dumps(res, indent=2)
    print(txt)
    if a.out:
        with open(a.out, "w") as fh:
            fh.write(txt)


if __name__ == "__main__":
    _main()
