# Встановлення та CLI

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

[Покажчик документації](../../README.md#documentation)

Використовуйте Python 3.11 або новіший. Створіть і активуйте окреме віртуальне середовище, а в робочій копії виконайте `python3 -m pip install -e .`. Пакет не має залежностей часу виконання; pip може завантажити свій бекенд збирання. Для автономної машини заздалегідь підготуйте wheel і залежності збирання. Перевірте обране встановлення командою `ha-entity-migrations --version`; вона показує версію встановленого пакета.

CLI має дві команди, глобальну мовну опцію слід указувати перед командою:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` виводить SHA-256 точних байтів файлу малими літерами. Він не перевіряє файл як JSON. Відбитки знімка та джерел у маніфесті мають точно відповідати цим файлам, включно з пробільними символами. Не оновлюйте відбиток лише для приховування неочікуваних відхилень; спочатку порівняйте та схваліть новий вхід.

`plan` читає JSON-маніфест, нормалізований JSON-знімок і лише файли, явно названі в `manifest.sources`, відносно `--root`. Він не обходить каталог рекурсивно й не шукає у вашій домашній теці. Типовий вихід — JSON. Для `--lang en|ru|de|es` змінюються лише повідомлення для людей; назви полів і діагностичні коди стабільні. `--help` доступна на верхньому рівні й для кожної команди. Немає команд застосування, завантаження, виявлення чи автентифікації.

Статус завершення:

- **0:** підтримуваний обсяг входу внутрішньо узгоджений і готовий до перевірки.
- **2:** некоректні аргументи/вхід, нечитабельний файл або порушення схеми/лімітів.
- **3:** структурно коректний вхід створив заблокований план через конфлікт чи нерозв'язаний обсяг.

Помилки входу після розбору аргументів створюють оболонку JSON у stdout зі `status: invalid`. Помилки аргументів виводять локалізовану довідку в stderr. Успішне обчислення відбитка виводить лише хеш. У текстовому режимі записи запропонованих змін зберігають машинні назви полів; пояснення перекладені.

Зберігайте робочі файли в приватному каталозі. Перенаправлення stdout створює ваш власний звіт, що може містити ідентифікаційні назви сутностей і шляхи. Сам засіб нічого не записує. Видалення: `python3 -m pip uninstall ha-entity-migrations`. Перевірки для розробників наведено в [CONTRIBUTING](../../CONTRIBUTING.md).
