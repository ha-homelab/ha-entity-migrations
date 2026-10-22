# สถาปัตยกรรมและสัญญารูปแบบรายงาน

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

[แบบจำลอง](model.md) · [ข้อจำกัด](limitations.md)

![การไหลของข้อมูลแบบอ่านอย่างเดียว](../diagrams/pipeline.svg)

`io.py` บังคับใช้ขอบเขตของไฟล์ พาธ JSON และพอยน์เตอร์ที่แน่นอน `planner.py` ตรวจสอบคำประกาศ สร้างแผนผังก่อน/หลัง สแกนค่าต้นทาง แก้ไขนโยบายที่ระบุชัดเจน และรวบรวมข้อมูลวินิจฉัย `cli.py` เพิ่มข้อความแปลและพิมพ์รายงาน `i18n.py` มีแค็ตตาล็อกข้อความครบถ้วนสี่ภาษา เส้นทางนี้ไม่ขึ้นกับเครือข่ายหรือ Home Assistant

ตัวสแกนจงใจระมัดระวัง สตริงที่มีรูปแบบตรงกับการอ้างอิงเอนทิตีจะถูกตรวจเทียบกับสแนปช็อต สตริงที่ฝังการอ้างอิงไว้ยังถือว่าแก้ไขไม่ได้ เทมเพลตในคีย์หรือค่าและคีย์เป้าหมายอุปกรณ์/พื้นที่/ป้ายกำกับยังถือว่าแก้ไขไม่ได้ แม้จะดูเดาความหมายได้ง่าย ฟิลด์บริการทั่วไปไม่ถือเป็น ID เอนทิตี แต่บริการแบบไดนามิกยังไม่ถูกแก้ไข ไฟล์ที่ไม่ใช่ JSON จะถูกบันทึกเป็นแหล่งข้อมูลที่ไม่รองรับและบล็อกการวางแผน นี่ไม่ใช่ตัวแยกวิเคราะห์ HA ทั่วไป

![การตัดสินใจตามนโยบาย](../diagrams/policy.svg)

## โครงหุ้ม JSON ที่คงที่ สคีมาเวอร์ชัน 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary` เมื่ออินพุตถูกต้อง `status` จะเป็น ready หรือ blocked โดย `scope` เป็น `supplied_files_only` เสมอ และ `read_only` เป็น true เสมอ ข้อผิดพลาดอินพุตใช้โครงหุ้ม invalid ที่เล็กกว่าตามที่อธิบายในคู่มือติดตั้ง

รายการแก้ไขมีการดำเนินการ ไฟล์ และพอยน์เตอร์ `replace_reference` มี before/after/policy เพิ่มเติม `replace_service` มี before/after และ `remove_consumer` มีการอ้างอิงที่จะเลิกใช้ สิ่งเหล่านี้ **ไม่ใช่ JSON Patch ที่นำไปรันได้** เพราะไม่มีความหมายด้านธุรกรรม การเลื่อนดัชนี หรือวงจรชีวิต HA ให้ทบทวนเป็นข้อเสนอ รุ่นนี้จงใจไม่มีเครื่องมือใช้แพตช์

การวินิจฉัยมี `code`, `location`, `severity` ที่คงที่ และ `message` ที่แปลแล้ว ทั้ง `error` และ `unresolved` บล็อกแผน รายงาน `blocked` อาจมีข้อเสนอแก้ไขสำหรับการอ้างอิงที่ไม่ได้รับผลกระทบ แต่ไม่มีข้อใดเป็นธุรกรรมพร้อมใช้ แบบจำลองเริ่มต้นที่เก่าหรือขัดแย้งจะระงับข้อเสนอแก้ไขการอ้างอิงทั้งหมด การกำหนดค่าต่าง ๆ สะท้อนแบบจำลองที่ผู้ใช้ขอเสมอ ไม่ใช่การเปลี่ยนแปลงที่เสร็จแล้ว

รายงานเรียงแหล่งข้อมูล การกำหนดค่า รายการแก้ไข และการวินิจฉัยเพื่อทำซ้ำได้ ไม่มีเวลาปัจจุบันหรือคะแนนความมั่นใจที่แต่งขึ้น แฮชของไบต์พิสูจน์ว่าได้วิเคราะห์อินพุตเวอร์ชันใด ไม่ได้พิสูจน์ว่าอินพุตเป็นจริงหรืออุปกรณ์จะทำตามคำสั่ง
