#!/usr/bin/env python3
"""Grounding guards: keep withdrawn references and unearned verdicts from coming back.

Two checks, both offline and deterministic:

1. Withdrawn references. DOIs, arXiv ids and repository URLs that grounding reviews found to point at the wrong
   paper, not to resolve, or not to exist. None may appear anywhere in the folio sources, the lab script or the
   generated pages, except inside an explicit withdrawal note (a sentence that says the reference was withdrawn,
   removed or not found).
2. Verdict language. The short strings a reader takes as a result (readout values, status badges, threshold
   labels and every string literal in the interactive lab script) may not claim a proof, a verification, a
   certification, a guarantee or an eradication, in any letter case. Headlines (titles, subtitles, dispatch,
   spec plates) may not claim a proof, a certification, a guarantee or an eradication either. Folios state model values and design targets; see the grounding
   reviews of 2026-11-13 and 2026-11-14.

Run: python tools/check_grounding_guards.py   (exit 1 on any finding)
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLIOS = ROOT / "tools" / "folios"
SOLVERS = ROOT / "src" / "modules" / "solvers.mjs"

# reference -> why it is withdrawn
WITHDRAWN_REFS = {
    "github.com/anthropics/theorem-riscv": "no public repository",
    "github.com/openai/formal-math-qrh": "no such repository (the result is in openai/math)",
    "github.com/openai/navier-stokes-formal": "no such repository (see openai/NavierStokesAndEuler)",
    "github.com/openai/erdos-unit-distance": "no such repository",
    "10.1126/science.adx2026": "does not resolve ('AlphaProof Nexus')",
    "10.1098/rspa.1954.0152": "a glow-discharge paper, not Prigogine",
    "10.1085/jgp.202012676": "a Shaker potassium-channel paper",
    "10.1016/j.jcf.2021.08.014": "a treatment-patterns paper, not a threshold source",
    "10.1016/j.jcf.2021.03.013": "steam disinfection of cutlery, not sink drains",
    "10.1016/0031-8914(64)90154-1": "does not resolve",
    "10.1038/s41563-020-00845-y": "does not resolve",
    "10.1146/annurev-fluid-010719-060144": "does not resolve",
    "arXiv:2405.10935": "unrelated paper (Guth-Maynard is arXiv:2405.20552)",
    "arxiv.org/abs/2405.10935": "unrelated paper (Guth-Maynard is arXiv:2405.20552)",
    "arxiv.org/abs/2501.16499": "a Schrodinger-map PDE paper, not Seed-Prover",
    "ETHIsFalse": "no such file in anthropics/formal-math (read 2026-11-14)",
    "EightSquare.lean": "no such file in anthropics/formal-math (read 2026-11-14)",
    "ETH Refutation": "a repository's unchecked claim, never a site headline",
    "Refutación ETH": "a repository's unchecked claim, never a site headline",
}
# A withdrawn reference may be named only in a sentence that says so.
WITHDRAWAL_CONTEXT = re.compile(
    r"withdrawn|removed|not publicly reachable|not found|no public|does not (?:resolve|exist)|did not resolve|"
    r"earlier editions?|printed here before|retirad|no se encontr|no era accesible|unverified|not checked|"
    r"no file of that name|not listed|was not found|withdraws?|did not exist|do(?:es)? not appear|file tree|"
    r"earlier versions?|no aparecen?|ediciones anteriores|no se encontr|consultad[oa]|reported only as|readme's statement", re.I)

# Verdict words that may not appear in result strings.
VERDICT = re.compile(
    r"\bQED\b|\b0 sorry|\bzero sorry|sorryAx|\bVERIFIED\b|\bCERTIFIED\b|\bGUARANTEED?\b|ERADICAT|"
    r"\bPROVEN\b|ZERO BIOFILM|PATHOGEN-FREE|STERILE|\bCURE[SD]?\b|VERIFICAD[OA]|CERTIFICAD[OA]|ERRADIC", re.I)
# Headlines (title, subtitle, dispatch, spec plate) may say "verified" when they describe someone else's proof, but
# never these.
HEADLINE_VERDICT = re.compile(r"\bQED\b|\b0 sorry|sorryAx|\bCERTIFIED\b|ERADICAT|PATHOGEN-FREE|ZERO BIOFILM|"
                              r"\bGUARANTEED?\b|ERRADIC|CERTIFICAD[OA]", re.I)
# Phrases that use a verdict word to say the opposite, and are therefore allowed.
VERDICT_OK = re.compile(r"NOT A PROOF|NOT VERIFIED|NOT CHECKED|NOT BUILT|UNVERIFIED|SIN VERIFICAR|NO VERIFICAD|"
                        r"SHA-256 VERIFIED|NOTHING VERIFIED|NOT (?:INDEPENDENTLY |TESTED OR )?(?:VERIFIED|CERTIFIED)|"
                        r"NOT A CERTIFIED", re.I)
# Lab strings that are HTML element ids or class names, not reader-facing text.
IDENTIFIER = re.compile(r"^[a-z0-9_-]+$")  # SHA-256: a checksum the verifier really compares
# Folio groups with their own label lint (timegravity: check_timegravity_labels.py) or no readouts.
PILLARS = ("architecture", "engineering", "physics", "math", "bounties", "toolchain")


def load(path: Path):
    spec = importlib.util.spec_from_file_location(f"g_{path.parent.name}_{path.stem}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def headline_strings(mod) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    folio = getattr(mod, "FOLIO", {}) or {}
    for key in ("title", "subtitle"):
        if folio.get(key):
            out.append((key, str(folio[key])))
    es = getattr(mod, "ES_TRANSLATION", {}) or {}
    for key in ("title_es", "subtitle_es"):
        if es.get(key):
            out.append((key, str(es[key])))
    for key, val in (getattr(mod, "DISPATCH", {}) or {}).items():
        out.append((f"DISPATCH.{key}", str(val)))
    for key, val in (folio.get("spec_plate") or {}).items():
        out.append((f"spec_plate.{key}", str(val)))
    return out


def verdict_strings(mod) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    folio = getattr(mod, "FOLIO", {}) or {}
    for i, r in enumerate(folio.get("readouts", [])):
        out.append((f"readouts[{i}].value", str(r.get("value", ""))))
        out.append((f"readouts[{i}].label", str(r.get("label", ""))))
    for key in ("status_badge", "kernel_verdict", "kernel_verdict_es"):
        if folio.get(key):
            out.append((key, str(folio[key])))
    dd = (getattr(mod, "LONGFORM_DATA", {}) or {}).get("distill_diagram", {}) or {}
    for key in ("threshold_pass", "threshold_fail", "threshold_title"):
        if dd.get(key):
            out.append((f"distill_diagram.{key}", str(dd[key])))
    return out


def sentences_with(text: str, needle: str, whole_line: bool = False) -> list[str]:
    """The context of each mention: its sentence, or (whole_line) the whole joined Python string field."""
    # Python sources wrap long strings across adjacent literals; join them so one field reads as one line.
    text = re.sub(r"['\"]\s*\n\s*['\"]", "", text)
    out = []
    for m in re.finditer(re.escape(needle), text):
        if whole_line:
            a = text.rfind("\n", 0, m.start()) + 1
            b = text.find("\n", m.end())
        else:
            a = max(text.rfind(". ", 0, m.start()), text.rfind("\n", 0, m.start()), 0)
            b = min([x for x in (text.find(". ", m.end()), text.find("\n", m.end())) if x != -1] or [len(text)])
        out.append(text[a:b if b != -1 else len(text)])
    return out


def s_line(text: str, needle: str) -> str:
    """The physical line holding the first mention (long generated lines fall back to sentence mode)."""
    i = text.lower().find(needle.lower())
    end = text.find("\n", i)
    return text[text.rfind("\n", 0, i) + 1: end if end != -1 else len(text)]


def main() -> int:
    findings: list[str] = []
    sources = sorted(FOLIOS.rglob("*.py")) + [SOLVERS, ROOT / "tools" / "folio_puzzles_data.py"]
    pages = sorted((ROOT / "src").rglob("*.html"))
    docs = ([ROOT / "README.md"] + sorted((ROOT / "bounties").glob("*.md")) + sorted((ROOT / "skills").rglob("SKILL.md"))
            + sorted((ROOT / "src" / "data").glob("*.json")) + sorted((ROOT / "src" / "data").glob("*.md"))
            + [ROOT / "src" / "llms.txt"])
    for path in sources + pages + [d for d in docs if d.is_file()]:
        text = path.read_text(encoding="utf-8", errors="replace")
        # A council ledger is a historical record of proposals; it may name withdrawn references if it carries a
        # grounding note saying so.
        if path.name.endswith("council_ledger.json") and "grounding_note" in text:
            continue
        for ref, why in WITHDRAWN_REFS.items():
            if ref.lower() not in text.lower():
                continue
            for s in sentences_with(text.lower(), ref.lower(), whole_line=path.suffix in (".py", ".json") or (path.suffix == ".html" and len(s_line(text, ref)) < 4000)):
                if not WITHDRAWAL_CONTEXT.search(s):
                    findings.append(f"WITHDRAWN-REF {path.relative_to(ROOT).as_posix()}: {ref} ({why})")
                    break
    for path in sorted(p for pillar in PILLARS for p in (FOLIOS / pillar).glob("*.py")):
        if path.name.startswith("_"):
            continue
        try:
            mod = load(path)
        except Exception as exc:  # a folio that does not import is a finding too
            findings.append(f"IMPORT {path.relative_to(ROOT).as_posix()}: {exc}")
            continue
        for where, s in headline_strings(mod):
            if HEADLINE_VERDICT.search(s) and not VERDICT_OK.search(s):
                findings.append(f"HEADLINE {path.relative_to(ROOT).as_posix()} {where}: {s[:120]!r}")
        for where, s in verdict_strings(mod):
            if VERDICT.search(s) and not VERDICT_OK.search(s):
                findings.append(f"VERDICT {path.relative_to(ROOT).as_posix()} {where}: {s!r}")
    lab = SOLVERS.read_text(encoding="utf-8")
    for m in re.finditer(r"([\"'`])((?:\\.|(?!\1).)*)\1", lab):
        s = m.group(2)
        if VERDICT.search(s) and not VERDICT_OK.search(s) and not IDENTIFIER.match(s):
            line = lab.count("\n", 0, m.start()) + 1
            findings.append(f"VERDICT src/modules/solvers.mjs:{line}: {s[:120]!r}")
    for f in findings:
        print(f"FAIL {f}")
    print(f"SUMMARY grounding guards: {len(findings)} finding(s); {len(WITHDRAWN_REFS)} withdrawn references guarded")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
