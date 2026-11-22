#!/usr/bin/env python3
"""Cross-format byte-level GLB, STEP Part-21 POLY_LOOP, and 3MF parity checks for Toolbox X.01."""

from __future__ import annotations

import io
import math
import re
import struct
import zipfile
from pathlib import Path
from typing import Any

Vec3 = tuple[float, float, float]
Tri = tuple[int, int, int]

_STEP_DATA_RE = re.compile(r"\bDATA\s*;(.*?)\bENDSEC\s*;", re.S)
_STEP_CP_RE = re.compile(
    r"#(\d+)\s*=\s*CARTESIAN_POINT\s*\(\s*'[^']*'\s*,\s*\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^)]+)\s*\)\s*\)\s*;"
)
_STEP_VP_RE = re.compile(r"#(\d+)\s*=\s*VERTEX_POINT\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*\)\s*;")
_STEP_DIR_RE = re.compile(
    r"#(\d+)\s*=\s*DIRECTION\s*\(\s*'[^']*'\s*,\s*\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^)]+)\s*\)\s*\)\s*;"
)
_STEP_AX_RE = re.compile(
    r"#(\d+)\s*=\s*AXIS2_PLACEMENT_3D\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*,\s*#(\d+)\s*,\s*[^)]+\)\s*;"
)
_STEP_PL_RE = re.compile(r"#(\d+)\s*=\s*PLANE\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*\)\s*;")
_STEP_LOOP_RE = re.compile(r"#(\d+)\s*=\s*POLY_LOOP\s*\(\s*'[^']*'\s*,\s*\(([^)]+)\)\s*\)\s*;")
_STEP_FOB_RE = re.compile(
    r"#(\d+)\s*=\s*FACE_OUTER_BOUND\s*\(\s*'[^']*'\s*,\s*#(\d+)\s*,\s*\.(T|F)\.\s*\)\s*;"
)
_STEP_AF_RE = re.compile(
    r"#(\d+)\s*=\s*ADVANCED_FACE\s*\(\s*'[^']*'\s*,\s*\(\s*#(\d+)\s*\)\s*,\s*#(\d+)\s*,\s*\.(T|F)\.\s*\)\s*;"
)
_STEP_SHELL_RE = re.compile(r"#(\d+)\s*=\s*CLOSED_SHELL\s*\(\s*'[^']*'\s*,\s*\(([^)]+)\)\s*\)\s*;")


def strip_step_comments_and_strings(step_text: str) -> str:
    """Strip /* ... */ comments and blank single-quoted string literals to ''.

    A "/*" inside a comment is refused. Whether such a comment ends at the first or the last "*/" decides what text
    is live, and a checker that guesses can be made to hide or reveal a unit declaration. A file that needs the
    guess is not accepted.
    """
    out: list[str] = []
    n = len(step_text)
    i = 0
    comment_depth = 0
    in_str = False
    while i < n:
        ch = step_text[i]
        nxt = step_text[i + 1] if i + 1 < n else ""
        if comment_depth > 0:
            if ch == "/" and nxt == "*":
                raise AssertionError("Nested /* inside a block comment in STEP file: ambiguous, not accepted")
            elif ch == "*" and nxt == "/":
                comment_depth -= 1
                i += 2
            else:
                if ch == "\n":
                    out.append("\n")
                i += 1
        elif in_str:
            if ch == "'" and nxt == "'":
                i += 2
            elif ch == "'":
                in_str = False
                out.append("'")
                i += 1
            else:
                if ch == "\n":
                    out.append("\n")
                i += 1
        else:
            if ch == "/" and nxt == "*":
                comment_depth = 1
                i += 2
            elif ch == "*" and nxt == "/":
                raise AssertionError("Unmatched */ comment delimiter in STEP file")
            elif ch == "'":
                in_str = True
                out.append("'")
                i += 1
            else:
                out.append(ch)
                i += 1
    if comment_depth != 0:
        raise AssertionError("Unclosed /* block comment in STEP file")
    if in_str:
        raise AssertionError("Unclosed string literal in STEP file")
    return "".join(out)


