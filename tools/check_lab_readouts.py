#!/usr/bin/env python3
"""Lab readout parity: every interactive lab must show, at its default slider values, exactly the readouts its folio
prints. Grounding reviews on 2026-11-14 found 40 of 48 labs disagreeing with their pages (values under the wrong
labels, impossible numbers, and verdicts the text had withdrawn); this check keeps them aligned.

Method: serve src/ on a free localhost port, open each folio page in headless Chromium, read the readouts as
printed in the HTML, fire `input` on every slider at its default value, and compare what the lab writes.

Requires the `playwright` Python package and a Chromium build (`python -m playwright install chromium`).
Run: python tools/check_lab_readouts.py      exit 0 all match, 1 mismatches, 2 Playwright unavailable
"""
from __future__ import annotations

import functools
import http.server
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
PILLARS = (("engineering", "e"), ("architecture", "a"), ("physics", "p"), ("math", "m"))

SWEEP_JS = """async () => {
  const n = (x) => (x || "").replace(/\\s+/g, " ").trim();
  const html = await (await fetch(location.pathname, { cache: "reload" })).text();
  const printed = [...new DOMParser().parseFromString(html, "text/html")
    .querySelectorAll(".tp-readout-strip .tp-readout-box")]
    .map((b) => [n(b.querySelector(".tp-readout-k")?.textContent), n(b.querySelector(".tp-readout-v")?.textContent)]);
  const sliders = [...document.querySelectorAll('input[type="range"]')];
  const bound = sliders.some((s) => s.dataset.bound === "true");
  sliders.forEach((s) => s.dispatchEvent(new Event("input", { bubbles: true })));
  await new Promise((r) => setTimeout(r, 150));
  const lab = [...document.querySelectorAll(".tp-readout-strip .tp-readout-v")].map((v) => n(v.textContent));
  return { bound, rows: printed.map(([label, value], i) => ({ label, printed: value, lab: lab[i] })) };
}"""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args) -> None:  # keep the report readable
        pass


def pages() -> list[str]:
    counts = {"math": 15}
    return [f"/{pillar}/{code}{i:02d}/" for pillar, code in PILLARS for i in range(1, counts.get(pillar, 12) + 1)]


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("SKIPPED lab readout parity: the playwright package is not installed")
        return 2
    handler = functools.partial(QuietHandler, directory=str(SRC))
    with http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler) as httpd:
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        failures: list[str] = []
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            for path in pages():
                resp = page.goto(f"http://127.0.0.1:{port}{path}", wait_until="load")
                if resp is None or not resp.ok:
                    failures.append(f"{path} did not load ({resp.status if resp else 'no response'})")
                    continue
                page.wait_for_timeout(500)
                result = page.evaluate(SWEEP_JS)
                if len(result["rows"]) != 4:
                    failures.append(f"{path} has {len(result['rows'])} readouts, expected 4")
                if not result["bound"]:
                    failures.append(f"{path} lab script did not attach to its sliders")
                for row in result["rows"]:
                    if row["printed"] != row["lab"]:
                        failures.append(f"{path} [{row['label']}] printed {row['printed']!r} | lab {row['lab']!r}")
                for e in errors:
                    failures.append(f"{path} page error: {e[:160]}")
                errors.clear()
            browser.close()
        httpd.shutdown()
    for f in failures:
        print(f"FAIL {f}")
    print(f"SUMMARY lab readout parity: {len(pages())} pages, {len(failures)} mismatch(es)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
