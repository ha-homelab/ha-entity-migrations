# 输入模型

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

[安装](installation.md) · [示例](examples.md)

所有文档使用 UTF-8 严格 JSON。拒绝重复键、非有限数和未知模式字段。`examples/` 中的精确示例是可执行参考。版本字段必须是整数 `1`，不能是字符串或布尔值。

## 快照

顶层对象仅含 `version` 和 `entities`。每个实体精确包含：

- `entity_id`：小写域/对象 ID，例如 `light.workbench`。
- `hardware_id`：操作员选择的私有、不透明标识符。
- `channel`：物理通道标识符，字符串形式。
- `role`：唯一逻辑用途，例如 `workbench` 或 `pump_enable`。
- `capabilities`：描述能力的唯一字符串，例如 `on_off`。

硬件/通道对标识物理端点。实体 ID、物理端点、逻辑角色各自必须唯一。物理诊断应表示为另一通道，例如 `rssi`，并赋予独立的唯一角色。角色是规划标签，不是 Home Assistant 区域、标签或设备类别。声明不是测量，工具无法对照硬件验证。

## 清单

顶层对象精确包含 `version`、`snapshot_sha256`、`sources`、`assignments` 和 `consumers`。`sources` 将相对文件名映射到 SHA-256 摘要。`assignments` 含快照中已有物理端点的完整替换实体记录。未列出的端点保持不变。加入新设备前，先把观察到的备用端点写入快照。不会隐式创建或删除硬件，而且此版本要求角色唯一。

每个消费者通过 `file` 和 RFC 6901 `pointer` 标识一个**字面量字符串值**。把 `/` 转义为 `~1`，把 `~` 转义为 `~0`；列表索引从零开始且不能有前导零。每个发现的引用都需要显式策略：

- `follows_role`：查找拥有源逻辑角色的目标。
- `follows_hardware`：保留源物理通道，使用其新实体 ID。
- `retire`：建议移除包含该引用的显式 `retire_scope` 对象。

非停用消费者还需要 `kind`（`action`、`display`、`reference`）、`allowed_roles`（非空）和 `required_capabilities`（可以为空）。动作需要 `service_pointer`。这些关卡防止把刚改作他用的泵当成照明目标。它们是声明，不是推断的意图。

停用消费者精确包含四个字段：file、pointer、policy 和 retire_scope。范围必须是非根祖先对象，只能包含对同一停用来源的引用；混合或动态引用会阻止停用。如果删除动作会留下无效的空序列，应选择整个过时自动化。工具不运行 HA 模式验证器。

## 域变化

跨 light/switch 的动作只支持 `turn_on`、`turn_off`、`toggle` 及匹配的 `homeassistant.*` 服务。自动服务转换不接受非空 `data` 或 `data_template`。有多个字面量目标的域专用服务会被阻止。服务指针必须在其动作下拥有该目标。显示域变化始终需要人工审查卡片功能；开关不能悄悄继承亮度控件。

## 边界

每文件 2 MiB；源文件总共 16 MiB；64 个文件；5,000 个实体、分配或消费者；每文件 JSON 深度 40、100,000 个值节点。标识符是最长 256 字符的非空字符串，能力/允许角色列表最多含 64 个唯一字符串。相对源路径不能向上穿越、不能为绝对路径，也不能包含符号链接。输入仅限常规文件。

文件加载器拒绝解析到同一规范路径或打开文件身份（设备/inode）的两个来源名称，包括重复路径分隔符、硬链接，以及不区分大小写文件系统上的大小写别名。保留一个来源名称并更新消费者；别名不能为同一物理文件携带不同迁移策略。内容相同的独立文件仍是有效输入。纯 `plan` API 不访问文件系统；自行构建来源映射的调用者必须在调用前执行此身份边界检查。
