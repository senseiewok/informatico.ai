#!/usr/bin/env python3
"""Build-time LaTeX-to-MathML Core cache & HTMLParser allowlist sanitizer.

Production site builds remain 100% stdlib-only: build_longform_folios.py reads
pre-rendered MathML Core markup from tools/folios/mathml_cache.json and verifies
SHA-256 digests and sanitizer invariants without requiring third-party packages.

Regenerating mathml_cache.json after editing a folio's `governing_law_latex`
requires an offline Python environment with `latex2mathml`:
    <math-audit-python> tools/folios/mathml_render.py --regenerate
"""
from __future__ import annotations

import argparse
import hashlib
import html
import html.parser
import importlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FOLIOS_DIR = Path(__file__).resolve().parent
CACHE_PATH = FOLIOS_DIR / "mathml_cache.json"
PILLAR_DIRS = ("engineering", "architecture", "physics", "math")

ALLOWED_TAGS = frozenset({
    "math",
    "mrow",
    "mi",
    "mn",
    "mo",
    "mtext",
    "mspace",
    "msup",
    "msub",
    "msubsup",
    "mfrac",
    "msqrt",
    "mroot",
    "munder",
    "mover",
    "munderover",
    "mtable",
    "mtr",
    "mtd",
    "mpadded",
    "mphantom",
    "mstyle",
    "semantics",
})

DROP_SUBTREE_TAGS = frozenset({
    "script",
    "style",
    "iframe",
    "object",
    "svg",
    "annotation",
    "annotation-xml",
    "noscript",
    "template",
    "textarea",
    "title",
    "xmp",
    "noembed",
    "noframes",
})

HTML_VOID_TAGS = frozenset({
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
})

ALLOWED_MATHVARIANT = frozenset({
    "normal",
    "italic",
    "bold",
    "bold-italic",
    "double-struck",
    "script",
    "fraktur",
    "sans-serif",
    "monospace",
})

ALLOWED_BOOL = frozenset({"true", "false"})
ALLOWED_FORM = frozenset({"prefix", "infix", "postfix"})
LENGTH_RE = re.compile(r"^-?\d+(?:\.\d+)?(?:em|ex|px|rem)$")
LINETHICK_RE = re.compile(r"^(?:\d+(?:\.\d+)?(?:em|ex|px|rem|%)?|thin|medium|thick)$")
DIGITS_RE = re.compile(r"^[1-9]\d*$")


def _filter_attrs(tag: str, attrs: list[tuple[str, str | None]]) -> list[tuple[str, str]]:
    """Keep strictly allowlisted MathML Core presentation attributes; drop everything else."""
    attr_map = {k.lower(): (v or "").strip() for k, v in attrs if k}
    kept: list[tuple[str, str]] = []

    if tag == "math":
        display = attr_map.get("display", "block").lower()
        kept.append(("display", "inline" if display == "inline" else "block"))
        return kept

    if tag == "mo":
        for bool_attr in ("stretchy", "fence", "separator", "symmetric", "accent", "movablelimits"):
            val = attr_map.get(bool_attr, "").lower()
            if val in ALLOWED_BOOL:
                kept.append((bool_attr, val))
        form = attr_map.get("form", "").lower()
        if form in ALLOWED_FORM:
            kept.append(("form", form))
        for size_attr in ("lspace", "rspace", "minsize", "maxsize"):
            val = attr_map.get(size_attr, "").lower()
            if LENGTH_RE.match(val) or (size_attr == "maxsize" and val == "infinity"):
                kept.append((size_attr, val))
        return kept

    if tag in ("mi", "mstyle"):
        mv = attr_map.get("mathvariant", "").lower()
        if mv in ALLOWED_MATHVARIANT:
            kept.append(("mathvariant", mv))
        return kept

    if tag == "mspace":
        for dim_attr in ("width", "height", "depth"):
            val = attr_map.get(dim_attr, "").lower()
            if LENGTH_RE.match(val):
                kept.append((dim_attr, val))
        return kept

    if tag == "mfrac":
        lt = attr_map.get("linethickness", "").lower()
        if LINETHICK_RE.match(lt):
            kept.append(("linethickness", lt))
        return kept

    if tag == "mtd":
        for span_attr in ("columnspan", "rowspan"):
            val = attr_map.get(span_attr, "")
            if DIGITS_RE.match(val):
                kept.append((span_attr, val))
        return kept

    return kept


