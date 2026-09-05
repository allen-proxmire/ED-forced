# -*- coding: utf-8 -*-
"""Three-way sign check on Sigma_C = Coh - Str - Grad (2026-09-05).

Foundations #10: the object |sum_a P|^2 is assigned to BOTH Coh and Str, which
enter Sigma_C with opposite signs. Three candidate assignments were on the
table. This settles which one reproduces the arc's established result

    a(R) = a_N + sqrt(a_N a_0),   a_N = GM/R^2,   sqrt(a_N a_0) = sqrt(G M a_0)/R

from Paper_030 / Paper_QuadraticStrain_v1 sections 4-5.

Inputs, all taken from Paper_QuadraticStrain_v1 sections 4 and 5.1 and NOT
chosen here:
    diagonal, summed over channels:  D(R) = sum_K b_K^(L) = G M / R
    cross term, after the radial integral with the 1/R bilocal channel density:
                                     X(R) = 2 cos(Theta) sqrt(b^L b^H) summed
                                          = cos(Theta) sqrt(G M a_0) ln(R/R0)

P04 makes bandwidth NON-NEGATIVE, so D(R) > 0 is forced, not a convention.
That single fact is what decides the check: see the note at the bottom.

Sign convention: radial component, negative = attractive (inward).
Target:  a_r(R) = -(GM/R^2) - sqrt(G M a_0)/R      (both terms attractive)

Run: python "internal notes/_check_sigma_sign.py"
"""
import math

G, M, a0, R0 = 6.674e-11, 2.0e30, 1.2e-10, 1.0e19
COS_THETA = 1.0                      # constructive; Paper_PhaseCoherence_P12Coh

def D(R):                            # diagonal: sum of NON-NEGATIVE bandwidths
    return G * M / R
def dD(R):
    return -G * M / R**2

def X(R):                            # interference cross term
    return COS_THETA * math.sqrt(G * M * a0) * math.log(R / R0)
def dX(R):
    return COS_THETA * math.sqrt(G * M * a0) / R

def target(R):                       # Paper_030's established result, attractive
    return -(G * M / R**2) - math.sqrt(G * M * a0) / R

# --- the three candidate assignments -----------------------------------------
# a_r = -d(Sigma_C)/dR  in every case (P12).  Grad is dropped throughout: it is
# spherically uninvolved here and identical across the three, so it cannot
# discriminate.

def opt1(R):
    """Coh = Str = |sum P|^2. They cancel identically; Sigma_C = -Grad."""
    return 0.0                       # no gravitational term survives at all

def opt2(R):
    """Str = diagonal only; Coh = the interference part.
       Sigma_C = Coh - Str = X - D."""
    return -(dX(R) - dD(R))

def opt3a(R):
    """Coh sits out; Str = the full square.  Sigma_C = -Str = -(D + X)."""
    return -(-(dD(R) + dX(R)))

def opt3b(R):
    """Same, with Sigma_C = +Str (i.e. if the minus in P12 were dropped)."""
    return -(dD(R) + dX(R))

CASES = [
    ("1  Coh = Str = |sum P|^2 (they cancel)", opt1),
    ("2  Str = diagonal, Coh = interference ", opt2),
    ("3a Coh sits out, Sigma_C = -Str       ", opt3a),
    ("3b Coh sits out, Sigma_C = +Str       ", opt3b),
]

print(__doc__.split("Run:")[0].strip()[:0] or "", end="")
print("Three-way sign check on Sigma_C\n" + "=" * 78)
print("target a_r(R) = -(GM/R^2) - sqrt(GMa0)/R   [both terms attractive]\n")
hdr = "%-40s %14s %14s %10s" % ("assignment", "a_r at 1e19 m", "target", "match")
print(hdr); print("-" * len(hdr))

winners = []
for label, f in CASES:
    Rs = [5e18, 1e19, 5e19, 2e20]
    ok = all(abs(f(R) - target(R)) <= 1e-12 * abs(target(R)) for R in Rs)
    if ok:
        winners.append(label.strip())
    print("%-40s %14.6e %14.6e %10s"
          % (label, f(1e19), target(1e19), "YES" if ok else "no"))

print("\n" + "=" * 78)
print("Reproduces Paper_030's result:", ", ".join(winners) if winners else "NONE")

print("""
Why option 2 and only option 2, in one line:

  The target needs the diagonal and the cross term to enter Sigma_C with
  OPPOSITE signs -- because d(1/R)/dR is negative while d(ln R)/dR is
  positive, so making both accelerations point inward requires opposite
  signs upstream.  A single Str = |sum P|^2 carries them with the SAME
  sign, so no choice of an overall sign on Str can work.  Splitting them
  across Coh (+) and Str (-) is the only assignment that delivers it, and
  P12's own sign pattern -- Sigma_C = Coh - Str - Grad -- is already
  exactly right.  P12 needs no amendment.

Independent confirmation from P04:

  P04 makes bandwidth non-negative, so D(R) = sum_K b_K^(L) > 0 is forced.
  Paper_QuadraticStrain_v1 section 4 writes "Phi_N = sum_K b_K^(L) = -GM/R",
  equating a sum of non-negative quantities with a NEGATIVE number.  Under
  option 2 that minus sign is P12's own -Str and the equation is
  Phi_N = -Str = -sum_K b_K^(L) = -GM/R, which is consistent.  Section 4
  silently absorbed P12's minus sign, and that is what hid the collision.
""")
