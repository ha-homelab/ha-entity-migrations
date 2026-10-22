# トラブルシューティング

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

[インストール](installation.md) · [制限](limitations.md)

**コマンドが見つからない：**インストールしたときと同じ仮想環境を有効化します。`python3 -m ha_entity_migrations --version` を試してください。パス不一致を回避するだけのためにシステムPythonへインストールしないでください。

**終了2、schema_invalid：**実行可能な例と[入力モデル](model.md)にキーを照合します。未知のフィールドはエラーです。バージョンは整数1、チャンネル識別子は文字列です。各アクションポリシーにはサービスポインターが必要です。スナップショットはエンティティを、マニフェストは割り当てと利用側設定を持ちます。入れ替え可能なファイルではありません。

**終了2、duplicate_source：**2つのソース名が同じ物理ファイルを示しています。`sources` に正規名を1つ残し、全利用側設定の `file` フィールドを更新します。重複区切りやハードリンク/大小文字エイリアスを除き、エイリアスに2つ目のポリシーを与えないでください。内容が同じでも別ファイルなら対応します。

**stale_snapshot / stale_source：**実際の変更を承認済みソースと比較します。レビュー後にだけ指紋コマンドを使用します。空白の変更もハッシュに影響します。古いハッシュを通すためだけに古いコピーを参照しないでください。

**source_collision / destination_collision：**物理チャンネル、役割、エンティティIDのいずれかが重複しています。役割交換の両側を明記し、未変更エンドポイントが希望する移行先IDを保持していないか確認します。

**role_not_allowed / capability_missing：**利用側設定が不適切な負荷へ到達するか、機能を失います。役割とハードウェアのどちらに追従すべきか確認します。allowed_rolesを自動で広げたり、ハードウェアにない機能を宣言したりしないでください。オン/オフリレーに置換された照明は調光できません。

**missing_policy / unmodeled_reference：**参照先エンドポイントを一覧化し、目的を確認した後でだけ明示的な利用側宣言を追加します。古い履歴文字列は稼働範囲外かもしれません。その場合は意図的にファイルを計画範囲から外し、除外を記録してソース契約を再生成します。

**dynamic_reference / embedded_reference / indirect_target：**本リリースは対応関係を証明できません。Jinjaやグループ/エリア/ラベルの動作を別途レビューするか、明示的で正規化されたリテラル設定を提供します。プログラムはテンプレートを実行しません。

**display_domain_review / service_data_review / mixed_action_targets：**カード機能、アクション引数、対象のまとまりを確認します。複数ドメインのアクションは別途レビューするソース変更で分割し、サービスドメインだけを変えないでください。

**retire_scope_mixed / overlapping_edits：**無関係な参照を含まない、一貫した古い利用側オブジェクトを選びます。アクションからentity_idだけを削除しないでください。広すぎる対象や無効な設定になり得ます。本プログラムは自動廃止を適用しません。

**unsupported_source：**計画できるのはJSONだけです。YAML、バイナリー、その他のファイルを黙ってスキップしません。明示的に正規化したJSONコピーは分析に役立つ場合がありますが、実際に編集する前に原本と比較する必要があります。

不具合は最小限の合成入力、ツール/Pythonのバージョン、終了コード、診断コードを使って報告してください。未加工の家庭環境エクスポートやAPI認証情報は絶対に添付しないでください。
