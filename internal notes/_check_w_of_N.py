# -*- coding: utf-8 -*-
"""Can w(N) be computed?  Attempt, with the negatives banked.

Task (AP, 2026-09-06): the commitment-DOF ordering (#98) is an ordering, which
is the weakest thing that line can produce.  Compute w(N) instead -- a VALUE --
and check it against sqrt(2) at N = 2.

Method note, stated first because it constrains everything below: the corpus
explicitly forbids bolting Koide on by matching a stray fraction (the retrofit
trap, Paper_ChargeAsTopology_B4).  So this script does NOT search distributions
until one lands on sqrt(2).  It fixes the candidates FIRST from ED's own
machinery, computes what each gives, and reports the result whatever it is.

Run: python "internal notes/_check_w_of_N.py"
"""
import math

SQRT2 = math.sqrt(2.0)

# ---------------------------------------------------------------- part 1 ----
print("Computing w(N)")
print("=" * 78)
print("""
PART 1 -- what w actually IS, before any mechanism

Brannen form (corpus): sqrt(m_k) = M (1 + w cos(delta + 2 pi k / 3)), k=0,1,2.

Over the three 120-degree-separated points, sum(cos) = 0 and sum(cos^2) = 3/2
for ANY delta.  So for the three generation AMPLITUDES A_k = sqrt(m_k):

    mean(A)  = M
    var(A)   = M^2 w^2 / 2
    => w = sqrt(2) * sigma_A / mu_A

So w is sqrt(2) times the COEFFICIENT OF VARIATION of the generation
amplitudes, and Koide's Q = 2/3 (w = sqrt(2)) says exactly:

    *** the standard deviation of the three generation amplitudes
        EQUALS their mean.  CV = 1. ***

That is a restatement, not a mechanism -- but it is the variable any mechanism
has to deliver, and it is sharper than "why sqrt(2)".
""")

FAM = [
    ("neutrinos",        0.586, 1, "bound"),
    ("charged leptons",  2.0 / 3.0, 2, "exact"),
    ("down quarks",      0.731, 3, "fit"),
    ("up quarks",        0.849, 3, "fit"),
]
print("  %-18s %7s %8s %8s %8s" % ("family", "N", "Q", "w", "CV = w/sqrt2"))
for name, Q, N, kind in FAM:
    w = math.sqrt(6 * Q - 2)
    print("  %-18s %7d %8.4f %8.4f %8.4f%s"
          % (name, N, Q, w, w / SQRT2, "   <== CV = 1 exactly" if kind == "exact" else ""))

# ---------------------------------------------------------------- part 2 ----
print("""
PART 2 -- the candidates, fixed from ED's machinery before computing

  (a) SIMPLEX SHARING.  P04 gives non-negative bandwidth; P-Locus-Bandwidth-
      Bound (named 2026-09-05) gives a finite per-locus total.  N channels
      sharing a fixed budget with no further information = uniform on the
      simplex = Dirichlet(1,...,1).  One channel's share is Beta(1, N-1).

  (b) RANDOM-PHASE SUPERPOSITION.  P11 randomizes the un-selected channels'
      phase.  Pushed to its limit: an amplitude is the modulus of a sum of N
      equal contributions with iid uniform phases -- a 2-D random walk, whose
      amplitude is Rayleigh.

  (c) MAXIMUM ENTROPY.  Non-negativity (P04) plus a fixed mean and nothing
      else = exponential.
""")


def cv_simplex_intensity(N):
    """Beta(1, N-1): CV of the SHARE itself."""
    if N < 2:
        return float("nan")
    mean = 1.0 / N
    var = (N - 1.0) / (N * N * (N + 1.0))
    return math.sqrt(var) / mean


