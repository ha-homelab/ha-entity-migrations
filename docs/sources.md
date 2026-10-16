# Sources and relationship to other projects

The implementation and synthetic diagrams are original MIT-licensed work. No
Home Assistant code, household inventory, screenshots or physical test results
are bundled. Terminology and supported configuration shapes were checked against:

- [HA actions and targets](https://www.home-assistant.io/docs/scripts/perform-actions/): services, entity targets and action data.
- [HA templating](https://www.home-assistant.io/docs/configuration/templating/): runtime-dependent Jinja cannot be safely guessed offline.
- [HA entity registry](https://developers.home-assistant.io/docs/entity_registry_index/): stable identities differ from display names.
- [RFC 6901](https://www.rfc-editor.org/rfc/rfc6901): exact JSON-pointer syntax.
- [Spook automation repairs](https://spook.boo/automation/) and [Watchman](https://github.com/dummylabs/thewatchman): existing missing-reference diagnostics.

This tool complements those diagnostics with an explicitly declared destination
role/hardware mapping. It does not replace a HA configuration check, physical
verification, registry backup or either upstream repair tool. Runtime behavior
and APIs may change; this release has no direct registry/API integration.
