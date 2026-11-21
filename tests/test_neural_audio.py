"""Offline tests for the narration audio audit in tools/build_neural_audio.py (no speech service, no network)."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import build_neural_audio as audio  # noqa: E402


def mp3_bytes(frames: int, with_id3: bool = False) -> bytes:
    """A synthetic MPEG-2 Layer III stream: 24 kHz, 48 kbit/s, mono, so each frame is 144 bytes and 0.024 s."""
    header = bytes([0xFF, 0xF3, 0x64, 0xC4])
    frame = header + bytes(144 - len(header))
    tag = b"ID3" + bytes([4, 0, 0, 0, 0, 0, 20]) + bytes(20) if with_id3 else b""
    return tag + frame * frames


class TestDuration(unittest.TestCase):
    def test_duration_is_read_from_the_frames(self):
        self.assertAlmostEqual(audio.mp3_duration_seconds(mp3_bytes(1000)), 24.0, places=1)
        self.assertAlmostEqual(audio.mp3_duration_seconds(mp3_bytes(1000, with_id3=True)), 24.0, places=1)

    def test_a_truncated_file_is_shorter_not_trusted(self):
        whole = mp3_bytes(1000)
        self.assertLess(audio.mp3_duration_seconds(whole[: len(whole) // 2]), 12.5)

    def test_bytes_that_are_not_audio_give_none(self):
        self.assertIsNone(audio.mp3_duration_seconds(b"<html>not audio</html>" * 500))
        self.assertIsNone(audio.mp3_duration_seconds(b""))
        self.assertIsNone(audio.mp3_duration_seconds(mp3_bytes(3)))          # too few frames to be a track
        self.assertIsNone(audio.mp3_duration_seconds(b"ID3" + bytes(5000)))  # a tag and nothing else


class TestFindings(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        text = "word " * 80                                                   # 400 characters
        self.item = {"domain": "informatico", "slug": "z99", "folio_id": "Z.99", "en_segments": [text], "es_segments": [text],
                     "en_out": root / "z99-en.mp3", "es_out": root / "z99-es.mp3"}
        self.good = mp3_bytes(1000)                                           # 24 s for 400 characters: about 17 a second

    def tearDown(self):
        self.tmp.cleanup()

    def recorded(self):
        return {"en_text_sha256": audio.text_hash(audio.script_text(self.item, "en"))}

    def test_missing_track(self):
        self.assertEqual(audio.track_findings(self.item, "en", self.recorded()), ["missing"])

    def test_track_that_matches_its_script_has_no_findings(self):
        self.item["en_out"].write_bytes(self.good)
        self.assertEqual(audio.track_findings(self.item, "en", self.recorded()), [])

    def test_script_changed_after_recording_is_stale(self):
        self.item["en_out"].write_bytes(self.good)
        recorded = self.recorded()
        self.item["en_segments"] = ["word " * 79 + "claim "]                  # one word corrected on the page
        self.assertEqual(audio.track_findings(self.item, "en", recorded), ["stale"])

    def test_track_with_no_recorded_hash_is_stale(self):
        self.item["en_out"].write_bytes(self.good)
        self.assertEqual(audio.track_findings(self.item, "en", None), ["stale"])
        self.assertEqual(audio.track_findings(self.item, "en", {"folio_id": "Z.99"}), ["stale"])

    def test_wrong_length_and_unreadable_tracks(self):
        self.item["en_out"].write_bytes(mp3_bytes(60))                        # 1.4 s for 400 characters
        self.assertEqual(audio.track_findings(self.item, "en", self.recorded()), ["duration"])
        self.item["en_out"].write_bytes(mp3_bytes(20000))                     # 8 minutes for 400 characters
        self.assertEqual(audio.track_findings(self.item, "en", self.recorded()), ["duration"])
        self.item["en_out"].write_bytes(b"not an mp3 at all" * 400)
        self.assertEqual(audio.track_findings(self.item, "en", self.recorded()), ["invalid"])

    def test_manifest_entry_records_a_hash_only_for_a_track_that_exists(self):
        self.item["en_out"].write_bytes(self.good)
        entry = audio.manifest_entry(self.item, "audio")
        self.assertEqual(entry["en_text_sha256"], audio.text_hash(audio.script_text(self.item, "en")))
        self.assertAlmostEqual(entry["en_seconds"], 24.0, places=1)
        self.assertNotIn("es_text_sha256", entry)                             # no Spanish file, so nothing claims it is current
        self.assertEqual(entry["en_src"], "audio/z99-en.mp3")


class TestRealSite(unittest.TestCase):
    def test_every_folio_has_a_script_in_both_languages(self):
        items = audio.build_informatico_scripts()
        self.assertGreaterEqual(len(items), 60)
        for item in items:
            for lang in ("en", "es"):
                self.assertGreater(len(audio.script_text(item, lang)), 200, f"{item['slug']} {lang}")

    def test_every_existing_track_parses_and_the_audit_reports_the_rest(self):
        findings, total = audio.audit()
        self.assertEqual(total, 2 * len(audio.build_informatico_scripts()) + 2 * len(audio.build_cf_scripts()))
        for path, found in findings.items():
            self.assertNotIn("invalid", found, path)
            self.assertNotIn("duration", found, path)

    def test_manifest_is_json_and_lists_only_real_folios(self):
        manifest = json.loads((ROOT / "src" / "audio" / "manifest.json").read_text(encoding="utf-8"))
        slugs = {item["slug"] for item in audio.build_informatico_scripts()}
        self.assertTrue(set(manifest["folios"]) <= slugs)


if __name__ == "__main__":
    unittest.main()
