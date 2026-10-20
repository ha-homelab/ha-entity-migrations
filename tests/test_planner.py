import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ha_entity_migrations import __version__
from ha_entity_migrations.i18n import CATALOGS, LANGUAGES, ROWS
from ha_entity_migrations.io import (
    MAX_BYTES,
    InputError,
    parse_json,
    read_regular,
    resolve,
    source_path,
)
from ha_entity_migrations.planner import load_plan, plan

ROOT = Path(__file__).resolve().parents[1]


def fixture(name="domain-change"):
    root = ROOT / "examples" / name
    manifest = json.loads((root / "manifest.json").read_text())
    raw = (root / "snapshot.json").read_bytes()
    source = (root / "automations.json").read_bytes()
    return (
        manifest,
        json.loads(raw),
        {"automations.json": (source, json.loads(source))},
        hashlib.sha256(raw).hexdigest(),
    )


def codes(result):
    return {item["code"] for item in result["diagnostics"]}


class PlannerTests(unittest.TestCase):
    def test_report_identifies_running_package_version(self):
        self.assertEqual(plan(*fixture())["tool_version"], __version__)

    def test_role_moved_off_repurposed_hardware(self):
        data = fixture("role-swap")
        result = plan(*data)
        self.assertEqual(result["status"], "ready")
        self.assertFalse(any(edit.get("after") == "switch.pump_enable" for edit in result["edits"]))
        self.assertEqual(result["assignments"][0]["entity_id"], "switch.pump_enable")
        self.assertEqual(result["edits"][0]["operation"], "remove_consumer")

    def test_follows_hardware_cannot_silently_turn_lights_off_to_pump_off(self):
        m, s, docs, digest = fixture("role-swap")
        m["consumers"][0]["policy"] = "follows_hardware"
        result = plan(m, s, docs, digest)
        self.assertEqual(result["status"], "blocked")
        self.assertIn("role_not_allowed", codes(result))

    def test_domain_change_updates_reference_and_own_service(self):
        result = plan(*fixture())
        self.assertEqual(result["status"], "ready")
        self.assertEqual(
            {edit["after"] for edit in result["edits"]}, {"switch.table", "switch.turn_off"}
        )

    def test_destination_collision(self):
        m, s, docs, digest = fixture("role-swap")
        m["assignments"][1]["entity_id"] = "switch.pump_enable"
        result = plan(m, s, docs, digest)
        self.assertIn("destination_collision", codes(result))
        self.assertEqual(result["edits"], [])

    def test_duplicate_hardware_assignment(self):
        m, s, docs, digest = fixture()
        m["assignments"] *= 2
        self.assertIn("assignment_collision", codes(plan(m, s, docs, digest)))

    def test_snapshot_collision(self):
        m, s, docs, digest = fixture()
        s["entities"] *= 2
        self.assertIn("source_collision", codes(plan(m, s, docs, digest)))

    def test_unknown_hardware(self):
        m, s, docs, digest = fixture()
        m["assignments"][0]["hardware_id"] = "absent"
        self.assertIn("unknown_hardware", codes(plan(m, s, docs, digest)))

    def test_stale_snapshot_never_emits_candidate_edits(self):
        m, s, docs, _ = fixture()
        result = plan(m, s, docs, "0" * 64)
        self.assertIn("stale_snapshot", codes(result))
        self.assertEqual(result["edits"], [])

    def test_stale_source(self):
        m, s, docs, digest = fixture()
        m["sources"]["automations.json"] = "0" * 64
        self.assertIn("stale_source", codes(plan(m, s, docs, digest)))

    def test_template_is_blocked_not_executed(self):
        self.assertIn("dynamic_reference", codes(plan(*fixture("blocked-template"))))

    def test_template_keys_and_entity_keys_are_unresolved(self):
        for key, expected in [
            ("{{ dynamic_key }}", "dynamic_reference"),
            ("light.table", "embedded_reference"),
        ]:
            m, s, docs, digest = fixture()
            docs["automations.json"][1][0][key] = "value"
            self.assertIn(expected, codes(plan(m, s, docs, digest)))

    def test_direct_script_service_is_not_silently_ignored(self):
        m, s, docs, digest = fixture()
        docs["automations.json"][1].append({"action": "script.unmodeled"})
        self.assertIn("unmodeled_reference", codes(plan(m, s, docs, digest)))

    def test_no_policy_is_not_success(self):
        m, s, docs, digest = fixture()
        m["consumers"] = []
        self.assertIn("missing_policy", codes(plan(m, s, docs, digest)))

    def test_retirement_cannot_remove_unrelated_actions(self):
        m, s, docs, digest = fixture("role-swap")
        docs["automations.json"][1][1]["other"] = "light.workbench"
        self.assertIn("retire_scope_mixed", codes(plan(m, s, docs, digest)))

    def test_capability_guard(self):
        m, s, docs, digest = fixture()
        m["consumers"][0]["required_capabilities"] = ["brightness"]
        self.assertIn("capability_missing", codes(plan(m, s, docs, digest)))

    def test_data_and_brightness_not_carried_to_switch(self):
        m, s, docs, digest = fixture()
        docs["automations.json"][1][0]["actions"][0]["data"] = {"brightness_pct": 70}
        self.assertIn("service_data_review", codes(plan(m, s, docs, digest)))

    def test_mixed_targets_not_given_single_new_domain(self):
        m, s, docs, digest = fixture()
        action = docs["automations.json"][1][0]["actions"][0]
        action["target"]["entity_id"] = ["light.table", "light.other"]
        m["consumers"][0]["pointer"] += "/0"
        self.assertIn("mixed_action_targets", codes(plan(m, s, docs, digest)))

    def test_display_domain_needs_features_review(self):
        m, s, docs, digest = fixture()
        m["consumers"][0]["kind"] = "display"
        del m["consumers"][0]["service_pointer"]
        self.assertIn("display_domain_review", codes(plan(m, s, docs, digest)))

    def test_indirect_targets_and_unknown_references(self):
        m, s, docs, digest = fixture()
        action = docs["automations.json"][1][0]["actions"][0]
        action["target"]["area_id"] = "synthetic_room"
        action["extra"] = "sensor.unmodeled"
        result = plan(m, s, docs, digest)
        self.assertTrue({"indirect_target", "unmodeled_reference"} <= codes(result))

    def test_input_not_mutated_and_deterministic(self):
        data = fixture()
        old = copy.deepcopy(data)
        first = plan(*data)
        self.assertEqual(data, old)
        self.assertEqual(first, plan(*data))

    def test_invalid_types_return_input_error(self):
        for field, value in [
            ("file", []),
            ("kind", {}),
            ("policy", []),
            ("required_capabilities", 3),
        ]:
            with self.subTest(field=field):
                data = fixture()
                data[0]["consumers"][0][field] = value
                with self.assertRaises(InputError):
                    plan(*data)

    def test_load_examples(self):
        for name, status in [
            ("role-swap", "ready"),
            ("domain-change", "ready"),
            ("blocked-template", "blocked"),
        ]:
            root = ROOT / "examples" / name
            self.assertEqual(
                load_plan(root / "manifest.json", root / "snapshot.json", root)["status"], status
            )


