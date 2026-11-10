# Time & Gravity (`T.00`–`T.07`, `T.10`) · a track where the open problem is the subject

**Live:** [https://informatico.ai/timegravity/](https://informatico.ai/timegravity/) · **Español (es-MX):** [https://informatico.ai/es-mx/timegravity/](https://informatico.ai/es-mx/timegravity/)

> **Fixed boundary, printed on every T page and asserted by the lint:** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.

A sibling track beside *Tech & Tools · The Toolbox* (`X.01`–`X.06`), outside the Folio count of 48. The hub states a common intuition once, in the third person, as a question, and carries no claims. Each later page ships six things, and the build refuses a page that lacks one:

1. **One instrument**, hand-written SVG, reduced-motion and keyboard paths, a static plate fallback; the knockout is the argument.
2. **A standard-library verifier** that recomputes the page's central number and fails on a planted defect.
3. **A grounding ledger and a ledger-driven label lint** (`timegravity/ledger.json`, `tools/check_timegravity_labels.py`).
4. **A `SKILL.md` companion** (`skills/timegravity/<slug>/SKILL.md`).
5. **A 5-pace distillation ladder and es-MX** in the same commit.
6. **An AI-contribution line** naming any AI system that contributed to a cited result and the human who checked it.

## Shipped pages (batch 1)

| Code | Page | Instrument and knockout | Verifier's central number · planted defect | Labels on the page |
| --- | --- | --- | --- | --- |
| `T.00` | [The hub](https://informatico.ai/timegravity/) | A worldline with a movable "now" marker: a picture of the question, not a result | none; the lint asserts zero claim spans | none |
| `T.01` | [Gravity as a Slope in the Rate of Time](https://informatico.ai/timegravity/t01/) | 1+1 geodesic where only `g_tt` varies with height; the body falls at g with no force term; knockout flattens the gradient and nothing falls | `a = −9.80665 m/s²` within `1e-6` relative · sign flip makes the body rise | MEASURED, SINGLE RESULT, DERIVED, OPEN |
| `T.02` | [Everyone Moves at One Rate](https://informatico.ai/timegravity/t02/) | Light clock stretched by γ; GPS clock budget from GM, a and c; knockout leaves the satellite clock uncorrected (≈11.5 km/day pseudorange error) | `+45.7 − 7.2 = +38.4 µs/day`, recomputed two ways within `0.3 µs/day`, with a GUM-style uncertainty budget · sign flip | MEASURED, DERIVED, BOUND, OPEN |
| `T.03` | [What Sets the Slope](https://informatico.ai/timegravity/t03/) | ∇²Φ = 4πGρ solved on a radial grid; mass slider reshapes the clock-rate map; two compositions fall together; knockout removes the source | grid recovers `−GM/r` (≈1e-6) and `Φ(0) = −3GM/2R`; separation `< 1e-12 m` · planted η = 10⁻³ separates them by 4.9 mm | MEASURED, SINGLE RESULT, DERIVED, OPEN |
| `T.04` | [A Clock in Two Places](https://informatico.ai/timegravity/t04/) | Zych–Brukner clock interferometer: visibility against height difference and clock frequency; knockout switches gravity off | `V = |cos(ω Δτ/2)|` recomputed two ways; Sr clock 1 m × 1 s keeps V = 0.989; first zero at 10.7 m·s · a clock that never decoheres | DERIVED, SINGLE RESULT, PROPOSED, OPEN (page label PROPOSED) |
| `T.07` | [The Equation with No Time](https://informatico.ai/timegravity/t07/) | Page–Wootters history state on a 16-level clock and a qubit; knockout reads the clock in a different basis and time disappears | `‖Ĥ|Ψ⟩⟩‖ ≈ 1e-15`, `P(+x|tₙ) = cos²(εtₙ/2)` within 1e-10, Jacobi kernel holds the state · a clock whose spectrum ignores the constraint | MEASURED, DERIVED, SINGLE RESULT, PROPOSED, OPEN |
| `T.05` | [Does Gravity Entangle, and Would That Settle It?](https://informatico.ai/timegravity/t05/) | Bose–Marletto–Vedral four-branch phases; entanglement against hold time for three channels at equal weight (quantum, classical LOCC, disputed non-LOCC); knockout switches the channel | Δφ = 0.314 rad, concurrence 0.156 (two ways, 1e-12), negativity 0.078, full entanglement at 25.0 s; LOCC channel < 1e-12 · a classical LOCC channel that entangles. Dispute kernel: Diósi–Penrose critical separation 0.8508σ (letter 0.8501σ), Fig. 3 geometry none at σ = 50 µm and 5 h / 16 h / 20 d at 75 / 100 / 250 µm; classical-channel rate KΔx²/2ħ equals the dephasing threshold (ratio 1.000); the model's entangling power sits in its smeared-potential part (noise part alone: 0; σ → 0: the quantum channel); pure DP collapse with Newton intact kills the 2017 witness below σ = 130 µm (letter geometry: 14 µm; the threshold scales with the geometry's size, ×0.5 → 66 µm, ×2 → 259 µm, and barely with mass or hold time while the phase is small); the dephasing threshold 0.062 /s is the 1/τ_G of Rijavec et al. 2021 within 1 %; geometry map (Plate T.05-M): hybrid entangles above 1.2–38 × nearest approach, witness survives pure collapse above 0.37–1.0 × it, over split/gap 0.03–32 · the model's decoherence dropped. Smeared-gravity kernel: plate-mode ratio ½[erfc(qσ − s/2σ) + e^(2qs) erfc(qσ + s/2σ)] (closed form vs quadrature 1e-14); on the full 2020 Eöt-Wash wedge pattern (Fourier–Bessel, stdlib Bessel functions) the 120-fold torque at 52 µm loses 17.0 % for σ = 75 µm (Yukawa at the published edge 2.5 %; matching σ 44 µm; one-mode bound 10.4 %), Newtonian 120-fold torque 1.51 fN·m at 72 µm; window at σ ≤ 44 µm: nearest separations below 37 µm only; HUST 2020 at the pair level (210 µm gap, geometry from the 2026 review): 4.8 % at σ = 75 µm vs 1.3 % for the α = 1, λ = 48 µm Yukawa, matching at σ ≈ 60 µm · the closed form's second term dropped; the radial series fixed at 250 terms | PROPOSED, DERIVED, OPEN, MEASURED, SINGLE RESULT (page label OPEN) |
| `T.06` | [Does Gravity Collapse the Wave?](https://informatico.ai/timegravity/t06/) | Diósi–Penrose collapse time τ = ħ/E_G for two displaced spheres; R0 exclusion bar with the Gran Sasso and XENONnT bounds; knockout switches gravity off | R0 > 0.545 × 10⁻¹⁰ m recomputed from 576 vs 506 counts (paper 0.54); parameter-free value ⇒ 1.4 × 10⁵ photons, excluded · bound drawn on the wrong side · σ ladder: LISA Pathfinder 40 fm, Gran Sasso 0.54 Å, XENONnT 4.9 Å, natural cut-off 10⁻¹⁴ m, Orch-OR's tubulin (6.5 × 10⁸ s at 10⁻¹⁴ m; 5.5 × 10³⁷ s at 44 µm), the 2025 letter's 50–250 µm, T.05's 44 µm; Casimir floor 17.1 µm · series dropped | PROPOSED, BOUND, SINGLE RESULT, OPEN (page label BOUND) |
| `T.10` | [Page's Counting Argument](https://informatico.ai/timegravity/t10/) | Hawking's line against Page's curve; Haar toy on 10 qubits with a pure-Python eigensolver; knockout removes unitarity | toy within 0.002 nats of Page's formula, peak 2.97 nats at 5 qubits, final 0.69 · a non-unitary toy that never turns over | MEASURED, SINGLE RESULT, DERIVED, PROPOSED, OPEN |

Reading order (T.00 → T.02 → T.01 → T.03 → …) and the open question each page ends with: `tools/folios/timegravity/__init__.py` (`TRACK_MAP`). All nine pages are shipped; T.05 (gravity-mediated entanglement) went last, after its own council pass, by council decision.

## Borrowed from other fields (batch 2)

| Field | What the track does with it |
| --- | --- |
| Software verification (mutation testing) | `tools/check_timegravity_labels.py --mutants` applies ten in-memory mutants (label flipped up, parent dropped, press row, stale review date, one collaboration, young rows, es-MX mismatch, missing boundary, hub-only phrase on a claim page, a claim on the hub); every one must be killed or the lint fails. |
| Accounting (double entry) | T.02's net GPS term is computed by two unrelated paths (first-order terms; Schwarzschild rate ratio) that must agree within 0.3 µs/day. |
| Metrology (GUM uncertainty budget) | T.02 propagates the stated 1σ of GM, a and R to the net term and combines them in quadrature; c is exact. |
| Evidence synthesis (citation polarity) | Every ledger DOI carries Scite's public tallies (`scite:<doi>` in the cache; `[observed: Scite ML citation classification]`); the lint warns when contrasting > supporting and fails on a retracted row. |
| Aviation (checklist) | `timegravity/LABEL-CHECKLIST.md`: the human decision procedure the lint cannot replace. |
| Pedagogy (predict before reveal) | T.02 and T.03 ask the reader to commit to an answer before the knockout or the planted defect reveals it. |
| Cartography (one map, many views) | Each instrument keeps one state object that every panel and readout reads from. |

## The ledger and the label lint

`timegravity/ledger.json` has one row per cited source with the fields `id`, `label`, `doi`, `year`, `collaboration`, `kind`, `review_by` (schema: `timegravity/ledger.schema.json`). A claim on a page is a span:

```html
<span class="tg-claim" data-tg-label="MEASURED" data-tg-ledger="T01-PR1960,T01-HK1972O">…</span>
```

`tools/check_timegravity_labels.py` enforces: MEASURED needs at least two rows from different collaborations with peer-reviewed DOIs; BOUND is for exclusion limits; DERIVED names a parent MEASURED row (`data-tg-parent`); rows younger than 24 months or preprints cap at SINGLE RESULT or PROPOSED; press URLs cannot back a claim; every DOI resolves in the offline Crossref cache (`data/folio-citations.cache.json`); English and es-MX pages carry identical label sequences; the build fails when a `review_by` date has passed; a banned-phrase backstop in both languages; the hub-only sentence appears on no other page. The lint's own planted defect (`--planted-defect`) flips one label upward and must fail. The lint checks mechanics; a human checklist decides the label.

New DOIs enter the cache with `python timegravity/refresh_crossref_cache.py` (the only network call in the track; run by a maintainer, sends no personal data).

## One-command runner

```bash
python timegravity/run_all_timegravity.py
```

runs `make_t01.py`, `verify_t01_time_slope_geodesic.py` (and `--planted-defect`, which must fail), the label lint (and its `--planted-defect`, which must fail) and `tools/check_folio_citations.py --offline`. Pages are built by `python tools/build_timegravity.py` (also called at the end of `tools/build_longform_folios.py`); plates by `python timegravity/make_plates.py`. Tests: `python -m unittest tests.test_timegravity_track`.
