# Gravity as Horizon Equipartition: How Event Density Grounds Padmanabhan's Count

**Allen Proxmire**

**July 2026**

---

## Preamble — what this article does NOT claim

1. **No new forced derivation, and — this time — not even a new ED derivation.** The equipartition construction this article discusses *already exists inside ED* as **Theorem T19** (`Substrate_Gravity_Foundations`, April 2026): the holographic participation count, the equipartition step, the Unruh-analog inversion, and the recovery of `G = c³ℓ_P²/ℏ`. This article's job is to **recognize that T19 is Padmanabhan's holographic-equipartition move in ED's own language**, to state precisely the one thing ED genuinely adds over Padmanabhan, and to mark — honestly — the two things ED does *not* add.
2. **ED's results are conditional derivations from thirteen posited primitives**, never derivations from nothing, and the framework is not experimentally confirmed.
3. **What ED grounds here is the *count*, not the *equipartition rule*.** Both Padmanabhan and ED's T19 *posit* that each surface degree of freedom carries `½T`. ED supplies a substrate reason for the *number* of degrees of freedom (the area law), not yet for the equipartition principle itself. That distinction is the spine of §5 and is not blurred anywhere.
4. **T19 reaches Newton, not the full Einstein equation.** Padmanabhan's own route to the full field equation invokes local Lorentz invariance, which ED's khronometric class modifies; the honest wall is the same one the companion Jacobson paper hit, and it is stated in §6, not glossed.
5. **T19's April-2026 framing ("structurally complete… final… parameter-free") is not inherited.** This article uses T19's *derivation* as the asset and re-tiers its claims against the current, more conservative corpus posture.

---

## 1. What Event Density is, in one page

Event Density is an account of physics built on a **discrete, relational substrate**: a participation graph in which chains participate in channels, each channel carrying a **bandwidth** `b ≥ 0` and a phase. There is one process primitive: **commitment** (P11), the irreversible act by which an uncommitted participation becomes a definite, recorded fact. The arrow of time is not a boundary condition layered on reversible laws; it *is* this act, written into the law. Gravity in ED is emergent: the metric is the *reading* of the bandwidth field's connectivity (`g ~ 1/b`, `Paper_GR-I`), and the field equation is the steady state of a dynamical bandwidth rule (`Paper_GR-III`). ED's gravitational class is **khronometric**: Einstein's two tensor modes plus one scalar, the *khronon*, the arrow made dynamical (`Paper_GR-II`).

This article is the second in the *microscopic-completions* family. The first (`Paper_GravityAsEquationOfState`) grounds Jacobson's 1995 derivation. This one does the same service for Padmanabhan's equipartition picture, and finds — usefully — that ED had already walked the road without knowing whose road it was.

## 2. Padmanabhan's move, and the input he left open

In 2009 Padmanabhan ("Equipartition of energy in the horizon degrees of freedom and the emergence of gravity," arXiv:0912.3165) reread his earlier relation `S = E/2T` between horizon entropy, active gravitational mass, and temperature as a **law of equipartition**:

$$ E = \tfrac{1}{2}\, n\, k_B T, \qquad n = \frac{\Delta A}{L_P^2}. $$

The energy of the active gravitational mass is equipartitioned over `n` microscopic horizon degrees of freedom, one batch of `½T` per Planck area. From this, with the Rindler temperature `k_B T = ℏκ/2πc`, Newton's law drops out directly (his eq. 9):

$$ \kappa = \frac{GM}{r^2} = \left(\frac{A_P\, c^3}{ℏ}\right)\frac{M}{r^2}, $$

so that **the Planck area `A_P = L_P²` is what fixes the gravitational coupling** — take `ℏ → 0` with the grain finite and `G` diverges, which is Padmanabhan's way of saying gravity is intrinsically a quantum-of-area phenomenon.

But the whole construction rests on an input Padmanabhan does not derive and does not pretend to. The count `n = A/L_P²` is introduced by hypothesis:

> *"Suppose we have any formalism of quantum gravity in which there is a minimum quantum of length or area, of the order of `L_P² ≡ Gℏ/c³`. Given this result, a patch of horizon having an area `A` can be divided into `n = A/(c₁ L_P²)` microscopic cells…"*

The numerical factor `c₁` is then set to 1 by hand to recover `S = A/4L_P²`. So the load-bearing input — *there is one degree of freedom per Planck area on the horizon, and the count is the area* — is assumed, awaiting "any formalism of quantum gravity" to supply it. That is the opening this article walks through, and it is the *same* opening Jacobson left when he called his entropy density `η` "undetermined… given a microscopic theory of spacetime structure." Padmanabhan's `n` and Jacobson's `η` are the same grain seen twice: the count is four times the entropy, `n = 4S`, and `n/A = 4η = 1/ℓ_P²`.

