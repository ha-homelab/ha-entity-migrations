# Усунення несправностей

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

[Встановлення](installation.md) · [Обмеження](limitations.md)

**Команду не знайдено:** активуйте те саме віртуальне середовище, яке використовувалося для встановлення. Спробуйте `python3 -m ha_entity_migrations --version`; не встановлюйте в системний Python лише для обходу невідповідного шляху.

**Код 2, schema_invalid:** порівняйте ключі з виконуваним прикладом і [моделлю входу](model.md). Невідомі поля — помилки. Версії — ціле число 1, ідентифікатори каналів — рядки. Кожна політика дії потребує вказівника сервісу. Знімок містить сутності, маніфест — призначення й споживачів. Ці файли невзаємозамінні.

**Код 2, duplicate_source:** два імені джерел визначають один фізичний файл. Залиште одне канонічне ім'я в `sources` і оновіть усі поля `file` споживачів. Приберіть дублікати роздільників, жорсткі посилання чи регістрові псевдоніми; не давайте псевдоніму другу політику. Окремі файли з однаковим вмістом залишаються підтримуваними.

**stale_snapshot / stale_source:** порівняйте фактичні зміни зі схваленим джерелом. Використовуйте fingerprint лише після їх перегляду. Пробільні зміни впливають на хеш. Не вказуйте застарілу копію тільки заради збігу старого хешу.

**source_collision / destination_collision:** фізичний канал, роль чи ID сутності дублюється. Явно опишіть обидва боки обміну ролями та перевірте, чи незмінна точка не утримує бажаний цільовий ID.

**role_not_allowed / capability_missing:** споживач потрапить на невідповідне навантаження або втратить можливість. Уточніть, чи має він слідувати за роллю, чи за обладнанням. Не розширюйте allowed_roles автоматично й не декларуйте можливості, яких обладнання не має. Лампа, замінена реле ввімкнення/вимкнення, не може регулювати яскравість.

**missing_policy / unmodeled_reference:** інвентаризуйте точку, на яку є посилання, і додавайте явну декларацію споживача лише після підтвердження призначення. Старий історичний рядок може бути поза активним обсягом; свідомо вилучіть файл з обсягу, задокументуйте виключення та відновіть контракт джерел.

**dynamic_reference / embedded_reference / indirect_target:** ця версія не може довести відповідність. Перевірте Jinja чи поведінку груп/областей/міток окремо або надайте явну нормалізовану літеральну конфігурацію. Програма ніколи не виконує шаблони.

**display_domain_review / service_data_review / mixed_action_targets:** перевірте функції карток, параметри дій і групи цілей. Розділіть багатодоменну дію в окремо переглянутій зміні джерела; не змінюйте лише домен сервісу.

**retire_scope_mixed / overlapping_edits:** оберіть цілісний застарілий об'єкт споживача без сторонніх посилань. Не видаляйте з дії лише entity_id: це може створити надто широку ціль або некоректну конфігурацію. Ця програма не застосовує автоматичне вилучення.

**unsupported_source:** планувати можна лише JSON. YAML, бінарні й інші файли не пропускаються мовчки. Явно нормалізована копія JSON може допомогти аналізу, але її слід порівняти з оригіналом перед реальною правкою.

Повідомляйте про помилки з мінімальним синтетичним входом, версіями засобу/Python, кодом завершення та діагностичними кодами. Ніколи не додавайте необроблений експорт домівки чи облікові дані API.
