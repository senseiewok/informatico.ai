#!/usr/bin/env python3
"""Deterministic reference artefact generator for Time & Gravity · T.10 (Page's Counting Argument).
Canonical URL: https://informatico.ai/timegravity/t10/
Writes src/timegravity/t10/files/t10_reference.json (the Haar-random toy's radiation entropy at every cut
against Page's closed form and Hawking's line) and manifest.json. Standard library only; fixed seed, reproducible.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))

from timegravity_kernel_bounds import PAGE_N_QUBITS, PAGE_SAMPLES, PAGE_SEED, PAGE_TOL_NATS, page_average_entropy, page_curve_toy  # noqa: E402

FILES_DIR = ROOT / "src" / "timegravity" / "t10" / "files"
BOUNDARY_EN = (
    "Nothing on this page is a theory of everything, and this site proposes none. Every claim carries one of "
    "six labels, each tied to a ledger row: MEASURED, DERIVED, BOUND, PROPOSED, OPEN, or SINGLE RESULT. "
    "Preprints never rise above PROPOSED. Each page ends with one open question that the next page takes up."
)


def r12(x: float) -> float:
    return float(f"{x:.12g}")


def build_reference() -> dict:
    toy = page_curve_toy()
    return {
        "folio_id": "T.10",
        "title": "Page's Counting Argument",
        "formula": "S(m,n) = sum_{k=n+1}^{mn} 1/k - (m-1)/(2n), m <= n (Page 1993, average entropy of a subsystem)",
        "parameters": {"n_qubits": PAGE_N_QUBITS, "samples": PAGE_SAMPLES, "seed": PAGE_SEED, "tolerance_nats": PAGE_TOL_NATS},
        "curve_a__toy_mean__page__hawking_line": [[c["a"], r12(c["toy_mean_nats"]), r12(c["page_nats"]), r12(c["hawking_line_nats"])] for c in toy["curve"]],
        "page_table_N_qubits__S_half_nats": [[N, r12(page_average_entropy(2 ** (N // 2), 2 ** (N - N // 2)))] for N in range(4, 13)],
        "note": "The assertion is against Page's closed form; the random states are only the sample. No island, no horizon, no gravity in the toy.",
        "boundary_en": BOUNDARY_EN,
        "license": "CC0-1.0 / CC-BY-4.0",
    }


def main() -> int:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    ref_bytes = (json.dumps(build_reference(), indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    ref_path = FILES_DIR / "t10_reference.json"
    ref_path.write_bytes(ref_bytes)
    manifest = {
        "folio_id": "T.10",
        "generator": "skills/timegravity/t10/make_t10.py",
        "verifier": "skills/timegravity/t10/verify_t10_page_curve.py",
        "license": "CC0-1.0 / CC-BY-4.0",
        "boundary_en": BOUNDARY_EN,
        "files": [{"filename": ref_path.name, "bytes": len(ref_bytes), "sha256": hashlib.sha256(ref_bytes).hexdigest()}],
    }
    (FILES_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PASS: T.10 reference artefact written ({len(ref_bytes)} bytes, sha256 {manifest['files'][0]['sha256'][:12]}...).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
