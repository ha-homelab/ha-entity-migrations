# Instalação e CLI

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

[Índice da documentação](../../README.md#documentation)

Use Python 3.11 ou mais recente. Crie e ative um ambiente virtual dedicado e execute `python3 -m pip install -e .` na cópia do repositório. O pacote não tem dependências de execução; o pip pode obter seu backend de construção. Para uma máquina offline, prepare antecipadamente o wheel e as dependências de construção. Verifique a instalação selecionada com `ha-entity-migrations --version`, que informa a versão instalada do pacote.

A CLI tem dois comandos, com uma opção global de idioma antes do comando:

```sh
ha-entity-migrations --lang ru fingerprint examples/domain-change/snapshot.json
ha-entity-migrations --lang en plan --manifest examples/domain-change/manifest.json --snapshot examples/domain-change/snapshot.json --root examples/domain-change --format text
```

`fingerprint` imprime o SHA-256 em minúsculas dos bytes exatos do arquivo. Não valida o arquivo como JSON. As impressões digitais de snapshot e origens no manifesto devem corresponder exatamente aos arquivos, inclusive espaços. Não atualize uma impressão digital só para descartar um desvio inesperado; compare e aprove a nova entrada primeiro.

`plan` lê um manifesto JSON, um snapshot JSON normalizado e somente os arquivos explicitamente indicados em `manifest.sources`, relativos a `--root`. Não percorre diretórios recursivamente nem pesquisa sua pasta pessoal. A saída padrão é JSON. Apenas mensagens humanas mudam com `--lang en|ru|de|es`; nomes de campos e códigos diagnósticos permanecem estáveis. `--help` existe no nível principal e para cada comando. Não há comandos para aplicar, enviar, descobrir ou autenticar.

Estado de saída:

- **0:** o escopo de entrada suportado é internamente consistente e está pronto para revisão.
- **2:** argumentos/entrada inválidos, arquivo ilegível ou violação de esquema/limite.
- **3:** uma entrada estruturalmente válida produziu um plano bloqueado por conflito ou escopo não resolvido.

Falhas de entrada após a análise dos argumentos produzem um envelope JSON em stdout com `status: invalid`. Erros de argumentos imprimem instruções localizadas em stderr. O cálculo bem-sucedido da impressão digital imprime apenas o resumo. No modo texto, as edições propostas mantêm os nomes de campo de máquina; as explicações são traduzidas.

Guarde arquivos operacionais em diretório privado. Redirecionar stdout cria seu próprio relatório, que pode conter nomes identificadores de entidades e caminhos. A ferramenta em si não grava nada. Desinstale com `python3 -m pip uninstall ha-entity-migrations`. Para verificações de desenvolvimento, consulte [CONTRIBUTING](../../CONTRIBUTING.md).
