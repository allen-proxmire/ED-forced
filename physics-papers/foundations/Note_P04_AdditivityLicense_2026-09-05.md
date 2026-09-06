# Note — When P04's additivity extends past disjoint sub-channels, and what licenses it

**Date:** 2026-09-05 (late)
**Status:** Working note. Resolves the `Paper_073` §3.2 flag raised in `Note_EdgeWeight_Discriminator_2026-09-05.md` §8c, and finds the defect is **corpus-wide documentation, not a local error**.
**Check:** `internal notes/_check_dcgt_regime_users.py` (screen + adjudication, re-runnable).
**Write-back:** licensing clause added to canonical `Paper_087` P04; follow-up note at `Paper_073` §3.2. Gravity ledger #90.

---

## 1. The question

`Note_EdgeWeight_Discriminator` §8c flagged that `Paper_073` (DCGT) §3.2 attributes bandwidth-additive merging over a coarse-graining cell to *"P04 (bandwidth additivity)"* with no regime condition. **The open question was whether anything downstream inherits that clause where coherence survives across the cell** — which would be a live error rather than a documentation defect.

**105 papers cite DCGT**, so the question needed narrowing twice: first to papers doing coarse-graining work near coherence content (55 by proximity screen), then to the operation actually at issue.

## 2. The operation actually at issue

Canonical `Paper_087` P04 states additivity as:

> Additive under channel decomposition: `b_{K₁∪K₂} = b_{K₁} + b_{K₂}` for **disjoint sub-channels**.

**That is its scope: disjoint sub-channels at a locus.** Summing bandwidth over a **region** or a **cell** — over *loci* — is a different operation, and the general rule for combining contributions is §P12's `b(U) = Σ_a b_a + 2Σ_{a<b}√(b_a b_b)cos Δπ_ab`, whose cross term is `Coh`. Plain addition is its zero-phase case.

**So the right search was not "who cites DCGT" but "who cites P04 additivity for an over-a-region sum".** That found at least eight sites.

## 3. The adjudication

| site | what it sums | verdict |
|---|---|---|
| `Paper_004_6_Tsirelson_Continuum` | `Σ_K → ∫`, `P_K → Ψ(x)` | **not at risk** — coarse-grains **amplitudes** |
| `Paper_009_BerryPhase` | substrate connection → `U(1)` one-form | **not at risk** — a phase object, not bandwidth |
| `Paper_066_NoSignaling` (L3) | operator support / local algebras | **not at risk** — locality, not bandwidth |
| `Paper_065_Monogamy` | `W_A = Σ_i` over **partner chains** | **licensed** — partners are disjoint channel sets: P04 *as written* |
| `Paper_067/068_VonNeumannEntropy` | `S(ρ_A⊗ρ_B) = S_A + S_B` | **licensed** — explicitly **independent** subsystems; named `P-Additivity` |
| `Paper_042_NoSingularity` | `C_cum` over a spatial **region** | **licensed** — `C_cum` is **committed** content |
| `Paper_V5UnifiedBudget` | `W_max = ∫F_V5 dμ` | **licensed** — integral of a bounded kernel; additivity decorative |
| `Paper_073_DCGT` §3.2 | bandwidth over **loci in a cell** | **licensed** — decoherent by its own §3.3 |

**The three coherence-critical papers turn out not to inherit the clause at all.** They coarse-grain amplitudes, connections and operator support — never bandwidths. That is the right thing to do and it is what the corpus already does, without saying that it is making a choice.

## 4. The common license, which none of them state

Every site is fine, and **all for the same reason: the summed contributions carry no relative phase.** That happens exactly three ways in ED:

**(a) Disjoint channels** — P04's additivity precisely as written. `Paper_065` sums over *partner chains*, which are disjoint channel sets, so it is not an extension at all.

**(b) Committed content** — **P11 commits in the channel basis only.** From `Paper_QuantumLogicKeystone_GleasonReconstruction` §7: *"ED commits only in the channel basis: the channel basis is the unique pointer basis, selected by the arrow … phase … is never a commitment basis."* **Committed content has no phase left to interfere, so bandwidth is additive over a region for it.** This is what licenses `Paper_042`'s `C_cum` bound, and it is the most interesting of the three, because it means **commitment is what makes bandwidth behave classically over a region** — the arrow doing structural work nobody had cashed out here.

**(c) A decoherent regime** — `Coh → 0`. `Paper_073` §3.2's hydrodynamic window (§3.3 averages out exactly the phase-carrying microstructure), and `Paper_067/068`'s independent subsystems.

**Outside (a)–(c) the extension is not licensed.**

## 5. The error would not run in the safe direction

Worth stating because the intuition points the wrong way. Phase-aligned contributions carry **more** total bandwidth than the additive sum — `n²` against `n` for `n` unit contributions. **So a bound derived from bandwidth-additivity is not conservative; it would be violated, by a factor up to the number of contributions.**

That is why the license matters for `Paper_042`'s no-singularity bound in particular. **`Paper_042` is doubly safe**: its bound is a *named postulate*, `P-Bandwidth-Boundedness`, not a consequence of additivity alone. But the general point stands — an unstated licensing condition on a step that fails *upward* is worth writing down.

## 6. Verdict

**No live error found.** The defect is documentation, and it is **corpus-wide rather than local to `Paper_073`** — an unstated licensing condition on a step taken in at least eight papers. `Paper_073` is on the safe side of a rule it happens to instantiate.

**Written back once, canonically, at `Paper_087` P04**, where the primitive being extended lives, rather than eight times. `Paper_073` §3.2 now points at it and names its clause, (c).

**What this does not settle.** Whether any *future* construction lands outside (a)–(c) — the clause is a rule to check against, not a guarantee. The individuation edge weight is the first construction that had to sit explicitly inside one of these regimes to be well-defined (`Note_EdgeWeight_Discriminator` §8b); it will not be the last.
