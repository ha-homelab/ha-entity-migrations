# Uitgewerkte voorbeelden

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/examples.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/examples.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/examples.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/examples.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/examples.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/examples.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/examples.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/examples.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/examples.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/examples.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/examples.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/examples.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/examples.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/examples.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/examples.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/examples.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/examples.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/examples.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/examples.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/examples.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/examples.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/examples.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/examples.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/examples.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Invoermodel](model.md) · [Architectuur](architecture.md)

Alle hardware en rollen hier zijn synthetisch. Maak identieke invoer opnieuw met `python3 tools/generate_examples.py`. Geen enkele opdracht verbindt met Home Assistant.

## Een lamprol verlaat een anders ingezet stopcontact

Voer de README-opdracht uit voor `examples/role-swap`. Aanvankelijk bezit `plug-a/1` de entiteit `light.workbench` en `plug-b/1` de entiteit `switch.spare`. Het manifest kent de pomprol toe aan stopcontact A en de werkbankrol aan B. De lichtautomatisering gebruikt `follows_role` en staat alleen `workbench` toe. De verwijzing blijft `light.workbench`, terwijl de doelhardware verandert. Dat er geen tekstbewerking nodig is, is bedoeld en geen ontbrekende migratie. `assignments` in het rapport bevat de hardwarewijzigingen voor menselijke beoordeling.

De oude reserveafnemer wordt verwijderd bij `/1`, het volledige tweede automatiseringsobject. Zo blijft geen lege actiereeks achter. Het rapport is adviserend; het programma verwijdert geen JSON-arrayelementen. Houd bij handmatige toepassing van meerdere voorgestelde verwijderingen rekening met verschoven indices en voer opnieuw uit vanaf een verse momentopname.

Wijzig het eerste beleid in `follows_hardware` en laat `workbench` als toegestane rol staan: het plan blokkeert met `role_not_allowed`. De rollenlijst uitbreiden met een pomp is een expliciete gevaarlijke intentiewijziging, geen normale manier om de fout op te lossen. Herstel liever het juiste beleid.

## Een relais verandert van light naar switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

De twee voorgestelde wijzigingen veranderen het doel en de service `light.turn_off`. Voeg helderheidsgegevens toe aan de bronactie, werk de goedgekeurde bronvingerafdruk bij en voer opnieuw uit: `service_data_review` blokkeert automatische omzetting. Verwijder helderheidsinstellingen niet alleen om de controle te laten slagen; beoordeel het gewenste gedrag.

## Een onopgelost template

Voer dezelfde opdracht uit met `examples/blocked-template`. Het doel is dynamische Jinja. Het hulpmiddel evalueert dit niet en retourneert code 3. Een volledig ondersteund plan vereist expliciete configuratie met aantoonbare letterlijke doelen; behandel dit anders als gedocumenteerde handmatige migratie buiten het gereedstaande bereik. De afsluitcode negeren lost het template niet op.

## Afwijkingen en herhaalbaarheid

Een bron aanpassen zonder de manifesthash te wijzigen geeft `stale_source`. De momentopname aanpassen geeft `stale_snapshot`. Voor zulke verouderde modellen worden geen kandidaatwijzigingen van verwijzingen uitgegeven. Bij ongewijzigde bestanden is het JSON-resultaat deterministisch, behalve de gekozen taal. Bronbestanden blijven byte voor byte gelijk.

Kopieer voor een echt project het formaat naar een privémap, controleer fysieke identiteiten, inventariseer afnemers en voer de planner uit. Beoordeel alle toewijzingen en wijzigingen, voer HA's eigen controles uit binnen uw gebruikelijke uitrolproces en maak daarna een nieuwe alleen-lezen momentopname ter verificatie. Dit project implementeert die uitrol noch een rollback-uitvoerder.
