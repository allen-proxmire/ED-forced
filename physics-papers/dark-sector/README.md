# The ED Dark Sector

**What this folder is.** The **standalone dark-sector papers** — Event Density's peer-facing statement on dark matter across galaxies, clusters, and the CMB. The *working record* behind them (debt map, program note, position statement, build map) lives in the `event-density` working repo under `theory/Dark_Sector/`, with the probes in `event-density/evaluation/DarkSector/`.

## The position in one paragraph

ED explains **galactic** dynamics — rotation curves, the baryonic Tully–Fisher relation, `a₀` — **without** a dark-matter particle: the phenomenology is carried by the khronon (the arrow made dynamical), i.e. MOND (Papers KM-I, 027–034). ED does **not**, however, refute dark matter as *particle content* (stated in Paper_029 and Paper_031): the galactic success shows a particle is not *needed for galaxies*, not that none exists. The **cluster-scale missing-mass shortfall** (which MOND-class theories famously do not cover) and the **CMB acoustic peaks** are a *separate, mapped, addressable* debt (KM-I §8), not a contradiction. ED's candidate for that debt is a **committed neutral relic** produced at the inflation/saturation exit by the same admission mechanism that makes the baryons — decoupled (neutral), cold-capable (binding mass), `a⁻³`, and surviving reheating — **form-complete and native, with the relic's mass (hence its free-streaming length) value-inherited** and consistency-bounded to a **warm ~keV** window (the falsifiable prediction: warm dark matter, not a cold WIMP). So the dark sector is honest **open frontier with a live failure path**, sitting alongside a large body of cross-sector explanation — a frontier, not (yet) a killer, and stated as such.

## The papers (this folder)

- **[Paper_ED_DarkSector.md](Paper_ED_DarkSector.md)** — **START HERE.** The peer-facing flagship: the complete, evidence-first case, organized as **two culprits, one mechanism** (galaxies = the horizon/MOND, no particle; clusters+CMB = a warm neutral relic). It walks the evidence exhibit by exhibit (rotation curves, Tully-Fisher, DF2/DF4, clusters, the Bullet, lensing, cosmic web, CMB), contrasts ED with its nearest published rival (Berezhiani–Khoury superfluid dark matter), and states the distinctive bets — headlined by the flagship **a₀(z) = cH(z)/(2π)** evolution — and the honest gaps (CMB spectrum uncomputed; galactic small-scale puzzles unaddressed). Self-contained synthesis; the deep relic construction is the companion below. Built to `Paper_ED_DarkSector.pdf` (Zenodo) via `_build_paper.py`.
- **[Paper_ED_RelicLagrangian_v1.md](Paper_ED_RelicLagrangian_v1.md)** — the companion **construction**: assembles the relic field `Φ = √(ρ/m_R)e^{iθ}` from Baryogenesis + Mass-Without-Mass + MS-II; derives `ρ ∝ a⁻³` from the P11 commitment number; and coarse-grains `L_self` to canonical (`p ≈ 1.99`) → two-component. The detailed derivation behind the flagship's §3–4.

## The working record (in the `event-density` repo, `theory/Dark_Sector/`)

- `DarkSector_DebtMap.md` — what clusters and the CMB *require*, where MOND-class theories die, and what is proven vs. open (Bullet included).
- `DarkSector_SuperfluidRelic_Program.md` — the one-substance (Berezhiani–Khoury) exploration and its resolution to two-component, with the retraction history.
- `Paper_ED_DarkSector_Position.md` — the canonical position map: the galaxy/cluster/CMB split, the warm-keV bound, the honest crux and falsifiers.
- `DarkMatter_SourceInventory.md` — the build map for the eventual comprehensive "ED Takes on Dark Matter" paper (every DM-relevant paper sorted by the two-crimes spine; the Bullet is now a relic phenomenon).
- Probes: `event-density/evaluation/DarkSector/` (`relic_mass_bound.py`, `v5_coarsegrain_Lself_probe.py`, condensation / thermal / off-diagonal probes).

## Source papers (this folder synthesizes, it does not supersede)

- **Galactic MOND / no particle needed:** `../gravity/Paper_KM-I_KhrononMOND.md`, `../gravity/Paper_029_a0.md`, `../gravity/Paper_030_CombinationRule.md`, `../gravity/Paper_031_BTFR.md`, `../gravity/Paper_QuadraticStrain_v1.md`.
- **"Does not refute DM as particle content":** `../gravity/Paper_029_a0.md`, `../gravity/Paper_031_BTFR.md` (falsifier sections).
- **Cluster/CMB debt + cosmological sector:** `../gravity/Paper_KM-II_KhrononCosmology.md`, `../cosmology/Paper_ED_Cos_03_CMBAcoustic.md`, `../cosmology/Paper_ED_Cos_04_StructureFormation.md`.
- **The Bullet (relic-primary):** `../gravity/Paper_117_Bullet_TopologicalDefect.md` (repositioned — the relic gives the offset; the topological-defect offset-velocity law is a speculative bonus).
- **Not the DM candidate (ruled out in-corpus):** `../black-hole/Paper_041_RemnantMass.md` (Planck-mass remnants are explicitly *not* the DM candidate).
- **The neutral-relic candidate machinery:** `../cosmology/Paper_ED_Baryogenesis.md` (saturation-exit admission), `../qft/Paper_MS-II_MatterSectorFromTheArrow.md` (neutral singlet in the channel structure), `../substrate-evaluation/Paper_MassWithoutMass_BindingInertia.md` (binding mass; magnitude inherited).
- **Conserved-current dust structure:** `../gravity/Paper_GR-II_KhronometricClass.md` §3.

## Honest status (read before citing)

Form-complete, value-inherited, with a named risk. Nothing here is a closed derivation; the galactic account (MOND) is the strongest piece and is a separate, standing result. The cluster/CMB account is a *candidate direction*, not a computed fit — no CMB spectrum is computed from ED, the relic mass is not derived (only consistency-bounded to warm ~keV), and the natural-scale expectation leans cold. Treat the papers here as the peer-facing statement of an open frontier; the working record in `event-density/theory/Dark_Sector/` carries the audit trail.

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[`DarkSector_TieredClaims_Ledger.md`](DarkSector_TieredClaims_Ledger.md)** — the arc's **tiered-claims ledger**: every load-bearing claim in this folder with its current tier. It doubles as the arc's staleness detector — where a paper and the ledger disagree, the ledger's `Status` column is the current state. Read it before citing anything here.
