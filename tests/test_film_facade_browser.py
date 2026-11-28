#!/usr/bin/env python3
"""Browser check of the click-to-play films on the cover and on /about/ (src/modules/film-facade.mjs), in Chromium.

The site is served from 127.0.0.1 with the Content-Security-Policy, Permissions-Policy and Referrer-Policy
read from deploy/htaccess.txt, so the policies the live site sends are the policies under test. Every request
to another host is recorded and aborted.

- before the press: no request leaves 127.0.0.1, no frame exists, the play button is shown with its name;
- the deployed Permissions-Policy delegates autoplay to the player host and to no other;
- after the press: exactly one frame, with the exact src, allow and referrerpolicy, holding focus, and the
  only outside request is that frame's document on the one player host, carrying the site origin as its
  Referer and nothing more; no CSP or Trusted Types error;
- a bad video ID never shows the button and never builds a frame; an ID that goes bad before the press
  hides the button again and moves focus to the plain link;
- without scripts, on all four pages, the poster and the plain link remain.

Skipped when Playwright or Chromium is not installed. Set FILM_FACADE_SHOTS to a folder to save screenshots.
"""
from __future__ import annotations

import functools
import json
import os
import re
import threading
import unittest
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover
    sync_playwright = None

from tests.test_a11y_axe import _StaticSiteServer, _StrictCspHandler, _load_csp_header, find_chrome

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
HTACCESS = ROOT / "deploy" / "htaccess.txt"
PLAYER_ORIGIN = "https://www.youtube-nocookie.com"
_HEADER_LINE = r'^\s*Header always set {name} "((?:[^"\\]|\\.)*)"\s*$'


def _deployed_header(name: str) -> str:
    """The value deploy/htaccess.txt sets for a header; Apache's backslash-quote is read back as a plain quote."""
    found = re.findall(_HEADER_LINE.replace("{name}", re.escape(name)), HTACCESS.read_text(encoding="utf-8"), re.M)
    if len(found) != 1:
        raise RuntimeError(f"{name}: expected one 'Header always set' line in {HTACCESS}, found {len(found)}")
    return found[0].replace('\\"', '"')


