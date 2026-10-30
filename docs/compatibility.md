# Compatibility and validation

## Supported scope

The distribution requires Python 3.12 or newer, Pylint 4.x and Astroid 4.x.
The Pylint dependency supplies its narrower compatible Astroid range.
fmdtools is installed separately; it is needed to resolve the model's classes,
but importing this plugin does not import the simulation library.

The v0.1.0 implementation is identical to the source reviewed in
[nasa/fmdtools#79](https://github.com/nasa/fmdtools/pull/79), pinned to the
[recorded upstream snapshot](../PROVENANCE.md).

## Release validation

The installed wheel passed all **22 tests** in clean macOS arm64 environments:

| Python | Pylint | Astroid | fmdtools | Tests |
| --- | --- | --- | --- | --- |
| 3.12.14 | 4.1.3 | 4.3.4 | 2.5.7 | 22 passed |
| 3.13.15 | 4.1.3 | 4.3.4 | 2.5.7 | 22 passed |
| 3.14.7 | 4.1.3 | 4.3.4 | 2.5.7 | 22 passed |
| 3.12.14, source archive | 4.0.0 | 4.0.4 | 2.5.7 | 22 passed |

These are 17 retained inference regressions and five distribution checks.
Every test invokes the installed package; the test harness does not add the
plugin source tree or NASA's tools directory to PYTHONPATH. Temporary fixture
helpers are the only added source path. Tests fail rather than silently skip
when required dependencies are missing.

The CI workflow additionally exercises Linux, Windows and macOS, the minimum
Pylint version, and source-archive installation. Current job results are visible
on the [Actions page](https://github.com/sylvesterkaczmarek/fmdtools-pylint/actions/workflows/ci.yml).
Local command-line results do not imply interactive GUI verification in VS Code
or Spyder, and no claim is made about NASA's internal CI.

## Compatibility boundaries

The plugin resolves literal role declarations and known fmdtools bases. It does
not invent attributes for unrelated classes, execute model constructors, or
claim to validate equations or simulation results. Dynamic factories, unknown
mixins and dynamically computed role names retain conservative inference.

Use a clean environment when migrating from a development checkout that bundled
`fmdtools_pylint`. Verify the imported module's path before enabling the plugin.
Do not allow two installed distributions to own the same package path.
