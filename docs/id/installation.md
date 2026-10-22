# Instalasi dan CLI

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

[Indeks dokumentasi](../../README.md#documentation)

Gunakan Python 3.11 atau lebih baru. Buat dan aktifkan lingkungan virtual khusus, lalu jalankan `python3 -m pip install -e .` dari checkout. Paket tidak memiliki dependensi runtime; pip mungkin mengunduh backend build-nya. Untuk komputer offline, siapkan wheel dan dependensi build terlebih dahulu. Verifikasi instalasi terpilih dengan `ha-entity-migrations --version`, yang menampilkan versi paket terpasang.

CLI mempunyai dua perintah dengan opsi bahasa global sebelum perintah:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` mencetak SHA-256 huruf kecil dari byte file yang tepat. Perintah ini tidak memvalidasi file sebagai JSON. Sidik jari snapshot dan sumber dalam manifest harus cocok dengan file persis, termasuk spasi. Jangan memperbarui sidik jari hanya untuk mengabaikan penyimpangan tak terduga; bandingkan dan setujui masukan baru terlebih dahulu.

`plan` membaca manifest JSON, snapshot JSON ternormalisasi, dan hanya file yang disebut eksplisit dalam `manifest.sources`, relatif terhadap `--root`. Alat tidak menelusuri direktori secara rekursif atau mencari di direktori pribadi. Keluaran baku adalah JSON. Hanya pesan untuk manusia yang berubah melalui `--lang en|ru|de|es`; nama kolom dan kode diagnostik tetap stabil. `--help` tersedia pada tingkat atas dan setiap perintah. Tidak ada perintah penerapan, unggah, penemuan, atau autentikasi.

Status keluar:

- **0:** cakupan masukan yang didukung konsisten secara internal dan siap ditinjau.
- **2:** argumen/masukan tidak valid, file tidak terbaca, atau pelanggaran skema/batas.
- **3:** masukan yang valid secara struktur menghasilkan rencana terblokir karena konflik atau cakupan belum terselesaikan.

Kegagalan masukan setelah penguraian argumen menghasilkan pembungkus JSON di stdout dengan `status: invalid`. Kesalahan argumen mencetak petunjuk penggunaan terlokalisasi di stderr. Pembuatan sidik jari yang berhasil hanya mencetak digest. Dalam mode teks, catatan edit usulan mempertahankan nama kolom mesin; penjelasannya diterjemahkan.

Simpan file operasional di direktori privat. Mengalihkan stdout membuat laporan Anda sendiri, yang mungkin memuat nama entitas pengenal dan jalur file. Alat itu sendiri tidak menulis apa pun. Hapus instalasi dengan `python3 -m pip uninstall ha-entity-migrations`. Pemeriksaan pengembang dijelaskan dalam [CONTRIBUTING](../../CONTRIBUTING.md).
