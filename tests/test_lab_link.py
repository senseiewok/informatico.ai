#!/usr/bin/env python3
"""Regression tests for the optional local-lab masthead link (src/modules/lab-link.mjs).

The link is off by default and can only ever point at the reader's own loopback address.
These tests pin the properties that make that true.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "src"


class LabLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.src = (RES / "modules" / "lab-link.mjs").read_text(encoding="utf-8")
        self.main = (RES / "modules" / "main.mjs").read_text(encoding="utf-8")

    def test_module_is_wired_once_before_the_theme_pass(self) -> None:
        self.assertIn('import { initLabLink } from "./lab-link.mjs";', self.main)
        self.assertEqual(self.main.count("initLabLink();"), 1)
        self.assertLess(self.main.index("initLabLink();"), self.main.index("bootMagazine(document);"))

    def test_the_only_address_is_loopback_with_a_fixed_shape(self) -> None:
        hrefs = re.findall(r"`(http[^`]*)`", self.src)
        self.assertEqual(hrefs, ["http://127.0.0.1:${port}/"])
        self.assertEqual(self.src.count('setAttribute("href"'), 1)
        self.assertIn('link.setAttribute("href", labHref(port));', self.src)
        self.assertNotIn("https://", self.src.split("*/", 1)[1])

    def test_the_port_is_the_only_input_and_is_strictly_numeric(self) -> None:
        self.assertIn("/^[0-9]{4,5}$/", self.src)
        self.assertIn("port >= 1024 && port <= 65535", self.src)
        gets = re.findall(r"params\.get\(([A-Z_]+)\)", self.src)
        self.assertEqual(gets, ["PARAM"], "the query string is read in exactly one place")
        self.assertRegex(self.src, r"const fromQuery = parseLabPort\(raw\);")
        self.assertIn("return parseLabPort(readStored(storage));", self.src, "a stored value is re-validated on every read")

    def test_no_markup_injection_no_network_no_redirect(self) -> None:
        for banned in (".innerHTML", "outerHTML", "insertAdjacentHTML", "document.write", "eval(", "fetch(",
                       "XMLHttpRequest", "sendBeacon", "location.href", "location.assign", "location.replace",
                       "window.open", "import("):
            self.assertNotIn(banned, self.src, banned)
        self.assertIn('link.textContent = isEs ? "Laboratorio" : "Lab";', self.src)

    def test_off_by_default_and_can_be_switched_off(self) -> None:
        self.assertIn('if (raw === "off")', self.src)
        self.assertIn("writeStored(storage, null);", self.src)
        self.assertRegex(self.src, r"if \(port === null\) \{\s+return null;")

    def test_it_cannot_stop_the_page_from_booting(self) -> None:
        self.assertNotIn("storage = window.localStorage", self.src, "reading localStorage can throw; it must be guarded")
        self.assertIn("storage = safeStorage()", self.src)
        self.assertIn("return window.sessionStorage;", self.src)
        self.assertNotIn("localStorage", self.src.replace("storage = window.localStorage", ""), "the port is remembered per tab, never permanently")
        body = self.src[self.src.index("export function initLabLink("):]
        self.assertRegex(body, r"\{\s+try \{")
        self.assertRegex(body, r"\} catch \{\s+return null;\s+\}\s+\}\s*$")

    def test_no_page_ships_the_link_in_its_markup(self) -> None:
        for page in list(RES.glob("*.html")) + list(RES.glob("*/index.html")) + list(RES.glob("es-mx/*/index.html")):
            self.assertNotIn('data-tp-nav="lab"', page.read_text(encoding="utf-8"), page.name)


if __name__ == "__main__":
    unittest.main()
