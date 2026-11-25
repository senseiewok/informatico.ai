#!/usr/bin/env python3
"""Cross-format byte-level GLB, STEP AP242, 3MF, polyhedral inertia, and static tip-over checks for Toolbox X.08."""

from __future__ import annotations

from fractions import Fraction
import io
import math
import struct
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any

from toolchain_x01_checks import (
    _assert_vertex_congruence,
    count_connected_components,
    parse_step_faceted_brep,
    verify_strict_single_shell_2_manifold,
)

Vec2 = tuple[float, float]
Vec3 = tuple[float, float, float]
Tri = tuple[int, int, int]

NS_3MF_CORE = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"

# Canonical 8-node (ix, kz) order per y-plane (jy in {0, 1}) -> 16 vertices total.
# Shared identically with buildParametricMesh(isX08) in src/modules/glb-viewer.mjs.
X08_NODE_ORDER: tuple[tuple[int, int], ...] = (
    (0, 0),
    (1, 0),
    (0, 1),
    (1, 1),
    (2, 1),
    (0, 2),
    (1, 2),
    (2, 2),
)


def build_parametric_cantilever_mesh(
    base_width_mm: float = 24.0,
    depth_mm: float = 30.0,
    stem_height_mm: float = 36.0,
    cantilever_reach_mm: float = 18.0,
    cap_thickness_mm: float = 18.0,
) -> tuple[list[Vec3], list[Tri], list[Vec3]]:
    """Build a conforming 16-vertex, 28-face monolithic cantilevered pier-and-arm solid (chi = 2, 0 T-junctions)."""
    for name, val in (
        ("base_width_mm", base_width_mm),
        ("depth_mm", depth_mm),
        ("stem_height_mm", stem_height_mm),
        ("cantilever_reach_mm", cantilever_reach_mm),
        ("cap_thickness_mm", cap_thickness_mm),
    ):
        if not (math.isfinite(val) and val > 0.0):
            raise AssertionError(f"X.08 parameter {name} must be finite and positive, got {val!r}")

    xs = (0.0, float(base_width_mm), float(base_width_mm) + float(cantilever_reach_mm))
    ys = (-0.5 * float(depth_mm), 0.5 * float(depth_mm))
    zs = (0.0, float(stem_height_mm), float(stem_height_mm) + float(cap_thickness_mm))
    occupied = {(0, 0, 0), (0, 0, 1), (1, 0, 1)}

    vid_map: dict[tuple[int, int, int], int] = {}
    vertices: list[Vec3] = []
    colors: list[Vec3] = []
    for jy in (0, 1):
        for ix, kz in X08_NODE_ORDER:
            vid_map[(ix, jy, kz)] = len(vertices)
            vertices.append((xs[ix], ys[jy], zs[kz]))
            # Warm limestone pier (ix <= 1, kz <= 1) transitioning to walnut cantilever arm (ix == 2 or kz == 2)
            if ix == 2:
                colors.append((0.44, 0.31, 0.22))
            elif kz == 2:
                colors.append((0.58, 0.50, 0.42))
            else:
                colors.append((0.78, 0.76, 0.72))

    triangles: list[Tri] = []

    def _add_quad(p0: tuple[int, int, int], p1: tuple[int, int, int], p2: tuple[int, int, int], p3: tuple[int, int, int]) -> None:
        triangles.append((vid_map[p0], vid_map[p1], vid_map[p2]))
        triangles.append((vid_map[p0], vid_map[p2], vid_map[p3]))

    for ix, jy, kz in sorted(occupied):
        if (ix - 1, jy, kz) not in occupied:  # -X outward normal (-1, 0, 0)
            _add_quad((ix, 0, kz), (ix, 0, kz + 1), (ix, 1, kz + 1), (ix, 1, kz))
        if (ix + 1, jy, kz) not in occupied:  # +X outward normal (+1, 0, 0)
            _add_quad((ix + 1, 0, kz), (ix + 1, 1, kz), (ix + 1, 1, kz + 1), (ix + 1, 0, kz + 1))
        if (ix, jy - 1, kz) not in occupied:  # -Y outward normal (0, -1, 0)
            _add_quad((ix, 0, kz), (ix + 1, 0, kz), (ix + 1, 0, kz + 1), (ix, 0, kz + 1))
        if (ix, jy + 1, kz) not in occupied:  # +Y outward normal (0, +1, 0)
            _add_quad((ix, 1, kz), (ix, 1, kz + 1), (ix + 1, 1, kz + 1), (ix + 1, 1, kz))
        if (ix, jy, kz - 1) not in occupied:  # -Z outward normal (0, 0, -1)
            _add_quad((ix, 0, kz), (ix, 1, kz), (ix + 1, 1, kz), (ix + 1, 0, kz))
        if (ix, jy, kz + 1) not in occupied:  # +Z outward normal (0, 0, +1)
            _add_quad((ix, 0, kz + 1), (ix + 1, 0, kz + 1), (ix + 1, 1, kz + 1), (ix, 1, kz + 1))

    return vertices, triangles, colors


