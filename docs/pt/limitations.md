# Limitações e limites da revisão

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

[Arquitetura](architecture.md) · [Segurança](../../SECURITY.md)

Um plano só é tão preciso quanto suas declarações físicas/de canais/papéis e os arquivos fornecidos. A ferramenta não descobre painéis omitidos, gatilhos de dispositivos, cenas, blueprints, automações armazenadas em outros lugares, filtros Matter, clientes externos ou estados ocultos de integrações. Um relatório pronto não é uma auditoria completa do Home Assistant. Cada papel é único nesta versão; papéis semânticos muitos-para-muitos e grupos exigem decomposição manual.

Origens de configuração JSON são suportadas. YAML, inclusões, aliases, âncoras, tags executáveis, componentes personalizados e templates gerados em execução não são interpretados. A normalização está fora desta versão e pode perder semântica; preserve o original e revise a equivalência. Nem mesmo o JSON suportado é comparado ao esquema completo de configuração do HA. Remover um objeto consumidor explícito pode deixar um objeto pai inválido; revise-o e execute o verificador de configuração do HA no seu processo normal de homologação.

Capacidades e papéis permitidos são restrições explícitas, não segurança inferida. A ferramenta não sabe se uma bomba ou motor de garagem foi conectado a uma tomada antes inofensiva. O estado informado de um relé não comprova o comportamento do contato/carga. Não execute scripts para toda a casa nem desligue e religue um aparelho em uso apenas para validar nomes. O comissionamento físico exige um procedimento controlado separado.

Esta versão não aplica planos, renomeia entidades do registro, altera IDs únicos, recarrega o HA, reinicia controladores, retira integrações ou reverte mudanças. As operações retornadas são consultivas, não JSON Patch executáveis. Para aplicá-las manualmente, obtenha um novo snapshot e verifique após cada alteração revisada: índices e versões podem ter mudado. Hashes não fornecem assinaturas nem controle de acesso.

Os relatórios podem conter nomes e identificadores privados. Não os coloque em Git público, rastreadores de issues ou artefatos de CI. Os exemplos públicos usam dispositivos sintéticos e não alegam validação em campo. Diagnósticos bloqueiam o plano por projeto; não há opção de forçar, lista de exclusão nem modo permissivo oculto.
