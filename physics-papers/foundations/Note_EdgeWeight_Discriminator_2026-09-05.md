# Note — The `w(e)` fork is decided: regridding consistency forces the geometric mean

**Date:** 2026-09-05 (late)
**Status:** Working note. Feeds `foundations/Paper_Individuation_TheSystemEnvironmentCut.md` §2.1 and audit row 4.
**Check:** `internal notes/_check_edge_weight_discriminator.py` (re-runnable, four tests).
**Anchors:** `Paper_007_HilbertSpace` §2 (`P-Motif-Algebra`), `Paper_087` §P12 (the `Coh` operationalization), `Paper_087` P03 (locus index set).

---

## 1. The fork, as it was left

Written earlier today into the individuation paper:

$$w(u,v)\;=\!\!\!\sum_{K\,\in\,\mathcal K(u)\cap\mathcal K(v)}\!\!\!\sqrt{b_K(u)\,b_K(v)}$$

with the honest caveat attached: **`min(b_K(u), b_K(v))` satisfies all five stated requirements too** — non-negative, vanishing on unshared channels, symmetric, normalized so a fully-shared channel of bandwidth `b` carries weight `b`. A *bottleneck* reading against an *amplitude-product* one. The geometric mean was chosen because it is what the corpus already does, **not because anything forced it**.

That is a real fork, and `min` is not a strawman: the individuation ratio is a **cut** quantity, and minimum-capacity is the canonical thing to put on a cut.

## 2. Why the obvious discriminator would have been circular

The tempting move is to point at `Paper_030`'s bilocal `√(b_loc·b_horizon)` and at `P-Quadratic-Strain`'s cross term, note that the MOND interpolation `a = a_N + √(a_N a_0)` is a maximally asymmetric two-locus term fixed by data, and observe that `min(a_N, a_0)` would give a completely different and wrong interpolation.

**That is not admissible here.** Those two constructions were reason #3 in the original justification. Using them to settle the fork restates the evidence rather than testing it. The discriminator has to come from somewhere else.

## 3. The decisive input, from elsewhere in the corpus

Two established facts, neither used in the original justification:

