"""Catalog adoption and publication consistency checks."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ecosystem", ROOT / "tools/ecosystem.py")
ecosystem = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ecosystem)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads((ROOT / "ecosystem.json").read_text())

    def test_five_independent_modules(self):
        self.assertEqual(len(ecosystem.validate(self.catalog)["modules"]), 5)
        self.assertIn("No model call", ecosystem.render(self.catalog))

    def test_dependency_on_another_module_is_rejected(self):
        self.catalog["modules"][1]["requires_aeion_modules"] = ["factory"]
        with self.assertRaises(ValueError):
            ecosystem.validate(self.catalog)

    def test_missing_module_or_localization_is_rejected(self):
        for mutation in (lambda d: d["modules"].pop(), lambda d: d["modules"][0]["summary"].pop("fr")):
            data = copy.deepcopy(self.catalog)
            mutation(data)
            with self.assertRaises(ValueError):
                ecosystem.validate(data)

    def test_unsafe_repository_or_paid_quickstart_is_rejected(self):
        for key, value in [("repository", "https://example.com/factory"), ("quickstart", {"paid_calls": True, "external_writes": False})]:
            data = copy.deepcopy(self.catalog)
            data["modules"][0][key] = value
            with self.assertRaises(ValueError):
                ecosystem.validate(data)

    def test_duplicate_json_key_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.json"
            path.write_text('{"standalone": true, "standalone": false}')
            with self.assertRaises(ValueError):
                ecosystem.read_json(path)

    def test_malformed_catalog_values_are_rejected(self):
        mutations = [lambda d: d.update(schema_version=True),
                     lambda d: d["modules"][0]["quickstart"].update(commands="echo demo"),
                     lambda d: d["website"]["headline"].update(fr="")]
        for mutation in mutations:
            data = copy.deepcopy(self.catalog)
            mutation(data)
            with self.assertRaises(ValueError):
                ecosystem.validate(data)

    def test_generated_guide_and_inactive_examples(self):
        ecosystem.check(ROOT, self.catalog)


if __name__ == "__main__":
    unittest.main()
