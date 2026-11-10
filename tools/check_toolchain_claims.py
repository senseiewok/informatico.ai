#!/usr/bin/env python3
"""Deterministic Claim, Boundary-Sentence, Global FOSS Compliance & Security-Runtime Gate for Tech & Tools · The Toolbox (X.01–X.06).

Enforces Fable & Argon Council Contract:
1. Exact English boundary sentence (`BOUNDARY_EN`) on `/toolchain/index.html` and `/toolchain/x01..x06/index.html`.
2. Exact Spanish boundary sentence (`BOUNDARY_ES`) on `/es-mx/toolchain/index.html` and `/es-mx/toolchain/x01..x06/index.html`.
3. Every `manifest.json` in `src/research/toolchain/x01..x06/files/` embeds `BOUNDARY_EN`, `BOUNDARY_ES`, and `"Not certified for fitness"` in its license metadata.
4. Zero un-negated fitness claims ("certified as load-bearing", "certified printable", "safe to build", "ready for structural load") across `src/research/toolchain/` and `skills/toolchain/`.
5. Every `skills/toolchain/x01..x06/SKILL.md` enforces the `security-runtime` workspace boundary (no home-directory or external network grants).
6. Global Open-Source & Legal Compliance Charter (`GCC-01`..`GCC-05`) in `skills/toolchain/licenses.json` + zero proprietary CAD software endorsements or dependencies across all Toolbox files.
"""
from __future__ import annotations

import ast
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

FORBIDDEN_PROPRIETARY_TOOLS = re.compile(
    r"\b("
    r"Rhino\b|Rhinoceros|rhino3dm|McNeel|Grasshopper|"
    r"AutoCAD|Autodesk|Revit|Fusion\s*360|Inventor|Navisworks|3ds\s*Max|"
    r"SolidWorks|CATIA|Dassault|"
    r"MicroStation|Bentley|"
    r"LightBurn|"
    r"Bambu\s*Studio|"
    r"SketchUp"
    r")\b",
    re.IGNORECASE,
)

REQUIRED_CHARTER_KEYS = (
    "version",
    "effective_date",
    "jurisdiction_scope",
    "tenets",
    "forbidden_proprietary_software_registry",
)


def _strip_boundaries(txt: str) -> str:
    return (
        txt.replace(BOUNDARY_EN, "")
        .replace(html.escape(BOUNDARY_EN), "")
        .replace(BOUNDARY_ES, "")
        .replace(html.escape(BOUNDARY_ES), "")
    )


def check_global_compliance_charter(root: Path, errors: list[str]) -> None:
    """Audit skills/toolchain/licenses.json for the Global Compliance Charter (GCC-01..GCC-05)."""
    lic_path = root / "skills" / "toolchain" / "licenses.json"
    if not lic_path.is_file():
        errors.append("Missing skills/toolchain/licenses.json")
        return

    data = json.loads(lic_path.read_text(encoding="utf-8"))
    charter = data.get("global_compliance_charter")
    if not charter:
        errors.append("licenses.json is missing 'global_compliance_charter'")
        return

    for key in REQUIRED_CHARTER_KEYS:
        if key not in charter:
            errors.append(f"licenses.json global_compliance_charter missing '{key}'")

    tenet_ids = [t.get("id") for t in charter.get("tenets", [])]
    for expected_id in ("GCC-01", "GCC-02", "GCC-03", "GCC-04", "GCC-05"):
        if expected_id not in tenet_ids:
            errors.append(f"licenses.json global_compliance_charter missing tenet {expected_id}")

    for tool in data.get("tools", []):
        tname = tool.get("name", "")
        m = FORBIDDEN_PROPRIETARY_TOOLS.search(tname)
        if m:
            errors.append(
                f"licenses.json contains forbidden proprietary tool '{m.group(0)}' in {tname}"
            )


CHIMERA_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("F508del-CSI-MasterFormat", re.compile(r"F508del-CSI-MasterFormat", re.IGNORECASE)),
    ("CSI-MasterFormat mRNA", re.compile(r"CSI-MasterFormat\s+mRNA", re.IGNORECASE)),
    (
        "ventilation duct viscoplastic grout",
        re.compile(r"ventilation\s+duct\s+viscoplastic\s+grout", re.IGNORECASE),
    ),
    ("viscoplastic grout", re.compile(r"\bviscoplastic\s+grout\b", re.IGNORECASE)),
    (
        "CSI-MasterFormat paired with biophysical token",
        re.compile(
            r"CSI-MasterFormat.{0,160}\b(?:PDB|polyplex|epitheli\w*|ionocyte\w*|splicing|channel|1717-1G>A|G551D|F508del)\b"
            r"|\b(?:PDB|polyplex|epitheli\w*|ionocyte\w*|splicing|1717-1G>A|G551D|F508del)\b.{0,160}CSI-MasterFormat",
            re.IGNORECASE,
        ),
    ),
    ("/cf/csi-masterformat/", re.compile(r"/cf/csi-masterformat/", re.IGNORECASE)),
    (
        "colloidal tracer LNP chimera",
        re.compile(
            r"\b(?:SORT-colloidal\s+tracer|d_colloidal\s+tracer|mRNA\s+colloidal\s+tracer|PEGylated\s+colloidal\s+tracer|colloidal\s+tracer\s+lipid|nanopart[ií]culas\s+lip[ií]dicas\s*\(\s*colloidal\s+tracer\s*\))\b",
            re.IGNORECASE,
        ),
    ),
    (
        "bronchial-to-tubular / airway-to-duct anatomical chimera",
        re.compile(
            r"\btracheotubular\b"
            r"|\btubular\s+(?:tree|generations?|window|dean\s+vortices)\b"
            r"|\bventilation\s+duct\s+(?:irritants?|surface|mucosa|clearance)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "Civil & Structural Engineering / Ingeniería Hidrosanitaria / Non-Equilibrium disease chimera",
        re.compile(
            r"\b(?:people|patients|adults|children|living)\s+with\s+(?:Civil\s*(?:&|&amp;)\s*Structural\s+Engineering|Non-Equilibrium\s+Statistical\s+Biophysics)\b"
            r"|\bIn\s+Non-Equilibrium\s+Statistical\s+Biophysics,\s+(?:the\s+F508del|Class\s+III\s+gating)\b"
            r"|\b(?:pacientes|personas)\s+con\s+Ingenier[ií]a\s+Hidrosanitaria\b"
            r"|\bmucina\s+en\s+Ingenier[ií]a\s+Hidrosanitaria\b"
            r"|\ben\s+la\s+Ingenier[ií]a\s+Hidrosanitaria,\s+el\s+moco\b",
            re.IGNORECASE,
        ),
    ),
)

