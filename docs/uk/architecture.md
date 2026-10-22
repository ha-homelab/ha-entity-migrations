# Архітектура та контракт звіту

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

[Модель](model.md) · [Обмеження](limitations.md)

![Потік даних лише для читання](../diagrams/pipeline.svg)

`io.py` забезпечує обмеження файлів, шляхів і JSON та точні вказівники. `planner.py` перевіряє декларації, будує відповідності до/після, сканує вихідні значення, застосовує явні політики й накопичує діагностичні записи. `cli.py` додає перекладені повідомлення та виводить звіт. `i18n.py` містить чотири повні каталоги повідомлень. Цей шлях не залежить від мережі чи Home Assistant.

Сканер навмисно обережний. Рядки, що точно відповідають посиланням на сутності, перевіряються за знімком. Рядки з вбудованими посиланнями залишаються нерозв'язаними. Шаблони в ключах або значеннях і ключі цілей пристрою/області/мітки залишаються нерозв'язаними, навіть якщо їхнє значення здається очевидним. Звичайні поля сервісів не вважаються ID сутностей; динамічні сервіси залишаються нерозв'язаними. Файли не у форматі JSON реєструються як непідтримувані джерела та блокують планування. Це не універсальний парсер HA.

![Ухвалення рішень за політиками](../diagrams/policy.svg)

## Стабільна оболонка JSON, версія схеми 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Для коректного входу `status` має значення ready або blocked. `scope` завжди дорівнює `supplied_files_only`, а `read_only` — true. Помилки входу використовують меншу оболонку invalid, описану в інструкції зі встановлення.

Зміни містять операцію, файл і вказівник. `replace_reference` також містить before/after/policy; `replace_service` містить before/after; `remove_consumer` містить посилання, що вилучається. Це **не виконуваний JSON Patch**. Тут немає семантики транзакцій, зсуву індексів і життєвого циклу HA. Розглядайте їх як пропозиції; ця версія навмисно не надає засобу застосування патчів.

Діагностика містить стабільні `code`, `location`, `severity` та перекладене `message`. І `error`, і `unresolved` блокують план. Звіти `blocked` можуть містити запропоновані зміни для незачеплених посилань, але жодна з них не є готовою транзакцією. Застарілі або суперечливі початкові моделі пригнічують усі запропоновані зміни посилань. Призначення завжди повторюють запитану користувачем модель, а не вже виконані зміни.

Для відтворюваності звіти сортують джерела, призначення, зміни та діагностику. Немає поточних часових позначок чи вигаданих оцінок упевненості. Хеші байтів доводять, яку версію входу було проаналізовано, а не його правдивість чи те, що пристрій виконає команду.
