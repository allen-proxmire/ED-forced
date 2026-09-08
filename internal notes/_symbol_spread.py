# -*- coding: utf-8 -*-
"""Corpus-wide symbol spread — measures the collision SURFACE, not the registry.

Why this exists. A two-folder pilot was run on foundations + arc-foundations and
returned 77 corpus-shaped symbols, 8 of them spanning the pair. But that scope
would have MISSED the pilot's own strongest find: sigma denotes three unrelated
objects across arc-foundations (the mass signature), Arc_D (transport mobility)
and Black_Holes (the saturation parameter) -- three folders, no pair among them.

So the folder-pair is the wrong unit. The question this answers: how many symbols
are actually defined across MANY folders? That set, not "all symbols in two
folders", is what a checker has to cover.
"""
from __future__ import annotations
import io, os, re, sys, collections

sys.stdout.reconfigure(encoding="utf-8")

EDG = r"C:\Users\allen\GitHub\ED Generative\physics-papers"
EVD = r"C:\Users\allen\GitHub\event-density"

GREEK = ("alpha|beta|gamma|Gamma|delta|Delta|epsilon|theta|Theta|kappa|lambda|Lambda|mu|nu|"
         "pi|Pi|rho|sigma|Sigma|tau|phi|Phi|chi|psi|Psi|omega|Omega")
SYM = re.compile(r"^[\\]?(" + GREEK + r"|[A-Za-z]{1,4})(?:_[{]?[\\]?([A-Za-z0-9]{1,8})[}]?)?$")
MATH = re.compile(r"[$][$]?(.+?)[$][$]?", re.S)
TICK = re.compile(r"`([^`\n]{1,40})`")
DEFCTX = re.compile(r"(\bdefine[sd]?\b|\bdenote[sd]?\b|\bis the\b|\bwhere\b|:=|equiv)", re.I)

STOP = set("""the and for not see per its was are is of in to a an as if or on at by it we so no
yes all one two new old open true false ok eq fig ref cf etc ie eg vs cite text mathrm left right
frac sqrt sum int cdot times approx leq geq neq quad qquad big bigl bigr tfrac hat vec nabla
partial mathcal mathbb langle rangle propto equiv km kg eV MeV GeV TeV nm fm AU Mpc kpc pc yr
sec md acc min max abs log exp cos sin tan val idx tmp py json csv""".split())


def roots():
    out = []
    if os.path.isdir(EDG):
        for d in sorted(os.listdir(EDG)):
            p = os.path.join(EDG, d)
            if os.path.isdir(p):
                out.append((p, "pp/" + d))
    for sub in ("arcs", "theory"):
        base = os.path.join(EVD, sub)
        if not os.path.isdir(base):
            continue
        for d in sorted(os.listdir(base)):
            p = os.path.join(base, d)
            if os.path.isdir(p):
                out.append((p, sub + "/" + d))
    return out


def is_corpus_symbol(k):
    if k in STOP:
        return False
    if "_" in k:
        return True
    if len(k) == 1:
        return False
    return k[0].isupper() or k in ("rho", "sigma", "tau", "phi", "chi", "psi", "mu", "nu", "pi")


raw = collections.Counter()
defined = collections.Counter()
where = collections.defaultdict(set)

RS = roots()
for root, label in RS:
    for dp, _, fns in os.walk(root):
        if ".claude" in dp or "worktrees" in dp:
            continue
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            try:
                txt = io.open(os.path.join(dp, fn), encoding="utf-8").read()
            except Exception:
                continue
            for line in txt.split("\n"):
                toks = []
                for m in MATH.finditer(line):
                    toks += re.split(r"[^A-Za-z0-9_]+", m.group(1))
                for m in TICK.finditer(line):
                    toks += re.split(r"[^A-Za-z0-9_]+", m.group(1))
                isdef = bool(DEFCTX.search(line))
                for t in toks:
                    if not t or t.lower() in STOP:
                        continue
                    mm = SYM.match(t)
                    if not mm or mm.group(1).lower() in STOP:
                        continue
                    raw[t] += 1
                    where[t].add(label)
                    if isdef:
                        defined[t] += 1

cand = [k for k in defined if raw[k] >= 3 and is_corpus_symbol(k)]
buckets = collections.Counter(len(where[k]) for k in cand)

print("=" * 74)
print("CORPUS-WIDE SYMBOL SPREAD  —  %d folders scanned" % len(RS))
print("=" * 74)
print("  corpus-shaped defined symbols: %d" % len(cand))
print()
print("  spread distribution:")
for n in sorted(buckets):
    bar = "#" * min(40, buckets[n])
    print("    defined in %2d folder(s): %3d  %s" % (n, buckets[n], bar))

wide = [k for k in cand if len(where[k]) >= 4]
print()
print("  COLLISION SURFACE — defined in 4+ folders: %d symbols" % len(wide))
for k in sorted(wide, key=lambda k: (-len(where[k]), -raw[k]))[:25]:
    print("    %-14s %2d folders  raw=%-5d  %s"
          % (k, len(where[k]), raw[k], ",".join(sorted(where[k]))[:60]))

print()
print("=" * 74)
print("DESIGN ANSWER")
print("=" * 74)
print("  A two-FOLDER pilot has the wrong unit: the pilot's own strongest find")
print("  (sigma, three objects) spans arc-foundations / Arc_D / Black_Holes,")
print("  and no folder-PAIR contains it.")
print()
print("  Corpus-wide, %d symbols are defined in 4 or more folders." % len(wide))
if len(wide) <= 40:
    print("  -> The checker does NOT need a citation graph over ~77 symbols per")
    print("     folder-pair. It needs a SPREAD CHECK over these %d, corpus-wide." % len(wide))
    print("     That is a lookup, not an NLP problem, and it is one session of work.")
else:
    print("  -> Still large. Restrict further before writing the checker.")
