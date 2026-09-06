# -*- coding: utf-8 -*-
"""Does the generation wobble depth w order by COMMITMENT DEGREES OF FREEDOM?

AP's Path B instruction, 2026-09-06: "construct the pattern for other particles
using your relational commitment principles, do not look for masses directly.
Look for the degrees of freedom that define the commitment."

Existing corpus work (theory/Note_MassArc_Koide_CoherenceReframe.md,
theory/Paper_Koide_GenerationCoherenceMap.md) established:

    Q = 1/3 + w^2/6          (Brannen form; Q depends ONLY on wobble depth w)

and mapped w across families against CHARGE, giving w ~ 1.61 + 0.20*Q_charge.
That map predicted neutrinos at w ~ 1.63, Q_nu ~ 0.77, and was FALSIFIED in
2026-08: measured mass-squared splittings bound Q_nu <= 0.586 (normal ordering)
regardless of the unknown lightest mass, so the wobble SHRINKS toward the
neutral corner rather than growing.

This script tests a different ordering variable -- not charge, and not any mass
quantity, but a COUNT: how many distinct gauge sectors (i.e. how many distinct
classes of P05-transporting channel) the family couples to.  That is a
commitment-DOF count in ED's own variables, since P11 selects one channel from
the participating set.

It fits nothing.  It checks an ORDERING.

Run: python "internal notes/_check_commitment_dof_ordering.py"
"""
import math

# Q values: charged leptons exact (Koide); quark values from the corpus's
# Brannen fit, flagged scheme-dependent there; neutrino is a measured BOUND.
FAMILIES = [
    #  name                    Q       kind        gauge sectors coupled
    ("neutrinos (nu1,2,3)",    0.586, "bound",     1, "weak"),
    ("charged leptons (e,mu,tau)", 2.0 / 3.0, "exact", 2, "weak + EM"),
    ("down quarks (d,s,b)",    0.731, "fit",       3, "weak + EM + colour"),
    ("up quarks (u,c,t)",      0.849, "fit",       3, "weak + EM + colour"),
]


def w_of(Q):
    """Brannen wobble depth from the Koide ratio: Q = 1/3 + w^2/6."""
    return math.sqrt(6.0 * Q - 2.0)


print("Commitment-DOF ordering test")
print("=" * 78)
print("\nQ = 1/3 + w^2/6   =>   w = sqrt(6Q - 2)\n")
print("  %-28s %8s %8s %7s  %s" % ("family", "Q", "w", "sectors", "couples to"))
rows = []
for name, Q, kind, n, what in FAMILIES:
    w = w_of(Q)
    tag = {"exact": "", "bound": "  (upper bound)", "fit": "  (scheme-dependent)"}[kind]
    print("  %-28s %8.4f %8.4f %7d  %s%s" % (name, Q, w, n, what, tag))
    rows.append((name, w, n, kind))

print("""
ORDERING CHECK
""")
ws = [r[1] for r in rows]
ns = [r[2] for r in rows]
print("  w  ordering : " + " < ".join("%.3f" % x for x in ws))
print("  DOF ordering: " + " <= ".join(str(x) for x in ns))
mono = all(ws[i] < ws[i + 1] for i in range(len(ws) - 1))
consistent = all((ns[i] < ns[j]) <= (ws[i] < ws[j])
                 for i in range(len(ws)) for j in range(len(ws)))
print("\n  w strictly increasing across the listed order : %s" % mono)
print("  no DOF inversion (n_i < n_j implies w_i < w_j) : %s" % consistent)

print("""
WHAT THIS DOES AND DOES NOT SHOW

  SHOWS -- the coarse ordering is consistent with a DOF COUNT, and in
  particular the NEUTRINO DIRECTION IS RIGHT.  The corpus's earlier
  charge-linear map extrapolated neutrinos UPWARD (w ~ 1.63) and was falsified
  by the measured splittings.  A sector count puts neutrinos BELOW charged
  leptons, because they couple to fewer sectors -- which is the direction the
  data actually took.  So the datum that killed the charge map is the datum
  that supports this one.

  DOES NOT SHOW -- the d/u split.  Both are 3-sector families and their w
  values differ (1.545 vs 1.759), so the count is degenerate exactly where
  charge is not.  A complete account needs both, and this supplies one.

  DOES NOT SHOW -- any value.  Not w = sqrt(2) for the charged leptons, not
  delta ~ 2/9, not the Z_3 generation structure itself.  Those remain the
  three open questions the corpus already names.

  TIER -- structural postdiction of an ORDERING over four families with three
  distinct DOF values, two of whose w's are scheme-dependent.  That is weak
  evidence, and it is stated as weak.  Its one virtue is that it is a
  DIRECTION predicted from a count, not a value fitted to masses -- which is
  what the instruction asked for and what the falsified map did not do.
""")
