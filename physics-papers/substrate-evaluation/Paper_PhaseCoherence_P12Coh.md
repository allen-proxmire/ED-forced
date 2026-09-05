# Phase Coherence in ED: Attractive Sign, Finite Reach, and Substrate Disorder

*The attractive/constructive sign that V5 and MOND assumed, supplied and build-verified on the certified substrate; a companion to "Knots, Not Crystals."*

**Draft v1, 2026-07-08.** Event Density (ED) Generative Papers, substrate-evaluation arc. Build-and-run on the certified $\Sigma$-rule (measured); the phase channel is an honestly-named polarity-extended rule, not the certified rule. Cold-reader oriented; corpus facts inlined; cross-references minimal.

---

## Preamble: what this paper does NOT claim

Written first, per house discipline; the abstract is reconciled against it.

1. **The 13 primitives are not derived** (Paper_087).
2. **It does not derive that P12's coherence term must be phase-based.** It *operationalizes* the coherence term $\mathrm{Coh}$ as the coherence content of the participation superposition, a substrate-level reading that is shown to be permitted, needed, natural, and build-verified. That is form-forced conditional on the reading, not forced from a deeper layer. The certified rule's $\mathrm{Coh}$ is $-(\rho-\rho_*)^2$ (phase-blind); the phase-coherence term here is an extension.
3. **The measured result is on a polarity-extended rule, not the certified rule.** The certified $\rho$-dynamics are used verbatim; a P09 phase channel is *added*. No certified result is altered.
4. **It does not derive the reach $\xi$** (identified with V5's memory length $\ell_{V5}$ and the MOND transition reach). $\xi$ is value-inherited, set by the P05-connection strength and the substrate's disorder variance. Form-forced-finite, value-inherited.
5. **It is not a new empirical prediction.** It supplies the *attractive/constructive sign* that the V5 clock-binding result (RelationalTick) and the MOND interference term (Interference-Gravity) previously assumed; the observational content of those results is unchanged.
6. **It does not claim the phase-coherence term is the only functional that could supply the sign**, only that this one does, and that it is Knots-safe.

---

## Abstract

Three ED results converge on a single unproven bit. The V5 kernel must be *attractive* to bind chains into local clocks (RelationalTick); the MOND interference term must be *constructive* to enhance gravity (Interference-Gravity); and both trace to whether the P12 stability landscape's coherence term $\mathrm{Coh}$ rewards phase alignment. Reading $\mathrm{Coh}$ as the coherence content of the participation superposition, $\big|\sum_a P_a\big|^2 - \sum_a|P_a|^2 = 2\sum_{a<b}\sqrt{b_a b_b}\cos\Delta\pi$, answers *yes* by construction: it is maximal when phases align. The worry is that an alignment reward is an *ordering coupling*, and the companion result "Knots, Not Crystals" established that the certified substrate has no long-range ordering coupling in any sector. We test this directly by build-and-run on the certified $\Sigma$-rule with an added P09 phase channel, in two and three dimensions. Three findings. First, the phase-coherence term does reward alignment: order emerges where a phase-blind control shows none. Second, with a *trivial* (substrate-blind) connection the term crystallizes, producing exactly the forbidden long-range order. Third, and decisively, with the physical P05 connection, which carries the substrate's own quenched disorder (bandwidth heterogeneity, the commitment-density field), the phase-order is **finite-reach**, short-range stiffness with defects rather than a crystal, robustly in both 2D and 3D. The reason is ED-native: commitment is irreversible (P11), so this is a one-shot deposition, not an equilibrium spin model, and there is no thermal ordering transition; the phase accumulates holonomy along growth paths, a one-dimensional random walk that is roughly dimension-independent. Crystallization is confined to the unphysical trivial connection. This supplies the constructive/attractive sign for MOND and V5, operationalizes P12-Coh, and grounds the quadratic strain reading, while preserving Knots. Tier: MEASURED; the operationalization is form-forced-conditional; $\xi$ is value-inherited.

---

## 1. The Question, and Why One Answer Moves Three Arcs

### 1.1 The convergence

Three separate ED results, developed independently, reduce to the same missing fact.

- **V5 must be attractive.** The RelationalTick result derives that V5, ED's finite-reach cross-chain kernel, must have a *synchronizing* (attractive) phase coupling to bind nearby chains into a shared local clock: a repulsive coupling gives no binding, hence no composite rest frames. The attractive sign is carried there as a necessity condition, not a derivation.
- **MOND must be constructive.** The Interference-Gravity result reads the MOND transition as the interference cross-term of two source amplitudes (local mass and cosmic horizon) on a shared substrate channel, with the geometric-mean modulus $\sqrt{a_N a_0}$. That term enhances gravity only if the interference is *constructive*; the constructive sign is the paper's one named residual.
- **P12-Coh is unoperationalized.** Both signs trace upstream to the P12 stability landscape $\Sigma = \mathrm{Coh} - \mathrm{Str} - \mathrm{Grad}$: specifically, to whether the coherence term $\mathrm{Coh}$ rewards phase alignment. The canonical gloss calls $\mathrm{Coh}$ the "alignment / phase-consistency content," but the only operational instance, the certified simulator, reads commitment density only and is phase-blind.

One answer to "does $\mathrm{Coh}$ reward phase alignment" therefore moves all three: it supplies V5's sign, MOND's sign, and the operational reading of P12-Coh at once.

### 1.2 The question, made precise

$\Sigma$ is extremized by the substrate dynamics (a chain's experienced acceleration is $-\nabla\Sigma$). The question is whether the functional $\mathrm{Coh}$ is *higher* when participating phases are aligned, so that alignment is dynamically favored.

### 1.3 The candidate answer, and the danger

With the canonical participation amplitude $P_K = \sqrt{b_K}\,e^{i\pi_K}$ (P04 bandwidth as squared modulus, P09 polarity as phase), the coherence content of a multi-source superposition on one channel is the phase-dependent interference part,
$$\mathrm{Coh} \;=\; \Big|\sum_a P_a\Big|^2 - \sum_a |P_a|^2 \;=\; 2\sum_{a<b}\sqrt{b_a b_b}\,\cos\Delta\pi_{ab},$$
which is zero at random or orthogonal phase and maximal in phase. A functional named "coherence" that rewards alignment is what "coherence" *means* given the amplitude structure. So the candidate answer is *yes, by construction*.

The danger is equally structural: an alignment reward is an **ordering coupling**, and the companion result "Knots, Not Crystals" showed that the certified substrate has no long-range ordering coupling in any sector, and therefore no spontaneous long-range order (no crystal). A phase-coherence term that produced a crystal would contradict that result. Whether a phase-rewarding $\mathrm{Coh}$ gives a crystal or stays finite-reach is not decidable by inspection; it is an empirical question about the substrate's dynamics. That is what this paper measures.

---

## 2. Method: A Polarity-Extended Rule on the Certified Engine

### 2.1 The certified rule

The certified $\Sigma$-rule scores a candidate transition $u \to v$ as $\Sigma = k_c\,\mathrm{Coh} - k_s\,\mathrm{Str} - k_g\,\mathrm{Grad}$, with $\mathrm{Coh} = -(\rho_v - \rho_*)^2$, $\mathrm{Str} = \rho_v$, $\mathrm{Grad} = |\rho_v - \rho_u|$. Every term reads the commitment density $\rho$ and graph-local structure only; the rule is orientation-blind by a hard invariant. Dynamics enumerate admissible candidates, take the $\Sigma$-maximal set, break ties deterministically (by bandwidth, then node id), and commit at the winner, the sole writer of $\rho$ (irreversible, monotone non-decreasing).

### 2.2 The load-bearing distinction: the blind sector is not the phase sector

The certified rule's blind quantity is a *spatial director* (the substrate's transverse relational-directional structure). P09 polarity is a different thing: the *phase* $\pi_K$ of the participation amplitude, the rule's phase relative to the local flow. The corpus associates the certified director with P05/P09 only weakly and non-explicitly, and the single-rule-type simulator does not represent the amplitude phase $\pi_K$ at all. So a P09-phase coherence term reads a channel that is, at most, weakly associated with the blind director, and that the orientation-blindness invariant does not directly govern. This is why a phase-coherence term is not forbidden at the outset, and it corrects a conflation (reading the spatial director as the amplitude phase) that had made the phase channel look walled off.

### 2.3 The extension

We add a phase $\pi_K \in [0, 2\pi)$ to each node and, at each node's first commit, deposit the phase that maximizes the finite-reach coherence term, which is the mean-field angle of its already-committed neighbors. The phase is transported across each edge with a **P05 connection** (a holonomy) $A(w \to v)$; a trivial connection is $A \equiv 0$ (a pure copy), the physical connection ties $A$ to the substrate's own heterogeneity (§5). The $\rho$-dynamics, including winner selection, are the certified rule verbatim; the phase channel never writes $\rho$, so the certified $\rho$-results are untouched.

### 2.4 What the observables mean

We report the order parameter $R = \big|\langle e^{i\pi}\rangle\big|$ over committed nodes ($R \approx 1$ is a crystal, $R \approx 1/\sqrt{N}$ is disorder), and the phase correlation $C(r) = \langle\cos(\pi_x - \pi_y)\rangle$ over node pairs at separation $r$. A finite correlation length $\xi$ (so that $C(r) \to 0$ for $r \gg \xi$) is short-range stiffness, the Knots-permitted regime; $C(r) \to \text{const}$ is long-range order, the forbidden crystal.

---

## 3. Result 1: The Coherence Term Rewards Phase Alignment

On a $60\times 60$ grid, a control run with the coherence term off (phases assigned at random) gives $R = 0.016 \approx 1/\sqrt{N}$ and $C(r) \approx 0$ at every $r$: no order, and, since this run commits every node under the certified rule, a confirmation that the $\rho$-dynamics are the certified rule. With the coherence term on, strong local order appears ($C(1) \approx +0.9$).

That the term produces alignment is, in part, by construction: the deposition maximizes the coherence term over the phase, which is exactly what extremizing $\Sigma$ with a phase-coherence term does. The control's role is therefore precise rather than dramatic: it shows the alignment comes from the coherence term, not from the $\rho$-dynamics, which give none. The substantive, non-obvious question, whether the resulting order is a crystal or finite-reach, is the subject of §§4 and 5. Tier: MEASURED.

---

## 4. Result 2: A Trivial Connection Crystallizes

With a trivial connection ($A \equiv 0$, a pure phase-copy) and a single nucleation site, the phase-coherence deposition produces perfect long-range order: $R = 1.000$ and $C(r) = +1.000$ at all separations out to $r = 25$. This is exactly the crystal that "Knots, Not Crystals" says the substrate should not have. We state it plainly rather than bury it: an alignment reward *is* an ordering coupling, and with no connection disorder it orders the whole field. The rest of the paper is the resolution.

A noise sweep locates a standard order-disorder transition: single-seed deposition survives as ordered up to a deposition noise of order $0.3$ radians ($R = 0.89$) and breaks to finite-reach by $0.8$ radians ($R = 0.26$), the XY-type transition expected of an aligning coupling.

---

## 5. Result 3: The Substrate's Own Disorder, and Irreversibility, Keep It Finite-Reach

### 5.1 P05 as a real connection

P05 transports polarity with a connection. A physical connection is not flat; it responds to the substrate. We tie the holonomy to the substrate's own intrinsic disorder, in two independent ways: quenched **bandwidth heterogeneity**, $A(w\to v) = \kappa_{bw}\,(b_{wv} - 1)$, a real feature of any participation graph; and the substrate's own **commitment-density field**, $A(w\to v) = \kappa_{\rho}\,(\rho_w - \rho_v)$. Both are deterministic functions of the substrate state, not imposed thermal noise.

On the $60\times 60$ grid, single seed, no imposed noise, the crystal breaks into finite-reach order:

- **Bandwidth connection** ($\kappa_{bw} = 0.5$): $R = 0.16$, $C(r)$ decaying from $+0.89$ at $r=1$ to near zero by $r \approx 8$ to $12$ ($\xi$ a few lattice units), shortening as the connection strengthens ($\kappa_{bw} = 2.0$ gives $\xi \approx 2$).
- **Density connection alone** (homogeneous grid, $\kappa_\rho = 0.5$): $R = 0.064$, $C(r)$ from $+0.92$ to near zero by $r \approx 5$. Even with no imposed graph heterogeneity, the certified dynamics' own commitment-density disorder breaks the crystal.

The phase-order becomes short-range stiffness plus phase-domain defects, which is precisely what Knots permits.

### 5.2 The 3D hardening test

Genuine long-range order is easier in three dimensions (the planar XY model has only quasi-order, the three-dimensional one has true long-range order), and physical space is $3+1$. So the decisive test is whether the intrinsic disorder still holds the phase finite-reach in 3D. On a $28^3$ grid, single seed, no imposed noise:

- **Trivial connection** ($\kappa = 0$): crystal, $R = 1.000$, $C(r) = +1$ out to $r = 18$. The ordering tendency is confirmed, if anything stronger than in 2D.
- **Bandwidth connection** ($\kappa_{bw} = 0.5$): finite-reach, $R = 0.046$, $C(r)$ from $+0.74$ to near zero by $r \approx 6$ ($\xi \approx 3$ to $4$).
- **Density connection** ($\kappa_\rho = 0.5$): finite-reach, $R = 0.010$, $C(r)$ from $+0.78$ to near zero by $r \approx 4$ ($\xi \approx 2$ to $3$).

The finite-reach result is robust to dimensionality; if anything $\xi$ is *shorter* in 3D at the same connection strength, because each node averages over more disordered paths.

### 5.3 Why it is robust: irreversibility, not equilibrium

The three-dimensional-XY intuition does not apply, and the reason is the program's defining primitive. This is not an equilibrium spin model relaxing to a ground state; it is a one-shot **irreversible** deposition (P11): each phase is set once, at commitment, and never relaxes. There is no temperature and no thermal ordering transition. The phase at a node is the seed phase plus the holonomy accumulated along the growth path that reached it, a one-dimensional random walk in phase whose variance grows with path length, so the correlation length $\xi \sim 1/\mathrm{var}(A)$ is roughly independent of the spatial dimension. The measured near-dimension-independence of the reach (§5.2) is the evidence; the path-holonomy picture is the intuition for it. The irreversibility of commitment is what confines the crystal to the unphysical trivial connection.

### 5.4 The window

The connection strength has a usable window. Too weak ($\kappa \to 0$, a trivial connection) crystallizes. Too strong ($\kappa_\rho \gtrsim 2$ in these runs) gives $\xi < 1$: complete decorrelation, no binding at all. Useful finite-reach binding lives between, and it is there that V5's memory length $\ell_{V5}$ and the MOND transition reach sit.

---

## 6. What This Discharges

Why the sign comes out constructive, and not destructive, is worth stating explicitly, because it is the basis of the discharge. The coherence term enters $\Sigma$ with a positive, stabilizing coefficient, $\Sigma = k_c\,\mathrm{Coh} - k_s\,\mathrm{Str} - k_g\,\mathrm{Grad}$ with $k_c > 0$ (the certified rule), and it is maximal at phase alignment (§1.3). Since the dynamics extremize $\Sigma$, they favor the aligned configuration, at which the interference cross-term $2\sqrt{b_a b_b}\cos\Delta\pi$ is *positive*. The sign is therefore constructive, not destructive, and §3 confirms the dynamics settle there. This holds given the operationalization of $\mathrm{Coh}$ as the coherence content, and given a connection strength in the physical window (§5.4). On that basis:

- The **MOND constructive sign** (the Interference-Gravity residual) is supplied: alignment is favored, so the interference cross-term is positive, gravity-enhancing, and finite-reach.
- The **V5 attractive sign** (the RelationalTick necessity condition) is supplied: the phase-coherence term has exactly the property V5 needs, an attractive (alignment-favoring) coupling that is finite-reach, which is V5's local-not-universal binding. This establishes the *property*; it is not a reconstruction of the specific V5 kernel or of a bound clock.
- **P12-Coh is operationalized** as the phase-coherence content, and the **quadratic strain reading** of the Interference-Gravity paper is grounded. *(⚠ **Internal inconsistency flagged 2026-09-05:** this line originally read “$\mathrm{Coh}$ read as $|\sum P|^2$”, **the full square** — while §2 defines $\mathrm{Coh} = |\sum P|^2 - \sum|P|^2$, **the interference part only.** The two differ by the diagonal $\sum_a b_a$. **And the full square is what `P-Quadratic-Strain` assigns to `Str`**, which enters $\Sigma_C$ with the opposite sign — so on either reading the cross term cancels and the gravity arc's mechanism vanishes. **Not resolved here.** `foundations/Note_SigmaC_Defined_2026-09-05.md` §4.)*
- **Knots is preserved**: the resulting order is finite-reach, not a crystal.

The conditionality is stated precisely: these follow *given the operationalization*, which is form-forced (natural, permitted, needed, and now build-verified) rather than a theorem from the primitives alone.

---

## 7. Honest Accounting

Tier: MEASURED, in 2D and 3D. The operationalization is a substrate-level reading, not a derivation; the certified rule remains phase-blind, and its results stand unchanged. The reach $\xi$ is value-inherited, set by the connection strength and the disorder variance; the paper forces the *finiteness* of the reach, not its value. The crystal at a trivial connection is reported as a genuine finding, not elided: the safety rests on the connection being physical (substrate-coupled) and on commitment being irreversible.

This paper *extends* "Knots, Not Crystals" rather than contradicting it. That result found no crystal in the phase-blind certified rule. This one adds the phase channel the certified rule omits, makes the rule reward phase alignment, and finds *still no crystal*, together with the attractive sign as the new content.

---

## 8. Falsification Criteria

1. **Long-range order under a physical connection.** If a phase-coherence term on the substrate produced long-range order ($C(r) \to \text{const}$) under a physical, substrate-coupled connection, the finite-reach claim of §5 would fail.
2. **A trivial substrate connection.** If the substrate's P05 connection were shown to be flat (not coupled to any substrate heterogeneity), the crystal of §4 would be the physical outcome and the attractive sign would need another home.
3. **Reach outside the window.** If V5's binding or the MOND transition demanded a reach $\xi$ outside the window the connection can produce (§5.4), the operationalization would be challenged.
4. **The sign comes out repulsive.** If a faithful phase-coherence term on the substrate favored anti-alignment (a repulsive coupling), the MOND and V5 signs would be refuted, not supplied.

---

## 9. Position Statement

P12's coherence term rewards phase alignment; the substrate's own disorder, carried by the P05 connection, together with the irreversibility of commitment, keeps the resulting phase-order finite-reach rather than crystalline. This supplies the attractive/constructive sign that three ED results assumed, build-verified on the certified substrate in two and three dimensions, with Knots preserved. It is a companion to "Knots, Not Crystals": that paper found no crystal in the phase-blind rule; this one finds no crystal even when the rule is made to reward phase, and finds the attractive sign there. Tier MEASURED, conditional on the operationalization; the reach is value-inherited.

---

## Methods and Reproducibility

All runs reuse the certified simulator's per-decision functions (`compute_sigma`, `compute_candidates`, `apply_tiebreak`, `NodeState.commit`) verbatim for the $\rho$-dynamics; only the P09 phase channel and its P05-connection deposition are added, and both are flagged as additions.

- **Base probe** (`p12_phase_coherence_probe.py`): $60\times 60$ grid, single-carrier phase superposition deposited as the mean-field angle over committed neighbors within a reach $\ell$. Control (coherence off): $R = 0.016$, $C(r) \approx 0$. Single-seed pure copy: $R = 1.000$, $C(r) = +1.000$ to $r = 25$ (crystal). Multi-seed (40 seeds): $R \approx 0.22$ to $0.27$, $C(r)$ decaying by $r \approx 8$ to $12$. Deposition-noise sweep: ordered at $0.3$ rad ($R = 0.89$), finite-reach at $0.8$ rad ($R = 0.26$). Shuffle-null confirms the baseline.
- **Intrinsic-disorder probe** (`p12_phase_coherence_probe_v2_intrinsic.py`): P05 connection $A = \kappa_{bw}(b_{wv}-1) + \kappa_\rho(\rho_w - \rho_v)$, single seed, no imposed noise. Trivial connection $R = 1.000$ (crystal). Bandwidth: $\kappa_{bw} = 0.5 \to R = 0.16$, $\xi \approx 4$ to $6$; $\kappa_{bw} = 2.0 \to \xi \approx 2$. Density: $\kappa_\rho = 0.5 \to R = 0.064$, $\xi \approx 4$ to $5$; $\kappa_\rho = 2.0 \to \xi < 1$.
- **3D probe** (`p12_phase_coherence_probe_3d.py`): $28^3$ grid, 6-neighbor, single seed, no imposed noise. Trivial connection $R = 1.000$ (crystal, $C = +1$ to $r = 18$). Bandwidth $\kappa_{bw} = 0.5 \to R = 0.046$, $\xi \approx 3$ to $4$; $\kappa_{bw} = 4.0 \to \xi < 1$. Density $\kappa_\rho = 0.5 \to R = 0.010$, $\xi \approx 2$ to $3$.

Estimators, seeds, grids, and connection forms are stated so each result is rerunnable from the cited scripts.

---

**End of draft (Phase Coherence in ED).**

*Substrate-evaluation arc. P12's coherence term rewards phase alignment; the substrate's own disorder plus irreversible commitment keep the phase-order finite-reach, not crystalline. Supplies the attractive/constructive sign for V5 and MOND, operationalizes P12-Coh, grounds the quadratic strain reading, and preserves Knots. Tier MEASURED, conditional on the operationalization; reach value-inherited. Companion to "Knots, Not Crystals."*
