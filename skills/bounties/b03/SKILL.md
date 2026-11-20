---
name: bounty-b03-simp-carbon-slab
description: Governing law, 4-stage proof spine, and T0-T3 truth boundary for B.03 (BOUNTY-E1): After the $100M XPRIZE Carbon Removal: A Sub-45 kg CO₂e/m² SIMP Mineralized Slab Design Study. The proof harness is bounties/bounty_e1_simp_carbon_slab.py.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# After the $100M XPRIZE Carbon Removal: A Sub-45 kg CO₂e/m² SIMP Mineralized Slab Design Study (B.03 · BOUNTY-E1)

## 1. Governing Law, Prize Registry & Canonical URL
- **Bounty Folio**: `B.03` (`BOUNTY-E1` · `REV 1.3`, Redated `2026-11-15`)
- **Canonical URL**: https://informatico.ai/bounties/b03/ (Spanish: https://informatico.ai/es-mx/bounties/b03/)
- **Prize / Challenge**: GRAND CHALLENGE B.03 (E-1) · XPRIZE CARBON (CLOSED 2025) + ISTRUCTE
- **Official Registry**: [XPRIZE Carbon Removal ($100M, Closed Apr 2025)](https://www.xprize.org/prizes/carbonremoval)
- **Governing Equation**: `e_net = e_0 (V/V_0) − m_CO2 = 39.40 kg CO₂e/m² < 45.0 · c/c_0 = 1 + 0.40(1 − V/V_0)^1.35 = 1.224 < 1.35`
- **Proof harness (computes the reference results; no planted-defect mode yet)**: `python bounties/bounty_e1_simp_carbon_slab.py`
- **Primary Scite Anchor DOI**: https://doi.org/10.1007/s001580050176 (Scite Report: https://scite.ai/reports/10.1007/s001580050176)

## 2. Falsification Rules
1. Embodied Carbon Ceiling (folio design target): Net cradle-to-gate embodied carbon e_net = 148.0(V/V₀) - m_CO₂ must remain strictly below 45.0 kg CO₂e/m².
2. Normalized Compliance Bound (model target): Normalized structural compliance surrogate c/c₀ = 1.0 + 0.40(1 - V/V₀)^1.35 must remain strictly below 1.35.
3. Model Window on the Workbench: At m_CO₂ = 12.4 kg/m², keeping e_net < 45.0 kg CO₂e/m² requires V/V₀ < 0.3878 (at most 0.38 on the 0.01-step slider). Across the slider range [0.20, 0.70], c/c₀ is at most 1.296 (at V/V₀ = 0.20); in the algebraic surrogate curve, c/c₀ reaches 1.35 only below V/V₀ ≈ 0.0942.

## 3. 4-Stage Formal Proof & Benchmark Mechanism
- Conceptual Stage 1 (SIMP Context, Not Run in Script): Linear elasticity assembly K(ρ) u = f on floor domain Ω (as in FEniCS/dolfinx, DOI 10.1145/3524456).
- Conceptual Stage 2 (SIMP Context, Not Run in Script): Power-law penalization E(ρ_e) with p = 3 and sensitivity filtering ∂c/∂ρ_e (Bendsøe 1989; Sigmund 2001, DOI 10.1007/s001580050176).
- Conceptual Stage 3 & Surrogate Check: At reference fraction V/V₀ = 0.35, the surrogate compliance function gives c/c₀ = 1.0 + 0.40(1 - 0.35)^1.35 = 1.224 < 1.35.
- Stage 4 (Evaluated by Harness): Subtract illustrative mineralization parameter m_CO₂ = 12.4 kg CO₂e/m² from 148.0 × 0.35 = 51.80 to get e_net = 39.40 kg CO₂e/m² < 45.0.

## 4. Reference Results Computed by the Harness (T0/T1)
- **Net Embodied Carbon e_net**: `39.40 kg CO₂e/m² (< 45.0 target)`
- **Normalized Compliance c / c₀**: `1.224 (< 1.35 L/250 deflection limit)`
- **Mass Reduction vs. Solid Slab**: `65.0% concrete mass saved`
- **Verifier Verdict (Worked Example)**: `PASS · SUB-45 KG CO₂E/M²`

## 5. Exact T0–T3 Truth Boundary
### Verified in Repository Today (T0/T1)
- Algebraic compliance-carbon model in bounties/bounty_e1_simp_carbon_slab.py (< 0.05s runtime; no finite-element solver or planted-defect mode yet).
- References FEniCS/dolfinx (Scroggs et al., 2022, DOI 10.1145/3524456) and Sigmund (2001, DOI 10.1007/s001580050176) for the SIMP formulation.

### Open Global Prize Horizon (T2/T3)
- XPRIZE Carbon Removal ($100M, concluded April 2025) & IStructE Structural Awards (commissioned built structures only): any real claim about a slab would require full-scale physical load testing (ACI 318 / EN 1992-1-1 four-point bending to ultimate failure) and third-party ISO 14040/14044 cradle-to-grave LCA review.
