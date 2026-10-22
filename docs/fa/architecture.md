# معماری و قرارداد گزارش

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


<div dir="rtl" lang="fa">

[مدل](model.md) · [محدودیت‌ها](limitations.md)

![جریان دادهٔ فقط‌خواندنی](../diagrams/pipeline.svg)

`io.py` محدودیت فایل، مسیر و JSON و اشاره‌گرهای دقیق را اعمال می‌کند. `planner.py` اعلان‌ها را اعتبارسنجی می‌کند، نگاشت‌های قبل/بعد را می‌سازد، مقادیر منبع را می‌کاود، سیاست‌های صریح را حل می‌کند و رکوردهای تشخیصی را گرد می‌آورد. `cli.py` پیام‌های ترجمه‌شده را می‌افزاید و گزارش را چاپ می‌کند. `i18n.py` چهار کاتالوگ کامل پیام دارد. این مسیر به شبکه یا Home Assistant وابسته نیست.

پویشگر عمداً محافظه‌کار است. رشته‌هایی که دقیقاً شکل ارجاع موجودیت دارند با عکس وضعیت مقایسه می‌شوند. رشته‌های دارای ارجاع جاسازی‌شده حل‌نشده می‌مانند. الگوها در کلیدها یا مقادیر و کلیدهای مقصد دستگاه/ناحیه/برچسب حتی وقتی تفسیرشان آسان به نظر برسد حل‌نشده می‌مانند. فیلدهای عادی سرویس شناسهٔ موجودیت محسوب نمی‌شوند؛ سرویس‌های پویا همچنان حل‌نشده‌اند. فایل‌های غیر JSON به‌عنوان منابع پشتیبانی‌نشده ثبت و مانع برنامه‌ریزی می‌شوند. این یک تجزیه‌گر عمومی HA نیست.

![جریان تصمیم سیاست‌ها](../diagrams/policy.svg)

## پوشش پایدار JSON، نسخهٔ طرح‌وارهٔ 1

`schema_version`، `tool_version`، `status`، `read_only`، `scope`، `snapshot_sha256`، `source_sha256`، `assignments`، `edits`، `diagnostics`، `language`، `summary`. برای ورودی معتبر، `status` برابر ready یا blocked است. `scope` همیشه `supplied_files_only` و `read_only` همیشه true است. خطاهای ورودی از پوشش کوچک‌تر invalid که در نصب توضیح داده شده استفاده می‌کنند.

ویرایش‌ها عملیات، فایل و اشاره‌گر دارند. `replace_reference` همچنین before/after/policy را دارد؛ `replace_service` شامل before/after است؛ `remove_consumer` ارجاع کنارگذاشته‌شده را دارد. این‌ها **JSON Patch قابل‌اجرا نیستند**. معنای تراکنش، جابه‌جایی اندیس‌ها و چرخهٔ عمر HA در آن‌ها وجود ندارد. آن‌ها را پیشنهاد تلقی و بررسی کنید؛ این نسخه عمداً ابزار اعمال وصله ندارد.

تشخیص‌ها دارای `code`، `location` و `severity` پایدار و `message` ترجمه‌شده‌اند. هم `error` و هم `unresolved` طرح را مسدود می‌کنند. گزارش‌های `blocked` ممکن است ویرایش‌های پیشنهادی برای ارجاع‌های بی‌تأثیر داشته باشند، اما هیچ‌یک تراکنشی آماده نیست. مدل‌های اولیهٔ کهنه یا متناقض همهٔ ویرایش‌های پیشنهادی ارجاع را متوقف می‌کنند. تخصیص‌ها همیشه مدل درخواستی کاربر را بازتاب می‌دهند، نه تغییرات انجام‌شده را.

گزارش‌ها منابع، تخصیص‌ها، ویرایش‌ها و تشخیص‌ها را برای بازتولیدپذیری مرتب می‌کنند. زمان فعلی یا امتیاز اطمینان ساختگی وجود ندارد. هش بایت‌ها ثابت می‌کند کدام نسخهٔ ورودی تحلیل شده، نه اینکه ورودی حقیقت دارد یا دستگاه فرمان را اجرا خواهد کرد.

</div>
