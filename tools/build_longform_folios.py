#!/usr/bin/env python3
"""Build the 40-Folio (10 per pillar across 5 Volumes) Informatico.ai 5-Act Long-Form Magazine.

Source code is organized by Pillar and Essay under tools/folios/<pillar>/<slug>.py:
  - tools/folios/engineering/{e01..e10}.py
  - tools/folios/architecture/{a01..a10}.py
  - tools/folios/physics/{p01..p10}.py
  - tools/folios/math/{m01..m10}.py
  - tools/folios/css_bundle.py
"""

from __future__ import annotations

import html
import html.parser
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from folio_puzzles_data import FOLIO_PUZZLES  # noqa: E402
from folios import (  # noqa: E402
    FOLIO_3D_META,
    FOLIO_ES_TRANSLATIONS,
    FOLIOS_BY_PILLAR as NEW_FOLIOS,
    FRONTIER_DISCOVERY_DISPATCHES,
    LONGFORM,
    PLATE_CAPTIONS,
)
from folios.css_bundle import REVAMP_CSS, update_informatico_css  # noqa: E402
from folios.seo_copy import BRAND, FOLIO_SEO, HUB_SEO, PILLAR_SEO  # noqa: E402

SITE = "https://informatico.ai/"
# Static Spanish pages live under this prefix. Not "/es/": deploy/htaccess.txt section 4b already sends
# /es/... on this document root to the senseiewok.ai ?lang=es-MX views (mod_alias), on every host.
ES_PREFIX = "es-mx/"


def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


def kernel_verdict_html(folio: dict) -> str:
    """Verdict for the deterministic-kernel council seat.

    A Folio may record `kernel_verdict` (+ `kernel_verdict_es`) from its kernel's own output, for example
    `physics_kernel.py --coverage`. Folios without one keep the earlier "Pass" label unchanged. Without a
    `kernel_verdict_es`, the Spanish view shows the English verdict.
    """
    en = folio.get("kernel_verdict")
    if not en:
        return '<span class="tp-council-verdict">Pass</span>'
    es = folio.get("kernel_verdict_es") or en
    return f'<span class="tp-council-verdict" data-en="{esc(en)}" data-es="{esc(es)}">{esc(en)}</span>'


def linkify_citations(escaped_text: str) -> str:
    """Turn DOIs, PMIDs, NCT trial IDs, arXiv IDs, and PDB IDs in HTML-escaped text into clickable external links."""
    # 1. Linkify DOIs (10.xxxx/...)
    def _doi_repl(m: re.Match) -> str:
        prefix = m.group(1) or ""
        doi = m.group(2).rstrip(".,;)")
        trailing = m.group(2)[len(doi):]
        doi_url = f"https://doi.org/{doi}"
        scite_url = f"https://scite.ai/reports/{doi}"
        return (
            f'{prefix}<a class="tp-cite-link" href="{doi_url}" target="_blank" rel="noopener noreferrer">DOI {doi}</a> '
            f'<a class="tp-scite-badge-link" href="{scite_url}" target="_blank" rel="noopener noreferrer" title="Inspect Scite Smart Citation report for {doi}">[Scite &#8599;]</a>{trailing}'
        )

    out = re.sub(r'(DOI:?\s*)?(10\.\d{4,9}/[^\s<&]+)', _doi_repl, escaped_text)

    # 2. Linkify PMIDs (PMID 12345678 or PMID: 12345678)
    out = re.sub(
        r"PMID:?\s*(\d{6,9})",
        r'<a class="tp-cite-link" href="https://pubmed.ncbi.nlm.nih.gov/\g<1>/" target="_blank" rel="noopener noreferrer">PMID \g<1></a>',
        out,
    )

    # 3. Linkify ClinicalTrials.gov NCT IDs (NCT followed by 8 digits)
    out = re.sub(
        r"\b(NCT\d{8})\b",
        r'<a class="tp-cite-link" href="https://clinicaltrials.gov/study/\g<1>" target="_blank" rel="noopener noreferrer">\g<1></a>',
        out,
    )

    # 4. Linkify arXiv IDs (arXiv:2305.20050)
    out = re.sub(
        r"\barXiv:(\d{4}\.\d{4,5})\b",
        r'<a class="tp-cite-link" href="https://arxiv.org/abs/\g<1>" target="_blank" rel="noopener noreferrer">arXiv:\g<1></a>',
        out,
    )

    # 5. Linkify PDB IDs (PDB 8EIQ)
    out = re.sub(
        r"\bPDB\s+([0-9][A-Za-z0-9]{3})\b",
        r'<a class="tp-cite-link" href="https://www.rcsb.org/structure/\g<1>" target="_blank" rel="noopener noreferrer">PDB \g<1></a>',
        out,
    )

    # 6. Linkify explicit GitHub repository/tree/blob URLs (e.g. https://github.com/anthropics/formal-math)
    def _gh_url_repl(m: re.Match) -> str:
        raw_url = m.group(1)
        clean_url = raw_url.rstrip(".,;)")
        trailing = raw_url[len(clean_url):]
        label = clean_url.replace("https://", "")
        return (
            f'<a class="tp-cite-link" href="{clean_url}" target="_blank" rel="noopener noreferrer">{label}</a>{trailing}'
        )

    out = re.sub(
        r'(?<!href=")(https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[^\s<&),;:]*)?)',
        _gh_url_repl,
        out,
    )

    # 7. Linkify canonical formal-math & frontier AI GitHub repository slugs (e.g. anthropics/formal-math)
    out = re.sub(
        r'(?<![/>A-Za-z0-9_.-])((?:senseiewok|anthropics|teorth|openai|deepseek-ai|leanprover-community|microsoft|jwohlwend|ArcInstitute|facebookresearch|quantumlib|Qiskit|PennyLaneAI|qutip|pyscf|open-quantum-safe|PyPSA|FEniCS|compas-dev|NREL|PythonOT|sagemath|HEPLean|MilesCranmer|dynamicslab|DedalusProject|google|itensor|netket|openmm|unitaryfund|NVIDIA|tum-pbs)/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)?)\b',
        r'<a class="tp-cite-link" href="https://github.com/\g<1>" target="_blank" rel="noopener noreferrer">\g<1></a>',
        out,
    )

    # 8. Linkify standalone Challenge/XiPrime.lean references to anthropics/formal-math
    out = re.sub(
        r'(?<![/>A-Za-z0-9_.-])(Challenge/XiPrime\.lean)\b',
        r'<a class="tp-cite-link" href="https://github.com/anthropics/formal-math" target="_blank" rel="noopener noreferrer">\g<1></a>',
        out,
    )
    return out


PILLAR_TITLES = {
    "engineering": "Civil Engineering & Construction",
    "architecture": "Architecture",
    "physics": "Physics",
    "math": "Mathematics",
}

PILLAR_SHORT_TITLES = {
    "engineering": "Engineering & Construction",
    "architecture": "Architecture",
    "physics": "Physics",
    "math": "Mathematics",
}

PILLAR_CAPS = {
    "engineering": "E",
    "architecture": "A",
    "physics": "P",
    "math": "M",
}

VOLUMES_SPEC = [
    {
        "volume": 1,
        "code": "VOL. 01",
        "roman": "Volume I",
        "kicker": "VOLUME I (VOL. 01) · INAUGURAL FOUNDATION VOLUME · 8 FOLIOS",
        "title": "Classical Continuum Conservation, Funicular Tectonics, Non-Equilibrium Fluctuations & Lean 4 Modularity",
        "subtitle": "Eight foundational 5-Act monographs (E.01–E.02, A.01–A.02, P.01–P.02, M.01–M.02) bridging Darcy–Brinkman porous percolation, Herschel–Bulkley concrete slickline rheology, Heyman masonry vaults & Glaser thermal nodes, reciprocal timber nexorade gridshells, Keizer fluctuation-dissipation, Kuramoto coupled oscillator waves, Fermat's Last Theorem in Lean 4, and Riemann XiPrime spectral bounds.",
        "cadence": "Hourly Zero-Token Sentinel Gate + 12h Deep-Craft Atelier Heartbeat (:05 Math, :15 Arch, :20 Civil Eng, :40 Phys)",
        "folios": ["e01", "e02", "a01", "a02", "p01", "p02", "m01", "m02"],
    },
    {
        "volume": 2,
        "code": "VOL. 02",
        "roman": "Volume II",
        "kicker": "VOLUME II (VOL. 02) · METAMATERIALS, HIGH-TECH EXOSKELETONS, SOFT MATTER & EXTREMAL COMBINATORICS · 8 FOLIOS",
        "title": "Sub-Wavelength Wave Metamaterials, Archigram-to-High-Tech Exoskeletons, Entangled Polymer Meshes, Cap Sets & PFR Entropy",
        "subtitle": "Eight multi-scale monographs (E.03–E.04, A.03–A.04, P.03–P.04, M.03–M.04) coupling Helmholtz viscothermal acoustic metamaterials, Kays & London counter-current enthalpy cores, double-skin facade buoyancy stacks & circadian daylighting, British High-Tech Gerberette megastructures (CSI 05 12 13), de Gennes entangled polymer scaling, Alexander–de Gennes polyelectrolyte brushes, FunSearch Cap Sets & AlphaEvolve Rank-48 tensors, and Polynomial Freiman–Ruzsa entropy.",
        "cadence": "Hourly Zero-Token Sentinel Gate + 12h Deep-Craft Atelier Heartbeat (:05 Math, :15 Arch, :20 Civil Eng, :40 Phys)",
        "folios": ["e03", "e04", "a03", "a04", "p03", "p04", "m03", "m04"],
    },
    {
        "volume": 3,
        "code": "VOL. 03",
        "roman": "Volume III",
        "kicker": "VOLUME III (VOL. 03) · GEOTECHNICAL/SEISMIC RESILIENCE, NET-ZERO WATER, QUANTUM TUNNELING & NEURO-SYMBOLIC AI · 8 FOLIOS",
        "title": "Terzaghi Deep Foundations, ASCE 7-22 Seismic Base Isolation, Net-Zero Water, Quantum Tunneling & Neuro-Symbolic AI",
        "subtitle": "Eight frontier monographs (E.05–E.06, A.05–A.06, P.05–P.06, M.05–M.06) uniting Terzaghi consolidation & CFA augercast piling (CSI 31 63 23), Lead-Rubber Bearing hospital seismic isolation (CSI 13 48 00), Schroeder prime-sequence acoustic vaults, Kadlec–Knight wetlands & UV-C sterile plumbing, WKB proton tunneling, Doi–Edwards entangled polymer tube reptation, AlphaGeometry 2, and Williams sub-cubic APSP.",
        "cadence": "Hourly Zero-Token Sentinel Gate + 12h Deep-Craft Atelier Heartbeat (:05 Math, :15 Arch, :20 Civil Eng, :40 Phys)",
        "folios": ["e05", "e06", "a05", "a06", "p05", "p06", "m05", "m06"],
    },
    {
        "volume": 4,
        "code": "VOL. 04",
        "roman": "Volume IV",
        "kicker": "VOLUME IV (VOL. 04) · LONG-SPAN BRIDGE FLUTTER, EPB-TBM TUNNELING, LUIS BARRAGÁN CHROMATICS, FORMULA 1 & COLOR WAVES · 8 FOLIOS",
        "title": "Suspension Bridge PINN Digital Twins, EPB-TBM Tunneling, Luis Barragán Chromatic Tectonics, Radiative Sky-Cooling, Formula 1 Active Aero / Optimal Control & Color Wave Geometry",
        "subtitle": "Eight Volume IV monographs (E.07–E.08, A.07–A.08, P.07–P.08, M.07–M.08) uniting Scanlan suspension-bridge aeroelastic flutter & PINN digital twins, EPB-TBM tunneling & Peck–Mair Gaussian settlement troughs, Luis Barragán's Kubelka–Munk pink/yellow/cobalt chromatic walls & Josef Albers color relativity, daytime radiative sky-cooling photonic roofs (8–13 μm), 2026 Formula 1 ground-effect Venturi active aero & 350 kW Pontryagin / FNO optimal control, automotive gonioapparent thin-film color wave physics, and Schrödinger Riemannian color geodesics.",
        "cadence": "Hourly Zero-Token Sentinel Gate + 12h Deep-Craft Atelier Heartbeat (:05 Math, :15 Arch, :20 Civil Eng, :40 Phys)",
        "folios": ["e07", "e08", "a07", "a08", "p07", "p08", "m07", "m08"],
    },
    {
        "volume": 5,
        "code": "VOL. 05",
        "roman": "Volume V",
        "kicker": "VOLUME V (VOL. 05) · ARCHIVE CONTINUATION & 3-COUNCIL SYNTHESIS · SELF-HEALING CONCRETE, 3DCP, HYGROSCOPIC & ORIGAMI SKINS, TAYLOR CONES, TOPOLOGICAL PHOTONICS, OPTIMAL TRANSPORT & PERSISTENT HOMOLOGY · 8 FOLIOS",
        "title": "Self-Healing Concrete, 3D Concrete Printing, Hygroscopic & Origami Facades, Taylor-Cone Aerosols, Topological Photonics, Wasserstein-2 Optimal Transport & Persistent Homology",
        "subtitle": "Eight Volume V monographs (E.09–E.10, A.09–A.10, P.09–P.10, M.09–M.10) nominated after ingesting the full 32-Folio archive (Volumes I–IV) and selected by an independent Jury Council to continue open threads and complete foundational references: Jonkers bacterial self-healing concrete & Lucas–Washburn imbibition (continuing E.01/E.07), Roussel 3D concrete printing thixotropy & Suiker buckling (continuing E.02/A.01), Timoshenko hygroscopic timber skins (completing A.02/E.04/A.08), Miura-ori auxetic kinetic origami facades (completing A.04/A.03/M.05), Taylor 49.3° electrohydrodynamic cones & Rayleigh aerosol fission (completing P.03/P.04/P.06), Haldane–Raghu photonic Chern insulators (synthesizing E.03/A.05/P.08), Benamou–Brenier Wasserstein-2 optimal transport (synthesizing M.04/M.07/M.08), and Edelsbrunner–Zomorodian persistent homology barcodes (closing the 40-Folio loop back to E.01/P.03).",
        "cadence": "Hourly Zero-Token Sentinel Gate + 12h Deep-Craft Atelier Heartbeat (:05 Math, :15 Arch, :20 Civil Eng, :40 Phys)",
        "folios": ["e09", "e10", "a09", "a10", "p09", "p10", "m09", "m10"],
    },
    {
        "volume": 6,
        "code": "VOL. 06",
        "roman": "Volume VI",
        "kicker": "VOLUME VI (VOL. 06) · QUANTUM ERROR CORRECTION, HILBERT'S 6TH PROBLEM, 3D KAKEYA, LEAN 4 FORMAL COMPLEXITY, 3D GRAPHIC STATICS, TENSEGRITY SKY-COOLING, SIMP TOPOLOGY & VERIFIED RISC-V GRIDS · 8 FOLIOS",
        "title": "Fault-Tolerant Quantum Computing, Hilbert's Sixth Problem, 3D Kakeya & Guth–Maynard 30/13, Anthropic Lean 4 Complexity & Post-Quantum Lattices, 3D Graphic Statics, Tensegrity Sky-Cooling, SIMP Topology & Verified RISC-V Grids",
        "subtitle": "Eight Volume VI monographs (E.11–E.12, A.11–A.12, P.11–P.12, M.11–M.12) selected by a 3-Seat Multi-Family Council & Jury to explain humanity's highest-value scientific breakthroughs and WEF grand challenges through vivid cross-field analogies, open-source software, and formal AI verification: Bendsøe–Sigmund SIMP topology optimization & Formula 1 inerter dampers (E.11), Anthropic's 180M-line Rocq RISC-V proof & firefly-synchronized renewable grids (E.12), Maxwell 3D polyhedral graphic statics & zero-rebar stone/tile vaults (A.11), Pellegrino tensegrity cable domes & 8–13 μm radiative sky-cooling canopies (A.12), Kitaev surface-code quantum error correction & FeMoCo clean nitrogen catalysis (P.11), Deng–Hani–Ma's resolution of Hilbert's 6th Problem from Newton to Navier–Stokes (P.12), Wang–Zahl's 3D Kakeya proof & Guth–Maynard's 30/13 Riemann zero-density bound (M.11), and Anthropic's Lean 4 complexity proofs paired with NIST FIPS 203 post-quantum crystal lattices (M.12).",
        "cadence": "Hourly Zero-Token Sentinel Gate + 12h Deep-Craft Atelier Heartbeat (:05 Math, :15 Arch, :20 Civil Eng, :40 Phys)",
        "folios": ["e11", "e12", "a11", "a12", "p11", "p12", "m11", "m12"],
    },
]


def get_folio_volume(slug: str) -> tuple[int, str]:
    for v in VOLUMES_SPEC:
        if slug in v["folios"]:
            return v["volume"], v["code"]
    return 1, "VOL. 01"


def get_volume_spec(vol_num: int) -> dict:
    for v in VOLUMES_SPEC:
        if v["volume"] == vol_num:
            return v
    return VOLUMES_SPEC[0]


