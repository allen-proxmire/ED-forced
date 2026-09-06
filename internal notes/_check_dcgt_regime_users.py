# -*- coding: utf-8 -*-
"""Who applies DCGT's coarse-graining where phase coherence SURVIVES the cell?

Paper_073 section 3.2's well-definedness clause merges bandwidth additively
within a coarse-graining cell.  That is the random-phase limit of the general
rule (Coh -> 0), not a general consequence of P04 -- flagged there 2026-09-05.
Harmless inside DCGT's own hydrodynamic window.  The question this script asks
is whether anything DOWNSTREAM inherits the clause in a regime where coherence
survives across the cell, which would be a live error rather than a
documentation defect.

Method: for every paper citing DCGT, find lines that do coarse-graining/
averaging work AND lines that carry coherence content (phase, interference,
entanglement, superposition, holonomy, Coh), and report papers where the two
appear within PROXIMITY lines of each other.  Proximity co-occurrence is a
SCREEN, not a verdict -- it produces candidates to read, and the reading is
what decides.

Run: python "internal notes/_check_dcgt_regime_users.py"
"""
import io
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "physics-papers")
PROXIMITY = 6

CG = re.compile(r"coarse-grain|coarse grain|coarse-graining|DCGT|averag|\bcell\b|R_\{?\\?mathrm\{cg\}?", re.I)
COH = re.compile(r"phase|coheren|interfer|entangl|superposition|holonom|\bCoh\b|off-diagonal|winding", re.I)
DECOH = re.compile(r"decoher|random.?phase|incoheren|thermal|classical limit|Lindblad|dephas", re.I)
CITES = re.compile(r"DCGT|Paper_073", re.I)

hits = []
for dirpath, _dirs, files in os.walk(ROOT):
    for fn in files:
        if not fn.endswith(".md"):
            continue
        if "Ledger" in fn or fn.startswith("README") or "Note_EdgeWeight" in fn or "Paper_073_DCGT" in fn:
            continue
        path = os.path.join(dirpath, fn)
        try:
            lines = io.open(path, encoding="utf-8").read().splitlines()
        except Exception:
            continue
        text = "\n".join(lines)
        if not CITES.search(text):
            continue
        cg_lines = [i for i, L in enumerate(lines) if CG.search(L)]
        coh_lines = [i for i, L in enumerate(lines) if COH.search(L)]
        if not cg_lines or not coh_lines:
            continue
        pairs = []
        for i in cg_lines:
            for j in coh_lines:
                if abs(i - j) <= PROXIMITY:
                    pairs.append((i, j))
                    break
        if not pairs:
            continue
        # does the paper anywhere say it is in the decoherent regime?
        decoh_n = len(DECOH.findall(text))
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        hits.append((len(pairs), decoh_n, rel, pairs[:3]))

hits.sort(key=lambda h: (-h[0], h[2]))

print("DCGT regime-inheritance screen")
print("=" * 78)
print("Papers citing DCGT with coarse-graining and coherence language within %d lines.\n" % PROXIMITY)
print("  %-58s %6s %8s" % ("paper", "co-occ", "decoh-kw"))
for n, d, rel, _p in hits[:28]:
    flag = "  <-- no decoherence language anywhere" if d == 0 else ""
    print("  %-58s %6d %8d%s" % (rel, n, d, flag))

print("\n  total DCGT-citing papers screened with any co-occurrence: %d" % len(hits))
print("""
Reading: a high co-occurrence count is a candidate, not a finding.  The two
columns matter together -- a paper with many co-occurrences and NO decoherence
vocabulary anywhere is the profile of one coarse-graining coherent content
without ever saying it is in the decoherent regime.  Those are the ones to
open.
""")

# ---------------------------------------------------------------------------
# ADJUDICATION -- the screen above produced candidates; these are the readings.
# ---------------------------------------------------------------------------
import math

print("=" * 78)
print("ADJUDICATION -- who extends P04 additivity beyond its stated scope, and")
print("what licenses each one\n")
print("P04 as canonically stated (Paper_087): bandwidth is non-negative and")
print("ADDITIVE OVER DISJOINT SUB-CHANNELS at a locus.  Summing over LOCI in a")
print("region is a different operation.  The general combination rule is")
print("b(U) = sum_a b_a + 2 sum_{a<b} sqrt(b_a b_b) cos dpi_ab (Paper_087 P12).\n")

