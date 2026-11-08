---
name: hygroscopic-timber-timoshenko-bilayer
description: AI-agnostic architectural and timber-engineering skill for Stephen Timoshenko bilayer curvature, orthotropic wood moisture swelling (alpha_T vs alpha_L), and zero-energy responsive building skins.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Bending-Active & Hygroscopic Programmable Timber Skins: Timoshenko Bilayer Curvature, Orthotropic Moisture Swelling & Zero-Energy Climate Facades (Folio A.09)

## 1. Governing Law & Tectonic Identity
- **Folio**: `A.09 · Hygroscopic Timber Skins & Timoshenko Curvature · CSI 06 18 00` (`REV 1.0`, Redated `2026-11-03`)
- **Governing Equation**: `κ = 6(1+m)² Δα ΔMC / [h (3(1+m)² + (1+mn)(m² + 1/mn))] · EN 1995-1-1 · CSI 06 18 00`
- **Primary Verification Kernel**: `skills/architecture/a09/verify_a09.py`
- **Verification Benchmarks**: `ΔMC = +6.0% · h = 6.0 mm ⇒ κ = 1.42 m⁻¹ · δ_tip = 128 mm (0 W Power)`
- **Primary Scite Anchor DOI**: https://doi.org/10.1364/JOSA.11.000233 (Scite Report: https://scite.ai/reports/10.1364/JOSA.11.000233)

## 2. Deterministic Verification & Falsification Rules
1. Compute differential hygroscopic strain Delta_epsilon = (alpha_T - alpha_L) * Delta_MC below the Fiber Saturation Point (MC <= 28%).
2. Evaluate Timoshenko curvature kappa = 6 * (1 + m)^2 * Delta_epsilon / (h * (3 * (1 + m)^2 + (1 + m*n) * (m^2 + 1/(m*n)))) with m = h_1/h_2 and n = E_1/E_2.
3. Calculate cantilever aperture tip deflection delta_tip = (1 - cos(kappa * L)) / kappa approx 0.5 * kappa * L^2 and verify Eurocode 5 rolling-shear stress limits.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Orthotropic Cellulose Cell-Wall Sorption, Continuing E.04): Below fiber saturation (28% MC), tangential beech wood swells at α_T = 0.32%/%MC while longitudinal grain stays locked at α_L = 0.012%/%MC.
- Stage 2 (Timoshenko Bilayer Interfacial Shear, DOI 10.1364/JOSA.11.000233): Bonding active tangential ply h_2 to passive longitudinal ply h_1 converts Δε = (α_T − α_L)ΔMC into pure curvature κ = 1.42 m⁻¹.
- Stage 3 (Zero-Energy Weather-Responsive Facade Petal): A 425 mm cantilever petal opens δ_tip = ½ κ L² = 128 mm in dry sun (64.5% free vent area) and seals tight against driving rain.
- Stage 4 (Industrial Self-Shaping CLT Shells, Continuing A.02): Kiln-drying flat 90 mm cross-laminated billets pre-forms doubly curved structural tower skins without curved CNC milling.

## 4. Reference Telemetry & Acceptance Bounds
- **Timoshenko Curvature (κ)**: `1.42 m⁻¹ (R = 0.70 m)`
- **Petal Tip Deflection (δ_tip)**: `128.0 mm (at L = 425 mm)`
- **Passive Ventilation Opening**: `64.5% Free Area (0 W)`
- **Eurocode 5 / Hygro Verdict**: `ZERO-ENERGY ACTUATION · PASS`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Stephen Timoshenko's 1925 Bilayer Theorem & Cross-Grained Beech Skins Power Zero-Energy Climate Facades**: Completing the mass-timber and psychrometric threads of Folios A.02, E.04, and A.08, Achim Menges's meteorosensitive timber architecture unites Stephen Timoshenko's bilayer curvature theorem (JOSA DOI 10.1364/JOSA.11.000233) with wood's 25:1 tangential-to-longitudinal moisture swelling ratio to open and seal building envelopes with zero motor power.
