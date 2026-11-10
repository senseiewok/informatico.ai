#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.01 · The Mesoscopic Floor.

Verifies:
  1. Universal Fluctuation-Dissipation identity D_p = gamma_m * M * k_B * T across both
     cryogenic ultra-high vacuum (Kn >> 1) and warm liquid water (Kn << 1).
  2. Knudsen / Cunningham-Epstein crossover across 19.6 decades of Kn = lambda_mfp / R.
  3. Short-wavelength single-collision saturation of 4.0 K helium gas decoherence
     (lambda_th = 0.436 nm << Delta_x, Delta_x^0 plateau, exact 8*pi/3 cited-to-kinetic
     ratio, and exact agreement with tools/timegravity_kernel_decoherence.py) versus
     long-wavelength thermal-photon dipole localization (lambda_bb = 1228 um >> Delta_x,
     Gamma_ph propto Delta_x^2, Lambda_sc propto R^6 T^9, Lambda_em propto R^3 T^6).
  4. Continuum Stokes-Einstein diffusivity at 310.15 K (D_0 = 6.58 um^2/s for R = 50 nm)
     and Ogston-Amsden polymer-mesh steric hindrance D_eff / D_0 across xi = 300 nm,
     120 nm, 70 nm, and 63 nm.
  5. ESSAY schema, SEO bounds, cached Crossref DOIs, proportional framing, and 100%
     EN / es-MX numeric token parity.

Supports `--planted-defect`, which activates naive long-wavelength Delta_x^2 gas scaling
and un-hindered hydrogel transport and must exit non-zero (1).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.essays.e01_mesoscopic import (  # noqa: E402
    BODY_TEMP_K,
    CRYO_TEMP_K,
    DIAMOND_DENSITY_KG_M3,
    DIAMOND_MASS_QGEM_KG,
    ESSAY,
    HYDROGEL_FIBER_RADIUS_M,
    K_B,
    NANOPARTICLE_RADIUS_M,
    QGEM_SPLIT_M,
    UHV_PRESSURE_PA,
    WATER_VISCOSITY_310K_PA_S,
    cunningham_slip_factor,
    evaluate_mesoscopic_floor,
    photon_lambda_emission,
    photon_lambda_scattering,
    sphere_radius,
)
from timegravity_kernel_decoherence import (  # noqa: E402
    gas_rate_saturated as tg_gas_rate_saturated,
    photon_rate as tg_photon_rate,
)

FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
NUM_TOKEN_RE = re.compile(r"\d+(?:\.\d+)?|[⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]+")
ALLOWED_BLOCK_TYPES = {"p", "bridge", "analogy", "equation", "table"}


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
                    for c_idx, (c_en, c_es) in enumerate(row):
                        pairs.append((f"section[{s_idx}].block[{b_idx}].cell[{r_idx}][{c_idx}]", c_en, c_es))
    for n_idx, sn in enumerate(essay["sidenotes"]):
        pairs.append((f"sidenote[{n_idx}].label", sn["label_en"], sn["label_es"]))
        pairs.append((f"sidenote[{n_idx}].body", sn["en"], sn["es"]))
    for src_idx, src in enumerate(essay["sources"]):
        pairs.append((f"source[{src_idx}].role", src["role_en"], src["role_es"]))
    return pairs


