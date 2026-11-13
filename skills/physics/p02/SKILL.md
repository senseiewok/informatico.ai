---
name: ciliary-active-matter
description: AI-agnostic physical skill for micro-hydrodynamic active matter synchronization, low Reynolds Stokes flow, and ciliary metachronal wave velocity.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Active Matter Hydrodynamics and Ciliary Metachronal Wave Synchronization (Folio P.02)

A plain-text companion to the essay at https://informatico.ai/physics/p02/ (`P.02 · Active Matter & Cilia`, `REV 1.2`, redated `2026-11-02`).

## The governing relation
`∂_t θ_i = ω_0 + ∑_j K_ij sin(θ_j − θ_i − α) · v_wave = λ f_beat`

## Rules the essay derives
1. Verify PCL height >= 7.0 μm to ensure unhindered active recovery stroke.
2. Calculate Kuramoto order parameter r = |(1/N) sum exp(i theta_k)| >= 0.70 for wave coherence.
3. Flag complete ciliary collapse when h_PCL < 3.5 μm.

## How it works, in four stages
- Stage 1 (Autonomous Beating, omega_0): Individual cilia oscillate at 12–14 Hz, generating localized Stokesian velocity fields.
- Stage 2 (Hydrodynamic Phase-Lag Coupling): Neighboring cilia interact via viscous fluid stress with phase lag alpha ≈ pi/6.
- Stage 3 (Emergent Metachronal Wave): Kuramoto order parameter climbs above 0.85, organizing an antiplectic traveling wave at velocity v = lambda * f ≈ 336 μm/s.
- Stage 4 (Steric & Viscous Arrest): Desiccation below h < 7 μm causes cilia tips to catch on the overlying mucus gel, collapsing wave velocity to zero.

## Reference values stated in the essay
- **Beating Frequency**: `14.00 Hz (Healthy PCL)`
- **Metachronal Wave Velocity**: `336.00 μm/s`
- **Kuramoto Order Parameter**: `0.880 (High Coherence)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1016/s0022-5193(86)80098-4 (Scite report: https://scite.ai/reports/10.1016/s0022-5193(86)80098-4)
- What the essay compares against: High-Speed Video Cilia Kinematics (14 Hz)

## Recent research context
- **Kuramoto Phase Synchronization Explains How Airway Cilia Coordinate Mucociliary Clearance**: Recent active-matter biophysics (Fulford & Blake (1986) DOI 10.1016/s0022-5193(86)80098-4; Kuramoto synchronization) demonstrates that hydrodynamic Oseen coupling across periciliary liquid depth h_ASL = 7.2 μm locks millions of beating cilia (12–15 Hz) into coherent antiplectic metachronal waves.
