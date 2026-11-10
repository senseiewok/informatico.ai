# -*- coding: utf-8 -*-
"""Cross-Scale Essay ES.04 · Tensegrity, Microcausality & Zero Modes.

Pure-Python stdlib linear-algebra kernel and bilingual (EN / es-MX) monograph data for
Informatico.ai's fourth Cross-Scale Featured Essay (/essays/tensegrity-microcausality-zero-modes/).

Unites two distinct physical spaces through the Fundamental Rank-Nullity Index Theorem,
    dim ker(C) - dim coker(C) = D - E,
without ever conflating Euclidean spatial frame coordinates with Lie-algebra generators:

  1. Map A — Space-Frame Truss Rigidity Matrix R in R^{E x (3V - 6)} (Calladine 1978;
     Pellegrino & Calladine 1986; Kane & Lubensky 2014):
     - Acts on Euclidean nodal displacements R^{3V} modulo the 6 rigid-body motions se(3),
       yielding the Maxwell-Calladine index N_floppy - N_self_stress = (3V - 6) - E.
     - Pure-Python Gaussian elimination tracks an 8-vertex cubic truss (D = 18, E = 12 -> 18 -> 19)
       from 6 floppy shear/warping modes down to 0 floppy modes and 1 state of self-stress,
       exposes why coplanar double-bracing (E = 18, rank = 17) leaves N_floppy = 1 alongside
       N_self_stress = 1, and verifies both the regular convex octahedron (V = 6, E = 12, rank = 12)
       and the 3-prism tensegrity simplex at its 30 deg prestressable twist (rank = 11).

  2. Map B — Explicit 54 x 15 Real Normalizer-Commutator Matrix C_loc on su(4)
     (Bose et al. 2017; Marletto & Vedral 2017; Page & Wootters 1983; Stoica 2026 preprint):
     - Acts on the 15-dimensional traceless Hermitian Pauli-tensor basis of su(4)
       (3 local A + 3 local B + 9 non-local sigma_a x sigma_b).
     - Projects the 6 commutators -i[X, sigma_k x I] and -i[X, I x sigma_k] onto the
       9-dimensional non-local subspace (6 * 9 = 54 rows, 15 columns).
     - Pure-Python Gaussian elimination proves rank(C_loc) = 9, nullity = 15 - 9 = 6
       (su(2)_A + su(2)_B), and coker = 54 - 9 = 45, collapsing all 9 continuous Cartan-Weyl
       non-local refactorization modes (9 -> 0) so two-mass BMV negativity (N = 0.078162 at
       M = 10^-14 kg, d = 450 um, Delta_x = 250 um, T = 2.5 s) is invariant under every
       connected local gauge unitary U_A x U_B as well as discrete SWAP_AB.
"""
from __future__ import annotations

import cmath
from decimal import Decimal, InvalidOperation
import math
import re

# Exact SI & gravitational constants aligned with tools/timegravity_kernel.py
# and tools/timegravity_kernel_entangle.py
G_NEWTON = 6.67430e-11
HBAR = 1.054571817e-34

BMV_MASS_KG = 1.0e-14
BMV_SEP_M = 450.0e-6
BMV_SPLIT_M = 250.0e-6
BMV_HOLD_S = 2.5

RANK_TOL = 1.0e-9

_SUB_SUP_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻₀₁₂₃₄₅₆₇₈₉", "0123456789-0123456789")
_NUM_RE = re.compile(r"(?<![A-Za-z])[-−]?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-−+]?\d+)?")


def extract_number_tokens(text: str) -> list[str]:
    """Extract normalized numeric tokens from prose or table cells for EN / es-MX parity."""
    norm = text.translate(_SUB_SUP_DIGITS).replace("−", "-")
    tokens: list[str] = []
    for match in _NUM_RE.finditer(norm):
        raw = match.group(0).replace(",", "")
        try:
            tokens.append(format(Decimal(raw).normalize(), "f"))
        except InvalidOperation:
            tokens.append(raw)
    return sorted(tokens)


# ---------------------------------------------------------------------------
# Pure-Python Linear Algebra & Rank-Nullity Kernel
# ---------------------------------------------------------------------------

def gaussian_elimination_rank(matrix: list[list[float]], tol: float = RANK_TOL) -> int:
    """Compute exact numerical rank of a real matrix via partial-pivoting Gaussian elimination."""
    if not matrix or not matrix[0]:
        return 0
    work = [[float(v) for v in row] for row in matrix]
    n_rows = len(work)
    n_cols = len(work[0])
    rank = 0
    for col in range(n_cols):
        if rank >= n_rows:
            break
        piv = max(range(rank, n_rows), key=lambda r: abs(work[r][col]))
        if abs(work[piv][col]) <= tol:
            continue
        if piv != rank:
            work[rank], work[piv] = work[piv], work[rank]
        piv_val = work[rank][col]
        for j in range(col, n_cols):
            work[rank][j] /= piv_val
        for i in range(n_rows):
            if i != rank and abs(work[i][col]) > tol:
                factor = work[i][col]
                for j in range(col, n_cols):
                    work[i][j] -= factor * work[rank][j]
        rank += 1
    return rank


def rank_nullity_audit(matrix: list[list[float]], domain_dim: int | None = None, tol: float = RANK_TOL) -> dict:
    """Audit any linear constraint map C : R^D -> R^E against dim ker(C) - dim coker(C) = D - E."""
    n_rows = len(matrix)
    n_cols = domain_dim if domain_dim is not None else (len(matrix[0]) if n_rows > 0 else 0)
    rk = gaussian_elimination_rank(matrix, tol=tol) if (n_rows > 0 and n_cols > 0) else 0
    nullity = n_cols - rk
    cokernel = n_rows - rk
    index_lhs = nullity - cokernel
    index_rhs = n_cols - n_rows
    return {
        "rows_E": n_rows,
        "cols_D": n_cols,
        "rank": rk,
        "nullity": nullity,
        "cokernel": cokernel,
        "index_lhs": index_lhs,
        "index_rhs": index_rhs,
        "index_exact": index_lhs == index_rhs,
    }


# ---------------------------------------------------------------------------
# Map A: 3D Space-Frame Rigidity Matrix R in R^{E x (3V - 6)}
# ---------------------------------------------------------------------------

def _gram_schmidt_columns(vectors: list[list[float]], tol: float = 1.0e-11) -> list[list[float]]:
    """Orthonormalize a list of vectors in R^N via modified Gram-Schmidt."""
    basis: list[list[float]] = []
    for vec in vectors:
        v = [float(x) for x in vec]
        for b in basis:
            proj = sum(v[k] * b[k] for k in range(len(v)))
            for k in range(len(v)):
                v[k] -= proj * b[k]
        norm = math.sqrt(sum(x * x for x in v))
        if norm > tol:
            basis.append([x / norm for x in v])
    return basis


def rigid_body_se3_basis(vertices: list[tuple[float, float, float]]) -> list[list[float]]:
    """Construct an orthonormal basis for the 6-dimensional Euclidean rigid-body subspace se(3) in R^{3V}."""
    n_verts = len(vertices)
    dim_3v = 3 * n_verts
    cx = sum(p[0] for p in vertices) / n_verts
    cy = sum(p[1] for p in vertices) / n_verts
    cz = sum(p[2] for p in vertices) / n_verts

    generators: list[list[float]] = []
    # 3 uniform translations
    for axis in range(3):
        vec = [0.0] * dim_3v
        for idx in range(n_verts):
            vec[3 * idx + axis] = 1.0
        generators.append(vec)
    # 3 infinitesimal rotations omega x (p_i - c)
    for rot_axis in ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)):
        ox, oy, oz = rot_axis
        vec = [0.0] * dim_3v
        for idx, (px, py, pz) in enumerate(vertices):
            rx, ry, rz = px - cx, py - cy, pz - cz
            vec[3 * idx + 0] = oy * rz - oz * ry
            vec[3 * idx + 1] = oz * rx - ox * rz
            vec[3 * idx + 2] = ox * ry - oy * rx
        generators.append(vec)

    basis = _gram_schmidt_columns(generators)
    if len(basis) != 6:
        raise ValueError(f"Non-generic vertex set: expected 6 rigid-body modes, got {len(basis)}")
    return basis


def internal_deformation_complement(vertices: list[tuple[float, float, float]]) -> list[list[float]]:
    """Return 3V - 6 orthonormal vectors spanning the internal deformation quotient R^{3V} / se(3)."""
    dim_3v = 3 * len(vertices)
    se3 = rigid_body_se3_basis(vertices)
    candidates = list(se3)
    for k in range(dim_3v):
        e_k = [0.0] * dim_3v
        e_k[k] = 1.0
        candidates.append(e_k)
    full_onb = _gram_schmidt_columns(candidates)
    return full_onb[6:]


def build_nodal_rigidity_matrix(
    vertices: list[tuple[float, float, float]],
    edges: list[tuple[int, int]],
) -> list[list[float]]:
    """Full compatibility matrix R_nodal in R^{E x 3V} mapping nodal velocities to axial bar extensions."""
    dim_3v = 3 * len(vertices)
    rows: list[list[float]] = []
    for i, j in edges:
        dx = vertices[i][0] - vertices[j][0]
        dy = vertices[i][1] - vertices[j][1]
        dz = vertices[i][2] - vertices[j][2]
        length = math.sqrt(dx * dx + dy * dy + dz * dz)
        if length <= 0.0:
            raise ValueError(f"Zero-length bar ({i}, {j})")
        row = [0.0] * dim_3v
        row[3 * i + 0] = dx / length
        row[3 * i + 1] = dy / length
        row[3 * i + 2] = dz / length
        row[3 * j + 0] = -dx / length
        row[3 * j + 1] = -dy / length
        row[3 * j + 2] = -dz / length
        rows.append(row)
    return rows


def build_internal_rigidity_matrix(
    vertices: list[tuple[float, float, float]],
    edges: list[tuple[int, int]],
) -> list[list[float]]:
    """Quotient rigidity matrix R in R^{E x (3V - 6)} acting strictly on internal deformations."""
    r_nodal = build_nodal_rigidity_matrix(vertices, edges)
    q_int = internal_deformation_complement(vertices)  # list of (3V - 6) vectors in R^{3V}
    dim_3v = 3 * len(vertices)
    out: list[list[float]] = []
    for r_row in r_nodal:
        out.append([sum(r_row[k] * q_col[k] for k in range(dim_3v)) for q_col in q_int])
    return out


def analyze_space_frame(
    vertices: list[tuple[float, float, float]],
    edges: list[tuple[int, int]],
    planted_defect: bool = False,
) -> dict:
    """Compute Maxwell-Calladine counts for a 3D pin-jointed space frame.

    When planted_defect=True, skips Gaussian elimination and applies naive scalar Maxwell
    counting N_floppy = max(0, (3V - 6) - E), N_self_stress = max(0, E - (3V - 6)), which
    fails whenever coplanar redundancy or tensegrity geometry drops rank(R) below min(D, E).
    """
    n_verts = len(vertices)
    n_edges = len(edges)
    d_internal = 3 * n_verts - 6
    r_nodal = build_nodal_rigidity_matrix(vertices, edges)
    r_internal = build_internal_rigidity_matrix(vertices, edges)

    if planted_defect:
        n_floppy = max(0, d_internal - n_edges)
        n_self_stress = max(0, n_edges - d_internal)
        rk = d_internal - n_floppy
    else:
        rk_nodal = gaussian_elimination_rank(r_nodal)
        rk = gaussian_elimination_rank(r_internal)
        assert rk == rk_nodal, f"Quotient rank mismatch: internal {rk} vs nodal {rk_nodal}"
        n_floppy = d_internal - rk
        n_self_stress = n_edges - rk

    return {
        "vertices_V": n_verts,
        "edges_E": n_edges,
        "internal_dof_D": d_internal,
        "matrix_shape": (len(r_internal), len(r_internal[0]) if r_internal else d_internal),
        "rank": rk,
        "n_floppy": n_floppy,
        "n_self_stress": n_self_stress,
        "maxwell_index": n_floppy - n_self_stress,
        "expected_index": d_internal - n_edges,
        "calladine_identity_holds": (n_floppy - n_self_stress) == (d_internal - n_edges),
    }


