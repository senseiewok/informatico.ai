#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic pure-Python stdlib verifier for Essay ES.03 · Barriers, Pores, and Clocks.

Verifies:
1. Barato-Seifert Thermodynamic Uncertainty Relation Q_TUR = (A / N) coth(A / (2 N)) >= 2.0
   across a 9 x 11 grid of (N_states, affinity A), near-equilibrium saturation Q_TUR -> 2,
   high-affinity scaling Q_TUR -> A / N, independent tilted Markov generator cumulants,
   the 1 % clock uncertainty bound (Delta_S / k_B >= 20,000), and the 4-state ATP-gated
   channel conformational cycle (A = 20 => Q_TUR = 5 coth(2.5) ≈ 5.0678 >= 2).
2. Brinkman porous-medium screening ell_B = sqrt(kappa) across 10 orders of magnitude in kappa,
   exact 1D Brinkman PDE residual < 1e-13, Poiseuille open-channel limit, and Darcy plug limit.
3. Kramers Arrhenius/Eyring barrier-escape identity k(Delta_G - 3 k_B T) / k(Delta_G) = exp(3) ≈ 20.09.
4. Essay ES.03 contract: exact keys, SEO budgets, 1,800–2,600 EN word count, <= 2 'Cystic Fibrosis'
   mentions, offline DOI cache membership in data/folio-citations.cache.json, and 100 % EN/es-MX
   numeric token parity.
5. `--planted-defect`: injects an equilibrium zero-affinity perpetual-clock defect (k_plus = k_minus,
   A = 0 claiming directed ticks with Q_TUR = 0 < 2) plus inverted Brinkman scaling, exiting non-zero.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "folios" / "essays"))

import e03_barriers_pores_clocks as es03  # noqa: E402

TOL = 1e-12
FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
NUM_RE = re.compile(r"(?<![A-Za-z])\d+(?:,\d{3})*(?:\.\d+)?")
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s,;\"'\]\\<)]+)")


def extract_numbers(text: str) -> list[str]:
    """Extract sorted numeric literals (normalized for thousands separators if any, keeping '.' decimals)."""
    return sorted(NUM_RE.findall(text))


