#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.06 · Coupled Timeless Constraints & Zero-Sorry Formal Proof.

Verifies:
  1. 64x64 Hermitian Wheeler-DeWitt / Page-Wootters nullspace on H_C^(16) (x) H_path^(2) (x) H_tick^(2)
     and H_C^(16) (x) H_A^(2) (x) H_B^(2) via 128x128 real Jacobi diagonalization (||C|Psi>>|| < 1e-13,
     kernel projection = 1.0000000000, conditioned visibility error < 1e-13) + physical 429.228 THz
     optical 87Sr clock (first zero 10.68 m*s, exact Quantum Equivalence Principle eta = 0).
  2. Updated 33 um (sigma_95 = 33.08 um <= 33.5 um) Eot-Wash signed Yukawa recast, 4-wall hybrid
     exclusion across all published geometries (including Schut 2024 z=30 um at 39.4 um > 33.1 um and
     Wall 4 elimination of z=10 um at gamma = 1e-3 s^-1), and Oppenheim's (2023) 3.31e16x torque-residual
     momentum-diffusion suppression below the Cavendish ceiling.
  3. Synchronous bilateral X_A (x) X_B vs unilateral X_A (x) I CPMG spin-echo physics: unilateral pulses
     erase gravitational entanglement to 0, bilateral pulses preserve +Z_A Z_B and suppress quasistatic
     stray gradient rates as 1 / N_dd^2, while memoryless white Markovian Lindblad dephasing stays 1x invariant.
  4. Comment-stripped AST & multivariate Fraction polynomial audit of IRUG_Unification.lean: 0 forbidden
     tokens (sorry|sorryAx|admit|axiom), >= 8 theorems, >= 4 universal quantifiers, sigma_95_recast_um = 33,
     zero retired 44067, zero vacuous self-subtractions, and 4/4 identically zero multivariate polynomials.
  5. ESSAY metadata, SEO bounds, 1800..2600 EN word count, <= 2 CFTR / cystic fibrosis mentions (< 10%
     of <p> blocks), >= 9 pre-cached Crossref DOIs, SKILL.md frontmatter, and 100% EN / es-MX numeric parity.

Supports `--planted-defect`, which activates anharmonic k^2+1 clock modes, the retired 44.07 um edge match,
unilateral X_A (x) I pulses, and an injected `sorry` theorem, and must exit non-zero (1).
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

