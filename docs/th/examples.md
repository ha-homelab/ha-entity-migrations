# ตัวอย่างพร้อมคำอธิบาย

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

[แบบจำลองอินพุต](model.md) · [สถาปัตยกรรม](architecture.md)

ฮาร์ดแวร์และบทบาททั้งหมดในนี้เป็นข้อมูลสังเคราะห์ สร้างอินพุตเหมือนเดิมได้ด้วย `python3 tools/generate_examples.py` ไม่มีคำสั่งใดเชื่อมต่อ Home Assistant

## บทบาทหลอดไฟย้ายออกจากปลั๊กที่เปลี่ยนหน้าที่

รันคำสั่ง README สำหรับ `examples/role-swap` เริ่มแรก `plug-a/1` ครอบครอง `light.workbench` และ `plug-b/1` ครอบครอง `switch.spare` แมนิเฟสต์กำหนดบทบาทปั๊มให้ปลั๊ก A และบทบาทโต๊ะทำงานให้ปลั๊ก B ระบบอัตโนมัติของไฟใช้ `follows_role` และยอมให้เฉพาะ `workbench` การอ้างอิงยังเป็น `light.workbench` ขณะที่ฮาร์ดแวร์ปลายทางเปลี่ยน การไม่มีการแก้ไขข้อความคือผลที่ตั้งใจ ไม่ใช่การย้ายที่ตกหล่น `assignments` ในรายงานมีการเปลี่ยนฮาร์ดแวร์ให้มนุษย์ตรวจสอบ

ผู้ใช้อ้างอิงสำรองเดิมจะถูกเลิกใช้ที่ `/1` ซึ่งคือออบเจ็กต์ระบบอัตโนมัติลำดับที่สองทั้งก้อน จึงไม่เหลือลำดับการกระทำว่าง รายงานเป็นเพียงคำแนะนำ โปรแกรมไม่ลบสมาชิกอาร์เรย์ JSON หากใช้ข้อเสนอลบหลายรายการด้วยตนเอง ต้องคำนึงถึงดัชนีที่เลื่อนและรันใหม่จากสแนปช็อตล่าสุด

เปลี่ยนนโยบายแรกเป็น `follows_hardware` แต่คงบทบาทที่อนุญาตเป็น `workbench` แผนจะถูกบล็อกด้วย `role_not_allowed` การขยายรายการให้รวมปั๊มคือการเปลี่ยนเจตนาอย่างชัดเจนและอันตราย ไม่ใช่วิธีปกติในการลบข้อผิดพลาด ให้คืนค่านโยบายที่ถูกต้องแทน

## รีเลย์เปลี่ยนจาก light เป็น switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

ข้อเสนอแก้ไขสองรายการเปลี่ยนเป้าหมายและบริการ `light.turn_off` ของมัน เพิ่มข้อมูลความสว่างให้การกระทำต้นทาง อัปเดตลายนิ้วมือแหล่งข้อมูลที่อนุมัติแล้วและรันใหม่ `service_data_review` จะบล็อกการแปลงอัตโนมัติ อย่าลบการตั้งค่าความสว่างเพียงเพื่อให้ผ่านเครื่องมือ ให้ตรวจสอบพฤติกรรมที่ต้องการ

## เทมเพลตที่ยังแก้ไขไม่ได้

รันคำสั่งเดิมกับ `examples/blocked-template` เป้าหมายเป็น Jinja แบบไดนามิก เครื่องมือไม่ประเมินค่าและคืนรหัส 3 แผนที่รองรับครบถ้วนต้องมีการกำหนดค่าชัดเจนพร้อมเป้าหมายค่าคงที่ที่พิสูจน์ได้ มิฉะนั้นให้เก็บส่วนนี้เป็นงานย้ายด้วยตนเองที่มีเอกสารและอยู่นอกขอบเขตพร้อมใช้ การละเลยรหัสออกไม่ได้แก้เทมเพลต

## ความคลาดเคลื่อนและการทำซ้ำ

แก้ไขแหล่งข้อมูลโดยไม่เปลี่ยนแฮชในแมนิเฟสต์จะได้ `stale_source` แก้ไขสแนปช็อตจะได้ `stale_snapshot` แบบจำลองเก่าเหล่านี้จะไม่ส่งออกข้อเสนอแก้ไขการอ้างอิง เมื่อไฟล์ไม่เปลี่ยน ผล JSON จะคงเดิมยกเว้นภาษาที่เลือก ไฟล์ต้นทางไม่เปลี่ยนแม้แต่ไบต์เดียว

สำหรับโครงการจริง ให้คัดลอกรูปแบบไปยังโฟลเดอร์ส่วนตัว ตรวจสอบตัวตนทางกายภาพ ระบุผู้ใช้อ้างอิงทั้งหมด และรันตัววางแผน ตรวจสอบการกำหนดค่าและรายการแก้ไขทั้งหมด ทำการตรวจของ HA ภายในกระบวนการนำใช้ที่มีอยู่ แล้วสร้างสแนปช็อตอ่านอย่างเดียวใหม่เพื่อตรวจผล โครงการนี้ไม่ได้ทำการนำใช้นั้นหรือมีตัวดำเนินการย้อนกลับ
