---
name: timegravity-t09-kerr-ringdown
description: Rebuild and verify the Time & Gravity T.09 toy - Kerr horizon geometry, Smarr's identity, and Leaver's (1985) coupled angular and radial continued-fraction solver for the l=m=2, n=0 fundamental and n=1 first-overtone quasinormal modes across spin chi in [0, 0.90] - with a planted defect (spin-blind Schwarzschild area and spectrum on a spinning Kerr hole).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# A Horizon Rings Like a Bell (T.09 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.09` (Time & Gravity, reading order 10 of 11, dated `2026-11-10`)
- **Canonical URL**: https://informatico.ai/timegravity/t09/ (Spanish: https://informatico.ai/es-mx/timegravity/t09/)
- **Kerr geometry**: `r_+ = (GM/c²)(1 + √(1 − χ²))`, `A(M, χ) = 8π (GM/c²)² (1 + √(1 − χ²))`, `Ω_H = χc³ / (2GM(1 + √(1 − χ²)))`.
- **Smarr & First Law**: `Mc² = (κc² / 4πG) A + 2 Ω_H J` and `d(Mc²) = (κc² / 8πG) dA + Ω_H dJ`.
- **Teukolsky–Leaver QNMs**: coupled 3-term continued fractions for `s = −2, l = m = 2` angular separation constant `A_{lm}(χ, Mω)` and complex frequency `Mω_{lmn}(χ)`; `f_{lmn} = c³ Re(Mω_{lmn}) / (2π GM)`, `τ_{lmn} = (GM/c³) / |Im(Mω_{lmn})|`.
- **Central numbers**: across `χ ∈ (0.0, 0.2, 0.4, 0.5, 0.68, 0.8, 0.9)`, Leaver continued-fraction residual `< 1e-11` (achieved `2.81e-15`), matching published tables within `6.41e-9` (`n = 0`) and `8.34e-9` (`n = 1`); Smarr relative error `1.17e-16`; at fiducial GW150914 remnant `(M = 62 M_☉, χ = 0.68)`, `r_+ = 158.68 km`, `A = 365,125 km²`, `f_{220} = 273.07 Hz`, `τ_{220} = 3.747 ms`, `f_{221} = 266.80 Hz`, `τ_{221} = 1.239 ms`.
- **Generator**: `python skills/timegravity/t09/make_t09.py`
- **Verifier**: `python skills/timegravity/t09/verify_t09_kerr_ringdown.py`
- **Knockout check**: `python skills/timegravity/t09/verify_t09_kerr_ringdown.py --planted-defect` (must exit non-zero: spin-blind Schwarzschild area and spectrum at `χ > 0` violate Smarr by `69.1 %` and Leaver's radial continued fraction by `2.14`)
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T10-ABBOTT2016` | MEASURED | GW150914, first binary black hole merger observation | https://doi.org/10.1103/PhysRevLett.116.061102 |
| `T09-ABBOTT2016B` | MEASURED | GW150914 tests of GR, post-merger fundamental ringdown consistency | https://doi.org/10.1103/PhysRevLett.116.221101 |
| `T10-ISI2021` | MEASURED | Isi et al. 2021, independent GW150914 area-law analysis | https://doi.org/10.1103/PhysRevLett.127.011103 |
| `T09-KERR1963` | DERIVED | Kerr 1963, spinning vacuum metric | https://doi.org/10.1103/PhysRevLett.11.237 |
| `T10-HAWKING1971` | DERIVED | Hawking 1971, area theorem `δA ≥ 0` | https://doi.org/10.1103/PhysRevLett.26.1344 |
| `T09-SMARR1973` | DERIVED | Smarr 1973, Kerr horizon mass formula | https://doi.org/10.1103/PhysRevLett.30.71 |
| `T09-TEUKOLSKY1973` | DERIVED | Teukolsky 1973, separable Kerr perturbation equations | https://doi.org/10.1086/152444 |
| `T09-LEAVER1985` | DERIVED | Leaver 1985, continued-fraction QNM representation | https://doi.org/10.1098/rspa.1985.0119 |
| `T09-ISI2019` | PROPOSED | Isi et al. 2019, GW150914 `n = 1` overtone spectroscopy claim | https://doi.org/10.1103/PhysRevLett.123.111102 |
| `T09-COTESTA2022` | OPEN | Cotesta et al. 2022, ringdown overtone start-time sensitivity | https://doi.org/10.1103/PhysRevLett.129.111102 |
| `T10-LVK2025` | SINGLE RESULT | GW250114 SNR 80 Kerr ringdown and area law (young row) | https://doi.org/10.1103/kw5g-d732 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t09/make_t09.py`; standard library only; writes only under `src/timegravity/t09/files/`.
2. **Acceptance gate**: `python skills/timegravity/t09/verify_t09_kerr_ringdown.py` must print `"status": "PASS"` with `leaver_continued_fraction_roots: PASS`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task.

## 4. Deterministic verification and falsification rules
1. Smarr's identity `Mc² = (κc² / 4πG) A + 2 Ω_H J` holds within `1e-12` and the differential first law holds within `1e-9` across `χ ∈ [0, 0.90]`.
2. Leaver's coupled angular and radial continued fractions converge with residual `< 1e-11` for `(2,2,0)` and `(2,2,1)` across `χ ∈ (0.0, 0.2, 0.4, 0.5, 0.68, 0.8, 0.9)` and match published tables within `1e-5`.
3. Planted defect: replacing `A(M, χ)` and `Mω(χ)` with spin-independent Schwarzschild values violates Smarr and Leaver's radial continued fraction at `χ > 0`; `--planted-defect` exits non-zero.
4. `t09_reference.json` matches `manifest.json` and regenerates byte for byte.

## 5. What the instrument shows (reader side)
- Left panel: damped ringdown strain `h(t)` for `(2,2,0)` and `(2,2,1)` with interactive sliders for remnant mass `M / M_☉` (`20–100 M_☉`) and spin `χ` (`0.00–0.90`). Right panel: `(f_{220}, τ_{220})` and `(f_{221}, τ_{221})` trajectories in the frequency–damping plane, plus horizon radius `r_+`, area `A`, and Smarr balance.
- Knockout: replace Kerr with a spin-blind Schwarzschild horizon (`χ = 0` locked); the frequency misses `273 Hz` by `53 Hz` and Smarr's rotational work term fails.
- Predict before you reveal: whether spinning up a black hole at fixed mass makes itshorizon area larger or smaller, and its fundamental ringdown pitch higher or lower.

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel `tools/timegravity_kernel_kerr.py`, generator, verifier, ledger rows above, and the ES module `src/modules/timegravity-slope.mjs`.

### Not on this page (T2/T3)
- Never plug published median masses/spins into `A(M, χ)` to claim an independent observational test of `A_f > A_1 + A_2`; an observational area-law test requires full joint `(M, χ)` posteriors gated at the merger time (`T10-ISI2021`, `T10-LVK2025`), quoted as those papers' own reported results.
- Whether the `n = 1` first overtone was cleanly resolved above noise transients in `GW150914` remains disputed (`T09-ISI2019` vs `T09-COTESTA2022`, labelled `PROPOSED` / `OPEN`); `GW250114` (`T10-LVK2025`, 2025) is capped at `SINGLE RESULT` under the 24-month rule.