## 3. Event Density already made this move — it is Theorem T19

The striking finding, from reading the corpus before writing, is that ED did not *need* to construct a grounding for Padmanabhan. It already had one, registered as **Theorem T19** (`Substrate_Gravity_Foundations` §3) and apparently arrived at independently. The correspondence is line for line:

| Padmanabhan 0912.3165 | ED Theorem T19 (§3) |
|---|---|
| horizon d.o.f. count `n = ΔA/L_P²` | participation d.o.f. `N_R = 4πR²/ℓ_ED²` |
| equipartition `E = ½ n k_B T`, with `E = Mc²` | `½ N_R k_B T_R = M c²` |
| Rindler temperature `k_B T = ℏκ/2πc` | Unruh-analog `T_R = ℏa/(2π k_B c)` |
| `κ = GM/r²`, `G = A_P c³/ℏ` (eq. 9) | `a = M c³ ℓ_ED²/(R² ℏ)`, `G = c³ ℓ_P²/ℏ` |

Same holographic 2-sphere, same equipartition of the active mass over surface degrees of freedom, same Unruh inversion, same cancellation of `2π`, same Newton's constant. T19 *is* Padmanabhan's "emergence of gravity from horizon equipartition," expressed in participation-channel language, with no citation to his paper. Recognizing this is what closes the target: the microscopic-completions program listed Padmanabhan's equipartition as its first open target, and the honest resolution is that **ED's answer to it was already on the books.** The contribution of this article is the recognition and the attribution, plus the two clarifications that follow.

## 4. What ED genuinely adds: it grounds the count

Padmanabhan supplies the count `n = A/L_P²` by positing "any formalism of quantum gravity" with a minimum area. ED supplies a *specific substrate reason* for it, and this is the one place ED does more than restate the move.

The count of surface degrees of freedom is, in ED, the count of **severed cross-chain participation edges straddling the causal cut**:

- **The cut is real and capacity-zero.** A1 (`Paper_CommonCauseNotChannel_A1`) establishes that controlled channel capacity across a decoupling surface is *exactly* zero — the horizon is a genuine one-sided participation boundary, not a soft gradient. This is the substrate object Padmanabhan's "horizon degrees of freedom" are degrees of freedom *of*.
- **The area-*scaling* is measured, not posited — conditional on an assumed emergent geometry.** The severed count scales as the boundary, not the bulk: `Paper_AreaLawIsTheEdgeCount` measures the straddling-edge count growing as `r^{2.02}` (area law), and `Paper_GR-III` §7.4 independently measures the horizon severed-count scaling as the perimeter `r_h^{0.96}`. The honesty pin those papers carry travels here: the scaling is measured *given* an assumed 3D embedding, and deriving the emergent geometry and its length scale from the raw participation graph is the still-open curvature-emergence program. So where Padmanabhan *posits* the area law by fiat, ED *measures its exponent* (boundary, not bulk) from weaker inputs. That reduces the assumption; it does not eliminate it.
- **The per-cell size is the grain — value-inherited, not free-fit.** One degree of freedom per `ℓ_P²`: P08 posits that a grain *exists*; its *value* `ℓ_ED = ℓ_P` is fixed by Newton-matching (T19 §3.3), not by P08 alone. The `1/4` coefficient that turns the count into the entropy is a separate ED result (`BH_EntropyCoefficient_FromEventCounting`), not a hand-set `c₁` — but it, and the grain value, sit at the value-inherited tier, the same one Padmanabhan's `L_P` and Jacobson's `l_c` occupy.

So the flagged input decomposes. The **boundary-not-bulk scaling** (exponent 2, not 3) is *measured*; the **per-cell size** and the **`1/4` normalization** stay *posited / inherited*. ED therefore *reduces* Padmanabhan's assumption rather than eliminating it: it earns the area-*scaling* from weaker inputs (grain plus an assumed geometry), and leaves the grain value and coefficient at the value-inherited tier he and Jacobson also sit at. This is the genuine fill, and it is narrow: even at its strongest, ED grounds *the number of things being equipartitioned* — its scaling — not the equipartition rule that acts on them. That is §5.

## 5. What ED does NOT add: equipartition itself is posited by both

Here is the honest limit, stated plainly because the whole family depends on not overselling. **T19 posits equipartition exactly as Padmanabhan does.** Its own words: *"A substrate-level equipartition principle distributes the local mass-energy across these participation degrees of freedom."* The `½T` per channel is an input in T19 no less than in 0912.3165. ED grounds the *count* the `½T` is applied to; it does not, at present, derive *why each severed channel carries `½T`.*

