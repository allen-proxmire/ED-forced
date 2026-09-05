# -*- coding: utf-8 -*-
"""Sweep the corpus for comparative claims about neighbouring literatures.

These are sentences asserting that a RIVAL framework lacks something, or that
ED noticed/derived something first.  They are the one claim type no internal
audit can check (gravity ledger Staleness #60), so they are enumerated here
for individual external verification.
"""
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
os.chdir(r"C:\Users\allen\GitHub\ED Generative")

ROOT = "physics-papers"

# Each pattern is (label, regex).  Deliberately broad; triaged by hand after.
PATS = [
    ("no-analogue",      r"no\s+(\w+\s+){0,3}analogu?e"),
    ("does-not-exist-in",r"does\s+not\s+exist\s+in|doesn't\s+exist\s+in"),
    ("nobody/no-one",    r"\bnobody\b|\bno\s+one\s+has\b"),
    ("never-been",       r"has\s+never\s+been|have\s+never\s+been|had\s+never\s+been"),
    ("unique-to-ED",     r"unique\s+to\s+ED|uniquely\s+ED|only\s+ED\b|ED\s+alone\b"),
    ("first-to",         r"\bthe\s+first\s+(framework|theory|account|paper|to\b)|\bfirst\s+to\s+(derive|note|predict|show|identify)"),
    ("no-other-frmwk",   r"no\s+other\s+(framework|theory|account|approach|program)|no\s+existing\s+(framework|theory|account)"),
    ("not-noted",        r"not\s+been\s+(noted|observed|remarked|recognized|recognised|written\s+down)|never\s+been\s+written\s+down"),
    ("nothing-else",     r"nothing\s+else\s+(in|does|derives|predicts)|no\s+rival\b"),
    ("std-physics-lacks",r"standard\s+(physics|model|cosmology)\s+(has\s+no|lacks|cannot|does\s+not)"),
    ("mond-lacks",       r"(MOND|dark[- ]matter|\u039bCDM|LCDM|GR|general\s+relativity|quantum\s+mechanics)\s+(has\s+no|lacks|cannot|has\s+never|does\s+not\s+(derive|predict|explain|have))"),
    ("genuinely-novel",  r"genuinely\s+novel|truly\s+novel|unprecedented|has\s+no\s+counterpart"),
    ("cannot-in-rival",  r"cannot\s+be\s+(done|derived|obtained|reached)\s+in\b"),
]

hits = {}   # (label) -> list of (path, lineno, text)
for dirpath, _, files in os.walk(ROOT):
    for fn in files:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(dirpath, fn).replace("\\", "/")
        try:
            lines = io.open(path, encoding="utf-8").read().split("\n")
        except Exception as e:
            print("SKIP", path, e); continue
        for i, line in enumerate(lines, 1):
            for label, pat in PATS:
                if re.search(pat, line, re.I):
                    hits.setdefault(label, []).append((path, i, line.strip()))

total = sum(len(v) for v in hits.values())
print("=== SWEEP: %d raw hits across %d pattern classes ===\n" % (total, len(hits)))
for label, _ in PATS:
    v = hits.get(label, [])
    if not v:
        continue
    print("## %s  (%d)" % (label, len(v)))
    for path, i, line in v:
        # trim to the matching neighbourhood so output stays readable
        print("  %s:%d" % (path, i))
        print("     %s" % (line[:400]))
    print()
