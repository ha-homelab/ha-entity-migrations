# Архитектура и контракт отчёта

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

[Модель](model.md) · [Ограничения](limitations.md)

![Поток данных только для чтения](../diagrams/pipeline.svg)

`io.py` обеспечивает ограничения файлов, путей и JSON и точность указателей. `planner.py` проверяет объявления, строит соответствия до и после, сканирует исходные значения, разрешает явные политики и собирает диагностические записи. `cli.py` добавляет переведённые сообщения и выводит отчёт. `i18n.py` содержит четыре полных словаря сообщений. На этом пути нет сетевых обращений или зависимости от Home Assistant.

Сканер намеренно консервативен. Строки, целиком похожие на идентификаторы сущностей, сверяются со снимком. Строки со встроенными ссылками остаются неразрешёнными. Шаблоны в ключах или значениях и ключи целей device/area/label остаются неразрешёнными, даже если ответ кажется очевидным. Обычные поля сервисов не считаются идентификаторами сущностей; динамические сервисы всё равно не разрешаются. Файлы не в JSON регистрируются как неподдерживаемые источники и блокируют планирование. Это не универсальный парсер HA.

![Выбор политики](../diagrams/policy.svg)

## Стабильная оболочка JSON, версия схемы 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Для корректных входных данных `status` равен ready или blocked. `scope` всегда равен `supplied_files_only`; `read_only` всегда true. Ошибки входа используют меньшую оболочку invalid, описанную в руководстве по установке.

Изменения содержат операцию, файл и указатель. `replace_reference` также содержит before/after/policy; `replace_service` — before/after; `remove_consumer` — выводимую из использования ссылку. Это **не исполняемый JSON Patch**. Здесь нет семантики транзакций, сдвига индексов и жизненного цикла HA. Рассматривайте их как предложения; в этом выпуске намеренно нет средства применения патчей.

Диагностики содержат стабильные `code`, `location`, `severity` и переведённое `message`. И `error`, и `unresolved` блокируют план. Отчёты `blocked` могут содержать предлагаемые изменения незатронутых ссылок, но они не образуют готовую транзакцию. Устаревшие или конфликтующие исходные модели подавляют все предлагаемые изменения ссылок. Назначения всегда повторяют запрошенную пользователем модель, а не выполненные изменения.

Для воспроизводимости отчёты сортируют источники, назначения, изменения и диагностики. Текущих временных меток или выдуманных оценок уверенности нет. Хеши байтов подтверждают версию проанализированного входа, но не его истинность и не то, что устройство выполнит команду.
