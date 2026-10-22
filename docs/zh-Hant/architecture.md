# 架構與報告契約

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

[模型](model.md) · [限制](limitations.md)

![只讀資料流](../diagrams/pipeline.svg)

`io.py` 強制執行檔案、路徑和 JSON 限制，並處理精確指標。`planner.py` 驗證宣告，構建變更前後對映，掃描源值，解析顯式策略並收集診斷記錄。`cli.py` 新增翻譯後的訊息並輸出報告。`i18n.py` 包含四套完整訊息目錄。此路徑不依賴網路或 Home Assistant。

掃描器刻意採取保守方式。精確的實體引用字串會與快照核對。含嵌入引用的字串仍為未解決狀態。鍵或值中的模板，以及裝置、區域、標籤目標鍵，即使看似容易推斷，也仍為未解決狀態。普通服務欄位不當作實體 ID；動態服務仍為未解決狀態。非 JSON 檔案被登記為不支援的來源並阻止規劃。這不是通用 HA 解析器。

![策略決策流程](../diagrams/policy.svg)

## 穩定的 JSON 外層結構，模式版本 1

`schema_version`、`tool_version`、`status`、`read_only`、`scope`、`snapshot_sha256`、`source_sha256`、`assignments`、`edits`、`diagnostics`、`language`、`summary`。有效輸入的 `status` 為 ready 或 blocked。`scope` 始終為 `supplied_files_only`；`read_only` 始終為 true。輸入錯誤使用安裝指南說明的較小 invalid 外層結構。

編輯項包含操作、檔案和指標。`replace_reference` 還包含 before/after/policy；`replace_service` 包含 before/after；`remove_consumer` 包含要停用的引用。這些**不是可執行的 JSON Patch**，缺少事務、索引移動及 HA 生命週期語義。請將它們視為建議進行審查；此版本有意不提供補丁應用器。

診斷包含穩定的 `code`、`location`、`severity` 以及翻譯後的 `message`。`error` 和 `unresolved` 都會阻止計劃。`blocked` 報告可能包含不受影響引用的候選編輯，但這些都不是可直接執行的事務。過期或衝突的初始模型會抑制全部候選引用編輯。分配項始終回顯使用者請求的模型，不表示已完成的變更。

為便於復現，報告會排序來源、分配、編輯和診斷。沒有當前時間戳或憑空生成的置信分數。位元組雜湊證明分析了哪個輸入版本，不證明輸入真實，也不證明裝置會服從命令。
