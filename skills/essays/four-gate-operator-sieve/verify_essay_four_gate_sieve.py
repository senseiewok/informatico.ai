#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.10 · The Four-Gate Operator Sieve Across Scales.

Verifies (< 2.0 s normal + planted-defect runtime):
  1. 310.15 K d = 2 Helfrich lipid bilayer Green's difference Delta G_2(r) Hankel quadrature vs
     exact K_0(r / l_b) (< 1e-6 relative error), UV cancellation (< 1e-20 at 1e-15 l_b), resting/tense
     healing lengths (65.44 nm, 9.25 nm), Goulian-Bruinsma-Pincus 1-loop attraction (-0.07407 k_B T),
     and Barato-Seifert 1% TUR dissipation floor (20,000 k_B = 1,000 ATP).
  2. Overflow-free closed-form 3D combined (sigma, l_b) sheet kernel R_brane(q, s; sigma, l_b) vs
     6,000-step cosine quadrature (< 1e-11), 3D isotropic potential vs Simpson quadrature (< 1e-7),
     and the 6-point Schur-orthogonal 95% exclusion contour on Lee et al. (2020) Table 11.4:
       - sigma = 0 um: signed 27.22 um vs unsigned 38.47 um;
       - monotone contraction [27.22, 25.47, 23.34, 20.01, 16.22, 7.83] um across [0, 10, 18, 24, 28, 32] um.
  3. Sign split (-17.67% spatial bending vs +22.19% warped RS-II KK tail at 52 um, l = 30 um;
     +6.06e-62 Donoghue 1-loop at 75 um), 3.68e54 [N / N] Einstein-to-lipid pinching-force ratio,
     43,479.2 sigma Cassini PPN scalar rejection, 2.0 K equilateral-prism Mermin witness ordering
     (0.3227 <= 2.0 < 2.8284 < 3.6504 < 3.6741), and exact 2 unconditional survivors
     (["warped_rs2_brane", "canonical_quantum_gr"]).
  4. Comment-stripped AST & multivariate Fraction polynomial audit of FourGateSieve.lean:
     0 imports, 0 forbidden tokens (sorry|sorryAx|admit|axiom), 0 vacuous x - x self-subtractions,
     0 unknown qualified identifiers, all 10 required theorems, >= 8 universal quantifiers, and
     3/3 identically zero multivariate polynomials (partial_fraction_poly_zero, sheet_branch1_poly_zero,
     sheet_branch2_poly_zero).
  5. ESSAY metadata, exact SEO tuple lengths/regexes/dangling-word gates, 1800..2400 EN prose words,
     <= 2 CF / CFTR mentions (<= 1 CFTR mention), zero medical/médic terms, zero banned unification
     phrases ("unifies", "unify", "unification", "unifica", "unificación", "unificada"), 13 pre-cached
     Crossref DOIs, SKILL.md YAML frontmatter, zero es-MX decimal commas, and 100% EN / es-MX
     extract_number_tokens parity.

