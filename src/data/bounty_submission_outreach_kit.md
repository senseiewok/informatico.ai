# Verified Participation Routes & Grand-Challenge Registry (B.01–B.06 · Audited 2026-11-15)

**Status Update (2026-11-15):** Cold-email outreach templates from REV 1.0 have been **retired**. Competition eligibility windows and participation mechanisms for every external prize or open-source project referenced across Folios `B.01–B.06` were audited against official program notices on `2026-11-15`. Informatico.ai is an independent computational research monograph site—not a prize entrant or organizer.

## 1. Current Competition & Participation Status

| Folio | Program / Registry | Status as of 2026-11-15 | Verified Participation Route |
| --- | --- | --- | --- |
| **B.01** | **Erdős Problem #30 ($1,000)** | **OPEN** | Publish a proof or counterexample and record it via [erdosproblems.com/30](https://www.erdosproblems.com/30). |
| **B.01** | **XTX Markets AIMO Prize** | **CLOSED (`2026-09-16`)** | XTX Markets ended the AIMO Prize (`~$1.62M` awarded) and reallocated to Lean FRO (`$10M`), Mathlib (`$10M`), and **SAIR Foundation** research challenges (covered in Folios [`M.13`](../math/m13/), [`M.14`](../math/m14/), [`M.15`](../math/m15/)). |
| **B.02** | **XPRIZE Quantum Applications ($5M)** | **CLOSED to new entrants (`May 2026`)** | Restricted to the 12 Phase I (Dec 2025) and Wildcard (May 2026) finalists. |
| **B.02** | **Unitary Foundation Microgrants & Metriq** | **OPEN (Rolling)** | Submit a rolling microgrant proposal (`<= $4,000`) via [unitary.foundation/grants](https://unitary.foundation/grants/) or log reproducible QEC benchmarks on [metriq.info](https://metriq.info/). *(Note: `unitaryHACK 2026` concluded 3–17 June 2026.)* |
| **B.03** | **XPRIZE Carbon Removal ($100M)** | **CONCLUDED (`Apr 2025`)** | Winners announced (Mati Carbon `$50M`, NetZero `$15M`, Vaulted Deep `$8M`, UNDO `$5M`); archived reference only. |
| **B.03** | **IStructE Structural Awards** | **COMMISSIONED BUILDINGS ONLY** | Annual awards judge completed, physically constructed works; theoretical slab studies are ineligible. |
| **B.04** | **Holcim Foundation Awards (8th Cycle)** | **CONCLUDED (`Feb / Nov 2025`)** | 8th cycle closed Feb 2025 and named winners in Venice (Nov 2025); accepts commissioned construction/concepts during active cycles only. |
| **B.04** | **Global Cooling Prize ($3M)** | **CONCLUDED (`2021`)** | Competition ended in 2021; archived reference only. |
| **B.05** | **SRBench / PySR / PySINDy / Dedalus** | **OPEN-SOURCE (No Cash Purse)** | Submit reproducible benchmarks or pull requests via upstream GitHub repositories ([PySR](https://github.com/MilesCranmer/PySR), [PySINDy](https://github.com/dynamicslab/pysindy), [Dedalus](https://github.com/DedalusProject/dedalus)). |
| **B.06** | **HEPLean / PhysLean + ITensors.jl + NetKet** | **OPEN-SOURCE (Active PRs, No Cash Purse)** | Contribute reviewed Lean 4 pull requests directly to [HEPLean/PhysLean](https://github.com/HEPLean/PhysLean). |

## 2. XTX-Funded Successor Mathematics Challenges (Folios M.13–M.15)

Following XTX Markets' `2026-09-16` announcement ending the AIMO Prize, XTX-supported research challenges hosted through the **SAIR Foundation** ([competition.sair.foundation](https://competition.sair.foundation/)) are covered as full Mathematics Pillar Folios in Volume VII:

1. **Folio M.13 — SAIR Lean Kernel Challenge** (`/math/m13/`): Kernel vs. elaboration separation (`de Bruijn` trusted computing base, definitional reduction performance) backed by `skills/math/m13/verify_m13_lean_kernel_reduction.py`.
2. **Folio M.14 — SAIR Andrews–Curtis Conjecture Challenge** (`/math/m14/`): Free-group Nielsen/AC moves on balanced presentations (`AK(2)` vs. `AK(3)` Akbulut–Kirby series) backed by `skills/math/m14/verify_m14_andrews_curtis_moves.py`.
3. **Folio M.15 — SAIR Inverse Galois Problem Challenge (`IGP24`)** (`/math/m15/`): Polynomial realization of finite groups over $\mathbb{Q}$ (`Dedekind` cycle-type sampling and Chebotarev density) backed by `skills/math/m15/verify_m15_inverse_galois_dedekind.py`.

---

*Reproducible harnesses across `B.01–B.06` remain runnable locally via `python -X utf8 bounties/run_all_bounties.py`.*
