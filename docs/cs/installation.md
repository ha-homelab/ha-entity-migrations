# Instalace a CLI

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

[Rejstřík dokumentace](../../README.md#documentation)

Použijte Python 3.11 nebo novější. Vytvořte a aktivujte samostatné virtuální prostředí a v pracovní kopii spusťte `python3 -m pip install -e .`. Balíček nemá běhové závislosti; pip může stáhnout sestavovací backend. Pro počítač bez připojení připravte wheel a sestavovací závislosti předem. Zvolenou instalaci ověřte pomocí `ha-entity-migrations --version`; vypíše instalovanou verzi balíčku.

CLI má dva příkazy, globální volba jazyka se uvádí před příkazem:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` vypíše SHA-256 přesných bajtů souboru malými písmeny. Neověřuje, zda je soubor platný JSON. Otisky snímku a zdrojů v manifestu musí přesně odpovídat souborům včetně bílých znaků. Neobnovujte otisk jen pro potlačení neočekávané odchylky; nejprve nový vstup porovnejte a schvalte.

`plan` čte JSON manifest, normalizovaný JSON snímek a pouze soubory výslovně uvedené v `manifest.sources`, relativně k `--root`. Neprochází adresář rekurzivně ani nehledá ve vašem domovském adresáři. Výchozí výstup je JSON. S `--lang en|ru|de|es` se mění pouze zprávy pro lidi; názvy polí a diagnostické kódy zůstávají stabilní. `--help` je dostupná na nejvyšší úrovni i pro každý příkaz. Neexistuje příkaz pro použití, nahrání, objevování ani autentizaci.

Návratový stav:

- **0:** podporovaný rozsah vstupu je vnitřně konzistentní a připravený ke kontrole.
- **2:** neplatné argumenty/vstup, nečitelný soubor nebo porušení schématu/limitů.
- **3:** strukturálně platný vstup vytvořil blokovaný plán kvůli konfliktu nebo nevyřešenému rozsahu.

Chyby vstupu po zpracování argumentů vytvářejí JSON obálku na stdout s `status: invalid`. Chyby argumentů vypisují lokalizovanou nápovědu na stderr. Úspěšný výpočet otisku vypíše jen digest. V textovém režimu si navržené úpravy zachovají strojové názvy polí; vysvětlení jsou přeložena.

Provozní soubory uchovávejte v soukromém adresáři. Přesměrováním stdout vznikne váš report, který může obsahovat identifikující názvy entit a cesty. Nástroj sám nic nezapisuje. Odinstalujte příkazem `python3 -m pip uninstall ha-entity-migrations`. Vývojářské kontroly najdete v [CONTRIBUTING](../../CONTRIBUTING.md).