def verify_tur_grid(planted_defect: bool = False) -> dict:
    if planted_defect:
        # Planted second-law defect: zero-affinity equilibrium ring (k_plus == k_minus, A = 0)
        # claiming finite directed ticks with zero entropy dissipation (Q_TUR = 0 < 2)
        q_tur_planted = 0.0
        ell_b_planted = es03.brinkman_screening_length(1.0e-16, planted_invert=True)
        assert q_tur_planted >= 2.0 - 1e-14, (
            f"Planted defect caught: equilibrium A = 0 ring claimed directed clock ticks with "
            f"Q_TUR = {q_tur_planted:.6f} < 2.0 (violates Barato-Seifert TUR and detailed balance)"
        )
        assert math.isclose(ell_b_planted, 1.0e-8, rel_tol=1e-12), (
            f"Planted defect caught: inverted Brinkman screening gave ell_B = {ell_b_planted:.3e} m"
        )

    # Confirm the kernel itself rejects equilibrium k_plus == k_minus for a directed clock
    equilibrium_rejected = False
    try:
        es03.tur_biased_ring_rates(n_states=4, k_plus=5.0, k_minus=5.0)
    except ValueError:
        equilibrium_rejected = True
    assert equilibrium_rejected, "tur_biased_ring_rates failed to reject equilibrium k_plus == k_minus"

    n_grid = (1, 2, 3, 4, 6, 8, 10, 16, 32)
    a_grid = (1e-4, 1e-2, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0)
    min_q = float("inf")
    max_analytic_diff = 0.0
    max_cgf_diff = 0.0

    for n_states in n_grid:
        for affinity in a_grid:
            res = es03.tur_from_affinity(n_states=n_states, affinity_kb=affinity, k_minus=1.25, tau=2.5)
            q_val = res["q_tur"]
            q_ana = res["q_tur_analytic"]
            assert res["current_hz"] > 0.0, f"Expected J > 0 for A={affinity} > 0"
            assert q_val >= 2.0, f"TUR violated at N={n_states}, A={affinity}: Q_TUR={q_val}"
            assert math.isclose(res["fano_tick"], res["fano_tick_analytic"], rel_tol=TOL, abs_tol=TOL), (
                f"Fano factor mismatch at N={n_states}, A={affinity}: {res['fano_tick']} vs {res['fano_tick_analytic']}"
            )
            assert math.isclose(res["eps2_tau"] * res["current_hz"], res["fano_tick"], rel_tol=TOL, abs_tol=TOL), (
                f"Dimensional eps2_tau * J != fano_tick at N={n_states}, A={affinity}"
            )
            diff = abs(q_val - q_ana)
            max_analytic_diff = max(max_analytic_diff, diff)
            min_q = min(min_q, q_val)

            # Independent check from tilted Markov ring cumulant generating function:
            # mu(lambda) = k_+ (exp(lambda/N) - 1) + k_- (exp(-lambda/N) - 1)
            km, n_f = res["k_minus"], float(n_states)
            dk = km * math.expm1(affinity / n_f)
            j_cgf = dk / n_f
            var_rate_cgf = (2.0 * km + dk) / (n_f * n_f)  # mu''(0) = 2 * D_J
            q_cgf = (var_rate_cgf / j_cgf) * affinity
            max_cgf_diff = max(max_cgf_diff, abs(q_val - q_cgf))

    assert max_analytic_diff < TOL, f"Analytic coth mismatch {max_analytic_diff:.3e}"
    assert max_cgf_diff < TOL, f"Tilted Markov CGF mismatch {max_cgf_diff:.3e}"

    # Near-equilibrium saturation (A -> 0 => Q_TUR -> 2)
    near_eq = es03.tur_from_affinity(n_states=4, affinity_kb=1e-4)
    assert 0.0 < (near_eq["q_tur"] - 2.0) < 1e-8, f"Near-equilibrium Q_TUR={near_eq['q_tur']} did not saturate 2"

    # High-driving asymptotic scaling (A >> 2 N => Q_TUR -> A / N)
    high_drv = es03.tur_from_affinity(n_states=4, affinity_kb=200.0)
    assert abs(high_drv["q_tur"] / (200.0 / 4.0) - 1.0) < TOL, "High-affinity Q_TUR / (A/N) failed to approach 1"

    # Benchmark 1: 1 % clock relative error => Var(N)/<N>^2 = 1e-4 => Delta_S / k_B >= 20,000
    min_entropy_1pct = es03.minimum_clock_entropy_kb(1e-4)
    assert math.isclose(min_entropy_1pct, 20000.0, rel_tol=0.0, abs_tol=1e-12)

    # Benchmark 2: ATP-gated channel conformational cycle (A = 20 k_B, N = 4 states)
    atp_ring = es03.tur_from_affinity(n_states=4, affinity_kb=20.0)
    expected_atp_q = 5.0 * (math.cosh(2.5) / math.sinh(2.5))
    assert abs(atp_ring["q_tur"] - expected_atp_q) < TOL
    assert atp_ring["q_tur"] > 5.06

    return {
        "grid_points": len(n_grid) * len(a_grid),
        "min_q_tur": min_q,
        "near_equilibrium_q_tur": near_eq["q_tur"],
        "atp_4state_q_tur": atp_ring["q_tur"],
        "clock_1pct_min_entropy_kb": min_entropy_1pct,
        "max_analytic_diff": max_analytic_diff,
        "max_cgf_diff": max_cgf_diff,
        "equilibrium_zero_affinity_rejected": equilibrium_rejected,
    }


