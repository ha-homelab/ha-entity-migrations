# 操作示例

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

[輸入模型](model.md) · [架構](architecture.md)

這裡的所有硬體和角色都是合成示例。用 `python3 tools/generate_examples.py` 可重建相同輸入。沒有任何命令會連線 Home Assistant。

## 燈具角色離開改作他用的插座

執行 README 中針對 `examples/role-swap` 的命令。最初 `plug-a/1` 擁有 `light.workbench`，`plug-b/1` 擁有 `switch.spare`。清單把泵角色分配給插座 A，把工作臺角色分配給插座 B。照明自動化使用 `follows_role`，只允許 `workbench`。其實體引用仍為 `light.workbench`，而目標硬體改變。不產生文字編輯是預期結果，並非遺漏遷移。報告的 `assignments` 包含供人工審查的硬體變更。

原來的備用消費者在 `/1` 處停用，即整個第二個自動化物件。因此不會留下空動作序列。報告僅提供建議，程式不會刪除任何 JSON 陣列元素。如果手動應用多項建議的陣列刪除，應考慮索引偏移，並用新快照重新執行。

將第一條策略改為 `follows_hardware`，但允許角色仍保留 `workbench`：計劃將因 `role_not_allowed` 受阻。擴大允許角色列表以包含泵，是顯式且危險的意圖變更，不是清除錯誤的常規方法。應恢復正確策略。

## 繼電器從 light 改為 switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

兩項候選編輯分別更改目標及其 `light.turn_off` 服務。向源動作新增亮度資料，更新已批准的源指紋並重新執行：`service_data_review` 會阻止自動轉換。不要僅為了讓工具透過而刪除亮度設定，應審查期望行為。

## 未解決的模板

使用 `examples/blocked-template` 執行相同命令。目標是動態 Jinja。工具不求值，並返回程式碼 3。完整且受支援的計劃需要顯式配置和可證明的字面量目標；否則應把它保留為已記錄、位於就緒範圍外的手動遷移。忽略退出程式碼無法解決模板。

## 漂移與可重複性

修改來源卻不修改清單雜湊會產生 `stale_source`。修改快照會產生 `stale_snapshot`。這些過期模型不會輸出候選引用編輯。檔案未改變時，除了所選語言，JSON 結果是確定性的。原始檔逐位元組保持不變。

用於真實專案時，將格式複製到私有資料夾，核實物理身份，列出消費者，再執行規劃器。審查全部分配和編輯，在既定部署流程中執行 HA 自身檢查，然後生成新的只讀快照驗證結果。本專案不實現該部署或回滾執行器。
