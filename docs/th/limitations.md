# ข้อจำกัดและขอบเขตการตรวจสอบ

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

[สถาปัตยกรรม](architecture.md) · [ความปลอดภัย](../../SECURITY.md)

ความแม่นยำของแผนจำกัดด้วยคำประกาศฮาร์ดแวร์/ช่อง/บทบาทและไฟล์ที่ให้ เครื่องมือไม่ค้นพบแดชบอร์ดที่ตกหล่น ทริกเกอร์อุปกรณ์ ฉาก บลูพริ้นต์ ระบบอัตโนมัติที่เก็บที่อื่น ตัวกรอง Matter ไคลเอนต์ภายนอก หรือสถานะแฝงของการเชื่อมต่อ อย่าเรียกรายงานพร้อมใช้ว่าการตรวจ Home Assistant ครบถ้วน รุ่นนี้บทบาทต้องไม่ซ้ำ บทบาทเชิงความหมายแบบหลายต่อหลายและกลุ่มต้องแยกด้วยตนเอง

รองรับแหล่งการกำหนดค่า JSON แต่ไม่ตีความ YAML, include, ชื่อแทน, anchor, แท็กที่รันได้, คอมโพเนนต์กำหนดเอง หรือเทมเพลตที่สร้างขณะทำงาน การปรับรูปแบบอยู่นอกรุ่นนี้และอาจสูญเสียความหมาย ให้เก็บต้นฉบับและตรวจความเท่าเทียม แม้ JSON ที่รองรับก็ไม่ได้ตรวจตามสคีมาการกำหนดค่า HA ทั้งหมด การลบออบเจ็กต์ผู้ใช้อ้างอิงอาจเหลือออบเจ็กต์แม่ที่ไม่ถูกต้อง ให้ตรวจแม่และรันตัวตรวจการกำหนดค่า HA ในกระบวนการทดสอบก่อนนำใช้ตามปกติ

ความสามารถและบทบาทที่อนุญาตเป็นข้อจำกัดที่ระบุ ไม่ใช่ความปลอดภัยจากการอนุมาน เครื่องมือไม่รู้ว่ามีปั๊มหรือมอเตอร์ประตูโรงรถเสียบแทนโหลดที่เคยไม่เป็นอันตราย สถานะรีเลย์ที่รายงานไม่ได้พิสูจน์พฤติกรรมหน้าสัมผัส/โหลด อย่ารันสคริปต์ทั้งบ้านหรือตัดแล้วจ่ายไฟเครื่องที่ใช้งานอยู่เพียงเพื่อตรวจชื่อ การทดสอบใช้งานทางกายภาพต้องเป็นขั้นตอนควบคุมแยกต่างหาก

รุ่นนี้ไม่ใช้แผน ไม่เปลี่ยนชื่อเอนทิตีในทะเบียน ไม่แก้ ID เฉพาะ ไม่โหลด HA ใหม่ ไม่รีสตาร์ตตัวควบคุม ไม่เลิกใช้การเชื่อมต่อ และไม่ย้อนการเปลี่ยนแปลง การดำเนินการที่คืนมาเป็นคำแนะนำ ไม่ใช่ JSON Patch ที่รันได้ หากนำไปทำเองต้องใช้สแนปช็อตใหม่และตรวจหลังการเปลี่ยนแปลงแต่ละรายการที่ผ่านทบทวน เพราะดัชนีและเวอร์ชันอาจเปลี่ยน แฮชไม่ใช่ลายเซ็นหรือการควบคุมสิทธิ์

รายงานอาจมีชื่อและตัวระบุส่วนตัว อย่าใส่ใน Git สาธารณะ ระบบติดตามปัญหา หรือสิ่งส่งมอบ CI ตัวอย่างสาธารณะใช้อุปกรณ์สังเคราะห์และไม่อ้างว่าผ่านการทดสอบภาคสนาม การวินิจฉัยบล็อกแผนตามการออกแบบ ไม่มีตัวเลือกบังคับ รายการละเว้น หรือโหมดผ่อนปรนที่ซ่อนอยู่
