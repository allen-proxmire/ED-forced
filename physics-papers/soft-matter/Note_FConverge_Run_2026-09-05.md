# F-CONVERGE, run 2026-09-05: the test is not runnable, and the reason is a problem with the wall itself

*Working note, soft-matter transport arc. Companion to `Paper_UnifiedP04TransportBudget.md` §§8–9. Written after a literature check, not a calculation.*

---

## Verdict

**F-CONVERGE did not run.** It is not runnable on existing data, and three things came out of finding that out. **The third is a defect in this arc's own §9, written yesterday.**

| | |
|---|---|
| **F-CONVERGE** | **NOT RUN.** No system has `ℓ_ee` and `ℓ_mr` characterized near the wall. |
| **The wall's identification with MIR** | **In trouble, either way it is read.** §1 below. |
| **`Λ`'s derivation** | **Evaluated outside the domain of validity of both its inputs.** §3. |
| **A candidate venue exists** | The Dirac fluid, and it is awkward for the arc. §2. |

**Nothing here is banked as a falsification.** Each finding is stated with the escape available to it, and §4 says what would settle each.

---

## 1. The premise fails in the regime the arc points at: bad metals do not saturate

`Paper_UnifiedP04TransportBudget` §3 reads `ρ_max` as the **MIR saturation value** and identifies it with the Adjacency band filling, `f → 1`, at a mean free path floored at the cell `a_eff`. §8 then makes the strange-metal / quantum-critical regime the arena where the co-onset is to be tested.

**In that arena resistivity does not saturate.** Gunnarsson, Calandra & Han's review states saturation occurs when the apparent mean free path approaches the interatomic separation, and names **high-T꜀ cuprates and alkali-doped fullerides as cases where the Ioffe–Regel condition is violated**. In bad metals the extracted mean free path passes *below* the interatomic spacing with no saturation at all, and the standard reading of that is that the quasiparticle Fermi velocity has stopped being a meaningful quantity.

**So the arc points at the one family of materials that has no wall.** Where saturation *is* observed — large-resistivity metals that respect Ioffe–Regel — electron viscosity is not measured, so the co-onset cannot be looked for there either.

**This is a dilemma rather than a refutation, and both horns cost something.**

- **If `a_eff` is the interatomic spacing**, then bad metals run straight through the floor and **the wall does not exist where the arc says it does.**
- **If `a_eff` is not the interatomic spacing** — the DCGT coarse-graining cell need not be a lattice constant — **then MIR saturation is not ED's wall**, and §3's identification of `ρ_max` with MIR, along with §8's whole corrected pairing, is a misidentification.

**Either way the arc owes an argument it has not made: why the Adjacency-band wall should be the MIR wall.** That argument is currently an assumption carried by a name.

## 2. The one candidate venue, and it is awkward

The Dirac fluid in charge-neutral graphene is the only established system where a momentum-transport bound and quantum-critical dissipation are reached together, and at room temperature. Ku *et al.* imaged viscous Dirac-fluid flow and report viscosity and scattering rates **"comparable to the universal values expected at quantum criticality"**, with the inter-particle scattering rate expected to saturate at the Planckian time.

**Momentum transport is at or near its floor there. Charge transport is not.** The resistivity of charge-neutral graphene is nowhere near MIR saturation and `ℓ_mr` stays long — that separation is what makes the system hydrodynamic in the first place. **On the arc's own account, `f → 1` is one event: if momentum transport has hit the Adjacency band's wall, charge transport should have hit it too.**

**That is a tension with F-COONSET, not with F-CONVERGE.** It is also not a falsification, because three escapes are available and each is real:

1. **"Comparable to" is not "at."** Ku *et al.* claim proximity to the universal values, not saturation of a bound.
2. **The arc's co-onset is explicitly conditional** on *"a system where one cell governs both transports."* At charge neutrality, momentum relaxation is extrinsic (disorder, phonons, boundaries) while the momentum-conserving collisions are intrinsic. ED can say the resistivity there is not Adjacency-limited at all, and the condition is simply not met.
3. **There is no Fermi surface at charge neutrality**, so `p_F` is undefined and `Λ` as derived in §9 does not apply to this system in the first place.

