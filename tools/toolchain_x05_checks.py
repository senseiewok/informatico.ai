#!/usr/bin/env python3
"""Cross-format byte-level GLB, STEP Part-21 POLY_LOOP, 3MF, frustum-volume, and overhang checks for Toolbox X.05."""

from __future__ import annotations

import io
import math
import struct
import zipfile
from pathlib import Path
from typing import Any

from toolchain_x01_checks import (
    _assert_vertex_congruence,
    count_connected_components,
    parse_step_faceted_brep,
    verify_strict_single_shell_2_manifold,
)

Vec3 = tuple[float, float, float]
Tri = tuple[int, int, int]


def compute_frustum_stack_volume(rings: list[tuple[float, float]]) -> dict[str, Any]:
    """Evaluate the Moscow-Papyrus square-frustum sum across ordered (z_mm, half_width_mm) stations."""
    if len(rings) < 2:
        raise AssertionError("Frustum stack requires at least 2 cross-sectional stations")
    for idx, (z_s, hw_s) in enumerate(rings):
        if not (math.isfinite(z_s) and math.isfinite(hw_s) and hw_s > 0.0):
            raise AssertionError(f"Invalid frustum station {idx}: (z={z_s}, hw={hw_s})")
    seg_vols: list[float] = []
    areas = [(2.0 * hw) * (2.0 * hw) for _, hw in rings]
    for k in range(1, len(rings)):
        z0, hw0 = rings[k - 1]
        z1, hw1 = rings[k]
        dz = z1 - z0
        if not (math.isfinite(dz) and dz > 0.0 and hw0 > 0.0 and hw1 > 0.0):
            raise AssertionError(
                f"Invalid frustum station pair {k - 1}->{k}: (z0={z0}, hw0={hw0}) -> (z1={z1}, hw1={hw1})"
            )
        a0, a1 = areas[k - 1], areas[k]
        vk = (dz / 3.0) * (a0 + a1 + math.sqrt(a0 * a1))
        seg_vols.append(vk)
    return {
        "segment_volumes_mm3": seg_vols,
        "total_volume_mm3": sum(seg_vols),
    }


def extract_square_rings(vertices: list[Vec3], tol: float = 1e-4) -> list[tuple[float, float]]:
    """Group 4-corner square station vertices by elevation z and return sorted (z, half_width) pairs."""
    if len(vertices) % 4 != 0 or not vertices:
        raise AssertionError(f"Expected 4*N square-ring vertices, found {len(vertices)}")
    if not (math.isfinite(tol) and tol >= 0.0):
        raise AssertionError(f"Invalid ring tolerance tol={tol}")
    buckets: list[tuple[float, list[Vec3]]] = []
    for pt in vertices:
        if not (math.isfinite(pt[0]) and math.isfinite(pt[1]) and math.isfinite(pt[2])):
            raise AssertionError(f"Non-finite vertex coordinate in square-ring extraction: {pt}")
        placed = False
        for idx, (z_ref, pts) in enumerate(buckets):
            if abs(pt[2] - z_ref) <= tol:
                pts.append(pt)
                buckets[idx] = (z_ref, pts)
                placed = True
                break
        if not placed:
            buckets.append((pt[2], [pt]))
    buckets.sort(key=lambda item: item[0])
    rings: list[tuple[float, float]] = []
    for z_val, pts in buckets:
        if len(pts) != 4:
            raise AssertionError(f"Station z={z_val:.4f} mm has {len(pts)} vertices instead of 4")
        hws = {round(abs(p[0]), 4) for p in pts} | {round(abs(p[1]), 4) for p in pts}
        if len(hws) != 1:
            raise AssertionError(f"Station z={z_val:.4f} mm is not a centered square ring: {pts}")
        hw = next(iter(hws))
        if not (math.isfinite(hw) and hw > 0.0):
            raise AssertionError(f"Station z={z_val:.4f} mm has non-positive half-width hw={hw}")
        expected_corners = {(-hw, -hw), (hw, -hw), (hw, hw), (-hw, hw)}
        actual_corners = {(round(p[0], 4), round(p[1], 4)) for p in pts}
        if actual_corners != expected_corners:
            raise AssertionError(f"Station z={z_val:.4f} mm lacks all 4 square quadrants: {actual_corners}")
        rings.append((round(z_val, 5), hw))
    return rings


