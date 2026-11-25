#!/usr/bin/env python3
"""Parity, isolated negative-control, and browser JS solver tests for Architecture Folio A.04."""
from __future__ import annotations

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

from folios.architecture import a04 as a04_folio  # noqa: E402

PAGES = (
    (ROOT / "src" / "architecture" / "a04" / "index.html", "en"),
    (ROOT / "src" / "es-mx" / "architecture" / "a04" / "index.html", "es"),
)
SKILL_MD = ROOT / "skills" / "architecture" / "a04" / "SKILL.md"


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


def _require_int_at_least(value: object, name: str, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer, got {value!r}")
    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}, got {value}")
    return value


def evaluate_gerberette_lever(
    arm_a_m: float = 1.6,
    backspan_c_m: float = 6.0,
    floor_reaction_vp_kn: float = 4800.0,
) -> dict[str, float]:
    a_m = _require_positive(arm_a_m, "arm_a_m")
    c_m = _require_positive(backspan_c_m, "backspan_c_m")
    vp_kn = _require_positive(floor_reaction_vp_kn, "floor_reaction_vp_kn")

    ratio = a_m / c_m
    t_tie_kn = vp_kn * ratio
    c_col_kn = vp_kn * (1.0 + ratio)
    moment_pivot_residual = vp_kn * a_m - t_tie_kn * c_m
    vertical_residual = c_col_kn - (vp_kn + t_tie_kn)
    sf_surrogate = 3.12 * (1280.0 / max(100.0, t_tie_kn))
    return {
        "ratio_a_over_c": ratio,
        "t_tie_unrounded_kn": t_tie_kn,
        "t_tie_kn": round(t_tie_kn, 1),
        "c_col_unrounded_kn": c_col_kn,
        "c_col_kn": round(c_col_kn, 1),
        "moment_pivot_residual_kn_m": moment_pivot_residual,
        "vertical_residual_kn": vertical_residual,
        "sf_surrogate_unrounded": sf_surrogate,
        "sf_surrogate": round(sf_surrogate, 2),
    }


def evaluate_maxwell_calladine_3d(
    bars_b: int,
    joints_j: int,
    self_stress_s: int = 0,
) -> dict[str, int]:
    b = _require_int_at_least(bars_b, "bars_b", 1)
    j = _require_int_at_least(joints_j, "joints_j", 3)
    s = _require_int_at_least(self_stress_s, "self_stress_s", 0)
    lhs = b - 3 * j + 6
    mechanisms_m = s - lhs
    if mechanisms_m < 0:
        raise ValueError(
            f"self_stress_s={s} incompatible with b - 3j + 6 = {lhs} (would imply m = {mechanisms_m} < 0)"
        )
    return {
        "b_minus_3j_plus_6": lhs,
        "self_stress_s": s,
        "mechanisms_m": mechanisms_m,
    }


def _js_round_half_up(x: float) -> int:
    return int(math.floor(x + 0.5))