from folios.essays.e06_coupled_constraints_proof import (  # noqa: E402
    CODE,
    ESSAY,
    PLATE_SLUG,
    SLUG,
    evaluate_coupled_synthesis,
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
                pairs.append((f"section[{s_idx}].block[{b_idx}].label", blk["label_en"], blk["label_es"]))
                pairs.append((f"section[{s_idx}].block[{b_idx}].note", blk["note_en"], blk["note_es"]))
            elif btype == "table":
                pairs.append((f"section[{s_idx}].block[{b_idx}].caption", blk["caption_en"], blk["caption_es"]))
                assert len(blk["headers_en"]) == len(blk["headers_es"]), "Table header length mismatch"
                for h_idx, (h_en, h_es) in enumerate(zip(blk["headers_en"], blk["headers_es"])):
                    pairs.append((f"section[{s_idx}].block[{b_idx}].header[{h_idx}]", h_en, h_es))
                for r_idx, row in enumerate(blk["rows"]):
                    assert len(row) == len(blk["headers_en"]), "Table row column count mismatch"
                    for c_idx, (c_en, c_es) in enumerate(row):
                        pairs.append((f"section[{s_idx}].block[{b_idx}].cell[{r_idx}][{c_idx}]", c_en, c_es))
    for n_idx, sn in enumerate(essay["sidenotes"]):
        pairs.append((f"sidenote[{n_idx}].label", sn["label_en"], sn["label_es"]))
        pairs.append((f"sidenote[{n_idx}].body", sn["en"], sn["es"]))
    for src_idx, src in enumerate(essay["sources"]):
        pairs.append((f"source[{src_idx}].role", src["role_en"], src["role_es"]))
    return pairs


def verify_metadata_and_parity() -> dict:
    required_keys = {
        "code", "slug", "plate_slug", "date", "seo",
        "kicker_en", "kicker_es", "reading_time_en", "reading_time_es",
        "title_en", "title_es", "standfirst_en", "standfirst_es",
        "card_dek_en", "card_dek_es", "instrument_kind", "predict",
        "sections", "sidenotes", "sources", "skill_path", "verifier_path",
        "ai_line_en", "ai_line_es",
    }
    missing = required_keys - set(ESSAY.keys())
    assert not missing, f"Missing ESSAY keys: {sorted(missing)}"

    assert ESSAY["code"] == "ES.06"
    assert ESSAY["slug"] == "coupled-constraints-formal-proof"
    assert ESSAY["plate_slug"] == "essay06"
    assert ESSAY["instrument_kind"] == "wdw_clock"
    assert ESSAY["date"] == "2026-11-10"
    assert ESSAY["skill_path"] == "skills/essays/coupled-constraints-formal-proof/SKILL.md"
    assert ESSAY["verifier_path"] == "skills/essays/coupled-constraints-formal-proof/verify_essay_coupled_constraints.py"
    assert len(ESSAY["sections"]) == 5
    assert 4 <= len(ESSAY["sidenotes"]) <= 5
    assert len(ESSAY["sources"]) >= 9

    # SEO checks
    t_en, d_en, t_es, d_es = ESSAY["seo"]
    assert t_en != t_es, "SEO titles must be distinct between EN and ES"
    for label, title in (("title_en", t_en), ("title_es", t_es)):
        assert 18 <= len(title) <= 52, f"{label} length {len(title)} out of [18, 52]: {title!r}"
        assert "informatico" not in title.lower(), f"{label} must not include brand suffix"
    for label, desc in (("desc_en", d_en), ("desc_es", d_es)):
        assert 110 <= len(desc) <= 158, f"{label} length {len(desc)} out of [110, 158]: {desc!r}"
        assert desc.endswith("."), f"{label} must end with period: {desc!r}"
        assert FORMULA_RE.search(desc) is None, f"{label} contains formula symbol: {desc!r}"
        assert "medical" not in desc.lower() and "médic" not in desc.lower(), f"{label} contains forbidden word"
        last_word = re.findall(r"[\wÀ-ÿ]+", desc)[-1].lower()
        assert last_word not in DANGLING_WORDS, f"{label} ends on dangling word {last_word!r}"

    # Word count & proportional CF framing checks
    roman_prefixes = ("I · ", "II · ", "III · ", "IV · ", "V · ")
    prose_words_en = 0
    all_words_en = 0
    p_blocks_total = 0
    p_blocks_with_cf = 0
    en_chunks: list[str] = [ESSAY["title_en"], ESSAY["standfirst_en"], ESSAY["card_dek_en"]]
    es_chunks: list[str] = [ESSAY["title_es"], ESSAY["standfirst_es"], ESSAY["card_dek_es"]]

    for idx, sec in enumerate(ESSAY["sections"]):
        assert sec["h2_en"].startswith(roman_prefixes[idx]), f"Section {idx + 1} h2_en prefix mismatch"
        assert sec["h2_es"].startswith(roman_prefixes[idx]), f"Section {idx + 1} h2_es prefix mismatch"
        all_words_en += len(sec["h2_en"].split())
        en_chunks.append(sec["h2_en"])
        es_chunks.append(sec["h2_es"])
        for blk in sec["blocks"]:
            btype = blk["type"]
            if btype == "p":
                p_blocks_total += 1
                if re.search(r"\b(cftr|cystic\s+fibrosis)\b", blk["en"], flags=re.IGNORECASE):
                    p_blocks_with_cf += 1
                w = len(blk["en"].split())
                prose_words_en += w
                all_words_en += w
                en_chunks.append(blk["en"])
                es_chunks.append(blk["es"])
            elif btype in ("bridge", "analogy"):
                all_words_en += len(blk["kicker_en"].split()) + len(blk["title_en"].split())
                en_chunks.extend([blk["kicker_en"], blk["title_en"]])
                es_chunks.extend([blk["kicker_es"], blk["title_es"]])
                for p_en, p_es in blk["paras"]:
                    p_blocks_total += 1
                    if re.search(r"\b(cftr|cystic\s+fibrosis)\b", p_en, flags=re.IGNORECASE):
                        p_blocks_with_cf += 1
                    w = len(p_en.split())
                    prose_words_en += w
                    all_words_en += w
                    en_chunks.append(p_en)
                    es_chunks.append(p_es)
            elif btype == "equation":
                all_words_en += len(blk["label_en"].split()) + len(blk["note_en"].split())
                en_chunks.extend([blk["label_en"], blk["note_en"]])
                es_chunks.extend([blk["label_es"], blk["note_es"]])
            elif btype == "table":
                all_words_en += len(blk["caption_en"].split()) + sum(len(h.split()) for h in blk["headers_en"])
                all_words_en += sum(len(c_en.split()) for row in blk["rows"] for c_en, _ in row)
                en_chunks.append(blk["caption_en"])
                es_chunks.append(blk["caption_es"])
                for row in blk["rows"]:
                    for c_en, c_es in row:
                        en_chunks.append(c_en)
                        es_chunks.append(c_es)

    assert 1800 <= prose_words_en <= 2600, f"English prose words {prose_words_en} outside [1800, 2600]"
    assert 1800 <= all_words_en <= 2600, f"English total section words {all_words_en} outside [1800, 2600]"

    for sn in ESSAY["sidenotes"]:
        en_chunks.append(sn["en"])
        es_chunks.append(sn["es"])

    full_en = " ".join(en_chunks)
    full_es = " ".join(es_chunks)
    cf_en = len(re.findall(r"cystic\s+fibrosis", full_en, flags=re.IGNORECASE))
    cftr_en = len(re.findall(r"\bcftr\b", full_en, flags=re.IGNORECASE))
    cf_es = len(re.findall(r"fibrosis\s+qu[ií]stica", full_es, flags=re.IGNORECASE))
    assert cf_en <= 2 and cftr_en <= 2 and cf_es <= 2, (
        f"CF/CFTR mention cap exceeded: cf_en={cf_en}, cftr_en={cftr_en}, cf_es={cf_es}"
    )
    cf_p_ratio = p_blocks_with_cf / max(p_blocks_total, 1)
    assert cf_p_ratio < 0.10, f"CF paragraph fraction {cf_p_ratio:.3f} >= 0.10 ({p_blocks_with_cf}/{p_blocks_total})"

    # Ensure retired 44.067 um is never claimed as current bound
    assert "44.067" not in full_en and "44.067" not in full_es, "Superseded 44.067 um bound must not appear"

    prose_no_filename_en = re.sub(r"IRUG_Unification\.lean", "", full_en, flags=re.IGNORECASE)
    prose_no_filename_es = re.sub(r"IRUG_Unification\.lean", "", full_es, flags=re.IGNORECASE)
    for phrase in BANNED_PHRASES:
        pat = re.compile(rf"\b{re.escape(phrase)}\b", flags=re.IGNORECASE)
        assert pat.search(prose_no_filename_en) is None, f"Banned overclaim phrase {phrase!r} in EN"
        assert pat.search(prose_no_filename_es) is None, f"Banned overclaim phrase {phrase!r} in ES"

    # Offline DOI cache gate
    cache_path = ROOT / "data" / "folio-citations.cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8"))
    seen_dois: set[str] = set()
    for src in ESSAY["sources"]:
        doi = src["doi"].strip().lower()
        doi_key = f"doi:{doi}"
        assert doi_key in cache and cache[doi_key].get("found") is True, f"Uncached DOI: {src['doi']}"
        seen_dois.add(doi)
    for inline_doi in set(INLINE_DOI_RE.findall(full_en + " " + full_es)):
        cleaned = inline_doi.rstrip(".,;:)")
        assert f"doi:{cleaned.lower()}" in cache, f"Uncached inline DOI: {cleaned}"

    # SKILL.md &Lean file presence + frontmatter gate
    skill_path = ROOT / ESSAY["skill_path"]
    lean_path = skill_path.parent / "IRUG_Unification.lean"
    assert skill_path.is_file(), f"Missing SKILL.md: {skill_path}"
    assert lean_path.is_file(), f"Missing IRUG_Unification.lean: {lean_path}"
    fm = _parse_frontmatter(skill_path.read_text(encoding="utf-8"))
    assert fm.get("name") == "essay-es06-coupled-constraints-formal-proof"
    assert fm.get("license") == "MIT"
    assert fm.get("description") and fm.get("compatibility")

    # 100% EN / es-MX numeric parity + es-MX decimal point rule
    pairs = _collect_bilingual_pairs(ESSAY)
    for label, en_txt, es_txt in pairs:
        toks_en = extract_number_tokens(en_txt)
        toks_es = extract_number_tokens(es_txt)
        assert toks_en == toks_es, f"Numeric parity mismatch in {label}: EN={toks_en} vs ES={toks_es}"
        assert DECIMAL_COMMA_RE.search(es_txt) is None, f"Forbidden decimal comma in es-MX ({label}): {es_txt!r}"

    return {
        "prose_words_en": prose_words_en,
        "all_section_words_en": all_words_en,
        "bilingual_pairs_checked": len(pairs),
        "cached_sources_verified": len(seen_dois),
        "cf_mentions_en": cf_en,
        "cftr_mentions_en": cftr_en,
        "cf_paragraph_fraction": round(cf_p_ratio, 4),
        "seo_lengths": {
            "title_en": len(t_en),
            "desc_en": len(d_en),
            "title_es": len(t_es),
            "desc_es": len(d_es),
        },
    }


