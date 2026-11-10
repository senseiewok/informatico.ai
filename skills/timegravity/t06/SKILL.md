---
name: timegravity-t06-collapse-bound
description: Rebuild and verify the Time & Gravity T.06 instrument - the Diosi-Penrose collapse proposal (tau = hbar / E_G for two displaced uniform spheres, closed form against numerical quadrature) and the Gran Sasso spontaneous-radiation bound on R0 recomputed from the published counts - with a planted defect that draws the bound on the wrong side.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Does Gravity Collapse the Wave? (T.06 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.06` (Time & Gravity, reading order 7 of 11, dated `2026-11-09`). Page label **BOUND**; the model itself is **PROPOSED**.
- **Canonical URL**: https://informatico.ai/timegravity/t06/ (Spanish: https://informatico.ai/es-mx/timegravity/t06/)
- **Model**: `τ = ħ / E_G`, `E_G = 2 U_self − U_int(d)`, `U_self = (3/5) G M²/R`, `U_int = G M²/d` beyond contact (quintic in d/2R when overlapping). Far apart `E_G = (6/5) G M²/R`; coincident `E_G = 0`.
- **Radiation (Donadi et al. 2021, Eq. 4)**: `dΓ/dω = (2/3) G e² N² N_a / (π^{3/2} ε₀ c³ R0³ ω)` ⇒ `z_s = a / R0³`, `a ≈ 1.8 × 10⁻²⁹ m³` in the 1,000–3,800 keV window over 62 days.
- **Central numbers**: 576 counts against 506 background ⇒ 95 % excess limit ≈ 111 ⇒ `R0 > 0.545 × 10⁻¹⁰ m` (paper: `0.54 × 10⁻¹⁰ m`); parameter-free `R0 = 0.05 × 10⁻¹⁰ m` ⇒ ≈ 1.4 × 10⁵ predicted photons, excluded. XENONnT 2026: `R0 > 4.9 × 10⁻¹⁰ m` (90 %), `4.5 × 10⁻¹⁰ m` (95 %).
- **Generator**: `python skills/timegravity/t06/make_t06.py`
- **Verifier**: `python skills/timegravity/t06/verify_t06_collapse_bound.py`
- **σ ladder** (`tools/timegravity_kernel_ladder.py`, Plate T.06-L): the smearing width on one log axis. Lower bounds: LISA Pathfinder ≥ 40.1 fm (Helou 2017), Gran Sasso > 0.54 Å, XENONnT > 4.9 Å; the authors' natural cut-off 10⁻¹⁴ m (Tilloy–Diósi 2016, footnote 3); the 2025 letter's 50–250 µm; T.05's recast of the Eöt-Wash 2020 published limits, 33.1 µm (cross-checked live against the recast kernel's σ_95; the retired 44.07 µm edge match kept reproducible). Point-mass DP rate `Γ = (G m²/ħ)[f̃(0) − f̃(Δx)]` with the small-Δx series `Δx²/(12√π σ³)(1 − 3z²/40)`: one tubulin (55 kDa) a nucleon radius apart lives 6.5 × 10⁸ s at 10⁻¹⁴ m and 2.3 × 10³⁷ s at 33 µm, the recast rung (the 25 ms count stays a verifier-internal check, not page text); σ³ law between the top rungs within 1 %. Casimir floor (Van De Kamp 2020, Eq. 14; ρ = 3.5 g/cm³, ε = 5.7, ∂B = 10⁴ T/m, W = 1 µm): gap 8.1 µm, nearest separation ≥ 17.1 µm at 10⁻¹⁵ kg (26.5 µm at 10⁻¹⁴ kg); at the recast limit σ = 33 µm the 23 µm split's window (5.7 µm) is closed, the 10, 5 and 1 µm splits stay open at 10⁻¹⁵ kg (18.3, 23.2 and 27.2 µm against the 17.1 µm floor). Same verifier; `--planted-defect` also drops the series, which breaks the σ³ law.
- **Knockout check**: `python skills/timegravity/t06/verify_t06_collapse_bound.py --planted-defect` (must exit non-zero: the bound inverted, small R0 "allowed")
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T06-DIOSI1987` | PROPOSED | Diósi 1987, universal master equation | https://doi.org/10.1016/0375-9601(87)90681-5 |
| `T06-PENROSE1996` | PROPOSED | Penrose 1996, gravity's role in state reduction | https://doi.org/10.1007/BF02105068 |
| `T06-DONADI2021` | BOUND | Donadi et al. 2021, Gran Sasso underground test | https://doi.org/10.1038/s41567-020-1008-4 |
| `T06-XENONNT2026` | BOUND (young: SINGLE RESULT at most) | XENONnT 2026, PRL 136, 120201 | https://doi.org/10.1103/2jm3-4976 |
| `T06-FEIN2019` | SINGLE RESULT | Fein et al. 2019, superposition beyond 25 kDa | https://doi.org/10.1038/s41567-019-0663-9 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t06/make_t06.py`; standard library only; writes only under `src/research/timegravity/t06/files/`.
2. **Acceptance gate**: `python skills/timegravity/t06/verify_t06_collapse_bound.py` must print `"status": "PASS"` with `bound_recomputed_from_counts: PASS`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task; the cache refresher is the track's only network script, run by hand by a maintainer.

## 4. Deterministic verification and falsification rules
1. `E_G` closed form against a midpoint-rule integration of one sphere's potential over the other's volume: relative difference `< 10⁻³` at `d = 0.5R, 2R, 5R`; the limits `(6/5) G M²/R` and `0` recovered.
2. The 95 % Poisson upper limit on the excess, inverted through `z_s = a/R0³`, lands within 20 % of the published `0.54 × 10⁻¹⁰ m` (achieved 2 %).
3. The rate prefactor `a` recomputed from Eq. 4 without detection efficiency lies within a decade of the paper's value.
4. The parameter-free value lies on the excluded side; XENONnT's bound lies on the allowed side above Gran Sasso's.
5. Planted defect: the orientation of the bound inverted; rule 4 fails and `--planted-defect` exits non-zero.
6. `t06_reference.json` matches `manifest.json` and regenerates byte for byte.

## 5. What the instrument shows (reader side)
- Left: the model's collapse time against mass for the chosen radius and displacement. Right: the R0 exclusion line with the Gran Sasso and XENONnT bounds and the parameter-free value on the excluded side.
- Knockout: gravity off (G → 0), the model predicts nothing. Planted defect: the bound painted on the wrong side.
- Predict before you reveal: how many photons the parameter-free model would have produced at Gran Sasso.

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel `tools/timegravity_kernel_bounds.py` (`dp_self_energy_difference`, `sphere_interaction_energy_numeric`, `poisson_upper_limit`, `gran_sasso_r0_bound`, `check_dp`), generator, verifier, ledger rows above.

### Not on this page (T2/T3)
- Dissipative variants of the model and R0 as a free parameter above the bound are not assessed. CSL is not a gravity model and is out of scope.
- No statement is made that superpositions never collapse; only that this proposal, in its parameter-free form, is excluded by the radiation it predicts.
