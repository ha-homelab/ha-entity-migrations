# 安裝與 CLI

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

[文件索引](../../README.md#documentation)

使用 Python 3.11 或更新版本。建立並啟用專用虛擬環境，然後在檢出目錄執行 `python3 -m pip install -e .`。包沒有執行時依賴；pip 可能會獲取構建後端。離線機器應提前準備 wheel 和構建依賴。用 `ha-entity-migrations --version` 驗證所選安裝，它報告已安裝的包版本。

CLI 有兩個命令，全域性語言選項放在命令之前：

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` 輸出精確檔案位元組的小寫 SHA-256，不驗證檔案是否為 JSON。清單中的快照和源指紋必須與那些精確檔案匹配，包括空白。不要只為消除意外漂移而更新指紋；先比較並批准新輸入。

`plan` 讀取 JSON 清單、規範化 JSON 快照，以及相對於 `--root`、在 `manifest.sources` 中明確列出的檔案。它不遞迴目錄，也不搜尋主目錄。預設輸出為 JSON。`--lang en|ru|de|es` 僅改變人類可讀訊息；欄位名和診斷程式碼保持穩定。頂層和每個命令都支援 `--help`。沒有應用、上傳、發現或認證命令。

退出狀態：

- **0：**受支援的輸入範圍內部一致，可供審查。
- **2：**引數或輸入無效、檔案不可讀，或違反模式/限制。
- **3：**結構有效的輸入生成受阻計劃，例如衝突或範圍未解決。

引數解析之後的輸入失敗會在 stdout 輸出帶 `status: invalid` 的 JSON 外層結構。引數錯誤會在 stderr 輸出本地化用法。指紋成功時只輸出摘要。文字模式下，候選編輯記錄保留機器欄位名，解釋訊息會翻譯。

執行檔案應儲存在私有目錄。重定向 stdout 會建立自己的報告，其中可能包含可識別的實體名和路徑。工具自身不寫任何內容。用 `python3 -m pip uninstall ha-entity-migrations` 解除安裝。開發者檢查見 [CONTRIBUTING](../../CONTRIBUTING.md)。