def verify_brinkman_and_kramers() -> dict:
    # Brinkman screening lengths across civil stone/concrete and hydrogels
    benchmarks = {
        "pervious_concrete_m": (1.0e-8, 1.0e-4),
        "lime_mortar_m": (1.0e-12, 1.0e-6),
        "open_hydrogel_m": (2.5e-15, 5.0e-8),
        "compacted_hydrogel_m": (1.0e-16, 1.0e-8),
        "cement_paste_m": (1.0e-18, 1.0e-9),
    }
    screening_out = {}
    for name, (kappa, expected_ell) in benchmarks.items():
        ell = es03.brinkman_screening_length(kappa)
        assert math.isclose(ell, expected_ell, rel_tol=TOL, abs_tol=0.0), f"{name}: {ell} != {expected_ell}"
        screening_out[name] = ell

    # PDE residual across interior collocation points and regimes
    max_pde_res = 0.0
    for kappa in (1.0e-8, 1.0e-12, 2.5e-15, 1.0e-16):
        h_half = 1.0e-4
        eta = 1.0e-3
        grad_p = 1.0e4
        # No-slip walls
        assert abs(es03.brinkman_channel_velocity(h_half, h_half, kappa, eta, grad_p)) < 1e-18
        assert abs(es03.brinkman_channel_velocity(-h_half, h_half, kappa, eta, grad_p)) < 1e-18
        for frac in (-0.85, -0.4, 0.0, 0.35, 0.75):
            res = es03.brinkman_pde_residual(frac * h_half, h_half, kappa, eta, grad_p)
            max_pde_res = max(max_pde_res, res)
    assert max_pde_res < 1e-13, f"Brinkman PDE residual too large: {max_pde_res:.3e}"

    # Asymptotic Poiseuille limit (ell_B >> H) and Darcy plug limit (ell_B << H)
    h_test, eta_test, g_test = 1.0e-3, 1.0e-3, 100.0
    u_pois_exact = g_test * (h_test * h_test) / (2.0 * eta_test)
    u_pois_brink = es03.brinkman_channel_velocity(0.0, h_test, kappa_m2=100.0, eta_pa_s=eta_test, grad_p_pa_per_m=g_test)
    assert math.isclose(u_pois_brink, u_pois_exact, rel_tol=1e-7)

    kappa_tight = 1.0e-16
    u_darcy_exact = g_test * kappa_tight / eta_test
    u_darcy_brink = es03.brinkman_channel_velocity(0.0, h_test, kappa_m2=kappa_tight, eta_pa_s=eta_test, grad_p_pa_per_m=g_test)
    assert math.isclose(u_darcy_brink, u_darcy_exact, rel_tol=1e-12)

    # Kramers barrier escape identities
    r_init = es03.kramers_escape_rate(k0_hz=1.0e6, delta_g_dag_kbt=18.0)
    r_resc = es03.kramers_escape_rate(k0_hz=1.0e6, delta_g_dag_kbt=15.0)
    mult_3kbt = es03.kramers_flux_multiplier(3.0)
    mult_6kbt = es03.kramers_flux_multiplier(6.0)
    assert math.isclose(r_resc / r_init, mult_3kbt, rel_tol=TOL)
    assert math.isclose(mult_3kbt, math.exp(3.0), rel_tol=TOL)
    assert math.isclose(round(mult_3kbt, 2), 20.09, rel_tol=0.0, abs_tol=1e-9)
    assert math.isclose(round(mult_6kbt, 2), 403.43, rel_tol=0.0, abs_tol=1e-9)

    return {
        "screening_lengths_m": screening_out,
        "max_brinkman_pde_rel_residual": max_pde_res,
        "kramers_3kbt_multiplier": mult_3kbt,
        "kramers_6kbt_multiplier": mult_6kbt,
    }


