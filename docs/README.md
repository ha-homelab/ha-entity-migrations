# Documentation

Guides for the offline CLI that moves a logical role to new hardware and produces a
reviewable migration plan from an explicit inventory and consumer policies. The tool
never connects to Home Assistant or applies a change.

## English guides

- [Installation and CLI](en/installation.md) — virtual environment setup, the `fingerprint` and `plan` commands, and language and format options.
- [Input model](en/model.md) — the strict JSON snapshot and manifest schema, including entities, assignments, consumers and action policies.
- [Worked examples](en/examples.md) — the synthetic role-swap, domain-change and blocked-template cases with their expected reports.
- [Architecture and report contract](en/architecture.md) — module layout, the conservative source scanner and the deterministic report fields.
- [Troubleshooting](en/troubleshooting.md) — schema errors, duplicate sources, stale fingerprints and other failure diagnoses by exit code.
- [Limitations and review boundary](en/limitations.md) — what a plan cannot see, why YAML is unsupported, and the checks left to the operator.

## References

- [Sources and relationship to other projects](sources.md) — the upstream HA documentation and diagnostics tools this project's terminology follows.
- [Maintaining documentation translations](translations.md) — the language catalog and how translated pages and wiki pages are maintained.

## Translations

Each language directory holds the same six guides, cross-linked to every other
language. The English pages are the source.

- [English](en/README.md)
- [العربية](ar/README.md)
- [বাংলা](bn/README.md)
- [Čeština](cs/README.md)
- [Deutsch](de/README.md)
- [Español](es/README.md)
- [فارسی](fa/README.md)
- [Français](fr/README.md)
- [עברית](he/README.md)
- [हिन्दी](hi/README.md)
- [Bahasa Indonesia](id/README.md)
- [Italiano](it/README.md)
- [日本語](ja/README.md)
- [한국어](ko/README.md)
- [Nederlands](nl/README.md)
- [Polski](pl/README.md)
- [Português](pt/README.md)
- [Русский](ru/README.md)
- [ไทย](th/README.md)
- [Türkçe](tr/README.md)
- [Українська](uk/README.md)
- [Tiếng Việt](vi/README.md)
- [简体中文](zh-Hans/README.md)
- [繁體中文](zh-Hant/README.md)