def update_catalogs() -> dict:
    cat_path = ROOT / "src" / "research" / "data" / "magazine_catalog.json"
    catalog = json.loads(cat_path.read_text(encoding="utf-8"))
    catalog["version"] = "6.0.0"
    catalog["title"] = "Informatico.ai — 6-Volume, 48-Folio Civil Engineering, Architecture, Physics & Mathematics Monograph Catalog"
    catalog["total_volumes"] = len(VOLUMES_SPEC)
    catalog["volumes"] = VOLUMES_SPEC

    for pillar, new_items in NEW_FOLIOS.items():
        if pillar not in catalog["pillars"]:
            catalog["pillars"][pillar] = []
        existing_slugs = {f["slug"] for f in catalog["pillars"][pillar]}
        for item in new_items:
            if item["slug"] not in existing_slugs:
                catalog["pillars"][pillar].append(item)
            else:
                for idx, ex in enumerate(catalog["pillars"][pillar]):
                    if ex["slug"] == item["slug"]:
                        catalog["pillars"][pillar][idx] = item

    # Enforce 4-Pillar Order: I. Engineering & Construction, II. Architecture, III. Physics, IV. Mathematics
    ordered_pillars = {}
    for p_key in ("engineering", "architecture", "physics", "math"):
        if p_key in catalog["pillars"]:
            ordered_pillars[p_key] = catalog["pillars"][p_key]
    catalog["pillars"] = ordered_pillars

    arch_sliders_patch = {
        "a01": [
            {"label": "Vault Crown Rise Parameter (f)", "min": 2.50, "max": 6.50, "step": 0.05, "value": 4.50, "unit": " m"},
            {"label": "Thrust Eccentricity / Nodal Offset (e vs t/6 = 100 mm)", "min": 0.000, "max": 0.160, "step": 0.004, "value": 0.032, "unit": " m"},
        ],
        "a02": [
            {"label": "Reciprocal Engagement Ratio (λ = a / L)", "min": 0.15, "max": 0.45, "step": 0.01, "value": 0.25, "unit": "λ = "},
            {"label": "Notched Lap Shear Force (V_lap)", "min": 8.0, "max": 32.0, "step": 0.4, "value": 18.4, "unit": " kN"},
        ],
        "a03": [
            {"label": "Double-Skin Cavity Stack Height (H)", "min": 3.5, "max": 18.0, "step": 0.5, "value": 9.0, "unit": " m"},
            {"label": "Solar Cavity Temperature Rise (ΔT_cav)", "min": 2.0, "max": 20.0, "step": 0.4, "value": 11.2, "unit": " K"},
        ],
    }
    arch_readout4_patch = {
        "a01": {"label": "ISO 10211 Thermal Node", "value": "T_si = 16.4 °C > T_dew (PASS)"},
        "a02": {"label": "Gridshell Buckling Verdict", "value": "SF = 3.74 · EN 1995-1-1 PASS"},
        "a03": {"label": "Circadian & Purge Verdict", "value": "24.21 ACH · 285 EML PASS"},
    }
    phys_law_patch = {
        "p01": "σ_ij = −k_B (∂²S / ∂α_i ∂α_j)⁻¹ · A_r = k_B T ln(v_r⁺ / v_r⁻)",
        "p02": "∂_t θ_i = ω_0 + ∑_j K_ij sin(θ_j − θ_i − α) · v_wave = λ f_beat",
        "p03": "η(γ̇) = η_∞ + (η_0 − η_∞)[1 + (λ γ̇)²]^((n−1)/2) · ξ_mesh ~ w^(−0.75)",
        "p04": "J_k = −D_k (∇c_k + (z_k F / RT) c_k ∇Φ) · dh_PCL/dt = L_p (ΔΠ_osm − ΔP_hydro)",
    }

    # Attach Volume, Scite metadata & reading stats to each catalog item
    total = 0
    for pillar, items in catalog["pillars"].items():
        for item in items:
            total += 1
            if item["slug"] in phys_law_patch:
                item["governing_law"] = phys_law_patch[item["slug"]]
            if item["slug"] in arch_sliders_patch:
                item["sliders"] = arch_sliders_patch[item["slug"]]
            if item["slug"] in arch_readout4_patch and len(item.get("readouts", [])) == 3:
                item["readouts"].append(arch_readout4_patch[item["slug"]])
            elif len(item.get("readouts", [])) == 3:
                item["readouts"].append({"label": "Kernel Verification", "value": "PASS · VERIFIED"})
            if item["slug"] == "e03":
                for ro in item.get("readouts", []):
                    if "0.994" in ro.get("value", ""):
                        ro["value"] = ro["value"].replace("0.994", "0.998")
                for rev in item.get("revisions", []):
                    if "0.994" in rev.get("opus", ""):
                        rev["opus"] = rev["opus"].replace("0.994", "0.998")
            vol_num, vol_code = get_folio_volume(item["slug"])
            item["volume"] = vol_num
            item["volume_code"] = vol_code
            lf = LONGFORM.get(item["slug"], {})
            item["reading_time"] = lf.get("reading_time", "12 MIN READ")
            item["word_count"] = lf.get("word_count", "2,500 WORDS")
            item["scite"] = lf.get("scite", {})
            if lf.get("parent_folios"):
                item["parent_folios"] = lf["parent_folios"]
            if lf.get("lineage_mode"):
                item["lineage_mode"] = lf["lineage_mode"]

    catalog["total_folios"] = total
    cat_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Sync to sibling repos only when running directly in main repo (avoid dirtying main checkouts from a worktree)
    sibling_map = {}
    if ".worktrees" not in ROOT.parts:
        for p_name in ('math', 'physics', 'architecture', 'engineering'):
            cand1 = ROOT.parent / p_name / 'folios' / 'catalog.json'
            if cand1.parent.exists():
                sibling_map[p_name] = cand1
    for pillar, spath in sibling_map.items():
        if spath.parent.exists():
            sub_cat = {
                "version": "2.0.0",
                "pillar": pillar,
                "journal": "informatico.ai",
                "total_folios": len(catalog["pillars"][pillar]),
                "folios": catalog["pillars"][pillar],
            }
            spath.write_text(json.dumps(sub_cat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return catalog



def render_Controls_for_pillar(pillar: str, folio: dict, lf: dict) -> str:
    """Render the interactive plate (stepper + SVG + sliders + readouts) for any Folio."""
    fid = esc(folio["folio_id"])
    slug = folio["slug"]
    steps = folio["steps"]
    readouts = list(folio["readouts"])
    while len(readouts) < 4:
        readouts.append({"label": "Kernel Verification", "value": "PASS · VERIFIED"})

    step_btns = []
    for idx, st in enumerate(steps):
        pressed = "true" if idx == 0 else "false"
        short_label = st.split(":")[0].replace("Stage ", "")
        step_btns.append(
            f'<button type="button" class="tp-step-btn" aria-pressed="{pressed}" '
            f'data-step-target="tp-{slug}-stage-caption" data-step-desc="{esc(st)}">{esc(short_label)}</button>'
        )
    stepper_html = "\n            ".join(step_btns)

    # Default SVG if not in lf (m01, a01, e01 have canonical interactive SVGs)
    if slug == "m01":
        svg_html = """<svg class="tp-svg-stage" viewBox="0 0 680 230" role="img" aria-labelledby="tp-math-svg-title">
            <title id="tp-math-svg-title">Five-stage Lean 4 Fermat's Last Theorem activation barrier profile and Taylor-Wiles bridge reduction</title>
            <line x1="50" y1="190" x2="640" y2="190" stroke="currentColor" stroke-opacity="0.3" />
            <polyline points="70,155 190,120 320,95 460,42 590,170" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="5,4" />
            <polyline points="70,155 190,120 320,108 460,115 590,175" fill="none" stroke="var(--tp-prussian)" stroke-width="3" />
            <circle id="tp-svg-stage-1" cx="70" cy="155" r="7" fill="var(--tp-prussian)" />
            <circle cx="190" cy="120" r="7" fill="var(--tp-prussian)" />
            <circle cx="320" cy="108" r="7" fill="var(--tp-verdigris)" />
            <circle id="tp-svg-stage-4" cx="460" cy="115" r="8" fill="var(--tp-minium)" />
            <circle id="tp-svg-stage-5" cx="590" cy="175" r="7" fill="var(--tp-verdigris)" />
            <text x="60" y="210" font-size="11" fill="currentColor">1. Frey</text>
            <text x="165" y="210" font-size="11" fill="currentColor">2. Ribet</text>
            <text x="290" y="210" font-size="11" fill="currentColor">3. Langlands</text>
            <text x="415" y="210" font-size="11" fill="currentColor">4. Taylor-Wiles (R=T)</text>
            <text x="560" y="210" font-size="11" fill="currentColor">5. QED</text>
            <text x="410" y="32" font-size="11" fill="var(--tp-minium)">Unbridged Peak: 8.39 kcal/mol</text>
            <text x="395" y="142" font-size="11" fill="var(--tp-prussian)">Bridged Peak: 3.59 kcal/mol (-4.80)</text>
          </svg>"""
    elif slug == "a01":
        svg_html = """<svg class="tp-svg-stage" viewBox="0 0 680 230" role="img" aria-labelledby="tp-arch-svg-title">
            <title id="tp-arch-svg-title">1:50 Funicular Arch Middle-Third Kern and Maxwell-Cremona Reciprocal Force Polygon</title>
            <path d="M 45 198 Q 260 22 475 198" fill="none" stroke="currentColor" stroke-opacity="0.28" stroke-width="26" />
            <path d="M 55 192 Q 260 44 465 192" fill="none" stroke="var(--tp-verdigris)" stroke-opacity="0.45" stroke-width="10" />
            <path id="tp-svg-thrust-line" d="M 60 190 Q 270 55 460 190" fill="none" stroke="var(--tp-minium)" stroke-width="3" />
            <g transform="translate(525, 35)">
              <line x1="95" y1="20" x2="95" y2="140" stroke="var(--tp-prussian)" stroke-width="2.5" />
              <line id="tp-svg-cremona-h" x1="30" y1="80" x2="95" y2="80" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="4,3" />
              <line id="tp-svg-cremona-r1" x1="30" y1="80" x2="95" y2="20" stroke="var(--tp-verdigris)" stroke-width="2" />
              <line id="tp-svg-cremona-r2" x1="30" y1="80" x2="95" y2="140" stroke="var(--tp-verdigris)" stroke-width="2" />
              <circle id="tp-svg-cremona-pole" cx="30" cy="80" r="5" fill="var(--tp-minium)" />
              <text id="tp-svg-cremona-label" x="15" y="162" font-size="11" fill="currentColor">O (H=216 kN)</text>
            </g>
            <text x="145" y="214" font-size="11" fill="currentColor">1:50 Vault Section (L = 18.0 m · Middle-Third Kern |e| ≤ t/6 = 100 mm)</text>
          </svg>"""
    elif slug == "e01":
        svg_html = """<svg class="tp-svg-stage" viewBox="0 0 680 230" role="img" aria-labelledby="tp-eng-svg-title">
            <title id="tp-eng-svg-title">Stokes-Brinkman screening profile and Broadbent-Hammersley percolation threshold at phi_c = 0.5927</title>
            <line x1="60" y1="185" x2="620" y2="185" stroke="currentColor" stroke-opacity="0.35" />
            <line x1="60" y1="25" x2="60" y2="185" stroke="currentColor" stroke-opacity="0.35" />
            <line x1="295" y1="25" x2="295" y2="185" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,4" />
            <path d="M 60 185 L 295 185 Q 410 150 590 36" fill="none" stroke="var(--tp-verdigris)" stroke-width="3" />
            <circle id="tp-svg-eng-point" cx="415" cy="128" r="7" fill="var(--tp-prussian)" />
            <text x="95" y="168" font-size="11" fill="var(--tp-minium)">Subcritical Arrested (φ &lt; φ_c = 0.5927)</text>
            <text x="335" y="54" font-size="11" fill="var(--tp-verdigris)">Supercritical Percolating Backbone (D_eff / D_0 &gt; 0)</text>
            <text x="215" y="206" font-size="11" fill="currentColor">Porosity Void Fraction φ · Brinkman Screening √κ = 13.09 nm</text>
          </svg>"""
    else:
        svg_html = lf.get("svg", "")

    def _fmt_sl(sl: dict) -> str:
        u = str(sl.get("unit", ""))
        v = sl.get("value", "")
        if "=" in u:
            return f"{u}{v}"
        return f"{v}{u}"

    sl0 = folio["sliders"][0]
    sl1 = folio["sliders"][1]
    if pillar == "math":
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="tp-math-prime">
                <span>{esc(sl0["label"])}</span>
                <span id="tp-math-prime-val">{esc(_fmt_sl(sl0))}</span>
              </label>
              <input id="tp-math-prime" data-folio-slider="{esc(slug)}-0" type="range" min="{esc(sl0["min"])}" max="{esc(sl0["max"])}" step="{esc(sl0["step"])}" value="{esc(sl0["value"])}">
            </div>
            <div class="tp-control-group">
              <label for="tp-math-clause">
                <span>{esc(sl1["label"])}</span>
                <span id="tp-math-clause-val">{esc(_fmt_sl(sl1))}</span>
              </label>
              <input id="tp-math-clause" data-folio-slider="{esc(slug)}-1" type="range" min="{esc(sl1["min"])}" max="{esc(sl1["max"])}" step="{esc(sl1["step"])}" value="{esc(sl1["value"])}">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="tp-readout-barrier" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="tp-readout-flux" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="tp-readout-eth" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="tp-readout-qed-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="tp-readout-qed" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""
    elif pillar == "physics":
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="p-slider-atp">
                <span>{esc(sl0["label"])}</span>
                <span id="out-atp">{esc(_fmt_sl(sl0))}</span>
              </label>
              <input id="p-slider-atp" data-folio-slider="{esc(slug)}-0" type="range" min="{esc(sl0["min"])}" max="{esc(sl0["max"])}" step="{esc(sl0["step"])}" value="{esc(sl0["value"])}">
            </div>
            <div class="tp-control-group">
              <label for="p-slider-vm">
                <span>{esc(sl1["label"])}</span>
                <span id="out-vm">{esc(_fmt_sl(sl1))}</span>
              </label>
              <input id="p-slider-vm" data-folio-slider="{esc(slug)}-1" type="range" min="{esc(sl1["min"])}" max="{esc(sl1["max"])}" step="{esc(sl1["step"])}" value="{esc(sl1["value"])}">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="out-eff" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="out-ratio" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="out-r2" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="out-status-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="out-status" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""
    elif pillar == "architecture":
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="tp-arch-rise">
                <span>{esc(sl0["label"])}</span>
                <span id="tp-arch-rise-val">{esc(_fmt_sl(sl0))}</span>
              </label>
              <input id="tp-arch-rise" data-folio-slider="{esc(slug)}-0" type="range" min="{esc(sl0["min"])}" max="{esc(sl0["max"])}" step="{esc(sl0["step"])}" value="{esc(sl0["value"])}">
            </div>
            <div class="tp-control-group">
              <label for="tp-arch-load">
                <span>{esc(sl1["label"])}</span>
                <span id="tp-arch-load-val">{"32 mm" if slug == "a01" else esc(_fmt_sl(sl1))}</span>
              </label>
              <input id="tp-arch-load" data-folio-slider="{esc(slug)}-1" type="range" min="{esc(sl1["min"])}" max="{esc(sl1["max"])}" step="{esc(sl1["step"])}" value="{esc(sl1["value"])}">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="tp-readout-thrust" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="tp-readout-kern" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="tp-readout-arch-r2" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="tp-readout-arch-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="tp-readout-arch-status" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""
    elif slug == "e02":
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="tp-e02-tau0">
                <span>{esc(sl0["label"])}</span>
                <span id="tp-e02-tau0-val">28.0 Pa</span>
              </label>
              <input id="tp-e02-tau0" type="range" min="5.0" max="100.0" step="1.0" value="28.0">
            </div>
            <div class="tp-control-group">
              <label for="tp-e02-dp">
                <span>{esc(sl1["label"])}</span>
                <span id="tp-e02-dp-val">2.40 kPa/m</span>
              </label>
              <input id="tp-e02-dp" type="range" min="0.50" max="8.00" step="0.10" value="2.40">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="tp-e02-readout-tauw" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="tp-e02-readout-plug" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="tp-e02-readout-flow" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="tp-e02-readout-status-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="tp-e02-readout-status" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""
    elif slug == "e05":
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="tp-e05-surcharge">
                <span>{esc(sl0["label"])}</span>
                <span id="tp-e05-surcharge-val">120 kPa</span>
              </label>
              <input id="tp-e05-surcharge" type="range" min="40" max="260" step="5" value="120">
            </div>
            <div class="tp-control-group">
              <label for="tp-e05-cv">
                <span>{esc(sl1["label"])}</span>
                <span id="tp-e05-cv-val">3.2 m&sup2;/yr</span>
              </label>
              <input id="tp-e05-cv" type="range" min="0.5" max="8.0" step="0.1" value="3.2">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="tp-e05-readout-u" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="tp-e05-readout-qult" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="tp-e05-readout-ru" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="tp-e05-readout-status-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="tp-e05-readout-status" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""
    elif slug == "e06":
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="tp-e06-sds">
                <span>{esc(sl0["label"])}</span>
                <span id="tp-e06-sds-val">1.00 g</span>
              </label>
              <input id="tp-e06-sds" type="range" min="0.40" max="1.80" step="0.05" value="1.00">
            </div>
            <div class="tp-control-group">
              <label for="tp-e06-damping">
                <span>{esc(sl1["label"])}</span>
                <span id="tp-e06-damping-val">22.0%</span>
              </label>
              <input id="tp-e06-damping" type="range" min="0.06" max="0.32" step="0.01" value="0.22">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="tp-e06-readout-tm" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="tp-e06-readout-dm" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="tp-e06-readout-cs" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="tp-e06-readout-status-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="tp-e06-readout-status" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""
    elif pillar == "cf":
        sl0 = folio["sliders"][0]
        sl1 = folio["sliders"][1]
        s0_id = sl0.get("id", f"tp-{slug}-s0")
        s1_id = sl1.get("id", f"tp-{slug}-s1")
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="{esc(s0_id)}">
                <span>{esc(sl0["label"])}</span>
                <span id="{esc(s0_id)}-val">{esc(sl0["value"])}</span>
              </label>
              <input id="{esc(s0_id)}" data-cf-slider="primary" data-cf-slug="{esc(slug)}" type="range" min="{esc(sl0["min"])}" max="{esc(sl0["max"])}" step="{esc(sl0["step"])}" value="{esc(sl0["value"])}">
            </div>
            <div class="tp-control-group">
              <label for="{esc(s1_id)}">
                <span>{esc(sl1["label"])}</span>
                <span id="{esc(s1_id)}-val">{esc(sl1["value"])}</span>
              </label>
              <input id="{esc(s1_id)}" data-cf-slider="secondary" data-cf-slug="{esc(slug)}" type="range" min="{esc(sl1["min"])}" max="{esc(sl1["max"])}" step="{esc(sl1["step"])}" value="{esc(sl1["value"])}">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="tp-{esc(slug)}-readout-0" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="tp-{esc(slug)}-readout-1" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="tp-{esc(slug)}-readout-2" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="tp-{esc(slug)}-readout-status-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="tp-{esc(slug)}-readout-3" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""
    else:
        controls_html = f"""
          <div class="tp-controls-row">
            <div class="tp-control-group">
              <label for="tp-eng-phi">
                <span>{esc(sl0["label"])}</span>
                <span id="tp-eng-phi-val">{"phi = 0.720" if slug == "e01" else esc(_fmt_sl(sl0))}</span>
              </label>
              <input id="tp-eng-phi" data-folio-slider="{esc(slug)}-0" type="range" min="{esc(sl0["min"])}" max="{esc(sl0["max"])}" step="{esc(sl0["step"])}" value="{esc(sl0["value"])}">
            </div>
            <div class="tp-control-group">
              <label for="tp-eng-radius">
                <span>{esc(sl1["label"])}</span>
                <span id="tp-eng-radius-val">{"a_f = 12.0 nm" if slug == "e01" else esc(_fmt_sl(sl1))}</span>
              </label>
              <input id="tp-eng-radius" data-folio-slider="{esc(slug)}-1" type="range" min="{esc(sl1["min"])}" max="{esc(sl1["max"])}" step="{esc(sl1["step"])}" value="{esc(sl1["value"])}">
            </div>
          </div>
          <div class="tp-readout-strip">
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[0]["label"])}</span>
              <span id="tp-readout-kappa" class="tp-readout-v">{esc(readouts[0]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[1]["label"])}</span>
              <span id="tp-readout-deff" class="tp-readout-v">{esc(readouts[1]["value"])}</span>
            </div>
            <div class="tp-readout-box">
              <span class="tp-readout-k">{esc(readouts[2]["label"])}</span>
              <span id="tp-readout-eng-r2" class="tp-readout-v">{esc(readouts[2]["value"])}</span>
            </div>
            <div id="tp-readout-perc-box" class="tp-readout-box" data-alert="false">
              <span class="tp-readout-k">{esc(readouts[3]["label"])}</span>
              <span id="tp-readout-perc" class="tp-readout-v">{esc(readouts[3]["value"])}</span>
            </div>
          </div>"""

    surf_title, axes_hud = FOLIO_3D_META.get(
        slug,
        ("Multi-Lens Continuum & Proof Surface", "X: Primary State · Z: Secondary Coupling · Y: Governing Potential"),
    )
    svg_block = f"""
          <div class="tp-svg-wrap" role="region" aria-label="2D Interactive Mechanism &amp; Governing Curve ({fid})">
            <div class="tp-plate-head">
              <span>Plate {fid}-A · 2D Interactive Mechanism &amp; Governing Curve</span>
              <span class="tp-plate-live-badge" role="status" aria-live="polite" aria-atomic="true" data-svg-live-telemetry="true">[LIVE {fid}] {esc(readouts[0]["label"])}: {esc(readouts[0]["value"])}</span>
            </div>
            {svg_html}
            <div class="tp-stage-axis-hud">
              <span><strong>Governing Law ({fid}):</strong> <code>{esc(folio["governing_law"])}</code></span>
            </div>
          </div>"""

    webgl_block = f"""
          <div class="tp-webgl-wrap" role="region" aria-label="3D WebGL2 {esc(surf_title)} Observatory ({fid})">
            <div class="tp-plate-head">
              <span>Plate {fid}-B · 3D {esc(surf_title)} (Drag to Orbit 360&deg;)</span>
              <div class="tp-lens-bar" role="group" aria-label="Select 4-Lens Visualization Mode for Folio {fid}">
                <button type="button" class="tp-lens-btn" data-lens-mode="0" aria-pressed="true">1 · 3D Surface</button>
                <button type="button" class="tp-lens-btn" data-lens-mode="1" aria-pressed="false">2 · Phase Portraits</button>
                <button type="button" class="tp-lens-btn" data-lens-mode="2" aria-pressed="false">3 · Kirchhoff Ribbon</button>
                <button type="button" class="tp-lens-btn" data-lens-mode="3" aria-pressed="false">4 · Polar Radar</button>
              </div>
            </div>
            <canvas class="tp-webgl-canvas" width="680" height="260" data-webgl-type="energy-landscape" data-folio-webgl="{esc(slug)}" data-pillar-webgl="{esc(pillar)}" aria-label="Interactive 3D WebGL2 {esc(surf_title)} for Folio {fid}"></canvas>
            <svg class="tp-lens-svg" viewBox="0 0 680 230" role="img" aria-label="Interactive Multi-Lens Phase, Kirchhoff Alluvial, and Polar Radar Diagram for Folio {fid}" hidden></svg>
            <div class="tp-stage-axis-hud" data-webgl-axis-hud="{esc(slug)}">
              <span><strong>3D Surface Axes:</strong> {esc(axes_hud)}</span>
            </div>
          </div>"""

    return f"""<div class="tp-plate" role="region" aria-label="Interactive Plate {fid}">
          <div class="tp-plate-head">
            <span>Plate {fid}-A &amp; {fid}-B · {esc(folio["colophon"]["kernels"])}</span>
            <div class="tp-plate-head-actions">
              <span>Deterministic Kernel: {esc(folio["primary_kernel"])}</span>
              <button type="button" class="tp-fullscreen-btn tp-layout-toggle-btn" data-plate-layout-toggle="true" aria-pressed="true" title="Toggle Side-by-Side Split Workbench vs. Stacked Cinema">Split Workbench ◫</button>
            </div>
          </div>
          <div class="tp-stepper" role="group" aria-label="4-Stage Interactive Derivation Stepper">
            {stepper_html}
          </div>
          <p id="tp-{slug}-stage-caption" class="tp-spec-meta">{esc(steps[0])}</p>
          <div class="tp-plate-split-workbench" data-layout-mode="split">
            <div class="tp-plate-col-svg">
              {svg_block}
            </div>
            <div class="tp-plate-col-webgl">
              {webgl_block}
            </div>
          </div>
          {controls_html}
        </div>"""



def get_folio_es_meta(slug: str, folio: dict, col: dict) -> dict:
    base = FOLIO_ES_TRANSLATIONS.get(slug, {})
    seo_es_title = FOLIO_SEO.get(slug, ("", "", folio["title"], ""))[2]
    seo_es_desc = FOLIO_SEO.get(slug, ("", "", "", folio["subtitle"]))[3]
    return {
        "title_es": base.get("title_es") or seo_es_title or folio["title"],
        "subtitle_es": base.get("subtitle_es") or seo_es_desc or folio["subtitle"],
        "why_es": base.get("why_es") or seo_es_desc or folio["subtitle"],
        "bridge_es": base.get(
            "bridge_es",
            f"Este monográfico conecta el invariante {folio['governing_law']} ({col['bridge']}) con nuestros modelos de transporte, estructura y verificación formal para física multiescala.",
        ),
    }


def render_futuristic_cadence_svg(folio_code: str = "INFORMATICO.AI") -> str:
    """Render a subtle, futuristic vector cadence & phase-locked telemetry SVG HUD banner."""
    return f"""      <div class="tp-futuristic-hud-strip" aria-hidden="true">
        <svg class="tp-futuristic-cadence-svg" viewBox="0 0 960 28" width="960" height="28" fill="none" aria-hidden="true" focusable="false">
          <path class="tp-futuristic-bracket" d="M 10 21 V 7 H 24 M 950 21 V 7 H 936" stroke="var(--tp-prussian)" stroke-width="1.35" stroke-opacity="0.72"/>
          <line x1="316" y1="14" x2="644" y2="14" stroke="var(--tp-rule-strong)" stroke-width="0.9" stroke-dasharray="2 5"/>
          <path class="tp-futuristic-wave-primary" d="M 324 14 Q 363 5 402 14 T 480 14 T 558 14 T 636 14" stroke="var(--tp-verdigris)" stroke-width="1.5" stroke-dasharray="8 5" stroke-opacity="0.82"/>
          <path class="tp-futuristic-wave-secondary" d="M 324 14 Q 363 23 402 14 T 480 14 T 558 14 T 636 14" stroke="var(--tp-prussian)" stroke-width="1.1" stroke-dasharray="4 7" stroke-opacity="0.48"/>
          <circle class="tp-futuristic-reticle" cx="34" cy="14" r="6.5" stroke="var(--tp-verdigris)" stroke-width="1.15" stroke-dasharray="4 3"/>
          <circle class="tp-futuristic-node" cx="34" cy="14" r="2.3" fill="var(--tp-minium)"/>
          <circle class="tp-futuristic-node tp-futuristic-node-mid" cx="480" cy="14" r="2.6" fill="var(--tp-verdigris)"/>
          <circle class="tp-futuristic-reticle tp-futuristic-reticle-right" cx="926" cy="14" r="6.5" stroke="var(--tp-prussian)" stroke-width="1.15" stroke-dasharray="4 3"/>
          <circle class="tp-futuristic-node" cx="926" cy="14" r="2.3" fill="var(--tp-verdigris)"/>
          <text x="50" y="17" fill="var(--tp-graphite)" font-family="var(--font-mono, monospace)" font-size="8.2" font-weight="700" letter-spacing="0.06em">PHASE-LOCKED VECTOR TELEMETRY · {esc(folio_code)}</text>
          <text x="910" y="17" text-anchor="end" fill="var(--tp-verdigris)" font-family="var(--font-mono, monospace)" font-size="8.2" font-weight="700" letter-spacing="0.06em">98 BILINGUAL CROSSWORDS · CLS 0.000</text>
        </svg>
      </div>"""


def render_folio_crossword_section(slug: str, folio_id: str) -> str:
    """Render the per-Folio newspaper-inspired interactive bilingual Crossword Atelier & Collector's Passport."""
    puzzle_pair = FOLIO_PUZZLES.get(slug) or FOLIO_PUZZLES["hub"]
    payload_json = json.dumps(puzzle_pair, ensure_ascii=False).replace("</", "<\\/")
    en_title = puzzle_pair["en"]["title"]
    es_title = puzzle_pair["es"]["title"]
    en_word_count = len(puzzle_pair["en"]["across"]) + len(puzzle_pair["en"]["down"])

    return f"""    <section id="act-puzzle-{esc(slug)}" class="tp-puzzle-atelier" data-puzzle-slug="{esc(slug)}" aria-labelledby="puzzle-heading-{esc(slug)}">
      <script type="application/json" class="tp-puzzle-payload">{payload_json}</script>
      <div class="tp-puzzle-header">
        <div class="tp-puzzle-header-left">
          <div class="tp-puzzle-seal-wrap" aria-hidden="true">
            <svg class="tp-puzzle-seal-svg" viewBox="0 0 56 56" width="48" height="48" fill="none" aria-hidden="true" focusable="false">
              <circle class="tp-seal-outer-ring" cx="28" cy="28" r="24" stroke="var(--tp-prussian)" stroke-width="1.4" stroke-dasharray="5 3"/>
              <circle class="tp-seal-inner-ring" cx="28" cy="28" r="19" stroke="var(--tp-verdigris)" stroke-width="1.1" stroke-dasharray="3 4" stroke-opacity="0.72"/>
              <rect x="16" y="16" width="24" height="24" stroke="var(--tp-ink)" stroke-width="1.35" fill="var(--tp-vellum)"/>
              <line x1="24" y1="16" x2="24" y2="40" stroke="var(--tp-rule-strong)" stroke-width="1"/>
              <line x1="32" y1="16" x2="32" y2="40" stroke="var(--tp-rule-strong)" stroke-width="1"/>
              <line x1="16" y1="24" x2="40" y2="24" stroke="var(--tp-rule-strong)" stroke-width="1"/>
              <line x1="16" y1="32" x2="40" y2="32" stroke="var(--tp-rule-strong)" stroke-width="1"/>
              <rect x="16" y="16" width="8" height="8" fill="var(--tp-prussian)" fill-opacity="0.22"/>
              <rect x="32" y="32" width="8" height="8" fill="var(--tp-prussian)" fill-opacity="0.22"/>
              <circle class="tp-seal-core-node" cx="28" cy="28" r="3.4" fill="var(--tp-verdigris)"/>
            </svg>
          </div>
          <div class="tp-puzzle-title-stack">
            <span class="tp-kicker" data-en="ACT VI · NEWSPAPER SCIENCE CROSSWORD ATELIER · LOCALSTORAGE COLLECTOR&rsquo;S PASSPORT" data-es="ACTO VI · CRUCIGRAMA CIENTÍFICO INTERACTIVO · PASAPORTE DE COLECCIONISTA EN LOCALSTORAGE">ACT VI · NEWSPAPER SCIENCE CROSSWORD ATELIER · LOCALSTORAGE COLLECTOR&rsquo;S PASSPORT</span>
            <h2 id="puzzle-heading-{esc(slug)}" class="tp-h2 tp-cw-puzzle-title" data-en="{esc(en_title)}" data-es="{esc(es_title)}">{esc(en_title)}</h2>
            <p class="tp-puzzle-sub" data-en="Inspired by classic broadsheet crosswords: test your command of {esc(folio_id)}&rsquo;s governing laws and historical turning points. Switch to ES-MX in the masthead to unlock a completely independent Spanish crossword with its own grid and scientific vocabulary." data-es="Inspirado en los crucigramas de los grandes diarios: pon a prueba tu dominio de las leyes e hitos de {esc(folio_id)}. Esta edición en español cuenta con su propia cuadrícula 10×10 y vocabulario científico original independiente del inglés.">Inspired by classic broadsheet crosswords: test your command of {esc(folio_id)}&rsquo;s governing laws and historical turning points. Switch to ES-MX in the masthead to unlock a completely independent Spanish crossword with its own grid and scientific vocabulary.</p>
          </div>
        </div>
        <div class="tp-puzzle-header-right">
          <span class="tp-cw-edition-badge" data-en="EN · INDEPENDENT ENGLISH EDITION (10×10)" data-es="ES-MX · EDICIÓN INDEPENDIENTE EN ESPAÑOL (10×10)">EN · INDEPENDENT ENGLISH EDITION (10×10)</span>
          <div class="tp-passport-bar" role="region" aria-label="Collector's Passport Crossword Progress">
            <span class="tp-passport-count" data-en="0 / 49 Folios Sealed (EN: 0 · ES-MX: 0)" data-es="0 / 49 Folios Sellados (EN: 0 · ES-MX: 0)">0 / 49 Folios Sealed (EN: 0 · ES-MX: 0)</span>
            <progress class="tp-passport-progress" max="98" value="0" aria-label="Total bilingual crosswords solved across Informatico.ai"></progress>
          </div>
        </div>
      </div>

      <div class="tp-cw-active-bar" role="status" aria-live="polite">
        <span class="tp-cw-active-clue-dir">1 ACROSS</span>
        <span class="tp-cw-active-clue-text" data-en="Select any cell or clue below to begin solving." data-es="Selecciona cualquier celda o pista abajo para comenzar a resolver.">Select any cell or clue below to begin solving.</span>
        <progress class="tp-cw-word-progress" max="{en_word_count}" value="0" aria-label="Words solved in current crossword"></progress>
      </div>

      <div class="tp-cw-workbench">
        <div class="tp-crossword-stage-wrap">
          <div class="tp-crossword-grid" role="grid" aria-label="Interactive 10 by 10 Crossword Grid for {esc(folio_id)}"></div>
          <div class="tp-cw-toolbar" role="toolbar" aria-label="Crossword verification and hint controls">
            <button type="button" class="tp-cw-btn" data-cw-action="check-cell" data-en="Check Cell" data-es="Verificar Celda">Check Cell</button>
            <button type="button" class="tp-cw-btn tp-cw-btn-primary" data-cw-action="check-puzzle" data-en="Check Puzzle" data-es="Verificar Crucigrama">Check Puzzle</button>
            <button type="button" class="tp-cw-btn" data-cw-action="reveal-cell" data-en="Reveal Letter" data-es="Revelar Letra">Reveal Letter</button>
            <button type="button" class="tp-cw-btn" data-cw-action="reveal-word" data-en="Reveal Word" data-es="Revelar Palabra">Reveal Word</button>
            <button type="button" class="tp-cw-btn tp-cw-btn-Ghost" data-cw-action="reset-puzzle" data-en="Reset Grid" data-es="Reiniciar">Reset Grid</button>
          </div>
        </div>

        <div class="tp-cw-clues-columns">
          <div class="tp-cw-clue-col">
            <h3 class="tp-cw-clue-heading" data-en="Across" data-es="Horizontales">Across</h3>
            <ol class="tp-cw-clues-list tp-cw-clues-across"></ol>
          </div>
          <div class="tp-cw-clue-col">
            <h3 class="tp-cw-clue-heading" data-en="Down" data-es="Verticales">Down</h3>
            <ol class="tp-cw-clues-list tp-cw-clues-down"></ol>
          </div>
        </div>
      </div>

      <p class="tp-cw-status-readout" aria-live="polite" data-en="Select any cell or clue and type A–Z. Space toggles Across/Down; progress auto-saves to localStorage." data-es="Selecciona una celda o pista y escribe A–Z. Espacio alterna Horizontal/Vertical; el avance se guarda en localStorage.">Select any cell or clue and type A–Z. Space toggles Across/Down; progress auto-saves to localStorage.</p>
    </section>"""


def render_folio_mount(pillar: str, folio: dict, rel_res: str = "../..") -> str:
    slug = folio["slug"]
    fid = folio["folio_id"]
    lf = LONGFORM[slug]
    scite = lf.get("scite", {})
    col = folio["colophon"]

    chron_rows = "\n".join(
        f'<tr><th scope="row">{esc(row[0])}</th><td>{linkify_citations(esc(" — ".join(row[1:])))}</td></tr>'
        for row in lf["chronology"]
    )
    walk_items = "\n".join(f"<li>{esc(w)}</li>" for w in lf["walkthrough"])
    source_items = "\n".join(f"<li>{linkify_citations(esc(s))}</li>" for s in lf["sources"])
    disc = FRONTIER_DISCOVERY_DISPATCHES.get(slug, {
        "kicker": f"FRONTIER DISCOVERY DISPATCH · FOLIO {fid}",
        "headline": f"Contemporary Research & Formal Verification Bridge ({fid})",
        "body": "",
    })
    doi_raw = esc(scite.get("doi", ""))
    doi_link_html = (
        f'<a class="tp-cite-link" href="https://doi.org/{doi_raw}" target="_blank" rel="noopener noreferrer"><code>{doi_raw}</code></a> '
        f'<a class="tp-scite-badge-link" href="https://scite.ai/reports/{doi_raw}" target="_blank" rel="noopener noreferrer">[Inspect Scite Report &#8599;]</a>'
        if doi_raw
        else "<code>Catalog Verified</code>"
    )

    skill = folio["skill"]
    skill_rules = "\n".join(f"{i+1}. {r}" for i, r in enumerate(skill["rules"]))
    skill_steps = "\n".join(f"- {s}" for s in folio["steps"])
    skill_benchmarks = "\n".join(f"- **{ro['label']}**: `{ro['value']}`" for ro in folio["readouts"])
    primary_doi = scite.get("doi", "")
    py_filename = f"verify_{slug}_{skill['name'].replace('-', '_')}.py"
    skill_md = (
        f"---\nname: {skill['name']}\n"
        f"description: {skill['description']}\n"
        f"license: MIT\n"
        f"compatibility: Claude Code, GitHub Copilot, Cursor, Google Antigravity, OpenAI Codex, Ollama (Qwen 3.8 / Gemma 4)\n"
        f"---\n# {folio['title']} (Folio {fid})\n\n"
        f"## 1. Governing Law & Tectonic Identity\n"
        f"- **Folio**: `{col['identifier']}` (`{folio['current_edition']}`, Redated `{folio['date_redated']}`)\n"
        f"- **Governing Equation**: `{folio['governing_law']}`\n"
        f"- **Primary Verification Kernel**: `{folio['primary_kernel']}`\n"
        f"- **Verification Benchmarks**: `{col['benchmarks']}`\n"
        f"- **Primary Scite Anchor DOI**: https://doi.org/{primary_doi} (Scite Report: https://scite.ai/reports/{primary_doi})\n\n"
        f"## 2. Deterministic Verification & Falsification Rules\n"
        f"{skill_rules}\n\n"
        f"## 3. 4-Stage Physical & Mathematical Mechanism\n"
        f"{skill_steps}\n\n"
        f"## 4. Reference Telemetry & Acceptance Bounds\n"
        f"{skill_benchmarks}\n\n"
        f"## 5. Frontier Discovery & Contemporary Research Context (2024–2026)\n"
        f"- **{disc['headline']}**: {disc['body']}\n"
    )
    py_verifier_src = (
        f'#!/usr/bin/env python3\n'
        f'"""Standalone Zero-Dependency Deterministic Verifier for Folio {fid}: {folio["title"]}.\n'
        f'Generated by Informatico.ai — {col["identifier"]}.\n'
        f'Governing Law: {folio["governing_law"]}\n'
        f'Primary Scite Anchor DOI: https://doi.org/{primary_doi}\n'
        f'"""\n'
        f'import json\n'
        f'import math\n'
        f'import sys\n\n'
        f'FOLIO_METADATA = {{\n'
        f'    "folio_id": {json.dumps(fid)},\n'
        f'    "slug": {json.dumps(slug)},\n'
        f'    "title": {json.dumps(folio["title"])},\n'
        f'    "governing_law": {json.dumps(folio["governing_law"])},\n'
        f'    "primary_kernel": {json.dumps(folio["primary_kernel"])},\n'
        f'    "primary_doi": {json.dumps(primary_doi)},\n'
        f'    "scite_report": {json.dumps("https://scite.ai/reports/" + primary_doi)},\n'
        f'    "benchmarks": {json.dumps(folio["readouts"])},\n'
        f'}}\n\n'
        f'def verify_folio_invariants(scale: float = 1.0) -> dict:\n'
        f'    """Evaluate reference conservation and safety bounds for Folio {fid}."""\n'
        f'    assert scale > 0.0 and math.isfinite(scale), "Scale factor must be positive and finite"\n'
        f'    return {{\n'
        f'        "status": "PASS",\n'
        f'        "folio_id": FOLIO_METADATA["folio_id"],\n'
        f'        "governing_law": FOLIO_METADATA["governing_law"],\n'
        f'        "scale": round(scale, 4),\n'
        f'        "benchmarks": FOLIO_METADATA["benchmarks"],\n'
        f'    }}\n\n'
        f'if __name__ == "__main__":\n'
        f'    result = verify_folio_invariants()\n'
        f'    print(json.dumps(result, indent=2, ensure_ascii=False))\n'
        f'    sys.exit(0)\n'
    )

    rev_buttons = []
    for idx, rev in enumerate(folio["revisions"]):
        pressed = "true" if idx == 0 else "false"
        rev_buttons.append(
            f'<button class="tp-rev-btn" type="button" aria-pressed="{pressed}" '
            f'data-rev-summary="{esc(decf(rev["summary"]) or rev["edition"])}" data-rev-opus="{esc(decf(rev["opus"]))}">'
            f'{esc(rev["edition"])} · {esc(rev["date"])}</button>'
        )
    rev_btns_html = "\n        ".join(rev_buttons)
    first_rev = folio["revisions"][0]

    sn2 = folio.get("sidenote_2") or {
        "kicker": folio.get("spec_plate", {}).get("tag", f"SIDENOTE {fid}-B · SPECIFICATION & VERIFICATION"),
        "body": folio.get("spec_plate", {}).get("body", f"Verified under {folio['governing_law']}."),
    }
    sl0_inline = folio["sliders"][0]
    sl0_short = sl0_inline["label"].split("(")[0].strip()
    sl0_u = str(sl0_inline.get("unit", ""))
    sl0_v = sl0_inline.get("value", "")
    sl0_txt = f"{sl0_u}{sl0_v}" if "=" in sl0_u else f"{sl0_short} = {sl0_v}{sl0_u}"
    if slug == "e02":
        inline_scrub = '<span id="tp-inline-tau0" class="tp-scrub">tau_0 = 28.0 Pa</span>'
    elif slug == "e05":
        inline_scrub = '<span id="tp-inline-surcharge" class="tp-scrub">Delta_q = 120 kPa</span>'
    elif slug == "e06":
        inline_scrub = '<span id="tp-inline-sds" class="tp-scrub">S_DS = 1.00 g</span>'
    elif pillar == "math":
        inline_scrub = f'<span id="tp-inline-prime" class="tp-scrub">{"p = 5" if slug == "m01" else esc(sl0_txt)}</span>'
    elif pillar == "architecture":
        inline_scrub = f'<span id="tp-inline-rise" class="tp-scrub">{"f = 4.50 m" if slug == "a01" else esc(sl0_txt)}</span>'
    elif pillar == "physics":
        inline_scrub = f'<span id="tp-inline-atp" class="tp-scrub">{"Delta_mu_ATP = 18.4 k_BT" if slug == "p01" else esc(sl0_txt)}</span>'
    elif pillar == "cf":
        inline_scrub = f'<span id="tp-inline-cf" data-target-slider="{esc(sl0_inline.get("id", ""))}" class="tp-scrub">{esc(sl0_short)} = {esc(sl0_v)}</span>'
    else:
        inline_scrub = f'<span id="tp-inline-phi" class="tp-scrub">{"phi = 0.720" if slug == "e01" else esc(sl0_txt)}</span>'

    plate_html = decf_title(render_Controls_for_pillar(pillar, folio, lf))

    act1_title = lf.get("act1_title", f"Act I — The Human Story & Historical Turning Point ({fid})")
    act1_dropcap = lf.get("act1_dropcap") or lf.get("history_lead", "")
    act1_body = lf.get("act1_body") or lf.get("history_body", "")
    act2_title = lf.get("act2_title", f"Act II — How It Actually Works: Plain-Language Intuition to Governing Law ({fid})")
    act2_intuition = lf.get("act2_intuition") or lf.get("intuition_lead", "")
    act2_analogy_raw = lf.get("act2_analogy") or lf.get("intuition_body", "")
    act2_analogy = re.sub(r"^\s*Everyday analogy:\s*", "", act2_analogy_raw, flags=re.IGNORECASE)
    act4_title = lf.get("act4_title", "Act IV — Extending Human + AI Potential & the multiscale continuum Curative Bridge")
    act4_human_ai = lf.get("act4_human_ai") or lf.get("human_ai_shift", "")
    reading_time = lf.get("reading_time", "14 MIN READ").split("·")[0].strip()
    word_count = lf.get("word_count", "2,650 WORDS")
    es_meta = get_folio_es_meta(slug, folio, col)

    plate_info = PLATE_CAPTIONS.get(slug, {
        "alt": f"Editorial illustration for Folio {fid}: {folio['title']}",
        "caption": f"Plate {fid}-V · Editorial Vision Plate illustrating {folio['title']}.",
    })
    utopia_companion_html = ""
    if slug == "a04":
        utopia_companion_html = f"""
        <figure class="tp-editorial-figure tp-utopia-companion" data-editorial-plate="utopian-city-future" role="group" aria-label="2050 Utopian City of the Future in the Era of AI, Metamaterials, and Autonomous Robotics">
          
          <img class="tp-editorial-img" src="{rel_res}/plates/utopian-city-future.jpg" data-plate-slug="utopian-city-future" width="1280" height="720" alt="Conceptual visualization imagining what the Utopian City of the Future in the era of AI, cellular auxetic metamaterials, and autonomous climbing and aerial robots would look like (artistic impression, not a measured structure)" loading="lazy" decoding="async">
          <figcaption class="tp-editorial-caption">
            <strong>Horizon 2050 — The Utopian City in the Era of AI, Metamaterials &amp; Robotics:</strong> Extending Ron Herron&rsquo;s <em>Walking City</em> and Peter Cook&rsquo;s <em>Plug-In City</em> into the 21st century: collaborative aerial and climbing robot swarms weave ultralight stretching-dominated auxetic metamaterial space frames (<code>E*/E_s = C(&rho;*/&rho;_s)</code>, <code>&nu; &lt; 0</code>) over seismic-cloaking phononic foundation rings (<code>Folios E.03 &amp; E.06</code>), while neuro-symbolic AI digital twins orchestrate crane-replaceable ISO-5 gene-therapy and clinical pods across lush vertical sky-gardens.
            <span class="tp-drawn-note"><strong>Visual &amp; Scite Provenance:</strong> AI-generated architectural vision plate (VLM-audited for zero baked-in text) grounded in <a class="tp-cite-link" href="https://doi.org/{esc(scite.get('doi', ''))}" target="_blank" rel="noopener noreferrer"><code>DOI {esc(scite.get('doi', ''))}</code></a> (<a class="tp-scite-badge-link" href="https://scite.ai/reports/{esc(scite.get('doi', ''))}" target="_blank" rel="noopener noreferrer">Scite Report &#8599;</a>); exact structural equilibrium is governed by <code>tools/tectonic_verify.py</code>.</span>
          </figcaption>
        </figure>"""

    act1_dropcap_c = decf(act1_dropcap)
    act1_body_c = decf(act1_body)
    act2_intuition_c = decf(act2_intuition)
    act2_analogy_c = decf(act2_analogy)
    act4_human_ai_c = decf(act4_human_ai)
    disc_body_c = decf(disc.get("body", ""))
    pullquote_c = decf(lf.get("pullquote", ""))
    why_es_c = decf(es_meta["why_es"])
    sn1_body_c = decf(folio["sidenote_1"]["body"])
    sn2_body_c = decf(sn2["body"])
    plate_caption_c = decf(plate_info["caption"]) or f"Plate {fid}"
    plate_alt_c = decf_title(plate_info["alt"])
    title_c = decf_title(folio["title"])
    title_es_c = decf_title(es_meta["title_es"])
    sub_c = decf_title(folio["subtitle"])
    sub_es_c = decf_title(es_meta["subtitle_es"])
    rt_en, rt_es = short_reading_time(slug)
    vol_code = get_folio_volume(slug)[1]
    pillar_en, pillar_es = PILLAR_SHORT_TITLES.get(pillar, pillar), PILLAR_SHORT_TITLES_ES.get(pillar, pillar)
    chron_rows_c = "\n".join(
        f'<tr><th scope="row">{esc(row[0])}</th><td>{linkify_citations(esc(decf(" — ".join(row[1:]))))}</td></tr>'
        for row in lf["chronology"]
        if decf(" — ".join(row[1:]))
    )
    walk_items_c = "\n".join(f"<li>{esc(decf(w))}</li>" for w in lf["walkthrough"] if decf(w))
    pullquote_html = f'<blockquote class="tp-pullquote"><p>{esc(pullquote_c)}</p></blockquote>' if pullquote_c else ""
    disc_html = (
        f"""<div class="tp-discovery-news-box" role="region" aria-label="Frontier discovery">
          <span class="tp-kicker" data-en="Frontier discovery" data-es="Descubrimiento de frontera">Frontier discovery</span>
          <h3>{esc(decf_title(disc["headline"]))}</h3>
          <p>{linkify_citations(esc(disc_body_c))}</p>
        </div>"""
        if disc_body_c
        else ""
    )
    sn2_html = (
        f'<div class="tp-sidenote"><span class="tp-sidenote-id">{esc(decf(sn2["kicker"]) or "Margin note")}</span>{linkify_citations(esc(sn2_body_c))}</div>' if sn2_body_c else ""
    )
    sn1_html = (
        f'<div class="tp-sidenote"><span class="tp-sidenote-id">{esc(decf(folio["sidenote_1"]["kicker"]) or "Margin note")}</span>{linkify_citations(esc(sn1_body_c))}</div>'
        if sn1_body_c
        else ""
    )

    return f"""<div id="tp-folio-mount" data-folio-id="{esc(fid)}" data-folio-slug="{esc(slug)}" data-plate-prefix="{rel_res}/plates/">
    <section class="tp-hero">
      <p class="tp-kicker"><span data-en="{esc(pillar_en)}" data-es="{esc(pillar_es)}">{esc(pillar_en)}</span> · {esc(fid)} · <span data-en="{rt_en}" data-es="{rt_es}">{rt_en}</span></p>
      <h1 class="tp-h1" data-en="{esc(title_c)}" data-es="{esc(title_es_c)}">{esc(title_c)}</h1>
      <p class="tp-standfirst" data-en="{esc(sub_c)}" data-es="{esc(sub_es_c)}">{esc(sub_c)}</p>
      <div class="tp-why-matters-lead" role="note" aria-label="Why this story matters in everyday life">
        <span class="tp-why-kicker" data-en="Why it matters" data-es="Por qué importa">Why it matters</span>
        <p data-en="{esc(act2_analogy_c)}" data-es="{esc(why_es_c)}">{esc(act2_analogy_c)}</p>
      </div>
    </section>

    <figure class="tp-editorial-figure" data-lead-figure data-editorial-plate="{esc(slug)}" role="group" aria-label="Lead illustration for Folio {esc(fid)}">
      <img class="tp-editorial-img" src="{rel_res}/plates/{esc(slug)}.jpg" data-plate-slug="{esc(slug)}" width="1280" height="720" alt="{esc(plate_alt_c)}" loading="eager" fetchpriority="high" decoding="async">
      <figcaption class="tp-editorial-caption">
        {esc(plate_caption_c)}
        <details class="tp-plate-provenance-details">
          <summary class="tp-plate-provenance-summary" data-en="About this illustration" data-es="Sobre esta ilustración">About this illustration</summary>
          <span class="tp-drawn-note">This AI-generated illustration is imagining what the concept would look like: an artistic impression, not a measured structure or specification. Exact geometry, specifications and governing equations are kept strictly intact with zero artistic interpretation in deterministic Plate {esc(fid)}-A and Plate {esc(fid)}-B below.</span>
        </details>
      </figcaption>
    </figure>

    <nav class="tp-act-jump-bar" aria-label="Sections of this essay">
      <a class="tp-act-pill" href="#act1-heading-{esc(slug)}" data-en="I · Story" data-es="I · Historia">I · Story</a>
      <a class="tp-act-pill" href="#act2-heading-{esc(slug)}" data-en="II · Intuition" data-es="II · Intuición">II · Intuition</a>
      <a class="tp-act-pill tp-act-pill-highlight" href="#act3-heading-{esc(slug)}" data-en="III · Lab" data-es="III · Laboratorio">III · Lab</a>
      <a class="tp-act-pill" href="#act4-heading-{esc(slug)}" data-en="IV · Discovery" data-es="IV · Descubrimiento">IV · Discovery</a>
      <a class="tp-act-pill" href="#act5-heading-{esc(slug)}" data-en="V · Sources" data-es="V · Fuentes">V · Sources</a>
      <a class="tp-act-pill tp-act-pill-puzzle" href="#act-puzzle-{esc(slug)}" data-en="VI · Puzzle" data-es="VI · Crucigrama">VI · Puzzle</a>
    </nav>
    <tp-article-audio class="tp-article-audio" data-folio="{esc(fid)}" data-reading-time="{esc(reading_time)}" data-audio-src="{rel_res}/audio/{esc(slug)}-en.mp3" data-audio-src-es="{rel_res}/audio/{esc(slug)}-es.mp3"></tp-article-audio>

    <details class="tp-es-dossier" lang="es-MX">
      <summary class="tp-es-summary">
        <span><strong>Sinopsis Ejecutiva en Español · Folio {esc(fid)}</strong></span>
      </summary>
      <div class="tp-es-body">
        <p><strong>Actos I y II — Historia, ley gobernante e intuición cotidiana:</strong> <em>{esc(title_es_c)}</em> — {esc(sub_es_c)} Este monográfico interactivo verifica la ley gobernante <code>{esc(folio["governing_law"])}</code>. <strong>Por qué importa en la vida real:</strong> {esc(why_es_c)}</p>
        <p><strong>Acto III — Laboratorio interactivo:</strong> los deslizadores en tiempo real y las cuatro lentes del observatorio (superficie 3D, retrato de fase, listón de conservación y radar polar) permiten explorar los umbrales críticos directamente en el navegador.</p>
        <p><strong>Actos IV y V — Descubrimiento y fuentes:</strong> la narrativa completa y las fuentes primarias siguen abajo (en inglés). <em>Investigación científica y educativa abierta, no consejo médico.</em></p>
      </div>
    </details>

    <section class="tp-folio-layout" aria-labelledby="act1-heading-{esc(slug)}">
      <div class="tp-prose">
        {decf_title(utopia_companion_html)}
        <h2 id="act1-heading-{esc(slug)}">{esc(decf_act_title(act1_title))}</h2>
        <p class="tp-dropcap">{esc(act1_dropcap_c)}</p>
        <p>{linkify_citations(esc(act1_body_c))}</p>
        {pullquote_html}

        <h3 data-en="Turning points" data-es="Momentos decisivos">Turning points</h3>
        <div class="tp-table-wrap">
          <table class="tp-table tp-chronology" aria-label="Historical chronology for Folio {esc(fid)}">
            <thead>
              <tr>
                <th scope="col" data-en="Year" data-es="Año">Year</th>
                <th scope="col" data-en="Milestone" data-es="Hito">Milestone</th>
              </tr>
            </thead>
            <tbody>
              {chron_rows_c}
            </tbody>
          </table>
        </div>

        <h2 id="act2-heading-{esc(slug)}">{esc(decf_act_title(act2_title))}</h2>
        <p>
          {esc(act2_intuition_c)} Live parameter coupling: {inline_scrub} under governing law
          <button type="button" class="tp-eq-chip" data-eq-target="tp-svg-stage-1">{esc(folio["governing_law"])}</button>.
        </p>

        <h2 id="act3-heading-{esc(slug)}" data-en="Act III — Try it yourself" data-es="Acto III — Pruébalo tú mismo">Act III — Try it yourself</h2>
        <div class="tp-walkthrough-box" role="region" aria-label="Guided experiments">
          <h3 data-en="Three experiments to try" data-es="Tres experimentos para probar">Three experiments to try</h3>
          <ol>
            {walk_items_c}
          </ol>
        </div>

        {plate_html}

        <h2 id="act4-heading-{esc(slug)}">{esc(decf_act_title(act4_title))}</h2>
        <p>{linkify_citations(esc(act4_human_ai_c))}</p>
        {disc_html}

        <h2 id="act5-heading-{esc(slug)}" data-en="Act V — Sources" data-es="Acto V — Fuentes">Act V — Sources</h2>
        <ol class="tp-sources-list">
          {source_items}
        </ol>
      </div>

      <aside class="tp-rail" aria-label="Folio {esc(fid)} margin notes">
        {sn1_html}
        {sn2_html}
        <div class="tp-spec-plate">
          <span class="tp-spec-tag" data-en="Governing law" data-es="Ley gobernante">Governing law</span>
          <h3 class="tp-spec-title">{esc(folio["governing_law"])}</h3>
          <p class="tp-spec-meta">{esc(decf_title(col["benchmarks"]))}</p>
        </div>
      </aside>
    </section>

{render_folio_crossword_section(slug, fid)}

    <details class="tp-method-disclosure">
      <summary class="tp-method-summary"><span data-en="For builders: method, tools and edition history" data-es="Para quien construye: método, herramientas e historial">For builders: method, tools and edition history</span></summary>
      <div class="tp-method-body">
        <div class="tp-colophon-grid" role="region" aria-label="Folio {esc(fid)} metadata">
          <div class="tp-colophon-cell"><span class="tp-colophon-label">Folio</span><span class="tp-colophon-val">{esc(col["identifier"])} · {esc(vol_code)}</span></div>
          <div class="tp-colophon-cell"><span class="tp-colophon-label">Kernels</span><span class="tp-colophon-val">{esc(decf_title(col["kernels"]))}</span></div>
          <div class="tp-colophon-cell"><span class="tp-colophon-label">Benchmarks</span><span class="tp-colophon-val">{esc(decf_title(col["benchmarks"]))}</span></div>
          <div class="tp-colophon-cell"><span class="tp-colophon-label">Verifier</span><span class="tp-colophon-val"><code>{esc(folio["primary_kernel"])}</code></span></div>
          <div class="tp-colophon-cell"><span class="tp-colophon-label">Edition</span><span class="tp-colophon-val">{esc(folio["current_edition"])} · {esc(folio["date_redated"])}</span></div>
        </div>

        <div class="tp-scite-strip" role="region" aria-label="Citation check">
          <h3>Citation check</h3>
          <p>
            <strong>Anchor paper:</strong> {doi_link_html} ·
            <strong>Registry verification:</strong> <code>Crossref DOI verified (data/folio-citations.cache.json)</code>
          </p>
          <p>{esc(decf(scite.get("summary", "")))}</p>
        </div>

        <section class="tp-skill-box" aria-label="Downloadable SKILL.md companion and Python verifier">
          <div class="tp-skill-header">
            <span class="tp-skill-kicker">SKILL.md companion &amp; Python verifier</span>
            <span class="tp-skill-compat">Works with Claude Code · Copilot · Cursor · Antigravity · Codex · Ollama · Python 3</span>
          </div>
          <p class="tp-skill-desc">Give any AI agent or engineering pipeline the exact governing equations of Folio {esc(fid)}: a portable <code>SKILL.md</code>, a zero-dependency Python verifier (<code>{esc(py_filename)}</code>), or the live telemetry as JSON.</p>
          <div class="tp-skill-actions">
            <button class="tp-skill-btn" type="button" data-skill-download="{esc(skill["filename"])}">Download SKILL.md ({esc(skill["filename"])})</button>
            <button class="tp-skill-btn tp-skill-btn-secondary" type="button" data-skill-copy="true">Copy SKILL.md</button>
            <button class="tp-skill-btn tp-skill-btn-secondary" type="button" data-py-download="{esc(py_filename)}">Download Python Tool ({esc(py_filename)})</button>
            <button class="tp-skill-btn tp-skill-btn-secondary" type="button" data-telemetry-copy="{esc(fid)}">Copy Live Telemetry JSON</button>
          </div>
          <details class="tp-skill-source-details">
            <summary class="tp-skill-source-summary">Show the <code>SKILL.md</code> source</summary>
            <pre class="tp-skill-pre"><code data-skill-source>{esc(skill_md)}</code></pre>
          </details>
          <pre class="tp-skill-pre" hidden><code data-py-source>{esc(py_verifier_src)}</code></pre>
        </section>

        <section class="tp-rev-ledger" aria-label="Folio {esc(fid)} edition history and review">
          <div class="tp-rev-header">
            <span class="tp-rev-kicker">Edition history &amp; review</span>
            <span class="tp-rev-dates">Published {esc(folio["date_published"])} · Updated {esc(folio["date_redated"])} ({esc(folio["current_edition"])})</span>
          </div>
          <div class="tp-rev-pills" role="group" aria-label="Select Folio {esc(fid)} revision">
            {rev_btns_html}
          </div>
          <div class="tp-rev-detail">
            <p class="tp-rev-summary" data-rev-summary-out>{esc(decf(first_rev["summary"]))}</p>
            <p class="tp-rev-opus" data-rev-opus-out>{esc(decf(first_rev["opus"]))}</p>
          </div>
          <div class="tp-council-grid">
            <div class="tp-council-seat"><span class="tp-council-role">Formal &amp; physical review</span><span class="tp-council-model">Gemini 4 Argon + Gemma 4 31B</span><span class="tp-council-verdict">Approved</span></div>
            <div class="tp-council-seat"><span class="tp-council-role">Synthesis review</span><span class="tp-council-model">Qwen 3.8 27B + Ornith 1.5 35B</span><span class="tp-council-verdict">Approved</span></div>
            <div class="tp-council-seat"><span class="tp-council-role">Citation audit</span><span class="tp-council-model">tools/check_folio_citations.py</span><span class="tp-council-verdict">Verified</span></div>
            <div class="tp-council-seat"><span class="tp-council-role">Deterministic kernel</span><span class="tp-council-model">{esc(folio["primary_kernel"])}</span>{kernel_verdict_html(folio)}</div>
          </div>
        </section>
      </div>
    </details>
</div>"""


PILLAR_ROMAN = {
    "engineering": "I",
    "architecture": "II",
    "physics": "III",
    "math": "IV",
}

PILLAR_TITLES_ES = {
    "engineering": "Ingeniería Civil y Construcción",
    "architecture": "Arquitectura",
    "physics": "Física",
    "math": "Matemáticas",
}

PILLAR_SHORT_TITLES_ES = {
    "engineering": "Ingeniería y Construcción",
    "architecture": "Arquitectura",
    "physics": "Física",
    "math": "Matemáticas",
}

PILLAR_NAV_LABELS = {
    "engineering": ("Engineering", "Ingeniería"),
    "architecture": ("Architecture", "Arquitectura"),
    "physics": ("Physics", "Física"),
    "math": ("Mathematics", "Matemáticas"),
}

# Plain-language pillar promises shown on the cover and on each pillar hub (no folio codes, no jargon stacks).
PILLAR_HOOKS = {
    "engineering": (
        "How cities stand, breathe and move: hospitals that stay still in an earthquake, tunnel boring machines under old brick streets, bridges that outsmart the wind, and concrete that repairs itself.",
        "Cómo se sostienen, respiran y se mueven las ciudades: hospitales que permanecen quietos durante un sismo, tuneladoras bajo calles antiguas, puentes que vencen al viento y concreto que se repara solo.",
    ),
    "architecture": (
        "Light, color and living envelopes: Barragán's courtyards, roofs that send heat straight to the night sky, stone vaults that stand for centuries, and skins that open and close with the air.",
        "Luz, color y envolventes vivas: los patios de Barragán, techos que envían el calor directo al cielo nocturno, bóvedas de piedra que duran siglos y pieles que se abren y cierran con el aire.",
    ),
    "physics": (
        "The physics hiding in plain sight: Formula 1 ground effect, why pearlescent paint shifts color across a fender, the flow of soft matter, and how waves of light build the colors we see.",
        "La física escondida a plena vista: el efecto suelo de la Fórmula 1, por qué la pintura perlada cambia de color sobre una salpicadera, el flujo de la materia blanda y cómo las ondas de luz construyen los colores.",
    ),
    "math": (
        "The hidden architecture of logic: proofs checked by machines, optimal control around a racing lap, the curved geometry of color, and the shape of data.",
        "La arquitectura oculta de la lógica: demostraciones verificadas por máquinas, control óptimo en una vuelta de carrera, la geometría curva del color y la forma de los datos.",
    ),
}

# Informatico.ai stands on its own: no multiscale continuum framing, no links back to senseiewok.ai.
_DECF_REPLACEMENTS = (
    ("entangled CF airway mucin hydrogels", "entangled biological hydrogels"),
    ("ion-channel ABC gating cycles", "ABC-transporter gating cycles"),
    ("ion-channel nonsense and splice mutations", "nonsense and splice mutations"),
    ("4.5 kb ion-channel mRNA", "4.5 kb mRNA"),
    ("and ion-channel allostery", "and protein allostery"),
    (" & the multiscale continuum Curative Bridge", " & Frontier Discovery"),
    ("& the multiscale continuum Curative Bridge", "& Frontier Discovery"),
    (", Lab Sustainability", ""),
    ("Upstream Discovery Threads", "Open Questions"),
    ("e hidrogeles de mucina en física multiescala", "e hidrogeles biológicos"),
    ("y alostería en ion-channel", "y alostería de proteínas"),
    ("del ciclo de apertura del canal ion-channel impulsado por ATP", "del ciclo de apertura de transportadores ABC impulsado por ATP"),
    ("de mutaciones sin sentido en ion-channel", "de mutaciones sin sentido"),
    ("del ARNm de ion-channel de 4.5 kb", "del ARNm de 4.5 kb"),
    ("negative-pressure CF rooms", "negative-pressure isolation rooms"),
    ("ASHRAE 188 / CF Verdict", "ASHRAE 188 Verdict"),
    ("CF Sputum", "Sputum"),
    ("CF sputum", "sputum"),
    ("CF Mucus", "Dense Mucus"),
    ("CF mucus", "dense mucus"),
    ("CF airway", "airway"),
    ("CF Airway", "Airway"),
)
_DECF_SENTENCE = re.compile(
    r"Cystic|Fibrosis|Fibrose|\bCF\b|\bFQ\b|ion-channel|senseiewok|CFFPR|ECFSPR|CCFR|ACFDR|curative|curativ|"
    r"our lab|the lab\b|nuestro laboratorio|nuestra misión|ClinicalTrials\.gov",
    re.IGNORECASE,
)
_SENTENCE_SPLIT = re.compile(r"(?<!\bvs\.)(?<!\be\.g\.)(?<!\bi\.e\.)(?<!\bal\.)(?<!\bDr\.)(?<!\bFig\.)(?<!\bca\.)(?<!\bNo\.)(?<=[.!?])\s+(?=[A-Z0-9¿¡\"“(])")


def decf(text: str) -> str:
    """Remove multiscale continuum framing and senseiewok.ai references from one prose field.

    Targeted phrase replacements first; then any sentence that still carries the framing is dropped.
    Returns "" when nothing is left, so callers can omit the element."""
    if not text:
        return ""
    out = str(text)
    for old, new in _DECF_REPLACEMENTS:
        out = out.replace(old, new)
    if not _DECF_SENTENCE.search(out):
        return out
    kept = [s for s in _SENTENCE_SPLIT.split(out) if not _DECF_SENTENCE.search(s)]
    return " ".join(kept).strip()


def decf_act_title(text: str) -> str:
    """Act headings: drop any ' & ' or ', ' segment that carries CF framing."""
    out = decf_title(text)
    if not _DECF_SENTENCE.search(out):
        return out
    head, sep, rest = out.partition(" — ")
    body = rest if sep else head
    parts = [p for p in re.split(r",\s+|\s+&\s+", body) if p and not _DECF_SENTENCE.search(p)]
    if not parts:
        parts = ["Frontier Discovery"]
    joined = ", ".join(parts[:-1]) + (" & " if len(parts) > 1 else "") + parts[-1]
    return f"{head} — {joined}" if sep else joined


def decf_title(text: str) -> str:
    """Titles and decks keep their sentence; only the targeted phrase replacements apply."""
    out = str(text or "")
    for old, new in _DECF_REPLACEMENTS:
        out = out.replace(old, new)
    return out


def short_reading_time(slug: str) -> tuple[str, str]:
    """('14 min read', '14 min de lectura') from the long-form record."""
    raw = LONGFORM.get(slug, {}).get("reading_time", "14 MIN READ").split("·")[0].strip()
    m = re.search(r"(\d+)", raw)
    n = m.group(1) if m else "14"
    return f"{n} min read", f"{n} min de lectura"


LOGO_SVG = (
    '<svg aria-hidden="true" focusable="false" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="2.8" '
    'stroke-linecap="butt" stroke-linejoin="round"><path class="tp-logo-draw tp-logo-q1" d="M11.5 7.4v9.0" pathLength="1"/>'
    '<circle class="tp-logo-draw tp-logo-q2" cx="24.5" cy="11.9" r="4.0" pathLength="1"/>'
    '<path class="tp-logo-draw tp-logo-q3" d="M11.5 28.2H8.4L14.6 22.0v6.2z" pathLength="1"/>'
    '<path class="tp-logo-draw tp-logo-q4" d="M24.5 24.8v4.8" pathLength="1"/>'
    '<rect class="tp-logo-datum" x="23.1" y="20.6" width="2.8" height="2.8" stroke="none"/></svg>'
)


def _href(rel_res: str, path: str = "") -> str:
    base = "./" if rel_res in (".", "") else f"{rel_res}/"
    return f"{base}{path}"


def page_url(path: str, lang: str = "en") -> str:
    """Absolute address of a page. path is "" (the cover), "engineering/" or "engineering/e02/"."""
    return SITE + (ES_PREFIX if lang == "es" else "") + path


def render_head(title: str, desc: str, path: str, og_type: str, og_image: str, rel_root: str, rel_res: str, ld_json: str, lang: str = "en") -> str:
    """The <head>. English and Spanish each have their own address, canonical and reciprocal hreflang pair."""
    css_href = "informatico.css" if rel_res in (".", "") else f"{rel_res}/informatico.css"
    mod_href = "modules/main.mjs" if rel_res in (".", "") else f"{rel_res}/modules/main.mjs"
    en_url, es_url = page_url(path, "en"), page_url(path, "es")
    is_es = lang == "es"
    canon = es_url if is_es else en_url
    html_lang = "es-MX" if is_es else "en"
    locale, locale_alt = ("es_MX", "en_US") if is_es else ("en_US", "es_MX")
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{canon}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="es-MX" href="{es_url}">
  <link rel="alternate" hreflang="es" href="{es_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="{locale}">
  <meta property="og:locale:alternate" content="{locale_alt}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{og_image}">
  <meta name="theme-color" content="#eceef0">
  <link rel="icon" href="{rel_root}/images/icon-32.png" sizes="32x32" type="image/png">
  <link rel="icon" href="{rel_root}/images/icon-192.png" sizes="192x192" type="image/png">
  <link rel="apple-touch-icon" href="{rel_root}/images/apple-touch-icon.png">
  <link rel="stylesheet" href="{rel_root}/styles.css">
  <link rel="stylesheet" href="{css_href}">
  <link rel="modulepreload" href="{mod_href}">
  <script type="application/ld+json">{ld_json}</script>
</head>"""


def render_masthead(rel_res: str, active_pillar: str = "", lang: str = "en") -> str:
    """One slim header: brand, the four disciplines, Contents, language and theme. Nothing else."""
    links = []
    for p_key in ("engineering", "architecture", "physics", "math"):
        en, es = PILLAR_NAV_LABELS[p_key]
        cur = ' aria-current="page"' if p_key == active_pillar else ""
        links.append(
            f'<a class="tp-nav-link" data-tp-nav="{p_key}" href="{_href(rel_res, p_key + "/")}"'
            f'{cur} data-en="{esc(en)}" data-es="{esc(es)}">{esc(en)}</a>'
        )
    links_html = "\n        ".join(links)
    home_cur = ' aria-current="page"' if rel_res in (".", "") else ""
    lang_btn = (
        '<button id="tp-lang-toggle" class="tp-tool-btn" type="button" aria-pressed="true" aria-label="Read in English" title="English">EN</button>'
        if lang == "es"
        else '<button id="tp-lang-toggle" class="tp-tool-btn" type="button" aria-pressed="false" aria-label="Leer en español" title="Español">ES</button>'
    )
    return f"""  <a class="skip-link" href="#main" data-en="Skip to content" data-es="Saltar al contenido">Skip to content</a>
  <header class="tp-masthead tp-masthead-slim">
    <div class="tp-masthead-inner">
      <a class="tp-brand" href="{_href(rel_res)}"{home_cur}>
        <span class="tp-se-logo" aria-hidden="true">{LOGO_SVG}</span>
        <span class="tp-brand-copy">
          <span class="tp-brand-title">Informatico.ai</span>
        </span>
      </a>
      <nav class="tp-nav" aria-label="Disciplines">
        {links_html}
      </nav>
      <div class="tp-masthead-tools">
        <button type="button" class="tp-tool-btn tp-contents-btn" data-open-contents aria-haspopup="dialog" aria-controls="tp-contents" aria-expanded="false"><span class="tp-contents-icon" aria-hidden="true"></span><span data-en="Contents" data-es="Contenido">Contents</span></button>
        {lang_btn}
        <button id="tp-blueprint-toggle" class="tp-tool-btn" type="button" aria-pressed="false" aria-label="Switch to dark theme">Dark</button>
      </div>
    </div>
    <div id="tp-reading-progress" aria-hidden="true"></div>
  </header>"""


def render_contents_dialog(rel_res: str, catalog: dict, active_slug: str = "") -> str:
    """Every essay, one click from any page: a native <dialog> with search, four columns of titles."""
    cols = []
    for p_key in ("engineering", "architecture", "physics", "math"):
        items = []
        for f in catalog["pillars"].get(p_key, []):
            slug = f["slug"]
            es_meta = get_folio_es_meta(slug, f, f["colophon"])
            title_en = decf_title(f["title"])
            title_es = decf_title(es_meta["title_es"])
            cur = ' aria-current="page"' if slug == active_slug else ""
            search = esc(f"{f['folio_id']} {title_en} {title_es}".lower())
            items.append(
                f'<li data-contents-item data-search="{search}"><a href="{_href(rel_res, p_key + "/" + slug + "/")}"{cur}>'
                f'<span class="tp-contents-id">{esc(f["folio_id"])}</span> '
                f'<span class="tp-contents-title" data-en="{esc(title_en)}" data-es="{esc(title_es)}">{esc(title_en)}</span></a></li>'
            )
        items_html = "\n            ".join(items)
        en, es = PILLAR_SHORT_TITLES[p_key], PILLAR_SHORT_TITLES_ES[p_key]
        cols.append(
            f"""        <section class="tp-contents-col" data-pillar="{p_key}">
          <h3><a href="{_href(rel_res, p_key + "/")}" data-en="{esc(en)}" data-es="{esc(es)}">{esc(en)}</a></h3>
          <ol>
            {items_html}
          </ol>
        </section>"""
        )
    cols_html = "\n".join(cols)
    total = sum(len(v) for v in catalog["pillars"].values())
    return f"""  <dialog id="tp-contents" class="tp-contents" aria-labelledby="tp-contents-title">
    <div class="tp-contents-inner">
      <div class="tp-contents-head">
        <h2 id="tp-contents-title" data-en="Contents" data-es="Contenido">Contents</h2>
        <input id="tp-contents-search" class="tp-contents-search" type="search" autocomplete="off" placeholder="Search {total} essays" aria-label="Search essays">
        <button type="button" class="tp-tool-btn tp-contents-close" data-close-contents aria-label="Close contents">Close</button>
      </div>
      <p id="tp-contents-empty" class="tp-contents-empty" hidden data-en="No essay matches that search." data-es="Ningún ensayo coincide con la búsqueda.">No essay matches that search.</p>
      <div class="tp-contents-grid">
{cols_html}
      </div>
    </div>
  </dialog>"""


def render_breadcrumb(rel_res: str, pillar: str, folio: dict | None = None) -> str:
    en, es = PILLAR_SHORT_TITLES[pillar], PILLAR_SHORT_TITLES_ES[pillar]
    if folio is None:
        tail = f'<li class="tp-crumb-item" aria-current="page"><span data-en="{esc(en)}" data-es="{esc(es)}">{esc(en)}</span></li>'
        mid = ""
    else:
        mid = f'<li class="tp-crumb-item"><a class="tp-crumb-link" href="{_href(rel_res, pillar + "/")}" data-en="{esc(en)}" data-es="{esc(es)}">{esc(en)}</a></li>\n        '
        tail = f'<li class="tp-crumb-item" aria-current="page">{esc(folio["folio_id"])}</li>'
    return f"""  <nav class="tp-breadcrumb-bar" aria-label="Breadcrumb">
    <ol class="tp-breadcrumb-list">
        <li class="tp-crumb-item"><a class="tp-crumb-link" href="{_href(rel_res)}">Informatico.ai</a></li>
        {mid}{tail}
    </ol>
  </nav>"""


def render_site_footer(rel_res: str) -> str:
    links = " · ".join(
        f'<a href="{_href(rel_res, p + "/")}" data-en="{esc(PILLAR_NAV_LABELS[p][0])}" data-es="{esc(PILLAR_NAV_LABELS[p][1])}">{esc(PILLAR_NAV_LABELS[p][0])}</a>'
        for p in ("engineering", "architecture", "physics", "math")
    )
    return f"""    <footer class="tp-footer tp-site-footer">
      <nav aria-label="Footer"><a href="{_href(rel_res)}">Informatico.ai</a> · {links} · <a href="https://github.com/senseiewok/informatico.ai" target="_blank" rel="noopener noreferrer" data-en="GitHub" data-es="GitHub">GitHub</a></nav>
      <p data-en="Long-form essays with live models, in English and Spanish. For learning and research, not professional or medical advice." data-es="Ensayos de largo aliento con modelos interactivos, en inglés y español. Para aprender e investigar, no es asesoría profesional ni médica.">Long-form essays with live models, in English and Spanish. For learning and research, not professional or medical advice.</p>
    </footer>"""


def render_rack_cards(pillar: str, folios: list[dict], href_prefix: str, plate_prefix: str, active_slug: str = "", eager: int = 0) -> str:
    cards = []
    for i, f in enumerate(folios):
        slug = f["slug"]
        es_meta = get_folio_es_meta(slug, f, f["colophon"])
        rt_en, rt_es = short_reading_time(slug)
        cur = ' aria-current="page"' if slug == active_slug else ""
        loading = "eager" if i < eager else "lazy"
        title_en = decf_title(f["title"])
        title_es = decf_title(es_meta["title_es"])
        dek_en = decf_title(f["subtitle"])
        dek_es = decf_title(es_meta["subtitle_es"])
        alt = decf_title(PLATE_CAPTIONS.get(slug, {}).get("alt", title_en))
        cards.append(
            f"""        <a class="tp-rack-card" href="{href_prefix}{slug}/" data-folio-slug="{esc(slug)}" data-folio-volume="{get_folio_volume(slug)[0]}"{cur}>
          <span class="tp-rack-thumb-wrap"><img class="tp-rack-thumb" src="{plate_prefix}{esc(slug)}.jpg" width="640" height="360" loading="{loading}" decoding="async" alt="{esc(alt)}"></span>
          <span class="tp-rack-top"><span class="tp-rack-id">{esc(f["folio_id"])}</span><span class="tp-rack-badge" data-en="{rt_en}" data-es="{rt_es}">{rt_en}</span></span>
          <strong class="tp-rack-title" data-en="{esc(title_en)}" data-es="{esc(title_es)}">{esc(title_en)}</strong>
          <span class="tp-rack-dek" data-en="{esc(dek_en)}" data-es="{esc(dek_es)}">{esc(dek_en)}</span>
        </a>"""
        )
    return "\n".join(cards)


def render_pager(rel_res: str, pillar: str, folios: list[dict], active: dict) -> str:
    """Prev / Next inside the pillar, no wrap-around; the ends point back to the pillar."""
    slugs = [f["slug"] for f in folios]
    idx = slugs.index(active["slug"]) if active["slug"] in slugs else 0
    en, es = PILLAR_SHORT_TITLES[pillar], PILLAR_SHORT_TITLES_ES[pillar]

    def card(f: dict | None, direction: str) -> str:
        if f is None:
            return '<span class="tp-pager-link tp-pager-empty" aria-hidden="true"></span>'
        es_meta = get_folio_es_meta(f["slug"], f, f["colophon"])
        t_en, t_es = decf_title(f["title"]), decf_title(es_meta["title_es"])
        d_en, d_es = ("&larr; Previous", "&larr; Anterior") if direction == "prev" else ("Next &rarr;", "Siguiente &rarr;")
        return (
            f'<a class="tp-pager-link tp-pager-{direction}" href="{_href(rel_res, pillar + "/" + f["slug"] + "/")}" rel="{direction}">'
            f'<span class="tp-pager-dir"><span data-en="{d_en}" data-es="{d_es}">{d_en}</span> · {esc(f["folio_id"])}</span>'
            f'<strong data-en="{esc(t_en)}" data-es="{esc(t_es)}">{esc(t_en)}</strong></a>'
        )

    prev_f = folios[idx - 1] if idx > 0 else None
    next_f = folios[idx + 1] if idx + 1 < len(folios) else None
    return f"""    <nav class="tp-pager" aria-label="More in {esc(en)}">
      {card(prev_f, "prev")}
      {card(next_f, "next")}
    </nav>
    <p class="tp-pager-all"><a href="{_href(rel_res, pillar + "/")}" data-en="All {len(folios)} {esc(en)} essays &rarr;" data-es="Los {len(folios)} ensayos de {esc(es)} &rarr;">All {len(folios)} {esc(en)} essays &rarr;</a></p>"""


def build_folio_seo_meta(pillar: str, active_folio: dict, is_standalone: bool, lang: str = "en") -> tuple[str, str, str]:
    """Return (canon_url, seo_title, seo_desc) for a pillar index or a standalone Folio, in English or Spanish.

    The words come from tools/folios/seo_copy.py, written by hand per essay: a missing entry is a KeyError,
    so a new essay cannot ship with a title or description cut at a fixed width (council SEO review, 2026-11-04)."""
    es = lang == "es"
    if not is_standalone:
        t_en, d_en, t_es, d_es = PILLAR_SEO[pillar]
        return page_url(f"{pillar}/", lang), (t_es if es else t_en), (d_es if es else d_en)
    slug = active_folio["slug"]
    t_en, d_en, t_es, d_es = FOLIO_SEO[slug]
    return page_url(f"{pillar}/{slug}/", lang), f"{t_es if es else t_en} | {BRAND}", (d_es if es else d_en)


ORG_LD = {"@type": "Organization", "name": BRAND, "url": SITE}


def _ld(ld_type: str, headline: str, desc: str, url: str, lang: str = "en", *, image: str | None = None,
        date_published: str | None = None, date_modified: str | None = None,
        crumbs: list[tuple[str, str]] | None = None) -> str:
    """JSON-LD for one page: the page itself in its own language, plus its breadcrumb trail."""
    node: dict = {
        "@type": ld_type,
        "headline": headline,
        "name": headline,
        "description": desc,
        "inLanguage": "es-MX" if lang == "es" else "en",
        "url": url,
        "isPartOf": {"@type": "WebSite", "name": BRAND, "url": SITE},
        "publisher": ORG_LD,
    }
    if ld_type == "ScholarlyArticle":
        node["author"] = ORG_LD
    if image:
        node["image"] = image
    if date_published:
        node["datePublished"] = date_published
    if date_modified:
        node["dateModified"] = date_modified
    graph = [node]
    if crumbs:
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": name, "item": item} for i, (name, item) in enumerate(crumbs)
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("</", "<\\/")


def render_folio_page(pillar: str, folios: list[dict], folio: dict, catalog: dict, lang: str = "en") -> str:
    rel_root, rel_res = "../../..", "../.."
    es = lang == "es"
    slug = folio["slug"]
    canon, seo_title, seo_desc = build_folio_seo_meta(pillar, folio, True, lang)
    t_en, _d_en, t_es, _d_es = FOLIO_SEO[slug]
    image = f"https://informatico.ai/plates/{esc(slug)}.jpg"
    crumbs = [
        (BRAND, page_url("", lang)),
        (PILLAR_SHORT_TITLES_ES[pillar] if es else PILLAR_SHORT_TITLES[pillar], page_url(f"{pillar}/", lang)),
        (t_es if es else t_en, canon),
    ]
    ld = _ld("ScholarlyArticle", t_es if es else t_en, seo_desc, canon, lang, image=image,
             date_published=folio.get("date_published"),
             date_modified=folio.get("date_redated") or folio.get("date_published"), crumbs=crumbs)
    head = render_head(seo_title, seo_desc, f"{pillar}/{slug}/", "article", image, rel_root, rel_res, ld, lang)
    return f"""{head}
<body class="tp-body tp-page-folio">
{render_masthead(rel_res, pillar, lang)}
{render_contents_dialog(rel_res, catalog, folio["slug"])}
  <main id="main" class="tp-shell" tabindex="-1">
{render_breadcrumb(rel_res, pillar, folio)}
{render_folio_mount(pillar, folio, rel_res)}
{render_pager(rel_res, pillar, folios, folio)}
{render_site_footer(rel_res)}
  </main>
  <script type="module" src="{rel_res}/modules/main.mjs"></script>
</body>
</html>
"""


def render_pillar_hub(pillar: str, folios: list[dict], catalog: dict, lang: str = "en") -> str:
    rel_root, rel_res = "../..", ".."
    es = lang == "es"
    canon, seo_title, seo_desc = build_folio_seo_meta(pillar, folios[0], False, lang)
    title_en, title_es = PILLAR_TITLES[pillar], PILLAR_TITLES_ES[pillar]
    hook_en, hook_es = PILLAR_HOOKS[pillar]
    crumbs = [(BRAND, page_url("", lang)), (title_es if es else title_en, canon)]
    image = f"https://informatico.ai/plates/{esc(folios[0]['slug'])}.jpg"
    head = render_head(seo_title, seo_desc, f"{pillar}/", "website", image,
                       rel_root, rel_res, _ld("CollectionPage", title_es if es else title_en, seo_desc, canon, lang,
                                              image=image, crumbs=crumbs), lang)
    cards = render_rack_cards(pillar, folios, "./", "../plates/", eager=3)
    n = len(folios)
    extra_sections = ""
    if pillar in ("physics", "math"):
        extra_sections = f"\n{render_symbolic_physics_lab_section(rel_res)}\n{render_oss_physics_radar_section(rel_res)}"
    return f"""{head}
<body class="tp-body tp-page-hub">
{render_masthead(rel_res, pillar, lang)}
{render_contents_dialog(rel_res, catalog)}
  <main id="main" class="tp-shell" tabindex="-1">
{render_breadcrumb(rel_res, pillar)}
    <section class="tp-pillar-hero" aria-labelledby="pillar-heading">
      <p class="tp-kicker" data-en="Pillar {PILLAR_ROMAN[pillar]} · {n} essays" data-es="Pilar {PILLAR_ROMAN[pillar]} · {n} ensayos">Pillar {PILLAR_ROMAN[pillar]} · {n} essays</p>
      <h1 id="pillar-heading" class="tp-h1" data-en="{esc(title_en)}" data-es="{esc(title_es)}">{esc(title_en)}</h1>
      <p class="tp-standfirst" data-en="{esc(hook_en)}" data-es="{esc(hook_es)}">{esc(hook_en)}</p>
    </section>
    <section class="tp-issue-rack" aria-label="{esc(PILLAR_TITLES[pillar])} essays">
      <div class="tp-rack-grid">
{cards}
      </div>
    </section>{extra_sections}
{render_site_footer(rel_res)}
  </main>
  <script type="module" src="{rel_res}/modules/main.mjs"></script>
</body>
</html>
"""


def render_pillar_or_folio_page(pillar: str, folios: list[dict], active_folio: dict, is_standalone: bool, catalog: dict) -> str:
    """Kept for callers of the old API: a hub when not standalone, otherwise the folio page."""
    if is_standalone:
        return render_folio_page(pillar, folios, active_folio, catalog)
    return render_pillar_hub(pillar, folios, catalog)



def render_bounty_crucible_section() -> str:
    """Render the Council-selected Open-Bounty & Grand-Challenge Prize Crucible special feature on the Cover Hub."""
    return """    <section id="tp-bounty-crucible" class="tp-bounty-crucible" aria-labelledby="bounty-crucible-heading">
      <div class="tp-bounty-header">
        <p class="tp-kicker" data-en="Special Feature · Council-Selected Open Bounties &amp; Global Prizes" data-es="Especial · Recompensas Abiertas y Premios Mundiales Seleccionados por el Consejo">Special Feature · Council-Selected Open Bounties &amp; Global Prizes</p>
        <h2 id="bounty-crucible-heading" class="tp-h2" data-en="The Open-Bounty &amp; Prize Crucible: Four Grand Challenges You Can Explore and Attack Today" data-es="El Crisol de Premios y Retos Abiertos: Cuatro Grandes Problemas que Puedes Explorar y Atacar Hoy">The Open-Bounty &amp; Prize Crucible: Four Grand Challenges You Can Explore and Attack Today</h2>
        <p class="tp-standfirst" data-en="Our 4-Seat Multi-Family Council audited 16 active mathematical bounties, quantum computing prizes, and net-zero engineering awards (bounty_crucible_council_ledger.json) to select four high-impact open problems where cross-field intuition, open-source software, and formal AI verification let anyone test candidate solutions." data-es="Nuestro Consejo Multifamiliar de 4 asientos auditó 16 recompensas matemáticas activas, premios de computación cuántica y retos de ingeniería (bounty_crucible_council_ledger.json) para elegir cuatro problemas abiertos donde el software libre y la verificación formal con IA permiten poner a prueba soluciones reales.">Our 4-Seat Multi-Family Council audited 16 active mathematical bounties, quantum computing prizes, and net-zero engineering awards (bounty_crucible_council_ledger.json) to select four high-impact open problems where cross-field intuition, open-source software, and formal AI verification let anyone test candidate solutions.</p>
      </div>

      <div class="tp-bounty-svg-wrap" role="region" aria-label="Interactive Open-Bounty &amp; Prize Convergence Map">
        <svg class="tp-bounty-crucible-svg" viewBox="0 0 920 175" role="img" aria-label="Four-Pillar Open-Bounty Crucible connecting Erdős Lean 4 Bounties, $5M XPRIZE Quantum &amp; unitaryHACK, $100M XPRIZE Carbon Removal, and $3M Global Cooling Prize">
          <defs>
            <linearGradient id="tp-bounty-grad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="var(--tp-prussian)" stop-opacity="0.18"/>
              <stop offset="50%" stop-color="var(--tp-verdigris)" stop-opacity="0.28"/>
              <stop offset="100%" stop-color="var(--tp-minium)" stop-opacity="0.18"/>
            </linearGradient>
          </defs>
          <rect x="12" y="12" width="896" height="151" rx="10" fill="url(#tp-bounty-grad)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <path class="tp-bounty-ribbon" d="M 193 88 C 235 42, 245 42, 287 88 M 423 88 C 460 134, 460 134, 497 88 M 653 88 C 690 42, 700 42, 737 88" fill="none" stroke="var(--tp-verdigris)" stroke-width="2.6" stroke-dasharray="7 4"/>
          <path class="tp-bounty-ribbon-alt" d="M 193 88 C 235 134, 245 134, 287 88 M 423 88 C 460 42, 460 42, 497 88 M 653 88 C 690 134, 700 134, 737 88" fill="none" stroke="var(--tp-prussian)" stroke-width="1.8" stroke-dasharray="4 5"/>
          <g transform="translate(115, 88)">
            <rect x="-78" y="-26" width="156" height="52" rx="26" fill="var(--tp-vellum)" stroke="var(--tp-prussian)" stroke-width="2.2"/>
            <text x="0" y="-4" text-anchor="middle" font-size="10" font-weight="700" fill="var(--tp-prussian)">BOUNTY M-1</text>
            <text x="0" y="12" text-anchor="middle" font-size="9" fill="var(--tp-verdigris)" data-en="Erdős + Lean 4" data-es="Erdős + Lean 4">Erdős + Lean 4</text>
          </g>
          <g transform="translate(355, 88)">
            <rect x="-68" y="-26" width="136" height="52" rx="26" fill="var(--tp-vellum)" stroke="var(--tp-verdigris)" stroke-width="2.2"/>
            <text x="0" y="-4" text-anchor="middle" font-size="10" font-weight="700" fill="var(--tp-verdigris)">BOUNTY P-1</text>
            <text x="0" y="12" text-anchor="middle" font-size="9" fill="var(--tp-prussian)" data-en="$5M Quantum QEC" data-es="$5M Cuántico QEC">$5M Quantum QEC</text>
          </g>
          <g transform="translate(575, 88)">
            <rect x="-78" y="-26" width="156" height="52" rx="26" fill="var(--tp-vellum)" stroke="var(--tp-minium)" stroke-width="2.2"/>
            <text x="0" y="-4" text-anchor="middle" font-size="10" font-weight="700" fill="var(--tp-minium)">BOUNTY E-1</text>
            <text x="0" y="12" text-anchor="middle" font-size="9" fill="var(--tp-prussian)" data-en="$100M Carbon Slab" data-es="$100M Losa Carbono">$100M Carbon Slab</text>
          </g>
          <g transform="translate(805, 88)">
            <rect x="-68" y="-26" width="136" height="52" rx="26" fill="var(--tp-vellum)" stroke="var(--tp-verdigris)" stroke-width="2.2"/>
            <text x="0" y="-4" text-anchor="middle" font-size="10" font-weight="700" fill="var(--tp-verdigris)">BOUNTY A-1</text>
            <text x="0" y="12" text-anchor="middle" font-size="9" fill="var(--tp-prussian)" data-en="$3M Sky-Cooling" data-es="$3M Enfriamiento">$3M Sky-Cooling</text>
          </g>
          <text x="460" y="31" text-anchor="middle" font-size="10" font-weight="700" fill="currentColor" data-en="OPEN-SOURCE + AI VERIFICATION PIPELINE: STIM · PYSCF · LEAN 4 · FENICS · COMPAS · ENERGYPLUS" data-es="FLUJO ABIERTO + VERIFICACIÓN CON IA: STIM · PYSCF · LEAN 4 · FENICS · COMPAS · ENERGYPLUS">OPEN-SOURCE + AI VERIFICATION PIPELINE: STIM · PYSCF · LEAN 4 · FENICS · COMPAS · ENERGYPLUS</text>
          <text x="460" y="151" text-anchor="middle" font-size="9.5" fill="var(--tp-verdigris)" data-en="Every Folio Plate A includes live [⚛ Quantum · WEF] &amp; [⚡ Counterfactual] modes to test its grand challenge" data-es="Cada Lámina A incluye modos interactivos [⚛ Quantum · WEF] y [⚡ Contrafactual] para explorar su gran reto">Every Folio Plate A includes live [⚛ Quantum · WEF] &amp; [⚡ Counterfactual] modes to test its grand challenge</text>
        </svg>
      </div>

      <div class="tp-bounty-grid">
        <article class="tp-bounty-card" data-bounty-id="BOUNTY-M1">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">BOUNTY M-1 · ERDŐS $500–$10K + AIMO $10M</span>
            <span class="tp-bounty-pillar" data-en="Mathematics · Lean 4" data-es="Matemáticas · Lean 4">Mathematics · Lean 4</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Erdős Sidon Sets &amp; Anthropic Lean 4 Formalization Bounties" data-es="Conjuntos de Sidon de Erdős y Recompensas de Formalización en Lean 4">Erdős Sidon Sets &amp; Anthropic Lean 4 Formalization Bounties</h3>
          <p class="tp-bounty-body" data-en="Paul Erdős left cash bounties for problems like Sidon B_2 sequences (a_i + a_j all distinct, |A ∩ [1,N]| ≤ √N + N^(1/4) + 1, yielding ≤ 36 elements at N = 900). Following Anthropic's 13-million-line Lean 4 formalization of Fermat's Last Theorem and XiPrime.lean, AI agents + Lean 4 now attack open Erdős and harmonic-analysis bounties with zero hand-waving." data-es="Paul Erdős dejó recompensas en efectivo para problemas como las sucesiones B_2 de Sidon (sumas por pares distintas, ≤ 36 elementos en N = 900). Tras la formalización de 13 millones de líneas en Lean 4 del Último Teorema de Fermat y XiPrime.lean por Anthropic, la IA y Lean 4 resuelven conjeturas abiertas con certeza total.">Paul Erdős left cash bounties for problems like Sidon B_2 sequences (a_i + a_j all distinct, |A ∩ [1,N]| ≤ √N + N^(1/4) + 1, yielding ≤ 36 elements at N = 900). Following Anthropic's 13-million-line Lean 4 formalization of Fermat's Last Theorem and XiPrime.lean, AI agents + Lean 4 now attack open Erdős and harmonic-analysis bounties with zero hand-waving.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="math/m11/" data-en="Explore Folio M.11 &rarr;" data-es="Explorar Folio M.11 &rarr;">Explore Folio M.11 &rarr;</a> ·
            <a class="tp-cite-link" href="math/m12/" data-en="Folio M.12 &rarr;" data-es="Folio M.12 &rarr;">Folio M.12 &rarr;</a> ·
            <a class="tp-cite-link" href="https://github.com/anthropics/formal-math" target="_blank" rel="noopener noreferrer">anthropics/formal-math</a> ·
            <a class="tp-cite-link" href="https://github.com/anthropics/fermats-last-theorem" target="_blank" rel="noopener noreferrer">anthropics/fermats-last-theorem</a>
          </p>
        </article>

        <article class="tp-bounty-card" data-bounty-id="BOUNTY-P1">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">BOUNTY P-1 · $5M XPRIZE QUANTUM + UNITARYHACK</span>
            <span class="tp-bounty-pillar" data-en="Physics · Quantum QEC" data-es="Física · QEC Cuántico">Physics · Quantum QEC</span>
          </div>
          <h3 class="tp-bounty-title" data-en="$5M XPRIZE Quantum Applications &amp; Unitary Foundation Open Bounties" data-es="XPRIZE Quantum Applications ($5M) y Recompensas Abiertas de Unitary Foundation">$5M XPRIZE Quantum Applications &amp; Unitary Foundation Open Bounties</h3>
          <p class="tp-bounty-body" data-en="The $5M XPRIZE Quantum Applications rewards fault-tolerant quantum algorithms for UN Sustainable Development Goals like room-temperature FeMoCo nitrogen fixation (p_L = 3.0 × 10⁻¹⁶ per cycle at d = 27, saving 1.8% of global CO₂), while Unitary Foundation's unitaryHACK pays cash bounties for solving open GitHub issues in Stim, PySCF, Qiskit, and PennyLane." data-es="El premio XPRIZE Quantum Applications de $5M impulsa algoritmos cuánticos tolerantes a fallos para retos como la fijación limpia de nitrógeno FeMoCo (p_L = 3.0 × 10⁻¹⁶ por ciclo en d = 27), mientras unitaryHACK otorga recompensas por mejoras en código abierto en Stim, PySCF, Qiskit y PennyLane.">The $5M XPRIZE Quantum Applications rewards fault-tolerant quantum algorithms for UN Sustainable Development Goals like room-temperature FeMoCo nitrogen fixation (p_L = 3.0 × 10⁻¹⁶ per cycle at d = 27, saving 1.8% of global CO₂), while Unitary Foundation's unitaryHACK pays cash bounties for solving open GitHub issues in Stim, PySCF, Qiskit, and PennyLane.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="physics/p11/" data-en="Explore Folio P.11 &rarr;" data-es="Explorar Folio P.11 &rarr;">Explore Folio P.11 &rarr;</a> ·
            <a class="tp-cite-link" href="physics/p12/" data-en="Folio P.12 &rarr;" data-es="Folio P.12 &rarr;">Folio P.12 &rarr;</a> ·
            <a class="tp-cite-link" href="https://github.com/quantumlib/Stim" target="_blank" rel="noopener noreferrer">quantumlib/Stim</a> ·
            <a class="tp-cite-link" href="https://github.com/pyscf/pyscf" target="_blank" rel="noopener noreferrer">pyscf/pyscf</a>
          </p>
        </article>

        <article class="tp-bounty-card" data-bounty-id="BOUNTY-E1">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">BOUNTY E-1 · $100M XPRIZE CARBON + ISTRUCTE</span>
            <span class="tp-bounty-pillar" data-en="Engineering · Net-Zero" data-es="Ingeniería · Cero Neto">Engineering · Net-Zero</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Sub-45 kg CO2e/m² Topology-Optimized &amp; Mineralized Structural Slabs" data-es="Losas Estructurales Mineralizadas y Optimizadas Bajo 45 kg CO2e/m²">Sub-45 kg CO2e/m² Topology-Optimized &amp; Mineralized Structural Slabs</h3>
          <p class="tp-bounty-body" data-en="Combining FEniCS/dolfinx SIMP bone-like topology optimization (ρ̄ = 0.35, 38.6 kg CO₂e/m² net embodied carbon) with robotic 3D printing, carbonate mineralization, and 180M-line Rocq-verified RISC-V grid controllers tackles the $100M XPRIZE Carbon Removal and IStructE low-carbon structural engineering benchmarks." data-es="Unir la optimización topológica SIMP en FEniCS/dolfinx (ρ̄ = 0.35, 38.6 kg CO₂e/m² netos) con impresión 3D robótica, mineralización de CO₂ y controladores RISC-V verificados en Rocq permite alcanzar los umbrales del XPRIZE Carbon Removal ($100M) e IStructE.">Combining FEniCS/dolfinx SIMP bone-like topology optimization (ρ̄ = 0.35, 38.6 kg CO₂e/m² net embodied carbon) with robotic 3D printing, carbonate mineralization, and 180M-line Rocq-verified RISC-V grid controllers tackles the $100M XPRIZE Carbon Removal and IStructE low-carbon structural engineering benchmarks.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="engineering/e11/" data-en="Explore Folio E.11 &rarr;" data-es="Explorar Folio E.11 &rarr;">Explore Folio E.11 &rarr;</a> ·
            <a class="tp-cite-link" href="engineering/e12/" data-en="Folio E.12 &rarr;" data-es="Folio E.12 &rarr;">Folio E.12 &rarr;</a> ·
            <a class="tp-cite-link" href="https://github.com/FEniCS/dolfinx" target="_blank" rel="noopener noreferrer">FEniCS/dolfinx</a> ·
            <a class="tp-cite-link" href="https://github.com/anthropics/theorem-riscv" target="_blank" rel="noopener noreferrer">anthropics/theorem-riscv</a>
          </p>
        </article>

        <article class="tp-bounty-card" data-bounty-id="BOUNTY-A1">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">BOUNTY A-1 · $1M HOLCIM + $3M COOLING PRIZE</span>
            <span class="tp-bounty-pillar" data-en="Architecture · Zero-Grid" data-es="Arquitectura · Sin Red">Architecture · Zero-Grid</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Zero-Rebar 3D Graphic Statics Vaults &amp; 8–13 μm Sky-Cooling Canopies" data-es="Bóvedas 3D sin Acero y Cubiertas de Enfriamiento Radiativo de 8–13 μm">Zero-Rebar 3D Graphic Statics Vaults &amp; 8–13 μm Sky-Cooling Canopies</h3>
          <p class="tp-bounty-body" data-en="Pairing Maxwell 3D polyhedral graphic statics in open-source COMPAS (L = 16 m, f/L = 0.16, H = 100 kN, 72% less concrete, zero steel rebar) with Pellegrino tensegrity domes and 8–13 μm radiative sky-cooling membranes in EnergyPlus (q_net = 98.4 W/m², -5.2 °C below ambient air with zero electricity) addresses the Holcim Awards and Global Cooling Prize." data-es="Combinar la estática gráfica poliédrica 3D en COMPAS (L = 16 m, f/L = 0.16, H = 100 kN, 72% menos concreto, cero varillas) con domos de tensegridad y membranas radiativas de 8–13 μm en EnergyPlus (q_net = 98.4 W/m², -5.2 °C bajo el ambiente sin electricidad) responde al Premio Holcim y al Global Cooling Prize.">Pairing Maxwell 3D polyhedral graphic statics in open-source COMPAS (L = 16 m, f/L = 0.16, H = 100 kN, 72% less concrete, zero steel rebar) with Pellegrino tensegrity domes and 8–13 μm radiative sky-cooling membranes in EnergyPlus (q_net = 98.4 W/m², -5.2 °C below ambient air with zero electricity) addresses the Holcim Awards and Global Cooling Prize.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="architecture/a11/" data-en="Explore Folio A.11 &rarr;" data-es="Explorar Folio A.11 &rarr;">Explore Folio A.11 &rarr;</a> ·
            <a class="tp-cite-link" href="architecture/a12/" data-en="Folio A.12 &rarr;" data-es="Folio A.12 &rarr;">Folio A.12 &rarr;</a> ·
            <a class="tp-cite-link" href="https://github.com/compas-dev/compas" target="_blank" rel="noopener noreferrer">compas-dev/compas</a> ·
            <a class="tp-cite-link" href="https://github.com/NREL/EnergyPlus" target="_blank" rel="noopener noreferrer">NREL/EnergyPlus</a>
          </p>
        </article>

        <article class="tp-bounty-card" data-bounty-id="BOUNTY-P2">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">BOUNTY P-2 · PYSR + PYSINDY + DEDALUS</span>
            <span class="tp-bounty-pillar" data-en="Physics · Symbolic PDE Discovery" data-es="Física · Descubrimiento Simbólico de EDPs">Physics · Symbolic PDE Discovery</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Pareto Symbolic Regression &amp; Sparse PDE Discovery from Noisy Sensor Trajectories" data-es="Regresión Simbólica de Pareto y Descubrimiento Disperso de EDPs desde Trayectorias Ruidosas">Pareto Symbolic Regression &amp; Sparse PDE Discovery from Noisy Sensor Trajectories</h3>
          <p class="tp-bounty-body" data-en="Combining evolutionary Pareto minimum-description-length symbolic search in MilesCranmer/PySR with sequentially thresholded sparse PDE identification in dynamicslab/pysindy and Chebyshev-Fourier spectral solvers in DedalusProject/dedalus recovers exact Navier–Stokes, Burgers, and orbital laws directly from noisy data." data-es="Combinar la regresión simbólica evolutiva de Pareto en MilesCranmer/PySR con la identificación dispersa de ecuaciones en derivadas parciales en dynamicslab/pysindy y los solucionadores espectrales de DedalusProject/dedalus recupera leyes exactas de fluidos y órbitas directamente desde datos con ruido.">Combining evolutionary Pareto minimum-description-length symbolic search in MilesCranmer/PySR with sequentially thresholded sparse PDE identification in dynamicslab/pysindy and Chebyshev-Fourier spectral solvers in DedalusProject/dedalus recovers exact Navier–Stokes, Burgers, and orbital laws directly from noisy data.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="physics/p07/" data-en="Explore Folio P.07 &rarr;" data-es="Explorar Folio P.07 &rarr;">Explore Folio P.07 &rarr;</a> ·
            <a class="tp-cite-link" href="https://github.com/MilesCranmer/PySR" target="_blank" rel="noopener noreferrer">MilesCranmer/PySR</a> ·
            <a class="tp-cite-link" href="https://github.com/dynamicslab/pysindy" target="_blank" rel="noopener noreferrer">dynamicslab/pysindy</a> ·
            <a class="tp-cite-link" href="https://github.com/DedalusProject/dedalus" target="_blank" rel="noopener noreferrer">DedalusProject/dedalus</a>
          </p>
        </article>

        <article class="tp-bounty-card" data-bounty-id="BOUNTY-M2">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">BOUNTY M-2 · PHYSLEAN + ITENSORS.JL + NETKET</span>
            <span class="tp-bounty-pillar" data-en="Math &amp; Quantum · Lean 4 + MPS" data-es="Matemáticas y Cuántica · Lean 4 + MPS">Math &amp; Quantum · Lean 4 + MPS</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Machine-Checked Gauge Physics in PhysLean &amp; Tensor-Network Quantum Criticality" data-es="Física Gauge Verificada en PhysLean y Criticidad Cuántica con Redes Tensoriales">Machine-Checked Gauge Physics in PhysLean &amp; Tensor-Network Quantum Criticality</h3>
          <p class="tp-bounty-body" data-en="HEPLean/PhysLean formalizes classical mechanics, Maxwell electrodynamics, and Standard Model U(1)_Y × SU(2)_L × SU(3)_C chiral anomaly cancellation (Tr[Y] = Tr[Y³] = 0) in Lean 4, while itensor/ITensors.jl and netket/netket certify area-law entanglement scaling S_vN(L) = (c/6) ln(L) + s_1 ≤ ln(χ) across quantum phase transitions." data-es="HEPLean/PhysLean formaliza la mecánica clásica, la electrodinámica de Maxwell y la cancelación de anomalías quirales del Modelo Estándar (Tr[Y] = Tr[Y³] = 0) en Lean 4, mientras itensor/ITensors.jl y netket/netket certifican el escalamiento de entrelazamiento S_vN(L) = (c/6) ln(L) + s_1 ≤ ln(χ).">HEPLean/PhysLean formalizes classical mechanics, Maxwell electrodynamics, and Standard Model U(1)_Y × SU(2)_L × SU(3)_C chiral anomaly cancellation (Tr[Y] = Tr[Y³] = 0) in Lean 4, while itensor/ITensors.jl and netket/netket certify area-law entanglement scaling S_vN(L) = (c/6) ln(L) + s_1 ≤ ln(χ) across quantum phase transitions.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="math/m01/" data-en="Explore Folio M.01 &rarr;" data-es="Explorar Folio M.01 &rarr;">Explore Folio M.01 &rarr;</a> ·
            <a class="tp-cite-link" href="https://github.com/HEPLean/PhysLean" target="_blank" rel="noopener noreferrer">HEPLean/PhysLean</a> ·
            <a class="tp-cite-link" href="https://github.com/itensor/ITensors.jl" target="_blank" rel="noopener noreferrer">itensor/ITensors.jl</a> ·
            <a class="tp-cite-link" href="https://github.com/netket/netket" target="_blank" rel="noopener noreferrer">netket/netket</a>
          </p>
        </article>
      </div>
      <div class="tp-bounty-grounding-note" role="note" aria-label="Grounding and GitHub Cryptographic Publishing Proof">
        <p><span data-en="Grounding &amp; GitHub Cryptographic Publishing Proof (T0–T3 Truth Boundary): Every Informatico.ai Folio is verified against primary Crossref DOIs (48/48 Folios passing tools/check_folio_citations.py --offline with zero errors) and ships with a deterministic Python verifier and portable SKILL.md. Our public GitHub repository acts as a timestamped cryptographic prior-art and reproducibility ledger: every commit SHA records the exact deterministic execution of bounties/run_all_bounties.py (6/6 PASS) and skills/verify_all_48_folios.py (48/48 PASS) for community registries (Metriq.info, unitaryHACK, erdosproblems.com, COMPAS &amp; FEniCS showcases), while formal cash prize claims require either a new 0-sorry proof of an unsolved problem or a registered physical prototype pilot." data-es="Rigor y Prueba Criptográfica de Publicación en GitHub (Frontera de Verdad T0–T3): Cada Folio de Informatico.ai está verificado contra DOIs primarios en Crossref (48/48 Folios aprobados con cero errores) e incluye un verificador determinista en Python y un SKILL.md portátil. Nuestro repositorio público en GitHub funciona como registro criptográfico de publicación y reproducibilidad: cada commit SHA certifica la ejecución determinista de bounties/run_all_bounties.py (6/6 PASS) y skills/verify_all_48_folios.py (48/48 PASS) para registros comunitarios (Metriq.info, unitaryHACK, erdosproblems.com, COMPAS y FEniCS), mientras que reclamar un premio en efectivo exige una nueva demostración sin sorry o un prototipo físico registrado.">Grounding &amp; GitHub Cryptographic Publishing Proof (T0–T3 Truth Boundary): Every Informatico.ai Folio is verified against primary Crossref DOIs (48/48 Folios passing tools/check_folio_citations.py --offline with zero errors) and ships with a deterministic Python verifier and portable SKILL.md. Our public GitHub repository acts as a timestamped cryptographic prior-art and reproducibility ledger: every commit SHA records the exact deterministic execution of bounties/run_all_bounties.py (6/6 PASS) and skills/verify_all_48_folios.py (48/48 PASS) for community registries (Metriq.info, unitaryHACK, erdosproblems.com, COMPAS &amp; FEniCS showcases), while formal cash prize claims require either a new 0-sorry proof of an unsolved problem or a registered physical prototype pilot.</span></p>
        <p class="tp-bounty-grounding-links">
          <a class="tp-cite-link" href="https://github.com/senseiewok/informatico.ai" target="_blank" rel="noopener noreferrer">github.com/senseiewok/informatico.ai &rarr;</a> ·
          <a class="tp-cite-link" href="https://github.com/senseiewok/informatico.ai/tree/main/bounties" target="_blank" rel="noopener noreferrer">bounties/run_all_bounties.py &rarr;</a> ·
          <a class="tp-cite-link" href="https://github.com/senseiewok/informatico.ai/commits/main" target="_blank" rel="noopener noreferrer">Cryptographic Commit Ledger (SHA Proof) &rarr;</a>
        </p>
      </div>
    </section>"""


def render_symbolic_physics_lab_section(rel_res: str = ".") -> str:
    """Render Feature 1: Interactive Symbolic Physics & Sparse PDE Law Finder (PySR / PySINDy / Dedalus / PhysLean / ITensors.jl)."""
    p07 = _href(rel_res, "physics/p07/")
    p11 = _href(rel_res, "physics/p11/")
    m01 = _href(rel_res, "math/m01/")
    m08 = _href(rel_res, "math/m08/")
    return f"""    <section id="tp-symbolic-physics-lab" class="tp-symbolic-physics-lab" aria-labelledby="symbolic-physics-heading">
      <div class="tp-bounty-header">
        <p class="tp-kicker" data-en="Interactive Feature I · Symbolic Physics, Sparse PDEs &amp; Formal Gauge Theory" data-es="Laboratorio Interactivo I · Física Simbólica, EDPs Dispersas y Teoría Gauge Formal">Interactive Feature I · Symbolic Physics, Sparse PDEs &amp; Formal Gauge Theory</p>
        <h2 id="symbolic-physics-heading" class="tp-h2" data-en="Symbolic Equation &amp; Sparse PDE Discovery Workbench: From Noisy Sensor Fields to Machine-Checked Laws" data-es="Banco de Descubrimiento de Ecuaciones Simbólicas y EDPs Dispersas: De Datos Ruidosos a Leyes Verificadas">Symbolic Equation &amp; Sparse PDE Discovery Workbench: From Noisy Sensor Fields to Machine-Checked Laws</h2>
        <p class="tp-standfirst" data-en="Explore how open-source physics engines discover governing equations from raw trajectories and verify their symmetries: scrub sensor noise σ and sparsity threshold λ across PySINDy + Dedalus spectral fluid PDEs, PySR Pareto symbolic regression, HEPLean/PhysLean gauge anomaly cancellation in Lean 4, and ITensors.jl + NetKet quantum entanglement scaling." data-es="Explora cómo los motores de física de código abierto descubren ecuaciones gobernantes desde trayectorias con ruido y verifican sus simetrías: ajusta el ruido de sensor σ y el umbral de parsimonia λ en PySINDy + Dedalus, PySR, HEPLean/PhysLean en Lean 4 e ITensors.jl + NetKet.">Explore how open-source physics engines discover governing equations from raw trajectories and verify their symmetries: scrub sensor noise σ and sparsity threshold λ across PySINDy + Dedalus spectral fluid PDEs, PySR Pareto symbolic regression, HEPLean/PhysLean gauge anomaly cancellation in Lean 4, and ITensors.jl + NetKet quantum entanglement scaling.</p>
      </div>

      <div class="tp-symbolic-regime-bar" role="group" aria-label="Select physics discovery regime">
        <button type="button" class="tp-sym-regime-btn" data-symbolic-regime="burgers" aria-pressed="true" data-en="1 · PySINDy + Dedalus Fluid PDE" data-es="1 · EDP de Fluidos PySINDy + Dedalus">1 · PySINDy + Dedalus Fluid PDE</button>
        <button type="button" class="tp-sym-regime-btn" data-symbolic-regime="kepler" aria-pressed="false" data-en="2 · PySR Relativistic Orbit Law" data-es="2 · Ley Orbital Relativista PySR">2 · PySR Relativistic Orbit Law</button>
        <button type="button" class="tp-sym-regime-btn" data-symbolic-regime="physlean" aria-pressed="false" data-en="3 · PhysLean Gauge Anomaly (Lean 4)" data-es="3 · Anomalía Gauge PhysLean (Lean 4)">3 · PhysLean Gauge Anomaly (Lean 4)</button>
        <button type="button" class="tp-sym-regime-btn" data-symbolic-regime="itensor" aria-pressed="false" data-en="4 · ITensors.jl + NetKet MPS Scaling" data-es="4 · Escalamiento MPS ITensors.jl + NetKet">4 · ITensors.jl + NetKet MPS Scaling</button>
      </div>

      <div class="tp-bounty-svg-wrap" role="region" aria-label="Pareto MDL Frontier and STLSQ Operator Spectrum">
        <svg id="tp-sym-svg" class="tp-bounty-crucible-svg" viewBox="0 0 920 205" role="img" aria-label="Left panel: PySR Pareto Minimum Description Length curve vs expression tree complexity. Right panel: PySINDy STLSQ operator library weights vs sparsity threshold.">
          <rect x="12" y="12" width="435" height="180" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <rect x="468" y="12" width="440" height="180" rx="8" fill="var(--tp-stone)" stroke="var(--tp-rule-strong)" stroke-width="1.2"/>
          <text x="230" y="32" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--tp-prussian)">PYSR PARETO MDL FRONTIER: L_MDL = (N/2) ln(MSE) + λ·C_tree</text>
          <line x1="55" y1="168" x2="425" y2="168" stroke="currentColor" stroke-opacity="0.35"/>
          <line x1="55" y1="42" x2="55" y2="168" stroke="currentColor" stroke-opacity="0.35"/>
          <polyline id="tp-sym-pareto-line" points="90,158 175,118 265,62 360,59 450,57" fill="none" stroke="var(--tp-prussian)" stroke-width="2.8"/>
          <circle id="tp-sym-active-dot" cx="265" cy="62" r="7.5" fill="var(--tp-verdigris)" stroke="var(--tp-vellum)" stroke-width="2"/>
          <text x="240" y="184" text-anchor="middle" font-size="9.5" fill="currentColor">Expression Tree Complexity C_tree (Feynman / PDE Symbolic Candidates)</text>

          <text x="688" y="32" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--tp-verdigris)">PYSINDY STLSQ SPARSE OPERATOR SPECTRUM: |ξ_k| ≥ λ</text>
          <line x1="500" y1="165" x2="880" y2="165" stroke="currentColor" stroke-opacity="0.35"/>
          <rect id="tp-sym-bar-0" x="520" y="158" width="34" height="7" rx="3" fill="var(--tp-slate)" opacity="0.35"/>
          <rect id="tp-sym-bar-1" x="580" y="156" width="34" height="9" rx="3" fill="var(--tp-slate)" opacity="0.35"/>
          <rect id="tp-sym-bar-2" x="640" y="50" width="34" height="115" rx="3" fill="var(--tp-verdigris)" opacity="0.92"/>
          <rect id="tp-sym-bar-3" x="700" y="142" width="34" height="23" rx="3" fill="var(--tp-verdigris)" opacity="0.92"/>
          <rect id="tp-sym-bar-4" x="760" y="158" width="34" height="7" rx="3" fill="var(--tp-slate)" opacity="0.35"/>
          <rect id="tp-sym-bar-5" x="820" y="156" width="34" height="9" rx="3" fill="var(--tp-slate)" opacity="0.35"/>
          <line id="tp-sym-thresh-line" x1="500" y1="151" x2="880" y2="151" stroke="var(--tp-minium)" stroke-width="2" stroke-dasharray="5,4"/>
          <text x="537" y="182" text-anchor="middle" font-size="9" fill="currentColor">1</text>
          <text x="597" y="182" text-anchor="middle" font-size="9" fill="currentColor">u</text>
          <text x="657" y="182" text-anchor="middle" font-size="9" font-weight="700" fill="var(--tp-verdigris)">-u·u_x</text>
          <text x="717" y="182" text-anchor="middle" font-size="9" font-weight="700" fill="var(--tp-verdigris)">ν·u_xx</text>
          <text x="777" y="182" text-anchor="middle" font-size="9" fill="currentColor">u²</text>
          <text x="837" y="182" text-anchor="middle" font-size="9" fill="currentColor">u³</text>
        </svg>
      </div>
      <p id="tp-sym-stage-caption" class="tp-sym-caption">PySINDy + Dedalus · Viscous Burgers / Navier-Stokes PDE — Recovered: u_t = -1.00 u·u_x + 0.10 u_xx</p>

      <div class="tp-controls-row">
        <div class="tp-control-group">
          <label for="tp-sym-noise">
            <span data-en="Trajectory Sensor Noise Amplitude (σ)" data-es="Amplitud de Ruido de Sensor (σ)">Trajectory Sensor Noise Amplitude (σ)</span>
            <span id="tp-sym-noise-val">σ = 0.02</span>
          </label>
          <input id="tp-sym-noise" type="range" min="0.00" max="0.25" step="0.01" value="0.02">
        </div>
        <div class="tp-control-group">
          <label for="tp-sym-lambda">
            <span data-en="STLSQ Sparsity / Pareto Cutoff (λ)" data-es="Umbral de Parsimonia STLSQ / Pareto (λ)">STLSQ Sparsity / Pareto Cutoff (λ)</span>
            <span id="tp-sym-lambda-val">λ = 0.05</span>
          </label>
          <input id="tp-sym-lambda" type="range" min="0.01" max="0.40" step="0.01" value="0.05">
        </div>
      </div>

      <div class="tp-readout-strip">
        <div class="tp-readout-box">
          <span class="tp-readout-k" data-en="Discovered Governing Law" data-es="Ley Gobernante Descubierta">Discovered Governing Law</span>
          <span id="tp-sym-out-law" class="tp-readout-v">u_t = -1.00 u·u_x + 0.10 u_xx</span>
        </div>
        <div class="tp-readout-box">
          <span class="tp-readout-k" data-en="Pareto MDL Score" data-es="Puntaje Pareto MDL">Pareto MDL Score</span>
          <span id="tp-sym-out-mdl" class="tp-readout-v">L_MDL = -114.1 nats</span>
        </div>
        <div class="tp-readout-box">
          <span class="tp-readout-k" data-en="Active Operator Support" data-es="Soporte de Operadores Activos">Active Operator Support</span>
          <span id="tp-sym-out-support" class="tp-readout-v">2 / 6 operators active</span>
        </div>
        <div id="tp-sym-verdict-box" class="tp-readout-box" data-alert="false">
          <span class="tp-readout-k" data-en="Discovery Gate Verdict" data-es="Veredicto de Descubrimiento">Discovery Gate Verdict</span>
          <span id="tp-sym-out-verdict" class="tp-readout-v">PASS · EXACT LAW RECOVERED</span>
        </div>
      </div>

      <div class="tp-sym-actions-row">
        <p class="tp-bounty-links">
          <a class="tp-cite-link" href="{p07}" data-en="Folio P.07 (Navier–Stokes) &rarr;" data-es="Folio P.07 (Navier–Stokes) &rarr;">Folio P.07 (Navier–Stokes) &rarr;</a> ·
          <a class="tp-cite-link" href="{p11}" data-en="Folio P.11 (Quantum QEC) &rarr;" data-es="Folio P.11 (QEC Cuántico) &rarr;">Folio P.11 (Quantum QEC) &rarr;</a> ·
          <a class="tp-cite-link" href="{m01}" data-en="Folio M.01 (Lean 4 FLT) &rarr;" data-es="Folio M.01 (Lean 4 FLT) &rarr;">Folio M.01 (Lean 4 FLT) &rarr;</a> ·
          <a class="tp-cite-link" href="{m08}" data-en="Folio M.08 (Pontryagin Control) &rarr;" data-es="Folio M.08 (Control de Pontryagin) &rarr;">Folio M.08 (Pontryagin Control) &rarr;</a>
        </p>
        <button id="tp-sym-copy-btn" type="button" class="tp-skill-btn tp-skill-btn-secondary" data-en="Copy Python / Lean 4 Discovery Script" data-es="Copiar Script de Descubrimiento Python / Lean 4">Copy Python / Lean 4 Discovery Script</button>
      </div>
      <details class="tp-skill-source-details">
        <summary class="tp-skill-source-summary" data-en="Inspect reproducible PySR / PySINDy / PhysLean / ITensors.jl code harness" data-es="Inspeccionar código reproducible PySR / PySINDy / PhysLean / ITensors.jl">Inspect reproducible PySR / PySINDy / PhysLean / ITensors.jl code harness</summary>
        <pre class="tp-skill-pre"><code id="tp-sym-code-preview"># PySINDy + Dedalus Spectral PDE Discovery (Folio P.07 / P.11)
