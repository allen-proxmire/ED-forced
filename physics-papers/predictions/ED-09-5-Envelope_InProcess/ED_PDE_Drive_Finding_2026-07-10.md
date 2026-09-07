# ED-09.5 driven from the real canonical PDE — the envelope frequency is `f_v ≈ (Q/π)·γ_dec ≈ 1.1·γ_dec`, not `8·γ_dec`

> **Artifact paths below are working-repo paths and are no longer in this repo.** This folder is the *record* of an in-process experiment; its data files, scripts and result JSONs live under `event-density` / `ed-lab`, and the paths are kept verbatim so a run can be reproduced there. *(Annotated 2026-09-07 during the dead-pointer sweep; they were being counted as broken links.)*

**2026-07-10.** Crank-rail ON; this is a NEGATIVE about ED's own flagship prediction, held to the same bar as a positive (simulation + analytic cross-check + regime check). Script: [`scripts/ed_pde_envelope_drive.py`](scripts/ed_pde_envelope_drive.py).

## What was done
Instead of a resonator stand-in, I integrated the **actual canonical ED PDE** (`event-density/theory/Architectural_Canon.md`, principles P2+P3+P5, uniform-mode reduction — the same object Observable-Sharpening §22 used to fix the `v↔X_cav` identification): `ρ̇ = D·F + H·v`, `v̇ = (F − ζv)/τ`, with `F = −P_SY2(ρ)` and the P3 saturating penalty. Ran it in the oscillatory regime (P6: `(D−ζ)² < 4(1−D)`), extracted the participation field `v(t)`, and **measured** its frequency `f_v`, decay `γ_dec`, quality `Q = ω₀/2γ_dec`, and the ratio `r = f_v/γ_dec` (= cycles per 1/e envelope time) — no ansatz.

## Result

| regime | Q (measured) | `r = f_v/γ_dec` | vs prediction `r=8` |
|---|---|---|---|
| **canon-default ζ=¼, D=0.02** | 3.6 | **1.16** | off ~6.9× |
| **canon-default ζ=¼, D=0.05** | 3.2 | **1.03** | off ~7.8× |
| **canon-default ζ=¼, D=0.09** | 2.8 | **0.89** | off ~9× |
| large-amplitude (probes nonlinearity) | ~3.2 | ~1.0 | nonlinearity does **not** rescue it |
| ζ=0.02 (non-default, high-Q) | 33 | 10.4 | "holds" — but Q=33 ≠ Canon's Q≈3.5 |

Two independent confirmations that this is the faithful PDE, not a strawman:
1. **The measured `Q ≈ 3.5` reproduces the Canon's own stated invariant** (`Architectural_Canon.md` §3: "Quality factor `Q ≈ 3.5` in the oscillatory sector"). The simulation is the canonical PDE.
2. **The analytic relation closes it exactly.** For any damped oscillator, the number of cycles until the amplitude falls to a fraction `f` is `N(f) = Q·ln(1/f)/π`. So `N_osc = 8 ⟺ Q = 3.5 AND f = 10⁻³` (`3.5·ln(1000)/π = 7.7`). The `N_osc≈9`/`Q≈3.5` pair the corpus lists as two invariants is **one quantity**: `N_osc` is just `Q` re-expressed with a `10⁻³` amplitude threshold.

## The error, precisely
Observable-Sharpening §15 derives `τ_v = N_osc·(2π/ω_v)` with the ansatz `τ_v = 1/γ_dec` (the **1/e** envelope decoherence time), giving `ω_v = 2π·N_osc·γ_dec`. That formula is only correct if `N_osc` is the cycle count **within one 1/e time**, which is `r = Q/π ≈ 1.1`. But the value plugged in — `N_osc = 8` — is the ED-Phys-17 turning-point count **down to ~10⁻³ amplitude** (`ed_phys_oscosmo.py` lines 408–415, replicated). **Plugging a 10⁻³-threshold cycle count into a 1/e-time formula overstates the envelope frequency by `8 / (Q/π) ≈ 7×`.** The corpus flagged this Q-vs-N_osc inconsistency (Observable-Sharpening v0.4, 2026-04-20) but resolved it toward `N_osc=8`; running the real PDE resolves it the other way — toward the dynamically consistent `Q≈3.5` it reproduces.

## The corrected prediction (survives, sharper, ~7× lower)
The participation envelope is **real and still distinctive** — the correction is to its frequency, not its existence:

    f_v ≈ (Q/π)·γ_dec ≈ 1.1·γ_dec        (from the Canon's own Q≈3.5, self-consistent)

not `8·γ_dec`. Consequences for the (unfunded — commissioned FRAP is off the table, AP 2026-07-10) test design:
- **Track B FRAP band:** `~11–110 Hz`, not 80–800 Hz. *This makes the test MORE accessible* — Nyquist ~220 Hz needs only ≥~250 Hz framerate, vs the 2 kHz the 80–800 Hz band demanded.
- **Track A optomechanics (Delic/Magrini):** envelope at `~2.2 mHz`, period `~450 s` (not 16 mHz / 63 s) — a longer contiguous record required. Worth fixing before any Aspelmeyer ask.

## Honest scope
- This is the **uniform-mode** canonical PDE (the §22-anchored object). Harmonics (F4) and triad (F5) require the P7 gradient term (spatial structure) and are not tested here — but they do not affect the `f_v` correction, which is set by Q.
- The correction is `f_v` (frequency), tied to the reproduced `Q≈3.5`. If a future spatial run showed the canonical oscillatory sector genuinely sustains `Q≈25–33` (contradicting the Canon's own invariant), `8·γ_dec` would return — but the large-amplitude runs give no sign of that, and it would require retiring the `Q≈3.5` invariant.
- **Net:** ED-09.5 is not falsified; its central frequency is corrected downward ~7×, and it becomes internally consistent (one Q, one number) and somewhat easier to test. The detector pipeline (`frap_envelope_lombscargle.py`) is unaffected — only its default `N_osc` changes from 8 to `Q/π≈1.1`.

## Addendum — the harmonic leg (F4), spatial run: order-consistent, NOT cleanly confirmed (inconclusive)
`scripts/ed_pde_spatial_harmonic.py` runs the full 1-D canonical PDE (the P7 gradient term is nonzero only with spatial structure, so the uniform run above could not test harmonics). Honest, hedged result:
- The nonlinearity **does** generate a 3rd **spatial** harmonic (k=3 from the k=1 excitation) that **grows with amplitude**, reaching **~2%** at moderate excitation — the same order of magnitude as the pre-registered 3–6% (P7's spatial invariant), slightly below, plausibly reaching the band at larger amplitude.
- But the **temporal** 3rd harmonic (the quantity the FRAP/optomechanics observable F4 actually measures, power at `3·f_v`) comes out **~0.1% and amplitude-independent** — i.e. at/near the numerical floor, **far below the 3–6% claim**. This suggests the protocol's F4 (a *temporal* 3–6%) may conflate P7's *spatial* harmonic invariant with the *temporal* observable; the spatial→temporal mapping is not established.
- **Verdict: inconclusive.** The P7 harmonic *mechanism* is present (spatial, few-%), but the specific F4 *observable* value (3–6% temporal) is not reproduced by this run and needs a careful spatial→temporal derivation before it can be a pre-registered number. This is a soft caveat, not a hard error like the 7× frequency correction — flagged, not banked as a claim.
