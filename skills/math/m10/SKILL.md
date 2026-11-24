---
name: persistent-homology-betti-percolation
description: Explanatory algebraic-topology companion for Alpha and Vietoris-Rips simplicial filtrations, Z_2 boundary reduction, persistence barcodes, bottleneck stability, and micro-CT pore-scale persistence. Explanation only, not a structural, hydrological, or clinical design method; no folio number may be used on a real structure or patient sample.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Persistent Homology, Vietoris–Rips Simplicial Filtrations, Betti Barcodes & Topological Percolation Thresholds in Disordered Media (Folio M.10)

A plain-text companion to the essay at https://informatico.ai/math/m10/ (`M.10 · Persistent Homology & Topological Persistence Barcodes`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`∂_{k−1} ∘ ∂_k = 0 · β_k^{i,j} = rank(H_k(K_i) → H_k(K_j)) · d_B(D(f), D(g)) ≤ ||f − g||_∞`

## Rules the essay derives
1. Explanation only, not a structural, hydrological, or clinical design method: none of this folio's illustrative numbers (65 nm, beta_0 = 1, beta_1 = 3, chi = -2, 38-116 nm) may be used on a real structure, foundation, or patient sample; check chain nilpotency partial_{k-1} o partial_k = 0 and truncate chi = sum_{k>=0} (-1)^k |K^(k)| = sum_{k>=0} (-1)^k beta_k to beta_0 - beta_1 + beta_2 only if beta_k = 0 for k >= 3 (DOI 10.1007/s00454-002-2885-2).
2. Apply diagonal separation d_i - b_i > 2*delta under tame bottleneck stability d_B(D(f), D(g)) <= ||f - g||_inf <= delta only in matching units (DOI 10.1007/s00454-006-1276-5), account for diameter t = 2*epsilon vs. ball-radius epsilon conventions in Vietoris-Rips software (DOI 10.1090/S0273-0979-09-01249-X; DOI 10.1007/s41468-021-00071-5), and do not equate a dimensionless slider (sigma = 0.08) to a nanometer bound.
3. Distinguish Robins et al. (2016, DOI 10.1002/2015WR017937) persistence on bead, sand, sandstone, and limestone micro-CT images from untested biological gel proposals, note that charge and binding could also block particles, and state when readouts are fixed illustrative text.

## How it works, in four stages
- Stage 1 (Alpha & Vietoris–Rips Filtrations): 3D alpha filtrations (Edelsbrunner, Letscher & Zomorodian 2002, DOI 10.1007/s00454-002-2885-2) and Vietoris–Rips cliques (indexed by diameter ||x_a − x_b|| ≤ t in Carlsson 2009, DOI 10.1090/S0273-0979-09-01249-X and Bauer 2021, DOI 10.1007/s41468-021-00071-5, so t = 2ε under ball radius ε) build nested complexes.
- Stage 2 (Chain Nilpotency & Z_2 Pairing, DOI 10.1007/s00454-002-2885-2): ∂_{k−1} ∘ ∂_k = 0 gives H_k = ker(∂_k)/im(∂_{k+1}) and pairs cycle births b_i with bounding deaths d_i. Explanation only, not a structural or clinical design method.
- Stage 3 (Bottleneck Stability, DOI 10.1007/s00454-006-1276-5): Cohen-Steiner, Edelsbrunner & Harer bound d_B(D(f), D(g)) ≤ ||f − g||_∞ for tame functions; under uniform bound δ in matching units, bars with d_i − b_i > 2δ stay off b = d (σ = 0.08 is a dimensionless slider setting).
- Stage 4 (Micro-CT Persistence Reference, DOI 10.1002/2015WR017937): Robins et al. (2016) relate persistence on bead, sand, sandstone, and limestone micro-CT images to pore-size distributions and percolating sphere radius ([38, 116] nm is fixed illustrative text; chemistry and binding also affect transport).

## Reference values stated in the essay
- **Betti Numbers (β_0, β_1, β_2, model)**: `β₀ = 1 · β₁ = 3 · β₂ = 0 (Fixed 7-Vertex 2-Skeleton)`
- **Euler–Poincaré Invariant (χ, model)**: `χ = 7 − 10 + 1 = −2 (Fixed Illustrative Text)`
- **Longest H_1 Bar Death Scale (model)**: `116 nm on [38, 116] nm (Fixed Illustrative Text)`
- **M.10 Model Boundary**: `EXPLANATORY MODEL · NOT A DESIGN METHOD`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1007/s00454-002-2885-2 (Scite report: https://scite.ai/reports/10.1007/s00454-002-2885-2)
- What the essay compares against: Abstract 7-vertex flag 2-skeleton (|V|=7, |E|=10, |F|=1): β_0=1, β_1=3, χ=−2 · H_1 [38, 116] nm (fixed illustrative)

## Recent research context
- **Persistent Homology, Bottleneck Stability & Percolating Sphere Scales in Micro-CT Porous Media**: Synthesizing Folios E.01, P.03, and M.05, Edelsbrunner, Letscher, and Zomorodian's alpha-complex persistence (DOI 10.1007/s00454-002-2885-2) pairs cycle births and deaths across scales, while Robins et al. (2016, DOI 10.1002/2015WR017937) relate micro-CT persistence in bead, sand, and rock scans to percolating sphere radii.
