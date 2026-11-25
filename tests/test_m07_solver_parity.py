#!/usr/bin/env python3
"""Focused algebraic, DOM-sync, and grounding-boundary parity tests for Folio M.07."""
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

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
SKILLS = ROOT / "skills"
sys.path.insert(0, str(ROOT / "tools"))

from folios.math import m07  # noqa: E402
from folios.seo_copy import FOLIO_SEO  # noqa: E402


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


def _main_html(text: str) -> str:
    m = re.search(r"<main\b[^>]*>(.*)</main>", text, re.S)
    return m.group(1) if m else text


def _check_real(name: str, val: object) -> float:
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        raise TypeError(f"{name} must be a real number, got {type(val).__name__}")
    out = float(val)
    if not math.isfinite(out):
        raise ValueError(f"{name} must be finite, got {val!r}")
    return out


def pontryagin_motoring_control(
    *,
    p_k_max_w: float,
    mass_kg: float,
    eta_k: float,
    alpha_loss_per_w: float,
    lambda_v: float,
    lambda_e: float,
    v_m_s: float,
) -> tuple[float, float, float]:
    """Return (optimal P_k* in W, v_switch in m/s, v_zero in m/s) on M.07's motoring arc.

    Minimizes the motoring terms of
      H = 1/v + lambda_v * a_net / v - lambda_E * P_batt(P_k) / v
    over P_k in [0, P_{k,max}] with P_batt(P_k) = P_k / eta_k + alpha * P_k^2,
    where lambda_v < 0 and lambda_E < 0 on an open acceleration arc.
    """
    pk_max = _check_real("p_k_max_w", p_k_max_w)
    m = _check_real("mass_kg", mass_kg)
    eta = _check_real("eta_k", eta_k)
    alpha = _check_real("alpha_loss_per_w", alpha_loss_per_w)
    lv = _check_real("lambda_v", lambda_v)
    le = _check_real("lambda_e", lambda_e)
    v = _check_real("v_m_s", v_m_s)

    if pk_max <= 0.0:
        raise ValueError("p_k_max_w must be positive")
    if m <= 0.0:
        raise ValueError("mass_kg must be positive")
    if not (0.0 < eta <= 1.0):
        raise ValueError("eta_k must lie in (0, 1]")
    if alpha < 0.0:
        raise ValueError("alpha_loss_per_w must be non-negative")
    if lv >= 0.0:
        raise ValueError("lambda_v must be negative on a motoring arc")
    if le >= 0.0:
        raise ValueError("lambda_e must be negative when stored energy reduces lap time")
    if v <= 0.0:
        raise ValueError("v_m_s must be positive")

    marginal_at_cap = (1.0 / eta) + 2.0 * alpha * pk_max
    v_switch = lv / (le * m * marginal_at_cap)
    v_zero = (lv * eta) / (le * m)

    if alpha == 0.0:
        dh_dpk = lv / (m * v * v) - le / (eta * v)
        p_opt = pk_max if dh_dpk <= 0.0 else 0.0
        return p_opt, v_switch, v_zero

    p_unconstrained = ((lv / (le * m * v)) - (1.0 / eta)) / (2.0 * alpha)
    p_opt = max(0.0, min(pk_max, p_unconstrained))
    return p_opt, v_switch, v_zero


