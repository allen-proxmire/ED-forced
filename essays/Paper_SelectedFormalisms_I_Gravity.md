# Selected Formalisms from the Event Density Framework
## I. Gravity and the Cosmic Acceleration Scale

**Allen Proxmire**
*2026-08-18. §1–§9 complete; QC and referee passes applied; the §6 QuadraticStrain wording verified against the source. Every tier label is transcribed from the gravity and foundations tiered-claims ledgers, not inflated.*

---

## Abstract

Event Density (ED) posits a discrete substrate of *events*, specified by thirteen postulated primitives, and treats the smooth laws of physics as coarse-grained averages over it. The keystone of the substrate is the irreversible *commitment* of events, the arrow of time made physical. This paper works one sector end to end. From the primitives we obtain, in order: a holographic edge-count on closed surfaces; Newton's law from a cumulative-strain reading of that count; the weak-field Einstein metric with the correct factor-of-two light bending; the deep-MOND combination $a = √(a_N·a₀)$; and the acceleration scale $a₀ = cH(z)/2π$. We are explicit about tiers throughout: the *forms* are derived (each conditioning postulate named), while the *magnitudes* of $G$ and $a₀$ are inherited through $ℓ_P$ and $H₀$; the emergent metric is the kinematic weak field (the nonlinear regime is open), and ED gravity is *khronometric*, not pure general relativity. The sector ends on a falsifiable, zero-dial prediction: the MOND acceleration scale is not a constant but tracks the cosmic expansion rate, $a₀(z) = cH(z)/2π$. A 2026 survey (MUSE-DARK III) excludes a constant $a₀$ at ≈30σ (a bar any evolving-scale model clears) and confirms ED's evolution in direction, while mildly disfavoring the ED-distinctive rate $α = 1$ (a ≈1–2σ tension once systematics are folded in). We state what the sector does *not* deliver, and point to the full corpus for the remaining sectors and their tiers.

---

## 1. The substrate and its primitives

Event Density (ED) is a substrate ontology. Beneath the continuous fields and smooth spacetime of established physics it posits a discrete, graph-like layer of *events*, and it treats the familiar continuum laws as coarse-grained readings of that layer. This paper does not argue for the substrate from first principles. It takes the substrate as given and works one sector, gravity, through to a falsifiable prediction, stating at each step exactly what is derived and what is inherited.

**Postulated, not derived.** The substrate is specified by thirteen primitives, P01–P13 (Paper_087). They are *postulated*, not derived from a deeper layer, and ED makes no claim that they are minimal or unique. In this respect ED's epistemic standing is that of the substrate-ontology programs it sits beside: the causal-set program and 't Hooft's cellular-automaton interpretation, which posit a discrete substrate and argue from its downstream reach. It is *not* the operational-reconstruction tradition (Hardy; Chiribella–D'Ariano–Perinotti; Masanes–Müller), which derives quantum theory from operational axioms by closed proof. Every result below is therefore a *conditional structural derivation*: given the thirteen primitives, plus the kernel inheritance named below, the stated consequence follows. Removing a load-bearing primitive breaks the derivation.

**The primitives this sector uses.** The gravitational chain rests on a subset of the thirteen (Paper_087 §7): the participation of chains in channels (P02); channel and locus indexing with spatial homogeneity (P03); bandwidth as a non-negative additive scalar, $b_K(u) ≥ 0$ (P04); spatial dimension $D = 3+1$ (P06); channels as ontological primitives (P07); the substrate scale $ℓ_{ED}$ (P08); a stability landscape $Σ_C$ whose negative gradient along the chain's adjacency direction is its acceleration (P12); and time homogeneity (P13). Two of these carry unusually heavy load, and we flag them where they bite: P06, because the $4πR²$ area and the inverse-square law are dimensional facts about three space dimensions, and P08, whose *value* is inherited rather than derived (below).

**The arrow.** One primitive is the keystone of this paper's story, and it deserves to be stated precisely rather than in shorthand. P11 (commitment irreversibility) is the substrate event at which a chain's multi-channel participation collapses to a single channel, the unselected phases are randomized, and no substrate operation returns the post-commitment state to the pre-commitment one. The one-way character of the substrate, the arrow, is supplied *jointly* by P11, time homogeneity (P13), and the strictly retarded support of the participation kernel V1 (Theorem T18, Paper_093); ED does not claim the arrow reduces to any one of these alone. Where a popular account of ED calls commitment "the tick of time," this is its precise content: an irreversible substrate event, forward-supported at the kernel level.

