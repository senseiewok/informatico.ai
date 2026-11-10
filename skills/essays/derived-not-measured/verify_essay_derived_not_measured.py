#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic stdlib verifier for Essay ES.02 (`Derived, Not Measured`).

Usage:
  python -X utf8 skills/essays/derived-not-measured/verify_essay_derived_not_measured.py
  python -X utf8 skills/essays/derived-not-measured/verify_essay_derived_not_measured.py --planted-defect
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools" / "folios" / "essays" / "e02_derived_not_measured.py"
CACHE_PATH = ROOT / "data" / "folio-citations.cache.json"

FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
INLINE_DOI_RE = re.compile(r"10\.\d{4,9}/[^\s,;)\"']+")
DECIMAL_COMMA_RE = re.compile(r"\d,\d{1,2}(?!\d)")

BANNED_PHRASES = (
    "unifies",
    "unify gravity",
    "unification of gravity",
    "proves the theory of everything",
    "theory of everything is",
    "solves the information paradox",
    "resolves the information paradox",
    "unifica",
    "demuestra la teoría del todo",
    "prueba la teoría del todo",
    "resuelve la paradoja de la información",
    "gravity is a slope in time",
    "gravity is a slope in the rate of time",
    "la gravedad es una pendiente en el tiempo",
    "la gravedad es una pendiente en el ritmo del tiempo",
)


def _load_essay_module():
    assert MODULE_PATH.is_file(), f"Missing essay module: {MODULE_PATH}"
    spec = importlib.util.spec_from_file_location("e02_derived_not_measured", MODULE_PATH)
    assert spec is not None and spec.loader is not None, "Unable to create module spec"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _word_count(text: str) -> int:
    return len(re.findall(r"\S+", text.strip()))


