# 制限とレビュー境界

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

[アーキテクチャ](architecture.md) · [セキュリティ](../../SECURITY.md)

計画の正確さは、物理機器・チャンネル・役割の宣言と提供したファイルに依存します。本ツールは省略されたダッシュボード、デバイストリガー、シーン、ブループリント、別の場所のオートメーション、Matterフィルター、外部クライアント、隠れた連携状態を検出しません。準備完了のレポートを完全なHome Assistant監査と呼ばないでください。このリリースでは役割は一意です。多対多の意味的役割やグループは手動で分解する必要があります。

JSON設定ソースに対応しています。YAML自体、include、エイリアス、アンカー、実行可能タグ、カスタムコンポーネント、実行時生成テンプレートは解釈しません。正規化は本リリースの範囲外で、意味を失う場合があります。原本を保持し、同等性を確認してください。対応JSONでも、Home Assistantの完全な設定スキーマとの照合はしません。明示的な利用側オブジェクトの削除が、無効な親を残す場合があります。親をレビューし、通常のステージング手順でHA設定チェックを実行してください。

機能と許可役割は明示的制約であり、推論された安全性ではありません。かつて無害だったコンセントにポンプやガレージ駆動装置が接続されたことをツールは知りません。報告されたリレー状態は接点や負荷の動作を証明しません。名前確認のためだけに全館スクリプトを実行したり、稼働中の機器を電源再投入したりしないでください。実機の試運転は別の管理された手順で行います。

このリリースは計画適用、レジストリエンティティ改名、一意ID変更、HA再読み込み、コントローラー再起動、連携廃止、変更のロールバックを行いません。返す操作は助言で、実行可能なJSON Patchではありません。手動適用するなら新しいスナップショットを取得し、レビューした各変更後に確認してください。インデックスやバージョンが変わっている可能性があります。ハッシュは署名やアクセス制御を提供しません。

レポートは非公開の名前や識別子を含む場合があります。公開Git、課題管理、CI成果物に入れないでください。公開例は合成デバイスを使い、現場検証を主張しません。診断は設計どおり計画をブロックします。強制フラグ、無視リスト、隠れた寛容モードはありません。
