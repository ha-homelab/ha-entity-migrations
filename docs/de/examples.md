# Durchgearbeitete Beispiele

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

[Eingabemodell](model.md) · [Architektur](architecture.md)

Alle Geräte und Rollen hier sind synthetisch. Mit `python3 tools/generate_examples.py` erzeugen Sie identische Eingaben erneut. Kein Befehl verbindet sich mit Home Assistant.

## Eine Lampenrolle verlässt eine umgewidmete Steckdose

Führen Sie den README-Befehl für `examples/role-swap` aus. Anfangs besitzt `plug-a/1` die Entity `light.workbench` und `plug-b/1` die Entity `switch.spare`. Das Manifest weist Steckdose A die Pumpenrolle und Steckdose B die Werkbankrolle zu. Die Lichtautomation verwendet `follows_role` und erlaubt ausschließlich `workbench`. Ihr Entity-Verweis bleibt `light.workbench`, während sich die Zielhardware ändert. Dass keine Textänderung entsteht, ist beabsichtigt und keine fehlende Migration. Die `assignments` des Berichts enthalten die Hardwareänderungen zur menschlichen Prüfung.

Der bisherige Reserveverbraucher wird bei `/1` stillgelegt, also als vollständiges zweites Automationsobjekt. Dadurch bleibt keine leere Aktionsfolge zurück. Der Bericht ist nur eine Empfehlung; das Programm entfernt kein JSON-Arrayelement. Wenn Sie mehrere vorgeschlagene Array-Löschungen manuell durchführen, berücksichtigen Sie verschobene Indizes und starten Sie mit einem frischen Snapshot erneut.

Ändern Sie die erste Richtlinie zu `follows_hardware`, lassen Sie aber `workbench` als erlaubte Rolle bestehen: Der Plan wird mit `role_not_allowed` blockiert. Die Liste um eine Pumpe zu erweitern ist eine explizite gefährliche Absichtsänderung, keine übliche Fehlerbehebung. Stellen Sie stattdessen die richtige Richtlinie wieder her.

## Ein Relais wechselt von light zu switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Die zwei vorgeschlagenen Änderungen betreffen das Ziel und dessen Service `light.turn_off`. Ergänzen Sie die Quellaktion um Helligkeitsdaten, aktualisieren Sie den freigegebenen Quellfingerabdruck und führen Sie den Befehl erneut aus: `service_data_review` blockiert die automatische Umwandlung. Entfernen Sie Helligkeitseinstellungen nicht bloß, um die Prüfung zu bestehen; prüfen Sie das gewünschte Verhalten.

## Ein ungeklärtes Template

Führen Sie denselben Befehl mit `examples/blocked-template` aus. Das Ziel ist dynamisches Jinja. Das Werkzeug wertet es nicht aus und liefert Code 3. Ein vollständiger unterstützter Plan benötigt explizite Konfiguration mit nachweisbaren literalen Zielen; andernfalls bleibt dies eine dokumentierte manuelle Migration außerhalb des freigegebenen Umfangs. Das Ignorieren des Exitcodes löst das Template nicht auf.

## Abweichungen und Wiederholbarkeit

Eine Quelländerung ohne angepassten Manifest-Hash erzeugt `stale_source`. Eine Snapshot-Änderung erzeugt `stale_snapshot`. Für solche veralteten Modelle werden keine Verweisänderungskandidaten ausgegeben. Bei unveränderten Dateien ist das JSON-Ergebnis abgesehen von der gewählten Sprache deterministisch. Quelldateien bleiben Byte für Byte unverändert.

Übernehmen Sie das Format für ein echtes Projekt in einen privaten Ordner, überprüfen Sie physische Identitäten, erfassen Sie Verbraucher und führen Sie den Planer aus. Prüfen Sie alle Zuweisungen und Änderungen, führen Sie HA-eigene Prüfungen im etablierten Bereitstellungsverfahren aus und erstellen Sie anschließend einen neuen schreibgeschützten Snapshot zur Ergebniskontrolle. Dieses Projekt implementiert weder diese Bereitstellung noch eine Rollback-Ausführung.
