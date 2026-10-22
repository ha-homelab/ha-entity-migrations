# Installation and CLI

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/installation.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/installation.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/installation.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/installation.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/installation.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/installation.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/installation.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/installation.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/installation.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/installation.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/installation.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/installation.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/installation.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/installation.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/installation.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/installation.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/installation.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/installation.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/installation.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/installation.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/installation.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/installation.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/installation.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/installation.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Documentation index](../../README.md#documentation)

Use Python 3.11 or newer. Create a dedicated virtual environment, activate it,
then run `python3 -m pip install -e .` from the checkout. The package has no
runtime dependencies; pip may obtain its build backend. For an offline machine,
prepare the wheel and build dependencies in advance. Verify the selected
installation with `ha-entity-migrations --version`; it reports the installed package version.

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
