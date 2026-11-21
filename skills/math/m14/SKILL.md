---
name: sphere-packing-cohn-elkies
description: AI-agnostic harmonic analysis and lattice geometry skill for Cohn-Elkies Fourier linear programming bounds, Laguerre-Gaussian radial eigenfunctions, E8 and Leech lattice kissing counts, and open packing gaps.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Sphere Packing in Dimensions 3, 4, 8 & 24: Cohn–Elkies Bounds, Modular Functions & Open Gaps (Folio M.14)

A plain-text companion to the essay at https://informatico.ai/math/m14/ (`M.14 · Sphere Packing, Cohn–Elkies LP & Open Gaps · REV 1.0`, `REV 1.0`, redated `2026-11-21`).

## The governing relation
`Δ_d ≤ Vol(B_d(r_cut/2)) · f(0)/f̂(0) · f(x) ≤ 0 (|x| ≥ r_cut) · f̂(t) ≥ 0 · Δ_8 = π⁴/384 · Δ_24 = π¹²/12!`

## Rules the essay derives
1. Fix the Fourier normalization f_hat(t) = integral f(x) exp(-2*pi*i x.t) dx so the radial eigenfunctions L_k^(d/2 - 1)(2*pi*|x|^2) exp(-pi*|x|^2) carry exact eigenvalue (-1)^k.
2. Check primal non-positivity f(x) <= 0 for |x| >= r_cut algebraically in exact rational arithmetic by checking that every coefficient of the shifted polynomial P(u_cut + w) is <= 0.
3. Distinguish settled kissing numbers from open packing densities: Musin (2008) settled tau_4 = 24 in dimension 4, while optimal sphere packing density Delta_4 >= pi^2/16 remains open.
4. Report asymptotic lower-bound preprints (Campos et al. arXiv:2312.10026; Klartag arXiv:2504.05042) as unrefereed high-dimensional scaling bounds separate from fixed-dimension finite checks.

## How it works, in four stages
- Stage 1 (Lattice Geometry & Kissing Numbers from d = 2 to d = 24): Packing equal spheres in Euclidean space asks what fraction of volume non-overlapping balls can fill. In dimension 2 the hexagonal lattice A_2 fills π/√12 ≈ 0.906900 with 6 neighbors; in dimension 3, Hales et al. (2017, DOI 10.1017/fmp.2017.1) completed the formal Flyspeck check of the Kepler conjecture at π/(3√2) ≈ 0.740480 with 12 neighbors. In dimension 4, the checkerboard lattice D_4 has density π²/16 ≈ 0.616850 and Musin (2008, DOI 10.4007/annals.2008.168.1) settled the kissing number at τ_4 = 24, yet packing optimality in dimension 4 remains open.
- Stage 2 (Cohn–Elkies Fourier Linear Programming Duality): Cohn and Elkies (2003, DOI 10.4007/annals.2003.157.689) showed that any radial Schwartz function f with f(0) = f̂(0) > 0, dual non-negativity f̂(t) ≥ 0 everywhere, and primal non-positivity f(x) ≤ 0 for |x| ≥ r_cut yields an upper bound Δ_d ≤ Vol(B_d(r_cut/2)) · f(0)/f̂(0) via the Poisson summation formula. Writing f in the Fourier eigenbasis ψ_k(x) = L_k^(d/2−1)(2π|x|²) exp(−π|x|²) with exact eigenvalue (−1)^k lets our offline verifier construct rational Laguerre–Gaussian test polynomials whose shifted polynomial P(u_cut + w) has every coefficient ≤ 0.
- Stage 3 (Viazovska’s Modular Magic Functions in d = 8 and d = 24): In 2017, Viazovska (DOI 10.4007/annals.2017.185.3.7) constructed an infinite modular-form eigenfunction matching the E_8 root lattice (τ_8 = 240, Δ_8 = π⁴/384 ≈ 0.253670) with double roots at every non-minimal shell √(2k). Days later, Cohn, Kumar, Miller, Radchenko, and Viazovska (DOI 10.4007/annals.2017.185.3.8) extended the modular construction to the 24-dimensional Leech lattice Λ_24 (Δ_24 = π¹²/12! ≈ 0.001930, τ_24 = 196,560 minimal vectors built from the 759 octads of the extended binary Golay code G_24), and later established universal optimality across radial potentials (2022, DOI 10.4007/annals.2022.196.3.3).
- Stage 4 (Open Hypothesis, Tier T0–T2, and Falsification Condition): Hypothesis (Tier T0–T2): finite-degree Laguerre–Gaussian test functions shrink the Cohn–Elkies upper bound monotonically from degree 3 to degree 5 (0.346486 → 0.303541 in d = 8; 0.087466 → 0.008955 in d = 24; 0.700415 → 0.672477 in d = 4), yet leave a roughly 9.0% gap above D_4 in dimension 4 while recent preprints push high-dimensional lower bounds upward via graph independence (arXiv:2312.10026) and stochastic ellipsoids (arXiv:2504.05042). This polynomial gap hypothesis would be falsified if an explicit non-lattice packing in dimension 4 exceeded π²/16 or if an admissible degree-5 Laguerre polynomial dropped below 0.616850; our deterministic checks inspect finite dimensions only and do not re-derive the asymptotic preprint bounds.

## Reference values stated in the essay
- **Lattice Packing Density (Δ_d)**: `0.253670 (E_8, π^4/384, τ = 240)`
- **Laguerre Cohn–Elkies Bound (M = 5)**: `0.303541 (r_cut = 1.6683, model)`
- **Polynomial-to-Lattice Ratio**: `1.1966x (Viazovska modular limit: 1.0000x)`
- **Dimension Optimality Status**: `E_8 MATCHED BY VIAZOVSKA LP LIMIT (d = 8)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/math/m14/verify_m14_sphere_packing.py
python skills/math/m14/verify_m14_sphere_packing.py --planted-defect
```

## Primary source
- https://doi.org/10.4007/annals.2003.157.689 (Scite report: https://scite.ai/reports/10.4007/annals.2003.157.689)
- What the essay compares against: Offline model values: Δ_8(E_8) = 0.253670 (τ_8 = 240; deg-5 LP 0.303541) · Δ_24(Λ_24) = 0.001930 (τ_24 = 196,560; deg-5 LP 0.008955) · d=4 open gap (0.616850 vs 0.672477)

## Recent research context
- **Cohn–Elkies Fourier Bounds, Viazovska Modular Forms & The Open Dimension-4 Gap**: Why do 8-dimensional E_8 and 24-dimensional Leech lattices lock into optimal sphere packings while dimension 4 remains open? Pairing exact Laguerre–Gaussian Fourier eigenfunctions (Cohn & Elkies 2003, DOI 10.4007/annals.2003.157.689) with Viazovska’s modular functions (DOI 10.4007/annals.2017.185.3.7) separates closed dimensions 8 and 24 from the open 9.02% degree-5 gap in dimension 4.
