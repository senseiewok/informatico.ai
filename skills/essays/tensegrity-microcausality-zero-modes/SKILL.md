---
name: essay-es04-tensegrity-microcausality-zero-modes
description: Verify Cross-Scale Essay ES.04 (Tensegrity, Microcausality, and Zero Modes) on Informatico.ai - uniting the Maxwell-Calladine 3D space-frame rigidity matrix R in R^{E x (3V - 6)} and the explicit 54 x 15 real normalizer-commutator matrix C_loc on su(4) through the exact rank-nullity index theorem dim ker C - dim coker C = D - E, locking 2-mass BMV negativity at 0.078162 - with a --planted-defect knockout check.
license: CC0-1.0
compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)
---
# Tensegrity, Microcausality, and Zero Modes (ES.04 · Cross-Scale Essay)

> **Non-Clinical & Epistemic Scope Boundary (`EN`):** Essay `ES.04` compares exact linear-algebraic rank–nullity constraints across 3D pin-jointed trusses, fixed-slice quantum subsystem algebras on `su(4)`, and `10 nm` multi-domain ABC transporter protein frames. Mechanical coordinates (`3V - 6`) and Lie-algebra dimensions (`dim su(4) = 15`) live on distinct vector spaces and are never conflated. Preprint `10.48550/arxiv.2608.16732` (`Stoica 2026`) is explicitly capped at `PROPOSED`. Zero clinical or treatment claims are made.
>
> **Frontera Epistémica y No Clínica (`ES-MX`):** El ensayo `ES.04` compara restricciones exactas de rango-nulidad entre armaduras espaciales 3D, álgebras locales de subsistemas cuánticos en `su(4)` y marcos proteicos multidominio de `10 nm`. Las coordenadas mecánicas (`3V - 6`) y la dimensión del álgebra de Lie (`dim su(4) = 15`) habitan espacios vectoriales distintos y jamás se confunden. La prepublicación `10.48550/arxiv.2608.16732` (`Stoica 2026`) mantiene techo `PROPOSED`. No contiene promesas ni orientación clínica.

## 1. Essay Identity, Canonical URLs, and Module Paths
- **Essay code & slug**: `ES.04` · `tensegrity-microcausality-zero-modes` (dated `2026-11-10`, instrument kind `kinematic`, plate `essay04`)
- **Canonical URL**: https://informatico.ai/essays/tensegrity-microcausality-zero-modes/ (Spanish twin: https://informatico.ai/es-mx/essays/tensegrity-microcausality-zero-modes/)
- **Pure-Python kernel & bilingual monograph**: `tools/folios/essays/e04_tensegrity_microcausality.py`
- **Standalone deterministic verifier**: `python -X utf8 skills/essays/tensegrity-microcausality-zero-modes/verify_essay_tensegrity_microcausality.py`
- **Planted-defect knockout check**: `python -X utf8 skills/essays/tensegrity-microcausality-zero-modes/verify_essay_tensegrity_microcausality.py --planted-defect` (must exit `1`)

## 2. Governing Linear-Algebraic Laws Across Distinct Spaces
1. **Unifying Law — The Fundamental Rank–Nullity Index Theorem**:
   - For any real linear constraint operator `C : R^D -> R^E` of rank `r = rank(C)`:
     `dim ker(C) - dim coker(C) = (D - r) - (E - r) = D - E`.
2. **Map A — 3D Space-Frame Rigidity Matrix `R in R^{E x (3V - 6)}` (`Calladine 1978`; `Pellegrino & Calladine 1986`; `Kane & Lubensky 2014`)**:
   - Quotienting Euclidean nodal displacements `R^{3V}` by the `6`-dimensional rigid-body subspace `se(3)` yields internal dimension `D_mech = 3V - 6` and the Maxwell–Calladine index:
     `N_floppy - N_self_stress = (3V - 6) - E`.
   - **Cubic truss bracing sequence (`V = 8`, `D_mech = 18`)**: Unbraced `E = 12` cube has `rank(R) = 12`, `N_floppy = 6`, `N_self_stress = 0`; adding `6` independent face diagonals (`E = 18`) raises `rank(R)` to `18` (`N_floppy: 6 -> 0`, `N_self_stress = 0`); a `7`th body diagonal (`E = 19`) leaves `rank(R) = 18` and creates `N_self_stress = 1`. Conversely, double-bracing `1` planar face while leaving the opposite face unbraced (`E = 18`) drops `rank(R)` to `17` (`N_floppy = 1`, `N_self_stress = 1`).
   - **Octahedron & Tensegrity 3-Prism (`V = 6`, `E = 12`, `D_mech = 12`)**: Regular convex octahedron has `rank(R) = 12` (`0` floppy, `0` self-stress); the `3`-prism tensegrity simplex drops from `rank(R) = 12` at generic twist (`0.7 rad`) to `rank(R) = 11` at `30 deg` (`pi/6 rad`), creating `N_self_stress = 1` cable-strut prestress alongside `N_floppy = 1` first-order twist mechanism stiffened at quadratic order.
