# Path A — state at pause, 2026-09-05

*Written to be picked up cold, by me or by anyone. **Read this before resuming; do not reconstruct Path A from memory.** Everything below is checkable against the ledgers and the scripts named.*

---

## What Path A was

**One thread, followed where it led:** *can an AI, given only ED's stated assumptions, land on ED?* It started as a test of the framework's generativity and turned into something more useful — **a gap-finding instrument, and then an audit that reached the foundations.**

**23 ledger items (gravity #58–#80), all 2026-09-05.**

## Where it ended up — the honest read

**Better than it started, and the improvement is mostly subtraction.** Nothing new was derived that wasn't there; what changed is that several things that *looked* settled turned out not to be, and several things that looked missing turned out to be present. **Net: the corpus's self-description is now closer to the corpus.**

**Three things genuinely gained:**

1. **`Σ_C` is defined end-to-end for the first time.** `Str` = the diagonal, `Coh` = the off-diagonal (settled by arithmetic against `Paper_030`'s established result, confirmed 2/3 by external readers), `Grad` = a proposal (the discrete Dirichlet form, with six supports including one independent external proposal). **Every gravitational claim in the corpus runs through this functional, and this morning two of its three terms had no definition a reader could reach.**
2. **A real sign error found and fixed.** `Paper_030` §§4.3/5.2 published `Σ_cross = −√(GMa₀)log(R/R₀)`, whose gradient makes **MOND repulsive**. `Paper_QuadraticStrain_v1` §5.1 had it right. Hidden because §5.3 quoted one term as a magnitude and one at face value. **No downstream result moved.**
3. **The collapse identity.** `E_Δ = Str − Coh = −Σ_C` — Penrose's collapse energy is minus the ED stability landscape, exact, with all three limits right. Tier `D-via-I`.

**Three things genuinely lost, or narrowed:**

1. **`Paper_029`'s novelty is smaller than it read.** `a₀ ~ cH₀` is Milgrom's (1983); the `2π`-normalized form is standard in the review literature. **ED's claim is the derivation of the coefficient and nothing else** — and that coefficient is `Postulated / disputed`.
2. **Prediction 1.16's "no MOND analogue" was false** and had propagated to five sites including the public workbook.
3. **The soft-matter transport arc took real damage.** `F-EXIST` fired; `a_eff` is inherited, not derived; **ED does not explain MIR, it inherits it.**

## The three open items, ranked

**1. The layer seam. — THE 2π HALF IS PAID, 2026-09-06 (gravity ledger #101).** The seam divides rather than multiplies because **layer 1 counts and layer 2 winds**: the 2π in T = κ/2π is just ω = 2πν, a chain's acceleration is a **count-rate** (a ν, because P11's commitments are discrete events), and the horizon presents only coarse-grained as an ω. One conversion, direction fixed by P11. It also explains §4b's predicted pattern (one 2π per cross-layer comparison, none for like-layer). **And the second half is paid too, same day (#102): `Coh` is evaluated at LAYER 1, on raw polarity transported by P05** — because `∇_adj` makes accelerations layer-1 and `Coh` sits inside `Σ_C`; a layer-2 `Coh` would be phase-averaged and would cost MOND its transition scale entirely. **A correction fell out: `ξ` is NOT `≈ 5ℓ_ED` (that was a probe-grid lattice number I mis-read) but the MOND transition reach, `≳ 10¹⁵ m` — so `Θ₁₂` is coherent in any real experiment, not decoherent.** **Both seam debts are now closed; what remains open is the VALUE of `ξ` and of `a₀`, both inherited.**

**1. The layer seam.** Four arcs now reduce to one question: **at which layer is `Σ_C` evaluated, and what crosses the seam when it is read from the other side?** It carries the `a₀` `2π`'s remaining debt (§4f: *why `1/2π` and not `2π`*), the collapse arc's `Θ₁₂`, the `ln R` licensing, and `Grad`'s phase half. **`layers/` already has a thesis and a forced operator; what it does not supply is any account of a numerical factor attaching to a crossing.** That gap is the whole `2π`.

**2. The radial `1/R` channel density — an unnamed, un-tiered postulate.** `Paper_030` §4.3, one clause, justified by *"substrate-graph radial-projection geometry, anchored by P03."* **It is what turns an `R`-independent per-channel strain into a logarithm, and therefore what produces `√(a_N a₀)` rather than nothing.** Its sibling `P-Bilocal-Count` is named, tiered and has a falsifier; this has none. **A name is proposed in `Note_StrC_Bridge_2026-09-05.md` and deliberately not written into the paper — adopting it increments the census (171).**

**3. `Grad` remains a proposal. — STILL A PROPOSAL, and its one surviving discriminator was WITHDRAWN 2026-09-06 (#103):** the `ξ`-versus-coupling trend was a **coordination-number artifact** (a phase-blind control reproduces it). **The structural reason is now stated: `Coh` sums over contribution-pairs at a locus, `Grad` over graph edges, and a one-phase-per-node probe collapses those onto each other — so no probe of that design can settle it. A discriminating probe needs multiple channels per locus.** Six supports, one passed compatibility check, one failed Knots sub-case, not derived. And an open question about whether `Paper_PhaseCoherence`'s measured phase-alignment belongs to `Grad` rather than `Coh`.

## What not to trust without re-checking

- **My "what's missing" claims.** I was wrong four times in one session — three claims that the corpus lacked something it had (`Coh`'s definition, the disjoint-index-set reading, the `layers/` folder), and one over-classification (the aggregation as "missing structure"). **All four were caught by opening a file. Discount accordingly.**
- **Anything downstream of the `Coh`/`Str` split without noting its scope.** The three-way sign check answers *"which assignment, given the `ln R` form"* and **not** *"is the `ln R` licensed"*. Scope banner is on that note.
- **The blind run's S2 was 0/3.** Handed the candidates, 2/3 reach the settlement; blind, nobody did. **The split is the reading you get if you run the check, not the obvious reading of the material.**

## Instruments built (all re-runnable)

| Script | What it catches |
|---|---|
| `internal notes/_census_postulates.py` | postulate-count drift **and** the predictions cross-check (named falsifiers absent from the master list) |
| `internal notes/_sweep_comparative_claims.py` | claims that a rival framework lacks something (failure mode 8) |
| `internal notes/_check_sigma_sign.py` | the `Coh`/`Str` assignment against `a = a_N + √(a_N a_0)` |
| `internal notes/_check_030_cross_sign.py` | `Paper_030`'s cross-term sign |
| `internal notes/_check_grad_compat.py` | the Dirichlet `Grad` against the established results |
| `internal notes/_check_collapse_correspondence.py` | `E_Δ = Str − Coh` and its limits |
| `internal notes/_safe_edit_template.py` | **use this for scripted edits** — see below |
| `substrate-evaluation/Seed_F1_Arm{A,B,C}*.md`, `Seed_F1_S2_*` | the cold-model protocol, with pre-registered scoring |

**Two files were zeroed tonight by an unsafe edit helper** (`Paper_087_13Primitives.md`, `Gravity_TieredClaims_Ledger.md`) — both restored from git and verified by AP. **Use `_safe_edit_template.py` for any scripted edit: it encodes before opening, refuses a result under half the original length, and replaces atomically.**

## Housekeeping left

- **8 stale PDFs**, none of them touched today: `Paper_KhronometricEquationOfState_Jacobson`, `Paper_ED_DarkSector`, `Paper_GravityAsEquationOfState`, `Paper_HowPDECoarseGrainReality`, `Paper_HowTheoryCoarseGrainReality`, and three `readings/` papers. Only 15 PDFs exist across 314 markdown files.
- **The PR on `build/inline-math-operators` is still unopened** (`gh` not installed; body in `internal notes/PR_BODY_build_inline_math_operators.md`).
- **`Paper_029` prior-art citation**: Famaey & McGaugh section number unpinned, marked *"pin before submission"*.

## How to resume

1. **Read this file, then `Gravity_TieredClaims_Ledger.md` items #58–#80 in reverse order.** They are the whole thread.
2. **Run `_census_postulates.py`.** It exits 0 if the corpus is where Path A left it.
3. **The first real question is the layer seam** — it is the only item feeding four arcs, and unlike everything else in Path A it is about the physics rather than the bookkeeping.

---

*Paused 2026-09-05 to open Path B. Gravity ledger #58–#80; foundations #5–#12.*