**Escape 2 is the substantive one, and it has a price:** it says the co-onset test requires a system where the resistivity is *intrinsically* budget-limited, which by §1 means a material that actually saturates — and no such material has a measured electron viscosity. **The two conditions the test needs have not yet been met together, and it is not obvious that any known material meets them.**

## 3. A defect in §9, found by trying to use it

This is the finding that matters most, and it is self-inflicted.

§9.2 derives `Π_q = 1` from the Drude form `ρ = p_F/(n e² ℓ)` and `Π_p = 1/3` from kinetic `η = ⅓ n p_F ℓ`, **both evaluated at `ℓ = a_eff` — the wall.** But the wall is exactly where the bad-metal literature says the Boltzmann/quasiparticle description stops holding: the mean-free-path language survives past MIR only as an extrapolation, and the Fermi velocity along with it.

**Both inherited ingredients of `Λ` are being used outside their domain of validity, at the single point where the answer is wanted.**

§9.5's tier table records `η` and `ρ` as **I (inherited)** and §9.6 flags the coefficient as a `[1/5, 1/3]` averaging band. **Neither captures this.** The problem is not that the coefficient is uncertain; it is that at the wall `p_F` and `n` may not be the right variables at all, in which case `Λ`'s **parameter-independence** — the whole claim, per §9.6 — loses the derivation that produced it.

**`Λ` may still be correct.** Bounds of that shape are reached in the Planckian and holographic literature without quasiparticles, which is precisely why the quantity is interesting. **But ED has not derived it that way, and the derivation ED has is evaluated where its inputs fail.** Recording this rather than leaving it for a referee.

## 4. What would settle each of these

- **The wall's identity (§1).** An argument from the substrate for why the Adjacency band fills at the interatomic spacing rather than at some other length — or an explicit statement that `a_eff` is *not* the lattice constant, followed by re-deriving what `ρ_max` then is. **The second is more likely to be right and it costs the MIR identification.**
- **The co-onset tension (§2).** Identify a material that both saturates (respects Ioffe–Regel) and has an accessible electron viscosity. **If none exists, F-COONSET is not near-term and the paper should stop calling it so.**
- **The derivation's domain (§3).** Either restrict `Λ` to the quasiparticle regime *approaching* the wall rather than at it — which is testable and honest, and turns `Λ` into a limiting statement — or re-derive it without quasiparticles. **The first is cheap and should be done now.**

## 5. One claim of mine, withdrawn

On 2026-09-05 I recorded F-CONVERGE as *"the cheapest test in the arc"* and *"the actionable item; the derivation is done."* **That asserted an availability I had not checked.** The two lengths are measured in **disjoint** windows in every established system — WP₂ is hydrodynamic below ~20 K and conventional above, graphene and PdCoO₂ are ultra-clean low-temperature systems — so there is no dataset to run it against. **Withdrawn, and corrected at every site that carries it.**

---

## References

- **Gunnarsson, O., Calandra, M. & Han, J. E. (2003).** *Colloquium: Saturation of electrical resistivity.* Rev. Mod. Phys. **75**, 1085 (arXiv:cond-mat/0305412). Source for saturation at the Ioffe–Regel condition and for high-T꜀ cuprates and alkali-doped fullerides violating it.
- **Ku, M. J. H. *et al.* (2020).** *Imaging viscous flow of the Dirac fluid in graphene.* Nature **583**, 537 (arXiv:1905.10791). Viscosity and scattering rates "comparable to the universal values expected at quantum criticality," at room temperature.
- **Lucas, A. & Hartnoll, S. A. (2017).** *Resistivity bound for hydrodynamic bad metals.* PNAS **114**, 11344. Cited in §9.9 for the opposite-sign `η`–`ρ` correlation in its own regime.
- **Zaanen, J. (2019).** *Planckian dissipation, minimal viscosity and the transport in cuprate strange metals.* SciPost Phys. **6**, 061. The existing unification of minimal viscosity with strange-metal resistivity; see the arc's 2026-09-05 correction.

*Gravity ledger Staleness #65; soft-matter ledger.*