def cube_vertices() -> list[tuple[float, float, float]]:
    """Vertices of the unit 3D cube [0, 1]^3 indexed by 4*x + 2*y + z."""
    return [(float(x), float(y), float(z)) for x in (0, 1) for y in (0, 1) for z in (0, 1)]


def cube_frame_edges() -> list[tuple[int, int]]:
    """The 12 axial edge bars of the unit 3D cube."""
    verts = cube_vertices()
    edges: list[tuple[int, int]] = []
    for i in range(8):
        for j in range(i + 1, 8):
            dist_sq = sum((verts[i][k] - verts[j][k]) ** 2 for k in range(3))
            if abs(dist_sq - 1.0) < 1.0e-12:
                edges.append((i, j))
    return edges


# One diagonal brace across each of the 6 faces (x=0, x=1, y=0, y=1, z=0, z=1), plus a 7th space diagonal
CUBE_SIX_FACE_BRACES: tuple[tuple[int, int], ...] = (
    (0, 3),  # face x = 0: (0,0,0)-(0,1,1)
    (4, 7),  # face x = 1: (1,0,0)-(1,1,1)
    (0, 5),  # face y = 0: (0,0,0)-(1,0,1)
    (2, 7),  # face y = 1: (0,1,0)-(1,1,1)
    (0, 6),  # face z = 0: (0,0,0)-(1,1,0)
    (1, 7),  # face z = 1: (0,0,1)-(1,1,1)
)
CUBE_SEVENTH_BRACE: tuple[int, int] = (0, 7)  # body diagonal (0,0,0)-(1,1,1)


