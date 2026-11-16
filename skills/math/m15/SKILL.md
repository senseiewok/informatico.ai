---
name: sair-inverse-galois-dedekind
description: AI-agnostic computational number theory skill for Folio M.15: Dedekind Frobenius cycle-type factorization in F_p[x], Chebotarev equidistribution, transitive group identification (Dokchitser 2013; Jones & Roberts 2014; Hulpke 2005), and verifier skills/math/m15/verify_m15_inverse_galois_dedekind.py.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# The Inverse Galois Problem & SAIR IGP24 Challenge: Rational Polynomial Realizations & Dedekind Frobenius Cycles (Folio M.15)

A plain-text companion to the essay at https://informatico.ai/math/m15/ (`M.15 · SAIR Inverse Galois Problem Challenge (IGP24 · competition.sair.foundation)`, `REV 1.0`, redated `2026-11-15`).

## The governing relation
`Gal(f/ℚ) ↪ S_n identified mod p via Frobenius cycle partitions (Dedekind) & Chebotarev density |C|/|G| · Test polynomial f(x) = x⁴ − x − 1 (Δ = −283, Gal = S₄): 13/50 = 0.260 vs. 6/24 = 0.250 4-cycles`

## Rules the essay derives
1. Exclude primes dividing the polynomial discriminant disc(f) before invoking Dedekind’s theorem relating factor degrees in F_p[x] to cycle types in Gal(f/Q).
2. Compute exact Frobenius action via repeated p-th power composition x -> x^p mod (f, p) inside gcd(x^(p^d) - x, f), never linearized exponents p * d.
3. Run python -X utf8 skills/math/m15/verify_m15_inverse_galois_dedekind.py to audit all 50 unramified primes and test failure detection under --planted-defect.

## How it works, in four stages
- Stage 1 (Hilbert–Noether Inverse Galois Problem): Does every finite group G occur as the Galois group Gal(K/ℚ) of some finite Galois extension K over the rational numbers ℚ? While symmetric, alternating, and solvable groups are settled (Shafarevich; Malle & Matzat, DOI 10.1007/978-3-662-55420-3), concrete minimal-degree polynomials for specific transitive subgroups—especially degree-24 benchmarks in SAIR’s IGP24—remain computationally demanding.
- Stage 2 (Discriminant Ramification & Dedekind’s Theorem): Reducing a monic integer polynomial f(x) modulo any prime p not dividing its discriminant yields degrees of irreducible factors in F_p[x] that directly equal the cycle lengths of a genuine Frobenius permutation inside Gal(f/ℚ).
- Stage 3 (Chebotarev Equidistribution & Frobenius Fingerprints): By Chebotarev’s density theorem and Dokchitser & Dokchitser’s invariant-resolvent framework (2013, DOI 10.2140/ant.2013.7.1325), each conjugacy class C ⊂ G occurs across unramified primes in proportion |C| / |G|. For f(x) = x⁴ − x − 1 (Δ = −283), sampling the first 50 unramified primes yields 13 four-cycles (26.0% vs. 6/24 = 25.0%), alongside 3-cycles and transpositions generating S₄.
- Stage 4 (LMFDB, Transitive Group Classification & IGP24): Databases of number fields (Jones & Roberts 2014, DOI 10.1112/s1461157014000424) and Hulpke’s transitive permutation classification (2005, DOI 10.1016/j.jsc.2004.08.002) underpin modern Galois identification; SAIR’s IGP24 (https://competition.sair.foundation/) challenges solvers to construct missing explicit polynomials of degree 24.

## Reference values stated in the essay
- **Sampled Polynomial & Discriminant**: `f(x) = x⁴ − x − 1 (Δ = −283)`
- **Observed 4-Cycle Share vs. Chebotarev**: `13/50 = 26.0% vs. 6/24 = 25.0%`
- **Dedekind Subgroup Identification (50 Primes)**: `All 5 S₄ classes present (order 24)`
- **SAIR IGP24 Benchmark Frontier**: `Explicit polynomials at degree 24 over ℚ`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/math/m15/verify_m15_inverse_galois_dedekind.py
python skills/math/m15/verify_m15_inverse_galois_dedekind.py --planted-defect
```

## Primary source
- https://doi.org/10.2140/ant.2013.7.1325 (Scite report: https://scite.ai/reports/10.2140/ant.2013.7.1325)
- What the essay compares against: x⁴ − x − 1 (disc = −283): 50 unramified primes p ≠ 283 yield (4,)×13, (3,1)×18, (2,1,1)×11, (2,2)×7, (1,1,1,1)×1 → S₄ of order 24 (26.0% vs 25.0% 4-cycles)

## Recent research context
- **SAIR IGP24 Benchmarks Explicit Polynomial Realizations for Degree-24 Galois Groups**: Grounded in Dokchitser & Dokchitser (2013, DOI 10.2140/ant.2013.7.1325), Jones & Roberts (2014, DOI 10.1112/s1461157014000424), Hulpke (2005), and Malle & Matzat (2018), SAIR IGP24 brings finite-field Frobenius diagnostics to degree-24 polynomial synthesis (https://competition.sair.foundation/).
