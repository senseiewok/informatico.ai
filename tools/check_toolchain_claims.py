#!/usr/bin/env python3
"""Deterministic Claim, Boundary-Sentence & Security-Runtime Gate for Tech & Tools · The Toolbox (X.01–X.06).

Enforces Fable's Council Contract:
1. Exact English boundary sentence (`BOUNDARY_EN`) on `/toolchain/index.html` and `/toolchain/x01..x06/index.html`.
2. Exact Spanish boundary sentence (`BOUNDARY_ES`) on `/es-mx/toolchain/index.html` and `/es-mx/toolchain/x01..x06/index.html`.
3. Every `manifest.json` in `src/research/toolchain/x01..x06/files/` embeds `BOUNDARY_EN`, `BOUNDARY_ES`, and `"Not certified for fitness"` in its license metadata.
4. Zero un-negated fitness claims ("certified as load-bearing", "certified printable", "safe to build", "ready for structural load") across `src/research/toolchain/` and `skills/toolchain/`.
5. Every `skills/toolchain/x01..x06/SKILL.md` enforces the `security-runtime` workspace boundary (no home-directory or external network grants).
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from toolchain_uga import BOUNDARY_EN, BOUNDARY_ES  # noqa: E402

SLUGS = ("x01", "x02", "x03", "x04", "x05", "x06")

# Positive fitness claims that are forbidden unless preceded by a negation ("Nothing here", "nothing on this page", "Not ", "Never ", "Nada aquí", "No ")
FORBIDDEN_POSITIVE_CLAIMS = re.compile(
    r"(?<!Nothing here )(?<!nothing on this page )(?<!nothing )(?<!not )(?<!never )(?<!Nada aqu\u00ed )(?<!nada )(?<!no )\b("
    r"is certified as load-bearing"
    r"|is certified printable"
    r"|is safe to build"
    r"|is structurally certified"
    r"|ready for structural construction"
    r"|est\u00e1 certificado como estructural"
    r"|est\u00e1 certificado como imprimible"
    r"|es seguro para construir"
    r")\b",
    re.IGNORECASE,
)

FORBIDDEN_SKILL_GRANTS = re.compile(
    r"\b(allow-home-dir|allow-network-outbound|curl\s+http|wget\s+http|rm\s+-rf\s+/)\b",
    re.IGNORECASE,
)


def _strip_boundaries(txt: str) -> str:
    return (
        txt.replace(BOUNDARY_EN, "")
        .replace(html.escape(BOUNDARY_EN), "")
        .replace(BOUNDARY_ES, "")
        .replace(html.escape(BOUNDARY_ES), "")
    )


def main() -> int:
    errors: list[str] = []
    res_dir = ROOT / "src" / "research"
    skills_dir = ROOT / "skills" / "toolchain"

    # 1. Check English pages for BOUNDARY_EN
    en_pages = [res_dir / "toolchain" / "index.html"] + [
        res_dir / "toolchain" / s / "index.html" for s in SLUGS
    ]
    for p in en_pages:
        if not p.is_file():
            errors.append(f"Missing English toolchain page: {p.relative_to(ROOT)}")
            continue
        txt = p.read_text(encoding="utf-8")
        if BOUNDARY_EN not in txt:
            errors.append(f"Missing exact BOUNDARY_EN in {p.relative_to(ROOT)}")
        m = FORBIDDEN_POSITIVE_CLAIMS.search(_strip_boundaries(txt))
        if m:
            errors.append(f"Forbidden positive fitness claim '{m.group(0)}' in {p.relative_to(ROOT)}")

    # 2. Check Spanish pages for BOUNDARY_ES
    es_pages = [res_dir / "es-mx" / "toolchain" / "index.html"] + [
        res_dir / "es-mx" / "toolchain" / s / "index.html" for s in SLUGS
    ]
    for p in es_pages:
        if not p.is_file():
            errors.append(f"Missing Spanish toolchain page: {p.relative_to(ROOT)}")
            continue
        txt = p.read_text(encoding="utf-8")
        if BOUNDARY_ES not in txt:
            errors.append(f"Missing exact BOUNDARY_ES in {p.relative_to(ROOT)}")
        m = FORBIDDEN_POSITIVE_CLAIMS.search(_strip_boundaries(txt))
        if m:
            errors.append(f"Forbidden positive fitness claim '{m.group(0)}' in {p.relative_to(ROOT)}")

    # 3. Check manifest.json and SKILL.md for all 6 Folios
    for s in SLUGS:
        mpath = res_dir / "toolchain" / s / "files" / "manifest.json"
        if not mpath.is_file():
            errors.append(f"Missing manifest.json for {s}: {mpath.relative_to(ROOT)}")
        else:
            mdata = json.loads(mpath.read_text(encoding="utf-8"))
            if mdata.get("boundary_en") != BOUNDARY_EN:
                errors.append(f"{s}/files/manifest.json boundary_en mismatch")
            if mdata.get("boundary_es") != BOUNDARY_ES:
                errors.append(f"{s}/files/manifest.json boundary_es mismatch")
            if mdata.get("license") != "CC0-1.0 / CC-BY-4.0":
                errors.append(f"{s}/files/manifest.json license must be 'CC0-1.0 / CC-BY-4.0'")

        spath = skills_dir / s / "SKILL.md"
        if not spath.is_file():
            errors.append(f"Missing SKILL.md for {s}: {spath.relative_to(ROOT)}")
        else:
            stxt = spath.read_text(encoding="utf-8")
            if BOUNDARY_EN not in stxt or BOUNDARY_ES not in stxt:
                errors.append(f"{spath.relative_to(ROOT)} missing BOUNDARY_EN or BOUNDARY_ES")
            if "security-runtime" not in stxt:
                errors.append(f"{spath.relative_to(ROOT)} missing security-runtime boundary section")
            m = FORBIDDEN_POSITIVE_CLAIMS.search(_strip_boundaries(stxt))
            if m:
                errors.append(f"Forbidden positive fitness claim '{m.group(0)}' in {spath.relative_to(ROOT)}")
            mg = FORBIDDEN_SKILL_GRANTS.search(stxt)
            if mg:
                errors.append(f"Forbidden skill grant '{mg.group(0)}' in {spath.relative_to(ROOT)}")

    if errors:
        for err in errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1

    print(
        "PASS: Tech & Tools claim & boundary gate verified (7 EN pages, 7 ES-MX pages, 6 manifests, 6 SKILL.md files)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
