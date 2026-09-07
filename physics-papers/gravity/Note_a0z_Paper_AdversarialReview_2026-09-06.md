# Adversarial review — `Paper_a0z_MONDScaleTracksHubbleRate.md`

**Date:** 2026-09-06
**Brief:** Read as a hostile referee, and checked against the corpus's own papers and ledgers rather than only against the draft's internal logic (`CLAUDE.md` review rule). **Written by the same session that drafted it**, which is a real limitation and is stated at the end.

---

## Verdict up front

**Two objections are serious enough to change what the paper can claim, and one of them may be fatal to its headline.** The rest are fixable. Ordered by how much they matter.

---

## 1. FATAL-IF-UNADDRESSED — "MOND excluded at 29σ" is not a claim about MOND

> **✅ ADDRESSED 2026-09-07.** §1.2 is now a **four-way** table with *MOND-with-an-evolving-`a₀`* as its own row, and states plainly that **against that rival the discriminating content is the specific value `α = 1`** — the part under tension. It also concedes in the paper's own voice that position 3 **fits better right now and will keep fitting whatever is measured**, and that the only distinction is that **position 4 made a commitment that could fail.** The abstract and §5.2 were pulled into line: neither now claims MOND-as-such is excluded. **The paper is weaker and no longer contradicts itself.**

**The paper's central rhetorical move is that `α = 0` dying kills MOND and leaves ED standing. It does not.**

The draft's own §1.1 concedes that the `a₀ ≈ cH₀` connection is **standard MOND material**, citing Milgrom 2020 — *which is a review of it*. The corpus itself corrected a "no MOND analogue" claim as **false** on 2026-09-05 for exactly this reason. So:

- A MOND practitioner who already expects `a₀` to track the cosmic scale is **not refuted by evolution being detected. They are vindicated by it.**
- What died at 29σ is **constant-`a₀` MOND**, which is one reading among several — and not obviously the one the field's own theorists hold.

**And the consequence is worse than a framing problem.** If MOND can accommodate `a₀ ∝ H(z)^α` with `α` *fitted*, then on this data:

| account | fit to `α = 1.18 ± 0.04` |
|---|---|
| MOND with a fitted exponent | **fits exactly, by construction** |
| this prediction (`α = 1`, unfudgeable) | **+4.4σ off** |

> **On its own evidence, the data currently favour a MOND with a free exponent over this framework.** The paper's advantage is that its `α` cannot be tuned — but an untunable number is a virtue **only when it is right**, and right now it is the thing under tension.

**The paper says "the ED-vs-MOND weapon" in spirit and never confronts this.** §1.2's three-way table is the load-bearing rhetorical device and it **quietly assumes constant-`a₀` MOND is the only MOND**, which §1.1 has already denied two paragraphs earlier. **The paper contradicts itself across one page.**

**Required fix:** the three-way table must become four-way, with *MOND-with-evolving-`a₀`* as a distinct column, and the paper must state plainly that its discriminating content against **that** rival is the **specific value** `α = 1` — which is exactly the part currently disfavoured. That is a much weaker paper, and it is the honest one.

## 2. SERIOUS — the 8% local match may be circular

> **✅ ADDRESSED 2026-09-07.** Checked first: `Paper_029` audit row 10 says the assembly constant was *“set to the value that returns the result”*, and **the result targeted was the `1/(2π)` FORM, not the observed `a₀`** — so the charge of reverse-engineering from data is **not** supported, and the review overstated it. **But that rescues the intent, not the inference:** a coefficient nothing upstream fixes cannot be evidenced by the value it was set to produce. **The ~8% is now excluded from the evidence** — demoted in the abstract, removed from §5.2's confirming half, and §3.2 states the general consequence, that any paper making this prediction must decline its own best-sounding sentence.

§5.2 offers the local intercept matching to ~8% as supporting evidence. §3.2 says the `1/(2π)` is **postulated**, reinstated "at an assembly step fixed by a normalisation choice that nothing upstream determines."

