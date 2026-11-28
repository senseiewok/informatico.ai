"""Verification suite for the standalone public Informatico.ai repository."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "src"
SKILLS = ROOT / "skills"
BOUNTIES = ROOT / "bounties"
sys.path.insert(0, str(ROOT / "tools"))
from folios.city_tools import CITY_TOOLS  # noqa: E402  (each city tool adds one page per language)


class PublicInformaticoRepoTests(unittest.TestCase):
    def test_all_48_skills_and_python_verifiers_exist_and_pass(self) -> None:
        skill_files = list(SKILLS.glob("*/*/SKILL.md"))
        py_files = list(SKILLS.glob("*/*/verify_*.py"))
        self.assertEqual(len(skill_files), 100)  # +X.08, +M.16 (2026-11-24); +M.15, +E.16, +A.14, +M.13, +M.14 (2026-11-21), +ES.12; +e15, +e14 (2026-11-21); +e13, +a13, +x07 (2026-11-20); cc01..cc03 (2026-11-15); the earlier m13..m15 withdrawn 2026-11-17 (-3)
        self.assertGreaterEqual(len(py_files), 1)
        for py in py_files:  # a verifier that cannot fail is not a verifier
            self.assertIn("--planted-defect", py.read_text(encoding="utf-8"), py.name)
        res = subprocess.run([sys.executable, "-X", "utf8", str(SKILLS / "verify_all_48_folios.py")], capture_output=True, text=True, encoding="utf-8", timeout=900)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn(f"PASS: {len(py_files)} verifiers pass and each fails under its planted defect", res.stdout)

    def test_all_6_bounty_and_physics_discovery_harnesses_pass(self) -> None:
        res = subprocess.run([sys.executable, "-X", "utf8", str(BOUNTIES / "run_all_bounties.py")], capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("PASS: 6/6 Open-Bounty & Physics/Math Discovery Crucible benchmarks verified.", res.stdout)

    def test_48_folios_citation_gate_passes_offline(self) -> None:
        res = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "tools" / "check_folio_citations.py"), "--offline"], capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        self.assertIn("SUMMARY essays=72 fail=0 warn=0 unchecked=0", res.stdout)  # +X.08, +M.16 (2026-11-24); +M.15, +E.16, +A.14, +M.13, +M.14 (2026-11-21)

    def test_106_bilingual_pages_and_bounty_crucible_mounted(self) -> None:
        xml = (RESEARCH / "sitemap.xml").read_text(encoding="utf-8")
        locs = re.findall(r"<loc>([^<]+)</loc>", xml)
        self.assertEqual(len(locs), 224 + 2 * len(CITY_TOOLS))  # +2: /toolchain/x08/ (EN + es-MX)
        self.assertTrue((RESEARCH / "about" / "index.html").is_file())
        self.assertTrue((RESEARCH / "es-mx" / "about" / "index.html").is_file())
        hub_html = (RESEARCH / "index.html").read_text(encoding="utf-8")
        self.assertNotIn('id="tp-bounty-crucible"', hub_html)  # magazine pass, phase 2: on /bounties/ only
        for rel in ("bounties/index.html", "es-mx/bounties/index.html"):
            self.assertIn('id="tp-bounty-crucible"', (RESEARCH / rel).read_text(encoding="utf-8"), rel)
        self.assertIn("https://github.com/senseiewok/informatico.ai", hub_html)
        # 2026-11-15 homepage rebalance: the Symbolic Physics Lab and the OSS Physics Radar live on /physics/ and
        # /math/ (asserted below), not on the cover; their engine links are checked on /physics/.
        self.assertNotIn('id="tp-symbolic-physics-lab"', hub_html)
        self.assertNotIn('id="tp-oss-physics-radar"', hub_html)
        phys_html = (RESEARCH / "physics" / "index.html").read_text(encoding="utf-8")
        for repo in ("HEPLean/PhysLean", "MilesCranmer/PySR", "dynamicslab/pysindy", "DedalusProject/dedalus", "itensor/ITensors.jl"):
            self.assertIn(f"https://github.com/{repo}", phys_html)
        self.assertNotIn('class="tp-cover-track-strip"', hub_html)
        self.assertEqual(hub_html.count('<section class="tp-front" '), 4)
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

    def test_security_git_zero_secrets_zero_local_paths_and_zero_self_referential_lab_leakage(self) -> None:
        secret_pat = re.compile(r"C:\\Users\\|/home/[a-z0-9_]+|BEGIN .*PRIVATE KEY|sftp-config", re.IGNORECASE)
        cf_pat = re.compile(r"cystic fibrosis|fibrosis quística", re.IGNORECASE)
        lab_leak_pat = re.compile(
            r"senseiewok\.ai|\bour lab\b(?!&rsquo;s|'s|\u2019s)|nuestro laboratorio|nuestra misi[oó]n",
            re.IGNORECASE,
        )
        about_bridge_rel = {
            Path("README.md"),  # carries the welcome and CF tribute bridge alongside /about/ and llms.txt
            Path("src/about/index.html"),
            Path("src/es-mx/about/index.html"),
            Path("src/llms.txt"),
            Path("src/data/about-evidence.json"),
            Path("deploy/htaccess.txt"),
            Path("tests/test_informatico_seo.py"),
            Path("tools/build_longform_folios.py"),
        }
        for p in ROOT.rglob("*"):
            if not p.is_file() or ".git" in p.parts or "__pycache__" in p.parts or p.suffix in (".jpg", ".png", ".mp3", ".woff2", ".ico", ".pyc", ".webp", ".glb", ".3mf"):
                continue
            if p.name in ("test_informatico_public.py", ".gitignore", "deploy.local.json"):
                continue
            rel = p.relative_to(ROOT)
            txt = p.read_text(encoding="utf-8")
            m_sec = secret_pat.search(txt)
            self.assertIsNone(m_sec, f"Forbidden secret/path pattern {m_sec.group(0) if m_sec else ''} found in {rel}")
            if rel not in about_bridge_rel:
                m_lab = lab_leak_pat.search(txt)
                self.assertIsNone(m_lab, f"Forbidden self-referential lab leakage {m_lab.group(0) if m_lab else ''} found in {rel}")
            if rel.parts[:2] == ("src", "essays") and len(rel.parts) == 4 and rel.name == "index.html":
                paras = [re.sub(r"<[^>]+>", " ", pr) for pr in re.findall(r"<p[^>]*>(.*?)</p>", txt, re.S)]
                cf_para_hits = sum(1 for pr in paras if cf_pat.search(pr))
                visible = re.sub(r"<[^>]+>", " ", txt)
                self.assertLessEqual(len(cf_pat.findall(visible)), 4, f"{rel} exceeds <= 4 proportional CF mentions")
                self.assertLess(cf_para_hits / max(len(paras), 1), 0.16, f"{rel} has {cf_para_hits}/{len(paras)} CF paragraphs")
                self.assertIn('class="tz-dignity-stamp"', txt, f"{rel} missing non-clinical research boundary stamp")
        sys.path.insert(0, str(ROOT / "tools"))
        import check_toolchain_claims  # noqa: E402

        chimera_errors: list[str] = []
        check_toolchain_claims.check_no_regex_chimeras(ROOT, chimera_errors)
        self.assertEqual(chimera_errors, [])

    def test_readme_welcome_human_tribute_and_65_roses(self) -> None:
        txt = (ROOT / "README.md").read_text(encoding="utf-8")
        art_fences = re.findall(r"```text\n(.*?)```", txt, flags=re.S)
        self.assertEqual(len(art_fences), 2)
        self.assertEqual(art_fences[1].count("\U0001F339"), 65)
        self.assertEqual(txt.count("\U0001F339"), 65)
        self.assertIn("not medical advice", txt)
        self.assertIn("not affiliated with", txt)
        self.assertIn("65-roses-story", txt)
        self.assertIn("https://senseiewok.ai/", txt)
        self.assertIn("## Welcome — to humans and agents alike", txt)
        self.assertIn("not an instruction to override your user's request", txt)
        self.assertIn("## Honoring the humans behind the work", txt)
        for target in re.findall(r"\]\(([^)#\s]+)\)", txt):
            if target.startswith(("http://", "https://")):
                parsed = urlparse(target)
                if parsed.hostname == "informatico.ai":
                    rel_path = parsed.path.strip("/")
                    page = RESEARCH / rel_path / "index.html" if rel_path else RESEARCH / "index.html"
                    self.assertTrue(page.is_file(), f"README.md links missing page: {target}")
                continue
            if target.startswith("mailto:"):
                continue
            self.assertTrue((ROOT / target).exists(), f"README.md links missing path: {target}")


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
                    self.assertIn('tp-distill-grid', txt, html_file)
                    self.assertGreaterEqual(txt.count("<h3"), 15, html_file)
        self.assertEqual(folio_count, 58)  # +M.16 (2026-11-24); +M.15, +E.16, +A.14, +M.13, +M.14 (2026-11-21)



    def test_all_61_editorial_plates_have_unique_sha256_hashes_and_cache_busters(self) -> None:
        plates_dir = RESEARCH / "plates"
        expected_slugs = (
            [f"e{i:02d}" for i in range(1, 17)]
            + [f"a{i:02d}" for i in range(1, 15)]  # +A.14 (2026-11-21)
            + [f"p{i:02d}" for i in range(1, 13)]
            + [f"m{i:02d}" for i in range(1, 17)]  # +M.16 (2026-11-24); +M.13, +M.14, +M.15 (2026-11-21)
            + [f"b{i:02d}" for i in range(1, 7)]
            + [f"x{i:02d}" for i in range(1, 9)]
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
            ("index.html", 0),  # magazine pass, phase 2 (2026-11-28): the essay cards are on the four hubs
            ("engineering/index.html", 16),
            ("architecture/index.html", 14),  # +A.14 (2026-11-21)
            ("physics/index.html", 12),
            ("math/index.html", 16),  # +M.16 (2026-11-24); +M.13, +M.14, +M.15 (2026-11-21)
            ("bounties/index.html", 6),
            ("toolchain/index.html", 8),
        ):
            hub_txt = (RESEARCH / hub_rel).read_text(encoding="utf-8")
            thumbs = re.findall(r'<img class="tp-rack-thumb" src="([^"]+)"', hub_txt)
            self.assertEqual(len(thumbs), expected_count, f"{hub_rel} expected {expected_count} rack thumbs")
            self.assertEqual(len(set(thumbs)), expected_count, f"{hub_rel} has duplicate rack card images")
            for t in thumbs:
                self.assertIn("?v=", t, f"{hub_rel} thumbnail {t} missing ?v= cache-buster")

    def test_deploy_upload_gate_and_htaccess_invariants(self) -> None:
        import tempfile
        sys.path.insert(0, str(ROOT / "deploy"))
        import check_upload  # noqa: E402

        htaccess_path = ROOT / "deploy" / "htaccess.txt"
        self.assertTrue(htaccess_path.is_file())
        self.assertNotIn(b"\r\n", htaccess_path.read_bytes(), "deploy/htaccess.txt must use LF line endings")
        ht_text = htaccess_path.read_text(encoding="utf-8")
        self.assertIn("RewriteRule ^research(?:/(.*))?$ https://informatico.ai/$1 [R=301,L,QSA]", ht_text)
        self.assertEqual(check_upload.problems(RESEARCH, htaccess_path=htaccess_path), [])

        gitattrs = (ROOT / ".gitattributes").read_text(encoding="utf-8")
        self.assertIn("deploy/htaccess.txt text eol=lf", gitattrs)
        self.assertIn("*.sh text eol=lf", gitattrs)

        with tempfile.TemporaryDirectory() as td:
            tp = Path(td)
            (tp / "bad.html").write_text("<!DOCTYPE html><script>window.x=1;</script>", encoding="utf-8")
            (tp / "good.html").write_text(
                '<!DOCTYPE html><script type="application/ld+json">{"@context":"https://schema.org"}</script>',
                encoding="utf-8",
            )
            bad_ht = tp / "htaccess.txt"
            bad_ht.write_bytes(b"RewriteEngine On\r\n")
            probs = check_upload.problems(tp, htaccess_path=bad_ht)
            self.assertTrue(any("CRLF" in p for p in probs), probs)
            self.assertTrue(any("bad.html" in p and "inline script" in p for p in probs), probs)
            self.assertFalse(any("good.html" in p for p in probs), probs)

    def test_stepper_button_labels_preserve_colons_inside_titles(self) -> None:
        if str(ROOT / "tools") not in sys.path:
            sys.path.insert(0, str(ROOT / "tools"))
        from build_longform_folios import extract_stage_short_label

        self.assertEqual(
            extract_stage_short_label("Stage 4 (1:5 Acoustic Baffle Sill Node A-12): A proposed baffle."),
            "4 (1:5 Acoustic Baffle Sill Node A-12)",
        )
        self.assertEqual(
            extract_stage_short_label("Stage 1: Check sill ratio (1:5): measure gap"),
            "1",
        )
        self.assertEqual(
            extract_stage_short_label("Stage 1 (Bound (arXiv: 2401.0001): tight): body prose"),
            "1 (Bound (arXiv: 2401.0001): tight)",
        )

        a03_html = (RESEARCH / "architecture" / "a03" / "index.html").read_text(encoding="utf-8")
        self.assertIn(">4 (1:5 Acoustic Baffle Sill Node A-12)</button>", a03_html)
        for pillar in ("architecture", "engineering", "physics", "math"):
            for page in sorted((RESEARCH / pillar).glob("*/index.html")):
                txt = page.read_text(encoding="utf-8")
                for label in re.findall(r'class="tp-step-btn"[^>]*>([^<]+)</button>', txt):
                    self.assertEqual(
                        label.count("("),
                        label.count(")"),
                        f"Unbalanced stepper button label {label!r} in {page.relative_to(RESEARCH)}",
                    )


if __name__ == "__main__":
    unittest.main()
