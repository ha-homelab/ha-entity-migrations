# Arquitetura e contrato do relatório

<!-- language-navigation:start -->
<p dir="ltr">
<a href="../en/architecture.md" lang="en" dir="ltr">English</a> ·
<a href="../ar/architecture.md" lang="ar" dir="rtl">العربية</a> ·
<a href="../bn/architecture.md" lang="bn" dir="ltr">বাংলা</a> ·
<a href="../cs/architecture.md" lang="cs" dir="ltr">Čeština</a> ·
<a href="../de/architecture.md" lang="de" dir="ltr">Deutsch</a> ·
<a href="../es/architecture.md" lang="es" dir="ltr">Español</a> ·
<a href="../fa/architecture.md" lang="fa" dir="rtl">فارسی</a> ·
<a href="../fr/architecture.md" lang="fr" dir="ltr">Français</a> ·
<a href="../he/architecture.md" lang="he" dir="rtl">עברית</a> ·
<a href="../hi/architecture.md" lang="hi" dir="ltr">हिन्दी</a> ·
<a href="../id/architecture.md" lang="id" dir="ltr">Bahasa Indonesia</a> ·
<a href="../it/architecture.md" lang="it" dir="ltr">Italiano</a> ·
<a href="../ja/architecture.md" lang="ja" dir="ltr">日本語</a> ·
<a href="../ko/architecture.md" lang="ko" dir="ltr">한국어</a> ·
<a href="../nl/architecture.md" lang="nl" dir="ltr">Nederlands</a> ·
<a href="../pl/architecture.md" lang="pl" dir="ltr">Polski</a> ·
<a href="../pt/architecture.md" lang="pt" dir="ltr">Português</a> ·
<a href="../ru/architecture.md" lang="ru" dir="ltr">Русский</a> ·
<a href="../th/architecture.md" lang="th" dir="ltr">ไทย</a> ·
<a href="../tr/architecture.md" lang="tr" dir="ltr">Türkçe</a> ·
<a href="../uk/architecture.md" lang="uk" dir="ltr">Українська</a> ·
<a href="../vi/architecture.md" lang="vi" dir="ltr">Tiếng Việt</a> ·
<a href="../zh-Hans/architecture.md" lang="zh-Hans" dir="ltr">简体中文</a> ·
<a href="../zh-Hant/architecture.md" lang="zh-Hant" dir="ltr">繁體中文</a>
</p>
<!-- language-navigation:end -->

[Modelo](model.md) · [Limitações](limitations.md)

![Fluxo de dados somente leitura](../diagrams/pipeline.svg)

`io.py` impõe limites de arquivos, caminhos e JSON, além de ponteiros exatos. `planner.py` valida as declarações, constrói mapas antes/depois, examina os valores de origem, resolve políticas explícitas e acumula diagnósticos. `cli.py` acrescenta mensagens traduzidas e imprime o relatório. `i18n.py` contém quatro catálogos completos de mensagens. Esse caminho não depende da rede nem do Home Assistant.

O analisador é deliberadamente conservador. Strings que correspondem exatamente a referências de entidades são comparadas com o snapshot. Strings com referências incorporadas ficam sem resolução. Templates em chaves ou valores e chaves de destino de dispositivo/área/rótulo ficam sem resolução mesmo quando parecem fáceis de interpretar. Campos simples de serviço não são tratados como IDs de entidade; serviços dinâmicos continuam sem resolução. Arquivos não JSON são registrados como origens não suportadas e bloqueiam o planejamento. Não se trata de um analisador geral do HA.

![Fluxo de decisões das políticas](../diagrams/policy.svg)

## Envelope JSON estável, versão 1 do esquema

`schema_version`, `tool_version`, `status`, `read_only`, `scope`, `snapshot_sha256`, `source_sha256`, `assignments`, `edits`, `diagnostics`, `language`, `summary`. Para entradas válidas, `status` é ready ou blocked. `scope` é sempre `supplied_files_only`; `read_only` é sempre true. Erros de entrada usam o envelope invalid menor descrito na instalação.

As edições têm operação, arquivo e ponteiro. `replace_reference` também contém before/after/policy; `replace_service` contém before/after; `remove_consumer` contém a referência retirada. Elas **não são JSON Patch executáveis**. Faltam semânticas de transação, deslocamento de índices e ciclo de vida do HA. Revise-as como propostas; esta versão não fornece aplicador de patches por decisão explícita.

Os diagnósticos contêm `code`, `location`, `severity` estáveis e `message` traduzida. Tanto `error` quanto `unresolved` bloqueiam um plano. Relatórios `blocked` podem conter edições candidatas para referências não afetadas, mas nenhuma constitui uma transação pronta. Modelos iniciais desatualizados ou conflitantes suprimem todas as edições candidatas de referências. As atribuições sempre refletem o modelo solicitado pelo usuário, nunca mudanças concluídas.

Os relatórios ordenam origens, atribuições, edições e diagnósticos para permitir reprodução. Não há horários atuais nem pontuações de confiança inventadas. Os hashes dos bytes comprovam qual versão da entrada foi analisada, não sua veracidade nem que um dispositivo obedecerá a um comando.
