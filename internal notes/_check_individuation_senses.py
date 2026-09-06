# -*- coding: utf-8 -*-
"""Measure how "individuation" is used across the corpus, by sense.

`primitives/INDIVIDUATION_DISAMBIGUATION.md` records that the word names two
different things:

  SENSE 1  commitment -- a chain's multi-channel participation collapsing to
           single-channel.  An event/rate, indexed by CHANNELS.  This is P11
           (`Paper_087` P11), and `q-compute/Paper_054` 3.4's
           `Gamma_individuation` is its rate, in the same words.

  SENSE 2  the system/environment cut -- when a set of LOCI counts as a distinct
           identity.  A dimensionless ratio b_int/b_bdry against theta_ind.

They are ANTI-CORRELATED in the regime that matters: raising a system's boundary
bandwidth drives commitment (sense 1 up) while lowering b_int/b_bdry (sense 2
down).  So an unglossed "individuation" in a decoherence or measurement context
is genuinely ambiguous, not merely imprecise.

This classifies each occurrence by the vocabulary around it and reports:

  SENSE 1 / SENSE 2   the marker words decided it
  AMBIGUOUS           no marker either way, or markers for BOTH -- the ones a
                      reader has to guess at, and the work list

It is a WORD-USE check, not a physics check.  An AMBIGUOUS hit is not an error;
it is a place where the sense should be said out loud.

Run: python "internal notes/_check_individuation_senses.py"
     python "internal notes/_check_individuation_senses.py" --full
"""
import io
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FULL = "--full" in sys.argv
WORD = re.compile(r"individuat\w*", re.I)
WINDOW = 340

S1 = re.compile(r"multi-channel|single-channel|\bP11\b|commit|collapse|rate|timescale"
                r"|M_?crit|M_\{?\\mathrm\{crit|unresolved|pointer basis|\btau_|\bGamma_",
                re.I)
S2 = re.compile(r"b_int|b_bdry|b_\{?\\mathrm\{int|theta_ind|\\theta_\{?\\mathrm\{ind"
                r"|system/environment|system-environment|boundary bandwidth"
                r"|boundary-bandwidth|chain-complex|\bcut\b", re.I)

# The disambiguation itself and the notes that established it are ABOUT the
# ambiguity; counting them as ambiguous usage would be circular.
SKIP = ("INDIVIDUATION_DISAMBIGUATION.md", "Note_Individuation_TwoSenses",
        "Note_ThetaInd_", "_check_individuation_senses.py")


def files():
    out = []
    for base in ("physics-papers", "primitives", "internal notes"):
        for dp, _dn, fn in os.walk(base):
            for f in fn:
                if f.endswith(".md") and not any(s in f for s in SKIP):
                    out.append(os.path.join(dp, f))
    return sorted(out)


def main():
    counts = Counter()
    amb = []
    per_file = {}
    for path in files():
        text = io.open(path, encoding="utf-8", errors="replace").read()
        local = Counter()
        for m in WORD.finditer(text):
            lo = max(0, m.start() - WINDOW)
            win = text[lo:m.end() + WINDOW]
            a, b = bool(S1.search(win)), bool(S2.search(win))
            if a and not b:
                k = "SENSE 1 (commitment)"
            elif b and not a:
                k = "SENSE 2 (the cut)"
            elif a and b:
                k = "AMBIGUOUS (both vocabularies)"
            else:
                k = "AMBIGUOUS (no marker)"
            counts[k] += 1
            local[k] += 1
            if k.startswith("AMBIGUOUS"):
                amb.append((path, re.sub(r"\s+", " ", win[WINDOW - 60:WINDOW + 110])))
        if local:
            per_file[path] = local

    total = sum(counts.values())
    print('How "individuation" is used across the corpus')
    print("=" * 78)
    print("  files scanned with a hit : %d      occurrences : %d\n"
          % (len(per_file), total))
    for k in ("SENSE 1 (commitment)", "SENSE 2 (the cut)",
              "AMBIGUOUS (both vocabularies)", "AMBIGUOUS (no marker)"):
        n = counts.get(k, 0)
        print("  %-32s %4d   %4.0f%%" % (k, n, 100.0 * n / total if total else 0))

    print("\n  by file (sense 1 / sense 2 / ambiguous):")
    rows = sorted(per_file.items(),
                  key=lambda kv: -sum(kv[1].values()))[:None if FULL else 14]
    for path, c in rows:
        print("    %-58s %3d / %3d / %3d"
              % (os.path.relpath(path)[:58],
                 c.get("SENSE 1 (commitment)", 0),
                 c.get("SENSE 2 (the cut)", 0),
                 c.get("AMBIGUOUS (both vocabularies)", 0)
                 + c.get("AMBIGUOUS (no marker)", 0)))
    if not FULL and len(per_file) > 14:
        print("    ... and %d more files (--full)" % (len(per_file) - 14))

    if FULL and amb:
        print("\n  ambiguous occurrences in context:")
        for path, ctx in amb[:60]:
            print("    %s\n       ...%s..." % (os.path.relpath(path), ctx))

    print("""
  WHAT TO DO WITH THIS.  An AMBIGUOUS hit is not an error -- it is a place where
  the sense should be said out loud.  The writing rule is in
  `primitives/INDIVIDUATION_DISAMBIGUATION.md` section 4: if the object is a
  CHANNEL, say commitment; if it is a set of LOCI, say cut.

  Sense 1 dominating is expected and is not a defect: sense 1 is P11, which the
  corpus has always had, while sense 2 has one paper, promoted 2026-09-05.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