**Form-derived, value-inherited.** ED separates two kinds of result, and the separation governs every claim in this paper (Paper_095). The *form* of a law (its functional shape, its exponents, and its structural constants such as the factor of two in light bending or the $1/2π$ in the acceleration scale) is a structural consequence of the primitives. Its *magnitude* is frequently *inherited* from measurement: Newton's constant $G$, the substrate scale $ℓ_{ED}$, the acceleration scale $a₀$, and the cosmological constant each carry an empirically fixed number, not a substrate-derived one. We say so at each occurrence. A form-derivation that reproduces a tested law is a genuine result; it is not the stronger claim that ED computes the law's dimensional magnitude from nothing.

**Coarse-graining.** Finally, the continuum objects of this paper (a metric, a Newtonian potential, a MOND interpolation) are not substrate primitives. They are the coarse-grained reading of substrate participation, obtained when the hydrodynamic-window scale separation holds (the direct coarse-graining transport, DCGT). The smooth, time-symmetric appearance of those laws is a property of the average, not of the substrate beneath it; the substrate is discrete and one-way. With that established, the sector proceeds: from the edge-count on a closed surface (§2) to Newton (§3), the weak-field metric (§4), the acceleration scale (§5), the deep-MOND law (§6), and the prediction that the scale evolves with cosmic time (§7).

---

## 2. A count on a surface: the holographic participation bound

Gravity, in ED, is a reading of how a localized source distributes its participation across the substrate channels that reach a distant test chain. Before any dynamics, then, we need a count: how many distinct channels connect a source at one locus to a test at substrate distance $R$? This section fixes that count. It is pure substrate geometry (no arrow, no commitment enters yet), but it is where the inverse-square law comes from, and it is the first place ED reaches a result usually attributed to black-hole thermodynamics.

**The result.** For a source region and a test chain at separation $R$, the number of distinct substrate channels connecting them is bounded by

> $N(R) ≤ 4πR² / ℓ_{ED}²$   (Paper_025).

**Tier: Derived, conditional on two named postulates (P-Codim-1, P-Sat); the scale $ℓ_{ED}$ is value-inherited.** We give the derivation, then say exactly what "derived" is conditional on.

**Derivation.** Four substrate facts and one combinatorial step.

1. *Channels are the only cross-locus mechanism.* By P02 (participation) and P07 (channels as ontological primitives), a source's influence on a distant test proceeds through some set of substrate channels; the substrate has no other primitive way for one locus to affect another.
2. *They must cross an enclosing surface.* Place a closed 2-surface $Σ_R$ at substrate distance $R$ around the source. Any channel from the interior source to an exterior test must cross $Σ_R$, the substrate-graph version of the ordinary topological fact that a path from inside a closed surface to outside it crosses the surface (P03 supplies the translation-invariant adjacency). So the number of source-to-test channels is bounded by the number crossing $Σ_R$.
3. *The surface has area $4πR²$.* By P06 (three spatial dimensions), $Σ_R$ is the substrate-graph 2-sphere of radius $R$, whose coarse-grained area is $4πR²$. This factor is a dimensional fact about three space dimensions; in $D$ spatial dimensions the surface scales as $R^(D−1)$, and the whole bound with it.
4. *Channels are resolved at $ℓ_{ED}$.* By P08, the substrate has a finite discretization scale $ℓ_{ED}$; two channel-crossings closer than $ℓ_{ED}$ on the surface are the same channel.

The combinatorial step is area divided by footprint, and here the one substantive assumption enters. A channel's footprint on $Σ_R$ is $ℓ_{ED}²$ only if channels are **codimension-1** substrate objects, so that a crossing occupies a two-dimensional patch of the surface with linear extent $ℓ_{ED}$ in each tangent direction. That is P-Codim-1, a postulate about what a channel *is*. It is not derivable from P02 and P07, and it is load-bearing: codimension-2 channels would give a footprint $ℓ_{ED}$ and a bound $∝ R²/ℓ_{ED}$, a different law with different consequences. Granting it,

> $A_{footprint} = ℓ_{ED} · ℓ_{ED} = ℓ_{ED}²$,   so   $N(R) ≤ 4πR² / ℓ_{ED}²$.

