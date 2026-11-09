---
name: timegravity-t10-page-curve
description: Rebuild and verify the Time & Gravity T.10 toy - Page's counting argument on ten qubits: Haar-random pure states whose radiation entropy matches Page's closed form S(m,n) = sum_{k=n+1}^{mn} 1/k - (m-1)/(2n) at every cut, turns over at N/2 and falls back, with eigenvalues from a pure-Python Jacobi solver - whose planted defect is a non-unitary toy that follows Hawking's line and never turns over.
license: MIT
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Page's Counting Argument (T.10 · Time & Gravity)

> **Fixed Boundary (`EN`):** Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up.
>
> **Frontera Fija (`ES-MX`):** Nada en esta página es una teoría del todo, y este sitio no propone ninguna. Cada afirmación lleva una de seis etiquetas, cada una ligada a una fila del libro de registro: MEDIDO, DERIVADO, COTA, PROPUESTO, ABIERTO o RESULTADO ÚNICO. Las prepublicaciones nunca suben de PROPUESTO. Cada página termina con una pregunta abierta que la siguiente página retoma.

## 1. Page, canonical URL and governing equations
- **Track page**: `T.10` (Time & Gravity, reading order 9 of 9, dated `2026-11-09`). Page labels **DERIVED** and **OPEN**.
- **Canonical URL**: https://informatico.ai/timegravity/t10/ (Spanish: https://informatico.ai/es-mx/timegravity/t10/)
- **Page's formula**: `S(m, n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n)` for `m ≤ n` (nats). Hawking's line: `S = a · ln 2`.
- **Central numbers**: 8 Haar-random pure states on 10 qubits; mean entropy at every cut within `0.03` nats of Page's formula (achieved ≈ 0.002); peak at `a = 5` with `2.97` nats; final `0.69` nats; symmetric about `N/2`.
- **Generator**: `python skills/timegravity/t10/make_t10.py`
- **Verifier**: `python skills/timegravity/t10/verify_t10_page_curve.py`
- **Knockout check**: `python skills/timegravity/t10/verify_t10_page_curve.py --planted-defect` (must exit non-zero: entropies replaced by Hawking's line, never turning over)
- **Label lint**: `python tools/check_timegravity_labels.py` (and `--planted-defect`, `--mutants`)

## 2. Ledger rows this page may cite (timegravity/ledger.json)
| Row | Label | Source | DOI |
| --- | --- | --- | --- |
| `T10-ABBOTT2016` | MEASURED | GW150914, first binary black hole merger | https://doi.org/10.1103/PhysRevLett.116.061102 |
| `T10-ISI2021` | MEASURED (first area-law test; SINGLE RESULT as a test) | Isi et al. 2021 | https://doi.org/10.1103/PhysRevLett.127.011103 |
| `T10-LVK2025` | SINGLE RESULT | GW250114 area law and Kerr test (young) | https://doi.org/10.1103/kw5g-d732 |
| `T10-HAWKING1971` | DERIVED | area theorem | https://doi.org/10.1103/PhysRevLett.26.1344 |
| `T10-BEKENSTEIN1973` | DERIVED | black-hole entropy | https://doi.org/10.1103/PhysRevD.7.2333 |
| `T10-HAWKING1975` | DERIVED | particle creation by black holes | https://doi.org/10.1007/BF02345020 |
| `T10-PAGE1993A` / `T10-PAGE1993B` | DERIVED | average entropy of a subsystem; information in black hole radiation | https://doi.org/10.1103/PhysRevLett.71.1291 · https://doi.org/10.1103/PhysRevLett.71.3743 |
| `T10-PENINGTON2020` / `T10-ALMHEIRI2019` | DERIVED | quantum extremal surfaces, islands | https://doi.org/10.1007/JHEP09(2020)002 · https://doi.org/10.1007/JHEP12(2019)063 |
| `T10-APOLOGIA2025` / `T10-BLINDERS2026` | PROPOSED (preprints) | the island dispute | https://doi.org/10.48550/arXiv.2506.04311 · https://doi.org/10.48550/arXiv.2602.06543 |

## 3. Tool-neutral agent packet and security boundary (`security-runtime`)
1. **Rebuild locally**: `python skills/timegravity/t10/make_t10.py`; standard library only; fixed seed; writes only under `src/research/timegravity/t10/files/`.
2. **Acceptance gate**: `python skills/timegravity/t10/verify_t10_page_curve.py` must print `"status": "PASS"` with `turns_over_at_half: PASS`; `--planted-defect` must exit non-zero. Then `python tools/check_timegravity_labels.py`.
3. **Security boundary (`security-runtime`)**: no shell outside the repository, no home-directory access, no outbound network for this task.

## 4. Deterministic verification and falsification rules
1. At every cut `a = 1..N−1` the sample mean entropy lies within `0.03` nats of `S(2ᵃ, 2^{N−a})`; the assertion is against the closed form, never against the random numbers.
2. The curve is symmetric about `N/2` within `0.06` nats and its last value is below half its peak.
3. Planted defect: entropies replaced by `a · ln 2` (non-unitary, thermal all the way); rule 2 fails and `--planted-defect` exits non-zero.
4. `t10_reference.json` matches `manifest.json` and regenerates byte for byte (fixed seed).

## 5. What the instrument shows (reader side)
- Hawking's straight line and Page's curve for a chosen N, with the 10-qubit toy's dots; the N slider redraws both.
- Knockout: non-unitary evaporation, the line only rises. Second button: Page's formula without its `−(m−1)/2n` correction, to show the naive count's miss.
- Predict before you reveal: where the radiation entropy peaks.

## 6. Exact T0–T3 truth boundary
### In the repository today (T0/T1)
- Kernel functions `page_average_entropy`, `haar_random_state`, `reduced_density_matrix`, `von_neumann_entropy`, `page_curve_toy`, `check_page_curve` in `tools/timegravity_kernel_bounds.py`.

### Not on this page (T2/T3)
- The GW250114 area figure is quoted as the paper's own claim and never recomputed from medians.
- Islands are a derivation inside semiclassical gravity, labelled DERIVED; the mechanism dispute is PROPOSED (preprints); where the information goes in our universe is OPEN.