def count_connected_components(vertex_count: int, triangles: list[Tri]) -> int:
    """Count connected vertex-graph components (beta_0), counting isolated vertices individually."""
    if vertex_count == 0:
        return 0
    adj: list[set[int]] = [set() for _ in range(vertex_count)]
    for i0, i1, i2 in triangles:
        adj[i0].update((i1, i2))
        adj[i1].update((i0, i2))
        adj[i2].update((i0, i1))
    visited: set[int] = set()
    comps = 0
    for start in range(vertex_count):
        if start in visited:
            continue
        comps += 1
        stack = [start]
        visited.add(start)
        while stack:
            cur = stack.pop()
            for nxt in adj[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)
    return comps


def verify_strict_single_shell_2_manifold(vertex_count: int, triangles: list[Tri], label: str) -> None:
    """Verify paired half-edges, single dual face-edge component, and single-fan vertex links."""
    if vertex_count <= 0 or not triangles:
        raise AssertionError(f"{label}: empty vertex or triangle list")
    he_face: dict[tuple[int, int], int] = {}
    fans: list[dict[int, int]] = [{} for _ in range(vertex_count)]
    incident_counts = [0] * vertex_count

    for f_idx, (i0, i1, i2) in enumerate(triangles):
        if not (0 <= i0 < vertex_count and 0 <= i1 < vertex_count and 0 <= i2 < vertex_count):
            raise AssertionError(f"{label}: triangle {f_idx} index out of bounds")
        if i0 == i1 or i1 == i2 or i2 == i0:
            raise AssertionError(f"{label}: degenerate triangle {f_idx}")
        for u, v in ((i0, i1), (i1, i2), (i2, i0)):
            if (u, v) in he_face:
                raise AssertionError(f"{label}: duplicate directed half-edge ({u}, {v})")
            he_face[(u, v)] = f_idx
        for apex, u_spoke, w_spoke in ((i0, i1, i2), (i1, i2, i0), (i2, i0, i1)):
            if u_spoke in fans[apex]:
                raise AssertionError(f"{label}: non-manifold fan branch at vertex {apex}")
            fans[apex][u_spoke] = w_spoke
            incident_counts[apex] += 1

    for u, v in he_face:
        if (v, u) not in he_face:
            raise AssertionError(f"{label}: unpaired directed half-edge ({u}, {v})")

    # 1. Dual face-edge connectivity (rules out edge-disjoint shells pinched at shared vertices)
    seen_faces = {0}
    f_stack = [0]
    while f_stack:
        cur_f = f_stack.pop()
        a, b, c = triangles[cur_f]
        for u, v in ((a, b), (b, c), (c, a)):
            nbr_f = he_face[(v, u)]
            if nbr_f not in seen_faces:
                seen_faces.add(nbr_f)
                f_stack.append(nbr_f)
    if len(seen_faces) != len(triangles):
        raise AssertionError(
            f"{label}: dual face-edge graph has multiple shells ({len(seen_faces)}/{len(triangles)} faces reached)"
        )

    # 2. Single-umbrella vertex-link cycle at every vertex (rules out unreferenced and pinch vertices)
    for v_idx in range(vertex_count):
        fan = fans[v_idx]
        deg = incident_counts[v_idx]
        if deg == 0 or len(fan) != deg:
            raise AssertionError(f"{label}: isolated or malformed vertex link at vertex {v_idx}")
        start_spoke = next(iter(fan))
        cur = start_spoke
        steps = 0
        while True:
            cur = fan.get(cur, -1)
            if cur == -1:
                raise AssertionError(f"{label}: open boundary fan at vertex {v_idx}")
            steps += 1
            if cur == start_spoke or steps > deg:
                break
        if cur != start_spoke or steps != deg:
            raise AssertionError(f"{label}: non-manifold multi-umbrella pinch at vertex {v_idx}")


