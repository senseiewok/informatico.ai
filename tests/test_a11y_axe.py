#!/usr/bin/env python3
"""Isolated WCAG 2.2 AA accessibility and strict-CSP MathML Core visual gate via Playwright Chromium."""
from __future__ import annotations

import functools
import glob
import http.server
import os
from pathlib import Path
import re
import shutil
import tempfile
import threading
import unittest

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover
    sync_playwright = None

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
HTACCESS_PATH = ROOT / "deploy" / "htaccess.txt"

AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"]
AUDIT_ROUTES = ["", "math/", "math/m01/", "es-mx/math/m01/", "physics/p01/", "about/"]
MATHML_ROUTES = ["math/m01/", "es-mx/math/m01/", "physics/p01/", "physics/p05/"]
VIEWPORTS = [
    ("desktop", {"width": 1440, "height": 900}),
    ("mobile", {"width": 375, "height": 812}),
]


def _load_csp_header() -> str:
    txt = HTACCESS_PATH.read_text(encoding="utf-8")
    m = re.search(r'Header always set Content-Security-Policy "([^"]+)"', txt)
    if not m:
        raise RuntimeError(f"Could not parse Content-Security-Policy from {HTACCESS_PATH}")
    return m.group(1)


def find_chrome() -> str | None:
    if os.environ.get("CHROME_PATH") and Path(os.environ["CHROME_PATH"]).is_file():
        return os.environ["CHROME_PATH"]
    for pattern in (
        Path.home() / "AppData/Local/ms-playwright/chromium-*/chrome-win64/chrome.exe",
        Path.home() / ".cache/ms-playwright/chromium-*/chrome-linux/chrome",
    ):
        found = sorted(glob.glob(str(pattern)), reverse=True)
        if found:
            return found[0]
    return None


def _lab_files_root() -> Path | None:
    here = Path(__file__).resolve()
    for idx in (4, 3, 2, 1):
        if len(here.parents) > idx:
            candidate = here.parents[idx] / ".lab-files"
            if candidate.is_dir():
                return candidate
    return None


def find_axe_js() -> Path | None:
    env_path = os.environ.get("LAB_AXE_JS")
    if env_path:
        p = Path(env_path)
        return p if p.is_file() else None
    lf = _lab_files_root()
    if lf is not None:
        candidate = lf / "tools" / "axe" / "axe.min.js"
        if candidate.is_file():
            return candidate
    return None


class _StaticSiteServer(http.server.ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


class _StrictCspHandler(http.server.SimpleHTTPRequestHandler):
    csp_policy = ""

    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".mjs": "text/javascript",
        ".css": "text/css",
        ".woff2": "font/woff2",
        ".woff": "font/woff",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
        ".avif": "image/avif",
        ".json": "application/json",
        ".glb": "model/gltf-binary",
        ".3mf": "model/3mf",
        ".mp3": "audio/mpeg",
        ".webm": "video/webm",
    }

    def end_headers(self) -> None:
        if self.csp_policy:
            self.send_header("Content-Security-Policy", self.csp_policy)
        super().end_headers()

    def log_message(self, fmt: str, *args: object) -> None:
        return


def serve(directory: Path, csp_policy: str = ""):
    class _BoundHandler(_StrictCspHandler):
        pass

    _BoundHandler.csp_policy = csp_policy
    handler = functools.partial(_BoundHandler, directory=str(directory))
    httpd = _StaticSiteServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}/"


