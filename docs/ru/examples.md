# Разобранные примеры

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

[Входная модель](model.md) · [Архитектура](architecture.md)

Всё оборудование и роли здесь синтетические. Воссоздайте идентичные входные данные командой `python3 tools/generate_examples.py`. Ни одна команда не подключается к Home Assistant.

## Роль светильника покидает перепрофилированную розетку

Выполните команду из README для `examples/role-swap`. Изначально `plug-a/1` владеет `light.workbench`, а `plug-b/1` — `switch.spare`. Манифест назначает роль насоса розетке A, а роль рабочего освещения — розетке B. Автоматизация света использует `follows_role` и разрешает только `workbench`. Её ссылка на сущность остаётся `light.workbench`, хотя целевое оборудование меняется. Отсутствие текстового изменения — ожидаемый результат, а не пропущенная миграция. Поле отчёта `assignments` содержит аппаратные изменения для проверки человеком.

Старый потребитель запасной розетки выводится из использования по `/1` — это весь второй объект автоматизации. Пустая последовательность действий не остаётся. Отчёт рекомендательный; программа не удаляет элементы массива JSON. Применяя вручную несколько предложенных удалений из массива, учитывайте смещение индексов и повторяйте запуск со свежим снимком.

Измените первую политику на `follows_hardware`, оставив разрешённую роль `workbench`: план блокируется с `role_not_allowed`. Расширение списка ролей для включения насоса — явное опасное изменение намерения, а не обычный способ убрать ошибку. Вместо этого восстановите правильную политику.

## Реле меняет домен с light на switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Два предлагаемых изменения меняют цель и её сервис `light.turn_off`. Добавьте данные яркости в исходное действие, обновите одобренный отпечаток источника и запустите снова: `service_data_review` блокирует автоматическое преобразование. Не удаляйте настройки яркости лишь ради прохождения проверки; разберите желаемое поведение.

## Неразрешённый шаблон

Выполните ту же команду для `examples/blocked-template`. Цель — динамический Jinja. Инструмент не вычисляет шаблон и возвращает код 3. Полный поддерживаемый план требует явной конфигурации с доказуемыми буквальными целями; иначе сохраните этот случай как документированную ручную миграцию вне готовой области. Игнорирование кода выхода не разрешает шаблон.

## Дрейф и повторяемость

Изменение источника без обновления хеша манифеста даёт `stale_source`. Изменение снимка даёт `stale_snapshot`. Для этих устаревших моделей предлагаемые изменения ссылок не выводятся. На неизменных файлах результат JSON детерминирован, кроме выбранного языка. Исходные файлы остаются побайтно неизменными.

В реальном проекте скопируйте формат в приватную папку, проверьте физические идентичности, перечислите потребителей и запустите планировщик. Проверьте все назначения и изменения, выполните собственные проверки HA в обычном процессе развёртывания, затем сделайте новый снимок только для чтения для проверки результата. Этот проект не реализует такое развёртывание или исполнитель отката.
