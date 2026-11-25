#!/usr/bin/env python3
"""Parity, isolated negative-control, and browser JS solver tests for Mathematics Folio M.16."""
from __future__ import annotations

import importlib.util
import json
import math
import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from folios.math import m16 as m16_folio  # noqa: E402

VERIFIER_PATH = ROOT / "skills" / "math" / "m16" / "verify_m16_progression_bounds.py"
_spec = importlib.util.spec_from_file_location("verify_m16", VERIFIER_PATH)
assert _spec is not None and _spec.loader is not None
v_m16 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v_m16)


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


class M16VerifierAndSolverParityTests(unittest.TestCase):
    def test_exact_r3_sequence_behrend_shells_and_cyclic_fourier_identities(self) -> None:
        ok, report, failures = v_m16.run_verification(planted_defect=False)
        self.assertTrue(ok, f"Unexpected verifier failures: {failures}")
        self.assertEqual(report["status"], "PASS")
        self.assertTrue(report["input_guards_ok"])
        self.assertLess(report["max_dft_abs_error"], 1e-12)

        expected_r3 = {
            1: 1, 2: 2, 3: 2, 4: 3, 5: 4, 6: 4, 7: 4, 8: 4,
            9: 5, 10: 5, 11: 6, 12: 6, 13: 7, 14: 8, 15: 8, 16: 8,
            17: 8, 18: 8, 19: 8, 20: 9, 21: 9, 22: 9, 23: 9, 24: 10,
        }
        self.assertEqual(report["r3_1_to_24"], expected_r3)
        self.assertEqual(report["witness_n9"], [1, 2, 4, 8, 9])
        self.assertEqual(report["witness_n20"], [1, 2, 6, 7, 9, 14, 15, 18, 20])
        self.assertEqual(report["witness_n24"], [1, 2, 5, 7, 11, 16, 18, 19, 23, 24])

        d5m4 = report["default_slider_d5_m4"]
        self.assertEqual(d5m4["radix"], 9)
        self.assertEqual(d5m4["ambient_n"], 6561)
        self.assertEqual(d5m4["total_grid_vectors"], 625)
        self.assertEqual(d5m4["shell_count"], 65)
        self.assertEqual(d5m4["modal_r2"], 18)
        self.assertEqual(d5m4["modal_shell_size"], 30)
        self.assertEqual(d5m4["pigeonhole_floor"], 10)
        self.assertEqual(d5m4["cantor_base3_size"], 256)

        d8m6 = report["grid_highlights"]["d8_m6"]
        self.assertEqual(d8m6["ambient_n"], 11390625)
        self.assertEqual(d8m6["modal_r2"], 103)
        self.assertEqual(d8m6["modal_shell_size"], 3300)
        self.assertEqual(d8m6["pigeonhole_floor"], 889)
        self.assertEqual(d8m6["cantor_base3_size"], 32768)

        f14 = report["fourier_n14_cantor"]
        self.assertEqual(f14["modulus_m"], 29)
        self.assertEqual(f14["exact_ordered_triples"], 8)
        self.assertLess(f14["dft_abs_error"], 1e-12)
        self.assertAlmostEqual(f14["max_nonzero_fourier"], 4.229546, places=5)
        self.assertAlmostEqual(f14["roth_linear_bias_floor"], 35.0 / 21.0, places=6)
        self.assertAlmostEqual(f14["parseval_rms_floor"], math.sqrt(6.0), places=6)

        f20 = report["fourier_n20_extremal"]
        self.assertEqual(f20["modulus_m"], 41)
        self.assertEqual(f20["exact_ordered_triples"], 9)
        self.assertLess(f20["dft_abs_error"], 1e-12)
        self.assertAlmostEqual(f20["max_nonzero_fourier"], 5.146830, places=5)
        self.assertAlmostEqual(f20["roth_linear_bias_floor"], 40.0 / 32.0, places=6)
        self.assertAlmostEqual(f20["parseval_rms_floor"], math.sqrt((9.0 * 32.0) / 40.0), places=6)

    def test_four_isolated_negative_controls_and_strict_input_validation(self) -> None:
        # 1. Base b = d carry knockout ALONE on genuine quadratic shell ||x||_2^2 = 5 at (d = 3, m = 3)
        good_b33 = v_m16.construct_behrend_set(3, 3, radix_override=5, use_l1_norm=False)
        self.assertEqual(good_b33["modal_level"], 5)
        self.assertEqual(good_b33["shell_vector_count"], 6)
        self.assertEqual(good_b33["elements_sample"], [8, 12, 28, 36, 52, 56])
        self.assertEqual(good_b33["nontrivial_3ap_count"], 0)

        bad_carry_only = v_m16.construct_behrend_set(3, 3, planted_defect=True, use_l1_norm=False)
        self.assertEqual(bad_carry_only["radix"], 3)
        self.assertEqual(bad_carry_only["modal_level"], 5)
        self.assertEqual(bad_carry_only["elements_sample"], [6, 8, 12, 16, 20, 22])
        self.assertEqual(bad_carry_only["nontrivial_3ap_count"], 2)

        # 2. Flat L^1 hyperplane knockout ALONE in carry-free base b = 2d - 1 = 5 at (d = 3, m = 3)
        bad_l1_only = v_m16.construct_behrend_set(3, 3, radix_override=5, use_l1_norm=True)
        self.assertEqual(bad_l1_only["modal_level"], 3)
        self.assertEqual(bad_l1_only["shell_vector_count"], 7)
        self.assertGreater(bad_l1_only["nontrivial_3ap_count"], 0)

        # 3. Cyclic DFT conj(A_hat(r)) frequency mismatch ALONE
        bad_dft = v_m16.verify_cyclic_fourier_identity(v_m16.cantor_base3_set(14), 14, planted_defect=True)
        self.assertGreater(bad_dft["dft_abs_error"], 1.0)

        # 4. Step-1 3-AP omission in r_3(N) search ALONE
        bad_r3, bad_wit = v_m16.compute_exact_r3_sequence(9, planted_defect=True)
        self.assertGreater(bad_r3[3], 2)
        self.assertGreater(v_m16.count_nontrivial_3aps(bad_wit[3]), 0)

        # 5. CLI --planted-defect exits non-zero and reports FAIL in JSON across all 4 mechanisms
        cli_bad = subprocess.run(
            [sys.executable, "-X", "utf8", str(VERIFIER_PATH), "--planted-defect"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=30,
        )
        self.assertNotEqual(cli_bad.returncode, 0)
        payload = json.loads(cli_bad.stdout)
        self.assertEqual(payload["status"], "FAIL")
        self.assertGreaterEqual(payload["failure_count"], 4)

        # 6. Strict input validation raises named ValueErrors
        with self.assertRaisesRegex(ValueError, r"digit_d must be an integer"):
            v_m16.evaluate_behrend_slider(True, 4)
        with self.assertRaisesRegex(ValueError, r"digit_d must lie in \[2, 8\]"):
            v_m16.evaluate_behrend_slider(9, 4)
        with self.assertRaisesRegex(ValueError, r"dim_m must lie in \[2, 6\]"):
            v_m16.evaluate_behrend_slider(5, 1)
        with self.assertRaisesRegex(ValueError, r"radix_override must be an integer >= 2"):
            v_m16.construct_behrend_set(3, 3, radix_override=1)
        with self.assertRaisesRegex(ValueError, r"subset must be a non-empty subset"):
            v_m16.verify_cyclic_fourier_identity([0, 2], 5)
        with self.assertRaisesRegex(ValueError, r"subset elements must be integers"):
            v_m16.verify_cyclic_fourier_identity([True, 2], 5)
        with self.assertRaisesRegex(ValueError, r"subset elements must be integers"):
            v_m16.verify_cyclic_fourier_identity([1.5, 2.5], 5)  # type: ignore[list-item]

    def test_browser_solvers_mjs_matches_python_verifier_and_folio_readouts_across_grid(self) -> None:
        found = _find_node_cmd()
        if found is None:
            self.skipTest("No Node/Electron runtime available for solvers.mjs parity check")
        cmd_prefix, env = found
        solvers_uri = (ROOT / "src" / "modules" / "solvers.mjs").resolve().as_uri()
        cases = [(2, 2), (2, 3), (3, 3), (5, 4), (6, 5), (8, 6)]
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
  'tp-math-prime': new El('tp-math-prime', '5'),
  'tp-math-clause': new El('tp-math-clause', '4'),
  'tp-math-prime-val': new El('tp-math-prime-val'),
  'tp-math-clause-val': new El('tp-math-clause-val'),
  'tp-inline-prime': new El('tp-inline-prime'),
  'tp-readout-barrier': new El('tp-readout-barrier'),
  'tp-readout-flux': new El('tp-readout-flux'),
  'tp-readout-eth': new El('tp-readout-eth'),
  'tp-readout-qed-box': new El('tp-readout-qed-box'),
  'tp-readout-qed': new El('tp-readout-qed'),
  'tp-m16-shell-curve': new El('tp-m16-shell-curve'),
  'tp-m16-pigeon-line': new El('tp-m16-pigeon-line'),
  'tp-m16-shell-bar': new El('tp-m16-shell-bar'),
  'tp-m16-cantor-bar': new El('tp-m16-cantor-bar'),
  'tp-m16-point': new El('tp-m16-point'),
  'tp-m16-status-lbl': new El('tp-m16-status-lbl'),
}};
globalThis.window = {{ location: {{ pathname: '/math/m16/' }}, addEventListener() {{}} }};
globalThis.document = {{
  documentElement: {{ dataset: {{}}, getAttribute: () => 'en' }},
  body: {{ dataset: {{}}, getAttribute: (k) => (k === 'data-folio-slug' ? 'm16' : null) }},
  addEventListener() {{}},
  getElementById: (id) => nodes[id] || null,
  querySelector: (sel) => (sel === '[data-folio-slug]' ? {{ getAttribute: () => 'm16' }} : null),
  querySelectorAll: () => [],
}};
const {{ initPlateSolvers }} = await import({json.dumps(solvers_uri)});
initPlateSolvers();
const cases = {json.dumps(cases)};
const out = {{}};
for (const [d, m] of cases) {{
  nodes['tp-math-prime'].value = String(d);
  nodes['tp-math-clause'].value = String(m);
  nodes['tp-math-prime'].listeners['input']();
  out[`${{d}}_${{m}}`] = {{
    pLabel: nodes['tp-math-prime-val'].textContent,
    cLabel: nodes['tp-math-clause-val'].textContent,
    r0: nodes['tp-readout-barrier'].textContent,
    r1: nodes['tp-readout-flux'].textContent,
    r2: nodes['tp-readout-eth'].textContent,
    r3: nodes['tp-readout-qed'].textContent,
    alert: nodes['tp-readout-qed-box'].getAttribute('data-alert'),
    status: nodes['tp-m16-status-lbl'].textContent,
    curveD: nodes['tp-m16-shell-curve'].getAttribute('d'),
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

        folio_ro = [r["value"] for r in m16_folio.FOLIO["readouts"]]
        def_js = js_map["5_4"]
        self.assertEqual([def_js["r0"], def_js["r1"], def_js["r2"], def_js["r3"]], folio_ro)

        for d, m in cases:
            py_ev = v_m16.evaluate_behrend_slider(d, m)
            got = js_map[f"{d}_{m}"]
            self.assertEqual(got["pLabel"], f"d = {d}")
            self.assertEqual(got["cLabel"], f"m = {m}")
            self.assertEqual(
                got["r0"],
                f"|B({d}, {m})| = {py_ev['modal_shell_size']:,} on R*² = {py_ev['modal_r2']} "
                f"(in N = {py_ev['ambient_n']:,}, base {py_ev['radix']})",
            )
            self.assertEqual(
                got["r1"],
                f"Pigeonhole ≥ {py_ev['pigeonhole_floor']:,} ({py_ev['total_grid_vectors']:,} / "
                f"{py_ev['shell_count']} shells) · Cantor C_3({py_ev['ambient_n']:,}) = {py_ev['cantor_base3_size']:,}",
            )
            self.assertEqual(
                got["r2"],
                "r_3(9) = 5, r_3(14) = 8, r_3(20) = 9, r_3(24) = 10 · max |Â(r)| = 5.15 at N = 20 (M = 41)",
            )
            self.assertEqual(got["r3"], "OPEN EXPONENT GAP β ∈ [1/9, 1/2] · FINITE CROSSOVER REGIME")
            self.assertEqual(
                got["status"],
                f"d = {d}, m = {m} (b = {py_ev['radix']}): |B| = {py_ev['modal_shell_size']:,} "
                f"at R*² = {py_ev['modal_r2']} · C_3 = {py_ev['cantor_base3_size']:,}",
            )
            self.assertEqual(got["alert"], "true")
            self.assertTrue(got["curveD"].startswith("M 56 "))


if __name__ == "__main__":
    unittest.main()
