# أمثلة مشروحة

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


<div dir="rtl" lang="ar">

[نموذج الإدخال](model.md) · [البنية](architecture.md)

كل الأجهزة والأدوار هنا اصطناعية. أعد إنشاء مدخلات مطابقة باستخدام `python3 tools/generate_examples.py`. لا يتصل أي أمر بـ Home Assistant.

## دور المصباح يغادر مقبساً أعيد تخصيصه

شغّل أمر README الخاص بـ `examples/role-swap`. في البداية يملك `plug-a/1` الكيان `light.workbench`، ويملك `plug-b/1` الكيان `switch.spare`. يسند البيان دور المضخة إلى المقبس A ودور طاولة العمل إلى المقبس B. تستخدم أتمتة الإضاءة `follows_role` وتسمح فقط بالدور `workbench`. يبقى مرجعها `light.workbench` بينما يتغير الجهاز المستهدف. عدم وجود تعديل نصي هو النتيجة المقصودة، وليس ترحيلاً مفقوداً. يحتوي `assignments` في التقرير على تغييرات الأجهزة لمراجعة بشرية.

يُوقف المستهلك الاحتياطي القديم عند `/1`، أي كائن الأتمتة الثاني بأكمله. لا يترك ذلك تسلسلاً فارغاً من الإجراءات. التقرير استشاري؛ ولا يحذف البرنامج أي عنصر من مصفوفة JSON. إذا طبقت عدة عمليات حذف مقترحة يدوياً، فانتبه إلى تحرك الفهارس وأعد التشغيل من لقطة جديدة.

غيّر السياسة الأولى إلى `follows_hardware` مع إبقاء الدور المسموح `workbench`: تُمنع الخطة بالخطأ `role_not_allowed`. توسيع قائمة الأدوار لتشمل مضخة هو تغيير صريح وخطير في القصد، وليس طريقة عادية لإزالة الخطأ. أعد السياسة الصحيحة بدلاً من ذلك.

## مرحّل ينتقل من light إلى switch

</div>

<div dir="ltr">

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

</div>

<div dir="rtl" lang="ar">

يغير التعديلان المقترحان الهدف وخدمته `light.turn_off`. أضف بيانات السطوع إلى إجراء المصدر، وحدّث بصمة المصدر المعتمدة، ثم أعد التشغيل: يمنع `service_data_review` التحويل التلقائي. لا تتخلص من إعدادات السطوع لمجرد إرضاء الأداة؛ راجع السلوك المطلوب.

## قالب غير محلول

شغّل الأمر نفسه مع `examples/blocked-template`. الهدف عبارة عن Jinja ديناميكي. لا تقيّمه الأداة وتعيد الرمز 3. تتطلب الخطة الكاملة المدعومة إعداداً صريحاً بأهداف حرفية قابلة للإثبات؛ وإلا فأبقِ هذه الجزئية كترحيل يدوي موثق خارج النطاق الجاهز. تجاهل رمز الخروج لا يحل القالب.

## الانحراف وقابلية التكرار

يؤدي تعديل مصدر دون تغيير تجزئته في البيان إلى `stale_source`. ويؤدي تعديل اللقطة إلى `stale_snapshot`. لا تصدر تعديلات مراجع مرشحة لهذه النماذج القديمة. مع بقاء الملفات دون تغيير تكون نتيجة JSON حتمية باستثناء اللغة المختارة. تظل ملفات المصدر مطابقة بايتاً ببايت.

لمشروع حقيقي، انسخ الصيغة إلى مجلد خاص، وتحقق من الهويات المادية، واحصر المستهلكين ثم شغّل المخطط. راجع كل الإسنادات والتعديلات، ونفّذ فحوص HA ضمن عملية النشر المعتمدة لديك، ثم أنشئ لقطة جديدة للقراءة فقط للتحقق من النتيجة. لا ينفذ هذا المشروع عملية النشر تلك ولا أداة للتراجع.

</div>
