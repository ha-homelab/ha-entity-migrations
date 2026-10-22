# Risoluzione dei problemi

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

[Installazione](installation.md) · [Limiti](limitations.md)

**Comando non trovato:** attiva lo stesso ambiente virtuale usato per installare. Prova `python3 -m ha_entity_migrations --version`; non installare nel Python di sistema solo per aggirare un percorso errato.

**Uscita 2, schema_invalid:** confronta le chiavi con l'esempio eseguibile e il [modello di input](model.md). I campi sconosciuti sono errori. Le versioni sono l'intero 1; gli identificatori di canale sono stringhe. Ogni politica di azione necessita del suo puntatore di servizio. Un'istantanea ha entità; un manifesto assegnazioni e consumatori. I file non sono intercambiabili.

**Uscita 2, duplicate_source:** due nomi identificano un file fisico. Mantieni un nome canonico in `sources` e aggiorna tutti i campi `file` dei consumatori. Elimina separatori doppi e alias da hard link o maiuscole; non assegnare una seconda politica a un alias. File distinti con contenuto identico rimangono supportati.

**stale_snapshot / stale_source:** confronta le modifiche effettive con la sorgente approvata. Usa fingerprint solo dopo averle esaminate. Gli spazi influiscono sull'hash. Non puntare a una copia obsoleta solo per far corrispondere il vecchio hash.

**source_collision / destination_collision:** un canale fisico, ruolo o ID di entità è duplicato. Esprimi esplicitamente entrambi i lati dello scambio di ruoli e verifica che un endpoint invariato non conservi l'ID di destinazione desiderato.

**role_not_allowed / capability_missing:** il consumatore raggiungerebbe un carico inappropriato o perderebbe una capacità. Conferma se deve seguire ruolo o hardware. Non ampliare automaticamente allowed_roles né dichiarare capacità assenti. Una luce sostituita da un relè on/off non può regolare la luminosità.

**missing_policy / unmodeled_reference:** censisci l'endpoint referenziato e aggiungi una dichiarazione esplicita solo dopo averne confermato lo scopo. Una vecchia stringa storica può essere fuori dall'ambito attivo; escludi deliberatamente quel file, documenta l'esclusione e rigenera il contratto delle sorgenti.

**dynamic_reference / embedded_reference / indirect_target:** questa versione non può dimostrare la corrispondenza. Esamina separatamente Jinja o il comportamento di gruppi/aree/etichette, oppure fornisci configurazione letterale normalizzata esplicita. Il programma non esegue mai un template.

**display_domain_review / service_data_review / mixed_action_targets:** ispeziona funzioni delle schede, parametri delle azioni e gruppi di destinazioni. Dividi un'azione multidominio in una modifica sorgente esaminata separatamente; non cambiarne soltanto il dominio del servizio.

**retire_scope_mixed / overlapping_edits:** scegli un oggetto consumatore obsoleto coerente, senza riferimenti estranei. Non cancellare solo entity_id da un'azione: potresti creare una destinazione troppo ampia o configurazione non valida. Il programma non applica ritiri automatici.

**unsupported_source:** si può pianificare solo JSON. YAML, binari e altri file non vengono ignorati silenziosamente. Una copia JSON normalizzata esplicitamente può aiutare l'analisi, ma va confrontata con l'originale prima di modifiche reali.

Segnala bug con un input sintetico minimo, versioni strumento/Python, codice di uscita e codici diagnostici. Non allegare mai esportazioni domestiche grezze o credenziali API.