This is a real open step, not a formality, and there is a plausible route to it worth naming. ED already reproduces the near-horizon **Rindler mode structure** to obtain `T = κ/2π` (`BH_Thermal2Pi_FromNearHorizonRindler`): the vacuum bandwidth profile has Rindler form at the horizon, and smoothness fixes the temperature. Equipartition — `½T` per quadratic mode in thermal equilibrium — may fall out of that *same* mode analysis, because Unruh thermality already *is* the statement that each Rindler mode is thermally populated. If it does, the result is sharper than "ED derives equipartition":

> **`½T`-per-channel and `T = κ/2π` would be one near-horizon fact, not two independent assumptions** — collapsing two of the equipartition picture's inputs into a single grounded one.

The honest risk is that this stays *inherited from the Rindler structure* rather than derived from something deeper, in which case ED shows the two inputs are one fact but does not reduce the fact further. Even that is a gain. **This is the standing open lead of this paper**, and it is deferred to its own step, on the same discipline the companion paper used for the continuation-free `2π`.

## 6. Newton, not Einstein: the same khronometric wall

Padmanabhan does not stop at Newton. Applying equipartition on arbitrary volumes (his eq. 12) he reaches `R_{ab} u^a u^b = 8πG \bar{T}_{ab} u^a u^b`, the `00`-component of the Einstein equation, and then promotes it to the full covariant equation by **"demanding local Lorentz invariance."** That final demand is exactly where ED parts company, and it is the *same* wall the Jacobson paper hit: ED's gravitational class is khronometric, with a preferred foliation, so it does not simply grant local Lorentz invariance as a free input.

T19, correspondingly, reaches **Newton's law** and stops there — it derives `a = GM/R²`, not the covariant field equation. This is not a defect to hide; it is the consistent ED position across both microscopic-completions papers:

- The equipartition/thermodynamic route grounds the **Newtonian / static** face of gravity cleanly, from a substrate count.
- The step to the **full covariant Einstein equation** runs through a Lorentz-invariance assumption that ED's khronon modifies at order `λ_local ~ ρ_event/ρ_Planck`, seventy orders of magnitude below current bounds (`Paper_GR-IV`).

The companion Jacobson paper argues that this khronometric departure is *benign* at a local Rindler horizon: both ED cones are luminal, `α₂ = 0`, the causal structure is the standard light cone, and the Unruh temperature survives. That argument is a fact about **ED's cone structure, not about which thermodynamic route is run**, so it is route-independent. Since Padmanabhan reaches full Einstein by the *same* "demand local Lorentz invariance" step Jacobson uses, the same benign verdict would, at the companion paper's stated tier, license the equipartition covariant step too. Why this paper still stops at Newton is narrower and purely factual: **T19 as written never attempted the covariant step** — it derived `a = GM/R²` and stopped. So the honest statement is *not* that the wall is more open for equipartition than for Jacobson (it is the same wall, with the same luminal-cone verdict available); it is that **T19 grounds Newton from a substrate count, and the covariant extension by equipartition has simply not been carried out in ED yet, though the companion's luminal-cone argument says it should go through at the stated tier.**

## 7. The grain fixes G three ways

One convergence is worth stating for its own sake. Newton's constant `G = c³ℓ_P²/ℏ` is reached inside or alongside ED by three thermodynamic framings:

1. **Jacobson**, from entropy-per-area: `G = (4ℏη)^{−1}` with `η = 1/4ℓ_P²` (`Paper_GravityAsEquationOfState`).
2. **Padmanabhan / T19**, from equipartition energy: `G = A_P c³/ℏ` with `A_P = ℓ_P²` (this paper).
3. **ED's constants ledger**, from the grain directly: `G = c³ℓ_P²/ℏ` as the dimensional conversion factor tied to `ℓ_P` (`Paper_027`, Essays 13/14).

These are not three independent confirmations. As §2 noted, Padmanabhan's count `n` and Jacobson's density `η` are the same grain seen twice (`n = 4S`), and the ledger route *is* that grain directly. They are three thermodynamic framings of one fact, so their agreement is a consistency check, not triple corroboration. But the one fact they frame is the point: **once the grain is set, `G` is not free.** It is the least-fundamental, first-to-emerge conversion factor, the "first shadow" the ledger names it. The honest caveat travels with all three equally: the *value* of the grain `ℓ_P` is a units anchor, inherited, not computed from something deeper — the same status as Jacobson's `l_c` and Padmanabhan's `L_P`. What the three routes establish is not the value but the *structure*: `G` is fixed the moment you have the grain, with `c` and `ℏ`.

## 8. Honest tiers and open edges

