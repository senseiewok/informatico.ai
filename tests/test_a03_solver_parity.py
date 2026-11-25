#!/usr/bin/env python3
"""Parity, isolated negative-control, and browser JS solver tests for Architecture Folio A.03."""
from __future__ import annotations

import importlib.util
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

from folios.architecture import a03 as a03_folio  # noqa: E402

PAGES = (
    (ROOT / "src" / "architecture" / "a03" / "index.html", "en"),
    (ROOT / "src" / "es-mx" / "architecture" / "a03" / "index.html", "es"),
)
SKILL_MD = ROOT / "skills" / "architecture" / "a03" / "SKILL.md"


def _load_tectonic_verify():
    candidates = (
        ROOT.parent / "architecture" / "tools" / "tectonic_verify.py",
        ROOT.parent.parent.parent / "architecture" / "tools" / "tectonic_verify.py",
    )
    for cand in candidates:
        if cand.is_file():
            spec = importlib.util.spec_from_file_location("architecture_tectonic_verify", cand)
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                return mod
    return None


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


def _require_nonnegative(value: object, name: str) -> float:
    out = _require_number(value, name)
    if out < 0.0:
        raise ValueError(f"{name} must be non-negative (>= 0), got {out}")
    return out


def evaluate_stack_draft_physical(
    stack_height_m: float = 9.0,
    delta_t_k: float = 11.2,
    t_ext_k: float = 303.0,
    rho_0_kg_m3: float = 1.2,
    zeta_tot: float = 9.3,
    free_area_m2_per_m: float = 0.047,
    g_m_s2: float = 9.81,
) -> dict[str, float]:
    h_m = _require_positive(stack_height_m, "stack_height_m")
    dt_k = _require_nonnegative(delta_t_k, "delta_t_k")
    te_k = _require_positive(t_ext_k, "t_ext_k")
    rho = _require_positive(rho_0_kg_m3, "rho_0_kg_m3")
    zeta = _require_positive(zeta_tot, "zeta_tot")
    area_m = _require_positive(free_area_m2_per_m, "free_area_m2_per_m")
    grav = _require_positive(g_m_s2, "g_m_s2")

    dp_pa = rho * grav * h_m * (dt_k / te_k)
    vel_m_s = math.sqrt((2.0 * dp_pa) / (zeta * rho))
    m_dot_kg_s_m = rho * area_m * vel_m_s
    m_dot_radical_kg_s_m = area_m * math.sqrt((2.0 * rho * dp_pa) / zeta)
    flow_m3_h_per_m = area_m * vel_m_s * 3600.0
    return {
        "dp_unrounded_pa": dp_pa,
        "dp_pa": round(dp_pa, 2),
        "velocity_unrounded_m_s": vel_m_s,
        "velocity_m_s": round(vel_m_s, 2),
        "m_dot_kg_s_m": m_dot_kg_s_m,
        "m_dot_radical_kg_s_m": m_dot_radical_kg_s_m,
        "flow_unrounded_m3_h_m": flow_m3_h_per_m,
        "flow_m3_h_m": round(flow_m3_h_per_m, 1),
    }


def evaluate_thermosiphon_worked_example(
    chimney_height_m: float = 4.5,
    delta_t_k: float = 8.0,
    t_0_k: float = 293.15,
    cd: float = 0.65,
    opening_area_m2: float = 0.36,
    room_volume_m3: float = 54.0,
    g_m_s2: float = 9.81,
) -> dict[str, float]:
    h_m = _require_positive(chimney_height_m, "chimney_height_m")
    dt_k = _require_nonnegative(delta_t_k, "delta_t_k")
    t0_k = _require_positive(t_0_k, "t_0_k")
    c_d = _require_positive(cd, "cd")
    if c_d > 1.0:
        raise ValueError(f"cd must lie in (0, 1], got {c_d}")
    area = _require_positive(opening_area_m2, "opening_area_m2")
    vol = _require_positive(room_volume_m3, "room_volume_m3")
    grav = _require_positive(g_m_s2, "g_m_s2")

    v_ideal = math.sqrt(2.0 * grav * h_m * (dt_k / t0_k))
    q_m3_s = (c_d * area) * v_ideal
    ach_hr = (q_m3_s * 3600.0) / vol
    return {
        "v_ideal_m_s": round(v_ideal, 2),
        "q_unrounded_m3_s": q_m3_s,
        "q_m3_s": round(q_m3_s, 3),
        "ach_unrounded_hr": ach_hr,
        "ach_hr": round(ach_hr, 2),
    }


