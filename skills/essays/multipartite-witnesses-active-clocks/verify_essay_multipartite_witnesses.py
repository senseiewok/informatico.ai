#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.09 · Multipartite Witnesses, Scaling Tomography & Active Clocks.

Verifies:
  1. Exact 8x8 equilateral-prism Mermin law <M_3(t)> = eta^3 + 3 eta sin^2(Delta_phi(t)/2) matches
     8x8 density-matrix traces to < 1e-13 and reaches 3.6741 at T = 2.0 K (t_pi = 2.6120 s), clearing
     both the 2.0 3-local bound and the 2*sqrt(2) = 2.8284 biseparable GTE bound, while 3-body
     Diósi-Penrose hybrid dynamics obeys no-signalling, sigma_c^(1|23) = 34.93 um > 33.08 um
     (N_{1|23}^hyb = 0.0), log-grid max <M_3>_hyb = 0.9268 < 1.0, and collinear (x, y, x) nullity.
  2. Log-scaling & composition tomography: swapping 12C diamond for 173Yb at fixed (M, D, Delta_x, t)
     leaves passive Newtonian Delta_phi_Q invariant (1.0000x) while boosting sqrt(theta)_AH by 165.8x
     and theta_AH by 27,500x (det = 4.0 != 0), plus unitary revival at 2 t_pi vs Markovian decay.
  3. Active quantum clock proper-time phases (Zych 2011; Sorci 2026; Tobar, Aspelmeyer & Zych 2026)
     for 87Sr and 229Th transitions and exact Equivalence Principle ratio hbar*omega_clock / (M c^2).
  4. Comment-stripped AST & multivariate Fraction polynomial audit of MultipartiteWitness.lean:
     0 forbidden tokens, 0 unknown qualified IDs, >= 9 theorems, >= 7 universal quantifiers, and
     3/3 identically zero multivariate polynomials.
  5. ESSAY metadata, SEO bounds, 1750..2500 EN word count, <= 2 CFTR / cystic fibrosis mentions,
     12 pre-cached DOIs, SKILL.md frontmatter, zero banned phrases, and 100% EN / es-MX numeric parity.

Supports `--planted-defect`, which conflates the 2.0 LHV and 2.8284 biseparable bounds, applies naive
eta^3 damping to -X_i Z_j Z_k, drops the m_atom^2 composition exponent in Aziz-Howl, and injects a
`sorry` theorem into the Lean 4 audit buffer, exiting 1.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.essays.e09_multipartite_witnesses import (  # noqa: E402
    CODE,
    ESSAY,
    PLATE_SLUG,
    SLUG,
    evaluate_multipartite_synthesis,
    extract_number_tokens,
)

FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
MEDICAL_SEO_RE = re.compile(r"medical|médic|medic", re.I)
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
DECIMAL_COMMA_RE = re.compile(r"\d,\d{1,2}(?!\d)")
INLINE_DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s,;)\"']+")
ALLOWED_BLOCK_TYPES = {"p", "bridge", "analogy", "equation", "table"}

