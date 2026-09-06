# -*- coding: utf-8 -*-
"""Does the proposed w(e) map reproduce individuation's own worked examples?

The gap (Paper_Individuation_TheSystemEnvironmentCut section 2.1): individuation
is written with edge weights w(e), inherited from the OLD primitive scheme where
"Primitive 04 supplies edge weights -- a positive real number on each edge"
(primitives/concepts/participation_bandwidth.md). Canonical P04 instead puts
bandwidth on (channel, locus): b_K(u,t).

Proposed map -- an edge carries what its two endpoints SHARE:

    w(u,v) = sum over channels K participated at BOTH u and v of
             sqrt( b_K(u) * b_K(v) )

This script does not prove the map. It checks that it reproduces the three
worked examples the source concept states, which a wrong map would not.

Run: python "internal notes/_check_edge_weight_map.py"
"""
import math
from itertools import combinations

def w(bu, bv):
    """Edge weight: geometric mean over SHARED channels only."""
    shared = set(bu) & set(bv)
    return sum(math.sqrt(bu[K] * bv[K]) for K in shared)

def ratio(nodes, S, edges):
    """b_int(S)/b_bdry(S) over the given graph."""
    b_int = b_bdry = 0.0
    for (u, v) in edges:
        ww = w(nodes[u], nodes[v])
        inside = (u in S) + (v in S)
        if inside == 2:
            b_int += ww
        elif inside == 1:
            b_bdry += ww
    return b_int, b_bdry, (b_int / b_bdry if b_bdry else float("inf"))

def show(label, nodes, S, edges, expect):
    bi, bb, r = ratio(nodes, S, edges)
    print("  %-46s b_int=%6.2f  b_bdry=%6.2f  ratio=%8s   expect %s"
          % (label, bi, bb, ("inf" if r == float("inf") else "%.2f" % r), expect))
    return r

print("Edge-weight map check\n" + "=" * 84)
print("w(u,v) = sum_{K shared} sqrt(b_K(u) b_K(v))\n")

# --- 1. Isolated qubit: few shared channels with the environment ----------
print("1. Isolated qubit vs environment  (source: 'a qubit in a dilution refrigerator')")
nodes = {"q1": {"a": 1.0}, "q2": {"a": 1.0},                 # the qubit's own two loci
         "e1": {"z": 1.0}, "e2": {"z": 1.0}}                 # environment loci
edges = [("q1", "q2"), ("q1", "e1"), ("q2", "e2"), ("e1", "e2")]
show("well-shielded (no shared channel with env)", nodes, {"q1", "q2"}, edges, "individuated (inf)")
nodes_leaky = {"q1": {"a": 1.0, "z": 0.9}, "q2": {"a": 1.0},
               "e1": {"z": 1.0}, "e2": {"z": 1.0}}
show("leaky (qubit shares env channel z)", nodes_leaky, {"q1", "q2"}, edges, "lower ratio")

# --- 2. Entanglement = pre-individuation ---------------------------------
print("\n2. Entangled pair  (source: 'a single un-individuated complex at two endpoints')")
nodes = {"A": {"s": 1.0}, "B": {"s": 1.0}, "env": {"x": 1.0}}
edges = [("A", "B"), ("A", "env"), ("B", "env")]
rA   = show("A alone, sharing channel s with B", nodes, {"A"}, edges, "NOT individuated")
rAB  = show("A+B together", nodes, {"A", "B"}, edges, "individuated vs env")
print("     -> pair individuated jointly (%s) while A alone is not (%.2f): matches the concept."
      % (("inf" if rAB == float("inf") else "%.2f" % rAB), rA))

# --- 3. Cooper pair in a normal metal vs in a superconductor -------------
print("\n3. Cooper pair  (source: 'individuated inside a normal metal; inside a")
print("   superconductor the whole condensate is one un-individuated chain')")
metal = {"c1": {"p": 1.0}, "c2": {"p": 1.0},
         "m1": {"n": 1.0}, "m2": {"n": 1.0}}
edges3 = [("c1", "c2"), ("c1", "m1"), ("c2", "m2"), ("m1", "m2")]
r_metal = show("pair in normal metal (no shared channel w/ metal)", metal, {"c1", "c2"}, edges3,
               "individuated")
sc = {"c1": {"p": 1.0, "cond": 1.0}, "c2": {"p": 1.0, "cond": 1.0},
      "m1": {"n": 1.0, "cond": 1.0}, "m2": {"n": 1.0, "cond": 1.0}}
r_sc = show("same pair in a superconductor (condensate channel)", sc, {"c1", "c2"}, edges3,
            "NOT individuated")
print("     -> ratio falls from %s to %.2f on adding the shared condensate channel."
      % (("inf" if r_metal == float("inf") else "%.2f" % r_metal), r_sc))

print("""
Reading:

  The map reproduces all three worked examples of
  primitives/concepts/individuation.md without adjustment:

    - shielding raises the ratio, leakage lowers it;
    - an entangled member is not individuated alone but the pair is jointly;
    - the SAME pair individuates in a metal and de-individuates in a
      superconductor, purely from gaining a shared channel -- which is the
      concept's own example of individuation being RELATIONAL, not intrinsic.

  That is a consistency check, not a derivation. A map that got the shared-
  channel condition wrong (e.g. summing all channels at both endpoints rather
  than only shared ones) would make the superconductor case indistinguishable
  from the metal case, so the check does discriminate.
""")