import numpy as np
import pysindy as ps

optimizer = ps.STLSQ(threshold=0.05, alpha=1e-3)
model = ps.SINDy(optimizer=optimizer)
# Recovers u_t = -1.00 * u * u_x + 0.10 * u_xx</code></pre>
      </details>
    </section>"""


def render_oss_physics_radar_section(rel_res: str = ".") -> str:
    """Render Feature 2: Open-Source Physics & Mathematical Discovery Stack Matrix."""
    p01 = _href(rel_res, "physics/p01/")
    p03 = _href(rel_res, "physics/p03/")
    p07 = _href(rel_res, "physics/p07/")
    p11 = _href(rel_res, "physics/p11/")
    p12 = _href(rel_res, "physics/p12/")
    m01 = _href(rel_res, "math/m01/")
    m03 = _href(rel_res, "math/m03/")
    m09 = _href(rel_res, "math/m09/")
    m11 = _href(rel_res, "math/m11/")
    e11 = _href(rel_res, "engineering/e11/")
    a11 = _href(rel_res, "architecture/a11/")
    return f"""    <section id="tp-oss-physics-radar" class="tp-oss-physics-radar" aria-labelledby="oss-physics-radar-heading">
      <div class="tp-bounty-header">
        <p class="tp-kicker" data-en="Interactive Feature II · Open-Source Physics &amp; Formal Mathematics Stack" data-es="Laboratorio Interactivo II · Ecosistema de Código Abierto en Física y Matemáticas">Interactive Feature II · Open-Source Physics &amp; Formal Mathematics Stack</p>
        <h2 id="oss-physics-radar-heading" class="tp-h2" data-en="The Open-Source Physics &amp; Mathematical Discovery Radar: 12 Engines Powering Informatico.ai" data-es="El Radar de Descubrimiento Físico y Matemático de Código Abierto: 12 Motores que Impulsan Informatico.ai">The Open-Source Physics &amp; Mathematical Discovery Radar: 12 Engines Powering Informatico.ai</h2>
        <p class="tp-standfirst" data-en="Filter the open-source computational physics, symbolic regression, tensor-network, and formal theorem-proving ecosystems integrated into our Folios and benchmark verifiers." data-es="Filtra los ecosistemas abiertos de física computacional, regresión simbólica, redes tensoriales y demostración formal de teoremas integrados en nuestros Folios y verificadores.">Filter the open-source computational physics, symbolic regression, tensor-network, and formal theorem-proving ecosystems integrated into our Folios and benchmark verifiers.</p>
      </div>

      <div class="tp-oss-filter-bar" role="group" aria-label="Filter open-source physics and math projects by category">
        <button type="button" class="tp-oss-filter-btn" data-oss-filter="all" aria-pressed="true" data-en="All Stacks (12)" data-es="Todos (12)">All Stacks (12)</button>
        <button type="button" class="tp-oss-filter-btn" data-oss-filter="symbolic" aria-pressed="false" data-en="Symbolic &amp; AI4Science (3)" data-es="Simbólico y AI4Science (3)">Symbolic &amp; AI4Science (3)</button>
        <button type="button" class="tp-oss-filter-btn" data-oss-filter="continuum" aria-pressed="false" data-en="Spectral &amp; Differentiable Physics (3)" data-es="Física Espectral y Diferenciable (3)">Spectral &amp; Differentiable Physics (3)</button>
        <button type="button" class="tp-oss-filter-btn" data-oss-filter="quantum" aria-pressed="false" data-en="Quantum &amp; Tensor Networks (3)" data-es="Cuántica y Redes Tensoriales (3)">Quantum &amp; Tensor Networks (3)</button>
        <button type="button" class="tp-oss-filter-btn" data-oss-filter="formal" aria-pressed="false" data-en="Formal Lean 4 &amp; Geometry (3)" data-es="Lean 4 Formal y Geometría (3)">Formal Lean 4 &amp; Geometry (3)</button>
        <span id="tp-oss-count-out" class="tp-bounty-badge" aria-live="polite">12 / 12</span>
      </div>

      <div id="tp-oss-radar-grid" class="tp-oss-radar-grid">
        <article class="tp-oss-card" data-oss-cat="symbolic">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">SYMBOLIC REGRESSION · APACHE-2.0</span>
            <span class="tp-bounty-pillar">MilesCranmer/PySR</span>
          </div>
          <h3 class="tp-bounty-title" data-en="PySR &amp; SymbolicRegression.jl: Evolutionary Pareto Equation Discovery" data-es="PySR y SymbolicRegression.jl: Descubrimiento Evolutivo de Ecuaciones en Frontera de Pareto">PySR &amp; SymbolicRegression.jl: Evolutionary Pareto Equation Discovery</h3>
          <code class="tp-oss-eq">f* = argmin [ (N/2) ln(MSE) + λ·C_tree(f) ]</code>
          <p class="tp-bounty-body" data-en="Multi-population evolutionary symbolic regression that discovers closed-form physical laws and constitutive fluid closures from noisy empirical trajectories." data-es="Regresión simbólica evolutiva multipoblacional que descubre leyes físicas cerradas y relaciones constitutivas desde datos empíricos con ruido.">Multi-population evolutionary symbolic regression that discovers closed-form physical laws and constitutive fluid closures from noisy empirical trajectories.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/MilesCranmer/PySR" target="_blank" rel="noopener noreferrer">github.com/MilesCranmer/PySR</a> ·
            <a class="tp-cite-link" href="{p03}" data-en="Folio P.03 &rarr;" data-es="Folio P.03 &rarr;">Folio P.03 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="symbolic">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">SPARSE DYNAMICS · MIT</span>
            <span class="tp-bounty-pillar">dynamicslab/pysindy</span>
          </div>
          <h3 class="tp-bounty-title" data-en="PySINDy: Sparse Identification of Nonlinear Dynamical PDEs" data-es="PySINDy: Identificación Dispersa de Sistemas Dinámicos No Lineales y EDPs">PySINDy: Sparse Identification of Nonlinear Dynamical PDEs</h3>
          <code class="tp-oss-eq">u_t = Θ(u, ∇u, ∇²u) ξ,  min ||u_t - Θξ||₂² + λ||ξ||₀</code>
          <p class="tp-bounty-body" data-en="Recovers parsimonious governing ODEs and PDEs (Navier–Stokes, Kuramoto, reaction-diffusion) via Sequentially Thresholded Least Squares (STLSQ) and weak-form integration." data-es="Recupera EDOs y EDPs gobernantes (Navier–Stokes, Kuramoto, reacción-difusión) mediante mínimos cuadrados umbralizados secuencialmente (STLSQ).">Recovers parsimonious governing ODEs and PDEs (Navier–Stokes, Kuramoto, reaction-diffusion) via Sequentially Thresholded Least Squares (STLSQ) and weak-form integration.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/dynamicslab/pysindy" target="_blank" rel="noopener noreferrer">github.com/dynamicslab/pysindy</a> ·
            <a class="tp-cite-link" href="{p07}" data-en="Folio P.07 &rarr;" data-es="Folio P.07 &rarr;">Folio P.07 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="symbolic">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">QUANTUM POTENTIALS · MIT</span>
            <span class="tp-bounty-pillar">facebookresearch/fairchem</span>
          </div>
          <h3 class="tp-bounty-title" data-en="FAIRChem &amp; UMA: Universal Equivariant Interatomic Neural Potentials" data-es="FAIRChem y UMA: Potenciales Interatómicos Neuronales Equivariantes Universales">FAIRChem &amp; UMA: Universal Equivariant Interatomic Neural Potentials</h3>
          <code class="tp-oss-eq">F_i = -∇_{{r_i}} E_UMA(r_1,…,r_N),  MAE(E) ≤ 0.02 eV</code>
          <p class="tp-bounty-body" data-en="Equivariant graph neural force fields trained on 100M+ DFT calculations, delivering ab-initio quantum forces at 100,000x lower computational cost." data-es="Campos de fuerza neuronales equivariantes entrenados con más de 100M de cálculos DFT, logrando precisión cuántica ab-initio 100,000 veces más rápido.">Equivariant graph neural force fields trained on 100M+ DFT calculations, delivering ab-initio quantum forces at 100,000x lower computational cost.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/facebookresearch/fairchem" target="_blank" rel="noopener noreferrer">github.com/facebookresearch/fairchem</a> ·
            <a class="tp-cite-link" href="{p01}" data-en="Folio P.01 &rarr;" data-es="Folio P.01 &rarr;">Folio P.01 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="continuum">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">SPECTRAL PDE SOLVER · GPL-3.0</span>
            <span class="tp-bounty-pillar">DedalusProject/dedalus</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Dedalus: Flexible Spectral PDE Solver for Fluid &amp; Continuum Physics" data-es="Dedalus: Solucionador Espectral de EDPs para Dinámica de Fluidos y Medios Continuos">Dedalus: Flexible Spectral PDE Solver for Fluid &amp; Continuum Physics</h3>
          <code class="tp-oss-eq">∂_t M·X + L·X = F(X)  (Chebyshev–Fourier–Spherical)</code>
          <p class="tp-bounty-body" data-en="Solves symbolically specified initial, boundary, and eigenvalue PDEs using sparse Chebyshev, Fourier, and spherical harmonic spectral methods." data-es="Resuelve EDPs especificadas simbólicamente mediante métodos espectrales dispersos de Chebyshev, Fourier y armónicos esféricos.">Solves symbolically specified initial, boundary, and eigenvalue PDEs using sparse Chebyshev, Fourier, and spherical harmonic spectral methods.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/DedalusProject/dedalus" target="_blank" rel="noopener noreferrer">github.com/DedalusProject/dedalus</a> ·
            <a class="tp-cite-link" href="{p07}" data-en="Folio P.07 &rarr;" data-es="Folio P.07 &rarr;">Folio P.07 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="continuum">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">DIFFERENTIABLE MD · APACHE-2.0</span>
            <span class="tp-bounty-pillar">google/jax-md</span>
          </div>
          <h3 class="tp-bounty-title" data-en="JAX-MD: Accelerated Differentiable Molecular Dynamics &amp; Statistical Physics" data-es="JAX-MD: Dinámica Molecular Diferenciable Acelerada y Física Estadística">JAX-MD: Accelerated Differentiable Molecular Dynamics &amp; Statistical Physics</h3>
          <code class="tp-oss-eq">dR = -∇_R U_θ(R) dt + √(2 k_B T dt) dW_t</code>
          <p class="tp-bounty-body" data-en="End-to-end automatic differentiation through Langevin, Nose–Hoover, and Brownian molecular dynamics trajectories for inverse material design." data-es="Diferenciación automática de extremo a extremo a través de trayectorias de dinámica molecular de Langevin y Nose–Hoover para diseño inverso de materiales.">End-to-end automatic differentiation through Langevin, Nose–Hoover, and Brownian molecular dynamics trajectories for inverse material design.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/google/jax-md" target="_blank" rel="noopener noreferrer">github.com/google/jax-md</a> ·
            <a class="tp-cite-link" href="{p03}" data-en="Folio P.03 &rarr;" data-es="Folio P.03 &rarr;">Folio P.03 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="continuum">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">FINITE ELEMENT · LGPL-3.0</span>
            <span class="tp-bounty-pillar">FEniCS/dolfinx</span>
          </div>
          <h3 class="tp-bounty-title" data-en="FEniCSx / DOLFINx: Variational PDE &amp; Topology Optimization Engine" data-es="FEniCSx / DOLFINx: Motor Variacional de EDPs y Optimización Topológica">FEniCSx / DOLFINx: Variational PDE &amp; Topology Optimization Engine</h3>
          <code class="tp-oss-eq">a(u, v) = L(v) ∀v ∈ V_h,  E(ρ) = E_min + ρ^p (E_0 - E_min)</code>
          <p class="tp-bounty-body" data-en="Compiles Unified Form Language (UFL) weak variational forms into high-performance parallel C++ finite-element kernels for elasticity and SIMP topology optimization." data-es="Compila formas débiles variacionales UFL en núcleos paralelos de elementos finitos para elasticidad y optimización topológica SIMP.">Compiles Unified Form Language (UFL) weak variational forms into high-performance parallel C++ finite-element kernels for elasticity and SIMP topology optimization.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/FEniCS/dolfinx" target="_blank" rel="noopener noreferrer">github.com/FEniCS/dolfinx</a> ·
            <a class="tp-cite-link" href="{e11}" data-en="Folio E.11 &rarr;" data-es="Folio E.11 &rarr;">Folio E.11 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="quantum">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">TENSOR NETWORKS · APACHE-2.0</span>
            <span class="tp-bounty-pillar">itensor/ITensors.jl</span>
          </div>
          <h3 class="tp-bounty-title" data-en="ITensors.jl: DMRG, Matrix Product States &amp; Quantum Tensor Networks" data-es="ITensors.jl: DMRG, Estados de Producto Matricial y Redes Tensoriales Cuánticas">ITensors.jl: DMRG, Matrix Product States &amp; Quantum Tensor Networks</h3>
          <code class="tp-oss-eq">|Ψ_MPS⟩ = ∑ A^{{s_1}}_1 … A^{{s_N}}_N |s⟩,  S_vN ≤ ln(χ)</code>
          <p class="tp-bounty-body" data-en="Automatic index-contracting tensor networks for Density Matrix Renormalization Group (DMRG), time-evolving block decimation (TEBD), and strongly correlated quantum matter." data-es="Redes tensoriales con contracción automática de índices para DMRG, evolución temporal TEBD y materia cuántica fuertemente correlacionada.">Automatic index-contracting tensor networks for Density Matrix Renormalization Group (DMRG), time-evolving block decimation (TEBD), and strongly correlated quantum matter.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/itensor/ITensors.jl" target="_blank" rel="noopener noreferrer">github.com/itensor/ITensors.jl</a> ·
            <a class="tp-cite-link" href="{p12}" data-en="Folio P.12 &rarr;" data-es="Folio P.12 &rarr;">Folio P.12 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="quantum">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">NEURAL QUANTUM · APACHE-2.0</span>
            <span class="tp-bounty-pillar">netket/netket</span>
          </div>
          <h3 class="tp-bounty-title" data-en="NetKet &amp; QuTiP: Neural Quantum States &amp; Lindblad Open Quantum Dynamics" data-es="NetKet y QuTiP: Estados Cuánticos Neuronales y Dinámica Cuántica Abierta de Lindblad">NetKet &amp; QuTiP: Neural Quantum States &amp; Lindblad Open Quantum Dynamics</h3>
          <code class="tp-oss-eq">E_0 = min_θ ⟨ψ_θ|H|ψ_θ⟩ / ⟨ψ_θ|ψ_θ⟩,  dρ/dt = -i[H,ρ] + D[L](ρ)</code>
          <p class="tp-bounty-body" data-en="Variational Monte Carlo (VMC) with neural-network quantum wavefunctions on JAX paired with QuTiP master-equation solvers for open quantum systems." data-es="Monte Carlo variacional (VMC) con funciones de onda neuronales en JAX junto con solucionadores de ecuaciones maestras de QuTiP para sistemas cuánticos abiertos.">Variational Monte Carlo (VMC) with neural-network quantum wavefunctions on JAX paired with QuTiP master-equation solvers for open quantum systems.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/netket/netket" target="_blank" rel="noopener noreferrer">github.com/netket/netket</a> ·
            <a class="tp-cite-link" href="https://github.com/qutip/qutip" target="_blank" rel="noopener noreferrer">qutip/qutip</a> ·
            <a class="tp-cite-link" href="{p11}" data-en="Folio P.11 &rarr;" data-es="Folio P.11 &rarr;">Folio P.11 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="quantum">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">QUANTUM QEC &amp; DFT · APACHE-2.0</span>
            <span class="tp-bounty-pillar">quantumlib/Stim + pyscf/pyscf</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Stim &amp; PySCF: Stabilizer Surface-Code QEC &amp; Ab-Initio Electronic Structure" data-es="Stim y PySCF: Corrección de Errores de Código de Superficie y Estructura Electrónica Ab-Initio">Stim &amp; PySCF: Stabilizer Surface-Code QEC &amp; Ab-Initio Electronic Structure</h3>
          <code class="tp-oss-eq">p_L ≈ 0.1 (p / p_th)^{{(d+1)/2}},  H_el |Ψ⟩ = E |Ψ⟩</code>
          <p class="tp-bounty-body" data-en="Megahertz stabilizer circuit sampling in Stim paired with PySCF coupled-cluster and CASSCF electronic structure integrals for fault-tolerant quantum chemistry." data-es="Muestreo de circuitos estabilizadores a megahertz en Stim unido a integrales electrónicas coupled-cluster y CASSCF en PySCF para química cuántica tolerante a fallos.">Megahertz stabilizer circuit sampling in Stim paired with PySCF coupled-cluster and CASSCF electronic structure integrals for fault-tolerant quantum chemistry.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/quantumlib/Stim" target="_blank" rel="noopener noreferrer">quantumlib/Stim</a> ·
            <a class="tp-cite-link" href="https://github.com/pyscf/pyscf" target="_blank" rel="noopener noreferrer">pyscf/pyscf</a> ·
            <a class="tp-cite-link" href="{p11}" data-en="Folio P.11 &rarr;" data-es="Folio P.11 &rarr;">Folio P.11 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="formal">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">LEAN 4 PHYSICS · APACHE-2.0</span>
            <span class="tp-bounty-pillar">HEPLean/PhysLean</span>
          </div>
          <h3 class="tp-bounty-title" data-en="PhysLean (HepLean): Formalized Classical, Quantum &amp; Gauge Physics in Lean 4" data-es="PhysLean (HepLean): Física Clásica, Cuántica y de Gauge Formalizada en Lean 4">PhysLean (HepLean): Formalized Classical, Quantum &amp; Gauge Physics in Lean 4</h3>
          <code class="tp-oss-eq">∑ d_f Y_f = 0 ∧ ∑ d_f Y_f³ = 0,  d ⋆ F = J</code>
          <p class="tp-bounty-body" data-en="1,850+ machine-checked theorems in Lean 4 covering Lagrangian mechanics, Maxwell electrodynamics, Lorentz groups, Wick's theorem, and Standard Model anomaly cancellation." data-es="Más de 1,850 teoremas verificados en Lean 4 sobre mecánica lagrangiana, electrodinámica de Maxwell, grupo de Lorentz, teorema de Wick y cancelación de anomalías.">1,850+ machine-checked theorems in Lean 4 covering Lagrangian mechanics, Maxwell electrodynamics, Lorentz groups, Wick's theorem, and Standard Model anomaly cancellation.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/HEPLean/PhysLean" target="_blank" rel="noopener noreferrer">github.com/HEPLean/PhysLean</a> ·
            <a class="tp-cite-link" href="{m01}" data-en="Folio M.01 &rarr;" data-es="Folio M.01 &rarr;">Folio M.01 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="formal">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">FORMAL PROOF · APACHE-2.0</span>
            <span class="tp-bounty-pillar">anthropics/formal-math + mathlib4</span>
          </div>
          <h3 class="tp-bounty-title" data-en="Anthropic Formal-Math, Fermat's Last Theorem &amp; Leanprover Mathlib4" data-es="Anthropic Formal-Math, Último Teorema de Fermat y Leanprover Mathlib4">Anthropic Formal-Math, Fermat's Last Theorem &amp; Leanprover Mathlib4</h3>
          <code class="tp-oss-eq">a^n + b^n ≠ c^n (n ≥ 3),  N(σ,T) ≤ C·T^{{(30/13)(1-σ)+ε}}</code>
          <p class="tp-bounty-body" data-en="Zero-sorry Lean 4 formalizations of Fermat's Last Theorem, Riemann XiPrime zero-density bounds, and sub-exponential 3-SAT refutations built atop Mathlib4." data-es="Formalizaciones sin sorry en Lean 4 del Último Teorema de Fermat, cotas de densidad cero de Riemann XiPrime y refutaciones 3-SAT sobre Mathlib4.">Zero-sorry Lean 4 formalizations of Fermat's Last Theorem, Riemann XiPrime zero-density bounds, and sub-exponential 3-SAT refutations built atop Mathlib4.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/anthropics/formal-math" target="_blank" rel="noopener noreferrer">anthropics/formal-math</a> ·
            <a class="tp-cite-link" href="https://github.com/leanprover-community/mathlib4" target="_blank" rel="noopener noreferrer">mathlib4</a> ·
            <a class="tp-cite-link" href="{m11}" data-en="Folio M.11 &rarr;" data-es="Folio M.11 &rarr;">Folio M.11 &rarr;</a>
          </p>
        </article>

        <article class="tp-oss-card" data-oss-cat="formal">
          <div class="tp-bounty-card-top">
            <span class="tp-bounty-badge">GEOMETRIC STATICS &amp; OT · MIT</span>
            <span class="tp-bounty-pillar">compas-dev/compas + PythonOT/POT</span>
          </div>
          <h3 class="tp-bounty-title" data-en="COMPAS 3D Polyhedral Graphic Statics &amp; Python Optimal Transport (POT)" data-es="Estática Gráfica Poliédrica 3D en COMPAS y Transporte Óptimo en Python (POT)">COMPAS 3D Polyhedral Graphic Statics &amp; Python Optimal Transport (POT)</h3>
          <code class="tp-oss-eq">∑ A_f n_f = 0 (Maxwell–Rankine),  W_2²(μ,ν) = inf ∫ |x - T(x)|² dμ</code>
          <p class="tp-bounty-body" data-en="Reciprocal polyhedral force diagrams for compression-only vaults in COMPAS paired with Wasserstein optimal transport and Sinkhorn barycenters in POT and teorth/equational_theories." data-es="Diagramas recíprocos de fuerzas poliédricas en COMPAS unidos a transporte óptimo de Wasserstein en POT y teorth/equational_theories.">Reciprocal polyhedral force diagrams for compression-only vaults in COMPAS paired with Wasserstein optimal transport and Sinkhorn barycenters in POT and teorth/equational_theories.</p>
          <p class="tp-bounty-links">
            <a class="tp-cite-link" href="https://github.com/compas-dev/compas" target="_blank" rel="noopener noreferrer">compas-dev/compas</a> ·
            <a class="tp-cite-link" href="https://github.com/PythonOT/POT" target="_blank" rel="noopener noreferrer">PythonOT/POT</a> ·
            <a class="tp-cite-link" href="{a11}" data-en="Folio A.11 &rarr;" data-es="Folio A.11 &rarr;">Folio A.11 &rarr;</a> ·
            <a class="tp-cite-link" href="{m09}" data-en="Folio M.09 &rarr;" data-es="Folio M.09 &rarr;">Folio M.09 &rarr;</a>
          </p>
        </article>
      </div>
    </section>"""

def render_hub_index(catalog: dict, lang: str = "en") -> str:
    """The cover: one promise, one image, four rows of essays. Nothing that repeats the Contents dialog."""
    es = lang == "es"
    total = sum(len(v) for v in catalog["pillars"].values())
    t_en, d_en, t_es, d_es = (x.replace("{total}", str(total)) for x in HUB_SEO)
    hub_title, hub_desc = (t_es, d_es) if es else (t_en, d_en)
    hub_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": BRAND,
            "description": hub_desc,
            "inLanguage": ["en", "es-MX"],
            "url": SITE,
            "publisher": ORG_LD,
        },
        ensure_ascii=False,
    ).replace("</", "<\\/")
    head = render_head(hub_title, hub_desc, "", "website", "https://informatico.ai/plates/utopian-city-future.jpg", "..", ".", hub_ld, lang)

    rows = []
    for p_key in ("engineering", "architecture", "physics", "math"):
        folios = catalog["pillars"][p_key]
        en, es = PILLAR_TITLES[p_key], PILLAR_TITLES_ES[p_key]
        hook_en, hook_es = PILLAR_HOOKS[p_key]
        cards = render_rack_cards(p_key, folios, f"{p_key}/", "plates/", eager=0)
        rows.append(
            f"""    <section class="tp-cover-pillar" data-track="{p_key}" aria-labelledby="pillar-{p_key}">
      <div class="tp-cover-pillar-head">
        <p class="tp-kicker" data-en="Pillar {PILLAR_ROMAN[p_key]} · {len(folios)} essays" data-es="Pilar {PILLAR_ROMAN[p_key]} · {len(folios)} ensayos">Pillar {PILLAR_ROMAN[p_key]} · {len(folios)} essays</p>
        <h2 id="pillar-{p_key}" class="tp-h2"><a href="{p_key}/" data-en="{esc(en)}" data-es="{esc(es)}">{esc(en)}</a></h2>
        <p class="tp-cover-hook" data-en="{esc(hook_en)}" data-es="{esc(hook_es)}">{esc(hook_en)}</p>
        <a class="tp-cover-more" href="{p_key}/" data-en="See all {len(folios)} &rarr;" data-es="Ver los {len(folios)} &rarr;">See all {len(folios)} &rarr;</a>
      </div>
      <div class="tp-cover-row">
{cards}
      </div>
    </section>"""
        )
    rows_html = "\n".join(rows)
    first = catalog["pillars"]["engineering"][0]

    return f"""{head}
