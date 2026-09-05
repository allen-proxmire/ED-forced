# F1 Arm C (Σ_C) — Result: the collision was findable blind, the resolution was not, and one run found a hole in my sign check

*Run 2026-09-05, **three families**. Scored against the measures pre-registered in `Seed_F1_ArmC_SigmaC.md` before any output was seen. **The third family's reply arrived after the first scoring pass and materially changed three of the four measures; the revision is §7 and the tables below are the revised ones.***

**Conflict of interest, and it bites harder here than in any previous arm:** one family is Claude, the scorer is Claude, and **the thing being scored is a chain the scorer wrote this morning.** That family produced the finding that damages the chain most. **Recorded because the alternative reading — that the scorer softened the other family and amplified its own — is exactly what a reader should suspect, and §5 is the check on it.**

---

## Verdict

| Measure | GPT | Gemini | Claude |
|---|---|---|---|
| **S1 — find the `Coh`/`Str` collision** | **YES** | **YES** | **YES** |
| **S2 — reach the settled split** | no — posed it as a choice | no — different resolution | no — declined |
| **S3 — the P04 non-negativity route** | **YES, independently (gap 7)** | not raised | used, not flagged |
| **S4 — `Grad`** | undefined, `(i)` | **proposed the Dirichlet form** | undefined; may carry MOND |
| *The aggregation gap* (unregistered) | **YES** | no | **YES** |

**S1 passes 3/3. The collision was findable blind, by every family, in one pass.** It took me a full session and an external prompt.

**S2 fails 0/3 — nobody reached the settled split.** But the closest attempt failed in a way that is itself evidence for the check (§7).

**S3 hits 1/3, and the hit was independent** — without the equation the measure was written against.

---

## 1. The collision was findable

**Gemini:** *"This introduces an explicit contradiction in the literature: Part 2(b) equates `Coh` both with the cross-term … and with the full sum squared (which equals `Str`) … If `Coh = Str`, then `Coh − Str ≡ 0`, causing the interference dynamics to cancel out completely."*

**Claude, more sharply, and it went one step further than I did.** Under the §2 reading it computed `Coh − Str = −Σ_a b_a` **exactly**, and then drew the consequence:

> *"Phase/polarity — the substrate's supposedly primitive angular variable (P09) — plays no role at all in `Σ_C` under this combination … if phase cancels out of `Σ_C`, **decoherence events are gravitationally inert**, which seems like a strange design choice for a framework that puts phase transport among its primitives."*

**That is a better statement of the stakes than the one in `Note_SigmaC_Defined_2026-09-05.md` §4.** I framed the collision as *the gravity arc loses its MOND mechanism*. **The sharper framing is that P09 and P05 become dynamically irrelevant** — a primitive and a connection doing no work — which is a structural indictment rather than an arc-local one.

## 2. Neither reached the settled split, and one refused to try

**Claude declined outright**, correctly under the seed's own honesty instruction: *"I am not going to pick the one that looks more likely to be right — this is a genuine contradiction in the source material, and I'm reporting it rather than resolving it."*

**Gemini proposed a different resolution: drop `Str` entirely.** *"`Σ_C = Σ_K (Coh_K − Grad_K)` … pure non-interfering bandwidth `Σb_a` is absorbed into the background."*

**That resolution does not reproduce Part 3, and Gemini's own check contradicts it.** Its Newtonian verification used *"if strain enters with a negative sign (`−Str`)"* — **the term its resolution deletes.** Without the diagonal there is no `−GM/R`, and Newton is lost. **So the pre-registered negative check does not fire: no family produced a different resolution that reproduces the established results.**

**But S2 failing 0/3 is not nothing.** The settlement was reached by pushing three candidate assignments through to `a(R)` and keeping the survivor. **No family did that** — one declined, one proposed a rival that loses Newton, and one reverse-engineered the target `Σ(R)` analytically and got the sign wrong (§7). So the settlement is not the *obvious* reading of the material — **it is the reading you get only if you run the check.** That is a real limit on how much independent support today's four supports represent.

## 3. Gemini independently proposed the Dirichlet `Grad`

> *"`Grad_K(u) = γ Σ_{v∼u} |P_K(v) − P_K(u)|²`, representing the discrete Dirichlet energy of participation amplitudes across adjacent loci."*

