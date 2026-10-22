# פתרון בעיות

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


<div dir="rtl" lang="he">

[התקנה](installation.md) · [מגבלות](limitations.md)

**הפקודה לא נמצאה:** הפעילו את הסביבה הווירטואלית ששימשה להתקנה. נסו `python3 -m ha_entity_migrations --version`; אל תתקינו ב־Python של המערכת רק כדי לעקוף אי־התאמה בנתיב.

**יציאה 2, schema_invalid:** השוו את המפתחות לדוגמה הניתנת להרצה ול[מודל הקלט](model.md). שדות לא מוכרים הם שגיאות. גרסאות הן המספר השלם 1; מזהי ערוצים הם מחרוזות. כל מדיניות פעולה דורשת מצביע שירות. בתמונת מצב יש ישויות; במניפסט הקצאות וצרכנים. הקבצים אינם חלופיים זה לזה.

**יציאה 2, duplicate_source:** שני שמות מקור מזהים קובץ פיזי אחד. השאירו שם קנוני אחד ב־`sources` ועדכנו את כל שדות `file` של הצרכנים. הסירו מפרידים כפולים או כינויי קישור קשיח/רישיות; אל תתנו לכינוי מדיניות שנייה. קבצים נפרדים עם תוכן זהה עדיין נתמכים.

**stale_snapshot / stale_source:** השוו שינויים בפועל למקור המאושר. השתמשו בפקודת טביעת האצבע רק לאחר בדיקה. רווחים משפיעים על הגיבוב. אל תפנו לעותק מיושן רק כדי להתאים לגיבוב הישן.

**source_collision / destination_collision:** ערוץ פיזי, תפקיד או מזהה ישות מוכפל. תארו במפורש את שני צדי החלפת התפקידים ובדקו שנקודת קצה שלא השתנתה אינה שומרת את מזהה היעד המבוקש.

**role_not_allowed / capability_missing:** הצרכן יגיע לעומס לא מתאים או יאבד יכולת. ודאו אם עליו לעקוב אחר התפקיד או החומרה. אל תרחיבו אוטומטית allowed_roles ואל תצהירו על יכולות שאין לחומרה. מנורה שהוחלפה בממסר הפעלה/כיבוי אינה יכולה לעמעם.

**missing_policy / unmodeled_reference:** מנו את נקודת הקצה שאליה מפנים והוסיפו הצהרת צרכן מפורשת רק לאחר אישור מטרתה. מחרוזת היסטוריה ישנה עשויה להיות מחוץ להיקף הפעיל; הוציאו במכוון את הקובץ מההיקף, תעדו את ההחרגה וצרו מחדש את חוזה המקורות.

**dynamic_reference / embedded_reference / indirect_target:** גרסה זו אינה יכולה להוכיח את המיפוי. בדקו בנפרד Jinja או התנהגות קבוצה/אזור/תווית, או ספקו תצורה מילולית מנורמלת מפורשת. התוכנית לעולם אינה מריצה תבנית.

**display_domain_review / service_data_review / mixed_action_targets:** בדקו תכונות כרטיסים, פרמטרי פעולות ואצוות יעדים. פצלו פעולה רב־תחומית בשינוי מקור שנבדק בנפרד; אל תשנו רק את תחום השירות שלה.

**retire_scope_mixed / overlapping_edits:** בחרו אובייקט צרכן ישן עקבי ללא הפניות לא קשורות. אל תמחקו רק entity_id מפעולה: הדבר עלול ליצור יעד רחב או תצורה לא תקינה. התוכנית אינה מחילה הוצאה אוטומטית משימוש.

**unsupported_source:** ניתן לתכנן רק JSON. YAML, קבצים בינריים ואחרים אינם מדולגים בשקט. עותק JSON שנורמל במפורש יכול לעזור בניתוח, אך יש להשוותו למקור לפני עריכה אמיתית.

דווחו על באג עם קלט סינתטי מזערי, גרסאות הכלי/Python, קוד יציאה וקודי אבחון. לעולם אל תצרפו יצוא גולמי של הבית או אישורי API.

</div>
