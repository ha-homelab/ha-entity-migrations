# 入力モデル

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

[インストール](installation.md) · [例](examples.md)

すべての文書はUTF-8の厳密なJSONを使用します。重複キー、非有限数、未知のスキーマフィールドは拒否します。`examples/` の正確な例が実行可能な基準です。バージョンフィールドは整数 `1` であり、文字列や真偽値ではいけません。

## スナップショット

最上位オブジェクトは `version` と `entities` のみを含みます。各エンティティは正確に以下を含みます。

- `entity_id`：小文字のドメイン/オブジェクトID。例は `light.workbench`。
- `hardware_id`：運用者が選ぶ非公開の不透明識別子。
- `channel`：文字列の物理チャンネル識別子。
- `role`：一意の論理目的。例は `workbench` や `pump_enable`。
- `capabilities`：能力を表す重複のない文字列。例は `on_off`。

ハードウェア/チャンネルの組が物理エンドポイントを識別します。エンティティID、物理エンドポイント、論理役割はそれぞれ一意でなければなりません。物理診断は `rssi` など別チャンネルとして、独自の一意な役割を与えます。役割は計画用ラベルであり、Home Assistantのエリア、ラベル、デバイスクラスではありません。宣言は測定ではなく、ツールはハードウェアと照合できません。

## マニフェスト

最上位オブジェクトは正確に `version`、`snapshot_sha256`、`sources`、`assignments`、`consumers` を持ちます。`sources` は相対ファイル名をSHA-256ダイジェストへ対応付けます。`assignments` はスナップショットにすでにある物理エンドポイントの完全な置換エンティティ記録です。列挙されないエンドポイントは不変です。新規デバイスを入れる場合、まず観測済みの予備エンドポイントをスナップショットへ追加してください。ハードウェアの暗黙の作成・削除はなく、このリリースでは役割の一意性が必要です。

各利用側設定は `file` とRFC 6901の `pointer` で**リテラル文字列値**を指定します。`/` は `~1`、`~` は `~0` とエスケープします。リストのインデックスはゼロ始まりで、先頭ゼロを許しません。見つかった各参照に明示的ポリシーが必要です。

- `follows_role`：ソースの論理役割を持つ移行先を探します。
- `follows_hardware`：ソースの物理チャンネルを保ち、新エンティティIDを使います。
- `retire`：参照を含む明示的な `retire_scope` オブジェクトの削除を提案します。

廃止以外の利用側設定には `kind`（`action`、`display`、`reference`）、空でない `allowed_roles`、空でもよい `required_capabilities` も必要です。アクションには `service_pointer` が必要です。これらのゲートは用途変更したポンプを照明対象にすることを防ぎます。宣言であって、推論した意図ではありません。

廃止する利用側設定はfile、pointer、policy、retire_scopeの4フィールドだけを持ちます。スコープはルートではない祖先オブジェクトでなければなりません。同じ廃止ソースへの参照だけを含められ、混在参照や動的参照はブロックします。アクション削除が無効な空列を残す場合は、古いオートメーション全体を選んでください。ツールはHAスキーマ検証器を実行しません。

## ドメイン変更

light/switchをまたぐアクションでは `turn_on`、`turn_off`、`toggle` と一致する `homeassistant.*` サービスのみ対応します。自動サービス変換では空でない `data` や `data_template` を受け付けません。複数のリテラル対象を持つドメイン固有サービスはブロックします。サービスポインターは自分のアクション配下に対象を所有する必要があります。表示のドメイン変更には必ずカード機能の手動レビューが必要です。スイッチが明るさ操作を黙って引き継ぐことはできません。

## 上限

1ファイル2 MiB、ソース合計16 MiB、64ファイル、エンティティ・割り当て・利用側設定は5,000、JSON深さ40、値ノードは1ファイル100,000です。識別子は最大256文字の空でない文字列で、機能/許可役割リストは最大64個の一意な文字列です。相対ソースパスは上位へ遡れず、絶対パスやシンボリックリンクを含められません。入力は通常ファイルのみです。

ファイルローダーは同じ正規パスまたは開いたファイルの同一性（デバイス/inode）へ解決される2つのソース名を拒否します。重複したパス区切り、ハードリンク、大文字小文字を区別しないファイルシステム上の大小文字エイリアスを含みます。ソース名を1つにし利用側設定を更新してください。エイリアスで同一物理ファイルに別々の移行ポリシーを持たせることはできません。同じ内容でも独立ファイルなら有効です。純粋な `plan` APIはファイルシステムにアクセスしません。ソース対応表を自作する呼び出し側は、呼び出す前にこの同一性境界を強制する必要があります。
