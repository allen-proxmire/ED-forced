# -*- coding: utf-8 -*-
"""Verify the three outward-facing artifacts are current and agree with each other.

WHY THIS EXISTS
---------------
On 2026-09-07 I twice reported documents as current when they were not: once
because a canonical list was stale and fed an error into a new paper (ledger
#151), and once because I read three external reviews, acted on one, and then
described "the external review" as addressed (#153). Both times the thing that
caught it was AP asking, not a check.

Neither failure is exotic. Both are the same shape: a claim about a document's
state, made from memory of what I did rather than from the document. This script
reads the documents.

THE THREE ARTIFACTS
    ED_UnifiedFramework_Report.md          the synthesis
    ED_ItemizedTheory_TieredClaims_v2.xlsx the ledger of record
    physics-papers/gravity/Paper_a0z_...md the standalone prediction paper

FOUR CLASSES OF CHECK
    A  STALE     text that a fix was supposed to remove and did not
    B  APPLIED   text a fix was supposed to add, verified present
    C  AGREE     shared numbers that must match across artifacts
    D  FRESH     PDFs newer than sources; workbook counts match its own rows

Run with --selftest to confirm the checks can actually fail: it plants a stale
string in memory and asserts the checker flags it.

Exit 0 clean, 1 on any finding.
"""
from __future__ import print_function
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

REPORT = "ED_UnifiedFramework_Report.md"
PAPER = "physics-papers/gravity/Paper_a0z_MONDScaleTracksHubbleRate.md"
WORKBOOK = "ED_ItemizedTheory_TieredClaims_v2.xlsx"
REVIEW = "physics-papers/gravity/Note_a0z_Paper_AdversarialReview_2026-09-06.md"

# --------------------------------------------------------------------------- A
# Each entry: (file, regex, what it means, which ledger item should have killed it)
STALE = [
    (REPORT, r"It is a closed sector, but",
     "'a closed sector' contradicts the edge-list beneath it", "GPT item 3 / #153"),
    (REPORT, r"One residual is open and named: the constructive sign",
     "the constructive sign is structurally settled, not open", "GPT item 1 / #153"),
    (REPORT, r"softening to ~1–2σ once one-survey systematics are folded in",
     "the '~1-2 sigma' was asserted; the computed figure is 2.3", "#152"),
    (REPORT, r"a direct fit gives",
     "alpha = 1.18 is an ED-side recast, not the survey's fit", "#151"),
    (PAPER, r"\*\*I — measurement\*\* \| same source",
     "audit row 8 mislabelled our conversion as the survey's measurement", "#151"),
    (PAPER, r"tension softens to ~1–2σ under a realistic error budget",
     "step 9's special pleading, replaced by the computed budget", "#152"),
    (PAPER, r"untouched here — this paper does not test it",
     "LCDM is not untouched; Magneticum predicts apparent evolution", "#151"),
    ("physics-papers/predictions/ED_Master_Predictions_List.md",
     r"the implied power is \*\*\$\\alpha = 1\.18",
     "canonical row must attribute alpha to ED, not the survey", "#151"),
    ("physics-papers/predictions/ED_Master_Predictions_List.md",
     r"α=1 is \*dimensionally forced\*",
     "alpha=1 is mechanism-forced; ED carries l_P", "#151"),
    ("physics-papers/predictions/22_Ways_to_Kill_Event_Density.md", r"a direct fit gives",
     "alpha provenance", "#151"),
    ("physics-papers/predictions/Paper_101_FalsificationRegister.md", r"a direct fit gives",
     "alpha provenance", "#151"),
    ("essays/Paper_SelectedFormalisms_I_Gravity.md", r"A direct fit gives",
     "alpha provenance", "#151"),
]

# --------------------------------------------------------------------------- B
APPLIED = [
    (REPORT, "Magneticum", "the LCDM rival is named", "#151"),
    (REPORT, "closed in the GR regime that has been tested", "closed-sector fix", "GPT 3"),
    (REPORT, "The MOND residuals, stated as the three they actually are", "residual list", "GPT 5"),
    (REPORT, "conditional on the still-unproven universal-free-fall normalisation",
     "abstract conditioned on UFF", "GPT 4"),
    (REPORT, "2.3σ on a computed conversion budget", "computed tension", "#152"),
    (PAPER, "Magneticum", "LCDM rival in the four-way table", "#151"),
    (PAPER, "a0z_powerlaw_refit.py", "the refit is cited and reproducible", "#152"),
    (PAPER, "5.3a", "the unverified rebuttal is recorded as a check", "#151"),
    (PAPER, "5.3b", "the shape comparison exists", "#152"),
    (PAPER, "converted by us from their linear fit", "alpha provenance stated", "#151"),
    (REVIEW, "Round 2", "the external review round is recorded", "#151"),
]

# --------------------------------------------------------------------------- C
# A shared number must appear in every artifact that discusses it, identically.
AGREE = [
    ("the computed tension", r"2\.3σ", [REPORT, PAPER,
                                            "physics-papers/predictions/ED_Master_Predictions_List.md",
                                            "physics-papers/predictions/Paper_101_FalsificationRegister.md",
                                            "physics-papers/predictions/22_Ways_to_Kill_Event_Density.md",
                                            "essays/Paper_SelectedFormalisms_I_Gravity.md"]),
    ("the refit central value", r"1\.15", [REPORT, PAPER,
                                           "physics-papers/predictions/ED_Master_Predictions_List.md"]),
    ("the survey's linear slope", r"1\.59", [PAPER,
                                             "physics-papers/predictions/ED_Master_Predictions_List.md"]),
]