**That is `foundations/Note_Grad_Proposal_2026-09-05.md`'s proposal, arrived at independently, from the same material, without any of the four supports that note assembled.** It also classified it `(iii) GENUINE POSTULATE` — matching that note's own tier of *proposal, not derived*.

**This is the strongest support the `Grad` proposal has.** The other five are internal arguments; this is a second reader reaching the same object from the same axioms and agreeing on its status.

## 4. The finding that damages this morning's work

**Claude's central negative, and I have checked it and it stands:**

> *"`2√(b^{(L)}b^{(H)})\cos(Δπ) = 2√((GM/R)(a₀R))\cos(Δπ) = 2√(GMa₀)·\cos(Δπ)`. Notice the R cancels — this quantity is **exactly independent of R**. An R-independent term has zero adjacency-gradient, so under a direct, pointwise application of P12 … this cross term contributes **nothing** to the acceleration — not a small contribution, exactly zero."*

**`Paper_QuadraticStrain_v1` §5.1 says the same thing about the R-cancellation** — *"the per-channel geometric mean is `√(GMa₀)`, independent of R"* — and then supplies the log from *"the bilocal-channel density `∝ 1/R` along the radial direction (`Paper_030` §4.3)"* plus a radial integral.

**Two things follow, and the second is the one that costs.**

**(i) Partly a seed error, mine.** I gave the prompt *"after the appropriate sum over channels and the radial integral"* without the `1/R` bilocal density. **The corpus supplies the measure and the run could not have known.** Gap 4 is therefore over-stated as a corpus defect.

