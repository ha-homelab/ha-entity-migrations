# Esempi svolti

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

[Modello di input](model.md) · [Architettura](architecture.md)

Tutti i dispositivi e i ruoli qui sono sintetici. Ricrea input identici con `python3 tools/generate_examples.py`. Nessun comando si connette a Home Assistant.

## Il ruolo lampada lascia una presa riutilizzata

Esegui il comando del README per `examples/role-swap`. Inizialmente `plug-a/1` possiede `light.workbench` e `plug-b/1` possiede `switch.spare`. Il manifesto assegna il ruolo pompa alla presa A e quello banco di lavoro alla B. L'automazione di illuminazione usa `follows_role` e permette soltanto `workbench`. Il riferimento resta `light.workbench` mentre cambia l'hardware di destinazione. L'assenza di modifiche testuali è voluta, non una migrazione mancante. `assignments` nel rapporto contiene i cambiamenti hardware da esaminare manualmente.

Il vecchio consumatore di riserva viene ritirato in `/1`, l'intero secondo oggetto di automazione. Così non resta una sequenza di azioni vuota. Il rapporto è consultivo: il programma non elimina elementi dell'array JSON. Applicando manualmente più rimozioni proposte, considera lo spostamento degli indici ed esegui nuovamente da un'istantanea aggiornata.

Cambia la prima politica in `follows_hardware` lasciando `workbench` come ruolo consentito: il piano si blocca con `role_not_allowed`. Estendere la lista per includere una pompa cambia esplicitamente l'intento in modo pericoloso, non è un rimedio ordinario all'errore. Ripristina invece la politica corretta.

## Un relè passa da light a switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Le due modifiche proposte cambiano la destinazione e il suo servizio `light.turn_off`. Aggiungi dati di luminosità all'azione sorgente, aggiorna l'impronta sorgente approvata e ripeti: `service_data_review` blocca la conversione automatica. Non eliminare le impostazioni di luminosità solo per soddisfare lo strumento; esamina il comportamento desiderato.

## Un template irrisolto

Esegui lo stesso comando con `examples/blocked-template`. La destinazione è Jinja dinamico. Lo strumento non lo valuta e restituisce codice 3. Un piano completo supportato richiede configurazione esplicita con destinazioni letterali dimostrabili; altrimenti mantieni questa parte come migrazione manuale documentata fuori dall'ambito pronto. Ignorare il codice di uscita non risolve il template.

## Deriva e ripetibilità

Modificare una sorgente senza cambiarne l'hash nel manifesto produce `stale_source`. Modificare l'istantanea produce `stale_snapshot`. Questi modelli obsoleti non generano modifiche candidate ai riferimenti. Con file invariati, il risultato JSON è deterministico salvo la lingua scelta. I file sorgente restano identici byte per byte.

Per un progetto reale, copia il formato in una cartella privata, verifica le identità fisiche, elenca i consumatori ed esegui il pianificatore. Esamina tutte le assegnazioni e modifiche, effettua i controlli propri di HA nel processo di distribuzione abituale e crea poi una nuova istantanea in sola lettura per verificare il risultato. Questo progetto non implementa tale distribuzione né un esecutore di rollback.
