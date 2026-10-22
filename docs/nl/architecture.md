# Architectuur en rapportcontract

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/architecture.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/architecture.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/architecture.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/architecture.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/architecture.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/architecture.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/architecture.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/architecture.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/architecture.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/architecture.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/architecture.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/architecture.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/architecture.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/architecture.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/architecture.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/architecture.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/architecture.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/architecture.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/architecture.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/architecture.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/architecture.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/architecture.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/architecture.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/architecture.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Model](model.md) · [Beperkingen](limitations.md)

![Gegevensstroom zonder schrijfacties](../diagrams/pipeline.svg)

`io.py` bewaakt grenzen voor bestanden, paden en JSON en exacte pointers. `planner.py` valideert declaraties, bouwt voor/na-koppelingen, onderzoekt bronwaarden, verwerkt expliciet beleid en verzamelt diagnostiek. `cli.py` voegt vertaalde meldingen toe en drukt het rapport af. `i18n.py` bevat vier volledige berichtencatalogi. Dit pad heeft geen netwerk- of Home Assistant-afhankelijkheid.

De scanner is bewust terughoudend. Exacte tekenreeksen die op entiteitsverwijzingen lijken, worden met de momentopname vergeleken. Tekenreeksen met ingebedde verwijzingen blijven onopgelost. Templates in sleutels of waarden en doelsleutels voor apparaten/gebieden/labels blijven onopgelost, zelfs als de betekenis eenvoudig lijkt. Gewone servicevelden gelden niet als entiteits-ID's; dynamische services blijven onopgelost. Niet-JSON-bestanden worden als niet-ondersteunde bronnen geregistreerd en blokkeren de planning. Dit is geen algemene HA-parser.

![Beslisstroom voor beleid](../diagrams/policy.svg)

## Stabiele JSON-envelop, schemaversie 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Bij geldige invoer is `status` ready of blocked. `scope` is altijd `supplied_files_only`; `read_only` is altijd true. Invoerfouten gebruiken de kleinere invalid-envelop uit de installatiehandleiding.

Wijzigingen bevatten een bewerking, bestand en pointer. `replace_reference` bevat ook before/after/policy; `replace_service` bevat before/after; `remove_consumer` bevat de te verwijderen verwijzing. Dit zijn **geen uitvoerbare JSON Patch-bewerkingen**. Semantiek voor transacties, verschoven indices en de HA-levenscyclus ontbreekt. Beoordeel ze als voorstellen; deze versie bevat bewust geen patchtoepasser.

Diagnostiek bevat stabiele `code`, `location`, `severity` en een vertaalde `message`. Zowel `error` als `unresolved` blokkeren een plan. Rapporten met `blocked` kunnen kandidaatwijzigingen voor onaangetaste verwijzingen bevatten, maar geen daarvan vormt een gereedstaande transactie. Verouderde of tegenstrijdige beginmodellen onderdrukken alle kandidaatwijzigingen van verwijzingen. Toewijzingen herhalen altijd het door de gebruiker gevraagde model, nooit voltooide wijzigingen.

Rapporten sorteren bronnen, toewijzingen, wijzigingen en diagnostiek voor reproduceerbaarheid. Er zijn geen actuele tijdstempels of verzonnen betrouwbaarheidsscores. Bytehashes bewijzen welke invoerversie is geanalyseerd, niet of de invoer waar was of een apparaat een opdracht zal opvolgen.