Supports `--planted-defect`, which flips the spatial bending sign (+second instead of -second,
corrupting the sheet quadrature, sign split, and 27.22 um signed contour) and injects a `sorry`
theorem into the Lean 4 audit copy, exiting 1.
"""
from __future__ import annotations

import json
import math
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

from folios.essays.e10_four_gate_sieve import (  # noqa: E402
    CODE,
    ESSAY,
    PLATE_SLUG,
    SLUG,
    evaluate_four_gate_sieve,
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
    "10.1515/znc-1973-11-1209",
    "10.1209/0295-5075/22/2/012",
    "10.1103/physrevlett.114.158101",
    "10.1103/physrevd.16.953",
    "10.1103/physrevlett.72.2996",
    "10.1103/physrevlett.75.1260",
    "10.1103/physrevlett.83.4690",
    "10.1103/physrevlett.84.2778",
    "10.1038/nature01997",
    "10.1103/physrevlett.98.021101",
    "10.1103/physrevd.79.084008",
    "10.1103/physrevlett.124.101101",
    "10.1103/physrevd.111.l121101",
)

EXPECTED_THEOREMS = (
    "four_gate_sieve_si_homogeneity",
    "partial_fraction_uv_split",
    "combined_sheet_exponent_cancellation",
    "gauss_flux_dimension_scaling",
    "sign_split_bending_vs_warped_kk",
    "signed_vs_unsigned_bound_tightening",
    "cassini_scalar_rejection_43479_sigma",
    "pinching_force_hierarchy_10_54",
    "mermin_gte_window_separation",
    "four_gate_sieve_survivors",
)

BANNED_PHRASES = (
    "unifies",
    "unify gravity",
    "unification of gravity",
    "unification",
    "unify",
    "proves the theory of everything",
    "theory of everything is",
    "solves the information paradox",
    "resolves the information paradox",
    "unifica",
    "unificación",
    "unificada",
    "unificar",
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
    syn = evaluate_four_gate_sieve(planted_defect=planted_defect)
    kernel_s = time.perf_counter() - t0
    assert kernel_s < 2.5, f"evaluate_four_gate_sieve exceeded 2.5 s speed budget: {kernel_s:.3f} s"

    bio = syn["biophysics_scale_310K"]
    grav = syn["spacetime_scale_2K"]
    lean = syn["lean4_four_gate_spine"]

    # 1. 310.15 K Helfrich 2D bilayer & TUR dissipated clock checks
    assert bio["helfrich_2d_hankel_vs_k0_rel_err"] < 1.0e-6, (
        f"2D Helfrich Hankel quadrature relative error >= 1e-6: {bio['helfrich_2d_hankel_vs_k0_rel_err']:.3e}"
    )
    assert abs(bio["helfrich_2d_uv_zero"]) < 1.0e-20, (
        f"2D Helfrich UV cancellation failed at 1e-15 l_b: {bio['helfrich_2d_uv_zero']:.3e}"
    )
    assert abs(bio["healing_length_resting_nm"] - 65.44) <= 0.02
    assert abs(bio["healing_length_tense_nm"] - 9.25) <= 0.02
    assert abs(bio["gbp_1loop_casimir_at_7p5nm_kBT"] - (-0.07407)) < 1.0e-4
    assert abs(bio["lipid_pinching_force_pN"] - 1.309) <= 0.002
    assert bio["tur_1pct_min_entropy_kB"] == 20000.0 and bio["tur_1pct_min_atp"] == 1000.0

    # 2. Combined 3D (sigma, l_b) sheet kernel & 6-point Schur-orthogonal Eot-Wash contour
    assert grav["combined_sheet_kernel_quadrature_err"] < 1.0e-11, (
        f"Combined (sigma, l_b) sheet kernel quadrature error >= 1e-11: {grav['combined_sheet_kernel_quadrature_err']:.3e}"
    )
    assert grav["combined_3d_isotropic_quadrature_err"] < 1.0e-7, (
        f"Combined 3D isotropic potential quadrature error >= 1e-7: {grav['combined_3d_isotropic_quadrature_err']:.3e}"
    )

    contour = grav["joint_sigma_lb_95_contour_um"]
    assert len(contour) == 6, f"Expected 6 joint (sigma, l_b) contour points, got {len(contour)}"
    c0 = contour[0]
    assert c0["sigma_um"] == 0.0
    assert 27.10 <= c0["lb_95_signed_um"] <= 27.35, f"sigma=0 signed l_b bound drifted from 27.22 um: {c0['lb_95_signed_um']}"
    assert 38.35 <= c0["lb_95_unsigned_um"] <= 38.60, f"sigma=0 unsigned l_b bound drifted from 38.47 um: {c0['lb_95_unsigned_um']}"
    assert c0["lb_95_signed_um"] < c0["lb_95_unsigned_um"]
    signed_curve = [pt["lb_95_signed_um"] for pt in contour]
    for prev_lb, next_lb in zip(signed_curve[:-1], signed_curve[1:]):
        assert next_lb < prev_lb, f"Signed l_{{b,95}}(sigma) contour failed strict monotone contraction: {signed_curve}"
    assert 7.50 <= contour[-1]["lb_95_signed_um"] <= 8.15, f"sigma=32 um signed l_b bound drifted from 7.83 um: {contour[-1]}"
    assert contour[-1]["lb_95_signed_um"] < contour[-1]["lb_95_unsigned_um"]

    # 3. Sign split, 3.68e54 force hierarchy, 43,479 sigma Cassini razor, Mermin witness & 4-gate survivors
    ss = grav["sign_split_at_52um"]
    assert abs(ss["spatial_bending_lb30um_frac_shift"] - (-0.1767)) <= 0.0005, (
        f"Spatial bending shift at 52 um drifted from -0.1767: {ss['spatial_bending_lb30um_frac_shift']}"
    )
    assert abs(ss["warped_rs2_lAdS30um_frac_shift"] - 0.2219) <= 0.0005, (
        f"Warped RS-II shift at 52 um drifted from +0.2219: {ss['warped_rs2_lAdS30um_frac_shift']}"
    )
    assert ss["spatial_bending_lb30um_frac_shift"] < 0.0 < ss["warped_rs2_lAdS30um_frac_shift"]
    assert 6.0e-62 <= ss["donoghue_1loop_qg_at_75um_frac_shift"] <= 6.2e-62

    assert 3.67e54 <= grav["dimensionless_force_ratio_N_over_N"] <= 3.69e54
    assert grav["log10_force_ratio"] == 54.57
    assert 43478.5 <= grav["cassini_scalar_rejection_sigma"] <= 43479.8

    mw = grav["mermin_M3_witnesses"]
    gte_bound = 2.0 * math.sqrt(2.0)
    assert 0.30 <= mw["classical_dp_hybrid_2K"] <= 0.35 and mw["classical_dp_hybrid_2K"] <= 2.0
    assert mw["quantum_brane_sigma18_lb18_2K"] > gte_bound and 3.645 <= mw["quantum_brane_sigma18_lb18_2K"] <= 3.655
    assert mw["unitary_gr_2K"] > mw["quantum_brane_sigma18_lb18_2K"] and 3.670 <= mw["unitary_gr_2K"] <= 3.678

    assert syn["unconditional_survivor_ids"] == ["warped_rs2_brane", "canonical_quantum_gr"], (
        f"Unexpected 4-gate unconditional survivors: {syn['unconditional_survivor_ids']}"
    )

    # 4. Lean 4 Prelude AST & 3 multivariate Fraction polynomials
    assert not lean["has_import"], "FourGateSieve.lean must be pure Lean 4 Prelude with zero imports"
    assert not lean["forbidden_tokens"], f"Forbidden tokens in FourGateSieve.lean: {lean['forbidden_tokens']}"
    assert not lean["has_vacuous_self_sub"], "Vacuous x - x self-subtraction detected in FourGateSieve.lean"
    assert not lean["unknown_qualified_ids"], f"Unverified qualified IDs in FourGateSieve.lean: {lean['unknown_qualified_ids']}"
    assert lean["lean_compiler_ok"], f"Lean 4 compiler failed: {lean['lean_compiler_stderr']}"
    assert tuple(lean["theorem_names"]) == EXPECTED_THEOREMS, (
        f"Theorem roster mismatch in FourGateSieve.lean: {lean['theorem_names']}"
    )
    assert lean["theorem_count"] == 10
    assert lean["universal_quantifier_count"] >= 8, (
        f"Expected >= 8 universal quantifiers in FourGateSieve.lean, got {lean['universal_quantifier_count']}"
    )
    assert (
        lean["partial_fraction_poly_zero"]
        and lean["sheet_branch1_poly_zero"]
        and lean["sheet_branch2_poly_zero"]
    ), "Multivariate Fraction polynomial identity check failed"

    # 5. Monograph metadata, SEO, DOI cache, SKILL.md, banned phrases & EN/es-MX numeric parity
    assert ESSAY["code"] == "ES.10" and ESSAY["slug"] == "four-gate-operator-sieve"
    assert ESSAY["plate_slug"] == "essay10" and ESSAY["date"] == "2026-11-11"
    assert ESSAY["instrument"] == {"kind": "four_gate_sieve"} and ESSAY["instrument_kind"] == "four_gate_sieve"
    assert len(ESSAY["sections"]) == 5 and len(ESSAY["sidenotes"]) == 4 and len(ESSAY["predict"]["choices"]) == 3

    t_en, d_en, t_es, d_es = ESSAY["seo"]
    assert t_en == "The Four-Gate Operator Sieve Across Scales" and len(t_en) == 42
    assert t_es == "La Criba de Operadores de Cuatro Compuertas" and len(t_es) == 43
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
        assert key in cache and cache[key].get("found"), f"Uncached DOI {src['doi']} in ES.10"

    skill_md = (ROOT / ESSAY["skill_path"]).read_text(encoding="utf-8")
    fm = _parse_frontmatter(skill_md)
    for req_key in ("name", "description", "license", "compatibility"):
        assert fm.get(req_key), f"SKILL.md missing frontmatter key {req_key}"
    assert MEDICAL_RE.search(skill_md) is None, "Medical term found in SKILL.md"
    low_skill = skill_md.lower()
    for banned in BANNED_PHRASES:
        assert banned not in low_skill, f"SKILL.md contains banned phrase {banned!r}"

    pairs = _collect_bilingual_pairs(ESSAY)
    en_words = 0
    cf_mentions = 0
    cftr_mentions = 0
    for label, en_txt, es_txt in pairs:
        if label.endswith(".p") or ".para[" in label:
            en_words += len(en_txt.split())
        combined_txt = en_txt + " " + es_txt
        if re.search(r"\bcystic fibrosis\b|\bfibrosis quística\b|\bcftr\b", combined_txt, re.I):
            cf_mentions += 1
        if re.search(r"\bcftr\b", combined_txt, re.I):
            cftr_mentions += 1
        assert MEDICAL_RE.search(combined_txt) is None, f"{label}: medical/médic term found"
        assert DECIMAL_COMMA_RE.search(es_txt) is None, f"{label}: decimal comma in es-MX text: {es_txt!r}"
        assert INLINE_DOI_RE.search(en_txt) is None and INLINE_DOI_RE.search(es_txt) is None, f"{label}: raw inline DOI in prose"
        low_both = combined_txt.lower()
        for banned in BANNED_PHRASES:
            assert banned not in low_both, f"{label}: banned phrase {banned!r} found"
        toks_en = extract_number_tokens(en_txt)
        toks_es = extract_number_tokens(es_txt)
        assert toks_en == toks_es, f"{label}: EN/es-MX numeric parity mismatch: {toks_en} vs {toks_es}"

    assert 1800 <= en_words <= 2400, f"EN prose word count {en_words} outside 1800..2400"
    assert cf_mentions <= 2, f"CF / CFTR mentions ({cf_mentions}) exceed <= 2 cross-scale cap"
    assert cftr_mentions <= 1, f"CFTR mentions ({cftr_mentions}) exceed <= 1 cap"

    return {
        "status": "PASS",
        "essay_code": CODE,
        "slug": SLUG,
        "plate_slug": PLATE_SLUG,
        "kernel_seconds": round(kernel_s, 3),
        "en_prose_words": en_words,
        "cf_mentions_total": cf_mentions,
        "cftr_mentions_total": cftr_mentions,
        "bilingual_pairs_checked": len(pairs),
        "lb95_signed_sigma0_um": c0["lb_95_signed_um"],
        "lb95_unsigned_sigma0_um": c0["lb_95_unsigned_um"],
        "lb95_signed_sigma32_um": contour[-1]["lb_95_signed_um"],
        "force_hierarchy_ratio": f"{grav['dimensionless_force_ratio_N_over_N']:.3e}",
        "cassini_scalar_rejection_sigma": grav["cassini_scalar_rejection_sigma"],
        "mermin_m3_gr_2k": mw["unitary_gr_2K"],
        "mermin_m3_qbrane_18_2k": mw["quantum_brane_sigma18_lb18_2K"],
        "mermin_m3_dp_2k": mw["classical_dp_hybrid_2K"],
        "unconditional_survivors": syn["unconditional_survivor_ids"],
        "lean_theorem_count": lean["theorem_count"],
    }


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    t_total = time.perf_counter()
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
    report["total_seconds"] = round(time.perf_counter() - t_total, 3)
    assert report["total_seconds"] < 3.0, f"Total verifier runtime exceeded 3.0 s: {report['total_seconds']} s"
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
