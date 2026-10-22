# Installazione e CLI

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

[Indice della documentazione](../../README.md#documentation)

Usa Python 3.11 o successivo. Crea e attiva un ambiente virtuale dedicato, poi esegui `python3 -m pip install -e .` dalla copia del repository. Il pacchetto non ha dipendenze di esecuzione; pip può scaricare il backend di compilazione. Per una macchina offline, prepara prima il wheel e le dipendenze di compilazione. Verifica l'installazione scelta con `ha-entity-migrations --version`, che mostra la versione del pacchetto installato.

La CLI ha due comandi, con l'opzione globale della lingua prima del comando:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` stampa lo SHA-256 in minuscolo dei byte esatti del file. Non convalida il file come JSON. Le impronte di istantanea e sorgenti nel manifesto devono corrispondere ai file esatti, spazi compresi. Non aggiornare un'impronta solo per ignorare una deriva inattesa: confronta e approva prima il nuovo input.

`plan` legge un manifesto JSON, un'istantanea JSON normalizzata e solo i file nominati esplicitamente in `manifest.sources`, relativi a `--root`. Non percorre ricorsivamente directory né cerca nella cartella personale. L'output predefinito è JSON. Con `--lang en|ru|de|es` cambiano soltanto i messaggi umani; nomi dei campi e codici diagnostici restano stabili. `--help` è disponibile al livello principale e per ogni comando. Non esistono comandi per applicare, caricare, rilevare o autenticarsi.

Stato di uscita:

- **0:** l'ambito di input supportato è coerente internamente e pronto per la revisione.
- **2:** argomenti/input non validi, file illeggibile o violazione di schema/limiti.
- **3:** input strutturalmente valido ha prodotto un piano bloccato da conflitti o ambito irrisolto.

Gli errori di input dopo l'analisi degli argomenti producono su stdout un involucro JSON con `status: invalid`. Gli errori degli argomenti stampano istruzioni localizzate su stderr. Il calcolo riuscito dell'impronta stampa soltanto il digest. In modalità testo, le modifiche proposte mantengono i nomi macchina dei campi; le spiegazioni sono tradotte.

Conserva i file operativi in una directory privata. Reindirizzando stdout crei un rapporto che può contenere nomi identificativi di entità e percorsi. Lo strumento non scrive nulla da sé. Disinstalla con `python3 -m pip uninstall ha-entity-migrations`. Per i controlli di sviluppo, vedi [CONTRIBUTING](../../CONTRIBUTING.md).
