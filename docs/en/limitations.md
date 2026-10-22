# Limitations and review boundary

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/limitations.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/limitations.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/limitations.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/limitations.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/limitations.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/limitations.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/limitations.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/limitations.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/limitations.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/limitations.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/limitations.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/limitations.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/limitations.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/limitations.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/limitations.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/limitations.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/limitations.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/limitations.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/limitations.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/limitations.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/limitations.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/limitations.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/limitations.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/limitations.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Architecture](architecture.md) · [Security](../../SECURITY.md)

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
