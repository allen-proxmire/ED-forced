# -*- coding: utf-8 -*-
"""Find the defect class this corpus generates faster than it catches: two
documents saying related things, neither knowing about the other.

WHY THIS EXISTS
---------------
Every existing checker verifies documents against the LEDGERS. None checks
documents against EACH OTHER. On 2026-09-07 alone, five instances of that shape
turned up, all found by hand or by an outside reader:

  * `M_cap` defined two ways -- min{N_bw,N_V5,N_commit} in Paper_053, and
    (Gamma_indiv^-1/Gamma_0)^(1/gamma) in Paper_054. (ledger #154)
  * The A/B/C classes sorted by two different trichotomies under one name. (#155)
  * Paper_055 row 4 tiering a claim `I` and citing Paper_056, which does not
    contain it. (#155)
  * The alpha-provenance correction living in the Report and never reaching the
    canonical predictions list. (#151)
  * And earlier, |Sigma P|^2 assigned to BOTH Coh and Str. (foundations #10)

Each was invisible to reading either file alone. Each cost a session to find.

TWO DETECTORS, one per shape
----------------------------
A  MULTI-DEFINITION   one symbol given materially different right-hand sides in
                      two or more files.
B  EMPTY PROVENANCE   a claim tiered `I` (inherited) whose cited source does not
                      contain the claim's distinctive words.

Both are CANDIDATE generators, not verdicts. The output is a shortlist a human
reads, the same contract as _triage_open_surface.py. Precision matters more than
recall here: a noisy list gets ignored, and an ignored checker is worse than none.

--selftest plants a synthetic collision of each kind and asserts both are caught.
"""
from __future__ import print_function
import io
import os
import re
import sys
import collections

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "archive"}

# A definition looks like  LHS := RHS  or  LHS = RHS  inside math or a code span.
DEF = re.compile(r"(?<![A-Za-z0-9\\])([\\A-Za-z][\\A-Za-z0-9_{}^() .,-]{1,40}?)\s*(?::=|=)\s*([^\n$`]{6,160})")

# Symbols worth tracking: they carry a subscript or a \mathrm/\mathcal wrapper.
INTERESTING = re.compile(r"_|\\mathrm|\\mathcal|\\Gamma|\\Sigma|\\mathcal")

NOISE_LHS = re.compile(r"^(i|j|k|n|x|y|z|t|r|s|f|g|d|e|a|b|c|p|q|u|v|w|N|M|E|S|T)$")


def norm_symbol(s):
    """Collapse the many spellings of one symbol to a single key."""
    s = s.strip().strip("$` ")
    s = re.sub(r"\\(mathrm|mathcal|mathbf|text|operatorname)\s*", "", s)
    s = s.replace("{", "").replace("}", "").replace("\\", "")
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"\(.*?\)$", "", s)          # drop a trailing argument list
    return s


# The same expression is written both ways across the corpus; comparing the
# spellings instead of the content produced overlap 0.00 on identical formulas.
SPELL = [("\u221a", "sqrt"), ("\u03c0", "pi"), ("\u03a3", "sum"), ("\u2211", "sum"),
         ("\u2207", "nabla"), ("\u0393", "Gamma"), ("\u03c3", "sigma"),
         ("\u03b1", "alpha"), ("\u03b2", "beta"), ("\u03b3", "gamma"),
         ("\u0398", "Theta"), ("\u03b8", "theta"), ("\u03bc", "mu"),
         ("\u2113", "ell"), ("\u00b7", ""), ("\u00d7", "*"), ("\u2212", "-"),
         ("\u2264", "<="), ("\u2265", ">="), ("\u221d", "propto"),
         ("\u2248", "~"), ("\u223c", "~"), ("\u2192", "->")]


# The captured RHS ran into the prose following the formula, so two spellings of
# one definition compared as two definitions. Cut at the first sentence break.
RHS_END = re.compile(r"(?:\$\$|\$|\.\s+[A-Z(]|,\s+(?:where|with|and|which)\b|\s{2,}|\|)")


