#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.11 · The Seven-Gate Crown Sieve.

Verifies (< 2.5 s normal + planted-defect runtime):
  1. Gate G5 (Chiral Anomaly & Domain-Wall Lock):
     - Unique integer weak hypercharges (1, -4, 2, -3, 6) and (1, 2, -4, -3, 6) over [-12, 12];
     - Zero integer roots at u = d = -1 when [Grav]^2 U(1)_Y = 0 is omitted, with continuous real
       irrational root e(0) = 54^(1/3) = 3.779763 (Minahan, Ramond & Warner 1990);
     - Gell-Mann-Nishijima 6 Q_em charges (+4, -2, 0, -6), proton +6, neutron 0, Hydrogen 0;
     - Spin(10) 15 + 1 = 16 Weyl spinor states, Tr(y_int^2) = 120, and Jackiw-Rebbi / Kaplan
       domain-wall zero-mode ODE residual < 1e-11.
  2. Gate G6 (Dark-Energy Horizon Scale, Null-Ray Vacuum Decoupling & Singlet Ladder):
     - Planck 2018 rho_Lambda = 5.24470e-10 J/m^3 (524,470 fJ/m^3), l_Lambda = 88.11 um, E_Lambda = 2.24 meV;
     - Kapner 2007 WMAP3 rho_Lambda = 6.08827e-10 J/m^3 (608,827 fJ/m^3), l_Lambda = 84.89 um;
     - Exact Jacobson / Weinberg null-ray decoupling (leak == 0.0 even at rho_vac = 1e113 J/m^3);
     - Bulk-singlet Compton ladder (hbar*c = 197.32698 meV*um, solar 22.92 um, atmospheric 3.94 um).
  3. Gate G7 (Entire Weierstrass UV Gravity & Eot-Wash / Mermin Bounds):
     - 400-node 3D spectral quadrature vs erf(r / 2 l_*) error < 1e-14 and finite V(0) prefactor 1/sqrt(pi);
     - Strictly monotone radial force ratio 0 < F_erf / F_N < 1 (|Delta F / F_N| <= 1 everywhere);
     - Schur-projected Eot-Wash 2020 bounds l_* = 32.98 um (signed) < 44.95 um (unsigned), M_* = 5.983 meV,
       3D FWHM = 77.66 um, and 75 / 32.98 = 2.2741 > 2.2109;
     - 2.0 K equilateral-prism Mermin witness ordering: 0.3227 <= 2.0 < 2.8284 < 3.6740 <= 3.6741.
  4. Eight-Architecture x Seven-Gate Crown Sieve & 12 Zero-Sorry Core Lean 4 Prelude Theorems:
     - Exact 8 Lean constructors, 2 six-gate EFT survivors, and unique 7-gate survivor
       ["nonlocal_chiral_horizon_crown"];
     - 0 imports, 0 forbidden tokens (sorry|sorryAx|admit|axiom), 0 vacuous x - x subtractions,
       0 unknown qualified IDs, live `lean` compiler check when present, all 12 required theorems,
       and 4/4 identically zero multivariate Fraction polynomials.
  5. ESSAY metadata, exact SEO tuple lengths/budgets, 1800..2400 EN prose words, zero banned phrases,
     zero privacy/lab leaks, zero `src/research/` legacy paths in SKILL.md, 16 cached Crossref DOIs,
     zero es-MX decimal commas, and 100% EN / es-MX extract_number_tokens parity.

Supports `--planted-defect`, which corrupts the anomaly lock, null-ray vacuum tensor, erf potential,
Eot-Wash l_* bound, and Lean 4 proof copy, exiting 1.
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

from folios.essays.e11_seven_gate_crown import (  # noqa: E402
    CODE,
    ESSAY,
    PLATE_SLUG,
    SLUG,
    evaluate_seven_gate_crown,
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
    "10.1016/0003-4916(75)90211-0",
    "10.1103/physrevd.13.3398",
    "10.1103/physrevd.16.953",
    "10.1103/revmodphys.61.1",
    "10.1103/physrevd.39.693",
    "10.1103/physrevd.41.715",
    "10.1016/0370-2693(92)91112-m",
    "10.1103/physrevlett.75.1260",
    "10.1103/physrevlett.83.4690",
    "10.1038/nature01997",
    "10.1103/physrevlett.98.021101",
    "10.1103/physrevlett.108.031101",
    "10.1103/physrevlett.114.158101",
    "10.1051/0004-6361/201833910",
    "10.1103/physrevlett.124.101101",
    "10.1103/physrevd.111.l121101",
)

