#!/usr/bin/env python3
"""Parity, Fourier-series consolidation, negative-control, and browser JS solver tests for Folio E.05."""
from __future__ import annotations

import html
import json
import math
import os
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from folios.engineering import e05 as e05_folio  # noqa: E402

PAGES = (
    (ROOT / "src" / "engineering" / "e05" / "index.html", "en"),
    (ROOT / "src" / "es-mx" / "engineering" / "e05" / "index.html", "es"),
)
SKILL_MD = ROOT / "skills" / "engineering" / "e05" / "SKILL.md"


def _require_number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite real number, got {value!r}")
    out = float(value)
    if not math.isfinite(out):
        raise ValueError(f"{name} must be finite, got {value!r}")
    return out


def _require_positive(value: object, name: str) -> float:
    out = _require_number(value, name)
    if out <= 0.0:
        raise ValueError(f"{name} must be strictly positive (> 0), got {out}")
    return out


def _js_round_half_up(x: float) -> int:
    return int(math.floor(x + 0.5))


def terzaghi_fourier_u_avg(tv: float, terms: int = 200) -> float:
    """Exact 1D Terzaghi Fourier series U_avg(T_v) for uniform initial excess pore pressure."""
    tv_pos = _require_positive(tv, "tv")
    if isinstance(terms, bool) or not isinstance(terms, int) or terms < 10:
        raise ValueError(f"terms must be an integer >= 10, got {terms!r}")
    rem = 0.0
    for m in range(terms):
        odd = 2 * m + 1
        rem += (8.0 / ((odd * odd) * (math.pi * math.pi))) * math.exp(
            -((odd * odd) * (math.pi * math.pi) * tv_pos) / 4.0
        )
    return 1.0 - rem


def evaluate_e05_consolidation_and_pile(
    delta_q_kpa: float = 120.0,
    cv_m2_yr: float = 3.2,
    h_dr_m: float = 6.0,
    t_yr: float = 3.6,
    sigma_v0_kpa: float = 200.0,
) -> dict[str, float | bool]:
    dq = _require_positive(delta_q_kpa, "delta_q_kpa")
    cv = _require_positive(cv_m2_yr, "cv_m2_yr")
    h_dr = _require_positive(h_dr_m, "h_dr_m")
    t_years = _require_positive(t_yr, "t_yr")
    sigma_v0 = _require_positive(sigma_v0_kpa, "sigma_v0_kpa")

    tv = (cv * t_years) / (h_dr * h_dr)
    u_raw = (
        math.sqrt((4.0 * tv) / math.pi)
        if tv <= 0.286
        else 1.0 - (8.0 / (math.pi * math.pi)) * math.exp((-math.pi * math.pi * tv) / 4.0)
    )
    u_clamped = max(0.05, min(0.995, u_raw))
    u_fourier = terzaghi_fourier_u_avg(tv, terms=200)

    sc_mm = (dq / 120.0) * 66.7 * u_clamped
    delta_u = dq * (1.0 - u_clamped)
    ru = min(0.98, delta_u / sigma_v0)
    sigma_v_prime = max(4.0, sigma_v0 * (1.0 - ru))

    q_skin = 2380.0 * (1.0 - 0.65 * ru)
    q_toe = 1980.0 * (1.0 - 0.35 * ru)
    q_ult = max(650.0, q_skin + q_toe)
    p_design = 1400.0 + dq * 1.25
    fs = q_ult / p_design
    alert = bool(ru >= 0.70 or fs < 2.0)

    return {
        "tv": tv,
        "u_avg_clamped": u_clamped,
        "u_avg_fourier": u_fourier,
        "u_avg_pct": round(u_clamped * 100.0, 1),
        "sc_mm": round(sc_mm, 1),
        "delta_u_kpa": delta_u,
        "ru_unrounded": ru,
        "ru": round(ru, 2),
        "sigma_v_prime_kpa": round(sigma_v_prime, 0),
        "q_ult_unrounded_kn": q_ult,
        "q_ult_kn": _js_round_half_up(q_ult),
        "p_design_kn": p_design,
        "fs_unrounded": fs,
        "fs": round(fs, 2),
        "alert": alert,
    }


