# Primitives Directory

**Date:** 2026-05-14
**Purpose:** Per-primitive reference for the 13 canonical primitives of the ED Generative System, plus underlying ontological-concept treatments.

**State.** These are the **postulated axioms** of the whole program — P01–P13 are *not derived*; every "Derived" or "Grounded" result anywhere in the corpus is conditional on them. This folder is the granular per-primitive breakdown *beneath* the canonical position paper (`../position-paper/paper_ED_Framework_13_Primitive_Generative_System.md`, = `../physics-papers/foundations/Paper_087_13Primitives.md`, same axioms). The load-bearing audit (which primitive does real work where) is `PRIMITIVE_LOAD_BEARING_AUDIT.md` (= foundations `Paper_088`).

> **Cross-reference hazard.** The `concepts/` files carry their **own independent 01–13 numbering that does NOT match the canonical P-numbers** (e.g. concept "Primitive 05" = Event Density, not P05 polarity-transport). Always resolve primitive citations by **P-number via the top-level `Pnn_*.md` cards**, never by a concept file's internal number. This is the same non-canonical-vintage confusion that produced real errors elsewhere (see the T14 downgrade); cite canonical, not archived/concept enumerations.

---

## Structure

The directory is organized in two tiers:

### Tier 1 — Canonical primitives (top-level files, `P01–P13`)

The 13 canonical primitives as enumerated in `position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1. Each canonical primitive has its own file:

| File | Canonical primitive |
|---|---|
| [`P01_event_density_layer.md`](P01_event_density_layer.md) | Event-density layer existence |
| [`P02_participation.md`](P02_participation.md) | Participation as primitive relation |
| [`P03_channel_locus_indexing.md`](P03_channel_locus_indexing.md) | Channel + locus indexing; spatial homogeneity |
| [`P04_bandwidth.md`](P04_bandwidth.md) | Bandwidth (non-negative additive scalar, four-band partition) |
| [`P05_polarity_transport.md`](P05_polarity_transport.md) | Polarity-transport between adjacent loci |
| [`P06_spatial_dimension.md`](P06_spatial_dimension.md) | Spatial dimension $D = 3+1$ |
| [`P07_channel_structure.md`](P07_channel_structure.md) | Channel structure as ontological primitive |
| [`P08_substrate_scale.md`](P08_substrate_scale.md) | Substrate scale $\ell_{\mathrm{ED}}$ |
| [`P09_u1_polarity.md`](P09_u1_polarity.md) | $U(1)$-valued polarity |
| [`P10_rule_type.md`](P10_rule_type.md) | Rule-type primitive |
| [`P11_commitment.md`](P11_commitment.md) | Commitment with environmental phase-randomization, irreversible |
| [`P12_stability_landscape.md`](P12_stability_landscape.md) | Stability landscape |
| [`P13_time_homogeneity.md`](P13_time_homogeneity.md) | Time homogeneity; primitive event-discreteness |

These are the **citation targets** for downstream papers. When a Forcing Paper writes "by P03..." or "P11 supplies...", it refers to the canonical files in this tier.

### Tier 2 — Ontological-concept treatments (`concepts/` subdirectory)

The `concepts/` subdirectory contains 13 process-level treatments of the **underlying ontological concepts** that the canonical primitives organize:

| Concept file | Closest canonical primitive(s) |
|---|---|
| [`concepts/micro_event.md`](concepts/micro_event.md) | P01 (atomic unit underlying the event-density layer) |
| [`concepts/chain.md`](concepts/chain.md) | P02 (chains are the things that participate; not themselves a canonical primitive — derived composite structures) |
| [`concepts/participation.md`](concepts/participation.md) | P02 |
| [`concepts/participation_bandwidth.md`](concepts/participation_bandwidth.md) | P04 |
| [`concepts/event_density.md`](concepts/event_density.md) | P01 (the namesake scalar count-measure) |
| [`concepts/ed_gradient.md`](concepts/ed_gradient.md) | P12 (gradient component of stability landscape) |
| [`concepts/channel.md`](concepts/channel.md) | P03 + P07 |
| [`concepts/multiplicity.md`](concepts/multiplicity.md) | P10 / P03 (channel count, rule-type count) |
| [`concepts/tension_polarity.md`](concepts/tension_polarity.md) | P09 |
| [`concepts/individuation.md`](concepts/individuation.md) | P11 (threshold dynamics of commitment) |
| [`concepts/commitment.md`](concepts/commitment.md) | P11 |
| [`concepts/thickening.md`](concepts/thickening.md) | P08 (substrate-scale accumulation into classical regime) |
| [`concepts/relational_timing.md`](concepts/relational_timing.md) | P13 |

The concept files are **substantive ontological treatments at the process level** — micro-events, chains, what individuation means, what thickening produces. They were written before the canonical P01–P13 consolidation and develop the constituent concepts that the canonical primitives organize.

Note that the mapping is **not 1-to-1**:
- Some concepts (chain, individuation) are *derived structures*, not canonical primitives.
- Some concept files (micro_event, event_density) jointly contribute to P01.
- Some canonical primitives (P05 polarity-transport, P06 spatial dimension) have no concept-file counterpart; they were declared at primitive level only.

The two-tier structure preserves both views: the axiomatic primitive layer (citation targets) and the process-level concept layer (definitional depth).

---

## Per-primitive load-bearing audit

For the audit of which primitives are load-bearing across the corpus (per-primitive trace of which Forcing Papers invoke each P01–P13 as a §3.0 input, and what each is structurally necessary for), see [`PRIMITIVE_LOAD_BEARING_AUDIT.md`](PRIMITIVE_LOAD_BEARING_AUDIT.md).

---

## Citation convention for downstream papers

- Cite **canonical primitives by P-number** (e.g., "by P03...", "P11 supplies...") for any load-bearing claim.
- The position paper (`position-paper/paper_ED_Framework_13_Primitive_Generative_System.md` §1) is the single source of truth for the canonical enumeration.
- The per-primitive files at this directory's top level (`P01_*.md` through `P13_*.md`) are reference cards summarizing each primitive's role and load-bearing function.
- The `concepts/` files are for definitional depth on the underlying ontological concepts; cite them only when the process-level treatment is the load-bearing content.

---

**End of README.**

---

## Also in this folder

*Files present here that this guide had not listed. Added 2026-09-03 by a pointer-layer coverage sweep.*

- **[Contrast](Contrast_Minimality.md)**
- **[Emergent Decoupling Surfaces](Emergent_Decoupling_Surfaces.md)**
- **[Primitives](P1-13_Primitives_Ledger.md)**
