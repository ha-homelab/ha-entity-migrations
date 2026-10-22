# Exemplos detalhados

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

[Modelo de entrada](model.md) · [Arquitetura](architecture.md)

Todo hardware e todos os papéis aqui são sintéticos. Recrie entradas idênticas com `python3 tools/generate_examples.py`. Nenhum comando se conecta ao Home Assistant.

## O papel de lâmpada deixa uma tomada reaproveitada

Execute o comando do README para `examples/role-swap`. Inicialmente, `plug-a/1` possui `light.workbench` e `plug-b/1` possui `switch.spare`. O manifesto atribui o papel de bomba à tomada A e o de bancada à B. A automação de iluminação usa `follows_role` e permite apenas `workbench`. Sua referência continua sendo `light.workbench` enquanto o hardware de destino muda. A ausência de edição textual é intencional, não uma migração esquecida. O campo `assignments` do relatório contém as mudanças de hardware para revisão humana.

O antigo consumidor reserva é retirado em `/1`, o segundo objeto de automação inteiro. Isso não deixa uma sequência de ações vazia. O relatório é consultivo; o programa não remove elementos do array JSON. Ao aplicar manualmente várias remoções propostas, considere o deslocamento dos índices e execute novamente a partir de um snapshot recente.

Mude a primeira política para `follows_hardware`, mantendo `workbench` como papel permitido: o plano é bloqueado com `role_not_allowed`. Ampliar a lista para incluir uma bomba altera explicitamente a intenção de forma perigosa; não é uma correção rotineira. Restaure a política correta.

## Um relé muda de light para switch

```sh
ha-entity-migrations plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change
```

As duas edições propostas alteram o destino e seu serviço `light.turn_off`. Acrescente dados de brilho à ação de origem, atualize a impressão digital aprovada e execute novamente: `service_data_review` bloqueia a conversão automática. Não descarte configurações de brilho apenas para satisfazer a ferramenta; revise o comportamento desejado.

## Um template não resolvido

Execute o mesmo comando com `examples/blocked-template`. O destino é Jinja dinâmico. A ferramenta não o avalia e retorna código 3. Um plano completo suportado exige configuração explícita com destinos literais demonstráveis; caso contrário, mantenha essa parte como migração manual documentada fora do escopo pronto. Ignorar o código de saída não resolve o template.

## Desvio e repetibilidade

Editar uma origem sem alterar seu hash no manifesto produz `stale_source`. Editar o snapshot produz `stale_snapshot`. Nenhuma edição candidata de referência é emitida para esses modelos desatualizados. Com arquivos inalterados, o resultado JSON é determinístico, exceto pelo idioma escolhido. Os arquivos de origem permanecem idênticos byte a byte.

Para um projeto real, copie o formato para uma pasta privada, verifique identidades físicas, enumere consumidores e execute o planejador. Revise todas as atribuições e edições, realize os testes próprios do HA no processo de implantação estabelecido e depois obtenha outro snapshot somente leitura para verificar o resultado. Este projeto não implementa essa implantação nem um executor de reversão.
