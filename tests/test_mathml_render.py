#!/usr/bin/env python3
"""Unit tests for build-time MathML Core cache, HTMLParser sanitizer, and static folio integration."""
from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
SRC = ROOT / "src"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import build_longform_folios as builder  # noqa: E402
from folios import mathml_render  # noqa: E402

PILOT_PAGES = [
    ("math", "m01"),
    ("math", "m02"),
    ("physics", "p01"),
    ("physics", "p05"),
]


class MathMLRenderTests(unittest.TestCase):
    def test_cache_matches_all_folios(self) -> None:
        errors = mathml_render.check_cache()
        self.assertEqual(errors, [], f"MathML cache check failed: {errors}")
        folios = mathml_render.discover_mathml_folios()
        for _, slug in PILOT_PAGES:
            self.assertIn(slug, folios)

    def test_rendered_pages_contain_clean_mathml_and_zero_inline_styles(self) -> None:
        for pillar, slug in PILOT_PAGES:
            for lang_prefix in (SRC, SRC / "es-mx"):
                page_path = lang_prefix / pillar / slug / "index.html"
                self.assertTrue(page_path.is_file(), f"Missing built folio page {page_path}")
                raw = page_path.read_text(encoding="utf-8")
                self.assertIn('<p class="tp-theorem-eq tp-theorem-eq--mathml"><math display="block">', raw, str(page_path))
                self.assertIn("</math></p>", raw, str(page_path))
                self.assertNotIn('style="', raw, f"Unexpected inline style in {page_path}")
                self.assertEqual(
                    builder.to_spanish_static(raw, swap=False, shift=False),
                    raw,
                    f"to_spanish_static round-trip failed for {page_path}",
                )

    def test_planted_hostile_input_sanitized(self) -> None:
        hostile = (
            '<math xmlns="http://www.w3.org/1998/Math/MathML" display="block" style="color:red" onclick="evil()">'
            "<script>alert(1)</script>"
            "<style>.x{color:red}</style>"
            '<iframe src="https://example.com"></iframe>'
            '<mrow style="background:url(x)" onclick="evil()" href="javascript:alert(1)">'
            '<mi mathvariant="normal">x</mi><mo>=</mo><mn>1</mn>'
            '<mspace width="0.167em" />'
            '<img src="x" onerror="alert(1)">'
            '<annotation encoding="application/x-tex"></bogus>raw<p>unclosed</annotation>'
            "<textarea><mi>hidden</mi></textarea>"
            "</mrow></math>"
            "<math display=\"inline\"><mi>second</mi></math>"
        )
        cleaned = mathml_render.sanitize_mathml_core(hostile)
        self.assertTrue(cleaned.startswith('<math display="block">'))
        self.assertTrue(cleaned.endswith("</math>"))
        self.assertIn('<mspace width="0.167em"></mspace>', cleaned)
        for forbidden in (
            "<script",
            "<style",
            "<iframe",
            "<img",
            "<textarea",
            "alert(",
            "evil(",
            "style=",
            "onclick",
            "onerror",
            "javascript:",
            "<annotation",
            "hidden",
            "second",
            "xmlns=",
        ):
            self.assertNotIn(forbidden, cleaned.lower(), f"Forbidden token {forbidden!r} survived sanitizer: {cleaned}")

        # Literal text containing "style=" inside mtext must still round-trip cleanly without attribute injection
        literal = mathml_render.sanitize_mathml_core("<math><mtext>style=notation</mtext></math>")
        self.assertEqual(literal, '<math display="block"><mtext>style=notation</mtext></math>')

    def test_planted_stale_hash_rejected(self) -> None:
        with self.assertRaises(ValueError):
            mathml_render.get_cached_mathml("m01", r"x + y = z")


if __name__ == "__main__":
    unittest.main()
