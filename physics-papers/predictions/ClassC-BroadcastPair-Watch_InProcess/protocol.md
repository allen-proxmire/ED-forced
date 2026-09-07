# Class-C Broadcast-Pair Watch — Operational Protocol

**Status.** Monitoring protocol (no facility time, no collaboration, no new derivation). Tracks the two live public data streams that carry the re-scoped weapon #4 (prediction 4.10) after the α_topological = 0 settlement. Runs today; the "experiment" is other groups' ongoing engineering campaigns.

**What this document does.** Turns `Paper_058b_PlateauDomain_AlphaTopological` §5 (the discriminator) into a standing watch with pre-registered pass/fail conditions, converted under the `Paper_ProxyConversionDoctrine` §3.1 content rule so that when new numbers land we already know what they mean. It does **not** modify any derivation.

**Source papers (locked).**
- `Paper_058_ClassC_Plateau` — the plateau mechanism (P-Corr-Budget, per-locus, finite).
- `Paper_058b_PlateauDomain_AlphaTopological` — α_topological = 0; plateau binds for broadcast-type redundancy, not code distance; §5 discriminator.
- `Paper_QuantumDarwinism_RecordBandwidth` — the cat-width ceiling leg + the certified-content floor arithmetic.
- `Paper_V5UnifiedBudget` — the fixed ratios `1 : 1 : 0.88 : r_QD` tying the two legs to each other and to monogamy/Page.
- `Paper_ProxyConversionDoctrine` §3.1 — the pre-registered content rule (per-locus certified live pairwise correlation, certification-discounted; qubit-count is not a content rule).

---

## 1. The prediction in one paragraph

The V5 cross-chain correlation budget `W_max` is finite and per-locus. In **broadcast-type** redundancy — repetition codes, GHZ/cat-type encodings, any scheme where redundant channels hold direct live pairwise correlation with a common locus — growing the redundancy loads a locus linearly, so error suppression **plateaus** at `Γ_plateau > 0` once the locus saturates (058), and coherent branching width hits a **ceiling** `N_max ~ W_max/w_min` (QD paper). These are the **same budget** seen two ways, so their content values must be commensurate (fixed ratio, `Paper_V5UnifiedBudget`). In **topological** encodings the mechanism does not bind (α_topological = 0), so ED predicts *no* substrate plateau in surface-code distance. The watch: track (Leg 1) the persistence of the repetition-code error floor and (Leg 2) the largest certified cat-state width, both converted to per-locus content, and check them against each other and against the null (mundane, engineering-limited) hypothesis.

## 2. Pre-registered watch parameters

| Quantity | Current public value (2026-07) | Converted content (doctrine §3.1) | Source |
|:---|:---|:---|:---|
| Repetition-code floor onset | deviation from exponential above `d ≈ 15`; apparent logical floor `~10⁻¹⁰`/cycle | plateau **shape** present in a broadcast encoding | Google, Nature 638 / arXiv:2408.13687 |
| Largest certified GHZ width | `N = 120`, GME fidelity `F = 0.56` | guaranteed `≈ 1` bit/locus (adversarial junk); `≈ 28` (benign junk) | IBM, arXiv:2510.09520 |
| Surface-code suppression | `Λ ≈ 2` clean through `d = 7`, no plateau | consistent with **no** topological plateau (predicted) | Google Willow, arXiv:2408.13687 |
| Budget ratio (legs to each other) | `1 : 1 : 0.88 : r_QD` | the two legs' content must be commensurate (O(1)) | `Paper_V5UnifiedBudget` |

**These are pre-registered before the deciding data exists.** The deciding data is each group's *next* release (Google's burst-mitigation results; the next-larger certified cat state). Registering the content rule now is the point of the doctrine: the floor's *meaning* is fixed before the number arrives, so a post-hoc conversion cannot be chosen to force either verdict.

## 3. The two legs

