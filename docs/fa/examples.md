# مثال‌های تشریح‌شده

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


<div dir="rtl" lang="fa">

[مدل ورودی](model.md) · [معماری](architecture.md)

همهٔ سخت‌افزارها و نقش‌های اینجا مصنوعی‌اند. ورودی‌های یکسان را با `python3 tools/generate_examples.py` بازسازی کنید. هیچ فرمانی به Home Assistant وصل نمی‌شود.

## نقش چراغ از پریزی با کاربرد تازه جدا می‌شود

فرمان README را برای `examples/role-swap` اجرا کنید. ابتدا `plug-a/1` دارای `light.workbench` و `plug-b/1` دارای `switch.spare` است. مانیفست نقش پمپ را به پریز A و نقش میز کار را به B می‌دهد. اتوماسیون روشنایی از `follows_role` استفاده می‌کند و فقط `workbench` را مجاز می‌داند. ارجاع آن `light.workbench` می‌ماند، درحالی‌که سخت‌افزار مقصد عوض می‌شود. نبود ویرایش متن نتیجهٔ موردنظر است، نه مهاجرت فراموش‌شده. `assignments` گزارش تغییرات سخت‌افزار را برای بررسی انسانی دارد.

مصرف‌کنندهٔ یدکی قدیمی در `/1`، یعنی کل شیء اتوماسیون دوم، کنار گذاشته می‌شود. این کار دنبالهٔ کنش خالی باقی نمی‌گذارد. گزارش فقط مشورتی است؛ برنامه هیچ عضو آرایهٔ JSON را حذف نمی‌کند. اگر چند حذف پیشنهادی آرایه را دستی اعمال می‌کنید، جابه‌جایی اندیس‌ها را در نظر بگیرید و از عکس وضعیت تازه دوباره اجرا کنید.

سیاست اول را به `follows_hardware` تغییر دهید و نقش مجاز را `workbench` نگه دارید: طرح با `role_not_allowed` مسدود می‌شود. گسترش فهرست برای شامل شدن پمپ، تغییر صریح و خطرناک قصد است؛ راه عادی برطرف کردن خطا نیست. سیاست درست را برگردانید.

## رله از light به switch تغییر می‌کند

</div>

<div dir="ltr">

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

</div>

<div dir="rtl" lang="fa">

دو ویرایش پیشنهادی مقصد و سرویس `light.turn_off` آن را تغییر می‌دهند. دادهٔ روشنایی را به کنش منبع اضافه کنید، اثرانگشت تأییدشدهٔ منبع را به‌روز کنید و دوباره اجرا کنید: `service_data_review` تبدیل خودکار را مسدود می‌کند. تنظیمات روشنایی را صرفاً برای قبول شدن بررسی حذف نکنید؛ رفتار مطلوب را ارزیابی کنید.

## الگوی حل‌نشده

همان فرمان را با `examples/blocked-template` اجرا کنید. مقصد Jinja پویا است. ابزار آن را ارزیابی نمی‌کند و کد 3 می‌دهد. طرح کامل پشتیبانی‌شده به پیکربندی صریح با مقصدهای ثابت قابل‌اثبات نیاز دارد؛ وگرنه این بخش را مهاجرت دستی مستند، بیرون از محدودهٔ آماده، نگه دارید. نادیده گرفتن کد خروج الگو را حل نمی‌کند.

## انحراف و تکرارپذیری

ویرایش منبع بدون تغییر هش مانیفست باعث `stale_source` می‌شود. ویرایش عکس وضعیت باعث `stale_snapshot` می‌شود. برای این مدل‌های کهنه، ویرایش پیشنهادی ارجاع تولید نمی‌شود. با فایل‌های بدون تغییر، نتیجهٔ JSON به‌جز زبان انتخابی قطعی است. فایل‌های منبع بایت‌به‌بایت بدون تغییر می‌مانند.

برای پروژهٔ واقعی، قالب را در پوشهٔ خصوصی کپی کنید، هویت‌های فیزیکی را بررسی کنید، مصرف‌کنندگان را فهرست کنید و برنامه‌ریز را اجرا کنید. همهٔ تخصیص‌ها و ویرایش‌ها را بررسی کنید، کنترل‌های خود HA را در روند استقرار برقرار انجام دهید، سپس برای تأیید نتیجه عکس وضعیت فقط‌خواندنی تازه بسازید. این پروژه آن استقرار یا اجراکنندهٔ بازگردانی را پیاده نمی‌کند.

</div>