SITES = [
    ("qm-kinematics/Paper_004_6_Tsirelson_Continuum", "sum_K -> integral, P_K -> Psi(x)",
     "NOT AT RISK", "coarse-grains AMPLITUDES, not bandwidths; sesquilinear in Psi"),
    ("qm-kinematics/Paper_009_BerryPhase", "substrate connection -> U(1) one-form",
     "NOT AT RISK", "coarse-grains a connection (a phase object), not bandwidth"),
    ("entanglement/Paper_066_NoSignaling", "L3: DCGT preserves local algebras",
     "NOT AT RISK", "coarse-grains operator support/locality, not bandwidth"),
    ("entanglement/Paper_065_Monogamy", "W_A = sum_i over PARTNER CHAINS",
     "LICENSED", "partners are disjoint channel sets -- this IS P04 as stated"),
    ("entanglement/Paper_067/068_VonNeumannEntropy", "S(rho_A x rho_B) = S_A + S_B",
     "LICENSED", "explicitly conditioned on INDEPENDENT subsystems; named P-Additivity"),
    ("black-hole/Paper_042_NoSingularity", "C_cum over a spatial REGION",
     "LICENSED", "C_cum is COMMITTED content (P11); commitment is channel-basis only"),
    ("substrate-evaluation/Paper_V5UnifiedBudget", "W_max = integral F_V5 dmu",
     "LICENSED", "integral of a bounded finite-width kernel; additivity is decorative"),
    ("soft-matter/Paper_073_DCGT sec 3.2", "bandwidth sums over LOCI IN A CELL",
     "LICENSED", "hydrodynamic window is decoherent by its own sec 3.3"),
]
print("  %-46s %-12s" % ("site / what it sums", "verdict"))
for path, what, verdict, why in SITES:
    print("  %-46s %-12s" % (path, verdict))
    print("      sums: %s" % what)
    print("      why : %s" % why)

print("""
THE COMMON LICENSE, WHICH NONE OF THEM STATE

  Every site is fine, and all for the same reason: the summed contributions
  carry NO RELATIVE PHASE.  That happens three ways in ED --

    (a) DISJOINT CHANNELS      -- P04's additivity exactly as written (065);
    (b) COMMITTED CONTENT      -- P11 commits in the channel basis only.
        "ED commits only in the channel basis: the channel basis is the unique
         pointer basis, selected by the arrow.  Phase remains a genuine
         coherence observable ... but it is never a commitment basis."
        (Paper_QuantumLogicKeystone_GleasonReconstruction sec 7.)
        Committed content has no phase left to interfere, so bandwidth IS
        additive over a region for it (042);
    (c) A DECOHERENT REGIME    -- Coh -> 0 (073 sec 3.2, 067/068).

  So the extension from "disjoint sub-channels at a locus" to "over a region"
  is licensed by COMMITMENT, INDEPENDENCE or DECOHERENCE -- and by nothing
  else.  That is a statable rule, and it is currently stated nowhere.

WHICH DIRECTION THE ERROR WOULD RUN, IF THE LICENSE FAILED""")
for n in (2, 4, 10):
    print("  %2d phase-aligned unit contributions: additive total %3d, actual %4d  (x%d)"
          % (n, n, n * n, n))
print("""
  Coherent content carries MORE total bandwidth than the additive sum, not
  less.  So a bound derived from bandwidth-additivity is NOT conservative --
  it would be VIOLATED, by a factor up to the number of contributions.  That
  is why the license matters for Paper_042's no-singularity bound in
  particular, and why it is worth stating rather than leaving implicit.
  (Paper_042 is doubly safe: its bound is a named postulate,
  P-Bandwidth-Boundedness, not a consequence of additivity alone.)

VERDICT: no live error found.  The defect is documentation, corpus-wide
rather than local to Paper_073 -- an unstated licensing condition on a step
taken in at least eight papers.
""")
