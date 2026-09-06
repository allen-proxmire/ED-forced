# -*- coding: utf-8 -*-
"""Does the corpus already need requirement (R)?  Yes -- and it uses the OTHER
merge rule when it does.  This script works out what that costs.

Requirement (R), as stated in _check_edge_weight_discriminator.py: a coarse-
grained quantity must be a property of the cell/cut, not of the indexing inside
it.  Paper_073 (DCGT) section 3.2 already demands exactly this:

    "Well-definedness.  By P03 (spatial homogeneity), translation-invariance of
     substrate-graph operations means the average depends only on (u-bar,t-bar)
     -- the coarse-graining center -- NOT ON THE SPECIFIC SUBSTRATE CHANNELS
     ENUMERATED WITHIN THE CELL.  By P04 (bandwidth additivity), substrate
     bandwidth contributions sum additively within the cell."

So (R) is a standing corpus commitment, not an invention -- and a load-bearing
one, since DCGT section 1 says every continuum-level empirical prediction in the
corpus traces structurally through it.

BUT the second sentence uses a DIFFERENT merge rule from the one the edge-weight
argument used:

    DCGT              b_K(U) = b_1 + b_2            (bandwidth-additive)
    P-Motif-Algebra   b_K(U) = |P_1 + P_2|^2        (amplitude-additive)

and the Cauchy argument is sensitive to which.  This script asks three things:

  A. Are the two rules actually in conflict, or is one the limit of the other?
  B. Under DCGT's rule, what does (R) force the edge weight to be?
  C. Does that change any individuation verdict?

Run: python "internal notes/_check_merge_rule_regimes.py"
"""
import math
import random

random.seed(20260905)

print("Merge rules and requirement (R)")
print("=" * 78)

# ------------------------------------------------------------------- A ------
print("""
A. Are the two merge rules in conflict?  Amplitude-additive merging of n loci
   each with b = 1 gives b_K(U) = |sum of e^{i pi_a}|^2.  Average that over
   random phases and compare with the bandwidth-additive answer, n.
""")
print("   %6s %14s %14s %14s" % ("n", "aligned", "random (mean)", "bandwidth-add"))
for n in (2, 4, 8, 16):
    trials = 200000 // n
    tot = 0.0
    for _ in range(trials):
        re = im = 0.0
        for _a in range(n):
            p = random.uniform(0, 2 * math.pi)
            re += math.cos(p)
            im += math.sin(p)
        tot += re * re + im * im
    print("   %6d %14.2f %14.4f %14d" % (n, float(n * n), tot / trials, n))
print("""   Reading: NOT in conflict.  b_K(U) = sum_a b_a + 2 sum_{a<b} sqrt(b_a b_b)
   cos(dpi_ab) -- the cross term is exactly Coh.  Phase-aligned it gives n^2;
   phase-random it gives n in expectation, which is DCGT's bandwidth
   additivity.  The two rules are ONE rule in two regimes, and DCGT's is the
   decoherent limit, i.e. Coh -> 0.  DCGT section 3.3 is explicit that its
   regime scrambles exactly the microstructure that would carry the phase
   ("specific channel labels, specific commitment-event timings" averaged out),
   so DCGT is entitled to its rule -- but it cites "P04 (bandwidth additivity)"
   as though the rule were general, and canonical Paper_087 section P12 says
   it is not.  The regime condition is unstated there.""")

# ------------------------------------------------------------------- B ------
print("""
B. Under DCGT's decoherent rule, what does (R) force?  (R) now reads
   f(b1 + b2, bv) = f(b1, bv) + f(b2, bv): f is additive and monotone in its
   first argument, so linear; symmetry makes it linear in both.  The forced
   weight is the PRODUCT, c * bu * bv -- a third candidate.  Check numerically.
""")


def gm(bu, bv):
    return math.sqrt(bu * bv)


def mn(bu, bv):
    return min(bu, bv)


def prod(bu, bv):
    return bu * bv


CAND = [("geometric mean", gm), ("min", mn), ("product (c=1)", prod)]

for rule, label in (("amplitude", "b_K(U) = (sum sqrt(b))^2, aligned"),
                    ("bandwidth", "b_K(U) = sum b")):
    print("   merge rule: %-12s  %s" % (rule, label))
    print("      %-18s %10s %10s %10s" % ("map", "N=2", "N=4", "N=10"))
    for name, f in CAND:
        row = []
        for N in (2, 4, 10):
            bU = float(N * N) if rule == "amplitude" else float(N)
            row.append(f(bU, 1.0) - N * f(1.0, 1.0))
        ok = all(abs(x) < 1e-12 for x in row)
        print("      %-18s %10.3f %10.3f %10.3f  %s"
              % (name, row[0], row[1], row[2], "SATISFIES (R)" if ok else ""))
