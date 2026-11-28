#!/usr/bin/env python3
"""The Contents dialog on a phone (src/modules/folio-router.mjs, .tp-contents in informatico.css).

Two reader reports, 2026-11-28: on a phone, opening Contents "changes the size and scrolling gets messed up", and
there was no way to go to a whole section such as Mathematics. What was measured at 375x812 and 390x844:

- the dialog's first focusable element was the search field, so showModal() focused it and a touch screen
  answered with its keyboard (the view resized);
- scrolling the dialog to either end went on to scroll the page behind it, so closing left the reader somewhere
  else on the page;
- the masthead hides its seven section links at 860px and below, and the dialog did not list them.

Part one reads the built pages with html.parser (no browser): every page with the dialog lists the seven sections,
in English or Mexican Spanish, each link resolving to a built page, the current one marked as the masthead marks
it. Part two drives Chromium with touch emulation under the Content-Security-Policy from deploy/htaccess.txt.

Part two is skipped when Playwright or Chromium is not installed. Set MOBILE_CONTENTS_SHOTS to a folder to save
screenshots.
"""
from __future__ import annotations

import os
import unittest
from html.parser import HTMLParser
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover
    sync_playwright = None

from tests.test_a11y_axe import _load_csp_header, find_chrome
from tests.test_film_facade_browser import serve_with_headers

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
SECTION_KEYS = ("engineering", "architecture", "physics", "math", "bounties", "toolchain", "about")
SECTIONS_EN = ("Engineering", "Architecture", "Physics", "Mathematics", "Bounties", "Tech & Tools", "About")
SECTIONS_ES = ("Ingeniería", "Arquitectura", "Física", "Matemáticas", "Retos", "Herramientas", "Acerca de")
PHONES = ((375, 812), (390, 844))
# (name, route, the section the page belongs to, labels, list heading)
PAGES = (
    ("cover-en", "", None, SECTIONS_EN, "Sections"),
    ("essay-en", "math/m01/", "math", SECTIONS_EN, "Sections"),
    ("cover-es", "es-mx/", None, SECTIONS_ES, "Secciones"),
    ("essay-es", "es-mx/physics/p01/", "physics", SECTIONS_ES, "Secciones"),
)
OPENER = ".tp-masthead-tools [data-open-contents]"
BOUND_JS = "document.getElementById('tp-contents').dataset.bound === 'true'"  # folio-router.mjs has run
STATE_JS = """() => {
  const d = document.getElementById('tp-contents');
  const root = document.documentElement;
  const box = d.getBoundingClientRect();
  const a = document.activeElement;
  return {
    open: d.open,
    locked: root.classList.contains('tp-contents-open'),
    scrollY: Math.round(window.scrollY),
    innerWidth: window.innerWidth,
    clientWidth: root.clientWidth,
    pageScrollWidth: Math.max(root.scrollWidth, document.body.scrollWidth),
    dialogScrollWidth: d.scrollWidth,
    dialogClientWidth: d.clientWidth,
    dialogScrollHeight: d.scrollHeight,
    dialogClientHeight: d.clientHeight,
    dialogScrollTop: Math.round(d.scrollTop),
    box: [box.left, box.top, box.right, box.bottom],
    overscroll: getComputedStyle(d).overscrollBehaviorY,
    animation: getComputedStyle(d).animationName,
    activeId: a ? a.id : '',
    activeTag: a ? a.tagName : '',
    activeIsOpener: !!a && a.matches('[data-open-contents]'),
    expanded: Array.from(document.querySelectorAll('[data-open-contents][aria-expanded]')).map((b) => b.getAttribute('aria-expanded')),
  };
}"""
SECTION_LINKS_JS = """() => Array.from(document.querySelectorAll('#tp-contents .tp-contents-sections a')).map((a) => {
  const r = a.getBoundingClientRect();
  return {text: a.textContent.trim(), key: a.getAttribute('data-contents-section'), current: a.getAttribute('aria-current'),
          left: r.left, right: r.right, top: r.top, height: r.height, shown: r.width > 0 && r.height > 0};
})"""