def parse_step_faceted_brep(step_text: str) -> tuple[list[Vec3], list[Tri], int]:
    """Parse an ISO 10303-21 faceted POLY_LOOP B-rep solid after lexing comments and string literals."""
    sanitized = strip_step_comments_and_strings(step_text)
    m_data = _STEP_DATA_RE.search(sanitized)
    if not m_data:
        raise AssertionError("STEP file missing DATA; ... ENDSEC; section")
    data_sec = m_data.group(1)
    if re.search(r"\bCONVERSION_BASED_UNIT\b", data_sec) or not re.search(
        r"#\d+\s*=\s*\([^;]*\bLENGTH_UNIT\s*\(\s*\)[^;]*\bSI_UNIT\s*\(\s*\.MILLI\.\s*,\s*\.METRE\.\s*\)",
        data_sec,
    ):
        raise AssertionError("STEP DATA section missing millimeter LENGTH_UNIT / SI_UNIT(.MILLI.,.METRE.)")

    cps: dict[int, Vec3] = {}
    for m in _STEP_CP_RE.finditer(data_sec):
        pts = (float(m.group(2)), float(m.group(3)), float(m.group(4)))
        if not all(math.isfinite(c) for c in pts):
            raise AssertionError("Non-finite CARTESIAN_POINT coordinate in STEP")
        cps[int(m.group(1))] = pts

    vp_to_idx: dict[int, int] = {}
    vertices: list[Vec3] = []
    for m in _STEP_VP_RE.finditer(data_sec):
        vp_id = int(m.group(1))
        cp_id = int(m.group(2))
        if cp_id not in cps:
            raise AssertionError(f"STEP VERTEX_POINT #{vp_id} references missing CARTESIAN_POINT #{cp_id}")
        if vp_id in vp_to_idx:
            raise AssertionError(f"Duplicate STEP VERTEX_POINT #{vp_id}")
        vp_to_idx[vp_id] = len(vertices)
        vertices.append(cps[cp_id])

    dirs: dict[int, Vec3] = {}
    for m in _STEP_DIR_RE.finditer(data_sec):
        dvec = (float(m.group(2)), float(m.group(3)), float(m.group(4)))
        if not all(math.isfinite(c) for c in dvec):
            raise AssertionError("Non-finite DIRECTION vector in STEP")
        d_mag = math.sqrt(dvec[0] * dvec[0] + dvec[1] * dvec[1] + dvec[2] * dvec[2])
        if d_mag <= 1e-12:
            raise AssertionError(f"Zero-length STEP DIRECTION #{m.group(1)}")
        dirs[int(m.group(1))] = (dvec[0] / d_mag, dvec[1] / d_mag, dvec[2] / d_mag)

    axes: dict[int, int] = {int(m.group(1)): int(m.group(3)) for m in _STEP_AX_RE.finditer(data_sec)}
    planes: dict[int, Vec3] = {}
    for m in _STEP_PL_RE.finditer(data_sec):
        pl_id = int(m.group(1))
        ax_id = int(m.group(2))
        dir_id = axes.get(ax_id, -1)
        if dir_id not in dirs:
            raise AssertionError(f"STEP PLANE #{pl_id} missing AXIS2_PLACEMENT_3D / DIRECTION")
        planes[pl_id] = dirs[dir_id]

    loops: dict[int, list[int]] = {}
    for m in _STEP_LOOP_RE.finditer(data_sec):
        refs = [int(tok.strip().lstrip("#")) for tok in m.group(2).split(",") if tok.strip()]
        if len(refs) != 3:
            raise AssertionError(f"STEP POLY_LOOP #{m.group(1)} does not have 3 vertices")
        for r_id in refs:
            if r_id not in vp_to_idx:
                raise AssertionError(f"STEP POLY_LOOP #{m.group(1)} references missing VERTEX_POINT #{r_id}")
        loops[int(m.group(1))] = [vp_to_idx[r_id] for r_id in refs]

    fobs: dict[int, tuple[int, bool]] = {
        int(m.group(1)): (int(m.group(2)), m.group(3) == "T")
        for m in _STEP_FOB_RE.finditer(data_sec)
    }

    faces: dict[int, Tri] = {}
    for m in _STEP_AF_RE.finditer(data_sec):
        af_id = int(m.group(1))
        fob_id = int(m.group(2))
        pl_id = int(m.group(3))
        same_sense = m.group(4) == "T"
        if fob_id not in fobs or pl_id not in planes:
            raise AssertionError(f"STEP ADVANCED_FACE #{af_id} missing FACE_OUTER_BOUND or PLANE")
        loop_id, fob_sense = fobs[fob_id]
        if loop_id not in loops:
            raise AssertionError(f"STEP FACE_OUTER_BOUND #{fob_id} missing POLY_LOOP #{loop_id}")
        i0, i1, i2 = loops[loop_id]
        if not fob_sense:
            i1, i2 = i2, i1
        if not same_sense:
            i1, i2 = i2, i1
        p0, p1, p2 = vertices[i0], vertices[i1], vertices[i2]
        ux, uy, uz = p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]
        vx, vy, vz = p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]
        nx, ny, nz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
        n_mag = math.sqrt(nx * nx + ny * ny + nz * nz)
        if n_mag <= 1e-12:
            raise AssertionError(f"Degenerate STEP ADVANCED_FACE #{af_id}")
        pdir = planes[pl_id]
        if not same_sense:
            pdir = (-pdir[0], -pdir[1], -pdir[2])
        align = (nx * pdir[0] + ny * pdir[1] + nz * pdir[2]) / n_mag
        if align < 0.999:
            raise AssertionError(f"STEP ADVANCED_FACE #{af_id} normal disagrees with PLANE DIRECTION (dot={align:.4f})")
        faces[af_id] = (i0, i1, i2)

    shells = list(_STEP_SHELL_RE.finditer(data_sec))
    if len(shells) != 1:
        raise AssertionError(f"Expected 1 STEP CLOSED_SHELL, found {len(shells)}")
    shell_refs = [int(tok.strip().lstrip("#")) for tok in shells[0].group(2).split(",") if tok.strip()]
    if len(shell_refs) != len(faces) or set(shell_refs) != set(faces.keys()):
        raise AssertionError("STEP CLOSED_SHELL face list does not match defined ADVANCED_FACE entities")
    triangles = [faces[fid] for fid in shell_refs]
    return vertices, triangles, len(cps)


