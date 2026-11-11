---
name: herschel-bulkley-yield-rheology
description: AI-agnostic civil and non-Newtonian fluid mechanics skill for Herschel-Bulkley and Bingham concrete pumping rheology, plug-flow radius r_p/R = tau_0/tau_w, and thixotropic dispersion.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Herschel–Bulkley Yield-Stress Rheology: High-Performance Concrete Pumping & Tremie Placement (Folio E.02)

## 1. Governing Law & Tectonic Identity
- **Folio**: `E.02 · Concrete Yield Rheology · CSI 03 30 00` (`REV 1.3`, Redated `2026-11-02`)
- **Governing Equation**: `τ = τ_0 + K γ̇^n · r_p / R = τ_0 / τ_w · ΔP/L = 2τ_w/R`
- **Primary Verification Kernel**: `skills/engineering/e02/verify_e02.py`
- **Verification Benchmarks**: `125 mm Steel Slickline · ACI 304.2R Pumping`
- **Primary Scite Anchor DOI**: https://doi.org/10.1016/j.cemconcomp.2015.11.002 (Scite Report: https://scite.ai/reports/10.1016/j.cemconcomp.2015.11.002)

## 2. Deterministic Verification & Falsification Rules
1. Verify slickline yield mobilization: pumping requires wall shear stress tau_w = (DeltaP * R)/(2L) > tau_0 (plug ratio r_p / R = tau_0 / tau_w < 1).
2. Evaluate Buckingham-Reiner volumetric flow multiplier Q / Q_Newtonian = 1 - (4/3)*(tau_0/tau_w) + (1/3)*(tau_0/tau_w)^4 for Bingham plastics.
3. Account for shear-thinning power-law index n < 1 in the annular tribological lubrication layer.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Unmobilized Solid Arrest, τ_w ≤ τ_0): When wall shear stress falls below yield stress τ_0, the concrete locks into zero-flow solid arrest.
- Stage 2 (Central Unsheared Plug Core, r ≤ r_p): For τ_w > τ_0, an unsheared solid plug of radius r_p/R = τ_0/τ_w translates along the pipe center.
- Stage 3 (Annular Shear-Thinning Lubrication Layer): High shear concentrates in the boundary layer r_p < r ≤ R with power-law index n = 0.65.
- Stage 4 (Polycarboxylate Thixotropic Dispersion): PCE dispersants deflocculate cement grains, cutting yield stress by 65% for high-speed pumping.

## 4. Reference Telemetry & Acceptance Bounds
- **Wall Shear Stress**: `75.0 Pa`
- **Plug Core Radius Ratio**: `37.3% (23.3 mm)`
- **Discharge Output**: `48.2 m³/hr (63.0 yd³/hr)`
- **Pumping State**: `STEADY MOBILIZED PUMPING`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Coaxial Cylinder Tribometers Decode the Sub-Millimeter Slickline Lubrication Layer**: Classical Bingham (1922) and Herschel–Bulkley (1926) pipe equations assumed homogeneous wall slip, but recent high-pressure coaxial tribometry by Secrieru, Feys, Mechtcherine & Roussel (Cement and Concrete Research, DOI 10.1016/j.cemconcomp.2015.11.002) directly measured how polycarboxylate ether (PCE) comb-copolymers form a depleted paste lubrication film at the steel slickline wall—the exact rheological analogue of dornase alfa cleaving DNA-mucin networks in NCT06350474 (PMID 41388033).
