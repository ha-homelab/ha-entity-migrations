# Mimari ve rapor sözleşmesi

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

[Model](model.md) · [Sınırlamalar](limitations.md)

![Salt okunur veri akışı](../diagrams/pipeline.svg)

`io.py` dosya/yol/JSON sınırlarını ve kesin işaretçileri uygular. `planner.py` bildirimleri doğrular, önce/sonra eşlemelerini kurar, kaynak değerleri tarar, açık politikaları çözümler ve tanı kayıtlarını toplar. `cli.py` çevrilmiş iletileri ekleyip raporu yazdırır. `i18n.py` dört eksiksiz ileti kataloğu içerir. Bu yolun ağ veya Home Assistant bağımlılığı yoktur.

Tarayıcı bilerek temkinlidir. Tam varlık başvurusu biçimindeki dizeler anlık görüntüyle karşılaştırılır. Gömülü başvurular içeren dizeler çözümlenmemiş kalır. Anahtar veya değerlerdeki şablonlar ve cihaz/alan/etiket hedef anahtarları, anlamları kolay tahmin edilebilir görünse bile çözümlenmez. Basit hizmet alanları varlık kimliği sayılmaz; dinamik hizmetler yine çözümlenmemiştir. JSON olmayan dosyalar desteklenmeyen kaynak olarak kaydedilir ve planlamayı engeller. Bu genel amaçlı bir HA ayrıştırıcısı değildir.

![Politika karar akışı](../diagrams/policy.svg)

## Kararlı JSON zarfı, şema sürümü 1

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Geçerli girdilerde `status` ready veya blocked olur. `scope` her zaman `supplied_files_only`, `read_only` her zaman true olur. Girdi hataları kurulumda anlatılan daha küçük invalid zarfını kullanır.

Düzenlemeler işlem, dosya ve işaretçi içerir. `replace_reference` ayrıca before/after/policy; `replace_service` before/after; `remove_consumer` kaldırılan başvuruyu içerir. Bunlar **çalıştırılabilir JSON Patch değildir**. İşlem bütünlüğü, indis kayması ve HA yaşam döngüsü anlamları yoktur. Öneri olarak inceleyin; bu sürüm bilerek yama uygulayıcı sunmaz.

Tanılar kararlı `code`, `location`, `severity` ve çevrilmiş `message` içerir. Hem `error` hem `unresolved` planı engeller. `blocked` raporları etkilenmeyen başvurular için aday düzenlemeler içerebilir, ancak hiçbiri hazır bir işlem oluşturmaz. Eski veya çelişkili başlangıç modelleri tüm aday başvuru düzenlemelerini bastırır. Atamalar her zaman kullanıcının istediği modeli yansıtır, tamamlanmış değişiklikleri değil.

Raporlar yeniden üretilebilirlik için kaynakları, atamaları, düzenlemeleri ve tanıları sıralar. Güncel zaman damgaları veya uydurma güven puanları bulunmaz. Bayt karmaları hangi girdi sürümünün incelendiğini kanıtlar; girdinin doğru olduğunu ya da cihazın komuta uyacağını kanıtlamaz.
