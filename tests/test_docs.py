import hashlib
import re
import subprocess
import sys
import tomllib
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from ha_entity_migrations import __version__
from ha_entity_migrations.i18n import CATALOGS

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_version_sources_match(self):
        project = tomllib.loads((ROOT / "pyproject.toml").read_text())
        self.assertEqual(project["project"]["version"], __version__)
        self.assertEqual((ROOT / "version").read_text().strip(), __version__)

    def test_local_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
                continue
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                target = target.split("#")[0]
                self.assertTrue((path.parent / target).exists(), f"{path}: {target}")

    def test_translations_cover_every_emitted_code(self):
        emitted = set()
        for file in ["io.py", "planner.py"]:
            text = (ROOT / "src" / "ha_entity_migrations" / file).read_text()
            emitted |= set(re.findall(r'(?:InputError|issue)\("([a-z_]+)"', text))
        for values in CATALOGS.values():
            self.assertTrue(emitted <= values.keys(), emitted - values.keys())

    def test_diagrams_and_examples_are_reproducible(self):
        paths = list((ROOT / "docs" / "diagrams").glob("*.svg")) + list(
            (ROOT / "examples").rglob("*.json")
        )
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        for tool in ["generate_examples.py", "render_diagrams.py"]:
            subprocess.run([sys.executable, str(ROOT / "tools" / tool)], check=True)
        self.assertEqual(
            before, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
        )
        self.assertEqual(len(list((ROOT / "docs" / "diagrams").glob("*.svg"))), 3)
        for path in (ROOT / "docs" / "diagrams").glob("*.svg"):
            root = ET.parse(path).getroot()
            self.assertEqual(root.attrib["role"], "img")
            self.assertIsNotNone(root.find("{http://www.w3.org/2000/svg}title"))
            self.assertIsNotNone(root.find("{http://www.w3.org/2000/svg}desc"))

    def test_four_readme_and_two_complete_guides(self):
        for name in ["README.md", "README.ru.md", "README.de.md", "README.es.md"]:
            self.assertGreater(len((ROOT / name).read_text()), 2000)
        for language in ["en", "ru"]:
            for topic in [
                "installation",
                "model",
                "examples",
                "architecture",
                "troubleshooting",
                "limitations",
            ]:
                self.assertGreater(
                    len((ROOT / "docs" / language / f"{topic}.md").read_text()), 1000
                )


if __name__ == "__main__":
    unittest.main()