Equality holds in the substrate-saturated regime (P-Sat), where every $ℓ_{ED}²$ patch carries exactly one channel. This is the regime the source-influenced substrate near a mass approaches, and the one Paper_027 uses when it turns the bound into an equality.

**What this is, and is not.** The bound has the same area-scaling form as the Bekenstein–Hawking entropy bound, $S ≤ A/4ℓ_P²$, and under the later identification $ℓ_{ED} = ℓ_P$ (§3) the numerical scales agree up to the order-unity coefficient (1 versus 1/4). We claim no more than that. ED reaches the area law by counting substrate channels on a surface, not from black-hole thermodynamics, so the agreement is cross-domain coherence, not a derivation of the holographic principle and not an identity, and what is bounded is a *channel count*, not an entropy. The magnitude that makes the two scales coincide, $ℓ_{ED} = ℓ_P$, is inherited from matching Newton's constant (§3), not computed.

The one fact to carry forward is the scaling: **$N(R) ∝ R²$** in three dimensions. That single fact, fed through the participation kernel in §3, is what makes gravity fall off as $1/R²$.

---

## 3. Newton from a cumulative-strain reading

Put a localized source on the substrate and ask what a distant test chain feels. The test chain carries P12's stability landscape $Σ_C = Coh − Str − Grad$, and its acceleration is the negative gradient of that landscape along its adjacency direction. In the Newtonian regime the variation that matters is the strain sourced by the distant mass, read through the participation kernel V1. This section shows that reading returns $Φ = −GM/R$ and $a_N = GM/R²$, and identifies $G = c³ℓ_{ED}²/ℏ$. Two honesty notes travel with it: one *choice* (how P12's strain is read) and one *inheritance* (the value of the scale).

**Tier: Newton's law is Derived, conditional on P-Potential-Reading (a substrate-level choice) plus the §2 postulates; the V1 $1/R$ envelope is inherited; and $G$'s magnitude is value-inherited via $ℓ_{ED} = ℓ_P$.**

**Per-channel potential.** At separations $R ≫ ℓ_{ED}$ the V1 kernel's coarse-grained envelope falls off as $1/R$, a Coulomb-like envelope inherited from the direct coarse-graining transport (Paper_073), not derived here. Under the potential reading of P12 (P-Potential-Reading), a single channel carrying source content $σ_{ch}$ contributes

> $Φ_{ch}(R) = −κ_{V1} · σ_{ch}(M) / R$,

with $κ_{V1}$ the V1 coupling and the sign attractive. P-Potential-Reading is a genuine choice: the source (Paper_026 §3.4) flags a substrate-consistent alternative it does not pursue, its "Model B," a per-channel-modulation reading. ED commits to the potential reading and labels it a choice rather than burying it.

**The source distributes, it does not duplicate.** This is the load-bearing step, and it is where §2's count re-enters. The source content $σ(M)$ is one fact about the source, not a separate copy seen by each channel. By P03 (no preferred channel) and P07 (each channel carries a definite fraction), it distributes uniformly across the `N(R)` channels crossing $Σ_R$:

> $σ_{ch}(M; R) = σ(M) / N(R)$.

**The count cancels.** Summing the per-channel potential over the `N(R)` channels,

> $Φ(R) = N(R) · Φ_{ch} = N(R) · ( −κ_{V1} · [σ(M)/N(R)] / R ) = −κ_{V1} · σ(M)/R$.

The `N(R)` factors cancel exactly, and that cancellation is the entire mechanism. It is worth saying plainly why the inverse-square law is *not* "a competition between an $R²$ surface and a $1/R$ kernel." That appealing story gives the wrong answer ($Φ ∝ R$). The count sets *how many channels the source spreads over*; the kernel sets *how each channel contributes*; the two multiply in the per-channel coefficient and cancel in the sum, leaving one Coulomb-like potential. Identifying $κ_{V1}·σ(M) = GM$,

> $Φ(R) = −GM/R$,   $a_N(R) = −dΦ/dR = GM/R²$.

That is Newton's law, and its $1/R²$ form is the three-dimensional fact $N(R) ∝ R²$ from §2 run through the kernel. In $D$ spatial dimensions the same construction gives $1/R^(D−1)$; the inverse square is P06 showing up again.

**Newton's constant.** Dimensional analysis leaves a unique combination of the available substrate constants $c$, $ℏ$, $ℓ_{ED}$ with the dimensions of $G$:

> $G = c³ ℓ_{ED}² / ℏ$.

Here the honesty matters most, because this is the kind of result easiest to oversell. The relation is the standard Planck-length definition $ℓ_P = √(ℏG/c³)$ read backwards. ED does not compute the *number*: the substrate scale $ℓ_{ED}$ is postulated (P08), and matching the measured $G$ fixes $ℓ_{ED} = ℓ_P ≈ 1.6×10⁻³⁵ m$, a value-inherited quantity. What ED *adds* is the structural reframing (a single postulated scale $ℓ_{ED}$, with $G$ downstream of it through the mechanism above) so that $G$ stops being an independent dial and the count of free constants drops by one. That is the claim: $G$'s form is derived and it is demoted from primitive to downstream; its magnitude is inherited. Nothing here computes gravitational strength from nothing, and this is the Newtonian limit only. The field equations are §4's concern, and there only in the weak field.

---

## 4. The weak-field Einstein metric

So far there is no metric, only a channel count and a Newtonian potential. This section builds the emergent metric and shows it is the weak-field Schwarzschild metric, recovering the three classical tests including the factor of two in light bending. The honesty that governs the section: the metric is a coarse-grained object, not a fundamental field; the result is weak-field only; and ED gravity is not pure general relativity but *khronometric*: Einstein's tensor sector plus a preferred-foliation scalar inherited from the arrow. It coincides with GR in the regime treated here and departs from it elsewhere.

**The spatial metric.** Bandwidth measures coupling capacity: more bandwidth, shorter metric distance. The emergent spatial metric is the inverse bandwidth field,

> $g_{ij} ∼ b⁻¹$   (Paper_GR-I §3).

It is symmetric (reciprocal edges, P02), positive in the bulk, and degenerates exactly where $b → 0$, at the emergent horizons ED locates independently. Tier: Derived; it is the explicit realization of the acoustic metric that an earlier paper had only postulated.

**The lapse.** The new content is the time component. The substrate front, the locus of new commitments, is the fastest signal, so in the emergent metric it rides the null cone, $ds² = 0$. It advances $Γ$ edges per tick, and by P-Commitment-Linear the commitment rate is linear in bandwidth, $Γ ∝ b$. Putting the front on the null cone of $ds² = −N²dt² + b⁻¹dx²$,

> $0 = −N² + b⁻¹·Γ² = −N² + b⁻¹·b²  ⟹  N² ∼ b$.

**Tier: Derived, conditional on P-Commitment-Linear.** That postulate is load-bearing and honestly labeled: with $Γ ∝ b^α$ the lapse is $N² ∼ b^(2α−1)$, and $α = 1$ is what selects the Einstein branch over the conformal (Nordström) one. ED argues linearity is the natural reading (the commitment rate should rise with available bandwidth, not fall), and a companion paper (GR-III) later forces it from the reserve law, but in this derivation it is a postulate.

**The Schwarzschild relation and the metric.** With $g_{00} = −N² ∼ −b$ and $g_{rr} ∼ b⁻¹$,

> $g_{00} · g_{rr} ∼ (−b)(b⁻¹) = −1$,

the Schwarzschild relation, signature of the Einstein branch (the conformal branch would need $N² ∼ b⁻¹$). The inherited Newtonian limit gives $∇²b ∼ ρ$, hence $b = 1 − r_s/r$ in vacuum, and the metric assembles to $g_{00} = −(1 − r_s/r)$, $g_{rr} = (1 − r_s/r)⁻¹$, the weak-field Schwarzschild metric, now built rather than assumed.

**The factor of two.** Light follows the optical index $n_{opt} = √g_{rr} / N ∼ b^(−1/2)/b^(1/2) = b⁻¹$, the *square* of the spatial-only index $b^(−1/2)$. Since $ln(b⁻¹) = 2·ln(b^(−1/2))$, the deflection is exactly twice the Newtonian value, $α = 2r_s/ξ$, the Einstein result. An eikonal ray-tracer confirms it: Einstein/Newtonian ratio 2.09, conformal control exactly zero. **Tier: Derived + simulation.** The reason is structural and worth stating: one field $b$ sets both the spatial metric and the lapse, so space curves as much as time and in the same sense. Relativistic-MOND covariantizations such as TeVeS had to bolt on a vector field to install that spatial curvature; ED gets it from the single bandwidth field. Gravitational redshift ($N ∼ b^{1/2}$) and perihelion precession (for test particles in the metric) follow as corollaries.

