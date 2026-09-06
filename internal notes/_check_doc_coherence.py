# -*- coding: utf-8 -*-
"""Does the documentation actually hang together?

Two failure modes a repo this size drifts into that the tier and census checks
do not catch:

  D1  DEAD LIVE POINTER.  A line presents a file as somewhere you can go, and it
      is not there.  The read-first rule fails silently when the pointer is
      broken -- and `PAPERS_INDEX.md`, `ED_ORIENTATION.md` and `ED_MEMORY.md`
      are exactly where `CLAUDE.md` sends a session first.

  D2  ORPHANED NOTE.  A note nothing references.  Real work nobody will find,
      which is the same as not having it.

TWO THINGS THIS DELIBERATELY DOES NOT FLAG, because flagging them made the first
version of this check useless:

  PROVENANCE.  A dead filename named ON PURPOSE is not a defect.  PAPERS_INDEX
  keeps a removed-files provenance table; the orientation notes carry
  struck-through rows recording what went where.  A reference only counts as a
  live pointer if its line carries no strike-through and no death-word.

  SIBLING REPOS.  `event-density/` and `ed-lab/` hold the probe scripts and
  working docs this repo cites by bare filename.  Those are indexed and treated
  as resolved, with a separate count, rather than reported as missing.

Run: python "internal notes/_check_doc_coherence.py" [YYYY-MM-DD] [--full]
"""
import io
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

TODAY = next((a for a in sys.argv[1:] if re.match(r"^20\d\d-\d\d-\d\d$", a)), "2026-09-06")
FULL = "--full" in sys.argv

REF = re.compile(r"`([A-Za-z0-9_\-./ ]+\.(?:md|py|json|xlsx|pdf))`")
DEATH = r"deleted|removed|rename|retired|supersed|archived|moved|provenance|no longer|" \
        r"never existed|gitignored|former|stale|now in|excluded|correction|was\s+`"
PROVENANCE = re.compile(r"~~|" + DEATH, re.I)
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
SIBLINGS = (r"C:\Users\allen\GitHub\event-density", r"C:\Users\allen\GitHub\ed-lab",
            r"C:\Users\allen\GitHub\ED Primitives")
NAV = ("PAPERS_INDEX.md", "README.md",
       "internal notes/ED_ORIENTATION.md", "internal notes/ED_MEMORY.md")


def index(root):
    by_base, rels = defaultdict(set), set()
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), root).replace("\\", "/")
            rels.add(rel)
            by_base[f].add(rel)
    return by_base, rels


def main():
    by_base, rels = index(".")
    sib = set()
    for s in SIBLINGS:
        if os.path.isdir(s):
            sib |= set(index(s)[0].keys())

    md = [r for r in sorted(rels) if r.endswith(".md")]
    dead, in_sibling, referenced = defaultdict(set), 0, set()

    for path in md:
        try:
            text = io.open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for ref in set(REF.findall(text)):          # D2 uses every mention
            referenced.add(os.path.basename(ref.strip()))
        for line in text.split("\n"):
            if PROVENANCE.search(line):
                continue                            # a deliberate record
            for ref in set(REF.findall(line)):
                r = ref.strip()
                if r.startswith("../"):
                    continue
                b = os.path.basename(r)
                if r in rels or b in by_base:
                    continue
                if b in sib:
                    in_sibling += 1
                else:
                    dead[path].add(r)

    todays = [r for r in md if TODAY in os.path.basename(r)]
    orphans = [r for r in todays if os.path.basename(r) not in referenced]
    n = sum(len(v) for v in dead.values())
    nav_dead = {p: v for p, v in dead.items() if p.replace("\\", "/") in NAV}

    print("Documentation coherence")
    print("=" * 74)
    print("  markdown files: %d      notes dated %s: %d\n" % (len(md), TODAY, len(todays)))
    print("D1  DEAD LIVE POINTERS (provenance lines and sibling repos excluded)")
    print("      in the four NAVIGATION files : %d   <- these are the ones that matter"
          % sum(len(v) for v in nav_dead.values()))
    print("      everywhere else              : %d" % (n - sum(len(v) for v in nav_dead.values())))
    print("      resolved in a sibling repo   : %d  (not defects)" % in_sibling)
    if nav_dead:
        for p, v in sorted(nav_dead.items()):
            for r in sorted(v):
                print("        %-34s -> %s" % (p, r))
    shown = 0
    for p, v in sorted(dead.items()):
        if p.replace("\\", "/") in NAV:
            continue
        for r in sorted(v):
            if FULL or shown < 12:
                print("      %-50s -> %s" % (os.path.relpath(p)[:50], r))
                shown += 1
    if not FULL and n - shown > 0:
        print("      ... (--full for the rest)")

    print("\nD2  TODAY'S NOTES THAT NOTHING REFERENCES")
    print("      %s" % ("\n      ".join(orphans) if orphans
                        else "none - every note dated %s is referenced" % TODAY))
    return 1 if (nav_dead or orphans) else 0


if __name__ == "__main__":
    sys.exit(main())
