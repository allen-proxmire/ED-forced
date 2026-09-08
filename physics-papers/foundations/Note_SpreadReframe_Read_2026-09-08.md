# Reading `SPREAD_AND_DU` on its own terms — the one Koide-line result none of the blockers touch

**2026-09-08.** AP: *read `SPREAD_AND_DU` on its own terms.* The arc-Q negative (§4.4.1) closed the three routes into ED. **This note is about the piece that survives, because it never enters ED's substrate at all** — it uses `Q` as published and makes no substitution, so neither the `b`-assignment gap nor the chain-identity block reaches it.

**Verified independently rather than accepted:** `theory/Koide_Hierarchy/spread_claims_verify.py`, re-runnable.

---

## 1. Three load-bearing claims, checked

| claim | verdict |
|---|---|
| **`Q` is invariant under common rescaling `m → k·m`** | **CONFIRMED, exact.** `Q = Σm/(Σ√m)²`; numerator and denominator each scale by `k`. Identical to 8 figures at `k = 1, 137, 10⁶`. *So flavour-universal running cancels out of `Q` and only **differential** running moves it.* |
| **`Q_ν ≤ 0.584` (normal) / `0.500` (inverted), so `2/3` is EXCLUDED for neutrinos** | **CONFIRMED.** Scanned the lightest mass from `0` to `1 eV` against `Δm²₂₁ = 7.53e-5`, `Δm²₃₁ = 2.453e-3`. Maximum at lightest → 0; degenerate limit → `1/3`. **`2/3 = 0.667` is above both maxima.** *A real falsification, and it kills the same claim that killed the 2026-08 charge map.* |
| **the down-quark inverse relation is tunable inside its own error bar** | **CONFIRMED, and understated — see §2.** |

> **The gap is stable, and that is the note's best structural point.** `Q_down` moves **2.3%** between `2 GeV` and `M_Z`, while the **d/u gap is 18.7%**. *An order larger than the drift, so the target is not a renormalisation artefact.* **Confirmed by the invariance result above, which explains *why*: universal running cancels.**

**⚠ One correction, and it was mine.** My first pass used `m_s(M_Z) = 60 MeV` and failed to reproduce the note. **The note's `53.0 MeV` is right** (PDG `93.4 MeV` at `2 GeV` runs down to `~53`), and with it the note's `Q_inv = 0.66748`, `dev = 8.2e-4` reproduces exactly. *The mismatch was my input, not its arithmetic.*

---

## 2. Where I can strengthen its own scepticism: it swept one mass, and there are two

`Q_inv` weights `1/m`, so it is dominated by the **worst-measured** mass. The note swept `m_d` and found the deviation running `0.0008 → 0.0118`. **But `m_s` is also poorly known** (`93.4 +8.6 −3.4 MeV` at `2 GeV`, so roughly `+9%/−4%`). Sweeping both:

| `m_d` \ `m_s` | 50.9 | 53.0 | 57.8 |
|---|---|---|---|
| **2.40** | 0.0082 | 0.0118 | 0.0193 |
| **2.55** | 0.0020 | 0.0055 | 0.0131 |
| **2.67** | 0.0027 | **0.0008** | 0.0084 |
| **2.80** | 0.0076 | 0.0041 | 0.0035 |
| **2.95** | 0.0130 | 0.0095 | 0.0019 |

> **Across the two-dimensional error box the deviation runs `0.0008` to `0.0193`. The reachable band STRADDLES `2/3` rather than landing on it.** *The note's verdict — "a `1e-2` coincidence on a `1e-1`-uncertain mass" — is confirmed and if anything too kind.*

**The contrast it draws is also real.** A **1%** swing on `m_e` moves the lepton `Q` by only `~1e-4`, because the direct relation weights the lightest mass *least*, and `m_e` is known to eleven figures. `dev = 6.2e-6`. **The two relations are not comparable in strength, and the note says so.**

---

## 3. ⚠ NEW PRIOR ART — a second obligation, and it changes the right test

