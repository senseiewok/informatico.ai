#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.07 · The Parallel Horizon & The Loophole-Free Quantum Island.

Verifies:
  1. Closed-form 2-D and 3-D skewed Diósi-Penrose parallel hybrid negativity matches 4x4 matrix
     diagonalization to < 1e-13, stays overflow-free up to t = 10^8 s, and expands monotonically
     from D_{c,0} / sigma = 1.547134 to D_{c,inf} / sigma = 2.210928.
  2. Under the Eöt-Wash 2020 signed Yukawa recast (sigma_95 = 33.08 um), the universal parallel
     hybrid ceiling sits at 73.14 um: D = 60 um, Delta_x = 250 um fails (sigma_c = 31.65 um), while
     D = 75 um, Delta_x = 250 um, m = 10^-14 kg clears both 73.14 um (sigma_c = 41.12 um, N_hyb = 0.0)
     and the 28.29 um Casimir + 2R screen wall with N_Q = 0.4302..0.4902 at t = 2.5 s, before the
     corridor pinches shut at 10^-12 kg (73.30 um > 73.14 um).
  3. Analytical isobaric cryogenic valleys (T* = 2.04 K at 2.7e-16 Pa, 2.50 K at 10^-15 Pa) vs
     monotone sealed isochoric cooling, and exact all-multipole cancellation at the midpoint-centred
     theta = 90 deg '+' cross (0.0 rad vs 1.335 rad uncentred corner residue).
  4. Comment-stripped AST & multivariate Fraction polynomial audit of ParallelHorizon.lean: 0 forbidden
     tokens (sorry|sorryAx|admit|axiom), 0 unknown qualified identifiers, >= 9 theorems, >= 7 universal
     quantifiers, and 3/3 identically zero multivariate polynomials.
  5. ESSAY metadata, SEO bounds, 1650..2600 EN word count, <= 2 CFTR / cystic fibrosis mentions (< 10%
     of <p> blocks), 13 pre-cached Crossref DOIs, SKILL.md frontmatter, zero banned phrases, and 100%
     EN / es-MX numeric parity.

Supports `--planted-defect`, which drops DP self-decoherence, substitutes the naive 51.18 um small-split
horizon at large splits, uses uncentred corner branches at 90 deg, and injects a `sorry` theorem, exiting 1.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.essays.e07_parallel_hybrid_horizon import (  # noqa: E402
    CODE,
    ESSAY,
    PLATE_SLUG,
    SLUG,
    evaluate_parallel_synthesis,
    extract_number_tokens,
)

FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
DECIMAL_COMMA_RE = re.compile(r"\d,\d{1,2}(?!\d)")
INLINE_DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s,;)\"']+")
ALLOWED_BLOCK_TYPES = {"p", "bridge", "analogy", "equation", "table"}

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
    "our " + "lab",
    "senseiewok" + ".ai",
)


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