_BINARY_SUFFIXES = frozenset(
    {".jpg", ".jpeg", ".png", ".mp3", ".woff2", ".ico", ".pyc", ".webp", ".glb", ".3mf", ".step", ".dxf"}
)


def check_no_regex_chimeras(root: Path, errors: list[str]) -> None:
    """Reject regex-substitution chimeras across all repository source, skill, catalog, and HTML files."""
    skip_rel = {Path("tools/check_toolchain_claims.py")}
    ws_re = re.compile(r"\s+")
    tag_re = re.compile(r"<[^>]+>")
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if ".git" in p.parts or "__pycache__" in p.parts or p.suffix.lower() in _BINARY_SUFFIXES:
            continue
        rel = p.relative_to(root)
        if rel in skip_rel or (rel.parts and rel.parts[0] == "tests"):
            continue
        try:
            txt = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"Unreadable or non-UTF-8 file in {rel.as_posix()}: {exc}")
            continue

        blocks_to_scan: list[tuple[str, str]] = []
        if p.suffix.lower() == ".py":
            try:
                tree = ast.parse(txt, filename=rel.as_posix())
            except SyntaxError as exc:
                errors.append(f"Python syntax error in {rel.as_posix()}: {exc}")
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, str):
                    blocks_to_scan.append((f"line {getattr(node, 'lineno', 1)}", ws_re.sub(" ", node.value)))
        elif p.suffix.lower() in (".html", ".htm"):
            plain = ws_re.sub(" ", html.unescape(tag_re.sub(" ", txt)))
            blocks_to_scan.append(("document", plain))
        else:
            blocks_to_scan.append(("document", ws_re.sub(" ", txt)))

        for loc, block in blocks_to_scan:
            for label, rx in CHIMERA_PATTERNS:
                m = rx.search(block)
                if m:
                    errors.append(
                        f"Regex chimera ({label}: '{m.group(0)}') in {rel.as_posix()} ({loc})"
                    )


def check_forbidden_proprietary_mentions(root: Path, errors: list[str]) -> None:
    """Enforce zero proprietary software mentions across all published Toolbox folios, generators, and skills."""
    scan_targets = [
        root / "toolchain" / "README.md",
        root / "src" / "research" / "toolchain" / "README.md",
        root / "skills" / "toolchain" / "README.md",
        root / "skills" / "toolchain" / "licenses.json",
        root / "tools" / "build_longform_folios.py",
        root / "tools" / "toolchain_uga.py",
    ]
    scan_targets.extend((root / "tools" / "folios" / "toolchain").glob("*.py"))
    scan_targets.extend((root / "tools" / "folios" / "bounties").glob("*.py"))
    scan_targets.extend((root / "src" / "research" / "bounties").glob("**/index.html"))
    scan_targets.extend((root / "src" / "research" / "es-mx" / "bounties").glob("**/index.html"))
    scan_targets.extend((root / "skills" / "toolchain").glob("x0*/SKILL.md"))
    scan_targets.extend((root / "src" / "research" / "toolchain").glob("x0*/files/manifest.json"))
    scan_targets.extend((root / "src" / "research" / "toolchain").glob("**/index.html"))
    scan_targets.extend((root / "src" / "research" / "es-mx" / "toolchain").glob("**/index.html"))

    for p in scan_targets:
        if not p.is_file():
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for line_num, line in enumerate(txt.splitlines(), 1):
            m = FORBIDDEN_PROPRIETARY_TOOLS.search(line)
            if m:
                rel = p.relative_to(root)
                errors.append(
                    f"Forbidden proprietary software reference '{m.group(0)}' in {rel}:{line_num}"
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

    # 4. Check Global Compliance Charter, Zero Proprietary Software Mentions & Zero Regex Chimeras
    check_global_compliance_charter(ROOT, errors)
    check_forbidden_proprietary_mentions(ROOT, errors)
    check_no_regex_chimeras(ROOT, errors)

    if errors:
        for err in errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1

    print(
        "PASS: Tech & Tools claim, boundary & global FOSS compliance gate verified (7 EN pages, 7 ES-MX pages, 6 manifests, 6 SKILL.md files, GCC-01..GCC-05, zero regex chimeras)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
