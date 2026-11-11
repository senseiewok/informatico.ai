---
name: essay-es08-schur-complements-nuisance-identifiability
description: Verify Cross-Scale Essay ES.08 (Schur Complements and Nuisance Identifiability) - Modified Gram-Schmidt W-orthogonal Fisher Schur-complement projection of the 2020 Eöt-Wash 120-fold wedge recast, saturated 3-point Kiefer-Wolfowitz D-optimal separation design, sub-50 um Fisher gains, cross-scale sloppy Fisher spectra, and 10 zero-sorry core Lean 4 theorems.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Schur Complements & Nuisance Identifiability: Floating Calibrations, 3-Point Optimal Designs, and Why Sloppy Fits Still Pin Short-Range Gravity (`ES.08` · Cross-Scale Essay)

## 1. Essay identity, canonical URLs, and owned artifacts
- **Essay code & slug**: `ES.08` · `schur-complements-nuisance-identifiability` (dated `2026-11-11`, plate `essay08`, instrument `schur_recast`)
- **Canonical URL**: https://informatico.ai/essays/schur-complements-nuisance-identifiability/ (Spanish twin: https://informatico.ai/es-mx/essays/schur-complements-nuisance-identifiability/)
- **Physics kernel & bilingual monograph module**: `tools/folios/essays/e08_schur_identifiability.py` (coupled to `tools/timegravity_kernel_recast.py` and `tools/timegravity_kernel_wedge.py`)
- **Companion zero-sorry formal specification**: `skills/essays/schur-complements-nuisance-identifiability/SchurIdentifiability.lean` (pure core Lean 4 Prelude, zero external imports)
- **Standalone deterministic verifier**: `python -X utf8 skills/essays/schur-complements-nuisance-identifiability/verify_essay_schur_identifiability.py`
- **Planted-defect knockout check**: `python -X utf8 skills/essays/schur-complements-nuisance-identifiability/verify_essay_schur_identifiability.py --planted-defect` (must exit `1`)

## 2. Five coupled physics, experimental-design & epistemic pillars
1. **Modified Gram–Schmidt Fisher Schur-Complement Projection (`Lee et al. 2020`; `Lee et al. 2021`; `Trillo & Navascués 2025`)**:
   - Constructs a `W`-orthonormal basis `Q = [q₁, q₂]` (error `< 10⁻¹³`, projector idempotence `< 10⁻¹⁴`) for the linearized floating calibration tangent space `N = span{1, s_min ∂_s ln T_N(s)}` corresponding to floating Newtonian torque scale `δγ` and rigid separation offset `δs₀`.
   - Under equal relative weights (`W = I`, 12 log separations `52 µm` to `3000 µm`): raw `σ_95 = 33.08 µm` (`α_eff(33 µm) = −7.302`, `2.38%` residual) vs Schur-projected `σ_95^⊥ = 32.98 µm` (`α_eff^⊥(33 µm) = −7.383 < −7.360`, `2.20%` residual, `cos θ_⊥ = 0.999758`, `82.05%` retained norm, `67.32%` Fisher retention).
   - Under constant-torque-noise weights (`W = diag(T_N²)`): raw `σ_95 = 33.01 µm` vs Schur-projected `σ_95^⊥ = 32.87 µm` (`32.85 µm` exact continuous root; `α_eff^⊥(33 µm) = −7.534 < −7.360`, `1.14%` residual, `cos θ_⊥ = 0.999935`, `45.77%` retained norm, `20.95%` Fisher retention—`79.05%` absorbed by floating `(δγ, δs₀)`).