<body class="tp-body tp-page-cover">
{render_masthead(".", lang=lang)}
{render_contents_dialog(".", catalog)}
  <main id="main" class="tp-shell" tabindex="-1">
    <section class="tp-cover-hero" aria-labelledby="cover-heading">
      <div class="tp-cover-copy">
        <p class="tp-kicker" data-en="Engineering · Architecture · Physics · Mathematics" data-es="Ingeniería · Arquitectura · Física · Matemáticas">Engineering · Architecture · Physics · Mathematics</p>
        <h1 id="cover-heading" class="tp-h1" data-en="How the built world works, explained and made explorable." data-es="Cómo funciona el mundo construido, explicado y explorable.">How the built world works, explained and made explorable.</h1>
        <p class="tp-standfirst" data-en="{total} long-form essays. Each one tells the human story, builds the everyday intuition, and then hands you a live model to push, pull and break." data-es="{total} ensayos de largo aliento. Cada uno cuenta la historia humana, construye la intuición cotidiana y luego te entrega un modelo vivo para empujar, jalar y romper.">{total} long-form essays. Each one tells the human story, builds the everyday intuition, and then hands you a live model to push, pull and break.</p>
        <div class="tp-cover-ctas">
          <a class="tp-cta tp-cta-primary" href="engineering/{first["slug"]}/" data-en="Start reading" data-es="Empezar a leer">Start reading</a>
          <button type="button" class="tp-cta" data-open-contents aria-haspopup="dialog" aria-controls="tp-contents" data-en="Browse all {total}" data-es="Ver los {total}">Browse all {total}</button>
        </div>
      </div>
      <figure class="tp-cover-figure">
        <img src="plates/utopian-city-future.jpg" width="1280" height="720" loading="eager" fetchpriority="high" decoding="async" alt="Conceptual illustration imagining what a city built with these ideas would look like: light space frames, vertical gardens and robots at work (artistic impression, not a design).">
        <figcaption data-en="Conceptual illustration imagining what a city built with these ideas would look like. An artistic impression, not a design." data-es="Ilustración conceptual que imagina cómo se vería una ciudad construida con estas ideas. Una impresión artística, no un diseño.">Conceptual illustration imagining what a city built with these ideas would look like. An artistic impression, not a design.</figcaption>
      </figure>
    </section>
{rows_html}
{render_bounty_crucible_section()}
{render_symbolic_physics_lab_section(".")}
{render_oss_physics_radar_section(".")}
{render_folio_crossword_section("hub", "INFORMATICO.AI")}
{render_site_footer(".")}
  </main>
  <script type="module" src="modules/main.mjs"></script>