def _assert_vertex_congruence(ref_verts: list[Vec3], cand_verts: list[Vec3], label: str, tol: float = 1e-4) -> None:
    if len(ref_verts) != len(cand_verts):
        raise AssertionError(f"{label}: vertex count {len(cand_verts)} != GLB {len(ref_verts)}")
    for idx, (pa, pb) in enumerate(zip(ref_verts, cand_verts)):
        if max(abs(pa[0] - pb[0]), abs(pa[1] - pb[1]), abs(pa[2] - pb[2])) > tol:
            raise AssertionError(f"{label}: vertex {idx} {pb} differs from GLB {pa}")


def _verify_3mf_identity_build_transform(root: Any, ns: dict[str, str]) -> None:
    objs = root.findall("m:resources/m:object", ns)
    items = root.findall("m:build/m:item", ns)
    if len(objs) != 1 or len(items) != 1:
        raise AssertionError(f"X.01 3MF expected 1 object and 1 build item, got {len(objs)} and {len(items)}")
    obj_id = objs[0].attrib.get("id")
    if items[0].attrib.get("objectid") != obj_id:
        raise AssertionError("X.01 3MF build item objectid does not match object id")
    tf_raw = items[0].attrib.get("transform")
    if tf_raw is not None:
        parts = [float(x) for x in tf_raw.split()]
        ident = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
        if len(parts) != 12 or any(not math.isfinite(x) for x in parts) or any(
            abs(a - b) > 1e-6 for a, b in zip(parts, ident)
        ):
            raise AssertionError(f"X.01 3MF build item carries non-identity transform: {tf_raw!r}")


