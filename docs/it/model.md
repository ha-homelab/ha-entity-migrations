# Modello di input

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

[Installazione](installation.md) · [Esempi](examples.md)

Tutti i documenti usano JSON rigoroso UTF-8. Chiavi duplicate, numeri non finiti e campi di schema sconosciuti vengono rifiutati. Gli esempi esatti in `examples/` sono il riferimento eseguibile. I campi di versione devono contenere l'intero `1`, non una stringa o un booleano.

## Istantanea

L'oggetto principale contiene solo `version` e `entities`. Ogni entità contiene esattamente:

- `entity_id`: ID dominio/oggetto in minuscolo, come `light.workbench`.
- `hardware_id`: identificatore privato opaco scelto dall'operatore.
- `channel`: identificatore del canale fisico, come stringa.
- `role`: scopo logico unico, come `workbench` o `pump_enable`.
- `capabilities`: stringhe uniche che descrivono capacità, per esempio `on_off`.

La coppia hardware/canale identifica un endpoint fisico. ID di entità, endpoint fisici e ruoli logici devono essere ciascuno unici. Rappresenta una diagnostica fisica come canale distinto, ad esempio `rssi`, con un proprio ruolo unico. Un ruolo è un'etichetta di pianificazione, non un'area, etichetta o classe di dispositivo HA. Queste dichiarazioni non sono misure; lo strumento non può verificarle sull'hardware.

## Manifesto

L'oggetto principale ha esattamente `version`, `snapshot_sha256`, `sources`, `assignments` e `consumers`. `sources` associa nomi relativi di file a digest SHA-256. `assignments` contiene record completi di sostituzione per endpoint fisici già presenti nell'istantanea. Gli endpoint non elencati rimangono invariati. Per aggiungere un dispositivo, includi prima nell'istantanea il suo endpoint di riserva osservato. Non esistono creazione o eliminazione implicite di hardware; questa versione richiede ruoli unici.

Ogni consumatore identifica un **valore stringa letterale** mediante `file` e un `pointer` RFC 6901. Effettua l'escape di `/` come `~1` e di `~` come `~0`; gli indici delle liste partono da zero senza zeri iniziali. Ogni riferimento rilevato richiede una politica esplicita:

- `follows_role`: trovare la destinazione che possiede il ruolo logico della sorgente.
- `follows_hardware`: mantenere il canale fisico sorgente e usare il suo nuovo ID di entità.
- `retire`: proporre la rimozione dell'oggetto esplicito `retire_scope` contenente il riferimento.

I consumatori non ritirati richiedono anche `kind` (`action`, `display`, `reference`), `allowed_roles` (non vuoto) e `required_capabilities` (eventualmente vuoto). Le azioni richiedono `service_pointer`. Questi vincoli impediscono di usare una pompa riutilizzata come destinazione di illuminazione. Sono dichiarazioni, non intenzioni dedotte.

I consumatori ritirati hanno esattamente quattro campi: file, pointer, policy e retire_scope. L'ambito deve essere un oggetto antenato diverso dalla radice. Può contenere solo riferimenti alla medesima sorgente ritirata; riferimenti misti o dinamici lo bloccano. Se rimuovere un'azione lascerebbe una sequenza vuota non valida, seleziona l'intera automazione obsoleta. Lo strumento non esegue il validatore di schema HA.

## Cambi di dominio

Per un'azione che attraversa light/switch sono supportati solo `turn_on`, `turn_off`, `toggle` e i corrispondenti servizi `homeassistant.*`. `data` o `data_template` non vuoti non sono ammessi nella conversione automatica. Un servizio specifico del dominio con più destinazioni letterali viene bloccato. Il puntatore del servizio deve possedere la destinazione sotto la propria azione. Cambiare dominio di visualizzazione richiede sempre revisione manuale delle funzioni della scheda; un interruttore non può ereditare silenziosamente i controlli di luminosità.

## Limiti

2 MiB per file; 16 MiB complessivi di sorgenti; 64 file; 5.000 entità, assegnazioni o consumatori; profondità JSON 40 e 100.000 nodi valore per file. Gli identificatori sono stringhe non vuote di massimo 256 caratteri; le liste di capacità/ruoli consentiti contengono massimo 64 stringhe uniche. I percorsi relativi non possono risalire, essere assoluti o contenere collegamenti simbolici. Sono ammessi solo file regolari.

Il caricatore rifiuta due nomi sorgente che risolvono allo stesso percorso canonico o alla stessa identità di file aperto (dispositivo/inode). Include separatori ripetuti, hard link e alias di maiuscole/minuscole su filesystem non sensibili alla distinzione. Mantieni un solo nome e aggiorna i consumatori: gli alias non possono attribuire politiche diverse a uno stesso file fisico. File indipendenti dal contenuto identico restano validi. L'API pura `plan` non accede al filesystem: chi costruisce autonomamente la mappa delle sorgenti deve imporre questo confine di identità prima della chiamata.