class FolioM07ParityTests(unittest.TestCase):
    def test_quadratic_loss_taper_deadband_and_braking_sign_identities(self) -> None:
        params = dict(
            mass_kg=798.0,
            eta_k=0.95,
            alpha_loss_per_w=4.5e-7,
            lambda_v=-0.042,
            lambda_e=-5.5e-7,
        )
        p_120, v_sw_120, v_zero = pontryagin_motoring_control(p_k_max_w=120_000.0, v_m_s=75.0, **params)
        p_350, v_sw_350, v_zero_350 = pontryagin_motoring_control(p_k_max_w=350_000.0, v_m_s=75.0, **params)
        _, v_sw_affine, v_zero_aff = pontryagin_motoring_control(
            p_k_max_w=350_000.0,
            v_m_s=75.0,
            mass_kg=798.0,
            eta_k=0.95,
            alpha_loss_per_w=0.0,
            lambda_v=-0.042,
            lambda_e=-5.5e-7,
        )
        self.assertAlmostEqual(v_zero, v_zero_350, places=12)
        self.assertAlmostEqual(v_sw_affine, v_zero_aff, places=12)
        self.assertLess(v_sw_350, v_sw_120)
        self.assertLess(v_sw_120, v_zero)
        self.assertEqual(p_120, 120_000.0)
        self.assertGreater(p_350, 0.0)
        self.assertLess(p_350, 350_000.0)

        # Above v_zero, even infinitesimal electric draw costs more shadow-price energy than thrust saves
        p_above_zero, _, _ = pontryagin_motoring_control(
            p_k_max_w=350_000.0, v_m_s=v_zero + 5.0, **params
        )
        self.assertEqual(p_above_zero, 0.0)

        # Grid-search verification of min_{P_k in [0, P_k,max]} H_motor(v, P_k)
        for v_test in (35.0, v_sw_350, 75.0, v_zero + 5.0):
            p_star, _, _ = pontryagin_motoring_control(p_k_max_w=350_000.0, v_m_s=v_test, **params)

            def h_motor(pk: float, v_cur: float = v_test) -> float:
                p_batt = pk / params["eta_k"] + params["alpha_loss_per_w"] * pk * pk
                return (
                    (1.0 / v_cur)
                    + params["lambda_v"] * (pk / v_cur) / (params["mass_kg"] * v_cur)
                    - params["lambda_e"] * p_batt / v_cur
                )

            grid = [350_000.0 * k / 2000.0 for k in range(2001)] + [p_star]
            best_pk = min(grid, key=h_motor)
            self.assertLessEqual(h_motor(p_star), h_motor(best_pk) + 1.0e-15)
            self.assertAlmostEqual(p_star, best_pk, delta=200.0)

        # Subgradient coasting deadband at P_k = 0: lambda_E* / eta_k <= lambda_v / (m * v) <= lambda_E* * eta_regen
        le_int = -5.5e-7
        eta_k = 0.95
        eta_regen = 0.88
        v_coast = 80.0
        self.assertLess(le_int / eta_k, le_int * eta_regen)
        lv_coast = 0.5 * (le_int / eta_k + le_int * eta_regen) * 798.0 * v_coast
        self.assertLess(le_int / eta_k, lv_coast / (798.0 * v_coast))
        self.assertLess(lv_coast / (798.0 * v_coast), le_int * eta_regen)
        dh_motor_right = lv_coast / (798.0 * v_coast * v_coast) - le_int / (eta_k * v_coast)
        dh_regen_left = lv_coast / (798.0 * v_coast * v_coast) - le_int * eta_regen / v_coast
        self.assertGreater(dh_motor_right, 0.0)
        self.assertLess(dh_regen_left, 0.0)

        # Lift-and-coast regen (lambda_E* * eta_regen < lambda_v / (m * v) < 0): regen active, friction brake off
        lv_lift = 0.5 * (le_int * eta_regen) * 798.0 * v_coast
        self.assertGreater(lv_lift / (798.0 * v_coast), le_int * eta_regen)
        self.assertLess(lv_lift, 0.0)
        self.assertGreater(lv_lift / (798.0 * v_coast * v_coast) - le_int * eta_regen / v_coast, 0.0)
        self.assertGreater(-lv_lift / (798.0 * v_coast), 0.0)

        # Corner-braking arc (lambda_v > 0, lambda_e < 0): dH/dF_brake < 0 and dH/dP_k > 0 -> full regen
        lv_brake = 0.035
        v_corner = 60.0
        dh_df_brake = -lv_brake / (798.0 * v_corner)
        dh_dpk_regen = lv_brake / (798.0 * v_corner * v_corner) - le_int * eta_regen / v_corner
        self.assertLess(dh_df_brake, 0.0)
        self.assertGreater(dh_dpk_regen, 0.0)

    def test_motoring_helper_rejects_invalid_inputs(self) -> None:
        base = dict(
            p_k_max_w=350_000.0,
            mass_kg=798.0,
            eta_k=0.95,
            alpha_loss_per_w=4.5e-7,
            lambda_v=-0.042,
            lambda_e=-5.5e-7,
            v_m_s=75.0,
        )
        with self.assertRaisesRegex(TypeError, "p_k_max_w must be a real number"):
            pontryagin_motoring_control(**{**base, "p_k_max_w": True})  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, "v_m_s must be finite"):
            pontryagin_motoring_control(**{**base, "v_m_s": float("nan")})
        with self.assertRaisesRegex(ValueError, "p_k_max_w must be positive"):
            pontryagin_motoring_control(**{**base, "p_k_max_w": 0.0})
        with self.assertRaisesRegex(ValueError, "mass_kg must be positive"):
            pontryagin_motoring_control(**{**base, "mass_kg": 0.0})
        with self.assertRaisesRegex(ValueError, "eta_k must lie in"):
            pontryagin_motoring_control(**{**base, "eta_k": 1.05})
        with self.assertRaisesRegex(ValueError, "alpha_loss_per_w must be non-negative"):
            pontryagin_motoring_control(**{**base, "alpha_loss_per_w": -1.0e-8})
        with self.assertRaisesRegex(ValueError, "lambda_v must be negative"):
            pontryagin_motoring_control(**{**base, "lambda_v": 0.01})
        with self.assertRaisesRegex(ValueError, "lambda_e must be negative"):
            pontryagin_motoring_control(**{**base, "lambda_e": 0.0})
        with self.assertRaisesRegex(ValueError, "v_m_s must be positive"):
            pontryagin_motoring_control(**{**base, "v_m_s": -5.0})

    def test_solvers_mjs_updates_m07_labels_and_preserves_fixed_readouts(self) -> None:
        solvers_src = (SRC / "modules" / "solvers.mjs").read_text(encoding="utf-8")
        self.assertIn('if (slug === "m07")', solvers_src)
        self.assertIn("tp-m07-pk-text", solvers_src)
        self.assertIn("tp-m07-modes-text", solvers_src)

        found = _find_node_cmd()
        if found is None:
            self.skipTest("No Node/Electron runtime available for solvers.mjs parity check")
        cmd_prefix, env = found
        solvers_uri = (SRC / "modules" / "solvers.mjs").resolve().as_uri()
        js_harness = f"""
class El {{
  constructor(id, val = "", step = "1", text = "", attrs = {{}}) {{
    this.id = id;
    this.value = String(val);
    this.step = String(step);
    this.min = "0";
    this.max = "400";
    this.textContent = String(text);
    this.dataset = {{}};
    this.attrs = {{ ...attrs }};
    this.listeners = {{}};
    this.classList = {{ add() {{}}, remove() {{}}, toggle() {{}}, contains() {{ return false; }} }};
    this.style = {{ setProperty() {{}} }};
    this.children = [];
  }}
  addEventListener(ev, fn) {{ (this.listeners[ev] ||= []).push(fn); }}
  dispatch(ev) {{ for (const fn of (this.listeners[ev] || [])) fn(); }}
  setAttribute(k, v) {{ this.attrs[k] = String(v); }}
  getAttribute(k) {{ return this.attrs[k] ?? null; }}
  appendChild(ch) {{ this.children.push(ch); return ch; }}
  closest() {{ return null; }}
  querySelector() {{ return null; }}
  querySelectorAll() {{ return []; }}
}}
const clipCurve = new El("tp-m07-clip-curve", "", "1", "", {{
  "data-custom-curve": "1",
  stroke: "var(--tp-minium)",
  "stroke-dasharray": "4,3",
}});
const pmpCurve = new El("tp-m07-pmp-curve", "", "1", "", {{
  "data-custom-curve": "1",
  stroke: "var(--tp-verdigris)",
}});
const unmarkedCurve = new El("tp-m07-unmarked-control", "", "1", "", {{
  stroke: "var(--tp-prussian)",
}});
const svgStage = new El("tp-m07-svg");
svgStage.querySelectorAll = (sel) => (sel.includes("path") ? [clipCurve, pmpCurve, unmarkedCurve] : []);
const nodes = {{
  "tp-math-prime": Object.assign(new El("tp-math-prime", "350.0", "10.0"), {{ min: "120.0", max: "350.0" }}),
  "tp-math-clause": Object.assign(new El("tp-math-clause", "32", "4"), {{ min: "8", max: "64" }}),
  "tp-math-prime-val": new El("tp-math-prime-val", "", "1", "350.0 kW"),
  "tp-math-clause-val": new El("tp-math-clause-val", "", "1", "32 modes"),
  "tp-inline-prime": new El("tp-inline-prime", "", "1", "MGU-K Peak Electric Power = 350.0 kW"),
  "tp-readout-barrier": new El("tp-readout-barrier", "", "1", "FIXED_0"),
  "tp-readout-flux": new El("tp-readout-flux", "", "1", "FIXED_1"),
  "tp-readout-eth": new El("tp-readout-eth", "", "1", "FIXED_2"),
  "tp-readout-qed-box": new El("tp-readout-qed-box"),
  "tp-readout-qed": new El("tp-readout-qed", "", "1", "FIXED_3"),
  "tp-m07-pk-text": new El("tp-m07-pk-text", "", "1", "PMP Co-State Taper (P_k = 350.0 kW → Convex-Loss Arc)"),
  "tp-m07-modes-text": new El("tp-m07-modes-text", "", "1", "32 Modes"),
}};
const plateEl = new El("tp-m07-plate");
plateEl.querySelector = (sel) => (sel === "svg.tp-svg-stage" ? svgStage : null);
plateEl.querySelectorAll = (sel) => {{
  if (sel.includes('input[type="range"]')) return [nodes["tp-math-prime"], nodes["tp-math-clause"]];
  return [];
}};
globalThis.requestAnimationFrame = () => 0;
globalThis.cancelAnimationFrame = () => {{}};
globalThis.window = {{
  location: {{ pathname: "/math/m07/" }},
  addEventListener() {{}},
  matchMedia() {{ return {{ matches: false, addEventListener() {{}} }}; }},
}};
globalThis.document = {{
  documentElement: {{ dataset: {{}}, getAttribute: () => "en" }},
  body: {{ dataset: {{ folioSlug: "m07" }}, getAttribute: (k) => (k === "data-folio-slug" ? "m07" : null) }},
  addEventListener() {{}},
  createElementNS: (_ns, tag) => new El(tag),
  getElementById: (id) => nodes[id] || null,
  querySelector(sel) {{
    if (sel === "[data-folio-slug]") return {{ getAttribute: () => "m07" }};
    if (sel === 'label[for="tp-math-prime"] span') return {{ textContent: "MGU-K Peak Electric Power (P_k)" }};
    return null;
  }},
  querySelectorAll: (sel) => (sel === ".tp-plate" ? [plateEl] : []),
}};
const {{ initPlateSolvers }} = await import({json.dumps(solvers_uri)});
initPlateSolvers();
const snapshots = [];
for (const [p, k] of [["120", "8"], ["240", "32"], ["350", "64"]]) {{
  nodes["tp-math-prime"].value = p;
  nodes["tp-math-clause"].value = k;
  nodes["tp-math-prime"].dispatch("input");
  nodes["tp-math-clause"].dispatch("input");
  snapshots.push({{
    pVal: nodes["tp-math-prime-val"].textContent,
    cVal: nodes["tp-math-clause-val"].textContent,
    inlineP: nodes["tp-inline-prime"].textContent,
    pkSvg: nodes["tp-m07-pk-text"].textContent,
    modesSvg: nodes["tp-m07-modes-text"].textContent,
    clipTransform: clipCurve.getAttribute("transform"),
    pmpTransform: pmpCurve.getAttribute("transform"),
    unmarkedTransform: unmarkedCurve.getAttribute("transform"),
    readouts: [
      nodes["tp-readout-barrier"].textContent,
      nodes["tp-readout-flux"].textContent,
      nodes["tp-readout-eth"].textContent,
      nodes["tp-readout-qed"].textContent,
    ],
  }});
}}
console.log(JSON.stringify(snapshots));
"""
        proc = subprocess.run(
            cmd_prefix + ["--input-type=module", "-e", js_harness],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
            timeout=20,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        snaps = json.loads(proc.stdout.strip())
        self.assertEqual(snaps[0]["pVal"], "120.0 kW")
        self.assertEqual(snaps[0]["cVal"], "8 modes")
        self.assertEqual(snaps[0]["pkSvg"], "PMP Co-State Taper (P_k = 120.0 kW → Convex-Loss Arc)")
        self.assertEqual(snaps[0]["modesSvg"], "8 Modes")
        self.assertEqual(snaps[2]["pVal"], "350.0 kW")
        self.assertEqual(snaps[2]["cVal"], "64 modes")
        self.assertEqual(snaps[2]["modesSvg"], "64 Modes")
        for snap in snaps:
            self.assertIsNone(snap["clipTransform"])
            self.assertIsNone(snap["pmpTransform"])
            self.assertIsNotNone(snap["unmarkedTransform"])
            self.assertEqual(snap["readouts"], ["FIXED_0", "FIXED_1", "FIXED_2", "FIXED_3"])

    def test_m07_boundaries_and_unit_formatting_in_built_artifacts(self) -> None:
        self.assertEqual(m07.FOLIO["current_edition"], "REV 1.1")
        self.assertFalse(any((SKILLS / "math" / "m07").glob("verify_*.py")))

        en_html = _main_html((SRC / "math" / "m07" / "index.html").read_text(encoding="utf-8"))
        es_html = _main_html((SRC / "es-mx" / "math" / "m07" / "index.html").read_text(encoding="utf-8"))
        skill_md = (SKILLS / "math" / "m07" / "SKILL.md").read_text(encoding="utf-8")
        seo_tuple = " ".join(FOLIO_SEO["m07"])

        for blob_name, blob in (
            ("en_html", en_html),
            ("es_html", es_html),
            ("skill_md", skill_md),
            ("seo_tuple", seo_tuple),
        ):
            low = blob.lower()
            self.assertNotIn("design study", low, blob_name)
            self.assertNotIn("estudio de diseño", low, blob_name)
            self.assertNotIn("fia 2026 art. 5", low, blob_name)
            self.assertNotIn("banach-space", low, blob_name)
            self.assertNotIn("blind from an accident", low, blob_name)
            self.assertNotIn("race engineers compute", low, blob_name)
            self.assertNotIn("typically", low, blob_name)

        self.assertIn("not a vehicle design method", en_html.lower())
        self.assertIn("not independently verified", en_html.lower())
        self.assertIn("no un método de diseño vehicular", es_html.lower())
        self.assertIn("sustitutos neuronales propuestos", seo_tuple.lower())
        self.assertNotIn("cystic fibrosis", en_html.lower())
        self.assertNotIn("fibrosis quística", es_html.lower())
        self.assertIn("+0.42 s slower, illustrative", en_html)
        self.assertIn("not as a vehicle, battery, or powertrain controller design method", skill_md.lower())
        self.assertIn("<code>350.0 kW</code>", en_html)
        self.assertIn("<code>32 modes</code>", en_html)
        self.assertNotIn(" kW350", en_html)
        self.assertNotIn(" modes32", en_html)
        self.assertEqual(en_html.count('data-custom-curve="1"'), 2)
        self.assertIn("Source Module: tools/folios/math/m07.py", en_html)
        self.assertNotIn("Deterministic Kernel: tools/folios/math/m07.py", en_html)
        self.assertIn("expone la relación gobernante", en_html)
        self.assertNotIn("verifica la ley gobernante", en_html)
        self.assertIn("inspeccionar los controles y las cifras de referencia", en_html)
        self.assertNotIn("executable mathematical and physical treatise", en_html.lower())
        self.assertIn("λ_e* / η_k ≤ λ_v / (m · v) ≤ λ_e* · η_regen", en_html.lower())
        self.assertNotIn("λ_e* · η_regen ≤ λ_v", en_html.lower())
        self.assertIn("lambda_e* / eta_k <= lambda_v / (m * v) <= lambda_e* * eta_regen", skill_md.lower())
        self.assertNotIn("lambda_e* * eta_regen <= lambda_v", skill_md.lower())


if __name__ == "__main__":
    unittest.main()
