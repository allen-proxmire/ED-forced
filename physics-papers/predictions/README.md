# Predictions — Folder Guide *(falsification & the north-star prediction inventory)*

**What this folder is.** The prediction and falsification hub — the corpus's experiment-facing content, and the home of the goal that matters most: an **indisputable, confirmed, novel prediction**. It holds the falsification register / prediction inventory, the master predictions list, the "22 ways to kill ED" falsifier set, prediction bundles, postdiction (passed-test) records, and the **active in-process experiments** (protocols and, where run, prediction outputs).

**State** *(authoritative source: `event-density/docs/ED_Research_Targets.md` — the "prediction inventory" is flagged as the north-star meta-target; PAPERS_INDEX)*:
- **Paper_101 (the Falsification Register + Prediction Inventory) is the corpus capstone for the goal** — the survey of every falsifiable, experiment-facing prediction. Its **§0 (Sharpened Update 2026-07-10)** is the weapons-first view: a *ranked* separation of the genuinely novel, sharp, near-term bets from the postdictions and consistency-checks. The **current superset enumeration** is `ED_Master_Predictions_List.md` (2026-07-05, entries 1.1–5.6); Paper_101's §3/§5 register is pre-2026-05-13 and stale (the §0 update flags this). Growing this — from protocols to *run results* on the top bets — is the highest-leverage build for making ED *undeniable*.
- **The honest distinction is enforced here:** *postdictions / consilience* (reproducing known results — easy to fudge toward, weak evidence) are kept separate from *novel falsifiable predictions* (the failable ones that can actually end arguments).
- **Active experiments are in progress** (each in its own `*_InProcess/` subfolder with a protocol): RLC analogue, FRAP-BSA mobility, acoustic BEC/EIT/optical-pulse, AFM dewetting, QC mass extrapolation, triad coupling. These are operational and stay in this repo.
- **The sharpest near-term weapons** (Paper_101 §0.2): the **participation-envelope ratio `f_v≈1.1·γ_dec`** (`= Q/π`; corrected 2026-07-10 from a stale `8·γ_dec`; band ~11–110 Hz; the cheapest new result — FRAP Track B ≈ $0/1 week), the **offset–velocity cluster knee** (experiment-ready on existing fast mergers, `gravity/`), the **Class-A multiplicity wall** (140–250 kDa, `q-compute/`), the **Class-C error-correction plateau** (industry is testing it anyway), **BTFR zero intrinsic scatter**, **dark energy strict `w=−1`** (DESI), and the preferred-frame `α₂=0`-exact (`gravity/GR-IV`). *(The gauge-handedness ↔ matter-sign "correlation" is NOT a live prediction — it was retired to a wall by the 2026-07-08 ParityWall hardening.)*

**Tier key:** `Prediction` (novel, falsifiable, experiment-facing) · `Postdiction` (reproduces a known result — consilience, not failable) · `Register` (an inventory / falsifier list) · `In-Process` (an active experiment) · `Experiment` (a specific test paper).

---

## Registers, lists & bundles

| Paper | Contents | Tier |
|---|---|---|
| [Paper_101 — Falsification Register & Prediction Inventory](Paper_101_FalsificationRegister.md) | the corpus capstone: every prediction + falsifier, inventoried | **Register** (north-star build) |
| [The Master Predictions List](ED_Master_Predictions_List.md) | the running master list of ED predictions | Register |
| [22 Ways to Kill Event Density (+ Eight More)](22_Ways_to_Kill_Event_Density.md) | 30 concrete falsifiers (22 + 8) + 2 provisional + 3 already-passed | Register |
| [Predictions Bundle (a₀ = cH₀/2π)](Paper_ED_Predictions_Bundle.md) | empirical predictions from the substrate `a₀` identification | **Prediction** |
| [Postdictions / Passed Tests](Paper_ED_Postdictions_PassedTests.md) | tests ED already passes (consilience — *not* novel predictions) | Postdiction |

## Experiment papers

| Paper | Test | Tier |
|---|---|---|
| [FRAP Mobility-Scaling Template](Paper_ED_FRAP_Template.md) | FRAP test of the universal degenerate-mobility law in concentrated BSA | Experiment / Prediction |

## Active experiments (in-process)

Each has its own protocol and status in its subfolder:

| Experiment | Folder |
|---|---|
| RLC electrical analogue | [`ED-RLC-Analogue_InProcess/`](ED-RLC-Analogue_InProcess/README.md) — protocol + `rlc_predictions.py` + predicted-run plots |
| FRAP high-BSA mobility | [`FRAP-High-BSA_InProcess/`](FRAP-High-BSA_InProcess/README.md) — protocol + data |
| Acoustic BEC (extremal) | [`ED-Acoustic-BEC-Extremal_InProcess/`](ED-Acoustic-BEC-Extremal_InProcess/README.md) |
| Acoustic EIT (extremal) | [`ED-Acoustic-EIT-Extremal_InProcess/`](ED-Acoustic-EIT-Extremal_InProcess/README.md) |
| Acoustic optical-pulse | [`ED-Acoustic-OpticalPulse_InProcess/`](ED-Acoustic-OpticalPulse_InProcess/README.md) |
| AFM dewetting (ED-SC) | [`AFM-Dewetting-ED-SC_InProcess/`](AFM-Dewetting-ED-SC_InProcess/README.md) |
| ED-09.5 envelope | [`ED-09-5-Envelope_InProcess/`](ED-09-5-Envelope_InProcess/README.md) |
| QC mass extrapolation | [`QC-Mass-Extrapolation_InProcess/`](QC-Mass-Extrapolation_InProcess/README.md) |
| Triad coupling (C7) | [`Triad-Coupling-C7_InProcess/`](Triad-Coupling-C7_InProcess/README.md) |

*(The in-process experiment folders — protocols, data, and prediction outputs — are operational deliverables and stay in this repo, per AP. Growing Paper_101 into the full prediction inventory is the program's highest-leverage move toward the north star.)*
