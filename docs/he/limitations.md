# מגבלות וגבולות הבדיקה

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


<div dir="rtl" lang="he">

[ארכיטקטורה](architecture.md) · [אבטחה](../../SECURITY.md)

דיוק התוכנית מוגבל להצהרות החומרה/ערוצים/תפקידים ולקבצים שסופקו. הכלי אינו מגלה לוחות מחוונים חסרים, טריגרים של התקנים, סצנות, blueprints, אוטומציות שנשמרו במקום אחר, מסנני Matter, לקוחות חיצוניים או מצב נסתר של אינטגרציה. דוח מוכן אינו ביקורת מלאה של Home Assistant. כל תפקיד ייחודי בגרסה זו; תפקידים סמנטיים רבים־לרבים וקבוצות דורשים פירוק ידני.

מקורות תצורה בפורמט JSON נתמכים. YAML עצמו, הכללות, כינויים, עוגנים, תגיות ניתנות לביצוע, רכיבים מותאמים ותבניות שנוצרות בזמן ריצה אינם מפורשים. נרמול אינו חלק מגרסה זו ועלול לאבד משמעות; שמרו את המקור ובדקו שקילות. גם JSON נתמך אינו נבדק מול סכימת התצורה המלאה של HA. הסרת אובייקט צרכן מפורש עלולה להשאיר הורה לא תקין; בדקו אותו והריצו את בודק התצורה של HA בתהליך הבדיקות המקדים הרגיל.

יכולות ותפקידים מותרים הם אילוצים מפורשים, לא בטיחות שהוסקה. הכלי אינו יודע שמשאבה או מנוע דלת מוסך חוברו לשקע שהיה תמים בעבר. מצב ממסר מדווח אינו מוכיח את התנהגות המגע/העומס. אל תריצו סקריפטים לכל הבית ואל תנתקו ותחברו מכשיר פעיל רק כדי לאמת שמות. הפעלה פיזית ראשונית שייכת לנוהל מבוקר נפרד.

גרסה זו אינה מחילה תוכנית, משנה שם של ישות ברישום, משנה מזהה ייחודי, טוענת מחדש את HA, מאתחלת בקר, מוציאה אינטגרציה משימוש או מבטלת שינוי. הפעולות המוחזרות הן המלצות, לא JSON Patch בר־ביצוע. בהחלה ידנית קחו תמונת מצב חדשה ואמתו לאחר כל שינוי שנבדק; אינדקסים וגרסאות עשויים להשתנות. גיבובים אינם מספקים חתימות או בקרת גישה.

דוחות עשויים להכיל שמות ומזהים פרטיים. שמרו אותם מחוץ ל־Git ציבורי, למערכות דיווח תקלות ולתוצרי CI. הדוגמאות הציבוריות משתמשות בהתקנים סינתטיים ואינן טוענות לאימות בשטח. האבחונים חוסמים בכוונה; אין דגל כפייה, רשימת התעלמות או מצב מתירני נסתר.

</div>
