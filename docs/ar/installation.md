# التثبيت وواجهة الأوامر

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


<div dir="rtl" lang="ar">

[فهرس التوثيق](../../README.md#documentation)

استخدم Python 3.11 أو أحدث. أنشئ بيئة افتراضية مخصصة وفعّلها، ثم شغّل `python3 -m pip install -e .` من نسخة المستودع. لا تعتمد الحزمة على مكتبات وقت تشغيل؛ وقد يجلب pip خلفية البناء. لجهاز غير متصل، حضّر wheel واعتماديات البناء مسبقاً. تحقق من التثبيت المختار باستخدام `ha-entity-migrations --version`؛ يعرض الأمر إصدار الحزمة المثبتة.

تضم الواجهة أمرين، ويوضع خيار اللغة العام قبل الأمر:

</div>

<div dir="ltr">

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

</div>

<div dir="rtl" lang="ar">

يطبع `fingerprint` تجزئة SHA-256 بأحرف صغيرة للبايتات الدقيقة للملف. لا يتحقق من صحة الملف بوصفه JSON. يجب أن تطابق بصمات اللقطة والمصادر في البيان الملفات نفسها تماماً، بما فيها المسافات. لا تحدّث بصمة لمجرد تجاهل انحراف غير متوقع؛ قارن الإدخال الجديد واعتمده أولاً.

يقرأ `plan` بيان JSON ولقطة JSON مطبّعة والملفات المذكورة صراحة في `manifest.sources` فقط، نسبةً إلى `--root`. لا يبحث في المجلدات تكرارياً ولا في مجلدك الشخصي. الخرج الافتراضي JSON. تتغير الرسائل البشرية وحدها مع `--lang en|ru|de|es`، وتبقى أسماء الحقول ورموز التشخيص مستقرة. يتوفر `--help` على المستوى الأعلى ولكل أمر. لا يوجد أمر للتطبيق أو الرفع أو الاكتشاف أو المصادقة.

حالة الخروج:

- **0:** نطاق الإدخال المدعوم متسق داخلياً وجاهز للمراجعة.
- **2:** وسائط أو مدخلات غير صالحة، أو ملف غير قابل للقراءة، أو مخالفة مخطط أو حد.
- **3:** أنتج إدخال صحيح بنيوياً خطة ممنوعة بسبب تعارض أو نطاق غير محلول.

تنتج أخطاء الإدخال بعد تحليل الوسائط غلاف JSON على stdout بقيمة `status: invalid`. تطبع أخطاء الوسائط إرشادات استخدام مترجمة على stderr. يطبع حساب البصمة الناجح التجزئة فقط. في الوضع النصي تحتفظ سجلات التعديلات المقترحة بأسماء حقولها الآلية، وتُترجم الشروح.

احتفظ بملفات التشغيل في مجلد خاص. يؤدي توجيه stdout إلى إنشاء تقريرك الخاص، وقد يتضمن أسماء كيانات ومسارات تكشف الهوية. الأداة نفسها لا تكتب شيئاً. أزل التثبيت باستخدام `python3 -m pip uninstall ha-entity-migrations`. لفحوص المطورين، راجع [CONTRIBUTING](../../CONTRIBUTING.md).

</div>
