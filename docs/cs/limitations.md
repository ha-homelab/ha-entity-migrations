# Omezení a hranice kontroly

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

[Architektura](architecture.md) · [Bezpečnost](../../SECURITY.md)

Přesnost plánu omezuje přesnost deklarací hardwaru/kanálů/rolí a dodaných souborů. Nástroj neobjeví vynechané dashboardy, spouštěče zařízení, scény, blueprinty, automatizace uložené jinde, filtry Matter, externí klienty ani skrytý stav integrací. Připravený report není úplný audit Home Assistantu. Každá role je v této verzi jedinečná; sémantické role mnoho-na-mnoho a skupiny vyžadují ruční rozklad.

Podporovány jsou konfigurační zdroje JSON. Samotný YAML, vkládání souborů, aliasy, kotvy, spustitelné značky, vlastní komponenty a šablony generované za běhu se neinterpretují. Normalizace je mimo tuto verzi a může ztratit sémantiku; zachovejte originál a ověřte ekvivalenci. Ani podporovaný JSON se nekontroluje proti úplnému konfiguračnímu schématu HA. Odstranění explicitního objektu konzumenta může zanechat neplatného rodiče; zkontrolujte ho a spusťte kontrolu konfigurace HA v běžném testovacím prostředí před nasazením.

Schopnosti a povolené role jsou výslovné podmínky, nikoli odvozená bezpečnost. Nástroj neví, že k původně neškodné zásuvce bylo připojeno čerpadlo nebo pohon garáže. Hlášený stav relé nedokazuje chování kontaktu/zátěže. Nespouštějte celodomovní skripty ani nevypínejte a nezapínejte běžící spotřebič jen pro ověření názvů. Fyzické zprovoznění patří do samostatného řízeného postupu.

Tato verze nepoužívá plány, nepřejmenovává entity v registru, nemění jedinečné ID, nenačítá znovu HA, nerestartuje řadiče, nevyřazuje integrace a nevrací změny. Vrácené operace jsou doporučení, nikoli spustitelný JSON Patch. Při ruční aplikaci získejte nový snímek a ověřte stav po každé zkontrolované změně; indexy a verze se mohly změnit. Hashe neposkytují podpisy ani řízení přístupu.

Reporty mohou obsahovat soukromé názvy a identifikátory. Nedávejte je do veřejného Gitu, issue trackerů ani CI artefaktů. Veřejné příklady používají syntetická zařízení a netvrdí ověření v terénu. Diagnostika blokuje plán záměrně; není žádný přepínač vynucení, seznam ignorování ani skrytý benevolentní režim.
