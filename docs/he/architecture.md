# ארכיטקטורה וחוזה הדוח

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


<div dir="rtl" lang="he">

[מודל](model.md) · [מגבלות](limitations.md)

![זרימת נתונים לקריאה בלבד](../diagrams/pipeline.svg)

`io.py` אוכף מגבלות על קבצים, נתיבים ו־JSON ומצביעים מדויקים. `planner.py` מאמת הצהרות, בונה מיפויי לפני/אחרי, סורק ערכי מקור, פותר מדיניות מפורשת ואוסף אבחונים. `cli.py` מוסיף הודעות מתורגמות ומדפיס את הדוח. `i18n.py` מכיל ארבעה קטלוגי הודעות מלאים. מסלול זה אינו תלוי ברשת או ב־Home Assistant.

הסורק שמרני במכוון. מחרוזות התואמות בדיוק להפניות לישויות נבדקות מול תמונת המצב. מחרוזות עם הפניות משובצות נשארות לא פתורות. תבניות במפתחות או בערכים, ומפתחות יעד של התקן/אזור/תווית, נשארים לא פתורים גם כשהפירוש נראה קל לניחוש. שדות שירות רגילים אינם נחשבים למזהי ישויות; שירותים דינמיים עדיין לא פתורים. קבצים שאינם JSON נרשמים כמקורות לא נתמכים וחוסמים את התכנון. זה אינו מנתח כללי של HA.

![זרימת החלטות המדיניות](../diagrams/policy.svg)

## מעטפת JSON יציבה, גרסת סכימה 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. בקלט תקין `status` הוא ready או blocked. `scope` תמיד `supplied_files_only`, ו־`read_only` תמיד true. שגיאות קלט משתמשות במעטפת invalid הקטנה יותר המתוארת בהתקנה.

עריכות כוללות פעולה, קובץ ומצביע. `replace_reference` כולל גם before/after/policy; `replace_service` כולל before/after; `remove_consumer` כולל את ההפניה המוצאת משימוש. אלו **אינן פקודות JSON Patch ניתנות לביצוע**. חסרה בהן סמנטיקה של עסקאות, הסטת אינדקסים ומחזור החיים של HA. בדקו אותן כהצעות; גרסה זו אינה מספקת בכוונה כלי להחלת טלאים.

אבחונים מכילים `code`, `location`, `severity` יציבים ו־`message` מתורגם. גם `error` וגם `unresolved` חוסמים תוכנית. דוחות `blocked` עשויים לכלול עריכות מועמדות להפניות שלא נפגעו, אך אף אחת אינה עסקה מוכנה. מודלים התחלתיים מיושנים או סותרים מונעים את כל עריכות ההפניות המועמדות. הקצאות משקפות תמיד את המודל שהמשתמש ביקש, לעולם לא שינויים שבוצעו.

הדוחות ממיינים מקורות, הקצאות, עריכות ואבחונים לשם שחזור. אין חותמות זמן נוכחיות או ציוני ביטחון מומצאים. גיבובי הבתים מוכיחים איזו גרסת קלט נותחה, לא אם הקלט אמיתי או אם התקן יציית לפקודה.

</div>
