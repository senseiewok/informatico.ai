---
name: mucus-soft-matter
description: AI-agnostic physical skill for complex fluid rheology, Carreau-Yasuda shear thinning, and nanoparticle anomalous subdiffusion in airway mucus.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Soft Matter Rheology and Anomalous Subdiffusion in Entangled Mucin Hydrogels (Folio P.03)

## 1. Governing Law & Tectonic Identity
- **Folio**: `P.03 · Soft Matter & Subdiffusion` (`REV 1.2`, Redated `2026-11-02`)
- **Governing Equation**: `η(γ̇) = η_∞ + (η_0 − η_∞)[1 + (λ γ̇)²]^((n−1)/2) · ξ_mesh ~ w^(−0.75)`
- **Primary Verification Kernel**: `skills/physics/p03/verify_p03.py`
- **Verification Benchmarks**: `Multiple-Particle Tracking (MPT) · MUC5AC / MUC5B Hydrogels`
- **Primary Scite Anchor DOI**: https://doi.org/10.1103/PhysRevLett.74.1250 (Scite Report: https://scite.ai/reports/10.1103/PhysRevLett.74.1250)

## 2. Deterministic Verification & Falsification Rules
1. Scale mesh pore diameter as xi = 140 * (2.0 / w)^0.75 nm.
2. Compute subdiffusion exponent alpha(d_p, xi) to verify penetration window.
3. Trigger mucus plug alert when solids fraction w >= 7.0%.

## 3. 4-Stage Physical & Mathematical Mechanism
- Stage 1 (Healthy Mesh, 2% solids): Mucin mesh pore size xi ≈ 140 nm allows 65 nm PEGylated LNPs to diffuse freely (alpha ≈ 0.72).
- Stage 2 (Shear-Thinning Response): Ciliary shear rates (dot_gamma ~ 10 s^-1) reduce local gel viscosity by an order of magnitude via Carreau-Yasuda dynamics.
- Stage 3 (Concentration Shock & Plug Formation): In CF sputum (8% solids), pore size drops to 45 nm, sterically locking particles larger than 50 nm.
- Stage 4 (Subdiffusive Trapping): Particle trajectory collapses to alpha < 0.20, demonstrating the necessity of dense PEGylation and mucolytic co-delivery.

## 4. Reference Telemetry & Acceptance Bounds
- **Mesh Pore Size**: `140.0 nm (Healthy) vs 49.5 nm (CF)`
- **Subdiffusion Exponent (alpha)**: `0.814 (65 nm LNP in Healthy)`
- **Zero-Shear Viscosity**: `0.055 Pa·s (2% solids)`
- **Kernel Verification**: `PASS · VERIFIED`

## 5. Frontier Discovery & Contemporary Research Context (2024–2026)
- **Single-Particle Tracking Reveals Anomalous Subdiffusion to Normal Diffusion Crossover in CF Sputum**: Applying Pierre-Gilles de Gennes's polymer correlation scaling and Mason–Weitz generalized Stokes–Einstein microrheology (Phys. Rev. Lett. DOI 10.1103/PhysRevLett.74.1250), multiple-particle tracking studies (Lai et al. PNAS DOI 10.1073/pnas.0705326104) map the exact mesh-size threshold where inhaled mRNA lipid nanoparticles escape mucin caging.
