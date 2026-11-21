"""The site build must not write into sibling repositories unless it is asked to."""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import build_longform_folios as builder  # noqa: E402


class TestNoSiblingWrites(unittest.TestCase):
    def test_sibling_sync_is_off_unless_the_flag_is_given(self):
        self.assertFalse(builder.SYNC_SIBLINGS)                  # the test runner was not started with --sync-siblings

    def test_the_only_write_outside_the_repository_is_behind_the_flag(self):
        source = (ROOT / "tools" / "build_longform_folios.py").read_text(encoding="utf-8")
        block = source[source.index("sibling_map = {}"):]
        block = block[: block.index("return catalog")]
        self.assertRegex(block, r"if SYNC_SIBLINGS and \"\.worktrees\" not in ROOT\.parts:")
        self.assertEqual(len(re.findall(r"ROOT\.parent\s*/", source)), len(re.findall(r"ROOT\.parent\s*/", block)),
                         "a path outside the repository is built somewhere other than the guarded sibling block")

    def test_a_default_build_of_the_catalog_leaves_siblings_untouched(self):
        import subprocess
        siblings = [ROOT.parent / name / "folios" / "catalog.json" for name in ("math", "physics", "architecture", "engineering")]
        before = {p: (p.read_bytes() if p.is_file() else None) for p in siblings}
        builder.update_catalogs()
        for p in siblings:
            self.assertEqual(before[p], p.read_bytes() if p.is_file() else None, str(p))
        subprocess.run(["git", "-C", str(ROOT), "checkout", "--", "src/data/magazine_catalog.json"], check=False)


if __name__ == "__main__":
    unittest.main()
