# 限制与审查边界

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

[架构](architecture.md) · [安全](../../SECURITY.md)

计划的准确性取决于物理设备、通道、角色声明及所提供文件。工具不会发现遗漏的仪表板、设备触发器、场景、蓝图、存于其他位置的自动化、Matter 过滤器、外部客户端或隐藏集成状态。不要把就绪报告称为完整 Home Assistant 审计。此版本要求角色唯一；多对多语义角色和组需要手动拆解。

支持 JSON 配置来源。不解释 YAML 本身、include、别名、锚点、可执行标签、自定义组件或运行时生成的模板。规范化不在本版本范围内，而且可能丢失语义；保留原件并审查等价性。即使受支持的 JSON，也不会对照 Home Assistant 完整配置模式进行检查。删除显式消费者对象可能留下无效父对象；应审查父对象，并在正常预发布流程中运行 HA 配置检查器。

能力和允许角色是显式约束，不是推断的安全性。工具无法知道以前无害的插座现在接了泵或车库门驱动器。报告的继电器状态不证明触点或负载行为。不要仅为验证名称而执行全屋脚本或给正在工作的电器断电重启。物理调试属于独立、受控流程。

此版本不应用计划、不重命名注册表实体、不修改唯一 ID、不重载 HA、不重启控制器、不停用集成，也不回滚变更。返回的操作是建议，不是可执行 JSON Patch。如果人工应用，需取得新快照并在每项已审查变更后验证，因为索引和版本可能已变化。哈希不提供签名或访问控制。

报告可能含私有名称和标识符，不应放进公开 Git、问题跟踪器或 CI 产物。公开示例使用合成设备，不声称现场验证。诊断按设计阻止计划；没有强制标志、忽略列表或隐藏宽松模式。
