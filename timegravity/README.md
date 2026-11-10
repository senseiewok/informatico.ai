# Time & Gravity (`T.00`–`T.12`) · a track where the open problem is the subject

**Live:** [https://informatico.ai/timegravity/](https://informatico.ai/timegravity/) · **Español (es-MX):** [https://informatico.ai/es-mx/timegravity/](https://informatico.ai/es-mx/timegravity/)

> **Fixed boundary, printed on every T page and asserted by the lint:** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.

A sibling track beside *Tech & Tools · The Toolbox* (`X.01`–`X.06`), outside the Folio count of 48, and featured at the top of the Physics section and Home cover. The hub states a common intuition once, in the third person, as a question, and carries no claims. Each later page ships six things, and the build refuses a page that lacks one:

1. **One instrument**, hand-written SVG, reduced-motion and keyboard paths, a static plate fallback; the knockout is the argument.
2. **A standard-library verifier** that recomputes the page's central number and fails on a planted defect.
3. **A grounding ledger and a ledger-driven label lint** (`timegravity/ledger.json`, `tools/check_timegravity_labels.py`). `DERIVED` claims render visibly as `DERIVED (NOT MEASURED)` (`DERIVADO (NO MEDIDO)` in `es-MX`) with a localized hover tooltip naming their `MEASURED` parent row (`data-tg-parent`).
4. **A `SKILL.md` companion** (`skills/timegravity/<slug>/SKILL.md`).
5. **A 5-pace distillation ladder and es-MX** in the same commit.
6. **An AI-contribution line** naming any AI system that contributed to a cited result and the human who checked it.

## All 13 shipped pages (in pedagogical reading order, `T.00` → `T.02` → `T.01` → … → `T.12`)

*Note: Rows below follow the fixed pedagogical reading sequence (`TRACK_MAP`), where Step 2 (`T.02`, universal spacetime rate) precedes Step 3 (`T.01`, geodesic fall in a clock-rate gradient).*

| Step · Code | Page | Instrument and knockout | Verifier's central number · planted defect | Labels on the page |
| --- | --- | --- | --- | --- |
| `1 · T.00` | [The hub](https://informatico.ai/timegravity/) | A worldline with a movable "now" marker: a picture of the question, not a result | none; the lint asserts zero claim spans | none |
| `2 · T.02` | [Everyone Moves at One Rate](https://informatico.ai/timegravity/t02/) | Light clock stretched by γ; GPS clock budget from GM, a and c; knockout leaves the satellite clock uncorrected (≈11.5 km/day pseudorange error) | `+45.7 − 7.2 = +38.5 µs/day`, recomputed two ways within `0.3 µs/day`, with a GUM-style uncertainty budget · sign flip | MEASURED, DERIVED, BOUND, OPEN |
| `3 · T.01` | [Gravity as a Slope in the Rate of Time](https://informatico.ai/timegravity/t01/) | 1+1 geodesic where only `g_tt` varies with height; the body falls at g with no force term; knockout flattens the gradient and nothing falls | `a = −9.80665 m/s²` within `1e-6` relative · sign flip makes the body rise | MEASURED, SINGLE RESULT, DERIVED, OPEN |
| `4 · T.03` | [What Sets the Slope](https://informatico.ai/timegravity/t03/) | ∇²Φ = 4πGρ solved on a radial grid; mass slider reshapes the clock-rate map; two compositions fall together; knockout removes the source | grid recovers `−GM/r` (≈1e-6) and `Φ(0) = −3GM/2R`; separation `< 1e-12 m` · planted η = 10⁻³ separates them by 4.9 mm | MEASURED, SINGLE RESULT, DERIVED, OPEN |
| `5 · T.04` | [A Clock in Two Places](https://informatico.ai/timegravity/t04/) | Zych–Brukner clock interferometer: visibility against height difference and clock frequency; knockout switches gravity off | `V = |cos(ω Δτ/2)|` recomputed two ways; Sr clock 1 m × 1 s keeps V = 0.989; first zero at 10.7 m·s · a clock that never decoheres | DERIVED, SINGLE RESULT, PROPOSED, OPEN |
| `6 · T.05` | [Does Gravity Entangle, and Would That Settle It?](https://informatico.ai/timegravity/t05/) | Bose–Marletto–Vedral four-branch phases; entanglement against hold time for three channels at equal weight (quantum, classical LOCC, disputed non-LOCC); Eöt-Wash 2020 Table 11.4 recast (`σ ≤ 33 µm` at 95 %, DERIVED); Table T.05-H gas & photon decoherence ceilings; knockout switches the channel | `Δφ = 0.314 rad` (`m = 10⁻¹⁴ kg`, `d = 200 µm`, `Δx = 250 µm`, `t = 2.5 s`), concurrence `0.156`, negativity `0.078`, full entanglement at `25.0 s`; 5 verifiers covering channels, dispute kernel, Fourier–Bessel smeared ISL, recast, and decoherence ceilings | MEASURED, DERIVED, SINGLE RESULT, PROPOSED, OPEN |
| `7 · T.06` | [Does Gravity Collapse the Wave?](https://informatico.ai/timegravity/t06/) | Diósi–Penrose collapse time `τ = ħ/E_G` for two displaced spheres; `R0` exclusion bar with Gran Sasso and XENONnT bounds + σ ladder across 29 orders of magnitude; knockout switches gravity off | `R0 > 0.545 × 10⁻¹⁰ m` recomputed from 576 vs 506 counts (paper `0.54`); parameter-free value ⇒ `1.4 × 10⁵` photons, excluded · bound drawn on the wrong side / small-displacement series dropped | DERIVED, BOUND, SINGLE RESULT, PROPOSED, OPEN |
| `8 · T.07` | [The Equation with No Time](https://informatico.ai/timegravity/t07/) | Page–Wootters history state on a 16-level clock and a qubit; knockout reads the clock in a different basis and time disappears | `‖Ĥ|Ψ⟩⟩‖ ≈ 1e-15`, `P(+x|tₙ) = cos²(εtₙ/2)` within `1e-10`, Jacobi kernel holds the state · a clock whose spectrum ignores the constraint | MEASURED, DERIVED, SINGLE RESULT, PROPOSED, OPEN |
| `9 · T.08` | [A Horizon Has a Temperature](https://informatico.ai/timegravity/t08/) | Rindler causal horizon and accelerated worldline beside the Planck thermal occupation spectrum of the right wedge; knockout severs cross-horizon entanglement (`|0_L⟩ ⊗ |0_R⟩`) | Jacobi eigenvalues of `ρ_R = Tr_L(|Ψ⟩⟨Ψ|)` match truncated Gibbs weights within `1e-12`; `d(Mc²)/(k_B T_H) = d(A / 4ℓ_P²)` within `1e-12` · factorized vacuum state with zero entropy | MEASURED, DERIVED, SINGLE RESULT, OPEN |
| `10 · T.09` | [A Horizon Rings Like a Bell](https://informatico.ai/timegravity/t09/) | Kerr ringdown damped sinusoid for `(2,2,0)` and `(2,2,1)` beside the `(f, τ)` spin trajectory; knockout corrupts the Kerr radical `√(1 − χ²) → √(1 + χ²)` | Leaver continued-fraction solver reproduces `(2,2,0)` and `(2,2,1)` benchmarks across `χ ∈ [0, 0.90]` within `1e-6` and Smarr's identity `Mc² = κA/(4πG) + 2Ω_H J` within `1e-12` · corrupted radical breaks Smarr and shifts `Mω_220` | MEASURED, DERIVED, SINGLE RESULT, PROPOSED, OPEN |
| `11 · T.10` | [Page's Counting Argument](https://informatico.ai/timegravity/t10/) | Hawking's line against Page's curve; Haar toy on 10 qubits with a pure-Python eigensolver; knockout removes unitarity | toy within `0.03 nats` of Page's formula, peak `2.97 nats` at 5 qubits, final `0.69` · a non-unitary toy that never turns over | MEASURED, DERIVED, SINGLE RESULT, PROPOSED, OPEN |
| `12 · T.11` | [What Selects the World a Clock Sees?](https://informatico.ai/timegravity/t11/) | 1+6-qubit pure-dephasing pointer-state & Quantum Darwinism plateau beside Joos–Zeh photon-bath localization; knockout uncouples the bath (`θ = 0`, `ε = 1 → Λ_EM = 0`) | statevector partial traces match Zurek's closed form `I(S:E_k) = h₂(γ^N) + h₂(γ^k) − h₂(γ^{N−k})` within `1e-12` nats (`0.998 bits` at `k = 2` of `6`); long-wavelength Rayleigh `R⁶T⁹` scaling exact · scrambled pointer basis (`Z_S → X_S`) collapses the plateau | MEASURED, DERIVED, BOUND, PROPOSED, OPEN |
| `13 · T.12` | [Two Clocks That Only Meet in Gravity](https://informatico.ai/timegravity/t12/) | Dark-matter flyby proper-time step across two optical clocks (`Λ_EM = 0`, `G > 0`); knockout sets equal impact parameters `b₂ = b₁` (`Δτ = 0`) | Planck 2018 `Ω_c / Ω_b = 5.364 ± 0.065` (`84.3 %` of non-relativistic gravitating matter); analytic `Δτ(T)` vs Gauss–Legendre quadrature within `1e-11` and impulse identity `+c² ∂Δτ_∞/∂b₁ = 2GM/(b₁v₀)` within `1e-9` · dropping `G_dark = 0` or halving arsinh breaks both | MEASURED, DERIVED, BOUND, PROPOSED, OPEN |

Reading order (`T.00` → `T.02` → `T.01` → `T.03` → `T.04` → `T.05` → `T.06` → `T.07` → `T.08` → `T.09` → `T.10` → `T.11` → `T.12`) and the open question each page ends with: `tools/folios/timegravity/__init__.py` (`TRACK_MAP`). All thirteen pages (`26` bilingual EN/`es-MX` pages, `110` claims, `108` ledger rows) are shipped.

## Borrowed from other fields

| Field | What the track does with it |
| --- | --- |
| Software verification (mutation testing) | `tools/check_timegravity_labels.py --mutants` applies thirteen in-memory mutants (label flipped up, parent dropped, parent downgraded from `MEASURED`, press row, stale review date, one collaboration, young rows, es-MX label mismatch, es-MX claim-number drift, unaudited Scite contrasting dominance, missing boundary, hub-only phrase on a claim page, a claim on the hub); every one must be killed or the lint fails. |
| Accounting (double entry) | T.02's net GPS term is computed by two unrelated paths (first-order terms; Schwarzschild rate ratio) that must agree within 0.3 µs/day. |
| Metrology (GUM uncertainty budget) | T.02 propagates the stated 1σ of GM, a and R to the net term and combines them in quadrature; c is exact. |
| Evidence synthesis (citation polarity & claim-number parity) | Every ledger DOI carries Scite's public tallies (`scite:<doi>` in the cache; `[observed: Scite ML citation classification]`); the lint fails on a retracted row, requires an audited `contrasting_audit` scope note whenever `contrasting > supporting`, and enforces exact numeric parity across every English and `es-MX` claim span. |
| Aviation (checklist) | `timegravity/LABEL-CHECKLIST.md`: the human decision procedure the lint cannot replace. |
| Pedagogy (predict before reveal) | Every claim page (`T.01`–`T.12`) asks the reader to commit to a prediction before the knockout or planted defect reveals the verdict. |
| Cartography (one map, many views) | Each instrument keeps one state object that every panel and readout reads from. |

## The ledger and the label lint

`timegravity/ledger.json` has one row per cited source (`108` rows, `100 %` referenced in per-page Grounding Ledger tables) with the fields `id`, `label`, `doi`, `year`, `collaboration`, `kind`, `review_by` (schema: `timegravity/ledger.schema.json`). A claim on a page is a span:

```html
<span class="tg-claim" data-tg-label="MEASURED" data-tg-ledger="T01-PR1960,T01-HK1972O">…</span>
```

`DERIVED` claims additionally carry `data-tg-parent="<MEASURED-ID>"`, `data-tg-qualifier="DERIVED (NOT MEASURED)"` (`"DERIVADO (NO MEDIDO)"` on `es-MX`), and localized hover `title` attributes naming the `MEASURED` parent row so computed kernel deductions are never visually conflated with direct experimental measurements.

`tools/check_timegravity_labels.py` enforces: MEASURED needs at least two rows from different collaborations with peer-reviewed DOIs; BOUND is for exclusion limits; DERIVED names a parent MEASURED row (`data-tg-parent`) plus a mature peer-reviewed derivation anchor; rows younger than 24 months or preprints cap at SINGLE RESULT or PROPOSED; press URLs cannot back a claim; every DOI resolves in the offline Crossref cache (`data/folio-citations.cache.json`); English and es-MX pages carry identical label sequences; the build fails when a `review_by` date has passed; a banned-phrase backstop in both languages; the hub-only sentence appears on no other page. The lint's own planted defect (`--planted-defect`) flips one label upward and must fail.

New DOIs enter the cache with `python timegravity/refresh_crossref_cache.py` (the only network call in the track; run by a maintainer, sends no personal data).

## One-command runner

```bash
python timegravity/run_all_timegravity.py
```

runs all `12` generators (`make_t01.py`–`make_t12.py`), all `16` stdlib verifiers across `T.01`–`T.12` (including `T.05`'s five verifiers, plus `--planted-defect` on every one, which must fail), the label lint (plus its `--planted-defect` and `10/10` mutation suite), and `tools/check_folio_citations.py --offline`. Pages are built by `python tools/build_timegravity.py` (also called at the end of `tools/build_longform_folios.py`); plates by `python timegravity/make_plates.py`. Tests: `python -m unittest tests.test_timegravity_track`.
