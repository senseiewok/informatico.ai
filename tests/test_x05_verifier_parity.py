"""Adversarial parity, overhang-trigonometry, and negative-control tests for Toolbox Folio X.05."""
from __future__ import annotations

import hashlib
import io
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import toolchain_uga  # noqa: E402
from folios.toolchain import x05 as x05_folio  # noqa: E402
from toolchain_x01_checks import parse_step_faceted_brep, verify_strict_single_shell_2_manifold  # noqa: E402
from toolchain_x05_checks import (  # noqa: E402
    _build_parametric_strut_mesh,
    audit_mesh_overhang_angles,
    compute_frustum_stack_volume,
    extract_square_rings,
    run_x05_strut_checks,
)


class X05VerifierParityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.files_dir = ROOT / "src" / "toolchain" / "x05" / "files"
        self.make_script = ROOT / "skills" / "toolchain" / "x05" / "make_x05.py"
        self.verify_script = ROOT / "skills" / "toolchain" / "x05" / "verify_x05_toolchain_x05_simp_manifold_3mf.py"
        self.manifest = json.loads((self.files_dir / "manifest.json").read_text(encoding="utf-8"))

    def test_committed_x05_manifest_sha256_frustum_volume_overhang_and_cross_format_parity(self) -> None:
        self.assertEqual(
            hashlib.sha256(self.make_script.read_bytes()).hexdigest(),
            "d6f7c184f3bddfad27851a144cda2924393554136fa722c87ee70f3c5da9a58b",
        )
        res = toolchain_uga.verify_folio_assets("x05", self.files_dir, self.make_script)
        self.assertEqual(res["status"], "PASS")
        x05 = res["x05_strut_checks"]
        self.assertEqual(x05["glb_bytes"], 2936)
        self.assertEqual(20 + x05["glb_json_chunk_bytes"] + 8 + x05["glb_bin_chunk_bytes"], 2936)
        self.assertEqual(x05["connected_components_beta0"], 1)

        segs = x05["frustum_segment_volumes_mm3"]
        self.assertEqual(len(segs), 3)
        self.assertAlmostEqual(segs[0], 20821.3333, places=3)
        self.assertAlmostEqual(segs[1], 12629.3333, places=3)
        self.assertAlmostEqual(segs[2], 12629.3333, places=3)
        self.assertAlmostEqual(x05["frustum_total_volume_mm3"], 46080.0, places=3)

        self.assertEqual(x05["step_vertex_points"], 16)
        self.assertEqual(x05["step_advanced_faces"], 28)
        self.assertAlmostEqual(x05["step_signed_volume_mm3"], 46080.0, places=3)
        self.assertEqual(x05["threemf_vertices"], 16)
        self.assertEqual(x05["threemf_faces"], 28)
        self.assertAlmostEqual(x05["threemf_signed_volume_mm3"], 46080.0, places=3)

        self.assertEqual(x05["build_plate_base_faces"], 2)
        self.assertEqual(x05["upward_crown_faces"], 2)
        self.assertEqual(x05["inward_or_vertical_wall_faces"], 16)
        self.assertEqual(x05["downward_overhang_wall_faces"], 8)
        self.assertAlmostEqual(x05["min_signed_wall_tilt_deg"], -14.0362, places=3)
        self.assertAlmostEqual(x05["max_wall_overhang_deg"], 14.0362, places=3)
        self.assertAlmostEqual(x05["knockout_flare20_volume_mm3"], 66560.0, places=2)
        self.assertAlmostEqual(x05["knockout_flare20_overhang_deg"], 51.3402, places=3)

        # Explicitly check arcsin(-n.z_hat) = 14.0362 deg vs polar complement arccos(-n.z_hat) = 75.9638 deg
        down_sin = 4.0 / math.hypot(16.0, 4.0)
        self.assertAlmostEqual(math.degrees(math.asin(down_sin)), 14.036243, places=5)
        self.assertAlmostEqual(math.degrees(math.acos(down_sin)), 75.963757, places=5)

    def test_overhang_audit_rejects_flare_breach_and_suspended_soffit_with_named_errors(self) -> None:
        # 1. Exact 45.0 deg boundary (Delta_hw_top = 16.0 mm over Delta_z = 16.0 mm) passes
        v_45, t_45 = _build_parametric_strut_mesh([(0.0, 20.0), (16.0, 16.0), (32.0, 12.0), (48.0, 28.0)])
        ok_45 = audit_mesh_overhang_angles(v_45, t_45, threshold_deg=45.0, build_plate_z=0.0)
        self.assertAlmostEqual(ok_45["max_wall_overhang_deg"], 45.0, places=4)

        # 2. Segment-2 flare when mid-span waist w_2 = 36 mm (hw_2 = 18 mm > hw_1 = 16 mm) and Delta_hw_top = 0
        v_s2, t_s2 = _build_parametric_strut_mesh([(0.0, 20.0), (16.0, 16.0), (32.0, 18.0), (48.0, 18.0)])
        ok_s2 = audit_mesh_overhang_angles(v_s2, t_s2, threshold_deg=45.0, build_plate_z=0.0)
        self.assertAlmostEqual(ok_s2["max_wall_overhang_deg"], math.degrees(math.atan2(2.0, 16.0)), places=3)

        # 3. Slight breach above 45 deg (Delta_hw_top = 16.5 mm -> 45.8814 deg) fails with named angle
        v_46, t_46 = _build_parametric_strut_mesh([(0.0, 20.0), (16.0, 16.0), (32.0, 12.0), (48.0, 28.5)])
        with self.assertRaisesRegex(AssertionError, r"45\.8814 deg exceeds threshold 45\.00 deg"):
            audit_mesh_overhang_angles(v_46, t_46, threshold_deg=45.0, build_plate_z=0.0)

        # 4. Browser knockout flare (Delta_hw_top = 20.0 mm -> 51.3402 deg) fails with named angle
        v_ko, t_ko = _build_parametric_strut_mesh([(0.0, 20.0), (16.0, 16.0), (32.0, 12.0), (48.0, 32.0)])
        with self.assertRaisesRegex(AssertionError, r"51\.3402 deg exceeds threshold 45\.00 deg"):
            audit_mesh_overhang_angles(v_ko, t_ko, threshold_deg=45.0, build_plate_z=0.0)

        # 5. Suspended horizontal soffit at z = 10 mm above build_plate_z = 0.0 fails at 90.0000 deg
        g_base = toolchain_uga.build_x05_geometry()
        lifted_verts = [(x, y, z + 10.0) for (x, y, z) in g_base["vertices"]]
        with self.assertRaisesRegex(AssertionError, r"90\.0000 deg exceeds threshold 45\.00 deg"):
            audit_mesh_overhang_angles(lifted_verts, g_base["triangles"], threshold_deg=45.0, build_plate_z=0.0)

        # 6. Flipped z = 0 base triangle normal fails build-plate -Z orientation check
        bad_base_tris = list(g_base["triangles"])
        i0, i1, i2 = bad_base_tris[0]
        bad_base_tris[0] = (i0, i2, i1)
        with self.assertRaisesRegex(AssertionError, r"lacks downward -Z normal"):
            audit_mesh_overhang_angles(g_base["vertices"], bad_base_tris, threshold_deg=45.0, build_plate_z=0.0)

        # 7. Out-of-domain threshold rejected
        with self.assertRaisesRegex(AssertionError, r"must lie in \(0, 90\)"):
            audit_mesh_overhang_angles(g_base["vertices"], g_base["triangles"], threshold_deg=0.0)

        # 8. Non-square ring station rejected by extract_square_rings
        skew_verts = list(g_base["vertices"])
        skew_verts[0] = (-22.0, -20.0, 0.0)
        with self.assertRaisesRegex(AssertionError, r"not a centered square ring"):
            extract_square_rings(skew_verts)

        # 9. Non-increasing frustum station z rejected
        with self.assertRaisesRegex(AssertionError, r"Invalid frustum station pair"):
            compute_frustum_stack_volume([(0.0, 20.0), (0.0, 16.0)])

    def test_cross_format_negative_controls_step_3mf_and_flipped_triangles(self) -> None:
        g_x05 = toolchain_uga.build_x05_geometry()
        step_orig = (self.files_dir / "x05_artifact.step").read_text(encoding="utf-8")

        # 1. Flipping Triangle 0 (on z = 0 plane) breaks half-edge pairing while signed volume stays 46,080.0 mm^3;
        #    flipping Crown Triangle 26 (on z = 48 plane) drops signed volume by 16,384.0 to 29,696.0 mm^3.
        tris_flip0 = list(g_x05["triangles"])
        a0, b0, c0 = tris_flip0[0]
        tris_flip0[0] = (a0, c0, b0)
        topo_flip0 = toolchain_uga.check_manifold_topology(g_x05["vertices"], tris_flip0)
        self.assertFalse(topo_flip0["is_watertight"])
        self.assertEqual((topo_flip0["duplicate_half_edges"], topo_flip0["unpaired_half_edges"]), (3, 3))
        self.assertAlmostEqual(toolchain_uga.signed_mesh_volume(g_x05["vertices"], tris_flip0), 46080.0, places=3)

        tris_flip_top = list(g_x05["triangles"])
        at, bt, ct = tris_flip_top[-2]
        tris_flip_top[-2] = (at, ct, bt)
        self.assertAlmostEqual(toolchain_uga.signed_mesh_volume(g_x05["vertices"], tris_flip_top), 29696.0, places=3)

        # 2. CLI --planted-defect exits non-zero with expected message
        bad_cli = subprocess.run(
            [sys.executable, "-X", "utf8", str(self.verify_script), "--planted-defect"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=20,
        )
        self.assertNotEqual(bad_cli.returncode, 0)
        self.assertIn("PLANTED_DEFECT_CAUGHT", bad_cli.stderr)
        self.assertIn("51.34 deg", bad_cli.stderr)

        with tempfile.TemporaryDirectory() as tmp:
            fdir = Path(tmp) / "files"
            shutil.copytree(self.files_dir, fdir)

            # 3a. Translated STEP (+25 mm in X) fails vertex congruence with GLB
            step_path = fdir / "x05_artifact.step"
            shifted_verts = [(x + 25.0, y, z) for (x, y, z) in g_x05["vertices"]]
            toolchain_uga.write_step_ap242(step_path, shifted_verts, g_x05["triangles"], "X05_SHIFTED", {})
            with self.assertRaisesRegex(AssertionError, r"X\.05 STEP: vertex 0 .* differs from GLB"):
                run_x05_strut_checks(fdir, self.manifest)

            # 3b. Dropped face in STEP CLOSED_SHELL rejected
            dropped_shell = re.sub(
                r"(CLOSED_SHELL\s*\(\s*'[^']*'\s*,\s*\()\s*#\d+\s*,",
                r"\1",
                step_orig,
                count=1,
            )
            step_path.write_text(dropped_shell, encoding="utf-8")
            with self.assertRaisesRegex(AssertionError, r"CLOSED_SHELL"):
                run_x05_strut_checks(fdir, self.manifest)
            step_path.write_text(step_orig, encoding="utf-8")

            tmf_path = fdir / "x05_artifact.3mf"
            with zipfile.ZipFile(tmf_path, "r") as zf:
                entries = {n: zf.read(n) for n in zf.namelist()}
            model_xml = entries["3D/3dmodel.model"].decode("utf-8")

            def _write_3mf(custom_entries: dict[str, bytes]) -> None:
                buf = io.BytesIO()
                with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf_out:
                    for k, v in custom_entries.items():
                        zf_out.writestr(k, v)
                tmf_path.write_bytes(buf.getvalue())

            # 3c. Missing _rels/.rels OPC entry rejected
            missing_rels = {k: v for k, v in entries.items() if k != "_rels/.rels"}
            _write_3mf(missing_rels)
            with self.assertRaisesRegex(AssertionError, r"missing required OPC entry _rels/\.rels"):
                run_x05_strut_checks(fdir, self.manifest)

            # 3d. unit="inch" rejected
            _write_3mf({**entries, "3D/3dmodel.model": model_xml.replace('unit="millimeter"', 'unit="inch"').encode("utf-8")})
            with self.assertRaisesRegex(AssertionError, r"unit must be 'millimeter'"):
                run_x05_strut_checks(fdir, self.manifest)

            # 3e. Non-identity <item transform> rejected
            _write_3mf(
                {
                    **entries,
                    "3D/3dmodel.model": model_xml.replace(
                        '<item objectid="1"/>', '<item objectid="1" transform="2 0 0 0 2 0 0 0 2 0 0 0"/>'
                    ).encode("utf-8"),
                }
            )
            with self.assertRaisesRegex(AssertionError, r"non-identity transform"):
                run_x05_strut_checks(fdir, self.manifest)

            # 3f. Out-of-bounds triangle vertex index raises AssertionError (never IndexError)
            _write_3mf({**entries, "3D/3dmodel.model": model_xml.replace('v2="3"', 'v2="99"', 1).encode("utf-8")})
            with self.assertRaisesRegex(AssertionError, r"out of bounds"):
                run_x05_strut_checks(fdir, self.manifest)

            # 3g. Non-numeric <item transform> raises AssertionError (never ValueError)
            _write_3mf(
                {
                    **entries,
                    "3D/3dmodel.model": model_xml.replace(
                        '<item objectid="1"/>', '<item objectid="1" transform="abc"/>'
                    ).encode("utf-8"),
                }
            )
            with self.assertRaisesRegex(AssertionError, r"non-numeric transform"):
                run_x05_strut_checks(fdir, self.manifest)

            # 3h. Lifting all three files (GLB + STEP + 3MF) by +10 mm above z = 0 fails closed on 90.0 deg soffit
            lifted_verts = [(x, y, z + 10.0) for (x, y, z) in g_x05["vertices"]]
            toolchain_uga.write_glb(fdir / "x05_artifact.glb", lifted_verts, g_x05["triangles"], g_x05["colors"], {})
            toolchain_uga.write_step_ap242(step_path, lifted_verts, g_x05["triangles"], "X05_LIFTED", {})
            toolchain_uga.write_3mf(tmf_path, lifted_verts, g_x05["triangles"], "X05_LIFTED", {})
            with self.assertRaisesRegex(AssertionError, r"90\.0000 deg exceeds threshold"):
                run_x05_strut_checks(fdir, self.manifest)

        # 4. IEEE-754 NaN and degenerate hw=0 station fail closed
        ko_verts, ko_tris = _build_parametric_strut_mesh([(0.0, 20.0), (16.0, 16.0), (32.0, 12.0), (48.0, 32.0)])
        with self.assertRaisesRegex(AssertionError, r"overhang threshold"):
            audit_mesh_overhang_angles(ko_verts, ko_tris, threshold_deg=float("nan"), build_plate_z=0.0)
        with self.assertRaisesRegex(AssertionError, r"build_plate_z must be finite"):
            audit_mesh_overhang_angles(g_x05["vertices"], g_x05["triangles"], threshold_deg=45.0, build_plate_z=float("nan"))
        with self.assertRaisesRegex(AssertionError, r"Invalid frustum station"):
            compute_frustum_stack_volume([(0.0, 20.0), (16.0, float("nan"))])
        with self.assertRaisesRegex(AssertionError, r"non-positive half-width"):
            extract_square_rings([(0.0, 0.0, 0.0)] * 4)

    def test_glb_viewer_mjs_and_folio_rule5_alignment(self) -> None:
        mjs_path = ROOT / "src" / "modules" / "glb-viewer.mjs"
        mjs = mjs_path.read_text(encoding="utf-8")
        self.assertIn("export function buildParametricMesh(", mjs)
        self.assertIn("const dhw2 = 0.5 * p0 - 16.0;", mjs)
        self.assertIn("const maxFlare = Math.max(0.0, dhw2, p1);", mjs)
        self.assertIn('overhangOk ? "≤" : ">"', mjs)
        self.assertIn('else if (slug === "x05") { s0.value = "24"; s1.value = "20"; }', mjs)
        self.assertIn("gl.bufferData(gl.ARRAY_BUFFER, curMesh.normals, gl.DYNAMIC_DRAW);", mjs)

        f = x05_folio.FOLIO
        self.assertIn("arcsin(max(0, −n_f · ẑ))", f["governing_law"])
        self.assertNotIn("arccos", f["governing_law"])
        self.assertNotIn("arccos", f["subtitle"])
        self.assertNotIn("production-ready", json.dumps(f).lower())
        self.assertIn("explanation, not a design method", f["act1_body"])
        self.assertIn("none of its numbers or files may be used on a real structure", f["act1_body"])
        self.assertIn("no un método de diseño estructural", f["plain_es"].lower())
        self.assertIn("ninguna de sus cifras o archivos puede usarse en una estructura real", f["plain_es"].lower())
        self.assertIn("not a structural design method", f["rules"][0])
        self.assertIn("none of their numbers or files may be used on a real structure", f["rules"][0])
        self.assertNotIn("OpenCascade EDGE_LOOP STEP AP242 in Feeney", f["act1_body"])
        self.assertNotIn("alongside unit-aware 3MF Core XML archives", json.dumps(f["chronology"]))

        for built_rel in ("src/toolchain/x05/index.html", "src/es-mx/toolchain/x05/index.html", "src/llms.txt"):
            built_txt = (ROOT / built_rel).read_text(encoding="utf-8")
            self.assertNotIn("SIMP Structural Lattices", built_txt, built_rel)
            self.assertNotIn("SIMP structural struts are synthesized", built_txt, built_rel)

    def test_node_esm_x05_ring_deformation_and_exports(self) -> None:
        mjs_path = ROOT / "src" / "modules" / "glb-viewer.mjs"
        node_bin = shutil.which("node")
        if not node_bin:
            self.skipTest("SKIPPED Node ESM X.05 round-trip: node is not on PATH")
        js_harness = (
            "import fs from 'node:fs';\n"
            f"import {{ parseGlbBuffer, buildParametricMesh, encodeCustomGlbBuffer, encodeCustomStepString, encodeCustomDxfString }} from {json.dumps(mjs_path.as_uri())};\n"
            f"const raw = fs.readFileSync({json.dumps(str(self.files_dir / 'x05_artifact.glb'))});\n"
            "const ab = raw.buffer.slice(raw.byteOffset, raw.byteOffset + raw.byteLength);\n"
            "const parsed = parseGlbBuffer(ab);\n"
            "const mBase = buildParametricMesh(parsed, [1, 1, 1], 'x05', 24, 4);\n"
            "const mKo = buildParametricMesh(parsed, [1, 2, 1], 'x05', 24, 20);\n"
            "const glbKo = encodeCustomGlbBuffer(parsed, [1, 2, 1], 'x05', 24, 20);\n"
            "const parsedKo = parseGlbBuffer(glbKo);\n"
            "const stepKo = encodeCustomStepString(parsed, [1, 2, 1], 'x05', 24, 20);\n"
            "const dxfBad = encodeCustomDxfString(parsed, [1, 1, 1], 'bad\\n0\\nEOF', 24, 4);\n"
            "process.stdout.write(JSON.stringify({baseVol: mBase.signedVolume, koVol: mKo.signedVolume, glbKoVol: parsedKo.signedVolume, koBmax: mKo.bmax, dxfSafe: !dxfBad.includes('BAD\\n0\\nEOF')}) + '\\n===STEP===\\n' + stepKo);\n"
        )
        proc = subprocess.run(
            [node_bin, "--input-type=module", "-e", js_harness],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=15,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        meta_str, step_ko = proc.stdout.split("\n===STEP===\n", 1)
        meta = json.loads(meta_str)
        self.assertAlmostEqual(meta["baseVol"], 46080.0, places=1)
        self.assertAlmostEqual(meta["koVol"], 66560.0, places=1)
        self.assertAlmostEqual(meta["glbKoVol"], 66560.0, places=1)
        self.assertEqual(meta["koBmax"], [32.0, 32.0, 48.0])
        self.assertTrue(meta["dxfSafe"])
        s_verts, s_tris, _ = parse_step_faceted_brep(step_ko)
        verify_strict_single_shell_2_manifold(len(s_verts), s_tris, "X.05 knockout STEP")
        self.assertAlmostEqual(toolchain_uga.signed_mesh_volume(s_verts, s_tris), 66560.0, places=1)
        with self.assertRaisesRegex(AssertionError, r"51\.3402 deg exceeds threshold"):
            audit_mesh_overhang_angles(s_verts, s_tris, threshold_deg=45.0, build_plate_z=0.0)


if __name__ == "__main__":
    unittest.main()