def norm_rhs(s):
    cut = RHS_END.search(s)
    if cut and cut.start() > 5:
        s = s[:cut.start()]
    s = s.strip().strip("$` .,")
    # \frac{a}{b} and a/b are one thing
    s = re.sub(r"\\frac\s*\{([^{}]{1,40})\}\s*\{([^{}]{1,40})\}", r"(\1)/(\2)", s)
    s = re.sub(r"\\(mathrm|mathcal|mathbf|text|left|right|big|Big|,|;|!|quad|qquad)\s*", "", s)
    for u, a in SPELL:
        s = s.replace(u, a)
    s = re.sub(r"[{}\\$`\s,;]", "", s)
    return s.strip()


def content_tokens(s):
    return set(re.findall(r"[A-Za-z][A-Za-z0-9_]{1,}", s.lower()))


def md_files():
    out = []
    for dp, dn, fn in os.walk("."):
        dn[:] = [d for d in dn if d not in SKIP_DIRS and not d.startswith(".")]
        for f in fn:
            if f.endswith(".md"):
                out.append(os.path.join(dp, f).replace("\\", "/")[2:])
    return out


def rule(c="-", n=78):
    print(c * n)


# --------------------------------------------------------------- detector A
def detect_multidef(texts):
    """Symbols whose definitions split into clusters carried by DISJOINT files."""
    defs = collections.defaultdict(list)          # symbol -> [(file, rhs)]
    for path, text in texts.items():
        for m in DEF.finditer(text):
            lhs_raw, rhs_raw = m.group(1), m.group(2)
            lhs = norm_symbol(lhs_raw)
            if not lhs or len(lhs) < 3 or NOISE_LHS.match(lhs):
                continue
            if not INTERESTING.search(lhs_raw):
                continue
            rhs = norm_rhs(rhs_raw)
            if len(rhs) < 6 or rhs.replace(".", "").isdigit():
                continue
            defs[lhs].append((path, rhs))

    def same(a, b):
        """One definition, two spellings or one plus its intermediate step."""
        ca, cb = a.replace(" ", ""), b.replace(" ", "")
        if ca in cb or cb in ca:
            return True
        strip = lambda x: re.sub(r"_?0|\(z\)|_z", "", x).replace("(", "").replace(")", "")
        if strip(ca) == strip(cb):
            return True
        ta, tb = content_tokens(a), content_tokens(b)
        if not ta or not tb:
            return True
        return len(ta & tb) / float(len(ta | tb)) >= 0.34

    findings = []
    for sym, entries in defs.items():
        if len({p for p, _ in entries}) < 2:
            continue
        clusters = []                              # [(representative, {files})]
        for path, rhs in entries:
            for i, (rep, fs) in enumerate(clusters):
                if same(rep, rhs):
                    fs.add(path)
                    if len(rhs) > len(rep):
                        clusters[i] = (rhs, fs)
                    break
            else:
                clusters.append((rhs, {path}))
        if len(clusters) < 2:
            continue
        # FLAG only where two clusters are carried by disjoint file sets.
        live = []
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                fa, fb = clusters[i][1], clusters[j][1]
                if fa & fb:
                    continue                       # a file carries both: documented
                live.append((clusters[i], clusters[j]))
        if live:
            findings.append((sym, live))
    return findings


# --------------------------------------------------------------- detector B
ROW = re.compile(r"^\|([^|]{8,200})\|\s*\**I\**\s*\|\s*([^|]{3,80})\|", re.M)
SRC = re.compile(r"Paper[_ ]?([0-9]{2,3}[a-z]?|[A-Z][A-Za-z\-]{1,20})")


