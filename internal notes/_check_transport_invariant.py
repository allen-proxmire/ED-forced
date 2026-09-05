# -*- coding: utf-8 -*-
"""Numerical check for Paper_UnifiedP04TransportBudget section 9.

Verifies that the three forms of the transport-wall invariant agree:
    eta_min * rho_max  ==  pF^2 / (3 e^2)  ==  (hbar kF^2 / 6 pi) * R_K
and that Lambda = eta rho e^2 / pF^2 = Pi_p Pi_q = 1/3.

Run: python "internal notes/_check_transport_invariant.py"
"""
import math

hbar = 1.054571817e-34      # J s
e    = 1.602176634e-19      # C

kF = 1e10                   # m^-1, a representative metallic Fermi wavevector
a  = 3e-10                  # m,    the DCGT cell taken at a lattice spacing

n   = kF**3 / (3 * math.pi**2)      # carrier density implied by kF (free-electron)
pF  = hbar * kF                     # carrier momentum

eta = (1/3) * n * pF * a            # Pi_p = 1/3, floored at l = a
rho = pF / (n * e**2 * a)           # Pi_q = 1,   floored at l = a

product = eta * rho
form_pF = pF**2 / (3 * e**2)
R_K     = 2 * math.pi * hbar / e**2
form_RK = hbar * kF**2 / (6 * math.pi) * R_K
Lambda  = product * e**2 / pF**2

print("n        = %.4e m^-3" % n)
print("pF       = %.4e kg m/s" % pF)
print("eta_min  = %.4e Pa s" % eta)
print("rho_max  = %.4e Ohm m = %.0f uOhm cm" % (rho, rho * 1e8))
print()
print("eta*rho          = %.6e" % product)
print("pF^2/(3 e^2)     = %.6e   ratio %.12f" % (form_pF, product / form_pF))
print("(hbar kF^2/6pi)RK= %.6e   ratio %.12f" % (form_RK, product / form_RK))
print("Lambda           = %.12f   (expected 1/3 = %.12f)" % (Lambda, 1/3))

assert abs(product / form_pF - 1) < 1e-12
assert abs(product / form_RK - 1) < 1e-12
assert abs(Lambda - 1/3)         < 1e-12
print("\nAll three forms agree. Lambda is independent of n and a by construction:")
for kk, aa in ((5e9, 2e-10), (2e10, 5e-10), (1e10, 1e-9)):
    nn = kk**3 / (3 * math.pi**2); pp = hbar * kk
    ee = (1/3) * nn * pp * aa; rr = pp / (nn * e**2 * aa)
    print("  kF=%.1e a=%.1e -> Lambda=%.12f" % (kk, aa, ee * rr * e**2 / pp**2))
