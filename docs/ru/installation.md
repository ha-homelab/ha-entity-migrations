# Установка и CLI

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/installation.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/installation.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/installation.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/installation.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/installation.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/installation.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/installation.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/installation.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/installation.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/installation.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/installation.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/installation.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/installation.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/installation.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/installation.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/installation.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/installation.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/installation.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/installation.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/installation.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/installation.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/installation.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/installation.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/installation.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Указатель документации](../../README.md#documentation)

Используйте Python 3.11 или новее. Создайте отдельное виртуальное окружение, активируйте его, затем выполните `python3 -m pip install -e .` из рабочей копии. У пакета нет зависимостей времени исполнения; pip может загрузить средство сборки. Для автономной машины заранее подготовьте wheel и сборочные зависимости. Проверьте выбранную установку командой `ha-entity-migrations --version`: она сообщает версию установленного пакета.

CLI имеет две команды; глобальный параметр языка указывается перед командой:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` выводит SHA-256 точных байтов файла в нижнем регистре. Файл не проверяется как JSON. Отпечатки снимка и источников в манифесте должны соответствовать именно этим файлам, включая пробельные символы. Не обновляйте отпечаток просто для подавления неожиданного дрейфа; сначала сравните и одобрите новый вход.

`plan` читает JSON-манифест, нормализованный JSON-снимок и только файлы, явно перечисленные в `manifest.sources` относительно `--root`. Он не обходит каталог рекурсивно и не ищет в домашней папке. Формат вывода по умолчанию — JSON. Для `--lang en|ru|de|es` меняются только сообщения для человека; имена полей и диагностические коды стабильны. `--help` доступен на верхнем уровне и у каждой команды. Команд применения, загрузки, обнаружения или аутентификации нет.

Коды выхода:

- **0:** поддерживаемая область входа внутренне согласована и готова к проверке.
- **2:** неверные аргументы или вход, нечитаемый файл либо нарушение схемы или лимита.
- **3:** структурно правильный вход дал заблокированный план — конфликт или неразрешённую область.

Ошибки входа после разбора аргументов выводят в stdout оболочку JSON с `status: invalid`. Ошибки аргументов выводят локализованную справку использования в stderr. Успешное вычисление отпечатка печатает только хеш. В текстовом режиме записи предложенных изменений сохраняют машинные имена полей; пояснения переводятся.

Храните рабочие данные в приватном каталоге. Перенаправление stdout создаёт ваш собственный отчёт; он может содержать идентифицирующие имена сущностей и пути файлов. Сам инструмент ничего не записывает. Удаление: `python3 -m pip uninstall ha-entity-migrations`. Проверки разработчика описаны в [CONTRIBUTING](../../CONTRIBUTING.md).
