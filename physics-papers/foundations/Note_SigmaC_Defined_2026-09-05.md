# `Σ_C`, defined: `Coh` exists and was missed, `Grad` does not, and `|Σ P|²` is assigned to two terms with opposite signs

*Foundations working note, 2026-09-05. Written to discharge Foundations staleness #8. **It discharges part of it, corrects my own statement of it, and replaces the rest with a sharper problem.***

---

## Verdict

| Term | Status |
|---|---|
| **`Coh`** | **Defined, build-verified in 2D and 3D.** `Paper_PhaseCoherence_P12Coh` §2. **My arm-C scoring said "defined nowhere" and that was wrong** — §1. |
| **`Grad`** | **Undefined at theory level.** One operational form exists, in the simulator only. §2. |
| **`Str`** | **Defined twice, and the two are incompatible.** §3. |
| **The real problem** | **`|Σ P|²` is assigned to `Coh` *and* to `Str`, which enter `Σ_C` with opposite signs. As written, they cancel and the gravity arc's interference term vanishes.** §4. |

**Nothing here is fixed by fiat.** §4's candidate resolutions change the gravity arc's sign structure, so the choice is the author's, not a note's.

---

## 1. `Coh` is defined, and I missed it

**`Paper_PhaseCoherence_P12Coh` §2** (substrate-evaluation, draft v1, 2026-07-08) gives it explicitly:

$$\mathrm{Coh} \;=\; \Big|\sum_a P_a\Big|^2 - \sum_a |P_a|^2 \;=\; 2\sum_{a<b}\sqrt{b_a b_b}\,\cos\Delta\pi_{ab}$$

the phase-dependent interference content of the participation superposition, zero at random phase and maximal at alignment.

**And it is not a bare proposal.** `../event-density/theory/P12_Coherence_PhaseAlignment_Scoping.md` runs it through four build steps on the certified Σ-engine: it rewards alignment (Step 2), the resulting order is **finite-reach natively** because the P05 connection carries the substrate's own quenched disorder (Step 3, `ξ ≈ 4–6`), it survives being made causal in the selection functional (Step 4, `flip_frac ≈ 0.48` — the phase decides about half of all growth choices), and **the finite-reach result is robust to dimensionality**, re-run on a 28³ grid. Tier: **MEASURED** for finite-reach; the operationalization itself is form-forced-conditional, not a theorem.

**Correction to Foundations #8 and to `Result_F1_ArmC_2026-09-05.md` §4.** I scored the external finding as *"`Coh` and `Grad` are defined nowhere"* after checking `Paper_087`, `Paper_088`, `Paper_026`, `Paper_027` and `Paper_054`. **I did not check `substrate-evaluation`, where the definition has been sitting since July.** The external model's finding was correct about the *primitives* paper and about the gravity arc's own citations; it was not correct that the corpus lacks the definition. **The defect is that `Paper_087` §P12 does not point at it** — a reader of the primitive has no way to reach the operationalization.

**Cheapest repair, and it is one sentence:** `Paper_087` §P12 gains a forward pointer to `Paper_PhaseCoherence_P12Coh` §2.

## 2. `Grad` is genuinely undefined

**No theory-level definition exists.** The only operational form in the corpus is the certified simulator's:

$$\mathrm{Grad} = |\rho_v - \rho_u|$$

a nearest-neighbour commitment-density penalty (`Paper_BlindnessInvariant_KnotsNotCrystals` §2; `Paper_PhaseCoherence_P12Coh` §2.1). **That is a simulator rule, not a substrate definition**, and unlike `Coh` there is no companion arc lifting it to one.

**This half of the external finding stands unqualified.** `Σ_C = Coh − Str − Grad` has one term now defined, one term defined twice and incompatibly, and one term with no theory-level definition at all.

**What `Grad` plausibly is**, stated as a question rather than an answer: the certified form penalises density difference *across an edge*, which is the natural adjacency-gradient content of P12's own `∇_adj`. Whether the substrate-level `Grad` should read commitment density, bandwidth, or participation amplitude is not settled anywhere, and the three give different dynamics.

## 3. The two `Str`s

- **`P-Quadratic-Strain` ("Model C"), `Paper_QuadraticStrain_v1` §2:** $\mathrm{Str}_K = \big|\sum_a P_K^{(a)}\big|^2$ — the squared modulus of the total participation amplitude on channel `K`.
- **Certified simulator:** $\mathrm{Str} = \rho_v$ — a local commitment-density penalty.

**These are different functionals of different objects**, and no paper reconciles them. The simulator's is a scalar density; Model C's is a quadratic form over complex amplitudes.

**This is less alarming than it first looks and should be recorded that way.** The certified rule is explicitly a **tractability reduction** — `P12_Coherence_PhaseAlignment_Scoping.md` Step 1 records that the simulator is *"single-rule-type; no explicit polarity"*, and that its `Coh = −(ρ−ρ_*)²` is *"a density-target, not a coherence measure; **arguably mislabeled**."* **The corpus already knows the simulator's Σ-terms are named after theory terms they do not implement.** What is missing is a statement saying so where a reader will meet it.

