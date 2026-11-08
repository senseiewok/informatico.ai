#!/usr/bin/env python3
"""Offline & Crossref citation verifier for the 48 Informatico.ai Folios (tools/folios/<pillar>/<slug>.py)."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
CACHE = ROOT / "data" / "folio-citations.cache.json"
INLINE_DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s,;\"'\]]+)")


def load_informatico_folios() -> list[dict]:
    from folios import FOLIOS_BY_PILLAR, LONGFORM
    new_folios, longform_data = FOLIOS_BY_PILLAR, LONGFORM
    out: list[dict] = []
    for pillar, items in new_folios.items():
        for f in items:
            slug = f["slug"]
            lf = longform_data.get(slug, {})
            rec = dict(f)
            rec["id"] = f.get("folio_id", slug)
            rec["doi"] = (f.get("scite") or {}).get("doi", "")
            rec["why_it_matters"] = lf.get("act2_analogy", "")
            rec["act1_body"] = lf.get("act1_body", "")
            rec["act2_body"] = lf.get("act2_intuition", "")
            rec["act4_body"] = lf.get("act4_human_ai", "")
            rec["steps"] = lf.get("walkthrough", [])
            rec["sources"] = lf.get("sources", [])
            out.append(rec)
    return out


def check(folios: list[dict]) -> list[str]:
    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    findings: list[str] = []
    for e in folios:
        fid = e["id"]
        doi = e.get("doi", "").rstrip(".)]")
        if not doi or f"doi:{doi.lower()}" not in cache or not cache[f"doi:{doi.lower()}"].get("found"):
            findings.append(f"FAIL {fid}: DOI-NOT-FOUND {doi}")
        blobs = [e.get("why_it_matters", ""), e.get("act1_body", ""), e.get("act2_body", ""), e.get("act4_body", "")]
        blobs += list(e.get("steps", [])) + list(e.get("sources", []))
        for d in sorted({m.rstrip(".)];,:") for b in blobs for m in INLINE_DOI_RE.findall(str(b))}):
            if f"doi:{d.lower()}" not in cache or not cache[f"doi:{d.lower()}"].get("found"):
                findings.append(f"FAIL {fid}: INLINE-DOI-NOT-FOUND {d}")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", default=True)
    ap.add_argument("--include-informatico", action="store_true", default=True)
    ap.parse_args()
    folios = load_informatico_folios()
    findings = check(folios)
    for f in findings:
        print(f)
    print(f"SUMMARY essays={len(folios)} fail={len(findings)} warn=0 unchecked=0")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