def verify_metadata_and_parity() -> dict:
    assert ESSAY["code"] == "ES.01"
    assert ESSAY["slug"] == "mesoscopic-floor"
    assert ESSAY["plate_slug"] == "essay01"
    assert ESSAY["instrument_kind"] == "mesoscopic"
    assert len(ESSAY["sections"]) == 5
    assert 4 <= len(ESSAY["sidenotes"]) <= 5
    assert 8 <= len(ESSAY["sources"]) <= 10

    t_en, d_en, t_es, d_es = ESSAY["seo"]
    for label, title in (("title_en", t_en), ("title_es", t_es)):
        assert 18 <= len(title) <= 50, f"{label} length {len(title)} out of [18, 50]: {title!r}"
        assert "Informatico.ai" not in title, f"{label} must not include brand suffix"
    for label, desc in (("desc_en", d_en), ("desc_es", d_es)):
        assert 115 <= len(desc) <= 152, f"{label} length {len(desc)} out of [115, 152]: {desc!r}"
        assert desc.endswith("."), f"{label} must end with period: {desc!r}"
        assert FORMULA_RE.search(desc) is None, f"{label} contains formula symbol: {desc!r}"
        assert "medical" not in desc.lower() and "médic" not in desc.lower(), f"{label} contains forbidden word"
        last_word = re.findall(r"[\wÀ-ÿ]+", desc)[-1].lower()
        assert last_word not in DANGLING_WORDS, f"{label} ends on dangling word {last_word!r}"

    # Word count check across sections (both prose-only and all-blocks must sit in 1800..2600)
    prose_words_en = 0
    all_words_en = 0
    for sec in ESSAY["sections"]:
        all_words_en += len(sec["h2_en"].split())
        for blk in sec["blocks"]:
            btype = blk["type"]
            if btype == "p":
                w = len(blk["en"].split())
                prose_words_en += w
                all_words_en += w
            elif btype in ("bridge", "analogy"):
                all_words_en += len(blk["kicker_en"].split()) + len(blk["title_en"].split())
                for p_en, _ in blk["paras"]:
                    w = len(p_en.split())
                    prose_words_en += w
                    all_words_en += w
            elif btype == "equation":
                all_words_en += len(blk["label_en"].split()) + len(blk["note_en"].split())
            elif btype == "table":
                all_words_en += len(blk["caption_en"].split()) + sum(len(h.split()) for h in blk["headers_en"])
                all_words_en += sum(len(c_en.split()) for row in blk["rows"] for c_en, _ in row)
    assert 1800 <= prose_words_en <= 2600, f"English prose words {prose_words_en} outside [1800, 2600]"
    assert 1800 <= all_words_en <= 2600, f"English total section words {all_words_en} outside [1800, 2600]"

    # Citation cache gate
    cache_path = ROOT / "data" / "folio-citations.cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8"))
    for src in ESSAY["sources"]:
        doi_key = f"doi:{src['doi'].strip().lower()}"
        assert doi_key in cache and cache[doi_key].get("found") is True, f"Uncached DOI: {src['doi']}"

    # Proportional framing guardrail
    raw_src = (ROOT / "tools" / "folios" / "essays" / "e01_mesoscopic.py").read_text(encoding="utf-8")
    cf_mentions = len(re.findall(r"cystic fibrosis", raw_src, flags=re.IGNORECASE))
    assert cf_mentions <= 2, f"Expected <= 2 mentions of target condition, found {cf_mentions}"

    # Exact EN / es-MX numeric parity
    pairs = _collect_bilingual_pairs(ESSAY)
    for label, en_txt, es_txt in pairs:
        nums_en = sorted(NUM_TOKEN_RE.findall(en_txt))
        nums_es = sorted(NUM_TOKEN_RE.findall(es_txt))
        assert nums_en == nums_es, f"Numeric parity mismatch in {label}: EN={nums_en} vs ES={nums_es}"

    return {
        "prose_words_en": prose_words_en,
        "all_section_words_en": all_words_en,
        "bilingual_pairs_checked": len(pairs),
        "cached_sources_verified": len(ESSAY["sources"]),
        "cf_mentions": cf_mentions,
    }


