"""
Census ED's declared postulate load, mechanically, so the number cannot go stale.

The corpus states its own postulate count in four places with four different
accounting bases, and on 2026-09-04 the two most authoritative (Paper_088's boxed
"31 total", Paper_087 §4.15's "~35") were understated by roughly a factor of two
while Paper_100's "60+" was right. That is Gravity_TieredClaims_Ledger.md
Staleness #33 and event-density research target #20. This script exists so the
count is a measurement rather than a recollection, and so drift is detected the
next time it happens instead of two months later.

BASIS (declared, per target #20 — a count without a stated basis is what caused
the problem): distinctly-named postulates of the form `P-Name` appearing anywhere
in the scanned corpus. Excluded: the 13 canonical primitives and P14 (written
P01..P14, which this pattern does not match), and the denylist below. Counted
once per distinct name regardless of how many papers use it. A name occurring
ONLY in a ledger/note/README is excluded: it has been written about, not declared.

SECOND JOB, added 2026-09-05 — the predictions cross-check.
-----------------------------------------------------------
On 2026-09-05 the soft-matter transport arc was found to have no entry at all in
`ED_Master_Predictions_List.md`, despite its own paper calling co-onset its
"distinctive, falsifiable, ED-owned content". A distinctive bet had sat outside
the corpus's own prediction inventory since the paper was written, and nothing
flagged it because nothing cross-checks arc papers against the master list. That
is checklist item 21's third face (an inventory is a propagation target too) and
it is the one instance of the day's defect pattern a script can actually catch.

Three checks, chosen for precision rather than coverage:

  P1  Named falsifiers (`F-NAME`) that the master list never mentions.
  P2  Master-list paper citations that resolve to no file in the corpus.
  P3  Papers whose own prose calls their falsifier content distinctive or
      ED-owned, which the master list does not cite.

WHY NAMED FALSIFIERS AND NOT `F1`/`F2`. A first attempt keyed on any paper with a
falsification section: 210 papers, 180 of them absent from the master list, which
is noise -- the list is a curated superset of the sharp bets, not an index of
every paper. The `F1`/`F2` numbering is per-paper and not unique (600+ uses), so
it cannot join anything. But a paper *names* a falsifier exactly when it is
specific enough to be a bet. That makes `F-NAME` the natural join key between a
paper and the inventory, and P1 enforces it as one.

Usage:
    python "internal notes/_census_postulates.py"              # both drift checks
    python "internal notes/_census_postulates.py" --list       # + every name, with sources
    python "internal notes/_census_postulates.py" --triage     # the breadth ladder (research target #20)
    python "internal notes/_census_postulates.py" --predictions  # the full cross-check detail
    python "internal notes/_census_postulates.py" --all        # widen scope past physics-papers/
    python "internal notes/_census_postulates.py" --update     # re-baseline after a real change

Exit status is 1 when either the postulate count or the orphaned-falsifier set has
moved from its baseline. That is the point: run it after any session that names a
new postulate or a new falsifier, and it will say which list has gone stale.
"""
import io, os, re, sys
from collections import defaultdict

try:                      # Windows consoles default to cp1252 and mangle the output
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- baseline -----------------------------------------------------------------
# Update ONLY via --update, and only when the change is real (a postulate was
# genuinely added or removed). A moved count with no corresponding paper change
# means the pattern or the scope changed, which is a bug in this script.
BASELINE = 175
BASELINE_DATE = "2026-09-07"
BASELINE_SCOPE = "physics-papers"

# --- predictions cross-check baseline ----------------------------------------
# The orphan SET, not just its size, so that fixing one and adding another is
# still detected. 19 of 19 named falsifiers were orphaned when this was first
# run: the join-key convention did not exist as a discipline, it existed only as
# a habit. Clearing this backlog means adding the label to the relevant master-
# list row, which is a one-line edit per falsifier and makes the list navigable
# from the papers for the first time.
MASTER_LIST = "physics-papers/predictions/ED_Master_Predictions_List.md"

