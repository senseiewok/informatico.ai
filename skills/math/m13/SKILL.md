---
name: shannon-capacity-lovasz-theta
description: AI-agnostic combinatorial information theory skill for Shannon zero-error graph capacity, the Lovasz theta sandwich alpha(G) <= Theta(G) <= vartheta(G) <= chi_bar(G), and Haemers minrank separation.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Shannon Zero-Error Graph Capacity, Lovász Theta Sandwich & the Open Seven-Cycle Gap (Folio M.13)

A plain-text companion to the essay at https://informatico.ai/math/m13/ (`M.13 · Zero-Error Capacity & Lovász Theta Sandwich · REV 1.0`, `REV 1.0`, redated `2026-11-21`).

## The governing relation
`α(G) ≤ Θ(G) ≤ ϑ(G) ≤ α*(G) ≤ χ̄(G) · ϑ(C_n) = n cos(π/n) / [1 + cos(π/n)]`

## Rules the essay derives
1. Model zero-error k-symbol block codes as independent sets in the strong product G^{oxtimes k}, never the Cartesian box product, so symbol confusability across simultaneous coordinates is captured.
2. Enforce the Lovasz sandwich alpha(G) <= Theta(G) <= vartheta(G) <= alpha*(G) <= chi_bar(G) and compute odd-cycle theta values via n * cos(pi/n) / (1 + cos(pi/n)).
3. Never treat vartheta(G) as equal to Theta(G) in general: check algebraic minrank bounds such as Haemers rank(A(S_bar) - I) = 7 < 9 = vartheta(S_bar) on the 27-vertex Schlafli complement.
4. Keep Theta(C_7) explicitly labeled OPEN between the verified lower floor 367^(1/5) (~3.257866) and the Lovasz upper bound vartheta(C_7) (~3.317667).

## How it works, in four stages
- Stage 1 (Confusability Graphs and Strong Products, Shannon 1956): Claude Shannon (DOI 10.1109/TIT.1956.1056798) modeled a noisy discrete channel as a graph G whose vertices are input letters and whose edges connect pairs that can produce the same output. Zero-error words of length k form an independent set in the k-fold strong product G^k, yielding Θ(G) = sup_k α(G^k)^(1/k). For C_5, α(C_5) = 2, whereas the five pairs (i, 2i mod 5) form an independent set in C_5^2, giving Θ(C_5) ≥ √5.
- Stage 2 (Lovász Orthonormal Umbrellas and Sandwich Inequality, 1979): László Lovász (DOI 10.1109/TIT.1979.1055985) defined ϑ(G) by placing unit vectors u_i in Euclidean space so non-adjacent vertices are orthogonal, minimizing max_i 1/(c · u_i)^2 over unit handles c. Because ϑ is multiplicative under strong products, α(G) ≤ Θ(G) ≤ ϑ(G) ≤ α*(G) ≤ χ̄(G). On odd cycles, ϑ(C_n) = n cos(π/n) / [1 + cos(π/n)], pinning Θ(C_5) = √5 ≈ 2.236068 via the 3D umbrella cos²φ = 1/√5.
- Stage 3 (Haemers Minrank Separation on the Schläfli Complement, 1979): Willem Haemers (DOI 10.1109/TIT.1979.1056027) bounded Θ(G) above by the minimum rank of any matrix fitting G over a field. On the 27-line cubic-surface intersection graph S_bar = SRG(27, 10, 1, 5), spectrum {10^1, 1^20, (-5)^6} gives ϑ(S_bar) = 9, whereas A(S_bar) − I fits S_bar with exact rational rank 7. Thus Θ(S_bar) ≤ 7 < 9, and the diagonal in S ⊠ S_bar shows Θ(S ⊠ S_bar) ≥ 27 > 3 × 7 ≥ Θ(S) Θ(S_bar).
- Stage 4 (Open Hypothesis on C_7, Tier T0–T1 Bounds, and Falsification Condition): For the seven-cycle C_7, Polak & Schrijver (2019, DOI 10.1016/j.ipl.2018.11.006) found 367 independent vertices in C_7^5, establishing Tier T0/T1 bounds 367^(1/5) ≈ 3.257866 ≤ Θ(C_7) ≤ ϑ(C_7) ≈ 3.317667. Whether Θ(C_7) equals ϑ(C_7) or stays strictly below it remains OPEN. Any strict algebraic upper bound below 3.317667 refutes equality Θ(C_7) = ϑ(C_7), while any block code with α(C_7^k)^(1/k) > 3.257866 tightens the lower floor.

## Reference values stated in the essay
- **Lovász Theta Upper Bound ϑ(C_n)**: `2.236068 (closed Θ(C_5) = √5)`
- **Best Block-k Rate α(C_n^k)^(1/k)**: `2.236068 at n = 5, k = 2`
- **Sandwich: α · ϑ · α* · χ̄**: `2 ≤ 2.2361 ≤ 2.500 ≤ 3`
- **Open Capacity Gap ϑ − Rate**: `0.000000 (CLOSED ON C_5)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/math/m13/verify_m13_shannon_capacity.py
python skills/math/m13/verify_m13_shannon_capacity.py --planted-defect
```

## Primary source
- https://doi.org/10.1109/TIT.1979.1055985 (Scite report: https://scite.ai/reports/10.1109/TIT.1979.1055985)
- What the essay compares against: C_5 (k = 2): α = 2 · Θ(C_5) = ϑ(C_5) = √5 ≈ 2.236068 · C_7 (k = 5): 367^(1/5) ≈ 3.257866 ≤ Θ(C_7) ≤ ϑ(C_7) ≈ 3.317667 (OPEN)

## Recent research context
- **Lovász's Theta Sandwich, Haemers's Rank Barrier & the Open Seven-Cycle Capacity Gap**: Pairing two symbols lets five error-free codewords pack into a five-cycle, closing Θ(C_5) = √5 via Lovász's 1979 orthonormal umbrella (DOI 10.1109/TIT.1979.1055985). Yet Haemers's rank-7 bound on the 27-vertex Schläfli complement (DOI 10.1109/TIT.1979.1056027) separates capacity from theta, and on C_7 the gap [3.257866, 3.317667] (Polak & Schrijver 2019, DOI 10.1016/j.ipl.2018.11.006) stays open.