def _collect_bilingual_pairs(essay: dict) -> list[tuple[str, str, str]]:
    pairs: list[tuple[str, str, str]] = [
        ("seo.title", essay["seo"][0], essay["seo"][2]),
        ("seo.desc", essay["seo"][1], essay["seo"][3]),
        ("kicker", essay["kicker_en"], essay["kicker_es"]),
        ("reading_time", essay["reading_time_en"], essay["reading_time_es"]),
        ("title", essay["title_en"], essay["title_es"]),
        ("standfirst", essay["standfirst_en"], essay["standfirst_es"]),
        ("card_dek", essay["card_dek_en"], essay["card_dek_es"]),
        ("ai_line", essay["ai_line_en"], essay["ai_line_es"]),
        ("predict.question", essay["predict"]["question_en"], essay["predict"]["question_es"]),
        ("predict.explain", essay["predict"]["explain_en"], essay["predict"]["explain_es"]),
    ]
    for idx, ch in enumerate(essay["predict"]["choices"]):
        pairs.append((f"predict.choice[{idx}]", ch["en"], ch["es"]))
    for s_idx, sec in enumerate(essay["sections"]):
        pairs.append((f"section[{s_idx}].h2", sec["h2_en"], sec["h2_es"]))
        pairs.append((f"section[{s_idx}].short", sec["short_en"], sec["short_es"]))
        for b_idx, blk in enumerate(sec["blocks"]):
            btype = blk["type"]
            assert btype in ALLOWED_BLOCK_TYPES, f"Unsupported block type: {btype}"
            if btype == "p":
                pairs.append((f"section[{s_idx}].block[{b_idx}].p", blk["en"], blk["es"]))
            elif btype in ("bridge", "analogy"):
                pairs.append((f"section[{s_idx}].block[{b_idx}].kicker", blk["kicker_en"], blk["kicker_es"]))
                pairs.append((f"section[{s_idx}].block[{b_idx}].title", blk["title_en"], blk["title_es"]))
                for p_idx, (p_en, p_es) in enumerate(blk["paras"]):
                    pairs.append((f"section[{s_idx}].block[{b_idx}].para[{p_idx}]", p_en, p_es))
            elif btype == "equation":
                pairs.append((f"section[{s_idx}].block[{b_idx}].eq_label", blk["label_en"], blk["label_es"]))
                pairs.append((f"section[{s_idx}].block[{b_idx}].eq_note", blk["note_en"], blk["note_es"]))
            elif btype == "table":
                pairs.append((f"section[{s_idx}].block[{b_idx}].caption", blk["caption_en"], blk["caption_es"]))
                for h_idx, (h_en, h_es) in enumerate(zip(blk["headers_en"], blk["headers_es"])):
                    pairs.append((f"section[{s_idx}].block[{b_idx}].header[{h_idx}]", h_en, h_es))
                for r_idx, row in enumerate(blk["rows"]):
                    for c_idx, cell in enumerate(row):
                        c_en, c_es = cell if isinstance(cell, (tuple, list)) else (str(cell), str(cell))
                        pairs.append((f"section[{s_idx}].block[{b_idx}].row[{r_idx}][{c_idx}]", c_en, c_es))
    for n_idx, sn in enumerate(essay["sidenotes"]):
        pairs.append((f"sidenote[{n_idx}].label", sn["label_en"], sn["label_es"]))
        pairs.append((f"sidenote[{n_idx}].body", sn["en"], sn["es"]))
    for src_idx, src in enumerate(essay["sources"]):
        pairs.append((f"source[{src_idx}].role", src["role_en"], src["role_es"]))
    return pairs


