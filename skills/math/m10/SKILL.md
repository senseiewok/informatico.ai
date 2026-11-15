---
name: persistent-homology-betti-percolation
description: AI-agnostic algebraic-topology and porous-media skill for Vietoris-Rips/Alpha simplicial filtrations, boundary matrix reduction (partial_{k-1} o partial_k = 0), Betti persistence barcodes, and percolation throat sizing.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Persistent Homology, Vietoris–Rips Simplicial Filtrations, Betti Barcodes & Topological Percolation Thresholds in Disordered Media (Folio M.10)

A plain-text companion to the essay at https://informatico.ai/math/m10/ (`M.10 · Persistent Homology & Topological Percolation Barcodes`, `REV 1.1`, redated `2026-11-14`).

## The governing relation
`∂_{k−1} ∘ ∂_k = 0 · β_k^{i,j} = rank(H_k(K_i) → H_k(K_j)) · d_B(D(f), D(g)) ≤ ||f − g||_∞`

## Rules the essay derives
1. Verify the fundamental chain-complex identity partial_{k-1} * partial_k = 0 and Euler-Poincare invariant chi = sum_k (-1)^k |K^(k)| = sum_k (-1)^k beta_k.
2. Filter out topological noise features with persistence lifetime (d_i - b_i) <= 2 * sigma_noise under the Cohen-Steiner Bottleneck Stability bound.
3. Compare the birth/death scale of the dominant H_1 / H_2 cycle with a particle diameter only as a first geometric screen, and state that transport also depends on chemistry and binding.

## How it works, in four stages
- Stage 1 (Vietoris–Rips Simplicial Filtration K_ε, Continuing M.05): Grows balls of radius ε around 3D pore/mucin nodes, adding edges, triangles, and tetrahedra as pairwise distances cross 2ε.
- Stage 2 (Chain Complex & Z_2 Boundary Reduction ∂_{k−1} ∘ ∂_k = 0, DOI 10.1007/s00454-002-2885-2): Reduces boundary matrices to pair each k-cycle birth b_i with its bounding (k+1)-simplex death d_i.
- Stage 3 (Cohen-Steiner Bottleneck Stability): By the stability theorem of Cohen-Steiner, Edelsbrunner & Harer, a perturbation moves persistence points by at most d_B ≤ ||f − g||_∞, so short bars near the diagonal can be read as noise and long bars as structure. σ_noise = 0.08 is the model setting.
- Stage 4 (Pore-Throat Reading, Completing E.01 & P.03): In the synthetic model the longest H_1 interval is [38 nm, 116 nm]. Robins et al. (2016) relate persistence features of this kind to percolating length scales in micro-CT images of porous materials. Whether a given particle passes through a real mesh also depends on chemistry and binding, which topology alone does not settle.

## Reference values stated in the essay
- **Betti Numbers (β_0, β_1, β_2, model)**: `β₀ = 1 · β₁ = 3 · β₂ = 0`
- **Euler–Poincaré Invariant (χ)**: `χ = β₀ − β₁ + β₂ = −2`
- **Longest H_1 Bar Death Scale (model)**: `116 nm (synthetic point cloud)`
- **Model Reading**: `Long bar stands out from noise (not a measurement)`

## What is and is not checked
The reference values above are stated in the essay. No script in this repository recomputes them yet, so treat them as the essay's claims and check them against the primary source before relying on them.

## Primary source
- https://doi.org/10.1007/s00454-002-2885-2 (Scite report: https://scite.ai/reports/10.1007/s00454-002-2885-2)
- What the essay compares against: Synthetic model: ε = 65 nm · β_0 = 1, β_1 = 3, χ = −2 · longest H_1 bar ends at 116 nm (illustrative)

## Recent research context
- **Persistent Homology & Betti Barcodes as a Way to Read Pore Scales in 3D Porous Media**: Closing the 40-Folio arc back to Folio E.01's continuum percolation and Folio P.03's mucin hydrogels, Edelsbrunner, Letscher & Zomorodian's persistent homology (Discrete Comput. Geom. DOI 10.1007/s00454-002-2885-2) tracks Vietoris–Rips H_0/H_1/H_2 Betti barcodes across filtration scales; this folio shows the idea on a synthetic model.
