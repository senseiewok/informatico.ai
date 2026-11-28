"""Guard: bounty pages must say plainly that they are not prize entries (grounding review, 2026-11-13)."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(ROOT / "tools"))

# A readout or gate label must never read as a prize organizer's verdict.
PRIZE_VERDICT = re.compile(r"(XPRIZE|Holcim|Cooling Prize|IStructE|Erd\u0151s|AIMO)[^<>\"]{0,40}(Verdict|Veredicto|\bGate\b)")


class BountyBoundaryTests(unittest.TestCase):
    def pages(self) -> list[Path]:
        out = [SRC / "bounties" / "index.html", SRC / "es-mx" / "bounties" / "index.html"]
        for n in range(1, 7):
            out.append(SRC / "bounties" / f"b{n:02d}" / "index.html")
            out.append(SRC / "es-mx" / "bounties" / f"b{n:02d}" / "index.html")
        return out

    def test_every_bounty_page_carries_the_not_a_prize_entry_notice(self) -> None:
        import build_longform_folios as blf

        for page in self.pages():
            html = page.read_text(encoding="utf-8")
            self.assertIn("tp-bounty-boundary", html, page)
            self.assertIn(blf.esc(blf.BOUNTY_BOUNDARY_ES), html, page)
            if "es-mx" not in page.parts:
                self.assertIn(blf.esc(blf.BOUNTY_BOUNDARY_EN), html, page)

    def test_cover_names_no_prize_so_none_can_read_as_entered_or_won(self) -> None:
        """Since the magazine pass of 2026-11-28 the open-problems section lives on /bounties/ (with the notice).
        The cover only links there, and must not name a prize, a sum of money or a verdict."""
        named = re.compile(r"XPRIZE|Holcim|Cooling Prize|IStructE|AIMO|Erd\u0151s Problem|\$\s?\d|\bPASS\b|APROBADO|\bw[oi]n\b|\bgan[oó]\b|award", re.I)
        for rel in ("index.html", "es-mx/index.html"):
            html = (SRC / rel).read_text(encoding="utf-8")
            main = html[html.index("<main"):html.index("</main>")]
            hit = named.search(main)
            self.assertIsNone(hit, f"{rel}: {hit.group(0) if hit else ''}")
            self.assertIn('href="bounties/"', main, rel)
            self.assertNotIn("tp-bounty-crucible", main, rel)

    def test_no_label_reads_as_a_prize_verdict(self) -> None:
        for page in self.pages():
            html = page.read_text(encoding="utf-8")
            hit = PRIZE_VERDICT.search(html)
            self.assertIsNone(hit, f"{page}: {hit.group(0) if hit else ''}")

    def test_b05_matches_verifier_mdl_and_rejects_planted_defect(self) -> None:
        script = ROOT / "bounties" / "bounty_p2_pysr_pysindy_pde_discovery.py"
        normal = subprocess.run(
            [sys.executable, "-X", "utf8", str(script), "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertEqual(normal.returncode, 0, normal.stdout + normal.stderr)
        payload = json.loads(normal.stdout)
        self.assertEqual(payload["verdict"], "PASS")
        self.assertAlmostEqual(payload["pysr_mdl_score"], -1073.4509, places=4)

        defect = subprocess.run(
            [sys.executable, "-X", "utf8", str(script), "--planted-defect", "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        self.assertNotEqual(defect.returncode, 0, defect.stdout + defect.stderr)
        defect_payload = json.loads(defect.stdout)
        self.assertEqual(defect_payload["verdict"], "FAIL")
        self.assertEqual(defect_payload["overfit_case"]["verdict"], "FAIL")
        self.assertEqual(defect_payload["overfit_case"]["active_pde_terms"], ["u*u_x", "u_xx", "u^3"])
        self.assertEqual(defect_payload["underfit_case"]["verdict"], "FAIL")
        self.assertEqual(defect_payload["underfit_case"]["active_pde_terms"], ["u*u_x"])

        for path in (
            SRC / "bounties" / "b05" / "index.html",
            SRC / "es-mx" / "bounties" / "b05" / "index.html",
            ROOT / "skills" / "bounties" / "b05" / "SKILL.md",
            SRC / "modules" / "physics-discovery-crucible.mjs",
        ):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("1360.87", text, path)
            self.assertNotIn("1360.9", text, path)
            if path.suffix != ".mjs":
                self.assertIn("1073.45", text, path)


if __name__ == "__main__":
    unittest.main()
