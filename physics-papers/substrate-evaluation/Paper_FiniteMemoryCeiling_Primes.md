# Template, Not Escape: Primes as a Ruler for the Finite-Memory Ceiling of the Event-Density Substrate

**Allen Proxmire**

**June 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (ceiling-location)
**Status:** Publication draft. Empirical ceiling-location test, externally anchored. Standalone; cold-reader accessible. *A proven negative, calibrated against established mathematics.*
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative) — substrate-evaluation

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **ED does not generate, explain, or produce the prime numbers.** The integers — through their factorization structure (the "Factor Skyline," FS) — are used here as an **external ruler** to locate the substrate's information ceiling. This is a **structural / form** parallel only; there is **no content claim** about number theory and no claim that ED has anything to say about why the primes are as they are.
3. **This is a ceiling-*location* test, not a generation test.** The substrate is independently in the finite-reach / finite-memory (zero-entropy) class by its own primitives; the test measures *where* that class's ceiling falls against the ruler. The expected outcome **confirms known hardness** — it is the allowed, predicted result, not a surprise.
4. **The "no" is anchored to external mathematics, not to ED grading itself.** The escape layer's unreachability is read off established results — the **prime number theorem in arithmetic progressions** (the proven, periodic-case core of **Sarnak's Möbius-disjointness** program; §2) and the **sieve parity barrier** (Selberg's parity problem) — not from any ED-internal verdict. ED's role is only to belong to the finite-memory class those results constrain. The operative anchor for the sharp test (Test B, §4.3) is a *theorem*, not Sarnak's open conjecture.
5. **No number theory is claimed or proven.** The paper measures a known computational class against known theorems; it advances no result in number theory. The one genuine experiment (Test B's falsifier) returned the expected negative.
6. **The 1.700-bit template figure is the citable, scale-invariant invariant; the ~0.26-bit "escape" figure is a scale-dependent peak, not a universal constant.**
7. **Finite-N measurement.** The sieve runs to `N = 5×10⁶` (twin primes to `N = 32{,}463`); the asymptotic statements (the best finite-memory Möbius correlator → 0) are read from the N-trend and anchored to the proven theorems, not separately proven at infinity here.

---

## Abstract

Can a finite-memory substrate produce the prime numbers? Event Density's substrate is, by its own primitives (#2–#3), in the **finite-reach / finite-memory** class, and two established results — **Sarnak Möbius-disjointness** and the **sieve parity barrier** — predict precisely what such a class can and cannot reproduce of the prime structure: the **template** layer (the finite-local residue statistics) yes, the **escape** layer (primality itself, the Möbius function, pair correlations) no. Using the integers as an external ruler, we measure both. **The template is reproduced exactly:** the scale-invariant template information `H(dx) − H(dx | n mod 30) = 1.700 bits` is matched, and the least-prime-factor density ladder `P(lpf = p) = (1/p)∏_{q<p}(1 − 1/q)` is reproduced to five decimals. **The escape is provably blocked, three ways.** (A) Conditioning primality on any finite template state `n mod M` leaves an irreducible residual — `H(prime | n mod M) ≈ 0.18–0.29` bits per integer (`≈ 0.58–0.95` bits per *open* position) — the parity barrier expressed in bits. (B, the sharp test) The *optimal* finite-memory correlator with the Möbius function, `C*(N,M) = (1/N)Σ_r |Σ_{n≡r (M)} μ(n)|`, decays toward zero as `N` grows (bounded by `~√(M/N)`) for every fixed `M` — Sarnak-in-this-class confirmed, and the falsifier (a bounded-complexity function correlating with μ) **was not seen**. (C) The twin-prime density requires the Hardy–Littlewood singular series `2C₂ = 1.3203` — a pair-correlation a finite-local template generator does not supply. The mechanism is the **√N activation horizon**: a larger template state `M` needs proportionally larger `N` to resolve, so no *fixed* finite memory ever reaches the escape. The result locates the substrate's ceiling exactly where external mathematics places it — **template yes, escape no, and the *no* is load-bearing.** It is the substrate-evaluation program's only *proven* negative, because it is anchored to theorems outside ED.

---

## 1. Introduction

### 1.1 What this paper does

The standing question for a finite substrate ontology is sharp: *can ED's finite memory produce an infinite-memory object like the primes?* This paper answers it as a **ceiling-location** measurement. ED's substrate is, by primitives #2–#3 (finite reach, finite memory), in a definite computational class. The prime numbers carry two layers of structure — a **template** (finite-local residue statistics, the part a sieve "knows" from `n mod M`) and an **escape** (primality, the Möbius function, pair correlations, the part no finite residue state determines). External mathematics predicts a finite-memory class captures the first and provably not the second. We measure both, using the integers as a calibrated external ruler.

### 1.2 Why this matters

Most substrate-evaluation results are *located-but-open* — an obstruction is identified but not proven insurmountable. This one is different: the wall is a **theorem** (the parity barrier; Möbius orthogonality to periodic sequences), so the "no" is not ED grading its own homework. That makes this the program's **sharpest, most defensible negative** — a clean, externally-certified statement of exactly which structures ED's finite-memory class can and cannot carry, and a concrete in-bits picture of where the ceiling sits.

*Why the primes, and a word of context.* The primes are the cleanest available external ruler for a finite-memory ceiling: their template/escape split is mathematically **sharp** (residue structure vs primality), and the finite-memory class coincides exactly with the **sieve** class whose limits a century of analytic number theory has charted — Eratosthenes' residue sieves, Selberg's parity problem (1949), the Hardy–Littlewood prime-pair heuristics, and the modern Möbius-randomness (Sarnak) program. ED's substrate falls in that class, so those results apply to it directly — which is why the ceiling can be *located by theorem* rather than merely measured.

### 1.3 Arc context

This pairs with the **channel-capacity** result (A1), which found ED's controlled capacity is exactly zero — the same finite-reach ceiling, measured *internally*. Here the *same* ceiling is measured against an **external, math-certified ruler** (Möbius disjointness). Two readings of one property: ED's hard ceiling on long-range / global information, one internal, one externally calibrated.

### 1.4 Regime of validity

This is a **finite-N measurement** (`N ≤ 5×10⁶`; twin primes to `N = 32{,}463`) using **standard sieve data** — the integers' own factorization, **not an ED simulation**. No ED dynamics are run. The ED input is *class membership* (the substrate is finite-memory by primitives #2–#3); the result is therefore a statement about that **class**, not about any specific ED run or observable. The asymptotic statements (the Möbius correlator → 0; the √N horizon) are anchored to the proven theorems (§2) and read from the N-trend, not separately proven at infinity here.

---

## 2. The Substrate Class and the External Anchors

**Substrate class (from primitives).** ED's substrate is finite-reach (primitive #2) and finite-memory / zero-entropy (primitive #3): every determination is a function of a bounded local state. **Explicitly: finite reach + finite local state means every determination is a function of a bounded *residue* state `n mod M` (for some fixed `M`) — which is precisely a periodic, zero-entropy sequence, exactly the class the parity barrier and Sarnak's program constrain.** So the substrate's membership in the sieve / zero-entropy class is not an analogy but an identity. The integers' template structure is exactly such a residue state, so the class *can* represent it; the question is whether it can represent more.

**External anchors (established mathematics — inherited, not ED-derived).**

- **Möbius orthogonality (the proven core of Sarnak's program):** the Möbius function `μ(n)` does not correlate with any sequence produced by a low-complexity (zero-entropy) dynamical system. A finite-memory function of `n mod M` is exactly such a sequence — and, crucially, **the special case this paper needs is not conjectural.** Functions of `n mod M` are *periodic*, and Möbius orthogonality to periodic sequences is a **classical theorem**: `Σ_{n≡r\,(M)} μ(n) = o(N)` for each fixed `M`, by the prime number theorem in arithmetic progressions (Siegel–Walfisz). Sarnak's *conjecture* is the vast generalization to **all** zero-entropy systems; this paper invokes only its already-proven, periodic base case. So the finite-memory negative rests on a **theorem**, not on the open conjecture.
- **The sieve parity barrier (Selberg's parity problem):** sieve methods (finite-local, residue-based) cannot distinguish integers with an even number of prime factors from those with an odd number — they cannot, on their own, isolate the primes. This is the escape layer's irreducibility expressed sieve-theoretically.

These are the *rulers*. The substrate belongs to the class they constrain; the measurements below confirm the class hits the predicted ceiling.

**Ruler (the Factor Skyline).** The integers' factorization statistics, computed by a sieve to `N = 5×10⁶` (`primes_test.py`, numpy). No ED simulation is run; the substrate's *class membership* is the ED input, and the integers supply the external scale against which the class is measured.

**Reproducibility.** The integers `1…N` (`N = 5×10⁶`) are sieved by a simple Eratosthenes sieve recording the least prime factor and the prime-factor count per integer (numpy). Entropies are plug-in (empirical-histogram) estimates of the gap distribution `dx` and the conditional `dx | n mod M`. The Test-B correlator is `C*(N,M) = (1/N)Σ_r |Σ_{n≡r\,(M)} μ(n)|`, the exact optimum over functions of `n mod M`, evaluated at `N/4, N/2, N` for `M ∈ {2, 6, 30, 2310, 30030}`. Twin primes `(p, p+2)` are counted directly and normalized by `N/ln²N`. No randomness and no fitting beyond the entropy histograms. Script: `primes_test.py`.

**No primitive forcing is invoked.**

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Substrate is finite-reach / finite-memory class | **D** | primitives #2–#3 |
| Sarnak Möbius-disjointness; sieve parity barrier | **I (external math)** | established results; the rulers |
| Template information `= 1.700 bits` reproduced | **measured** | §4.1 — scale-invariant invariant |
| lpf density ladder exact to 5 decimals | **measured** | §4.1 |
| Escape floor `H(prime\|n mod M) ≈ 0.18–0.29` bits irreducible | **measured + I-anchored** | §4.2 — parity barrier in bits |
| Best finite-memory μ-correlator `→ 0` (bounded `~√(M/N)`) | **measured + I-anchored** | §4.3 — Sarnak-in-class; falsifier not seen |
| Twin density needs `2C₂ = 1.3203` | **measured** | §4.4 — Hardy–Littlewood singular series |
| Mechanism: √N activation horizon | **D-structural** | §5 — fixed `M` needs growing `N` |
| Template yes / escape no; the "no" is load-bearing | **interpretation** | §7 |
| ED generates the primes | **NOT CLAIMED** | preamble 2 |

All steps P, D, I, measured, structural, interpretation, or explicitly not-claimed. *The negative is I-anchored (external theorems), which is what makes it a proven rather than merely located ceiling.*

---

## 3. The Two Layers: Template and Escape

The prime structure decomposes, for a finite-local observer, into:

- **Template** — what a finite residue state `n mod M` determines: which positions are *definitely composite* (covered by a small prime) and the equidistribution of primes among the *open* (coprime-to-`M`) residues. This is finite-local and representable by the substrate class.
- **Escape** — what no finite residue state determines: *which open positions are actually prime*, the sign of `μ(n)`, and pair correlations (twins). By Dirichlet, primes equidistribute among the open residues, so conditioning on `n mod M` says *nothing beyond base rate* about which open position is prime. That residual is the escape — the parity barrier.

The test measures whether the substrate class reproduces the template (it should) and reaches the escape (it should not).

---

## 4. Results

### 4.1 The template is reproduced exactly

| quantity | measured | scale-invariant target |
|---|---|---|
| `H(dx)` | 2.997 bits | (scale-dependent) |
| `H(dx \| n mod 30)` | 1.297 bits | (scale-dependent) |
| **template information** `H(dx) − H(dx\|n mod 30)` | **1.700 bits** | **1.700 (invariant)** |

The **1.700-bit template invariant is reproduced exactly** — the robust, scale-invariant figure (the absolute entropies are scale-dependent; their difference is not). And the least-prime-factor density ladder falls straight out of finite-local residue structure:

| `p` | empirical | `P(lpf=p) = (1/p)∏_{q<p}(1−1/q)` |
|---|---|---|
| 2 | 0.50000 | 0.50000 |
| 3 | 0.16667 | 0.16667 |
| 5 | 0.06667 | 0.06667 |
| 7 | 0.03810 | 0.03810 |
| 11 | 0.02078 | 0.02078 |
| 13 | 0.01598 | 0.01598 |

Exact to five decimals. **The template layer is fully within the substrate class.**

### 4.2 Test A — the escape floor (the parity barrier in bits)

Conditioning primality on the template state `n mod M` (`M` = primorials):

| `M` | `P(open)` | `H(prime\|n mod M)` | template captured | `H_b(escape per open)` |
|---|---|---|---|---|
| 2 | 0.500 | 0.291 | 0.074 | 0.583 |
| 30 | 0.267 | 0.221 | 0.144 | 0.829 |
| 210 | 0.229 | 0.203 | 0.162 | 0.887 |
| 2310 | 0.208 | 0.191 | 0.174 | 0.920 |
| 30030 | 0.192 | 0.181 | 0.184 | 0.945 |

As `M` grows, finite memory **captures more of the template** (captured bits rise, conditional entropy falls) by resolving the *covered* positions (definitely composite → zero entropy). But it supplies **nothing beyond base rate** about which *open* position is prime — open residues are structurally identical, primes equidistribute among them (Dirichlet). The residual `H(prime | n mod M) ≈ 0.18–0.29` bits/integer (`H_b ≈ 0.58–0.95` bits per *open* position) is the **escape: the parity barrier in bits**, irreducible to any finite template state.

Two clarifications. *On the figure:* the escape entropy is **not a universal constant** — it is the irreducible conditional entropy *at the tested `N` and `M`*, and the meaningful fact is its **persistence** (it does not fall toward zero as `M` and `N` grow), not its particular value. *On why it is irreducible:* **Dirichlet's theorem** guarantees the primes equidistribute among the open (coprime-to-`M`) residues, so those residues are statistically identical — which is exactly why a finite residue state `n mod M` cannot distinguish *which* open position is prime.

### 4.3 Test B — the Möbius correlation (the sharp experiment)

The **optimal** finite-memory correlator with `μ` — the best over *all* functions of `n mod M`:

$$
C^*(N,M) = \frac{1}{N}\sum_r \Big|\sum_{n\equiv r\ (M)} \mu(n)\Big|.
$$

| `M` | `N/4` | `N/2` | `N` | `~√(M/N)` |
|---|---|---|---|---|
| 2 | 0.00018 | 0.00014 | 0.00014 | 0.0006 |
| 30 | 0.00329 | 0.00192 | 0.00118 | 0.0024 |
| 2310 | 0.03241 | 0.02225 | 0.01523 | 0.0215 |
| 30030 | 0.10033 | 0.07101 | 0.05021 | 0.0775 |

For **every fixed `M`**, the best finite-memory correlator **decays toward 0 as `N` grows** (≈ halving as `N` doubles; bounded by `~√(M/N)`). Even the *optimal* function of the template state cannot correlate with `μ` asymptotically. For each fixed `M` this decay is a **classical theorem** — `Σ_{n≡r\,(M)} μ(n) = o(N)` by the prime number theorem in arithmetic progressions — so the experiment is *confirming a proven result and quantifying its `√(M/N)` rate*, not testing Sarnak's open conjecture. This is nonetheless the genuine experiment of the paper: a bounded-complexity, finite-memory function with `C*` bounded away from zero would be a real discovery (it would refute Möbius orthogonality in this class). **It was not seen.** (A companion probe re-uses this correlator to test a QM-amplitude reading of the escape; see §4.5. The one hinge that probe could not decide — irreducible bilinearity — is resolved (heuristic-structural) to the form-only limit in `OPEN_QUESTION_FS_TB_QM_AMP_02_Bilinearity.md` §9 — no single-amplitude `|A|²`; the twin escape is a two-particle mixed-state object.) *(a fork document in the working repo — no longer in this repo)*

### 4.4 Test C — twin density needs a correlation the template does not supply

The template (lpf ladder, §4.1) is reproduced exactly. The **escape** — a correlation beyond the template — shows up in the twin-prime density (twins `(p, p+2)` to `N = 32{,}463`):

- `π₂ / (N/ln²N) = 1.545` — pure independence/template predicts **1.000** and *misses*.
- `π₂ / (2C₂ · N/ln²N) = 1.170` — the Hardy–Littlewood singular series **`2C₂ = 1.3203`** is the dominant correction (the residual 1.17 is the crude `N/ln²N` versus the integral `Li₂(N)`, ~+13% at this `N`).

The twin density carries the **`2C₂` pair-correlation** — an escape structure a finite-local template generator does not supply. (`2C₂ = 1.3203` is **not derived here**; it is the known Hardy–Littlewood twin-prime singular-series constant, used as the external yardstick. The point is only that the measured twin density *needs* it — i.e. carries a pair-correlation the template lacks.)

### 4.5 Tested analogy with documented limit — the QM-amplitude reading of the escape

A companion memo (`Memo_QM_Amplitude_PrimeEscape.md`, Appendix A; original `Twin Bertrand/papers/FS_TB_QM_Amplitude_Memo.md`) reads the template/escape split as the probability/amplitude (L²) structure of quantum mechanics: the template is the accessible `|ψ|²`-level density, the escape is the withheld amplitude/phase (the `√x` zero-waves of `M(x) = Σμ(n) = Σ_ρ x^ρ/(ρζ'(ρ))`, whose phase is the Möbius sign). The hinge — *does the twin escape factor as `|A|²` with phase equal to the parity-barrier-withheld Möbius sign?* — was probed at `N = 5×10⁶` (`Twin Bertrand/scripts/pg_qm_amplitude_probe.py`) against the pre-registered clean-negative criteria. The result is an **honest non-negative on the decidable axes, with the predicted obstruction isolated**: *(working-repo artifact: lives under `event-density`/`ed-lab`, not in this repo)* *(working-repo artifact — no longer in this repo; lives under `event-density`/`ed-lab`)*

- **(i) trivial-factorization trap — non-negative.** The detrended twin fluctuation (111 sign changes) and the Mertens amplitude `M(x)` (190 sign changes; `M(N)/√N = −0.317`, bounded) both genuinely change sign. The escape is a sign-bearing *phase* object, not a positive density trivially equal to `|√f|²`.
- **(iii) finite-memory phase — non-negative.** Re-using the §4.3 optimal correlator, `C*(N′,M)` vanishes at least as fast as the `√(M/N)` random-walk bound (log-log decay slopes −0.73 / −0.62 / −0.53 for `M = 30 / 210 / 2310`). The Möbius phase is **not** finite-memory, so the parity-barrier↔hidden-phase identification survives (it is *not* refuted by a finite-memory predictor).
- **(ii) irreducible bilinearity — RESOLVED (heuristic-structural) to the form-only limit.** An analytic argument (fork `OPEN_QUESTION_FS_TB_QM_AMP_02_Bilinearity.md` §9) settles the single-amplitude question **NEGATIVE**: in the heuristic explicit-formula expansion of `Σ Λ(n)Λ(n+2)`, the zero-*pair* kernel carries the Hilbert coupling `1/(ρ+ρ'−1)` — the classical **infinite-rank, non-separable** positive operator — so the twin escape admits **no single-amplitude `|A|²` (no pure-state square)**. The probe's near-zero correlations (`corr(Δ₂, M) ≈ 0.06`, `corr(Δ₂, ψ−x) ≈ −0.03`) are consistent with this. The QM analogy therefore holds **form-only** at the single-amplitude level. The correct reading is **not** "two correlated particles" but **one object sampled twice**: a single non-separable pattern `ρ(ρ,ρ') ∝ N^{ρ+ρ'}/(ρ+ρ'−1)` read at offset 0 and offset 2 (Schmidt decomposition = one shared spectrum at two sampling sites), not a pure single-particle `|ψ|²`. **Load-bearing consequence:** a finite-memory (sieve / finite-local) observer cannot individuate a twin into two independent primality facts — so the **parity barrier is what keeps the twin one un-resolved pattern** (this arc's "unresolved individuation" reading of entanglement, §6 / Papers 063–072). Established: non-separability (one object). **Open successor:** whether that one object is *quantum*-entangled (its Schmidt spectrum lies outside the Bell–Tsirelson / classical polytope) or merely classically correlated. Routed to the fork's Pad A; the rigorous kernel (Bogomolny–Keating form factor) remains open. **Information-theoretic face:** the two offsets are correlated but primality is unchooseable, so no signal can pass — *correlation without control*, the same way entanglement coexists with no-signaling (rooted in CRT independence: the sieve is a product `∏(1−1/p)` of independent factors, none of which sees the product). This is a **consistency, not a result** — the barrier's informational nature is already standard (Sarnak Möbius-randomness; the in-bits escape of §4.2–§4.3) — and **not a discriminator**: no-signaling holds for quantum *or* classical correlation, so the Bell–Tsirelson test stays the only way to settle the open successor. *(a fork document in the working repo — no longer in this repo)*

**Net.** The QM-amplitude analogy **survives on every front this probe can decide**; the mechanism question reduces to a single conjectural point — whether the escape admits a single-amplitude versus an irreducibly-bilinear (pairs-of-zeros) representation. **Form, not mechanism**; no number theory is claimed (consistent with Preamble §§2, 5). Tracked as `OPEN_QUESTION_FS_TB_QM_AMP_01`; verdict file `results/qm_amplitude_probe.md` in the Twin Bertrand repo. *(working-repo artifact: lives under `event-density`/`ed-lab`, not in this repo)* *(working-repo artifact — no longer in this repo; lives under `event-density`/`ed-lab`)*

---

## 5. The Mechanism: the √N Activation Horizon

Why does no *fixed* finite memory ever reach the escape? Because the template state that would resolve more of the structure grows with the scale it must resolve. Test B makes this quantitative: a larger `M` *does* correlate with `μ` at small `N` (the `√(M/N)` envelope), but that correlation **washes out** as `N` grows — a *fixed* `M` with growing `N` goes to zero, and capturing more requires `M` to grow proportionally with `N`. The required memory grows like `√N`. So a finite-memory substrate is always, eventually, beneath the escape: it can chase the template arbitrarily far, but the escape recedes at exactly the rate that keeps it out of finite reach. This is the **activation horizon**, and it is the substrate-level shadow of the parity barrier. The `√N` scaling is not coincidental: it is the same square-root-cancellation scaling that governs the **large-sieve inequality** and the expected size of character sums — the quantitative form of "finite memory buys only `√N` of resolution."

---

## 6. Relation to the Channel-Capacity Result and the Program

The channel-capacity result (A1) found ED's controlled capacity is exactly zero — the finite-reach ceiling measured *inside* ED, against ED's own observables. This paper measures the *same* finite-reach / finite-memory ceiling against an **external, math-certified ruler** (Möbius disjointness, the parity barrier). Two readings of one property — ED's hard ceiling on long-range / global information — one internal, one externally calibrated. Together they answer the standing question, *can ED finite-memory produce an infinite-memory system like the primes?*: **the template, yes; the escape, no — and the *no* is load-bearing.**

This negative is also of a *different kind* from the program's others. Most are coarse-graining walls (the continuum / metric flesh) — located but not proven insurmountable. This one is a **finite-memory / uncomputability** wall, anchored to a theorem, hence **proven**. It is the program's only proven negative, and it owes that status entirely to having an *external* ruler.

---

## 7. Interpretation

**Finite memory saturates the template and fails the escape.** The substrate class reproduces the prime template exactly (the 1.700-bit invariant; the lpf ladder) and provably cannot reproduce the escape (per-open-position primality entropy irreducible; the best finite-memory Möbius correlator → 0; the twin density's `2C₂` pair-correlation unavailable). The integers, used as a ruler, locate the substrate's ceiling **precisely where Sarnak disjointness and the sieve parity barrier place it.**

The *no* is the load-bearing content. It is not a failure of ED — ED is not in the business of generating primes — but a clean, externally-certified **measurement of the class ED belongs to**. And it sharpens the program's overall shape: where the continuum / metric results are "form yes, flesh-as-coarse-grained-shadow," this is "template yes, escape **provably** no" — the one place the wall is a theorem rather than an open obstruction.

---

## 8. Limitations (honest)

- **Finite N.** The sieve runs to `5×10⁶` (twins to `32{,}463`); the asymptotic claims are read from the N-trend and anchored to the proven theorems, not separately proven at infinity.
- **Ruler, not generator.** No ED simulation is run; the ED input is *class membership* (finite-memory), and the integers supply the external scale. The result is about the class, not about a specific ED dynamical run.
- **The escape figure is scale-dependent.** The citable invariant is the 1.700-bit template; the ~0.26-bit per-integer escape peak is scale-dependent, not a universal constant.

---

## 9. Falsification Criteria

### 9.1 A finite-memory Möbius correlator (the genuine falsifier)

**Falsifier sentence:** *A bounded-complexity, ED-definable function `f(n)` (a function of a finite local state) with `(1/N)Σ μ(n)f(n)` bounded away from zero as `N → ∞` would refute Sarnak-in-this-class — a real mathematical discovery, and a refutation of §4.3. It was searched for (over all functions of `n mod M`) and not found.*

### 9.2 The template not reproduced

**Falsifier sentence:** *A finite-local computation failing to reproduce the 1.700-bit template invariant or the lpf density ladder would falsify §4.1 (the substrate class would then not even capture the template).*

### 9.3 The escape captured by finite memory

**Falsifier sentence:** *A fixed finite template state `M` for which `H(prime | n mod M)` falls toward zero as `N` grows — i.e. finite memory resolving primality beyond base rate among open residues — would falsify §4.2 and the parity-barrier anchoring.*

### 9.4 The activation horizon not √N

**Falsifier sentence:** *A finite-memory correlator whose useful `M` does not have to grow with `N` (a fixed `M` retaining correlation with `μ` as `N → ∞`) would falsify the √N activation-horizon mechanism (§5).*

---

## 10. Position Statement

Using the integers as an external ruler, ED's **finite-memory substrate class reproduces the prime template exactly and provably cannot reproduce the escape.** The 1.700-bit template invariant and the lpf ladder are matched; the primality entropy per open position is irreducible; the optimal finite-memory Möbius correlator decays to zero; the twin density requires a pair-correlation the template does not supply; and the √N activation horizon is the mechanism.

**What this paper claims.** ED's finite-memory class hits the parity-barrier ceiling exactly where external mathematics (Sarnak disjointness; the sieve parity barrier) says it must — template captured, escape blocked. Because the wall is a theorem, this is the substrate-evaluation program's only *proven* negative.

**What this paper does not claim.** ED does not generate or explain the primes; the integers are a ruler, not a target. No number theory is advanced; the structural parallel carries no content claim. The asymptotic statements are anchored to the proven theorems and read from finite-N trends, not separately proven here.

**Series context.** The externally-calibrated companion to the channel-capacity result (A1): one finite-reach ceiling, measured internally there and against a math-certified ruler here. The standing question — can ED's finite memory produce an infinite-memory object like the primes? — is answered: **the template, yes; the escape, no; and the *no* is load-bearing.**

---

## Appendix — Artifacts and Glossary

### Artifacts

- `Primes_Arc/primes_test.py` — sieve to `N = 5×10⁶` (numpy); template-information, Test A (escape floor), Test B (optimal mod-M Möbius correlator), Test C (lpf ladder; twin density).

### Glossary

- **Open residues.** The residue classes `r mod M` coprime to `M` — the positions a sieve to level `M` leaves *uncovered*, among which the primes above `M` must lie and (by Dirichlet) equidistribute.
- **Template layer.** The finite-local residue structure of the integers (`n mod M`): coverage by small primes + equidistribution of primes among open residues. Within the finite-memory class.
- **Escape layer.** Primality itself, the Möbius function, pair correlations — the structure no finite residue state determines. The parity barrier.
- **Template information (1.700 bits).** The scale-invariant `H(dx) − H(dx | n mod 30)`; reproduced exactly. The citable invariant.
- **Parity barrier.** The sieve-theoretic obstruction that finite-local methods cannot isolate the primes (cannot resolve the parity of the number of prime factors).
- **Sarnak disjointness.** Möbius does not correlate with any zero-entropy (low-complexity) sequence — including any finite-memory function of `n mod M`.
- **Activation horizon (√N).** The required template memory grows like `√N`, so no fixed finite memory ever reaches the escape — the substrate-level mechanism of the ceiling.
- **`2C₂ = 1.3203`.** The Hardy–Littlewood twin-prime singular series; the escape pair-correlation the template does not supply.

### Reader map and open work

*Intuition — the parity barrier in one line.* Finite memory can classify residue classes but cannot see the **parity of the number of prime factors**; isolating the primes requires exactly that parity, which no finite residue state encodes. That is the whole obstruction.

**Where to look next.**
- *The internal reading of the same ceiling (channel capacity = 0):* the A1 result.
- *The coarse-graining wall (the continuum / PDE shadow):* the Continuum paper.
- *The gravity arc (the same finite-reach character):* GR-II.

**Open work** (declared): test other arithmetic rulers (the Liouville function `λ`, the divisor function `d(n)`) for the same template/escape split; test ED-*generated* sequences against the Möbius correlator directly (rather than via the class argument); push `N` higher; and test adaptive `M(N)` scaling against the √N horizon explicitly.

---

**End of Paper (Finite-Memory Ceiling).**

*Substrate-evaluation arc. ED's finite-memory class reproduces the prime template exactly (1.700-bit invariant; lpf ladder) and provably fails the escape (primality entropy irreducible; optimal Möbius correlator → 0; twin density needs 2C₂), located by Sarnak disjointness + the parity barrier via the √N activation horizon. ED does not generate the primes — they are a ruler for the substrate's ceiling. The program's only proven negative, because it is anchored to a theorem.*
