"""Adversarial parity and negative-control tests for Toolbox Folio X.01."""
from __future__ import annotations

import hashlib
import io
import json
import math
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import toolchain_uga  # noqa: E402
from folios.toolchain import x01 as x01_folio  # noqa: E402
from toolchain_x01_checks import (  # noqa: E402
    count_connected_components,
    parse_step_faceted_brep,
    run_x01_cross_format_checks,
    verify_strict_single_shell_2_manifold,
)


class X01VerifierParityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.files_dir = ROOT / "src" / "toolchain" / "x01" / "files"
        self.make_script = ROOT / "skills" / "toolchain" / "x01" / "make_x01.py"
        self.manifest = json.loads((self.files_dir / "manifest.json").read_text(encoding="utf-8"))

    def test_committed_x01_manifest_sha256_and_cross_format_parity(self) -> None:
        self.assertEqual(
            hashlib.sha256(self.make_script.read_bytes()).hexdigest(),
            "6a30774411e9ca3f5c88ac7fb33982ad1de73c72e402ac98c530b5c41edb5480",
        )
        res = toolchain_uga.verify_folio_assets("x01", self.files_dir, self.make_script)
        self.assertEqual(res["status"], "PASS")
        x01 = res["x01_format_checks"]
        self.assertEqual(x01["glb_bytes"], 2716)
        self.assertEqual(x01["glb_json_chunk_bytes"], 1896)
        self.assertEqual(x01["glb_bin_chunk_bytes"], 792)
        self.assertEqual(x01["connected_components_beta0"], 1)
        self.assertEqual(x01["step_cartesian_points"], 38)
        self.assertEqual(x01["step_vertex_points"], 14)
        self.assertEqual(x01["step_advanced_faces"], 24)
        self.assertAlmostEqual(x01["step_signed_volume_mm3"], 24000.0, places=3)
        self.assertEqual(x01["threemf_vertices"], 14)
        self.assertEqual(x01["threemf_faces"], 24)
        self.assertAlmostEqual(x01["threemf_signed_volume_mm3"], 24000.0, places=3)
        self.assertAlmostEqual(x01["flipped_tri0_signed_volume_mm3"], 22000.0, places=3)

    def test_parse_glb_rejects_unaligned_chunks_bad_bufferviews_unreferenced_accessors_and_nan(self) -> None:
        raw = bytearray((self.files_dir / "x01_artifact.glb").read_bytes())
        c0_len, _ = struct.unpack_from("<2I", raw, 12)

        # 1. Non-4-byte-aligned JSON chunk length
        bad_align = bytearray(raw)
        struct.pack_into("<I", bad_align, 12, c0_len - 1)
        with self.assertRaisesRegex(ValueError, "4-byte aligned"):
            toolchain_uga.parse_glb(bytes(bad_align))

        c1_offset = 20 + c0_len
        c1_len, _ = struct.unpack_from("<2I", raw, c1_offset)
        bin_chunk = raw[c1_offset + 8 : c1_offset + 8 + c1_len]
        gltf_base = json.loads(raw[20 : 20 + c0_len].decode("utf-8"))

        def _pack_custom_glb(gltf_obj: dict, bchunk: bytes) -> bytes:
            jb = json.dumps(gltf_obj, separators=(",", ":"), sort_keys=True).encode("utf-8")
            while len(jb) % 4 != 0:
                jb += b" "
            tot = 20 + len(jb) + 8 + len(bchunk)
            return (
                struct.pack("<3I", 0x46546C67, 2, tot)
                + struct.pack("<2I", len(jb), 0x4E4F534A)
                + jb
                + struct.pack("<2I", len(bchunk), 0x004E4942)
                + bchunk
            )

        # 2. Mutate JSON bufferView[1] (NORMAL) out of bounds
        g_bv_oob = json.loads(json.dumps(gltf_base))
        g_bv_oob["bufferViews"][1]["byteLength"] = 9999
        with self.assertRaisesRegex(ValueError, "bufferView\\[1\\]"):
            toolchain_uga.parse_glb(_pack_custom_glb(g_bv_oob, bin_chunk))

        # 3. Accessor byteOffset pushes slice past its own bufferView even though still inside BIN
        g_acc_oob = json.loads(json.dumps(gltf_base))
        g_acc_oob["accessors"][0]["byteOffset"] = 24
        with self.assertRaisesRegex(ValueError, "Accessor 0 span"):
            toolchain_uga.parse_glb(_pack_custom_glb(g_acc_oob, bin_chunk))

        # 4. Unreferenced extra accessor with out-of-bounds byteOffset is also caught
        g_extra_acc = json.loads(json.dumps(gltf_base))
        g_extra_acc["accessors"].append(
            {"bufferView": 0, "byteOffset": 99999, "componentType": 5126, "count": 1, "type": "VEC3"}
        )
        with self.assertRaisesRegex(ValueError, "Accessor 4 span"):
            toolchain_uga.parse_glb(_pack_custom_glb(g_extra_acc, bin_chunk))

        # 5. Wrong POSITION type (SCALAR instead of VEC3) is rejected
        g_bad_type = json.loads(json.dumps(gltf_base))
        g_bad_type["accessors"][0]["type"] = "SCALAR"
        with self.assertRaisesRegex(ValueError, "type 'SCALAR' != 'VEC3'"):
            toolchain_uga.parse_glb(_pack_custom_glb(g_bad_type, bin_chunk))

        # 6. Non-finite NaN in POSITION float buffer
        bad_bin = bytearray(bin_chunk)
        struct.pack_into("<f", bad_bin, 0, float("nan"))
        with self.assertRaisesRegex(ValueError, "Non-finite POSITION"):
            toolchain_uga.parse_glb(_pack_custom_glb(gltf_base, bytes(bad_bin)))

        # 7. Zero-vector NORMAL fails unit-length check
        zero_norm_bin = bytearray(bin_chunk)
        struct.pack_into("<3f", zero_norm_bin, 168, 0.0, 0.0, 0.0)
        with self.assertRaisesRegex(ValueError, "Non-unit NORMAL"):
            toolchain_uga.parse_glb(_pack_custom_glb(gltf_base, bytes(zero_norm_bin)))

    def test_step_comments_strings_directions_pinch_shells_and_3mf_transforms(self) -> None:
        step_txt = (self.files_dir / "x01_artifact.step").read_text(encoding="utf-8")

        # 1a. Nested ISO 10303-21 block comment cannot spoof SI_UNIT(.MILLI.,.METRE.)
        nested_spoof = step_txt.replace(
            "SI_UNIT(.MILLI.,.METRE.)",
            "CONVERSION_BASED_UNIT('INCH',#5) /* outer /* inner */ SI_UNIT(.MILLI.,.METRE.) */",
        )
        with self.assertRaisesRegex(AssertionError, "SI_UNIT"):
            parse_step_faceted_brep(nested_spoof)

        # 1b. String literal inside PRODUCT(...) cannot spoof SI_UNIT(.MILLI.,.METRE.)
        str_spoof = step_txt.replace(
            "'Educational CAD Solid'",
            "'SI_UNIT(.MILLI.,.METRE.)'",
        ).replace("SI_UNIT(.MILLI.,.METRE.)", "SI_UNIT($,.METRE.)")
        with self.assertRaisesRegex(AssertionError, "SI_UNIT"):
            parse_step_faceted_brep(str_spoof)

        # 2a. Unnormalized nearly orthogonal DIRECTION (1000, 0, -1) is rejected after normalization
        tilted_dir = step_txt.replace(
            "#38 = DIRECTION('',(0.000000,0.000000,-1.000000));",
            "#38 = DIRECTION('',(1000.000000,0.000000,-1.000000));",
            1,
        )
        self.assertNotEqual(tilted_dir, step_txt)
        with self.assertRaisesRegex(AssertionError, "PLANE DIRECTION"):
            parse_step_faceted_brep(tilted_dir)

        # 2b. Valid non-unit STEP DIRECTION (0, 0, -0.5) is accepted
        non_unit_dir = step_txt.replace(
            "#38 = DIRECTION('',(0.000000,0.000000,-1.000000));",
            "#38 = DIRECTION('',(0.000000,0.000000,-0.500000));",
            1,
        )
        nu_v, nu_t, _ = parse_step_faceted_brep(non_unit_dir)
        self.assertEqual((len(nu_v), len(nu_t)), (14, 24))

        # 3. Dropping one face from CLOSED_SHELL fails face-set parity
        dropped_shell = re.sub(
            r"(CLOSED_SHELL\s*\(\s*'[^']*'\s*,\s*\()\s*#\d+\s*,",
            r"\1",
            step_txt,
            count=1,
        )
        self.assertNotEqual(dropped_shell, step_txt)
        with self.assertRaisesRegex(AssertionError, "CLOSED_SHELL"):
            parse_step_faceted_brep(dropped_shell)

        # 4. Isolated vertex component count (beta_0) is exact
        self.assertEqual(count_connected_components(4, [(0, 1, 2)]), 2)
        g_box = toolchain_uga.build_x01_geometry()
        self.assertEqual(count_connected_components(15, g_box["triangles"]), 2)

        # 5. Two bipyramids (4-gon + 8-gon) pinched at 2 shared poles -> V=14, E=36, F=24, chi=2
        # Passes basic half-edge pairing and vertex-graph beta_0=1, MUST fail strict single-shell 2-manifold!
        # Vertices: 0 = south pole, 1 = north pole, 2..5 = 4-ring, 6..13 = 8-ring (total 14 vertices)
        pinch_tris: list[tuple[int, int, int]] = []
        for k in range(4):
            u = 2 + k
            v = 2 + ((k + 1) % 4)
            pinch_tris.append((1, u, v))
            pinch_tris.append((0, v, u))
        for k in range(8):
            u = 6 + k
            v = 6 + ((k + 1) % 8)
            pinch_tris.append((1, u, v))
            pinch_tris.append((0, v, u))
        pinch_verts = [(0.0, 0.0, -1.0), (0.0, 0.0, 1.0)] + [
            (math.cos(i), math.sin(i), 0.0) for i in range(12)
        ]
        pinch_topo = toolchain_uga.check_manifold_topology(pinch_verts, pinch_tris)
        self.assertTrue(pinch_topo["is_watertight"])
        self.assertEqual((pinch_topo["vertices"], pinch_topo["edges"], pinch_topo["faces"], pinch_topo["euler_characteristic"]), (14, 36, 24, 2))
        self.assertEqual(count_connected_components(14, pinch_tris), 1)
        with self.assertRaisesRegex(AssertionError, "multiple shells"):
            verify_strict_single_shell_2_manifold(14, pinch_tris, "pinched-2-shell")

        # 6. STEP coordinate shift and 3MF non-identity <item transform> / unit / OOB index fail
        with tempfile.TemporaryDirectory() as tmp:
            fdir = Path(tmp) / "files"
            shutil.copytree(self.files_dir, fdir)

            # 6a. Rigidly translated STEP solid (+50 mm in X, preserving PLANE normals and 24,000 mm^3 volume) breaks congruence with GLB
            step_path = fdir / "x01_artifact.step"
            shifted_verts = [(x + 50.0, y, z) for (x, y, z) in g_box["vertices"]]
            toolchain_uga.write_step_ap242(step_path, shifted_verts, g_box["triangles"], "X01_SHIFTED", {})
            with self.assertRaisesRegex(AssertionError, "differs from GLB"):
                run_x01_cross_format_checks(fdir, self.manifest)
            step_path.write_text(step_txt, encoding="utf-8")

            tmf_path = fdir / "x01_artifact.3mf"
            with zipfile.ZipFile(tmf_path, "r") as zf:
                entries = {n: zf.read(n) for n in zf.namelist()}
            model_xml = entries["3D/3dmodel.model"].decode("utf-8")

            def _write_3mf_xml(xml_str: str) -> None:
                buf = io.BytesIO()
                with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf_out:
                    for k, v in entries.items():
                        zf_out.writestr(k, xml_str.encode("utf-8") if k.endswith(".model") else v)
                tmf_path.write_bytes(buf.getvalue())

            # 6b. Non-identity <item transform> rejected
            _write_3mf_xml(
                model_xml.replace('<item objectid="1"/>', '<item objectid="1" transform="2 0 0 0 2 0 0 0 2 0 0 0"/>')
            )
            with self.assertRaisesRegex(AssertionError, "non-identity transform"):
                run_x01_cross_format_checks(fdir, self.manifest)

            # 6c. unit="inch" rejected
            _write_3mf_xml(model_xml.replace('unit="millimeter"', 'unit="inch"'))
            with self.assertRaisesRegex(AssertionError, "millimeter"):
                run_x01_cross_format_checks(fdir, self.manifest)

            # 6d. Out-of-bounds v1="99" raises AssertionError (never IndexError)
            _write_3mf_xml(model_xml.replace('v1="0"', 'v1="99"', 1))
            with self.assertRaisesRegex(AssertionError, "out of bounds"):
                run_x01_cross_format_checks(fdir, self.manifest)

    def test_glb_viewer_mjs_static_alignment(self) -> None:
        mjs_path = ROOT / "src" / "modules" / "glb-viewer.mjs"
        mjs = mjs_path.read_text(encoding="utf-8")
        self.assertIn("glTF v2 · 2,716 B (PASS)", mjs)
        self.assertNotIn("1,708 B", mjs)
        self.assertIn("3 DUP / 3 UNPAIRED", mjs)
        self.assertIn("(11.0 / 12.0) * vol", mjs)
        self.assertIn("AP242_MANAGED_MODEL_BASED_3D_ENGINEERING_MIM_LF", mjs)
        self.assertNotIn("AUTOMOTIVE_DESIGN { 1 0 10303 214", mjs)
        self.assertNotIn("Certified Geometry Regime", mjs)
        self.assertIn("Verified Geometry Regime", mjs)
        self.assertIn("Number.isInteger(accOff)", mjs)
        self.assertEqual(x01_folio.FOLIO["pass_pill_es"], "APROBADO · χ = 2 · V = 24,000 mm³ · 4/4 FUZZ RECHAZADOS")

    def test_node_esm_glb_and_step_roundtrip(self) -> None:
        mjs_path = ROOT / "src" / "modules" / "glb-viewer.mjs"
        node_bin = shutil.which("node")
        if not node_bin:
            self.skipTest("SKIPPED Node ESM round-trip: node is not on PATH")
        js_harness = (
            "import fs from 'node:fs';\n"
            f"import {{ parseGlbBuffer, encodeCustomStepString }} from {json.dumps(mjs_path.as_uri())};\n"
            f"const raw = fs.readFileSync({json.dumps(str(self.files_dir / 'x01_artifact.glb'))});\n"
            "const ab = raw.buffer.slice(raw.byteOffset, raw.byteOffset + raw.byteLength);\n"
            "const parsed = parseGlbBuffer(ab);\n"
            "const stepOut = encodeCustomStepString(parsed, [1, 1, 1], \"bad');\\n/*INJECT*/\", 40, 20);\n"
            "function repack(mutFn) {\n"
            "  const view = new DataView(ab.slice(0));\n"
            "  const c0Len = view.getUint32(12, true);\n"
            "  const gltf = JSON.parse(new TextDecoder().decode(new Uint8Array(ab, 20, c0Len)));\n"
            "  mutFn(gltf);\n"
            "  let jb = Buffer.from(JSON.stringify(gltf), 'utf8');\n"
            "  while (jb.length % 4 !== 0) jb = Buffer.concat([jb, Buffer.from(' ')]);\n"
            "  const binPart = Buffer.from(ab, 20 + c0Len);\n"
            "  const hdr = Buffer.alloc(20);\n"
            "  hdr.writeUInt32LE(0x46546c67, 0); hdr.writeUInt32LE(2, 4); hdr.writeUInt32LE(20 + jb.length + binPart.length, 8);\n"
            "  hdr.writeUInt32LE(jb.length, 12); hdr.writeUInt32LE(0x4e4f534a, 16);\n"
            "  const out = Buffer.concat([hdr, jb, binPart]);\n"
            "  return out.buffer.slice(out.byteOffset, out.byteOffset + out.byteLength);\n"
            "}\n"
            "for (const bad of [\n"
            "  repack((g) => { g.accessors[0].byteOffset = 24; }),\n"
            "  repack((g) => { g.accessors[0].byteOffset = '0'; }),\n"
            "  repack((g) => { g.accessors[0].count = 0.5; }),\n"
            "]) {\n"
            "  let caught = false;\n"
            "  try { parseGlbBuffer(bad); } catch { caught = true; }\n"
            "  if (!caught) process.exit(2);\n"
            "}\n"
            "process.stdout.write(stepOut);\n"
        )
        proc = subprocess.run(
            [node_bin, "--input-type=module", "-e", js_harness],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=15,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertNotIn("INJECT", proc.stdout)
        self.assertNotIn("bad'", proc.stdout)
        b_verts, b_tris, _ = parse_step_faceted_brep(proc.stdout)
        verify_strict_single_shell_2_manifold(len(b_verts), b_tris, "browser-exported STEP")
        self.assertAlmostEqual(toolchain_uga.signed_mesh_volume(b_verts, b_tris), 24000.0, places=2)


if __name__ == "__main__":
    unittest.main()
