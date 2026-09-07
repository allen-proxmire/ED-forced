# ED-09.5 Participation-Envelope Test

> **Artifact paths below are working-repo paths and are no longer in this repo.** This folder is the *record* of an in-process experiment; its data files, scripts and result JSONs live under `event-density` / `ed-lab`, and the paths are kept verbatim so a run can be reproduced there. *(Annotated 2026-09-07 during the dead-pointer sweep; they were being counted as broken links.)*

**Status:** InProcess. **Two parallel tracks** — one blocked on external collaboration, one executable within ~1 week at $0.

**Test of:** ED-09.5 sharp quantum-classical transition — the canonical ED PDE's damping-discriminant bifurcation at `D_crit = 0.5` (Canon P6) predicts that systems in the oscillatory regime (`D < 0.1`) carry a **slow envelope modulation** of their dynamics at frequency `f_v ≈ 1.1·γ_dec` (`= Q/π`; **corrected 2026-07-10** from an earlier erroneous `8·γ_dec` — see [`ED_PDE_Drive_Finding_2026-07-10.md`](ED_PDE_Drive_Finding_2026-07-10.md); corrected band ~11–110 Hz, needs ≥~250 Hz framerate). Quantum-side signatures include `Q_v ∈ [4, 9]`, third-harmonic content 3–6%, triad coupling `C ∈ [0.01, 0.05]`. ED-09.5 is **the single most distinctive falsifiable prediction in the ED corpus.**

**Channel exercised:** participation `v(t)` (Canon principle P5 — Participation Feedback Loop) + damping discriminant (Canon P6).

## The two tracks

### Track A — Cavity-coupled optomechanics reanalysis

**Target datasets:** Delic 2020 (levitated SiO₂) and Magrini 2021 (real-time feedback) — both at `D ~ 10⁻⁹`, predicted `ω_v/2π ≈ 16 mHz`, envelope period ~63 s, required record length ≥ 200 s.

**Observable:** slow envelope on raw heterodyne `x(t)` after demodulation at `ω_m`.

**Status:** **Blocked on raw data access.** Aspelmeyer email v3 drafted in [`docs/ED-09-5-Experimental-Strategy.md`](../../docs/ED-09-5-Experimental-Strategy.md) §7, not yet sent (pending affiliation line + cold-reader pass). Both Delic 2019 and Magrini 2021 theses are publicly downloadable but raw `x(t)` is not in any public deposit (verified 2026-04-20 via 5-step search).

**Timeline:** 2–6 months gated by Aspelmeyer response.

### Track B — FRAP-side Lomb-Scargle on public recovery curves

**Target datasets:** concentrated-FRAP datasets from the cell-biology literature with sampling rate ≥ 1 kHz (Mueller et al. 2008, Kang et al. 2012, Wachsmuth et al. 2003 as candidates). Predicted `ω_v/2π ∈ [80, 800] Hz`.

**Observable:** Lomb-Scargle periodogram of the residual `r(t) = I(t) − I_model(t)` after subtracting the best-fit standard recovery model from a public FRAP curve.

**Status:** **Pipeline BUILT + VALIDATED, and the prediction FREQUENCY CORRECTED ~7×, 2026-07-10** (`scripts/`). (1) The detector `frap_envelope_lombscargle.py` passes its synthetic validation (sensitive + specific). (2) **Driving the test from the real canonical PDE** (`ed_pde_envelope_drive.py`, [`ED_PDE_Drive_Finding_2026-07-10.md`](ED_PDE_Drive_Finding_2026-07-10.md)) found the participation envelope sits at **`f_v ≈ (Q/π)·γ_dec ≈ 1.1·γ_dec`, not `8·γ_dec`** — the `8` was a `10⁻³`-threshold cycle count mis-used in a `1/e`-time formula; the PDE reproduces the Canon's own `Q≈3.5` and gives `f_v/γ_dec≈1.1`. **Corrected band: ~11–110 Hz** (more accessible — needs ≥~250 Hz framerate, not 2 kHz). Commissioned FRAP is **not funded** ($15k declined). **Remaining = data** (literature dig) or a **spatial-PDE run** for the F4/F5 harmonic/triad legs.