def compute_simplex_mass_properties(
    vertices: list[Vec3],
    triangles: list[Tri],
    label: str = "X.08 mesh",
) -> dict[str, Any]:
    """Method A: Exact surface-triangle canonical simplex integration for V (mm^3), r_cm (mm), and I_geom = I/rho (mm^5)."""
    if not vertices or not triangles:
        raise AssertionError(f"{label}: empty vertex or triangle list")
    nv = len(vertices)
    for idx, pt in enumerate(vertices):
        if not (math.isfinite(pt[0]) and math.isfinite(pt[1]) and math.isfinite(pt[2])):
            raise AssertionError(f"{label}: non-finite coordinate at vertex {idx}: {pt}")

    vol = 0.0
    m1 = [0.0, 0.0, 0.0]
    s_origin = [[0.0, 0.0, 0.0] for _ in range(3)]
    for f_idx, (i0, i1, i2) in enumerate(triangles):
        if not (0 <= i0 < nv and 0 <= i1 < nv and 0 <= i2 < nv):
            raise AssertionError(f"{label}: face {f_idx} index ({i0}, {i1}, {i2}) out of bounds for {nv} vertices")
        a, b, c = vertices[i0], vertices[i1], vertices[i2]
        cx = b[1] * c[2] - b[2] * c[1]
        cy = b[2] * c[0] - b[0] * c[2]
        cz = b[0] * c[1] - b[1] * c[0]
        vf = (a[0] * cx + a[1] * cy + a[2] * cz) / 6.0
        vol += vf
        s = (a[0] + b[0] + c[0], a[1] + b[1] + c[1], a[2] + b[2] + c[2])
        for p in range(3):
            m1[p] += vf * s[p] * 0.25
            for q in range(3):
                s_origin[p][q] += (vf / 20.0) * (
                    s[p] * s[q] + a[p] * a[q] + b[p] * b[q] + c[p] * c[q]
                )

    if not (math.isfinite(vol) and vol > 1e-9):
        raise AssertionError(f"{label}: signed volume must be positive, got {vol:.6f} mm^3")

    cm = (m1[0] / vol, m1[1] / vol, m1[2] / vol)
    s_cm = [[s_origin[p][q] - vol * cm[p] * cm[q] for q in range(3)] for p in range(3)]
    tr_s = s_cm[0][0] + s_cm[1][1] + s_cm[2][2]
    inertia_cm = [[(tr_s if p == q else 0.0) - s_cm[p][q] for q in range(3)] for p in range(3)]
    return {
        "volume_mm3": vol,
        "center_of_mass_mm": cm,
        "second_moment_cm_mm5": s_cm,
        "inertia_cm_mm5": inertia_cm,
    }


