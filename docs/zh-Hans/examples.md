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

[输入模型](model.md) · [架构](architecture.md)

这里的所有硬件和角色都是合成示例。用 `python3 tools/generate_examples.py` 可重建相同输入。没有任何命令会连接 Home Assistant。

## 灯具角色离开改作他用的插座

运行 README 中针对 `examples/role-swap` 的命令。最初 `plug-a/1` 拥有 `light.workbench`，`plug-b/1` 拥有 `switch.spare`。清单把泵角色分配给插座 A，把工作台角色分配给插座 B。照明自动化使用 `follows_role`，只允许 `workbench`。其实体引用仍为 `light.workbench`，而目标硬件改变。不产生文本编辑是预期结果，并非遗漏迁移。报告的 `assignments` 包含供人工审查的硬件变更。

原来的备用消费者在 `/1` 处停用，即整个第二个自动化对象。因此不会留下空动作序列。报告仅提供建议，程序不会删除任何 JSON 数组元素。如果手动应用多项建议的数组删除，应考虑索引偏移，并用新快照重新运行。

将第一条策略改为 `follows_hardware`，但允许角色仍保留 `workbench`：计划将因 `role_not_allowed` 受阻。扩大允许角色列表以包含泵，是显式且危险的意图变更，不是清除错误的常规方法。应恢复正确策略。

## 继电器从 light 改为 switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

两项候选编辑分别更改目标及其 `light.turn_off` 服务。向源动作添加亮度数据，更新已批准的源指纹并重新运行：`service_data_review` 会阻止自动转换。不要仅为了让工具通过而删除亮度设置，应审查期望行为。

## 未解决的模板

使用 `examples/blocked-template` 运行相同命令。目标是动态 Jinja。工具不求值，并返回代码 3。完整且受支持的计划需要显式配置和可证明的字面量目标；否则应把它保留为已记录、位于就绪范围外的手动迁移。忽略退出代码无法解决模板。

## 漂移与可重复性

修改来源却不修改清单哈希会产生 `stale_source`。修改快照会产生 `stale_snapshot`。这些过期模型不会输出候选引用编辑。文件未改变时，除了所选语言，JSON 结果是确定性的。源文件逐字节保持不变。

用于真实项目时，将格式复制到私有文件夹，核实物理身份，列出消费者，再运行规划器。审查全部分配和编辑，在既定部署流程中执行 HA 自身检查，然后生成新的只读快照验证结果。本项目不实现该部署或回滚执行器。
