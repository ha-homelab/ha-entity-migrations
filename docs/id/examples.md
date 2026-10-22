# Contoh lengkap

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

[Model masukan](model.md) · [Arsitektur](architecture.md)

Semua perangkat keras dan peran di sini sintetis. Buat ulang masukan identik dengan `python3 tools/generate_examples.py`. Tidak ada perintah yang terhubung ke Home Assistant.

## Peran lampu meninggalkan stopkontak yang dialihfungsikan

Jalankan perintah README untuk `examples/role-swap`. Awalnya `plug-a/1` memiliki `light.workbench` dan `plug-b/1` memiliki `switch.spare`. Manifest menetapkan peran pompa pada stopkontak A dan peran meja kerja pada B. Otomasi penerangan memakai `follows_role` dan hanya mengizinkan `workbench`. Referensinya tetap `light.workbench` sementara perangkat keras tujuan berubah. Tidak adanya edit teks adalah hasil yang disengaja, bukan migrasi yang terlewat. `assignments` pada laporan memuat perubahan perangkat keras untuk ditinjau manusia.

Konsumen cadangan lama dihentikan pada `/1`, yakni seluruh objek otomasi kedua. Ini tidak menyisakan urutan aksi kosong. Laporan bersifat saran; program tidak menghapus elemen array JSON. Jika menerapkan beberapa usulan penghapusan array secara manual, perhitungkan pergeseran indeks dan jalankan ulang dari snapshot baru.

Ubah kebijakan pertama menjadi `follows_hardware` sambil tetap mengizinkan peran `workbench`: rencana diblokir dengan `role_not_allowed`. Memperluas daftar tersebut agar mencakup pompa merupakan perubahan niat eksplisit yang berbahaya, bukan cara rutin menghilangkan kesalahan. Pulihkan kebijakan yang benar.

## Relai berubah dari light menjadi switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

Dua edit yang diusulkan mengubah target dan layanan `light.turn_off` miliknya. Tambahkan data kecerahan ke aksi sumber, perbarui sidik jari sumber yang disetujui, lalu jalankan ulang: `service_data_review` memblokir konversi otomatis. Jangan membuang pengaturan kecerahan sekadar untuk lolos pemeriksaan; tinjau perilaku yang diinginkan.

## Template belum terselesaikan

Jalankan perintah yang sama dengan `examples/blocked-template`. Target berupa Jinja dinamis. Alat tidak mengevaluasinya dan mengembalikan kode 3. Rencana lengkap yang didukung membutuhkan konfigurasi eksplisit dengan target literal yang dapat dibuktikan; jika tidak, pertahankan sebagai migrasi manual terdokumentasi di luar cakupan siap. Mengabaikan kode keluar tidak menyelesaikan template.

## Penyimpangan dan keterulangan

Mengedit sumber tanpa mengubah hash manifest menghasilkan `stale_source`. Mengedit snapshot menghasilkan `stale_snapshot`. Tidak ada kandidat edit referensi yang dikeluarkan untuk model kedaluwarsa tersebut. Pada file yang tidak berubah, hasil JSON deterministik kecuali bahasa pilihan. File sumber tetap identik byte demi byte.

Untuk proyek nyata, salin format ke folder privat, verifikasi identitas fisik, inventarisasi konsumen, dan jalankan perencana. Tinjau semua penetapan dan edit, lakukan pemeriksaan HA sendiri dalam proses penerapan yang telah ditetapkan, lalu buat snapshot hanya baca baru untuk memverifikasi hasil. Proyek ini tidak mengimplementasikan penerapan tersebut maupun pelaksana rollback.
