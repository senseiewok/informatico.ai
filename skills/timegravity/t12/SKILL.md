---
name: timegravity-t12-dark-clock
description: Rebuild and verify the Time & Gravity T.12 toy - the Planck 2018 dark-to-baryonic matter budget (Omega_c / Omega_b = 5.3643), the gravitational proper-time step of an electromagnetically transparent flyby across a two-clock network (closed-form arsinh vs composite Gauss-Legendre quadrature within 1e-11), and the ultralight scalar clock modulation bound - with a planted defect (G_dark = 0 violating the Equivalence Principle).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Two Clocks That Only Meet in Gravity (T.12 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.12` (Time & Gravity, reading order 13 of 13, dated `2026-11-10`)
- **Canonical URL**: https://informatico.ai/timegravity/t12/ (Spanish: https://informatico.ai/es-mx/timegravity/t12/)
- **Cosmological dark-to-baryonic ratio**: `Ω_c h² = 0.1200 ± 0.0012`, `Ω_b h² = 0.02237 ± 0.00015`, `Ω_c / Ω_b = 5.3643 ± 0.0646`, `f_dark = Ω_c / (Ω_c + Ω_b) = 84.29 %`.
- **Gravitational proper-time step of an EM-transparent transit**: `Δν(t)/ν = (Φ_1(t) − Φ_2(t))/c²`, `Δτ(T) = −(2 G M_DM / c² v_0) [arsinh(v_0 T / b_1) − arsinh(v_0 T / b_2)] → −(2 G M_DM / c² v_0) ln(b_2 / b_1)`, `+c² ∂(Δτ_∞)/∂b_1 = 2 G M_DM / (b_1 v_0) = Δv_⊥`.
- **Ultralight scalar clock modulation**: `Φ_Pl = ħ √(8π G ρ_DM) / (m_φ c³)`, `δ(ν_A/ν_B)/(ν_A/ν_B) = ΔK_α d_e Φ_Pl cos(ω_φ t)`.
- **Central numbers**: `Ω_c / Ω_b = 5.3643` (`84.29 %` of non-relativistic matter); for a `10^6 kg` electromagnetically transparent mass at `b_1 = 1 m`, `d_c = 1000 m`, `v_0 = 220 km/s`, `Δτ = −4.664 × 10^{-26} s`, with Gauss–Legendre quadrature matching closed-form `arsinh` within `3.69e-16` (`< 1e-11`) and `+c² ∂(Δτ_∞)/∂b_1` matching `Δv_⊥ = 6.068 × 10^{-10} m/s` within `5.64e-11`; at `m_φ c² = 10^{-15} eV` and `ρ_DM = 0.4 GeV/cm³`, `Φ_Pl = 7.199 × 10^{-16}` (`d_e = 0` gives `0` modulation for co-located clocks).
- **Generator**: `python skills/timegravity/t12/make_t12.py`
- **Verifier**: `python skills/timegravity/t12/verify_t12_dark_clock.py`
- **Knockout check**: `python skills/timegravity/t12/verify_t12_dark_clock.py --planted-defect` (must exit non-zero: `G_dark = 0` severs universal gravitational coupling)
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T12-PLANCK2020` | MEASURED | Planck Collaboration 2020, cosmological parameters (`Ω_c h²`, `Ω_b h²`) | https://doi.org/10.1051/0004-6361/201833910 |
| `T12-CLOWE2006` | MEASURED | Clowe et al. 2006, Bullet Cluster weak-lensing separation of mass from X-ray gas | https://doi.org/10.1086/508162 |
| `T03-MICRO2022` | MEASURED | Touboul et al. 2022, MICROSCOPE weak equivalence principle test (`η ~ 10^{-15}`) | https://doi.org/10.1103/PhysRevLett.129.121102 |
| `T01-PR1960` | MEASURED | Pound & Rebka 1960, gravitational redshift | https://doi.org/10.1103/PhysRevLett.4.337 |
| `T01-CHOU2010` | MEASURED | Chou et al. 2010, optical-clock gravitational redshift at 33 cm | https://doi.org/10.1126/science.1192720 |
| `T03-EIN1916` | DERIVED | Einstein 1916, universal metric coupling to stress-energy `T_{μν}` | https://doi.org/10.1002/andp.19163540702 |
| `T11-JOOS1985` | DERIVED | Joos & Zeh 1985, dipole photon scattering vanishes when `α_EM = 0` | https://doi.org/10.1007/BF01725541 |
| `T12-KENNEDY2020` | BOUND | Kennedy et al. 2020, JILA `87Sr` vs silicon cavity ultralight dark-matter bound | https://doi.org/10.1103/PhysRevLett.125.201302 |
| `T12-FILZINGER2023` | BOUND | Filzinger et al. 2023, PTB `171Yb+` E3/E2 clock ratio dark-matter bound | https://doi.org/10.1103/PhysRevLett.130.253001 |
| `T12-LZ2023` | BOUND | Aalbers et al. (LUX-ZEPLIN) 2023, WIMP-nucleon spin-independent cross-section bound | https://doi.org/10.1103/PhysRevLett.131.041002 |
| `T12-CARNEY2021` | PROPOSED | Carney et al. 2021, mechanical sensor and clock array detection of gravitational dark matter | https://doi.org/10.1088/1367-2630/abd9e7 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t12/make_t12.py`; standard library only; writes only under `src/timegravity/t12/files/`.
2. **Acceptance gate**: `python skills/timegravity/t12/verify_t12_dark_clock.py` must print `"status": "PASS"` with `arsinh_matches_gl5_quadrature: PASS`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task.

## 4. Deterministic verification and falsification rules
1. `Ω_c / Ω_b = 0.1200 / 0.02237 = 5.36432722396` and analytic vs finite-difference error propagation agree within `1e-9`.
2. Across baselines `d_c ∈ {1, 10, 100, 1000} m`, composite Gauss–Legendre quadrature of `∫ (Φ_1(t) − Φ_2(t))/c² dt` matches `−(2 G M_DM / c² v_0) [arsinh(v_0 T / b_1) − arsinh(v_0 T / b_2)]` within `1e-11`, and central differences of `+c² ∂(Δτ_∞)/∂b_1` match `2 G M_DM / (b_1 v_0)` within `1e-9`.
3. Under pure gravity (`d_e = 0`), co-located clocks (`d_c = 0`) have `Δτ = 0` and `δ(ν_A/ν_B) = 0`, while the ultralight scalar energy-density identity `(c² / 8πG) ω_φ² Φ_Pl² = ρ_DM` holds within `1e-12`.
4. Planted defect: setting `G_dark = 0` gives `Δτ = 0` at `d_c > 0`; rule 2 fails and `--planted-defect` exits non-zero.
5. `t12_reference.json` matches `manifest.json` and regenerates byte for byte.

## 5. What the instrument shows (reader side)
- Left panel: Differential gravitational redshift `Δν(t)/ν` and accumulated proper-time step `Δτ(t)` across a two-clock network (`b_1`, baseline `d_c`) during the flyby of an electromagnetically transparent mass `M_DM` (`Λ_EM = 0`). Right panel: Co-located optical-clock portal bound `|d_e|` vs scalar mass `m_φ c²` (`Kennedy 2020`, `Filzinger 2023`) alongside the `d_c = 0` equivalence-principle null for pure gravity (`d_e = 0`).
- Knockout: turn off universal gravitational coupling (`G_dark = 0`) or set clock baseline `d_c = 0`; the differential proper-time step collapses to `0`.
- Predict before you reveal: whether two co-located clocks at the same point (`d_c = 0`) can detect a passing mass that couples only through Einstein's metric `g_{μν}` (`d_e = 0`).

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel `tools/timegravity_kernel_dark_clock.py`, generator, verifier, ledger rows above, and the ES module `src/modules/timegravity-slope.mjs`.

### Not on this page (T2/T3)
- Direct laboratory detection of individual dark-matter transits through gravity alone (`T12-CARNEY2021`) is `PROPOSED` and requires Planck-mass-scale sensors far beyond current optical-clock or optomechanical noise floors.
- The microscopic particle identity of dark matter (and whether it carries any non-gravitational portal coupling `d_e ≠ 0` or `σ_SI ≠ 0` below current `BOUND` limits) is `OPEN`.