**Repair:** a naming note in `Paper_BlindnessInvariant_KnotsNotCrystals` §2 and in `Paper_PhaseCoherence_P12Coh` §2.1 — *the certified `Coh`/`Str`/`Grad` are the simulator's density-level stand-ins and are not the substrate functionals of the same name.*

## 4. The real problem: `|Σ P|²` is assigned to both `Coh` and `Str`

**This is what the reconciliation actually turns on, and it is not what Foundations #8 said.**

`Paper_PhaseCoherence_P12Coh` §2 defines `Coh` as the **interference part**, `|Σ P|² − Σ|P|²`. But that same paper's own conclusion (§5, discharge list) states its result as ***"the quadratic strain reading of the Interference-Gravity paper is grounded (`Coh` read as `|Σ P|²`)"*** — the full square, not the interference part. **The paper gives `Coh` two values three pages apart, differing by the diagonal `Σ|P|² = Σ b_a`.**

**And `P-Quadratic-Strain` assigns the full square `|Σ P|²` to `Str`.** In `Σ_C = Coh − Str − Grad` these enter with **opposite signs**. So on the corpus's text as it stands:

- **If `Coh = |Σ P|²` and `Str_K = |Σ P|²`** (the §5 reading): the two cancel identically and `Σ_C = −Grad`.
- **If `Coh = |Σ P|² − Σ|P|²` and `Str_K = |Σ P|²`** (the §2 reading): `Coh − Str = −Σ_a b_a`. **The cross term cancels exactly** — and the cross term `2√(b^{(L)}b^{(H)})\cosΘ_{LH}` **is the entire MOND mechanism** of `Paper_QuadraticStrain_v1` and `Paper_030`.

**Both readings delete the interference the gravity arc runs on.** That is a sharp, checkable, load-bearing problem and it does not appear in any ledger.

**Three candidate resolutions, none of which I am adopting on my own authority**, because each changes the arc's sign structure:

1. **Different index sets.** `Coh` sums over the chain's **own** participations (intra-chain phase alignment); `Str_K` sums over **external sources** contributing to channel `K` (inter-chain). No cancellation, because the sums run over disjoint sets. **This is the most likely intended reading** — `Paper_PhaseCoherence` speaks of *"the participating phases"* at a node, `P-Quadratic-Strain` of *"contributing sources"* — **but neither paper states the index set, and that is precisely why the collision is invisible.**
2. **`Coh` is the interference part and `Str` is the diagonal only.** Then `Coh − Str = 2Σ√(b_a b_b)cos Θ − Σ b_a`, the interference survives with the constructive sign, and `Paper_QuadraticStrain_v1`'s `Str_K = |Σ P|²` is a misstatement of what should be `Str_K = Σ_a b_K^{(a)}`. **This makes the arc work but contradicts the postulate as written.**
3. **`Coh` and `Str` are the same content read at different layers** and the corpus should carry one term, not two. **Cleanest if true, largest rewrite if adopted.**

**Resolution 1 costs the least and is most likely right.** Confirming it requires one sentence in each of the two papers naming the index set — and until it is written, **the corpus contains an exact cancellation of its own gravitational mechanism.**

## 5. What this changes elsewhere

**Foundations #8 is half-discharged and half-replaced.** The `Coh`-is-undefined half is withdrawn (§1). The `Grad` half stands (§2). The two-`Str`s half is downgraded from *contradiction* to *a naming collision the corpus already half-knows* (§3). **And a new, heavier item replaces them: §4's double assignment.**

**Research target #24(a) needs correcting too.** I listed the `cos Θ` sign as **open**. `Paper_QuadraticStrain_v1` §9 carries an **Update 2026-07-08 (constructive sign supplied)** pointing at `Paper_PhaseCoherence_P12Coh`. **The sign was discharged two months ago.** What is stale is that paper's **audit table row 11**, which still reads `A / OPEN`. So (a) is a table-versus-body desync, not an open physics question — and the external model that "found ED's own §9 residual" found a residual the corpus had already answered in the body of the same section.

---

## Actions, ranked by cost

1. **State the index sets** for `Coh` and `Str_K` (§4). One sentence each, in `Paper_PhaseCoherence_P12Coh` §2 and `Paper_QuadraticStrain_v1` §2. **Highest value, lowest cost, and the arc does not work without it.**
2. **Reconcile `Paper_PhaseCoherence_P12Coh` §2 against its own §5** — `Coh` cannot be both `|Σ P|²` and `|Σ P|² − Σ|P|²`.
3. **Fix `Paper_QuadraticStrain_v1` audit row 11** to match its own §9 update.
4. **Forward-pointer in `Paper_087` §P12** to the `Coh` operationalization.
5. **Naming note** distinguishing the certified simulator's Σ-terms from the substrate functionals (§3).
6. **`Grad` remains open** and is now the only genuinely undefined term in `Σ_C`.

*Foundations staleness #8 (revised), #10 (new); gravity ledger Staleness #70.*
