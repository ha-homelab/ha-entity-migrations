# محدودیت‌ها و مرز بررسی

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/limitations.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/limitations.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/limitations.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/limitations.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/limitations.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/limitations.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/limitations.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/limitations.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/limitations.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/limitations.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/limitations.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/limitations.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/limitations.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/limitations.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/limitations.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/limitations.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/limitations.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/limitations.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/limitations.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/limitations.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/limitations.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/limitations.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/limitations.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/limitations.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->


<div dir="rtl" lang="fa">

[معماری](architecture.md) · [امنیت](../../SECURITY.md)

دقت طرح به اعلان‌های سخت‌افزار/کانال/نقش و فایل‌های ارائه‌شده محدود است. ابزار داشبوردهای حذف‌شده، محرک‌های دستگاه، صحنه‌ها، blueprintها، اتوماسیون‌های ذخیره‌شده در جای دیگر، فیلترهای Matter، مشتریان بیرونی یا وضعیت پنهان یکپارچه‌سازی را کشف نمی‌کند. گزارش آماده را ممیزی کامل Home Assistant ننامید. نقش در این نسخه یکتا است؛ نقش‌های معنایی چندبه‌چند و گروه‌ها به تجزیهٔ دستی نیاز دارند.

منابع پیکربندی JSON پشتیبانی می‌شوند. خود YAML، فایل‌های include، نام‌های مستعار، لنگرها، برچسب‌های اجرایی، مؤلفه‌های سفارشی و الگوهای ساخته‌شده در زمان اجرا تفسیر نمی‌شوند. نرمال‌سازی خارج از این نسخه است و ممکن است معنا را از دست بدهد؛ اصل را نگه دارید و هم‌ارزی را بررسی کنید. حتی JSON پشتیبانی‌شده با طرح‌وارهٔ کامل پیکربندی HA سنجیده نمی‌شود. حذف شیء مصرف‌کنندهٔ صریح ممکن است والد نامعتبر باقی بگذارد؛ والد را بررسی کنید و کنترل پیکربندی HA را در روند معمول آزمایش پیش از استقرار اجرا کنید.

توانایی‌ها و نقش‌های مجاز قیدهای صریح‌اند، نه ایمنی استنباط‌شده. ابزار نمی‌داند پمپ یا موتور در گاراژ به پریزی که قبلاً بی‌خطر بوده وصل شده است. وضعیت گزارش‌شدهٔ رله، رفتار کنتاکت/بار را ثابت نمی‌کند. صرفاً برای تأیید نام‌ها اسکریپت کل خانه اجرا نکنید یا برق دستگاه فعال را قطع و وصل نکنید. راه‌اندازی فیزیکی به رویهٔ کنترل‌شدهٔ جداگانه تعلق دارد.

این نسخه طرح را اعمال نمی‌کند، موجودیت رجیستری را تغییرنام نمی‌دهد، شناسهٔ یکتا را عوض نمی‌کند، HA را دوباره بار نمی‌کند، کنترل‌گر را راه‌اندازی مجدد نمی‌کند، یکپارچه‌سازی را کنار نمی‌گذارد و تغییر را برنمی‌گرداند. عملیات خروجی مشورتی‌اند، نه JSON Patch اجرایی. در صورت اعمال دستی، عکس وضعیت تازه بگیرید و پس از هر تغییر بررسی‌شده تأیید کنید؛ اندیس‌ها و نسخه‌ها ممکن است عوض شده باشند. هش امضا یا کنترل دسترسی فراهم نمی‌کند.

گزارش‌ها می‌توانند نام و شناسهٔ خصوصی داشته باشند. آن‌ها را در Git عمومی، سامانهٔ پیگیری مشکل یا خروجی CI قرار ندهید. مثال‌های عمومی دستگاه مصنوعی دارند و ادعای تأیید میدانی ندارند. تشخیص‌ها عمداً طرح را مسدود می‌کنند؛ پرچم اجبار، فهرست نادیده‌گیری یا حالت سهل‌گیر پنهان وجود ندارد.

</div>
