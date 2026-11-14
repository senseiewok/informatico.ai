#!/usr/bin/env python3
"""The site may only claim a verifier where one exists and can fail.

A skill is `verified` when a hand-written verify_*.py is on disk; otherwise it is plain text and its
page must say its values are stated in the essay. On 2026-11-13, 54 generated scripts that printed
PASS without computing anything were removed. These tests keep that from coming back.
"""
from __future__ import annotations

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
SKILLS = ROOT / "skills"
PILLARS = ("engineering", "architecture", "physics", "math")
# Phrases that assert a script checked something. None may appear on the page of a text skill.
FORBIDDEN = (
    "Verified deterministically",
    "Kernel Verification",
    "PASS · VERIFIED",
    "machine-checked falsification rules",
    "zero drift across all 48",
    "certified by our offline verification kernel",
    "Download Python Tool",
    "Download Python Verifier",
    "data-py-source",
    "Primary Verification Kernel",
)

_spec = importlib.util.spec_from_file_location("verify_all", SKILLS / "verify_all_48_folios.py")
runner = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(runner)


def has_verifier(pillar: str, slug: str) -> bool:
    return any((SKILLS / pillar / slug).glob("verify_*.py"))


def pillar_pages() -> list[tuple[str, str, Path]]:
    out = []
    for pillar in PILLARS:
        for page in sorted((SRC / pillar).glob("*/index.html")):
            slug = page.parent.name
            out.append((pillar, slug, page))
            twin = SRC / "es-mx" / pillar / slug / "index.html"
            if twin.is_file():
                out.append((pillar, slug, twin))
    return out


class VerifierClaimTests(unittest.TestCase):
    def test_every_verifier_on_disk_can_fail(self) -> None:
        scripts = runner.discover()
        self.assertTrue(scripts)
        for path in scripts:
            source = path.read_text(encoding="utf-8")
            self.assertIn("--planted-defect", source, path.name)
            self.assertFalse(runner.reacts_only_to_the_flag(source), f"{path.name}: planted-defect mode only prints or exits")
            self.assertNotRegex(source, r'return \{\s*"status": "PASS",\s*"verdict": "PASS",', f"{path.name}: unconditional PASS")

    def test_the_guard_catches_the_cheapest_fake_and_accepts_a_real_one(self) -> None:
        fake = 'import sys, json\nif "--planted-defect" in sys.argv:\n    sys.exit(1)\nprint(json.dumps({"status": "PASS"}))\n'
        fake2 = ('import sys, json\nplanted = "--planted-defect" in sys.argv\nif planted:\n    print(json.dumps({"status": "FAIL"}))\n'
                 '    raise SystemExit(1)\nprint(json.dumps({"status": "PASS"}))\n')
        real = ('import sys, json\n\ndef area(w, h, planted_defect=False):\n    return w * h + (1 if planted_defect else 0)\n\n'
                'planted = "--planted-defect" in sys.argv\nok = area(3, 4, planted_defect=planted) == 12\n'
                'print(json.dumps({"status": "PASS" if ok else "FAIL"}))\nsys.exit(0 if ok else 1)\n')
        self.assertTrue(runner.reacts_only_to_the_flag(fake))
        self.assertTrue(runner.reacts_only_to_the_flag(fake2))
        self.assertFalse(runner.reacts_only_to_the_flag(real))

    def test_no_pillar_or_bounty_skill_has_a_generated_script(self) -> None:
        for folder in PILLARS + ("bounties",):
            for script in (SKILLS / folder).glob("*/verify_*.py"):
                self.assertIn("--planted-defect", script.read_text(encoding="utf-8"),
                              f"{script.relative_to(ROOT).as_posix()} cannot fail; the generator must never write one")

    def test_text_skill_pages_claim_no_verifier(self) -> None:
        pages = pillar_pages()
        self.assertGreaterEqual(len(pages), 96)
        for pillar, slug, page in pages:
            if has_verifier(pillar, slug):
                continue
            text = page.read_text(encoding="utf-8")
            rel = page.relative_to(SRC).as_posix()
            for phrase in FORBIDDEN:
                self.assertNotIn(phrase, text, f"{rel} still says {phrase!r}")
            self.assertNotRegex(text, rf"skills/{pillar}/{slug}/verify_[a-z0-9_]+\.py", f"{rel} names a script that does not exist")
            self.assertIn("Stated in the essay", text, f"{rel} must say where its reference values come from")

    def test_text_skill_files_say_what_is_not_checked(self) -> None:
        for pillar in PILLARS:
            for skill in sorted((SKILLS / pillar).glob("*/SKILL.md")):
                text = skill.read_text(encoding="utf-8")
                rel = skill.relative_to(ROOT).as_posix()
                self.assertNotIn("Primary Verification Kernel", text, rel)
                self.assertNotIn("Tectonic Identity", text, rel)
                if has_verifier(pillar, skill.parent.name):
                    self.assertIn("## Check it yourself", text, rel)
                else:
                    self.assertIn("## What is and is not checked", text, rel)
                    self.assertIn("No script in this repository recomputes them yet", text, rel)

    def test_repository_docs_link_no_missing_verifier(self) -> None:
        for doc in ("README.md", "bounties/PUBLISHING_PROOF.md", "SECURITY.md", "CONTRIBUTING.md", "AGENTS.md"):
            text = (ROOT / doc).read_text(encoding="utf-8")
            for target in re.findall(r"\]\((skills/[^)\s]+verify_[^)\s]+\.py)\)", text):
                self.assertTrue((ROOT / target).is_file(), f"{doc} links a verifier that does not exist: {target}")
            self.assertNotIn("54/54", text, doc)
            self.assertNotIn("89/89", text, doc)

    def test_home_counts_verifiers_from_disk(self) -> None:
        count = len(runner.discover())
        home = (SRC / "index.html").read_text(encoding="utf-8")
        self.assertIn(f"{count} verifiers across the Toolbox, Time and Gravity and the cross-scale essays", home)
        self.assertNotIn("hands you a live model, Python verifier, and AI SKILL.md", home)


if __name__ == "__main__":
    unittest.main()
