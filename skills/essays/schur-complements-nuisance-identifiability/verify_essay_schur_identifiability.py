#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.08 · Schur Complements & Nuisance Identifiability.

Verifies:
  1. Modified Gram-Schmidt W-orthonormality (< 1e-13) and projector idempotence (< 1e-14) on the
     2020 Eöt-Wash 120-fold wedge recast across 52 um to 3000 um:
       - Equal weights (W = I): raw sigma_95 = 33.08 um (alpha_eff = -7.302, residual 2.38%) vs
         Schur-projected sigma_95^perp = 32.98 um (alpha_eff = -7.383 < -7.360, residual 2.20%,
         cos theta_perp = 0.999758, norm 82.05%, Fisher retention 67.32%).
       - Constant-torque-noise weights (W = diag(T_N^2)): raw sigma_95 = 33.01 um vs Schur-projected
         sigma_95^perp = 32.87 um (32.85 um exact root; alpha_eff = -7.534 < -7.360, residual 1.14%,
         cos theta_perp = 0.999935, norm 45.77%, Fisher retention 20.95%), preserving 2.2109 sigma_95 < 75.00 um.
  2. Saturated 3-point Carathéodory / Kiefer-Wolfowitz D-optimal design on [25 um, 3000 um]
     (support [25.00 um, 101.01 um, 3000.00 um], equal weights 1/3, max directional variance <= 3.0 + 1e-9
     and 3.0 at all 3 support points) plus sub-50 um Schur Fisher gains (5.36x at 35 um, 13.20x at 25 um).
  3. Standardized 3x3 correlation Fisher spectra (Tr = 3.00) and Schur retention across Eöt-Wash
     wedges, Folio E.07 sparse/PDE bridge PINNs (1004x PDE boost), Folio M.08 trichromatic cones,
     and 2-site allosteric rescue (10.14x 2-D checkerboard Schur Fisher boost).
  4. Comment-stripped AST & multivariate Fraction polynomial audit of SchurIdentifiability.lean:
     0 forbidden tokens (sorry|sorryAx|admit|axiom), 0 vacuous self-subtractions, 0 unknown qualified
     identifiers, >= 9 theorems, >= 7 universal quantifiers, and 3/3 zero multivariate polynomials.
  5. ESSAY metadata, SEO character/symbol/medical/dangling gates, 1750..2500 EN prose word count,
     <= 2 cystic fibrosis / CFTR mentions, 10 pre-cached Crossref DOIs, SKILL.md YAML frontmatter,
     zero banned phrases, and 100% EN / es-MX numeric token parity.

Supports `--planted-defect`, which omits nuisance projection (substituting raw Fisher info and the
retired 44.07 um single-gap match), breaks Kiefer-Wolfowitz weights to [0.8, 0.1, 0.1], and injects
a `sorry` theorem into the Lean 4 audit copy, exiting 1.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.essays.e08_schur_identifiability import (  # noqa: E402
    CODE,
    ESSAY,
    PLATE_SLUG,
    SLUG,
    evaluate_schur_synthesis,
    extract_number_tokens,
)

FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
MEDICAL_RE = re.compile(r"medical|médic|medic", re.I)
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
DECIMAL_COMMA_RE = re.compile(r"\d,\d{1,2}(?!\d)")
INLINE_DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s,;)\"']+")
ALLOWED_BLOCK_TYPES = {"p", "bridge", "analogy", "equation", "table"}

