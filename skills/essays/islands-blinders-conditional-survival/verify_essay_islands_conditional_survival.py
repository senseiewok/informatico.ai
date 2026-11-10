#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic pure-Python stdlib verifier for Cross-Scale Essay ES.05
(`Islands, Blinders, and Conditional Survival`).

Verifies:
  1. Regime 1 — Unitary Gauss-Dressed / QES Saddle Switch (DERIVED; Page 1993a, 1993b;
     Almheiri et al. 2019; Penington 2020):
     - S_gen(k) = min(k ln 2, (6 - k) ln 2) in nats peaks at k = 3 (3 ln 2 ≈ 2.0794 nats)
       and returns to S_gen(6) = 0 nats;
     - Explicit 6-qubit Bell-pair partial trace diagonalized via pure-Python Jacobi on
       dense DCT-II rotated density matrices matches min(k, 6 - k) ln 2 to < 10^-12 with
       exact trace 1.0, 0% discarded trajectories, and V_Doob = 0 nats;
     - Exact Page Haar-average S_Page(8, 8) ≈ 1.5885 nats sits below 3 ln 2 by ~0.4909 nats,
       and asymptotic midpoint deficit approaches 0.5 nats.
  2. Regime 2 — Subalgebra Coarse-Graining / "Detector Blinders" (PROPOSED preprint;
     Geng et al. 2026, arXiv:2602.06543):
     - Global 12-qubit (4096-state) pure state has S_global = 0 nats, while CPTP partial
       trace onto k undressed radiation qubits preserves trace 1.0 (0% discarded runs,
       V_Doob = 0 nats) and raises coarse-grained entropy to 6 ln 2 ≈ 4.1589 nats at k = 6.
  3. Regime 3 — Doob h-Transform / Conditional Survival (DERIVED; Doob 1957;
     Chetrite & Touchette 2015):
     - Discrete harmonicity |(P h)(k) - h(k)| < 10^-15, tilted row-stochasticity, and
       64-path asymmetric branching sum D_KL(P^h || P) = -ln h(0) = -6 ln(1 - gamma) to
       < 10^-14;
     - At N = 6, gamma = 0.25: h(0) = 729 / 4096 ≈ 0.1780, discarding 82.20% of runs,
       V_Doob ≈ 1.7261 nats, contrasted against physical hazard shielding (gamma = 0.05:
       h(0) ≈ 0.7351, 4.13x higher yield, V_Doob ≈ 0.3078 nats).
  4. Metadata, SEO, offline Crossref/DataCite DOI cache, SKILL.md CC0-1.0 frontmatter,
     proportional CFTR/CF cap (<= 3 mentions, < 12% of <p> blocks, zero clinical claims),
     and 100% EN / es-MX numeric token parity.
  5. `--planted-defect` knockout: must fail closed and exit non-zero (1).
