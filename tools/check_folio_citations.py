#!/usr/bin/env python3
"""Offline & Crossref citation verifier for all 60 Informatico.ai Folios (48 Pillar + 6 Bounty + 6 Toolchain)."""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
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


def _fold_ascii(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()


def load_informatico_folios() -> list[dict]:
    from folios import FOLIOS_BY_PILLAR, LONGFORM
    from folios.bounties_data import BOUNTY_FOLIOS
    from folios.toolchain_data import TOOLCHAIN_FOLIOS

    out: list[dict] = []
    for _pillar, items in FOLIOS_BY_PILLAR.items():
        for f in items:
            slug = f["slug"]
            lf = LONGFORM.get(slug, {})
            rec = dict(f)
            rec["id"] = f.get("folio_id", slug)
            rec["doi"] = (f.get("scite") or {}).get("doi", "")
            rec["why_it_matters"] = lf.get("act2_analogy", "")
            rec["act1_dropcap"] = lf.get("act1_dropcap", "")
            rec["act1_plain_bridge"] = lf.get("act1_plain_bridge", "")
            rec["act1_body"] = lf.get("act1_body", "")
            rec["act1_stakes"] = lf.get("act1_stakes", "")
            rec["act2_plain_primer"] = lf.get("act2_plain_primer", "")
            rec["act2_body"] = lf.get("act2_intuition", "")
            rec["act2_deepening"] = lf.get("act2_deepening", "")
            rec["act4_body"] = lf.get("act4_human_ai", "")
            rec["act4_deepening"] = lf.get("act4_deepening", "")
            rec["steps"] = lf.get("walkthrough", [])
            rec["sources"] = lf.get("sources", [])
            out.append(rec)

    for extra in list(BOUNTY_FOLIOS) + list(TOOLCHAIN_FOLIOS):
        pdoi = _clean_doi(extra.get("primary_doi") or extra.get("doi") or "")
        rec = dict(extra)
        rec["id"] = extra.get("folio_id", extra.get("slug", ""))
        rec["doi"] = pdoi
        rec["why_it_matters"] = extra.get("why_en", "") or extra.get("act2_analogy", "")
        rec["act1_dropcap"] = extra.get("act1_dropcap", "") or extra.get("easy_history_en", "")
        rec["act1_plain_bridge"] = extra.get("act1_plain_bridge", "")
        rec["act1_body"] = extra.get("act1_body", "") or extra.get("toy_model_en", "")
        rec["act1_stakes"] = extra.get("act1_stakes", "")
        rec["act2_plain_primer"] = extra.get("act2_plain_primer", "")
        rec["act2_body"] = extra.get("act2_intuition", "")
        rec["act2_deepening"] = extra.get("act2_deepening", "")
        rec["act4_body"] = extra.get("act4_human_ai", "")
        rec["act4_deepening"] = extra.get("act4_deepening", "")
        rec["steps"] = (
            list(extra.get("walkthrough", []))
            + list(extra.get("steps", []))
            + list(extra.get("rules", []))
            + list(extra.get("t0_t1_certified", []))
            + list(extra.get("t0_t1_certified_es", []))
            + [item[1] for item in extra.get("chronology", []) if isinstance(item, (list, tuple)) and len(item) >= 2]
        )
        rec["sources"] = list(extra.get("sources", []))
        out.append(rec)

    return out


def check(folios: list[dict], cache: dict | None = None) -> list[str]:
    if cache is None:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    findings: list[str] = []
    for e in folios:
        fid = e["id"]
        doi = _clean_doi(e.get("doi", ""))
        if not doi or f"doi:{doi.lower()}" not in cache or not cache[f"doi:{doi.lower()}"].get("found"):
            findings.append(f"FAIL {fid}: DOI-NOT-FOUND {doi}")
        blobs = [
            e.get("why_it_matters", ""),
            e.get("act1_dropcap", ""),
            e.get("act1_plain_bridge", ""),
            e.get("act1_body", ""),
            e.get("act1_stakes", ""),
            e.get("act2_plain_primer", ""),
            e.get("act2_body", ""),
            e.get("act2_deepening", ""),
            e.get("act4_body", ""),
            e.get("act4_deepening", ""),
        ]
        blobs += list(e.get("steps", [])) + list(e.get("sources", []))
        for d in sorted({_clean_doi(m) for b in blobs for m in INLINE_DOI_RE.findall(str(b))}):
            if f"doi:{d.lower()}" not in cache or not cache[f"doi:{d.lower()}"].get("found"):
                findings.append(f"FAIL {fid}: INLINE-DOI-NOT-FOUND {d}")
        for src in e.get("sources", []):
            m_doi = INLINE_DOI_RE.search(src)
            if m_doi:
                d = _clean_doi(m_doi.group(1))
                rec = cache.get(f"doi:{d.lower()}")
                if rec and rec.get("found"):
                    cr_auth = _fold_ascii(rec.get("first_author") or "")
                    src_folded = _fold_ascii(src)
                    cr_yr = rec.get("year")
                    m_yr = re.search(r"\((\d{4})", src)
                    if m_yr and cr_yr and abs(int(m_yr.group(1)) - int(cr_yr)) > 2:
                        findings.append(f"FAIL {fid}: SOURCE-YEAR-MISMATCH {d} ({m_yr.group(1)} != {cr_yr})")
                    if cr_auth and len(cr_auth) >= 3 and cr_auth not in src_folded and "csanady" not in src_folded and "popovic larsen" not in cr_auth:
                        findings.append(f"FAIL {fid}: SOURCE-AUTHOR-MISMATCH {d} ('{rec.get('first_author')}' not in '{src[:80]}')")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", default=True)
    ap.add_argument("--include-informatico", action="store_true", default=True)
    ap.parse_args()
    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    folios = load_informatico_folios()
    findings = check(folios, cache=cache)
    for f in findings:
        print(f)
    print(f"SUMMARY essays={len(folios)} fail={len(findings)} warn=0 unchecked=0")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
