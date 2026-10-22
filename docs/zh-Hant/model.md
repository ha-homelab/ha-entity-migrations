# 輸入模型

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

[安裝](installation.md) · [示例](examples.md)

所有文件使用 UTF-8 嚴格 JSON。拒絕重複鍵、非有限數和未知模式欄位。`examples/` 中的精確示例是可執行參考。版本欄位必須是整數 `1`，不能是字串或布林值。

## 快照

頂層物件僅含 `version` 和 `entities`。每個實體精確包含：

- `entity_id`：小寫域/物件 ID，例如 `light.workbench`。
- `hardware_id`：操作員選擇的私有、不透明識別符號。
- `channel`：物理通道識別符號，字串形式。
- `role`：唯一邏輯用途，例如 `workbench` 或 `pump_enable`。
- `capabilities`：描述能力的唯一字串，例如 `on_off`。

硬體/通道對標識物理端點。實體 ID、物理端點、邏輯角色各自必須唯一。物理診斷應表示為另一通道，例如 `rssi`，並賦予獨立的唯一角色。角色是規劃標籤，不是 Home Assistant 區域、標籤或裝置類別。宣告不是測量，工具無法對照硬體驗證。

## 清單

頂層物件精確包含 `version`、`snapshot_sha256`、`sources`、`assignments` 和 `consumers`。`sources` 將相對檔名對映到 SHA-256 摘要。`assignments` 含快照中已有物理端點的完整替換實體記錄。未列出的端點保持不變。加入新裝置前，先把觀察到的備用端點寫入快照。不會隱式建立或刪除硬體，而且此版本要求角色唯一。

每個消費者透過 `file` 和 RFC 6901 `pointer` 標識一個**字面量字串值**。把 `/` 轉義為 `~1`，把 `~` 轉義為 `~0`；列表索引從零開始且不能有前導零。每個發現的引用都需要顯式策略：

- `follows_role`：查詢擁有源邏輯角色的目標。
- `follows_hardware`：保留源物理通道，使用其新實體 ID。
- `retire`：建議移除包含該引用的顯式 `retire_scope` 物件。

非停用消費者還需要 `kind`（`action`、`display`、`reference`）、`allowed_roles`（非空）和 `required_capabilities`（可以為空）。動作需要 `service_pointer`。這些關卡防止把剛改作他用的泵當成照明目標。它們是宣告，不是推斷的意圖。

停用消費者精確包含四個欄位：file、pointer、policy 和 retire_scope。範圍必須是非根祖先物件，只能包含對同一停用來源的引用；混合或動態引用會阻止停用。如果刪除動作會留下無效的空序列，應選擇整個過時自動化。工具不執行 HA 模式驗證器。

## 域變化

跨 light/switch 的動作只支援 `turn_on`、`turn_off`、`toggle` 及匹配的 `homeassistant.*` 服務。自動服務轉換不接受非空 `data` 或 `data_template`。有多個字面量目標的域專用服務會被阻止。服務指標必須在其動作下擁有該目標。顯示域變化始終需要人工審查卡片功能；開關不能悄悄繼承亮度控制元件。

## 邊界

每檔案 2 MiB；原始檔總共 16 MiB；64 個檔案；5,000 個實體、分配或消費者；每檔案 JSON 深度 40、100,000 個值節點。識別符號是最長 256 字元的非空字串，能力/允許角色列表最多含 64 個唯一字串。相對源路徑不能向上穿越、不能為絕對路徑，也不能包含符號連結。輸入僅限常規檔案。

檔案載入器拒絕解析到同一規範路徑或開啟檔案身份（裝置/inode）的兩個來源名稱，包括重複路徑分隔符、硬連結，以及不區分大小寫檔案系統上的大小寫別名。保留一個來源名稱並更新消費者；別名不能為同一物理檔案攜帶不同遷移策略。內容相同的獨立檔案仍是有效輸入。純 `plan` API 不訪問檔案系統；自行構建來源對映的呼叫者必須在呼叫前執行此身份邊界檢查。
