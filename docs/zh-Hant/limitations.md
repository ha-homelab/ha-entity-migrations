# 限制與審查邊界

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

[架構](architecture.md) · [安全](../../SECURITY.md)

計劃的準確性取決於物理裝置、通道、角色宣告及所提供檔案。工具不會發現遺漏的儀表板、裝置觸發器、場景、藍圖、存於其他位置的自動化、Matter 過濾器、外部客戶端或隱藏整合狀態。不要把就緒報告稱為完整 Home Assistant 審計。此版本要求角色唯一；多對多語義角色和組需要手動拆解。

支援 JSON 配置來源。不解釋 YAML 本身、include、別名、錨點、可執行標籤、自定義元件或執行時生成的模板。規範化不在本版本範圍內，而且可能丟失語義；保留原件並審查等價性。即使受支援的 JSON，也不會對照 Home Assistant 完整配置模式進行檢查。刪除顯式消費者物件可能留下無效父物件；應審查父物件，並在正常預釋出流程中執行 HA 配置檢查器。

能力和允許角色是顯式約束，不是推斷的安全性。工具無法知道以前無害的插座現在接了泵或車庫門驅動器。報告的繼電器狀態不證明觸點或負載行為。不要僅為驗證名稱而執行全屋指令碼或給正在工作的電器斷電重啟。物理除錯屬於獨立、受控流程。

此版本不應用計劃、不重新命名登錄檔實體、不修改唯一 ID、不過載 HA、不重啟控制器、不停用整合，也不回滾變更。返回的操作是建議，不是可執行 JSON Patch。如果人工應用，需取得新快照並在每項已審查變更後驗證，因為索引和版本可能已變化。雜湊不提供簽名或訪問控制。

報告可能含私有名稱和識別符號，不應放進公開 Git、問題跟蹤器或 CI 產物。公開示例使用合成裝置，不聲稱現場驗證。診斷按設計阻止計劃；沒有強制標誌、忽略列表或隱藏寬鬆模式。
