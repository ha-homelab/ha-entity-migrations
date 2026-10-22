# البنية وعقد التقرير

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


<div dir="rtl" lang="ar">

[النموذج](model.md) · [القيود](limitations.md)

![تدفق البيانات للقراءة فقط](../diagrams/pipeline.svg)

يفرض `io.py` حدود الملفات والمسارات وJSON والمؤشرات الدقيقة. يتحقق `planner.py` من التصريحات، ويبني خرائط ما قبل التغيير وما بعده، ويفحص قيم المصادر، ويحل السياسات الصريحة ويجمع السجلات التشخيصية. يضيف `cli.py` الرسائل المترجمة ويطبع التقرير. يحتوي `i18n.py` على أربعة فهارس رسائل كاملة. لا يعتمد هذا المسار على الشبكة أو Home Assistant.

الماسح متحفظ عمداً. يقارن السلاسل المطابقة تماماً لشكل مراجع الكيانات باللقطة. تبقى السلاسل ذات المراجع المضمنة دون حل. كذلك تبقى القوالب في المفاتيح أو القيم ومفاتيح أهداف الأجهزة والمناطق والتسميات دون حل، حتى إن بدا تخمين معناها سهلاً. لا تُعامل حقول الخدمات العادية كمعرّفات كيانات، بينما تظل الخدمات الديناميكية دون حل. تُسجل الملفات غير المكتوبة بصيغة JSON كمصادر غير مدعومة وتمنع التخطيط. هذه ليست أداة عامة لتحليل HA.

![تدفق قرارات السياسات](../diagrams/policy.svg)

## غلاف JSON مستقر، إصدار المخطط 1

`schema_version`، `tool_version`، `status`، `read_only`، `scope`، `snapshot_sha256`، `source_sha256`، `assignments`، `edits`، `diagnostics`، `language`، `summary`. تكون قيمة `status` إما ready أو blocked للمدخلات الصحيحة. تكون `scope` دائماً `supplied_files_only`، وتكون `read_only` دائماً true. تستخدم أخطاء الإدخال غلاف invalid الأصغر الموضح في دليل التثبيت.

تتضمن التعديلات عملية وملفاً ومؤشراً. يتضمن `replace_reference` أيضاً before/after/policy، ويتضمن `replace_service` الحقلين before/after، ويتضمن `remove_consumer` المرجع المطلوب إيقافه. هذه **ليست تعليمات JSON Patch قابلة للتنفيذ**. فهي تفتقر إلى دلالات المعاملات وتحرك الفهارس ودورة حياة HA. راجعها كمقترحات؛ فهذا الإصدار لا يوفر عمداً أداة لتطبيق الرقع.

تتضمن التشخيصات الحقول المستقرة `code` و`location` و`severity` وحقل `message` المترجم. تمنع كل من `error` و`unresolved` الخطة. قد تحتوي تقارير `blocked` على تعديلات مرشحة للمراجع غير المتأثرة، لكن أياً منها لا يشكل معاملة جاهزة. تمنع النماذج الأولية القديمة أو المتعارضة جميع تعديلات المراجع المرشحة. تعكس الإسنادات دائماً النموذج الذي طلبه المستخدم، ولا تمثل تغييرات مكتملة.

ترتب التقارير المصادر والإسنادات والتعديلات والتشخيصات لضمان قابلية إعادة الإنتاج. لا توجد طوابع زمنية حالية أو درجات ثقة مختلقة. تثبت تجزئات البايتات إصدار الإدخال الذي جرى تحليله، لا صحة محتواه ولا أن الجهاز سينفذ الأمر.

</div>
