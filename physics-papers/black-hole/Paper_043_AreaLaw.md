# Paper 043 — Area-Law Form FORCED; Coefficient $(\log g)$ INHERITED

**Series:** Wave-2 Generative Papers (Black-Hole Arc)
**Status:** Conditional structural derivation given the 13 ED primitives (per Paper_087) + paper-specific postulates declared in §2.
**Companions:** Paper_025 (holographic participation-count bound), Paper_039 (horizon as decoupling surface), Paper_047 (Hawking spectrum), Paper_068 (von Neumann entropy — supersedes the earlier Paper_067, merged 2026-07-05).

---

## Preamble — What This Paper Does NOT Claim

1. This paper does **not** claim a derivation of the Bekenstein–Hawking coefficient $1/4$ (in Planck units) from first principles; the area-coefficient $\log g$ is INHERITED via the multiplicity-count $g$ inheriting from standard quantum-statistical-mechanics matching.
2. It does **not** claim to resolve the black-hole information paradox; that is in Arc Hawking (Paper_052).
3. It does **not** introduce new substrate primitives.
4. It does **not** claim that the area-law is unique to black-hole horizons; the substrate audit applies to any decoupling surface (Paper_039).
5. "Area-law form" means: black-hole entropy proportional to horizon area $A$: $S_{\mathrm{BH}} = (\log g) \cdot A / \ell_P^2$ (omitting numerical prefactors).
6. "Coefficient $\log g$ INHERITED" means: the multiplicity $g$ per substrate Planck-cell at the horizon is set by substrate combinatorics inherited from external matching, not derived from first principles in this paper.

---

## Abstract

The black-hole area-law form is FORM-FORCED in ED by: (i) Paper_025 holographic participation-count bound $N = 4\pi R^2/\ell_{\mathrm{ED}}^2$; (ii) Paper_039 horizon as decoupling surface; (iii) Paper_068 von Neumann entropy via Shannon–Khinchin axioms. Composing these: the substrate participation count at the horizon scales as area / $\ell_P^2$; the von Neumann entropy of substrate-horizon participation is $S = (\log g) \cdot A/\ell_P^2$ where $\log g$ is the per-Planck-cell multiplicity. The structural form $S \propto A$ is FORCED. The coefficient $\log g$ is INHERITED — it cannot be derived from first principles in this paper because the multiplicity $g$ depends on substrate combinatorics matched against standard quantum-statistical-mechanics conventions.

---

## §1 Introduction

The Bekenstein–Hawking entropy $S_{\mathrm{BH}} = A/(4\ell_P^2)$ (in natural units) is the central result of black-hole thermodynamics. Its area-proportionality is the foundational input for holographic principle, AdS/CFT, and most subsequent black-hole thermodynamics.

This paper supplies the substrate audit: the area-law form is FORM-FORCED in ED via three substrate-level inputs. The numerical coefficient ($1/4$ in standard units) is INHERITED via $g$-multiplicity matching, not derived.

---

## §2 Primitive Inputs and Paper-Specific Postulates

### 2.1 Primitives invoked (per Paper_087)

- **P02 (Participation)** — substrate-level participation count.
- **P04 (Bandwidth)** — bandwidth-additivity for substrate entropy.
- **P08 (Substrate scale $\ell_{\mathrm{ED}}$)** — Planck length.
- **P11 (Commitment-irreversibility)** — directional structure / second-law content.

### 2.2 Upstream dependencies

- **I-025:** Holographic participation-count bound $N = 4\pi R^2/\ell_{\mathrm{ED}}^2$ (Paper_025).
- **I-039:** Horizon as decoupling surface (Paper_039).
- **I-068:** von Neumann entropy via Shannon–Khinchin (Paper_068).
- **I-Born:** Born rule (Paper_002).
- **I-SK:** Shannon–Khinchin axiomatization (standard math).

### 2.3 Paper-specific postulates

- **P-Horizon-Participation:** The substrate-level participation count at a black-hole horizon equals the holographic bound $N = A/\ell_P^2$ to leading order, where $A$ is the horizon area.
  > **CORRECTED 2026-09-04. This postulate previously read $N = A/(4\pi\ell_P^2)$.** That was inconsistent with the rest of this paper and with its source. `Paper_025` derives the bound as area-divided-by-footprint-area: the per-channel footprint on a 2-surface is $\ell_{\mathrm{ED}}^2$ (its audit row 111, from P-Codim-1 + P08), so $N \leq 4\pi R^2/\ell_{\mathrm{ED}}^2$, and $4\pi R^2$ **is** $A$. This paper's §1 cites that form and its audit row 3 records $A/\ell_P^2$; only this line carried the extra $4\pi$, which is what a conversion from $4\pi R^2$ to $A$ looks like when the substitution is made twice. Two of three statements and the upstream derivation agree, so the $4\pi$ is removed.
  >
  > **The correction sharpens the open problem rather than resolving it, and that is the honest reading.** With $S = N\log g$ (audit row 6) and $N = A/\ell_P^2$, matching Bekenstein $S = A/(4\ell_P^2)$ requires $\log g = 1/4$, i.e. $g \approx 1.28$ — which **violates P-Multiplicity-$g$'s own floor $g \geq 2$**. At that floor the horizon entropy comes out $2.77\times$ Bekenstein. The $4\pi$ reading would have been admissible ($\log g = \pi$, $g \approx 23.1$); removing it closes that escape. **The arc now has a live coefficient problem where it previously had an ambiguity**, which is the more useful state to be in.
  >
  > Two routes remain, neither taken here: the $g \geq 2$ floor may be tidiness rather than commitment, or — more promising — audit row 6 assumes *independent* cells, and correlated horizon cells give $S < N\log g$, which is the kind of structure V5 cross-chain content could supply and which is claimed nowhere. See `BlackHole_TieredClaims_Ledger.md` addendum 2026-09-04 and `gravity/Gravity_TieredClaims_Ledger.md` Staleness #18.
  >
  > *Unaffected: the area-law* form*, which is this paper's actual claim, and the honest "coefficient INHERITED" framing of the title and item 1.*