def compute_fraction_cuboid_mass_properties(
    base_width_mm: float = 24.0,
    depth_mm: float = 30.0,
    stem_height_mm: float = 36.0,
    cantilever_reach_mm: float = 18.0,
    cap_thickness_mm: float = 18.0,
) -> dict[str, Any]:
    """Method B: Independent exact fractions.Fraction parallel-axis cuboid sum (zero shared simplex math)."""
    b = Fraction(str(base_width_mm))
    w = Fraction(str(depth_mm))
    hs = Fraction(str(stem_height_mm))
    lc = Fraction(str(cantilever_reach_mm))
    tc = Fraction(str(cap_thickness_mm))
    if min(b, w, hs, lc, tc) <= 0:
        raise AssertionError("X.08 cuboid dimensions must all be strictly positive")

    boxes = (
        (Fraction(0), b, -w / 2, w / 2, Fraction(0), hs),
        (Fraction(0), b, -w / 2, w / 2, hs, hs + tc),
        (b, b + lc, -w / 2, w / 2, hs, hs + tc),
    )
    v_tot = Fraction(0)
    m1 = [Fraction(0), Fraction(0), Fraction(0)]
    for x0, x1, y0, y1, z0, z1 in boxes:
        vb = (x1 - x0) * (y1 - y0) * (z1 - z0)
        cb = ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)
        v_tot += vb
        for p in range(3):
            m1[p] += vb * cb[p]

    cm = (m1[0] / v_tot, m1[1] / v_tot, m1[2] / v_tot)
    inertia = [[Fraction(0), Fraction(0), Fraction(0)] for _ in range(3)]
    for x0, x1, y0, y1, z0, z1 in boxes:
        lx, ly, lz = x1 - x0, y1 - y0, z1 - z0
        vb = lx * ly * lz
        cb = ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2)
        d = (cb[0] - cm[0], cb[1] - cm[1], cb[2] - cm[2])
        d2 = d[0] * d[0] + d[1] * d[1] + d[2] * d[2]
        ic = (
            vb * (ly * ly + lz * lz) / 12,
            vb * (lx * lx + lz * lz) / 12,
            vb * (lx * lx + ly * ly) / 12,
        )
        for p in range(3):
            for q in range(3):
                inertia[p][q] += (ic[p] if p == q else Fraction(0)) + vb * (
                    (d2 if p == q else Fraction(0)) - d[p] * d[q]
                )

    return {
        "volume_mm3": float(v_tot),
        "volume_exact": str(v_tot),
        "center_of_mass_mm": (float(cm[0]), float(cm[1]), float(cm[2])),
        "center_of_mass_exact": tuple(str(c) for c in cm),
        "inertia_cm_mm5": [[float(inertia[r][c]) for c in range(3)] for r in range(3)],
    }


def jacobi_3x3_symmetric(matrix: list[list[float]], max_sweeps: int = 60) -> tuple[list[float], list[Vec3]]:
    """Pure-stdlib 3x3 cyclic Jacobi symmetric eigensolver returning sorted eigenvalues I_1 <= I_2 <= I_3 and unit eigenvectors."""
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise AssertionError("Expected a 3x3 inertia matrix")
    for r in range(3):
        for c in range(3):
            if not math.isfinite(matrix[r][c]):
                raise AssertionError(f"Non-finite inertia tensor entry at ({r}, {c})")
        for c in range(r + 1, 3):
            scale = max(1.0, abs(matrix[r][c]), abs(matrix[c][r]))
            if abs(matrix[r][c] - matrix[c][r]) > 1e-9 * scale:
                raise AssertionError(f"Inertia tensor is asymmetric at ({r}, {c}): {matrix[r][c]} vs {matrix[c][r]}")

    a = [[0.5 * (float(matrix[r][c]) + float(matrix[c][r])) for c in range(3)] for r in range(3)]
    u = [[1.0 if r == c else 0.0 for c in range(3)] for r in range(3)]
    for _ in range(max_sweeps):
        p, q = 0, 1
        best = abs(a[0][1])
        for r, c in ((0, 2), (1, 2)):
            if abs(a[r][c]) > best:
                best = abs(a[r][c])
                p, q = r, c
        if best < 1e-14 * max(1.0, abs(a[0][0]), abs(a[1][1]), abs(a[2][2])):
            break
        tau = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
        t = (1.0 if tau >= 0.0 else -1.0) / (abs(tau) + math.hypot(1.0, tau))
        cs = 1.0 / math.hypot(1.0, t)
        sn = t * cs
        app = a[p][p] - t * a[p][q]
        aqq = a[q][q] + t * a[p][q]
        a[p][p], a[q][q], a[p][q], a[q][p] = app, aqq, 0.0, 0.0
        for k in range(3):
            if k != p and k != q:
                akp = cs * a[k][p] - sn * a[k][q]
                akq = sn * a[k][p] + cs * a[k][q]
                a[k][p] = a[p][k] = akp
                a[k][q] = a[q][k] = akq
        for k in range(3):
            ukp = cs * u[k][p] - sn * u[k][q]
            ukq = sn * u[k][p] + cs * u[k][q]
            u[k][p], u[k][q] = ukp, ukq

    raw_evals = [a[0][0], a[1][1], a[2][2]]
    order = sorted(range(3), key=lambda i: raw_evals[i])
    evals = [raw_evals[i] for i in order]
    evecs: list[Vec3] = [(u[0][i], u[1][i], u[2][i]) for i in order]
    return evals, evecs


