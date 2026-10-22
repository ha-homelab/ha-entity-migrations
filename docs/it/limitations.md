# Limiti e confini della revisione

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

[Architettura](architecture.md) · [Sicurezza](../../SECURITY.md)

Un piano è accurato solo quanto le dichiarazioni di hardware/canali/ruoli e i file forniti. Lo strumento non scopre dashboard omesse, trigger di dispositivi, scene, blueprint, automazioni archiviate altrove, filtri Matter, client esterni o stati nascosti delle integrazioni. Un rapporto pronto non è un audit completo di Home Assistant. In questa versione ogni ruolo è unico; ruoli semantici molti-a-molti e gruppi richiedono scomposizione manuale.

Sono supportate sorgenti di configurazione JSON. YAML, inclusioni, alias, ancore, tag eseguibili, componenti personalizzati e template generati durante l'esecuzione non vengono interpretati. La normalizzazione è fuori da questa versione e può perdere semantica: conserva l'originale e verificane l'equivalenza. Anche il JSON supportato non viene controllato contro lo schema completo di HA. Rimuovere un oggetto consumatore esplicito può lasciare un genitore non valido; esaminalo ed esegui il controllo di configurazione HA nel normale processo di staging.

Capacità e ruoli consentiti sono vincoli espliciti, non sicurezza dedotta. Lo strumento non sa che una pompa o un motore da garage è stato collegato a una presa prima innocua. Lo stato dichiarato di un relè non dimostra il comportamento di contatto/carico. Non eseguire script per tutta la casa né togliere e ridare alimentazione a un apparecchio in servizio soltanto per convalidare nomi. La messa in servizio fisica richiede una procedura controllata separata.

Questa versione non applica piani, rinomina entità del registro, modifica ID unici, ricarica HA, riavvia controller, ritira integrazioni o annulla modifiche. Le operazioni restituite sono consultive, non JSON Patch eseguibili. Chi le applica manualmente deve ottenere una nuova istantanea e verificare dopo ogni modifica esaminata: indici e versioni possono essere cambiati. Gli hash non offrono firme né controllo degli accessi.

I rapporti possono contenere nomi e identificatori privati. Non inserirli in Git pubblico, issue tracker o artefatti CI. Gli esempi pubblici usano dispositivi sintetici e non dichiarano verifiche sul campo. La diagnostica blocca il piano per scelta progettuale; non esistono flag di forzatura, liste di esclusione o modalità permissive nascoste.
