# Applying the Rate-Balance Template Inside the Quantum Regime: `D_nd = 1/3`, not `0.3`

*Opened 2026-09-04, running the derivation named in `The_0_6_Problem_Resolution.md` §8. The template closes. It does not land on the Atlas convention.*

---

## Preamble: what this note does NOT claim

1. It does **not** show the Atlas convention is wrong. It shows what the convention *requires*, and leaves the choice open.
2. It does **not** derive `0.6`. It derives **`2/3`**, conditional on one named identification.
3. The identification of `ω_sys` is **interpretive** — the template's own §2.3 says steps 1–4 are interpretive and only step 5 is forced. This note does not pretend otherwise.
4. It raised the question of whether `Paper_097`'s `0.6` and the dictionary's `0.6` are the same object; that was **settled the same day (§5): they are not.** This note therefore bears on the **dictionary** `0.6` only.

---

## 1. The task

`The_0_6_Problem_Resolution.md` reduces `0.6 = 2·D_nd(quantum)` and closes with: *"Full closure requires: **`D_nd(quantum)` derivation.** Apply the rate-balance template inside the quantum regime itself — identify the quantum-regime `γ_dec` and `ω_sys` from first principles, compute `D_nd = γ_dec/(γ_dec + ω_sys)`, and check."* `ED-Dimensional-01-Ext.md` applies the template to cavity-QED, condensed matter, galactic and cosmological regimes — **but not to the quantum regime**, which is the one the dictionary is built on.

## 2. `γ_dec` is forced, not chosen

This is the step that makes the exercise tractable, and it does not appear to have been noticed. The dictionary construction and the rate-balance prescription are two expressions for the same quantity:

$$T_0 = \frac{L_0^2\,D_{\mathrm{nd}}}{D_{\mathrm{phys}}} \quad\Longrightarrow\quad D_{\mathrm{nd}} = T_0\cdot\frac{D_{\mathrm{phys}}}{L_0^2}, \qquad\qquad D_{\mathrm{nd}} = \frac{\gamma_{\mathrm{dec}}}{\gamma_{\mathrm{dec}}+\omega_{\mathrm{sys}}}$$

Equating them gives $T_0 = 1/(\gamma_{\mathrm{dec}}+\omega_{\mathrm{sys}})$ and identifies

$$\boxed{\;\gamma_{\mathrm{dec}} \;=\; \frac{D_{\mathrm{phys}}}{L_0^{2}} \;=\; \frac{\hbar/2m}{(\hbar/mc)^{2}} \;=\; \frac{mc^{2}}{2\hbar} \;=\; \tfrac{1}{2}\,\omega_C\;}$$

where `ω_C = mc²/ħ` is the Compton frequency. **This is algebra on the dictionary, not a physical judgment** — template step 3 is discharged without interpretation. The factor of ½ is inherited directly from `D_phys = ħ/(2m)`.

So **only `ω_sys` remains interpretive**, and the whole question reduces to one identification.

## 3. The natural identification, and what it gives

The template asks for *"the system's natural coherent oscillation rate."* The dictionary's own length scale is `L_0 = ħ/(mc)`, the Compton length; the coherent rate at that scale is `c/L_0`:

$$\omega_{\mathrm{sys}} = \frac{c}{L_0} = \frac{mc^{2}}{\hbar} = \omega_C$$

Then, with `γ_dec = ω_C/2` forced from §2:

$$D_{\mathrm{nd}} = \frac{\omega_C/2}{\omega_C/2 + \omega_C} = \boxed{\tfrac{1}{3}} \qquad\Longrightarrow\qquad 2D_{\mathrm{nd}} = \tfrac{2}{3} \approx 0.667, \qquad \frac{c_0}{c} = \frac{1}{2D_{\mathrm{nd}}} = \tfrac{3}{2}$$

**The template closes in the quantum regime.** It lands on `1/3`, and the dictionary would read `T_0 = \tfrac{2}{3}\,\hbar/(mc^2)` with `c_0 = 1.5c`.

## 4. What the Atlas convention requires instead

Running it backwards from `D_nd = 0.3` (equivalently `T_0 = 0.6\,\hbar/(mc^2)`), with `γ_dec` forced:

$$\omega_{\mathrm{sys}} = \frac{1}{T_0} - \gamma_{\mathrm{dec}} = \tfrac{5}{3}\omega_C - \tfrac{1}{2}\omega_C = \boxed{\tfrac{7}{6}\,\omega_C}$$

**The convention requires the quantum regime's coherent rate to be seven-sixths of the Compton frequency.** No interpretation of `7/6·ω_C` is offered anywhere in the Atlas or the extension, and none is evident.

