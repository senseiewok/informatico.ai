#!/usr/bin/env python3
"""Regression tests for lazy <audio> DOM mounting in article-audio.mjs and deploy User-Agent headers.

Prevents:
1. Mounting a sourceless <audio> element (<audio preload="none" hidden playsinline> with getAttribute("src") === null)
   during _buildDOM(), which caused headless crawlers (meta-webindexer/1.1, meta-externalagent/1.1) to resolve `null`
   relative to each folio URL (`/<pillar>/<id>/null`, 152 HTTP 404s in Nov 2026).
2. Sending empty User-Agent ("-") headers from System.Net.Http.HttpClient in deploy/deploy.ps1.
3. Trailing-newline (`$`) or leading-dash (`--help`) bypasses in PowerShell parameter validation.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIO_MJS = ROOT / "src" / "modules" / "article-audio.mjs"
DEPLOY_PS1 = ROOT / "deploy" / "deploy.ps1"


def _find_node_cmd() -> tuple[list[str], dict[str, str]] | None:
    node_bin = shutil.which("node")
    if node_bin:
        return [node_bin], dict(os.environ)
    local_app = os.environ.get("LOCALAPPDATA", "")
    if local_app:
        vscode_exe = Path(local_app) / "Programs" / "Microsoft VS Code" / "Code.exe"
        if vscode_exe.is_file():
            env = dict(os.environ)
            env["ELECTRON_RUN_AS_NODE"] = "1"
            return [str(vscode_exe)], env
    return None


class AudioNullAndDeployTelemetryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audio_src = AUDIO_MJS.read_text(encoding="utf-8")
        self.deploy_src = DEPLOY_PS1.read_text(encoding="utf-8")

    def test_build_dom_does_not_mount_sourceless_audio_element(self) -> None:
        build_start = self.audio_src.index("_buildDOM() {")
        sync_start = self.audio_src.index("\n  _syncLabels(", build_start)
        build_body = self.audio_src[build_start:sync_start]
        self.assertNotIn('createElement("audio")', build_body)
        self.assertIn("this._audioEl = null;", build_body)
        self.assertIn("_ensureAudioElement(rawSrc)", self.audio_src)

    def test_ensure_audio_element_self_sanitizes_and_reuses_in_place(self) -> None:
        found = _find_node_cmd()
        if found is None:
            self.skipTest("No Node/Electron runtime available for ES module execution check")
        cmd_prefix, env = found
        mod_uri = AUDIO_MJS.resolve().as_uri()
        harness = f"""
