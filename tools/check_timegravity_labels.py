#!/usr/bin/env python3
"""Ledger-driven claim-label lint for the Time & Gravity track (standard library only).

A claim on a T page is a span: <span class="tg-claim" data-tg-label="MEASURED" data-tg-ledger="T01-A,T01-B"
[data-tg-parent="T01-A"]>...</span>. Transitions, questions and definitions carry no span. This lint checks the
mechanics; a human checklist decides the label itself.

Rules (council contract, 2026-11-08):
  1. MEASURED needs at least two supporting rows from different collaborations with peer-reviewed DOIs.
  2. BOUND is for exclusion limits: at least one peer-reviewed row whose own label is BOUND.
  3. DERIVED names a parent row (data-tg-parent) whose ledger label is MEASURED.
  4. A row younger than 24 months (conservatively: published in this or the previous calendar year) or a preprint
     never supports MEASURED, DERIVED or BOUND; such claims cap at SINGLE RESULT or PROPOSED unless other rows carry them.
  5. SINGLE RESULT needs a peer-reviewed row; preprints never rise above PROPOSED; press rows back nothing.
  6. Every DOI resolves in data/folio-citations.cache.json (the offline Crossref cache).
  7. English and es-MX pages carry identical label sequences.
  8. The build fails once any row's review_by date has passed.
  9. Banned phrases in both languages are a cheap backstop; the hub-only sentence appears on no other page, and at
     most once per language on the hub.
 10. The hub carries zero claim spans; every T page prints the fixed boundary line; every claim page carries the
     AI-contribution line.

--planted-defect flips the first SINGLE RESULT claim upward to MEASURED in memory; the lint must then fail (exit 1,
FAIL on stderr). The normal run performs that flip internally as a self-test and reports REJECTED_AS_EXPECTED.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from folios.timegravity import (  # noqa: E402
    BANNED_EVERYWHERE,
    BOUNDARY_EN,
    BOUNDARY_ES,
    HUB_ONLY_PHRASES,
    LABEL_RANK,
    LABELS,
    PAGES,
)

RESEARCH = ROOT / "src" / "research"
LEDGER_PATH = ROOT / "timegravity" / "ledger.json"
CACHE_PATH = ROOT / "data" / "folio-citations.cache.json"
KINDS = ("peer-reviewed", "preprint", "review", "press")
VOID_TAGS = frozenset({"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"})
ID_RE = re.compile(r"^T[0-9]{2}-[A-Z0-9]+$")
DOI_RE = re.compile(r"^10\.[0-9]{4,9}/\S+$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


class _Claims(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.claims: list[dict] = []
        self.text: list[str] = []
        self._depth = 0
        self._cur: dict | None = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self._cur is not None and tag.lower() not in VOID_TAGS:
            self._depth += 1
        if "tg-claim" in (a.get("class") or "").split():
            self._cur = {
                "label": a.get("data-tg-label", ""),
                "ids": [x.strip() for x in (a.get("data-tg-ledger") or "").split(",") if x.strip()],
                "parent": a.get("data-tg-parent"),
                "text": "",
            }
            self._depth = 0

    def handle_endtag(self, tag):
        if self._cur is not None:
            if self._depth == 0:
                self.claims.append(self._cur)
                self._cur = None
            else:
                self._depth -= 1

    def handle_data(self, data):
        self.text.append(data)
        if self._cur is not None:
            self._cur["text"] += data


def parse_page(path: Path) -> tuple[list[dict], str, str]:
    raw = path.read_text(encoding="utf-8")
    p = _Claims()
    p.feed(raw)
    p.close()
    return p.claims, raw, " ".join(p.text)


def is_young(row: dict, today: dt.date) -> bool:
    return today.year - int(row["year"]) < 2


def check_ledger(ledger: dict, cache: dict, today: dt.date, errors: list[str]) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for row in ledger.get("rows", []):
        rid = row.get("id", "<missing id>")
        for key in ("id", "label", "doi", "year", "collaboration", "kind", "review_by"):
            if key not in row:
                errors.append(f"ledger {rid}: missing field '{key}'")
        if rid in rows:
            errors.append(f"ledger {rid}: duplicate id")
        if not ID_RE.match(str(rid)):
            errors.append(f"ledger {rid}: id does not match T##-TAG")
        if row.get("label") not in LABELS:
            errors.append(f"ledger {rid}: label {row.get('label')!r} is not one of {LABELS}")
        if row.get("kind") not in KINDS:
            errors.append(f"ledger {rid}: kind {row.get('kind')!r} is not one of {KINDS}")
        doi = str(row.get("doi", ""))
        if not DOI_RE.match(doi):
            errors.append(f"ledger {rid}: malformed DOI {doi!r}")
        if doi.lower().startswith(("http", "www")):
            errors.append(f"ledger {rid}: a URL is not a DOI")
        rec = cache.get("doi:" + doi.lower())
        if not rec or not rec.get("found"):
            errors.append(f"ledger {rid}: DOI {doi} does not resolve in the offline Crossref cache")
        elif rec.get("year") and abs(int(rec["year"]) - int(row.get("year", 0))) > 1:
            errors.append(f"ledger {rid}: year {row.get('year')} disagrees with Crossref {rec['year']}")
        # Evidence-synthesis habit: Scite citation polarity is a WARN, never a verdict (the checklist says what to do).
        sc = cache.get("scite:" + doi.lower())
        if sc and sc.get("found"):
            if sc.get("retracted"):
                errors.append(f"ledger {rid}: Scite marks DOI {doi} as retracted; a retracted row cannot back a claim")
            if int(sc.get("contrasting", 0)) > int(sc.get("supporting", 0)):
                WARNINGS.append(
                    f"ledger {rid}: Scite shows more contrasting ({sc.get('contrasting')}) than supporting ({sc.get('supporting')}) "
                    "citation statements [observed: Scite ML citation classification]; re-read three contrasting statements before keeping the label"
                )
        rb = str(row.get("review_by", ""))
        if not DATE_RE.match(rb):
            errors.append(f"ledger {rid}: review_by {rb!r} is not YYYY-MM-DD")
        elif dt.date.fromisoformat(rb) < today:
            errors.append(f"ledger {rid}: review_by {rb} has passed; reread the source and renew the row")
        if row.get("kind") == "press":
            errors.append(f"ledger {rid}: press rows cannot enter the ledger as backing for any claim")
        if row.get("kind") == "preprint" and LABEL_RANK.get(row.get("label", ""), 0) > LABEL_RANK["PROPOSED"]:
            errors.append(f"ledger {rid}: a preprint row cannot carry a label above PROPOSED")
        rows[rid] = row
    return rows


def check_claim(page: str, idx: int, claim: dict, rows: dict[str, dict], today: dt.date, errors: list[str]) -> None:
    where = f"{page} claim #{idx + 1} [{claim['label']}] \"{claim['text'][:60]}...\""
    label = claim["label"]
    if label not in LABELS:
        errors.append(f"{where}: unknown label {label!r}")
        return
    if not claim["ids"]:
        errors.append(f"{where}: no ledger id")
        return
    cited = []
    for rid in claim["ids"]:
        if rid not in rows:
            errors.append(f"{where}: ledger id {rid} not in ledger")
        else:
            cited.append(rows[rid])
    if not cited:
        return
    if any(r["kind"] == "press" for r in cited):
        errors.append(f"{where}: a press row cannot back a claim")
    rank = LABEL_RANK[label]
    mature = [r for r in cited if r["kind"] in ("peer-reviewed", "review") and not is_young(r, today)]
    supporting = [r for r in mature if LABEL_RANK[r["label"]] >= rank]
    if label == "MEASURED":
        collabs = {r["collaboration"] for r in supporting if r["kind"] == "peer-reviewed"}
        if len(collabs) < 2:
            errors.append(
                f"{where}: MEASURED needs >= 2 mature peer-reviewed rows from different collaborations "
                f"(found {len(collabs)}); cap at SINGLE RESULT"
            )
    elif label == "BOUND":
        if not any(r["label"] == "BOUND" and r["kind"] == "peer-reviewed" for r in mature):
            errors.append(f"{where}: BOUND needs a mature peer-reviewed exclusion-limit row (ledger label BOUND)")
    elif label == "DERIVED":
        parent = claim.get("parent")
        if not parent:
            errors.append(f"{where}: DERIVED must name a parent MEASURED row (data-tg-parent)")
        elif parent not in rows:
            errors.append(f"{where}: parent {parent} not in ledger")
        elif rows[parent]["label"] != "MEASURED":
            errors.append(f"{where}: parent {parent} is labelled {rows[parent]['label']}, not MEASURED")
        elif rows[parent]["kind"] != "peer-reviewed" or is_young(rows[parent], today):
            errors.append(f"{where}: parent {parent} must be a mature peer-reviewed MEASURED row")
        elif parent not in claim["ids"]:
            errors.append(f"{where}: parent {parent} must also be cited in data-tg-ledger")
        deriv_rows = [r for r in cited if r["id"] != parent]
        if not deriv_rows or not any(
            r["kind"] in ("peer-reviewed", "review")
            and not is_young(r, today)
            and LABEL_RANK[r["label"]] >= LABEL_RANK["DERIVED"]
            for r in deriv_rows
        ):
            errors.append(f"{where}: DERIVED needs a mature peer-reviewed derivation row distinct from parent")
    elif label == "SINGLE RESULT":
        if not any(
            r["kind"] == "peer-reviewed" and LABEL_RANK[r["label"]] >= LABEL_RANK["SINGLE RESULT"]
            for r in cited
        ):
            errors.append(f"{where}: SINGLE RESULT needs a peer-reviewed row whose ledger label is >= SINGLE RESULT; preprints/proposals stay PROPOSED")
    elif label == "PROPOSED":
        if not any(LABEL_RANK[r["label"]] >= LABEL_RANK["PROPOSED"] for r in cited):
            errors.append(f"{where}: PROPOSED needs a row whose ledger label is >= PROPOSED")
    # OPEN: any non-press row is enough.
    if label in ("MEASURED", "DERIVED", "BOUND"):
        young = [r["id"] for r in cited if is_young(r, today) or r["kind"] == "preprint"]
        if young and not supporting:
            errors.append(f"{where}: only young/preprint rows {young} back a {label} claim; cap at SINGLE RESULT or PROPOSED")


def page_paths() -> list[tuple[str, Path, Path, bool]]:
    out = []
    for p in PAGES:
        slug = p["slug"]
        rel = "timegravity/" + (f"{slug}/" if slug else "")
        out.append((rel, RESEARCH / rel / "index.html", RESEARCH / "es-mx" / rel / "index.html", slug == ""))
    return out


WARNINGS: list[str] = []

# Mutation suite (software-verification habit): each mutant is applied in memory and the lint must report >= 1 error.
MUTANTS: tuple[str, ...] = (
    "flip_up",        # SINGLE RESULT -> MEASURED (the planted defect)
    "drop_parent",    # first DERIVED claim loses data-tg-parent
    "press_row",      # a cited row becomes kind=press
    "stale_review",   # every review_by date has passed
    "same_collab",    # the rows behind the first MEASURED claim collapse to one collaboration
    "young_rows",     # the rows behind the first MEASURED claim were all published this year
    "es_mismatch",    # the Spanish twin's first label differs
    "no_boundary",    # the boundary line is missing from one page
    "hub_phrase",     # the hub-only sentence appears on a claim page
    "hub_claim",      # the hub carries a claim span
)


def lint(planted_defect: bool = False, today: dt.date | None = None, mutation: str | None = None) -> tuple[list[str], dict]:
    today = today or dt.date.today()
    if mutation == "flip_up":
        planted_defect = True
    if mutation == "stale_review":
        today = dt.date(2099, 1, 1)
    errors: list[str] = []
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    cache = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    if mutation == "press_row":
        ledger["rows"][0]["kind"] = "press"
    rows = check_ledger(ledger, cache, today, errors)
    summary = {"pages": 0, "claims": 0, "labels": {}}
    planted_done = False
    mutated = mutation in (None, "flip_up", "stale_review", "press_row")  # mutations applied before the page loop

    for rel, en_path, es_path, is_hub in page_paths():
        for path, lang in ((en_path, "en"), (es_path, "es")):
            if not path.is_file():
                errors.append(f"{rel}: missing {lang} page {path.relative_to(ROOT)}")
        if not (en_path.is_file() and es_path.is_file()):
            continue
        summary["pages"] += 2
        en_claims, en_raw, en_text = parse_page(en_path)
        es_claims, es_raw, es_text = parse_page(es_path)

        if mutation and not mutated:
            if mutation == "drop_parent" and any(c["label"] == "DERIVED" for c in en_claims):
                for lst in (en_claims, es_claims):
                    nxt_c = next(c for c in lst if c["label"] == "DERIVED")
                    nxt_c["parent"] = None
                mutated = True
            elif mutation in ("same_collab", "young_rows") and any(c["label"] == "MEASURED" for c in en_claims):
                first = next(c for c in en_claims if c["label"] == "MEASURED")
                for rid in first["ids"]:
                    if rid in rows:
                        if mutation == "same_collab":
                            rows[rid]["collaboration"] = "one collaboration"
                        else:
                            rows[rid]["year"] = today.year
                mutated = True
            elif mutation == "es_mismatch" and es_claims:
                es_claims[0]["label"] = "OPEN" if es_claims[0]["label"] != "OPEN" else "PROPOSED"
                mutated = True
            elif mutation == "no_boundary" and not is_hub:
                en_raw = en_raw.replace(BOUNDARY_EN, "").replace(html.escape(BOUNDARY_EN), "")
                mutated = True
            elif mutation == "hub_phrase" and not is_hub:
                en_raw = en_raw + "<p>" + HUB_ONLY_PHRASES[0] + "</p>"
                mutated = True
            elif mutation == "hub_claim" and is_hub:
                en_claims.append({"label": "OPEN", "ids": ["T01-WILL2014"], "parent": None, "text": "mutant"})
                es_claims.append({"label": "OPEN", "ids": ["T01-WILL2014"], "parent": None, "text": "mutante"})
                mutated = True

        if planted_defect and not planted_done:
            for idx_c, c in enumerate(en_claims):
                if c["label"] == "SINGLE RESULT":
                    c["label"] = "MEASURED"
                    if idx_c < len(es_claims):
                        es_claims[idx_c]["label"] = "MEASURED"
                    planted_done = True
                    break

        if [c["label"] for c in en_claims] != [c["label"] for c in es_claims]:
            errors.append(f"{rel}: English and es-MX label sequences differ")
        if [c["ids"] for c in en_claims] != [c["ids"] for c in es_claims]:
            errors.append(f"{rel}: English and es-MX ledger-id sequences differ")
        if [c.get("parent") for c in en_claims] != [c.get("parent") for c in es_claims]:
            errors.append(f"{rel}: English and es-MX parent-id sequences differ")

        if is_hub:
            if en_claims or es_claims:
                errors.append(f"{rel}: the hub must carry zero claim spans (found {len(en_claims)})")
        else:
            if not en_claims:
                errors.append(f"{rel}: a claim page with no claim spans")
            for raw, lang in ((en_raw, "en"), (es_raw, "es")):
                if 'class="tg-ai-line"' not in raw:
                    errors.append(f"{rel} ({lang}): missing the AI-contribution line (class tg-ai-line)")

        for i, c in enumerate(en_claims):
            summary["claims"] += 1
            summary["labels"][c["label"]] = summary["labels"].get(c["label"], 0) + 1
            check_claim(rel, i, c, rows, today, errors)
        for i, c in enumerate(es_claims):
            check_claim(f"{rel} (es)", i, c, rows, today, errors)

        for raw, text, lang, boundary in ((en_raw, en_text, "en", BOUNDARY_EN), (es_raw, es_text, "es", BOUNDARY_ES)):
            if boundary not in raw and html.escape(boundary) not in raw:
                errors.append(f"{rel} ({lang}): the fixed boundary line is missing")
            low = html.unescape(raw).lower()          # attributes and text: a mention anywhere counts
            low_text = " ".join(text.split()).lower()  # rendered text only, for the once-per-language rule
            for phrase in BANNED_EVERYWHERE:
                if phrase in low:
                    errors.append(f"{rel} ({lang}): banned phrase {phrase!r}")
            for phrase in HUB_ONLY_PHRASES:
                if is_hub:
                    n = low_text.count(phrase)
                    if n > 1:
                        errors.append(f"{rel} ({lang}): the hub states {phrase!r} {n} times in its text; once is the limit")
                elif phrase in low:
                    errors.append(f"{rel} ({lang}): {phrase!r} is allowed on the hub only")

    referenced = {rid for p in PAGES for rid in p.get("ledger_ids", [])}
    for rid in rows:
        if rid not in referenced:
            summary.setdefault("unreferenced_rows", []).append(rid)

    if planted_defect and not planted_done:
        errors.append("planted defect requested but no SINGLE RESULT claim exists to flip")
    if mutation and not mutated:
        errors.append(f"mutant {mutation!r} could not be applied (nothing to mutate)")
    return errors, summary


def run_mutants(today: dt.date) -> tuple[list[str], list[str]]:
    """Apply every mutant in memory; return (killed, survived). A surviving mutant means a fail-open rule."""
    killed, survived = [], []
    for m in MUTANTS:
        errs, _ = lint(today=today, mutation=m)
        (killed if errs else survived).append(m)
    return killed, survived


def main() -> int:
    ap = argparse.ArgumentParser(description="Time & Gravity ledger-driven label lint")
    ap.add_argument("--planted-defect", action="store_true", help="flip one label upward in memory; the lint must fail")
    ap.add_argument("--mutants", action="store_true", help="run the mutation suite only and report killed/survived")
    ap.add_argument("--today", help="override the build date (YYYY-MM-DD) for review_by and age rules")
    args = ap.parse_args()
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    if args.mutants:
        killed, survived = run_mutants(today)
        for m in killed:
            print(f"KILLED   {m}")
        for m in survived:
            print(f"SURVIVED {m}", file=sys.stderr)
        print(f"MUTANTS: {len(killed)}/{len(MUTANTS)} killed")
        return 1 if survived else 0

    errors, summary = lint(planted_defect=args.planted_defect, today=today)
    if args.planted_defect:
        if errors:
            print("FAIL: planted label defect caught as expected:", file=sys.stderr)
            for e in errors:
                print(f"FAIL: {e}", file=sys.stderr)
            return 1
        print("FAIL: planted label defect was NOT caught; the lint is fail-open", file=sys.stderr)
        return 2

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1

    # Self-test: the lint must reject a label flipped upward via check_claim().
    planted_errors, _ = lint(planted_defect=True, today=today)
    has_epistemic_rejection = any("MEASURED needs >=" in e for e in planted_errors)
    knockout = "REJECTED_AS_EXPECTED" if has_epistemic_rejection else "NOT_REJECTED"
    if not has_epistemic_rejection:
        print("FAIL: self-test: a label flipped upward was not rejected by check_claim()", file=sys.stderr)
        return 1
    killed, survived = run_mutants(today)
    if survived:
        for m in survived:
            print(f"FAIL: mutant {m!r} survived the lint (fail-open rule)", file=sys.stderr)
        return 1
    for w in sorted(set(WARNINGS)):
        print(f"WARN: {w}", file=sys.stderr)
    labels = ", ".join(f"{k}={v}" for k, v in sorted(summary["labels"].items()))
    print(
        f"PASS: Time & Gravity label lint verified ({summary['pages']} pages, {summary['claims']} claims: {labels}; "
        f"{len(json.loads(LEDGER_PATH.read_text(encoding='utf-8'))['rows'])} ledger rows resolve; planted_defect_knockout={knockout}; "
        f"mutants killed {len(killed)}/{len(MUTANTS)}; scite warnings {len(set(WARNINGS))})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