**Timeline:** detector ready; band corrected; result gated only on data or a spatial-PDE harmonic run.

## Why two tracks test the same prediction

The `ω_v` prediction is regime-agnostic — it depends only on the system's decoherence rate `γ_dec`. The two tracks test the same ED-09.5 bifurcation in regimes separated by **10+ orders of magnitude** in `γ_dec` (mHz for optomechanics, 10–100 Hz for condensed-matter FRAP). A Full PASS on both would be the strongest possible confirmation of ED-09.5.

## Contents of this folder

| File | Purpose |
|:---|:---|
| `protocol.md` | Full operational protocol. §3–§5 cover Track A (Aspelmeyer); §6–§10 cover Track B (FRAP-side). Pre-registered parameters in §2; falsification criteria F0–F5 in §2 with per-track decision trees. |
| `README.md` | This file — status landing page. |

## Key external references

See `protocol.md` §15 for full list. Essential context:
- **Strategy:** [`docs/ED-09-5-Experimental-Strategy.md`](../../docs/ED-09-5-Experimental-Strategy.md) — three-tier strategy, draft emails to Aspelmeyer and Arndt, pre-send checklist.
- **Theory memo:** [`docs/ED-09-5-Observable-Sharpening.md`](../../docs/ED-09-5-Observable-Sharpening.md) v0.9 — §15 `ω_v = 2π·N_osc·γ_dec` derivation; §22 selects candidate-(b) `v ↔ X_cav` identification; §16 pre-registered F0–F5.
- **Vienna program map:** [`docs/ED_Vienna_Program_Map.md`](../../docs/ED_Vienna_Program_Map.md) — 12 candidate Vienna targets including Delic / Magrini / Arndt regimes.
- **Orientation:** [`docs/ED-Orientation.md`](../../docs/ED-Orientation.md) §5.5 (ED-09 + ED-09.5 overview), §7 empirical-status table (Track A + Track B rows).

## Related experiments

- **NOT the same as** [`../FRAP-High-BSA_InProcess/`](../FRAP-High-BSA_InProcess/) — that tests the **mobility** channel via `R(t) ~ t^(1/6)` spatial-front propagation, using raw TIFF stacks. Track B of this experiment uses the **1D recovery curve** residual, tests the **participation** channel, and can use literature data (no new sample prep required). Same class of instrument (FRAP), completely different observable and channel.
- AFM test at [`../AFM-Dewetting-ED-SC_InProcess/`](../AFM-Dewetting-ED-SC_InProcess/) tests the architectural-invariance claim rather than the participation channel directly; complementary, not redundant.

## Status transitions (for folder rename when outcome lands)

- `ED-09-5-Envelope_Evidence` on Full PASS in either track (strongest possible result for ED program).
- `ED-09-5-Envelope_PartialEvidence` on Linear PASS (F0 + F2∧F3 but F4∧F5 fail).
- `ED-09-5-Envelope_Falsified` on structural FAIL in both tracks.
- `ED-09-5-Envelope_Inconclusive` on UNDECIDABLE in both tracks.
- Current: `_InProcess` — Track A blocked, Track B executable.

## Next action

- ~~**Days 2–3:** write and validate the pipeline.~~ **DONE 2026-07-10** — see [`scripts/`](scripts/README.md) (built + validated, sensitive + specific).
- **Day 1 (now the gating step):** obtain a **concentrated, high-framerate (≥1–2 kHz)** FRAP recovery curve with known/estimable `γ_dec` — either a machine-readable literature dataset (protocol §7 candidates) or the in-house UDM-FRAP V2 high-framerate add-on. Most published FRAP is dilute (low `f_v`); matched concentrated data is the search challenge.
- **Then:** `python scripts/frap_envelope_lombscargle.py curve.csv --gamma-dec <Hz>` → per-dataset F0–F5; write up (result or null memo).
- **Recommended parallel theory check:** drive the injected signal from the actual canonical ED PDE (Canon P6), not a resonator, to confirm ED *produces* the `f_v≈1.1γ_dec` envelope (`scripts/README.md` §"stronger theory-side check"). *(Already run once, 2026-07-10: this is exactly the drive that corrected `8`→`1.1`.)*

In parallel: finalize the Aspelmeyer email v3 (Track A) and send.
