# -*- coding: utf-8 -*-
"""C5 — claims the arc ledgers carry that the claim register never received.

THE GAP THIS FILLS.  C1, C2 and C4 all audit rows that EXIST in
`ED_ItemizedTheory_TieredClaims*.xlsx`: C1 asks whether a postulate is mentioned,
C2 whether a row is stale, C4 whether a `Derived` row rests on a postulate.
NOTHING looked for a claim the corpus has made and the register never received.

That gap was found the hard way on 2026-09-06: universal free fall was carried by
`Foundations_TieredClaims_Ledger.md` #9 and `Gravity_TieredClaims_Ledger.md`
Staleness #69, both dated 2026-09-05, and had NO ROW in the register at all --
zero hits across 436 rows.  Not a stale row.  A missing one.  It surfaced only
because an external reader raised it and the placement work went looking.

WHAT THIS DOES.  Two passes, because claims reach a ledger by two routes.

  C5a  CLAIM TABLES -- every `| Claim | Paper |` table row.  Tidy and precise.

  C5b  NUMBERED ITEMS -- the staleness / finding entries.  Noisier, and it is
       the path that matters: UFF lived in `Foundations` item #9, NOT in a
       claim table, so a table-only check would have MISSED the very case it
       was built for.  Only items asserting a state of the theory are kept
       (a verdict word must appear); process notes are skipped.

`--selftest` proves C5b works by hiding the universal-free-fall row from the
register and checking the item comes back flagged.

MATCHING, AND WHY IT IS DELIBERATELY LOOSE.  The same claim is worded differently
in a ledger and in the register -- that is normal and is not the defect being
looked for.  So a ledger row counts as COVERED when the register has a row for
the same paper whose claim text shares enough content words, and the threshold is
set low on purpose: a false "covered" costs nothing, while a false "missing"
wastes a read.  The output is therefore a SHORTLIST TO READ, not a defect count.

Run: python "internal notes/_check_register_coverage.py"
     python "internal notes/_check_register_coverage.py" --full
     python "internal notes/_check_register_coverage.py" --threshold 0.5
"""
import io
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

XLSX = next((a for a in sys.argv[1:] if a.endswith(".xlsx")),
            "ED_ItemizedTheory_TieredClaims_v2.xlsx")
FULL = "--full" in sys.argv
THRESH = 0.34
if "--threshold" in sys.argv:
    THRESH = float(sys.argv[sys.argv.index("--threshold") + 1])

# words that carry no discriminating content between two claim statements
STOP = set("""the a an and or of to in on for from with by is are was were be been it its this that
these those as at not no non via given under over into onto per than then so if but only also both
each any all one two three new same other more most less least such which what when where how why
its it's ed substrate level claim claim's paper papers result results form forms value values""".split())
WORD = re.compile(r"[a-z0-9_]+")


def norm(text):
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text or "")     # links -> label
    t = re.sub(r"[*`~_$\\]", " ", t)
    t = t.lower()
    return {w for w in WORD.findall(t) if w not in STOP and len(w) > 2}


def ledgers():
    out = []
    for dp, _dn, fn in os.walk("physics-papers"):
        for f in fn:
            if f.endswith("_TieredClaims_Ledger.md"):
                out.append(os.path.join(dp, f))
    return sorted(out)


def ledger_claims():
    """(arc, paper, claim_text) for every claim-table row in every arc ledger."""
    rows = []
    for path in ledgers():
        arc = os.path.basename(os.path.dirname(path))
        in_table = False
        for line in io.open(path, encoding="utf-8", errors="replace"):
            l = line.rstrip()
            if l.startswith("| Claim ") and "| Paper " in l:
                in_table = True
                continue
            if in_table:
                if not l.startswith("|"):
                    in_table = False
                    continue
                if re.match(r"^\|[\s\-:|]+\|?$", l):
                    continue
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                if len(cells) < 2 or not cells[0]:
                    continue
                rows.append((arc, cells[1], cells[0]))
    return rows


VERDICT = re.compile(
    r"\bunestablished\b|\bnot established\b|\bunproven\b|\bnot proven\b|\bopen\b"
    r"|\bforced\b|\bderived\b|\bmeasured\b|\binherited\b|\bpostulated\b"
    r"|\bfalsifi|\bre-?tier|\bwithdraw", re.I)
ITEM = re.compile(r"^(\d+)\. \*\*(.+)$")