print("""   Reading: exactly one weight per merge rule, and min satisfies (R) under
   NEITHER.  So min stays excluded in both regimes -- that half of the earlier
   result survives untouched.  What does not survive is the claim that the
   geometric mean is forced full stop: it is forced in the COHERENT regime.
   The product is forced in the decoherent one.

   Note what excluded the product earlier: the normalization f(b,b) = b, which
   the product cannot meet with a constant c (it would need c = 1/b).  That
   normalization was a choice, and it was doing real work -- but the
   individuation RATIO is a quotient of sums of w, so c cancels and the product
   is a legitimate unnormalized candidate.  It has to be excluded on regime
   grounds, not by normalization.""")

# ------------------------------------------------------------------- C ------
print("""
C. Does the regime choice change any individuation verdict?  Re-run the source
   concept's three worked examples under the product as well.
""")


def ratio(nodes, S, edges, f):
    b_int = b_bdry = 0.0
    for (u, v) in edges:
        shared = set(nodes[u]) & set(nodes[v])
        ww = sum(f(nodes[u][K], nodes[v][K]) for K in shared)
        inside = (u in S) + (v in S)
        if inside == 2:
            b_int += ww
        elif inside == 1:
            b_bdry += ww
    return b_int / b_bdry if b_bdry else float("inf")


CASES = []
CASES.append(("qubit shielded", {"q1": {"a": 1.0}, "q2": {"a": 1.0},
                                 "e1": {"z": 1.0}, "e2": {"z": 1.0}},
              {"q1", "q2"}, [("q1", "q2"), ("q1", "e1"), ("q2", "e2"), ("e1", "e2")]))
CASES.append(("qubit leaky", {"q1": {"a": 1.0, "z": 0.9}, "q2": {"a": 1.0},
                              "e1": {"z": 1.0}, "e2": {"z": 1.0}},
              {"q1", "q2"}, [("q1", "q2"), ("q1", "e1"), ("q2", "e2"), ("e1", "e2")]))
CASES.append(("entangled: A alone", {"A": {"s": 1.0}, "B": {"s": 1.0}, "env": {"x": 1.0}},
              {"A"}, [("A", "B"), ("A", "env"), ("B", "env")]))
CASES.append(("entangled: A+B", {"A": {"s": 1.0}, "B": {"s": 1.0}, "env": {"x": 1.0}},
              {"A", "B"}, [("A", "B"), ("A", "env"), ("B", "env")]))
CASES.append(("Cooper pair, metal", {"c1": {"p": 1.0}, "c2": {"p": 1.0},
                                     "m1": {"n": 1.0}, "m2": {"n": 1.0}},
              {"c1", "c2"}, [("c1", "c2"), ("c1", "m1"), ("c2", "m2"), ("m1", "m2")]))
CASES.append(("Cooper pair, superconductor",
              {"c1": {"p": 1.0, "cond": 1.0}, "c2": {"p": 1.0, "cond": 1.0},
               "m1": {"n": 1.0, "cond": 1.0}, "m2": {"n": 1.0, "cond": 1.0}},
              {"c1", "c2"}, [("c1", "c2"), ("c1", "m1"), ("c2", "m2"), ("m1", "m2")]))

print("   %-30s %14s %14s" % ("case", "geometric mean", "product"))
for label, nodes, S, edges in CASES:
    rg = ratio(nodes, S, edges, gm)
    rp = ratio(nodes, S, edges, prod)
    fmt = lambda r: "inf" if r == float("inf") else "%.4f" % r
    print("   %-30s %14s %14s" % (label, fmt(rg), fmt(rp)))
print("""   Reading: the qualitative verdicts agree on every worked example -- all
   the bandwidths there are 0 or 1, where the two weights coincide.  The
   examples do not separate the regimes, so they cannot be used to argue the
   coherent reading.  That has to be argued from what individuation IS.

CONCLUSION

  1. (R) is already a corpus commitment.  Paper_073 section 3.2's
     well-definedness clause is (R), and DCGT is upstream of the whole Wave-3
     corpus.  The individuation result no longer rests on a requirement
     invented for it.

  2. But the corpus carries TWO merge rules, and DCGT uses the other one.
     Under (R), amplitude merging forces the geometric mean and bandwidth
     merging forces the product.  So the edge weight is REGIME-DEPENDENT, and
     "the geometric mean is forced" is true only in the coherent regime.

  3. min is excluded under BOTH rules.  That half stands.

  4. The two rules reconcile: bandwidth additivity is the random-phase limit of
     amplitude additivity (test A), i.e. Coh -> 0.  DCGT's regime is decoherent
     by its own section 3.3, so DCGT is entitled to its rule; but section 3.2
     attributes it to "P04 (bandwidth additivity)" without the regime
     condition, and canonical Paper_087 section P12's Coh says the general rule
     has a cross term.  That is an unstated regime condition in a clause the
     Wave-3 corpus inherits.

  5. Individuation's regime is the coherent one -- but by argument, not by the
     worked examples (test C), which do not discriminate.  The argument: the
     source concept's own decisive example is a Cooper pair de-individuating on
     gaining a CONDENSATE channel, and its account of entanglement is that an
     entangled pair is one un-individuated complex.  Both are coherence
     statements; both are invisible if Coh -> 0.  Individuation in the
     decoherent limit would not have the content the concept claims for it.
""")