### Leg 1 — Repetition-code floor persistence (Google, and any repetition-code group)

The observable is whether the ~10⁻¹⁰ logical-error floor in long repetition-code runs **survives mitigation**. Google attributes it to rare correlated bursts (cosmic rays, TLS transients) and is pursuing shielding + burst-detection. Two hypotheses separate cleanly:

- **Null (mundane):** the floor is engineered down by shielding/post-selection; residual floors on different platforms sit at *uncorrelated* heights set by each lab's local burst environment.
- **ED substrate floor:** a residual floor survives mitigation, and its converted per-locus content is *consistent across broadcast-type platforms* (058 §5.2) and *commensurate with Leg 2*.

**What to watch for (triggers a run of §4):** any new Google/other repetition-code paper reporting (a) floor behavior after shielding or burst-rejection, (b) floor vs code distance beyond `d = 29`, or (c) a second platform's repetition-code floor (for the cross-platform-consistency test).

### Leg 2 — Certified cat-state width ceiling (IBM, Quantinuum, and any GHZ/cat group)

The observable is the largest **certified-GME** GHZ/cat width and its fidelity. Each such record raises the floor under `W_max/w_min` when converted under §3.1 (per-locus content = certified pairwise pointer correlation, discounted by the certification bound — *not* the qubit count). ED predicts widths cannot grow without bound; standard physics predicts only an engineering-noise limit with no fundamental wall.

**What to watch for:** any new certified-GME GHZ/cat-state record (N and F), especially one where fidelity is high enough that the certified content is a strong floor (F well above the GME threshold, not barely above it).

## 4. Analysis pipeline (per new data point)

```
New public result (repetition-floor OR certified cat width)
    │
    ▼
Classify leg (1 or 2) and encoding type (broadcast / topological / hybrid)
    │  topological → log as consistency check for "no plateau"; do NOT feed the floor
    ▼
Convert to per-locus content via doctrine §3.1
    │  Leg 1: floor height → residual per-locus uncorrelated-error content
    │  Leg 2: (N, F) → guaranteed per-locus pairwise content (adversarial + benign junk bounds)
    ▼
Update the running floor/ceiling on W_max/w_min (content units)
    │
    ▼
Commensurability check: are Leg-1 and Leg-2 converted contents within the fixed-ratio O(1) window?
    │
    ▼
Null-vs-ED test (Leg 1 only): did the floor survive mitigation? is it cross-platform-consistent?
    │
    ▼
Record verdict row + date; update decision table §5
```

No new script is needed for the intake: the QD-paper certification-bound arithmetic (§3.2 worked example) is the Leg-2 converter, and the Leg-1 converter is a per-locus residual-error content estimate. A small helper (`classc_watch_convert.py`) can be written when the first post-mitigation floor lands; until then the conversions are done by hand per the worked example. *(working-repo artifact: lives under `event-density`/`ed-lab`, not in this repo)* *(working-repo artifact — no longer in this repo; lives under `event-density`/`ed-lab`)*

## 5. Decision table (pre-registered)

| Outcome | Leg 1 (floor) | Leg 2 (width) | Commensurate? | Interpretation |
|:---|:---|:---|:---|:---|
| **ED-positive** | residual floor survives mitigation, cross-platform-consistent content | ceiling appears at converted content near Leg-1 | yes | Both legs of the re-scoped weapon #4 fire; a substrate budget is showing in two independent QC data streams at a fixed ratio. Highest-impact QC outcome in the program. Write it up. |
| **Partial (Leg 1)** | floor survives, consistent | no width ceiling reached yet (widths still climbing below the floor-implied content) | n/a yet | Consistent with ED; Leg 2 not yet at the wall. Keep watching cat records. |
| **Partial (Leg 2)** | floor mitigated away / not yet tested | width ceiling appears at consistent content across platforms | n/a yet | Consistent with ED; Leg 1 inconclusive. Keep watching floors. |
| **Null wins** | floor engineered to zero, OR residual floors cross-platform-*inconsistent* | widths keep climbing with no wall as noise improves | — | Mundane explanation holds; the re-scoped weapon #4 does not fire. Narrow or retire prediction 4.10; report honestly. This is F-058b-1 / F-058b-3. |
| **Topological plateau** | — | surface-code distance plateaus at content matching B_cross,max | — | Would contradict α_topological = 0 (F-058b-2): rescues the original code-distance leg but overturns the settlement. Flag loudly. |
| **Undecidable** | data too noisy / mitigation ambiguous | fidelity too low to floor content | — | Wait for cleaner release. |

