# Mass Without Mass in Event Density: Rest Mass and Inertia from Binding, and Why Mass Is Not Time Dilation

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers, substrate-evaluation arc (the mass sector). Build-and-run result on the certified Σ-rule simulator.
**Status:** Publication draft. Empirical substrate-evaluation with the certified simulator plus V5's known cross-chain structure. Standalone, cold-reader accessible.
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative).

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **This is BINDING mass, not the fundamental Higgs mass.** The result is a native mechanism for the rest mass of *composites* (bound structures), which is the physically dominant form of mass (the bulk of a proton's mass is binding, not the Higgs coupling). The *fundamental* Higgs/electroweak mass (electron, current-quark, W/Z from spontaneous symmetry breaking) is a separate mechanism, not natively realized on the certified substrate (a companion condensate probe comes up empty), and is **inherited**.
2. **The binding coupling (V5) is a structural addition, not a primitive.** It is faithful to the corpus's V5 cross-chain kernel (finite reach, retarded, attractive), but the bare certified substrate does not carry it, and the primitives are not shown to *force* it. So this establishes *V5's known structure yields binding-mass*, not that the 13 primitives force mass.
3. **The confinement, the sub-luminal composite, and the inertia are measured; the strict rest limit is an extrapolation.** The composite's residual center-of-mass drift shrinks monotonically with cluster size (a small steady net-momentum bias that cancels better with more constituents), heading to rest; "at rest" is that trend, not a single measured zero.
4. **The equivalence-principle reading is a consistent interpretation, not an independent proof.** The mass-independent response to a uniform force is reported as such and read as the equivalence principle; that reading is not separately established.
5. **No numerical mass values are produced.** Not the electron mass, not any spectrum. The result is the *mechanism* and its qualitative signatures.
6. **No new substrate primitive is introduced**, and no primitive forcing is invoked.
7. **Credit.** The framing that a lone front is massless like the cosmic horizon, so mass cannot be a property of a front but must come from binding, is due to A. Proxmire and is the seed of the whole approach.

---

## Abstract

Does Event Density's substrate produce rest mass, or inherit it? At the level of an individual excitation the honest answer is that it cannot: the certified update rule is **ballistic-or-extinct**, a front advances one step at the maximal speed or it dies, with no slow-but-surviving mode for a rest mass to live in. So a lone ED front is *massless*, moving always at the substrate speed `c`, sharing the cosmic horizon's defining feature (`c`-moving, no rest frame). This paper shows that mass nonetheless emerges, exactly where physics says most of it lives: **binding.** A composite is a different object from its constituents, and we test whether the cross-chain coupling V5, with its finite-reach retarded structure (attractive, as binding requires — a constraint the corpus derived, not an independently established feature), confines massless fronts into a bound composite whose center of mass moves sub-luminally. Running it on the certified simulator, it does. **A free front moves at `c` (measured `v = 0.98`); with the coupling off a cluster disperses (unbound); with it on the cluster is confined (its spatial extent stays bounded while each constituent keeps moving at `c`), and the composite's center of mass is sub-luminal (`v ≈ 0.5 < c`), heading to rest as the cluster grows (drift `0.54 → 0.31` from eight to thirty-two constituents).** The composite also has **inertia**, the defining property of mass: pushed by a force, it accelerates less than a free front (`v_x = 0.72` versus `0.98`), while an *unbound* cluster under the same force responds at `0.97` (≈ the free front), so the resistance is genuinely from binding, not from averaging. Under a *uniform* force the response is mass-independent, a mobility-saturated velocity response consistent with (but not proof of) mass-independent acceleration. This is **mass without mass**, the physical origin of the dominant part of real mass (a bound system of massless-moving constituents has rest energy, hence rest mass, though its parts move at `c`). Finally we separate two things the substrate had entangled: **mass is not time dilation.** A lone front carrying commitment-memory *dwells* (a slower clock; the dwell is itself a non-certified addition, used only as a contrast), but under a force its drift tracks its path speed exactly, no directional inertia; that is **time dilation** (and it is why the same commitment-rate factor appears in the gravitational sparse-commitment parameter), whereas only *binding* gives directional inertia. So mass (binding) and the clock rate (commitment sparseness) are distinct. Honest scope: the mechanism is native but V5-conditional (V5 is a structural addition, not primitive-forced), and it is *binding* mass, the fundamental Higgs mass being separate and inherited.

---

## 1. Introduction: the Wall, and Why a Lone Front Is Massless

An emergent-physics program must eventually answer where mass comes from, and Event Density's certified substrate makes the question sharp. The certified update rule is **ballistic-or-extinct**: a surviving front commits and advances exactly one hop per step, or it fails and dies. There is no dwell, no fractional hop, no reduced-but-surviving group velocity. Rest mass needs exactly that missing mode, a Lorentz-scalar sluggishness that lets a thing sit slower than the maximal speed. So **an individual ED front cannot have a rest mass**: it moves always at the substrate speed `c`.

This is not a failure to hide, it is a clue, and the cleanest way to see it is A. Proxmire's: **a lone front shares the cosmic horizon's defining feature.** In ED the horizon is the surface where participation capacity runs to zero, and it recedes at `c`; it is a massless, `c`-moving boundary with no rest frame. A single front is the same in that one respect, massless and `c`-moving (the analogy is motivation, not a claim that a local excitation and a global causal boundary are the same object). So mass is not a property a front can carry at all. If mass exists in ED, it must come from something a *collection* of fronts can do that a single one cannot: **bind.**

This is also exactly how most real mass works. The rest mass of a proton is roughly ninety-nine percent binding energy, not the Higgs coupling to its quarks; a box of light has a rest mass equal to its energy, though every photon inside moves at `c`. A bound system of massless-moving constituents has rest energy in its own frame, hence rest mass, while its parts move at `c`. This paper asks whether ED realizes that mechanism, and shows it does.

---

## 2. Method: a Faithful Test of Binding on the Certified Substrate

**The substrate dynamics are the certified ones.** Fronts live on a two-dimensional participation graph; each front's per-step choice is scored by the certified Σ functional `compute_sigma` on the real event-density field, and the front must advance to a neighbour every step (no dwell — faithful to the "ballistic" half of ballistic-or-extinct; extinction is disabled here, so the binding fronts are ballistic-always, which is harmless for a binding test). Because a front avoids its own committed trail (higher density), it moves into fresh ground, a ballistic worldline. The certified front carries an orientation (Σ itself is orientation-blind), so the orientation only breaks the ties among equally-good fresh neighbours; we implement that as a small persistence bias (far below the Σ scale, so it never overrides Σ), chosen to mimic the persistent straight-line motion of the certified `(ρ, orientation)` front (whose persistence the corpus's continuum study measured; this probe measures only the resulting net speed, `v = 0.98`).