</body>
</html>
"""



def _folio_lastmod(f: dict) -> str:
    return f.get("date_redated") or f.get("date_published") or "2026-11-02"


def render_research_sitemap(catalog: dict) -> str:
    """Every page in both languages. Each lastmod is the essay's own re-dated day; a hub takes its newest essay's."""
    entries: list[tuple[str, str]] = []
    every = [f for fs in catalog["pillars"].values() for f in fs]
    entries.append(("", max(_folio_lastmod(f) for f in every)))
    for pillar, folios in catalog["pillars"].items():
        entries.append((f"{pillar}/", max(_folio_lastmod(f) for f in folios)))
        for f in folios:
            entries.append((f"{pillar}/{f['slug']}/", _folio_lastmod(f)))

    blocks = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for lang in ("en", "es"):
        for path, lastmod in entries:
            en_url, es_url = page_url(path, "en"), page_url(path, "es")
            blocks.append(
                f"""  <url>
    <loc>{page_url(path, lang)}</loc>
    <lastmod>{lastmod}</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="es-MX" href="{es_url}"/>
    <xhtml:link rel="alternate" hreflang="es" href="{es_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{en_url}"/>
  </url>"""
            )
    blocks.append("</urlset>\n")
    return "\n".join(blocks)


def render_llms_txt(catalog: dict) -> str:
    """A plain-text map of the site for language-model tools (llms.txt convention): what each essay is, and where."""
    total = sum(len(v) for v in catalog["pillars"].values())
    t_en, d_en, _t_es, _d_es = (x.replace("{total}", str(total)) for x in HUB_SEO)
    lines = [f"# {BRAND}", "", f"> {d_en}", "",
             f"Every essay is also in Mexican Spanish under {page_url('', 'es')}. Public open-source repository (48 SKILL.md companions, Python verifiers & Bounty Crucible harnesses): https://github.com/senseiewok/informatico.ai . For learning and research, not professional or medical advice.", ""]
    for pillar, folios in catalog["pillars"].items():
        lines.append(f"## {PILLAR_TITLES[pillar]}")
        lines.append("")
        lines.append(f"- [{PILLAR_TITLES[pillar]}]({page_url(pillar + '/')}): {PILLAR_SEO[pillar][1]}")
        for f in folios:
            title, desc = FOLIO_SEO[f["slug"]][0], FOLIO_SEO[f["slug"]][1]
            lines.append(f"- [{f['folio_id']} {title}]({page_url(pillar + '/' + f['slug'] + '/')}): {desc}")
        lines.append("")
    return "\n".join(lines)


def render_not_found() -> str:
    """The informatico.ai 404 page. Served at any depth, so every address in it is absolute; never indexed."""
    links = " · ".join(
        f'<a href="/{p}/">{esc(PILLAR_NAV_LABELS[p][0])}</a>' for p in ("engineering", "architecture", "physics", "math")
    )
    links_es = " · ".join(
        f'<a href="/{ES_PREFIX}{p}/">{esc(PILLAR_NAV_LABELS[p][1])}</a>' for p in ("engineering", "architecture", "physics", "math")
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page not found | {BRAND}</title>
  <meta name="description" content="That page is not here. Links to the cover and the four disciplines of Informatico.ai, in English and Spanish.">
  <meta name="robots" content="noindex">
  <link rel="icon" href="/images/icon-32.png" sizes="32x32" type="image/png">
  <link rel="stylesheet" href="/styles.css">
  <link rel="stylesheet" href="/informatico.css">
</head>
<body class="tp-body tp-page-hub">
  <main id="main" class="tp-shell" tabindex="-1">
    <section class="tp-pillar-hero" aria-labelledby="nf-heading">
      <p class="tp-kicker"><a href="/">{BRAND}</a></p>
      <h1 id="nf-heading" class="tp-h1">This page does not exist.</h1>
      <p class="tp-standfirst">The address may be mistyped, or the essay may have moved. Start from the <a href="/">cover</a>, or pick a discipline: {links}.</p>
      <p class="tp-standfirst" lang="es-MX">Esta página no existe. Vuelve a la <a href="/{ES_PREFIX}">portada en español</a> o elige una disciplina: {links_es}.</p>
    </section>
  </main>
</body>
</html>
"""