def _parse_frontmatter(md_text: str) -> dict[str, str]:
    lines = md_text.splitlines()
    assert lines and lines[0].strip() == "---", "SKILL.md must begin with YAML --- frontmatter"
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    assert end_idx is not None, "SKILL.md frontmatter missing closing ---"
    meta: dict[str, str] = {}
    for line in lines[1:end_idx]:
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def _assert_parity(mod, label: str, en_text: str, es_text: str) -> None:
    en_nums = mod.extract_number_tokens(en_text)
    es_nums = mod.extract_number_tokens(es_text)
    assert en_nums == es_nums, f"Numeric parity mismatch in {label}: EN {en_nums} vs ES {es_nums}"
    assert DECIMAL_COMMA_RE.search(es_text) is None, (
        f"Spanish decimal comma forbidden in es-MX ({label}): {es_text!r}"
    )


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args

    try:
        mod = _load_essay_module()
        essay = mod.ESSAY

        # 1. Physics & Three-Absence Quantitative Probes
        bmv = mod.compute_bmv_derived_witness()
        assert 0.30 < bmv["delta_phi_rad"] < 0.33, f"Unexpected BMV phase: {bmv['delta_phi_rad']}"
        assert 0.15 < bmv["concurrence_closed"] < 0.165, f"Unexpected BMV concurrence: {bmv['concurrence_closed']}"
        assert bmv["purity_agreement_abs_diff"] < 1.0e-12, (
            f"Closed form vs purity exceeded 1e-12: {bmv['purity_agreement_abs_diff']}"
        )
        assert bmv["phenomenon_label"] == "PROPOSED", "Unbuilt BMV witness must stay PROPOSED"
        assert bmv["calculation_label"] == "DERIVED (NOT MEASURED)", "BMV calculation must be DERIVED (NOT MEASURED)"
        assert bmv["measured_parent_id"] == "T05-WESTPHAL2021", "BMV calculation must cite T05-WESTPHAL2021 parent"

        recast = mod.compute_smeared_recast_probe()
        assert abs(recast["newton_limit_ratio"] - 1.0) < 1.0e-12, "sigma -> 0 limit must recover Newton 1.0"
        assert recast["at_33um"]["excluded_95"] is False, "sigma = 33 um (-7.3 vs -7.4) must remain allowed at 95%"
        assert recast["at_35um"]["excluded_95"] is True, "sigma = 35 um (-10.2 vs -7.4) must be excluded at 95%"
        assert recast["calculation_label"] == "DERIVED (NOT MEASURED)", "Recast must be DERIVED (NOT MEASURED)"
        assert recast["measured_parent_id"] == "T05-LEE2020", "Recast must cite T05-LEE2020 parent"

        cryo = mod.audit_cryoem_coordinate_absence()
        assert cryo["wt_508_resolved"] is True, "Wild-type Phe508 must be resolved in 5UAK, 5W81, and 6MSM"
        assert cryo["df508_genetically_deleted"] is True, "8EIQ must record residue 508 as genetically deleted"
        assert cryo["all_four_r_domain_open"] is True, "All 4 Cryo-EM maps must mark ~200 R-domain residues OPEN"

        # 2. Epistemic Lattice & 8-Mutant Falsification Harness
        mut = mod.run_epistemic_mutations(planted_defect=planted)
        assert mut["baseline_valid"] is True, f"Clean benchmark failed lattice check: {mut['baseline_errors']}"
        assert mut["mutants_total"] == 8, f"Expected 8 epistemic mutants, got {mut['mutants_total']}"
        assert mut["mutants_killed"] == 8, (
            f"Epistemic mutation-kill failure: {mut['mutants_killed']}/{mut['mutants_total']} killed "
            f"(surviving: {[m['id'] for m in mut['mutants'] if not m['killed']]})"
        )

        # Internal knockout self-check on normal runs
        knockout_probe = mod.run_epistemic_mutations(planted_defect=True)
        assert knockout_probe["mutants_killed"] < knockout_probe["mutants_total"], (
            "--planted-defect failed to let a mutant survive during internal self-test"
        )

        # 3. ESSAY Dictionary Contract & SEO Validation
        required_keys = (
            "code", "slug", "plate_slug", "date", "seo",
            "kicker_en", "kicker_es", "reading_time_en", "reading_time_es",
            "title_en", "title_es", "standfirst_en", "standfirst_es",
            "card_dek_en", "card_dek_es", "instrument_kind", "predict",
            "sections", "sidenotes", "sources", "skill_path", "verifier_path",
            "ai_line_en", "ai_line_es",
        )
        for key in required_keys:
            assert key in essay, f"ESSAY missing required key: {key!r}"

        assert essay["code"] == "ES.02"
        assert essay["slug"] == "derived-not-measured"
        assert essay["plate_slug"] == "essay02"
        assert essay["date"] == "2026-11-10"
        assert essay["reading_time_en"] == "13 min read"
        assert essay["reading_time_es"] == "13 min de lectura"
        assert essay["instrument_kind"] == "epistemic"

        t_en, d_en, t_es, d_es = essay["seo"]
        for lang_tag, s_title in (("en", t_en), ("es", t_es)):
            assert 18 <= len(s_title) <= 50, f"SEO title_{lang_tag} length {len(s_title)} outside 18..50: {s_title!r}"
            assert "informatico" not in s_title.lower(), f"SEO title_{lang_tag} must omit brand suffix"
        for lang_tag, s_desc in (("en", d_en), ("es", d_es)):
            assert 115 <= len(s_desc) <= 152, f"SEO desc_{lang_tag} length {len(s_desc)} outside 115..152: {s_desc!r}"
            assert s_desc.endswith("."), f"SEO desc_{lang_tag} must end with period: {s_desc!r}"
            assert "medical" not in s_desc.lower() and "médic" not in s_desc.lower(), (
                f"SEO desc_{lang_tag} must not mention medical/médic"
            )
            assert FORMULA_RE.search(s_desc) is None, f"SEO desc_{lang_tag} contains forbidden formula characters"
            last_word = re.findall(r"[\wÀ-ÿ]+", s_desc)[-1].lower()
            assert last_word not in DANGLING_WORDS, f"SEO desc_{lang_tag} ends on dangling word {last_word!r}"

        # Predict block check
        pred = essay["predict"]
        assert pred["answer"] in ("a", "b")
        assert len(pred["choices"]) == 2 and {c["id"] for c in pred["choices"]} == {"a", "b"}
        _assert_parity(mod, "predict.question", pred["question_en"], pred["question_es"])
        _assert_parity(mod, "predict.explain", pred["explain_en"], pred["explain_es"])
        for ch in pred["choices"]:
            _assert_parity(mod, f"predict.choice.{ch['id']}", ch["en"], ch["es"])

        _assert_parity(mod, "reading_time", essay["reading_time_en"], essay["reading_time_es"])
        _assert_parity(mod, "standfirst", essay["standfirst_en"], essay["standfirst_es"])
        _assert_parity(mod, "card_dek", essay["card_dek_en"], essay["card_dek_es"])
        _assert_parity(mod, "ai_line", essay["ai_line_en"], essay["ai_line_es"])

        # 4. Sections, Word Counts, Bilingual Numeric Parity & Proportional CF Cap
        sections = essay["sections"]
        assert len(sections) == 5, f"Expected 5 sections, got {len(sections)}"
        roman_prefixes = ("I · ", "II · ", "III · ", "IV · ", "V · ")

        prose_en_chunks: list[str] = []
        prose_es_chunks: list[str] = []
        all_en_chunks: list[str] = []
        all_es_chunks: list[str] = []

        for idx, sec in enumerate(sections):
            for skey in ("id", "h2_en", "h2_es", "short_en", "short_es", "blocks"):
                assert skey in sec, f"Section #{idx + 1} missing {skey!r}"
            assert sec["h2_en"].startswith(roman_prefixes[idx]), f"Section #{idx + 1} h2_en prefix mismatch"
            assert sec["h2_es"].startswith(roman_prefixes[idx]), f"Section #{idx + 1} h2_es prefix mismatch"
            _assert_parity(mod, f"section.{sec['id']}.h2", sec["h2_en"], sec["h2_es"])

            for b_idx, blk in enumerate(sec["blocks"]):
                btype = blk["type"]
                assert btype in ("p", "bridge", "analogy", "equation", "table"), f"Unknown block type {btype!r}"
                loc = f"{sec['id']}.block[{b_idx}]({btype})"
                if btype == "p":
                    _assert_parity(mod, loc, blk["en"], blk["es"])
                    prose_en_chunks.append(blk["en"])
                    prose_es_chunks.append(blk["es"])
                    all_en_chunks.append(blk["en"])
                    all_es_chunks.append(blk["es"])
                elif btype in ("bridge", "analogy"):
                    _assert_parity(mod, f"{loc}.kicker", blk["kicker_en"], blk["kicker_es"])
                    if blk.get("title_en") or blk.get("title_es"):
                        _assert_parity(mod, f"{loc}.title", blk["title_en"], blk["title_es"])
                    assert blk.get("paras"), f"{loc} must contain non-empty paras"
                    for p_idx, (pe, ps_) in enumerate(blk["paras"]):
                        _assert_parity(mod, f"{loc}.paras[{p_idx}]", pe, ps_)
                        prose_en_chunks.append(pe)
                        prose_es_chunks.append(ps_)
                        all_en_chunks.append(pe)
                        all_es_chunks.append(ps_)
                elif btype == "equation":
                    assert blk.get("formula"), f"{loc} missing formula"
                    _assert_parity(mod, f"{loc}.label", blk["label_en"], blk["label_es"])
                    _assert_parity(mod, f"{loc}.note", blk["note_en"], blk["note_es"])
                    all_en_chunks.append(blk["label_en"] + " " + blk["note_en"])
                    all_es_chunks.append(blk["label_es"] + " " + blk["note_es"])
                elif btype == "table":
                    _assert_parity(mod, f"{loc}.caption", blk["caption_en"], blk["caption_es"])
                    assert len(blk["headers_en"]) == len(blk["headers_es"])
                    all_en_chunks.append(blk["caption_en"] + " " + " ".join(blk["headers_en"]))
                    all_es_chunks.append(blk["caption_es"] + " " + " ".join(blk["headers_es"]))
                    for r_idx, row in enumerate(blk["rows"]):
                        assert len(row) == len(blk["headers_en"]), f"{loc}.row[{r_idx}] column count mismatch"
                        for c_idx, (cell_en, cell_es) in enumerate(row):
                            _assert_parity(mod, f"{loc}.row[{r_idx}].col[{c_idx}]", cell_en, cell_es)
                        all_en_chunks.append(" ".join(c[0] for c in row))
                        all_es_chunks.append(" ".join(c[1] for c in row))

        prose_words_en = _word_count(" ".join(prose_en_chunks))
        total_words_en = _word_count(" ".join(all_en_chunks))
        assert 1800 <= prose_words_en <= 2600, (
            f"English prose word count {prose_words_en} outside 1800..2600 (all-blocks={total_words_en})"
        )
        assert 1800 <= total_words_en <= 2600, (
            f"English all-blocks word count {total_words_en} outside 1800..2600 (prose={prose_words_en})"
        )

        # Sidenotes check
        sidenotes = essay["sidenotes"]
        assert 4 <= len(sidenotes) <= 5, f"Expected 4..5 sidenotes, got {len(sidenotes)}"
        for sn_idx, sn in enumerate(sidenotes):
            _assert_parity(mod, f"sidenote[{sn_idx}].label", sn["label_en"], sn["label_es"])
            _assert_parity(mod, f"sidenote[{sn_idx}].body", sn["en"], sn["es"])

        # Proportional CF & accuracy guardrails across full text
        full_en = " ".join(
            [essay["title_en"], essay["standfirst_en"], essay["card_dek_en"]]
            + all_en_chunks
            + [sn["en"] for sn in sidenotes]
        )
        full_es = " ".join(
            [essay["title_es"], essay["standfirst_es"], essay["card_dek_es"]]
            + all_es_chunks
            + [sn["es"] for sn in sidenotes]
        )
        cf_count_en = len(re.findall(r"cystic fibrosis", full_en, flags=re.IGNORECASE))
        cf_count_es = len(re.findall(r"fibrosis qu[ií]stica", full_es, flags=re.IGNORECASE))
        assert cf_count_en <= 2, f"Cystic Fibrosis mentioned {cf_count_en} times in EN (max 2)"
        assert cf_count_es <= 2, f"fibrosis quística mentioned {cf_count_es} times in ES (max 2)"

        for phrase in BANNED_PHRASES:
            assert phrase not in full_en.lower(), f"Banned phrase {phrase!r} found in EN text"
            assert phrase not in full_es.lower(), f"Banned phrase {phrase!r} found in ES text"

        # 5. Offline Crossref Cache Resolution for Sources & Inline DOIs
        assert CACHE_PATH.is_file(), f"Missing citation cache: {CACHE_PATH}"
        cache = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        sources = essay["sources"]
        assert 8 <= len(sources) <= 10, f"Expected 8..10 sources, got {len(sources)}"
        seen_ids: set[str] = set()
        for src in sources:
            sid = src["id"]
            assert sid.startswith("ES02-") and sid not in seen_ids, f"Invalid or duplicate source id {sid!r}"
            seen_ids.add(sid)
            doi = src["doi"].strip()
            rec = cache.get("doi:" + doi.lower())
            assert rec and rec.get("found"), f"Source {sid} DOI {doi} missing from data/folio-citations.cache.json"
            if rec.get("year"):
                assert abs(int(rec["year"]) - int(src["year"])) <= 1, (
                    f"Source {sid} year {src['year']} disagrees with Crossref {rec['year']}"
                )
            _assert_parity(mod, f"source.{sid}.role", src["role_en"], src["role_es"])

        for inline_doi in set(INLINE_DOI_RE.findall(full_en + " " + full_es)):
            cleaned = inline_doi.rstrip(".")
            rec = cache.get("doi:" + cleaned.lower())
            assert rec and rec.get("found"), f"Inline DOI {cleaned} not found in data/folio-citations.cache.json"

        # 6. Companion SKILL.md & Verifier Path Validation
        skill_file = ROOT / essay["skill_path"]
        verifier_file = ROOT / essay["verifier_path"]
        assert skill_file.is_file(), f"Missing SKILL.md at {skill_file}"
        assert verifier_file.is_file(), f"Missing verifier at {verifier_file}"
        fm = _parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        assert fm.get("name") == "essay-es02-derived-not-measured", f"Unexpected SKILL.md name: {fm.get('name')!r}"
        assert fm.get("license") == "MIT", "SKILL.md must declare license: MIT"
        assert fm.get("description") and fm.get("compatibility"), "SKILL.md missing description or compatibility"

    except AssertionError as exc:
        print(
            json.dumps(
                {
                    "status": "FAIL",
                    "essay": "ES.02",
                    "slug": "derived-not-measured",
                    "planted_defect": planted,
                    "error": str(exc),
                }
            ),
            file=sys.stderr,
        )
        return 1

    out = {
        "status": "PASS",
        "essay": "ES.02",
        "slug": "derived-not-measured",
        "mutants_killed": mut["mutants_killed"],
        "mutants_total": mut["mutants_total"],
        "mutation_recall": mut["recall"],
        "planted_defect_self_test": "REJECTED_AS_EXPECTED",
        "word_counts": {
            "prose_en": prose_words_en,
            "all_blocks_en": total_words_en,
        },
        "seo_lengths": {
            "title_en": len(t_en),
            "desc_en": len(d_en),
            "title_es": len(t_es),
            "desc_es": len(d_es),
        },
        "cf_mentions": {
            "en": cf_count_en,
            "es": cf_count_es,
        },
        "probes": {
            "bmv_delta_phi_rad": round(bmv["delta_phi_rad"], 6),
            "bmv_concurrence": round(bmv["concurrence_closed"], 6),
            "bmv_purity_diff": bmv["purity_agreement_abs_diff"],
            "recast_sigma_95_um": recast["sigma_95_limit_um"],
            "sources_verified": len(sources),
        },
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
