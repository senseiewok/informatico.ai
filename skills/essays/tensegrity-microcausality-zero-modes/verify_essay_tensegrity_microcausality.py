#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic standalone Python verifier for Cross-Scale Essay ES.04 · Tensegrity, Microcausality & Zero Modes.

Verifies:
  1. Map A — Pure-Python Gaussian elimination on the 3D internal rigidity matrix R in R^{E x (3V - 6)}:
     - Regular convex octahedron (V = 6, E = 12, D = 12): rank = 12, N_floppy = 0, N_self_stress = 0.
     - V = 8 cubic truss bracing sequence (D = 18): E = 12 -> 18 collapses N_floppy: 6 -> 0 with
       N_self_stress = 0; 7th diagonal brace (E = 19) yields rank = 18, N_floppy = 0, N_self_stress = 1;
       coplanar misplaced 6th brace (E = 18) drops rank = 17, N_floppy = 1, N_self_stress = 1.
     - 3-prism tensegrity simplex (Calladine 1978, V = 6, E = 12): rank = 11 (N_floppy = 1,
       N_self_stress = 1) at 30 deg twist vs rank = 12 at generic 0.7 rad twist.
  2. Map B — Explicit 54 x 15 real normalizer-commutator matrix C_loc on su(4):
     - Exact rank = 9, nullity = 6 (su(2)_A + su(2)_B), cokernel = 45 (index 6 - 45 = 15 - 54 = -39),
       collapsing all 9 continuous Cartan-Weyl non-local refactorization modes (9 -> 0).
     - Exact 2-mass BMV entanglement negativity N = 0.078162 (M = 10^-14 kg, d = 450 um,
       Delta_x = 250 um, T = 2.5 s), cross-checked against tools/timegravity_kernel_entangle.py,
       invariant to < 10^-13 across connected local SU(2)_A x SU(2)_B unitaries and discrete SWAP_AB,
       while unconstrained exp(i (Delta_phi/4) sigma_z x sigma_z) erases N to 0.
  3. ESSAY schema, SEO bounds, scope caveats (PROPOSED preprint ceiling on arXiv:2608.16732 and
     discrete SWAP_AB), proportional CF framing (<= 3 mentions, < 12% of <p> blocks), cached DOIs,
     companion SKILL.md frontmatter (license: CC0-1.0), and 100% EN / es-MX numeric token parity.

Supports `--planted-defect`, which activates naive scalar Maxwell counting (missing rank drops)
and drops the 54 x 15 microcausality constraint (unleashing 9 non-local zero modes that erase
BMV negativity to 0), and must exit non-zero (1).
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

from folios.essays.e04_tensegrity_microcausality import (  # noqa: E402
    ESSAY,
    evaluate_essay_es04,
    extract_number_tokens,
)
from timegravity_kernel_entangle import check_bmv as tg_check_bmv  # noqa: E402

FORMULA_RE = re.compile(r"[=√∂²³∑∫δ_^]|\bexp\(")
DANGLING_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "with", "by", "for", "under",
    "y", "de", "del", "la", "el", "los", "las", "en", "con", "por",
}
DECIMAL_COMMA_RE = re.compile(r"\d,\d{1,2}(?!\d)")
INLINE_DOI_RE = re.compile(r"10\.\d{4,9}/[^\s,;)\"']+")
ALLOWED_BLOCK_TYPES = {"p", "bridge", "analogy", "equation", "table"}


