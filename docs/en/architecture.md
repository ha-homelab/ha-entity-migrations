# Architecture and report contract

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/architecture.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/architecture.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/architecture.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/architecture.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/architecture.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/architecture.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/architecture.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/architecture.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/architecture.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/architecture.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/architecture.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/architecture.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/architecture.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/architecture.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/architecture.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/architecture.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/architecture.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/architecture.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/architecture.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/architecture.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/architecture.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/architecture.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/architecture.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/architecture.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Model](model.md) · [Limitations](limitations.md)

![Read-only data flow](../diagrams/pipeline.svg)

`io.py` enforces file/path/JSON bounds and exact pointers. `planner.py` validates
the declarations, builds before/after maps, scans source values, resolves explicit
policies and accumulates diagnostic records. `cli.py` adds translated messages
and prints the report. `i18n.py` contains four complete message catalogs. There
is no network or Home Assistant dependency in this path.

The scanner is deliberately conservative. Exact entity-like strings are checked
against the snapshot. Strings with embedded references are unresolved. Templates
in keys or values, and device/area/label target keys, are unresolved even when
one seems easy to guess. Plain service fields are not treated as entity IDs;
dynamic services are still unresolved. Non-JSON files are registered as
unsupported sources and block planning. This is not a general HA parser.

![Policy decision flow](../diagrams/policy.svg)

## Stable JSON envelope, schema version 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`,
`snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`,
`language`, `summary`. `status` is ready or blocked for valid inputs.
`scope` is always `supplied_files_only`; `read_only` is always true.
Input errors use the smaller invalid envelope described in installation.

Edits have an operation, file and pointer. `replace_reference` also contains
before/after/policy; `replace_service` contains before/after; `remove_consumer`
contains the retired reference. These are **not an executable JSON Patch**.
They lack transaction, index-shift and HA lifecycle semantics. Review them as
proposals; this release intentionally supplies no patch applier.

Diagnostics contain stable `code`, `location`, `severity` and translated `message`.
Both `error` and `unresolved` block a plan. `blocked` reports can contain candidate
edits for unaffected references, but none are a ready transaction. Stale or
conflicting initial models suppress all candidate reference edits. Assignments
always echo the user's requested model, never completed changes.

Reports sort sources, assignments, edits and diagnostics for reproducibility.
There are no current timestamps or invented confidence scores. The byte hashes
prove which input version was analyzed, not whether an input was truthful or
whether a device will obey a command.
