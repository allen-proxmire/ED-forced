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

§5.2 offers the local intercept matching to ~8% as supporting evidence. §3.2 says the `1/(2π)` is **postulated**, reinstated "at an assembly step fixed by a normalisation choice that nothing upstream determines."

**A referee will ask the obvious question: was that normalisation chosen to land on the observed `a₀`?** The corpus's own audit says the step is *"set to the value that returns the result."* If so, the 8% agreement is **not evidence at all** — it is the calibration, reported as a result.

**The paper cannot have this both ways.** Either the coefficient is independently motivated — in which case say how — or the local match must be **struck from the evidence section** and appear only as a consistency remark with the circularity flagged. **As drafted, §5.2 invites a reviewer to catch the paper doing something its own §3.2 has already admitted.**

## 3. SERIOUS — the coefficient failure undermines confidence in the exponent

The paper's structural pride (§3.3) is that the disputed `K` and the tested `α` are independent, so scepticism about the `2π` need not touch the exponent. **Formally true. Evidentially weak.**

**Both come from the same mechanism.** That mechanism demonstrably failed to deliver `K` — the factor cancels in the source's own algebra and has to be reinstated by hand. A referee is entitled to ask: **if the horizon-projection argument cannot be trusted to produce the coefficient, why should it be trusted to produce the exponent?**

The paper needs an answer. There may be a good one — the exponent follows from *how many powers of `H` a live horizon contributes*, which is a counting statement, while the coefficient depends on angular integrals that are where the failure occurred. **That distinction, if it holds, is worth a paragraph and the paper does not make it.**

## 4. MODERATE — step 9 is special pleading without a number

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

## Limitation of this review

**I drafted the paper and then reviewed it, in the same session.** That is precisely the arrangement the corpus's own review rule exists to prevent — an internal-consistency check validating its own output. Objections 1, 2 and 3 are ones I did not see while writing and do change the paper materially, which is some evidence the review was not a rubber stamp. **It is not a substitute for an outside reader, and the corpus has a documented instance of a self-review validating redundant work.** Treat this as a first pass that lowers the cost of a real one.
