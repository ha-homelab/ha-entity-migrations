# Model masukan

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/model.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/model.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/model.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/model.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/model.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/model.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/model.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/model.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/model.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/model.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/model.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/model.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/model.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/model.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/model.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/model.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/model.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/model.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/model.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/model.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/model.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/model.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/model.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/model.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Instalasi](installation.md) · [Contoh](examples.md)

Semua dokumen memakai JSON UTF-8 ketat. Kunci ganda, angka non-finit, dan kolom skema tak dikenal ditolak. Contoh persis dalam `examples/` merupakan referensi yang dapat dijalankan. Kolom versi harus berupa bilangan bulat `1`, bukan string atau boolean.

## Snapshot

Objek teratas hanya memuat `version` dan `entities`. Setiap entitas memuat tepat:

- `entity_id`: ID domain/objek huruf kecil, seperti `light.workbench`.
- `hardware_id`: pengenal privat opak yang dipilih operator.
- `channel`: pengenal kanal fisik, berupa string.
- `role`: tujuan logis unik, seperti `workbench` atau `pump_enable`.
- `capabilities`: string unik yang menjelaskan kemampuan, misalnya `on_off`.

Pasangan perangkat keras/kanal mengidentifikasi endpoint fisik. ID entitas, endpoint fisik, dan peran logis masing-masing harus unik. Wakili diagnostik fisik sebagai kanal berbeda, misalnya `rssi`, dengan peran uniknya sendiri. Peran adalah label perencanaan, bukan area, label, atau kelas perangkat HA. Deklarasi ini bukan pengukuran; alat tidak dapat memverifikasinya terhadap perangkat keras.

## Manifest

Objek teratas mempunyai tepat `version`, `snapshot_sha256`, `sources`, `assignments`, dan `consumers`. `sources` memetakan nama file relatif ke digest SHA-256. `assignments` memuat catatan entitas pengganti lengkap untuk endpoint fisik yang sudah ada di snapshot. Endpoint yang tidak tercantum tetap tidak berubah. Untuk menambahkan perangkat, sertakan dahulu endpoint cadangannya yang teramati ke dalam snapshot. Tidak ada pembuatan atau penghapusan perangkat keras implisit, dan rilis ini mensyaratkan peran unik.

Setiap konsumen mengidentifikasi **nilai string literal** dengan `file` dan `pointer` RFC 6901. Escape `/` sebagai `~1` dan `~` sebagai `~0`; indeks daftar dimulai dari nol tanpa nol di depan. Setiap referensi yang ditemukan membutuhkan kebijakan eksplisit:

- `follows_role`: temukan tujuan yang memiliki peran logis sumber.
- `follows_hardware`: pertahankan kanal fisik sumber dan gunakan ID entitas barunya.
- `retire`: usulkan penghapusan objek eksplisit `retire_scope` yang memuat referensi.

Konsumen yang tidak dihentikan juga memerlukan `kind` (`action`, `display`, `reference`), `allowed_roles` (tidak kosong), dan `required_capabilities` (boleh kosong). Aksi memerlukan `service_pointer`. Batas ini mencegah pompa yang dialihfungsikan dipakai sebagai target penerangan. Semuanya deklarasi, bukan inferensi niat.

Konsumen yang dihentikan memiliki tepat empat kolom: file, pointer, policy, dan retire_scope. Cakupan harus berupa objek leluhur yang bukan akar. Hanya referensi ke sumber yang sama-sama dihentikan yang boleh ada; referensi campuran atau dinamis memblokirnya. Pilih seluruh otomasi usang jika menghapus aksi akan menyisakan urutan kosong yang tidak valid. Alat tidak menjalankan validator skema HA.

## Perubahan domain

Untuk aksi yang melintasi light/switch, hanya `turn_on`, `turn_off`, `toggle`, dan layanan `homeassistant.*` yang sesuai yang didukung. `data` atau `data_template` tidak kosong tidak diterima untuk konversi layanan otomatis. Layanan khusus domain dengan beberapa target literal diblokir. Pointer layanan harus memiliki target di bawah aksinya. Perubahan domain tampilan selalu memerlukan tinjauan manual fitur kartu; switch tidak dapat diam-diam mewarisi kontrol kecerahan.

## Batas

2 MiB per file; gabungan sumber 16 MiB; 64 file; 5.000 entitas, penetapan, atau konsumen; kedalaman JSON 40 dan 100.000 node nilai per file. Pengenal adalah string tidak kosong sampai 256 karakter; daftar kapabilitas/peran yang diizinkan sampai 64 string unik. Jalur relatif tidak boleh naik ke induk, absolut, atau mengandung tautan simbolik. Masukan hanya berupa file reguler.

Pemuat file menolak dua nama sumber yang mengarah ke jalur kanonis atau identitas file terbuka (perangkat/inode) yang sama. Ini mencakup pemisah berulang, hard link, dan alias kapitalisasi pada sistem file yang tidak membedakan huruf besar/kecil. Pertahankan satu nama dan perbarui konsumennya; alias tidak boleh membawa kebijakan migrasi berbeda untuk satu file fisik. File independen dengan isi identik tetap valid. API murni `plan` tidak mengakses sistem file: pemanggil yang membuat pemetaan sumber sendiri harus menegakkan batas identitas ini sebelum memanggilnya.