class _ContentsMarkup(HTMLParser):
    """The section links inside dialog#tp-contents, the masthead's own links, and the dialog heading's attributes."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, dict[str, str | None]]] = []
        self.section_links: list[dict] = []
        self.masthead_links: list[dict] = []
        self.list_heading = ""
        self.list_heading_id: str | None = None
        self.nav_labelledby: str | None = None
        self.title_attrs: dict[str, str | None] | None = None
        self.focusable_before_title = 0
        self._link: dict | None = None
        self._in_list_heading = False

    def _inside(self, tag: str, cls: str = "", el_id: str = "") -> bool:
        for t, a in self.stack:
            if t == tag and (not cls or cls in (a.get("class") or "").split()) and (not el_id or a.get("id") == el_id):
                return True
        return False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        void = tag in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
        in_dialog = self._inside("dialog", el_id="tp-contents")
        if in_dialog and a.get("id") == "tp-contents-title":
            self.title_attrs = a
        elif in_dialog and self.title_attrs is None and tag in {"a", "button", "input", "select", "textarea"}:
            self.focusable_before_title += 1
        if in_dialog and tag == "nav" and "tp-contents-sections" in (a.get("class") or "").split():
            self.nav_labelledby = a.get("aria-labelledby")
        in_list = in_dialog and self._inside("nav", "tp-contents-sections")
        if in_list and tag == "h3":
            self._in_list_heading = True
            self.list_heading_id = a.get("id")
        if tag == "a":
            if in_list:
                self._link = {"where": "dialog", "href": a.get("href"), "key": a.get("data-contents-section"),
                              "current": a.get("aria-current"), "text": ""}
            elif self._inside("nav", "tp-nav") and a.get("data-tp-nav"):
                self._link = {"where": "masthead", "href": a.get("href"), "key": a.get("data-tp-nav"),
                              "current": a.get("aria-current"), "text": ""}
        if not void:
            self.stack.append((tag, a))

    def handle_endtag(self, tag):
        if tag == "a" and self._link is not None:
            (self.section_links if self._link["where"] == "dialog" else self.masthead_links).append(self._link)
            self._link = None
        if tag == "h3":
            self._in_list_heading = False
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self._link is not None:
            self._link["text"] += data
        if self._in_list_heading:
            self.list_heading += data


def _pages_with_contents() -> list[Path]:
    return sorted(p for p in SRC.rglob("*.html") if 'id="tp-contents"' in p.read_text(encoding="utf-8"))


class ContentsSectionListMarkupTests(unittest.TestCase):
    """No browser: the section list is in the HTML of every page that has the Contents dialog."""

    def test_every_page_lists_the_seven_sections_in_its_language(self) -> None:
        pages = _pages_with_contents()
        self.assertGreater(len(pages), 200, "expected the whole site, English and Spanish")
        spanish = 0
        for path in pages:
            rel = path.relative_to(SRC).as_posix()
            is_es = rel.startswith("es-mx/")
            spanish += is_es
            parsed = _ContentsMarkup()
            parsed.feed(path.read_text(encoding="utf-8"))
            parsed.close()
            with self.subTest(page=rel):
                links = parsed.section_links
                self.assertEqual(tuple(l["key"] for l in links), SECTION_KEYS)
                self.assertEqual(tuple(l["text"].strip() for l in links), SECTIONS_ES if is_es else SECTIONS_EN)
                self.assertEqual(parsed.list_heading.strip(), "Secciones" if is_es else "Sections")
                self.assertIsNotNone(parsed.nav_labelledby)
                self.assertEqual(parsed.nav_labelledby, parsed.list_heading_id)
                # Each link leads to that section's built page, in the same language.
                for link in links:
                    href = link["href"] or ""
                    target = (SRC / href.lstrip("/")) if href.startswith("/") else (path.parent / href)
                    target = target.resolve() / "index.html"
                    self.assertTrue(target.is_file(), f"{href} does not lead to a built page")
                    target_rel = target.relative_to(SRC.resolve()).as_posix()
                    if not href.startswith("/"):
                        self.assertEqual(target_rel, ("es-mx/" if is_es else "") + link["key"] + "/index.html")
                # The current section is the one the masthead marks, and no other.
                masthead_current = [l["key"] for l in parsed.masthead_links if l["current"] == "page"]
                dialog_current = [l["key"] for l in links if l["current"] == "page"]
                self.assertLessEqual(len(dialog_current), 1)
                if parsed.masthead_links:
                    self.assertEqual(tuple(l["key"] for l in parsed.masthead_links), SECTION_KEYS)
                    self.assertEqual(dialog_current, masthead_current)
                # The heading takes the opening focus, ahead of any field or button.
                self.assertIsNotNone(parsed.title_attrs, "dialog heading missing")
                self.assertIn("autofocus", parsed.title_attrs)
                self.assertEqual(parsed.title_attrs.get("tabindex"), "-1")
        self.assertGreater(spanish, 100)

    def test_a_section_page_marks_itself(self) -> None:
        for route, key in (("math/index.html", "math"), ("es-mx/math/index.html", "math"),
                           ("es-mx/bounties/index.html", "bounties"), ("about/index.html", "about")):
            parsed = _ContentsMarkup()
            parsed.feed((SRC / route).read_text(encoding="utf-8"))
            with self.subTest(page=route):
                self.assertEqual([l["key"] for l in parsed.section_links if l["current"] == "page"], [key])
        cover = _ContentsMarkup()
        cover.feed((SRC / "index.html").read_text(encoding="utf-8"))
        self.assertEqual([l for l in cover.section_links if l["current"]], [])


@unittest.skipIf(sync_playwright is None, "Playwright is not installed in this Python")
class MobileContentsBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome = find_chrome()
        if not cls.chrome:
            raise unittest.SkipTest("no Chromium found (set CHROME_PATH)")
        cls.httpd, cls.base = serve_with_headers(SRC, {"Content-Security-Policy": _load_csp_header()})
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=cls.chrome,
            headless=True,
            args=["--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1"],
        )
        shots = os.environ.get("MOBILE_CONTENTS_SHOTS")
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

    def _phone(self, route: str, width: int = 375, height: int = 812, **context_options):
        ctx = self.browser.new_context(
            viewport={"width": width, "height": height}, is_mobile=True, has_touch=True, **context_options
        )
        try:
            return ctx, self._page(ctx, route)
        except Exception:
            ctx.close()
            raise

    def _page(self, ctx, route: str):
        page = ctx.new_page()
        self.errors: list[str] = []
        page.on("console", lambda m: self.errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: self.errors.append(str(e)))
        page.goto(self.base + route, wait_until="load")
        page.wait_for_function(BOUND_JS, timeout=20000)
        return page

    def _open(self, page) -> None:
        page.locator(OPENER).tap()
        page.wait_for_function("document.getElementById('tp-contents').open")
        page.wait_for_timeout(250)

    def _touch_scroll(self, page, distance: int) -> None:
        """Finger drags up the middle of the screen (down, for a negative distance), as a phone sends them.

        Real touch events through the DevTools protocol: these scroll whatever a finger would scroll, including
        the page behind a dialog that lets the scroll through."""
        vp = page.viewport_size
        x, top, bottom = vp["width"] // 2, 120, vp["height"] - 120
        cdp = page.context.new_cdp_session(page)
        left = abs(distance)
        while left > 0:
            step = min(left, bottom - top)
            start, end = (bottom, bottom - step) if distance > 0 else (top, top + step)
            cdp.send("Input.dispatchTouchEvent", {"type": "touchStart", "touchPoints": [{"x": x, "y": start}]})
            for i in range(1, 11):
                y = start + (end - start) * i / 10
                cdp.send("Input.dispatchTouchEvent", {"type": "touchMove", "touchPoints": [{"x": x, "y": y}]})
                page.wait_for_timeout(16)
            for _ in range(6):  # rest the finger before lifting it, so the list does not coast on
                cdp.send("Input.dispatchTouchEvent", {"type": "touchMove", "touchPoints": [{"x": x, "y": end}]})
                page.wait_for_timeout(30)
            cdp.send("Input.dispatchTouchEvent", {"type": "touchEnd", "touchPoints": []})
            page.wait_for_timeout(120)
            left -= step
        cdp.detach()
        page.wait_for_timeout(400)

    def _shot(self, page, name: str) -> None:
        if self.shots:
            page.screenshot(path=str(self.shots / f"{name}.jpg"), type="jpeg", quality=70)

    def test_opening_keeps_the_view_its_size_and_the_keyboard_down(self) -> None:
        for width, height in PHONES:
            for name, route, _section, _labels, _heading in PAGES:
                with self.subTest(page=name, width=width):
                    ctx, page = self._phone(route, width, height)
                    try:
                        before = page.evaluate(STATE_JS)
                        self.assertLessEqual(before["pageScrollWidth"], width, "page wider than the phone")
                        self._shot(page, f"{name}-{width}-closed")
                        self._open(page)
                        now = page.evaluate(STATE_JS)
                        self._shot(page, f"{name}-{width}-open")
                        # A focused text field brings up a phone's keyboard, which resizes the view.
                        self.assertNotIn(now["activeTag"], ("INPUT", "TEXTAREA", "SELECT"))
                        self.assertEqual(now["activeId"], "tp-contents-title")
                        # Same layout width, nothing wider than the screen, the dialog exactly on it.
                        self.assertEqual((now["innerWidth"], now["clientWidth"]), (before["innerWidth"], before["clientWidth"]))
                        self.assertLessEqual(now["pageScrollWidth"], width)
                        self.assertLessEqual(now["dialogScrollWidth"], now["dialogClientWidth"], "dialog scrolls sideways")
                        self.assertEqual(now["box"], [0, 0, width, height])
                        # The list is longer than the screen and scrolls inside the dialog.
                        self.assertGreater(now["dialogScrollHeight"], now["dialogClientHeight"])
                        self.assertEqual(now["overscroll"], "contain")
                        self._touch_scroll(page, 700)
                        self.assertGreater(page.evaluate(STATE_JS)["dialogScrollTop"], 300, "the dialog did not scroll")
                        self.assertEqual(self.errors, [])
                    finally:
                        ctx.close()

    def test_page_behind_stays_put_and_returns_to_where_it_was(self) -> None:
        for width, height in PHONES:
            for name, route, _section, _labels, _heading in PAGES:
                with self.subTest(page=name, width=width):
                    ctx, page = self._phone(route, width, height)
                    try:
                        # The masthead scrolls away with the page, so open from mid-page as a keyboard or a
                        # second opener would: the button's own click, with the page 600px down.
                        page.evaluate("window.scrollTo({top: 600, behavior: 'instant'})")
                        page.wait_for_timeout(150)
                        start = page.evaluate(STATE_JS)
                        self.assertEqual(start["scrollY"], 600)
                        page.evaluate("(sel) => document.querySelector(sel).click()", OPENER)
                        page.wait_for_function("document.getElementById('tp-contents').open")
                        page.wait_for_timeout(250)
                        opened = page.evaluate(STATE_JS)
                        self.assertEqual(opened["scrollY"], 600)
                        self.assertEqual(opened["dialogScrollTop"], 0)
                        # Drag to the end of the list and keep dragging: the page behind must not take over.
                        page.evaluate("document.getElementById('tp-contents').scrollTop = 1e7")
                        for _ in range(3):
                            self._touch_scroll(page, 900)
                        page.mouse.move(width // 2, height // 2)
                        page.mouse.wheel(0, 2500)
                        page.wait_for_timeout(250)
                        at_end = page.evaluate(STATE_JS)
                        self.assertEqual(at_end["scrollY"], 600, "the page behind the open dialog scrolled")
                        # And the same at the top of the list.
                        page.evaluate("document.getElementById('tp-contents').scrollTop = 0")
                        self._touch_scroll(page, -900)
                        self.assertEqual(page.evaluate(STATE_JS)["scrollY"], 600)
                        page.keyboard.press("Escape")
                        page.wait_for_function("!document.getElementById('tp-contents').open")
                        page.wait_for_timeout(150)
                        closed = page.evaluate(STATE_JS)
                        self.assertFalse(closed["locked"])
                        self.assertEqual(closed["scrollY"], 600, "closing moved the page")
                        self.assertEqual((closed["innerWidth"], closed["clientWidth"]), (start["innerWidth"], start["clientWidth"]))
                        # The page scrolls again once the dialog is closed.
                        self._touch_scroll(page, 400)
                        self.assertGreater(page.evaluate(STATE_JS)["scrollY"], 700)
                        self.assertEqual(self.errors, [])
                    finally:
                        ctx.close()

    def test_escape_and_close_button_close_and_focus_returns(self) -> None:
        for name, route, _section, _labels, _heading in PAGES:
            with self.subTest(page=name):
                ctx, page = self._phone(route)
                try:
                    self._open(page)
                    self.assertEqual(set(page.evaluate(STATE_JS)["expanded"]), {"true"})
                    page.keyboard.press("Escape")
                    page.wait_for_function("!document.getElementById('tp-contents').open")
                    state = page.evaluate(STATE_JS)
                    self.assertTrue(state["activeIsOpener"], "focus did not return to the Contents button")
                    self.assertEqual(set(state["expanded"]), {"false"})
                    self.assertFalse(state["locked"])
                    self.assertEqual(state["scrollY"], 0)
                    # Again with the Close button, scrolled down the list first.
                    self._open(page)
                    self._touch_scroll(page, 500)
                    page.locator("#tp-contents [data-close-contents]").tap()
                    page.wait_for_function("!document.getElementById('tp-contents').open")
                    state = page.evaluate(STATE_JS)
                    self.assertTrue(state["activeIsOpener"])
                    self.assertFalse(state["locked"])
                    # A third opening starts at the top of the list again.
                    self._open(page)
                    self.assertEqual(page.evaluate(STATE_JS)["dialogScrollTop"], 0)
                    self.assertEqual(self.errors, [])
                finally:
                    ctx.close()

    def test_focus_stays_inside_the_open_dialog(self) -> None:
        ctx, page = self._phone("math/m01/")
        try:
            self._open(page)
            for _ in range(12):
                page.keyboard.press("Shift+Tab")
                inside = page.evaluate(
                    "() => { const a = document.activeElement; return !a || a === document.body || !!a.closest('#tp-contents'); }"
                )
                self.assertTrue(inside, "focus left the open dialog for the page behind it")
        finally:
            ctx.close()

    def test_sections_are_listed_first_and_lead_to_the_section(self) -> None:
        for width, height in PHONES:
            for name, route, section, labels, heading in PAGES:
                with self.subTest(page=name, width=width):
                    ctx, page = self._phone(route, width, height)
                    try:
                        # The masthead's own section links are hidden at this width: the dialog is the way in.
                        self.assertEqual(page.locator(".tp-masthead .tp-nav").evaluate("(n) => getComputedStyle(n).display"), "none")
                        self._open(page)
                        links = page.evaluate(SECTION_LINKS_JS)
                        self.assertEqual(tuple(l["text"] for l in links), labels)
                        self.assertEqual(page.locator("#tp-contents-sections-title").inner_text().strip().lower(), heading.lower())
                        self.assertEqual(page.get_by_role("navigation", name=heading, exact=True).count(), 1)
                        self.assertEqual([l["key"] for l in links if l["current"] == "page"], [section] if section else [])
                        first_essay_top = page.locator("#tp-contents .tp-contents-grid").evaluate("(n) => n.getBoundingClientRect().top")
                        for link in links:
                            self.assertTrue(link["shown"], link["text"])
                            self.assertGreaterEqual(link["left"], 0)
                            self.assertLessEqual(link["right"], width)
                            self.assertGreaterEqual(link["height"], 44, f"{link['text']}: touch target under 44px")
                            self.assertLess(link["top"], first_essay_top, "sections must come before the essay list")
                            self.assertLess(link["top"], height, "sections must be on the first screen")
                        # Typing a search puts the results first; clearing it brings the sections back.
                        page.locator("#tp-contents-search").fill("zz")
                        self.assertFalse(any(l["shown"] for l in page.evaluate(SECTION_LINKS_JS)))
                        page.locator("#tp-contents-search").fill("")
                        self.assertTrue(all(l["shown"] for l in page.evaluate(SECTION_LINKS_JS)))
                        # Tap Mathematics: the Mathematics page of the same language opens, marked as current.
                        es = route.startswith("es-mx/")
                        page.locator("#tp-contents .tp-contents-sections a[data-contents-section='math']").tap()
                        page.wait_for_url(self.base + ("es-mx/" if es else "") + "math/", timeout=5000)
                        page.wait_for_function(BOUND_JS, timeout=20000)
                        self.assertEqual(page.evaluate("document.documentElement.lang"), "es-MX" if es else "en")
                        self.assertIn("Matemáticas" if es else "Mathematics", page.locator("h1").first.inner_text())
                        arrived = page.evaluate(STATE_JS)
                        self.assertFalse(arrived["open"])
                        self.assertFalse(arrived["locked"])
                        self._open(page)
                        current = [l["key"] for l in page.evaluate(SECTION_LINKS_JS) if l["current"] == "page"]
                        self.assertEqual(current, ["math"])
                        self.assertEqual(self.errors, [])
                    finally:
                        ctx.close()

    def test_every_section_link_opens_its_page(self) -> None:
        for name, route, _section, _labels, _heading in (PAGES[1], PAGES[3]):
            es = route.startswith("es-mx/")
            ctx, page = self._phone(route)
            try:
                for key in SECTION_KEYS:
                    with self.subTest(page=name, section=key):
                        page.goto(self.base + route, wait_until="load")
                        page.wait_for_function(BOUND_JS, timeout=20000)
                        self._open(page)
                        with page.expect_navigation(wait_until="load") as nav:
                            page.locator(f"#tp-contents .tp-contents-sections a[data-contents-section='{key}']").tap()
                        self.assertEqual(nav.value.status, 200)
                        self.assertEqual(page.url, self.base + ("es-mx/" if es else "") + key + "/")
            finally:
                ctx.close()

    def test_a_link_tap_closes_the_dialog_and_frees_the_page(self) -> None:
        ctx, page = self._phone("")
        try:
            # Hold the page here, to see the state the reader would come back to.
            page.evaluate("document.addEventListener('click', (ev) => { if (ev.target.closest('a')) ev.preventDefault(); })")
            self._open(page)
            page.locator("#tp-contents .tp-contents-sections a[data-contents-section='physics']").tap()
            page.wait_for_function("!document.getElementById('tp-contents').open", timeout=3000)
            state = page.evaluate(STATE_JS)
            self.assertFalse(state["locked"])
            self.assertEqual(set(state["expanded"]), {"false"})
        finally:
            ctx.close()

    def test_reduced_motion_opens_without_animation(self) -> None:
        for setting, want in (("reduce", "none"), ("no-preference", "tp-contents-in")):
            with self.subTest(reduced_motion=setting):
                ctx, page = self._phone("", reduced_motion=setting)
                try:
                    page.locator(OPENER).tap()
                    page.wait_for_function("document.getElementById('tp-contents').open")
                    self.assertEqual(page.evaluate(STATE_JS)["animation"], want)
                finally:
                    ctx.close()

    def _desktop_round_trip(self, browser, classic_scrollbar: bool) -> None:
        ctx = browser.new_context(viewport={"width": 1280, "height": 800})
        try:
            page = self._page(ctx, "math/m01/")
            tools_right = "document.querySelector('.tp-masthead-tools').getBoundingClientRect().right"
            page.evaluate("window.scrollTo({top: 500, behavior: 'instant'})")
            before = page.evaluate(STATE_JS)
            before_x = page.evaluate(tools_right)
            body_width = "document.body.getBoundingClientRect().width"
            before_body = page.evaluate(body_width)
            self.assertEqual(before["innerWidth"] > before["clientWidth"], classic_scrollbar)
            page.evaluate("(sel) => document.querySelector(sel).click()", OPENER)
            page.wait_for_function("document.getElementById('tp-contents').open")
            page.wait_for_timeout(250)
            opened = page.evaluate(STATE_JS)
            # With a keyboard and a mouse the search field is ready to type in.
            self.assertEqual(opened["activeId"], "tp-contents-search")
            # Locking the page hides its scrollbar; the layout stays where it was.
            self.assertTrue(opened["locked"])
            # (Under a pixel is allowed: with the gutter kept, Chromium measures vw-based padding without it.)
            self.assertAlmostEqual(page.evaluate(tools_right), before_x, delta=1, msg="the page shifted sideways when Contents opened")
            self.assertEqual(page.evaluate(body_width), before_body)
            # The masthead shows the sections here, so the dialog does not repeat them.
            self.assertFalse(any(l["shown"] for l in page.evaluate(SECTION_LINKS_JS)))
            # The wheel over the backdrop does not move the page.
            page.mouse.move(8, 400)
            page.mouse.wheel(0, 1200)
            page.wait_for_timeout(200)
            self.assertEqual(page.evaluate(STATE_JS)["scrollY"], 500)
            # A click inside the dialog's own box, on no control, keeps it open; one on the backdrop closes it.
            box = opened["box"]
            page.mouse.click(box[0] + 6, box[1] + 6)
            page.wait_for_timeout(100)
            self.assertTrue(page.evaluate(STATE_JS)["open"])
            page.mouse.click(6, 6)
            page.wait_for_function("!document.getElementById('tp-contents').open", timeout=3000)
            closed = page.evaluate(STATE_JS)
            self.assertTrue(closed["activeIsOpener"])
            self.assertFalse(closed["locked"])
            self.assertEqual(closed["scrollY"], 500)
            self.assertEqual(page.evaluate(tools_right), before_x)
            self.assertEqual(page.evaluate(body_width), before_body)
            self.assertEqual(self.errors, [])
        finally:
            ctx.close()

    def test_desktop_keeps_its_width_search_focus_and_backdrop_close(self) -> None:
        self._desktop_round_trip(self.browser, classic_scrollbar=False)

    def test_desktop_with_a_classic_scrollbar_does_not_shift(self) -> None:
        # Headless Chromium hides scrollbars; a desktop reader usually has one that takes up 15px or so.
        browser = self.pw.chromium.launch(
            executable_path=self.chrome,
            headless=True,
            ignore_default_args=["--hide-scrollbars"],
            args=["--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1"],
        )
        try:
            self._desktop_round_trip(browser, classic_scrollbar=True)
        finally:
            browser.close()


if __name__ == "__main__":
    unittest.main()
