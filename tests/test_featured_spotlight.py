#!/usr/bin/env python3
"""Regression tests for the Rotating Featured Cover Essay Spotlight & Release Schedule Desk."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "src"


class FeaturedSpotlightTests(unittest.TestCase):
    def test_en_and_es_cover_render_featured_desk_and_release_queue(self) -> None:
        for rel, is_es in (("index.html", False), ("es-mx/index.html", True)):
            page = RES / rel
            self.assertTrue(page.is_file(), f"Missing {rel}")
            html = page.read_text(encoding="utf-8")

            self.assertIn('id="tp-featured-edition-desk"', html, rel)
            slides = re.findall(r'<article class="tp-spotlight-slide" data-spotlight-slot="(\d+)"', html)
            self.assertEqual(slides, ["0", "1", "2", "3", "4", "5", "6", "7"], rel)

            pills = re.findall(r'data-spotlight-pick="(\d+)"', html)
            self.assertEqual(pills, ["0", "1", "2", "3", "4", "5", "6", "7"], rel)

            releases = re.findall(r'<li class="tp-release-item">', html)
            self.assertEqual(len(releases), 3, rel)

            if is_es:
                self.assertIn("Monografía Destacada y Calendario Editorial", html)
                self.assertIn("../plates/t00.png?v=", html)
                self.assertIn("timegravity/", html)
            else:
                self.assertIn("Featured Monograph Spotlight &amp; Release Desk", html)
                self.assertIn("plates/t00.png?v=", html)
                self.assertIn("timegravity/", html)

            # Verify every spotlight href and img src resolves inside src/
            desk_match = re.search(
                r'<section class="tp-featured-edition-desk".*?</section>',
                html,
                re.S,
            )
            self.assertIsNotNone(desk_match, rel)
            desk_html = desk_match.group(0)
            base_dir = page.parent

            for href in re.findall(r'href="([^"]+)"', desk_html):
                self.assertFalse(href.startswith("http"), f"{rel}: unexpected external href {href}")
                clean = href.split("#", 1)[0].split("?", 1)[0]
                target = (base_dir / clean / "index.html") if clean.endswith("/") else (base_dir / clean)
                self.assertTrue(target.resolve().is_file(), f"{rel}: broken spotlight href {href} -> {target}")

            for src in re.findall(r'src="([^"]+)"', desk_html):
                clean_src = src.split("?", 1)[0]
                img_path = (base_dir / clean_src).resolve()
                self.assertTrue(img_path.is_file(), f"{rel}: missing spotlight image {src} -> {img_path}")

    def test_spotlight_module_is_wired_without_innerhtml(self) -> None:
        mod_path = RES / "modules" / "featured-spotlight.mjs"
        main_path = RES / "modules" / "main.mjs"
        self.assertTrue(mod_path.is_file())
        self.assertTrue(main_path.is_file())

        mod_src = mod_path.read_text(encoding="utf-8")
        main_src = main_path.read_text(encoding="utf-8")
        self.assertIn("export function initFeaturedSpotlight", mod_src)
        self.assertIn("export function computeHalfDaySlot", mod_src)
        self.assertIsNone(re.search(r"\.innerHTML\s*=", mod_src))
        self.assertIn('import { initFeaturedSpotlight } from "./featured-spotlight.mjs";', main_src)
        self.assertIn("initFeaturedSpotlight(scope);", main_src)


if __name__ == "__main__":
    unittest.main()
