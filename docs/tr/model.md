# Girdi modeli

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

[Kurulum](installation.md) · [Örnekler](examples.md)

Bütün belgeler katı UTF-8 JSON kullanır. Yinelenen anahtarlar, sonlu olmayan sayılar ve bilinmeyen şema alanları reddedilir. `examples/` içindeki kesin örnekler çalıştırılabilir referanstır. Sürüm alanı metin veya boolean değil, `1` tamsayısı olmalıdır.

## Anlık görüntü

Üst nesne yalnızca `version` ve `entities` içerir. Her varlık tam olarak şunları içerir:

- `entity_id`: `light.workbench` gibi küçük harfli alan/nesne kimliği.
- `hardware_id`: operatörün seçtiği özel, opak tanımlayıcı.
- `channel`: metin biçiminde fiziksel kanal tanımlayıcısı.
- `role`: `workbench` veya `pump_enable` gibi benzersiz mantıksal amaç.
- `capabilities`: `on_off` gibi yetenekleri belirten benzersiz dizeler.

Donanım/kanal çifti fiziksel uç noktayı tanımlar. Varlık kimlikleri, fiziksel uç noktalar ve mantıksal roller ayrı ayrı benzersiz olmalıdır. Fiziksel tanı verisini örneğin `rssi` gibi, kendi benzersiz rolü olan ayrı bir kanal olarak temsil edin. Rol bir planlama etiketidir; HA alanı, etiketi veya cihaz sınıfı değildir. Bu bildirimler ölçüm değildir; araç donanımla karşılaştırarak doğrulayamaz.

## Manifest

Üst nesnede tam olarak `version`, `snapshot_sha256`, `sources`, `assignments` ve `consumers` bulunur. `sources` göreli dosya adlarını SHA-256 özetleriyle eşler. `assignments`, anlık görüntüde zaten bulunan fiziksel uç noktaların tam yedek varlık kayıtlarını içerir. Listelenmeyen uç noktalar değişmez. Yeni cihaz için önce gözlemlenen yedek uç noktasını anlık görüntüye ekleyin. Örtük donanım oluşturma veya silme yoktur; bu sürüm benzersiz roller gerektirir.

Her tüketici bir **sabit dize değerini** `file` ve RFC 6901 `pointer` ile tanımlar. `/` karakterini `~1`, `~` karakterini `~0` olarak kaçırın; liste indisleri sıfır tabanlıdır ve başta sıfır içermez. Bulunan her başvuru açık politika gerektirir:

- `follows_role`: kaynağın mantıksal rolüne sahip hedefi bulur.
- `follows_hardware`: kaynak fiziksel kanalı koruyup yeni varlık kimliğini kullanır.
- `retire`: başvuruyu içeren açık `retire_scope` nesnesinin kaldırılmasını önerir.

Kaldırılmayan tüketiciler ayrıca `kind` (`action`, `display`, `reference`), `allowed_roles` (boş olmayan) ve `required_capabilities` (boş olabilir) gerektirir. Eylemler `service_pointer` gerektirir. Bu sınırlar yeniden amaçlandırılan pompanın aydınlatma hedefi olmasını önler. Bunlar bildirimdir, niyet çıkarımı değildir.

Kaldırılan tüketiciler tam dört alan içerir: file, pointer, policy ve retire_scope. Kapsam, kök olmayan bir üst nesne olmalıdır. Yalnızca aynı kaldırılan kaynağa başvurular içerebilir; karma veya dinamik başvurular onu engeller. Bir eylemi kaldırmak geçersiz boş dizi bırakacaksa eski otomasyonun tamamını seçin. Araç HA şema doğrulayıcısını çalıştırmaz.

## Alan değişiklikleri

Light/switch arasında geçen eylemlerde yalnızca `turn_on`, `turn_off`, `toggle` ve eşleşen `homeassistant.*` hizmetleri desteklenir. Otomatik hizmet dönüşümünde boş olmayan `data` veya `data_template` kabul edilmez. Birden fazla sabit hedefi olan alana özgü hizmet engellenir. Hizmet işaretçisi hedefe kendi eylemi altında sahip olmalıdır. Görüntüleme alanı değişiklikleri her zaman kart özelliklerinin elle incelenmesini gerektirir; anahtar parlaklık kontrollerini sessizce devralamaz.

## Sınırlar

Dosya başına 2 MiB; kaynak dosyalar toplamı 16 MiB; 64 dosya; 5.000 varlık, atama veya tüketici; dosya başına JSON derinliği 40 ve 100.000 değer düğümü. Tanımlayıcılar en fazla 256 karakterlik boş olmayan dizelerdir; yetenek/izinli rol listeleri en fazla 64 benzersiz dize içerir. Göreli kaynak yolları yukarı çıkamaz, mutlak olamaz veya sembolik bağ içeremez. Girdiler yalnızca normal dosyalardır.

Dosya yükleyici, aynı kanonik yola veya açık dosya kimliğine (cihaz/inode) çözümlenen iki kaynak adını reddeder. Yinelenen yol ayırıcıları, sabit bağlar ve büyük/küçük harfe duyarsız sistemlerde harf takma adları buna dahildir. Tek kaynak adını tutup tüketicilerini güncelleyin; takma adlar aynı fiziksel dosyaya farklı geçiş politikaları veremez. İçeriği aynı olan bağımsız dosyalar geçerli kalır. Saf `plan` API'si dosya sistemine erişmez: kaynak eşlemesini kendisi kuran çağırıcılar çağrı öncesinde bu kimlik sınırını uygulamalıdır.
