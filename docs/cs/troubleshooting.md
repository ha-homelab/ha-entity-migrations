# Řešení potíží

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/troubleshooting.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/troubleshooting.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/troubleshooting.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/troubleshooting.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/troubleshooting.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/troubleshooting.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/troubleshooting.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/troubleshooting.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/troubleshooting.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/troubleshooting.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/troubleshooting.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/troubleshooting.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/troubleshooting.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/troubleshooting.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/troubleshooting.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/troubleshooting.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/troubleshooting.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/troubleshooting.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/troubleshooting.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/troubleshooting.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/troubleshooting.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/troubleshooting.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/troubleshooting.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/troubleshooting.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Instalace](installation.md) · [Omezení](limitations.md)

**Příkaz nenalezen:** aktivujte stejné virtuální prostředí jako při instalaci. Zkuste `python3 -m ha_entity_migrations --version`; neinstalujte do systémového Pythonu jen kvůli obejití nesprávné cesty.

**Návratový kód 2, schema_invalid:** porovnejte klíče se spustitelným příkladem a [vstupním modelem](model.md). Neznámá pole jsou chyby. Verze jsou celé číslo 1; identifikátory kanálů jsou řetězce. Každá zásada akce potřebuje ukazatel služby. Snímek má entity, manifest přiřazení a konzumenty. Soubory nejsou zaměnitelné.

**Návratový kód 2, duplicate_source:** dva názvy označují jeden fyzický soubor. Ponechte jediný kanonický název v `sources` a přepište na něj všechna pole `file` konzumentů. Odstraňte duplicitní oddělovače a aliasy pevných odkazů/velikosti písmen; nepřiřazujte aliasu druhou zásadu. Oddělené soubory se stejným obsahem zůstávají podporovány.

**stale_snapshot / stale_source:** porovnejte skutečné změny se schváleným zdrojem. Příkaz fingerprint použijte až po kontrole. Bílé znaky mění hash. Neodkazujte na starou kopii jen proto, aby vyhověl starý hash.

**source_collision / destination_collision:** fyzický kanál, role nebo ID entity je duplicitní. Výslovně popište obě strany výměny rolí a ověřte, že nezměněný bod nedrží požadované cílové ID.

**role_not_allowed / capability_missing:** konzument by dosáhl nevhodné zátěže nebo ztratil schopnost. Potvrďte, zda má sledovat roli, nebo hardware. Automaticky nerozšiřujte allowed_roles ani nedeklarujte schopnosti, které hardware nemá. Světlo nahrazené relé zapnuto/vypnuto nemůže stmívat.

**missing_policy / unmodeled_reference:** zmapujte odkazovaný bod a přidejte výslovnou deklaraci konzumenta až po potvrzení účelu. Starý řetězec historie může být mimo aktivní rozsah; záměrně vyřaďte soubor z rozsahu, zdokumentujte vyloučení a znovu vytvořte smlouvu zdrojů.

**dynamic_reference / embedded_reference / indirect_target:** tato verze nemůže prokázat mapování. Jinja nebo chování skupin/oblastí/štítků ověřte zvlášť, případně dodejte výslovnou normalizovanou literální konfiguraci. Program nikdy nespouští šablonu.

**display_domain_review / service_data_review / mixed_action_targets:** prohlédněte funkce karty, parametry akcí a dávky cílů. Vícedoménovou akci rozdělte v samostatně kontrolované změně zdroje; nestačí jen změnit doménu služby.

**retire_scope_mixed / overlapping_edits:** zvolte souvislý zastaralý objekt konzumenta bez nesouvisejících odkazů. Neodstraňujte z akce pouze entity_id: mohlo by vzniknout příliš široké cílení nebo neplatná konfigurace. Program žádné vyřazení automaticky neprovádí.

**unsupported_source:** plánovat lze jen JSON. YAML, binární a další soubory se tiše nepřeskakují. Výslovně normalizovaná kopie JSON může pomoci analýze, ale před reálnou úpravou se musí porovnat s originálem.

Chybu hlaste s minimálním syntetickým vstupem, verzí nástroje/Pythonu, návratovým kódem a diagnostickými kódy. Nikdy nepřikládejte surový export domácnosti ani přihlašovací údaje API.
