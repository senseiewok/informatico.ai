---
name: timegravity-t08-horizon-thermodynamics
description: Rebuild and verify the Time & Gravity T.08 toy - a two-mode Rindler thermofield double on 16 Fock levels whose partial trace over the left wedge yields a Planck thermal density matrix on the right wedge (verified via a pure-Python Jacobi eigensolver), alongside Rindler proper-time redshift and Gauss-Legendre integration of dS = c^2 dM / T_H(M) = k_B c^3 A / (4 G hbar) - with a planted defect (r = 0 product state with zero cross-horizon entanglement).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# A Horizon Has a Temperature (T.08 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.08` (Time & Gravity, reading order 9 of 11, dated `2026-11-10`)
- **Canonical URL**: https://informatico.ai/timegravity/t08/ (Spanish: https://informatico.ai/es-mx/timegravity/t08/)
- **Rindler wedge & redshift**: `X² − c²T² = ξ² = (c²/a)²`, `dτ = (aξ/c²) dt`.
- **Unruh & Hawking temperatures**: `T_U = ħa / (2π k_B c)`, `κ = c⁴ / (4GM)`, `T_H = ħκ / (2π k_B c) = ħc³ / (8π G M k_B)`.
- **Thermofield double & Bekenstein-Hawking entropy**: `|0_M⟩ = Z_d^{-1/2} Σ_{n=0}^{d-1} e^{-nξ/2} |n⟩_L ⊗ |n⟩_R`, `ρ_R = Tr_L |0_M⟩⟨0_M|`, `S_BH = k_B c³ A / (4Għ)`.
- **Central numbers**: at `ξ = βħω = 2.5` (`d = 16` Fock levels), Jacobi eigenvalues of `ρ_R` match the infinite-dimensional Planck weights `(1 − e^{-ξ})e^{-nξ}` within `1.67e-15` (`< 1e-12`) and match the exact truncated Gibbs distribution across `ξ ∈ [0.5, 4.0]` within `4.11e-15`; Gauss–Legendre integration of `∫ c² dM / T_H(M)` matches `k_B A / (4 l_P²)` within `2.45e-16`; for `1 M_☉`, `T_H = 6.170 × 10^{-8} K` and `S_BH / k_B = 1.049 × 10^{77}`.
- **Generator**: `python skills/timegravity/t08/make_t08.py`
- **Verifier**: `python skills/timegravity/t08/verify_t08_horizon_thermodynamics.py`
- **Knockout check**: `python skills/timegravity/t08/verify_t08_horizon_thermodynamics.py --planted-defect` (must exit non-zero: `r = 0` product vacuum `|0⟩_L ⊗ |0⟩_R`, `S(ρ_R) = 0`)
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T01-PR1960` | MEASURED | Pound & Rebka 1960, gravitational redshift | https://doi.org/10.1103/PhysRevLett.4.337 |
| `T01-GPA1980` | MEASURED | Vessot et al. 1980, Gravity Probe A | https://doi.org/10.1103/PhysRevLett.45.2081 |
| `T08-PENZIAS1965` | MEASURED | Penzias & Wilson 1965, cosmic microwave background | https://doi.org/10.1086/148307 |
| `T08-MATHER1994` | MEASURED | Mather et al. 1994, COBE FIRAS Planck blackbody spectrum | https://doi.org/10.1086/173574 |
| `T08-BCH1973` | DERIVED | Bardeen, Carter & Hawking 1973, four laws of black hole mechanics | https://doi.org/10.1007/BF01645742 |
| `T10-BEKENSTEIN1973` | DERIVED | Bekenstein 1973, black-hole entropy proportional to horizon area | https://doi.org/10.1103/PhysRevD.7.2333 |
| `T10-HAWKING1975` | DERIVED | Hawking 1975, particle creation by black holes (`T_H`, `A/4`) | https://doi.org/10.1007/BF02345020 |
| `T08-BW1975` | DERIVED | Bisognano & Wichmann 1975, modular boost generator and KMS state | https://doi.org/10.1063/1.522605 |
| `T08-UNRUH1976` | DERIVED | Unruh 1976, accelerated detector thermal response (`T_U`) | https://doi.org/10.1103/PhysRevD.14.870 |
| `T08-MUNOZ2019` | SINGLE RESULT | Muñoz de Nova et al. 2019, acoustic BEC sonic horizon (analogue only) | https://doi.org/10.1038/s41586-019-1241-0 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t08/make_t08.py`; standard library only; writes only under `src/timegravity/t08/files/`.
2. **Acceptance gate**: `python skills/timegravity/t08/verify_t08_horizon_thermodynamics.py` must print `"status": "PASS"` with `partial_trace_recovers_planck: PASS`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task.

## 4. Deterministic verification and falsification rules
1. At `ξ = 2.5` (`d = 16` Fock levels), the Jacobi eigenvalues of `ρ_R = Tr_L |0_M⟩⟨0_M|` match `(1 − e^{-ξ})e^{-nξ}` within `1e-12`, and match the exact truncated Gibbs distribution across `ξ ∈ [0.5, 4.0]` within `1e-12`.
2. Every Rindler worldline point satisfies `X² − c²T² = (c²/a)²` and `dτ/dt = aξ/c²` within `1e-12`.
3. 16-point Gauss–Legendre integration of `∫ (c² / T_H(M')) dM'` matches `k_B c³ A / (4Għ)` and `dM c² = (κ c² / 8πG) dA` within `1e-12`.
4. Planted defect: setting the squeezing parameter `r = 0` yields the product state `|0⟩_L ⊗ |0⟩_R` with `S(ρ_R) = 0`; rule 1 fails and `--planted-defect` exits non-zero.
5. `t08_reference.json` matches `manifest.json` and regenerates byte for byte.

## 5. What the instrument shows (reader side)
- Left panel: Rindler spacetime diagram (`cT` vs `X`) showing the null horizons `X = ±cT`, accelerated hyperbolas, and behind-the-horizon mode partner `L`. Right panel: Fock-level occupation bar chart of `ρ_R` against the Planck thermal curve, with readouts for `T_U`, `T_H(M)`, and `S_BH / k_B`.
- Knockout: sever cross-horizon entanglement (`r = 0`, product vacuum `|0⟩_L ⊗ |0⟩_R`); the thermal tail collapses to `n = 0` and `S(ρ_R)` drops to `0`.
- Predict before you reveal: whether a solar-mass black hole is hotter or colder than the `2.725 K` cosmic microwave background.

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel `tools/timegravity_kernel_horizon.py`, generator, verifier, ledger rows above, and the ES module `src/modules/timegravity-slope.mjs`.

### Not on this page (T2/T3)
- Direct detection of astrophysical Hawking radiation (`61.7 nK` for `1 M_☉` is eight orders of magnitude colder than the `2.725 K` CMB) or the full Unruh effect for a macroscopic thermometer is OPEN.
- Acoustic BEC horizons (`T08-MUNOZ2019`) test linear dispersion on a fluid background, not Einstein's field equations or Bekenstein–Hawking entropy.