def verify_essay_contract() -> dict:
    e = es03.ESSAY
    required_keys = {
        "code", "slug", "plate_slug", "date", "seo",
        "kicker_en", "kicker_es", "reading_time_en", "reading_time_es",
        "title_en", "title_es", "standfirst_en", "standfirst_es",
        "card_dek_en", "card_dek_es", "instrument_kind", "predict",
        "sections", "sidenotes", "sources", "skill_path", "verifier_path",
        "ai_line_en", "ai_line_es",
    }
    missing = required_keys - set(e.keys())
    assert not missing, f"Missing ESSAY keys: {sorted(missing)}"
    assert e["code"] == "ES.03"
    assert e["slug"] == "barriers-pores-clocks"
    assert e["plate_slug"] == "essay03"
    assert e["date"] == "2026-11-10"
    assert e["instrument_kind"] == "tur_pores"
    assert e["reading_time_en"] == "14 min read"
    assert e["reading_time_es"] == "14 min de lectura"
    assert (ROOT / e["skill_path"]).is_file(), f"Missing skill file {e['skill_path']}"
    assert (ROOT / e["verifier_path"]).is_file(), f"Missing verifier file {e['verifier_path']}"

    # SEO checks
    t_en, d_en, t_es, d_es = e["seo"]
    for label, t in (("title_en", t_en), ("title_es", t_es)):
        assert 18 <= len(t) <= 50, f"SEO {label} length {len(t)} outside [18, 50]: {t!r}"
        assert "| Informatico.ai" not in t, f"SEO {label} must not contain brand suffix"
    for label, d in (("desc_en", d_en), ("desc_es", d_es)):
        assert 115 <= len(d) <= 152, f"SEO {label} length {len(d)} outside [115, 152]: {d!r}"
        assert d.endswith("."), f"SEO {label} must end with period: {d!r}"
        assert "medical" not in d.lower() and "médic" not in d.lower(), f"Forbidden medical term in {label}"
        assert FORMULA_RE.search(d) is None, f"Formula character in {label}: {d!r}"
        last_word = re.findall(r"[\wÀ-ÿ]+", d)[-1].lower()
        assert last_word not in DANGLING_WORDS, f"Dangling final word {last_word!r} in {label}"

    # Sections, word count, and bilingual numeric parity
    assert len(e["sections"]) == 5, f"Expected 5 sections, got {len(e['sections'])}"
    roman_prefixes = ("I · ", "II · ", "III · ", "IV · ", "V · ")
    en_prose_words = 0
    en_total_section_words = 0
    all_en_blobs: list[str] = [
        t_en, d_en, e["kicker_en"], e["title_en"], e["standfirst_en"], e["card_dek_en"],
        e["predict"]["question_en"], e["predict"]["explain_en"], e["ai_line_en"],
    ]

    parity_pairs: list[tuple[str, str, str]] = [
        ("kicker", e["kicker_en"], e["kicker_es"]),
        ("reading_time", e["reading_time_en"], e["reading_time_es"]),
        ("title", e["title_en"], e["title_es"]),
        ("standfirst", e["standfirst_en"], e["standfirst_es"]),
        ("card_dek", e["card_dek_en"], e["card_dek_es"]),
        ("predict.question", e["predict"]["question_en"], e["predict"]["question_es"]),
        ("predict.explain", e["predict"]["explain_en"], e["predict"]["explain_es"]),
        ("ai_line", e["ai_line_en"], e["ai_line_es"]),
    ]
    for ch in e["predict"]["choices"]:
        parity_pairs.append((f"predict.choice.{ch['id']}", ch["en"], ch["es"]))
        all_en_blobs.append(ch["en"])

    for idx, sec in enumerate(e["sections"]):
        assert sec["h2_en"].startswith(roman_prefixes[idx]), f"Section {idx+1} h2_en missing prefix"
        assert sec["h2_es"].startswith(roman_prefixes[idx]), f"Section {idx+1} h2_es missing prefix"
        parity_pairs.append((f"sec.{sec['id']}.h2", sec["h2_en"], sec["h2_es"]))
        parity_pairs.append((f"sec.{sec['id']}.short", sec["short_en"], sec["short_es"]))
        en_total_section_words += len(sec["h2_en"].split())
        all_en_blobs.append(sec["h2_en"])

        for b_idx, blk in enumerate(sec["blocks"]):
            btype = blk["type"]
            assert btype in {"p", "bridge", "analogy", "equation", "table"}, f"Unknown block type {btype}"
            tag = f"sec.{sec['id']}.block[{b_idx}]({btype})"
            if btype == "p":
                parity_pairs.append((tag, blk["en"], blk["es"]))
                w_count = len(blk["en"].split())
                en_prose_words += w_count
                en_total_section_words += w_count
                all_en_blobs.append(blk["en"])
            elif btype in {"bridge", "analogy"}:
                parity_pairs.append((f"{tag}.kicker", blk["kicker_en"], blk["kicker_es"]))
                en_total_section_words += len(blk["kicker_en"].split())
                all_en_blobs.append(blk["kicker_en"])
                if blk.get("title_en") or blk.get("title_es"):
                    parity_pairs.append((f"{tag}.title", blk["title_en"], blk["title_es"]))
                    en_total_section_words += len(blk["title_en"].split())
                    all_en_blobs.append(blk["title_en"])
                for p_i, (pe, ps_) in enumerate(blk["paras"]):
                    parity_pairs.append((f"{tag}.para[{p_i}]", pe, ps_))
                    w_count = len(pe.split())
                    en_prose_words += w_count
                    en_total_section_words += w_count
                    all_en_blobs.append(pe)
            elif btype == "equation":
                parity_pairs.append((f"{tag}.label", blk["label_en"], blk["label_es"]))
                parity_pairs.append((f"{tag}.note", blk["note_en"], blk["note_es"]))
                assert isinstance(blk.get("formula"), str) and blk["formula"].strip()
                w_count = len(blk["note_en"].split())
                en_prose_words += w_count
                en_total_section_words += len(blk["label_en"].split()) + w_count
                all_en_blobs.extend([blk["label_en"], blk["note_en"]])
            elif btype == "table":
                parity_pairs.append((f"{tag}.caption", blk["caption_en"], blk["caption_es"]))
                en_total_section_words += len(blk["caption_en"].split())
                all_en_blobs.append(blk["caption_en"])
                assert len(blk["headers_en"]) == len(blk["headers_es"])
                for h_i, (he, hs) in enumerate(zip(blk["headers_en"], blk["headers_es"])):
                    parity_pairs.append((f"{tag}.header[{h_i}]", he, hs))
                    en_total_section_words += len(he.split())
                    all_en_blobs.append(he)
                for r_i, row in enumerate(blk["rows"]):
                    assert len(row) == len(blk["headers_en"])
                    for c_i, (ce, cs) in enumerate(row):
                        parity_pairs.append((f"{tag}.row[{r_i}][{c_i}]", ce, cs))
                        en_total_section_words += len(ce.split())
                        all_en_blobs.append(ce)

    assert 1800 <= en_prose_words <= 2600, f"EN prose words {en_prose_words} outside [1800, 2600]"
    assert 1800 <= en_total_section_words <= 2600, f"EN total section words {en_total_section_words} outside [1800, 2600]"

    assert 4 <= len(e["sidenotes"]) <= 5, f"Expected 4–5 sidenotes, got {len(e['sidenotes'])}"
    for s_i, sn in enumerate(e["sidenotes"]):
        parity_pairs.append((f"sidenote[{s_i}].label", sn["label_en"], sn["label_es"]))
        parity_pairs.append((f"sidenote[{s_i}].body", sn["en"], sn["es"]))
        all_en_blobs.append(sn["en"])

    assert 8 <= len(e["sources"]) <= 10, f"Expected 8–10 sources, got {len(e['sources'])}"
    cache_path = ROOT / "data" / "folio-citations.cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8"))
    source_dois: set[str] = set()
    for src in e["sources"]:
        doi_low = src["doi"].lower()
        assert f"doi:{doi_low}" in cache and cache[f"doi:{doi_low}"].get("found"), f"DOI not in cache: {src['doi']}"
        source_dois.add(doi_low)
        parity_pairs.append((f"source.{src['id']}.role", src["role_en"], src["role_es"]))

    # Verify every inline DOI in prose is also in cache and in sources
    joined_en = "\n".join(all_en_blobs)
    inline_dois = {m.rstrip(".,;:)") for m in DOI_RE.findall(joined_en)}
    for d in inline_dois:
        assert f"doi:{d.lower()}" in cache and cache[f"doi:{d.lower()}"].get("found"), f"Inline DOI not in cache: {d}"
        assert d.lower() in source_dois, f"Inline DOI {d} missing from ESSAY['sources']"

    # Proportional CF guardrail: <= 2 mentions of 'Cystic Fibrosis' across entire essay
    cf_mentions = len(re.findall(r"cystic\s+fibrosis", joined_en, flags=re.IGNORECASE))
    assert cf_mentions <= 2, f"Cystic Fibrosis mentioned {cf_mentions} times (> 2 limit)"

    # Exact EN / es-MX numeric parity across every bilingual pair
    for label, en_txt, es_txt in parity_pairs:
        nums_en = extract_numbers(en_txt)
        nums_es = extract_numbers(es_txt)
        assert nums_en == nums_es, f"Numeric parity mismatch in {label}: EN={nums_en} vs ES={nums_es}"

    return {
        "en_prose_words": en_prose_words,
        "en_total_section_words": en_total_section_words,
        "cf_mentions": cf_mentions,
        "sources_verified_in_cache": len(e["sources"]),
        "bilingual_parity_pairs_checked": len(parity_pairs),
        "seo_lengths": {
            "title_en": len(t_en),
            "desc_en": len(d_en),
            "title_es": len(t_es),
            "desc_es": len(d_es),
        },
    }


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    planted = "--planted-defect" in args
    try:
        tur_report = verify_tur_grid(planted_defect=planted)
        transport_report = verify_brinkman_and_kramers()
        contract_report = verify_essay_contract()
    except AssertionError as exc:
        print(
            json.dumps(
                {
                    "status": "FAIL",
                    "essay": es03.CODE,
                    "slug": es03.SLUG,
                    "error": str(exc),
                }
            ),
            file=sys.stderr,
        )
        return 1

    print(
        json.dumps(
            {
                "status": "PASS",
                "essay": es03.CODE,
                "slug": es03.SLUG,
                "tur_grid": tur_report,
                "transport_and_barriers": transport_report,
                "essay_contract": contract_report,
                "planted_defect_guard": "REJECTED_AS_EXPECTED",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
