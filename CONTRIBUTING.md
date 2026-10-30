# Contributing

Open plugin issues and pull requests in this repository. Simulation-library
issues belong in [nasa/fmdtools](https://github.com/nasa/fmdtools).

Use a virtual environment and install `python -m pip install -e ".[dev]"`.
Run `python -m pytest`, `python -m ruff check src tests`, and `python -m build`.
Regression tests must retain real typo detection and must not execute model
source. Avoid expanding inference in ways that hide unresolved attributes.

Keep source provenance and existing notices intact. New contributions are
accepted under the distribution terms in [docs/licensing.md](docs/licensing.md).
Do not add NASA branding or describe this independent project as NASA-endorsed.
