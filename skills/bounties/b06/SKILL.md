---
name: bounty-b06-physlean-itensor-quantum-gauge
description: Deterministic verification harness, 4-stage proof spine, and T0-T3 truth boundary for B.06 (BOUNTY-M2): Machine-Checked Gauge Physics in PhysLean & Tensor-Network Quantum Criticality (ITensors.jl + NetKet).
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Machine-Checked Gauge Physics in PhysLean & Tensor-Network Quantum Criticality (ITensors.jl + NetKet) (B.06 · BOUNTY-M2)

## 1. Governing Law, Prize Registry & Canonical URL
- **Bounty Folio**: `B.06` (`BOUNTY-M2` · `REV 1.2`, Redated `2026-11-08`)
- **Canonical URL**: https://informatico.ai/bounties/b06/ (Spanish: https://informatico.ai/es-mx/bounties/b06/)
- **Prize / Challenge**: BOUNTY B.06 (M-2) · PHYSLEAN + ITENSORS.JL + NETKET
- **Official Registry**: [HEPLean/PhysLean (Lean 4 Physics)](https://github.com/HEPLean/PhysLean)
- **Governing Equation**: `Tr[Y] = Tr[Y³] = Tr[τ²Y] = Tr[λ²Y] = 0 · S_vN(L) = (c/6) ln(L) + s_1 = 0.8828 ≤ ln(χ = 64) = 4.1589`
- **Primary Verification Harness**: `python bounties/bounty_m2_physlean_itensor_quantum_gauge.py`
- **Primary Scite Anchor DOI**: https://doi.org/10.1016/j.cpc.2024.109457 (Scite Report: https://scite.ai/reports/10.1016/j.cpc.2024.109457)

## 2. Deterministic Verification & Falsification Rules
1. Standard Model Gauge Anomaly Cancellation: All four chiral trace invariants (gravitational Tr[Y], cubic U(1)_Y³ Tr[Y³], weak mixed Tr[τ²Y], and colour mixed Tr[λ²Y]) must vanish identically (|Tr| < 10⁻¹²); any hypercharge drift δY ≠ 0 breaks quantum gauge invariance.
2. Calabrese–Cardy Entanglement Bound: To faithfully represent the critical Ising ground state at chain length L = 128 (c = 0.5, S_vN = 0.882836 nats), the MPS bond dimension must satisfy ln(χ) ≥ S_vN(L), i.e., χ ≥ 3.
3. Pfeuty Ground-State Energy Invariant: Critical TFIM energy per site at g = J = 1 must equal -4/π = -1.27323954.

## 3. 4-Stage Formal Proof & Benchmark Mechanism
- Stage 1: Weyl Multiplet Assignment in PhysLean — Declare the five chiral SU(3)_C × SU(2)_L × U(1)_Y representations per generation: Q_L(3,2,1/6), u_R^c(3,1,-2/3), d_R^c(3,1,1/3), L_L(1,2,-1/2), e_R^c(1,1,1).
- Stage 2: Four-Trace Gauge Anomaly Cancellation — Verify Tr[Y] = 0, Tr[Y³] = 0, Tr[τ²Y] = 0, and Tr[λ²Y] = 0 to machine precision (and exactly over ℚ in Lean 4).
- Stage 3: Exact Pfeuty & Calabrese–Cardy Critical Scaling — Evaluate 1D critical Transverse-Field Ising ground-state energy density E₀/N = -4/π = -1.27323954 and entanglement entropy S_vN(L=128) = (0.5/6) ln(128) + 0.4785 = 0.882836 nats.
- Stage 4: MPS Bond-Dimension Capacity Certification — Confirm that MPS bond capacity ln(χ) = ln(64) = 4.158883 nats strictly bounds S_vN(128) = 0.882836 nats.

## 4. Certified Reference Telemetry (T0/T1)
- **PhysLean Cubic Trace Tr[Y³]**: `0.000000000000 (Anomaly-Free)`
- **Critical TFIM Energy E₀ / N**: `−1.27323954 (−4 / π exact)`
- **CFT Entanglement S_vN(128)**: `0.8828 nats ≤ ln(χ) = 4.1589`
- **Verifier Verdict (Worked Example)**: `PASS · ANOMALY-FREE & AREA-LAW`

## 5. Exact T0–T3 Truth Boundary
### Certified in Repository Today (T0/T1)
- Deterministic Standard Model four-trace anomaly verifier and 1D critical TFIM entanglement harness in bounties/bounty_m2_physlean_itensor_quantum_gauge.py (< 0.05s runtime).
- Cross-checked against Tooby-Smith (2024, DOI 10.1016/j.cpc.2024.109457), Fishman et al. (2022, DOI 10.21468/SciPostPhysCodeb.4), and Vicentini et al. (2022, DOI 10.21468/SciPostPhysCodeb.7).
- Ready for immediate community showcase submission to HEPLean/PhysLean Zulip and ITensors / NetKet showcases.

### Open Global Prize Horizon (T2/T3)
- HEPLean / PhysLean open formalization work (no cash prize is named here): submitting 0-sorry Lean 4 pull requests formalizing renormalization group flows, lattice gauge bounds, or BSM anomaly classification directly in HEPLean/PhysLean.
