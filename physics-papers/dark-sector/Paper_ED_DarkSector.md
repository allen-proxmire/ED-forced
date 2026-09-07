# The Event Density Account of Dark Matter: Two Culprits, One Mechanism

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — dark-sector flagship. A self-contained, cold-reader-accessible synthesis of ED's complete account of dark matter across galaxies, clusters, and the cosmic microwave background. It supersedes the earlier short mechanism note; the detailed relic construction lives in the companion `Paper_ED_RelicLagrangian_v1`.

**Status: synthesis / position paper, honestly tiered.** This paper does not derive new results; it assembles standing ED results into one account and states what each is (derived, standing, bounded, inherited, or open). The one derived headline it leans on, `ρ ∝ a⁻³` from commitment-irreversibility, is established in the companion construction and cited here.

**Anchors (the mechanisms this paper cites, not re-derives):** `Paper_029_a0` (a₀ = cH₀/2π), `Paper_QuadraticStrain_v1` (MOND as the interference cross-term), `Paper_030_CombinationRule`, `Paper_031_BTFR`, `Paper_KM-I_KhrononMOND`, `Paper_ED_RelicLagrangian_v1` (the relic Lagrangian, `ρ ∝ a⁻³`), `Paper_ED_Baryogenesis`, `Paper_MassWithoutMass_BindingInertia`, `Paper_ED_DF2_DF4_GroupSuppression`, `Paper_117_Bullet_TopologicalDefect`, `Paper_ED_Cos_03_CMBAcoustic`. Working record: `event-density/theory/Dark_Sector/`.

---

## Preamble — What This Paper Does NOT Claim

1. **No CMB spectrum is computed from ED.** The relic supplies the *kind* of component the acoustic peaks require; a full Boltzmann fit is owed and named as such (§4.5).
2. **The relic mass is inherited, not derived.** It is *consistency-bounded* to a warm ~keV window (§4, §6); ED derives no mass values, this one included.
3. **Two galactic small-scale puzzles are unaddressed** — the missing-satellite and satellite-plane anomalies (§3.4). ED has not engaged them; they are stated as an open gap, not resolved.
4. **This is a synthesis.** It cites mechanisms and does not re-derive them; the one genuinely new derivation the account rests on, the relic's `a⁻³`, is in the companion paper.
5. **No primitive-forcing is claimed.** "Derived" means conditional on the ED primitives plus the standard effective-field-theory reading; "standing" means a prior corpus result; "inherited" means a value ED does not fix.

---

## Abstract

"Dark matter" is one name for two distinct observations that the field has, for fifty years, assumed are one substance: the missing gravity in galaxies, and the gravitating, non-oscillating component the cosmic microwave background and galaxy clusters require. The assumption is economical and it fits the numbers, but it is an assumption, and it has been costly — it held MOND's precise galactic success hostage to its cluster and CMB failures, discarding a working account of one phenomenon for its inability to also explain a different one. Event Density separates the two, because in ED they have two different answers. The galactic effect is the **horizon**: MOND, read as the off-diagonal interference cross-term of gravitational strain between a local mass and the cosmic decoupling surface, with the scale a₀ = cH₀/(2π) supplied by that horizon and no dark-matter particle anywhere. The cluster and CMB effect is a **relic**: a committed neutral remnant from the same early process that made the baryons, uncharged and therefore decoupled, whose dilution as `a⁻³` is *derived* from the irreversibility of commitment. The two are one mechanism (the same bilinear interference cross-term) in two roles that differ only by whether the horizon is a partner, so ED is mechanism-unified but substance-separate: two culprits, not one. This paper walks the evidence, exhibit by exhibit, assigning each to its culprit and showing ED does not dodge it, including the Bullet Cluster (the relic, collisionless, sails through) and the CMB (the relic dust, spectrum not yet computed). It positions the account against its nearest published neighbor, superfluid dark matter (Berezhiani–Khoury), to which ED offers a first-principles a₀ and a mass-independent condensation criterion while reaching, by calculation, a two-component rather than a one-substance verdict. The distinctive, falsifiable bets are stated plainly: the MOND scale **evolves** as a₀(z) = cH(z)/(2π), a parameter-free shape ED cannot refit (the rate is fixed by the horizon-projection mechanism, not chosen) whose first decisive data (MUSE-DARK III, A&A 2026) confirm the evolution at ~30σ and exclude a constant a₀, vindicating ED's distinctive call against MOND, while mildly disfavoring ED's *exact* rate (the measured evolution runs somewhat faster than H(z)); dark matter is **warm**, not a cold WIMP; and galaxies contain **no dark-matter halo at all**. The honest ledger of what remains undelivered is stated with equal plainness.