def cv_simplex_amplitude(N):
    """CV of sqrt(share) for share ~ Beta(1, N-1)."""
    if N < 2:
        return float("nan")
    # E[X^(1/2)] = Gamma(3/2)Gamma(N) / Gamma(N + 1/2)
    e_sqrt = math.exp(math.lgamma(1.5) + math.lgamma(N) - math.lgamma(N + 0.5))
    e_x = 1.0 / N
    var = e_x - e_sqrt ** 2
    return math.sqrt(var) / e_sqrt


print("  %-34s %9s %9s %9s %9s" % ("candidate", "N=2", "N=3", "N=4", "N->inf"))
rows = [
    ("(a) simplex, CV of the share", [cv_simplex_intensity(n) for n in (2, 3, 4, 400)]),
    ("(a') simplex, CV of sqrt(share)", [cv_simplex_amplitude(n) for n in (2, 3, 4, 400)]),
    ("(b) Rayleigh amplitude", [math.sqrt(4.0 / math.pi - 1.0)] * 4),
    ("(c) exponential (max-ent)", [1.0] * 4),
]
for label, vals in rows:
    print("  %-34s %9.4f %9.4f %9.4f %9.4f" % (label, *vals))
print("\n  target: CV = 1.0000 at N = 2, and RISING with N (leptons 1.000,")
print("          down quarks 1.092, up quarks 1.244).\n")

print("""  Reading -- all three fail, and they fail in COMPLEMENTARY ways:

    (a)/(a') give real N-dependence in the right DIRECTION but never reach
             CV = 1: the share CV approaches 1 only as N -> infinity, and at
             N = 2 gives 0.577 (share) or 0.354 (amplitude), far below.
    (b)      is N-independent at 0.523.  Wrong value, no dependence.
    (c)      gives CV = 1 EXACTLY -- the lepton value -- but is likewise
             N-independent, so it predicts w = sqrt(2) for every family and
             is falsified by the quarks.

  So one candidate supplies the lepton value and precludes the variation;
  another supplies the variation and precludes the value.  No mechanism here
  computes w(N).  *** THE TASK DID NOT SUCCEED. ***
""")

# ---------------------------------------------------------------- part 3 ----
print("""PART 3 -- the one structural thing that did fall out

There is a standard result: a log-concave density on [0, infinity) has
coefficient of variation CV <= 1, with EQUALITY IFF EXPONENTIAL.  (Inherited
mathematics, not derived here.)  Applying it to the measured values:
""")
print("  %-18s %8s %10s   %s" % ("family", "CV", "vs 1", "generation-amplitude distribution"))
for name, Q, N, kind in FAM:
    cv = math.sqrt(6 * Q - 2) / SQRT2
    if kind == "bound":
        verdict = "<= 0.871  ->  log-concave is ALLOWED"
        rel = "below"
    elif abs(cv - 1) < 1e-3:
        verdict = "== 1.000  ->  EXACTLY the log-concave BOUNDARY (exponential)"
        rel = "on"
    else:
        verdict = " > 1      ->  CANNOT be log-concave"
        rel = "above"
    print("  %-18s %8.4f %10s   %s" % (name, cv, rel, verdict))

print("""
  So, without fitting anything -- the CVs are arithmetic from the measured Q,
  and the threshold is a standard theorem:

    *** Koide's 2/3 places the charged leptons EXACTLY ON the log-concavity
        boundary of the generation-amplitude distribution.  Neutrinos sit
        below it, quarks above it, and the crossing is ordered by N. ***

  WHAT THIS IS.  A relocation of the question, from "why sqrt(2)" to "why does
  the generation-amplitude distribution sit exactly at the log-concave
  boundary at N = 2".  The second is a CLASSIFICATION question (log-concave or
  not), which is the half arc-M says ED does cleanly, whereas "why sqrt(2)" is
  a value question, which is the half it says ED does not.

  WHAT THIS IS NOT.  Not a derivation, not a mechanism, and not evidence: a
  threshold crossing at one of four points is a coincidence until something
  explains it.  It is a better-posed place to put the question, and nothing
  more.  Held to the same bar as a positive, this is a NEGATIVE RESULT with a
  reframe attached.
""")
