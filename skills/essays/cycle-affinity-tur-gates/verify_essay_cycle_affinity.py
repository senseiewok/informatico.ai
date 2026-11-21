#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.12 · Cycle Affinity & Irreversible Gates.

Supports `--planted-defect`, which corrupts the iso-P_o gauge family and injects equilibrium-entry
conflation plus a `sorry` theorem into the temporary Lean 4 audit copy, failing closed (exit 1).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import time
import unicodedata

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from folios.essays.e12_cycle_affinity_gates import (  # noqa: E402
    CODE,
    ESSAY,
    PLATE_SLUG,
    SLUG,
    _LEAN_SECONDS,
    evaluate_cycle_affinity_gates,
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
    "10.1103/physrev.37.405",
    "10.1103/physrevlett.95.130602",
    "10.1085/jgp.200609558",
    "10.1088/0034-4885/75/12/126001",
    "10.1103/physrevlett.114.158101",
    "10.1103/physrevlett.116.120601",
    "10.1103/physrevx.6.041064",
    "10.1073/pnas.1815287115",
    "10.1103/physrevlett.126.010601",
)

EXPECTED_THEOREMS = (
    "cycle_affinity_si_homogeneity",
    "sq_nonneg",
    "mul_sq_nonneg",
    "iso_po_kirchhoff_stationarity_and_flux",
    "cauchy_schwarz_variance_identity",
    "lagrange_tur_four_ab_bound",
    "equilibrium_entry_initial_slope_nonpositive",
    "equilibrium_two_state_discriminant_nonnegative",
    "driven_entry_peaked_burst_witness",
    "driven_entry_monotonic_subthreshold_witness",
    "single_open_state_always_monotone",
    "four_architecture_gate_table",
)

