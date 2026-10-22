# القيود وحدود المراجعة

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


<div dir="rtl" lang="ar">

[البنية](architecture.md) · [الأمان](../../SECURITY.md)

لا تتجاوز دقة الخطة دقة تصريحات الأجهزة والقنوات والأدوار والملفات المقدمة. لا تكتشف الأداة لوحات التحكم المتروكة، أو محفزات الأجهزة، أو المشاهد، أو blueprints، أو الأتمتة المحفوظة في مكان آخر، أو مرشحات Matter، أو العملاء الخارجيين، أو حالات التكامل المخفية. لا تعتبر التقرير الجاهز تدقيقاً كاملاً لـ Home Assistant. كل دور فريد في هذا الإصدار؛ وتتطلب الأدوار الدلالية متعددة العلاقات والمجموعات تفكيكاً يدوياً.

تُدعم مصادر الإعداد بصيغة JSON. لا تُفسر YAML أو تضمينات الملفات أو الأسماء البديلة أو المراسي أو الوسوم القابلة للتنفيذ أو المكونات المخصصة أو القوالب المنشأة أثناء التشغيل. التطبيع خارج هذا الإصدار وقد يفقد بعض المعاني؛ احتفظ بالأصل وراجع التكافؤ. حتى JSON المدعوم لا يُفحص مقابل مخطط إعداد HA الكامل. قد يترك حذف كائن مستهلك صريح كائناً أباً غير صالح؛ راجعه وشغّل مدقق إعداد HA ضمن بيئة الاختبار المعتادة قبل النشر.

القدرات والأدوار المسموحة قيود صريحة وليست استنتاجاً للسلامة. لا تستطيع الأداة معرفة أن مضخة أو محرك باب مرآب قد وُصل بمقبس كان غير مؤذٍ. حالة المرحّل المبلّغ عنها لا تثبت سلوك التلامس أو الحمل. لا تشغّل نصوصاً برمجية للمنزل بأكمله ولا تفصل وتوصل كهرباء جهاز عامل لمجرد التحقق من الأسماء. التشغيل المادي الأولي إجراء منفصل وخاضع للتحكم.

لا يطبق هذا الإصدار الخطط، ولا يعيد تسمية كيانات السجل، ولا يغير المعرّفات الفريدة، ولا يعيد تحميل HA أو تشغيل وحدة التحكم، ولا يزيل التكاملات أو يتراجع عن التغييرات. العمليات المعادة استشارية وليست JSON Patch قابلة للتنفيذ. عند تطبيقها يدوياً، احصل على لقطة جديدة وتحقق بعد كل تغيير تمت مراجعته؛ فقد تتغير الفهارس والإصدارات. التجزئات لا توفر توقيعات أو تحكماً في الوصول.

قد تحتوي التقارير على أسماء ومعرّفات خاصة. أبقها خارج Git العام ومتتبعات المشكلات ومخرجات CI. تستخدم الأمثلة المنشورة أجهزة اصطناعية ولا تدعي تحققاً ميدانياً. تمنع التشخيصات الخطة عمداً؛ لا يوجد خيار فرض أو قائمة تجاهل أو وضع تساهل مخفي.

</div>
