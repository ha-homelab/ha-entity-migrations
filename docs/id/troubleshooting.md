# Pemecahan masalah

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

[Instalasi](installation.md) · [Batasan](limitations.md)

**Perintah tidak ditemukan:** aktifkan lingkungan virtual yang digunakan saat instalasi. Coba `python3 -m ha_entity_migrations --version`; jangan memasang ke Python sistem hanya untuk mengatasi jalur yang tidak cocok.

**Keluar 2, schema_invalid:** bandingkan kunci dengan contoh yang dapat dijalankan dan [model masukan](model.md). Kolom tak dikenal adalah kesalahan. Versi berupa bilangan bulat 1; pengenal kanal berupa string. Setiap kebijakan aksi membutuhkan pointer layanan. Snapshot memiliki entitas; manifest memiliki penetapan dan konsumen. Kedua file tidak dapat dipertukarkan.

**Keluar 2, duplicate_source:** dua nama sumber mengidentifikasi satu file fisik. Simpan satu nama kanonis di `sources` dan perbarui semua kolom `file` konsumen. Hapus pemisah ganda atau alias hard link/kapitalisasi; jangan memberi kebijakan kedua kepada alias. File terpisah dengan isi identik tetap didukung.

**stale_snapshot / stale_source:** bandingkan perubahan nyata dengan sumber yang disetujui. Gunakan fingerprint hanya setelah meninjaunya. Perubahan spasi memengaruhi hash. Jangan menunjuk salinan usang hanya supaya cocok dengan hash lama.

**source_collision / destination_collision:** kanal fisik, peran, atau ID entitas terduplikasi. Nyatakan kedua sisi pertukaran peran secara eksplisit dan pastikan endpoint yang tidak berubah tidak mempertahankan ID tujuan yang diinginkan.

**role_not_allowed / capability_missing:** konsumen akan mencapai beban yang tidak tepat atau kehilangan kemampuan. Pastikan apakah harus mengikuti peran atau perangkat keras. Jangan otomatis memperluas allowed_roles atau mengklaim kemampuan yang tidak dimiliki perangkat. Lampu yang diganti relai on/off tidak dapat meredup.

**missing_policy / unmodeled_reference:** inventarisasi endpoint referensi dan tambahkan deklarasi konsumen eksplisit hanya setelah tujuannya dipastikan. String riwayat lama mungkin di luar cakupan aktif; keluarkan file dari cakupan dengan sengaja, dokumentasikan pengecualian, dan buat ulang kontrak sumber.

**dynamic_reference / embedded_reference / indirect_target:** rilis ini tidak dapat membuktikan pemetaan. Tinjau Jinja atau perilaku grup/area/label secara terpisah, atau sediakan konfigurasi literal ternormalisasi eksplisit. Program tidak pernah menjalankan template.

**display_domain_review / service_data_review / mixed_action_targets:** periksa fitur kartu, parameter aksi, dan kelompok target. Pisahkan aksi lintas domain dalam perubahan sumber yang ditinjau tersendiri; jangan hanya mengganti domain layanannya.

**retire_scope_mixed / overlapping_edits:** pilih objek konsumen usang yang koheren tanpa referensi lain. Jangan hanya menghapus entity_id dari aksi: itu dapat menciptakan target luas atau konfigurasi tidak valid. Program tidak menerapkan penghentian otomatis.

**unsupported_source:** hanya JSON yang dapat direncanakan. YAML, biner, dan file lain tidak dilewati diam-diam. Salinan JSON yang dinormalisasi eksplisit dapat membantu analisis, tetapi harus dibandingkan dengan aslinya sebelum edit nyata.

Laporkan bug dengan masukan sintetis minimal, versi alat/Python, kode keluar, dan kode diagnostik. Jangan pernah melampirkan ekspor rumah mentah atau kredensial API.