def verify_inertia_realizability(
    inertia_cm: list[list[float]],
    tol: float = 1e-6,
    label: str = "X.08 inertia",
) -> dict[str, Any]:
    """Verify Jacobi spectral decomposition, eigenvector orthogonality, positivity I_1 > 0, and triangle inequality I_1 + I_2 >= I_3."""
    evals, evecs = jacobi_3x3_symmetric(inertia_cm)
    i1, i2, i3 = evals
    norm_scale = max(1.0, abs(i3))

    max_ortho_err = 0.0
    max_eig_res = 0.0
    for j in range(3):
        vj = evecs[j]
        for k in range(3):
            vk = evecs[k]
            dot_jk = vj[0] * vk[0] + vj[1] * vk[1] + vj[2] * vk[2]
            max_ortho_err = max(max_ortho_err, abs(dot_jk - (1.0 if j == k else 0.0)))
        av = [sum(inertia_cm[r][c] * vj[c] for c in range(3)) for r in range(3)]
        for r in range(3):
            max_eig_res = max(max_eig_res, abs(av[r] - evals[j] * vj[r]))

    if max_ortho_err > 1e-11:
        raise AssertionError(f"{label}: eigenvector orthogonality error {max_ortho_err:.3e} > 1e-11")
    if max_eig_res > tol * norm_scale:
        raise AssertionError(f"{label}: Jacobi eigen-residual {max_eig_res:.3e} exceeds tolerance")
    if i1 <= 0.0:
        raise AssertionError(f"{label}: non-positive principal moment I_1 = {i1:.4f} mm^5 (violates positive definiteness)")

    slack = i1 + i2 - i3
    if slack < -tol * norm_scale:
        raise AssertionError(
            f"{label}: rigid-body triangle inequality violated: I_1 + I_2 - I_3 = {slack:.4f} mm^5 < 0 "
            f"(I_1={i1:.2f}, I_2={i2:.2f}, I_3={i3:.2f})"
        )

    return {
        "principal_moments_mm5": [round(x, 4) for x in evals],
        "principal_axes": [[round(c, 8) for c in v] for v in evecs],
        "triangle_inequality_slack_mm5": round(slack, 4),
        "max_orthogonality_error": max_ortho_err,
        "max_eigen_residual": max_eig_res,
    }


