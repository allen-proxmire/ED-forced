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
once per distinct name regardless of how many papers use it.

Usage:
    python "internal notes/_census_postulates.py"              # summary + drift check
    python "internal notes/_census_postulates.py" --list       # + every name, with sources
    python "internal notes/_census_postulates.py" --triage     # the breadth ladder (research target #20)
    python "internal notes/_census_postulates.py" --all        # widen scope past physics-papers/
    python "internal notes/_census_postulates.py" --update     # re-baseline after a real change

Exit status is 1 when the count has moved from the baseline. That is the point:
run it after any session that names a new postulate, and it will tell you the
foundations arc needs a re-count.
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
BASELINE = 173
BASELINE_DATE = "2026-09-04"
BASELINE_SCOPE = "physics-papers"

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
    names = sorted(n for n in found if n not in variants)
    total = len(names)
    raw = len(found)

    print(f"ED postulate census — scope: {', '.join(roots)}")
    print(f"Basis: distinctly-named `P-Name` postulates; the 13 primitives and P14 excluded.\n")
    print(f"  Distinctly-named postulates : {total}")
    print(f"  Probable spelling variants  : {len(variants)}  (merged out; --list shows them)")
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

    print(f"\n{'-' * 78}")
    if scope != BASELINE_SCOPE:
        print(f"No drift check: baseline was taken at scope '{BASELINE_SCOPE}', this run is '{scope}'.")
        return 0

    if total == BASELINE:
        print(f"No drift. Count matches the {BASELINE_DATE} baseline of {BASELINE}.")
        return 0

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
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
