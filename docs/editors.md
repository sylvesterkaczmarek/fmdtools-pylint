# Editor setup

Install the plugin in the interpreter that actually runs Pylint. The import
name remains `fmdtools_pylint`; the distribution is `fmdtools-pylint`.

## Verify the environment

```bash
python -c "import sys, pylint, fmdtools_pylint; print(sys.executable); print(pylint.__file__); print(fmdtools_pylint.__file__)"
python -m pylint --load-plugins=fmdtools_pylint path/to/model.py
```

Use the [installation instructions](../README.md#quick-start). Pylint must also
be able to locate the fmdtools package used by the model. Avoid mixing a legacy
fmdtools checkout that bundled this module with a standalone installation;
recreate the virtual environment if the paths above point to the wrong copy.
Do not install the legacy `fmdtools[lint]` extra for this standalone package.

## VS Code

Install Microsoft's Python and Pylint extensions. Select the project virtual
environment using **Python: Select Interpreter**. Add the following keys to the
existing `.vscode/settings.json`, without replacing other workspace settings:

```json
{
  "pylint.cwd": "${workspaceFolder}",
  "pylint.importStrategy": "fromEnvironment",
  "pylint.path": ["${interpreter}", "-m", "pylint"],
  "pylint.args": ["--load-plugins=fmdtools_pylint"]
}
```

Alternatively load the plugin in `.pylintrc` and omit the duplicate load argument.
Restart the Pylint server after installing or changing settings. Inspect
**Output > Pylint** for the actual executable and any import errors.
`fromEnvironment` alone can fall back to a bundled Pylint if installation is
missing; the explicit command selects the intended interpreter.

Reference: [Microsoft's Pylint extension](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint).

## Spyder

Following the upstream maintainer's guidance, use the project IPython console
or a terminal rather than modifying Spyder's internal application environment.
From the console, run Pylint in a separate process using that console's Python:

```python
import subprocess
import sys

completed = subprocess.run(
    [sys.executable, "-m", "pylint", "--load-plugins=fmdtools_pylint", "/absolute/path/to/model.py"],
    capture_output=True,
    text=True,
    check=False,
)
print(completed.stdout)
print(completed.stderr)
```

A nonzero status can mean diagnostics were found, rather than a failed import.
This command prints the diagnostics in the console; it does not populate the
Code Analysis pane or configure that pane's interpreter. Spyder's application
and console environments can differ, as discussed in
[spyder-ide/spyder#26423](https://github.com/spyder-ide/spyder/issues/26423).
No claim is made that the built-in pane has been tested on every Spyder install.

## Focused checks and troubleshooting

Use `--disable=all --enable=no-member,fmdtools-unknown-field` for a focused
model-member pass, or omit those options for ordinary Pylint diagnostics.

If the plugin cannot load, verify its location in the same interpreter shown by
the editor. If valid roles still produce E1101, check that the source bases and
role declarations are statically resolvable. Dynamic factories and unknown
mixins intentionally retain ordinary inference. Semantic colouring and editor
completion are separate capabilities and are not provided by this plugin.
