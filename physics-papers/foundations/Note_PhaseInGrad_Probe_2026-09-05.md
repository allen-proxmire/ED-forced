# Phase-in-`Grad`: finite-reach survives in the physical case, crystallizes in the partial one. And a third support for the split, from the density matrix.

> **⚠ THIS PROBE'S `Coh` ARM IS NOT `Coh` — found 2026-09-06 (gravity ledger #104).** The docstring is accurate that *“the substantive difference is precisely the `/n` normalisation”*, and **`|acc|` is correct for `Grad`** (maximising the Dirichlet form over `v`'s free phase gives exactly `2|acc|`). **But `|acc|/n` is not canonical `Coh`** — it is the simulator's `v3_active` per-locus-average convention. **Canonical `Coh` maximised over `v`'s phase gives `2|acc|` PLUS a neighbour–neighbour cross term**, and `|acc|/n` has no such term: it is `Grad` divided by the coordination number. **So the comparison being run was `Grad` against `Grad/n` — the `Coh`-versus-`Grad` question was never actually being asked.** That explains the draw on Knots-safety (both arms are the same functional), and it explains why #103's `ξ` trend was a coordination-number artifact: **`/n` *is* the coordination number, and it was the only difference between the arms.** `foundations/Note_MultiChannel_CohGrad_2026-09-06.md`.

*Foundations working note, 2026-09-05. Answers the open item raised by `Note_Grad_Proposal_2026-09-05.md` §5. Probe: `../event-density/theory/p12_phase_in_grad_probe.py`, re-runnable.*

---

## Verdict

**The open item does not close, and the reason is worth more than a closure would have been: both readings survive where it counts, so Knots-safety cannot discriminate between them.**

| Condition | `Coh` reading (`|acc|/n`) | `Grad` reading (`|acc|`) |
|---|---|---|
| **CONTROL** — homogeneous, no disorder | CRYSTAL (expected) | CRYSTAL (expected) |
| **(A)** — bandwidth holonomy only | **finite-reach**, `ξ ≈ 4–6` | **CRYSTAL**, `R ≈ 0.9`, `ξ = grid` |
| **(C)** — physical: bandwidth **and** `ρ` holonomy | **finite-reach**, `ξ ≈ 3.7–4.2` | **finite-reach**, `ξ` falls `2.2 → 0.8` |

**In the physically-faithful case both are Knots-safe.** So the `cos Θ` discharge keeps both of its supports, and neither assignment is eliminated.

**But the `Grad` reading acquires a crystallizing sub-case the `Coh` reading does not have**, and that is a real limit on the proposal — recorded in §4.

---

## 1. What was changed, and why it is the right change

Write `acc(v) = Σ_{w committed nbr} exp(i(φ_w + A(w→v)))`.

- **`Coh` reading** (`v3_active`, as run in July): bonus `= |acc| / n`, in `[0,1]`. **A per-locus average** — *do the incoming votes agree with each other?*
- **`Grad` reading** (this probe): bonus `= |acc|`, in `[0,n]`. **An edge sum** — every edge contributes, so agreement *and* neighbour count both raise it.

**That normalization is not a free parameter; it is the whole difference between the two terms.** Maximising the Dirichlet form `Σ_w |P(v) − P(w)|²` over the candidate's not-yet-assigned phase gives exactly `2|acc|` at `b ≈ 1`, and the `2` absorbs into `k_phase`. **An edge sum is extensive; a per-locus coherence is intensive. The `/n` is the discriminator.**

The deposit rule is untouched — setting `φ_v` to the resultant angle is already the Dirichlet-optimal choice — so **only selection differs.** Matched seeds throughout.

## 2. The results, read carefully

**(C), the physical case — both safe, and they differ in a new way.** `Coh`'s `ξ` sits at `3.7–4.2`, essentially **flat** across a 16× sweep in `k_phase`. `Grad`'s `ξ` falls **monotonically**, `2.2 → 1.9 → 1.5 → 1.0 → 0.8`, as the coupling strengthens.

**That trend is the interesting part, and at first sight it is backwards**: strengthening an alignment reward should not shorten the correlation length. The explanation is in the extensivity. `|acc|` rewards *many* neighbours as much as *aligned* ones, so a strong coupling makes the front prefer high-coordination sites rather than phase-coherent ones. **The phase order is not being reinforced; it is being outcompeted by a coordination-number preference riding in the same term.**

**(A), bandwidth holonomy only — `Grad` crystallizes at every non-zero coupling.** `R ≈ 0.89–0.96`, `ξ` = grid. The `Coh` reading stays finite-reach here (`ξ ≈ 4–6`). **This is a Knots violation for the `Grad` assignment in a sub-case where the `Coh` assignment is safe.**

**Control — both crystallize**, as they must: with no disorder there is nothing to break the order, and the July arc found the same. Sanity check passed.

## 3. What this settles and what it does not

**Settles:** the `Grad` assignment **does not destroy** the July result. In the physically-faithful substrate, phase-order remains finite-reach whichever term carries the phase. **`Paper_QuadraticStrain_v1` §9's `cos Θ` discharge is unaffected and retains both its supports.**

