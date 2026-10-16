# Architecture and report contract

[Model](model.md) · [Limitations](limitations.md) · [Русский](../ru/architecture.md)

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