3. **Map B — Explicit `54 x 15` Real Normalizer-Commutator Matrix `C_loc` on `su(4)` (`Bose et al. 2017`; `Marletto & Vedral 2017`)**:
   - Spanning `su(4)` (`D_alg = 15`) by `3` local `A` (`sigma_i x I`), `3` local `B` (`I x sigma_j`), and `9` non-local Cartan–Weyl (`sigma_a x sigma_b`) Pauli pairs, spatial microcausality `[A_A(x), A_B(y)] = 0` demands zero projection of `-i[X, L_m]` (`m = 1..6`) onto all `9` non-local generators (`E_alg = 6 * 9 = 54` rows).
   - Pure-Python Gaussian elimination proves `rank(C_loc) = 9`, `dim ker(C_loc) = 6` (`su(2)_A + su(2)_B`), and `dim coker(C_loc) = 45` (`6 - 45 = 15 - 54 = -39`), collapsing all `9` continuous non-local refactorization modes (`9 -> 0`).
   - At the `2017` BMV benchmark (`M = 10^-14 kg`, `d = 450 um`, `Delta_x = 250 um`, `T = 2.5 s`), Peres–Horodecki negativity `N = 0.078162` (`Delta_phi = 0.313934 rad`, concurrence `0.156323`) stays invariant to `< 10^-14` across every connected local unitary `U_A x U_B` and under the disconnected discrete exchange coset `exp(i pi/4) SWAP_AB in SU(4)` (`0` continuous tangent modes in `su(4)`), whereas omitting `C_loc` lets `exp(i (Delta_phi/4) sigma_z x sigma_z)` erase `N` to `0`.
4. **Scope Caveats & Nanoscale Protein-Frame Parallel**:
   - Explicitly separates fixed-slice `su(4)` refactorizations from clock-system unitaries `[V, C] = 0` in Page–Wootters (`1983`) timeless dynamics (`Stoica 2026`, `PROPOSED` preprint), where operational Haag–Kastler net locality pins physical laboratory observables.
   - Brief (`<= 3` mentions, `< 12%` of `<p>` blocks) `10 nm` structural biophysics parallel (`Fiedorczuk & Chen 2022`) illustrating non-coplanar interfacial cross-struts suppressing cooperative floppy hinges (`N_floppy > 0`) in multi-domain ABC transporter protein frames.

## 3. Primary Offline-Verified DOIs (`data/folio-citations.cache.json`)
| Source ID | Reference | DOI |
| --- | --- | --- |
| `ES04-CALLADINE1978` | Calladine (1978), *Int. J. Solids Struct.* | https://doi.org/10.1016/0020-7683(78)90052-5 |
| `ES04-PAGE1983` | Page & Wootters (1983), *Phys. Rev. D* | https://doi.org/10.1103/physrevd.27.2885 |
| `ES04-PELLEGRINO1986` | Pellegrino & Calladine (1986), *Int. J. Solids Struct.* | https://doi.org/10.1016/0020-7683(86)90014-4 |
| `ES04-KANE2014` | Kane & Lubensky (2014), *Nature Physics* | https://doi.org/10.1038/nphys2835 |
| `ES04-BOSE2017` | Bose et al. (2017), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.119.240401 |
| `ES04-MARLETTO2017` | Marletto & Vedral (2017), *Phys. Rev. Lett.* | https://doi.org/10.1103/physrevlett.119.240402 |
| `ES04-FIEDORCZUK2022` | Fiedorczuk & Chen (2022), *Science* | https://doi.org/10.1126/science.ade2216 |
| `ES04-STOICA2026` | Stoica (2026), *arXiv preprint* (`PROPOSED`) | https://doi.org/10.48550/arxiv.2608.16732 |