- **P-Multiplicity-$g$:** Each substrate Planck-cell at the horizon supports $g \geq 2$ distinguishable rule-type configurations, contributing $\log g$ to the per-cell entropy.

---

## §2.5 Load-Bearing Step Audit Table

| # | Step | Label | Notes |
|---|---|---|---|
| 1 | Holographic participation-count bound | I | Paper_025. |
| 2 | Horizon as decoupling surface | I | Paper_039. |
| 3 | Substrate participation count at horizon = $A/\ell_P^2$ | P-Horizon-Participation | Postulate. *Hedge "(up to constants)" removed 2026-09-04: the constant is now fixed, the postulate above is corrected to match, and the resulting coefficient problem is recorded rather than absorbed into the hedge.* |
| 4 | Per-Planck-cell multiplicity $g$ | P-Multiplicity-$g$ | Postulate. |
| 5 | von Neumann entropy via Shannon–Khinchin axioms | I | Paper_068. |
| 6 | Substrate participation-state entropy = $N \cdot \log g$ | D-via-I | Standard entropy on independent cells (I-SK). |
| 7 | Substitute $N = A/(4\pi \ell_P^2)$ | D | Algebraic substitution. |
| 8 | Area-law form $S \propto A$ | D | Result of step 7. |
| 9 | Coefficient $(\log g)/(4\pi)$ | I | Inherited via $g$-matching; not derived. |
| 10 | Bekenstein–Hawking $1/4$ coefficient | I | Empirical / standard matching. |
| 11 | Numerical $\log g$ from substrate combinatorics | OPEN | Not claimed. |

---

## §3 The Derivation

### 3.1 Holographic count at the horizon

By I-025 (Paper_025), the maximum participation count over a sphere of radius $R$ is bounded as $N = 4\pi R^2/\ell_{\mathrm{ED}}^2$ (up to constants). At a black-hole horizon of area $A = 4\pi R^2$, this gives $N \sim A/\ell_P^2$.

By P-Horizon-Participation, the substrate count **saturates** this bound at the horizon (the horizon is the maximum-entropy configuration for fixed mass).

### 3.2 Per-cell multiplicity

By P-Multiplicity-$g$, each Planck-cell at the horizon supports $g$ distinguishable rule-type configurations. The substrate is approximately independent across cells (decoupling surface structure, I-039).

### 3.3 Entropy computation

By I-068 (von Neumann entropy = Shannon entropy on diagonal probabilities), for $N$ independent cells each with multiplicity $g$:
$$S = N \cdot \log g .$$

Substituting $N = A/(4\pi \ell_P^2)$:
$$S = \frac{(\log g)}{4\pi} \cdot \frac{A}{\ell_P^2} .$$

### 3.4 Area-law form FORCED

The functional form $S \propto A$ is **FORCED** by the composition above. The numerical prefactor $(\log g)/(4\pi)$ depends on $g$, which is INHERITED — not derived in this paper.

To match Bekenstein–Hawking ($S = A/(4\ell_P^2)$), $g$ must be set such that $(\log g)/(4\pi) = 1/4$, giving $\log g = \pi$. This is **matching**, not derivation.

---

## §4 Distinguishing Structural vs Inherited Content

- **Structural (D-via-I):** Area-law form $S \propto A$. Composition of holographic count + per-cell entropy.
- **Inherited (I):** Numerical coefficient $\log g$ (and hence the $1/4$ factor). $g$ is matched against standard quantum-statistical-mechanics.
- **OPEN:** Substrate derivation of $\log g$ from substrate combinatorics.

The substrate program **does not derive** the Bekenstein–Hawking $1/4$; it derives the **area-law form** and supplies a postulate (P-Multiplicity-$g$) that, with appropriate $g$, recovers the standard coefficient.

---

## §5 Falsification Criteria

- **F1:** Empirical detection of black-hole entropy with $S \not\propto A$ — refutes the area-law form (and standard BH thermodynamics).
- **F2:** Substrate evidence that the holographic count (I-025) does not saturate at the horizon — refutes P-Horizon-Participation.
- **F3:** Substrate evidence that per-cell multiplicity $g < 2$ — refutes P-Multiplicity-$g$.
- **F4:** Empirical detection of $S = c \cdot A^\alpha$ for $\alpha \ne 1$ — refutes the area-law form.

---

## §6 Position Statement

The black-hole area-law form $S \propto A$ is **FORM-FORCED** in ED via Paper_025 + Paper_039 + Paper_068 + paper-specific postulates. The Bekenstein–Hawking coefficient $1/4$ is **INHERITED** via $\log g$ matching, **not derived**. Substrate derivation of $\log g$ from substrate combinatorics is OPEN.

---

**End Paper 043 (FIXED).**
