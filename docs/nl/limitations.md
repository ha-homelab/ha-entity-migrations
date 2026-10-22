# Beperkingen en beoordelingsgrens

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

[Architectuur](architecture.md) · [Beveiliging](../../SECURITY.md)

Een plan is slechts zo nauwkeurig als de declaraties van hardware/kanalen/rollen en de aangeleverde bestanden. Het hulpmiddel ontdekt geen weggelaten dashboards, apparaattriggers, scènes, blueprints, elders opgeslagen automatiseringen, Matter-filters, externe clients of verborgen integratiestatus. Een gereed rapport is geen volledige Home Assistant-audit. Rollen zijn uniek in deze versie; semantische veel-op-veelrollen en groepen vereisen handmatige opsplitsing.

JSON-configuratiebronnen worden ondersteund. YAML zelf, includes, aliassen, ankers, uitvoerbare tags, aangepaste componenten en tijdens uitvoering gegenereerde templates worden niet geïnterpreteerd. Normalisatie valt buiten deze versie en kan betekenis verliezen; bewaar het origineel en controleer gelijkwaardigheid. Ook ondersteund JSON wordt niet getoetst aan het volledige HA-configuratieschema. Een expliciet afnemerobject verwijderen kan een ongeldig bovenliggend object achterlaten; beoordeel dat object en voer HA's configuratiecontrole uit binnen het normale stagingproces.

Mogelijkheden en toegestane rollen zijn expliciete beperkingen, geen afgeleide veiligheid. Het hulpmiddel weet niet dat een pomp of garagedeuraandrijving op een eerder onschuldig stopcontact is aangesloten. Een gemelde relaisstatus bewijst niet het gedrag van contact/belasting. Voer geen scripts voor het hele huis uit en schakel geen werkend apparaat uit en in alleen om namen te verifiëren. Fysieke ingebruikname hoort bij een afzonderlijke gecontroleerde procedure.

Deze versie past geen plannen toe, hernoemt geen registerentiteiten, wijzigt geen unieke ID's, herlaadt HA niet, herstart geen controllers, verwijdert geen integraties en draait geen wijzigingen terug. Teruggegeven bewerkingen zijn adviserend en geen uitvoerbare JSON Patch. Verkrijg bij handmatige toepassing een verse momentopname en controleer na elke beoordeelde wijziging; indices en versies kunnen veranderd zijn. Hashes bieden geen handtekeningen of toegangsbeheer.

Rapporten kunnen privénamen en identificatoren bevatten. Houd ze buiten openbare Git-repositories, issuetrackers en CI-artefacten. Openbare voorbeelden gebruiken synthetische apparaten en claimen geen praktijkvalidatie. Diagnostiek blokkeert bewust het plan; er is geen force-optie, negeerlijst of verborgen permissieve modus.
