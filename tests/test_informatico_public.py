"""Verification suite for the standalone public Informatico.ai repository."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "src" / "research"
SKILLS = ROOT / "skills"
BOUNTIES = ROOT / "bounties"


class PublicInformaticoRepoTests(unittest.TestCase):
    def test_all_48_skills_and_python_verifiers_exist_and_pass(self) -> None:
        skill_files = list(SKILLS.glob("*/*/SKILL.md"))
        py_files = list(SKILLS.glob("*/*/verify_*.py"))
        self.assertEqual(len(skill_files), 48)
        self.assertEqual(len(py_files), 48)
        res = subprocess.run([sys.executable, "-X", "utf8", str(SKILLS / "verify_all_48_folios.py")], capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: All 48/48", res.stdout)

    def test_all_6_bounty_and_physics_discovery_harnesses_pass(self) -> None:
        res = subprocess.run([sys.executable, "-X", "utf8", str(BOUNTIES / "run_all_bounties.py")], capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: 6/6 Open-Bounty & Physics/Math Discovery Crucible benchmarks verified.", res.stdout)

    def test_48_folios_citation_gate_passes_offline(self) -> None:
        res = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "tools" / "check_folio_citations.py"), "--offline"], capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("SUMMARY essays=48 fail=0 warn=0 unchecked=0", res.stdout)

    def test_106_bilingual_pages_and_bounty_crucible_mounted(self) -> None:
        xml = (RESEARCH / "sitemap.xml").read_text(encoding="utf-8")
        locs = re.findall(r"<loc>([^<]+)</loc>", xml)
        self.assertEqual(len(locs), 106)
        hub_html = (RESEARCH / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="tp-bounty-crucible"', hub_html)
        self.assertIn('id="tp-symbolic-physics-lab"', hub_html)
        self.assertIn('id="tp-oss-physics-radar"', hub_html)
        self.assertIn("https://github.com/senseiewok/informatico.ai", hub_html)
        self.assertIn("https://github.com/HEPLean/PhysLean", hub_html)
        self.assertIn("https://github.com/MilesCranmer/PySR", hub_html)
        self.assertIn("https://github.com/dynamicslab/pysindy", hub_html)
        self.assertIn("https://github.com/DedalusProject/dedalus", hub_html)
        self.assertIn("https://github.com/itensor/ITensors.jl", hub_html)
        for p in ("physics", "math"):
            p_html = (RESEARCH / p / "index.html").read_text(encoding="utf-8")
            es_p_html = (RESEARCH / "es-mx" / p / "index.html").read_text(encoding="utf-8")
            self.assertIn('id="tp-symbolic-physics-lab"', p_html)
            self.assertIn('id="tp-oss-physics-radar"', p_html)
            self.assertIn('id="tp-symbolic-physics-lab"', es_p_html)
            self.assertIn('id="tp-oss-physics-radar"', es_p_html)

    def test_security_git_zero_secrets_zero_local_paths_and_zero_cf_leakage(self) -> None:
        forbidden = re.compile(r"C:\\Users\\|/home/[a-z0-9_]+|BEGIN .*PRIVATE KEY|sftp-config|cystic fibrosis", re.IGNORECASE)
        for p in ROOT.rglob("*"):
            if not p.is_file() or ".git" in p.parts or "__pycache__" in p.parts or p.suffix in (".jpg", ".png", ".mp3", ".woff2", ".ico", ".pyc", ".webp"):
                continue
            if p.name in ("test_informatico_public.py", ".gitignore"):
                continue
            txt = p.read_text(encoding="utf-8")
            m = forbidden.search(txt)
            self.assertIsNone(m, f"Forbidden pattern {m.group(0) if m else ''} found in {p.relative_to(ROOT)}")


    def test_every_folio_meets_multi_chapter_monograph_depth_contract(self) -> None:
        folio_count = 0
        for pillar in ("math", "physics", "engineering", "architecture"):
            for fdir in sorted((RESEARCH / pillar).iterdir()):
                if not fdir.is_dir():
                    continue
                folio_count += 1
                slug = fdir.name
                for html_file in (fdir / "index.html", RESEARCH / "es-mx" / pillar / slug / "index.html"):
                    txt = html_file.read_text(encoding="utf-8")
                    paras = re.findall(r"<p[^>]*>(.*?)</p>", txt, re.S)
                    words = sum(len(re.sub(r"<[^>]+>", " ", p).split()) for p in paras)
                    self.assertGreaterEqual(words, 2800, f"{html_file} has only {words} visible <p> words (< 2800)")
                    self.assertGreaterEqual(len(paras), 45, f"{html_file} has only {len(paras)} <p> paragraphs (< 45)")
                    self.assertIn('class="tp-proof-spine"', txt, html_file)
                    self.assertEqual(txt.count('class="tp-proof-chapter"'), 4, html_file)
                    self.assertEqual(txt.count('class="tp-proof-stage-block"'), 4, html_file)
                    self.assertIn('class="tp-worked-verification-chapter"', txt, html_file)
                    self.assertIn('tp-telemetry-benchmark-table', txt, html_file)
                    self.assertIn('class="tp-transfer-chapter"', txt, html_file)
                    self.assertGreaterEqual(txt.count("<h3"), 15, html_file)
        self.assertEqual(folio_count, 48)


if __name__ == "__main__":
    unittest.main()
