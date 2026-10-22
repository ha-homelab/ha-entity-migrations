# عیب‌یابی

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


<div dir="rtl" lang="fa">

[نصب](installation.md) · [محدودیت‌ها](limitations.md)

**فرمان پیدا نشد:** همان محیط مجازی نصب را فعال کنید. `python3 -m ha_entity_migrations --version` را امتحان کنید؛ برای دور زدن ناهماهنگی مسیر در Python سیستم نصب نکنید.

**خروج 2، schema_invalid:** کلیدها را با مثال اجرایی و [مدل ورودی](model.md) مقایسه کنید. فیلد ناشناخته خطاست. نسخه عدد صحیح 1 است؛ شناسهٔ کانال رشته است. هر سیاست کنش اشاره‌گر سرویس می‌خواهد. عکس وضعیت موجودیت دارد؛ مانیفست تخصیص و مصرف‌کننده دارد. این فایل‌ها قابل‌جایگزینی نیستند.

**خروج 2، duplicate_source:** دو نام منبع یک فایل فیزیکی را مشخص می‌کنند. در `sources` یک نام متعارف نگه دارید و همهٔ فیلدهای `file` مصرف‌کنندگان را به آن تغییر دهید. جداکنندهٔ تکراری یا نام مستعار پیوند سخت/بزرگی حروف را بردارید؛ سیاست دوم به نام مستعار ندهید. فایل‌های جدا با محتوای یکسان همچنان پشتیبانی می‌شوند.

**stale_snapshot / stale_source:** تغییر واقعی را با منبع تأییدشده مقایسه کنید. فقط پس از بررسی از فرمان اثرانگشت استفاده کنید. فاصله‌ها هش را تغییر می‌دهند. فقط برای قبول شدن هش قدیمی به نسخهٔ کهنه اشاره نکنید.

**source_collision / destination_collision:** کانال فیزیکی، نقش یا شناسهٔ موجودیت تکراری است. دو سوی جابه‌جایی نقش را صریح بیان کنید و بررسی کنید نقطهٔ تغییرنکرده شناسهٔ مقصد مطلوب را نگه نداشته باشد.

**role_not_allowed / capability_missing:** مصرف‌کننده به بار نامناسب می‌رسد یا توانایی از دست می‌دهد. تأیید کنید باید نقش را دنبال کند یا سخت‌افزار را. allowed_roles را خودکار گسترش ندهید و توانایی نداشتهٔ سخت‌افزار را ادعا نکنید. چراغی که با رلهٔ روشن/خاموش جایگزین شده کم‌نورکردن ندارد.

**missing_policy / unmodeled_reference:** نقطهٔ ارجاع‌شده را فهرست کنید و فقط پس از تأیید هدف، اعلان صریح مصرف‌کننده بیفزایید. رشتهٔ تاریخچهٔ قدیمی ممکن است خارج محدودهٔ فعال باشد؛ فایل را آگاهانه از محدوده خارج کنید، استثنا را مستند کنید و قرارداد منابع را بازسازی کنید.

**dynamic_reference / embedded_reference / indirect_target:** این نسخه نمی‌تواند نگاشت را ثابت کند. Jinja یا رفتار گروه/ناحیه/برچسب را جداگانه بررسی کنید یا پیکربندی ثابت نرمال‌شدهٔ صریح بدهید. برنامه هرگز الگو اجرا نمی‌کند.

**display_domain_review / service_data_review / mixed_action_targets:** امکانات کارت، پارامتر کنش و دسته‌های مقصد را بررسی کنید. کنش چنددامنه‌ای را در تغییر منبع جداگانه و بررسی‌شده تقسیم کنید؛ فقط دامنهٔ سرویس را عوض نکنید.

**retire_scope_mixed / overlapping_edits:** شیء مصرف‌کنندهٔ منسوخ منسجمی بدون ارجاع نامرتبط انتخاب کنید. فقط entity_id را از کنش حذف نکنید: ممکن است هدف گسترده یا پیکربندی نامعتبر بسازد. برنامه کنارگذاری خودکار انجام نمی‌دهد.

**unsupported_source:** فقط JSON برنامه‌ریزی می‌شود. YAML، فایل دودویی و بقیه بی‌صدا نادیده گرفته نمی‌شوند. کپی JSON صریحاً نرمال‌شده می‌تواند به تحلیل کمک کند، اما پیش از ویرایش واقعی باید با اصل مقایسه شود.

اشکال را با ورودی مصنوعی کمینه، نسخهٔ ابزار/Python، کد خروج و کدهای تشخیصی گزارش کنید. هرگز خروجی خام خانه یا اعتبارنامهٔ API پیوست نکنید.

</div>
