# Architektur und Berichtsvertrag

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

[Modell](model.md) · [Einschränkungen](limitations.md)

![Schreibgeschützter Datenfluss](../diagrams/pipeline.svg)

`io.py` erzwingt Grenzen für Dateien, Pfade und JSON sowie exakte Zeiger. `planner.py` validiert die Deklarationen, erstellt Vorher-/Nachher-Zuordnungen, untersucht Quellwerte, löst explizite Richtlinien auf und sammelt Diagnosen. `cli.py` ergänzt übersetzte Meldungen und gibt den Bericht aus. `i18n.py` enthält vier vollständige Meldungskataloge. Dieser Ablauf hat keine Netzwerk- oder Home-Assistant-Abhängigkeit.

Der Scanner arbeitet bewusst vorsichtig. Zeichenfolgen, die exakt wie Entity-Verweise aussehen, werden gegen den Snapshot geprüft. Zeichenfolgen mit eingebetteten Verweisen bleiben ungeklärt. Templates in Schlüsseln oder Werten sowie Zielschlüssel für Geräte, Bereiche oder Labels bleiben ungeklärt, auch wenn eine Interpretation naheliegt. Einfache Service-Felder gelten nicht als Entity-IDs; dynamische Services bleiben jedoch ungeklärt. Nicht-JSON-Dateien werden als nicht unterstützte Quellen erfasst und blockieren die Planung. Dies ist kein allgemeiner HA-Parser.

![Entscheidungsablauf der Richtlinien](../diagrams/policy.svg)

## Stabiler JSON-Rahmen, Schemaversion 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Bei gültigen Eingaben ist `status` ready oder blocked. `scope` ist stets `supplied_files_only`; `read_only` ist stets true. Eingabefehler verwenden den kleineren invalid-Rahmen aus der Installationsanleitung.

Änderungsvorschläge haben eine Operation, eine Datei und einen Zeiger. `replace_reference` enthält außerdem before/after/policy; `replace_service` enthält before/after; `remove_consumer` enthält den stillzulegenden Verweis. Diese Vorschläge sind **kein ausführbarer JSON Patch**. Ihnen fehlen Transaktions-, Indexverschiebungs- und HA-Lebenszyklus-Semantik. Prüfen Sie sie als Vorschläge; diese Version stellt bewusst keinen Patch-Anwender bereit.

Diagnosen enthalten stabile Felder `code`, `location`, `severity` und eine übersetzte `message`. Sowohl `error` als auch `unresolved` blockieren einen Plan. Berichte mit `blocked` können Änderungskandidaten für nicht betroffene Verweise enthalten; keiner davon bildet jedoch eine ausführungsbereite Transaktion. Veraltete oder widersprüchliche Ausgangsmodelle unterdrücken alle Verweisänderungskandidaten. Zuweisungen geben immer das gewünschte Modell wieder, niemals bereits abgeschlossene Änderungen.

Berichte sortieren Quellen, Zuweisungen, Änderungen und Diagnosen für reproduzierbare Ergebnisse. Es gibt weder aktuelle Zeitstempel noch erfundene Konfidenzwerte. Byte-Hashes belegen die analysierte Eingabeversion, nicht deren Wahrheitsgehalt oder ob ein Gerät einen Befehl befolgt.
