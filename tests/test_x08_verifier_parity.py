"""Adversarial parity, dual-method inertia, Jacobi triangle-inequality, and tip-over tests for Toolbox Folio X.08."""
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
from folios.toolchain import x08 as x08_folio  # noqa: E402
from toolchain_x08_checks import (  # noqa: E402
    audit_static_support_stability,
    build_parametric_cantilever_mesh,
    compute_fraction_cuboid_mass_properties,
    compute_simplex_mass_properties,
    convex_hull_2d,
    run_x08_mass_stability_checks,
    verify_inertia_realizability,
)


class X08VerifierParityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.files_dir = ROOT / "src" / "toolchain" / "x08" / "files"
        self.make_script = ROOT / "skills" / "toolchain" / "x08" / "make_x08.py"
        self.verify_script = ROOT / "skills" / "toolchain" / "x08" / "verify_x08_toolchain_x08_polyhedral_inertia_tipover.py"
        self.manifest = json.loads((self.files_dir / "manifest.json").read_text(encoding="utf-8"))

    def test_committed_x08_dual_method_inertia_jacobi_and_printed_readout_parity(self) -> None:
        res = toolchain_uga.verify_folio_assets("x08", self.files_dir, self.make_script)
        self.assertEqual(res["status"], "PASS")
        g = res["geometry_checks"]
        self.assertEqual((g["vertices"], g["edges"], g["faces"], g["euler_characteristic"]), (16, 42, 28, 2))
        self.assertAlmostEqual(g["signed_volume_mm3"], 48600.0, places=3)

        x08 = res["x08_mass_stability_checks"]
        self.assertEqual(20 + x08["glb_json_chunk_bytes"] + 8 + x08["glb_bin_chunk_bytes"], x08["glb_bytes"])
        self.assertEqual(x08["connected_components_beta0"], 1)
        self.assertEqual(x08["fraction_center_of_mass_exact"], ["81/5", "0", "153/5"])
        self.assertAlmostEqual(x08["center_of_mass_mm"][0], 16.2, places=5)
        self.assertAlmostEqual(x08["center_of_mass_mm"][1], 0.0, places=5)
        self.assertAlmostEqual(x08["center_of_mass_mm"][2], 30.6, places=5)
        self.assertLessEqual(x08["simplex_vs_fraction_max_inertia_diff_mm5"], 1e-8)

        pm = x08["principal_moments_mm5"]
        self.assertEqual(len(pm), 3)
        self.assertAlmostEqual(pm[0], 8092688.8241, places=3)
        self.assertAlmostEqual(pm[1], 16984911.1759, places=3)
        self.assertAlmostEqual(pm[2], 17787600.0, places=3)
        self.assertAlmostEqual(x08["triangle_inequality_slack_mm5"], 7290000.0, places=2)
        self.assertAlmostEqual(x08["support_area_mm2"], 720.0, places=3)
        self.assertAlmostEqual(x08["tip_margin_mm"], 7.8, places=5)
        self.assertAlmostEqual(x08["critical_tilt_deg"], math.degrees(math.atan2(7.8, 30.6)), places=4)
        self.assertAlmostEqual(x08["critical_cantilever_reach_mm"], 24.0 * math.sqrt(3.0), places=4)

        self.assertEqual(x08["step_vertex_points"], 16)
        self.assertEqual(x08["step_advanced_faces"], 28)
        self.assertAlmostEqual(x08["step_signed_volume_mm3"], 48600.0, places=3)
        self.assertEqual(x08["threemf_vertices"], 16)
        self.assertEqual(x08["threemf_faces"], 28)
        self.assertAlmostEqual(x08["threemf_signed_volume_mm3"], 48600.0, places=3)

        # Assert exact parity with the 4 printed readouts on the page
        ro = x08_folio.FOLIO["readouts"]
        self.assertEqual(ro[0]["value"], f"V={g['vertices']}, E={g['edges']}, F={g['faces']} \u00b7 \u03c7={g['euler_characteristic']}")
        self.assertEqual(
            ro[1]["value"],
            f"x_cm={x08['center_of_mass_mm'][0]:.2f} mm \u00b7 m_tip=+{x08['tip_margin_mm']:.2f} mm ({x08['critical_tilt_deg']:.2f}\u00b0)",
        )
        self.assertEqual(
            ro[2]["value"],
            f"{pm[0]/1e6:.2f} / {pm[1]/1e6:.2f} / {pm[2]/1e6:.2f} \u00d710\u2076 mm\u2075",
        )
        self.assertEqual(ro[3]["value"], "PASS \u00b7 STANDS IN BASE HULL")

    def test_tipover_triangle_inequality_and_base_winding_negative_controls_raise_named_errors(self) -> None:
        # 1. Near-critical reach L_c = 41.0 mm < 24*sqrt(3) = 41.5692 mm passes with positive m_tip
        v_ok, t_ok, _ = build_parametric_cantilever_mesh(24.0, 30.0, 36.0, 41.0, 18.0)
        p_ok = compute_simplex_mass_properties(v_ok, t_ok)
        f_ok = compute_fraction_cuboid_mass_properties(24.0, 30.0, 36.0, 41.0, 18.0)
        self.assertAlmostEqual(p_ok["volume_mm3"], f_ok["volume_mm3"], places=5)
        s_ok = audit_static_support_stability(v_ok, t_ok, p_ok["center_of_mass_mm"], support_z=0.0)
        self.assertGreater(s_ok["tip_margin_mm"], 0.0)
        self.assertLess(s_ok["tip_margin_mm"], 0.25)

        # 2. Slight breach L_c = 42.0 mm > 41.5692 mm at t_cap = 18 mm -> m_tip = -3/19 = -0.1579 mm fails with named margin
        v_42, t_42, _ = build_parametric_cantilever_mesh(24.0, 30.0, 36.0, 42.0, 18.0)
        p_42 = compute_simplex_mass_properties(v_42, t_42)
        with self.assertRaisesRegex(AssertionError, r"m_tip = -0\.1579 mm <= 0\.00 mm"):
            audit_static_support_stability(v_42, t_42, p_42["center_of_mass_mm"], support_z=0.0)

        # 3. Browser knockout (L_c = 48.0 mm, t_cap = 24.0 mm) -> exact m_tip = -4.0000 mm fails with named margin
        v_ko, t_ko, _ = build_parametric_cantilever_mesh(24.0, 30.0, 36.0, 48.0, 24.0)
        p_ko = compute_simplex_mass_properties(v_ko, t_ko)
        self.assertAlmostEqual(p_ko["volume_mm3"], 77760.0, places=4)
        self.assertAlmostEqual(p_ko["center_of_mass_mm"][0], 28.0, places=5)
        with self.assertRaisesRegex(AssertionError, r"m_tip = -4\.0000 mm <= 0\.00 mm"):
            audit_static_support_stability(v_ko, t_ko, p_ko["center_of_mass_mm"], support_z=0.0)

        # 4. Flipped z = 0 base triangle normal fails downward -Z check
        v_base, t_base, _ = build_parametric_cantilever_mesh(24.0, 30.0, 36.0, 18.0, 18.0)
        p_base = compute_simplex_mass_properties(v_base, t_base)
        bad_tris = list(t_base)
        for idx, (a, b, c) in enumerate(bad_tris):
            if v_base[a][2] == 0.0 and v_base[b][2] == 0.0 and v_base[c][2] == 0.0:
                bad_tris[idx] = (a, c, b)
                break
        with self.assertRaisesRegex(AssertionError, r"lacks downward -Z normal"):
            audit_static_support_stability(v_base, bad_tris, p_base["center_of_mass_mm"], support_z=0.0)

        # 5. Collinear intermediate points are stripped cleanly by convex_hull_2d
        hull = convex_hull_2d([(0.0, -15.0), (12.0, -15.0), (24.0, -15.0), (24.0, 0.0), (24.0, 15.0), (0.0, 15.0)])
        self.assertEqual(len(hull), 4)

        # 6. Non-physical inertia tensors fail with named errors
        with self.assertRaisesRegex(AssertionError, r"triangle inequality violated"):
            verify_inertia_realizability([[3.0e6, 0.0, 0.0], [0.0, 4.0e6, 0.0], [0.0, 0.0, 9.0e6]])
        with self.assertRaisesRegex(AssertionError, r"non-positive principal moment"):
            verify_inertia_realizability([[-1.0e5, 0.0, 0.0], [0.0, 5.0e6, 0.0], [0.0, 0.0, 5.0e6]])
        with self.assertRaisesRegex(AssertionError, r"asymmetric"):
            verify_inertia_realizability([[5.0e6, 100.0, 0.0], [0.0, 6.0e6, 0.0], [0.0, 0.0, 7.0e6]])

    def test_cli_planted_defect_cross_format_mutations_and_non_design_safety_boundary(self) -> None:
        bad_cli = subprocess.run(
            [sys.executable, "-X", "utf8", str(self.verify_script), "--planted-defect"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=20,
        )
        self.assertNotEqual(bad_cli.returncode, 0)
        self.assertIn("PLANTED_DEFECT_CAUGHT", bad_cli.stderr)
        self.assertIn("m_tip = -4.00 mm", bad_cli.stderr)

        g_x08 = toolchain_uga.build_x08_geometry()
        with tempfile.TemporaryDirectory() as tmp:
            fdir = Path(tmp) / "files"
            shutil.copytree(self.files_dir, fdir)

            # Translated STEP (+10 mm in X) fails vertex congruence
            step_path = fdir / "x08_artifact.step"
            step_orig = step_path.read_text(encoding="utf-8")
            shifted = [(x + 10.0, y, z) for (x, y, z) in g_x08["vertices"]]
            toolchain_uga.write_step_ap242(step_path, shifted, g_x08["triangles"], "X08_SHIFTED", {})
            with self.assertRaisesRegex(AssertionError, r"X\.08 STEP: vertex 0 .* differs from GLB"):
                run_x08_mass_stability_checks(fdir, self.manifest)
            step_path.write_text(step_orig, encoding="utf-8")

            # 3MF non-identity transform rejected
            tmf_path = fdir / "x08_artifact.3mf"
            with zipfile.ZipFile(tmf_path, "r") as zf_in:
                entries = {n: zf_in.read(n) for n in zf_in.namelist()}
            entries["3D/3dmodel.model"] = (
                entries["3D/3dmodel.model"]
                .decode("utf-8")
                .replace('<item objectid="1"/>', '<item objectid="1" transform="1 0 0 0 1 0 0 0 1 5 0 0"/>')
                .encode("utf-8")
            )
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf_out:
                for n, b in entries.items():
                    zf_out.writestr(n, b)
            tmf_path.write_bytes(buf.getvalue())
            with self.assertRaisesRegex(AssertionError, r"non-identity build transform"):
                run_x08_mass_stability_checks(fdir, self.manifest)

        # Check explicit non-design safety boundary across Act I, Spanish summary, and SKILL rules (0 'screening'/'design study')
        skill_txt = (ROOT / "skills" / "toolchain" / "x08" / "SKILL.md").read_text(encoding="utf-8")
        en_html = (ROOT / "src" / "toolchain" / "x08" / "index.html").read_text(encoding="utf-8")
        es_html = (ROOT / "src" / "es-mx" / "toolchain" / "x08" / "index.html").read_text(encoding="utf-8")
        self.assertIn("not a structural, seismic, foundation, rigging, or fabrication design method", x08_folio.FOLIO["act1_stakes"])
        self.assertIn("no un m\u00e9todo de dise\u00f1o estructural", x08_folio.FOLIO["plain_es"])
        self.assertIn("Non-Design Educational Safety Boundary", skill_txt)
        folio_blob = json.dumps(x08_folio.FOLIO, ensure_ascii=False).lower()
        for blob in (folio_blob, skill_txt.lower()):
            self.assertNotIn("design study", blob)
            self.assertNotIn("estudio de dise\u00f1o", blob)
            self.assertIsNone(re.search(r"\bscreening\b", blob), msg="Unexpected 'screening' claim in X.08")
        self.assertIn("non-design boundary", en_html.lower())
        self.assertIn("aviso educativo importante", es_html.lower())


if __name__ == "__main__":
    unittest.main()
