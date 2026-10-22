# Invoermodel

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/model.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/model.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/model.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/model.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/model.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/model.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/model.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/model.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/model.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/model.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/model.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/model.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/model.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/model.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/model.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/model.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/model.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/model.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/model.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/model.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/model.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/model.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/model.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/model.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Installatie](installation.md) · [Voorbeelden](examples.md)

Alle documenten gebruiken strikt UTF-8-JSON. Dubbele sleutels, niet-eindige getallen en onbekende schemavelden worden geweigerd. De exacte voorbeelden in `examples/` zijn de uitvoerbare referentie. Versievelden moeten het gehele getal `1` bevatten, geen tekenreeks of booleaanse waarde.

## Momentopname

Het hoofdobject bevat uitsluitend `version` en `entities`. Elke entiteit bevat precies:

- `entity_id`: domein-/object-ID in kleine letters, zoals `light.workbench`.
- `hardware_id`: privé, ondoorzichtige identificator gekozen door de beheerder.
- `channel`: fysieke kanaalidentificator als tekenreeks.
- `role`: uniek logisch doel, zoals `workbench` of `pump_enable`.
- `capabilities`: unieke tekenreeksen voor mogelijkheden, bijvoorbeeld `on_off`.

Het paar hardware/kanaal identificeert een fysiek eindpunt. Entiteits-ID's, fysieke eindpunten en logische rollen moeten ieder uniek zijn. Geef een fysieke diagnose weer als ander kanaal, bijvoorbeeld `rssi`, met een eigen unieke rol. Een rol is een planningslabel, geen HA-gebied, -label of -apparaatklasse. Deze declaraties zijn geen metingen; het hulpmiddel kan ze niet bij de hardware controleren.

## Manifest

Het hoofdobject bevat precies `version`, `snapshot_sha256`, `sources`, `assignments` en `consumers`. `sources` koppelt relatieve bestandsnamen aan SHA-256-hashes. `assignments` bevat volledige vervangende entiteitsrecords voor fysieke eindpunten die al in de momentopname staan. Niet-vermelde eindpunten blijven gelijk. Neem voor een nieuw apparaat eerst het waargenomen reserve-eindpunt in de momentopname op. Hardware wordt niet impliciet gemaakt of verwijderd; deze versie vereist unieke rollen.

Elke afnemer identificeert een **letterlijke tekenreekswaarde** via `file` en een RFC 6901-`pointer`. Escape `/` als `~1` en `~` als `~0`; lijstindices beginnen bij nul zonder voorloopnullen. Elke gevonden verwijzing vereist expliciet beleid:

- `follows_role`: zoek het doel dat de logische rol van de bron bezit.
- `follows_hardware`: behoud het fysieke bronkanaal en gebruik de nieuwe entiteits-ID.
- `retire`: stel verwijdering voor van het expliciete object `retire_scope` met de verwijzing.

Niet te verwijderen afnemers vereisen ook `kind` (`action`, `display`, `reference`), `allowed_roles` (niet leeg) en `required_capabilities` (eventueel leeg). Acties vereisen `service_pointer`. Deze grenzen voorkomen dat een anders ingezette pomp een verlichtingsdoel wordt. Het zijn declaraties, geen afgeleide intenties.

Te verwijderen afnemers hebben precies vier velden: file, pointer, policy en retire_scope. Het bereik moet een bovenliggend object zijn dat niet de wortel is. Het mag alleen verwijzingen naar dezelfde verwijderde bron bevatten; gemengde of dynamische verwijzingen blokkeren het. Kies een volledige verouderde automatisering wanneer een losse actie verwijderen een ongeldige lege reeks zou achterlaten. Het hulpmiddel voert HA's schemavalidator niet uit.

## Domeinwijzigingen

Voor acties tussen light/switch worden alleen `turn_on`, `turn_off`, `toggle` en overeenkomende `homeassistant.*`-services ondersteund. Niet-lege `data` of `data_template` zijn niet toegestaan bij automatische serviceomzetting. Een domeinspecifieke service met meerdere letterlijke doelen wordt geblokkeerd. De servicepointer moet het doel onder zijn actie bezitten. Domeinwijzigingen voor weergave vereisen altijd handmatige controle van kaartfuncties; een schakelaar mag niet ongemerkt helderheidsregelaars erven.

## Grenzen

2 MiB per bestand; samen 16 MiB bronbestanden; 64 bestanden; 5.000 entiteiten, toewijzingen of afnemers; JSON-diepte 40 en 100.000 waardeknooppunten per bestand. Identificatoren zijn niet-lege tekenreeksen tot 256 tekens; lijsten van mogelijkheden/toegestane rollen bevatten maximaal 64 unieke tekenreeksen. Relatieve bronpaden mogen niet omhoog gaan, absoluut zijn of symbolische links bevatten. Alleen gewone bestanden zijn invoer.

De bestandslader weigert twee bronnamen die naar hetzelfde canonieke pad of dezelfde open-bestandsidentiteit (apparaat/inode) verwijzen. Dit omvat herhaalde padscheidingstekens, harde links en hoofdletteraliassen op niet-hoofdlettergevoelige bestandssystemen. Behoud één bronnaam en werk de afnemers bij; aliassen mogen geen verschillend migratiebeleid aan hetzelfde fysieke bestand geven. Onafhankelijke bestanden met dezelfde inhoud blijven geldig. De zuivere `plan`-API heeft geen bestandssysteemtoegang: aanroepers die zelf de bronkoppeling bouwen, moeten deze identiteitsgrens vóór de aanroep afdwingen.