def evaluate_a04_browser_slider(
    arm_a_m: float = 1.6,
    backspan_c_m: float = 6.0,
) -> dict[str, object]:
    """Mirror src/modules/solvers.mjs a04 branch, including JS parseFloat(...) || fallback semantics."""
    a_raw = _require_number(arm_a_m, "arm_a_m")
    c_raw = _require_number(backspan_c_m, "backspan_c_m")
    if a_raw < 0.0:
        raise ValueError(f"arm_a_m must be non-negative (>= 0), got {a_raw}")
    if c_raw < 0.0:
        raise ValueError(f"backspan_c_m must be non-negative (>= 0), got {c_raw}")

    a_m = a_raw if a_raw != 0.0 else 4.5
    c_m = c_raw if c_raw != 0.0 else 0.032
    tie_tension = 4800.0 * (a_m / c_m)
    sf = 3.12 * (1280.0 / max(100.0, tie_tension))
    camber_y1 = _js_round_half_up(86.0 - (a_m - 1.6) * 8.0)
    camber_y2 = _js_round_half_up(134.0 - (a_m - 1.6) * 8.0)
    tie_int = _js_round_half_up(tie_tension)
    return {
        "a_label": f"{a_m:.2f} m",
        "c_label": f"{c_m:.2f} m",
        "inline_a": f"a = {a_m:.2f} m",
        "r0": "About 48 m (fixed reference text)",
        "r1": f"{tie_tension:,.1f} kN (SF = {sf:.2f}, illustrative)",
        "r2": "τ_pod = 15 yr / τ_frame = 100 yr (fixed text)",
        "r3": (
            "m = 0 assumed (fixed) · SF ≥ 1.50 (illustrative)"
            if sf >= 1.5
            else "SF < 1.50 (illustrative tie surrogate; m = 0 assumed)"
        ),
        "alert": "false" if sf >= 1.5 else "true",
        "truss1_d": f"M 175 82 Q 340 {camber_y1} 505 82",
        "truss2_d": f"M 175 130 Q 340 {camber_y2} 505 130",
        "svg_label": f"Exoskeleton model · T_tie = {tie_int:,} kN (assumed V_p = 4,800 kN)",
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


class A04SolverAndSafetyBoundaryTests(unittest.TestCase):
    def test_lever_statics_thresholds_and_built_html_boundaries(self) -> None:
        self.assertEqual(a04_folio.FOLIO["primary_kernel"], "tools/folios/architecture/a04.py")
        self.assertEqual(a04_folio.FOLIO["kernel_verdict"], "Not independently verified")
        self.assertEqual(a04_folio.FOLIO["kernel_verdict_es"], "Sin verificación independiente")

        base = evaluate_gerberette_lever(1.6, 6.0, 4800.0)
        self.assertEqual(base["t_tie_kn"], 1280.0)
        self.assertEqual(base["c_col_kn"], 6080.0)
        self.assertEqual(base["sf_surrogate"], 3.12)
        self.assertAlmostEqual(base["moment_pivot_residual_kn_m"], 0.0, places=9)
        self.assertAlmostEqual(base["vertical_residual_kn"], 0.0, places=9)

        grid_min = evaluate_gerberette_lever(0.8, 8.5, 4800.0)
        grid_max = evaluate_gerberette_lever(2.6, 3.5, 4800.0)
        just_safe = evaluate_gerberette_lever(1.90, 3.5, 4800.0)
        just_alert = evaluate_gerberette_lever(1.95, 3.5, 4800.0)
        self.assertEqual(grid_min["t_tie_kn"], 451.8)
        self.assertEqual(grid_min["sf_surrogate"], 8.84)
        self.assertEqual(grid_max["t_tie_kn"], 3565.7)
        self.assertEqual(grid_max["sf_surrogate"], 1.12)
        self.assertGreaterEqual(just_safe["sf_surrogate_unrounded"], 1.50)
        self.assertLess(just_alert["sf_surrogate_unrounded"], 1.50)
        self.assertEqual(just_alert["t_tie_kn"], 2674.3)
        self.assertEqual(just_alert["sf_surrogate"], 1.49)

        tetra = evaluate_maxwell_calladine_3d(bars_b=6, joints_j=4, self_stress_s=0)
        octa = evaluate_maxwell_calladine_3d(bars_b=12, joints_j=6, self_stress_s=0)
        cube_pin = evaluate_maxwell_calladine_3d(bars_b=12, joints_j=8, self_stress_s=0)
        self.assertEqual(tetra["mechanisms_m"], 0)
        self.assertEqual(octa["mechanisms_m"], 0)
        self.assertEqual(cube_pin["mechanisms_m"], 6)

        self.assertTrue(SKILL_MD.is_file(), f"Missing generated skill file: {SKILL_MD}")
        skill_txt = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("not a structural design method", skill_txt.lower())
        self.assertIn("2,662.4 kn", skill_txt.lower())
        self.assertIn("fixed reference text", skill_txt.lower())

        ref_slider = evaluate_a04_browser_slider(1.6, 6.0)
        expected_readouts = (ref_slider["r0"], ref_slider["r1"], ref_slider["r2"], ref_slider["r3"])
        for page, lang in PAGES:
            self.assertTrue(page.is_file(), f"Missing built HTML page: {page}")
            txt = page.read_text(encoding="utf-8")
            strip = re.search(r'<div class="tp-readout-strip".*?</div>\s*</div>', txt, re.S)
            self.assertIsNotNone(strip, f"Missing readout strip in {page}")
            scope = strip.group(0) if strip else txt
            for tok in expected_readouts:
                self.assertIn(str(tok), scope, page.name)
            self.assertIn('id="tp-a04-truss-1" data-custom-curve="1"', txt)
            self.assertIn('id="tp-a04-truss-2" data-custom-curve="1"', txt)
            self.assertIn(str(ref_slider["truss1_d"]), txt)
            self.assertIn(str(ref_slider["truss2_d"]), txt)
            self.assertIn(str(ref_slider["svg_label"]), txt)
            self.assertNotIn("Stages 1 -&gt; 4 above", txt)
            self.assertNotIn("Stages 1 -> 4 above", txt)
            self.assertNotIn("tectonic_verify.py", txt)
            self.assertNotIn("widely seen", txt.lower())
            self.assertNotIn("kitchen tables", txt.lower())
            self.assertNotIn("cook drew plug-in city and walking city", txt.lower())
            self.assertNotIn("outside the column line", txt.lower())
            self.assertNotIn("fuera de la línea de columnas", txt.lower())
            self.assertIsNone(re.search(r"\boften\b", txt, re.I), f"Unsourced 'often' in {page}")
            if lang == "en":
                self.assertIn("not a structural design method", txt.lower())
                self.assertIn("herron drew walking city", txt.lower())
                self.assertIn("inside the column line", txt.lower())
                self.assertIn("gave bar-count rules for stiff frames", txt.lower())
                self.assertIn("2,662.4 kn", txt.lower())
                self.assertIn("451.8 kn", txt.lower())
                self.assertIn("3,565.7 kn", txt.lower())
            else:
                self.assertIn("no un método de diseño estructural", txt.lower())
                self.assertIn("dentro de la línea de columnas", txt.lower())
                self.assertIn("2,662.4 kn", txt.lower())
                self.assertIn("451.8", txt.lower())
                self.assertIn("3,565.7 kn", txt.lower())

    def test_strict_input_validation_with_named_value_errors(self) -> None:
        with self.assertRaisesRegex(ValueError, r"arm_a_m must be a finite real number"):
            evaluate_gerberette_lever(arm_a_m=True)  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, r"arm_a_m must be strictly positive"):
            evaluate_gerberette_lever(arm_a_m=0.0)
        with self.assertRaisesRegex(ValueError, r"backspan_c_m must be strictly positive"):
            evaluate_gerberette_lever(backspan_c_m=-2.0)
        with self.assertRaisesRegex(ValueError, r"floor_reaction_vp_kn must be finite"):
            evaluate_gerberette_lever(floor_reaction_vp_kn=math.inf)
        with self.assertRaisesRegex(ValueError, r"joints_j must be >= 3"):
            evaluate_maxwell_calladine_3d(bars_b=3, joints_j=2)
        with self.assertRaisesRegex(ValueError, r"self_stress_s=0 incompatible with b - 3j \+ 6 = 1"):
            evaluate_maxwell_calladine_3d(bars_b=7, joints_j=4, self_stress_s=0)
        with self.assertRaisesRegex(ValueError, r"arm_a_m must be non-negative"):
            evaluate_a04_browser_slider(arm_a_m=-0.5, backspan_c_m=6.0)

    def test_browser_solvers_mjs_matches_python_reference_and_folio_readouts_across_grid(self) -> None:
        found = _find_node_cmd()
        if found is None:
            self.skipTest("No Node/Electron runtime available for solvers.mjs parity check")
        cmd_prefix, env = found
        solvers_uri = (ROOT / "src" / "modules" / "solvers.mjs").resolve().as_uri()
        cases = [
            (0.8, 8.5),
            (1.6, 6.0),
            (1.90, 3.5),
            (1.95, 3.5),
            (2.2, 4.5),
            (2.6, 3.5),
            (0.0, 6.0),
        ]
        harness = f"""
class El {{
  constructor(id, val = '') {{
    this.id = id;
    this.value = String(val);
    this.step = '0.05';
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
  'tp-arch-rise': new El('tp-arch-rise', '1.6'),
  'tp-arch-load': new El('tp-arch-load', '6.0'),
  'tp-arch-rise-val': new El('tp-arch-rise-val'),
  'tp-arch-load-val': new El('tp-arch-load-val'),
  'tp-inline-rise': new El('tp-inline-rise'),
  'tp-readout-thrust': new El('tp-readout-thrust'),
  'tp-readout-kern': new El('tp-readout-kern'),
  'tp-readout-arch-r2': new El('tp-readout-arch-r2'),
  'tp-readout-arch-box': new El('tp-readout-arch-box'),
  'tp-readout-arch-status': new El('tp-readout-arch-status'),
  'tp-a04-truss-1': new El('tp-a04-truss-1'),
  'tp-a04-truss-2': new El('tp-a04-truss-2'),
  'tp-a04-svg-label': new El('tp-a04-svg-label'),
}};
globalThis.window = {{ location: {{ pathname: '/architecture/a04/' }}, addEventListener() {{}} }};
globalThis.document = {{
  documentElement: {{ dataset: {{}}, getAttribute: () => 'en' }},
  body: {{ dataset: {{}}, getAttribute: (k) => (k === 'data-folio-slug' ? 'a04' : null) }},
  addEventListener() {{}},
  getElementById: (id) => nodes[id] || null,
  querySelector: (sel) => (sel === '[data-folio-slug]' ? {{ getAttribute: () => 'a04' }} : null),
  querySelectorAll: () => [],
}};
const {{ initPlateSolvers }} = await import({json.dumps(solvers_uri)});
initPlateSolvers();
const initSnapshot = {{
  r0: nodes['tp-readout-thrust'].textContent,
  r1: nodes['tp-readout-kern'].textContent,
  r2: nodes['tp-readout-arch-r2'].textContent,
  r3: nodes['tp-readout-arch-status'].textContent,
  alert: nodes['tp-readout-arch-box'].getAttribute('data-alert'),
  truss1: nodes['tp-a04-truss-1'].getAttribute('d'),
  truss2: nodes['tp-a04-truss-2'].getAttribute('d'),
  svgLabel: nodes['tp-a04-svg-label'].textContent,
}};
const cases = {json.dumps(cases)};
const out = {{ init: initSnapshot }};
for (const [a, c] of cases) {{
  nodes['tp-arch-rise'].value = String(a);
  nodes['tp-arch-load'].value = String(c);
  nodes['tp-arch-rise'].listeners['input']();
  out[`${{a}}_${{c}}`] = {{
    aLabel: nodes['tp-arch-rise-val'].textContent,
    cLabel: nodes['tp-arch-load-val'].textContent,
    inlineA: nodes['tp-inline-rise'].textContent,
    r0: nodes['tp-readout-thrust'].textContent,
    r1: nodes['tp-readout-kern'].textContent,
    r2: nodes['tp-readout-arch-r2'].textContent,
    r3: nodes['tp-readout-arch-status'].textContent,
    alert: nodes['tp-readout-arch-box'].getAttribute('data-alert'),
    truss1: nodes['tp-a04-truss-1'].getAttribute('d'),
    truss2: nodes['tp-a04-truss-2'].getAttribute('d'),
    svgLabel: nodes['tp-a04-svg-label'].textContent,
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

        folio_ro = [r["value"] for r in a04_folio.FOLIO["readouts"]]
        init_js = js_map["init"]
        self.assertEqual([init_js["r0"], init_js["r1"], init_js["r2"], init_js["r3"]], folio_ro)
        self.assertEqual(init_js["alert"], "false")

        for a_val, c_val in cases:
            py_ev = evaluate_a04_browser_slider(a_val, c_val)
            key_a = int(a_val) if float(a_val).is_integer() else a_val
            key_c = int(c_val) if float(c_val).is_integer() else c_val
            got = js_map[f"{key_a}_{key_c}"]
            self.assertEqual(got["aLabel"], py_ev["a_label"])
            self.assertEqual(got["cLabel"], py_ev["c_label"])
            self.assertEqual(got["inlineA"], py_ev["inline_a"])
            self.assertEqual(got["r0"], py_ev["r0"])
            self.assertEqual(got["r1"], py_ev["r1"])
            self.assertEqual(got["r2"], py_ev["r2"])
            self.assertEqual(got["r3"], py_ev["r3"])
            self.assertEqual(got["alert"], py_ev["alert"])
            self.assertEqual(got["truss1"], py_ev["truss1_d"])
            self.assertEqual(got["truss2"], py_ev["truss2_d"])
            self.assertEqual(got["svgLabel"], py_ev["svg_label"])


if __name__ == "__main__":
    unittest.main()
