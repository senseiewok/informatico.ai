---
name: acoustic-helmholtz-metamaterial
description: AI-agnostic acoustics and wave-mechanics engineering skill for sub-wavelength Helmholtz resonator arrays, Stinson viscothermal boundary-layer impedance, and critical coupling.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Sub-Wavelength Acoustic Metamaterial Helmholtz Arrays and Viscothermal Boundary-Layer Damping (Folio E.03)

## 1. Governing Law & Tectonic Identity
- **Folio**: `E.03 · Acoustic Metamaterials & Viscothermal Damping · CSI 09 84 13` (`REV 1.2`, Redated `2026-11-02`)
- **Governing Equation**: `δ_v = √(2ν/ω) · Z_s = ρ_0 c_0 ⇒ α = 1.0 · CSI 09 84 13`
- **Primary Verification Kernel**: `skills/engineering/e03/verify_e03.py`
- **Verification Benchmarks**: `Critical Coupling R_v = ρ_0 c_0 ⇒ α = 0.998 · δ_v = 0.174 mm`
- **Primary Scite Anchor DOI**: https://doi.org/10.1146/annurev-matsci-070616-124032 (Scite Report: https://scite.ai/reports/10.1146/annurev-matsci-070616-124032)

## 2. Deterministic Verification & Falsification Rules
1. Compute viscous boundary layer thickness delta_v = sqrt(2 * nu / omega) and Womersley shear number s = r_neck / delta_v.
2. Enforce critical coupling condition Re(Z_surface) = rho_0 * c_0 and Im(Z_surface) = 0 at target resonance omega_0 for unity absorption.
3. Include end-correction length delta_l = 0.85 * r_neck * (1 - 1.25 * sqrt(porosity)) in effective neck inductance.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Oscillatory Stokes Boundary Layer): At f_0 = 160 Hz, the viscous boundary layer in air is δ_v = √(2ν/ω) = 0.174 mm.
- Stage 2 (Complex Effective Density & Bulk Modulus): When neck radius r_neck = 0.65 mm approaches 3.7 δ_v, viscous shear dissipates acoustic kinetic energy.
- Stage 3 (Critical Impedance Matching, Z_s = Z_0): Reactance vanishes at Helmholtz resonance ω_0 while resistance matches ρ_0 c_0 = 413 Pa·s/m.
- Stage 4 (Broadband Detuned Rainbow Array): Coupling 8 detuned coiled cavities spans 125–315 Hz inside a 110 mm timber ceiling panel.

## 4. Reference Telemetry & Acceptance Bounds
- **Viscous Boundary Layer (δ_v)**: `0.174 mm (at 160 Hz)`
- **Normalized Surface Impedance**: `Z_s / Z_0 = 1.04 + 0.08 i`
- **Peak Absorption Coefficient**: `α_peak = 0.998 (Critical Match)`
- **Acoustic Verdict**: `CLASS A · ZERO FIBER`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Coiled-Space Labyrinthine Metamaterials & Multimode Thixotropic Airway Mucus Liquefaction**: Building on Helmholtz (1863) and Stinson's viscothermal wave theory (1991), modern coiled-space acoustic metamaterials (DOI 10.1146/annurev-matsci-070616-124032) achieve α = 0.998 absorption in 1/19th of a wavelength, while 2025 multimode thixo-viscoelastoplastic rheometry (PMID 41388033; trial NCT07175012) confirms that 15 Hz oscillatory shear (τ_osc = 14.8 Pa) liquefies CF airway mucus plugs above τ_y = 11.5 Pa.
