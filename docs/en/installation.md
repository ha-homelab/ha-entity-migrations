# Installation and CLI

[Documentation index](../../README.md#documentation) · [Русский](../ru/installation.md)

Use Python 3.11 or newer. Create a dedicated virtual environment, activate it,
then run `python3 -m pip install -e .` from the checkout. The package has no
runtime dependencies; pip may obtain its build backend. For an offline machine,
prepare the wheel and build dependencies in advance. Verify the selected
installation with `ha-entity-migrations --version` (0.1.0).

The CLI has two commands, with a global language option before the command:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` prints lowercase SHA-256 of the exact file bytes. It does not
validate the file as JSON. Snapshot and source fingerprints in a manifest must
match those exact files, including whitespace. Do not refresh a fingerprint just
to dismiss unexpected drift; compare and approve the new input first.

`plan` reads a JSON manifest, a normalized JSON snapshot and only the files
explicitly named in `manifest.sources`, relative to `--root`. It does not recurse
through a directory or search your home. Default output is JSON. Only human
messages change for `--lang en|ru|de|es`; field names and diagnostic codes stay
stable. `--help` is available at the top level and for each command. There is no
apply, upload, discover or authentication command.

Exit status:

- **0:** supported input scope is internally consistent and ready for review.
- **2:** invalid arguments/input, unreadable file or schema/limit violation.
- **3:** structurally valid input produced a blocked plan (conflict or unresolved scope).

Input failures after argument parsing produce a JSON envelope on stdout with
`status: invalid`. Argument errors print localized usage to stderr. Successful
fingerprinting prints only the digest. In text mode, proposed edit records keep
their machine field names; explanations are translated.

Keep operational files in a private directory. Redirecting stdout creates your
own report; it may contain identifying entity names and file paths. The tool
itself writes nothing. Uninstall with `python3 -m pip uninstall ha-entity-migrations`.
For developer checks, see [CONTRIBUTING](../../CONTRIBUTING.md).
