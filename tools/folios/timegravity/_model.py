# -*- coding: utf-8 -*-
"""Tiny content model for Time & Gravity pages.

A paragraph is a list of segments. Every segment carries both languages, so the generator can emit
`data-en`/`data-es` on each piece and the Spanish twin keeps the same claim-span sequence by construction.

  T(en, es)                              plain text: transitions, questions, definitions (no label)
  C(label, ids, en, es, parent=None)     a claim span: label + ledger ids (+ parent MEASURED row for DERIVED)
"""
from __future__ import annotations


def T(en: str, es: str) -> dict:
    return {"kind": "text", "en": en, "es": es}


def C(
    label: str,
    ids: list[str] | tuple[str, ...],
    en: str,
    es: str,
    parent: str | None = None,
    kernel: str | None = None,
    scope: str | None = None,
) -> dict:
    seg = {"kind": "claim", "label": label, "ids": list(ids), "en": en, "es": es}
    if parent:
        seg["parent"] = parent
    if kernel:
        seg["kernel"] = kernel
    if scope:
        seg["scope"] = scope
    return seg


def P(*segments: dict) -> dict:
    return {"type": "p", "segments": list(segments)}


def H3(en: str, es: str, anchor: str = "") -> dict:
    return {"type": "h3", "en": en, "es": es, "anchor": anchor}