**The note's attribution is correct:** the inverse-Koide-for-quarks idea is **Rivero** and **Kartavtsev**, not an ED finding, and the note says so plainly. *(Web-checked 2026-09-08 under the standing prior-art rule.)*

**But the literature has moved, and further than the note knew.** **`arXiv:2606.10060`, "New sum rules of the Koide type" (June 2026)** reports the down-sector inverse relation in a sharper form: an inverse tuple `m_i^(d) = M^(d)/(w₀+w_i)²` with `Σw_i = 0` and `⅓Σw_i² = w₀²`, **stated to be exact near `Q ≈ 280 TeV` under SM running and within `1σ` of central values throughout** — the mirror of the lepton relation, exact in the ultraviolet rather than the infrared.

> ### This reframes §2's fragility rather than cancelling it.
>
> **If the relation is a high-scale one, the right test is not *does it hit `2/3` at `M_Z`* but *does the RG trajectory pass through `2/3`* — a far more constrained question with much less tuning freedom than my error box suggests.** *My sweep is a fair test of the claim as the note stated it, and not a fair test of the claim as the literature states it.*

**Tier: reported by search, NOT yet read.** **Owed: read `2606.10060` before this is relied on either way.** *Two prior-art obligations now stand on this line — Rousselle `2608.19277` (§4.4.1) and this one — and both postdate nothing in the corpus; both predate the corpus's Koide notes.*

---

## 4. The one place this connects back to ED, and it is the Open item

**§5's lead:** leptons balance **rate** (direct, weights `m`), down-type balances **extent** (inverse, weights `1/m` ~ dwell footprint, `λ ~ ħ/mc`). The note points at `Paper_MassWithoutMass_BindingInertia` §5, which already separates clock rate from mass-from-binding.

> **That is not a separate idea from the tiering's `Open` item. It is the same question from the other side.**
>
> The `Open` item asks **what `b` is for a charged lepton**. The direct/inverse flip is a claim that **the answer differs between free and bound chains** — rate for one, extent for the other. *So if the flip is real, it is not merely a curiosity: it is an **empirical constraint on the `b`-assignment**, which is the one thing that gap currently has none of.*

**That upgrades the `Open` item's shape**, from *missing ingredient* to *missing ingredient with a candidate discriminator*. **It does not upgrade its tier.**

**And the note is right to flag its own confinement story as post-hoc.** *Built after seeing that up-type fits neither relation, rescued by observing that top never hadronises.* **It predicts nothing yet.** Its one virtue, which is real, is that it turns on a **relational** property — does the chain bind before it commits — rather than on a fitted label, and relational properties are the kind of thing ED can speak to. **Tier: `A → position`. Do not cite as a mechanism.**

---

## 5. Net

| | |
|---|---|
| the d/u gap is real, stable, and not an RG artefact | **CONFIRMED** |
| `Q` rises with a family's own hierarchy, so "explain the spread" **is** the flavour hierarchy problem | **CONFIRMED** — no shortcut here, and the note says so |
| `Q_ν = 2/3` | **EXCLUDED by data**, independently reconfirmed |
| the inverse relation splits d from u without a continuous label | **holds**, and it is the only thing found that does |
| its precision at `M_Z` | **weaker than the note said** (§2) — but §3 says `M_Z` may be the wrong place to test it |
| whose result it is | **Rivero / Kartavtsev**, correctly attributed, **plus `2606.10060` unread** |
| what ED would add | a **reason** for the rate/extent flip. **Not built.** |

> **The note's own closing verdict — *"d vs u is not close, and I am reporting that rather than a fit"* — survives the check.** *This is the folder's most useful output precisely because it declines to bank anything, and the one honest gain is that the target is now sharp: a mechanism must explain the **flip**, and must be about **binding** rather than about **charge**.*

**Status: live target, not a result.** Unblocked by §4.4.1's three closures, because it never enters the substrate. **Next real move is reading `2606.10060`, not more probing.**