- **Recognition (the core result):** T19 *is* Padmanabhan's holographic-equipartition derivation in ED language (§3, line-for-line). This closes the microscopic-completions Padmanabhan target by recognition, not by new construction.
- **Grounded / measured (conditional):** ED grounds Padmanabhan's assumed *count-scaling* (boundary, not bulk) via A1 severance and the measured edge-count area law (`r^{2.02}`, `r_h^{0.96}`) — conditional on an assumed emergent geometry (curvature-emergence still open), the per-cell size and `1/4` coefficient value-inherited; the `G = c³ℓ_P²/ℏ` convergence is an algebraic identity across three framings of the one grain (§7), not three independent derivations.
- **Posited by both (the honest limit):** the equipartition rule itself (`½T` per channel) — an input in T19 exactly as in Padmanabhan (§5). ED grounds the count, not the rule.
- **Open:** a substrate derivation of the `½T`-per-channel from the near-horizon Rindler mode structure, ideally unifying it with `T = κ/2π` as one fact (§5, the standing lead); the covariant step past Newton, which inherits the open khronometric-vs-Lorentz question (§6); the value of the grain (inherited, as for Jacobson and Padmanabhan alike).
- **Explicitly out of scope, deferred:** Padmanabhan's *"law of emergence,"* `dV/dt ∝ (N_sur − N_bulk)`, the emergence of cosmic space as surface and bulk degrees of freedom equilibrate. The corpus has never engaged it. It runs directly into ED's own cosmic-horizon and `a₀` line (T20, `Paper_KM-II`, the dark-sector folder) and requires its own read-first pass before ED touches it. It is flagged, not attempted.

## 9. Position statement

Padmanabhan showed that gravity emerges from equipartition of energy over horizon degrees of freedom, one `½T` per Planck area, and left the count of those degrees of freedom to "any formalism of quantum gravity" with a minimum area. Event Density is such a formalism, and — the useful surprise of reading before writing — it had already made his exact move, apparently independently, as Theorem T19: the same holographic count, the same equipartition, the same Unruh inversion, the same `G = c³ℓ_P²/ℏ`. What ED adds over Padmanabhan is a substrate reason for the one thing he assumes: the count is the severed cross-chain edge-count on the causal cut, area-scaling *measured* rather than posited, one degree of freedom per grain. What ED does *not* yet add, and this paper does not pretend it does, is a derivation of the equipartition rule itself; that `½T`-per-channel is posited in T19 exactly as in Padmanabhan, and grounding it — plausibly by unifying it with the near-horizon temperature into one Rindler fact — is the open lead. T19 reaches Newton; the covariant step inherits the same khronometric wall as the rest of ED's gravity line. And the grain fixes Newton's constant in three thermodynamic framings — Jacobson's entropy density, Padmanabhan's equipartition count, and the ledger's grain — which §7 notes are one fact seen three ways rather than three independent confirmations; their consistency underlines that `G` was never fundamental. None of this is claimed as confirmed physics. It is claimed as a grounding, and as a recognition: the count Padmanabhan said his equipartition was waiting for, ED already had.

---

## Cross-references

- Padmanabhan, T., *Mod. Phys. Lett. A* **25**, 1129 (2010), arXiv:0912.3165 — "Equipartition of energy in the horizon degrees of freedom and the emergence of gravity." Related: arXiv:0911.5004 (review, *Thermodynamical Aspects of Gravity*); the `S = E/2T` origin, gr-qc/0308070.
- **The ED equipartition derivation (already on the books):** `event-density/papers/Substrate_Gravity_Foundations/ED_substrate_gravity_foundations_2026-04-28.md` §3 — Theorem T19, `N_R = 4πR²/ℓ_ED²`, `½ N_R k_B T_R = Mc²`, `G = c³ℓ_P²/ℏ`. (April-2026 framing re-tiered here per the preamble.)
- **The count-grounding assets:** `physics-papers/substrate-evaluation/Paper_CommonCauseNotChannel_A1.md` (A1, capacity-zero cut); `physics-papers/substrate-evaluation/Paper_AreaLawIsTheEdgeCount.md` (straddling-edge count, measured `r^{2.02}`); `physics-papers/gravity/Paper_GR-III_DynamicalRule.md` §7.4 (severed count `∝ r_h^{0.96}`); `foundations/BH_EntropyCoefficient_FromEventCounting.md` (the `1/4`).
- **The equipartition open lead:** `foundations/BH_Thermal2Pi_FromNearHorizonRindler.md` (`T = κ/2π` from ED's Rindler mode structure — the candidate home for a `½T`-per-channel derivation).
- **The khronometric wall:** `physics-papers/gravity/Paper_GR-II` (khronometric class), `Paper_GR-IV_ArrowsAlibi.md` (`α₁ = −4λ_local`, `α₂ = 0`, sparse-becoming suppression).
- **The three-route G convergence:** `physics-papers/substrate-evaluation/Paper_GravityAsEquationOfState.md` (Jacobson route); `Paper_027_Newtons_G.md` + Essays 13/14 (constants ledger).
- **Companion:** `physics-papers/microscopic-completions/README.md` (the family; Padmanabhan was ranked target #1).