class _MathMLSanitizer(html.parser.HTMLParser):
    """Token-by-token MathML Core sanitizer with explicit end tags and zero inline styles."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.stack: list[str] = []
        self.drop_stack: list[str] = []
        self.finished_root = False

    def _emit_open(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        kept = _filter_attrs(tag, attrs)
        for k, _ in kept:
            if k == "style":
                raise ValueError("Sanitizer invariant violated: inline style attribute filtered unexpectedly")
        attr_str = "".join(
            f' {k}="{html.escape(v, quote=True)}"' for k, v in kept
        )
        self.out.append(f"<{tag}{attr_str}>")

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        if self.drop_stack:
            if t not in HTML_VOID_TAGS:
                self.drop_stack.append(t)
            return
        if t in DROP_SUBTREE_TAGS:
            self.drop_stack.append(t)
            return
        if t in HTML_VOID_TAGS or t not in ALLOWED_TAGS:
            return
        if t == "math":
            if self.stack or self.finished_root:
                return
        elif not self.stack:
            return
        self._emit_open(t, attrs)
        self.stack.append(t)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = tag.lower()
        if self.drop_stack or t in DROP_SUBTREE_TAGS or t in HTML_VOID_TAGS or t not in ALLOWED_TAGS:
            return
        if t == "math":
            if self.stack or self.finished_root:
                return
            self.finished_root = True
        elif not self.stack:
            return
        self._emit_open(t, attrs)
        self.out.append(f"</{t}>")

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()
        if self.drop_stack:
            for i in range(len(self.drop_stack) - 1, -1, -1):
                if self.drop_stack[i] == t:
                    del self.drop_stack[i:]
                    break
            return
        if t not in ALLOWED_TAGS:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == t:
                while len(self.stack) > i:
                    top = self.stack.pop()
                    self.out.append(f"</{top}>")
                    if top == "math":
                        self.finished_root = True
                break

    def handle_data(self, data: str) -> None:
        if self.drop_stack or not self.stack:
            return
        if not data:
            return
        escaped = html.escape(data, quote=False)
        self.out.append(escaped)

    def finish(self) -> str:
        while self.stack:
            self.out.append(f"</{self.stack.pop()}>")
        return "".join(self.out).strip()


def sanitize_mathml_core(raw_html: str) -> str:
    """Sanitize raw MathML markup to a strict, style-free HTML5 MathML Core subset."""
    if not isinstance(raw_html, str) or not raw_html.strip():
        raise ValueError("Empty MathML input")
    parser = _MathMLSanitizer()
    parser.feed(raw_html)
    parser.close()
    cleaned = parser.finish()
    if not cleaned.startswith("<math display=") or not cleaned.endswith("</math>"):
        raise ValueError(f"Sanitized output does not form a valid <math> element: {cleaned[:80]!r}")
    return cleaned


def latex_sha256(latex: str) -> str:
    """Return canonical UTF-8 SHA-256 hex digest of a LaTeX governing-law string."""
    return hashlib.sha256(latex.encode("utf-8")).hexdigest()


def discover_mathml_folios() -> dict[str, str]:
    """Return {slug: governing_law_latex} across all pillar folio modules that opt in."""
    if str(ROOT / "tools") not in sys.path:
        sys.path.insert(0, str(ROOT / "tools"))
    found: dict[str, str] = {}
    for pillar in PILLAR_DIRS:
        pdir = FOLIOS_DIR / pillar
        if not pdir.is_dir():
            continue
        for py_path in sorted(pdir.glob("*.py")):
            if py_path.name == "__init__.py":
                continue
            mod_name = f"folios.{pillar}.{py_path.stem}"
            mod = importlib.import_module(mod_name)
            folio = getattr(mod, "FOLIO", None)
            slug = getattr(mod, "SLUG", None)
            if isinstance(folio, dict) and isinstance(slug, str) and folio.get("governing_law_latex"):
                found[slug] = str(folio["governing_law_latex"])
    return found


def load_cache(cache_path: Path = CACHE_PATH) -> dict[str, dict[str, str]]:
    """Read pre-rendered MathML cache JSON."""
    if not cache_path.is_file():
        return {}
    raw = json.loads(cache_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"Invalid MathML cache object in {cache_path}")
    return raw


def get_cached_mathml(slug: str, latex: str, cache_path: Path = CACHE_PATH) -> str:
    """Return verified, sanitized MathML Core markup for a folio's governing_law_latex."""
    cache = load_cache(cache_path)
    entry = cache.get(slug)
    if not isinstance(entry, dict):
        raise ValueError(
            f"Missing MathML cache entry for folio '{slug}'; run mathml_render.py --regenerate"
        )
    expected_hash = latex_sha256(latex)
    if entry.get("latex_sha256") != expected_hash or entry.get("latex") != latex:
        raise ValueError(
            f"Stale MathML cache entry for folio '{slug}'; run mathml_render.py --regenerate"
        )
    clauses = entry.get("clauses")
    if isinstance(clauses, list) and clauses:
        return " ".join(sanitize_mathml_core(str(c)) for c in clauses)
    return sanitize_mathml_core(entry.get("mathml", ""))


