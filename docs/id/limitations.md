# Batasan dan batas tinjauan

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

[Arsitektur](architecture.md) · [Keamanan](../../SECURITY.md)

Akurasi rencana hanya sebatas deklarasi fisik/kanal/peran dan file yang diberikan. Alat tidak menemukan dashboard yang terlewat, pemicu perangkat, scene, blueprint, otomasi di tempat lain, filter Matter, klien eksternal, atau status integrasi tersembunyi. Jangan menyebut laporan siap sebagai audit Home Assistant lengkap. Setiap peran unik dalam rilis ini; peran semantis banyak-ke-banyak dan grup memerlukan penguraian manual.

Sumber konfigurasi JSON didukung. YAML, include, alias, anchor, tag yang dapat dieksekusi, komponen khusus, dan template yang dihasilkan saat runtime tidak ditafsirkan. Normalisasi berada di luar rilis ini dan bisa menghilangkan semantik; simpan dokumen asli dan tinjau kesetaraan. Bahkan JSON yang didukung tidak diperiksa terhadap skema konfigurasi HA lengkap. Menghapus objek konsumen eksplisit dapat menyisakan induk yang tidak valid; tinjau induknya dan jalankan pemeriksa konfigurasi HA dalam proses staging biasa.

Kapabilitas dan peran yang diizinkan adalah batasan eksplisit, bukan keamanan hasil inferensi. Alat tidak bisa mengetahui pompa atau penggerak garasi telah dipasang pada stopkontak yang sebelumnya aman. Status relai yang dilaporkan tidak membuktikan perilaku kontak/beban. Jangan menjalankan skrip seluruh rumah atau memutus lalu menyalakan listrik perangkat aktif hanya untuk memvalidasi nama. Komisioning fisik memerlukan prosedur terkendali tersendiri.

Rilis ini tidak menerapkan rencana, mengganti nama entitas registri, mengubah ID unik, memuat ulang HA, memulai ulang pengontrol, menghentikan integrasi, atau mengembalikan perubahan. Operasi yang dikembalikan bersifat saran, bukan JSON Patch yang dapat dieksekusi. Jika diterapkan manual, ambil snapshot baru dan verifikasi setelah setiap perubahan yang ditinjau; indeks dan versi mungkin berubah. Hash tidak menyediakan tanda tangan atau kontrol akses.

Laporan dapat memuat nama dan pengenal privat. Jangan memasukkannya ke Git publik, pelacak issue, atau artefak CI. Contoh publik memakai perangkat sintetis dan tidak mengklaim validasi lapangan. Diagnostik sengaja memblokir rencana; tidak ada flag pemaksaan, daftar pengabaian, atau mode permisif tersembunyi.
