# -*- coding: utf-8 -*-
"""Does Penrose's collapse energy E_Delta equal -Sigma_C?  (2026-09-05)

The 2026-09-05 sign check settled the P12 split:

    Str_K = sum_a b_K^(a)                            the diagonal
    Coh_K = 2 sum_{a<b} sqrt(b_a b_b) cos Theta_ab   the off-diagonal

and ED_Reading_ManyWorlds says commitment is the diagonalization of rho: it
destroys the off-diagonal coherences and leaves the diagonal facts.  If that
correspondence is real, then for a two-BRANCH superposition (a = 1, 2 indexing
the branches rather than source regions) the P12 landscape should be the
collapse energy the state-reduction arc already uses.

Penrose / Diosi:

    E_Delta = -G int int [rho_1 - rho_2](x) [rho_1 - rho_2](y) / |x-y|
            = E_11 + E_22 - 2 E_12

which is DIAGONAL minus TWICE THE CROSS TERM -- structurally Str - Coh.  With
Paper_030 sec 4.2's identification of per-channel bandwidth as potential content,
b^(a) is the branch's own gravitational content and sqrt(b_1 b_2) cos Theta is
the mutual term.  So the claim under test is

    E_Delta  =  Str - Coh  =  -(Sigma_C + Grad)  ~  -Sigma_C

This script checks the algebra and the two limits that would kill it.

Run: python "internal notes/_check_collapse_correspondence.py"
"""
import math

def E_pair(b1, b2, theta):
    """ED reading: diagonal minus off-diagonal, from the settled P12 split."""
    Str = b1 + b2
    Coh = 2.0 * math.sqrt(b1 * b2) * math.cos(theta)
    return Str - Coh, Str, Coh

def E_penrose(E11, E22, E12):
    """Standard expansion of the Penrose self-energy of the difference."""
    return E11 + E22 - 2.0 * E12

print("Collapse-energy correspondence check")
print("=" * 78)
print("Claim under test:  E_Delta = Str - Coh = -(Sigma_C + Grad)\n")

# --- 1. algebraic identity, term by term -------------------------------------
print("1. Term-by-term identity (b_a <-> branch content, sqrt(b1 b2)cos <-> E_12)\n")
hdr = "%-28s %12s %12s %12s" % ("case", "Str - Coh", "Penrose", "match")
print(hdr); print("-" * len(hdr))
ok_all = True
for label, b1, b2, th in [
        ("identical, in phase",      1.0, 1.0, 0.0),
        ("identical, anti-phase",    1.0, 1.0, math.pi),
        ("identical, quadrature",    1.0, 1.0, math.pi / 2),
        ("unequal 4:1, in phase",    4.0, 1.0, 0.0),
        ("unequal 4:1, anti-phase",  4.0, 1.0, math.pi),
        ("unequal 9:1, quadrature",  9.0, 1.0, math.pi / 2)]:
    ed, Str, Coh = E_pair(b1, b2, th)
    pen = E_penrose(b1, b2, math.sqrt(b1 * b2) * math.cos(th))
    ok = abs(ed - pen) < 1e-12
    ok_all &= ok
    print("%-28s %12.6f %12.6f %12s" % (label, ed, pen, "YES" if ok else "NO"))
assert ok_all
print("\n   Identity holds exactly.  It is the same expansion of the same square,\n"
      "   with E_12 = sqrt(b1 b2) cos(Theta) as ED's phase-carrying mutual term.\n")

# --- 2. the two limits that would kill it ------------------------------------
print("2. Limiting behaviour -- where a wrong correspondence would show\n")
print("   %-42s %10s %10s" % ("configuration", "E_Delta", "Sigma_C"))
print("   " + "-" * 64)
for label, b1, b2, th in [
        ("branches identical and in phase",      1.0, 1.0, 0.0),
        ("branches maximally distinguishable",   1.0, 1.0, math.pi),
        ("one branch vanishing (b2 -> 0)",       1.0, 1e-9, 0.0)]:
    ed, Str, Coh = E_pair(b1, b2, th)
    print("   %-42s %10.6f %10.6f" % (label, ed, -ed))

print("""
   Reading:

     Identical, in-phase branches  ->  E_Delta = 0, Sigma_C = 0.
       No separation, no collapse pressure.  Correct: Penrose's rate
       1/tau = E_Delta/hbar vanishes when there is nothing to collapse between.

     Maximally distinguishable     ->  E_Delta = 4b, its maximum.
       Correct: fastest collapse when the branches are most separated.

     One branch vanishing          ->  E_Delta -> b, the surviving self-energy.
       Correct: a lone branch has no interference to destroy.

   Sigma_C = Coh - Str is NEGATIVE-or-zero throughout for a two-branch state,
   zero only at perfect coherence.  A superposition sits at Sigma_C = 0 and
   commitment drives it down.  That is the right sign for an instability.
""")

# --- 3. what is ED-distinctive here ------------------------------------------
print("3. Where ED and Diosi-Penrose come apart\n")
print("   %-24s %14s %14s" % ("relative phase", "ED E_Delta", "DP E_Delta"))
print("   " + "-" * 54)
for th, name in [(0.0, "0 (in phase)"), (math.pi/3, "pi/3"),
                 (math.pi/2, "pi/2"), (math.pi, "pi (anti)")]:
    ed, _, _ = E_pair(1.0, 1.0, th)
    dp = 1.0 + 1.0 - 2.0 * 1.0        # DP has no phase: E_12 is a real overlap
    print("   %-24s %14.6f %14.6f" % (name, ed, dp))

print("""
   DP's E_12 is a real overlap integral with no phase, so its E_Delta is
   phase-INDEPENDENT.  ED's carries cos(Theta), so ED's collapse energy --
   and hence its collapse RATE -- depends on the relative phase between
   branches, which is exactly the quantity an interferometer controls.

   Recorded as a consequence to check, NOT as a prediction: whether Theta is
   controllable, fixed, or randomised in a real superposition is not settled
   by anything here, and if it randomises the dependence averages away.
""")
