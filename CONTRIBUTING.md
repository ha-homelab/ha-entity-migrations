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
