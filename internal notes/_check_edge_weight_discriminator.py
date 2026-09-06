# -*- coding: utf-8 -*-
"""Does anything in ED distinguish the geometric mean from min as the w(e) map?

Paper_Individuation_TheSystemEnvironmentCut section 2.1 wrote

    w(u,v) = sum over channels K shared by u and v of sqrt( b_K(u) b_K(v) )

and recorded, honestly, that min(b_K(u), b_K(v)) satisfies the same five
requirements -- a "bottleneck" reading rather than an amplitude-product one --
and that the geometric mean was chosen by the corpus's convention, not forced.

This script builds the construction that decides it.  The decisive input is NOT
the evidence used to justify the geometric mean in the first place (that would
be circular).  It is a different established fact:

  * P-Motif-Algebra (Paper_007 section 2, a named censused postulate): substrate
    amplitude content is a COMPLEX VECTOR SPACE under componentwise addition.
    So when contributions combine, AMPLITUDES add, and b = |sum of P|^2.
    Canonical Paper_087's Coh operationalization already uses exactly this rule:
    Coh = |sum_a P_a|^2 - sum_a |P_a|^2.

  * P03 supplies "the locus index set".  An index set is a bookkeeping choice.

REQUIREMENT (R) -- regridding consistency.  b_bdry(S) is supposed to be a
property of the CUT.  Merge two loci that lie on the SAME side of the cut into
one coarser locus.  The boundary bandwidth must not change:

    w(U, v) = w(u1, v) + w(u2, v)      for U the merge of u1, u2

stated for phase-ALIGNED merges, which is the weakest defensible form: merging
two already-coherent loci should not move the boundary.  (For misaligned merges
no weight can be additive, because merging genuinely destroys shared amplitude;
that is physics, not bookkeeping.  Test 2 shows the two candidates handle that
deficit very differently.)

Run: python "internal notes/_check_edge_weight_discriminator.py"
"""
import math


def gm(bu, bv):
    return math.sqrt(bu * bv)


def mn(bu, bv):
    return min(bu, bv)


def pmean(p):
    """Power mean M_p; M_0 = geometric mean, M_-inf = min.  All satisfy
    M(b,b) = b, so the whole family is correctly normalized."""
    def f(bu, bv):
        if bu <= 0 or bv <= 0:
            return 0.0
        if p == 0:
            return math.sqrt(bu * bv)
        return (0.5 * (bu ** p + bv ** p)) ** (1.0 / p)
    return f


CAND = [("geometric mean sqrt(bu bv)", gm), ("min(bu, bv)", mn)]

print("Edge-weight discriminator: geometric mean vs min")
print("=" * 78)

# ---------------------------------------------------------------- test 1 ----
print("""
TEST 1 -- Regridding a cut.  N loci on the system side, phase-ALIGNED, each with
b_K = 1 on the shared channel, all adjacent to one outside locus v with b_K(v)=1.
Merge them into a single coarse locus U.  Amplitude addition (P-Motif-Algebra)
gives P_K(U) = N * 1, hence b_K(U) = N^2.  Boundary weight must not change.
""")
print("   %-28s %10s %10s %10s" % ("map", "N", "unmerged", "merged"))
for name, f in CAND:
    for N in (1, 2, 4, 10):
        unmerged = N * f(1.0, 1.0)
        merged = f(float(N * N), 1.0)
        flag = "  OK" if abs(unmerged - merged) < 1e-12 else "  <-- CHANGED by regridding"
        print("   %-28s %10d %10.2f %10.2f%s" % (name, N, unmerged, merged, flag))
print("""   Reading: the geometric mean is EXACT for every N -- sqrt(N^2 * 1) = N.
   min is wrong by a factor of N: it saturates at b_K(v) and stops seeing the
   system side at all.  Under min, b_bdry is a function of how finely the
   substrate is indexed, not of the cut.""")

# ---------------------------------------------------------------- test 2 ----
print("""
TEST 2 -- Misaligned merge.  Same two loci, relative phase d.  Now b_K(U) =
|P1 + P2|^2 = 2 + 2cos d, which is genuinely less than 2: merging destroys
shared amplitude.  The question is whether the merge deficit is a property of
the MERGED PAIR alone, or leaks in a dependence on the outside locus v.
""")
print("   %-22s %8s %10s %10s %10s" % ("map", "b_K(v)", "d=0", "d=pi/2", "d=2pi/3"))
for name, f in CAND:
    for bv in (0.25, 1.0, 9.0):
        row = []
        for d in (0.0, math.pi / 2, 2 * math.pi / 3):
            bU = 2 + 2 * math.cos(d)
            row.append(f(bU, bv) / (2 * f(1.0, bv)))
        print("   %-22s %8.2f %10.4f %10.4f %10.4f" % (name, bv, row[0], row[1], row[2]))
print("""   Reading: for the geometric mean the deficit ratio is |P1+P2|/(|P1|+|P2|)
   -- identical down all three b_K(v) rows.  Regridding the system side
   FACTORIZES out of the environment side, and the deficit is exactly the
   amplitude triangle inequality, i.e. exactly the deficit Coh already records.
   For min the ratio changes with b_K(v): the system-side graining and the
   environment bandwidth do not separate.""")

