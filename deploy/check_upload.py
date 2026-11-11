"""Before a deploy: make sure the upload folder holds only safe web files, matching deploy/deploy.ps1.

The deploy script uploads src/ to /informatico.ai as it is, so anything else in it (a backup, a source map,
a script, a hidden file, a local settings file, leaked credentials, or CSP-violating inline scripts) would go live.
Also verifies that deploy/htaccess.txt uses LF line endings so Linux Apache never fails with 500 on CRLF.

Usage: python deploy/check_upload.py [FOLDER]      (default: src)
Exit 0: only safe web files. 1: something else is there. 2: the folder is missing or empty.
Standard library only."""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Keep in step with $allowed in deploy/deploy.ps1.
ALLOWED = {
    ".html", ".css", ".js", ".mjs",
    ".webp", ".avif", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
    ".txt", ".xml", ".json", ".webmanifest",
    ".woff", ".woff2",
    ".csv", ".tsv", ".md",
    ".mp3", ".webm",
    ".glb", ".3mf", ".step", ".stp", ".dxf",
}
TEXT_SCAN_EXTS = {
    ".html", ".css", ".js", ".mjs", ".svg",
    ".txt", ".xml", ".json", ".webmanifest", ".csv", ".tsv", ".md",
}
# Allowed types, but names that hold settings or logins, never site content.
SETTINGS_NAMES = {"credentials.json", "auth.json", "sftp.json", "deploy.local.json"}

DISALLOWED_TEXT_SIGNATURES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("PEM block header", re.compile("-----BEGIN [A-Z0-9 ]*PRIV" + "ATE KEY-----")),
    ("GitHub prefix", re.compile(r"\b(?:" + "gh" + r"p_[A-Za-z0-9]{20,}|github_" + r"pat_[A-Za-z0-9_]{20,})\b")),
    ("Cloud access identifier", re.compile(r"\b" + "AK" + r"IA[0-9A-Z]{16}\b")),
    ("Bearer prefix", re.compile(r"\b" + "sk" + r"-[A-Za-z0-9]{24,}\b")),
)


class _InlineScriptChecker(HTMLParser):
    """Detects executable inline <script> bodies via HTML tokenization (no tag regexes)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self._in_exec_script = False
        self.has_executable_inline_script = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "script":
            return
        attr_map = {k.lower(): (v or "").strip() for k, v in attrs}
        if attr_map.get("src"):
            self._in_exec_script = False
            return
        stype = attr_map.get("type", "").lower()
        if stype in ("application/ld+json", "application/json", "importmap"):
            self._in_exec_script = False
            return
        self._in_exec_script = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script":
            self._in_exec_script = False

    def handle_data(self, data: str) -> None:
        if self._in_exec_script and data.strip():
            self.has_executable_inline_script = True


def _scan_text_content(path: Path, rel_posix: str) -> list[str]:
    issues: list[str] = []
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    for label, rx in DISALLOWED_TEXT_SIGNATURES:
        if rx.search(text):
            issues.append(f"{rel_posix}: contains disallowed signature ({label})")
    if path.suffix.lower() == ".html":
        parser = _InlineScriptChecker()
        parser.feed(text)
        if parser.has_executable_inline_script:
            issues.append(f"{rel_posix}: contains executable inline script (blocked by CSP)")
    return issues


def problems(folder: Path, htaccess_path: Path | None = None) -> list[str]:
    """Each file under folder that must not be uploaded, as a relative path with the reason."""
    out: list[str] = []
    if htaccess_path is not None and htaccess_path.is_file():
        if b"\r\n" in htaccess_path.read_bytes():
            out.append(f"{htaccess_path.name}: contains CRLF line endings (Apache requires LF)")

    for f in sorted(p for p in folder.rglob("*") if p.is_file() or p.is_symlink()):
        rel = f.relative_to(folder)
        rel_posix = rel.as_posix()
        lower_name = f.name.lower()
        suffix = f.suffix.lower()
        if f.is_symlink():
            out.append(f"{rel_posix}: a link")
        elif any(part.startswith(".") for part in rel.parts):
            out.append(f"{rel_posix}: hidden")
        elif lower_name in SETTINGS_NAMES or lower_name.startswith("sftp") or lower_name.endswith(".local.json"):
            out.append(f"{rel_posix}: a local settings file")
        elif suffix not in ALLOWED:
            out.append(f"{rel_posix}: not a web file type")
        elif f.stat().st_size == 0:
            out.append(f"{rel_posix}: empty (0 bytes)")
        elif suffix in TEXT_SCAN_EXTS:
            out.extend(_scan_text_content(f, rel_posix))
    return out


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    folder = Path(argv[0]) if argv else ROOT / "src"
    if not folder.is_dir() or not any(folder.rglob("*")):
        print(f"{folder} is missing or empty; nothing to deploy.")
        return 2
    default_htaccess = (ROOT / "deploy" / "htaccess.txt") if not argv else None
    bad = problems(folder, htaccess_path=default_htaccess)
    for line in bad:
        print(f"would not be uploaded safely: {line}")
    if bad:
        print(f"{len(bad)} file(s) in {folder} failed upload safety checks.")
        return 1
    count = sum(1 for p in folder.rglob("*") if p.is_file())
    print(f"{count} file(s) in {folder}, all web files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
