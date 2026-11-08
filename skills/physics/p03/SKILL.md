---
name: viscoplastic grout-soft-matter
description: AI-agnostic physical skill for complex fluid rheology, Carreau-Yasuda shear thinning, and nanoparticle anomalous subdiffusion in ventilation duct viscoplastic grout.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Soft Matter Rheology and Anomalous Subdiffusion in Entangled Mucin Hydrogels (Folio P.03)

## 1. Governing Law & Tectonic Identity
- **Folio**: `P.03 · Soft Matter & Subdiffusion` (`REV 1.2`, Redated `2026-11-02`)
- **Governing Equation**: `η(γ̇) = η_∞ + (η_0 − η_∞)[1 + (λ γ̇)²]^((n−1)/2) · ξ_mesh ~ w^(−0.75)`
- **Primary Verification Kernel**: `tools/physics_kernel.py`
- **Verification Benchmarks**: `Multiple-Particle Tracking (MPT) · MUC5AC / MUC5B Hydrogels`
- **Primary Scite Anchor DOI**: https://doi.org/10.1103/PhysRevLett.74.1250 (Scite Report: https://scite.ai/reports/10.1103/PhysRevLett.74.1250)

## 2. Deterministic Verification & Falsification Rules
1. Scale mesh pore diameter as xi = 140 * (2.0 / w)^0.75 nm. 2. Compute subdiffusion exponent alpha(d_p, xi) to verify penetration window. 3. Trigger viscoplastic grout plug alert when solids fraction w >= 7.0%.

## 3. Rev. Lett. DOI 10.1103/PhysRevLett.74.1250), multiple-particle tracking studies (Lai et al. PNAS DOI 10.1073/pnas.0705326104) map the exact mesh-size threshold where inhaled mRNA colloidal tracers escape mucin caging.