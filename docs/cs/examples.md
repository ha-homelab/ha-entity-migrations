# Podrobné příklady

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

[Vstupní model](model.md) · [Architektura](architecture.md)

Veškerý hardware a role zde jsou syntetické. Shodné vstupy znovu vytvoříte příkazem `python3 tools/generate_examples.py`. Žádný příkaz se nepřipojuje k Home Assistantu.

## Role lampy opouští zásuvku s novým účelem

Spusťte příkaz z README pro `examples/role-swap`. Původně `plug-a/1` vlastní `light.workbench` a `plug-b/1` vlastní `switch.spare`. Manifest přiřadí zásuvce A roli čerpadla a zásuvce B roli pracovního stolu. Automatizace osvětlení používá `follows_role` a povoluje pouze `workbench`. Odkaz zůstane `light.workbench`, zatímco cílový hardware se změní. Absence textové úpravy je zamýšlený výsledek, nikoli chybějící migrace. Pole `assignments` v reportu obsahuje hardwarové změny k lidské kontrole.

Původní rezervní konzument je vyřazen na `/1`, tedy jako celý druhý objekt automatizace. Nezůstane tak prázdná posloupnost akcí. Report je doporučující; program neodstraňuje žádný prvek pole JSON. Při ručním použití více návrhů odstranění počítejte s posunutými indexy a plánování zopakujte z čerstvého snímku.

Změňte první zásadu na `follows_hardware`, ale ponechte povolenou roli `workbench`: plán zablokuje `role_not_allowed`. Rozšíření seznamu o čerpadlo je výslovná nebezpečná změna záměru, nikoli běžný způsob odstranění chyby. Obnovte raději správnou zásadu.

## Relé se mění z light na switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Dvě navržené úpravy změní cíl a jeho službu `light.turn_off`. Přidejte ke zdrojové akci údaje o jasu, aktualizujte schválený otisk zdroje a spusťte znovu: `service_data_review` zablokuje automatický převod. Neodstraňujte nastavení jasu jen kvůli průchodu kontrolou; posuďte požadované chování.

## Nevyřešená šablona

Spusťte stejný příkaz s `examples/blocked-template`. Cílem je dynamická Jinja. Nástroj ji nevyhodnocuje a vrací kód 3. Úplný podporovaný plán vyžaduje výslovnou konfiguraci s prokazatelnými literálními cíli; jinak tuto část ponechte jako zdokumentovanou ruční migraci mimo připravený rozsah. Ignorování návratového kódu šablonu nevyřeší.

## Odchylky a opakovatelnost

Úprava zdroje bez změny jeho hashe v manifestu způsobí `stale_source`. Úprava snímku způsobí `stale_snapshot`. Pro takové zastaralé modely se nevypisují kandidátní změny odkazů. Při nezměněných souborech je JSON výsledek deterministický, kromě zvoleného jazyka. Zdrojové soubory zůstávají bajt po bajtu nezměněné.

Pro skutečný projekt zkopírujte formát do soukromé složky, ověřte fyzické identity, sepište konzumenty a spusťte plánovač. Zkontrolujte všechna přiřazení a úpravy, proveďte vlastní kontroly HA v zavedeném procesu nasazení a následně vytvořte nový snímek pouze pro čtení k ověření výsledku. Tento projekt neimplementuje toto nasazení ani vykonavatele návratu změn.
