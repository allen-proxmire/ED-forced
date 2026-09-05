# -*- coding: utf-8 -*-
"""Compatibility check for the proposed Grad (2026-09-05).

AP's reading of the three P12 terms is Relation / Boundary / Gradient.  The
2026-09-05 sign check independently fixed the first two:

    Coh_K = 2 sum_{a<b} sqrt(b_a b_b) cos Theta_ab   the OFF-diagonal
    Str_K = sum_a b_K^(a)                            the diagonal

Coh vanishes for a single source and exists only when two contributions meet,
which is exactly "relation".  Str is the load against P04's finite per-locus
capacity, which is exactly "boundary".  Both are built from the participation
amplitude P_K = sqrt(b_K) e^{i pi_K}, and both live AT a locus.

That leaves Grad as the only INTER-locus term, and fixes what it should be
built from: the same amplitude, differenced across an edge.  The natural
quadratic form is the discrete Dirichlet form,

    Grad = sum_K sum_<u,v> |P_K(v) - P_K(u)|^2
         = sum_K sum_<u,v> [ b_K(v) + b_K(u) - 2 sqrt(b_K(v) b_K(u)) cos(dpi) ]

This script asks the one question that could kill it: does adding a Dirichlet
Grad break the established a(R) = a_N + sqrt(a_N a_0)?

Run: python "internal notes/_check_grad_compat.py"
"""
import math

G, M, a0 = 6.674e-11, 2.0e30, 1.2e-10
l_ED = 1.616e-35                      # P08 substrate scale
c = 2.998e8

# b^(L) proportional to GM/R (Paper_030 sec 4.2), so P = sqrt(b) ~ sqrt(GM/R).
# Across one edge of length l_ED the Dirichlet contribution per channel is
#     |dP/dR|^2 * l_ED^2 ,  with  P(R) = sqrt(GM/R)
#     dP/dR = -(1/2) sqrt(GM) R^{-3/2}
#     |dP/dR|^2 = (1/4) GM / R^3
def grad_term(R):
    return 0.25 * G * M / R**3 * l_ED**2

def dgrad(R):
    return -0.75 * G * M / R**4 * l_ED**2

def a_newton(R):   return -G * M / R**2
def a_mond(R):     return -math.sqrt(G * M * a0) / R
# Sigma_C contains -Grad, so a_r gets -d(-Grad)/dR = +dGrad/dR
def a_grad(R):     return dgrad(R)

print("Grad compatibility check\n" + "=" * 78)
print("Proposed:  Grad = sum |P(v) - P(u)|^2   (discrete Dirichlet form)\n")
hdr = "%-14s %14s %14s %14s %12s" % ("R (m)", "a_Newton", "a_MOND", "a_Grad", "|Grad/N|")
print(hdr); print("-" * len(hdr))
for R, name in ((1e7, "neutron star"), (7e8, "solar radius"),
                (1.5e11, "1 AU"), (1e19, "galactic"), (1e21, "outer halo")):
    aN, aM, aG = a_newton(R), a_mond(R), a_grad(R)
    print("%-14s %14.3e %14.3e %14.3e %12.2e   %s"
          % ("%.1e" % R, aN, aM, aG, abs(aG / aN), name))

print("""
Reading:

  Grad enters a_r as +dGrad/dR = -(3/4) l_ED^2 GM / R^4 -- ATTRACTIVE, and
  suppressed by l_ED^2 relative to Newton by a factor l_ED^2 / R^2.  At every
  scale in the table that is between 10^-90 and 10^-113.  The established
  results are untouched to any conceivable precision.

  So the Dirichlet Grad is COMPATIBLE.  It is not confirmed by this -- a
  compatibility check cannot confirm anything -- but the obvious way for the
  proposal to die is that it wrecks Newton, and it does not.

  Note the sign: Grad contributes ATTRACTIVELY, which is not automatic.  The
  Dirichlet form is non-negative and enters Sigma_C with a minus, and the
  radial falloff of b^(L) then makes dGrad/dR negative.  A Grad built from
  bandwidth difference rather than amplitude difference gives a different
  power and, for some choices, the wrong sign.
""")

# The phase half of the Dirichlet form, which is the interesting part
print("The phase half, and an item it raises:\n")
print("""  |P(v) - P(u)|^2 = b(v) + b(u) - 2 sqrt(b(v) b(u)) cos(dpi)

  Sigma_C carries -Grad, so that last term enters as

      + 2 sqrt(b(v) b(u)) cos(dpi)

  i.e. Sigma_C is RAISED when the phase is aligned ACROSS AN EDGE.  Alignment
  across edges is favoured, with the P05 connection transporting the phase.

  That is what Paper_PhaseCoherence_P12Coh's simulator actually measures: it
  deposits phase from COMMITTED NEIGHBOURS across edges via the P05 connection.
  So the measured phase-alignment result may belong to Grad rather than to Coh.
  Both reward alignment and both come from the same amplitude structure, so
  nothing breaks either way -- but which term the measurement belongs to is
  now an open question, and it is not settled here.
""")
