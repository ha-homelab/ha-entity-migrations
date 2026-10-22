# 詳しい使用例

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

[入力モデル](model.md) · [アーキテクチャ](architecture.md)

ここにあるハードウェアと役割はすべて合成例です。`python3 tools/generate_examples.py` で同じ入力を再生成できます。どのコマンドもHome Assistantに接続しません。

## 用途変更したプラグから照明の役割を移す

`examples/role-swap` 用のREADMEコマンドを実行します。初期状態では `plug-a/1` が `light.workbench` を、`plug-b/1` が `switch.spare` を持ちます。マニフェストはプラグAにポンプの役割、プラグBに作業台の役割を割り当てます。照明オートメーションは `follows_role` を使い、`workbench` だけを許可します。移行先ハードウェアが変わってもエンティティ参照は `light.workbench` のままです。テキスト編集がないことは意図した結果であり、移行漏れではありません。レポートの `assignments` に、人が確認するハードウェア変更が含まれます。

古い予備の利用側設定は `/1`、つまり2番目のオートメーションオブジェクト全体で廃止されます。空のアクション列は残りません。レポートは助言であり、プログラムがJSON配列要素を削除することはありません。複数の配列削除提案を手動適用する場合はインデックスのずれを考慮し、新しいスナップショットから再実行してください。

最初のポリシーを `follows_hardware` に変え、許可する役割を `workbench` のままにすると、計画は `role_not_allowed` でブロックされます。ポンプを含めるよう許可役割リストを広げるのは、明示的で危険な意図変更であって、通常のエラー解消法ではありません。正しいポリシーに戻してください。

## リレーをlightからswitchへ変更する

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

2つの編集提案はターゲットとその `light.turn_off` サービスを変更します。ソースアクションに明るさデータを加え、承認済みソース指紋を更新して再実行すると、`service_data_review` が自動変換をブロックします。ツールを通すためだけに明るさ設定を削除せず、望む動作を確認してください。

## 未解決のテンプレート

`examples/blocked-template` に対して同じコマンドを実行します。ターゲットは動的Jinjaです。ツールは評価せずコード3を返します。完全で対応範囲内の計画には、証明可能なリテラルターゲットを持つ明示的設定が必要です。それ以外は、準備完了範囲外の文書化された手動移行として残してください。終了コードを無視してもテンプレートは解決しません。

## ドリフトと再現性

マニフェストのハッシュを変えずにソースを編集すると `stale_source` が発生します。スナップショットを編集すると `stale_snapshot` が発生します。これらの古いモデルに参照編集候補は出力されません。ファイルが同じなら、選択言語以外のJSON結果は決定的です。ソースファイルはバイト単位で変更されません。

実際のプロジェクトでは形式を非公開フォルダーにコピーし、物理的な識別を確認し、利用側設定を列挙してプランナーを実行します。すべての割り当てと編集をレビューし、既存のデプロイ手順でHA自身のチェックを実行した後、新たな読み取り専用スナップショットで結果を確認します。本プロジェクトはそのデプロイやロールバック実行器を実装しません。