## 6. Falsification criteria (inherited, restated for the watch)

- **F-058b-1:** a pure broadcast-type platform showing continued exponential suppression to arbitrarily high redundancy *after* burst mitigation → the re-scoped plateau is false.
- **F-058b-3:** post-mitigation floors at *inconsistent* converted content across broadcast platforms → the cross-platform-consistency leg (058 §5.2) is false.
- **F-QD-1:** a confirmed plateau at content `X` in one leg together with the other leg reaching content `≫ X` with no wall → the single-budget commensurability (P-QD-LiveWeight + ρ_loc = 1) is false.
- **F-058b-2:** a topological code-distance plateau at `B_cross,max` content → α_topological = 0 is false (and the original code-distance leg is rescued).

## 7. Cadence and logging

- **Cadence:** event-driven, not scheduled. Trigger a §4 run whenever a relevant paper appears (major QEC / large-GHZ releases from Google Quantum AI, IBM, Quantinuum, and the surface/repetition-code literature). A light quarterly scan of the QEC arXiv listings is sufficient between major releases.
- **Log:** append each data point + conversion + verdict row to `watch_log.md` in this folder (create on first entry), dated, with the source DOI/arXiv id and the converted content shown. *(working-repo artifact: lives under `event-density`/`ed-lab`, not in this repo)* *(working-repo artifact — no longer in this repo; lives under `event-density`/`ed-lab`)*
- **Escalation:** an ED-positive or Null-wins row is a report-v2 event → write an addendum entry (event-density `REPORT_ADDENDA.md`) and, if positive, a results paper.

## 8. Why this runs with no cost or permission

The deciding experiments are already funded and running inside Google, IBM, and Quantinuum for their own reasons. This protocol contributes the *interpretation*: it fixes, in advance, what each of their next numbers means for ED under a pre-registered content rule, so that neither a hopeful nor a dismissive reading can be retrofitted after the fact. That pre-registration is the entire scientific content of the watch; the data collection is done by others.

---

## 9. References

- `Paper_058_ClassC_Plateau`, `Paper_058b_PlateauDomain_AlphaTopological`, `Paper_QuantumDarwinism_RecordBandwidth`, `Paper_V5UnifiedBudget`, `Paper_ProxyConversionDoctrine` (all `physics-papers/`).
- Google Quantum AI. *Quantum error correction below the surface code threshold.* Nature **638**, 920–926 (2025). arXiv:[2408.13687](https://arxiv.org/abs/2408.13687). (Surface-code Λ≈2 through d=7; repetition-code d≤29 with the ~10⁻¹⁰ correlated-burst floor above d≈15.)
- IBM. *Largest certified-GME GHZ state (120 qubits, F = 0.56).* arXiv:[2510.09520](https://arxiv.org/abs/2510.09520).
- GHZ record lineage: 60-qubit scalable protocol, *Nat. Commun.* (2024); 32-qubit trapped-ion GHZ (Quantinuum).

*This protocol mirrors the house `_InProcess/` structure. It is a monitoring protocol: its only maintenance is a periodic QEC-literature scan and a §4 conversion when a relevant number lands. The re-scoped weapon #4 (prediction 4.10) is decided by others' engineering campaigns; this doc makes the decision rule pre-registered and honest.*