- **`P-Motif-Algebra`** (`Paper_007` §2, a named postulate carried in `Paper_087`'s census table): *"The set of substrate-level amplitude tuples `{P_K^C}` forms a complex vector space under componentwise addition."* **Contributions combine by adding amplitudes, and `b = |ΣP|²`.** Canonical `Paper_087` §P12 already computes on exactly this rule: `Coh = |Σ_a P_a|² − Σ_a |P_a|²`.
- **P03 supplies "the locus index set".** An index set is a bookkeeping choice, not a physical fact.

## 4. Requirement (R) — regridding consistency

`b_bdry(S)` is supposed to be a property of **the cut**. So: merge two loci lying on the **same side** of the cut into one coarser locus. The boundary bandwidth must not move.

$$w(U,v)\;=\;w(u_1,v)+w(u_2,v)\qquad\text{for }U=\text{merge}(u_1,u_2)$$

Stated for **phase-aligned** merges, which is the weakest useful form. For misaligned merges *no* weight can be additive, because merging genuinely destroys shared amplitude (`|P₁+P₂| < |P₁|+|P₂|`) — that is physics, not bookkeeping, and §5's Test 2 is about how the two candidates handle that deficit.

## 5. What the four tests show

| | geometric mean | `min` |
|---|---|---|
| **1. Regrid `N` aligned loci** | exact for every `N` | wrong by a factor of `N` |
| **2. Misaligned merge deficit** | independent of `b_K(v)` | depends on `b_K(v)` |
| **3. Verdict under regridding** | stable | **flips** |
| **4. Power-mean scan `M_p`** | `p = 0`: violation `0` | `p → −∞`: violation grows |

**Test 1.** `N` aligned loci each with `b_K = 1`, merged: amplitude addition gives `b_K(U) = N²`. The geometric mean returns `√(N²·1) = N`, matching the unmerged sum exactly, for every `N`. `min` returns `min(N², 1) = 1` against an unmerged `N` — it **saturates at the outside locus and stops seeing the system side at all**.

**Test 2.** At relative phase `d`, the geometric mean's merge deficit is `|P₁+P₂|/(|P₁|+|P₂|)` — identical down every `b_K(v)` row, so **regridding the system side factorizes out of the environment side**, and the deficit is exactly the amplitude triangle inequality, which is exactly the deficit `Coh` already records. Under `min` the deficit ratio changes with `b_K(v)` (`0.50 / 0.50 / 2.00` across the rows at `d = 0`): the two sides do not separate.

**Test 3 — the one that matters.** Regridding **only the environment**, so the system and `b_int` are untouched and every change lands in `b_bdry`. With `b_int = 1.5`, `b_leak = 0.25`, `M = 4` environment loci, `θ_ind = 2`:

| map | `b_bdry` fine | `b_bdry` coarse | ratio fine | ratio coarse | verdict |
|---|---|---|---|---|---|
| geometric mean | 2.0000 | 2.0000 | 0.7500 | 0.7500 | not → not |
| `min` | 1.0000 | 0.2500 | 1.5000 | 6.0000 | **not → individuated** |

**Under `min`, the same physical system is not individuated on the fine grid and is individuated on the coarse one.** Nothing physical changed; only the indexing did.

**Test 4 — uniqueness, not preference.** Scan the power-mean family `M_p`, which interpolates continuously from `min` (`p → −∞`) to the geometric mean (`p = 0`) and is correctly normalized at every `p` since `M_p(b,b) = b`. The regridding violation is `8.91, 8.81, 8.59, 8.02, 6.69, 2.31` for `p = −8 … −0.1`, **`0.000000` at `p = 0`**, then `3.01, 20.25` for `p > 0`. **A unique zero.** (Every `p > 0` had already failed an earlier requirement anyway — `M_p(b, 0) ≠ 0`, so an unshared channel would carry weight — which is why the honest fork was between `p = 0` and `p → −∞` to begin with.)

## 6. The argument behind the scan

Let `w = f(b_u, b_v)`, non-decreasing in each argument (more bandwidth cannot mean less shared capacity). Requirement (R) for phase-aligned merges, with amplitudes `x_i = |P(u_i)|`:

$$f\big((x_1+x_2)^2,\,b_v\big)=f(x_1^2,\,b_v)+f(x_2^2,\,b_v)$$

Set `g(x) = f(x², b_v)`. Then `g(x₁+x₂) = g(x₁)+g(x₂)` for all `x ≥ 0` — **Cauchy's functional equation** — and `g` is monotone, so `g(x) = c(b_v)·x`. Hence `f(b_u,b_v) = c(b_v)√b_u`; symmetry forces `c(b_v) = c√b_v`; and `f(b,b) = b` fixes `c = 1`:

$$\boxed{\,f(b_u,b_v)=\sqrt{b_u\,b_v}\,}$$

**The geometric mean is the unique regridding-consistent edge weight, given that contributions combine by amplitude addition.**

## 7. The result worth keeping: the fork was the merge rule in disguise

**The edge weight was never an independent choice.** Had bandwidth itself been additive under merging (`b_K(U) = b₁ + b₂`) rather than amplitude, the same Cauchy argument run in `b` gives `f` linear in each argument — the **product** `c·b_u b_v` — and **both** candidates fail. Whatever rule governs coarse-graining loci fixes the edge weight, and fixes it uniquely.

ED's merge rule is amplitude addition. So ED's edge weight is the geometric mean, and there was never room for `min`.

Note also what `min` fails *at*: it is regridding-consistent only in the corner where the minimum always falls on the same side, i.e. **exactly where it stops depending on both endpoints** and is no longer a shared-content measure at all.

## 8. What is assumed, stated plainly

1. **Requirement (R) is an assumption, not a theorem** — that `b_bdry` is a property of the cut rather than of the locus indexing. It is the standard demand on any coarse-grained quantity, it is stated in its weakest useful form (same-side, phase-aligned merges only), and **without it the individuation ratio is not a measurable quantity and `F-IND-1` is not a falsifier.** So the cost of rejecting (R) is higher than the cost of accepting it, but it is a cost either way.
2. **One soft joint.** `P-Motif-Algebra` is stated for *chain* amplitude tuples, componentwise over channels. Applying it to a merge of *loci* is the same operation on the same objects and is what `Paper_087`'s `Coh` already does when it sums `P_a` over contributions, but **it is an extension of the postulate's stated domain**, and it is the one place this argument leans on a reading rather than a statement. If a future audit narrows `P-Motif-Algebra` to chains only, this result needs a locus-level restatement of the same rule.
3. **Verdict: `D-via-I` conditional on (R) + `P-Motif-Algebra`** — not unconditional, and not `D`.

## 9. Write-back

- `Paper_Individuation_TheSystemEnvironmentCut.md` §2.1 — the "honest alternative" paragraph is replaced by this result; audit row 4's parenthetical drops "not a forced choice".
- No new postulate named; the census is unchanged. `P-Motif-Algebra` already exists.
- Gravity ledger #88.
