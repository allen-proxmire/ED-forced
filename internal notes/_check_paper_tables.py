# -*- coding: utf-8 -*-
"""Verify the paper's hand-typed tables against the script that produced them.

This is the check most likely to find something. The numbers in sections 5.3 and
5.3b were transcribed from console output by hand; a transposed digit there would
survive every other check in this session and would be found by a referee.
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\allen\GitHub\event-density\theory")
import numpy as np
import a0z_powerlaw_refit as R

P = r"C:\Users\allen\GitHub\ED Generative\physics-papers\gravity\Paper_a0z_MONDScaleTracksHubbleRate.md"
doc = io.open(P, encoding="utf-8").read()

bad = 0


def cmp(label, computed, claimed, tol):
    global bad
    ok = abs(computed - claimed) <= tol
    if not ok:
        bad += 1
    print("   %-46s script %8.3f   paper %8.3f   %s"
          % (label, computed, claimed, "OK" if ok else "*** MISMATCH ***"))


print()
print("=" * 74)
print("PAPER TABLES vs THE SCRIPT THAT PRODUCED THEM")
print("=" * 74)

# ---- section 5.3: the local-exponent table ----------------------------------
print("\n1. Section 5.3, local exponent d ln a0 / d ln H")
m = re.search(r"\| local `\u03b1` \|([^\n]+)\|", doc)
assert m, "local alpha row not found in the paper"
claimed = [float(x) for x in m.group(1).split("|") if x.strip()]
zs = (0.33, 0.50, 0.75, 1.00, 1.25, 1.44)
assert len(claimed) == len(zs), (len(claimed), len(zs))
for z, c in zip(zs, claimed):
    cmp("local alpha at z = %.2f" % z, R.alpha_local(z, R.A0_0, R.A1, R.OM), c, 0.005)

# ---- section 5.3b: the shape table ------------------------------------------
print("\n2. Section 5.3b, shape comparison")
zg = np.linspace(R.Z_LO, R.Z_HI, 501)
lin_g = R.A0_0 + R.A1 * zg
ed_g = R.hubble(zg, R.OM)
r = lin_g / ed_g
A = float(np.sqrt(r.min() * r.max()))
print("   (minimax amplitude A = %.3f)" % A)

for label, fn in (("their fit", lambda z: R.A0_0 + R.A1 * z),
                  ("ED alpha=1", lambda z: A * R.hubble(z, R.OM))):
    m = re.search(r"\| %s[^|]*\|([^\n]+)\|" % re.escape(label.split()[0]), doc)

m = re.search(r"\| their fit \|([^\n]+)\|", doc)
assert m, "their-fit row not found"
for z, c in zip(zs, [float(x) for x in m.group(1).split("|") if x.strip()]):
    cmp("their fit at z = %.2f" % z, R.A0_0 + R.A1 * z, c, 0.006)

m = re.search(r"\| ED, `\u03b1 = 1` \|([^\n]+)\|", doc)
assert m, "ED row not found"
for z, c in zip(zs, [float(x) for x in m.group(1).split("|") if x.strip()]):
    cmp("ED curve at z = %.2f" % z, A * R.hubble(z, R.OM), c, 0.006)

m = re.search(r"\| deviation \|([^\n]+)\|", doc)
assert m, "deviation row not found"
dev_claimed = [float(x.replace("*", "").replace("%", "").replace("\u2212", "-").strip())
               for x in m.group(1).split("|") if x.strip()]
for z, c in zip(zs, dev_claimed):
    l = R.A0_0 + R.A1 * z
    e = A * R.hubble(z, R.OM)
    cmp("deviation at z = %.2f (%%)" % z, 100.0 * (e - l) / l, c, 0.06)

# ---- prose claims ------------------------------------------------------------
print("\n3. Prose numbers")
lo = R.alpha_local(R.Z_HI, R.A0_0, R.A1, R.OM)
hi = R.alpha_local(R.Z_LO, R.A0_0, R.A1, R.OM)
cmp("local alpha range, low end", lo, 0.90, 0.005)
cmp("local alpha range, high end", hi, 1.78, 0.005)

zz = np.linspace(0.5, 2.0, 20001)
cross = float(zz[np.argmin(abs(R.alpha_local(zz, R.A0_0, R.A1, R.OM) - 1.0))])
cmp("alpha = 1 crossing redshift", cross, 1.1, 0.02)

vals = sorted(fn(R.A0_0, R.A1, R.OM) for _, fn in R.METHODS)
claimed_methods = [1.118, 1.147, 1.162, 1.178]
for v, c in zip(vals, claimed_methods):
    cmp("reduction value", float(v), c, 0.001)

cmp("endpoint reduction (the corpus's 1.178)",
    float(R.alpha_endpoint(R.A0_0, R.A1, R.OM)), 1.178, 0.001)

worst = float(np.abs(100.0 * (A * ed_g - lin_g) / lin_g).max())
cmp("worst shape deviation (%)", worst, 6.5, 0.06)

print()
print("=" * 74)
print("RESULT: %s" % ("CLEAN - every table entry reproduces" if not bad
                      else "%d MISMATCH(ES) - fix the paper" % bad))
print("=" * 74)
print()
sys.exit(1 if bad else 0)
