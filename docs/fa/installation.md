# نصب و CLI

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


<div dir="rtl" lang="fa">

[فهرست مستندات](../../README.md#documentation)

از Python 3.11 یا جدیدتر استفاده کنید. محیط مجازی اختصاصی بسازید و فعال کنید، سپس در نسخهٔ کاری `python3 -m pip install -e .` را اجرا کنید. بسته وابستگی زمان اجرا ندارد؛ pip ممکن است پس‌زمینهٔ ساخت را دریافت کند. برای دستگاه آفلاین، wheel و وابستگی‌های ساخت را از پیش آماده کنید. نصب انتخابی را با `ha-entity-migrations --version` بررسی کنید؛ این فرمان نسخهٔ بستهٔ نصب‌شده را نشان می‌دهد.

CLI دو فرمان دارد و گزینهٔ سراسری زبان پیش از فرمان می‌آید:

</div>

<div dir="ltr">

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

</div>

<div dir="rtl" lang="fa">

`fingerprint` مقدار SHA-256 بایت‌های دقیق فایل را با حروف کوچک چاپ می‌کند. صحت JSON فایل را بررسی نمی‌کند. اثرانگشت عکس وضعیت و منابع در مانیفست باید دقیقاً با فایل‌ها، شامل فاصله‌ها، تطبیق داشته باشد. اثرانگشت را صرفاً برای رد کردن انحراف غیرمنتظره تازه نکنید؛ اول ورودی جدید را مقایسه و تأیید کنید.

`plan` مانیفست JSON، عکس وضعیت JSON نرمال‌شده و فقط فایل‌های نام‌برده‌شدهٔ صریح در `manifest.sources` را نسبت به `--root` می‌خواند. پوشه را بازگشتی نمی‌کاود و در پوشهٔ خانگی جست‌وجو نمی‌کند. خروجی پیش‌فرض JSON است. فقط پیام‌های انسانی با `--lang en|ru|de|es` عوض می‌شوند؛ نام فیلدها و کدهای تشخیصی پایدارند. `--help` در سطح بالا و برای هر فرمان موجود است. فرمان اعمال، بارگذاری، کشف یا احراز هویت وجود ندارد.

وضعیت خروج:

- **0:** محدودهٔ ورودی پشتیبانی‌شده درونی سازگار و آمادهٔ بررسی است.
- **2:** آرگومان/ورودی نامعتبر، فایل ناخوانا یا نقض طرح‌واره/محدودیت.
- **3:** ورودی از نظر ساختار معتبر، طرحی مسدود به دلیل تعارض یا محدودهٔ حل‌نشده ساخته است.

خطاهای ورودی پس از تجزیهٔ آرگومان‌ها پوشش JSON با `status: invalid` روی stdout تولید می‌کنند. خطاهای آرگومان راهنمای محلی‌سازی‌شده را روی stderr چاپ می‌کنند. محاسبهٔ موفق اثرانگشت فقط چکیده را چاپ می‌کند. در حالت متنی، رکوردهای ویرایش پیشنهادی نام‌های ماشینی فیلدها را نگه می‌دارند و توضیحات ترجمه می‌شوند.

فایل‌های عملیاتی را در پوشهٔ خصوصی نگه دارید. هدایت stdout گزارش خودتان را می‌سازد؛ ممکن است نام‌های شناسایی‌کنندهٔ موجودیت و مسیر فایل داشته باشد. خود ابزار چیزی نمی‌نویسد. با `python3 -m pip uninstall ha-entity-migrations` حذف کنید. کنترل‌های توسعه‌دهنده در [CONTRIBUTING](../../CONTRIBUTING.md) آمده‌اند.

</div>