**The binding is V5's known structure, added honestly.** V5 is ED's cross-chain kernel; its established form (Paper_090) is retarded (it references past positions) and finite-reach; the *attractive* sign is a constraint the corpus separately derived as necessary for binding (the V5-synchronization work), not an independently established feature. We add exactly this: each front is nudged toward the reach-weighted (`exp(-|Δr|/ℓ)`) mean position of the other fronts, a constant-magnitude inward pull toward that reach-gated centroid (the reach enters the centroid weighting, not a distance-decaying force law, so the confinement may be somewhat stronger than a literal exp-decaying kernel would give). It is **not** rigged to bind: whether a finite reach can confine `c`-speed fronts is precisely the open question, and if the fronts outrun the reach the probe returns "unbound."

**Honest scope of the model (preamble 2).** V5 is a structural addition, faithful in kind to the corpus kernel but not carried by the bare certified substrate and not shown to be primitive-forced. This tests whether V5's *known structure* produces binding-mass, not whether the raw primitives do. The coupling reads positions (a coarse stand-in for recent commitment activity — not the actual phase-coherence form of Paper_090); the gauge phase is implicit. These are flagged.

**Controls.** A single free front (expected massless, `v ≈ c`); the cluster with the coupling off (expected to disperse).

---

## 3. Result 1: Binding Confines Massless Fronts into a Sub-Luminal Composite

