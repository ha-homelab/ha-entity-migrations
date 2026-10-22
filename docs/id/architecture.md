# Arsitektur dan kontrak laporan

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

[Model](model.md) · [Batasan](limitations.md)

![Alur data hanya baca](../diagrams/pipeline.svg)

`io.py` menerapkan batas file/jalur/JSON serta pointer yang tepat. `planner.py` memvalidasi deklarasi, membangun pemetaan sebelum/sesudah, memindai nilai sumber, menyelesaikan kebijakan eksplisit, dan mengumpulkan diagnostik. `cli.py` menambahkan pesan terjemahan dan mencetak laporan. `i18n.py` memuat empat katalog pesan lengkap. Alur ini tidak bergantung pada jaringan atau Home Assistant.

Pemindai sengaja konservatif. String yang persis menyerupai referensi entitas diperiksa terhadap snapshot. String dengan referensi tertanam tetap belum terselesaikan. Template pada kunci atau nilai serta kunci target perangkat/area/label tetap belum terselesaikan meskipun artinya tampak mudah ditebak. Kolom layanan biasa tidak dianggap sebagai ID entitas; layanan dinamis tetap belum terselesaikan. File non-JSON dicatat sebagai sumber yang tidak didukung dan memblokir perencanaan. Ini bukan parser HA serbaguna.

![Alur keputusan kebijakan](../diagrams/policy.svg)

## Pembungkus JSON stabil, versi skema 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Untuk masukan valid, `status` adalah ready atau blocked. `scope` selalu `supplied_files_only`; `read_only` selalu true. Kesalahan masukan memakai pembungkus invalid yang lebih kecil sebagaimana dijelaskan pada instalasi.

Edit memiliki operasi, file, dan pointer. `replace_reference` juga memuat before/after/policy; `replace_service` memuat before/after; `remove_consumer` memuat referensi yang dihentikan. Ini **bukan JSON Patch yang dapat dijalankan**. Semantik transaksi, pergeseran indeks, dan siklus hidup HA tidak disediakan. Tinjau sebagai usulan; rilis ini sengaja tidak menyediakan penerap patch.

Diagnostik memuat `code`, `location`, `severity` yang stabil dan `message` terjemahan. Baik `error` maupun `unresolved` memblokir rencana. Laporan `blocked` dapat berisi kandidat edit untuk referensi yang tidak terdampak, tetapi tidak satu pun merupakan transaksi siap pakai. Model awal kedaluwarsa atau berkonflik meniadakan semua kandidat edit referensi. Penetapan selalu mencerminkan model yang diminta pengguna, bukan perubahan yang telah selesai.

Laporan mengurutkan sumber, penetapan, edit, dan diagnostik agar dapat direproduksi. Tidak ada cap waktu saat ini atau skor keyakinan yang dibuat-buat. Hash byte membuktikan versi masukan yang dianalisis, bukan kebenaran masukan atau apakah perangkat akan mematuhi perintah.
