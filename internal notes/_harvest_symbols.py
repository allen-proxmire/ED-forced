# -*- coding: utf-8 -*-
"""Harvest candidate symbols from foundations + arc-foundations, to MEASURE the
row count before committing to a citation-relative checker.

The point is not to produce the registry. It is to answer one question a
parallel session raised: is the checker's input ~30 symbols or ~300? The
citation-relative rule needs a populated registry AND a machine-readable
citation graph ("B cites A for X"), and corpus citations are prose. If two
folders yield 30 symbols the graph is worth building; if they yield 300 the
graph is the bottleneck and that should be known before writing code against
an assumption.

Reports three numbers, because they measure different things:
  RAW        every distinct math-ish token
  FILTERED   tokens that look like corpus symbols (drops prose, units, refs)
  DEFINED    tokens that appear in a definitional context at least once
             -- the closest mechanical proxy for "load-bearing"
"""
from __future__ import annotations
import io, os, re, sys, collections

sys.stdout.reconfigure(encoding="utf-8")

ROOTS = [
    (r"C:\Users\allen\GitHub\ED Generative\physics-papers\foundations", "foundations"),
    (r"C:\Users\allen\GitHub\event-density\arcs\arc-foundations", "arc-foundations"),
]

# inline math $...$, display $$...$$, and backticked code spans
MATH = re.compile(r"\$\$?(.+?)\$\$?", re.S)
TICK = re.compile(r"`([^`\n]{1,40})`")

# a "symbol" = a base name optionally subscripted, e.g. b_K, rho_max, Sigma_C,
# Gamma_0, M_eff, N_bw, theta_ind, sigma_tau, P_K, w_tau
GREEK = (r"alpha|beta|gamma|Gamma|delta|Delta|epsilon|theta|Theta|kappa|lambda|Lambda|mu|nu|"
         r"pi|Pi|rho|sigma|Sigma|tau|phi|Phi|chi|psi|Psi|omega|Omega")
SYM = re.compile(r"^\\?(" + GREEK + r"|[A-Za-z]{1,4})(?:_\{?\\?([A-Za-z0-9]{1,8})\}?)?$")

# things that are not corpus symbols
STOP = {
    "the","and","for","not","see","per","its","was","are","is","of","in","to","a","an","as",
    "if","or","on","at","by","it","we","so","no","yes","all","one","two","new","old","open",
    "true","false","ok","eq","fig","ref","cf","etc","ie","eg","vs","cite","text","mathrm",
    "left","right","frac","sqrt","sum","int","cdot","times","approx","leq","geq","neq","to",
    "quad","qquad","big","Big","bigl","bigr","tfrac","hat","vec","nabla","partial","Theta",
    "mathcal","mathbb","langle","rangle","propto","equiv","xrightarrow","longrightarrow",
    "km","kg","eV","MeV","GeV","TeV","GHz","nm","fm","AU","Mpc","kpc","pc","yr","sec",
}
DEFCTX = re.compile(r"(\bdefine[sd]?\b|\bdenote[sd]?\b|\bis the\b|\bwhere\b|:=|\\equiv|\bequiv\b|\bwith\b\s*$)", re.I)


def harvest():
    raw = collections.Counter()
    defined = collections.Counter()
    where = collections.defaultdict(set)
    for root, label in ROOTS:
        if not os.path.isdir(root):
            print("  !! missing:", root); continue
        for dp, _, fns in os.walk(root):
            for fn in fns:
                if not fn.endswith(".md"):
                    continue
                p = os.path.join(dp, fn)
                try:
                    txt = io.open(p, encoding="utf-8").read()
                except Exception:
                    continue
                for line in txt.split("\n"):
                    toks = []
                    for m in MATH.finditer(line):
                        toks += re.split(r"[^A-Za-z0-9_\\{}]+", m.group(1))
                    for m in TICK.finditer(line):
                        toks += re.split(r"[^A-Za-z0-9_\\{}]+", m.group(1))
                    isdef = bool(DEFCTX.search(line))
                    for t in toks:
                        t = t.strip("\\{}")
                        if not t or t.lower() in STOP:
                            continue
                        mm = SYM.match(t)
                        if not mm:
                            continue
                        base = mm.group(1)
                        if base.lower() in STOP or len(base) > 6:
                            continue
                        key = t
                        raw[key] += 1
                        where[key].add(label)
                        if isdef:
                            defined[key] += 1
    return raw, defined, where


raw, defined, where = harvest()
# FILTERED: appears at least 3 times (drops one-off prose artifacts)
filtered = {k: v for k, v in raw.items() if v >= 3}
# DEFINED: appears in a definitional context at least once AND >=3 times overall
defd = {k: v for k, v in defined.items() if k in filtered}
spanning = [k for k in defd if len(where[k]) == 2]

print("=" * 74)
print("SYMBOL HARVEST — foundations + arc-foundations")
print("=" * 74)
print("  RAW distinct symbol-shaped tokens        : %4d" % len(raw))
print("  FILTERED (>= 3 occurrences)              : %4d" % len(filtered))
print("  DEFINED  (filtered + definitional context): %4d   <-- checker's input" % len(defd))
print("  ...of which appear in BOTH folders       : %4d   <-- collision surface" % len(spanning))
print()
print("  Top 30 DEFINED by frequency:")
for k, v in sorted(defd.items(), key=lambda kv: -raw[kv[0]])[:30]:
    print("    %-14s raw=%-5d def=%-4d folders=%s" % (k, raw[k], v, ",".join(sorted(where[k]))))
print()
print("  Symbols appearing in BOTH folders (highest collision risk):")
for k in sorted(spanning, key=lambda k: -raw[k])[:25]:
    print("    %-14s raw=%d" % (k, raw[k]))
print()
print("=" * 74)
n = len(defd)
print("DECISION INPUT (the question this script exists to answer)")
print("=" * 74)
print("  Checker input is %d symbols across two folders." % n)
if n <= 60:
    print("  -> TRACTABLE. A citation graph over this many symbols is worth building.")
elif n <= 150:
    print("  -> BORDERLINE. Build the graph for the %d spanning symbols only." % len(spanning))
else:
    print("  -> THE GRAPH IS THE BOTTLENECK, not the registry. Do not write the")
    print("     citation extractor against prose at this scale; restrict to the")
    print("     spanning set (%d) or to a hand-curated load-bearing list." % len(spanning))
print()
print("  NOTE: this counts symbol-shaped TOKENS, not load-bearing claims. It is")
print("  an upper bound on the checker's input, which is the right side to err on")
print("  when costing the work.")
