# Architettura e contratto del rapporto

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

[Modello](model.md) · [Limiti](limitations.md)

![Flusso dei dati in sola lettura](../diagrams/pipeline.svg)

`io.py` impone i limiti di file, percorsi e JSON e puntatori esatti. `planner.py` convalida le dichiarazioni, costruisce le mappe prima/dopo, esamina i valori sorgente, risolve le politiche esplicite e raccoglie la diagnostica. `cli.py` aggiunge messaggi tradotti e stampa il rapporto. `i18n.py` contiene quattro cataloghi completi di messaggi. Questo percorso non dipende dalla rete né da Home Assistant.

Lo scanner è volutamente prudente. Le stringhe che corrispondono esattamente a riferimenti di entità vengono confrontate con l'istantanea. Le stringhe con riferimenti incorporati restano irrisolte. I template nelle chiavi o nei valori e le chiavi di destinazione dispositivo/area/etichetta restano irrisolti anche quando sembrano facili da interpretare. I normali campi di servizio non sono trattati come ID di entità; i servizi dinamici restano irrisolti. I file non JSON vengono registrati come sorgenti non supportate e bloccano la pianificazione. Non è un parser generico per HA.

![Flusso decisionale delle politiche](../diagrams/policy.svg)

## Involucro JSON stabile, versione 1 dello schema

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Per input validi, `status` è ready o blocked. `scope` è sempre `supplied_files_only`; `read_only` è sempre true. Gli errori di input usano l'involucro invalid ridotto descritto nell'installazione.

Le modifiche hanno operazione, file e puntatore. `replace_reference` contiene anche before/after/policy; `replace_service` contiene before/after; `remove_consumer` contiene il riferimento ritirato. **Non sono JSON Patch eseguibili**. Mancano le semantiche di transazione, spostamento degli indici e ciclo di vita HA. Vanno esaminate come proposte; questa versione non fornisce intenzionalmente un applicatore di patch.

La diagnostica contiene `code`, `location`, `severity` stabili e `message` tradotto. Sia `error` sia `unresolved` bloccano il piano. I rapporti `blocked` possono contenere modifiche candidate per riferimenti non coinvolti, ma nessuna costituisce una transazione pronta. Modelli iniziali obsoleti o in conflitto sopprimono tutte le modifiche candidate ai riferimenti. Le assegnazioni riportano sempre il modello richiesto dall'utente, mai cambiamenti completati.

I rapporti ordinano sorgenti, assegnazioni, modifiche e diagnostica per essere riproducibili. Non contengono orari correnti né punteggi di confidenza inventati. Gli hash dei byte provano quale versione dell'input è stata analizzata, non la sua veridicità né che un dispositivo obbedirà a un comando.
