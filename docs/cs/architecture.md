# Architektura a smlouva reportu

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

[Model](model.md) · [Omezení](limitations.md)

![Datový tok pouze pro čtení](../diagrams/pipeline.svg)

`io.py` vynucuje limity souborů, cest a JSON a přesné ukazatele. `planner.py` ověřuje deklarace, sestavuje mapy před/po, prochází zdrojové hodnoty, vyhodnocuje výslovné zásady a shromažďuje diagnostiku. `cli.py` přidává přeložené zprávy a vypisuje report. `i18n.py` obsahuje čtyři úplné katalogy zpráv. Tato cesta nemá závislost na síti ani Home Assistantu.

Skener je záměrně opatrný. Řetězce přesně odpovídající odkazům na entity porovnává se snímkem. Řetězce s vloženými odkazy zůstávají nevyřešené. Šablony v klíčích či hodnotách a cílové klíče zařízení/oblast/štítek zůstávají nevyřešené, i když jejich význam vypadá zřejmý. Prostá pole služeb se nepovažují za ID entit; dynamické služby zůstávají nevyřešené. Soubory mimo JSON jsou evidovány jako nepodporované zdroje a blokují plánování. Nejde o obecný parser HA.

![Rozhodování podle zásad](../diagrams/policy.svg)

## Stabilní obálka JSON, verze schématu 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Pro platné vstupy je `status` ready nebo blocked. `scope` je vždy `supplied_files_only`; `read_only` je vždy true. Chyby vstupu používají menší obálku invalid popsanou v instalaci.

Úpravy mají operaci, soubor a ukazatel. `replace_reference` obsahuje také before/after/policy; `replace_service` obsahuje before/after; `remove_consumer` obsahuje vyřazovaný odkaz. **Nejde o spustitelný JSON Patch**. Chybí sémantika transakcí, posunu indexů a životního cyklu HA. Posuzujte je jako návrhy; tato verze záměrně nenabízí nástroj pro aplikaci záplat.

Diagnostika obsahuje stabilní `code`, `location`, `severity` a přeloženou `message`. `error` i `unresolved` blokují plán. Reporty `blocked` mohou obsahovat kandidátní úpravy neovlivněných odkazů, žádná však netvoří připravenou transakci. Zastaralé nebo rozporné počáteční modely potlačují všechny kandidátní změny odkazů. Přiřazení vždy opakují požadovaný model uživatele, nikdy již provedené změny.

Reporty řadí zdroje, přiřazení, úpravy a diagnostiku pro reprodukovatelnost. Neobsahují aktuální časová razítka ani vymyšlená skóre spolehlivosti. Hash bajtů dokládá analyzovanou verzi vstupu, ne jeho pravdivost ani to, že zařízení uposlechne příkaz.
