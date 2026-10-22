# 故障排查

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

[安裝](installation.md) · [限制](limitations.md)

**找不到命令：**啟用安裝時使用的同一個虛擬環境。嘗試 `python3 -m ha_entity_migrations --version`；不要只為繞過路徑不匹配而安裝到系統 Python。

**退出 2，schema_invalid：**對照可執行示例及[輸入模型](model.md)檢查鍵。未知欄位是錯誤。版本為整數 1；通道識別符號為字串。每條動作策略都需要服務指標。快照包含實體，清單包含分配和消費者，兩者不可互換。

**退出 2，duplicate_source：**兩個來源名稱標識同一物理檔案。在 `sources` 中保留一個規範名稱，並讓全部消費者的 `file` 欄位指向它。去掉重複分隔符或硬連結/大小寫別名；不要給別名第二條策略。內容相同的獨立檔案仍受支援。

**stale_snapshot / stale_source：**將實際變化與批准的來源比較。只有審查後才能使用指紋命令。空白變化也影響雜湊。不要只為匹配舊雜湊而指向過期副本。

**source_collision / destination_collision：**物理通道、角色或實體 ID 重複。顯式表達角色互換的雙方，並檢查未變化端點是否仍保留期望的目標 ID。

**role_not_allowed / capability_missing：**消費者將指向不合適的負載或失去能力。確認應跟隨角色還是硬體。不要自動擴大 allowed_roles，也不要聲稱硬體具有實際上不存在的能力。燈具換成開關繼電器後無法調光。

**missing_policy / unmodeled_reference：**盤點被引用端點，確認用途後再新增顯式消費者宣告。舊歷史字串可能不在活動範圍；應有意從計劃範圍移除該檔案、記錄排除，並重新生成來源契約。

**dynamic_reference / embedded_reference / indirect_target：**此版本無法證明對映。單獨審查 Jinja 或組/區域/標籤行為，或提供顯式、規範化的字面量配置。程式從不執行模板。

**display_domain_review / service_data_review / mixed_action_targets：**檢查卡片功能、動作引數和目標批次。應在另行審查的來源修改中拆分跨域動作，不要只改變服務域。

**retire_scope_mixed / overlapping_edits：**選擇一致且過時的消費者物件，不能有無關引用。不要僅刪除動作中的 entity_id，這可能產生過寬目標或無效配置。程式不會自動應用停用。

**unsupported_source：**只能規劃 JSON。YAML、二進位制及其他檔案不會被悄悄跳過。顯式規範化的 JSON 副本可能有助於分析，但任何真實編輯前必須與原件比較。

報告問題時使用最小合成輸入、工具/Python 版本、退出程式碼和診斷程式碼。絕不附上原始家庭匯出或 API 憑據。
