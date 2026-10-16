# Contributing

Start with a synthetic failing example, not an export of your home. Reproduce the
case with `PYTHONPATH=src python3 -m unittest discover -s tests -v` on Python 3.11+.
Install with `python3 -m pip install -e .` in a virtual environment. Runtime code
has no third-party dependencies and must not gain a Home Assistant client or an
automatic apply path without a separately reviewed design.

Add a behavior test for each rule: role and hardware identity, changed domains,
data/target interaction, stale source, unexpected input and unknown references.
Preserve stable report keys, exit codes and diagnostic codes. Bump the report
schema for incompatible output changes. Add all four translations to
`src/ha_entity_migrations/i18n.py`; tests require parity. Maintain the English and
Russian detailed guides and the four README files when changing user behavior.

Regenerate examples with `python3 tools/generate_examples.py` and diagrams with
`python3 tools/render_diagrams.py`. Generated examples are deliberately synthetic;
never replace them with real entity/device inventories. Check links and XML with
`PYTHONPATH=src python3 -m unittest discover -s tests -v`.

Use signed commits and a focused pull request, with all checks passing. Do not
push directly to main. Any GitHub Actions reference must be pinned to a full
commit SHA; shared organization CI is maintained by the repository owner.
The maintainer publishes releases; changing `version` and `pyproject.toml`
together does not itself publish a package. Contributions use the MIT license.


## Feedback and review

Use [GitHub Issues](https://github.com/ha-homelab/ha-entity-migrations/issues) for bug reports,
questions and enhancement proposals; existing issues and pull requests retain
searchable discussion. Include the source revision, expected/actual behavior and
a minimal synthetic reproducer. English reports are welcome. Security reports
follow [SECURITY.md](SECURITY.md), and all participation follows our
[Code of Conduct](CODE_OF_CONDUCT.md).

Contributions are under the repository's MIT license. Submit only material you
have the right to contribute. Follow Python PEP 8 and the repository's Ruff
configuration. Every new major feature and behavior fix requires automated tests,
including a negative or regression case; update the interface documentation and
changelog in the same pull request. Run tests without Python optimization so
assertions remain enabled. The maintainer reviews the diff, test evidence and
open comments before a normal merge. Automated reviews assist this process.

See [RELEASING.md](RELEASING.md) for build and source-version instructions,
[GOVERNANCE.md](GOVERNANCE.md) for responsibilities, and
[ROADMAP.md](ROADMAP.md) for planned work.