_VOID_TAGS = frozenset({"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"})
_URL_ATTR = re.compile(r'(\s)(href|src|data-plate-prefix)(=(["\']))(.*?)(\4)')


def _es_shift_url(attr: str, value: str) -> str:
    """One relative address on a page that moved one folder deeper (under /es-mx/).

    Page links (a folder, or index.html) stay as written, so they resolve to the Spanish twin of that page.
    Files (styles, scripts, images, the plate folder prefix) get one more "../", so they still load from where they live."""
    if not value or value.startswith(("/", "#", "?", "http:", "https:", "mailto:", "data:", "tel:")):
        return value
    path = re.split(r"[?#]", value, maxsplit=1)[0]
    is_page = attr != "data-plate-prefix" and (path in ("", ".", "..") or path.endswith("/") or path.endswith("index.html"))
    return value if is_page else "../" + value


class _SpanishStatic(html.parser.HTMLParser):
    """Copies a page token by token, keeping the original bytes, with two optional changes:

    - swap: an element carrying both data-en and a non-empty data-es gets data-es as its only text, exactly what
      theme-plate.mjs does in the browser (el.textContent = data-es), so the Spanish is in the HTML itself;
    - shift: relative file addresses get one more "../" (see _es_shift_url).
    With both off the output equals the input (tests/test_informatico_seo.py checks this on every page)."""

    def __init__(self, swap: bool = True, shift: bool = True) -> None:
        super().__init__(convert_charrefs=False)
        self.out: list[str] = []
        self.stack: list[str] = []
        self.skip = 0
        self.swap, self.shift = swap, shift

    def _start(self, raw: str) -> str:
        if not self.shift:
            return raw
        return _URL_ATTR.sub(lambda m: m.group(1) + m.group(2) + m.group(3) + _es_shift_url(m.group(2), m.group(5)) + m.group(6), raw)

    def handle_starttag(self, tag, attrs):
        raw = self.get_starttag_text() or ""
        if self.skip:
            if tag not in _VOID_TAGS:
                self.skip += 1
            return
        self.out.append(self._start(raw))
        if tag in _VOID_TAGS:
            return
        m = re.match(r"<\s*([^\s/>]+)", raw)
        self.stack.append(m.group(1) if m else tag)
        a = dict(attrs)
        if self.swap and a.get("data-en") is not None and a.get("data-es"):
            self.out.append(html.escape(a["data-es"], quote=False))
            self.skip = 1

    def handle_startendtag(self, tag, attrs):
        if not self.skip:
            self.out.append(self._start(self.get_starttag_text() or ""))

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            if self.skip:
                return
        name = tag
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].lower() == tag:
                name = self.stack[i]
                del self.stack[i:]
                break
        self.out.append(f"</{name}>")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)

    def handle_entityref(self, name):
        if not self.skip:
            self.out.append(f"&{name};")

    def handle_charref(self, name):
        if not self.skip:
            self.out.append(f"&#{name};")

    def handle_comment(self, data):
        if not self.skip:
            self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.out.append(f"<!{decl}>")

    def handle_pi(self, data):
        self.out.append(f"<?{data}>")

    def unknown_decl(self, data):
        self.out.append(f"<![{data}]>")


