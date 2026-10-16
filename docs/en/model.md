# Input model

[Installation](installation.md) · [Examples](examples.md) · [Русский](../ru/model.md)

All documents use UTF-8 strict JSON. Duplicate keys, non-finite numbers and unknown
schema fields are rejected. Exact examples in `examples/` are the executable
reference. Version fields must be the integer `1`, not a string or boolean.

## Snapshot

The top object contains only `version` and `entities`. Each entity contains exactly:

- `entity_id`: lower-case domain/object ID, such as `light.workbench`.
- `hardware_id`: private opaque identifier chosen by the operator.
- `channel`: physical channel identifier, as a string.
- `role`: unique logical purpose, such as `workbench` or `pump_enable`.
- `capabilities`: unique strings describing abilities, for example `on_off`.

The pair hardware/channel identifies a physical endpoint. Entity IDs, physical
endpoints and logical roles must each be unique. Represent a physical diagnostic
as a different channel, e.g. `rssi`, with its own unique role. A role is a planning
label, not a Home Assistant area, label or device class. These declarations are
not measurements; the tool cannot verify them against hardware.

## Manifest

The top object has exactly `version`, `snapshot_sha256`, `sources`, `assignments`
and `consumers`. `sources` maps relative filenames to SHA-256 digests. `assignments`
contains complete replacement entity records for physical endpoints already in
the snapshot. Unlisted endpoints remain unchanged. To bring in a new device,
first include its observed spare endpoint in the snapshot. There is no implicit
creation or deletion of hardware, and this release requires unique roles.

Each consumer identifies a **literal string value** by `file` and RFC 6901
`pointer`. Escape `/` as `~1` and `~` as `~0`; list indexes are zero-based without
leading zeros. Every discovered reference needs an explicit policy:

- `follows_role`: find the destination owning the source's logical role.
- `follows_hardware`: keep the source physical channel and use its new entity ID.
- `retire`: propose removal of the explicit `retire_scope` object containing the reference.

Non-retirement consumers also require `kind` (`action`, `display`, `reference`),
`allowed_roles` (nonempty) and `required_capabilities` (possibly empty). Actions
require `service_pointer`. These gates protect against using a newly repurposed
pump as a lighting target. They are declarations, not inferred intent.

Retirement consumers have exactly four fields: file, pointer, policy and
retire_scope. The scope must be a non-root ancestor object. It may contain only
references to the same retired source; mixed or dynamic references block it.
Select an entire obsolete automation when removing an action would leave an
invalid empty sequence. The tool does not run HA's schema validator.

## Domain changes

For an action crossing light/switch, only `turn_on`, `turn_off`, `toggle` and
matching `homeassistant.*` services are supported. No nonempty `data` or
`data_template` is accepted for automatic service conversion. A domain-specific
service with multiple literal targets is blocked. The service pointer must own
the target under its action. Display domain changes always require manual card
feature review; a switch cannot silently inherit brightness controls.

## Bounds

2 MiB per file; 16 MiB combined source files; 64 files; 5,000 entities,
assignments or consumers; JSON depth 40 and 100,000 value nodes per file.
Identifiers are nonempty strings up to 256 characters, capabilities/allowed-role
lists up to 64 unique strings. Relative source paths cannot traverse upward,
be absolute, or contain symlinks. Inputs are regular files only.
