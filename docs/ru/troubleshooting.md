# Устранение неисправностей

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

[Установка](installation.md) · [Ограничения](limitations.md)

**Команда не найдена:** активируйте то же виртуальное окружение, в котором выполнялась установка. Попробуйте `python3 -m ha_entity_migrations --version`; не устанавливайте в системный Python лишь для обхода несоответствия путей.

**Выход 2, schema_invalid:** сравните ключи с исполняемым примером и [входной моделью](model.md). Неизвестные поля — ошибки. Версии — целое 1; идентификаторы каналов — строки. Каждая политика действия требует указателя сервиса. Снимок содержит сущности; манифест — назначения и потребителей. Эти файлы невзаимозаменяемы.

**Выход 2, duplicate_source:** два имени источника обозначают один физический файл. Оставьте одно каноническое имя в `sources` и обновите на него поля `file` всех потребителей. Уберите повторные разделители, жёсткие ссылки или варианты регистра; не назначайте псевдониму вторую политику. Отдельные файлы с одинаковым содержимым по-прежнему поддерживаются.

**stale_snapshot / stale_source:** сравните фактические изменения с одобренным источником. Используйте команду отпечатка только после проверки. Пробельные изменения влияют на хеш. Не подставляйте устаревшую копию лишь ради совпадения старого хеша.

**source_collision / destination_collision:** дублируется физический канал, роль или ID сущности. Явно опишите обе стороны обмена ролями и проверьте, что неизменная точка не сохраняет желаемый целевой ID.

**role_not_allowed / capability_missing:** потребитель попадёт на неподходящую нагрузку или утратит возможность. Уточните, должен ли он следовать роли или оборудованию. Не расширяйте автоматически allowed_roles и не объявляйте отсутствующие возможности оборудования. Светильник, заменённый реле включения/выключения, не умеет регулировать яркость.

**missing_policy / unmodeled_reference:** внесите точку, на которую ссылаются, в инвентарь и добавьте явное объявление потребителя только после подтверждения назначения. Старая историческая строка может быть вне активной области; осознанно исключите файл из плана, задокументируйте исключение и заново создайте контракт источников.

**dynamic_reference / embedded_reference / indirect_target:** этот выпуск не может доказать соответствие. Отдельно проверьте Jinja или поведение групп, областей и меток либо предоставьте явную нормализованную конфигурацию с буквальными значениями. Программа никогда не выполняет шаблон.

**display_domain_review / service_data_review / mixed_action_targets:** проверьте возможности карточек, параметры действий и группы целей. Разделите многодоменное действие в отдельном проверенном изменении источника; не меняйте просто домен сервиса.

**retire_scope_mixed / overlapping_edits:** выберите цельный устаревший объект-потребитель без посторонних ссылок. Не удаляйте из действия только entity_id: это может сделать цель слишком широкой или оставить некорректную конфигурацию. Программа ничего автоматически не выводит из использования.

**unsupported_source:** планировать можно только JSON. YAML, двоичные и другие файлы не пропускаются молча. Явно нормализованная JSON-копия может помочь анализу, но её нужно сравнить с оригиналом до реального изменения.

Сообщайте об ошибке с минимальным синтетическим входом, версией инструмента и Python, кодом выхода и диагностическими кодами. Никогда не прикладывайте необработанный экспорт домашней системы или учётные данные API.
