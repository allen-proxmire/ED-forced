# The sign check cannot answer this — and the question was mis-framed. It is about the commitment rule, not `Σ_C`

**Date:** 2026-09-06
**Status:** **A proposed check withdrawn before running it, and the question relocated.** No new probe.

---

## 1. The check I proposed does not apply

I recommended re-running the three-way sign check (#71) with `Grad` entering intensively, on the grounds that it is the one place `Σ_C`'s form is pinned by an external result.

**`Grad` is not in that check.** From `internal notes/_check_sigma_sign.py`, in the source:

> `a_r = -d(Sigma_C)/dR` in every case (P12). **`Grad` is dropped throughout: it is spherically uninvolved here and identical across the three, so it cannot discriminate.**

**So the run would have produced bit-identical output and told us nothing.** Reading the script took under a minute; I should have done it before proposing the check.

## 2. Nor can anything else gravitational

`Grad`'s contribution to the gravitational results is suppressed by `ℓ_ED²/R²` — **`10⁻⁸⁴` to `10⁻¹¹²` across physical scales** (`Note_Grad_Proposal` §4). **No gravitational observable can distinguish an extensive `Grad` from an intensive one**, because neither is measurable there at all.

## 3. Nor can the layer-2 Laplacian, on a regular lattice

`Grad`'s strongest structural support is that it coarse-grains to the layers program's one forced operator, `∇·(M∇φ)` (`layers/layer_2/OneOperator_TheLaplacian.md`).

**On a regular lattice the coordination number `n` is constant, so extensive and intensive differ by an overall constant and yield the same operator.** The distinction only exists where `n` varies — **on an irregular graph, or on a growth front.**

**Which is exactly where the probe found it.**

## 4. So the question was mis-framed, and the right version is different

I asked whether `Σ_C`'s extensive `−Grad` is *"the right way for the term to enter the functional."* **That conflates two things:**

- **`Σ_C` is a landscape.** Its terms are what they are; `Grad` extensive is the Dirichlet form, summed over edges, and nothing here challenges that.
- **How a chain *selects* among candidates using that landscape is a separate rule.**

**The extensive/intensive difference lives entirely in the second.** The functional can stay extensive while selection normalizes — **those are compatible, not competing.** So the correct question is not about `Σ_C` at all:

> **Is ED's commitment-selection rule normalized over the candidate set, or does it use raw `Σ` scores?**

## 5. And the corpus already answers that, which is the useful part

**`Paper_003`'s `P-LinRate`**, the load-bearing postulate of the Born-rule derivation:

$$\Pr(\text{commit to }K^*)\;\propto\;\frac{b_{K^*}}{\sum_{K'}b_{K'}}$$

> **ED's own commitment rule is normalized over the candidate set. It is a probability, not a raw score.**

**So intensive selection is what the corpus already commits to, and the simulator's argmax-over-raw-`Σ` is the outlier** — a convenient deterministic stand-in for a normalized probabilistic rule.

**That is a candidate resolution and not a proof.** The two normalizations are not the same object: `P-LinRate` normalizes over the **channel set at a locus**, while the probe normalizes by the **coordination number of the growth front**. **They coincide only if the candidate set is the neighbour set**, which is true in the probe and is not stated anywhere as a general identification.

## 6. What this leaves

**Withdrawn:** the sign-check recommendation. It cannot discriminate and would have been a theatrical run.

**Relocated:** the question is about the **commitment rule**, not `Σ_C`'s construction. `Σ_C` is untouched by any of this.

**Newly relevant, and not previously connected:** **`P-LinRate` already normalizes**, which makes intensive selection the corpus-consistent reading and the probe's raw argmax the anomaly. **That is a genuine link between the Born-rule arc and the phase-coherence arc that neither paper draws** — and it is the strongest thing supporting #111's finding, because it means the form that binds is also the form ED's own selection postulate prescribes.

**Owed:** whether `P-LinRate`'s channel-set normalization and the probe's coordination-number normalization are the same operation. **They are not obviously the same, and nothing in the corpus identifies them.**