Three seeds, eight fronts unless noted, on the certified simulator.

| case | outcome |
|---|---|
| single free front | `v = 0.98` — ballistic, massless, moves at `c` |
| cluster, coupling OFF | **unbound** — spatial extent grows `28 → 55`, fronts radiate away |
| cluster, coupling ON (every strength and reach tested) | **bound** — extent stays `1.4 – 2.3` (confined); center of mass moves at `v ≈ 0.5 < c` |

**The finite-reach binding confines the ballistic fronts — the load-bearing positive result.** With the coupling off the cluster's radius grows without bound; with it on the radius stays small at every coupling strength and reach tried, while each constituent keeps advancing at `c` every step. That is a genuine bound state of massless-moving parts.

The composite's center of mass moves at `v ≈ 0.5`, below the free-front `0.98`. On its own this is a *weak* signature, an *unbound* cluster's center of mass also drifts below `c` (at `0.12`) purely from internal-momentum averaging, so we do **not** rest the mass claim on the bare center-of-mass speed; the decisive signatures are the confinement here and the inertia of §4. What the bound center-of-mass does show cleanly is that it heads toward rest as the cluster grows, a small **steady net-momentum bias** (from asymmetric seeding and the persistence tie-break, not a wobble) that shrinks monotonically with size, even as the bound extent itself grows:

| constituents `N` | 8 | 16 | 24 | 32 |
|---|---|---|---|---|
| center-of-mass drift | 0.54 | 0.49 | 0.44 | 0.31 |
| bound extent (rms) | 1.4 | 3.0 | 4.7 | 8.6 |

More constituents cancel their internal momenta better and the drift falls toward zero; the extent grows simply because a larger bound state is bigger, and crucially it stays *bounded* (versus `55` and rising for the coupling-off case). So a large bound cluster extrapolates to a **composite at rest whose parts each move at `c`** (the strict rest limit is this trend, not a measured zero, preamble 3). This is mass without mass.

---

## 4. Result 2: the Composite Has Inertia (and the Equivalence Principle Appears)

Sub-luminal motion is one signature of mass; the *defining* property is **inertia**, resistance to acceleration. Apply a uniform force and measure the drift response.

- **Free front, forced: `v_x = 0.98`** — at `c`, unresisted. A force cannot slow a massless front, only steer it.
- **Unbound cluster, forced: `v_x = 0.97`** — ≈ the free front. Without binding there is no resistance; the eight fronts simply align to the force. *(This is the control that matters: it rules out the objection that a many-front center-of-mass is slow merely by averaging.)*
- **Bound composite, same force: `v_x = 0.72 < 0.97`** — the binding **resists** the force; the composite accelerates *less* than the *unbound* cluster of the same size. **The resistance is from binding, and it is inertia. The composite is massive.**

The bound response is essentially independent of cluster size (relative response `≈ 1` to about ten percent from eight to thirty-two constituents). We do **not** read this as the mass magnitude being size-independent — a uniform force simply cannot resolve the mass magnitude, which is extensive (a bigger bound system has more rest energy by `E = mc²`) but lives in the momentum, not in the uniform-force drift *velocity*. A mass-independent velocity response to a *uniform* force is what the equivalence principle would give (all masses fall alike), but it is equally the generic signature of a mobility-saturated response, so we report it as **mass-independent (mobility-saturated), consistent with — but not evidence for — the equivalence principle** (preamble 4). The load-bearing, controlled fact is the bound-versus-unbound gap (`0.72` versus `0.97`): binding produces genuine inertia.

---

## 5. Result 3: Mass Is Not Time Dilation