def convex_hull_2d(points: list[Vec2], eps: float = 1e-9) -> list[Vec2]:
    """Compute the strict CCW 2D monotone-chain convex hull, dropping collinear boundary intermediates."""
    pts = sorted({(round(float(x), 6), round(float(y), 6)) for (x, y) in points})
    if len(pts) <= 2:
        return pts

    def _cross(o: Vec2, a: Vec2, b: Vec2) -> float:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower: list[Vec2] = []
    for p in pts:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= eps:
            lower.pop()
        lower.append(p)

    upper: list[Vec2] = []
    for p in reversed(pts):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= eps:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def audit_static_support_stability(
    vertices: list[Vec3],
    triangles: list[Tri],
    center_of_mass: Vec3,
    support_z: float | None = None,
    label: str = "X.08 mesh",
) -> dict[str, Any]:
    """Audit base contact polygon at z = z_min (strictly from downward -Z faces) and signed CoM tip-over margin m_tip > 0."""
    if not vertices or not triangles:
        raise AssertionError(f"{label}: empty vertex or triangle list")
    z_min = min(v[2] for v in vertices) if support_z is None else float(support_z)
    if not math.isfinite(z_min):
        raise AssertionError(f"{label}: support_z must be finite")

    contact_pts: list[Vec2] = []
    downward_base_faces = 0
    nv = len(vertices)
    for f_idx, (i0, i1, i2) in enumerate(triangles):
        if not (0 <= i0 < nv and 0 <= i1 < nv and 0 <= i2 < nv):
            raise AssertionError(f"{label}: face {f_idx} index out of bounds")
        p0, p1, p2 = vertices[i0], vertices[i1], vertices[i2]
        if max(abs(p0[2] - z_min), abs(p1[2] - z_min), abs(p2[2] - z_min)) <= 1e-5:
            ux, uy, uz = p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]
            vx, vy, vz = p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]
            nx = uy * vz - uz * vy
            ny = uz * vx - ux * vz
            nz = ux * vy - uy * vx
            n_len = math.hypot(nx, math.hypot(ny, nz))
            if n_len <= 1e-9:
                raise AssertionError(f"{label}: degenerate zero-area base face {f_idx} at z={z_min:.4f}")
            nz_hat = nz / n_len
            if nz_hat > -1.0 + 1e-7:
                raise AssertionError(
                    f"{label}: base face {f_idx} on z={z_min:.4f} lacks downward -Z normal (n_z={nz_hat:.6f})"
                )
            downward_base_faces += 1
            contact_pts.extend([(p0[0], p0[1]), (p1[0], p1[1]), (p2[0], p2[1])])

    if downward_base_faces == 0:
        raise AssertionError(f"{label}: zero downward-oriented base contact faces found on z={z_min:.4f}")

    hull = convex_hull_2d(contact_pts)
    if len(hull) < 3:
        raise AssertionError(f"{label}: base support convex hull is degenerate with {len(hull)} vertices")

    hull_area = 0.0
    min_margin = float("inf")
    cx, cy, cz = center_of_mass
    nh = len(hull)
    for k in range(nh):
        x0, y0 = hull[k]
        x1, y1 = hull[(k + 1) % nh]
        hull_area += 0.5 * (x0 * y1 - x1 * y0)
        ex, ey = x1 - x0, y1 - y0
        elen = math.hypot(ex, ey)
        if elen <= 1e-9:
            raise AssertionError(f"{label}: zero-length hull edge in support polygon")
        # For a CCW hull edge (x0,y0)->(x1,y1), the inward normal is (-ey, ex) / elen
        inward_dist = (ex * (cy - y0) - ey * (cx - x0)) / elen
        if inward_dist < min_margin:
            min_margin = inward_dist

    dz_cm = cz - z_min
    if dz_cm <= 1e-6:
        raise AssertionError(f"{label}: center of mass height dz_cm={dz_cm:.6f} mm must exceed support plane")

    crit_tilt_deg = math.degrees(math.atan2(min_margin, dz_cm))
    if min_margin <= 0.0:
        raise AssertionError(
            f"{label}: static tip-over margin m_tip = {min_margin:.4f} mm <= 0.00 mm "
            f"(CoM x={cx:.4f}, y={cy:.4f} exits base hull; critical tilt {crit_tilt_deg:.4f} deg)"
        )

    return {
        "support_z_mm": round(z_min, 5),
        "downward_base_faces": downward_base_faces,
        "hull_vertices_mm": [[round(px, 4), round(py, 4)] for (px, py) in hull],
        "support_area_mm2": round(hull_area, 4),
        "tip_margin_mm": round(min_margin, 6),
        "critical_tilt_deg": round(crit_tilt_deg, 4),
    }


