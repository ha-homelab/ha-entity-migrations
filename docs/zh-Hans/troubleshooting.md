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

[安装](installation.md) · [限制](limitations.md)

**找不到命令：**激活安装时使用的同一个虚拟环境。尝试 `python3 -m ha_entity_migrations --version`；不要只为绕过路径不匹配而安装到系统 Python。

**退出 2，schema_invalid：**对照可执行示例及[输入模型](model.md)检查键。未知字段是错误。版本为整数 1；通道标识符为字符串。每条动作策略都需要服务指针。快照包含实体，清单包含分配和消费者，两者不可互换。

**退出 2，duplicate_source：**两个来源名称标识同一物理文件。在 `sources` 中保留一个规范名称，并让全部消费者的 `file` 字段指向它。去掉重复分隔符或硬链接/大小写别名；不要给别名第二条策略。内容相同的独立文件仍受支持。

**stale_snapshot / stale_source：**将实际变化与批准的来源比较。只有审查后才能使用指纹命令。空白变化也影响哈希。不要只为匹配旧哈希而指向过期副本。

**source_collision / destination_collision：**物理通道、角色或实体 ID 重复。显式表达角色互换的双方，并检查未变化端点是否仍保留期望的目标 ID。

**role_not_allowed / capability_missing：**消费者将指向不合适的负载或失去能力。确认应跟随角色还是硬件。不要自动扩大 allowed_roles，也不要声称硬件具有实际上不存在的能力。灯具换成开关继电器后无法调光。

**missing_policy / unmodeled_reference：**盘点被引用端点，确认用途后再添加显式消费者声明。旧历史字符串可能不在活动范围；应有意从计划范围移除该文件、记录排除，并重新生成来源契约。

**dynamic_reference / embedded_reference / indirect_target：**此版本无法证明映射。单独审查 Jinja 或组/区域/标签行为，或提供显式、规范化的字面量配置。程序从不执行模板。

**display_domain_review / service_data_review / mixed_action_targets：**检查卡片功能、动作参数和目标批次。应在另行审查的来源修改中拆分跨域动作，不要只改变服务域。

**retire_scope_mixed / overlapping_edits：**选择一致且过时的消费者对象，不能有无关引用。不要仅删除动作中的 entity_id，这可能产生过宽目标或无效配置。程序不会自动应用停用。

**unsupported_source：**只能规划 JSON。YAML、二进制及其他文件不会被悄悄跳过。显式规范化的 JSON 副本可能有助于分析，但任何真实编辑前必须与原件比较。

报告问题时使用最小合成输入、工具/Python 版本、退出代码和诊断代码。绝不附上原始家庭导出或 API 凭据。