**A referee will ask the obvious question: was that normalisation chosen to land on the observed `a₀`?** The corpus's own audit says the step is *"set to the value that returns the result."* If so, the 8% agreement is **not evidence at all** — it is the calibration, reported as a result.

**The paper cannot have this both ways.** Either the coefficient is independently motivated — in which case say how — or the local match must be **struck from the evidence section** and appear only as a consistency remark with the circularity flagged. **As drafted, §5.2 invites a reviewer to catch the paper doing something its own §3.2 has already admitted.**

## 3. SERIOUS — the coefficient failure undermines confidence in the exponent

> **✅ ADDRESSED 2026-09-07, §3.6.** Checked against `Paper_029`'s audit table rather than argued: the derivation has a **radial** step (`R_H = c/H`, a rate crossover) and an **angular** step (the `|m|=1` dipole projection), and **every disputed, postulated and analogical row is in the angular step** — the radial step carries none. **The exponent is entirely radial** (`a₀ ~ c²/R_H`, one power of `H` because there is one horizon). **Independent check:** the scale is reached by three routes, **two of which never use the dipole projection**, so the `H`-dependence survives deleting the machinery that failed. **The honest residual is now named in the paper:** the exponent also rests on the horizon being read **live rather than frozen**, which is the mechanism's core assertion and not a theorem — a frozen horizon gives `α = 0` and is indistinguishable from MOND. **That is the right place to be attackable.**

The paper's structural pride (§3.3) is that the disputed `K` and the tested `α` are independent, so scepticism about the `2π` need not touch the exponent. **Formally true. Evidentially weak.**

**Both come from the same mechanism.** That mechanism demonstrably failed to deliver `K` — the factor cancels in the source's own algebra and has to be reinstated by hand. A referee is entitled to ask: **if the horizon-projection argument cannot be trusted to produce the coefficient, why should it be trusted to produce the exponent?**

The paper needs an answer. There may be a good one — the exponent follows from *how many powers of `H` a live horizon contributes*, which is a counting statement, while the coefficient depends on angular integrals that are where the failure occurred. **That distinction, if it holds, is worth a paragraph and the paper does not make it.**

## 4. MODERATE — step 9 is special pleading without a number

> **✅ ADDRESSED 2026-09-07, §5.3 — and the number did not come back convenient.** The budget is computed in `event-density/theory/a0z_powerlaw_refit.py`. **Propagating only their `a₁ = 1.59 ± 0.10` through the endpoint conversion reproduces `±0.034`, which identifies the published bar exactly**: their statistical error through one reduction and nothing else. Adding the intercept, the cosmology and the **reduction choice** gives **`α = 1.15 ± 0.07`, `α = 1` at 2.3σ**, with **73% of the variance missing from the published bar**. **The asserted “~1–2σ” was wrong in the paper's own favour** — the computed figure is 2.3σ, and the paper now says so. **Step 9 re-tiered `A → D-via-I`; the residual judgement is the intercept's unpublished error, carried as an explicit sensitivity (3.2σ / 2.3σ / 1.8σ) rather than chosen.**

> **A finding that came out of doing it rather than arguing it:** their linear fit has **no constant exponent**. The local slope `d ln a₀/d ln H` runs **1.78 → 0.90** across their own range, **crossing `α = 1` at `z ≈ 1.1`, inside the data.** Four defensible reductions give 1.118–1.178, and **the corpus quoted 1.178 — the choice that maximises `α`.** A new §5.3b compares the shapes directly without forming an exponent: they agree to 4–7%, but the residual is **structured, not an offset**, so the disputed amplitude cannot absorb it.

The paper's own audit calls step 9 its "soft joint," which is honest, but does not repair it. **The argument is: the published `±0.04` is too small, therefore `+4.4σ` is really `1–2σ`.** No alternative error budget is produced. No systematic is quantified. The paper argues against both the published number **and** the survey team's own reading, on the strength of unquantified concerns.

