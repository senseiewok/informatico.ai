---
name: fine-grained-prm
description: AI-agnostic skill for fine-grained complexity reductions (3SUM/APSP/OV) and step-level process reward verification.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Sub-Cubic Fine-Grained Reductions (3SUM → APSP) and Step-Level Process Supervision (PRM800K) (Folio M.06)

A plain-text companion to the essay at https://informatico.ai/math/m06/ (`M.06 · Fine-Grained Complexity & PRM`, `REV 1.2`, redated `2026-11-14`).

## The governing relation
`O(n³ / 2^(Ω(√log n))) APSP (randomized) · Step-Level PRM`

## Rules the essay derives
1. Do not present the n^3/2^(Ω(√log n)) APSP bound as a practical speedup: it is an asymptotic result with an unspecified constant, and no speedup at a given n follows from it.
2. Check each intermediate reasoning step with an exact checker where one exists, and say when a step score is only a model estimate.
3. State fine-grained hypotheses (3SUM, APSP, SETH, ETH) as conjectures, and report a claim that refutes one as the claim of its source, not as established.

## How it works, in four stages
- Stage 1 (Min-Plus Distance Product): Formulates All-Pairs Shortest Paths as (A ⋆ B)_{ij} = min_k (A_{ik} + B_{kj}) over n = 4,096 vertices.
- Stage 2 (Razborov-Smolensky Polynomial Batching): Williams uses Razborov-Smolensky polynomials over F_2 to reduce a min-plus product to a relatively small number of rectangular matrix products (SIAM J. Comput. 2018, abstract).
- Stage 3 (Step-Level Scoring): A process reward model scores each step of a solution. Lightman et al. report that process supervision significantly outperformed outcome supervision on problems from the MATH dataset (arXiv:2305.20050).
- Stage 4 (Illustrative Numbers): The figures on this page are illustrative. A cubic count at n = 4,096 is 4,096³ = 6.87 × 10^10 operations; 14.8 is an assumed divisor that no theorem implies. A 20-step chain whose validity is the product of per-step probabilities gives 0.9566^20 ≈ 41.2% and 0.99723^20 ≈ 94.6%. None of these is a measured result.

## Reference values stated in the essay
- **Assumed Speedup Divisor**: `14.8× at n = 4,096 (assumed, illustrative)`
- **20-Step Chain Validity (model)**: `94.6% vs 41.2% (from assumed per-step probabilities 0.99723 and 0.9566)`
- **ETH Status (see M.01)**: `formal-math eth README states it refutes ETH (not checked here)`
- **Verification Status**: `nothing verified by this site`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1137/15M1024524 (Scite report: https://scite.ai/reports/10.1137/15M1024524)
- What the essay compares against: SIAM 10.1137/15M1024524 · PRM800K (arXiv:2305.20050)

## Recent research context
- **Williams's APSP Algorithm, a Repository's Statement on 3SUM and APSP, and Step-Level Process Supervision**: Ryan Williams's randomized All-Pairs Shortest Paths algorithm runs in time n^3 / 2^(Ω(√log n)) (SIAM J. Comput. DOI 10.1137/15M1024524). The README of anthropics/formal-math lists a 3sum-apsp project whose stated result, by Alman and Vassilevska Williams (arXiv:2610.06783), is a polynomial saving for 3SUM and APSP. Lightman et al. (PRM800K, arXiv:2305.20050) report that step-level process supervision outperformed outcome supervision on MATH problems. This site reports these results and has not checked the repository or the preprint.