def _parse_frontmatter(md_text: str) -> dict[str, str]:
    lines = md_text.splitlines()
    assert lines and lines[0].strip() == "---", "SKILL.md must start with --- YAML frontmatter"
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    assert end_idx is not None, "SKILL.md missing closing --- frontmatter fence"
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
            assert btype in ALLOWED_BLOCK_TYPES, f"Unsupported block type: {btype!r}"
            if btype == "p":
                pairs.append((f"section[{s_idx}].block[{b_idx}].p", blk["en"], blk["es"]))
            elif btype in ("bridge", "analogy"):
                pairs.append((f"section[{s_idx}].block[{b_idx}].kicker", blk["kicker_en"], blk["kicker_es"]))
                if blk.get("title_en") or blk.get("title_es"):
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
    required_keys = (
        "code", "slug", "plate_slug", "date", "seo",
        "kicker_en", "kicker_es", "reading_time_en", "reading_time_es",
        "title_en", "title_es", "standfirst_en", "standfirst_es",
        "card_dek_en", "card_dek_es", "instrument_kind", "predict",
        "sections", "sidenotes", "sources", "skill_path", "verifier_path",
        "ai_line_en", "ai_line_es",
    )
    for k in required_keys:
        assert k in ESSAY, f"ESSAY missing required key {k!r}"

    assert ESSAY["code"] == "ES.04"
    assert ESSAY["slug"] == "tensegrity-microcausality-zero-modes"
    assert ESSAY["plate_slug"] == "essay04"
    assert ESSAY["instrument_kind"] == "kinematic"
    assert ESSAY["date"] == "2026-11-10"
    assert ESSAY["skill_path"] == "skills/essays/tensegrity-microcausality-zero-modes/SKILL.md"
    assert ESSAY["verifier_path"] == "skills/essays/tensegrity-microcausality-zero-modes/verify_essay_tensegrity_microcausality.py"
    assert len(ESSAY["sections"]) == 5
    assert 4 <= len(ESSAY["sidenotes"]) <= 5
    assert 7 <= len(ESSAY["sources"]) <= 10

    t_en, d_en, t_es, d_es = ESSAY["seo"]
    assert t_en != t_es, "SEO title_en and title_es must be distinct"
    for label, title in (("title_en", t_en), ("title_es", t_es)):
        assert 18 <= len(title) <= 52, f"{label} length {len(title)} outside [18, 52]: {title!r}"
        assert "informatico" not in title.lower(), f"{label} must omit brand suffix"
    for label, desc in (("desc_en", d_en), ("desc_es", d_es)):
        assert 110 <= len(desc) <= 158, f"{label} length {len(desc)} outside [110, 158]: {desc!r}"
        assert desc.endswith("."), f"{label} must end with period: {desc!r}"
        assert FORMULA_RE.search(desc) is None, f"{label} contains forbidden formula symbol: {desc!r}"
        assert "medical" not in desc.lower() and "médic" not in desc.lower(), f"{label} contains forbidden medical term"
        last_word = re.findall(r"[\wÀ-ÿ]+", desc)[-1].lower()
        assert last_word not in DANGLING_WORDS, f"{label} ends on dangling word {last_word!r}"

    # Word count & paragraph proportionality checks
    prose_words_en = 0
    all_words_en = 0
    p_blocks_en: list[str] = []
    all_en_chunks: list[str] = [ESSAY["title_en"], ESSAY["standfirst_en"], ESSAY["card_dek_en"]]
    all_es_chunks: list[str] = [ESSAY["title_es"], ESSAY["standfirst_es"], ESSAY["card_dek_es"]]

    roman_prefixes = ("I · ", "II · ", "III · ", "IV · ", "V · ")
    for idx, sec in enumerate(ESSAY["sections"]):
        assert sec["h2_en"].startswith(roman_prefixes[idx]), f"Section {idx+1} h2_en prefix mismatch"
        assert sec["h2_es"].startswith(roman_prefixes[idx]), f"Section {idx+1} h2_es prefix mismatch"
        all_words_en += len(sec["h2_en"].split())
        all_en_chunks.append(sec["h2_en"])
        all_es_chunks.append(sec["h2_es"])
        for blk in sec["blocks"]:
            btype = blk["type"]
            if btype == "p":
                w = len(blk["en"].split())
                prose_words_en += w
                all_words_en += w
                p_blocks_en.append(blk["en"])
                all_en_chunks.append(blk["en"])
                all_es_chunks.append(blk["es"])
            elif btype in ("bridge", "analogy"):
                all_words_en += len(blk["kicker_en"].split()) + len(blk.get("title_en", "").split())
                all_en_chunks.append(blk["kicker_en"] + " " + blk.get("title_en", ""))
                all_es_chunks.append(blk["kicker_es"] + " " + blk.get("title_es", ""))
                for p_en, p_es in blk["paras"]:
                    w = len(p_en.split())
                    prose_words_en += w
                    all_words_en += w
                    p_blocks_en.append(p_en)
                    all_en_chunks.append(p_en)
                    all_es_chunks.append(p_es)
            elif btype == "equation":
                all_words_en += len(blk["label_en"].split()) + len(blk["note_en"].split())
                all_en_chunks.append(blk["label_en"] + " " + blk["note_en"])
                all_es_chunks.append(blk["label_es"] + " " + blk["note_es"])
            elif btype == "table":
                all_words_en += len(blk["caption_en"].split()) + sum(len(h.split()) for h in blk["headers_en"])
                all_words_en += sum(len(c_en.split()) for row in blk["rows"] for c_en, _ in row)
                all_en_chunks.append(blk["caption_en"] + " " + " ".join(blk["headers_en"]))
                all_es_chunks.append(blk["caption_es"] + " " + " ".join(blk["headers_es"]))
                for row in blk["rows"]:
                    all_en_chunks.append(" ".join(c[0] for c in row))
                    all_es_chunks.append(" ".join(c[1] for c in row))

    assert 1800 <= prose_words_en <= 2600, f"English prose words {prose_words_en} outside [1800, 2600]"
    assert 1800 <= all_words_en <= 2600, f"English all-section words {all_words_en} outside [1800, 2600]"

    for sn in ESSAY["sidenotes"]:
        all_en_chunks.append(sn["label_en"] + " " + sn["en"])
        all_es_chunks.append(sn["label_es"] + " " + sn["es"])
    for src in ESSAY["sources"]:
        all_en_chunks.append(src["role_en"])
        all_es_chunks.append(src["role_es"])

    full_en = " ".join(all_en_chunks)
    full_es = " ".join(all_es_chunks)

    # Proportional CF / CFTR framing guardrail (<= 3 mentions across essay, < 12% of <p> blocks)
    cf_en_mentions = len(re.findall(r"\bcftr\b|cystic fibrosis", full_en, flags=re.IGNORECASE))
    cf_es_mentions = len(re.findall(r"\bcftr\b|fibrosis qu[ií]stica", full_es, flags=re.IGNORECASE))
    assert cf_en_mentions <= 3, f"Expected <= 3 CFTR/CF mentions in EN prose, found {cf_en_mentions}"
    assert cf_es_mentions <= 3, f"Expected <= 3 CFTR/CF mentions in ES prose, found {cf_es_mentions}"
    cf_p_hits = sum(1 for p in p_blocks_en if re.search(r"\bcftr\b|cystic fibrosis", p, flags=re.IGNORECASE))
    cf_p_ratio = cf_p_hits / max(len(p_blocks_en), 1)
    assert cf_p_ratio < 0.12, f"CF paragraph fraction {cf_p_ratio:.3f} ({cf_p_hits}/{len(p_blocks_en)}) >= 0.12"

    # Required Carbon Audit scope caveats: Stoica PROPOSED preprint & discrete SWAP_AB
    assert "PROPOSED" in full_en and "preprint" in full_en.lower(), "Stoica (2026) must be marked PROPOSED preprint in EN"
    assert "PROPOSED" in full_es and "prepublicación" in full_es.lower(), "Stoica (2026) must be marked PROPOSED preprint in ES"
    assert "SWAP_AB" in full_en and "SWAP_AB" in full_es, "Discrete SWAP_AB coset caveat must appear in EN and ES"

    # Offline Crossref / DataCite cache check
    cache_path = ROOT / "data" / "folio-citations.cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8"))
    seen_ids: set[str] = set()
    for src in ESSAY["sources"]:
        sid = src["id"]
        assert sid.startswith("ES04-") and sid not in seen_ids, f"Invalid or duplicate source id {sid!r}"
        seen_ids.add(sid)
        doi = src["doi"].strip()
        rec = cache.get(f"doi:{doi.lower()}")
        assert rec and rec.get("found") is True, f"Uncached DOI in sources: {doi}"
        if rec.get("year"):
            assert abs(int(rec["year"]) - int(src["year"])) <= 1, (
                f"Source {sid} year {src['year']} disagrees with cached year {rec['year']}"
            )

    for inline_doi in set(INLINE_DOI_RE.findall(full_en + " " + full_es)):
        cleaned = inline_doi.rstrip(".")
        rec = cache.get(f"doi:{cleaned.lower()}")
        assert rec and rec.get("found") is True, f"Uncached inline DOI: {cleaned}"

    # Exact EN / es-MX numeric parity & Mexican Spanish '.' decimal rule
    pairs = _collect_bilingual_pairs(ESSAY)
    for label, en_txt, es_txt in pairs:
        nums_en = extract_number_tokens(en_txt)
        nums_es = extract_number_tokens(es_txt)
        assert nums_en == nums_es, f"Numeric parity mismatch in {label}: EN={nums_en} vs ES={nums_es}"
        assert DECIMAL_COMMA_RE.search(es_txt) is None, f"Forbidden decimal comma in es-MX ({label}): {es_txt!r}"

    # Companion SKILL.md frontmatter check
    skill_file = ROOT / ESSAY["skill_path"]
    verifier_file = ROOT / ESSAY["verifier_path"]
    assert skill_file.is_file(), f"Missing SKILL.md at {skill_file}"
    assert verifier_file.is_file(), f"Missing verifier at {verifier_file}"
    fm = _parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    assert fm.get("name") == "essay-es04-tensegrity-microcausality-zero-modes"
    assert fm.get("license") == "CC0-1.0", f"Expected license: CC0-1.0, got {fm.get('license')!r}"
    assert fm.get("description") and fm.get("compatibility")

    return {
        "prose_words_en": prose_words_en,
        "all_section_words_en": all_words_en,
        "paragraph_blocks": len(p_blocks_en),
        "cf_paragraph_ratio": round(cf_p_ratio, 4),
        "cf_mentions_en": cf_en_mentions,
        "cf_mentions_es": cf_es_mentions,
        "bilingual_pairs_checked": len(pairs),
        "cached_sources_verified": len(ESSAY["sources"]),
        "seo_lengths": {
            "title_en": len(t_en),
            "desc_en": len(d_en),
            "title_es": len(t_es),
            "desc_es": len(d_es),
        },
    }


