# Розібрані приклади

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

[Модель входу](model.md) · [Архітектура](architecture.md)

Усе обладнання й ролі тут синтетичні. Відтворіть ідентичні вхідні дані командою `python3 tools/generate_examples.py`. Жодна команда не підключається до Home Assistant.

## Роль лампи залишає розетку з новим призначенням

Виконайте команду з README для `examples/role-swap`. Спочатку `plug-a/1` володіє `light.workbench`, а `plug-b/1` — `switch.spare`. Маніфест призначає розетці A роль насоса, а розетці B — роль робочого столу. Автоматизація освітлення використовує `follows_role` і дозволяє лише `workbench`. Її посилання залишається `light.workbench`, хоча цільове обладнання змінюється. Відсутність текстової правки — очікуваний результат, а не пропущена міграція. Поле `assignments` звіту містить зміни обладнання для перевірки людиною.

Старий резервний споживач вилучається за `/1` — як цілий другий об'єкт автоматизації. Це не залишає порожньої послідовності дій. Звіт має рекомендаційний характер; програма не видаляє елементи масиву JSON. Застосовуючи вручну кілька запропонованих видалень, враховуйте зсув індексів і повторіть запуск зі свіжим знімком.

Змініть першу політику на `follows_hardware`, залишивши дозволену роль `workbench`: план заблокується з `role_not_allowed`. Розширення списку дозволених ролей насосом — явна небезпечна зміна наміру, а не звичайний спосіб прибрати помилку. Натомість відновіть правильну політику.

## Реле переходить із light до switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Дві запропоновані правки змінюють ціль і її сервіс `light.turn_off`. Додайте дані яскравості до вихідної дії, оновіть схвалений відбиток джерела та запустіть знову: `service_data_review` блокує автоматичне перетворення. Не видаляйте параметри яскравості лише заради проходження перевірки; оцініть бажану поведінку.

## Нерозв'язаний шаблон

Виконайте ту саму команду з `examples/blocked-template`. Ціль — динамічний Jinja. Засіб не обчислює його й повертає код 3. Повний підтримуваний план потребує явної конфігурації з довідними літеральними цілями; інакше залиште цю частину документованою ручною міграцією поза готовим обсягом. Ігнорування коду завершення не розв'язує шаблон.

## Відхилення та повторюваність

Редагування джерела без зміни його хешу в маніфесті дає `stale_source`. Редагування знімка дає `stale_snapshot`. Для цих застарілих моделей не виводяться запропоновані зміни посилань. За незмінних файлів результат JSON детермінований, окрім обраної мови. Вихідні файли залишаються незмінними байт у байт.

Для реального проєкту скопіюйте формат у приватну теку, перевірте фізичні ідентичності, перелічіть споживачів і запустіть планувальник. Перевірте всі призначення та зміни, виконайте власні перевірки HA в усталеному процесі розгортання, а потім створіть новий знімок лише для читання, щоб перевірити результат. Цей проєкт не реалізує такого розгортання чи виконавця відкату.