2. **Saturated 3-Point Carathéodory / Kiefer–Wolfowitz D-Optimal Separation Design (`Geraci et al. 2008`; `Tan et al. 2020`; `Westphal et al. 2021`)**:
   - Maximizing `det M(ξ)` for `(γ, s₀, α_smeared)` over `[25 µm, 3000 µm]` concentrates onto `3` support points `[25.00 µm, 101.01 µm, 3000.00 µm]` with equal weights `(1/3, 1/3, 1/3)`, satisfying `max_s x(s)ᵀ M(ξ*)⁻¹ x(s) = 3.0000` at every support point.
   - Stepping minimum wedge separation down from `52 µm` boosts constant-torque-noise Schur Fisher information `I_schur` by `5.36×` at `35 µm` and `13.20×` at `25 µm`.
3. **Cross-Scale Standardized `3 × 3` Sloppy Fisher Spectra (`Raissi et al. 2019`; `MacAdam 1942`; `Veit et al. 2020`)**:
   - Compares unit-diagonal correlation Fisher eigenvalues `Tr(R) = 3.00` and coordinate-invariant Schur retention `1 − R_θn R_nn⁻¹ R_nθ` across Eöt-Wash wedges (`20.95%`), Folio `E.07` 8-sensor bridge PINNs (`0.019%` sparse displacement vs `19.52%` with `∂_x⁴` PDE regularization, `1004×` boost), Folio `M.08` trichromatic `L, M, S` cones (`10.96%`), and 2-site allosteric rescue (`0.85%` on 1-D equimolar co-dosing vs `5.34%` and `10.14×` `I_schur` on a 2-D checkerboard).
4. **Epistemic Scope & Preservation of ES.07's `D = 75 µm` Quantum Island**:
   - Across all `4` weighting and projection variants (`32.85 µm ≤ σ_95 ≤ 33.08 µm`), the infinite-split parallel hybrid ceiling `2.2109 σ_95` stays inside `72.63 µm..73.14 µm < 75.00 µm`, while separating linearized surrogate-grid projection (`DERIVED (NOT MEASURED)`) from a raw 95-run Eöt-Wash nonlinear profile refit.
5. **Ten Zero-`sorry` Core Lean 4 Prelude Theorems (`SchurIdentifiability.lean`; `Tooby-Smith 2025`)**:
   - Certifies `6` SI dimensional identities, `0 ≤ sq x`, 4-variable Cauchy–Schwarz–Lagrange identity, Schur Fisher bounds, Gram–Schmidt nuisance annihilation, Pythagorean Fisher decomposition, Kiefer–Wolfowitz trace saturation, `23 < 125 < 309` sub-`50 µm` gain, `75 µm` island preservation, and `n_pts < p_params` rank deficiency.

## 3. Primary Crossref DOIs verified offline (`10 / 10` cached)
| Source ID | Reference | DOI |
| --- | --- | --- |
| `ES08-LEE2020` | Lee et al. / Eöt-Wash (2020), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.124.101101 |
| `ES08-LEE2021` | Lee et al. (2021), *Class. Quantum Grav.* | https://doi.org/10.1088/1361-6382/abebf2 |
| `ES08-GERACI2008` | Geraci et al. (2008), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.78.022002 |
| `ES08-TAN2020` | Tan et al. (2020), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.124.051301 |
| `ES08-TRILLO2025` | Trillo & Navascués (2025), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.111.l121101 |
| `ES08-WESTPHAL2021` | Westphal et al. (2021), *Nature* | https://doi.org/10.1038/s41586-021-03250-7 |
| `ES08-RAISSI2019` | Raissi, Perdikaris & Karniadakis (2019), *J. Comput. Phys.* | https://doi.org/10.1016/j.jcp.2018.10.045 |
| `ES08-MACADAM1942` | MacAdam (1942), *J. Opt. Soc. Am.* | https://doi.org/10.1364/josa.32.000247 |
| `ES08-VEIT2020` | Veit et al. (2020), *JCI Insight* | https://doi.org/10.1172/jci.insight.139983 |
| `ES08-TOOBYSMITH2025` | Tooby-Smith / HepLean (2025), *Comput. Phys. Commun.* | https://doi.org/10.1016/j.cpc.2024.109457 |
