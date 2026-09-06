# -*- coding: utf-8 -*-
"""How much of the "four-band" footprint is actually the DISPUTED partition?

The four-band conflict (gravity ledger #82-#85) is about ONE partition:

  primitives/P04_bandwidth.md sec 1.5 --
      Internal / Adjacency / Environmental / Commitment-reserve
      (a partition of b_K by PARTICIPATION-PARTNER TYPE)

A raw grep for "four-band" across the corpus returns ~28 files and suggests a
wide blast radius for AP's pending branch decision.  This script records what
reading those files actually found: **the term is overloaded**, and at least
four distinct things are called "four-band".

Run: python "internal notes/_check_fourband_senses.py"
"""

SENSES = {
    1: ("THE DISPUTED PARTITION -- Internal / Adjacency / Environmental / "
        "Commitment-reserve; partitions b_K by participation-partner type "
        "(primitives/P04_bandwidth.md sec 1.5)"),
    2: ("CONJUGATE-PAIR BANDS -- position (P03 adjacency) / momentum (P04 "
        "propagation) / time (P13) / energy (P-RB-1).  A SEPARATE, NAMED, "
        "CENSUSED postulate: P-FourBand, Paper_012_6 sec 2.3, substrate "
        "derivation declared OPEN"),
    3: ("CHSH SETTINGS -- the four Bell-test settings {a, a', b, b'} generating "
        "four CORRELATION bands.  Not a bandwidth partition at all"),
    4: ("ADJACENCY-BANDWIDTH -- bandwidth along graph adjacency (P03 locus "
        "indexing + P04): which edges a motif traverses.  Not a band"),
}

# (file, mentions, sense, verdict, evidence)
FILES = [
    ("qm-kinematics/Paper_012_6_Heisenberg", 12, 2, "NOT a dependent",
     "sec 2.3 declares its own P-FourBand: 'position-band (P03 adjacency), "
     "momentum-band (P04 propagation), time-band (P13), energy-band (P-RB-1)'"),
    ("qm-kinematics/Paper_004_5_Tsirelson_Discrete", 6, 3, "NOT a dependent",
     "sec 3.6, verbatim: 'The four-band partition (Bell-test settings a, a', b, b')'"),
    ("qm-kinematics/Paper_003_BornRule", 1, 1, "NOT a dependent",
     "checked as ledger #91: insensitive -- any partition leaves sum_K' b_K' unchanged"),
    ("qm-kinematics/Paper_003_5_ParticipationMeasure", 0, 4, "NOT a dependent",
     "secs 3.3-3.4 'adjacency-bandwidth' = bandwidth along graph adjacency"),
    ("foundations/Paper_089_V1Kernel", 2, 1, "NOT a dependent",
     "line 460, corrected 2026-07-29: the four-band citation was archived "
     "M-series, 'not load-bearing'"),
    ("soft-matter/Paper_UnifiedP04TransportBudget", 6, 1, "GENUINE DEPENDENT",
     "audit row: 'P04 four-band partition; Adjacency = P05-transport content | "
     "P (primitive) | primitives/P04 sec 1.5' -- and the paper already calls it "
     "'the load-bearing joint ... the single most important thing to attack'"),
    ("gravity/Paper_GR-I_WeakFieldEinsteinMetric", 3, 1, "nominal",
     "cites 'P04 (four-band bandwidth)' in a primitives list; the derivation "
     "uses reciprocal edge bandwidth b_uv, not the partition"),
    ("primitives/P04_bandwidth", 3, 1, "THE CARD ITSELF", "sec 1.5 is the source"),
    ("primitives/concepts/participation_bandwidth", 12, 1, "THE SOURCE CONCEPT",
     "but tiers it far weaker than the card: 'The four-band structure is "
     "motivated EMPIRICALLY.  Whether it is mathematically forced ... ' -- open"),
]

print("Four-band: how many mentions are the disputed partition?")
print("=" * 78)
print("\nThe senses found:\n")
for k in sorted(SENSES):
    print("  Sense %d -- %s" % (k, SENSES[k]))
    print()

print("  %-46s %5s %6s  %s" % ("file", "ment.", "sense", "verdict"))
for path, n, sense, verdict, _ev in FILES:
    print("  %-46s %5d %6d  %s" % (path, n, sense, verdict))

tot = sum(n for _p, n, _s, _v, _e in FILES)
disputed = sum(n for _p, n, s, v, _e in FILES
               if s == 1 and v in ("GENUINE DEPENDENT", "nominal"))
print("\n  mentions in the files read : %d" % tot)
print("  of those, sense-1 dependents in PAPERS (not cards) : %d" % disputed)

print("""
EVIDENCE, per file
""")
for path, n, sense, verdict, ev in FILES:
    print("  %s  [sense %d, %s]" % (path, sense, verdict))
    print("      %s" % ev)

print("""
FINDINGS

  1. The two heaviest "four-band" papers -- Paper_012_6 (12 mentions) and
     Paper_004_5 (6) -- are NOT about the disputed partition.  Paper_012_6
     declares its OWN four-band partition as a named postulate with its
     substrate derivation open; Paper_004_5's "four bands" are Bell-test
     settings.  Together that is 18 of the mentions that looked like blast
     radius and are not.

  2. In the papers, exactly ONE genuine sense-1 dependent survives:
     Paper_UnifiedP04TransportBudget -- and it already declares the dependency
     as a posit and names it the single most attackable joint in the arc.
     Paper_GR-I's is a nominal citation in a primitives list.

  3. The source concept tiers the partition WEAKER than the primitive card
     does.  primitives/concepts/participation_bandwidth: "The four-band
     structure is motivated empirically.  Whether it is mathematically forced
     by the participation-graph structure ... " -- open question.
     primitives/P04_bandwidth presents it as canonical primitive-level
     content.  Those are not the same claim.

  4. A FALSE downstream-dependency claim on the card.  primitives/
     P04_bandwidth: "The four-band partition (P04 sec 1.5) supplies the
     sesquilinear inner-product structure on the participation manifold
     (Paper 003)."  Ledger #91 showed Paper_003 needs CHANNEL ORTHOGONALITY,
     not the partition, and is insensitive to how the channel set is
     partitioned.  The card claims a dependent it does not have.

WHAT THIS DOES TO THE BRANCH DECISION

  It does not decide it -- whether the partition is canonical is still a
  primitive-definition question.  But it prices it.  The disputed partition
  has ONE genuine paper-level dependent, which already flags itself as a
  declared posit.  Branch 3 (bands as channel classes, disjointness licensed
  by individuation) is therefore much cheaper than the raw footprint implied.
""")
