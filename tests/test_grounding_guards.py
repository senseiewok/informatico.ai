"""Grounding guards (2026-11-14): withdrawn references and unearned verdicts stay out; labs match their folios."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(script: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "tools" / script)], capture_output=True,
                          text=True, encoding="utf-8", timeout=900)


class GroundingGuardTests(unittest.TestCase):
    def test_no_withdrawn_reference_or_unearned_verdict(self) -> None:
        res = run("check_grounding_guards.py")
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)

    def test_guard_catches_a_planted_verdict(self) -> None:
        # Failure control: the verdict pattern must reject the strings the 2026-11-14 review removed.
        sys.path.insert(0, str(ROOT / "tools"))
        import check_grounding_guards as g

        for bad in ("QED VERIFIED (29,500 Lemmas)", "ZERO BIOFILM VERIFIED", "0 sorryAx · QED", "FIPS 203 ML-KEM VERIFIED",
                    "6.84 (WKB Verified)", "proven safe", "Certified clean-air loop"):
            self.assertTrue(g.VERDICT.search(bad) and not g.VERDICT_OK.search(bad), bad)
        for ok in ("KERNEL CHECKS PASS (NOT A PROOF)", "Not independently verified", "not tested or certified to any standard"):
            self.assertTrue(g.VERDICT_OK.search(ok), ok)
        self.assertTrue(g.HEADLINE_VERDICT.search("ETH Refutation · 0 sorry"))
        self.assertTrue(g.IDENTIFIER.match("tp-readout-qed"))

    def test_labs_match_their_folios(self) -> None:
        res = run("check_lab_readouts.py")
        if res.returncode == 2:
            self.skipTest(res.stdout.strip())
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)


if __name__ == "__main__":
    unittest.main()