**What is and isn't claimed.** The emergent metric coincides with general relativity at weak field, which is why the three classical tests come out right. It is not the full Einstein equations (the field-equation form and the nonlinear regime are a companion paper's business, and the strong-field metric is open), and it is not pure GR: the same lapse mechanism that gives the factor of two carries a preferred foliation, so ED gravity is khronometric. That class has a sharp, favorable consequence carried in the companion papers: the tensor sector propagates at $c_T = c$ structurally (clean against the GW170817 bound) and the preferred-frame parameter $α₂ = 0$ exactly. Those are stated here, not derived. The metric of this section is the weak field: kinematic, coarse-grained, and honest about where it stops.

---

## 5. The cosmic crossover and the acceleration scale a₀

Here the arrow finally does work. Newton (§3–4) used only the local source. This section brings in the cosmos, and the mechanism turns on commitment being forward and finite-speed: content from far enough away is outrun by the expansion and never coherently reaches a local chain. That sets a scale, and the scale is the MOND acceleration $a₀$.

**The decoupling surface.** Substrate content propagates at speed $c$; the Hubble flow carries two points apart at $H₀R$. Where these rates match,

> $c = H₀ R_H  ⟹  R_H = c/H₀$,

is the cosmic decoupling surface, the radius beyond which kernel-mediated content cannot keep up with the expansion. It is a substrate-level effective horizon, not the GR event horizon.

**The dipole and the 2π.** For a chain at rest this surface is isotropic. For an *accelerating* chain the acceleration singles out an axis, breaking the adjacency's `SO(3)` to a residual `SO(2)`, and the leading anisotropic response is the dipole. Projecting the horizon's dipole content onto that residual `SO(2)` is an azimuthal Fourier projection on a circle of period $2π$, whose orthonormal normalization carries a factor $1/(2π)$. The induced acceleration is

> $a₀ = cH₀ / (2π)$   (Paper_029 §5.1).

**Tier: form-forced (Derived given the dipole projection and Fourier normalization); $H₀$ is value-inherited.** The $1/(2π)$ is the honest structural core: the canonical Fourier normalization on the $2π$-period `SO(2)`, not a fit, and a different factor ($1/4π$, $1/π$) would be a different mode. To be exact about what is derived: the $2π$ and the $cH₀$ scaling are structural, and nothing else is. The remaining polar and substrate normalizations are order-unity factors the source sets so their product closes to unity, and it is the ~10% empirical match, not an independent computation, that confirms they do. A skeptical reader is entitled to call that O(1) closure partly anchored to the answer; the load-bearing structural content is the $2π$ factor and the $cH₀$ scaling, not the unit coefficient.

**The number.** With $H₀ ≈ 70 km/s/Mpc$,

> $a₀ = cH₀/(2π) ≈ 1.08 × 10⁻¹⁰ m/s²$,

against the measured MOND scale $≈ 1.2 × 10⁻¹⁰ m/s²$, a ~10% match with **zero free parameters**. That $a₀ ≈ cH₀$ has been noticed for decades as a hint of a cosmological connection; ED supplies the mechanism and fixes the coefficient. Two honesty lines travel with it: $H₀$ is inherited, not derived, and ED derives the transition *scale*, not the full MOND interpolation function $μ(x)$.

The identification carries a sharper consequence than the number, and it is this paper's payload: because $a₀$ reads the horizon $R_H = c/H$ at whatever epoch you evaluate it, $a₀$ cannot be a constant of nature. That is §7.

---

## 6. The deep-MOND combination

Newton (§3) and the acceleration scale (§5) are the two ingredients; this section combines them. In the deep-MOND regime the result is the geometric-mean law $a = √(a_N · a₀)$, which is what makes galaxy rotation curves flat.

**The two strains and their combination.** A test chain feels two contributions to its P12 landscape: the local-mass strain $Σ_N = −GM/R$ (§3) and the coarse-grained cosmic-horizon potential $Σ₀ = −a₀·R$ (§5). Where both matter (the joint weak-gradient regime, $a_N ∼ a₀$), bilocal channels carry strain set by the *geometric mean* of the two, and the cumulative reading yields a logarithmic cross-term

> $Σ_{cross}(R) = −√(GMa₀) · log(R/R₀)$   (Paper_030),

whose gradient is the combination rule

