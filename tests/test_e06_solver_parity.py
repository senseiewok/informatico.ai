"""Folio E.06: the numbers the page prints follow from its formulas, and the
safety boundary appears in Act I, the Spanish summary and the skill rules."""
from __future__ import annotations

import math
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.folios.engineering import e06  # noqa: E402

G_MM = 9810.0
T_M = 2.85
B_TABLE = [(0.02, 0.8), (0.05, 1.0), (0.10, 1.2), (0.20, 1.5), (0.30, 1.7), (0.40, 1.9), (0.50, 2.0)]
BOUNDARY_EN = "explanation, not a design method"
BOUNDARY_ES = "no es un método de diseño"


def b_m(beta: float) -> float:
    if not 0.02 <= beta <= 0.50:
        raise ValueError(f"beta_eff out of table range: {beta}")
    for (x0, y0), (x1, y1) in zip(B_TABLE, B_TABLE[1:]):
        if beta <= x1:
            return y0 + (beta - x0) / (x1 - x0) * (y1 - y0)
    raise ValueError("unreachable")


def d_m(sds: float, beta: float) -> float:
    return G_MM * 0.60 * sds * T_M / (4 * math.pi ** 2 * b_m(beta))


def c_s(sds: float, beta: float) -> float:
    return 0.60 * sds / (T_M * b_m(beta))


class E06Numbers(unittest.TestCase):
    def test_default_readouts(self):
        self.assertAlmostEqual(b_m(0.22), 1.54, places=6)
        self.assertAlmostEqual(d_m(1.0, 0.22), 276.0, delta=0.5)
        self.assertAlmostEqual(c_s(1.0, 0.22), 0.137, delta=0.0005)
        values = {r["label"]: r["value"] for r in e06.FOLIO["readouts"]}
        self.assertEqual(values["Isolator Displacement D_M"], f"{d_m(1.0, 0.22):.0f} mm (assumed moat 400 mm)")
        self.assertIn(f"{c_s(1.0, 0.22):.3f}", values["Seismic Base Shear Ratio"])

    def test_prose_numbers(self):
        fixed = 0.60 / 0.65
        iso = 0.60 / T_M
        self.assertAlmostEqual(fixed, 0.92, delta=0.005)
        self.assertAlmostEqual(iso, 0.21, delta=0.005)
        self.assertAlmostEqual(1 - iso / fixed, 0.77, delta=0.005)
        self.assertAlmostEqual(1 - c_s(1.0, 0.22) / fixed, 0.85, delta=0.005)
        lf, es = e06.LONGFORM_DATA, e06.ES_TRANSLATION
        self.assertIn(f"{fixed:.2f} to {c_s(1.0, 0.22):.3f}, about {(1 - c_s(1.0, 0.22) / fixed) * 100:.0f}%", lf["act1_body"])
        self.assertIn(f"{fixed:.2f} g", lf["act1_stakes"])
        self.assertIn(f"{iso:.2f} g", lf["act1_stakes"])
        self.assertIn(f"{fixed:.2f} a {c_s(1.0, 0.22):.3f}", es["deep_es"])
        self.assertIn(f"{d_m(1.0, 0.22):.0f} mm", es["deep_es"])

    def test_walkthrough_thresholds(self):
        # Experiment 1: the moat is first exceeded at the 1.45 g slider step.
        self.assertLessEqual(d_m(1.40, 0.22), 400.0)
        self.assertGreater(d_m(1.45, 0.22), 400.0)
        self.assertAlmostEqual(d_m(1.45, 0.22), 400.1, delta=0.05)
        # Experiment 2: B_M from 8% to 28% damping.
        self.assertAlmostEqual(b_m(0.08), 1.12, places=6)
        self.assertAlmostEqual(b_m(0.28), 1.66, places=6)
        walk = " ".join(e06.LONGFORM_DATA["walkthrough"])
        for token in ("1.45 g", "400.1", "1.12", "1.66"):
            self.assertIn(token, walk)

    def test_b_m_rejects_out_of_range(self):
        with self.assertRaisesRegex(ValueError, "out of table range"):
            b_m(0.6)

    def test_browser_solver_constants(self):
        js = (ROOT / "src" / "modules" / "solvers.mjs").read_text(encoding="utf-8")
        block = js[js.index("const updateE06"):]
        block = block[: block.index("};")]
        self.assertIn("const tM = 2.85;", block)
        self.assertIn("const sd1 = sds * 0.60;", block)
        self.assertIn("dMMm > 400.0", block)
        table = re.search(r"const bTable = (\[\[.*?\]\]);", block).group(1)
        pairs = [tuple(map(float, p)) for p in re.findall(r"\[([\d.]+), ([\d.]+)\]", table)]
        self.assertEqual(pairs, B_TABLE)


class E06Boundary(unittest.TestCase):
    def test_source_boundary(self):
        self.assertIn(BOUNDARY_EN, e06.LONGFORM_DATA["act1_body"])
        self.assertIn(BOUNDARY_ES, e06.ES_TRANSLATION["plain_es"])
        self.assertIn("not a design method", e06.FOLIO["skill"]["rules"][0])

    def test_built_pages_and_skill(self):
        en = (ROOT / "src" / "engineering" / "e06" / "index.html").read_text(encoding="utf-8")
        es = (ROOT / "src" / "es-mx" / "engineering" / "e06" / "index.html").read_text(encoding="utf-8")
        skill = (ROOT / "skills" / "engineering" / "e06" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(BOUNDARY_EN, en)
        self.assertIn(BOUNDARY_ES, es)
        self.assertIn("not a design method", skill)
        for text in (en, es, skill):
            self.assertNotRegex(text, r"(?i)design sketch|screening|recrystalliz")


if __name__ == "__main__":
    unittest.main()