> **→ DOWNGRADED the same night (gravity ledger #79).** The runs read the radial integral as a **path/history** aggregation. It is not one: `ρ_bilocal(R')` is a **channel density**, so `∫ρ dR'` is a **sum over the chain's radially-distributed channels** — and P12 already requires that sum, defining chain-level `Str(C)` against per-channel `Str_K`. **So this is not a missing structure but the already-known `Str(C) = Σ_K Str_K` bridge** (arm B's `D07a`; gap 1 of this very run). **The log is licensed once the channel sum is granted; what is unstated is the sum.** One residual stands: the integral sums channels anchored at *other loci*, and whether those are the chain's own is the layer seam's locality question.

**(ii) The deeper point survives, and it is a hole in `Note_SigmaC_SignCheck_2026-09-05.md`.** **P12 as stated is a *local* gradient of a *locally-evaluated* functional. The corpus's derivation uses a shell integral with a measure.** That is an aggregation rule, and P12 does not contain one. **My sign check took the `ln R` form from §5.1 as given and asked only which assignment gets the signs right. It never asked whether P12 licenses a log at all.**

**So the sign check settles less than I claimed for it.** It establishes: *given* that the cross term enters `Σ_C` as `√(GMa₀)\ln R`, only the diagonal/off-diagonal split produces two attractive terms. **It does not establish that P12 can produce that form.** The check is sound within its scope and its scope was not stated.

**And it lands on the layer seam from a third direction.** A locally-evaluated `Σ_C` and an accumulated one are not the same object, and which one P12 means is the question `layers/Note_TheSeam_And_SigmaC_2026-09-05.md` and `gravity/Note_a0_TwoPi_RepairRoutes` §4f are both circling. **Three arcs now, reached independently, and this one by a reader who had none of the others.**

## 5. What this run says about the day's chain

**Confirms:** the collision is real and findable by any careful reader — 3/3 blind, first pass. **The `Grad` proposal is not idiosyncratic** — an independent reader produced the same object and the same tier.

**Does not confirm:** the settled split. **No family reached it, and none ran the check that produces it.** Four supports were assembled today on the premise that only one assignment works; **this run does not test that premise, because nobody tested it.**

**Damages:** the sign check's scope. **It answers "which assignment, given the log" and not "is the log licensed."** Corrected in that note.

**Net: the chain's foundation (the collision) is independently confirmed; its resolution is independently unreached; and its most-cited step has a stated scope it did not previously carry.** That is roughly the outcome a blind replication is for, and it is not the outcome I expected.

## 6. Seed errors, recorded

1. **S3 was unscoreable.** The P04 route depends on `Paper_QuadraticStrain_v1` §4's `Φ_N = Σ_K b_K^{(L)} = −GM/R`, **which the prompt did not contain.** The measure was pre-registered against material the reader never saw. **My error, not theirs.**
2. **The `1/R` bilocal density was withheld** without intending to withhold anything load-bearing (§4(i)).
3. **One family returned the prompt rather than a reply.** Recorded as no-return; a re-run on that family would make this a three-family result.

---

*Gravity ledger Staleness #77. Seed: `Seed_F1_ArmC_SigmaC.md`.*

---

## 7. Revision after the third family's reply

**Three of the four measures move, and one new finding is the most useful thing in the run.**

### S1 → 3/3

GPT found the collision and worked both branches explicitly: *“Those are not the same quantity … there are consequently two possible readings”* — literal, giving `Coh − Str = −Σ_a b_a`; or `Coh = |ΣP|²`, giving `Coh − Str = 0`. *“Those are materially different stability landscapes. The framework has to choose.”* **All three families found it independently. The collision is not subtle; it was simply never looked for.**

### S3 → hit, and it is the P04 route reached without the equation it was written against

GPT's gap 7: *“Bandwidth is explicitly non-negative: `b_K ≥ 0`. **Yet the required gravitational stability contribution is `Σ_N = −GM/R`.** A positive quantity proportional to `GM/R` therefore cannot simply be identified with this contribution without specifying which term enters `Σ` and with what sign.”* **Its proposed fix — `Σ_grav = −λ B_grav`, `λ > 0` — is exactly `Σ_C ⊃ −Str` with positive bandwidth.**

**That is the second of the two independent routes to the settlement**, reached without `Paper_QuadraticStrain_v1` §4's equation, which §6 recorded as making the measure unscoreable. **The measure was scoreable after all; my seed error was less damaging than recorded.**

### The aggregation gap → 2/3, which changes its weight

GPT reached it independently: *“a radial integration of a constant gives `∝ R`, whereas the required contribution is `∝ \ln R`. To obtain the stated logarithm, the quantity being integrated must instead have an effective `1/R` dependence at the appropriate stage.”* **Two of three families, from the same material, with no contact. That is no longer one model's quibble — it is the run's most-converged finding**, and §4's scope correction to the sign check stands on firmer ground than when it rested on one report.

### The new finding: GPT reverse-engineered the required `Σ(R)` and got the sign wrong

**This is the most useful thing in the run, and it is evidence *for* the three-way check.**

GPT did what no other family did — it worked backwards from Part 3 to the `Σ(R)` P12 would need:

> *“`−dΣ_H/dR = −√(GMa₀)/R`, which integrates to `Σ_H = −√(GMa₀)\ln R + const`”*

and concluded `Σ(R) = −GM/R − √(GMa₀)\ln R`, *“so the target is mathematically consistent with P12.”*

**The integration flipped a sign.** From `−dΣ/dR = −k/R` it follows that `dΣ/dR = +k/R`, hence **`Σ_H = +k\ln R`, not `−k\ln R`.** Checked numerically: **GPT's stated `Σ` gives `a_r = +1.265473×10⁻¹⁴` — Newton attractive, MOND *repulsive* — contradicting the final line of its own derivation.** The correct landscape is `Σ = −GM/R + √(GMa₀)\ln R`, which is what `Note_SigmaC_SignCheck_2026-09-05.md` option 2 produces, and it matches the target to twelve digits.

**Why this matters more than a caught slip.** The three-way check was built because the `Coh`/`Str` assignment looked like a matter of taste. **An independent reader, attempting the same reconstruction analytically, got the sign backwards on the very term the check exists to settle** — and did not notice, because its final line quoted the right answer while its stated `Σ` gives the wrong one. **That is direct evidence that this sign is easy to get wrong by inspection and worth settling numerically.** It does not validate the *assignment* — nobody reached that — but it validates the *method*.

### Net, revised

**Confirmed:** the collision (3/3); the aggregation gap (2/3); the P04 route (1/3, independent); `Grad`'s Dirichlet form (1/3, independent, same tier). **Unreached:** the settled split (0/3). **Damaged:** the sign check's scope, unchanged from §4. **New:** the method behind the sign check is validated even though its conclusion is not — which is an odd result to have, and worth stating exactly that way.
