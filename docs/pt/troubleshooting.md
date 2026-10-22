# Solução de problemas

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

[Instalação](installation.md) · [Limitações](limitations.md)

**Comando não encontrado:** ative o mesmo ambiente virtual usado na instalação. Tente `python3 -m ha_entity_migrations --version`; não instale no Python do sistema apenas para contornar um caminho incorreto.

**Saída 2, schema_invalid:** compare suas chaves ao exemplo executável e ao [modelo de entrada](model.md). Campos desconhecidos são erros. Versões são o inteiro 1; identificadores de canal são strings. Cada política de ação precisa do ponteiro de serviço. Um snapshot tem entidades; um manifesto tem atribuições e consumidores. Os arquivos não são intercambiáveis.

**Saída 2, duplicate_source:** dois nomes identificam um arquivo físico. Mantenha um nome canônico em `sources` e atualize todos os campos `file` de consumidores. Remova separadores duplicados e aliases de link físico/maiúsculas; não atribua uma segunda política ao alias. Arquivos separados com conteúdo idêntico continuam suportados.

**stale_snapshot / stale_source:** compare as mudanças reais à origem aprovada. Use fingerprint somente após revisá-las. Espaços afetam o hash. Não aponte para uma cópia desatualizada só para fazer o hash antigo corresponder.

**source_collision / destination_collision:** há um canal físico, papel ou ID de entidade duplicado. Expresse explicitamente os dois lados de uma troca de papéis e confira se um endpoint inalterado mantém o ID de destino desejado.

**role_not_allowed / capability_missing:** o consumidor atingiria uma carga inadequada ou perderia uma capacidade. Confirme se deve seguir o papel ou o hardware. Não amplie automaticamente allowed_roles nem declare capacidades que o hardware não tem. Uma luz substituída por relé liga/desliga não pode ajustar brilho.

**missing_policy / unmodeled_reference:** inventarie o endpoint referenciado e acrescente uma declaração explícita de consumidor só após confirmar a finalidade. Uma string antiga de histórico pode estar fora do escopo ativo; exclua deliberadamente esse arquivo do escopo, documente e regenere o contrato das origens.

**dynamic_reference / embedded_reference / indirect_target:** esta versão não pode comprovar o mapeamento. Revise Jinja ou o comportamento de grupos/áreas/rótulos separadamente, ou forneça configuração literal normalizada explícita. O programa nunca executa um template.

**display_domain_review / service_data_review / mixed_action_targets:** inspecione recursos de cartões, parâmetros de ações e lotes de destinos. Divida uma ação multidomínio em uma mudança de origem revisada separadamente; não altere apenas o domínio do serviço.

**retire_scope_mixed / overlapping_edits:** escolha um objeto consumidor obsoleto coerente sem referências alheias. Não exclua apenas entity_id de uma ação: isso pode criar um destino amplo ou configuração inválida. O programa não aplica retiradas automáticas.

**unsupported_source:** somente JSON pode ser planejado. YAML, binários e outros arquivos não são ignorados silenciosamente. Uma cópia JSON explicitamente normalizada pode ajudar na análise, mas deve ser comparada ao original antes de qualquer edição real.

Relate bugs com entrada sintética mínima, versões da ferramenta/Python, código de saída e códigos diagnósticos. Nunca anexe exportação doméstica bruta nem credenciais de API.