def evaluate_cubic_bracing_sequence(planted_defect: bool = False) -> dict:
    """Evaluate the V = 8 cubic truss across 0..7 braces plus a coplanar misplaced-brace trap."""
    verts = cube_vertices()
    base_edges = cube_frame_edges()
    steps: list[dict] = []
    for k in range(8):
        braces = list(CUBE_SIX_FACE_BRACES[: min(k, 6)])
        if k == 7:
            braces.append(CUBE_SEVENTH_BRACE)
        res = analyze_space_frame(verts, base_edges + braces, planted_defect=planted_defect)
        res["added_braces"] = k
        steps.append(res)

    # Misplaced 6-brace configuration (E = 18): double-brace face z = 0 with (0,6) and (2,4),
    # leaving face z = 1 unbraced -> rank = 17, N_floppy = 1, N_self_stress = 1!
    misplaced_braces = list(CUBE_SIX_FACE_BRACES[:5]) + [(2, 4)]
    misplaced = analyze_space_frame(verts, base_edges + misplaced_braces, planted_defect=planted_defect)

    # Regular convex octahedron (V = 6, E = 12, D = 12 -> rank = 12, N_floppy = 0, N_self_stress = 0)
    oct_verts = [
        (1.0, 0.0, 0.0), (-1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0), (0.0, -1.0, 0.0),
        (0.0, 0.0, 1.0), (0.0, 0.0, -1.0),
    ]
    oct_edges = [(i, j) for i in range(6) for j in range(i + 1, 6) if (i // 2) != (j // 2)]
    octahedron = analyze_space_frame(oct_verts, oct_edges, planted_defect=planted_defect)

    # Fuller-Snelson 3-prism tensegrity simplex (Calladine 1978): V = 6, E = 12 (9 cables + 3 struts)
    def _prism_verts(twist_rad: float) -> list[tuple[float, float, float]]:
        bot = [(math.cos(2.0 * math.pi * m / 3.0), math.sin(2.0 * math.pi * m / 3.0), 0.0) for m in range(3)]
        top = [
            (math.cos(2.0 * math.pi * m / 3.0 + twist_rad), math.sin(2.0 * math.pi * m / 3.0 + twist_rad), 1.0)
            for m in range(3)
        ]
        return bot + top

    prism_edges = [
        (0, 1), (1, 2), (2, 0),  # bottom cable triangle
        (3, 4), (4, 5), (5, 3),  # top cable triangle
        (0, 3), (1, 4), (2, 5),  # 3 lateral cables
        (0, 4), (1, 5), (2, 3),  # 3 compression struts
    ]
    tensegrity_30deg = analyze_space_frame(_prism_verts(math.pi / 6.0), prism_edges, planted_defect=planted_defect)
    tensegrity_generic = analyze_space_frame(_prism_verts(0.7), prism_edges, planted_defect=planted_defect)

    return {
        "steps": steps,
        "misplaced_18bar_cube": misplaced,
        "regular_octahedron": octahedron,
        "tensegrity_simplex_30deg": tensegrity_30deg,
        "tensegrity_simplex_generic": tensegrity_generic,
    }


# ---------------------------------------------------------------------------
# Map B: Explicit 54 x 15 Real Normalizer-Commutator Matrix on su(4) & BMV Witness
# ---------------------------------------------------------------------------

Matrix4C = list[list[complex]]

_I2: list[list[complex]] = [[1.0 + 0.0j, 0.0j], [0.0j, 1.0 + 0.0j]]
_SX: list[list[complex]] = [[0.0j, 1.0 + 0.0j], [1.0 + 0.0j, 0.0j]]
_SY: list[list[complex]] = [[0.0j, -1.0j], [1.0j, 0.0j]]
_SZ: list[list[complex]] = [[1.0 + 0.0j, 0.0j], [0.0j, -1.0 + 0.0j]]
_PAULI_NAMED: tuple[tuple[str, list[list[complex]]], ...] = (("X", _SX), ("Y", _SY), ("Z", _SZ))


def _kron2(a: list[list[complex]], b: list[list[complex]]) -> Matrix4C:
    return [[a[r // 2][c // 2] * b[r % 2][c % 2] for c in range(4)] for r in range(4)]


def _matmul4(a: Matrix4C, b: Matrix4C) -> Matrix4C:
    return [[sum(a[r][k] * b[k][c] for k in range(4)) for c in range(4)] for r in range(4)]


def _dagger4(a: Matrix4C) -> Matrix4C:
    return [[a[c][r].conjugate() for c in range(4)] for r in range(4)]


def _commutator_minus_i(x_mat: Matrix4C, y_mat: Matrix4C) -> Matrix4C:
    """Hermitian adjoint action -i [X, Y] for traceless Hermitian generators X, Y in su(4)."""
    xy = _matmul4(x_mat, y_mat)
    yx = _matmul4(y_mat, x_mat)
    return [[-1.0j * (xy[r][c] - yx[r][c]) for c in range(4)] for r in range(4)]


def _hs_inner(a: Matrix4C, b: Matrix4C) -> complex:
    """Normalized Hilbert-Schmidt inner product (1/4) Tr(A^dagger B), orthonormal on Pauli pairs."""
    return 0.25 * sum(a[r][c].conjugate() * b[r][c] for r in range(4) for c in range(4))


def su4_pauli_basis() -> tuple[list[str], list[Matrix4C]]:
    """Construct the 15 traceless Hermitian Pauli-pair generators of su(4).

    Ordering:
      0..2  : sigma_x x I, sigma_y x I, sigma_z x I   (3 local subsystem A generators)
      3..5  : I x sigma_x, I x sigma_y, I x sigma_z   (3 local subsystem B generators)
      6..14 : sigma_a x sigma_b for a, b in {x, y, z} (9 non-local Cartan-Weyl generators)
    """
    labels: list[str] = []
    mats: list[Matrix4C] = []
    for name, p in _PAULI_NAMED:
        labels.append(f"sigma_{name} x I")
        mats.append(_kron2(p, _I2))
    for name, p in _PAULI_NAMED:
        labels.append(f"I x sigma_{name}")
        mats.append(_kron2(_I2, p))
    for na, pa in _PAULI_NAMED:
        for nb, pb in _PAULI_NAMED:
            labels.append(f"sigma_{na} x sigma_{nb}")
            mats.append(_kron2(pa, pb))
    return labels, mats


def build_su4_normalizer_matrix(planted_defect: bool = False) -> list[list[float]]:
    """Construct the explicit 54 x 15 real normalizer-commutator constraint matrix C_loc on su(4).

    For X = sum_{nu=1}^{15} x_nu B_nu, microcausality pins the local subsystem algebras
    A_A = span{sigma_k x I} and A_B = span{I x sigma_k}, requiring that each of the 6
    commutators -i[X, L_m] (m = 1..6) have zero projection onto all 9 non-local Pauli-pair
    generators N_q = sigma_a x sigma_b (q = 1..9), yielding 6 * 9 = 54 real linear equations
    in 15 real unknowns.

    When planted_defect=True, omits the microcausality constraint (returns a 54 x 15 zero
    matrix), leaving all 15 su(4) directions—including the 9 non-local refactorization modes—free.
    """
    if planted_defect:
        return [[0.0] * 15 for _ in range(54)]

    _, basis = su4_pauli_basis()
    local_6 = basis[:6]
    nonlocal_9 = basis[6:]
    c_loc: list[list[float]] = []
    for l_m in local_6:
        for n_q in nonlocal_9:
            row: list[float] = []
            for b_nu in basis:
                comm = _commutator_minus_i(b_nu, l_m)
                proj = _hs_inner(n_q, comm)
                assert abs(proj.imag) < 1.0e-14, f"Expected real structure constant, got imag={proj.imag}"
                row.append(proj.real)
            c_loc.append(row)
    return c_loc


def _unitary_su2(axis: tuple[float, float, float], angle_rad: float) -> list[list[complex]]:
    """Exact SU(2) exponential exp(i * angle * (n . sigma)) = cos(angle) I + i sin(angle) (n . sigma)."""
    nx, ny, nz = axis
    norm = math.sqrt(nx * nx + ny * ny + nz * nz)
    nx, ny, nz = nx / norm, ny / norm, nz / norm
    c = math.cos(angle_rad)
    s = math.sin(angle_rad)
    return [
        [complex(c, s * nz), complex(s * ny, s * nx)],
        [complex(-s * ny, s * nx), complex(c, -s * nz)],
    ]


def _jacobi_real_symmetric(sym: list[list[float]], max_sweeps: int = 80, tol: float = 1.0e-14) -> list[float]:
    """Pure-Python cyclic Jacobi eigenvalue solver for an n x n real symmetric matrix."""
    n = len(sym)
    a = [[float(sym[r][c]) for c in range(n)] for r in range(n)]
    for _ in range(max_sweeps):
        off_max = 0.0
        for p in range(n):
            for q in range(p + 1, n):
                if abs(a[p][q]) > off_max:
                    off_max = abs(a[p][q])
        if off_max <= tol:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) <= tol:
                    continue
                tau = (a[q][q] - a[p][p]) / (2.0 * apq)
                t = (1.0 / (tau + math.hypot(1.0, tau))) if tau >= 0.0 else (-1.0 / (-tau + math.hypot(1.0, tau)))
                c = 1.0 / math.hypot(1.0, t)
                s = t * c
                app = a[p][p]
                aqq = a[q][q]
                a[p][p] = app - t * apq
                a[q][q] = aqq + t * apq
                a[p][q] = 0.0
                a[q][p] = 0.0
                for k in range(n):
                    if k != p and k != q:
                        akp = a[k][p]
                        akq = a[k][q]
                        a[k][p] = c * akp - s * akq
                        a[p][k] = a[k][p]
                        a[k][q] = s * akp + c * akq
                        a[q][k] = a[k][q]
    return sorted(a[k][k] for k in range(n))


def partial_transpose_negativity(rho: Matrix4C) -> float:
    """Peres-Horodecki partial-transpose negativity N(rho) = sum_{lambda_i(rho^{T_B}) < 0} |lambda_i|."""
    pt: Matrix4C = [[0.0j] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for m in range(2):
                    pt[2 * i + j][2 * k + m] = rho[2 * i + m][2 * k + j]
    # Real 8x8 symmetric embedding [[Re H, -Im H], [Im H, Re H]] doubles each Hermitian eigenvalue
    big = [[0.0] * 8 for _ in range(8)]
    for r in range(4):
        for c in range(4):
            re_val = pt[r][c].real
            im_val = pt[r][c].imag
            big[r][c] = re_val
            big[r + 4][c + 4] = re_val
            big[r][c + 4] = -im_val
            big[r + 4][c] = im_val
    vals = _jacobi_real_symmetric(big)
    eigs = [0.5 * (vals[2 * idx] + vals[2 * idx + 1]) for idx in range(4)]
    return sum(-ev for ev in eigs if ev < -1.0e-15)


def bmv_four_branch_density_matrix(
    mass_kg: float = BMV_MASS_KG,
    sep_m: float = BMV_SEP_M,
    split_m: float = BMV_SPLIT_M,
    hold_s: float = BMV_HOLD_S,
) -> tuple[Matrix4C, dict]:
    """Construct the pure 4-branch BMV density matrix rho_BMV and phase telemetry."""
    seps = {
        "LL": sep_m,
        "LR": sep_m + split_m,
        "RL": sep_m - split_m,
        "RR": sep_m,
    }
    pref = G_NEWTON * (mass_kg ** 2) * hold_s / HBAR
    phases = {br: pref / dist for br, dist in seps.items()}
    delta_phi = phases["LR"] + phases["RL"] - phases["LL"] - phases["RR"]
    order = ("LL", "LR", "RL", "RR")
    amps = [0.5 * cmath.exp(1.0j * phases[br]) for br in order]
    rho = [[amps[r] * amps[c].conjugate() for c in range(4)] for r in range(4)]
    concurrence_closed = abs(math.sin(0.5 * delta_phi))
    neg_closed = 0.5 * concurrence_closed
    return rho, {
        "phases_rad": phases,
        "delta_phi_rad": delta_phi,
        "concurrence_closed": concurrence_closed,
        "negativity_closed": neg_closed,
    }


def apply_nonlocal_zz_refactorization(rho: Matrix4C, theta_rad: float) -> Matrix4C:
    """Apply U_nl(theta) = exp(i * theta * (sigma_z x sigma_z)) in SU(4) generated by B_15."""
    # sigma_z x sigma_z = diag(+1, -1, -1, +1)
    phases = (
        cmath.exp(1.0j * theta_rad),
        cmath.exp(-1.0j * theta_rad),
        cmath.exp(-1.0j * theta_rad),
        cmath.exp(1.0j * theta_rad),
    )
    return [[phases[r] * rho[r][c] * phases[c].conjugate() for c in range(4)] for r in range(4)]


def su4_swap_operator() -> Matrix4C:
    """Disconnected normalizer element e^{i pi/4} SWAP_{AB} in SU(4) (det = +1)."""
    phase = cmath.exp(1.0j * math.pi / 4.0)
    raw = [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ]
    return [[phase * raw[r][c] for c in range(4)] for r in range(4)]


def evaluate_microcausality_and_bmv(planted_defect: bool = False) -> dict:
    """Audit the 54 x 15 su(4) normalizer matrix, local gauge invariance, SWAP_AB, and BMV negativity."""
    labels, basis = su4_pauli_basis()
    # Verify Hilbert-Schmidt orthonormality of all 15 traceless Hermitian Pauli-pair generators
    max_gram_err = 0.0
    for i in range(15):
        for j in range(15):
            target = 1.0 if i == j else 0.0
            err = abs(_hs_inner(basis[i], basis[j]) - target)
            if err > max_gram_err:
                max_gram_err = err

    c_loc = build_su4_normalizer_matrix(planted_defect=planted_defect)
    audit = rank_nullity_audit(c_loc, domain_dim=15)

    # Local subalgebra columns (0..5) vs non-local Cartan-Weyl columns (6..14)
    local_block_max = max(abs(c_loc[r][c]) for r in range(54) for c in range(6))
    nonlocal_submatrix = [row[6:] for row in c_loc]
    nonlocal_rank = gaussian_elimination_rank(nonlocal_submatrix)
    free_nonlocal_modes = 9 - nonlocal_rank

    rho_bmv, info = bmv_four_branch_density_matrix()
    neg_bmv = partial_transpose_negativity(rho_bmv)

    # Test invariance across deterministic connected local gauge transformations U_A x U_B in SU(2)_A x SU(2)_B
    local_axes = (
        ((1.0, 0.0, 0.0), 0.73, (0.0, 1.0, 0.0), -1.19),
        ((0.0, 0.0, 1.0), 1.41, (1.0, 1.0, 0.0), 0.58),
        ((1.0, -2.0, 0.5), -0.94, (-0.4, 0.7, 1.3), 1.87),
        ((0.3, 0.9, -1.1), 2.31, (1.2, -0.5, 0.8), -2.05),
    )
    max_local_gauge_drift = 0.0
    for ax_a, ang_a, ax_b, ang_b in local_axes:
        u_loc = _kron2(_unitary_su2(ax_a, ang_a), _unitary_su2(ax_b, ang_b))
        rho_rot = _matmul4(_matmul4(u_loc, rho_bmv), _dagger4(u_loc))
        drift = abs(partial_transpose_negativity(rho_rot) - neg_bmv)
        if drift > max_local_gauge_drift:
            max_local_gauge_drift = drift

    # Discrete SWAP_AB coset check: normalizes su(2)_A + su(2)_B by exchanging A <-> B, preserves negativity
    u_swap = su4_swap_operator()
    rho_swapped = _matmul4(_matmul4(u_swap, rho_bmv), _dagger4(u_swap))
    swap_neg_drift = abs(partial_transpose_negativity(rho_swapped) - neg_bmv)

    # Non-local refactorization U_nl(theta) = exp(i theta sigma_z x sigma_z):
    # Forbidden when microcausality holds (||C_loc e_15||_2 = 4.0 > 0), allowed when planted_defect=True!
    zz_col_norm = math.sqrt(sum(c_loc[r][14] ** 2 for r in range(54)))
    theta_disentangle = 0.25 * info["delta_phi_rad"]
    rho_disentangled = apply_nonlocal_zz_refactorization(rho_bmv, theta_disentangle)
    neg_if_unconstrained = partial_transpose_negativity(rho_disentangled)
    effective_witness_min_negativity = neg_if_unconstrained if free_nonlocal_modes > 0 else neg_bmv

    return {
        "basis_count": len(labels),
        "max_gram_orthonormality_err": max_gram_err,
        "c_loc_audit": audit,
        "local_columns_max_residual": local_block_max,
        "nonlocal_submatrix_rank": nonlocal_rank,
        "free_nonlocal_modes": free_nonlocal_modes,
        "zz_constraint_norm": zz_col_norm,
        "bmv_delta_phi_rad": info["delta_phi_rad"],
        "bmv_concurrence": info["concurrence_closed"],
        "bmv_negativity": neg_bmv,
        "bmv_negativity_closed_diff": abs(neg_bmv - info["negativity_closed"]),
        "max_local_gauge_negativity_drift": max_local_gauge_drift,
        "swap_ab_negativity_drift": swap_neg_drift,
        "unconstrained_refactorized_negativity": neg_if_unconstrained,
        "effective_witness_min_negativity": effective_witness_min_negativity,
    }


def evaluate_essay_es04(planted_defect: bool = False) -> dict:
    """Run both Map A (3D space-frame rigidity) and Map B (54 x 15 su(4) microcausality) audits."""
    return {
        "truss": evaluate_cubic_bracing_sequence(planted_defect=planted_defect),
        "quantum": evaluate_microcausality_and_bmv(planted_defect=planted_defect),
    }


# ---------------------------------------------------------------------------
# Bilingual Monograph Specification (EN / es-MX)
# ---------------------------------------------------------------------------

ESSAY: dict = {
    "code": "ES.04",
    "slug": "tensegrity-microcausality-zero-modes",
    "plate_slug": "essay04",
    "date": "2026-11-10",
    "seo": (
        "Tensegrity, Microcausality, and Zero Modes",
        "How one rank-nullity index theorem eliminates floppy shear modes in space trusses and fixes quantum subsystem locality in entanglement tests.",
        "Tensegridad, Microcausalidad y Modos Cero",
        "Cómo un teorema de rango-nulidad elimina modos blandos en armaduras espaciales y fija la localidad cuántica en pruebas de entrelazamiento.",
    ),
    "kicker_en": "Cross-Scale Essay · ES.04 · Structural Rigidity, Algebraic Locality & Zero Modes",
    "kicker_es": "Ensayo Transescalar · ES.04 · Rigidez Estructural, Localidad Algebraica y Modos Cero",
    "reading_time_en": "14 min read",
    "reading_time_es": "14 min de lectura",
    "title_en": "Tensegrity, Microcausality, and Zero Modes: How Constraint Rank Locks Space Frames and Quantum Subsystems",
    "title_es": "Tensegridad, Microcausalidad y Modos Cero: Cómo el Rango de Restricción Fija Armaduras Espaciales y Subsistemas Cuánticos",
    "standfirst_en": (
        "An unbraced 8-vertex steel cube and an abstract 4-level quantum state space fail for the same "
        "linear-algebraic reason: before independent constraints act, continuous zero modes let the cube "
        "shear without stretching a bar and let global SU(4) rotations erase 2-mass entanglement without "
        "touching the spectrum. Follow the exact rank-nullity index dim ker C − dim coker C = D − E across "
        "3D tensegrity frames, the 54 × 15 microcausality commutator map on su(4), and nanoscale protein hinges."
    ),
    "standfirst_es": (
        "Un cubo de acero de 8 vértices sin arriostrar y un espacio cuántico abstracto de 4 niveles fallan por "
        "la misma razón de álgebra lineal: antes de imponer restricciones independientes, los modos cero continuos "
        "permiten que el cubo se corte sin estirar barras y que rotaciones globales SU(4) borren el entrelazamiento "
        "de 2 masas sin alterar el espectro. Sigue el índice rango-nulidad dim ker C − dim coker C = D − E entre "
        "armaduras de tensegridad 3D, el mapa conmutador 54 × 15 en su(4) y bisagras proteicas en la nanoescala."
    ),
    "card_dek_en": (
        "One exact rank-nullity index eliminates 6 floppy modes in 8-node space trusses and collapses "
        "9 non-local su(4) refactorization modes to lock BMV entanglement negativity at 0.078162."
    ),
    "card_dek_es": (
        "Un mismo índice exacto de rango-nulidad elimina 6 modos blandos en armaduras de 8 nodos y colapsa "
        "9 modos no locales en su(4) para fijar la negatividad BMV en 0.078162."
    ),
    "instrument_kind": "kinematic",
    "predict": {
        "question_en": (
            "An 8-vertex cubic truss has 18 internal degrees of freedom and 12 edge bars (6 floppy modes). "
            "Suppose you add 6 diagonal braces so E = 18, placing 2 braces across the same flat face while "
            "leaving the opposite face unbraced—and compare this with imposing all 54 microcausality commutator "
            "rows on the 15 generators of su(4). What does Gaussian elimination reveal in each space?"
        ),
        "question_es": (
            "Una armadura cúbica de 8 vértices tiene 18 grados internos de libertad y 12 barras de arista (6 modos blandos). "
            "Supón que añades 6 diagonales hasta E = 18, colocando 2 en una misma cara plana y dejando la cara opuesta "
            "sin diagonal, y compáralo con imponer las 54 filas conmutadoras de microcausalidad sobre los 15 generadores "
            "de su(4). ¿Qué revela la eliminación gaussiana en cada espacio?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "Scalar counting 18 − 18 = 0 guarantees 0 floppy modes in the 18-bar cube, while 54 rows overconstrain su(4) to 0 generators.",
                "es": "El conteo escalar 18 − 18 = 0 garantiza 0 modos blandos en el cubo de 18 barras, mientras 54 filas reducen su(4) a 0 generadores.",
            },
            {
                "id": "b",
                "en": "Coplanar double-bracing drops rank(R) to 17 (1 floppy mode + 1 self-stress), while the 54 × 15 map on su(4) has rank 9 and nullity 6.",
                "es": "El doble arriostramiento coplanar baja rank(R) a 17 (1 modo blando + 1 autotensión), mientras el mapa 54 × 15 en su(4) tiene rango 9 y nulidad 6.",
            },
        ],
        "answer": "b",
        "explain_en": (
            "Scalar subtraction D − E = 0 only fixes the difference dim ker C − dim coker C, never the rank itself. "
            "Putting 2 braces on 1 planar square creates 1 redundant self-stress and leaves 1 unbraced shear mode "
            "(rank 17, 1 − 1 = 0). On su(4), 45 Jacobi redundancies among the 54 commutator rows leave exact rank 9, "
            "eliminating all 9 non-local modes and preserving the 6 local su(2)_A ⊕ su(2)_B gauge generators (nullity 6)."
        ),
        "explain_es": (
            "La resta escalar D − E = 0 solo fija la diferencia dim ker C − dim coker C, nunca el rango. "
            "Poner 2 diagonales en 1 cuadrado plano crea 1 autotensión redundante y deja 1 modo de corte libre "
            "(rango 17, 1 − 1 = 0). En su(4), 45 redundancias de Jacobi entre las 54 filas dejan rango exacto 9, "
            "eliminando los 9 modos no locales y conservando los 6 generadores locales su(2)_A ⊕ su(2)_B (nulidad 6)."
        ),
    },
    "sections": [
        {
            "id": "rank-nullity-spine",
            "h2_en": "I · Two Different Spaces, One Exact Index Theorem",
            "h2_es": "I · Dos Espacios Distintos, un Mismo Teorema Exacto de Índice",
            "short_en": "I · Index Theorem",
            "short_es": "I · Teorema de Índice",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Weld 12 steel rods with frictionless ball joints into the 12 edges of a 3D cube of V = 8 "
                        "vertices, set it on a laboratory table, and push gently on an upper corner. Even if every rod "
                        "is infinitely stiff in axial tension and compression, the frame folds effortlessly into a "
                        "rhombohedral prism. Now step across physics to the tabletop quantum-gravity witness proposed "
                        "independently by Bose et al. (2017) and Marletto and Vedral (2017): 2 diamond microspheres "
                        "of mass M = 10⁻¹⁴ kg fall side by side at center separation d = 450 µm, each held in a "
                        "2-branch spatial superposition of width Δx = 250 µm for T = 2.5 s. Hand a mathematician "
                        "only the abstract 4-dimensional complex Hilbert space ℂ⁴ of the 4 joint branches without "
                        "specifying which operators belong to left trap A and which belong to right trap B. Just like "
                        "the unbraced cube, the bare state vector can be continuously deformed by global unitary "
                        "rotations in SU(4) that turn an entangled pair into a separable product state without altering "
                        "a single eigenvalue of the density matrix."
                    ),
                    "es": (
                        "Ensambla 12 barras de acero con rótulas sin fricción en las 12 aristas de un cubo 3D de V = 8 "
                        "vértices, apóyalo sobre una mesa de laboratorio y empuja suavemente una esquina superior. Aunque "
                        "cada barra sea infinitamente rígida a tracción y compresión axial, el marco se pliega sin esfuerzo "
                        "en un prisma romboédrico. Cruza ahora hacia el testigo de gravedad cuántica de mesa propuesto de "
                        "forma independiente por Bose et al. (2017) y Marletto y Vedral (2017): 2 microesferas de diamante "
                        "de masa M = 10⁻¹⁴ kg caen en paralelo con separación central d = 450 µm, cada una mantenida en "
                        "superposición espacial de 2 ramas de ancho Δx = 250 µm durante T = 2.5 s. Entrega a un matemático "
                        "únicamente el espacio de Hilbert complejo abstracto de dimensión 4 (ℂ⁴) de las 4 ramas conjuntas sin especificar "
                        "qué operadores pertenecen a la trampa izquierda A y cuáles a la trampa derecha B. Igual que el "
                        "cubo sin arriostrar, el vector de estado desnudo admite rotaciones unitarias continuas en SU(4) "
                        "que convierten un par entrelazado en un estado producto separable sin cambiar un solo autovalor."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Precision requires stating what is NOT shared before naming what is. Structural mechanics "
                        "and quantum subsystem locality act on completely different vector spaces, and rigorous "
                        "modeling never conflates spatial coordinates with Lie-algebra generators. A 3D pin-jointed "
                        "truss with V ≥ 3 non-collinear joints lives in Euclidean configuration space ℝ³ⱽ; quotienting "
                        "out the 6 rigid-body motions of se(3) (3 translations and 3 rotations) leaves an internal "
                        "deformation space of dimension D_mech = 3V − 6 constrained by E axial bar-length equations. "
                        "A 2-qubit quantum experiment at a fixed clock slice lives instead on ℋ_A ⊗ ℋ_B ≅ ℂ² ⊗ ℂ², "
                        "where continuous basis refactorizations U = exp(i X) belong to the 15-dimensional Lie group "
                        "SU(4), so the infinitesimal generator X lives in a real vector space of dimension D_alg = 15 "
                        "constrained by E_alg = 54 commutator equations enforcing spatial microcausality. What unites "
                        "both worlds is not a metaphor, but the exact rank-nullity theorem of linear algebra."
                    ),
                    "es": (
                        "El rigor exige precisar qué NO comparten ambos problemas antes de enunciar qué los une. La "
                        "mecánica estructural y la localidad cuántica de subsistemas actúan sobre espacios vectoriales "
                        "completamente distintos, y un modelo serio jamás confunde coordenadas espaciales con generadores "
                        "de un álgebra de Lie. Una armadura articulada 3D con V ≥ 3 nudos no colineales vive en ℝ³ⱽ; al "
                        "dividir por los 6 movimientos de cuerpo rígido de se(3) (3 traslaciones y 3 rotaciones) queda "
                        "un espacio interno de dimensión D_mech = 3V − 6 sujeto a E ecuaciones axiales de barra. Un "
                        "experimento cuántico de 2 qubits en un corte fijo de reloj vive en ℋ_A ⊗ ℋ_B ≅ ℂ² ⊗ ℂ², donde "
                        "las refactorizaciones continuas U = exp(i X) pertenecen al grupo de Lie SU(4) de dimensión 15, "
                        "de modo que X habita un espacio real de dimensión D_alg = 15 sujeto a E_alg = 54 ecuaciones "
                        "conmutadoras de microcausalidad espacial. Lo que une ambos dominios no es una metáfora, sino "
                        "el teorema exacto de rango-nulidad del álgebra lineal."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "Plain-Language Bridge · Zero Modes and Redundant Locks",
                    "kicker_es": "Puente en Lenguaje Claro · Modos Cero y Cerraduras Redundantes",
                    "title_en": "Why counting equations minus unknowns misses hidden hinges unless you check matrix rank",
                    "title_es": "Por qué restar incógnitas menos ecuaciones pasa por alto bisagras ocultas sin el rango matricial",
                    "paras": [
                        (
                            "Every first-order constraint system maps D candidate motions to E checks via a linear "
                            "operator C of rank r. The D − r nullspace directions (ker C) are zero modes deforming the "
                            "system at 0 linear cost, while the E − r cokernel combinations (coker C = ker Cᵀ) are "
                            "equilibrium states of self-stress at 0 external load or redundant Jacobi identities.",
                            "Todo sistema lineal de primer orden envía D movimientos candidatos hacia E verificaciones "
                            "mediante un operador C de rango r. Las D − r direcciones del núcleo (ker C) son modos "
                            "cero con costo lineal 0, mientras las E − r combinaciones del conúcleo (coker C = ker Cᵀ) "
                            "son autotensiones en equilibrio con carga externa 0 o identidades de Jacobi redundantes.",
                        ),
                        (
                            "Subtracting cokernel from nullspace cancels rank r identically: (D − r) − (E − r) = D − E. "
                            "Scalar subtraction D − E fixes the net index, yet only Gaussian elimination of r reveals "
                            "whether zero modes and self-stresses both vanish or cancel in pairs.",
                            "Al restar conúcleo de núcleo, el rango r se cancela: (D − r) − (E − r) = D − E. "
                            "La resta escalar D − E fija el índice neto, pero solo la eliminación gaussiana de r revela "
                            "si modos cero y autotensiones se anulan juntos o se compensan en pares.",
                        ),
                    ],
                },
                {
                    "type": "equation",
                    "label_en": "Fundamental Rank–Nullity Index Identity",
                    "label_es": "Identidad Fundamental de Índice Rango–Nulidad",
                    "formula": "dim ker(C) − dim coker(C) = (D − rank(C)) − (E − rank(C)) = D − E",
                    "note_en": (
                        "For any real linear constraint operator C : ℝᴰ → ℝᴱ of rank r = rank(C), nullity dim ker(C) = D − r "
                        "counts unconstrained zero modes while corank dim coker(C) = dim ker(Cᵀ) = E − r counts redundant "
                        "constraint dependencies or equilibrium states of self-stress."
                    ),
                    "note_es": (
                        "Para cualquier operador lineal real C : ℝᴰ → ℝᴱ de rango r = rank(C), la nulidad dim ker(C) = D − r "
                        "cuenta modos cero libres mientras el corrango dim coker(C) = dim ker(Cᵀ) = E − r cuenta dependencias "
                        "redundantes o estados de autotensión en equilibrio."
                    ),
                },
            ],
        },
        {
            "id": "maxwell-calladine-trusses",
            "h2_en": "II · Space Frames and Tensegrity: Why Scalar Counting Needs Matrix Rank",
            "h2_es": "II · Armaduras Espaciales y Tensegridad: Por Qué el Conteo Escalar Exige Rango Matricial",
            "short_en": "II · 3D Rigidity",
            "short_es": "II · Rigidez 3D",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "In 1864 James Clerk Maxwell wrote down the bar-and-joint counting rule for stiff 3D frames: "
                        "V joints carry 3V Cartesian coordinates, 6 of which move the whole frame as a rigid body in "
                        "Euclidean space, leaving D_mech = 3V − 6 internal degrees of freedom to be locked by E bars. "
                        "Over a century later, Calladine (1978) and Pellegrino and Calladine (1986) resolved why "
                        "Buckminster Fuller's and Kenneth Snelson's cable-and-strut tensegrity sculptures stood taut "
                        "even when Maxwell's scalar count predicted mechanisms. Projecting the E × 3V nodal compatibility "
                        "matrix onto the (3V − 6)-dimensional orthogonal complement of se(3) produces the internal "
                        "rigidity matrix R ∈ ℝᴱˣ⁽³ⱽ⁻⁶⁾, whose nullity is N_floppy = (3V − 6) − rank(R) and whose "
                        "transpose nullity is N_self_stress = E − rank(R). Subtracting yields the Maxwell–Calladine "
                        "theorem: N_floppy − N_self_stress = (3V − 6) − E."
                    ),
                    "es": (
                        "En 1864 James Clerk Maxwell formuló la regla de conteo de barras y nudos para marcos rígidos "
                        "3D: V nudos portan 3V coordenadas cartesianas, 6 de las cuales desplazan todo el marco como "
                        "cuerpo rígido euclidiano, dejando D_mech = 3V − 6 grados internos por fijar mediante E barras. "
                        "Más de un siglo después, Calladine (1978) y Pellegrino y Calladine (1986) explicaron por qué "
                        "las esculturas de tensegridad de cables y puntales de Buckminster Fuller y Kenneth Snelson "
                        "permanecían tensas aun cuando el conteo escalar de Maxwell predecía mecanismos. Proyectar la "
                        "matriz nodal E × 3V sobre el complemento ortogonal de dimensión 3V − 6 de se(3) produce la "
                        "matriz interna de rigidez R ∈ ℝᴱˣ⁽³ⱽ⁻⁶⁾, cuya nulidad es N_floppy = (3V − 6) − rank(R) y cuya "
                        "nulidad transpuesta es N_self_stress = E − rank(R). Al restarlas surge el teorema de "
                        "Maxwell–Calladine: N_floppy − N_self_stress = (3V − 6) − E."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Watch our pure-Python Gaussian-elimination solver track R across 3 canonical space frames. "
                        "First, a regular convex octahedron has V = 6 vertices, D_mech = 3(6) − 6 = 12 internal degrees "
                        "of freedom, and E = 12 triangular edges; its 12 × 12 internal rigidity matrix has full rank 12, "
                        "so N_floppy = 0 and N_self_stress = 0 (strictly isostatic). Second, return to the V = 8 unit "
                        "cube [0, 1]³, where D_mech = 3(8) − 6 = 18. With only its E = 12 axial edges, R ∈ ℝ¹²ˣ¹⁸ has "
                        "rank 12, leaving N_floppy = 6 zero-energy modes (3 face shears plus 3 warping modes) and "
                        "N_self_stress = 0. Adding 1 diagonal cross-brace across each of the 6 distinct faces raises "
                        "rank(R) by 1 per brace—12 → 13 → 14 → 15 → 16 → 17 → 18—driving N_floppy from 6 down to 0 "
                        "at E = 18 with N_self_stress = 0. Inserting a 7th space diagonal across the body interior "
                        "(E = 19) cannot raise rank(R) above 18, so N_floppy stays 0 while N_self_stress jumps to 1 "
                        "(index 0 − 1 = 18 − 19 = −1)."
                    ),
                    "es": (
                        "Observemos cómo nuestro solucionador de eliminación gaussiana en Python puro evalúa R en 3 "
                        "armaduras espaciales canónicas. Primero, un octaedro convexo regular tiene V = 6 vértices, "
                        "D_mech = 3(6) − 6 = 12 grados internos y E = 12 aristas triangulares; su matriz interna 12 × 12 "
                        "alcanza rango completo 12, dando N_floppy = 0 y N_self_stress = 0 (estrictamente isostático). "
                        "Segundo, volvamos al cubo unitario [0, 1]³ de V = 8, donde D_mech = 3(8) − 6 = 18. Con solo "
                        "sus E = 12 aristas axiales, R ∈ ℝ¹²ˣ¹⁸ tiene rango 12, dejando N_floppy = 6 modos sin energía "
                        "elástica (3 cortes de cara más 3 alabeos) y N_self_stress = 0. Añadir 1 diagonal en cada una de las 6 "
                        "caras distintas eleva rank(R) en 1 por diagonal —12 → 13 → 14 → 15 → 16 → 17 → 18—, bajando N_floppy "
                        "de 6 a 0 en E = 18 con N_self_stress = 0. Añadir una diagonal espacial número 7 por el interior "
                        "(E = 19) no puede subir rank(R) por encima de 18, así que N_floppy sigue en 0 mientras "
                        "N_self_stress sube a 1 (índice 0 − 1 = 18 − 19 = −1)."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Now test why scalar counting fails without rank(R). Keep V = 8 and E = 18 so (3V − 6) − E = 0, "
                        "but place 2 diagonals on the z = 0 face while leaving z = 1 unbraced. A 2D 4-node square has "
                        "2(4) − 3 = 5 planar degrees of freedom, so 4 edges plus 2 diagonals (6 bars) create 1 planar "
                        "self-stress; Gaussian elimination on the 3D cube gives rank(R) = 17, uncovering N_floppy = 1 "
                        "shear mode paired with N_self_stress = 1 (1 − 1 = 0). Calladine (1978) showed tensegrity uses "
                        "this rank drop constructively: in the 3-prism simplex (V = 6, E = 12: 9 cables, 3 struts, "
                        "D_mech = 12), a generic 0.7 rad twist gives rank(R) = 12 and N_self_stress = 0, whereas the "
                        "symmetric 30° (π/6 rad) twist drops rank(R) to 11, creating N_self_stress = 1 global prestress "
                        "across all 12 members that stiffens N_floppy = 1 twist mode at quadratic order. Kane and "
                        "Lubensky (2014) extended R and Rᵀ to isostatic lattices (N_floppy − N_self_stress = 0), "
                        "proving topological polarization shifts boundary zero modes across opposite crystal edges."
                    ),
                    "es": (
                        "Probemos por qué falla el conteo escalar sin rank(R). Con V = 8 y E = 18 ((3V − 6) − E = 0), "
                        "coloquemos 2 diagonales en la cara z = 0 dejando z = 1 sin diagonal. Un cuadrado 2D de 4 nudos "
                        "tiene 2(4) − 3 = 5 grados planos, así que 4 aristas más 2 diagonales (6 barras) crean 1 "
                        "autotensión plana; la eliminación gaussiana en el cubo 3D arroja rank(R) = 17, revelando "
                        "N_floppy = 1 modo blando junto con N_self_stress = 1 (1 − 1 = 0). Calladine (1978) mostró que "
                        "la tensegridad aprovecha esa caída de rango: en el símplex 3-prisma (V = 6, E = 12: 9 cables, "
                        "3 puntales, D_mech = 12), un giro genérico de 0.7 rad da rank(R) = 12 y N_self_stress = 0, pero "
                        "el giro simétrico de 30° (π/6 rad) baja rank(R) a 11, creando N_self_stress = 1 pretensión en "
                        "los 12 miembros que rigidiza a orden cuadrático el modo N_floppy = 1. Kane y Lubensky (2014) "
                        "extendieron R y Rᵀ a redes isostáticas (N_floppy − N_self_stress = 0), demostrando que una "
                        "polarización topológica desplaza modos cero hacia bordes cristalinos opuestos."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Maxwell–Calladine Space-Frame Rigidity Index",
                    "label_es": "Índice de Rigidez Espacial de Maxwell–Calladine",
                    "formula": "R ∈ ℝ^{E × (3V−6)} ,    N_floppy − N_self_stress = (3V − 6 − rank(R)) − (E − rank(R)) = (3V − 6) − E",
                    "note_en": (
                        "For the V = 8 cube (3V − 6 = 18), 6 face braces give E = 18, rank(R) = 18, N_floppy = 0, "
                        "N_self_stress = 0; coplanar misplacement at E = 18 gives rank(R) = 17 (1 floppy, 1 self-stress); "
                        "adding a 7th brace (E = 19) gives rank(R) = 18 (0 floppy, 1 self-stress)."
                    ),
                    "note_es": (
                        "Para el cubo de V = 8 (3V − 6 = 18), 6 diagonales de cara dan E = 18, rank(R) = 18, N_floppy = 0, "
                        "N_self_stress = 0; un doble arriostramiento coplanar en E = 18 da rank(R) = 17 (1 modo blando, "
                        "1 autotensión); una diagonal número 7 (E = 19) da rank(R) = 18 (0 modos blandos, 1 autotensión)."
                    ),
                },
            ],
        },
        {
            "id": "microcausality-su4",
            "h2_en": "III · Fixing the Tensor Split: The 54 × 15 Normalizer Matrix on su(4)",
            "h2_es": "III · Fijar la Partición Tensorial: La Matriz Normalizadora 54 × 15 en su(4)",
            "short_en": "III · su(4) Locality",
            "short_es": "III · Localidad su(4)",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Now apply the exact same rank-nullity machinery—on its own Lie-algebraic space—to the 2-mass "
                        "gravitationally induced entanglement witness of Bose et al. (2017) and Marletto and Vedral "
                        "(2017). At M = 10⁻¹⁴ kg, center separation d = 450 µm, branch split Δx = 250 µm (closest "
                        "approach d − Δx = 200 µm), and free-fall hold time T = 2.5 s, Newtonian gravity imprints 4 "
                        "branch phases φ_ij = G M² T / (ℏ d_ij) with net entanglement phase Δφ = φ_LR + φ_RL − φ_LL − "
                        "φ_RR = 0.313934 rad. On the fixed tensor product ℋ_A ⊗ ℋ_B ≅ ℂ² ⊗ ℂ², the pure 4-branch state "
                        "has Wootters concurrence |sin(Δφ / 2)| = 0.156323 and Peres–Horodecki partial-transpose "
                        "negativity 𝒩 = 0.078162. Why can an adversarial skeptic not simply apply a global unitary "
                        "change of basis U ∈ SU(4) on ℂ⁴ and declare the state unentangled?"
                    ),
                    "es": (
                        "Apliquemos ahora exactamente la misma maquinaria de rango-nulidad —en su propio espacio de "
                        "álgebra de Lie— al testigo de entrelazamiento gravitacional de 2 masas de Bose et al. (2017) "
                        "y Marletto y Vedral (2017). Con M = 10⁻¹⁴ kg, separación central d = 450 µm, división de "
                        "ramas Δx = 250 µm (acercamiento mínimo d − Δx = 200 µm) y tiempo de caída libre T = 2.5 s, la "
                        "gravedad newtoniana imprime 4 fases φ_ij = G M² T / (ℏ d_ij) con fase neta de entrelazamiento "
                        "Δφ = φ_LR + φ_RL − φ_LL − φ_RR = 0.313934 rad. En el producto tensorial fijo ℋ_A ⊗ ℋ_B ≅ "
                        "ℂ² ⊗ ℂ², el estado puro de 4 ramas alcanza concurrencia de Wootters |sin(Δφ / 2)| = 0.156323 "
                        "y negatividad de transposición parcial de Peres–Horodecki 𝒩 = 0.078162. ¿Por qué un escéptico "
                        "no puede aplicar un cambio unitario global U ∈ SU(4) en ℂ⁴ y declarar nulo el entrelazamiento?"
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Without local observable algebras, that skeptic would succeed completely. Span the 15-dimensional "
                        "real Lie algebra su(4) of traceless Hermitian 4 × 4 generators by its 15 orthonormal Pauli-pair "
                        "operators under (1/4) Tr(B_µ B_ν) = δ_µν: 3 local A operators {σ_x ⊗ I, σ_y ⊗ I, σ_z ⊗ I}, "
                        "3 local B operators {I ⊗ σ_x, I ⊗ σ_y, I ⊗ σ_z}, and 9 non-local Cartan–Weyl correlation "
                        "operators {σ_a ⊗ σ_b} for a, b ∈ {x, y, z}. If 0 locality constraints are imposed (E_alg = 0), "
                        "all 9 non-local directions are unconstrained zero modes. In fact, exponentiating the 15th basis "
                        "element B₁₅ = σ_z ⊗ σ_z = diag(+1, −1, −1, +1) through the tiny angle θ = Δφ / 4 = 0.078484 rad "
                        "defines a smooth curve U_nl(θ) = exp(i θ σ_z ⊗ σ_z) ∈ SU(4) that shifts LL and RR by +Δφ/4 and "
                        "LR and RL by −Δφ/4, cancelling Δφ identically to 0 and collapsing negativity from 𝒩 = 0.078162 "
                        "to 0! Entanglement on an unpartitioned Hilbert space is as gauge-floppy as an unbraced cube."
                    ),
                    "es": (
                        "Sin álgebras de observables locales, ese escéptico tendría éxito total. Generemos el álgebra "
                        "de Lie real su(4) de dimensión 15 de matrices hermíticas sin traza de 4 × 4 mediante sus 15 "
                        "pares ortonormales de Pauli bajo (1/4) Tr(B_µ B_ν) = δ_µν: 3 operadores locales de A "
                        "{σ_x ⊗ I, σ_y ⊗ I, σ_z ⊗ I}, 3 operadores locales de B {I ⊗ σ_x, I ⊗ σ_y, I ⊗ σ_z} y 9 "
                        "operadores no locales de Cartan–Weyl {σ_a ⊗ σ_b} con a, b ∈ {x, y, z}. Si se imponen 0 "
                        "restricciones de localidad (E_alg = 0), las 9 direcciones no locales quedan como modos cero "
                        "libres. De hecho, exponenciar el elemento base número 15, B₁₅ = σ_z ⊗ σ_z = diag(+1, −1, −1, +1), "
                        "con el pequeño ángulo θ = Δφ / 4 = 0.078484 rad define una curva suave U_nl(θ) = "
                        "exp(i θ σ_z ⊗ σ_z) ∈ SU(4) que desplaza LL y RR en +Δφ/4 y LR y RL en −Δφ/4, anulando Δφ a 0 "
                        "y desplomando la negatividad de 𝒩 = 0.078162 a 0. En un espacio de Hilbert sin partición física, "
                        "el entrelazamiento es tan blando como un cubo sin diagonales."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Relativistic laboratory physics eliminates those 9 non-local zero modes through spatial "
                        "microcausality. Trap A and trap B sit in disjoint, spacelike-separated laboratory regions "
                        "𝒪_A and 𝒪_B at d − Δx = 200 µm, where Stern–Gerlach readout coils address 2 commuting local "
                        "observable subalgebras [𝒜_A(x), 𝒜_B(y)] = 0. Any continuous unitary refactorization "
                        "U(s) = exp(i s X) with X = ∑_{ν=1}^{15} x_ν B_ν that respects the physical laboratory split "
                        "must map each local subalgebra into itself: −i[X, L_m] ∈ 𝒜_A for m = 1, 2, 3 and −i[X, L_m] ∈ "
                        "𝒜_B for m = 4, 5, 6. Because commutators of Pauli tensors with L_m never mix 𝒜_A directly "
                        "into 𝒜_B, preserving locality is equivalent to requiring zero Hilbert–Schmidt projection onto "
                        "all 9 non-local basis elements N_q = σ_a ⊗ σ_b across all 6 local generators. That yields an "
                        "explicit real normalizer-commutator matrix C_loc ∈ ℝ⁵⁴ˣ¹⁵ (6 × 9 = 54 rows, 15 columns). "
                        "Running exact Gaussian elimination in our kernel proves rank(C_loc) = 9, nullity dim ker(C_loc) "
                        "= 15 − 9 = 6, and cokernel dim coker(C_loc) = 54 − 9 = 45 (index 6 − 45 = 15 − 54 = −39). "
                        "All 9 continuous Cartan–Weyl refactorization modes collapse (9 → 0; on B₁₅ alone, "
                        "‖C_loc e₁₅‖₂ = 4 > 0), leaving only the 6-dimensional local gauge algebra su(2)_A ⊕ su(2)_B, "
                        "under whose connected group SU(2)_A × SU(2)_B the BMV negativity 𝒩 = 0.078162 is invariant "
                        "to machine precision (< 10⁻¹⁴)."
                    ),
                    "es": (
                        "La física relativista de laboratorio elimina esos 9 modos cero no locales mediante la "
                        "microcausalidad espacial. Las trampas A y B ocupan regiones disjuntas separadas espacialmente "
                        "𝒪_A y 𝒪_B a d − Δx = 200 µm, donde bobinas locales de Stern–Gerlach leen 2 subálgebras "
                        "conmutativas [𝒜_A(x), 𝒜_B(y)] = 0. Toda refactorización unitaria continua U(s) = exp(i s X) "
                        "con X = ∑_{ν=1}^{15} x_ν B_ν que respete esa separación física debe enviar cada subálgebra "
                        "local sobre sí misma: −i[X, L_m] ∈ 𝒜_A para m = 1, 2, 3 y −i[X, L_m] ∈ 𝒜_B para m = 4, 5, 6. "
                        "Como los conmutadores con L_m nunca mezclan 𝒜_A directamente con 𝒜_B, preservar la localidad "
                        "equivale a exigir proyección de Hilbert–Schmidt nula sobre los 9 operadores no locales "
                        "N_q = σ_a ⊗ σ_b para los 6 generadores locales. Eso define una matriz real explícita "
                        "C_loc ∈ ℝ⁵⁴ˣ¹⁵ (6 × 9 = 54 filas, 15 columnas). La eliminación gaussiana exacta demuestra "
                        "rank(C_loc) = 9, nulidad dim ker(C_loc) = 15 − 9 = 6 y conúcleo dim coker(C_loc) = 54 − 9 = 45 "
                        "(índice 6 − 45 = 15 − 54 = −39). Los 9 modos continuos de Cartan–Weyl colapsan (9 → 0; tan "
                        "solo en B₁₅ se cumple ‖C_loc e₁₅‖₂ = 4 > 0), dejando únicamente el álgebra local su(2)_A ⊕ "
                        "su(2)_B de dimensión 6, bajo cuyo grupo conexo SU(2)_A × SU(2)_B la negatividad BMV "
                        "𝒩 = 0.078162 permanece invariante a precisión de máquina (< 10⁻¹⁴)."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "su(4) Microcausality Normalizer-Commutator Map",
                    "label_es": "Mapa Normalizador-Conmutador de Microcausalidad en su(4)",
                    "formula": "(C_loc)_{(m,q), ν} = (1/4) Tr( N_q · (−i [B_ν, L_m]) ) ∈ ℝ^{54 × 15} ,    rank = 9 ,  dim ker = 6 ,  dim coker = 45",
                    "note_en": (
                        "Across m = 1..6 local Pauli generators L_m and q = 1..9 non-local Pauli pairs N_q, C_loc "
                        "annihilates all 6 local generators and locks all 9 non-local Cartan–Weyl directions (9 → 0), "
                        "fixing 2-mass BMV negativity at 𝒩 = 0.078162 across every connected local unitary U_A ⊗ U_B."
                    ),
                    "note_es": (
                        "Sobre m = 1..6 generadores locales L_m y q = 1..9 pares no locales N_q, C_loc anula los 6 "
                        "generadores locales y bloquea las 9 direcciones no locales de Cartan–Weyl (9 → 0), fijando la "
                        "negatividad BMV de 2 masas en 𝒩 = 0.078162 bajo toda unitaria local conexa U_A ⊗ U_B."
                    ),
                },
            ],
        },
        {
            "id": "timeless-and-nanoscale-boundaries",
            "h2_en": "IV · Scope Caveats: Timeless Clock Slices, Discrete SWAP, and Nanoscale Protein Frames",
            "h2_es": "IV · Límites de Alcance: Cortes Atemporales de Reloj, SWAP Discreto y Marcos Proteicos",
            "short_en": "IV · Scope & Scale",
            "short_es": "IV · Alcance y Escala",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Two sharp mathematical scope boundaries keep our su(4) theorem honest. First, C_loc ∈ ℝ⁵⁴ˣ¹⁵ "
                        "acts on a fixed conditioned time slice ℋ_A ⊗ ℋ_B (dim su(4) = 15), which must be distinguished "
                        "from timeless clock-system refactorizations in the conditional-time formalism of Page and "
                        "Wootters (1983). In Page–Wootters quantum mechanics, a stationary universe state |Ψ⟩ ∈ ℋ_C ⊗ "
                        "ℋ_S obeys the Wheeler–DeWitt-like constraint (Ĥ_C ⊗ I_S + I_C ⊗ Ĥ_S)|Ψ⟩ = Ĉ|Ψ⟩ = 0, and "
                        "Schrödinger evolution emerges by conditioning |ψ(τ)⟩_S ∝ ⟨τ|_C Ψ⟩ on clock readings τ. In a "
                        "2026 arXiv preprint (PROPOSED epistemic ceiling, unrefereed), Stoica (2026) proves that "
                        "unitary transformations V̂ inside the commutant [V̂, Ĉ] = 0 preserve Ĉ|Ψ⟩ = 0 while remixing "
                        "ℋ_C and ℋ_S across slices, altering apparent conditional dynamics and subsystem entanglement "
                        "whenever Hilbert-space vectors and abstract spectra are all one specifies. What closes that "
                        "ambiguity in laboratory experiments is operational net locality: once hardware fixes the "
                        "physical clock observable algebra 𝒜_C and the spacelike-commuting diamond trap algebras "
                        "[𝒜_A(x), 𝒜_B(y)] = 0 on each conditioned slice, clock-system and inter-trap unitaries outside "
                        "the local algebra net are physically excluded."
                    ),
                    "es": (
                        "Dos fronteras matemáticas estrictas mantienen íntegro nuestro teorema en su(4). Primero, "
                        "C_loc ∈ ℝ⁵⁴ˣ¹⁵ actúa sobre un corte temporal condicionado fijo ℋ_A ⊗ ℋ_B (dim su(4) = 15), "
                        "lo cual debe distinguirse de las refactorizaciones reloj-sistema en el formalismo atemporal "
                        "de Page y Wootters (1983). En la mecánica cuántica de Page–Wootters, un estado estacionario "
                        "|Ψ⟩ ∈ ℋ_C ⊗ ℋ_S satisface la restricción tipo Wheeler–DeWitt (Ĥ_C ⊗ I_S + I_C ⊗ Ĥ_S)|Ψ⟩ = "
                        "Ĉ|Ψ⟩ = 0, y la evolución emerge al condicionar |ψ(τ)⟩_S ∝ ⟨τ|_C Ψ⟩ en lecturas τ del reloj. "
                        "En una prepublicación de arXiv de 2026 (techo epistémico PROPOSED, sin revisión por pares), "
                        "Stoica (2026) demuestra que unitarias V̂ dentro del conmutante [V̂, Ĉ] = 0 preservan Ĉ|Ψ⟩ = 0 "
                        "pero mezclan ℋ_C y ℋ_S entre cortes, alterando la dinámica condicional y el entrelazamiento "
                        "aparente si solo se especifican vectores y espectros abstractos. Lo que cierra esa ambigüedad "
                        "en el laboratorio es la localidad operacional de redes de observables: una vez que el aparato "
                        "fija el álgebra física del reloj 𝒜_C y las álgebras conmutativas [𝒜_A(x), 𝒜_B(y)] = 0 en "
                        "regiones espacialmente separadas de cada corte, esas mezclas quedan físicamente excluidas."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Second, inspect the difference between Lie-algebra tangent modes and disconnected discrete "
                        "group cosets. Within SU(4), the full group normalizer of su(2)_A ⊕ su(2)_B has 2 connected "
                        "components, (SU(2)_A × SU(2)_B) ⋊ ℤ₂, where the non-identity coset is generated by the "
                        "discrete subsystem exchange operator exp(i π/4) SWAP_AB ∈ SU(4) (with det(SWAP_AB) = −1 "
                        "compensated by exp(i π/4)⁴ = −1 so det = +1). Under conjugation, SWAP_AB exchanges the two "
                        "local subalgebras 𝒜_A ↔ 𝒜_B wholesale rather than keeping each inside itself. Crucially, "
                        "because ℤ₂ is discrete, SWAP_AB contributes 0 continuous tangent modes to ker(C_loc) (whose "
                        "dimension stays 6), is ruled out operationally as soon as trap 𝒪_A and trap 𝒪_B carry "
                        "distinct spatial coordinates, and—even if applied—leaves bipartite entanglement negativity "
                        "identically unchanged: 𝒩(SWAP_AB ρ_BMV SWAP_AB†) = 𝒩(ρ_BMV) = 0.078162 to 10⁻¹⁶."
                    ),
                    "es": (
                        "Segundo, conviene distinguir entre modos tangentes del álgebra de Lie y clases laterales "
                        "discretas desconectadas del grupo. Dentro de SU(4), el normalizador grupal completo de "
                        "su(2)_A ⊕ su(2)_B posee 2 componentes conexas, (SU(2)_A × SU(2)_B) ⋊ ℤ₂, cuya componente no "
                        "trivial está generada por el intercambio discreto exp(i π/4) SWAP_AB ∈ SU(4) (donde "
                        "det(SWAP_AB) = −1 se compensa con exp(i π/4)⁴ = −1 para dar det = +1). Bajo conjugación, "
                        "SWAP_AB permuta en bloque las subálgebras 𝒜_A ↔ 𝒜_B en vez de preservar cada una por separado. "
                        "De manera crucial, como ℤ₂ es discreto, SWAP_AB aporta 0 modos tangentes continuos a "
                        "ker(C_loc) (cuya dimensión sigue siendo 6), queda excluido en cuanto las trampas 𝒪_A y 𝒪_B "
                        "tienen coordenadas espaciales distintas y, aun si se aplica, deja idénticamente invariante la "
                        "negatividad bipartita: 𝒩(SWAP_AB ρ_BMV SWAP_AB†) = 𝒩(ρ_BMV) = 0.078162 hasta 10⁻¹⁶."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Step down 11 orders of magnitude in length from metre-scale steel trusses to a 10 nm "
                        "multi-domain membrane protein, and the exact same rank-nullity bar counting reappears in "
                        "structural biophysics. ATP-binding cassette (ABC) transporters assemble 2 transmembrane "
                        "helical bundles and 2 cytosolic nucleotide-binding domains across non-covalent domain "
                        "interfaces that transmit allosteric motion. In cryo-electron microscopy structures of the "
                        "human chloride channel CFTR studied in cystic fibrosis research, Fiedorczuk and Chen (2022) "
                        "resolved how deletion of residue 508 weakens an inter-domain packing junction, leaving "
                        "cooperative floppy hinge motions (N_floppy > 0) that destabilize the multi-domain frame, "
                        "whereas 2 small molecules binding distinct interfacial pockets act mechanically as "
                        "non-coplanar cross-linking struts—adding linearly independent distance constraints across "
                        "separate domain faces to suppress floppy shear hinges without over-constraining the single "
                        "functional pore-opening coordinate."
                    ),
                    "es": (
                        "Si descendemos 11 órdenes de magnitud en longitud desde armaduras métricas de acero hasta una "
                        "proteína de membrana multidominio de 10 nm, el mismo conteo de rango-nulidad reaparece en la "
                        "biofísica estructural. Los transportadores de casete de unión a ATP (ABC) ensamblan 2 haces "
                        "helicoidales transmembrana y 2 dominios citosólicos de unión a nucleótidos mediante interfaces "
                        "no covalentes que transmiten movimiento alostérico. En estructuras de criomicroscopía "
                        "electrónica del canal humano de cloruro CFTR estudiado en investigación sobre fibrosis "
                        "quística, Fiedorczuk y Chen (2022) resolvieron cómo la deleción del residuo 508 debilita una "
                        "unión entre dominios, dejando modos bisagra blandos cooperativos (N_floppy > 0) que "
                        "desestabilizan el marco multidominio, mientras que 2 moléculas pequeñas unidas en bolsillos "
                        "interfaciales distintos actúan mecánicamente como puntales transversales no coplanares: "
                        "añaden restricciones linealmente independientes en caras distintas para suprimir bisagras "
                        "blandas sin bloquear la coordenada funcional de apertura del poro."
                    ),
                },
            ],
        },
        {
            "id": "cross-domain-verification",
            "h2_en": "V · Five Constraint Audits, Verified Without Hand-Waving",
            "h2_es": "V · Cinco Auditorías de Restricción, Verificadas sin Conjeturas",
            "short_en": "V · Verification",
            "short_es": "V · Verificación",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Place our mechanical and quantum constraint maps side by side in a single ledger and the "
                        "structural unity becomes transparent. Whether a column represents an infinitesimal joint "
                        "displacement in ℝ³ⱽ / se(3) or a traceless Hermitian generator in su(4), nothing physical "
                        "is settled by subtracting D − E on the back of an envelope. You have to build the explicit "
                        "constraint operator C, compute rank(C) deterministically, and inspect both ker(C) and coker(C)."
                    ),
                    "es": (
                        "Al colocar nuestros mapas de restricción mecánicos y cuánticos uno junto al otro en un mismo "
                        "registro, la unidad estructural resulta transparente. Ya sea que una columna represente un "
                        "desplazamiento nodal infinitesimal en ℝ³ⱽ / se(3) o un generador hermítico sin traza en su(4), "
                        "nada físico queda resuelto restando D − E de manera superficial. Es indispensable construir "
                        "explícitamente el operador C, calcular rank(C) de forma determinista e inspeccionar tanto "
                        "ker(C) como coker(C)."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.04 · Exact Rank–Nullity Zero-Mode Audit Across Space Frames and su(4)",
                    "caption_es": "Tabla ES.04 · Auditoría Exacta Rango–Nulidad de Modos Cero en Armaduras Espaciales y su(4)",
                    "headers_en": [
                        "System & Space",
                        "(D, E)",
                        "rank(C)",
                        "Nullity dim ker(C)",
                        "Corank dim coker(C) & Physical Verdict",
                    ],
                    "headers_es": [
                        "Sistema y Espacio",
                        "(D, E)",
                        "rank(C)",
                        "Nulidad dim ker(C)",
                        "Corrango dim coker(C) y Veredicto Físico",
                    ],
                    "rows": [
                        [
                            (
                                "Unbraced cube (V = 8, E = 12) on ℝ²⁴ / se(3)",
                                "Cubo sin diagonales (V = 8, E = 12) en ℝ²⁴ / se(3)",
                            ),
                            ("(18, 12)", "(18, 12)"),
                            ("12", "12"),
                            ("6 floppy modes", "6 modos blandos"),
                            (
                                "0 self-stress; shears freely (6 − 0 = 6)",
                                "0 autotensión; se corta libremente (6 − 0 = 6)",
                            ),
                        ],
                        [
                            (
                                "6-face braced cube (V = 8, E = 18) vs coplanar trap (E = 18)",
                                "Cubo arriostrado en 6 caras (V = 8, E = 18) vs trampa coplanar (E = 18)",
                            ),
                            ("(18, 18)", "(18, 18)"),
                            ("18 vs 17", "18 vs 17"),
                            ("0 vs 1 floppy", "0 vs 1 modo blando"),
                            (
                                "0 vs 1 self-stress; rank separates rigid from hinged",
                                "0 vs 1 autotensión; el rango separa rigidez de bisagra",
                            ),
                        ],
                        [
                            (
                                "Tensegrity 3-prism simplex (V = 6, E = 12) at 30° twist",
                                "3-prisma de tensegridad (V = 6, E = 12) con giro de 30°",
                            ),
                            ("(12, 12)", "(12, 12)"),
                            ("11", "11"),
                            ("1 twist mode", "1 modo de giro"),
                            (
                                "1 global cable-strut prestress stabilizes frame (1 − 1 = 0)",
                                "1 pretensión global cable-puntal estabiliza el marco (1 − 1 = 0)",
                            ),
                        ],
                        [
                            (
                                "Bare ℂ⁴ without microcausality on su(4)",
                                "ℂ⁴ desnudo sin microcausalidad en su(4)",
                            ),
                            ("(15, 0)", "(15, 0)"),
                            ("0", "0"),
                            ("15 (9 non-local)", "15 (9 no locales)"),
                            (
                                "0; exp(i θ σ_z⊗σ_z) at θ = 0.078484 rad erases 𝒩 to 0",
                                "0; exp(i θ σ_z⊗σ_z) en θ = 0.078484 rad borra 𝒩 a 0",
                            ),
                        ],
                        [
                            (
                                "Spacelike traps [𝒜_A, 𝒜_B] = 0 via C_loc ∈ ℝ⁵⁴ˣ¹⁵",
                                "Trampas espaciales [𝒜_A, 𝒜_B] = 0 vía C_loc ∈ ℝ⁵⁴ˣ¹⁵",
                            ),
                            ("(15, 54)", "(15, 54)"),
                            ("9", "9"),
                            ("6 (su(2)_A⊕su(2)_B)", "6 (su(2)_A⊕su(2)_B)"),
                            (
                                "45 Jacobi redundancies; locks 9 → 0, pins 𝒩 = 0.078162",
                                "45 redundancias de Jacobi; fija 9 → 0 y 𝒩 = 0.078162",
                            ),
                        ],
                    ],
                },
                {
                    "type": "p",
                    "en": (
                        "Run verify_essay_tensegrity_microcausality.py --planted-defect—or toggle the planted-defect "
                        "switch in the kinematic observatory above—to watch both shortcuts fail deterministically. "
                        "In Map A, replacing Gaussian elimination with naive scalar counting max(0, 3V − 6 − E) "
                        "falsely certifies both the coplanar-misplaced 18-bar cube (true rank 17, N_floppy = 1) and "
                        "misses the 30° tensegrity prestress state (true rank 11, N_self_stress = 1). In Map B, "
                        "dropping the 54 × 15 microcausality commutator map unleashes all 9 Cartan–Weyl zero modes "
                        "so U_nl(0.078484 rad) wipes out the 𝒩 = 0.078162 gravitational entanglement witness to 0. "
                        "Across bridges, molecules, and quantum spacetimes, physical structure lives in the rank of "
                        "the constraints that forbid zero modes."
                    ),
                    "es": (
                        "Ejecuta verify_essay_tensegrity_microcausality.py --planted-defect —o activa el interruptor "
                        "de defecto plantado en el observatorio cinemático— para ver fallar de forma determinista "
                        "ambos atajos. En el Mapa A, sustituir la eliminación gaussiana por el conteo escalar ingenuo "
                        "max(0, 3V − 6 − E) certifica falsamente el cubo mal arriostrado de 18 barras (rango real 17, "
                        "N_floppy = 1) y omite el estado de pretensión de 30° en tensegridad (rango real 11, "
                        "N_self_stress = 1). En el Mapa B, suprimir el mapa conmutador 54 × 15 de microcausalidad "
                        "libera los 9 modos cero de Cartan–Weyl para que U_nl(0.078484 rad) borre el testigo "
                        "gravitacional de 𝒩 = 0.078162 hasta 0. Entre puentes, moléculas y espaciotiempos cuánticos, "
                        "la estructura física reside en el rango de las restricciones que impiden modos cero."
                    ),
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Sidenote 1 · Quotienting se(3) vs Pinning 6 Coordinates",
            "label_es": "Nota al Margen 1 · Cociente por se(3) frente a Fijar 6 Coordenadas",
            "en": (
                "Engineers often remove the 6 Euclidean rigid-body motions by pinning 1 vertex (3 coordinates), "
                "2 coordinates of a 2nd vertex, and 1 coordinate of a 3rd vertex. Our kernel instead projects "
                "R_nodal ∈ ℝ^{E × 3V} orthogonally onto the (3V − 6)-dimensional complement of se(3), avoiding "
                "any coordinate-axis singularity while preserving rank(R) to 10⁻¹²."
            ),
            "es": (
                "En ingeniería suelen eliminarse los 6 movimientos euclidianos de cuerpo rígido fijando 1 vértice (3 "
                "coordenadas), 2 coordenadas de un 2.º vértice y 1 coordenada de un 3.º vértice. Nuestro núcleo "
                "proyecta ortogonalmente R_nodal ∈ ℝ^{E × 3V} sobre el complemento de dimensión 3V − 6 de se(3), "
                "evitando singularidades axiales y conservando rank(R) a 10⁻¹²."
            ),
        },
        {
            "label_en": "Sidenote 2 · Prestress Stiffening at Order 2",
            "label_es": "Nota al Margen 2 · Rigidez Geométrica de Orden 2 por Pretensión",
            "en": (
                "Why doesn't the 1 infinitesimal twist mode of the 30° tensegrity 3-prism make it collapse? "
                "Pellegrino and Calladine (1986) showed that when an equilibrium self-stress vector t ∈ ker(Rᵀ) "
                "places cables in positive tension, bar lengths change at order δu², contributing a positive-definite "
                "geometric stiffness quadratic form that stabilizes the 1st-order mechanism."
            ),
            "es": (
                "¿Por qué el 1 modo infinitesimal de giro del 3-prisma de tensegridad a 30° no provoca su colapso? "
                "Pellegrino y Calladine (1986) demostraron que cuando un vector de autotensión t ∈ ker(Rᵀ) pone "
                "los cables en tracción positiva, las longitudes cambian a orden δu², aportando una rigidez "
                "geométrica definida positiva que estabiliza el mecanismo de orden 1."
            ),
        },
        {
            "label_en": "Sidenote 3 · Why 45 of the 54 Commutator Rows Are Redundant",
            "label_es": "Nota al Margen 3 · Por Qué 45 de las 54 Filas Conmutadoras Son Redundantes",
            "en": (
                "In C_loc ∈ ℝ^{54 × 15}, even the 27 rows generated by subsystem A's 3 Pauli operators L₁, L₂, L₃ "
                "already achieve full rank 9 on the 9 non-local generators σ_a ⊗ σ_b, because only multiples of I₂ "
                "commute with all 3 Pauli matrices. Subsystem B's 27 rows and internal su(2) Jacobi identities add "
                "45 linearly dependent checks (54 − 9 = 45) without touching the 6 local generators."
            ),
            "es": (
                "En C_loc ∈ ℝ^{54 × 15}, incluso las 27 filas generadas por los 3 operadores de Pauli L₁, L₂, L₃ "
                "del subsistema A ya alcanzan rango completo 9 sobre los 9 generadores no locales σ_a ⊗ σ_b, pues "
                "solo múltiplos de I₂ conmutan con las 3 matrices de Pauli. Las 27 filas de B y las identidades "
                "internas de Jacobi en su(2) añaden 45 verificaciones dependientes (54 − 9 = 45) sin tocar los 6 generadores locales."
            ),
        },
        {
            "label_en": "Sidenote 4 · Preprint Provenance Ceiling on arXiv:2608.16732",
            "label_es": "Nota al Margen 4 · Techo Epistémico PROPOSED en arXiv:2608.16732",
            "en": (
                "Under Informatico.ai's epistemic lattice (see Essay ES.02), Stoica (2026, 10.48550/arxiv.2608.16732) "
                "carries the PROPOSED preprint ceiling. Its mathematical theorem—existence of unitaries in the "
                "commutant of Ĉ on ℋ_C ⊗ ℋ_S—is exact linear algebra, whereas how nature selects local clock "
                "and field algebras in quantum gravity remains an active foundational research question."
            ),
            "es": (
                "Bajo la celosía epistémica de Informatico.ai (véase el Ensayo ES.02), Stoica (2026, "
                "10.48550/arxiv.2608.16732) mantiene el techo de prepublicación PROPOSED. Su teorema matemático "
                "—la existencia de unitarias en el conmutante de Ĉ sobre ℋ_C ⊗ ℋ_S— es álgebra lineal exacta, "
                "mientras que cómo selecciona la naturaleza las álgebras locales en gravedad cuántica sigue abierto."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES04-CALLADINE1978",
            "citation": "Calladine, C. R. — Buckminster Fuller's “Tensegrity” structures and Clerk Maxwell's rules for the construction of stiff frames, International Journal of Solids and Structures 14(2), 161–172",
            "doi": "10.1016/0020-7683(78)90052-5",
            "year": 1978,
            "role_en": "Establishes the exact rank-nullity index N_floppy − N_self_stress = (3V − 6) − E and explains 3-prism tensegrity prestress.",
            "role_es": "Establece el índice exacto N_floppy − N_self_stress = (3V − 6) − E y explica la pretensión del 3-prisma de tensegridad.",
        },
        {
            "id": "ES04-PAGE1983",
            "citation": "Page, D. N., & Wootters, W. K. — Evolution without evolution: Dynamics described by stationary observables, Physical Review D 27(12), 2885–2892",
            "doi": "10.1103/physrevd.27.2885",
            "year": 1983,
            "role_en": "Formulates conditional relational time slices from the timeless stationary constraint Ĉ|Ψ⟩ = 0 on ℋ_C ⊗ ℋ_S.",
            "role_es": "Formula cortes temporales condicionales a partir de la restricción estacionaria atemporal Ĉ|Ψ⟩ = 0 en ℋ_C ⊗ ℋ_S.",
        },
        {
            "id": "ES04-PELLEGRINO1986",
            "citation": "Pellegrino, S., & Calladine, C. R. — Matrix analysis of statically and kinematically indeterminate frameworks, International Journal of Solids and Structures 22(4), 409–428",
            "doi": "10.1016/0020-7683(86)90014-4",
            "year": 1986,
            "role_en": "Develops subspace matrix decomposition of ker(R) mechanisms, ker(Rᵀ) self-stresses, and 2nd-order geometric stiffness.",
            "role_es": "Desarrolla la descomposición matricial de mecanismos ker(R), autotensiones ker(Rᵀ) y rigidez geométrica de orden 2.",
        },
        {
            "id": "ES04-KANE2014",
            "citation": "Kane, C. L., & Lubensky, T. C. — Topological boundary modes in isostatic lattices, Nature Physics 10(1), 39–45",
            "doi": "10.1038/nphys2835",
            "year": 2014,
            "role_en": "Elevates the Maxwell–Calladine rigidity operator R to a topological index localizing zero modes on isostatic lattice edges.",
            "role_es": "Eleva el operador de rigidez R de Maxwell–Calladine a un índice topológico que localiza modos cero en bordes isostáticos.",
        },
        {
            "id": "ES04-BOSE2017",
            "citation": "Bose, S., Mazumdar, A., Morley, G. W., Ulbricht, H., Toroš, M., Paternostro, M., Geraci, A. A., Barker, P. F., Kim, M. S., & Milburn, G. — Spin entanglement witness for quantum gravity, Physical Review Letters 119(24), 240401",
            "doi": "10.1103/physrevlett.119.240401",
            "year": 2017,
            "role_en": "Defines the 2-mass 10⁻¹⁴ kg, d = 450 µm, Δx = 250 µm, T = 2.5 s gravitational entanglement benchmark (𝒩 = 0.078162).",
            "role_es": "Define la geometría de referencia de 2 masas de 10⁻¹⁴ kg, d = 450 µm, Δx = 250 µm y T = 2.5 s (𝒩 = 0.078162).",
        },
        {
            "id": "ES04-MARLETTO2017",
            "citation": "Marletto, C., & Vedral, V. — Gravitationally induced entanglement between two massive particles is sufficient evidence of quantum effects in gravity, Physical Review Letters 119(24), 240402",
            "doi": "10.1103/physrevlett.119.240402",
            "year": 2017,
            "role_en": "Proves that entanglement generation between 2 spacelike-localized subsystems requires non-classical mediator observables.",
            "role_es": "Demuestra que generar entrelazamiento entre 2 subsistemas espacialmente localizados exige observables mediadores no clásicos.",
        },
        {
            "id": "ES04-FIEDORCZUK2022",
            "citation": "Fiedorczuk, K., & Chen, J. — Molecular structures reveal synergistic rescue of Δ508 CFTR by Trikafta modulators, Science 378(6617), 284–290",
            "doi": "10.1126/science.ade2216",
            "year": 2022,
            "role_en": "Resolves non-coplanar interfacial domain cross-struts stabilizing a multi-domain ABC transporter protein frame at 10 nm scale.",
            "role_es": "Resuelve puntales interfaciales no coplanares que estabilizan el marco multidominio de un transportador ABC en la escala de 10 nm.",
        },
        {
            "id": "ES04-STOICA2026",
            "citation": "Stoica, O. C. — The preferred-time problem in the conditional interpretation of time, arXiv preprint arXiv:2608.16732 (PROPOSED, unrefereed)",
            "doi": "10.48550/arxiv.2608.16732",
            "year": 2026,
            "role_en": "Analyzes clock-system refactorizations inside the commutant of Ĉ in Page–Wootters dynamics (PROPOSED preprint).",
            "role_es": "Analiza refactorizaciones reloj-sistema en el conmutante de Ĉ bajo la dinámica de Page–Wootters (prepublicación PROPOSED).",
        },
    ],
    "skill_path": "skills/essays/tensegrity-microcausality-zero-modes/SKILL.md",
    "verifier_path": "skills/essays/tensegrity-microcausality-zero-modes/verify_essay_tensegrity_microcausality.py",
    "ai_line_en": (
        "AI contribution to cited primary literature: none. Essay prose, bilingual es-MX twin, pure-Python "
        "3D rigidity and 54 × 15 su(4) commutator rank solvers, and deterministic verifier were drafted with "
        "AI assistance and audited offline against primary DOIs."
    ),
    "ai_line_es": (
        "Contribución de IA a la literatura primaria citada: ninguna. El texto del ensayo, su gemelo bilingüe es-MX, "
        "los solucionadores en Python puro de rigidez 3D y rango 54 × 15 en su(4), y el verificador determinista "
        "se redactaron con asistencia de IA y se auditaron sin conexión contra DOIs primarios."
    ),
}
