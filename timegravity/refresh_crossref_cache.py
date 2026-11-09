#!/usr/bin/env python3
"""Add the Time & Gravity ledger DOIs to the site's offline Crossref cache (data/folio-citations.cache.json).

Standard library only. Fetches https://api.crossref.org/works/<doi> for every ledger DOI that the cache does not
hold yet and writes an entry in the cache's existing shape: fetched, first_author, found, journal, title, year.
Nothing personal is sent: the User-Agent names the repository, not a person. Rows already cached are left alone
unless --force is given. Exit 1 if any DOI could not be resolved, so a typo never silently enters the ledger.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "timegravity" / "ledger.json"
CACHE = ROOT / "data" / "folio-citations.cache.json"
USER_AGENT = "informatico.ai-timegravity-ledger/1.0 (https://github.com/senseiewok/informatico.ai)"
DOI_RE = re.compile(r"^10\.[0-9]{4,9}/[^\s?#]+$")


def fetch_datacite(doi: str) -> dict:
    """arXiv DOIs (10.48550/...) are registered with DataCite, not Crossref; same cache shape, source noted."""
    url = "https://api.datacite.org/dois/" + urllib.request.quote(doi, safe="/()")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.api+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        attrs = json.load(resp)["data"]["attributes"]
    creators = attrs.get("creators") or []
    first = (creators[0].get("familyName") or creators[0].get("name") or "").split(",")[0] if creators else ""
    titles = attrs.get("titles") or []
    return {
        "fetched": dt.date.today().isoformat(),
        "first_author": first,
        "found": True,
        "journal": attrs.get("publisher") or "arXiv",
        "title": titles[0].get("title", "") if titles else "",
        "year": int(attrs.get("publicationYear") or 0) or None,
        "registry": "DataCite (preprint)",
    }


def fetch(doi: str) -> dict:
    if not DOI_RE.match(doi) or ".." in doi:
        raise ValueError(f"Malformed or unsafe DOI: {doi!r}")
    url = "https://api.crossref.org/works/" + urllib.request.quote(doi, safe="/()")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        msg = json.load(resp)["message"]
    authors = msg.get("author") or []
    first = (authors[0].get("family") or authors[0].get("name") or "") if authors else ""
    year = None
    for key in ("published-print", "published-online", "issued", "created"):
        parts = (msg.get(key) or {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            year = int(parts[0][0])
            break
    titles = msg.get("title") or []
    containers = msg.get("container-title") or []
    return {
        "fetched": dt.date.today().isoformat(),
        "first_author": first,
        "found": True,
        "journal": containers[0] if containers else "",
        "title": titles[0] if titles else "",
        "year": year,
    }


def fetch_scite_tally(doi: str) -> dict:
    """Scite's public, unauthenticated tallies endpoint (zero quota, no key; see cf-evidence-loop's scite provider).

    Stored in the cache's existing `scite:<doi>` shape so the site renders it like the OSS radar does. The counts are
    [observed: Scite ML citation classification]: a classifier's output, never a substitute for reading the source.
    """
    if not DOI_RE.match(doi) or ".." in doi:
        raise ValueError(f"Malformed or unsafe DOI: {doi!r}")
    url = "https://api.scite.ai/tallies/" + urllib.request.quote(doi, safe="/()")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if not isinstance(data, dict) or not data.get("doi"):
        raise ValueError(f"unexpected Scite tally shape: {str(data)[:120]}")
    contrasting = int(data.get("contradicting", data.get("contrasting", 0)) or 0)
    return {
        "citing_publications": int(data.get("citingPublications", 0) or 0),
        "contrasting": contrasting,
        "fetched": dt.date.today().isoformat(),
        "found": True,
        "mentioning": int(data.get("mentioning", 0) or 0),
        "retracted": bool(data.get("retracted", False)),
        "supporting": int(data.get("supporting", 0) or 0),
        "total_smart_citations": int(data.get("total", 0) or 0),
        "unclassified": int(data.get("unclassified", 0) or 0),
        "classification_provenance": "Scite ML citation classification",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--force", action="store_true", help="re-fetch rows that are already cached")
    ap.add_argument("--dry-run", action="store_true", help="list what would be fetched and exit")
    ap.add_argument("--scite", action="store_true", help="also fetch Scite public citation tallies (scite:<doi> rows)")
    args = ap.parse_args()

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    todo = []
    for row in ledger["rows"]:
        key = "doi:" + row["doi"].lower()
        if args.force or key not in cache or not cache[key].get("found"):
            todo.append((key, row["doi"]))
        if args.scite:
            skey = "scite:" + row["doi"].lower()
            if args.force or skey not in cache or not cache[skey].get("found"):
                todo.append((skey, row["doi"]))
    if args.dry_run:
        for key, doi in todo:
            print("would fetch", key)
        return 0

    failures = 0
    for key, doi in todo:
        try:
            if key.startswith("scite:"):
                cache[key] = fetch_scite_tally(doi)
                t = cache[key]
                print(f"OK   scite {doi}: {t['citing_publications']} citing · {t['supporting']} supporting · {t['contrasting']} contrasting · {t['mentioning']} mentioning")
            else:
                cache[key] = fetch_datacite(doi) if doi.lower().startswith("10.48550/") else fetch(doi)
                print(f"OK   {doi}: {cache[key]['first_author']} ({cache[key]['year']}) {cache[key]['title'][:70]}")
            time.sleep(1.2)  # polite pacing for the public endpoints
        except (urllib.error.URLError, urllib.error.HTTPError, KeyError, ValueError, TimeoutError) as exc:
            failures += 1
            print(f"FAIL {key}: {exc}", file=sys.stderr)

    if todo and not failures:
        # Keep the cache's own formatting (indent=1, sorted keys, CRLF) so the diff shows only the new rows.
        ordered = {k: cache[k] for k in sorted(cache)}
        text = json.dumps(ordered, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
        CACHE.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))
        print(f"PASS: cache holds {len(ordered)} DOIs; {len(todo)} added or refreshed.")
    elif not todo:
        print("PASS: every ledger DOI is already cached.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
