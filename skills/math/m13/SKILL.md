---
name: sair-lean-kernel-reduction
description: AI-agnostic formal type-checking and kernel reduction skill for Folio M.13: de Bruijn isolation between elaborator search and kernel Γ ⊢ t : T checking, proof by reflection (Boutin 1997; Grégoire–Leroy 2002), and the binary fast-doubling verifier skills/math/m13/verify_m13_lean_kernel_reduction.py.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# The SAIR Lean Kernel Challenge: Trusted Type-Checking, Reflection & Proof-Term Reduction (Folio M.13)

A plain-text companion to the essay at https://informatico.ai/math/m13/ (`M.13 · SAIR Lean Kernel Challenge & Reflection Reduction (competition.sair.foundation)`, `REV 1.0`, redated `2026-11-15`).

## The governing relation
`Γ ⊢ t : T (de Bruijn kernel isolation) · Binary fast-doubling F_1024 mod (10⁹ + 7) = 754,854,590 in 33 modular muls vs. 1,024 unary steps`

## Rules the essay derives
1. Keep search heuristics, LLM tactic synthesis, and elaborator macros outside the trusted computing base; trust only what passes an explicit, minimal Γ ⊢ t : T kernel checker.
2. Avoid unary Peano O(n) reduction inside kernel conversion checks; replace linear step-by-step witness chains with binary reflection identities F_{2k} = F_k (2 F_{k+1} - F_k) and explicit soundness lemmas.
3. Validate the binary vs. linear equivalence deterministically via python -X utf8 skills/math/m13/verify_m13_lean_kernel_reduction.py and test failure detection with --planted-defect.

## How it works, in four stages
- Stage 1 (de Bruijn Criterion & Kernel Isolation): A proof assistant separates tactic heuristics and neural search in the elaborator from a compact, independent type-checker—the Lean 4 kernel (de Moura & Ullrich 2021, DOI 10.1007/978-3-030-79876-5_37)—so a bug in search cannot sneak an unsound theorem past Γ ⊢ t : T.
- Stage 2 (The Definitional Reduction Bottleneck): Inside a formal kernel, evaluating arithmetic or algebraic normal forms step-by-step on unary Peano natural numbers forces O(n) or O(n²) term traversals, choking the type-checker even when the underlying mathematical argument is sound.
- Stage 3 (Proof by Reflection & Compiled Reduction): Proof by reflection (Boutin 1997, DOI 10.1007/bfb0014565) and compiled strong reduction (Grégoire & Leroy 2002, DOI 10.1145/581478.581501) replace long proof terms with a decision algorithm plus one soundness lemma; binary fast doubling reduces F_1024 mod (10⁹ + 7) = 754,854,590 in 33 multiplications instead of 1,024 sequential steps.
- Stage 4 (The SAIR Lean Kernel Challenge Landscape): On 16 September 2026, XTX Markets concluded the AIMO Prize and directed philanthropy toward Lean FRO ($10M to 2030), the Mathlib Initiative ($10M to 2030), and SAIR competitions including the Lean Kernel Challenge (https://competition.sair.foundation/), targeting high-throughput checking of complex proof terms.

## Reference values stated in the essay
- **Binary Reflection Output (F_1024 mod 1e9+7)**: `754,854,590 (matches linear DP)`
- **Binary Doubling Work vs. Unary Steps**: `33 modular muls vs. 1,024 steps (31.03x)`
- **Fast-Doubling Recursion Tree Depth**: `12 frames (n = 1,024)`
- **Trusted Boundary**: `Kernel checks Γ ⊢ t : T independent of search`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/math/m13/verify_m13_lean_kernel_reduction.py
python skills/math/m13/verify_m13_lean_kernel_reduction.py --planted-defect
```

## Primary source
- https://doi.org/10.1007/978-3-030-79876-5_37 (Scite report: https://scite.ai/reports/10.1007/978-3-030-79876-5_37)
- What the essay compares against: F_1024 mod 1,000,000,007 = 754,854,590 · recursion depth 12 · 33 modular multiplications vs. 1,024 unary steps (31.03x step ratio)

## Recent research context
- **XTX Reallocates AIMO Funding Toward Lean FRO, Mathlib & SAIR Lean Kernel Challenge**: Following XTX Markets’ 16 September 2026 update ending the AIMO Prize, open infrastructure grants prioritize Lean FRO, Mathlib, and SAIR’s Lean Kernel Challenge (https://competition.sair.foundation/), built atop de Moura & Ullrich (2021, DOI 10.1007/978-3-030-79876-5_37).