"""
from __future__ import annotations

import importlib.util
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
MODULE_PATH = ROOT / "tools" / "folios" / "essays" / "e05_islands_conditional_survival.py"
CACHE_PATH = ROOT / "data" / "folio-citations.cache.json"

FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
INLINE_DOI_RE = re.compile(r"10\.\d{4,9}/[^\s,;)\"']+")
DECIMAL_COMMA_RE = re.compile(r"\d,\d{1,2}(?!\d)")
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
    "la gravedad es una pendiente en el tiempo",
)


def _load_essay_module():
    assert MODULE_PATH.is_file(), f"Missing essay module: {MODULE_PATH}"
    spec = importlib.util.spec_from_file_location("e05_islands_conditional_survival", MODULE_PATH)
    assert spec is not None and spec.loader is not None, "Unable to create module spec"
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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


def _word_count(text: str) -> int:
    return len(re.findall(r"\S+", text.strip()))


def verify_physics_and_regimes(mod, planted_defect: bool = False) -> dict:
    res = mod.evaluate_three_regimes(
        n_steps=6,
        gamma=0.25,
        gamma_shielded=0.05,
        planted_defect=planted_defect,
    )
    ln2 = math.log(2.0)

    # 1. Regime 1: Unitary QES saddle switch & explicit 6-qubit Jacobi partial trace
    qes = res["qes_curve"]
    assert len(qes) == 7
    assert abs(qes[0]["s_gen_nats"] - 0.0) < 1.0e-15
    assert abs(qes[3]["s_gen_nats"] - 3.0 * ln2) < 1.0e-15
    assert abs(qes[6]["s_gen_nats"] - 0.0) < 1.0e-15, (
        f"Regime 1 unitary QES curve failed to purify at k = 6: S_gen(6) = {qes[6]['s_gen_nats']:.6f} nats"
    )
    assert qes[1]["dominant_saddle"] == "empty"
    assert qes[3]["dominant_saddle"] == "degenerate_page_transition"
    assert qes[5]["dominant_saddle"] == "island", (
        f"Expected interior island saddle at k = 5, got {qes[5]['dominant_saddle']!r}"
    )

    # Explicit 6-qubit Bell state Jacobi check
    paired = res["paired_state_jacobi_check"]
    max_jacobi_err = max(row["abs_err"] for row in paired)
    max_trace_err = max(abs(row["trace_rho"] - 1.0) for row in paired)
    assert max_jacobi_err < 1.0e-12, f"Jacobi partial-trace entropy error {max_jacobi_err:.3e}"
    assert max_trace_err < 1.0e-12, f"Unitary partial-trace trace error {max_trace_err:.3e}"

    # Page (1993) Haar subsystem checks: S_Page(8, 8) ≈ 1.588534 nats, large-N deficit -> 0.5 nats
    s_page_8_8 = res["page_midpoint_haar_nats"]
    assert 1.5885 < s_page_8_8 < 1.5886, f"Unexpected S_Page(8, 8) = {s_page_8_8}"
    large_d = 256
    asymptotic_gap = math.log(large_d) - mod.page_haar_entropy_nats(large_d, large_d)
    assert abs(asymptotic_gap - 0.5) < 5.0e-3, f"Expected ~0.5 nat Haar midpoint deficit, got {asymptotic_gap}"

    # 2. Regime 2: CPTP undressed subalgebra blinders (12 qubits = 4096 dim, 0% discard, 6 ln 2 at k = 6)
    blinders = res["blinders_curve"]
    assert abs(blinders[6]["global_dim"] - 4096.0) < 1.0e-12
    assert abs(blinders[6]["global_entropy_nats"] - 0.0) < 1.0e-14
    assert abs(blinders[3]["subalgebra_entropy_nats"] - 3.0 * ln2) < 1.0e-12
    assert abs(blinders[6]["subalgebra_entropy_nats"] - 6.0 * ln2) < 1.0e-12
    for row in blinders:
        assert abs(row["trace_preserved"] - 1.0) < 1.0e-12
        assert row["discarded_run_fraction"] == 0.0
        assert row["doob_kl_cost_nats"] == 0.0

    # 3. Regime 3: Doob h-transform on N = 6 absorbing chain (gamma = 0.25 vs shielded 0.05)
    doob = res["doob_passive"]
    assert abs(doob["h0_survival_prob"] - (729.0 / 4096.0)) < 1.0e-15
    assert abs(doob["discarded_fraction"] - (3367.0 / 4096.0)) < 1.0e-15
    expected_kl = -6.0 * math.log(0.75)
    assert abs(doob["v_doob_nats"] - expected_kl) < 1.0e-14, (
        f"Doob path-space KL cost mismatch: got {doob['v_doob_nats']:.6f} nats, expected {expected_kl:.6f} nats"
    )
    assert doob["kl_double_entry_abs_err"] < 1.0e-14, (
        f"64-path branching KL sum disagreed with -ln h(0): {doob['kl_double_entry_abs_err']:.3e}"
    )
    assert doob["max_harmonic_err"] < 1.0e-15
    assert doob["max_stochastic_err"] < 1.0e-15
    assert doob["uncond_total_mass_err"] < 1.0e-14
    assert doob["tilted_total_mass_err"] < 1.0e-14

    shield = res["doob_shielded"]
    assert abs(shield["h0_survival_prob"] - (0.95 ** 6)) < 1.0e-15
    assert abs(shield["v_doob_nats"] - (-6.0 * math.log(0.95))) < 1.0e-14
    gain = res["regime_ledger"]["regime_3_physical_shielding"]["survival_gain_factor"]
    kl_drop = res["regime_ledger"]["regime_3_physical_shielding"]["kl_reduction_factor"]
    assert 4.12 < gain < 4.14
    assert 5.60 < kl_drop < 5.62

    # 4. Epistemic & non-strawman ledger invariants (Carbon + Ornith audit rules)
    ledger = res["regime_ledger"]
    assert ledger["regime_1_unitary_qes"]["epistemic_label"] == "DERIVED", (
        "Semiclassical QES / replica wormholes must be DERIVED, never MEASURED"
    )
    assert ledger["regime_1_unitary_qes"]["discarded_fraction"] == 0.0
    assert ledger["regime_1_unitary_qes"]["v_doob_nats"] == 0.0

    assert ledger["regime_2_undressed_blinders"]["epistemic_label"] == "PROPOSED", (
        "Geng et al. (2026, arXiv:2602.06543) preprint must stay PROPOSED, never MEASURED"
    )
    assert ledger["regime_2_undressed_blinders"]["discarded_fraction"] == 0.0, (
        "Geng et al. (2026) CPTP subalgebra restriction must have 0% discarded runs (never strawmanned as post-selection)"
    )
    assert ledger["regime_2_undressed_blinders"]["v_doob_nats"] == 0.0

    assert ledger["regime_3_doob_postselection"]["epistemic_label"] == "DERIVED"
    assert ledger["regime_3_doob_postselection"]["discarded_fraction"] > 0.82
    assert ledger["regime_3_doob_postselection"]["v_doob_nats"] > 1.72

    # Internal self-check that planted_defect=True triggers failure on a clean run
    if not planted_defect:
        bad = mod.evaluate_three_regimes(planted_defect=True)
        assert bad["qes_curve"][6]["s_gen_nats"] > 4.0, "Planted defect failed to corrupt k=6 QES turnover"
        assert bad["doob_passive"]["v_doob_nats"] == 0.0, "Planted defect failed to corrupt V_Doob"
        assert bad["regime_ledger"]["regime_1_unitary_qes"]["epistemic_label"] == "MEASURED"
        assert bad["regime_ledger"]["regime_2_undressed_blinders"]["discarded_fraction"] > 0.0

    return {
        "qes_k3_nats": round(qes[3]["s_gen_nats"], 6),
        "qes_k6_nats": round(qes[6]["s_gen_nats"], 6),
        "page_haar_k3_nats": round(s_page_8_8, 6),
        "blinders_k6_nats": round(blinders[6]["subalgebra_entropy_nats"], 6),
        "blinders_global_entropy_nats": blinders[6]["global_entropy_nats"],
        "doob_gamma_0p25_h0": round(doob["h0_survival_prob"], 6),
        "doob_gamma_0p25_discarded_pct": round(doob["discarded_fraction"] * 100.0, 4),
        "doob_gamma_0p25_kl_nats": round(doob["v_doob_nats"], 6),
        "shielded_gamma_0p05_h0": round(shield["h0_survival_prob"], 6),
        "shielded_gamma_0p05_kl_nats": round(shield["v_doob_nats"], 6),
        "max_jacobi_entropy_err": max_jacobi_err,
        "kl_64path_double_entry_err": doob["kl_double_entry_abs_err"],
    }


def verify_metadata_seo_and_parity(mod) -> dict:
    essay = mod.ESSAY
    required_keys = {
        "code", "slug", "plate_slug", "date", "seo",
        "kicker_en", "kicker_es", "reading_time_en", "reading_time_es",
        "title_en", "title_es", "standfirst_en", "standfirst_es",
        "card_dek_en", "card_dek_es", "instrument_kind", "predict",
        "sections", "sidenotes", "sources", "skill_path", "verifier_path",
        "ai_line_en", "ai_line_es",
    }
    missing = required_keys - set(essay.keys())
    assert not missing, f"ESSAY missing keys: {sorted(missing)}"

    assert essay["code"] == "ES.05"
    assert essay["slug"] == "islands-blinders-conditional-survival"
    assert essay["plate_slug"] == "essay05"
    assert essay["instrument_kind"] == "island_page"
    assert essay["date"] == "2026-11-10"
    assert essay["skill_path"] == "skills/essays/islands-blinders-conditional-survival/SKILL.md"
    assert essay["verifier_path"] == "skills/essays/islands-blinders-conditional-survival/verify_essay_islands_conditional_survival.py"

    # SEO Contract
    t_en, d_en, t_es, d_es = essay["seo"]
    assert t_en != t_es, "SEO title_en and title_es must be distinct"
    for label, title in (("title_en", t_en), ("title_es", t_es)):
        assert 18 <= len(title) <= 52, f"{label} length {len(title)} outside [18, 52]: {title!r}"
        assert "informatico" not in title.lower(), f"{label} must omit brand suffix"
    for label, desc in (("desc_en", d_en), ("desc_es", d_es)):
        assert 110 <= len(desc) <= 158, f"{label} length {len(desc)} outside [110, 158]: {desc!r}"
        assert desc.endswith("."), f"{label} must end with period: {desc!r}"
        assert FORMULA_RE.search(desc) is None, f"{label} contains forbidden formula character: {desc!r}"
        assert "medical" not in desc.lower() and "médic" not in desc.lower(), f"{label} contains forbidden word"
        last_word = re.findall(r"[\wÀ-ÿ]+", desc)[-1].lower()
        assert last_word not in DANGLING_WORDS, f"{label} ends on dangling word {last_word!r}"

    # Bilingual pairs collection + word counts + <p> block CF audit
    pairs: list[tuple[str, str, str]] = [
        ("seo.title", t_en, t_es),
        ("seo.desc", d_en, d_es),
        ("kicker", essay["kicker_en"], essay["kicker_es"]),
        ("reading_time", essay["reading_time_en"], essay["reading_time_es"]),
        ("title", essay["title_en"], essay["title_es"]),
        ("standfirst", essay["standfirst_en"], essay["standfirst_es"]),
        ("card_dek", essay["card_dek_en"], essay["card_dek_es"]),
        ("ai_line", essay["ai_line_en"], essay["ai_line_es"]),
        ("predict.question", essay["predict"]["question_en"], essay["predict"]["question_es"]),
        ("predict.explain", essay["predict"]["explain_en"], essay["predict"]["explain_es"]),
    ]
    assert essay["predict"]["answer"] in ("a", "b")
    assert len(essay["predict"]["choices"]) == 2
    for ch in essay["predict"]["choices"]:
        pairs.append((f"predict.choice.{ch['id']}", ch["en"], ch["es"]))

    sections = essay["sections"]
    assert len(sections) == 5, f"Expected 5 sections, got {len(sections)}"
    roman_prefixes = ("I · ", "II · ", "III · ", "IV · ", "V · ")

    prose_en_chunks: list[str] = []
    all_en_chunks: list[str] = []
    all_es_chunks: list[str] = []
    p_blocks_en: list[str] = []

    for idx, sec in enumerate(sections):
        assert sec["h2_en"].startswith(roman_prefixes[idx]), f"Section {idx + 1} h2_en prefix mismatch"
        assert sec["h2_es"].startswith(roman_prefixes[idx]), f"Section {idx + 1} h2_es prefix mismatch"
        pairs.append((f"section[{idx}].h2", sec["h2_en"], sec["h2_es"]))
        pairs.append((f"section[{idx}].short", sec["short_en"], sec["short_es"]))
        all_en_chunks.append(sec["h2_en"])
        all_es_chunks.append(sec["h2_es"])

        for b_idx, blk in enumerate(sec["blocks"]):
            btype = blk["type"]
            assert btype in ALLOWED_BLOCK_TYPES, f"Unsupported block type {btype!r}"
            loc = f"section[{idx}].block[{b_idx}]({btype})"
            if btype == "p":
                pairs.append((loc, blk["en"], blk["es"]))
                prose_en_chunks.append(blk["en"])
                all_en_chunks.append(blk["en"])
                all_es_chunks.append(blk["es"])
                p_blocks_en.append(blk["en"])
            elif btype in ("bridge", "analogy"):
                pairs.append((f"{loc}.kicker", blk["kicker_en"], blk["kicker_es"]))
                pairs.append((f"{loc}.title", blk["title_en"], blk["title_es"]))
                all_en_chunks.extend([blk["kicker_en"], blk["title_en"]])
                all_es_chunks.extend([blk["kicker_es"], blk["title_es"]])
                for p_i, (pe, ps_) in enumerate(blk["paras"]):
                    pairs.append((f"{loc}.para[{p_i}]", pe, ps_))
                    prose_en_chunks.append(pe)
                    all_en_chunks.append(pe)
                    all_es_chunks.append(ps_)
                    p_blocks_en.append(pe)
            elif btype == "equation":
                assert blk.get("formula"), f"{loc} missing formula"
                pairs.append((f"{loc}.label", blk["label_en"], blk["label_es"]))
                pairs.append((f"{loc}.note", blk["note_en"], blk["note_es"]))
                all_en_chunks.extend([blk["label_en"], blk["note_en"]])
                all_es_chunks.extend([blk["label_es"], blk["note_es"]])
            elif btype == "table":
                pairs.append((f"{loc}.caption", blk["caption_en"], blk["caption_es"]))
                assert len(blk["headers_en"]) == len(blk["headers_es"])
                all_en_chunks.append(blk["caption_en"] + " " + " ".join(blk["headers_en"]))
                all_es_chunks.append(blk["caption_es"] + " " + " ".join(blk["headers_es"]))
                for h_i, (he, hs) in enumerate(zip(blk["headers_en"], blk["headers_es"])):
                    pairs.append((f"{loc}.header[{h_i}]", he, hs))
                for r_i, row in enumerate(blk["rows"]):
                    assert len(row) == len(blk["headers_en"])
                    for c_i, (ce, cs) in enumerate(row):
                        pairs.append((f"{loc}.cell[{r_i}][{c_i}]", ce, cs))
                    all_en_chunks.append(" ".join(c[0] for c in row))
                    all_es_chunks.append(" ".join(c[1] for c in row))

    prose_words_en = _word_count(" ".join(prose_en_chunks))
    all_words_en = _word_count(" ".join(all_en_chunks))
    assert 1800 <= prose_words_en <= 2600, f"EN prose words {prose_words_en} outside [1800, 2600]"
    assert 1800 <= all_words_en <= 2600, f"EN all-section words {all_words_en} outside [1800, 2600]"

    sidenotes = essay["sidenotes"]
    assert 4 <= len(sidenotes) <= 5, f"Expected 4..5 sidenotes, got {len(sidenotes)}"
    for n_idx, sn in enumerate(sidenotes):
        pairs.append((f"sidenote[{n_idx}].label", sn["label_en"], sn["label_es"]))
        pairs.append((f"sidenote[{n_idx}].body", sn["en"], sn["es"]))

    sources = essay["sources"]
    assert 8 <= len(sources) <= 10, f"Expected 8..10 sources, got {len(sources)}"
    cache = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    expected_dois = {
        "10.1103/physrevlett.71.3743",
        "10.1103/physrevlett.71.1291",
        "10.1007/jhep12(2019)063",
        "10.1007/jhep09(2020)002",
        "10.48550/arxiv.2602.06543",
        "10.24033/bsmf.1494",
        "10.1007/s00023-014-0375-8",
        "10.1371/journal.pgen.1007723",
        "10.1172/jci154571",
    }
    seen_dois: set[str] = set()
    for src_idx, src in enumerate(sources):
        assert src["id"].startswith("ES05-")
        doi_low = src["doi"].strip().lower()
        rec = cache.get(f"doi:{doi_low}")
        assert rec and rec.get("found") is True, f"Uncached DOI: {src['doi']}"
        if rec.get("year"):
            assert abs(int(rec["year"]) - int(src["year"])) <= 1, f"Year mismatch for {src['id']}"
        seen_dois.add(doi_low)
        pairs.append((f"source[{src_idx}].role", src["role_en"], src["role_es"]))
    assert len(seen_dois & expected_dois) >= 8, "Must cite at least 8 pre-cached ES.05 DOIs"

    # Numeric parity + es-MX decimal separator check
    for label, en_txt, es_txt in pairs:
        nums_en = mod.extract_number_tokens(en_txt)
        nums_es = mod.extract_number_tokens(es_txt)
        assert nums_en == nums_es, f"Numeric parity mismatch in {label}: EN={nums_en} vs ES={nums_es}"
        assert DECIMAL_COMMA_RE.search(es_txt) is None, f"Forbidden decimal comma in es-MX ({label}): {es_txt!r}"

    # Proportional CF / CFTR guardrail (<= 3 combined mentions in authored essay text, < 12% of <p> blocks)
    full_authored_en = " ".join(
        [t_en, d_en, essay["title_en"], essay["standfirst_en"], essay["card_dek_en"]]
        + all_en_chunks
        + [sn["en"] for sn in sidenotes]
        + [src["role_en"] for src in sources]
    )
    full_authored_es = " ".join(
        [t_es, d_es, essay["title_es"], essay["standfirst_es"], essay["card_dek_es"]]
        + all_es_chunks
        + [sn["es"] for sn in sidenotes]
        + [src["role_es"] for src in sources]
    )
    cf_or_cftr_pat_en = re.compile(r"\bcftr\b|cystic\s+fibrosis", re.IGNORECASE)
    cf_or_cftr_pat_es = re.compile(r"\bcftr\b|fibrosis\s+qu[ií]stica", re.IGNORECASE)
    cf_mentions_en = len(cf_or_cftr_pat_en.findall(full_authored_en))
    cf_mentions_es = len(cf_or_cftr_pat_es.findall(full_authored_es))
    assert cf_mentions_en <= 3, f"CFTR / cystic fibrosis mentioned {cf_mentions_en} times in EN (> 3)"
    assert cf_mentions_es <= 3, f"CFTR / fibrosis quística mentioned {cf_mentions_es} times in ES (> 3)"

    p_cf_hits = sum(1 for p_txt in p_blocks_en if cf_or_cftr_pat_en.search(p_txt))
    p_cf_ratio = p_cf_hits / max(1, len(p_blocks_en))
    assert p_cf_ratio < 0.12, f"CF paragraph fraction {p_cf_ratio:.3f} ({p_cf_hits}/{len(p_blocks_en)}) >= 0.12"

    for phrase in BANNED_PHRASES:
        assert phrase not in full_authored_en.lower(), f"Banned phrase {phrase!r} in EN"
        assert phrase not in full_authored_es.lower(), f"Banned phrase {phrase!r} in ES"

    for inline_doi in set(INLINE_DOI_RE.findall(full_authored_en + " " + full_authored_es)):
        cleaned = inline_doi.rstrip(".")
        rec = cache.get("doi:" + cleaned.lower())
        assert rec and rec.get("found"), f"Uncached inline DOI {cleaned}"

    # SKILL.md YAML frontmatter validation
    skill_file = ROOT / essay["skill_path"]
    verifier_file = ROOT / essay["verifier_path"]
    assert skill_file.is_file(), f"Missing {skill_file}"
    assert verifier_file.is_file(), f"Missing {verifier_file}"
    fm = _parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    assert fm.get("name") == "essay-es05-islands-blinders-conditional-survival"
    assert fm.get("license") == "CC0-1.0", f"Expected license: CC0-1.0, got {fm.get('license')!r}"
    assert fm.get("description") and fm.get("compatibility")

    return {
        "prose_words_en": prose_words_en,
        "all_section_words_en": all_words_en,
        "bilingual_pairs_checked": len(pairs),
        "cached_sources_verified": len(sources),
        "cf_or_cftr_mentions_en": cf_mentions_en,
        "cf_p_block_fraction": round(p_cf_ratio, 4),
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
        mod = _load_essay_module()
        phys = verify_physics_and_regimes(mod, planted_defect=planted)
        meta = verify_metadata_seo_and_parity(mod)
        payload = {
            "status": "PASS",
            "folio_id": "ES.05",
            "essay": "ES.05",
            "slug": "islands-blinders-conditional-survival",
            "verified_benchmarks": phys,
            "metadata_checks": meta,
            "planted_defect_guard": "REJECTED_AS_EXPECTED",
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    except AssertionError as exc:
        print(
            json.dumps(
                {
                    "status": "FAIL",
                    "folio_id": "ES.05",
                    "essay": "ES.05",
                    "slug": "islands-blinders-conditional-survival",
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
