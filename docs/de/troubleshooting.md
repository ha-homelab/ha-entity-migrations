# Fehlerbehebung

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

[Installation](installation.md) · [Einschränkungen](limitations.md)

**Befehl nicht gefunden:** Aktivieren Sie dieselbe virtuelle Umgebung wie bei der Installation. Versuchen Sie `python3 -m ha_entity_migrations --version`; installieren Sie nicht in das System-Python, nur um einen Pfadfehler zu umgehen.

**Exit 2, schema_invalid:** Vergleichen Sie die Schlüssel mit dem ausführbaren Beispiel und dem [Eingabemodell](model.md). Unbekannte Felder sind Fehler. Versionen sind die Ganzzahl 1; Kanalkennungen sind Zeichenfolgen. Jede Aktionsrichtlinie benötigt ihren Service-Zeiger. Ein Snapshot enthält Entities, ein Manifest Zuweisungen und Verbraucher. Die Dateien sind nicht austauschbar.

**Exit 2, duplicate_source:** Zwei Quellnamen bezeichnen dieselbe physische Datei. Behalten Sie einen kanonischen Namen in `sources` und passen Sie alle `file`-Felder der Verbraucher an. Entfernen Sie doppelte Trenner oder Hardlink-/Schreibungsaliase; geben Sie einem Alias keine zweite Richtlinie. Separate Dateien mit identischem Inhalt bleiben unterstützt.

**stale_snapshot / stale_source:** Vergleichen Sie tatsächliche Änderungen mit der freigegebenen Quelle. Verwenden Sie den Fingerprint-Befehl erst nach deren Prüfung. Leerraumänderungen beeinflussen den Hash. Verweisen Sie nicht auf eine veraltete Kopie, nur damit der alte Hash passt.

**source_collision / destination_collision:** Ein physischer Kanal, eine Rolle oder eine Entity-ID ist doppelt. Beschreiben Sie beide Seiten eines Rollentauschs explizit und prüfen Sie, ob ein unveränderter Endpunkt die gewünschte Ziel-ID behält.

**role_not_allowed / capability_missing:** Der Verbraucher würde eine ungeeignete Last erreichen oder eine Fähigkeit verlieren. Klären Sie, ob er Rolle oder Hardware folgen soll. Erweitern Sie allowed_roles nicht automatisch und behaupten Sie keine Fähigkeiten, die der Hardware fehlen. Ein Ein-/Aus-Relais als Lichtersatz kann nicht dimmen.

**missing_policy / unmodeled_reference:** Erfassen Sie den referenzierten Endpunkt und ergänzen Sie eine explizite Verbraucherdeklaration erst nach Klärung ihres Zwecks. Eine alte Verlaufszeichenfolge kann außerhalb des aktiven Umfangs liegen; schließen Sie die Datei bewusst aus, dokumentieren Sie das und erzeugen Sie den Quellvertrag erneut.

**dynamic_reference / embedded_reference / indirect_target:** Diese Version kann die Zuordnung nicht beweisen. Prüfen Sie Jinja oder Gruppen-/Bereichs-/Label-Verhalten separat oder liefern Sie eine explizite normalisierte literale Konfiguration. Das Programm führt niemals ein Template aus.

**display_domain_review / service_data_review / mixed_action_targets:** Prüfen Sie Kartenfunktionen, Aktionsparameter und Zielgruppen. Teilen Sie eine Aktion über mehrere Domains in einer separat geprüften Quelländerung auf; ändern Sie nicht bloß deren Service-Domain.

**retire_scope_mixed / overlapping_edits:** Wählen Sie ein zusammenhängendes veraltetes Verbraucherobjekt ohne fremde Verweise. Löschen Sie nicht nur entity_id aus einer Aktion: Dadurch könnte ein zu breites Ziel oder eine ungültige Konfiguration entstehen. Dieses Programm führt keine automatische Stilllegung aus.

**unsupported_source:** Nur JSON lässt sich planen. YAML, Binär- und andere Dateien werden nicht stillschweigend übersprungen. Eine explizit normalisierte JSON-Kopie kann die Analyse erleichtern, muss aber vor realen Änderungen mit dem Original verglichen werden.

Melden Sie Fehler mit minimalen synthetischen Eingaben, Werkzeug-/Python-Version, Exitcode und Diagnosecodes. Fügen Sie niemals einen unbearbeiteten Haushaltsexport oder API-Zugangsdaten bei.