def evaluate_a03_browser_slider(
    stack_height_m: float = 9.0,
    delta_t_k: float = 11.2,
) -> dict[str, object]:
    """Mirror src/modules/solvers.mjs:1389-1432, including JS parseFloat(...) || fallback semantics."""
    h_raw = _require_nonnegative(stack_height_m, "stack_height_m")
    dt_raw = _require_nonnegative(delta_t_k, "delta_t_k")
    h_m = h_raw if h_raw != 0.0 else 4.5
    dt_k = dt_raw if dt_raw != 0.0 else 0.032
    dp = 3.92 * (h_m / 9.0) * (dt_k / 11.2)
    vel = 0.84 * math.sqrt(max(0.05, dp / 3.92))
    flow = int(math.floor(142.0 * (vel / 0.84) + 0.5))
    ach = 24.21 * (vel / 0.84)
    return {
        "h_label": f"{h_m:.1f} m",
        "dt_label": f"{dt_k:.1f} K",
        "inline_h": f"H = {h_m:.1f} m",
        "dp_ratio": dp / 3.92,
        "vel_m_s": round(vel, 4),
        "r0": f"{dp:.2f} Pa",
        "r1": f"{vel:.2f} m/s ({flow} m³/h·m)",
        "r2": "0.11 (assumed; EN ISO 52022-3 method)",
        "r3": f"{ach:.2f} ACH · 285 EML (illustrative)",
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


class A03SolverAndSafetyBoundaryTests(unittest.TestCase):
    def test_physical_stack_draft_worked_example_and_built_html_boundaries(self) -> None:
        phys = evaluate_stack_draft_physical()
        self.assertEqual(phys["dp_pa"], 3.92)
        self.assertAlmostEqual(phys["dp_unrounded_pa"], 3.9162, places=4)
        self.assertEqual(phys["velocity_m_s"], 0.84)
        self.assertAlmostEqual(phys["m_dot_kg_s_m"], phys["m_dot_radical_kg_s_m"], places=12)
        self.assertAlmostEqual(phys["m_dot_kg_s_m"], 0.04725, places=4)
        self.assertAlmostEqual(phys["flow_m3_h_m"], 141.7, delta=0.5)

        phys_h6 = evaluate_stack_draft_physical(stack_height_m=6.0)
        phys_h12 = evaluate_stack_draft_physical(stack_height_m=12.0)
        phys_4x = evaluate_stack_draft_physical(stack_height_m=18.0, delta_t_k=22.4)
        self.assertAlmostEqual(phys_h12["dp_unrounded_pa"] / phys_h6["dp_unrounded_pa"], 2.0, places=6)
        self.assertAlmostEqual(phys_4x["velocity_unrounded_m_s"] / phys["velocity_unrounded_m_s"], 2.0, places=6)

        worked_54 = evaluate_thermosiphon_worked_example(room_volume_m3=54.0)
        worked_204 = evaluate_thermosiphon_worked_example(room_volume_m3=204.0)
        self.assertEqual(worked_54["v_ideal_m_s"], 1.55)
        self.assertEqual(worked_54["q_m3_s"], 0.363)
        self.assertEqual(worked_54["ach_hr"], 24.21)
        self.assertAlmostEqual(worked_204["ach_hr"], 6.41, places=2)

        low_dt = evaluate_a03_browser_slider(3.5, 0.2)
        self.assertLess(float(low_dt["dp_ratio"]), 0.05)
        self.assertAlmostEqual(float(low_dt["vel_m_s"]), round(0.84 * math.sqrt(0.05), 4), places=4)

        zero_dt = evaluate_a03_browser_slider(9.0, 0.0)
        self.assertEqual(zero_dt["r0"], "0.01 Pa")
        self.assertAlmostEqual(float(zero_dt["vel_m_s"]), round(0.84 * math.sqrt(0.05), 4), places=4)

        self.assertTrue(SKILL_MD.is_file(), f"Missing generated skill file: {SKILL_MD}")
        skill_txt = SKILL_MD.read_text(encoding="utf-8")
        self.assertIn("A * sqrt(2 * rho_0 * delta_p_stack / zeta_tot)", skill_txt)
        self.assertNotIn("sqrt(2 * delta_p / zeta_tot)", skill_txt)

        ref_slider = evaluate_a03_browser_slider(9.0, 11.2)
        expected_readouts = (ref_slider["r0"], ref_slider["r1"], ref_slider["r2"], ref_slider["r3"])
        for page, lang in PAGES:
            self.assertTrue(page.is_file(), f"Missing built HTML page: {page}")
            txt = page.read_text(encoding="utf-8")
            strip = re.search(r'<div class="tp-readout-strip".*?</div>\s*</div>', txt, re.S)
            self.assertIsNotNone(strip, f"Missing readout strip in {page}")
            scope = strip.group(0) if strip else txt
            for tok in expected_readouts:
                self.assertIn(str(tok), scope, page.name)
            self.assertIn(">4 (1:5 Acoustic Baffle Sill Node A-12)</button>", txt)
            self.assertNotIn("Stages 1 -&gt; 4 above", txt)
            self.assertNotIn("Stages 1 -> 4 above", txt)
            self.assertIsNone(re.search(r"\b(?:metre|modelled)\b", txt, re.I), f"UK spelling in {page}")
            if lang == "en":
                self.assertIn("not a facade design method", txt.lower())
                self.assertIn("293.15 k", txt.lower())
                self.assertIn("54 m", txt.lower())
            else:
                self.assertIn("no un método de diseño de fachadas", txt.lower())
                self.assertIn("293.15 k", txt.lower())

    def test_tectonic_verify_kernel_direct_parity(self) -> None:
        tv = _load_tectonic_verify()
        if tv is None:
            self.skipTest("Sibling architecture/tools/tectonic_verify.py not present in standalone checkout")
        res_54 = tv.evaluate_gridshell_and_thermosiphon_cf_ventilation(
            chimney_height_m=4.5,
            delta_t_k=8.0,
            room_volume_m3=54.0,
            opening_area_m2=0.36,
        )
        res_204 = tv.evaluate_gridshell_and_thermosiphon_cf_ventilation(
            chimney_height_m=4.5,
            delta_t_k=8.0,
            room_volume_m3=204.0,
            opening_area_m2=0.36,
        )
        ref_54 = evaluate_thermosiphon_worked_example(room_volume_m3=54.0)
        ref_204 = evaluate_thermosiphon_worked_example(room_volume_m3=204.0)
        self.assertEqual(res_54["thermosiphon_flow_m3_s"], ref_54["q_m3_s"])
        self.assertEqual(res_54["air_changes_per_hour"], ref_54["ach_hr"])
        self.assertEqual(res_54["air_changes_per_hour"], 24.21)
        self.assertEqual(res_204["air_changes_per_hour"], ref_204["ach_hr"])
        self.assertEqual(res_204["air_changes_per_hour"], 6.41)

    def test_strict_input_validation_with_named_value_errors(self) -> None:
        with self.assertRaisesRegex(ValueError, r"stack_height_m must be a finite real number"):
            evaluate_stack_draft_physical(stack_height_m=True)  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, r"stack_height_m must be strictly positive"):
            evaluate_stack_draft_physical(stack_height_m=0.0)
        with self.assertRaisesRegex(ValueError, r"delta_t_k must be non-negative"):
            evaluate_stack_draft_physical(delta_t_k=-1.5)
        with self.assertRaisesRegex(ValueError, r"t_ext_k must be finite"):
            evaluate_stack_draft_physical(t_ext_k=math.nan)
        with self.assertRaisesRegex(ValueError, r"zeta_tot must be strictly positive"):
            evaluate_stack_draft_physical(zeta_tot=0.0)
        with self.assertRaisesRegex(ValueError, r"cd must lie in \(0, 1\]"):
            evaluate_thermosiphon_worked_example(cd=1.2)
        with self.assertRaisesRegex(ValueError, r"room_volume_m3 must be strictly positive"):
            evaluate_thermosiphon_worked_example(room_volume_m3=-10.0)

    def test_browser_solvers_mjs_matches_python_reference_and_folio_readouts_across_grid(self) -> None:
        found = _find_node_cmd()
        if found is None:
            self.skipTest("No Node/Electron runtime available for solvers.mjs parity check")
        cmd_prefix, env = found
        solvers_uri = (ROOT / "src" / "modules" / "solvers.mjs").resolve().as_uri()
        cases = [(3.5, 0.2), (9.0, 0.0), (3.5, 2.0), (4.5, 8.0), (9.0, 11.2), (13.5, 16.0), (18.0, 20.0)]
        harness = f"""
class El {{
  constructor(id, val = '') {{
    this.id = id;
    this.value = String(val);
    this.step = '0.1';
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
  'tp-arch-rise': new El('tp-arch-rise', '9.0'),
  'tp-arch-load': new El('tp-arch-load', '11.2'),
  'tp-arch-rise-val': new El('tp-arch-rise-val'),
  'tp-arch-load-val': new El('tp-arch-load-val'),
  'tp-inline-rise': new El('tp-inline-rise'),
  'tp-readout-thrust': new El('tp-readout-thrust'),
  'tp-readout-kern': new El('tp-readout-kern'),
  'tp-readout-arch-r2': new El('tp-readout-arch-r2'),
  'tp-readout-arch-box': new El('tp-readout-arch-box'),
  'tp-readout-arch-status': new El('tp-readout-arch-status'),
}};
globalThis.window = {{ location: {{ pathname: '/architecture/a03/' }}, addEventListener() {{}} }};
globalThis.document = {{
  documentElement: {{ dataset: {{}}, getAttribute: () => 'en' }},
  body: {{ dataset: {{}}, getAttribute: (k) => (k === 'data-folio-slug' ? 'a03' : null) }},
  addEventListener() {{}},
  getElementById: (id) => nodes[id] || null,
  querySelector: (sel) => (sel === '[data-folio-slug]' ? {{ getAttribute: () => 'a03' }} : null),
  querySelectorAll: () => [],
}};
const {{ initPlateSolvers }} = await import({json.dumps(solvers_uri)});
initPlateSolvers();
const cases = {json.dumps(cases)};
const out = {{}};
for (const [h, dt] of cases) {{
  nodes['tp-arch-rise'].value = String(h);
  nodes['tp-arch-load'].value = String(dt);
  nodes['tp-arch-rise'].listeners['input']();
  out[`${{h}}_${{dt}}`] = {{
    hLabel: nodes['tp-arch-rise-val'].textContent,
    dtLabel: nodes['tp-arch-load-val'].textContent,
    inlineH: nodes['tp-inline-rise'].textContent,
    r0: nodes['tp-readout-thrust'].textContent,
    r1: nodes['tp-readout-kern'].textContent,
    r2: nodes['tp-readout-arch-r2'].textContent,
    r3: nodes['tp-readout-arch-status'].textContent,
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

        folio_ro = [r["value"] for r in a03_folio.FOLIO["readouts"]]
        def_js = js_map["9_11.2"]
        self.assertEqual([def_js["r0"], def_js["r1"], def_js["r2"], def_js["r3"]], folio_ro)

        for h, dt in cases:
            py_ev = evaluate_a03_browser_slider(h, dt)
            key = f"{int(h) if float(h).is_integer() else h}_{int(dt) if float(dt).is_integer() else dt}"
            got = js_map[key]
            self.assertEqual(got["hLabel"], py_ev["h_label"])
            self.assertEqual(got["dtLabel"], py_ev["dt_label"])
            self.assertEqual(got["inlineH"], py_ev["inline_h"])
            self.assertEqual(got["r0"], py_ev["r0"])
            self.assertEqual(got["r1"], py_ev["r1"])
            self.assertEqual(got["r2"], py_ev["r2"])
            self.assertEqual(got["r3"], py_ev["r3"])


if __name__ == "__main__":
    unittest.main()
