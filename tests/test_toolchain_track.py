"""Verification suite for Track X: Tech & Tools · The Toolbox (X.01–X.06)."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "src"
SKILLS = ROOT / "skills"
TOOLCHAIN_SKILLS = SKILLS / "toolchain"
TOOLCHAIN_RESEARCH = RESEARCH / "toolchain"
SLUGS = ("x01", "x02", "x03", "x04", "x05", "x06", "x07")


class ToolchainTrackTests(unittest.TestCase):
    def test_glb_viewer_mjs_makes_zero_network_calls(self) -> None:
        viewer_mjs = (RESEARCH / "modules" / "glb-viewer.mjs").read_text(encoding="utf-8")
        code_only = re.sub(r"//.*?$|/\*.*?\*/", "", viewer_mjs, flags=re.M | re.S)
        forbidden = re.compile(r"\b(fetch|XMLHttpRequest|WebSocket|EventSource|sendBeacon)\b")
        m = forbidden.search(code_only)
        self.assertIsNone(m, f"Forbidden network API {m.group(0) if m else ''} in glb-viewer.mjs")

    def test_spdx_license_manifest_has_zero_copyleft_active_v1_tools(self) -> None:
        lic_path = TOOLCHAIN_SKILLS / "licenses.json"
        self.assertTrue(lic_path.is_file())
        data = json.loads(lic_path.read_text(encoding="utf-8"))
        self.assertRegex(data.get("audit_date", ""), r"^\d{4}-\d{2}-\d{2}$")
        tools = data.get("tools", [])
        active = [t for t in tools if t.get("category") in ("first_edition_active", "first_edition_compatible")]
        self.assertGreaterEqual(len(active), 4)
        for item in active:
            spdx = item.get("spdx_id", "")
            self.assertNotIn("GPL", spdx.upper(), f"Copyleft license {spdx} in active v1 tools")
            self.assertRegex(item.get("read_date", ""), r"^\d{4}-\d{2}-\d{2}$")

    def test_file_size_budgets_and_sha256_manifests(self) -> None:
        total_track_bytes = 0
        for slug in SLUGS:
            files_dir = TOOLCHAIN_RESEARCH / slug / "files"
            self.assertTrue(files_dir.is_dir(), f"Missing {files_dir}")
            manifest_path = files_dir / "manifest.json"
            self.assertTrue(manifest_path.is_file(), f"Missing {manifest_path}")
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest.get("license"), "CC0-1.0 / CC-BY-4.0")
            self.assertIn("Nothing here is certified as load-bearing", manifest.get("boundary_en", ""))
            self.assertIn("Nada aqu\u00ed est\u00e1 certificado como estructural", manifest.get("boundary_es", ""))

            folio_bytes = 0
            for entry in manifest["files"]:
                fpath = files_dir / entry["filename"]
                self.assertTrue(fpath.is_file(), f"Missing artifact {fpath}")
                raw = fpath.read_bytes()
                self.assertEqual(len(raw), entry["bytes"], f"Byte size mismatch for {fpath}")
                self.assertEqual(
                    hashlib.sha256(raw).hexdigest(),
                    entry["sha256"],
                    f"SHA-256 mismatch for {fpath}",
                )
                ext = fpath.suffix.lower()
                if ext in (".glb", ".3mf", ".dxf"):
                    self.assertLessEqual(len(raw), 512 * 1024, f"{fpath} exceeds 512 KB budget")
                elif ext == ".step":
                    self.assertLessEqual(len(raw), 1024 * 1024, f"{fpath} exceeds 1 MB budget")
                folio_bytes += len(raw)

            self.assertLessEqual(folio_bytes, int(1.5 * 1024 * 1024), f"{slug} exceeds 1.5 MB folio budget")
            total_track_bytes += folio_bytes

        self.assertLessEqual(total_track_bytes, 8 * 1024 * 1024, "Track X exceeds 8 MB total budget")

    def test_all_6_generators_and_verifiers_pass_and_planted_defects_fail(self) -> None:
        for slug in SLUGS:
            sdir = TOOLCHAIN_SKILLS / slug
            make_py = sdir / f"make_{slug}.py"
            self.assertTrue(make_py.is_file(), f"Missing {make_py}")
            verifiers = list(sdir.glob("verify_*.py"))
            self.assertEqual(len(verifiers), 1, f"Expected 1 verifier in {sdir}")
            verify_py = verifiers[0]

            # 1. Run generator and confirm exit 0
            gen_res = subprocess.run(
                [sys.executable, "-X", "utf8", str(make_py)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=20,
            )
            self.assertEqual(gen_res.returncode, 0, gen_res.stdout + gen_res.stderr)

            # 2. Run verifier in normal mode -> must exit 0 and return status == PASS
            ver_res = subprocess.run(
                [sys.executable, "-X", "utf8", str(verify_py)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=20,
            )
            self.assertEqual(ver_res.returncode, 0, ver_res.stdout + ver_res.stderr)
            payload = json.loads(ver_res.stdout)
            self.assertEqual(payload.get("status"), "PASS")
            self.assertEqual(
                payload.get("geometry_checks", {}).get("planted_defect_knockout"),
                "REJECTED_AS_EXPECTED",
            )

            # 3. Run verifier with --planted-defect -> MUST exit non-zero (knockout test!)
            bad_res = subprocess.run(
                [sys.executable, "-X", "utf8", str(verify_py), "--planted-defect"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=20,
            )
            self.assertNotEqual(
                bad_res.returncode,
                0,
                f"Verifier {verify_py.name} --planted-defect must fail with non-zero exit code!",
            )
            self.assertIn("FAIL", bad_res.stderr)

    def test_toolchain_claims_and_boundary_gate(self) -> None:
        res = subprocess.run(
            [sys.executable, "-X", "utf8", str(ROOT / "tools" / "check_toolchain_claims.py")],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=20,
        )
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: Tech & Tools claim, boundary & global FOSS compliance gate verified", res.stdout)
        self.assertIn("GCC-01..GCC-05", res.stdout)

    def test_five_pace_distillation_and_studio_quickstart_and_4200_word_depth(self) -> None:
        hub_html = (TOOLCHAIN_RESEARCH / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-studio-quickstart"', hub_html)
        for bridged in ("engineering/e10", "architecture/a11", "math/m10"):
            b_html = (RESEARCH / bridged / "index.html").read_text(encoding="utf-8")
            self.assertIn('class="tp-small-studio-box"', b_html, f"{bridged} missing Toolbox companion drawer")
        for slug in SLUGS:
            for base in (TOOLCHAIN_RESEARCH, RESEARCH / "es-mx" / "toolchain"):
                page = base / slug / "index.html"
                self.assertTrue(page.is_file(), f"Missing {page}")
                txt = page.read_text(encoding="utf-8")
                self.assertIn('class="tp-studio-quickstart"', txt, f"{page} missing studio quick-start bar")
                self.assertIn('class="tp-studio-dl-pill"', txt, f"{page} missing 1-click download pill")
                self.assertIn('class="tp-plain-bridge-box"', txt, f"{page} missing 5-Pace plain bridge")
                self.assertIn('class="tp-analogy-box"', txt, f"{page} missing 5-Pace tactile analogy")
                self.assertIn('class="tp-distill-figure"', txt, f"{page} missing Plate D distillation figure")
                self.assertIn('class="tp-distill-grid"', txt, f"{page} missing Plate D distillation grid")
                self.assertIn('class="tp-proof-spine"', txt, f"{page} missing formal proof spine")
                if base == TOOLCHAIN_RESEARCH:
                    paras = re.findall(r"<p\b[^>]*>(.*?)</p>", txt, flags=re.S)
                    self.assertGreaterEqual(len(paras), 52, f"{slug} has only {len(paras)} <p> paragraphs")
                    words = sum(len(re.sub(r"<[^>]+>", " ", p).split()) for p in paras)
                    self.assertGreaterEqual(words, 4200, f"{slug} has only {words} <p> words (< 4,200)")

    def test_modular_repo_layout_and_one_command_runner(self) -> None:
        for slug in SLUGS:
            self.assertTrue((ROOT / "tools" / "folios" / "toolchain" / f"{slug}.py").is_file())
        for bslug in ("b01", "b02", "b03", "b04", "b05", "b06"):
            self.assertTrue((ROOT / "tools" / "folios" / "bounties" / f"{bslug}.py").is_file())
        self.assertTrue((ROOT / "toolchain" / "README.md").is_file())
        self.assertTrue((ROOT / "skills" / "toolchain" / "README.md").is_file())
        runner = ROOT / "toolchain" / "run_all_toolchain.py"
        self.assertTrue(runner.is_file())
        res = subprocess.run(
            [sys.executable, "-X", "utf8", str(runner)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=30,
        )
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: All 7 Tech & Tools (The Toolbox)", res.stdout)


    def test_parametric_cad_browser_exporter_and_realtime_mesh_scaling(self) -> None:
        viewer_mjs = (RESEARCH / "modules" / "glb-viewer.mjs").read_text(encoding="utf-8")
        for sym in (
            "VIEWER_REGISTRY",
            "encodeCustomGlbBuffer",
            "encodeCustomStepString",
            "encodeCustomDxfString",
            "updateScale",
            "data-tc-export",
        ):
            self.assertIn(sym, viewer_mjs, f"Missing {sym} in glb-viewer.mjs")
        for slug in SLUGS:
            for base in (TOOLCHAIN_RESEARCH, RESEARCH / "es-mx" / "toolchain"):
                html = (base / slug / "index.html").read_text(encoding="utf-8")
                for fmt in ("glb", "step", "dxf"):
                    self.assertIn(f'data-tc-export="{fmt}"', html, f"{slug} missing {fmt} export button")
                self.assertIn("data-tc-export-status", html, f"{slug} missing export status caption")
                self.assertIn("<tp-article-audio", html, f"{slug} missing <tp-article-audio>")

    def test_bounties_five_pace_distillation_quickstart_and_60_folio_parity(self) -> None:
        bounties_res = RESEARCH / "bounties"
        hub_html = (bounties_res / "index.html").read_text(encoding="utf-8")
        self.assertIn('class="tp-studio-quickstart"', hub_html)
        for bslug in ("b01", "b02", "b03", "b04", "b05", "b06"):
            for base in (bounties_res, RESEARCH / "es-mx" / "bounties"):
                page = base / bslug / "index.html"
                self.assertTrue(page.is_file(), f"Missing {page}")
                txt = page.read_text(encoding="utf-8")
                self.assertIn('class="tp-studio-quickstart"', txt, f"{page} missing quick-start bar")
                self.assertIn('class="tp-studio-dl-pill"', txt, f"{page} missing quick-start pill")
                self.assertIn('class="tp-plain-bridge-box"', txt, f"{page} missing 5-Pace plain bridge")
                self.assertIn('class="tp-analogy-box"', txt, f"{page} missing 5-Pace analogy box")
                self.assertIn('class="tp-distill-figure"', txt, f"{page} missing Plate D distillation figure")
                self.assertIn('class="tp-distill-grid"', txt, f"{page} missing Plate D distillation grid")
                self.assertIn("<tp-article-audio", txt, f"{page} missing <tp-article-audio>")
                if base == bounties_res:
                    paras = re.findall(r"<p\b[^>]*>(.*?)</p>", txt, flags=re.S)
                    self.assertGreaterEqual(len(paras), 52, f"{bslug} has only {len(paras)} <p> paragraphs")
                    words = sum(len(re.sub(r"<[^>]+>", " ", p).split()) for p in paras)
                    self.assertGreaterEqual(words, 4200, f"{bslug} has only {words} <p> words (< 4,200)")

    def test_60_unique_plates_and_female_fast_audio_configuration(self) -> None:
        all_slugs = (
            [f"e{i:02d}" for i in range(1, 16)]
            + [f"a{i:02d}" for i in range(1, 15)]  # +A.14 (2026-11-21)
            + [f"p{i:02d}" for i in range(1, 13)]
            + [f"m{i:02d}" for i in range(1, 15)]  # +M.13, +M.14 (2026-11-21)
            + [f"b{i:02d}" for i in range(1, 7)]
            + [f"x{i:02d}" for i in range(1, 8)]
        )
        self.assertEqual(len(all_slugs), 68)  # +A.14, +M.13, +M.14 (2026-11-21)
        hashes: dict[str, str] = {}
        plates_dir = RESEARCH / "plates"
        for s in all_slugs:
            img_path = plates_dir / f"{s}.jpg"
            self.assertTrue(img_path.is_file(), f"Missing plate {img_path}")
            raw = img_path.read_bytes()
            self.assertGreater(len(raw), 10_000, f"Plate {img_path} is too small")
            h = hashlib.sha256(raw).hexdigest()
            self.assertNotIn(h, hashes, f"Duplicate plate SHA-256 between {s}.jpg and {hashes.get(h)}.jpg")
            hashes[h] = s

        audio_mjs = (RESEARCH / "modules" / "article-audio.mjs").read_text(encoding="utf-8")
        self.assertIn("const SPEEDS = [1.15, 1.35, 1.5, 1.0, 0.85];", audio_mjs)
        self.assertIn("ava|emma|jenny|aria|dalia", audio_mjs)
        audio_py = (ROOT / "tools" / "build_neural_audio.py").read_text(encoding="utf-8")
        self.assertIn('EN_VOICE = "en-US-AvaMultilingualNeural"', audio_py)
        self.assertIn('ES_VOICE_INF = "es-MX-DaliaNeural"', audio_py)
        self.assertIn('SPEECH_RATE = "+20%"', audio_py)

    def test_x02_cross_format_entity_parity_and_sagitta_verifier_rejects_drift(self) -> None:
        import io
        import shutil
        import tempfile
        import zipfile

        sys.path.insert(0, str(ROOT / "tools"))
        import toolchain_uga  # noqa: E402

        files_dir = TOOLCHAIN_RESEARCH / "x02" / "files"
        make_py = TOOLCHAIN_SKILLS / "x02" / "make_x02.py"
        res = toolchain_uga.verify_folio_assets("x02", files_dir, make_py)
        rt = res.get("x02_roundtrip_checks", {})
        self.assertEqual(rt.get("step_vertex_points"), 16)
        self.assertEqual(rt.get("step_poly_loops"), 28)
        self.assertEqual(rt.get("step_advanced_faces"), 28)
        self.assertEqual(rt.get("step_signed_volume_mm3"), 43200.0)
        self.assertEqual(rt.get("threemf_vertices"), 16)
        self.assertEqual(rt.get("threemf_faces"), 28)
        self.assertEqual(rt.get("threemf_signed_volume_mm3"), 43200.0)
        self.assertAlmostEqual(rt.get("chordal_sagitta_mm", 0.0), 0.072229, places=6)
        self.assertEqual(rt.get("min_facets_for_0p10mm"), 28)

        def _update_manifest_file(mpath: Path, fname: str, raw_bytes: bytes) -> None:
            mdata = json.loads(mpath.read_text(encoding="utf-8"))
            for f_entry in mdata["files"]:
                if f_entry["filename"] == fname:
                    f_entry["bytes"] = len(raw_bytes)
                    f_entry["sha256"] = hashlib.sha256(raw_bytes).hexdigest()
            mpath.write_text(json.dumps(mdata, indent=2) + "\n", encoding="utf-8", newline="\n")

        # 1. STEP comment-spoofed ADVANCED_FACE + zeroed coordinate -> must fail closed
        with tempfile.TemporaryDirectory() as td:
            tmp_dir = Path(td)
            shutil.copytree(files_dir, tmp_dir, dirs_exist_ok=True)
            step_path = tmp_dir / "x02_artifact.step"
            spoofed = (
                "/* #999 = ADVANCED_FACE('',(#998),#997,.T.); */\n"
                + step_path.read_text(encoding="utf-8").replace("ADVANCED_FACE(", "FACE_SURFACE(", 1)
            )
            raw_spoofed = spoofed.encode("utf-8")
            step_path.write_bytes(raw_spoofed)
            _update_manifest_file(tmp_dir / "manifest.json", "x02_artifact.step", raw_spoofed)
            with self.assertRaises(AssertionError):
                toolchain_uga.verify_folio_assets("x02", tmp_dir, make_py)

        # 2. STEP zeroed coordinates (volume collapse) -> must fail closed
        with tempfile.TemporaryDirectory() as td:
            tmp_dir = Path(td)
            shutil.copytree(files_dir, tmp_dir, dirs_exist_ok=True)
            step_path = tmp_dir / "x02_artifact.step"
            zeroed = re.sub(
                r"CARTESIAN_POINT\('',\([^)]+\)\)",
                "CARTESIAN_POINT('',(0.0,0.0,0.0))",
                step_path.read_text(encoding="utf-8"),
            )
            raw_zeroed = zeroed.encode("utf-8")
            step_path.write_bytes(raw_zeroed)
            _update_manifest_file(tmp_dir / "manifest.json", "x02_artifact.step", raw_zeroed)
            with self.assertRaisesRegex(AssertionError, "x02 STEP round-trip mismatch"):
                toolchain_uga.verify_folio_assets("x02", tmp_dir, make_py)

        # 3. 3MF unit changed to inch or out-of-bounds triangle index -> must raise AssertionError (not IndexError)
        for bad_mut, expected_msg in (
            (('unit="millimeter"', 'unit="inch"'), "x02 3MF unit"),
            (('v1="0"', 'v1="99"'), "x02 3MF triangle index out of bounds"),
        ):
            with tempfile.TemporaryDirectory() as td:
                tmp_dir = Path(td)
                shutil.copytree(files_dir, tmp_dir, dirs_exist_ok=True)
                tmf_path = tmp_dir / "x02_artifact.3mf"
                with zipfile.ZipFile(tmf_path, "r") as zf_in:
                    entries = {n: zf_in.read(n) for n in zf_in.namelist()}
                entries["3D/3dmodel.model"] = (
                    entries["3D/3dmodel.model"].decode("utf-8").replace(bad_mut[0], bad_mut[1], 1).encode("utf-8")
                )
                buf = io.BytesIO()
                with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf_out:
                    for n, b in entries.items():
                        zf_out.writestr(n, b)
                raw_tmf = buf.getvalue()
                tmf_path.write_bytes(raw_tmf)
                _update_manifest_file(tmp_dir / "manifest.json", "x02_artifact.3mf", raw_tmf)
                with self.assertRaisesRegex(AssertionError, expected_msg):
                    toolchain_uga.verify_folio_assets("x02", tmp_dir, make_py)

        # 4. Negative (-32) or zero (0) chordal_segments in manifest -> must raise AssertionError
        for bad_n in (-32, 0):
            with tempfile.TemporaryDirectory() as td:
                tmp_dir = Path(td)
                shutil.copytree(files_dir, tmp_dir, dirs_exist_ok=True)
                mpath = tmp_dir / "manifest.json"
                mdata = json.loads(mpath.read_text(encoding="utf-8"))
                mdata["parameters"]["chordal_segments"] = bad_n
                mpath.write_text(json.dumps(mdata, indent=2) + "\n", encoding="utf-8", newline="\n")
                with self.assertRaisesRegex(AssertionError, "x02 invalid bore parameters"):
                    toolchain_uga.verify_folio_assets("x02", tmp_dir, make_py)


if __name__ == "__main__":
    unittest.main()