class InputTests(unittest.TestCase):
    def alias_fixture(self, root, second_name, *, hardlink=False, separate=False):
        manifest, snapshot, sources, _ = fixture()
        raw = sources["automations.json"][0]
        (root / "sub").mkdir()
        original = root / "sub/config.json"
        original.write_bytes(raw)
        if hardlink:
            os.link(original, root / second_name)
        elif separate:
            (root / second_name).write_bytes(raw)
        first_name = "sub/config.json"
        manifest["sources"] = {
            first_name: hashlib.sha256(raw).hexdigest(),
            second_name: hashlib.sha256(raw).hexdigest(),
        }
        consumer = manifest["consumers"][0]
        manifest["consumers"] = [dict(consumer, file=first_name), dict(consumer, file=second_name)]
        snapshot_raw = json.dumps(snapshot).encode()
        manifest["snapshot_sha256"] = hashlib.sha256(snapshot_raw).hexdigest()
        (root / "snapshot.json").write_bytes(snapshot_raw)
        (root / "manifest.json").write_text(json.dumps(manifest))

    def test_repeated_separator_source_alias_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.alias_fixture(root, "sub//config.json")
            with self.assertRaises(InputError) as caught:
                load_plan(root / "manifest.json", root / "snapshot.json", root)
            self.assertEqual(caught.exception.code, "duplicate_source")

    @unittest.skipUnless(hasattr(os, "link"), "hard links unavailable")
    def test_hardlink_source_alias_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.alias_fixture(root, "sub/alias.json", hardlink=True)
            with self.assertRaises(InputError) as caught:
                load_plan(root / "manifest.json", root / "snapshot.json", root)
            self.assertEqual(caught.exception.code, "duplicate_source")

    def test_case_alias_is_rejected_on_case_insensitive_filesystem(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.alias_fixture(root, "sub/CONFIG.json")
            if not (root / "sub/CONFIG.json").exists():
                self.skipTest("filesystem is case-sensitive")
            with self.assertRaises(InputError) as caught:
                load_plan(root / "manifest.json", root / "snapshot.json", root)
            self.assertEqual(caught.exception.code, "duplicate_source")

    def test_equal_content_in_independent_files_is_not_an_alias(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.alias_fixture(root, "sub/copy.json", separate=True)
            report = load_plan(root / "manifest.json", root / "snapshot.json", root)
            self.assertEqual(report["status"], "ready")
            self.assertEqual(len(report["edits"]), 4)
            self.assertEqual(
                {edit["file"] for edit in report["edits"]}, {"sub/config.json", "sub/copy.json"}
            )

    def test_duplicate_nonfinite_and_excessive_depth(self):
        for raw in [
            b'{"a":1,"a":2}',
            b'{"a":NaN}',
            b'{"a":1e999}',
            ("[" * 45 + "0" + "]" * 45).encode(),
            b'"\xff"',
        ]:
            with self.subTest(raw=raw[:30]), self.assertRaises(InputError):
                parse_json(raw)

    def test_pointer_escaping_and_bad_indices(self):
        self.assertEqual(resolve({"a/b": {"~": 5}}, "/a~1b/~0"), 5)
        for pointer in ["/00", "/-1", "/-", "/~3", "/9"]:
            with self.assertRaises(InputError):
                resolve([1], pointer)

    def test_traversal_symlink_oversize_and_fifo(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ["../outside", "/etc/passwd", "sub/../inside", "sub\\inside"]:
                with self.assertRaises(InputError):
                    source_path(root, name)
            target = root / "target"
            target.write_text("{}")
            (root / "link").symlink_to(target)
            with self.assertRaises(InputError):
                read_regular(root / "link")
            with self.assertRaises(InputError):
                source_path(root, "link")
            target.write_bytes(b"x" * (MAX_BYTES + 1))
            with self.assertRaises(InputError):
                read_regular(target)
            if hasattr(os, "mkfifo"):
                os.mkfifo(root / "pipe")
                with self.assertRaises(InputError):
                    read_regular(root / "pipe")


class CliTests(unittest.TestCase):
    def call(self, *args):
        return subprocess.run(
            [sys.executable, "-m", "ha_entity_migrations", *args],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

    def test_exit_codes_and_translation(self):
        for lang in LANGUAGES:
            for name, code in [("domain-change", 0), ("blocked-template", 3)]:
                root = ROOT / "examples" / name
                result = self.call(
                    "--lang",
                    lang,
                    "plan",
                    "--manifest",
                    str(root / "manifest.json"),
                    "--snapshot",
                    str(root / "snapshot.json"),
                    "--root",
                    str(root),
                )
                self.assertEqual(result.returncode, code, result.stderr)
                doc = json.loads(result.stdout)
                self.assertEqual(doc["language"], lang)
                self.assertEqual(doc["summary"], CATALOGS[lang][doc["status"]])
                if code:
                    self.assertEqual(
                        doc["diagnostics"][0]["message"], CATALOGS[lang]["dynamic_reference"]
                    )

    def test_invalid_input_exit_two(self):
        result = self.call(
            "plan", "--manifest", "/absent", "--snapshot", "/absent", "--root", "/absent"
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["status"], "invalid")

    def test_i18n_parity_and_help(self):
        for lang in LANGUAGES:
            self.assertEqual(set(CATALOGS[lang]), set(ROWS))
            self.assertTrue(all(CATALOGS[lang].values()))
            result = self.call("--lang", lang, "--help")
            self.assertEqual(result.returncode, 0)
            self.assertIn(CATALOGS[lang]["description"], result.stdout)
        self.assertEqual(len({CATALOGS[lang]["blocked"] for lang in LANGUAGES}), 4)


if __name__ == "__main__":
    unittest.main()