def verify_physics_and_algebra(planted_defect: bool = False) -> dict:
    res = evaluate_essay_es04(planted_defect=planted_defect)
    truss = res["truss"]
    q = res["quantum"]

    # 1. Map A: 3D Space-Frame Rigidity Matrix R in R^{E x (3V - 6)}
    octa = truss["regular_octahedron"]
    assert octa["matrix_shape"] == (12, 12)
    assert octa["rank"] == 12 and octa["n_floppy"] == 0 and octa["n_self_stress"] == 0

    steps = truss["steps"]
    assert len(steps) == 8
    for k in range(7):
        st = steps[k]
        assert st["matrix_shape"] == (12 + k, 18)
        assert st["rank"] == 12 + k
        assert st["n_floppy"] == 6 - k
        assert st["n_self_stress"] == 0
        assert st["calladine_identity_holds"] is True

    st7 = steps[7]
    assert st7["matrix_shape"] == (19, 18)
    assert st7["rank"] == 18 and st7["n_floppy"] == 0 and st7["n_self_stress"] == 1
    assert st7["maxwell_index"] == -1 and st7["calladine_identity_holds"] is True

    # Planted-defect gate 1: coplanar double-brace on V=8, E=18 cube & 30 deg tensegrity 3-prism
    misplaced = truss["misplaced_18bar_cube"]
    assert misplaced["rank"] == 17 and misplaced["n_floppy"] == 1 and misplaced["n_self_stress"] == 1, (
        f"Coplanar misplaced 18-bar cube failed rank check: got rank={misplaced['rank']}, "
        f"N_floppy={misplaced['n_floppy']}, N_self_stress={misplaced['n_self_stress']} (scalar Maxwell defect active)"
    )
    tens30 = truss["tensegrity_simplex_30deg"]
    tens_gen = truss["tensegrity_simplex_generic"]
    assert tens_gen["rank"] == 12 and tens_gen["n_self_stress"] == 0
    assert tens30["rank"] == 11 and tens30["n_floppy"] == 1 and tens30["n_self_stress"] == 1, (
        f"30 deg tensegrity simplex failed Calladine prestress rank drop: got rank={tens30['rank']}"
    )

    # 2. Map B: Explicit 54 x 15 su(4) Normalizer-Commutator Matrix & BMV Witness
    assert q["basis_count"] == 15
    assert q["max_gram_orthonormality_err"] < 1.0e-14

    c_audit = q["c_loc_audit"]
    assert c_audit["rows_E"] == 54 and c_audit["cols_D"] == 15
    assert c_audit["index_exact"] is True and c_audit["index_lhs"] == -39

    # Planted-defect gate 2: microcausality must lock all 9 non-local Cartan-Weyl modes (rank = 9, nullity = 6)
    assert c_audit["rank"] == 9 and c_audit["nullity"] == 6 and c_audit["cokernel"] == 45, (
        f"su(4) normalizer matrix C_loc failed rank-9 locality lock: rank={c_audit['rank']}, "
        f"nullity={c_audit['nullity']} (missing microcausality constraint defect active)"
    )
    assert q["local_columns_max_residual"] < 1.0e-14
    assert q["nonlocal_submatrix_rank"] == 9 and q["free_nonlocal_modes"] == 0
    assert math.isclose(q["zz_constraint_norm"], 4.0, rel_tol=1.0e-12)

    # Cross-check BMV negativity against tools/timegravity_kernel_entangle.py
    tg_bmv = tg_check_bmv()
    assert abs(q["bmv_delta_phi_rad"] - tg_bmv["entanglement_phase_rad"]) < 1.0e-12
    assert abs(q["bmv_concurrence"] - tg_bmv["concurrence_closed"]) < 1.0e-12
    assert abs(q["bmv_negativity"] - tg_bmv["negativity"]) < 1.0e-12
    assert round(q["bmv_negativity"], 6) == 0.078162
    assert q["bmv_negativity_closed_diff"] < 1.0e-14
    assert q["max_local_gauge_negativity_drift"] < 1.0e-13
    assert q["swap_ab_negativity_drift"] < 1.0e-14
    assert q["unconstrained_refactorized_negativity"] < 1.0e-14
    assert abs(q["effective_witness_min_negativity"] - q["bmv_negativity"]) < 1.0e-14

    return res