def detect_empty_provenance(texts):
    base = {os.path.basename(p): p for p in texts}
    findings = []
    for path, text in texts.items():
        for m in ROW.finditer(text):
            claim, src = m.group(1).strip(), m.group(2).strip()
            sm = SRC.search(src)
            if not sm:
                continue
            token = sm.group(1)
            targets = [p for b, p in base.items()
                       if re.search(r"Paper_%s[_.]" % re.escape(token), b)]
            if not targets or path in targets:
                continue
            # distinctive words of the claim: long, not generic
            words = [w for w in re.findall(r"[A-Za-z_]{5,}", claim)
                     if w.lower() not in ("class", "saturates", "substrate", "paper",
                                          "level", "structural", "content", "value",
                                          "values", "inherited", "derived", "constant")]
            words += re.findall(r"N_\{?\\?mathrm\{?[a-zA-Z0-9]+", claim)
            if len(words) < 2:
                continue
            tgt_text = " ".join(texts[t] for t in targets)
            missing = [w for w in set(words) if w not in tgt_text]
            if len(missing) >= max(2, int(0.6 * len(set(words)))):
                findings.append((path, claim[:70], src, sorted(missing)[:5], targets[0]))
    return findings


def main():
    selftest = "--selftest" in sys.argv
    files = md_files()
    texts = {}
    for p in files:
        try:
            texts[p] = io.open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            pass

    print()
    rule("=")
    print("CROSS-DOCUMENT COLLISIONS -- two files, related claims, neither aware")
    rule("=")
    print("  scanned %d markdown files" % len(texts))
    print("  A CANDIDATE GENERATOR, NOT A VERDICT. Expect a meaningful share of the")
    print("  A-list to be one definition written two ways -- formula equivalence is")
    print("  undecidable in prose and chasing it further costs more than reading the")
    print("  list. The useful column is WHICH FILES: two disjoint file sets is the")
    print("  signal; a symbol whose clusters share a file has already been reconciled.")
    print()

    A = detect_multidef(texts)
    B = detect_empty_provenance(texts)

    rule()
    print("A. ONE SYMBOL, MATERIALLY DIFFERENT DEFINITIONS IN TWO FILES  (%d)" % len(A))
    rule()
    if not A:
        print("     none")
    for sym, live in sorted(A, key=lambda x: -len(x[1]))[:12]:
        print("\n     SYMBOL  %s" % sym)
        for (ra, fa), (rb, fb) in live[:2]:
            print("       = %s" % ra[:94])
            print("           in: %s" % ", ".join(sorted(os.path.basename(f) for f in fa))[:88])
            print("       = %s" % rb[:94])
            print("           in: %s" % ", ".join(sorted(os.path.basename(f) for f in fb))[:88])
    print()

    rule()
    print("B. `I`-TIERED CLAIM WHOSE CITED SOURCE LACKS ITS DISTINCTIVE WORDS  (%d)" % len(B))
    rule()
    if not B:
        print("     none")
    for path, claim, src, missing, tgt in B[:12]:
        print("\n     %s" % os.path.basename(path))
        print("       claim   : %s" % claim)
        print("       cites   : %s  -> %s" % (src, os.path.basename(tgt)))
        print("       missing : %s" % ", ".join(missing))
    print()

    if selftest:
        rule()
        print("SELF-TEST")
        rule()
        t = dict(texts)
        t["__synthetic_a1.md"] = "$$\\mathcal{Z}_{\\mathrm{probe}} := \\min\\{ alpha, beta, gamma \\}$$"
        t["__synthetic_a2.md"] = "$$Z_{\\mathrm{probe}} = \\left(\\frac{omega}{kappa}\\right)^{1/n}$$"
        got = [s for s, _ in detect_multidef(t) if s.startswith("Z_probe")]
        print("  %s - detector A catches a planted two-definition symbol"
              % ("PASS" if got else "FAIL"))
        t2 = dict(texts)
        t2["__synthetic_b.md"] = ("| Zorbulator coupling saturates the widget manifold | I | "
                                  "Paper_087. |")
        gotb = [f for f in detect_empty_provenance(t2) if "synthetic_b" in f[0]]
        print("  %s - detector B catches a planted empty citation"
              % ("PASS" if gotb else "FAIL"))
        print()
        if not (got and gotb):
            return 2

    print("  A=%d  B=%d" % (len(A), len(B)))
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