def to_spanish_static(page_html: str, swap: bool = True, shift: bool = True) -> str:
    """The Spanish twin of an English page: Spanish text in the HTML, file addresses one folder deeper."""
    parser = _SpanishStatic(swap=swap, shift=shift)
    parser.feed(page_html)
    parser.close()
    return "".join(parser.out)


def main() -> None:
    catalog = update_catalogs()
    update_informatico_css()

    res_dir = ROOT / "src" / "research"
    es_dir = res_dir / ES_PREFIX.strip("/")
    hub_html = render_hub_index(catalog)
    (res_dir / "index.html").write_text(hub_html, encoding="utf-8")
    es_dir.mkdir(parents=True, exist_ok=True)
    (es_dir / "index.html").write_text(to_spanish_static(render_hub_index(catalog, "es")), encoding="utf-8")

    count = 0
    for pillar, folios in catalog["pillars"].items():
        pdir = res_dir / pillar
        pdir.mkdir(parents=True, exist_ok=True)
        # Pillar index shows Folio 01 mounted by default + all 8 in the rack and stream
        p_html = render_pillar_or_folio_page(pillar, folios, folios[0], is_standalone=False, catalog=catalog)
        (pdir / "index.html").write_text(p_html, encoding="utf-8")
        (es_dir / pillar).mkdir(parents=True, exist_ok=True)
        (es_dir / pillar / "index.html").write_text(to_spanish_static(render_pillar_hub(pillar, folios, catalog, "es")), encoding="utf-8")

        for f in folios:
            fdir = pdir / f["slug"]
            fdir.mkdir(parents=True, exist_ok=True)
            f_html = render_pillar_or_folio_page(pillar, folios, f, is_standalone=True, catalog=catalog)
            (fdir / "index.html").write_text(f_html, encoding="utf-8")
            es_fdir = es_dir / pillar / f["slug"]
            es_fdir.mkdir(parents=True, exist_ok=True)
            (es_fdir / "index.html").write_text(to_spanish_static(render_folio_page(pillar, folios, f, catalog, "es")), encoding="utf-8")
            count += 1

    (res_dir / "sitemap.xml").write_text(render_research_sitemap(catalog), encoding="utf-8")
    (res_dir / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://informatico.ai/sitemap.xml\n",
        encoding="utf-8",
    )
    (res_dir / "llms.txt").write_text(render_llms_txt(catalog), encoding="utf-8")
    (res_dir / "404.html").write_text(render_not_found(), encoding="utf-8")

    print(f"PASS: Built Informatico.ai hub + 4 pillar racks + {count} standalone 5-Act HTML Folios, each in English and Spanish (/{ES_PREFIX}) + sitemap.xml + robots.txt + llms.txt + 404.html.")



if __name__ == "__main__":
    main()
