# Source provenance

The initial extraction is from [nasa/fmdtools's preserved lint branch](https://github.com/nasa/fmdtools/tree/6f19c23b8659c253decef2b2e85f3c373cddbbfd),
commit `6f19c23b8659c253decef2b2e85f3c373cddbbfd`.

The implementation was contributed in
[PR #79](https://github.com/nasa/fmdtools/pull/79).
Its source history includes Sylvester Kaczmarek's commits
[`a591fc372`](https://github.com/nasa/fmdtools/commit/a591fc372cbd91fefd2087d566dc85896b1825c7)
and [`796076f5`](https://github.com/nasa/fmdtools/commit/796076f5d97cf5959f2de5517a41e1993b6c0c27).
Daniel Hulse's final usage changes are in
[`6f19c23b`](https://github.com/nasa/fmdtools/commit/6f19c23b8659c253decef2b2e85f3c373cddbbfd).
The [separation request](https://github.com/nasa/fmdtools/pull/79#issuecomment-6505406554)
is recorded in the original discussion.

## Extraction map

| Original path | Standalone use |
| --- | --- |
| `tools/fmdtools_pylint/__init__.py` | `src/fmdtools_pylint/__init__.py`, unchanged implementation |
| `tests/test_model_role_linting.py` | Same 17 cases, adapted for installed-package testing |
| `tools/pylint-models.rc` | Installed resource `fmdtools_pylint/pylint-models.rc` |
| `.pylintrc` | Project configuration, with standalone installation comments |
| `docs-source/Model_linting.rst` | README and editor guide, retaining Daniel's console-first Spyder guidance |

The original implementation's SHA-256 is:
`8eff4f549e49d754eeb8b47e551e0864c4a34ab9bf772b1e31094f2bb44f9d54`.

This is a new distribution with explicit provenance, not a rewritten or
re-attributed copy of NASA's complete Git history. It contains no simulation
library, internal NASA material or unrelated upstream files. The extraction
manifest records the original source-file hashes below.

```json
{
  "repository": "nasa/fmdtools",
  "commit": "6f19c23b8659c253decef2b2e85f3c373cddbbfd",
  "files": [
    {
      "source": "tools/fmdtools_pylint/__init__.py",
      "destination": "src/fmdtools_pylint/__init__.py",
      "sha256": "8eff4f549e49d754eeb8b47e551e0864c4a34ab9bf772b1e31094f2bb44f9d54"
    },
    {
      "source": "tests/test_model_role_linting.py",
      "destination": "tests/test_model_role_linting.py",
      "sha256": "25c62f0a6598b5e85631145c6968f5dd6f9a47dbffae35481b6db279dc4c6db2"
    },
    {
      "source": "tools/pylint-models.rc",
      "destination": "src/fmdtools_pylint/pylint-models.rc",
      "sha256": "34f2fb80de3e503c25bdea0ca818f20b1c2654ecfca8094436f9edd07672b8e9"
    },
    {
      "source": ".pylintrc",
      "destination": ".pylintrc",
      "sha256": "22fcbd3d94156fb6f5f6358cbb218ffbe281b647cdd1a46af110deb1efbfbd4e"
    },
    {
      "source": "docs-source/Model_linting.rst",
      "destination": "docs/model-linting-upstream.rst",
      "sha256": "8f07587d8132b3b0f1f081a1aa2bf4121310739c653938c36ae9a0f2d581bb20"
    }
  ]
}
```
