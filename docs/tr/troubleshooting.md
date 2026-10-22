# Sorun giderme

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

[Kurulum](installation.md) · [Sınırlamalar](limitations.md)

**Komut bulunamadı:** kurulumda kullanılan sanal ortamı etkinleştirin. `python3 -m ha_entity_migrations --version` deneyin; yalnızca yol uyuşmazlığını aşmak için sistem Python'una kurmayın.

**Çıkış 2, schema_invalid:** anahtarları çalıştırılabilir örnek ve [girdi modeli](model.md) ile karşılaştırın. Bilinmeyen alanlar hatadır. Sürümler tamsayı 1, kanal tanımlayıcıları metindir. Her eylem politikası hizmet işaretçisi gerektirir. Anlık görüntü varlıkları, manifest atama ve tüketicileri içerir. Dosyalar birbirinin yerine geçmez.

**Çıkış 2, duplicate_source:** iki kaynak adı tek fiziksel dosyayı tanımlar. `sources` içinde tek kanonik ad tutun ve bütün tüketici `file` alanlarını güncelleyin. Yinelenen ayırıcıları veya sabit bağ/harf takma adlarını kaldırın; takma ada ikinci politika vermeyin. Aynı içerikli ayrı dosyalar desteklenmeye devam eder.

**stale_snapshot / stale_source:** gerçek değişiklikleri onaylı kaynakla karşılaştırın. Fingerprint komutunu ancak incelemeden sonra kullanın. Boşluk değişiklikleri karmayı etkiler. Eski karma geçsin diye eski kopyaya yönelmeyin.

**source_collision / destination_collision:** fiziksel kanal, rol veya varlık kimliği yinelenmiştir. Rol değişiminin iki tarafını açıkça belirtin ve değişmeyen uç noktanın istenen hedef kimliğini tutmadığını kontrol edin.

**role_not_allowed / capability_missing:** tüketici uygunsuz yüke ulaşacak veya yetenek kaybedecektir. Rolü mü donanımı mı izlemesi gerektiğini doğrulayın. Allowed_roles listesini otomatik genişletmeyin veya donanımın sahip olmadığı yetenekleri bildirmeyin. Aç/kapat rölesiyle değiştirilen ışık kısma sağlayamaz.

**missing_policy / unmodeled_reference:** başvurulan uç noktayı envantere alın ve amacını doğruladıktan sonra açık tüketici bildirimi ekleyin. Eski geçmiş dizesi etkin kapsamın dışında olabilir; dosyayı bilinçli olarak kapsamdan çıkarın, dışlamayı belgeleyin ve kaynak sözleşmesini yeniden üretin.

**dynamic_reference / embedded_reference / indirect_target:** bu sürüm eşlemeyi kanıtlayamaz. Jinja veya grup/alan/etiket davranışını ayrı inceleyin ya da açık normalleştirilmiş sabit yapılandırma sağlayın. Program hiçbir zaman şablon çalıştırmaz.

**display_domain_review / service_data_review / mixed_action_targets:** kart özelliklerini, eylem parametrelerini ve hedef gruplarını inceleyin. Çok alanlı eylemi ayrı incelenen kaynak değişikliğiyle bölün; yalnızca hizmet alanını değiştirmeyin.

**retire_scope_mixed / overlapping_edits:** ilgisiz başvurular içermeyen tutarlı eski tüketici nesnesi seçin. Eylemden yalnızca entity_id silmeyin: geniş hedef veya geçersiz yapılandırma oluşabilir. Program otomatik kaldırma uygulamaz.

**unsupported_source:** yalnızca JSON planlanabilir. YAML, ikili ve diğer dosyalar sessizce atlanmaz. Açıkça normalleştirilmiş JSON kopyası incelemeye yardım edebilir, ancak gerçek düzenleme öncesinde özgün dosyayla karşılaştırılmalıdır.

Hata bildirirken en küçük sentetik girdiyi, araç/Python sürümünü, çıkış kodunu ve tanı kodlarını kullanın. Ham ev dışa aktarımını veya API kimlik bilgilerini asla eklemeyin.
