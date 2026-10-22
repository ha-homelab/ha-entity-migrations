# Einschränkungen und Prüfgrenzen

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

[Architektur](architecture.md) · [Sicherheit](../../SECURITY.md)

Ein Plan ist nur so genau wie seine Deklarationen von Hardware, Kanälen und Rollen und die bereitgestellten Dateien. Das Werkzeug entdeckt keine ausgelassenen Dashboards, Geräteauslöser, Szenen, Blueprints, andernorts gespeicherten Automationen, Matter-Filter, externen Clients oder verborgenen Integrationszustände. Ein freigegebener Bericht ist keine vollständige Home-Assistant-Prüfung. In dieser Version ist jede Rolle eindeutig; semantische Viele-zu-viele-Rollen und Gruppen müssen manuell zerlegt werden.

JSON-Konfigurationsquellen werden unterstützt. YAML selbst, Includes, Aliasse, Anker, ausführbare Tags, eigene Komponenten und zur Laufzeit erzeugte Templates werden nicht interpretiert. Normalisierung liegt außerhalb dieser Version und kann Semantik verlieren; bewahren Sie das Original auf und prüfen Sie die Gleichwertigkeit. Auch unterstütztes JSON wird nicht gegen das vollständige Home-Assistant-Konfigurationsschema geprüft. Das Entfernen eines expliziten Verbraucherobjekts kann ein ungültiges Elternobjekt hinterlassen; prüfen Sie dieses und führen Sie HAs Konfigurationsprüfung im normalen Staging-Verfahren aus.

Fähigkeiten und erlaubte Rollen sind explizite Einschränkungen, keine abgeleitete Sicherheit. Das Werkzeug kann nicht wissen, dass eine Pumpe oder ein Garagenantrieb an einer zuvor harmlosen Steckdose steckt. Ein gemeldeter Relaiszustand beweist nicht das Verhalten von Kontakt und Last. Führen Sie keine hausweiten Skripte aus und schalten Sie kein laufendes Gerät aus und ein, nur um Namen zu prüfen. Physische Inbetriebnahme gehört in ein separates kontrolliertes Verfahren.

Diese Version wendet keinen Plan an, benennt keine Registry-Entity um, ändert keine eindeutige ID, lädt HA nicht neu, startet keinen Controller neu, legt keine Integration still und setzt keine Änderung zurück. Zurückgegebene Operationen sind Empfehlungen, kein ausführbarer JSON Patch. Bei manueller Anwendung ist ein frischer Snapshot erforderlich; prüfen Sie nach jeder begutachteten Änderung, denn Indizes und Versionen können sich geändert haben. Hashes bieten weder Signaturen noch Zugriffskontrolle.

Berichte können private Namen und Kennungen enthalten. Halten Sie sie aus öffentlichen Git-Repositories, Issue-Trackern und CI-Artefakten heraus. Öffentliche Beispiele nutzen synthetische Geräte und behaupten keine Validierung im Einsatz. Diagnosen blockieren den Plan absichtlich; es gibt weder Force-Flag noch Ignorierliste oder versteckten großzügigen Modus.
