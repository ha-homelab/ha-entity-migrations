# התקנה ו־CLI

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


<div dir="rtl" lang="he">

[אינדקס התיעוד](../../README.md#documentation)

השתמשו ב־Python 3.11 ומעלה. צרו והפעילו סביבה וירטואלית ייעודית, ואז הריצו `python3 -m pip install -e .` מעותק המאגר. לחבילה אין תלויות זמן ריצה; pip עשוי להוריד את מנוע הבנייה. למחשב ללא רשת הכינו מראש wheel ותלויות בנייה. אמתו את ההתקנה שנבחרה באמצעות `ha-entity-migrations --version`, המציג את גרסת החבילה המותקנת.

ל־CLI שתי פקודות, ואפשרות השפה הכללית באה לפני הפקודה:

</div>

<div dir="ltr">

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

</div>

<div dir="rtl" lang="he">

`fingerprint` מדפיס SHA-256 באותיות קטנות של הבתים המדויקים בקובץ. הוא אינו מאמת את הקובץ כ־JSON. טביעות האצבע של תמונת המצב והמקורות במניפסט חייבות להתאים בדיוק לקבצים, כולל רווחים. אל תרעננו טביעת אצבע רק כדי לבטל סטייה לא צפויה; השוו ואשרו תחילה את הקלט החדש.

`plan` קורא מניפסט JSON, תמונת מצב JSON מנורמלת ורק קבצים שצוינו במפורש ב־`manifest.sources`, יחסית ל־`--root`. הוא אינו סורק תיקיות רקורסיבית או מחפש בתיקיית הבית. פלט ברירת המחדל הוא JSON. רק הודעות לבני אדם משתנות עם `--lang en|ru|de|es`; שמות השדות וקודי האבחון נשארים יציבים. `--help` זמין ברמה הראשית ולכל פקודה. אין פקודה להחלה, העלאה, גילוי או אימות זהות.

מצב יציאה:

- **0:** היקף הקלט הנתמך עקבי פנימית ומוכן לבדיקה.
- **2:** ארגומנטים/קלט לא תקינים, קובץ בלתי קריא או הפרת סכימה/מגבלה.
- **3:** קלט תקין מבנית יצר תוכנית חסומה בגלל סתירה או היקף לא פתור.

כשלי קלט לאחר ניתוח הארגומנטים יוצרים מעטפת JSON ב־stdout עם `status: invalid`. שגיאות ארגומנטים מדפיסות הוראות שימוש מתורגמות ב־stderr. חישוב מוצלח של טביעת אצבע מדפיס רק את הגיבוב. במצב טקסט רשומות העריכות המוצעות שומרות את שמות השדות למכונה; ההסברים מתורגמים.

שמרו קבצים תפעוליים בתיקייה פרטית. הפניית stdout יוצרת דוח משלכם, שעשוי לכלול שמות ישויות ונתיבים מזהים. הכלי עצמו אינו כותב דבר. להסרה הריצו `python3 -m pip uninstall ha-entity-migrations`. לבדיקות פיתוח ראו [CONTRIBUTING](../../CONTRIBUTING.md).

</div>
