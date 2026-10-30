# Licensing and separation

## Distribution terms

This independently maintained distribution is offered under GNU GPL version 3
or, at your option, any later version. [LICENSE](../LICENSE) contains GPLv3.
Apache-2.0-origin portions remain attributed under their original terms; their
licence text is retained in [LICENSES/Apache-2.0.txt](../LICENSES/Apache-2.0.txt).
The complete distribution's SPDX expression is
`GPL-3.0-or-later AND Apache-2.0`, not a choice between those obligations.

The original plugin source retains its Apache-2.0 identifier. The extracted
regression tests retain their original copyright and licence notice, alongside
a notice identifying standalone adaptations. New packaging, documentation and
tests are GPL-3.0-or-later unless explicitly marked otherwise. No upstream
copyright or licence notice has been removed or silently reassigned.

## Why GPL version 3

[Pylint declares GPL-2.0-or-later](https://github.com/pylint-dev/pylint/blob/main/pyproject.toml).
The "or later" option permits GPLv3. The Apache Software Foundation documents
[Apache-2.0 compatibility with GPLv3, but not GPLv2](https://www.apache.org/licenses/GPL-compatibility).
GPLv3 therefore provides a compatible distribution route while retaining the
Apache-origin files, tests and documentation. This does not claim that the
original NASA files have been exclusively relicensed.

Astroid and the other dependencies retain their own licences. They are installed
as separate dependencies, not copied into the release artefacts.

## Relationship to fmdtools

The fmdtools project remains separately licensed and maintained. This package
contains no fmdtools simulation implementation, and the simulation package need
not depend on this plugin. An informational documentation link is separate from
bundling this plugin or adding it as an upstream dependency.

This project does not assert NASA legal approval, endorsement, sponsorship, or
a general prohibition on NASA using GPL software. Institutional redistribution
or deployment decisions remain with the organisations involved.

For the exact extraction record and credits, see [PROVENANCE](../PROVENANCE.md)
and [NOTICE](../NOTICE).