def evaluate_e05_browser_slider(
    delta_q_kpa: float = 120.0,
    cv_m2_yr: float = 3.2,
) -> dict[str, str]:
    """Mirror src/modules/solvers.mjs updateE05, including JS parseFloat(...) || fallback semantics."""
    dq_raw = _require_number(delta_q_kpa, "delta_q_kpa")
    cv_raw = _require_number(cv_m2_yr, "cv_m2_yr")
    if dq_raw < 0.0:
        raise ValueError(f"delta_q_kpa must be non-negative (>= 0), got {dq_raw}")
    if cv_raw < 0.0:
        raise ValueError(f"cv_m2_yr must be non-negative (>= 0), got {cv_raw}")

    dq = dq_raw if dq_raw != 0.0 else 120.0
    cv = cv_raw if cv_raw != 0.0 else 3.2
    ev = evaluate_e05_consolidation_and_pile(dq, cv)
    u_pct = float(ev["u_avg_clamped"]) * 100.0
    sc_mm = (dq / 120.0) * 66.7 * float(ev["u_avg_clamped"])
    delta_u = float(ev["delta_u_kpa"])
    ru = float(ev["ru_unrounded"])
    sigma_vp = max(4.0, 200.0 * (1.0 - ru))
    q_ult_int = _js_round_half_up(float(ev["q_ult_unrounded_kn"]))
    fs = float(ev["fs_unrounded"])
    alert = bool(ev["alert"])
    bulge_x = _js_round_half_up(360.0 + min(265.0, delta_u * 2.1))

    return {
        "dq_label": f"{dq:.0f} kPa",
        "cv_label": f"{cv:.1f} m²/yr",
        "inline_dq": f"Delta_q = {dq:.0f} kPa",
        "r0": f"{u_pct:.1f}% (S_c = {sc_mm:.1f} mm, model)",
        "r1": f"{q_ult_int:,} kN (FS = {fs:.2f}, model)",
        "r2": f"{ru:.2f} (σ'_v = {sigma_vp:.0f} kPa)",
        "r3": (
            "MODEL FS < 2.0 OR r_u ≥ 0.70 · ILLUSTRATIVE, NOT A SITE DESIGN"
            if alert
            else "MODEL FS ≥ 2.0 · ILLUSTRATIVE, NOT A SITE DESIGN"
        ),
        "alert": "true" if alert else "false",
        "iso_d": f"M 360 30 Q {bulge_x} 112 360 195",
        "svg_label": f"U_avg = {u_pct:.1f}% · Q_ult = {q_ult_int:,} kN",
    }


def _find_node_cmd() -> tuple[list[str], dict[str, str]] | None:
    node_bin = shutil.which("node")
    if node_bin:
        return [node_bin], dict(os.environ)
    local_app = os.environ.get("LOCALAPPDATA", "")
    if local_app:
        vscode_exe = Path(local_app) / "Programs" / "Microsoft VS Code" / "Code.exe"
        if vscode_exe.is_file():
            env = dict(os.environ)
            env["ELECTRON_RUN_AS_NODE"] = "1"
            return [str(vscode_exe)], env
    return None