def serve_with_headers(directory: Path, headers: dict[str, str]):
    """Serve a folder on 127.0.0.1 with the given response headers on every response."""

    class _Handler(_StrictCspHandler):
        def end_headers(self) -> None:
            for name, value in headers.items():
                self.send_header(name, value)
            super().end_headers()

    httpd = _StaticSiteServer(("127.0.0.1", 0), functools.partial(_Handler, directory=str(directory)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}/"


FILMS = json.loads((ROOT / "data" / "films.json").read_text(encoding="utf-8"))
INTRO = next(f for f in FILMS if f["slug"] == "informatico-intro")
TRAILER = next(f for f in FILMS if f["slug"] == "cf-lab-trailer")
PLAYER_HOST = "www.youtube-nocookie.com"
VIEWPORTS = (("desktop", {"width": 1440, "height": 900}), ("mobile", {"width": 375, "height": 812}))
PRIVACY_EN = "This film plays from YouTube. Nothing from YouTube loads until you press play; then YouTube can see you came from this site."
PRIVACY_ES = "Este video se reproduce desde YouTube. No se carga nada de YouTube hasta que oprimas reproducir; entonces YouTube puede ver que llegaste desde este sitio."
# Every page that carries a player: (page, lang, route, button name, frame title, privacy line, film row).
PAGES = (
    ("cover", "en", "", "Play film: Informatico intro, 45 seconds, from YouTube", "Informatico: intro (YouTube video player)", PRIVACY_EN, INTRO),
    ("cover", "es", "es-mx/", "Reproducir video: Informatico, introducción, 45 segundos, desde YouTube",
     "Informatico: introducción (reproductor de video de YouTube)", PRIVACY_ES, INTRO),
    ("about", "en", "about/", "Play film: Sensei Ewok's CF Lab, 30 seconds, from YouTube",
     "Sensei Ewok's CF Lab: a 30-second trip to the CFTR gene", PRIVACY_EN, TRAILER),
    ("about", "es", "es-mx/about/", "Reproducir video: Sensei Ewok's CF Lab, 30 segundos, desde YouTube",
     "Sensei Ewok's CF Lab: un viaje de 30 segundos al gen CFTR", PRIVACY_ES, TRAILER),
)
POLICY_ERROR_RE = re.compile(r"content security policy|trusted ?types|refused to|permissions policy", re.I)


@unittest.skipIf(sync_playwright is None, "Playwright is not installed in this Python")
@unittest.skipIf(INTRO["youtube_id"] is None or TRAILER["youtube_id"] is None, "a click-to-play film is dormant")
class FilmFacadeBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome = find_chrome()
        if not cls.chrome:
            raise unittest.SkipTest("no Chromium found (set CHROME_PATH)")
        cls.csp = _load_csp_header()
        cls.headers = {
            "Content-Security-Policy": cls.csp,
            "Permissions-Policy": _deployed_header("Permissions-Policy"),
            "Referrer-Policy": _deployed_header("Referrer-Policy"),
        }
        cls.httpd, cls.base = serve_with_headers(SRC, cls.headers)
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=cls.chrome,
            headless=True,
            args=["--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1"],
        )
        shots = os.environ.get("FILM_FACADE_SHOTS")
        cls.shots = Path(shots) if shots else None
        if cls.shots:
            cls.shots.mkdir(parents=True, exist_ok=True)

    @classmethod
    def tearDownClass(cls) -> None:
        for name, closer in (("browser", "close"), ("pw", "stop")):
            obj = getattr(cls, name, None)
            if obj is not None:
                getattr(obj, closer)()
        httpd = getattr(cls, "httpd", None)
        if httpd is not None:
            httpd.shutdown()
            httpd.server_close()

    def _open(self, route: str, viewport: dict[str, int]):
        """A page with every outside request recorded and aborted, and console errors collected."""
        ctx = self.browser.new_context(viewport=viewport)
        outside: list[str] = []
        errors: list[str] = []
        self.referers: dict[str, str | None] = {}

        def handle(r) -> None:
            if r.request.url.startswith(self.base):
                r.continue_()
            else:
                outside.append(r.request.url)
                self.referers[r.request.url] = r.request.headers.get("referer")
                r.abort()

        ctx.route("**/*", handle)
        page = ctx.new_page()
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(self.base + route, wait_until="load")
        page.wait_for_selector(".tp-film-play:not([hidden])", timeout=5000)
        page.wait_for_timeout(300)
        return ctx, page, outside, errors

    def _shot(self, page, name: str) -> None:
        if self.shots:
            page.screenshot(path=str(self.shots / f"{name}.jpg"), type="jpeg", quality=62)

    def test_headers_under_test_are_the_deployed_ones(self) -> None:
        self.assertEqual(self.headers["Referrer-Policy"], "no-referrer")
        self.assertIn('autoplay=(self "https://www.youtube-nocookie.com")', self.headers["Permissions-Policy"])
        with urllib.request.urlopen(self.base) as resp:  # the test server really sends them
            for name, value in self.headers.items():
                self.assertEqual(resp.headers.get_all(name), [value], name)
        self.assertIn("frame-src https://www.youtube-nocookie.com;", self.csp)
        self.assertIn("require-trusted-types-for 'script'; trusted-types 'none'", self.csp)
        self.assertIn("style-src-attr 'none'", self.csp)

    def test_nothing_from_youtube_before_the_press_then_one_exact_focused_frame(self) -> None:
        for vp_name, viewport in VIEWPORTS:
            for page_name, lang, route, name, title, privacy, film in PAGES:
                want_src = f"https://www.youtube-nocookie.com/embed/{film['youtube_id']}?autoplay=1&rel=0&playsinline=1"
                with self.subTest(page=page_name, viewport=vp_name, lang=lang):
                    ctx, page, outside, errors = self._open(route, viewport)
                    try:
                        # Before the press.
                        self.assertEqual(outside, [], "a request left 127.0.0.1 before the press")
                        self.assertEqual(page.locator("iframe").count(), 0)
                        self.assertEqual(page.locator("link[rel~=preconnect], link[rel~=dns-prefetch]").count(), 0)
                        # The deployed Permissions-Policy lets this site and the one player host autoplay, nobody else.
                        policy = page.evaluate(
                            """(host) => {
                                const fp = document.permissionsPolicy || document.featurePolicy;
                                return fp ? {
                                    player: fp.allowsFeature('autoplay', host),
                                    self: fp.allowsFeature('autoplay'),
                                    other: fp.allowsFeature('autoplay', 'https://www.youtube.com'),
                                    camera: fp.allowsFeature('camera'),
                                } : null;
                            }""",
                            PLAYER_ORIGIN,
                        )
                        self.assertIsNotNone(policy, "this Chromium exposes no permissions policy object")
                        self.assertTrue(policy["player"], "autoplay is delegated to the player host")
                        self.assertTrue(policy["self"])
                        self.assertFalse(policy["other"], "autoplay is not delegated to any other host")
                        self.assertFalse(policy["camera"])
                        button = page.get_by_role("button", name=name, exact=True)
                        self.assertEqual(button.count(), 1)
                        self.assertEqual(page.locator(".tp-film-play").count(), 1)
                        before = page.evaluate(
                            """() => {
                                const b = document.querySelector('.tp-film-play');
                                const f = document.querySelector('.tp-film-facade').getBoundingClientRect();
                                const p = document.getElementById(b.getAttribute('aria-describedby'));
                                const img = document.querySelector('.tp-film-facade img');
                                return {
                                    tag: b.tagName, type: b.getAttribute('type'), describedby: p.textContent,
                                    privacyShown: !p.hidden && p.getBoundingClientRect().height > 0,
                                    top: f.top, bottom: f.bottom, width: f.width, height: f.height,
                                    vh: innerHeight, vw: innerWidth, scrollW: document.documentElement.scrollWidth,
                                    posterOk: img.complete && img.naturalWidth === 640, alt: img.getAttribute('alt'),
                                    glyphHidden: b.querySelector('.tp-film-play-glyph').getAttribute('aria-hidden'),
                                    bw: b.getBoundingClientRect().width, bh: b.getBoundingClientRect().height,
                                };
                            }"""
                        )
                        self.assertEqual((before["tag"], before["type"]), ("BUTTON", "button"))
                        self.assertEqual(before["describedby"], privacy)
                        self.assertTrue(before["privacyShown"], "the privacy line is visible once the button is")
                        self.assertTrue(before["posterOk"], "poster loaded from this site")
                        self.assertEqual(before["alt"], "")
                        self.assertEqual(before["glyphHidden"], "true")
                        # Above the fold, inside the viewport, and the page does not scroll sideways.
                        self.assertGreaterEqual(before["top"], 0)
                        self.assertLessEqual(before["bottom"], before["vh"], "the player is above the fold")
                        self.assertLessEqual(before["scrollW"], before["vw"])
                        self.assertGreaterEqual(before["width"], 300)
                        self.assertAlmostEqual(before["width"] / before["height"], 16 / 9, delta=0.03)
                        self.assertAlmostEqual(before["bw"], before["width"], delta=3)
                        self.assertAlmostEqual(before["bh"], before["height"], delta=3)
                        self._shot(page, f"{page_name}-{vp_name}-{lang}-1-before")

                        # The press, from the keyboard path: focus, then Enter.
                        button.focus()
                        page.keyboard.press("Enter")
                        page.wait_for_selector("iframe.tp-film-frame", state="attached", timeout=5000)
                        page.wait_for_timeout(500)
                        after = page.evaluate(
                            """() => {
                                const frames = [...document.querySelectorAll('iframe')];
                                const f = frames[0];
                                const r = f.getBoundingClientRect();
                                const box = f.parentElement.getBoundingClientRect();
                                return {
                                    count: frames.length,
                                    attrs: Object.fromEntries([...f.attributes].map((a) => [a.name, a.value])),
                                    focused: document.activeElement === f,
                                    buttons: document.querySelectorAll('.tp-film-play').length,
                                    inFacade: f.parentElement.classList.contains('tp-film-facade'),
                                    w: r.width, h: r.height, bw: box.width, bh: box.height,
                                    inlineStyles: document.querySelectorAll('.tp-cover-film [style]').length,
                                };
                            }"""
                        )
                        self.assertEqual(after["count"], 1)
                        self.assertEqual(
                            after["attrs"],
                            {
                                "class": "tp-film-frame",
                                "src": want_src,
                                "title": title,
                                "allow": "autoplay; fullscreen",
                                "referrerpolicy": "strict-origin-when-cross-origin",
                                "width": "640",
                                "height": "360",
                                "tabindex": "0",
                            },
                        )
                        self.assertTrue(after["focused"], "focus moves to the player frame")
                        self.assertEqual(after["buttons"], 0, "the frame replaced the button")
                        self.assertTrue(after["inFacade"])
                        self.assertEqual(after["inlineStyles"], 0)
                        # Sized by the class: the frame fills the 16:9 box (inside its 1px border).
                        self.assertAlmostEqual(after["w"], after["bw"], delta=3)
                        self.assertAlmostEqual(after["h"], after["bh"], delta=3)
                        # The only request that ever left 127.0.0.1 is the frame's own document.
                        self.assertEqual(outside, [want_src])
                        # The page is served no-referrer; the frame's own referrerpolicy sends the site origin and
                        # nothing more (no path), which the YouTube player needs.
                        self.assertEqual(self.referers, {want_src: self.base})
                        self.assertEqual({urlsplit(u).hostname for u in outside}, {PLAYER_HOST})
                        policy_errors = [e for e in errors if POLICY_ERROR_RE.search(e)]
                        self.assertEqual(policy_errors, [], "CSP or Trusted Types violation")
                        self._shot(page, f"{page_name}-{vp_name}-{lang}-2-after-press-frame-aborted")
                    finally:
                        ctx.close()

    def test_bad_ids_are_rejected_in_the_browser(self) -> None:
        for route, film in (("", INTRO), ("about/", TRAILER)):
            with self.subTest(route=route):
                self._bad_ids_on(route, film)

    def _bad_ids_on(self, route: str, film: dict) -> None:
        ctx, page, outside, errors = self._open(route, VIEWPORTS[0][1])
        try:
            result = page.evaluate(
                """async () => {
                    const m = await import('/modules/film-facade.mjs');
                    const bad = ['', 'abc', 'AbC_dEf-1234', 'AbC dEf-123', 'AbC_dEf-123\\n', 'AbC"dEf-123', '../../../../x',
                                 'https://evil.example/', 'AbC_dEf-12\\u0661', null, undefined, 12345678901, ['AbC_dEf-123']];
                    const out = { accepted: [], frames: [], good: m.filmEmbedSrc('AbC_dEf-123') };
                    for (const id of bad) {
                        if (m.isFilmId(id) || m.filmEmbedSrc(id) !== null) out.accepted.push(String(id));
                        if (m.createFilmFrame(document, id, 't') !== null) out.frames.push(String(id));
                    }
                    // A facade whose ID was tampered with after load: the click builds nothing.
                    const facade = document.querySelector('.tp-film-facade');
                    facade.setAttribute('data-yt', 'x" onload="alert(1)');
                    document.querySelector('.tp-film-play').click();
                    out.framesAfterTamperedClick = document.querySelectorAll('iframe').length;
                    // No dead control: button and privacy line hidden again, focus on the plain link.
                    out.buttonHiddenAgain = document.querySelector('.tp-film-play').hasAttribute('hidden');
                    out.privacyHiddenAgain = document.querySelector('.tp-film-privacy').hasAttribute('hidden');
                    out.focusOnPlainLink = document.activeElement === document.querySelector('a.tp-film-out');
                    out.plainLinkHref = document.querySelector('a.tp-film-out').getAttribute('href');
                    // A fresh facade with a bad ID: init leaves its button hidden and wires nothing.
                    const fresh = document.createElement('div');
                    fresh.setAttribute('class', 'tp-film-facade');
                    fresh.setAttribute('data-yt', 'not-an-id');
                    const b = document.createElement('button');
                    b.setAttribute('class', 'tp-film-play');
                    b.setAttribute('hidden', '');
                    fresh.append(b);
                    document.body.append(fresh);
                    out.wired = m.initFilmFacade(document);
                    out.freshHidden = b.hasAttribute('hidden');
                    b.click();
                    out.framesAtEnd = document.querySelectorAll('iframe').length;
                    return out;
                }"""
            )
            self.assertEqual(result["good"], "https://www.youtube-nocookie.com/embed/AbC_dEf-123?autoplay=1&rel=0&playsinline=1")
            self.assertEqual(result["accepted"], [])
            self.assertEqual(result["frames"], [])
            self.assertEqual(result["framesAfterTamperedClick"], 0)
            self.assertTrue(result["buttonHiddenAgain"])
            self.assertTrue(result["privacyHiddenAgain"])
            self.assertTrue(result["focusOnPlainLink"])
            self.assertEqual(result["plainLinkHref"], f"https://www.youtube.com/watch?v={film['youtube_id']}")
            self.assertEqual(result["wired"], 0)
            self.assertTrue(result["freshHidden"])
            self.assertEqual(result["framesAtEnd"], 0)
            self.assertEqual(outside, [])
        finally:
            ctx.close()

    def test_without_scripts_the_poster_and_plain_link_remain(self) -> None:
        ctx = self.browser.new_context(java_script_enabled=False, viewport=VIEWPORTS[0][1])
        outside: list[str] = []
        try:
            ctx.route("**/*", lambda r: r.continue_() if r.request.url.startswith(self.base) else (outside.append(r.request.url), r.abort()))
            for route, link_text, film in (
                ("", "Watch on youtube.com", INTRO),
                ("es-mx/", "Ver en youtube.com", INTRO),
                ("about/", "Watch on youtube.com", TRAILER),
                ("es-mx/about/", "Ver en youtube.com", TRAILER),
            ):
                with self.subTest(route=route):
                    page = ctx.new_page()
                    page.goto(self.base + route, wait_until="load")
                    self.assertFalse(page.locator(".tp-film-play").is_visible())
                    self.assertFalse(page.locator(".tp-film-privacy").is_visible())
                    self.assertTrue(page.locator(".tp-film-facade img").is_visible())
                    link = page.locator("a.tp-film-out")
                    self.assertTrue(link.is_visible())
                    self.assertEqual(link.inner_text(), link_text)
                    self.assertEqual(link.get_attribute("href"), f"https://www.youtube.com/watch?v={film['youtube_id']}")
                    self.assertEqual(page.locator("iframe").count(), 0)
                    page.close()
            self.assertEqual(outside, [])
        finally:
            ctx.close()


if __name__ == "__main__":
    unittest.main()
