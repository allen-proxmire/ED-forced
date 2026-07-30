# The Crank Safety Protocol

**How Event Density is built, checked, and kept honest — including how AI tools are used and, deliberately, distrusted.**

This note exists because an independent framework for physics faces two fair skepticisms at once. The first is old: outsiders are prone to the crank-trap, the slow slide where a compelling idea stops being tested and starts being defended. The second is new: AI tools are productive but fallible, capable of their own kind of drift, confident restatement, and quiet overclaiming. A reader is right to ask how this work guards against both. This is the answer, stated plainly so it can be audited rather than trusted.

The protocol has three rules. Two are visible in the repository itself; the third is the one that needs explaining.

## 1. Transparency

Everything is open source, from the first philosophical commitment to the last falsifiable prediction. Every commit is tracked. Every derivation is repeatable. Every route tried, every mistake, every retraction, and every staleness flag is recorded next to the results, not scrubbed from them. The failures are part of the record on purpose: a body of work that never shows a wrong turn is not more trustworthy, it is less. If a claim in a paper disagrees with the ledger, that disagreement is itself logged as a staleness item to be reconciled.

## 2. Honest-tiering

An outsider has to be as loud about what is *not* claimed as about what is. Every load-bearing claim in the corpus carries one of 19 explicit rankings, from **Derived** and **Measured** at the strong end, through **Grounded**, **Inherited**, and **Postulated**, down to **Asserted**, **Wall**, and **Open**. The tier is set by the paper's own audit, never inflated to sound stronger. "Form-forced, value-inherited" means the substrate fixes a law's form while the universe supplies its number, and it is labeled as such rather than dressed up as a derivation from nothing. The walls and the open problems are named as walls and open problems.

## 3. Adversarial review — the builder-and-breaker method

The physics is mine. The judgment, the tiering, and the decisions about what stands are mine. AI is used as a tool and, just as importantly, as an adversary, inside a structure rather than as an oracle.

The structure is what one might call **regulated multiplicity**: a single human regulator coordinating several AI models held in *differentiated* roles, rather than asking one model for one answer and accepting it. The human self-model is the anchor. It holds the goals, the epistemic standards, and the long-term commitments, and it is what keeps the ensemble centered instead of drifting toward whatever any one model finds most fluent.

In practice the roles are kept distinct:

- a **generator** proposes derivations and drafts;
- a **critic** attacks the reasoning on its own terms;
- a **breaker** is calibrated to dismantle a finished paper, hunting for the weakest load-bearing step;
- a **synthesizer** reconciles the survivors;
- an **archivist** maintains the tiers, the cross-references, and the staleness flags.

Work moves through a loop, not a single pass. A claim is drafted, cross-checked against a second model rather than trusted from the first, stress-tested by the breaker, assigned a tier by its own audit, and committed to the open repository with its provenance intact. When the breaker wins, the result is retracted or downgraded, and that retraction stays in the record. Several of the corpus's most-cited internal lessons are exactly these catches: reinventions caught, over-claims walked back, negatives held to the same bar as positives.

## What this guarantees, and what it does not

This protocol reduces drift and curbs overclaiming. It does not make any result true, and it is not offered as one. No method of review, human or machine, certifies physics. The real backstops are the ones a skeptic can operate without me: the repository is open and repeatable, so any derivation can be re-run; the tiers are explicit, so no claim can hide its strength; and the predictions are falsifiable, so the framework can be killed by measurement rather than argued with.

That is the point of leading every package with the predictions and not the theory. The builder-and-breaker method is how the work is kept honest on the way in. Falsification is how you keep it honest from the outside. Both are on the table on purpose.