EXPECTED_DOIS = {
    "10.1103/physrevlett.119.240401",
    "10.1103/physrevlett.119.240402",
    "10.1103/physrevresearch.6.013199",
    "10.1103/physrevd.111.l121101",
    "10.1038/s41586-025-09595-7",
    "10.1088/1361-6382/ae6f62",
    "10.1038/s41467-023-43348-2",
    "10.1038/ncomms1498",
    "10.1103/qhj9-pc2b",
    "10.48550/arxiv.2611.08313",
    "10.22331/q-2021-07-06-497",
    "10.1016/j.cpc.2024.109457",
}

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
    syn = evaluate_multipartite_synthesis(planted_defect=planted_defect)
    tp = syn["tripartite_prism"]
    sc = syn["scaling_tomography"]
    clk = syn["active_clocks"]
    lean = syn["lean4_multipartite_spine"]

    # 1. Exact 8x8 equilateral-prism Mermin witness & 3-body Diósi-Penrose bounds
    assert tp["eotwash_bracket_verified"] and 33.00 <= tp["sigma_95_um"] <= 33.15, (
        f"Eöt-Wash sigma_95 bracket verification failed: {tp['sigma_95_um']:.4f} um"
    )
    assert tp["max_8x8_vs_closed_mermin_diff"] < 1.0e-13, (
        f"Position-Pointer Mermin formula drifted from 8x8 matrix trace: {tp['max_8x8_vs_closed_mermin_diff']:.3e}"
    )
    assert abs(tp["biseparable_bound"] - 2.0 * math.sqrt(2.0)) < 1.0e-12, (
        f"Biseparable GTE bound conflated with LHV bound: {tp['biseparable_bound']:.4f}"
    )
    assert 3.670 <= tp["mermin_2k_at_tpi"] <= 3.678 and tp["gte_certified_at_2k"], (
        f"2.0 K equilateral prism Mermin value out of range: {tp['mermin_2k_at_tpi']:.4f}"
    )
    assert tp["dp3_trace_error"] < 1.0e-14, f"3-body DP trace error: {tp['dp3_trace_error']:.3e}"
    assert tp["dp3_nosignal_decoupled_diff"] < 1.0e-14 and tp["dp3_nosignal_local_unitary_diff"] < 1.0e-14, (
        "3-body DP no-signalling / marginal reduction check failed"
    )
    assert 34.90 <= tp["sigma_c_1_23_um"] <= 34.96 and tp["sigma_c_1_23_um"] > tp["sigma_95_um"], (
        f"3-body collective sigma_c^(1|23) drifted from 34.93 um: {tp['sigma_c_1_23_um']:.4f} um"
    )
    assert tp["dp3_negativity_1_23_at_sigma95"] == 0.0 and tp["dp3_negativity_below_sc_34p8um"] == 0.0, (
        "3-body DP 1|23 negativity must vanish identically below sigma_c^(1|23) = 34.93 um"
    )
    assert tp["dp3_negativity_above_sc_35p15um"] > 1.0e-5, (
        "3-body DP 1|23 negativity must turn strictly positive above sigma_c^(1|23)"
    )
    assert tp["max_dp3_8x8_vs_closed_mermin_diff"] < 1.0e-13, (
        f"Closed-form DP3 Mermin drifted from 8x8 trace: {tp['max_dp3_8x8_vs_closed_mermin_diff']:.3e}"
    )
    assert 0.925 <= tp["dp3_mermin_log_grid_max"] <= 0.929 and tp["dp3_mermin_log_grid_max"] < 1.0, (
        f"DP3 Mermin log-grid max drifted from 0.9268: {tp['dp3_mermin_log_grid_max']:.4f}"
    )
    assert tp["collinear_xyx_nn_spread_m"] < 1.0e-15 and 0.47 <= tp["planar_xyz_spurious_phase_rad"] <= 0.48, (
        "3-D Euclidean null obstruction / collinear (x, y, x) stack check failed"
    )

    # 2. Log-scaling & 12C vs 173Yb composition tomography + unitary revival
    assert abs(sc["newtonian_yb_over_c12_ratio"] - 1.0) < 1.0e-15, "Newtonian phase violated Weak Equivalence Principle"
    assert 165.5 <= sc["aziz_sqrt_theta_yb_over_c12_ratio"] <= 166.2, (
        f"Aziz-Howl 173Yb / 12C sqrt(theta) boost drifted from 165.8x: {sc['aziz_sqrt_theta_yb_over_c12_ratio']:.4f}"
    )
    assert 27400.0 <= sc["aziz_theta_yb_over_c12_ratio"] <= 27600.0, (
        f"Aziz-Howl 173Yb / 12C theta boost drifted from 27,500x: {sc['aziz_theta_yb_over_c12_ratio']:.2f}"
    )
    assert sc["jacobian_det_m_matom"] == 4.0 and abs(sc["jacobian_det_m_t_theta"] + 8.0 / 3.0) < 1.0e-12
    assert sc["single_qubit_vis_tpi"] < 1.0e-14 and sc["single_qubit_vis_revival_2tpi"] > 0.88
    assert sc["markov_diffusive_vis_2tpi"] < 0.003

    # 3. Active quantum clocks & proper-time interferometry
    assert clk["sr87_optical"]["ep_ratio_diff"] < 1.0e-15 and clk["th229_nuclear"]["ep_ratio_diff"] < 1.0e-15
    assert 4.70 <= clk["th229_over_sr87_gain"] <= 4.72, f"Unexpected 229Th / 87Sr gain: {clk['th229_over_sr87_gain']:.4f}"
    assert abs(clk["compton_limit"]["dphi_source_mass_rad"] - 0.5 * math.pi) < 1.0e-12
    assert 4.0 <= clk["sr87_earth_null_split_m"] <= 4.2

    # 4. Lean 4 AST & multivariate Fraction polynomials
    assert not lean["forbidden_tokens"], f"Forbidden tokens in MultipartiteWitness.lean: {lean['forbidden_tokens']}"
    assert not lean["unknown_qualified_ids"], f"Unverified qualified IDs in MultipartiteWitness.lean: {lean['unknown_qualified_ids']}"
    assert lean["lean_compiler_ok"], f"Lean 4 compiler failed: {lean['lean_compiler_stderr']}"
    assert lean["theorem_count"] >= 9, f"Expected >= 9 theorems in MultipartiteWitness.lean, got {lean['theorem_count']}"
    assert lean["universal_quantifier_count"] >= 7, (
        f"Expected >= 7 universal quantifiers, got {lean['universal_quantifier_count']}"
    )
    assert lean["z2_ising_poly_zero"] and lean["lagrange_2d_poly_zero"] and lean["cramer_2d_poly_zero"], (
        "Multivariate Fraction polynomial identity check failed"
    )

    # 5. Monograph metadata, SEO, DOI cache, SKILL.md, banned phrases & EN/es-MX numeric parity
    assert ESSAY["code"] == "ES.09" and ESSAY["slug"] == "multipartite-witnesses-active-clocks" and ESSAY["plate_slug"] == "essay09"
    assert ESSAY["date"] == "2026-11-11"
    assert ESSAY["instrument"] == {"kind": "multipartite_witness"} and ESSAY["instrument_kind"] == "multipartite_witness"
    assert len(ESSAY["sections"]) == 5 and len(ESSAY["sidenotes"]) == 4 and len(ESSAY["predict"]["choices"]) == 3

    t_en, d_en, t_es, d_es = ESSAY["seo"]
    for t_str in (t_en, t_es):
        assert 18 <= len(t_str) <= 52, f"SEO title length {len(t_str)} outside 18..52: {t_str!r}"
        assert FORMULA_RE.search(t_str) is None and MEDICAL_SEO_RE.search(t_str) is None, f"SEO title rule failed: {t_str!r}"
    for d_str in (d_en, d_es):
        assert 110 <= len(d_str) <= 158 and d_str.endswith("."), f"SEO desc budget failed ({len(d_str)}): {d_str!r}"
        assert FORMULA_RE.search(d_str) is None and MEDICAL_SEO_RE.search(d_str) is None, f"SEO desc rule failed: {d_str!r}"
        last_w = re.findall(r"[\wÀ-ÿ]+", d_str)[-1].lower()
        assert last_w not in DANGLING_WORDS, f"Dangling end word in SEO desc: {d_str!r}"

    cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
    source_dois = {src["doi"].lower() for src in ESSAY["sources"]}
    assert len(ESSAY["sources"]) == 12 and source_dois == EXPECTED_DOIS, (
        f"ES.09 DOI set mismatch: {source_dois ^ EXPECTED_DOIS}"
    )
    for src in ESSAY["sources"]:
        key = "doi:" + src["doi"].lower()
        assert key in cache and cache[key].get("found"), f"Uncached DOI {src['doi']} in ES.09"

    skill_md = (ROOT / ESSAY["skill_path"]).read_text(encoding="utf-8")
    fm = _parse_frontmatter(skill_md)
    for req_key in ("name", "description", "license", "compatibility"):
        assert fm.get(req_key), f"SKILL.md missing frontmatter key {req_key}"

    block_types_seen = {blk["type"] for sec in ESSAY["sections"] for blk in sec["blocks"]}
    assert block_types_seen == ALLOWED_BLOCK_TYPES, f"Expected all 5 block types {ALLOWED_BLOCK_TYPES}, got {block_types_seen}"

    pairs = _collect_bilingual_pairs(ESSAY)
    en_words = 0
    p_blocks_total = 0
    cf_mentions = 0
    for label, en_txt, es_txt in pairs:
        if label.endswith(".p") or ".para[" in label:
            p_blocks_total += 1
            en_words += len(en_txt.split())
        if re.search(r"\bcystic fibrosis\b|\bfibrosis quística\b|\bcftr\b", en_txt + " " + es_txt, re.I):
            cf_mentions += 1
        assert DECIMAL_COMMA_RE.search(es_txt) is None, f"{label}: decimal comma in es-MX text: {es_txt!r}"
        assert INLINE_DOI_RE.search(en_txt) is None and INLINE_DOI_RE.search(es_txt) is None, f"{label}: raw inline DOI in prose"
        low_both = (en_txt + " " + es_txt).lower()
        for banned in BANNED_PHRASES:
            assert banned not in low_both, f"{label}: banned phrase {banned!r} found"
        toks_en = extract_number_tokens(en_txt)
        toks_es = extract_number_tokens(es_txt)
        assert toks_en == toks_es, f"{label}: EN/es-MX numeric parity mismatch: {toks_en} vs {toks_es}"

    assert 1750 <= en_words <= 2500, f"EN prose word count {en_words} outside 1750..2500"
    assert cf_mentions <= 2 and cf_mentions / max(1, p_blocks_total) <= 0.15, (
        f"CF/CFTR bridge mentions ({cf_mentions}/{p_blocks_total}) exceed cross-scale guardrail"
    )

    return {
        "status": "PASS",
        "essay_code": CODE,
        "slug": SLUG,
        "plate_slug": PLATE_SLUG,
        "en_prose_words": en_words,
        "bilingual_pairs_checked": len(pairs),
        "mermin_2k_at_tpi": round(tp["mermin_2k_at_tpi"], 4),
        "sigma_95_um": round(tp["sigma_95_um"], 3),
        "sigma_c_1_23_um": round(tp["sigma_c_1_23_um"], 3),
        "dp3_mermin_log_grid_max": round(tp["dp3_mermin_log_grid_max"], 4),
        "aziz_yb_over_c12_sqrt_theta_ratio": round(sc["aziz_sqrt_theta_yb_over_c12_ratio"], 2),
        "aziz_yb_over_c12_theta_ratio": round(sc["aziz_theta_yb_over_c12_ratio"], 1),
        "th229_over_sr87_gain": round(clk["th229_over_sr87_gain"], 3),
        "lean_theorem_count": lean["theorem_count"],
        "lean_universal_quantifiers": lean["universal_quantifier_count"],
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
