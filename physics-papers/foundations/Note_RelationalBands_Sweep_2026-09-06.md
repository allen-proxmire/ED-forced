# Note — The relational-bands sweep: the debt was already paid in the source, and the scope is narrower than I flagged

**Date:** 2026-09-06
**Status:** Working note. Pays the propagation debt created by #93 ("the bands are relational") — and finds the premise of that debt was over-broad.
**Anchors:** `primitives/concepts/participation_bandwidth.md` §"Integration over bands", `primitives/concepts/commitment.md`, `primitives/P04_bandwidth.md` (post-Branch 3), `gravity/Paper_GR-I` §2, `gravity/Paper_GR-III` §preamble 5, `soft-matter/Paper_UnifiedP04TransportBudget` §2.

---

## 1. What I expected to find, and what is actually there

#93 recorded that `P-Band-Partition` is discharged only *relative to a choice of system `S`*, therefore **"the bands are relational, not intrinsic"** — and I flagged, as a debt created that night, that every downstream use of "the Adjacency band" now carries an implicit *with respect to which `S`?* while only the transport arc and the card say so.

**The sweep found the opposite. The source concept already writes the bands relationally, with explicit arguments:**

> - `b_int(C)` = bandwidth along C's own update-rule participation
> - `b_adj(C, N)` = bandwidth with adjacency-neighborhood `N`
> - `b_env(C, E)` = bandwidth with environment `E`
> - `b_com(C)` = commitment-reserve bandwidth
>
> — `primitives/concepts/participation_bandwidth.md`

**Every band is a function of the chain; two take a second argument.** So the relational reading is not a constraint Branch 3 imposed. **It is what the source always said, and what the downstream papers dropped in transmission** — the third instance of that exact pattern this session, after the `w(e)` scheme translation (#87) and the "Primitive 10" header fossil.

**The debt was not created on 2026-09-05. It was created whenever `b_adj(C, N)` was first written as `b_adj`.**

## 2. The scope is much narrower than "the bands are relational"

Not all four arguments are free. Sorting them is the useful part:

| band | arguments | is there a **free** parameter? |
|---|---|---|
| `b_int(C)` | the chain alone | **No** |
| `b_com(C)` | the chain alone | **No** |
| `b_adj(C, N)` | chain + neighbourhood | **Only via the cut** — see below |
| `b_env(C, E)` | chain + environment | **Yes** — `E` *is* the system/environment cut |

**`b_int` and `b_com` are cut-independent.** They are properties of a chain and its own rule content, and no choice of environment moves them.

**The free parameter lives at exactly one place: the Adjacency/Environmental boundary.** `Note_BandOverlap_Check_2026-09-05.md` (#84) showed P05-transporting and P11-randomized channels genuinely overlap, and individuation separates them by *which side of `S`'s boundary the far endpoint sits on*. So `N` and `E` are complementary halves of one cut, and **a P05-transporting channel is Adjacency or Environmental according to that cut and nothing else.**

**So #93's "the bands are relational" is right about the partition and over-broad about the bands.** Two of the four are intrinsic to the chain.

## 3. What that clears, and what it leaves

**Cleared — no propagation needed:**

- **`Paper_GR-I` §2, `P-Commitment-Linear`.** `Γ_commit ∼ b_int/reserve` uses `b_int(C)` and `b_com(C)`, **both cut-independent.** The lapse derivation and its falsifier are untouched by the relational reading.
- **`Paper_GR-III` preamble 5**, which already flags that `α = 1` is forced *"modulo a stated band-accounting premise (that the metric band and the commitment-rate-numerator band are the same)"*. **Both bands in that premise are `b_int`/`b_com`-type, so the premise does not acquire a free parameter.** It remains what it already declared itself to be.
- **`Paper_GR-IV`'s "dissipative commitment-reserve sector"** — `b_com`, cut-independent.

**Left, and it is one identification rather than a sweep:**

- **`Paper_UnifiedP04TransportBudget`'s `b_adj^max` is written per-cell with no `N`.** Restoring the argument, the arc is using **`N` = the cell's graph neighbourhood, i.e. `S` = the single cell.** That is a coherent choice and probably the intended one — **and it conditionally answers Path C's open item 5** (*is the transport cell the individuated complex?*): the arc is committed to **`S` = the cell**, whether or not that cell is individuated in individuation's sense. **Whether a single cell can be individuated at all is the real question**, and it is not answered here.

## 4. A sixth collision found on the way

**`b_int` means two different things.**

- **Individuation:** `b_int(S)` = the sum of `w(e)` over edges with **both endpoints inside the complex `S`** — an edge sum over a region.
- **The Internal band:** `b_int(C)` = bandwidth along **`C`'s own update-rule participation** — a channel-class total.

**These may be the same object and may not, and nothing in the corpus states either way.** They coincide if a chain's own-rule channels are exactly the edges internal to it, which is plausible and unargued. **Added to `ADJACENCY_AND_BAND_DISAMBIGUATION.md`; not resolved here.**

## 5. What was actually done

**No caveats were sprayed across the gravity arc**, because the sweep showed they would have been wrong. What changed instead:

1. The **P04 card** now carries the source concept's four band signatures verbatim, so the arguments are visible at the canonical location rather than only in `concepts/`.
2. **`Paper_GR-I`, `Paper_GR-III`** get a one-line note recording that their bands are the cut-independent pair, so a future reader does not re-open this.
3. The **transport arc** gets the `N` restored explicitly, with `S` = the cell named as the identification it is.
4. **`b_int`'s two senses** recorded in the disambiguation.

**The honest summary: I flagged a debt of the wrong shape. The real one is older, narrower, and now stated.**
