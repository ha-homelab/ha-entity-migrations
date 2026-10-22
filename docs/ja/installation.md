# インストールとCLI

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

[ドキュメント一覧](../../README.md#documentation)

Python 3.11以降を使用します。専用の仮想環境を作成して有効化し、チェックアウトから `python3 -m pip install -e .` を実行します。パッケージに実行時依存はありませんが、pipはビルドバックエンドを取得する場合があります。オフライン環境ではwheelとビルド依存を事前に用意してください。`ha-entity-migrations --version` で選択したインストールを確認できます。インストール済みパッケージのバージョンを表示します。

CLIには2コマンドがあり、グローバル言語オプションはコマンドの前に置きます。

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` は正確なファイルバイトのSHA-256を小文字で出力します。ファイルがJSONとして有効かは検証しません。マニフェスト中のスナップショットとソースの指紋は、空白も含めて対象の正確なファイルと一致する必要があります。予期しないドリフトを消すためだけに指紋を更新せず、先に新しい入力を比較・承認してください。

`plan` はJSONマニフェスト、正規化済みJSONスナップショット、および `--root` を基準として `manifest.sources` に明記したファイルだけを読みます。ディレクトリ再帰やホームの検索は行いません。既定出力はJSONです。`--lang en|ru|de|es` で変わるのは人向けメッセージだけで、フィールド名と診断コードは安定しています。最上位と各コマンドで `--help` を使用できます。適用、アップロード、検出、認証のコマンドはありません。

終了ステータス：

- **0：**対応する入力範囲の内部整合性があり、レビュー可能です。
- **2：**引数や入力が無効、ファイルが読めない、またはスキーマ/制限違反です。
- **3：**構造的には有効な入力が、競合や未解決の範囲によりブロックされた計画を生成しました。

引数解析後の入力失敗は、`status: invalid` を持つJSONエンベロープをstdoutへ出力します。引数エラーはローカライズした使い方をstderrに出します。指紋成功時はダイジェストだけを出力します。テキストモードでも編集提案のフィールド名は機械向けのまま、説明が翻訳されます。

運用ファイルは非公開ディレクトリに置いてください。stdoutをリダイレクトすると自分のレポートが作られ、識別可能なエンティティ名やパスを含むことがあります。ツール自身は何も書き込みません。アンインストールは `python3 -m pip uninstall ha-entity-migrations` です。開発者向けチェックは [CONTRIBUTING](../../CONTRIBUTING.md) を参照してください。