def read(p):
    try:
        return io.open(p, encoding="utf-8").read()
    except IOError:
        return None


def rule(c="-", n=76):
    print(c * n)


def check(texts):
    """Returns list of (class, file, message)."""
    out = []

    for path, pat, why, owner in STALE:
        t = texts.get(path)
        if t is None:
            out.append(("A", path, "FILE MISSING"))
            continue
        if re.search(pat, t):
            out.append(("A", path, "STALE: %s  [%s]" % (why, owner)))

    for path, needle, why, owner in APPLIED:
        t = texts.get(path)
        if t is None:
            out.append(("B", path, "FILE MISSING"))
            continue
        if needle not in t:
            out.append(("B", path, "NOT APPLIED: %s (%r) [%s]" % (why, needle, owner)))

    for label, pat, files in AGREE:
        missing = [f for f in files if texts.get(f) and not re.search(pat, texts[f])]
        if missing:
            out.append(("C", ", ".join(os.path.basename(m) for m in missing),
                        "DISAGREES on %s (pattern %s absent)" % (label, pat)))
    return out


def freshness():
    out = []
    for md in (REPORT, PAPER):
        pdf = md[:-3] + ".pdf"
        if not os.path.exists(pdf):
            out.append(("D", pdf, "PDF MISSING"))
        elif os.path.getmtime(pdf) < os.path.getmtime(md):
            out.append(("D", pdf, "PDF IS OLDER THAN ITS SOURCE - rebuild"))

    # Desktop copy: compare CONTENT, not mtime. `git checkout` rewrites the working
    # tree and bumps mtimes without changing bytes, which made an identical copy
    # look stale on the first run of this script.
    desk = os.path.join(os.path.expanduser("~"), "Desktop", "ED_UnifiedFramework_Report.pdf")
    rp = REPORT[:-3] + ".pdf"
    if os.path.exists(desk) and os.path.exists(rp):
        import hashlib

        def h(p):
            with open(p, "rb") as fh:
                return hashlib.sha256(fh.read()).hexdigest()

        if h(desk) != h(rp):
            out.append(("D", "Desktop copy", "desktop PDF differs from the built one - re-copy"))

    try:
        import openpyxl
    except ImportError:
        out.append(("D", WORKBOOK, "openpyxl unavailable - workbook not checked"))
        return out
    if not os.path.exists(WORKBOOK):
        out.append(("D", WORKBOOK, "MISSING"))
        return out
    wb = openpyxl.load_workbook(WORKBOOK, read_only=True)
    ws = wb["Ledger w Claims"]
    import collections
    live = collections.Counter()
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[3]:
            live[str(r[3]).strip()] += 1
    tc = wb["Tier Counts"]
    for row in tc.iter_rows(values_only=True):
        if not row or not row[0]:
            continue
        name, stored = str(row[0]), row[1]
        key = name.split("(")[0].strip()
        if key in live and isinstance(stored, int) and live[key] != stored:
            out.append(("D", "Tier Counts",
                        "%s: sheet says %d, rows say %d" % (key, stored, live[key])))
    return out


def main():
    selftest = "--selftest" in sys.argv
    paths = set(p for p, _, _, _ in STALE) | set(p for p, _, _, _ in APPLIED)
    for _, _, fs in AGREE:
        paths |= set(fs)
    texts = {p: read(p) for p in paths}

    print()
    rule("=")
    print("ARTIFACT CURRENCY CHECK - do the three documents say what I think they say?")
    rule("=")
    print("  checks: %d stale-patterns, %d applied-fixes, %d cross-doc agreements"
          % (len(STALE), len(APPLIED), len(AGREE)))
    print()

    findings = check(texts) + freshness()

    if selftest:
        rule()
        print("SELF-TEST - plant a known-stale string and confirm it is caught")
        rule()
        planted = dict(texts)
        planted[REPORT] = (planted[REPORT] or "") + "\nIt is a closed sector, but it still has edges:\n"
        got = [f for f in check(planted) if f[0] == "A" and "closed sector" in f[2]]
        if got:
            print("  PASS - the checker detects a planted stale string.")
        else:
            print("  FAIL - the checker did NOT detect a planted stale string.")
            findings.append(("SELFTEST", "-", "checker is not sensitive"))
        # and confirm a removed fix is caught
        planted2 = dict(texts)
        planted2[PAPER] = (planted2[PAPER] or "").replace("Magneticum", "XXX")
        got2 = [f for f in check(planted2) if f[0] == "B"]
        print("  %s - the checker detects a removed fix." % ("PASS" if got2 else "FAIL"))
        if not got2:
            findings.append(("SELFTEST", "-", "applied-check is not sensitive"))
        print()

    rule()
    if not findings:
        print("RESULT: CLEAN")
        rule()
        print("  No stale text, every recorded fix present, shared numbers agree,")
        print("  PDFs newer than their sources, workbook counts match its own rows.")
        print()
        print("  This does NOT verify the claims are true. It verifies the documents")
        print("  say what the ledger says they say. Those are different jobs and only")
        print("  the second one can be automated.")
        print()
        return 0

    print("RESULT: %d FINDING(S)" % len(findings))
    rule()
    for cls, where, msg in findings:
        print("  [%s] %-46s %s" % (cls, os.path.basename(str(where))[:46], msg))
    print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