def ledger_items():
    """(arc, number, headline) for numbered ledger entries that assert a STATE.

    A ledger's numbered items are mostly process notes -- 'propagation fixed',
    'audit run'. Only those carrying a verdict word are candidates for being a
    claim the register should hold."""
    out = []
    for path in ledgers():
        arc = os.path.basename(os.path.dirname(path))
        for line in io.open(path, encoding="utf-8", errors="replace"):
            m = ITEM.match(line.rstrip())
            if not m:
                continue
            head = m.group(2)
            head = head.split(".")[0] if len(head.split(".")[0]) > 40 else head[:220]
            if VERDICT.search(head):
                out.append((arc, m.group(1), head))
    return out


def main():
    import openpyxl
    ws = openpyxl.load_workbook(XLSX, read_only=True)["Ledger w Claims"]
    data = list(ws.iter_rows(values_only=True))
    hdr = [str(c) if c else "" for c in data[0]]
    ix = {h: n for n, h in enumerate(hdr) if h}

    by_paper = defaultdict(list)
    allreg = []
    for v in data[1:]:
        if not any(v):
            continue
        paper = str(v[ix["Paper"]] or "").strip()
        toks = norm(" ".join(str(c) for c in v if c))
        by_paper[paper].append(toks)
        allreg.append(toks)

    claims = ledger_claims()
    missing, covered = [], 0
    for arc, paper, claim in claims:
        ct = norm(claim)
        if len(ct) < 3:
            continue                       # too short to judge
        cands = by_paper.get(paper.strip(), [])
        if not cands:                      # paper naming differs; fall back to all
            cands = allreg
        best = max((len(ct & r) / len(ct) for r in cands), default=0.0)
        if best >= THRESH:
            covered += 1
        else:
            missing.append((best, arc, paper, claim))

    n = covered + len(missing)
    print("C5 - arc-ledger claims with no register row")
    print("=" * 78)
    print("  register: %s      arc ledgers: %d" % (XLSX, len(ledgers())))
    print("  ledger claim rows read : %d" % n)
    print("  matched in the register: %d  (%.0f%%)" % (covered, 100.0 * covered / n if n else 0))
    print("  NO MATCH               : %d  <- the shortlist to read\n" % len(missing))
    missing.sort()
    show = missing if FULL else missing[:20]
    for best, arc, paper, claim in show:
        print("  [%.2f] %-16s %-14s %s"
              % (best, arc[:16], paper[:14], re.sub(r"\s+", " ", claim)[:78]))
    if not FULL and len(missing) > 20:
        print("  ... and %d more (--full)" % (len(missing) - 20))

    # ---- C5b: the numbered items, which is where UFF lived -------------------
    hide = "--selftest" in sys.argv
    if hide:
        allreg2, by_paper2 = [], defaultdict(list)
        for v in data[1:]:
            if not any(v):
                continue
            blob = " ".join(str(c) for c in v if c)
            if re.search(r"free.fall|equivalence.principle", blob, re.I):
                continue                   # hide the known row
            allreg2.append(norm(blob))
    else:
        allreg2 = allreg

    items = ledger_items()
    unmatched = []
    for arc, num, head in items:
        ht = norm(head)
        if len(ht) < 5:
            continue
        best = max((len(ht & r) / len(ht) for r in allreg2), default=0.0)
        if best < THRESH:
            unmatched.append((best, arc, num, head))
    print("\nC5b  NUMBERED LEDGER ITEMS asserting a state (the path UFF travelled)")
    print("     items scanned: %d      no register match: %d" % (len(items), len(unmatched)))
    unmatched.sort()
    for best, arc, num, head in (unmatched if FULL else unmatched[:12]):
        print("     [%.2f] %-14s #%-4s %s"
              % (best, arc[:14], num, re.sub(r"\s+", " ", head)[:74]))
    if not FULL and len(unmatched) > 12:
        print("     ... and %d more (--full)" % (len(unmatched) - 12))
    if hide:
        hit = [u for u in unmatched if re.search(r"free fall", u[3], re.I)]
        print("\n     SELFTEST (universal-free-fall row hidden from the register): %s"
              % ("PASS - the item is flagged" if hit else "FAIL - not flagged"))

    print("""
  READ THIS AS A SHORTLIST, NOT A COUNT.  Matching is deliberately loose, so a
  low score means "the register may have nothing for this", not "it does not".
  The score is the fraction of the ledger claim's content words found in the
  best-matching register row for the same paper.

  A genuine hit looks like universal free fall did: carried in an arc ledger,
  dated, load-bearing, and simply never entered in the register.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