# ---------------------------------------------------------------- test 3 ----
print("""
TEST 3 -- Can regridding ALONE flip the individuation verdict?  Regrid only the
ENVIRONMENT side, so the system and its internal bandwidth are untouched and
every change is in b_bdry.  Environment = M aligned loci, each b_K = 1 on the
channel shared with the system's boundary locus, which carries b_leak = 0.25.
Internal bandwidth b_int = 1.5, threshold theta_ind = 2.0.
""")
THETA, B_INT, B_LEAK, M = 2.0, 1.5, 0.25, 4


def bdry_fine(f):
    return M * f(B_LEAK, 1.0)


def bdry_coarse(f):
    # M aligned environment loci merge by amplitude addition -> b = (M*1)^2
    return f(B_LEAK, float(M * M))


print("   %-28s %9s %9s %9s %9s %s"
      % ("map", "bd fine", "bd coarse", "r fine", "r coarse", "verdict fine -> coarse"))
for name, f in CAND:
    bf, bc = bdry_fine(f), bdry_coarse(f)
    rf, rc = B_INT / bf, B_INT / bc
    vf = "indiv" if rf > THETA else "not"
    vc = "indiv" if rc > THETA else "not"
    tag = "  <-- FLIPPED by regridding alone" if vf != vc else "  stable"
    print("   %-28s %9.4f %9.4f %9.4f %9.4f %s -> %s%s"
          % (name, bf, bc, rf, rc, vf, vc, tag))
print("""   Reading: under the geometric mean the boundary bandwidth and the verdict
   are untouched by how finely the environment is indexed.  Under min the same
   physical system is NOT individuated on the fine grid and IS individuated on
   the coarse one.  b_bdry is the denominator of the individuation ratio and the
   quantity F-IND-1 is a falsifier for; if it moves with the indexing, F-IND-1
   is not a falsifier and the ratio is not a measurable quantity.""")

# ---------------------------------------------------------------- test 4 ----
print("""
TEST 4 -- Is the geometric mean merely one that works, or the only one?  Scan
the power-mean family M_p, which interpolates continuously between min (p ->
-inf) and the geometric mean (p = 0), and which is correctly normalized for
every p since M_p(b,b) = b.  Report the worst regridding violation over N.
""")
print("   %10s %-24s %16s" % ("p", "M_p", "max |merged - unmerged|"))
for p in (-8.0, -4.0, -2.0, -1.0, -0.5, -0.1, 0.0, 0.1, 0.5):
    f = pmean(p)
    worst = max(abs(f(float(N * N), 1.0) - N * f(1.0, 1.0)) for N in (2, 3, 4, 10))
    label = {0.0: "geometric mean", -1.0: "harmonic mean"}.get(p, "")
    print("   %10.2f %-24s %16.6f %s"
          % (p, label, worst, "  <== unique zero" if worst < 1e-12 else ""))
print("""   Reading: the violation vanishes at p = 0 and nowhere else.  Note also
   that every p > 0 already fails an earlier requirement -- M_p(b, 0) != 0, so
   an unshared channel would still carry weight -- which is why the honest
   fork was between p = 0 and p -> -inf in the first place.""")

# ---------------------------------------------------------------- proof ------
print("""
THE ARGUMENT BEHIND THE SCAN (why p = 0 is forced, not merely selected)

  Write the edge weight as w = f(b_u, b_v), non-decreasing in each argument
  (more bandwidth cannot mean less shared capacity).  Requirement (R) for
  phase-aligned merges says, for amplitudes x1 = |P(u1)|, x2 = |P(u2)|:

      f((x1 + x2)^2, b_v) = f(x1^2, b_v) + f(x2^2, b_v)

  Set g(x) = f(x^2, b_v).  Then g(x1 + x2) = g(x1) + g(x2) for all x1, x2 >= 0
  -- Cauchy's functional equation -- and g is monotone, so g(x) = c(b_v) x.
  Hence f(b_u, b_v) = c(b_v) sqrt(b_u).  Symmetry in u and v forces
  c(b_v) = c sqrt(b_v), and f(b, b) = b fixes c = 1:

      f(b_u, b_v) = sqrt(b_u b_v).      QED

  The geometric mean is the UNIQUE regridding-consistent edge weight, given
  that contributions combine by amplitude addition.

  And the fork is not independent -- it is the merge rule in disguise.  Had
  bandwidth itself been additive under merging (b_K(U) = b1 + b2) rather than
  amplitude, the same Cauchy argument in b would give f linear in each
  argument, i.e. the PRODUCT c * b_u * b_v, and BOTH candidates would fail.
  Whatever rule governs coarse-graining loci fixes the edge weight.  ED's rule
  is amplitude addition (P-Motif-Algebra, Paper_007 section 2; and canonical
  Paper_087 already computes Coh as |sum_a P_a|^2 - sum_a |P_a|^2 on exactly
  that rule).  So ED's edge weight is the geometric mean.

WHAT IS ASSUMED, STATED PLAINLY

  Requirement (R) is an assumption, not a theorem: that b_bdry is a property of
  the cut rather than of the locus indexing.  It is the standard demand on any
  coarse-grained quantity, it is the weakest useful form (same-side, phase-
  aligned merges only), and without it the individuation ratio is not a
  measurable quantity and F-IND-1 is not a falsifier.  The result is therefore
  D-via-I conditional on (R) + P-Motif-Algebra -- not unconditional.
""")
