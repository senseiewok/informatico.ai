"""Deterministic unit tests for anti-chimera integrity and bibliography citation gates."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import check_folio_citations  # noqa: E402
import check_toolchain_claims  # noqa: E402


class AntiChimeraAndCitationGateTests(unittest.TestCase):
    def test_repo_has_zero_regex_substitution_chimeras(self) -> None:
        errors: list[str] = []
        check_toolchain_claims.check_no_regex_chimeras(ROOT, errors)
        self.assertEqual(errors, [])

    def test_anti_chimera_check_fails_on_all_planted_chimeras(self) -> None:
        planted_samples = (
            "Cryo-EM structure of F508del-CSI-MasterFormat (PDB 8EIQ).",
            "Accelerating 4.5 kb CSI-MasterFormat mRNA delivery.",
            "Transport across ventilation duct viscoplastic grout.",
            "Restoring CSI-MasterFormat gating at PDB 8EIQ.",
            "Threading a CSI-MasterFormat polyplex through nanopores.",
            "Hydrated epithelium requires CSI-MasterFormat chloride transport.",
            "Aerosol tracheotubular deposition across Tubular Generations 4-16.",
            "Avoiding ventilation duct irritants that trigger bronchospasm.",
            "Hidrogeles de mucina en Ingeniería Hidrosanitaria.",
            "In Non-Equilibrium Statistical Biophysics, the F508del transmembrane channel misfolds.",
        )
        for idx, sample in enumerate(planted_samples):
            with self.subTest(sample=sample):
                with tempfile.TemporaryDirectory() as tmp:
                    tmp_path = Path(tmp)
                    (tmp_path / f"sample_{idx}.txt").write_text(sample, encoding="utf-8")
                    errors: list[str] = []
                    check_toolchain_claims.check_no_regex_chimeras(tmp_path, errors)
                    self.assertGreater(
                        len(errors),
                        0,
                        f"Expected check_no_regex_chimeras to reject: {sample!r}",
                    )

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "multiline_folio.py").write_text(
                'ESSAY = {"bridge": (\n    "F508del-"\n    "CSI-MasterFormat"\n)}\n',
                encoding="utf-8",
            )
            errors_ml: list[str] = []
            check_toolchain_claims.check_no_regex_chimeras(tmp_path, errors_ml)
            self.assertGreater(len(errors_ml), 0, "Expected AST multi-line literal chimera detection")

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "bad_utf8.txt").write_bytes(b"\xff\xfe" + "F508del-CSI-MasterFormat".encode("utf-16le"))
            errors_enc: list[str] = []
            check_toolchain_claims.check_no_regex_chimeras(tmp_path, errors_enc)
            self.assertGreater(len(errors_enc), 0, "Expected invalid UTF-8 file to fail closed")

    def test_anti_chimera_check_allows_legitimate_structural_prose(self) -> None:
        legit = (
            "CSI MasterFormat Division 03 30 00 cast-in-place concrete and tubular steel column.\n"
            "Separating mechanical ventilation ducts from load-bearing masonry vaults.\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "legit_arch.txt").write_text(legit, encoding="utf-8")
            errors: list[str] = []
            check_toolchain_claims.check_no_regex_chimeras(tmp_path, errors)
            self.assertEqual(errors, [])

    def test_folio_citation_checker_passes_all_60_folios(self) -> None:
        folios = check_folio_citations.load_informatico_folios()
        self.assertEqual(len(folios), 60)
        findings = check_folio_citations.check(folios)
        self.assertEqual(findings, [])

    def test_folio_citation_checker_catches_deliberate_author_and_year_mismatch(self) -> None:
        fake_cache = {
            "doi:10.1017/cbo9781107050310": {
                "found": True,
                "first_author": "Heyman",
                "year": 1995,
                "title": "The Stone Skeleton",
            }
        }
        bad_folio = [
            {
                "id": "A.01-TEST",
                "doi": "10.1017/CBO9781107050310",
                "steps": [],
                "sources": [
                    "Hooke, R. (1675). A Description of Helioscopes. DOI: 10.1017/CBO9781107050310."
                ],
            }
        ]
        findings = check_folio_citations.check(bad_folio, cache=fake_cache)
        self.assertTrue(
            any("SOURCE-YEAR-MISMATCH" in f for f in findings),
            f"Expected SOURCE-YEAR-MISMATCH in {findings}",
        )
        self.assertTrue(
            any("SOURCE-AUTHOR-MISMATCH" in f for f in findings),
            f"Expected SOURCE-AUTHOR-MISMATCH in {findings}",
        )

    def test_claude_security_perimeter_and_agents_md_present(self) -> None:
        settings_path = ROOT / ".claude" / "settings.json"
        self.assertTrue(settings_path.is_file())
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        perms = settings.get("permissions", {})
        self.assertEqual(perms.get("disableBypassPermissionsMode"), "disable")
        deny_rules = perms.get("deny", [])
        self.assertGreaterEqual(len(deny_rules), 180)
        for required_rule in ("Read(.env)", "Bash(git push --force*)", "Read(~/.gemini/config/**)"):
            self.assertIn(required_rule, deny_rules)

        agents_md = ROOT / "AGENTS.md"
        self.assertTrue(agents_md.is_file())
        raw = agents_md.read_bytes()
        self.assertLess(len(raw), 4000)


if __name__ == "__main__":
    unittest.main()
