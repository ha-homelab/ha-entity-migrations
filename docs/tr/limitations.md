# Sınırlamalar ve inceleme sınırı

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

[Mimari](architecture.md) · [Güvenlik](../../SECURITY.md)

Planın doğruluğu fiziksel/kanal/rol bildirimleri ve verilen dosyalarla sınırlıdır. Araç atlanmış panoları, cihaz tetikleyicilerini, sahneleri, blueprint'leri, başka yerde tutulan otomasyonları, Matter filtrelerini, harici istemcileri veya gizli entegrasyon durumlarını keşfetmez. Hazır raporu tam Home Assistant denetimi olarak adlandırmayın. Bu sürümde her rol benzersizdir; çoktan çoğa anlamsal roller ve gruplar elle ayrıştırılmalıdır.

JSON yapılandırma kaynakları desteklenir. YAML, eklemeler, takma adlar, çapalar, çalıştırılabilir etiketler, özel bileşenler ve çalışma zamanında üretilen şablonlar yorumlanmaz. Normalleştirme bu sürümün dışındadır ve anlam kaybına neden olabilir; özgün dosyayı koruyup eşdeğerliği inceleyin. Desteklenen JSON bile HA'nın tam yapılandırma şemasına göre denetlenmez. Açık bir tüketici nesnesinin kaldırılması üst nesneyi geçersiz bırakabilir; üst nesneyi inceleyin ve normal hazırlık sürecinde HA yapılandırma denetleyicisini çalıştırın.

Yetenekler ve izin verilen roller açık kısıtlardır, çıkarımla elde edilen güvenlik değildir. Araç, önceden zararsız bir prize pompa veya garaj motoru bağlandığını bilemez. Bildirilen röle durumu kontak/yük davranışını kanıtlamaz. Yalnızca adları doğrulamak için tüm evi etkileyen betikler çalıştırmayın veya çalışan cihazın elektriğini kesip açmayın. Fiziksel devreye alma ayrı ve kontrollü bir prosedürdür.

Bu sürüm plan uygulamaz, kayıt defteri varlığını yeniden adlandırmaz, benzersiz kimliği değiştirmez, HA'yı yeniden yüklemez, denetleyiciyi yeniden başlatmaz, entegrasyonu kaldırmaz veya değişikliği geri almaz. Döndürülen işlemler tavsiye niteliğindedir; çalıştırılabilir JSON Patch değildir. Elle uygulanacaksa yeni anlık görüntü alın ve incelenen her değişiklikten sonra doğrulayın; indisler ve sürümler değişmiş olabilir. Karmalar imza veya erişim kontrolü sağlamaz.

Raporlar özel ad ve kimlikler içerebilir. Bunları herkese açık Git'e, sorun takip sistemlerine veya CI çıktısına koymayın. Genel örnekler sentetik cihaz kullanır ve saha doğrulaması iddiasında bulunmaz. Tanılar tasarım gereği planı engeller; zorlama bayrağı, yok sayma listesi veya gizli izin verici mod bulunmaz.
