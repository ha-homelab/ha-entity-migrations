# استكشاف الأخطاء وإصلاحها

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


<div dir="rtl" lang="ar">

[التثبيت](installation.md) · [القيود](limitations.md)

**الأمر غير موجود:** فعّل البيئة الافتراضية نفسها التي استخدمتها للتثبيت. جرّب `python3 -m ha_entity_migrations --version`؛ لا تثبّت في Python النظام لمجرد تجاوز عدم تطابق المسار.

**الخروج 2، schema_invalid:** قارن مفاتيحك بالمثال القابل للتشغيل و[نموذج الإدخال](model.md). الحقول غير المعروفة أخطاء. الإصدارات هي العدد الصحيح 1، ومعرّفات القنوات سلاسل. تحتاج كل سياسة إجراء إلى مؤشر خدمتها. تحتوي اللقطة على كيانات، والبيان على إسنادات ومستهلكين. الملفان غير قابلين للتبادل.

**الخروج 2، duplicate_source:** اسما مصدر يحددان ملفاً مادياً واحداً. أبقِ اسماً قانونياً واحداً في `sources` وحدّث كل حقول `file` لدى المستهلكين. أزل الفواصل المكررة أو أسماء الروابط الصلبة أو بدائل حالة الأحرف؛ ولا تعطِ الاسم البديل سياسة ثانية. تظل الملفات المنفصلة ذات المحتوى المتطابق مدعومة.

**stale_snapshot / stale_source:** قارن التغييرات الفعلية بالمصدر المعتمد. لا تستخدم أمر البصمة إلا بعد مراجعتها. تغير المسافات يؤثر في التجزئة. لا تشير إلى نسخة قديمة لمجرد إنجاح التجزئة القديمة.

**source_collision / destination_collision:** توجد قناة مادية أو دور أو معرّف كيان مكرر. صف طرفي تبادل الأدوار صراحة وتحقق من أن نقطة غير متغيرة لا تحتفظ بمعرّف الوجهة المطلوب.

**role_not_allowed / capability_missing:** سيصل المستهلك إلى حمل غير مناسب أو يفقد قدرة. أكد ما إذا كان يجب أن يتبع الدور أم الجهاز. لا توسّع allowed_roles تلقائياً ولا تصرّح بقدرات لا يملكها الجهاز. المصباح المستبدل بمرحّل تشغيل/إيقاف لا يمكنه تعتيم الإضاءة.

**missing_policy / unmodeled_reference:** احصر نقطة النهاية المشار إليها وأضف تصريح مستهلك صريحاً فقط بعد تأكيد الغرض. قد تكون سلسلة تاريخية قديمة خارج النطاق النشط؛ استبعد الملف عمداً من النطاق، ووثّق الاستبعاد، وأعد توليد عقد المصادر.

**dynamic_reference / embedded_reference / indirect_target:** لا يستطيع هذا الإصدار إثبات الربط. راجع Jinja أو سلوك المجموعة/المنطقة/التسمية منفصلاً، أو قدم إعداداً حرفياً مطبّعاً وصريحاً. لا ينفذ البرنامج أي قالب أبداً.

**display_domain_review / service_data_review / mixed_action_targets:** افحص خصائص البطاقات ومعاملات الإجراءات ومجموعات الأهداف. قسّم الإجراء متعدد النطاقات ضمن تغيير مصدر تتم مراجعته منفصلاً؛ لا تغير نطاق خدمته فقط.

**retire_scope_mixed / overlapping_edits:** اختر كائن مستهلك قديماً متماسكاً دون مراجع غير مرتبطة. لا تحذف entity_id وحده من إجراء؛ فقد يوسع ذلك الهدف أو يترك إعداداً غير صالح. لا ينفذ البرنامج إيقافاً تلقائياً.

**unsupported_source:** يمكن التخطيط لـ JSON فقط. لا يجري تخطي YAML أو الملفات الثنائية وغيرها بصمت. قد تساعد نسخة JSON مطبّعة صراحة في التحليل، لكن يجب مقارنتها بالأصل قبل أي تعديل فعلي.

أبلغ عن الخطأ بمدخل اصطناعي مصغر، وإصدار الأداة وPython، ورمز الخروج، ورموز التشخيص. لا ترفق أبداً تصديراً منزلياً خاماً أو بيانات اعتماد API.

</div>
