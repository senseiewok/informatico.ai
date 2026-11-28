---
name: lean4-complexity-mlkem-lattice
description: AI-agnostic formal mathematics and cryptography skill for reading the Lean 4 projects in anthropics/formal-math (zeta23, 3sum-apsp, eth, vp-vnp) by their READMEs and for NIST FIPS 203 ML-KEM Module-LWE parameters.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Public Lean 4 Repositories and NIST FIPS 203 (ML-KEM): What They State, Side by Side (Folio M.12)

A plain-text companion to the essay at https://informatico.ai/math/m12/ (`M.12 · anthropics/formal-math (as stated in its READMEs) & NIST FIPS 203 ML-KEM Lattices`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`b = A s + e (mod q) · q = 3329 · n = 256 · k ∈ {2, 3, 4} (NIST FIPS 203)`

## Rules the essay derives
1. Configure Module-LWE over polynomial ring R_q = Z_q[X]/(X^256 + 1) with prime modulus q = 3329 and module rank k in {2, 3, 4} (ML-KEM-512/768/1024).
2. Take decapsulation failure rates from FIPS 203 Table 1 (2^-138.8, 2^-164.8 and 2^-174.8 for ML-KEM-512/768/1024) and noise widths from Table 2 (eta1 = 3, 2, 2; eta2 = 2) rather than deriving them from a rule of thumb.
3. Before citing a Lean file, check it exists in the repository, and report its README claims as repository statements unless you built it.

## How it works, in four stages
- Stage 1 (Shor's Quantum Period-Finding): Shor's 1994 algorithm would let a large fault-tolerant quantum computer (Folio P.11) find the period r of a^x mod N in time polynomial in log N, which would break RSA and elliptic-curve cryptography. No quantum computer able to do this for cryptographic key sizes has been reported.
- Stage 2 (Module Learning With Errors, NIST FIPS 203 ML-KEM): The public key b = A s + e (mod q = 3329) over the ring R_q = ℤ_q[X]/(X²⁵⁶ + 1) hides the secret s behind small centered binomial noise e. Its security rests on the presumed hardness of module lattice problems; Regev (2009) showed that plain LWE is at least as hard, under a quantum reduction, as certain worst-case lattice problems.
- Stage 3 (What anthropics/formal-math says it contains): The README of anthropics/formal-math, read on 2026-11-28, lists four Lean 4 projects: zeta23 (Alpöge–Furman on zeta zeros), 3sum-apsp (Alman–Vassilevska Williams on 3SUM and APSP), eth, described there as an algorithm for counting k-CNF solutions that refutes the Exponential Time Hypothesis, and vp-vnp. This site has not built or checked any of them. Claims about named Lean files in earlier editions are withdrawn.
- Stage 4 (Implementation): open-quantum-safe/liboqs is an open-source library of post-quantum algorithms. Formal proofs about mathematics do not by themselves make an implementation bug-free; verifying cryptographic code is a separate task.

## Reference values stated in the essay
- **ML-KEM-768 Security (FIPS 203)**: `NIST security category 3 (k = 3)`
- **Eight-Square Rank Claim**: `Withdrawn: not verified by this site`
- **formal-math/eth README Statement**: `README read 2026-11-28 states an ETH refutation (not checked here)`
- **ML-KEM-768 Decapsulation Failure**: `2^−164.8 (FIPS 203, Table 1)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1145/1568318.1568324 (Scite report: https://scite.ai/reports/10.1145/1568318.1568324)
- What the essay compares against: ML-KEM-768: k = 3 · q = 3329 · n = 256 · NIST security category 3 · decapsulation failure 2^−164.8 (FIPS 203, Table 1)

## Recent research context
- **Public Lean 4 Repositories and the NIST FIPS 203 Lattice Standard, Side by Side**: A synthesis of Folios M.01 (Wiles, DOI 10.2307/2118559), M.03 (FunSearch, DOI 10.1038/s41586-023-06924-6) and M.06 (Williams, DOI 10.1137/15M1024524), read beside what the README of https://github.com/anthropics/formal-math, read on 2026-11-28, says the repository contains (including a statement, not checked here, that one project refutes ETH) and the ML-KEM standard implemented in https://github.com/open-quantum-safe/liboqs.
