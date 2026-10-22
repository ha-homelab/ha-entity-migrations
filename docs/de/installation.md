# Installation und CLI

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

[Dokumentationsübersicht](../../README.md#documentation)

Verwenden Sie Python 3.11 oder neuer. Erstellen und aktivieren Sie eine eigene virtuelle Umgebung und führen Sie im Checkout `python3 -m pip install -e .` aus. Das Paket hat keine Laufzeitabhängigkeiten; pip muss möglicherweise sein Build-Backend herunterladen. Bereiten Sie für einen Offline-Rechner Wheel und Build-Abhängigkeiten vorab vor. Prüfen Sie die ausgewählte Installation mit `ha-entity-migrations --version`; der Befehl meldet die installierte Paketversion.

Die CLI hat zwei Befehle; die globale Sprachoption steht vor dem Befehl:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` gibt den SHA-256-Hash der exakten Dateibytes in Kleinbuchstaben aus. Die Datei wird dabei nicht als JSON validiert. Snapshot- und Quellfingerabdrücke im Manifest müssen genau diesen Dateien einschließlich Leerraum entsprechen. Erneuern Sie einen Fingerabdruck nicht nur, um unerwartete Abweichungen zu verbergen; vergleichen und genehmigen Sie zuerst die neue Eingabe.

`plan` liest ein JSON-Manifest, einen normalisierten JSON-Snapshot und ausschließlich die in `manifest.sources` ausdrücklich genannten Dateien relativ zu `--root`. Es durchsucht weder Verzeichnisse rekursiv noch Ihr Home-Verzeichnis. Die Standardausgabe ist JSON. Bei `--lang en|ru|de|es` ändern sich nur menschenlesbare Meldungen; Feldnamen und Diagnosecodes bleiben stabil. `--help` ist auf oberster Ebene und für jeden Befehl verfügbar. Es gibt keinen Befehl zum Anwenden, Hochladen, Erkennen oder Authentifizieren.

Exitstatus:

- **0:** Der unterstützte Eingabeumfang ist intern konsistent und bereit zur Prüfung.
- **2:** Ungültige Argumente/Eingaben, nicht lesbare Datei oder Schema-/Grenzwertverletzung.
- **3:** Strukturell gültige Eingaben erzeugen einen blockierten Plan, etwa wegen Konflikten oder ungeklärtem Umfang.

Eingabefehler nach der Argumentverarbeitung erzeugen einen JSON-Rahmen mit `status: invalid` auf stdout. Argumentfehler geben lokalisierte Verwendungshinweise auf stderr aus. Eine erfolgreiche Fingerabdruckberechnung gibt nur den Hash aus. Im Textmodus behalten vorgeschlagene Änderungsdatensätze ihre maschinellen Feldnamen; Erläuterungen werden übersetzt.

Bewahren Sie Betriebsdateien in einem privaten Verzeichnis auf. Durch Umleiten von stdout erstellen Sie Ihren eigenen Bericht; er kann identifizierende Entity-Namen und Dateipfade enthalten. Das Werkzeug selbst schreibt nichts. Deinstallieren Sie mit `python3 -m pip uninstall ha-entity-migrations`. Entwicklerprüfungen stehen in [CONTRIBUTING](../../CONTRIBUTING.md).