def audit_mesh_overhang_angles(
    vertices: list[Vec3],
    triangles: list[Tri],
    threshold_deg: float = 45.0,
    build_plate_z: float | None = None,
    label: str = "X.05 mesh",
) -> dict[str, Any]:
    """Audit facet-normal overhang angles theta_f = arcsin(max(0, -n_f . z_hat)) <= threshold_deg.

    Build-plate contact is determined strictly by vertex elevation (all 3 vertices at z == build_plate_z
    within 1e-5 mm), never by n_z alone, so any suspended horizontal soffit at z > build_plate_z
    evaluates -n_f . z_hat = 1.0 -> theta_f = 90.0 deg and fails closed against threshold_deg.
    """
    if not (math.isfinite(threshold_deg) and 0.0 < threshold_deg < 90.0):
        raise AssertionError(f"{label}: overhang threshold {threshold_deg} deg must lie in (0, 90)")
    if not vertices or not triangles:
        raise AssertionError(f"{label}: empty vertex or triangle list")
    for v_idx, pt in enumerate(vertices):
        if not (math.isfinite(pt[0]) and math.isfinite(pt[1]) and math.isfinite(pt[2])):
            raise AssertionError(f"{label}: vertex {v_idx} carries non-finite coordinate {pt}")

    z_min = min(p[2] for p in vertices) if build_plate_z is None else float(build_plate_z)
    if not math.isfinite(z_min):
        raise AssertionError(f"{label}: build_plate_z must be finite, got {build_plate_z!r}")
    nv = len(vertices)
    base_faces = 0
    crown_faces = 0
    inward_or_vertical_faces = 0
    downward_overhang_faces = 0
    max_overhang_deg = 0.0
    min_signed_wall_tilt_deg = 90.0

    for f_idx, (i0, i1, i2) in enumerate(triangles):
        if not (0 <= i0 < nv and 0 <= i1 < nv and 0 <= i2 < nv):
            raise AssertionError(f"{label}: triangle {f_idx} index out of bounds")
        p0, p1, p2 = vertices[i0], vertices[i1], vertices[i2]
        ux, uy, uz = p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]
        vx, vy, vz = p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]
        nx = uy * vz - uz * vy
        ny = uz * vx - ux * vz
        nz = ux * vy - uy * vx
        n_mag = math.sqrt(nx * nx + ny * ny + nz * nz)
        if n_mag <= 1e-12:
            raise AssertionError(f"{label}: degenerate zero-area facet {f_idx}")
        nz_unit = nz / n_mag

        on_plate = (
            abs(p0[2] - z_min) <= 1e-5
            and abs(p1[2] - z_min) <= 1e-5
            and abs(p2[2] - z_min) <= 1e-5
        )
        if on_plate:
            if nz_unit > -0.9999:
                raise AssertionError(
                    f"{label}: build-plate facet {f_idx} at z={z_min:.4f} lacks downward -Z normal (n_z={nz_unit:.6f})"
                )
            base_faces += 1
            continue

        if nz_unit >= 0.9999:
            crown_faces += 1
            continue

        down_sin = max(-1.0, min(1.0, -nz_unit))
        signed_tilt_deg = math.degrees(math.asin(down_sin))
        if signed_tilt_deg < min_signed_wall_tilt_deg:
            min_signed_wall_tilt_deg = signed_tilt_deg

        overhang_deg = max(0.0, signed_tilt_deg)
        if down_sin > 1e-9:
            downward_overhang_faces += 1
        else:
            inward_or_vertical_faces += 1

        if overhang_deg > max_overhang_deg:
            max_overhang_deg = overhang_deg

        if not (overhang_deg <= threshold_deg + 1e-9):
            raise AssertionError(
                f"{label}: facet {f_idx} overhang {overhang_deg:.4f} deg exceeds threshold {threshold_deg:.2f} deg"
            )

    return {
        "build_plate_z_mm": round(z_min, 5),
        "build_plate_base_faces": base_faces,
        "upward_crown_faces": crown_faces,
        "inward_or_vertical_wall_faces": inward_or_vertical_faces,
        "downward_overhang_wall_faces": downward_overhang_faces,
        "min_signed_wall_tilt_deg": round(min_signed_wall_tilt_deg, 4),
        "max_wall_overhang_deg": round(max_overhang_deg, 4),
        "overhang_threshold_deg": round(threshold_deg, 2),
    }


