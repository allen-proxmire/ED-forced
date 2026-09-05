# -*- coding: utf-8 -*-
"""Safe edit helper. The bug that zeroed two files tonight was

    open(p, "wb").write(s.replace(old, new).encode("utf-8"))

Python evaluates open(p,"wb") FIRST -- which truncates -- and only then the
argument, which raised on an unencodable surrogate. Result: an empty file.

Fix: encode to bytes, verify, and only then touch the file. Also refuses to
write a result shorter than half the original, which is a second net under the
first.
"""
import io, os, sys
sys.stdout.reconfigure(encoding="utf-8")
os.chdir(r"C:\Users\allen\GitHub\ED Generative")


def sub(path, old, new, label):
    s = io.open(path, encoding="utf-8").read()
    n = s.count(old)
    assert n == 1, (label, "expected 1 match, got %d" % n)
    out = s.replace(old, new)
    data = out.encode("utf-8")                     # raises here, before any open
    assert len(data) >= len(s.encode("utf-8")) // 2, (label, "result suspiciously short")
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)                          # atomic
    print("  ok: %s (%d -> %d bytes)" % (label, len(s), len(out)))


# NOTE: no astral-plane characters. The script-K that caused the crash is
# written as the LaTeX \mathcal{K}, which is plain ASCII.
K = r"$\mathcal{K}$"

A = ("**Written, and the useful result is that the three audits that flagged it were not flagging the same "
"thing.** Arm B's `D07a` and the blind run's GPT gap 1 both asked what the aggregation **is**; the blind run's "
"Claude gap 4 asked what it **runs over** (*\u201ca stated measure `\u03bc(R\u2032)`\u201d*). **Reading all three as one item is why "
"it looked like a single missing sentence with wide reach. It is one trivial sentence and one substantive "
"postulate.**")

B = ("**The bridge itself costs nothing.** `Coh(C)`, `Str(C)`, `Grad(C)` are plain sums of their per-channel "
"counterparts over " + K + "`(C,u,t)`, the channels `C` participates in at `(u,t)` \u2014 P02's four-tuple, "
"restricted. **The notation was already in the corpus:** `Paper_001_PreIndividuation` \u00a73.1 writes `b_K^C(u,t)`, "
"`\u03c0_K^C(u,t)`, `K \u2208 " + K + "`. **And the sum is plain rather than weighted, by P04 additivity** \u2014 a quantity "
"built from `b_K` and aggregated non-additively would contradict the primitive it is built from, **so GPT's "
"alternatives (weighted sums, maxima, graph integrals) are excluded rather than merely unchosen.** Written into "
"`Paper_087` \u00a7P12.")

C = ("**All the content is in the second statement, and nobody had flagged it.** What " + K + " *contains* for a "
"chain at radius `R` is a postulate, currently split across two clauses of `Paper_030`: **`P-Bilocal-Count`** "
"(\u00a74.2 \u2014 **named**, tiered, with falsifier `F-BC`) and **the radial `1/R` channel density** (\u00a74.3 \u2014 "
"**unnamed, un-tiered, one clause of justification**). **The unnamed one is what turns an `R`-independent "
"per-channel strain into a logarithm, and therefore what produces `\u221a(a_N a\u2080)` rather than nothing.** Flagged "
"in place.")

D = ("**And it relocates the locality question rather than dissolving it.** A channel in " + K + "`(C,u,t)` is one "
"`C` participates in **at its own locus**; a *bilocal* channel by construction also carries content from a "
"second source region \u2014 **so the far ends are not foreign loci `C` reaches into, they are the second sources "
"feeding channels `C` already touches.** Coherent. **The price:** the radial density becomes a claim about **how "
"many distinct channels one chain participates in at one locus, as a function of its distance from a mass**, "
"and *\u201csubstrate-graph radial-projection geometry\u201d* is a gesture at a derivation rather than one.")

E = ("**Three process notes, all against me, and two are serious.** **(1) A destructive bug in my edit helper "
"zeroed `Paper_087_13Primitives.md`** \u2014 it called `open(p,\"w\")`, which truncates, and *then* raised on "
"encoding. Restored from git intact (49,009 bytes, verified). **(2) I then reproduced the same bug and zeroed "
"this ledger \u2014 and committed and pushed the truncation** (215 lines) before catching it. Restored from "
"`HEAD~1`, verified at 299,176 bytes with all 79 prior items present. **Both files were committed, so nothing "
"was lost; neither would have survived if they had not been.** Helper rewritten to encode first, write to a "
"temp file, `os.replace` atomically, and **refuse any result less than half the original length**. "
"**(3) The census caught a third error on the same turn:** I wrote that naming the new postulate in a paper was "
"AP's call, then wrote the name into `Paper_030` \u2014 count went **171 \u2192 172**, the script flagged it, and the "
"name now appears in the note only. **All three instruments fired on my mistakes tonight, not the corpus's.**")

ITEM = ("80. **`Str(C)` bridge written 2026-09-05 (late) \u2014 it is two statements, only the second carries content, "
"and an unnamed load-bearing postulate sits behind it.** " + A + " " + B + " " + C + " " + D + " " + E + "\n")

sub("physics-papers/gravity/Gravity_TieredClaims_Ledger.md",
    "79. **Aggregation rule investigated 2026-09-05 ", ITEM + "79. **Aggregation rule investigated 2026-09-05 ",
    "gravity ledger item 80")

sub("physics-papers/foundations/Foundations_TieredClaims_Ledger.md",
"11. **`Grad` \u2014 a proposal on the table 2026-09-05",
"12. **The `Str(C)`/`Coh(C)` chain-level bridge \u2014 WRITTEN 2026-09-05 (late), and it splits in two.** "
"**Half one, definitional and free:** they are plain sums of their per-channel counterparts over " + K +
"`(C,u,t)`, the channels `C` participates in at `(u,t)` (P02's four-tuple, restricted; notation already in "
"`Paper_001_PreIndividuation` \u00a73.1). **Plain rather than weighted, by P04 additivity** \u2014 which **excludes** the "
"alternatives an external audit listed rather than merely not choosing among them. Written into `Paper_087` "
"\u00a7P12. **Half two, a postulate, and the real finding:** what " + K + " contains as a function of a chain's "
"distance from a mass \u2014 split in `Paper_030` between the **named** `P-Bilocal-Count` (\u00a74.2) and an **unnamed, "
"un-tiered** radial `1/R` channel density (\u00a74.3) **which is what produces `\u221a(a_N a\u2080)` rather than nothing.** "
"Flagged in place; a name is proposed in the note only, since naming it in a paper increments the census. "
"**Three audits flagged half one \u2014 two asking what the aggregation *is*, one what it *runs over* \u2014 and reading "
"them as one item is why this looked like a single sentence with wide reach.** "
"`foundations/Note_StrC_Bridge_2026-09-05.md`; gravity ledger Staleness #80.\n\n"
"11. **`Grad` \u2014 a proposal on the table 2026-09-05",
"foundations #12")
print("done")