def main() -> int:
    planted = "--planted-defect" in sys.argv
    try:
        meta = verify_metadata_and_parity()
        phys = verify_physics_and_algebra(planted_defect=planted)

        # Internal self-check on normal runs confirming planted_defect=True is deterministically rejected
        defect_caught = False
        try:
            verify_physics_and_algebra(planted_defect=True)
        except AssertionError:
            defect_caught = True
        assert defect_caught, "Internal self-check failed: planted_defect=True was not rejected"

        truss = phys["truss"]
        q = phys["quantum"]
        payload = {
            "status": "PASS",
            "folio_id": "ES.04",
            "essay": "ES.04",
            "slug": "tensegrity-microcausality-zero-modes",
            "verified_benchmarks": {
                "cube_unbraced_12bars": {
                    "shape": list(truss["steps"][0]["matrix_shape"]),
                    "rank": truss["steps"][0]["rank"],
                    "n_floppy": truss["steps"][0]["n_floppy"],
                    "n_self_stress": truss["steps"][0]["n_self_stress"],
                },
                "cube_isostatic_18bars": {
                    "shape": list(truss["steps"][6]["matrix_shape"]),
                    "rank": truss["steps"][6]["rank"],
                    "n_floppy": truss["steps"][6]["n_floppy"],
                    "n_self_stress": truss["steps"][6]["n_self_stress"],
                },
                "cube_overconstrained_19bars": {
                    "shape": list(truss["steps"][7]["matrix_shape"]),
                    "rank": truss["steps"][7]["rank"],
                    "n_floppy": truss["steps"][7]["n_floppy"],
                    "n_self_stress": truss["steps"][7]["n_self_stress"],
                },
                "cube_misplaced_18bars_rank": truss["misplaced_18bar_cube"]["rank"],
                "tensegrity_3prism_30deg_rank": truss["tensegrity_simplex_30deg"]["rank"],
                "octahedron_12bars_rank": truss["regular_octahedron"]["rank"],
                "su4_normalizer_shape": [q["c_loc_audit"]["rows_E"], q["c_loc_audit"]["cols_D"]],
                "su4_normalizer_rank": q["c_loc_audit"]["rank"],
                "su4_normalizer_nullity": q["c_loc_audit"]["nullity"],
                "su4_normalizer_cokernel": q["c_loc_audit"]["cokernel"],
                "free_nonlocal_modes_after_microcausality": q["free_nonlocal_modes"],
                "bmv_delta_phi_rad": round(q["bmv_delta_phi_rad"], 6),
                "bmv_concurrence": round(q["bmv_concurrence"], 6),
                "bmv_negativity": round(q["bmv_negativity"], 6),
                "max_local_gauge_negativity_drift": q["max_local_gauge_negativity_drift"],
                "swap_ab_negativity_drift": q["swap_ab_negativity_drift"],
            },
            "planted_defect_self_test": "REJECTED_AS_EXPECTED",
            "metadata_checks": meta,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    except AssertionError as exc:
        print(
            json.dumps(
                {
                    "status": "FAIL",
                    "folio_id": "ES.04",
                    "essay": "ES.04",
                    "slug": "tensegrity-microcausality-zero-modes",
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