def verify_physics(planted_defect: bool = False) -> dict:
    res = evaluate_mesoscopic_floor(planted_defect=planted_defect)
    uhv = res["uhv_diamond"]
    gel = res["aqueous_hydrogel"]

    # 1. Universal Fluctuation-Dissipation identity in both regimes
    assert abs(uhv["dp_epstein_kg2_m2_s3"] / (uhv["gamma_m_epstein_specular_s"] * uhv["mass_kg"] * K_B * CRYO_TEMP_K) - 1.0) < 1e-12
    assert abs(gel["dp_stokes_kg2_m2_s3"] / (gel["gamma_m_stokes_s"] * gel["mass_kg"] * K_B * BODY_TEMP_K) - 1.0) < 1e-12
    assert abs(gel["d0_m2_s"] / gel["d0_from_fdt_m2_s"] - 1.0) < 1e-12
    assert abs(gel["d0_m2_s"] / (gel["dp_stokes_kg2_m2_s3"] / ((gel["mass_kg"] * gel["gamma_m_stokes_s"]) ** 2)) - 1.0) < 1e-12

    # 2. Knudsen / Cunningham-Epstein crossover
    mag = res["magrini_hv_silica"]
    assert 1.07e11 < mag["knudsen_n2"] < 1.09e11, f"Unexpected Magrini N2 Kn {mag['knudsen_n2']:.3e}"
    assert 4.28e-5 < mag["gamma_m_epstein_diffuse_n2_s"] < 4.32e-5, f"Unexpected Magrini gamma_m {mag['gamma_m_epstein_diffuse_n2_s']:.3e}"
    assert 5.88e-43 < mag["dp_epstein_diffuse_n2_kg2_m2_s3"] < 5.92e-43, f"Unexpected Magrini D_p {mag['dp_epstein_diffuse_n2_kg2_m2_s3']:.3e}"
    assert 8.79e-7 < uhv["radius_m"] < 8.80e-7, f"Unexpected diamond radius {uhv['radius_m']}"
    assert uhv["knudsen"] > 1.0e17, f"Expected Kn >> 1 in UHV, got {uhv['knudsen']}"
    assert gel["knudsen_effective"] < 1.0e-2, f"Expected Kn << 1 in liquid water, got {gel['knudsen_effective']}"
    assert res["knudsen_span_decades"] > 19.0
    assert abs(cunningham_slip_factor(1.0e-6) - 1.0) < 1.0e-5
    assert cunningham_slip_factor(uhv["knudsen"]) > 1.0e17
    assert abs(uhv["gamma_m_epstein_diffuse_s"] / uhv["gamma_m_epstein_specular_s"] - (1.0 + math.pi / 8.0)) < 1e-12

    # 3. Short-wavelength helium saturation vs long-wavelength photon dipole scaling
    assert 4.3e-10 < uhv["lambda_th_m"] < 4.4e-10
    assert uhv["lambda_th_m"] / QGEM_SPLIT_M < 5.0e-6
    assert uhv["lambda_bb_m"] / QGEM_SPLIT_M > 4.5

    # Planted-defect gate 1: doubling split 100 um -> 200 um MUST NOT quadruple saturated 4 K He rate!
    gas_split_ratio = uhv["gamma_gas_200um_s"] / uhv["gamma_gas_100um_s"]
    assert abs(gas_split_ratio - 1.0) < 1e-12, (
        f"Short-wavelength 4 K He decoherence failed Delta_x^0 saturation: "
        f"Gamma(200 um)/Gamma(100 um) = {gas_split_ratio:.6f} (naive Delta_x^2 defect active)"
    )
    assert abs(uhv["gamma_gas_250um_cited_s"] / uhv["gamma_gas_250um_kinetic_s"] - (8.0 * math.pi / 3.0)) < 1e-12
    assert uhv["gamma_gas_250um_naive_long_s"] / uhv["gamma_gas_250um_cited_s"] > 1.0e11

    # Cross-check agreement with T.05 decoherence kernel (allowing 1e-8 for 9-digit HBAR truncation in T.05)
    r_diam = sphere_radius(DIAMOND_MASS_QGEM_KG, DIAMOND_DENSITY_KG_M3)
    tg_kin = tg_gas_rate_saturated(UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, form="kinetic")
    tg_cit = tg_gas_rate_saturated(UHV_PRESSURE_PA, CRYO_TEMP_K, r_diam, form="cited")
    tg_ph = tg_photon_rate(QGEM_SPLIT_M, r_diam, CRYO_TEMP_K, CRYO_TEMP_K)
    assert abs(uhv["gamma_gas_250um_kinetic_s"] / tg_kin - 1.0) < 1e-12, "Mismatch vs T.05 kinetic gas rate"
    assert abs(uhv["gamma_gas_250um_cited_s"] / tg_cit - 1.0) < 1e-12, "Mismatch vs T.05 cited gas rate"
    assert abs(uhv["photon_250um_rates_s"]["total"] / tg_ph["total"] - 1.0) < 1e-7, "Mismatch vs T.05 photon rate"

    # Long-wavelength photon exponents: Delta_x^2 dipole law, R^6 T^9 scattering, R^3 T^6 emission
    dipole_200_over_100 = (photon_lambda_scattering(r_diam, CRYO_TEMP_K) * (200.0e-6 ** 2)) / (
        photon_lambda_scattering(r_diam, CRYO_TEMP_K) * (100.0e-6 ** 2)
    )
    assert abs(dipole_200_over_100 - 4.0) < 1.0e-12, f"Expected exact 4.0 dipole ratio, got {dipole_200_over_100}"
    phot_split_ratio = uhv["photon_200um_scattering_s"] / uhv["photon_100um_scattering_s"]
    assert 3.95 < phot_split_ratio <= 4.000001, f"Expected ~3.96-4.00 long-wavelength photon ratio, got {phot_split_ratio}"
    r_sc_ratio = photon_lambda_scattering(2.0 * r_diam, CRYO_TEMP_K) / photon_lambda_scattering(r_diam, CRYO_TEMP_K)
    t_sc_ratio = photon_lambda_scattering(r_diam, 2.0 * CRYO_TEMP_K) / photon_lambda_scattering(r_diam, CRYO_TEMP_K)
    r_em_ratio = photon_lambda_emission(2.0 * r_diam, CRYO_TEMP_K) / photon_lambda_emission(r_diam, CRYO_TEMP_K)
    t_em_ratio = photon_lambda_emission(r_diam, 2.0 * CRYO_TEMP_K) / photon_lambda_emission(r_diam, CRYO_TEMP_K)
    assert abs(r_sc_ratio - 64.0) < 1e-10 and abs(t_sc_ratio - 512.0) < 1e-10, "Photon scattering R^6 T^9 check failed"
    assert abs(r_em_ratio - 8.0) < 1e-10 and abs(t_em_ratio - 64.0) < 1e-10, "Photon emission R^3 T^6 check failed"

    # 4. Stokes-Einstein & Ogston-Amsden steric hindrance (Planted-defect gate 2)
    assert 6.55 < gel["d0_um2_s"] < 6.60
    assert 0.90 < gel["hindrance_xi_300nm"] < 0.92, f"Unexpected open-mesh hindrance {gel['hindrance_xi_300nm']}"
    assert 0.21 < gel["hindrance_xi_70nm"] < 0.23, (
        f"Dense xi=70 nm hydrogel hindrance {gel['hindrance_xi_70nm']:.4f} outside [0.21, 0.23] "
        f"(un-hindered pure-water defect active)"
    )
    assert 0.15 < gel["hindrance_xi_63nm"] < 0.17
    assert 4.0 < gel["slowdown_300_over_70"] < 4.3
    assert 5.5 < gel["slowdown_300_over_63"] < 5.9
    assert abs(NANOPARTICLE_RADIUS_M - 50.0e-9) < 1e-18
    assert abs(HYDROGEL_FIBER_RADIUS_M - 3.5e-9) < 1e-18
    assert abs(WATER_VISCOSITY_310K_PA_S - 0.691e-3) < 1e-18

    return res