def _build_parametric_strut_mesh(rings: list[tuple[float, float]]) -> tuple[list[Vec3], list[Tri]]:
    """Construct a closed 4-station square frustum mesh for in-process knockout verification."""
    vertices: list[Vec3] = []
    for z, hw in rings:
        vertices.extend([(-hw, -hw, z), (hw, -hw, z), (hw, hw, z), (-hw, hw, z)])
    triangles: list[Tri] = [(0, 3, 2), (0, 2, 1)]
    for r in range(len(rings) - 1):
        b = r * 4
        t = (r + 1) * 4
        for side in range(4):
            s0 = side
            s1 = (side + 1) % 4
            triangles.append((b + s0, b + s1, t + s1))
            triangles.append((b + s0, t + s1, t + s0))
    top_base = (len(rings) - 1) * 4
    triangles.extend([(top_base + 0, top_base + 1, top_base + 2), (top_base + 0, top_base + 2, top_base + 3)])
    return vertices, triangles


def _verify_x05_3mf_identity_build_transform(root: Any, ns: dict[str, str]) -> None:
    objs = root.findall("m:resources/m:object", ns)
    items = root.findall("m:build/m:item", ns)
    if len(objs) != 1 or len(items) != 1:
        raise AssertionError(f"X.05 3MF expected 1 object and 1 build item, got {len(objs)} and {len(items)}")
    obj_id = objs[0].attrib.get("id")
    if items[0].attrib.get("objectid") != obj_id:
        raise AssertionError("X.05 3MF build item objectid does not match object id")
    tf_raw = items[0].attrib.get("transform")
    if tf_raw is not None:
        try:
            parts = [float(x) for x in tf_raw.split()]
        except ValueError as exc:
            raise AssertionError(f"X.05 3MF build item carries non-numeric transform: {tf_raw!r}") from exc
        ident = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
        if len(parts) != 12 or any(not math.isfinite(x) for x in parts) or any(
            abs(a - b) > 1e-6 for a, b in zip(parts, ident)
        ):
            raise AssertionError(f"X.05 3MF build item carries non-identity transform: {tf_raw!r}")


