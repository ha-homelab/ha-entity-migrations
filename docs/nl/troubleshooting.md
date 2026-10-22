# Problemen oplossen

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

[Installatie](installation.md) · [Beperkingen](limitations.md)

**Opdracht niet gevonden:** activeer dezelfde virtuele omgeving als bij installatie. Probeer `python3 -m ha_entity_migrations --version`; installeer niet in systeem-Python om een verkeerd pad te omzeilen.

**Afsluitcode 2, schema_invalid:** vergelijk sleutels met het uitvoerbare voorbeeld en [invoermodel](model.md). Onbekende velden zijn fouten. Versies zijn het gehele getal 1; kanaalidentificatoren zijn tekenreeksen. Elk actiebeleid heeft een servicepointer nodig. Een momentopname bevat entiteiten, een manifest toewijzingen en afnemers. Deze bestanden zijn niet uitwisselbaar.

**Afsluitcode 2, duplicate_source:** twee bronnamen identificeren één fysiek bestand. Behoud één canonieke naam in `sources` en pas alle `file`-velden van afnemers aan. Verwijder dubbele scheidingstekens of harde-link-/hoofdletteraliassen; geef een alias geen tweede beleid. Aparte bestanden met gelijke inhoud blijven ondersteund.

**stale_snapshot / stale_source:** vergelijk werkelijke wijzigingen met de goedgekeurde bron. Gebruik fingerprint pas na beoordeling. Witruimte verandert de hash. Verwijs niet naar een oude kopie alleen om de oude hash te laten kloppen.

**source_collision / destination_collision:** een fysiek kanaal, rol of entiteits-ID is dubbel. Beschrijf beide kanten van een rolruil expliciet en controleer of een ongewijzigd eindpunt de gewenste doel-ID vasthoudt.

**role_not_allowed / capability_missing:** de afnemer zou een ongeschikte belasting bereiken of een mogelijkheid verliezen. Bevestig of hij rol of hardware moet volgen. Verruim allowed_roles niet automatisch en claim geen ontbrekende hardwaremogelijkheden. Een lamp vervangen door een aan/uit-relais kan niet dimmen.

**missing_policy / unmodeled_reference:** inventariseer het genoemde eindpunt en voeg pas na bevestiging van het doel een expliciete afnemerdeclaratie toe. Een oude geschiedenisstring kan buiten het actieve bereik vallen; sluit dat bestand bewust uit, documenteer dit en genereer het broncontract opnieuw.

**dynamic_reference / embedded_reference / indirect_target:** deze versie kan de koppeling niet bewijzen. Beoordeel Jinja of groeps-/gebieds-/labelgedrag afzonderlijk of lever expliciete genormaliseerde letterlijke configuratie. Het programma voert nooit een template uit.

**display_domain_review / service_data_review / mixed_action_targets:** inspecteer kaartfuncties, actieparameters en doelgroepen. Splits een actie met meerdere domeinen in een afzonderlijk beoordeelde bronwijziging; wijzig niet alleen het servicedomein.

**retire_scope_mixed / overlapping_edits:** kies een samenhangend verouderd afnemerobject zonder andere verwijzingen. Verwijder niet alleen entity_id uit een actie: dat kan een te breed doel of ongeldige configuratie opleveren. Het programma past geen automatische verwijdering toe.

**unsupported_source:** alleen JSON kan worden gepland. YAML, binaire en andere bestanden worden niet stilzwijgend overgeslagen. Een expliciet genormaliseerde JSON-kopie kan analyse helpen, maar moet vóór echte wijzigingen met het origineel worden vergeleken.

Meld fouten met minimale synthetische invoer, hulpmiddel-/Python-versie, afsluitcode en diagnosecodes. Voeg nooit een onbewerkte huishoudenexport of API-inloggegevens toe.
