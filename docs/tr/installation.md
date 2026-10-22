# Kurulum ve CLI

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

[Belge dizini](../../README.md#documentation)

Python 3.11 veya yenisini kullanın. Ayrı sanal ortam oluşturup etkinleştirin, ardından çalışma kopyasında `python3 -m pip install -e .` çalıştırın. Paketin çalışma zamanı bağımlılığı yoktur; pip derleme arka ucunu indirebilir. Çevrimdışı makine için wheel ve derleme bağımlılıklarını önceden hazırlayın. Seçili kurulumu `ha-entity-migrations --version` ile doğrulayın; kurulu paket sürümünü gösterir.

CLI iki komut sunar; genel dil seçeneği komuttan önce gelir:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint`, dosyanın kesin baytlarının SHA-256 değerini küçük harflerle yazdırır. Dosyanın JSON geçerliliğini denetlemez. Manifestteki anlık görüntü ve kaynak parmak izleri boşluklar dahil tam dosyalarla eşleşmelidir. Beklenmedik sapmayı gizlemek için parmak izini yenilemeyin; önce yeni girdiyi karşılaştırıp onaylayın.

`plan`, JSON manifestini, normalleştirilmiş JSON anlık görüntüsünü ve yalnızca `manifest.sources` içinde açıkça belirtilen dosyaları `--root` köküne göre okur. Dizinleri özyinelemeli taramaz veya ev klasörünüzü aramaz. Varsayılan çıktı JSON'dur. `--lang en|ru|de|es` yalnızca insanlara yönelik iletileri değiştirir; alan adları ve tanı kodları kararlı kalır. `--help` üst düzeyde ve her komutta vardır. Uygulama, yükleme, keşif veya kimlik doğrulama komutu yoktur.

Çıkış durumu:

- **0:** desteklenen girdi kapsamı kendi içinde tutarlı ve incelemeye hazırdır.
- **2:** geçersiz argüman/girdi, okunamayan dosya veya şema/sınır ihlali.
- **3:** yapısal olarak geçerli girdi, çakışma ya da çözümlenmemiş kapsam nedeniyle engellenen plan üretmiştir.

Argüman ayrıştırmasından sonraki girdi hataları stdout üzerinde `status: invalid` içeren JSON zarfı üretir. Argüman hataları yerelleştirilmiş kullanım bilgisini stderr'e yazar. Başarılı parmak izi işlemi yalnızca özeti yazdırır. Metin modunda önerilen düzenlemeler makine alan adlarını korur; açıklamalar çevrilir.

İşletim dosyalarını özel dizinde saklayın. Stdout'u yönlendirmek kendi raporunuzu oluşturur; rapor tanımlayıcı varlık adları ve dosya yolları içerebilir. Araç kendisi hiçbir şey yazmaz. `python3 -m pip uninstall ha-entity-migrations` ile kaldırın. Geliştirici kontrolleri için [CONTRIBUTING](../../CONTRIBUTING.md) belgesine bakın.
