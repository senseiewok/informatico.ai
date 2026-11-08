---
name: bounty-b02-surface-code-femoco
description: Deterministic verification harness, 4-stage proof spine, and T0-T3 truth boundary for B.02 (BOUNTY-P1): $5M XPRIZE Quantum Applications & Unitary Foundation: Surface-Code Thresholds & FeMoCo Catalysis.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# $5M XPRIZE Quantum Applications & Unitary Foundation: Surface-Code Thresholds & FeMoCo Catalysis (B.02 · BOUNTY-P1)

## 1. Governing Law, Prize Registry & Canonical URL
- **Bounty Folio**: `B.02` (`BOUNTY-P1` · `REV 1.2`, Redated `2026-11-08`)
- **Canonical URL**: https://informatico.ai/bounties/b02/ (Spanish: https://informatico.ai/es-mx/bounties/b02/)
- **Prize / Challenge**: BOUNTY B.02 (P-1) · $5M XPRIZE QUANTUM + UNITARYHACK
- **Official Registry**: [Metriq.info Quantum Benchmark Registry](https://metriq.info/)
- **Governing Equation**: `P_L = 0.03 (p_phys / p_th)^((d+1)/2) · Q_phys = 2 · N_tiles · d² (d = 27 ⇒ P_L = 3.00 × 10⁻¹⁶)`
- **Primary Verification Harness**: `python bounties/bounty_p1_surface_code_femoco.py`
- **Primary Scite Anchor DOI**: https://doi.org/10.1103/PhysRevA.86.032324 (Scite Report: https://scite.ai/reports/10.1103/PhysRevA.86.032324)

## 2. Deterministic Verification & Falsification Rules
1. Sub-Threshold Suppression Invariant: Fault-tolerant exponential suppression holds if and only if p_phys < p_th = 0.01; at p_phys ≥ p_th, increasing code distance d degrades rather than improves logical fidelity.
2. Deep-Circuit Survival Ceiling: Simulating FeMoCo's 10¹⁰ Toffoli/T gates requires per-round logical error P_L < 10⁻¹²; at p_phys = 0.001 and d = 27, P_L = 3.00 × 10⁻¹⁶ passes with >3 orders of magnitude margin.
3. Physical Qubit Footprint Conservation: Total physical qubits scale strictly as Q_phys = 2 × (N_data + N_factory) × d² = 2 × 294 × 27² = 428,652.

## 3. 4-Stage Formal Proof & Benchmark Mechanism
- Stage 1: PySCF Active-Space Hamiltonian & Qubitization — Extract the 54-electron, 54-orbital FeMoCo active-space integrals in PySCF and compress the Coulomb tensor via tensor hypercontraction (THC) for qubitized walk operators.
- Stage 2: Syndrome Extraction & Threshold Scaling in Stim — Sample stabilizer circuits at physical gate error p_phys = 10⁻³ against threshold p_th = 10⁻², achieving per-round suppression factor (p_phys / p_th) = 0.10.
- Stage 3: Code Distance Selection for Deep Toffoli Circuits — Choose odd code distance d = 27 so the exponent (d+1)/2 = 14 drives P_L = 0.03 × 10⁻¹⁴ = 3.00 × 10⁻¹⁶ below the 10⁻¹² deep-circuit survival ceiling.
- Stage 4: Active-Volume Tile & Magic-State Footprint — Sum 114 logical data/routing tiles and 180 magic-state distillation tiles (294 tiles × 2d² = 428,652 physical qubits).

## 4. Certified Reference Telemetry (T0/T1)
- **Logical Error / Round P_L**: `3.00 × 10⁻¹⁶ (at d = 27, p = 0.001)`
- **Active-Volume Logical Tiles**: `294 tiles (114 data + 180 factory)`
- **Total Physical Qubit Footprint**: `428,652 physical qubits`
- **XPRIZE / QEC Threshold Verdict**: `PASS · FAULT-TOLERANT REGIME`

## 5. Exact T0–T3 Truth Boundary
### Certified in Repository Today (T0/T1)
- Zero-dependency surface-code threshold and FeMoCo active-volume resource estimator in bounties/bounty_p1_surface_code_femoco.py (< 0.05s runtime).
- Exact verification of Fowler et al. (2012) asymptotic logical error scaling and Reiher et al. (2017) / THC logical tile counts.
- Ready for immediate submission as an open educational and resource-estimation benchmark on Unitary Foundation's Metriq.info registry.

### Open Global Prize Horizon (T2/T3)
- XPRIZE Quantum Applications ($5M purse): Requires formal team registration and a novel quantum algorithm paper reducing logical T-count or qubit footprint beyond state-of-the-art THC/qDRIFT baselines.
- Unitary Foundation unitaryHACK Cash Bounties: Awarded during the annual hackathon window for merged pull requests resolving tagged issues in Stim, PySCF, Mitiq, PennyLane, or Qiskit.
