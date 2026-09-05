## What this is

An audit-and-research branch spanning 2026-08-31 → 2026-09-05, with the bulk on 09-04/05. **146 files, +4138/−411.** No physics was overturned; every finding was about a sentence, a scope, or a pointer.

The full audit trail is `physics-papers/gravity/Gravity_TieredClaims_Ledger.md`, staleness items **#10–#57**. The map is `internal notes/AUDIT_2026-09-04_ClaimStrength_AllArcs.md`.

## The audit half

A claim-strength pass over every arc ledger, asking one question of each load-bearing chain: *does the sentence claim exactly what the derivation supports?*

- **One claim lost its tier.** The `1/(2π)` in `a₀ = cH₀/(2π)` is not established as forced — it cancels in `Paper_028` §6.3 and `Paper_029` §5.1's own displayed algebra. Re-tiered **Postulated/disputed** and flagged in twelve documents. `a₀ ~ cH₀` is untouched and now has four independent routes.
- **Six claims were one notch stronger than their support** (GR-IV's `α₂ = 0`, `Paper_030` §6.3/§7.2, `Paper_038.5`'s `w = −1`, `Paper_027`'s "unique", `Paper_065` §3.3, `Paper_066`'s three locks). In every case the paper's own audit table already said the right thing.
- **Seven propagation failures** — corrections recorded in a ledger and never distributed. The last one **inverted**: a 2026-07-29 entry that should never have been made, distributed once and then cited as settled fact for five weeks (#57).
- **Two arcs returned nothing**: Yang–Mills and relativistic-QM.

## The research half — gravity arc

- **The MOND threshold's switch is now derived**, from `Paper_039` §3.1 + `Paper_090` §4.4, with **no new postulate** (#34).
- **`μ` is re-filed as the inherited V5 envelope** — not an open derivation, which is why three attempts to derive it were blocked.
- **`Σ₀` resolved and the rewrite applied** (#36/#37): `a₀` is a normalization, not a force. `Paper_030` now reads `a = a_N + √(a_N a₀)`, both limits follow as limits, and §5.3's regime assumption is **removed**.
- **QuadraticStrain's second discharge rescued** (#44) — the asymmetry it needed was #36's, not a dipole.
- **Prediction 1.16 registered**: `H₀ = 2πa₀/c`, the Hubble constant from rotation curves. No MOND analogue. Currently `77.0 ± 6.3`.

## Structural

- **Research target #20 closed** with a ladder, not a number: 171 declared postulates, 26 cross-cutting, **103 (60%) used in exactly one paper**. `internal notes/POSTULATE_BASIS.md`.
- **New standing check**: `internal notes/_census_postulates.py` — re-runnable, declares its basis, exits nonzero on drift. It caught its own author twice.
- **The corpus's sixteenth arc ledger**: `soft-matter/` had 17 papers and no ledger, which is why it was invisible to the audit. The coverage claim was measuring the instrument.
- **Four `ED-SC 4.x` papers migrated** from a frozen fork into `cosmology/`, each with the disputed `2π`, the `ξ` precision correction, and its arc caveat. They discharge `Paper_SCBU`'s own falsifier F4.
- **`ξ_canonical` traced to ground**: measured, not memory-floating — but `1.76 ± 0.30`, not `1.7575`, and processing-dependent.

## Review notes

- **Nothing here is a silent edit.** Every correction carries a dated flag naming what it superseded; withdrawn findings keep their original text as audit trail.
- **Four flags were placed and then withdrawn the same session** (#56 → #57). That reversal is deliberate and documented — the four-band partition is canonical, and the near-miss is recorded as a method caution.
- **Dating**: the session crossed midnight. Items #10–#45 are 2026-09-04; #46–#57 are 2026-09-05. Headers are corrected; body stamps inside the later items still read 09-04 and should be read as "this session." See the session-boundary note at the head of the staleness section.
- **The branch name is stale.** `build/inline-math-operators` no longer describes the contents.

## What is still open

The `2π` coefficient (four routes to the scale, none to the coefficient — but it now has an empirical clock via 1.16); target #19's remaining debt; target #21 (derive the V5 envelope shape); `SC_4_3` and `SC_4_6` still in the fork; and a two-line repair to `Paper_087` §P04's cross-reference.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
