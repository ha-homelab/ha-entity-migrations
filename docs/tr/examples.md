# Açıklamalı örnekler

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

[Girdi modeli](model.md) · [Mimari](architecture.md)

Buradaki donanım ve rollerin tamamı sentetiktir. Aynı girdileri `python3 tools/generate_examples.py` ile yeniden oluşturun. Hiçbir komut Home Assistant'a bağlanmaz.

## Lamba rolü, başka amaçla kullanılan prizden ayrılır

`examples/role-swap` için README komutunu çalıştırın. Başlangıçta `plug-a/1`, `light.workbench` varlığına; `plug-b/1` ise `switch.spare` varlığına sahiptir. Manifest pompa rolünü A prizine, tezgâh rolünü B prizine atar. Aydınlatma otomasyonu `follows_role` kullanır ve yalnızca `workbench` rolüne izin verir. Hedef donanım değişirken varlık başvurusu `light.workbench` kalır. Metin düzenlemesi olmaması amaçlanan sonuçtur, atlanan bir geçiş değildir. Rapordaki `assignments`, insan incelemesi için donanım değişikliklerini içerir.

Eski yedek tüketici `/1` konumunda, ikinci otomasyon nesnesinin tamamı olarak kaldırılır. Böylece boş bir eylem dizisi kalmaz. Rapor tavsiye niteliğindedir; program JSON dizisinden öğe silmez. Birkaç önerilen dizi silmesini elle uyguluyorsanız kaymış indisleri hesaba katıp yeni anlık görüntüyle yeniden çalıştırın.

İzin verilen rolü `workbench` bırakarak ilk politikayı `follows_hardware` yapın: plan `role_not_allowed` ile engellenir. İzin listesini pompayı kapsayacak şekilde genişletmek açık ve tehlikeli bir niyet değişikliğidir; sıradan hata giderme yöntemi değildir. Doğru politikayı geri yükleyin.

## Röle light alanından switch alanına geçer

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

İki önerilen düzenleme hedefi ve onun `light.turn_off` hizmetini değiştirir. Kaynak eyleme parlaklık verisi ekleyin, onaylı kaynak parmak izini güncelleyin ve yeniden çalıştırın: `service_data_review` otomatik dönüşümü engeller. Yalnızca aracı memnun etmek için parlaklık ayarlarını silmeyin; istenen davranışı değerlendirin.

## Çözümlenmemiş şablon

Aynı komutu `examples/blocked-template` ile çalıştırın. Hedef dinamik Jinja'dır. Araç bunu değerlendirmez ve kod 3 döndürür. Tam desteklenen plan, kanıtlanabilir sabit hedeflerle açık yapılandırma gerektirir; aksi durumda bunu hazır kapsamın dışında belgelenmiş elle geçiş olarak tutun. Çıkış kodunu yok saymak şablonu çözmez.

## Sapma ve tekrarlanabilirlik

Kaynağı manifest karmasını değiştirmeden düzenlemek `stale_source` üretir. Anlık görüntüyü düzenlemek `stale_snapshot` üretir. Bu eski modeller için aday başvuru düzenlemeleri üretilmez. Değişmeyen dosyalarda JSON sonucu seçilen dil dışında belirlenimlidir. Kaynak dosyalar bayt bayt aynı kalır.

Gerçek projede biçimi özel klasöre kopyalayın, fiziksel kimlikleri doğrulayın, tüketicileri listeleyin ve planlayıcıyı çalıştırın. Bütün atamaları ve düzenlemeleri inceleyin, yerleşik dağıtım sürecinizde HA'nın kendi kontrollerini yapın, ardından sonucu doğrulamak için yeni salt okunur anlık görüntü alın. Proje bu dağıtımı veya geri alma çalıştırıcısını uygulamaz.
