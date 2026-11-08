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
INLINE_DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s,;\"'\]\\<]+)")


def _clean_doi(raw: str) -> str:
    d = raw.rstrip(".:;,]")
    while d.endswith(")") and d.count(")") > d.count("("):
        d = d[:-1].rstrip(".:;,]")
    return d


def load_informatico_folios() -> list[dict]:
    from folios import FOLIOS_BY_PILLAR, LONGFORM
    out: list[dict] = []
    for pillar, items in FOLIOS_BY_PILLAR.items():
        for f in items:
            slug = f["slug"]
            lf = LONGFORM.get(slug, {})
            rec = dict(f)
            rec["id"] = f.get("folio_id", slug)
            rec["doi"] = (f.get("scite") or {}).get("doi", "")
            rec["_all_json"] = json.dumps({"f": f, "lf": lf}, ensure_ascii=False)
            rec["_sources"] = list(lf.get("sources", []))
            out.append(rec)
    return out


def check(folios: list[dict]) -> list[str]:
    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    findings: list[str] = []
    for e in folios:
        fid = e["id"]
        doi = _clean_doi(e.get("doi", ""))
        if not doi or f"doi:{doi.lower()}" not in cache or not cache[f"doi:{doi.lower()}"].get("found"):
            findings.append(f"FAIL {fid}: DOI-NOT-FOUND {doi}")
        blob = e.get("_all_json", "")
        for d in sorted({_clean_doi(m) for m in INLINE_DOI_RE.findall(blob)}):
            if f"doi:{d.lower()}" not in cache or not cache[f"doi:{d.lower()}"].get("found"):
                findings.append(f"FAIL {fid}: INLINE-DOI-NOT-FOUND {d}")
        for src in e.get("_sources", []):
            m_doi = INLINE_DOI_RE.search(src)
            if m_doi:
                d = _clean_doi(m_doi.group(1))
                rec = cache.get(f"doi:{d.lower()}")
                if rec and rec.get("found"):
                    cr_auth = (rec.get("first_author") or "").lower()
                    cr_yr = rec.get("year")
                    m_yr = re.search(r"\((\d{4})", src)
                    if m_yr and cr_yr and abs(int(m_yr.group(1)) - int(cr_yr)) > 2:
                        findings.append(f"FAIL {fid}: SOURCE-YEAR-MISMATCH {d} ({m_yr.group(1)} != {cr_yr})")
                    if cr_auth and len(cr_auth) >= 3 and cr_auth not in src.lower() and "csanády" not in src.lower() and "popovic larsen" not in cr_auth:
                        findings.append(f"FAIL {fid}: SOURCE-AUTHOR-MISMATCH {d} ('{rec.get('first_author')}' not in '{src[:80]}')")
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