class E05SolverAndSafetyBoundaryTests(unittest.TestCase):
    def test_consolidation_fourier_parity_thresholds_and_built_html_boundaries(self) -> None:
        self.assertEqual(e05_folio.FOLIO["primary_kernel"], "tools/folios/engineering/e05.py")
        self.assertEqual(e05_folio.FOLIO["kernel_verdict"], "Not independently verified")
        self.assertEqual(e05_folio.FOLIO["kernel_verdict_es"], "Sin verificación independiente")
        self.assertEqual(e05_folio.FOLIO["current_edition"], "REV 1.2")
        self.assertEqual(e05_folio.FOLIO["date_redated"], "2026-11-14")

        # Verify piecewise Terzaghi approximation tracks 200-term Fourier series within 0.004 across slider range
        for cv_probe in (0.5, 0.8, 1.5, 2.8, 2.9, 3.2, 5.5, 8.0):
            ev_probe = evaluate_e05_consolidation_and_pile(120.0, cv_probe)
            self.assertAlmostEqual(
                float(ev_probe["u_avg_clamped"]),
                float(ev_probe["u_avg_fourier"]),
                delta=0.004,
                msg=f"Piecewise vs Fourier mismatch at c_v={cv_probe}",
            )

        base = evaluate_e05_consolidation_and_pile(120.0, 3.2)
        self.assertAlmostEqual(float(base["tv"]), 0.320, places=6)
        self.assertEqual(base["u_avg_pct"], 63.2)
        self.assertEqual(base["sc_mm"], 42.2)
        self.assertEqual(base["ru"], 0.22)
        self.assertEqual(base["sigma_v_prime_kpa"], 156.0)
        self.assertEqual(base["q_ult_kn"], 3865)
        self.assertEqual(base["fs"], 2.49)
        self.assertFalse(bool(base["alert"]))

        exp1_lo = evaluate_e05_consolidation_and_pile(60.0, 3.2)
        exp1_hi = evaluate_e05_consolidation_and_pile(220.0, 3.2)
        self.assertEqual((exp1_lo["sc_mm"], exp1_lo["ru"], exp1_lo["q_ult_kn"], exp1_lo["fs"]), (21.1, 0.11, 4113, 2.79))
        self.assertEqual((exp1_hi["sc_mm"], exp1_hi["ru"], exp1_hi["q_ult_kn"], exp1_hi["fs"]), (77.3, 0.40, 3453, 2.06))

        exp2_nom = evaluate_e05_consolidation_and_pile(120.0, 0.8)
        exp2_alert = evaluate_e05_consolidation_and_pile(220.0, 0.8)
        self.assertAlmostEqual(float(exp2_nom["tv"]), 0.080, places=6)
        self.assertEqual((exp2_nom["u_avg_pct"], exp2_nom["ru"], exp2_nom["fs"], exp2_nom["alert"]), (31.9, 0.41, 2.22, False))
        self.assertEqual((exp2_alert["u_avg_pct"], exp2_alert["ru"], exp2_alert["q_ult_kn"], exp2_alert["fs"], exp2_alert["alert"]), (31.9, 0.75, 2682, 1.60, True))

        self.assertTrue(SKILL_MD.is_file(), f"Missing generated skill file: {SKILL_MD}")
        skill_txt = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("not a foundation or structural design method", skill_txt.lower())
        self.assertIn("no number here may be used on a real structure", skill_txt.lower())
        self.assertNotIn("screening", skill_txt.lower())

        self.assertIn("no un método de diseño", e05_folio.ES_TRANSLATION["subtitle_es"].lower())
        self.assertIn("no un método de diseño", e05_folio.ES_TRANSLATION["plain_es"].lower())
        self.assertIn("2,682 kn", e05_folio.ES_TRANSLATION["deep_es"].lower())
        self.assertIn("pueden registrar", e05_folio.ES_TRANSLATION["deep_es"].lower())

        ref_slider = evaluate_e05_browser_slider(120.0, 3.2)
        expected_readouts = (ref_slider["r0"], ref_slider["r1"], ref_slider["r2"], ref_slider["r3"])
        for page, lang in PAGES:
            self.assertTrue(page.is_file(), f"Missing built HTML page: {page}")
            txt = page.read_text(encoding="utf-8")
            paras = re.findall(r"<p\b[^>]*>(.*?)</p>", txt, re.S)
            words = sum(len(re.sub(r"<[^>]+>", " ", p).split()) for p in paras)
            self.assertGreaterEqual(words, 4200, f"{page} below 4200-word depth floor ({words})")
            self.assertLess(words, 4937 if lang == "en" else 4948, f"{page} was not shortened ({words})")

            strip = re.search(r'<div class="tp-readout-strip".*?</div>\s*</div>', txt, re.S)
            self.assertIsNotNone(strip, f"Missing readout strip in {page}")
            scope = html.unescape(strip.group(0) if strip else txt)
            for tok in expected_readouts:
                self.assertIn(tok, scope, page.name)

            self.assertIn('id="tp-e05-svg-isochrone" data-custom-curve="1" d="M 360 30 Q 453 112 360 195"', txt)
            self.assertIn('<path data-custom-curve="1" d="M 360 30 Q 445 112 360 195"', txt)
            self.assertIn(ref_slider["svg_label"], txt)
            self.assertNotIn("continuum_verify.py", txt)
            self.assertNotIn("robert college", txt.lower())
            self.assertNotIn("usually taken", txt.lower())
            self.assertNotIn("commonly instrumented", txt.lower())
            self.assertNotIn("suele fecharse", txt.lower())
            self.assertNotIn("suelen registrar", txt.lower())
            self.assertNotIn("poroelastic gels", txt.lower())
            self.assertNotIn("design sketch", txt.lower())
            self.assertNotIn("requires larger downward displacement to mobilize ultimate skin friction", txt.lower())
            self.assertIsNone(re.search(r"\bscreening\b", txt, re.I), f"Forbidden 'screening' in {page}")
            es_dossier = re.search(r'<details class="tp-es-dossier".*?</details>', txt, re.S)
            self.assertIsNotNone(es_dossier, f"Missing Spanish dossier in {page}")
            es_scope = html.unescape(es_dossier.group(0)).lower() if es_dossier else ""
            self.assertIn("no un método de diseño", es_scope)
            self.assertIn("2,682 kn", es_scope)
            self.assertIn("pueden registrar", es_scope)
            if lang == "en":
                self.assertIn("not a geotechnical or structural design method", txt.lower())
                self.assertIn("2,682 kn", txt.lower())
                self.assertIn("distinct from statement tallies", txt.lower())
                self.assertIn("differential settlement and angular distortion can crack walls and frames", txt.lower())

    def test_strict_input_validation_with_named_value_errors(self) -> None:
        with self.assertRaisesRegex(ValueError, r"delta_q_kpa must be a finite real number"):
            evaluate_e05_consolidation_and_pile(delta_q_kpa=False)  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, r"delta_q_kpa must be strictly positive"):
            evaluate_e05_consolidation_and_pile(delta_q_kpa=0.0)
        with self.assertRaisesRegex(ValueError, r"cv_m2_yr must be strictly positive"):
            evaluate_e05_consolidation_and_pile(cv_m2_yr=-1.0)
        with self.assertRaisesRegex(ValueError, r"h_dr_m must be finite"):
            evaluate_e05_consolidation_and_pile(h_dr_m=math.nan)
        with self.assertRaisesRegex(ValueError, r"terms must be an integer >= 10"):
            terzaghi_fourier_u_avg(0.32, terms=3)
        with self.assertRaisesRegex(ValueError, r"delta_q_kpa must be non-negative"):
            evaluate_e05_browser_slider(delta_q_kpa=-5.0, cv_m2_yr=3.2)

    def test_browser_solvers_mjs_matches_python_reference_and_folio_readouts_across_grid(self) -> None:
        found = _find_node_cmd()
        if found is None:
            self.skipTest("No Node/Electron runtime available for solvers.mjs parity check")
        cmd_prefix, env = found
        solvers_uri = (ROOT / "src" / "modules" / "solvers.mjs").resolve().as_uri()
        cases = [
            (40.0, 8.0),
            (60.0, 3.2),
            (120.0, 3.2),
            (120.0, 0.8),
            (220.0, 3.2),
            (220.0, 0.8),
            (260.0, 0.5),
            (0.0, 0.0),
        ]
        harness = f"""
class El {{
  constructor(id, val = '') {{
    this.id = id;
    this.value = String(val);
    this.step = '1';
    this.textContent = '';
    this.dataset = {{}};
    this.attrs = {{}};
    this.listeners = {{}};
  }}
  addEventListener(ev, fn) {{ this.listeners[ev] = fn; }}
  setAttribute(k, v) {{ this.attrs[k] = String(v); }}
  getAttribute(k) {{ return this.attrs[k] ?? null; }}
}}
const nodes = {{
  'tp-e05-surcharge': new El('tp-e05-surcharge', '120'),
  'tp-e05-cv': new El('tp-e05-cv', '3.2'),
  'tp-e05-surcharge-val': new El('tp-e05-surcharge-val'),
  'tp-e05-cv-val': new El('tp-e05-cv-val'),
  'tp-inline-surcharge': new El('tp-inline-surcharge'),
  'tp-e05-readout-u': new El('tp-e05-readout-u'),
  'tp-e05-readout-qult': new El('tp-e05-readout-qult'),
  'tp-e05-readout-ru': new El('tp-e05-readout-ru'),
  'tp-e05-readout-status-box': new El('tp-e05-readout-status-box'),
  'tp-e05-readout-status': new El('tp-e05-readout-status'),
  'tp-e05-svg-isochrone': new El('tp-e05-svg-isochrone'),
  'tp-e05-svg-label': new El('tp-e05-svg-label'),
}};
globalThis.window = {{ location: {{ pathname: '/engineering/e05/' }}, addEventListener() {{}} }};
globalThis.document = {{
  documentElement: {{ dataset: {{}}, getAttribute: () => 'en' }},
  body: {{ dataset: {{}}, getAttribute: (k) => (k === 'data-folio-slug' ? 'e05' : null) }},
  addEventListener() {{}},
  getElementById: (id) => nodes[id] || null,
  querySelector: (sel) => (sel === '[data-folio-slug]' ? {{ getAttribute: () => 'e05' }} : null),
  querySelectorAll: () => [],
}};
const {{ initPlateSolvers }} = await import({json.dumps(solvers_uri)});
initPlateSolvers();
if (typeof nodes['tp-e05-surcharge'].listeners['input'] !== 'function') {{
  throw new Error('Missing input listener on tp-e05-surcharge');
}}
if (typeof nodes['tp-e05-cv'].listeners['input'] !== 'function') {{
  throw new Error('Missing input listener on tp-e05-cv');
}}
const initSnapshot = {{
  r0: nodes['tp-e05-readout-u'].textContent,
  r1: nodes['tp-e05-readout-qult'].textContent,
  r2: nodes['tp-e05-readout-ru'].textContent,
  r3: nodes['tp-e05-readout-status'].textContent,
  alert: nodes['tp-e05-readout-status-box'].getAttribute('data-alert'),
  isoD: nodes['tp-e05-svg-isochrone'].getAttribute('d'),
  svgLabel: nodes['tp-e05-svg-label'].textContent,
}};
const cases = {json.dumps(cases)};
const out = {{ init: initSnapshot }};
for (let idx = 0; idx < cases.length; idx++) {{
  const [dq, cv] = cases[idx];
  nodes['tp-e05-surcharge'].value = String(dq);
  nodes['tp-e05-cv'].value = String(cv);
  if (idx % 2 === 0) {{
    nodes['tp-e05-surcharge'].listeners['input']();
  }} else {{
    nodes['tp-e05-cv'].listeners['input']();
  }}
  out[`${{dq}}_${{cv}}`] = {{
    dqLabel: nodes['tp-e05-surcharge-val'].textContent,
    cvLabel: nodes['tp-e05-cv-val'].textContent,
    inlineDq: nodes['tp-inline-surcharge'].textContent,
    r0: nodes['tp-e05-readout-u'].textContent,
    r1: nodes['tp-e05-readout-qult'].textContent,
    r2: nodes['tp-e05-readout-ru'].textContent,
    r3: nodes['tp-e05-readout-status'].textContent,
    alert: nodes['tp-e05-readout-status-box'].getAttribute('data-alert'),
    isoD: nodes['tp-e05-svg-isochrone'].getAttribute('d'),
    svgLabel: nodes['tp-e05-svg-label'].textContent,
  }};
}}
console.log(JSON.stringify(out));
"""
        res = subprocess.run(
            [*cmd_prefix, "--input-type=module", "-e", harness],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
            timeout=20,
        )
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
        js_map = json.loads(res.stdout)

        folio_ro = [r["value"] for r in e05_folio.FOLIO["readouts"]]
        init_js = js_map["init"]
        self.assertEqual([init_js["r0"], init_js["r1"], init_js["r2"], init_js["r3"]], folio_ro)
        self.assertEqual(init_js["alert"], "false")
        self.assertEqual(init_js["isoD"], "M 360 30 Q 453 112 360 195")
        self.assertEqual(init_js["svgLabel"], "U_avg = 63.2% · Q_ult = 3,865 kN")

        for dq_val, cv_val in cases:
            py_ev = evaluate_e05_browser_slider(dq_val, cv_val)
            key_dq = int(dq_val) if float(dq_val).is_integer() else dq_val
            key_cv = int(cv_val) if float(cv_val).is_integer() else cv_val
            got = js_map[f"{key_dq}_{key_cv}"]
            self.assertEqual(got["dqLabel"], py_ev["dq_label"])
            self.assertEqual(got["cvLabel"], py_ev["cv_label"])
            self.assertEqual(got["inlineDq"], py_ev["inline_dq"])
            self.assertEqual(got["r0"], py_ev["r0"])
            self.assertEqual(got["r1"], py_ev["r1"])
            self.assertEqual(got["r2"], py_ev["r2"])
            self.assertEqual(got["r3"], py_ev["r3"])
            self.assertEqual(got["alert"], py_ev["alert"])
            self.assertEqual(got["isoD"], py_ev["iso_d"])
            self.assertEqual(got["svgLabel"], py_ev["svg_label"])


if __name__ == "__main__":
    unittest.main()
