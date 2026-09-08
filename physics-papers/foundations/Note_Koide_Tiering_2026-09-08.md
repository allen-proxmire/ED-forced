# Tiering `M_eff = 1/Q` — and the two ED readings of Koide are incompatible

**2026-09-08.** AP: *tier `M_eff = 1/Q` first and let the rest follow from it.* **The tiering does not complete, and the reason is the result.**

---

## 1. The finding, before any tier

The corpus now holds **two** ED readings of Koide's `Q`, written three days apart. **They assign `b` differently, and they cannot both hold.**

| reading | assignment | what it gives | check |
|---|---|---|---|
| `foundations/Note_Koide_In_StrCoh_2026-09-05` | `P_i = √m_i`, so **`b = m`** | `Q = Str/(Str + Coh)` | **0.66666051 ✓** |
| `theory/Koide_Hierarchy/koide_is_Meff_check.py` | **`b = √m`** | `M_eff = 1/Q` | **1.50001385 ✓** |

**Each is exact under its own substitution. Neither survives the other's.**

- Under `b = m`, `M_eff = (Σm)²/(Σm²) = ` **1.119**, not `1/Q = 1.500`.
- Under `b = √m`, `Str = Σb = ` **53.1 MeV**, which is not the sum of the lepton masses, so `Str/(Str+Coh)` is no longer Koide's `Q`.

> **Both hold only if `m = 1`.** They are **two different substitutions, each chosen so that one ED quantity matches a known number** — not, as an earlier write-up of mine claimed, *"the same algebra reached twice."* **That claim is withdrawn; it was made without checking the two `b`-assignments against each other.**

---

## 2. Why the tiering does not complete

**The load-bearing content of `M_eff = 1/Q` is not the algebra. It is the identification `b = √m`.** Given that substitution the equality is arithmetic, provable in one line, and carries no physics.

**And that identification is unlicensed.** Three separate facts:

1. **No `b ↔ mass` map exists anywhere in the corpus.** A search of `foundations/` and `substrate-evaluation/` returns none.
2. **The corpus has a measured result pointing the other way.** `Paper_MassWithoutMass_BindingInertia`: *"the commitment rate and mass are **different phenomena** … mass is a separate thing that comes from **binding**."* Bandwidth-rate was tested against mass **and separated from it**.
3. **The two readings contradict each other about what `b` is** (§1), so at most one can ever be right, and nothing currently selects between them.

**Against the tier grammar, then:**

| tier | verdict |
|---|---|
| **Derived** — *forced from the 13 primitives, no paper-specific postulate* | **No.** Nothing forces `b = √m`. |
| **D-via-I** — *form derived by composing inherited pieces* | **No.** The form is an identity, not a composition; and the substitution is not an inherited piece, it is a choice. |
| **Grounded** — *form-forced GIVEN a stated input or declared postulate* | **No** — and this is the near miss. Grounded requires the input to be **stated and declared**. Here it is **unstated**, and there are **two mutually exclusive candidates in play**. Tiering it Grounded would name a postulate the corpus has not adopted. |
| **Measured** | No — no substrate run. |
| **Selected/Inherited** | No — `Q` is not a value ED selected; it is a number ED restated. |

> ## Verdict: **it does not receive a claim tier, because it is not yet a claim about ED.**
>
> **It is an algebraic identity conditional on an unlicensed substitution, and a competing note uses a different one.** *The formula is correct. What it is a formula **about** is undetermined.*

---

## 2b. And there is a SECOND blocker, already in the corpus, prior to the first

**The `b`-assignment problem is not the only thing wrong, and it is not the deepest thing wrong.** `theory/Koide_Hierarchy/GENERATIONS_LICENCE_2026-09-07.md` — written the night before, in the same folder, and **never connected to the 09-05 note** — closes the route by a different argument entirely.

**Both readings treat the three charged leptons as three channels of ONE chain.** `Str_K`, `Coh_K` and `M_eff` are all sums over `𝒦(C,u,t)`, the channel set **of a single chain**. But:

> `primitives/concepts/chain.md` §1 (**verified at source 2026-09-08**): *“The chain's identity is encoded **entirely in the update rule**. … **Two chains with different update rules are different kinds of chains** even if they traverse overlapping regions.”*

> `arcs/arc-Q/generations_and_mixing.md` §3.1: **generation = distinct rule-type.**

**Rule-type is the update rule; the update rule *is* chain identity. So three generations are three different KINDS OF CHAIN, and no per-chain functional can range over them.** *Electron, muon and tau are not three channels of one thing. They are three things.*

> ### This blocker is **prior** to the `b` question, and it is worse.
>
> **The `b`-assignment gap says: we do not yet know what to put in the sum. This says: there is no sum.** *A licensed `b` for a charged lepton — the `Open` item below — would not rescue either reading, because the object being summed over does not exist as a single chain's channel set.* **`GENERATIONS_LICENCE` §4 already records “the `Σ_C = −½Str` opening — DEAD — `Σ_C` is per-chain and does not apply.” That verdict was written about the 09-05 note's route and never reached it. It applies to `M_eff = 1/Q` identically, and for the same reason.**

**Two independent blockers, then, and they fail at different depths:**

| | what it says | would a licensed `b` fix it? |
|---|---|---|
| **the `b` gap** (§2) | nothing licenses `b = m` or `b = √m`, and they contradict each other | — |
| **chain identity** (§2b) | there is no single chain whose channels are the three leptons | **No.** |

*That the second blocker sat unconnected in a sibling folder for a day is itself the drift-bug shape `CLAUDE.md` names — and it is why the folder was moved into version control before being tiered.*

---

## 3. What is real, and it is an `Open` item

**The tierable content is the gap the exercise exposed:**

> **OPEN — assign `b` for a charged lepton.** ED has no licensed map from a substrate bandwidth to a fermion mass, has a measured result separating bandwidth-rate from mass, and now carries two incompatible ad-hoc assignments introduced to reach Koide. **Until one is licensed from the primitives or declared as a postulate, no ED reading of Koide is available — including both current ones.**

**That is a stronger and more useful statement than either reading, and it is worth carrying** — the gap is real, it is an instance of Target #16, and it is the simplest object #16 could be tried on. **But §2b means it is NOT sufficient:** closing it would license the ingredients and still leave no chain to put them in. *A route to Koide needs the chain-identity blocker cleared first, and that is arc Q's `G4` door — gated on Q.7/Q.8 vacuum structure, not on flavour.*

---

## 4. What this does *not* say

**It does not refute a Koide/ED connection in principle.** It says both routes on the table fail, at two depths, and that the deeper failure (§2b) is not about Koide at all — it is arc Q's chain-identity closure, whose one live door (`G4`, vacuum-anchored differentiation) is **deferred, not refuted**, and gated on Q.7/Q.8. *A licensed `b` alone would not revive either reading.*

**It does not touch the session's other results.** The **spread reframe** stands — `Q` is a hierarchy measure, invariant under common rescaling, and the d/u gap is an order larger than scale drift, so the target is structural. The **Cauchy–Schwarz observation** stands as an observation, with its own refutation attached (`ED inherits the Tsirelson number and inherits the masses, so connecting two inherited numbers transmits nothing`). **The prior-art obligation on Rousselle 2608.19277 is untouched and still owed.**

**And arc M's verdict is unchanged.** Mass relations remain empirical. *What §4 of the 2026-09-05 note flagged for re-examination — arc M's stated **reason**, that "ED produces dichotomies, not continuous numerical relationships" — is not settled here either way, because the `M_eff` route that appeared to challenge it turns out to rest on an unlicensed substitution.*

---

## 5. The caution this is an instance of

`Note_Koide_In_StrCoh_2026-09-05` names it itself:

> ***"`Paper_030`'s own history is the caution here — a relation restated in substrate language read as a result for months before the prior art was checked."***

**This is the same failure caught at tiering instead of after months** — and caught only because tiering forced the two `b`-assignments to be written next to each other. *An earlier version of this write-up called them convergent. Tiering is what found otherwise, which is what the tier grammar is for.*