@unittest.skipIf(sync_playwright is None, "Playwright is not installed in this Python")
class InformaticoAxeAndMathMLTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome = find_chrome()
        if not cls.chrome:
            raise unittest.SkipTest("no Chromium found (set CHROME_PATH)")
        cls.axe_js = find_axe_js()
        if not cls.axe_js:
            raise unittest.SkipTest("axe.min.js not found (set LAB_AXE_JS)")

        cls.csp_policy = _load_csp_header()
        cls.httpd, cls.base = serve(SRC, csp_policy=cls.csp_policy)
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=cls.chrome,
            headless=True,
            args=[
                "--use-angle=swiftshader",
                "--enable-unsafe-swiftshader",
                "--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1",
            ],
        )

    @classmethod
    def tearDownClass(cls) -> None:
        if hasattr(cls, "browser") and cls.browser is not None:
            cls.browser.close()
        if hasattr(cls, "pw") and cls.pw is not None:
            cls.pw.stop()
        if hasattr(cls, "httpd") and cls.httpd is not None:
            cls.httpd.shutdown()
            cls.httpd.server_close()

    def _run_axe_on_url(self, url: str, viewport: dict[str, int]) -> list[dict]:
        ctx = self.browser.new_context(bypass_csp=True, viewport=viewport)
        try:
            page = ctx.new_page()
            page.goto(url, wait_until="load")
            page.wait_for_timeout(400)
            page.add_script_tag(path=str(self.axe_js))
            results = page.evaluate(
                """async (tags) => {
                    return await window.axe.run(document, {
                        runOnly: { type: 'tag', values: tags }
                    });
                }""",
                AXE_TAGS,
            )
            return results.get("violations", [])
        finally:
            ctx.close()

    def test_planted_defect_detected(self) -> None:
        """Can-fail check: planted missing img alt and empty button must trigger >= 2 axe violations."""
        tmp_dir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp_dir, True)
        (tmp_dir / "index.html").write_text(
            "<!doctype html>"
            '<html lang="en"><head><meta charset="utf-8"><title>Planted Defect Fixture</title></head>'
            '<body><main><h1>Planted Defect</h1><img src="missing.png"><button></button></main></body></html>',
            encoding="utf-8",
        )
        httpd, base = serve(tmp_dir)
        self.addCleanup(httpd.server_close)
        self.addCleanup(httpd.shutdown)

        violations = self._run_axe_on_url(base, {"width": 1440, "height": 900})
        violation_ids = {v.get("id") for v in violations}
        self.assertGreaterEqual(len(violations), 2, f"Expected >=2 violations on planted defects, got {violations}")
        self.assertIn("image-alt", violation_ids)
        self.assertIn("button-name", violation_ids)

    def test_wcag22_aa_audit_across_routes_and_viewports(self) -> None:
        """Run axe WCAG 2.2 AA across 6 routes at desktop (1440x900) and mobile (375x812); fail on critical."""
        critical_hits: list[dict] = []
        summary_lines: list[str] = ["\n[informatico.ai axe-core WCAG 2.2 AA Summary]"]

        for route in AUDIT_ROUTES:
            route_label = route or "/"
            for vp_name, vp_size in VIEWPORTS:
                violations = self._run_axe_on_url(self.base + route, vp_size)
                if not violations:
                    summary_lines.append(
                        f"  {route_label:<16} {vp_name:<8} ({vp_size['width']}x{vp_size['height']}): 0 violations"
                    )
                    continue
                summary_lines.append(
                    f"  {route_label:<16} {vp_name:<8} ({vp_size['width']}x{vp_size['height']}): {len(violations)} rule(s)"
                )
                for v in violations:
                    impact = v.get("impact") or "unknown"
                    rule_id = v.get("id") or "unknown"
                    nodes_count = len(v.get("nodes", []))
                    summary_lines.append(f"    - impact={impact:<9} id={rule_id:<30} nodes={nodes_count}")
                    if impact == "critical":
                        critical_hits.append(
                            {
                                "route": route_label,
                                "viewport": vp_name,
                                "id": rule_id,
                                "nodes": nodes_count,
                                "help": v.get("help", ""),
                            }
                        )

        print("\n".join(summary_lines), flush=True)
        self.assertEqual(critical_hits, [], f"Critical WCAG 2.2 AA violations detected: {critical_hits}")

    def test_mathml_renders_under_strict_csp(self) -> None:
        """Verify native MathML Core lays out under strict production CSP and save 2x Retina screenshots."""
        lf = _lab_files_root()
        screenshot_dir = lf / "scratch" / "screenshots" / "2026-11-24" / "mathml-m01" if lf else None
        if screenshot_dir is not None:
            screenshot_dir.mkdir(parents=True, exist_ok=True)

        for route in MATHML_ROUTES:
            for vp_name, vp_size in VIEWPORTS:
                ctx = self.browser.new_context(bypass_csp=False, viewport=vp_size, device_scale_factor=2)
                try:
                    page = ctx.new_page()
                    page_errors: list[str] = []
                    csp_console_errors: list[str] = []
                    page.on("pageerror", lambda exc: page_errors.append(str(exc)))
                    page.on(
                        "console",
                        lambda msg: csp_console_errors.append(msg.text)
                        if msg.type == "error"
                        and (
                            "Content Security Policy" in msg.text
                            or "Trusted" in msg.text
                            or "Refused to" in msg.text
                        )
                        else None,
                    )
                    page.goto(self.base + route, wait_until="load")
                    page.wait_for_timeout(300)
                    self.assertEqual(page_errors, [], f"pageerror on {route} ({vp_name}): {page_errors}")
                    self.assertEqual(
                        csp_console_errors,
                        [],
                        f"CSP/TrustedTypes console error on {route} ({vp_name}): {csp_console_errors}",
                    )
                    box = page.evaluate(
                        """() => {
                            const wrap = document.querySelector('.tp-theorem-eq--mathml');
                            const el = wrap ? wrap.querySelector('math') : null;
                            if (!wrap || !el) return null;
                            const r = el.getBoundingClientRect();
                            return {
                                width: r.width,
                                height: r.height,
                                namespace: el.namespaceURI,
                                wrapScrollW: Math.round(wrap.scrollWidth),
                                wrapClientW: Math.round(wrap.clientWidth),
                            };
                        }"""
                    )
                    self.assertIsNotNone(box, f"Missing MathML element on {route}")
                    self.assertGreater(box["height"], 10.0, f"MathML collapsed vertically on {route}: {box}")
                    self.assertGreater(box["width"], 40.0, f"MathML collapsed horizontally on {route}: {box}")
                    self.assertLessEqual(
                        box["wrapScrollW"],
                        box["wrapClientW"] + 2,
                        f"MathML theorem equation clipped horizontally on {route} ({vp_name}): {box}",
                    )
                    self.assertEqual(box["namespace"], "http://www.w3.org/1998/Math/MathML")

                    if route == "math/m01/" and screenshot_dir is not None:
                        theorem_box = page.locator(".tp-theorem-box").first
                        theorem_box.scroll_into_view_if_needed()
                        theorem_box.screenshot(path=str(screenshot_dir / f"m01-theorem-{vp_name}-2x.png"))
                        page.screenshot(path=str(screenshot_dir / f"m01-viewport-{vp_name}-2x.png"))
                finally:
                    ctx.close()


if __name__ == "__main__":
    unittest.main()