# Named falsifiers that are NOT predictions and must not be pushed into the
# predictions list. Clearing the 2026-09-05 backlog showed the `F-` convention
# covers two different objects: empirical bets, and theory-internal conditions
# that a derivation rather than an experiment would settle. Forcing the second
# kind into a predictions list would misrepresent it, so they are exempted here
# WITH the reason attached -- an unexplained exemption is how a check quietly
# stops meaning anything.
NOT_A_PREDICTION = {
    "F-Gauge": "verdict-UPGRADE condition, not a falsifier: deriving P-Gauge moves "
               "Paper_114 M2 -> M1. Nothing about the world decides it.",
    "F-BC":    "fires on a substrate-level demonstration that horizon content resolves "
               "across Sigma_{R_H} rather than Sigma_R. A derivation refutes it, not an "
               "experiment. (Paper_030)",
    "F-P":     "reformulated 2026-09-04 because it could not fire: needs two independent "
               "determinations of l_ED and the corpus has one. Conditional on a "
               "determination that does not exist today. (Paper_027)",
}
PRED_BASELINE = ()
PRED_BASELINE_DATE = "2026-09-05"

# --- scope --------------------------------------------------------------------
# Default: physics-papers/ only. `readings/` is deliberately excluded even under
# --all: it covers OTHER theories, whose postulates are not ED's.
DEFAULT_ROOTS = ["physics-papers"]
WIDE_ROOTS = ["physics-papers", "position-paper", "essays", "theorems",
              "primitives", "layers", "scale correspondence"]
SKIP_DIRS = {"readings", "__pycache__", ".git", "internal notes"}

# --- the pattern --------------------------------------------------------------
# A postulate name is `P-` followed by a capitalized word, optionally hyphenated.
# Requiring the capital is what separates `P-Gauge` from prose like
# `P-construction`. Trailing hyphens and stray punctuation are trimmed.
NAME = re.compile(r"\bP-[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*")

# Known non-postulates that survive the capital test. Keep this list short and
# justified — anything added here is a claim that the token is not a postulate.
DENY = {
    "P-Codim",          # fragment of P-Codim-1 when the digit is split by markup
    "P-V5",             # fragment of the P-V5-* family
    "P-RB",             # fragment of P-RB-1
}

# Fenced code blocks and inline code that is obviously a path are not prose.
FENCE = re.compile(r"^```", re.M)


def strip_fences(text):
    """Drop fenced code blocks so scripts quoting postulate names don't count."""
    out, inside = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return "\n".join(out)


def markdown_files(roots):
    for root in roots:
        base = os.path.join(REPO, root)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if fn.endswith(".md"):
                    yield os.path.join(dirpath, fn)


def census(roots):
    """Return {name: {relpath: occurrences}}."""
    found = defaultdict(lambda: defaultdict(int))
    for path in markdown_files(roots):
        try:
            text = io.open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            print(f"  ! could not decode, skipped: {path}", file=sys.stderr)
            continue
        rel = os.path.relpath(path, REPO).replace("\\", "/")
        for m in NAME.finditer(strip_fences(text)):
            name = m.group(0).rstrip("-")
            if name in DENY:
                continue
            found[name][rel] += 1
    return found


def find_variants(found):
    """Probable spelling variants rather than distinct postulates.

    A name that appears exactly ONCE in the whole corpus and is a hyphen-extension
    (either direction) of a name that appears repeatedly is almost always a prose
    variant or a ledger abbreviation: `P-Adiabatic-CG` for `P-Adiabatic-Coarse-
    Graining`, `P-Bipartite-Mapping-like`, `P-AcousticMetric-postulated`.

    The single-occurrence condition is what makes this safe. Genuinely distinct
    siblings both recur -- `P-Cutoff-Saturation` (8x) and its `-Endpoint` variant
    (7x) are two real postulates and neither is touched here.
    """
    totals = {n: sum(f.values()) for n, f in found.items()}
    variants = {}
    for n, t in totals.items():
        if t != 1:
            continue
        for m, tm in totals.items():
            if m == n or tm <= 1:
                continue
            if n.startswith(m + "-") or m.startswith(n + "-"):
                variants[n] = m
                break
    return variants


def is_paper(rel):
    """A paper USES a postulate. A ledger, note or README only CATALOGUES it."""
    b = os.path.basename(rel)
    return not (b.endswith("Ledger.md") or b.startswith("Note_") or b.startswith("README"))


