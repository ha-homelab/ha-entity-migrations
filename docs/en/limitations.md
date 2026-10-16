# Limitations and review boundary

[Architecture](architecture.md) · [Security](../../SECURITY.md) · [Русский](../ru/limitations.md)

A plan is only as accurate as its physical/channel/role declarations and the
files you provide. This tool does not discover omitted dashboards, device
triggers, scenes, blueprints, automations stored elsewhere, Matter filters,
external clients or hidden integration state. Do not call a ready report a full
Home Assistant audit. A role is unique in this release; many-to-many semantic
roles and groups require manual decomposition.

JSON configuration sources are supported. YAML itself, includes, aliases,
anchors, executable tags, custom components and runtime-generated templates are
not interpreted. Normalization is outside this release and may lose semantics;
keep the original and review the equivalence. Even supported JSON is not checked
against Home Assistant's complete configuration schema. Removing an explicit
consumer object can leave an invalid parent; review that parent and run HA's
configuration checker in your normal staging process.

Capabilities and allowed roles are explicit constraints, not inferred safety.
The tool cannot know that a pump or garage drive has been plugged into a formerly
harmless outlet. A reported relay state does not prove contact/load behavior.
Do not run whole-house scripts or power-cycle a live appliance merely to validate
names. Physical commissioning belongs to a separate controlled procedure.

This release does not apply a plan, rename a registry entity, modify a unique ID,
reload HA, restart a controller, retire an integration or roll back a change.
Returned operations are advisory and not executable JSON Patch. If someone
manually applies them, obtain a fresh snapshot and verify after each reviewed
change; indexes and versions may have changed. Hashes do not provide signatures
or access control.

Reports can contain private names and identifiers. Keep them out of public Git,
issue trackers and CI artifacts. Public examples use synthetic devices and do
not claim field validation. Diagnostics block the plan by design; there is no
force flag, ignore list or hidden permissive mode.