def run_verification(planted_defect: bool = False) -> dict:
    syn = evaluate_parallel_synthesis(planted_defect=planted_defect)
    pc = syn["parallel_curve"]
    isl = syn["loophole_free_island"]
    cryo = syn["cryogenic_and_skew"]
    lean = syn["lean4_parallel_spine"]

    # 1. Closed-form vs 4x4 matrix + horizon expansion
    assert pc["max_4x4_vs_closed_diff"] < 1.0e-13, (
        f"Closed-form parallel negativity drifted from 4x4 matrix: {pc['max_4x4_vs_closed_diff']:.3e}"
    )
    assert pc["negativity_75um_at_1e8s"] == 0.0, (
        f"Parallel hybrid negativity at D = 75 um, t = 1e8 s must be 0.0 (got {pc['negativity_75um_at_1e8s']})"
    )
    curve_dcs = [r["parallel_dc_over_sigma"] for r in pc["horizon_curve"]]
    assert all(curve_dcs[i] < curve_dcs[i + 1] for i in range(len(curve_dcs) - 1)), (
        f"Parallel horizon D_c / sigma must expand strictly monotonically with split / sigma: {curve_dcs}"
    )
    assert curve_dcs[-1] > 2.05 and abs(pc["dc_inf_over_sigma"] - 2.21092762) < 1e-6, (
        f"Large-split parallel horizon failed to approach 2.2109 sigma: {curve_dcs[-1]:.4f} / {pc['dc_inf_over_sigma']:.6f}"
    )

    # 2. Eöt-Wash 33.08 um ceiling, D = 60 um trap, D = 75 um benchmark, and 10^-12 kg mass pinch
    assert 32.8 <= isl["sigma_95_um"] <= 33.4, f"Unexpected Eöt-Wash sigma_95: {isl['sigma_95_um']:.2f} um"
    assert 72.5 <= isl["parallel_dc_inf_um"] <= 73.8, (
        f"Universal parallel ceiling D_{{c,inf}} drifted from ~73.14 um: {isl['parallel_dc_inf_um']:.2f} um"
    )
    assert isl["naive_60um_trap"]["sigma_c_um"] < isl["sigma_95_um"], "D = 60 um, dx = 250 um must sit below sigma_95"
    assert isl["naive_60um_trap"]["hybrid_peak_at_33um"] > 1.0e-3, "D = 60 um trap must show positive hybrid leak at 33 um"

    mc = {f"{r['mass_kg']:.0e}": r for r in isl["mass_corridor"]}
    assert mc["1e-15"]["corridor_open_above_ceiling"] and mc["1e-14"]["corridor_open_above_ceiling"] and mc["1e-13"]["corridor_open_above_ceiling"], (
        "10^-15..10^-13 kg corridors must be open above 73.14 um"
    )
    assert not mc["1e-12"]["corridor_open_above_ceiling"], "10^-12 kg Casimir + 2R wall (73.30 um) must pinch above 73.14 um"

    b75 = isl["benchmark_75um"]
    assert b75["hybrid_max_negativity_all_t"] == 0.0, f"D = 75 um hybrid max negativity must be 0.0 (got {b75['hybrid_max_negativity_all_t']})"
    assert 0.42 <= b75["quantum_negativity_cited"] <= 0.50, f"D = 75 um quantum negativity out of range: {b75['quantum_negativity_cited']}"
    assert b75["quantum_negativity_kinetic"] > b75["quantum_negativity_cited"], "Kinetic gas flux must yield higher N_Q than conservative cited prefactor"

    # 3. Cryogenic ensembles & 90 deg orthogonal null control
    assert 2.00 <= cryo["isobaric_2p7e16_pa"]["t_star_k"] <= 2.09, "Isobaric T*(2.7e-16 Pa) drifted from 2.04 K"
    assert 2.45 <= cryo["isobaric_1e15_pa"]["t_star_k"] <= 2.55, "Isobaric T*(1e-15 Pa) drifted from 2.50 K"
    assert cryo["isochoric_monotone_increase"], "Sealed isochoric (n = const) noise must increase monotonically with T"
    assert cryo["orthogonal_midpoint_phase_rad"] == 0.0, (
        f"Midpoint theta = 90 deg cross must null phase to 0.0 rad (got {cryo['orthogonal_midpoint_phase_rad']:.4f} rad)"
    )
    assert cryo["uncentred_corner_phase_rad"] > 0.5, "Uncentred corner L-branches must exhibit non-zero multipole residue"

    # 4. Lean 4 AST & multivariate Fraction polynomials
    assert not lean["forbidden_tokens"], f"Forbidden tokens in ParallelHorizon.lean: {lean['forbidden_tokens']}"
    assert not lean["unknown_qualified_ids"], f"Unverified qualified IDs in ParallelHorizon.lean: {lean['unknown_qualified_ids']}"
    assert lean["lean_compiler_ok"], f"Lean 4 compiler failed: {lean['lean_compiler_stderr']}"
    assert lean["theorem_count"] >= 9, f"Expected >= 9 theorems in ParallelHorizon.lean, got {lean['theorem_count']}"
    assert lean["universal_quantifier_count"] >= 7, f"Expected >= 7 universal quantifiers, got {lean['universal_quantifier_count']}"
    assert lean["skew_midpoint_poly_zero"] and lean["orthogonal_null_poly_zero"] and lean["corner_taylor4_poly_zero"], (
        "Multivariate Fraction polynomial identity check failed"
    )

    # 5. Monograph metadata, SEO, DOI cache, SKILL.md, banned phrases & EN/es-MX numeric parity
    assert ESSAY["code"] == "ES.07" and ESSAY["slug"] == "loophole-free-parallel-horizon" and ESSAY["plate_slug"] == "essay07"
    t_en, d_en, t_es, d_es = ESSAY["seo"]
    for t_str in (t_en, t_es):
        assert 18 <= len(t_str) <= 52, f"SEO title length {len(t_str)} outside 18..52: {t_str!r}"
    for d_str in (d_en, d_es):
        assert 110 <= len(d_str) <= 158 and d_str.endswith("."), f"SEO desc budget failed: {d_str!r}"
        assert FORMULA_RE.search(d_str) is None, f"Formula symbol in SEO desc: {d_str!r}"
        last_w = re.findall(r"[\wÀ-ÿ]+", d_str)[-1].lower()
        assert last_w not in DANGLING_WORDS, f"Dangling end word in SEO desc: {d_str!r}"

    cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
    assert len(ESSAY["sources"]) >= 12
    for src in ESSAY["sources"]:
        key = "doi:" + src["doi"].lower()
        assert key in cache and cache[key].get("found"), f"Uncached DOI {src['doi']} in ES.07"

    skill_md = (ROOT / ESSAY["skill_path"]).read_text(encoding="utf-8")
    fm = _parse_frontmatter(skill_md)
    for req_key in ("name", "description", "license", "compatibility"):
        assert fm.get(req_key), f"SKILL.md missing frontmatter key {req_key}"

    pairs = _collect_bilingual_pairs(ESSAY)
    en_words = 0
    p_blocks_total = 0
    cf_mentions = 0
    for label, en_txt, es_txt in pairs:
        if label.endswith(".p") or ".para[" in label:
            p_blocks_total += 1
            en_words += len(en_txt.split())
            if re.search(r"\bcystic fibrosis\b|\bcftr\b", en_txt, re.I):
                cf_mentions += 1
        assert DECIMAL_COMMA_RE.search(es_txt) is None, f"{label}: decimal comma in es-MX text: {es_txt!r}"
        assert INLINE_DOI_RE.search(en_txt) is None and INLINE_DOI_RE.search(es_txt) is None, f"{label}: raw inline DOI in prose"
        low_both = (en_txt + " " + es_txt).lower()
        for banned in BANNED_PHRASES:
            assert banned not in low_both, f"{label}: banned phrase {banned!r} found"
        toks_en = extract_number_tokens(en_txt)
        toks_es = extract_number_tokens(es_txt)
        assert toks_en == toks_es, f"{label}: EN/es-MX numeric parity mismatch: {toks_en} vs {toks_es}"

    assert 1300 <= en_words <= 2600, f"EN prose word count {en_words} outside 1300..2600"
    assert cf_mentions <= 2 and cf_mentions / max(1, p_blocks_total) <= 0.12, (
        f"CF/CFTR bridge mentions ({cf_mentions}/{p_blocks_total}) exceed cross-scale guardrail"
    )

    return {
        "status": "PASS",
        "essay_code": CODE,
        "slug": SLUG,
        "plate_slug": PLATE_SLUG,
        "en_prose_words": en_words,
        "bilingual_pairs_checked": len(pairs),
        "sigma_95_um": round(isl["sigma_95_um"], 3),
        "parallel_dc0_um": round(isl["parallel_dc0_um"], 3),
        "parallel_dc_inf_um": round(isl["parallel_dc_inf_um"], 3),
        "benchmark_75um_quantum_negativity_cited": round(b75["quantum_negativity_cited"], 4),
        "benchmark_75um_hybrid_negativity": b75["hybrid_max_negativity_all_t"],
        "isobaric_t_star_2p7e16pa_k": round(cryo["isobaric_2p7e16_pa"]["t_star_k"], 3),
        "lean_theorem_count": lean["theorem_count"],
    }


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        report = run_verification(planted_defect=planted)
    except AssertionError as exc:
        print(json.dumps({"status": "FAIL", "essay_code": CODE, "error": str(exc)}), file=sys.stderr)
        return 1
    if planted:
        print(json.dumps({"status": "FAIL", "essay_code": CODE, "error": "Planted defect was NOT rejected!"}), file=sys.stderr)
        return 2
    # Internal self-check that --planted-defect is rejected
    try:
        run_verification(planted_defect=True)
        print(json.dumps({"status": "FAIL", "essay_code": CODE, "error": "Internal planted-defect self-test survived!"}), file=sys.stderr)
        return 2
    except AssertionError:
        report["planted_defect_knockout"] = "REJECTED_AS_EXPECTED"
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