def run_x01_cross_format_checks(files_dir: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    """Verify X.01 byte-level GLB structure, STEP Part-21 B-rep, 3MF XML mesh, and 4 fuzz reasons."""
    from toolchain_uga import (  # local import avoids circular dependency
        NS_3MF_CORE,
        check_manifold_topology,
        parse_3mf_model,
        parse_glb,
        signed_mesh_volume,
    )

    params = manifest.get("parameters", {})
    lx = float(params.get("length_mm", 0.0))
    ly = float(params.get("width_mm", 0.0))
    lz = float(params.get("height_mm", 0.0))
    if lx <= 0.0 or ly <= 0.0 or lz <= 0.0:
        raise AssertionError(f"X.01 prism dimensions must be positive: ({lx}, {ly}, {lz})")
    exp_vol = lx * ly * lz
    exp = manifest["expected_geometry"]
    if abs(exp_vol - float(exp["analytical_volume"])) > 1e-6:
        raise AssertionError("X.01 parameter product disagrees with manifest analytical_volume")

    # 1. GLB chunk & strict single-shell 2-manifold check
    glb_raw = (files_dir / "x01_artifact.glb").read_bytes()
    parsed_glb = parse_glb(glb_raw)
    c0_len, _ = struct.unpack_from("<2I", glb_raw, 12)
    c1_len, _ = struct.unpack_from("<2I", glb_raw, 20 + c0_len)
    if 20 + c0_len + 8 + c1_len != len(glb_raw):
        raise AssertionError("X.01 GLB chunk lengths do not sum to total byte length")
    glb_verts = parsed_glb["vertices"]
    glb_tris = parsed_glb["triangles"]
    verify_strict_single_shell_2_manifold(len(glb_verts), glb_tris, "X.01 GLB")
    glb_comps = count_connected_components(len(glb_verts), glb_tris)

    # 2. STEP Part-21 POLY_LOOP B-rep check + coordinate congruence with GLB
    step_txt = (files_dir / "x01_artifact.step").read_text(encoding="utf-8")
    step_verts, step_tris, step_cp_count = parse_step_faceted_brep(step_txt)
    verify_strict_single_shell_2_manifold(len(step_verts), step_tris, "X.01 STEP")
    _assert_vertex_congruence(glb_verts, step_verts, "X.01 STEP")
    step_topo = check_manifold_topology(step_verts, step_tris)
    step_vol = signed_mesh_volume(step_verts, step_tris)
    if (
        not step_topo["is_watertight"]
        or step_topo["vertices"] != exp["vertices"]
        or step_topo["edges"] != exp["edges"]
        or step_topo["faces"] != exp["faces"]
        or step_topo["euler_characteristic"] != exp["euler_characteristic"]
        or abs(step_vol - exp_vol) > 1e-2
    ):
        raise AssertionError(f"X.01 STEP topology/volume mismatch: topo={step_topo}, vol={step_vol}")

    # 3. 3MF Core 1.2.3 XML mesh check + build transform + coordinate congruence with GLB
    tmf_raw = (files_dir / "x01_artifact.3mf").read_bytes()
    with zipfile.ZipFile(io.BytesIO(tmf_raw), "r") as zf:
        names = set(zf.namelist())
        for req_entry in ("[Content_Types].xml", "_rels/.rels", "3D/3dmodel.model"):
            if req_entry not in names:
                raise AssertionError(f"X.01 3MF archive missing {req_entry}")
        root = parse_3mf_model(zf.read("3D/3dmodel.model"), "x01_artifact.3mf")
    if root.attrib.get("unit") != "millimeter":
        raise AssertionError(f"X.01 3MF unit must be 'millimeter', got {root.attrib.get('unit')!r}")
    ns = {"m": NS_3MF_CORE}
    _verify_3mf_identity_build_transform(root, ns)
    tmf_verts: list[Vec3] = []
    for v_el in root.findall("m:resources/m:object/m:mesh/m:vertices/m:vertex", ns):
        try:
            vx = float(v_el.attrib["x"])
            vy = float(v_el.attrib["y"])
            vz = float(v_el.attrib["z"])
        except (KeyError, ValueError) as exc:
            raise AssertionError(f"Invalid 3MF vertex attribute: {exc}") from exc
        if not (math.isfinite(vx) and math.isfinite(vy) and math.isfinite(vz)):
            raise AssertionError("Non-finite 3MF vertex coordinate")
        tmf_verts.append((vx, vy, vz))
    nv_tmf = len(tmf_verts)
    tmf_tris: list[Tri] = []
    for t_el in root.findall("m:resources/m:object/m:mesh/m:triangles/m:triangle", ns):
        try:
            i0 = int(t_el.attrib["v1"])
            i1 = int(t_el.attrib["v2"])
            i2 = int(t_el.attrib["v3"])
        except (KeyError, ValueError) as exc:
            raise AssertionError(f"Invalid 3MF triangle index attribute: {exc}") from exc
        if not (0 <= i0 < nv_tmf and 0 <= i1 < nv_tmf and 0 <= i2 < nv_tmf):
            raise AssertionError(f"3MF triangle index ({i0}, {i1}, {i2}) out of bounds for {nv_tmf} vertices")
        tmf_tris.append((i0, i1, i2))

    verify_strict_single_shell_2_manifold(len(tmf_verts), tmf_tris, "X.01 3MF")
    _assert_vertex_congruence(glb_verts, tmf_verts, "X.01 3MF")
    tmf_topo = check_manifold_topology(tmf_verts, tmf_tris)
    tmf_vol = signed_mesh_volume(tmf_verts, tmf_tris)
    if (
        not tmf_topo["is_watertight"]
        or tmf_topo["vertices"] != exp["vertices"]
        or tmf_topo["edges"] != exp["edges"]
        or tmf_topo["faces"] != exp["faces"]
        or tmf_topo["euler_characteristic"] != exp["euler_characteristic"]
        or abs(tmf_vol - exp_vol) > 1e-2
    ):
        raise AssertionError(f"X.01 3MF topology/volume mismatch: topo={tmf_topo}, vol={tmf_vol}")

    # 4. Specific defect-reason verification on the 4 fuzz fixtures
    for fname, needle in (
        ("fuzz/fuzz_01_truncated_header.glb", "too short"),
        ("fuzz/fuzz_02_chunk_oob.glb", "exceeds file size"),
        ("fuzz/fuzz_03_index_oob.glb", "exceeds vertex count"),
    ):
        try:
            parse_glb((files_dir / fname).read_bytes())
        except ValueError as exc:
            if needle not in str(exc):
                raise AssertionError(f"{fname} failed with unexpected message: {exc}") from exc
        else:
            raise AssertionError(f"{fname} unexpectedly passed parse_glb")

    f4_parsed = parse_glb((files_dir / "fuzz/fuzz_04_non_manifold.glb").read_bytes())
    f4_topo = check_manifold_topology(f4_parsed["vertices"], f4_parsed["triangles"])
    f4_vol = signed_mesh_volume(f4_parsed["vertices"], f4_parsed["triangles"])
    if (
        f4_topo["is_watertight"]
        or f4_topo["duplicate_half_edges"] != 3
        or f4_topo["unpaired_half_edges"] != 3
        or abs(f4_vol - 22000.0) > 1e-2
    ):
        raise AssertionError(f"fuzz_04_non_manifold unexpected diagnostics: topo={f4_topo}, vol={f4_vol}")

    return {
        "glb_bytes": len(glb_raw),
        "glb_json_chunk_bytes": c0_len,
        "glb_bin_chunk_bytes": c1_len,
        "connected_components_beta0": glb_comps,
        "step_cartesian_points": step_cp_count,
        "step_vertex_points": step_topo["vertices"],
        "step_advanced_faces": step_topo["faces"],
        "step_signed_volume_mm3": round(step_vol, 3),
        "threemf_vertices": tmf_topo["vertices"],
        "threemf_faces": tmf_topo["faces"],
        "threemf_signed_volume_mm3": round(tmf_vol, 3),
        "flipped_tri0_signed_volume_mm3": round(f4_vol, 3),
    }
