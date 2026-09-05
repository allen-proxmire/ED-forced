# CLAUDE.md — Working on the Event Density (ED) corpus

## Where the two repos are

Paths below beginning `../event-density/` and `../ED Primitives/` are **sibling repositories**, not folders of this one: `GitHub/event-density/` is the working repo (arcs, evaluation harnesses, `docs/`, superseded drafts) and `GitHub/ED Primitives/` holds the constitutional registration (`CONSTITUTION.md`, `foundations/forced_theorems_inventory.md`). This repo (`ED Generative`) holds the standalone papers. Written without the `../` these resolve to nothing from here, which is how a session can follow the orientation instruction below and find no orientation docs.

## The premise (do not lose sight of this)

**ED is a research program building toward a unified theory of physics, spanning ~280 papers (234 of them named `Paper_*`; ~415 markdown files in all, once the essays, primitive cards, theorem entries and the **sixteen** arc ledgers are counted — `soft-matter` gained the sixteenth on 2026-09-04, having had none until then). *Recount 2026-09-03 — the old "~150" figure was roughly half the real size*. The papers ARE the theory.** Your job is to **read, digest, and build on that corpus** — not to re-derive it from scratch, and not to reconstruct it from memory summaries. Until proven otherwise, ED is unifying physics; treat the corpus as a serious, coherent body of work you are extending, not a sketch you are second-guessing.

## HARD RULE — read the corpus before you build (non-negotiable)

Before you derive, compute, falsify, or make any claim on a topic:

1. **Search first.** Grep `physics-papers/` (and `../event-density/foundations/`, `../event-density/theory/`) and consult **`PAPERS_INDEX.md`** for existing papers on that exact topic. Assume a paper already exists until you have confirmed it does not.
2. **Read the actual papers, not the memory summaries.** Memory (`MEMORY.md` + topic files) is an **index and pointer set** — it is *not* ground truth. The papers are ground truth. A memory note that says "X is established" is a pointer to a paper you must open, not a substitute for reading it.
3. **Build on what exists. Never reinvent.** Re-deriving a result the corpus already has is not "independent confirmation" — it produces a cruder duplicate that then looks like it conflicts with the corpus. If you find yourself deriving something from scratch, stop and find the paper that already did it.

## HARD RULE — close the loop: write findings back to the authoritative lists (non-negotiable)

A finding that lives only in a working note is a **future drift bug**. The read-first rule fails if the lists you read first are stale. So whenever an arc closes, a postulate is discharged, a theorem's status changes, or a paper lands, **update the authoritative lists in the same session**, before ending the task:

1. **`../event-density/docs/ED_Research_Targets.md`** — the open/closed map. Append the new state to the relevant `#N` item (don't silently overwrite the audit trail; add a dated update).
2. **`../event-density/docs/ED_Road_To_Unification.md`** — the strategic finish-line overlay, if a gate's status moved.
3. **The relevant folder `README.md`** (physics-papers/* or the companion folders) and **`theorems/T*.md`** — if a paper's or theorem's status changed.
4. **`MEMORY.md` + the topic memory file** — update the pointer; correct or delete any note the finding supersedes.

Cross-check for **staleness before you trust a list**: a target doc's wording may predate later work (e.g. #8b read "blocking / three routes fail" on 2026-07-10 while the keystone had actually been reconstructed 2026-07-08 — the finding never got written back). When a memory note and a doc disagree, open the papers and reconcile, then fix whichever is stale. Treat leaving a known-stale status in place as the same class of error as reinventing work.

## When a new result seems to contradict the corpus

**Assume YOU misframed it, not that the corpus is wrong.** Re-read the relevant papers before concluding anything is falsified or missing. A probe you write tests *your model* of ED, not ED itself — before treating a probe as falsifying an ED result, verify it is testing the corpus's actual construction, not a self-made stand-in. Hold negatives (including negatives about ED's own results) to the same bar as positives.

## Orientation at session start (for any substantive work)

Read, in order: `../event-density/docs/NEW_SESSION_ONBOARDING.md`, `PAPERS_INDEX.md`, `../event-density/docs/ED_Research_Targets.md`. Know the standing lines before touching them — e.g. the **gravity line**: `Paper_GR-I..IV` (weak-field Einstein metric; khronometric class; dynamical rule + khronon speed; preferred-frame α₁/α₂), `Paper_KM-I/II` (khronon = MOND/dark-matter deep field; khronon cosmology), and `Papers_025–038` (Newton's G, a₀, Combination Rule, BTFR, MOND field equation, Λ). ED's MOND / dark-matter account already exists and stands (KM-I); do not "rediscover" or "falsify" it without reading it.

## Adversarial review (Claude B / subagents)

Internal-consistency review is **not sufficient** — on 2026-07-09 it validated redundant reinventions because it was never given the corpus. Every reviewer brief MUST include: *"Check this against these specific existing corpus papers [list them]. Is it redundant with, or contradicting, established work? Is it re-deriving something the corpus already has?"* Ground the review against the papers, not just the draft's own logic.

## Why this file exists

On 2026-07-09 a full session was wasted re-deriving `GR-I..IV` / `KM-I..II` from memory summaries, inventing a cruder source-horizon "interference" MOND mechanism, falsifying that self-made strawman, and then wrongly concluding ED's already-published, standing MOND was dead — with a "Claude-B reviewed" stamp making the garbage look validated. The output was *plausible enough* to be hard to recognize as a bad redo of existing work. **Read the corpus first. Build on it. Never reinvent it.**
