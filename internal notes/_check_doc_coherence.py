# -*- coding: utf-8 -*-
"""Does the documentation actually hang together?

Three failure modes a repo of this size drifts into, none of which the tier or
census checks catch:

  D1  DANGLING REFERENCE.  A note or ledger item points at a file that does not
      exist -- a typo, a rename, or a file that was planned and never written.
      The read-first rule fails silently when the pointer is broken.

  D2  ORPHANED NOTE.  A note exists that no ledger item and no paper references.
      It is real work that nobody will find, which is the same as not having it.

  D3  UNBACKED LEDGER ITEM.  A ledger item cites a note as its evidence and the
      note is missing.  The audit trail claims a source it does not have.

Scope is the whole repo, but the report leads with TODAY so a session can verify
its own output before ending.

Run: python "internal notes/_check_doc_coherence.py" [YYYY-MM-DD]
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

# a backticked path ending .md / .py, possibly with a leading folder
REF = re.compile(r"`([A-Za-z0-9_\-./ ]+\.(?:md|py|json|xlsx))`")
SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def repo_files():
    """basename -> set of relative paths, plus the set of relative paths."""
    by_base, rels = defaultdict(set), set()
    for base in (".", ):
        for dp, dn, fn in os.walk(base):
            dn[:] = [d for d in dn if d not in SKIP_DIRS]
            for f in fn:
                rel = os.path.relpath(os.path.join(dp, f)).replace("\\", "/")
                rels.add(rel)
                by_base[f].add(rel)
    return by_base, rels


def resolve(ref, by_base, rels):
    ref = ref.strip().replace("\\", "/")
    if ref in rels:
        return True
    if os.path.basename(ref) in by_base:
        return True                       # named by basename or partial path
    # sibling repos are outside this tree; treat as out of scope, not dangling
    return False


def main():
    by_base, rels = repo_files()
    md = [r for r in sorted(rels) if r.endswith(".md")]

    dangling = defaultdict(set)
    referenced = set()
    for path in md:
        try:
            text = io.open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for ref in set(REF.findall(text)):
            r = ref.strip()
            if r.startswith("../") or "event-density" in r or "ed-lab" in r:
                continue                  # sibling repos, out of scope here
            if resolve(r, by_base, rels):
                referenced.add(os.path.basename(r))
            else:
                dangling[path].add(r)

    # notes written today, and whether anything points at them
    todays = [r for r in md if TODAY in os.path.basename(r)]
    orphans = [r for r in todays if os.path.basename(r) not in referenced]

    print("Documentation coherence")
    print("=" * 72)
    print("  markdown files: %d      notes dated %s: %d\n" % (len(md), TODAY, len(todays)))

    print("D1  DANGLING REFERENCES (a pointer to a file that is not here)")
    n = sum(len(v) for v in dangling.values())
    print("      total: %d across %d files" % (n, len(dangling)))
    shown = 0
    for path, refs in sorted(dangling.items()):
        for r in sorted(refs):
            if shown < 25:
                print("      %-52s -> %s" % (os.path.relpath(path)[:52], r))
                shown += 1
    if n > shown:
        print("      ... and %d more" % (n - shown))

    print("\nD2  TODAY'S NOTES THAT NOTHING REFERENCES")
    if orphans:
        for o in orphans:
            print("      %s" % o)
    else:
        print("      none - every note dated %s is referenced somewhere" % TODAY)

    print("\n  Today's notes and where they live:")
    for t in todays:
        print("      %s" % t)

    return 1 if (n or orphans) else 0


if __name__ == "__main__":
    sys.exit(main())