**A referee will not accept this**, and is right not to. Either estimate the dominant systematic — inclination and pressure support at `z ~ 1` are tractable to order-of-magnitude — or **state the tension at its face value of 4.4σ** and let the reader discount it. **Currently the paper takes the benefit of the doubt without earning it.**

## 5. MODERATE — the evidence base is one survey with unpublished per-bin data

Figure 3 only; no covariance; no per-bin table. **A paper built on a result whose numbers are not fully public is thin**, and the draft should say so in §5.1 rather than in a subordinate clause of §5.3.

## 6. MINOR but self-inflicted — §7 undercuts the standalone claim

The paper says it "stands or falls on §5 and §6 alone" and then names four corpus papers as its core chain. **Both cannot be true.** Either the derivation is reproduced here — §2 and §3 currently assert rather than derive — or the paper is a companion piece and should say so. **A reviewer who follows the provenance pointer finds ~280 papers, which is not the impression §7 intends to create.**

## 7. MINOR — an internal inconsistency the paper inherits and flags but does not resolve

§3.4 notes that the corpus's own prediction list says `α = 1` is *dimensionally forced* while the report says it is **not** (because `ℓ_P` exists). The draft picks the careful version and adds a parenthetical. **That is the right call, but a live contradiction in the source material should be fixed there, not annotated here.**

---

## What survives, and it is not nothing

- **The prediction was registered before the data**, with the `×1.8 at z = 1` figure explicit. That is rare and it is the paper's real asset.
- **The exponent is genuinely unfudgeable** within the framework, which makes it a real bet rather than a fit.
- **Evolution was detected.** Whatever the rate turns out to be, a framework that said "this scale should evolve" before a survey found it evolving has earned a hearing.
- **The kill condition in §6 is stated in advance and is sharp.** Most theory papers do not do this.

---

## What I would tell the author

**The paper as drafted claims a two-horse race it has already conceded is a three-horse race.** Fix §1.2 first — everything else is presentational, but that one is a contradiction a referee will find on the first read, and finding it will colour everything after.

**Then decide what the paper is for.** There are two honest versions:

1. **"A registered prediction under tension."** Lead with the tension, treat the 30σ evolution as context, and make the paper about a sharp falsifiable exponent and the test that would settle it. **Weaker headline, much harder to dismiss.**
2. **"Evolution detected, constant-`a₀` excluded."** Stronger headline, but the contribution is then mostly the survey's, and the framework's specific number is the part that is struggling.

**Version 1 is the one that matches the evidence.**

---

# Round 2 — external review, 2026-09-07

**Three models outside this session read the Report, the itemized-theory workbook and this paper.** That is the outside reader the limitation section below said this review was not a substitute for. **It found three things round 1 did not, and one of them is an error round 1 introduced.**

## E1. CONFIRMED, and it is mine — `α = 1.18` is our re-fit, not the survey's measurement

**The reviewer's charge:** the Load-Bearing Step Audit tags `α = 1.18 ± 0.04` as *"I — measurement, same source,"* which reads as though it came from the survey.

**Checked against the literature, and the reviewer is right.** Ciocan et al. (MUSE-DARK III, arXiv:2604.22613, A&A 2026) publish a **linear** parametrisation:

$$a_0(z) = a_0(0) + a_1 z, \qquad a_1 = 1.59 \pm 0.1 \times 10^{-10}\ \mathrm{m\,s^{-2}}$$

with per-bin values rising `1.99 → 2.71 ×10⁻¹⁰` across 79 galaxies at `0.33 < z < 1.44`. **They publish no power law and no `α`.** The exponent this paper's entire tension is stated against is **ED's own conversion** of their linear fit (addendum A10, 2026-07-14).

**Fixed:** audit row 8 split into 8 (theirs) and 8b (ours); §5.1 rebuilt as a three-column table with a *whose* column; §5.3 now says the `±0.04` is not the survey's error bar on `α` because the survey never fit `α`, and that a conversion between functional forms carries a form-choice error no propagated statistical bar contains. **The refit is still not shown explicitly, and the paper now says so.**

