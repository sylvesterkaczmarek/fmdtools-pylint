# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2026 Sylvester Kaczmarek.
"""Regression checks for the separately installed distribution."""

import hashlib
from importlib import metadata, resources
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_SHA256 = "8eff4f549e49d754eeb8b47e551e0864c4a34ab9bf772b1e31094f2bb44f9d54"


class TestStandaloneDistribution(unittest.TestCase):
    def test_reviewed_plugin_implementation_is_preserved(self):
        source = resources.files("fmdtools_pylint").joinpath("__init__.py").read_bytes()
        self.assertEqual(hashlib.sha256(source).hexdigest(), UPSTREAM_SHA256)

    def test_focused_profile_is_in_the_installed_package(self):
        profile = resources.files("fmdtools_pylint").joinpath("pylint-models.rc")
        text = profile.read_text(encoding="utf-8")
        self.assertIn("load-plugins=fmdtools_pylint", text)
        self.assertIn("enable=no-member,fmdtools-unknown-field", text)

    def test_metadata_retains_licences_and_no_simulation_runtime_dependency(self):
        distribution = metadata.distribution("fmdtools-pylint")
        self.assertEqual(distribution.version, "0.1.0")
        self.assertEqual(
            distribution.metadata["License-Expression"],
            "GPL-3.0-or-later AND Apache-2.0",
        )
        declared = distribution.metadata.get_all("License-File")
        for filename in ("LICENSE", "LICENSES/Apache-2.0.txt", "NOTICE", "AUTHORS.md"):
            self.assertIn(filename, declared)
        runtime = [item for item in distribution.requires if "extra ==" not in item]
        self.assertTrue(any(item.startswith("pylint") for item in runtime))
        self.assertTrue(any(item.startswith("astroid") for item in runtime))
        self.assertFalse(any(item.startswith("fmdtools") for item in runtime))
        paths = [str(path).replace("\\", "/") for path in distribution.files]
        self.assertFalse(any(path.startswith("fmdtools/") for path in paths))

    def test_regular_project_configuration_preserves_standard_diagnostics(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / ".pylintrc").write_text(
                (ROOT / ".pylintrc").read_text(encoding="utf-8"), encoding="utf-8"
            )
            (folder / "model.py").write_text(
                "from fmdtools.define.block.function import Function\n"
                "from fmdtools.define.container.state import State\n"
                "class S(State):\n    speed: float = 1.0\n"
                "class F(Function):\n    container_s = S\n"
                "    def value(self):\n        return self.s.speeed, undefined_value\n",
                encoding="utf-8",
            )
            env = dict(os.environ, PYLINTHOME=str(folder / "cache"))
            env.pop("PYTHONPATH", None)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pylint",
                    "--persistent=n",
                    "--score=n",
                    "--reports=n",
                    "--output-format=json",
                    "model.py",
                ],
                cwd=folder,
                env=env,
                capture_output=True,
                text=True,
                timeout=45,
                check=False,
            )
            self.assertEqual(completed.stderr, "")
            self.assertEqual(completed.returncode & 2, 2, completed.stdout)
            symbols = {message["symbol"] for message in json.loads(completed.stdout)}
            self.assertIn("undefined-variable", symbols)
            self.assertIn("fmdtools-unknown-field", symbols)

    def test_documented_cli_finds_the_example_typo_from_a_neutral_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            empty = Path(directory) / "empty.rc"
            empty.write_text("", encoding="utf-8")
            env = dict(os.environ, PYLINTHOME=str(Path(directory) / "cache"))
            env.pop("PYTHONPATH", None)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pylint",
                    "--load-plugins=fmdtools_pylint",
                    "--disable=all",
                    "--enable=no-member,fmdtools-unknown-field",
                    "--rcfile=" + str(empty),
                    "--persistent=n",
                    "--score=n",
                    "--reports=n",
                    "--output-format=json",
                    str(ROOT / "examples/model.py"),
                ],
                cwd=directory,
                env=env,
                capture_output=True,
                text=True,
                timeout=45,
                check=False,
            )
            self.assertEqual(
                completed.returncode, 2, completed.stdout + completed.stderr
            )
            messages = json.loads(completed.stdout)
            self.assertEqual(
                [m["symbol"] for m in messages], ["fmdtools-unknown-field"]
            )
            self.assertIn("speeed", messages[0]["message"])


if __name__ == "__main__":
    unittest.main()
