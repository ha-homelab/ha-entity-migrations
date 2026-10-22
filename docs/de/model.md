# Eingabemodell

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

[Installation](installation.md) · [Beispiele](examples.md)

Alle Dokumente verwenden striktes UTF-8-JSON. Doppelte Schlüssel, nicht endliche Zahlen und unbekannte Schemafelder werden abgelehnt. Die exakten Beispiele in `examples/` sind die ausführbare Referenz. Versionsfelder müssen die Ganzzahl `1` enthalten, keine Zeichenfolge und keinen booleschen Wert.

## Snapshot

Das oberste Objekt enthält nur `version` und `entities`. Jede Entity enthält genau:

- `entity_id`: Domain-/Objekt-ID in Kleinbuchstaben, etwa `light.workbench`.
- `hardware_id`: private, undurchsichtige, vom Betreiber gewählte Kennung.
- `channel`: Kennung des physischen Kanals als Zeichenfolge.
- `role`: eindeutiger logischer Zweck, etwa `workbench` oder `pump_enable`.
- `capabilities`: eindeutige Zeichenfolgen für Fähigkeiten, zum Beispiel `on_off`.

Das Paar Hardware/Kanal identifiziert einen physischen Endpunkt. Entity-IDs, physische Endpunkte und logische Rollen müssen jeweils eindeutig sein. Stellen Sie eine physische Diagnose als eigenen Kanal dar, etwa `rssi`, mit eigener eindeutiger Rolle. Eine Rolle ist eine Planungsbezeichnung, kein Home-Assistant-Bereich, -Label oder -Gerätetyp. Diese Deklarationen sind keine Messungen; das Werkzeug kann sie nicht an der Hardware überprüfen.

## Manifest

Das oberste Objekt enthält genau `version`, `snapshot_sha256`, `sources`, `assignments` und `consumers`. `sources` ordnet relativen Dateinamen SHA-256-Hashes zu. `assignments` enthält vollständige Ersatzdatensätze für bereits im Snapshot vorhandene physische Endpunkte. Nicht aufgeführte Endpunkte bleiben unverändert. Für ein neues Gerät nehmen Sie zuerst dessen beobachteten Reserveendpunkt in den Snapshot auf. Hardware wird nicht implizit erstellt oder gelöscht, und diese Version verlangt eindeutige Rollen.

Jeder Verbraucher identifiziert einen **literalen Zeichenfolgenwert** mittels `file` und RFC-6901-`pointer`. Maskieren Sie `/` als `~1` und `~` als `~0`; Listenindizes beginnen bei null und haben keine führenden Nullen. Jeder entdeckte Verweis benötigt eine explizite Richtlinie:

- `follows_role`: Ziel finden, das die logische Rolle der Quelle besitzt.
- `follows_hardware`: physischen Quellkanal beibehalten und dessen neue Entity-ID verwenden.
- `retire`: Entfernung des expliziten Objekts `retire_scope` vorschlagen, das den Verweis enthält.

Nicht stillzulegende Verbraucher benötigen zusätzlich `kind` (`action`, `display`, `reference`), `allowed_roles` (nicht leer) und `required_capabilities` (gegebenenfalls leer). Aktionen benötigen `service_pointer`. Diese Schranken verhindern, dass eine umgewidmete Pumpe als Lichtziel dient. Es sind Deklarationen, keine abgeleitete Absicht.

Stillzulegende Verbraucher haben genau vier Felder: file, pointer, policy und retire_scope. Der Umfang muss ein übergeordnetes Objekt unterhalb der Wurzel sein. Es darf nur Verweise auf dieselbe stillzulegende Quelle enthalten; gemischte oder dynamische Verweise blockieren es. Wählen Sie eine ganze veraltete Automation aus, wenn das Entfernen einer Aktion eine ungültige leere Folge hinterließe. Das Werkzeug führt HAs Schemavalidierung nicht aus.

## Domain-Wechsel

Bei Aktionen zwischen light und switch werden nur `turn_on`, `turn_off`, `toggle` und passende `homeassistant.*`-Services unterstützt. Für eine automatische Service-Umwandlung werden keine nicht leeren `data` oder `data_template` akzeptiert. Ein domainspezifischer Service mit mehreren literalen Zielen wird blockiert. Der Service-Zeiger muss das Ziel unter seiner Aktion besitzen. Ein Domain-Wechsel in Anzeigen erfordert immer eine manuelle Prüfung der Kartenfunktionen; ein Schalter darf nicht stillschweigend Helligkeitsregler übernehmen.

## Grenzen

2 MiB pro Datei; insgesamt 16 MiB Quelldateien; 64 Dateien; 5.000 Entities, Zuweisungen oder Verbraucher; JSON-Tiefe 40 und 100.000 Wertknoten pro Datei. Kennungen sind nicht leere Zeichenfolgen bis 256 Zeichen, Fähigkeits-/Rollenlisten enthalten bis zu 64 eindeutige Zeichenfolgen. Relative Quellpfade dürfen weder nach oben führen noch absolut sein oder symbolische Links enthalten. Eingaben sind ausschließlich reguläre Dateien.

Der Dateilader lehnt zwei Quellnamen ab, die denselben kanonischen Pfad oder dieselbe Identität einer geöffneten Datei (Gerät/Inode) ergeben. Dazu gehören wiederholte Pfadtrenner, Hardlinks und Groß-/Kleinschreibungsaliase auf entsprechenden Dateisystemen. Behalten Sie einen Quellnamen und aktualisieren Sie dessen Verbraucher; Aliase dürfen nicht verschiedene Migrationsrichtlinien für dieselbe physische Datei tragen. Unabhängige Dateien mit identischem Inhalt bleiben gültig. Die reine `plan`-API hat keinen Dateisystemzugriff: Aufrufer, die ihre Quellzuordnung selbst erstellen, müssen diese Identitätsgrenze vor dem Aufruf durchsetzen.
