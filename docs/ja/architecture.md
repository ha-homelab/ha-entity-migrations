# アーキテクチャとレポートの契約

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

[モデル](model.md) · [制限](limitations.md)

![読み取り専用のデータフロー](../diagrams/pipeline.svg)

`io.py` はファイル、パス、JSONの制限と正確なポインターを強制します。`planner.py` は宣言を検証し、変更前後の対応表を作り、ソース値を走査し、明示的なポリシーを解決して診断記録を蓄積します。`cli.py` は翻訳済みメッセージを加えてレポートを出力します。`i18n.py` は4つの完全なメッセージカタログを含みます。この経路はネットワークにもHome Assistantにも依存しません。

スキャナーは意図的に保守的です。エンティティ参照と厳密に一致する文字列をスナップショットと照合します。参照が埋め込まれた文字列は未解決です。キーや値のテンプレート、およびデバイス・エリア・ラベルのターゲットキーは、容易に推測できそうでも未解決です。通常のサービスフィールドはエンティティIDとして扱いませんが、動的サービスは未解決のままです。JSON以外のファイルは非対応ソースとして登録され、計画をブロックします。これは汎用HAパーサーではありません。

![ポリシーの判断フロー](../diagrams/policy.svg)

## 安定したJSONエンベロープ、スキーマバージョン1

`schema_version`、`tool_version`、`status`、`read_only`、`scope`、`snapshot_sha256`、`source_sha256`、`assignments`、`edits`、`diagnostics`、`language`、`summary`。有効な入力では `status` はreadyまたはblockedです。`scope` は常に `supplied_files_only`、`read_only` は常にtrueです。入力エラーはインストールガイドで説明する小さなinvalidエンベロープを使用します。

編集には操作、ファイル、ポインターがあります。`replace_reference` はbefore/after/policyも含み、`replace_service` はbefore/after、`remove_consumer` は廃止対象の参照を含みます。これらは**実行可能なJSON Patchではありません**。トランザクション、インデックス移動、HAライフサイクルの意味論がありません。提案としてレビューしてください。このリリースは意図的にパッチ適用器を提供しません。

診断は安定した `code`、`location`、`severity` と翻訳済み `message` を含みます。`error` と `unresolved` はどちらも計画をブロックします。`blocked` レポートに影響のない参照への編集候補があっても、そのいずれも実行準備済みトランザクションではありません。古い、または競合した初期モデルはすべての参照編集候補を抑止します。割り当ては常にユーザーの要求モデルを再掲し、完了済み変更を示しません。

再現性のため、レポートはソース、割り当て、編集、診断をソートします。現在時刻や架空の確信度はありません。バイトハッシュが証明するのは分析した入力バージョンであり、入力の真実性やデバイスが命令に従うことではありません。