def main() -> int:
    planted = "--planted-defect" in sys.argv
    try:
        meta = verify_metadata_and_parity()
        phys = verify_physics(planted_defect=planted)
        uhv = phys["uhv_diamond"]
        gel = phys["aqueous_hydrogel"]
        payload = {
            "status": "PASS",
            "folio_id": "ES.01",
            "essay": "ES.01",
            "slug": "mesoscopic-floor",
            "verified_benchmarks": {
                "knudsen_uhv_4K_1e-15Pa": uhv["knudsen"],
                "knudsen_water_310K": gel["knudsen_effective"],
                "knudsen_span_decades": round(phys["knudsen_span_decades"], 3),
                "diamond_radius_m": uhv["radius_m"],
                "helium_lambda_th_4K_nm": round(uhv["lambda_th_m"] * 1e9, 4),
                "photon_lambda_bb_4K_um": round(uhv["lambda_bb_m"] * 1e6, 2),
                "gamma_gas_4K_1e-15Pa_kinetic_s": uhv["gamma_gas_250um_kinetic_s"],
                "gamma_gas_4K_1e-15Pa_cited_s": uhv["gamma_gas_250um_cited_s"],
                "gamma_photon_4K_250um_scattering_s": uhv["photon_250um_rates_s"]["scattering"],
                "gamma_photon_4K_250um_total_s": uhv["photon_250um_rates_s"]["total"],
                "stokes_einstein_d0_310K_um2_s": round(gel["d0_um2_s"], 4),
                "ogston_hindrance_xi_300nm": round(gel["hindrance_xi_300nm"], 4),
                "ogston_hindrance_xi_120nm": round(gel["hindrance_xi_120nm"], 4),
                "ogston_hindrance_xi_70nm": round(gel["hindrance_xi_70nm"], 4),
                "ogston_hindrance_xi_63nm": round(gel["hindrance_xi_63nm"], 4),
                "slowdown_300nm_over_70nm": round(gel["slowdown_300_over_70"], 3),
                "slowdown_300nm_over_63nm": round(gel["slowdown_300_over_63"], 3),
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
                    "folio_id": "ES.01",
                    "essay": "ES.01",
                    "slug": "mesoscopic-floor",
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
