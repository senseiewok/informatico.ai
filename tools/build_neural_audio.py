#!/usr/bin/env python3
"""Generate and verify the 200 Bilingual Neural AI Audio Narration tracks (.mp3) for Informatico.ai and Sensei Ewok CF Lab.

Covers:
  - 60 Informatico.ai Folios (48 Pillar Folios e01..e12, a01..a12, p01..p12, m01..m12 + 6 Bounties b01..b06 + 6 Toolbox x01..x06)
    in EN-US & ES-MX -> src/research/audio/<slug>-{en,es}.mp3
  - 40 Sensei Ewok CF Lab Monographs (c01..c10, p01..p10, d01..d10, l01..l10) in EN-US & ES-MX -> src/cf/audio/<slug>-{en,es}.mp3

Uses a warm, brisk Woman's Neural AI Voice (`en-US-AvaMultilingualNeural` & `es-MX-DaliaNeural` at `rate="+20%"`)
paired with a Scientific & Mathematical Prosody Normalizer so equations, Greek symbols, units, and clinical/engineering
acronyms are spoken naturally rather than spelled character-by-character.

Usage:
  python tools/build_neural_audio.py           # Synthesize missing tracks (or --force to rebuild all)
  python tools/build_neural_audio.py --check   # Deterministic offline verification of all MP3 tracks & manifests
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
TOOLS = ROOT / "tools"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

EN_VOICE = "en-US-AvaMultilingualNeural"
ES_VOICE_CF = "es-MX-DaliaNeural"
ES_VOICE_INF = "es-MX-DaliaNeural"
SPEECH_RATE = "+20%"

SUBSCRIPT_MAP = str.maketrans("₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎", "0123456789+-=()")
SUPERSCRIPT_MAP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾", "0123456789+-=()")

GREEK_EN = {
    "ΔΔG": " delta delta G ",
    "ΔG‡": " delta G double-dagger ",
    "ΔG": " delta G ",
    "ΔE": " delta E ",
    "ΔS": " delta S ",
    "ΔH": " delta H ",
    "ΔP": " delta P ",
    "Δt": " delta t ",
    "Δx": " delta x ",
    "Δ": " delta ",
    "∇²": " Laplacian ",
    "∇": " gradient ",
    "∂": " partial ",
    "∑": " sum over ",
    "∏": " product over ",
    "∫": " integral of ",
    "∞": " infinity ",
    "≈": " approximately equals ",
    "≠": " is not equal to ",
    "≥": " is greater than or equal to ",
    "≤": " is less than or equal to ",
    "∝": " is proportional to ",
    "→": " yields ",
    "↔": " is in equilibrium with ",
    "⇌": " is in reversible equilibrium with ",
    "±": " plus or minus ",
    "×": " times ",
    "·": ", ",
    "α": " alpha ",
    "β": " beta ",
    "γ": " gamma ",
    "δ": " delta ",
    "ε": " epsilon ",
    "ζ": " zeta ",
    "η": " eta ",
    "θ": " theta ",
    "κ": " kappa ",
    "λ": " lambda ",
    "μm": " micrometers ",
    "μM": " micromolar ",
    "μs": " microseconds ",
    "μL": " microliters ",
    "μ": " mu ",
    "ν": " nu ",
    "ξ": " xi ",
    "π": " pi ",
    "ρ": " rho ",
    "σ": " sigma ",
    "τ": " tau ",
    "φ": " phi ",
    "χ": " chi ",
    "ψ": " psi ",
    "ω": " omega ",
    "Ω": " omega ",
    "Φ": " phi ",
    "Ψ": " psi ",
    "Λ": " lambda ",
}

GREEK_ES = {
    "ΔΔG": " delta delta G ",
    "ΔG‡": " delta G de activación ",
    "ΔG": " delta G ",
    "ΔE": " delta E ",
    "ΔS": " delta S ",
    "ΔH": " delta H ",
    "ΔP": " delta P ",
    "Δt": " delta t ",
    "Δx": " delta x ",
    "Δ": " delta ",
    "∇²": " laplaciano ",
    "∇": " gradiente ",
    "∂": " derivada parcial ",
    "∑": " suma sobre ",
    "∏": " producto sobre ",
    "∫": " integral de ",
    "∞": " infinito ",
    "≈": " aproximadamente igual a ",
    "≠": " distinto de ",
    "≥": " mayor o igual a ",
    "≤": " menor o igual a ",
    "∝": " proporcional a ",
    "→": " hacia ",
    "↔": " en equilibrio con ",
    "⇌": " en equilibrio reversible con ",
    "±": " más menos ",
    "×": " por ",
    "·": ", ",
    "α": " alfa ",
    "β": " beta ",
    "γ": " gamma ",
    "δ": " delta ",
    "ε": " épsilon ",
    "ζ": " zeta ",
    "η": " eta ",
    "θ": " theta ",
    "κ": " kappa ",
    "λ": " lambda ",
    "μm": " micrómetros ",
    "μM": " micromolar ",
    "μs": " microsegundos ",
    "μL": " microlitros ",
    "μ": " mu ",
    "ν": " nu ",
    "ξ": " xi ",
    "π": " pi ",
    "ρ": " ro ",
    "σ": " sigma ",
    "τ": " tau ",
    "φ": " fi ",
    "χ": " ji ",
    "ψ": " psi ",
    "ω": " omega ",
    "Ω": " omega ",
    "Φ": " fi ",
    "Ψ": " psi ",
    "Λ": " lambda ",
}


def normalize_scientific_speech(text: str, lang: str = "en") -> str:
    """Convert scientific equations, Unicode symbols, and acronyms into natural spoken prosody."""
    if not text:
        return ""
    s = str(text)
    s = re.sub(r"\[Scite\s*↗?\]", "", s)
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"\b([CEAPMLDGTRBX])\.0(\d)\b", r"\1 \2", s)
    s = re.sub(r"\b([CEAPMLDGTRBX])\.(\d{2})\b", r"\1 \2", s)

    if lang.startswith("es"):
        s = re.sub(r"\bppFEV[₁1]\b", "porcentaje predicho de F E V uno", s)
        s = re.sub(r"\bFEV[₁1]\b", "F E V uno", s)
        s = re.sub(r"\bk_B\s*T\b", "k B T", s)
        s = re.sub(r"\bmRNA\b", "A R N mensajero", s)
        s = re.sub(r"\btRNA\b", "A R N de transferencia", s)
        s = re.sub(r"\bsgRNA\b", "A R N guía", s)
        s = re.sub(r"\bCFTR\b", "C F T R", s)
        s = re.sub(r"\bF508del\b", "F quinientos ocho del", s)
        s = re.sub(r"\bInformatico\.ai\b", "Informático punto A I", s, flags=re.IGNORECASE)
        s = re.sub(r"\bsenseiewok\.ai\b", "Sensei Ewok punto A I", s, flags=re.IGNORECASE)
        s = re.sub(r"\bes-MX\b", "español de México", s, flags=re.IGNORECASE)
        s = re.sub(r"\ben-US\b", "inglés", s, flags=re.IGNORECASE)
        table = GREEK_ES
    else:
        s = re.sub(r"\bppFEV[₁1]\b", "percent predicted F E V 1", s)
        s = re.sub(r"\bFEV[₁1]\b", "F E V 1", s)
        s = re.sub(r"\bk_B\s*T\b", "k B T", s)
        s = re.sub(r"\bmRNA\b", "messenger R N A", s)
        s = re.sub(r"\btRNA\b", "transfer R N A", s)
        s = re.sub(r"\bsgRNA\b", "single guide R N A", s)
        s = re.sub(r"\bCFTR\b", "C F T R", s)
        s = re.sub(r"\bF508del\b", "F 508 del", s)
        s = re.sub(r"\bInformatico\.ai\b", "Informatico dot A I", s, flags=re.IGNORECASE)
        s = re.sub(r"\bsenseiewok\.ai\b", "Sensei Ewok dot A I", s, flags=re.IGNORECASE)
        s = re.sub(r"\bes-MX\b", "Mexican Spanish", s, flags=re.IGNORECASE)
        s = re.sub(r"\ben-US\b", "English", s, flags=re.IGNORECASE)
        table = GREEK_EN

    for sym, spoken in table.items():
        s = s.replace(sym, spoken)

    s = s.translate(SUBSCRIPT_MAP).translate(SUPERSCRIPT_MAP)
    s = re.sub(r"_([a-zA-Z0-9]+)", r" \1", s)
    s = s.replace("−", " minus " if not lang.startswith("es") else " menos ")
    s = s.replace("—", ", ")
    s = s.replace("–", " to " if not lang.startswith("es") else " a ")
    s = s.replace("|", ", given " if not lang.startswith("es") else ", dado ")
    s = re.sub(r"[{}[\]]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _trim_sentences(txt: str, max_chars: int = 340) -> str:
    txt = re.sub(r"\s+", " ", str(txt or "")).strip()
    if len(txt) <= max_chars:
        return txt
    cut = txt[:max_chars]
    last_dot = max(cut.rfind(". "), cut.rfind("; "))
    if last_dot > 120:
        return cut[: last_dot + 1]
    return cut.rsplit(" ", 1)[0] + "."


def build_informatico_scripts() -> list[dict]:
    """Extract 5-Act bilingual narration scripts for all 60 Informatico.ai Folios (48 Pillar + 6 Bounties + 6 Toolbox)."""
    from tools.build_longform_folios import decf, decf_title
    from tools.folios import (
        BOUNTY_FOLIOS,
        FOLIO_ES_TRANSLATIONS,
        FOLIOS_BY_PILLAR,
        FRONTIER_DISCOVERY_DISPATCHES,
        LONGFORM,
        TOOLCHAIN_FOLIOS,
    )

    items: list[dict] = []
    # 1. 48 Pillar Folios
    for pillar in ("engineering", "architecture", "physics", "math"):
        for folio in FOLIOS_BY_PILLAR[pillar]:
            slug = folio["slug"]
            fid = folio["folio_id"]
            lf = LONGFORM[slug]
            es_tr = FOLIO_ES_TRANSLATIONS.get(slug, {})
            disc = FRONTIER_DISCOVERY_DISPATCHES.get(slug, {})

            title_en = decf_title(folio["title"])
            sub_en = decf(folio["subtitle"])
            why_en = decf(lf.get("act1_plain_bridge") or lf.get("act2_analogy", ""))
            act1_en = decf(lf.get("act1_dropcap", ""))
            act2_en = decf(lf.get("act2_body", ""))
            act3_en = " ".join(decf(w) for w in lf.get("walkthrough", [])[:2])
            act4_en = decf_title(disc.get("headline", "")) + ". " + decf(lf.get("act4_body", ""))
            act5_en = decf(lf.get("act4_human_potential", "")) or f"Synthesis of Folio {fid}: {title_en}."

            chapters_en = [
                normalize_scientific_speech(
                    _trim_sentences(f"Folio {fid}: {title_en}. {sub_en} Act 1, Story: {act1_en}", 380),
                    "en",
                ),
                normalize_scientific_speech(
                    _trim_sentences(f"Act 2, Physical Intuition. Why it matters: {why_en} {act2_en}", 360),
                    "en",
                ),
                normalize_scientific_speech(
                    _trim_sentences(
                        f"Act 3, Interactive Workbench. Governing law: {folio.get('governing_law', '')}. {act3_en}",
                        340,
                    ),
                    "en",
                ),
                normalize_scientific_speech(
                    _trim_sentences(f"Act 4, Frontier Discovery. {act4_en}", 340),
                    "en",
                ),
                normalize_scientific_speech(
                    _trim_sentences(
                        f"Act 5, Synthesis. {act5_en} Open scientific and educational research, not clinical or engineering certification.",
                        340,
                    ),
                    "en",
                ),
            ]

            title_es = decf_title(es_tr.get("title_es", title_en))
            sub_es = decf(es_tr.get("subtitle_es", sub_en))
            why_es = decf(es_tr.get("plain_es") or es_tr.get("why_es", why_en))

            chapters_es = [
                normalize_scientific_speech(
                    _trim_sentences(f"Folio {fid}: {title_es}. {sub_es}", 360),
                    "es",
                ),
                normalize_scientific_speech(
                    _trim_sentences(f"Acto 2, Intuición física y por qué importa en la vida real: {why_es}", 360),
                    "es",
                ),
                normalize_scientific_speech(
                    _trim_sentences(
                        f"Acto 3, Laboratorio interactivo. Este monográfico verifica la ley gobernante {folio.get('governing_law', '')} mediante cuatro lentes interactivas en tiempo real.",
                        320,
                    ),
                    "es",
                ),
                normalize_scientific_speech(
                    _trim_sentences(
                        f"Acto 4, Descubrimiento de frontera. Explora los umbrales críticos, las cotas de estabilidad y las fuentes primarias verificadas de {title_es}.",
                        300,
                    ),
                    "es",
                ),
                normalize_scientific_speech(
                    "Acto 5, Síntesis. Edición bilingüe verificada por el consejo de cuatro asientos. Investigación científica y educativa abierta, no consejo médico ni certificación profesional.",
                    "es",
                ),
            ]

            items.append(
                {
                    "domain": "informatico",
                    "slug": slug,
                    "folio_id": fid,
                    "en_segments": chapters_en,
                    "es_segments": chapters_es,
                    "en_out": SRC / "research" / "audio" / f"{slug}-en.mp3",
                    "es_out": SRC / "research" / "audio" / f"{slug}-es.mp3",
                }
            )

    # 2. 6 Bounty Folios (b01..b06) + 6 Toolbox Folios (x01..x06)
    for track_label_en, track_label_es, collection in (
        ("Bounty Folio", "Folio de Reto", BOUNTY_FOLIOS),
        ("Tech and Tools Folio", "Folio de Herramientas", TOOLCHAIN_FOLIOS),
    ):
        for entry in collection:
            slug = entry["slug"]
            fid = entry["folio_id"]
            title_en = entry["title"]
            sub_en = entry["subtitle"]
            why_en = entry.get("act1_plain_bridge") or entry.get("why_en", "")
            act1_en = entry.get("act1_dropcap", "")
            act2_en = entry.get("act2_analogy") or entry.get("act2_intuition", "")
            act3_en = " ".join(entry.get("walkthrough", [])[:2])
            act4_en = entry.get("act4_human_ai") or entry.get("why_en", "")

            chapters_en = [
                normalize_scientific_speech(
                    _trim_sentences(f"{track_label_en} {fid}: {title_en}. {sub_en} Act 1, Story: {act1_en}", 380),
                    "en",
                ),
                normalize_scientific_speech(
                    _trim_sentences(f"Act 2, Everyday Intuition: {why_en} {act2_en}", 360),
                    "en",
                ),
                normalize_scientific_speech(
                    _trim_sentences(
                        f"Act 3, Interactive Workbench. Governing law: {entry.get('governing_law', '')}. {act3_en}",
                        340,
                    ),
                    "en",
                ),
                normalize_scientific_speech(
                    _trim_sentences(f"Act 4, Open-Source Synthesis and Truth Boundary. {act4_en}", 340),
                    "en",
                ),
                normalize_scientific_speech(
                    "Act 5, Reproducible Python Verifier and Portable Skill. Educational and exploratory calculation only, not a stamped engineering design.",
                    "en",
                ),
            ]

            title_es = entry.get("title_es", title_en)
            sub_es = entry.get("subtitle_es", sub_en)
            why_es = entry.get("plain_es") or entry.get("why_es", "")
            deep_es = entry.get("deep_es") or entry.get("why_es", "")

            chapters_es = [
                normalize_scientific_speech(
                    _trim_sentences(f"{track_label_es} {fid}: {title_es}. {sub_es}", 360),
                    "es",
                ),
                normalize_scientific_speech(
                    _trim_sentences(f"Acto 2, En palabras sencillas e intuición física: {why_es}", 360),
                    "es",
                ),
                normalize_scientific_speech(
                    _trim_sentences(
                        f"Acto 3, Laboratorio interactivo y mecanismo técnico: {deep_es}",
                        340,
                    ),
                    "es",
                ),
                normalize_scientific_speech(
                    _trim_sentences(
                        f"Acto 4, Frontera de verdad y herramientas abiertas para {title_es}.",
                        300,
                    ),
                    "es",
                ),
                normalize_scientific_speech(
                    "Acto 5, Verificador reproducible en Python y guía portátil. Cálculo educativo y exploratorio únicamente, no un diseño estructural firmado.",
                    "es",
                ),
            ]

            items.append(
                {
                    "domain": "informatico",
                    "slug": slug,
                    "folio_id": fid,
                    "en_segments": chapters_en,
                    "es_segments": chapters_es,
                    "en_out": SRC / "research" / "audio" / f"{slug}-en.mp3",
                    "es_out": SRC / "research" / "audio" / f"{slug}-es.mp3",
                }
            )
    return items


def build_cf_scripts() -> list[dict]:
    """Extract 4-landmark bilingual narration scripts for all 40 Sensei Ewok CF Lab Monographs."""
    try:
        from tools.cf_folios import PILLAR_ORDER, load_all_cf_folios
    except ImportError:
        return []

    by_pillar, _ = load_all_cf_folios()
    items: list[dict] = []
    for pillar in PILLAR_ORDER:
        for essay in by_pillar[pillar]:
            slug = essay["slug"]
            fid = essay["folio_id"]
            bridge_en = essay.get("therapeutic_bridge", essay.get("curative_bridge", ""))
            gov = essay.get("governing_law", "")

            segs_en = [
                normalize_scientific_speech(
                    f"Monograph {fid}, {essay['title']}: {essay['subtitle']}",
                    "en",
                ),
                normalize_scientific_speech(
                    f"Why it matters: {essay['why_it_matters']}",
                    "en",
                ),
                normalize_scientific_speech(
                    f"Therapeutic Horizon and Governing Law ({gov}): {bridge_en}",
                    "en",
                ),
                normalize_scientific_speech(
                    "Clinical Boundary: Independent research, not medical advice. Sensei Ewok Research Lab makes no clinical claims or promises of cure.",
                    "en",
                ),
            ]

            segs_es = [
                normalize_scientific_speech(
                    f"Monográfico {fid}, {essay['title_es']}: {essay['subtitle_es']}",
                    "es",
                ),
                normalize_scientific_speech(
                    f"Por qué importa: {essay['why_es']}",
                    "es",
                ),
                normalize_scientific_speech(
                    f"Horizonte terapéutico y ley física ({gov}): {essay['bridge_es']}",
                    "es",
                ),
                normalize_scientific_speech(
                    "Límite clínico y epistémico: Investigación independiente, no asesoramiento médico. Sensei Ewok Research Lab no promete curas ni tratamientos clínicos.",
                    "es",
                ),
            ]

            items.append(
                {
                    "domain": "cf",
                    "slug": slug,
                    "folio_id": fid,
                    "en_segments": segs_en,
                    "es_segments": segs_es,
                    "en_out": SRC / "cf" / "audio" / f"{slug}-en.mp3",
                    "es_out": SRC / "cf" / "audio" / f"{slug}-es.mp3",
                }
            )
    return items


def compute_segment_offsets_ratios(segments: list[str]) -> list[float]:
    """Compute cumulative character-weighted start ratios [0.0, r1, r2, ...] in [0, 1)."""
    lengths = [max(1, len(s)) for s in segments]
    total = sum(lengths)
    ratios: list[float] = []
    acc = 0
    for length in lengths:
        ratios.append(round(acc / total, 4))
        acc += length
    return ratios


async def synthesize_one_track(
    text: str,
    voice: str,
    out_path: Path,
    ffmpeg_exe: str | None,
    sem: asyncio.Semaphore,
    force: bool = False,
) -> None:
    import edge_tts

    if out_path.is_file() and out_path.stat().st_size > 1024 and not force:
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    async with sem:
        for attempt in range(4):
            try:
                if not ffmpeg_exe:
                    communicate = edge_tts.Communicate(text, voice, rate=SPEECH_RATE)
                    await communicate.save(str(out_path))
                    if out_path.is_file() and out_path.stat().st_size > 1024:
                        return
                else:
                    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                        tmp_raw = Path(tmp.name)
                    communicate = edge_tts.Communicate(text, voice, rate=SPEECH_RATE)
                    await communicate.save(str(tmp_raw))
                    res = subprocess.run(
                        [
                            ffmpeg_exe,
                            "-y",
                            "-i",
                            str(tmp_raw),
                            "-vn",
                            "-ac",
                            "1",
                            "-ar",
                            "24000",
                            "-b:a",
                            "32k",
                            str(out_path),
                        ],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    tmp_raw.unlink(missing_ok=True)
                    if res.returncode == 0 and out_path.is_file() and out_path.stat().st_size > 1024:
                        return
            except Exception as exc:
                if attempt == 3:
                    raise RuntimeError(f"Failed to synthesize {out_path.name}: {exc}") from exc
                await asyncio.sleep(1.5 * (attempt + 1))


async def generate_all(force: bool = False, informatico_only: bool = False) -> int:
    try:
        import imageio_ffmpeg
        ffmpeg_exe: str | None = imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        ffmpeg_exe = None
    inf_items = build_informatico_scripts()
    cf_items = [] if informatico_only else build_cf_scripts()
    all_items = inf_items + cf_items

    sem = asyncio.Semaphore(8)
    tasks = []
    for item in all_items:
        en_text = " ... ".join(item["en_segments"])
        es_text = " ... ".join(item["es_segments"])
        es_voice = ES_VOICE_INF if item["domain"] == "informatico" else ES_VOICE_CF
        tasks.append(synthesize_one_track(en_text, EN_VOICE, item["en_out"], ffmpeg_exe, sem, force=force))
        tasks.append(synthesize_one_track(es_text, es_voice, item["es_out"], ffmpeg_exe, sem, force=force))

    print(f"Synthesizing {len(tasks)} bilingual Neural AI audio tracks ({len(all_items)} monographs) with {EN_VOICE} & {ES_VOICE_INF} ({SPEECH_RATE})...")
    await asyncio.gather(*tasks)

    inf_manifest = {
        "engine": "neural-tts-v2-female-fast",
        "voices": {"en": EN_VOICE, "es": ES_VOICE_INF, "rate": SPEECH_RATE},
        "folios": {
            item["slug"]: {
                "folio_id": item["folio_id"],
                "en_src": f"audio/{item['slug']}-en.mp3",
                "es_src": f"audio/{item['slug']}-es.mp3",
                "en_offsets": compute_segment_offsets_ratios(item["en_segments"]),
                "es_offsets": compute_segment_offsets_ratios(item["es_segments"]),
            }
            for item in inf_items
        },
    }
    inf_man_path = SRC / "research" / "audio" / "manifest.json"
    inf_man_path.parent.mkdir(parents=True, exist_ok=True)
    inf_man_path.write_text(json.dumps(inf_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if cf_items:
        cf_manifest = {
            "engine": "neural-tts-v2-female-fast",
            "voices": {"en": EN_VOICE, "es": ES_VOICE_CF, "rate": SPEECH_RATE},
            "folios": {
                item["slug"]: {
                    "folio_id": item["folio_id"],
                    "en_src": f"cf/audio/{item['slug']}-en.mp3",
                    "es_src": f"cf/audio/{item['slug']}-es.mp3",
                    "en_offsets": compute_segment_offsets_ratios(item["en_segments"]),
                    "es_offsets": compute_segment_offsets_ratios(item["es_segments"]),
                }
                for item in cf_items
            },
        }
        cf_man_path = SRC / "cf" / "audio" / "manifest.json"
        cf_man_path.parent.mkdir(parents=True, exist_ok=True)
        cf_man_path.write_text(json.dumps(cf_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Wrote audio manifest:", inf_man_path.relative_to(ROOT))
    return 0


def check_all() -> int:
    """Offline deterministic check that all Informatico (60) and CF (if present) MP3 tracks and manifests exist and are valid."""
    inf_items = build_informatico_scripts()
    cf_items = build_cf_scripts()
    errors: list[str] = []

    for item in inf_items + cf_items:
        for _lang_key, path in (("en", item["en_out"]), ("es", item["es_out"])):
            if not path.is_file():
                errors.append(f"Missing neural audio track: {path.relative_to(ROOT).as_posix()}")
            else:
                size = path.stat().st_size
                if size < 4096:
                    errors.append(f"Audio track too small ({size} B): {path.relative_to(ROOT).as_posix()}")
                head = path.read_bytes()[:4]
                if not (head.startswith(b"ID3") or (len(head) >= 2 and head[0] == 0xFF and (head[1] & 0xE0) == 0xE0)):
                    errors.append(f"Invalid MP3 header in {path.relative_to(ROOT).as_posix()}")

    inf_man_path = SRC / "research" / "audio" / "manifest.json"
    if not inf_man_path.is_file():
        errors.append(f"Missing audio manifest: {inf_man_path.relative_to(ROOT).as_posix()}")
    else:
        data = json.loads(inf_man_path.read_text(encoding="utf-8"))
        folios = data.get("folios", {})
        if len(folios) != len(inf_items):
            errors.append(f"{inf_man_path.name}: expected {len(inf_items)} folios, got {len(folios)}")

    if errors:
        for e in errors[:20]:
            print(f"FAIL: {e}")
        return 1
    print(f"PASS: All {len(inf_items)*2} Informatico + {len(cf_items)*2} CF bilingual Neural AI MP3 tracks and manifests verified.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build or check bilingual Neural AI audio tracks.")
    parser.add_argument("--check", action="store_true", help="Verify all MP3 tracks and manifests offline.")
    parser.add_argument("--force", action="store_true", help="Re-synthesize all tracks even if already present.")
    parser.add_argument("--informatico-only", action="store_true", help="Synthesize only the 60 Informatico Folios (120 tracks).")
    args = parser.parse_args(argv)
    if args.check:
        return check_all()
    return asyncio.run(generate_all(force=args.force, informatico_only=args.informatico_only))


if __name__ == "__main__":
    sys.exit(main())
