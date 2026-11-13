"""Guard: bounty pages must say plainly that they are not prize entries (grounding review, 2026-11-13)."""
from __future__ import annotations

import re
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
        out = [SRC / "bounties" / "index.html", SRC / "es-mx" / "bounties" / "index.html", SRC / "index.html"]
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

    def test_no_label_reads_as_a_prize_verdict(self) -> None:
        for page in self.pages():
            html = page.read_text(encoding="utf-8")
            hit = PRIZE_VERDICT.search(html)
            self.assertIsNone(hit, f"{page}: {hit.group(0) if hit else ''}")


if __name__ == "__main__":
    unittest.main()
