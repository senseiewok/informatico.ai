---
name: essay-es12-cycle-affinity-tur-gates
description: Verify Cross-Scale Essay ES.12 (Cycle Affinity, Time-Reversal Asymmetry, and Irreversible Gates) - iso-P_o forward-flux gauge family on 3-state heterogeneous Markov rings, dual-solver Barato-Seifert TUR (Q_TUR >= 2), 4-state open-subspace complete-monotonicity breaking vs single-open-state monotonicity, 9 cached Crossref DOIs, and 10 core Lean 4 Prelude theorems.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Cycle Affinity, Time-Reversal Asymmetry, and the Irreversible Gate (`ES.12` · Cross-Scale Essay)

## 1. Essay identity, canonical URLs, and owned artifacts
- **Essay code & slug**: `ES.12` · `cycle-affinity-tur-gates` (dated `2026-11-21`, plate `essay12`, instrument `cycle_affinity`)
- **Canonical URL**: https://informatico.ai/essays/cycle-affinity-tur-gates/ (Spanish twin: https://informatico.ai/es-mx/essays/cycle-affinity-tur-gates/)
- **Interactive observatory module**: `src/modules/cross-scale-essays.mjs` (`data-cs-instrument="cycle_affinity"`)
- **Physics kernel & bilingual monograph module**: `tools/folios/essays/e12_cycle_affinity_gates.py`
- **Companion formal specification**: `skills/essays/cycle-affinity-tur-gates/CycleAffinityGates.lean` (pure core Lean 4 Prelude, zero external imports, `namespace Informatico.Essays.ES12`)
- **Standalone deterministic verifier**: `python -X utf8 skills/essays/cycle-affinity-tur-gates/verify_essay_cycle_affinity.py`
- **Planted-defect knockout check**: `python -X utf8 skills/essays/cycle-affinity-tur-gates/verify_essay_cycle_affinity.py --planted-defect` (must exit `1`)

## 2. Four coupled analytical & formal-verification pillars
1. **Iso-$P_o$ Forward-Flux Gauge Family (`Onsager 1931`; `Seifert 2012`; `Rao & Esposito 2016`)**:
   - On a 3-state cyclic graph `C₁ ↔ C₂ ↔ O ↔ C₁` with stationary occupancy `π = (0.35, 0.25, 0.40)` and heterogeneous base conductances `w₀ = (2.0, 1.5, 1.0) s⁻¹`, shifting forward bond fluxes `φ⁺ = w₀ + J` (`φ⁻ = w₀`) preserves Kirchhoff node balance identically for all `J >= 0`, keeping `P_o = 0.40` flat while cycle affinity `A(J) = ln(Φ⁺/Φ⁻)` grows.
2. **Heterogeneous 3-State Cycle Variance & Dimensionless Barato–Seifert TUR (`Barato & Seifert 2015`; `Gingrich et al. 2016`; `Van Vu & Hasegawa 2021`)**:
   - Computes current diffusivity `D_J = λ''(0) / 2` from closed-form characteristic-polynomial implicit differentiation of `det(λI − W(χ)) = 0` and checks agreement (`< 1e-7`) against direct tilted-eigenvalue finite differences, verifying `Q_TUR = (σ/k_B)(2 D_J)/J² >= 2` across all `J > 0` (`J = 4.0 s⁻¹ → A = 4.0073 k_B T, Q_TUR = 2.3203`; ATP-scale `w₀ = (0.02, 0.015, 0.01) s⁻¹` at `J = 10.0 s⁻¹ → A = 19.6291 k_B T, Q_TUR = 6.7903`).
3. **4-State Open-Subspace Complete-Monotonicity Breaking (`Csanády, Nairn & Gadsby 2006`; `Zhang et al. 2018`)**:
   - Under equilibrium detailed balance (`A = 0`) and equilibrium-flux entry `p_eq ∝ (π_O1 e₁, π_O2 e₂)`, the exit-time PDF from `{O₁, O₂}` has non-positive initial slope `f'_eq(0) = −42.3333 s⁻² <= 0` (`t_peak = 0.000 s`). Hydrolysis-driven entry into `O₁` (`p_drv = (1, 0)`) flips the slope to `f'_drv(0) = +31.0 s⁻² > 0` (`f_peak = 2.0166 s⁻¹` at `94 ms`), whereas a 1-open-state ring stays monotone (`−e² <= 0`).
4. **Ten Core Lean 4 Prelude Theorems (`CycleAffinityGates.lean`)**:
   - Checks SI homogeneity, Kirchhoff iso-`P_o` node balance + positive cycle flux, weighted 3-edge Cauchy–Schwarz variance identity, `4ab <= (a+b)^2`, equilibrium-entry non-positivity, `Q_OO` real-mode discriminant, `+31 > 0` peaked-burst and `−18 < 0` sub-threshold witnesses, single-open-state monotonicity, and the 4-architecture table.

## 3. Primary Crossref DOIs verified offline (`9 / 9` cached)
| Source ID | Reference | DOI |
| --- | --- | --- |
| `ES12-ONSAGER1931` | Onsager (1931), *Phys. Rev.* | https://doi.org/10.1103/physrev.37.405 |
| `ES12-HARADA2005` | Harada & Sasa (2005), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.95.130602 |
| `ES12-CSANADY2006` | Csanády, Nairn & Gadsby (2006), *J. Gen. Physiol.* | https://doi.org/10.1085/jgp.200609558 |
| `ES12-SEIFERT2012` | Seifert (2012), *Rep. Prog. Phys.* | https://doi.org/10.1088/0034-4885/75/12/126001 |
| `ES12-BARATO2015` | Barato & Seifert (2015), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.114.158101 |
| `ES12-GINGRICH2016` | Gingrich et al. (2016), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.116.120601 |
| `ES12-RAO2016` | Rao & Esposito (2016), *Phys. Rev. X* | https://doi.org/10.1103/physrevx.6.041064 |
| `ES12-ZHANG2018` | Zhang, Liu & Chen (2018), *PNAS* | https://doi.org/10.1073/pnas.1815287115 |
| `ES12-VANVU2021` | Van Vu & Hasegawa (2021), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.126.010601 |
