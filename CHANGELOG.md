# Changelog

## Unreleased

- Reject duplicate source paths and physical-file aliases before planning, including hard links.
- Preserve distinct files with identical content and report actionable source-alias errors in all four languages.

## 0.1.0

- Add offline role-aware planning from explicit JSON manifests and normalized snapshots.
- Guard entity/channel/role collisions, source fingerprints and consumer capabilities.
- Plan conservative light/switch service changes and explicit whole-consumer retirement.
- Block unresolved templates, indirect targets, unsupported sources and ambiguous edits.
- Provide English, Russian, German and Spanish CLI text and README entry points.
- Include tested synthetic examples, EN/RU manuals, checked-in wiki pages and original SVG diagrams.

This is a first software release. No live Home Assistant installation or physical
device has been migrated by this tool. There is no apply command.
