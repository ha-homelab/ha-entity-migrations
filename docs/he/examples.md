# דוגמאות מוסברות

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


<div dir="rtl" lang="he">

[מודל הקלט](model.md) · [ארכיטקטורה](architecture.md)

כל החומרה והתפקידים כאן סינתטיים. צרו שוב קלט זהה באמצעות `python3 tools/generate_examples.py`. שום פקודה אינה מתחברת ל־Home Assistant.

## תפקיד מנורה עוזב שקע ששינה ייעוד

הריצו את פקודת README עבור `examples/role-swap`. בתחילה `plug-a/1` מחזיק ב־`light.workbench`, ו־`plug-b/1` מחזיק ב־`switch.spare`. המניפסט מקצה את תפקיד המשאבה לשקע A ואת תפקיד שולחן העבודה לשקע B. אוטומציית התאורה משתמשת ב־`follows_role` ומאפשרת רק `workbench`. ההפניה נשארת `light.workbench` בעוד חומרת היעד משתנה. היעדר עריכת טקסט הוא התוצאה המכוונת, לא הסבה חסרה. `assignments` בדוח מכיל את שינויי החומרה לבדיקה אנושית.

הצרכן הרזרבי הישן מוצא משימוש ב־`/1`, כלומר כל אובייקט האוטומציה השני. כך לא נשאר רצף פעולות ריק. הדוח מייעץ בלבד; התוכנית אינה מוחקת איברי מערך JSON. אם מחילים ידנית כמה מחיקות מערך מוצעות, יש להתחשב בהסטת האינדקסים ולהריץ מחדש מתמונת מצב חדשה.

שנו את המדיניות הראשונה ל־`follows_hardware`, תוך השארת `workbench` כתפקיד מותר: התוכנית נחסמת עם `role_not_allowed`. הרחבת הרשימה כדי לכלול משאבה היא שינוי מפורש ומסוכן בכוונה, לא דרך שגרתית להסרת השגיאה. במקום זאת שחזרו את המדיניות הנכונה.

## ממסר עובר מ־light ל־switch

</div>

<div dir="ltr">

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

</div>

<div dir="rtl" lang="he">

שתי העריכות המוצעות משנות את היעד ואת השירות `light.turn_off` שלו. הוסיפו נתוני בהירות לפעולת המקור, עדכנו את טביעת האצבע המאושרת והריצו שוב: `service_data_review` חוסם המרה אוטומטית. אל תסירו הגדרות בהירות רק כדי לעבור בדיקה; בחנו את ההתנהגות הרצויה.

## תבנית לא פתורה

הריצו אותה פקודה עם `examples/blocked-template`. היעד הוא Jinja דינמי. הכלי אינו מעריך אותו ומחזיר קוד 3. תוכנית מלאה נתמכת דורשת תצורה מפורשת עם יעדים מילוליים ניתנים להוכחה; אחרת השאירו זאת כהסבה ידנית מתועדת מחוץ להיקף המוכן. התעלמות מקוד היציאה אינה פותרת את התבנית.

## סטייה וחזרתיות

עריכת מקור בלי שינוי הגיבוב שלו במניפסט יוצרת `stale_source`. עריכת תמונת המצב יוצרת `stale_snapshot`. לא מופקות עריכות הפניה מועמדות עבור מודלים מיושנים אלה. בקבצים ללא שינוי תוצאת JSON דטרמיניסטית למעט השפה שנבחרה. קובצי המקור נשארים זהים בית אחר בית.

לפרויקט אמיתי העתיקו את הפורמט לתיקייה פרטית, אמתו זהויות פיזיות, מנו את הצרכנים והריצו את המתכנן. בדקו את כל ההקצאות והעריכות, בצעו את בדיקות HA במסגרת תהליך הפריסה הקיים, ואז צרו תמונת מצב חדשה לקריאה בלבד כדי לאמת את התוצאה. פרויקט זה אינו מממש את הפריסה הזאת או מנגנון לביצוע שחזור לאחור.

</div>