---

## §1 — The charge: two crimes, one assumed suspect

Two different observations wear the same name.

The first is galaxies. Stars at the edge of a spiral orbit faster than the visible matter can hold them, and the excess tracks the ordinary matter with a precision, one acceleration scale and one tight relation, that has been measured for forty years. The second is the early universe. The pattern of the CMB acoustic peaks and the mass of galaxy clusters require a component that gravitates but does not slosh with the ordinary matter and light, settled into place before the first atoms formed, at roughly five times the baryon density.

For fifty years these have been treated as one substance: a single cold, invisible particle that solves both. The assumption is economical, it fits, and it is the whole reason "dark matter" is spoken of as a particle. But it is an assumption. The word bundled two problems together and then quietly claimed that one substance solves both, and the bundling was never evidence. It was an aesthetic preference, unification, wearing the costume of a logical requirement, and it has been epistemically expensive: when Milgrom's MOND fit galaxies precisely but failed at clusters and the CMB, the field's verdict was not "MOND is the galactic culprit and something else did the clusters," but "MOND fails, discard it for galaxies too." That is a broken inference. One does not acquit a proven culprit of the crime they plainly committed because a second, unrelated crime cannot also be pinned on them.

Event Density pries the two apart, because in ED they have two different answers. The thesis of this paper, stated once and defended through the rest: **there are two culprits, joined by one mechanism, and they are not the same substance.** One lives at the edge of the universe and acts on galaxies; the other was born at its beginning and acts on clusters and the CMB. The following section states the two culprits and the shared mechanism; the two after it walk the evidence and assign each exhibit; and the verdict states what would prove the account wrong.

## §2 — The two culprits, and the one mechanism

