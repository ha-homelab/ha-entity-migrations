# 安装与 CLI

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

[文档索引](../../README.md#documentation)

使用 Python 3.11 或更新版本。创建并激活专用虚拟环境，然后在检出目录运行 `python3 -m pip install -e .`。包没有运行时依赖；pip 可能会获取构建后端。离线机器应提前准备 wheel 和构建依赖。用 `ha-entity-migrations --version` 验证所选安装，它报告已安装的包版本。

CLI 有两个命令，全局语言选项放在命令之前：

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` 输出精确文件字节的小写 SHA-256，不验证文件是否为 JSON。清单中的快照和源指纹必须与那些精确文件匹配，包括空白。不要只为消除意外漂移而更新指纹；先比较并批准新输入。

`plan` 读取 JSON 清单、规范化 JSON 快照，以及相对于 `--root`、在 `manifest.sources` 中明确列出的文件。它不递归目录，也不搜索主目录。默认输出为 JSON。`--lang en|ru|de|es` 仅改变人类可读消息；字段名和诊断代码保持稳定。顶层和每个命令都支持 `--help`。没有应用、上传、发现或认证命令。

退出状态：

- **0：**受支持的输入范围内部一致，可供审查。
- **2：**参数或输入无效、文件不可读，或违反模式/限制。
- **3：**结构有效的输入生成受阻计划，例如冲突或范围未解决。

参数解析之后的输入失败会在 stdout 输出带 `status: invalid` 的 JSON 外层结构。参数错误会在 stderr 输出本地化用法。指纹成功时只输出摘要。文本模式下，候选编辑记录保留机器字段名，解释消息会翻译。

运行文件应保存在私有目录。重定向 stdout 会创建自己的报告，其中可能包含可识别的实体名和路径。工具自身不写任何内容。用 `python3 -m pip uninstall ha-entity-migrations` 卸载。开发者检查见 [CONTRIBUTING](../../CONTRIBUTING.md)。
