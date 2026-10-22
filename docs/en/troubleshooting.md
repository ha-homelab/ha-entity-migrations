# Troubleshooting

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/troubleshooting.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/troubleshooting.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/troubleshooting.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/troubleshooting.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/troubleshooting.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/troubleshooting.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/troubleshooting.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/troubleshooting.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/troubleshooting.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/troubleshooting.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/troubleshooting.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/troubleshooting.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/troubleshooting.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/troubleshooting.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/troubleshooting.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/troubleshooting.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/troubleshooting.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/troubleshooting.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/troubleshooting.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/troubleshooting.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/troubleshooting.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/troubleshooting.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/troubleshooting.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/troubleshooting.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Installation](installation.md) · [Limitations](limitations.md)

**Command not found:** activate the same virtual environment used for installation.
Try `python3 -m ha_entity_migrations --version`; do not install into system Python
just to work around a path mismatch.

**Exit 2, schema_invalid:** compare your keys with the executable example and
[input model](model.md). Unknown fields are errors. Versions are integer 1;
channel identifiers are strings. Every action policy needs its service pointer.
A snapshot has entities; a manifest has assignments and consumers. They are not
interchangeable files.

**Exit 2, duplicate_source:** two source names identify one physical file.
Keep a single canonical name in `sources` and update all consumer `file` fields
to it. Remove duplicate separators or hard-link/case aliases; do not give an
alias a second policy. Separate files with identical content remain supported.

**stale_snapshot / stale_source:** compare actual changes with the approved source.
Use the fingerprint command only after reviewing them. Whitespace changes affect
the hash. Do not point at a stale copy merely to make the old hash pass.

**source_collision / destination_collision:** a physical channel, role or entity
ID is duplicated. Express both sides of a role swap explicitly, and check that
an unchanged endpoint is not retaining the desired destination ID.

**role_not_allowed / capability_missing:** the consumer would reach an inappropriate
load or lose an ability. Confirm whether it should follow the role or hardware.
Do not automatically widen allowed_roles or claim capabilities that hardware does
not have. A light replaced by an on/off relay cannot provide dimming.

**missing_policy / unmodeled_reference:** inventory the referenced endpoint and
add an explicit consumer declaration only after confirming its purpose. An old
history string might be outside active scope; remove that file from the planned
scope deliberately, document the exclusion, and regenerate the source contract.

**dynamic_reference / embedded_reference / indirect_target:** this release cannot
prove the mapping. Review Jinja or group/area/label behavior separately, or supply
an explicit normalized literal configuration. The program never executes a template.

**display_domain_review / service_data_review / mixed_action_targets:** inspect
card features, action parameters and target batches. Split a multi-domain action
in a separately reviewed source change; don't just change its service domain.

**retire_scope_mixed / overlapping_edits:** choose a coherent obsolete consumer
object without unrelated references. Do not delete only entity_id from an action:
that could create a broad target or leave invalid configuration. No automatic
retirement is applied by this program.

**unsupported_source:** only JSON can be planned. YAML, binary and other files
are not silently skipped. An explicitly normalized JSON copy may help analysis,
but must be compared to its original before any real edit.

Report a bug using a minimal synthetic input, the tool/Python version, exit code
and diagnostic codes. Never attach a raw household export or API credentials.
