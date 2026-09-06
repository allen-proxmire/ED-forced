# -*- coding: utf-8 -*-
"""C2, rebuilt: which spreadsheet rows have been overtaken by a later ledger finding?

WHY A REWRITE.  The C2 inside `_check_tiered_claims_xlsx.py` reported 207 of 404
rows stale, which is too many to act on and turned out to be mostly noise.  It
had three defects, and they pulled in both directions:

  OVER-COUNTING (1)  It substring-matched the sheet's free-text Paper column
      against raw ledger prose.  "016" matches inside "2016", "1016", "Paper_016b"
      and any stray number.  Short numeric names are the majority of the column.

  OVER-COUNTING (2)  A row with no date at all was compared against `None` and
      every ledger item counted as later.  274 of 404 rows carry no date, so
      most of the 207 were simply undated, not overtaken.

  UNDER-COUNTING (3) It read ONLY `gravity/Gravity_TieredClaims_Ledger.md`.  A
      cosmology row overtaken by the cosmology ledger was invisible.  Row 45's
      a0 correction was caught only because it happened to be cross-filed into
      gravity.

WHAT THIS DOES INSTEAD.

  * Reads ALL eleven arc ledgers.
  * Matches paper names on a word boundary, and for bare numerics requires the
    name to appear as a paper reference (`Paper_029`, `029 §3`, backticked, or
    followed by a section mark) rather than as a loose digit run.
  * Separates three verdicts instead of one:
        OVERTAKEN  a later item mentions this paper AND carries a change word
                   (re-tier, corrected, narrowed, superseded, withdrawn, STALE,
                   supersedes, now reads, was ...)  -- these are actionable.
        LATER      a later item mentions the paper but says nothing about a
                   change -- informational only, usually a citation.
        UNDATED    the row has no date, so staleness cannot be assessed.

Only OVERTAKEN is a work list.  The other two are reported as counts.

Run: python "internal notes/_check_c2_staleness.py"
     python "internal notes/_check_c2_staleness.py" --full
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

XLSX = next((a for a in sys.argv[1:] if a.endswith(".xlsx")),
            "ED_ItemizedTheory_TieredClaims_v2.xlsx")
FULL = "--full" in sys.argv
DATE = re.compile(r"20\d\d-\d\d-\d\d")
WINDOW = 400   # chars either side of a paper reference

# Words that mean the item CHANGED something, not merely mentioned it.
CHANGE = re.compile(
    r"\bre-?tier(?:ed|s|ing)?\b|\bcorrect(?:ed|ion|s)\b|\bnarrow(?:ed|s|ing)\b"
    r"|\bsupersed(?:ed|es)\b|\bwithdraw(?:n|s)\b|\bSTALE\b|\bstaleness\b"
    r"|\bretract(?:ed|ion)\b|\bdemot(?:ed|ion)\b|\bpromot(?:ed|ion)\b"
    r"|\bwas\s+(?:D|A|I|P|Derived|Grounded|form D|current)\b|\bno longer\b"
    r"|\bdoes not follow\b|\bfails? to\b|\boverstat(?:ed|ement)\b", re.I)


def ledgers():
    out = []
    for dp, _dn, fn in os.walk("physics-papers"):
        for f in fn:
            if f.endswith("_TieredClaims_Ledger.md"):
                out.append(os.path.join(dp, f))
    return sorted(out)


def items():
    """Every dated ledger entry, as (date, arc, number, text)."""
    got = []
    for path in ledgers():
        arc = os.path.basename(os.path.dirname(path))
        text = io.open(path, encoding="utf-8").read()
        # split on numbered items where they exist, else on headings
        blocks = re.split(r"\n(?=\d+\. \*\*)", text)
        if len(blocks) < 3:
            blocks = re.split(r"\n(?=#{2,4} )", text)
        for b in blocks:
            ds = DATE.findall(b)
            if not ds:
                continue
            num = (re.match(r"(\d+)\.", b) or [None, "-"])[1]
            got.append((max(ds), arc, num, b))
    return got


def matcher(name):
    """A regex that finds this paper referenced, not merely its digits."""
    n = name.strip()
    if not n or len(n) < 2:
        return None
    if re.fullmatch(r"[0-9]+(?:[._][0-9]+)?[a-z]?", n):
        # bare numeric: demand a real paper reference around it
        d = re.escape(n)
        return re.compile(r"(?:Paper[_ ]?%s|`%s`|\b%s\s*(?:§|§))" % (d, d, d))
    return re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(n))


def main():
    import openpyxl
    ws = openpyxl.load_workbook(XLSX, read_only=True)["Ledger w Claims"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = [str(c) if c else "" for c in rows[0]]
    ix = {h: n for n, h in enumerate(hdr) if h}
    its = items()

    overtaken, later, undated, nopaper = [], 0, [], 0
    for n, v in enumerate(rows[1:], start=2):
        if not any(v):
            continue
        paper = str(v[ix["Paper"]] or "")
        if not paper:
            nopaper += 1
            continue
        blob = " ".join(str(c) for c in v if c)
        ds = DATE.findall(blob)
        if not ds:
            undated.append((n, paper))
            continue
        rowdate = max(ds)
        pat = matcher(paper)
        if pat is None:
            continue
        hits = [it for it in its if it[0] > rowdate and pat.search(it[3])]
        if not hits:
            continue
        # PROXIMITY. Mentioning a paper and containing a change word somewhere
        # are not the same thing. Paper_087 is cited in 33 later items; almost
        # none of them change any particular row. So the change word must sit
        # within WINDOW characters of an actual reference to this paper.
        changed = []
        for it in hits:
            for m in pat.finditer(it[3]):
                lo = max(0, m.start() - WINDOW)
                if CHANGE.search(it[3][lo:m.end() + WINDOW]):
                    changed.append(it)
                    break
        if changed:
            changed.sort(key=lambda t: t[0])
            overtaken.append((n, paper, rowdate, changed[-1], len(changed)))
        else:
            later += 1

    print("C2 REBUILT - rows overtaken by a later ledger finding")
    print("=" * 78)
    print("  workbook: %s" % XLSX)
    print("  arc ledgers read: %d      dated ledger items: %d\n"
          % (len(ledgers()), len(its)))
    print("  OVERTAKEN (actionable)                    : %d" % len(overtaken))
    print("  LATER mention, no change word (info only) : %d" % later)
    print("  UNDATED, staleness not assessable         : %d" % len(undated))
    print("  no Paper value                            : %d\n" % nopaper)

    show = overtaken if FULL else overtaken[:20]
    for n, paper, rd, it, cnt in show:
        print("  row %-4d %-22s row %s  <  %s #%s (%s)%s"
              % (n, paper[:22], rd, it[1], it[2], it[0],
                 "  [%d items]" % cnt if cnt > 1 else ""))
    if not FULL and len(overtaken) > 20:
        print("  ... and %d more (--full)" % (len(overtaken) - 20))

    print("""
  OVERTAKEN is the work list: a later ledger item mentions this row's paper AND
  says something changed.  It is still a FLAG, not a verdict -- the change may
  concern a different claim in the same paper, which is exactly how four of the
  C4 flags turned out to be false.  Read before re-dating.

  UNDATED is a separate problem with a separate fix: those rows cannot be
  checked for staleness at all until they carry a date.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
