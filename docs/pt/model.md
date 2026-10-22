# Modelo de entrada

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

[Instalação](installation.md) · [Exemplos](examples.md)

Todos os documentos usam JSON estrito em UTF-8. Chaves duplicadas, números não finitos e campos desconhecidos do esquema são rejeitados. Os exemplos exatos em `examples/` são a referência executável. Campos de versão devem ser o inteiro `1`, não string nem booleano.

## Snapshot

O objeto superior contém apenas `version` e `entities`. Cada entidade contém exatamente:

- `entity_id`: ID de domínio/objeto em minúsculas, como `light.workbench`.
- `hardware_id`: identificador privado opaco escolhido pelo operador.
- `channel`: identificador do canal físico, como string.
- `role`: finalidade lógica única, como `workbench` ou `pump_enable`.
- `capabilities`: strings únicas descrevendo capacidades, por exemplo `on_off`.

O par hardware/canal identifica um endpoint físico. IDs de entidades, endpoints físicos e papéis lógicos devem ser únicos, cada um em seu conjunto. Represente um diagnóstico físico como outro canal, por exemplo `rssi`, com papel próprio único. Um papel é um rótulo de planejamento, não área, rótulo ou classe de dispositivo do HA. Essas declarações não são medições; a ferramenta não pode verificá-las no hardware.

## Manifesto

O objeto superior tem exatamente `version`, `snapshot_sha256`, `sources`, `assignments` e `consumers`. `sources` relaciona nomes de arquivos relativos a resumos SHA-256. `assignments` contém registros completos de substituição para endpoints físicos já presentes no snapshot. Endpoints não listados ficam inalterados. Para incluir um dispositivo, adicione primeiro seu endpoint reserva observado ao snapshot. Não há criação ou exclusão implícita de hardware e esta versão exige papéis únicos.

Cada consumidor identifica um **valor de string literal** por `file` e um `pointer` RFC 6901. Escape `/` como `~1` e `~` como `~0`; índices de listas começam em zero, sem zeros à esquerda. Toda referência encontrada exige política explícita:

- `follows_role`: encontrar o destino que possui o papel lógico da origem.
- `follows_hardware`: manter o canal físico de origem e usar seu novo ID de entidade.
- `retire`: propor a remoção do objeto explícito `retire_scope` contendo a referência.

Consumidores não retirados também exigem `kind` (`action`, `display`, `reference`), `allowed_roles` (não vazio) e `required_capabilities` (possivelmente vazio). Ações exigem `service_pointer`. Essas barreiras impedem o uso de uma bomba reaproveitada como destino de iluminação. São declarações, não intenção inferida.

Consumidores retirados têm exatamente quatro campos: file, pointer, policy e retire_scope. O escopo deve ser um objeto ancestral diferente da raiz. Pode conter apenas referências à mesma origem retirada; referências mistas ou dinâmicas o bloqueiam. Escolha uma automação obsoleta inteira se remover uma ação deixaria uma sequência vazia inválida. A ferramenta não executa o validador de esquema do HA.

## Mudanças de domínio

Para ações entre light/switch, só são suportados `turn_on`, `turn_off`, `toggle` e serviços `homeassistant.*` correspondentes. Não se aceitam `data` nem `data_template` não vazios na conversão automática. Um serviço específico de domínio com múltiplos destinos literais é bloqueado. O ponteiro de serviço deve possuir o destino dentro de sua ação. Mudanças de domínio de exibição sempre exigem revisão manual dos recursos do cartão; um interruptor não pode herdar silenciosamente controles de brilho.

## Limites

2 MiB por arquivo; 16 MiB de origens combinadas; 64 arquivos; 5.000 entidades, atribuições ou consumidores; profundidade JSON 40 e 100.000 nós de valor por arquivo. Identificadores são strings não vazias com até 256 caracteres; listas de capacidades/papéis permitidos têm até 64 strings únicas. Caminhos relativos não podem subir diretórios, ser absolutos nem conter links simbólicos. Apenas arquivos regulares são aceitos.

O carregador rejeita dois nomes de origem que resolvam para o mesmo caminho canônico ou identidade de arquivo aberto (dispositivo/inode). Isso inclui separadores repetidos, links físicos e aliases por maiúsculas/minúsculas em sistemas sem essa distinção. Mantenha um nome e atualize seus consumidores; aliases não podem atribuir políticas diferentes a um mesmo arquivo físico. Arquivos independentes com conteúdo idêntico permanecem válidos. A API pura `plan` não acessa o sistema de arquivos: quem montar seu próprio mapa de origens deve impor esse limite de identidade antes de chamá-la.