**The upstream finding is worse than the paper's.** The **Report has carried the correct attribution since 2026-07-21**. Four downstream documents never received it, including **`ED_Master_Predictions_List` 1.15 — the canonical source of truth**, which is where this paper's numbers came from. **A stale canonical row fed the error into new work**, which is the exact failure `CLAUDE.md`'s close-the-loop rule exists to prevent. All four corrected 2026-09-07.

## E2. CONFIRMED, and round 1 missed the rival entirely — ΛCDM predicts apparent evolution too

**Round 1's objection 1 fixed the MOND framing and left position 1 alone**, marking ΛCDM "untouched here." **That was too generous to the paper.**

**Magneticum** (*MNRAS* `10.1093/mnras/stac3017`, *"ΛCDM with baryons versus MOND: the time evolution of the universal acceleration scale in the Magneticum simulations"*) shows plain ΛCDM **with baryons** producing an **apparent** rise in the RAR acceleration scale with redshift, from ordinary galaxy assembly and baryon modelling, **with no modified gravity.**

> **So the ~30σ detection of evolution excludes constant-`a₀` MOND and nothing else.** Three of the four positions accommodate evolution. **The paper's headline result discriminates against exactly one rival, and it is not the main one.**

**Fixed** in §1.2 (table row 1 and a following paragraph), ML 1.15, and the Report's flagship. **This is the second comparative claim about another literature in three days to be wrong in the ED-favourable direction** — the "no MOND analogue" correction was 2026-09-05. **No internal check catches this class; it needs a search box.**

## E3. NOT VERIFIED — a possible systematics rebuttal, recorded as a check

A reviewer reports a 2026 analysis, *"Three baryonic systematics, each sufficient,"* re-analysing Ciocan et al.'s own public catalogue and claiming baryonic mass-budget effects account for the trend: 82% of the binned trend, 77% of the fractional evolution, and a 0.39 dex dynamical-vs-photometric stellar-mass drift at 3.6σ.

**Three searches returned no locatable record of this paper**, and the one detailed description came back only after its title had been supplied in the query — so it may be an artifact of the search rather than a source. **It is written into the paper as §5.3a: an open check, explicitly not a citation.**

> **If it exists it matters more than the exponent tension**, because it attacks the ~30σ detection itself rather than the rate. **Confirming or excluding it is a prerequisite to treating §5 as settled.**

## What round 2 changes about the paper's standing

**Every supporting claim has now been removed by review, across two rounds.** The local 8% is out of the evidence (round 1, objection 2). The 29σ exclusion applies to one rival and not to ΛCDM (E2). The exponent the tension is measured against is our own conversion (E1). And the detection underpinning all of it has an unverified challenge on record (E3).

**What survives is what survived round 1, unchanged:** a **registered, forward-dated, untunable `α = 1` with a kill condition stated in advance.** That is the whole asset, and it is a real one. **A paper that arrives at exactly its bet, having had every ornament stripped off it by three rounds of review, is in the right shape** — it just cannot be sold as a result.

---

## Limitation of this review

**I drafted the paper and then reviewed it, in the same session.** That is precisely the arrangement the corpus's own review rule exists to prevent — an internal-consistency check validating its own output. Objections 1, 2 and 3 are ones I did not see while writing and do change the paper materially, which is some evidence the review was not a rubber stamp. **It is not a substitute for an outside reader, and the corpus has a documented instance of a self-review validating redundant work.** Treat this as a first pass that lowers the cost of a real one.

> **UPDATE 2026-09-07: the real one happened, and it is recorded above as Round 2.** It found an error this review introduced (E1), a rival this review left standing (E2), and a possible challenge to the underlying detection (E3). **The self-review was worth running and was not sufficient**, which is the outcome the corpus's review rule predicts rather than a surprise.
