# Installatie en CLI

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/installation.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/installation.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/installation.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/installation.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/installation.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/installation.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/installation.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/installation.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/installation.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/installation.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/installation.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/installation.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/installation.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/installation.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/installation.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/installation.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/installation.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/installation.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/installation.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/installation.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/installation.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/installation.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/installation.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/installation.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Documentatie-index](../../README.md#documentation)

Gebruik Python 3.11 of nieuwer. Maak en activeer een eigen virtuele omgeving en voer `python3 -m pip install -e .` uit vanuit de checkout. Het pakket heeft geen runtimeafhankelijkheden; pip kan zijn bouwbackend ophalen. Bereid voor een offlinecomputer vooraf het wheel en de bouwafhankelijkheden voor. Controleer de gekozen installatie met `ha-entity-migrations --version`; dit toont de geïnstalleerde pakketversie.

De CLI heeft twee opdrachten, met de globale taaloptie vóór de opdracht:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` toont de SHA-256 in kleine letters van de exacte bestandsbytes. Het valideert het bestand niet als JSON. Vingerafdrukken van momentopname en bronnen in het manifest moeten exact overeenkomen, inclusief witruimte. Vernieuw een vingerafdruk niet alleen om een onverwachte afwijking weg te drukken; vergelijk en keur de nieuwe invoer eerst goed.

`plan` leest een JSON-manifest, een genormaliseerde JSON-momentopname en uitsluitend de bestanden die expliciet in `manifest.sources` staan, relatief aan `--root`. Het doorzoekt geen mappen recursief of uw persoonlijke map. De standaarduitvoer is JSON. Alleen menselijke meldingen veranderen bij `--lang en|ru|de|es`; veldnamen en diagnosecodes blijven stabiel. `--help` bestaat op hoofdniveau en per opdracht. Er is geen opdracht om toe te passen, uploaden, ontdekken of authenticeren.

Afsluitstatus:

- **0:** het ondersteunde invoerbereik is intern consistent en gereed voor beoordeling.
- **2:** ongeldige argumenten/invoer, onleesbaar bestand of schending van schema/grenswaarden.
- **3:** structureel geldige invoer leverde een geblokkeerd plan op door conflict of onopgelost bereik.

Invoerfouten na argumentverwerking produceren een JSON-envelop op stdout met `status: invalid`. Argumentfouten tonen vertaalde gebruiksinformatie op stderr. Een geslaagde vingerafdruk toont uitsluitend de hash. In tekstmodus behouden wijzigingsvoorstellen hun machineveldnamen; toelichtingen worden vertaald.

Bewaar operationele bestanden in een privémap. Door stdout om te leiden maakt u een eigen rapport, mogelijk met identificerende entiteitsnamen en paden. Het hulpmiddel zelf schrijft niets. Verwijder het met `python3 -m pip uninstall ha-entity-migrations`. Zie [CONTRIBUTING](../../CONTRIBUTING.md) voor ontwikkelaarscontroles.