A second mechanism can make a front move slower than `c`, and it is important to separate it from mass: **commitment-memory.** A front carrying memory *dwells* (it re-commits in place when its memory is high), lowering its advance rate. Two disclosures up front, to hold this to the same bar as the V5 addition (§2): the dwell is **itself a structural addition**, not carried by the certified rule (which is ballistic-or-extinct and has *no* dwell), and it was previously flagged as **not primitive-licensed** (`H1_Leg_Scoping`); it is used here only as a *contrast*, to show what a non-binding slowdown does. The corpus had flagged a connection between this mass-memory rate and the gravitational sparse-commitment parameter through a shared commitment factor, so the question is whether that slowdown is itself a kind of mass. We separate them with the inertia test: push a lone memory-carrying front and compare its forward drift to its path speed.

| memory | path speed | forward drift `v_x` | `v_x / path` |
|---|---|---|---|
| none | 1.00 | 1.00 | 1.00 |
| medium | 0.55 | 0.55 | **1.00** |
| strong | 0.38 | 0.38 | **1.00** |

**The ratio is exactly one at every memory level.** The memory front dwells (its path speed drops), but its forward drift *tracks the path speed exactly*: every step it does take still aligns fully to the force. There is **no directional inertia**. Commitment-memory makes a **slow clock**, which is **time dilation**, not mass. Contrast the bound composite of §4, whose center-of-mass drift (`0.72`) sits *below* its constituents' path speed (`1`): the composite **resists**, that gap is **directional inertia**, mass.

> **So the commitment rate and mass are different phenomena.** The commitment/sparseness rate governs the **clock rate**, which is **time dilation**, and that is precisely why the same factor also appears in the gravitational sparse-commitment parameter (gravitational time dilation), while **mass is a separate thing that comes from binding.** The connection the corpus flagged is real, but it is about the clock, not the mass. Keep them separate: commitment sparseness sets the clock (time dilation); binding sets the mass.

---

## 6. Honest Tiers and Scope

