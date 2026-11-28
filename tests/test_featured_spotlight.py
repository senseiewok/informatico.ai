#!/usr/bin/env python3
"""Regression tests for the cover feature (#tp-featured-edition-desk): "This week's essay" and "Coming next".

Until 2026-11-28 this section was the "Featured Monograph Spotlight & Release Desk" with slot pills and a release
queue. The reader-facing structure is tested in tests/test_magazine_cover.py; this file keeps the rotation's
balance, the cover's section order and the module wiring.
"""
from __future__ import annotations

import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "src"


class _Ids(HTMLParser):
    """Element ids and classes in document order."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.slides: list[tuple[str, bool]] = []
        self.coming: list[tuple[str, bool]] = []
        self.release_items = 0
        self.pills = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        classes = (a.get("class") or "").split()
        if "data-spotlight-slot" in a:
            self.slides.append((a["data-spotlight-slot"], "hidden" in a))
        if "data-coming-slot" in a:
            self.coming.append((a["data-coming-slot"], "hidden" in a))
        if "tp-release-item" in classes:
            self.release_items += 1
        if "data-spotlight-pick" in a or "data-spotlight-step" in a:
            self.pills += 1


def _scan(rel: str) -> _Ids:
    parser = _Ids()
    parser.feed((RES / rel).read_text(encoding="utf-8"))
    parser.close()
    return parser


class FeaturedSpotlightTests(unittest.TestCase):
    def test_en_and_es_cover_render_one_essay_and_three_next(self) -> None:
        for rel in ("index.html", "es-mx/index.html"):
            scan = _scan(rel)
            self.assertIn("tp-featured-edition-desk", scan.ids, rel)
            self.assertEqual([s for s, _ in scan.slides], [str(i) for i in range(9)], rel)
            self.assertEqual([hidden for _, hidden in scan.slides], [False] + [True] * 8, rel)
            self.assertEqual([s for s, hidden in scan.coming if not hidden], ["1", "2", "3"], rel)
            self.assertEqual(scan.release_items, 0, f"{rel}: the release queue is back on the cover")
            self.assertEqual(scan.pills, 0, f"{rel}: slot pills are back on the cover")

    def test_cover_opens_off_physics_and_caps_physics_slides(self) -> None:
        """2026-11-15 homepage rebalance: slot 0 is not physics, physics holds at most 2 of 8 slots, and the cover
        order is pillars first, then series and essays; the physics lab and radar stay on /physics/."""
        sys.path.insert(0, str(ROOT / "tools"))
        import build_longform_folios as B  # noqa: E402

        rot = B.INFORMATICO_SPOTLIGHT_ROTATION
        is_phys = [("physics" in r["disc_en"].lower() or r["href"].startswith(("physics/", "timegravity/"))) for r in rot]
        self.assertFalse(is_phys[0], rot[0]["code"])
        self.assertLessEqual(sum(is_phys), 2)
        self.assertIn("classics/mini-jcw/", [r["href"] for r in rot])
        for rel in ("index.html", "es-mx/index.html"):
            ids = _scan(rel).ids
            order = [ids.index(i) for i in ("tp-featured-edition-desk", "pillar-engineering", "pillar-architecture", "pillar-physics", "pillar-math", "more-heading")]
            self.assertEqual(order, sorted(order), rel)
            # The long series band and the essays-across-scales showcase live on /physics/ and /timegravity/.
            self.assertNotIn("featured-timegravity", ids, rel)
            self.assertNotIn("cross-scale-essays", ids, rel)
        for rel in ("physics/index.html", "es-mx/physics/index.html"):
            ids = _scan(rel).ids
            self.assertLess(ids.index("timegravity-series"), ids.index("cross-scale-essays"), rel)

    def test_spotlight_module_is_wired_without_innerhtml(self) -> None:
        mod_src = (RES / "modules" / "featured-spotlight.mjs").read_text(encoding="utf-8")
        main_src = (RES / "modules" / "main.mjs").read_text(encoding="utf-8")
        self.assertIn("export function initFeaturedSpotlight", mod_src)
        self.assertIn("export function computeWeekSlot", mod_src)
        self.assertNotIn(".innerHTML =", mod_src)
        self.assertNotIn(".innerHTML=", mod_src)
        self.assertIn('import { initFeaturedSpotlight } from "./featured-spotlight.mjs";', main_src)
        self.assertIn("initFeaturedSpotlight(scope);", main_src)


if __name__ == "__main__":
    unittest.main()
