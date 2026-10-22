# การติดตั้งและ CLI

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

[ดัชนีเอกสาร](../../README.md#documentation)

ใช้ Python 3.11 หรือใหม่กว่า สร้างและเปิดใช้สภาพแวดล้อมเสมือนเฉพาะ แล้วรัน `python3 -m pip install -e .` จากสำเนารีโพซิทอรี แพ็กเกจไม่มีการพึ่งพาขณะทำงาน แต่ pip อาจดาวน์โหลดแบ็กเอนด์การสร้าง สำหรับเครื่องออฟไลน์ให้เตรียม wheel และสิ่งที่ต้องใช้ในการสร้างไว้ก่อน ตรวจสอบการติดตั้งที่เลือกด้วย `ha-entity-migrations --version` ซึ่งแสดงเวอร์ชันแพ็กเกจที่ติดตั้ง

CLI มีสองคำสั่ง โดยตัวเลือกภาษารวมอยู่ก่อนคำสั่ง:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` พิมพ์ SHA-256 ตัวพิมพ์เล็กของไบต์ไฟล์อย่างตรงตัว ไม่ได้ตรวจว่าไฟล์เป็น JSON ที่ถูกต้อง ลายนิ้วมือสแนปช็อตและต้นทางในแมนิเฟสต์ต้องตรงกับไฟล์ทุกประการรวมช่องว่าง อย่าอัปเดตลายนิ้วมือเพียงเพื่อกลบความคลาดเคลื่อนที่ไม่คาดคิด ให้เปรียบเทียบและอนุมัติอินพุตใหม่ก่อน

`plan` อ่านแมนิเฟสต์ JSON สแนปช็อต JSON ที่ปรับรูปแบบแล้ว และเฉพาะไฟล์ที่ระบุชัดใน `manifest.sources` โดยสัมพันธ์กับ `--root` ไม่ค้นไดเรกทอรีแบบวนซ้ำหรือค้นโฟลเดอร์ส่วนตัว ผลลัพธ์เริ่มต้นเป็น JSON มีเพียงข้อความสำหรับมนุษย์ที่เปลี่ยนตาม `--lang en|ru|de|es` ชื่อฟิลด์และรหัสวินิจฉัยคงเดิม `--help` มีทั้งระดับหลักและแต่ละคำสั่ง ไม่มีคำสั่งนำใช้ อัปโหลด ค้นพบ หรือยืนยันตัวตน

สถานะออก:

- **0:** ขอบเขตอินพุตที่รองรับสอดคล้องกันภายในและพร้อมให้ตรวจสอบ
- **2:** อาร์กิวเมนต์/อินพุตไม่ถูกต้อง อ่านไฟล์ไม่ได้ หรือละเมิดสคีมา/ขีดจำกัด
- **3:** อินพุตมีโครงสร้างถูกต้องแต่แผนถูกบล็อกเพราะขัดแย้งหรือมีขอบเขตที่ยังแก้ไขไม่ได้

ความล้มเหลวของอินพุตหลังแยกอาร์กิวเมนต์สร้างโครงหุ้ม JSON บน stdout ที่มี `status: invalid` ข้อผิดพลาดอาร์กิวเมนต์พิมพ์วิธีใช้ที่แปลแล้วบน stderr การคำนวณลายนิ้วมือสำเร็จพิมพ์เฉพาะค่าแฮช ในโหมดข้อความ รายการแก้ไขยังใช้ชื่อฟิลด์สำหรับเครื่อง แต่แปลคำอธิบาย

เก็บไฟล์ใช้งานในไดเรกทอรีส่วนตัว การเปลี่ยนทาง stdout สร้างรายงานของคุณเองซึ่งอาจมีชื่อเอนทิตีและพาธที่ระบุตัวตนได้ ตัวเครื่องมือไม่เขียนอะไร ถอนการติดตั้งด้วย `python3 -m pip uninstall ha-entity-migrations` ดูการตรวจสำหรับนักพัฒนาที่ [CONTRIBUTING](../../CONTRIBUTING.md)
