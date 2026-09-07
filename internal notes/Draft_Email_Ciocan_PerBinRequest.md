> # ⛔ WITHDRAWN 2026-09-07 — DO NOT SEND. The data is already public.
>
> **AP asked whether this email was worth sending at all** (*“very few people will reply, none reply twice. i doubt any will send data”*). Checking before answering settled it, and he was right to push back — though not for the reason he gave.
>
> **The catalogue is public.** MUSE-DARK III: *“All catalogues and data products from our disk–halo decomposition, including the RCs, can be found on the DARK website”* — **`https://dark.univ-lyon1.fr/data-releases/`**, MUSE UDF sample, 126 star-forming galaxies. **There was never anything to ask for.**
>
> **And the one question this draft would have added — whether molecular gas is in the baryonic budget — is answered in the paper's own text.** Their model is `a_bar = v_disk²/r + v_HI²/r (+ v_bulge²/r)`: **stellar disk, atomic gas, bulge, no H₂.** The authors state the consequence themselves: *“given typical molecular gas fractions of ∼30–50% at `z∼1`, this would introduce a systematic uncertainty of ∼0.2 dex in the total disk mass.”*
>
> **The lesson is cheaper than the email would have been: check whether the data is public before drafting a request for it.** Rusishvili's paper said it re-analysed *“Ciocan et al.'s own public catalogue”* — the word **public** was in the description I had, and I drafted a request anyway.
>
> **Kept, not deleted**, because the framing reasoning in it is sound and reusable, and because a withdrawn draft is part of the record.

---

# Draft email — MUSE-DARK III per-bin data request

**Status:** DRAFT, not sent. **2026-09-07.**

**To:** Bianca Ciocan and the MUSE-DARK team (corresponding author, per arXiv:2604.22613)
**Why this exists:** every reduction in `Paper_a0z_MONDScaleTracksHubbleRate.md` §5.3 is an approximation of one thing the authors already have and did not publish. A direct `a₀ ∝ H(z)^α` fit to the per-bin values would replace the whole conversion budget with a measurement.

---

## The framing decision, stated before the draft

**This asks for data. It does not mention Event Density, does not attach a paper, and does not propose a collaboration.** Three reasons, and the third is the real one:

1. A data request is a small favour between researchers and is answered on its own terms. A theory pitch is a large one and is answered on the theory's merits, which is a different conversation.
2. The request is legitimate independent of any framework: their published parametrisation is linear, and anyone testing a power-law model needs the per-bin table. That is true whether or not ED exists.
3. **The honest reason to want the data is that it could go against the prediction**, and a request that concealed the reason for wanting it would be worse than one that states it plainly. The draft says what the number is for.

**Do not send an ED paper in this first message even if the reply is warm.** If they ask what the model is, that is the moment.

---

## Draft

> **Subject:** Per-bin a₀(z) values from MUSE-DARK III — request for the tabulated data behind Fig. 3
>
> Dear Dr Ciocan,
>
> I read MUSE-DARK III with great interest — the ~30σ detection of evolution in the radial-acceleration-relation scale is a striking result, and the sample construction across 0.33 < z < 1.44 is impressive work.
>
> I am writing with a small data request. The paper reports the evolution through a linear parametrisation, a₀(z) = a₀(0) + a₁z with a₁ = 1.59 ± 0.1 × 10⁻¹⁰ m s⁻², and shows the binned values in Fig. 3. I am testing a model that predicts a specific power-law form, a₀ ∝ H(z)^α with α fixed at 1, and to compare it properly I need to fit that form directly rather than convert your linear fit into an exponent.
>
> I should be candid about why the conversion is not good enough. I have done it, and it is unstable in a way that makes it useless as a test: a straight line in z is not a power law in H(z), so the effective exponent implied by your fit is not constant — it runs from about 1.8 at z = 0.33 to about 0.9 at z = 1.44, and different defensible ways of collapsing that to a single number give answers spanning 1.12 to 1.18. Any exponent I quote is really a statement about my reduction choice, not about your data.
>
> If it were possible to share the tabulated per-bin values — a₀ per bin, the bin redshift ranges or effective redshifts, the number of galaxies per bin, and uncertainties, with the covariance if you have it — a direct fit would settle the question properly. Even the values and errors without covariance would be a large improvement on what I can do now.
>
> I would also be glad to know whether you regard the linear parametrisation as a description of the trend or as a preferred functional form, since that bears on how much weight the shape can carry.
>
> Any tabulated data would of course be credited to your team in anything that came of it, and I would be happy to share what the fit returns either way. To be straightforward about it: the prediction I am testing fixes α = 1 with no freedom to adjust it, so this is as likely to go against it as for it. That is rather the point of asking.
>
> Thank you for considering it, and congratulations on the result.
>
> Best regards,
> Allen Proxmire

---

## Notes on the draft

**Length.** Roughly 350 words. A cold data request that runs longer tends not to get read. Everything here is load-bearing; if it must be cut, the paragraph about the linear parametrisation's status is the one to lose.

**The one thing that makes this credible.** The third paragraph shows work already done and reports a result that is *inconvenient* — the conversion is unstable, so the requester cannot claim a clean answer from public data. **That is what distinguishes a researcher from someone fishing.** It also pre-empts the obvious reply, "the information is already in the paper."

**The 1.78 → 0.90 figure is the strongest thing in the message** and it is a genuine observation about their own fit, not about any model. If any single sentence earns a reply, it is that one.

**What is deliberately absent:** the framework's name, any claim about MOND or ΛCDM, the ~8% local match, and any mention of the tension being 2.3σ. All of that is a second conversation.

**Before sending:** confirm the correct corresponding-author address from the published paper rather than the arXiv listing, and check whether the journal or the team has a data-availability statement that already covers this — if a repository exists, the request should reference it rather than ask for a private transfer.