def verify_physics_and_lean(planted_defect: bool = False) -> dict:
    res = evaluate_coupled_synthesis(planted_defect=planted_defect)
    wdw1 = res["wdw_zych_64d"]
    wdw2 = res["wdw_bmv_64d"]
    sr = res["physical_sr_qep"]
    walls = res["four_wall_and_oppenheim"]
    cpmg = res["bilateral_cpmg"]
    lean = res["lean4_formal_spine"]

    # Pillar 1: 64x64 Hermitian Wheeler-DeWitt nullspace (128x128 real Jacobi) + 87Sr QEP
    for tag, wdw in (("zych_64d", wdw1), ("bmv_64d", wdw2)):
        assert wdw["dim_complex"] == 64 and wdw["dim_real_jacobi"] == 128
        assert wdw["off_diagonal_frobenius_norm"] > 25.0, f"{tag} matrix is trivially diagonal"
        assert wdw["constraint_residual_norm"] < 1.0e-13, (
            f"{tag} Wheeler-DeWitt residual {wdw['constraint_residual_norm']:.3e} >= 1e-13 (planted k^2+1 defect active)"
        )
        assert abs(wdw["kernel_projection"] - 1.0) < 1.0e-10, (
            f"{tag} Jacobi kernel projection {wdw['kernel_projection']:.10f} != 1.0"
        )
        assert wdw["visibility_max_err"] < 1.0e-13, f"{tag} conditioned visibility error {wdw['visibility_max_err']:.3e}"

    assert 1.09e-16 < sr["dtau_1m_1s_s"] < 1.10e-16
    assert 0.989 < sr["visibility_1m_1s"] < 0.990
    assert sr["visibility_double_entry_diff"] < 1.0e-12
    assert 10.67 < sr["first_zero_dh_t_m_s"] < 10.69
    assert abs(sr["qep_eotvos_eta"]) < 1.0e-25, f"Non-zero QEP Eotvos parameter {sr['qep_eotvos_eta']}"

    # Pillar 2: Updated 33 um recast + 4-Wall Hybrid Exclusion + Oppenheim torque suppression
    assert 32.5 < walls["recast_sigma_95_um"] < 33.5, (
        f"Recast sigma_95 = {walls['recast_sigma_95_um']:.3f} um outside [32.5, 33.5] (retired 44.07 um defect active)"
    )
    assert walls["at_33um_excluded"] is False
    assert walls["at_35um_excluded"] is True
    sc = walls["hybrid_sigma_c_um"]
    assert sc["bose2017"] > 500.0 and sc["chevalier2020"] > 400.0
    assert sc["vandekamp2020_47"] > 80.0 and sc["vandekamp2020_24"] > 50.0
    assert sc["schut2024_z30"] > walls["recast_sigma_95_um"], "z=30 um must be excluded by 33 um recast"
    assert sc["schut2024_z10"] < walls["recast_sigma_95_um"]

    deph = walls["schut2024_z10_dephasing"]
    assert deph["hybrid_33um_gamma_crit_s1"] < 1.0e-4 < 1.0e-3 < deph["quantum_gamma_crit_s1"]
    assert deph["hybrid_33um_peak_negativity_at_1e-3"] == 0.0
    assert 0.33 < deph["quantum_peak_negativity_at_1e-3"] < 0.35

    opp = walls["oppenheim"]
    assert 3.00e-26 < opp["eotwash_T1e3_rN1fm_ceiling"] < 3.05e-26
    assert 3.30e16 < opp["suppression_vs_printed_1fm"] < 3.32e16
    assert opp["suppression_vs_printed_7fm"] > 9.0e13
    assert opp["eotwash_T1e3_rN1fm_ceiling"] > opp["interferometry_floor_kg2_s_m"]

    # Pillar 3: Synchronous bilateral X_A (x) X_B vs unilateral X_A (x) I CPMG + Markovian invariance
    assert abs(cpmg["unilateral_echo"]["dphi_eff_rad"]) < 1.0e-12
    assert cpmg["unilateral_echo"]["negativity"] == 0.0
    assert cpmg["bilateral_echo"]["negativity"] > 0.30, (
        f"Bilateral CPMG negativity {cpmg['bilateral_echo']['negativity']:.6f} collapsed (unilateral pulse defect active)"
    )
    assert cpmg["bilateral_echo"]["negativity"] > 2.4 * cpmg["free_evolution"]["negativity"]
    assert cpmg["bilateral_echo"]["static_gradient_residual_s"] < 1.0e-12
    assert abs(cpmg["gamma_lowf_cpmg_s1"] - cpmg["gamma_lowf_raw_s1"] / 16.0) < 1.0e-16
    assert cpmg["markovian_invariance_abs_diff"] < 1.0e-14

    # Pillar 4: Zero-sorry Lean 4 AST, qualified-Prelude allowlist, optional live Lean kernel & polynomial check
    assert len(lean["forbidden_tokens"]) == 0, f"Forbidden tokens in IRUG_Unification.lean: {lean['forbidden_tokens']}"
    assert len(lean["unknown_qualified_ids"]) == 0, (
        f"Unverified/non-Prelude qualified identifiers in IRUG_Unification.lean: {lean['unknown_qualified_ids']}"
    )
    assert lean["lean_compiler_ok"] is True, f"Lean 4 compiler rejected IRUG_Unification.lean: {lean['lean_compiler_stderr']}"
    assert lean["theorem_count"] >= 8, f"Expected >= 8 Lean theorems, found {lean['theorem_count']}"
    assert lean["universal_quantifier_count"] >= 4, (
        f"Expected >= 4 universal quantifiers, found {lean['universal_quantifier_count']}"
    )
    assert lean["has_recast_33"] is True, "IRUG_Unification.lean missing sigma_95_recast_um = 33"
    assert lean["has_retired_44067"] is False, "IRUG_Unification.lean still references retired 44067"
    assert lean["has_vacuous_self_sub"] is False, "IRUG_Unification.lean contains vacuous x - x expression"
    assert lean["qep_polynomial_zero"] is True
    assert lean["stoica_polynomial_zero"] is True
    assert lean["bilateral_echo_polynomial_zero"] is True
    assert lean["maxwell_calladine_polynomial_zero"] is True

    return res


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        meta = verify_metadata_and_parity()
        phys = verify_physics_and_lean(planted_defect=planted)
        payload = {
            "status": "PASS",
            "folio_id": CODE,
            "essay": CODE,
            "slug": SLUG,
            "plate_slug": PLATE_SLUG,
            "verified_benchmarks": {
                "wdw_zych_residual_norm": phys["wdw_zych_64d"]["constraint_residual_norm"],
                "wdw_zych_kernel_projection": round(phys["wdw_zych_64d"]["kernel_projection"], 10),
                "wdw_bmv_residual_norm": phys["wdw_bmv_64d"]["constraint_residual_norm"],
                "wdw_bmv_kernel_projection": round(phys["wdw_bmv_64d"]["kernel_projection"], 10),
                "sr87_first_zero_dh_t_m_s": round(phys["physical_sr_qep"]["first_zero_dh_t_m_s"], 6),
                "qep_eotvos_eta": phys["physical_sr_qep"]["qep_eotvos_eta"],
                "recast_sigma_95_um": round(phys["four_wall_and_oppenheim"]["recast_sigma_95_um"], 4),
                "oppenheim_cavendish_over_eotwash": phys["four_wall_and_oppenheim"]["oppenheim"]["suppression_vs_printed_1fm"],
                "cpmg_unilateral_negativity": phys["bilateral_cpmg"]["unilateral_echo"]["negativity"],
                "cpmg_bilateral_negativity": round(phys["bilateral_cpmg"]["bilateral_echo"]["negativity"], 6),
                "cpmg_markovian_diff": phys["bilateral_cpmg"]["markovian_invariance_abs_diff"],
                "lean_theorem_count": phys["lean4_formal_spine"]["theorem_count"],
                "lean_universal_quantifiers": phys["lean4_formal_spine"]["universal_quantifier_count"],
                "lean_zero_sorry": len(phys["lean4_formal_spine"]["forbidden_tokens"]) == 0,
            },
            "metadata_checks": meta,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    except AssertionError as exc:
        print(
            json.dumps(
                {
                    "status": "FAIL",
                    "folio_id": CODE,
                    "essay": CODE,
                    "slug": SLUG,
                    "planted_defect": planted,
                    "error": str(exc),
                },
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