EXPECTED_DOIS = (
    "10.1103/physrevlett.124.101101",
    "10.1088/1361-6382/abebf2",
    "10.1103/physrevd.78.022002",
    "10.1103/physrevlett.124.051301",
    "10.1103/physrevd.111.l121101",
    "10.1038/s41586-021-03250-7",
    "10.1016/j.jcp.2018.10.045",
    "10.1364/josa.32.000247",
    "10.1172/jci.insight.139983",
    "10.1016/j.cpc.2024.109457",
)

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
    t0 = time.perf_counter()
    syn = evaluate_schur_synthesis(planted_defect=planted_defect)
    kernel_s = time.perf_counter() - t0
    assert kernel_s < 6.0, f"evaluate_schur_synthesis exceeded 6.0 s budget: {kernel_s:.2f} s"

    ew = syn["eotwash_schur"]
    kw = syn["kiefer_wolfowitz_design"]
    cs = syn["cross_scale_sloppy_fisher"]
    lean = syn["lean4_schur_spine"]

    # 1. Eöt-Wash raw vs Schur-projected recast + Gram-Schmidt stability
    eq = ew["equal_weights"]
    ab = ew["abs_torque_weights"]
    assert 33.04 <= eq["raw_sigma_95_um"] <= 33.12, f"Unexpected equal raw sigma_95: {eq['raw_sigma_95_um']}"
    assert 32.95 <= eq["schur_sigma_95_um"] <= 32.99, f"Equal Schur sigma_95 outside 32.95..32.99 um: {eq['schur_sigma_95_um']}"
    assert abs(eq["raw_at_33um"]["alpha_eff"] - (-7.30157)) < 0.01
    assert abs(eq["schur_at_33um"]["alpha_eff"] - (-7.38271)) < 0.01 and eq["schur_at_33um"]["excluded"]
    assert abs(eq["schur_at_33um"]["shape_residual"] - 0.0220) < 0.001
    assert abs(eq["schur_at_33um"]["cos_theta_perp"] - 0.999758) < 2.0e-5
    assert abs(eq["schur_at_33um"]["retained_norm_fraction"] - 0.8205) < 0.002
    assert abs(eq["schur_at_33um"]["fisher_retention_ratio"] - 0.6732) < 0.002

    assert 32.99 <= ab["raw_sigma_95_um"] <= 33.05, f"Unexpected abs_torque raw sigma_95: {ab['raw_sigma_95_um']}"
    assert 32.85 <= ab["schur_sigma_95_um"] <= 32.95, f"abs_torque Schur sigma_95 outside 32.85..32.95 um: {ab['schur_sigma_95_um']}"
    assert abs(ab["schur_at_33um"]["alpha_eff"] - (-7.53372)) < 0.01 and ab["schur_at_33um"]["excluded"]
    assert abs(ab["schur_at_33um"]["shape_residual"] - 0.0114) < 0.001
    assert abs(ab["schur_at_33um"]["cos_theta_perp"] - 0.999935) < 1.0e-5
    assert abs(ab["schur_at_33um"]["retained_norm_fraction"] - 0.4577) < 0.002
    assert abs(ab["schur_at_33um"]["fisher_retention_ratio"] - 0.2095) < 0.002

    assert ew["gram_schmidt_max_orthonormality_err"] < 1.0e-13, (
        f"Gram-Schmidt W-orthonormality error >= 1e-13: {ew['gram_schmidt_max_orthonormality_err']:.3e}"
    )
    assert ew["projector_max_idempotence_err"] < 1.0e-14, (
        f"Projector idempotence error >= 1e-14: {ew['projector_max_idempotence_err']:.3e}"
    )
    assert ew["preserves_75um_quantum_island"] and ew["max_parallel_ceiling_um"] < 73.5, (
        f"Parallel hybrid ceiling breached 75 um quantum island: {ew['max_parallel_ceiling_um']}"
    )

    # 2. Kiefer-Wolfowitz saturated 3-point D-optimal design + sub-50 um Schur Fisher gain
    d3 = kw["d_optimal_3pt"]
    supp = d3["support_separations_um"]
    assert abs(supp[0] - 25.0) < 1.0e-6 and 95.0 <= supp[1] <= 115.0 and abs(supp[2] - 3000.0) < 1.0e-4
    assert all(abs(w - 1.0 / 3.0) < 1.0e-12 for w in d3["support_weights"]), f"Non-equal D-optimal weights: {d3['support_weights']}"
    assert d3["max_directional_variance"] <= 3.0 + 1.0e-9 and d3["kiefer_wolfowitz_certified"], (
        f"Kiefer-Wolfowitz directional variance ceiling violated: max d(s) = {d3['max_directional_variance']}"
    )
    assert all(abs(dv - 3.0) < 1.0e-9 for dv in d3["support_directional_variances"]), (
        f"Support directional variances drifted from 3.0: {d3['support_directional_variances']}"
    )
    assert 5.30 <= kw["gain_35um_over_52um"] <= 5.42, f"Unexpected 35 um Schur Fisher gain: {kw['gain_35um_over_52um']}"
    assert 13.15 <= kw["gain_25um_over_52um"] <= 13.25, f"Unexpected 25 um Schur Fisher gain: {kw['gain_25um_over_52um']}"

    # 3. Cross-scale standardized 3x3 sloppy Fisher spectra
    assert abs(cs["eotwash_abs_torque"]["schur_retention_ratio"] - ab["schur_at_33um"]["fisher_retention_ratio"]) < 1.0e-12
    assert cs["pinn_pde_retention_gain"] > 900.0, f"Expected > 900x PINN PDE Schur boost, got {cs['pinn_pde_retention_gain']}"
    assert 0.10 <= cs["macadam_lms_color"]["schur_retention_ratio"] <= 0.12
    assert cs["allosteric_2d_fisher_gain"] > 9.5 and cs["allosteric_2d_retention_gain"] > 6.0

    # 4. Lean 4 AST & multivariate Fraction polynomials
    assert not lean["forbidden_tokens"], f"Forbidden tokens in SchurIdentifiability.lean: {lean['forbidden_tokens']}"
    assert not lean["has_vacuous_self_sub"], "Vacuous x - x self-subtraction detected in SchurIdentifiability.lean"
    assert not lean["unknown_qualified_ids"], f"Unverified qualified IDs in SchurIdentifiability.lean: {lean['unknown_qualified_ids']}"
    assert lean["lean_compiler_ok"], f"Lean 4 compiler failed: {lean['lean_compiler_stderr']}"
    assert lean["theorem_count"] >= 9, f"Expected >= 9 theorems in SchurIdentifiability.lean, got {lean['theorem_count']}"
    assert lean["universal_quantifier_count"] >= 7, f"Expected >= 7 universal quantifiers, got {lean['universal_quantifier_count']}"
    assert (
        lean["lagrange_cauchy_schwarz_poly_zero"]
        and lean["gram_schmidt_annihilation_poly_zero"]
        and lean["orthogonal_pythagoras_poly_zero"]
    ), "Multivariate Fraction polynomial identity check failed"

    # 5. Monograph metadata, SEO, DOI cache, SKILL.md, banned phrases & EN/es-MX numeric parity
    assert ESSAY["code"] == "ES.08" and ESSAY["slug"] == "schur-complements-nuisance-identifiability"
    assert ESSAY["plate_slug"] == "essay08" and ESSAY["date"] == "2026-11-11"
    assert ESSAY["instrument"] == {"kind": "schur_recast"} and ESSAY["instrument_kind"] == "schur_recast"
    assert len(ESSAY["sections"]) == 5 and len(ESSAY["sidenotes"]) == 4 and len(ESSAY["predict"]["choices"]) == 3

    t_en, d_en, t_es, d_es = ESSAY["seo"]
    for t_str in (t_en, t_es):
        assert 18 <= len(t_str) <= 52, f"SEO title length {len(t_str)} outside 18..52: {t_str!r}"
        assert FORMULA_RE.search(t_str) is None and MEDICAL_RE.search(t_str) is None
    for d_str in (d_en, d_es):
        assert 110 <= len(d_str) <= 158 and d_str.endswith("."), f"SEO desc budget failed ({len(d_str)}): {d_str!r}"
        assert FORMULA_RE.search(d_str) is None, f"Formula symbol in SEO desc: {d_str!r}"
        assert MEDICAL_RE.search(d_str) is None, f"Medical term in SEO desc: {d_str!r}"
        last_w = re.findall(r"[\wÀ-ÿ]+", d_str)[-1].lower()
        assert last_w not in DANGLING_WORDS, f"Dangling end word in SEO desc: {d_str!r}"

    cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
    actual_dois = tuple(src["doi"] for src in ESSAY["sources"])
    assert actual_dois == EXPECTED_DOIS, f"DOI list mismatch: {actual_dois}"
    for src in ESSAY["sources"]:
        key = "doi:" + src["doi"].lower()
        assert key in cache and cache[key].get("found"), f"Uncached DOI {src['doi']} in ES.08"

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
    assert cf_mentions <= 2, f"CF / CFTR mentions ({cf_mentions}) exceed <= 2 cross-scale cap"

    return {
        "status": "PASS",
        "essay_code": CODE,
        "slug": SLUG,
        "plate_slug": PLATE_SLUG,
        "kernel_seconds": round(kernel_s, 3),
        "en_prose_words": en_words,
        "cf_mentions_total": cf_mentions,
        "bilingual_pairs_checked": len(pairs),
        "schur_sigma_95_equal_um": round(eq["schur_sigma_95_um"], 3),
        "schur_sigma_95_abs_torque_um": round(ab["schur_sigma_95_um"], 3),
        "fisher_retention_abs_torque": round(ab["schur_at_33um"]["fisher_retention_ratio"], 4),
        "kiefer_wolfowitz_max_d": round(d3["max_directional_variance"], 6),
        "sub50um_gain_25um": round(kw["gain_25um_over_52um"], 2),
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
