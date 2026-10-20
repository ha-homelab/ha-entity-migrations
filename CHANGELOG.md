# Changelog

## Unreleased

No pending changes.

## 0.1.1b1 — 2026-10-20

- Report the package version in migration plans instead of a stale hard-coded version.
- First GitHub beta: source archive, wheel and SHA-256 checksums; no PyPI publication.
- Keep package metadata, source version and root version aligned. This prerelease retains the existing report/schema contracts.

- Update CI to pytest 9.0.3 (GHSA-6w46-j5rx-g56g) and the build backend to setuptools 83.0.0 (upstream fix for GHSA-h35f-9h28-mq5c).
- Document private reporting, review/release responsibilities, contribution rules and the current continuity limitation; include these policies in source distributions.

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