def triage(found, variants):
    """The breadth ladder answering research target #20.

    'How much does ED assume?' has no single answer, because the honest number
    depends on what you count. Breadth of use is the one basis that is mechanical
    and arguable: a postulate invoked in ONE paper is a modelling choice local to
    that derivation (the way a gauge choice is); one invoked across many papers is
    a standing commitment of the framework.
    """
    names = sorted(n for n in found if n not in variants)
    breadth = {n: len({f for f in found[n] if is_paper(f)}) for n in names}
    orphans = [n for n in names if breadth[n] == 0]

    print(f"\n{'-' * 78}\nBREADTH LADDER — research target #20\n")
    print("  Basis: number of distinct PAPERS naming the postulate.")
    print("  Ledgers, research notes and READMEs excluded — they catalogue, they do not use.\n")
    for thr, label in ((1, "declared anywhere"),
                       (2, "outlives its own derivation"),
                       (3, "used in three or more"),
                       (4, "cross-cutting")):
        n = sum(1 for v in breadth.values() if v >= thr)
        print(f"   used in >= {thr} paper(s): {n:>3}   + 13 primitives = {n + 13:>3}   ({label})")
    single = sum(1 for v in breadth.values() if v == 1)
    print(f"\n   exactly 1 paper : {single:>3}  ({100*single/len(names):.0f}% — local modelling choices)")
    if orphans:
        print(f"   0 papers        : {len(orphans):>3}  (named only in a ledger/note — abbreviations, not postulates)")
        for o in orphans:
            print(f"                      {o}")
    print("\n  The cross-cutting set (>= 4 papers) — the framework's standing commitments:\n")
    for n in sorted((n for n in names if breadth[n] >= 4), key=lambda n: (-breadth[n], n)):
        print(f"   {breadth[n]:>2} papers  {n}")
    print("\n  No single row here is 'the' number. Quote a row WITH its basis, never a bare count.")
    print("  See internal notes/POSTULATE_BASIS.md and research target #20.")


# =============================================================================
# The predictions cross-check
# =============================================================================

# A named falsifier: `F-` then a capital, then letters/digits, hyphen-extensible.
# The capital is what separates `F-RATIO` from prose like `F-test`.
FALSIFIER = re.compile(r"\bF-[A-Z][A-Za-z0-9\u03c0]*(?:-[A-Za-z0-9]+)*")

# Phrases a paper uses when it believes its own falsifier is a distinctive bet.
DISTINCTIVE = re.compile(
    r"ED-owned|ED-distinctive|the distinctive one|distinctive, falsifiable"
    r"|distinctive and falsifiable|the distinctive bets", re.I)

# `**F1`-style local labels. Not a join key -- used only to tell a paper that
# declares falsifiers from one that merely mentions the word.
LOCAL_FALSIFIER = re.compile(r"\*\*F[-0-9]")


def paper_index(roots):
    """{basename without .md: relpath} for every markdown file in scope."""
    idx = {}
    for path in markdown_files(roots):
        rel = os.path.relpath(path, REPO).replace("\\", "/")
        idx.setdefault(os.path.basename(rel)[:-3], rel)
    return idx


def predictions_crosscheck(roots):
    """P1/P2/P3. Returns (orphans, dangling, distinctive_uncited).

    `orphans` is {name: [papers that define it]} for named falsifiers absent from
    the master list. `dangling` is master-list citations resolving to no file.
    `distinctive_uncited` is papers claiming distinctive falsifier content that
    the master list does not cite.
    """
    ml_path = os.path.join(REPO, MASTER_LIST)
    if not os.path.isfile(ml_path):
        return None, None, None
    ml = io.open(ml_path, encoding="utf-8").read()
    idx = paper_index(roots)

    orphans, distinctive_uncited = defaultdict(list), []
    for path in markdown_files(roots):
        rel = os.path.relpath(path, REPO).replace("\\", "/")
        if not is_paper(rel) or rel == MASTER_LIST:
            continue
        try:
            text = io.open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        body = strip_fences(text)
        for name in sorted(set(FALSIFIER.findall(body))):
            if name in NOT_A_PREDICTION:
                continue          # exempt by declared reason, not by string match
            if name not in ml:
                orphans[name].append(rel)
        stem = os.path.basename(rel)[:-3]
        if (DISTINCTIVE.search(body) and LOCAL_FALSIFIER.search(body)
                and stem not in ml):
            distinctive_uncited.append(rel)

    # P2 -- a citation resolves if any paper's basename starts with it, because
    # the list cites both `Paper_029` and `Paper_029_a0` for the same file.
    dangling = []
    for m in re.finditer(r"`([A-Za-z0-9_/.\-]+?)(?:\.md)?`", ml):
        tok = m.group(1).split("/")[-1]
        if not (tok.startswith("Paper_") or "Predictions" in tok or "Falsifiers" in tok):
            continue
        if not any(k == tok or k.startswith(tok) for k in idx):
            dangling.append(tok)
    return dict(orphans), sorted(set(dangling)), distinctive_uncited