**Does not settle:** which term the July measurement belongs to. **Knots-safety was the obvious discriminator and it comes back a draw in the case that matters.**

> **⚠ THIS DISCRIMINATOR IS WITHDRAWN, 2026-09-06.** The cleaner probe named in the honest-limit paragraph below was run (`../event-density/theory/p12_grad_decomposed_probe.py`). **A phase-blind control — `bonus = n`, coordination number with the phase information deleted — reproduces the shrinkage: `2.0 → 0.6`, tracking `Grad`'s `2.2 → 0.8`.** **So the trend is an artifact of extensivity and says nothing about phase.** And the reason is structural rather than a tuning problem: **`Coh` sums over contribution-pairs *at a locus* while `Grad` sums over *graph edges*, and this probe carries one phase per node — which collapses the two index sets onto each other, leaving only the normalization to differ.** **No probe of this design can settle the question; a discriminating one needs multiple channels per locus.** `foundations/Note_GradPhase_Decomposed_2026-09-06.md`; gravity ledger #103.

**Notes a new discriminator, which did not exist before this run:** the *direction of `ξ`'s response to coupling strength*. Flat for `Coh`, monotonically shrinking for `Grad`. **A measurement of that trend in a system where the substrate's disorder is independently characterized would separate the two readings** — that is a sharper test than anything the original arc had, and it is not currently available.

**Honest limit on the run, and it is not cosmetic.** The extensive form conflates two effects: alignment quality and coordination number. **A cleaner probe would decompose `|acc| = n × (|acc|/n)` and sweep the two weights independently**, which would say whether `Grad`'s (A)-crystallization is a phase effect or a connectivity effect. **Until that is done, §2's explanation of the shrinking `ξ` is an interpretation of the numbers, not a measurement.**

## 4. The limit this places on the `Grad` proposal

`Note_Grad_Proposal_2026-09-05.md` listed four supports and no known problems. **It now has a known problem:** under the `Grad` assignment, condition (A) crystallizes, and long-range order in any sector is what `Paper_BlindnessInvariant_KnotsNotCrystals` rules out.

**Two readings of that, and the note should carry both.** Either **(i)** the `Grad` assignment is wrong and the phase belongs to `Coh`, whose (A) behaviour is clean; or **(ii)** condition (A) is not physical — it strips the substrate's own `ρ`-field disorder, keeping only quenched connectivity — and the physical case (C) is the one that must be Knots-safe, which it is. **The July arc made exactly argument (ii) about its own crystallizing sub-case (B), so the corpus has already accepted that reasoning once.** Applying it here is consistent, but it should be noticed that **each reading now has a crystallizing sub-case and each is defended by the same argument.**

**Tier on the `Grad` proposal is unchanged: proposal, form-forced-conditional at best.** This run neither confirms nor kills it; it adds one passed test in the physical case and one failed test in a partial one.

## 5. A third support for the `Coh`/`Str` split, from an unexpected direction

Prompted by AP's recollection of *"a paper about diagonal and off-diagonal"*. It exists — `readings/ED_Reading_ManyWorlds_TheOtherReadingOfSchrodinger.md` — and although it is about the density matrix rather than P12, **the correspondence is exact:**

> *"Its diagonal entries `|ψ_K|²` are real, phase-free, and committed, the Born weights. Its off-diagonal entries `ψ_K* ψ_L` carry the relative phase, interference between outcomes … commitment is the diagonalization of `ρ`. It removes the off-diagonal coherences and leaves the diagonal facts."*

Set against today's settled P12 split:

| | Density matrix `ρ = ψψ*` | P12 `Σ_C` |
|---|---|---|
| **Diagonal** | `|ψ_K|²` — real, phase-free, **committed** | `Str_K = Σ_a b_K^{(a)}` — real, phase-free |
| **Off-diagonal** | `ψ_K*ψ_L` — carries relative phase, **interference** | `Coh_K = 2Σ√(b_a b_b)\cosΘ_{ab}` — carries relative phase |

**Same structure, same names, and the same physical operator moving between them: P11 commitment.** If commitment diagonalizes, then **committing destroys `Coh` and leaves `Str`** — which is precisely what one would want if `Coh` is uncommitted interference content and `Str` is the settled load.

**This is a consilience, not a derivation.** It does not prove `Σ_C`'s terms *are* `ρ`'s entries. But it is a **third independent support** for an assignment already backed by the gravity arithmetic and by AP's Relation/Boundary/Gradient reading — and unlike those two it comes from the quantum-foundations arc, which had no stake in the question. **It also supplies something the split previously lacked: a dynamics. P11 is the operator that moves content from `Coh` to `Str`.**

**Worth pursuing separately:** if commitment really is the `Coh → Str` transfer, then `Σ_C` should decrease at a commitment by exactly the destroyed interference. That is checkable against `Paper_054`'s and the state-reduction arc's treatment of commitment cost, and nobody has looked.

---

*Gravity ledger Staleness #73. Probe: `../event-density/theory/p12_phase_in_grad_probe.py`.*