EXPECTED_THEOREMS = (
    "seven_gate_crown_si_homogeneity",
    "sm_hypercharge_uniqueness",
    "pure_gauge_fermat_and_vectorlike_branch",
    "gell_mann_nishijima_hydrogen_neutrality",
    "spin10_weyl_and_jackiw_rebbi_chirality",
    "jacobson_null_ray_vacuum_decoupling",
    "vacuum_length_scale_window_ordering",
    "stelle_ghost_vs_weierstrass_positivity",
    "erf_uv_origin_regularization_positivity",
    "nonlocal_lstar_eotwash_and_mermin_island",
    "six_gate_eft_survivors",
    "seven_gate_crown_unique_corridor",
)

EXPECTED_LEAN_CONSTRUCTORS = (
    "scalarSheet",
    "stelleBox2",
    "classicalDPHybrid",
    "fatGraviton85um",
    "pureGaugeIrrationalSM",
    "flatCircleKK5D",
    "canonicalQuantumGREFT",
    "nonlocalChiralHorizonCrown",
)

BANNED_PHRASES = (
    "unifies",
    "unify",
    "unification",
    "unifying",
    "unifica",
    "unificación",
    "unificada",
    "unificando",
    "unificar",
    "theory of everything",
    "teoría del todo",
    "solves the information paradox",
    "resolves the information paradox",
    "resuelve la paradoja de la información",
    "gravity is a slope in time",
    "our " + "lab",
    "nuestro " + "laboratorio",
    "sensei" + "ewok",
    "cystic " + "fibrosis",
    "fibrosis " + "quística",
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
    syn = evaluate_seven_gate_crown(planted_defect=planted_defect)
    kernel_s = time.perf_counter() - t0
    assert kernel_s < 2.2, f"evaluate_seven_gate_crown exceeded 2.2 s speed budget: {kernel_s:.3f} s"

    g14 = syn["mesoscopic_gates_g1_g4"]
    g5 = syn["gate_g5_chiral_fermat"]
    g6 = syn["gate_g6_dark_energy_null_horizon"]
    g7 = syn["gate_g7_entire_uv_gravity"]
    lean = syn["lean4_seven_gate_spine"]

    # 1. Gate G5: Chiral hypercharge uniqueness, Fermat irrational branch, Hydrogen neutrality & Spin(10)
    assert g5["integer_sm_roots"] == [(1, -4, 2, -3, 6), (1, 2, -4, -3, 6)], (
        f"Unexpected integer SM hypercharge roots: {g5['integer_sm_roots']}"
    )
    assert g5["pure_gauge_u_eq_d_integer_roots"] == []
    assert abs(g5["pure_gauge_e_at_u_eq_d_irrational"] - (54.0 ** (1.0 / 3.0))) < 1.0e-5
    assert g5["mrw_cubic_residual_t0"] < 1.0e-12 and g5["mrw_cubic_residual_t3"] == 0.0
    q6 = g5["q6_charges"]
    assert (q6["u_L"], q6["d_L"], q6["nu_L"], q6["e_L"]) == (4, -2, 0, -6)
    assert q6["proton"] == 6 and q6["neutron"] == 0 and q6["hydrogen_atom"] == 0
    assert g5["weyl_sm_states"] == 15 and g5["spin10_chiral_spinor_states"] == 16
    assert g5["trace_yint_squared"] == 120
    assert g5["domain_wall_dirac_residual"] < 1.0e-11 and g5["mirror_mode_at_w5"] > 5000.0

    # 2. Gate G6: Dark-energy fourth-root length scale, null-ray decoupling & bulk-singlet ladder
    assert g6["rho_lambda_planck18_fJ_per_m3"] == 524470
    assert abs(g6["l_lambda_planck18_um"] - 88.11) <= 0.02
    assert abs(g6["e_lambda_planck18_meV"] - 2.24) <= 0.01
    assert g6["rho_lambda_kapner07_fJ_per_m3"] == 608827
    assert abs(g6["l_lambda_kapner07_um"] - 84.89) <= 0.02
    assert g6["max_null_ray_vacuum_leak"] == 0.0, f"Null-ray vacuum energy leaked: {g6['max_null_ray_vacuum_leak']}"
    assert abs(g6["neutrino_solar_compton_um"] - 22.92) <= 0.02
    assert abs(g6["neutrino_atmos_compton_um"] - 3.94) <= 0.02
    assert g6["neutrino_atmos_compton_um"] < g6["neutrino_solar_compton_um"] < 32.98 < g6["l_lambda_kapner07_um"] < g6["l_lambda_planck18_um"]

    # 3. Gate G7: Entire Weierstrass UV potential, bounded force softening, Eot-Wash bounds & Mermin GTE
    assert g7["fourier_erf_quadrature_err"] < 1.0e-14, (
        f"3D spectral quadrature vs erf(r / 2 l_*) error >= 1e-14: {g7['fourier_erf_quadrature_err']:.3e}"
    )
    assert g7["origin_v0_prefactor_err"] < 1.0e-12
    assert g7["strictly_monotone_force_ratio"] and 0.0 < g7["max_abs_force_deficit_ratio"] <= 1.0
    assert 32.90 <= g7["lstar_95_signed_um"] <= 33.05, f"Signed l_* bound drifted from 32.98 um: {g7['lstar_95_signed_um']}"
    assert 44.85 <= g7["lstar_95_unsigned_um"] <= 45.05, f"Unsigned l_* bound drifted from 44.95 um: {g7['lstar_95_unsigned_um']}"
    assert g7["lstar_95_signed_um"] < g7["lstar_95_unsigned_um"] < g6["l_lambda_kapner07_um"]
    assert abs(g7["m_star_min_meV"] - 5.983) <= 0.005
    assert abs(g7["fwhm_3d_max_um"] - 77.66) <= 0.05
    assert g7["mermin_island_ratio_75_over_lstar"] > 2.2109

    assert 43478.5 <= g14["cassini_scalar_rejection_sigma"] <= 43479.8
    assert g14["tur_1pct_min_atp"] == 1000.0
    mw = g7["mermin_M3_witnesses"]
    gte_bound = 2.0 * math.sqrt(2.0)
    assert 0.30 <= mw["classical_dp_hybrid_2K"] <= 0.35 and mw["classical_dp_hybrid_2K"] <= 2.0
    assert mw["nonlocal_entire_lstar18_2K"] > gte_bound and 3.672 <= mw["nonlocal_entire_lstar18_2K"] <= 3.6741
    assert mw["unitary_gr_2K"] >= mw["nonlocal_entire_lstar18_2K"] and 3.673 <= mw["unitary_gr_2K"] <= 3.678

    # 4. Eight-Architecture x Seven-Gate Crown Sieve & 12 Lean 4 Prelude Theorems
    models = syn["candidate_models_sieve"]
    assert tuple(m["lean_constructor"] for m in models) == EXPECTED_LEAN_CONSTRUCTORS
    assert syn["six_gate_eft_survivor_ids"] == ["canonical_quantum_gr_eft", "nonlocal_chiral_horizon_crown"]
    assert syn["seven_gate_crown_survivor_ids"] == ["nonlocal_chiral_horizon_crown"]

    assert not lean["has_import"], "SevenGateCrown.lean must be pure Lean 4 Prelude with zero imports"
    assert not lean["forbidden_tokens"], f"Forbidden tokens in SevenGateCrown.lean: {lean['forbidden_tokens']}"
    assert not lean["has_vacuous_self_sub"], "Vacuous x - x self-subtraction detected in SevenGateCrown.lean"
    assert not lean["unknown_qualified_ids"], f"Unverified qualified IDs in SevenGateCrown.lean: {lean['unknown_qualified_ids']}"
    assert lean["lean_compiler_ok"], f"Lean 4 compiler failed: {lean['lean_compiler_stderr']}"
    assert tuple(lean["theorem_names"]) == EXPECTED_THEOREMS, (
        f"Theorem roster mismatch in SevenGateCrown.lean: {lean['theorem_names']}"
    )
    assert lean["theorem_count"] == 12
    assert lean["universal_quantifier_count"] >= 10
    assert (
        lean["geng_marshak_fermat_poly_zero"]
        and lean["jacobson_null_vacuum_poly_zero"]
        and lean["stelle_partial_fraction_poly_zero"]
        and lean["erf_uv_square_completion_poly_zero"]
    ), "Multivariate Fraction polynomial identity check failed"

    lean_raw_low = (ROOT / "skills" / "essays" / SLUG / "SevenGateCrown.lean").read_text(encoding="utf-8").lower()
    for banned in BANNED_PHRASES:
        assert banned not in lean_raw_low, f"SevenGateCrown.lean contains banned phrase {banned!r}"

    # 5. Monograph metadata, SEO, DOI cache, SKILL.md, banned phrases & EN/es-MX numeric parity
    assert ESSAY["code"] == "ES.11" and ESSAY["slug"] == "seven-gate-crown-sieve"
    assert ESSAY["skill_dir"] == "seven-gate-crown-sieve" and ESSAY["verifier"] == "verify_essay_seven_gate_crown.py"
    assert ESSAY["plate_slug"] == "essay11" and ESSAY["plate"] == "essay11"
    assert ESSAY["date"] == "2026-11-11" and ESSAY["published"] == "2026-11-11"
    assert ESSAY["instrument"] == {"kind": "seven_gate_crown"} and ESSAY["instrument_kind"] == "seven_gate_crown"
    assert len(ESSAY["sections"]) == 5 and len(ESSAY["sidenotes"]) == 4 and len(ESSAY["predict"]["choices"]) == 3

    t_en, d_en, t_es, d_es = ESSAY["seo"]
    assert t_en == "The Seven-Gate Crown Sieve" and len(t_en) == 26
    assert (
        d_en
        == "Seven physical gates eliminate gravitational and gauge architectures, leaving ghost-free entire UV gravity and chiral spinors as sole survivors."
        and len(d_en) == 144
    )
    assert t_es == "La Criba Corona de Siete Compuertas" and len(t_es) == 35
    assert (
        d_es
        == "Siete compuertas físicas filtran arquitecturas de gravedad y norma, dejando la gravedad entera sin fantasmas y espinores quirales como sobrevivientes."
        and len(d_es) == 150
    )
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
        assert key in cache and cache[key].get("found"), f"Uncached DOI {src['doi']} in ES.11"
        rec = cache[key]
        assert rec["first_author"].lower() in src["citation"].lower(), (
            f"Source {src['id']} citation missing Crossref first_author {rec['first_author']!r}"
        )
        assert abs(int(src["year"]) - int(rec["year"])) <= 2, f"Source {src['id']} year mismatch vs Crossref"

    skill_md = (ROOT / ESSAY["skill_path"]).read_text(encoding="utf-8")
    fm = _parse_frontmatter(skill_md)
    for req_key in ("name", "description", "license", "compatibility"):
        assert fm.get(req_key), f"SKILL.md missing frontmatter key {req_key}"
    assert "src/research/" not in skill_md and "/research/essays/" not in skill_md, (
        "SKILL.md must use flattened docroot paths (no legacy src/research/ or /research/essays/)"
    )
    assert "https://informatico.ai/essays/seven-gate-crown-sieve/" in skill_md
    assert "src/modules/cross-scale-essays.mjs" in skill_md
    assert MEDICAL_RE.search(skill_md) is None, "Medical term found in SKILL.md"
    low_skill = skill_md.lower()
    for banned in BANNED_PHRASES:
        assert banned not in low_skill, f"SKILL.md contains banned phrase {banned!r}"

    pairs = _collect_bilingual_pairs(ESSAY)
    en_words = 0
    for label, en_txt, es_txt in pairs:
        if label.endswith(".p") or ".para[" in label:
            en_words += len(en_txt.split())
        combined_txt = en_txt + " " + es_txt
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

    return {
        "status": "PASS",
        "essay_code": CODE,
        "slug": SLUG,
        "plate_slug": PLATE_SLUG,
        "kernel_seconds": round(kernel_s, 3),
        "en_prose_words": en_words,
        "bilingual_pairs_checked": len(pairs),
        "sm_hypercharge_roots": g5["integer_sm_roots"],
        "pure_gauge_irrational_e": g5["pure_gauge_e_at_u_eq_d_irrational"],
        "l_lambda_planck18_um": g6["l_lambda_planck18_um"],
        "l_lambda_kapner07_um": g6["l_lambda_kapner07_um"],
        "neutrino_solar_compton_um": g6["neutrino_solar_compton_um"],
        "lstar_95_signed_um": g7["lstar_95_signed_um"],
        "lstar_95_unsigned_um": g7["lstar_95_unsigned_um"],
        "mermin_m3_entire18_2k": mw["nonlocal_entire_lstar18_2K"],
        "six_gate_eft_survivors": syn["six_gate_eft_survivor_ids"],
        "seven_gate_crown_survivors": syn["seven_gate_crown_survivor_ids"],
        "lean_theorem_count": lean["theorem_count"],
        "lean_compiler_checked": lean["lean_compiler_checked"],
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
    assert report["total_seconds"] < 2.5, f"Total verifier runtime exceeded 2.5 s: {report['total_seconds']} s"
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