def _verify_3mf_identity_transform(root: ET.Element, ns: dict[str, str]) -> None:
    items = root.findall("m:build/m:item", ns)
    if len(items) != 1:
        raise AssertionError(f"X.08 3MF must declare exactly 1 build item, found {len(items)}")
    tf = items[0].attrib.get("transform")
    if tf is not None:
        vals = [float(x) for x in tf.split()]
        ident = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
        if len(vals) != 12 or any(abs(a - b) > 1e-7 for a, b in zip(vals, ident)):
            raise AssertionError(f"X.08 3MF non-identity build transform {tf!r} alters build-plate coordinates")


def run_x08_mass_stability_checks(files_dir: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    """Execute full cross-format GLB/STEP/3MF parity, dual simplex-vs-Fraction inertia, and tip-over negative controls."""
    from toolchain_uga import check_manifold_topology, parse_3mf_model, parse_glb, signed_mesh_volume

    exp = manifest["expected_geometry"]
    params = manifest.get("parameters", {})
    b_mm = float(params.get("base_width_mm", 24.0))
    w_mm = float(params.get("depth_mm", 30.0))
    h_stem = float(params.get("stem_height_mm", 36.0))
    l_cant = float(params.get("cantilever_reach_mm", 18.0))
    t_cap = float(params.get("cap_thickness_mm", 18.0))

    # 1. Binary GLB framing, single-shell topology, simplex mass properties, and Fraction cuboid agreement
    glb_raw = (files_dir / "x08_artifact.glb").read_bytes()
    if len(glb_raw) < 28:
        raise AssertionError("X.08 GLB truncated below 28-byte header")
    magic, version, total_len = struct.unpack_from("<III", glb_raw, 0)
    c0_len, c0_type = struct.unpack_from("<II", glb_raw, 12)
    bin_off = 20 + c0_len
    if magic != 0x46546C67 or version != 2 or total_len != len(glb_raw) or c0_type != 0x4E4F534A or bin_off + 8 > len(glb_raw):
        raise AssertionError("X.08 GLB header or JSON chunk framing invalid")
    c1_len, c1_type = struct.unpack_from("<II", glb_raw, bin_off)
    if c1_type != 0x004E4942 or bin_off + 8 + c1_len != len(glb_raw):
        raise AssertionError("X.08 GLB BIN chunk framing mismatch")

    parsed_glb = parse_glb(glb_raw)
    glb_verts, glb_tris = parsed_glb["vertices"], parsed_glb["triangles"]
    verify_strict_single_shell_2_manifold(len(glb_verts), glb_tris, "X.08 GLB")
    glb_comps = count_connected_components(len(glb_verts), glb_tris)
    if glb_comps != 1:
        raise AssertionError(f"X.08 GLB expected beta_0 = 1 connected component, got {glb_comps}")

    simplex = compute_simplex_mass_properties(glb_verts, glb_tris, "X.08 GLB")
    frac_ref = compute_fraction_cuboid_mass_properties(b_mm, w_mm, h_stem, l_cant, t_cap)

    vol_diff = abs(simplex["volume_mm3"] - frac_ref["volume_mm3"])
    cm_diff = max(abs(simplex["center_of_mass_mm"][k] - frac_ref["center_of_mass_mm"][k]) for k in range(3))
    in_diff = max(
        abs(simplex["inertia_cm_mm5"][r][c] - frac_ref["inertia_cm_mm5"][r][c])
        for r in range(3)
        for c in range(3)
    )
    if vol_diff > 1e-3 or cm_diff > 1e-4 or in_diff > 1e-2:
        raise AssertionError(
            f"X.08 simplex vs Fraction cuboid mismatch: dV={vol_diff:.3e}, dCM={cm_diff:.3e}, dI={in_diff:.3e}"
        )

    spec = verify_inertia_realizability(simplex["inertia_cm_mm5"], label="X.08 GLB")
    stab = audit_static_support_stability(
        glb_verts,
        glb_tris,
        simplex["center_of_mass_mm"],
        support_z=0.0,
        label="X.08 GLB",
    )

    # 2. STEP AP242 CLOSED_SHELL cross-format parity (topology, vertices, CoM, inertia, support margin)
    step_txt = (files_dir / "x08_artifact.step").read_text(encoding="utf-8")
    step_verts, step_tris, step_cp_count = parse_step_faceted_brep(step_txt)
    verify_strict_single_shell_2_manifold(len(step_verts), step_tris, "X.08 STEP")
    _assert_vertex_congruence(glb_verts, step_verts, "X.08 STEP")
    step_topo = check_manifold_topology(step_verts, step_tris)
    step_props = compute_simplex_mass_properties(step_verts, step_tris, "X.08 STEP")
    step_stab = audit_static_support_stability(
        step_verts,
        step_tris,
        step_props["center_of_mass_mm"],
        support_z=0.0,
        label="X.08 STEP",
    )
    if (
        not step_topo["is_watertight"]
        or step_topo["vertices"] != exp["vertices"]
        or step_topo["faces"] != exp["faces"]
        or abs(step_props["volume_mm3"] - frac_ref["volume_mm3"]) > 1e-2
        or abs(step_stab["tip_margin_mm"] - stab["tip_margin_mm"]) > 1e-4
    ):
        raise AssertionError(f"X.08 STEP round-trip mismatch: topo={step_topo}, stab={step_stab}")

    # 3. 3MF OPC ZIP cross-format parity
    tmf_raw = (files_dir / "x08_artifact.3mf").read_bytes()
    with zipfile.ZipFile(io.BytesIO(tmf_raw), "r") as zf:
        names = set(zf.namelist())
        for req_entry in ("[Content_Types].xml", "_rels/.rels", "3D/3dmodel.model"):
            if req_entry not in names:
                raise AssertionError(f"X.08 3MF archive missing required OPC entry {req_entry}")
        root = parse_3mf_model(zf.read("3D/3dmodel.model"), "x08_artifact.3mf")
    if root.attrib.get("unit") != "millimeter":
        raise AssertionError(f"X.08 3MF unit must be 'millimeter', got {root.attrib.get('unit')!r}")
    ns = {"m": NS_3MF_CORE}
    _verify_3mf_identity_transform(root, ns)

    tmf_verts: list[Vec3] = []
    for v_el in root.findall("m:resources/m:object/m:mesh/m:vertices/m:vertex", ns):
        tmf_verts.append((float(v_el.attrib["x"]), float(v_el.attrib["y"]), float(v_el.attrib["z"])))
    nv_tmf = len(tmf_verts)
    tmf_tris: list[Tri] = []
    for t_el in root.findall("m:resources/m:object/m:mesh/m:triangles/m:triangle", ns):
        i0, i1, i2 = int(t_el.attrib["v1"]), int(t_el.attrib["v2"]), int(t_el.attrib["v3"])
        if not (0 <= i0 < nv_tmf and 0 <= i1 < nv_tmf and 0 <= i2 < nv_tmf):
            raise AssertionError(f"X.08 3MF triangle index ({i0}, {i1}, {i2}) out of bounds for {nv_tmf} vertices")
        tmf_tris.append((i0, i1, i2))

    verify_strict_single_shell_2_manifold(len(tmf_verts), tmf_tris, "X.08 3MF")
    _assert_vertex_congruence(glb_verts, tmf_verts, "X.08 3MF")
    tmf_topo = check_manifold_topology(tmf_verts, tmf_tris)
    tmf_vol = signed_mesh_volume(tmf_verts, tmf_tris)
    tmf_props = compute_simplex_mass_properties(tmf_verts, tmf_tris, "X.08 3MF")
    tmf_stab = audit_static_support_stability(
        tmf_verts,
        tmf_tris,
        tmf_props["center_of_mass_mm"],
        support_z=0.0,
        label="X.08 3MF",
    )
    if abs(tmf_vol - frac_ref["volume_mm3"]) > 1e-2 or abs(tmf_stab["tip_margin_mm"] - stab["tip_margin_mm"]) > 1e-4:
        raise AssertionError("X.08 3MF volume or tip-over margin mismatch")

    # 4. Deterministic Negative Controls:
    # (a) Extended cantilever (L_c = 48 mm, t_cap = 24 mm) stays watertight (chi = 2) yet fails m_tip = -4.00 mm <= 0
    ko_verts, ko_tris, _ = build_parametric_cantilever_mesh(b_mm, w_mm, h_stem, 48.0, 24.0)
    ko_topo = check_manifold_topology(ko_verts, ko_tris)
    if not ko_topo["is_watertight"] or ko_topo["euler_characteristic"] != 2:
        raise AssertionError("X.08 tip-over knockout mesh must remain a valid watertight 2-manifold")
    ko_props = compute_simplex_mass_properties(ko_verts, ko_tris, "X.08 tip-over-knockout")
    try:
        audit_static_support_stability(
            ko_verts,
            ko_tris,
            ko_props["center_of_mass_mm"],
            support_z=0.0,
            label="X.08 tip-over-knockout",
        )
    except AssertionError as exc:
        if "static tip-over margin m_tip = -4.0000 mm" not in str(exc):
            raise AssertionError(f"X.08 tip-over-knockout failed for unexpected reason: {exc}") from exc
    else:
        raise AssertionError("X.08 tip-over-knockout (L_c=48, t_cap=24 -> m_tip=-4.00 mm) was NOT rejected")

    # (b) Unphysical inertia tensor violating rigid-body triangle inequality I_1 + I_2 < I_3 must fail closed
    bad_inertia = [[4.0e6, 0.0, 0.0], [0.0, 5.0e6, 0.0], [0.0, 0.0, 12.0e6]]
    try:
        verify_inertia_realizability(bad_inertia, label="X.08 non-physical-inertia")
    except AssertionError as exc:
        if "triangle inequality violated" not in str(exc):
            raise AssertionError(f"X.08 non-physical-inertia failed for unexpected reason: {exc}") from exc
    else:
        raise AssertionError("X.08 non-physical inertia tensor (I_1 + I_2 < I_3) was NOT rejected")

    crit_reach_mm = b_mm * math.sqrt(1.0 + h_stem / t_cap)
    return {
        "glb_bytes": len(glb_raw),
        "glb_json_chunk_bytes": c0_len,
        "glb_bin_chunk_bytes": c1_len,
        "connected_components_beta0": glb_comps,
        "center_of_mass_mm": [round(c, 5) for c in simplex["center_of_mass_mm"]],
        "fraction_center_of_mass_exact": list(frac_ref["center_of_mass_exact"]),
        "simplex_vs_fraction_max_inertia_diff_mm5": round(in_diff, 10),
        "inertia_cm_mm5": [[round(v, 3) for v in row] for row in simplex["inertia_cm_mm5"]],
        "principal_moments_mm5": spec["principal_moments_mm5"],
        "triangle_inequality_slack_mm5": spec["triangle_inequality_slack_mm5"],
        "support_area_mm2": stab["support_area_mm2"],
        "tip_margin_mm": stab["tip_margin_mm"],
        "critical_tilt_deg": stab["critical_tilt_deg"],
        "critical_cantilever_reach_mm": round(crit_reach_mm, 4),
        "step_cartesian_points": step_cp_count,
        "step_vertex_points": step_topo["vertices"],
        "step_advanced_faces": step_topo["faces"],
        "step_signed_volume_mm3": round(step_props["volume_mm3"], 3),
        "threemf_vertices": tmf_topo["vertices"],
        "threemf_faces": tmf_topo["faces"],
        "threemf_signed_volume_mm3": round(tmf_vol, 3),
        "knockout_tip_volume_mm3": round(ko_props["volume_mm3"], 3),
        "knockout_tip_cm_mm": [round(c, 4) for c in ko_props["center_of_mass_mm"]],
        "knockout_tip_margin_mm": -4.0,
    }