def regenerate_cache(cache_path: Path = CACHE_PATH) -> dict[str, dict[str, object]]:
    """Convert all opted-in folio governing_law_latex formulas to sanitized MathML Core."""
    try:
        from latex2mathml import converter as l2m_converter  # type: ignore[import-not-found]
    except ImportError as exc:
        raise RuntimeError(
            "latex2mathml is required for --regenerate (run with the math-audit venv Python)"
        ) from exc

    folios = discover_mathml_folios()
    out: dict[str, dict[str, object]] = {}
    for slug, latex in sorted(folios.items()):
        parts = [p.strip() for p in latex.split(r"\\") if p.strip()]
        clauses = [
            sanitize_mathml_core(l2m_converter.convert(part, display="block"))
            for part in parts
        ]
        joined = " ".join(clauses)
        out[slug] = {
            "latex": latex,
            "latex_sha256": latex_sha256(latex),
            "clauses": clauses,
            "mathml": joined,
            "generator": "latex2mathml",
        }
    cache_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def check_cache(cache_path: Path = CACHE_PATH) -> list[str]:
    """Stdlib-only check verifying cache completeness, SHA-256 parity, and sanitizer cleanliness."""
    errors: list[str] = []
    folios = discover_mathml_folios()
    try:
        cache = load_cache(cache_path)
    except Exception as exc:
        return [f"Cannot load cache {cache_path}: {exc}"]

    if not folios:
        errors.append("No folio modules define FOLIO['governing_law_latex']")
        return errors

    for slug, latex in sorted(folios.items()):
        if slug not in cache:
            errors.append(f"Missing cache entry for '{slug}'")
            continue
        try:
            get_cached_mathml(slug, latex, cache_path=cache_path)
        except Exception as exc:
            errors.append(f"Cache verification failed for '{slug}': {exc}")

    extra = sorted(set(cache.keys()) - set(folios.keys()))
    if extra:
        errors.append(f"Orphan MathML cache entries not in folios: {extra}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build-time MathML Core renderer & cache checker")
    parser.add_argument("--regenerate", action="store_true", help="Regenerate mathml_cache.json via latex2mathml")
    parser.add_argument("--check", action="store_true", help="Verify cache parity and sanitization using stdlib only")
    args = parser.parse_args(argv)

    if args.regenerate:
        cache = regenerate_cache()
        print(f"REGENERATED {len(cache)} MathML Core cache entry(ies) -> {CACHE_PATH.relative_to(ROOT)}")

    errors = check_cache()
    if errors:
        for err in errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1

    folios = discover_mathml_folios()
    print(f"PASS: MathML Core cache verified ({len(folios)} folios, stdlib sanitizer clean)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