def run_x05_strut_checks(files_dir: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    """Verify X.05 Moscow-Papyrus frustum sum, arcsin(-n.z_hat) overhang bounds, and GLB/STEP/3MF parity."""
    from toolchain_uga import (  # local import avoids circular dependency
        NS_3MF_CORE,
        check_manifold_topology,
        parse_3mf_model,
        parse_glb,
        signed_mesh_volume,
    )

    params = manifest.get("parameters", {})
    exp = manifest["expected_geometry"]
    height_mm = float(params.get("height_mm", 0.0))
    base_w = float(params.get("base_width_mm", 0.0))
    waist_w = float(params.get("waist_width_mm", 0.0))
    crown_w = float(params.get("crown_width_mm", 0.0))
    threshold_deg = float(params.get("overhang_threshold_deg", 45.0))
    manifest_overhang_deg = float(params.get("max_wall_overhang_deg", 0.0))
    exp_bmin = exp.get("bbox_min", [0.0, 0.0, 0.0])
    exp_bmax = exp.get("bbox_max", [0.0, 0.0, 0.0])

    if not all(
        math.isfinite(v)
        for v in (height_mm, base_w, waist_w, crown_w, threshold_deg, manifest_overhang_deg)
    ) or not (height_mm > 0.0 and base_w > 0.0 and waist_w > 0.0 and crown_w > 0.0):
        raise AssertionError(
            f"X.05 strut dimensions must be positive finite numbers: height={height_mm}, base={base_w}, waist={waist_w}, crown={crown_w}"
        )
    if len(exp_bmin) != 3 or len(exp_bmax) != 3 or abs(float(exp_bmin[2])) > 1e-6:
        raise AssertionError(f"X.05 manifest expected_geometry must seat base on build plate z = 0.0 mm, got bbox_min={exp_bmin!r}")

    # 1. Parse GLB, verify chunk arithmetic, single-shell 2-manifold, build-plate z = 0 overhang, square-ring stations, and frustum sum
    glb_raw = (files_dir / "x05_artifact.glb").read_bytes()
    parsed_glb = parse_glb(glb_raw)
    c0_len, _ = struct.unpack_from("<2I", glb_raw, 12)
    c1_len, _ = struct.unpack_from("<2I", glb_raw, 20 + c0_len)
    if 20 + c0_len + 8 + c1_len != len(glb_raw):
        raise AssertionError("X.05 GLB chunk lengths do not sum to total byte length")

    glb_verts = parsed_glb["vertices"]
    glb_tris = parsed_glb["triangles"]
    verify_strict_single_shell_2_manifold(len(glb_verts), glb_tris, "X.05 GLB")
    glb_comps = count_connected_components(len(glb_verts), glb_tris)
    if glb_comps != 1:
        raise AssertionError(f"X.05 GLB expected beta_0 = 1 connected component, got {glb_comps}")

    overhang = audit_mesh_overhang_angles(
        glb_verts,
        glb_tris,
        threshold_deg=threshold_deg,
        build_plate_z=0.0,
        label="X.05 GLB",
    )

    rings = extract_square_rings(glb_verts)
    if len(rings) != 4:
        raise AssertionError(f"X.05 expected 4 square cross-sectional stations, found {len(rings)}")
    if (
        abs(rings[0][0]) > 1e-4
        or abs(rings[-1][0] - height_mm) > 1e-4
        or abs(rings[-1][0] - float(exp_bmax[2])) > 1e-4
        or abs(2.0 * rings[0][1] - base_w) > 1e-4
        or abs(2.0 * rings[2][1] - waist_w) > 1e-4
        or abs(2.0 * rings[3][1] - crown_w) > 1e-4
    ):
        raise AssertionError(f"X.05 extracted rings {rings} disagree with z=0 build plate or manifest parameters {params}")

    frustum = compute_frustum_stack_volume(rings)
    frustum_vol = frustum["total_volume_mm3"]
    glb_vol = signed_mesh_volume(glb_verts, glb_tris)
    if abs(frustum_vol - float(exp["analytical_volume"])) > 1e-3 or abs(glb_vol - frustum_vol) > 1e-2:
        raise AssertionError(
            f"X.05 Moscow-Papyrus frustum volume {frustum_vol:.4f} disagrees with GLB {glb_vol:.4f} or manifest {exp['analytical_volume']}"
        )

    analytic_flare_deg = math.degrees(math.atan2(max(0.0, rings[3][1] - rings[2][1]), rings[3][0] - rings[2][0]))
    if (
        overhang["build_plate_base_faces"] != 2
        or overhang["upward_crown_faces"] != 2
        or overhang["inward_or_vertical_wall_faces"] != 16
        or overhang["downward_overhang_wall_faces"] != 8
        or abs(overhang["max_wall_overhang_deg"] - analytic_flare_deg) > 1e-3
        or abs(overhang["max_wall_overhang_deg"] - manifest_overhang_deg) > 1e-3
    ):
        raise AssertionError(f"X.05 overhang audit mismatch: {overhang} vs analytic {analytic_flare_deg:.4f} deg")

    # 2. Parse STEP Part-21 POLY_LOOP B-rep sketch and verify manifold, vertex congruence, volume, and overhang
    step_txt = (files_dir / "x05_artifact.step").read_text(encoding="utf-8")
    step_verts, step_tris, step_cp_count = parse_step_faceted_brep(step_txt)
    verify_strict_single_shell_2_manifold(len(step_verts), step_tris, "X.05 STEP")
    _assert_vertex_congruence(glb_verts, step_verts, "X.05 STEP")
    step_topo = check_manifold_topology(step_verts, step_tris)
    step_vol = signed_mesh_volume(step_verts, step_tris)
    if (
        not step_topo["is_watertight"]
        or step_topo["vertices"] != exp["vertices"]
        or step_topo["edges"] != exp["edges"]
        or step_topo["faces"] != exp["faces"]
        or step_topo["euler_characteristic"] != exp["euler_characteristic"]
        or abs(step_vol - frustum_vol) > 1e-2
    ):
        raise AssertionError(f"X.05 STEP topology/volume mismatch: topo={step_topo}, vol={step_vol:.4f}")
    audit_mesh_overhang_angles(
        step_verts,
        step_tris,
        threshold_deg=threshold_deg,
        build_plate_z=0.0,
        label="X.05 STEP",
    )

    # 3. Parse 3MF Core 1.2.3 ZIP archive and verify required entries, unit, identity transform, congruence, volume, and overhang
    tmf_raw = (files_dir / "x05_artifact.3mf").read_bytes()
    with zipfile.ZipFile(io.BytesIO(tmf_raw), "r") as zf:
        names = set(zf.namelist())
        for req_entry in ("[Content_Types].xml", "_rels/.rels", "3D/3dmodel.model"):
            if req_entry not in names:
                raise AssertionError(f"X.05 3MF archive missing required OPC entry {req_entry}")
        root = parse_3mf_model(zf.read("3D/3dmodel.model"), "x05_artifact.3mf")
    if root.attrib.get("unit") != "millimeter":
        raise AssertionError(f"X.05 3MF unit must be 'millimeter', got {root.attrib.get('unit')!r}")
    ns = {"m": NS_3MF_CORE}
    _verify_x05_3mf_identity_build_transform(root, ns)

    tmf_verts: list[Vec3] = []
    for v_el in root.findall("m:resources/m:object/m:mesh/m:vertices/m:vertex", ns):
        try:
            vx = float(v_el.attrib["x"])
            vy = float(v_el.attrib["y"])
            vz = float(v_el.attrib["z"])
        except (KeyError, ValueError) as exc:
            raise AssertionError(f"Invalid X.05 3MF vertex attribute: {exc}") from exc
        if not (math.isfinite(vx) and math.isfinite(vy) and math.isfinite(vz)):
            raise AssertionError("Non-finite X.05 3MF vertex coordinate")
        tmf_verts.append((vx, vy, vz))

    nv_tmf = len(tmf_verts)
    tmf_tris: list[Tri] = []
    for t_el in root.findall("m:resources/m:object/m:mesh/m:triangles/m:triangle", ns):
        try:
            i0 = int(t_el.attrib["v1"])
            i1 = int(t_el.attrib["v2"])
            i2 = int(t_el.attrib["v3"])
        except (KeyError, ValueError) as exc:
            raise AssertionError(f"Invalid X.05 3MF triangle index attribute: {exc}") from exc
        if not (0 <= i0 < nv_tmf and 0 <= i1 < nv_tmf and 0 <= i2 < nv_tmf):
            raise AssertionError(f"X.05 3MF triangle index ({i0}, {i1}, {i2}) out of bounds for {nv_tmf} vertices")
        tmf_tris.append((i0, i1, i2))

    verify_strict_single_shell_2_manifold(len(tmf_verts), tmf_tris, "X.05 3MF")
    _assert_vertex_congruence(glb_verts, tmf_verts, "X.05 3MF")
    tmf_topo = check_manifold_topology(tmf_verts, tmf_tris)
    tmf_vol = signed_mesh_volume(tmf_verts, tmf_tris)
    if (
        not tmf_topo["is_watertight"]
        or tmf_topo["vertices"] != exp["vertices"]
        or tmf_topo["edges"] != exp["edges"]
        or tmf_topo["faces"] != exp["faces"]
        or tmf_topo["euler_characteristic"] != exp["euler_characteristic"]
        or abs(tmf_vol - frustum_vol) > 1e-2
    ):
        raise AssertionError(f"X.05 3MF topology/volume mismatch: topo={tmf_topo}, vol={tmf_vol:.4f}")
    audit_mesh_overhang_angles(
        tmf_verts,
        tmf_tris,
        threshold_deg=threshold_deg,
        build_plate_z=0.0,
        label="X.05 3MF",
    )

    # 4. Deterministic negative controls: (a) excessive head flare (Delta_hw_top = 20 mm -> 51.3402 deg > 45 deg),
    #    and (b) suspended horizontal soffit above the build plate (90.0 deg > 45 deg).
    ko_rings = [(0.0, 20.0), (16.0, 16.0), (32.0, 12.0), (48.0, 32.0)]
    ko_verts, ko_tris = _build_parametric_strut_mesh(ko_rings)
    ko_frustum_vol = compute_frustum_stack_volume(ko_rings)["total_volume_mm3"]
    ko_overhang_deg = math.degrees(math.atan2(20.0, 16.0))
    try:
        audit_mesh_overhang_angles(ko_verts, ko_tris, threshold_deg=threshold_deg, build_plate_z=0.0, label="X.05 flare-knockout")
    except AssertionError as exc:
        if "exceeds threshold" not in str(exc):
            raise AssertionError(f"X.05 flare-knockout failed for unexpected reason: {exc}") from exc
    else:
        raise AssertionError("X.05 flare-knockout (Delta_hw_top = 20 mm -> 51.34 deg) was NOT rejected")

    suspended_verts = [(x, y, z + 10.0) for (x, y, z) in glb_verts]
    try:
        audit_mesh_overhang_angles(
            suspended_verts,
            glb_tris,
            threshold_deg=threshold_deg,
            build_plate_z=0.0,
            label="X.05 suspended-soffit-knockout",
        )
    except AssertionError as exc:
        if "90.0000 deg exceeds threshold" not in str(exc):
            raise AssertionError(f"X.05 suspended-soffit-knockout failed for unexpected reason: {exc}") from exc
    else:
        raise AssertionError("X.05 suspended horizontal soffit at z = 10 mm was NOT rejected")

    return {
        "glb_bytes": len(glb_raw),
        "glb_json_chunk_bytes": c0_len,
        "glb_bin_chunk_bytes": c1_len,
        "connected_components_beta0": glb_comps,
        "frustum_segment_volumes_mm3": [round(v, 4) for v in frustum["segment_volumes_mm3"]],
        "frustum_total_volume_mm3": round(frustum_vol, 3),
        "step_cartesian_points": step_cp_count,
        "step_vertex_points": step_topo["vertices"],
        "step_advanced_faces": step_topo["faces"],
        "step_signed_volume_mm3": round(step_vol, 3),
        "threemf_vertices": tmf_topo["vertices"],
        "threemf_faces": tmf_topo["faces"],
        "threemf_signed_volume_mm3": round(tmf_vol, 3),
        "build_plate_base_faces": overhang["build_plate_base_faces"],
        "upward_crown_faces": overhang["upward_crown_faces"],
        "inward_or_vertical_wall_faces": overhang["inward_or_vertical_wall_faces"],
        "downward_overhang_wall_faces": overhang["downward_overhang_wall_faces"],
        "min_signed_wall_tilt_deg": overhang["min_signed_wall_tilt_deg"],
        "max_wall_overhang_deg": overhang["max_wall_overhang_deg"],
        "knockout_flare20_volume_mm3": round(ko_frustum_vol, 3),
        "knockout_flare20_overhang_deg": round(ko_overhang_deg, 4),
    }