BANNED_PHRASES = (
    "our " + "lab",
    "nuestro " + "laboratorio",
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
    _LEAN_SECONDS[0] = 0.0
    t0 = time.perf_counter()
    syn = evaluate_cycle_affinity_gates(planted_defect=planted_defect)
    kernel_s = time.perf_counter() - t0 - _LEAN_SECONDS[0]
    assert kernel_s < 2.0, f"Pure Python kernel exceeded 2.0 s budget: {kernel_s:.3f} s"

    r_eq = syn["ring_eq"]
    r_lim = syn["ring_lim"]
    r_mid = syn["ring_mid"]
    r_drv = syn["ring_drv"]
    r_atp = syn["ring_atp"]
    burst = syn["burst_4state"]
    burst_sub = syn["burst_subthreshold"]
    lean = syn["lean"]

    failures: list[str] = []

    def _chk(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)

    # 1. Iso-P_o gauge invariance across equilibrium and driven regimes
    for label, row in (("eq", r_eq), ("lim", r_lim), ("mid", r_mid), ("drv", r_drv), ("atp", r_atp)):
        _chk(abs(row["p_open"] - 0.40) < 1.0e-12, f"{label} P_o drifted: {row['p_open']}")
        _chk(row["max_stationarity_residual"] < 1.0e-13, f"{label} W^T pi != 0")
        _chk(row["solver_diff"] < 1.0e-7, f"{label} dual-solver D_J mismatch: {row['solver_diff']}")

    _chk(r_eq["affinity_kb"] == 0.0 and abs(r_eq["flux_j"]) < 1.0e-14, "eq flux or affinity non-zero")
    _chk(abs(r_eq["q_tur"] - 2.0) < 1.0e-12, f"eq Q_TUR linear-response limit must be 2.0, got {r_eq['q_tur']}")
    _chk(abs(r_lim["q_tur"] - 2.0) < 1.0e-6, f"J=1e-4 limit Q_TUR diverged from 2.0: {r_lim['q_tur']}")
    _chk(r_mid["q_tur"] >= 2.0 and r_drv["q_tur"] >= 2.0 and r_atp["q_tur"] >= 2.0, "TUR floor violated")
    _chk(abs(r_mid["affinity_kb"] - 0.9162907) < 1.0e-4, f"mid affinity mismatch: {r_mid['affinity_kb']}")
    _chk(abs(r_mid["q_tur"] - 2.018639) < 1.0e-4, f"mid Q_TUR mismatch: {r_mid['q_tur']}")
    _chk(abs(r_drv["flux_ratio"] - 55.0) < 1.0e-12, f"drv flux_ratio mismatch: {r_drv['flux_ratio']}")
    _chk(abs(r_drv["affinity_kb"] - 4.007333) < 1.0e-4, f"drv affinity mismatch: {r_drv['affinity_kb']}")
    _chk(abs(r_drv["sigma_kb_per_s"] - 16.02933) < 1.0e-4, f"drv sigma mismatch: {r_drv['sigma_kb_per_s']}")
    _chk(abs(r_drv["lam2_poly"] - 2.316049) < 1.0e-4, f"drv lam2 mismatch: {r_drv['lam2_poly']}")
    _chk(abs(r_drv["q_tur"] - 2.320295) < 1.0e-4, f"drv Q_TUR mismatch: {r_drv['q_tur']}")
    _chk(abs(r_atp["affinity_kb"] - 19.62915) < 1.0e-3, f"atp affinity mismatch: {r_atp['affinity_kb']}")
    _chk(abs(r_atp["q_tur"] - 6.79031) < 1.0e-4, f"atp Q_TUR mismatch: {r_atp['q_tur']}")

    # 2. 4-State Open-Subspace Complete Monotonicity vs Driven Peak + Subthreshold Control
    _chk(burst["slope0_eq_err"] < 1.0e-12, "slope0_eq mismatch")
    _chk(abs(burst["f0_eq"] - 4.333333) < 1.0e-4, f"f0_eq mismatch: {burst['f0_eq']}")
    _chk(abs(burst["slope0_eq"] - (-42.333333)) < 1.0e-4 and burst["slope0_eq"] <= 0.0, "eq slope positive")
    _chk(bool(burst["eq_monotone"]), "Equilibrium exit PDF must be completely monotone")
    _chk(abs(burst["f0_drv"] - 1.0) < 1.0e-12, f"f0_drv mismatch: {burst['f0_drv']}")
    _chk(abs(burst["slope0_drv"] - 31.0) < 1.0e-10 and burst["slope0_drv"] > 0.0, f"slope0_drv={burst['slope0_drv']}")
    _chk(abs(burst["t_peak_drv_s"] - 0.094) <= 0.002, f"t_peak={burst['t_peak_drv_s']}")
    _chk(abs(burst["f_peak_drv"] - 2.0166) < 0.005, f"f_peak={burst['f_peak_drv']}")
    _chk(abs(burst_sub["slope0_drv"] - (-18.0)) < 1.0e-10 and burst_sub["slope0_drv"] < 0.0, "subthreshold -18 failed")
    _chk(0.999 <= burst["integral_eq"] <= 1.001, f"eq integral={burst['integral_eq']}")
    _chk(0.999 <= burst["integral_drv"] <= 1.001, f"drv integral={burst['integral_drv']}")

    # 3. Lean 4 Prelude formal checks
    _chk(lean["imports"] == 0, f"Unexpected Lean imports: {lean['imports']}")
    _chk(not lean["forbidden_tokens"], f"Forbidden Lean tokens: {lean['forbidden_tokens']}")
    _chk(lean["theorem_count"] == 12, f"Expected 12 Lean theorems (10 main + 2 lemmas), got {lean['theorem_count']}")
    _chk(tuple(lean["theorem_names"]) == EXPECTED_THEOREMS, f"Unexpected theorem names: {lean['theorem_names']}")
    _chk(bool(lean["cauchy_schwarz_fraction_identity"]), "Fraction Cauchy-Schwarz identity failed")
    if lean["lean_available"]:
        _chk(bool(lean["compiled"]), "CycleAffinityGates.lean failed Lean 4 compilation")

    # 4. Metadata, SEO, word budget, bilingual numeric parity, and offline DOI cache checks
    _chk(ESSAY["code"] == CODE and ESSAY["slug"] == SLUG and ESSAY["plate_slug"] == PLATE_SLUG, "ESSAY keys mismatch")
    t_en, d_en, t_es, d_es = ESSAY["seo"]
    for t_str in (t_en, t_es):
        _chk(18 <= len(t_str) <= 52, f"SEO title length out of 18..52: {len(t_str)} {t_str!r}")
    for d_str in (d_en, d_es):
        _chk(110 <= len(d_str) <= 158 and d_str.endswith("."), f"SEO desc budget failed: {len(d_str)} {d_str!r}")
        _chk(not FORMULA_RE.search(d_str), f"Formula char in SEO desc: {d_str!r}")
        _chk(not MEDICAL_RE.search(d_str), f"Medical term in SEO desc: {d_str!r}")
        last_word = re.findall(r"[\wÀ-ÿ]+", d_str)[-1].lower()
        _chk(last_word not in DANGLING_WORDS, f"Dangling end word in SEO desc: {d_str!r}")

    pairs = _collect_bilingual_pairs(ESSAY)
    cache = json.loads((ROOT / "data" / "folio-citations.cache.json").read_text(encoding="utf-8"))
    source_dois = [s["doi"].lower() for s in ESSAY["sources"]]
    _chk(tuple(source_dois) == EXPECTED_DOIS, f"Unexpected source DOIs: {source_dois}")
    def _fold(s: str) -> str:
        return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii").lower()
    for src in ESSAY["sources"]:
        doi = src["doi"].lower()
        entry = cache.get(f"doi:{doi}", {})
        _chk(bool(entry.get("found")), f"Uncached DOI {doi}")
        _chk(entry.get("year") == src.get("year"), f"Year mismatch for {doi}: {entry.get('year')} != {src.get('year')}")
        first_author = str(entry.get("first_author") or "")
        _chk(bool(first_author) and _fold(first_author) in _fold(src["citation"]), f"Author mismatch for {doi}")

    # Standard Cross-Scale Essay prose word count metric: prose paragraphs only (matching ES.10/ES.11)
    en_prose_words = 0
    for sec in ESSAY["sections"]:
        for blk in sec["blocks"]:
            if blk["type"] == "p":
                en_prose_words += len(blk["en"].split())
            elif blk["type"] in ("bridge", "analogy"):
                for p_en, _ in blk["paras"]:
                    en_prose_words += len(p_en.split())
    _chk(1800 <= en_prose_words <= 2400, f"EN prose word budget out of 1800..2400: {en_prose_words}")

    cf_en_count = 0
    cf_es_count = 0
    for field, en_txt, es_txt in pairs:
        _chk(not DECIMAL_COMMA_RE.search(es_txt), f"es-MX decimal comma in {field}: {es_txt!r}")
        for banned in BANNED_PHRASES:
            _chk(banned not in en_txt.lower() and banned not in es_txt.lower(), f"Banned phrase {banned!r} in {field}")
        for match in INLINE_DOI_RE.finditer(en_txt + " " + es_txt):
            doi = match.group(0).rstrip(".,;)").lower()
            _chk(doi in source_dois, f"Inline DOI {doi} missing from sources")
        cf_en_count += len(re.findall(r"cystic fibrosis", en_txt, re.I))
        cf_es_count += len(re.findall(r"fibrosis quística", es_txt, re.I))
        en_nums = extract_number_tokens(en_txt)
        es_nums = extract_number_tokens(es_txt)
        _chk(en_nums == es_nums, f"EN/es-MX numeric parity mismatch in {field}: {en_nums} != {es_nums}")
    _chk(cf_en_count <= 2 and cf_es_count <= 2, f"CF mentions exceed <= 2 limit: en={cf_en_count}, es={cf_es_count}")

    skill_md = (ROOT / ESSAY["skill_path"]).read_text(encoding="utf-8")
    meta = _parse_frontmatter(skill_md)
    _chk(meta.get("name") == "essay-es12-cycle-affinity-tur-gates", "SKILL.md name mismatch")
    _chk(meta.get("license") == "MIT", "SKILL.md license mismatch")
    _chk(len(meta.get("description", "")) >= 40, "SKILL.md description missing or too short")
    _chk(bool(meta.get("compatibility")), "SKILL.md compatibility missing")
    _chk(not (ROOT / "src" / "research").exists(), "Unexpected src/research directory in informatico.ai")

    assert not failures, "; ".join(failures)

    return {
        "status": "PASS",
        "essay": CODE,
        "slug": SLUG,
        "en_prose_words": en_prose_words,
        "p_open_invariant": r_drv["p_open"],
        "cycle_affinity_j4_kbt": round(r_drv["affinity_kb"], 4),
        "q_tur_j4": round(r_drv["q_tur"], 4),
        "slope0_eq": round(burst["slope0_eq"], 4),
        "slope0_drv": round(burst["slope0_drv"], 4),
        "slope0_subthreshold": round(burst_sub["slope0_drv"], 4),
        "t_peak_drv_s": round(burst["t_peak_drv_s"], 3),
        "lean_theorems": lean["theorem_count"],
        "lean_compiled": lean["compiled"],
        "kernel_seconds": round(kernel_s, 4),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Cross-Scale Essay ES.12")
    parser.add_argument("--planted-defect", action="store_true", help="Inject defect and fail closed")
    args = parser.parse_args()
    try:
        out = run_verification(planted_defect=args.planted_defect)
        print(json.dumps(out, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