class FakeNode {{
  constructor(tag) {{
    this.tagName = String(tag || '').toUpperCase();
    this.children = [];
    this.attrs = new Map();
    this.classList = {{ add() {{}} }};
    this.playbackRate = 1;
    this.readyState = 1;
    this.duration = 60;
    this.currentTime = 0;
  }}
  get firstChild() {{ return this.children[0] || null; }}
  appendChild(child) {{
    if (child.tagName === 'AUDIO' && !child.getAttribute('src')) {{
      throw new Error('Appended sourceless <audio> element into DOM');
    }}
    this.children.push(child);
    return child;
  }}
  removeChild(child) {{
    const idx = this.children.indexOf(child);
    if (idx >= 0) this.children.splice(idx, 1);
  }}
  setAttribute(k, v) {{ this.attrs.set(k, String(v)); }}
  getAttribute(k) {{ return this.attrs.has(k) ? this.attrs.get(k) : null; }}
  closest() {{ return null; }}
  querySelector() {{ return null; }}
  querySelectorAll() {{ return []; }}
  addEventListener() {{}}
  play() {{ return Promise.resolve(); }}
  pause() {{}}
}}
globalThis.HTMLElement = FakeNode;
globalThis.document = {{
  documentElement: {{ lang: 'en', dataset: {{}}, getAttribute: () => 'en' }},
  createElement: (tag) => new FakeNode(tag),
  querySelector: () => null,
  querySelectorAll: () => [],
}};
globalThis.window = {{
  location: {{ pathname: '/math/m02/' }},
  addEventListener() {{}},
  removeEventListener() {{}},
}};
const {{ TpArticleAudioElement }} = await import({json.dumps(mod_uri)});
const widget = new TpArticleAudioElement();
widget.setAttribute('data-folio', 'M.02');
widget.setAttribute('data-audio-src', '../../audio/m02-en.mp3');
widget.connectedCallback();
if (widget.children.filter((c) => c.tagName === 'AUDIO').length !== 0) {{
  throw new Error('Expected 0 <audio> elements on initial mount');
}}
// Direct sink calls with whitespace, null, or unsafe scheme must be rejected at _ensureAudioElement
for (const bad of [null, '', '   ', 'javascript:alert(1)', 'https://evil.example/a.mp3']) {{
  if (widget._ensureAudioElement(bad) !== null) {{
    throw new Error('_ensureAudioElement accepted unsafe input: ' + bad);
  }}
}}
if (widget.children.filter((c) => c.tagName === 'AUDIO').length !== 0) {{
  throw new Error('Mounted <audio> after rejected direct sink calls');
}}
if (widget._playMediaElementTrack('../../audio/m02-en.mp3', 0, 'en', 2) !== true) {{
  throw new Error('Failed valid media element track playback');
}}
let mounted = widget.children.filter((c) => c.tagName === 'AUDIO');
if (mounted.length !== 1 || mounted[0].getAttribute('src') !== '../../audio/m02-en.mp3') {{
  throw new Error('Expected 1 <audio> with valid src after first play');
}}
// Second track must reuse the existing <audio> element in place rather than appending a second node
if (widget._playMediaElementTrack('../../audio/m02-es.mp3', 0, 'es', 3) !== true) {{
  throw new Error('Failed second media element track playback');
}}
mounted = widget.children.filter((c) => c.tagName === 'AUDIO');
if (mounted.length !== 1 || mounted[0].getAttribute('src') !== '../../audio/m02-es.mp3') {{
  throw new Error('Expected in-place <audio> reuse with updated es-MX src');
}}
"""
        res = subprocess.run(
            [*cmd_prefix, "--input-type=module", "-e", harness],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
            timeout=20,
        )
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)

    def test_deploy_script_sets_explicit_user_agent_on_every_http_client(self) -> None:
        self.assertIn("$DeployUserAgent = 'SenseiEwokCFLab/0.1", self.deploy_src)
        self.assertNotIn("New-Object System.Net.Http.HttpClient", self.deploy_src)
        self.assertNotIn("Invoke-WebRequest", self.deploy_src)
        created = Counter(
            re.findall(r"\$(\w+)\s*=\s*\[System\.Net\.Http\.HttpClient\]::new\(\)", self.deploy_src)
        )
        tagged = Counter(
            re.findall(
                r"\$(\w+)\.DefaultRequestHeaders\.UserAgent\.ParseAdd\(\$DeployUserAgent\)",
                self.deploy_src,
            )
        )
        self.assertGreaterEqual(sum(created.values()), 3)
        self.assertEqual(created, tagged, f"HttpClient creation vs User-Agent mismatch: {created} vs {tagged}")

    def test_deploy_powershell_ast_and_strict_anchor_validation(self) -> None:
        self.assertIn(r"\A[A-Za-z0-9](?:[A-Za-z0-9.\-]*[A-Za-z0-9])?\z", self.deploy_src)
        self.assertIn(r"\A[A-Za-z0-9._][A-Za-z0-9._/\-]*\z", self.deploy_src)
        pwsh_bin = shutil.which("pwsh")
        if not pwsh_bin:
            self.skipTest("pwsh not installed on PATH")
        env = dict(os.environ)
        env["DEPLOY_PS1_PATH"] = str(DEPLOY_PS1)
        ps_check = r"""
$tokens = $null; $errors = $null
[void][System.Management.Automation.Language.Parser]::ParseFile($env:DEPLOY_PS1_PATH, [ref]$tokens, [ref]$errors)
if ($errors.Count -gt 0) { $errors | ForEach-Object { Write-Error $_.ToString() }; exit 1 }
$hostRx = '\A[A-Za-z0-9](?:[A-Za-z0-9.\-]*[A-Za-z0-9])?\z'
$dirRx  = '\A[A-Za-z0-9._][A-Za-z0-9._/\-]*\z'
foreach ($badHost in @("example.com`n", "--help", "-bad.host", "bad.host-")) {
    if ($badHost -match $hostRx) { throw "Accepted hostile host: $badHost" }
}
foreach ($goodHost in @("ftp.example.net", "a", "sub-1.host2.org")) {
    if ($goodHost -notmatch $hostRx) { throw "Rejected valid host: $goodHost" }
}
foreach ($badDir in @("informatico.ai`n", "-flag", "--option")) {
    if ($badDir -match $dirRx) { throw "Accepted hostile dir: $badDir" }
}
"""
        res = subprocess.run(
            [pwsh_bin, "-NoProfile", "-Command", ps_check],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
            timeout=15,
        )
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)


if __name__ == "__main__":
    unittest.main()