> $a = √(a_N · a₀)$.

A $−log R$ potential is a flat rotation curve: constant circular speed with $v⁴ = GMa₀$.

**Tier, and an honest history.** In Paper_030 the geometric mean rests on a postulate, P14 (bilocal strain coupling), which simply *states* the geometric-mean coupling; the paper says so plainly. A later paper (QuadraticStrain) discharges that postulate: reading gravity as the squared participation amplitude $|ΣP|²$, Newton is the diagonal term and MOND is the *off-diagonal interference cross-term*, and the geometric mean is then forced as an interference modulus rather than assumed. **Tier: the combination-rule form is Derived (form-forced). QuadraticStrain discharges two of Paper_030's postulates with one strain-reading choice (P-Quadratic-Strain): the geometric-mean coupling P14, now the forced off-diagonal interference modulus, and the deep-MOND regime assumption, removed by correcting Paper_030's horizon term from an isotropic monopole to the dipole Paper_029 actually derives.** ED does not assume a MOND interpolation function to get here: the geometric mean is an output, not an input. The one element not proved from the primitives is the constructive interference *sign*; it is supplied at simulation (measured) tier, conditional on the P12-coherence operationalization, not derived.

**What is, and isn't, distinctive.** Composing the three results gives the baryonic Tully–Fisher relation $v⁴ = GMa₀$, slope exactly 4, asymptotically zero intrinsic scatter. Honesty forbids overreach here: **slope-4 and the tightness are shared with standard MOND**: any MOND-class theory predicts them, and they are not an ED-specific win. What is ED-distinctive is the *normalization* $a₀ = cH₀/(2π)$ from §5, and its consequence, that $a₀$ cannot be constant. That consequence is the one genuinely new, falsifiable prediction of the whole chain, and it is §7.

---

## 7. The capstone: a₀ evolves with the cosmic expansion

Every prior section reproduces or reframes something already known. This one is a genuine forward prediction, it was on the record before the data, and in 2026 the data arrived. It is also the sharpest exposure of the framework, because there is no dial to turn if it fails.

**The prediction.** The acceleration scale reads the cosmic horizon $R_H = c/H$. But $H$ is not a constant (the universe expanded faster in the past), so evaluating $a₀$ at redshift $z$ gives

> $a₀(z) = cH(z) / (2π)$   (Paper_031 §8.8; Paper_038 CO-3; forced exponent $α = 1$ in $a₀ ∝ H^α$).

$a₀$ was larger in the early universe and has shrunk as expansion slowed. Standard MOND treats $a₀$ as a constant of nature; ED forbids it. And ED cannot soften the claim: the exponent $α = 1$ is fixed by the §5 mechanism (the horizon projection, plus the absence of any free dimensionless scale to bend it), so this is a zero-dial prediction. If $a₀$ is constant, or evolves with a different power, the framework is wrong here with nothing to adjust.

**The data.** In 2026 a survey (MUSE-DARK III, *A&A*) measured the rotation-curve acceleration scale across $0.33 < z < 1.44$. The corpus compiles the confrontation in Paper_031 §8.8, with the fine-grained fit below in the Master Predictions List §1.15. Three results, each stated at the tier it earns:

- **The scale evolves.** A constant $a₀$ is excluded at ≈30σ, which buries constant-scale MOND (dead at ≈29σ). But that bar is cleared by *any* evolving-scale model: the 30σ confirms ED's *direction*, not its distinctive content. The ED-specific claim is the *rate*, $α = 1$, and it lives in the third bullet.
- **The local value matches.** The present-day number agrees with $cH₀/(2π)$ to ~8%, the same parameter-free match as §5.
- **The exact rate is in mild tension.** A direct fit gives $α ≈ 1.18 ± 0.04$; the data run somewhat *faster* than `H(z)`. ED's forced $α = 1$ sits ~4σ off the raw fit, softening to roughly 1–2σ once the systematics of a single first-generation survey are folded in.

**The honest verdict.** This is a prediction confirmed in *direction* and in *local magnitude*, with a real, unresolved tension on the *exact rate*. It is not a clean victory and it is not a refutation. Either the high-redshift measurements carry systematics in how ancient starlight traces mass, or ED's coupling rate is genuinely off. Because there is no dial, the tension cannot be absorbed; it stands exposed for the next surveys (Rubin, Euclid) to sharpen or break. That exposure is what a real prediction meeting real data looks like, and it is why this section, not the reproductions before it, is the paper's point.