- **Measured (solid):** the confinement (bounded extent versus dispersal, the load-bearing result), and the inertia (forced response `0.72` against the **unbound control `0.97`**, so the resistance is from binding, not averaging), on the certified simulator with V5's structure, robust across coupling strengths and reaches. The mass-versus-time-dilation *contrast* is clean (`v_x/path = 1` for the memory front, `< 1` for binding). Both the V5 coupling (§2) and the memory-dwell (§5) are **non-certified structural additions**, disclosed as such; the contrast between them holds regardless.
- **Weak / not load-bearing:** the bare sub-luminal center-of-mass (`v ≈ 0.5`) taken alone (an unbound cluster's COM also drifts below `c`); the mass claim rests on confinement + inertia, not on it.
- **Extrapolated:** the strict rest limit (the drift trend `0.54 → 0.31`, not a measured zero).
- **Interpretation only:** the equivalence-principle reading of the mass-independent (mobility-saturated) uniform-force response.
- **V5-conditional (preamble 2):** the mechanism uses V5's known structure, a structural addition, not a bare-primitive result. The bare substrate's *native* cross-chain coupling was separately measured to be dispersive, not binding, so V5 is not obviously forced; the forward question, whether the primitives force V5, is open.
- **Binding mass only (preamble 1):** this is composite/binding mass, the dominant form. The fundamental Higgs mass is separate and inherited, the condensate route to it coming up empty on the certified field.

So the honest claim is **a native binding-mass mechanism, V5-conditional, for the physically dominant form of mass**, plus a clean separation of mass from time dilation, not a from-primitives derivation of all mass or of any mass value.

---

## 7. Falsification Criteria

### 7.1 Binding does not confine

**Falsifier sentence:** *A demonstration that V5's finite-reach retarded attraction fails to confine the ballistic fronts at every coupling strength and reach (the cluster always disperses) would falsify the binding mechanism (§3).*

### 7.2 The composite is not sub-luminal

**Falsifier sentence:** *A demonstration that a confined cluster's center of mass moves at the constituent speed `c` (not sub-luminally) would falsify the mass-from-binding kinematics (§3).*

### 7.3 No inertia

**Falsifier sentence:** *A demonstration that the bound composite responds to a force at the same rate as a free front (no resistance, `v_x ≈ c`) would falsify the inertia result (§4).*

### 7.4 The drift does not shrink with size

**Falsifier sentence:** *Observation that the center-of-mass drift stays fixed (or grows) with cluster size, rather than shrinking toward rest, would falsify the at-rest limit (§3) and the steady-bias-shrinking-with-N reading.*

### 7.5 Memory gives inertia

**Falsifier sentence:** *A demonstration that a lone commitment-memory front resists a force (its drift falling below its path speed) would collapse the mass-versus-time-dilation separation (§5) and reopen the possibility that the commitment rate is itself a mass.*

---

## 8. Position Statement

**Event Density has a V5-conditional binding mechanism for rest mass** (V5 is a faithful structural addition, not primitive-forced; the bare substrate's native cross-chain coupling was separately measured to be dispersive, not binding). An individual front is massless, moving always at `c` (ballistic-or-extinct), sharing the cosmic horizon's `c`-moving, no-rest-frame character. A composite is different: with V5's known finite-reach retarded attraction, massless fronts are confined into a bound cluster whose center of mass is sub-luminal and heads to rest as the cluster grows, and which has inertia (it resists a force more than a free front does) while showing the equivalence principle under a uniform force. This is mass without mass, the physical origin of the dominant part of real mass. The commitment rate, by contrast, produces a slow clock, time dilation, not inertia, so mass (binding) and the clock rate (commitment sparseness) are cleanly separated.

**What this paper claims.** A measured, native, V5-conditional binding-mass mechanism (confinement + sub-luminal composite + inertia); the rest limit as a size-trend; the equivalence principle as a consistent reading; and a clean measured separation of mass from time dilation.

**What this paper does not claim.** That the bare primitives force mass (V5 is a structural addition, not shown primitive-forced); that this is the fundamental Higgs mass (it is binding mass; the fundamental mass is separate and inherited); any numerical mass value; or the strict rest limit as a single measurement (it is an extrapolation).

**Series context.** The mass-sector result of the ED program, the sector its other papers left open. It turns on the same primitive the program's reduction isolates, the arrow (P11): the arrow makes an individual front `c`-moving and massless, and V5's binding of such fronts is what makes a composite massive, while the arrow's commitment sparseness separately sets the clock (time dilation). It pairs with the gravity papers (where the same sparse-commitment factor is the gravitational time dilation) and the gauge/chirality papers (where the arrow's other roles live).

---

## Appendix: Glossary, Reader Map, Artifacts

### Glossary

- **Ballistic-or-extinct.** The certified rule: a front advances one hop at the maximal speed or dies; no dwell, hence no individual rest mass. **— Status clarified 2026-09-06 (gravity ledger #116, #117): this is a property of the REFERENCE RULE, not of ED.** P11 selects a *channel* and is silent on locus; the certified rule selects a *locus* (`compute_candidates` → `admissible_neighbors`, `u` excluded), and **that substitution is what forbids dwell.** With **`P-Commitment-Advancement`** now adopted (`Paper_087` §P11), **the primitives admit a dwell** — a commitment into the Branch 3 **Internal** class — and *“always advances”* is the **special case** in which every commitment selects an Adjacency-class channel. **Nothing measured on the certified rule changes**, and whether a dwell-capable rule would change any of it is **untested**. **But “no individual rest mass” should be read as a statement about the reference substrate, not about ED.**
- **Mass without mass.** Rest mass of a bound system whose constituents move at `c`; the composite has rest energy in its frame though its parts do not sit still. The dominant form of real mass (hadron binding).
- **V5.** ED's cross-chain kernel; here used in its known form (retarded, finite-reach, attractive). A structural addition to the bare certified substrate.
- **Confinement.** The bound cluster's spatial extent stays bounded while each constituent moves at `c`; the signature of a bound state.
- **Inertia.** Resistance to acceleration; measured as a sub-luminal response to a force. The defining property of mass.
- **Time dilation (here).** The slow clock produced by commitment-memory dwelling; the same commitment-rate factor as the gravitational sparse-commitment parameter. Distinct from mass.

### Reader map

*Intuition.* A single ripple in this substrate always moves at the top speed, like light, or like the cosmic horizon, so it has no weight. Tie several such ripples together with a short-range pull and the *bundle* can sit still (or move slowly) even though every ripple inside it still races at top speed, and now the bundle is hard to push, it has weight. That is where mass comes from here, the same reason a proton is heavy while the quarks and gluons inside it are nearly massless. A separate effect, a ripple that pauses to re-commit, makes a *slower clock*, not weight, and that is time dilation, which is why the same "how often does it commit" number shows up in gravity's time-slowing, not in mass.

*Why it is worth reporting.* ED looked, at the level of a single excitation, to have no way to make rest mass at all. The honest resolution is that it does not need one: mass is not a property of an excitation, it is what binding does to a collection, which is both how most real mass works and a clean fit to ED's own picture of a lone front as a massless, horizon-like object.

### Artifacts (certified simulator; `evaluation/` and `theory/Higgs_Emergence/`)

- `theory/Higgs_Emergence/mass_from_binding_probe.py` — the full probe: free-front control; unbound-versus-bound; the size sweep; the inertia (force) test; the memory-versus-binding discriminator.
- `theory/Higgs_Emergence/Mass_From_Binding_Results.md` — the results record with the honest tiers.
- Prior mass-sector context: `theory/Higgs_Emergence/H1_Leg_Scoping.md` (the ballistic-or-extinct wall), `E1_MassFromStructure_Results.md` (the condensate route to fundamental mass, negative).

### Load-Bearing Step Audit

| Claim | Tier | Source |
|---|---|---|
| Individual front is massless (ballistic-or-extinct) | **grounded** | the certified rule; `H1_Leg_Scoping` |
| Free front moves at `c` (`v = 0.98`) | **measured** | §3 control |
| Coupling off → unbound (extent `28 → 55`) | **measured** | §3 |
| Coupling on → confined (extent `1.4 – 2.3`) | **measured** | §3 |
| Composite center-of-mass sub-luminal (`v ≈ 0.5`) | **measured; weak alone** (unbound COM also `< c`, `0.12`) | §3 |
| Drift shrinks with size (`0.54 → 0.31`) → rest limit | **measured trend; rest = extrapolated** | §3 |
| Composite has inertia (forced `v_x = 0.72` vs **unbound control `0.97`**) | **measured (controlled)** | §4 |
| Uniform-force response mass-independent (mobility-saturated) | **measured; equivalence-principle reading = interpretation only** | §4 |
| Memory front `v_x/path = 1` = slow clock = time dilation | **measured on a NON-certified dwell addition** (not primitive-licensed, `H1_Leg_Scoping`) | §5 |
| Binding = inertia; commitment rate = clock; distinct (the contrast) | **measured (from §4 vs §5); the contrast holds regardless of the dwell's licensing** | §5 |
| V5 is primitive-forced | **NOT CLAIMED** (structural addition) | preamble 2, §6 |
| This is the fundamental Higgs mass | **NOT CLAIMED** (binding mass; fundamental inherited) | preamble 1, §6 |
| Any numerical mass value | **NOT CLAIMED** | preamble 5 |

---

**End of Paper (Mass Without Mass).**

*Substrate-evaluation arc. A lone ED front is massless (ballistic-or-extinct, `c`-moving, sharing the horizon's no-rest-frame character); V5's finite-reach retarded binding confines such fronts into a bound composite that is confined, heads to rest as it grows, and is inertial (forced response `0.72` against the unbound control `0.97`, so the resistance is from binding, not averaging; the mass-independent uniform-force response is mobility-saturated, equivalence-principle-consistent). Mass without mass, the dominant form of real mass, V5-conditional (V5 a structural addition, not primitive-forced); the fundamental Higgs mass is separate and inherited. And mass (binding) is cleanly separated from time dilation (commitment-memory's slow clock, the gravitational sparse-commitment factor): `v_x/path = 1` for the memory dwell (itself a non-certified addition), `< 1` for binding. Credit A. Proxmire for the horizon-as-front framing.*