| | `ω_sys` | `D_nd` | `2·D_nd` | `c_0/c` |
|---|---|---|---|---|
| **Template + Compton** | `ω_C` | **1/3** | **2/3 ≈ 0.667** | **1.5** |
| **Atlas convention** | `7/6·ω_C` | 0.3 | 0.6 | 1.667 |

The two differ by exactly **9/10**.

**The asymmetry is suggestive but is not proof.** `ω_C` is the dictionary's own scale and needs no justification beyond `L_0`; `7/6·ω_C` needs one and has none. And `0.3` is what `1/3` looks like when written to one decimal place. But this note does not claim the convention is a rounding — that is a hypothesis about how a number was chosen, and settling it requires the Atlas's own record of the choice, not this calculation. **The honest statement is that the derivation closes on `1/3` and the convention is unexplained at `0.3`.**

*Nothing downstream breaks either way:* the resolution paper §3.3 already establishes that `c_0 > c` is a regime-boundary marker and not a physical prediction, so `1.5c` is as harmless as `1.667c`.

## 5. A prior question this raises — are there two different `0.6`s?

`Paper_097` describes its `0.6` as *"the transition regime exhibits a characteristic **exponent** ≈ 0.6"* (`P-0p6-Canonical`). The dimensional dictionary's `0.6` is a dimensionless **coefficient** in `T_0 = 0.6\,\hbar/(mc^2)`. **An exponent and a coefficient are different kinds of object**, and the identification of the two is assumed rather than argued anywhere I have found.

This matters because on 2026-09-04 `Paper_097`'s citation was repointed from a memory file to `The_0_6_Problem_Resolution.md` **on the assumption that they are the same `0.6`** (gravity Staleness #47). If they are not, that repoint is wrong and `Paper_097`'s number has no resolution paper at all. **SETTLED 2026-09-04, same day (Staleness #50): they are not the same object.** *“Characteristic exponent ≈ 0.6”* appears **only in `Paper_097`**; its cited memory source contains one exponent (`z = 2`) and never links `0.6` to the transition regime, and the four RG memos contain no `0.6` at all. **Consequences for this note: none adverse.** §§2–4 concern the *dictionary* `0.6`, which is real, well-sourced and exactly what `The_0_6_Problem_Resolution` addresses — so the `D_nd = 1/3` result stands unchanged. What changes is its **scope**: it bears on the dimensional dictionary and **not** on `Paper_097`'s claimed RG exponent, which currently has no located source at all.

## 6. Tier and what is owed

| # | Claim | Tier |
|---|---|---|
| 1 | `γ_dec = D_phys/L_0² = ω_C/2`, forced by the dictionary + template | **D** — algebra |
| 2 | `T_0 = 1/(γ_dec + ω_sys)` | **D** — algebra |
| 3 | `ω_sys = ω_C` (the Compton frequency, `= c/L_0`) | **form-IDENTIFIED (M2)** — interpretive, template step 4 |
| 4 | `D_nd(quantum) = 1/3`; `2D_nd = 2/3`; `c_0 = 1.5c` | **D-via-I** — conditional on 3 |
| 5 | The convention `D_nd = 0.3` requires `ω_sys = 7/6·ω_C` | **D** — algebra |
| 6 | `7/6·ω_C` has no evident interpretation | — observation, not a proof of absence |
| 7 | `Paper_097`'s exponent and the dictionary's coefficient are different objects; the exponent has no located source | **SETTLED** — §5, Staleness #50 |

**Verdict: M2.** The template closes in the quantum regime on one named interpretive identification, and lands 10% from the Atlas convention. **`0.6` is not derived by this note; `2/3` is.**

**Owed.** (a) Justify or replace `ω_sys = ω_C` from the substrate rather than from the dictionary's own length scale — that is the one remaining screw. (b) Recover the Atlas's record of *how* `D_nd = 0.3` was chosen; if it was chosen as a decimal convenience the two results reconcile, and if it was chosen physically then `7/6·ω_C` needs a meaning. ~~(c) Settle §5~~ — **done the same day; see §5.** In its place: locate any source for `Paper_097`'s exponent, or retire `P-0p6-Canonical`.

## 7. Falsification criteria

- **F1.** If the Atlas documents a physical derivation of `D_nd = 0.3` that fixes `ω_sys = 7/6·ω_C`, §3's identification is wrong and this note fails.
- **F2.** If `ω_sys` for the quantum regime is shown from substrate primitives to be anything other than `ω_C`, §3 fails and `D_nd` moves with it.
- **F3 — FIRED AND CONFIRMED 2026-09-04.** `Paper_097`'s `0.6` **is** a distinct object, so this note bears only on the dictionary and not on `Paper_097`. Scope narrowed accordingly; the result itself is unaffected.