---

## 8. What this sector does not claim

The results above are real at the tier each carries, and those tiers imply a matching list of things this paper does not deliver. Stated plainly, so a reader need not hunt for them:

- **Magnitudes are inherited, not derived.** $G$'s value (via $ℓ_{ED} = ℓ_P$), $a₀$'s value (via $H₀$), and the cosmological constant's value are fixed by measurement. ED derives their *forms* and reduces the count of independent constants; it does not compute the numbers, and the substrate derivation of $H₀$ itself is open.
- **The metric is weak-field and kinematic.** The nonlinear and strong-field regimes, and a background-free construction, are open, and are the distinctive, falsifiable frontier, not a solved problem.
- **ED gravity is khronometric, not pure GR.** It coincides with general relativity in the weak field treated here; the preferred-frame sector (the khronon, the scalar gravitational-wave polarization) is where it departs, and that lives in the companion papers.
- **The combination rule rests on a discharged postulate with a residual.** The geometric mean is forced as an interference cross-term rather than merely postulated, but the constructive *sign* is a simulation result, not a proof.
- **Clusters and the CMB are not addressed here.** The galactic MOND account does not by itself supply the cosmological dark component; ED carries that as a separate warm relic in the dark-sector papers, and the cluster/CMB fit is an open debt where MOND-class theories characteristically struggle.
- **Nothing here is forced from nothing.** Every result is conditional on the thirteen postulated primitives and the paper-specific postulates named at each step (P-Codim-1, P-Sat, P-Potential-Reading, P-Commitment-Linear, P14 / P-Quadratic-Strain, and the V1/V5 kernel inheritance).

The remaining sectors of the framework, and their tiers, are in the corpus and its per-domain tiered-claims ledgers.

---

## 9. Appendix: tier table

| Result | § | Tier (from the gravity ledger) |
|---|---|---|
| Holographic bound $N(R) ≤ 4πR²/ℓ_{ED}²$ | 2 | Derived, given P-Codim-1 + P-Sat; $ℓ_{ED}$ value-inherited |
| Newton $a_N = GM/R²$, $Φ = −GM/R$ | 3 | Derived, given P-Potential-Reading (+ §2 postulates); V1 $1/R$ envelope inherited |
| $G = c³ℓ_{ED}²/ℏ$ | 3 | Form-derived; magnitude value-inherited ($ℓ_{ED} = ℓ_P$) |
| Spatial metric $g_{ij} ∼ b⁻¹$ | 4 | Derived |
| Lapse $N² ∼ b$; Schwarzschild relation $g_{00} g_{rr} ∼ −1$ | 4 | Derived, conditional on P-Commitment-Linear (α = 1) |
| Weak-field Schwarzschild metric | 4 | Derived (relation + inherited Newtonian profile) |
| Factor-of-two light bending | 4 | Derived + simulation (ratio 2.09 vs 2.00) |
| Khronometric class; $c_T = c$; $α₂ = 0$ exact | 4 | Stated here; Derived in companion papers (GR-II / GR-IV) |
| Crossover $R_H = c/H₀$; $a₀ = cH₀/(2π)$ | 5 | Derived (form-forced); $H₀$ value-inherited |
| Deep-MOND $a = √(a_N a₀)$; $v⁴ = GMa₀$ | 6 | Derived (form-forced); QuadraticStrain replaces P14 + regime assumption with P-Quadratic-Strain (residual: constructive sign, sim/measured tier) |
| BTFR slope-4, zero scatter | 6 | Prediction — MOND-shared (only the $a₀$ normalization is ED-distinctive) |
| $a₀(z) = cH(z)/(2π)$ evolves | 7 | Prediction; ≈30σ evolution confirmed (2026), local value ~8%, exact rate ~1–2σ tension |

*Tiers transcribed from `physics-papers/gravity/Gravity_TieredClaims_Ledger.md`.*

---

*Provenance: §1–§9 built by reading Papers 087, 025, 026, 027, GR-I, 029, 030, and QuadraticStrain directly; other companion results (GR-II/III/IV, 031 §8.8, 038, Master Predictions List §1.15) are cited, not re-derived. QC and referee passes applied; §6 verified against the QuadraticStrain source; em-dash polish done (2026-08-18). Remaining before public release: a math-rendering PDF build (the inline `backtick` expressions become proper LaTeX).*
