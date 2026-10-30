# Security

Pylint executes installed plugins and may inspect dependencies. Only install
trusted plugins and use a controlled environment for untrusted projects.
The regression suite checks that this plugin does not execute model fixtures;
this does not turn Pylint into a security sandbox.

For a suspected security issue, contact the maintainer through the contact
route on [sylvesterkaczmarek.com](https://sylvesterkaczmarek.com/). Do not include
credentials, private models or personal data in a public GitHub issue.
