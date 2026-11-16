---
name: sair-andrews-curtis-moves
description: AI-agnostic combinatorial group theory skill for Folio M.14: Andrews–Curtis equivalence moves in free groups ⟨x, y⟩, Akbulut–Kirby AK(n) benchmark presentations, and explicit replay via skills/math/m14/verify_m14_andrews_curtis_moves.py.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# The Andrews–Curtis Conjecture & SAIR Challenge: Balanced Presentations, 4-Manifold Handles & Akbulut–Kirby Pairs (Folio M.14)

A plain-text companion to the essay at https://informatico.ai/math/m14/ (`M.14 · Andrews–Curtis Conjecture & SAIR Search Challenge (competition.sair.foundation)`, `REV 1.0`, redated `2026-11-15`).

## The governing relation
`AC moves {r_i ↦ r_i⁻¹, r_i ↦ r_i r_j (i≠j), r_i ↦ w r_i w⁻¹} · AK(2) = ⟨x, y | x y x = y x y, x² = y³⟩ (length 11) collapses to ⟨x, y | x, y⟩ (length 2) in 23 moves`

## Rules the essay derives
1. Allow strictly the three Andrews–Curtis operations: relator inversion r_i -> r_i^-1, relator multiplication r_i -> r_i r_j (i != j), and free-group conjugation r_i -> w r_i w^-1; never insert extra generators.
2. Maintain free-group cancellation g g^-1 -> eps at every multiplication and conjugation seam, and evaluate candidate reductions without assuming greedy length monotonicity.
3. Verify the explicit 23-move AK(2) trivialization trace offline with python -X utf8 skills/math/m14/verify_m14_andrews_curtis_moves.py and check --planted-defect detection.

## How it works, in four stages
- Stage 1 (Andrews & Curtis 1965): J. J. Andrews and M. L. Curtis (Proc. AMS, DOI 10.2307/2033843) asked whether every balanced finite presentation of the trivial group can be reduced to the empty identity ⟨x_1, …, x_n | x_1, …, x_n⟩ using only relator inversion, relator multiplication (i ≠ j), and free-group conjugation—excluding stabilization by extra generator/relator pairs.
- Stage 2 (4-Manifold Topology & Akbulut–Kirby Pairs): Selman Akbulut and Robion Kirby (Topology 1985, DOI 10.1016/0040-9383(85)90010-2) constructed infinite families such as AK(n) = ⟨x, y | x y x = y x y, xⁿ = yⁿ⁺¹⟩ arising from 4-manifold handleslides, generating classic stress tests for combinatorial search.
- Stage 3 (Non-Monotonic Search Landscapes & AK(2) Trace): Even simple trivializations are non-monotonic. Running skills/math/m14/verify_m14_andrews_curtis_moves.py replays 23 elementary AC moves on AK(2), temporarily swelling total relator length from 11 up to 14 before collapsing cleanly to ⟨x, y | x, y⟩ (length 2).
- Stage 4 (AI Search & SAIR Challenge): Deep reinforcement learning and discrete search methods (Gukov et al. 2021, DOI 10.1088/2632-2153/abe91f) explore super-exponential AC move graphs; the SAIR Andrews–Curtis Conjecture Challenge (https://competition.sair.foundation/) benchmarks open search algorithms on harder balanced presentations.

## Reference values stated in the essay
- **AK(2) Initial → Peak → Final Length**: `11 → 14 → 2 (⟨x, y | x, y⟩)`
- **Elementary AC Moves Replayed (AK(2))**: `23 valid free-group moves`
- **AK(3) Initial Length & |det(Ab)|**: `13 symbols · |det| = 1 (trivial Z⁰)`
- **Conjecture Open Status**: `Open since 1965 (stable AC uses Tietze add)`

## Check it yourself
This skill ships a verifier that recomputes its values. Its planted-defect mode must fail:

```
python skills/math/m14/verify_m14_andrews_curtis_moves.py
python skills/math/m14/verify_m14_andrews_curtis_moves.py --planted-defect
```

## Primary source
- https://doi.org/10.2307/2033843 (Scite report: https://scite.ai/reports/10.2307/2033843)
- What the essay compares against: AK(2) total length 11 → trivial length 2 in 23 AC moves (peak intermediate length 14); AK(3) starts at length 13 with |det| = 1 trivial abelianization

## Recent research context
- **Andrews–Curtis Search Challenge Tests Non-Monotonic Free-Group Planners**: Originating in Andrews & Curtis (1965, DOI 10.2307/2033843) and Akbulut & Kirby (1985, DOI 10.1016/0040-9383(85)90010-2), balanced group trivializations become a clean open benchmark at SAIR (https://competition.sair.foundation/).
