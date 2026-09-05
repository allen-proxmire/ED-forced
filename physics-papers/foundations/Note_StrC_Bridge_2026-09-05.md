# The `Str(C)` bridge: it is two statements, not one — and only the second carries content

*Foundations working note, 2026-09-05 (late). Writes the chain-level bridge that arm B, the blind `Σ_C` run and tonight's aggregation work each flagged as unstated. **The useful result is that they were not all flagging the same thing.***

---

## Verdict

$$\boxed{\;\mathrm{Str}(C)(u,t)=\!\!\sum_{K\in\mathcal K(C,u,t)}\!\!\mathrm{Str}_K(u,t),\qquad \mathrm{Coh}(C)(u,t)=\!\!\sum_{K\in\mathcal K(C,u,t)}\!\!\mathrm{Coh}_K(u,t)\;}$$

where `𝒦(C,u,t)` is **the set of channels in which `C` participates at `(u,t)`** — which is P02's participation relation, restricted.

**That statement is definitional and free.** It introduces nothing: P02 already gives the four-tuple `(C,K,u,t)`, and `Paper_001_PreIndividuation` §3.1 already writes the per-tuple content as `b_K^C(u,t)` and `π_K^C(u,t)` with `K ∈ 𝒦`. **The bridge is a plain sum over the index P02 supplies.**

**All the content is in a second statement that the bridge does not contain:** *what `𝒦(C,u,t)` actually holds* for a chain at radius `R` from a mass. **That one is a postulate, it is doing load-bearing work in the gravity arc, and it is currently split between a named condition and an unnamed clause.**

---

## 1. Why this looked like one unstated sentence, and is not

Three audits flagged it. **They flagged different halves.**

| Audit | What it asked for | Half |
|---|---|---|
| **F1 arm B, `D07a`** | *"P12 uses `Str(C)`; `D07` defines `Str_K`. The summation bridge is not stated."* | **the bridge** |
| **Blind `Σ_C` run, GPT gap 1** | *"The framework does not say whether these are sums over channels, weighted sums, graph integrals, maxima, or something else."* | **the bridge** |
| **Blind `Σ_C` run, Claude gap 4** | *"an explicit rule for how `Σ_C` aggregates channel contributions … `∫ Str_K(R′)·μ(R′)dR′` **with a stated measure `μ(R′)`**"* | **the measure** |

**Two asked what the aggregation *is*; one asked what it *runs over*.** Reading all three as one item is what made the bridge look like a single missing sentence with wide reach. **It is one trivial sentence and one substantive postulate, and the substantive one is not new — it is already in the arc under other names.**

## 2. Half one: the bridge, and why it costs nothing

P02's operational content is the four-tuple `(C, K, u, t)`. `Paper_001` §3.1 already carries `b_K^C(u,t)`, `π_K^C(u,t)`, `K ∈ 𝒦`. **So "the channels `C` participates in at `(u,t)`" is a set P02 defines, and summing a per-channel quantity over it is the only reading that types.**

Weighted sums, maxima and graph integrals — GPT's alternatives — are all available in principle, **but none of them is what P04 licenses.** P04 makes bandwidth **additive under channel decomposition**; a quantity built from `b_K` and summed non-additively over channels would contradict the primitive it is built from. **So the plain sum is not merely the natural choice, it is the one P04 permits.**

**Recommended wording, one sentence, for `Paper_087` §P12:**

> *`Coh(C)`, `Str(C)` and `Grad(C)` are the sums of their per-channel counterparts over `𝒦(C,u,t)`, the set of channels in which `C` participates at `(u,t)` (P02); the sum is plain rather than weighted, by P04 additivity.*

## 3. Half two: what `𝒦` contains — this is the postulate

The gravity arc needs a chain at radius `R` to participate in bilocal channels distributed over `[R₀, R]` with density `∝ 1/R′`. **That is a claim about channel membership, and it is currently carried by two separate statements in `Paper_030`:**

- **`P-Bilocal-Count`** (§4.2, named): `N_bilocal = N_horizon = N(R) = 4πR²/ℓ_ED²`. **Already flagged as load-bearing** — the paper says outright that the alternative reading *"would suppress the cross-term far below the Newtonian term everywhere in a galaxy and destroy the deep-MOND result."*
- **The radial density** (§4.3, **unnamed**): *"the bilocal-channel density along the radial direction scales as `1/R` (substrate-graph radial-projection geometry, anchored by P03 spatial-homogeneity)."*

**The second is doing as much work as the first and has no name, no tier row, and one clause of justification.** It is what turns an `R`-independent per-channel strain into a logarithm, and therefore what produces `√(a_N a_0)` rather than nothing.

**Proposed name, for tracking rather than adoption: `P-Radial-Channel-Density`.** *(Named only in this note. Writing it into a paper increments the postulate census — currently baselined at 171 — so that is AP's call, not a note's.)*

## 4. What this settles about the aggregation

**The radial integral is a channel sum, not a path integral** (gravity ledger #79). With the bridge written, that is explicit: `∫ρ_bilocal(R′)dR′` counts the members of `𝒦` in each shell, and summing over `𝒦` is what the bridge says `Str(C)` *is*.

**And the residual I flagged tonight — "it sums channels anchored at other loci" — is answered, though not comfortably.** A channel in `𝒦(C,u,t)` is one `C` participates in *at its own locus*; a **bilocal** channel by construction also carries content from a second source region. **So the far ends are not foreign loci `C` reaches into; they are the second sources feeding channels `C` already touches.** That is coherent.

**What it costs:** the radial density is then a statement about **how many distinct channels a single chain participates in at one locus, as a function of its distance from a mass.** Stated that way it is a strong claim, and *"substrate-graph radial-projection geometry"* is a gesture at a derivation rather than one. **The locality question does not disappear; it relocates into the membership postulate, where it can at least be named.**

## 5. Tier, and what remains open

- **The bridge (§2): definitional, `D` given P02 + P04.** No new commitment.
- **`P-Bilocal-Count`: `P`, already named and flagged**, with its own falsifier `F-BC`.
- **The radial `1/R` density: `P`, unnamed, unflagged, and load-bearing.** **This is the finding.**
- **Still open:** a derivation of the radial density from P03 and P06 rather than a citation to them. `Paper_030` §4.3 gives one clause; nothing else in the corpus addresses it.

**Net: the "missing bridge" three audits flagged is written and costs nothing. The thing standing behind it that nobody flagged — an unnamed postulate fixing channel membership as a function of radius — is what the arc actually rests on.**

---

*Gravity ledger Staleness #80. Companions: `Paper_087` §P02/§P12, `Paper_001_PreIndividuation` §3.1, `Paper_030` §§4.2–4.3.*