ED reads gravity, at the level of its substrate, as **quadratic in a participation amplitude** $P = \sqrt{b}\,e^{i\pi}$, where $b$ is the local event density and $\pi$ a phase. The quadratic participation form $\big|\sum_a P^{(a)}\big|^2$ then splits into a **diagonal** term (each source's self-potential, which is Newton) and an **off-diagonal** interference term between distinct sources (`Paper_QuadraticStrain_v1`, sharpening `Paper_030`). Both culprits are that same off-diagonal cross-term; they differ only in *who is interfering with whom*.

> **Notation aligned 2026-09-07 with the settled `Coh`/`Str` assignment.** The two terms named above are, in the canonical notation fixed by the three-way sign check (foundations #10, 2026-09-05):
>
> $$\mathrm{Str}_K = \sum_a b_K^{(a)} \ \ \text{(diagonal, Newton)}, \qquad \mathrm{Coh}_K = 2\!\!\sum_{a<b}\!\sqrt{b_K^{(a)} b_K^{(b)}}\,\cos\Theta_{ab} \ \ \text{(off-diagonal, MOND)},$$
>
> so that $\big|\sum_a P^{(a)}\big|^2 = \mathrm{Str}_K + \mathrm{Coh}_K$. **This paper previously called the whole quadratic form `Str`, which collided with that assignment.** *(Found by `internal notes/_check_cross_document_collisions.py` on its first real run.)*
>
> **The correction is to the NAME, not to the physics, and an earlier version of this flag said otherwise.** It claimed the old wording *“deletes the interference cross-term the gravity arc runs on”*. **It does not** — the sentence above splits the form and runs the entire argument on the off-diagonal term, which is exactly what the settlement assigns to `Coh`. **Deleting the cross-term is what the ruled-out reading would have done; this was never that reading.** The flag was written from the formula without reading the sentence around it, and is corrected here.

**The horizon (galaxies, no particle).** When a local mass interferes with the cosmic decoupling surface at $R_H = c/H_0$, the cross-term's modulus is the geometric mean $\sqrt{a_N\,a_0}$, with the scale
$$a_0 = \frac{c H_0}{2\pi}$$
supplied by the horizon and the factor $2\pi$ forced by the azimuthal-Fourier normalization of the dipole projection (`Paper_029`). This *is* MOND: the deep-field law and the tight galactic phenomenology, with nothing added and no particle present. There is no missing matter in a galaxy, only a piece of gravity, the interference of matter with the horizon, that was being missed. **Standing / structural.** **[DISPUTED 2026-09-04 — the `1/(2π)` is not established as forced.** The azimuthal-Fourier normalization does **not** survive: `Paper_028` §6.3 and `Paper_029` §5.1 both evaluate the azimuthal integral to **1**, so the factor cancels in their own displayed algebra and is reinstated at an assembly step by a normalization fixed nowhere. Re-tiered **Postulated / disputed**; see `Gravity_TieredClaims_Ledger.md` Staleness #10. **Unaffected:** `a₀ ~ cH₀`, reached three independent ways, and `a₀(z) = cH(z)/(2π)` with its forced exponent of 1.]**

**The relic (clusters and the CMB, a particle).** The early-universe component the peaks and clusters demand is a *matter* requirement, and ED supplies a native candidate: a **committed neutral relic**, the neutral-channel sibling of the baryons produced at the inflation/saturation exit by the same admission mechanism (`Paper_ED_Baryogenesis`), uncharged and so decoupled from light, and massive by binding, hence cold-capable (`Paper_MassWithoutMass_BindingInertia`). Its defining property is *derived*: because commitment is irreversible (P11), the relic carries a conserved comoving number, so its density dilutes as
$$\rho \propto a^{-3},$$
exactly the volume memory a modified-gravity dial structurally lacks (`Paper_ED_RelicLagrangian_v1`). It gravitates, it clusters, it is genuinely there. Its abundance is inherited, at the same tier as the baryon-to-photon ratio; its `a⁻³` is derived. **Derived (the `a⁻³`); form-complete / native (the candidate); value-inherited (the amount).**

**One mechanism, two roles.** Both culprits are the same bilinear cross-term of $P = \sqrt{b}\,e^{i\pi}$. Coarse-graining the relic's *self*-interaction from ED's real coherence kernel gives a canonical kinetic term, not the non-analytic deep-MOND one, because a cosine kernel is analytic and the relic's local self-pairing carries no horizon and hence no $a_0$ (`Paper_ED_RelicLagrangian_v1` §3.3). So the relic is ordinary (super)fluid cold dark matter, not a MOND source: the two roles differ precisely by whether the horizon is one of the interfering partners. ED is **mechanism-unified, substance-separate.** That is the two-culprit structure, and the rest of the paper is the case.

## §3 — Crime 1: the galactic exhibits (the horizon)

Galaxies are the horizon's jurisdiction, and in ED they contain no dark matter at all.

**3.1 Rotation curves.** Flat rotation curves, the original hint, are the deep-field limit of the horizon interference: $a \to \sqrt{a_N\,a_0}$ below $a_0$, reproducing the flat asymptotic velocity from the baryons alone (`Paper_KM-I`, `Paper_029`). No halo. The distinctive edge, developed in §6, is that $a_0$ is not a constant of nature but tracks the *instantaneous* Hubble rate.

**3.2 The Tully-Fisher conspiracy.** The baryonic Tully-Fisher relation, $v_{\rm flat}^4 = G M a_0$, slope exactly four with near-zero scatter, is what Khoury rightly calls a conspiracy: the visible matter dictates the asymptotic velocity with a precision a scattered dark-matter halo should not allow. In ED it is an exact consequence of the combination rule (`Paper_031`). Honesty requires a distinction here: the slope-4 and the tightness are *MOND-shared*, so they discriminate ED-and-MOND from ΛCDM, not ED from MOND; the one ED-distinctive claim in this exhibit is the normalization $a_0 = cH_0/(2\pi)$, a parameter-free ~10% match. **Standing (BTFR); the distinctive part is the a₀ normalization.**

**3.3 DF2 and DF4, the "dark-matter-free" galaxies.** Two ultra-diffuse galaxies whose kinematics match their baryons alone, famously awkward for a theory that boosts gravity everywhere. ED recovers the external-field effect through a native mechanism: both sit deep inside the NGC 1052 group, whose external field dominates their internal one and saturates the substrate's finite outer-scale capacity, so the horizon enhancement is locally spent and the internal dynamics go Newtonian (`Paper_ED_DF2_DF4_GroupSuppression`). ED's reading is in fact cleaner than the puzzle assumes: since *no* galaxy carries a dark-matter halo in ED, "dark-matter-free" is universal, not special; what is special about DF2/DF4 is only that they are *Newtonian rather than MOND*, which is the external-field effect. The distinctive prediction is a *sharper*, knee-like suppression than MOND's smooth roll-off. **Structural; the suppression function is not yet derived (an open number, §6).**

**3.4 The small-scale puzzles — an open gap, stated plainly.** Two anomalies Khoury raises, the missing-satellite problem and the planar arrangement of satellite galaxies around the Milky Way and Andromeda, are *not* addressed by ED. MOND has partial phenomenological answers; ED has engaged neither. They are galactic, so they fall in the horizon's jurisdiction, but no ED mechanism has been worked out for them. This is a genuine gap in the galactic account, recorded here rather than skipped. **Open.**

## §4 — Crime 2: the cluster and CMB exhibits (the relic)

Clusters and the early universe are the relic's jurisdiction, and here ED does have a particle.

**4.1 The cluster missing mass.** Galaxy clusters need more gravity than their galaxies and hot gas provide, and MOND-class theories characteristically under-predict cluster masses by about a factor of two, the shortfall that has always been the honest weak point of modified gravity. In ED that shortfall is filled by the relic, real collisionless matter clustering at cluster scale (`event-density/theory/Dark_Sector/DarkSector_DebtMap`; `Paper_KM-II` §8). The same warm-keV window that keeps the relic diffuse in galaxies (so it does not spoil the horizon account there) keeps it clumped at cluster scale, so its cluster and galactic roles do not conflict, though that window is narrow and is itself the sector's live risk (§6).

**4.2 The Bullet Cluster.** The most-cited single piece of evidence for particle dark matter: two galaxy *clusters* collided, the hot gas (most of the visible mass) was slowed by ram pressure and stranded in the middle, and gravitational lensing places the mass off to the sides with the galaxies. In ED this is the relic doing what collisionless matter does. Being neutral, the relic feels no ram pressure; it sails through the merger with the galaxies while the gas is stripped, and the lensing follows the relic, offset from the gas. This is the same account ΛCDM gives, and it requires no exotic mechanism, because at cluster scale the relic *is* collisionless dark matter. ED does not compute the Bullet anew; it *inherits* the standard collisionless-dark-matter account, and what it contributes is the relic itself, a native reason for that collisionless component to be present. ED also carries a distinctive *if-present* bonus signal here: a substrate-quench mechanism predicts a sharp offset-velocity knee across the merging-cluster population (`Paper_117`, repositioned), which the relic account alone does not, but that is a bonus, not the primary explanation. **The relic account is ΛCDM-grade; the offset-velocity knee is a speculative bonus.**

**4.3 Gravitational lensing.** Cluster lensing follows the total mass, dominated by the relic, so ED lenses as ΛCDM does. Two ED-distinctive lensing statements sit alongside: no gravitational slip beyond $O(\Phi)$ (the metric-only coupling has no vector field to repair one with), and an activity-dependent weak-lensing enhancement in dynamically disturbed systems (`Paper_038_6`, provisional). **Relic gravitates (standing); the slip and activity signatures are ED-distinctive.**

**4.4 The cosmic web.** Large-scale structure, the filaments and clumps of the dark-matter simulations, is the relic clustering under gravity from the primordial spectrum (`Paper_ED_Cos_04`). As a warm relic it suppresses power below its free-streaming scale but forms the web above it, the standard warm-dark-matter picture.

**4.5 The CMB acoustic peaks — the owed computation.** The peaks require a component that gravitates but does not oscillate with the photon-baryon fluid, decoupled and diluting as `a⁻³` at ~5× the baryons. That is precisely the relic (`Paper_ED_Cos_03`; `Paper_ED_RelicLagrangian_v1`). But honesty is load-bearing here: **no CMB spectrum has been computed from ED.** The current cosmology papers inherit the standard `Ω_c` value inside a standard Boltzmann code; the relic gives that value a native field-theoretic home and a derived `a⁻³`, but the peaks themselves have not been computed from the relic action. The owed calculation is an AeST-style Boltzmann run (Skordis–Złośnik being the sister-theory existence proof that a relativistic-MOND-class model *can* fit the peaks), and it is the sector's headline undelivered piece. **Open (well-specified).**

## §5 — The nearest published rival: superfluid dark matter

The closest published, peer-reviewed idea to this two-component picture is the **superfluid dark matter** of Berezhiani and Khoury (2015), and ED is best located by contrast with it. The comparison is worth making generously, because ED shares that program's central instincts and, on two specific points, has something concrete to offer it.

**What ED shares with it, and offers it.** Both hold that MOND is a real, fundamental fact about galaxies rather than a star-formation artifact; both reach for coherence and condensation as the language; and both keep real dark matter for the large scales while splitting galaxies from clusters by a temperature-like criterion (ED's thermal-decoherence split independently reproduces exactly that galaxy-cold, cluster-hot division). On two points ED contributes something the superfluid program takes as input. First, a **first-principles a₀**: where superfluid DM fits the MOND scale into its phonon Lagrangian, ED derives $a_0 = cH_0/(2\pi)$ from the horizon. Second, a **mass-independent condensation criterion**: ED's condensation is coherence-driven rather than de Broglie-driven, which relaxes the light-boson mass tension the superfluid picture must otherwise carry.

**Where ED diverges, and why.** The programs part on their central claim. Superfluid DM is *one substance*: the dark matter's own superfluid phonon mediates the MOND force, so dark matter and MOND are two phases of one thing. ED tested exactly this route and, by coarse-graining its real coherence kernel, found the relic's collective mode comes out *canonical*, not the MOND kinetic term, so ED lands on **two components**, not one substance (§2). This is a calculated verdict offered as a result to compare notes on, not a refutation of their program. The clean observational discriminator between the two pictures is direct: superfluid DM has real dark-matter substance *inside* galaxies (a halo with a superfluid core, carrying vortices and reduced dynamical friction); ED has **none** — galaxies are pure horizon-MOND. Whether a galaxy contains dark-matter substance or only MOND is the question that separates the two, cleanly and eventually observably.

## §6 — The verdict: the distinctive bets and the honest ledger

**The weapons.** The account makes bets that single ED out from both ΛCDM and MOND:

- **The flagship bet — the MOND scale evolves: $a_0(z) = cH(z)/(2\pi)$.** Because $a_0$ is the horizon read live, it tracks the instantaneous Hubble rate, so $a_0(z)/a_0(0) = H(z)/H_0$. This is not a constant of nature (MOND) nor absent (ΛCDM), and it is *unfudgeable*, though not by dimensional necessity: ED does carry a second length scale ($\ell_P$), so a bent power would be dimensionally legal, but the horizon-projection that sets $a_0$ (Paper_029) introduces no $\ell_P$, and ED's no-intrinsic-scalar result leaves no free dimensionless number available to bend the power, so the rate is fixed at exactly $\propto H(z)$ and ED cannot refit it the way MOND refits its constant. The first decisive data are in hand and split the verdict cleanly. **The distinctive call is confirmed:** MUSE-DARK III (A&A 2026) detects evolution of the acceleration scale across $0.33<z<1.44$ at ~30σ, with $a_0$ rising from $1.2\times10^{-10}$ locally to $\sim 2.4\times10^{-10}\,\mathrm{m/s^2}$ by $z\sim1$, which excludes a constant $a_0$ and kills MOND's constant-scale picture. **The exact rate is in mild tension:** the paper reports the evolution running *faster than $H(z)$*, whereas ED's forced prediction is exactly $H(z)$, so ED's rate is somewhat too slow (a tension of order one to a few sigma on one first-generation survey, with high-$z$ systematics and modeling still to be pinned). ED got the direction right where MOND got it wrong, and owns a real, unfudgeable rate that the next surveys (Rubin, Euclid) will confirm or break. (Not to be confused with its companion: dark energy's Λ is the *frozen* horizon and does not evolve; that is a separate box, the dark-energy sector, not this bet.)
- **Dark matter is warm (~keV), not a cold WIMP.** Two-component consistency bounds the relic to a warm window; a cold heavy WIMP detection, or perfectly cold dark matter, refutes the picture.
- **Galaxies contain no dark-matter halo at all.** Cold-dark-matter fingerprints inside galaxies (cusps, a scattered halo mass distribution) would refute the horizon account.
- **DF2/DF4 show a sharper external-field knee than MOND**, and the Bullet population may show the offset-velocity knee (a bonus, not required).

**The honest ledger.** What the account does not yet deliver, stated as plainly as the bets:

- **No CMB spectrum computed** from the relic action (§4.5) — the largest owed piece.
- **The relic mass is inherited**, bounded to warm ~keV but not derived; ED derives no mass values.
- **The galactic small-scale puzzles are unaddressed** (§3.4).
- **The DF2/DF4 suppression function is not derived** (§3.3), only estimated.

## §7 — Falsifiers

- **F1.** A direct dark-matter particle detection that is *cold and heavy* (a WIMP), or a demonstration that dark matter is perfectly cold — refutes the warm relic.
- **F2.** Dark-matter substance found *inside* galaxies (a halo, cold-DM cusps, a scattered mass distribution) — refutes the horizon-only galactic account.
- **F3.** The MOND scale shown *constant* with redshift, $a_0(z) = a_0(0)$ — refutes the flagship $a_0(z)$ bet. (The first data instead detect evolution and exclude constant $a_0$; the live tension is on the exact rate, which the data prefer *faster* than ED's forced $\propto H(z)$, so a robustly confirmed rate incompatible with $H(z)$ would also refute the exact bet, though not the evolution.)
- **F4.** The interference reading of MOND shown inconsistent with lensing or the classical tests where GR-I..IV succeed — the $\sqrt{a_N a_0}$ derivation collapses.
- **F5.** The relic's conserved commitment number shown *not* to be ED-native — the `a⁻³` headline collapses and the relic loses its advantage over a modified-gravity dial.
- **F6.** A computed CMB spectrum from the relic action that misses the Planck peaks for every mass in the warm window.

## §8 — Tiers

| Claim | Tier |
|---|---|
| Galactic dynamics from MOND/horizon, no particle | **standing** (KM-I / 027–034) |
| MOND is the off-diagonal horizon-interference cross-term; `√(a_N a₀)` forced | **standing / structural** (QuadraticStrain, Paper_030) |
| a₀ = cH₀/(2π) matches, parameter-free | **derived, ~10% postdiction** (Paper_029) |
| **a₀(z) = cH(z)/(2π) evolution** | **derived, unfudgeable shape; evolution CONFIRMED ~30σ (MUSE-DARK III, A&A 2026), kills constant-a₀ MOND; exact rate ∝H(z) in mild tension (data run faster)** (flagship) |
| Committed neutral relic for clusters/CMB | **form-complete / native** (Baryogenesis + MS-II + binding mass) |
| Relic `ρ ∝ a⁻³` from the P11 commitment number | **derived** (RelicLagrangian) |
| Sector is two-component, not one substance | **derived** (L_self coarse-graining canonical) |
| Bullet offset via the relic (collisionless) | **inherited mechanism** (the relic is native; the ΛCDM-class collisionless account is inherited, not re-derived); the offset-velocity knee is a **speculative bonus** |
| Relic warm, ~0.2–0.7 keV | **consistency bound**; mass value **inherited** |
| Cluster shortfall filled by the relic | **structural** |
| DF2/DF4 external-field suppression | **structural**; suppression function **open** |
| Galactic small-scale puzzles | **open / unaddressed** |
| CMB spectrum from ED | **not done** |

## §9 — Position

Event Density's account of dark matter is not "no dark matter," and it is not one substance doing every job. It is **two culprits joined by one mechanism.** Gravity's own strain, read as interference of the participation amplitude, is Newton on its diagonal and MOND on its off-diagonal with the horizon, so galaxies are explained with no dark-matter particle at all. A committed neutral relic, the neutral-channel sibling of the baryons, supplies the decoupled `a⁻³` dust the clusters and the CMB demand, with that `a⁻³` derived from the irreversibility of commitment rather than assumed, and the Bullet Cluster falls out of it as plainly as it does in ΛCDM. The relic is not MOND, because its self-interaction coarse-grains to a canonical mode with no horizon in it, so the two roles are the same interference structure with different partners. The account makes distinctive, falsifiable bets, chief among them that the MOND scale evolves with the Hubble rate, a bet whose first data confirm the evolution and bury constant-scale MOND, and it is candid about the debts it has not paid, chief among them a CMB spectrum it has not computed. The word "dark matter" was covering two different things. Separating them is not a loss of the idea but a clarification of it: one culprit at the edge of the universe, acting on galaxies; the other born at its beginning, acting on the cosmic web. The case is that they were never the same, and that a framework which keeps them apart, and stays candid about the debts it has not yet paid, is a more honest reading of the evidence than one which held them together because a single substance was tidier.

---

*Dark-sector flagship; a self-contained, evidence-first account (companion construction: `Paper_ED_RelicLagrangian_v1`; working record: `event-density/theory/Dark_Sector/`). Standing: MOND as horizon interference. Derived: the relic's `a⁻³` from P11; the sector two-component. Bounded: the relic warm, ~keV. Inherited: the relic mass and abundance. Open: the CMB spectrum, the galactic small-scale puzzles, the DF2/DF4 suppression function. The flagship bet is that the MOND scale evolves, a₀(z) = cH(z)/(2π).*
