"""Verification suite for the standalone public Informatico.ai repository."""
from __future__ import annotations

import hashlib
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
        self.assertEqual(len(skill_files), 67)
        self.assertEqual(len(py_files), 67)
        res = subprocess.run([sys.executable, "-X", "utf8", str(SKILLS / "verify_all_48_folios.py")], capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: All 67/67", res.stdout)

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
        self.assertEqual(len(locs), 152)
        self.assertTrue((RESEARCH / "about" / "index.html").is_file())
        self.assertTrue((RESEARCH / "es-mx" / "about" / "index.html").is_file())
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
        self.assertIn('class="tp-cover-track-strip"', hub_html)
        self.assertTrue((RESEARCH / "bounties" / "index.html").is_file())
        self.assertTrue((RESEARCH / "es-mx" / "bounties" / "index.html").is_file())
        for bslug in ("b01", "b02", "b03", "b04", "b05", "b06"):
            self.assertTrue((RESEARCH / "bounties" / bslug / "index.html").is_file())
            self.assertTrue((RESEARCH / "es-mx" / "bounties" / bslug / "index.html").is_file())
        for p in ("physics", "math"):
            p_html = (RESEARCH / p / "index.html").read_text(encoding="utf-8")
            es_p_html = (RESEARCH / "es-mx" / p / "index.html").read_text(encoding="utf-8")
            self.assertIn('id="tp-symbolic-physics-lab"', p_html)
            self.assertIn('id="tp-oss-physics-radar"', p_html)
            self.assertIn('id="tp-symbolic-physics-lab"', es_p_html)
            self.assertIn('id="tp-oss-physics-radar"', es_p_html)

    def test_security_git_zero_secrets_zero_local_paths_and_zero_cf_leakage(self) -> None:
        secret_pat = re.compile(r"C:\\Users\\|/home/[a-z0-9_]+|BEGIN .*PRIVATE KEY|sftp-config", re.IGNORECASE)
        cf_pat = re.compile(r"cystic fibrosis", re.IGNORECASE)
        about_bridge_rel = {
            Path("src/research/about/index.html"),
            Path("src/research/es-mx/about/index.html"),
            Path("src/research/data/about-evidence.json"),
            Path("src/research/modules/trace-sentence.mjs"),
            Path("tools/build_longform_folios.py"),
        }
        for p in ROOT.rglob("*"):
            if not p.is_file() or ".git" in p.parts or "__pycache__" in p.parts or p.suffix in (".jpg", ".png", ".mp3", ".woff2", ".ico", ".pyc", ".webp", ".glb", ".3mf"):
                continue
            if p.name in ("test_informatico_public.py", ".gitignore"):
                continue
            rel = p.relative_to(ROOT)
            txt = p.read_text(encoding="utf-8")
            m_sec = secret_pat.search(txt)
            self.assertIsNone(m_sec, f"Forbidden secret/path pattern {m_sec.group(0) if m_sec else ''} found in {rel}")
            if rel not in about_bridge_rel:
                m_cf = cf_pat.search(txt)
                self.assertIsNone(m_cf, f"Forbidden CF leakage {m_cf.group(0) if m_cf else ''} found in {rel}")


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
                    self.assertGreaterEqual(words, 4200, f"{html_file} has only {words} visible <p> words (< 4200)")
                    self.assertGreaterEqual(len(paras), 52, f"{html_file} has only {len(paras)} <p> paragraphs (< 52)")
                    self.assertIn('class="tp-proof-spine"', txt, html_file)
                    self.assertEqual(txt.count('class="tp-proof-chapter"'), 4, html_file)
                    self.assertEqual(txt.count('class="tp-proof-stage-block"'), 4, html_file)
                    self.assertIn('class="tp-worked-verification-chapter"', txt, html_file)
                    self.assertIn('tp-telemetry-benchmark-table', txt, html_file)
                    self.assertIn('class="tp-transfer-chapter"', txt, html_file)
                    self.assertIn('tp-plain-bridge-box', txt, html_file)
                    self.assertIn('tp-analogy-box', txt, html_file)
                    self.assertIn('tp-distill-figure', txt, html_file)
                    self.assertIn('tp-distill-svg', txt, html_file)
                    self.assertGreaterEqual(txt.count("<h3"), 15, html_file)
        self.assertEqual(folio_count, 48)



    def test_all_61_editorial_plates_have_unique_sha256_hashes_and_cache_busters(self) -> None:
        plates_dir = RESEARCH / "plates"
        expected_slugs = (
            [f"e{i:02d}" for i in range(1, 13)]
            + [f"a{i:02d}" for i in range(1, 13)]
            + [f"p{i:02d}" for i in range(1, 13)]
            + [f"m{i:02d}" for i in range(1, 13)]
            + [f"b{i:02d}" for i in range(1, 7)]
            + [f"x{i:02d}" for i in range(1, 7)]
            + ["utopian-city-future"]
        )
        seen_hashes: dict[str, str] = {}
        for slug in expected_slugs:
            p = plates_dir / f"{slug}.jpg"
            self.assertTrue(p.is_file(), f"Missing plate {slug}.jpg")
            data = p.read_bytes()
            self.assertGreater(len(data), 40_000, f"Plate {slug}.jpg too small")
            h = hashlib.sha256(data).hexdigest()
            self.assertNotIn(h, seen_hashes, f"Duplicate plate {slug}.jpg == {seen_hashes.get(h)}.jpg")
            seen_hashes[h] = slug

        for hub_rel, expected_count in (
            ("index.html", 48),
            ("engineering/index.html", 12),
            ("architecture/index.html", 12),
            ("physics/index.html", 12),
            ("math/index.html", 12),
            ("bounties/index.html", 6),
            ("toolchain/index.html", 6),
        ):
            hub_txt = (RESEARCH / hub_rel).read_text(encoding="utf-8")
            thumbs = re.findall(r'<img class="tp-rack-thumb" src="([^"]+)"', hub_txt)
            self.assertEqual(len(thumbs), expected_count, f"{hub_rel} expected {expected_count} rack thumbs")
            self.assertEqual(len(set(thumbs)), expected_count, f"{hub_rel} has duplicate rack card images")
            for t in thumbs:
                self.assertIn("?v=", t, f"{hub_rel} thumbnail {t} missing ?v= cache-buster")


if __name__ == "__main__":
    unittest.main()
