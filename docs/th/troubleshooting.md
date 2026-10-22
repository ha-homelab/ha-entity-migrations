# การแก้ปัญหา

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

[การติดตั้ง](installation.md) · [ข้อจำกัด](limitations.md)

**ไม่พบคำสั่ง:** เปิดใช้สภาพแวดล้อมเสมือนเดียวกับที่ติดตั้ง ลอง `python3 -m ha_entity_migrations --version` อย่าติดตั้งลง Python ระบบเพียงเพื่อเลี่ยงปัญหาพาธไม่ตรง

**ออก 2, schema_invalid:** เปรียบเทียบคีย์กับตัวอย่างที่รันได้และ[แบบจำลองอินพุต](model.md) ฟิลด์ที่ไม่รู้จักเป็นข้อผิดพลาด เวอร์ชันเป็นจำนวนเต็ม 1 ตัวระบุช่องเป็นสตริง ทุกนโยบายการกระทำต้องมีพอยน์เตอร์บริการ สแนปช็อตมีเอนทิตี ส่วนแมนิเฟสต์มีการกำหนดค่าและผู้ใช้อ้างอิง สองไฟล์นี้ใช้แทนกันไม่ได้

**ออก 2, duplicate_source:** ชื่อแหล่งข้อมูลสองชื่อระบุไฟล์กายภาพเดียว ให้เหลือชื่อมาตรฐานเดียวใน `sources` และอัปเดตฟิลด์ `file` ของผู้ใช้อ้างอิงทั้งหมด ลบตัวคั่นซ้ำหรือชื่อแทนจากฮาร์ดลิงก์/ตัวพิมพ์ อย่ากำหนดนโยบายที่สองให้ชื่อแทน ไฟล์แยกที่มีเนื้อหาเหมือนกันยังรองรับ

**stale_snapshot / stale_source:** เปรียบเทียบการเปลี่ยนจริงกับต้นทางที่อนุมัติ ใช้คำสั่งลายนิ้วมือหลังตรวจแล้วเท่านั้น ช่องว่างมีผลต่อแฮช อย่าชี้สำเนาเก่าเพียงเพื่อให้ตรงแฮชเดิม

**source_collision / destination_collision:** ช่องกายภาพ บทบาท หรือ ID เอนทิตีซ้ำ ระบุทั้งสองด้านของการสลับบทบาทให้ชัด และตรวจว่าปลายทางที่ไม่เปลี่ยนไม่ได้ยึด ID เป้าหมายที่ต้องการอยู่

**role_not_allowed / capability_missing:** ผู้ใช้อ้างอิงจะเข้าถึงโหลดไม่เหมาะสมหรือสูญเสียความสามารถ ยืนยันว่าควรตามบทบาทหรือฮาร์ดแวร์ อย่าขยาย allowed_roles อัตโนมัติหรืออ้างความสามารถที่ฮาร์ดแวร์ไม่มี ไฟที่แทนด้วยรีเลย์เปิด/ปิดไม่สามารถหรี่ได้

**missing_policy / unmodeled_reference:** ทำรายการปลายทางที่ถูกอ้างอิงและเพิ่มคำประกาศผู้ใช้ชัดเจนหลังยืนยันวัตถุประสงค์แล้ว สตริงประวัติเก่าอาจอยู่นอกขอบเขตปัจจุบัน ให้ตั้งใจตัดไฟล์ออก บันทึกเหตุผล และสร้างสัญญาแหล่งข้อมูลใหม่

**dynamic_reference / embedded_reference / indirect_target:** รุ่นนี้พิสูจน์แผนผังไม่ได้ ตรวจ Jinja หรือพฤติกรรมกลุ่ม/พื้นที่/ป้ายแยกต่างหาก หรือให้การกำหนดค่าตรงตัวที่ปรับรูปแบบชัดเจน โปรแกรมไม่รันเทมเพลตเด็ดขาด

**display_domain_review / service_data_review / mixed_action_targets:** ตรวจฟังก์ชันการ์ด พารามิเตอร์การกระทำ และกลุ่มเป้าหมาย แยกการกระทำหลายโดเมนในงานแก้ต้นทางที่ทบทวนต่างหาก ไม่ใช่แค่เปลี่ยนโดเมนบริการ

**retire_scope_mixed / overlapping_edits:** เลือกออบเจ็กต์ผู้ใช้อ้างอิงเก่าที่สอดคล้องและไม่มีการอ้างอิงอื่น อย่าลบเฉพาะ entity_id จากการกระทำ เพราะอาจทำให้เป้าหมายกว้างเกินหรือการกำหนดค่าผิด โปรแกรมนี้ไม่เลิกใช้ให้อัตโนมัติ

**unsupported_source:** วางแผนได้เฉพาะ JSON ไฟล์ YAML ไบนารี และอื่น ๆ ไม่ถูกข้ามเงียบ ๆ สำเนา JSON ที่ปรับรูปแบบชัดเจนอาจช่วยวิเคราะห์ แต่ต้องเทียบต้นฉบับก่อนแก้จริง

รายงานบั๊กด้วยอินพุตสังเคราะห์น้อยที่สุด เวอร์ชันเครื่องมือ/Python รหัสออก และรหัสวินิจฉัย อย่าแนบข้อมูลส่งออกบ้านดิบหรือข้อมูลรับรอง API