def report_predictions(orphans, dangling, distinctive_uncited, verbose):
    """Print the cross-check. Returns True if anything has drifted."""
    if orphans is None:
        print(f"\n  ! master list not found at {MASTER_LIST}; cross-check skipped.")
        return False

    now = tuple(sorted(orphans))
    new = [n for n in now if n not in PRED_BASELINE]
    fixed = [n for n in PRED_BASELINE if n not in now]

    print(f"\n{'-' * 78}\nPREDICTIONS CROSS-CHECK \u2014 papers against {MASTER_LIST}\n")
    print(f"  Named falsifiers orphaned : {len(now):>3}  (baseline {len(PRED_BASELINE)}, {PRED_BASELINE_DATE})")
    print(f"  Dangling citations        : {len(dangling):>3}  (master list \u2192 no such file)")
    print(f"  Distinctive but uncited   : {len(distinctive_uncited):>3}  (paper claims a distinctive bet; list has no row)")
    print(f"  Exempt \u2014 not predictions  : {len(NOT_A_PREDICTION):>3}  (theory-internal conditions; --predictions for why)")

    if verbose:
        if orphans:
            print("\n  P1 \u2014 named falsifiers the master list never mentions:\n")
            for name in now:
                mark = "NEW " if name in new else "    "
                print(f"   {mark}{name:<14} {'; '.join(orphans[name])}")
        if dangling:
            print("\n  P2 \u2014 master-list citations with no matching file:\n")
            for c in dangling:
                print(f"       {c}")
        if distinctive_uncited:
            print("\n  P3 \u2014 papers claiming distinctive falsifier content, absent from the list:\n")
            for p in distinctive_uncited:
                print(f"       {p}")
        print("\n  Exempt \u2014 named falsifiers that are NOT predictions:\n")
        for name in sorted(NOT_A_PREDICTION):
            print(f"       {name:<14} {NOT_A_PREDICTION[name]}")
        print("\n  A P1 hit is cleared by adding the label to the relevant master-list row,")
        print("  not by deleting it from the paper. The label is the join key: without it")
        print("  the list cannot be navigated from the papers, which is how the transport")
        print("  arc stayed invisible. See gravity ledger Staleness #63.")

    drift = bool(new or fixed)
    if new:
        print(f"\n  DRIFT \u2014 {len(new)} newly orphaned falsifier(s): {', '.join(new)}")
        print("  A paper named a falsifier and the prediction inventory does not know it.")
    if fixed:
        print(f"\n  Resolved since baseline: {', '.join(fixed)} \u2014 re-baseline with --update.")
    if not drift:
        print(f"\n  No drift against the {PRED_BASELINE_DATE} orphan set.")
    return drift


def update_pred_baseline(orphans):
    """Rewrite PRED_BASELINE in this file after the orphan set legitimately moves."""
    import datetime
    today = datetime.date.today().isoformat()
    src = io.open(__file__, encoding="utf-8").read()
    lit = "(" + ", ".join(repr(n) for n in sorted(orphans)) + ")"
    src = re.sub(r"^PRED_BASELINE = \(.*\)$", "PRED_BASELINE = " + lit, src, count=1, flags=re.M)
    src = re.sub(r'^PRED_BASELINE_DATE = ".*"$', f'PRED_BASELINE_DATE = "{today}"', src, count=1, flags=re.M)
    open(__file__, "wb").write(src.encode("utf-8"))
    print(f"Predictions baseline updated: {len(orphans)} orphaned falsifier(s) ({today}).")


def update_baseline(new_count, scope):
    """Rewrite the BASELINE constants in this file."""
    import datetime
    today = datetime.date.today().isoformat()
    src = io.open(__file__, encoding="utf-8").read()
    src = re.sub(r"^BASELINE = \d+$", f"BASELINE = {new_count}", src, count=1, flags=re.M)
    src = re.sub(r'^BASELINE_DATE = ".*"$', f'BASELINE_DATE = "{today}"', src, count=1, flags=re.M)
    src = re.sub(r'^BASELINE_SCOPE = ".*"$', f'BASELINE_SCOPE = "{scope}"', src, count=1, flags=re.M)
    open(__file__, "wb").write(src.encode("utf-8"))
    print(f"\nBaseline updated: {new_count} ({today}, scope={scope}).")
    print("Now update Foundations_TieredClaims_Ledger.md staleness #3 and, if the")
    print("stated figures in Paper_087/Paper_088 have moved out of date again, their")
    print("census notes. A baseline bump with no ledger entry is the exact failure")
    print("this script was written to catch (checklist item 21).")


