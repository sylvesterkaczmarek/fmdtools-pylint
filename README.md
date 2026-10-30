# fmdtools-pylint

**Static checks for fmdtools models, without running simulations.**

[![CI](https://github.com/sylvesterkaczmarek/fmdtools-pylint/actions/workflows/ci.yml/badge.svg)](https://github.com/sylvesterkaczmarek/fmdtools-pylint/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/sylvesterkaczmarek/fmdtools-pylint)](https://github.com/sylvesterkaczmarek/fmdtools-pylint/releases)
[![Python](https://img.shields.io/badge/Python-3.12%20%7C%203.13%20%7C%203.14-blue)](docs/compatibility.md)
[![License](https://img.shields.io/badge/License-GPLv3%2B-blue)](docs/licensing.md)

An opt-in Pylint plugin for [NASA's fmdtools](https://github.com/nasa/fmdtools).
It understands dynamically declared model roles and reports misspelled container
fields while retaining ordinary Pylint checks.

Maintained by **[Sylvester Kaczmarek](https://github.com/sylvesterkaczmarek)**.
Originally developed and reviewed in [nasa/fmdtools#79](https://github.com/nasa/fmdtools/pull/79),
then extracted into a separate package at the
[upstream maintainer's request](https://github.com/nasa/fmdtools/pull/79#issuecomment-6505406554).
This is independently maintained, not a NASA-sponsored or endorsed product.

[Quick start](#quick-start) · [Editor setup](docs/editors.md) · [Compatibility](docs/compatibility.md) · [Provenance](PROVENANCE.md)

## What it catches

| Model code | Result |
| --- | --- |
| `self.s.speed` with a declared `speed` field | Accepted |
| `self.water.s.speed` through a declared flow | Accepted |
| `self.flows` / `self.fxns` on the appropriate architecture | Accepted |
| `self.s.speeed` or `self.water.s.speeed` | `E9901`, unknown container field |
| `self.watre` or `self.flwos` | Standard `E1101`, unknown member |

Inherited roles, aliases, custom role names and overridden state types are
covered. Unknown mixins and genuinely dynamic attributes retain conservative
Pylint inference. The plugin does not validate physical equations, simulation
results, safety, autocomplete or semantic colouring.

## Quick start

Use a clean project environment. Install fmdtools separately, then the tagged
plugin release from GitHub. No PyPI publication is assumed.

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell instead: .venv\Scripts\Activate.ps1

python -m pip install fmdtools "git+https://github.com/sylvesterkaczmarek/fmdtools-pylint.git@v0.1.0"
python -m pylint --load-plugins=fmdtools_pylint path/to/model.py
```

No Git installed? Use the wheel attached to the
[release](https://github.com/sylvesterkaczmarek/fmdtools-pylint/releases/tag/v0.1.0):

```bash
python -m pip install fmdtools "https://github.com/sylvesterkaczmarek/fmdtools-pylint/releases/download/v0.1.0/fmdtools_pylint-0.1.0-py3-none-any.whl"
```

With uv, use `uv pip install` with the same package arguments in your selected
virtual environment. The plugin installs Pylint and Astroid; it neither bundles
nor installs the fmdtools simulation library as a runtime dependency.

### Check model members only

```bash
python -m pylint --load-plugins=fmdtools_pylint --disable=all --enable=no-member,fmdtools-unknown-field path/to/model.py
```

Keep the full command above for your regular linting policy. The focused command
is useful for model-role checks and does not replace the rest of Pylint.

### Enable it for a project

Add to your existing `.pylintrc`, preserving other settings:

```ini
[MAIN]
load-plugins=fmdtools_pylint
```

Then run `python -m pylint path/to/model.py`. Merely installing this package does
not change another repository's configuration. A focused profile is also shipped
as the package resource `fmdtools_pylint/pylint-models.rc`.

## A small example

```python
from fmdtools.define.block.function import Function
from fmdtools.define.container.state import State

class PumpState(State):
    speed: float = 1.0

class Pump(Function):
    container_s = PumpState

    def read_speed(self):
        return self.s.speeed  # E9901: the declared field is speed.
```

The plugin parses model definitions instead of importing or instantiating them.
Its regression suite includes source-execution sentinels. This is a tested
property of the plugin, not a general sandbox guarantee for Pylint, other
plugins or untrusted editor configurations.

## Using it with NASA's project

[fmdtools](https://github.com/nasa/fmdtools) provides simulation and risk analysis.
This repository provides the optional model-linting add-on, with its own
installation, issues, releases and licensing. Neither a submodule nor a runtime
link from fmdtools to this repository is required.

The first standalone release preserves the reviewed plugin implementation.
Daniel Hulse's latest usage guidance is carried forward, including the Spyder
console workflow. See [editor setup](docs/editors.md) and the precise
[source record](PROVENANCE.md).

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest
python -m build
```

Tests require fmdtools to be installed and run Pylint in subprocesses against
small model fixtures. They do not rely on NASA's checkout, its `tools` folder or
source-tree path injection. CI additionally tests installed wheel and source
archives from a neutral directory. See [contributing](CONTRIBUTING.md).

## Licence and attribution

The standalone distribution is GPL-3.0-or-later and includes Apache-2.0-origin
material with its notices retained. Its SPDX distribution expression is
`GPL-3.0-or-later AND Apache-2.0`. The original fmdtools project keeps its own
licence. See [licensing details](docs/licensing.md), [NOTICE](NOTICE) and
[contributors](AUTHORS.md).
