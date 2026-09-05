# -*- coding: utf-8 -*-
"""Paper_030's cross-term sign, checked numerically (2026-09-05, late).

Paper_030 sections 4.3 and 5.2 published

    Sigma_cross(R) = - sqrt(G M a0) * log(R/R0)

while Paper_QuadraticStrain_v1 section 5.1 has the same quantity with a PLUS.
Only one can be right. Convention throughout: a_r = -dSigma/dR, and a NEGATIVE
a_r is inward, i.e. attractive.

Run: python "internal notes/_check_030_cross_sign.py"
"""
import math

G, M, a0, R0 = 6.674e-11, 2.0e30, 1.2e-10, 1.0e19
k = math.sqrt(G * M * a0)

def d(f, R, h=1e12):
    return (f(R + h) - f(R - h)) / (2 * h)

Sigma_N      = lambda R: -G * M / R              # Paper_030 sec 5.1
cross_minus  = lambda R: -k * math.log(R / R0)   # Paper_030 secs 4.3, 5.2 as published
cross_plus   = lambda R: +k * math.log(R / R0)   # Paper_QuadraticStrain_v1 sec 5.1

R = 5e19
target = -(G * M / R**2) - k / R                 # both terms inward

print("a_r = -dSigma/dR ; negative = inward = attractive\n")
for label, S in (("Sigma_N          = -GM/R",   Sigma_N),
                 ("cross, published = -k lnR",  cross_minus),
                 ("cross, corrected = +k lnR",  cross_plus)):
    a = -d(S, R)
    print("  %-28s a_r = %+.4e   %s"
          % (label, a, "attractive" if a < 0 else "REPULSIVE"))

pub = -(d(Sigma_N, R) + d(cross_minus, R))
cor = -(d(Sigma_N, R) + d(cross_plus,  R))
print("\n  Paper_030 as published   a_r = %+.4e   %s" % (pub, "REPULSIVE" if pub > 0 else ""))
print("  with the corrected sign  a_r = %+.4e" % cor)
print("  target                   a_r = %+.4e" % target)
assert abs(cor - target) < 1e-6 * abs(target)
assert pub > 0
print("""
  How it stayed hidden: section 5.3 writes

      a = -dSigma_N/dR - dSigma_cross/dR = GM/R^2 + sqrt(GMa0)/R

  quoting the Newtonian term as a MAGNITUDE (its signed value is -GM/R^2)
  and the cross term at FACE VALUE, then adding them as though both pointed
  inward. The stated result of 5.3 is correct; the Sigma it is derived from
  is not. Corrected to +sqrt(GMa0) log(R/R0), matching Paper_QuadraticStrain
  and the three-way sign check. No downstream result moves.
""")
