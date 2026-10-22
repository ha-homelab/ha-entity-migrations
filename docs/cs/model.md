# Vstupní model

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

[Instalace](installation.md) · [Příklady](examples.md)

Všechny dokumenty používají striktní UTF-8 JSON. Duplicitní klíče, nekonečné hodnoty a NaN a neznámá pole schématu se odmítají. Přesné příklady v `examples/` jsou spustitelná reference. Pole verze musí být celé číslo `1`, ne řetězec ani logická hodnota.

## Snímek

Kořenový objekt obsahuje pouze `version` a `entities`. Každá entita obsahuje přesně:

- `entity_id`: ID domény/objektu malými písmeny, například `light.workbench`.
- `hardware_id`: soukromý neprůhledný identifikátor zvolený provozovatelem.
- `channel`: identifikátor fyzického kanálu jako řetězec.
- `role`: jedinečný logický účel, například `workbench` nebo `pump_enable`.
- `capabilities`: jedinečné řetězce popisující schopnosti, například `on_off`.

Dvojice hardware/kanál identifikuje fyzický koncový bod. ID entit, fyzické koncové body a logické role musí být každé jedinečné. Fyzickou diagnostiku vyjádřete jiným kanálem, například `rssi`, s vlastní jedinečnou rolí. Role je plánovací označení, nikoli oblast, štítek nebo třída zařízení HA. Tyto deklarace nejsou měření; nástroj je nemůže ověřit vůči hardwaru.

## Manifest

Kořenový objekt má přesně `version`, `snapshot_sha256`, `sources`, `assignments` a `consumers`. `sources` mapuje relativní názvy souborů na otisky SHA-256. `assignments` obsahuje úplné náhradní záznamy entit pro fyzické koncové body už přítomné ve snímku. Neuvedené body se nemění. Nové zařízení zaveďte tak, že nejprve přidáte jeho pozorovaný rezervní bod do snímku. Hardware se implicitně nevytváří ani nemaže a tato verze vyžaduje jedinečné role.

Každý konzument určuje **literální řetězcovou hodnotu** pomocí `file` a RFC 6901 `pointer`. Znak `/` kódujte jako `~1` a `~` jako `~0`; indexy seznamů začínají nulou, bez úvodních nul. Každý nalezený odkaz potřebuje výslovnou zásadu:

- `follows_role`: najít cíl vlastnící logickou roli zdroje.
- `follows_hardware`: zachovat fyzický zdrojový kanál a použít jeho nové ID entity.
- `retire`: navrhnout odstranění explicitního objektu `retire_scope` obsahujícího odkaz.

Nevyřazovaní konzumenti také vyžadují `kind` (`action`, `display`, `reference`), `allowed_roles` (neprázdné) a `required_capabilities` (případně prázdné). Akce vyžadují `service_pointer`. Tato omezení brání použití nově přeznačeného čerpadla jako cíle osvětlení. Jde o deklarace, nikoli odhad záměru.

Vyřazovaní konzumenti mají přesně čtyři pole: file, pointer, policy a retire_scope. Rozsah musí být objekt předka odlišný od kořene. Smí obsahovat jen odkazy na stejný vyřazovaný zdroj; smíšené nebo dynamické odkazy ho blokují. Pokud by odstranění akce nechalo neplatnou prázdnou posloupnost, vyberte celou zastaralou automatizaci. Nástroj nespouští validátor schématu HA.

## Změny domén

Pro akci přecházející mezi light/switch jsou podporovány jen `turn_on`, `turn_off`, `toggle` a odpovídající služby `homeassistant.*`. Automatický převod služeb nepřijímá neprázdné `data` ani `data_template`. Doménová služba s více literálními cíli je blokována. Ukazatel služby musí vlastnit cíl pod svou akcí. Změna domény zobrazení vždy vyžaduje ruční kontrolu funkcí karty; spínač nemůže tiše převzít ovládání jasu.

## Meze

2 MiB na soubor; celkem 16 MiB zdrojových souborů; 64 souborů; 5 000 entit, přiřazení nebo konzumentů; hloubka JSON 40 a 100 000 hodnotových uzlů na soubor. Identifikátory jsou neprázdné řetězce do 256 znaků, seznamy schopností/povolených rolí mají nejvýše 64 jedinečných řetězců. Relativní cesty nesmějí procházet nahoru, být absolutní ani obsahovat symbolické odkazy. Vstupy jsou pouze běžné soubory.

Načítač odmítne dva názvy zdrojů odkazující na stejnou kanonickou cestu nebo identitu otevřeného souboru (zařízení/inode). Zahrnuje to opakované oddělovače, pevné odkazy a aliasy velikosti písmen na systémech bez jejího rozlišení. Ponechte jeden název a aktualizujte konzumenty; aliasy nesmějí nést různá migrační pravidla pro jeden fyzický soubor. Nezávislé soubory se shodným obsahem zůstávají platné. Čisté API `plan` nemá přístup k souborovému systému: volající sestavující vlastní mapu zdrojů musí tuto hranici identity vynutit před voláním.