def main():
    args = set(sys.argv[1:])
    wide = "--all" in args
    roots = WIDE_ROOTS if wide else DEFAULT_ROOTS
    scope = "all" if wide else "physics-papers"

    found = census(roots)
    variants = find_variants(found)
    # A postulate must appear in at least one PAPER. A name that occurs only in a
    # ledger, note or README has been *written about*, not declared -- and writing
    # about one in a ledger used to inflate this count (2026-09-04: reporting the
    # SC-4.x census in a ledger entry added two names to the corpus's own total).
    ledger_only = [n for n in found
                   if n not in variants and not any(is_paper(f) for f in found[n])]
    names = sorted(n for n in found if n not in variants and n not in ledger_only)
    total = len(names)
    raw = len(found)

    print(f"ED postulate census — scope: {', '.join(roots)}")
    print(f"Basis: distinctly-named `P-Name` postulates; the 13 primitives and P14 excluded.\n")
    print(f"  Distinctly-named postulates : {total}")
    print(f"  Probable spelling variants  : {len(variants)}  (merged out; --list shows them)")
    print(f"  Ledger/note-only names      : {len(ledger_only)}  (excluded \u2014 written about, not declared)")
    print(f"  Raw pattern matches         : {raw}")
    print(f"  Total occurrences           : {sum(sum(f.values()) for f in found.values())}")
    print(f"  With the 13 primitives      : {13 + total}")

    print("\nAgainst the figures stated in the corpus:")
    print(f"  Paper_088 (boxed, Wave-2 scope) : 13 + ~18 = 31")
    print(f"  Paper_087 §4.15 (round-5)       : 13 + ~22 = ~35")
    print(f"  Paper_100 (program overview)    : 60+")
    print(f"  This census                     : 13 + {total} = {13 + total}")

    if "--triage" in args:
        triage(found, variants)

    if "--list" in args:
        print(f"\n{'-' * 78}\nThe names, with occurrence count and where they appear:\n")
        for name in names:
            files = found[name]
            n = sum(files.values())
            first = sorted(files, key=lambda f: (-files[f], f))[0]
            extra = f" (+{len(files) - 1} more file{'s' if len(files) > 2 else ''})" if len(files) > 1 else ""
            print(f"  {name:<46} {n:>4}x  {first}{extra}")
        if variants:
            print(f"\n  Merged out as probable variants ({len(variants)}):\n")
            for v in sorted(variants):
                print(f"    {v:<44} -> {variants[v]}")

    # --- postulate drift ------------------------------------------------------
    print(f"\n{'-' * 78}")
    postulate_drift = False
    if scope != BASELINE_SCOPE:
        print(f"No drift check: baseline was taken at scope '{BASELINE_SCOPE}', this run is '{scope}'.")
    elif total == BASELINE:
        print(f"No drift. Count matches the {BASELINE_DATE} baseline of {BASELINE}.")
    else:
        postulate_drift = True
        delta = total - BASELINE
        print(f"DRIFT: {total} vs the {BASELINE_DATE} baseline of {BASELINE} ({delta:+d}).")
        print("\nThe corpus's declared postulate load has changed and the foundations arc")
        print("does not know it. Before re-baselining:")
        print("  1. Confirm the change is real (a postulate was named or retired), not a")
        print("     pattern artifact. Run with --list and diff against the last list.")
        print("  2. Record it in physics-papers/foundations/Foundations_TieredClaims_Ledger.md,")
        print("     staleness #3, and in the paper that introduced it.")
        print("  3. If Paper_087/Paper_088's census notes are now wrong again, update them.")
        print("  4. Then re-run with --update.")
        if "--update" in args:
            update_baseline(total, scope)
            postulate_drift = False

    # --- predictions cross-check ---------------------------------------------
    # Always run. The failure it exists to catch (an arc's falsifiers absent from
    # the prediction inventory) is silent by construction, so it must not be
    # behind a flag -- the flag only controls how much detail is printed.
    orphans, dangling, distinctive_uncited = predictions_crosscheck(roots)
    pred_drift = report_predictions(orphans, dangling, distinctive_uncited,
                                    verbose="--predictions" in args)
    if pred_drift and "--update" in args and orphans is not None:
        update_pred_baseline(orphans)
        pred_drift = False

    if orphans is not None and not ("--predictions" in args):
        print("\n  Run with --predictions for the full list.")

    return 1 if (postulate_drift or pred_drift) else 0


if __name__ == "__main__":
    sys.exit(main())
